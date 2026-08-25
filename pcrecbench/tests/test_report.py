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
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
FIXDIR = os.path.join(HERE, "fixtures")
PKG_ROOT = os.path.dirname(os.path.dirname(HERE))  # .../worktrees/b5report

if PKG_ROOT not in sys.path:
    sys.path.insert(0, PKG_ROOT)

from pcrecbench import report  # noqa: E402


STORE = os.path.join(FIXDIR, "store")
STORE_WALK_ONLY = os.path.join(FIXDIR, "store_walk_only")
# v1.1 (manager, 2026-08-25): two SEPARATE mixed-version scenarios, kept in
# separate subdirectories so querying one never accidentally exercises the
# other's refusal -- see fixtures/mixed_version/CLAUDE.md.
MIXED_VERSION_MAJOR = os.path.join(FIXDIR, "mixed_version", "major_mismatch")
MIXED_VERSION_MINOR = os.path.join(FIXDIR, "mixed_version", "minor_pair")

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


# ------------------------------------------------- [B9] hand-built record helpers
#
# R1 (status), R2 (dedup/--all-records), R3 (tier, a schema v1.2 field the
# validator this reporter shares does not know yet) and R8 (cross-pin) are
# tested directly against `report.build_report`/`report.LoadedRecord`,
# bypassing `schema/validate.py` entirely -- the same technique this file's
# `_lazy_jit_derivation` test already uses for a case no fixture testee
# exercises end-to-end. `tier` in particular CANNOT go through a real
# fixture file yet: the schema's `setup` object is `additionalProperties:
# false`, so a `tier` field the validator does not know about would be
# REJECTED, never reaching the tier-exclusion logic under test (the [B9]
# brief's own escape hatch: "keep that fixture out of the validator-checked
# set and say so in the report" -- here, "out of the validator" entirely).

def _mini_setup(testee_id, sb_id="rb-mini", sb_version="1.0", machine="m1",
                 timestamp="2026-08-25T10:00:00Z", status="measured",
                 status_detail=None, tier=None, record_id=None, subjects=None):
    s = {
        "kind": "setup",
        "schema_version": "1.1",
        "record_id": record_id or f"{sb_id}@{sb_version}__{testee_id}__{machine}",
        "subbench": {"id": sb_id, "version": sb_version},
        "testee": {"testee_id": testee_id},
        "environment": {"machine_id": machine},
        "run": {"timestamp": timestamp},
        "status": status,
    }
    if status_detail is not None:
        s["status_detail"] = status_detail
    if tier is not None:
        s["tier"] = tier
    if subjects is not None:
        s["subjects"] = subjects
    return s


def _mini_row(pattern_id, subject_id, regime, trial, seq, ns, iterations=1000, form=None):
    row = {
        "kind": "match", "pattern_id": pattern_id, "subject_id": subject_id,
        "regime": regime, "trial": trial, "seq": seq,
        "match_outcome": "matched-as-expected",
        "timing": {"elapsed_ns": ns * iterations, "iterations": iterations,
                   "bytes_processed": iterations},
    }
    if form:
        row["form"] = form
    return row


