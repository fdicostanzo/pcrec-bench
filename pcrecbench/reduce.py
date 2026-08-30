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
arithmetic over raw trials, the only place it is allowed to live -- with
ONE argued exception (v1.4, [B20]): `judge_trial_agreement` below is the
harness's derivation of the `trial_agreement` setup block, COUNTS under a
recomputation rule (record_schema.md X32), never a time. It is the ONE
derivation the harness stamps with, the reporter renders from and `quick`
prints from (docs/design/gate_shape_v14.md 5 H4); schema/validate.py
carries a deliberate SECOND implementation of the same 3.5 arithmetic
(no shared source) and X32 compares the two on integer counts.
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


# ---------------------------------------------------- trial agreement (v1.4)
#
# docs/design/gate_shape_v14.md 3.2-3.5: the rule `v1.4-group`. Per judged
# ROW (pattern, regime, form, subject) with m the median of its per-trial
# ns/iter: `slow` = trials strictly above k*m, `fast` = 1 iff the minimum
# is strictly below m/k; the row DISAGREES iff slow >= 2 or fast == 1, or
# it is a MIXED row (a `timed-out` trial beside >= 1 timed trial). Per
# GROUP (pattern, regime, form) with n judged rows and d disagreeing ones:
# the group DISAGREES iff d >= d_min and share_c * d >= n. The record
# disagrees iff >= 1 group does -- provided its trial count is >= 5 and
# odd; otherwise `n/a-trials` and nothing is judged. Constants MEASURED
# over the store's 68 records (the census files under
# docs/dev/measurements/): k = 1.5, d_min = 2, share_c = 3.

TRIAL_AGREEMENT_RULE = "v1.4-group"
TRIAL_AGREEMENT_K = 1.5
TRIAL_AGREEMENT_D_MIN = 2
TRIAL_AGREEMENT_SHARE_C = 3
TRIAL_AGREEMENT_MIN_TRIALS = 5

TIMED_OUT = "timed-out"


def _row_key(r):
    return (r.get("pattern_id"), r.get("regime"), r.get("form") or "plain",
            r.get("subject_id"))


def _ns_per_iter_judged(r):
    """A TRIAL is timed for the rule iff `matched-as-expected` AND
    `timing.iterations > 1` (3.5) -- stricter than `ns_per_call`, which
    accepts a one-iteration loop the ranking may still use."""
    t = r.get("timing") or {}
    it = t.get("iterations")
    if r.get("match_outcome") != MATCHED or not isinstance(it, int) or it <= 1:
        return None
    return t["elapsed_ns"] / it


