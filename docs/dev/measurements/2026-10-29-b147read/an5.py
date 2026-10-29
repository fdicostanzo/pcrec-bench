import sys,statistics,glob
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S+"/sentinel@0.1"
for t,ref in (("pcrec_9ae59f5d4_auto-caps-simdna","20261028T161655Z"),("libpcre2_10.46_jit-caps-simdna","20261028T162849Z")):
    fs=sorted(glob.glob(f"{S}/{t}/*2026102*.jsonl"))
    base=recs.load([f for f in fs if ref in f][0])[2]
    for f in fs:
        c=recs.load(f)[2]
        keys=[k for k in base if k in c and base[k][0] and c[k][0]]
        r=[c[k][0]/base[k][0] for k in keys]
        print(t.split('_')[0], f.split('__')[-1][:-6], "n=%d median ratio vs 10-28 opening %.4f"%(len(r),statistics.median(r)))
