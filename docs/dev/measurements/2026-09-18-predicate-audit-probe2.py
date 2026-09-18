#!/usr/bin/env python3
"""b50predaudit probe 2: the per-rule blind-spot instances.

Uses the interpreter's OWN functions (parse_selector, _glob_match,
_select, _sections_for, split_testee, config_of, is_reference) rather
than reimplementing them."""
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


# ---------------------------------------------------------------- M2: alpha
print("=" * 72)
print("M2  ruling (alpha)'s POPULATION on the newest capability report")
rep = os.path.join(ROOT, "reports",
                   "2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv")
preds = I.load_predictions(os.path.join(ROOT, "docs/dev/predictions/"
                                              "capability-0.1-first.tsv"))
report = I.ReportTsv(rep, I.header_keys_from_source())
cat = I.load_catalogue(os.path.join(ROOT, "catalogue/rules.toml"))
rule = next(r for r in cat["rule"] if r["id"] == "R-PRED-1")
view = I.RuleView(rule, report, None)
for p in preds:
    sel_rows = I._select(view, p)
    by_sec = collections.Counter(r["section"] for r in sel_rows)
    vals = I._keyed_values(view, p)
    cells = {(r["pattern"], r["regime_or_na"], r["form"], r["testee"])
             for r in sel_rows}
    print(f"  {p['prediction_id']}{p['clause']:3} q={p['quantity']:26} "
          f"default_sections={I._sections_for(p)} rows={len(sel_rows):4} "
          f"valued={len(vals):4} distinct_cells={len(cells):4} "
          f"by_section={dict(by_sec)}")

print("\n  P5.a detail: which rows carry the counterevidence")
p5 = next(p for p in preds if p["prediction_id"] == "P5")
sel = I._select(view, p5)
ce = [r for r in sel if I._float_or_none(r["n_wrong"]) not in (None, 0.0)]
print(f"    selected rows {len(sel)}; rows with n_wrong>0: {len(ce)}")
print(f"    those rows' sections: "
      f"{dict(collections.Counter(r['section'] for r in ce))}")
print(f"    rank rows in the selection: "
      f"{sum(1 for r in sel if r['section']=='rank')} "
      f"(= 6 x {sum(1 for r in sel if r['section']=='rank')//6} cells)")
print(f"    excluded rows in the selection: "
      f"{sum(1 for r in sel if r['section']=='excluded')}")

# -------------------------------------------------- M3: floor_pattern none
print("=" * 72)
print("M3  reports whose header floor_pattern is `none` or multi-valued")
for path in files:
    hdr, _rows = rows_of(path)
    i = hdr.find("floor_pattern: ")
    val = hdr[i + len("floor_pattern: "):].split("; ")[0] if i >= 0 else "(absent)"
    if val == "none" or "," in val:
        print(f"  {os.path.basename(path)}  ->  floor_pattern: {val!r}")

# ------------------------------------- M5: R-ARM-1 refused-arm blindness
print("=" * 72)
print("M5  a one-token-apart arm pair where ONE arm is in did_not_compile")
hits = 0
for path in files:
    _hdr, rows = rows_of(path)
    ranked = collections.defaultdict(set)     # (pattern,regime,form) -> testees
    dnc = collections.defaultdict(set)        # pattern -> testees
    for r in rows:
        if r["section"] == "rank" and r["metric"] == "median_ns":
            ranked[(r["pattern"], r["regime_or_na"], r["form"])].add(r["testee"])
        elif r["section"] == "did_not_compile":
            dnc[r["pattern"]].add(r["testee"])
    for (pat, reg, form), testees in sorted(ranked.items()):
        for refused in sorted(dnc.get(pat, ())):
            pr = I.split_testee(refused)
            if not pr:
                continue
            for t in sorted(testees):
                pt = I.split_testee(t)
                if not pt or pt[0] != pr[0] or pt[1] != pr[1]:
                    continue
                diff = [k for k in range(4) if pt[2 + k] != pr[2 + k]]
                if len(diff) == 1:
                    hits += 1
                    if hits <= 6:
                        print(f"  {os.path.basename(path)}")
                        print(f"    {pat} / {reg} / {form}: ranked "
                              f"`{t}` vs REFUSED `{refused}` "
                              f"(one token apart: "
                              f"{('mode','caps','simd','extra')[diff[0]]} "
                              f"{pt[2+diff[0]]!r} vs {pr[2+diff[0]]!r})")
print(f"  total such (cell, ranked arm, refused arm) triples: {hits}")

# ------------------------- M6: cross-pin regression invisible to R-DELTA-1
print("=" * 72)
print("M6  one pin RANKS a cell while the same config at another pin is")
print("    EXCLUDED or REFUSED in the same report (no delta_verdict exists)")
hits = 0
for path in files:
    _hdr, rows = rows_of(path)
    ranked = {}
    bad = {}
    for r in rows:
        pr = I.split_testee(r["testee"])
        if not pr:
            continue
        key = (r["pattern"], r["regime_or_na"], r["form"], pr[0],
               I.config_of(r["testee"]))
        if r["section"] == "rank" and r["metric"] == "median_ns":
            ranked.setdefault(key, []).append((pr[1], r["testee"]))
        elif r["section"] == "excluded" and r["metric"] == "pass_rate":
            bad.setdefault(key, []).append((pr[1], r["testee"], "excluded"))
        elif r["section"] == "did_not_compile":
            k2 = (r["pattern"], r["regime_or_na"], "", pr[0],
                  I.config_of(r["testee"]))
            bad.setdefault(k2, []).append((pr[1], r["testee"], "did_not_compile"))
    for key, rk in sorted(ranked.items()):
        for k2 in (key, (key[0], key[1], "", key[3], key[4])):
            for (v, t, sec) in bad.get(k2, ()):
                for (v2, t2) in rk:
                    if v2 != v:
                        hits += 1
                        if hits <= 8:
                            print(f"  {os.path.basename(path)}")
                            print(f"    {key[0]} / {key[1]} / cfg {key[4]}: "
                                  f"{v2} RANKS (`{t2}`) but {v} is in "
                                  f"{sec} (`{t}`)")
print(f"  total such pairs: {hits}")

# ---------------------------------- M8: not_ranked / scratch populations
print("=" * 72)
print("M8  `not_ranked` and `scratch` section rows in the whole corpus")
c = collections.Counter()
for path in files:
    _hdr, rows = rows_of(path)
    for r in rows:
        if r["section"] in ("not_ranked", "scratch"):
            c[(os.path.basename(path), r["section"])] += 1
print(f"  {sum(c.values())} rows" + (f" {dict(c)}" if c else ""))
