/* testees/tre/driver.c -- the TRE batched in-process timing driver.
 *
 * Implements the DRIVER PROTOCOL in pcrecbench/adapters.py verbatim; read
 * that first. This file's own decisions ([B7]/L6b, capability_set_v1.md
 * 11.1, lane l6btre, 2026-09-17):
 *
 * DIRECT LINKING (this box has libtre-dev 0.9.0-1build1, confirmed
 * installed by scripts/install_l6b_deps.sh before this lane started):
 * `#include <tre/tre.h>`, link `-ltre`. No dlopen, no probed constants --
 * every symbol below is the real header's.
 *
 * THE POSIX API, THE BYTE-LITERAL / EXPLICIT-LENGTH VARIANTS.
 * `tre_regncompb`/`tre_regnexecb` -- the "n" (explicit length, so an
 * embedded NUL never truncates the pattern or the subject the way
 * NUL-terminated `tre_regcomp`/`tre_regexec` would) AND "b" (BYTE
 * LITERAL: tre.h's own comment, "regn*b versions take byte literally as
 * 8-bit values" -- bypasses TRE's locale/multibyte decoding entirely, the
 * same convention testees/pcre2/ (8-bit non-UTF) and testees/onig/
 * (ONIG_ENCODING_ASCII) already hold themselves to: a byte >= 0x80 is one
 * "character", never a decode error) suffixed pair. This is what makes
 * I-72 (raw pattern bytes end to end) hold for TRE without a driver-side
 * workaround: the pattern travels as a FILE (`--pattern`, this driver's
 * own `slurp()`), never argv text, exactly like testees/pcre2/ and
 * testees/onig/'s own convention.
 *
 * CFLAGS: REG_EXTENDED only -- NOT REG_NEWLINE. Two consequences,
 * MEASURED live by this lane (docs/dev/measurements/2026-09-17-tre-
 * capability-witness-census.txt), stated here because they are the
 * compile-flag's own doing, not a pattern-by-pattern surprise:
 *   (a) `.` MATCHES a newline byte under REG_EXTENDED alone (`a.b` vs
 *       "a\nb" matches) -- this DIVERGES from PCRE2's default (`.`
 *       excludes `\n` unless PCRE2_DOTALL). REG_NEWLINE would flip this
 *       the right way but at a cost stated in (b), so it is not used.
 *   (b) `^`/`$` are SINGLE-LINE anchors (`^b$` against "a\nb\nc" does
 *       NOT match) -- this MATCHES PCRE2's default (`^`/`$` anchor the
 *       whole subject, not each embedded line, absent PCRE2_MULTILINE).
 *       REG_NEWLINE would turn this into MULTILINE `^`/`$` instead, which
 *       is the wrong direction for a pcre2-oracled corpus, so REG_NEWLINE
 *       is not enabled and (a)'s divergence is accepted instead: POSIX/TRE
 *       offers no flag combination that gets BOTH pcre2-default behaviors
 *       at once.
 * A further consequence, also measured live: TRE's `$` WITHOUT
 * REG_NEWLINE is a TRUE end-of-string anchor -- `a$` against "a\n" does
 * NOT match, unlike PCRE2's own default `$` (which ALSO matches
 * immediately before a final newline). This makes plain `$` closer to
 * PCRE2's `\z` than to PCRE2's own `$` -- useful below.
 *
 * TWO FORMS, mirroring testees/onig/adapter.py's own model (TRE, like
 * Oniguruma, has no runtime end-anchor option):
 *   `plain`         -- the pattern as authored. A SINGLE tre_regnexecb
 *                      call already performs an UNANCHORED, leftmost
 *                      search over the whole subject (POSIX regexec's own
 *                      contract: "the leftmost, and among those, the
 *                      longest match" -- unlike onig_search/pcre2_match,
 *                      TRE needs no separate search-vs-match ENTRY POINT
 *                      or explicit search window; ONE call already does
 *                      the `search` regime's job).
 *   `whole-subject` -- `^(?:<pattern>)$`, NOT
 *                      `pcrecbench.record.whole_subject_text()`'s
 *                      `(?:<pattern>)\z` -- TRE has NO `\z`/`\A`/`\Z`
 *                      tokens at all (confirmed absent from
 *                      lib/tre-parse.c's escape switch, docs/dev/research/
 *                      2026-09-12-b42-engine-landscape.md (5); reconfirmed
 *                      live here, `\z` in a pattern compiles as literal
 *                      "z", never an anchor). `(?:...)` -- a NON-POSIX,
 *                      UNDOCUMENTED TRE extension -- IS accepted (measured
 *                      live: `(?:ab)c` compiles, re_nsub unchanged from
 *                      the unwrapped `ab`), so the wrap preserves the
 *                      PLAIN form's own capture-group numbering exactly
 *                      like pcrec's/onig's own `(?:...)`-based wrap does.
 *                      `^` and `$` (both single-line per the CFLAGS note
 *                      above) supply the start and end anchors: `^` binds
 *                      to the true string start because eflags carries no
 *                      REG_NOTBOL on this call, and `$`'s TRUE
 *                      end-of-string behavior (not before a trailing
 *                      newline) makes this wrap's END anchor semantically
 *                      the same contract `\z` gives pcrec/onig's own
 *                      wrap, just spelled with POSIX syntax instead of a
 *                      token TRE does not have. MEASURED: `^(ab)$` matches
 *                      "ab" at [0,2) and refuses "abx" -- both directions
 *                      confirmed live.
 *
 * FIND-ALL / THROUGHPUT: pcrec match_api.md S3.1's advance-from-reported-
 * START rule (KB-17, adopted BY REFERENCE, the same rule testees/pcre2/
 * and testees/onig/ apply): the next scan starts at the match END when
 * non-empty, else one past the match's own reported START. TRE's exec API
 * (tre_regnexecb) has NO "search starting at position N within a LARGER
 * true buffer" primitive -- unlike pcre2_match's `startoffset` or
 * onig_search's separate `str`/`end`/`start`/`range` pointers, both of
 * which keep the TRUE buffer start visible to the engine while moving
 * only the search window. TRE's public exec surface takes exactly one
 * `(string, len)` pair, so advancing means RE-SLICING the buffer
 * (`str + pos`, `len - pos`) and there is no way to hand TRE the discarded
 * prefix as context. Consequence, stated plainly rather than hidden: `^`
 * is corrected with REG_NOTBOL (so it does not wrongly re-fire at the new
 * slice's own start once pos > 0), but a WORD-BOUNDARY (`\b`) assertion
 * straddling the re-slice point loses its left-context byte and can
 * misjudge the boundary there -- a genuine ENGINE-API limitation, not an
 * adapter oversight, and one this driver has no way to route around
 * within tre.h's exec surface. This only bears on `--find-all` (the
 * throughput regime's multi-match loop) with a `\b`-bearing pattern; the
 * single-shot `search_short`/`match` calls (pos always 0) are unaffected
 * because they see the whole, real buffer from its own true start.
 *
 * GAVE-UP: TRE's own `reg_errcode_t` is shared between tre_regcomp and
 * tre_regexec, and POSIX regexec's own contract recognizes only 0
 * (match) and REG_NOMATCH (no match) as answers -- ANY OTHER return code
 * is therefore, by construction, not an answer but an internal
 * resource/error condition, and this driver treats it as `gave-up`
 * generically (code + tre_regerror's own text as the diagnostic) rather
 * than hardcoding a guessed enumeration the way testees/pcre2/ and
 * testees/onig/ do over their MANY distinguishable negative codes. TRE's
 * own TRE_MAX_STACK (1,048,576 B, the match-time backtracking stack --
 * lib/tre-internal.h, docs/dev/research/2026-09-12-b42-engine-landscape.md
 * (5)) is the one documented match-time budget that could produce such a
 * code (REG_ESPACE); testees/tre/CLAUDE.md states plainly that this
 * lane's own probe (a five-way backreference pattern, `tre_have_backrefs`
 * confirmed 1, over 40 non-matching bytes under a 2 s alarm) did NOT
 * reproduce it -- REG_NOMATCH came back well inside the alarm -- so the
 * mechanism is PROVISIONED and UNWITNESSED, not confirmed live the way
 * onig's own retry-limit gave-up code was.
 *
 * COMPILE COST: one phase, `compile` -- `tre_regncompb`, timed in-driver.
 * No separate JIT/DFA-construction step is exposed (TRE builds its
 * internal TNFA/backtracking form inside this one call); the same
 * execution-model shape as pcre2-interp/onig-default.
 *
 * refusal_class (engine_metadata, declared in testees/tre/adapter.py):
 * TRE's `reg_errcode_t` is a CLOSED, structural signal (capability_set_v1.md
 * 5.5's own bar for declaring one) -- bucketed by the adapter from the
 * numeric code this driver prints, never re-derived here. REG_ESPACE is
 * the one code TRE overloads for TWO different causes at COMPILE time
 * (lib/regcomp.c: `if (n > TRE_MAX_RE) return REG_ESPACE;`, alongside a
 * genuine allocation failure) -- this driver cannot tell them apart from
 * the code alone, so it also reports the PATTERN'S OWN BYTE LENGTH
 * (`info\tpattern_bytes\tN`) so the adapter can classify `size-limit`
 * only when N exceeds TRE_MAX_RE (65536), leaving refusal_class ABSENT
 * (never a guessed "memory") otherwise -- testees/onig/adapter.py's own
 * "an honest omission is not a wrong classification" rule, applied here
 * to a code TRE conflates rather than one this driver cannot parse.
 */

