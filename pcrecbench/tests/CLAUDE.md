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
  non-mixed_version fixture validates cleanly against
  `schema/validate.py`, a HAND-COMPUTED `--grain subject` reduction
  (median/min/max/stddev for a specific cell, worked out by hand against
  the fixture's raw trials -- see `test_known_reduction`'s docstring for
  the arithmetic), a HAND-COMPUTED `--grain set` reduction (summing two
  subjects' ns/call per trial --
  `test_set_grain_sums_per_subject_ns_per_call`), that a set cell is
  excluded WHOLESALE when any one subject in it fails rather than
  averaged through
  (`test_set_grain_excludes_whole_set_when_any_subject_fails`), the
  subject-grain expectation-failing-cell exclusion from ranking,
  `unsupported-by-declaration` handling, `--where`/`--regime`/
  `--subbench`/`--version` filter semantics, the default exclusion of
  `synthetic: true` records, the mixed-schema-major-version refusal, that
  a structurally invalid record is dropped with a message rather than
  crashing the report, and that both render formats are deterministic.
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
