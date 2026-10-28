/* [B148] L4 The CALL-STREAM timed replay's interface (see timed_calls.c). */
#ifndef VS_TIMED_CALLS_H
#define VS_TIMED_CALLS_H

#include <hs/hs.h>
#include <stddef.h>

#include "../common/calls_io.h"

struct tcalls_in {
    const unsigned char *buf;       /* the whole subject, already in memory */
    size_t len;
    const struct call_decl *calls;
    size_t ncalls;
    long iters;                     /* REPLAYS of the whole call list */
    hs_database_t *db;              /* compiled with HS_FLAG_SOM_LEFTMOST */
    hs_scratch_t *scratch;
    struct call_res *res;           /* [ncalls], preallocated */
};

struct tcalls_out {
    volatile long replays_done;
    volatile size_t calls_done;
};

double timed_calls(const struct tcalls_in *in, struct tcalls_out *out);

#endif
