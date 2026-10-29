import sys,glob
sys.path.insert(0,"/home/pcrec/projects/pcrec-bench/worktrees/b147read/docs/dev/measurements/2026-10-29-b147read")
import recs
S=recs.S
a=recs.load(glob.glob(S+"/capability@0.3/pcrec_9ae59f5d4_auto-caps-simdna/*.jsonl")[0])[1]
b=recs.load(glob.glob(S+"/capability@0.3/pcrec_614d45eb3_auto-caps-simdna/*.jsonl")[0])[1]
fs=("engine","dfa_scan","dfa_scan_edge","scan_edges","scan_edges_match","dfa_prefilter","dfa_start","dfa_match","req_why","emit_bytes","emit_code_bytes","artifact_bytes")
for p in ("tail-space-eol","tail-dotstar-txt","tail-ext-lower-txt","wild-logparse-base10num-noatomic","wild-logparse-base10num-grok","wild-logparse-winpath-grok","wild-secrets-username-password-pair","wild-codegrammar-json-number-extended"):
    k=(p,"plain")
    x,y=a[k],b[k]
    xm,ym=dict(x["engine_metadata"]),dict(y["engine_metadata"]); xm["artifact_bytes"]=x["artifact_bytes"]; ym["artifact_bytes"]=y["artifact_bytes"]
    print(p); 
    for f in fs:
        if xm.get(f)!=ym.get(f): print("    ",f,xm.get(f),"->",ym.get(f))
        elif f in ("engine","dfa_scan","dfa_prefilter"): print("    ",f,xm.get(f),"(same)")
