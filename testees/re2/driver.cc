// testees/re2/driver.cc -- the RE2 batched in-process timing driver.
//
// Implements the DRIVER PROTOCOL in pcrecbench/adapters.py verbatim; read
// that first (and testees/pcre2/driver.c, the reference implementation
// this file's loop shape is deliberately identical to -- same argv, same
// per-subject clock discipline, same find-all advance rule -- so a
// difference between RE2's and pcre2's numbers is the ENGINE, not the
// harness).
//
// WHY A DIRECT RE2 C++ DRIVER, NOT `cre2`. docs/dev/research/2026-09-12-
// b42-engine-landscape.md (2), CLOSED: `cre2` needs a four-package
// autotools bootstrap this box does not have to build a project that has
// never once been release-tagged, while `libre2-dev` is already installed
// and pkg-config-discoverable, and the driver protocol imposes NO
// language constraint -- it specifies argv/stdout SHAPE only. This file
// is built by `prepare()` with its own g++/pkg-config step (testees/re2/
// adapter.py), never through pcrecbench/driverrun.py's generic
// build_driver() helper, which assumes a C compiler.
//
// ENCODING: every RE2 object this driver builds -- UNLESS `--encoding
// utf8` is passed ([B77] U2, the `re2-utf8` config only; utf8_set_v1.md
// 7.1) -- uses RE2::Options::EncodingLatin1 -- BYTE mode, not RE2's UTF-8 default. This
// matches the project's byte-level convention every other adapter already
// uses (pcre2's driver compiles with no PCRE2_UTF option; pcrec's own byte
// engine is its default route) and is a real capability consequence, not
// a cosmetic choice: RE2's DEFAULT UTF-8 mode raises ErrorBadUTF8 on a
// lone byte >= 0x80 that is not part of a valid UTF-8 sequence, which
// would make family 12's (`binary-nonutf8`) non-UTF-8 pattern/subject
// members refuse for a reason that has nothing to do with the capability
// the family exists to measure. Latin1 mode treats every byte as its own
// codepoint, exactly as pcre2's byte-mode and pcrec's byte engine already
// do -- stated here once rather than left for a reader to discover as an
// unexplained option flag. testees/re2/CLAUDE.md states this decision and
// its consequence for the `re2-longest`/`re2-default` roster.
//
// consumed_length: the LENGTH ARGUMENT this driver passed and RE2 accepted,
// i.e. the whole subject -- RE2's Match() takes an explicit endpos and
// exposes no scan high-water mark, the same shape as pcre2_match's size_t
// length argument. Same convention, same caveat: "no byte was withheld or
// refused", never "the engine looked at every byte". testees/re2/CLAUDE.md
// states this where a reader of the numbers will find it.
//
// `giveup:<code>` NEVER FIRES FROM THIS DRIVER. RE2's public Match() API
// returns a plain bool; unlike pcre2_match's negative resource-limit
// codes (MATCHLIMIT, DEPTHLIMIT, HEAPLIMIT) there is no per-call signal
// that RE2 declined to keep searching -- RE2 is a linear-time automaton
// simulation with nothing to decline (docs/design/capability_set_v1.md
// 5.4's own finding: a DFA-cache-flush-and-retry under `max_mem` pressure
// is a graceful MATCH-TIME MECHANISM change, not a per-call refusal the
// caller can observe). So this driver's only per-subject answers are
// `match` / `nomatch` / `timedout` (this driver's own alarm) -- never
// `giveup:*`. Stated here so a reader does not go looking for a giveup
// code this engine structurally cannot report through this API.

#include <re2/re2.h>

#include <csignal>
#include <csetjmp>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <string>
#include <vector>

using absl::string_view;

// ------------------------------------------------------------- clock/io

/* [B77] U1: the find-all EMPTY-MATCH advance under --utf8 -- pcrec
 * match_api.md S3.1.1's NORMATIVE utf8 rule, the same one
 * pcrecbench/oracle_pcre2.py's next_start() and every other driver apply:
 * from pos + 1, skip every byte in 0x80-0xBF, stop at the first byte outside
 * that range or at n. Without --utf8 the advance stays start + 1. */
static size_t utf8_next_start(const unsigned char *b, size_t n, size_t pos) {
    size_t p = pos + 1;
    while (p < n && (b[p] & 0xC0u) == 0x80u) p++;
    return p;
}

static double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

static void die(const char *what) {
    std::printf("error\t%s\n", what);
    std::fflush(stdout);
    std::exit(2);
}

