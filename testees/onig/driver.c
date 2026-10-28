/* testees/onig/driver.c -- the Oniguruma batched in-process timing driver.
 *
 * Implements the DRIVER PROTOCOL in pcrecbench/adapters.py verbatim; read
 * that first. This file's own decisions:
 *
 * WHY DIRECT LINKING, NOT dlopen. Unlike testees/pcre2/ (runtime-only box,
 * no -dev package at the time that adapter was written), this box HAS
 * libonig-dev (6.9.10-1build1, `/usr/include/oniguruma.h`, verified
 * byte-identical to the upstream v6.9.10 tag this file's comments cite) --
 * so this driver simply `#include <oniguruma.h>` and links `-lonig`. No
 * hand-declared prototypes, no probed constants: every symbol and value
 * below is the real header's.
 *
 * SYNTAX (testees/onig/CLAUDE.md has the full argument): ONIG_SYNTAX_PERL_NG
 * -- the closest of this version's shipped syntaxes to PCRE (named groups,
 * `\K`, possessive quantifiers, atomic groups, if-else conditionals, `\g`
 * subexp calls, `\p{...}`). `ONIG_SYNTAX_PERL_NT` does not exist in 6.9.10.
 *
 * ENCODING: ONIG_ENCODING_ASCII (UNLESS `--encoding utf8` -- [B77] U2, the
 * `onig-utf8` config only: ONIG_ENCODING_UTF8, chosen at runtime) --
 * single-byte, `is_valid_mbc_string`
 * unconditionally true (src/ascii.c: `onigenc_always_true_is_valid_mbc_
 * string`), so a byte >= 0x80 is a valid one-byte "character" like PCRE2's
 * default 8-bit non-UTF mode, never a decode error. testees/onig/CLAUDE.md
 * states the consequences for `\p{...}` and case folding.
 *
 * COMPILE COST: one phase, `compile` -- `onig_new`, timed in-driver.
 * Oniguruma has no separate JIT step (an interpretive backtracking engine,
 * the same execution-model class as pcre2-interp).
 *
 * TWO FORMS, ONE INVOCATION EACH (`--form plain|whole-subject`): Oniguruma
 * has no runtime end-anchor option (no PCRE2_ENDANCHORED equivalent), so
 * the `match` regime (anchored AND end-anchored) is answered on a SECOND
 * artifact compiled from `(?:<pattern>)\z` (the SAME bytes
 * `pcrecbench.record.whole_subject_text` produces for pcrec -- `\z` is
 * ONIG_SYN_OP_ESC_AZ_BUF_ANCHOR, present under Perl_NG, confirmed live in
 * src/regparse.c). `onig_match` (not `onig_search`) supplies the START
 * anchor: it matches AT the given position only, never scanning -- so
 * `--form whole-subject` always calls `onig_match` at offset 0, and the
 * wrapper's own `\z` supplies the end anchor. `--form plain` always calls
 * `onig_search` (unanchored, leftmost). Adapter.compile() runs this driver
 * TWICE per pattern, once per form -- the DRIVER PROTOCOL's `compile` line
 * carries no form column, so form separation is the ADAPTER's job, exactly
 * as pcrec's own two-artifact model does it.
 *
 * consumed_length: the length argument (`end - str`) this driver passed
 * onig_search/onig_match and Oniguruma accepted -- i.e. the whole subject.
 * Oniguruma exposes no scan high-water mark either (same convention as
 * testees/pcre2/CLAUDE.md states for pcre2: "no byte was withheld or
 * refused", never "the engine looked at every byte").
 *
 * GAVE-UP CODES ([measured] against this box's /usr/include/oniguruma.h +
 * a direct read of src/regparse.c and src/regexec.c, v6.9.10, this lane,
 * 2026-09-17): four MATCH-TIME resource-limit codes, raised in regexec.c --
 *   ONIGERR_MATCH_STACK_LIMIT_OVER           (-15)
 *   ONIGERR_RETRY_LIMIT_IN_MATCH_OVER        (-17)  DEFAULT budget
 *                                                    10,000,000 (regint.h
 *                                                    DEFAULT_RETRY_LIMIT_IN_
 *                                                    MATCH) -- NOT
 *                                                    unlimited: a
 *                                                    catastrophic-
 *                                                    backtracking witness
 *                                                    CAN give up under
 *                                                    onig-default with no
 *                                                    special config.
 *   ONIGERR_RETRY_LIMIT_IN_SEARCH_OVER       (-18)
 *   ONIGERR_SUBEXP_CALL_LIMIT_IN_SEARCH_OVER (-19)
 * Deliberately NOT in that set:
 *   ONIGERR_MEMORY (-5) -- an allocation failure, not a configured budget
 *     (same reasoning as pcre2's -48; the adapter classifies it `crashed`).
 *   ONIGERR_PARSE_DEPTH_LIMIT_OVER (-16) -- raised in src/regparse.c, i.e.
 *     at COMPILE time (a parse-nesting-depth budget, DEFAULT 4096), so the
 *     adapter's ordinary `did-not-compile` path handles it; it can never
 *     reach this driver's match loop.
 * `onig_error_code_to_str` supplies the message text for every code this
 * driver did not expect, so a code the header adds later still prints a
 * real diagnostic instead of a blank one.
 *
 * [B148] L4 (docs/design/unusual_set_v1.md 6.2, 7.1-7.3):
 *   `--mode calls` -- a CALL STREAM over the whole subject, one onig_search
 *     per declared call starting at the call's offset (`--anchor-explicit`:
 *     onig_match there), replayed `--iters` times; the replay is
 *     timed_calls() in timed_calls.c (BD16), the tokens and the `stream`
 *     line are testees/common/calls_io.h's, after the clock.
 *   `--deep` -- the `deep` limits arm (lim-ceil1g): Oniguruma's GLOBAL
 *     setters, applied once after onig_initialize and before onig_new,
 *     outside every timed call: the match stack capped at the 1 GiB
 *     equivalent in STACK ELEMENTS (ONIG_DEEP_STACK_ELEMS below, Q-E), both
 *     retry limits and the subexp-call limit 0 (= unlimited, P10), and the
 *     subexp-call nest level 1,000,000 (P11; the default 20 answers
 *     SILENTLY WRONG past it, 6.3).
 *   `--limits` -- the six global getters READ BACK after the setters, as
 *     `info lim_*` lines (every arm).
 *   `--mem-pass` -- 6.4's `rss-delta`: an UNTIMED single pass; prints
 *     `mem<TAB>ID<TAB>BYTES<TAB>rss-delta<TAB>MAXRSS_KB` with BYTES the
 *     ru_maxrss growth across the subject's call(s) (a coarse upper bound:
 *     oniguruma.h has no high-water getter), then the subject's usual
 *     line(s) from that one untimed call.
 */

