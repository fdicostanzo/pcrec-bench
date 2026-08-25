/* testees/pcrec/driver.c -- the pcrec batched in-process timing driver.
 *
 * Implements the DRIVER PROTOCOL in pcrecbench/adapters.py; read that first.
 * It differs from testees/pcre2/driver.c in exactly one place -- it is handed
 * a BUILT ARTIFACT (`--lib artifact-N.so`) rather than a pattern, because an
 * AOT engine's "compile" already happened in two earlier phases that python
 * timed. The third phase, `load`, is the dlopen, and it is timed HERE.
 *
 * NO pcrec ABI IS DECLARED IN THIS FILE. Everything crosses through the flat
 * `pb_*` surface `shim.c` exports, and the shim gets it from the artifact's
 * own generated header. See shim.c's comment for why that matters.
 *
 * consumed_length: the subject length the artifact's entry was given and
 * accepted. `<prefix>_search` takes a `size_t n` and exposes no scan
 * high-water mark, so the claim is "no byte was withheld", never "the engine
 * looked at every byte" -- the same convention as the pcre2 driver, stated in
 * testees/pcrec/CLAUDE.md.
 */

#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <setjmp.h>
#include <signal.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

static int       (*pb_abi)(void);
static int       (*pb_ncaps)(void);
static int       (*pb_ngroups)(void);
static int       (*pb_nnames)(void);
static int       (*pb_engine)(void);
static long long (*pb_step_budget)(void);
static long long (*pb_work_budget)(void);
static long long (*pb_frame_capacity)(void);
static long long (*pb_subject_ceiling)(void);
static const char *(*pb_engine_why)(void);
static int       (*pb_has_vm_stamps)(void);
static const char *(*pb_vm_prefilter)(void);
static unsigned  (*pb_vm_rungs)(void);
static unsigned  (*pb_vm_strats)(void);
static unsigned  (*pb_vm_prunes)(void);
static const char *(*pb_engine_stamp)(void);
static int       (*pb_search)(const unsigned char *, size_t, size_t,
                              ptrdiff_t (*)[2]);
static long long (*pb_match_caps)(const unsigned char *, size_t, size_t,
                                  ptrdiff_t (*)[2]);

static double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
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

static sigjmp_buf timeout_jmp;
static volatile sig_atomic_t timed_out;

static void on_alarm(int sig) {
    (void)sig;
    timed_out = 1;
    siglongjmp(timeout_jmp, 1);
}

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

#define SYM(name) do {                                            \
        *(void **)(&name) = dlsym(lib, #name);                    \
        if (!name) { printf("error\tdlsym %s: %s\n", #name,       \
                            dlerror()); return 2; }               \
    } while (0)

static void emit_caps(const ptrdiff_t (*caps)[2], int ncaps,
                      char *out, size_t outcap) {
    size_t off = 0;
    out[0] = 0;
    for (int i = 1; i < ncaps; i++) {
        int k = snprintf(out + off, outcap - off, "%s%td:%td",
                         i > 1 ? "," : "", caps[i][0], caps[i][1]);
        if (k < 0 || (size_t)k >= outcap - off) break;
        off += (size_t)k;
    }
    if (!out[0]) { out[0] = '-'; out[1] = 0; }
}

