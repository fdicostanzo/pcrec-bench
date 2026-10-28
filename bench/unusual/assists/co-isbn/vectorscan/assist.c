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


/* BOILERPLATE wrappers */
static int pred(const unsigned char *subj, size_t n, size_t g1s, size_t g1e) { return ub_pred(subj, n, g1s, g1e); }
/* END BOILERPLATE */

static hs_database_t *db;
static hs_scratch_t *scr;
struct ctx { const unsigned char *subj; size_t n, base, start; ub_span *m; };

static int on_match(unsigned id, unsigned long long from, unsigned long long to, unsigned flags, void *p) {
    struct ctx *c = p;
    size_t s = c->base + from, e = c->base + to, b = s + 0;
    if (s < c->start || !pred(c->subj, c->n, b, e)) return 0;
    *c->m = (ub_span){s, e, b, e};
    return 1;
}

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    hs_compile_error_t *err;
    return hs_compile("\\b97[89]\\d{10}\\b", HS_FLAG_SOM_LEFTMOST, HS_MODE_BLOCK, NULL, &db, &err) != HS_SUCCESS
        || hs_alloc_scratch(db, &scr) != HS_SUCCESS;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first PASSING candidate at or after `start` in subj[0, n)
 * (bytes before `start` stay visible). pred(subj, n, b, c) is the member's
 * shared predicate on group 1 = [b, c): 1 pass, 0 fail. Fill m->s, m->e and
 * group 1 in m->g1s, m->g1e. */
/* BOILERPLATE shim */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m) {
/* END BOILERPLATE */
    size_t base = start ? start - 1 : 0;   /* one byte of context for \b */
    struct ctx c = {subj, n, base, start, m};
    hs_error_t r = hs_scan(db, (const char *)subj + base, n - base, 0, scr, on_match, &c);
    return r == HS_SCAN_TERMINATED ? UB_M : r == HS_SUCCESS ? UB_N : r;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */



/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
