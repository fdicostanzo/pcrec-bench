#!/usr/bin/env python3
"""b50predaudit probe 1: the structural population census over every
committed report TSV.  Read-only; no store, no engine."""
import glob, os, sys, collections

ROOT = os.environ.get("PCRECBENCH_ROOT", os.getcwd())  # repoint at a checkout
COLS = ["section", "pattern", "subject_or_na", "regime_or_na", "form", "fact",
        "testee", "status", "tier", "rank_or_na", "metric", "value", "n",
        "pass_rate", "n_gave_up", "n_wrong", "gave_up_summary", "delta_verdict"]

files = sorted(glob.glob(os.path.join(ROOT, "reports", "*.tsv")))
files = [f for f in files if not f.endswith(".subject-grain.tsv")]
print(f"# set-grain report TSVs: {len(files)}")
sg = sorted(glob.glob(os.path.join(ROOT, "reports", "*.subject-grain.tsv")))
print(f"# subject-grain slices:  {len(sg)}")

nonempty = collections.defaultdict(set)      # section -> cols ever non-empty
rowcount = collections.Counter()             # section -> rows
metrics = collections.defaultdict(collections.Counter)  # section -> metric
floor_hdr = collections.Counter()
grain_hdr = collections.Counter()
bad_float = collections.Counter()            # (section, metric) -> n empty/nan
fail_rows = collections.Counter()            # section -> rows with n_wrong>0 or n_gave_up>0
rank_rows_per_cell = collections.Counter()

def num(s):
    try:
        v = float(s)
        return v
    except ValueError:
        return None

for path in files:
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    hdr = lines[0]
    for key, ctr in (("floor_pattern: ", floor_hdr), ("grain: ", grain_hdr)):
        i = hdr.find(key)
        if i < 0:
            ctr["(absent)"] += 1
            continue
        val = hdr[i + len(key):].split("; ")[0]
        ctr[val] += 1
    cells = collections.Counter()
    for ln in lines[2:]:
        if not ln:
            continue
        r = dict(zip(COLS, ln.split("\t")))
        s = r["section"]
        rowcount[s] += 1
        metrics[s][r["metric"]] += 1
        for c in COLS:
            if r[c] != "":
                nonempty[s].add(c)
        nw, ng = num(r["n_wrong"]), num(r["n_gave_up"])
        if (nw or 0) > 0 or (ng or 0) > 0:
            fail_rows[s] += 1
        if s == "rank":
            cells[(r["pattern"], r["regime_or_na"], r["form"], r["testee"])] += 1
            if r["metric"] in ("median_ns", "stddev_ns", "min_ns", "max_ns",
                               "ratio_vs_baseline", "ratio_vs_best"):
                v = num(r["value"])
                if v is None or v != v or v in (float("inf"), float("-inf")):
                    bad_float[(s, r["metric"], r["value"][:12])] += 1
    for _k, n in cells.items():
        rank_rows_per_cell[n] += 1

print("\n## rows and ever-non-empty columns, by section")
for s in sorted(rowcount):
    miss = [c for c in COLS if c not in nonempty[s]]
    print(f"{s:16} rows={rowcount[s]:8,}  ALWAYS-EMPTY: {','.join(miss) or '(none)'}")

print("\n## metrics by section")
for s in sorted(metrics):
    print(f"{s:16} " + ", ".join(f"{m or '(empty)'}={n:,}"
                                 for m, n in metrics[s].most_common()))

print("\n## rows carrying n_wrong>0 or n_gave_up>0, by section")
for s in sorted(rowcount):
    print(f"{s:16} {fail_rows[s]:8,} of {rowcount[s]:8,}")

print("\n## rank rows per (pattern,regime,form,testee) cell")
for n, c in sorted(rank_rows_per_cell.items()):
    print(f"  {n} rows/cell : {c:,} cells")

print("\n## header floor_pattern values")
for v, n in floor_hdr.most_common():
    print(f"  {v!r}: {n} report(s)")
print("## header grain values")
for v, n in grain_hdr.most_common():
    print(f"  {v!r}: {n}")

print("\n## non-finite / empty numeric rank values")
print(f"  {sum(bad_float.values())} occurrence(s)")
for k, n in bad_float.most_common(10):
    print(f"  {k}: {n}")