#include <tre/tre.h>

#include <errno.h>
#include <setjmp.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define TRE_DRIVER_CFLAGS REG_EXTENDED

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

/* noinline: gcc otherwise inlines this into main(), where sigsetjmp lives,
 * and warns that its locals `might be clobbered by longjmp` -- the same
 * note testees/pcre2/driver.c and testees/onig/driver.c both carry for
 * the identical reason. */
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

/* ------------------------------------------------------------------- main */

#define MAX_CAPS 64

static void emit_caps(regmatch_t *pmatch, size_t nmatch, char *out,
                      size_t outcap) {
    size_t off = 0;
    out[0] = 0;
    for (size_t i = 1; i < nmatch; i++) {
        long s = (pmatch[i].rm_so < 0) ? -1 : (long)pmatch[i].rm_so;
        long e = (pmatch[i].rm_eo < 0) ? -1 : (long)pmatch[i].rm_eo;
        int k = snprintf(out + off, outcap - off, "%s%ld:%ld",
                         i > 1 ? "," : "", s, e);
        if (k < 0 || (size_t)k >= outcap - off) break;
        off += (size_t)k;
    }
    if (!out[0]) { out[0] = '-'; out[1] = 0; }
}

int main(int argc, char **argv) {
    const char *pattern_path = NULL, *list_path = NULL, *mode = "search";
    const char *form = "plain";
    /* `volatile` on everything the per-subject sigsetjmp/siglongjmp pair can
     * see across the jump -- C11 6.8.6.1's indeterminate-after-longjmp rule,
     * the same note testees/pcre2/driver.c and testees/onig/driver.c both
     * carry. */
    volatile long iters = 1, subject_timeout = 0, skip = 0;
    long compile_trials = 1;
    volatile int find_all = 0;

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
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    if (!pattern_path) die("--pattern is required");
    if (iters < 1) iters = 1;
    int whole_subject = !strcmp(form, "whole-subject");
    /* `--mode` and `--form` are set TOGETHER by the adapter -- same
     * cross-check testees/onig/driver.c carries, same reason: there is no
     * second, independent anchoring dial once `--form` is chosen. */
    if (list_path) {
        int mode_wants_whole = !strcmp(mode, "match");
        if (mode_wants_whole != whole_subject)
            die("--mode and --form disagree (this driver has no anchoring "
                "dial independent of --form)");
    }

    setvbuf(stdout, NULL, _IOLBF, 0);

    {
        char verbuf[64];
        snprintf(verbuf, sizeof verbuf, "%s", tre_version());
        printf("info\tversion\t%s\n", verbuf);
    }
    printf("info\tcflags\tREG_EXTENDED\n");
    printf("info\tform\t%s\n", form);

    size_t patlen = 0;
    unsigned char *pat = slurp(pattern_path, &patlen);
    if (!pat) { printf("error\tcannot read pattern %s\n", pattern_path); return 2; }
    printf("info\tpattern_bytes\t%zu\n", patlen);

    unsigned char *wrapped = NULL;
    const char *comp_text = (const char *)pat;
    size_t comp_len = patlen;
    if (whole_subject) {
        /* `^(?:<pattern>)$` -- this file's header comment states why, at
         * length. wlen = strlen("^(?:") + patlen + strlen(")$")
         *              = 4 + patlen + 2. */
        size_t wlen = patlen + 6;
        wrapped = malloc(wlen + 1);
        memcpy(wrapped, "^(?:", 4);
        memcpy(wrapped + 4, pat, patlen);
        memcpy(wrapped + 4 + patlen, ")$", 2);
        wrapped[wlen] = 0;
        comp_text = (const char *)wrapped;
        comp_len = wlen;
    }

    /* ---- compile, `compile_trials` times, the one phase timed ---- */
    regex_t re;
    int have_re = 0;
    for (long t = 1; t <= compile_trials; t++) {
        regex_t r;
        double t0 = now();
        int rc = tre_regncompb(&r, comp_text, comp_len, TRE_DRIVER_CFLAGS);
        double t1 = now();
        if (rc != REG_OK) {
            char msg[512];
            tre_regerror(rc, &r, msg, sizeof msg);
            for (char *p = msg; *p; p++)
                if (*p == '\t' || *p == '\n') *p = ' ';
            printf("error\ttre_regncompb failed (code %d): %s\n", rc, msg);
            free(wrapped);
            return 3;
        }
        printf("compile\t%ld\tcompile\t%.9f\n", t, t1 - t0);
        if (have_re) tre_regfree(&re);
        re = r;
        have_re = 1;
    }

    /* engine_metadata, `pattern`-scoped (record_schema.md 7 rule 2):
     * declared in testees/tre/adapter.py -- an undeclared pair is a
     * validator error, so the two lists move together. re_nsub excludes
     * the whole-match group 0, matching pcre2's/onig's own capturecount
     * convention. */
    printf("info\tcapturecount\t%zu\n", re.re_nsub);
    printf("info\thas_backrefs\t%d\n", tre_have_backrefs(&re));

    if (!list_path) { fflush(stdout); tre_regfree(&re); free(wrapped); return 0; }

    size_t nsub = 0;
    subject *subs = load_list(list_path, &nsub);
    if (!subs) { printf("error\tcannot read subject list %s\n", list_path); return 2; }

    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);

    size_t nmatch_cap = re.re_nsub + 1;
    if (nmatch_cap > MAX_CAPS) nmatch_cap = MAX_CAPS;
    regmatch_t pmatch[MAX_CAPS];
    char caps[4096];

    for (size_t i = (size_t)skip; i < nsub; i++) {
        subject *s = &subs[i];
        volatile long   first_s = -1, first_e = -1, nmatches = -1;
        volatile int    rc_final = REG_NOMATCH;
        volatile double elapsed = 0.0;
        int ncaps_final = 0;
        char caps_final[4096]; caps_final[0] = '-'; caps_final[1] = 0;

        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            double t0 = now();
            for (long it = 0; it < iters; it++) {
                first_s = first_e = -1;
                if (find_all) {
                    size_t pos = 0;
                    long   count = 0;
                    for (;;) {
                        int eflags = (pos > 0) ? REG_NOTBOL : 0;
                        int rc = tre_regnexecb(&re, (const char *)s->buf + pos,
                                               s->len - pos, nmatch_cap,
                                               pmatch, eflags);
                        if (rc != REG_OK) { if (count == 0) rc_final = rc; break; }
                        long m_s = (long)pmatch[0].rm_so + (long)pos;
                        long m_e = (long)pmatch[0].rm_eo + (long)pos;
                        if (first_s < 0) {
                            first_s = m_s; first_e = m_e;
                            rc_final = rc;
                            ncaps_final = (int)nmatch_cap - 1;
                            /* pmatch[] is relative to the RE-SLICED buffer
                             * (s->buf + pos); the emitted caps must be
                             * absolute against the true subject, exactly
                             * like first_s/first_e above -- offset every
                             * entry by pos before rendering. */
                            if (pos > 0) {
                                for (size_t ci = 0; ci < nmatch_cap; ci++) {
                                    if (pmatch[ci].rm_so >= 0) pmatch[ci].rm_so += (regoff_t)pos;
                                    if (pmatch[ci].rm_eo >= 0) pmatch[ci].rm_eo += (regoff_t)pos;
                                }
                            }
                            emit_caps(pmatch, nmatch_cap, caps_final, sizeof caps_final);
                        }
                        count++;
                        /* pcrec match_api.md S3.1's find-all advance: off the
                         * match's own reported START, never off the scan
                         * position -- KB-17, the same rule testees/pcre2/
                         * driver.c and testees/onig/driver.c both apply. */
                        size_t start = (size_t)pmatch[0].rm_so;
                        size_t end = (size_t)pmatch[0].rm_eo;
                        pos += (end > start) ? end : start + 1;
                        if (whole_subject) break; /* one anchored position only */
                        if (pos > s->len) break;
                    }
                    nmatches = count;
                } else {
                    int rc = tre_regnexecb(&re, (const char *)s->buf, s->len,
                                           nmatch_cap, pmatch, 0);
                    rc_final = rc;
                    if (rc == REG_OK) {
                        first_s = (long)pmatch[0].rm_so;
                        first_e = (long)pmatch[0].rm_eo;
                        ncaps_final = (int)nmatch_cap - 1;
                        emit_caps(pmatch, nmatch_cap, caps_final, sizeof caps_final);
                    }
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

        char answerbuf[512];
        const char *answer;
        char sbuf[32], ebuf[32], nbuf[32];

        if (first_s >= 0) {
            answer = "match";
            strncpy(caps, caps_final, sizeof caps - 1);
            caps[sizeof caps - 1] = 0;
            snprintf(sbuf, sizeof sbuf, "%ld", (long)first_s);
            snprintf(ebuf, sizeof ebuf, "%ld", (long)first_e);
        } else {
            strcpy(sbuf, "-");
            strcpy(ebuf, "-");
            caps[0] = '-'; caps[1] = 0;
            ncaps_final = 0;
            if (rc_final == REG_NOMATCH) {
                answer = "nomatch";
            } else {
                /* Any code TRE returns from an exec call that is neither
                 * REG_OK nor REG_NOMATCH is, by POSIX's own contract for
                 * these functions, not an answer -- `giveup:<code>:<...>`.
                 * This driver's header comment states why no fixed code
                 * table is hardcoded here the way testees/pcre2/ and
                 * testees/onig/ hardcode theirs. */
                char emsg[512];
                tre_regerror(rc_final, &re, emsg, sizeof emsg);
                for (char *p = emsg; *p; p++)
                    if (*p == '\t' || *p == '\n') *p = ' ';
                snprintf(answerbuf, sizeof answerbuf, "giveup:%d:%s",
                         (int)rc_final, emsg);
                answer = answerbuf;
            }
        }
        if (find_all && nmatches >= 0) snprintf(nbuf, sizeof nbuf, "%ld", (long)nmatches);
        else strcpy(nbuf, "-");

        /* consumed_length: the length TRE was given and accepted for this
         * call -- the whole subject on the single-shot (non-find-all)
         * path; on find-all the LAST attempted slice's length is not what
         * this column means (it is a per-subject total, not per-attempt),
         * so this driver reports the WHOLE subject length here too,
         * matching testees/pcre2/'s and testees/onig/'s own convention:
         * "no byte was withheld or refused", never "the engine looked at
         * every byte in one call". */
        printf("subject\t%s\t%s\t%s\t%s\t%d\t%zu\t%ld\t%.9f\t%s\t%s\n",
               s->id, answer, sbuf, ebuf, ncaps_final,
               s->len, (long)iters, (double)elapsed, nbuf, caps);
    }

    tre_regfree(&re);
    free(wrapped);
    fflush(stdout);
    return 0;
}
