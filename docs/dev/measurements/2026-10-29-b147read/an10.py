import sys,glob,json,collections
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S
a=recs.load(glob.glob(S+"/syntax@0.1/pcrec_9ae59f5d4_auto-caps-simdna/*.jsonl")[0])[1]
for cfg in ("auto-caps",):
    b=recs.load(glob.glob(S+f"/syntax@0.2/pcrec_614d45eb3_{cfg}-simdna/*.jsonl")[0])[1]
    ch=[];same=0;miss=[]
    for k in sorted(set(a)|set(b)):
        x,y=a.get(k),b.get(k)
        if not x or not y or x.get("compile_outcome")!="compiled" or y.get("compile_outcome")!="compiled":
            miss.append((k,(x or {}).get("compile_outcome"),(y or {}).get("compile_outcome"))); continue
        hx,hy=x["engine_metadata"].get("program_sha256_v3"),y["engine_metadata"].get("program_sha256_v3")
        if hx==hy: same+=1
        else: ch.append(k)
    print(cfg,"compiled-both identical(v3)",same,"changed",len(ch),ch)
    print(" not compiled in both:",[m for m in miss if m[1]!=m[2]] , "n both-refused:",sum(m[1]==m[2] for m in miss))
    k=("grp-callout","plain"); print(" grp-callout compile row:", {f:b[k].get(f) for f in ("compile_outcome","artifact_bytes")}, {f:b[k]["engine_metadata"].get(f) for f in ("callout_bindings","callout_binding","engine","engine_sel","engine_why","emit_bytes","emit_code_bytes","vm_program_bytes","dfa_prefilter","req_why") if k in b})
    print(" ",sorted(b[k]["engine_metadata"].items())[:80] if k in b else "")
