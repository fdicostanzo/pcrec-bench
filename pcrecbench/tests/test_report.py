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
import re
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
# [B14]: the PROJECT's own real committed store (email-specimen@0.1, the
# 692c2e8/8da6120 pcrec pins alongside libpcre2) -- used by R1/R2/R3/R4/R7's
# end-to-end firing checks, since those rulings need REAL engine_metadata
# stamps (resume_frames/trail_frames/buffer_frames pairs at two different
# pins) and a REAL `bench/email/expectations.tsv` (R3) that no synthetic
# fixture here reproduces. Read-only; nothing in this suite writes to it.
REAL_STORE = os.path.join(report.REPO_ROOT, "store")
STORE_WALK_ONLY = os.path.join(FIXDIR, "store_walk_only")
# v1.1 (manager, 2026-08-25): two SEPARATE mixed-version scenarios, kept in
# separate subdirectories so querying one never accidentally exercises the
# other's refusal -- see fixtures/mixed_version/CLAUDE.md.
MIXED_VERSION_MAJOR = os.path.join(FIXDIR, "mixed_version", "major_mismatch")
MIXED_VERSION_MINOR = os.path.join(FIXDIR, "mixed_version", "minor_pair")
# [B20] (schema v1.4): a VALID 1.3 + 1.4 pair of ONE cell (the pcrec fixture
# re-stamped 1.3 at 12:00; the same grown to 5 trials with the
# trial_agreement block at 12:05) plus a 1.4 `inconclusive-spread` record
# of the jit testee with FAILED after samples -- see fixtures/CLAUDE.md.
V14_PAIR = os.path.join(FIXDIR, "v14_pair", "store")
GOLDEN_V8 = os.path.join(FIXDIR, "golden", "store_v8.md")
V13_RID = "fixture-mini@1.0__pcrec_1.0.0-gdeadbee_vm-caps-simdna__repfix-box__20260825T120000Z"
V14_RID = "fixture-mini@1.0__pcrec_1.0.0-gdeadbee_vm-caps-simdna__repfix-box__20260825T120500Z"
SPREAD_RID = "fixture-mini@1.0__libpcre2_10.46_jit-caps-simdna__repfix-box__20260825T121000Z"

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


# [B12] R10, THE test_report RUNTIME FIX: `_load_store(REAL_STORE)` pays
# `schema/validate.py`'s jsonschema validation cost for EVERY record in
# `store/` -- measured at ~39 s per call on this box once bench/loglines
# and email-specimen@0.2's records joined email-specimen@0.1's (26
# records, 2026-08-29; `python3 -m cProfile` pointed the cost at
# `jsonschema.validators.iter_errors`/`descend`/`referencing`'s `$ref`
# resolution, not file I/O -- `report.discover_records` itself takes
# ~0.1 ms). Seven call sites in this suite each pay that cost
# independently, which is where `test_report`'s > 2 minute runtime goes
# (`gnutimeout 540 python3 -u -m pytest ...` durations, 2026-08-29).
# Loading it ONCE for the whole suite run and sharing the result is safe:
# nothing in this suite, and nothing in `report.build_report`/
# `report.render_markdown`/`render_tsv`, ever mutates a `LoadedRecord`
# after `report.load_all` returns it (checked: no `r.setup = `/`r.rows =
# `/`r.problems = ` assignment exists in report.py outside the
# dataclass's own constructor) -- every reader only iterates and reduces.
# `REAL_STORE`'s SYNTHETIC counterpart (`STORE`, the small hand-built
# fixture store) is not cached here: it is fast on its own (well under a
# second for all of `fixtures/store/`) and every one of ITS few call
# sites already gets a fresh, independent `loaded` list, which is a
# smaller thing to reason about than adding a second cache for a store
# that was never the slow one.
_REAL_STORE_CACHE = None


def _load_real_store():
    """Cached `_load_store(REAL_STORE)` -- see the comment above. Returns
    the SAME `(loaded, paths, source)` tuple (and the same `LoadedRecord`
    objects inside it) to every caller within one process run."""
    global _REAL_STORE_CACHE
    if _REAL_STORE_CACHE is None:
        _REAL_STORE_CACHE = _load_store(REAL_STORE)
    return _REAL_STORE_CACHE


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
                 status_detail=None, tier=None, record_id=None, subjects=None,
                 patterns=None):
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
    if patterns is not None:
        # [B14] R9: schema v1.3's `patterns[].role` is not yet schema-legal
        # (`setup` is `additionalProperties: false` until b15floor lands
        # it) -- only ever reaches `build_report` through a hand-built
        # LoadedRecord that bypasses `schema/validate.py`, same technique
        # R3's [B9] `tier` tests already use.
        s["patterns"] = patterns
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
    for store_dir in (STORE, STORE_WALK_ONLY, V14_PAIR):
        loaded, paths, _source = _load_store(store_dir)
        for rec in loaded:
            _check(not rec.problems,
                   f"{rec.path} unexpectedly failed validation: {rec.problems}")
    # [B20] R8: the inconclusive-spread fixture's block RECOMPUTES (X32 fired
    # on it at validation above, so this only names the fact) and one
    # group of >= 2 rows with two slow trials each is what disagrees.
    loaded, _p, _s = _load_store(V14_PAIR)
    spread = next(r for r in loaded if r.setup["record_id"] == SPREAD_RID)
    blk = spread.setup["trial_agreement"]
    _check(spread.setup["status"] == "inconclusive-spread" and blk["verdict"] == "disagree"
           and blk["groups_disagreeing"] == 1 and blk["worst_group"]["d"] == 2
           and blk["worst_group"]["n"] == 2,
           f"the spread fixture must disagree on one 2-row group: {blk}")

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

    # [B20] R1 (v1.4): an `inconclusive-spread` record is unranked like
    # `inconclusive-load`, and its parenthesis prints FROM THE BLOCK, never
    # from the free text -- the CONTROL: the measured fixture in the same
    # group ranks, and the spread record's `status_detail` is a decoy the
    # bullet must not echo.
    loaded, _p, _s = _load_store(V14_PAIR)
    args3 = _args(store=V14_PAIR, include_synthetic=True)
    rd3, err3 = report.build_report(loaded, args3)
    _check(err3 is None, f"unexpected refusal: {err3}")
    md3 = report.render_markdown(rd3)
    _check("not ranked: `libpcre2_10.46_jit-caps-simdna` — inconclusive-spread "
           "(1 of 4 groups disagree, worst p-digits / match-compliance / plain "
           "d=2 of n=2, k=1.5)" in md3,
           f"the spread bullet must print the block's numbers:\n{md3}")
    _check("the trials' agreement decided" not in md3.split("## Ranking")[1],
           "the not-ranked bullet must come from the block, not from status_detail")
    _check("`pcrec_1.0.0-gdeadbee_vm-caps-simdna` | measured |" in md3,
           f"the measured 1.4 record in the same group must rank:\n{md3}")
    args4 = _args(store=V14_PAIR, include_synthetic=True, include_unmeasured=True)
    rd4, _e = report.build_report(loaded, args4)
    md4 = report.render_markdown(rd4)
    _check("`libpcre2_10.46_jit-caps-simdna` | inconclusive-spread |" in md4,
           f"--include-unmeasured must rank the spread row with its status:\n{md4}")


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
    # [B14] R8: shortened to a one-line count (pcrecdev1 feedback repin-v2
    # (4)) -- the ids themselves live in `rd.superseded` (checked above)
    # and in `--all-records`, not repeated in the rendered header.
    _check("superseded: 1 record(s) (OD-B15; --all-records lists them)" in md,
           f"the header must summarise the superseded count:\n{md}")
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


