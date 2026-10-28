/* testees/pcre2/driver.c -- the libpcre2 batched in-process timing driver.
 *
 * Implements the DRIVER PROTOCOL in pcrecbench/adapters.py verbatim; read
 * that first. This file's own decisions:
 *
 * WHY dlopen AND HAND-DECLARED PROTOTYPES. This box has the PCRE2 8-bit
 * RUNTIME (libpcre2-8.so.0) but not the -dev package: no pcre2.h, no
 * unversioned .so, no pkg-config file. The precedent is pcrec's
 * tests/fuzz/pcre2_abi.h and the email specimen's pcre2_throughput.c, and the
 * function subset below is theirs -- read off the library's exported symbols,
 * nothing guessed. Constants that are not symbols (the option bits, the error
 * codes, PCRE2_CONFIG_VERSION) carry a [measured] note where the value was
 * established by probing rather than read from a header.
 *
 * COMPILE PHASES. `compile` (pcre2_compile_8) always; `jit-compile`
 * (pcre2_jit_compile_8) additionally when --jit. Both timed IN-DRIVER, which
 * is what an eager-JIT's compile cost is (requirements 3).
 *
 * --dfa ([B42] L6a, 2026-09-16): a THIRD execution model on the SAME
 * compiled pattern -- pcre2_dfa_match_8 instead of pcre2_match_8, chosen at
 * MATCH time, never at compile time (`pcre2_compile_8` does not know or
 * care which matcher will be used; testees/pcre2/CLAUDE.md's "pcre2-dfa"
 * section states the full semantics). Three consequences for this file:
 *   (1) a match_data block for DFA is NOT created from the pattern (man
 *       `pcre2_dfa_match`: "the size of vector needed ... depends on the
 *       number of simultaneous matches, not on the number of parentheses
 *       ... therefore not advisable") -- `pcre2_match_data_create_8` with a
 *       small fixed oveccount instead, since this driver reads only the
 *       FIRST (longest) match's span either way (below).
 *   (2) `pcre2_dfa_match` needs a caller-owned WORKSPACE (`workspace`,
 *       `wscount`) with no relation to subject length or capture count --
 *       malloc'd once, sized generously (`DFA_WS_ELEMS`, its own comment).
 *   (3) the ovector's [0]/[1] pair is ALWAYS the LONGEST match at the
 *       leftmost successful start point regardless of how many
 *       SIMULTANEOUS matches were found there (man `pcre2_dfa_match`:
 *       "stored ... in reverse order of length; the longest matching
 *       string is first" -- true whether the return code is the exact
 *       count or 0, "too many to fit, filled with the longest"). So the
 *       existing rc>=0-is-a-match / ov[0..1]-is-the-span structure below
 *       needs NO change for DFA -- only the match CALL itself branches
 *       (`do_match`), and the CAPTURES reporting is forced to "none" (man
 *       item 2: "no captured substrings are available" -- DFA_UITEM/
 *       DFA_UCOND/DFA_UINVALID_UTF, the STRUCTURAL refusals a pattern the
 *       DFA route cannot run at all raises, and DFA_WSSIZE/DFA_RECURSE, the
 *       RESOURCE-shaped ones, all surface through the SAME
 *       `giveup:<code>:<message>` protocol every other negative code
 *       already uses below -- classified `gave-up` vs `crashed` by the
 *       ADAPTER's per-testee code set (testees/pcre2/adapter.py), never in
 *       this file.
 *
 * consumed_length: the LENGTH ARGUMENT the driver passed and pcre2 accepted,
 * i.e. the whole subject. pcre2_match takes a size_t length and has no
 * subject-size ceiling to truncate against, and the API exposes no scan
 * high-water mark -- so the honest claim is "the engine was given and
 * accepted N bytes", never "the engine looked at N bytes". testees/pcre2/
 * CLAUDE.md states this where a reader of the numbers will find it.
 *
 * VALIDATE-ONCE ([B94], docs/dev/decisions.md BD15, 2026-09-26). Under
 * PCRE2_UTF, libpcre2 re-validates the subject as a UTF-8 string on every
 * pcre2_match/pcre2_dfa_match call (man pcre2api, "PCRE2_NO_UTF_CHECK":
 * "the validity of the subject as a UTF string is checked unless
 * PCRE2_NO_UTF_CHECK is passed"). A find-all loop calls the matcher once per
 * match found, each call re-checking from its own start offset to the END of
 * the subject -- quadratic in the subject's length. utf8@0.1's first window
 * lost pcre2-utf-interp and pcre2-utf-jit to the 5400 s CELL_CAP over this.
 * Frank's ruling (BD15): "keeping the check handicaps pcre2 times, so I want
 * it removed after the first." The fix mirrors BD14's oracle
 * (pcrecbench/oracle_pcre2.py's `_find_all_impl`, NOT shared code -- the
 * testee and the oracle stay independently implemented): call 1 of a
 * find-all runs at offset 0 WITHOUT PCRE2_NO_UTF_CHECK, so libpcre2 validates
 * the WHOLE subject itself (an ill-formed subject is refused there, loudly,
 * by the existing `giveup:<code>:<message>` protocol -- never silently);
 * calls 2..n on the SAME buffer pass PCRE2_NO_UTF_CHECK, with every such
 * start offset ASSERTED (`die()`, never silently trusted) to be a character
 * boundary first. man pcre2api's own "PCRE2_NO_UTF_CHECK" section, under
 * "Option bits for pcre2_match()", recommends EXACTLY this caller shape:
 * "You might want to do this for the second and subsequent calls to
 * pcre2_match() if you are making repeated calls to find multiple matches in
 * the same subject string." The SAME section states JIT honours every
 * match-time option "apart from PCRE2_NO_JIT (obviously)" -- and this driver
 * never calls a separate pcre2_jit_match: pcre2_match() itself dispatches to
 * the JIT-compiled code internally when present (man pcre2jit), so ONE call
 * site (`do_match`) and one flag cover pcre2-utf-interp and pcre2-utf-jit
 * alike, measured, not assumed
 * (docs/dev/measurements/2026-09-26-b94-pcre2-driver-validate-once.txt). The
 * DFA route (`pcre2_dfa_match`) honours PCRE2_NO_UTF_CHECK too (man
 * pcre2api, "Option bits for pcre2_dfa_match()": "All but the last four of
 * these are exactly the same as for pcre2_match()"), so `do_match`'s single
 * branch point covers it as well.
 *
 * The single-call regimes (`search`/`match`, no --find-all) are UNCHANGED:
 * one pcre2_match/pcre2_dfa_match call per iteration, always at offset 0 on
 * the same immutable subject buffer -- each call independently pays the
 * O(subject length) validation cost once, never compounding across
 * increasing start offsets the way a find-all loop does. Measured, not
 * assumed: docs/dev/measurements/2026-09-26-b94-pcre2-driver-validate-once.txt
 * (the "search regime" section).
 *
 * `--mode subst` ([B140], docs/design/subst_bench_v1.md 3.1, 3.1.1, 3.1.2): a
 * TRANSFORM, not a match -- pcre2_substitute(GLOBAL [| EXTENDED]) over the
 * whole subject, the OUTPUT being the answer. Everything it adds is below the
 * `run_subst()` banner and the timed call is timed_subst() in timed_subst.c
 * (its own translation unit, BD16's discipline; timed.c is untouched). The
 * protocol additions (pcrecbench/adapters.py): `--template FILE` (raw bytes,
 * ALREADY PCRE2's dialect -- the harness rendered the neutral template),
 * `--subst-flags extended|none`, `--bound ID=BYTES` (the output buffer
 * capacity per subject: n + 8 * the oracle's substitution count + 1, the
 * charter's engine-neutral bound), `--sizing bound|first` (the PCRE2
 * OVERFLOW_LENGTH arm), `--out-dir DIR` (trial 1 only: the output is written
 * to DIR/ID.out OUTSIDE the clock and announced on an `out` line). iters is
 * always 1. --find-all, --prime, --dfa and --utf8 are REFUSED in this mode
 * by name (they have no meaning for a transform). The existing modes are not
 * touched: nothing in main() runs differently unless --mode is `subst`.
 *
 * `--mode calls` ([B148] L4, docs/design/unusual_set_v1.md 7.1-7.3): a CALL
 * STREAM -- one pcre2_match_8 per declared call at the call's offset over the
 * WHOLE subject (`\G` anchors there), replayed `--iters` times, each replay
 * clocked separately and summed. The replay is timed_calls() in
 * timed_calls.c (its own translation unit, BD16); run_calls() below loads
 * the streams, spells the result tokens after the clock and prints the
 * `stream` line (testees/common/calls_io.h). `--anchor-explicit` passes
 * PCRE2_ANCHORED on every call (7.1's O(segment) fallback).
 *
 * `--deep` ([B148] L4, 6.1-6.2, the `lim-ceil1g` arm): ONE match context,
 * created before any timed call: pcre2_set_heap_limit(1048576 KiB = 1 GiB),
 * pcre2_set_match_limit / pcre2_set_depth_limit(UINT32_MAX) (P10: counters
 * unbounded, storage capped), and under --jit a JIT stack of 32 KiB growing
 * to 1 GiB (pcre2_jit_stack_create + pcre2_jit_stack_assign). The calls mode
 * hands it to timed_calls directly; the search/throughput modes hand
 * timed.c (BD16, untouched) timed_ctx.c's forwarder as `match`, which
 * substitutes the context for the NULL timed.c passes. Absent, every mode's
 * code path is exactly what it was (a NULL context = the library defaults =
 * the `default` arm).
 *
 * `--limits` ([B148] L4, 6.2): print the effective limits as `info lim_*`.
 * libpcre2 has NO getter on a match context, so the READ-BACK is
 * pcre2_config_8 (the library defaults the `default` arm runs under) and
 * pcre2_pattern_info_8 (a pattern's own (*LIMIT_...) settings, printed only
 * when set); the `deep` arm's values are the ones this driver SET (the
 * adapter declares which is which).
 *
 * `--mem-pass` ([B148] L4, 6.4): an UNTIMED high-water pass instead of a
 * measurement -- one call per subject (calls mode: every call once), the
 * interpreter's match context built on a COUNTING general context (peak live
 * bytes of every allocation libpcre2 makes through it: heap frames, `deep`
 * or not), the JIT's stack measured by mincore(2) over its mapping (found by
 * diffing /proc/self/maps around pcre2_jit_stack_create). Prints `mem<TAB>ID
 * <TAB>BYTES<TAB>METHOD<TAB>MAXRSS_KB` per subject, then the subject's usual
 * line(s) from that one untimed call (the harness pairs them, driverrun.py).
 *
 * `--utf-always-check` is a DRIVER-ONLY flag (never part of the driver
 * PROTOCOL in pcrecbench/adapters.py, never passed by testees/pcre2/
 * adapter.py) that disables validate-once and restores the always-check
 * path -- reachable ONLY by `make check-harness`'s control, which compares
 * the two paths' answers for identity.
 */

