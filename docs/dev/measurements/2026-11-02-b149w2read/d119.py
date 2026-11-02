# b149w2read: the committed capability@0.4 report's own d119 / null_band verdicts, tabulated (read of the report TSV only)
import csv, sys, collections
T = sys.argv[1]
def kv(s): return dict(p.split("=", 1) for p in s.split("; ") if "=" in p)
rows = [r for r in csv.reader(open(T), delimiter="\t") if r and r[0] == "d119"]
print(len(rows), "d119 rows")
c = collections.Counter()
for r in rows:
    d = kv(r[16]); c[(d["identity"], r[11], r[16 - 0 and 0 or 0] if False else r[3], d.get("capture_class"))] += 1
print("(identity, verdict, regime, capture_class) counts:")
for k, v in sorted(c.items()): print("  ", k, v)
print("\nchanged cells, non-'within' verdicts (pattern regime config delta% bar% src verdict before->after):")
for r in rows:
    d = kv(r[16])
    if d["identity"] == "changed" and r[11] != "within":
        print("  %-42s %-8s %-8s %+7.2f%% bar %s %s %s %s -> %s" % (r[1], r[3][:5], r[6].split("_")[-1].replace("-simdna", ""), float(d["delta_pct"]), d["bar_pct"][:6], d["bar_source"], r[11], d["before_ns"][:10], d["after_ns"][:10]))
print("\nidentical cells with |delta| > 5%:")
for r in rows:
    d = kv(r[16])
    if d["identity"] == "identical" and abs(float(d["delta_pct"])) > 5:
        print("  %-42s %-8s %-8s %+7.2f%% iqr %s stratum %s" % (r[1], r[3][:5], r[6].split("_")[-1].replace("-simdna", ""), float(d["delta_pct"]), d["iqr_pct"][:6], d["stratum"]))
for r in csv.reader(open(T), delimiter="\t"):
    if r and r[0] == "null_band": print("null_band", r[2], r[3], r[10:13], r[-1] if len(r) > 16 else "", r[16] if len(r) > 16 else "")