def test_duplicate_record_dedup_prefers_measured_r2():
    """[B9] R2/OD-B15, AMENDED (manager, 2026-08-25, before merge): the
    default kept record is the NEWEST *MEASURED* one, not merely the
    newest by timestamp -- a newer non-measured record is not evidence
    against an older measured one of the same testee and version.
    Three scenarios, matching the real store's libpcre2-interp shape:
    (a) measured-older beats unmeasured-newer -- the newer one is listed
        as "newer, not measured", NOT superseded, and the reduction
        comes from the OLDER measured record;
    (b) unmeasured-only still shows -- when NO record in the group is
        measured, the newest record overall stands (unranked per R1
        unless --include-unmeasured), same as before this amendment;
    (c) both at once (older-superseded AND newer-not-measured around one
        measured record in the middle) -- the real shape this amendment
        exists for."""
    # (a) measured-older beats unmeasured-newer
    setup_old_measured = _mini_setup("engine-f_1.0.0_cfg-caps-simdna", status="measured",
                                      timestamp="2026-08-25T02:22:00Z", record_id="rec-f-measured")
    setup_new_unmeasured = _mini_setup("engine-f_1.0.0_cfg-caps-simdna", status="inconclusive-load",
                                        status_detail="box was noisy", timestamp="2026-08-25T13:34:00Z",
                                        record_id="rec-f-unmeasured")
    rows_old_measured = [_mini_row("p1", "s1", "short-subject-search", t, t, 100) for t in (1, 2, 3)]
    rows_new_unmeasured = [_mini_row("p1", "s1", "short-subject-search", t, t, 999) for t in (1, 2, 3)]
    loaded_a = [_mk_loaded("f-old.jsonl", setup_old_measured, rows_old_measured),
                _mk_loaded("f-new.jsonl", setup_new_unmeasured, rows_new_unmeasured)]
    args = _args(store="x", include_synthetic=True)
    rd_a, err_a = report.build_report(loaded_a, args)
    _check(err_a is None, f"unexpected refusal: {err_a}")
    _check([rid for rid, _p in rd_a.included] == ["rec-f-measured"],
           f"the older MEASURED record must be kept, got {rd_a.included}")
    _check(rd_a.superseded == [],
           f"the newer non-measured record must NOT be listed as superseded, got {rd_a.superseded}")
    _check(rd_a.newer_not_measured == [("rec-f-measured", "rec-f-unmeasured", "inconclusive-load")],
           f"expected the newer record listed as 'newer, not measured', got {rd_a.newer_not_measured}")
    key_a = next(k for k in rd_a.set_cells if k[1] == "engine-f_1.0.0_cfg-caps-simdna")
    _tid_a, red_a = rd_a.set_cells[key_a]
    _check(red_a.median_ns == 100.0,
           f"the reduction must come from the OLDER MEASURED record (100.0), never the "
           f"newer non-measured one (999.0) -- got {red_a.median_ns}")
    md_a = report.render_markdown(rd_a)
    _check("newer, not measured: `rec-f-unmeasured` (inconclusive-load) -- kept `rec-f-measured`" in md_a,
           f"expected the header's 'newer, not measured' line:\n{md_a}")
    _check("`engine-f_1.0.0_cfg-caps-simdna` | measured |" in md_a,
           f"the kept (measured) record must rank by default:\n{md_a}")

    # (b) unmeasured-only still shows -- no record in the group is measured,
    # so the newest overall stands (the pre-amendment fallback), and the
    # older one is still an ordinary superseded duplicate.
    setup_g_old = _mini_setup("engine-g_1.0.0_cfg-caps-simdna", status="inconclusive-load",
                               timestamp="2026-08-25T09:00:00Z", record_id="rec-g-old")
    setup_g_new = _mini_setup("engine-g_1.0.0_cfg-caps-simdna", status="inconclusive-load",
                               timestamp="2026-08-25T11:00:00Z", record_id="rec-g-new")
    rows_g_old = [_mini_row("p1", "s1", "short-subject-search", t, t, 50) for t in (1, 2, 3)]
    rows_g_new = [_mini_row("p1", "s1", "short-subject-search", t, t, 60) for t in (1, 2, 3)]
    loaded_b = [_mk_loaded("g-old.jsonl", setup_g_old, rows_g_old),
                _mk_loaded("g-new.jsonl", setup_g_new, rows_g_new)]
    rd_b, err_b = report.build_report(loaded_b, args)
    _check(err_b is None, f"unexpected refusal: {err_b}")
    _check([rid for rid, _p in rd_b.included] == ["rec-g-new"],
           f"with no measured record at all, the newest overall must stand, got {rd_b.included}")
    _check(rd_b.superseded == [("rec-g-new", ["rec-g-old"])],
           f"the older one is an ordinary superseded duplicate, got {rd_b.superseded}")
    _check(rd_b.newer_not_measured == [],
           f"nothing is 'newer than the kept measured record' when none is measured, "
           f"got {rd_b.newer_not_measured}")
    md_b = report.render_markdown(rd_b)
    _check("not ranked: `engine-g_1.0.0_cfg-caps-simdna` — inconclusive-load" in md_b,
           f"the unmeasured-only kept record must still be unranked by default (R1):\n{md_b}")

    # (c) both at once -- older-superseded AND newer-not-measured around
    # one measured record in the middle (the real store's exact shape:
    # libpcre2-interp measured@06:22, then re-measured inconclusive@17:34
    # -- here with an extra older duplicate too, for full coverage).
    setup_h_oldest = _mini_setup("engine-h_1.0.0_cfg-caps-simdna", status="inconclusive-load",
                                  timestamp="2026-08-25T01:00:00Z", record_id="rec-h-oldest")
    setup_h_measured = _mini_setup("engine-h_1.0.0_cfg-caps-simdna", status="measured",
                                    timestamp="2026-08-25T02:22:00Z", record_id="rec-h-measured")
    setup_h_newest = _mini_setup("engine-h_1.0.0_cfg-caps-simdna", status="inconclusive-load",
                                  timestamp="2026-08-25T13:34:00Z", record_id="rec-h-newest")
    rows_h = [_mini_row("p1", "s1", "short-subject-search", t, t, 70) for t in (1, 2, 3)]
    loaded_c = [_mk_loaded("h-oldest.jsonl", setup_h_oldest, rows_h),
                _mk_loaded("h-measured.jsonl", setup_h_measured, rows_h),
                _mk_loaded("h-newest.jsonl", setup_h_newest, rows_h)]
    rd_c, err_c = report.build_report(loaded_c, args)
    _check(err_c is None, f"unexpected refusal: {err_c}")
    _check([rid for rid, _p in rd_c.included] == ["rec-h-measured"],
           f"the single measured record (the middle one) must be kept, got {rd_c.included}")
    _check(rd_c.superseded == [("rec-h-measured", ["rec-h-oldest"])],
           f"the OLDER-than-kept record must still be superseded, got {rd_c.superseded}")
    _check(rd_c.newer_not_measured == [("rec-h-measured", "rec-h-newest", "inconclusive-load")],
           f"the NEWER-than-kept, non-measured record must be listed separately, "
           f"got {rd_c.newer_not_measured}")


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
    `pcrecbench.reduce.giveup_code` (the SHARED extractor `quick` also
    uses, R5 -- imported by name here since [B10] landed it) and
    `_gave_up_cell_summary` directly, then the existing fixture's single
    gave-up subject end-to-end."""
    _check(report.giveup_code(
               {"match_outcome": "gave-up",
                "diagnostic": "the engine gave up rather than answering: giveup:-4:PCREC_ERR_WORK"})
           == "-4:PCREC_ERR_WORK",
           "expected the driver-protocol token's numeric code AND name extracted")
    _check(report.giveup_code(
               {"match_outcome": "gave-up",
                "diagnostic": "pcre2: PCRE2_ERROR_MATCHLIMIT (match limit exceeded) -- FIXTURE"})
           == "pcre2: PCRE2_ERROR_MATCHLIMIT (match limit exceeded) -- FIXTURE",
           "an engine whose diagnostic never carries the giveup: token falls back to the raw text")
    _check(report.giveup_code({"match_outcome": "matched-as-expected"}) is None,
           "a non-gave-up row has no give-up code")

    def _mkc(n_gave_up, code):
        codes = {code: n_gave_up} if n_gave_up else {}
        return report.MatchCellReduction(
            n_trials=n_gave_up, n_timed=0, median_ns=None, min_ns=None, max_ns=None,
            stddev_ns=None, iters=[], outcome_counts={"gave-up": n_gave_up} if n_gave_up else {},
            pass_rate=0.0, n_gave_up=n_gave_up, n_wrong=0, giveup_codes=codes)

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
    expected_code = "pcre2: PCRE2_ERROR_MATCHLIMIT (match limit exceeded) -- FIXTURE"
    _check(f"{expected_code}×1 (smallest: s-give-up-1, 3 B)" in excl,
           f"expected the fixture's gave-up subject formatted by R7's rule, reduce.py's "
           f"raw-diagnostic-fallback spelling and all:\n{excl}")


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
    # [B16] R1 SUPERSEDES this ruling's "(no stamp -- pcrec I-3)" string.
    # I-3 was CLEARED at pcrec abi 4: a DFA artifact stamps its own scan and
    # candidate-start filter now, and they are `dfa_scan`/`dfa_prefilter`,
    # not the VM's `prefilter`. This row declares neither, so both read `-`
    # here and `_dfa_scan_display` is what turns that into a sentence
    # (`test_dfa_scan_legend_b16_r1` covers the sentence, including which
    # KIND of absence it is).
    _check(dfa_stamp["prefilter"] == "-",
           f"an undeclared VM prefilter must pass through as '-', got "
           f"{dfa_stamp['prefilter']!r}")
    _check(dfa_stamp["dfa_prefilter"] == "-" and dfa_stamp["dfa_scan"] == "-",
           "an undeclared DFA scan pair must pass through as '-'")
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

    # [B14] R5 superseded the boolean 'stddev > median' flag with the
    # ratio itself, plus 'timer-floor' under the clock's practical floor
    # -- see test_jitter_ratio_r5 below for the dedicated ruling test.
    # `_jitter_flag` is still exercised here because R9's mechanism-stamp
    # columns and R5's jitter column share the same compiled-aot table.
    _check(report._jitter_flag(100000.0, 50000.0, 90000.0) == "0.500",
           "stddev/median, three decimals")

    loaded, _paths, _source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    compiled = md.split("### `compiled-aot`")[1].split("### `")[0]
    # [B14] R8: engine/entry/prefilter/vm_rungs moved from table COLUMNS
    # to a one-line-per-testee LEGEND above the table.
    _check("engine=" in compiled and "entry=" in compiled and "rungs=" in compiled,
           f"the compiled-aot table must carry the mechanism-stamp legend:\n{compiled[:800]}")
    _check("emit-c ns" in compiled and "gcc ns" in compiled and "load ns" in compiled,
           "the compiled-aot table must carry the phase-split columns")
    interp = md.split("### `interpretive`")[1]
    _check("rungs=" not in interp,
           "a non-pcrec compile class must NOT carry the pcrec-only stamp legend")


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


# ============================================================= [B14] tests
#
# One test per ruling (R1-R10), each exercising both the rule FIRING and a
# case where it does not -- docs/dev/feedback_pcrecdev1_2026-08-25-repin-v2.md
# is the spec. R1/R2/R4/R7's firing cases go through `REAL_STORE` (the
# project's own committed email-specimen sample): they need REAL
# `engine_metadata` stamps at two different pcrec pins, which no synthetic
# fixture here reproduces. R3 (CORRECTED, KB-2 -- see its own docstring)
# is exercised entirely against the synthetic fixture store, on purpose:
# the whole point of the fix is that the reporter no longer reaches into
# `bench/` at all. R5/R6/R8/R9 go through hand-built `LoadedRecord`s (the
# same technique the [B9] `tier`/cross-pin tests already use); R9 also
# gets a REAL schema-valid fixture FILE (`fixtures/floor_pattern/`,
# validated by `schema/validate.py` itself, not bypassed) now that lane
# b15floor's schema v1.3 makes `patterns[].role` legal.

def test_plain_entry_capacities_r1():
    """[B14] R1: a plain-entry compile row (no `buffer_frames`/
    `buffer_trail`) is not bufferless -- it runs on the STAMPED DEFAULT
    capacity (`resume_frames`/`trail_frames`), and that is what
    [OPT-1]'s cost is proportional to (pcrecdev1 feedback, repin-v2
    (1)). Firing: `pcrec_692c2e8_vm-caps-simdna`'s plain entry in the
    REAL store stamps `resume_frames=2048`/`trail_frames=3072` (abi 3).
    Not firing: `_in` rows keep the caller capacity unchanged, and a
    pre-I-3 pin (`pcrec_8da6120_vm-caps-simdna`) stamped neither pair at
    all, so R1 has nothing to derive from (R4 covers that case: `n/s`)."""
    _check(report._buffers_display({"resume_frames": 2048, "trail_frames": 3072})
           == "2048/3072 (stamped default)",
           "a plain entry with a stamped rx_info pair must show the STAMPED DEFAULT")
    _check(report._buffers_display({"buffer_frames": 32768, "buffer_trail": 131072,
                                     "resume_frames": 2048, "trail_frames": 3072})
           == "32768/131072 (caller-provided)",
           "an _in row keeps the CALLER capacity even when the stamped default is also present")
    _check(report._buffers_display({}) == "n/s", "no pair stamped at all -> n/s")

    loaded, _paths, _source = _load_real_store()
    args = _args(store=REAL_STORE, subbench="email-specimen")
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    compiled = md.split("### `compiled-aot`")[1].split("### `")[0]
    # The legend's WORDING moved at [B16] (R1's dfa clause, R2's fast tier,
    # R3's engine reading), so this assertion checks the two facts THIS
    # ruling is about -- the testee's identity and its stamped-default
    # capacity in one line -- rather than pinning a sentence another
    # ruling owns. The literal-line form of the check belongs to whichever
    # ruling last set the wording; see `test_dfa_scan_legend_b16_r1`.
    vm_legend = [ln for ln in compiled.splitlines()
                 if ln.startswith("- `pcrec_692c2e8_vm-caps-simdna`")]
    _check(len(vm_legend) == 1,
           f"expected exactly one legend line for the plain VM testee, got "
           f"{len(vm_legend)}:\n{compiled[:1500]}")
    _check("entry=plain entry" in vm_legend[0]
           and "buffers=2048/3072 (stamped default)" in vm_legend[0]
           and "frame=24" in vm_legend[0],
           f"expected the plain VM entry's stamped-default capacity in the "
           f"legend:\n{vm_legend[0]}")
    in_legend = [ln for ln in compiled.splitlines()
                 if ln.startswith("- `pcrec_692c2e8_vm-in-caps-simdna`")]
    _check(len(in_legend) == 1 and "entry=_in" in in_legend[0]
           and "buffers=32768/131072 (caller-provided)" in in_legend[0]
           and "frame=24" in in_legend[0],
           f"an _in row must still show the CALLER capacity unchanged:\n"
           f"{in_legend or compiled[:1500]}")


def test_matching_subject_count_r3():
    """[B14] R3, CORRECTED (KB-2, manager steer 2026-08-25): the reporter
    works from RECORDS ALONE -- this ruling's first cut read `bench/
    <dir>/expectations.tsv` through `pcrecbench.subbench`, which this
    test used to exercise against the real store; that dependency is
    gone (`report.py` no longer imports `pcrecbench.subbench` at all).
    `_matching_subject_count` now always returns `None` -- checked
    directly, and end to end against the EXISTING fixture store (real
    schema-valid records, `fixture-mini`, whose `p-digits`/`match-
    compliance` cell already exercises the match-compliance regime) --
    because the record's own `matched-as-expected` rows carry `observed:
    null` (verified against this very fixture below), so there is no
    per-subject expected-answer field to derive `m`/`n` from. The
    rendered line therefore reads `matches: n/s`, not a fabricated
    fraction and not silence."""
    _check(report._matching_subject_count(None, "no-such-sb@1.0", "orig", "match-compliance", ["s-000"])
           is None, "always None for now -- KB-2 is unresolved")
    _check(report._matching_subject_count(None, "email-specimen@0.1", "orig",
                                           "large-subject-throughput", ["t-a-valid-addrs"]) is None,
           "always None regardless of regime too")

    loaded, _paths, _source = _load_store(STORE)
    # Confirm the premise directly against the fixture's own bytes: a
    # matched-as-expected match-compliance row carries `observed: null`,
    # the fact the whole correction rests on.
    for rec in loaded:
        for row in rec.rows:
            if (row.get("kind") == "match" and row.get("regime") == "match-compliance"
                    and row.get("match_outcome") == "matched-as-expected"):
                _check(row.get("observed") is None,
                       f"premise check: expected observed=null on a matched-as-expected "
                       f"row, got {row.get('observed')!r} ({rec.path})")

    args = _args(store=STORE, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    n_s_lines = [l for l in md.splitlines() if l.strip().startswith("- matches:")]
    _check(n_s_lines and all("n/s" in l for l in n_s_lines),
           f"every match-compliance group must state 'matches: n/s', got:\n{n_s_lines}")
    _check("KB-2" in md, f"the n/s note must point at the tracked known issue:\n{n_s_lines}")
    _check(not re.search(r"matches: \d+/\d+", md),
           f"must never print a fabricated m/n fraction:\n{n_s_lines}")

    # Not firing (regime-gated): the fixture store has exactly TWO
    # match-compliance groups (p-digits, p-word) and no others -- so
    # exactly two 'matches:' lines total, none attached to its
    # short-subject-search groups.
    _check(len(n_s_lines) == 2, f"expected exactly 2 'matches:' lines "
           f"(p-digits, p-word match-compliance), got {len(n_s_lines)}: {n_s_lines}")


def test_buffer_frame_legend_r4():
    """[B14] R4: `n/s` (neither pair stamped at this pin) vs `0 (DFA)`
    (stamped, and zero because a DFA artifact takes no buffers) -- `-`
    and bare `0` must never again stand for two different facts
    (pcrecdev1 feedback, repin-v2 (2))."""
    _check(report._buffers_display({"resume_frames": 0, "trail_frames": 0}) == "0 (DFA)",
           "a stamped, all-zero pair is a DFA fact, not a blank")
    _check(report._buffers_display({}) == "n/s", "neither pair stamped -> n/s")
    _check(report._frame_size_display({"resume_frame_size": 0}) == "0 (DFA)",
           "a stamped, zero frame size is a DFA fact")
    _check(report._frame_size_display({}) == "n/s", "no frame size stamped -> n/s")
    _check(report._frame_size_display({"resume_frame_size": 24}) == "24",
           "a real stamped frame size passes through as-is")

    loaded, _paths, _source = _load_real_store()
    args = _args(store=REAL_STORE, subbench="email-specimen")
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    compiled = md.split("### `compiled-aot`")[1].split("### `")[0]
    # As above: [B16] R1 retired the "(no stamp -- pcrec I-3)" clause (I-3
    # is CLEARED; the DFA side stamps its own mechanism from pcrec abi 4),
    # so this ruling's own two facts are what is checked here.
    dfa_legend = [ln for ln in compiled.splitlines()
                  if ln.startswith("- `pcrec_692c2e8_auto-caps-simdna`")]
    _check(len(dfa_legend) == 1,
           f"expected exactly one legend line for the DFA testee, got "
           f"{len(dfa_legend)}:\n{compiled[:1500]}")
    _check("engine=dfa" in dfa_legend[0]
           and "buffers=0 (DFA)" in dfa_legend[0]
           and "frame=0 (DFA)" in dfa_legend[0],
           f"a DFA artifact at a stamped pin must read '0 (DFA)', not a "
           f"blank:\n{dfa_legend[0]}")
    # 8da6120 is the pin whose `auto` testee compiled `orig` to a DFA
    # artifact and `factored` to a VM one, so under [B16] R3 its legend is
    # SPLIT per (pattern, form) instead of one line claiming the first
    # pattern's engine for both. This ruling's own fact -- neither buffer
    # pair stamped at that pin reads `n/s`, never the same `0` as the DFA
    # fact above -- is checked on the `orig`/`plain` line.
    old_orig = [ln for ln in compiled.splitlines()
                if ln.startswith("- `pcrec_8da6120_auto-caps-simdna` / "
                                 "`orig` / `plain`")]
    _check(len(old_orig) == 1 and "engine=dfa" in old_orig[0]
           and "buffers=n/s" in old_orig[0] and "frame=n/s" in old_orig[0],
           f"a pre-I-3 pin (neither pair stamped) must read 'n/s', not the same '0' "
           f"as the DFA fact above:\n{old_orig or compiled[:1500]}")


