# b149monread an7: cscan / wild-* large cells answered at both pins (the K134 cost candidates), both routes.
import sys
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
R = {n: load(n)[0] for n in ("auto614", "auto", "vm614", "vm", "auto_in", "vm_in")}
for pat in ("cscan", "cscan-onig", "wild-sexp-balanced", "wild-json-validate"):
    for k in sorted(R["auto"][2]):
        if k[0] != pat or k[1] != "large-subject-throughput": continue
        o, n = R["auto614"][2][k], R["auto"][2][k]
        if o[0]["o"] == n[0]["o"] == "matched-as-expected":
            ov, nv = R["vm614"][2][k], R["vm"][2][k]
            sp = lambda rows: "%.5g-%.5g" % (min(r["ns"] for r in rows), max(r["ns"] for r in rows))
            print(f"  {pat:20s} {k[2]:16s} auto x{med(n)/med(o):.3f} ({sp(o)} -> {sp(n)})  vm x{med(nv)/med(ov):.3f}")
