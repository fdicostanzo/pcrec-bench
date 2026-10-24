#!/usr/bin/env python3
# b139gaps / report_tables.py -- source header. Reads cells_kept.json (aggregate.py), prints the groups.
import json,collections
K=json.load(open("/var/tmp/pcrecbench/b139gaps/cells_kept.json"))
def f(c): return (float(c["mean_gap"]) if c["mean_gap"] else None)
have=[c for c in K if c["mean_gap"]!=""]
print("kept cells",len(K),"with >=2 landings",len(have),"(<2 landings:",len(K)-len(have),")")
by=collections.Counter((c["cfg"],c["site"]) for c in K); print(sorted(by.items()))
Q=[c for c in have if f(c)<=8]; print("mean<=8:",len(Q), " with share>0.5:",sum(1 for c in Q if float(c["dom_share"])>0.5))
N=[c for c in have if 8<f(c)<=16]; print("8<mean<=16:",len(N)," share>0.5:",sum(1 for c in N if float(c["dom_share"])>0.5))
g=collections.Counter((c["cfg"],c["set"],c["pattern"],c["site"],c["cover"],c["setsize"]) for c in Q)
for k,v in sorted(g.items()): print(v,k)