#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <setjmp.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#include <sys/mman.h>
#include <sys/resource.h>

#include "timed.h"
#include "timed_subst.h"
#include "timed_calls.h"

/* [B148] L4 timed_ctx.c: the deep arm's forwarder for timed.c's `match`. */
extern void *timed_ctx_mctx;
extern int (*timed_ctx_match)(void *, const unsigned char *, size_t, size_t,
                              uint32_t, void *, void *);
int timed_ctx_forward(void *, const unsigned char *, size_t, size_t, uint32_t,
                      void *, void *);

/* ---- the hand-declared 8-bit ABI slice (pcrec tests/fuzz/pcre2_abi.h) ---- */

typedef size_t PCRE2_SIZE;

static int      (*p_config)(uint32_t, void *);
static void    *(*p_compile)(const unsigned char *, size_t, uint32_t, int *,
                             size_t *, void *);
static int      (*p_jit_compile)(void *, uint32_t);
static void    *(*p_match_data_create_from_pattern)(void *, void *);
static int      (*p_match)(void *, const unsigned char *, size_t, size_t,
                           uint32_t, void *, void *);
static int      (*p_dfa_match)(void *, const unsigned char *, size_t, size_t,
                               uint32_t, void *, void *, int *, size_t);
static void    *(*p_match_data_create)(uint32_t, void *);
static size_t  *(*p_get_ovector_pointer)(void *);
static uint32_t (*p_get_ovector_count)(void *);
static void     (*p_match_data_free)(void *);
static void     (*p_code_free)(void *);
static int      (*p_get_error_message)(int, unsigned char *, size_t);
static int      (*p_pattern_info)(const void *, uint32_t, void *);
/* [B148] L4: the match context, its limits, the JIT stack, and a general
 * context for the counting allocator (--mem-pass). */
static void    *(*p_general_context_create)(void *(*)(size_t, void *),
                                            void (*)(void *, void *), void *);
static void    *(*p_match_context_create)(void *);
static int      (*p_set_match_limit)(void *, uint32_t);
static int      (*p_set_depth_limit)(void *, uint32_t);
static int      (*p_set_heap_limit)(void *, uint32_t);
static void    *(*p_jit_stack_create)(size_t, size_t, void *);
static void     (*p_jit_stack_assign)(void *, void *(*)(void *), void *);
static int      (*p_substitute)(void *, const unsigned char *, size_t, size_t,
                                uint32_t, void *, void *,
                                const unsigned char *, size_t,
                                unsigned char *, size_t *);   /* [B140] */

#define PCRE2_ERROR_NOMATCH   (-1)
#define PCRE2_UNSET           ((size_t)-1)
/* [B148] L4: read straight off /usr/include/pcre2.h (10.46) like the DFA
 * codes below: the three limit getters and PCRE2_ERROR_UNSET (no
 * pattern-embedded limit). */
