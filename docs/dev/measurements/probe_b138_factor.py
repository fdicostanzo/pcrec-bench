#!/usr/bin/env python3
"""probe_b138_factor.py -- [B138] the per-testee ENGINE-SPEED factor of a new
box against a reference box, from the canonical store's records.

Owed by the b138 read (plan.md [B138] COMPARABILITY): per-testee factors
labelled 'box incl. governor', never one number, SHORT cells split from LONG
ones. The chain's SENTINEL_FACTOR is a wall-clock ratio of cell spans and
measures window LENGTH (protocol-bound), not engine speed -- this is the
speed factor.

Pairing: every `measured` record on --new is paired with the NEWEST
`measured` record on --ref with the same (subbench, version, testee_id); the
testee_id carries the pin, so a pair is the same engine build. Per set cell
(pattern, regime, form) both sides reduce with pcrecbench.reduce's set-grain
arithmetic (the reporter's own); factor = ref median / new median (>1 = the
new box is faster). Expectation-failing cells (no number) are skipped and
counted. Aggregates per (testee, class) are the geometric mean, the median
and the min..max of the cell factors, with the cell count. Class: LONG if the
regime is a large-subject regime (name contains 'throughput', 'large' or
'sweep'), else SHORT; every regime's own class is printed so the split is
visible. Compile: per record pair, ref/new of the median compile
cost.total_ns over patterns compiled on both sides (a separate axis).

Usage: python3 docs/dev/measurements/probe_b138_factor.py \
           [--new ryzen7700x] [--ref budu-ryzen1600] [--since 2026-10-18]
Reads store/index.tsv and the paired record files only; writes nothing.
"""
import argparse
import math
import os
import statistics
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
from pcrecbench.reduce import cells_from_record, read_record, reduce_set_cell  # noqa: E402

LONG_TOKENS = ("throughput", "large", "sweep")


def klass(regime):
    return "LONG" if any(t in (regime or "") for t in LONG_TOKENS) else "SHORT"


def load_index(path):
    with open(path, encoding="utf-8") as f:
        hdr = f.readline().rstrip("\n").split("\t")
        return [dict(zip(hdr, ln.rstrip("\n").split("\t"))) for ln in f if ln.strip()]


def set_medians(rows):
    out = {}
    for key, by_subj in cells_from_record(rows).items():
        c = reduce_set_cell(by_subj)
        out[key] = c.median_ns if not c.expectation_failing else None
    return out


def compile_medians(rows):
    per = defaultdict(list)
    for r in rows:
        if r.get("kind") == "compile":
            ns = (r.get("cost") or {}).get("total_ns")
            if ns and r.get("compile_outcome", "compiled") == "compiled":
                per[(r.get("pattern_id"), r.get("form", "plain"))].append(ns)
    return {k: statistics.median(v) for k, v in per.items()}


def agg(fs):
    g = math.exp(sum(math.log(x) for x in fs) / len(fs))
    return "geo %.3f  med %.3f  range %.3f..%.3f  n=%d" % (
        g, statistics.median(fs), min(fs), max(fs), len(fs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--new", default="ryzen7700x")
    ap.add_argument("--ref", default="budu-ryzen1600")
    ap.add_argument("--since", default="", help="new records with timestamp >= this")
    ap.add_argument("--store", default=os.path.join(ROOT, "store"))
    ap.add_argument("--subbench", action="append", default=[],
                    help="restrict to these sub-benches (repeatable)")
    a = ap.parse_args()

    idx = [r for r in load_index(os.path.join(a.store, "index.tsv"))
           if r["status"] == "measured"]
    ref = {}
    for r in idx:
        if r["machine_id"] == a.ref:
            k = (r["subbench"], r["version"], r["testee_id"])
            if k not in ref or r["timestamp"] > ref[k]["timestamp"]:
                ref[k] = r
    new = [r for r in idx if r["machine_id"] == a.new and r["timestamp"] >= a.since
           and (not a.subbench or r["subbench"] in a.subbench)]

    by_class = defaultdict(list)          # (testee, class) -> factors
    by_regime = defaultdict(list)         # (testee, regime) -> factors
    by_set = defaultdict(list)            # (testee, subbench, class) -> factors
    comp = defaultdict(list)              # testee -> compile factors
    regimes = {}
    unpaired, skipped = [], 0
    for r in sorted(new, key=lambda r: (r["testee_id"], r["subbench"])):
        k = (r["subbench"], r["version"], r["testee_id"])
        if k not in ref:
            unpaired.append("%s@%s %s" % k)
            continue
        _, nrows = read_record(os.path.join(a.store, r["path"]))
        _, rrows = read_record(os.path.join(a.store, ref[k]["path"]))
        nm, rm = set_medians(nrows), set_medians(rrows)
        for key in nm.keys() & rm.keys():
            if not nm[key] or not rm[key]:
                skipped += 1
                continue
            f = rm[key] / nm[key]
            regime = key[1]
            regimes[regime] = klass(regime)
            by_class[(r["testee_id"], klass(regime))].append(f)
            by_regime[(r["testee_id"], regime)].append(f)
            by_set[(r["testee_id"], r["subbench"], klass(regime))].append(f)
        nc, rc = compile_medians(nrows), compile_medians(rrows)
        cf = [rc[p] / nc[p] for p in nc.keys() & rc.keys() if nc[p] and rc[p]]
        if cf:
            comp[r["testee_id"]].append(statistics.median(cf))
        del nrows, rrows

    print("# probe_b138_factor.py --new %s --ref %s --since %r" % (a.new, a.ref, a.since))
    print("# factor = %s median / %s median, set grain; >1 = %s faster (box incl. governor)"
          % (a.ref, a.new, a.new))
    print("# new records %d, paired %d, unpaired %d, cells skipped (no number) %d"
          % (len(new), len(new) - len(unpaired), len(unpaired), skipped))
    print("\n## regime classes")
    for g, c in sorted(regimes.items()):
        print("%-36s %s" % (g, c))
    print("\n## MATCH, per testee x class")
    for (t, c), fs in sorted(by_class.items()):
        print("%-48s %-5s %s" % (t, c, agg(fs)))
    print("\n## MATCH, per testee x set x class")
    for (t, s, c), fs in sorted(by_set.items()):
        print("%-48s %-10s %-5s %s" % (t, s, c, agg(fs)))
    print("\n## MATCH, per testee x regime")
    for (t, g), fs in sorted(by_regime.items()):
        print("%-48s %-30s %s" % (t, g, agg(fs)))
    print("\n## COMPILE (per record pair: median over patterns of ref/new total_ns)")
    for t, fs in sorted(comp.items()):
        print("%-48s %s" % (t, agg(fs)))
    if unpaired:
        print("\n## unpaired (no %s record at the same testee_id)" % a.ref)
        for u in unpaired:
            print("  " + u)


if __name__ == "__main__":
    main()
