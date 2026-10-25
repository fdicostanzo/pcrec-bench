/* [B140] THE SUBSTITUTION TIMED CALL, ISOLATED. Every instruction between the
 * two clock reads of a `--mode subst` subject is in timed_subst() below and
 * nowhere else. Same discipline as timed.c (BD16, docs/dev/decisions.md):
 * its own translation unit, noinline + aligned(64), nothing else in the
 * object, the driver passes in already-resolved entry points.
 *
 * WHY A SECOND FILE AND NOT A SECOND FUNCTION IN timed.c. timed.c is the
 * INSTRUMENT every pcre2 matching cell in the store was measured with; BD16
 * (2) makes ANY edit to it an instrument change needing a re-pin-control
 * run, and this lane may not run timing. A new mode needs a new timed
 * function, not a changed old one, so it lives in a NEW file and timed.c
 * stays byte-identical (proved in docs/dev/lanes/b140drv_report.md:
 * timed_run's disassembly and alignment are the same in the old and the new
 * driver). `driverrun.build_driver(extra_sources=...)` links this file.
 *
 * WHAT IS TIMED (docs/design/subst_bench_v1.md 3.1, 3.1.1).
 *   bound arm      ONE pcre2_substitute call into the caller's pre-sized,
 *                  pre-faulted buffer. No NOSPACE retry exists in here: the
 *                  libpcre2 retry re-matches (contract 9 #7) and would be a
 *                  timing artifact; a too-small buffer is rc == -48, reported
 *                  by the driver as a failure, never retried.
 *   size-first arm TWO calls: the first with PCRE2_SUBSTITUTE_OVERFLOW_LENGTH
 *                  and a zero-length output (libpcre2 matches the whole
 *                  subject to learn the size and returns NOMEMORY with the
 *                  needed length), then the real call into the arena. This is
 *                  the "analogue of pcrec's size-then-render" the charter
 *                  names: its cost IS the second search. The arena is sized
 *                  and faulted before the clock, so allocation is in neither
 *                  arm (the arms differ by the matching work, not by malloc).
 * iters is 1 in this bench; the loop is kept so the field means what it says.
 */
#include <stddef.h>
#include <stdint.h>
#include <time.h>

#include "timed_subst.h"

#define PCRE2_ERROR_NOMEMORY            (-48)
#define PCRE2_SUBSTITUTE_OVERFLOW_LENGTH 0x00001000u
#define TSUBST_ERR_ARENA                (-1000)   /* size-first: needed > cap */

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

__attribute__((noinline, aligned(64)))
double timed_subst(const struct tsubst_in *in, struct tsubst_out *out) {
    const int size_first = in->size_first;
    const long iters = in->iters;
    int rc = 0;
    size_t outlen = 0;
    double t0 = now();
    for (long it = 0; it < iters; it++) {
        if (size_first) {
            outlen = 0;
            rc = in->subst(in->code, in->buf, in->len, 0,
                           in->opts | PCRE2_SUBSTITUTE_OVERFLOW_LENGTH,
                           in->md, NULL, in->repl, in->repl_len,
                           in->out, &outlen);
            if (rc != PCRE2_ERROR_NOMEMORY) break;     /* an error, or empty */
            if (outlen > in->cap) { rc = TSUBST_ERR_ARENA; break; }
        }
        outlen = in->cap;
        rc = in->subst(in->code, in->buf, in->len, 0, in->opts, in->md, NULL,
                       in->repl, in->repl_len, in->out, &outlen);
    }
    double t1 = now();
    out->rc = rc;
    out->outlen = outlen;
    return t1 - t0;
}
