/* testees/common/calls_io.h -- the `--mode calls` I/O every C/C++ driver
 * shares ([B148] L4, docs/design/unusual_set_v1.md 7.1-7.3; the protocol is
 * pcrecbench/adapters.py's docstring, "--mode calls").
 *
 * EVERYTHING HERE RUNS OUTSIDE THE CLOCK: reading the subject list (3
 * columns in this mode: id, subject path, calls path), reading a call list,
 * turning the preallocated per-call results into the protocol's tokens and
 * writing them to `<tokens-dir>/<id>.tok`, and printing the `stream` line.
 * The timed replay loop lives in each driver's own `timed_calls.*` (BD16:
 * a new mode is a new instrument TU, the existing `timed.*` untouched).
 *
 * THE TOKENS (7.1): `n` no match, `m:<s>,<e>` group 0, `m:<s>,<e>;<g1s>,<g1e>`
 * when the pattern HAS a group 1 (an unset group 1 is `-1,-1`), `r` a call the
 * HOST refused without calling the engine (vars only; never produced here
 * until lane L7), `g` a call the engine gave up on. One token per line; the
 * harness hashes the file (sha256 of the tokens each followed by "\n", the
 * spelling bench/unusual/gen_expectations.py derives `results_sha256` with),
 * so SHA-256 stays out of every driver -- the [B140] `out` line precedent.
 *
 * Header-only (static functions), so each driver links nothing new; a C++
 * driver (RE2) includes it inside its own translation unit. */
