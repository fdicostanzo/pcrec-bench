# lane b43giveup — the batched-give-up misclassification fix (KB-20)

Branch `lane/b43giveup`, worktree `worktrees/b43giveup`, off `master`
(`c5180ed`). DO-THEN-FINISH: this report is committed with the fix; no
background job is outstanding.

## The bug, and the fix

pcrec's per-search-call step budget fires correctly and cheaply on its
own terms (~2.5-2.8 s/call on the F3 witness, `evil-alt-nested` /
`rd-evil-alt-near-miss`). But the driver protocol's per-subject loop
(`testees/pcrec/driver.c`: `for (it = 0; it < iters; it++) { ... }`)
never breaks early on a give-up — it re-tries every iteration, keeping
only the last answer — and `pcrecbench/harness.py`'s calibration probe
sizes that loop at `iters` ≈ 200 for `search_short`/`match`
(`PROBE_ITERS`). So a give-up subject re-pays its engine's own give-up
cost ~200 times: ≈540 s against the 60 s per-subject alarm, recorded
`timed-out` where the true outcome is `gave-up`. The pcre2 reference
arms on the same cell read `gave-up` only because pcre2's per-call
give-up is cheap enough to fit its own 200-iteration batch inside the
alarm — so, before this fix, the RECORDED outcome depended on the
ENGINE's give-up cost, which is the class of harness artifact this bench
exists not to produce.

**The fix** (`pcrecbench/harness.py`): two new functions.

- `_first_call_outcomes(adapter, handle, regime, subjects, timeout)` —
  one iters=1 driver call over every subject in the regime, BEFORE any
  batch-sized call runs.
- `measure_regime_cell(adapter, handle, regime, subjects, requested_iters,
  trials, driver_timeout, subject_timeout, budget=None)` — the new seam
  `run_cell`'s per-regime loop calls in place of the old direct
  `calibrate()` + `adapter.measure()` pair. A subject whose first call
  gave up is pulled out of `calibrate()`'s probe (so its inflated
  per-iteration time cannot skew the median that sets `iters` for every
  OTHER subject either) and out of the batched timed run, and is instead
  measured on its own, at iters=1, for every trial. A give-up is now
  TERMINAL for its own (pattern, subject, regime) cell.

The recorded outcome is still the driver's own typed answer
(`giveup:<code>[:<name>]`, classified by the EXISTING
`harness.classify_giveup` range rule) — nothing is inferred from the
batch's timing, and nothing about the give-up row's SHAPE changes:
`record.match_row` never stamps a `timing` block on any outcome but
`matched-as-expected`, so a give-up row carries none today or after this
fix. This is a wall-time and correctness fix, not a schema change.

`run_cell`'s per-regime loop (`pcrecbench/harness.py`, around line 794)
now calls `measure_regime_cell` instead of `calibrate()` +
`adapter.measure()` directly; the `say()` progress messages were
reordered slightly (a "measuring ..." line now prints before the work
starts and a "measured ..." line with the final counts after — both
harmless liveness signals, not part of the record).

`harness.py`'s "prepare" section (`adapter.prepare`/`describe`/tier
refusal, around lines 570-600) is untouched — the change is entirely in
the per-regime measuring loop, well clear of lane l6bre2's pending hunk
there.

## THE NO-OP ARGUMENT, and its witness

**Argument.** `measure_regime_cell`'s no-give-up branch calibrates and
measures over the FULL, unchanged subject list — the exact two calls
(`calibrate()`, then `adapter.measure()`) `run_cell` made before this
function existed, in the same order, over the same list. The only
difference from the pre-fix path is the one extra iters=1 probe call,
whose rows are inspected and discarded: nothing it returns feeds
calibration, `n_iters`, or any row the function returns.

**Isolated witness (deterministic, seconds).**
`tools/selfcheck.py`'s `check_giveup_not_batched` runs
`measure_regime_cell` against a stub `Adapter.measure()` (never pcrec,
never a compile) whose timings are simulated numbers, not real ones —
so the comparison is exact, not noisy:

    testee's own numbers are a NO-OP: unaffected by s-giveup's presence
    n_iters=50000 both ways

i.e. calibrating/measuring `s-ok` ALONE reaches the identical `n_iters`
and the identical per-subject answers as the `s-ok` slice of a
two-subject cell that also contains `s-giveup`. 6/6 PASS (verified
standalone below).

