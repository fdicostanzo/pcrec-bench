/* U6 repro: TRE 0.9.0 (tre_regncompb, byte mode) mis-parses a `\xHH`
 * hex-byte escape INSIDE a bracket expression `[...]` as a literal
 * backslash followed by literal characters, rather than as the same
 * hex escape TRE itself recognises OUTSIDE a bracket expression.
 *
 * Pattern under test: `[\x80-\xff]{2,4}` -- "two to four consecutive
 * high (non-ASCII) bytes", a common byte-oriented idiom (this exact
 * spelling is a real pattern in pcrec-bench's capability set,
 * bench/capability/patterns/high-byte-run.rx). Every other engine in
 * that project's roster (libpcre2, pcrec, oniguruma, RE2, vectorscan)
 * parses it as intended: match two to four bytes each in [0x80,0xFF].
 *
 * What TRE actually compiles it to (established below AND by reading
 * TRE 0.9.0's lib/tre-parse.c: tre_parse_bracket_items(), lines ~256-365,
 * builds bracket-expression ranges directly off the raw characters with
 * NO escape processing at all -- contrast the top-level atom parser's
 * `case L'x':` case a thousand lines later, which DOES recognise
 * `\xHH`, but is never consulted while inside `[...]`): the bracket
 * content "\x80-\xff" is read as the literal character sequence
 *   \  x  8  0  -  \  x  f  f
 * A '-' between two ordinary characters forms a range, so this becomes
 * the range '0'-'\' (0x30-0x5C) plus the two standalone literals 'x'
 * (0x78) and 'f' (0x66, already inside the range) -- nothing to do
 * with high bytes at all. The range 0x30-0x5C alone covers every ASCII
 * digit, ':;<=>?@', and 'A'-'Z' plus '[' '\', so ordinary ASCII text
 * with 2-4 consecutive such characters (e.g. "GET", any HTTP verb,
 * most identifiers) spuriously MATCHES, while genuine high-byte pairs
 * (0x81 0x82, outside 0x30-0x5C) correctly do NOT.
 *
 * This is a single self-contained reproduction using only <tre/tre.h>
 * and libtre (`-ltre`) -- the same header and link line
 * pcrec-bench's own testees/tre/driver.c uses (`tre_regncompb`/
 * `tre_regnexecb`, REG_EXTENDED, no REG_NEWLINE). No pcrec-bench code
 * is linked or executed.
 *
 * Build: gcc -O2 -std=gnu11 repro.c -ltre -o repro   (see run.sh)
 */

#include <stdio.h>
#include <string.h>
#include <tre/tre.h>

/* one call: compile PAT, match against (SUBJ, LEN), report [so,eo) or -1 */
static int try_match(const char *pat, const char *subj, size_t len,
                      int *so, int *eo) {
    regex_t re;
    int rc = tre_regncompb(&re, pat, strlen(pat), REG_EXTENDED);
    if (rc != 0) {
        char buf[256];
        tre_regerror(rc, &re, buf, sizeof(buf));
        fprintf(stderr, "tre_regncompb(\"%s\") failed (code %d): %s\n",
                pat, rc, buf);
        return -2;
    }
    regmatch_t m[1];
    rc = tre_regnexecb(&re, subj, len, 1, m, 0);
    tre_regfree(&re);
    if (rc == 0) {
        *so = (int)m[0].rm_so;
        *eo = (int)m[0].rm_eo;
        return 1;
    }
    return 0;
}

int main(void) {
    const char *pat = "[\\x80-\\xff]{2,4}";

    /* Case A: plain ASCII text with no byte >= 0x80 at all.
     * Oracle (libpcre2 10.46, PCRE2_UTF unset -- byte mode, same as
     * this project's pcre2-interp/pcre2-jit testees): NOMATCH. */
    const char *a = "GET /products?category=shoes&sort=price";
    int a_so = -1, a_eo = -1;
    int a_matched = try_match(pat, a, strlen(a), &a_so, &a_eo);

    /* Case B: the genuine high-byte pair the pattern is meant to catch.
     * Oracle: MATCH [0,2). */
    unsigned char b[2] = {0x81, 0x82};
    int b_so = -1, b_eo = -1;
    int b_matched = try_match(pat, (const char *)b, sizeof(b), &b_so, &b_eo);

    if (a_matched < 0 || b_matched < 0)
        return 2; /* compile failed -- not the finding under test */

    printf("case A (\"%s\"): tre=%s oracle=nomatch",
           a, a_matched ? "MATCH" : "nomatch");
    if (a_matched)
        printf(" [%d,%d)", a_so, a_eo);
    printf("\n");

    printf("case B (0x81 0x82): tre=%s oracle=match [0,2)",
           b_matched ? "MATCH" : "nomatch");
    if (b_matched)
        printf(" [%d,%d)", b_so, b_eo);
    printf("\n");

    int wrong_a = (a_matched != 0);        /* TRE matches; oracle does not */
    int wrong_b = (b_matched == 0 || b_so != 0 || b_eo != 2); /* TRE misses it */

    if (wrong_a || wrong_b) {
        printf("PRESENT: TRE's [\\x80-\\xff] disagrees with the oracle "
               "(case A wrong=%d, case B wrong=%d)\n", wrong_a, wrong_b);
        return 0;
    }
    printf("ABSENT: both cases agree with the oracle\n");
    return 1;
}
