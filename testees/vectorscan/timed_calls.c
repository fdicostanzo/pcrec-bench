/* [B148] L4 THE CALL-STREAM TIMED REPLAY, ISOLATED (docs/design/
 * unusual_set_v1.md 7.1-7.2). A new mode is a new instrument: this
 * translation unit holds ONLY the replay loop and its callback; timed.c is
 * not touched (BD16). noinline + aligned(64) like every timed function.
 * `vectorscan-block-som` only (the driver refuses --mode calls without
 * --som by name: a boolean-grain engine has no span token to give).
 *
 * One ITERATION is one full REPLAY of the declared call list, clocked
 * separately and SUMMED (P6). Each call is ONE hs_scan over the subject's
 * REST from the call's offset (block mode has no start offset into a larger
 * buffer, so the slice IS the call; bytes before the offset are not context
 * -- a pattern with lookbehind or `\b` at the offset could differ, stated in
 * testees/vectorscan/CLAUDE.md). The callback never stops early and keeps,
 * online, the driver's own SOM reduction (driver.c header, "SOM MODE" (1)):
 * the minimum `from`, then the maximum `to` at that `from` -- leftmost, then
 * longest. Offsets are slice-relative and shifted by the call's offset after
 * the scan. Hyperscan has no capture groups: group 0 only. */
#include <time.h>

#include "timed_calls.h"

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

typedef struct {
    int any;
    unsigned long long from, to;
} span_ctx;

static int HS_CDECL on_match_span(unsigned int id, unsigned long long from,
                                  unsigned long long to, unsigned int flags,
                                  void *context) {
    (void)id; (void)flags;
    span_ctx *c = (span_ctx *)context;
    if (!c->any || from < c->from) {
        c->any = 1;
        c->from = from;
        c->to = to;
    } else if (from == c->from && to > c->to) {
        c->to = to;
    }
    return 0;
}

__attribute__((noinline, aligned(64)))
double timed_calls(const struct tcalls_in *in, struct tcalls_out *out) {
    const size_t n = in->ncalls;
    hs_database_t *db = in->db;
    hs_scratch_t *scratch = in->scratch;
    struct call_res *res = in->res;
    double total = 0.0;
    for (long it = 0; it < in->iters; it++) {
        out->calls_done = 0;
        double t0 = now();
        for (size_t i = 0; i < n; i++) {
            const size_t off = in->calls[i].offset;
            struct call_res *r = &res[i];
            span_ctx c = { 0, 0, 0 };
            hs_error_t rc = hs_scan(db, (const char *)in->buf + off,
                                    (unsigned int)(in->len - off), 0, scratch,
                                    on_match_span, &c);
            if (rc != HS_SUCCESS) {
                r->kind = CALL_G;
                r->code = (int)rc;
            } else if (c.any) {
                r->kind = CALL_M;
                r->s = (long)(off + c.from);
                r->e = (long)(off + c.to);
                r->g1s = r->g1e = -1;
            } else {
                r->kind = CALL_N;
            }
            out->calls_done = i + 1;
        }
        total += now() - t0;
        out->replays_done = it + 1;
    }
    return total;
}
