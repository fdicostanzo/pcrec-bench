#!/usr/bin/env python3
"""Tests for pcrecbench.report ([B5] landing bar).

pytest >= 8 is the declared dev dependency (pyproject.toml
`[project.optional-dependencies].dev`), but it is NOT installed on this
box (checked 2026-08-25: `import pytest` -> ModuleNotFoundError). Per the
lane brief, this is therefore written as a plain runnable module:

    python3 -m pcrecbench.tests.test_report

It also collects fine under pytest (plain `test_*` functions, `assert`)
if/when pytest is available -- no pytest-only API is used.

Fixtures: pcrecbench/tests/fixtures/ (see its CLAUDE.md). Every fixture
record is `synthetic: true`; tests that go through the CLI/store-discovery
path pass `--include-synthetic` explicitly (report.py excludes synthetic
records by default, mirroring schema/examples/CLAUDE.md's stated reporter
behaviour) -- see report.py's module docstring for why the flag exists.

POSITIVE CONTROL (brief: "a fixture edited to the wrong median makes the
test fail -- show it once, then restore"): this was done BY HAND during
development, not committed as a permanently-failing test (that would
leave `make check-report` red, which defeats its purpose as a gate).
Procedure and observed result are recorded in `_POSITIVE_CONTROL_LOG`
below and were reported to the manager verbatim.
"""

from __future__ import annotations

import os
import statistics
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
FIXDIR = os.path.join(HERE, "fixtures")
PKG_ROOT = os.path.dirname(os.path.dirname(HERE))  # .../worktrees/b5report

if PKG_ROOT not in sys.path:
    sys.path.insert(0, PKG_ROOT)

from pcrecbench import report  # noqa: E402


STORE = os.path.join(FIXDIR, "store")
STORE_WALK_ONLY = os.path.join(FIXDIR, "store_walk_only")
MIXED_VERSION = os.path.join(FIXDIR, "mixed_version")

TESTEE_A = "pcrec_1.0.0-gdeadbee_vm-caps-simdna"
TESTEE_B = "libpcre2_10.46_interp-caps-simdna"
TESTEE_C = "libpcre2_10.46_jit-caps-simdna"

_POSITIVE_CONTROL_LOG = """
Performed by hand on 2026-08-25 against
pcrecbench/tests/fixtures/store/records/fixture-mini@1.0/
  pcrec_1.0.0-gdeadbee_vm-caps-simdna/fixture-mini@1.0__pcrec_1.0.0-gdeadbee_vm-caps-simdna__repfix-box__20260825T100000Z.jsonl

Round 1 (hash-tamper control, unplanned but instructive): edited
`timing.elapsed_ns` 100000 -> 999000 on the p-digits/s-num-1/
match-compliance/trial=1 row WITHOUT restamping `content_hash`.
`test_all_fixtures_validate` failed first (rule X6, tampered hash), which
cascaded into `test_known_reduction` and two others failing on "cell not
found" / "testee A ... got []" because the corrupted record was dropped
before it ever reached the reducer. Correct behaviour, but it tests X6,
not the reducer -- so it does not by itself establish that the median
computation is checked.

Round 2 (the actual positive control): restamped `content_hash` to match
the edited bytes (`python3 schema/validate.py --print-hash <file>`, value
patched in), so the file validates cleanly again but the underlying
number is genuinely wrong (999000 instead of 100000 for trial 1).
Re-ran `python3 -m pcrecbench.tests.test_report`:

    FAIL test_known_reduction
    TestFailure: known-reduction check failed: expected median_ns == 100.0,
    got 110.0 (fixtures/store/.../pcrec_..._20260825T100000Z.jsonl...,
    cell p-digits/s-num-1/match-compliance)
    13 passed, 1 failed

(110.0, not 999.0: with trial 1 pushed to the new max, the middle value
of the sorted [90, 110, 999] triple is 110 -- the median moved, which is
itself a small confirmation the reducer's median logic is doing real
work, not just echoing trial 1.) All 13 OTHER tests still passed,
confirming this specific check -- and only this check -- is sensitive to
the reduction being wrong.

Restored the original bytes from a pre-edit backup copy (the fixture is
untracked/new in this branch, so `git checkout` had nothing to restore
from) and re-ran: all 14 tests PASSED.

This demonstrates `test_known_reduction` is not vacuous -- it fails when
the underlying data changes and the schema hash cannot be used to paper
over that -- which is the whole point of a hand-computed positive control
(pcrec's check-design lesson, inherited into this project's CLAUDE.md:
"a check with no failing case proves nothing").
"""


