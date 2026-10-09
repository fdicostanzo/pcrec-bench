/* [B133] The TIMED LOOP's interface (see timed.c's header). */
#ifndef ONIG_TIMED_H
#define ONIG_TIMED_H

#include <oniguruma.h>
#include <stddef.h>

struct timed_in {
    const unsigned char *buf;
    size_t len;
    long iters;
    int prime;          /* [B129] pass 0 is the one UNTIMED call */
    int find_all;
    int utf8_adv;       /* [B77] U1 */
    int whole_subject;
    regex_t *reg;
    OnigRegion *region;
};

struct timed_out {
    volatile long first_s, first_e, nmatch;
    volatile int rc_final;
};

/* Runs the timed loop for one subject and returns the elapsed seconds. */
double timed_run(const struct timed_in *in, struct timed_out *out);

#endif