static bool slurp(const char *path, std::string *out) {
    FILE *f = std::fopen(path, "rb");
    if (!f) {
        std::printf("error\tfopen %s: %s\n", path, std::strerror(errno));
        return false;
    }
    if (std::fseek(f, 0, SEEK_END) != 0) { std::fclose(f); return false; }
    long sz = std::ftell(f);
    if (sz < 0) { std::fclose(f); return false; }
    std::rewind(f);
    out->resize((size_t)sz);
    if (sz > 0 && std::fread(&(*out)[0], 1, (size_t)sz, f) != (size_t)sz) {
        std::fclose(f);
        return false;
    }
    std::fclose(f);
    return true;
}

// ------------------------------------------------- the per-subject alarm

static sigjmp_buf timeout_jmp;
static volatile sig_atomic_t timed_out;

static void on_alarm(int sig) {
    (void)sig;
    timed_out = 1;
    siglongjmp(timeout_jmp, 1);
}

// ---------------------------------------------------------------- subjects

struct Subject {
    std::string id;
    std::string buf;
};

static bool load_list(const char *path, std::vector<Subject> *out) {
    FILE *f = std::fopen(path, "r");
    if (!f) return false;
    char line[8192];
    while (std::fgets(line, sizeof line, f)) {
        size_t len = std::strlen(line);
        while (len > 0 && (line[len - 1] == '\n' || line[len - 1] == '\r'))
            line[--len] = 0;
        if (len == 0) continue;
        char *tab = std::strchr(line, '\t');
        if (!tab) continue;
        *tab = 0;
        Subject s;
        s.id = line;
        if (!slurp(tab + 1, &s.buf)) { std::fclose(f); return false; }
        out->push_back(std::move(s));
    }
    std::fclose(f);
    return true;
}

// -------------------------------------------------------- error code name
//
// N2 3's "structural observation": RE2 gives a CLOSED ErrorCode enum, so
// the ADAPTER (testees/re2/adapter.py) declares `refusal_class`
// (docs/design/capability_set_v1.md 5.5) by reading the bracketed name
// this driver embeds in its `error` line, the same "adapter classifies,
// driver reports structurally" split testees/pcre2/adapter.py already
// uses for its own `giveup:<code>` lines. This function only renders the
// name; the class MAPPING lives in adapter.py, one place, not duplicated
// here.
static const char *error_code_name(RE2::ErrorCode code) {
    switch (code) {
        case RE2::NoError: return "NoError";
        case RE2::ErrorInternal: return "ErrorInternal";
        case RE2::ErrorBadEscape: return "ErrorBadEscape";
        case RE2::ErrorBadCharClass: return "ErrorBadCharClass";
        case RE2::ErrorBadCharRange: return "ErrorBadCharRange";
        case RE2::ErrorMissingBracket: return "ErrorMissingBracket";
        case RE2::ErrorMissingParen: return "ErrorMissingParen";
        case RE2::ErrorUnexpectedParen: return "ErrorUnexpectedParen";
        case RE2::ErrorTrailingBackslash: return "ErrorTrailingBackslash";
        case RE2::ErrorRepeatArgument: return "ErrorRepeatArgument";
        case RE2::ErrorRepeatSize: return "ErrorRepeatSize";
        case RE2::ErrorRepeatOp: return "ErrorRepeatOp";
        case RE2::ErrorBadPerlOp: return "ErrorBadPerlOp";
        case RE2::ErrorBadUTF8: return "ErrorBadUTF8";
        case RE2::ErrorBadNamedCapture: return "ErrorBadNamedCapture";
        case RE2::ErrorPatternTooLarge: return "ErrorPatternTooLarge";
        default: return "ErrorUnknown";
    }
}

// ------------------------------------------------------------------- main