class TestFailure(AssertionError):
    pass


def _check(cond, msg):
    if not cond:
        raise TestFailure(msg)


# ------------------------------------------------------------- loading helpers

def _load_store(store_dir, **kw):
    paths, source = report.discover_records(store_dir)
    loaded = report.load_all(paths, check_filename=True)
    return loaded, paths, source


def _args(**overrides):
    ap = report.build_argparser()
    args = ap.parse_args([])
    args.where = []
    args._source_desc = "test"
    for k, v in overrides.items():
        setattr(args, k, v)
    return args


# ----------------------------------------------------------------------- tests

def test_store_discovery_uses_index_when_present():
    paths, source = report.discover_records(STORE)
    _check(source == "store/index.tsv", f"expected index-based discovery, got {source!r}")
    _check(len(paths) == 3, f"expected 3 records from index.tsv, got {len(paths)}: {paths}")
    for p in paths:
        _check(os.path.isfile(p), f"index.tsv named a path that does not exist: {p}")


def test_store_discovery_walks_when_index_absent():
    paths, source = report.discover_records(STORE_WALK_ONLY)
    _check(source.startswith("walked"), f"expected walk fallback, got {source!r}")
    _check(len(paths) == 1, f"expected 1 record under store_walk_only, got {len(paths)}")


def test_all_fixtures_validate():
    """Every fixture record in the main store (+ store_walk_only, + the
    mixed_version v1-ok half) must independently pass schema/validate.py --
    the brief's 'all fixtures ... validating with schema/validate.py'
    (mixed_version's deliberately-future-version half is excepted; see its
    CLAUDE.md -- that file's WHOLE POINT is that it does not validate)."""
    for store_dir in (STORE, STORE_WALK_ONLY):
        loaded, paths, _source = _load_store(store_dir)
        for rec in loaded:
            _check(not rec.problems,
                   f"{rec.path} unexpectedly failed validation: {rec.problems}")

    mv_paths, _source = report.discover_records(MIXED_VERSION)
    mv_loaded = report.load_all(mv_paths, check_filename=True)
    ok = [r for r in mv_loaded if not r.problems]
    bad = [r for r in mv_loaded if r.problems]
    _check(len(ok) == 1, f"expected exactly 1 valid record in mixed_version, got {len(ok)}")
    _check(len(bad) == 1, f"expected exactly 1 invalid record in mixed_version, got {len(bad)}")
    _check(any(p.rule == "X17" for p in bad[0].problems),
           f"the invalid mixed_version record should fail on X17, got: {bad[0].problems}")


def test_known_reduction():
    """HAND-COMPUTED answer for pcrec / p-digits / s-num-1 / match-compliance:
    trials (elapsed_ns, iterations) = (100000,1000), (110000,1000), (90000,1000)
    => ns/call = [100, 110, 90]
    => median 100, min 90, max 110, n=3
    => population stdev = sqrt(((0)^2+(10)^2+(-10)^2)/3) = sqrt(200/3) = 8.16496580927726
    """
    loaded, paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")

    key = None
    for k, (testee_id, _red) in rd.match_cells.items():
        sb, tid, pattern_id, subject_id, regime = k
        if (tid == TESTEE_A and pattern_id == "p-digits"
                and subject_id == "s-num-1" and regime == "match-compliance"):
            key = k
            break
    _check(key is not None, "known-reduction cell not found in rd.match_cells")
    _testee_id, red = rd.match_cells[key]

    expected_median = 100.0
    expected_min = 90.0
    expected_max = 110.0
    expected_stddev = statistics.pstdev([100.0, 110.0, 90.0])

    _check(red.n_trials == 3, f"expected n_trials == 3, got {red.n_trials}")
    _check(red.n_timed == 3, f"expected n_timed == 3, got {red.n_timed}")
    _check(red.median_ns == expected_median,
           f"known-reduction check failed: expected median_ns == {expected_median}, "
           f"got {red.median_ns} ({os.path.relpath(paths[0], PKG_ROOT)}..., "
           f"cell p-digits/s-num-1/match-compliance)")
    _check(red.min_ns == expected_min, f"expected min_ns == {expected_min}, got {red.min_ns}")
    _check(red.max_ns == expected_max, f"expected max_ns == {expected_max}, got {red.max_ns}")
    _check(abs(red.stddev_ns - expected_stddev) < 1e-9,
           f"expected stddev_ns == {expected_stddev}, got {red.stddev_ns}")
    _check(red.pass_rate == 1.0, f"expected pass_rate == 1.0, got {red.pass_rate}")
    _check(red.iters == [1000], f"expected iters == [1000], got {red.iters}")


