#!/usr/bin/env python3
"""probe_trial_agreement.py -- the TRIAL-AGREEMENT CENSUS over the store
([B20], schema v1.4: the constants of the `inconclusive-spread` rule are
MEASURED from every pinned record before one is chosen).

Reads PINNED RECORDS (never measures anything). For every timed match row
group -- one (pattern, regime, form, subject) with `timing.iterations > 1`
and at least two timed trials -- it computes:

  * the per-trial ns/iteration and the row MEDIAN over its trials;
  * for k in K_LIST: the number of trials STRICTLY ABOVE k x median (the
    slow outliers), and whether the MIN trial is below median / k (a fast
    outlier -- a burst can only add time, so this is expected ~0);
  * the index of the slowest trial when the row has >= 1 slow outlier at
    k = 1.5 (the warm-up question: is it always trial 1?).

Per record it prints, for each k: rows judged, rows with >= 1 and with
>= 2 slow outliers (count and fraction), rows with a fast outlier, rows
DISAGREEING (>= 2 slow OR a fast outlier -- the v1.4 rule's row verdict),
every disagreeing row in full at k in LIST_K, and the WORST row by
>= 2-count then by max/median. The summary at the end gives,
per k, the distribution over records of the >= 2 fraction (the number the
v1.4 rule judges), and per k the worst record.

D35 rules (docs/dev/measurements/CLAUDE.md): stable name, verbatim output,
the source header below, NEVER a ranking input (nothing here is a record;
no schema, no store write, no reporter).

    python3 docs/dev/measurements/probe_trial_agreement.py            # store/records/*/*/*.jsonl
    python3 docs/dev/measurements/probe_trial_agreement.py PATH...    # explicit records
"""
import glob
import json
import os
import statistics
import subprocess
import sys
import time
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))  # measurements -> dev -> docs -> repo root
K_LIST = (1.25, 1.5, 2.0)
LIST_K = (1.25, 1.5)   # the k values whose disagreeing rows are listed in full


def header(paths):
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                                capture_output=True, text=True).stdout.strip()
    except OSError:
        commit = "unknown"
    with open("/proc/loadavg") as fh:
        load = fh.read().strip()
    print("== probe_trial_agreement.py -- run %s"
          % time.strftime("%Y-%m-%dT%H:%M:%S%z"))
    print("bench commit %s; records read only; load at run: %s"
          % (commit, load))
    print("k values: %s; slow outlier = trial ns/iter STRICTLY ABOVE k x row "
          "median; fast outlier = min trial BELOW row median / k"
          % " ".join(str(k) for k in K_LIST))
    print("rows judged: kind match, matched-as-expected, timing.iterations > 1, "
          ">= 2 timed trials; grouped by (pattern, regime, form, subject)")
    print("records: %d" % len(paths))
    print()


def read_record(path):
    with open(path, "r", encoding="utf-8") as fh:
        lines = [ln for ln in fh.read().split("\n") if ln.strip()]
    return json.loads(lines[0]), [json.loads(ln) for ln in lines[1:]]


def timed_rows(rows):
    groups = {}
    for r in rows:
        if r.get("kind") != "match":
            continue
        t = r.get("timing") or {}
        it = t.get("iterations") or 0
        if r.get("match_outcome") != "matched-as-expected" or it <= 1:
            continue
        key = (r["pattern_id"], r["regime"], r.get("form", "plain"),
               r["subject_id"])
        groups.setdefault(key, {})[int(r["trial"])] = t["elapsed_ns"] / it
    return {k: v for k, v in groups.items() if len(v) >= 2}


def judge_record(groups):
    """-> per-k stats plus the trial-count census and the odd-trial hist."""
    out = {k: {"rows": 0, "ge1": 0, "ge2": 0, "fast": 0, "dis": 0,
               "worst": None, "listing": []} for k in K_LIST}
    ntrials = Counter()
    odd_hist = Counter()
    for key, by_trial in sorted(groups.items()):
        vals = [by_trial[t] for t in sorted(by_trial)]
        med = statistics.median(vals)
        ntrials[len(vals)] += 1
        ratio_max = max(vals) / med if med else float("inf")
        for k in K_LIST:
            st = out[k]
            st["rows"] += 1
            slow = sum(1 for v in vals if v > k * med)
            fast = 1 if min(vals) < med / k else 0
            st["ge1"] += 1 if slow >= 1 else 0
            st["ge2"] += 1 if slow >= 2 else 0
            st["fast"] += fast
            st["dis"] += 1 if (slow >= 2 or fast) else 0
            if slow >= 2 or fast:
                st["listing"].append((slow, fast, key, vals))
            cand = (slow, ratio_max, key, vals)
            if st["worst"] is None or cand[:2] > st["worst"][:2]:
                st["worst"] = cand
            if k == 1.5 and slow >= 1:
                odd = sorted(by_trial)[vals.index(max(vals))]
                odd_hist[odd] += 1
    return out, ntrials, odd_hist


def fmt_row(key, vals):
    return "%s / %s / %s / %s: %s" % (
        key[0], key[1], key[2], key[3],
        " ".join("%.1f" % v for v in vals))


