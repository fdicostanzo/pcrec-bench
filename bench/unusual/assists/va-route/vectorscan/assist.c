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
#include <stdio.h>
#include <hs.h>
#include "ub_assist.h"
#include "ub_map.h"
/* END BOILERPLATE */




/* BOILERPLATE shim */
static ub_map cache;            /* the compiled-pattern cache: key -> hs_database_t * */
static void cache_drop(void *v) { hs_free_database((hs_database_t *)v); }
void ub_reset(void) { ub_map_each(&cache, cache_drop); ub_map_free(&cache); }
/* END BOILERPLATE */

static hs_scratch_t *sc;

static int hit(unsigned id, unsigned long long from, unsigned long long to, unsigned fl, void *ctx) {
    ub_span *m = ctx;
    m->s = from; m->e = to;
    return 1;
}

/* every byte as \xHH: matches as itself, NUL included */
static char *esc(char *o, const ub_var *x) {
    for (size_t i = 0; i < x->len; i++) sprintf(o + 4 * i, "\\x%02x", x->p[i]);
    o[4 * x->len] = 0;
    return o;
}

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
    const ub_var *p = ub_lookup(v, nv, "prefix"), *r = ub_lookup(v, nv, "res");
    if (!r) return UB_R;
    size_t k = p ? p->len : 0;
    char e[4 * r->len + 1], f[4 * k + 1], pat[4 * (r->len + k) + 64];
    sprintf(pat, "^/%s/v[0-9]+/%s%s(?:\\?|$)", k ? esc(f, p) : "api", esc(e, r),
            ub_lookup(v, nv, "fmt") ? "\\.json" : "");
    m->s = m->g1s = m->g1e = -1;
    hs_database_t *db = ub_map_get(&cache, pat, strlen(pat));
    if (!db) {
        hs_compile_error_t *err;
        int rc = hs_compile(pat, HS_FLAG_SOM_LEFTMOST, HS_MODE_BLOCK, NULL, &db, &err);
        if (rc != HS_SUCCESS) return hs_free_compile_error(err), rc;
        ub_map_put(&cache, pat, strlen(pat), db);
        hs_alloc_scratch(db, &sc);
    }
    hs_scan(db, (const char *)line, n, 0, sc, hit, m);
    return m->s < 0 ? UB_N : UB_M;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
