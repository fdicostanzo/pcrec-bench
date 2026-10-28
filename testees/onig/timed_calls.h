/* [B148] L4 The CALL-STREAM timed replay's interface (see timed_calls.c). */
#ifndef ONIG_TIMED_CALLS_H
#define ONIG_TIMED_CALLS_H

#include <oniguruma.h>
#include <stddef.h>

#include "../common/calls_io.h"

struct tcalls_in {
    const unsigned char *buf;       /* the whole subject, already in memory */
    size_t len;
    const struct call_decl *calls;
    size_t ncalls;
    long iters;                     /* REPLAYS of the whole call list */
    int anchored;                   /* --anchor-explicit: onig_match at the offset */
    int has_g1;
    regex_t *reg;
    OnigRegion *region;
    struct call_res *res;           /* [ncalls], preallocated */
};

struct tcalls_out {
    volatile long replays_done;
    volatile size_t calls_done;
};

/* Runs `iters` replays, clocking each separately; returns the SUM (P6). */
double timed_calls(const struct tcalls_in *in, struct tcalls_out *out);

#endif
