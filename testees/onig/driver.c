/* testees/onig/driver.c -- the Oniguruma batched in-process timing driver.
 *
 * Implements the DRIVER PROTOCOL in pcrecbench/adapters.py verbatim; read
 * that first. This file's own decisions:
 *
 * WHY DIRECT LINKING, NOT dlopen. Unlike testees/pcre2/ (runtime-only box,
 * no -dev package at the time that adapter was written), this box HAS
 * libonig-dev (6.9.10-1build1, `/usr/include/oniguruma.h`, verified
 * byte-identical to the upstream v6.9.10 tag this file's comments cite) --
 * so this driver simply `#include <oniguruma.h>` and links `-lonig`. No
 * hand-declared prototypes, no probed constants: every symbol and value
 * below is the real header's.
 *
 * SYNTAX (testees/onig/CLAUDE.md has the full argument): ONIG_SYNTAX_PERL_NG
 * -- the closest of this version's shipped syntaxes to PCRE (named groups,
 * `\K`, possessive quantifiers, atomic groups, if-else conditionals, `\g`
 * subexp calls, `\p{...}`). `ONIG_SYNTAX_PERL_NT` does not exist in 6.9.10.
 *
 * ENCODING: ONIG_ENCODING_ASCII -- single-byte, `is_valid_mbc_string`
 * unconditionally true (src/ascii.c: `onigenc_always_true_is_valid_mbc_
 * string`), so a byte >= 0x80 is a valid one-byte "character" like PCRE2's
 * default 8-bit non-UTF mode, never a decode error. testees/onig/CLAUDE.md
 * states the consequences for `\p{...}` and case folding.
 *
 * COMPILE COST: one phase, `compile` -- `onig_new`, timed in-driver.
 * Oniguruma has no separate JIT step (an interpretive backtracking engine,
 * the same execution-model class as pcre2-interp).
 *
 * TWO FORMS, ONE INVOCATION EACH (`--form plain|whole-subject`): Oniguruma
 * has no runtime end-anchor option (no PCRE2_ENDANCHORED equivalent), so
 * the `match` regime (anchored AND end-anchored) is answered on a SECOND
 * artifact compiled from `(?:<pattern>)\z` (the SAME bytes
 * `pcrecbench.record.whole_subject_text` produces for pcrec -- `\z` is
 * ONIG_SYN_OP_ESC_AZ_BUF_ANCHOR, present under Perl_NG, confirmed live in
 * src/regparse.c). `onig_match` (not `onig_search`) supplies the START
 * anchor: it matches AT the given position only, never scanning -- so
 * `--form whole-subject` always calls `onig_match` at offset 0, and the
 * wrapper's own `\z` supplies the end anchor. `--form plain` always calls
 * `onig_search` (unanchored, leftmost). Adapter.compile() runs this driver
 * TWICE per pattern, once per form -- the DRIVER PROTOCOL's `compile` line
 * carries no form column, so form separation is the ADAPTER's job, exactly
 * as pcrec's own two-artifact model does it.
 *
 * consumed_length: the length argument (`end - str`) this driver passed
 * onig_search/onig_match and Oniguruma accepted -- i.e. the whole subject.
 * Oniguruma exposes no scan high-water mark either (same convention as
 * testees/pcre2/CLAUDE.md states for pcre2: "no byte was withheld or
 * refused", never "the engine looked at every byte").
 *
 * GAVE-UP CODES ([measured] against this box's /usr/include/oniguruma.h +
 * a direct read of src/regparse.c and src/regexec.c, v6.9.10, this lane,
 * 2026-09-17): four MATCH-TIME resource-limit codes, raised in regexec.c --
 *   ONIGERR_MATCH_STACK_LIMIT_OVER           (-15)
 *   ONIGERR_RETRY_LIMIT_IN_MATCH_OVER        (-17)  DEFAULT budget
 *                                                    10,000,000 (regint.h
 *                                                    DEFAULT_RETRY_LIMIT_IN_
 *                                                    MATCH) -- NOT
 *                                                    unlimited: a
 *                                                    catastrophic-
 *                                                    backtracking witness
 *                                                    CAN give up under
 *                                                    onig-default with no
 *                                                    special config.
 *   ONIGERR_RETRY_LIMIT_IN_SEARCH_OVER       (-18)
 *   ONIGERR_SUBEXP_CALL_LIMIT_IN_SEARCH_OVER (-19)
 * Deliberately NOT in that set:
 *   ONIGERR_MEMORY (-5) -- an allocation failure, not a configured budget
 *     (same reasoning as pcre2's -48; the adapter classifies it `crashed`).
 *   ONIGERR_PARSE_DEPTH_LIMIT_OVER (-16) -- raised in src/regparse.c, i.e.
 *     at COMPILE time (a parse-nesting-depth budget, DEFAULT 4096), so the
 *     adapter's ordinary `did-not-compile` path handles it; it can never
 *     reach this driver's match loop.
 * `onig_error_code_to_str` supplies the message text for every code this
 * driver did not expect, so a code the header adds later still prints a
 * real diagnostic instead of a blank one.
 */

