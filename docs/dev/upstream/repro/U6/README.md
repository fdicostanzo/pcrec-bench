# U6 — TRE's bracket-expression parser never processes backslash escapes

**Engine:** TRE (`libtre`), byte-mode POSIX API (`tre_regncompb`/
`tre_regnexecb`, `REG_EXTENDED`). **Version:** 0.9.0 (both the Ubuntu
`libtre-dev 0.9.0-1build1` package this project uses and the pristine
upstream `v0.9.0` release tag — identical result from both builds, see
`expected.txt`). **Kind:** semantics (see Status below — **this is
NOT A BUG**, corrected 2026-09-27 after a manager review; it was
initially misread as a TRE defect and a note was nearly sent).

## What it shows

`tre_regncompb()` accepts the pattern `[\x80-\xff]{2,4}` (a common
byte-oriented idiom in PCRE-family dialects: "two to four consecutive
high/non-ASCII bytes") without error, but the compiled program has
nothing to do with high bytes. Outside a bracket expression TRE
recognises `\xHH` as a hex-byte escape (its own documented GNU-style
extension) — but its bracket parser (`tre_parse_bracket_items()` in
`lib/tre-parse.c`) reads characters directly with **no escape
processing of any kind**: `\` is just an ordinary character there. So
`\x80-\xff` inside `[...]` is read as the literal sequence
`\ x 8 0 - \ x f f`, which bracket-expression syntax turns into the
range `'0'`-`'\'` (0x30-0x5C, i.e. every ASCII digit, `:;<=>?@`, `A`-`Z`,
`[`, `\`) plus the two standalone literals `x` (0x78) and `f` (0x66,
already inside the range).

Consequence, demonstrated by `repro.c`:
- **Case A**, plain ASCII text with no byte ≥ 0x80 at all
  (`"GET /products?category=shoes&sort=price"`): the pattern
  **matches** `GET` at `[0,3)` — three ASCII letters that happen to
  fall in the accidental 0x30-0x5C range.
- **Case B**, the actual high-byte pair the pattern's *author* meant
  it to catch (bytes `0x81 0x82`): TRE reports **no match**.

## Why this is NOT A BUG

**POSIX.1-2017 XBD 9.3.5 states plainly:** *"The special characters
`.`, `*`, `[`, and `\` shall lose their special meaning within a
bracket expression."* Backslash carries no escaping power inside
`[...]` in POSIX bracket-expression syntax, full stop — TRE's parser
implements this correctly. `[\x80-\xff]` was never valid syntax for
"the byte range 0x80-0xFF" under POSIX; it is valid PCRE/Perl syntax
that happens to also parse (differently) as a POSIX bracket expression,
and TRE — "a lightweight, robust, and efficient **POSIX compliant**
regexp matching library" (its own package description) — is reading it
by the rules it actually implements.

**Confirmed with an independent control, `control_glibc.c`**, which
links ONLY glibc's `<regex.h>` (no TRE at all) and runs the identical
pattern and both subjects through `regcomp()`/`regexec()`,
`REG_EXTENDED` — the reference POSIX ERE implementation on this box,
used by countless other programs. It shows the **exact same split**:
case A matches `[0,3)`, case B does not match. See `expected.txt` for
the verbatim run. Nobody would call glibc's `regcomp` a broken POSIX
implementation; TRE agrees with it byte for byte on this pattern.

This is the same shape as the *already-documented* portability finding
in `testees/tre/CLAUDE.md` (d)4 ("POSIX bracket expressions give
backslash NO special meaning at all"), which names three DIFFERENT
capability-set patterns that REFUSE to compile for the same underlying
reason (a resulting DESCENDING range, `REG_ERANGE`). This finding
covers the SILENT-WRONG-ANSWER manifestation of the identical
mechanism — patterns that still compile, just to something else — on
three more patterns (`high-byte-run`, `tag-pair-match`,
`wild-waf-crs-942360-concat-sqli`), plus a fourth-and-broader census;
see `docs/dev/lanes/b103other_report.md` and
`docs/dev/measurements/2026-09-27-tre-bracket-escape-census.*` for the
full corpus scan and readings.

## Bench-side implication (not upstream's problem)

Because this is TRE correctly implementing POSIX, the actionable
finding is entirely on this project's side: **the `tre-default` adapter
receives PCRE-dialect pattern text (including `\xHH`/`\w`/`\s`-style
escapes inside `[...]`) and hands it to a POSIX-only engine that reads
those bytes under different rules.** See
`docs/dev/lanes/b103other_report.md` for: the full corpus census (which
`bench/*/patterns/*.rx` files contain a bracket expression with a
backslash inside it, across all seven sub-benches, not just
`bench/capability`), which of those rows are measured wrong for
`tre-default` TODAY (per the store's own capability@0.1 records), which
are moot (already intercepted by an existing `unsupported-by-`
declaration or already refuse to compile for the reason (d)4 already
documents), and a proposed — **not implemented** — fix shape (either
translate the escapes this adapter's own pattern text uses before
handing them to TRE, or declare such patterns unsupported for
`tre-default`).

## Build and run

Needs `libtre-dev` (header `<tre/tre.h>`, `-ltre`) for `repro.c`; the
CONTROL (`control_glibc.c`) needs nothing beyond a working C toolchain
(`<regex.h>` is glibc's own header, always present on this box).
`run.sh` builds and runs both with `gcc -O2 -std=gnu11`; the control's
result is informational only and never changes this script's exit code.

    UPSTREAM_SCRATCH=/var/tmp/some-dir ./run.sh

Exit 0 = PRESENT (TRE disagrees with a PCRE-style reading on at least
one case — still true; POSIX-conformance doesn't change the behaviour,
only how it should be read), 1 = ABSENT, 2 = CANNOT-RUN (libtre not
found / build failed).

## Status

**NOT-A-BUG** (POSIX bracket-expression semantics, confirmed against
POSIX.1-2017 XBD 9.3.5 and an independent glibc `regcomp` control — see
above). REPRODUCED and UNDERSTOOD as a POSIX-conformance question (this
repro; also independently reproduced twice by the bench itself before
this correction, see `docs/dev/upstream_findings.md` U6). No note
drafted for TRE's maintainers — telling them their POSIX-conforming
parser is wrong would be exactly backwards. The real, actionable
finding is a BENCH-side one: see "Bench-side implication" above and
`docs/dev/lanes/b103other_report.md`.
