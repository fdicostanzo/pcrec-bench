/* [B133] The TIMED LOOP's interface (see timed.c's header). */
#ifndef VS_TIMED_H
#define VS_TIMED_H

#include <hs/hs.h>
#include <stddef.h>

/* [B92] SOM MODE: every (from, to) pair one hs_scan() accumulates. */
typedef struct { unsigned long long from, to; } vs_match;

typedef struct {
    vs_match *v;
    size_t    n, cap;
} vs_match_list;

struct timed_in {
    const unsigned char *buf;
    size_t len;
    long iters;
    int prime;          /* [B129] pass 0 is the one UNTIMED call */
    int som_mode;
    hs_database_t *db;
    hs_scratch_t *scratch;
    vs_match_list *ml;  /* SOM mode only; reused across subjects/passes */
};

struct timed_out {
    volatile int matched;
};

/* Runs the timed loop for one subject and returns the elapsed seconds. */
double timed_run(const struct timed_in *in, struct timed_out *out);

#endif
