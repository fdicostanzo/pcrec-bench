/* [B148] L4 The CALL-STREAM timed replay's interface (see timed_calls.c). */
#ifndef PCREC_TIMED_CALLS_H
#define PCREC_TIMED_CALLS_H

#include <stddef.h>

#include "../common/calls_io.h"

struct tcalls_in {
    const unsigned char *buf;       /* the whole subject, already in memory */
    size_t len;
    const struct call_decl *calls;
    size_t ncalls;
    long iters;                     /* REPLAYS of the whole call list */
    int anchored;                   /* --anchor-explicit: _match_caps at the offset */
    int has_g1;
    ptrdiff_t (*caps)[2];
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
    struct call_res *res;           /* [ncalls], preallocated */
};

struct tcalls_out {
    volatile long replays_done;
    volatile size_t calls_done;
};

/* Runs `iters` replays, clocking each separately; returns the SUM (P6). */
double timed_calls(const struct tcalls_in *in, struct tcalls_out *out);

#endif
