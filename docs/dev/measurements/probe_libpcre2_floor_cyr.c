/* probe.c -- standalone libpcre2 probe for the b102floor lane task.
 *
 * Question: bench/utf8@0.1's `floor` pattern (the literal `~`, matched
 * against a NO-MATCH expectation on every subject) costs ~3.05-3.12x more
 * ns/byte on `t-64k-cyr` (88.3% multi-byte, 36555 chars in 65536 bytes)
 * than on `t-64k-asc` (pure ASCII, 65536 chars in 65536 bytes) on all
 * three libpcre2 routes (dfa/interp/jit) in the committed
 * 2026-09-26-utf8-0.1-*-first-ce658cb7 report. Both subjects are
 * EXACTLY 65536 bytes (subject_facts.tsv), so ns/byte is a fair unit.
 * `~` occurs zero times in either subject (expectations.tsv: nomatch,
 * confirmed independently here with grep -c). Since it never matches,
 * the real driver's find-all loop (testees/pcre2/driver.c) makes exactly
 * ONE match call per subject -- so this single-call cost IS the whole
 * measured cost. This probe isolates: (a) whether PCRE2_UTF is even
 * involved (byte-mode control), (b) whether it is the UTF-8 VALIDATION
 * pass specifically (PCRE2_NO_UTF_CHECK ablation) or something else in
 * the match engine's own scan, on all three routes, plus (c) a
 * find-all-loop control on a common byte (space, 0x20) that matches
 * often on both subjects, replicating the ACTUAL driver's VALIDATE-ONCE
 * behaviour (testees/pcre2/driver.c ~line 516-552: call 1 unchecked,
 * calls 2..n forced PCRE2_NO_UTF_CHECK once call 1 proved validity).
 *
 * Build: gcc -O2 -Wall -o probe probe.c -lpcre2-8
 * libpcre2-8-0 10.46-1build1 (system package, this box; no vendored
 * source in this repo -- ldconfig -p / dpkg -s confirm the version).
 *
 * Usage: ./probe <asc.bin> <cyr.bin>
 * Single-threaded; pin with taskset -c <core> externally.
 */
#define PCRE2_CODE_UNIT_WIDTH 8
#include <pcre2.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define NTRIALS 21

static double now_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec * 1e9 + (double)ts.tv_nsec;
}

static int cmp_double(const void *a, const void *b) {
    double da = *(const double *)a, db = *(const double *)b;
    return (da > db) - (da < db);
}

static double median(double *v, int n) {
    double tmp[64];
    memcpy(tmp, v, n * sizeof(double));
    qsort(tmp, n, sizeof(double), cmp_double);
    return (n % 2) ? tmp[n / 2] : (tmp[n / 2 - 1] + tmp[n / 2]) / 2.0;
}

static unsigned char *slurp(const char *path, size_t *len_out) {
    FILE *f = fopen(path, "rb");
    if (!f) { perror(path); exit(1); }
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char *buf = malloc(sz);
    if (fread(buf, 1, sz, f) != (size_t)sz) { fprintf(stderr, "short read\n"); exit(1); }
    fclose(f);
    *len_out = (size_t)sz;
    return buf;
}

/* one no-match probe call: compiled pattern, subject, whether the call
 * itself carries PCRE2_NO_UTF_CHECK. Returns elapsed ns for ONE call. */
static double time_one_call_interp(pcre2_code *re, const unsigned char *subj, size_t len,
                                    int no_utf_check, int *rc_out) {
    pcre2_match_data *md = pcre2_match_data_create(1, NULL);
    uint32_t opts = no_utf_check ? PCRE2_NO_UTF_CHECK : 0;
    double t0 = now_ns();
    int rc = pcre2_match(re, subj, len, 0, opts, md, NULL);
    double t1 = now_ns();
    *rc_out = rc;
    pcre2_match_data_free(md);
    return t1 - t0;
}

static double time_one_call_jit(pcre2_code *re, const unsigned char *subj, size_t len,
                                 int no_utf_check, int *rc_out) {
    pcre2_match_data *md = pcre2_match_data_create(1, NULL);
    uint32_t opts = no_utf_check ? PCRE2_NO_UTF_CHECK : 0;
    double t0 = now_ns();
    int rc = pcre2_jit_match(re, subj, len, 0, opts, md, NULL);
    double t1 = now_ns();
    *rc_out = rc;
    pcre2_match_data_free(md);
    return t1 - t0;
}

/* testees/pcre2/driver.c's OWN documented shape for the pcre2-jit testee
 * (see its header comment ~line 81): it NEVER calls pcre2_jit_match
 * directly -- do_match's single call site is pcre2_match_8 for BOTH
 * pcre2-interp and pcre2-jit, and pcre2_match() dispatches to the
 * JIT-compiled code internally when present. This function replicates
 * THAT call shape exactly (same function symbol as time_one_call_interp,
 * named separately here only to keep the report legible) -- distinct
 * from time_one_call_jit above, which calls the lower-level
 * pcre2_jit_match() entry point the real testee never uses. */
