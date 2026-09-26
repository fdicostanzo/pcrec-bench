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

#define PCRE2_ERROR_NOMATCH   (-1)
#define PCRE2_UNSET           ((size_t)-1)
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

/* ------------------------------------------------------------------- main */

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

/* ONE call site for both matchers ([B42] L6a): the rc>=0-is-a-match /
 * ov[0..1]-is-the-span reading downstream is IDENTICAL either way (this
 * file's header comment says why), so only the CALL itself branches. */
static int do_match(int dfa, void *code, const unsigned char *buf, size_t len,
                    size_t pos, uint32_t opts, void *md,
                    int *ws, size_t wsn) {
    if (dfa) return p_dfa_match(code, buf, len, pos, opts, md, NULL, ws, wsn);
    return p_match(code, buf, len, pos, opts, md, NULL);
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
    /* [B94]: the CONTROL-ONLY escape hatch back to the always-check path
     * (this file's header comment, "VALIDATE-ONCE"). Never set by
     * testees/pcre2/adapter.py; `make check-harness`'s control invokes the
     * driver directly with it, the same technique bench/utf8's own
     * check_utf8_validate_once uses for the oracle's `validate_once=False`
     * arm. */
    volatile int utf_always_check = 0;
    int jit = 0, dfa = 0;
    uint32_t copts = 0;

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
        else if (!strcmp(a, "--utf"))                       copts |= PCRE2_UTF;
        else if (!strcmp(a, "--ucp"))                       copts |= PCRE2_UCP;
        else if (!strcmp(a, "--utf-always-check"))          utf_always_check = 1;
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    if (dfa && jit) die("--dfa and --jit together: pcre2_dfa_match has no JIT "
                        "(man pcre2jit: \"It does not apply when the DFA "
                        "matching function is being used\")");
    if (!pattern_path) die("--pattern is required");
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
    }
    if (!list_path) { fflush(stdout); return 0; }   /* compile-only run */

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
            double t0 = now();
            for (long it = 0; it < iters; it++) {
                first_s = first_e = -1;
                npairs = 0;
                if (find_all) {
                    size_t pos = 0;
                    long   count = 0;
                    /* [B94]/BD15: VALIDATE-ONCE. `utf_once` is true only
                     * under PCRE2_UTF and only when the control has not
                     * disabled it; `validated` tracks whether call 1 (offset
                     * 0, always without the flag) has completed. See this
                     * file's header comment for the full rule and its man
                     * pcre2api citations. */
                    int utf_once = (copts & PCRE2_UTF) && !utf_always_check;
                    int validated = 0;
                    for (;;) {
                        uint32_t call_opts = opts;
                        if (utf_once && validated) {
                            /* NEVER trusted silently: assert pos is a
                             * character boundary before passing the flag --
                             * the same discipline oracle_pcre2.py's
                             * `_find_all_impl` uses (an AssertionError there,
                             * a loud die() here). A continuation byte here
                             * would mean --utf8's advance rule broke, not
                             * that this control should look away. */
                            if (pos < s->len && (s->buf[pos] & 0xC0u) == 0x80u)
                                die("validate-once: find-all start offset is "
                                    "not a character boundary -- refusing to "
                                    "pass PCRE2_NO_UTF_CHECK");
                            call_opts |= PCRE2_NO_UTF_CHECK;
                        }
                        int rc = do_match(dfa, code, s->buf, s->len, pos,
                                          call_opts, md, dfa_ws, dfa_ws_n);
                        /* Call 1 (pos == 0) just RAN: whether it matched,
                         * found no match, or gave up on something other than
                         * UTF validity, libpcre2 has by now checked the
                         * whole subject from offset 0 to its end (this
                         * file's header comment). A call that genuinely
                         * failed UTF validation is reported below through
                         * the ordinary `giveup:<code>:<message>` protocol
                         * and the loop breaks (rc < 0) before any call 2
                         * happens, so marking `validated` here is never
                         * reached by an unvalidated subject in practice. */
                        if (utf_once && pos == 0 && !validated) validated = 1;
                        if (rc < 0) { if (count == 0) rc_final = rc; break; }
                        if (first_s < 0) {
                            first_s = (long)ov[0];
                            first_e = (long)ov[1];
                            /* DFA: `rc` is the SIMULTANEOUS-match count at
                             * this start point, not a capture-pair count
                             * (man pcre2_dfa_match item 2: "no captured
                             * substrings are available") -- forced to 0,
                             * never read as if it were one. */
                            npairs = dfa ? 0 : (uint32_t)(rc > 0 ? rc : 1);
                            if (npairs > ovn) npairs = ovn;
                            if (npairs > 256) npairs = 256;
                            memcpy(firstov, ov, (size_t)npairs * 2 * sizeof *ov);
                            rc_final = rc;
                        }
                        count++;
                        /* pcrec match_api.md S3.1's find-all advance: off the
                         * match's own reported START (ov[0]), never off the
                         * scan position -- an empty match can be found AHEAD
                         * of pos, and advancing pos itself re-finds the same
                         * empty match next call (KB-17). Byte encoding: the
                         * S3.1.1 `next_pos` residual is start+1; under
                         * --utf8 ([B77] U1) it is the next CHARACTER
                         * boundary -- a mid-character start offset under
                         * PCRE2_UTF is PCRE2_ERROR_BADUTFOFFSET. */
                        size_t start = ov[0];
                        size_t end = ov[1];
                        pos = (end > start) ? end
                            : utf8_adv ? utf8_next_start(s->buf, s->len, start)
                                       : start + 1;
                        if (pos > s->len) break;
                    }
                    nmatch = count;
                } else {
                    int rc = do_match(dfa, code, s->buf, s->len, 0, opts,
                                      md, dfa_ws, dfa_ws_n);
                    rc_final = rc;
                    if (rc >= 0) {
                        first_s = (long)ov[0];
                        first_e = (long)ov[1];
                        npairs = dfa ? 0 : (uint32_t)(rc > 0 ? rc : 1);
                        if (npairs > ovn) npairs = ovn;
                        if (npairs > 256) npairs = 256;
                        memcpy(firstov, ov, (size_t)npairs * 2 * sizeof *ov);
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
