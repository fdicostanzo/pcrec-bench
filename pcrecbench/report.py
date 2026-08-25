#!/usr/bin/env python3
"""pcrecbench.report -- the reporter ([B5] landing bar; [B9] columns/rulings).

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

REPORTER_VERSION below is stamped into every rendered report's header
(the [B9] brief: "the header carries the reporter's version") -- bump it
whenever rendering changes so a reader can tell two reports produced by
different reporter code apart even when the query is identical.

Design decisions this module makes that the contract leaves to [B5]/[B9]
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
  numbers (requirements 3). Not exercised by an end-to-end fixture record
  (none of this project's testees are `lazy-jit`), so it is unit-tested
  directly against hand-built row dicts instead.
* `form` (`plain` / `whole-subject`, schema v1.1, record_schema.md 5
  ADDITIONS 3) is part of every match- and compile-cell key here (a
  testee with no end-anchored mode, like pcrec, compiles and times a
  SEPARATE artifact for the match-compliance regime, and the two must
  never share a row or a reduction). Shown as its own column beside the
  numbers, but only in tables where more than `plain` actually appears
  in the selected records -- when everything is `plain` (the common
  case) the column is omitted rather than clutter every report with a
  constant. [B9] R4 adds the `fact` column beside it -- see `_form_fact`.
* `match_outcome = gave-up` (schema v1.1) means the engine exhausted its
  OWN resource limit and said so -- it is not a wrong answer and not a
  crash, and lumping its count into "wrong answers" would bury the
  bench's own headline finding (record_schema.md 5 ADDITIONS 2). Every
  outcome-counting surface here (`MatchCellReduction.n_gave_up` /
  `.n_wrong`, `SetCellReduction`'s aggregates, the excluded-cells
  tables) keeps `gave-up` a separate tally from
  `did-not-match-as-expected` / `wrong-span-or-captures` /
  `truncated-subject`.

[B9] (2026-08-25) additions, rulings R1-R9 (docs/dev/plan.md row [B9];
docs/design/requirements.md OD-B11, OD-B13, OD-B14, OD-B15):

* R1/OD-B14 -- every ranking row carries the record's `status`; a
  non-`measured` status excludes the row from ranking by default
  (`--include-unmeasured` overrides), listed under its table as
  `not ranked: <testee> -- <status> (<excerpt>)`.
* R2/OD-B15 -- two records of one (subbench@version, testee_id, machine):
  the NEWEST by `run.timestamp` ranks by default; older ones are
  SUPERSEDED (named in the header, never silently pooled);
  `--all-records` shows every record as its own row, its testee id
  suffixed `@<compact-timestamp>`.
* R3 -- the optional `tier` setup field lane b10loop is adding at schema
  v1.2 (`pinned` default | `scratch`); coded here as "absent = pinned"
  ahead of the schema landing it. A `scratch` row is excluded from
  ranking by default (`--include-scratch` overrides, and adds a `tier`
  column).
* R4 -- the `fact` column beside `form`: `form` is, BY CONSTRUCTION
  (record_schema.md 5 ADDITIONS 3, enforced by X27), a restatement --
  `whole-subject` is always a second compiled artifact, `plain` is
  always the one ordinary artifact with a runtime flag. A ranking table
  whose rankable rows mix both facts gets a note under its title (the
  "regime artifact" bucket, pcrecdev1 feedback 2a, stated as a fact).
* R5 -- two ratio columns, `vs baseline` (the named reference testee,
  named in the table TITLE too) and `vs best` (best measured row = 1.000x).
* R6 -- `short-subject-search` tables (SET grain) carry `n subjects` and
  `per-subject mean ns` always, plus a `floor` note; no floor field
  exists in the schema yet, so the note says so rather than inventing a
  number (`_floor_note_line`).
* R7/OD-B11 -- a set cell with give-ups shows `gave-up: <CODE>x<n
  subjects> (smallest: <id>, <bytes> B)` in the excluded-cells table
  (`_gave_up_cell_summary`), the count in SUBJECTS not trials; `crashed`
  / `timed-out` are named by the outcome itself in the per-subject
  failure label (`_failure_label`), never folded into "(other)".
* R8 -- a cross-pin pair (same engine + config, different version_slug,
  record_schema.md 6.4) gets a `Δ vs previous version` column (SET grain
  only) with a computed verdict (`_cross_pin_verdict`: unchanged within
  2x the larger stddev, else faster/slower xN.NN) and a per-row "worst
  subject" note; a cell excluded at the previous pin and ranked now says
  `now measured (was: <reason>)`.
* R9 -- pcrec compile-cost rows carry mechanism-stamp columns read ONLY
  from `engine_metadata` (never diagnostics): `engine`, `entry` (`_in`
  when buffer pairs are present, `plain entry` otherwise), `prefilter`
  (a DFA row states `(no stamp -- pcrec I-3)` rather than leaving it
  blank), `vm_rungs` (bit names joined by `|`), `buffer_frames`/
  `buffer_trail`, `resume_frame_size`; the compile table also splits by
  phase (emit-c/gcc/load, beside the total) and flags `stddev > median`
  rows as timer jitter. OD-B13: `--subbench` accepts the sub-bench
  DIRECTORY name (resolved via `bench/<dir>/subbench.toml`'s own `id`)
  as well as the sidecar id.
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

REPORTER_VERSION = "v2 (2026-08-25)"

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


def _date_suffix(ts):
    """[B9] R2: the compact timestamp `--all-records` appends to a
    testee id to disambiguate multiple records of one (subbench@version,
    testee_id, machine) -- the same digits as the record filename's own
    timestamp component ("2026-08-25T17:34:02Z" -> "20260825T173402Z")."""
    return re.sub(r"[-:]", "", str(ts))


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


def resolve_subbench_arg(value, repo_root=REPO_ROOT):
    """OD-B13: `--subbench` accepts a sub-bench DIRECTORY name (e.g.
    `email`) as well as its sidecar id (`email-specimen`) -- resolved via
    `bench/<dir>/subbench.toml`'s own `id` field, so nothing here has to
    duplicate the sidecar's own claim.

    Returns (resolved_value, alias_note): alias_note is a human-readable
    string when a directory-name resolution actually happened, else
    `None` (including when `value` is already the sidecar id, or names
    no directory at all -- filtering then simply matches nothing, same
    as before this ruling)."""
    if not value:
        return value, None
    toml_path = os.path.join(repo_root, "bench", value, "subbench.toml")
    if not os.path.isfile(toml_path):
        return value, None
    try:
        import tomllib
        with open(toml_path, "rb") as fh:
            data = tomllib.load(fh)
    except Exception:
        return value, None
    sidecar_id = data.get("id")
    if not sidecar_id or sidecar_id == value:
        return value, None
    return sidecar_id, (f"subbench={sidecar_id} (resolved from directory "
                         f"name {value!r} via bench/{value}/subbench.toml)")


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

# TODO(manager, [B9]->[B10] merge): lane/b10loop (unmerged as of this
# session, commit 897b68f "pcrecbench/reduce.py, the set-grain reduction
# quick and the reporter share (R5)") places a SHARED reduce_match_cell/
# reduce_set_cell/giveup_code in pcrecbench/reduce.py, explicitly so
# `quick`'s inline comparable and this reporter's never disagree about
# "faster". It was not on master when this lane finished, so
# reduce_match_cell/reduce_set_cell below (and _extract_diagnostic_code,
# the analogue of reduce.py's giveup_code) are this lane's OWN
# implementations -- replace all four with `from pcrecbench.reduce import
# reduce_match_cell, reduce_set_cell, giveup_code` at merge time, keeping
# only what reduce.py does not cover (the R1-R9 rendering above it).
# FLAG FOR RECONCILIATION: the two `giveup_code` functions format
# DIFFERENTLY today -- reduce.py's regex-matches the `giveup:<n>:<NAME>`
# driver-protocol token and keeps the NUMERIC code too
# (`-3:PCREC_ERR_FRAMES`), falling back to a 64-char truncated raw
# diagnostic when that token is absent (e.g. pcre2's diagnostics, which
# never carry it); `_extract_diagnostic_code` below instead pattern-matches
# any trailing ALL-CAPS_WITH_UNDERSCORE token generically, dropping the
# numeric code, which is what lets it read BOTH engines' diagnostics with
# one rule. Importing reduce.py's `giveup_code` as-is would change every
# `gave-up: <CODE>x...` cell this lane's R7 renders (pcre2 diagnostics in
# particular would start showing a truncated sentence instead of a bare
# code) -- worth a decision at merge, not a silent adoption.

# [B9] R7: a diagnostic's engine-specific CODE -- an ALL-CAPS token with at
# least one underscore-separated segment (`PCREC_ERR_WORK`,
# `PCRE2_ERROR_MATCHLIMIT`), so a plain all-caps English word swept up in
# the sentence around it (e.g. a fixture's trailing "FIXTURE") never
# qualifies. The LAST such token in the diagnostic is taken -- both
# engines' diagnostic strings put the specific code at the end.
_CODE_RE = re.compile(r"[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+")


def _extract_diagnostic_code(diagnostic):
    if not diagnostic:
        return None
    matches = _CODE_RE.findall(diagnostic)
    return matches[-1] if matches else None


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
    gave_up_codes: Counter = field(default_factory=Counter)  # [B9] R7: per-trial diagnostic codes

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
    gave_up_codes = Counter(
        _extract_diagnostic_code(r.get("diagnostic"))
        for r in rows if r.get("match_outcome") == "gave-up")
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
        gave_up_codes=gave_up_codes,
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
    `gave-up` (the engine's own limit) from a wrong answer, AND, per
    OD-B11, from the harness's own hazard outcomes `crashed` /
    `timed-out` (never folded into an unnamed "(other)"). More than one
    kind combines with `+` -- distinct trials of one subject cell may
    have failed for distinct reasons."""
    labels = []
    if red.n_gave_up:
        labels.append("gave-up")
    if red.n_wrong:
        labels.append("wrong")
    if red.outcome_counts.get("crashed"):
        labels.append("crashed")
    if red.outcome_counts.get("timed-out"):
        labels.append("timed-out")
    if labels:
        return "+".join(labels)
    if red.n_trials == 0:
        return "no-data"
    return "other"


