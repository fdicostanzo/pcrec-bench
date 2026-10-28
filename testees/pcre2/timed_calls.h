/* [B148] L4 The CALL-STREAM timed replay's interface (see timed_calls.c). */
#ifndef PCRE2_TIMED_CALLS_H
#define PCRE2_TIMED_CALLS_H

#include <stddef.h>
#include <stdint.h>

#include "../common/calls_io.h"

struct tcalls_in {
    const unsigned char *buf;       /* the whole subject, already in memory */
    size_t len;
    const struct call_decl *calls;  /* the declared calls, in order */
    size_t ncalls;
    long iters;                     /* REPLAYS of the whole call list */
    uint32_t opts;                  /* 0, or PCRE2_ANCHORED (explicit anchoring) */
    void *code, *md, *mctx;         /* mctx NULL = the library's defaults */
    size_t *ov;                     /* the match data's ovector */
    int (*match)(void *, const unsigned char *, size_t, size_t, uint32_t,
                 void *, void *);
    struct call_res *res;           /* [ncalls], preallocated, untouched pages ok */
};

struct tcalls_out {
    volatile long replays_done;     /* for the timeout path */
    volatile size_t calls_done;     /* calls answered in the current replay */
};

/* Runs `iters` replays, clocking each separately; returns the SUM (P6). */
double timed_calls(const struct tcalls_in *in, struct tcalls_out *out);

#endif
