# bench/unusual/assists/ -- the assist budget's declared rules and ledger

[B148] lane L2 (unusual_set_v1.md 5.1-5.5). Declared and committed BEFORE any
assist is authored.

- `RULES.md` -- the 300-token budget, the counting rule, the DECLARED
  boilerplate items (the only excluded regions), the ledger format.
- `ub_map.h` -- the ONE declared C hash-map helper (outside the count);
  compile- and behaviour-tested by `tools/tests/test_tokcount.py`.
- `assists.tsv` -- the ledger (header only until the L6 author lanes land);
  checked against the counter by `python3 tools/tokcount.py ledger-check`.
- `<member>/<engine>/assist.<ext>` -- (L6, later) one blinded author's assist.

The counter is `tools/tokcount.py` (shared with [B141]); the item registry
lives in its `ITEMS` and RULES.md must name every item (the self-test checks).
