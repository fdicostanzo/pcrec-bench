// [B148] L4 The CALL-STREAM timed replay's interface (see timed_calls.cc).
#ifndef RE2_TIMED_CALLS_H
#define RE2_TIMED_CALLS_H

#include <re2/re2.h>

#include "../common/calls_io.h"

struct tcalls_in {
    absl::string_view text;          // the whole subject, already in memory
    const struct call_decl *calls;
    size_t ncalls;
    long iters;                      // REPLAYS of the whole call list
    RE2::Anchor anchor;              // UNANCHORED, or ANCHOR_START (--anchor-explicit)
    int nsub;                        // submatches asked for: 1, or 2 with a group 1
    const RE2 *re;
    absl::string_view *submatch;     // nsub entries
    struct call_res *res;            // [ncalls], preallocated
};

struct tcalls_out {
    volatile long replays_done;
    volatile size_t calls_done;
};

double timed_calls(const struct tcalls_in *in, struct tcalls_out *out);

#endif
