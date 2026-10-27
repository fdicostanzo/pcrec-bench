# Assist rules (unusual@0.1; counter `tokcount-1`)

Declared and committed BEFORE any assist is authored (unusual_set_v1.md 5.2).
A change to anything below is a new counter version and a new `assist-v..`
identity decision, never an edit in place.

## Budget

**300** lexical tokens per (MEMBER, engine), counted by `tools/tokcount.py`
(counter version `tokcount-1`) in the engine's binding language: C for
libpcre2, Oniguruma and Vectorscan; C++ for RE2; Rust for rust-regex (Python
for the [B141] expressibility bench, which shares this counter and this rule).
<= 300 is ASSISTED; > 300 is NOT-CAPABLE with the count recorded. An assist
serving several members of a family is counted in full against EACH member.

## The counting rule

A token is a lexical token of the file's language from one hand lexer per
language: identifier/keyword; number (one token with suffix, digit
separators, exponent); string or char literal (one token, prefixes and
raw / triple-quoted / f-string forms included); Rust lifetime; the C
header-name after `#include`; punctuator (multi-character punctuators are
one token). Comments, whitespace and Python layout are not tokens. LINES is
the number of physical lines on which a counted token starts or continues.
Standard-library containers and types are free (they are just identifiers
the author did not write). Nothing is estimated: the counter prints the
number and the ledger stores it.

## Declared boilerplate (the ONLY excluded regions)

Fenced in the assist file: `/* BOILERPLATE <item> */ ... /* END BOILERPLATE */`
(C, C++, Rust) or `# BOILERPLATE <item>` ... `# END BOILERPLATE` (Python).
An undeclared item, a malformed or unclosed or nested fence fails the count
naming it. A region whose content breaks its item's shape is SMUGGLING: the
region is counted in full and flagged (`smuggled`; `ledger-check` fails on it).

| item | what it may hold | shape enforced by the counter |
|---|---|---|
| `includes` | `#include` / `use` / `extern crate` / `import` / `from` lines, incl. `#include "ub_map.h"` | every statement is an import; <= 120 tokens |
| `main` | the entry point that calls the driver shim | no `if else for while do switch case match loop goto try`; <= 40 tokens |
| `io` | subject loading and result reporting glue | no `switch match goto`; <= 80 tokens |
| `shim` | the driver-protocol shim (timed loop, call-stream decoding) | <= 200 tokens |
| `wrappers` | the per-engine wrappers of the shared callees (`callees.c`) | no `switch match goto`; <= 120 tokens |

The shared callees themselves (`callees.c`) live outside the assist file and
are not counted. A fence is for the item's own content only: an author who
needs an `if` in `main` has logic, and logic counts.

## The one C helper

`assists/ub_map.h` (string-key -> pointer hash map, ~60 lines) is the ONE
declared hash-map helper for C assists, outside the count; an assist includes
it (inside `includes`) and may not carry a hash map of its own. C++ and Rust
use their standard containers (free).

## Ledger

`assists/<member>/<engine>/assist.<ext>` plus one `assists.tsv` row per
(member, engine); columns in this order: member, feature, engine, language,
tokens, lines, budget, verdict (ASSISTED / NOT-CAPABLE), assist_sha256,
keying (what the memo key is), container, counter_version, author_lane,
reviewer_lane, reviewer_verdict (accepted / golfed / not-idiomatic /
pending). `python3 tools/tokcount.py ledger-row FILE ...` produces a row;
`ledger-check` recounts every row and fails on any disagreement (the counter,
not the author, produces the count). Self-test: `make check-tokcount`.