def test_expectation_failing_cell_is_excluded_from_ranking():
    """--grain subject: the original per-(pattern,subject,regime) exclusion."""
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True, grain="subject")
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    _check(rd.grain == "subject", f"expected rd.grain == 'subject', got {rd.grain!r}")

    groups = report._ranking_groups(rd, grain="subject")
    failing_key = None
    for k, entries in groups.items():
        sb, pattern_id, subject_id, regime = k
        if pattern_id == "p-word" and subject_id == "s-word-1" and regime == "match-compliance":
            failing_key = k
            break
    _check(failing_key is not None, "expected p-word/s-word-1/match-compliance group to exist")
    entries = groups[failing_key]
    testee_b_entry = next((r for t, r in entries if t == TESTEE_B), None)
    _check(testee_b_entry is not None, "expected testee B's failing cell to be present")
    _check(testee_b_entry.expectation_failing,
           "testee B's did-not-match-as-expected cell must be flagged expectation_failing")
    _check(testee_b_entry.pass_rate == 0.0, f"expected pass_rate 0.0, got {testee_b_entry.pass_rate}")

    rankable = [t for t, r in entries if not r.expectation_failing and r.n_timed]
    _check(TESTEE_B not in rankable,
           f"testee B must be excluded from the rankable set, got {rankable}")
    _check(TESTEE_A in rankable, f"testee A (passing) must remain rankable, got {rankable}")

    md = report.render_markdown(rd)
    _check("Excluded from ranking" in md, "markdown report must have an excluded-cells section")
    _check(TESTEE_B in md.split("Excluded from ranking")[1].split("## Compile cost")[0],
           "testee B's failing cell must be listed under Excluded from ranking")


def test_set_grain_sums_per_subject_ns_per_call():
    """--grain set (default), manager change request 2026-08-25: p-digits/
    match-compliance has TWO subjects (s-num-1, s-num-2) for every testee.
    HAND-COMPUTED for testee A: s-num-1 ns/call=[100,110,90] (trials 1,2,3),
    s-num-2 ns/call=[50,90,160] -> per-trial SUMS=[150,200,250]
    -> median 200, min 150, max 250, n_subjects=2, pass_rate=1.0."""
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)  # grain defaults to 'set'
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    _check(rd.grain == "set", f"expected the default grain to be 'set', got {rd.grain!r}")

    key = next((k for k in rd.set_cells
                if k[1] == TESTEE_A and k[2] == "p-digits" and k[3] == "match-compliance"), None)
    _check(key is not None, "expected a set cell for (testee A, p-digits, match-compliance)")
    _testee_id, red = rd.set_cells[key]

    sums = [150.0, 200.0, 250.0]
    expected_median = statistics.median(sums)
    expected_min = min(sums)
    expected_max = max(sums)
    expected_stddev = statistics.pstdev(sums)

    _check(red.n_subjects == 2, f"expected n_subjects == 2, got {red.n_subjects}")
    _check(red.n_agreeing == 2, f"expected n_agreeing == 2, got {red.n_agreeing}")
    _check(red.pass_rate == 1.0, f"expected pass_rate == 1.0, got {red.pass_rate}")
    _check(red.failing_subjects == [], f"expected no failing subjects, got {red.failing_subjects}")
    _check(red.n_trials == 3, f"expected n_trials == 3, got {red.n_trials}")
    _check(red.median_ns == expected_median,
           f"set-grain known-sum check failed: expected median_ns == {expected_median}, "
           f"got {red.median_ns} (cell p-digits/match-compliance, testee A, "
           f"summing s-num-1 + s-num-2 per trial)")
    _check(red.min_ns == expected_min, f"expected min_ns == {expected_min}, got {red.min_ns}")
    _check(red.max_ns == expected_max, f"expected max_ns == {expected_max}, got {red.max_ns}")
    _check(abs(red.stddev_ns - expected_stddev) < 1e-9,
           f"expected stddev_ns == {expected_stddev}, got {red.stddev_ns}")

    # p-digits/short-subject-search has exactly one subject (s-num-1) for
    # every testee -- set and subject grain must agree there.
    single_key = next((k for k in rd.set_cells
                        if k[1] == TESTEE_A and k[2] == "p-digits"
                        and k[3] == "short-subject-search"), None)
    _check(single_key is not None, "expected the single-subject set cell to exist")
    _tid, single_red = rd.set_cells[single_key]
    subj_key = (single_key[0], TESTEE_A, "p-digits", "s-num-1", "short-subject-search")
    _check(subj_key in rd.match_cells, "expected the matching subject cell to exist")
    _tid2, subj_red = rd.match_cells[subj_key]
    _check(single_red.n_subjects == 1, f"expected n_subjects == 1, got {single_red.n_subjects}")
    _check(single_red.median_ns == subj_red.median_ns,
           "a single-subject set cell must equal its subject-grain counterpart: "
           f"set={single_red.median_ns} subject={subj_red.median_ns}")
    _check("short-subject-search" in rd.single_subject_regimes,
           f"expected short-subject-search in single_subject_regimes, got "
           f"{rd.single_subject_regimes}")


