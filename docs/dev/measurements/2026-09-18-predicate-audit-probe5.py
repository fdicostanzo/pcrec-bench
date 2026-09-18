import glob, os, sys, collections, re
ROOT = os.environ.get("PCRECBENCH_ROOT", os.getcwd())  # repoint at a checkout
sys.path.insert(0, ROOT)
from pcrecbench import interpret as I
COLS = I.REPORT_COLUMNS
def rows_of(p):
    L = open(p, encoding="utf-8").read().split("\n")
    return L[0], [dict(zip(COLS, ln.split("\t"))) for ln in L[2:] if ln]

print("== the 4 R-DELTA-1 firings with NO other-pin sibling rank row in the cell")
rep = os.path.join(ROOT, "reports", "2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv")
_h, rows = rows_of(rep)
rk = [r for r in rows if r["section"]=="rank" and r["metric"]=="median_ns"]
for r in rk:
    if not r["delta_verdict"]: continue
    pr = I.split_testee(r["testee"]); 
    if not pr: continue
    sibs = [o for o in rk if (o["pattern"],o["regime_or_na"],o["form"])==(r["pattern"],r["regime_or_na"],r["form"])
            and I.split_testee(o["testee"]) and I.split_testee(o["testee"])[0]==pr[0]
            and I.split_testee(o["testee"])[1]!=pr[1]
            and I.config_of(o["testee"])==I.config_of(r["testee"])]
    if sibs: continue
    # where IS the partner?
    partner = [o for o in rows if o["testee"].startswith("pcrec_") and o["section"] in ("excluded","did_not_compile","rank")
               and o["pattern"]==r["pattern"] and I.split_testee(o["testee"])
               and I.config_of(o["testee"])==I.config_of(r["testee"])
               and I.split_testee(o["testee"])[1]!=pr[1]
               and o["regime_or_na"] in (r["regime_or_na"], "")]
    secs = collections.Counter((o["section"], o["form"], o["regime_or_na"]) for o in partner)
    print(f"  {r['pattern']} / {r['regime_or_na']} / {r['form']} / {r['testee']}")
    print(f"     delta_verdict={r['delta_verdict']!r}")
    print(f"     the same config at another pin appears as: {dict(secs)}")

print()
print("== R-STATUS-12 / R-STATUS-3: subjects that gave up vs subjects NAMED")
files = [f for f in sorted(glob.glob(os.path.join(ROOT,"reports","*.tsv"))) if not f.endswith(".subject-grain.tsv")]
named = 0; gaveup = 0
for p in files:
    _h, rs = rows_of(p)
    for r in rs:
        if r["section"]=="excluded" and r["metric"]=="giveup_smallest":
            named += 1
        if r["section"]=="excluded" and r["metric"]=="pass_rate":
            for m in re.finditer(r"×(\d+)", r["gave_up_summary"]):
                gaveup += int(m.group(1))
print(f"  subjects that gave up (sum of the base rows' ×N): {gaveup}")
print(f"  subjects NAMED by a giveup_smallest row: {named}")
