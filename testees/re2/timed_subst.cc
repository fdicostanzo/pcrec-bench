// [B140] THE SUBSTITUTION TIMED CALL, ISOLATED. Every instruction between the
// two clock reads of a `--mode subst` subject is in timed_subst() below and
// nowhere else. Same discipline as timed.cc (BD16, docs/dev/decisions.md): its
// own translation unit, noinline + aligned(64), nothing else in the object.
//
// WHY A SECOND FILE AND NOT A SECOND FUNCTION IN timed.cc. timed.cc is the
// INSTRUMENT every RE2 matching cell in the store was measured with; BD16 (2)
// makes any edit to it an instrument change needing a re-pin-control timing
// run, and this lane may not run timing. A new mode needs a new timed
// function, not a changed old one. timed.cc / timed.h are byte-identical
// (docs/dev/measurements/2026-10-25-b140drv2-instrument-additivity.txt).
//
// WHAT IS TIMED (docs/design/subst_bench_v1.md 3.1): ONE
// RE2::GlobalReplace(std::string*, const RE2&, rewrite). It edits the
// string IN PLACE, so the driver hands in a fresh copy of the subject made
// OUTSIDE the clock (and a `std::string` copy is ~0.1 s per 320 MB, none of
// it timed). iters is 1 in this bench (3.1.2); there is no loop to put a
// second copy inside.
#include <re2/re2.h>

#include <ctime>

#include "timed_subst.h"

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

__attribute__((noinline, aligned(64)))
double timed_subst(const struct tsubst_in *in, struct tsubst_out *out) {
    double t0 = now();
    int n = RE2::GlobalReplace(in->text, *in->re, in->rewrite);
    double t1 = now();
    out->nsubst = n;
    return t1 - t0;
}