def _mk_loaded(path, setup, rows):
    return report.LoadedRecord(path=path, setup=setup, rows=rows, problems=[],
                                schema_major=1, schema_minor=1)


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
    mixed_version/*/  'ok' halves) must independently pass
    schema/validate.py -- the brief's 'all fixtures ... validating with
    schema/validate.py'. Two fixtures are DELIBERATELY exempted, and each
    asserts exactly WHY it fails rather than merely THAT it fails (see
    fixtures/mixed_version/CLAUDE.md):
      * major_mismatch/'s 2.0 file -- rule X17 (unreadable future major).
      * minor_pair/'s schema-1.0-shaped file -- generic SCHEMA errors
        (missing v1.1-required fields), NOT X17, since its major (1)
        agrees with the validator's; record_schema.md 4.1's own point
        that "a 1.0-stamped file is NOT readable as 1.1"."""
    for store_dir in (STORE, STORE_WALK_ONLY):
        loaded, paths, _source = _load_store(store_dir)
        for rec in loaded:
            _check(not rec.problems,
                   f"{rec.path} unexpectedly failed validation: {rec.problems}")

    mm_paths, _source = report.discover_records(MIXED_VERSION_MAJOR)
    mm_loaded = report.load_all(mm_paths, check_filename=True)
    ok = [r for r in mm_loaded if not r.problems]
    bad = [r for r in mm_loaded if r.problems]
    _check(len(ok) == 1, f"expected exactly 1 valid record in major_mismatch, got {len(ok)}")
    _check(len(bad) == 1, f"expected exactly 1 invalid record in major_mismatch, got {len(bad)}")
    _check(any(p.rule == "X17" for p in bad[0].problems),
           f"the invalid major_mismatch record should fail on X17, got: {bad[0].problems}")

    mp_paths, _source = report.discover_records(MIXED_VERSION_MINOR)
    mp_loaded = report.load_all(mp_paths, check_filename=True)
    mp_ok = [r for r in mp_loaded if not r.problems]
    mp_bad = [r for r in mp_loaded if r.problems]
    _check(len(mp_ok) == 1, f"expected exactly 1 valid record in minor_pair, got {len(mp_ok)}")
    _check(len(mp_bad) == 1, f"expected exactly 1 invalid record in minor_pair, got {len(mp_bad)}")
    _check(not any(p.rule == "X17" for p in mp_bad[0].problems),
           f"the minor_pair old-shape record must NOT fail on X17 (same major, 1) -- "
           f"it should fail on missing v1.1 fields instead; got: {mp_bad[0].problems}")
    _check(any(p.rule == "SCHEMA" for p in mp_bad[0].problems),
           f"expected generic SCHEMA (missing-field) problems, got: {mp_bad[0].problems}")


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
        sb, tid, pattern_id, subject_id, regime, form = k
        if (tid == TESTEE_A and pattern_id == "p-digits"
                and subject_id == "s-num-1" and regime == "match-compliance"):
            key = k
            break
    _check(key is not None, "known-reduction cell not found in rd.match_cells")
    _check(key[5] == "whole-subject",
           "pcrec's match-compliance rows are v1.1 form=whole-subject "
           f"(record_schema.md 5 ADDITIONS 3); got form={key[5]!r}")
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
    """--grain subject: the (pattern, subject, regime) exclusion. Testee
    B's p-word/s-word-1/match-compliance is `form: plain` (B has no
    end-anchored-mode workaround) and testee A's SAME (pattern, subject,
    regime) is `form: whole-subject` (pcrec's own compliance artifact).

    Manager fix request (2026-08-25), reversing this module's first cut:
    `form` is NOT a ranking-group key -- both testees answering the same
    (pattern, subject, regime) belong in ONE group regardless of form
    (record_schema.md 5 ADDITIONS 3 says the two artifacts are different
    THINGS, not that they answer different QUESTIONS; ranking exists to
    compare engines on a question). So this checks A and B are in the
    SAME group, B is excluded from THAT group's rankable set while A
    remains rankable in it, and each entry still carries its own form."""
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True, grain="subject")
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    _check(rd.grain == "subject", f"expected rd.grain == 'subject', got {rd.grain!r}")

    groups = report._ranking_groups(rd, grain="subject")

    key = next((k for k in groups if k[1] == "p-word" and k[2] == "s-word-1"
                and k[3] == "match-compliance"), None)
    _check(key is not None, "expected ONE p-word/s-word-1/match-compliance group to exist")
    _check(len(key) == 4, f"the group key must NOT carry form (4-tuple), got {key}")
    entries = groups[key]
    testees_present = {t for t, _f, _r in entries}
    _check(testees_present == {TESTEE_A, TESTEE_B},
           f"testee A (whole-subject) and testee B (plain) must share ONE group, got {testees_present}")

    testee_a_form, _a_red = next((f, r) for t, f, r in entries if t == TESTEE_A)
    testee_b_form, testee_b_red = next((f, r) for t, f, r in entries if t == TESTEE_B)
    _check(testee_a_form == "whole-subject",
           f"expected testee A's form == 'whole-subject', got {testee_a_form!r}")
    _check(testee_b_form == "plain",
           f"expected testee B's form == 'plain' (absent on the row), got {testee_b_form!r}")
    _check(testee_b_red.expectation_failing,
           "testee B's did-not-match-as-expected cell must be flagged expectation_failing")
    _check(testee_b_red.pass_rate == 0.0, f"expected pass_rate 0.0, got {testee_b_red.pass_rate}")

    rankable = [t for t, _f, r in entries if not r.expectation_failing and r.n_timed]
    _check(rankable == [TESTEE_A],
           f"testee B must be excluded from the SHARED group's rankable set while testee A "
           f"remains rankable in it, got {rankable}")

    md = report.render_markdown(rd)
    _check("Excluded from ranking" in md, "markdown report must have an excluded-cells section")
    _check(TESTEE_B in md.split("Excluded from ranking")[1].split("## Compile cost")[0],
           "testee B's failing cell must be listed under Excluded from ranking")


def test_form_never_splits_the_ranking_table():
    """THE FIX ITSELF (manager, 2026-08-25): p-digits/match-compliance has
    THREE testees answering the SAME question via TWO different forms --
    pcrec (`whole-subject`, its own `(?:pattern)\\z` artifact) and both
    libpcre2 testees (`plain`, runtime ANCHORED|ENDANCHORED flags on
    their ordinary artifact). All three MUST appear in ONE ranking table,
    each row carrying its own form, at both grains -- the whole point of
    `form` is to make this comparison possible, not to prevent it."""
    loaded, _paths, _source = _load_store(STORE)

    for grain in ("set", "subject"):
        args = _args(store=STORE, include_synthetic=True, grain=grain)
        rd, err = report.build_report(loaded, args)
        _check(err is None, f"unexpected refusal (grain={grain}): {err}")

        groups = report._ranking_groups(rd, grain=grain)
        if grain == "subject":
            key = next((k for k in groups if k[1] == "p-digits" and k[2] == "s-num-1"
                        and k[3] == "match-compliance"), None)
        else:
            key = next((k for k in groups if k[1] == "p-digits"
                        and k[2] == "match-compliance"), None)
        _check(key is not None, f"expected a p-digits/match-compliance group to exist (grain={grain})")
        entries = groups[key]
        testees_present = {t for t, _f, _r in entries}
        _check(testees_present == {TESTEE_A, TESTEE_B, TESTEE_C},
               f"all three testees must share ONE p-digits/match-compliance group "
               f"(grain={grain}), got {testees_present}")
        forms_by_testee = {t: f for t, f, _r in entries}
        _check(forms_by_testee[TESTEE_A] == "whole-subject",
               f"expected testee A form == 'whole-subject' (grain={grain}), "
               f"got {forms_by_testee[TESTEE_A]!r}")
        _check(forms_by_testee[TESTEE_B] == "plain" and forms_by_testee[TESTEE_C] == "plain",
               f"expected testees B and C form == 'plain' (grain={grain}), got {forms_by_testee}")

        md = report.render_markdown(rd)
        _check(TESTEE_A in md and TESTEE_B in md and TESTEE_C in md,
               "sanity: all three testee ids must appear somewhere in the report")
        _check("| form |" in md, "the ranking table must carry a form column")
        _check("`whole-subject`" in md and "`plain`" in md,
               "both form values must appear as per-row column values in the rendered report")


def test_compile_cost_still_keyed_by_form():
    """The ONE place `form` remains a key (manager, 2026-08-25): a
    whole-subject compile row is a genuinely separate compile (its own
    cost, own artifact, own trials) -- pcrec's p-digits gets TWO compile
    cells here, `plain` and `whole-subject`, never pooled."""
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")

    forms_for_a_digits = {form for (_sb, t, p, form), (_t, _r) in rd.compile_cells.items()
                           if t == TESTEE_A and p == "p-digits"}
    _check(forms_for_a_digits == {"plain", "whole-subject"},
           f"expected pcrec's p-digits compile cells keyed by BOTH forms, got {forms_for_a_digits}")


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
                if k[1] == TESTEE_A and k[2] == "p-digits" and k[3] == "match-compliance"
                and k[4] == "whole-subject"), None)
    _check(key is not None, "expected a whole-subject set cell for (testee A, p-digits, match-compliance)")
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
    subj_key = (single_key[0], TESTEE_A, "p-digits", "s-num-1", "short-subject-search", "plain")
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
    """Testee B's (p-word, match-compliance) set has TWO failing subjects:
    s-word-1 (wrong answer, all 3 trials did-not-match-as-expected) and
    s-give-up-1 (v1.1 ADDITION: all 3 trials gave-up, the engine's own
    resource limit). Per the manager's rule, the WHOLE set cell must be
    excluded, not averaged through; per the manager's gave-up request,
    the two failure REASONS must be counted and labelled separately, not
    folded into one tally."""
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)  # grain='set'
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")

    key = next((k for k in rd.set_cells
                if k[1] == TESTEE_B and k[2] == "p-word" and k[3] == "match-compliance"), None)
    _check(key is not None, "expected a (testee B, p-word, match-compliance) set cell")
    _tid, red = rd.set_cells[key]
    _check(red.expectation_failing, "the set cell must be flagged expectation_failing")
    _check(red.n_subjects == 2, f"expected n_subjects == 2 (s-word-1 + s-give-up-1), got {red.n_subjects}")
    _check(red.failing_subjects == ["s-give-up-1", "s-word-1"],
           f"expected failing_subjects == ['s-give-up-1', 's-word-1'], got {red.failing_subjects}")
    _check(red.pass_rate == 0.0, f"expected pass_rate 0.0 (2 subjects, 0 agreeing), got {red.pass_rate}")
    _check(red.n_trials == 0, f"an excluded set cell must carry no reduced trials, got {red.n_trials}")

    # gave-up counted APART from wrong answers (manager, 2026-08-25), both
    # at the aggregate SetCellReduction level and per failing subject.
    _check(red.n_gave_up == 3, f"expected n_gave_up == 3 (s-give-up-1's 3 trials), got {red.n_gave_up}")
    _check(red.n_wrong == 3, f"expected n_wrong == 3 (s-word-1's 3 trials), got {red.n_wrong}")
    _check(report._failure_label(red.failing_detail["s-give-up-1"]) == "gave-up",
           f"expected s-give-up-1 labelled 'gave-up', got "
           f"{report._failure_label(red.failing_detail['s-give-up-1'])!r}")
    _check(report._failure_label(red.failing_detail["s-word-1"]) == "wrong",
           f"expected s-word-1 labelled 'wrong', got "
           f"{report._failure_label(red.failing_detail['s-word-1'])!r}")

    md = report.render_markdown(rd)
    _check("SET grain" in md, "the set-grain report must label itself as such")
    excluded_section = md.split("Excluded from ranking")[1].split("## Compile cost")[0]
    _check("s-word-1" in excluded_section and "s-give-up-1" in excluded_section,
           "both failing subjects must be named in the set-grain excluded table")
    _check("(gave-up)" in excluded_section and "(wrong)" in excluded_section,
           f"the excluded table must label EACH failing subject's reason "
           f"separately, not just list ids: {excluded_section!r}")


def test_unsupported_by_declaration_outcome():
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")

    found = False
    for (sb, testee_id, pattern_id, form), (tid, red) in rd.compile_cells.items():
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
    regimes_seen = {regime for (_sb, _t, _p, _s, regime, _f), _v in rd.match_cells.items()}
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


def test_lazy_jit_derivation_uses_lowest_seq_not_trial_one():
    """Unit test of `_lazy_jit_derivation` directly (schema v1.1,
    record_schema.md 8: 'first-match-row-minus-steady-state', the
    GLOBALLY-first timed match row by `seq` minus the median of every
    other timed row) -- against HAND-BUILT rows, not a fixture record,
    since none of this lane's fixture testees are `lazy-jit` (see
    report.py's module docstring for why).

    Deliberately constructs the rows so the lowest-`seq` row is NOT
    `trial == 1` of whichever (subject, regime) sorts first, and is not
    even the row with the smallest `trial` number anywhere -- exercising
    exactly the distinction the manager's correction (2026-08-25) is
    about: 'first' means emission order (`seq`), never `trial`.

      seq=2 (subject B, short-subject-search, trial=1): ns/call = 40   <- the true "first"
      seq=3 (subject B, short-subject-search, trial=2): ns/call = 20
      seq=4 (subject B, short-subject-search, trial=3): ns/call = 22
      seq=5 (subject A, match-compliance,    trial=1): ns/call = 25   <- trial=1 but NOT lowest seq
      seq=6 (subject A, match-compliance,    trial=2): ns/call = 24

    steady state = median(20, 22, 25, 24) = 23.0
    derived = 40 - 23.0 = 17.0
    """
    def row(seq, subject_id, regime, trial, elapsed_ns, iterations=1000):
        return {
            "kind": "match", "pattern_id": "p-lazy", "subject_id": subject_id,
            "regime": regime, "trial": trial, "seq": seq,
            "match_outcome": "matched-as-expected",
            "timing": {"elapsed_ns": elapsed_ns, "iterations": iterations,
                        "bytes_processed": 3 * iterations},
        }

    rows = [
        row(5, "subject-a", "match-compliance", 1, 25000),
        row(6, "subject-a", "match-compliance", 2, 24000),
        row(2, "subject-b", "short-subject-search", 1, 40000),
        row(3, "subject-b", "short-subject-search", 2, 20000),
        row(4, "subject-b", "short-subject-search", 3, 22000),
    ]
    derived = report._lazy_jit_derivation(rows)
    _check(len(derived) == 1, f"expected exactly one derived value, got {derived}")
    expected = 40.0 - statistics.median([20.0, 22.0, 25.0, 24.0])
    _check(abs(derived[0] - expected) < 1e-9,
           f"expected derived == {expected} (40 minus steady-state median 23.0), "
           f"got {derived[0]}")

    # fewer than 2 timed rows -> no derivation possible
    _check(report._lazy_jit_derivation(rows[:1]) == [],
           "a single timed row has no 'steady state' to subtract from")
    _check(report._lazy_jit_derivation([]) == [],
           "no timed rows -> no derivation")

    # a non-timed row (e.g. gave-up) must never be treated as a candidate "first"
    untimed_first = [{"kind": "match", "pattern_id": "p-lazy", "subject_id": "x",
                        "regime": "match-compliance", "trial": 1, "seq": 1,
                        "match_outcome": "gave-up", "diagnostic": "budget exhausted"}] + rows
    derived2 = report._lazy_jit_derivation(untimed_first)
    _check(derived2 == derived,
           f"an untimed row (even at the lowest seq) must be skipped, not treated as "
           f"the derivation's subtrahend; got {derived2}, expected {derived}")


def test_mixed_schema_versions_refused():
    """major_mismatch/: a real 1.x record + a declared-2.0 record -- the
    reporter refuses the whole query rather than silently dropping one."""
    loaded, _paths, _source = _load_store(MIXED_VERSION_MAJOR)
    args = _args(store=MIXED_VERSION_MAJOR, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(rd is None, "a report spanning two major schema versions must be refused (rd is None)")
    _check(err is not None and "mix MAJOR schema versions" in err, f"unexpected error text: {err!r}")
    _check("1.x" in err and "2.x" in err, f"the refusal message must name both majors: {err!r}")


def test_minor_version_pair_not_refused():
    """minor_pair/: a schema-1.0-SHAPED record (pre-v1.1 content, now
    invalid under the current schema -- missing seq/calibration/the new
    load+occupancy shape/etc, per record_schema.md 4.1's own warning)
    alongside a real 1.1-valid record. SAME major (1), different minor
    (0 vs 1): the reporter must NOT treat this as a mixed-version
    refusal -- it must drop the old-shaped record via the ordinary
    per-record-invalidity path (with its own message) and report
    normally on the 1.1 record (manager, 2026-08-25: 'a real 1.0-vs-1.1
    minor pair')."""
    loaded, _paths, _source = _load_store(MIXED_VERSION_MINOR)
    args = _args(store=MIXED_VERSION_MINOR, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None,
           f"a MINOR-only version difference (both major=1) must not be refused as "
           f"'mixed versions'; got: {err!r}")
    _check(len(rd.included) == 1,
           f"expected exactly 1 record included (the 1.1 one), got {len(rd.included)}: {rd.included}")
    _check(len(rd.excluded_invalid) == 1,
           f"expected exactly 1 record excluded as invalid (the old-shaped 1.0 one), "
           f"got {len(rd.excluded_invalid)}")
    excluded_path, excluded_problems = rd.excluded_invalid[0]
    _check("090000Z" in excluded_path,
           f"expected the OLD-shaped record (timestamp 09:00:00Z) to be the excluded one, "
           f"got {excluded_path!r}")
    _check(any("seq" in p or "required" in p for p in excluded_problems),
           f"the excluded-record message should point at a missing v1.1 field; "
           f"got: {excluded_problems[:2]}")
    _check("1.1" in rd.schema_versions,
           f"the surviving record's schema version must be 1.1, got {rd.schema_versions}")


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


def test_status_gate_r1():
    """[B9] R1/OD-B14: a ranking row whose record `status` is not
    `measured` is excluded from ranking by default (listed under its
    table as 'not ranked: <testee> -- <status> (<excerpt>)'), and ranked
    -- with its status shown -- under --include-unmeasured."""
    setup_a = _mini_setup("engine-a_1.0.0_cfg-caps-simdna", status="measured")
    setup_b = _mini_setup("engine-b_1.0.0_cfg-caps-simdna", status="inconclusive-load",
                           status_detail="box was noisy during the run")
    rows_a = [_mini_row("p1", "s1", "short-subject-search", t, t, 100) for t in (1, 2, 3)]
    rows_b = [_mini_row("p1", "s1", "short-subject-search", t, t, 50) for t in (1, 2, 3)]
    loaded = [_mk_loaded("a.jsonl", setup_a, rows_a), _mk_loaded("b.jsonl", setup_b, rows_b)]

    args = _args(store="x", include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("`engine-a_1.0.0_cfg-caps-simdna` | measured |" in md,
           f"the measured testee must appear ranked, with its status shown:\n{md}")
    _check("not ranked: `engine-b_1.0.0_cfg-caps-simdna` — inconclusive-load "
           "(box was noisy during the run)" in md,
           f"expected a 'not ranked' line naming status and excerpt:\n{md}")
    _check("`engine-b_1.0.0_cfg-caps-simdna` |" not in md,
           "the inconclusive-load testee must not appear as a ranked ROW by default")

    args2 = _args(store="x", include_synthetic=True, include_unmeasured=True)
    rd2, err2 = report.build_report(loaded, args2)
    _check(err2 is None, f"unexpected refusal: {err2}")
    md2 = report.render_markdown(rd2)
    _check("`engine-b_1.0.0_cfg-caps-simdna` | inconclusive-load |" in md2,
           f"--include-unmeasured must rank the row with its status shown:\n{md2}")


def test_duplicate_record_dedup_r2():
    """[B9] R2/OD-B15: two records of one (subbench@version, testee_id,
    machine) -- the NEWEST by run.timestamp ranks by default (the older
    superseded, named in the header, never pooled); --all-records shows
    each record as its own row, its testee id suffixed by timestamp."""
    setup_old = _mini_setup("engine-c_1.0.0_cfg-caps-simdna",
                             timestamp="2026-08-25T09:00:00Z", record_id="rec-old")
    setup_new = _mini_setup("engine-c_1.0.0_cfg-caps-simdna",
                             timestamp="2026-08-25T11:00:00Z", record_id="rec-new")
    rows_old = [_mini_row("p1", "s1", "short-subject-search", t, t, 999) for t in (1, 2, 3)]
    rows_new = [_mini_row("p1", "s1", "short-subject-search", t, t, 100) for t in (1, 2, 3)]
    loaded = [_mk_loaded("old.jsonl", setup_old, rows_old), _mk_loaded("new.jsonl", setup_new, rows_new)]

    args = _args(store="x", include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    _check([rid for rid, _p in rd.included] == ["rec-new"],
           f"only the newest record should be included, got {rd.included}")
    _check(rd.superseded == [("rec-new", ["rec-old"])],
           f"expected rec-old superseded by rec-new, got {rd.superseded}")
    md = report.render_markdown(rd)
    _check("`rec-old` superseded by `rec-new`" in md, f"the header must name the superseded record:\n{md}")
    key = next(k for k in rd.set_cells if k[1] == "engine-c_1.0.0_cfg-caps-simdna")
    _tid, red = rd.set_cells[key]
    _check(red.median_ns == 100.0,
           f"the reduction must come from the NEWEST record ONLY (100.0), not pooled "
           f"with the superseded record (999.0) -- got {red.median_ns}")

    args_all = _args(store="x", include_synthetic=True, all_records=True)
    rd_all, err_all = report.build_report(loaded, args_all)
    _check(err_all is None, f"unexpected refusal: {err_all}")
    _check(sorted(rid for rid, _p in rd_all.included) == ["rec-new", "rec-old"],
           f"--all-records must include both records, got {rd_all.included}")
    testees_present = {k[1] for k in rd_all.set_cells}
    _check(testees_present == {"engine-c_1.0.0_cfg-caps-simdna@20260825T090000Z",
                                "engine-c_1.0.0_cfg-caps-simdna@20260825T110000Z"},
           f"--all-records must suffix each record's testee id by its timestamp, got {testees_present}")


def test_scratch_tier_gate_r3():
    """[B9] R3: the optional schema v1.2 `tier` field (absent = `pinned`)
    -- a `scratch` row is excluded from ranking by default (listed as
    'scratch: <testee>'), and ranked -- with a `tier` column -- under
    --include-scratch."""
    setup_pinned = _mini_setup("engine-d_1.0.0_cfg-caps-simdna", status="measured")
    setup_scratch = _mini_setup("engine-e_1.0.0_cfg-caps-simdna", status="measured", tier="scratch")
    rows_p = [_mini_row("p1", "s1", "short-subject-search", t, t, 100) for t in (1, 2, 3)]
    rows_s = [_mini_row("p1", "s1", "short-subject-search", t, t, 50) for t in (1, 2, 3)]
    loaded = [_mk_loaded("d.jsonl", setup_pinned, rows_p), _mk_loaded("e.jsonl", setup_scratch, rows_s)]

    args = _args(store="x", include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("scratch: `engine-e_1.0.0_cfg-caps-simdna` (tier=scratch)" in md,
           f"expected a scratch exclusion line:\n{md}")
    _check("`engine-e_1.0.0_cfg-caps-simdna` |" not in md,
           "the scratch-tier testee must not appear as a ranked row by default")

    args2 = _args(store="x", include_synthetic=True, include_scratch=True)
    rd2, err2 = report.build_report(loaded, args2)
    _check(err2 is None, f"unexpected refusal: {err2}")
    md2 = report.render_markdown(rd2)
    _check("| tier |" in md2, f"the tier column must appear under --include-scratch:\n{md2}")
    _check("scratch |" in md2, "the scratch row's tier value must be shown as a column")


def test_form_fact_and_mixed_regime_note_r4():
    """[B9] R4: `fact` restates `form` ('separate artifact' /
    'same program'); a ranking table whose rankable rows mix both facts
    (pcrec's whole-subject p-digits compliance row beside libpcre2's
    plain one, this suite's existing fixture) carries the 'regime
    artifact' note under its title."""
    _check(report._form_fact("whole-subject") == "separate artifact",
           "whole-subject must be a separate artifact")
    _check(report._form_fact("plain") == "same program", "plain must be the same program")
    _check(report._form_fact(None) == "same program", "an absent form means plain, i.e. same program")

    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    section = md.split("`p-digits` / `match-compliance`")[1].split("###")[0]
    _check("same program" in section and "separate artifact" in section,
           f"the fact column must show both values in a mixed-form ranking group:\n{section}")
    _check("rows compare different programs answering the same regime" in section,
           f"a table mixing forms must carry the regime-artifact note:\n{section}")


def test_two_ratio_columns_r5():
    """[B9] R5: two ratio columns, `vs baseline` (named in the table
    TITLE) and `vs best` (the best measured row = 1.000x)."""
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("| vs baseline | vs best |" in md, f"expected two ratio columns:\n{md[:2000]}")
    _check("baseline: libpcre2 engine_mode=interp" in md,
           "the baseline testee must be named in the table title")
    section = md.split("`p-digits` / `match-compliance`")[1].split("###")[0]
    first_row_line = next(l for l in section.split("\n") if l.startswith("| 1 |"))
    cells = [c.strip() for c in first_row_line.strip("|").split("|")]
    _check(cells[-1] == "1.000x", f"rank 1's 'vs best' ratio must be 1.000x, got {cells[-1]!r}")


def test_near_floor_columns_r6():
    """[B9] R6: short-subject-search tables (SET grain) always carry
    `n subjects` and `per-subject mean ns`, plus a floor note; no floor
    field exists in the schema yet, so the note says so honestly."""
    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)  # grain='set'
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    section = md.split("`p-digits` / `short-subject-search`")[1].split("###")[0]
    _check("n subjects" in section and "per-subject mean ns" in section,
           f"short-subject-search tables must always carry n subjects + per-subject mean:\n{section}")
    _check("floor: n/a" in section, f"a floor note must follow a short-subject-search table:\n{section}")


def test_gave_up_cell_summary_r7():
    """[B9] R7/OD-B11: a set cell's give-ups shown by CODE, counted in
    SUBJECTS not trials, with the smallest firing subject named --
    `_extract_diagnostic_code` and `_gave_up_cell_summary` directly,
    then the existing fixture's single gave-up subject end-to-end."""
    _check(report._extract_diagnostic_code(
               "the engine gave up rather than answering: giveup:-4:PCREC_ERR_WORK")
           == "PCREC_ERR_WORK", "expected PCREC_ERR_WORK extracted")
    _check(report._extract_diagnostic_code(
               "pcre2: PCRE2_ERROR_MATCHLIMIT (match limit exceeded) -- FIXTURE")
           == "PCRE2_ERROR_MATCHLIMIT",
           "a trailing all-caps WORD with no underscore (FIXTURE) must not be mistaken for the code")
    _check(report._extract_diagnostic_code(None) is None, "no diagnostic -> no code")

    def _mkc(n_gave_up, code):
        codes = Counter({code: n_gave_up}) if n_gave_up else Counter()
        return report.MatchCellReduction(
            n_trials=n_gave_up, n_timed=0, median_ns=None, min_ns=None, max_ns=None,
            stddev_ns=None, iters=[], outcome_counts={"gave-up": n_gave_up} if n_gave_up else {},
            pass_rate=0.0, n_gave_up=n_gave_up, n_wrong=0, gave_up_codes=codes)

    failing_detail = {
        "big": _mkc(3, "PCREC_ERR_STEPS"),
        "small": _mkc(3, "PCREC_ERR_STEPS"),
        "other": _mkc(3, "PCREC_ERR_FRAMES"),
    }
    subject_bytes = {"big": 1000, "small": 5, "other": 50}
    summary = report._gave_up_cell_summary(failing_detail, subject_bytes)
    _check(summary == "PCREC_ERR_FRAMES×1 (smallest: other, 50 B); PCREC_ERR_STEPS×2 (smallest: small, 5 B)",
           f"unexpected gave-up summary: {summary!r}")
    _check(report._gave_up_cell_summary({}, {}) == "0", "no gave-ups -> '0'")

    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    excl = md.split("Excluded from ranking")[1].split("## Compile cost")[0]
    _check("PCRE2_ERROR_MATCHLIMIT×1 (smallest: s-give-up-1, 3 B)" in excl,
           f"expected the fixture's gave-up subject formatted by R7's rule:\n{excl}")


def test_cross_pin_delta_r8():
    """[B9] R8: a cross-pin pair (same engine+config, different
    version_slug) gets a computed Δ verdict and a worst-subject note; a
    cell excluded at the previous pin and ranked now says
    'now measured (was: <reason>)'."""
    _check(report._parse_testee_config("pcrec_692c2e8_auto-caps-simdna")
           == ("pcrec", "692c2e8", "auto-caps-simdna"), "expected engine/version/config split")
    _check(report._parse_testee_config("pcrec_692c2e8_auto-caps-simdna@20260825T175131Z")
           == ("pcrec", "692c2e8", "auto-caps-simdna"),
           "an --all-records date suffix must be stripped before parsing")
    _check(report._parse_testee_config("weird") is None,
           "a testee id with fewer than 3 underscore segments has no config to parse")

    _check(report._cross_pin_verdict(100.0, 1.0, 100.5, 1.0) == "unchanged (within spread)",
           "a small difference within 2x the larger stddev must read as unchanged")
    _check(report._cross_pin_verdict(100.0, 1.0, 50.0, 1.0) == "faster ×2.00", "half the time -> faster x2.00")
    _check(report._cross_pin_verdict(50.0, 1.0, 100.0, 1.0) == "slower ×2.00", "double the time -> slower x2.00")

    setup_old = _mini_setup("pcrec_AAAAAAA_vm-caps-simdna",
                             timestamp="2026-08-25T09:00:00Z", record_id="rec-old8")
    setup_new = _mini_setup("pcrec_BBBBBBB_vm-caps-simdna",
                             timestamp="2026-08-25T11:00:00Z", record_id="rec-new8")
    rows_old = [_mini_row("p1", "s1", "short-subject-search", t, t, 100) for t in (1, 2, 3)]
    rows_new = [_mini_row("p1", "s1", "short-subject-search", t, t, 40) for t in (1, 2, 3)]
    loaded = [_mk_loaded("old8.jsonl", setup_old, rows_old), _mk_loaded("new8.jsonl", setup_new, rows_new)]
    args = _args(store="x", include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("Δ vs previous version" in md, f"expected a delta column:\n{md}")
    _check("faster ×2.50" in md, f"100ns -> 40ns is a 2.5x speedup:\n{md}")
    _check("Δ detail: `pcrec_BBBBBBB_vm-caps-simdna` vs previous `pcrec_AAAAAAA_vm-caps-simdna`" in md,
           f"expected a worst-subject Δ detail line:\n{md}")

    # a same-VERSION pair (e.g. two --all-records rows of one identical pin)
    # must NOT be treated as a cross-pin pair.
    same_version = report._parse_testee_config("pcrec_AAAAAAA_vm-caps-simdna@20260825T090000Z")
    _check(same_version == ("pcrec", "AAAAAAA", "vm-caps-simdna"), same_version)

    # 'now measured (was: <reason>)': the OLD pin's cell was expectation-failing
    # (a wrong answer), the NEW pin's cell passes.
    setup_old2 = _mini_setup("pcrec_CCCCCCC_vm-caps-simdna",
                              timestamp="2026-08-25T09:00:00Z", record_id="rec-old8b")
    setup_new2 = _mini_setup("pcrec_DDDDDDD_vm-caps-simdna",
                              timestamp="2026-08-25T11:00:00Z", record_id="rec-new8b")
    row_old_wrong = {"kind": "match", "pattern_id": "p2", "subject_id": "s1",
                      "regime": "short-subject-search", "trial": 1, "seq": 1,
                      "match_outcome": "did-not-match-as-expected"}
    rows_new2 = [_mini_row("p2", "s1", "short-subject-search", t, t, 40) for t in (1, 2, 3)]
    loaded2 = [_mk_loaded("old8b.jsonl", setup_old2, [row_old_wrong]),
               _mk_loaded("new8b.jsonl", setup_new2, rows_new2)]
    rd2, err2 = report.build_report(loaded2, args)
    _check(err2 is None, f"unexpected refusal: {err2}")
    md2 = report.render_markdown(rd2)
    _check("now measured (was: wrong)" in md2, f"expected the 'now measured' verdict:\n{md2}")


def test_mechanism_stamp_columns_r9():
    """[B9] R9: pcrec compile-cost stamp columns, read ONLY from
    `engine_metadata` -- a DFA row states the no-stamp fact rather than
    a blank; `entry` is derived from buffer-pair presence; the compile
    table splits by phase and flags timer jitter."""
    dfa_stamp = report._mechanism_stamp_columns({"engine": "dfa", "ncaps": 1})
    _check(dfa_stamp["engine"] == "dfa", "engine must be read from engine_metadata")
    _check(dfa_stamp["prefilter"] == "(no stamp — pcrec I-3)",
           f"a DFA row must state the no-stamp fact, got {dfa_stamp['prefilter']!r}")
    _check(dfa_stamp["entry"] == "plain entry", "no buffer pair -> plain entry")

    vm_stamp = report._mechanism_stamp_columns({
        "engine": "vm", "prefilter": "hybrid",
        "vm_rungs": ["PCREC_VM_RUNG_CURSOR", "PCREC_VM_RUNG_REVDET"],
        "buffer_frames": 32768, "buffer_trail": 131072, "resume_frame_size": 24})
    _check(vm_stamp["entry"] == "_in", "a buffer-capacity pair present -> the _in entry")
    _check(vm_stamp["prefilter"] == "hybrid", "a VM row's declared prefilter must pass through")
    _check(vm_stamp["vm_rungs"] == "PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_REVDET",
           f"expected bit names joined by |, got {vm_stamp['vm_rungs']!r}")
    _check(vm_stamp["buffer_frames"] == 32768 and vm_stamp["resume_frame_size"] == 24,
           "buffer_frames/resume_frame_size must pass through")

    vm_no_buffers = report._mechanism_stamp_columns({"engine": "vm", "prefilter": "none"})
    _check(vm_no_buffers["entry"] == "plain entry", "no buffer pair on a VM row -> plain entry too")
    _check(vm_no_buffers["vm_rungs"] == "-", "no vm_rungs declared -> '-'")

    _check(report._jitter_flag(100.0, 50.0) == "", "stddev below median -> no jitter flag")
    _check(report._jitter_flag(100.0, 150.0) == "timer jitter", "stddev above median -> the jitter flag")
    _check(report._jitter_flag(None, 1.0) == "", "no median -> no flag (nothing to compare)")

    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    compiled = md.split("### `compiled-aot`")[1].split("### `")[0]
    _check("engine" in compiled and "entry" in compiled and "vm_rungs" in compiled,
           f"the compiled-aot table must carry the mechanism-stamp columns:\n{compiled[:800]}")
    _check("emit-c ns" in compiled and "gcc ns" in compiled and "load ns" in compiled,
           "the compiled-aot table must carry the phase-split columns")
    interp = md.split("### `interpretive`")[1]
    _check("vm_rungs" not in interp,
           "a non-pcrec compile class must NOT carry the pcrec-only stamp columns")


def test_subbench_dir_alias_od_b13():
    """OD-B13: `--subbench` accepts the sub-bench DIRECTORY name
    (`email`) as well as the sidecar id (`email-specimen`), resolved via
    `bench/<dir>/subbench.toml`'s own `id` field."""
    resolved, note = report.resolve_subbench_arg("email", report.REPO_ROOT)
    _check(resolved == "email-specimen", f"expected 'email' resolved to 'email-specimen', got {resolved!r}")
    _check(note is not None and "email-specimen" in note and "'email'" in note,
           f"expected an alias note, got {note!r}")

    resolved2, note2 = report.resolve_subbench_arg("email-specimen", report.REPO_ROOT)
    _check(resolved2 == "email-specimen", "an already-sidecar id must pass through unchanged")
    _check(note2 is None, "no alias note when the value was already the sidecar id")

    resolved3, note3 = report.resolve_subbench_arg("nonexistent-dir", report.REPO_ROOT)
    _check(resolved3 == "nonexistent-dir", "an unknown directory name must pass through unchanged")
    _check(note3 is None, "no alias note for an unresolved value")


TESTS = [
    test_store_discovery_uses_index_when_present,
    test_store_discovery_walks_when_index_absent,
    test_all_fixtures_validate,
    test_known_reduction,
    test_expectation_failing_cell_is_excluded_from_ranking,
    test_form_never_splits_the_ranking_table,
    test_compile_cost_still_keyed_by_form,
    test_set_grain_sums_per_subject_ns_per_call,
    test_set_grain_excludes_whole_set_when_any_subject_fails,
    test_unsupported_by_declaration_outcome,
    test_lazy_jit_derivation_uses_lowest_seq_not_trial_one,
    test_where_filter_dotted_path,
    test_regime_filter_restricts_match_rows_only,
    test_subbench_and_version_filters,
    test_synthetic_excluded_by_default,
    test_mixed_schema_versions_refused,
    test_minor_version_pair_not_refused,
    test_invalid_record_is_dropped_with_a_message,
    test_markdown_and_tsv_render_without_error,
    test_deterministic_output,
    test_status_gate_r1,
    test_duplicate_record_dedup_r2,
    test_scratch_tier_gate_r3,
    test_form_fact_and_mixed_regime_note_r4,
    test_two_ratio_columns_r5,
    test_near_floor_columns_r6,
    test_gave_up_cell_summary_r7,
    test_cross_pin_delta_r8,
    test_mechanism_stamp_columns_r9,
    test_subbench_dir_alias_od_b13,
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
