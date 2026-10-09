#!/usr/bin/env python3
"""[B132] A/B/A/B analysis. Source: the stores written by
2026-10-09-b132-shim-layout-ab-run.sh (OUT/store-{OLD1,NEW1,OLD2,NEW2}) and
the O-92 ratios from 2026-10-09-b132-select-cells.py's TSV.
Arithmetic: pcrecbench.reduce.reduce_set_cell (set-grain median over the 75
short subjects, plain form) -- the reporter's own. "DISJOINT" = the closed
[min,max] per-subject-median ranges of the two runs do not overlap.
Run: python3 this.py OUTDIR CELLS_TSV
"""
import glob, json, os, sys
MAIN = "/home/duxevents/pcrec-bench"
sys.path.insert(0, MAIN)
from pcrecbench import reduce as R

out, tsv = sys.argv[1], sys.argv[2]
cells = {}
for step in ("OLD1", "NEW1", "OLD2", "NEW2"):
    for f in glob.glob("%s/store-%s/records/capability@0.2/*/*.jsonl" % (out, step)):
        setup, rows = R.read_record(f)
        tid = os.path.basename(os.path.dirname(f))
        cfg = "pcrec-auto" if "auto-caps" in tid else "pcrec-nocaps"
        for key, subs in R.cells_from_record(rows).items():
            if key[1] == "short-subject-search" and key[2] == "plain":
                cells[(cfg, key[0], step)] = R.reduce_set_cell(subs)
o92 = {}
for l in list(open(tsv))[1:]:
    c, p, r, ov, a, b, ident, n = l.rstrip("\n").split("\t")
    o92[(c, p)] = (float(r), ov)
def rel(a, b):
    ov = not (b.max_ns < a.min_ns or b.min_ns > a.max_ns)
    return b.median_ns / a.median_ns, "ov" if ov else "DISJ"
print("%-13s %-44s %7s %-5s | %-14s %-14s | %-14s %-14s | %s" % (
    "config", "pattern", "O-92", "", "NEW1/OLD1", "NEW2/OLD2", "OLD2/OLD1", "NEW2/NEW1", "medians ns O1 N1 O2 N2"))
for (cfg, p) in sorted({(c, p) for c, p, s in cells}):
    g = {s: cells.get((cfg, p, s)) for s in ("OLD1", "NEW1", "OLD2", "NEW2")}
    if None in g.values() or any(v.median_ns is None for v in g.values()):
        print(cfg, p, "MISSING", [s for s, v in g.items() if v is None]); continue
    r92 = o92.get((cfg, p))
    a = rel(g["OLD1"], g["NEW1"]); b = rel(g["OLD2"], g["NEW2"]); d1 = rel(g["OLD1"], g["OLD2"]); d2 = rel(g["NEW1"], g["NEW2"])
    print("%-13s %-44s %7.3f %-5s | %6.3f %-7s %6.3f %-7s | %6.3f %-7s %6.3f %-7s | %.0f %.0f %.0f %.0f" % (
        cfg, p, r92[0] if r92 else float('nan'), (r92[1][:3] if r92 else ""),
        a[0], a[1], b[0], b[1], d1[0], d1[1], d2[0], d2[1],
        *[g[s].median_ns for s in ("OLD1", "NEW1", "OLD2", "NEW2")]))
