#!/usr/bin/env python3
"""Tests for pcrecbench.__main__'s `quick` command surface -- KB-10
(2026-09-02, docs/dev/known_issues.md).

Only `_split_quick_cells` (the pure cell-lookup helper `cmd_quick` calls)
is under test here: it needs no engine, no bench directory and no store,
so it is exercised directly against hand-built `RunResult`-shaped objects
rather than through the CLI end to end (`tools/selfcheck.py`'s
`check_quick` already covers the real, engine-running path -- see its own
CLAUDE.md; that check is a sibling lane's territory, not this suite's).

Plain runnable module, same technique as `test_report.py` (pytest is not
installed on this box; this file also collects fine under pytest):

    python3 -m pcrecbench.tests.test_quick
"""

from __future__ import annotations

import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
PKG_ROOT = os.path.dirname(os.path.dirname(HERE))  # .../pcrec-bench
if PKG_ROOT not in sys.path:
    sys.path.insert(0, PKG_ROOT)

from pcrecbench import __main__ as main_mod  # noqa: E402
from pcrecbench import reduce as rd  # noqa: E402


class TestFailure(AssertionError):
    pass


def _check(cond, msg):
    if not cond:
        raise TestFailure(msg)


class _FakeResult:
    """Just enough of `harness.RunResult` for `_split_quick_cells`: it
    reads `.rows` and `.path` only (never `.setup` -- that is `cmd_quick`'s
    own printing code, out of scope for this helper)."""

    def __init__(self, rows, path="fake/path.jsonl"):
        self.rows = rows
        self.path = path


def _match_row(pattern_id, regime, subject_id, trial=1, ns=1000.0, iters=100):
    return {
        "kind": "match",
        "pattern_id": pattern_id,
        "regime": regime,
        "subject_id": subject_id,
        "trial": trial,
        "match_outcome": "matched-as-expected",
        "timing": {"elapsed_ns": ns * iters, "iterations": iters},
    }


def _compile_row(pattern_id, outcome="did-not-compile", diagnostic="pattern too large"):
    return {
        "kind": "compile",
        "pattern_id": pattern_id,
        "trial": 1,
        "compile_outcome": outcome,
        "cost_class": "aot",
        "diagnostic": diagnostic,
    }


def _measured_result(pattern_id="p1", regime="search_short"):
    rows = [_match_row(pattern_id, regime, "s1", trial=t) for t in (1, 2, 3)]
    return _FakeResult(rows)


def test_both_arms_measured_unaffected():
    """CONTROL: two arms that both reduce cleanly -- unchanged from before
    KB-10, `refused` is empty and `error` is None."""
    results = [("testee-a", _measured_result()), ("testee-b", _measured_result())]
    reduced, refused, err = main_mod._split_quick_cells(results, "p1", "search_short", rd)
    _check(err is None, f"clean arms must not error: {err!r}")
    _check(len(reduced) == 2, f"both arms must reduce: {reduced!r}")
    _check(refused == [], f"no arm refused: {refused!r}")


def test_vs_arm_refused_kb10():
    """KB-10: the SECOND arm (`--vs`)'s only row for (p1, search_short) is a
    `did-not-compile` compile row (zero match rows) -- `_split_quick_cells`
    must report it as `refused`, not as an error, and the primary arm's
    cell must still reduce."""
    primary = _measured_result()
    vs_res = _FakeResult([_compile_row("p1", diagnostic="pattern too large "
                                        "(NFA exceeds 131072 states)")])
    results = [("pcrec-vm-bigcap", primary), ("pcrec-vm", vs_res)]
    reduced, refused, err = main_mod._split_quick_cells(results, "p1", "search_short", rd)
    _check(err is None, f"a --vs refusal must not error: {err!r}")
    _check(len(reduced) == 1 and reduced[0][0] == "pcrec-vm-bigcap",
           f"the primary arm must still reduce: {reduced!r}")
    _check(len(refused) == 1, f"exactly one refused entry: {refused!r}")
    tid, res, diagnostic = refused[0]
    _check(tid == "pcrec-vm", f"the refused entry names the --vs testee: {tid!r}")
    _check(res is vs_res, "the refused entry carries the ORIGINAL RunResult (KB-10: "
                          "\"the records are already right\")")
    _check(diagnostic == "pattern too large (NFA exceeds 131072 states)",
           f"the refused entry carries the compile row's own diagnostic: {diagnostic!r}")


