/* [B133] THE TIMED LOOP, ISOLATED. Every instruction between the two clock
 * reads of a subject (find-all and single-call modes, interpreter / JIT /
 * DFA, the [B129] --prime pass, the [B94] validate-once rule) is in
 * timed_run() below and nowhere else. See testees/pcrec/timed.c's header for
 * the full why ([B132]: stamp-getter lines added to a driver's main() moved
 * the timed loop it contained by +10-17% on short calls); this file is the
 * same fix for this engine: its own translation unit, noinline +
 * aligned(64), nothing else in the object. It is an INSTRUMENT -- an edit
 * here must be recorded as an instrument change (docs/dev/decisions.md
 * BD-B133). The body is the pre-[B133] loop with the driver's locals turned
 * into fields of *in / *out. */
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "timed.h"

#define PCRE2_ERROR_NOMATCH   (-1)
#define PCRE2_UTF             0x00080000u
#define PCRE2_NO_UTF_CHECK    0x40000000u

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

/* ONE call site for both matchers ([B42] L6a). */
static inline int do_match(const struct timed_in *in, const unsigned char *buf,
                           size_t len, size_t pos, uint32_t opts) {
    if (in->dfa)
        return in->dfa_match(in->code, buf, len, pos, opts, in->md, NULL,
                             in->dfa_ws, in->dfa_ws_n);
    return in->match(in->code, buf, len, pos, opts, in->md, NULL);
}

__attribute__((noinline, aligned(64)))
double timed_run(const struct timed_in *in, struct timed_out *out) {
    const int prime = in->prime, find_all = in->find_all, dfa = in->dfa,
              utf8_adv = in->utf8_adv, utf_always_check = in->utf_always_check;
    const uint32_t opts = in->opts, copts = in->copts, ovn = in->ovn;
    const size_t *ov = in->ov;
    size_t *firstov = in->firstov;
    void (*die)(const char *) = in->die;
    double t0 = now();
    /* [B129] --prime: pass 0 (only with the flag) is the UNTIMED call; the
     * timed loop below is the original one, its bounds and body untouched. */
    for (int pass = prime ? 0 : 1; pass < 2; pass++) {
        volatile long n_it = pass ? in->iters : 1;
        if (pass && prime) t0 = now();
        for (long it = 0; it < n_it; it++) {
        out->first_s = out->first_e = -1;
        out->npairs = 0;
        if (find_all) {
            size_t pos = 0;
            long   count = 0;
            /* [B94]/BD15: VALIDATE-ONCE. `utf_once` is true only
             * under PCRE2_UTF and only when the control has not
             * disabled it; `validated` tracks whether call 1 (offset
             * 0, always without the flag) has completed. See this
             * file's header comment for the full rule and its man
             * pcre2api citations. */
            int utf_once = (copts & PCRE2_UTF) && !utf_always_check;
            int validated = 0;
            for (;;) {
                uint32_t call_opts = opts;
                if (utf_once && validated) {
                    /* NEVER trusted silently: assert pos is a
                     * character boundary before passing the flag --
                     * the same discipline oracle_pcre2.py's
                     * `_find_all_impl` uses (an AssertionError there,
                     * a loud die() here). A continuation byte here
                     * would mean --utf8's advance rule broke, not
                     * that this control should look away. */
                    if (pos < in->len && (in->buf[pos] & 0xC0u) == 0x80u)
                        die("validate-once: find-all start offset is "
                            "not a character boundary -- refusing to "
                            "pass PCRE2_NO_UTF_CHECK");
                    call_opts |= PCRE2_NO_UTF_CHECK;
                }
                int rc = do_match(in, in->buf, in->len, pos,
                                  call_opts);
                /* Call 1 (pos == 0) just RAN: whether it matched,
                 * found no match, or gave up on something other than
                 * UTF validity, libpcre2 has by now checked the
                 * whole subject from offset 0 to its end (this
                 * file's header comment). A call that genuinely
                 * failed UTF validation is reported below through
                 * the ordinary `giveup:<code>:<message>` protocol
                 * and the loop breaks (rc < 0) before any call 2
                 * happens, so marking `validated` here is never
                 * reached by an unvalidated subject in practice. */
                if (utf_once && pos == 0 && !validated) validated = 1;
                /* KB-29 (docs/dev/known_issues.md): `out->rc_final` is
                 * now ALWAYS the loop's own terminal code -- not
                 * only when `count == 0` -- so a genuine give-up
                 * AFTER at least one match is never silently
                 * discarded in favour of the LAST successful
                 * match's own (non-negative) `rc`. */
                if (rc < 0) { out->rc_final = rc; break; }
                if (out->first_s < 0) {
                    out->first_s = (long)ov[0];
                    out->first_e = (long)ov[1];
                    /* DFA: `rc` is the SIMULTANEOUS-match count at
                     * this start point, not a capture-pair count
                     * (man pcre2_dfa_match item 2: "no captured
                     * substrings are available") -- forced to 0,
                     * never read as if it were one. */
                    out->npairs = dfa ? 0 : (uint32_t)(rc > 0 ? rc : 1);
                    if (out->npairs > ovn) out->npairs = ovn;
                    if (out->npairs > 256) out->npairs = 256;
                    memcpy(firstov, ov, (size_t)out->npairs * 2 * sizeof *ov);
                    out->rc_final = rc;
                }
                count++;
                /* pcrec match_api.md S3.1's find-all advance: off the
                 * match's own reported START (ov[0]), never off the
                 * scan position -- an empty match can be found AHEAD
                 * of pos, and advancing pos itself re-finds the same
                 * empty match next call (KB-17). Byte encoding: the
                 * S3.1.1 `next_pos` residual is start+1; under
                 * --utf8 ([B77] U1) it is the next CHARACTER
                 * boundary -- a mid-character start offset under
                 * PCRE2_UTF is PCRE2_ERROR_BADUTFOFFSET. */
                size_t start = ov[0];
                size_t end = ov[1];
                pos = (end > start) ? end
                    : utf8_adv ? utf8_next_start(in->buf, in->len, start)
                               : start + 1;
                if (pos > in->len) break;
            }
            out->nmatch = count;
            /* KB-29: a MID-loop give-up (any negative terminal
             * code OTHER than PCRE2_ERROR_NOMATCH, which is the
             * ORDINARY "no further matches" termination every
             * find-all call ends on) must propagate as the whole
             * subject's give-up, with its own code -- never
             * silently absorbed into a truncated "match" answer
             * just because count > 0 by the time the engine gave
             * up. Discarding the partial match/count here is what
             * makes the classification below (`out->first_s >= 0` ->
             * "match") fall through correctly to the SAME
             * `giveup:<code>:<message>` branch a first-call
             * give-up already takes. */
            if (out->rc_final < 0 && out->rc_final != PCRE2_ERROR_NOMATCH) {
                out->first_s = out->first_e = -1;
                out->npairs = 0;
                out->nmatch = -1;
            }
        } else {
            int rc = do_match(in, in->buf, in->len, 0, opts);
            out->rc_final = rc;
            if (rc >= 0) {
                out->first_s = (long)ov[0];
                out->first_e = (long)ov[1];
                out->npairs = dfa ? 0 : (uint32_t)(rc > 0 ? rc : 1);
                if (out->npairs > ovn) out->npairs = ovn;
                if (out->npairs > 256) out->npairs = 256;
                memcpy(firstov, ov, (size_t)out->npairs * 2 * sizeof *ov);
            }
        }
        }
    }
    return now() - t0;
}
