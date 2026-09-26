/* testees/vectorscan/driver.c -- the Vectorscan (Hyperscan-ABI-compatible
 * fork) batched in-process timing driver, BLOCK MODE, serving TWO configs:
 * `vectorscan-block-nosom` (NO SOM, boolean grain, capability_set_v1.md 5.6
 * option (B), Frank's Q3 ruling, 2026-09-16) and, since [B92]
 * (docs/dev/plan.md, Frank's ruling on 5.6 option (A) narrowed to what the
 * EXISTING protocol already expresses), `vectorscan-block-som`
 * (`--som`, `HS_FLAG_SOM_LEFTMOST` -- FULL grain: real spans, real
 * NMATCHES).
 *
 * Implements the DRIVER PROTOCOL in pcrecbench/adapters.py. `--som` ABSENT
 * (the `nosom` config): THIS DRIVER NEVER REPORTS A MATCH SPAN, byte for
 * byte as it always has -- `testees/vectorscan/CLAUDE.md` states in full
 * what that costs (a real, MEASURED gap in `harness.outcome_for` -- every
 * genuine match is scored `wrong-span-or-captures`, never `matched-as-
 * expected`); read that file before reading numbers out of a report row
 * for this testee. `--som` PRESENT: see "SOM MODE" below -- a real span
 * and a real find-all count, at FULL grain, with Hyperscan's genuine
 * leftmost-longest divergence from this project's leftmost-first oracle
 * left VISIBLE rather than hidden.
 *
 * WHY DIRECT LINKING, LIKE testees/onig/. This box has `libvectorscan-dev`
 * (5.4.11-2ubuntu2, `/usr/include/hs/*.h`, `pkg-config libhs` verified
 * working) -- so this driver `#include <hs/hs.h>` and links `-lhs`. No
 * dlopen, no hand-declared prototypes, no probed constants: every symbol
 * and value below is the real header's (`HS_FLAG_*`/`HS_MODE_*` grepped
 * live off this box's installed hs_compile.h/hs_common.h, 2026-09-17).
 *
 * COMPILE COST: one phase, `compile` -- `hs_compile()`, timed in-driver.
 * Vectorscan/Hyperscan's `hs_compile()` is the roster's most AOT-shaped
 * step short of pcrec's own real compiler+linker (docs/dev/research/
 * 2026-09-12-b42-engine-landscape.md 's own line 309: "explicitly
 * documented as the heavyweight, famously-slow-relative-to-match-speed
 * step... a huge compile-time investment for fast scanning"). Scratch
 * allocation (`hs_alloc_scratch`) happens ONCE, immediately after the
 * LAST compile trial, UNTIMED -- it is bookkeeping the harness's compile-
 * cost definition does not charge (mirrors pcre2/onig's convention of
 * timing only the engine's own semantic compile call, never driver
 * setup around it).
 *
 * TWO FORMS. Hyperscan block-mode `hs_scan()` has NO runtime anchoring
 * dial at all (unlike PCRE2_ANCHORED/PCRE2_ENDANCHORED, and unlike
 * Oniguruma's `onig_match`-at-a-fixed-position) -- it scans the WHOLE
 * buffer for matches starting anywhere. So the `match` regime's
 * artifact is NOT `pcrecbench.record.whole_subject_text()`'s bytes
 * (`(?:pattern)\z`, which supplies only the END anchor and relies on the
 * CALLER supplying the START anchor some other way): it is
 * `^(?:pattern)\z` -- this driver's OWN, wider wrapper, built by
 * `--form whole-subject` (mirroring testees/onig/driver.c's own
 * `--form plain|whole-subject` flag; DELIBERATELY prepending `^` rather
 * than `\A`, since neither HS_FLAG_MULTILINE nor HS_FLAG_UTF8 is ever
 * set by this driver -- under those defaults Hyperscan's documented
 * anchor list treats `^` as buffer-start, identically to `\A`).
 * `--mode`/`--form` are cross-checked exactly as onig's driver does
 * (dies loudly on disagreement rather than silently measuring the wrong
 * form).
 *
 * FLAGS: `VS_DRIVER_FLAGS` is 0 -- `HS_FLAG_UCP` is NEVER set, on the
 * MEASURED A/B in CLAUDE.md ("VS_DRIVER_FLAGS is 0"): `\p{L}` compiles
 * identically with or without it, while setting it BREAKS `\b` on five
 * real corpus patterns (40/64 corpus compiles at 0 vs 35/64 under UCP).
 * (An earlier draft of this header said UCP was set unconditionally --
 * that was the pre-A/B first cut.) `HS_FLAG_UTF8` is NEVER set: this
 * driver is byte-oriented (Vectorscan's documented default -- "ASCII by
 * default", docs/dev/research/2026-09-12-b42-engine-landscape.md, table
 * row 195), matching every OTHER testee on this roster's own default
 * 8-bit non-UTF convention and satisfying `non-utf8-subject`.
 * `HS_FLAG_SOM_LEFTMOST` is NEVER set -- the `nosom` config's entire
 * reason to exist.
 *
 * MATCHING: `hs_scan()` invokes its callback for EVERY match Hyperscan
 * finds in one pass. This driver's callback always returns 1 (stop
 * after the first) regardless of `--find-all`: at boolean grain the ONLY
 * question this driver answers is "did this pattern match the subject at
 * least once", and a non-overlapping match COUNT (`NMATCHES`) would need
 * each match's START offset to de-duplicate correctly (pcrec match_api.md
 * S3.1's advance rule -- KB-17), which HS_FLAG_SOM_LEFTMOST is what
 * supplies and this config, by construction, does not carry. `--find-all`
 * is therefore ACCEPTED (protocol compliance) but NMATCHES is always `-`
 * -- an honest gap, not a fabricated or silently-wrong count (the research
 * note's own S11 flags this precisely: "Hyperscan's natural one-pass
 * 'all ends' callback does not produce that count on its own"; building
 * the adapter-side reduction it goes on to describe is OWED, not done
 * here -- see CLAUDE.md).
 *
 * NO SPAN, EVER, WHEN `--som` IS ABSENT: START and END are ALWAYS printed
 * `-`, even on a real match (capability_set_v1.md 5.6 option (B)'s own
 * stated shape: "a Vectorscan driver reporting ANSWER=match/nomatch with
 * START=END=-"). Hyperscan's callback DOES hand this driver a real `to`
 * (end) offset on every match, and this driver deliberately never reports
 * it: printing a real END while STARTs stays `-` would be a half-measure
 * this project's own protocol comment does not describe, and would still
 * fail `harness.outcome_for`'s span comparison test (`row.end !=
 * expectation.end`) on every occurrence where the true end offset does
 * not happen to equal the oracle's -- no better than `-`, and less
 * honest about what this config actually knows. NCAPS is always 0, CAPS
 * is always `-`: Hyperscan has no capturing groups at all (`captures =
 * "off"` in configs.toml).
 *
 * consumed_length: the `length` argument passed to `hs_scan()` -- i.e.
 * the whole subject, `hs_scan`'s own `unsigned int length` parameter,
 * which this driver always sets to the subject's full byte count. Same
 * convention, same honest limit, as testees/pcre2/CLAUDE.md and
 * testees/onig/CLAUDE.md state for their engines: "no byte was withheld
 * or refused", never "the engine looked at every byte".
 *
 * GAVE-UP CODES: NONE. Vectorscan/Hyperscan's whole design is a BOUNDED
 * automaton with no backtracking and no configurable retry/depth/match
 * budget to exhaust (docs/dev/research/2026-09-12-b42-engine-landscape.md
 * line 122: "Hyperscan/Vectorscan all guarantee no catastrophic
 * backtracking") -- there is no `hs_scan()` return code documented as a
 * resource-limit REFUSAL the way PCRE2_ERROR_MATCHLIMIT or Oniguruma's
 * ONIGERR_RETRY_LIMIT_* are. `giveup_codes` is therefore the EMPTY SET:
 * `harness.classify_giveup` will bucket ANY negative `hs_scan()` return
 * this driver did not itself request (i.e. anything other than the
 * HS_SCAN_TERMINATED this driver's own callback causes by returning 1)
 * as `crashed` -- correctly, since Vectorscan structurally has nothing
 * else to report there. `--som` does not change this: HS_FLAG_SOM_LEFTMOST
 * documents no NEW resource-limit refusal at MATCH time either (the
 * refusals SOM adds are all at COMPILE time -- see "SOM MODE" below).
 *
 * ================================ SOM MODE ================================
 * [B92] (docs/dev/plan.md; Frank's ruling on docs/dev/lanes/
 * b72smalls_report.md 4 / capability_set_v1.md 5.6: option (b) of the two
 * live candidates -- wire `vectorscan-block-som` to answer the EXISTING
 * protocol shapes rather than grow a THIRD invocation mode (option (A)/OD-
 * B3, which needed a schema change and a list-valued row this project has
 * never built). `--som` is this driver's ONLY new flag; every line below
 * is reached ONLY when it is passed (`vectorscan-block-nosom`'s own argv
 * never carries it -- see testees/vectorscan/adapter.py), so the `nosom`
 * arm above is UNTOUCHED, not merely "unaffected in practice": the `if
 * (som_mode)`/`else` split below is the ONLY place the two paths fork, and
 * the `else` arm is the pre-[B92] code, byte for byte.
 *
 * COMPILE TIME: `--som` ORs `HS_FLAG_SOM_LEFTMOST` into the compile flags
 * word (both `hs_compile()` and `hs_expression_info()`) -- nothing else
 * about the compile path changes; a pattern Hyperscan refuses UNDER SOM
 * TRACKING (Hyperscan's own documented restriction: some expressions would
 * need to track an unbounded amount of match history to report a leftmost
 * start, and SOM_LEFTMOST refuses those outright at hs_compile time rather
 * than accept and misreport) takes the SAME generic `did-not-compile` path
 * every other refusal does, Vectorscan's own `hs_compile_error_t.message`
 * verbatim -- a FIRST-CLASS refusal by name, never a driver error, and no
 * new code was needed for it (see the census this lane archived under
 * docs/dev/measurements/ for which corpus patterns this actually costs).
 *
 * MATCH TIME: HS_FLAG_SOM_LEFTMOST makes Hyperscan's callback report a
 * REAL `from` (start) offset beside the `to` (end) it always reported --
 * but Hyperscan's underlying architecture is still "all-ends"
 * (capability_set_v1.md 5.6's own table: Vectorscan's declared convention
 * stays `all-ends`, not a new schema token): for a pattern like `a+`
 * scanning "aaa", the callback fires once per valid END offset (1, 2, 3),
 * each with `from=0` (SOM_LEFTMOST's own leftmost-start guarantee). A
 * single early-stopping callback (this driver's OWN `nosom` convention)
 * would report the SHORTEST completion, not the greedy-longest span a
 * leftmost-first oracle expects -- so `--som`'s callback (`on_match_som`)
 * NEVER stops early: it accumulates EVERY (from, to) pair Hyperscan
 * reports for the whole subject into a growable array, and this driver
 * reduces that FULL set itself, in two ways:
 *
 *   1. THE FIRST-MATCH SPAN (STAGE/END, always computed when >=1 match):
 *      the MINIMUM `from` over every reported match, then the MAXIMUM `to`
 *      among matches sharing that minimum `from` -- i.e. LEFTMOST, THEN
 *      LONGEST. This is a real, stated, MEASURED semantic divergence from
 *      this project's `perl-leftmost-first` oracle on any pattern where a
 *      shorter alternative would have won under backtracking precedence
 *      (`a|ab` against "ab": the oracle picks "a" [0,1); this reduction
 *      picks "ab" [0,2), because Hyperscan's all-ends scan reports BOTH
 *      completions at start 0 and this driver keeps the longest). It is
 *      NOT a bug and NOT hidden: `harness.outcome_for`'s ordinary
 *      `wrong-span-or-captures` path scores it exactly where the two
 *      conventions genuinely disagree, at FULL grain (no `grain`
 *      declaration this config needs) -- `testees/vectorscan/CLAUDE.md`
 *      names which corpus patterns this fires on.
 *   2. NMATCHES (`--find-all` only): the accumulated list is SORTED by
 *      (`from` ascending, `to` DESCENDING -- so the first entry at any
 *      given `from` is already its own longest completion, the SAME
 *      reduction rule as (1)), then walked with pcrec match_api.md S3.1's
 *      advance rule (KB-17, docs/dev/known_issues.md; the SAME rule the
 *      driver protocol's header states and every other driver in this
 *      repo implements): a cursor starts at 0; the first remaining match
 *      whose `from >= cursor` is counted, and the cursor advances to that
 *      match's `to` when the match is non-empty, else to `from + 1` (or,
 *      under `--utf8` -- [B77] U1 -- the next UTF-8 CHARACTER boundary,
 *      `utf8_next_start`, live for THIS config where it was inert on
 *      `nosom`'s span-free fast path). This is the adapter-side reduction
 *      capability_set_v1.md 5.6's own S11 note asked for and
 *      `testees/vectorscan/CLAUDE.md`'s "NMATCHES ... also honest" section
 *      named OWED -- built here, not routed around.
 *
 * A REAL, DOCUMENTED COST: `--som` always scans the WHOLE subject once per
 * `iters` pass, even for a bare boolean/first-match query with no
 * `--find-all` -- both reductions above need to see every match Hyperscan
 * reports before a canonical single answer exists, so there is no early-
 * stop optimisation to fall back to (unlike `nosom`, which always stops at
 * the first callback). This is the SAME "unconditional space cost, not a
 * dial" the roster row (`testees/CLAUDE.md`) already states for SOM's
 * compiled-database cost, extended honestly to its MATCH-time cost too.
 * ============================================================================
 */

