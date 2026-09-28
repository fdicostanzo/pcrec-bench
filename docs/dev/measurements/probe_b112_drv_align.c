/* drv_align.c -- [B112] diagnostic (2): subject-buffer alignment sweep.
 * Same as drv.c (I-114's driver, verbatim timing loop) except the subject
 * buffer is posix_memalign(4096)'d into an oversized block and the search
 * is run against base+OFFSET, OFFSET given on argv. Additive: with OFFSET=0
 * this is byte-for-byte the same access pattern as plain malloc almost
 * always gives (glibc malloc already returns 16-byte-aligned memory for
 * this size; OFFSET=0 here is 4096-aligned, a STRONGER guarantee, so it is
 * its own control row, not identical to drv.c's malloc).
 * argv: SUBJECT_FILE NTRIALS OFFSET
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#include <stdint.h>
#include <time.h>

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

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: %s SUBJECT_FILE [NTRIALS] [OFFSET]\n", argv[0]); return 2; }
    int ntrials = (argc >= 3) ? atoi(argv[2]) : 5;
    if (ntrials < 1) ntrials = 1;
    size_t offset = (argc >= 4) ? (size_t)atol(argv[3]) : 0;
    if (offset > 4095) { fprintf(stderr, "OFFSET must be 0..4095\n"); return 2; }
    FILE *f = fopen(argv[1], "rb");
    if (!f) { perror("fopen"); return 2; }
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fseek(f, 0, SEEK_SET);

    void *base = NULL;
    size_t block = (size_t)sz + 4096;
    if (posix_memalign(&base, 4096, block) != 0) { perror("posix_memalign"); return 2; }
    memset(base, 0, block);
    unsigned char *buf = (unsigned char *)base + offset;
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
    printf("matches=%ld hash=%016llx best_us=%.3f buf_addr=%p buf_mod64=%zu buf_mod4096=%zu all_us=",
           matches, (unsigned long long)hash, best_us, (void*)buf,
           ((size_t)(uintptr_t)buf) % 64, ((size_t)(uintptr_t)buf) % 4096);
    for (int i = 0; i < ntrials; i++) printf("%s%.3f", i ? "," : "", all_us[i]);
    printf("\n");
    free(all_us);
    free(base);
    return 0;
}
