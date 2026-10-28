/* [B148] L4 THE CALL-STREAM TIMED REPLAY, ISOLATED (docs/design/
 * unusual_set_v1.md 7.1-7.2). A new mode is a new instrument: this
 * translation unit holds ONLY the replay loop; timed.c, the matching
 * instrument, is not touched by it (BD16). noinline + aligned(64) like
 * every timed function.
 *
 * One ITERATION is one full REPLAY of the declared call list; each replay is
 * clocked separately and the clocks SUMMED (P6). Each call is ONE
 * `<prefix>_search` (or `_search_in` with the caller buffer) at the call's
 * offset over the WHOLE subject -- the artifact's own `\G` anchors there --
 * or, under --anchor-explicit, ONE `<prefix>_match_caps` at the offset (an
 * anchored-at-start call that returns the match LENGTH; timed.c's `match` mode
 * uses it with offset 0). Its answer goes into the preallocated res[]
 * (integers only); the tokens are spelled after the clock (calls_io.h). */
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
    const int anchored = in->anchored, has_g1 = in->has_g1,
              use_buffers = in->use_buffers;
    ptrdiff_t (*caps)[2] = in->caps;
    struct call_res *res = in->res;
    double total = 0.0;
    for (long it = 0; it < in->iters; it++) {
        out->calls_done = 0;
        double t0 = now();
        for (size_t i = 0; i < n; i++) {
            const size_t off = in->calls[i].offset;
            struct call_res *r = &res[i];
            long long rc;
            if (anchored) {
                rc = use_buffers
                    ? in->match_caps_in(in->buf, in->len, off, caps,
                                        in->buf_frames, in->buf_nframes,
                                        in->buf_trail, in->buf_ntrail)
                    : in->match_caps(in->buf, in->len, off, caps);
                if (rc >= 0) {
                    r->kind = CALL_M;
                    r->s = (long)off;
                    r->e = (long)(off + (size_t)rc);   /* rc = the LENGTH (shim.c) */
                } else if (rc == -1) {
                    r->kind = CALL_N;
                } else {
                    r->kind = CALL_G;
                    r->code = (int)rc;
                }
            } else {
                rc = use_buffers
                    ? in->search_in(in->buf, in->len, off, caps,
                                    in->buf_frames, in->buf_nframes,
                                    in->buf_trail, in->buf_ntrail)
                    : in->search(in->buf, in->len, off, caps);
                if (rc == 1) {
                    r->kind = CALL_M;
                    r->s = (long)caps[0][0];
                    r->e = (long)caps[0][1];
                } else if (rc == 0) {
                    r->kind = CALL_N;
                } else {
                    r->kind = CALL_G;
                    r->code = (int)rc;
                }
            }
            if (r->kind == CALL_M) {
                if (has_g1) { r->g1s = (long)caps[1][0]; r->g1e = (long)caps[1][1]; }
                else r->g1s = r->g1e = -1;
            }
            out->calls_done = i + 1;
        }
        total += now() - t0;
        out->replays_done = it + 1;
    }
    return total;
}
