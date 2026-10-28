/* ASSIST TEMPLATE -- libpcre2 (C). Families: vars, netstr.
 *
 * Start with `python3 -m pcrecbench assist-init --member M --engine pcre2`:
 * it writes assists/M/pcre2/assist.c holding only M's family. Fill the
 * function(s) marked ASSIST (and your setup); leave every BOILERPLATE fence
 * exactly as it is (the self-test compares them with this template). Read
 * bench/unusual/assists/AUTHORS.md and your problem statement first.
 *
 * Built with: gcc -O2, -DPCRE2_CODE_UNIT_WIDTH=8, -lpcre2-8, linked with the
 * assist runner (testees/assist/), which owns main's work, the protocol, the
 * clock and the answer tokens. Return UB_M (fill *m), UB_N, UB_R (vars: the
 * call is refused) or, on an engine give-up, the engine's own NEGATIVE code. */

/* BOILERPLATE includes */
#include <pcre2.h>
#include "ub_assist.h"
#include "ub_map.h"
/* END BOILERPLATE */

/* ==== FAMILY vars ==== */
/* BOILERPLATE shim */
static ub_map cache;            /* the compiled-pattern cache: key -> pcre2_code * */
static void cache_drop(void *v) { pcre2_code_free((pcre2_code *)v); }
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

/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
