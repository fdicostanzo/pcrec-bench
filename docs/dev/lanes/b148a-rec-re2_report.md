# Lane b148a-rec-re2 report: recursion assists for RE2 (blinded author)

Read only what the brief allowed (AUTHORS, RULES, recursion.md + samples, the re2 template, `ub_assist.h` for the `ub_span` field types).

| member | tokens | lines | verdict | selftest |
|---|---|---|---|---|
| cscan | 369 | 29 | NOT-CAPABLE | 44/44 |
| wild-sexp-balanced | 180 | 17 | ASSISTED | 25/25 |
| wild-json-validate | 388 | 36 | NOT-CAPABLE | 56/56 |

`ledger-check`: OK. Ledger rows appended to `bench/unusual/assists/assists.tsv`; reviewer columns empty/pending.

## Designs
- cscan: one anchored Latin-1 RE2 token pattern (splice-tolerant via a `~` placeholder expanded in setup; groups = opener / closer / unterminated-token refusal), host loop keeps the depth counter; a second tiny pattern checks `)` after the depth-1 closer. Unterminated string/comment fall to a "bad" group and answer `n`.
- wild-sexp-balanced: RE2 finds the next `[()]` unanchored; host keeps a stack of open offsets, keeps the minimum-start closed pair, stops when the stack empties (no earlier open can still close). One pass, no recursion, no cap.
- wild-json-validate: one anchored token pattern (ws + punct | string | number | keyword); the last byte of the token classifies it; a char state machine plus a stack string enforces the grammar (key/colon/comma/closer states).

## Notes
- cscan: ~45 tokens of the 369 are the `~` expansion lambda; spelling the splice run out in the pattern literal would save them but not reach 300 (~325). Not golfed.
- Unclear in statement: `ub_span` g1 fields for non-cscan members (I left them untouched; selftest passes); setup's `pattern` argument is ignored (statement says patterns are fixed). No RE2 give-up code is reported (Match returns bool only), so an RE2 memory/DFA-budget failure would read as `n`; a runner-side check on `re.error_code()` is not available to the assist.
- Perf caveat (not measured): cscan block comments / long strings are matched with captures, so RE2 uses its NFA over the whole token.