static double time_one_call_match_after_jit(pcre2_code *re, const unsigned char *subj, size_t len,
                                             int no_utf_check, int *rc_out) {
    return time_one_call_interp(re, subj, len, no_utf_check, rc_out);
}

#define DFA_WS_ELEMS 4096
static double time_one_call_dfa(pcre2_code *re, const unsigned char *subj, size_t len,
                                 int no_utf_check, int *rc_out) {
    pcre2_match_data *md = pcre2_match_data_create(2, NULL);
    int *ws = malloc(sizeof(int) * DFA_WS_ELEMS);
    uint32_t opts = no_utf_check ? PCRE2_NO_UTF_CHECK : 0;
    double t0 = now_ns();
    int rc = pcre2_dfa_match(re, subj, len, 0, opts, md, NULL, ws, DFA_WS_ELEMS);
    double t1 = now_ns();
    *rc_out = rc;
    free(ws);
    pcre2_match_data_free(md);
    return t1 - t0;
}

/* find-all loop for the "common byte" control, replicating the real
 * driver's VALIDATE-ONCE rule: call 1 unchecked (validates if PCRE2_UTF),
 * calls 2..n forced PCRE2_NO_UTF_CHECK once call 1 has proven validity
 * (only meaningful under PCRE2_UTF; a no-op flag under byte mode). */
static double time_findall_interp(pcre2_code *re, const unsigned char *subj, size_t len,
                                   int utf_mode, int *nmatches_out) {
    pcre2_match_data *md = pcre2_match_data_create(1, NULL);
    size_t pos = 0;
    int n = 0;
    int validated = !utf_mode; /* byte mode needs no validation */
    double t0 = now_ns();
    while (pos <= len) {
        uint32_t opts = validated ? PCRE2_NO_UTF_CHECK : 0;
        int rc = pcre2_match(re, subj, len, pos, opts, md, NULL);
        if (utf_mode && !validated) validated = 1; /* call 1 proved it, if it didn't error */
        if (rc < 0) break;
        PCRE2_SIZE *ov = pcre2_get_ovector_pointer(md);
        n++;
        size_t match_end = ov[1];
        pos = (match_end > pos) ? match_end : pos + 1; /* byte-mode advance; control is ASCII-safe */
    }
    double t1 = now_ns();
    pcre2_match_data_free(md);
    *nmatches_out = n;
    return t1 - t0;
}

typedef struct { const char *label; double median_ns; double npb; int rc; int trials; } Row;

