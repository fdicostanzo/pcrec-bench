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

  **KB-25 (2026-09-22, lane b72smalls), THE SECOND RUNTIME FIX: the ONE
  load itself still grew with the WHOLE store.** `_load_real_store()`
  above bounded the repeat-cost to once per suite run, but
  `discover_records(REAL_STORE)` still returned (and `load_all` still
  jsonschema-validated) every path under EVERY sub-bench regardless of
  which one a caller actually needed -- every REAL_STORE call site in
  this file filters `build_report` to `subbench="email-specimen"`
  afterwards. Fixed with KB-16's own mechanism (`report.discover_index`
  + `report.index_row_could_match`, reused rather than reimplemented):
  `_load_real_store(subbench="email-specimen")` now prefilters BEFORE
  `load_all` opens a file, and caches PER SUBBENCH. Measured before/after
  on this box, same store (217 records, 48 email-specimen), same
  84+7+8 = 99 passing tests both times, via `make check-report` (which
  also runs `test_quick`/`test_matrix_page`/the CLI smoke): 26:03.46 ->
  5:25.80 wall (×4.8), 7,667,420 -> 1,411,056 KB max RSS (×5.4).
  `docs/dev/known_issues.md` KB-25 has the full table.

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

**[B32] (b) additions (2026-09-02, 4 new tests, 66 total; reporter v12)**:
one test per ruling of the reporter-half wave (docs/dev/known_issues.md
KB-8/KB-9, ledger docs/dev/ledgers/2026-09-02-full-suite-1989c62.md
§12 (d), and the `scan_edges` column) --
`test_source_desc_query_filtered_kb8` (the header's record count tracks
`--testee`-filtered selection, not `len(loaded)`; a record OUTSIDE the
filter does not move it -- the CONTROL that makes the fix's own point:
store growth elsewhere must not move a bounded query's count),
`test_cc_clang_phase_note_kb9` (`_cc_from_testee_id` unit-tested
directly, then the end-to-end `(clang cc)` suffix on a clang row's `gcc
ns` cell beside its gcc sibling's UNSUFFIXED cell in the SAME table,
plus the legend note; controls: an explicit `cc-gcc` token, a
non-pcrec/unparseable testee_id, and a gcc-only table with neither),
`test_worst_other_core_header_ledger12d` (a hand-built timeline with two
items picks the WORST reading by value, not the first or last; control:
no timeline anywhere renders `n/a` by name), `test_scan_edges_legend_column`
(`_scan_edges_display` unit-tested for the `0`-is-real-and-not-absent
rule and the both-keys-together case, then the `edges=` clause rendering
beside -- and independently of -- `edge=`'s dfa-scan scope: a forced-VM
artifact carries `edges=0` with no `edge=` clause at all; control: an
older-pin record with neither key renders neither the clause nor the
note). `_V9_ALLOWED_ADDED` (`test_v13_record_still_renders`'s classifier)
gained the new unconditional `worst other-core busy:` header line
(same footing as the two v1.4 legend lines it already allows);
`test_reporter_version_pin` pins v12; the `fixtures/golden/store_v8.md`
`record source` line's wording was updated in place to match KB-8's new
phrasing (its record COUNT is unchanged -- the fixture's own query
selects all 3 records either way).
**[B52] additions (2026-09-18, lane b52matrix; reporter v18)**: 6 new
tests in `test_report.py` -- `test_matrix_all_refused_pattern_f26`,
`test_matrix_status_tokens`, `test_matrix_no_empty_cells`,
`test_matrix_ratio_arithmetic` (the F26-immunity row, the five closed
status tokens each in one hand-built fixture cell, the mechanical
no-blank-cells sweep over a mixed fixture, and a hand-computed ratio
arithmetic proof -- these four were WRITTEN by a predecessor lane's WIP
but never added to the `TESTS` list the plain runner (`main()`) walks,
so they had never actually been RUN before this lane found and fixed
the gap), plus `test_baseline_identity_interp_present` and
`test_baseline_identity_row_best_fallback` (the O-33 addendum's
baseline-identity fact, BOTH ARMS: the interp reference present in a
group states its own testee id by name; interp absent states the
FASTEST non-interp testee, never a slower one and never the query's
static predicted-baseline string). `_V9_ALLOWED_ADDED` gains the
`"- baseline: "` prefix (the new bullet is unconditional on every
rankable group, same footing as the KB-8/ledger-12(d) additions before
it) so `test_v13_record_still_renders` keeps passing. A NEW file,
`test_matrix_page.py` (8 tests): `scripts/matrix_page.py`'s `.matrix.tsv`
parser (provenance-lines-verbatim, header-shape refusal, empty-file
refusal) and HTML renderer (each status token's own fixed chip class
vs. the ratio ramp's inline `background:rgb(...)`, the log-scale ramp's
endpoints and its clamp past the ceiling, a full mixed-population page,
and `main()`'s default-output-path rule) -- loaded by file path
(`importlib.util`) since `scripts/` carries no `__init__.py`
deliberately. 84 tests in `test_report.py` (every one of them now
actually wired into `TESTS`), 7 in `test_quick.py`, 8 in
`test_matrix_page.py`: **99 reporter-side tests total across the three
files.**

- `test_quick.py` (new file, 7 tests, KB-10, `pcrecbench/__main__.py`'s
  `quick` command): `_split_quick_cells` (the cell-lookup helper pulled
  out of `cmd_quick` so it needs no engine, bench directory or store) is
  exercised against hand-built `RunResult`-shaped objects --
  `test_both_arms_measured_unaffected` (control: unchanged behaviour),
  `test_vs_arm_refused_kb10` (the firing case: a `--vs` arm's
  `did-not-compile` compile row becomes a `refused` entry, the primary
  arm still reduces), `test_vs_arm_refused_diagnostic_first_line_only`
  (a multi-line diagnostic truncates), `test_primary_arm_refusal_still_
  errors` (KB-10 does not cover the PRIMARY `--testee` arm),
  `test_vs_arm_empty_for_other_reason_still_errors` (an empty cell with
  no `did-not-compile` row for that pattern is still the old error --
  KB-10 covers refusals only, not every empty cell),
  `test_vs_arm_wrong_form_only_matches_two_cells_still_errors` (two
  cells, not zero, is a different failure shape and must still error),
  `test_diagnostic_first_line_helper`. The real, engine-running `quick`
  path is `tools/selfcheck.py`'s `check_quick` (a sibling lane's
  territory) -- this file covers only the pure helper `_split_quick_
  cells`/`_diagnostic_first_line` KB-10 added. 73 reporter-side tests
  total across both files.

**[B42] CB2 addition (2026-09-16, 1 new test, 74 reporter-side tests
total; lane b42cap)**: `test_variant_kind_rendering_cb2` -- `variant.kind`
rendering, designed and built from nothing (R5 B2/CB2: before this
change, `variant` appeared nowhere in `report.py` but as unrelated
prose). A SYNTHETIC many-variant fixture (thirteen patterns, two
testees: `engine-a` always runs the canonical text, `engine-b` runs a
declared variant -- alternating `syntax-only`/`restructured` -- on
twelve of them and the canonical text on the thirteenth, the control),
never a live sample: no committed record anywhere carries a non-null
`patterns[].variant` (`gen_variants.py`'s table is deliberately empty in
v1 for every set). Asserts the `variant` column and kind token appear in
every one of the twelve mixed tables (`engine-b`'s row shows the kind,
`engine-a`'s shows `-`, the explanatory legend note is present), and
that the thirteenth (control) pattern's table carries NEITHER the column
nor the note even though the SAME report shows both everywhere else --
the per-table conditional rule (`dominated_by_testee`/`delta_by_testee`'s
own shape), not `show_form`'s report-wide flag. `REPORTER_VERSION` is
UNCHANGED (no committed report renders differently); see `report.py`'s
own `[B42] CB2` module-docstring section.

**KB-27 additions (2026-09-22, lane b75kb27; reporter v19)**: 2 new
tests in `test_report.py` (86 total) --
`test_no_expectation_cell_is_not_wrong` (a `did-not-match-as-
expected` row carrying `harness.outcome_for()`'s own fixed "no
expectation exists for this (pattern, subject, regime)" diagnostic
reduces to `n_no_expectation`, never `n_wrong`, and `_failure_label`
calls it `no-expectation`; the CONTROL right beside it is the SAME
`match_outcome` with a REAL disagreement diagnostic, which must still
reduce to `n_wrong` and label `wrong`, exactly as before this fix) and
`test_no_expectation_diagnostic_matches_harness` (an anti-drift
cross-check: calls `harness.outcome_for()` directly with
`expectation=None` and asserts the REAL diagnostic it returns starts
with `reduce.py`'s own duplicated literal, `NO_EXPECTATION_DIAGNOSTIC_
PREFIX` -- the two are two copies by necessity, `reduce.py`'s own
docstring explains why, so this is what keeps them from silently
drifting apart). `test_matrix_status_tokens` gains a SIXTH testee,
`engine-no-expectation`, exercising the new status token in the same
one-testee-per-token fixture the other five already use. The token is
`no-expectation`, deliberately NOT `unjudged` -- that word already names
an unrelated count on the SAME report's `trial_agreement` line
(`reduce.judge_trial_agreement`/`agreement_line`), and reusing it here
would have put two unrelated meanings of "unjudged" in one document.
`test_matrix_no_empty_cells`'s `_FLOAT_OR_TOKEN` constant and
`test_reporter_version_pin`'s history/assertions move to v19.
`test_status_chip_cell_html` (`test_matrix_page.py`) needed only its
`row` dict widened by one entry -- it iterates `mp.STATUS_CHIPS.items()`
generically, so the new `no-expectation` chip's CSS class and title are
already covered by the existing loop once `scripts/matrix_page.py`'s
`STATUS_CHIPS` dict gains the entry. No `test_quick.py` change.

**[B82] additions (2026-09-23, lane b82views; reporter v20)**: 3 new
tests in `test_report.py` (89 total) — `test_capture_class_declaration_
table` (a pure unit test of the new `pcrecbench/capture_class.py`
module: every real roster row, rust-default's I-100 override with its
`is_override`/`how_told` check, an unknown engine and an unparseable id
both UNDECLARED), `test_b82_capture_class_views_and_query` (a
MIXED-ROSTER fixture spanning YES/NO/UNDECLARED asserting both
class-pure views' memberships, the undeclared testee excluded from both
and listed on its own, rust-default's declaration rendering visibly in
the view it ranks in, the mixed table unchanged in membership, the
standing cross-class query firing on a constructed yes-beats-nocaps
pattern and NOT on its control, and markdown/TSV hit counts agreeing
exactly) and `test_b82_single_class_roster_unchanged` (the CONTROL: no
new heading text on a roster that does not span both classes, the query
section still rendering with an honest `0 hits`). `test_matrix_page.py`
gains 4 (12 total): `test_parse_capture_class`, `test_class_pure_row_
rebases_within_class` (the re-derivation arithmetic directly — a lone
NO-class member re-bases 2.000x -> 1.000x), `test_matrix_class_pure_
split_renders_two_tables`, `test_matrix_single_class_roster_unchanged`.
See `docs/dev/lanes/b82views_report.md` for the full charter-vs-
committed checklist and what is OWED to the manager's merge.

**[B85] additions (2026-09-23, lane b85kb28; KB-28, reporter v21)**: 4
new tests in `test_report.py` (89 → 93) —
`test_kb28_subject_grain_single_table_with_class_column` (the [B82]
mixed-roster fixture at `--grain subject`: no `CAPTURING`/`NON-
CAPTURING`/`MIXED CLASSES` heading, exactly ONE ranking section, a
`capture class` column read out of the rendered table with the correct
bucket per testee, the TSV mirroring it with a 19th `capture_class`
header column and no `rank_yes`/`rank_no` sections, plus a generic
ragged-row check every TSV line matches the header's field count),
`test_kb28_set_grain_unaffected` (the CONTROL: the IDENTICAL fixture at
the default `set` grain still renders [B82]'s three headings and the
unchanged 18-column TSV header), `test_kb28_single_class_subject_grain_
unchanged` (a single-class roster at subject grain renders no `capture
class` text and the unchanged 18-column header — the byte-identity proof
for the case no real committed single-class subject-grain report exists
to diff against), and `test_kb28_large_report_warns_but_never_fails`
(`_warn_if_large` unit-tested directly with an explicit small
`threshold`, plus an end-to-end `report.main()` call with
`_LARGE_REPORT_WARN_BYTES` monkeypatched to 0 — this integration test is
what caught a real bug: the function's first cut read `threshold` as a
literal default-argument value, evaluated once at def time, so `main()`'s
own unparameterised calls would never have honoured a monkeypatch;
fixed by resolving the module constant INSIDE the function body). See
`docs/dev/lanes/b85kb28_report.md` for the full checklist, the SET-grain
byte-identity proof against a real committed v20 report, and the
`pcrecbench/interpret.py` `ReportTsv` parsing fix this lane's own check
of the `[B47]`-era subject-grain slice found necessary (a mixed-roster
subject-grain report's new 19-column header would otherwise have been
refused outright by `pcrecbench interpret`).

**[B79] additions (2026-09-25, lane b79nullband; the null-control band,
reporter v22)**: 3 new tests in `test_report.py` (93 → 96) —
`test_b79_null_band_hand_computed` (two pins of one config, a
hand-written census, every number worked in the fixture's own comments:
ten program-identical cells at >=1us giving a ±6.00% band, three at
100ns-1us (INSUFFICIENT, n=3 < 10), none at <100ns (EMPTY), and the five
verdict shapes -- regress past the band, within a WIDER IQR (Type-7 IQR
150 of 900/950/1000/1100/1200 = 15%), improve past the band, and the two
IQR-only verdicts naming their stratum's n -- plus the per-view counts,
the conditional `null_band:` header key, the `null_band`/`d119`/
`d119_view` TSV rows and a ragged-row check),
`test_b79_no_census_is_stated_never_silent` (CONTROL: a cross-pin pair
with no census renders `NO NULL BAND` naming the path, no D119 column,
no d119 rows) and `test_b79_single_pin_report_renders_no_band` (CONTROL:
no cross-pin pair, nothing new rendered). `test_b82_capture_class_views_
and_query`'s I-101 assertion now checks the COMPUTED clearance (`clears
IQR only` / `IQR 0.00% (clears)` / `no null band (no cross-pin pair in
this report)`) in place of the retired "[B79] not-started" text.

**[B87] addition (2026-09-25, lane b87query; the standing query pairs
pcrec same-pin only, reporter v23)**: 1 new test in `test_report.py`
(96 → 97) — `test_b87_query_pairs_pcrec_same_pin_only`: a synthetic
two-pin fixture (`pinA`/`pinB`, each with its own `auto-caps`/
`auto-nocaps` pair) plus one non-pcrec competitor, medians chosen so the
OLD pairing would have produced 6 hits (2 same-pin pcrec + 2 cross-pin
pcrec + 2 competitor-vs-each-pin) and the fix leaves 4 (the two
cross-pin pcrec pairs dropped, everything else unchanged) — asserted
directly against `report._cross_class_query_hits`'s own return value
(every hit pair checked by testee id, not just the count) AND against
both rendered surfaces (markdown table rows, the TSV `hit_count` row),
plus a per-row check that neither `pinA_caps` nor `pinB_caps` ever
appears paired with the OTHER pin's `auto-nocaps` anywhere in the
rendered query section. `test_reporter_version_pin`'s docstring and
pinned assertions move to v23.

**[B88] addition (2026-09-25, lane b90repin; BD13, reporter v23
unchanged)**: 1 new test in `test_report.py` (97 -> 98) --
`test_b88_null_band_reads_program_sha256_first`: [B79]'s hand-computed
fixture with one plain compile row per pattern carrying
`engine_metadata.program_sha256` (equal on both sides for an
`identical` cell, different for a `changed` one). (1) NO census: the
band is built from the field alone and its strata equal [B79]'s census
band exactly (10 null at >=1us, +-6.00%; 3 insufficient; 0 empty), with
the `identity from the records` line and the TSV `identity_field` row;
(2) a census that DISAGREES on `n0`: the field decides (still null) and
the disagreement is named; (3) CONTROL: the field on ONE side only ->
the census fallback, the band section and every `d119`/`null_band` row
byte-identical to [B79]'s pure-census render. Plus the pure
`nullband.field_identity` / `cell_identity` arms.

## `make check-report`

Runs `python3 -m pcrecbench.tests.test_report`, then
`python3 -m pcrecbench.tests.test_quick` ([B32] (b), KB-10), then
`python3 -m pcrecbench.tests.test_matrix_page` ([B52]), then a smoke
invocation of the CLI itself over `fixtures/store` in both formats plus
`--format matrix` (rendered through `scripts/matrix_page.py`, and
refused BY NAME at `--grain subject`). See the root Makefile.

Maintenance: update this file when files are added/removed or change
role.
