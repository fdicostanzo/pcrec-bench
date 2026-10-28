/* bench/unusual/callees/callees.c -- the shared callee bodies (callees.h).
 * Compiled ONCE by pcrecbench/callees.py with fixed flags; never by a
 * driver's own build. Each callee is a PURE function of its view: no state
 * but the member set built before any timed call, read-only after.
 *
 * -DUB_COUNT (the untimed counting object only): every fire appends one
 * line, `<callee>\t<pos>\t<g1s>\t<g1e>\t<verdict>`, to $UB_FIRE_LOG -- the
 * view the callee read and what it answered (unusual_set_v1.md 3.2
 * calibration items 1-2). The timed object has no counter and no log. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "callees.h"

#ifdef UB_COUNT
static FILE *ub_log;
static int ub_log_tried;

static void ub_note(const char *name, const struct ub_view *v, long verdict) {
    if (!ub_log_tried) {
        const char *p = getenv("UB_FIRE_LOG");
        ub_log_tried = 1;
        ub_log = p && *p ? fopen(p, "a") : NULL;
    }
    if (!ub_log) return;
    long g1s = -1, g1e = -1;
    if (v->ncap > 1) { g1s = (long)v->caps[1][0]; g1e = (long)v->caps[1][1]; }
    fprintf(ub_log, "%s\t%zu\t%ld\t%ld\t%ld\n", name, v->pos, g1s, g1e, verdict);
    fflush(ub_log);
}
#define UB_RETURN(name, v, r) do { long ub_r_ = (r); ub_note(name, v, ub_r_); return ub_r_; } while (0)
int ub_counting_build(void) { return 1; }
#else
#define UB_RETURN(name, v, r) return (r)
int ub_counting_build(void) { return 0; }
#endif

/* group 1's bytes, or 0 when it is unset */
static int g1(const struct ub_view *v, const unsigned char **p, size_t *n) {
    if (v->ncap < 2 || v->caps[1][0] < 0 || v->caps[1][1] < v->caps[1][0])
        return 0;
    *p = v->subject + v->caps[1][0];
    *n = (size_t)(v->caps[1][1] - v->caps[1][0]);
    return 1;
}

long ub_luhn(const struct ub_view *v) {
    const unsigned char *p;
    size_t n;
    if (!g1(v, &p, &n)) UB_RETURN("luhn", v, UB_FAIL);
    unsigned t = 0;
    for (size_t k = 0; k < n; k++) {
        unsigned d = (unsigned)(p[n - 1 - k] - '0');
        if (k & 1) { d *= 2; if (d > 9) d -= 9; }
        t += d;
    }
    UB_RETURN("luhn", v, t % 10 == 0 ? UB_CONTINUE : UB_FAIL);
}

long ub_isbn13(const struct ub_view *v) {
    const unsigned char *p;
    size_t n;
    if (!g1(v, &p, &n) || n != 13 || p[0] != '9' || p[1] != '7'
        || (p[2] != '8' && p[2] != '9'))
        UB_RETURN("isbn13", v, UB_FAIL);
    unsigned t = 0;
    for (size_t k = 0; k < 13; k++)
        t += (unsigned)(p[k] - '0') * ((k & 1) ? 3u : 1u);
    UB_RETURN("isbn13", v, t % 10 == 0 ? UB_CONTINUE : UB_FAIL);
}

/* ---- the member set: open addressing, FNV-1a, a power-of-two table */
struct ub_set {
    size_t mask;
    struct { const unsigned char *p; size_t n; } *slot;
};

static size_t fnv(const unsigned char *p, size_t n) {
    size_t h = (size_t)1469598103934665603ULL;
    for (size_t i = 0; i < n; i++) { h ^= p[i]; h *= (size_t)1099511628211ULL; }
    return h;
}

long ub_member(const struct ub_view *v) {
    const struct ub_set *s = v->user;
    const unsigned char *p;
    size_t n;
    if (!s || !g1(v, &p, &n)) UB_RETURN("member", v, UB_FAIL);
    for (size_t i = fnv(p, n) & s->mask;; i = (i + 1) & s->mask) {
        if (!s->slot[i].p) UB_RETURN("member", v, UB_FAIL);
        if (s->slot[i].n == n && memcmp(s->slot[i].p, p, n) == 0)
            UB_RETURN("member", v, UB_CONTINUE);
    }
}

void *ub_member_new(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) return NULL;
    struct ub_set *s = calloc(1, sizeof *s);
    size_t cap = 64;                       /* load factor <= 1/2 below */
    char line[512];
    size_t nnames = 0;
    unsigned char *names[256];
    size_t lens[256];
    while (fgets(line, sizeof line, f)) {
        size_t n = strcspn(line, "\r\n");
        while (n && (line[n - 1] == ' ' || line[n - 1] == '\t')) n--;
        if (!n || line[0] == '#') continue;
        if (nnames == 256) { fclose(f); free(s); return NULL; }
        names[nnames] = malloc(n);
        memcpy(names[nnames], line, n);
        lens[nnames++] = n;
    }
    fclose(f);
    while (cap < 2 * nnames) cap *= 2;
    s->mask = cap - 1;
    s->slot = calloc(cap, sizeof *s->slot);
    for (size_t k = 0; k < nnames; k++) {
        size_t i = fnv(names[k], lens[k]) & s->mask;
        while (s->slot[i].p) i = (i + 1) & s->mask;
        s->slot[i].p = names[k];
        s->slot[i].n = lens[k];
    }
    return s;
}

/* group 1 as a decimal length (the pattern admits 1-9 digits) */
static long g1_len(const struct ub_view *v) {
    const unsigned char *p;
    size_t n;
    if (!g1(v, &p, &n) || n == 0 || n > 9) return -1;
    long len = 0;
    for (size_t k = 0; k < n; k++) len = len * 10 + (p[k] - '0');
    return len;
}

/* pcrec's native `(\d{1,9}):(?C"netstr,consume"),` -- consume the declared
 * length in ONE fire; an overlong length (past the subject's end) FAILS the
 * candidate (consuming past the end traps, match_api 11.4 para 2). */
long ub_netstr(const struct ub_view *v) {
    long len = g1_len(v);
    if (len < 0 || (size_t)len > v->len - v->pos) UB_RETURN("netstr", v, UB_FAIL);
    UB_RETURN("netstr", v, len ? len : UB_CONTINUE);
}

/* the assisted `(\d{1,9}):(?>(?s:.)*?(?C4)),` -- the lazy run fires once
 * per data byte; pass exactly when the run is `len` bytes long (P3). */
long ub_netstr_end(const struct ub_view *v) {
    long len = g1_len(v);
    if (len < 0) UB_RETURN("netstr-end", v, UB_FAIL);
    size_t start = (size_t)v->caps[1][1] + 1;
    UB_RETURN("netstr-end", v, v->pos - start == (size_t)len ? UB_CONTINUE : UB_FAIL);
}

long ub_stub(const struct ub_view *v) {
    (void)v;
    UB_RETURN("stub", v, UB_CONTINUE);
}
