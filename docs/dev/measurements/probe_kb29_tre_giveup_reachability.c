/* SCRATCH measurement only (KB-29's TRE reachability question,
 * docs/dev/known_issues.md, lane b98kb29): does testees/tre/driver.c's
 * find-all loop's SECOND (or later) tre_regnexecb() call ever return a
 * genuine mid-loop give-up (any reg_errcode_t other than REG_OK/
 * REG_NOMATCH -- REG_ESPACE is the only one TRE's own source can return
 * from an EXEC call, never a syntax code)?
 *
 * Reproduces driver.c's own find-all shape directly against libtre
 * (compile once, then repeated tre_regnexecb calls advancing `pos` by
 * KB-17's rule), with one MARKER line to stderr around each call so
 * this file's own probe_kb29_tre_failmalloc.c interposer (LD_PRELOAD)
 * can report exactly how many malloc/calloc/realloc calls happen inside
 * each bracketed phase (compile / call 1 / call 2).
 *
 * argv: <pattern> <b-run-length> [nmatch]
 * Subject is always "Xa" + <b-run-length> 'b' bytes (no trailing
 * terminator for the pattern's own backreference-closing literal) so
 * call 1 (pos 0) matches the leading "X" trivially and call 2 (pos 1)
 * is where the pattern's own backtracking machinery -- IF the pattern
 * carries a backreference, which is what routes TRE to its backtracking
 * matcher at all (testees/tre/CLAUDE.md's own `automaton_class` section)
 * -- runs against the "a" + b-run. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <tre/tre.h>

int main(int argc, char **argv) {
    if (argc < 3) {
        fprintf(stderr, "usage: %s <pattern> <b-run-length> [nmatch]\n", argv[0]);
        return 2;
    }
    const char *pat = argv[1];
    long blen = strtol(argv[2], NULL, 10);
    int nmatch = argc > 3 ? atoi(argv[3]) : 8;
    if (nmatch > 32) nmatch = 32;

    fprintf(stderr, "MARK before-compile\n");
    regex_t re;
    int rc = tre_regncompb(&re, pat, strlen(pat), REG_EXTENDED);
    fprintf(stderr, "MARK after-compile rc=%d\n", rc);
    if (rc != REG_OK) {
        char m[256];
        tre_regerror(rc, &re, m, sizeof m);
        printf("compile failed: %d %s\n", rc, m);
        return 1;
    }
    printf("has_backrefs=%d\n", tre_have_backrefs(&re));

    char *subj = malloc((size_t)blen + 3);
    subj[0] = 'X';
    subj[1] = 'a';
    memset(subj + 2, 'b', (size_t)blen);
    subj[blen + 2] = 0;

    regmatch_t pmatch[32];
    fprintf(stderr, "MARK before-call-1\n");
    rc = tre_regnexecb(&re, subj, 1, (size_t)nmatch, pmatch, 0);
    fprintf(stderr, "MARK after-call-1 rc=%d\n", rc);
    printf("call1 rc=%d\n", rc);

    fprintf(stderr, "MARK before-call-2\n");
    rc = tre_regnexecb(&re, subj + 1, (size_t)(blen + 1), (size_t)nmatch,
                        pmatch, REG_NOTBOL);
    fprintf(stderr, "MARK after-call-2 rc=%d\n", rc);
    if (rc == REG_OK)
        printf("call2 MATCH [%ld,%ld)\n", (long)pmatch[0].rm_so,
               (long)pmatch[0].rm_eo);
    else if (rc == REG_NOMATCH)
        printf("call2 NOMATCH\n");
    else {
        char m[256];
        tre_regerror(rc, &re, m, sizeof m);
        printf("call2 GIVEUP code=%d msg=%s\n", rc, m);
    }
    free(subj);
    return 0;
}
