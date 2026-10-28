/* testees/assist/ub_runner.c -- THE ASSIST RUNNER: the driver protocol
 * (pcrecbench/adapters.py, read that first) around ONE assist file
 * ([B148] lane b148aw, docs/design/unusual_set_v1.md 5, 7.1-7.3).
 *
 * An assisted member's "driver" is this file + ub_timed.c (the timed loops,
 * their own TU) + the assist (bench/unusual/assists/<member>/<engine>/
 * assist.<ext>, C / C++ / a Rust staticlib) + the engine's library; for the
 * callout family also ../common/ub_bind.c and the ONE callees.o. Built by
 * pcrecbench/assists.py. The assist defines the functions of ub_assist.h;
 * everything else -- I/O, the protocol, the clock -- is here (the template's
 * fenced `main` only calls ub_main), so the
 * assist file holds only the counted logic and its fenced boilerplate.
 *
 * INVOCATION (the protocol's subset an assisted cell uses):
 *   --pattern FILE --member ID [--compile-trials T] [--phases a,b]
 *   [--has-g1 0|1] [--callees SPEC]
 *   --list FILE --mode search|calls --iters N [--find-all]
 *   [--tokens-dir DIR] [--subject-timeout S] [--skip N]
 * `--mode match`, `--prime`, `--utf8`, `--deep`, `--mem-pass` are refused BY
 * NAME (no assisted member runs the match regime; the high-water pass and
 * the deep arm are the native drivers'). In calls mode a 4-column list is a
 * VARS stream (testees/common/vars_io.h).
 *
 * COMPILE: `ub_setup` is the compile -- timed, once per compile trial, the
 * whole time attributed to the FIRST declared phase (`--phases`, the base
 * testee's compile_phases; any later phase prints 0: setup is one call).
 *
 * EXIT 0 all subjects reported; 2 usage/IO; 3 ub_setup failed. */
#include <setjmp.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#include "ub_assist.h"
#include "ub_timed.h"
#include "../common/calls_io.h"
#include "../common/vars_io.h"

#ifdef UB_CALLOUTS
#include "../common/ub_bind.h"
#endif

/* An assist defines only its family's functions; the others come from
 * ub_defaults.c, linked AFTER the assist as an ARCHIVE (one member per
 * symbol), so a member is pulled only for a symbol the assist left undefined
 * -- the rule that works for a Rust staticlib as for a C object. */

static char setup_err[512];
void ub_fail(const char *msg) {
    snprintf(setup_err, sizeof setup_err, "%s", msg ? msg : "");
}

/* ---- the binding lookup (vars) --------------------------------------- */
const ub_var *ub_lookup(const ub_var *v, size_t nv, const char *name) {
    for (size_t i = 0; i < nv; i++)
        if (!strcmp(v[i].name, name)) return v[i].p ? &v[i] : NULL;
    return NULL;
}

/* ---- the shared predicate (callouts) ---------------------------------- */
static int pred_site = -1;
#ifdef UB_CALLOUTS
int ub_pred(const unsigned char *subj, size_t n, size_t g1s, size_t g1e) {
    const struct ub_slot *sl = pred_site >= 0 ? &ub_slots[pred_site] : NULL;
    if (!sl || !sl->fn) {
        fprintf(stderr, "ub_pred: no callee bound to this member's site\n");
        abort();
    }
    /* the view a native callout at the site after group 1 would build:
     * pos = the end of group 1; the attempt start is not known here and is
     * read by no shared callee (callees.h) */
    ptrdiff_t caps[2][2] = { { -1, -1 }, { (ptrdiff_t)g1s, (ptrdiff_t)g1e } };
    struct ub_view v = { subj, n, g1e, 2, (const ptrdiff_t (*)[2])caps,
                         sl->user };
    return sl->fn(&v) == UB_CONTINUE;
}
#else
int ub_pred(const unsigned char *subj, size_t n, size_t g1s, size_t g1e) {
    (void)subj; (void)n; (void)g1s; (void)g1e;
    fprintf(stderr, "ub_pred: this runner was built without the callees\n");
    abort();
}
#endif

/* the first `(?C<digits>)` in the member's pattern: the site its predicate
 * is bound to (`--callees 1=luhn,...`). -1 when there is none. */
static int site_of(const unsigned char *p, size_t n) {
    for (size_t i = 0; i + 3 < n; i++)
        if (p[i] == '(' && p[i + 1] == '?' && p[i + 2] == 'C'
            && p[i + 3] >= '0' && p[i + 3] <= '9') {
            int v = 0;
            size_t j = i + 3;
            while (j < n && p[j] >= '0' && p[j] <= '9') v = v * 10 + (p[j++] - '0');
            if (j < n && p[j] == ')' && v < 256) return v;
        }
    return -1;
}

static double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

static sigjmp_buf timeout_jmp;
static void on_alarm(int sig) { (void)sig; siglongjmp(timeout_jmp, 1); }