def _gave_up_cell_summary(failing_detail, subject_bytes):
    """[B9] R7: the excluded-cells table's give-up cell, by CODE (never a
    bare trial count) -- 'gave-up: <CODE>x<n subjects> (smallest: <id>,
    <bytes> B)', one clause per distinct code seen, sorted by code for a
    deterministic render. The count is SUBJECTS that gave up (each
    counted once, by its DOMINANT code), not trials."""
    by_code = defaultdict(list)  # code -> [(subject_id, bytes_or_None)]
    for sid, red in failing_detail.items():
        if not red.n_gave_up:
            continue
        code = red.gave_up_codes.most_common(1)[0][0] if red.gave_up_codes else "UNKNOWN"
        by_code[code or "UNKNOWN"].append((sid, subject_bytes.get(sid)))
    if not by_code:
        return "0"
    clauses = []
    for code in sorted(by_code):
        subs = by_code[code]
        smallest = min(subs, key=lambda sb: (sb[1] is None, sb[1] if sb[1] is not None else 0))
        b_str = f"{smallest[1]:,}" if smallest[1] is not None else "?"
        clauses.append(f"{code}×{len(subs)} (smallest: {smallest[0]}, {b_str} B)")
    return "; ".join(clauses)


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
    sample_engine_metadata: dict | None = None   # [B9] R9: one row's engine_metadata (declared-consistent)
    phase_medians: dict = field(default_factory=dict)  # [B9] R9: {"emit-c"/"gcc"/"load": median_ns}