def test_vs_arm_refused_diagnostic_first_line_only():
    """KB-10's own spelling: \"refused (<diagnostic, first line>)\" -- a
    multi-line diagnostic is truncated to its first line."""
    vs_res = _FakeResult([_compile_row("p1", diagnostic="line one\nline two\nline three")])
    results = [("a", _measured_result()), ("b", vs_res)]
    _reduced, refused, err = main_mod._split_quick_cells(results, "p1", "search_short", rd)
    _check(err is None, f"must not error: {err!r}")
    _check(refused[0][2] == "line one", f"diagnostic must be first-line-only: {refused[0][2]!r}")


def test_primary_arm_refusal_still_errors():
    """CONTROL: a refusal on the PRIMARY (`--testee`, index 0) arm is what
    the caller asked to measure -- KB-10 does not cover it, and
    `_split_quick_cells` must still return the old error."""
    primary_refused = _FakeResult([_compile_row("p1")])
    results = [("pcrec-vm", primary_refused), ("pcre2-jit", _measured_result())]
    reduced, refused, err = main_mod._split_quick_cells(results, "p1", "search_short", rd)
    _check(err is not None, "a primary-arm refusal must still be an error")
    _check("expected one cell" in err, f"the old error message must survive: {err!r}")
    _check(reduced == [] and refused == [],
           "nothing is reported as reduced or refused once an arm errors")


def test_vs_arm_empty_for_other_reason_still_errors():
    """CONTROL: a `--vs` arm with zero rows for (p1, search_short) and NO
    `did-not-compile` compile row for that pattern (e.g. a typo'd pattern
    id, or an adapter bug) is still the OLD error -- KB-10 only covers a
    genuine refusal, not every empty cell."""
    vs_res = _FakeResult([_match_row("other-pattern", "search_short", "s1")])
    results = [("a", _measured_result()), ("b", vs_res)]
    reduced, refused, err = main_mod._split_quick_cells(results, "p1", "search_short", rd)
    _check(err is not None, "an unexplained empty --vs cell must still error")
    _check("expected one cell" in err, f"the old error message must survive: {err!r}")


def test_vs_arm_wrong_form_only_matches_two_cells_still_errors():
    """CONTROL: two forms both present for (p1, search_short) -- `len(mine)
    == 2`, not 0 -- is a different failure shape (an adapter carrying two
    forms for a regime that should only have one) and must still error,
    never silently picked as `refused`."""
    vs_res = _FakeResult([
        _match_row("p1", "search_short", "s1"),
        dict(_match_row("p1", "search_short", "s1"), form="whole-subject"),
    ])
    results = [("a", _measured_result()), ("b", vs_res)]
    reduced, refused, err = main_mod._split_quick_cells(results, "p1", "search_short", rd)
    _check(err is not None, "two cells for one (pattern, regime) must still error")
    _check("found 2" in err, f"the error must name the count: {err!r}")


def test_diagnostic_first_line_helper():
    _check(main_mod._diagnostic_first_line("a\nb\nc") == "a", "splits on the first line")
    _check(main_mod._diagnostic_first_line("one line") == "one line", "single line unchanged")
    _check(main_mod._diagnostic_first_line(None) == "(no diagnostic)",
           "a missing diagnostic gets a stated placeholder, never a blank")
    _check(main_mod._diagnostic_first_line("") == "(no diagnostic)",
           "an empty diagnostic gets the same placeholder")


TESTS = [
    test_both_arms_measured_unaffected,
    test_vs_arm_refused_kb10,
    test_vs_arm_refused_diagnostic_first_line_only,
    test_primary_arm_refusal_still_errors,
    test_vs_arm_empty_for_other_reason_still_errors,
    test_vs_arm_wrong_form_only_matches_two_cells_still_errors,
    test_diagnostic_first_line_helper,
]


def main():
    os.environ.setdefault("LC_ALL", "C")
    passed = failed = 0
    for t in TESTS:
        try:
            t()
        except Exception:  # noqa: BLE001 -- a test harness wants every failure, not just AssertionError
            failed += 1
            print(f"FAIL {t.__name__}")
            traceback.print_exc()
        else:
            passed += 1
            print(f"ok   {t.__name__}")
    print(f"\n{passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
