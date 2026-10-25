/* [B140] The SUBSTITUTION timed call's interface (see timed_subst.c). */
#ifndef PCRE2_TIMED_SUBST_H
#define PCRE2_TIMED_SUBST_H

#include <stddef.h>
#include <stdint.h>

struct tsubst_in {
    const unsigned char *buf;       /* the subject, already in memory */
    size_t len;
    const unsigned char *repl;      /* the template, in PCRE2's dialect */
    size_t repl_len;
    uint32_t opts;                  /* GLOBAL [| EXTENDED]; never OVERFLOW_LENGTH */
    int size_first;                 /* 0 = bound arm, 1 = size-first arm */
    long iters;                     /* 1 in this bench (subst_bench_v1.md 3.1.2) */
    void *code, *md;
    unsigned char *out;             /* pre-sized AND pre-faulted, untimed */
    size_t cap;
    int (*subst)(void *, const unsigned char *, size_t, size_t, uint32_t,
                 void *, void *, const unsigned char *, size_t,
                 unsigned char *, size_t *);
};

struct tsubst_out {
    volatile int rc;                /* the last call's return: nsubst, or < 0 */
    volatile size_t outlen;         /* the output length, NUL excluded */
};

/* Runs the timed substitution for one subject; returns the elapsed seconds. */
double timed_subst(const struct tsubst_in *in, struct tsubst_out *out);

#endif
