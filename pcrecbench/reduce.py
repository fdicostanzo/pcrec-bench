"""reduce.py -- the SET-GRAIN reduction, shared by `quick` and the reporter.

Rule R5 of [B10] (Frank's I-4 (b)): the comparable `pcrecbench quick` prints
inline must be the SAME arithmetic the reporter uses, or a loop that watches
one number and a report that ranks another will disagree about what "faster"
means. So the arithmetic lives here, once, and both import it:

    from pcrecbench.reduce import reduce_set_cell, cells_from_record

THE SET-GRAIN COMPARABLE (the reporter's `--grain set`, manager change
request 2026-08-25, `pcrecbench/report.py`'s docstring):

  * per row, the comparable is `elapsed_ns / iterations` -- nanoseconds per
    CALL. Raw `elapsed_ns` is not comparable across testees because each
    calibrates its own `iterations`;
  * per TRIAL, sum that over every subject of the set -- "time to process
    the whole set once per call-set";
  * over trials, median / min / max / population stddev of those sums;
  * a subject whose cell is expectation-failing (any trial not
    `matched-as-expected`) FAILS THE SET: the set cell carries no number,
    and the failing subjects are listed with their own reductions rather
    than averaged away. `gave-up` (the engine's OWN limit) is counted apart
    from wrong answers everywhere.

This module deliberately mirrors `report.py`'s `reduce_set_cell` field for
field (that lane owns `report.py`; the manager will point it here), so the
hand-computed fixture in tools/selfcheck.py -- 3 trials x 2 subjects, whose
median you can do in your head -- pins the arithmetic both surfaces share.

No statistics enter a RECORD (record_schema.md 10.3); this is READER-side
arithmetic over raw trials, the only place it is allowed to live.
"""

import re
import statistics
from collections import Counter

#: `match_outcome` values meaning "the engine ANSWERED, and the answer
#: disagreed with the expectation" -- as opposed to `gave-up` (the engine's
#: own resource limit) and the hazard outcomes `crashed` / `timed-out`.
WRONG_ANSWER_OUTCOMES = frozenset({
    "did-not-match-as-expected", "wrong-span-or-captures", "truncated-subject",
})

MATCHED = "matched-as-expected"

_GIVEUP_RE = re.compile(r"giveup:(-?\d+)(?::([A-Za-z0-9_]+))?")


def _pstdev(values):
    return statistics.pstdev(values) if len(values) > 1 else 0.0


def ns_per_call(row):
    """The per-row comparable, or None when the row carries no usable timing
    (an untimed outcome, or `iterations` absent/zero)."""
    t = row.get("timing") or {}
    it = t.get("iterations")
    if row.get("match_outcome") != MATCHED or not it:
        return None
    return t["elapsed_ns"] / it


def giveup_code(row):
    """The engine's give-up CODE from a `gave-up` row's diagnostic --
    `giveup:-3:PCREC_ERR_FRAMES` -> `-3:PCREC_ERR_FRAMES`, the driver
    protocol's spelling (adapters.py) as the harness copied it into
    `diagnostic`. A `gave-up` row whose diagnostic does not carry the
    protocol token yields the diagnostic itself, truncated: the record is
    schema-valid without the token (X-rules require a non-empty diagnostic,
    not a shape), so this never raises."""
    if row.get("match_outcome") != "gave-up":
        return None
    diag = str(row.get("diagnostic") or "")
    m = _GIVEUP_RE.search(diag)
    if m:
        return m.group(1) + (":" + m.group(2) if m.group(2) else "")
    return diag[:64] or "(no code)"


class MatchCell:
    """One (pattern, subject, regime, form) cell's reduction over its trials.
    Field names match `report.py`'s MatchCellReduction."""

    __slots__ = ("n_trials", "n_timed", "median_ns", "min_ns", "max_ns",
                 "stddev_ns", "iters", "outcome_counts", "pass_rate",
                 "n_gave_up", "n_wrong", "giveup_codes")

    def __init__(self, **kw):
        for k in self.__slots__:
            setattr(self, k, kw.get(k))

    @property
    def expectation_failing(self):
        return self.n_trials == 0 or self.pass_rate < 1.0


def reduce_match_cell(rows):
    """Reduce one subject's rows (every trial of one (pattern, subject,
    regime, form)) -- the per-subject half the set grain is built from."""
    total = len(rows)
    outcome_counts = Counter(r.get("match_outcome") for r in rows)
    ns = [v for v in (ns_per_call(r) for r in rows) if v is not None]
    iters = sorted({r["timing"]["iterations"] for r in rows
                    if ns_per_call(r) is not None})
    n = len(ns)
    codes = Counter(c for c in (giveup_code(r) for r in rows) if c)
    return MatchCell(
        n_trials=total, n_timed=n,
        median_ns=statistics.median(ns) if n else None,
        min_ns=min(ns) if n else None,
        max_ns=max(ns) if n else None,
        stddev_ns=_pstdev(ns) if n else None,
        iters=iters,
        outcome_counts=dict(sorted(outcome_counts.items())),
        pass_rate=(outcome_counts.get(MATCHED, 0) / total) if total else 0.0,
        n_gave_up=outcome_counts.get("gave-up", 0),
        n_wrong=sum(outcome_counts.get(o, 0) for o in WRONG_ANSWER_OUTCOMES),
        giveup_codes=dict(codes),
    )


