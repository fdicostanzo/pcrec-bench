/* [B148] L4 THE CALL-STREAM TIMED REPLAY, ISOLATED (docs/design/
 * unusual_set_v1.md 7.1-7.2). A new mode is a new instrument: this
 * translation unit holds ONLY the replay loop; timed.c, the matching
 * instrument, is not touched by it (BD16). noinline + aligned(64) like
 * every timed function.
 *
 * One ITERATION is one full REPLAY of the declared call list over the one
 * subject; each replay is clocked separately and the clocks are SUMMED
 * (P6), so nothing between replays (there is nothing today; the vars memo
 * clear is lane L7's) is ever inside the clock. Each call is ONE
 * pcre2_match_8 at the call's offset over the WHOLE subject (the engine is
 * given the rest of the subject; `\G` anchors at the offset), and its answer
 * is written into the preallocated `res[]` -- integers only; the tokens are
 * spelled after the clock (calls_io.h). The ovector is read back inside the
 * loop because the next call overwrites it. */
#include <time.h>

#include "timed_calls.h"

#define PCRE2_ERROR_NOMATCH (-1)
#define PCRE2_UNSET         ((size_t)-1)

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

__attribute__((noinline, aligned(64)))
double timed_calls(const struct tcalls_in *in, struct tcalls_out *out) {
    const size_t n = in->ncalls;
    const uint32_t opts = in->opts;
    const size_t *ov = in->ov;
    struct call_res *res = in->res;
    double total = 0.0;
    for (long it = 0; it < in->iters; it++) {
        out->calls_done = 0;
        double t0 = now();
        for (size_t i = 0; i < n; i++) {
            int rc = in->match(in->code, in->buf, in->len, in->calls[i].offset,
                               opts, in->md, in->mctx);
            struct call_res *r = &res[i];
            if (rc >= 0) {
                r->kind = CALL_M;
                r->s = (long)ov[0];
                r->e = (long)ov[1];
                if (rc > 1 && ov[2] != PCRE2_UNSET) {
                    r->g1s = (long)ov[2];
                    r->g1e = (long)ov[3];
                } else {
                    r->g1s = r->g1e = -1;
                }
            } else if (rc == PCRE2_ERROR_NOMATCH) {
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
