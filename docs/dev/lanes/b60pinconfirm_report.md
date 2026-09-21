# Lane b60pinconfirm — [B58] pin's acceptance AFTER on the MEASURED axis

Charter (team-lead brief, 2026-09-20): the [B58] re-pin (pcrec cf0962e3
-> 25b1984f, abi 26 -> 27, [EMIT-VERB]/D112 -- emitted comments off by
default) claims that NOTHING measuring TIME or OBJECT SIZE moves. The
[B58] lane (`b58repin`) proved the SIZE half statically (object bytes
identical except the abi literal). This lane measures the TIME half.

## 0. Design (stated before the run)

`store/index.tsv` was grepped directly before choosing cells: the ONLY
`cf0962e3`-measured (subbench, pcrec-testee) tuples anywhere in the store
are the four `bench/capability@0.1` cells written 2026-09-18 by the
[B48] cross-pin AFTER window (`pcrec_cf0962e3_{auto,auto-nocaps,vm,
vm-in}-caps-simdna`; every other set's newest pcrec sample is an older
pin -- `1989c62`/`334fd10e`/`d34c9131`/etc.). This is a data-availability
fact, not a design choice: a genuine single-variable cf0962e3 ->
25b1984f comparison is possible on `bench/capability@0.1` and NOWHERE
else in the store today. The brief's "6-8 cells across two sub-benches"
target is therefore not reachable honestly; **4 cells, one sub-bench**,
matching the [B48] AFTER's own four-testee shape exactly, is what this
window runs:

| cell | testee | route | comparison record (cf0962e3, 2026-09-18) |
|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | DFA/auto route, captures on | `capability@0.1__pcrec_cf0962e3_auto-caps-simdna__budu-ryzen1600__20260918T011054Z` |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | DFA/auto route, captures off | `capability@0.1__pcrec_cf0962e3_auto-nocaps-simdna__budu-ryzen1600__20260918T014138Z` |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | VM forced, captures on | `capability@0.1__pcrec_cf0962e3_vm-caps-simdna__budu-ryzen1600__20260918T021057Z` |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | VM forced, caller buffer | `capability@0.1__pcrec_cf0962e3_vm-in-caps-simdna__budu-ryzen1600__20260918T025149Z` |

Both engine routes are covered (P1/P2 = DFA/auto-selectable, P3/P4 = VM
forced); the regime spread within `bench/capability@0.1` itself covers
`short-subject-search` and `large-subject-throughput` (no separate
compile-only regime in this set beyond the compile rows every cell
already carries).

## 1. Predictions (committed BEFORE the run)

`docs/dev/predictions/capability-0.1-pin-25b1984f-confirm.tsv` (commit
3cd3305), 4 parents (P1-P4, one per testee above), single clause each:
`quantity=delta_verdict; reducer=identity; op=eq-token; hi=unchanged
(within spread)` -- the report's own R8 cross-pin rule
(`_cross_pin_verdict`, spread = 2x the larger of the two cells' own
trial stddev) applied to EVERY ranked row for that testee. Grounding
(stated in the file, not invented): the identical four-testee
population's LAST cross-pin comparison (a770139e -> cf0962e3,
`reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv`)
read 451/488 non-blank rank rows exactly `unchanged (within spread)`,
every other row within ±×1.04 except two cells at ×2.00 that were an
EXPLAINED real fix (mojibake-curly-quote, I-72) -- so this strict
eq-token op is EXPECTED to register some ordinary boundary jitter as
"refuted" by construction; this report reads each non-matching row's
own ratio against that ≤×1.04 historical ceiling to separate ordinary
spread from a genuine mover.

**KNOWN GAP, documented before scoring (not found live)**: this file's
population necessarily includes the already-measured `pcrec_cf0962e3_*`
records (required for `delta_verdict` to exist), so
`check_stated_utc`'s F27 re-anchor refuses the normal
`pcrecbench interpret --predictions ... --render` CLI path -- the exact
"second sample of an already-measured population" case
`docs/dev/predictions/CLAUDE.md`'s `capability-0.1-ext-roster.tsv` entry
(finding 1) already names as structurally unfixable without a ruling.
Scored via a direct `interpret.evaluate_predictions` call (bypassing
only `check_stated_utc`), same precedent as that file.

## 2. Window

Launched 2026-09-20 18:33:35 EDT, quiet-gate VERDICT quiet immediately
before launch (load1 0.63-1.14, max_busy_pct <=2.8%, both `quiet
--samples 5` and a `--samples 3` re-check). `SUBBENCH=capability
TESTEES="pcrec-auto pcrec-nocaps pcrec-vm pcrec-vm-in" TRIALS=5
STORE=store PIN=11 CELL_CAP=5400`, detached under `setsid … & disown`
(the boilerplate's long-run rule -- capability cells ran 25-42 min each
at the [B48] AFTER, ~2-3h total expected for four).

