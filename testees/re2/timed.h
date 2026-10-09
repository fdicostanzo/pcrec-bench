// [B133] The TIMED LOOP's interface (see timed.cc's header).
#ifndef RE2_TIMED_H
#define RE2_TIMED_H

#include <re2/re2.h>

struct timed_in {
    absl::string_view text;
    long iters;
    int prime;          // [B129] pass 0 is the one UNTIMED call
    int find_all;
    int utf8_adv;       // [B77] U1
    int nsub;
    const RE2 *re;
    RE2::Anchor anchor;
    absl::string_view *submatch;   // nsub entries, read by the caller after
};

struct timed_out {
    volatile long first_s, first_e, nmatch;
    volatile int matched_final;
    volatile int nsub_out;
};

// Runs the timed loop for one subject and returns the elapsed seconds.
double timed_run(const struct timed_in *in, struct timed_out *out);

#endif
