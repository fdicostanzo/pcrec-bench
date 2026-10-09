/* [B133] THE TIMED LOOP, ISOLATED. Every instruction between the two clock
 * reads of a subject (search / find-all / whole-subject, the [B129] --prime
 * pass; the first match's captures rendering, emit_caps(), is part of the
 * loop and so lives here) is in timed_run() below and nowhere else. See
 * testees/pcrec/timed.c's header for the why ([B132]); the same fix for this
 * engine: its own translation unit, noinline + aligned(64), nothing else in
 * the object. It is an INSTRUMENT -- an edit here must be recorded as an
 * instrument change (docs/dev/decisions.md BD16). The body is the
 * pre-[B133] loop with the driver's locals turned into fields of *in / *out. */
#include <tre/tre.h>

#include <stdio.h>
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

static void emit_caps(regmatch_t *pmatch, size_t nmatch, char *out,
                      size_t outcap) {
    size_t off = 0;
    out[0] = 0;
    for (size_t i = 1; i < nmatch; i++) {
        long s = (pmatch[i].rm_so < 0) ? -1 : (long)pmatch[i].rm_so;
        long e = (pmatch[i].rm_eo < 0) ? -1 : (long)pmatch[i].rm_eo;
        int k = snprintf(out + off, outcap - off, "%s%ld:%ld",
                         i > 1 ? "," : "", s, e);
        if (k < 0 || (size_t)k >= outcap - off) break;
        off += (size_t)k;
    }
    if (!out[0]) { out[0] = '-'; out[1] = 0; }
}

__attribute__((noinline, aligned(64)))
double timed_run(const struct timed_in *in, struct timed_out *out) {
    const int prime = in->prime, find_all = in->find_all,
              utf8_adv = in->utf8_adv, whole_subject = in->whole_subject;
    regex_t *re_p = in->re;
#define re (*re_p)
    const size_t nmatch_cap = in->nmatch_cap;
    regmatch_t *pmatch = in->pmatch;
    char *caps_final = in->caps_final;
    const size_t caps_final_cap = in->caps_final_cap;
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
                int eflags = (pos > 0) ? REG_NOTBOL : 0;
                int rc = tre_regnexecb(&re, (const char *)in->buf + pos,
                                       in->len - pos, nmatch_cap,
                                       pmatch, eflags);
                /* KB-29 (docs/dev/known_issues.md): out->rc_final is now
                 * ALWAYS the loop's own terminal code -- not only
                 * when count == 0 -- so a genuine give-up (any code
                 * other than REG_OK/REG_NOMATCH) AFTER at least one
                 * match is never silently discarded in favour of
                 * the LAST successful match's own REG_OK. Mirrors
                 * testees/{pcre2,onig,pcrec}/driver.c's own fix
                 * exactly. See this driver's own reachability note
                 * below: on the pinned libtre build, tre_regnexecb
                 * is EMPIRICALLY shown to make zero heap
                 * allocations for any pattern/subject this project
                 * could construct (docs/dev/measurements/2026-09-26-
                 * kb29-tre-giveup-reachability.txt), so REG_ESPACE
                 * -- the only code besides REG_OK/REG_NOMATCH TRE's
                 * own source can return from an exec call -- has
                 * never been observed to fire here; this fix is
                 * therefore DEFENSIVE (correct if a future libtre
                 * build or an exotic pattern this project has not
                 * tried ever does allocate mid-match), not a fix
                 * for a witnessed truncation on this engine. */
                if (rc != REG_OK) { out->rc_final = rc; break; }
                long m_s = (long)pmatch[0].rm_so + (long)pos;
                long m_e = (long)pmatch[0].rm_eo + (long)pos;
                if (out->first_s < 0) {
                    out->first_s = m_s; out->first_e = m_e;
                    out->rc_final = rc;
                    out->ncaps_final = (int)nmatch_cap - 1;
                    /* pmatch[] is relative to the RE-SLICED buffer
                     * (in->buf + pos); the emitted caps must be
                     * absolute against the true subject, exactly
                     * like out->first_s/out->first_e above -- offset every
                     * entry by pos before rendering. */
                    if (pos > 0) {
                        for (size_t ci = 0; ci < nmatch_cap; ci++) {
                            if (pmatch[ci].rm_so >= 0) pmatch[ci].rm_so += (regoff_t)pos;
                            if (pmatch[ci].rm_eo >= 0) pmatch[ci].rm_eo += (regoff_t)pos;
                        }
                    }
                    emit_caps(pmatch, nmatch_cap, caps_final, caps_final_cap);
                }
                count++;
                /* pcrec match_api.md S3.1's find-all advance: off the
                 * match's own reported START, never off the scan
                 * position -- KB-17, the same rule testees/pcre2/
                 * driver.c and testees/onig/driver.c both apply.
                 * Under --utf8 ([B77] U1): the next CHARACTER
                 * boundary of the TRUE subject (pmatch[] is
                 * slice-relative, so the absolute start is
                 * pos + start), not start + 1. TRE itself stays
                 * byte-literal (utf8_set_v1.md 7.3); the flag moves
                 * the harness's advance, never the engine. */
                size_t start = (size_t)pmatch[0].rm_so;
                size_t end = (size_t)pmatch[0].rm_eo;
                if (end > start || !utf8_adv)
                    pos += (end > start) ? end : start + 1;
                else
                    pos = utf8_next_start(in->buf, in->len, pos + start);
                if (whole_subject) break; /* one anchored position only */
                if (pos > in->len) break;
            }
            out->nmatches = count;
            /* KB-29: a MID-loop give-up (any code other than
             * REG_OK/REG_NOMATCH, POSIX's own ordinary "no further
             * matches" terminator for these functions) must
             * propagate as the whole subject's give-up -- discard
             * any match already found THIS call so the
             * classification below falls through to the SAME
             * giveup:<code>:<message> branch a first-call give-up
             * already takes. Mirrors testees/{pcre2,onig,pcrec}/
             * driver.c's own discard exactly. */
            if (out->rc_final != REG_OK && out->rc_final != REG_NOMATCH) {
                out->first_s = out->first_e = -1;
                out->nmatches = -1;
                out->ncaps_final = 0;
                caps_final[0] = '-'; caps_final[1] = 0;
            }
        } else {
            int rc = tre_regnexecb(&re, (const char *)in->buf, in->len,
                                   nmatch_cap, pmatch, 0);
            out->rc_final = rc;
            if (rc == REG_OK) {
                out->first_s = (long)pmatch[0].rm_so;
                out->first_e = (long)pmatch[0].rm_eo;
                out->ncaps_final = (int)nmatch_cap - 1;
                emit_caps(pmatch, nmatch_cap, caps_final, caps_final_cap);
            }
        }
        }
    }
    return now() - t0;
#undef re
}
