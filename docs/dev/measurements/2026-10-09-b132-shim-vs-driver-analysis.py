#!/usr/bin/env python3
"""[B132] factor-split analysis over OUT/store-{OLD,MID,NEW,MID2} from
2026-10-09-b132-shim-vs-driver-run.sh. MID/OLD = shim.c alone; NEW/MID = driver.c
alone; MID2/MID = drift. Same set-grain reduction as the A/B analysis.
Run: python3 this.py OUTDIR"""
import glob, os, sys
sys.path.insert(0, "/home/duxevents/pcrec-bench")
from pcrecbench import reduce as R
out = sys.argv[1]; cells = {}
for step in ("OLD", "MID", "NEW", "MID2"):
    for f in glob.glob("%s/store-%s/records/capability@0.2/*/*.jsonl" % (out, step)):
        tid = os.path.basename(os.path.dirname(f)); cfg = "pcrec-auto" if "auto-caps" in tid else "pcrec-nocaps"
        for key, subs in R.cells_from_record(R.read_record(f)[1]).items():
            if key[1] == "short-subject-search" and key[2] == "plain": cells[(cfg, key[0], step)] = R.reduce_set_cell(subs)
def rel(a, b):
    return "%.3f %s" % (b.median_ns / a.median_ns, "ov" if not (b.max_ns < a.min_ns or b.min_ns > a.max_ns) else "DISJ")
print("%-13s %-36s | MID/OLD (shim) | NEW/MID (driver) | NEW/OLD | MID2/MID (drift) | medians ns OLD MID NEW MID2" % ("config", "pattern"))
for (c, p) in sorted({(c, p) for c, p, s in cells}):
    g = [cells[(c, p, s)] for s in ("OLD", "MID", "NEW", "MID2")]
    print("%-13s %-36s | %-14s | %-16s | %-13s | %-16s | %s" % (c, p, rel(g[0], g[1]), rel(g[1], g[2]), rel(g[0], g[2]), rel(g[1], g[3]), " ".join("%.0f" % x.median_ns for x in g)))