#include <hs/hs.h>

#include <errno.h>
#include <setjmp.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

/* The DEFAULT hs_compile flags word. [B77] U2 (utf8_set_v1.md 7.1/7.6):
 * `--encoding utf8` ORs in HS_FLAG_UTF8 -- the `vectorscan-block-nosom-
 * utf8` config only -- and NEVER HS_FLAG_UCP (the measured A/B below: UCP
 * breaks `\b`; a UCP config is named, not built, 7.6 (2)). */
#define VS_DRIVER_FLAGS  0

static double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

static void die(const char *what) {
    printf("error\t%s\n", what);
    fflush(stdout);
    exit(2);
}

/* [B77] U1: the find-all EMPTY-MATCH advance under --utf8 -- pcrec
 * match_api.md S3.1.1's NORMATIVE utf8 rule, the same one every other
 * driver in this repo implements (testees/pcre2/driver.c's own copy,
 * quoted there verbatim): from pos + 1, skip every byte in 0x80-0xBF,
 * stop at the first byte outside that range or at n. Reached only from
 * `--som`'s find-all reduction below (SOM MODE); `nosom` has no find-all
 * loop for this to serve. */
static size_t utf8_next_start(const unsigned char *b, size_t n, size_t pos) {
    size_t p = pos + 1;
    while (p < n && (b[p] & 0xC0u) == 0x80u) p++;
    return p;
}

