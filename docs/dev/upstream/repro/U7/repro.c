/* U7 repro: vectorscan (Hyperscan-ABI-compatible) refuses a `(?x)`
 * free-spacing pattern whose FINAL line is an unterminated `#` comment
 * (no trailing newline), with `hs_compile()` code -4 "Unterminated
 * comment.", where PCRE itself defines a `(?x)` `#` comment as ending
 * at a newline OR AT THE END OF THE PATTERN -- so the plain form is
 * well-formed PCRE and every other engine on pcrec-bench's roster
 * (libpcre2 10.46, pcrec, oniguruma 6.9.10, rust-regex 1.13.1) accepts
 * it. Real corpus witnesses:
 * bench/capability/patterns/wild-codegrammar-json-number-extended.rx
 * and .../wild-codegrammar-json-stringcontent-escape.rx, both `(?x)`
 * patterns literally ending "...portion optional" with NO trailing
 * newline byte (verified with `xxd`/`cat -A`).
 *
 * A second, harness-relevant observation this repro also demonstrates:
 * simply APPENDING one newline byte after the pattern text is enough
 * to make vectorscan accept it (the newline terminates the open `#`
 * comment) -- which is exactly what pcrec-bench's own whole-subject
 * wrap spelling does incidentally for a free-spacing pattern
 * (record_schema.md §5 ADDITIONS 3), so the SAME pattern text compiles
 * under one wrap and refuses under another. That split is a harness
 * observation, included here for completeness; the finding proper is
 * the plain-form refusal itself.
 *
 * Self-contained: only <hs/hs.h> and libvectorscan (`-lhs`), the same
 * header and link line pcrec-bench's own testees/vectorscan/driver.c
 * uses (`#include <hs/hs.h>`, direct-linked, no dlopen). No
 * pcrec-bench code is linked or executed.
 *
 * Build: gcc -O2 -std=gnu11 -I/usr/include/hs repro.c -lhs -o repro
 *   (see run.sh; substitutes a different -I/-L if $UPSTREAM_SCRATCH
 *   holds an alternate build)
 */

#include <stdio.h>
#include <string.h>
#include <hs/hs.h>

static int trial(const char *label, const char *pat) {
    hs_database_t *db = NULL;
    hs_compile_error_t *err = NULL;
    hs_error_t rc = hs_compile(pat, HS_FLAG_DOTALL, HS_MODE_BLOCK, NULL,
                                &db, &err);
    if (rc == HS_SUCCESS) {
        printf("%-32s COMPILED\n", label);
        hs_free_database(db);
        return 1;
    }
    printf("%-32s REFUSED code %d: %s\n", label, (int)rc,
           err ? err->message : "?");
    hs_free_compile_error(err);
    return 0;
}

int main(void) {
    /* Minimal (?x) free-spacing pattern whose last line is an
     * unterminated '#' comment -- the shape of the two real corpus
     * patterns named above, reduced to its essence. */
    const char *plain = "(?x) abc  # trailing comment, no newline";

    static char wrapped[128];
    snprintf(wrapped, sizeof(wrapped), "%s\n", plain);

    int plain_ok = trial("plain (no trailing newline)", plain);
    int wrapped_ok = trial("plain + one trailing \\n", wrapped);

    if (!plain_ok && wrapped_ok) {
        printf("PRESENT: the plain form refuses (code -4, "
               "\"Unterminated comment.\") while appending a bare "
               "trailing newline alone makes the identical pattern "
               "text compile\n");
        return 0;
    }
    if (plain_ok) {
        printf("ABSENT: the plain form now compiles (plain_ok=%d "
               "wrapped_ok=%d)\n", plain_ok, wrapped_ok);
        return 1;
    }
    printf("CANNOT-DECIDE: plain_ok=%d wrapped_ok=%d (neither form "
           "compiled -- not this finding's shape)\n", plain_ok, wrapped_ok);
    return 2;
}
