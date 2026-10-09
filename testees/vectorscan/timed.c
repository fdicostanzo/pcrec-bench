/* [B133] THE TIMED LOOP, ISOLATED. Every instruction between the two clock
 * reads of a subject (nosom and SOM modes, the [B129] --prime pass, and the
 * hs_scan match callbacks, which run INSIDE the timed scan) is in
 * timed_run() and this file's callbacks and nowhere else. See
 * testees/pcrec/timed.c's header for the why ([B132]); the same fix for this
 * engine: its own translation unit, the timed function noinline +
 * aligned(64). It is an INSTRUMENT -- an edit here must be recorded as an
 * instrument change (docs/dev/decisions.md BD-B133). The body is the
 * pre-[B133] loop with the driver's locals turned into fields of *in / *out;
 * the SOM match list (vs_match_list) and its push/reset live here because
 * the callback pushes inside the timed scan, and driver.c reads the list
 * after it. */
#include <hs/hs.h>

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

static void die(const char *what) {
    printf("error\t%s\n", what);
    fflush(stdout);
    exit(2);
}

static void vs_reset(vs_match_list *m) { m->n = 0; }

static void vs_push(vs_match_list *m, unsigned long long from,
                    unsigned long long to) {
    if (m->n == m->cap) {
        size_t newcap = m->cap ? m->cap * 2 : 64;
        vs_match *nv = realloc(m->v, newcap * sizeof *nv);
        if (!nv) die("out of memory accumulating SOM matches");
        m->v = nv;
        m->cap = newcap;
    }
    m->v[m->n].from = from;
    m->v[m->n].to = to;
    m->n++;
}

/* `--som`'s callback: NEVER requests early termination (always returns 0)
 * -- see driver.c's header, "SOM MODE". `context` is a `vs_match_list *`. */
static int HS_CDECL on_match_som(unsigned int id, unsigned long long from,
                                 unsigned long long to, unsigned int flags,
                                 void *context) {
    (void)id; (void)flags;
    vs_push((vs_match_list *)context, from, to);
    return 0;
}

/* The nosom callback: always requests early termination (return 1) -- this
 * config never reports a span or a count (driver.c's header, "MATCHING"). */
typedef struct { volatile int matched; } match_ctx;

static int HS_CDECL on_match(unsigned int id, unsigned long long from,
                             unsigned long long to, unsigned int flags,
                             void *context) {
    (void)id; (void)from; (void)to; (void)flags;
    match_ctx *ctx = (match_ctx *)context;
    ctx->matched = 1;
    return 1;
}

__attribute__((noinline, aligned(64)))
double timed_run(const struct timed_in *in, struct timed_out *out) {
    const int prime = in->prime, som_mode = in->som_mode;
    hs_database_t *db = in->db;
    hs_scratch_t *scratch = in->scratch;
    vs_match_list *ml = in->ml;
    double t0 = now();
    if (som_mode) {
        /* [B92], SOM MODE: the callback never stops early (see the
         * file header) -- every `iters` pass re-scans and
         * re-accumulates the WHOLE subject, which is `--som`'s own
         * real, documented cost. */
        /* [B129] --prime: pass 0 (only with the flag) is the UNTIMED call; the
         * timed loop below is the original one, its bounds and body untouched. */
        for (int pass = prime ? 0 : 1; pass < 2; pass++) {
            volatile long n_it = pass ? in->iters : 1;
            if (pass && prime) t0 = now();
            for (long it = 0; it < n_it; it++) {
            vs_reset(ml);
            hs_error_t rc = hs_scan(db, (const char *)in->buf,
                                    (unsigned int)in->len, 0, scratch,
                                    on_match_som, ml);
            if (rc != HS_SUCCESS) {
                /* Same reasoning as the `nosom` arm below (see
                 * header, "GAVE-UP CODES: NONE") -- `on_match_som`
                 * never requests early termination, so there is no
                 * HS_SCAN_TERMINATED to except here either. */
                out->matched = -1;
                (void)rc;
                break;
            }
            out->matched = ml->n > 0 ? 1 : 0;
            }
        }
    } else {
        /* [B129] --prime: pass 0 (only with the flag) is the UNTIMED call; the
         * timed loop below is the original one, its bounds and body untouched. */
        for (int pass = prime ? 0 : 1; pass < 2; pass++) {
            volatile long n_it = pass ? in->iters : 1;
            if (pass && prime) t0 = now();
            for (long it = 0; it < n_it; it++) {
            match_ctx ctx = { 0 };
            hs_error_t rc = hs_scan(db, (const char *)in->buf,
                                    (unsigned int)in->len, 0, scratch,
                                    on_match, &ctx);
            if (rc != HS_SUCCESS && rc != HS_SCAN_TERMINATED) {
                /* No documented resource-limit refusal on this route
                 * (see header, "GAVE-UP CODES: NONE") -- an
                 * unexpected negative return is a driver/API-level
                 * problem, reported via the ANSWER column so the
                 * harness's crashed path (never a gave-up range,
                 * empty by construction) picks it up. */
                out->matched = -1;
                (void)rc;
                break;
            }
            out->matched = ctx.matched ? 1 : 0;
            }
        }
    }
    return now() - t0;
}
