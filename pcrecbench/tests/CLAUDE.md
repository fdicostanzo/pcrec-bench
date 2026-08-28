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

  **[B14] additions (2026-08-25, 11 new tests, 42 total)**: one test per
  R1-R10 ruling plus a fixture-validated proof for R9
  (`test_plain_entry_capacities_r1`, `test_tiny_set_per_subject_subtable_r2`,
  `test_matching_subject_count_r3`, `test_buffer_frame_legend_r4`,
  `test_jitter_ratio_r5`, `test_worst_now_vs_largest_delta_r6`,
  `test_artifact_bytes_column_r7`, `test_legend_and_superseded_shortening_r8`,
  `test_floor_pattern_r9`, `test_floor_pattern_fixture_r9`,
  `test_reporter_v4_r10`). R1/R2/R4/R7's firing cases go through
  `REAL_STORE` (`os.path.join(report.REPO_ROOT, "store")`, the project's
  own committed email-specimen sample) because they need REAL
  `engine_metadata` stamps at two different pcrec pins that no synthetic
  fixture reproduces. R3 was corrected SAME DAY, before merge (KB-2,
  docs/dev/known_issues.md; manager steer): its first cut (exercised
  against `REAL_STORE` + `bench/email/expectations.tsv`) read the
  sub-bench sidecar live, which a report over a record from elsewhere
  cannot do; the corrected version reads nothing but the record (which
  turns out to carry no usable field either -- `pcrecbench.harness.
  outcome_for` sets `observed = None` on `matched-as-expected` rows), so
  `test_matching_subject_count_r3` now runs entirely against the
  synthetic `fixtures/store/` and asserts the honest `matches: n/s`
  line, plus a direct check that the fixture's own rows really do carry
  `observed: null` (the premise the whole correction rests on). R5/R6/
  R8/R9 (jitter/legend/cross-pin-delta/floor) go through hand-built
  `LoadedRecord`s, the same bypass technique R3's [B9] `tier` tests used
  -- R9 ALSO gets `test_floor_pattern_fixture_r9`, a REAL schema-valid
  fixture file (`fixtures/floor_pattern/`) once lane b15floor's schema
  v1.3 made `patterns[].role` legal, proving the wired path through
  `schema/validate.py` itself, not just the bypass.
  **[B16] additions (2026-08-28, 7 new tests, 49 total)**: one test per
  R1-R7 ruling of the abi-8 re-pin's reporter wave
  (`test_dfa_scan_legend_b16_r1`, `test_fast_tier_legend_b16_r2`,
  `test_engine_reading_and_scoped_legend_b16_r3`,
  `test_giveup_names_engine_and_selection_changed_b16_r4`,
  `test_gcc_band_witness_b16_r5`, `test_max_is_trial_one_b16_r6`,
  `test_dominated_set_ratio_b16_r7`; R8 is the version bump, which
  `test_reporter_v4_r10` already pins). Each carries its own CONTROL,
  because each ruling is the kind that passes trivially without one:
  R1's three ABSENCES must render as three DIFFERENT strings (a single
  blank for all of them is the bug the ruling exists to prevent); R5's
  witness must ABSTAIN between the two gcc bands and must not appear at
  all on a stamped row; R7 must NOT flag an evenly-spread set. R3 and R4
  fire against `REAL_STORE` for the same reason [B14]'s R1/R2/R4/R7 do —
  they need two real pcrec pins whose `engine_metadata` disagrees, which
  is exactly the 8da6120 record where `pcrec-auto` compiled `orig` to a
  DFA artifact and `factored` to a VM one, and which no synthetic
  fixture reproduces. Four [B9]/[B14] tests were re-pointed rather than
  deleted: they had pinned a legend SENTENCE that a later ruling owns
  (`(no stamp — pcrec I-3)`, retired when pcrec cleared I-3), so they
  now assert their OWN ruling's facts and leave the wording to whichever
  ruling last set it.
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
