/* drv_probe.c -- [B112] diagnostic (3): counters substituted (perf refused,
 * paranoid=4, no sudo). Identical timing loop and identical malloc() subject
 * allocation to I-114's drv.c (no alignment change here -- that is
 * drv_align.c's job) plus per-launch PLACEMENT telemetry: the hot
 * function's own runtime address (rx_search is statically linked into this
 * PIE binary, so the C function pointer IS its runtime virtual address --
 * no /proc/self/maps or nm needed), the subject buffer's runtime address,
 * and the executable's own load base (first r-xp region of argv[0] in
 * /proc/self/maps) so a reader can compute the in-binary offset too. This
 * cannot see physical frame / cache-set placement (that needs perf or
 * /proc/self/pagemap, both refused without root) -- it is a virtual-address
 * substitute, reported as such.
 * argv: SUBJECT_FILE NTRIALS
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#include <stdint.h>
#include <time.h>
#include <unistd.h>

extern int rx_search(const unsigned char *subject, size_t subject_length,
                      size_t search_from, ptrdiff_t (*capture_spans)[2]);
extern size_t rx_next_pos(const unsigned char *s, size_t n, size_t pos);

static uint64_t now_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (uint64_t)ts.tv_sec * 1000000000ull + (uint64_t)ts.tv_nsec;
}

static void run_once(const unsigned char *s, size_t n,
                      long *out_matches, uint64_t *out_hash) {
    size_t pos = 0;
    long matches = 0;
    uint64_t h = 1469598103934665603ull;
    const uint64_t prime = 1099511628211ull;
    ptrdiff_t caps[1][2];
    while (pos <= n) {
        int ok = rx_search(s, n, pos, caps);
        if (!ok) break;
        ptrdiff_t start = caps[0][0], end = caps[0][1];
        matches++;
        h ^= (uint64_t)start; h *= prime;
        h ^= (uint64_t)end;   h *= prime;
        if (end > start) pos = (size_t)end;
        else pos = rx_next_pos(s, n, pos);
    }
    *out_matches = matches;
    *out_hash = h;
}

/* first r-xp mapping whose path is our own /proc/self/exe target; good
 * enough since we exec a freshly-built standalone binary each launch. */
static uintptr_t exe_base(void) {
    FILE *f = fopen("/proc/self/maps", "r");
    if (!f) return 0;
    char line[512];
    uintptr_t base = 0;
    while (fgets(line, sizeof line, f)) {
        uintptr_t lo, hi;
        char perms[8];
        if (sscanf(line, "%lx-%lx %7s", &lo, &hi, perms) == 3) {
            if (strchr(perms, 'x') && strstr(line, "r-xp")) {
                /* first executable mapping in address order == our own
                 * text segment for a statically-linked-regex PIE binary
                 * with no other r-xp mapping before it (checked: ld.so's
                 * own text comes later in this box's layout). */
                base = lo;
                break;
            }
        }
    }
    fclose(f);
    return base;
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: %s SUBJECT_FILE [NTRIALS]\n", argv[0]); return 2; }
    int ntrials = (argc >= 3) ? atoi(argv[2]) : 5;
    if (ntrials < 1) ntrials = 1;
    FILE *f = fopen(argv[1], "rb");
    if (!f) { perror("fopen"); return 2; }
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char *buf = malloc((size_t)sz);
    if (fread(buf, 1, (size_t)sz, f) != (size_t)sz) { perror("fread"); return 2; }
    fclose(f);

    long matches = 0;
    uint64_t hash = 0;
    double best_us = -1.0;
    double *all_us = malloc(sizeof(double) * (size_t)ntrials);
    for (int i = 0; i < ntrials; i++) {
        long m; uint64_t h;
        uint64_t t0 = now_ns();
        run_once(buf, (size_t)sz, &m, &h);
        uint64_t t1 = now_ns();
        double us = (double)(t1 - t0) / 1000.0;
        all_us[i] = us;
        if (i == 0) { matches = m; hash = h; }
        else if (m != matches || h != hash) {
            fprintf(stderr, "NONDETERMINISM run %d: matches %ld->%ld hash %llx->%llx\n",
                    i, matches, m, (unsigned long long)hash, (unsigned long long)h);
        }
        if (best_us < 0 || us < best_us) best_us = us;
    }
    uintptr_t base = exe_base();
    uintptr_t fn = (uintptr_t)(void*)rx_search;
    uintptr_t bufaddr = (uintptr_t)(void*)buf;
    printf("matches=%ld hash=%016llx best_us=%.3f "
           "exe_base=0x%lx fn_addr=0x%lx fn_off=0x%lx fn_mod64=%lu fn_mod2m=%lu "
           "buf_addr=0x%lx buf_mod64=%lu buf_mod4096=%lu all_us=",
           matches, (unsigned long long)hash, best_us,
           (unsigned long)base, (unsigned long)fn, (unsigned long)(fn - base),
           (unsigned long)(fn % 64), (unsigned long)(fn % 2097152),
           (unsigned long)bufaddr, (unsigned long)(bufaddr % 64), (unsigned long)(bufaddr % 4096));
    for (int i = 0; i < ntrials; i++) printf("%s%.3f", i ? "," : "", all_us[i]);
    printf("\n");
    free(all_us);
    free(buf);
    return 0;
}
