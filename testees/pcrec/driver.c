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
 *
 * THE CALLER-PROVIDED FRAME BUFFER (`--buffer-frames N --buffer-trail M`,
 * pcrec match_api.md 10). N and M are CAPACITIES -- frames and trail
 * entries, never bytes. When both are given the driver allocates the two
 * regions ONCE per run, aligned to pb_buffer_align() and sized
 * N * pb_resume_frame_size() and M * pb_trail_frame_size() bytes, touches
 * every page once OUTSIDE any timed loop (so no timed loop pays a first-touch
 * page fault), and then uses the `_in` entries in ALL THREE modes with the
 * same protocol lines and the same give-up propagation. Without the options
 * the driver's behaviour and output are byte-identical to before they
 * existed. Two facts a reader of the info lines needs:
 *
 *   - `info resume_frames/trail_frames/resume_frame_size/trail_frame_size`
 *     are printed whenever the artifact STAMPS them (every artifact at abi
 *     3, both engines); `info buffer_frames/buffer_trail` ONLY when the
 *     buffers were actually used, so an ABSENT pair in a record means the
 *     stamped default storage was what ran.
 *   - a stamped frame size of 0 means the engine takes no buffers (every
 *     DFA artifact, 10.4). The options are then accepted but INERT: nothing
 *     is allocated, no `buffer_*` pair is printed, the plain entries run,
 *     and `info buffer_inert stamped-size-0` says so. Dividing by the 0 is
 *     the documented mistake and is never done.
 *
 * THE ABI FLOOR IS CHECKED HERE, FIRST. `pb_abi()` against
 * `pb_shim_min_abi()` (shim.c) before any other info line and before any
 * subject is read: an artifact below the floor is REFUSED by name --
 * `error abi-below-shim-floor: ...` carrying both numbers -- and the driver
 * exits 3. The adapter turns that one line into a clean AdapterError. It is
 * a REFUSAL and not a degraded run on purpose: a shim that read a field the
 * artifact does not have would be reading whatever follows it.
 *
 * WHAT IS PRINTED FOR THE MECHANISM STAMPS, and the rule none of it breaks
 * (pcrec I-5): NOTHING IS EVER INFERRED FROM A STAMP'S ABSENCE. Each of
 * `info dfa_scan / dfa_prefilter / dfa_table / dfa_prefilter_offsets /
 * dfa_scan_edge / dfa_start / dfa_match / dfa_uniform_folds / vm_frameless /
 * vm_alt_islands / vm_entry_shape / vm_program_bytes / altcls_merges /
 * altcls_factored / fast_frames /
 * fast_trail / unroll_k /
 * unroll_k_why / max_emit_code_bytes / max_emit_bytes / engine_sel /
 * vm_prefilter_lang / vm_prefilter_lang_why` is printed only when the artifact
 * stamps it, and a consumer of these lines reads a MISSING line as "not
 * stamped" and nothing else -- never as "DFA", never as "not a hybrid". The
 * two facts that ARE readable from an absence are the spec's own iffs and
 * come from FIELDS rather than macros: `info rxinfo_scan_present 0` on a VM
 * artifact is "not a hybrid" (match_api.md 6, consequence 2) and
 * `info rxinfo_match_form_present 0` is "this artifact's _match is not a
 * DFA form" ([ENG-ABS]); both are printed on EVERY artifact so that reading
 * is never made from silence either. [B26] adds two more FIELD lines on the
 * same terms -- `info artifact_name` / `info nentries` (rx_info.name /
 * .nentries, appended at abi 15) with `info rxinfo_name_present` beside the
 * first -- which are PROVENANCE rather than selection facts: no macro
 * spells either, so neither is cross-checked against a stamp. [B34] adds
 * a third FIELD line, `info rxinfo_search_form` with its own
 * `_present` (rx_info.search_form, abi 16), which IS a selection fact
 * with a macro spelling (`info dfa_start`) and IS cross-checked -- the
 * `match_form` pattern, and the two are deliberately printed side by side
 * because their NULL rules differ: on a VM hybrid `match_form` is NULL
 * and `search_form` is not. [B34] also adds `info altcls_merges` /
 * `info altcls_factored` (pcrec I-39, [OPT-ALTCLS]) -- COUNTS with NO
 * rx_info mirror at all, so neither is cross-checked against a field;
 * they are printed together, behind one presence check, whenever the
 * artifact stamps them -- in practice every artifact this driver will
 * ever load, since the macros predate this pin by a long margin and only
 * the READ is new here. [B37] (pin 334fd10e, abi 22 -- six abi steps in
 * one re-pin) adds FOUR more MACRO lines on the same terms, none with an
 * rx_info mirror and so none cross-checked against a field: `info
 * dfa_uniform_folds` (abi 17, inside the DFA-scan guard -- RX_DFA_TABLE's
 * own scope), `info vm_alt_islands` (abi 18) and the PAIR `info
 * vm_entry_shape` / `info vm_program_bytes` (abi 22), the last three
 * VM-only beside `vm_frameless`. Each is printed behind its own presence
 * check, so a `0`, an `"inline"` or a byte count is a VALUE the adapter
 * read and an absent line is "not stamped" and nothing more. `struct
 * rx_info` gained no member across those six steps, which is why the
 * floor message below still ends at abi 16.
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
static int       (*pb_err_floor)(void);
static int       (*pb_err_giveup_top)(void);
static int       (*pb_err_internal)(void);
static const char *(*pb_err_name)(int);
static int       (*pb_has_vm_stamps)(void);
static const char *(*pb_vm_prefilter)(void);
static unsigned  (*pb_vm_rungs)(void);
static unsigned  (*pb_vm_strats)(void);
static unsigned  (*pb_vm_prunes)(void);
static const char *(*pb_engine_stamp)(void);
static int       (*pb_shim_min_abi)(void);
static const char *(*pb_info_scan)(void);
static const char *(*pb_info_prefilter)(void);
static int       (*pb_has_dfa_stamps)(void);
static const char *(*pb_dfa_scan)(void);
static const char *(*pb_dfa_prefilter)(void);
static const char *(*pb_dfa_table)(void);
static const char *(*pb_dfa_prefilter_offsets)(void);
static const char *(*pb_dfa_scan_edge)(void);
static const char *(*pb_dfa_match)(void);
static const char *(*pb_info_match_form)(void);
static const char *(*pb_info_name)(void);
static int       (*pb_info_nentries)(void);
static const char *(*pb_dfa_start)(void);
static const char *(*pb_info_search_form)(void);
static int       (*pb_has_vm_frameless)(void);
static int       (*pb_vm_frameless)(void);
static int       (*pb_has_altcls)(void);
static long long (*pb_altcls_merges)(void);
static long long (*pb_altcls_factored)(void);
static int       (*pb_has_dfa_uniform_folds)(void);
static long long (*pb_dfa_uniform_folds)(void);
static int       (*pb_has_vm_alt_islands)(void);
static long long (*pb_vm_alt_islands)(void);
static int       (*pb_has_vm_entry_shape)(void);
static const char *(*pb_vm_entry_shape)(void);
static long long (*pb_vm_program_bytes)(void);
static int       (*pb_has_unroll_k)(void);
static long long (*pb_unroll_k)(void);
static const char *(*pb_unroll_k_why)(void);
static int       (*pb_has_max_emit_code_bytes)(void);
static long long (*pb_max_emit_code_bytes)(void);
static int       (*pb_has_max_emit_bytes)(void);
static long long (*pb_max_emit_bytes)(void);
static int       (*pb_has_engine_sel)(void);
static const char *(*pb_engine_sel)(void);
static int       (*pb_has_vm_prefilter_lang)(void);
static const char *(*pb_vm_prefilter_lang)(void);
static const char *(*pb_vm_prefilter_lang_why)(void);
static int       (*pb_has_fast_tier)(void);
static long long (*pb_fast_frames)(void);
static long long (*pb_fast_trail)(void);
static int       (*pb_search)(const unsigned char *, size_t, size_t,
                              ptrdiff_t (*)[2]);
