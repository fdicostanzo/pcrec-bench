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
static size_t *stack, cap, depth, lo, hi;

/* every paren is an event; the host keeps the nesting stack */
static int on_paren(unsigned id, unsigned long long from, unsigned long long to,
                    unsigned flags, void *ctx) {
    if (((const char *)ctx)[to - 1] == '(') { stack[depth++] = to - 1; return 0; }
    if (!depth) return 0;
    size_t s = stack[--depth];
    if (s < lo) { lo = s; hi = to; }
    return !depth;
}

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    hs_compile_error_t *err;
    return hs_compile("[()]", 0, HS_MODE_BLOCK, NULL, &db, &err) ||
           hs_alloc_scratch(db, &scratch);
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` (cscan: exactly at `start`) in
 * subj[0, n) (bytes before `start` stay visible). Fill m->s, m->e and, for
 * cscan, the body in m->g1s, m->g1e. */
/* BOILERPLATE shim */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m) {
/* END BOILERPLATE */
    if (cap < n) stack = realloc(stack, (cap = n) * sizeof *stack);
    depth = 0; lo = -1;
    int r = hs_scan(db, (const char *)subj + start, n - start, 0, scratch,
                    on_paren, (void *)(subj + start));
    if (r && r != HS_SCAN_TERMINATED) return r;
    if (lo == (size_t)-1) return UB_N;
    m->s = start + lo; m->e = start + hi;
    return UB_M;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */




/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
