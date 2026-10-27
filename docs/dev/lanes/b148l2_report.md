# Lane b148l2 report -- the assist token counter ([B148] L2)

Branch lane/b148l2. Code + self-tests only; no timing, no engine runs.

## The counting rule (one paragraph, shared with [B141])
A token is a lexical token of the file's own language from one hand lexer
per language (C, C++, Rust, Python): identifier/keyword; number (suffix,
digit separators, exponent inside one token); string/char literal (one
token, incl. prefixes, raw, triple-quoted, f-strings); Rust lifetime; the C
header-name after `#include`; punctuator (multi-character ones are one
token). Comments, whitespace, backslash-newline and Python layout are not
tokens. LINES = physical lines on which a counted token starts or continues.
Regions fenced `/* BOILERPLATE <item> */ ... /* END BOILERPLATE */` (Python:
`# ...`) are excluded only if `<item>` is declared (`ITEMS`:
includes, main, io, shim, wrappers); an undeclared/malformed/unclosed/nested
fence fails naming it (exit 2); a declared region whose content breaks the
item's shape (non-import statement in `includes`, control keywords in
`main`, token cap) is SMUGGLING: counted in full and flagged. Budget 300.
[B141] (plan.md, STATE:not-started) states "non-blank lines + lexical tokens
against a declared boilerplate list" and no finer rule, so this is that
rule made exact; B141 should import `tokcount.py` rather than restate it.

## Checklist vs unusual_set_v1.md section 5
- 5.1 budget 300 per (member, engine), languages C/C++/Rust (+Python for B141), containers free, one C helper: done (RULES.md, `BUDGET`).
- 5.2 RULES.md declared (budget, counter+version, boilerplate list, fence syntax, "item must be declared else the run fails naming it"); `ub_map.h` (63 lines, compiled -Wall -Wextra -Werror and behaviour-tested); counter `tools/tokcount.py` hand lexers, self-tested on hand-counted fixtures: done.
- 5.3 ledger: `assists.tsv` header with the 15 columns of 5.3 (`counter_version` included), `ledger-row` producing a row, `ledger-check` recounting every row (tokens, lines, sha256, verdict, language, counter version, duplicates, smuggling): done. Header-only until L6.
- 5.4 authoring: not this lane (L6). The counter produces the count; `reviewer_verdict` vocabulary fixed.
- 5.5 identity/capability: not this lane (L1/L4).
Note: 5.2 puts the callees/shim under "boilerplate"; I made `shim`/`wrappers` caps (200/120 tokens) because an unbounded fence is an unbounded loophole. Raise in RULES.md + `ITEMS` if L5's real shim is larger (that is a counter-version bump).

## Self-test (47 checks, `make check-tokcount`, ~1 s)
Hand-counted fixtures: C 33 tokens/6 lines (6 excluded), unfenced 39/8; C
splice 10/3; C++ raw string+templates 15/2; Rust 47/6 (11 excluded: lifetimes,
byte/raw strings, `..=`, `1.max`, nested comment); Python 36/7 (6 excluded:
f/rb strings, triple quote, `:=`, `**`, `//`). Sabotage (counted + flagged):
`if` in main, code in includes, tokens after an `#include`, a loop in a Python
main, code in Python imports, `fn` in Rust includes, over-cap main. Control: a
loop in `shim` is excluded. Fence errors by name: undeclared, unclosed, stray
END, `//` form, no item, nested. Ledger round trip incl. tamper, duplicate,
301 -> NOT-CAPABLE, 300 -> ASSISTED. RULES.md names every item.

## Wiring
New target `check-tokcount` (self-test + `ledger-check`), added to `check`'s
prerequisites and `.PHONY` in the Makefile (the smallest hook; nothing else
in `check` touched). `tools/CLAUDE.md` row added. Not run: full `make check`.
