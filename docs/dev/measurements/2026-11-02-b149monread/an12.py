# b149monread an12: R1 (3x the best non-excluded engine) for the pcrec _in / default arms vs the deep libpcre2/onig arms; fire-count doubling evidence.
import sys, statistics
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
R = {n: load(n)[0] for n in ("auto", "auto_in", "vm_in", "jit_deep", "interp_deep", "onig_deep", "auto614")}
ok = lambda rows: rows and rows[0]["o"] == "matched-as-expected" and med(rows)
others = ("jit_deep", "interp_deep", "onig_deep")
print("== R1, large-subject-throughput, pcrec auto_in vs best of {jit,interp,onig}-deep: cells > 3x (and the median MB/s)")
n = 0; tot = 0; lst = []
for k, rows in R["auto_in"][2].items():
    if k[1] != "large-subject-throughput" or not ok(rows): continue
    cands = [(med(R[o][2][k]), o) for o in others if k in R[o][2] and ok(R[o][2][k])]
    if not cands: continue
    best = min(cands); tot += 1; r = med(rows) / best[0]
    if r > 3: lst.append((r, k, best[1], best[0], med(rows)))
print(f"  cells with a comparator: {tot}; pcrec _in > 3x best: {len(lst)}")
for r in sorted(lst, reverse=True): print(f"   x{r[0]:.1f} {r[1][0]:22s} {r[1][2]:16s} best={r[2]} {r[3]:.5g} ns  pcrec_in={r[4]:.5g} ns")
print("   cells where pcrec _in is the best:", sum(1 for k, rows in R['auto_in'][2].items() if k[1]=='large-subject-throughput' and ok(rows) and all(not(k in R[o][2] and ok(R[o][2][k])) or med(R[o][2][k]) > med(rows) for o in others)))
print("\n== R1 short-subject mean ns/call per pattern (set-sum / 161): pcrec auto_in vs best of others")
pats = sorted({k[0] for k in R["auto_in"][2] if k[1] == "short-subject-search"})
for p in pats:
    def mean(n):
        v = [med(rows) for k, rows in R[n][2].items() if k[0] == p and k[1] == "short-subject-search" and ok(rows)]
        return (sum(v) / len(v), len(v)) if v else (None, 0)
    a = mean("auto_in"); b = {o: mean(o) for o in others}
    cand = [(v[0], o) for o, v in b.items() if v[0]]
    if not cand or not a[0]: print(f'  {p:24s} no comparator'); continue
    best = min(cand)
    flag = "R1" if a[0] > 3 * best[0] else ""
    print(f"  {p:24s} pcrec_in={a[0]:.1f} ({a[1]}) best={best[1]}:{best[0]:.1f}  ratio={a[0]/best[0]:.2f} {flag}")
print("\n== callout_fires evidence (engine_metadata on a match row): default vs _in arm, co-luhn-1m")
for n in ("auto", "auto_in", "jit_deep", "onig_deep"):
    rows = R[n][2].get(("co-luhn", "large-subject-throughput", "co-luhn-1m", "plain"))
    print("  ", n, [ (r["em"] or {}).get("callout_fires") for r in rows][:5], {k: v for k, v in (rows[0]["em"] or {}).items() if "fire" in k or "prime" in k or "deep" in k})