static void run_no_match_suite(const char *subj_label, const unsigned char *subj, size_t len,
                                const char *pat, int with_utf) {
    int errcode; PCRE2_SIZE erroff;
    uint32_t copts = with_utf ? PCRE2_UTF : 0;
    pcre2_code *re = pcre2_compile((PCRE2_SPTR)pat, PCRE2_ZERO_TERMINATED, copts,
                                    &errcode, &erroff, NULL);
    if (!re) {
        PCRE2_UCHAR buf[256];
        pcre2_get_error_message(errcode, buf, sizeof(buf));
        fprintf(stderr, "compile failed for '%s' (utf=%d): %s\n", pat, with_utf, buf);
        exit(1);
    }
    int jit_rc = pcre2_jit_compile(re, PCRE2_JIT_COMPLETE);
    int have_jit = (jit_rc == 0);

    double v[NTRIALS];

    /* interp, checked (real UTF-check cost included when with_utf) */
    for (int i = 0; i < NTRIALS; i++) { int rc; v[i] = time_one_call_interp(re, subj, len, 0, &rc); }
    double m_interp_check = median(v, NTRIALS);

    /* interp, PCRE2_NO_UTF_CHECK forced (ablate the validation pass) */
    for (int i = 0; i < NTRIALS; i++) { int rc; v[i] = time_one_call_interp(re, subj, len, 1, &rc); }
    double m_interp_nocheck = median(v, NTRIALS);

    double m_dfa_check = -1, m_dfa_nocheck = -1;
    for (int i = 0; i < NTRIALS; i++) { int rc; v[i] = time_one_call_dfa(re, subj, len, 0, &rc); }
    m_dfa_check = median(v, NTRIALS);
    for (int i = 0; i < NTRIALS; i++) { int rc; v[i] = time_one_call_dfa(re, subj, len, 1, &rc); }
    m_dfa_nocheck = median(v, NTRIALS);

    double m_jit_check = -1, m_jit_nocheck = -1;
    double m_jitviamatch_check = -1, m_jitviamatch_nocheck = -1;
    if (have_jit) {
        for (int i = 0; i < NTRIALS; i++) { int rc; v[i] = time_one_call_jit(re, subj, len, 0, &rc); }
        m_jit_check = median(v, NTRIALS);
        for (int i = 0; i < NTRIALS; i++) { int rc; v[i] = time_one_call_jit(re, subj, len, 1, &rc); }
        m_jit_nocheck = median(v, NTRIALS);
        for (int i = 0; i < NTRIALS; i++) { int rc; v[i] = time_one_call_match_after_jit(re, subj, len, 0, &rc); }
        m_jitviamatch_check = median(v, NTRIALS);
        for (int i = 0; i < NTRIALS; i++) { int rc; v[i] = time_one_call_match_after_jit(re, subj, len, 1, &rc); }
        m_jitviamatch_nocheck = median(v, NTRIALS);
    }

    printf("%-10s %-6s utf=%d  interp_check=%10.1f ns (%.6f ns/B)  interp_nocheck=%10.1f ns (%.6f ns/B)  "
           "dfa_check=%10.1f ns (%.6f ns/B)  dfa_nocheck=%10.1f ns (%.6f ns/B)  "
           "jit_direct_check=%10.1f ns (%.6f ns/B)  jit_direct_nocheck=%10.1f ns (%.6f ns/B)  "
           "jit_via_match_check=%10.1f ns (%.6f ns/B)  jit_via_match_nocheck=%10.1f ns (%.6f ns/B)  have_jit=%d\n",
           subj_label, pat, with_utf,
           m_interp_check, m_interp_check / len, m_interp_nocheck, m_interp_nocheck / len,
           m_dfa_check, m_dfa_check / len, m_dfa_nocheck, m_dfa_nocheck / len,
           m_jit_check, m_jit_check / len, m_jit_nocheck, m_jit_nocheck / len,
           m_jitviamatch_check, m_jitviamatch_check / len, m_jitviamatch_nocheck, m_jitviamatch_nocheck / len,
           have_jit);

    pcre2_code_free(re);
}

static void run_control_findall(const char *subj_label, const unsigned char *subj, size_t len,
                                 const char *pat, int with_utf) {
    int errcode; PCRE2_SIZE erroff;
    uint32_t copts = with_utf ? PCRE2_UTF : 0;
    pcre2_code *re = pcre2_compile((PCRE2_SPTR)pat, PCRE2_ZERO_TERMINATED, copts,
                                    &errcode, &erroff, NULL);
    if (!re) { fprintf(stderr, "control compile failed\n"); exit(1); }

    double v[NTRIALS]; int n = -1;
    for (int i = 0; i < NTRIALS; i++) v[i] = time_findall_interp(re, subj, len, with_utf, &n);
    double m = median(v, NTRIALS);
    printf("%-10s %-6s utf=%d  findall_interp=%10.1f ns (%.6f ns/B)  nmatches=%d\n",
           subj_label, pat, with_utf, m, m / len, n);
    pcre2_code_free(re);
}

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: %s <asc.bin> <cyr.bin>\n", argv[0]); return 1; }
    size_t alen, clen;
    unsigned char *abuf = slurp(argv[1], &alen);
    unsigned char *cbuf = slurp(argv[2], &clen);

    uint32_t v;
    pcre2_config(PCRE2_CONFIG_VERSION, NULL); /* touch to confirm link works */
    char vbuf[64]; pcre2_config(PCRE2_CONFIG_VERSION, vbuf);
    printf("# libpcre2-8 version (PCRE2_CONFIG_VERSION): %s\n", vbuf);
    pcre2_config(PCRE2_CONFIG_JIT, &v);
    printf("# JIT support: %u\n", v);
    printf("# t-64k-asc.bin: %zu bytes; t-64k-cyr.bin: %zu bytes\n", alen, clen);
    printf("# NTRIALS=%d per cell, median reported\n", NTRIALS);
    printf("#\n# === floor pattern '~' (0 matches on both subjects), single no-match call ===\n");

    run_no_match_suite("asc", abuf, alen, "~", 0);
    run_no_match_suite("cyr", cbuf, clen, "~", 0);
    run_no_match_suite("asc", abuf, alen, "~", 1);
    run_no_match_suite("cyr", cbuf, clen, "~", 1);

    printf("#\n# === control pattern ' ' (space, common byte, matches often), find-all loop, VALIDATE-ONCE ===\n");
    run_control_findall("asc", abuf, alen, " ", 0);
    run_control_findall("cyr", cbuf, clen, " ", 0);
    run_control_findall("asc", abuf, alen, " ", 1);
    run_control_findall("cyr", cbuf, clen, " ", 1);

    return 0;
}
