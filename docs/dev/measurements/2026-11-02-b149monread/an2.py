# b149monread an2: K134 flip detail by cell; deep-arm non-matching cells; cross-pin timing on answered cells.
import sys, collections, statistics
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
R = {n: load(n)[0] for n in NAMES}
def cell_list(a, b, pats):
    old, new = R[a][2], R[b][2]
    for k in sorted(old):
        if k[0] in pats and (old[k][0]["o"] != "matched-as-expected" or new[k][0]["o"] != "matched-as-expected"):
            print(f"  {k[0]:24s} {k[1][:12]:12s} {k[2]:18s} {old[k][0]['o']:10s} -> {new[k][0]['o']:10s}  {(new[k][0]['diag'] or '')[-24:]}")
print("== auto: 614d45eb3 -> cb32eda28, cells with a gave-up on either side")
cell_list("auto614", "auto", {"cscan", "cscan-onig", "wild-sexp-balanced", "wild-json-validate", "wild-json-validate-onig"})
print("\n== per-pattern gave-up counts at each pin (auto)")
for n in ("auto614", "auto"):
    c = collections.Counter()
    for k, rows in R[n][2].items():
        if rows[0]["o"] == "gave-up": c[k[0]] += 1
    print(n, dict(c), "total", sum(c.values()))
print("\n== call-stream counts (auto): matched / nomatch / refused / gave_up per stream at both pins")
for n in ("auto614", "auto", "auto_in", "auto_inl", "jit_deep", "interp_deep", "onig_deep"):
    for k, rows in sorted(R[n][2].items()):
        if k[1] == "call-stream" and k[0] in ("cscan", "cscan-onig") and rows[0]["stream"]:
            s = rows[0]["stream"]
            print(f"  {n:11s} {k[0]:11s} {k[2]:15s} calls={s['calls']} m={s['matched']} n={s['nomatch']} r={s['refused']} gu={s['gave_up']} {rows[0]['o']}")
print("\n== deep arms: cells not matched-as-expected")
for n in ("jit_deep", "interp_deep", "onig_deep"):
    for k, rows in sorted(R[n][2].items()):
        if rows[0]["o"] != "matched-as-expected":
            print(f"  {n:11s} {k[0]:24s} {k[1][:12]:12s} {k[2]:18s} {[r['o'] for r in rows]} obs={rows[0]['obs']}")
print("\n== cross-pin timing (cb32eda28 / 614d45eb3 medians) on cells answered at both pins, by regime")
for a, b in (("auto614", "auto"), ("vm614", "vm")):
    for reg in ("short-subject-search", "large-subject-throughput"):
        rat = []; wt = []
        for k, rows in R[b][2].items():
            if k[1] != reg: continue
            o = R[a][2][k]
            if o[0]["o"] != "matched-as-expected" or rows[0]["o"] != "matched-as-expected": continue
            x, y = med(o), med(rows)
            if x and y: rat.append(y / x); wt.append((x, y))
        rat.sort()
        q = lambda p: rat[int(p * (len(rat) - 1))]
        sx = sum(w[0] for w in wt); sy = sum(w[1] for w in wt)
        print(f"  {b:5s} {reg:26s} n={len(rat)} median={statistics.median(rat):.4f} p5={q(.05):.4f} p95={q(.95):.4f} sum-ratio={sy/sx:.4f}")
