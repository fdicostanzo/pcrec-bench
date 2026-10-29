import csv,re,sys,collections,statistics
T=sys.argv[1]
rows=[r for r in csv.reader(open(T),delimiter='\t') if r and r[0]=="d119"]
def kv(s): return dict(p.split("=",1) for p in s.split("; ") if "=" in p)
out=[]
for r in rows:
    d=kv(r[16]) if len(r)>16 else {}
    out.append((r[1],r[3],r[4],r[6],r[10],r[11],d,r[-1] if len(r)>17 else ""))
print(len(out), "d119 rows; sample:", rows[0][:12])
print(collections.Counter((o[6].get("identity"),o[5]) for o in out))
idc=[o for o in out if o[6].get("identity")=="identical"]
idc.sort(key=lambda o:-abs(float(o[6]["delta_pct"])))
print("identical cells top |delta|:")
for o in idc[:12]: print(o[0],o[1],o[2],o[3].split("_")[-1],o[6]["delta_pct"],o[6]["before_ns"],o[6]["after_ns"],o[6]["iqr_pct"],o[6]["stratum"])
ds=sorted(float(o[6]["delta_pct"]) for o in idc)
print("identical n=%d median %.3f p5 %.3f p95 %.3f"%(len(ds),statistics.median(ds),ds[int(.05*len(ds))],ds[int(.95*len(ds))]))
