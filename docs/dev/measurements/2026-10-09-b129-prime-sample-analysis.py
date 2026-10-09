#!/usr/bin/env python3
"""[B129] priming A/B, SAMPLED (lane b129prime, 2026-10-09).

Source: the scratch store build/scratch-store-b129s written by
2026-10-09-b129-prime-sample-run.sh (`pcrecbench quick`, capability@0.2,
5 trials; per (testee, pattern, regime) an UNPRIMED record A and a PRIMED
record B, the latter carrying harness.PRIME_NOTE in its note).
Run:  python3 docs/dev/measurements/2026-10-09-b129-prime-sample-analysis.py \
          build/scratch-store-b129s > docs/dev/measurements/2026-10-09-b129-prime-sample.txt
Arithmetic: pcrecbench.reduce via tools/frontpage.Summary (set-grain cell:
median over trials of the per-trial sum of per-subject ns/call, min, max);
classification: tools/frontpage.classify -- the front page's own tie rule.
No number is typed; everything printed is computed here. quick records are
single-cell, so a "pair" is the A and B records of the same
(testee, pattern, regime), matched by note sentence and timestamp order.

B/A = primed median / unprimed median (< 1: priming made it faster).
"moved" = the A and B closed [min,max] ranges are DISJOINT.
"""
import math
import os
import statistics
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import frontpage as fp                      # noqa: E402
from pcrecbench.harness import PRIME_NOTE   # noqa: E402


def fam(testee_id):
    e = fp.engine_of(testee_id)
    return {"pcrec": "pcrec-auto"}.get(e, e)


def geo(xs):
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else None


def f(x, n=4):
    return "-" if x is None else "%.*g" % (n, x)


def main(store):
    rows = [r for r in fp.index_rows(store) if r["subbench"] == "capability"]
    pairs = defaultdict(dict)       # (fam, pattern, regime) -> {"A": cell, "B": cell}
    print("== records: %d in %s ==" % (len(rows), store))
    for r in sorted(rows, key=lambda r: r["timestamp"]):
        s = fp.Summary(store, r)
        arm = "B" if PRIME_NOTE in (s.setup.get("note") or "") else "A"
        for (pid, regime), c in s.cells.items():
            if c["median"] is None:
                print("NO NUMBER %s %s %s arm %s status %s (wrong=%s gaveup=%s)" % (
                    s.testee_id, pid, regime, arm, r["status"], c["n_wrong"], c["n_gave_up"]))
                continue
            c = dict(c, status=r["status"], ts=r["timestamp"])
            pairs[(fam(s.testee_id), pid, regime)][arm] = c
    non = sorted({(k, c["status"]) for k, d in pairs.items() for c in d.values()
                  if c["status"] != "measured"})
    print("non-measured records (status):", non if non else "none")
    full = {k: d for k, d in pairs.items() if "A" in d and "B" in d}
    print("pairs complete: %d of %d keys" % (len(full), len(pairs)))

    res = defaultdict(list)
    print("\n== B/A per (testee, pattern, regime) ==")
    print("%-12s %-36s %-13s %12s %12s %8s %s" % (
        "testee", "pattern", "regime", "A median", "B median", "B/A", "ranges"))
    for k in sorted(full):
        a, b = full[k]["A"], full[k]["B"]
        ratio = b["median"] / a["median"]
        ov = max(a["lo"], b["lo"]) <= min(a["hi"], b["hi"])
        res[k[0]].append(dict(key=k, ratio=ratio, overlap=ov))
        print("%-12s %-36s %-13s %12s %12s %8s %s" % (
            k[0], k[1], k[2], f(a["median"], 6), f(b["median"], 6), f(ratio),
            "overlap" if ov else "DISJOINT-" + ("faster" if ratio < 1 else "slower")))

    print("\n== per-testee / per-regime summary ==")
    for t in sorted(res):
        for reg in ("short-subject-search", "large-subject-throughput", "(all)"):
            sub = [o for o in res[t] if reg == "(all)" or o["key"][2] == reg]
            rs = [o["ratio"] for o in sub]
            mv = [o for o in sub if not o["overlap"]]
            print("%-12s %-13s cells=%2d B/A median=%s geomean=%s min=%s max=%s "
                  "moved=%d (faster %d, slower %d)" % (
                      t, reg, len(sub), f(statistics.median(rs)) if rs else "-",
                      f(geo(rs)), f(min(rs)) if rs else "-", f(max(rs)) if rs else "-",
                      len(mv), sum(o["ratio"] < 1 for o in mv),
                      sum(o["ratio"] > 1 for o in mv)))
    print("\n== largest movers per testee (by |log B/A|, 5 each) ==")
    for t in sorted(res):
        for o in sorted(res[t], key=lambda o: -abs(math.log(o["ratio"])))[:5]:
            print("%-12s %-36s %-13s B/A=%s %s" % (
                t, o["key"][1], o["key"][2], f(o["ratio"]),
                "overlap" if o["overlap"] else "DISJOINT"))

    print("\n== competitor vs pcrec-auto: win/loss/tie, A pairs vs B pairs "
          "(sample cells only; frontpage.classify) ==")
    for comp in sorted(t for t in res if t != "pcrec-auto"):
        for scope in ("(all)", "short-subject-search", "large-subject-throughput"):
            tally = {}
            flips = []
            for arm in "AB":
                cnt = defaultdict(int)
                for k, d in pairs.items():
                    if k[0] != comp or (scope != "(all)" and k[2] != scope):
                        continue
                    pk = ("pcrec-auto", k[1], k[2])
                    if arm not in d or arm not in pairs.get(pk, {}):
                        continue
                    sp, cl = fp.classify(pairs[pk][arm], d[arm])
                    cnt[cl] += 1
                tally[arm] = cnt
            line = "   |   ".join("%s: win %d loss %d tie %d" % (
                arm, tally[arm]["win"], tally[arm]["loss"], tally[arm]["tie"])
                for arm in "AB")
            print("%-12s %-13s %s" % (comp, scope, line))
        for k, d in sorted(pairs.items()):
            pk = ("pcrec-auto", k[1], k[2])
            if k[0] != comp or "A" not in d or "B" not in d \
                    or "A" not in pairs.get(pk, {}) or "B" not in pairs.get(pk, {}):
                continue
            ca = fp.classify(pairs[pk]["A"], d["A"])
            cb = fp.classify(pairs[pk]["B"], d["B"])
            if ca[1] != cb[1]:
                print("  class change %s / %s / %s : %s (x%s) -> %s (x%s)" % (
                    comp, k[1], k[2], ca[1], f(ca[0]), cb[1], f(cb[0])))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "build/scratch-store-b129s"))
