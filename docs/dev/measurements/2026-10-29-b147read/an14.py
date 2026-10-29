import sys,glob,collections,json
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S
for cfg in ("auto-caps","auto-nocaps"):
    b=recs.load(glob.glob(S+f"/syntax@0.2/pcrec_614d45eb3_{cfg}-simdna/*.jsonl")[0])[2]
    bad=collections.defaultdict(collections.Counter)
    for k,v in b.items():
        for o,n in v[2].items():
            if o!="matched-as-expected": bad[(k[0],k[2],k[3])][o]+=n
    print(cfg,{k:dict(v) for k,v in sorted(bad.items())})
    gc=collections.Counter()
    for k,v in b.items():
        if k[0]=="grp-callout":
            for o,n in v[2].items(): gc[(k[2],k[3],o)]+=n
    print("  grp-callout outcomes",dict(gc))
a=recs.load(glob.glob(S+"/syntax@0.1/pcrec_9ae59f5d4_auto-caps-simdna/*.jsonl")[0])[2]
bad=collections.defaultdict(collections.Counter)
for k,v in a.items():
    for o,n in v[2].items():
        if o!="matched-as-expected": bad[(k[0],k[2],k[3])][o]+=n
print("9ae syntax@0.1 caps non-expected:",{k:dict(v) for k,v in sorted(bad.items())})