int main(int argc, char **argv) {
    const char *pattern_path = NULL, *list_path = NULL, *mode = "search";
    volatile long iters = 1, subject_timeout = 0, skip = 0;
    long compile_trials = 1;
    volatile int find_all = 0;
    volatile int utf8_adv = 0;   // [B77] U1: --utf8, the protocol flag
    int longest = 0;
    int enc_utf8 = 0;            // [B77] U2: --encoding utf8 (the ENGINE's)
    int64_t max_mem = RE2::Options::kDefaultMaxMem;

    for (int i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!std::strcmp(a, "--pattern") && i + 1 < argc) pattern_path = argv[++i];
        else if (!std::strcmp(a, "--list") && i + 1 < argc) list_path = argv[++i];
        else if (!std::strcmp(a, "--mode") && i + 1 < argc) mode = argv[++i];
        else if (!std::strcmp(a, "--iters") && i + 1 < argc) iters = std::strtol(argv[++i], NULL, 10);
        else if (!std::strcmp(a, "--compile-trials") && i + 1 < argc) compile_trials = std::strtol(argv[++i], NULL, 10);
        else if (!std::strcmp(a, "--subject-timeout") && i + 1 < argc) subject_timeout = std::strtol(argv[++i], NULL, 10);
        else if (!std::strcmp(a, "--skip") && i + 1 < argc) skip = std::strtol(argv[++i], NULL, 10);
        else if (!std::strcmp(a, "--find-all")) find_all = 1;
        else if (!std::strcmp(a, "--utf8")) utf8_adv = 1;
        else if (!std::strcmp(a, "--longest")) longest = 1;
        else if (!std::strcmp(a, "--encoding") && i + 1 < argc) {
            const char *e = argv[++i];
            if (!std::strcmp(e, "utf8")) enc_utf8 = 1;
            else if (!std::strcmp(e, "latin1")) enc_utf8 = 0;
            else { std::printf("error\tunknown encoding %s\n", e); return 2; }
        }
        else if (!std::strcmp(a, "--max-mem") && i + 1 < argc) max_mem = std::strtoll(argv[++i], NULL, 10);
        else { std::printf("error\tunknown argument %s\n", a); return 2; }
    }
    if (!pattern_path) die("--pattern is required");
    if (iters < 1) iters = 1;

    std::setvbuf(stdout, NULL, _IOLBF, 0);

    // RE2 has no runtime-queryable release version (no RE2_VERSION symbol,
    // no version-string API -- testees/re2/CLAUDE.md states the convention
    // this project uses instead: the installed package's own pkg-config
    // Version, probed by the ADAPTER, not typed here). This driver reports
    // only what it can probe FROM THE LIBRARY ITSELF: nothing structural
    // exists to probe, so `version` is supplied by the adapter's `info`
    // line convention -- see adapter.py's describe(). Nothing printed here
    // duplicates or contradicts that; this driver simply has no version
    // fact of its own to add.
    std::printf("info\tlongest_match\t%s\n", longest ? "on" : "off");
    std::printf("info\tmax_mem\t%lld\n", (long long)max_mem);
    // [B77] U2: printed ONLY under --encoding utf8, so a byte config's
    // driver output is unchanged line for line.
    if (enc_utf8) std::printf("info\tencoding\tutf8\n");

    std::string pat;
    if (!slurp(pattern_path, &pat)) {
        std::printf("error\tcannot read pattern %s\n", pattern_path);
        return 2;
    }

    RE2::Options opts;
    // [B77] U2 (utf8_set_v1.md 7.1): `--encoding utf8` restores RE2's OWN
    // default, EncodingUTF8, for the `re2-utf8` config; every other config
    // stays Latin-1 (the header's ENCODING paragraph, unchanged).
    opts.set_encoding(enc_utf8 ? RE2::Options::EncodingUTF8
                               : RE2::Options::EncodingLatin1);
    opts.set_longest_match(longest != 0);
    opts.set_max_mem(max_mem);
    opts.set_log_errors(false);  // errors read structurally, never parsed from stderr

    RE2 * volatile re = NULL;
    for (long t = 1; t <= compile_trials; t++) {
        double t0 = now();
        RE2 *r = new RE2(string_view(pat), opts);
        double t1 = now();
        std::printf("compile\t%ld\tcompile\t%.9f\n", t, t1 - t0);
        if (!r->ok()) {
            std::printf("error\tRE2 construction failed [%s]: %s\n",
                       error_code_name(r->error_code()), r->error().c_str());
            delete r;
            return 3;
        }
        delete re;
        re = r;
    }

    // engine_metadata, `pattern`-scoped (record_schema.md 7 rule 2):
    // declared in testees/re2/adapter.py.
    std::printf("info\tncapturegroups\t%d\n", re->NumberOfCapturingGroups());
    std::printf("info\tprogram_size\t%d\n", re->ProgramSize());
    std::printf("info\treverse_program_size\t%d\n", re->ReverseProgramSize());

    if (!list_path) {
        delete re;
        std::fflush(stdout);
        return 0;  // compile-only run
    }

    std::vector<Subject> subs;
    if (!load_list(list_path, &subs)) {
        std::printf("error\tcannot read subject list %s\n", list_path);
        return 2;
    }

    const RE2::Anchor anchor =
        !std::strcmp(mode, "match") ? RE2::ANCHOR_BOTH : RE2::UNANCHORED;
    const int ncap = re->NumberOfCapturingGroups();
    const int nsub = ncap + 1;  // submatch[0] is the overall match

    struct sigaction sa;
    std::memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);

    std::vector<string_view> submatch(nsub);
    char caps[4096];

    for (volatile size_t i = (size_t)skip; i < subs.size(); i++) {
        Subject &s = subs[i];
        string_view text(s.buf);
        volatile long first_s = -1, first_e = -1, nmatch = -1;
        volatile int matched_final = 0;
        volatile double elapsed = 0.0;
        volatile int nsub_out = 0;

        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            double t0 = now();
            for (long it = 0; it < iters; it++) {
                first_s = first_e = -1;
                nsub_out = 0;
                if (find_all) {
                    size_t pos = 0;
                    long count = 0;
                    for (;;) {
                        if (pos > text.size()) break;
                        bool m = re->Match(text, pos, text.size(),
                                          RE2::UNANCHORED, submatch.data(),
                                          nsub);
                        if (!m) break;
                        size_t start = (size_t)(submatch[0].data() - text.data());
                        size_t end = start + submatch[0].size();
                        if (first_s < 0) {
                            first_s = (long)start;
                            first_e = (long)end;
                            nsub_out = nsub;
                            matched_final = 1;
                        }
                        count++;
                        // pcrec match_api.md S3.1's find-all advance rule
                        // (adopted by reference, KB-17, testees/pcre2/
                        // driver.c's own comment): off the match's own
                        // reported START, never off the scan position.
                        // Under --utf8 ([B77] U1): the next CHARACTER
                        // boundary, not start + 1.
                        pos = (end > start) ? end
                            : utf8_adv ? utf8_next_start(
                                  reinterpret_cast<const unsigned char *>(text.data()),
                                  text.size(), start)
                                       : start + 1;
                    }
                    nmatch = count;
                    matched_final = (count > 0);
                } else {
                    bool m = re->Match(text, 0, text.size(), anchor,
                                      submatch.data(), nsub);
                    matched_final = m ? 1 : 0;
                    if (m) {
                        first_s = (long)(submatch[0].data() - text.data());
                        first_e = first_s + (long)submatch[0].size();
                        nsub_out = nsub;
                    }
                }
            }
            elapsed = now() - t0;
            if (subject_timeout > 0) alarm(0);
        }

        if (timed_out) {
            std::printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                       s.id.c_str(), (long)iters, (double)elapsed);
            continue;
        }

        const char *answer;
        char sbuf[32], ebuf[32], nbuf[32];
        int ncaps_out = 0;

        if (matched_final) {
            answer = "match";
            // CAPS: 1-based groups 1..ncap (group 0, the overall match, is
            // NOT included -- the same convention testees/pcre2/driver.c's
            // emit_caps uses), "-1:-1" for an unset (non-participating)
            // group, "-" when there are no capturing groups at all.
            size_t off = 0;
            caps[0] = 0;
            for (int g = 1; g < nsub_out; g++) {
                long gs = submatch[g].data()
                             ? (long)(submatch[g].data() - text.data())
                             : -1;
                long ge = submatch[g].data() ? gs + (long)submatch[g].size() : -1;
                int k = std::snprintf(caps + off, sizeof(caps) - off, "%s%ld:%ld",
                                     g > 1 ? "," : "", gs, ge);
                if (k < 0 || (size_t)k >= sizeof(caps) - off) break;
                off += (size_t)k;
            }
            if (!caps[0]) { caps[0] = '-'; caps[1] = 0; }
            ncaps_out = ncap;
            std::snprintf(sbuf, sizeof sbuf, "%ld", (long)first_s);
            std::snprintf(ebuf, sizeof ebuf, "%ld", (long)first_e);
        } else {
            answer = "nomatch";
            std::strcpy(sbuf, "-");
            std::strcpy(ebuf, "-");
            caps[0] = '-'; caps[1] = 0;
        }
        if (find_all && nmatch >= 0)
            std::snprintf(nbuf, sizeof nbuf, "%ld", (long)nmatch);
        else
            std::strcpy(nbuf, "-");

        // consumed_length: the length RE2 was given and accepted -- the
        // whole subject, exactly as testees/pcre2/driver.c's own
        // convention. See this file's header and testees/re2/CLAUDE.md.
        std::printf("subject\t%s\t%s\t%s\t%s\t%d\t%zu\t%ld\t%.9f\t%s\t%s\n",
                   s.id.c_str(), answer, sbuf, ebuf, ncaps_out,
                   s.buf.size(), (long)iters, (double)elapsed, nbuf, caps);
    }

    delete re;
    std::fflush(stdout);
    return 0;
}
