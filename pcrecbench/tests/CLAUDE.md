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
  **[B16] additions (2026-08-28, 7 new tests, 50 total** — corrected here
  from a stale "49" that had drifted from the actual `TESTS` list by one;
  found while counting for [B12] below): one test per
  R1-R7 ruling of the abi-8 re-pin's reporter wave
  (`test_dfa_scan_legend_b16_r1`, `test_fast_tier_legend_b16_r2`,
  `test_engine_reading_and_scoped_legend_b16_r3`,
  `test_giveup_names_engine_and_selection_changed_b16_r4`,
  `test_gcc_band_witness_b16_r5`, `test_max_is_trial_one_b16_r6`,
  `test_dominated_set_ratio_b16_r7`; R8 is the version bump, which
  `test_reporter_version_pin` -- renamed at [B12], was `test_reporter_v4_r10`
  -- pins). Each carries its own CONTROL,
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

  **[B12] R10 addition (2026-08-29, 1 new test, 51 total)**:
  `test_did_not_compile_ranking_line_r10` -- the firing case (two
  hand-built testees sharing one pattern/regime group, one did-not-compile
  with no match rows at all, the other measured cleanly so the ranking
  GROUP exists to hang the bullet under) and a control pattern both
  testees compile cleanly on, asserted absent of any did-not-compile
  bullet. Anchored on `"\n### \`" on BOTH ends of its section-slicing
  split, the same reason `test_floor_pattern_r9`'s own comment already
  gives: a <= 3 subject cell (this one has 1) gets its own H4 per-subject
  sub-table (`#### ... per-subject`), whose bare heading text contains
  the bare H3 title as a one-off substring once its leading `#` is
  dropped -- the unanchored split form silently truncates the section at
  that `#` (caught by hand during development: the first draft of this
  test failed with a section that looked truncated at a lone trailing
  `#`, which is exactly this substring collision, not a `report.py` bug).

  Also at [B12]: the `test_report` RUNTIME FIX. `_load_store(REAL_STORE)`
  pays `schema/validate.py`'s full jsonschema validation cost for every
  record under `store/` -- measured ~39 s per call once bench/loglines
  and email-specimen@0.2 joined email-specimen@0.1 there (26 records,
  2026-08-29; `cProfile` pointed the cost at jsonschema's `iter_errors`/
  `descend`/`referencing` `$ref` resolution, not file I/O). Seven call
  sites in this suite each paid it independently -- where the suite's
  > 2 minute runtime went. `_load_real_store()` (a module-level cache
  around `_load_store(REAL_STORE)`) shares ONE load across all seven,
  safe because nothing in this suite or in `report.build_report`/
  `render_markdown`/`render_tsv` ever mutates a `LoadedRecord` after
  `report.load_all` returns it. Measured before/after on this box, same
  51 tests, all green both times: 274.6 s -> 47.6 s.
  **[B20] additions (2026-08-30, 5 new tests, 56 + 3 → 59 total; schema
  v1.4, `docs/design/gate_shape_v14.md` §6 R8)**:
  `test_status_gate_r1` gains the `inconclusive-spread` case (unranked,
  its bullet printed FROM THE BLOCK -- the control is the free-text
  `status_detail` it must NOT echo -- and ranked under
  `--include-unmeasured`); `test_trial_agreement_legend_and_na_v13` (the
  legend once, `n/a (v1.3)` on the 1.3 half, the block's numbers on the
  1.4 half, both reducing in one `--all-records` query);
  `test_rule_marker_on_mixed_x13_versions` (R4': `measured@1.3` /
  `measured@1.4` in markdown and TSV rows when one query mixes X13
  versions; control: the single-version default query carries no
  suffix); `test_v13_record_still_renders` (the existing 1.1 fixture
  store against `fixtures/golden/store_v8.md`: the ONLY differing lines
  are the version line, the two legend lines and the `agreement: n/a
  (v1.1)` suffixes -- the classifier `_classify_v9_diff` refuses a
  rendering with one number changed, the control);
  `test_provenance_flag` (the after-sample sentences only under
  `--include-provenance`, read from `status_detail` or `note` wherever
  they sit) and `test_after_clause_unconditional` (R5': `after: load1
  11.40 / occ 41.41%` on the record line whenever an after sample
  failed, no flag; control: the clean record carries none; the TSV's
  `record` rows carry the same). `test_all_fixtures_validate` covers the
  new `fixtures/v14_pair/` store and asserts the spread fixture's block
  disagrees on one 2-row group; `test_reporter_version_pin` pins v9.
  **[B22] changes (2026-08-31, no new test, 59 total)**:
  `test_b19_engine_sel_lang_and_emit_bytes` re-pinned to the VALUE-only
  fallback bucket (reporter v10, pin 263b013): the old 96e44c2 size-cap
  shape (`sel=selected` + a `size cap retry` why) is now the RETIREMENT
  CONTROL (unbucketed, the why readable in `lang=`), the new
  `size-cap-retry` and `declined-nullable` tokens are bucketed by value
  (the decline with no `lang=` clause -- the 6.3 iff), and the legend-note
  needle asserts the [B22] wording (and the ABSENCE of the retired
  "bucketed on its why prefix" sentence); `test_reporter_version_pin`
  pins v10; `_classify_v9_diff` skips whatever the CURRENT version line
  is instead of a hard-coded `v9` (the classifier is not re-edited at
  every bump).
  **[B28] additions (2026-09-01, 2 new tests, 61 total; KB-5/KB-6)**:
  `test_testee_filter_kb5` (a single id narrows; two occurrences OR; a
  known id AND'd with an excluding `--until` narrows to nothing with no
  error; an unknown id refuses naming it and a known id for contrast; a
  known+unknown mix still refuses, naming only the unknown one) and
  `test_dfa_scan_edge_legend_kb6` (`edge=` fires right after the `dfa:`
  clause on a DFA artifact; a VM hybrid carries `edge=` with no `match=`
  beside it -- the dfa-scan vs dfa-only scope distinction; CONTROL 1 a
  forced-VM artifact has neither scope nor clause; CONTROL 2 an abi-12
  record carries no pair; the legend note's presence on a table that
  carries the clause and absence on one that does not).
  `test_reporter_version_pin` pins v11.
  **[B28] KB-4 addition (2026-09-01, 1 new test, 62 total)**:
  `test_kb4_refusal_cost_in_phase_medians` -- the adapter half of KB-4
  (schema half DONE at [B20]): a `did-not-compile` row's `cost.total_ns`
  is read as its `emit-c` phase median, recognised by the ABSENCE of a
  `cost.phases` array (X12 forbids a partial one, so a refusal's cost
  never carries one). Three controls: a `compiled` row's phase medians
  are unchanged (still read from `cost.phases`, never `total_ns`); a
  did-not-compile row whose `cost` DOES carry a `phases` array -- a
  shape this adapter never emits, but the schema does not forbid of some
  other future one -- is NOT read for `emit-c`; a did-not-compile row
  with no `cost` at all (the shape every record in `store/` still has)
  renders exactly as before. Plus the end-to-end rendering: the
  compile-cost table's `emit-c ns` column carries the real number while
  `gcc ns`/`load ns` stay `-` (those phases never ran). No `REPORTER_
  VERSION` bump: no record in `store/` at the time carries a `cost` on a
  `did-not-compile` row, so no committed report's rendering moves.
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
