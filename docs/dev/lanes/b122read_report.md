# lane b122read report — [B122] round-1 WIDE read, pcrec c4c70f2c (abi 59)

Branch `lane/b122read`, worktree
`.claude/worktrees/agent-a18de239f08a29ab9` (this agent's own dedicated
worktree; renamed onto `lane/b122read` at the start rather than a
nested `worktrees/b122read`). Window: 16 cells at pcrec c4c70f2c, all
`measured` at attempt 1, 2026-10-05 00:28-08:42 EDT. `~/pcrec` was not
touched (read-only, as always).

## 1. Findings first

1. **A render-mechanic gap, found and fixed before any score was
   computed**: querying only the new `pcrec_c4c70f2c_*` testees gives
   EVERY row `"no null band (no cross-pin pair in this report)"` —
   `pcrecbench/report.py`'s R8 cross-pin detection
   (`_previous_pin_testee`) searches only testees PRESENT IN THE
   QUERY'S OWN RESULT SET, not the whole store. All eight report groups
   were re-rendered with the prior-pin same-(engine,config) testee
   added explicitly (fc719ca4 for seven sets, a32bc86e for litrun), and
   the Δ column fires throughout from the second render on — the
   committed reports and sidecars are the second render.
2. **K82 ([OPT-LITSCAN] S4 C3, `-fno-req-run-fold`) scores cleanly on
   its two named magnitude cells** — userpass `×55.66` (filed ~57×, 2.4%
   off), "customers union-select" `−0.3861 ns/B` (filed −0.40..−0.52
   ns/B) — **and finds a real, two-sided regime split on its five named
   fold-family patterns** (mod-i/mod-r/cls-fold-pair/cls-pair-ctl/
   ci-strasse) far larger than any magnitude the inbox text states:
   SLOWER on large-subject-throughput (`×1.10-×2.29`, worst on the
   forced-VM route) and FASTER on short-subject-search on the
   forced-VM route specifically (`×1.36-×1.68`).
3. **K81 ([OPT-VEDGE], `-fno-view-edge`) does NOT confirm as a real
   mover on either named pattern.** `base10num-grok` and
   `cls-upto-1024` both move further than predicted, in the predicted
   direction, on large-subject-throughput — but read `unchanged (within
   spread)` by this project's own R8 criterion (only 3 trials, wide
   stddev); their smaller-regime cells move the OPPOSITE direction and
   ARE real.
4. **Two citations could not be matched to a measured cell**: K81's
   "short-call +1-9 ns" (no pattern in any of this project's eight sets
   spells "short-call") and K82's "short union-srch calls +2.4-4.4 ns"
   (union-select's own short-subject-search cell moved the OPPOSITE
   direction, a real improvement). Flagged for pcrecdev1 to name
   exactly, the same precedent as this project's standing Q5
   (b120b121read ledger §3).
5. **K83 ([OPT-HYB-RESEED-FORM] A1) is unscored this window** — no
   clang cc-axis arm was in tonight's 16-cell list; the filed number is
   for clang specifically.
6. **pcrec wrong-answer count: 0 NEW.** The one nonzero reading
   (`syntax`'s `asr-k-uc`/`rec-r-uc`, `n_wrong=5` of 42, all three pcrec
   testees) is byte-identical to the same two patterns' fc719ca4 reading
   and is the pre-existing, documented 2026-09-07 whole-subject
   anchored-branch limitation (`first_s` hardcoded to 0) — confirmed
   unchanged across the re-pin, not a round-1 regression. All other 13
   of 16 cells read 0.
