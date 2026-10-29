import json,glob,sys
S="/home/pcrec/projects/pcrec-bench/worktrees/b147read/store/records"
fs=[]
for sb in ("capability@0.3","syntax@0.2","sentinel@0.1"):
    for f in sorted(glob.glob(f"{S}/{sb}/*/*2026102[89]T*.jsonl")):
        fs.append(f)
for f in fs:
    d=json.loads(open(f).readline())
    e=d["environment"]; ta=d.get("trial_agreement",{})
    o=e["occupancy"]
    print(f.split("/")[-1][:-6].replace("__ryzen7700x",""))
    print("   status",d.get("status"),"| load b/a %.2f/%.2f (%s) | occ before %s max %.1f tgt %.1f | after %s max %.1f tgt %.1f | trials %s"%(
        e["load"]["before"]["load1"],e["load"]["after"]["load1"],e["load"]["verdict"],o["before"]["verdict"],o["before"]["max_busy_pct"],o["before"]["target_busy_pct"],o["after"]["verdict"],o["after"]["max_busy_pct"],o["after"]["target_busy_pct"],d.get("run",{}).get("trials","?")),
        "| agreement:",{k:ta.get(k) for k in ("verdict","rule","n_groups","groups_failing") if k in ta} or list(ta)[:6])
