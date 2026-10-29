import csv,sys,collections
T=sys.argv[1]
def kv(s): return dict(p.split("=",1) for p in s.split("; ") if "=" in p)
rows=[r for r in csv.reader(open(T),delimiter='\t') if r and r[0]=="d119"]
print("pattern|regime|form|config|identity|verdict|delta%|iqr%|before|after|ratio")
for r in rows:
    d=kv(r[16])
    if d["identity"]!="changed": continue
    b,a=float(d["before_ns"]),float(d["after_ns"])
    print("|".join([r[1],r[3],r[4],r[6].split("_")[-1].replace("-simdna",""),d["identity"],r[11],d["delta_pct"][:7],d["iqr_pct"][:6],"%.1f"%b,"%.1f"%a,"x%.3f"%(a/b)]))
forms=collections.Counter(r[4] for r in rows); print(forms)
