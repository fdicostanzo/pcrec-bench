#!/usr/bin/env python3
# b139gaps / group.py -- source header. Groups cells_kept.json into audit tables; writes qualifying.tsv,
# nearmiss.tsv (full per-cell lists) and groups_*.md (compact markdown). Qualifying: mean gap <= 8 and
# dominant share > 0.5. Dense-irregular: mean <= 8, share <= 0.5. Near-miss: 8 < mean <= 16 (any share).
import json,collections,statistics,csv
O="/var/tmp/pcrecbench/b139gaps/"
K=json.load(open(O+"cells_kept.json"))
H=["cfg","set","pattern","regime","subject","len","site","setsize","cover","landings","mean_gap","dom_gap","dom_share"]
def cls(c):
    if c["mean_gap"]=="": return "lt2"
    m=float(c["mean_gap"]); s=float(c["dom_share"])
    if m>16: return "far"
    if int(c["landings"])<16: return "small-n"      # <15 gaps: "one dominant gap" is not meaningful (n=1 gap is 100%)
    if m<=8: return "Q" if s>0.5 else "dense-irregular"
    return "near"
for c in K: c["cls"]=cls(c)
print(collections.Counter(c["cls"] for c in K))
for name,sel in (("qualifying",("Q",)),("nearmiss",("near","dense-irregular")),("small_n",("small-n",))):
    with open(O+name+".tsv","w") as f:
        f.write("\t".join(H+["class"])+"\n")
        for c in K:
            if c["cls"] in sel: f.write("\t".join(str(c[h]) for h in H+["cls"])+"\n")
def groups(sel):
    G=collections.defaultdict(list)
    for c in K:
        if c["cls"] in sel: G[(c["set"],c["pattern"],c["site"],c["cover"],c["setsize"])].append(c)
    return G
def line(k,v):
    cf=",".join(sorted({c["cfg"] for c in v}))
    ms=[float(c["mean_gap"]) for c in v]; sh=[float(c["dom_share"]) for c in v]
    dg=collections.Counter(int(c["dom_gap"]) for c in v).most_common(3)
    ln=[int(c["len"]) for c in v]; rg=collections.Counter(c["regime"] for c in v)
    subj=len({(c["regime"],c["subject"]) for c in v})
    lg=[int(c["landings"]) for c in v]
    return "| %s | %s | %s | %s | %s/%s%s | %d (%s) | %d-%d | %d-%d | %.2f-%.2f (med %.2f) | %s | %.2f-%.2f |"%(
      k[0],k[1],cf,k[2],k[3],k[4],(" B5" if (k[2]=="vm-hat-first-class" and k[4]=="1") else ""),subj,",".join("%s %d"%(r.replace('search_short','ss').replace('throughput','tp'),n) for r,n in rg.items()),min(ln),max(ln),min(lg),max(lg),
      min(ms),max(ms),statistics.median(ms),", ".join("%d x%d"%(a,b) for a,b in dg),min(sh),max(sh))
HD="| set | pattern | cfg | site | cover/|S| | subjects (regime cells) | len B | landings | mean gap | dominant gap (cells) | share |\n|---|---|---|---|---|---|---|---|---|---|---|"
def groups_ge2():
    G=collections.defaultdict(list)
    for c in K:
        if c["cls"]=="Q" and int(c["dom_gap"])>=2: G[(c["set"],c["pattern"],c["site"],c["cover"],c["setsize"])].append(c)
    return G
G=groups_ge2()
with open(O+"groups_qualifying_domgap_ge2.md","w") as f:
    f.write(HD+"\n")
    for k in sorted(G): f.write(line(k,G[k])+"\n")
print("groups_ge2",len(G),sum(len(v) for v in G.values()),"cells")
for name,sel in (("groups_qualifying",("Q",)),("groups_nearmiss",("near",)),("groups_denseirregular",("dense-irregular",))):
    G=groups(sel)
    with open(O+name+".md","w") as f:
        f.write(HD+"\n")
        for k in sorted(G): f.write(line(k,G[k])+"\n")
    print(name,len(G),"groups")
