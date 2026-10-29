import sys,glob,collections
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S
res={}
for t in ("pcrec_614d45eb3_auto-caps-simdna","pcrec_614d45eb3_auto-nocaps-simdna","pcrec_9ae59f5d4_auto-caps-simdna","pcrec_9ae59f5d4_auto-nocaps-simdna"):
    c=recs.load(glob.glob(S+f"/capability@0.3/{t}/*.jsonl")[0])[2]
    bad=collections.defaultdict(collections.Counter)
    for k,v in c.items():
        for o,n in v[2].items():
            if o!="matched-as-expected": bad[(k[0],k[1])][o]+=n
    res[t]=bad
    print(t,sum(sum(v.values()) for v in bad.values()),"non-expected rows over",len(bad),"cells")
    for k,v in sorted(bad.items()): print("   ",k,dict(v))
print("identical key sets:",len({frozenset((k,tuple(sorted(v.items()))) for k,v in b.items()) for b in res.values()}))
