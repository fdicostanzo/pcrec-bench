import sys,statistics,glob,collections
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S+"/sentinel@0.1"
def pct(v,q):
    v=sorted(v); return v[min(len(v)-1,int(q*len(v)))]
tids=["pcrec_614d45eb3_auto-caps-simdna","pcrec_614d45eb3_auto-nocaps-simdna","pcrec_9ae59f5d4_auto-caps-simdna","libpcre2_10.46_jit-caps-simdna"]
for t in tids:
    fs=sorted(glob.glob(f"{S}/{t}/*20261028T*.jsonl"))
    assert len(fs)==2,(t,fs)
    o=recs.load(fs[0])[2]; c=recs.load(fs[1])[2]
    keys=[k for k in o if k in c and o[k][0] and c[k][0]]
    r=[c[k][0]/o[k][0] for k in keys]
    # set sums per (pattern,regime)
    so=collections.defaultdict(float); sc=collections.defaultdict(float)
    for k in keys: so[(k[0],k[2])]+=o[k][0]; sc[(k[0],k[2])]+=c[k][0]
    sr=[sc[k]/so[k] for k in so]
    byreg={}
    for k in so: byreg.setdefault(k[1],[]).append(sc[k]/so[k])
    print(f"{t}: closing/opening  subject-cells n={len(r)} median {statistics.median(r):.4f} p5 {pct(r,.05):.3f} p95 {pct(r,.95):.3f} min {min(r):.3f} max {max(r):.3f}; set-cells n={len(sr)} median {statistics.median(sr):.4f} p5 {pct(sr,.05):.3f} p95 {pct(sr,.95):.3f} min {min(sr):.3f} max {max(sr):.3f} |dev|>5%: {sum(abs(x-1)>.05 for x in sr)}; by regime:",{k:round(statistics.median(v),4) for k,v in byreg.items()})
    print("   files",[f.split('__')[-1] for f in fs])
