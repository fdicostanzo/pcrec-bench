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

/* BOILERPLATE shim */
static ub_map cache;            /* the compiled-pattern cache: key -> pcre2_code * */
static void cache_drop(void *v) { pcre2_code_free((pcre2_code *)v); }
void ub_reset(void) { ub_map_each(&cache, cache_drop); ub_map_free(&cache); }
/* END BOILERPLATE */

/* Every value byte is spelled \xHH, so a value always matches as itself. */
static char *lit(char *o, const unsigned char *s, size_t n) {
    for (; n--; s++) {
        *o++ = '\\';
        *o++ = 'x';
        *o++ = "0123456789abcdef"[*s >> 4];
        *o++ = "0123456789abcdef"[*s & 15];
    }
    return o;
}

/* Fetch the compiled pattern (compiling on a miss) and search the line. */
static int run(const char *pat, size_t len, const unsigned char *line, size_t n, ub_span *m) {
    pcre2_code *re = ub_map_get(&cache, pat, len);
    if (!re) {
        int err;
        PCRE2_SIZE off;
        re = pcre2_compile((PCRE2_SPTR)pat, len, 0, &err, &off, NULL);
        if (!re) return -err;
        ub_map_put(&cache, pat, len, re);
    }
    pcre2_match_data *md = pcre2_match_data_create_from_pattern(re, NULL);
    int rc = pcre2_match(re, line, n, 0, 0, md, NULL);
    if (rc > 0) {
        PCRE2_SIZE *ov = pcre2_get_ovector_pointer(md);
        m->s = ov[0];
        m->e = ov[1];
    }
    pcre2_match_data_free(md);
    return rc > 0 ? UB_M : rc == PCRE2_ERROR_NOMATCH ? UB_N : rc;
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
    const ub_var *t = ub_lookup(v, nv, "tenant");
    if (!t) return UB_R;
    char *p = malloc(4 * t->len + 64), *o = p;
    *o++ = '^';
    o = lit(o, t->p, t->len);
    o = stpcpy(o, "-[0-9]{4} (?:ERROR|WARN) ");
    int r = run(p, o - p, line, n, m);
    free(p);
    return r;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */


/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
