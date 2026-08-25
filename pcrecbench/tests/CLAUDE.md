# pcrecbench/tests/ -- the reporter's own test suite

Tests ONLY `pcrecbench.report`. No engine is run here, no other lane's
code is imported (`b5report`'s brief: "you never run an engine and never
depend on the other lane's code").

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