def _phase_medians(rows):
    """[B9] R9: per-phase (emit-c/gcc/load) median ns across a compile
    cell's COSTED rows -- AOT rows only (`cost.phases`); an interpreter
    or eager-JIT compile row has no phase breakdown and contributes
    nothing here."""
    by_phase = defaultdict(list)
    for r in rows:
        if r.get("compile_outcome") != "compiled":
            continue
        for ph in ((r.get("cost") or {}).get("phases") or []):
            by_phase[ph["name"]].append(ph["elapsed_ns"])
    return {name: statistics.median(vals) for name, vals in by_phase.items() if vals}


def reduce_compile_cell(rows, lazy_jit_derivation_source=None):
    """`rows` are the compile rows for one (subbench, testee, pattern,
    form). `lazy_jit_derivation_source` is a callable returning the
    (single-element, schema v1.1) list of the derived
    first-match-row-minus-steady-state value when `cost_class ==
    lazy-jit` -- see `_lazy_jit_derivation`."""
    total = len(rows)
    cost_class = rows[0].get("cost_class") if rows else None
    outcome_counts = Counter(r.get("compile_outcome") for r in rows)
    sample_em = next((r.get("engine_metadata") for r in rows if r.get("engine_metadata")), None)

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
            sample_engine_metadata=sample_em, phase_medians={},
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
        sample_engine_metadata=sample_em, phase_medians=_phase_medians(rows),
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

    `match_rows_for_pattern_testee` needs only a `seq` on every row; it
    does not need to be one full record (see
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


# ------------------------------------------------------------- [B9] R9 helpers

def _mechanism_stamp_columns(engine_metadata):
    """[B9] R9: pcrec's own mechanism as report columns, read ONLY from
    `engine_metadata` (never `diagnostic` -- record_schema.md 7's whole
    point is that these facts are STRUCTURED, not prose). A DFA artifact
    emits no VM_* stamps by construction (record_schema.md 7's own note:
    "A DFA-engine pcrec testee therefore declares only the rx_info-
    sourced pairs. An ABSENT pair is not an error"), so a DFA row states
    that as a FACT (pcrec I-3) rather than leaving a column blank as if
    the data were merely missing. `entry` is DERIVED from the presence
    of a buffer-capacity pair, not read from a field named `entry` (none
    exists): a testee that ran through the caller-provided-buffer `_in`
    entries carries `buffer_frames`/`buffer_trail`; one that did not,
    does not."""
    em = engine_metadata or {}
    engine = em.get("engine")
    has_buffers = ("buffer_frames" in em) or ("buffer_trail" in em)
    entry = "_in" if has_buffers else "plain entry"
    if engine == "dfa":
        prefilter = "(no stamp — pcrec I-3)"
    else:
        prefilter = em.get("prefilter", "-")
    vm_rungs = "|".join(em.get("vm_rungs") or []) or "-"
    return {
        "engine": engine or "-",
        "entry": entry,
        "prefilter": prefilter,
        "vm_rungs": vm_rungs,
        "buffer_frames": em.get("buffer_frames", "-"),
        "buffer_trail": em.get("buffer_trail", "-"),
        "resume_frame_size": em.get("resume_frame_size", "-"),
    }


def _jitter_flag(median_ns, stddev_ns):
    """[B9] R9: 'stddev > median = timer jitter -- the median is the
    number' (pcrecdev1 feedback, repin (3): interp compile-cost variance
    12..109 us over 10 trials with no flag saying why)."""
    if median_ns is None or stddev_ns is None:
        return ""
    return "timer jitter" if stddev_ns > median_ns else ""


# ------------------------------------------------------------- [B9] R4 helper

def _form_fact(form):
    """[B9] R4: the FACT beside `form` -- `whole-subject` is, BY
    CONSTRUCTION (record_schema.md 5 ADDITIONS 3, enforced by rule X27:
    "a whole-subject match row must have a whole-subject compile row for
    its pattern"), a SECOND compiled artifact; `plain` is always the one
    ordinary artifact reached via a runtime flag. This restates `form`
    rather than performing a fresh lookup precisely because ADDITIONS 3
    makes the two facts coincide by definition -- a `form` value that
    disagreed with its own compile evidence would fail X27 before this
    module ever saw the record."""
    return "separate artifact" if form == "whole-subject" else "same program"


# ------------------------------------------------------------- [B9] R8 helpers

def _parse_testee_config(testee_id):
    """(engine_name, version_slug, config_slug) from a CONSTRUCTED
    testee_id (record_schema.md 6.4: `<engine>_<version>_<config>[_<extra>]`,
    each of the first two segments free of underscores by construction).
    Strips an `--all-records` date suffix (`@<compact-timestamp>`) first
    so cross-pin detection still works on a report that also asked for
    every record separately. Returns `None` for a testee_id that does
    not split into exactly three underscore-separated segments (an
    author-chosen `config_extra` making a fourth is deliberately still
    ONE config for this purpose -- `split(..., 2)` leaves it in the
    third piece)."""
    base = testee_id.split("@", 1)[0]
    parts = base.split("_", 2)
    if len(parts) != 3:
        return None
    return tuple(parts)


def _cross_pin_verdict(old_median, old_stddev, new_median, new_stddev):
    """[B9] R8: 'unchanged (within spread)' if the medians' difference is
    within max(stddev_old, stddev_new) x 2, else faster/slower xN.NN
    (ratio expressed so it always reads > 1x)."""
    if old_median is None or new_median is None:
        return None
    spread = max(old_stddev or 0.0, new_stddev or 0.0) * 2
    diff = new_median - old_median
    if abs(diff) <= spread:
        return "unchanged (within spread)"
    if new_median < old_median:
        ratio = (old_median / new_median) if new_median else float("inf")
        return f"faster ×{ratio:.2f}"
    ratio = (new_median / old_median) if old_median else float("inf")
    return f"slower ×{ratio:.2f}"


def _set_cell_failure_reason(red: "SetCellReduction"):
    """A one-word summary of why a SET cell was excluded, for the R8
    'now measured (was: <reason>)' verdict -- distinct from
    `_failure_label` (which reduces one SUBJECT's MatchCellReduction;
    this reduces the whole SetCellReduction's aggregate counts)."""
    if red.n_gave_up and red.n_wrong:
        return "gave-up+wrong"
    if red.n_gave_up:
        return "gave-up"
    if red.n_wrong:
        return "wrong"
    if red.n_subjects == 0:
        return "no-data"
    return "other"


def _worst_subject(rd: "ReportData", sb, testee_id, pattern_id, regime, form):
    """The subject with the highest median ns/call among `rd.match_cells`
    contributing to one (sb, testee, pattern, regime, form) SET cell --
    R8's per-cell 'worst subject' line, from the per-subject data (set
    grain only, per the brief)."""
    worst = None
    for (sb2, t2, p2, subj2, r2, f2), (_tid2, red) in rd.match_cells.items():
        if (sb2, t2, p2, r2, f2) != (sb, testee_id, pattern_id, regime, form):
            continue
        if red.median_ns is None:
            continue
        if worst is None or red.median_ns > worst[1]:
            worst = (subj2, red.median_ns)
    if worst is None:
        return None
    sid, ns = worst
    return sid, ns, rd.subject_bytes.get(sid)


def _cross_pin_info(rd: "ReportData", sb, pattern_id, regime, testee_id, form, red):
    """[B9] R8: if `testee_id` has an older same-(engine, config) sibling
    present in this report (a "previous pin"), return
    {'verdict': str, 'worst_note': str|None}; else `None`. SET grain
    only -- the brief: 'from the per-subject data; set grain only'."""
    if rd.grain != "set":
        return None
    parsed = _parse_testee_config(testee_id)
    if not parsed:
        return None
    engine, version, config = parsed
    my_ts = rd.record_ts_by_testee.get((sb, testee_id))

    older = []
    for (sb2, tid2), ts2 in rd.record_ts_by_testee.items():
        if sb2 != sb or tid2 == testee_id:
            continue
        p2 = _parse_testee_config(tid2)
        if not p2 or p2[0] != engine or p2[2] != config:
            continue
        if p2[1] == version:
            # Same version_slug -- e.g. two records of one identical pin
            # surfaced separately by --all-records. Not a cross-PIN pair
            # (record_schema.md 6.4: the version segment is what changed);
            # OD-B15's dedup/superseded machinery covers that case, not R8.
            continue
        if my_ts is not None and ts_key(ts2) >= ts_key(my_ts):
            continue
        older.append((ts2, tid2))
    if not older:
        return None
    older.sort(key=lambda pair: ts_key(pair[0]))
    prev_tid = older[-1][1]

    prev_cell = rd.set_cells.get((sb, prev_tid, pattern_id, regime, form))
    if prev_cell is None:
        return None
    _prev_tid2, prev_red = prev_cell

    if prev_red.expectation_failing:
        if red.expectation_failing:
            return None
        verdict = f"now measured (was: {_set_cell_failure_reason(prev_red)})"
    else:
        verdict = _cross_pin_verdict(prev_red.median_ns, prev_red.stddev_ns,
                                      red.median_ns, red.stddev_ns)
        if verdict is None:
            return None

    worst_note = None
    worst = _worst_subject(rd, sb, testee_id, pattern_id, regime, form)
    if worst:
        sid, ns, bts = worst
        b_str = f"{bts:,}" if bts is not None else "?"
        worst_note = (f"Δ detail: `{testee_id}` vs previous `{prev_tid}`: "
                       f"worst subject `{sid}`, {_fmt_ns(ns)} ns, {b_str} B")
    return {"verdict": verdict, "worst_note": worst_note}


def _floor_note_line():
    """[B9] R6: a per-call FLOOR control (pcrecdev1 feedback 1d/repin-2):
    no field carrying such a number exists in the schema today (checked
    against record_schema.md and record.schema.json, 2026-08-25) -- say
    so honestly rather than invent one. Update this the day a
    calibration/floor field lands."""
    return ("_floor: n/a (no floor pattern in this set yet -- "
            "pcrecdev1 feedback 1d/repin-2)_")


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
                             # selected records -- gates the 'form'/'fact' columns so a
                             # report over an all-plain store looks exactly as it did
                             # before v1.1
    # [B9] additions:
    status_by_testee: dict = field(default_factory=dict)   # (sb, testee_id) -> (status, status_detail, record_id)
    tier_by_testee: dict = field(default_factory=dict)      # (sb, testee_id) -> 'pinned'|'scratch'
    record_ts_by_testee: dict = field(default_factory=dict)  # (sb, testee_id) -> run.timestamp
    subject_bytes: dict = field(default_factory=dict)       # subject_id -> bytes_offered
    superseded: list = field(default_factory=list)          # [(kept_record_id, [superseded_record_ids])]
    include_unmeasured: bool = False
    include_scratch: bool = False
    all_records: bool = False
    subbench_alias_note: str | None = None


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

    # [B9] R2/OD-B15: dedup by (subbench@version, testee_id, machine_id),
    # newest `run.timestamp` wins by default; `--all-records` keeps every
    # record, each its own row (testee id suffixed when its group has
    # more than one record, so the common single-record case is
    # untouched).
    all_records = bool(getattr(args, "all_records", False))
    dup_groups = defaultdict(list)  # (sb, testee_id, machine_id) -> [(ts, r)]
    for r in valid:
        s = r.setup
        sb = s["subbench"]["id"] + "@" + str(s["subbench"]["version"])
        testee_id = s["testee"]["testee_id"]
        machine_id = s["environment"]["machine_id"]
        ts = s["run"]["timestamp"]
        dup_groups[(sb, testee_id, machine_id)].append((ts, r))

    effective_id_by_path = {}
    superseded = []
    dedup_valid = []
    for (sb, testee_id, _machine_id), entries in dup_groups.items():
        entries.sort(key=lambda te: ts_key(te[0]))
        if all_records:
            for ts, r in entries:
                dedup_valid.append(r)
                effective_id_by_path[r.path] = (
                    testee_id + "@" + _date_suffix(ts) if len(entries) > 1 else testee_id)
        else:
            _newest_ts, newest_r = entries[-1]
            dedup_valid.append(newest_r)
            effective_id_by_path[newest_r.path] = testee_id
            if len(entries) > 1:
                superseded.append((
                    newest_r.setup["record_id"],
                    [r.setup["record_id"] for _ts, r in entries[:-1]],
                ))
    valid = dedup_valid

    included = []
    subbench_versions = set()
    machines = set()
    schema_versions = set()
    forms_seen = set()
    status_by_testee = {}
    tier_by_testee = {}
    record_ts_by_testee = {}
    subject_bytes = {}
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
        testee_id = effective_id_by_path[r.path]
        record_id = s["record_id"]
        included.append((record_id, r.path))
        subbench_versions.add(sb)
        machines.add(s["environment"]["machine_id"])
        schema_versions.add(s["schema_version"])
        status_by_testee[(sb, testee_id)] = (
            s.get("status", "measured"), s.get("status_detail"), record_id)
        # [B9] R3: `tier` is an OPTIONAL schema v1.2 field lane b10loop is
        # adding (not yet in the validator this reporter shares) --
        # "absent = pinned" ahead of the schema landing it.
        tier_by_testee[(sb, testee_id)] = s.get("tier", "pinned")
        record_ts_by_testee[(sb, testee_id)] = s.get("run", {}).get("timestamp")
        for subj in s.get("subjects", []) or []:
            subject_bytes[subj["subject_id"]] = subj.get("bytes_offered")

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
        status_by_testee=status_by_testee,
        tier_by_testee=tier_by_testee,
        record_ts_by_testee=record_ts_by_testee,
        subject_bytes=subject_bytes,
        superseded=sorted(superseded),
        include_unmeasured=bool(getattr(args, "include_unmeasured", False)),
        include_scratch=bool(getattr(args, "include_scratch", False)),
        all_records=all_records,
        subbench_alias_note=getattr(args, "_subbench_alias_note", None),
    ), None


