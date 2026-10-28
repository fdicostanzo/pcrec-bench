/* [B148] L4 THE CALL-STREAM TIMED REPLAY, ISOLATED (docs/design/
 * unusual_set_v1.md 7.1-7.2). A new mode is a new instrument: this
 * translation unit holds ONLY the replay loop; timed.c, the matching
 * instrument, is not touched by it (BD16). noinline + aligned(64) like
 * every timed function.
 *
 * One ITERATION is one full REPLAY of the declared call list; each replay is
 * clocked separately and the clocks SUMMED (P6). Each call is ONE
 * `onig_search` over the WHOLE subject with `start` at the call's offset and
 * `range` at the subject's end (`\G` is the search start under Perl_NG), or,
 * under --anchor-explicit, ONE `onig_match` at the offset (7.1's O(segment)
 * fallback). The answer goes into the preallocated res[] (integers only);
 * the tokens are spelled after the clock (calls_io.h). The deep arm's limits
 * are GLOBAL setters applied by driver.c before any call (6.2), so nothing
 * here differs between the arms. */
#include <time.h>

#include "timed_calls.h"

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

__attribute__((noinline, aligned(64)))
double timed_calls(const struct tcalls_in *in, struct tcalls_out *out) {
    const size_t n = in->ncalls;
    const int anchored = in->anchored, has_g1 = in->has_g1;
    const unsigned char *buf = in->buf, *end = in->buf + in->len;
    regex_t *reg = in->reg;
    OnigRegion *region = in->region;
    struct call_res *res = in->res;
    double total = 0.0;
    for (long it = 0; it < in->iters; it++) {
        out->calls_done = 0;
        double t0 = now();
        for (size_t i = 0; i < n; i++) {
            const unsigned char *at = buf + in->calls[i].offset;
            struct call_res *r = &res[i];
            int rc = anchored
                ? onig_match(reg, buf, end, at, region, ONIG_OPTION_NONE)
                : onig_search(reg, buf, end, at, end, region, ONIG_OPTION_NONE);
            if (rc >= 0) {
                r->kind = CALL_M;
                r->s = region->beg[0];
                r->e = region->end[0];
                if (has_g1 && region->num_regs > 1) {
                    r->g1s = region->beg[1];
                    r->g1e = region->end[1];
                } else {
                    r->g1s = r->g1e = -1;
                }
            } else if (rc == ONIG_MISMATCH) {
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
