/* [B140] The SUBSTITUTION timed call's interface (see timed_subst.c). */
#ifndef PCREC_TIMED_SUBST_H
#define PCREC_TIMED_SUBST_H

#include <stddef.h>

/* `pb_subst_all` (subst_shim.c): the contract's sub_all() (subst_api.md
 * 6.9) over the artifact pair -- the count of matches substituted (>= 0)
 * with *len the output length, or a negative code. out == NULL with cap == 0
 * only SIZES (10.7). */
typedef int (*psubst_fn)(const unsigned char *s, size_t n, unsigned char *out,
                         size_t cap, size_t *len);

struct psubst_in {
    const unsigned char *buf;       /* the subject, already in memory */
    size_t len;
    unsigned char *out;             /* pre-sized AND pre-faulted, untimed */
    size_t cap;                     /* the bound arm's capacity */
    int size_first;                 /* 0 = bound arm, 1 = size-first arm */
    long iters;                     /* 1 in this bench (subst_bench_v1.md 3.1.2) */
    psubst_fn subst_all;
};

struct psubst_out {
    volatile int rc;                /* the last call's return: nsubst, or < 0 */
    volatile size_t outlen;         /* the output length */
};

/* Runs the timed substitution for one subject; returns the elapsed seconds. */
double timed_subst(const struct psubst_in *in, struct psubst_out *out);

#endif
