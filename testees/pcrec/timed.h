/* [B133] The TIMED LOOP's interface. Everything between the two clock reads
 * of a subject lives in timed.c, a translation unit of its own that no stamp,
 * getter or protocol edit ever touches (see timed.c's header). The driver
 * hands the function the already-resolved entry points and gets the elapsed
 * seconds back; the volatile outputs are where the sigsetjmp/longjmp timeout
 * path in driver.c can still see them. */
#ifndef PCREC_TIMED_H
#define PCREC_TIMED_H

#include <stddef.h>

struct timed_in {
    const unsigned char *buf;
    size_t len;
    long iters;
    int prime;      /* [B129] --prime: pass 0 is the one UNTIMED call */
    int anchored;   /* --mode match */
    int find_all;
    int utf8_adv;   /* [B77] U1 */
    int ncaps;
    ptrdiff_t (*caps)[2];
    ptrdiff_t (*firstcaps)[2];
    int use_buffers;
    void *buf_frames, *buf_trail;
    size_t buf_nframes, buf_ntrail;
    int       (*search)(const unsigned char *, size_t, size_t,
                        ptrdiff_t (*)[2]);
    long long (*match_caps)(const unsigned char *, size_t, size_t,
                            ptrdiff_t (*)[2]);
    int       (*search_in)(const unsigned char *, size_t, size_t,
                           ptrdiff_t (*)[2], void *, size_t, void *, size_t);
    long long (*match_caps_in)(const unsigned char *, size_t, size_t,
                               ptrdiff_t (*)[2], void *, size_t, void *,
                               size_t);
};

struct timed_out {
    volatile long first_s, first_e, nmatch;
    volatile int giveup;
};

/* Runs the timed loop for one subject and returns the elapsed seconds. */
double timed_run(const struct timed_in *in, struct timed_out *out);

#endif
