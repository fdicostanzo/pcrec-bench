import sys,statistics,collections,glob
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
def pct(v,q):
    v=sorted(v); return v[min(len(v)-1,int(q*len(v)))]
S=recs.S
a=recs.load(glob.glob(S+"/syntax@0.1/pcrec_9ae59f5d4_auto-caps-simdna/*.jsonl")[0])
print("9ae syntax@0.1 file:",glob.glob(S+"/syntax@0.1/pcrec_9ae59f5d4_auto-caps-simdna/*.jsonl")[0].split("__")[-1])
for cfg in ("auto-caps","auto-nocaps"):
    b=recs.load(glob.glob(S+f"/syntax@0.2/pcrec_614d45eb3_{cfg}-simdna/*.jsonl")[0])
    ref=a if cfg=="auto-caps" else None
    if ref is None:
        # nocaps: use 9ae caps as the shape-only comparator? no -- skip
        continue
    ac,bc=a[2],b[2]
    keys=[k for k in ac if k in bc and ac[k][0] and bc[k][0] and set(ac[k][2])<={"matched-as-expected"} and set(bc[k][2])<={"matched-as-expected"}]
    sa=collections.defaultdict(float); sb=collections.defaultdict(float)
    for k in keys: sa[(k[0],k[2],k[3])]+=ac[k][0]; sb[(k[0],k[2],k[3])]+=bc[k][0]
    r={k:sb[k]/sa[k] for k in sa}
    movers={"asr-k-uc","cls-s-uc","cls-range","esc-tab","esc-nl","esc-cr","grp-callout"}
    print(f"== {cfg}: 614 syntax@0.2 / 9ae syntax@0.1 (10-26), set-cells over common clean subjects: n={len(r)}")
    byreg=collections.defaultdict(list)
    for k,v in r.items():
        if k[0] not in movers: byreg[(k[1],k[2])].append(v)
    for g,v in sorted(byreg.items()):
        print("  non-mover",g,"n=%d median %.4f p5 %.3f p95 %.3f max %.3f min %.3f"%(len(v),statistics.median(v),pct(v,.05),pct(v,.95),max(v),min(v)))
    print("  movers:")
    for k,v in sorted(r.items()):
        if k[0] in movers: print("   ",k,"x%.3f"%v,"%.1f -> %.1f"%(sa[k],sb[k]))
    out=sorted(((v,k) for k,v in r.items() if k[0] not in movers), key=lambda t:-abs(t[0]-1))[:8]
    print("  largest non-mover deviations:",[(k,round(v,3)) for v,k in out])
    only_b=sorted({k[0] for k in bc if k not in ac})
    print("  cells only in 0.2:", collections.Counter((k[1],k[2]) for k in bc if k not in ac).most_common(4))
    # cells with non-expected outcomes
    bad=collections.Counter()
    for k,v in bc.items():
        for o,n in v[2].items():
            if o!="matched-as-expected": bad[(o)]+=n
    print("  614 outcomes other than matched-as-expected:",dict(bad))
