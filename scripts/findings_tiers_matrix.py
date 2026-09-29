#!/usr/bin/env python3
"""findings_tiers_matrix.py -- [B115] the post-reduce ORACLE-BEST matrix
over one set's findings_tiers.sh scratch store (inbox I-118, outbox O-72
Q2). NOT a reporter change: it reads the SAME set-grain reduction the
reporter and `quick` already use (`pcrecbench.reduce.reduce_set_cell`),
never a second implementation of the arithmetic.

One row per (pattern, regime, form). Columns: DEFAULT, DECLARED-weblog,
DECLARED-log, PROFILED, ORACLE-BEST, oracle_best_arm (which sweep arm's
testee_id won the min), then three ratios (oracle-best/default,
declared/default, oracle-best/declared -- `declared` is DECLARED-weblog
when it exists, else DECLARED-log, else n/a). A cell that does not apply
prints `n/a:<reason>`; an arm whose record status is not `measured`, or
that gave a wrong/failing answer on any subject, is EXCLUDED from the
ORACLE-BEST minimum and flagged in a trailing `flags` column instead of
silently contributing a number that is not a real measurement.

USAGE

    python3 scripts/findings_tiers_matrix.py --store /var/tmp/b115/store \\
        --set loglines --out /tmp/loglines_matrix.tsv

The ARM -> testee_id mapping is read from `findings_tiers.sh --dry-run
--sets SET` (subprocess, no compile) rather than re-implemented here --
one arm list, in one shell function, is the whole point of committing
the sweep script in the first place; a second python copy of it would be
exactly the kind of drift this project's own CLAUDE.md files warn about.
"""
import argparse
import glob
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from pcrecbench import reduce as _reduce  # noqa: E402

SWEEP_PREFIX = "eng-"
DECLARED_PREFIXES = ("declared-",)
PROFILED_LABEL = "profiled"
DEFAULT_LABEL = "default"


def arm_testee_ids(set_name, extra_env=None):
    """-> {label: testee_id}, by running findings_tiers.sh --dry-run for
    exactly this one set (never any other -- SETS is set to just `set_name`
    so the dry run's arm list is this set's alone, matching arm_list()'s
    own per-set DECLARED/PROFILED membership)."""
    env = dict(os.environ)
    env["SETS"] = set_name
    if extra_env:
        env.update(extra_env)
    proc = subprocess.run(
        [os.path.join(HERE, "findings_tiers.sh"), "--dry-run"],
        cwd=ROOT, env=env, capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        raise RuntimeError("findings_tiers.sh --dry-run failed (rc=%d):\n%s"
                           % (proc.returncode, proc.stderr))
    out = {}
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) < 4 or parts[0] != set_name or "->" not in line:
            continue
        label = parts[1]
        tid = line.rsplit("->", 1)[1].strip()
        out[label] = tid
    return out


def newest_record_for_testee(store, set_name, testee_id):
    """-> path of the newest .jsonl under records/<set_name>@*/testee_id/,
    or None. Globs the version too (never assumes one) since a set's
    committed `subbench.toml` version is not this script's business."""
    pattern = os.path.join(store, "records", "%s@*" % set_name, testee_id, "*.jsonl")
    paths = sorted(glob.glob(pattern))
    return paths[-1] if paths else None


class ArmResult:
    __slots__ = ("label", "testee_id", "path", "status", "cells")

    def __init__(self, label, testee_id, path, status, cells):
        self.label = label
        self.testee_id = testee_id
        self.path = path
        self.status = status
        self.cells = cells  # {(pattern, regime, form): SetCell}


def load_arm(store, set_name, label, testee_id):
    path = newest_record_for_testee(store, set_name, testee_id)
    if path is None:
        return ArmResult(label, testee_id, None, "no-record", {})
    setup, rows = _reduce.read_record(path)
    status = setup.get("status", "unknown")
    grouped = _reduce.cells_from_record(rows)
    cells = {key: _reduce.reduce_set_cell(rows_by_subject)
             for key, rows_by_subject in grouped.items()}
    return ArmResult(label, testee_id, path, status, cells)


def arm_usable(arm, key):
    """-> True iff `arm`'s (pattern,regime,form) cell exists, the record's
    own status is `measured`, and the cell is not expectation-failing
    (n_subjects > 0, every subject agreeing) -- the three conditions the
    charter's "excluded from the min, flagged" rule names."""
    if arm.status != "measured":
        return False
    cell = arm.cells.get(key)
    if cell is None or cell.expectation_failing:
        return False
    return cell.median_ns is not None


