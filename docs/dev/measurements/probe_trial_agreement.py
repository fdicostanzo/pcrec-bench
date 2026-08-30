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
    python3 docs/dev/measurements/probe_trial_agreement.py --groups   # the GROUP-LEVEL census (below)

`--groups` (added 2026-08-30 for the panel's R-16, the r3 review): the
GROUP-LEVEL census, printed INSTEAD of the row-level one (the no-argument
run still reproduces 2026-08-30-trial-agreement-census.txt). A GROUP is
one (pattern, regime, form) -- the unit one PASS of the harness sweeps.
Row arithmetic per gate_shape_v14.md 3.5 (rulings R-3 / R-19): a TRIAL is
timed iff `matched-as-expected` and `iterations > 1`; a ROW is judged iff
it has >= 2 timed trials OR any `timed-out` trial (the latter counts as
DISAGREEING outright); every other row is UNJUDGED and counted; xs sorted
by trial, m = statistics.median(xs); slow = trials STRICTLY ABOVE k * m;
fast = min(xs) < m / k. Per record: trials (the largest trial index),
rows keyed / judged / unjudged / timed-out, groups, and at every k in
GROUP_K_LIST the rows disagreeing, the largest d (disagreeing rows) in any
group, the WORST group (largest d, then smallest n, then lowest seq) and,
per candidate (D_MIN, c) in CANDIDATES, the groups that would DISAGREE
(d >= D_MIN and c * d >= n). The summary gives the group-size census per
sub-bench, the totals, the per-candidate counts over the store at every k,
and the constraint table of R-16: per group size present, the threshold
in rows each candidate needs, whether a WHOLE-group two-pass disturbance
(d = n) and a HALF-pass overlap (d = floor(n / 2)) flag, and the margins
in rows.
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
GROUP_K_LIST = (1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 2.0)
GROUP_MAIN_K = 1.5
CANDIDATES = tuple((d, c) for d in (2, 3) for c in (2, 3, 4))   # (D_MIN, c)
MARGIN_SIZES = (4, 5, 30, 85, 112)   # R-16's named group sizes


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


# ---------------------------------------------------------------- --groups
def row_census(rows):
    """Every match-row KEY of a record with its trials, per 3.5 of the spec.

    -> dict key -> {"timed": {trial: ns_per_iter}, "timed_out": bool,
                    "seq": lowest seq among the key's rows}
    """
    keys = {}
    for r in rows:
        if r.get("kind") != "match":
            continue
        key = (r["pattern_id"], r["regime"], r.get("form", "plain"),
               r["subject_id"])
        e = keys.setdefault(key, {"timed": {}, "timed_out": False,
                                  "seq": None, "trials": 0})
        seq = int(r.get("seq", 0))
        e["seq"] = seq if e["seq"] is None else min(e["seq"], seq)
        e["trials"] = max(e["trials"], int(r.get("trial", 0)))
        if r.get("match_outcome") == "timed-out":
            e["timed_out"] = True
            continue
        t = r.get("timing") or {}
        it = t.get("iterations") or 0
        if r.get("match_outcome") != "matched-as-expected" or it <= 1:
            continue
        e["timed"][int(r["trial"])] = t["elapsed_ns"] / it
    return keys


def judge_row(entry, k):
    """-> (judged, disagreeing, slow, fast) for one row key at k."""
    if entry["timed_out"]:
        return True, True, None, None
    xs = [entry["timed"][t] for t in sorted(entry["timed"])]
    if len(xs) < 2:
        return False, False, None, None
    m = statistics.median(xs)
    slow = sum(1 for x in xs if x > k * m)
    fast = 1 if min(xs) < m / k else 0
    return True, (slow >= 2 or fast == 1), slow, fast


def group_stats(keys, k):
    """-> per group (pattern, regime, form): {"n", "d", "seq"}; counts."""
    groups = {}
    judged = unjudged = timed_out = dis = 0
    for key, e in keys.items():
        g = groups.setdefault(key[:3], {"n": 0, "d": 0, "seq": e["seq"]})
        g["seq"] = min(g["seq"], e["seq"])
        j, d, _, _ = judge_row(e, k)
        if e["timed_out"]:
            timed_out += 1
        if not j:
            unjudged += 1
            continue
        judged += 1
        g["n"] += 1
        if d:
            dis += 1
            g["d"] += 1
    groups = {gk: g for gk, g in groups.items() if g["n"] > 0}
    return groups, judged, unjudged, timed_out, dis


def disagrees(g, dmin, c):
    return g["d"] >= dmin and c * g["d"] >= g["n"]


def worst_group(groups):
    if not groups:
        return None
    return sorted(groups.items(),
                  key=lambda kv: (-kv[1]["d"], kv[1]["n"], kv[1]["seq"]))[0]


def threshold_rows(n, dmin, c):
    """The smallest d that disagrees in a group of n rows under (dmin, c)."""
    return max(dmin, -(-n // c))   # ceil(n / c)


def main_groups(paths):
    header(paths)
    print("== GROUP-LEVEL CENSUS (gate_shape_v14.md 3.2 / 3.5, ruling R-16): "
          "a GROUP is one (pattern, regime, form); it DISAGREES under a "
          "candidate (D_MIN, c) iff d >= D_MIN and c * d >= n")
    print("k values for the group census: %s; candidates (D_MIN, c): %s"
          % (" ".join(str(k) for k in GROUP_K_LIST),
             " ".join("(%d,%d)" % dc for dc in CANDIDATES)))
    print("row arithmetic: a trial is timed iff matched-as-expected and "
          "iterations > 1; a row is judged iff >= 2 timed trials OR any "
          "timed-out trial (counted as DISAGREEING); other rows UNJUDGED")
    print()
    per_sb_sizes = {}
    tot = {"keys": 0, "judged": 0, "unjudged": 0, "timed_out": 0,
           "groups": 0, "records": 0}
    per_k = {k: {"dis_rows": 0, "max_d": 0, "max_d_where": None,
                 "cand_groups": Counter(), "cand_records": Counter(),
                 "records_with_d": 0}
             for k in GROUP_K_LIST}
    size_max_d = Counter()   # at GROUP_MAIN_K: group size -> largest d seen
    for p in paths:
        setup, rows = read_record(p)
        rid = setup["record_id"]
        keys = row_census(rows)
        trials = max((e["trials"] for e in keys.values()), default=0)
        sb = rid.split("__")[0]
        groups_main, judged, unjudged, timed_out, dis = group_stats(
            keys, GROUP_MAIN_K)
        sizes = Counter(g["n"] for g in groups_main.values())
        per_sb_sizes.setdefault(sb, Counter()).update(sizes)
        tot["keys"] += len(keys)
        tot["judged"] += judged
        tot["unjudged"] += unjudged
        tot["timed_out"] += timed_out
        tot["groups"] += len(groups_main)
        tot["records"] += 1
        print("-- %s" % rid)
        print("   schema %s  status %s  tier %s  trials %d  row keys %d  "
              "judged %d  unjudged %d  timed-out rows %d  groups %d  "
              "group sizes %s"
              % (setup["schema_version"], setup["status"],
                 setup.get("tier", "(absent)"), trials, len(keys), judged,
                 unjudged, timed_out, len(groups_main),
                 " ".join("%d:x%d" % (n, c) for n, c in sorted(sizes.items()))))
        for k in GROUP_K_LIST:
            groups, j2, u2, t2, d2 = group_stats(keys, k)
            w = worst_group(groups)
            max_d = max((g["d"] for g in groups.values()), default=0)
            pk = per_k[k]
            pk["dis_rows"] += d2
            if max_d > pk["max_d"]:
                pk["max_d"], pk["max_d_where"] = max_d, (rid, w[0] if w else None)
            if max_d > 0:
                pk["records_with_d"] += 1
            cand = []
            any_rec = set()
            for dmin, c in CANDIDATES:
                ng = sum(1 for g in groups.values() if disagrees(g, dmin, c))
                pk["cand_groups"][(dmin, c)] += ng
                if ng:
                    pk["cand_records"][(dmin, c)] += 1
                cand.append("(%d,%d):%d" % (dmin, c, ng))
            if k == GROUP_MAIN_K:
                for g in groups.values():
                    size_max_d[g["n"]] = max(size_max_d[g["n"]], g["d"])
            wtxt = ("%s / %s / %s d=%d n=%d" % (w[0][0], w[0][1], w[0][2],
                                                w[1]["d"], w[1]["n"])
                    if w else "(none)")
            print("   k=%-4s rows disagreeing %3d  max d in any group %d  "
                  "worst group %s  groups disagreeing per candidate %s"
                  % (k, d2, max_d, wtxt, " ".join(cand)))
        print()

    print("== SUMMARY over %d records" % tot["records"])
    print("row keys %d; judged %d; unjudged %d; rows with a timed-out trial %d; "
          "groups %d" % (tot["keys"], tot["judged"], tot["unjudged"],
                         tot["timed_out"], tot["groups"]))
    print("group sizes (judged rows per group) per sub-bench, over all its "
          "records (size:x groups):")
    for sb, sizes in sorted(per_sb_sizes.items()):
        print("   %-22s %s" % (sb, " ".join("%d:x%d" % (n, c)
                                            for n, c in sorted(sizes.items()))))
    print()
    print("per k: rows disagreeing over the store, the largest d in any group "
          "(and where), records with any d > 0, and per candidate (D_MIN, c) "
          "the groups / records that DISAGREE:")
    for k in GROUP_K_LIST:
        pk = per_k[k]
        where = pk["max_d_where"]
        wt = ("%s :: %s / %s / %s" % (where[0], where[1][0], where[1][1],
                                      where[1][2])
              if where and where[1] else "(none)")
        print("-- k=%s  rows disagreeing %d  max d %d (%s)  records with d>0 %d"
              % (k, pk["dis_rows"], pk["max_d"], wt, pk["records_with_d"]))
        print("   " + "  ".join("(%d,%d): %d groups / %d records"
                                % (dmin, c, pk["cand_groups"][(dmin, c)],
                                   pk["cand_records"][(dmin, c)])
                                for dmin, c in CANDIDATES))
    print()
    sizes_present = sorted(set(n for s in per_sb_sizes.values() for n in s))
    print("== CONSTRAINT TABLE (R-16) at k=%s: per group size n, per candidate: "
          "T = the smallest d that disagrees (max(D_MIN, ceil(n/c))); "
          "WHOLE = a two-pass disturbance of the whole group (d = n) flags?; "
          "HALF = a half-pass overlap (d = floor(n/2)) flags?; "
          "margin-store = T - (largest d the store shows at this n); "
          "margin-half = floor(n/2) - T (rows to spare before the half shape "
          "stops flagging)" % GROUP_MAIN_K)
    print("   sizes present in the store: %s; R-16's named sizes: %s"
          % (" ".join(str(n) for n in sizes_present),
             " ".join(str(n) for n in MARGIN_SIZES)))
    for dmin, c in CANDIDATES:
        print("-- candidate (D_MIN=%d, c=%d): a group disagrees iff d >= %d and "
              "%d*d >= n" % (dmin, c, dmin, c))
        print("   %5s %4s %6s %5s %13s %12s" % ("n", "T", "WHOLE", "HALF",
                                               "margin-store", "margin-half"))
        for n in sorted(set(sizes_present) | set(MARGIN_SIZES)):
            T = threshold_rows(n, dmin, c)
            whole = disagrees({"d": n, "n": n}, dmin, c)
            half = disagrees({"d": n // 2, "n": n}, dmin, c)
            ms = ("%d" % (T - size_max_d[n])) if n in size_max_d else "n/a"
            print("   %5d %4d %6s %5s %13s %12d%s"
                  % (n, T, "yes" if whole else "NO", "yes" if half else "NO",
                     ms, n // 2 - T,
                     "" if n in sizes_present else "   (not in the store)"))
        both = all(disagrees({"d": n, "n": n}, dmin, c)
                   and disagrees({"d": n // 2, "n": n}, dmin, c)
                   for n in MARGIN_SIZES)
        print("   flags WHOLE and HALF at every named size: %s; groups "
              "disagreeing on the store at k=%s: %d"
              % ("yes" if both else "NO", GROUP_MAIN_K,
                 per_k[GROUP_MAIN_K]["cand_groups"][(dmin, c)]))
    return 0


def main(argv):
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        paths = sorted(glob.glob(os.path.join(REPO, "store", "records",
                                              "*", "*", "*.jsonl")))
    if "--groups" in argv:
        return main_groups(paths)
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
