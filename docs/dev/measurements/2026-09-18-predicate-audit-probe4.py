#!/usr/bin/env python3
"""b50predaudit probe 4: the remaining per-rule population facts."""
import glob, os, sys, collections
ROOT = os.environ.get("PCRECBENCH_ROOT", os.getcwd())  # repoint at a checkout
sys.path.insert(0, ROOT)
from pcrecbench import interpret as I
COLS = I.REPORT_COLUMNS
files = [f for f in sorted(glob.glob(os.path.join(ROOT, "reports", "*.tsv")))
         if not f.endswith(".subject-grain.tsv")]


def rows_of(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    return lines[0], [dict(zip(COLS, ln.split("\t")))
                      for ln in lines[2:] if ln]


# ---- R-FLOOR-1/3: compile cells with NO jitter row at all --------------
print("=" * 72)
print("R-FLOOR-1/3: the jitter POPULATION vs all compile cells")
cells = 0
with_j = 0
empty_median = 0
for path in files:
    _h, rows = rows_of(path)
    seen = collections.defaultdict(set)
    for r in rows:
        if r["section"] != "compile":
            continue
        k = (r["pattern"], r["form"], r["testee"])
        seen[k].add(r["metric"])
        if r["metric"] in ("median_total_ns",
                           "derived_first_match_row_minus_steady_state_ns") \
                and r["value"] == "":
            empty_median += 1
    for k, ms in seen.items():
        cells += 1
        if "jitter" in ms:
            with_j += 1
print(f"  compile cells: {cells:,}; with a jitter row: {with_j:,}; "
      f"WITHOUT: {cells - with_j:,} ({100*(cells-with_j)/cells:.1f}%)")
print(f"  compile median rows whose value is EMPTY (a refusal): "
      f"{empty_median:,}")

# ---- R-STATUS-12: the smallest-per-code narrowing ----------------------
print("=" * 72)
print("R-STATUS-12: giveup_smallest rows are ONE per (cell, code) --")
print("  the subject named is the SMALLEST firing one, not every one")
per_cell = collections.Counter()
subj_codes = collections.defaultdict(set)
tot = 0
for path in files:
    _h, rows = rows_of(path)
    for r in rows:
        if r["section"] == "excluded" and r["metric"] == "giveup_smallest":
            tot += 1
            per_cell[(path, r["pattern"], r["regime_or_na"], r["testee"])] += 1
            subj_codes[(path, r["testee"], r["regime_or_na"],
                        r["subject_or_na"])].add((r["pattern"], r["value"]))
print(f"  giveup_smallest rows corpus-wide: {tot}")
print(f"  distinct (cell) keys: {len(per_cell)}; rows per cell: "
      f"{dict(collections.Counter(per_cell.values()))}")
multi = {k: v for k, v in subj_codes.items()
         if len({c for _p, c in v}) > 1 and len({p for p, _c in v}) > 1}
print(f"  (testee,regime,subject) keys with 2+ codes on 2+ patterns "
      f"(R-STATUS-12's firing population): {len(multi)}")

# ---- R-ARM-1: how much of its output is spread-driven ------------------
print("=" * 72)
print("R-ARM-1: the ratio distribution of its firings")
cat = I.load_catalogue(os.path.join(ROOT, "catalogue/rules.toml"))
known = I.header_keys_from_source()
arm = next(r for r in cat["rule"] if r["id"] == "R-ARM-1")
for rep in ("2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv",
            "2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv"):
    report = I.ReportTsv(os.path.join(ROOT, "reports", rep), known)
    ctx = I.Context(cat, report, None)
    out = I.r_arm_1(I.RuleView(arm, report, None), ctx)
    rr = sorted(f.nums["ratio"] for f in out)
    if not rr:
        continue
    bands = collections.Counter()
    for v in rr:
        bands["<1.02" if v < 1.02 else
              "1.02-1.10" if v < 1.10 else
              "1.10-2.0" if v < 2.0 else ">=2.0"] += 1
    print(f"  {rep}")
    print(f"    {len(rr)} firings; ratio min={rr[0]:.3f} "
          f"median={rr[len(rr)//2]:.3f} max={rr[-1]:.3f}")
    print(f"    bands: {dict(bands)}")

# ---- R-DELTA-1: is the comparand unambiguous? -------------------------
print("=" * 72)
print("R-DELTA-1: the template names no comparand pin; how many older")
print("  same-config siblings exist per firing cell?")
for rep in ("2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv",
            "2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv"):
    _h, rows = rows_of(os.path.join(ROOT, "reports", rep))
    sib = collections.Counter()
    for r in rows:
        if r["section"] != "rank" or r["metric"] != "median_ns":
            continue
        if not r["delta_verdict"]:
            continue
        pr = I.split_testee(r["testee"])
        if not pr:
            continue
        n = 0
        for o in rows:
            if o["section"] != "rank" or o["metric"] != "median_ns":
                continue
            if (o["pattern"], o["regime_or_na"], o["form"]) != \
               (r["pattern"], r["regime_or_na"], r["form"]):
                continue
            po = I.split_testee(o["testee"])
            if not po or po[0] != pr[0] or po[1] == pr[1]:
                continue
            if I.config_of(o["testee"]) != I.config_of(r["testee"]):
                continue
            n += 1
        sib[n] += 1
    print(f"  {rep}: firings by number of other-pin siblings in the cell: "
          f"{dict(sorted(sib.items()))}")

# ---- R-BUCKET-DOMINATED on an EXCLUDED set cell -----------------------
print("=" * 72)
print("R-BUCKET-DOMINATED: firings whose SET cell is not ranked, and the")
print("  subjects its denominator omits")
rep = "2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3"
_h, setrows = rows_of(os.path.join(ROOT, "reports", rep + ".tsv"))
excluded_cells = {(r["pattern"], r["regime_or_na"], r["testee"])
                  for r in setrows
                  if r["section"] == "excluded" and r["metric"] == "pass_rate"}
ranked_cells = {(r["pattern"], r["regime_or_na"], r["testee"])
                for r in setrows
                if r["section"] == "rank" and r["metric"] == "median_ns"}
report = I.ReportTsv(os.path.join(ROOT, "reports", rep + ".tsv"), known)
sg = I.ReportTsv(os.path.join(ROOT, "reports", rep + ".subject-grain.tsv"),
                 known)
ctx = I.Context(cat, report, None, subject_grain=sg)
dom = next(r for r in cat["rule"] if r["id"] == "R-BUCKET-DOMINATED")
out = I.r_bucket_dominated(I.RuleView(dom, report, None), ctx)
_h2, sgrows = rows_of(os.path.join(ROOT, "reports", rep + ".subject-grain.tsv"))
sg_rank = collections.defaultdict(set)
sg_excl = collections.defaultdict(set)
for r in sgrows:
    k = (r["pattern"], r["regime_or_na"], r["testee"])
    if r["section"] == "rank" and r["metric"] == "median_ns":
        sg_rank[k].add(r["subject_or_na"])
    elif r["section"] == "excluded" and r["metric"] == "pass_rate":
        sg_excl[k].add(r["subject_or_na"])
bad = 0
for f in out:
    k = (f.keys["pattern"], f.keys["regime"], f.keys["testee"])
    if k in excluded_cells:
        bad += 1
        if bad <= 5:
            print(f"    {k[0]} / {k[1]} / {k[2]}: share "
                  f"{f.slots['share']} of a total over "
                  f"{len(sg_rank[k])} ranked subject(s); "
                  f"{len(sg_excl[k])} subject(s) of the same cell are in "
                  f"the subject-grain `excluded` section and are NOT in "
                  f"the denominator. The SET cell is EXCLUDED from ranking.")
print(f"  firings: {len(out)}; on a set cell the report EXCLUDED: {bad}; "
      f"on a ranked set cell: {sum(1 for f in out if (f.keys['pattern'], f.keys['regime'], f.keys['testee']) in ranked_cells)}")
