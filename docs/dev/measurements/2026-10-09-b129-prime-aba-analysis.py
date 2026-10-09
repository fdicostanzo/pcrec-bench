#!/usr/bin/env python3
"""[B129] A/B/A follow-up analysis (lane b129prime, 2026-10-09).

Source: build/scratch-store-b129aba from 2026-10-09-b129-prime-aba-run.sh
(per cell and testee three records in timestamp order: A1 unprimed, B primed,
A2 unprimed). Arithmetic: tools/frontpage.Summary (pcrecbench.reduce).
Run:  python3 docs/dev/measurements/2026-10-09-b129-prime-aba-analysis.py \
          build/scratch-store-b129aba
Reading: A2/A1 is pure order/time drift (no flag differs). B/A1 is the
sample's ratio. B/A2 is the primed arm against the LATER unprimed run: if
priming were real warming, B/A1 and B/A2 are both < 1 by similar amounts;
if it is drift, A2/A1 shows it too. "disjoint" = closed [min,max] trial
ranges do not overlap. No number is typed.
"""
import os, sys
from collections import defaultdict
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "tools"))
import frontpage as fp                      # noqa: E402
from pcrecbench.harness import PRIME_NOTE   # noqa: E402


def rel(x, y):
    ov = max(x["lo"], y["lo"]) <= min(x["hi"], y["hi"])
    return "%.4g (%s)" % (y["median"] / x["median"], "overlap" if ov else "DISJOINT")


def main(store):
    runs = defaultdict(list)
    for r in sorted(fp.index_rows(store), key=lambda r: r["timestamp"]):
        s = fp.Summary(store, r)
        primed = PRIME_NOTE in (s.setup.get("note") or "")
        for (pid, reg), c in s.cells.items():
            runs[(fp.engine_of(s.testee_id), pid, reg)].append((primed, c, r["status"]))
    print("%-7s %-34s %-24s %12s %12s %12s  %s | %s | %s" % (
        "testee", "pattern", "regime", "A1 median", "B median", "A2 median",
        "B/A1", "A2/A1 (drift)", "B/A2"))
    for k in sorted(runs):
        v = runs[k]
        if len(v) != 3 or [p for p, _, _ in v] != [False, True, False]:
            print(k, "UNEXPECTED SEQUENCE", [(p, st) for p, _, st in v]); continue
        (_, a1, s1), (_, b, s2), (_, a2, s3) = v
        if None in (a1["median"], b["median"], a2["median"]):
            print(k, "NO NUMBER"); continue
        print("%-7s %-34s %-24s %12.6g %12.6g %12.6g  %s | %s | %s   [%s,%s,%s]" % (
            k[0], k[1], k[2], a1["median"], b["median"], a2["median"],
            rel(a1, b), rel(a1, a2), rel(a2, b), s1, s2, s3))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "build/scratch-store-b129aba")
