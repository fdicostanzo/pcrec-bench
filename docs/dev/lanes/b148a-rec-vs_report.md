# Lane b148a-rec-vs: recursion assists, Vectorscan (blinded author)

All three selftests pass every public case. `ledger-check`: OK. Rows appended to bench/unusual/assists/assists.tsv.

| member | tokens | lines | verdict | selftest |
|---|---|---|---|---|
| wild-sexp-balanced | 261 | 22 | ASSISTED | 25/25 |
| wild-json-validate | 469 | 53 | NOT-CAPABLE | 56/56 |
| cscan | 755 | 48 | NOT-CAPABLE | 44/44 |

## Designs
- **wild-sexp-balanced**: one `[()]` pattern, block mode; the callback is the host's nesting stack (positions of `(`). A `)` popping to empty ends the scan (HS_SCAN_TERMINATED); otherwise the minimum popped start wins (unclosed leading `(` case). Scans `subj+start`; stack array grown once to n.
- **wild-json-validate**: four anchored token patterns (ws, string, scalar, punctuation) in one multi-pattern db; one `hs_scan` per token at the current position (callback keeps the last, i.e. longest, end); host runs a 6-state pushdown over a char stack. Untested at 1 MB: it relies on Vectorscan stopping the scan once the anchored automaton dies (else quadratic).
- **cscan**: a pure host lexer with a splice-skipping cursor. It calls NO engine, so it would be rejected `not-idiomatic`; it is only a lower bound. I did not find an engine-using design: Hyperscan reports every overlapping end, has no lookahead, and every token pattern would need a splice-tolerant gap after every unit (plus backslash-run ambiguity `\\\n`), which can only be larger than 755.

## Unclear in the statement
- Whether the counter treats the unused `ub_setup(pattern...)` argument as a free hook for the member's pattern; I ignored it.
- No stated way to learn the engine's behavior on scanning past a dead anchored automaton (cost model).
