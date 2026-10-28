/* [B148] L7 THE VARS CALL-STREAM TIMED REPLAY, ISOLATED (docs/design/
 * unusual_set_v1.md 3.3, 7.1-7.2). A new mode is a new instrument: this
 * translation unit holds ONLY the vars replay loop; timed.c and
 * timed_calls.c are not touched by it (BD16). noinline + aligned(64) like
 * every timed function.
 *
 * One ITERATION is one full REPLAY of the declared call list, each replay
 * clocked separately and the clocks SUMMED (P6). Each call is ONE
 * `<prefix>_search` on the call's LINE alone -- (buf + offset, length), start
 * 0, so `^` is the line's start and result offsets are line-relative -- with
 * the call's binding (its variable array, built once outside the clock). The
 * artifact resolves its mentioned names against that array itself, once per
 * call (vars.md 3): that resolution is pcrec's per-call cost and is INSIDE the
 * clock. PCREC_ERR_UNSET_VAR is a REFUSED call (vars.md 5: nothing was
 * attempted), tokenized `r`; any other negative code is a give-up. */
#include <time.h>

#include "timed_calls_vars.h"

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

__attribute__((noinline, aligned(64)))
double timed_calls_vars(const struct tvars_in *in, struct tcalls_out *out) {
    const size_t n = in->ncalls;
    const int has_g1 = in->has_g1, use_buffers = in->use_buffers,
              unset_code = in->unset_code;
    ptrdiff_t (*caps)[2] = in->caps;
    struct call_res *res = in->res;
    double total = 0.0;
    for (long it = 0; it < in->iters; it++) {
        out->calls_done = 0;
        double t0 = now();
        for (size_t i = 0; i < n; i++) {
            const struct vcall_decl *c = &in->calls[i];
            const struct vbinding *b = &in->bindings[c->binding];
            struct call_res *r = &res[i];
            const unsigned char *line = in->buf + c->offset;
            int rc = use_buffers
                ? in->search_in(line, c->length, 0, caps, b->vars, b->nvars,
                                in->buf_frames, in->buf_nframes,
                                in->buf_trail, in->buf_ntrail)
                : in->search(line, c->length, 0, caps, b->vars, b->nvars);
            if (rc == 1) {
                r->kind = CALL_M;
                r->s = (long)caps[0][0];
                r->e = (long)caps[0][1];
                if (has_g1) { r->g1s = (long)caps[1][0]; r->g1e = (long)caps[1][1]; }
                else r->g1s = r->g1e = -1;
            } else if (rc == 0) {
                r->kind = CALL_N;
            } else if (rc == unset_code) {
                r->kind = CALL_R;
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