def cell_display(arm, key):
    if arm.path is None:
        return "n/a:no-record"
    if arm.status != "measured":
        return "n/a:status=%s" % arm.status
    cell = arm.cells.get(key)
    if cell is None:
        return "n/a:no-cell"
    if cell.expectation_failing:
        if cell.failing_subjects:
            return "wrong-or-gaveup:%d-subjects" % len(cell.failing_subjects)
        return "n/a:no-subjects"
    return "%.1f" % cell.median_ns


def ratio(numer_arm, numer_key, denom_arm, denom_key):
    if not (arm_usable(numer_arm, numer_key) and arm_usable(denom_arm, denom_key)):
        return "n/a"
    d = denom_arm.cells[denom_key].median_ns
    if not d:
        return "n/a"
    return "%.4f" % (numer_arm.cells[numer_key].median_ns / d)


def build_matrix(store, set_name):
    arms_by_label = arm_testee_ids(set_name)
    if not arms_by_label:
        raise RuntimeError("no arms for set %r -- findings_tiers.sh --dry-run "
                           "returned nothing" % set_name)
    arms = {label: load_arm(store, set_name, label, tid)
            for label, tid in arms_by_label.items()}

    default_arm = arms.get(DEFAULT_LABEL)
    declared_arms = {lbl: a for lbl, a in arms.items()
                     if any(lbl.startswith(p) for p in DECLARED_PREFIXES)}
    profiled_arm = arms.get(PROFILED_LABEL)
    sweep_arms = {lbl: a for lbl, a in arms.items() if lbl.startswith(SWEEP_PREFIX)}

    all_keys = set()
    for a in arms.values():
        all_keys.update(a.cells.keys())

    header = ["pattern", "regime", "form", "DEFAULT"]
    declared_labels = sorted(declared_arms)
    header += ["DECLARED-%s" % lbl[len("declared-"):] for lbl in declared_labels]
    header += ["PROFILED", "ORACLE-BEST", "oracle_best_arm",
              "ratio_oracle_over_default", "ratio_declared_over_default",
              "ratio_oracle_over_declared", "flags"]
    rows = [header]

    for key in sorted(all_keys, key=lambda k: (k[0] or "", k[1] or "", k[2] or "")):
        pattern, regime, form = key
        default_val = (cell_display(default_arm, key) if default_arm
                       else "n/a:no-default-arm")
        declared_vals = [cell_display(declared_arms[lbl], key)
                         for lbl in declared_labels]
        profiled_val = (cell_display(profiled_arm, key) if profiled_arm
                        else "n/a:not-applicable")

        usable_sweep = [(lbl, a) for lbl, a in sweep_arms.items()
                        if arm_usable(a, key)]
        flags = []
        excluded_sweep = [lbl for lbl in sweep_arms if lbl not in
                          dict(usable_sweep)]
        if excluded_sweep:
            flags.append("excluded-from-min:%d-arms" % len(excluded_sweep))
        if usable_sweep:
            best_label, best_arm = min(
                usable_sweep, key=lambda kv: kv[1].cells[key].median_ns)
            oracle_val = "%.1f" % best_arm.cells[key].median_ns
            oracle_best_arm = best_label
            oracle_ratio = ratio(best_arm, key, default_arm, key) \
                if default_arm else "n/a"
        else:
            oracle_val, oracle_best_arm, oracle_ratio = "n/a:no-usable-arm", "", "n/a"

        # `declared` for the two cross-ratios is DECLARED-weblog when it
        # exists, else DECLARED-log, else n/a -- O-72's own tie order
        # (weblog is the real corpus; log is the fallback synthesized one).
        declared_arm_for_ratio = None
        for lbl in ("declared-weblog", "declared-log"):
            if lbl in declared_arms:
                declared_arm_for_ratio = declared_arms[lbl]
                break
        declared_over_default = (ratio(declared_arm_for_ratio, key,
                                       default_arm, key)
                                 if declared_arm_for_ratio and default_arm
                                 else "n/a")
        oracle_over_declared = "n/a"
        if declared_arm_for_ratio and usable_sweep:
            oracle_over_declared = ratio(best_arm, key,
                                         declared_arm_for_ratio, key)

        rows.append([pattern, regime or "", form] + [default_val] +
                    declared_vals + [profiled_val, oracle_val, oracle_best_arm,
                                     oracle_ratio, declared_over_default,
                                     oracle_over_declared, ";".join(flags)])
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--store", required=True)
    ap.add_argument("--set", required=True, dest="set_name")
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)

    rows = build_matrix(os.path.abspath(args.store), args.set_name)
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write("# [B115] findings_tiers_matrix.py -- set=%s store=%s\n"
               % (args.set_name, args.store))
        for row in rows:
            f.write("\t".join(str(c) for c in row) + "\n")
    print("findings_tiers_matrix: %d row(s) -> %s" % (len(rows) - 1, args.out))


if __name__ == "__main__":
    main()
