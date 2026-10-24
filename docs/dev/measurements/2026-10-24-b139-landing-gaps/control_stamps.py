#!/usr/bin/env python3
# b139gaps / control_stamps.py -- CONTROL: my compile-only stamps (compile_all.py output) vs the committed
# store's compile-row engine_metadata at pin 6b2dbd3e (ryzen7700x), plain form. Prints mismatches.
import json,csv,re,collections,os
ROOT="/home/pcrec/projects/pcrec-bench"; CD="/var/tmp/pcrecbench/b139gaps/c"
idx=list(csv.DictReader(open(ROOT+"/store/index.tsv"),delimiter="\t"))
mp={"auto-caps-simdna":"auto","auto-nocaps-simdna":"nocaps","vm-caps-simdna":"vm","auto-caps-simdna_utf8":"auto","auto-nocaps-simdna_utf8":"nocaps","vm-caps-simdna_utf8":"vm"}
man={(m["cfg"],m["set"],m["pattern"]):m["rc"] for m in json.load(open(CD+"/manifest.json"))}
ok=bad=miss=0; ex=[]
for r in idx:
    if "6b2dbd3e" not in r["testee_id"] or r["machine_id"]!="ryzen7700x" or r["status"]=="inconclusive-spread" and False: continue
    suf=r["testee_id"].split("6b2dbd3e_")[1]
    if suf not in mp: continue
    cfg=mp[suf]; s=r["subbench"].split("-")[0]
    seen=set()
    for l in open(ROOT+"/store/"+r["path"]):
        j=json.loads(l)
        if j.get("kind")!="compile" or j.get("form") not in (None,"plain"): continue
        if j["pattern_id"] in seen: continue
        seen.add(j["pattern_id"])
        f="%s/%s/%s/%s.c"%(CD,cfg,s,j["pattern_id"])
        if j.get("compile_outcome")!="compiled":
            if man.get((cfg,s,j["pattern_id"]),0)==0: bad+=1; ex.append(("store-refused-mine-compiled",cfg,s,j["pattern_id"]))
            else: ok+=1
            continue
        if not os.path.exists(f) or man[(cfg,s,j["pattern_id"])]!=0: miss+=1; ex.append(("mine-missing",cfg,s,j["pattern_id"])); continue
        t=open(f,errors="replace").read(); m=j["engine_metadata"]
        g=lambda k:(re.search(r'#define %s "?([^"\n]*)"?'%k,t) or [0,None])[1]
        mine=(g("RX_ENGINE"),g("RX_DFA_PREFILTER"),g("RX_VM_START_SCAN"))
        th=(m.get("engine"),m.get("dfa_prefilter"),m.get("vm_start_scan"))
        if tuple(map(str,mine))==tuple(map(str,th)): ok+=1
        else: bad+=1; ex.append((mine,th,cfg,s,j["pattern_id"]))
print("ok",ok,"bad",bad,"missing",miss)
for e in ex[:20]: print(e)