7. **Two real movers beyond I-127's own text**, found on a spot check
   (not a systematic sweep): utf8's `ci-ascii-control` improves hugely
   on large-subject-throughput (`×2.77` auto, `×8.38` forced vm — the
   window's largest win anywhere); `alt-shared-char` regresses on the
   same regime (`×2.06` DFA, `×1.21` forced vm).
8. **altwide's forced-VM class-tail family reads a real win tied
   directly to the census's own attribution**: `clsa-64`/`clsd-64`
   `×1.16-×1.37 faster` across all three regimes on `pcrec-vm`,
   matching the census's finding that 291 of 462 changed rows are
   altwide's own VM forms restored-by `-fno-run-overlap` alone —
   [OPT-LITSCAN] S4 C1's run-overlap mechanism is a real timing win on
   this set's forced-VM arm, not merely a compile-byte change.
9. **email's `factored` pattern — a flagless census mover (K78) —
   reads genuinely flat on timing** across all three regimes,
   confirming the census's own reading that a program change (the
   dead-group-fill relocation) need not move a number.
10. **litrun shows no cross-pin mover beyond ±1.17×** on any of its 15
    patterns across three regimes — expected: none of round 1's four
    changes is litrun's own mechanism family (S2a).

## 2. Charter-vs-committed checklist

