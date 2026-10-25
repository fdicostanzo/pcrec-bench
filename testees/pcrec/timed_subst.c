/* [B140] THE SUBSTITUTION TIMED CALL, ISOLATED (pcrec). Every instruction
 * between the two clock reads of a `--mode subst` subject is in
 * timed_subst() below and nowhere else. Same discipline as timed.c and
 * testees/pcre2/timed_subst.c (BD16, docs/dev/decisions.md): its own
 * translation unit, noinline + aligned(64), nothing else in the object, the
 * driver passes in the already-resolved entry point.
 *
 * WHY A SECOND FILE AND NOT A SECOND FUNCTION IN timed.c. timed.c is the
 * INSTRUMENT every pcrec matching cell in the store was measured with; BD16
 * (2) makes ANY edit to it an instrument change needing a re-pin-control
 * run, and this lane may not run timing. A new mode needs a new timed
 * function, not a changed old one, so it lives in a NEW file and timed.c
 * stays byte-identical (proved in docs/dev/measurements/
 * 2026-10-25-b140pcrec-instrument-additivity.txt).
 *
 * WHAT IS TIMED (docs/design/subst_bench_v1.md 3.1, 3.1.1). The called
 * function is subst_shim.c's pb_subst_all: the contract's own setup wrapper
 * (subst_api.md 6.9: iterator init, the context setup and its check, then
 * pcrec_subst_replace_all) -- the code a user writes once, so its setup is
 * part of the call and is in the clock.
 *   bound arm      ONE call into the caller's pre-sized, pre-faulted
 *                  buffer. A too-small buffer is NOSPACE (-11), reported by
 *                  the driver as a failure, never retried here.
 *   size-first arm TWO calls: out == NULL, cap == 0 (the size pass, 10.7:
 *                  the whole find-all runs and renders its pieces once),
 *                  then the real call into the arena with cap = the length
 *                  the first call returned -- the contract's NOSPACE-free
 *                  path. The arena is sized and faulted before the clock, so
 *                  allocation is in neither arm; the arms differ by the
 *                  second find-all only.
 * iters is 1 in this bench; the loop is kept so the field means what it says.
 */
#include <stddef.h>
#include <stdint.h>
#include <time.h>

#include "timed_subst.h"

#define TSUBST_ERR_ARENA (-1000)   /* size-first: needed > the arena */

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

__attribute__((noinline, aligned(64)))
double timed_subst(const struct psubst_in *in, struct psubst_out *out) {
    const int size_first = in->size_first;
    const long iters = in->iters;
    int rc = 0;
    size_t outlen = 0;
    double t0 = now();
    for (long it = 0; it < iters; it++) {
        size_t cap = in->cap;
        if (size_first) {
            outlen = 0;
            rc = in->subst_all(in->buf, in->len, NULL, 0, &outlen);
            if (rc < 0) break;
            if (outlen > in->cap) { rc = TSUBST_ERR_ARENA; break; }
            cap = outlen;
        }
        outlen = 0;
        rc = in->subst_all(in->buf, in->len, in->out, cap, &outlen);
    }
    double t1 = now();
    out->rc = rc;
    out->outlen = outlen;
    return t1 - t0;
}
