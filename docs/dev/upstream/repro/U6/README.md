# U6 — TRE's bracket-expression parser never processes backslash escapes

**Engine:** TRE (`libtre`), byte-mode POSIX API (`tre_regncompb`/
`tre_regnexecb`, `REG_EXTENDED`). **Version:** 0.9.0 (both the Ubuntu
`libtre-dev 0.9.0-1build1` package this project uses and the pristine
upstream `v0.9.0` release tag — identical result from both builds, see
`expected.txt`). **Kind:** correctness.

## What it shows

`tre_regncompb()` accepts the pattern `[\x80-\xff]{2,4}` (a common
byte-oriented idiom: "two to four consecutive high/non-ASCII bytes")
without error, but the compiled program has nothing to do with high
bytes. Outside a bracket expression TRE recognises `\xHH` as a hex-byte
escape (its own documented GNU-style extension) — but its bracket
parser (`tre_parse_bracket_items()` in `lib/tre-parse.c`) reads
characters directly with **no escape processing of any kind**: `\` is
just an ordinary character there. So `\x80-\xff` inside `[...]` is read
as the literal sequence `\ x 8 0 - \ x f f`, which POSIX bracket syntax
turns into the range `'0'`-`'\'` (0x30-0x5C, i.e. every ASCII digit,
`:;<=>?@`, `A`-`Z`, `[`, `\`) plus the two standalone literals `x`
(0x78) and `f` (0x66, already inside the range).

Consequence, demonstrated by `repro.c`:
- **Case A**, plain ASCII text with no byte ≥ 0x80 at all
  (`"GET /products?category=shoes&sort=price"`): the pattern
  spuriously **matches** `GET` at `[0,3)` — three ASCII letters that
  happen to fall in the accidental 0x30-0x5C range — where every other
  engine we tried (libpcre2, pcrec, oniguruma, RE2, vectorscan) reports
  no match, correctly.
- **Case B**, the actual high-byte pair the pattern is meant to catch
  (bytes `0x81 0x82`): TRE reports **no match**, where it should match
  `[0,2)`.

This is not a high-byte-specific gap; it is a **general property of
every bracket expression containing a backslash escape**. The same
mechanism explains two further capability-set patterns observed wrong
in the same window: `<([a-zA-Z][\w:-]*)...` (tag-pair-match, `\w`
inside `[...]` reads as literal `w`) and a SQL-injection detector whose
`[\s\x0b]` reads as the literal set `{\, s, x, 0, b}` instead of
"whitespace or vertical tab".

## How it was established

- **Behavioural**: `repro.c`'s cases A/B above, and a byte-by-byte scan
  of `^[\x80-\xff]$` against all 256 byte values (not shipped as part
  of this repro — see the finding's evidence trail in
  `docs/dev/upstream_findings.md` U6 / this note) confirming the
  matched set is exactly `{0x30-0x5C} ∪ {0x66, 0x78}` — precisely the
  parse this README derives above, not merely "some bytes wrong".
- **Source**: TRE 0.9.0's `lib/tre-parse.c`,
  `tre_parse_bracket_items()` (~lines 256-365): every branch reads
  `*re`/`*(re+1)`/`*(re+2)` as plain characters (`min = *re; max =
  *(re + 2);` for a range, `min = max = *re++;` for a literal) with no
  call into any escape-decoding routine. Contrast the top-level atom
  parser's `case L'x':` (~line 1466 of the same file), which DOES
  decode `\xHH` — but is never reached while inside `[...]`.

## Build and run

Needs `libtre-dev` (header `<tre/tre.h>`, `-ltre`) — or a pristine TRE
source tree already configured/built with the static `libtre.a`
`run.sh` will look for under `$UPSTREAM_SCRATCH` if a system copy isn't
found. `run.sh` builds with `gcc -O2 -std=gnu11` and runs the single
binary; no bench code, no store, no stdin.

    UPSTREAM_SCRATCH=/var/tmp/some-dir ./run.sh

Exit 0 = PRESENT (TRE disagrees with the oracle on at least one case),
1 = ABSENT (TRE agrees with the oracle on both — i.e. fixed), 2 =
CANNOT-RUN (libtre not found / build failed).

## What ABSENT (fixed) would look like

    case A ("GET /products?category=shoes&sort=price"): tre=nomatch oracle=nomatch
    case B (0x81 0x82): tre=MATCH oracle=match [0,2)
    ABSENT: both cases agree with the oracle
    U6 ABSENT tre <version> 1

## Status

REPRODUCED (this repro; also independently reproduced twice by the
bench itself, see `docs/dev/upstream_findings.md` U6) and now
**UNDERSTOOD** (this note upgrades U6 from "not yet UNDERSTOOD" —
the source read above is new since the narrative was last written).
Not yet checked for a matching upstream tracker entry beyond this
lane's own search (see `docs/dev/lanes/b103other_report.md`); not
REPORTED.
