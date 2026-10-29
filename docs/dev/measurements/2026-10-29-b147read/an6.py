import sys,glob,collections,json
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S+"/sentinel@0.1/pcrec_9ae59f5d4_auto-caps-simdna"
a=recs.load(glob.glob(S+"/*20261026T000001Z*")[0]); b=recs.load(glob.glob(S+"/*20261028T161655Z*")[0])
ca,cb=a[1],b[1]
diff=collections.Counter()
for k in ca:
    if k not in cb: diff["missing"]+=1; continue
    x,y=ca[k],cb[k]
    for f in ("artifact_bytes",):
        if x.get(f)!=y.get(f): diff[f]+=1
    mx,my=x.get("engine_metadata",{}),y.get("engine_metadata",{})
    for f in set(mx)|set(my):
        if mx.get(f)!=my.get(f): diff["em."+f]+=1
print(len(ca),diff)
sa,sb=a[0],b[0]
for path in (("run","harness_commit"),("run","driver_build_flags"),("testee","build_flags"),("testee","engine_commit"),("environment","compiler"),("environment","kernel"),("environment","cpu_mhz"),("environment","turbo"),("environment","governor")):
    def g(s):
        for p in path: s=s.get(p,{}) if isinstance(s,dict) else {}
        return s
    print(path, "\n  A:",str(g(sa))[:300],"\n  B:",str(g(sb))[:300])
print(sb["run"]["driver_build_flags"][-300:])
d=[(k[0],ca[k]["artifact_bytes"],cb[k]["artifact_bytes"]) for k in list(ca)[:5]]
print(d)
import statistics
print("artifact_bytes delta median",statistics.median(cb[k]["artifact_bytes"]-ca[k]["artifact_bytes"] for k in ca))