/* ------------------------------------------------- SOM MODE: match list
 *
 * A growable array of every (from, to) pair `--som`'s callback accumulates
 * for ONE hs_scan() call -- see the file header's "SOM MODE" section for
 * why nothing here stops early. Reused across `iters` passes via
 * `vs_reset()` rather than freed and reallocated each time. */
typedef struct { unsigned long long from, to; } vs_match;

typedef struct {
    vs_match *v;
    size_t    n, cap;
} vs_match_list;

static void vs_reset(vs_match_list *m) { m->n = 0; }

static void vs_push(vs_match_list *m, unsigned long long from,
                    unsigned long long to) {
    if (m->n == m->cap) {
        size_t newcap = m->cap ? m->cap * 2 : 64;
        vs_match *nv = realloc(m->v, newcap * sizeof *nv);
        if (!nv) die("out of memory accumulating SOM matches");
        m->v = nv;
        m->cap = newcap;
    }
    m->v[m->n].from = from;
    m->v[m->n].to = to;
    m->n++;
}

/* qsort comparator: `from` ASCENDING, `to` DESCENDING on a tie -- so the
 * FIRST entry at any given `from` is already that start's own LONGEST
 * completion (the file header's reduction rule (1)/(2), used identically
 * by the first-match span and the find-all cursor walk below). */
