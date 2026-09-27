/* U6 CONTROL: does glibc's OWN regcomp()/regexec() (the reference POSIX
 * ERE implementation on this box, <regex.h>, REG_EXTENDED) parse
 * `[\x80-\xff]{2,4}` the SAME way TRE does?
 *
 * Manager review (2026-09-27) flagged that POSIX.1-2017 XBD 9.3.5 says
 * plainly: "The special characters '.', '*', '[', and '\\' shall lose
 * their special meaning within a bracket expression." If glibc's own
 * regcomp -- which nobody would call a broken POSIX implementation --
 * shows the identical case A/case B split repro.c finds in TRE, that is
 * strong, independent confirmation that TRE's behaviour is CONFORMING,
 * not a TRE-specific defect: this control links ONLY <regex.h> (the
 * glibc system header), never TRE, never anything from repro.c.
 *
 * Build: gcc -O2 -std=gnu11 control_glibc.c -o control_glibc
 *   (no -ltre, no -l anything -- regcomp/regexec are in libc itself)
 */

#include <regex.h>
#include <stdio.h>
#include <string.h>

static int try_match(const char *pat, const char *subj, int *so, int *eo) {
    regex_t re;
    int rc = regcomp(&re, pat, REG_EXTENDED);
    if (rc != 0) {
        char buf[256];
        regerror(rc, &re, buf, sizeof(buf));
        fprintf(stderr, "regcomp(\"%s\") failed (code %d): %s\n", pat, rc, buf);
        return -2;
    }
    /* glibc's regexec takes a NUL-terminated string with no explicit
     * length argument -- fine here, neither subject below has an
     * embedded NUL. */
    regmatch_t m[1];
    rc = regexec(&re, subj, 1, m, 0);
    regfree(&re);
    if (rc == 0) {
        *so = (int)m[0].rm_so;
        *eo = (int)m[0].rm_eo;
        return 1;
    }
    return 0;
}

int main(void) {
    const char *pat = "[\\x80-\\xff]{2,4}";

    const char *a = "GET /products?category=shoes&sort=price";
    int a_so = -1, a_eo = -1;
    int a_matched = try_match(pat, a, &a_so, &a_eo);

    const char *b = "\x81\x82"; /* two raw high bytes, no embedded NUL */
    int b_so = -1, b_eo = -1;
    int b_matched = try_match(pat, b, &b_so, &b_eo);

    if (a_matched < 0 || b_matched < 0) return 2;

    printf("case A (\"%s\"): glibc=%s", a, a_matched ? "MATCH" : "nomatch");
    if (a_matched) printf(" [%d,%d)", a_so, a_eo);
    printf("\n");

    printf("case B (0x81 0x82): glibc=%s", b_matched ? "MATCH" : "nomatch");
    if (b_matched) printf(" [%d,%d)", b_so, b_eo);
    printf("\n");

    /* "same parse as TRE" == case A matches (the accidental '0'-'\'
     * range) AND case B does not (0x81/0x82 fall outside it). */
    if (a_matched && !b_matched)
        printf("CONTROL: glibc AGREES with TRE (same POSIX bracket-"
               "literal-backslash parse)\n");
    else
        printf("CONTROL: glibc DISAGREES with TRE (a_matched=%d "
               "b_matched=%d)\n", a_matched, b_matched);
    return 0;
}
