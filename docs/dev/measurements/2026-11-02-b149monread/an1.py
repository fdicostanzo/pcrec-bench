# b149monread an1: unusual@0.1 outcome census per record, K134 flips (614d45eb3 -> cb32eda28), the inline-vs-separate row accounting.
import sys, collections
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
R = {n: load(n)[0] for n in NAMES}
print("== records: rows (compile rows / match rows) and trial-1 outcome census")
for n, (s, c, m) in R.items():
    oc = collections.Counter(); 
    for k, rows in m.items():
        oc[(k[1], rows[0]["o"])] += 1
    nrow = sum(len(r) for r in m.values()); ncomp = sum(len(r) for r in c.values())
    print(f"{n:12s} compile_rows={ncomp} match_rows={nrow} cells={len(m)}")
    for k, v in sorted(oc.items()): print(f"     {k[0]:26s} {k[1]:24s} {v}")
print("\n== K134 flips: cell outcome at 614d45eb3 vs cb32eda28 (default arms)")
for a in ("auto", "vm"):
    old, new = R[a + "614"][2], R[a][2]
    flips = collections.Counter(); ex = collections.defaultdict(list)
    for k in sorted(set(old) | set(new)):
        o = old.get(k, [{"o": "ABSENT"}])[0]["o"]; n = new.get(k, [{"o": "ABSENT"}])[0]["o"]
        if o != n:
            flips[(o, n)] += 1; ex[(o, n)].append(k)
    print(f"-- {a}: cells {len(old)} vs {len(new)}")
    for f, v in flips.items():
        print("   ", f, v)
        pc = collections.Counter((k[0], k[1]) for k in ex[f])
        for kk, vv in sorted(pc.items()): print("        ", kk, vv)
    still = collections.Counter()
    for k, rows in new.items():
        if rows[0]["o"] == "gave-up":
            still[(k[0], k[1])] += 1
    print("   still gave-up at cb32eda28:", dict(still))
print("\n== give-up diagnostics at cb32eda28 default arms (first row per cell)")
for a in ("auto", "vm", "auto_in", "vm_in", "auto_inl", "vm_inl"):
    c = collections.Counter()
    for k, rows in R[a][2].items():
        if rows[0]["o"] != "matched-as-expected":
            c[(k[0], k[1], rows[0]["o"], (rows[0]["diag"] or "")[:90])] += 1
    print("--", a)
    for k, v in sorted(c.items()): print("   ", k, v)
print("\n== inline vs separate-TU row accounting")
for a in ("auto", "vm"):
    sep, inl = R[a], R[a + "_inl"]
    for kind, idx in (("match", 2), ("compile", 1)):
        ks, ki = set(sep[idx]), set(inl[idx])
        only_s = sorted(ks - ki); only_i = sorted(ki - ks)
        print(f"-- {a} {kind}: sep={sum(len(sep[idx][k]) for k in ks)} rows/{len(ks)} keys inline={sum(len(inl[idx][k]) for k in ki)} rows/{len(ki)} keys; only-sep={len(only_s)} only-inline={len(only_i)}")
        for k in only_s: print("    only-sep", k, len(sep[idx][k]))
        for k in only_i: print("    only-inl", k, len(inl[idx][k]))
        # row count differences on shared keys
        for k in sorted(ks & ki):
            if len(sep[idx][k]) != len(inl[idx][k]): print("    count-diff", k, len(sep[idx][k]), len(inl[idx][k]))
