/* [B133] THE TIMED LOOP, ISOLATED. Every instruction between the two clock
 * reads of a subject (search / find-all / whole-subject, the [B129] --prime
 * pass) is in timed_run() below and nowhere else. See testees/pcrec/timed.c's
 * header for the why ([B132]); this is the same fix for this engine: its own
 * translation unit, noinline + aligned(64), nothing else in the object. It
 * is an INSTRUMENT -- an edit here must be recorded as an instrument change
 * (docs/dev/decisions.md BD-B133). The body is the pre-[B133] loop with the
 * driver's locals turned into fields of *in / *out. */
#include <oniguruma.h>

#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "timed.h"

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

/* [B77] U1 (same rule as driver.c's --utf8 doc, kept in sync by hand). */
static inline size_t utf8_next_start(const unsigned char *b, size_t n, size_t pos) {
    size_t p = pos + 1;
    while (p < n && (b[p] & 0xC0u) == 0x80u) p++;
    return p;
}

__attribute__((noinline, aligned(64)))
double timed_run(const struct timed_in *in, struct timed_out *out) {
    const int prime = in->prime, find_all = in->find_all,
              utf8_adv = in->utf8_adv, whole_subject = in->whole_subject;
    regex_t *reg = in->reg;
    OnigRegion *region = in->region;
    double t0 = now();
    /* [B129] --prime: pass 0 (only with the flag) is the UNTIMED call; the
     * timed loop below is the original one, its bounds and body untouched. */
    for (int pass = prime ? 0 : 1; pass < 2; pass++) {
        volatile long n_it = pass ? in->iters : 1;
        if (pass && prime) t0 = now();
        for (long it = 0; it < n_it; it++) {
        out->first_s = out->first_e = -1;
        if (find_all) {
            size_t pos = 0;
            long   count = 0;
            for (;;) {
                int rc = whole_subject
                    ? onig_match(reg, in->buf, in->buf + in->len,
                                in->buf + pos, region, ONIG_OPTION_NONE)
                    : onig_search(reg, in->buf, in->buf + in->len,
                                 in->buf + pos, in->buf + in->len,
                                 region, ONIG_OPTION_NONE);
                /* KB-29 (docs/dev/known_issues.md): ALWAYS track
                 * the loop's own terminal code, not only when
                 * `count == 0` -- so a genuine give-up (any code
                 * other than ONIG_MISMATCH, the ordinary "no more
                 * matches" terminator) is never silently
                 * discarded in favour of an earlier successful
                 * match's own non-negative rc. */
                if (rc < 0) { out->rc_final = rc; break; }
                if (out->first_s < 0) {
                    out->first_s = (long)region->beg[0];
                    out->first_e = (long)region->end[0];
                    out->rc_final = rc;
                }
                count++;
                /* pcrec match_api.md S3.1's find-all advance: off the
                 * match's own reported START, never off the scan
                 * position -- KB-17, the same rule testees/pcre2/
                 * driver.c applies. Under --utf8 ([B77] U1): the
                 * next CHARACTER boundary, not start + 1. */
                size_t start = (size_t)region->beg[0];
                size_t end = (size_t)region->end[0];
                pos = (end > start) ? end
                    : utf8_adv ? utf8_next_start(in->buf, in->len, start)
                               : start + 1;
                if (whole_subject) break; /* onig_match: one position only */
                if (pos > in->len) break;
            }
            out->nmatch = count;
            /* KB-29: a genuine mid-loop give-up (any terminal
             * code other than ONIG_MISMATCH) must propagate as
             * the whole subject's give-up, discarding any
             * matches already accumulated this call -- falls
             * through to the ordinary `giveup:<code>:<message>`
             * branch below exactly as a first-call give-up
             * already does. */
            if (out->rc_final < 0 && out->rc_final != ONIG_MISMATCH) {
                out->first_s = out->first_e = -1;
                out->nmatch = -1;
            }
        } else {
            int rc = whole_subject
                ? onig_match(reg, in->buf, in->buf + in->len, in->buf,
                            region, ONIG_OPTION_NONE)
                : onig_search(reg, in->buf, in->buf + in->len, in->buf,
                             in->buf + in->len, region, ONIG_OPTION_NONE);
            out->rc_final = rc;
            if (rc >= 0) {
                out->first_s = (long)region->beg[0];
                out->first_e = (long)region->end[0];
            }
        }
        }
    }
    return now() - t0;
}
