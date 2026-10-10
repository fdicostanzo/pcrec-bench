#!/usr/bin/env python3
"""[B135] sentinel@0.1 open-vs-end analysis, states 1+2 window (2026-10-10).
Source: store/records/sentinel@0.1/*/*.jsonl (10 records: five testees, one
at the window's open ~12:49-13:22 EDT, one at its end ~18:40-19:19 EDT).
Arithmetic: pcrecbench.reduce.reduce_set_cell per (pattern) over the 75 short
subjects, regime search_short, plain form -- the reporter's own; "ov" = the
open and end [min,max] trial ranges overlap. Run from the repo root:
    python3 docs/dev/measurements/2026-10-10-b135-sentinel-open-end.py [STORE_DIR]
"""
import glob, os, sys, json
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from pcrecbench import reduce as R

store = sys.argv[1] if len(sys.argv) > 1 else "store"
recs = {}
for f in sorted(glob.glob(os.path.join(store, "records/sentinel@0.1/*/*.jsonl"))):
    tid = os.path.basename(os.path.dirname(f))
    ts = os.path.basename(f).rsplit("__", 1)[1].split(".")[0]
    recs.setdefault(tid, []).append((ts, f))
cells = {}
for tid, lst in recs.items():
    lst.sort()
    for slot, (ts, f) in zip(("open", "end"), lst):
        setup, rows = R.read_record(f)
        for key, subs in R.cells_from_record(rows).items():
            if key[2] == "plain":
                cells[(tid, key[0], slot)] = R.reduce_set_cell(subs)
print("%-34s %-42s | %-8s %-5s | open [min..max]  end [min..max]" % ("testee", "pattern", "end/open", "trials"))
agg = {}
for tid in sorted(recs):
    for p in sorted({k[1] for k in cells if k[0] == tid}):
        o, e = cells.get((tid, p, "open")), cells.get((tid, p, "end"))
        if not o or not e or o.median_ns is None or e.median_ns is None:
            print(tid, p, "MISSING"); continue
        ov = not (e.max_ns < o.min_ns or e.min_ns > o.max_ns)
        r = e.median_ns / o.median_ns
        agg.setdefault(tid, []).append((r, ov))
        print("%-34s %-42s | %7.3f  %-5s | %9.1f[%.1f..%.1f]  %9.1f[%.1f..%.1f]" % (
            tid, p, r, "ov" if ov else "DISJ", o.median_ns, o.min_ns, o.max_ns, e.median_ns, e.min_ns, e.max_ns))
print()
for tid in sorted(agg):
    rs = sorted(r for r, _ in agg[tid])
    print("%-34s %2d cells end/open: min %.3f median %.3f max %.3f; DISJ %d" % (
        tid, len(rs), rs[0], rs[len(rs) // 2], rs[-1], sum(1 for _, ov in agg[tid] if not ov)))
