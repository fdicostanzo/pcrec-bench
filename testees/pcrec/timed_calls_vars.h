/* [B148] L7 The VARS call-stream timed replay's interface (see
 * timed_calls_vars.c). Reuses timed_calls.h's output struct. */
#ifndef PCREC_TIMED_CALLS_VARS_H
#define PCREC_TIMED_CALLS_VARS_H

#include <stddef.h>

#include "timed_calls.h"
#include "../common/vars_io.h"

struct tvars_in {
    const unsigned char *buf;       /* the whole subject, already in memory */
    size_t len;
    const struct vcall_decl *calls;
    size_t ncalls;
    const struct vbinding *bindings;
    long iters;                     /* REPLAYS of the whole call list */
    int has_g1;
    ptrdiff_t (*caps)[2];
    int use_buffers;
    void *buf_frames, *buf_trail;
    size_t buf_nframes, buf_ntrail;
    int unset_code;                 /* PCREC_ERR_UNSET_VAR: a REFUSED call */
    int (*search)(const unsigned char *, size_t, size_t, ptrdiff_t (*)[2],
                  const void *, size_t);
    int (*search_in)(const unsigned char *, size_t, size_t, ptrdiff_t (*)[2],
                     const void *, size_t, void *, size_t, void *, size_t);
    struct call_res *res;           /* [ncalls], preallocated */
};

/* Runs `iters` replays, clocking each separately; returns the SUM (P6). */
double timed_calls_vars(const struct tvars_in *in, struct tcalls_out *out);

#endif