typedef struct { char *id; unsigned char *buf; size_t len; } subject;

static subject *load_list(const char *path, size_t *n_out) {
    FILE *f = fopen(path, "r");
    if (!f) return NULL;
    size_t cap = 16, n = 0;
    subject *v = malloc(cap * sizeof *v);
    char line[8192];
    while (fgets(line, sizeof line, f)) {
        char *nl = strchr(line, '\n');
        if (nl) *nl = 0;
        if (!*line) continue;
        char *tab = strchr(line, '\t');
        if (!tab) { fclose(f); return NULL; }
        *tab = 0;
        if (n == cap) { cap *= 2; v = realloc(v, cap * sizeof *v); }
        v[n].id = strdup(line);
        v[n].buf = calls_slurp(tab + 1, &v[n].len);
        if (!v[n].buf) { fclose(f); return NULL; }
        n++;
    }
    fclose(f);
    *n_out = n;
    return v;
}

static int run_search(const char *list, long iters, int find_all,
                      long subject_timeout, long skip) {
    size_t nsub = 0;
    subject *subs = load_list(list, &nsub);
    if (!subs) { printf("error\tcannot read subject list %s\n", list); return 2; }
    for (size_t i = (size_t)skip; i < nsub; i++) {
        subject *s = &subs[i];
        struct ub_search_in in = { s->buf, s->len, iters, find_all, ub_find };
        struct ub_search_out out;
        memset(&out, 0, sizeof out);
        volatile double elapsed = 0.0;
        volatile int timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            elapsed = ub_timed_search(&in, &out);
            if (subject_timeout > 0) alarm(0);
        } else {
            timed_out = 1;
        }
        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                   s->id, iters, (double)elapsed);
            continue;
        }
        int rc = find_all ? (out.rc_final < 0 ? out.rc_final : out.rc) : out.rc;
        char ans[64], sb[32] = "-", eb[32] = "-", nb[32] = "-";
        if (rc < 0) snprintf(ans, sizeof ans, "giveup:%d", rc);
        else snprintf(ans, sizeof ans, "%s", rc == UB_M ? "match" : "nomatch");
        if (rc == UB_M) {
            snprintf(sb, sizeof sb, "%ld", out.first.s);
            snprintf(eb, sizeof eb, "%ld", out.first.e);
        }
        if (find_all && rc >= 0) snprintf(nb, sizeof nb, "%ld", out.nmatch);
        printf("subject\t%s\t%s\t%s\t%s\t0\t%zu\t%ld\t%.9f\t%s\t-\n",
               s->id, ans, sb, eb, s->len, iters, (double)elapsed, nb);
    }
    return 0;
}

static int run_calls(const char *list, long iters, int has_g1,
                     long subject_timeout, long skip, const char *tokens_dir) {
    size_t nsub = 0;
    struct calls_subject *subs = calls_load_list(list, &nsub);
    if (!subs) return 2;
    for (size_t i = (size_t)skip; i < nsub; i++) {
        struct calls_subject *s = &subs[i];
        struct call_res *res = calloc(s->ncalls ? s->ncalls : 1, sizeof *res);
        struct ub_calls_in in = { s->buf, s->len, s->calls, s->ncalls, iters,
                                  ub_find, res };
        struct ub_calls_out out = { 0, 0 };
        volatile double elapsed = 0.0;
        volatile int timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            elapsed = ub_timed_calls(&in, &out);
            if (subject_timeout > 0) alarm(0);
        } else {
            timed_out = 1;
        }
        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                   s->id, iters, (double)elapsed);
            free(res);
            continue;
        }
        size_t matched = 0;
        for (size_t k = 0; k < s->ncalls; k++) matched += res[k].kind == CALL_M;
        printf("subject\t%s\tstream\t-\t-\t0\t%zu\t%ld\t%.9f\t%zu\t-\n",
               s->id, s->len, iters, (double)elapsed, matched);
        calls_report(s->id, res, s->ncalls, has_g1, tokens_dir, NULL);
        free(res);
    }
    return 0;
}

static int run_vcalls(const char *list, long iters, long subject_timeout,
                      long skip, const char *tokens_dir) {
    size_t nsub = 0;
    struct vars_subject *subs = vars_load_list(list, &nsub);
    if (!subs) return 2;
    for (size_t i = (size_t)skip; i < nsub; i++) {
        struct vars_subject *s = &subs[i];
        struct call_res *res = calloc(s->ncalls ? s->ncalls : 1, sizeof *res);
        struct ub_vcalls_in in = { s->buf, s->calls, s->ncalls, s->bindings,
                                   iters, ub_vars, ub_reset, res };
        struct ub_calls_out out = { 0, 0 };
        volatile double elapsed = 0.0;
        volatile int timed_out = 0;
        ub_reset();                  /* every replay starts with an empty cache */
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            elapsed = ub_timed_vcalls(&in, &out);
            if (subject_timeout > 0) alarm(0);
        } else {
            timed_out = 1;
        }
        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                   s->id, iters, (double)elapsed);
            free(res);
            continue;
        }
        size_t matched = 0;
        for (size_t k = 0; k < s->ncalls; k++) matched += res[k].kind == CALL_M;
        printf("subject\t%s\tstream\t-\t-\t0\t%zu\t%ld\t%.9f\t%zu\t-\n",
               s->id, s->len, iters, (double)elapsed, matched);
        calls_report(s->id, res, s->ncalls, 0, tokens_dir, NULL);
        free(res);
    }
    return 0;
}