LOG: `build/windows/window_capability_pinconfirm_20260920T223335Z.log`
(gitignored under `build/`, referenced by path per convention).

STATUS: **COMPLETE.** `WINDOW_RUN_COMPLETE cells=4/4` at 2026-09-20
21:01:16 EDT. This section was written before the run completed per
DO-THEN-FINISH; lane b60close (the fresh follow-up agent finishing this
lane's OWED items) filled every item below in from the finished
log/report/index.

## 3. Results

- **Per-cell attempt count, wall time, final status** (all four:
  attempt 1, rc=0, status `measured`; window log lines 324-330,
  651-657, 974-980, 1297-1303):

  | cell | testee | started (record_id timestamp) | attempt completed (EDT) | wall |
  |---|---|---|---|---|
  | 1 | `pcrec_25b1984f_auto-caps-simdna` | 2026-09-20T22:34:10Z | 19:06:53 | ~33m18s (from window start 18:33:35) |
  | 2 | `pcrec_25b1984f_auto-nocaps-simdna` | 2026-09-20T23:07:14Z | 19:35:31 | ~28m38s |
  | 3 | `pcrec_25b1984f_vm-caps-simdna` | 2026-09-20T23:35:51Z | 20:17:47 | ~42m16s |
  | 4 | `pcrec_25b1984f_vm-in-caps-simdna` | 2026-09-21T00:18:07Z | 21:00:59 | ~43m12s |

  Total window wall time: 18:33:35 -> 21:01:16 EDT, ~2h27m41s (inside
  the §2 estimate of ~2-3h for four cells). Each record's own
  `agreement` line reads `agree` (0 groups disagreeing on each of
  124/126/124/124 groups; 4/5/5/5 of ~4800-4900 rows unjudged at
  k=1.5, 2/3, 5 trials — all within normal trial-agreement noise, none
  triggering `inconclusive-spread`).

- **`store/index.tsv` before/after count**: 186 -> 190 records (window
  log: "index: 190 record(s) -> store/index.tsv"; `git diff --stat`
  against the pre-window commit confirms +4 lines). Store-wide status
  breakdown at close: measured 179, inconclusive-load 9,
  inconclusive-spread 2 (unrelated pre-existing records; none of this
  window's four cells fell into either non-measured bucket).

- **Cross-pin report group**:
  `reports/2026-09-20-capability-0.1-budu-ryzen1600-pinconfirm-
  25b1984f.{md,tsv,subject-grain.md,subject-grain.tsv,matrix.tsv,
  matrix.html}`, rendered from the eleven-testee roster (three pcre2
  baselines + four `pcrec_cf0962e3_*` + four `pcrec_25b1984f_*`),
  `--since 2026-09-17T00:00:00Z --until 2026-09-21T01:10:00Z` (brackets
  the pcre2 baselines' 2026-09-17 newest records, cf0962e3's
  2026-09-18 records and this window's 2026-09-20/21 25b1984f records;
  the bracket also spans the a770139e records from 2026-09-17 -- those
  are excluded by the explicit `--testee` roster, not by date).
  **Header: "12 record(s) matching this query; records: 11;
  excluded_invalid: 0; superseded: 1"** -- the roster's 11 testees are
  ALL present (the pcre2 baselines' newest capability records are still
  the 2026-09-17 first-sample ones; no pcre2 baseline was remeasured
  since, confirmed by grep of `store/index.tsv`); the one superseded
  record is the same pcre2-dfa `inconclusive-spread` history row the
  [B48] AFTER precedent (`2026-09-18-*-after-cf0962e3.md`) also
  supersedes. 128 matrix rows, 11 testees. R8 Δ column present
  throughout (`delta_verdict` populated on every ranked row with a
  cross-pin comparator). **One correction made mid-lane**: the first
  `.subject-grain.tsv` render used the FULL subject-grain shape
  (56.6 MB) instead of the committed convention's `--subject-grain-
  slice` (report.py's own documented rule: "this is the shape a
  committed `.subject-grain.tsv` takes"); caught by comparing against
  the [B48] precedent's 11 MB file, fixed and recommitted at 10.3 MB
  (commit 7a59d05).

- **`.interpretation.md` sidecar**: generated via `pcrecbench interpret
  reports/2026-09-20-capability-0.1-budu-ryzen1600-pinconfirm-25b1984f.tsv
  --index store/index.tsv --subject-grain <same>.subject-grain.tsv
  --render --out <same>.interpretation.md`, no `--predictions` (the
  documented F27 gap: this population necessarily includes the
  already-measured `pcrec_cf0962e3_*` records, so `check_stated_utc`'s
  re-anchor refuses the CLI's `--predictions` path). Determinism: an
  independent re-run to a scratch path diffed **byte-identical**
  against the committed file.

- **Predictions scoring** (direct `interpret.evaluate_predictions`
  call, same precedent as `capability-0.1-ext-roster.tsv`): **P1-P4 all
  REFUTED.**

  | pred | testee | verdict | n ranked values | distinct non-"unchanged" tokens seen |
  |---|---|---|---|---|
  | P1 | `pcrec_25b1984f_auto-caps-simdna` | refuted | 738 | faster ×1.01, faster ×1.02, slower ×1.00, slower ×1.01, slower ×1.04, slower ×1.07 |
  | P2 | `pcrec_25b1984f_auto-nocaps-simdna` | refuted | 750 | faster ×1.01, faster ×1.07, slower ×1.01, slower ×1.02, slower ×1.03 |
  | P3 | `pcrec_25b1984f_vm-caps-simdna` | refuted | 732 | faster ×1.00, faster ×1.01, slower ×1.00, slower ×1.01, slower ×1.04 |
  | P4 | `pcrec_25b1984f_vm-in-caps-simdna` | refuted | 732 | faster ×1.01, faster ×1.02, faster ×1.04, faster ×1.05, slower ×1.01, slower ×1.08 |

  All four refutations are exactly the predictions file's own stated
  grounding: a strict `eq-token "unchanged (within spread)"` clause
  registers ordinary trial-level boundary jitter as refuted by
  construction (every ratio here is in [1.00, 1.08]; the historical
  ceiling from the a770139e -> cf0962e3 comparison this file's
  grounding cites was ≤×1.04 except two EXPLAINED real-fix cells at
  ×2.00 -- nothing here reaches ×2.00). Refutation alone is therefore
  NOT itself the systematic-mover finding; see below.

  **A second, unplanned finding while scoring**: `evaluate_predictions`
  crashed outright on the unpatched call (`TypeError: bad operand type
  for abs(): 'str'`) -- `docs/dev/known_issues.md` KB-24, a genuine
  interpreter bug (`_measured_text` assumes every `identity`-reduced
  "num"-kind value is numeric; `delta_verdict`'s values are string
  tokens, and this is the FIRST predictions file ever to name
  `quantity=delta_verdict`). Scored via a scratch monkeypatch of the
  broken formatting helper only (`_op_holds`, the real confirm/refute
  predicate, is string-safe and untouched -- the crash reproduced first,
  unpatched, to confirm the finding before the workaround ran). Full
  writeup, workaround code and two fix candidates in KB-24.

- **THE FINDING THIS WINDOW EXISTS TO SURFACE, PER THE CHARTER'S
  QUESTION OF THE NIGHT** (read from R-DELTA-1's 32 firings, aggregated
  to 14 by regime × config × direction in the sidecar; every ratio in
  [1.00, 1.08]):

  **ONE genuine, tight, isolated systematic mover, not absorbed into
  ordinary spread**: `wild-datetime-moment-iso8601` /
  `short-subject-search` / `pcrec_25b1984f_vm-in-caps-simdna` reads
  **slower ×1.08** -- median 6,298.939973ns (cf0962e3) -> 6,808.083837ns
  (25b1984f), stddev 2.783444ns / 1.768220ns respectively. The delta
  (509.14ns) is **~91× the rule's own 2×stddev spread threshold**
  (2×2.783444 = 5.567ns) -- not a boundary-jitter case, a real,
  reproducible, tightly-bounded move (min-max span ~9ns and ~5.5ns on
  each side). Critically, **the SAME pattern on every OTHER pcrec route
  in this window reads `unchanged (within spread)`**:
  `auto-nocaps-simdna` (589.85ns vs 590.78ns), `auto-caps-simdna`
  (982.32ns vs 985.35ns), `vm-caps-simdna` (6,322.74ns vs 6,323.65ns) --
  all four routes measure this pattern's search cost, and only the
  caller-provided-frame-buffer route (`pcrec-vm-in`) moved. This is
  isolated by CONSTRUCTION to the one route [EMIT-VERB]'s
  comment-stripping (or something correlated with the same pin range)
  touches differently: `pcrec-vm-in` is not merely `pcrec-vm` with a
  supplied buffer, it is compiled/driven through a distinct code path
  ([B8]'s caller-provided frame-buffer testee). Everything else flagged
  by R-DELTA-1 (31 of the 32 firings) sits inside or barely above the
  ≤×1.04 historical ordinary-jitter ceiling this file's own grounding
  cites (the next-largest, `phone-palindrome-6` / `large-subject-
  throughput` / `auto-caps-simdna`, slower ×1.07, is marginal: diff
  456,755ns against 2×stddev = 369,336.6ns, only ~1.24× the threshold,
  n=3 trials only -- plausibly ordinary spread under a small trial
  count, unlike the iso8601 cell's ~91×).

  **FOR THE MANAGER'S OUTBOX, stated plainly and not absorbed**:
  [B58]/[EMIT-VERB]/D112's claim was that NOTHING measuring TIME moves
  between cf0962e3 and 25b1984f. This ONE cell is a counterexample by
  the report's own math, isolated to the `vm-in` route, on one pattern
  out of the set. Whether this is a real, small, `vm-in`-specific
  regression worth a pcrec ask, or noise this project's ≤×1.04 ceiling
  heuristic was too loose to catch until now, is a call for the
  manager/Frank, not this lane -- the charter's own instruction is to
  flag it, never explain it away.

## 4. Charter-vs-committed checklist

- [x] 4-8 cells spanning two engine routes and (where the store allows)
      two sub-benches with different regimes — **DELIVERED AS DESIGNED,
      NOT AS ORIGINALLY SCOPED**: 4 cells, one sub-bench, both engine
      routes — the store holds no second sub-bench's cf0962e3 sample: see
      §0.
- [x] Predictions committed before the window — DONE (commit 3cd3305).
- [x] Windows via scripts/run_window.sh, sequential, quiet gate as-is,
      generators run first — DONE (generators re-run in this worktree;
      quiet gate verdict quiet at launch).
- [x] Index — DONE (186 -> 190 records, commit 58c2d47).
- [x] Cross-pin report group with R8 Δ column — DONE (commits 33e0692,
      7a59d05 for the subject-grain-slice fix).
- [x] Interpretation sidecar(s) via `pcrecbench interpret` — DONE
      (commit d760983; predictions half scored by direct call, not the
      CLI path, per the documented F27 gap; a second interpreter bug,
      KB-24, found and worked around in the process).
- [x] Any systematic time mover flagged prominently for the manager's
      outbox, not absorbed — DONE, §3 above: the `wild-datetime-
      moment-iso8601` / `vm-in-caps-simdna` ×1.08 cell.
- [x] `reports/CLAUDE.md` updated with the new group's entry.
- [x] Committed incrementally (predictions commit, pre-run report
      commit, window-outputs commit, report-group commit,
      subject-grain-slice fix commit, sidecar commit, this closing
      commit).

## 5. Handback summary (lane b60close)

- **Scoring verdicts**: P1-P4 (all four pcrec testees) REFUTED under
  the strict `eq-token` op, exactly as the file's own grounding
  anticipated (ordinary boundary jitter registers as refuted by
  construction; not itself a mover finding). See the table in §3.
- **The Δ answer**: 31 of 32 R-DELTA-1 firings are ordinary spread
  (≤×1.07, most well inside the historical ≤×1.04 ceiling, none
  reaching the ×2.00 the last real-fix cells hit). ONE genuine mover:
  `wild-datetime-moment-iso8601` on `pcrec_25b1984f_vm-in-caps-simdna`,
  slower ×1.08, ~91× the spread threshold, isolated to the `vm-in`
  route alone (every other pcrec route reads unchanged on this exact
  pattern).
- **Record count**: store/index.tsv 186 -> 190 (+4, all `measured`
  attempt 1). Report group: 12 candidate records, 11 included, 1
  superseded (pcre2-dfa history row).
- **New finding beyond the charter**: `docs/dev/known_issues.md` KB-24
  -- `interpret.evaluate_predictions` crashes on any `quantity=
  delta_verdict` clause (first one ever authored); worked around by a
  scratch monkeypatch, not fixed in `pcrecbench/interpret.py` (a
  scoring lane's call, not this lane's to make without a ruling).
- **Commit list** (branch `lane/b60pinconfirm`, oldest to newest):
  `3cd3305` predictions, `f9af6d3` pre-run report, `58c2d47` window
  outputs (records + index + sidecars), `33e0692` report group,
  `7a59d05` subject-grain-slice fix, `d760983` interpretation sidecar,
  plus this commit (KB-24 + predictions/CLAUDE.md + reports/CLAUDE.md +
  this report's closing section). Not merged — the manager merges.
