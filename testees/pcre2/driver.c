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
 * consumed_length: the LENGTH ARGUMENT the driver passed and pcre2 accepted,
 * i.e. the whole subject. pcre2_match takes a size_t length and has no
 * subject-size ceiling to truncate against, and the API exposes no scan
 * high-water mark -- so the honest claim is "the engine was given and
 * accepted N bytes", never "the engine looked at N bytes". testees/pcre2/
 * CLAUDE.md states this where a reader of the numbers will find it.
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
    int jit = 0;

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
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
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
    p_get_ovector_pointer = dlsym(lib, "pcre2_get_ovector_pointer_8");
    p_get_ovector_count   = dlsym(lib, "pcre2_get_ovector_count_8");
    p_match_data_free = dlsym(lib, "pcre2_match_data_free_8");
    p_code_free       = dlsym(lib, "pcre2_code_free_8");
    p_get_error_message = dlsym(lib, "pcre2_get_error_message_8");
    p_pattern_info = dlsym(lib, "pcre2_pattern_info_8");
    if (!p_compile || !p_match || !p_get_ovector_pointer ||
        !p_match_data_create_from_pattern || !p_match_data_free ||
        !p_code_free || !p_get_error_message || !p_config ||
        !p_get_ovector_count || (jit && !p_jit_compile)) {
        printf("error\tdlsym: a required libpcre2 symbol is missing\n");
        return 2;
    }

    char ver[128] = "unknown";
    int vn = p_config(PCRE2_CONFIG_VERSION, ver);
    if (vn <= 0) strcpy(ver, "unknown");
    printf("info\tversion\t%s\n", ver);
    printf("info\tjit\t%s\n", jit ? "on" : "off");

    size_t patlen = 0;
    unsigned char *pat = slurp(pattern_path, &patlen);
    if (!pat) { printf("error\tcannot read pattern %s\n", pattern_path); return 2; }

    /* ---- compile, `compile_trials` times, every phase timed ---- */
    void *code = NULL;
    for (long t = 1; t <= compile_trials; t++) {
        int errcode = 0;
        size_t erroff = 0;
        double t0 = now();
        void *c = p_compile(pat, patlen, 0, &errcode, &erroff, NULL);
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

    void *md = p_match_data_create_from_pattern(code, NULL);
    if (!md) { printf("error\tmatch_data_create failed\n"); return 2; }
    size_t *ov = p_get_ovector_pointer(md);
    uint32_t ovn = p_get_ovector_count(md);

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
                    for (;;) {
                        int rc = p_match(code, s->buf, s->len, pos, opts, md, NULL);
                        if (rc < 0) { if (count == 0) rc_final = rc; break; }
                        if (first_s < 0) {
                            first_s = (long)ov[0];
                            first_e = (long)ov[1];
                            npairs = (uint32_t)(rc > 0 ? rc : 1);
                            if (npairs > ovn) npairs = ovn;
                            if (npairs > 256) npairs = 256;
                            memcpy(firstov, ov, (size_t)npairs * 2 * sizeof *ov);
                            rc_final = rc;
                        }
                        count++;
                        size_t end = ov[1];
                        pos = (end > pos) ? end : pos + 1;
                        if (pos > s->len) break;
                    }
                    nmatch = count;
                } else {
                    int rc = p_match(code, s->buf, s->len, 0, opts, md, NULL);
                    rc_final = rc;
                    if (rc >= 0) {
                        first_s = (long)ov[0];
                        first_e = (long)ov[1];
                        npairs = (uint32_t)(rc > 0 ? rc : 1);
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

        char answerbuf[64];
        const char *answer;
        char sbuf[32], ebuf[32], nbuf[32];

        if (first_s >= 0) {
            answer = "match";
            emit_caps(firstov, (uint32_t)npairs, caps, sizeof caps);
            snprintf(sbuf, sizeof sbuf, "%ld", (long)first_s);
            snprintf(ebuf, sizeof ebuf, "%ld", (long)first_e);
        } else {
            strcpy(sbuf, "-");
            strcpy(ebuf, "-");
            caps[0] = '-'; caps[1] = 0;
            if (rc_final == PCRE2_ERROR_NOMATCH) {
                answer = "nomatch";
            } else {
                snprintf(answerbuf, sizeof answerbuf, "giveup:%d", (int)rc_final);
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
    fflush(stdout);
    return 0;
}
