#!/usr/bin/env python3
# b139gaps / summ.py -- source header. Summary views over qualifying.tsv / nearmiss.tsv / cells_kept.json.
import json,collections,csv,statistics
O="/var/tmp/pcrecbench/b139gaps/"
Q=list(csv.DictReader(open(O+"qualifying.tsv"),delimiter="\t"))
K=json.load(open(O+"cells_kept.json"))
print("== qualifying cells by (set, cfg, site): cells / distinct patterns")
d=collections.defaultdict(lambda:[0,set()])
for c in Q: d[(c["set"],c["cfg"],c["site"])][0]+=1; d[(c["set"],c["cfg"],c["site"])][1].add(c["pattern"])
for k,v in sorted(d.items()): print(k,v[0],len(v[1]))
print("== qualifying cells by regime/length class")
print(collections.Counter(("tp" if c["regime"]=="throughput" else "ss", int(c["len"])>=65536) for c in Q))
print("== qualifying with landings>=64 and |S|<=64:", sum(1 for c in Q if int(c["landings"])>=64 and int(c["setsize"])<=64))
print("== dominant gap value distribution among Q:", collections.Counter(int(c["dom_gap"]) for c in Q).most_common(12))
print("== cover distribution among Q:", collections.Counter(c["cover"] for c in Q))
