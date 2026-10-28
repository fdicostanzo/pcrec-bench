/* testees/assist/ub_timed.h -- the assist runner's TIMED LOOPS (ub_timed.c),
 * their own translation unit (BD16: an instrument is a TU of its own,
 * noinline + aligned(64); the assist and the protocol code cannot move it).
 * The assist is reached through a function POINTER, so the loop's code does
 * not depend on the assist it times. */
#ifndef UB_TIMED_H
#define UB_TIMED_H

#include <stddef.h>

#include "ub_assist.h"
#include "../common/vars_io.h"

typedef int ub_find_fn(const unsigned char *, size_t, size_t, ub_span *);
typedef int ub_vars_fn(const unsigned char *, size_t, const ub_var *, size_t,
                       ub_span *);
typedef void ub_reset_fn(void);

/* search_short / throughput: `iters` repetitions of ONE operation on one
 * subject -- the first match from offset 0, or (find_all) every
 * non-overlapping match with the protocol's advance (end, or start + 1 after
 * an empty match). */
struct ub_search_in {
    const unsigned char *buf;
    size_t len;
    long iters;
    int find_all;
    ub_find_fn *find;
};
struct ub_search_out {
    int rc;              /* the FIRST call's answer (UB_M / UB_N / < 0) */
    ub_span first;       /* its spans when rc == UB_M */
    long nmatch;         /* find_all: the count (-1 after a give-up) */
    int rc_final;        /* find_all: the loop's terminal code */
};
double ub_timed_search(const struct ub_search_in *in, struct ub_search_out *out);

/* --mode calls (cscan streams): every call at its offset, the whole subject
 * visible; one replay clocked per iteration, the clocks summed (P6). */
struct ub_calls_in {
    const unsigned char *buf;
    size_t len;
    const struct call_decl *calls;
    size_t ncalls;
    long iters;
    ub_find_fn *find;
    struct call_res *res;
};
/* --mode calls (vars streams): every call one LINE alone with its binding;
 * `reset` (the cache) runs AFTER each replay's clock stopped. */
struct ub_vcalls_in {
    const unsigned char *buf;
    const struct vcall_decl *calls;
    size_t ncalls;
    const struct vbinding *bindings;
    long iters;
    ub_vars_fn *vars;
    ub_reset_fn *reset;
    struct call_res *res;
};
struct ub_calls_out {
    volatile long replays_done;
    volatile size_t calls_done;
};
double ub_timed_calls(const struct ub_calls_in *in, struct ub_calls_out *out);
double ub_timed_vcalls(const struct ub_vcalls_in *in, struct ub_calls_out *out);

#endif