def test_tiny_set_per_subject_subtable_r2():
    """[B14] R2: a SET cell of <= 3 subjects (today, every
    `large-subject-throughput` cell) gets its own per-subject sub-table
    -- subject id, bytes, median ns/call, ns/byte, for every ranked
    testee -- and every throughput ranking row gains `ns/byte` beside
    `ns/call`. Not firing: `short-subject-search` (77-85 subjects) gets
    neither."""
    loaded, _paths, _source = _load_real_store()
    args = _args(store=REAL_STORE, subbench="email-specimen")
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)

    # Split on "\n### `" (NOT bare "### `"): a per-subject sub-table's own
    # heading is "#### ..." which itself contains "### `" as a substring
    # starting at its second character, so a bare split would wrongly cut
    # the section off before the sub-table it is meant to capture.
    # Both the opening AND closing split points are anchored on "\n### `"
    # (a leading newline, exactly three hashes): a bare "### `<pattern>` /
    # `<regime>`" is not unique here -- R2's own per-subject sub-table
    # heading is "#### `<pattern>` / `<regime>` per-subject (...)", which
    # CONTAINS the bare three-hash text as a substring one character in,
    # so a bare split cuts the section off before the very sub-table this
    # test means to capture.
    throughput = md.split("\n### `orig` / `large-subject-throughput`")[1].split("\n### `")[0]
    _check("| rank | testee | status | form | fact | median ns/call | ns/byte | min |" in throughput,
           f"a throughput ranking row must carry ns/byte beside ns/call:\n{throughput[:600]}")
    _check("#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.1)" in throughput,
           f"a <=3-subject set must get its own per-subject sub-table:\n{throughput}")
    _check("| `t-a-valid-addrs` | 1,048,576 |" in throughput,
           f"the sub-table must name each subject with its byte count:\n{throughput}")

    search = md.split("\n### `orig` / `short-subject-search`")[1].split("\n### `")[0]
    _check("per-subject (" not in search,
           f"a 77-subject search set must NOT get the tiny-set sub-table:\n{search[:400]}")
    header_line = next(l for l in search.splitlines() if l.startswith("| rank |"))
    _check("ns/byte" not in header_line,
           f"short-subject-search is not a throughput regime -- no ns/byte column:\n{header_line}")


def test_jitter_ratio_r5():
    """[B14] R5: jitter is a computed ratio (`stddev/median`), not a
    boolean; `timer-floor` when `min_ns` is under the clock's practical
    floor (20 microseconds); a column empty on EVERY row of a table is
    OMITTED, not rendered as a wall of blanks (pcrecdev1 feedback,
    repin-v2 (2))."""
    _check(report._jitter_flag(100000.0, 50000.0, 90000.0) == "0.500",
           "stddev/median, three decimals")
    _check(report._jitter_flag(100000.0, 10000.0, 5000.0) == "timer-floor",
           "min_ns under 20 microseconds -> timer-floor, regardless of the ratio")
    _check(report._jitter_flag(None, None, None) == "", "nothing costed -> empty, not a ratio")
    _check(report._jitter_flag(0, 10.0, 90000.0) == "", "a zero median must not divide by zero")

    # Firing: the real store's interpretive compile rows have min well
    # under 20 microseconds (a libpcre2 interp compile is a handful of
    # microseconds) -- 'timer-floor', not a ratio close to 1.
    loaded, _paths, _source = _load_real_store()
    args = _args(store=REAL_STORE, subbench="email-specimen")
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    interp = md.split("### `interpretive`")[1].split("### `")[0] if "### `interpretive`" in md \
        else md.split("### `interpretive`")[1]
    _check("timer-floor" in interp, f"expected timer-floor on a sub-20us interpretive compile:\n{interp}")

    # Not firing: a column empty on EVERY row of a table is omitted --
    # a hand-built record whose only compile row never compiled (no
    # `cost` at all) has NOTHING to compute jitter from anywhere in its
    # (sole) class, so the header must not carry a 'jitter' column.
    setup = _mini_setup("engine-j_1.0.0_cfg-caps-simdna")
    row_uncompiled = {"kind": "compile", "pattern_id": "p1", "trial": 1, "seq": 1,
                       "compile_outcome": "did-not-compile", "cost_class": "interpretive",
                       "diagnostic": "syntax error -- FIXTURE"}
    loaded2 = [_mk_loaded("j.jsonl", setup, [row_uncompiled])]
    rd2, err2 = report.build_report(loaded2, _args(store="x", include_synthetic=True))
    _check(err2 is None, f"unexpected refusal: {err2}")
    md2 = report.render_markdown(rd2)
    section = md2.split("### `interpretive`")[1]
    header_line2 = next(l for l in section.splitlines() if l.startswith("| pattern |"))
    _check("jitter" not in header_line2,
           f"a table with nothing to compute jitter from must drop the column:\n{header_line2}")


def test_artifact_bytes_column_r7():
    """[B14] R7: a compile row's `artifact_bytes` becomes a column on
    every compile-cost table (pcrec and non-pcrec alike), so gcc time
    can be read against SIZE, not against engine. Not firing: a row
    with no `artifact_bytes` at all prints `-`, never a fabricated
    number."""
    setup = _mini_setup("engine-k_1.0.0_cfg-caps-simdna")
    row_sized = {"kind": "compile", "pattern_id": "p1", "trial": 1, "seq": 1,
                 "compile_outcome": "compiled", "cost_class": "interpretive",
                 "cost": {"total_ns": 1000}, "artifact_bytes": 4096}
    row_unsized = {"kind": "compile", "pattern_id": "p2", "trial": 1, "seq": 2,
                   "compile_outcome": "compiled", "cost_class": "interpretive",
                   "cost": {"total_ns": 2000}}
    loaded = [_mk_loaded("k.jsonl", setup, [row_sized, row_unsized])]
    rd, err = report.build_report(loaded, _args(store="x", include_synthetic=True))
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("| `p1` | `engine-k_1.0.0_cfg-caps-simdna` | 1,000.0 | 1,000.0 | 1,000.0 | 0.0 | 1 | 4,096 |" in md,
           f"expected artifact_bytes=4,096 on the sized row:\n{md}")
    _check("| `p2` | `engine-k_1.0.0_cfg-caps-simdna` | 2,000.0 | 2,000.0 | 2,000.0 | 0.0 | 1 | - |" in md,
           f"expected '-' (not a fabricated number) on the unsized row:\n{md}")

    # Firing against the real store too, for a real number.
    loaded_r, _p, _s = _load_real_store()
    rd_r, err_r = report.build_report(loaded_r, _args(store=REAL_STORE, subbench="email-specimen"))
    _check(err_r is None, f"unexpected refusal: {err_r}")
    md_r = report.render_markdown(rd_r)
    _check("29,744" in md_r, f"expected the real store's artifact_bytes to appear:\n{md_r[:200]}")


def test_legend_and_superseded_shortening_r8():
    """[B14] R8: two shortenings. The Query header's superseded-record
    list collapses to one summary line (`--all-records` is where the
    ids live); the compile-cost table's six per-testee CONSTANT columns
    move to a one-line-per-testee LEGEND above the table, not repeated
    on every (pattern, form) row."""
    setup_old = _mini_setup("engine-l_1.0.0_cfg-caps-simdna",
                             timestamp="2026-08-25T09:00:00Z", record_id="rec-l-old")
    setup_new = _mini_setup("engine-l_1.0.0_cfg-caps-simdna",
                             timestamp="2026-08-25T11:00:00Z", record_id="rec-l-new")
    rows_old = [_mini_row("p1", "s1", "short-subject-search", t, t, 999) for t in (1, 2, 3)]
    rows_new = [_mini_row("p1", "s1", "short-subject-search", t, t, 100) for t in (1, 2, 3)]
    loaded = [_mk_loaded("l-old.jsonl", setup_old, rows_old), _mk_loaded("l-new.jsonl", setup_new, rows_new)]
    rd, err = report.build_report(loaded, _args(store="x", include_synthetic=True))
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("superseded: 1 record(s) (OD-B15; --all-records lists them)" in md,
           f"expected the shortened one-line superseded summary:\n{md}")
    _check("`rec-l-old` superseded by `rec-l-new`" not in md,
           "the old per-id bullet must be gone, not merely supplemented")

    # The legend, against the real store: one line per pcrec testee,
    # never a per-row repetition of the same six facts.
    loaded_r, _p, _s = _load_real_store()
    rd_r, err_r = report.build_report(loaded_r, _args(store=REAL_STORE, subbench="email-specimen"))
    _check(err_r is None, f"unexpected refusal: {err_r}")
    md_r = report.render_markdown(rd_r)
    compiled = md_r.split("### `compiled-aot`")[1].split("### `")[0]
    _check(compiled.count("`pcrec_692c2e8_vm-caps-simdna`: engine=") == 1,
           f"the legend must name each testee's mechanism stamps exactly ONCE, "
           f"not once per (pattern, form) row:\n{compiled[:400]}")
    header_line = next(l for l in compiled.splitlines() if l.startswith("| pattern |"))
    _check("engine" not in header_line and "vm_rungs" not in header_line,
           f"the six per-testee constant columns must be gone from the table header:\n{header_line}")


