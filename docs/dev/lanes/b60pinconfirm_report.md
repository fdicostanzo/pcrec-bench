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

LOG (OWED, filled at close): `build/windows/window_capability_pinconfirm_20260920T223335Z.log`

STATUS: OWED -- window in progress. This report is written and
committed BEFORE the run completes per the boilerplate's DO-THEN-FINISH
discipline; a later commit on this branch fills in every OWED item below
from the finished log/report/index rather than replacing this section.

## 3. Results — OWED

- Per-cell attempt count, wall time, final status: OWED (from the LOG).
- `store/index.tsv` before/after count: OWED.
- Cross-pin report (`reports/2026-09-2?-capability-0.1-budu-ryzen1600-
  pinconfirm-25b1984f.{md,tsv,subject-grain.md,subject-grain.tsv,
  matrix.tsv,matrix.html}`), rendered from an explicit `--testee` roster
  naming all 8 pcrec testee_ids (cf0962e3 + 25b1984f) plus the three
  pcre2 baselines, per `reports/CLAUDE.md`'s KB-5 cross-pin convention:
  OWED.
- `.interpretation.md` sidecar (catalogue rules over the report/index,
  no `--predictions` -- the F27 gap above): OWED.
- Predictions scoring (direct `evaluate_predictions` call): OWED, per
  clause P1-P4.
- **THE FINDING THIS WINDOW EXISTS TO SURFACE**: any systematic time
  mover beyond the stated spread -- OWED. Per the charter, this is
  reported here for the manager's outbox, never absorbed or explained
  away by this lane.

## 4. Charter-vs-committed checklist

- [ ] 4-8 cells spanning two engine routes and (where the store allows)
      two sub-benches with different regimes — **DELIVERED AS DESIGNED,
      NOT AS ORIGINALLY SCOPED**: 4 cells, one sub-bench, both engine
      routes — the store holds no second sub-bench's cf0962e3 sample: see
      §0.
- [ ] Predictions committed before the window — DONE (commit 3cd3305).
- [ ] Windows via scripts/run_window.sh, sequential, quiet gate as-is,
      generators run first — DONE (generators re-run in this worktree;
      quiet gate verdict quiet at launch).
- [ ] Index — OWED.
- [ ] Cross-pin report group with R8 Δ column — OWED.
- [ ] Interpretation sidecar(s) via `pcrecbench interpret` — OWED
      (predictions half scored by direct call, not the CLI path, per the
      documented F27 gap).
- [ ] Any systematic time mover flagged prominently for the manager's
      outbox, not absorbed — OWED.
- [ ] Committed incrementally — DONE so far (predictions commit,
      pre-run report commit); more commits to follow as the window and
      analysis complete.