int ub_main(int argc, char **argv) {
    const char *pattern_path = NULL, *list = NULL, *mode = "search";
    const char *member = "", *phases = "compile", *tokens_dir = NULL;
    const char *callees = NULL;
    long iters = 1, compile_trials = 1, subject_timeout = 0, skip = 0;
    int find_all = 0, has_g1 = 0;
    for (int i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!strcmp(a, "--pattern") && i + 1 < argc) pattern_path = argv[++i];
        else if (!strcmp(a, "--member") && i + 1 < argc) member = argv[++i];
        else if (!strcmp(a, "--list") && i + 1 < argc) list = argv[++i];
        else if (!strcmp(a, "--mode") && i + 1 < argc) mode = argv[++i];
        else if (!strcmp(a, "--iters") && i + 1 < argc) iters = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--compile-trials") && i + 1 < argc) compile_trials = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--phases") && i + 1 < argc) phases = argv[++i];
        else if (!strcmp(a, "--has-g1") && i + 1 < argc) has_g1 = atoi(argv[++i]) != 0;
        else if (!strcmp(a, "--callees") && i + 1 < argc) callees = argv[++i];
        else if (!strcmp(a, "--tokens-dir") && i + 1 < argc) tokens_dir = argv[++i];
        else if (!strcmp(a, "--subject-timeout") && i + 1 < argc) subject_timeout = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--skip") && i + 1 < argc) skip = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--find-all")) find_all = 1;
        else if (!strcmp(a, "--prime") || !strcmp(a, "--utf8") || !strcmp(a, "--deep")
                 || !strcmp(a, "--mem-pass") || !strcmp(a, "--anchor-explicit")) {
            printf("error\t%s: not an assist-runner flag (the native drivers' only)\n", a);
            return 2;
        }
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    if (!pattern_path) { printf("error\t--pattern is required\n"); return 2; }
    const int calls = !strcmp(mode, "calls");
    if (list && !calls && strcmp(mode, "search")) {
        printf("error\t--mode %s: an assist answers search, find-all and calls only\n", mode);
        return 2;
    }
    if (calls && find_all) { printf("error\t--mode calls takes no --find-all\n"); return 2; }
    if (iters < 1) iters = 1;
    setvbuf(stdout, NULL, _IOLBF, 0);
    printf("info\tversion\tub-runner-1\n");
    printf("info\tassist_member\t%s\n", member);

    size_t plen = 0;
    unsigned char *pat = calls_slurp(pattern_path, &plen);
    if (!pat) return 2;
    pred_site = site_of(pat, plen);
#ifdef UB_CALLOUTS
    if (callees) {
        char err[256];
        if (ub_bind_parse(callees, err, sizeof err)) {
            printf("error\t--callees: %s\n", err);
            return 2;
        }
    }
#else
    if (callees) { printf("error\t--callees: this runner has no callees linked\n"); return 2; }
#endif

    char first_phase[64];
    {
        const char *c = strchr(phases, ',');
        size_t k = c ? (size_t)(c - phases) : strlen(phases);
        if (k >= sizeof first_phase) k = sizeof first_phase - 1;
        memcpy(first_phase, phases, k);
        first_phase[k] = 0;
    }
    for (long t = 1; t <= compile_trials; t++) {
        setup_err[0] = 0;
        double t0 = now();
        int rc = ub_setup(pat, plen, member);
        double t1 = now();
        if (rc != 0) {
            for (char *p = setup_err; *p; p++) if (*p == '\t' || *p == '\n') *p = ' ';
            printf("error\tub_setup failed (%d): %s\n", rc,
                   setup_err[0] ? setup_err : "no reason given");
            return 3;
        }
        printf("compile\t%ld\t%s\t%.9f\n", t, first_phase, t1 - t0);
        const char *rest = strchr(phases, ',');
        while (rest) {
            const char *nx = strchr(rest + 1, ',');
            int k = nx ? (int)(nx - rest - 1) : (int)strlen(rest + 1);
            printf("compile\t%ld\t%.*s\t0.000000000\n", t, k, rest + 1);
            rest = nx;
        }
    }
    if (!list) return 0;

    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);
    if (calls)
        return vars_list_has_bindings(list)
            ? run_vcalls(list, iters, subject_timeout, skip, tokens_dir)
            : run_calls(list, iters, has_g1, subject_timeout, skip, tokens_dir);
    return run_search(list, iters, find_all, subject_timeout, skip);
}