int main(int argc, char **argv) {
    const char *lib_path = NULL, *list_path = NULL, *mode = "search";
    volatile long iters = 1, subject_timeout = 0, skip = 0;
    long trial = 1;
    volatile int find_all = 0;

    for (int i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!strcmp(a, "--lib") && i + 1 < argc)                 lib_path = argv[++i];
        else if (!strcmp(a, "--list") && i + 1 < argc)           list_path = argv[++i];
        else if (!strcmp(a, "--mode") && i + 1 < argc)           mode = argv[++i];
        else if (!strcmp(a, "--iters") && i + 1 < argc)          iters = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--trial") && i + 1 < argc)          trial = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--subject-timeout") && i + 1 < argc) subject_timeout = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--skip") && i + 1 < argc)           skip = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--find-all"))                       find_all = 1;
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    if (!lib_path) { printf("error\t--lib is required\n"); return 2; }
    if (iters < 1) iters = 1;

    setvbuf(stdout, NULL, _IOLBF, 0);

    /* PHASE 3 of the AOT compile cost: the dlopen. Phases 1 and 2 (the pcrec
     * CLI and gcc) are separate processes and are timed by python. */
    double l0 = now();
    void *lib = dlopen(lib_path, RTLD_NOW | RTLD_LOCAL);
    double l1 = now();
    if (!lib) { printf("error\tdlopen %s: %s\n", lib_path, dlerror()); return 3; }
    printf("compile\t%ld\tload\t%.9f\n", trial, l1 - l0);

    dlerror();
    SYM(pb_abi); SYM(pb_ncaps); SYM(pb_ngroups); SYM(pb_nnames);
    SYM(pb_engine); SYM(pb_step_budget); SYM(pb_work_budget);
    SYM(pb_frame_capacity); SYM(pb_subject_ceiling); SYM(pb_engine_why);
    SYM(pb_has_vm_stamps); SYM(pb_vm_prefilter); SYM(pb_vm_rungs);
    SYM(pb_vm_strats); SYM(pb_vm_prunes); SYM(pb_engine_stamp);
    SYM(pb_search); SYM(pb_match_caps);

    /* engine_metadata, `pattern`-scoped: read from the artifact's STRUCTURED
     * fields, never from the prose RX_ENGINE_WHY (requirements 4.2). The
     * prose goes out as `engine_why` and the adapter puts it in the row's
     * unindexed `diagnostic`, which is where record_schema.md 7 puts it. */
    printf("info\tabi\t%d\n", pb_abi());
    printf("info\tncaps\t%d\n", pb_ncaps());
    printf("info\tngroups\t%d\n", pb_ngroups());
    printf("info\tnnames\t%d\n", pb_nnames());
    printf("info\tengine\t%s\n", pb_engine() == 1 ? "dfa"
                               : pb_engine() == 2 ? "vm" : "unknown");
    printf("info\tstep_budget\t%lld\n", pb_step_budget());
    printf("info\twork_budget\t%lld\n", pb_work_budget());
    printf("info\tframe_capacity\t%lld\n", pb_frame_capacity());
    printf("info\tsubject_ceiling\t%lld\n", pb_subject_ceiling());
    if (pb_engine_why() && *pb_engine_why())
        printf("info\tengine_why\t%s\n", pb_engine_why());
    if (pb_has_vm_stamps()) {
        const char *pf = pb_vm_prefilter();
        if (pf) printf("info\tprefilter\t%s\n", pf);
        printf("info\tvm_rungs\t0x%x\n", pb_vm_rungs());
        printf("info\tvm_strats\t0x%x\n", pb_vm_strats());
        printf("info\tvm_prunes\t0x%x\n", pb_vm_prunes());
    }
    const char *es = pb_engine_stamp();
    if (es) printf("info\tengine_stamp\t%s\n", es);

    if (!list_path) { fflush(stdout); return 0; }   /* load-only run */

    size_t nsub = 0;
    subject *subs = load_list(list_path, &nsub);
    if (!subs) { printf("error\tcannot read subject list %s\n", list_path); return 2; }

    const int anchored = !strcmp(mode, "match");
    const int ncaps = pb_ncaps() > 0 ? pb_ncaps() : 1;
    ptrdiff_t (*caps)[2] = malloc((size_t)ncaps * sizeof *caps);
    ptrdiff_t (*firstcaps)[2] = malloc((size_t)ncaps * sizeof *firstcaps);
    if (!caps || !firstcaps) { printf("error\tout of memory\n"); return 2; }

    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);

    char capsbuf[4096];

    for (size_t i = (size_t)skip; i < nsub; i++) {
        subject *s = &subs[i];
        volatile long   first_s = -1, first_e = -1, nmatch = -1;
        volatile int    giveup = 0;
        volatile double elapsed = 0.0;

        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            double t0 = now();
            for (long it = 0; it < iters; it++) {
                first_s = first_e = -1;
                giveup = 0;
                if (anchored) {
                    /* whole-subject: anchored at 0 AND ending at n. See
                     * shim.c's pb_match_caps comment for the asymmetry this
                     * carries against PCRE2_ENDANCHORED. */
                    long long r = pb_match_caps(s->buf, s->len, 0, caps);
                    if (r < 0) {
                        if (r < -1) giveup = (int)r;
                    } else if ((size_t)r == s->len) {
                        first_s = 0;
                        first_e = (long)r;
                        memcpy(firstcaps, caps, (size_t)ncaps * sizeof *caps);
                    }
                } else if (find_all) {
                    size_t pos = 0;
                    long count = 0;
                    for (;;) {
                        int r = pb_search(s->buf, s->len, pos, caps);
                        if (r == 0) break;
                        if (r < 0) { if (count == 0) giveup = r; break; }
                        if (first_s < 0) {
                            first_s = (long)caps[0][0];
                            first_e = (long)caps[0][1];
                            memcpy(firstcaps, caps, (size_t)ncaps * sizeof *caps);
                        }
                        count++;
                        size_t end = (size_t)caps[0][1];
                        pos = (end > pos) ? end : pos + 1;
                        if (pos > s->len) break;
                    }
                    nmatch = count;
                } else {
                    int r = pb_search(s->buf, s->len, 0, caps);
                    if (r == 1) {
                        first_s = (long)caps[0][0];
                        first_e = (long)caps[0][1];
                        memcpy(firstcaps, caps, (size_t)ncaps * sizeof *caps);
                    } else if (r < 0) {
                        giveup = r;
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

        char answerbuf[64], sbuf[32], ebuf[32], nbuf[32];
        const char *answer;
        if (first_s >= 0) {
            answer = "match";
            snprintf(sbuf, sizeof sbuf, "%ld", (long)first_s);
            snprintf(ebuf, sizeof ebuf, "%ld", (long)first_e);
            emit_caps((const ptrdiff_t (*)[2])firstcaps, ncaps,
                      capsbuf, sizeof capsbuf);
        } else {
            strcpy(sbuf, "-"); strcpy(ebuf, "-");
            capsbuf[0] = '-'; capsbuf[1] = 0;
            if (giveup) {
                snprintf(answerbuf, sizeof answerbuf, "giveup:%d", (int)giveup);
                answer = answerbuf;
            } else {
                answer = "nomatch";
            }
        }
        if (find_all && nmatch >= 0) snprintf(nbuf, sizeof nbuf, "%ld", (long)nmatch);
        else strcpy(nbuf, "-");

        printf("subject\t%s\t%s\t%s\t%s\t%d\t%zu\t%ld\t%.9f\t%s\t%s\n",
               s->id, answer, sbuf, ebuf, ncaps > 0 ? ncaps - 1 : 0,
               s->len, (long)iters, (double)elapsed, nbuf, capsbuf);
    }

    fflush(stdout);
    return 0;
}