| brief item | status |
|---|---|
| Step (c): CROSS-PIN report groups per set, c4c70f2c vs the same config at fc719ca4 (litrun: vs a32bc86e, two re-pins apart, stated in header/ledger); named `reports/2026-10-05-<set>-...-round1-c4c70f2c.*`; interpretation sidecars for each | **COMMITTED** — eight groups, `{tsv,md,interpretation.md}` each (24 files), `reports/2026-10-05-{capability-0.1,syntax-0.1,utf8-0.1,loglines-0.1,bounded-0.3,email-specimen-0.2,altwide-0.3,litrun-0.1}-budu-ryzen1600-round1-c4c70f2c.*`; litrun's cross-pin caveat stated in the ledger's intro and §1 and in both `reports/CLAUDE.md`'s and `docs/dev/ledgers/CLAUDE.md`'s new entries; every sidecar generated via `pcrecbench interpret` (the skill's documented procedure, applied by hand per-report since the skill itself takes one report at a time), determinism-checked byte-identical on a second stdout render, and re-confirmed fresh by `make check-interpret` section 3 (76/76) |
| A LEDGER `docs/dev/ledgers/2026-10-05-b122-round1-wide-c4c70f2c.md`: per-set cross-pin movers beyond the null band, each mover attributed where possible using the census, an unchanged-program-but-moved pattern called noise/environment; K81/K82/K83 scored; pcrec wrong-answer count per cell; what was NOT read; window facts (times, STOP_AT, per-set minutes, 16 cells, the miscount correction) | **COMMITTED** — `docs/dev/ledgers/2026-10-05-b122-round1-wide-c4c70f2c.md`, the intro (window facts, the 16-cell store confirmation, the litrun cross-pin caveat), §1 report groups + the render-mechanic finding, §2 census attribution (carried from pcrec's own file, not re-derived), §3 K81/K82/K83 scored against the rendered reports' own `median_ns`/`stddev_ns`/`delta_verdict` columns (R8's own verdict already applies this project's noise bar — no separate hand computation needed), §4 the wrong-answer headline, §5 what was not read, §6 nine ranked findings. The email/factored and altwide/run-overlap attributions in §6 items 8/9 are the "unchanged-program called noise" / "changed-program-confirmed-real" cases the brief asked for |
| An OUTBOX DRAFT `docs/dev/lanes/b122read_outbox_draft.md` in the O-81/O-82 shape, draft only | **COMMITTED** — full prose draft with every number inline, same shape as the cited precedents; explicitly marked as the manager's to commit to `outbox_to_pcrec.md` (never written there by this lane) |
| RAM/BOX GATE: all non-render work first; message "b122read ready to render" to main and WAIT; render one group at a time, detached, `nice -n 19`, after "renders OK" | **COMMITTED** — sent the readiness message (confirmed delivered), held without polling until the manager's "renders OK" arrived (13:41Z pcrec clear, mech rerun not timing-sensitive), then rendered all eight groups sequentially under `nice -n 19` (each `pcrecbench report` invocation auto-promoted to the Bash tool's own harness-tracked background slot when it exceeded 120 s — never a bare `&`/`setsid` detach, which this lane found does NOT survive the tool call boundary in this sandbox: a first attempt at `setsid ... & disown` produced a 0-byte output file and an empty log, diagnosed and abandoned in favour of the tool's native background promotion) |
| `make check` NOT run beyond check-report/check-interpret | **COMMITTED** — `make check-report` (OK, all suites including the 15-test matrix-page suite and the schema-example smoke) and `make check-interpret` (249/249, six sections, including section 3's 76/76 sidecar-freshness check over the live index) both run; no `make check-harness`/`check-schema`/`check-upstream`, no full `make check` |
| Deliver `docs/dev/lanes/b122read_report.md` with a charter-vs-committed checklist, then end | **COMMITTED** — this file |

## 3. How the numbers were produced

- All 16 `pcrecbench report` renders (8 groups × tsv/md) used the CLI
  directly, `--store store --subbench <name> --version <ver> --machine
  budu-ryzen1600 --testee <id>...`, with every pcrec testee's PRIOR-pin
  sibling named alongside the new one (the render-mechanic fix, finding
  1). Testee rosters match the 2026-10-02 b120b121read groups minus the
  arms not measured this window (nohybreseed/dfa/vm-nocaps/noedge/
  noisland) plus litrun's own first-sample roster's comparator
  (libpcre2-jit only).
- Every K81/K82/K83 number and every §6 finding was read DIRECTLY from
  the committed TSV's `rank` section (`awk -F'\t'` filters on `$1=="rank"
  && $2==<pattern> && $7==<testee>`, `$11` the metric name) — no number
  was computed by hand beyond the one ns/B division for "customers
  union-select" (997,001.28 → 465,668.87 ns over 1,376,256 B, the set's
  own throughput byte total from `bench/capability/manifest_
  throughput.tsv`). The `delta_verdict` column (last field) is the
  reporter's own R8 verdict, read verbatim, never recomputed.
- The pcrec wrong-answer scan: `grep` over each sidecar's own rendered
  `R-STATUS-3` ("EXCLUDED from ranking") lines for `pcrec_c4c70f2c` and
  a nonzero "wrong answer(s)" count, cross-checked against the same
  pattern's prior-pin reading in the already-committed 2026-10-02
  sidecar.
- The census attribution (§2 of the ledger) is pcrec's own
  `docs/dev/measurements/2026-10-04-b122-census.txt`, produced by lane
  b122repin — carried here verbatim (summary block + the per-set
  breakdown + the 64-row flagless-attribution list), not re-derived or
  independently verified against pcrec's source diff.

## 4. Validation

- All eight sidecars determinism-checked: a second `interpret --render`
  to stdout diffs byte-identical against each committed file (checked
  twice — once right after first render, once after the re-render with
  the prior-pin testee added).
- `make check-report`: OK (reporter unit tests, the matrix-page suite,
  schema-example fixtures, CLI smoke over the fixture store — never
  touches `store/`).
- `make check-interpret`: 249/249 across six sections, including
  section 3's sidecar-freshness re-render against the LIVE
  `store/index.tsv` (76/76) — confirms all eight new sidecars (and
  every pre-existing one) are not stale.
- No `make check-harness`/`check-schema`/`check-upstream`/full `make
  check` run (per the brief's explicit RAM/BOX GATE instruction).
- No store write beyond the 16 pre-existing records the window itself
  wrote (this lane only READ the store via `pcrecbench report`/
  `interpret`; it never ran `pcrecbench run`).

## 5. OWED

Nothing is OWED. The two unresolved citations (K81's "short-call",
K82's "short union-srch calls") are not OWED work on this lane's part
— they are explicitly flagged questions FOR pcrecdev1 in both the
ledger (§3, §6 item 4) and the outbox draft, exactly as this project's
Q5 precedent handles an unlocatable citation: ask, do not guess. A full
systematic sweep of every (pattern, regime, testee) cell across all
eight reports for movers beyond the named K81-K83 population was NOT
run (§5 of the ledger states this explicitly) — the two beyond-ask
findings (ci-ascii-control, alt-shared-char) came from a spot check on
utf8's largest-magnitude rows, and a future lane could run the full
sweep if the manager wants one.