# -------------------------------------------------------------- rendering

def _fmt_ns(ns):
    if ns is None:
        return "-"
    return f"{ns:,.1f}"


def _is_reference(testee_setup_by_id, testee_id):
    # testee_id is CONSTRUCTED (record_schema.md 6.4): engine_libpcre2's
    # interp mode is spelled `libpcre2_<version>_interp-...`. Strip a
    # possible --all-records `@<timestamp>` suffix first.
    base = testee_id.split("@", 1)[0]
    return base.startswith("libpcre2_") and "_interp-" in base


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


def _status_lookup(rd: ReportData, sb, testee_id):
    return rd.status_by_testee.get((sb, testee_id), ("measured", None, None))


def _tier_lookup(rd: ReportData, sb, testee_id):
    return rd.tier_by_testee.get((sb, testee_id), "pinned")


def _excerpt(text, n=120):
    if not text:
        return ""
    text = str(text)
    return text[:n] + ("..." if len(text) > n else "")


def render_markdown(rd: ReportData):
    out = []
    out.append("# pcrec-bench report\n")
    out.append(f"reporter: {REPORTER_VERSION}\n")
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
    if rd.superseded:
        total_sup = sum(len(sups) for _kept, sups in rd.superseded)
        out.append(f"- superseded records (OD-B15: older duplicate of a (subbench@version, "
                    f"testee_id, machine); newest kept by default, `--all-records` shows each "
                    f"separately): {total_sup}")
        for kept, sups in rd.superseded:
            for sup in sups:
                out.append(f"    - `{sup}` superseded by `{kept}`")
    out.append(f"- sub-bench version(s): {', '.join(sorted(rd.subbench_versions)) or '(none)'}")
    out.append(f"- machine(s): {', '.join(sorted(rd.machines)) or '(none)'}")
    out.append(f"- schema version(s): {', '.join(sorted(rd.schema_versions)) or '(none)'}")
    if rd.subbench_alias_note:
        out.append(f"- {rd.subbench_alias_note}")
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
                    "separate compile with its own cost); `fact` restates "
                    "it as 'same program' / 'separate artifact' (R4)")
    out.append("- status policy (OD-B14): a ranking row whose record `status` "
                "is not `measured` is excluded from ranking by default, "
                "listed under its table as `not ranked: <testee> -- "
                "<status> (<status_detail excerpt>)`; `--include-unmeasured` "
                "ranks it instead, with `status` shown"
                + (" [ACTIVE]" if rd.include_unmeasured else ""))
    out.append("- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): "
                "a `scratch`-tier row is excluded from ranking by default, "
                "listed as `scratch: <testee>`; `--include-scratch` ranks "
                "it instead, with a `tier` column"
                + (" [ACTIVE]" if rd.include_scratch else ""))
    out.append("- duplicate-record policy (OD-B15): only the NEWEST record "
                "per (subbench@version, testee_id, machine) by "
                "`run.timestamp` ranks by default; `--all-records` shows "
                "every record as its own row, its testee id suffixed "
                "`@<timestamp>`"
                + (" [ACTIVE]" if rd.all_records else ""))
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
    not_ranked_rows = []  # (gkey, t, form, r, status, status_detail)
    scratch_rows = []     # (gkey, t, form, r, tier)

    for gkey in sorted(groups):
        entries = groups[gkey]
        sb = gkey[0]
        pattern_id = gkey[1]
        regime = gkey[-1]

        rankable = []
        group_failing = []
        group_not_ranked = []
        group_scratch = []
        for t, form, r in entries:
            status, status_detail, _rid = _status_lookup(rd, sb, t)
            tier = _tier_lookup(rd, sb, t)
            if r.expectation_failing or not getattr(r, "n_timed", r.n_trials):
                group_failing.append((t, form, r))
                continue
            if status != "measured" and not rd.include_unmeasured:
                group_not_ranked.append((t, form, r, status, status_detail))
                continue
            if tier == "scratch" and not rd.include_scratch:
                group_scratch.append((t, form, r, tier))
                continue
            rankable.append((t, form, r))

        for t, form, r in group_failing:
            excluded_cells.append((gkey, t, form, r))
        for item in group_not_ranked:
            not_ranked_rows.append((gkey,) + item)
        for item in group_scratch:
            scratch_rows.append((gkey,) + item)

        if not rankable:
            continue

        rankable.sort(key=lambda tfr: tfr[2].median_ns)
        ref = next((r for t, form, r in rankable if _is_reference(None, t)), None)
        ref_ns = ref.median_ns if ref else rankable[0][2].median_ns
        best_ns = rankable[0][2].median_ns
        any_partial = any(_partial_coverage(r) for _t, _f, r in entries)
        near_floor = grain == "set" and regime == "short-subject-search"

        if grain == "subject":
            _sb2, _pat2, subject_id, _reg2 = gkey
            title = f"### `{pattern_id}` / `{subject_id}` / `{regime}`"
        else:
            title = f"### `{pattern_id}` / `{regime}`"
        title += f" ({sb}) — baseline: {rd.reference_testee_pred}"
        out.append(title + "\n")

        facts_present = {_form_fact(form) for _t, form, _r in rankable}
        if len(facts_present) > 1:
            out.append("_rows compare different programs answering the same regime; "
                        "rank order is real, the ratio between forms is a regime "
                        "artifact until an end-anchored entry exists (pcrec "
                        "[OS-4])._\n")

        header = ["rank", "testee", "status"]
        if rd.show_form:
            header += ["form", "fact"]
        header += ["median ns/call", "min", "max", "stddev", "vs baseline", "vs best"]

        delta_by_testee = {}
        if grain == "set":
            for t, form, r in rankable:
                info = _cross_pin_info(rd, sb, pattern_id, regime, t, form, r)
                if info:
                    delta_by_testee[t] = info
        if delta_by_testee:
            header.append("Δ vs previous version")
        if near_floor:
            header += ["n subjects", "per-subject mean ns", "pass-rate"]
        elif any_partial:
            header += (["n subjects", "pass-rate"] if grain == "set" else ["n", "pass-rate"])
        if rd.include_scratch:
            header.append("tier")
        out.append("| " + " | ".join(header) + " |")
        out.append("|" + "|".join(["---"] * len(header)) + "|")

        worst_notes = []
        for i, (t, form, r) in enumerate(rankable, start=1):
            status, _detail, _rid = _status_lookup(rd, sb, t)
            tier = _tier_lookup(rd, sb, t)
            ratio_baseline = r.median_ns / ref_ns if ref_ns else float("nan")
            ratio_best = r.median_ns / best_ns if best_ns else float("nan")
            row = [str(i), f"`{t}`", status]
            if rd.show_form:
                row += [f"`{form}`", _form_fact(form)]
            row += [_fmt_ns(r.median_ns), _fmt_ns(r.min_ns), _fmt_ns(r.max_ns),
                    _fmt_ns(r.stddev_ns), f"{ratio_baseline:.3f}x", f"{ratio_best:.3f}x"]
            if delta_by_testee:
                info = delta_by_testee.get(t)
                row.append(info["verdict"] if info else "-")
                if info and info.get("worst_note"):
                    worst_notes.append(info["worst_note"])
            if near_floor:
                n, pr = _n_and_pass_rate(r, grain)
                mean = (r.median_ns / n) if n else None
                row += [str(n), _fmt_ns(mean), f"{pr*100:.0f}%"]
            elif any_partial:
                n, pr = _n_and_pass_rate(r, grain)
                row += [str(n), f"{pr*100:.0f}%"]
            if rd.include_scratch:
                row.append(tier)
            out.append("| " + " | ".join(row) + " |")
        out.append("")

        if near_floor:
            out.append(_floor_note_line())
            out.append("")

        if worst_notes:
            for note in worst_notes:
                out.append(f"- {note}")
            out.append("")

        if group_not_ranked:
            for t, form, r, status, status_detail in group_not_ranked:
                excerpt = _excerpt(status_detail)
                out.append(f"- not ranked: `{t}` — {status}"
                            + (f" ({excerpt})" if excerpt else ""))
            out.append("")
        if group_scratch:
            for t, form, r, tier in group_scratch:
                out.append(f"- scratch: `{t}` (tier={tier})")
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
                        _gave_up_cell_summary(r.failing_detail, rd.subject_bytes),
                        str(r.n_wrong), failing_list]
                out.append("| " + " | ".join(row) + " |")
        out.append("")

    out.append("## Compile cost (by execution-model class; never pooled across classes)\n")
    by_class = defaultdict(list)
    for (sb, testee_id, pattern_id, form), (t, r) in rd.compile_cells.items():
        by_class[r.cost_class].append((sb, pattern_id, testee_id, form, r))
    for cls in sorted(by_class):
        out.append(f"### `{cls}`\n")
        rows_for_class = by_class[cls]
        has_pcrec = any(t.split("@", 1)[0].startswith("pcrec_") for _sb, _p, t, _f, _r in rows_for_class)
        label = "median ns (derived: first-match-row-minus-steady-state)" \
            if rows_for_class[0][4].derived else "median total_ns"
        header = ["pattern"]
        if rd.show_form:
            header.append("form")
        header += ["testee", label, "min", "max", "stddev", "n costed", "jitter", "outcomes"]
        if has_pcrec:
            header += ["engine", "entry", "prefilter", "vm_rungs", "buffer_frames",
                       "buffer_trail", "resume_frame_size", "emit-c ns", "gcc ns", "load ns"]
        out.append("| " + " | ".join(header) + " |")
        out.append("|" + "|".join(["---"] * len(header)) + "|")
        for sb, pattern_id, testee_id, form, r in sorted(rows_for_class):
            outcomes = ", ".join(f"{k}={v}" for k, v in r.outcome_counts.items())
            row = [f"`{pattern_id}`"]
            if rd.show_form:
                row.append(f"`{form}`")
            row += [f"`{testee_id}`", _fmt_ns(r.median_ns), _fmt_ns(r.min_ns), _fmt_ns(r.max_ns),
                    _fmt_ns(r.stddev_ns), str(r.n_costed), _jitter_flag(r.median_ns, r.stddev_ns), outcomes]
            if has_pcrec:
                stamps = _mechanism_stamp_columns(r.sample_engine_metadata)
                pm = r.phase_medians or {}
                row += [str(stamps["engine"]), stamps["entry"], str(stamps["prefilter"]),
                        stamps["vm_rungs"], str(stamps["buffer_frames"]), str(stamps["buffer_trail"]),
                        str(stamps["resume_frame_size"]), _fmt_ns(pm.get("emit-c")),
                        _fmt_ns(pm.get("gcc")), _fmt_ns(pm.get("load"))]
            out.append("| " + " | ".join(row) + " |")
        out.append("")

    return "\n".join(out) + "\n"