#include <oniguruma.h>

#include <errno.h>
#include <setjmp.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#include <sys/resource.h>

#include "timed.h"
#include "timed_calls.h"

#ifdef PB_CALLOUTS
/* [B148] L5 the callout driver (`onig_driver_co`, built -DPB_CALLOUTS with
 * callout_wrap.c, ../common/ub_bind.c and the ONE callees.o; the plain driver
 * has none of this). `--callees SPEC` binds each `(?{N})` site to a shared
 * callee (ub_bind.h) and sets callout_wrap.c's wrapper as Oniguruma's GLOBAL
 * progress callout, once, before onig_new and every timed call. */
#include "../common/ub_bind.h"
extern int pb_co_ncap;
int pb_onig_callout(OnigCalloutArgs *, void *);
#endif

/* [B148] L4 Q-E, MEASURED (docs/dev/lanes/b148l4_report.md "Q-E"): the match
 * stack limit counts STACK ELEMENTS; the 1 GiB equivalent is 1 GiB divided
 * by the measured bytes per element. */
#define ONIG_STACK_ELEM_BYTES   32   /* rss 3,200 KiB at a 100,000-element give-up = 32.8 B/elem incl. overhead; StackType = 2 ints + a 3-pointer union */
#define ONIG_DEEP_STACK_ELEMS   ((unsigned int)((1ULL << 30) / ONIG_STACK_ELEM_BYTES))
#define ONIG_DEEP_NEST_LEVEL    1000000

