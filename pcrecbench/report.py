#!/usr/bin/env python3
"""pcrecbench.report -- the reporter MVP ([B5]).

Answers a QUERY over the record store (docs/design/requirements.md 8,
docs/design/harness_contract.md 5): loads `store/index.tsv` (falling back to
walking `store/records/` when the index is absent -- it says which it did),
validates every candidate record with the SHARED validator
(schema/validate.py, requirements 6: "a tiny validator the reporter
shares"), applies filters over setup-layer fields, reduces raw trials per
(pattern, subject-or-subject-set, regime, testee) cell to comparables, and
renders a self-describing report in markdown (default) or TSV.

It never runs an engine (harness_contract.md 5: "it never runs an engine")
-- it only reads records that already exist, real or synthetic.

Design decisions this module makes that the contract leaves to [B5]
(stated here, and repeated in the final hand-off message):

* The per-trial COMPARABLE for a match cell is `elapsed_ns / iterations`
  (nanoseconds per call), not raw `elapsed_ns`. Two testees calibrate
  `iterations` independently (harness_contract 3: "iters chosen so one
  subject's loop is >= 50 ms"), so raw elapsed_ns is not comparable across
  testees; per-call time is. `iters` is carried alongside the reduction for
  transparency, per the brief's comparable set (median, min, max, stddev,
  n trials, iters).
* Ranking has two grains, `--grain set` (default) and `--grain subject`
  (manager, 2026-08-25, accepted as a change request on the original
  (pattern, subject, regime) MVP grain below). `set` reduces over the
  whole SUBJECT SET per (pattern, regime): per trial, sum the per-subject
  ns/call over every subject in the set (time to process the set once
  per call-set), then median/min/max/stddev over trials; a set cell is
  excluded from ranking if ANY subject in it fails its own expectation
  check (listed with its failing subjects, not folded into an average).
  `subject` gives the finer (pattern, subject, regime) tables this module
  used before the change request -- the drill-down once a set cell looks
  wrong. Regimes with exactly one subject per pattern (typically
  large-subject-throughput) are identical at both grains; the header
  says so when it applies.
* `synthetic: true` records are excluded by default (schema/examples/
  CLAUDE.md: "the reporter excludes such records from every query"); the
  `--include-synthetic` flag overrides this. It exists because every
  fixture record this reporter is tested against is necessarily
  synthetic (no engine is ever run here) -- without the override there
  would be no way to demonstrate the reporter against its own test store.
* The mixed-schema-version refusal (requirements 6, schema/record_schema.md
  4) is evaluated on the record's OWN DECLARED `schema_version`, peeked
  directly, independent of whether the shared validator can otherwise read
  that version -- so a report spanning a readable 1.0 record and an
  unreadable-future 2.0 record is refused for BEING MIXED, not silently
  reduced to "one invalid record dropped, one record reported".
* A lazy-JIT compile row carries no number (record_schema.md 8: "cost is
  FORBIDDEN"); its cost is derived here as `first-match-row-minus-steady-
  state` (schema v1.1's token; record_schema.md 8): the pattern's
  GLOBALLY-FIRST timed match row in the record -- lowest `seq`, across
  every subject/regime, NOT `trial == 1` of any one cell, since a
  pattern measured over many subjects has many `trial: 1` rows and only
  the very first one (by emission order) paid the JIT -- minus the
  median ns/call of every OTHER timed row for that pattern. ONE derived
  value per (pattern, testee), reduced like any other compile-cost class
  but never pooled with an AOT or interpreter class's `cost.total_ns`
  numbers (requirements 3). Superseded a schema-1.0-era version of this
  function that (wrongly, absent `seq`) derived one value per (subject,
  regime) sub-cell keyed on `trial == 1`; see `_lazy_jit_derivation`'s
  docstring. Not exercised by an end-to-end fixture record (none of this
  lane's testees are `lazy-jit`), so it is unit-tested directly against
  hand-built row dicts instead -- see
  `test_lazy_jit_derivation_uses_lowest_seq_not_trial_one`.
* `form` (`plain` / `whole-subject`, schema v1.1, record_schema.md 5
  ADDITIONS 3) is part of every match- and compile-cell key here (a
  testee with no end-anchored mode, like pcrec, compiles and times a
  SEPARATE artifact for the match-compliance regime, and the two must
  never share a row or a reduction). Shown as its own column beside the
  numbers, but only in tables where more than `plain` actually appears
  in the selected records -- when everything is `plain` (the common
  case) the column is omitted rather than clutter every report with a
  constant.
* `match_outcome = gave-up` (schema v1.1) means the engine exhausted its
  OWN resource limit and said so -- it is not a wrong answer and not a
  crash, and lumping its count into "wrong answers" would bury the
  bench's own headline finding (record_schema.md 5 ADDITIONS 2). Every
  outcome-counting surface here (`MatchCellReduction.n_gave_up` /
  `.n_wrong`, `SetCellReduction`'s aggregates, the excluded-cells
  tables) keeps `gave-up` a separate tally from
  `did-not-match-as-expected` / `wrong-span-or-captures` /
  `truncated-subject`.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import statistics
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
SCHEMA_DIR = os.path.join(REPO_ROOT, "schema")

_MISSING = object()


# --------------------------------------------------------------------- the
# shared validator (schema/validate.py) -- loaded dynamically since schema/
# is not a python package and this reporter must not fork its own copy of
# the rules it enforces (requirements 6: "a tiny validator the reporter
# shares").

_validator_module = None


def _load_validator_module():
    global _validator_module
    if _validator_module is not None:
        return _validator_module
    vpath = os.path.join(SCHEMA_DIR, "validate.py")
    spec = importlib.util.spec_from_file_location("pcrecbench._schema_validate", vpath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    _validator_module = mod
    return mod


def _get_record_validator():
    mod = _load_validator_module()
    with open(mod.SCHEMA_PATH, encoding="utf-8") as fh:
        schema = json.load(fh)
    return mod.RecordValidator(schema)


# --------------------------------------------------------------- utilities

def get_path(d, dotted):
    """Dotted-path lookup into a nested dict (`--where a.b.c=v`). Returns
    `_MISSING` (never raises) when any component is absent."""
    cur = d
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return _MISSING
        cur = cur[part]
    return cur


def parse_bound(s, end):
    """A `--since`/`--until` bound: a full RFC 3339 timestamp, or a bare
    `YYYY-MM-DD` date (start of day for `--since`, end of day for
    `--until`)."""
    s = s.strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        return s + ("T23:59:59Z" if end else "T00:00:00Z")
    return s


def ts_key(ts):
    """RFC 3339 UTC timestamps sort correctly as plain strings (fixed
    width, zero-padded, `Z` suffix) -- no datetime parsing needed, and
    LC_ALL=C string comparison is exactly what we want."""
    return str(ts)


# ------------------------------------------------------------- record load

@dataclass
class LoadedRecord:
    path: str
    setup: dict | None
    rows: list
    problems: list
    schema_major: int | None
    schema_minor: int | None


def _read_lines(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read().split("\n")
    while raw and raw[-1] == "":
        raw.pop()
    return raw


def _peek_setup_and_rows(raw):
    setup = None
    rows = []
    if raw:
        try:
            first = json.loads(raw[0])
        except json.JSONDecodeError:
            first = None
        if isinstance(first, dict) and first.get("kind") == "setup":
            setup = first
    for line in raw[1:]:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict) and obj.get("kind") in ("match", "compile"):
            rows.append(obj)
    return setup, rows


def load_record(path, rv, check_filename=True):
    raw = _read_lines(path)
    setup, rows = _peek_setup_and_rows(raw)
    problems, _sv = rv.validate_file(path, check_filename=check_filename)
    major = minor = None
    if setup is not None:
        sv = str(setup.get("schema_version", ""))
        m = re.match(r"^(\d+)\.(\d+)$", sv)
        if m:
            major, minor = int(m.group(1)), int(m.group(2))
    return LoadedRecord(path, setup, rows, problems, major, minor)


def load_all(paths, check_filename=True):
    rv = _get_record_validator()
    return [load_record(p, rv, check_filename=check_filename) for p in paths]


# ------------------------------------------------------------ store lookup

def discover_records(store_dir):
    """Returns (paths, source) where source is 'index.tsv' or 'walk
    store/records/', per harness_contract.md 5's "loads the index" and the
    brief's "walk store/records/ if the index is absent -- say which"."""
    index_path = os.path.join(store_dir, "index.tsv")
    if os.path.isfile(index_path):
        paths = []
        with open(index_path, encoding="utf-8") as fh:
            for line in fh:
                line = line.rstrip("\n")
                if not line or line.startswith("#"):
                    continue
                cols = line.split("\t")
                rel = cols[0]
                if rel == "path":  # tolerate an optional header row
                    continue
                paths.append(os.path.normpath(os.path.join(store_dir, rel)))
        return paths, "store/index.tsv"

    records_dir = os.path.join(store_dir, "records")
    paths = []
    for root, _dirs, files in os.walk(records_dir):
        for fname in files:
            if fname.endswith(".jsonl"):
                paths.append(os.path.join(root, fname))
    return sorted(paths), "walked store/records/ (no index.tsv)"


