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

/* ==== FAMILY recursion ==== */
/* Your state (globals), built by ub_setup outside the clock. */

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    return 0;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` (cscan: exactly at `start`) in
 * subj[0, n) (bytes before `start` stay visible). Fill m->s, m->e and, for
 * cscan, the body in m->g1s, m->g1e. */
/* BOILERPLATE shim */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m) {
/* END BOILERPLATE */
    return UB_N;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */
/* ==== END FAMILY recursion ==== */

/* ==== FAMILY callouts ==== */
/* BOILERPLATE wrappers */
static int pred(const unsigned char *subj, size_t n, size_t g1s, size_t g1e) { return ub_pred(subj, n, g1s, g1e); }
/* END BOILERPLATE */

/* Your state (globals), built by ub_setup outside the clock. */

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    return 0;
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
    return UB_N;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */
/* ==== END FAMILY callouts ==== */

/* ==== FAMILY netstr ==== */
/* Your state (globals), built by ub_setup outside the clock. */

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    return 0;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` in subj[0, n) (bytes before
 * `start` stay visible). Fill m->s, m->e and group 1 in m->g1s, m->g1e. */
/* BOILERPLATE shim */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m) {
/* END BOILERPLATE */
    return UB_N;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */
/* ==== END FAMILY netstr ==== */

/* ==== FAMILY vars ==== */
/* BOILERPLATE shim */
static ub_map cache;            /* the compiled-pattern cache: key -> hs_database_t * */
static void cache_drop(void *v) { hs_free_database((hs_database_t *)v); }
void ub_reset(void) { ub_map_each(&cache, cache_drop); ub_map_free(&cache); }
/* END BOILERPLATE */

/* Your state (globals), built by ub_setup outside the clock. */

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    return 0;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: one call. `line` is matched alone (offsets line-relative);
 * ub_lookup(v, nv, "name") is the variable's value or NULL when UNSET. Keep
 * compiled patterns in `cache` (ub_map_get / ub_map_put). */
/* BOILERPLATE shim */
int ub_vars(const unsigned char *line, size_t n, const ub_var *v, size_t nv, ub_span *m) {
/* END BOILERPLATE */
    return UB_N;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */
/* ==== END FAMILY vars ==== */

/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
