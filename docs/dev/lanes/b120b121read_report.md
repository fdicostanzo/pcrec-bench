# lane b120b121read report — the [B120]/[B121] window READ, pcrec fc719ca4

Branch `lane/b120b121read`, worktree `worktrees/b120b121read`, base
`3032122` ("merge lane/b121asks ..."). Window commit `fa5ba8c` ([B120]
item 3 + [B121] A5, 25 cells at pcrec fc719ca4, 23 measured at attempt
1, syntax `pcrec-vm-nocaps` `inconclusive-spread` TWICE). `~/pcrec` was
not touched (read-only, as always).

**Revision note**: this report's first draft misapplied the reporter's
20-microsecond COMPILE-jitter timer floor ([B14] R5) to match/search
median_ns cells, which are harness-calibrated per-call means over
~50 ms loops (Contract 3), not single clock reads — the exclusion was
wrong and withdrawn after the manager's review. Findings 2/3/4 below
are corrected accordingly (all re-derived from the records' own spread,
`gap > 2×max(stddev)`, never a flat ns threshold); the utf8 roster gap
(finding 4) is now FIXED, not merely diagnosed.

## 1. Findings first

1. **Step 0 PROVES the probe's own flagged bimodal cell is a
   governor-lottery artifact, not a real effect.** `asr-lb-fixed`/gcc/
   `synth-64k-asc` (default vs `-fno-hyb-reseed`), 45 fresh unpinned
   launches/arm + 15 `taskset -c 3` launches/arm: unpinned, both arms
   draw from the SAME two governor states at different lottery weights
   (min/min ratio 0.9996); pinned to one core the bimodality vanishes
   on both arms (0/15 slow each) and the medians agree to four figures
   (ratio 0.9999). Drops [B120]'s own named XCALL-trigger population
   from four cells to three real ones.
2. **The real window's per-pattern `vm_reseed`×`vm_frameless` bucket
   finds ALL TEN raw ">5% slower" syntax@0.1 cells are REAL** (by the
   records' own `gap > 2×max(stddev)` criterion, not a timer floor),
   beyond the six the predecessor probe already found: `grp-atomic-
   alt`/short-subject-search (×1.0640) and /large-subject-throughput
   (×1.0536), `lka-nonatomic`/short-subject-search (×1.0566) — the
   other seven are slower variants of patterns the probe already named
   at other regimes. Every gap clears its own noise floor, several by
   one to two orders of magnitude.
3. **capability@0.1's 1c prediction (clamped rows do not move) is
   CONFIRMED cleanly**, now on the same statistical basis, on all six
   real clamped cells. Its one `adaptive-dense` witness
   (`logparse-atomic`) splits in two: large-subject-throughput is
   genuinely flat for a STRUCTURAL reason — `vm_start=anchored` (the
   pattern is `^`-anchored, no MULTILINE, so only offset 0 is ever
   attempted and all three throughput subjects read `nomatch` there),
   NOT [B117]'s own zero-occurrence-necessary-byte mechanism (its
   `": "` run occurs 547-9,070 times in those subjects, checked
   directly) — while short-subject-search IS real (×1.0690, 6.6× its
   own noise floor), capability@0.1's one genuine XCALL trigger.
4. **A roster-declaration gap made utf8@0.1's real window cell
   unreadable for the per-pattern adaptive bucket — FIXED in this
   lane.** `pcrec-auto-nohybreseed-utf8` (and the two untested clang
   siblings) had no entry in `bench/utf8/gen_patterns.py`'s
   `EXT_BENCH_ROSTER`, so 73 of 76 patterns rendered `unsupported-by-
   declaration` and only 3 (all DFA-routed, zero `vm_reseed` stamp)
   ranked. All three now carry `pcrec-auto-utf8`'s own declaration
   (verified: `missing_capabilities()` now reads 5/76, matching the
   documented [B77] U2 gap on the other three `-utf8` siblings;
   `gen_patterns.py --check`, `check_rxt_export` and
   `check_capability_roster_coverage` all green). Per the manager's
   explicit instruction, the cell itself is NOT re-run and the utf8
   report is NOT regenerated in this lane — both are **OWED (manager,
   post-merge)**.
5. **A2(2) inverts I-125's own framing.** `qnt-counted-3b`'s `auto`
   (DFA) route is already ×29.7 faster than forced VM and ×2.19/×1.95
   behind the two fastest algorithmic engines (rust, vectorscan) — the
   DFA route is NOT losing to the VM's counter loop on this witness.
6. **A4/P20 is confirmed at a far larger margin than the compile-only
   census implied**: altwide@0.3's class-tail forced-VM route is
   ×25-229 slower than the plain ladder's own island arm, across every
   regime measured.
7. **Q3's forced-DFA "reverse population" is empty in real TIMING,
   not only in compile identity**: 0/191 syntax@0.1 common-cell movers
   >5%, 2/83 capability@0.1 movers — both program-identical artifacts
   by construction, so any apparent move there is noise regardless of
   its absolute ns scale.