def _timed_ns_by_trial(rows):
    out = {}
    for r in rows:
        v = ns_per_call(r)
        if v is not None:
            out[r.get("trial")] = v
    return out


class SetCell:
    """The set-grain reduction for one (pattern, regime, form, testee).
    Field names match `report.py`'s SetCellReduction, plus `giveup_codes`
    (code -> count over the whole set) and `n_rows`."""

    __slots__ = ("n_subjects", "n_agreeing", "pass_rate", "failing_subjects",
                 "failing_detail", "n_trials", "n_gave_up", "n_wrong",
                 "median_ns", "min_ns", "max_ns", "stddev_ns", "giveup_codes",
                 "n_rows", "sums")

    def __init__(self, **kw):
        for k in self.__slots__:
            setattr(self, k, kw.get(k))

    @property
    def expectation_failing(self):
        return self.n_subjects == 0 or self.pass_rate < 1.0


def reduce_set_cell(rows_by_subject):
    """`rows_by_subject`: {subject_id: [match rows]} for ONE (sub-bench,
    testee, pattern, regime, form). -> SetCell.

    A subject fails if its own reduce_match_cell() is expectation-failing;
    if ANY subject fails, the whole set cell is excluded (no number) and the
    failing subjects are recorded, each with its own reduction, so a caller
    can tell a `gave-up` failure from a wrong-answer one. Otherwise, per
    trial number COMMON to every subject, sum the per-subject ns/call, then
    reduce over those per-trial sums. `sums` keeps the per-trial sums (in
    trial order) so a caller can show its work."""
    n_subjects = len(rows_by_subject)
    per_subject = {sid: reduce_match_cell(rows)
                   for sid, rows in rows_by_subject.items()}
    failing = sorted(sid for sid, red in per_subject.items()
                     if red.expectation_failing)
    n_agreeing = n_subjects - len(failing)
    pass_rate = (n_agreeing / n_subjects) if n_subjects else 0.0
    n_gave_up = sum(red.n_gave_up for red in per_subject.values())
    n_wrong = sum(red.n_wrong for red in per_subject.values())
    codes = Counter()
    for red in per_subject.values():
        codes.update(red.giveup_codes)
    n_rows = sum(len(rows) for rows in rows_by_subject.values())
    base = dict(n_subjects=n_subjects, n_agreeing=n_agreeing,
                pass_rate=pass_rate, n_gave_up=n_gave_up, n_wrong=n_wrong,
                giveup_codes=dict(codes), n_rows=n_rows)

    if failing or not n_subjects:
        return SetCell(failing_subjects=failing,
                       failing_detail={sid: per_subject[sid] for sid in failing},
                       n_trials=0, median_ns=None, min_ns=None, max_ns=None,
                       stddev_ns=None, sums=[], **base)

    per_trial = {sid: _timed_ns_by_trial(rows)
                 for sid, rows in rows_by_subject.items()}
    trial_sets = [set(d) for d in per_trial.values()]
    common = sorted(set.intersection(*trial_sets)) if trial_sets else []
    sums = [sum(per_trial[sid][t] for sid in rows_by_subject) for t in common]
    n = len(sums)
    return SetCell(failing_subjects=[], failing_detail={}, n_trials=n,
                   median_ns=statistics.median(sums) if n else None,
                   min_ns=min(sums) if n else None,
                   max_ns=max(sums) if n else None,
                   stddev_ns=_pstdev(sums) if n else None,
                   sums=sums, **base)


# ---------------------------------------------------------- from a record

def cells_from_record(rows):
    """Group a record's match rows into set cells:
    {(pattern_id, regime, form): {subject_id: [rows]}}. `form` absent reads
    as `plain` (record_schema.md 5)."""
    out = {}
    for r in rows:
        if r.get("kind") != "match":
            continue
        key = (r.get("pattern_id"), r.get("regime"), r.get("form", "plain"))
        out.setdefault(key, {}).setdefault(r.get("subject_id"), []).append(r)
    return out


def read_record(path):
    """(setup, rows) of a record file. The caller validates it first if it
    cares (store.write already did, for anything the harness wrote)."""
    import json
    with open(path, "r", encoding="utf-8") as f:
        lines = [ln for ln in f.read().split("\n") if ln.strip()]
    setup = json.loads(lines[0])
    rows = [json.loads(ln) for ln in lines[1:]]
    return setup, rows