# ---------------------------------------------------------------- filters

def matches_filters(rec: LoadedRecord, args):
    s = rec.setup
    if s is None:
        return False
    if not args.include_synthetic and s.get("synthetic"):
        return False
    if args.subbench and s.get("subbench", {}).get("id") != args.subbench:
        return False
    if args.version and str(s.get("subbench", {}).get("version")) != args.version:
        return False
    if args.machine and s.get("environment", {}).get("machine_id") != args.machine:
        return False
    if args.since or args.until:
        ts = ts_key(s.get("run", {}).get("timestamp", ""))
        if args.since and ts < ts_key(parse_bound(args.since, end=False)):
            return False
        if args.until and ts > ts_key(parse_bound(args.until, end=True)):
            return False
    for f, v in args.where:
        got = get_path(s, f)
        if got is _MISSING or str(got) != v:
            return False
    return True


# --------------------------------------------------------------- reduction

def _pstdev_safe(values):
    return statistics.pstdev(values) if len(values) > 1 else 0.0


# The outcomes that mean "the engine answered, and the answer disagreed
# with the expectation" -- as opposed to `gave-up` (the engine refused to
# answer, on its OWN resource limit) or the hazard outcomes `crashed` /
# `timed-out` (the harness's own limit, not the engine's). schema v1.1,
# record_schema.md 5 ADDITIONS 2: "did-not-match-as-expected is the
# tempting one [to lump gave-up into] and it is the worst".
WRONG_ANSWER_OUTCOMES = frozenset({
    "did-not-match-as-expected", "wrong-span-or-captures", "truncated-subject",
})


@dataclass
class MatchCellReduction:
    n_trials: int
    n_timed: int
    median_ns: float | None
    min_ns: float | None
    max_ns: float | None
    stddev_ns: float | None
    iters: list
    outcome_counts: dict
    pass_rate: float
    n_gave_up: int      # match_outcome == "gave-up" -- the engine's OWN limit, not a wrong answer
    n_wrong: int         # WRONG_ANSWER_OUTCOMES -- an answer that disagreed with the expectation

    @property
    def expectation_failing(self):
        return self.n_trials == 0 or self.pass_rate < 1.0