static long long (*pb_match_caps)(const unsigned char *, size_t, size_t,
                                  ptrdiff_t (*)[2]);
static int       (*pb_has_in_entries)(void);
static long long (*pb_buffer_align)(void);
static long long (*pb_resume_frames)(void);
static long long (*pb_trail_frames)(void);
static long long (*pb_resume_frame_size)(void);
static long long (*pb_trail_frame_size)(void);
static int       (*pb_search_in)(const unsigned char *, size_t, size_t,
                                 ptrdiff_t (*)[2], void *, size_t, void *,
                                 size_t);
static long long (*pb_match_caps_in)(const unsigned char *, size_t, size_t,
                                     ptrdiff_t (*)[2], void *, size_t,
                                     void *, size_t);

/* The caller-provided regions, when in use (see the header comment). */
static void  *buf_frames, *buf_trail;
static size_t buf_nframes, buf_ntrail;
static int    use_buffers;

/* One call site per entry, so the three mode loops below read the same
 * whether the buffers are in use or not. */
static inline int do_search(const unsigned char *s, size_t n, size_t pos,
                            ptrdiff_t (*caps)[2]) {
    return use_buffers
        ? pb_search_in(s, n, pos, caps, buf_frames, buf_nframes,
                       buf_trail, buf_ntrail)
        : pb_search(s, n, pos, caps);
}