def main(argv):
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        paths = sorted(glob.glob(os.path.join(REPO, "store", "records",
                                              "*", "*", "*.jsonl")))
    header(paths)
    summary = {k: [] for k in K_LIST}
    trial_census = Counter()
    odd_total = Counter()
    for p in paths:
        setup, rows = read_record(p)
        groups = timed_rows(rows)
        stats, ntrials, odd_hist = judge_record(groups)
        trial_census.update(ntrials)
        odd_total.update(odd_hist)
        rid = setup["record_id"]
        print("-- %s" % rid)
        print("   schema %s  status %s  tier %s  trials/row %s"
              % (setup["schema_version"], setup["status"],
                 setup.get("tier", "(absent)"),
                 " ".join("%d:%d" % (n, c) for n, c in sorted(ntrials.items()))))
        for k in K_LIST:
            st = stats[k]
            n = st["rows"]
            f1 = st["ge1"] / n if n else 0.0
            f2 = st["ge2"] / n if n else 0.0
            ff = st["fast"] / n if n else 0.0
            fd = st["dis"] / n if n else 0.0
            print("   k=%-4s rows %5d  >=1 slow %5d (%6.2f%%)  >=2 slow %4d "
                  "(%6.2f%%)  fast %3d (%5.2f%%)  disagreeing (>=2 slow OR "
                  "fast) %4d (%6.2f%%)"
                  % (k, n, st["ge1"], 100 * f1, st["ge2"], 100 * f2,
                     st["fast"], 100 * ff, st["dis"], 100 * fd))
            summary[k].append((f2, st["ge2"], n, rid, f1, ff, fd, st["dis"]))
            if k in LIST_K and st["listing"]:
                for slow, fast, key, vals in st["listing"]:
                    print("      k=%s disagreeing row: slow=%d fast=%d  %s"
                          % (k, slow, fast, fmt_row(key, vals)))
        w = stats[1.5]["worst"]
        if w:
            print("   worst row @k=1.5: slow=%d max/median=%.2f  %s"
                  % (w[0], w[1], fmt_row(w[2], w[3])))
        if odd_hist:
            print("   slowest-trial index over rows with >=1 slow @k=1.5: %s"
                  % " ".join("t%d:%d" % (t, c) for t, c in sorted(odd_hist.items())))
        print()

    print("== SUMMARY over %d records" % len(paths))
    print("trials per row, census: %s"
          % " ".join("%d trials: %d rows" % (n, c)
                     for n, c in sorted(trial_census.items())))
    print("slowest-trial index over all rows with >=1 slow @k=1.5: %s"
          % " ".join("t%d:%d" % (t, c) for t, c in sorted(odd_total.items())))
    print()
    for k in K_LIST:
        rows = summary[k]
        f2s = sorted(x[0] for x in rows)
        f1s = sorted(x[4] for x in rows)
        ffs = sorted(x[5] for x in rows)
        fds = sorted(x[6] for x in rows)
        tot_rows = sum(x[2] for x in rows)
        tot_ge2 = sum(x[1] for x in rows)
        tot_dis = sum(x[7] for x in rows)
        print("-- k=%s" % k)
        print("   rows judged, all records: %d; rows with >=2 slow: %d "
              "(%.4f%%)" % (tot_rows, tot_ge2, 100 * tot_ge2 / tot_rows if tot_rows else 0))
        print("   per-record fraction of rows with >=2 slow: min %.4f%%  "
              "median %.4f%%  max %.4f%%" % (100 * f2s[0], 100 * statistics.median(f2s), 100 * f2s[-1]))
        print("   per-record fraction of rows with >=1 slow: min %.2f%%  "
              "median %.2f%%  max %.2f%%" % (100 * f1s[0], 100 * statistics.median(f1s), 100 * f1s[-1]))
        print("   per-record fraction of rows with a FAST outlier: max %.4f%%"
              % (100 * ffs[-1]))
        print("   rows DISAGREEING (>=2 slow OR fast), all records: %d (%.4f%%); "
              "per-record fraction: median %.4f%%  max %.4f%%"
              % (tot_dis, 100 * tot_dis / tot_rows if tot_rows else 0,
                 100 * statistics.median(fds), 100 * fds[-1]))
        print("   records with DISAGREEING fraction above 0 / 0.5 / 1 / 2 %%: %d / %d / %d / %d"
              % (sum(1 for x in rows if x[6] > 0),
                 sum(1 for x in rows if x[6] > 0.005),
                 sum(1 for x in rows if x[6] > 0.01),
                 sum(1 for x in rows if x[6] > 0.02)))
        print("   records with >=2-slow fraction above 0 / 1 / 2 / 5 %%: %d / %d / %d / %d"
              % (sum(1 for x in rows if x[0] > 0),
                 sum(1 for x in rows if x[0] > 0.01),
                 sum(1 for x in rows if x[0] > 0.02),
                 sum(1 for x in rows if x[0] > 0.05)))
        worst = sorted(rows, key=lambda x: (-x[6], x[3]))[:5]
        print("   worst five records by DISAGREEING fraction:")
        for f2, g2, n, rid, f1, ff, fd, nd in worst:
            print("      %7.4f%%  %4d / %5d  %s" % (100 * fd, nd, n, rid))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