#define PCRE2_ERROR_UNSET          (-55)
#define PCRE2_CONFIG_MATCHLIMIT    4u
#define PCRE2_CONFIG_DEPTHLIMIT    7u
#define PCRE2_CONFIG_HEAPLIMIT     12u
#define PCRE2_INFO_MATCHLIMIT      14u
#define PCRE2_INFO_DEPTHLIMIT      21u
#define PCRE2_INFO_HEAPLIMIT       25u
/* 6.2's deep arm: 1 GiB of matcher working storage (heap limit in KiB; the
 * JIT stack in bytes), every counter at its type maximum. */
#define DEEP_HEAP_KIB         1048576u
#define DEEP_JIT_STACK_MAX    ((size_t)1 << 30)
#define DEEP_JIT_STACK_START  ((size_t)32 * 1024)
/* pcre2jit(3) "CONTROLLING THE JIT STACK": with no assigned stack the JIT
 * uses 32 KiB on the machine stack -- documented, not readable. */
#define DEFAULT_JIT_STACK     ((size_t)32 * 1024)
/* [measured] the two anchoring bits and PCRE2_CONFIG_VERSION were established
 * by probing this box's libpcre2 10.46 (pcrecbench/oracle_pcre2.py's
 * self-check asserts the anchoring behaviour rather than the numbers). */
#define PCRE2_ANCHORED        0x80000000u
#define PCRE2_ENDANCHORED     0x20000000u
#define PCRE2_JIT_COMPLETE    0x00000001u
#define PCRE2_CONFIG_VERSION  11u
/* [B77] U1 (docs/design/utf8_set_v1.md 8): the two compile-time option bits
 * the utf8 set's oracle word can carry, the same values
 * pcrecbench/oracle_pcre2.py measured on this box's 10.46 (UTF alone leaves
 * `\w` ASCII-scoped over e-acute; UTF|UCP widens it). */
#define PCRE2_UTF             0x00080000u
#define PCRE2_UCP             0x00020000u
/* [B94] (docs/dev/decisions.md BD15): the VALIDATE-ONCE match-time option --
 * [measured] value 0x40000000, the same one pcrecbench/oracle_pcre2.py
 * measured on this box's 10.46 (docs/dev/measurements/2026-09-25-b77u5-
 * validate-once-probe.txt), independently re-measured here
 * (docs/dev/measurements/2026-09-26-b94-pcre2-driver-validate-once.txt).
 * Never part of the compile-time
 * options word; passed only at match time, only under PCRE2_UTF, only on
 * calls 2..n of one find-all loop over the SAME immutable subject buffer,
 * only after call 1 (offset 0, WITHOUT this flag) completed -- i.e. after
 * libpcre2 itself validated the whole subject. This file's header comment
 * has the full rule and the man pcre2api citations. */
#define PCRE2_NO_UTF_CHECK    0x40000000u
/* [B140] pcre2_substitute's option bits -- read straight off the installed
 * /usr/include/pcre2.h (10.46), the same way the DFA error codes below are. */
#define PCRE2_SUBSTITUTE_GLOBAL    0x00000100u
#define PCRE2_SUBSTITUTE_EXTENDED  0x00000200u

/* [verified] 2026-09-16 ([B42] L6a): this box now HAS libpcre2-dev (a side
 * finding of docs/dev/research/2026-09-12-b42-engine-landscape.md (3),
 * unactioned there), so these five are read straight off
 * /usr/include/pcre2.h and independently reproduced live with
 * `pcre2test -dfa` (a backreference atom and `\K` both raise -42; a
 * backreference-CONDITION raises -40 -- testees/pcre2/CLAUDE.md's
 * "pcre2-dfa" section has the transcript) rather than probed blind, the
 * discipline every other constant in this file states for itself. The
 * two STRUCTURAL refusals `pcre2_compile_8` cannot see (a construct
 * `pcre2_dfa_match` never supports, at any subject) and the three
 * RESOURCE-shaped ones (this driver's own budgets, not the pattern's
 * fault) are told apart in testees/pcre2/adapter.py's own comment, not
 * here -- this file emits every one of them through the SAME
 * `giveup:<code>:<message>` line every other negative code already uses. */
#define PCRE2_ERROR_DFA_BADRESTART    (-38)  /* unreachable: no --dfa-restart */
#define PCRE2_ERROR_DFA_RECURSE       (-39)  /* resource-shaped, "extremely rare" */
#define PCRE2_ERROR_DFA_UCOND         (-40)  /* structural: backref/recursion cond */
#define PCRE2_ERROR_DFA_UFUNC         (-41)  /* unreachable: no substring-by-name call */
#define PCRE2_ERROR_DFA_UITEM         (-42)  /* structural: e.g. a backref, \K */
#define PCRE2_ERROR_DFA_WSSIZE        (-43)  /* resource-shaped: our own workspace */
#define PCRE2_ERROR_DFA_UINVALID_UTF  (-66)  /* unreachable: never compiled with it */
/* Chosen generously against this project's own worst case
 * (bench/bounded's `cls-upto-65535` = `[a-z]{0,65535}`): `pcre2test -dfa`
 * matches it cleanly against a 70,000-byte all-matching subject in
 * single-digit milliseconds with no workspace complaint. A real
 * exhaustion is PCRE2_ERROR_DFA_WSSIZE above, a first-class per-subject
 * outcome (never assumed impossible), not a crash. */
#define PCRE2_DFA_WS_ELEMS    100000

/* [measured] 2026-08-25 on this box's libpcre2 10.46, by the same discipline
 * pcrec's tests/fuzz/pcre2_abi.h uses for PCRE2_INFO_CAPTURECOUNT (its
 * [M4.7d] note): probe `pcre2_pattern_info_8(code, N, &v)` and keep the N
 * whose value is consistent across patterns chosen to distinguish it.
 *   4  CAPTURECOUNT -- `a(b|c)+d`->1, `(x)(y)(z)`->3, `abc`->0, and the two
 *      email patterns ->0 and ->4. Written as a uint32_t, NOT a size_t:
 *      reading it into a size_t leaves garbage in the high half.
 *   22 SIZE -- the compiled block, size_t: 178 / 189 / 165 for the three
 *      small patterns and 1609 / 951 for the two email patterns.
 *   10 JITSIZE -- size_t, and the decisive control: 0 on every pattern
 *      BEFORE pcre2_jit_compile_8 and 3910 / 4467 after. */
#define PCRE2_INFO_CAPTURECOUNT 4u
#define PCRE2_INFO_SIZE        22u
#define PCRE2_INFO_JITSIZE     10u

/* --------------------------------------------------------------- helpers */

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
 * and warns that its locals `might be clobbered by longjmp`. */
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

/* ------------------------------------------- run_subst: --mode subst ([B140]) */

#define SUBST_MAX_BOUNDS 64

struct subst_args {
    const char *template_path, *out_dir;
    int extended, size_first;
    long subject_timeout, skip;
    int nbounds;
    char *bound_id[SUBST_MAX_BOUNDS];
    size_t bound_cap[SUBST_MAX_BOUNDS];
};

static int subst_bound_for(const struct subst_args *a, const char *id, size_t *cap) {
    for (int i = 0; i < a->nbounds; i++)
        if (!strcmp(a->bound_id[i], id)) { *cap = a->bound_cap[i]; return 1; }
    return 0;
}

