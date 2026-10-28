/* testees/common/vars_io.h -- the CALLER-VARIABLES half of `--mode calls`
 * ([B148] L7, docs/design/unusual_set_v1.md 3.3 / 7.3; the contract is
 * bench/unusual/assists/problems/vars.md and pcrecbench/adapters.py's
 * "--mode calls"). Header-only like calls_io.h, which it includes; shared by
 * every driver that runs a vars stream (today the pcrec driver; the assisted
 * engines' drivers are L6's).
 *
 * THE LIST FILE of a vars stream has FOUR columns,
 * `id<TAB>subject<TAB>calls<TAB>bindings`; the calls file is the usual
 * `call_id offset length segment_bytes binding_id`, but a call is ONE LINE of
 * the subject -- bytes [offset, offset + length) -- matched ALONE (the line is
 * its own subject: `^` is its start, result offsets are LINE-RELATIVE), and
 * every call names a binding. The bindings file is
 * `binding_id<TAB>name<TAB>value`, value = lowercase HEX of the bytes (a
 * NUL is "00"), or the literal `UNSET` (the variable has no value) or `EMPTY`
 * (set, zero bytes) -- vars.md 3 keeps the two states distinct.
 *
 * Everything here runs OUTSIDE the clock: parsing, hex decoding, resolving
 * each call's binding id to an index (bsearch), building each binding's
 * variable array ONCE. The timed loop (a driver's timed_calls_vars.*) indexes
 * `bindings[call.binding]` -- no lookup, no allocation inside a replay. */
#ifndef PCRECBENCH_VARS_IO_H
#define PCRECBENCH_VARS_IO_H

#include "calls_io.h"

/* One variable of one binding: the LAYOUT of pcrec's rx_var (name, p, len);
 * p == NULL is UNSET (len then ignored), p != NULL && len == 0 is EMPTY. */
struct vvar {
    const char *name;
    const unsigned char *p;
    size_t len;
};

struct vbinding {
    char *id;
    struct vvar *vars;
    size_t nvars;
};

struct vcall_decl {
    size_t offset, length;
    size_t binding;                 /* index into the subject's bindings[] */
};

struct vars_subject {
    char *id;
    unsigned char *buf;
    size_t len;
    struct vcall_decl *calls;
    size_t ncalls;
    unsigned long long segment_bytes;
    struct vbinding *bindings;
    size_t nbindings;
};

CALLS_FN int vars_hexval(int c) {
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'a' && c <= 'f') return c - 'a' + 10;
    if (c >= 'A' && c <= 'F') return c - 'A' + 10;
    return -1;
}

CALLS_FN int vars_cmp_binding(const void *a, const void *b) {
    return strcmp(((const struct vbinding *)a)->id, ((const struct vbinding *)b)->id);
}

/* The bindings file -> a binding array SORTED by id (rows of one binding are
 * consecutive in the file; a repeated id after a different one is an error). */
CALLS_FN int vars_load_bindings(const char *path, struct vbinding **out, size_t *n_out) {
    FILE *f = fopen(path, "r");
    if (!f) { printf("error\tfopen %s: %s\n", path, strerror(errno)); return 2; }
    size_t cap = 64, n = 0;
    struct vbinding *v = (struct vbinding *)calloc(cap, sizeof *v);
    char *line = (char *)malloc(1 << 20);
    int first = 1;
    if (!v || !line) { printf("error\tout of memory\n"); fclose(f); return 2; }
    while (fgets(line, 1 << 20, f)) {
        char *nl = strchr(line, '\n');
        if (nl) *nl = 0;
        if (first) { first = 0; if (!strncmp(line, "binding_id\t", 11)) continue; }
        if (!*line) continue;
        char *t1 = strchr(line, '\t');
        char *t2 = t1 ? strchr(t1 + 1, '\t') : NULL;
        if (!t1 || !t2) {
            printf("error\t%s: malformed binding row: %s\n", path, line);
            fclose(f); return 2;
        }
        *t1 = 0; *t2 = 0;
        const char *bid = line, *name = t1 + 1, *val = t2 + 1;
        if (n == 0 || strcmp(v[n - 1].id, bid) != 0) {
            for (size_t k = 0; k < n; k++)
                if (!strcmp(v[k].id, bid)) {
                    printf("error\t%s: binding %s is not contiguous\n", path, bid);
                    fclose(f); return 2;
                }
            if (n == cap) { cap *= 2; v = (struct vbinding *)realloc(v, cap * sizeof *v); memset(v + n, 0, (cap - n) * sizeof *v); }
            v[n].id = strdup(bid);
            n++;
        }
        struct vbinding *b = &v[n - 1];
        b->vars = (struct vvar *)realloc(b->vars, (b->nvars + 1) * sizeof *b->vars);
        struct vvar *x = &b->vars[b->nvars++];
        x->name = strdup(name);
        if (!strcmp(val, "UNSET")) { x->p = NULL; x->len = 0; }
        else if (!strcmp(val, "EMPTY")) { x->p = (const unsigned char *)malloc(1); x->len = 0; }
        else {
            size_t hl = strlen(val);
            if (hl % 2) { printf("error\t%s: odd-length hex for %s/%s\n", path, bid, name); fclose(f); return 2; }
            unsigned char *p = (unsigned char *)malloc(hl / 2 + 1);
            for (size_t i = 0; i < hl / 2; i++) {
                int h = vars_hexval(val[2 * i]), l = vars_hexval(val[2 * i + 1]);
                if (h < 0 || l < 0) { printf("error\t%s: bad hex for %s/%s\n", path, bid, name); fclose(f); return 2; }
                p[i] = (unsigned char)(h * 16 + l);
            }
            x->p = p; x->len = hl / 2;
        }
    }
    fclose(f); free(line);
    if (n == 0) { printf("error\t%s declares no bindings\n", path); return 2; }
    qsort(v, n, sizeof *v, vars_cmp_binding);
    *out = v; *n_out = n;
    return 0;
}

