# pcrecbench/tests/ -- the reporter's own test suite

Tests ONLY `pcrecbench.report`. No engine is run here (`b5report`'s
brief: "you never run an engine"). UPDATE at [B9] (2026-08-25): that
brief's further "never depend on the other lane's code" no longer holds
-- `report.py` now imports `pcrecbench.reduce` (lane b10loop's shared
set-grain reduction, R5: "the comparable `quick` prints inline must be
the SAME arithmetic the reporter uses") by name, on the manager's
explicit instruction once b10loop landed it. This suite therefore
requires `pcrecbench/reduce.py` to be importable -- it fails with
`ModuleNotFoundError` on a tree where lane b10loop has not merged yet,
which is expected and not a bug in this suite.

## Files

- `test_report.py` -- pytest >= 8 is the project's declared dev
  dependency (`pyproject.toml`), but it is NOT installed on this box
  (checked 2026-08-25). This file is therefore a PLAIN RUNNABLE MODULE
  (functions named `test_*`, a hand-rolled `_check()`/`TestFailure`
  instead of bare `assert` so failures print a clear message either way)
  that also collects fine under pytest if/when it is available:

      python3 -m pcrecbench.tests.test_report        # standalone
      pytest pcrecbench/tests/test_report.py          # if pytest lands

  Covers: store discovery (index-present vs walk-fallback), that every
  non-deliberately-invalid fixture validates cleanly against
  `schema/validate.py` (v1.1), a HAND-COMPUTED `--grain subject`
  reduction (median/min/max/stddev for a specific cell, worked out by
  hand against the fixture's raw trials -- see `test_known_reduction`'s
  docstring for the arithmetic), a HAND-COMPUTED `--grain set` reduction
  (summing two subjects' ns/call per trial --
  `test_set_grain_sums_per_subject_ns_per_call`), that a set cell is
  excluded WHOLESALE when any subject in it fails rather than averaged
  through, with `gave-up` and wrong-answer failures counted and labelled
  SEPARATELY per subject
  (`test_set_grain_excludes_whole_set_when_any_subject_fails`), the
  subject-grain expectation-failing-cell exclusion from ranking WHEN two
  testees share one (pattern, subject, regime) with DIFFERENT forms --
  pcrec `whole-subject`, libpcre2 `plain` -- and one of them fails
  (`test_expectation_failing_cell_is_excluded_from_ranking`); THE FIX
  ITSELF (manager, 2026-08-25, reversing this module's first cut, which
  wrongly split the ranking table by `form`): that all three testees
  answering `p-digits`/match-compliance rank TOGETHER in ONE table at
  BOTH grains, each row carrying its own `form` as a column, never as a
  split (`test_form_never_splits_the_ranking_table`) -- and that `form`
  DOES stay a key for compile-cost cells, where a whole-subject artifact
  is a genuinely separate compile
  (`test_compile_cost_still_keyed_by_form`); `unsupported-by-declaration`
  handling, the corrected seq-based
  lazy-JIT derivation as a direct UNIT TEST against hand-built rows (no
  fixture testee here is `lazy-jit`) --
  `test_lazy_jit_derivation_uses_lowest_seq_not_trial_one` -- deliberately
  constructing a case where the lowest-`seq` row is not `trial == 1` of
  any cell, `--where`/`--regime`/`--subbench`/`--version` filter
  semantics, the default exclusion of `synthetic: true` records, the
  mixed-MAJOR-schema-version refusal
  (`test_mixed_schema_versions_refused`) AND that a MINOR-only version
  spread (schema 1.0 vs 1.1, same major) is NOT refused but instead
  drops the now-invalid old-shaped record via the ordinary
  per-record-invalidity path (`test_minor_version_pair_not_refused`),
  that a structurally invalid record is dropped with a message rather
  than crashing the report, and that both render formats are
  deterministic.
  The module's `_POSITIVE_CONTROL_LOG` docstring-constant records a
  by-hand demonstration (done once, 2026-08-25) that mutating the known
  cell's raw data DOES make `test_known_reduction` fail with the
  specific wrong value, and that the fixture was then restored -- the
  check-design lesson this project inherits from pcrec CLAUDE.md: "a
  check with no failing case proves nothing".

  **[B9] additions (2026-08-25, 11 new tests, 31 total)**: one test per
  R1-R9 ruling plus OD-B13, each exercising both the rule FIRING and the
  case where it does not (`test_status_gate_r1`,
  `test_duplicate_record_dedup_r2`,
  `test_duplicate_record_dedup_prefers_measured_r2` (the manager's R2
  amendment before merge: measured-older beats unmeasured-newer,
  unmeasured-only still shows, and both at once), `test_scratch_tier_gate_r3`,
  `test_form_fact_and_mixed_regime_note_r4`, `test_two_ratio_columns_r5`,
  `test_near_floor_columns_r6`, `test_gave_up_cell_summary_r7`,
  `test_cross_pin_delta_r8`, `test_mechanism_stamp_columns_r9`,
  `test_subbench_dir_alias_od_b13`). R1/R2/R3/R8 (status, duplicate
  dedup, tier, cross-pin) go through `report.build_report`/
  `report.LoadedRecord` directly with HAND-BUILT setup dicts
  (`_mini_setup`/`_mini_row`/`_mk_loaded` helpers above the tests),
  bypassing `schema/validate.py` entirely -- the same technique
  `test_lazy_jit_derivation_uses_lowest_seq_not_trial_one` already uses.
  This is not a shortcut of convenience for R3 in particular: `tier` is
  an optional schema v1.2 field lane b10loop is adding that the shared
  validator does not know about yet, and `setup` is
  `additionalProperties: false` -- a real fixture FILE carrying `tier`
  would be REJECTED before ever reaching the tier-exclusion logic under
  test. R4-R7/R9 are exercised against the EXISTING `fixtures/store/`
  (no new fixture files were needed -- its pcrec `whole-subject` testee,
  gave-up subject and mixed-form `p-digits`/match-compliance cell
  already cover them) plus direct unit tests of the pure helper
  functions (`_form_fact`, `_gave_up_cell_summary`,
  `report.giveup_code` (lane b10loop's shared extractor -- see the note
  above), `_mechanism_stamp_columns`,
  `_jitter_flag`, `_cross_pin_verdict`, `_parse_testee_config`,
  `report.resolve_subbench_arg`).
- `fixtures/` -- the synthetic store this suite reads. See its own
  CLAUDE.md.
- `__init__.py` -- makes this a package so
  `python3 -m pcrecbench.tests.test_report` resolves its `from pcrecbench
  import report` regardless of the caller's cwd.

## `make check-report`

Runs `python3 -m pcrecbench.tests.test_report`, then a smoke invocation
of the CLI itself over `fixtures/store` in both formats. See the root
Makefile.

Maintenance: update this file when files are added/removed or change
role.