def judge_trial_agreement(rows, k=TRIAL_AGREEMENT_K, d_min=TRIAL_AGREEMENT_D_MIN,
                          share_c=TRIAL_AGREEMENT_SHARE_C):
    """-> the `trial_agreement` block (record_schema.md 8, v1.4) for a
    record's rows (compile rows are ignored). Every number in it is
    recomputable from the rows by X32's independent implementation."""
    match = [r for r in rows if r.get("kind") == "match"]
    by_key = {}
    for r in match:
        by_key.setdefault(_row_key(r), []).append(r)
    trials = max((int(r.get("trial") or 0) for r in match), default=0)
    block = {
        "rule": TRIAL_AGREEMENT_RULE,
        "k": k, "d_min": d_min, "share_c": share_c,
        "trials": trials,
        "groups_judged": 0, "groups_disagreeing": 0,
        "rows_judged": 0, "rows_disagreeing": 0,
        "rows_unjudged": 0,
        "rows_unjudged_reasons": {"few_timed_trials": 0, "all_timed_out": 0,
                                  "na_trials": 0},
        "worst_group": None,
        "verdict": "n/a-trials",
    }
    reasons = block["rows_unjudged_reasons"]
    if trials < TRIAL_AGREEMENT_MIN_TRIALS or trials % 2 == 0:
        block["rows_unjudged"] = len(by_key)
        reasons["na_trials"] = len(by_key)
        return block

    class Group:
        __slots__ = ("n", "d", "min_seq")

        def __init__(self):
            self.n = self.d = 0
            self.min_seq = None

    groups = {}
    for key, krows in by_key.items():
        timed = {r.get("trial"): v for r in krows
                 for v in (_ns_per_iter_judged(r),) if v is not None}
        n_timed_out = sum(1 for r in krows if r.get("match_outcome") == TIMED_OUT)
        if n_timed_out >= 1 and timed:
            disagreeing = True          # a MIXED row: the alarm hit some passes
        elif n_timed_out == len(krows):
            block["rows_unjudged"] += 1  # every trial timed out: the engine's answer
            reasons["all_timed_out"] += 1
            continue
        elif len(timed) >= 2:
            xs = [timed[t] for t in sorted(timed)]
            m = statistics.median(xs)
            slow = sum(1 for x in xs if x > k * m)
            fast = 1 if min(xs) < m / k else 0
            disagreeing = slow >= 2 or fast == 1
        else:
            block["rows_unjudged"] += 1
            reasons["few_timed_trials"] += 1
            continue
        block["rows_judged"] += 1
        g = groups.setdefault(key[:3], Group())
        g.n += 1
        if disagreeing:
            block["rows_disagreeing"] += 1
            g.d += 1
        for r in krows:
            sq = r.get("seq")
            if isinstance(sq, int) and (g.min_seq is None or sq < g.min_seq):
                g.min_seq = sq
    block["groups_judged"] = len(groups)
    block["groups_disagreeing"] = sum(
        1 for g in groups.values() if g.d >= d_min and share_c * g.d >= g.n)
    if groups:
        worst_key, worst = max(
            groups.items(),
            key=lambda kv: (kv[1].d, -kv[1].n,
                            -(kv[1].min_seq if kv[1].min_seq is not None else 0)))
        block["worst_group"] = {"pattern_id": worst_key[0], "regime": worst_key[1],
                                "form": worst_key[2], "d": worst.d, "n": worst.n}
    block["verdict"] = "disagree" if block["groups_disagreeing"] >= 1 else "agree"
    return block


def agreement_line(block):
    """The ONE rendering of a block the harness, `quick` and the reporter
    share: `agree (0 of 6 groups; 0 of 30 rows; 0 unjudged; k=1.5, 2/3;
    5 trials)` / `disagree (1 of 72 groups; worst <group> d=23 of n=30)` /
    `agree 0/0 groups -- nothing judged (N rows unjudged)` / `n/a (3
    trials)`; `N rows unjudged (M all-timed-out)` whenever any row was
    (gate_shape_v14.md 6 R4)."""
    v = block.get("verdict")
    if v == "n/a-trials":
        return "n/a (%d trials)" % block.get("trials", 0)
    unj = block.get("rows_unjudged", 0)
    ato = (block.get("rows_unjudged_reasons") or {}).get("all_timed_out", 0)
    unj_s = "%d unjudged" % unj + (" (%d all-timed-out)" % ato if ato else "")
    if v == "disagree":
        wg = block.get("worst_group") or {}
        return ("disagree (%d of %d groups; worst %s / %s / %s d=%d of n=%d; %s)"
                % (block["groups_disagreeing"], block["groups_judged"],
                   wg.get("pattern_id"), wg.get("regime"), wg.get("form"),
                   wg.get("d", 0), wg.get("n", 0), unj_s))
    if block.get("groups_judged", 0) == 0:
        return "agree 0/0 groups -- nothing judged (%d rows unjudged)" % unj
    return ("agree (%d of %d groups; %d of %d rows; %s; k=%s, %d/%d; %d trials)"
            % (block["groups_disagreeing"], block["groups_judged"],
               block["rows_disagreeing"], block["rows_judged"], unj_s,
               block.get("k"), block.get("d_min", 0), block.get("share_c", 0),
               block.get("trials", 0)))