def test_worst_now_vs_largest_delta_r6():
    """[B14] R6: 'worst subject' used to name the NEW record's slowest
    subject while reading as if it were the subject whose Delta was
    biggest -- not always the same one. Now explicit: `worst now`
    always, `largest Delta` ALSO printed when it names a different
    subject (pcrecdev1 feedback, repin-v2 (2))."""
    setup_old = _mini_setup("pcrec_EEEEEEE_vm-caps-simdna",
                             timestamp="2026-08-25T09:00:00Z", record_id="rec-e-old")
    setup_new = _mini_setup("pcrec_FFFFFFF_vm-caps-simdna",
                             timestamp="2026-08-25T11:00:00Z", record_id="rec-e-new")
    # s1: small Delta (900 -> 910) but the highest absolute ns in the NEW
    # record ("worst now"). s2: tiny old value, huge Delta (10 -> 400),
    # but still smaller in absolute terms than s1 ("largest Delta").
    rows_old = ([_mini_row("p1", "s1", "short-subject-search", t, t, 900) for t in (1, 2, 3)]
                + [_mini_row("p1", "s2", "short-subject-search", t, t + 3, 10) for t in (1, 2, 3)])
    rows_new = ([_mini_row("p1", "s1", "short-subject-search", t, t, 910) for t in (1, 2, 3)]
                + [_mini_row("p1", "s2", "short-subject-search", t, t + 3, 400) for t in (1, 2, 3)])
    loaded = [_mk_loaded("e-old.jsonl", setup_old, rows_old), _mk_loaded("e-new.jsonl", setup_new, rows_new)]
    rd, err = report.build_report(loaded, _args(store="x", include_synthetic=True))
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("worst now: `s1`, 910.0 ns" in md, f"expected s1 named as worst now:\n{md}")
    _check("largest Δ: `s2`, +390.0 ns (now 400.0 ns)" in md,
           f"expected s2 named as the largest Delta, distinct from worst now:\n{md}")

    # Not firing (same subject): reduce to one subject only -- the two
    # facts coincide, and the wording says so in ONE clause.
    rows_old_one = [_mini_row("p1", "s1", "short-subject-search", t, t, 900) for t in (1, 2, 3)]
    rows_new_one = [_mini_row("p1", "s1", "short-subject-search", t, t, 100) for t in (1, 2, 3)]
    loaded_one = [_mk_loaded("e-old1.jsonl", setup_old, rows_old_one),
                  _mk_loaded("e-new1.jsonl", setup_new, rows_new_one)]
    rd1, err1 = report.build_report(loaded_one, _args(store="x", include_synthetic=True))
    _check(err1 is None, f"unexpected refusal: {err1}")
    md1 = report.render_markdown(rd1)
    _check("worst now (also the largest Δ): `s1`" in md1,
           f"one shared subject must collapse to a single combined clause:\n{md1}")
    _check("largest Δ: `s1`, " not in md1, "must not ALSO print the separate largest-Delta clause")


def test_floor_pattern_r9():
    """[B14] R9: schema v1.3's `patterns[].role` (`member` default |
    `floor`, not yet schema-legal). A `role: floor` pattern's own
    short-subject-search table is retitled a control, not a ranking;
    every OTHER (member) pattern's short-subject-search row gains a
    `floor ns` figure beside its per-subject mean. Not firing: the
    existing [B9] `floor: n/a` note stands when no record declares a
    floor pattern at all (covered by `test_near_floor_columns_r6`,
    unaffected by this ruling -- reconfirmed here for the same store)."""
    patterns = [{"pattern_id": "p-mem", "role": "member"},
                {"pattern_id": "p-floor", "role": "floor"}]
    setup = _mini_setup("engine-m_1.0.0_cfg-caps-simdna", patterns=patterns)
    rows = (
        [_mini_row("p-mem", "s1", "short-subject-search", 1, 1, 50)]
        + [_mini_row("p-mem", "s2", "short-subject-search", 1, 2, 70)]
        + [_mini_row("p-floor", "s1", "short-subject-search", 1, 3, 100)]
        + [_mini_row("p-floor", "s2", "short-subject-search", 1, 4, 300)]
    )
    loaded = [_mk_loaded("m.jsonl", setup, rows)]
    rd, err = report.build_report(loaded, _args(store="x", include_synthetic=True))
    _check(err is None, f"unexpected refusal: {err}")
    _check(rd.floor_pattern_by_sb.get("rb-mini@1.0") == "p-floor",
           f"expected the floor pattern recorded for its sb, got {rd.floor_pattern_by_sb}")
    md = report.render_markdown(rd)

    # Anchored on "\n### `" both ends -- both `p-mem` and `p-floor` are
    # 2-subject sets, so R2's tiny-set rule ALSO fires here and each gets
    # its own H4 per-subject sub-table (`#### \`p-mem\`... per-subject`),
    # whose bare heading text contains the bare H3 title as a one-off
    # substring -- see the R2 test's comment for why the bare form is
    # unsafe.
    member = md.split("\n### `p-mem` / `short-subject-search`")[1].split("\n### `")[0]
    _check("floor ns" in member, f"a member pattern must gain the floor ns column:\n{member}")
    # floor SET cell: sum(100, 300) = 400 over 2 subjects -> per-subject mean 200.0
    _check("200.0" in member, f"expected the floor pattern's per-subject mean (200.0):\n{member}")

    floor_section = md.split("\n### `p-floor` / `short-subject-search`")[1].split("\n### `")[0]
    _check("(floor control — per-call overhead, not a ranking of engines)" in floor_section,
           f"the floor pattern's own table must be retitled a control:\n{floor_section[:300]}")
    _check("floor ns" not in floor_section.split("\n")[0],
           "the floor pattern's OWN table does not need a floor column on itself")

    # Not firing: no floor pattern declared at all -- the honest [B9] note.
    setup_plain = _mini_setup("engine-n_1.0.0_cfg-caps-simdna")
    rows_plain = [_mini_row("p1", "s1", "short-subject-search", t, t, 50) for t in (1, 2, 3)]
    loaded_plain = [_mk_loaded("n.jsonl", setup_plain, rows_plain)]
    rd_plain, err_plain = report.build_report(loaded_plain, _args(store="x", include_synthetic=True))
    _check(err_plain is None, f"unexpected refusal: {err_plain}")
    _check(rd_plain.floor_pattern_by_sb == {}, "no floor pattern declared -> empty mapping")
    md_plain = report.render_markdown(rd_plain)
    _check("floor: n/a (no floor pattern in this set yet" in md_plain,
           f"absent a floor pattern, the honest [B9] note must stand unchanged:\n{md_plain}")


def test_reporter_version_pin():
    """THE VERSION-PINNING TEST. Originally `test_reporter_v4_r10` ([B14]
    R10: a version bump whenever rendering changes, so two reports
    produced by different reporter code are never mistaken for each
    other) -- renamed and moved here at [B12] R10 (2026-08-29), because
    the rule is not any one ruling's own: every dated section that
    changes rendering re-bumps `REPORTER_VERSION` and this is the one
    test that pins the CURRENT value, not the ruling that happened to
    land it. History: [B14] took it to v3 then v4 the same day (the KB-2
    correction); [B16]'s R3/R4 changed the rendering of records ALREADY
    IN `store/` -- the 8da6120 legend and the x13.45 cross-pin verdict
    both moved -- so it became v5; [B16] R9 (the per-subject sub-table
    keyed on the regime) took it to v6; [B12] R10 (the did-not-compile
    ranking line, `test_did_not_compile_ranking_line_r10` below) took it
    to v7; [B19]'s scope addition (the abi-11 K=/caps= legend clauses,
    which render differently against records already in the store) took
    it to v8; [B20] (schema v1.4: the trial-agreement legend and the
    per-record `agreement:` line, which render on every existing record)
    took it to v9."""
    _check(report.REPORTER_VERSION == "v9 (2026-08-30)",
           f"expected REPORTER_VERSION == 'v9 (2026-08-30)', got {report.REPORTER_VERSION!r}")
    loaded, _paths, _source = _load_store(STORE)
    rd, err = report.build_report(loaded, _args(store=STORE, include_synthetic=True))
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("reporter: v9 (2026-08-30)" in md, f"expected the v9 header line:\n{md[:200]}")
    tsv = report.render_tsv(rd)
    _check("reporter: v9 (2026-08-30)" in tsv, f"the TSV header must carry it too:\n{tsv[:200]}")


def test_did_not_compile_ranking_line_r10():
    """[B12] R10: a testee whose compile FAILED (`compile_outcome ==
    "did-not-compile"`) must appear under its ranking table as
    `not ranked: <testee> -- did-not-compile (<diagnostic>)`, not merely
    vanish because it produced zero match rows. Found on bench/loglines'
    first sample: `level-context` under `pcrec-auto` did not compile at
    pcrec 35e1ab1 and disappeared from the ranking entirely (it still
    showed in the compile-cost table, which is not where a reader
    checking a RANKING looks).

    Two testees share one pattern/regime group: `engine-c` (did-not-
    compile, no match rows for `p1` at all -- the shape of the real
    loglines cell) and `engine-d` (compiles and measures `p1` cleanly,
    which is what keeps the ranking GROUP itself alive; see the module
    docstring's [B12] R10 section for why a did-not-compile-only group
    with no other testee is a different, unreachable case). The CONTROL
    is `p2`, which both testees compile and measure cleanly -- its
    ranking table must carry no did-not-compile bullet at all."""
    setup_c = _mini_setup("engine-c_1.0.0_cfg-caps-simdna")
    setup_d = _mini_setup("engine-d_1.0.0_cfg-caps-simdna")
    row_dnc_plain = {"kind": "compile", "pattern_id": "p1", "trial": 1, "seq": 1,
                      "compile_outcome": "did-not-compile", "cost_class": "interpretive",
                      "diagnostic": "engine-c: pattern too complex for the DFA engine "
                                    "(>32000 states; try --engine=vm) -- FIXTURE"}
    # p2 compiles cleanly on BOTH testees -- the control.
    row_c_p2_compile = {"kind": "compile", "pattern_id": "p2", "trial": 1, "seq": 2,
                         "compile_outcome": "compiled", "cost_class": "interpretive",
                         "cost": {"total_ns": 1000}}
    rows_c_p2_match = [_mini_row("p2", "s1", "short-subject-search", t, 10 + t, 50) for t in (1, 2, 3)]
    loaded_c = [_mk_loaded("c.jsonl", setup_c, [row_dnc_plain, row_c_p2_compile] + rows_c_p2_match)]

    rows_d_p1_match = [_mini_row("p1", "s1", "short-subject-search", t, 20 + t, 60) for t in (1, 2, 3)]
    row_d_p2_compile = {"kind": "compile", "pattern_id": "p2", "trial": 1, "seq": 2,
                         "compile_outcome": "compiled", "cost_class": "interpretive",
                         "cost": {"total_ns": 1200}}
    rows_d_p2_match = [_mini_row("p2", "s1", "short-subject-search", t, 30 + t, 55) for t in (1, 2, 3)]
    loaded_d = [_mk_loaded("d.jsonl", setup_d, rows_d_p1_match + [row_d_p2_compile] + rows_d_p2_match)]

    rd, err = report.build_report(loaded_c + loaded_d, _args(store="x", include_synthetic=True))
    _check(err is None, f"unexpected refusal: {err}")
    _check(rd.did_not_compile_by_pattern.get(("rb-mini@1.0", "p1")) ==
           {"engine-c_1.0.0_cfg-caps-simdna":
            "engine-c: pattern too complex for the DFA engine (>32000 states; "
            "try --engine=vm) -- FIXTURE"},
           f"expected the did-not-compile diagnostic indexed by (sb, pattern_id): "
           f"{rd.did_not_compile_by_pattern}")

    md = report.render_markdown(rd)
    # Anchored on "\n### `" on BOTH ends, same reason `test_floor_pattern_r9`
    # already documents: `p1` is a <= 3 subject set, so R2's tiny-set rule
    # fires and it gets its own H4 per-subject sub-table
    # (`#### \`p1\` ... per-subject`), whose bare heading text CONTAINS the
    # bare H3 title as a one-off substring once its leading `#` is dropped
    # -- the bare (unanchored) split form is unsafe here.
    p1_section = md.split("\n### `p1` / `short-subject-search`")[1].split("\n### `")[0]
    _check("not ranked: `engine-c_1.0.0_cfg-caps-simdna` — did-not-compile "
           "(engine-c: pattern too complex for the DFA engine (>32000 states; "
           "try --engine=vm) -- FIXTURE)" in p1_section,
           f"expected the did-not-compile ranking line under p1's table:\n{p1_section}")
    _check("`engine-d_1.0.0_cfg-caps-simdna`" in p1_section,
           f"engine-d must still rank normally in the same table:\n{p1_section}")

    # CONTROL: p2 compiled on both testees -- no did-not-compile bullet
    # anywhere near its table.
    p2_section = md.split("\n### `p2` / `short-subject-search`")[1].split("\n### `")[0]
    _check("did-not-compile" not in p2_section,
           f"a cell where both testees compiled must carry no did-not-compile "
           f"bullet:\n{p2_section}")

    tsv = report.render_tsv(rd)
    _check("did_not_compile\tp1\t(set)\tshort-subject-search\t\t\t"
           "engine-c_1.0.0_cfg-caps-simdna\tdid-not-compile" in tsv,
           f"expected a did_not_compile row in the TSV render:\n{tsv}")


