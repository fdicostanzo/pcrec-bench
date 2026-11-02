# b149monread an13: sentinel cross-window offset W2 (11-01) vs this window (11-02 open and close), pcrec_cb32eda28_auto-caps-simdna; by cell (pattern, subject) medians.
import sys, statistics, glob
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
tid = sys.argv[1]
fs = path_for(tid, "sentinel@0.1")
recs = {}
for f in fs:
    s, c, m = load_file(f)
    recs[f.split("__")[-1][:-6]] = m
ts = sorted(recs); print(ts)
def cells(m): return {k: med(v) for k, v in m.items() if v[0]["o"] == "matched-as-expected" and med(v)}
base = cells(recs[ts[0]])
for t in ts[1:]:
    c = cells(recs[t]); r = sorted(c[k] / base[k] for k in base if k in c)
    print(f"  {t} / {ts[0]}: cells={len(r)} median={statistics.median(r):.4f} p5={r[int(.05*(len(r)-1))]:.4f} p95={r[int(.95*(len(r)-1))]:.4f}")