8. **`pcrec-vm-nocaps` on syntax@0.1 has NO `measured` record at this
   pin, and the cause is TWO real, reproducible disagreeing groups**
   (re-derived directly from both record JSONLs, not merely the
   report's "worst group" summary): `cls-h` (likely trial noise at a
   sub-microsecond-per-call scale) and `rec-define` (a genuine ~14%
   run-to-run coefficient of variation on a multi-millisecond
   recursion pattern — not noise). The one re-measure `run_window.sh`
   allows made `cls-h` WORSE (d 28→39 of 42), not better.
9. A2(3) (loglines scan-edge) and Q9/Q10/A3 read unchanged from the
   predecessor lanes' own drafts — confirmed now with real numbers
   where a timed ratio was owed.

## LESSON for the standing process

**Any new pcrec testee (a deny flag, a compiler variant, a buffer-
capacity sibling) needs EVERY set's own roster/requires gate checked
before it is pointed at a real window — not only `bench/capability`'s
[B111]-gated one.** This is the THIRD time this exact gap class has
bitten a new testee silently (`pcrec-auto-nolitrun`, O-64/O-65; the
`-align64loops` pair, [B110]; now the three new `-utf8` siblings on
`bench/utf8`, this lane). `bench/capability` has an automated check
(`check_capability_roster_coverage`, [B111]) that fails BY NAME on an
unlisted testee id; `bench/utf8` and every other `ext bench`-bearing
set do not — building the equivalent check for every set that carries
a roster is a real follow-up, not done here (out of this lane's own
read-and-fix-what-broke scope).

## 2. Charter-vs-committed checklist

| brief item | status |
|---|---|
| Step 0: re-measure the flagged bimodal cell, 45/15 launches, `quiet` first, archived with a source header | **COMMITTED** — `docs/dev/measurements/probe_b120b121read_step0_pin_control.py` / `2026-10-02-b120b121read-step0-pin-control.txt`; answer: the ×0.49/×2.03 inversion does NOT survive pinning |
| Step 1: report group for {syntax,capability,utf8}@0.1 × {auto, nohybreseed}; bucket per pattern by RX_VM_RESEED × RX_VM_FRAMELESS; name every adaptive* cell >5% slower; test 1c; Q11/lka-pos answer; confirm answers identical before timing | **COMMITTED** — `reports/2026-10-02-{syntax,capability,utf8}-0.1-...-fc719ca4.{tsv,md}`; the bucket probe + its findings in `docs/dev/ledgers/2026-10-02-b120-b121-fc719ca4.md` §1 (corrected per the manager's review — every real cell named, the noise criterion is the records' own spread, not a timer floor); 1c CONFIRMED on capability@0.1 on the same basis; Q11 answered; answer identity checked at the FULL population level before any ratio was trusted |
| Step 2: report groups for every set the window touched; ledger with pcrec's stamps per row; A2(2)/A2(3)/A4/Q3/the syntax inconclusive-spread diagnosis; regenerate sidecars | **COMMITTED** — `reports/2026-10-02-{loglines-0.1,bounded-0.3,email-specimen-0.2,altwide-0.3}-...-fc719ca4.{tsv,md}`; ledger §2-§3; all seven new sidecars generated via the `/pcrec-bench-interpret` skill's exact procedure, determinism-checked |
| Step 3: two outbox DRAFTS (not written to outbox_to_pcrec.md) | **COMMITTED** — `docs/dev/lanes/b120b121read_outbox_I124.md`, `..._I125.md`, both whole answers superseding the two predecessor-lane drafts, with the manager's corrections applied (Step 1's redo, the utf8 fix-not-dead-end, Q5/Q12) |
| Step 4: re-run `make cc-gate-census`, report parity/divergence, archive it | see §5 below — run to completion in this lane per the manager's explicit instruction to finish it before ending |
| Manager review item (1): redo item 3's bucketing without the timer-floor exclusion; name every adaptive* cell >5% slower using the records' own spread; check logparse-atomic's RX_REQ_BYTE before calling anything flat | **COMMITTED** — see finding 2/3 above and the ledger's corrected §1 |
| Manager review item (2): fix the utf8 roster gap bench-side (same declaration as pcrec-auto-utf8); check the clang siblings; check gen_patterns.py --check and roster-coverage; do NOT re-run the cell or regenerate the report; mark it OWED; add the lesson line | **COMMITTED** — `bench/utf8/gen_patterns.py`/`patterns.rxt` fixed and verified green; utf8 item 3 marked OWED (manager, post-merge) in the ledger and both drafts; the lesson line is above |
| Deliverables: committed reports, sidecars, ledger, the two drafts, archives, `docs/dev/lanes/b120b121read_report.md` with a charter-vs-committed checklist; keep CLAUDE.md files current | **COMMITTED** — `docs/dev/ledgers/CLAUDE.md`, `reports/CLAUDE.md`, `docs/dev/measurements/CLAUDE.md` all updated; `docs/dev/plan.md`'s [B120]/[B121] rows marked `STATE:completed` (plan.md's own summary text there still reads the PRE-correction numbers from before the manager's review — see OWED below) |