def test_set_grain_excludes_whole_set_when_any_subject_fails():
    """Testee B's p-word set has TWO subjects: s-word-1 (fails, all 3
    trials did-not-match-as-expected) and s-mix-set (passes). Per the
    manager's rule, the WHOLE set cell must be excluded, not averaged
    through, and s-word-1 must be named as the failing subject."""
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)  # grain='set'
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")

    # p-word's two subjects (s-word-1, s-mix-set) sit under DIFFERENT
    # regimes in this fixture (match-compliance vs short-subject-search
    # respectively -- see fixtures/CLAUDE.md), so the set that actually
    # fails is (p-word, match-compliance), whose only subject IS
    # s-word-1: a single-subject set that fails is still a set-grain
    # exclusion (n_subjects=1, pass_rate=0.0), and it exercises the same
    # "any subject fails -> whole set excluded" rule as a larger set would.
    key = next((k for k in rd.set_cells
                if k[1] == TESTEE_B and k[2] == "p-word" and k[3] == "match-compliance"), None)
    _check(key is not None, "expected a (testee B, p-word, match-compliance) set cell")
    _tid, red = rd.set_cells[key]
    _check(red.expectation_failing, "the set cell must be flagged expectation_failing")
    _check(red.failing_subjects == ["s-word-1"],
           f"expected failing_subjects == ['s-word-1'], got {red.failing_subjects}")
    _check(red.pass_rate == 0.0, f"expected pass_rate 0.0 (1 subject, 0 agreeing), got {red.pass_rate}")
    _check(red.n_trials == 0, f"an excluded set cell must carry no reduced trials, got {red.n_trials}")

    md = report.render_markdown(rd)
    _check("SET grain" in md, "the set-grain report must label itself as such")
    _check("s-word-1" in md.split("Excluded from ranking")[1].split("## Compile cost")[0],
           "the failing subject must be named in the set-grain excluded table")


def test_unsupported_by_declaration_outcome():
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")

    found = False
    for (sb, testee_id, pattern_id), (tid, red) in rd.compile_cells.items():
        if testee_id == TESTEE_C and pattern_id == "p-word":
            found = True
            _check(red.outcome_counts.get("unsupported-by-declaration") == 1,
                   f"expected unsupported-by-declaration=1, got {red.outcome_counts}")
            _check(red.n_costed == 0, f"an unsupported pattern must cost nothing, got n_costed={red.n_costed}")
    _check(found, "expected a compile cell for (testee C, p-word)")


def test_where_filter_dotted_path():
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True,
                 where=[("testee.openness", "open-source"), ("testee.engine_name", "pcrec")])
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    testees_present = {tid for (_sb, tid, *_r), (_t, _red) in rd.match_cells.items()}
    _check(testees_present == {TESTEE_A},
           f"--where testee.engine_name=pcrec should isolate testee A only, got {testees_present}")

    args_none = _args(store=STORE, include_synthetic=True,
                      where=[("testee.engine_name", "nonexistent-engine")])
    rd_none, err_none = report.build_report(loaded, args_none)
    _check(err_none is None, f"unexpected refusal: {err_none}")
    _check(not rd_none.match_cells and not rd_none.compile_cells,
           "a --where filter matching nothing should produce an empty report, not an error")


def test_regime_filter_restricts_match_rows_only():
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True, regime="short-subject-search")
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    regimes_seen = {regime for (_sb, _t, _p, _s, regime), _v in rd.match_cells.items()}
    _check(regimes_seen == {"short-subject-search"},
           f"expected only short-subject-search cells, got {regimes_seen}")
    # compile rows are not regime-scoped and must still be present
    _check(len(rd.compile_cells) > 0, "compile cells must survive a --regime filter")


