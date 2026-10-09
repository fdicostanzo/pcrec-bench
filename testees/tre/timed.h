/* [B133] The TIMED LOOP's interface (see timed.c's header). */
#ifndef TRE_TIMED_H
#define TRE_TIMED_H

#include <tre/tre.h>
#include <stddef.h>

struct timed_in {
    const unsigned char *buf;
    size_t len;
    long iters;
    int prime;          /* [B129] pass 0 is the one UNTIMED call */
    int find_all;
    int utf8_adv;       /* [B77] U1 */
    int whole_subject;
    regex_t *re;
    size_t nmatch_cap;
    regmatch_t *pmatch;
    char *caps_final;   /* the first match's rendered captures */
    size_t caps_final_cap;
};

struct timed_out {
    volatile long first_s, first_e, nmatches;
    volatile int rc_final;
    int ncaps_final;
};

/* Runs the timed loop for one subject and returns the elapsed seconds. */
double timed_run(const struct timed_in *in, struct timed_out *out);

#endif
