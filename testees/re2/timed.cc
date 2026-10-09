// [B133] THE TIMED LOOP, ISOLATED. Every instruction between the two clock
// reads of a subject (search / find-all / whole-subject, the [B129] --prime
// pass) is in timed_run() below and nowhere else. See
// testees/pcrec/timed.c's header for the why ([B132]); the same fix for this
// engine: its own translation unit, noinline + aligned(64), nothing else in
// the object. It is an INSTRUMENT -- an edit here must be recorded as an
// instrument change (docs/dev/decisions.md BD16). The body is the
// pre-[B133] loop with the driver's locals turned into fields of *in / *out.
#include <re2/re2.h>

#include <cstddef>
#include <cstdlib>
#include <ctime>

#include "timed.h"

using absl::string_view;

static inline double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

// [B77] U1 (same rule as driver.cc's --utf8 doc, kept in sync by hand).
static inline size_t utf8_next_start(const unsigned char *b, size_t n, size_t pos) {
    size_t p = pos + 1;
    while (p < n && (b[p] & 0xC0u) == 0x80u) p++;
    return p;
}

__attribute__((noinline, aligned(64)))
double timed_run(const struct timed_in *in, struct timed_out *out) {
    const int prime = in->prime, find_all = in->find_all,
              utf8_adv = in->utf8_adv, nsub = in->nsub;
    const RE2 *re = in->re;
    const RE2::Anchor anchor = in->anchor;
    string_view *submatch = in->submatch;
    string_view text = in->text;
    double t0 = now();
    /* [B129] --prime: pass 0 (only with the flag) is the UNTIMED call; the
     * timed loop below is the original one, its bounds and body untouched. */
    for (int pass = prime ? 0 : 1; pass < 2; pass++) {
        volatile long n_it = pass ? in->iters : 1;
        if (pass && prime) t0 = now();
        for (long it = 0; it < n_it; it++) {
        out->first_s = out->first_e = -1;
        out->nsub_out = 0;
        if (find_all) {
            size_t pos = 0;
            long count = 0;
            for (;;) {
                if (pos > text.size()) break;
                bool m = re->Match(text, pos, text.size(),
                                  RE2::UNANCHORED, submatch,
                                  nsub);
                if (!m) break;
                size_t start = (size_t)(submatch[0].data() - text.data());
                size_t end = start + submatch[0].size();
                if (out->first_s < 0) {
                    out->first_s = (long)start;
                    out->first_e = (long)end;
                    out->nsub_out = nsub;
                    out->matched_final = 1;
                }
                count++;
                // pcrec match_api.md S3.1's find-all advance rule
                // (adopted by reference, KB-17, testees/pcre2/
                // driver.c's own comment): off the match's own
                // reported START, never off the scan position.
                // Under --utf8 ([B77] U1): the next CHARACTER
                // boundary, not start + 1.
                pos = (end > start) ? end
                    : utf8_adv ? utf8_next_start(
                          reinterpret_cast<const unsigned char *>(text.data()),
                          text.size(), start)
                               : start + 1;
            }
            out->nmatch = count;
            out->matched_final = (count > 0);
        } else {
            bool m = re->Match(text, 0, text.size(), anchor,
                              submatch, nsub);
            out->matched_final = m ? 1 : 0;
            if (m) {
                out->first_s = (long)(submatch[0].data() - text.data());
                out->first_e = out->first_s + (long)submatch[0].size();
                out->nsub_out = nsub;
            }
        }
        }
    }
    return now() - t0;
}