def reduce_match_cell(rows):
    total = len(rows)
    outcome_counts = Counter(r.get("match_outcome") for r in rows)
    timed = [r for r in rows
             if r.get("match_outcome") == "matched-as-expected" and "timing" in r]
    ns = [r["timing"]["elapsed_ns"] / r["timing"]["iterations"] for r in timed
          if r["timing"].get("iterations")]
    iters = sorted({r["timing"]["iterations"] for r in timed})
    n = len(ns)
    pass_rate = (outcome_counts.get("matched-as-expected", 0) / total) if total else 0.0
    n_gave_up = outcome_counts.get("gave-up", 0)
    n_wrong = sum(outcome_counts.get(o, 0) for o in WRONG_ANSWER_OUTCOMES)
    return MatchCellReduction(
        n_trials=total,
        n_timed=n,
        median_ns=statistics.median(ns) if n else None,
        min_ns=min(ns) if n else None,
        max_ns=max(ns) if n else None,
        stddev_ns=_pstdev_safe(ns) if n else None,
        iters=iters,
        outcome_counts=dict(sorted(outcome_counts.items())),
        pass_rate=pass_rate,
        n_gave_up=n_gave_up,
        n_wrong=n_wrong,
    )


def _timed_ns_by_trial(rows):
    """{trial: ns/call} for the `matched-as-expected` + timed rows of one
    (pattern, subject, regime, testee) cell -- the raw material `--grain
    set` sums across subjects, trial by trial."""
    out = {}
    for r in rows:
        if r.get("match_outcome") != "matched-as-expected" or "timing" not in r:
            continue
        t = r["timing"]
        if not t.get("iterations"):
            continue
        out[r.get("trial")] = t["elapsed_ns"] / t["iterations"]
    return out


@dataclass
class SetCellReduction:
    """The `--grain set` reduction for one (pattern, regime, testee):
    reduces over the WHOLE subject set, not one subject at a time
    (manager change request, 2026-08-25)."""
    n_subjects: int
    n_agreeing: int
    pass_rate: float           # n_agreeing / n_subjects
    failing_subjects: list     # subject_ids not fully agreeing (empty iff pass_rate == 1.0)
    failing_detail: dict       # failing subject_id -> its own MatchCellReduction
    n_trials: int              # trials contributing to the sum (0 if excluded/no data)
    n_gave_up: int             # sum of n_gave_up over every subject in the set
    n_wrong: int                # sum of n_wrong over every subject in the set
    median_ns: float | None
    min_ns: float | None
    max_ns: float | None
    stddev_ns: float | None

    @property
    def expectation_failing(self):
        return self.n_subjects == 0 or self.pass_rate < 1.0


def reduce_set_cell(rows_by_subject):
    """`rows_by_subject`: {subject_id: [match rows]} for one (sb, testee,
    pattern, regime, form). A subject "fails" if its own
    reduce_match_cell() is expectation_failing (any trial not
    matched-as-expected); if ANY subject in the set fails, the WHOLE set
    cell is excluded (manager: "excluded from ranking if ANY subject cell
    fails"), and the failing subject_ids (with their own reductions, so
    a caller can tell a `gave-up` failure from a wrong-answer one) are
    recorded rather than averaged away. Otherwise, per trial number
    common to every subject, sum the per-subject ns/call, then reduce
    (median/min/max/stddev) over those per-trial sums -- "time to process
    the whole set once per call-set"."""
    n_subjects = len(rows_by_subject)
    per_subject = {sid: reduce_match_cell(rows) for sid, rows in rows_by_subject.items()}
    failing = sorted(sid for sid, red in per_subject.items() if red.expectation_failing)
    n_agreeing = n_subjects - len(failing)
    pass_rate = (n_agreeing / n_subjects) if n_subjects else 0.0
    n_gave_up = sum(red.n_gave_up for red in per_subject.values())
    n_wrong = sum(red.n_wrong for red in per_subject.values())
    failing_detail = {sid: per_subject[sid] for sid in failing}

    if failing or not n_subjects:
        return SetCellReduction(
            n_subjects=n_subjects, n_agreeing=n_agreeing, pass_rate=pass_rate,
            failing_subjects=failing, failing_detail=failing_detail, n_trials=0,
            n_gave_up=n_gave_up, n_wrong=n_wrong,
            median_ns=None, min_ns=None, max_ns=None, stddev_ns=None,
        )

    per_subject_trials = {sid: _timed_ns_by_trial(rows) for sid, rows in rows_by_subject.items()}
    trial_sets = [set(d) for d in per_subject_trials.values()]
    common_trials = sorted(set.intersection(*trial_sets)) if trial_sets else []
    sums = [sum(per_subject_trials[sid][t] for sid in rows_by_subject) for t in common_trials]
    n = len(sums)
    return SetCellReduction(
        n_subjects=n_subjects, n_agreeing=n_agreeing, pass_rate=pass_rate,
        failing_subjects=[], failing_detail={}, n_trials=n,
        n_gave_up=n_gave_up, n_wrong=n_wrong,
        median_ns=statistics.median(sums) if n else None,
        min_ns=min(sums) if n else None,
        max_ns=max(sums) if n else None,
        stddev_ns=_pstdev_safe(sums) if n else None,
    )