**Real-artifact witness (structural, on a busy box — this box is under
pcrec's solo battery right now, so exact timing numbers are NOT
byte-comparable run to run; the record's SHAPE is).** `bench/email`'s
`floor` pattern, 5 subjects, no give-up anywhere, run twice through
`pcrecbench quick` — once with `pcrecbench/harness.py` reverted to
`HEAD` (the pre-fix code), once with the fix in place, both into fresh
scratch stores:

    before: {'setup': 1, 'compile': 6, 'match': 15} outcomes=['matched-as-expected']
    after:  {'setup': 1, 'compile': 6, 'match': 15} outcomes=['matched-as-expected']

Identical row counts, identical outcome population, one `measured`/one
`measuring` log line each (i.e. `calibrate()` + `measure()` ran exactly
once, not twice) — the pre-fix and post-fix code paths are structurally
identical on a cell with no give-up subject. (The `median ns/call` and
`n_iters` numbers themselves differ slightly between the two runs
—146.032 vs 99.119 ns/call, 1,709,402 vs 1,818,182 iters— which is
ordinary box noise on a shared, busy machine (`status: inconclusive-load`
both times), not a fix-induced change; the isolated deterministic
witness above is what actually proves the no-op, and it is byte-exact.)

**Real give-up witness, end to end.** The same command against
`bench/capability`'s `evil-alt-nested` pattern, 60 subjects (including
`rd-evil-alt-near-miss`, the F3 witness), `pcrec-auto`:

    testee         form           median ns/call ...  pass  give-ups               status
    pcrec-auto     plain                       -   ...59/60  -2:PCREC_ERR_STEPS x3  inconclusive-load
      EXCLUDED: 1 failing subject(s): rd-evil-alt-near-miss (gave-up x3)
    wall   52.2 s

`rd-evil-alt-near-miss` reads `gave-up x3` (by name, dense across all 3
trials) in 52 seconds total for the whole 60-subject cell — not the
"never returned" the pre-fix code would have produced for this one
subject alone (≈200 × 2.7 s ≈ 540 s, per the F3 numbers, against a 60 s
per-subject alarm). The give-up code observed here is `PCREC_ERR_STEPS`
(-2), not the `PCREC_ERR_FRAMES` (-3) the pinned capability@0.1 records
carry — a different resource budget on this quick cell's own capacities,
not a contradiction; either way `classify_giveup`'s range rule reads it
as `gave-up`.

## Deliverables

1. **The fix** — `pcrecbench/harness.py`: `_first_call_outcomes`,
   `measure_regime_cell`, and the `run_cell` call site. No change to
   `pcrecbench/adapters.py` (the driver protocol's C-level loop and the
   Python `measure()` signature are untouched — the fix is entirely in
   how `run_cell` chooses to CALL them).
2. **KB-20** — `docs/dev/known_issues.md`: the bug, the F3 numbers, the
   fix, the no-op argument, and the re-measure consequence. Numbering
   note included inline (KB-18 = lane/b42repdiag's row, KB-19 =
   lane/l6bre2's `DRIVER_BUILDS` row, both pending merge; renumber on
   conflict).
3. **The check** — `tools/selfcheck.py`'s `check_giveup_not_batched`
   (new, registered in `main()` right after `check_subject_timeout`, its
   `timed-out` sibling): isolated, stub-adapter, 6 assertions, verified
   standalone (see below) — never touches pcrec, runs in well under a
   second.
4. **The re-measure consequence** — stated in KB-20: the three
   `capability@0.1` first-sample cells (`evil-alt-nested` ×
   `pcrec-auto-caps`/`pcrec-vm-caps`/`pcrec-vm-in-caps`) carry pinned
   `timed-out` rows (re-verified byte for byte before writing this
   report — all three testees, all 5 trials, `diagnostic: "the
   per-subject alarm fired"`) that would read `gave-up` under the fixed
   harness. Pinned records are append-only; the re-measure rides the
   next capability window (the F1-fix checkpoint pin), alongside the
   I-72 erratum cells.
5. **Validation run**:
   - `check_giveup_not_batched()` standalone: **6/6 PASS** (shown above).
   - `check_convention_scoring()` standalone (an unrelated, pre-existing
     `outcome_for` check, run as a neighbor-regression smoke): **4/4
     PASS**, unaffected.
   - `make check-schema`: **4 example(s) accepted, 72 sabotage(s)
     rejected for the intended rule, 0 sabotage(s) WRONG** — unaffected
     (this lane touches no schema/harness-contract surface).
   - Real end-to-end `pcrecbench quick` smokes (scratch stores under the
     session scratchpad, never `store/`): the no-op structural witness
     (`bench/email` `floor`) and the real give-up witness
     (`bench/capability` `evil-alt-nested`), both above.

   **OWED**: `make check-harness` (the full ~324-check target, ~20 min,
   which would also run `check_giveup_not_batched` inside `main()`) —
   **NOT run in this lane, per the manager's hard rule that pcrec's solo
   battery owns the box this session.** Exact command:

       make check-harness

   from the repo root, once the box is free. `make check` (which
   includes `check-harness`) is likewise owed for the same reason.

## Scope discipline

Touched only `pcrec-bench`, only this worktree
(`worktrees/b43giveup`). `~/pcrec` was not read or written in this
lane. No `make check-harness`/`make check` or other multi-minute
CPU-bound run was launched; every validation above is either isolated
(python-level, sub-second) or a small `quick` smoke (12-52 s each,
`--force-unquiet` implied at the scratch tier so no quiet-gate
contention with the battery). Two sub-benches' gitignored subject trees
(`bench/email/{subjects,throughput}/`, `bench/capability/{subjects,
throughput}/`) were regenerated locally to run the smokes above — they
are gitignored build artifacts, not committed, and regenerating them is
idempotent (`gen_subjects.py`/`gen_throughput_subjects.py`, deterministic).

## Handback

Not merged (the manager merges). Branch `lane/b43giveup` is committed
with three files changed (`pcrecbench/harness.py`,
`tools/selfcheck.py`, `docs/dev/known_issues.md`) plus this report.