#include <oniguruma.h>

#include <errno.h>
#include <setjmp.h>
#include <signal.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define ONIG_DRIVER_SYNTAX  ONIG_SYNTAX_PERL_NG
#define ONIG_DRIVER_ENCODING ONIG_ENCODING_ASCII

static double now(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (double)ts.tv_sec + (double)ts.tv_nsec / 1e9;
}

static void die(const char *what) {
    printf("error\t%s\n", what);
    fflush(stdout);
    exit(2);
}

static unsigned char *slurp(const char *path, size_t *sz_out) {
    FILE *f = fopen(path, "rb");
    if (!f) { printf("error\tfopen %s: %s\n", path, strerror(errno)); return NULL; }
    if (fseek(f, 0, SEEK_END) != 0) { fclose(f); return NULL; }
    long sz = ftell(f);
    if (sz < 0) { fclose(f); return NULL; }
    rewind(f);
    unsigned char *buf = malloc((size_t)sz + 1);
    if (!buf) { fclose(f); return NULL; }
    if (sz > 0 && fread(buf, 1, (size_t)sz, f) != (size_t)sz) {
        fclose(f); free(buf); return NULL;
    }
    buf[sz] = 0;
    fclose(f);
    *sz_out = (size_t)sz;
    return buf;
}

/* ------------------------------------------------- the per-subject alarm */

static sigjmp_buf timeout_jmp;
static volatile sig_atomic_t timed_out;

static void on_alarm(int sig) {
    (void)sig;
    timed_out = 1;
    siglongjmp(timeout_jmp, 1);
}

/* ---------------------------------------------------------------- subjects */

typedef struct {
    char          *id;
    unsigned char *buf;
    size_t         len;
} subject;

/* noinline: gcc otherwise inlines this into main(), where sigsetjmp lives,
 * and warns that its locals `might be clobbered by longjmp` -- the same
 * note testees/pcre2/driver.c carries for the identical reason. */
__attribute__((noinline))
static subject *load_list(const char *path, size_t *n_out) {
    FILE *f = fopen(path, "r");
    if (!f) return NULL;
    size_t cap = 64, n = 0;
    subject *v = malloc(cap * sizeof *v);
    char line[8192];
    while (fgets(line, sizeof line, f)) {
        char *nl = strchr(line, '\n');
        if (nl) *nl = 0;
        if (!*line) continue;
        char *tab = strchr(line, '\t');
        if (!tab) continue;
        *tab = 0;
        if (n == cap) { cap *= 2; v = realloc(v, cap * sizeof *v); }
        v[n].id = strdup(line);
        v[n].buf = slurp(tab + 1, &v[n].len);
        if (!v[n].buf) { fclose(f); free(v); return NULL; }
        n++;
    }
    fclose(f);
    *n_out = n;
    return v;
}

/* ------------------------------------------------------------------- main */

static void emit_caps(OnigRegion *region, char *out, size_t outcap) {
    size_t off = 0;
    out[0] = 0;
    for (int i = 1; i < region->num_regs; i++) {
        long s = (region->beg[i] == ONIG_REGION_NOTPOS) ? -1 : (long)region->beg[i];
        long e = (region->end[i] == ONIG_REGION_NOTPOS) ? -1 : (long)region->end[i];
        int k = snprintf(out + off, outcap - off, "%s%ld:%ld",
                         i > 1 ? "," : "", s, e);
        if (k < 0 || (size_t)k >= outcap - off) break;
        off += (size_t)k;
    }
    if (!out[0]) { out[0] = '-'; out[1] = 0; }
}

