import sys,glob,statistics,csv
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S+"/sentinel@0.1/"
def get(t,stamp): return recs.load(glob.glob(S+t+f"/*{stamp}*")[0])
a=get("pcrec_9ae59f5d4_auto-caps-simdna","20261028T161655Z"); b=get("pcrec_614d45eb3_auto-caps-simdna","20261028T161100Z")
ka=[k for k in a[2] if k in b[2] and a[2][k][0] and b[2][k][0]]
r=[b[2][k][0]/a[2][k][0] for k in ka]
idn=sum(a[1][k]["engine_metadata"]["program_sha256_v3"]==b[1][k]["engine_metadata"]["program_sha256_v3"] for k in a[1] if k in b[1])
print("sentinel 614/9ae caps opening pass: subject-cells",len(r),"median %.4f p5 %.3f p95 %.3f ; patterns v3-identical %d of %d"%(statistics.median(r),sorted(r)[int(.05*len(r))],sorted(r)[int(.95*len(r))],idn,len(a[1])))
a2=get("pcrec_9ae59f5d4_auto-caps-simdna","20261028T224715Z"); b2=get("pcrec_614d45eb3_auto-caps-simdna","20261028T224116Z")
r2=[b2[2][k][0]/a2[2][k][0] for k in ka]
print("closing pass: median %.4f"%statistics.median(r2))
# null stats by regime from the capability TSV d119
T="/home/pcrec/projects/pcrec-bench/worktrees/b147read/reports/2026-10-29-capability-0.3-ryzen7700x-first-614d45eb3.tsv"
def kv(s): return dict(p.split("=",1) for p in s.split("; ") if "=" in p)
byreg={}
for rw in csv.reader(open(T),delimiter="\t"):
    if rw and rw[0]=="d119":
        d=kv(rw[16])
        if d["identity"]=="identical": byreg.setdefault(rw[3],[]).append(float(d["delta_pct"]))
for g,v in byreg.items():
    v.sort(); print(g,"n=%d median %.2f%% p5 %.2f p95 %.2f; |d|>5%%: %d; >10%%: %d"%(len(v),statistics.median(v),v[int(.05*len(v))],v[int(.95*len(v))],sum(abs(x)>5 for x in v),sum(abs(x)>10 for x in v)))
