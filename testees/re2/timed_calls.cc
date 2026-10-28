// [B148] L4 THE CALL-STREAM TIMED REPLAY, ISOLATED (docs/design/
// unusual_set_v1.md 7.1-7.2). A new mode is a new instrument: this
// translation unit holds ONLY the replay loop; timed.cc is not touched
// (BD16). noinline + aligned(64) like every timed function.
//
// One ITERATION is one full REPLAY of the declared call list, clocked
// separately and SUMMED (P6). Each call is ONE RE2::Match over the WHOLE
// subject with startpos at the call's offset (RE2 has no `\G`; ANCHOR_START
// under --anchor-explicit). Only group 0 and group 1 are asked for (E-2b: the
// tokens carry no more), so the submatch work is the same on every engine.
// The answer goes into the preallocated res[]; tokens after the clock.
#include <re2/re2.h>

#include <ctime>

#include "timed_calls.h"

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

__attribute__((noinline, aligned(64)))
double timed_calls(const struct tcalls_in *in, struct tcalls_out *out) {
    const size_t n = in->ncalls;
    const int nsub = in->nsub;
    const RE2 *re = in->re;
    const RE2::Anchor anchor = in->anchor;
    absl::string_view text = in->text, *sm = in->submatch;
    struct call_res *res = in->res;
    double total = 0.0;
    for (long it = 0; it < in->iters; it++) {
        out->calls_done = 0;
        double t0 = now();
        for (size_t i = 0; i < n; i++) {
            struct call_res *r = &res[i];
            if (re->Match(text, in->calls[i].offset, text.size(), anchor, sm, nsub)) {
                r->kind = CALL_M;
                r->s = (long)(sm[0].data() - text.data());
                r->e = r->s + (long)sm[0].size();
                if (nsub > 1 && sm[1].data() != NULL) {
                    r->g1s = (long)(sm[1].data() - text.data());
                    r->g1e = r->g1s + (long)sm[1].size();
                } else {
                    r->g1s = r->g1e = -1;
                }
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