def test_subbench_and_version_filters():
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True, subbench="fixture-mini", version="1.0")
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    _check(rd.subbench_versions == {"fixture-mini@1.0"}, rd.subbench_versions)

    args_wrong = _args(store=STORE, include_synthetic=True, subbench="nope")
    rd_wrong, err_wrong = report.build_report(loaded, args_wrong)
    _check(err_wrong is None, f"unexpected refusal: {err_wrong}")
    _check(not rd_wrong.included, "an unmatched --subbench should select nothing")


def test_synthetic_excluded_by_default():
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=False)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    _check(not rd.included,
           "every fixture record is synthetic:true; without --include-synthetic "
           "the reporter must exclude all of them (schema/examples/CLAUDE.md's "
           "stated behaviour)")


def test_mixed_schema_versions_refused():
    loaded, _paths, _source = _load_store(MIXED_VERSION)
    args = _args(store=MIXED_VERSION, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(rd is None, "a report spanning two major schema versions must be refused (rd is None)")
    _check(err is not None and "mix MAJOR schema versions" in err, f"unexpected error text: {err!r}")
    _check("1.x" in err and "2.x" in err, f"the refusal message must name both majors: {err!r}")


def test_invalid_record_is_dropped_with_a_message(capsys=None):
    """A structurally-broken record (bad JSON on line 2) must be excluded
    from the report, not crash it, and must be reported by name."""
    import tempfile
    good_path = os.path.join(
        STORE, "records", "fixture-mini@1.0", TESTEE_A,
        "fixture-mini@1.0__pcrec_1.0.0-gdeadbee_vm-caps-simdna__repfix-box__20260825T100000Z.jsonl")
    with open(good_path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    broken = lines[:1] + ["{not valid json"] + lines[2:]

    with tempfile.TemporaryDirectory() as td:
        records_dir = os.path.join(td, "records", "fixture-mini@1.0", TESTEE_A)
        os.makedirs(records_dir, exist_ok=True)
        broken_path = os.path.join(records_dir, os.path.basename(good_path))
        with open(broken_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(broken) + "\n")

        paths, _source = report.discover_records(td)
        loaded = report.load_all(paths, check_filename=True)
        _check(len(loaded) == 1, f"expected 1 candidate, got {len(loaded)}")
        _check(len(loaded[0].problems) > 0,
               "a record with invalid JSON on a row line must have validation problems")

        args = _args(store=td, include_synthetic=True)
        rd, err = report.build_report(loaded, args)
        _check(err is None, f"a single invalid record must not trigger a mixed-version refusal: {err}")
        _check(not rd.included, "the broken record must not be counted as included")
        _check(len(rd.excluded_invalid) == 1,
               f"expected 1 excluded-invalid entry, got {len(rd.excluded_invalid)}")
        _check(broken_path == rd.excluded_invalid[0][0],
               f"the excluded record's path must be named: {rd.excluded_invalid[0][0]!r}")


def test_markdown_and_tsv_render_without_error():
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    tsv = report.render_tsv(rd)
    _check("# pcrec-bench report" in md, "markdown report must have the expected header")
    _check(md.startswith("# pcrec-bench report"), "markdown report must start with its title")
    _check(tsv.startswith("#"), "tsv report must start with the self-describing comment line")
    _check("median_ns" in tsv, "tsv report must carry the median metric rows")


def test_deterministic_output():
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd1, _ = report.build_report(loaded, args)
    rd2, _ = report.build_report(loaded, args)
    md1 = report.render_markdown(rd1)
    md2 = report.render_markdown(rd2)
    _check(md1 == md2, "rendering the same report twice must be byte-identical")


TESTS = [
    test_store_discovery_uses_index_when_present,
    test_store_discovery_walks_when_index_absent,
    test_all_fixtures_validate,
    test_known_reduction,
    test_expectation_failing_cell_is_excluded_from_ranking,
    test_set_grain_sums_per_subject_ns_per_call,
    test_set_grain_excludes_whole_set_when_any_subject_fails,
    test_unsupported_by_declaration_outcome,
    test_where_filter_dotted_path,
    test_regime_filter_restricts_match_rows_only,
    test_subbench_and_version_filters,
    test_synthetic_excluded_by_default,
    test_mixed_schema_versions_refused,
    test_invalid_record_is_dropped_with_a_message,
    test_markdown_and_tsv_render_without_error,
    test_deterministic_output,
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
