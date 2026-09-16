/* docs/dev/measurements/accept41_cd371441/fixtures/b7_driver.c
 *
 * A minimal driver for check B7 ("@file:'s bytes are taken raw -- a
 * subject file containing a NUL and invalid UTF-8 reaches the matcher
 * whole"). pcrec's own harness (tests/harness/run.sh) is the intended
 * reader of an @file: case line, but it lives in ~/pcrec, which this
 * project may only READ from (BD2); this driver is OUR OWN, built
 * entirely under our own scratch directory against the generated
 * matcher's own C API (rx_search, docs/spec/match_api.md), so it proves
 * the same fact -- the file's bytes, NUL and high byte included, reach
 * rx_search unmodified -- without writing anything into pcrec's tree.
 * Pattern under test is '.*' (a whole-subject match at (0, len) proves
 * every byte of a short file reached the engine, including a NUL that
 * argv could never carry). See run.sh's B7 section for the exact build
 * and run commands. */
#include <stdio.h>
#include <stdlib.h>
#include "out.h"

int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "usage: %s file\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "rb");
    if (!f) { perror("fopen"); return 2; }
    unsigned char buf[4096];
    size_t n = fread(buf, 1, sizeof buf, f);
    fclose(f);
    ptrdiff_t caps[8][2];
    int rc = rx_search(buf, n, 0, caps);
    printf("subject_len=%zu rc=%d start=%td end=%td\n", n, rc, caps[0][0], caps[0][1]);
    return 0;
}
