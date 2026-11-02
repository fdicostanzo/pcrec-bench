# b149monread an10: sentinel@0.1 opening vs closing, per testee (from the committed report TSV; --all-records ids carry @<timestamp>).
import statistics, collections, re
f = "reports/2026-11-02-sentinel-0.1-ryzen7700x-cb32eda28.tsv"
d = collections.defaultdict(dict)
for l in open(f):
    if l.startswith("#") or l.startswith("section"): continue
    c = l.rstrip("\n").split("\t")
    if len(c) > 11 and c[0] in ("rank", "rank_yes", "rank_no") and c[10] == "median_ns":
        t = c[6]; m = re.match(r"(.*)@(\d{8}T\d{6}Z)$", t)
        base, ts = (m.group(1), m.group(2)) if m else (t, "")
        d[(base, c[1], c[2], c[3], c[4])][ts] = float(c[11])
print("testees:", sorted({k[0] for k in d}))
print("timestamps per testee:", {b: sorted({ts for k, v in d.items() if k[0] == b for ts in v}) for b in sorted({k[0] for k in d})})
for b in sorted({k[0] for k in d}):
    rat = []
    for k, v in d.items():
        if k[0] != b or len(v) != 2: continue
        o, e = (v[t] for t in sorted(v))
        rat.append((e / o, k))
    for reg in ("short-subject-search", "large-subject-throughput"):
        x = sorted(r[0] for r in rat if r[1][3] == reg)
        if x: print(f"  {b:44s} {reg:26s} cells={len(x):3d} close/open median={statistics.median(x):.4f} p5={x[int(.05*(len(x)-1))]:.4f} p95={x[int(.95*(len(x)-1))]:.4f} min={x[0]:.3f} max={x[-1]:.3f}")
# same-window N vs B: cb32 / 614 auto (identical patterns?) at open and at close
for ts_idx, nm in ((0, "open"), (1, "close")):
    rat = []
    for k, v in d.items():
        if k[0] != "pcrec_cb32eda28_auto-caps-simdna": continue
        k2 = ("pcrec_614d45eb3_auto-caps-simdna",) + k[1:]
        if k2 in d and len(v) == 2 and len(d[k2]) == 2:
            a = v[sorted(v)[ts_idx]]; b = d[k2][sorted(d[k2])[ts_idx]]
            rat.append((a / b, k))
    for reg in ("short-subject-search", "large-subject-throughput"):
        x = sorted(r[0] for r in rat if r[1][3] == reg)
        if x: print(f"  cb32/614 auto @{nm:5s} {reg:26s} cells={len(x)} median={statistics.median(x):.4f} p5={x[int(.05*(len(x)-1))]:.4f} p95={x[int(.95*(len(x)-1))]:.4f}")