/* The call list of a vars stream: every call names a binding (a `-` is an
 * error), is resolved to its index here, and must lie inside the subject. */
CALLS_FN int vars_load_calls(const char *path, size_t subject_len,
                           const struct vbinding *bindings, size_t nb,
                           struct vcall_decl **out, size_t *n_out,
                           unsigned long long *segb_out) {
    FILE *f = fopen(path, "r");
    if (!f) { printf("error\tfopen %s: %s\n", path, strerror(errno)); return 2; }
    size_t cap = 1024, n = 0;
    unsigned long long segb = 0;
    struct vcall_decl *v = (struct vcall_decl *)malloc(cap * sizeof *v);
    char line[512];
    int first = 1;
    while (fgets(line, sizeof line, f)) {
        if (first) { first = 0; if (!strncmp(line, "call_id\t", 8)) continue; }
        if (line[0] == '\n' || !line[0]) continue;
        char binding[256];
        unsigned long long cid, off, ln, sb;
        if (sscanf(line, "%llu\t%llu\t%llu\t%llu\t%255s", &cid, &off, &ln, &sb, binding) != 5) {
            printf("error\t%s: malformed call row: %s", path, line);
            fclose(f); free(v); return 2;
        }
        if (!strcmp(binding, "-")) {
            printf("error\t%s: call %llu has no binding (a vars stream names one per call)\n", path, cid);
            fclose(f); free(v); return 2;
        }
        struct vbinding key = { binding, NULL, 0 };
        struct vbinding *hit = (struct vbinding *)bsearch(&key, bindings, nb, sizeof *bindings, vars_cmp_binding);
        if (!hit) {
            printf("error\t%s: call %llu names binding %s, which the bindings file does not declare\n", path, cid, binding);
            fclose(f); free(v); return 2;
        }
        if (off > subject_len || ln > subject_len - off) {
            printf("error\t%s: call %llu (offset %llu, length %llu) lies outside the %zu-byte subject\n",
                   path, cid, off, ln, subject_len);
            fclose(f); free(v); return 2;
        }
        if (n == cap) { cap *= 2; v = (struct vcall_decl *)realloc(v, cap * sizeof *v); }
        v[n].offset = (size_t)off; v[n].length = (size_t)ln; v[n].binding = (size_t)(hit - bindings);
        segb += sb;
        n++;
    }
    fclose(f);
    if (n == 0) { printf("error\t%s declares no calls\n", path); free(v); return 2; }
    *out = v; *n_out = n; *segb_out = segb;
    return 0;
}

/* Does this `--list` file carry a fourth (bindings) column on its first
 * stream? A vars list is homogeneous: the harness writes four columns for a
 * vars stream and three for any other, and never mixes them in one list
 * because a (pattern, regime) cell runs the streams of ONE pattern. */
CALLS_FN int vars_list_has_bindings(const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) return 0;
    char line[8192];
    int tabs = 0;
    while (fgets(line, sizeof line, f)) {
        if (line[0] == '\n') continue;
        for (char *p = line; *p; p++) tabs += (*p == '\t');
        break;
    }
    fclose(f);
    return tabs >= 3;
}

/* The `--list` file in vars mode: `id subject calls bindings` per line. */
CALLS_FN struct vars_subject *vars_load_list(const char *path, size_t *n_out) {
    FILE *f = fopen(path, "r");
    if (!f) { printf("error\tcannot read subject list %s\n", path); return NULL; }
    size_t cap = 8, n = 0;
    struct vars_subject *v = (struct vars_subject *)calloc(cap, sizeof *v);
    char line[8192];
    while (fgets(line, sizeof line, f)) {
        char *nl = strchr(line, '\n');
        if (nl) *nl = 0;
        if (!*line) continue;
        char *t1 = strchr(line, '\t');
        char *t2 = t1 ? strchr(t1 + 1, '\t') : NULL;
        char *t3 = t2 ? strchr(t2 + 1, '\t') : NULL;
        if (!t1 || !t2 || !t3) {
            printf("error\t%s: a vars stream needs `id<TAB>subject<TAB>calls<TAB>bindings` per line\n", path);
            fclose(f); return NULL;
        }
        *t1 = 0; *t2 = 0; *t3 = 0;
        if (n == cap) { cap *= 2; v = (struct vars_subject *)realloc(v, cap * sizeof *v); memset(v + n, 0, (cap - n) * sizeof *v); }
        struct vars_subject *s = &v[n];
        s->id = strdup(line);
        s->buf = calls_slurp(t1 + 1, &s->len);
        if (!s->buf) { fclose(f); return NULL; }
        if (vars_load_bindings(t3 + 1, &s->bindings, &s->nbindings)) { fclose(f); return NULL; }
        if (vars_load_calls(t2 + 1, s->len, s->bindings, s->nbindings, &s->calls, &s->ncalls, &s->segment_bytes)) {
            fclose(f); return NULL;
        }
        n++;
    }
    fclose(f);
    *n_out = n;
    return v;
}

#endif
