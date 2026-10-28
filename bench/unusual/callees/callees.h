/* bench/unusual/callees/callees.h -- THE SHARED CALLEES of the unusual set's
 * callout members (docs/design/unusual_set_v1.md 3.2, r9 C5; lane b148l5).
 *
 * One C body per callee, PURE: the verdict depends only on the view (match
 * api 11.6 para 1). Engine-neutral: every engine's WRAPPER (testees/pcre2/
 * callout_wrap.c, testees/onig/callout_wrap.c, pcrec's generated binding
 * unit) builds a `struct ub_view` from its own callout block, calls the
 * callee through a `struct ub_slot`, and translates the verdict with the
 * RETURN-CODE MAPPING of 3.2:
 *
 *   callee verdict   pcrec            libpcre2              Oniguruma
 *   UB_CONTINUE      RX_PASS (0)      0                     ONIG_CALLOUT_SUCCESS (0)
 *   UB_FAIL          RX_FAIL (-1)     +1 (a NEGATIVE value  ONIG_CALLOUT_FAIL (1)
 *                                      abandons the match)
 *   n > 0 (CONSUME)  n (consume site)  --                   --
 *
 * Compiled ONCE into `callees.o` with fixed flags (pcrecbench/callees.py,
 * FLAGS) and linked into every driver; `-DUB_COUNT` builds the untimed
 * COUNTING object (`callees_count.o`), the only one with a counter: each
 * fire appends its view to the file named by $UB_FIRE_LOG. */
#ifndef UB_CALLEES_H
#define UB_CALLEES_H

#include <stddef.h>

#define UB_CONTINUE 0
#define UB_FAIL     (-1)
/* a CONSUME callee (pcrec `consume` sites only) returns n >= 1 to consume n
 * bytes, UB_CONTINUE for n == 0. */

#define UB_MAXCAP 16          /* groups a wrapper copies into the view (the
                                 callout members have 1) */

struct ub_view {
    const unsigned char *subject;   /* the whole subject */
    size_t len;
    size_t pos;                     /* where the engine stands at the site */
    size_t ncap;                    /* the pattern's group count + 1 */
    const ptrdiff_t (*caps)[2];     /* [k] = group k's last CLOSED span, or
                                       {-1,-1}; caps[0] = {attempt start, -1} */
    void *user;                     /* the slot's user data */
};

typedef long ub_fn(const struct ub_view *v);

/* the callees (spec names in testees/common/ub_bind.c) */
long ub_luhn(const struct ub_view *v);        /* group 1 passes the Luhn check */
long ub_isbn13(const struct ub_view *v);      /* group 1 is a valid ISBN-13 */
long ub_member(const struct ub_view *v);      /* group 1 is in the user set */
long ub_netstr(const struct ub_view *v);      /* CONSUME group 1's length (pcrec) */
long ub_netstr_end(const struct ub_view *v);  /* pass iff pos - (g1.end + 1) == len */
long ub_stub(const struct ub_view *v);        /* always UB_CONTINUE (the pass arm) */

/* the member set: built ONCE, before any timed call, from a file of one name
 * per line (`#` comments). -> the `user` for ub_member, or NULL. */
void *ub_member_new(const char *path);

/* 1 in the counting object, 0 in the timed one (a driver can refuse a fire
 * pass on the wrong build by name). */
int ub_counting_build(void);

#endif
