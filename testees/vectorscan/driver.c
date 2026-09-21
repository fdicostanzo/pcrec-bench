/* testees/vectorscan/driver.c -- the Vectorscan (Hyperscan-ABI-compatible
 * fork) batched in-process timing driver, BLOCK MODE, NO SOM
 * (`vectorscan-block-nosom`, capability_set_v1.md 5.6 option (B),
 * Frank's Q3 boolean-grain ruling, 2026-09-16).
 *
 * Implements the DRIVER PROTOCOL in pcrecbench/adapters.py, with ONE
 * deliberate, documented shape difference from every other driver in this
 * repo: THIS DRIVER NEVER REPORTS A MATCH SPAN. `testees/vectorscan/
 * CLAUDE.md` states in full what that costs (a real, MEASURED gap in
 * `harness.outcome_for` -- every genuine match is scored `wrong-span-or-
 * captures`, never `matched-as-expected`); read that file before reading
 * numbers out of a report row for this testee.
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
 * NO SPAN, EVER: START and END are ALWAYS printed `-`, even on a real
 * match (capability_set_v1.md 5.6 option (B)'s own stated shape: "a
 * Vectorscan driver reporting ANSWER=match/nomatch with START=END=-").
 * Hyperscan's callback DOES hand this driver a real `to` (end) offset on
 * every match, and this driver deliberately never reports it: printing a
 * real END while STARTs stays `-` would be a half-measure this project's
 * own protocol comment does not describe, and would still fail
 * `harness.outcome_for`'s span comparison test (`row.end !=
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
 * else to report there.
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
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    (void)find_all;  /* accepted for protocol compliance; see header */
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
        hs_error_t rc = hs_compile(expr, VS_DRIVER_FLAGS, HS_MODE_BLOCK,
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
        if (hs_expression_info(expr, VS_DRIVER_FLAGS, &info, &err) == HS_SUCCESS
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

    for (size_t i = (size_t)skip; i < nsub; i++) {
        subject *s = &subs[i];
        volatile int matched = 0;
        volatile double elapsed = 0.0;

        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            double t0 = now();
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

        /* NO SPAN, EVER: START=END=-, NCAPS=0, CAPS=-, NMATCHES=- -- see
         * this file's header. consumed_length: the whole subject, always
         * (hs_scan's own `length` argument, this driver always passes
         * the full byte count). */
        printf("subject\t%s\t%s\t-\t-\t0\t%zu\t%ld\t%.9f\t-\t-\n",
               s->id, answer, s->len, (long)iters, (double)elapsed);
    }

    hs_free_scratch(scratch);
    hs_free_database(db);
    fflush(stdout);
    return 0;
}