#define ONIG_DRIVER_SYNTAX  ONIG_SYNTAX_PERL_NG
/* [B77] U2 (utf8_set_v1.md 7.1): the DEFAULT encoding. `--encoding utf8`
 * selects ONIG_ENCODING_UTF8 at RUNTIME instead -- the `onig-utf8` config
 * only; every other config passes nothing and gets exactly this. */
#define ONIG_DRIVER_ENCODING ONIG_ENCODING_ASCII

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
 * note testees/pcre2/driver.c carries for the identical reason. */
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

static void emit_caps(OnigRegion *region, char *out, size_t outcap) {
    size_t off = 0;
    out[0] = 0;
    for (int i = 1; i < region->num_regs; i++) {
        long s = (region->beg[i] == ONIG_REGION_NOTPOS) ? -1 : (long)region->beg[i];
        long e = (region->end[i] == ONIG_REGION_NOTPOS) ? -1 : (long)region->end[i];
        int k = snprintf(out + off, outcap - off, "%s%ld:%ld",
                         i > 1 ? "," : "", s, e);
        if (k < 0 || (size_t)k >= outcap - off) break;
        off += (size_t)k;
    }
    if (!out[0]) { out[0] = '-'; out[1] = 0; }
}

static long maxrss_kb(void) {
    struct rusage ru;
    if (getrusage(RUSAGE_SELF, &ru) != 0) return -1;
    return ru.ru_maxrss;
}

static const char *onig_code_name(int rc) {
    switch (rc) {
    case ONIGERR_MATCH_STACK_LIMIT_OVER:           return "ONIGERR_MATCH_STACK_LIMIT_OVER";
    case ONIGERR_RETRY_LIMIT_IN_MATCH_OVER:        return "ONIGERR_RETRY_LIMIT_IN_MATCH_OVER";
    case ONIGERR_RETRY_LIMIT_IN_SEARCH_OVER:       return "ONIGERR_RETRY_LIMIT_IN_SEARCH_OVER";
    case ONIGERR_SUBEXP_CALL_LIMIT_IN_SEARCH_OVER: return "ONIGERR_SUBEXP_CALL_LIMIT_IN_SEARCH_OVER";
    case ONIGERR_MEMORY:                           return "ONIGERR_MEMORY";
    default:                                       return NULL;
    }
}

/* [B148] L4: --mode calls (header comment). */
static int run_calls(const char *list_path, regex_t *reg, long iters,
                     long subject_timeout, long skip, int anchor_explicit,
                     int mem_pass, const char *tokens_dir) {
    size_t nsub = 0;
    struct calls_subject *subs = calls_load_list(list_path, &nsub);
    if (!subs) return 2;
    OnigRegion *region = onig_region_new();
    if (!region) { printf("error\tonig_region_new failed\n"); return 2; }
    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);
    const int has_g1 = onig_number_of_captures(reg) >= 1;
    for (size_t i = (size_t)skip; i < nsub; i++) {
        struct calls_subject *s = &subs[i];
        struct call_res *res = calloc(s->ncalls, sizeof *res);
        if (!res) { printf("error\tcannot allocate %zu call results\n", s->ncalls); return 2; }
        volatile double elapsed = 0.0;
        struct tcalls_in tin = {
            .buf = s->buf, .len = s->len, .calls = s->calls, .ncalls = s->ncalls,
            .iters = mem_pass ? 1 : iters, .anchored = anchor_explicit,
            .has_g1 = has_g1, .reg = reg, .region = region, .res = res,
        };
        struct tcalls_out tout = { 0, 0 };
        long rss0 = maxrss_kb();
        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            elapsed = timed_calls(&tin, &tout);
            if (subject_timeout > 0) alarm(0);
        }
        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                   s->id, (long)tin.iters, (double)elapsed);
            free(res);
            continue;
        }
        if (mem_pass) {
            long rss1 = maxrss_kb();
            printf("mem\t%s\t%ld\trss-delta\t%ld\n", s->id,
                   (rss1 - rss0) * 1024L, rss1);
        }
        size_t matched = 0;
        int first_g = 0;
        for (size_t k = 0; k < s->ncalls; k++) {
            matched += res[k].kind == CALL_M;
            if (res[k].kind == CALL_G && !first_g) first_g = res[k].code;
        }
        printf("subject\t%s\tstream\t-\t-\t0\t%zu\t%ld\t%.9f\t%zu\t-\n",
               s->id, s->len, (long)tin.iters, (double)elapsed, matched);
        calls_report(s->id, res, s->ncalls, has_g1, tokens_dir,
                     first_g ? onig_code_name(first_g) : NULL);
        free(res);
    }
    onig_region_free(region, 1);
    return 0;
}