static int vs_cmp_match(const void *ap, const void *bp) {
    const vs_match *a = ap, *b = bp;
    if (a->from != b->from) return (a->from < b->from) ? -1 : 1;
    if (a->to != b->to) return (a->to > b->to) ? -1 : 1;
    return 0;
}

/* `--som`'s callback: NEVER requests early termination (always returns 0)
 * -- see the file header's "SOM MODE" section for why. `context` is a
 * `vs_match_list *`. */
static int HS_CDECL on_match_som(unsigned int id, unsigned long long from,
                                 unsigned long long to, unsigned int flags,
                                 void *context) {
    (void)id; (void)flags;
    vs_push((vs_match_list *)context, from, to);
    return 0;
}

static unsigned char *slurp(const char *path, size_t *sz_out) {
    FILE *f = fopen(path, "rb");
    if (!f) { printf("error\tfopen %s: %s\n", path, strerror(errno)); return NULL; }
    if (fseek(f, 0, SEEK_END) != 0) { fclose(f); return NULL; }
    long sz = ftell(f);
    if (sz < 0) { fclose(f); return NULL; }
    rewind(f);
    unsigned char *buf = malloc((size_t)sz + 1);
    if (!buf) { fclose(f); return NULL; }
    if (sz > 0 && fread(buf, 1, (size_t)sz, f) != (size_t)sz) {
        fclose(f); free(buf); return NULL;
    }
    buf[sz] = 0;
    fclose(f);
    *sz_out = (size_t)sz;
    return buf;
}