#ifndef PCRECBENCH_CALLS_IO_H
#define PCRECBENCH_CALLS_IO_H

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* static, noinline (kept out of a caller's sigsetjmp frame), and silent where a
 * translation unit (timed_calls.c) includes the
 * header for its types only */
#define CALLS_FN static __attribute__((unused, noinline))

/* One call's RESULT, written by the timed loop into a preallocated array. */
enum { CALL_N = 0, CALL_M = 1, CALL_R = 2, CALL_G = 3 };
struct call_res {
    int kind;           /* CALL_N / CALL_M / CALL_R / CALL_G */
    int code;           /* CALL_G: the engine's own return code */
    long s, e;          /* CALL_M: group 0 */
    long g1s, g1e;      /* CALL_M with a group 1 (else unused); -1 unset */
};

/* One declared call: (offset, length) into the subject. `length` is the
 * segment's declared span -- the throughput denominator only; the engine is
 * given the REST of the subject from `offset` (7.1). */
struct call_decl {
    size_t offset, length;
};

struct calls_subject {
    char *id;
    unsigned char *buf;
    size_t len;
    struct call_decl *calls;
    size_t ncalls;
    unsigned long long segment_bytes;
};

CALLS_FN unsigned char *calls_slurp(const char *path, size_t *sz_out) {
    FILE *f = fopen(path, "rb");
    if (!f) { printf("error\tfopen %s: %s\n", path, strerror(errno)); return NULL; }
    if (fseek(f, 0, SEEK_END) != 0) { fclose(f); return NULL; }
    long sz = ftell(f);
    if (sz < 0) { fclose(f); return NULL; }
    rewind(f);
    unsigned char *buf = (unsigned char *)malloc((size_t)sz + 1);
    if (!buf) { fclose(f); return NULL; }
    if (sz > 0 && fread(buf, 1, (size_t)sz, f) != (size_t)sz) {
        fclose(f); free(buf); return NULL;
    }
    buf[sz] = 0;
    fclose(f);
    *sz_out = (size_t)sz;
    return buf;
}

/* The call list: a header row, then `call_id offset length segment_bytes
 * binding_id` per call (bench/unusual/gen_streams.py). A binding other than
 * `-` is a VARS stream (lane L7): refused BY NAME, never ignored. Every call
 * must lie inside the subject. -> 0 ok, else an `error` line was printed. */
CALLS_FN int calls_load_decl(const char *path, size_t subject_len,
                           struct call_decl **out, size_t *n_out,
                           unsigned long long *segb_out) {
    FILE *f = fopen(path, "r");
    if (!f) { printf("error\tfopen %s: %s\n", path, strerror(errno)); return 2; }
    size_t cap = 256, n = 0;
    unsigned long long segb = 0;
    struct call_decl *v = (struct call_decl *)malloc(cap * sizeof *v);
    char line[512];
    int first = 1;
    while (fgets(line, sizeof line, f)) {
        if (first) {
            first = 0;
            if (!strncmp(line, "call_id\t", 8)) continue;
        }
        if (line[0] == '\n' || !line[0]) continue;
        char binding[128];
        unsigned long long cid, off, ln, sb;
        if (sscanf(line, "%llu\t%llu\t%llu\t%llu\t%127s", &cid, &off, &ln,
                   &sb, binding) != 5) {
            printf("error\t%s: malformed call row: %s", path, line);
            fclose(f); free(v); return 2;
        }
        if (strcmp(binding, "-")) {
            printf("error\t%s: call %llu names binding %s -- a vars stream "
                   "(--bindings) is lane L7's, not implemented by this "
                   "driver\n", path, cid, binding);
            fclose(f); free(v); return 2;
        }
        if (off > subject_len || ln > subject_len - off) {
            printf("error\t%s: call %llu (offset %llu, length %llu) lies "
                   "outside the %zu-byte subject\n", path, cid, off, ln,
                   subject_len);
            fclose(f); free(v); return 2;
        }
        if (n == cap) { cap *= 2; v = (struct call_decl *)realloc(v, cap * sizeof *v); }
        v[n].offset = (size_t)off;
        v[n].length = (size_t)ln;
        segb += sb;
        n++;
    }
    fclose(f);
    if (n == 0) { printf("error\t%s declares no calls\n", path); free(v); return 2; }
    *out = v; *n_out = n; *segb_out = segb;
    return 0;
}

/* The `--list` file in calls mode: `id<TAB>subject<TAB>calls` per line. */
CALLS_FN struct calls_subject *calls_load_list(const char *path, size_t *n_out) {
    FILE *f = fopen(path, "r");
    if (!f) { printf("error\tcannot read subject list %s\n", path); return NULL; }
    size_t cap = 8, n = 0;
    struct calls_subject *v = (struct calls_subject *)malloc(cap * sizeof *v);
    char line[8192];
    while (fgets(line, sizeof line, f)) {
        char *nl = strchr(line, '\n');
        if (nl) *nl = 0;
        if (!*line) continue;
        char *t1 = strchr(line, '\t');
        char *t2 = t1 ? strchr(t1 + 1, '\t') : NULL;
        if (!t1 || !t2) {
            printf("error\t%s: --mode calls needs `id<TAB>subject<TAB>calls` "
                   "per line\n", path);
            fclose(f); return NULL;
        }
        *t1 = 0; *t2 = 0;
        if (n == cap) { cap *= 2; v = (struct calls_subject *)realloc(v, cap * sizeof *v); }
        v[n].id = strdup(line);
        v[n].buf = calls_slurp(t1 + 1, &v[n].len);
        if (!v[n].buf) { fclose(f); return NULL; }
        if (calls_load_decl(t2 + 1, v[n].len, &v[n].calls, &v[n].ncalls,
                            &v[n].segment_bytes)) {
            fclose(f); return NULL;
        }
        n++;
    }
    fclose(f);
    *n_out = n;
    return v;
}

/* After the clock: the per-call results -> the counts, the token file and
 * the `stream` line. `has_g1` says whether the pattern has a group 1.
 * `first_limit` is the engine's own NAME for the first give-up's code when
 * the driver knows it (pcrec's shim does), else NULL (the adapter names it
 * from its measured code table). */
CALLS_FN void calls_report(const char *id, const struct call_res *res,
                         size_t ncalls, int has_g1, const char *tokens_dir,
                         const char *first_limit) {
    size_t matched = 0, nomatch = 0, refused = 0, gave_up = 0;
    int first_code = 0, have_first = 0;
    char path[4096];
    FILE *tf = NULL;
    path[0] = 0;
    if (tokens_dir) {
        snprintf(path, sizeof path, "%s/%s.tok", tokens_dir, id);
        tf = fopen(path, "w");
        if (!tf) {
            printf("error\tcannot write %s: %s\n", path, strerror(errno));
            path[0] = 0;
        }
    }
    for (size_t i = 0; i < ncalls; i++) {
        const struct call_res *r = &res[i];
        switch (r->kind) {
        case CALL_M:
            matched++;
            if (tf) {
                if (has_g1)
                    fprintf(tf, "m:%ld,%ld;%ld,%ld\n", r->s, r->e, r->g1s, r->g1e);
                else
                    fprintf(tf, "m:%ld,%ld\n", r->s, r->e);
            }
            break;
        case CALL_R:
            refused++;
            if (tf) fputs("r\n", tf);
            break;
        case CALL_G:
            gave_up++;
            if (!have_first) { first_code = r->code; have_first = 1; }
            if (tf) fputs("g\n", tf);
            break;
        default:
            nomatch++;
            if (tf) fputs("n\n", tf);
        }
    }
    if (tf) fclose(tf);
    char fc[32];
    if (have_first) snprintf(fc, sizeof fc, "%d", first_code);
    else strcpy(fc, "-");
    printf("stream\t%s\tcalls=%zu\tmatched=%zu\tnomatch=%zu\trefused=%zu\t"
           "gave_up=%zu\tfirst_code=%s\tfirst_limit=%s\tresults_sha256=-\t"
           "tokens=%s\n", id, ncalls, matched, nomatch, refused, gave_up, fc,
           (have_first && first_limit) ? first_limit : "-",
           path[0] ? path : "-");
}

#endif
