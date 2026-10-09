/* [B133] THE TIMED LOOP, ISOLATED. Every instruction between the two clock
 * reads of a subject -- all three modes (search, find-all, whole-subject
 * match), the [B129] --prime pass, the caller-provided-buffer variants -- is
 * in timed_run() below and nowhere else.
 *
 * WHY: [B132] measured that growing driver.c's main() by 37 stamp-getter
 * lines moved short-call timings +10-17% (~40-50 ns/call) on program-
 * identical cells, because the timed loop used to live inside main().
 * This file is a translation unit of its own, compiled and linked beside
 * driver.c, and holds ONLY the timed function (+ the one helper it calls),
 * so no driver/shim/stamp edit can change its code generation or its address
 * modulo 64: noinline + aligned(64) fix the function's own start, and being
 * the only function in its object, the object's .text layout cannot shift
 * under it. It is an INSTRUMENT: editing this file moves every record's
 * numbers, and the edit must say so (docs/dev/decisions.md BD-B133; records
 * before/after are told apart by run.harness_commit). Do NOT add anything
 * to this file that is not the timed loop; the info getters stay in
 * driver.c (they are not timed).
 *
 * The body is the pre-[B133] loop byte for byte except that the driver's
 * locals became fields of *in / *out (the volatile outputs stay volatile so
 * the sigsetjmp/longjmp timeout path in driver.c reads them as before). */
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "timed.h"

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

/* [B77] U1; same rule as driver.c's --utf8 doc (kept in sync by hand: it is
 * three lines and part of the timed find-all loop). */
static inline size_t utf8_next_start(const unsigned char *b, size_t n, size_t pos) {
    size_t p = pos + 1;
    while (p < n && (b[p] & 0xC0u) == 0x80u) p++;
    return p;
}

#define do_search(s, n, pos, caps) \
    (in->use_buffers \
        ? in->search_in(s, n, pos, caps, in->buf_frames, in->buf_nframes, \
                        in->buf_trail, in->buf_ntrail) \
        : in->search(s, n, pos, caps))
#define do_match_caps(s, n, pos, caps) \
    (in->use_buffers \
        ? in->match_caps_in(s, n, pos, caps, in->buf_frames, in->buf_nframes, \
                            in->buf_trail, in->buf_ntrail) \
        : in->match_caps(s, n, pos, caps))

__attribute__((noinline, aligned(64)))
double timed_run(const struct timed_in *in, struct timed_out *out) {
    const int prime = in->prime, anchored = in->anchored,
              find_all = in->find_all, utf8_adv = in->utf8_adv,
              ncaps = in->ncaps;
    ptrdiff_t (*caps)[2] = in->caps;
    ptrdiff_t (*firstcaps)[2] = in->firstcaps;
        double t0 = now();
        /* [B129] --prime: pass 0 (only with the flag) is the UNTIMED call; the
         * timed loop below is the original one, its bounds and body untouched. */
        for (int pass = prime ? 0 : 1; pass < 2; pass++) {
            volatile long n_it = pass ? in->iters : 1;
            if (pass && prime) t0 = now();
            for (long it = 0; it < n_it; it++) {
            out->first_s = out->first_e = -1;
            out->giveup = 0;
            if (anchored) {
                /* whole-subject: anchored at 0 AND ending at n. See
                 * shim.c's pb_match_caps comment for the asymmetry this
                 * carries against PCRE2_ENDANCHORED. */
                long long r = do_match_caps(in->buf, in->len, 0, caps);
                if (r < 0) {
                    if (r < -1) out->giveup = (int)r;
                } else if ((size_t)r == in->len) {
                    out->first_s = 0;
                    out->first_e = (long)r;
                    memcpy(firstcaps, caps, (size_t)ncaps * sizeof *caps);
                }
            } else if (find_all) {
                size_t pos = 0;
                long count = 0;
                for (;;) {
                    int r = do_search(in->buf, in->len, pos, caps);
                    if (r == 0) break;
                    /* KB-29 (docs/dev/known_issues.md): ALWAYS track a
                     * genuine give-up (r < 0 is never "no more matches"
                     * on this engine -- r == 0 already owns that,
                     * above), not only when `count == 0`, so a
                     * mid-loop give-up after count > 0 is never
                     * silently discarded in favour of the last
                     * successful match. */
                    if (r < 0) { out->giveup = r; break; }
                    if (out->first_s < 0) {
                        out->first_s = (long)caps[0][0];
                        out->first_e = (long)caps[0][1];
                        memcpy(firstcaps, caps, (size_t)ncaps * sizeof *caps);
                    }
                    count++;
                    /* pcrec match_api.md S3.1's find-all advance: off the
                     * match's own reported START (caps[0][0]), never off
                     * the scan position -- an empty match can be found
                     * AHEAD of pos, and advancing pos itself re-finds the
                     * same empty match next call (KB-17). Byte encoding:
                     * S3.1.1's `<prefix>_next_pos` residual is start+1
                     * (every position is a character boundary). Under
                     * --utf8 ([B77] U1) the next CHARACTER boundary --
                     * the rule a `-e utf8` artifact's own
                     * `<prefix>_next_pos` implements (S3.1.1), coded
                     * here once for every engine rather than called. */
                    size_t start = (size_t)caps[0][0];
                    size_t end = (size_t)caps[0][1];
                    pos = (end > start) ? end
                        : utf8_adv ? utf8_next_start(in->buf, in->len, start)
                                   : start + 1;
                    if (pos > in->len) break;
                }
                out->nmatch = count;
                /* KB-29: a genuine mid-loop give-up (any nonzero
                 * `out->giveup`) must propagate as the WHOLE subject's
                 * give-up, discarding any matches already
                 * accumulated this call -- the same reason
                 * `out->first_s`/`out->nmatch` are reset in testees/pcre2/
                 * driver.c's own fix. Falls through to the ordinary
                 * `out->giveup:<code>:<NAME>` branch below exactly as a
                 * first-call give-up already does. */
                if (out->giveup) { out->first_s = out->first_e = -1; out->nmatch = -1; }
            } else {
                int r = do_search(in->buf, in->len, 0, caps);
                if (r == 1) {
                    out->first_s = (long)caps[0][0];
                    out->first_e = (long)caps[0][1];
                    memcpy(firstcaps, caps, (size_t)ncaps * sizeof *caps);
                } else if (r < 0) {
                    out->giveup = r;
                }
            }
            }
        }
    return now() - t0;
}
