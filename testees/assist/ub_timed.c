/* testees/assist/ub_timed.c -- THE ASSIST RUNNER'S TIMED LOOPS, ISOLATED
 * ([B148] lane b148aw; BD16: each timed function noinline + aligned(64) in a
 * translation unit of its own). Everything between two clock reads is here:
 * the assist call through its function pointer and the integer bookkeeping
 * into a preallocated result. Tokens, hashing, printing: the runner, after
 * the clock (testees/common/calls_io.h). */
#include <time.h>

#include "ub_timed.h"

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

__attribute__((noinline, aligned(64)))
double ub_timed_search(const struct ub_search_in *in, struct ub_search_out *out) {
    const unsigned char *buf = in->buf;
    const size_t len = in->len;
    ub_find_fn *find = in->find;
    ub_span m;
    int rc = UB_N, rc_final = UB_N;
    long count = 0;
    double t0 = now();
    for (long it = 0; it < in->iters; it++) {
        if (!in->find_all) {
            rc = find(buf, len, 0, &m);
            if (rc == UB_M) out->first = m;
            continue;
        }
        count = 0;
        size_t pos = 0;
        rc_final = UB_N;
        for (;;) {
            int r = find(buf, len, pos, &m);
            if (count == 0) { rc = r; if (r == UB_M) out->first = m; }
            if (r != UB_M) { rc_final = r; break; }
            count++;
            pos = m.e > m.s ? (size_t)m.e : (size_t)m.s + 1;
            if (pos > len) break;
        }
    }
    double t1 = now();
    out->rc = rc;
    out->nmatch = rc_final < 0 ? -1 : count;
    out->rc_final = rc_final;
    return t1 - t0;
}

__attribute__((noinline, aligned(64)))
double ub_timed_calls(const struct ub_calls_in *in, struct ub_calls_out *out) {
    const size_t n = in->ncalls;
    ub_find_fn *find = in->find;
    struct call_res *res = in->res;
    ub_span m;
    double total = 0.0;
    for (long it = 0; it < in->iters; it++) {
        out->calls_done = 0;
        double t0 = now();
        for (size_t i = 0; i < n; i++) {
            struct call_res *r = &res[i];
            int rc = find(in->buf, in->len, in->calls[i].offset, &m);
            if (rc == UB_M) {
                r->kind = CALL_M;
                r->s = m.s; r->e = m.e; r->g1s = m.g1s; r->g1e = m.g1e;
            } else if (rc == UB_N) {
                r->kind = CALL_N;
            } else {
                r->kind = CALL_G;
                r->code = rc;
            }
            out->calls_done = i + 1;
        }
        total += now() - t0;
        out->replays_done = it + 1;
    }
    return total;
}

__attribute__((noinline, aligned(64)))
double ub_timed_vcalls(const struct ub_vcalls_in *in, struct ub_calls_out *out) {
    const size_t n = in->ncalls;
    ub_vars_fn *vars = in->vars;
    struct call_res *res = in->res;
    ub_span m;
    double total = 0.0;
    for (long it = 0; it < in->iters; it++) {
        out->calls_done = 0;
        double t0 = now();
        for (size_t i = 0; i < n; i++) {
            const struct vcall_decl *c = &in->calls[i];
            const struct vbinding *b = &in->bindings[c->binding];
            struct call_res *r = &res[i];
            int rc = vars(in->buf + c->offset, c->length,
                          (const ub_var *)b->vars, b->nvars, &m);
            if (rc == UB_M) {
                r->kind = CALL_M;
                r->s = m.s; r->e = m.e; r->g1s = r->g1e = -1;
            } else if (rc == UB_N) {
                r->kind = CALL_N;
            } else if (rc == UB_R) {
                r->kind = CALL_R;
            } else {
                r->kind = CALL_G;
                r->code = rc;
            }
            out->calls_done = i + 1;
        }
        total += now() - t0;
        in->reset();                 /* the cache emptied OUTSIDE the clock */
        out->replays_done = it + 1;
    }
    return total;
}