def test_floor_pattern_fixture_r9():
    """[B14] R9, PROVEN THROUGH THE SHARED VALIDATOR (lead steer,
    2026-08-25: "a fixture must prove the wired path"). Lane b15floor's
    schema v1.3 (`patterns[].role`) is now on master, so this is no
    longer bypass-only: `fixtures/floor_pattern/` is a REAL, schema-valid
    record (accepted by `schema/validate.py` itself, not a hand-built
    `LoadedRecord`) -- a copy of the existing `fixture-mini` libpcre2
    record with a genuine `role: floor` pattern (`p-floor`, the literal
    `@`, matching bench/email's own floor pattern in spirit) added
    alongside its two `role: member` patterns (stated explicitly, the
    schema default), with real compile/match rows and a recomputed
    `content_hash`. Proves the SAME wiring `test_floor_pattern_r9`
    (bypass technique) already covers, end to end through the real
    loader/validator path this time."""
    fixdir = os.path.join(FIXDIR, "floor_pattern", "store")
    loaded, paths, _source = _load_store(fixdir)
    _check(len(paths) == 1, f"expected exactly 1 record in the floor_pattern fixture, got {paths}")
    _check(not loaded[0].problems,
           f"the floor-pattern fixture must validate cleanly through schema/validate.py: "
           f"{loaded[0].problems}")

    args = _args(store=fixdir, include_synthetic=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    _check(rd.floor_pattern_by_sb.get("fixture-mini@1.0") == "p-floor",
           f"expected the real record's role=floor pattern recognised, got {rd.floor_pattern_by_sb}")

    md = report.render_markdown(rd)
    floor_section = md.split("\n### `p-floor` / `short-subject-search`")[1].split("\n### `")[0]
    _check("(floor control — per-call overhead, not a ranking of engines)" in floor_section,
           f"the real floor-pattern record's own table must be retitled a control:\n{floor_section[:300]}")

    # p-digits and p-word are role=member (stated explicitly) -- each
    # gains a floor ns figure sourced from p-floor's own reduction.
    digits_section = md.split("\n### `p-digits` / `short-subject-search`")[1].split("\n### `")[0]
    _check("floor ns" in digits_section,
           f"a member pattern in a real record with a floor pattern must gain the column:\n{digits_section}")



# --------------------------------------------------------------- [B16] tests

def test_dfa_scan_legend_b16_r1():
    """[B16] R1: the DFA scan's three stamps in the legend, and -- the part
    that matters -- three DIFFERENT absences that a single blank would have
    merged. pcrec I-5's hazard is the rule being enforced: never infer a
    mechanism from a stamp's absence; read the VALUE, and where there is no
    value, say WHICH absence it is."""
    stamped = report._dfa_scan_display({
        "abi": 8, "engine": "dfa", "dfa_scan": "unanchored",
        "dfa_prefilter": "byte-class", "dfa_table": "premultiplied"})
    _check(stamped == "scan=unanchored prefilter=byte-class table=premultiplied",
           f"a stamped DFA row must read all three, got {stamped!r}")

    hybrid = report._dfa_scan_display({
        "abi": 8, "engine": "vm", "prefilter": "hybrid",
        "dfa_scan": "unanchored", "dfa_prefilter": "memchr",
        "dfa_table": "premultiplied"})
    _check("scan=unanchored" in hybrid and "prefilter=memchr" in hybrid,
           f"a VM HYBRID carries the same three stamps ([DD-13c]), got {hybrid!r}")

    # (1) abi >= 6, VM, no pair: rx_info.scan is NULL and that IS "not a
    # hybrid" -- the one reading the spec states as an iff.
    not_hybrid = report._dfa_scan_display({"abi": 8, "engine": "vm",
                                           "prefilter": "none"})
    _check("not a hybrid" in not_hybrid and "rx_info.scan NULL" in not_hybrid,
           f"abi>=6 + VM + no scan pair IS 'not a hybrid', got {not_hybrid!r}")

    # (2) abi 4-5, VM, no pair: hybrids did not stamp yet, so this says
    # NOTHING about whether the artifact has a scan.
    unknowable = report._dfa_scan_display({"abi": 5, "engine": "vm",
                                           "prefilter": "hybrid"})
    _check("says nothing" in unknowable and "abi 6" in unknowable,
           f"abi 4-5 + VM + no pair must refuse to read, got {unknowable!r}")

    # (3) abi < 4: nothing was stamped at all.
    prestamp = report._dfa_scan_display({"abi": 3, "engine": "dfa"})
    _check("before the DFA stamps landed at abi 4" in prestamp,
           f"a pre-abi-4 pin must name itself, got {prestamp!r}")

    # (4) the table alone is younger than the other two -- its own gap, not
    # the whole clause's.
    no_table = report._dfa_scan_display({
        "abi": 6, "engine": "dfa", "dfa_scan": "attempt",
        "dfa_prefilter": "none"})
    _check("scan=attempt" in no_table and "abi 7" in no_table,
           f"abi 6 stamps scan/prefilter but not table, got {no_table!r}")

    # And the three states are DISTINCT strings -- the whole point.
    _check(len({not_hybrid, unknowable, prestamp}) == 3,
           "the three absences must not render identically")


def test_b18_offsets_and_match_form_in_legend():
    """[B18] (pcrec abi 9-11): `dfa_prefilter_offsets` rides on the `dfa:`
    clause and `dfa_match` is its own clause -- BOTH only where the record
    carries the pair, so a record from an older pin renders byte-for-byte
    as before (the control), and a VM hybrid, which carries the offsets
    but NO match form (match_api.md 6.3's two different iffs), shows
    exactly that."""
    uuid = {"abi": 11, "engine": "dfa", "dfa_scan": "unanchored",
            "dfa_prefilter": "offset-set-bounded",
            "dfa_prefilter_offsets": "0,8*,13", "dfa_table": "premultiplied",
            "dfa_match": "unwrapped", "max_emit_bytes": 1000000}
    clause = report._dfa_scan_display(uuid)
    _check(clause.endswith(" offsets=0,8*,13"),
           f"an offset-set artifact's dfa clause names its offsets, got {clause!r}")
    _check(report._match_form_display(uuid) == "unwrapped",
           "a DFA artifact at abi 10+ has a match form")
    line = report._testee_legend_line("pcrec_36d5963_auto-caps-simdna", uuid,
                                      scope="`uuid` plain")
    _check("offsets=0,8*,13" in line and "match=unwrapped, rungs=" in line,
           f"the legend line carries both new clauses, got {line!r}")

    # CONTROL 1: an abi-8 record has neither pair and renders as before.
    old = {"abi": 8, "engine": "dfa", "dfa_scan": "unanchored",
           "dfa_prefilter": "byte-class", "dfa_table": "premultiplied"}
    _check(report._dfa_scan_display(old)
           == "scan=unanchored prefilter=byte-class table=premultiplied",
           "an abi-8 record's dfa clause is unchanged by [B18]")
    _check(report._match_form_display(old) is None,
           "no dfa_match pair -> no clause, never a guess")
    _check("match=" not in report._testee_legend_line("t", old),
           "an abi-8 legend line has no match clause")

    # CONTROL 2: a VM HYBRID carries the offsets (it contains a DFA scan)
    # and NO match form (its _match is the VM's own body).
    hybrid = {"abi": 11, "engine": "vm", "prefilter": "hybrid",
              "dfa_scan": "unanchored", "dfa_prefilter": "memchr",
              "dfa_prefilter_offsets": "none", "dfa_table": "premultiplied",
              "unroll_k": 8, "unroll_k_why": "default"}
    hl = report._testee_legend_line("t", hybrid)
    _check("offsets=none" in hl and "match=" not in hl,
           f"a hybrid: offsets yes, match form no; got {hl!r}")

    # And the column map knows both names (a dropped pair is an absent key).
    cols = report._mechanism_stamp_columns(uuid)
    _check(cols["dfa_prefilter_offsets"] == "0,8*,13"
           and cols["dfa_match"] == "unwrapped",
           "the mechanism columns carry the two new pairs")
    _check(report._mechanism_stamp_columns(old)["dfa_match"] == "-",
           "an absent pair is `-` in the columns, as every other absent pair")


def test_b19_engine_sel_lang_and_emit_bytes():
    """[B19] (pcrec abi 12, pin 96e44c2): the route token and the prefilter
    language ride on the legend line; Frank's ask (b) bucket is DERIVED
    from the record by one rule (`sel not in (selected, forced)` -> `DFA
    fallback tripped`); the two source-bytes pairs become compile-table
    columns -- all ONLY where the record carries the pairs, so an abi-11
    record renders byte for byte as before (the control)."""
    # the [SEL-1] rescue as measured at 96e44c2 on loglines' level-context
    lc = {"abi": 12, "engine": "vm", "prefilter": "hybrid",
          "engine_sel": "collapsed-prefilter",
          "vm_prefilter_lang": "count-collapsed",
          "vm_prefilter_lang_why": "dfa overflow retry, exact nfa 462",
          "dfa_scan": "unanchored", "dfa_prefilter": "byte-class",
          "dfa_prefilter_offsets": "none", "dfa_table": "premultiplied",
          "unroll_k": 8, "unroll_k_why": "default",
          "emit_bytes": 75812, "emit_code_bytes": 33983}
    _check(report._engine_sel_display(lc) == "collapsed-prefilter (DFA fallback tripped)",
           f"a fallback token is bucketed, got {report._engine_sel_display(lc)!r}")
    _check(report._prefilter_lang_display(lc)
           == "count-collapsed (dfa overflow retry, exact nfa 462)",
           f"lang clause carries the why, got {report._prefilter_lang_display(lc)!r}")
    line = report._testee_legend_line("pcrec_96e44c2_auto-caps-simdna", lc,
                                      scope="`level-context` plain")
    _check("engine=vm, sel=collapsed-prefilter (DFA fallback tripped), entry=" in line
           and "vm_prefilter=hybrid, lang=count-collapsed (dfa overflow retry, exact nfa 462), dfa:" in line,
           f"the legend line carries both clauses in place, got {line!r}")

    # `selected` and `forced` are NOT bucketed; the size-cap rescue stamps
    # `selected` (measured), so its only trace is the lang clause.
    forced = {"abi": 12, "engine": "vm", "prefilter": "none", "engine_sel": "forced"}
    fl = report._testee_legend_line("t", forced)
    _check("sel=forced, entry=" in fl and "tripped" not in fl and "lang=" not in fl,
           f"forced: no bucket, no lang clause (not a hybrid); got {fl!r}")
    sizecap = {"abi": 12, "engine": "vm", "prefilter": "hybrid", "engine_sel": "selected",
               "vm_prefilter_lang": "count-collapsed",
               "vm_prefilter_lang_why": "size cap retry, exact 671050 > 500000"}
    sl = report._testee_legend_line("t", sizecap)
    _check("sel=selected (DFA fallback tripped: size-cap rescue), entry=" in sl
           and "lang=count-collapsed (size cap retry, exact 671050 > 500000)" in sl,
           f"the size-cap rescue: sel=selected, bucketed on the why prefix (I-19 (3)); got {sl!r}")
    # CONTROL: a `selected` hybrid whose why is NOT a size-cap retry stays
    # outside the bucket -- the prefix, not the hybrid-ness, is the rule.
    plain_hybrid = dict(sizecap, vm_prefilter_lang="exact",
                        vm_prefilter_lang_why="no counted repeat")
    pl = report._testee_legend_line("t", plain_hybrid)
    _check("sel=selected, entry=" in pl and "tripped" not in pl,
           f"a selected exact hybrid is not bucketed; got {pl!r}")

    # CONTROL: an abi-11 record has none of the pairs and renders as before.
    old = {"abi": 11, "engine": "vm", "prefilter": "none", "unroll_k": 8,
           "unroll_k_why": "default"}
    _check(report._engine_sel_display(old) is None
           and report._prefilter_lang_display(old) is None,
           "no pair -> no clause, never a guess")
    ol = report._testee_legend_line("t", old)
    _check("sel=" not in ol and "lang=" not in ol,
           f"an abi-11 legend line is unchanged by [B19], got {ol!r}")
    _check(report._emit_bytes_display(old) == "-",
           "no emit_bytes pair -> `-`, never a number")
    _check(report._emit_bytes_display(lc) == "75,812"
           and report._emit_bytes_display({"emit_bytes": 724699, "warned_emit_bytes": 724699})
           == "724,699 (warned)",
           "emit bytes render with the warning marker only where pcrec warned")
    cols = report._mechanism_stamp_columns(lc)
    _check(cols["engine_sel"] == "collapsed-prefilter"
           and cols["vm_prefilter_lang"] == "count-collapsed"
           and cols["emit_code_bytes"] == 33983
           and report._mechanism_stamp_columns(old)["engine_sel"] == "-",
           "the column map carries the new pairs, `-` when absent")

    # THE TABLE: the two columns appear when a row carries the pairs, and
    # not otherwise; the legend note appears under a `sel=` line.
    setup = _mini_setup("pcrec_96e44c2_auto-caps-simdna")
    setup["testee"]["engine_name"] = "pcrec"
    row_new = {"kind": "compile", "pattern_id": "p1", "trial": 1, "seq": 1,
               "compile_outcome": "compiled", "cost_class": "compiled-aot",
               "cost": {"total_ns": 1000,
                        "phases": [{"name": "emit-c", "elapsed_ns": 400},
                                   {"name": "gcc", "elapsed_ns": 500},
                                   {"name": "load", "elapsed_ns": 100}]},
               "artifact_bytes": 39448,
               "engine_metadata": dict(lc, warned_emit_bytes=75812)}
    loaded = [_mk_loaded("k.jsonl", setup, [row_new])]
    rd, err = report.build_report(loaded, _args(store="x", include_synthetic=True))
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("| artifact bytes | emit bytes | code bytes |" in md,
           f"the two source-bytes columns follow artifact bytes:\n{md}")
    _check("| 39,448 | 75,812 (warned) | 33,983 |" in md,
           f"the row carries the .so bytes, the warned emit bytes and the code bytes:\n{md}")
    _check("sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced)" in md
           and "bucketed on its why prefix" in md,
           f"the legend note defines the bucket:\n{md}")
    tsv = report.render_tsv(rd)
    for needle in ("\temit_bytes\t75812\t", "\temit_code_bytes\t33983\t",
                   "\twarned_emit_bytes\t75812\t", "\tengine_sel\tcollapsed-prefilter\t",
                   "\tvm_prefilter_lang\tcount-collapsed\t",
                   "\tvm_prefilter_lang_why\tdfa overflow retry, exact nfa 462\t"):
        _check(needle in tsv, f"the TSV carries {needle!r}:\n{tsv}")
    # ... and not otherwise (the control record).
    setup_o = _mini_setup("pcrec_36d5963_auto-caps-simdna")
    row_old = dict(row_new, engine_metadata=old)
    rd_o, err_o = report.build_report([_mk_loaded("o.jsonl", setup_o, [row_old])],
                                      _args(store="x", include_synthetic=True))
    _check(err_o is None, f"unexpected refusal: {err_o}")
    md_o = report.render_markdown(rd_o)
    _check("emit bytes" not in md_o and "sel = pcrec's" not in md_o
           and "| 39,448 |" in md_o,
           f"an abi-11 record's compile table is unchanged by [B19]:\n{md_o}")


def test_b19_size_term_and_caps_in_legend():
    """[B19] scope addition (manager, 2026-08-30): the [ART-SIZE] stamps
    the adapter has recorded on every VM artifact since abi 11 are
    rendered on the legend line -- `K=<unroll_k>/<unroll_k_why>` and
    `caps=<max_emit_code_bytes>/<max_emit_bytes>` -- and a DFA artifact
    shows NEITHER (it has no counter rung; `max_emit_code_bytes` is absent
    from its metadata by design, and its total cap alone is not shown).
    bounded's first sample's K movement (`nest3-16` = K=1 / size-model)
    is the firing case."""
    nest3 = {"abi": 11, "engine": "vm", "prefilter": "hybrid",
             "dfa_scan": "unanchored", "dfa_prefilter": "memchr",
             "dfa_prefilter_offsets": "none", "dfa_table": "premultiplied",
             "unroll_k": 1, "unroll_k_why": "size-model",
             "max_emit_code_bytes": 500000, "max_emit_bytes": 1000000}
    _check(report._size_term_display(nest3) == "1/size-model",
           f"K clause, got {report._size_term_display(nest3)!r}")
    _check(report._caps_display(nest3) == "500,000/1,000,000",
           f"caps clause, got {report._caps_display(nest3)!r}")
    line = report._testee_legend_line("pcrec_36d5963_auto-caps-simdna", nest3,
                                      scope="`nest3-16` plain")
    _check("rungs=-, K=1/size-model, caps=500,000/1,000,000, fast tier=" in line,
           f"both clauses sit on the legend line after rungs, got {line!r}")

    # the default K on an ordinary VM artifact
    plain_vm = {"abi": 11, "engine": "vm", "prefilter": "none",
                "unroll_k": 8, "unroll_k_why": "default",
                "max_emit_code_bytes": 500000, "max_emit_bytes": 1000000}
    _check("K=8/default, caps=500,000/1,000,000" in report._testee_legend_line("t", plain_vm),
           "the default K renders too (a constant is still a fact)")

    # CONTROL 1: a DFA artifact carries max_emit_bytes (both engines) but
    # no unroll_k and no max_emit_code_bytes -> NEITHER clause.
    dfa = {"abi": 11, "engine": "dfa", "dfa_scan": "unanchored",
           "dfa_prefilter": "memchr", "dfa_prefilter_offsets": "none",
           "dfa_table": "premultiplied", "dfa_match": "unwrapped",
           "max_emit_bytes": 1000000}
    _check(report._size_term_display(dfa) is None and report._caps_display(dfa) is None,
           "a DFA artifact has no K and shows no caps")
    dl = report._testee_legend_line("t", dfa)
    _check("K=" not in dl and "caps=" not in dl,
           f"a DFA legend line carries neither clause, got {dl!r}")
    # CONTROL 2: a pre-abi-11 VM record renders as before.
    old = {"abi": 8, "engine": "vm", "prefilter": "none"}
    ol = report._testee_legend_line("t", old)
    _check("K=" not in ol and "caps=" not in ol,
           f"an abi-8 legend line is unchanged, got {ol!r}")

    # THE NOTE: printed under a compile table whose legend carries a K.
    setup = _mini_setup("pcrec_36d5963_auto-caps-simdna")
    row = {"kind": "compile", "pattern_id": "nest3-16", "trial": 1, "seq": 1,
           "compile_outcome": "compiled", "cost_class": "compiled-aot",
           "cost": {"total_ns": 1000,
                    "phases": [{"name": "emit-c", "elapsed_ns": 400},
                               {"name": "gcc", "elapsed_ns": 500},
                               {"name": "load", "elapsed_ns": 100}]},
           "artifact_bytes": 30000, "engine_metadata": nest3}
    rd, err = report.build_report([_mk_loaded("k.jsonl", setup, [row])],
                                  _args(store="x", include_synthetic=True))
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("K=1/size-model, caps=500,000/1,000,000" in md
           and "K = pcrec's `RX_UNROLL_K`/`_WHY`" in md,
           f"the legend line and its note render:\n{md}")
    row_dfa = dict(row, engine_metadata=dfa)
    rd_d, _e = report.build_report([_mk_loaded("d.jsonl", setup, [row_dfa])],
                                   _args(store="x", include_synthetic=True))
    md_d = report.render_markdown(rd_d)
    _check("K=" not in md_d and "K = pcrec's" not in md_d,
           f"a DFA-only table has neither the clause nor the note:\n{md_d}")


def test_fast_tier_legend_b16_r2():
    """[B16] R2: [OPT-1]'s two-tier default entry in the legend, including
    pcrec's ONLY spelling of 'this artifact has one tier' (fast == stamped
    default) and the DFA's 'no tier at all', which is a fact rather than a
    gap."""
    two_tier = report._fast_tier_display({
        "abi": 8, "engine": "vm", "fast_frames": 61, "fast_trail": 92,
        "resume_frames": 2048, "trail_frames": 3072})
    _check(two_tier == "61/92 fast, escalates to 2048/3072",
           f"expected the boundary and what it escalates to, got {two_tier!r}")

    single = report._fast_tier_display({
        "abi": 8, "engine": "vm", "fast_frames": 1, "fast_trail": 3,
        "resume_frames": 1, "trail_frames": 3})
    _check("single tier" in single and "==" in single,
           f"fast == stamped default IS 'one tier' (match_api.md 6.3), got {single!r}")

    dfa = report._fast_tier_display({"abi": 8, "engine": "dfa",
                                     "resume_frames": 0, "trail_frames": 0})
    _check(dfa == "n/a (DFA: no tier)",
           f"a DFA artifact has no tier -- a fact, not a gap; got {dfa!r}")

    old = report._fast_tier_display({"abi": 3, "engine": "vm"})
    _check("no tier existed before abi 5" in old,
           f"a pre-abi-5 pin must name itself, got {old!r}")


def test_engine_reading_and_scoped_legend_b16_r3():
    """[B16] R3 (pcrec I-7 §3 (a)): a STAMPED engine is a reading; an
    unstamped one is announced as an inference; an unstamped `auto` config
    yields `unknown`, because --engine=auto selects per PATTERN. And the
    legend is scoped per (pattern, form) exactly when a testee's cells
    disagree -- the fault this ruling corrects."""
    display, stamped = report._engine_reading(
        "pcrec_35e1ab1_auto-caps-simdna", {"abi": 8, "engine": "dfa"})
    _check((display, stamped) == ("dfa", "dfa"),
           f"a stamped engine is the value itself, got {display!r}")

    display, stamped = report._engine_reading(
        "pcrec_8da6120_auto-caps-simdna", {})
    _check(stamped is None and "unknown" in display and "per PATTERN" in display,
           f"an unstamped `auto` config cannot name an engine, got {display!r}")

    display, stamped = report._engine_reading(
        "pcrec_8da6120_vm-caps-simdna", {})
    _check(stamped is None and display.startswith("vm — inferred (unstamped pin"),
           f"an unstamped `vm` config is an INFERENCE and says so, got {display!r}")

    # The scoping, against the real store: 8da6120's `auto` testee compiled
    # `orig` to a DFA artifact and `factored` to a VM one AT ONE PIN, which
    # is what a per-testee legend line could not say.
    loaded, _paths, _source = _load_real_store()
    rd, err = report.build_report(loaded, _args(store=REAL_STORE,
                                                subbench="email-specimen"))
    _check(err is None, f"unexpected refusal: {err}")
    compiled = report.render_markdown(rd).split("### `compiled-aot`")[1].split("### `")[0]
    scoped = [ln for ln in compiled.splitlines()
              if ln.startswith("- `pcrec_8da6120_auto-caps-simdna` / ")]
    _check(len(scoped) >= 2,
           f"a testee whose cells disagree must get one line per cell:\n{compiled[:2000]}")
    engines = {("dfa" if "engine=dfa" in ln else "vm" if "engine=vm" in ln else "?")
               for ln in scoped}
    _check(engines == {"dfa", "vm"},
           f"the split must SHOW both engines at that pin, got {engines}:\n"
           + "\n".join(scoped))
    # ...and a testee whose cells agree is still ONE line.
    collapsed = [ln for ln in compiled.splitlines()
                 if ln.startswith("- `pcrec_692c2e8_vm-caps-simdna`")]
    _check(len(collapsed) == 1 and " / " not in collapsed[0].split(": ")[0],
           f"an agreeing testee must stay collapsed to one unscoped line:\n{collapsed}")


def test_giveup_names_engine_and_selection_changed_b16_r4():
    """[B16] R4 (pcrec I-7 §3 (a)): a give-up code names an engine, and a
    cross-pin Δ between two different engines prints `selection changed`
    instead of faster/slower ×N.

    Built as the real case was: an OLD pin whose rows gave up with
    `-2:PCREC_ERR_STEPS` (a code only the VM can produce -- a DFA artifact
    stamps -1 for every budget) and a NEW pin that measures. Without the
    rule the two would compare as one engine getting faster."""
    _check(report._GIVEUP_NAMES_ENGINE["PCREC_ERR_STEPS"] == "vm",
           "PCREC_ERR_STEPS is a VM-only code (a DFA artifact has no step budget)")

    args = _args(store="x", include_synthetic=True)
    old_tid, new_tid = ("pcrec_AAAAAAA_auto-caps-simdna",
                        "pcrec_BBBBBBB_auto-caps-simdna")
    setup_old = _mini_setup(old_tid, timestamp="2026-08-25T09:00:00Z",
                            record_id="rec-b16-old")
    setup_new = _mini_setup(new_tid, timestamp="2026-08-25T11:00:00Z",
                            record_id="rec-b16-new")
    gave_up = {"kind": "match", "pattern_id": "p1", "subject_id": "s1",
               "regime": "short-subject-search", "trial": 1, "seq": 1,
               "match_outcome": "gave-up",
               "diagnostic": "giveup:-2:PCREC_ERR_STEPS"}
    # The NEW pin stamps its engine; the OLD one does not, so the give-up
    # code is the only witness of what answered there.
    compile_new = {"kind": "compile", "pattern_id": "p1", "trial": 1, "seq": 9,
                   "cost_class": "compiled-aot", "compile_outcome": "compiled",
                   "cost": {"total_ns": 130_000_000,
                            "phases": [{"name": "gcc",
                                        "elapsed_ns": 130_000_000}]},
                   "engine_metadata": {"abi": 8, "engine": "dfa",
                                       "dfa_scan": "unanchored",
                                       "dfa_prefilter": "byte-class",
                                       "dfa_table": "premultiplied"}}
    rows_new = [_mini_row("p1", "s1", "short-subject-search", t, t, 40)
                for t in (1, 2, 3)] + [compile_new]
    loaded = [_mk_loaded("old.jsonl", setup_old, [gave_up]),
              _mk_loaded("new.jsonl", setup_new, rows_new)]
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    _check(report._giveup_engines_for(rd, "rb-mini@1.0", old_tid, "p1", "plain")
           == {"vm"},
           "the old pin's give-up code must be read as naming the VM")
    md = report.render_markdown(rd)
    _check("selection changed" in md,
           f"a cross-pin pair of two different engines must read 'selection "
           f"changed', not faster/slower:\n{md}")
    # The selection change EXPLAINS a "now measured", so both are printed;
    # what it REPLACES is the faster/slower RATIO, which is the statement
    # two different engines make meaningless.
    _check("selection changed" in md and "now measured (was: gave-up)" in md,
           f"a selection change explains a 'now measured' rather than "
           f"hiding it:\n{md}")
    _check("faster ×" not in md and "slower ×" not in md,
           f"no faster/slower ratio may be printed across two engines:\n{md}")


def test_gcc_band_witness_b16_r5():
    """[B16] R5 (pcrec I-7 §3 (b)): the gcc-phase cost band as an
    INDEPENDENT witness of the engine on an unstamped pin -- and the two
    limits on it, which are the ruling as much as the bands are: it never
    fills the engine field, and it abstains rather than guessing."""
    _check(report._gcc_band_witness(130_000_000) == "dfa",
           "124-140 ms is the measured DFA band (pcrec I-7 §4)")
    _check(report._gcc_band_witness(470_000_000) == "vm",
           "400-540 ms is the measured VM band (pcrec I-7 §4)")
    _check(report._gcc_band_witness(230_000_000) is None,
           "between the bands the witness must ABSTAIN, not pick the nearer")
    _check(report._gcc_band_witness(None) is None, "no gcc phase -> no witness")

    # On an unstamped row the legend prints it AS a witness, and the engine
    # field still says the reading is an inference.
    line = report._testee_legend_line("pcrec_8da6120_vm-caps-simdna", {},
                                      gcc_median_ns=470_000_000,
                                      giveup_engines={"vm"})
    _check("inferred (unstamped pin" in line,
           f"the engine field must stay an inference, got:\n{line}")
    _check("witnesses (independent of any stamp" in line
           and "vm band" in line and "give-up code(s) name vm" in line,
           f"both witnesses must be printed as witnesses:\n{line}")

    # On a STAMPED row there is nothing to witness and no witness line.
    stamped_line = report._testee_legend_line(
        "pcrec_35e1ab1_vm-caps-simdna",
        {"abi": 8, "engine": "vm", "prefilter": "none"},
        gcc_median_ns=470_000_000, giveup_engines={"vm"})
    _check("witnesses" not in stamped_line,
           f"a stamped engine needs no witness:\n{stamped_line}")


def test_max_is_trial_one_b16_r6():
    """[B16] R6 (pcrec I-7 §5): 'max is trial 1' beside the jitter ratio --
    the fact that separates a warm-up from noise, which the ratio alone
    cannot. A FACT, not a verdict, and `None` when unanswerable."""
    def rows(*pairs):
        return [{"compile_outcome": "compiled", "trial": t,
                 "cost": {"total_ns": ns}} for t, ns in pairs]

    _check(report._max_is_first_trial(rows((1, 900), (2, 100), (3, 110))) is True,
           "a first-trial warm-up must be reported")
    _check(report._max_is_first_trial(rows((1, 100), (2, 900), (3, 110))) is False,
           "a max in the middle is not a first-trial warm-up")
    _check(report._max_is_first_trial(rows((1, 100))) is None,
           "one trial cannot answer the question")
    _check(report._max_is_first_trial(
        [{"compile_outcome": "compiled", "cost": {"total_ns": 1}},
         {"compile_outcome": "compiled", "cost": {"total_ns": 2}}]) is None,
        "rows with no `trial` number cannot be ordered -> None, not a default")

    # And it reaches the rendered jitter cell.
    args = _args(store="x", include_synthetic=True)
    setup = _mini_setup("pcrec_CCCCCCC_auto-caps-simdna")
    compile_rows = [
        {"kind": "compile", "pattern_id": "p1", "trial": t, "seq": 10 + t,
         "cost_class": "compiled-aot", "compile_outcome": "compiled",
         "cost": {"total_ns": ns},
         "engine_metadata": {"abi": 8, "engine": "dfa"}}
        for t, ns in ((1, 400_000_000), (2, 100_000_000), (3, 101_000_000))]
    loaded = [_mk_loaded("c.jsonl", setup,
                          [_mini_row("p1", "s1", "short-subject-search", t, t, 40)
                           for t in (1, 2, 3)] + compile_rows)]
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("(max is trial 1)" in md,
           f"the jitter cell must carry the fact:\n{md}")


def test_dominated_set_ratio_b16_r7():
    """[B16] R7 (pcrec I-7 §5): a SET-grain ratio that is really one
    subject says so, and points at the per-subject rows.

    The measured case it comes from: pcre2-interp's throughput set total is
    99.9 % one subject, so its '3.15x slower than JIT' was 7.7x slower on
    that subject and 144x FASTER on the other two."""
    args = _args(store="x", include_synthetic=True)
    setup = _mini_setup("engine-d_1.0.0_cfg-caps-simdna")
    rows = []
    seq = 0
    for sid, ns in (("s1", 100_000), ("s2", 50), ("s3", 50)):
        for t in (1, 2, 3):
            seq += 1
            rows.append(_mini_row("p1", sid, "large-subject-throughput",
                                  t, seq, ns))
    loaded = [_mk_loaded("d.jsonl", setup, rows)]
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"unexpected refusal: {err}")
    dom = report._dominant_subject(rd, "rb-mini@1.0",
                                   "engine-d_1.0.0_cfg-caps-simdna",
                                   "p1", "large-subject-throughput", "plain")
    _check(dom is not None and dom[0] == "s1" and dom[1] > 0.99,
           f"s1 is 99.9 % of this set and must be flagged, got {dom!r}")
    md = report.render_markdown(rd)
    _check("**dominated**: `s1`" in md and "set composition" in md,
           f"the ranking row must carry the flag:\n{md}")
    _check("per-subject rows below" in md,
           f"the note must point at the other reading:\n{md}")

    # An evenly-spread set is NOT flagged -- the control that keeps the
    # flag meaningful.
    setup_even = _mini_setup("engine-e_1.0.0_cfg-caps-simdna")
    rows_even = []
    seq = 0
    for sid in ("s1", "s2", "s3"):
        for t in (1, 2, 3):
            seq += 1
            rows_even.append(_mini_row("p1", sid, "large-subject-throughput",
                                       t, seq, 1000))
    rd_even, err_even = report.build_report(
        [_mk_loaded("e.jsonl", setup_even, rows_even)], args)
    _check(err_even is None, f"unexpected refusal: {err_even}")
    _check(report._dominant_subject(rd_even, "rb-mini@1.0",
                                     "engine-e_1.0.0_cfg-caps-simdna", "p1",
                                     "large-subject-throughput", "plain") is None,
           "an evenly-spread set must NOT be flagged")