/* Writes DIR/ID.out; 0 on success. Outside the clock, after the subject line. */
static int write_out_file(const char *dir, const char *id,
                          const unsigned char *buf, size_t n, char *path_out,
                          size_t path_cap) {
    snprintf(path_out, path_cap, "%s.out", id);
    char full[4096];
    snprintf(full, sizeof full, "%s/%s", dir, path_out);
    FILE *f = fopen(full, "wb");
    if (!f) return -1;
    size_t w = n ? fwrite(buf, 1, n, f) : 0;
    int rc = (w == n) ? 0 : -1;
    if (fclose(f) != 0) rc = -1;
    return rc;
}

/* noinline: sigsetjmp lives here, as in main(); see load_list's note. */
__attribute__((noinline))
static int run_subst(void *code, const char *list_path, const struct subst_args *a) {
    size_t replen = 0;
    unsigned char *repl = slurp(a->template_path, &replen);
    if (!repl) { printf("error\tcannot read template %s\n", a->template_path); return 2; }
    if (!p_substitute) { printf("error\tdlsym: pcre2_substitute_8 is missing\n"); return 2; }
    size_t nsub = 0;
    subject *subs = load_list(list_path, &nsub);
    if (!subs) { printf("error\tcannot read subject list %s\n", list_path); return 2; }
    void *md = p_match_data_create_from_pattern(code, NULL);
    if (!md) { printf("error\tmatch_data_create failed\n"); return 2; }

    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);

    const uint32_t opts = PCRE2_SUBSTITUTE_GLOBAL
                        | (a->extended ? PCRE2_SUBSTITUTE_EXTENDED : 0u);

    for (size_t i = (size_t)a->skip; i < nsub; i++) {
        subject *s = &subs[i];
        size_t cap = 0;
        if (!subst_bound_for(a, s->id, &cap)) {
            printf("error\tno --bound for subject %s\n", s->id);
            return 2;
        }
        /* The output arena: sized to the bound, then FAULTED IN before the
         * clock (a fresh 400 MB mapping would otherwise charge its page
         * faults to whichever call first writes it). */
        unsigned char *out = malloc(cap ? cap : 1);
        if (!out) { printf("error\tmalloc %zu failed\n", cap); return 2; }
        memset(out, 0, cap ? cap : 1);

        volatile int    rc_final = 0;
        volatile size_t outlen = 0;
        volatile double elapsed = 0.0;
        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (a->subject_timeout > 0) alarm((unsigned)a->subject_timeout);
            struct tsubst_in tin = {
                .buf = s->buf, .len = s->len, .repl = repl, .repl_len = replen,
                .opts = opts, .size_first = a->size_first, .iters = 1,
                .code = code, .md = md, .out = out, .cap = cap,
                .subst = p_substitute,
            };
            struct tsubst_out tout = { 0, 0 };
            elapsed = timed_subst(&tin, &tout);
            rc_final = tout.rc;
            outlen = tout.outlen;
            if (a->subject_timeout > 0) alarm(0);
        }
        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t1\t%.9f\t-\t-\n",
                   s->id, (double)elapsed);
            free(out);
            continue;
        }
        if (rc_final < 0) {
            char answerbuf[256];
            unsigned char emsg[160];
            int en = (rc_final > -1000)
                   ? p_get_error_message(rc_final, emsg, sizeof emsg) : 0;
            if (en > 0) {
                for (int k = 0; emsg[k]; k++)
                    if (emsg[k] == '\t' || emsg[k] == '\n') emsg[k] = ' ';
                snprintf(answerbuf, sizeof answerbuf, "giveup:%d:%s",
                         (int)rc_final, (char *)emsg);
            } else if (rc_final == -1000) {
                snprintf(answerbuf, sizeof answerbuf, "giveup:%d:size-first "
                         "output larger than the bound-sized arena",
                         (int)rc_final);
            } else {
                snprintf(answerbuf, sizeof answerbuf, "giveup:%d", (int)rc_final);
            }
            printf("subject\t%s\t%s\t-\t-\t0\t%zu\t1\t%.9f\t-\t-\n",
                   s->id, answerbuf, s->len, (double)elapsed);
            free(out);
            continue;
        }
        printf("subject\t%s\t%s\t-\t-\t0\t%zu\t1\t%.9f\t%d\t-\n",
               s->id, rc_final > 0 ? "match" : "nomatch", s->len,
               (double)elapsed, (int)rc_final);
        /* ---- outside the clock: announce (and on trial 1, write) the output */
        char pathbuf[512] = "-";
        if (a->out_dir &&
            write_out_file(a->out_dir, s->id, out, outlen, pathbuf,
                           sizeof pathbuf) != 0) {
            printf("error\tcannot write %s/%s.out: %s\n", a->out_dir, s->id,
                   strerror(errno));
            return 2;
        }
        printf("out\t%s\t%s\t%zu\n", s->id, pathbuf, (size_t)outlen);
        free(out);
    }
    p_match_data_free(md);
    free(repl);
    fflush(stdout);
    return 0;
}

/* ------------------------------------------------------------------- main */

/* ------------------------------------- [B148] L4 the deep arm + mem pass */

/* The counting allocator (--mem-pass, interpreter): peak live bytes through
 * the general context. A size header in front of each block, so free() knows
 * what it releases. Untimed by construction (the pass prints no SECONDS). */
static size_t mem_live, mem_peak;
static void *count_malloc(size_t n, void *u) {
    (void)u;
    size_t *p = malloc(n + sizeof(size_t) * 2);
    if (!p) return NULL;
    p[0] = n;
    mem_live += n;
    if (mem_live > mem_peak) mem_peak = mem_live;
    return p + 2;
}
static void count_free(void *q, void *u) {
    (void)u;
    if (!q) return;
    size_t *p = (size_t *)q - 2;
    mem_live -= p[0];
    free(p);
}

/* The JIT stack's MAPPING (--mem-pass, JIT): every /proc/self/maps range
 * present after pcre2_jit_stack_create and absent before it. sljit mmaps
 * the stack's whole MAXIMUM reservation and commits by touch, so resident
 * pages of the new range(s) = the stack's high-water at page grain. */
