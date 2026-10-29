import sys,glob,statistics,json,collections
S="/home/pcrec/projects/pcrec-bench/worktrees/b147read/store/records"
fs=[(f.split("/")[-2].replace("-simdna",""),f.split("__")[-1][:-6],f) for f in sorted(glob.glob(S+"/capability@0.[23]/pcrec_*/*ryzen7700x*.jsonl"))]
for pat in ("tail-space-eol","tail-dotstar-txt","tail-ext-lower-txt"):
  print("==",pat)
  for t,ts,f in fs:
    if "vm-caps" in t: continue
    v=collections.defaultdict(list); by={}
    for l in open(f):
        d=json.loads(l)
        if d["kind"]=="match" and d["pattern_id"]==pat and d["regime"]=="large-subject-throughput" and d.get("timing"):
            tm=d["timing"]; v[d["subject_id"]].append(tm["elapsed_ns"]/tm["iterations"]); by[d["subject_id"]]=tm["bytes_processed"]/tm["iterations"]
    tot=sum(statistics.median(x) for x in v.values())
    big=max(v,key=lambda s:statistics.median(v[s]))
    print(" %-22s %s total %9.0f ns; biggest %s %.0f ns over %d B = %.3f ns/B"%(t,ts,tot,big,statistics.median(v[big]),by[big],statistics.median(v[big])/by[big]))