/* ------------------------------------------------- the per-subject alarm */

static sigjmp_buf timeout_jmp;
static volatile sig_atomic_t timed_out;

static void on_alarm(int sig) {
    (void)sig;
    timed_out = 1;
    siglongjmp(timeout_jmp, 1);
}

/* ---------------------------------------------------------------- subjects */

typedef struct {
    char          *id;
    unsigned char *buf;
    size_t         len;
} subject;

/* noinline: the same gcc-vs-sigsetjmp-locals note testees/pcre2/driver.c
 * and testees/onig/driver.c both carry. */
__attribute__((noinline))
static subject *load_list(const char *path, size_t *n_out) {
    FILE *f = fopen(path, "r");
    if (!f) return NULL;
    size_t cap = 64, n = 0;
    subject *v = malloc(cap * sizeof *v);
    char line[8192];
    while (fgets(line, sizeof line, f)) {
        char *nl = strchr(line, '\n');
        if (nl) *nl = 0;
        if (!*line) continue;
        char *tab = strchr(line, '\t');
        if (!tab) continue;
        *tab = 0;
        if (n == cap) { cap *= 2; v = realloc(v, cap * sizeof *v); }
        v[n].id = strdup(line);
        v[n].buf = slurp(tab + 1, &v[n].len);
        if (!v[n].buf) { fclose(f); free(v); return NULL; }
        n++;
    }
    fclose(f);
    *n_out = n;
    return v;
}

/* ------------------------------------------------------------ the callback
 *
 * Always requests early termination (return 1): this config never reports
 * a span or a count, so nothing is gained by letting hs_scan keep finding
 * matches past the first -- see this file's header, "MATCHING". */
typedef struct { volatile int matched; } match_ctx;

static int HS_CDECL on_match(unsigned int id, unsigned long long from,
                             unsigned long long to, unsigned int flags,
                             void *context) {
    (void)id; (void)from; (void)to; (void)flags;
    match_ctx *ctx = (match_ctx *)context;
    ctx->matched = 1;
    return 1;
}

/* ------------------------------------------------------------------- main */