## 3. How the numbers were produced

- The seven report groups were rendered via the CLI directly
  (`pcrecbench report --format {tsv,md}`, explicit `--testee` values
  per set, `--include-unmeasured` only where the syntax `pcrec-vm-
  nocaps` record needed it). `syntax`'s render took ~5 min wall
  (1.1 GB peak RSS, measured with `/usr/bin/time -v` on a rehearsal
  query), run in the foreground via `&`/`disown` chains rather than a
  `setsid`+marker (each individual render stayed under the BOILERPLATE's
  ~4-minute DO-THEN-FINISH threshold once run one at a time; the chains
  themselves were launched disowned and polled by file existence /
  process liveness — Monitor notifications on this session lagged
  significantly more than once and were not trusted as the sole
  liveness check after the first miss).
- Every ratio/table in the ledger was computed directly from the
  committed report TSVs by standalone scripts (inline `python3 -c`
  one-offs for the cross-join tables, committed only as
  `docs/dev/measurements/probe_b120b121read_resecompat_bucket.py` for
  the per-pattern `vm_reseed` bucket, which reads the record JSONL
  directly rather than the report's own per-testee `compile_stamp`
  legend). The noise criterion (`gap > 2×max(stddev)`) reads both
  arms' own `stddev_ns` rank rows from the same report TSV — never a
  constant.
- `logparse-atomic`'s mechanism check: `req_byte`/`req_run`/`req_why`/
  `vm_start` read directly from the record's own `engine_metadata`;
  the `": "` occurrence count was a direct byte-count over the
  regenerated, sha256-verified `bench/capability/throughput/*.bin`
  files (gitignored, deterministic); the `nomatch` confirmation is
  `bench/capability/expectations.tsv`'s own oracle-derived rows.
- The `pcrec-vm-nocaps` disagreeing-group diagnosis replicates
  `pcrecbench.reduce.judge_trial_agreement`'s own per-group arithmetic
  inline (imported `_row_key`/`_ns_per_iter_judged`/`TIMED_OUT` and the
  three rule constants directly from that module, never retyped) to
  recover BOTH disagreeing groups per record, since the shared
  function's own `trial_agreement` block keeps only the single `worst_
  group`.
- The utf8@0.1 roster-gap fix: `bench/utf8/gen_patterns.py`'s
  `EXT_BENCH_ROSTER` table edited directly (three new rows, each
  `pcrec-auto-utf8`'s own declaration verbatim), `gen_patterns.py` run
  to regenerate `patterns.rxt`, then verified via `missing_
  capabilities()` directly (5/76, not inferred) and `tools.selfcheck.
  check_rxt_export()`/`check_capability_roster_coverage()` called
  directly (both green).
- Record provenance: `store/index.tsv`'s own fc719ca4 rows (37 total
  across the seven sets at authoring time), cross-checked against each
  report header's own `records: N; superseded: M` count.

## 4. Validation

- All seven sidecars regenerated and determinism-checked (a second
  `interpret --render` to stdout diffs byte-identical against each
  committed file).
- The utf8 roster fix verified three ways: `python3 bench/utf8/
  gen_patterns.py --check` clean; `tools.selfcheck.check_rxt_export()`
  green (utf8's own row, 76 patterns, round-trips); `tools.selfcheck.
  check_capability_roster_coverage()` green (unaffected — a different
  set's roster, confirmed not to regress).
- No `make check`/`make check-harness`/`make check-report`/`make
  check-interpret` full run in this lane (no reporter, harness,
  interpreter or catalogue code was touched — report outputs, one
  bench-side roster fix, one new measurement probe, docs, and
  plan.md).
- No store write, no new pinned-tier measurement beyond Step 0's own
  SCRATCH-tier multilaunch probe (never `store/`, by construction —
  the same protocol `probe_b120_reseed_multilaunch.py` already used).

## 5. OWED

- **utf8@0.1 item 3's own re-run and report regeneration**: per the
  manager's explicit instruction, NOT done in this lane. The manager
  re-runs `pcrecbench run --subbench utf8 --testee pcrec-auto-
  nohybreseed-utf8` (now that the roster fix is merged) and
  regenerates `reports/2026-10-02-utf8-0.1-...-fc719ca4.{tsv,md,
  interpretation.md}` after merge.
- **`make cc-gate-census`'s own archive**: run to completion in this
  lane (the manager's explicit instruction to finish Step 4 before
  ending, checking its DONE marker directly rather than relying on a
  notification) — see the commit that lands beside this report for
  the final parity verdict and the archived `.txt` file; if this
  sentence is still here unedited, the run had not yet finished when
  this report was last written and the marker (`/tmp/ccgate.log`'s
  trailing `DONE rc=<N>` line) should be checked directly.
