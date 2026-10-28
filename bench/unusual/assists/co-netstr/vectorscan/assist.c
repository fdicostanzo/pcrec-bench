/* ASSIST TEMPLATE -- Vectorscan (C). Families: recursion, callouts, netstr, vars.
 *
 * Start with `python3 -m pcrecbench assist-init --member M --engine vectorscan`:
 * it writes assists/M/vectorscan/assist.c holding only M's family. Fill the
 * function(s) marked ASSIST (and your setup); leave every BOILERPLATE fence
 * exactly as it is (the self-test compares them with this template). Read
 * bench/unusual/assists/AUTHORS.md and your problem statement first.
 *
 * Built with: gcc -O2, `pkg-config --cflags --libs libhs`, linked with the
 * assist runner (testees/assist/), which owns main's work, the protocol, the
 * clock and the answer tokens. Scratch space is yours (allocate it in
 * ub_setup). Return UB_M (fill *m), UB_N, UB_R (vars: the call is refused)
 * or, on an engine give-up, the engine's own NEGATIVE code. */

/* BOILERPLATE includes */
#include <hs.h>
#include "ub_assist.h"
#include "ub_map.h"
/* END BOILERPLATE */



/* Your state (globals), built by ub_setup outside the clock. */
static hs_database_t *db;
static hs_scratch_t *scratch;
typedef struct { const unsigned char *s; size_t n, base; ub_span *m; int hit; } ctx_t;

/* One event per colon: [from, to) is the digit run (leftmost start) plus ':'.
 * Any digit of the run may start the netstring, so try each start in turn. */
static int on_prefix(unsigned id, unsigned long long from, unsigned long long to,
                     unsigned flags, void *p) {
    ctx_t *x = p;
    size_t c = x->base + to - 1;
    for (size_t b = x->base + from; b < c; b++) {
        size_t len = 0;
        for (size_t i = b; i < c; i++) len = len * 10 + x->s[i] - '0';
        if (len < x->n - c - 1 && x->s[c + 1 + len] == ',') {
            *x->m = (ub_span){b, c + len + 2, b, c};
            return x->hit = 1;
        }
    }
    return 0;
}

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    hs_compile_error_t *err;
    if (hs_compile("\\d{1,9}:", HS_FLAG_SOM_LEFTMOST, HS_MODE_BLOCK, NULL, &db, &err))
        return -1;
    return hs_alloc_scratch(db, &scratch);
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` in subj[0, n) (bytes before
 * `start` stay visible). Fill m->s, m->e and group 1 in m->g1s, m->g1e. */
/* BOILERPLATE shim */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m) {
/* END BOILERPLATE */
    ctx_t x = {subj, n, start, m, 0};
    int rc = hs_scan(db, (const char *)subj + start, n - start, 0, scratch, on_prefix, &x);
    return x.hit ? UB_M : rc == HS_SUCCESS || rc == HS_SCAN_TERMINATED ? UB_N : rc;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */


/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
