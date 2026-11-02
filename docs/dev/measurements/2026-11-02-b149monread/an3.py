# b149monread an3: large-cell cross-pin movers; inline vs separate-TU; the _in arm; deep-arm ladder vs the L9 scratch numbers.
import sys, collections, statistics
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
R = {n: load(n)[0] for n in NAMES}
def spread(rows):
    v = sorted(r["ns"] for r in rows if r["ns"]); return (v[0], v[-1]) if v else (None, None)
print("== large-subject cells answered at both pins: ratio cb32/614 (auto), with min-max per side")
rows_ = []
for k, rows in R["auto"][2].items():
    if k[1] != "large-subject-throughput": continue
    o = R["auto614"][2][k]
    if o[0]["o"] == "matched-as-expected" and rows[0]["o"] == "matched-as-expected":
        rows_.append((med(rows) / med(o), k, med(o), med(rows), spread(o), spread(rows)))
for r in sorted(rows_)[:8] + sorted(rows_)[-6:]:
    print(f"  x{r[0]:.3f} {r[1][0]:24s} {r[1][2]:16s} 614={r[2]:.4g} ({r[4][0]:.4g}-{r[4][1]:.4g}) cb={r[3]:.4g} ({r[5][0]:.4g}-{r[5][1]:.4g})")
print("   (count of large cells with ratio<0.8:", sum(1 for r in rows_ if r[0] < 0.8), ">1.1:", sum(1 for r in rows_ if r[0] > 1.1), "of", len(rows_), ")")
print("\n== inline vs separate-TU (same pin cb32eda28, other window slot): per-pattern set-sum of short-subject ns/call (matched cells)")
for a in ("auto", "vm"):
    for pat in ("co-luhn", "co-luhn-pass", "co-luhn-twin", "co-luhn-nofn", "co-isbn", "co-isbn-pass", "co-isbn-twin", "co-member", "co-member-pass", "co-member-twin", "co-netstr", "co-netstr-assist", "co-netstr-twin", "floor", "cscan"):
        s, i = R[a][2], R[a + "_inl"][2]
        ks = [k for k in s if k[0] == pat and k[1] == "short-subject-search" and k in i and s[k][0]["o"] == i[k][0]["o"] == "matched-as-expected"]
        if not ks: continue
        ss = sum(med(s[k]) for k in ks); si = sum(med(i[k]) for k in ks)
        print(f"  {a:4s} {pat:18s} n={len(ks)} sep={ss:.1f} inl={si:.1f} inl/sep={si/ss:.4f}")
print("\n   throughput 1 MB subjects (callout members):")
for a in ("auto", "vm"):
    for pat, sub in (("co-luhn", "co-luhn-1m"), ("co-luhn-pass", "co-luhn-1m"), ("co-luhn-twin", "co-luhn-1m"), ("co-isbn", "co-isbn-1m"), ("co-isbn-pass", "co-isbn-1m"), ("co-isbn-twin", "co-isbn-1m"), ("co-member", "co-member-1m"), ("co-member-pass", "co-member-1m"), ("co-member-twin", "co-member-1m"), ("co-netstr", "co-netstr-1m"), ("co-netstr-assist", "co-netstr-1m")):
        k = (pat, "large-subject-throughput", sub, "plain")
        s, i = R[a][2].get(k), R[a + "_inl"][2].get(k)
        if s and i:
            print(f"  {a:4s} {pat:18s} {sub:13s} sep={med(s):.6g} ({spread(s)[0]:.5g}-{spread(s)[1]:.5g}) inl={med(i):.6g} ({spread(i)[0]:.5g}-{spread(i)[1]:.5g}) inl/sep={med(i)/med(s):.4f} outcomes {s[0]['o'][:8]}/{i[0]['o'][:8]}")
print("\n== callout-site overhead per 1 MB (pass - twin), ns; sep vs inline (vm)")
for fam, sub in (("co-luhn", "co-luhn-1m"), ("co-isbn", "co-isbn-1m"), ("co-member", "co-member-1m")):
    for a in ("vm", "vm_inl", "auto", "auto_inl"):
        p = R[a][2].get((fam + "-pass", "large-subject-throughput", sub, "plain")); t = R[a][2].get((fam + "-twin", "large-subject-throughput", sub, "plain")); r_ = R[a][2].get((fam, "large-subject-throughput", sub, "plain"))
        if p and t and r_: print(f"  {fam:10s} {a:9s} real={med(r_):.0f} pass={med(p):.0f} twin={med(t):.0f} pass-twin={med(p)-med(t):.0f} real-pass={med(r_)-med(p):.0f}")
print("\n== the _in arm vs the default arm on cells the default arm answers (cb32eda28): set ratios")
for a, b in (("auto", "auto_in"), ("vm", "vm_in")):
    for reg in ("short-subject-search", "large-subject-throughput"):
        rat = []
        for k, rows in R[b][2].items():
            if k[1] != reg: continue
            o = R[a][2][k]
            if o[0]["o"] == rows[0]["o"] == "matched-as-expected" and med(o) and med(rows): rat.append(med(rows) / med(o))
        rat.sort(); print(f"  {b:7s}/{a:5s} {reg:26s} n={len(rat)} median={statistics.median(rat):.4f} p5={rat[int(.05*len(rat))]:.4f} p95={rat[int(.95*(len(rat)-1))]:.4f}")
print("\n== deep-arm nest-brace ladder (cscan-onig), medians, vs the L9 scratch numbers (scratch at 614d45eb3, load ~1.5)")
L9 = {"interp": {"nest-brace-128": 226e3, "nest-brace-512": 3.0e6, "nest-brace-2k": 44.6e6, "nest-brace-8k": 1.64e9, "nest-brace-32k": 31.0e9},
      "onig": {"nest-brace-128": 144e3, "nest-brace-512": 2.2e6, "nest-brace-2k": 34.7e6, "nest-brace-8k": 0.56e9, "nest-brace-32k": 9.2e9},
      "jit": {"nest-brace-128": 2.7e3, "nest-brace-512": 11e3, "nest-brace-2k": 46e3, "nest-brace-8k": 186e3, "nest-brace-32k": 772e3, "nest-brace-100k": 2.43e6},
      "pcrec_in": {"nest-brace-128": 11.5e3, "nest-brace-512": 45e3, "nest-brace-2k": 184e3, "nest-brace-8k": 742e3, "nest-brace-32k": 3.18e6, "nest-brace-100k": 11.6e6}}
for nm, a in (("interp", "interp_deep"), ("onig", "onig_deep"), ("jit", "jit_deep"), ("pcrec_in", "auto_in"), ("pcrec_in", "vm_in")):
    print("--", a)
    for s in ("nest-brace-128", "nest-brace-512", "nest-brace-2k", "nest-brace-8k", "nest-brace-32k", "nest-brace-100k"):
        k = ("cscan-onig", "large-subject-throughput", s, "plain"); rows = R[a][2][k]
        l9 = L9[nm].get(s)
        m = med(rows)
        print(f"   {s:16s} {rows[0]['o'][:10]:10s} median={m if m is None else format(m, '.5g')} L9={l9} ratio={'' if not (m and l9) else format(m / l9, '.3f')} {(rows[0]['diag'] or '')[:70] if rows[0]['o']!='matched-as-expected' else ''}")