def _failure_label(red: "MatchCellReduction"):
    """A short label for why a subject's cell failed -- distinguishing
    `gave-up` (the engine's own limit) from a wrong answer, per the
    manager's request to count them apart, not fold them into one tally."""
    if red.n_gave_up and red.n_wrong:
        return "gave-up+wrong"
    if red.n_gave_up:
        return "gave-up"
    if red.n_wrong:
        return "wrong"
    if red.n_trials == 0:
        return "no-data"
    return "other"  # e.g. crashed / timed-out only


@dataclass
class CompileCellReduction:
    cost_class: str
    n_trials: int
    outcome_counts: dict
    median_ns: float | None
    min_ns: float | None
    max_ns: float | None
    stddev_ns: float | None
    n_costed: int
    derived: bool
    derived_n: int = 0


def reduce_compile_cell(rows, lazy_jit_derivation_source=None):
    """`rows` are the compile rows for one (subbench, testee, pattern,
    form). `lazy_jit_derivation_source` is a callable returning the
    (single-element, schema v1.1) list of the derived
    first-match-row-minus-steady-state value when `cost_class ==
    lazy-jit` -- see `_lazy_jit_derivation`."""
    total = len(rows)
    cost_class = rows[0].get("cost_class") if rows else None
    outcome_counts = Counter(r.get("compile_outcome") for r in rows)

    if cost_class == "lazy-jit":
        derived_vals = lazy_jit_derivation_source() if lazy_jit_derivation_source else []
        n = len(derived_vals)
        return CompileCellReduction(
            cost_class=cost_class, n_trials=total,
            outcome_counts=dict(sorted(outcome_counts.items())),
            median_ns=statistics.median(derived_vals) if n else None,
            min_ns=min(derived_vals) if n else None,
            max_ns=max(derived_vals) if n else None,
            stddev_ns=_pstdev_safe(derived_vals) if n else None,
            n_costed=n, derived=True, derived_n=n,
        )

    costed = [r["cost"]["total_ns"] for r in rows
              if r.get("compile_outcome") == "compiled" and "cost" in r]
    n = len(costed)
    return CompileCellReduction(
        cost_class=cost_class, n_trials=total,
        outcome_counts=dict(sorted(outcome_counts.items())),
        median_ns=statistics.median(costed) if n else None,
        min_ns=min(costed) if n else None,
        max_ns=max(costed) if n else None,
        stddev_ns=_pstdev_safe(costed) if n else None,
        n_costed=n, derived=False,
    )


def _lazy_jit_derivation(match_rows_for_pattern_testee):
    """schema v1.1's `first-match-row-minus-steady-state`
    (record_schema.md 8): "The subtrahend is the GLOBALLY-FIRST match row
    of this pattern in this record -- the one with the lowest `seq` --
    and the steady state is the rest." ONE derived ns/call value for the
    whole (pattern, testee), not one per (subject, regime) sub-cell --
    `seq` is a per-RECORD sequence (record_schema.md 8: shared with
    compile rows, in emission order), so "first" here means first across
    every subject and regime this pattern was measured over, which is
    deliberately NOT `trial == 1` of whichever cell happens to sort
    first: a pattern measured over many subjects has many `trial: 1`
    rows and only the very first one (by `seq`) paid the JIT.

    Supersedes a schema-1.0-era version of this function (no `seq`
    existed) that grouped by (subject, regime) and used `trial == 1` as
    the per-cell proxy for "first" -- correct only because schema 1.0
    could not do better. `match_rows_for_pattern_testee` needs only a
    `seq` on every row; it does not need to be one full record (see
    `test_lazy_jit_derivation_uses_lowest_seq_not_trial_one` for a
    hand-built, non-record unit test of exactly this function)."""
    timed = [r for r in match_rows_for_pattern_testee
             if r.get("match_outcome") == "matched-as-expected" and "timing" in r
             and r["timing"].get("iterations")]
    if len(timed) < 2:
        return []
    by_seq = sorted(
        ((r.get("seq"), r["timing"]["elapsed_ns"] / r["timing"]["iterations"]) for r in timed),
        key=lambda pair: pair[0],
    )
    first_ns = by_seq[0][1]
    steady = [ns for _seq, ns in by_seq[1:]]
    return [first_ns - statistics.median(steady)]


# ---------------------------------------------------------------- the run

@dataclass
class ReportData:
    query_desc: list
    source_desc: str
    included: list          # list of (record_id, path)
    excluded_invalid: list  # list of (path, [problem strings])
    subbench_versions: set
    machines: set
    schema_versions: set
    match_cells: dict       # (sb,testee,pattern,subject,regime,form) -> (testee_id, MatchCellReduction)
    set_cells: dict         # (sb,testee,pattern,regime,form) -> (testee_id, SetCellReduction)
    compile_cells: dict     # (sb,testee,pattern,form) -> (testee_id, CompileCellReduction)
    reference_testee_pred: str
    grain: str              # 'set' (default) or 'subject' -- which the renderer shows
    single_subject_regimes: list  # regimes where every (pattern) cell has <=1 subject:
                                   # set and subject grain render identically there
    show_form: bool         # True iff a form other than 'plain' appears anywhere in the
                             # selected records -- gates the 'form' column so a report over
                             # an all-plain store looks exactly as it did before v1.1