def test_per_subject_subtable_b16_r9():
    """[B16] R9: the per-subject sub-table's condition is a property of the
    CELL, not one sub-bench's subject count.

    THE REGRESSION THIS EXISTS FOR, first, as a real five-subject
    throughput cell: [B14] R2 keyed the sub-table on `<= 3 subjects` with
    the comment "today, every large-subject-throughput cell". [B17] added
    two non-periodic prose subjects to bench/email's throughput sweep
    (email-specimen@0.2, pcrec I-10), and that cell would have SILENTLY
    lost its per-subject rows -- in the one regime where those rows ARE
    the finding (pcrec I-7 §1: the set-grain sums hid that pcre2-interp is
    144x FASTER than JIT on two of the three subjects it is "3.15x slower"
    than JIT over)."""
    args = _args(store="x", include_synthetic=True)
    setup = _mini_setup("engine-f_1.0.0_cfg-caps-simdna")
    rows, seq = [], 0
    for sid in ("t-1", "t-2", "t-3", "t-4", "t-5"):
        for t in (1, 2, 3):
            seq += 1
            rows.append(_mini_row("p1", sid, "large-subject-throughput",
                                  t, seq, 1000))
    rd, err = report.build_report([_mk_loaded("f.jsonl", setup, rows)], args)
    _check(err is None, f"unexpected refusal: {err}")
    md = report.render_markdown(rd)
    _check("per-subject" in md and "`t-5`" in md,
           f"a FIVE-subject throughput cell must still get its per-subject "
           f"rows -- this is the [B17] regression:\n{md}")

    # The decision function itself, condition by condition.
    show, skip = report._per_subject_subtable("large-subject-throughput", 5,
                                              False, "set")
    _check(show and skip is None, "throughput at 5 subjects: shown")
    show, _skip = report._per_subject_subtable("large-subject-throughput", 12,
                                               False, "set")
    _check(show, "throughput at 12 (bench/loglines' sweep): shown")
    show, _skip = report._per_subject_subtable("match-compliance", 3, False,
                                               "set")
    _check(show, "[B14] R2's own case -- any regime, <= 3 subjects: shown")
    show, _skip = report._per_subject_subtable("match-compliance", 20, True,
                                               "set")
    _check(show, "a DOMINATED cell: shown, so R7's pointer does not dangle")
    show, skip = report._per_subject_subtable("match-compliance", 20, False,
                                              "set")
    _check(not show and skip is None,
           "20 ordinary compliance subjects: no sub-table and nothing to say")

    # The CAP, and the honesty rule about a fact not shown: an 85-subject
    # (bench/email) or 112-subject (bench/loglines) compliance set is not
    # made readable by printing every row of it.
    show, skip = report._per_subject_subtable("match-compliance", 85, True,
                                              "set")
    _check(not show and skip and "85 subjects" in skip
           and "--grain subject" in skip,
           f"above the cap the row must NAME the count and point at "
           f"--grain subject, not fall silent; got {skip!r}")
    show, skip = report._per_subject_subtable("large-subject-throughput", 112,
                                              False, "set")
    _check(not show and skip, "the cap binds in the throughput regime too")
    show, _skip = report._per_subject_subtable("large-subject-throughput", 5,
                                               False, "subject")
    _check(not show, "subject grain IS the per-subject view; no sub-table")
    show, _skip = report._per_subject_subtable("large-subject-throughput", 0,
                                               False, "set")
    _check(not show, "no subjects, no sub-table")

    # ...and the cap is not one sub-bench's subject count, which is the
    # coupling this ruling removes.
    _check(report._SUBTABLE_MAX_SUBJECTS > 12,
           "the cap must clear bench/loglines' 12-subject throughput sweep")
    _check(report._SUBTABLE_MAX_SUBJECTS < 85,
           "the cap must NOT admit a compliance set")

    # R7's note points where the rows actually ARE. A dominated cell over
    # the cap says `--grain subject`; one under it says "below".
    setup_d = _mini_setup("engine-g_1.0.0_cfg-caps-simdna")
    rows_d, seq = [], 0
    for sid, ns in (("d-1", 100_000), ("d-2", 50), ("d-3", 50)):
        for t in (1, 2, 3):
            seq += 1
            rows_d.append(_mini_row("p1", sid, "large-subject-throughput",
                                    t, seq, ns))
    rd_d, err_d = report.build_report([_mk_loaded("g.jsonl", setup_d, rows_d)],
                                       args)
    _check(err_d is None, f"unexpected refusal: {err_d}")
    md_d = report.render_markdown(rd_d)
    _check("**dominated**" in md_d and "the per-subject rows below" in md_d,
           f"a dominated cell WITH a sub-table must say 'below':\n{md_d}")


