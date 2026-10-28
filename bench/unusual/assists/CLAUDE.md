# bench/unusual/assists/ -- the assist budget's declared rules and ledger

[B148] lane L2 (unusual_set_v1.md 5.1-5.5). Declared and committed BEFORE any
assist is authored.

- `RULES.md` -- the 300-token budget, the counting rule, the DECLARED
  boilerplate items (the only excluded regions), the ledger format.
- `ub_map.h` -- the ONE declared C hash-map helper (outside the count);
  compile- and behaviour-tested by `tools/tests/test_tokcount.py`.
- `assists.tsv` -- the ledger (header only until the L6 author lanes land);
  checked against the counter by `python3 tools/tokcount.py ledger-check`.
- `problems/` -- the engine-neutral PROBLEM STATEMENTS the blinded L6 author lanes receive
  (one per family) and each one's public self-test sample (disjoint from the held-out
  subjects/streams): `vars.md` + `vars-samples.tsv` (L7, 80 cases), `recursion.md` +
  `recursion-samples.tsv` (cscan / wild-sexp-balanced / wild-json-validate for engines with no
  recursion, 125 cases), `callouts.md` + `callouts-samples.tsv` (co-luhn / co-isbn / co-member
  for engines with no callouts, 48 cases), `netstr.md` + `netstr-samples.tsv` (co-netstr for
  libpcre2, Oniguruma, RE2, rust-regex, Vectorscan; the callee of the callout-assisted shape is
  authored by the blind author, 27 cases) -- lane b148probs, docs/dev/lanes/b148probs_report.md.
- `<member>/<engine>/assist.<ext>` -- (L6, later) one blinded author's assist.

The counter is `tools/tokcount.py` (shared with [B141]); the item registry
lives in its `ITEMS` and RULES.md must name every item (the self-test checks).