def build_report(loaded, args):
    """Returns (ReportData | None, error_message | None). On a refusal
    (mixed major schema versions), returns (None, message)."""
    selected = [r for r in loaded if matches_filters(r, args)]

    # Mixed-schema-version refusal (requirements 6; record_schema.md 4).
    # Evaluated on the DECLARED major, independent of whether the shared
    # validator can read it -- see the module docstring.
    by_major = defaultdict(list)
    for r in selected:
        if r.schema_major is not None:
            by_major[r.schema_major].append(r)
    if len(by_major) > 1:
        detail = "; ".join(
            f"{maj}.x: " + ", ".join(sorted(os.path.basename(r.path) for r in rs))
            for maj, rs in sorted(by_major.items())
        )
        return None, (
            "refusing to report: the selected records mix MAJOR schema "
            f"versions with no declared migration ({detail}). Narrow the "
            "query (--subbench/--version/--where) to one major version, "
            "or wait for a migration to be declared."
        )

    excluded_invalid = []
    valid = []
    for r in selected:
        if r.problems:
            excluded_invalid.append(
                (r.path, [str(p) for p in r.problems]))
        else:
            valid.append(r)

    included = []
    subbench_versions = set()
    machines = set()
    schema_versions = set()
    forms_seen = set()
    # `form` (schema v1.1, record_schema.md 5 ADDITIONS 3) is part of every
    # match- and compile-cell key: a testee with no end-anchored mode
    # compiles and times a SEPARATE `whole-subject` artifact for the
    # match-compliance regime, and the two forms must never share a
    # reduction. ABSENT on a row means `plain`.
    match_rows_by_key = defaultdict(list)    # (sb, testee, pattern, subject, regime, form) -> rows
    compile_rows_by_key = defaultdict(list)  # (sb, testee, pattern, form) -> rows
    match_rows_by_pt = defaultdict(list)     # (sb, testee, pattern) -> match rows (for lazy-jit;
                                              # NOT split by form -- record_schema.md 8's "the rest"
                                              # is not form-scoped, and no fixture here crosses a
                                              # lazy-jit testee with a whole-subject form to test it)

    for r in valid:
        s = r.setup
        sb = s["subbench"]["id"] + "@" + str(s["subbench"]["version"])
        testee_id = s["testee"]["testee_id"]
        included.append((s["record_id"], r.path))
        subbench_versions.add(sb)
        machines.add(s["environment"]["machine_id"])
        schema_versions.add(s["schema_version"])

        for row in r.rows:
            form = row.get("form") or "plain"
            forms_seen.add(form)
            if row["kind"] == "match":
                if args.regime and row.get("regime") != args.regime:
                    continue
                key = (sb, testee_id, row["pattern_id"], row["subject_id"], row["regime"], form)
                match_rows_by_key[key].append(row)
                match_rows_by_pt[(sb, testee_id, row["pattern_id"])].append(row)
            else:
                key = (sb, testee_id, row["pattern_id"], form)
                compile_rows_by_key[key].append(row)

    match_cells = {}
    for key, rows in match_rows_by_key.items():
        sb, testee_id, pattern_id, subject_id, regime, form = key
        match_cells[key] = (testee_id, reduce_match_cell(rows))

    # --grain set: reduce over the whole subject set per (pattern, regime, form).
    set_rows_by_key = defaultdict(dict)  # (sb, testee, pattern, regime, form) -> {subject_id: rows}
    for (sb, testee_id, pattern_id, subject_id, regime, form), rows in match_rows_by_key.items():
        set_rows_by_key[(sb, testee_id, pattern_id, regime, form)][subject_id] = rows
    set_cells = {}
    for key, rows_by_subject in set_rows_by_key.items():
        sb, testee_id, pattern_id, regime, form = key
        set_cells[key] = (testee_id, reduce_set_cell(rows_by_subject))

    regime_subject_counts = defaultdict(set)
    for (sb, testee_id, pattern_id, regime, form), (tid, red) in set_cells.items():
        regime_subject_counts[regime].add(red.n_subjects)
    single_subject_regimes = sorted(
        r for r, counts in regime_subject_counts.items() if counts and max(counts) <= 1)

    compile_cells = {}
    for key, rows in compile_rows_by_key.items():
        sb, testee_id, pattern_id, form = key
        pt_key = (sb, testee_id, pattern_id)
        src = lambda rows=match_rows_by_pt.get(pt_key, []): _lazy_jit_derivation(rows)
        compile_cells[key] = (testee_id, reduce_compile_cell(rows, lazy_jit_derivation_source=src))

    query_desc = []
    for name in ("subbench", "version", "regime", "machine", "since", "until"):
        v = getattr(args, name)
        if v:
            query_desc.append(f"{name}={v}")
    for f, v in args.where:
        query_desc.append(f"where {f}={v}")
    if args.include_synthetic:
        query_desc.append("include-synthetic")

    return ReportData(
        query_desc=query_desc,
        source_desc=args._source_desc,
        included=sorted(included),
        excluded_invalid=sorted(excluded_invalid),
        subbench_versions=subbench_versions,
        machines=machines,
        schema_versions=schema_versions,
        match_cells=match_cells,
        set_cells=set_cells,
        compile_cells=compile_cells,
        reference_testee_pred="libpcre2 engine_mode=interp",
        grain=args.grain,
        single_subject_regimes=single_subject_regimes,
        show_form=bool(forms_seen - {"plain"}),
    ), None


# -------------------------------------------------------------- rendering

def _fmt_ns(ns):
    if ns is None:
        return "-"
    return f"{ns:,.1f}"


def _is_reference(testee_setup_by_id, testee_id):
    # testee_id is CONSTRUCTED (record_schema.md 6.4): engine_libpcre2's
    # interp mode is spelled `libpcre2_<version>_interp-...`.
    return testee_id.startswith("libpcre2_") and "_interp-" in testee_id


