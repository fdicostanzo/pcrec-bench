# bench/sentinel — NOTES (`sentinel@0.1`, [B133], pcrecdev1's ask O-95 (2))

## Objective
An INSTRUMENT sentinel, not a survey. [B132] showed that edits to the bench's
own driver moved short-call timings +10-17% on program-identical cells and
that this was mistaken for a pcrec regression (O-92). [B133] isolated the timed
loop (docs/dev/decisions.md BD16); this set is the standing check that it
stays still: a fixed list of short-call cells measured in EVERY window.

## Contents (all copied; nothing authored)
- 14 patterns + capability's floor: the eleven [B132] MOVERS (winpath-near-miss
  +25%, trim-nested-star, numeric-id-nested-plus, phone-list-nested-plus,
  wild-validator-us-zip-owasp, base10num-near-miss, ipv4-near-miss,
  uuid-near-miss, wild-semdiv-dollar-trailing-newline-pcre2,
  router-prefix-order, wild-validator-email-owasp) and three CONTROLS that were
  flat in every [B132] arm (wild-waf-crs-942360-concat-sqli,
  keyword-prefix-order, file-ext-order). `patterns/*.rx` are byte copies of
  bench/capability's (`gen_patterns.py --check`). Dropped from [B132]'s cell
  list: `wild-codegrammar-json-stringcontent-escape` and `bracket-array-define`
  — both contain a newline and cannot be exported as a `.rxt` `pattern` line
  (the per-set export gate needs that).
- 75 short subjects: capability@0.2's own, regenerated through capability's
  builder (identical bytes and manifest; `gen_subjects.py --check`).
- Regime `search_short` ONLY. 14 x 75 + floor = 1,125 expectation rows,
  libpcre2 oracle.
- Patterns carry capture groups on some members (`phone-list-nested-plus`,
  `trim-nested-star`, `wild-validator-us-zip-owasp`); the sentinel reads
  per-call time, never spans.

## "Program-identical" is a property of a PIN pair, not of the set
These cells were program-identical (`program_sha256`) between c4c70f2c and
255bcdd8 for pcrec-auto/-nocaps. A later pin may change a sentinel cell's
program; the reader of a window report must check `program_sha256` (the
reporter's per-cell identity facts) before attributing a sentinel shift to the
instrument. A shift on a cell whose program changed is the engine's, not the
sentinel's signal.

## How a window report reads it
Testees: pcrec-auto, pcrec-nocaps, pcre2-jit (`run_suite.sh` runs the set FIRST;
a closing `sentinel:end` pass is available for long windows).
1. Compare the set-grain medians (ns/call, reporter `--grain set`) against the
   PREVIOUS window's sentinel records on the same pins/drivers.
2. pcre2-jit flat (within its trial agreement) AND pcrec shifted on
   program-identical cells -> the INSTRUMENT (or the box) moved for pcrec's
   driver: check `run.harness_commit` for a `testees/pcrec/{driver.c,timed.c,
   shim.c}` change and the environment block (governor, load); do NOT file it
   against pcrec.
3. pcre2-jit shifted too -> box state, not an adapter edit; re-measure.
4. Sentinel flat across windows -> a pcrec Delta on other short cells of the
   same window is the engine's (the instrument demonstrably did not move).
5. Cell-level: the movers are the sensitive cells (winpath first); the three
   controls should be flat in every case — a control shifting while the movers
   do not is box noise.
The set is NOT ranked, not a scoreboard row, and carries no objective.

## Cost
14 patterns x 75 short subjects, five trials, three testees: minutes per cell.
