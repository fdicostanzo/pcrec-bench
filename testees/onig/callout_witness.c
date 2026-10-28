/* [B148] L5 THE ONIGURUMA CALLOUT WITNESSES (docs/design/unusual_set_v1.md
 * 3.2; a GATE in tools/check_callouts.py, never a testee). Four facts the
 * callout arms rest on, each printed as `witness<TAB>NAME<TAB>ok|FAIL<TAB>detail`:
 *   contents-spelling  `\b(\d{3})\b(?{1})` compiles under ONIG_SYNTAX_PERL_NG
 *                      and the GLOBAL progress callout fires under plain
 *                      onig_search, contents "1", group 1 readable; a FAIL
 *                      on the first fire moves the match to the next
 *                      candidate (the return-code mapping, ONIG_CALLOUT_FAIL)
 *   name-registration  `(*pbname)` does NOT compile before
 *                      onig_set_callout_of_name registers the name, and does
 *                      (and fires) after -- registration precedes onig_new
 *   high-byte-class    `[\x80-\xff]` under ONIG_ENCODING_ASCII compiles and
 *                      matches the raw byte 0xE9 (a byte set, not a refusal)
 *   G-anchor           `\Gab` searched from offset 3 of "ab ab" matches at 3
 *                      and from offset 2 does not (\G = the search start)
 * Exit 0 iff all four are ok. */
#include <oniguruma.h>
#include <stdio.h>
#include <string.h>

static int fires, fail_first, last_g1s, last_g1e;
static char last_contents[16];

static int progress(OnigCalloutArgs *a, void *u) {
    (void)u;
    const UChar *c = onig_get_contents_by_callout_args(a);
    const UChar *ce = onig_get_contents_end_by_callout_args(a);
    snprintf(last_contents, sizeof last_contents, "%.*s", c ? (int)(ce - c) : 0,
             c ? (const char *)c : "");
    onig_get_capture_range_in_callout(a, 1, &last_g1s, &last_g1e);
    fires++;
    return (fail_first && fires == 1) ? ONIG_CALLOUT_FAIL : ONIG_CALLOUT_SUCCESS;
}

static int by_name(OnigCalloutArgs *a, void *u) {
    (void)a; (void)u;
    fires++;
    return ONIG_CALLOUT_SUCCESS;
}

static int compile(regex_t **r, const char *p, OnigEncoding enc) {
    OnigErrorInfo ei;
    return onig_new(r, (const UChar *)p, (const UChar *)p + strlen(p),
                    ONIG_OPTION_NONE, enc, ONIG_SYNTAX_PERL_NG, &ei);
}

static int search(regex_t *r, const char *s, size_t n, size_t from, int *b) {
    OnigRegion *rg = onig_region_new();
    int rc = onig_search(r, (const UChar *)s, (const UChar *)s + n,
                         (const UChar *)s + from, (const UChar *)s + n, rg,
                         ONIG_OPTION_NONE);
    *b = rc >= 0 ? rg->beg[0] : -1;
    onig_region_free(rg, 1);
    return rc;
}

int main(void) {
    OnigEncoding enc = ONIG_ENCODING_ASCII;
    onig_initialize(&enc, 1);
    int bad = 0, b = -1;
    regex_t *r;

    /* contents-spelling */
    onig_set_progress_callout(progress);
    int rc = compile(&r, "\\b(\\d{3})\\b(?{1})", enc);
    const char *s1 = "x 123 456 y";
    fires = 0; fail_first = 1;
    int sr = rc == ONIG_NORMAL ? search(r, s1, strlen(s1), 0, &b) : -1;
    int ok = rc == ONIG_NORMAL && sr >= 0 && b == 6 && fires == 2
             && !strcmp(last_contents, "1") && last_g1s == 6 && last_g1e == 9;
    printf("witness\tcontents-spelling\t%s\tnew=%d first-fails -> start %d, fires %d, "
           "contents \"%s\", g1 [%d,%d)\n", ok ? "ok" : "FAIL", rc, b, fires,
           last_contents, last_g1s, last_g1e);
    bad += !ok;
    if (rc == ONIG_NORMAL) onig_free(r);
    onig_set_progress_callout(NULL);

    /* name-registration */
    int before = compile(&r, "ab(*pbname)c", enc);
    if (before == ONIG_NORMAL) onig_free(r);
    UChar nm[] = "pbname";
    int reg = onig_set_callout_of_name(enc, ONIG_CALLOUT_TYPE_SINGLE, nm, nm + 6,
                                       ONIG_CALLOUT_IN_PROGRESS, by_name, NULL,
                                       0, NULL, 0, 0);
    int after = compile(&r, "ab(*pbname)c", enc);
    fires = 0;
    sr = after == ONIG_NORMAL ? search(r, "xxabc", 5, 0, &b) : -1;
    ok = before != ONIG_NORMAL && reg >= 0 && after == ONIG_NORMAL && sr >= 0 && b == 2 && fires == 1;
    printf("witness\tname-registration\t%s\tbefore=%d register=%d after=%d match %d fires %d\n",
           ok ? "ok" : "FAIL", before, reg, after, b, fires);
    bad += !ok;
    if (after == ONIG_NORMAL) onig_free(r);

    /* high-byte-class */
    rc = compile(&r, "[\\x80-\\xff]", enc);
    const char s3[] = "caf\xe9!";
    sr = rc == ONIG_NORMAL ? search(r, s3, 5, 0, &b) : -1;
    ok = rc == ONIG_NORMAL && sr >= 0 && b == 3;
    printf("witness\thigh-byte-class\t%s\tnew=%d match at %d\n", ok ? "ok" : "FAIL", rc, b);
    bad += !ok;
    if (rc == ONIG_NORMAL) onig_free(r);

    /* G-anchor */
    rc = compile(&r, "\\Gab", enc);
    int b3 = -1, b2 = -1;
    int r3 = rc == ONIG_NORMAL ? search(r, "ab ab", 5, 3, &b3) : -1;
    int r2 = rc == ONIG_NORMAL ? search(r, "ab ab", 5, 2, &b2) : 0;
    ok = rc == ONIG_NORMAL && r3 >= 0 && b3 == 3 && r2 == ONIG_MISMATCH;
    printf("witness\tG-anchor\t%s\tfrom 3 -> %d, from 2 -> rc %d\n", ok ? "ok" : "FAIL", b3, r2);
    bad += !ok;
    if (rc == ONIG_NORMAL) onig_free(r);

    onig_end();
    return bad ? 1 : 0;
}
