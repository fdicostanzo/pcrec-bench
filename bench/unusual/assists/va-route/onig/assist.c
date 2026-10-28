/* ASSIST TEMPLATE -- Oniguruma (C). Families: vars, netstr.
 *
 * Start with `python3 -m pcrecbench assist-init --member M --engine onig`:
 * it writes assists/M/onig/assist.c holding only M's family. Fill the
 * function(s) marked ASSIST (and your setup); leave every BOILERPLATE fence
 * exactly as it is (the self-test compares them with this template). Read
 * bench/unusual/assists/AUTHORS.md and your problem statement first.
 *
 * Built with: gcc -O2, -lonig, linked with the assist runner
 * (testees/assist/), which owns main's work, the protocol, the clock and the
 * answer tokens. onig_initialize is yours (in ub_setup). Return UB_M (fill
 * *m), UB_N, UB_R (vars: the call is refused) or, on an engine give-up, the
 * engine's own NEGATIVE code. */

/* BOILERPLATE includes */
#include <oniguruma.h>
#include "ub_assist.h"
#include "ub_map.h"
#include <stdio.h>
/* END BOILERPLATE */

/* BOILERPLATE shim */
static ub_map cache;            /* the compiled-pattern cache: key -> regex_t * */
static void cache_drop(void *v) { onig_free((regex_t *)v); }
void ub_reset(void) { ub_map_each(&cache, cache_drop); ub_map_free(&cache); }
/* END BOILERPLATE */

/* Your state (globals), built by ub_setup outside the clock. */
static OnigRegion *region;

static char *hex(char *o, const unsigned char *p, size_t n) {
    while (n--) o += sprintf(o, "\\x%02x", *p++);
    return o;
}

/* Compile (or fetch by resolved pattern text) and search the line alone. */
static int run(const char *pat, const unsigned char *line, size_t n, ub_span *m) {
    size_t k = strlen(pat);
    regex_t *re = ub_map_get(&cache, pat, k);
    if (!re) {
        int r = onig_new(&re, (UChar *)pat, (UChar *)pat + k, ONIG_OPTION_NONE,
                         ONIG_ENCODING_ASCII, ONIG_SYNTAX_PERL_NG, NULL);
        if (r) return r;
        ub_map_put(&cache, pat, k, re);
    }
    int r = onig_search(re, line, line + n, line, line + n, region, ONIG_OPTION_NONE);
    m->s = region->beg[0];
    m->e = region->end[0];
    return r < 0 ? (r == ONIG_MISMATCH ? UB_N : r) : UB_M;
}

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    OnigEncoding enc = ONIG_ENCODING_ASCII;
    onig_initialize(&enc, 1);
    region = onig_region_new();
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
    const ub_var *p = ub_lookup(v, nv, "prefix"), *r = ub_lookup(v, nv, "res"),
                 *f = ub_lookup(v, nv, "fmt");
    if (!r) return UB_R;
    char s[64 + 4 * (r->len + (p ? p->len : 0))], *o = stpcpy(s, "^/");
    o = p && p->len ? hex(o, p->p, p->len) : hex(o, (const unsigned char *)"api", 3);
    o = hex(stpcpy(o, "/v[0-9]+/"), r->p, r->len);
    strcpy(f ? stpcpy(o, "\\.json") : o, "(?:\\?|$)");
    return run(s, line, n, m);
/* BOILERPLATE shim */
}
/* END BOILERPLATE */


/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
