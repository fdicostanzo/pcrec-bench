/* [B133] The TIMED LOOP's interface (see timed.c's header). */
#ifndef PCRE2_TIMED_H
#define PCRE2_TIMED_H

#include <stddef.h>
#include <stdint.h>

struct timed_in {
    const unsigned char *buf;
    size_t len;
    long iters;
    int prime;              /* [B129] pass 0 is the one UNTIMED call */
    int find_all;
    int utf8_adv;           /* [B77] U1 */
    int utf_always_check;   /* [B94] control-only */
    int dfa;
    uint32_t opts, copts, ovn;
    void *code, *md;
    size_t *ov;             /* the match data's ovector, read after each call */
    size_t *firstov;        /* [512] the first match's pairs, kept */
    int *dfa_ws;
    size_t dfa_ws_n;
    int (*match)(void *, const unsigned char *, size_t, size_t, uint32_t,
                 void *, void *);
    int (*dfa_match)(void *, const unsigned char *, size_t, size_t, uint32_t,
                     void *, void *, int *, size_t);
    void (*die)(const char *);
};

struct timed_out {
    volatile long first_s, first_e, nmatch;
    volatile int rc_final;
    volatile uint32_t npairs;
};

/* Runs the timed loop for one subject and returns the elapsed seconds. */
double timed_run(const struct timed_in *in, struct timed_out *out);

#endif