# --------------------------------------------------- [B20] schema v1.4 (v9)

def test_trial_agreement_legend_and_na_v13():
    """[B20] R3/R4 over the NEW valid 1.3 + 1.4 pair (`--all-records`, so
    both halves of one cell are included): the legend line prints once;
    the 1.3 record shows `agreement: n/a (v1.3)` (never re-judged, never
    invented); the 1.4 record shows its block's numbers; both reduce in
    one invocation. CONTROL: `test_mixed_schema_versions_refused` (the
    MAJOR pair) is still refused."""
    loaded, _p, _s = _load_store(V14_PAIR)
    args = _args(store=V14_PAIR, include_synthetic=True, all_records=True)
    rd, err = report.build_report(loaded, args)
    _check(err is None, f"a 1.3 + 1.4 pair must NOT be refused: {err}")
    md = report.render_markdown(rd)
    _check(md.count("- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33):") == 1,
           "the legend line must print exactly once")
    _check(f"`{V13_RID}`" in md and " — agreement: n/a (v1.3)" in md,
           f"the 1.3 record must show agreement n/a (v1.3):\n{md[:2000]}")
    # (the measured 1.4 half carries ONE disagreeing row -- s-num-2's trials
    # [50, 90, 160, 51, 49.5] have two above 1.5 x their median -- and is
    # still `agree`: d = 1 < d_min, one row is not a disturbed group, R-16)
    _check("agreement: agree (0 of 4 groups; 1 of 5 rows; 0 unjudged; k=1.5, 2/3; 5 trials)" in md,
           f"the 1.4 record must show its block's numbers:\n{md[:2000]}")
    _check("agreement: disagree (1 of 4 groups; worst p-digits / match-compliance / plain "
           "d=2 of n=2; 0 unjudged)" in md,
           f"the spread record must show its block's numbers:\n{md[:2500]}")
    testees = {k[1] for k in rd.set_cells}
    _check(any(t.endswith("@20260825T120000Z") for t in testees)
           and any(t.endswith("@20260825T120500Z") for t in testees),
           f"both halves of the pair must reduce in one invocation: {testees}")
    _check(rd.agreement_by_record[V13_RID] is None
           and rd.agreement_by_record[V14_RID]["verdict"] == "agree",
           "the block is threaded per record, None for the 1.3 half")