def render_tsv(rd: ReportData):
    grain = rd.grain
    lines = []
    lines.append("# " + "; ".join(
        [f"reporter: {REPORTER_VERSION}",
         f"filters: {', '.join(rd.query_desc) or '(none)'}",
         f"source: {rd.source_desc}",
         f"records: {len(rd.included)}",
         f"excluded_invalid: {len(rd.excluded_invalid)}",
         f"superseded: {sum(len(v) for _k, v in rd.superseded)}",
         f"subbench_versions: {','.join(sorted(rd.subbench_versions))}",
         f"machines: {','.join(sorted(rd.machines))}",
         f"schema_versions: {','.join(sorted(rd.schema_versions))}",
         f"grain: {grain}",
         f"single_subject_regimes: {','.join(rd.single_subject_regimes)}",
         f"include_unmeasured: {rd.include_unmeasured}",
         f"include_scratch: {rd.include_scratch}",
         f"all_records: {rd.all_records}"]))
    header = ["section", "pattern", "subject_or_na", "regime_or_na", "form", "fact",
              "testee", "status", "tier", "rank_or_na", "metric", "value", "n", "pass_rate",
              "n_gave_up", "n_wrong", "gave_up_summary", "delta_verdict"]
    lines.append("\t".join(header))

    groups = _ranking_groups(rd, grain)
    for gkey in sorted(groups):
        if grain == "subject":
            sb, pattern_id, subject_id, regime = gkey
        else:
            sb, pattern_id, regime = gkey
            subject_id = "(set)"
        entries = groups[gkey]

        rankable = []
        others = []  # (t, form, r, section, status, tier)
        for t, form, r in entries:
            status, _detail, _rid = _status_lookup(rd, sb, t)
            tier = _tier_lookup(rd, sb, t)
            if r.expectation_failing or not getattr(r, "n_timed", r.n_trials):
                others.append((t, form, r, "excluded", status, tier))
                continue
            if status != "measured" and not rd.include_unmeasured:
                others.append((t, form, r, "not_ranked", status, tier))
                continue
            if tier == "scratch" and not rd.include_scratch:
                others.append((t, form, r, "scratch", status, tier))
                continue
            rankable.append((t, form, r, status, tier))
        rankable.sort(key=lambda x: x[2].median_ns)
        ref = next((r for t, form, r, _s, _ti in rankable if _is_reference(None, t)), None)
        ref_ns = ref.median_ns if ref else (rankable[0][2].median_ns if rankable else None)
        best_ns = rankable[0][2].median_ns if rankable else None
        for i, (t, form, r, status, tier) in enumerate(rankable, start=1):
            ratio_b = (r.median_ns / ref_ns) if ref_ns else float("nan")
            ratio_best = (r.median_ns / best_ns) if best_ns else float("nan")
            n, pr = _n_and_pass_rate(r, grain)
            fact = _form_fact(form)
            delta_verdict = ""
            if grain == "set":
                info = _cross_pin_info(rd, sb, pattern_id, regime, t, form, r)
                delta_verdict = info["verdict"] if info else ""
            for metric, val in (("median_ns", r.median_ns), ("min_ns", r.min_ns),
                                 ("max_ns", r.max_ns), ("stddev_ns", r.stddev_ns),
                                 ("ratio_vs_baseline", ratio_b), ("ratio_vs_best", ratio_best)):
                lines.append("\t".join(["rank", pattern_id, subject_id, regime, form, fact, t,
                                         status, tier, str(i), metric,
                                         f"{val:.6f}" if val is not None else "",
                                         str(n), f"{pr:.4f}", str(r.n_gave_up), str(r.n_wrong),
                                         "", delta_verdict]))
        for t, form, r, section, status, tier in others:
            n, pr = _n_and_pass_rate(r, grain)
            fact = _form_fact(form)
            gs = _gave_up_cell_summary(r.failing_detail, rd.subject_bytes) \
                if grain == "set" and hasattr(r, "failing_detail") else ""
            lines.append("\t".join([section, pattern_id, subject_id, regime, form, fact, t,
                                     status, tier, "", "pass_rate", f"{r.pass_rate:.4f}",
                                     str(n), f"{pr:.4f}", str(r.n_gave_up), str(r.n_wrong),
                                     gs, ""]))

    for (sb, testee_id, pattern_id, form), (t, r) in sorted(rd.compile_cells.items()):
        metric = "derived_first_match_row_minus_steady_state_ns" if r.derived else "median_total_ns"
        fact = _form_fact(form)
        lines.append("\t".join(["compile", pattern_id, "", "", form, fact, testee_id, "", "",
                                 "", metric, f"{r.median_ns:.6f}" if r.median_ns is not None else "",
                                 str(r.n_trials), "", "", "", "", ""]))
        jf = _jitter_flag(r.median_ns, r.stddev_ns)
        if jf:
            lines.append("\t".join(["compile", pattern_id, "", "", form, fact, testee_id, "", "",
                                     "", "jitter_flag", jf, "", "", "", "", "", ""]))

    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------- CLI

