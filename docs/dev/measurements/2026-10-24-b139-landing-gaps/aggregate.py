#!/usr/bin/env python3
# b139gaps / aggregate.py -- source header (for archiving under docs/dev/measurements/)
# Reads cells.tsv (landings.py) and (a) CONTROL: compares the cell universe with the committed store's match
# rows at 6b2dbd3e (ryzen7700x) per set/config; (b) drops (cfg,set,pattern) the STORE shows as refused/absent;
# (c) prints the result groups. Threshold: mean gap <= 8 and dominant share > 0.5 (my reading of "one dominant
# gap value covering most landings"); near-miss: mean gap <= 16.
import csv,json,collections,sys
ROOT="/home/pcrec/projects/pcrec-bench"; OUT="/var/tmp/pcrecbench/b139gaps"
idx=list(csv.DictReader(open(ROOT+"/store/index.tsv"),delimiter="\t"))
mp={"auto-caps-simdna":"auto","auto-nocaps-simdna":"nocaps","vm-caps-simdna":"vm","auto-caps-simdna_utf8":"auto","auto-nocaps-simdna_utf8":"nocaps","vm-caps-simdna_utf8":"vm"}
store=collections.defaultdict(set)   # (cfg,setid) -> {(pattern,regime,subject)} of plain-form search-regime match rows
rmap={"short-subject-search":"search_short","large-subject-throughput":"throughput"}
rec=[]
for r in idx:
    if "6b2dbd3e" not in r["testee_id"] or r["machine_id"]!="ryzen7700x": continue
    suf=r["testee_id"].split("6b2dbd3e_")[1]
    if suf not in mp: continue
    rec.append((mp[suf],r["subbench"],r["version"],r["path"],r["status"]))
regs=collections.Counter()
for cfg,sb,ver,path,st in rec:
    setid=sb.split("-")[0]+"@"+ver
    for l in open(ROOT+"/store/"+path):
        j=json.loads(l)
        if j.get("kind")!="match": continue
        regs[(j.get("regime"),j.get("form"))]+=1
        store[(cfg,setid)].add((j["pattern_id"],j["regime"],j["subject_id"],j.get("form")))
print("store regimes/forms seen:",dict(regs)); 

cells=list(csv.DictReader(open(OUT+"/cells.tsv"),delimiter="\t"))
# (a) universe control
mine=collections.defaultdict(set)
for c in cells:
    mine[(c["cfg"],c["set"])].add((c["pattern"],rmap_inv:={"search_short":"short-subject-search","throughput":"large-subject-throughput"}[c["regime"]],c["subject"],None))
tot_in=tot_out=0
keep=[]
for c in cells:
    reg={"search_short":"short-subject-search","throughput":"large-subject-throughput"}[c["regime"]]
    k=(c["pattern"],reg,c["subject"],None)
    if k in store.get((c["cfg"],c["set"]),()): keep.append(c); tot_in+=1
    else: tot_out+=1
print("cells computed:",len(cells),"present in committed store:",tot_in,"not in store (dropped):",tot_out)
# per-set drop detail
d=collections.Counter()
for c in cells:
    reg={"search_short":"short-subject-search","throughput":"large-subject-throughput"}[c["regime"]]
    if (c["pattern"],reg,c["subject"],None) not in store.get((c["cfg"],c["set"]),()): d[(c["set"],c["pattern"])]+=1
print("dropped by (set,pattern):",dict(d))
# reverse: store cells at a site pattern that I did not compute? (patterns with a site but missing subjects)
json.dump(keep,open(OUT+"/cells_kept.json","w"))