#define MAXMAPS 4096
static int read_maps(unsigned long (*v)[2], int cap) {
    FILE *f = fopen("/proc/self/maps", "r");
    if (!f) return 0;
    int n = 0;
    char line[512];
    while (n < cap && fgets(line, sizeof line, f)) {
        unsigned long a, b;
        if (sscanf(line, "%lx-%lx", &a, &b) == 2) { v[n][0] = a; v[n][1] = b; n++; }
    }
    fclose(f);
    return n;
}
static unsigned long jit_maps[16][2];
static int njit_maps;
static void *jit_stack_tracked(void *gctx) {
    static unsigned long before[MAXMAPS][2], after[MAXMAPS][2];
    int nb = read_maps(before, MAXMAPS);
    void *st = p_jit_stack_create(DEEP_JIT_STACK_START, DEEP_JIT_STACK_MAX, gctx);
    int na = read_maps(after, MAXMAPS);
    njit_maps = 0;
    for (int i = 0; i < na && njit_maps < 16; i++) {
        int seen = 0;
        for (int j = 0; j < nb; j++)
            if (before[j][0] == after[i][0] && before[j][1] == after[i][1]) { seen = 1; break; }
        if (!seen) { jit_maps[njit_maps][0] = after[i][0]; jit_maps[njit_maps][1] = after[i][1]; njit_maps++; }
    }
    return st;
}
static size_t jit_resident_bytes(void) {
    long pg = sysconf(_SC_PAGESIZE);
    size_t total = 0;
    for (int i = 0; i < njit_maps; i++) {
        size_t len = jit_maps[i][1] - jit_maps[i][0];
        size_t np = (len + (size_t)pg - 1) / (size_t)pg;
        unsigned char *vec = malloc(np);
        if (!vec) continue;
        if (mincore((void *)jit_maps[i][0], len, vec) == 0)
            for (size_t k = 0; k < np; k++) if (vec[k] & 1) total += (size_t)pg;
        free(vec);
    }
    return total;
}
static void *jit_stack_cb(void *data) { return data; }

/* The deep arm's match context (6.2). -> NULL on failure (an `error` line). */
static void *deep_context(int jit, void *gctx, void **stack_out, int track) {
    if (!p_match_context_create || !p_set_match_limit || !p_set_depth_limit ||
        !p_set_heap_limit || (jit && (!p_jit_stack_create || !p_jit_stack_assign))) {
        printf("error\tdlsym: a match-context symbol the deep arm needs is missing\n");
        return NULL;
    }
    void *mc = p_match_context_create(gctx);
    if (!mc) { printf("error\tpcre2_match_context_create failed\n"); return NULL; }
    p_set_match_limit(mc, UINT32_MAX);
    p_set_depth_limit(mc, UINT32_MAX);
    p_set_heap_limit(mc, DEEP_HEAP_KIB);
    if (jit) {
        void *st = track ? jit_stack_tracked(gctx)
                         : p_jit_stack_create(DEEP_JIT_STACK_START, DEEP_JIT_STACK_MAX, gctx);
        if (!st) { printf("error\tpcre2_jit_stack_create(32 KiB, 1 GiB) failed\n"); return NULL; }
        p_jit_stack_assign(mc, jit_stack_cb, st);
        if (stack_out) *stack_out = st;
    }
    return mc;
}

/* --limits: the effective limits (6.2), READ BACK where libpcre2 has a
 * getter (pcre2_config_8, pcre2_pattern_info_8); the deep arm's values are
 * the ones deep_context() SET -- there is no match-context getter. */
static void print_limits(void *code, int jit, int deep) {
    uint32_t cm = 0, cd = 0, ch = 0, v = 0;
    if (p_config(PCRE2_CONFIG_MATCHLIMIT, &cm) >= 0) printf("info\tlim_config_match\t%u\n", cm);
    if (p_config(PCRE2_CONFIG_DEPTHLIMIT, &cd) >= 0) printf("info\tlim_config_depth\t%u\n", cd);
    if (p_config(PCRE2_CONFIG_HEAPLIMIT, &ch) >= 0) printf("info\tlim_config_heap_kib\t%u\n", ch);
    if (p_pattern_info) {
        if (p_pattern_info(code, PCRE2_INFO_MATCHLIMIT, &v) == 0) printf("info\tlim_pattern_match\t%u\n", v);
        if (p_pattern_info(code, PCRE2_INFO_DEPTHLIMIT, &v) == 0) printf("info\tlim_pattern_depth\t%u\n", v);
        if (p_pattern_info(code, PCRE2_INFO_HEAPLIMIT, &v) == 0) printf("info\tlim_pattern_heap_kib\t%u\n", v);
    }
    printf("info\tlim_match\t%u\n", deep ? UINT32_MAX : cm);
    printf("info\tlim_depth\t%u\n", deep ? UINT32_MAX : cd);
    printf("info\tlim_heap_kib\t%u\n", deep ? DEEP_HEAP_KIB : ch);
    if (jit) printf("info\tlim_jit_stack_bytes\t%zu\n",
                    deep ? DEEP_JIT_STACK_MAX : DEFAULT_JIT_STACK);
}

static long maxrss_kb(void) {
    struct rusage ru;
    if (getrusage(RUSAGE_SELF, &ru) != 0) return -1;
    return ru.ru_maxrss;
}

/* ---------------------------------------- run_calls: --mode calls ([B148]) */

struct calls_args {
    const char *tokens_dir;
    int anchor_explicit, has_g1, mem_pass, jit;
    long iters, subject_timeout, skip;
    void *mctx;
};

/* noinline for the same reason as load_list: sigsetjmp lives here. */
__attribute__((noinline))
static int run_calls(void *code, const char *list_path, const struct calls_args *a) {
    size_t nsub = 0;
    struct calls_subject *subs = calls_load_list(list_path, &nsub);
    if (!subs) return 2;
    void *md = p_match_data_create_from_pattern(code, NULL);
    if (!md) { printf("error\tmatch_data_create failed\n"); return 2; }
    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);
    for (size_t i = (size_t)a->skip; i < nsub; i++) {
        struct calls_subject *s = &subs[i];
        /* preallocated, NOT pre-touched beyond calloc's own zeroing */
        struct call_res *res = calloc(s->ncalls, sizeof *res);
        if (!res) { printf("error\tcannot allocate %zu call results\n", s->ncalls); return 2; }
        volatile double elapsed = 0.0;
        struct tcalls_in tin = {
            .buf = s->buf, .len = s->len, .calls = s->calls, .ncalls = s->ncalls,
            .iters = a->mem_pass ? 1 : a->iters,
            .opts = a->anchor_explicit ? PCRE2_ANCHORED : 0,
            .code = code, .md = md, .mctx = a->mctx,
            .ov = p_get_ovector_pointer(md), .match = p_match, .res = res,
        };
        struct tcalls_out tout = { 0, 0 };
        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (a->subject_timeout > 0) alarm((unsigned)a->subject_timeout);
            mem_peak = mem_live;
            elapsed = timed_calls(&tin, &tout);
            if (a->subject_timeout > 0) alarm(0);
        }
        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                   s->id, (long)tin.iters, (double)elapsed);
            free(res);
            continue;
        }
        if (a->mem_pass) {
            size_t bytes = a->jit ? jit_resident_bytes() : mem_peak;
            printf("mem\t%s\t%zu\t%s\t%ld\n", s->id, bytes,
                   a->jit ? "mincore" : "counting-alloc", maxrss_kb());
        }
        size_t matched = 0;
        for (size_t k = 0; k < s->ncalls; k++) matched += res[k].kind == CALL_M;
        printf("subject\t%s\tstream\t-\t-\t0\t%zu\t%ld\t%.9f\t%zu\t-\n",
               s->id, s->len, (long)tin.iters, (double)elapsed, matched);
        calls_report(s->id, res, s->ncalls, a->has_g1, a->tokens_dir, NULL);
        free(res);
    }
    p_match_data_free(md);
    return 0;
}