def _ranking_groups(rd: ReportData, grain):
    """grain='subject': keys are (sb, pattern, subject, regime), values
    are [(testee_id, form, MatchCellReduction)]. grain='set': keys are
    (sb, pattern, regime), values are [(testee_id, form,
    SetCellReduction)].

    `form` (schema v1.1) is DELIBERATELY NOT part of the group key
    (manager fix request, 2026-08-25, reversing this module's first cut):
    `form` records HOW a testee reached the regime (pcrec: a second
    `(?:P)\\z` artifact; libpcre2: runtime ANCHORED|ENDANCHORED flags on
    its ordinary artifact) -- both answer the SAME question and MUST
    rank together, or the compliance regime (the whole point of which is
    comparing engines) never compares anything. `form` still stays in
    `rd.match_cells`/`rd.set_cells`'s OWN keys (so a testee that somehow
    carries both forms for one regime still reduces to two distinguishable
    rows, each carrying its own form here) and in `rd.compile_cells`'s key
    (a `whole-subject` compile is a separate artifact with its own cost,
    size and trials -- that half of the schema's point stands unchanged)."""
    groups = defaultdict(list)
    if grain == "subject":
        for (sb, testee_id, pattern_id, subject_id, regime, form), (tid, red) \
                in rd.match_cells.items():
            groups[(sb, pattern_id, subject_id, regime)].append((testee_id, form, red))
    else:
        for (sb, testee_id, pattern_id, regime, form), (tid, red) in rd.set_cells.items():
            groups[(sb, pattern_id, regime)].append((testee_id, form, red))
    return groups


def _partial_coverage(r):
    """True iff `r` (a MatchCellReduction or SetCellReduction) has less
    than full coverage -- triggers the N + pass-rate columns."""
    return r.pass_rate < 1.0 or getattr(r, "n_trials", 1) == 0


def _n_and_pass_rate(r, grain):
    if grain == "subject":
        return r.n_trials, r.pass_rate
    return r.n_subjects, r.pass_rate