def build_argparser():
    ap = argparse.ArgumentParser(prog="pcrecbench report",
                                  description="Query the record store and "
                                              "render a comparison report "
                                              "(docs/design/requirements.md 8).")
    ap.add_argument("--store", default="store",
                     help="the store directory (default: ./store)")
    ap.add_argument("--subbench", help="filter: subbench.id equals this "
                                       "(OD-B13: the sub-bench DIRECTORY name "
                                       "under bench/, e.g. 'email', is also "
                                       "accepted and resolved via its own "
                                       "subbench.toml)")
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
    ap.add_argument("--include-unmeasured", action="store_true",
                     help="[B9] R1/OD-B14: rank rows whose record `status` "
                          "is not `measured` too (default: excluded from "
                          "ranking, listed as 'not ranked'), with their "
                          "status shown.")
    ap.add_argument("--all-records", action="store_true",
                     help="[B9] R2/OD-B15: show every record of a "
                          "(subbench@version, testee_id, machine) as its "
                          "own row (testee id suffixed by timestamp), "
                          "instead of the default newest-wins dedup.")
    ap.add_argument("--include-scratch", action="store_true",
                     help="[B9] R3: rank `tier: scratch` rows too (default: "
                          "excluded, listed as 'scratch'), with a `tier` "
                          "column.")
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

    args._subbench_alias_note = None
    if args.subbench:
        resolved, note = resolve_subbench_arg(args.subbench, REPO_ROOT)
        args.subbench = resolved
        args._subbench_alias_note = note

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
