/* bench/unusual/callees/replay.c -- the CALLEE-COST microbench ([B148] L5,
 * docs/design/unusual_set_v1.md 3.2 calibration item 3). Replays the views a
 * counting build logged (one fire-log line per callee call: `<callee> <pos>
 * <g1s> <g1e> <verdict>`) through the SAME callees.o the timed drivers link,
 * via the same binding table and the same indirect call, and prints the
 * median ns per fire over ROUNDS timed rounds:
 *
 *     replay SPEC SUBJECT FIRELOG [ROUNDS]
 *     -> `replay<TAB>fires<TAB>N<TAB>ns_per_fire<TAB>X<TAB>verdicts_agree<TAB>yes|no`
 *
 * `verdicts_agree` re-checks every replayed verdict against the logged one
 * (the callee is a pure function of its view). Built and run by
 * tools/callout_calib.py, pinned to one core; never part of a cell. */
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "../../../testees/common/ub_bind.h"

struct fire { const struct ub_slot *s; size_t pos; ptrdiff_t caps[2][2]; long verdict; };

static double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}

static int cmp(const void *a, const void *b) {
    double x = *(const double *)a, y = *(const double *)b;
    return x < y ? -1 : x > y;
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: replay SPEC SUBJECT FIRELOG [ROUNDS]\n"); return 2; }
    char err[256];
    if (ub_bind_parse(argv[1], err, sizeof err)) { fprintf(stderr, "spec: %s\n", err); return 2; }
    FILE *f = fopen(argv[2], "rb");
    if (!f) { perror(argv[2]); return 2; }
    fseek(f, 0, SEEK_END);
    long n = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char *subj = malloc(n ? n : 1);
    if (fread(subj, 1, n, f) != (size_t)n) { perror("read"); return 2; }
    fclose(f);
    int rounds = argc > 4 ? atoi(argv[4]) : 11;

    FILE *lf = fopen(argv[3], "r");
    if (!lf) { perror(argv[3]); return 2; }
    size_t cap = 1024, nf = 0;
    struct fire *fs = malloc(cap * sizeof *fs);
    char name[64];
    long pos, g1s, g1e, verdict;
    while (fscanf(lf, "%63s %ld %ld %ld %ld", name, &pos, &g1s, &g1e, &verdict) == 5) {
        const struct ub_slot *s = NULL;
        for (int k = 0; k < UB_NSLOT && !s; k++)
            if (ub_slots[k].fn && !strcmp(ub_slots[k].callee, name)) s = &ub_slots[k];
        for (int k = 0; k < ub_nnamed && !s; k++)
            if (!strcmp(ub_named[k].slot.callee, name)) s = &ub_named[k].slot;
        if (!s) { fprintf(stderr, "no slot binds callee %s\n", name); return 2; }
        if (nf == cap) fs = realloc(fs, (cap *= 2) * sizeof *fs);
        fs[nf].s = s;
        fs[nf].pos = (size_t)pos;
        fs[nf].caps[0][0] = 0; fs[nf].caps[0][1] = -1;
        fs[nf].caps[1][0] = g1s; fs[nf].caps[1][1] = g1e;
        fs[nf].verdict = verdict;
        nf++;
    }
    fclose(lf);
    if (!nf) { printf("replay\tfires\t0\tns_per_fire\t-\tverdicts_agree\tyes\n"); return 0; }

    /* inner repeat so one round is >= ~2 ms of callee time */
    long reps = 1;
    volatile long sink = 0;
    int agree = 1;
    double *t = malloc(rounds * sizeof *t);
    for (int r = -1; r < rounds; r++) {
        double t0 = now();
        for (long k = 0; k < reps; k++)
            for (size_t i = 0; i < nf; i++) {
                struct ub_view v = { subj, (size_t)n, fs[i].pos, 2,
                                     (const ptrdiff_t (*)[2])fs[i].caps, fs[i].s->user };
                long got = fs[i].s->fn(&v);
                sink += got;
                if (r == -1 && k == 0 && got != fs[i].verdict) agree = 0;
            }
        double dt = now() - t0;
        if (r == -1) {                       /* the warm-up round sizes reps */
            double per = dt / (double)nf;
            reps = per > 0 ? (long)(2e-3 / (per * nf)) + 1 : 1000;
            continue;
        }
        t[r] = dt / ((double)reps * nf) * 1e9;
    }
    qsort(t, rounds, sizeof *t, cmp);
    printf("replay\tfires\t%zu\tns_per_fire\t%.3f\tverdicts_agree\t%s\n", nf, t[rounds / 2],
           agree ? "yes" : "no");
    (void)sink;
    return agree ? 0 : 1;
}
