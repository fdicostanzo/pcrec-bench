#!/usr/bin/env python3
"""probe_kb27_no_expectation.py -- KB-27 (docs/dev/known_issues.md): a READ
of pinned records only (no compile, no run, no timing) over
`store/records/capability@0.1/*/*.jsonl`, for the two (pattern, subject)
pairs `bench/capability/NOTES.md` records as DROPPED at oracle derivation
(an oracle GIVE-UP, never a real answer): `evil-alt-nested` x
`rd-evil-alt-near-miss` and `evil-alt-nested` x `sd-empty-alt-hit`
(regime `short-subject-search`).

For every testee that carries a row for either pair, on every trial:

  1. prints the RAW `match_outcome` + `diagnostic` exactly as the record
     carries it -- proving the store never fabricates a wrong verdict;
  2. computes n_wrong the OLD way (`sum(outcome_counts.get(o, 0) for o in
     WRONG_ANSWER_OUTCOMES)`, reduce.py's own formula before this fix,
     reproduced here literally rather than re-imported so this file stays
     a snapshot of the BEFORE state even after reduce.py changes again)
     against the SAME rows run through the CURRENT (fixed) `reduce.
     reduce_match_cell`, and the `_matrix_cell`-equivalent status token
     each would render.

Confirms, from the real records rather than by inference: every pcrec
config that GENUINELY GAVE UP on these two cells reads `gave-up` in both
the OLD and NEW reduction (unaffected -- `outcome_for`'s give-up branch
never reaches the `expectation is None` one); every testee that does NOT
give up (`pcrec-auto-nocaps` at every pin, `oniguruma`, `re2`, `tre`,
`rust-default`, `libpcre2-*`, `vectorscan`) reads `wrong` under the OLD
formula and `no-expectation` under the NEW one, on the SAME raw rows.

Run from the repo root: `python3 docs/dev/measurements/probe_kb27_no_expectation.py`
"""
import glob
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, REPO_ROOT)

from pcrecbench import reduce  # noqa: E402

PATTERN = "evil-alt-nested"
SUBJECTS = ("rd-evil-alt-near-miss", "sd-empty-alt-hit")
REGIME = "short-subject-search"

# reduce.py's OLD formula (pre-KB-27): n_wrong summed WRONG_ANSWER_OUTCOMES
# with no subtraction. Reproduced literally (not imported) so this probe
# keeps demonstrating the BEFORE/AFTER contrast even after reduce.py
# changes again.
_OLD_WRONG_ANSWER_OUTCOMES = frozenset({
    "did-not-match-as-expected", "wrong-span-or-captures", "truncated-subject",
})


def old_n_wrong(rows):
    outcome_counts = Counter(r.get("match_outcome") for r in rows)
    return sum(outcome_counts.get(o, 0) for o in _OLD_WRONG_ANSWER_OUTCOMES)


def old_matrix_token(rows):
    """The `_matrix_cell` fallback chain as it stood before KB-27 (wrong
    checked before gave-up; no third bucket)."""
    outcome_counts = Counter(r.get("match_outcome") for r in rows)
    n_gave_up = outcome_counts.get("gave-up", 0)
    n_wrong = old_n_wrong(rows)
    if n_wrong > 0:
        return "wrong"
    if n_gave_up > 0:
        return "gave-up"
    return "excluded"


def new_matrix_token(red):
    if red.n_wrong > 0:
        return "wrong"
    if red.n_gave_up > 0:
        return "gave-up"
    if red.n_no_expectation > 0:
        return "no-expectation"
    return "excluded"


def main():
    root = os.path.join(REPO_ROOT, "store", "records", "capability@0.1")
    testee_dirs = sorted(d for d in glob.glob(os.path.join(root, "*")) if os.path.isdir(d))
    print("KB-27 probe: %s x %s (regime=%s)" % (PATTERN, SUBJECTS, REGIME))
    print("store root: %s" % os.path.relpath(root, REPO_ROOT))
    print()
    for subject in SUBJECTS:
        print("=" * 78)
        print("subject: %s" % subject)
        print("=" * 78)
        for tdir in testee_dirs:
            testee_id = os.path.basename(tdir)
            files = sorted(glob.glob(os.path.join(tdir, "*.jsonl")))
            if not files:
                continue
            # newest record only (mirrors the reporter's own dedup rule --
            # this probe is a read, not a ranking, but one record per
            # testee is the honest population to show).
            path = files[-1]
            rows = []
            with open(path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    if (rec.get("kind") == "match"
                            and rec.get("pattern_id") == PATTERN
                            and rec.get("subject_id") == subject
                            and rec.get("regime") == REGIME):
                        rows.append(rec)
            if not rows:
                continue
            outcomes = sorted({r.get("match_outcome") for r in rows})
            diag = rows[0].get("diagnostic")
            red = reduce.reduce_match_cell(rows)
            print("  %-45s n=%d outcome=%s" % (testee_id, len(rows), outcomes))
            print("      diagnostic (trial 1): %r" % (diag,))
            print("      OLD: n_wrong=%d  token=%s"
                  % (old_n_wrong(rows), old_matrix_token(rows)))
            print("      NEW: n_wrong=%d  n_gave_up=%d  n_no_expectation=%d  token=%s"
                  % (red.n_wrong, red.n_gave_up, red.n_no_expectation, new_matrix_token(red)))
        print()


if __name__ == "__main__":
    main()
