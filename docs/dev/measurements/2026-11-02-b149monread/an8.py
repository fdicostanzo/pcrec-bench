# b149monread an8: capability/syntax cross-arm reads from the committed report TSVs (no store load).
import sys, collections, statistics
R = "reports/2026-11-02-"
def load(f):
    d = {}
    for l in open(f):
        if l.startswith("#") or l.startswith("section"): continue
        c = l.rstrip("\n").split("\t")
        if len(c) < 12: continue
        if c[0] in ("rank", "rank_yes", "rank_no") and c[10] == "median_ns" and c[2] == "(set)":
            d.setdefault((c[1], c[3], c[4]), {})[c[6]] = (float(c[11]), c[7])
    return d
def short(t): return t.replace("pcrec_", "").replace("_auto-", ":").replace("-simdna", "")
cap = load(R + "capability-0.4-ryzen7700x-noedge-cb32eda28.tsv")
A, N = "pcrec_cb32eda28_auto-caps-simdna", "pcrec_cb32eda28_auto-caps-simdna_noedge"
print("== capability@0.4: noedge / auto (same pin cb32eda28; auto record 2026-11-01 13:39Z = W2, noedge 2026-11-02 15:02Z = this window: CROSS-WINDOW)")
rat = []
for k, v in sorted(cap.items()):
    if A in v and N in v: rat.append((v[N][0] / v[A][0], k, v[A][0], v[N][0]))
print("cells with both:", len(rat))
for pat in ("wild-logparse-base10num-noatomic", "wild-logparse-base10num-grok", "wild-secrets-username-password-pair"):
    for r in rat:
        if r[1][0] == pat: print(f"  {pat:40s} {r[1][1][:24]:24s} {r[1][2]:12s} auto={r[2]:.6g} noedge={r[3]:.6g} noedge/auto={r[0]:.4f}")
for reg in ("short-subject-search", "large-subject-throughput", "match-compliance"):
    v = sorted(r[0] for r in rat if r[1][1] == reg)
    if v: print(f"  all cells {reg:26s} n={len(v)} median={statistics.median(v):.4f} p5={v[int(.05*(len(v)-1))]:.4f} p95={v[int(.95*(len(v)-1))]:.4f}")
print("  largest noedge/auto movers (large + short):")
for r in sorted(rat, key=lambda x: -abs(x[0] - 1))[:14]:
    print(f"    x{r[0]:.3f} {r[1][0]:40s} {r[1][1][:22]:22s} {r[1][2]:6s} auto={r[2]:.5g} noedge={r[3]:.5g}")
syn = load(R + "syntax-0.2-ryzen7700x-cb32eda28.tsv")
P4a = "pcrec_614d45eb3_auto-caps-simdna"; P4n = "pcrec_614d45eb3_auto-nocaps-simdna"
Ca = "pcrec_cb32eda28_auto-caps-simdna"; Cn = "pcrec_cb32eda28_auto-nocaps-simdna"; Ce = "pcrec_cb32eda28_auto-caps-simdna_noedge"
print("\n== syntax@0.2: the named rows (614d45eb3 auto@10-28 | cb32eda28 auto | cb32eda28 noedge | cb32eda28 nocaps)")
for pat in ("cls-s-uc", "cls-range"):
    for k, v in sorted(syn.items()):
        if k[0] == pat:
            g = lambda t: f"{v[t][0]:.6g}" if t in v else "-"
            f = lambda a, b: f"{v[b][0]/v[a][0]:.3f}" if a in v and b in v else "-"
            print(f"  {pat:10s} {k[1][:22]:22s} {k[2]:6s} 614={g(P4a)} cb={g(Ca)} noedge={g(Ce)} nocaps cb={g(Cn)} | cb/614={f(P4a,Ca)} noedge/cb={f(Ca,Ce)} 614n->cbn={f(P4n,Cn)}")
print("\n== syntax: noedge/auto (same window, adjacent cells) over all rows; cb/614 over all rows")
rat = [(v[Ce][0] / v[Ca][0], k) for k, v in syn.items() if Ca in v and Ce in v]
for reg in ("short-subject-search", "large-subject-throughput", "match-compliance"):
    x = sorted(r[0] for r in rat if r[1][1] == reg)
    if x: print(f"  noedge/auto {reg:26s} n={len(x)} median={statistics.median(x):.4f} p5={x[int(.05*(len(x)-1))]:.4f} p95={x[int(.95*(len(x)-1))]:.4f}")
rat2 = [(v[Ca][0] / v[P4a][0], k) for k, v in syn.items() if Ca in v and P4a in v]
for reg in ("short-subject-search", "large-subject-throughput", "match-compliance"):
    x = sorted(r[0] for r in rat2 if r[1][1] == reg)
    if x: print(f"  cb/614 auto {reg:26s} n={len(x)} median={statistics.median(x):.4f} p5={x[int(.05*(len(x)-1))]:.4f} p95={x[int(.95*(len(x)-1))]:.4f}")
print("  noedge/auto movers beyond 1.1 or below 0.9 (large):")
for r in sorted([r for r in rat if r[1][1] == "large-subject-throughput" and abs(r[0] - 1) > .1], key=lambda x: -abs(x[0] - 1))[:12]:
    v = syn[r[1]]; print(f"    x{r[0]:.3f} {r[1][0]:20s} auto={v[Ca][0]:.5g} noedge={v[Ce][0]:.5g}")
print("\n== syntax cb/614 auto movers (large <0.9 or >1.1; short <0.85 or >1.15)")
for r in sorted(rat2, key=lambda x: x[0]):
    k = r[1]; v = syn[k]
    if (k[1] == "large-subject-throughput" and (r[0] < .9 or r[0] > 1.1)) or (k[1] == "short-subject-search" and (r[0] < .85 or r[0] > 1.15)):
        print(f"  x{r[0]:.3f} {k[0]:18s} {k[1][:22]:22s} 614={v[P4a][0]:.5g} cb={v[Ca][0]:.5g}")
