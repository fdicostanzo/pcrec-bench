#!/usr/bin/env python3
"""b50predaudit probe 7: the consequence for R-STATUS-4 (and for any
`section=did_not_compile` clause) of `render_tsv` emitting the
did_not_compile section only INSIDE an existing ranking group
(report.py:4555-4564) -- lane b51preds' finding 2, audited here as a
rule-population question.

A pattern NO testee in the roster compiled has no ranking group, so no
did_not_compile row exists for it anywhere: R-STATUS-4's population
cannot contain it, and its `no_fire` ("every pattern compiled on every
testee in this report") would be asserted over a pattern nothing
compiled."""
import glob, os, sys, collections
ROOT = os.environ.get("PCRECBENCH_ROOT", os.getcwd())
sys.path.insert(0, ROOT)
from pcrecbench import interpret as I
COLS = I.REPORT_COLUMNS
files = [f for f in sorted(glob.glob(os.path.join(ROOT, "reports", "*.tsv")))
         if not f.endswith(".subject-grain.tsv")]

total = 0
for path in files:
    lines = open(path, encoding="utf-8").read().split("\n")
    rows = [dict(zip(COLS, ln.split("\t"))) for ln in lines[2:] if ln]
    # every pattern the COMPILE section knows about, and for each whether
    # ANY compile cell carried a real median (i.e. something compiled)
    compiled = collections.defaultdict(bool)
    seen_compile = set()
    for r in rows:
        if r["section"] != "compile":
            continue
        if r["metric"] not in ("median_total_ns",
                              "derived_first_match_row_minus_steady_state_ns"):
            continue
        seen_compile.add(r["pattern"])
        if r["value"] != "":
            compiled[r["pattern"]] = True
    ranked = {r["pattern"] for r in rows
              if r["section"] in ("rank", "excluded", "not_ranked", "scratch")}
    dnc = {r["pattern"] for r in rows if r["section"] == "did_not_compile"}
    # a pattern with compile rows, NOTHING compiled, and NO did_not_compile row
    invisible = sorted(p for p in seen_compile
                       if not compiled[p] and p not in ranked and p not in dnc)
    if invisible:
        total += len(invisible)
        print(f"  {os.path.basename(path)}")
        print(f"    {len(invisible)} pattern(s) whose every compile cell is a "
              f"refusal AND which have NO did_not_compile row:")
        for p in invisible:
            n = sum(1 for r in rows if r["section"] == "compile"
                    and r["pattern"] == p
                    and r["metric"] == "median_total_ns")
            print(f"      {p}  ({n} refused compile cell(s), 0 rows in any "
                  f"ranking-family or did_not_compile section)")
print(f"\n  total (report, pattern) pairs invisible to R-STATUS-4: {total}")