int main(int argc, char **argv) {
    const char *pattern_path = NULL, *list_path = NULL, *mode = "search";
    const char *form = "plain";
    /* `volatile` on everything the per-subject sigsetjmp/siglongjmp pair can
     * see across the jump -- C11 6.8.6.1's indeterminate-after-longjmp rule,
     * the same note testees/pcre2/driver.c carries. */
    volatile long iters = 1, subject_timeout = 0, skip = 0;
    long compile_trials = 1;
    volatile int find_all = 0;
    volatile int utf8_adv = 0;   /* [B77] U1: --utf8, the protocol flag */
    volatile long prime = 0;   /* [B129] --prime: one untimed call per subject before the timed loop */
    int deep = 0, limits = 0, anchor_explicit = 0;   /* [B148] L4 */
    volatile int mem_pass = 0;
    const char *tokens_dir = NULL;
    OnigEncoding enc = ONIG_DRIVER_ENCODING;   /* [B77] U2: --encoding */
    const char *enc_name = "ASCII";
#ifdef PB_CALLOUTS
    const char *callee_spec = NULL;                /* [B148] L5 */
#endif

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
        else if (!strcmp(a, "--utf8"))                      utf8_adv = 1;
        else if (!strcmp(a, "--prime"))                      prime = 1;
        else if (!strcmp(a, "--deep"))                       deep = 1;       /* [B148] L4 */
        else if (!strcmp(a, "--limits"))                     limits = 1;
        else if (!strcmp(a, "--mem-pass"))                   mem_pass = 1;
        else if (!strcmp(a, "--anchor-explicit"))            anchor_explicit = 1;
        else if (!strcmp(a, "--tokens-dir") && i + 1 < argc) tokens_dir = argv[++i];
#ifdef PB_CALLOUTS
        else if (!strcmp(a, "--callees") && i + 1 < argc)    callee_spec = argv[++i];
#endif
        else if (!strcmp(a, "--encoding") && i + 1 < argc) {
            const char *e = argv[++i];
            if (!strcmp(e, "utf8"))       { enc = ONIG_ENCODING_UTF8;  enc_name = "UTF8"; }
            else if (!strcmp(e, "ascii")) { enc = ONIG_ENCODING_ASCII; enc_name = "ASCII"; }
            else { printf("error\tunknown encoding %s\n", e); return 2; }
        }
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    if (!pattern_path) die("--pattern is required");
    if (iters < 1) iters = 1;
    int whole_subject = !strcmp(form, "whole-subject");
    /* `--mode` and `--form` are set TOGETHER by the adapter (`--form
     * whole-subject` iff `--mode match`; testees/onig/adapter.py's
     * `measure()`), because the whole-subject artifact's own `\z` suffix
     * plus this driver's `onig_match`-at-zero already supply BOTH halves
     * of "anchored AND end-anchored" -- there is no second, independent
     * anchoring dial `--mode` could still turn once `--form` is chosen.
     * Accepted (protocol compliance) and cross-checked here rather than
     * silently ignored, so a future adapter bug that decouples the two
     * flags fails LOUDLY instead of quietly measuring the wrong form. */
    const int calls_mode = !strcmp(mode, "calls");    /* [B148] L4 */
    if (calls_mode && (find_all || prime || utf8_adv || whole_subject)) {
        printf("error\t--mode calls takes none of --find-all, --prime, --utf8, "
               "--form whole-subject\n");
        return 2;
    }
    if (anchor_explicit && !calls_mode) {
        printf("error\t--anchor-explicit is a --mode calls flag\n");
        return 2;
    }
    if (list_path && !calls_mode) {
        int mode_wants_whole = !strcmp(mode, "match");
        if (mode_wants_whole != whole_subject)
            die("--mode and --form disagree (this driver has no anchoring "
                "dial independent of --form)");
    }

    setvbuf(stdout, NULL, _IOLBF, 0);

    OnigEncoding use_encs[1];
    use_encs[0] = enc;
    onig_initialize(use_encs, 1);

    /* [B148] L4: the deep arm's GLOBAL setters, before onig_new and outside
     * every timed call (header comment). A setter's failure is a refusal BY
     * NAME, never a silently default arm. */
    if (deep) {
        if (onig_set_match_stack_limit_size(ONIG_DEEP_STACK_ELEMS) != 0
            || onig_set_retry_limit_in_match(0) != 0
            || onig_set_retry_limit_in_search(0) != 0
            || onig_set_subexp_call_limit_in_search(0) != 0
            || onig_set_subexp_call_max_nest_level(ONIG_DEEP_NEST_LEVEL) != 0) {
            printf("error\t--deep: an Oniguruma global limit setter refused\n");
            return 2;
        }
    }
    if (limits) {
        printf("info\tlim_match_stack_elems\t%u\n", onig_get_match_stack_limit_size());
        printf("info\tlim_retry_in_match\t%lu\n", onig_get_retry_limit_in_match());
        printf("info\tlim_retry_in_search\t%lu\n", onig_get_retry_limit_in_search());
        printf("info\tlim_subexp_call_in_search\t%lu\n", onig_get_subexp_call_limit_in_search());
        printf("info\tlim_subexp_call_nest\t%d\n", onig_get_subexp_call_max_nest_level());
        printf("info\tlim_parse_depth\t%u\n", onig_get_parse_depth_limit());
        printf("info\tlim_stack_elem_bytes\t%d\n", ONIG_STACK_ELEM_BYTES);
    }

    {
        char verbuf[64];
        snprintf(verbuf, sizeof verbuf, "%s", onig_version());
        printf("info\tversion\t%s\n", verbuf);
    }
#ifdef PB_CALLOUTS
    if (!callee_spec) die("the callout driver needs --callees");
    {
        char err[256];
        if (ub_bind_parse(callee_spec, err, sizeof err)) {
            printf("error\t--callees: %s\n", err);
            return 2;
        }
        if (onig_set_progress_callout(pb_onig_callout) != ONIG_NORMAL) {
            printf("error\tonig_set_progress_callout refused\n");
            return 2;
        }
    }
    printf("info\tcallout_fn\ton\n");
#endif
    printf("info\tsyntax\tPERL_NG\n");
    printf("info\tencoding\t%s\n", enc_name);
    printf("info\tform\t%s\n", form);

    size_t patlen = 0;
    unsigned char *pat = slurp(pattern_path, &patlen);
    if (!pat) { printf("error\tcannot read pattern %s\n", pattern_path); return 2; }

    /* ---- compile, `compile_trials` times, the one phase timed ---- */
    regex_t *reg = NULL;
    for (long t = 1; t <= compile_trials; t++) {
        OnigErrorInfo einfo;
        regex_t *r = NULL;
        double t0 = now();
        int rc = onig_new(&r, pat, pat + patlen, ONIG_OPTION_DEFAULT,
                          enc, ONIG_DRIVER_SYNTAX, &einfo);
        double t1 = now();
        if (rc != ONIG_NORMAL) {
            unsigned char msg[ONIG_MAX_ERROR_MESSAGE_LEN];
            onig_error_code_to_str(msg, rc, &einfo);
            for (unsigned char *p = msg; *p; p++)
                if (*p == '\t' || *p == '\n') *p = ' ';
            printf("error\tonig_new failed (code %d): %s\n", rc, (char *)msg);
            return 3;
        }
        printf("compile\t%ld\tcompile\t%.9f\n", t, t1 - t0);
        if (reg) onig_free(reg);
        reg = r;
    }

    /* engine_metadata, `pattern`-scoped (record_schema.md 7 rule 2):
     * declared in testees/onig/adapter.py -- an undeclared pair is a
     * validator error, so the two lists move together. */
    printf("info\tcapturecount\t%d\n", onig_number_of_captures(reg));
    printf("info\tnames\t%d\n", onig_number_of_names(reg));
#ifdef PB_CALLOUTS
    pb_co_ncap = onig_number_of_captures(reg) + 1;
#endif

    if (!list_path) { fflush(stdout); return 0; }   /* compile-only run */

    if (calls_mode) {                                 /* [B148] L4 */
        int rc = run_calls(list_path, reg, iters, subject_timeout, skip,
                           anchor_explicit, mem_pass, tokens_dir);
        onig_free(reg);
        onig_end();
        fflush(stdout);
        return rc;
    }

    size_t nsub = 0;
    subject *subs = load_list(list_path, &nsub);
    if (!subs) { printf("error\tcannot read subject list %s\n", list_path); return 2; }

    OnigRegion *region = onig_region_new();
    if (!region) { printf("error\tonig_region_new failed\n"); return 2; }

    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);

    char caps[4096];

    for (size_t i = (size_t)skip; i < nsub; i++) {
        subject *s = &subs[i];
        volatile long   first_s = -1, first_e = -1, nmatch = -1;
        volatile int    rc_final = ONIG_MISMATCH;
        volatile double elapsed = 0.0;
        long rss0 = maxrss_kb();                     /* [B148] L4 --mem-pass */

        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            /* [B133] the timed loop is timed_run() in timed.c (its own
             * translation unit; see that file's header). */
            struct timed_in tin = {
                .buf = s->buf, .len = s->len, .iters = mem_pass ? 1 : iters,
                .prime = (int)prime, .find_all = find_all,
                .utf8_adv = utf8_adv, .whole_subject = whole_subject,
                .reg = reg, .region = region,
            };
            struct timed_out tout = { -1, -1, -1, ONIG_MISMATCH };
            elapsed = timed_run(&tin, &tout);
            first_s = tout.first_s; first_e = tout.first_e;
            nmatch = tout.nmatch; rc_final = tout.rc_final;
            if (subject_timeout > 0) alarm(0);
        }

        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                   s->id, (long)iters, (double)elapsed);
            continue;
        }
        if (mem_pass) {
            long rss1 = maxrss_kb();
            printf("mem\t%s\t%ld\trss-delta\t%ld\n", s->id,
                   (rss1 - rss0) * 1024L, rss1);
        }

        char answerbuf[256];
        const char *answer;
        char sbuf[32], ebuf[32], nbuf[32];
        int ncaps = 0;

        if (first_s >= 0) {
            answer = "match";
            emit_caps(region, caps, sizeof caps);
            ncaps = region->num_regs > 0 ? region->num_regs - 1 : 0;
            snprintf(sbuf, sizeof sbuf, "%ld", (long)first_s);
            snprintf(ebuf, sizeof ebuf, "%ld", (long)first_e);
        } else {
            strcpy(sbuf, "-");
            strcpy(ebuf, "-");
            caps[0] = '-'; caps[1] = 0;
            if (rc_final == ONIG_MISMATCH) {
                answer = "nomatch";
            } else {
                /* `giveup:<code>:<oniguruma's own message>`. The message
                 * comes from onig_error_code_to_str rather than a table in
                 * this file, so it cannot fall out of step with the
                 * library; the harness/adapter classifies on the CODE. */
                unsigned char emsg[ONIG_MAX_ERROR_MESSAGE_LEN];
                onig_error_code_to_str(emsg, rc_final);
                for (unsigned char *p = emsg; *p; p++)
                    if (*p == '\t' || *p == '\n') *p = ' ';
                snprintf(answerbuf, sizeof answerbuf, "giveup:%d:%s",
                         (int)rc_final, (char *)emsg);
                answer = answerbuf;
            }
        }
        if (find_all && nmatch >= 0) snprintf(nbuf, sizeof nbuf, "%ld", (long)nmatch);
        else strcpy(nbuf, "-");

        /* consumed_length: the length argument onig_search/onig_match was
         * given and accepted. See this file's header and
         * testees/onig/CLAUDE.md. */
        printf("subject\t%s\t%s\t%s\t%s\t%d\t%zu\t%ld\t%.9f\t%s\t%s\n",
               s->id, answer, sbuf, ebuf, ncaps,
               s->len, (long)iters, (double)elapsed, nbuf, caps);
    }

    onig_region_free(region, 1);
    onig_free(reg);
    onig_end();
    fflush(stdout);
    return 0;
}
