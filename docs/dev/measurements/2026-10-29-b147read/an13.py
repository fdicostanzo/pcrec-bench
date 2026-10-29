import sys,glob,statistics
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S+"/sentinel@0.1/"
for t,old,new in (("pcrec_9ae59f5d4_auto-caps-simdna","20261026T000001Z","20261028T161655Z"),("libpcre2_10.46_jit-caps-simdna","20261026T001717Z","20261028T162849Z")):
    a=recs.load(glob.glob(S+t+f"/*{old}*")[0])[2]; b=recs.load(glob.glob(S+t+f"/*{new}*")[0])[2]
    ks=[k for k in a if k in b and a[k][0] and b[k][0]]
    d=[b[k][0]-a[k][0] for k in ks]
    print(t.split('_')[0],"n=%d  median delta %.2f ns (p25 %.2f p75 %.2f); median old %.1f ns"%(len(d),statistics.median(d),sorted(d)[len(d)//4],sorted(d)[3*len(d)//4],statistics.median(a[k][0] for k in ks)))