static void emit_caps(size_t *ov, uint32_t npairs, char *out, size_t outcap) {
    size_t off = 0;
    out[0] = 0;
    for (uint32_t i = 1; i < npairs; i++) {
        long s = (ov[2 * i] == PCRE2_UNSET) ? -1 : (long)ov[2 * i];
        long e = (ov[2 * i + 1] == PCRE2_UNSET) ? -1 : (long)ov[2 * i + 1];
        int k = snprintf(out + off, outcap - off, "%s%ld:%ld",
                         i > 1 ? "," : "", s, e);
        if (k < 0 || (size_t)k >= outcap - off) break;
        off += (size_t)k;
    }
    if (!out[0]) { out[0] = '-'; out[1] = 0; }
}

int main(int argc, char **argv) {
    const char *pattern_path = NULL, *list_path = NULL, *mode = "search";
    /* `volatile` on everything the per-subject sigsetjmp/siglongjmp pair can
     * see across the jump: C11 6.8.6.1 leaves a non-volatile automatic
     * indeterminate after a longjmp if it changed since the setjmp, and gcc
     * -Wclobbered says so. The alarm handler jumps out of a timed loop, so
     * every accumulator below is exactly that case. */
    volatile long iters = 1, subject_timeout = 0, skip = 0;
    long compile_trials = 1;
    volatile int find_all = 0;
    volatile int utf8_adv = 0;
    volatile long prime = 0;   /* [B129] --prime: one untimed call per subject before the timed loop */
    /* [B94]: the CONTROL-ONLY escape hatch back to the always-check path
     * (this file's header comment, "VALIDATE-ONCE"). Never set by
     * testees/pcre2/adapter.py; `make check-harness`'s control invokes the
     * driver directly with it, the same technique bench/utf8's own
     * check_utf8_validate_once uses for the oracle's `validate_once=False`
     * arm. */
    volatile int utf_always_check = 0;
    int jit = 0, dfa = 0;
    uint32_t copts = 0;
    struct subst_args sargs;                       /* [B140] --mode subst */
    memset(&sargs, 0, sizeof sargs);
    struct calls_args cargs;                       /* [B148] L4 --mode calls */
    memset(&cargs, 0, sizeof cargs);
    int deep = 0, limits = 0, mem_pass = 0;

    for (int i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!strcmp(a, "--pattern") && i + 1 < argc)        pattern_path = argv[++i];
        else if (!strcmp(a, "--list") && i + 1 < argc)      list_path = argv[++i];
        else if (!strcmp(a, "--mode") && i + 1 < argc)      mode = argv[++i];
        else if (!strcmp(a, "--iters") && i + 1 < argc)     iters = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--compile-trials") && i + 1 < argc) compile_trials = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--subject-timeout") && i + 1 < argc) subject_timeout = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--skip") && i + 1 < argc)      skip = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--find-all"))                  find_all = 1;
        else if (!strcmp(a, "--jit"))                       jit = 1;
        else if (!strcmp(a, "--dfa"))                       dfa = 1;
        /* [B77] U1: --utf8 is the PROTOCOL flag (pcrecbench/adapters.py):
         * the find-all advance steps to the next CHARACTER boundary. --utf /
         * --ucp are this ENGINE's compile options (PCRE2_UTF / PCRE2_UCP),
         * the driver's half of the oracle's per-pattern option word. */
        else if (!strcmp(a, "--utf8"))                      utf8_adv = 1;
        else if (!strcmp(a, "--prime"))                      prime = 1;
        else if (!strcmp(a, "--utf"))                       copts |= PCRE2_UTF;
        else if (!strcmp(a, "--ucp"))                       copts |= PCRE2_UCP;
        else if (!strcmp(a, "--utf-always-check"))          utf_always_check = 1;
        /* [B148] L4 (header comment) */
        else if (!strcmp(a, "--tokens-dir") && i + 1 < argc) cargs.tokens_dir = argv[++i];
        else if (!strcmp(a, "--anchor-explicit"))           cargs.anchor_explicit = 1;
        else if (!strcmp(a, "--deep"))                      deep = 1;
        else if (!strcmp(a, "--limits"))                    limits = 1;
        else if (!strcmp(a, "--mem-pass"))                  mem_pass = 1;
        /* [B140] the --mode subst arguments (header comment) */
        else if (!strcmp(a, "--template") && i + 1 < argc)  sargs.template_path = argv[++i];
        else if (!strcmp(a, "--out-dir") && i + 1 < argc)   sargs.out_dir = argv[++i];
        else if (!strcmp(a, "--subst-flags") && i + 1 < argc) {
            const char *v = argv[++i];
            if (!strcmp(v, "extended")) sargs.extended = 1;
            else if (strcmp(v, "none")) die("--subst-flags takes extended|none");
        }
        else if (!strcmp(a, "--sizing") && i + 1 < argc) {
            const char *v = argv[++i];
            if (!strcmp(v, "first")) sargs.size_first = 1;
            else if (strcmp(v, "bound")) die("--sizing takes bound|first");
        }
        else if (!strcmp(a, "--bound") && i + 1 < argc) {
            char *v = argv[++i], *eq = strchr(v, '=');
            if (!eq || sargs.nbounds >= SUBST_MAX_BOUNDS)
                die("--bound takes ID=BYTES (at most 64)");
            *eq = 0;
            sargs.bound_id[sargs.nbounds] = v;
            sargs.bound_cap[sargs.nbounds++] = (size_t)strtoull(eq + 1, NULL, 10);
        }
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    if (dfa && jit) die("--dfa and --jit together: pcre2_dfa_match has no JIT "
                        "(man pcre2jit: \"It does not apply when the DFA "
                        "matching function is being used\")");
    if (!pattern_path) die("--pattern is required");
    if (!strcmp(mode, "subst")) {
        /* [B140]: a transform has no find-all loop, no prime pass, no DFA
         * form and no find-all advance -- refused by name, never ignored. */
        if (find_all) die("--find-all has no meaning in --mode subst");
        if (prime) die("--prime has no meaning in --mode subst");
        if (dfa) die("--dfa has no meaning in --mode subst (pcre2_substitute "
                     "calls pcre2_match)");
        if (utf8_adv) die("--utf8 has no meaning in --mode subst");
        if (!sargs.template_path) die("--mode subst needs --template");
    }
    if (!strcmp(mode, "calls")) {
        /* [B148] L4: a call stream has no find-all loop, no prime pass, no
         * DFA form and no find-all advance -- refused by name. */
        if (find_all) die("--find-all has no meaning in --mode calls");
        if (prime) die("--prime has no meaning in --mode calls");
        if (dfa) die("--dfa has no meaning in --mode calls");
        if (utf8_adv) die("--utf8 has no meaning in --mode calls");
    } else if (cargs.anchor_explicit) {
        die("--anchor-explicit is a --mode calls flag");
    }
    if (dfa && deep) die("--deep has no meaning with --dfa (6.2 names "
                         "pcre2-interp and pcre2-jit)");
    if (mem_pass && strcmp(mode, "calls") && strcmp(mode, "search"))
        die("--mem-pass takes --mode calls or --mode search");
    if (iters < 1) iters = 1;

    setvbuf(stdout, NULL, _IOLBF, 0);

    void *lib = dlopen("libpcre2-8.so.0", RTLD_NOW);
    if (!lib) { printf("error\tdlopen libpcre2-8.so.0: %s\n", dlerror()); return 2; }
    p_config      = dlsym(lib, "pcre2_config_8");
    p_compile     = dlsym(lib, "pcre2_compile_8");
    p_jit_compile = dlsym(lib, "pcre2_jit_compile_8");
    p_match_data_create_from_pattern = dlsym(lib, "pcre2_match_data_create_from_pattern_8");
    p_match       = dlsym(lib, "pcre2_match_8");
    p_dfa_match   = dlsym(lib, "pcre2_dfa_match_8");
    p_match_data_create = dlsym(lib, "pcre2_match_data_create_8");
    p_get_ovector_pointer = dlsym(lib, "pcre2_get_ovector_pointer_8");
    p_get_ovector_count   = dlsym(lib, "pcre2_get_ovector_count_8");
    p_match_data_free = dlsym(lib, "pcre2_match_data_free_8");
    p_code_free       = dlsym(lib, "pcre2_code_free_8");
    p_get_error_message = dlsym(lib, "pcre2_get_error_message_8");
    p_pattern_info = dlsym(lib, "pcre2_pattern_info_8");
    p_substitute = dlsym(lib, "pcre2_substitute_8");          /* [B140] */
    p_general_context_create = dlsym(lib, "pcre2_general_context_create_8");
    p_match_context_create = dlsym(lib, "pcre2_match_context_create_8");
    p_set_match_limit = dlsym(lib, "pcre2_set_match_limit_8");
    p_set_depth_limit = dlsym(lib, "pcre2_set_depth_limit_8");
    p_set_heap_limit = dlsym(lib, "pcre2_set_heap_limit_8");
    p_jit_stack_create = dlsym(lib, "pcre2_jit_stack_create_8");
    p_jit_stack_assign = dlsym(lib, "pcre2_jit_stack_assign_8");
    if (!p_compile || !p_match || !p_get_ovector_pointer ||
        !p_match_data_create_from_pattern || !p_match_data_free ||
        !p_code_free || !p_get_error_message || !p_config ||
        !p_get_ovector_count || (jit && !p_jit_compile) ||
        (dfa && (!p_dfa_match || !p_match_data_create))) {
        printf("error\tdlsym: a required libpcre2 symbol is missing\n");
        return 2;
    }

    char ver[128] = "unknown";
    int vn = p_config(PCRE2_CONFIG_VERSION, ver);
    if (vn <= 0) strcpy(ver, "unknown");
    printf("info\tversion\t%s\n", ver);
    printf("info\tjit\t%s\n", jit ? "on" : "off");
    printf("info\tdfa\t%s\n", dfa ? "on" : "off");
    /* the utf/ucp/advance facts are printed ONLY when set, so a byte-mode
     * run's `info` stream is exactly what it was before [B77] (an info
     * NAME the adapter does not declare is a validator error). */
    if (copts & PCRE2_UTF) printf("info\tutf\ton\n");
    if (copts & PCRE2_UCP) printf("info\tucp\ton\n");

    size_t patlen = 0;
    unsigned char *pat = slurp(pattern_path, &patlen);
    if (!pat) { printf("error\tcannot read pattern %s\n", pattern_path); return 2; }

    /* ---- compile, `compile_trials` times, every phase timed ---- */
    void *code = NULL;
    for (long t = 1; t <= compile_trials; t++) {
        int errcode = 0;
        size_t erroff = 0;
        double t0 = now();
        void *c = p_compile(pat, patlen, copts, &errcode, &erroff, NULL);
        double t1 = now();
        if (!c) {
            unsigned char msg[256];
            p_get_error_message(errcode, msg, sizeof msg);
            printf("error\tpcre2_compile failed at offset %zu: %s\n",
                   erroff, (char *)msg);
            return 3;
        }
        printf("compile\t%ld\tcompile\t%.9f\n", t, t1 - t0);
        if (jit) {
            double j0 = now();
            int rc = p_jit_compile(c, PCRE2_JIT_COMPLETE);
            double j1 = now();
            if (rc != 0) {
                unsigned char msg[256];
                p_get_error_message(rc, msg, sizeof msg);
                printf("error\tpcre2_jit_compile failed: %s\n", (char *)msg);
                p_code_free(c);
                return 3;
            }
            printf("compile\t%ld\tjit-compile\t%.9f\n", t, j1 - j0);
        }
        if (code) p_code_free(code);
        code = c;
    }

    /* engine_metadata, `pattern`-scoped (record_schema.md 7 rule 2): the
     * STRUCTURED facts pcre2 exposes about what it built. Requirements 4.2
     * names exactly this shape ("RE2's program size, Vectorscan's bytecode
     * size"). Declared in testees/pcre2/adapter.py; an undeclared pair is a
     * validator error, so these two lists move together. */
    if (p_pattern_info && code) {
        uint32_t ncap = 0;
        size_t   csize = 0, jsize = 0;
        if (p_pattern_info(code, PCRE2_INFO_CAPTURECOUNT, &ncap) == 0)
            printf("info\tcapturecount\t%u\n", ncap);
        if (p_pattern_info(code, PCRE2_INFO_SIZE, &csize) == 0)
            printf("info\tcompiled_size_bytes\t%zu\n", csize);
        if (jit && p_pattern_info(code, PCRE2_INFO_JITSIZE, &jsize) == 0)
            printf("info\tjit_size_bytes\t%zu\n", jsize);
        cargs.has_g1 = ncap >= 1;
    }
    if (limits && code) print_limits(code, jit, deep);   /* [B148] L4 */
    if (!list_path) { fflush(stdout); return 0; }   /* compile-only run */

    /* [B148] L4: the deep arm's context and the mem pass's general context,
     * built ONCE, before any timed call. */
    void *mctx = NULL;
    if (deep || mem_pass) {
        void *gctx = NULL;
        if (mem_pass && !jit) {
            if (!p_general_context_create) die("dlsym pcre2_general_context_create_8");
            gctx = p_general_context_create(count_malloc, count_free, NULL);
        }
        if (deep) {
            mctx = deep_context(jit, gctx, NULL, mem_pass);
            if (!mctx) return 2;
        } else if (gctx) {
            mctx = p_match_context_create(gctx);   /* default limits, counted */
        } else if (jit) {
            /* the default arm's JIT stack is 32 KiB of MACHINE stack, which
             * has no mapping of its own to measure: assign a tracked 32 KiB
             * stack with no room to grow -- the same capacity, measurable. */
            mctx = p_match_context_create(NULL);
            void *st = NULL;
            static unsigned long b2[MAXMAPS][2], a2[MAXMAPS][2];
            int nb = read_maps(b2, MAXMAPS);
            st = p_jit_stack_create(DEFAULT_JIT_STACK, DEFAULT_JIT_STACK, NULL);
            int na = read_maps(a2, MAXMAPS);
            njit_maps = 0;
            for (int x = 0; x < na && njit_maps < 16; x++) {
                int seen = 0;
                for (int y = 0; y < nb; y++)
                    if (b2[y][0] == a2[x][0] && b2[y][1] == a2[x][1]) { seen = 1; break; }
                if (!seen) { jit_maps[njit_maps][0] = a2[x][0]; jit_maps[njit_maps][1] = a2[x][1]; njit_maps++; }
            }
            if (st) p_jit_stack_assign(mctx, jit_stack_cb, st);
        }
    }

    if (!strcmp(mode, "calls")) {                    /* [B148] L4 */
        cargs.iters = iters;
        cargs.subject_timeout = subject_timeout;
        cargs.skip = skip;
        cargs.mem_pass = mem_pass;
        cargs.jit = jit;
        cargs.mctx = mctx;
        int rc = run_calls(code, list_path, &cargs);
        p_code_free(code);
        fflush(stdout);
        return rc;
    }

    if (!strcmp(mode, "subst")) {                    /* [B140] */
        int rc = run_subst(code, list_path, &sargs);
        p_code_free(code);
        return rc;
    }

    size_t nsub = 0;
    subject *subs = load_list(list_path, &nsub);
    if (!subs) { printf("error\tcannot read subject list %s\n", list_path); return 2; }

    const int anchored = !strcmp(mode, "match");
    const uint32_t opts = anchored ? (PCRE2_ANCHORED | PCRE2_ENDANCHORED) : 0;

    /* man pcre2_dfa_match: a match_data block sized from the PATTERN's own
     * capture count "is therefore not advisable" for DFA -- a small fixed
     * oveccount instead (this driver only ever reads the first pair). */
    void *md = dfa ? p_match_data_create(16, NULL)
                   : p_match_data_create_from_pattern(code, NULL);
    if (!md) { printf("error\tmatch_data_create failed\n"); return 2; }
    size_t *ov = p_get_ovector_pointer(md);
    uint32_t ovn = p_get_ovector_count(md);

    int *dfa_ws = NULL;
    size_t dfa_ws_n = 0;
    if (dfa) {
        dfa_ws_n = PCRE2_DFA_WS_ELEMS;
        dfa_ws = malloc(dfa_ws_n * sizeof *dfa_ws);
        if (!dfa_ws) { printf("error\tmalloc dfa workspace failed\n"); return 2; }
    }

    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);

    char caps[4096];
    size_t firstov[512];

    for (size_t i = (size_t)skip; i < nsub; i++) {
        subject *s = &subs[i];
        volatile long   first_s = -1, first_e = -1, nmatch = -1;
        volatile int    rc_final = PCRE2_ERROR_NOMATCH;
        volatile double elapsed = 0.0;
        volatile uint32_t npairs = 0;

        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            /* [B133] the timed loop is timed_run() in timed.c (its own
             * translation unit; see that file's header). */
            struct timed_in tin = {
                .buf = s->buf, .len = s->len, .iters = iters,
                .prime = (int)prime, .find_all = find_all,
                .utf8_adv = utf8_adv, .utf_always_check = utf_always_check,
                .dfa = dfa, .opts = opts, .copts = copts, .ovn = ovn,
                .code = code, .md = md, .ov = ov, .firstov = firstov,
                .dfa_ws = dfa_ws, .dfa_ws_n = dfa_ws_n,
                /* [B148] L4: the deep arm (and the mem pass) runs through
                 * timed_ctx.c's forwarder, which supplies the context timed.c
                 * passes as NULL; otherwise pcre2_match_8 itself, as always. */
                .match = mctx ? timed_ctx_forward : p_match,
                .dfa_match = p_dfa_match, .die = die,
            };
            if (mctx) { timed_ctx_mctx = mctx; timed_ctx_match = p_match; }
            if (mem_pass) { mem_peak = mem_live; tin.iters = 1; }
            struct timed_out tout = { -1, -1, -1, PCRE2_ERROR_NOMATCH, 0 };
            elapsed = timed_run(&tin, &tout);
            first_s = tout.first_s; first_e = tout.first_e;
            nmatch = tout.nmatch; rc_final = tout.rc_final;
            npairs = tout.npairs;
            if (subject_timeout > 0) alarm(0);
        }

        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                   s->id, (long)iters, (double)elapsed);
            continue;
        }
        if (mem_pass) {                              /* [B148] L4, 6.4 */
            printf("mem\t%s\t%zu\t%s\t%ld\n", s->id,
                   jit ? jit_resident_bytes() : mem_peak,
                   jit ? "mincore" : "counting-alloc", maxrss_kb());
        }

        char answerbuf[256];
        const char *answer;
        char sbuf[32], ebuf[32], nbuf[32];

        if (first_s >= 0) {
            answer = "match";
            /* DFA structurally reports no per-group captures (npairs is
             * forced 0 above) -- "-" here is the same spelling emit_caps
             * itself falls back to on npairs==0, made explicit rather than
             * relying on that fallback silently doing the right thing. */
            if (dfa) { caps[0] = '-'; caps[1] = 0; }
            else emit_caps(firstov, (uint32_t)npairs, caps, sizeof caps);
            snprintf(sbuf, sizeof sbuf, "%ld", (long)first_s);
            snprintf(ebuf, sizeof ebuf, "%ld", (long)first_e);
        } else {
            strcpy(sbuf, "-");
            strcpy(ebuf, "-");
            caps[0] = '-'; caps[1] = 0;
            if (rc_final == PCRE2_ERROR_NOMATCH) {
                answer = "nomatch";
            } else {
                /* `giveup:<code>:<pcre2's own message>`. The message comes
                 * from pcre2_get_error_message rather than a table in this
                 * file, so it cannot fall out of step with the library; the
                 * harness classifies on the CODE. */
                unsigned char emsg[160];
                int en = p_get_error_message(rc_final, emsg, sizeof emsg);
                if (en > 0) {
                    for (int k = 0; emsg[k]; k++)
                        if (emsg[k] == '\t' || emsg[k] == '\n') emsg[k] = ' ';
                    snprintf(answerbuf, sizeof answerbuf, "giveup:%d:%s",
                             (int)rc_final, (char *)emsg);
                } else {
                    snprintf(answerbuf, sizeof answerbuf, "giveup:%d",
                             (int)rc_final);
                }
                answer = answerbuf;
            }
        }
        if (find_all && nmatch >= 0) snprintf(nbuf, sizeof nbuf, "%ld", (long)nmatch);
        else strcpy(nbuf, "-");

        /* consumed_length: the length argument pcre2 was given and accepted.
         * See this file's header and testees/pcre2/CLAUDE.md. */
        printf("subject\t%s\t%s\t%s\t%s\t%u\t%zu\t%ld\t%.9f\t%s\t%s\n",
               s->id, answer, sbuf, ebuf, npairs ? (uint32_t)npairs - 1u : 0u,
               s->len, (long)iters, (double)elapsed, nbuf, caps);
    }

    p_match_data_free(md);
    p_code_free(code);
    free(dfa_ws);
    fflush(stdout);
    return 0;
}
