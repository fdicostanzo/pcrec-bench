# b148a-rec-re2-v2 -- cscan x re2, re-authored unblinded (Frank, 2026-10-28)

## Result
`assists/cscan/re2/assist.cc`: **262 tokens, 28 lines, ASSISTED** (was 369, NOT-CAPABLE).
Selftest: `assist-selftest --member cscan --engine re2` -> 44/44 pass.
`tools/tokcount.py ledger-check`: OK.

## Design (ported from assists/cscan/rust/assist.rs)
- ONE token regex, compiled in setup (Latin-1, dot_nl), iterated UNANCHORED with
  `RE2::Match(s, pos, s.size(), UNANCHORED, &t, 1)` from the previous token's end; the engine
  skips ordinary bytes, so there is no catch-all `.` alternative.
- Tokens: identifier, pp-number, string, char, block comment, line comment, `{`, `<%`, a
  closer `(}|%>)` that ABSORBS an optional `)` (so no second `tail` regex), a lone quote
  (a refusal), and the two unterminated-comment tails (matched, then the loop reaches EOF -> n).
- Line splices: `~` in the pattern text is expanded to `(?:\\\n)*` by `RE2::GlobalReplace`
  (a one-line setup call; replaces the old 45-token lambda). Rewrite string needs `\\\\` per
  backslash, hence the odd-looking literal; commented.
- Host: a `switch` on the token's first byte keeps `depth`; the depth-1 closer must end in `)`
  (else n); a quote-only token is a refusal (n). Offsets are absolute; g1 = `[start+3, b)`.
- State: one global `unique_ptr<RE2>`; nothing cached between calls.

## R10A inputs (checked with a scratch driver including the assist; output matches expectation)
- R10A-1 `(?{ x; %>)` at 0, expect `m:0,10;3,7` -> `m:0,10;3,7`.
- R10A-2 `(?{ // c \<LF> })` (no later LF), expect `n` -> `n`.
- R10A-3 `(?{ "\\<LF><LF>"; })` (bytes `"` `\` `\` LF LF `"`), expect `n` -> `n`.

## Ledger / checks
Row `cscan`/`re2`: tokens 262, lines 28, ASSISTED, sha256 701f9780...fcbc, container "compiled RE2
unanchored token pattern", author_lane b148a-rec-re2-v2, reviewer_lane and reviewer_verdict `pending`.
`check_unusual.py --only assist-tree`: 12 pass / 4 FAIL, all expected consequences of the brief:
reviewer_verdict `pending` (x2 -- the "no pending" gate and the control), the ledger now has two author
lanes for (recursion, re2) (b148a-rec-re2 wrote wild-sexp-balanced; this row is b148a-rec-re2-v2), and the
reviewer Counts lines (41 accepted in ledger vs 42 in r10a/r10b, the old cscan/re2 `accepted`). The
manager needs to re-review the row and decide the author-lane / Counts bookkeeping.
`--only assist`: 15 pass / 1 FAIL -- `run_cell re2-default-assist-v01`: the worktree lacks the
generated (gitignored) subject trees; not related to this change.

## Read
assists/cscan/rust/assist.rs, the old re2 assist.cc, AUTHORS.md, RULES.md, problems/recursion.md
(+ samples), the templates region of assist.cc, docs/dev/reviews/2026-10-28-r10a-assists-recursion-netstr.md
(R10A rows). NOT read: held-out subjects/expectations, b148heldout_report, unusual_lib.py, expectations*.tsv,
any other member's assist.

## diff --name-status master...HEAD
M bench/unusual/assists/CLAUDE.md
M bench/unusual/assists/assists.tsv
M bench/unusual/assists/cscan/re2/assist.cc
A docs/dev/lanes/b148a-rec-re2-v2_report.md
