# U7 — vectorscan refuses a `(?x)` pattern ending in an unterminated `#` comment

**Engine:** vectorscan (Hyperscan-ABI-compatible fork), `hs_compile()`.
**Version:** 5.4.11 (`libvectorscan-dev 5.4.11-2ubuntu2`, this project's
current pin). **Kind:** compatibility.

## What it shows

`hs_compile()` refuses the free-spacing (`(?x)`) pattern
`"(?x) abc  # trailing comment, no newline"` with code **-4**,
`"Unterminated comment."`, even though the pattern is syntactically
complete PCRE: PCRE defines a `(?x)` `#`-comment as running to the next
newline **or to the end of the pattern**, whichever comes first — no
closing token is required. libpcre2 10.46, pcrec, oniguruma 6.9.10 and
rust-regex 1.13.1 all accept this exact text. Two real patterns in
pcrec-bench's capability set hit this at the corpus scale:
`wild-codegrammar-json-number-extended.rx` and
`wild-codegrammar-json-stringcontent-escape.rx`, both legitimate
free-spacing patterns whose author simply didn't add a trailing blank
line after the last comment.

A second, harness-relevant fact this repro also shows: appending a
**single trailing newline byte** to the identical pattern text is
enough to make it compile (the newline terminates the open comment).
This happens to be exactly what pcrec-bench's own whole-subject wrap
inserts for a free-spacing pattern (`record_schema.md` §5 ADDITIONS 3),
so the SAME pattern compiles under one wrap form and refuses under
another — stated here for completeness, but the finding itself is the
plain-form refusal, independent of any wrapping.

## How it was established

- **Behavioural**: `repro.c`, exactly as above — a two-line pattern
  reduced from the two real corpus patterns to its essential shape.
- **Source** (vectorscan 5.4.11's `src/parser/Parser.rl`): the
  extended-mode comment action `enterNewlineTerminatedComment` sets
  `inComment = true` and transitions to a state
  (`readNewlineTerminatedComment`) that clears `inComment` only on
  seeing `'\n'`; at end of input, if `inComment` is still true, the
  parser throws `ParseError("Unterminated comment.")` unconditionally
  — there is no "end of pattern also closes an open `#` comment" case,
  unlike PCRE's own documented rule.
- **Still present on the latest release**: vectorscan's newest tag is
  **`vectorscan/5.4.13`** (published 2026-08-23; `5.4.12` published
  2025-07-22 sits between it and our pinned `5.4.11`). Building
  vectorscan from source needs `ragel` and CMake plus Boost
  *development* headers, none of which are on this box (`ragel`/`cmake`
  absent; only Boost's runtime `.so` packages are installed, no
  `libboost-dev`) — a build materially heavier than "modest", so this
  lane did **not** build 5.4.12/5.4.13 (CANNOT-RUN for that step,
  reason above). Instead, `src/parser/Parser.rl` was fetched and
  diffed line-for-line across all three tags
  (`5.4.11`→`5.4.12`→`5.4.13`): the `inComment` /
  `readNewlineTerminatedComment` / end-of-input-throws-if-still-in-
  comment logic is **byte-for-byte identical** in every version; the
  only changes in that file across two releases are a `cppcheck`
  suppression comment, two `reinterpret_cast` style changes, a
  `std::move` removal, and a NEW, unrelated restriction (nested
  character classes / `&&` intersection now refused, issue #210) added
  in 5.4.12. None of the diff touches comment handling. This is
  read-only source evidence, not a run against the newest binary.

## Build and run

Needs `libvectorscan-dev` (`<hs/hs.h>`, `-lhs`) — this project's own
`testees/vectorscan/driver.c` link line. `run.sh` builds with
`gcc -O2 -std=gnu11 -I/usr/include/hs` (override the include dir with
`$VECTORSCAN_INCLUDE_DIR` for an alternate build under
`$UPSTREAM_SCRATCH`) and runs the single binary; no pcrec-bench code,
no store, no stdin.

    UPSTREAM_SCRATCH=/var/tmp/some-dir ./run.sh

Exit 0 = PRESENT (plain form refuses, wrapped form compiles), 1 = ABSENT
(plain form now compiles too — fixed), 2 = CANNOT-RUN (libvectorscan not
found / build failed).

## What ABSENT (fixed) would look like

    plain (no trailing newline)      COMPILED
    plain + one trailing \n          COMPILED
    ABSENT: the plain form now compiles (plain_ok=1 wrapped_ok=1)
    U7 ABSENT vectorscan <version> 1

## Status

REPRODUCED (this repro, and the bench's own
`capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__...`
record — see `docs/dev/upstream_findings.md` U7) and UNDERSTOOD (the
Parser.rl mechanism above). `latest_checked`: source-diffed (not run)
against `5.4.12`@2025-07-22 and `5.4.13`@2026-08-23, both unchanged in
the relevant code; no build of either was performed on this box (see
"heavy build" above). Tracker: searched, no existing report found (see
`docs/dev/lanes/b103other_report.md`). Not REPORTED. Whether this is
reportable-as-a-defect or simply vectorscan's documented "stricter than
PCRE" parsing stance (Hyperscan's PCRE-subset posture is stated policy,
not full PCRE compatibility) is a judgment call for whoever drafts the
note — this repro establishes only that it is real, reproducible, and
still present on the newest released source.