int main(int argc, char **argv) {
    const char *pattern_path = NULL, *list_path = NULL, *mode = "search";
    const char *form = "plain";
    /* `volatile` on everything the per-subject sigsetjmp/siglongjmp pair can
     * see across the jump -- C11 6.8.6.1's indeterminate-after-longjmp rule,
     * the same note testees/pcre2/driver.c carries. */
    volatile long iters = 1, subject_timeout = 0, skip = 0;
    long compile_trials = 1;
    volatile int find_all = 0;

    for (int i = 1; i < argc; i++) {
        const char *a = argv[i];
        if (!strcmp(a, "--pattern") && i + 1 < argc)        pattern_path = argv[++i];
        else if (!strcmp(a, "--list") && i + 1 < argc)      list_path = argv[++i];
        else if (!strcmp(a, "--mode") && i + 1 < argc)      mode = argv[++i];
        else if (!strcmp(a, "--form") && i + 1 < argc)      form = argv[++i];
        else if (!strcmp(a, "--iters") && i + 1 < argc)     iters = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--compile-trials") && i + 1 < argc) compile_trials = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--subject-timeout") && i + 1 < argc) subject_timeout = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--skip") && i + 1 < argc)      skip = strtol(argv[++i], NULL, 10);
        else if (!strcmp(a, "--find-all"))                  find_all = 1;
        else { printf("error\tunknown argument %s\n", a); return 2; }
    }
    if (!pattern_path) die("--pattern is required");
    if (iters < 1) iters = 1;
    int whole_subject = !strcmp(form, "whole-subject");
    /* `--mode` and `--form` are set TOGETHER by the adapter (`--form
     * whole-subject` iff `--mode match`; testees/onig/adapter.py's
     * `measure()`), because the whole-subject artifact's own `\z` suffix
     * plus this driver's `onig_match`-at-zero already supply BOTH halves
     * of "anchored AND end-anchored" -- there is no second, independent
     * anchoring dial `--mode` could still turn once `--form` is chosen.
     * Accepted (protocol compliance) and cross-checked here rather than
     * silently ignored, so a future adapter bug that decouples the two
     * flags fails LOUDLY instead of quietly measuring the wrong form. */
    if (list_path) {
        int mode_wants_whole = !strcmp(mode, "match");
        if (mode_wants_whole != whole_subject)
            die("--mode and --form disagree (this driver has no anchoring "
                "dial independent of --form)");
    }

    setvbuf(stdout, NULL, _IOLBF, 0);

    OnigEncoding use_encs[1];
    use_encs[0] = ONIG_DRIVER_ENCODING;
    onig_initialize(use_encs, 1);

    {
        char verbuf[64];
        snprintf(verbuf, sizeof verbuf, "%s", onig_version());
        printf("info\tversion\t%s\n", verbuf);
    }
    printf("info\tsyntax\tPERL_NG\n");
    printf("info\tencoding\tASCII\n");
    printf("info\tform\t%s\n", form);

    size_t patlen = 0;
    unsigned char *pat = slurp(pattern_path, &patlen);
    if (!pat) { printf("error\tcannot read pattern %s\n", pattern_path); return 2; }

    /* ---- compile, `compile_trials` times, the one phase timed ---- */
    regex_t *reg = NULL;
    for (long t = 1; t <= compile_trials; t++) {
        OnigErrorInfo einfo;
        regex_t *r = NULL;
        double t0 = now();
        int rc = onig_new(&r, pat, pat + patlen, ONIG_OPTION_DEFAULT,
                          ONIG_DRIVER_ENCODING, ONIG_DRIVER_SYNTAX, &einfo);
        double t1 = now();
        if (rc != ONIG_NORMAL) {
            unsigned char msg[ONIG_MAX_ERROR_MESSAGE_LEN];
            onig_error_code_to_str(msg, rc, &einfo);
            for (unsigned char *p = msg; *p; p++)
                if (*p == '\t' || *p == '\n') *p = ' ';
            printf("error\tonig_new failed (code %d): %s\n", rc, (char *)msg);
            return 3;
        }
        printf("compile\t%ld\tcompile\t%.9f\n", t, t1 - t0);
        if (reg) onig_free(reg);
        reg = r;
    }

    /* engine_metadata, `pattern`-scoped (record_schema.md 7 rule 2):
     * declared in testees/onig/adapter.py -- an undeclared pair is a
     * validator error, so the two lists move together. */
    printf("info\tcapturecount\t%d\n", onig_number_of_captures(reg));
    printf("info\tnames\t%d\n", onig_number_of_names(reg));

    if (!list_path) { fflush(stdout); return 0; }   /* compile-only run */

    size_t nsub = 0;
    subject *subs = load_list(list_path, &nsub);
    if (!subs) { printf("error\tcannot read subject list %s\n", list_path); return 2; }

    OnigRegion *region = onig_region_new();
    if (!region) { printf("error\tonig_region_new failed\n"); return 2; }

    struct sigaction sa;
    memset(&sa, 0, sizeof sa);
    sa.sa_handler = on_alarm;
    sigaction(SIGALRM, &sa, NULL);

    char caps[4096];

    for (size_t i = (size_t)skip; i < nsub; i++) {
        subject *s = &subs[i];
        volatile long   first_s = -1, first_e = -1, nmatch = -1;
        volatile int    rc_final = ONIG_MISMATCH;
        volatile double elapsed = 0.0;

        timed_out = 0;
        if (sigsetjmp(timeout_jmp, 1) == 0) {
            if (subject_timeout > 0) alarm((unsigned)subject_timeout);
            double t0 = now();
            for (long it = 0; it < iters; it++) {
                first_s = first_e = -1;
                if (find_all) {
                    size_t pos = 0;
                    long   count = 0;
                    for (;;) {
                        int rc = whole_subject
                            ? onig_match(reg, s->buf, s->buf + s->len,
                                        s->buf + pos, region, ONIG_OPTION_NONE)
                            : onig_search(reg, s->buf, s->buf + s->len,
                                         s->buf + pos, s->buf + s->len,
                                         region, ONIG_OPTION_NONE);
                        if (rc < 0) { if (count == 0) rc_final = rc; break; }
                        if (first_s < 0) {
                            first_s = (long)region->beg[0];
                            first_e = (long)region->end[0];
                            rc_final = rc;
                        }
                        count++;
                        /* pcrec match_api.md S3.1's find-all advance: off the
                         * match's own reported START, never off the scan
                         * position -- KB-17, the same rule testees/pcre2/
                         * driver.c applies. */
                        size_t start = (size_t)region->beg[0];
                        size_t end = (size_t)region->end[0];
                        pos = (end > start) ? end : start + 1;
                        if (whole_subject) break; /* onig_match: one position only */
                        if (pos > s->len) break;
                    }
                    nmatch = count;
                } else {
                    int rc = whole_subject
                        ? onig_match(reg, s->buf, s->buf + s->len, s->buf,
                                    region, ONIG_OPTION_NONE)
                        : onig_search(reg, s->buf, s->buf + s->len, s->buf,
                                     s->buf + s->len, region, ONIG_OPTION_NONE);
                    rc_final = rc;
                    if (rc >= 0) {
                        first_s = (long)region->beg[0];
                        first_e = (long)region->end[0];
                    }
                }
            }
            elapsed = now() - t0;
            if (subject_timeout > 0) alarm(0);
        }

        if (timed_out) {
            printf("subject\t%s\ttimedout\t-\t-\t0\t-\t%ld\t%.9f\t-\t-\n",
                   s->id, (long)iters, (double)elapsed);
            continue;
        }

        char answerbuf[256];
        const char *answer;
        char sbuf[32], ebuf[32], nbuf[32];
        int ncaps = 0;

        if (first_s >= 0) {
            answer = "match";
            emit_caps(region, caps, sizeof caps);
            ncaps = region->num_regs > 0 ? region->num_regs - 1 : 0;
            snprintf(sbuf, sizeof sbuf, "%ld", (long)first_s);
            snprintf(ebuf, sizeof ebuf, "%ld", (long)first_e);
        } else {
            strcpy(sbuf, "-");
            strcpy(ebuf, "-");
            caps[0] = '-'; caps[1] = 0;
            if (rc_final == ONIG_MISMATCH) {
                answer = "nomatch";
            } else {
                /* `giveup:<code>:<oniguruma's own message>`. The message
                 * comes from onig_error_code_to_str rather than a table in
                 * this file, so it cannot fall out of step with the
                 * library; the harness/adapter classifies on the CODE. */
                unsigned char emsg[ONIG_MAX_ERROR_MESSAGE_LEN];
                onig_error_code_to_str(emsg, rc_final);
                for (unsigned char *p = emsg; *p; p++)
                    if (*p == '\t' || *p == '\n') *p = ' ';
                snprintf(answerbuf, sizeof answerbuf, "giveup:%d:%s",
                         (int)rc_final, (char *)emsg);
                answer = answerbuf;
            }
        }
        if (find_all && nmatch >= 0) snprintf(nbuf, sizeof nbuf, "%ld", (long)nmatch);
        else strcpy(nbuf, "-");

        /* consumed_length: the length argument onig_search/onig_match was
         * given and accepted. See this file's header and
         * testees/onig/CLAUDE.md. */
        printf("subject\t%s\t%s\t%s\t%s\t%d\t%zu\t%ld\t%.9f\t%s\t%s\n",
               s->id, answer, sbuf, ebuf, ncaps,
               s->len, (long)iters, (double)elapsed, nbuf, caps);
    }

    onig_region_free(region, 1);
    onig_free(reg);
    onig_end();
    fflush(stdout);
    return 0;
}
