# b149monread an15: per-cell outcome equality across arms (trial-1 outcome, all 5 trials identical?).
import sys
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
R = {n: load(n)[0] for n in NAMES}
def eq(a, b):
    A, B = R[a][2], R[b][2]; ks = set(A) & set(B); d = [k for k in ks if [r["o"] for r in A[k]] != [r["o"] for r in B[k]]]
    print(f"  {a:9s} vs {b:9s} shared cells={len(ks)} outcome-differing (any of 5 trials)={len(d)} {sorted(d)[:3]}")
for a, b in (("auto", "auto_inl"), ("vm", "vm_inl"), ("auto", "vm"), ("auto614", "vm614"), ("auto_in", "vm_in"), ("auto", "auto_in"), ("jit_deep", "auto_in"), ("interp_deep", "jit_deep"), ("onig_deep", "jit_deep")):
    eq(a, b)
# trials per cell
import collections
print({n: collections.Counter(len(v) for v in R[n][2].values()) for n in ("auto", "interp_deep", "onig_deep")})
