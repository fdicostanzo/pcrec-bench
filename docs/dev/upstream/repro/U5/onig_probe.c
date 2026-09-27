/* Standalone oniguruma cross-check for the U5 finding: is the
 * super-linear per-byte cost on `\((?:[^()]|(?R))*\)` over text with
 * deliberately-unbalanced paren lines specific to libpcre2, or does a
 * SECOND independent backtracking engine (Oniguruma) show the same
 * shape? Reads a subject file, runs onig_search repeatedly (a manual
 * find-all: advance past each match's end, or +1 on failure) starting
 * from every position 0..len, exactly like a find-all loop, and prints
 * total match count + elapsed match time in microseconds. */
#include <oniguruma.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static double now_us(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1e6 + ts.tv_nsec / 1e3;
}

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: %s <pattern-file> <subject-file>\n", argv[0]); return 2; }
    FILE *pf = fopen(argv[1], "rb");
    if (!pf) { perror("pattern"); return 2; }
    char patbuf[4096];
    size_t patlen = fread(patbuf, 1, sizeof(patbuf), pf);
    fclose(pf);
    while (patlen > 0 && (patbuf[patlen-1] == '\n' || patbuf[patlen-1] == '\r')) patlen--;

    FILE *sf = fopen(argv[2], "rb");
    if (!sf) { perror("subject"); return 2; }
    fseek(sf, 0, SEEK_END);
    long slen = ftell(sf);
    fseek(sf, 0, SEEK_SET);
    unsigned char *subj = malloc(slen);
    if (fread(subj, 1, slen, sf) != (size_t)slen) { perror("read"); return 2; }
    fclose(sf);

    OnigErrorInfo einfo;
    regex_t *reg;
    OnigEncoding enc = ONIG_ENCODING_ASCII;  /* byte mode, matches this bench's own onig-default convention */
    int r = onig_new(&reg, (const UChar*)patbuf, (const UChar*)(patbuf + patlen),
                      ONIG_OPTION_NONE, enc, ONIG_SYNTAX_PERL_NG, &einfo);
    if (r != ONIG_NORMAL) {
        char ebuf[ONIG_MAX_ERROR_MESSAGE_LEN];
        onig_error_code_to_str((UChar*)ebuf, r, &einfo);
        fprintf(stderr, "onig_new failed: %s\n", ebuf);
        return 2;
    }

    OnigRegion *region = onig_region_new();
    double t0 = now_us();
    long pos = 0;
    long nmatches = 0;
    const unsigned char *start = subj, *range = subj + slen, *end = subj + slen;
    while (pos <= slen) {
        int rc = onig_search(reg, subj, end, subj + pos, range, region, ONIG_OPTION_NONE);
        if (rc >= 0) {
            nmatches++;
            long mend = region->end[0];
            pos = (mend > pos) ? mend : pos + 1;
        } else if (rc == ONIG_MISMATCH) {
            pos++;
        } else {
            fprintf(stderr, "onig_search error %d at pos %ld\n", rc, pos);
            break;
        }
    }
    double t1 = now_us();
    printf("matches=%ld elapsed_us=%.1f ns_per_byte=%.4f\n",
           nmatches, t1 - t0, (t1 - t0) * 1000.0 / slen);

    onig_region_free(region, 1);
    onig_free(reg);
    onig_end();
    return 0;
}
