/* testees/assist/ub_defaults.c -- the defaults for the ub_assist.h functions
 * an assist of another family does not define. Compiled THREE times
 * (-DUB_DEFAULT_FIND / _VARS / _RESET) into libub_defaults.a, which the build
 * links AFTER the assist: an archive member is pulled only for a symbol still
 * undefined, so the assist's own definition always wins (a C object, a C++
 * object or a Rust staticlib alike). Calling a default is a family mismatch:
 * it aborts by name. */
#include <stdio.h>
#include <stdlib.h>

#include "ub_assist.h"

#ifdef UB_DEFAULT_FIND
int ub_find(const unsigned char *s, size_t n, size_t st, ub_span *m) {
    (void)s; (void)n; (void)st; (void)m;
    fprintf(stderr, "ub_find: this assist defines no ub_find (another family?)\n");
    abort();
}
#endif
#ifdef UB_DEFAULT_VARS
int ub_vars(const unsigned char *l, size_t n, const ub_var *v, size_t nv,
            ub_span *m) {
    (void)l; (void)n; (void)v; (void)nv; (void)m;
    fprintf(stderr, "ub_vars: this assist defines no ub_vars (another family?)\n");
    abort();
}
#endif
#ifdef UB_DEFAULT_RESET
void ub_reset(void) {}
#endif