def test_rule_marker_on_mixed_x13_versions():
    """[B20] R4' (record_schema.md 4's rule-revision clause, R-1 (iii)):
    when one query mixes X13 versions every ranking row's status cell
    carries the record's schema version and the legend names both rules;
    CONTROL: the single-version default query (the 1.3 half deduped away
    under the newer measured 1.4 record) carries no suffix."""
    loaded, _p, _s = _load_store(V14_PAIR)
    rd, err = report.build_report(loaded, _args(store=V14_PAIR, include_synthetic=True,
                                                 all_records=True))
    _check(err is None, err)
    _check(rd.mixed_x13, f"--all-records over the pair must mix X13 versions: {rd.x13_rule_counts}")
    md = report.render_markdown(rd)
    _check("| measured@1.3 |" in md and "| measured@1.4 |" in md,
           f"mixed rows must carry the version marker:\n{md}")
    _check("- status rule: v1.1-1.3 X13 (both samples quiet) on 1 record(s); "
           "v1.4 X13 (pre-flight + trial agreement) on 2 record(s) — MIXED" in md,
           f"the legend must name both rules:\n{md[:3000]}")
    tsv = report.render_tsv(rd)
    _check("\tmeasured@1.3\t" in tsv and "\tmeasured@1.4\t" in tsv and "mixed_x13: True" in tsv,
           "the TSV rows carry the marker too")
    rd1, _e = report.build_report(loaded, _args(store=V14_PAIR, include_synthetic=True))
    _check(not rd1.mixed_x13, f"the default query is single-version: {rd1.x13_rule_counts}")
    md1 = report.render_markdown(rd1)
    _check("measured@" not in md1 and "| measured |" in md1,
           "a single-version query's rows carry no suffix")
    _check("- status rule: v1.4 X13 (pre-flight + trial agreement) on 2 record(s)" in md1
           and "MIXED" not in md1, f"the single-version legend names one rule:\n{md1[:3000]}")


_V9_ALLOWED_ADDED = (
    "- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33):",
    "- status rule: ",
)


def _classify_v9_diff(golden_text, new_text):
    """[B20] `test_v13_record_still_renders`'s classifier: every line that
    differs between the committed v8 rendering and the v9 one must be (a)
    the version line, (b) an R3/R4' legend line, (c) a record line that
    only GAINED ` — agreement: n/a (v1.x)` and/or an `; after: ...`
    clause. Returns the list of UNEXPLAINED differing lines."""
    import difflib
    old_lines = golden_text.splitlines()
    new_lines = new_text.splitlines()
    unexplained = []
    sm = difflib.SequenceMatcher(a=old_lines, b=new_lines, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        removed, added = old_lines[i1:i2], new_lines[j1:j2]
        for line in added:
            if line.startswith("reporter: v9 "):
                continue
            if any(line.startswith(a) for a in _V9_ALLOWED_ADDED):
                continue
            m = re.match(r"^(    - `[^`]+` \([^)]*\)) — agreement: n/a \(v1\.\d\)(; after: .*)?$", line)
            if m and m.group(1) in removed:
                continue
            unexplained.append("+ " + line)
        for line in removed:
            if line.startswith("reporter: v8 "):
                continue
            if re.match(r"^    - `[^`]+` \([^)]*\)$", line) and any(
                    a.startswith(line + " — agreement: n/a") for a in added):
                continue
            unexplained.append("- " + line)
    return unexplained


def test_v13_record_still_renders():
    """[B20] (panel C F13): the existing fixture store (schema 1.1, judged by
    the pre-1.4 X13) still renders under v9, and the ONLY lines that differ
    from the committed v8 rendering (`fixtures/golden/store_v8.md`) are the
    version line, the R3/R4' legend lines and the per-record `agreement:
    n/a (v1.1)` suffix -- no number, no ranking, no other line. CONTROL: the
    same diff with ONE number changed in the v9 rendering is refused."""
    with open(GOLDEN_V8, encoding="utf-8") as fh:
        golden = fh.read()
    loaded, paths, source = _load_store(STORE)
    args = _args(store=STORE, include_synthetic=True)
    args._source_desc = f"{source} ({len(paths)} candidate file(s))"   # as the CLI says it
    rd, err = report.build_report(loaded, args)
    _check(err is None, err)
    md = report.render_markdown(rd)
    unexplained = _classify_v9_diff(golden, md)
    _check(not unexplained, "v9 changed more than the legend and the agreement "
                            "suffix against the v8 golden:\n" + "\n".join(unexplained))
    _check(md != golden, "the v9 rendering must differ from v8 at all (the legend)")
    # the CONTROL: one number changed => the classifier refuses
    mutated = md.replace("| 20.0 | 19.0 | 21.0 |", "| 20.5 | 19.0 | 21.0 |", 1)
    _check(mutated != md, "the control's target number must exist in the rendering")
    _check(_classify_v9_diff(golden, mutated),
           "the classifier must refuse a rendering with a number changed")


def test_provenance_flag():
    """[B20] R5: the after-sample provenance sentence(s) appear under a
    record's header line ONLY under --include-provenance, from wherever
    they sit (`status_detail` on the spread record, `note` on a measured
    one); the default rendering of the same store lacks them."""
    loaded, _p, _s = _load_store(V14_PAIR)
    rd, err = report.build_report(loaded, _args(store=V14_PAIR, include_synthetic=True))
    _check(err is None, err)
    md = report.render_markdown(rd)
    _check("provenance: after-sample (provenance, not a verdict)" not in md,
           "the provenance sentence must be OFF by default")
    rdp, _e = report.build_report(loaded, _args(store=V14_PAIR, include_synthetic=True,
                                                 include_provenance=True))
    mdp = report.render_markdown(rdp)
    _check("        - provenance: after-sample (provenance, not a verdict): occupancy after "
           "the run 41.41% busy" in mdp
           and "        - provenance: after-sample (provenance, not a verdict): load1 after "
           "the run 11.40 exceeds the limit 6.00" in mdp,
           f"--include-provenance must print both after-sample sentences:\n{mdp[:3000]}")
    _check("[ACTIVE]" in mdp.split("trial-agreement policy")[1].split("\n")[0],
           "the legend must flag the flag as active")


def test_after_clause_unconditional():
    """[B20] R5': when either AFTER sample failed the record's header line
    carries `after: load1 11.40 / occ 41.41%` WITHOUT any flag; CONTROL: the
    record whose after samples are clean carries no such clause."""
    loaded, _p, _s = _load_store(V14_PAIR)
    rd, err = report.build_report(loaded, _args(store=V14_PAIR, include_synthetic=True))
    _check(err is None, err)
    md = report.render_markdown(rd)
    spread_line = next(l for l in md.splitlines() if f"`{SPREAD_RID}`" in l)
    clean_line = next(l for l in md.splitlines() if f"`{V14_RID}`" in l)
    _check(spread_line.endswith("; after: load1 11.40 / occ 41.41%"),
           f"the failed-after record must carry the clause: {spread_line}")
    _check("after:" not in clean_line,
           f"a record with clean after samples must carry no clause: {clean_line}")
    tsv = report.render_tsv(rd)
    _check(f"record\t\t\t\t\t\t{SPREAD_RID}\t\t\t\tagreement\t" in tsv
           and "after: load1 11.40 / occ 41.41%" in tsv,
           "the TSV carries a `record` row per record with the agreement and the clause")


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
    test_duplicate_record_dedup_prefers_measured_r2,
    test_scratch_tier_gate_r3,
    test_form_fact_and_mixed_regime_note_r4,
    test_two_ratio_columns_r5,
    test_near_floor_columns_r6,
    test_gave_up_cell_summary_r7,
    test_cross_pin_delta_r8,
    test_mechanism_stamp_columns_r9,
    test_subbench_dir_alias_od_b13,
    # [B14]
    test_plain_entry_capacities_r1,
    test_tiny_set_per_subject_subtable_r2,
    test_matching_subject_count_r3,
    test_buffer_frame_legend_r4,
    test_jitter_ratio_r5,
    test_worst_now_vs_largest_delta_r6,
    test_artifact_bytes_column_r7,
    test_legend_and_superseded_shortening_r8,
    test_floor_pattern_r9,
    test_floor_pattern_fixture_r9,
    test_reporter_version_pin,
    # [B16]
    test_dfa_scan_legend_b16_r1,
    test_b18_offsets_and_match_form_in_legend,
    test_b19_engine_sel_lang_and_emit_bytes,
    test_b19_size_term_and_caps_in_legend,
    test_fast_tier_legend_b16_r2,
    test_engine_reading_and_scoped_legend_b16_r3,
    test_giveup_names_engine_and_selection_changed_b16_r4,
    test_gcc_band_witness_b16_r5,
    test_max_is_trial_one_b16_r6,
    test_dominated_set_ratio_b16_r7,
    test_per_subject_subtable_b16_r9,
    # [B12]
    test_did_not_compile_ranking_line_r10,
    # [B20] schema v1.4 (v9)
    test_trial_agreement_legend_and_na_v13,
    test_rule_marker_on_mixed_x13_versions,
    test_v13_record_still_renders,
    test_provenance_flag,
    test_after_clause_unconditional,
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
