#!/usr/bin/env python3
"""[B129] priming A/B analysis (lane b129prime, 2026-10-09).

Source: the scratch store build/scratch-store-b129 written by
2026-10-09-b129-prime-run.sh (capability@0.2, 5 trials; per testee an
UNPRIMED arm A and a PRIMED arm B, `--prime`; the record note carries the
fixed sentence harness.PRIME_NOTE on arm B).
Run:  python3 docs/dev/measurements/2026-10-09-b129-prime-analysis.py \
          build/scratch-store-b129 > docs/dev/measurements/2026-10-09-b129-prime-ab.txt
Arithmetic: pcrecbench.reduce (cells_from_record / reduce_set_cell) via
tools/frontpage.Summary; classification: tools/frontpage.classify/compare/
stats -- the front page's own functions, run on these scratch records.
No number is typed; everything printed is computed here.

A "cell" = (pattern, regime), plain form. B/A = primed median / unprimed
median. Tie rule (the front page's): closed [min, max] trial ranges
overlap. "Moved" = the A and B ranges are DISJOINT (priming moved the median
beyond the overlap); direction by B/A (<1: priming made it faster).
"""
import csv
import math
import os
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tools"))
import frontpage as fp                      # noqa: E402
from pcrecbench.harness import PRIME_NOTE   # noqa: E402

TESTEES = ("re2-default", "rust-default", "pcrec-auto")


def geo(xs):
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else None


def f(x, n=4):
    return "-" if x is None else ("%.*g" % (n, x))


def main(store):
    rows = fp.index_rows(store)
    arms = {}      # (family, arm) -> Summary
    print("== records (store %s) ==" % store)
    for r in sorted(rows, key=lambda r: r["timestamp"]):
        if r["subbench"] != "capability":
            continue
        s = fp.Summary(store, r)
        primed = PRIME_NOTE in (s.setup.get("note") or "")
        fam = next((t for t in TESTEES if s.testee_id.endswith(t.split("-", 1)[1])
                    and fp.engine_of(s.testee_id) == t.split("-", 1)[0].replace("re2", "re2")), None)
        fam = fam or next((t for t in TESTEES if t.split("-")[0] in s.testee_id), None)
        print("%s  %s  status=%s  primed=%s  trials=%d  load1(before)=%s  %s" % (
            r["timestamp"], s.testee_id, r["status"], primed, s.max_trials,
            (s.env.get("load") or {}).get("before", {}).get("load1", "?")
            if isinstance(s.env.get("load"), dict) and isinstance(
                s.env.get("load", {}).get("before"), dict) else "?", r["path"]))
        # keep the LATEST record per (family, arm): a re-run of an rc-4 cell
        # supersedes its first attempt
        arms[(fam, "B" if primed else "A")] = s
    missing = [(t, a) for t in TESTEES for a in "AB" if (t, a) not in arms]
    if missing:
        print("MISSING arms: %r" % missing)
        return 1

    summary = {}
    for t in TESTEES:
        A, B = arms[(t, "A")], arms[(t, "B")]
        keys = sorted(set(A.cells) | set(B.cells))
        print("\n== %s: B(primed)/A(unprimed) per set-grain cell ==" % t)
        print("%-44s %-13s %12s %12s %8s %s" % (
            "pattern", "regime", "A median ns", "B median ns", "B/A", "ranges"))
        out = []
        for k in keys:
            a, b = A.numeric(k), B.numeric(k)
            if not (a and b):
                print("%-44s %-13s %s" % (k[0], k[1], "no number: A=%s B=%s" % (
                    A.reason(k) if not a else "ok", B.reason(k) if not b else "ok")))
                continue
            ratio = b["median"] / a["median"]
            overlap = max(a["lo"], b["lo"]) <= min(a["hi"], b["hi"])
            out.append(dict(key=k, ratio=ratio, overlap=overlap, a=a, b=b))
            print("%-44s %-13s %12s %12s %8s %s" % (
                k[0], k[1], f(a["median"], 6), f(b["median"], 6), f(ratio),
                "overlap" if overlap else ("DISJOINT-%s" % (
                    "faster" if ratio < 1 else "slower"))))
        summary[t] = out
        print("\n-- %s per-regime summary --" % t)
        for reg in sorted({o["key"][1] for o in out}) + ["(all)"]:
            sub = [o for o in out if reg == "(all)" or o["key"][1] == reg]
            rs = [o["ratio"] for o in sub]
            mv = [o for o in sub if not o["overlap"]]
            fast = [o for o in mv if o["ratio"] < 1]
            slow = [o for o in mv if o["ratio"] > 1]
            print("%-13s cells=%d  B/A median=%s geomean=%s min=%s max=%s  "
                  "moved-beyond-overlap=%d (faster %d, slower %d)" % (
                      reg, len(sub), f(statistics.median(rs)) if rs else "-",
                      f(geo(rs)), f(min(rs)) if rs else "-",
                      f(max(rs)) if rs else "-", len(mv), len(fast), len(slow)))
        movers = sorted((o for o in out if not o["overlap"]),
                        key=lambda o: -abs(math.log(o["ratio"])))[:10]
        print("-- %s largest movers (disjoint ranges) --" % t)
        for o in movers:
            print("  %-44s %-13s B/A=%s" % (o["key"][0], o["key"][1], f(o["ratio"])))
        if not movers:
            print("  (none)")
        top = sorted(out, key=lambda o: -abs(math.log(o["ratio"])))[:5]
        print("-- %s largest |log B/A| overall (overlap or not) --" % t)
        for o in top:
            print("  %-44s %-13s B/A=%s %s" % (o["key"][0], o["key"][1],
                  f(o["ratio"]), "overlap" if o["overlap"] else "DISJOINT"))

    print("\n== front-page headline consequence: competitor vs pcrec-auto ==")
    print("(tools/frontpage.compare/stats on the scratch records; A pairs = "
          "both unprimed, B pairs = both primed)")
    for comp in ("re2-default", "rust-default"):
        res = {}
        for arm in "AB":
            pcs, cs = arms[("pcrec-auto", arm)], arms[(comp, arm)]
            universe = set(pcs.cells) | set(cs.cells)
            cases, excl = fp.compare(pcs, cs, universe)
            res[arm] = (cases, excl, len(universe))
        for scope in ("(all)", "search_short", "throughput"):
            line = []
            for arm in "AB":
                cases = [c for c in res[arm][0] if scope == "(all)" or c["key"][1] == scope]
                st = fp.stats(cases)
                line.append("%s: win %d loss %d tie %d (n=%d, median speedup %s)" % (
                    arm, st["win"], st["loss"], st["tie"], st["n"], f(st["median"])))
            print("%-13s %-13s  %s" % (comp, scope, "   |   ".join(line)))
        print("%-13s excluded A: %s | B: %s" % (comp, fp.excl_text(res["A"][1]),
                                                fp.excl_text(res["B"][1])))
        ca = {c["key"]: c["cls"] for c in res["A"][0]}
        cb = {c["key"]: c["cls"] for c in res["B"][0]}
        flips = sorted(k for k in set(ca) & set(cb) if ca[k] != cb[k])
        print("%-13s cells whose win/loss/tie class differs A vs B: %d%s" % (
            comp, len(flips), "" if not flips else "".join(
                "\n    %s / %s : %s -> %s" % (k[0], k[1], ca[k], cb[k]) for k in flips)))
        only = sorted(set(ca) ^ set(cb))
        print("%-13s cells that are a case in only one arm: %d" % (comp, len(only)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "build/scratch-store-b129"))