static inline long long do_match_caps(const unsigned char *s, size_t n,
                                      size_t pos, ptrdiff_t (*caps)[2]) {
    return use_buffers
        ? pb_match_caps_in(s, n, pos, caps, buf_frames, buf_nframes,
                           buf_trail, buf_ntrail)
        : pb_match_caps(s, n, pos, caps);
}

static void *alloc_region(size_t align, size_t bytes) {
    void *p = NULL;
    if (align < sizeof(void *)) align = sizeof(void *);
    /* posix_memalign wants a power-of-two multiple of sizeof(void*), which
     * every alignment an artifact stamps is. */
    if (posix_memalign(&p, align, bytes ? bytes : 1) != 0) return NULL;
    /* Touch every page ONCE, here, so the first timed loop does not pay the
     * page faults for storage the match may never fill. */
    memset(p, 0, bytes);
    return p;
}

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
    long long buffer_frames = -1, buffer_trail = -1;
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
        else if (!strcmp(a, "--buffer-frames") && i + 1 < argc)  buffer_frames = strtoll(argv[++i], NULL, 10);
        else if (!strcmp(a, "--buffer-trail") && i + 1 < argc)   buffer_trail = strtoll(argv[++i], NULL, 10);
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    if (!lib_path) { printf("error\t--lib is required\n"); return 2; }
    if (iters < 1) iters = 1;
    if ((buffer_frames >= 0) != (buffer_trail >= 0)) {
        printf("error\t--buffer-frames and --buffer-trail go together: both "
               "regions are required by a non-NULL descriptor (match_api.md "
               "10.2)\n");
        return 2;
    }
    if (buffer_frames == 0 || buffer_trail == 0) {
        printf("error\ta buffer capacity of 0 is not a buffer\n");
        return 2;
    }

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
    SYM(pb_err_floor); SYM(pb_err_giveup_top); SYM(pb_err_internal);
    SYM(pb_err_name);
    SYM(pb_has_vm_stamps); SYM(pb_vm_prefilter); SYM(pb_vm_rungs);
    SYM(pb_vm_strats); SYM(pb_vm_prunes); SYM(pb_engine_stamp);
    SYM(pb_shim_min_abi); SYM(pb_info_scan); SYM(pb_info_prefilter);
    SYM(pb_has_dfa_stamps); SYM(pb_dfa_scan); SYM(pb_dfa_prefilter);
    SYM(pb_dfa_table);
    SYM(pb_dfa_prefilter_offsets); SYM(pb_dfa_scan_edge);
    SYM(pb_dfa_match); SYM(pb_info_match_form);
    SYM(pb_info_name); SYM(pb_info_nentries);
    SYM(pb_dfa_start); SYM(pb_info_search_form);
    SYM(pb_has_vm_frameless); SYM(pb_vm_frameless);
    SYM(pb_has_altcls); SYM(pb_altcls_merges); SYM(pb_altcls_factored);
    SYM(pb_has_dfa_uniform_folds); SYM(pb_dfa_uniform_folds);
    SYM(pb_has_vm_alt_islands); SYM(pb_vm_alt_islands);
    SYM(pb_has_vm_entry_shape); SYM(pb_vm_entry_shape);
    SYM(pb_vm_program_bytes);
    SYM(pb_has_unroll_k); SYM(pb_unroll_k); SYM(pb_unroll_k_why);
    SYM(pb_has_max_emit_code_bytes); SYM(pb_max_emit_code_bytes);
    SYM(pb_has_max_emit_bytes); SYM(pb_max_emit_bytes);
    SYM(pb_has_engine_sel); SYM(pb_engine_sel);
    SYM(pb_has_vm_prefilter_lang); SYM(pb_vm_prefilter_lang);
    SYM(pb_vm_prefilter_lang_why);
    SYM(pb_has_fast_tier); SYM(pb_fast_frames); SYM(pb_fast_trail);
    SYM(pb_search); SYM(pb_match_caps);
    SYM(pb_has_in_entries); SYM(pb_buffer_align);
    SYM(pb_resume_frames); SYM(pb_trail_frames);
    SYM(pb_resume_frame_size); SYM(pb_trail_frame_size);
    SYM(pb_search_in); SYM(pb_match_caps_in);

    /* engine_metadata, `pattern`-scoped: read from the artifact's STRUCTURED
     * fields, never from the prose RX_ENGINE_WHY (requirements 4.2). The
     * prose goes out as `engine_why` and the adapter puts it in the row's
     * unindexed `diagnostic`, which is where record_schema.md 7 puts it. */
    /* The give-up code SPACE, from the artifact's own constants. The harness
     * classifies a negative return by RANGE against these, never by a list.
     * See shim.c. */
    /* THE ABI FLOOR, before anything else is read or printed. shim.c reads
     * `rx_info.scan` / `.prefilter` (appended at pcrec's abi 6),
     * `rx_info.match_form` (abi 10), `rx_info.name` / `.nentries`
     * (abi 15, [DD-13b.W1.2]) and `rx_info.search_form` (abi 16,
     * [OPT-5] STEP 2); an older artifact has no
     * such fields and this shim would be reading past them. Refuse by NAME,
     * carrying both numbers, and stop. The number itself is shim.c's. */
    if (pb_abi() < pb_shim_min_abi()) {
        printf("error\tabi-below-shim-floor: artifact rx_info.abi %d is below "
               "the %d this shim was written for (testees/pcrec/shim.c reads "
               "rx_info.scan/.prefilter, appended at pcrec abi 6, "
               "rx_info.match_form, appended at abi 10, "
               "rx_info.name/.nentries, appended at abi 15, and "
               "rx_info.search_form, appended at abi 16). Re-pin, or point "
               "PCREC_BIN at a pcrec at or after that abi.\n",
               pb_abi(), pb_shim_min_abi());
        fflush(stdout);
        return 3;
    }

    printf("info\terr_floor\t%d\n", pb_err_floor());
    printf("info\terr_giveup_top\t%d\n", pb_err_giveup_top());
    printf("info\terr_internal\t%d\n", pb_err_internal());
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

    /* The abi-6 RUNTIME MIRRORS (match_api.md 6). `prefilter` is documented
     * never to be NULL; it is printed unconditionally so the adapter can
     * SEE a NULL and report the contract violation rather than infer one
     * from a line that is simply missing. `scan` may legitimately be NULL
     * (a non-hybrid VM artifact), so its presence is printed as its own
     * fact -- on every artifact, so that "not a hybrid" is read from a
     * VALUE and never from silence. */
    {
        const char *rs = pb_info_scan();
        const char *rp = pb_info_prefilter();
        printf("info\trxinfo_scan_present\t%d\n", rs ? 1 : 0);
        if (rs) printf("info\trxinfo_scan\t%s\n", rs);
        printf("info\trxinfo_prefilter_present\t%d\n", rp ? 1 : 0);
        if (rp) printf("info\trxinfo_prefilter\t%s\n", rp);
    }

    /* The DFA-SCAN stamps: on every artifact that CONTAINS a DFA scan (every
     * DFA artifact AND every VM hybrid -- match_api.md 6.3 (a)'s iff), and on
     * no other. `dfa_table` is [OPT-3]/abi 7 and can be absent while the
     * other two are present; that is "this pcrec did not stamp it", printed
     * as nothing at all rather than as a value. */
    if (pb_has_dfa_stamps()) {
        const char *ds = pb_dfa_scan(), *dp = pb_dfa_prefilter();
        const char *dt = pb_dfa_table(), *dofs = pb_dfa_prefilter_offsets();
        const char *dse = pb_dfa_scan_edge();
        const char *dst = pb_dfa_start();
        if (ds) printf("info\tdfa_scan\t%s\n", ds);
        if (dp) printf("info\tdfa_prefilter\t%s\n", dp);
        if (dt) printf("info\tdfa_table\t%s\n", dt);
        /* [OPT-K], abi 9: same scope as the three above. */
        if (dofs) printf("info\tdfa_prefilter_offsets\t%s\n", dofs);
        /* [OPT-5] STEP 1, abi 13: same scope again (match_api.md 6.3: the
         * scan edge "joins that iff unchanged"). */
        if (dse) printf("info\tdfa_scan_edge\t%s\n", dse);
        /* [OPT-5] STEP 2, abi 16 ([B34]): the SEARCH entry's start form,
         * the same iff a third time. Its rx_info mirror is printed with
         * the other FIELD lines below, outside this guard, so its
         * presence is read from a VALUE on every artifact. */
        if (dst) printf("info\tdfa_start\t%s\n", dst);
        /* [CC-DIFF] STEP 1, abi 17 ([B37]): the fold COUNT, on
         * RX_DFA_TABLE's own scope (every artifact that CONTAINS a DFA
         * scan) -- an INTEGER whose 0 is a value ("every table had a
         * varying cell"), so it is printed behind its own presence
         * question rather than tested for truth. */
        if (pb_has_dfa_uniform_folds())
            printf("info\tdfa_uniform_folds\t%lld\n", pb_dfa_uniform_folds());
    }

    /* [ENG-ABS], abi 10: the `_match` ENTRY's form. NOT gated on
     * pb_has_dfa_stamps() -- its scope is "RX_ENGINE is dfa", which a VM
     * hybrid (which has the DFA-scan stamps) is NOT in. The macro is printed
     * when stamped; the FIELD's presence is printed on EVERY artifact, so a
     * NULL match_form on a VM artifact is a value the adapter reads, and the
     * macro-vs-field agreement is checked there. */
    {
        const char *dm = pb_dfa_match();
        const char *mf = pb_info_match_form();
        if (dm) printf("info\tdfa_match\t%s\n", dm);
        printf("info\trxinfo_match_form_present\t%d\n", mf ? 1 : 0);
        if (mf) printf("info\trxinfo_match_form\t%s\n", mf);
    }

    /* [DD-13b.W1.2], abi 15: the two fields appended after `match_form`.
     * Both are FIELDS with no macro spelling, so neither is a
     * two-spellings pair: they are PROVENANCE, printed on every artifact
     * (the shim's floor is 15, so an artifact that reached this point has
     * them). `name` is NEVER NULL by contract -- a compile that supplies
     * no name stamps its own <prefix> -- so a `_present 0` here is a
     * contract violation the adapter refuses by name, not an "unnamed"
     * artifact. `nentries` is the WHOLE groups[] length, of which `nnames`
     * (printed above) counts a PREFIX. */
    {
        const char *an = pb_info_name();
        printf("info\trxinfo_name_present\t%d\n", an ? 1 : 0);
        if (an) printf("info\tartifact_name\t%s\n", an);
        printf("info\tnentries\t%d\n", pb_info_nentries());
    }

    /* [OPT-5] STEP 2, abi 16 ([B34]): the FIELD appended after `nentries`,
     * printed on EVERY artifact exactly as `match_form` is and for the
     * same reason -- so that "this artifact has no search form" is read
     * from a value and never from a missing line. Its NULL rule is
     * `scan`'s and NOT `match_form`'s: NON-NULL on every artifact that
     * CONTAINS a DFA scan, VM hybrids included, NULL only on a plain VM
     * artifact. On one hybrid, therefore, `rxinfo_match_form_present 0`
     * and `rxinfo_search_form_present 1` are printed together, and that
     * pair is the whole difference between the two iffs. The macro
     * spelling (`dfa_start`) is printed above; the adapter checks the two
     * against each other. */
    {
        const char *sf = pb_info_search_form();
        printf("info\trxinfo_search_form_present\t%d\n", sf ? 1 : 0);
        if (sf) printf("info\trxinfo_search_form\t%s\n", sf);
    }

    /* [ART-SIZE], abi 11: the size term's four stamps. `unroll_k` /
     * `unroll_k_why` / `max_emit_code_bytes` are VM-only; `max_emit_bytes`
     * is on both engines. Each printed only when stamped -- an absence is
     * "not stamped", and the adapter decides from the abi whether that is
     * a contract violation. */
    if (pb_has_unroll_k()) {
        const char *why = pb_unroll_k_why();
        printf("info\tunroll_k\t%lld\n", pb_unroll_k());
        if (why) printf("info\tunroll_k_why\t%s\n", why);
    }
    if (pb_has_max_emit_code_bytes())
        printf("info\tmax_emit_code_bytes\t%lld\n", pb_max_emit_code_bytes());
    if (pb_has_max_emit_bytes())
        printf("info\tmax_emit_bytes\t%lld\n", pb_max_emit_bytes());

    /* [OPT-4], abi 12 ([B19]): the engine ROUTE token (every artifact,
     * both engines) and the prefilter LANGUAGE pair (every VM HYBRID --
     * where RX_VM_PREFILTER reads "hybrid" -- and no other artifact,
     * match_api.md 6.3). Each printed only when stamped; the adapter's
     * scope table decides from the abi whether an absence is a contract
     * violation. Nothing is inferred from a missing line. */
    if (pb_has_engine_sel()) {
        const char *sel = pb_engine_sel();
        if (sel) printf("info\tengine_sel\t%s\n", sel);
    }
    if (pb_has_vm_prefilter_lang()) {
        const char *lang = pb_vm_prefilter_lang();
        const char *lwhy = pb_vm_prefilter_lang_why();
        if (lang) printf("info\tvm_prefilter_lang\t%s\n", lang);
        if (lwhy) printf("info\tvm_prefilter_lang_why\t%s\n", lwhy);
    }

    /* The two-tier default entry's capacities ([OPT-1], abi 5): VM-only,
     * never absent on a VM artifact. `fast_frames == resume_frames` IS
     * "this artifact has one tier" and is the only spelling of it. */
    if (pb_has_fast_tier()) {
        printf("info\tfast_frames\t%lld\n", pb_fast_frames());
        printf("info\tfast_trail\t%lld\n", pb_fast_trail());
    }

    /* [OPT-VMFL], abi 16 ([B34]): whether the emitted VM program contains
     * any RX_PUSH site or linked call -- 1 = none, so no pop-and-resume
     * dispatch at the fail label; 0 = it does. VM-only (hybrids included),
     * unconditional there, absent on every DFA artifact. Printed only when
     * the artifact stamps it, so the ABSENCE says "not a VM artifact" and
     * the VALUE 0 says "this program does push": two different facts,
     * which is why the shim exports the presence question separately. */
    if (pb_has_vm_frameless())
        printf("info\tvm_frameless\t%d\n", pb_vm_frameless());

    /* [ENG-ISL] STEP 1, abi 18 ([B37]): how many flat alternations this
     * VM program lowered as an alternation ISLAND (a trie) rather than
     * as vm_alt's resume chain. VM-only (hybrids included), unconditional
     * there, absent on every DFA artifact -- vm_frameless's scope, printed
     * on its terms: the VALUE 0 is "no alternation qualified" (or
     * -fno-alt-island), the ABSENCE "not a VM artifact". */
    if (pb_has_vm_alt_islands())
        printf("info\tvm_alt_islands\t%lld\n", pb_vm_alt_islands());

    /* [CC-DIFF] STEP 2, abi 22 ([B37]): the entry-chain rung the emitter
     * TOOK (a closed token) and the program size AUTO compared against
     * VM_INLINE_CHAIN_MAX_BYTES to choose it. Printed together behind
     * one presence check (one emitter call lands both), VM-only. */
    if (pb_has_vm_entry_shape()) {
        printf("info\tvm_entry_shape\t%s\n", pb_vm_entry_shape());
        printf("info\tvm_program_bytes\t%lld\n", pb_vm_program_bytes());
    }

    /* [OPT-ALTCLS], pcrec I-39: COMMON to both engines, unconditional
     * since long before this pin -- this shim only started reading it at
     * abi 16. Printed together, behind one presence check, only when the
     * artifact stamps them (the defensive #ifdef on the consumer side that
     * every macro here gets), which in practice is every artifact this
     * driver will ever load. */
    if (pb_has_altcls()) {
        printf("info\taltcls_merges\t%lld\n", pb_altcls_merges());
        printf("info\taltcls_factored\t%lld\n", pb_altcls_factored());
    }

    /* The frame-buffer sizing surface (match_api.md 10.4), whenever the
     * artifact stamps it -- both engines at abi 3; a DFA artifact stamps
     * zeros, which is its honest "no buffers" signal and is recorded as
     * such. */
    if (pb_has_in_entries()) {
        printf("info\tresume_frames\t%lld\n", pb_resume_frames());
        printf("info\ttrail_frames\t%lld\n", pb_trail_frames());
        printf("info\tresume_frame_size\t%lld\n", pb_resume_frame_size());
        printf("info\ttrail_frame_size\t%lld\n", pb_trail_frame_size());
        printf("info\tbuffer_align\t%lld\n", pb_buffer_align());
    }

    if (buffer_frames > 0) {
        if (!pb_has_in_entries()) {
            printf("error\t--buffer-frames/--buffer-trail given but this "
                   "artifact has no _in surface (pcrec before [DD-14.FB], "
                   "abi < 3)\n");
            return 2;
        }
        long long fs = pb_resume_frame_size(), ts = pb_trail_frame_size();
        if (fs <= 0 || ts <= 0) {
            /* 10.4: a stamped 0 means the engine takes no buffers. NEVER
             * divide by it; pass no descriptor. */
            printf("info\tbuffer_inert\tstamped-size-0\n");
        } else {
            size_t align = (size_t)pb_buffer_align();
            buf_nframes = (size_t)buffer_frames;
            buf_ntrail  = (size_t)buffer_trail;
            buf_frames = alloc_region(align, buf_nframes * (size_t)fs);
            buf_trail  = alloc_region(align, buf_ntrail * (size_t)ts);
            if (!buf_frames || !buf_trail) {
                printf("error\tcould not allocate the frame buffer: %lld "
                       "frames x %lld B + %lld entries x %lld B\n",
                       buffer_frames, fs, buffer_trail, ts);
                return 2;
            }
            use_buffers = 1;
            printf("info\tbuffer_frames\t%lld\n", buffer_frames);
            printf("info\tbuffer_trail\t%lld\n", buffer_trail);
        }
    }

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
                    long long r = do_match_caps(s->buf, s->len, 0, caps);
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
                        int r = do_search(s->buf, s->len, pos, caps);
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
                    int r = do_search(s->buf, s->len, 0, caps);
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
                const char *nm = pb_err_name((int)giveup);
                /* `giveup:<code>:<NAME>` -- the harness maps the CODE by
                 * range and puts the NAME in the row's diagnostic. */
                if (nm)
                    snprintf(answerbuf, sizeof answerbuf, "giveup:%d:%s",
                             (int)giveup, nm);
                else
                    snprintf(answerbuf, sizeof answerbuf, "giveup:%d",
                             (int)giveup);
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
