/* docs/dev/measurements/probe_tre_bracket_escape_followups.c
 *
 * U6 follow-up (manager review, 2026-09-27): three targeted witnesses
 * over the bracket-escape census (probe_tre_bracket_escape_census.py),
 * picked to show the mechanism is NOT uniformly harmful or uniformly
 * broken -- some real corpus idioms are "coincidentally safe" under
 * TRE's POSIX (backslash-not-special) bracket parse, others are not.
 * Self-contained: <tre/tre.h> + -ltre only.
 *
 * (1) bench/bounded/patterns/csv5.rx: `(?:[^,\n]{0,32},){4}[^,\n]{0,32}`.
 *     `[^,\n]` is meant to exclude comma-or-newline. Under TRE's literal
 *     parse it excludes {',', '\\', 'n'} instead (no range: no '-' in
 *     the content) -- a REAL newline byte is NOT excluded, so the class
 *     crosses embedded newlines. bench/bounded's own committed subjects
 *     (checked separately, `grep -c` over subjects/*) contain NO
 *     embedded newline today, so this is DORMANT for the current corpus,
 *     not a live wrong answer -- but a real semantic gap if the set ever
 *     grows multi-line subjects, or if csv5-shaped patterns are reused
 *     elsewhere. tre-default has NEVER been run against bench/bounded
 *     (no store or scratch record exists), so there is no "wrong
 *     TODAY" answer to report for this one either way.
 *
 * (2) bench/capability/patterns/codegrammar-flat.rx (and
 *     winpath-near-miss.rx): `[^"\\]` / `[^<>:"/\\|?*]` -- the common
 *     "escape the backslash" idiom, `\\` (TWO raw pattern bytes, one
 *     PCRE-escaped backslash). Under TRE's literal parse this reads as
 *     TWO literal backslash characters, which collapse to the SAME set
 *     as one -- so the class ends up meaning exactly what the PCRE
 *     author intended, BY COINCIDENCE. The store confirms this
 *     (capability@0.1, both patterns: n_wrong=0 on every measured
 *     regime) -- this witness demonstrates WHY, standalone.
 *
 * (3) bench/capability/patterns/tag-pair-match.rx:
 *     `<([a-zA-Z][\w:-]*)(?:\s[^>]*)?>.*?</\1\s*>` -- `[\w:-]` is meant
 *     to be "word char, colon, or hyphen". Under TRE's literal parse
 *     (no hyphen-as-range here either: '-' is the LAST content char,
 *     so POSIX reads it as literal) the class is {'\\', 'w', ':', '-'}
 *     -- accepts a literal backslash or the letter 'w' as if they were
 *     "word chars", and does NOT accept e.g. digits or most letters
 *     `\w` would. The store shows this bites on 5/75 short-subject-
 *     search trials (n_wrong=5) -- this witness isolates the mechanism
 *     on one hand-built tag name using the accidental members.
 *
 * Build: gcc -O2 -std=gnu11 probe_tre_bracket_escape_followups.c -ltre \
 *          -o probe_tre_bracket_escape_followups
 */

#include <stdio.h>
#include <string.h>
#include <tre/tre.h>

static void trial(const char *label, const char *pat, const char *subj) {
    regex_t re;
    int rc = tre_regncompb(&re, pat, strlen(pat), REG_EXTENDED);
    if (rc != 0) {
        printf("%-46s COMPILE FAILED rc=%d\n", label, rc);
        return;
    }
    regmatch_t m[1];
    rc = tre_regnexecb(&re, subj, strlen(subj), 1, m, 0);
    if (rc == 0)
        printf("%-46s MATCH [%d,%d) = \"%.*s\"\n", label,
               (int)m[0].rm_so, (int)m[0].rm_eo,
               (int)(m[0].rm_eo - m[0].rm_so), subj + m[0].rm_so);
    else
        printf("%-46s nomatch\n", label);
    tre_regfree(&re);
}

int main(void) {
    puts("(1) csv5 [^,\\n] crosses an embedded newline it should exclude:");
    trial("  csv5 vs \"a,b,c,d,e\\nZZZZZZZZZZ\"",
          "(?:[^,\\n]{0,32},){4}[^,\\n]{0,32}",
          "a,b,c,d,e\nZZZZZZZZZZ");
    puts("  (oracle/PCRE reading would stop the class at the newline;\n"
         "   the whole line above is one 20-byte match under TRE)");

    puts("\n(2) [^\"\\\\] / doubled-backslash idiom: coincidentally SAFE:");
    trial("  [^\"\\\\]+ vs \"\\\\\" (a lone backslash byte)",
          "[^\"\\\\]+", "\\");
    trial("  [^\"\\\\]+ vs \"quoted\\\"here\"",
          "[^\"\\\\]+", "quoted\"here");
    puts("  (both a literal backslash byte AND a literal '\"' byte are\n"
         "   correctly EXCLUDED -- the doubled escape happens to mean\n"
         "   the same thing whether or not backslash is special)");

    puts("\n(3) tag-pair-match [\\w:-] accepts accidental members, not \\w:");
    trial("  [\\w:-]+ vs \"w\" (should be a real \\w match anyway)",
          "[\\w:-]+", "w");
    trial("  [\\w:-]+ vs \"5\" (a digit -- \\w should match, TRE's literal set does not)",
          "[\\w:-]+", "5");
    trial("  [\\w:-]+ vs \"\\\\\" (a lone backslash -- \\w should NOT match, TRE's literal set DOES)",
          "[\\w:-]+", "\\");
    return 0;
}