int main(int argc, char **argv) {
    const char *pattern_path = NULL, *list_path = NULL, *mode = "search";
    const char *form = "plain";
    volatile long iters = 1, subject_timeout = 0, skip = 0;
    long compile_trials = 1;
    volatile int find_all = 0;
    /* [B70] docs/design/capability_set_v1.md 14: whether the harness has
     * read `requires=free-spacing` off THIS pattern's own tags -- decided
     * in pcrecbench/harness.py (the one place a Pattern's tags are
     * visible), forwarded through testees/vectorscan/adapter.py as this
     * flag, taken only on `--form whole-subject` (the adapter never sets
     * it for `plain`). See the whole-subject expr build below for what
     * it changes. */
    volatile int free_spacing = 0;
    /* [B77] U1: --utf8, the protocol's character-boundary find-all advance.
     * INERT under `nosom` (no find-all loop at boolean grain, the header's
     * MATCHING paragraph); LIVE under `--som`'s find-all reduction (the
     * header's "SOM MODE" section) -- it never selects HS_FLAG_UTF8 either
     * way, since the engine's ENCODING is a config's choice (utf8_set_v1.md
     * 7.1, lane U2), not the protocol's. */
    volatile int utf8_adv = 0;
    /* [B92]: HS_FLAG_SOM_LEFTMOST, `vectorscan-block-som` only -- see the
     * file header's "SOM MODE" section. `vectorscan-block-nosom`'s own
     * argv never carries this flag (testees/vectorscan/adapter.py), so its
     * own byte-for-byte behaviour is provably unreached by anything below. */
    volatile int som_mode = 0;
    unsigned int hs_flags = VS_DRIVER_FLAGS;   /* [B77] U2: --encoding */

    for (int i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!strcmp(a, "--pattern") && i + 1 < argc)        pattern_path = argv[++i];
        else if (!strcmp(a, "--list") && i + 1 < argc)      list_path = argv[++i];
        else if (!strcmp(a, "--mode") && i + 1 < argc)      mode = argv[++i];
        else if (!strcmp(a, "--form") && i + 1 < argc)      form = argv[++i];
        else if (!strcmp(a, "--iters") && i + 1 < argc)     iters = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--compile-trials") && i + 1 < argc) compile_trials = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--subject-timeout") && i + 1 < argc) subject_timeout = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--skip") && i + 1 < argc)      skip = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--find-all"))                  find_all = 1;
        else if (!strcmp(a, "--free-spacing"))               free_spacing = 1;
        else if (!strcmp(a, "--utf8"))                      utf8_adv = 1;
        else if (!strcmp(a, "--som"))                       som_mode = 1;
        else if (!strcmp(a, "--encoding") && i + 1 < argc) {
            const char *e = argv[++i];
            if (!strcmp(e, "utf8"))       hs_flags = VS_DRIVER_FLAGS | HS_FLAG_UTF8;
            else if (!strcmp(e, "byte"))  hs_flags = VS_DRIVER_FLAGS;
            else { printf("error\tunknown encoding %s\n", e); return 2; }
        }
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    /* [B92]: applied LAST, after --encoding, so it ORs onto either flags
     * value; see the file header's "SOM MODE" section, "COMPILE TIME". */
    if (som_mode) hs_flags |= HS_FLAG_SOM_LEFTMOST;
    /* `find_all`/`utf8_adv` ARE read below, in the `--som` branch of the
     * per-subject loop (the file header's "SOM MODE" section) -- under
     * `nosom` they stay accepted-but-inert exactly as before ([B77] U1,
     * "MATCHING"), so no `(void)` cast is needed on either path. */
    if (!pattern_path) die("--pattern is required");
    if (iters < 1) iters = 1;
    int whole_subject = !strcmp(form, "whole-subject");
    if (list_path) {
        int mode_wants_whole = !strcmp(mode, "match");
        if (mode_wants_whole != whole_subject)
            die("--mode and --form disagree (this driver has no anchoring "
                "dial independent of --form)");
    }

    setvbuf(stdout, NULL, _IOLBF, 0);

    printf("info\tversion\t%s\n", hs_version());
    printf("info\tform\t%s\n", form);
    /* [B77] U2: printed ONLY under --encoding utf8, so a byte config's
     * driver output is unchanged line for line. */
    if (hs_flags & HS_FLAG_UTF8) printf("info\tencoding\tutf8\n");

    size_t patlen = 0;
    unsigned char *pat = slurp(pattern_path, &patlen);
    if (!pat) { printf("error\tcannot read pattern %s\n", pattern_path); return 2; }

    /* Build the actual expression text this driver compiles. `plain`: the
     * pattern bytes verbatim. `whole-subject`: this driver's OWN wider
     * wrapper (see header) -- `^(?:` + pattern + `)\z`, or, when
     * `free_spacing` ([B70], docs/design/capability_set_v1.md 14), `^(?:`
     * + pattern + `\n)\z` -- a `(?x)` pattern may end its raw text on a
     * line comment with no trailing newline, and appending `)\z` directly
     * would land ON that comment (the [B69] census's finding); a `\n`
     * ends a free-spacing comment and is unsafe everywhere else (a
     * literal newline ATOM under the default syntax) -- the SAME
     * conditional rule `pcrecbench.record.whole_subject_text`'s own
     * docstring states in full, applied here in C because this driver
     * builds its own wider wrapper rather than reusing that function.
     * Requires a NUL-terminated C string either way:
     * hs_compile()/hs_expression_info() take `const char *expression`,
     * not a length-delimited buffer, the same constraint pcre2's
     * ZERO_TERMINATED convention and onig's `pat + patlen`-bounded call
     * both avoid in their own ways -- this bench's patterns are text
     * regexes with no embedded NUL, so a NUL-terminated copy is lossless
     * here. */
    char *expr;
    if (whole_subject) {
        size_t nl = free_spacing ? 1 : 0;
        size_t n = 4 + patlen + nl + 3 + 1;
        expr = malloc(n);
        memcpy(expr, "^(?:", 4);
        memcpy(expr + 4, pat, patlen);
        if (free_spacing) expr[4 + patlen] = '\n';
        memcpy(expr + 4 + patlen + nl, ")\\z", 3);
        expr[4 + patlen + nl + 3] = 0;
    } else {
        expr = malloc(patlen + 1);
        memcpy(expr, pat, patlen);
        expr[patlen] = 0;
    }

    /* ---- compile, `compile_trials` times, the one phase timed ---- */
    hs_database_t *db = NULL;
    for (long t = 1; t <= compile_trials; t++) {
        hs_database_t *d = NULL;
        hs_compile_error_t *err = NULL;
        double t0 = now();
        hs_error_t rc = hs_compile(expr, hs_flags, HS_MODE_BLOCK,
                                   NULL, &d, &err);
        double t1 = now();
        if (rc != HS_SUCCESS) {
            char msgbuf[1024];
            int expr_idx = err ? err->expression : -1;
            snprintf(msgbuf, sizeof msgbuf, "hs_compile failed (code %d, "
                     "expression %d): %s", (int)rc, expr_idx,
                     err && err->message ? err->message : "(no message)");
            for (char *p = msgbuf; *p; p++)
                if (*p == '\t' || *p == '\n') *p = ' ';
            printf("error\t%s\n", msgbuf);
            if (err) hs_free_compile_error(err);
            return 3;
        }
        printf("compile\t%ld\tcompile\t%.9f\n", t, t1 - t0);
        if (db) hs_free_database(db);
        db = d;
    }

    /* engine_metadata, `pattern`-scoped (record_schema.md 7 rule 2):
     * declared in testees/vectorscan/adapter.py. */
    {
        hs_expr_info_t *info = NULL;
        hs_compile_error_t *err = NULL;
        if (hs_expression_info(expr, hs_flags, &info, &err) == HS_SUCCESS
            && info) {
            printf("info\tmin_width\t%u\n", info->min_width);
            printf("info\tmax_width\t%u\n", info->max_width);
            printf("info\tunordered_matches\t%d\n", (int)info->unordered_matches);
            printf("info\tmatches_at_eod\t%d\n", (int)info->matches_at_eod);
            printf("info\tmatches_only_at_eod\t%d\n", (int)info->matches_only_at_eod);
            free(info);
        }
        if (err) hs_free_compile_error(err);
    }
    {
        size_t dbsize = 0;
        if (hs_database_size(db, &dbsize) == HS_SUCCESS)
            printf("info\tcompiled_size_bytes\t%zu\n", dbsize);
    }

    /* Scratch: allocated ONCE, UNTIMED, right after the last compile trial
     * -- see this file's header. A failure here is a driver-level defect,
     * not a per-pattern compile outcome (every pattern that compiles gets
     * a scratch; a scratch that cannot be sized for a legitimately
     * compiled database would itself be a Vectorscan bug worth surfacing
     * loudly rather than folding into `did-not-compile`). */
    hs_scratch_t *scratch = NULL;
    if (hs_alloc_scratch(db, &scratch) != HS_SUCCESS)
        die("hs_alloc_scratch failed");

    if (!list_path) { fflush(stdout); return 0; }   /* compile-only run */

    size_t nsub = 0;
    subject *subs = load_list(list_path, &nsub);
    if (!subs) { printf("error\tcannot read subject list %s\n", list_path); return 2; }

    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);

    /* [B92]: only touched when `som_mode` -- reused across subjects and
     * `iters` passes via `vs_reset()` rather than reallocated each time.
     * Left zero-initialized and unused on the `nosom` path. */
    vs_match_list ml = { 0 };

    for (size_t i = (size_t)skip; i < nsub; i++) {
        subject *s = &subs[i];
        volatile int matched = 0;
        volatile double elapsed = 0.0;

        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            double t0 = now();
            if (som_mode) {
                /* [B92], SOM MODE: the callback never stops early (see the
                 * file header) -- every `iters` pass re-scans and
                 * re-accumulates the WHOLE subject, which is `--som`'s own
                 * real, documented cost. */
                for (long it = 0; it < iters; it++) {
                    vs_reset(&ml);
                    hs_error_t rc = hs_scan(db, (const char *)s->buf,
                                            (unsigned int)s->len, 0, scratch,
                                            on_match_som, &ml);
                    if (rc != HS_SUCCESS) {
                        /* Same reasoning as the `nosom` arm below (see
                         * header, "GAVE-UP CODES: NONE") -- `on_match_som`
                         * never requests early termination, so there is no
                         * HS_SCAN_TERMINATED to except here either. */
                        matched = -1;
                        (void)rc;
                        break;
                    }
                    matched = ml.n > 0 ? 1 : 0;
                }
            } else {
                for (long it = 0; it < iters; it++) {
                    match_ctx ctx = { 0 };
                    hs_error_t rc = hs_scan(db, (const char *)s->buf,
                                            (unsigned int)s->len, 0, scratch,
                                            on_match, &ctx);
                    if (rc != HS_SUCCESS && rc != HS_SCAN_TERMINATED) {
                        /* No documented resource-limit refusal on this route
                         * (see header, "GAVE-UP CODES: NONE") -- an
                         * unexpected negative return is a driver/API-level
                         * problem, reported via the ANSWER column so the
                         * harness's crashed path (never a gave-up range,
                         * empty by construction) picks it up. */
                        matched = -1;
                        (void)rc;
                        break;
                    }
                    matched = ctx.matched ? 1 : 0;
                }
            }
            elapsed = now() - t0;
            if (subject_timeout > 0) alarm(0);
        }

        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                   s->id, (long)iters, (double)elapsed);
            continue;
        }

        const char *answer;
        char answerbuf[64];
        if (matched < 0) {
            answer = "error:hs_scan returned an unexpected code";
        } else if (matched) {
            answer = "match";
        } else {
            answer = "nomatch";
        }
        (void)answerbuf;

        if (!som_mode) {
            /* NO SPAN, EVER: START=END=-, NCAPS=0, CAPS=-, NMATCHES=- --
             * see this file's header. consumed_length: the whole subject,
             * always (hs_scan's own `length` argument, this driver always
             * passes the full byte count). BYTE FOR BYTE the pre-[B92]
             * line -- the `nosom` config's own argv never sets `som_mode`,
             * so this branch is the ONLY one it ever reaches. */
            printf("subject\t%s\t%s\t-\t-\t0\t%zu\t%ld\t%.9f\t-\t-\n",
                   s->id, answer, s->len, (long)iters, (double)elapsed);
            continue;
        }

        /* [B92], SOM MODE: a real span (leftmost, then longest -- see the
         * file header for the divergence this states honestly) and, under
         * `--find-all`, a real non-overlapping NMATCHES (KB-17's advance
         * rule over the SAME reduction). NCAPS is always 0, CAPS is always
         * `-`: Hyperscan has no capturing groups regardless of SOM.
         * consumed_length: the whole subject, always, same as `nosom`. */
        char sbuf[32] = "-", ebuf[32] = "-", nbuf[32] = "-";
        if (matched == 1) {
            unsigned long long min_from = ml.v[0].from, best_to = ml.v[0].to;
            for (size_t k = 1; k < ml.n; k++) {
                if (ml.v[k].from < min_from) {
                    min_from = ml.v[k].from;
                    best_to = ml.v[k].to;
                } else if (ml.v[k].from == min_from && ml.v[k].to > best_to) {
                    best_to = ml.v[k].to;
                }
            }
            snprintf(sbuf, sizeof sbuf, "%llu", min_from);
            snprintf(ebuf, sizeof ebuf, "%llu", best_to);

            if (find_all) {
                qsort(ml.v, ml.n, sizeof *ml.v, vs_cmp_match);
                long count = 0;
                unsigned long long cursor = 0;
                for (size_t k = 0; k < ml.n; k++) {
                    if (ml.v[k].from < cursor) continue;
                    unsigned long long S = ml.v[k].from, E = ml.v[k].to;
                    count++;
                    cursor = (E > S) ? E
                           : utf8_adv ? utf8_next_start(s->buf, s->len, (size_t)S)
                                      : S + 1;
                }
                snprintf(nbuf, sizeof nbuf, "%ld", count);
            }
        } else if (matched == 0 && find_all) {
            /* Zero matches IS a count -- `0`, never `-` (the SAME
             * convention testees/pcre2/driver.c's own `nmatch >= 0` guard
             * prints). */
            strcpy(nbuf, "0");
        }

        printf("subject\t%s\t%s\t%s\t%s\t0\t%zu\t%ld\t%.9f\t%s\t-\n",
               s->id, answer, sbuf, ebuf, s->len, (long)iters,
               (double)elapsed, nbuf);
    }

    free(ml.v);
    hs_free_scratch(scratch);
    hs_free_database(db);
    fflush(stdout);
    return 0;
}