def render_markdown(rd: ReportData):
    out = []
    out.append("# pcrec-bench report\n")
    out.append("## Query\n")
    out.append(f"- filters: {', '.join(rd.query_desc) if rd.query_desc else '(none)'}")
    out.append(f"- record source: {rd.source_desc}")
    out.append(f"- records included: {len(rd.included)}")
    for rid, path in rd.included:
        out.append(f"    - `{rid}` ({os.path.relpath(path)})")
    if rd.excluded_invalid:
        out.append(f"- records excluded (failed validation): {len(rd.excluded_invalid)}")
        for path, problems in rd.excluded_invalid:
            out.append(f"    - `{os.path.relpath(path)}`: {problems[0]}"
                        + (f" (+{len(problems)-1} more)" if len(problems) > 1 else ""))
    out.append(f"- sub-bench version(s): {', '.join(sorted(rd.subbench_versions)) or '(none)'}")
    out.append(f"- machine(s): {', '.join(sorted(rd.machines)) or '(none)'}")
    out.append(f"- schema version(s): {', '.join(sorted(rd.schema_versions)) or '(none)'}")
    out.append(f"- grain: {rd.grain} "
                + ("(sum of per-subject ns/call over the whole subject set, "
                   "reduced over trials; a set cell is excluded if ANY "
                   "subject in it fails)" if rd.grain == "set" else
                   "(per pattern x subject x regime; the drill-down)"))
    if rd.single_subject_regimes:
        out.append("- regime(s) with exactly one subject per pattern "
                    "(set and subject grain render identically there): "
                    + ", ".join(f"`{r}`" for r in rd.single_subject_regimes))
    out.append("- reduction: median/min/max/stddev (population) over "
                "per-trial `elapsed_ns / iterations`; lazy-JIT compile cost "
                "is DERIVED as first-match-row-minus-steady-state (lowest "
                "`seq` timed row for the pattern, minus the median of every "
                "other timed row), one value per (pattern, testee), never "
                "pooled with another execution-model class's compile cost")
    if rd.show_form:
        out.append("- `form`: this report includes a `whole-subject` "
                    "artifact beside `plain` for at least one cell (schema "
                    "v1.1: a testee with no end-anchored mode compiles and "
                    "times a SEPARATE artifact for match-compliance, e.g. "
                    "`(?:pattern)\\z`, where another testee reaches the "
                    "same regime via runtime flags on its ordinary "
                    "artifact) -- shown as a per-row COLUMN, not a split: "
                    "both forms answer the same regime and RANK TOGETHER "
                    "in one table (`form` is a key only for compile-cost "
                    "rows, where a whole-subject artifact is genuinely a "
                    "separate compile with its own cost)")
    out.append("")

    if not rd.match_cells and not rd.compile_cells:
        out.append("_No cells matched this query._\n")
        return "\n".join(out) + "\n"

    grain = rd.grain
    if grain == "subject":
        out.append("## Ranking (per pattern x subject x regime; best median first)\n")
    else:
        out.append("## Ranking (per pattern x regime, SET grain: sum over the "
                    "subject set; best median first)\n")
    groups = _ranking_groups(rd, grain)
    excluded_cells = []
    for gkey in sorted(groups):
        entries = groups[gkey]
        rankable = [(t, form, r) for t, form, r in entries
                    if not r.expectation_failing and getattr(r, "n_timed", r.n_trials)]
        failing = [(t, form, r) for t, form, r in entries if r.expectation_failing]
        for t, form, r in failing:
            excluded_cells.append((gkey, t, form, r))
        if not rankable:
            continue
        rankable.sort(key=lambda tfr: tfr[2].median_ns)
        ref = next((r for t, form, r in rankable if _is_reference(None, t)), None)
        ref_ns = ref.median_ns if ref else rankable[0][2].median_ns
        any_partial = any(_partial_coverage(r) for _t, _f, r in entries)

        if grain == "subject":
            sb, pattern_id, subject_id, regime = gkey
            title = f"### `{pattern_id}` / `{subject_id}` / `{regime}`"
        else:
            sb, pattern_id, regime = gkey
            title = f"### `{pattern_id}` / `{regime}`"
        out.append(f"{title} ({sb})\n")
        header = ["rank", "testee"]
        if rd.show_form:
            header.append("form")
        header += ["median ns/call", "min", "max", "stddev", "ratio"]
        if any_partial:
            header += (["n subjects", "pass-rate"] if grain == "set" else ["n", "pass-rate"])
        out.append("| " + " | ".join(header) + " |")
        out.append("|" + "|".join(["---"] * len(header)) + "|")
        for i, (t, form, r) in enumerate(rankable, start=1):
            ratio = r.median_ns / ref_ns if ref_ns else float("nan")
            row = [str(i), f"`{t}`"]
            if rd.show_form:
                row.append(f"`{form}`")
            row += [_fmt_ns(r.median_ns), _fmt_ns(r.min_ns),
                    _fmt_ns(r.max_ns), _fmt_ns(r.stddev_ns), f"{ratio:.3f}x"]
            if any_partial:
                n, pr = _n_and_pass_rate(r, grain)
                row += [str(n), f"{pr*100:.0f}%"]
            out.append("| " + " | ".join(row) + " |")
        out.append("")

    if excluded_cells:
        out.append("## Excluded from ranking (expectation-failing cells)\n")
        if grain == "subject":
            header = ["pattern", "subject", "regime"]
            if rd.show_form:
                header.append("form")
            header += ["testee", "n", "pass-rate", "gave-up", "wrong", "outcomes"]
            out.append("| " + " | ".join(header) + " |")
            out.append("|" + "|".join(["---"] * len(header)) + "|")
            for gkey, t, form, r in sorted(excluded_cells):
                sb, pattern_id, subject_id, regime = gkey
                outcomes = ", ".join(f"{k}={v}" for k, v in r.outcome_counts.items())
                row = [f"`{pattern_id}`", f"`{subject_id}`", f"`{regime}`"]
                if rd.show_form:
                    row.append(f"`{form}`")
                row += [f"`{t}`", str(r.n_trials), f"{r.pass_rate*100:.0f}%",
                        str(r.n_gave_up), str(r.n_wrong), outcomes]
                out.append("| " + " | ".join(row) + " |")
        else:
            header = ["pattern", "regime"]
            if rd.show_form:
                header.append("form")
            header += ["testee", "n subjects", "pass-rate", "gave-up", "wrong",
                       "failing subjects (reason)"]
            out.append("| " + " | ".join(header) + " |")
            out.append("|" + "|".join(["---"] * len(header)) + "|")
            for gkey, t, form, r in sorted(excluded_cells):
                sb, pattern_id, regime = gkey
                failing_list = ", ".join(
                    f"`{sid}` ({_failure_label(r.failing_detail[sid])})"
                    for sid in r.failing_subjects
                ) or "(none timed)"
                row = [f"`{pattern_id}`", f"`{regime}`"]
                if rd.show_form:
                    row.append(f"`{form}`")
                row += [f"`{t}`", str(r.n_subjects), f"{r.pass_rate*100:.0f}%",
                        str(r.n_gave_up), str(r.n_wrong), failing_list]
                out.append("| " + " | ".join(row) + " |")
        out.append("")

    out.append("## Compile cost (by execution-model class; never pooled across classes)\n")
    by_class = defaultdict(list)
    for (sb, testee_id, pattern_id, form), (t, r) in rd.compile_cells.items():
        by_class[r.cost_class].append((sb, pattern_id, testee_id, form, r))
    for cls in sorted(by_class):
        out.append(f"### `{cls}`\n")
        label = "median ns (derived: first-match-row-minus-steady-state)" \
            if by_class[cls][0][4].derived else "median total_ns"
        header = ["pattern"]
        if rd.show_form:
            header.append("form")
        header += ["testee", label, "min", "max", "stddev", "n costed", "outcomes"]
        out.append("| " + " | ".join(header) + " |")
        out.append("|" + "|".join(["---"] * len(header)) + "|")
        for sb, pattern_id, testee_id, form, r in sorted(by_class[cls]):
            outcomes = ", ".join(f"{k}={v}" for k, v in r.outcome_counts.items())
            row = [f"`{pattern_id}`"]
            if rd.show_form:
                row.append(f"`{form}`")
            row += [f"`{testee_id}`", _fmt_ns(r.median_ns), _fmt_ns(r.min_ns), _fmt_ns(r.max_ns),
                    _fmt_ns(r.stddev_ns), str(r.n_costed), outcomes]
            out.append("| " + " | ".join(row) + " |")
        out.append("")

    return "\n".join(out) + "\n"


