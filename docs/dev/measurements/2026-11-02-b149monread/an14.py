# b149monread an14: syntax@0.2 614d45eb3 -> cb32eda28 (auto-caps): program identity (v3) per pattern and the stamp keys that differ on the big movers.
import sys, statistics, collections
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
a = load("pcrec_614d45eb3_auto-caps-simdna", "syntax@0.2")[0]; b = load("pcrec_cb32eda28_auto-caps-simdna", "syntax@0.2")[0]
ident = {}; diffs = {}
for (p, f), rows in b[1].items():
    if f != "plain" or (p, f) not in a[1]: continue
    x, y = a[1][(p, f)][0], rows[0]
    if x["compile_outcome"] != "compiled" or y["compile_outcome"] != "compiled": continue
    mx, my = x["engine_metadata"], y["engine_metadata"]
    ident[p] = mx.get("program_sha256_v3") == my.get("program_sha256_v3")
    diffs[p] = {k: (mx.get(k), my.get(k)) for k in sorted(set(mx) | set(my)) if mx.get(k) != my.get(k) and k not in ("program_sha256", "program_sha256_v3", "abi", "emit_bytes", "emit_code_bytes")}
print("plain patterns compiled at both:", len(ident), "program-identical (v3):", sum(ident.values()), "changed:", len(ident) - sum(ident.values()))
for reg in ("large-subject-throughput", "short-subject-search"):
    for lab, want in (("identical", True), ("changed", False)):
        v = []
        for k, rows in b[2].items():
            if k[1] != reg or k[0] not in ident or ident[k[0]] != want: continue
            o = a[2].get(k)
            if o and o[0]["o"] == rows[0]["o"] == "matched-as-expected" and med(o) and med(rows): v.append(med(rows) / med(o))
        if reg == "large-subject-throughput":
            pass
        # set-level per pattern: use per-subject medians' sum ratio
        sums = []
        for p in ident:
            if ident[p] != want: continue
            ks = [k for k in b[2] if k[0] == p and k[1] == reg and k in a[2] and a[2][k][0]["o"] == b[2][k][0]["o"] == "matched-as-expected" and med(a[2][k]) and med(b[2][k])]
            if ks: sums.append(sum(med(b[2][k]) for k in ks) / sum(med(a[2][k]) for k in ks))
        sums.sort()
        if sums: print(f"  {reg:26s} {lab:9s} patterns={len(sums)} set-sum cb/614 median={statistics.median(sums):.4f} p5={sums[int(.05*(len(sums)-1))]:.4f} p95={sums[int(.95*(len(sums)-1))]:.4f} min={sums[0]:.3f}")
print("\nbig movers' differing stamps:")
for p in ("mod-i", "mod-r", "cls-n-uc", "grp-callout", "mod-s", "esc-octal-0", "asr-nwb", "cls-i-class", "asr-wb", "cls-dot", "mod-reset", "anc-m-dollar", "cls-s-uc", "cls-range"):
    print(f"  {p:14s} identical={ident.get(p)} engine={b[1][(p,'plain')][0]['engine_metadata'].get('engine')} diffs={diffs.get(p)}")
c = collections.Counter()
for p, d in diffs.items():
    if not ident[p]:
        for k in d: c[k] += 1
print("\nstamp keys that differ across all changed plain patterns:", dict(c))
