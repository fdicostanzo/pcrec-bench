#!/usr/bin/env python3
"""[B133] instrument A/B/A/B analysis. Source: the stores written by
scripts/instrument_ab.sh (OUT/store-{BEFORE1,AFTER1,BEFORE2,AFTER2}).
Arithmetic: pcrecbench.reduce.reduce_set_cell (the set-grain median over the
short subjects, plain form -- the reporter's own); the per-run trial range is
its min/max. "ov" = the AFTER and BEFORE [min,max] trial ranges overlap.
Run: python3 this.py OUTDIR
"""
import glob, os, sys
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from pcrecbench import reduce as R

out = sys.argv[1]
STEPS = ("BEFORE1", "AFTER1", "BEFORE2", "AFTER2")
cells = {}
for step in STEPS:
    for f in glob.glob("%s/store-%s/records/*/*/*.jsonl" % (out, step)):
        setup, rows = R.read_record(f)
        tid = os.path.basename(os.path.dirname(f))
        cfg = ("pcrec-auto" if "auto-caps" in tid else "pcrec-nocaps" if "nocaps" in tid
               else "pcre2-jit" if "jit" in tid else tid)
        for key, subs in R.cells_from_record(rows).items():
            if key[1] == "short-subject-search" and key[2] == "plain":
                cells[(cfg, key[0], step)] = R.reduce_set_cell(subs)

def rel(a, b):
    ov = not (b.max_ns < a.min_ns or b.min_ns > a.max_ns)
    return b.median_ns / a.median_ns, ("ov" if ov else "DISJ")

hdr = "%-13s %-44s | %-12s %-12s | %-12s %-12s | %s" % (
    "config", "pattern", "AFT1/BEF1", "AFT2/BEF2", "BEF2/BEF1", "AFT2/AFT1",
    "median ns [trial min..max]: BEF1 AFT1 BEF2 AFT2")
print(hdr)
agg = {}
for (cfg, p) in sorted({(c, p) for c, p, s in cells}):
    g = {s: cells.get((cfg, p, s)) for s in STEPS}
    if None in g.values() or any(v.median_ns is None for v in g.values()):
        print(cfg, p, "MISSING", [s for s, v in g.items() if v is None]); continue
    a = rel(g["BEFORE1"], g["AFTER1"]); b = rel(g["BEFORE2"], g["AFTER2"])
    d1 = rel(g["BEFORE1"], g["BEFORE2"]); d2 = rel(g["AFTER1"], g["AFTER2"])
    mid = (a[0] * b[0]) ** 0.5
    agg.setdefault(cfg, []).append((p, mid))
    print("%-13s %-44s | %5.3f %-5s  %5.3f %-5s  | %5.3f %-5s  %5.3f %-5s  | %s" % (
        cfg, p, a[0], a[1], b[0], b[1], d1[0], d1[1], d2[0], d2[1],
        " ".join("%.1f[%.1f..%.1f]" % (g[s].median_ns, g[s].min_ns, g[s].max_ns) for s in STEPS)))
print()
for cfg, v in sorted(agg.items()):
    xs = sorted(r for _p, r in v)
    print("%-13s %2d cells, AFTER/BEFORE geomean-of-reps: min %.3f median %.3f max %.3f" % (
        cfg, len(xs), xs[0], xs[len(xs) // 2], xs[-1]))