def render_tsv(rd: ReportData):
    grain = rd.grain
    lines = []
    lines.append("# " + "; ".join(
        [f"filters: {', '.join(rd.query_desc) or '(none)'}",
         f"source: {rd.source_desc}",
         f"records: {len(rd.included)}",
         f"excluded_invalid: {len(rd.excluded_invalid)}",
         f"subbench_versions: {','.join(sorted(rd.subbench_versions))}",
         f"machines: {','.join(sorted(rd.machines))}",
         f"schema_versions: {','.join(sorted(rd.schema_versions))}",
         f"grain: {grain}",
         f"single_subject_regimes: {','.join(rd.single_subject_regimes)}"]))
    lines.append("\t".join(["section", "pattern", "subject_or_na", "regime_or_na", "form",
                             "testee", "rank_or_na", "metric", "value", "n", "pass_rate",
                             "n_gave_up", "n_wrong"]))

    groups = _ranking_groups(rd, grain)
    for gkey in sorted(groups):
        if grain == "subject":
            sb, pattern_id, subject_id, regime = gkey
        else:
            sb, pattern_id, regime = gkey
            subject_id = "(set)"
        entries = groups[gkey]
        rankable = [(t, form, r) for t, form, r in entries
                    if not r.expectation_failing and getattr(r, "n_timed", r.n_trials)]
        rankable.sort(key=lambda tfr: tfr[2].median_ns)
        ref = next((r for t, form, r in rankable if _is_reference(None, t)), None)
        ref_ns = ref.median_ns if ref else (rankable[0][2].median_ns if rankable else None)
        for i, (t, form, r) in enumerate(rankable, start=1):
            ratio = (r.median_ns / ref_ns) if ref_ns else float("nan")
            n, pr = _n_and_pass_rate(r, grain)
            for metric, val in (("median_ns", r.median_ns), ("min_ns", r.min_ns),
                                 ("max_ns", r.max_ns), ("stddev_ns", r.stddev_ns),
                                 ("ratio", ratio)):
                lines.append("\t".join(["rank", pattern_id, subject_id, regime, form, t, str(i),
                                         metric, f"{val:.6f}" if val is not None else "",
                                         str(n), f"{pr:.4f}", str(r.n_gave_up), str(r.n_wrong)]))
        for t, form, r in entries:
            if r.expectation_failing:
                n, pr = _n_and_pass_rate(r, grain)
                lines.append("\t".join(["excluded", pattern_id, subject_id, regime, form, t, "",
                                         "pass_rate", f"{r.pass_rate:.4f}",
                                         str(n), f"{pr:.4f}", str(r.n_gave_up), str(r.n_wrong)]))

    for (sb, testee_id, pattern_id, form), (t, r) in sorted(rd.compile_cells.items()):
        metric = "derived_first_match_row_minus_steady_state_ns" if r.derived else "median_total_ns"
        lines.append("\t".join(["compile", pattern_id, "", "", form, testee_id, "",
                                 metric, f"{r.median_ns:.6f}" if r.median_ns is not None else "",
                                 str(r.n_trials), "", "", ""]))

    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------- CLI

def build_argparser():
    ap = argparse.ArgumentParser(prog="pcrecbench report",
                                  description="Query the record store and "
                                              "render a comparison report "
                                              "(docs/design/requirements.md 8).")
    ap.add_argument("--store", default="store",
                     help="the store directory (default: ./store)")
    ap.add_argument("--subbench", help="filter: subbench.id equals this")
    ap.add_argument("--version", help="filter: subbench.version equals this")
    ap.add_argument("--regime", help="restrict match rows to this regime")
    ap.add_argument("--machine", help="filter: environment.machine_id equals this")
    ap.add_argument("--since", help="filter: run.timestamp >= this "
                                    "(RFC 3339 or YYYY-MM-DD)")
    ap.add_argument("--until", help="filter: run.timestamp <= this "
                                    "(RFC 3339 or YYYY-MM-DD)")
    ap.add_argument("--where", action="append", default=[], metavar="field=value",
                     help="filter on a dotted setup-layer path, e.g. "
                          "testee.openness=open-source; repeatable (AND)")
    ap.add_argument("--format", choices=["md", "tsv"], default="md")
    ap.add_argument("--grain", choices=["set", "subject"], default="set",
                     help="ranking grain (manager change request, 2026-08-25): "
                          "'set' (default) reduces over the whole subject set "
                          "per (pattern, regime) -- per trial, sum the "
                          "per-subject ns/call over the set, then reduce over "
                          "trials; a set cell excludes if ANY subject in it "
                          "fails. 'subject' gives the finer (pattern, subject, "
                          "regime) drill-down tables.")
    ap.add_argument("--include-synthetic", action="store_true",
                     help="ADDITION beyond requirements/harness_contract: "
                          "include synthetic:true records (excluded by "
                          "default per schema/examples/CLAUDE.md). Needed "
                          "to report over this reporter's own fixtures, "
                          "since no engine is ever run here.")
    return ap


def _parse_where(items):
    out = []
    for w in items:
        if "=" not in w:
            raise ValueError(f"--where must be field=value, got {w!r}")
        k, v = w.split("=", 1)
        out.append((k, v))
    return out


def main(argv=None):
    os.environ.setdefault("LC_ALL", "C")
    args = build_argparser().parse_args(argv)
    try:
        args.where = _parse_where(args.where)
    except ValueError as exc:
        print(f"pcrecbench report: {exc}", file=sys.stderr)
        return 2

    paths, source_desc = discover_records(args.store)
    args._source_desc = f"{source_desc} ({len(paths)} candidate file(s))"
    if not paths:
        print(f"pcrecbench report: no records found under {args.store!r} "
              f"({source_desc})", file=sys.stderr)
        return 1

    loaded = load_all(paths, check_filename=True)
    rd, err = build_report(loaded, args)
    if err:
        print(f"pcrecbench report: {err}", file=sys.stderr)
        return 1

    if args.format == "tsv":
        sys.stdout.write(render_tsv(rd))
    else:
        sys.stdout.write(render_markdown(rd))
    return 0


if __name__ == "__main__":
    sys.exit(main())
