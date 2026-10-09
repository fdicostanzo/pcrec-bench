#!/usr/bin/env python3
"""tools/tests/test_frontpage.py -- self-tests for `tools/frontpage.py` ([B127]).

A synthetic three-cell fixture, hand-computed: pcrec median 100 ns, range
[90, 110] in every cell; the competitor's cells are
  A: median 400, [380, 420]  -> speedup 4.0  -> win  (ranges disjoint)
  B: median  50, [ 45,  55]  -> speedup 0.5  -> loss (ranges disjoint)
  C: median 105, [ 95, 115]  -> speedup 1.05 -> tie  (ranges overlap)
plus a fourth key where the competitor gave up, and a fifth where pcrec's
side is unsupported (attributed to pcrec first). Run: python3 tools/tests/test_frontpage.py
"""
import math
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import frontpage as F  # noqa: E402


def cell(med, lo, hi, wrong=0, gave=0):
    return dict(median=med, lo=lo, hi=hi, n_wrong=wrong, n_gave_up=gave,
                n_trials=5, n_subjects=1)


class Fake:
    def __init__(self, cells, compile_outcome=None):
        self.cells = cells
        self.compile_outcome = compile_outcome or {}

    numeric = F.Summary.numeric
    reason = F.Summary.reason


def main():
    fails = []

    def ok(name, cond):
        print(("PASS " if cond else "FAIL ") + name)
        if not cond:
            fails.append(name)

    k = lambda p: (p, "short")
    pc = Fake({k("a"): cell(100, 90, 110), k("b"): cell(100, 90, 110),
               k("c"): cell(100, 90, 110), k("d"): cell(100, 90, 110)},
              {"e": "unsupported-by-declaration"})
    cp = Fake({k("a"): cell(400, 380, 420), k("b"): cell(50, 45, 55),
               k("c"): cell(105, 95, 115),
               k("d"): cell(None, None, None, gave=2),
               k("e"): cell(10, 9, 11)})
    universe = set(pc.cells) | set(cp.cells)
    cases, excl = F.compare(pc, cp, universe)
    cls = {c["key"][0]: c["cls"] for c in cases}
    ok("win/loss/tie classification", cls == {"a": "win", "b": "loss", "c": "tie"})
    st = F.stats(cases)
    ok("counts", (st["n"], st["win"], st["loss"], st["tie"]) == (3, 1, 1, 1))
    ok("median speedup is the median of 4.0, 0.5, 1.05", st["median"] == 1.05)
    ok("geometric mean", abs(st["geo"] - (4.0 * 0.5 * 1.05) ** (1 / 3)) < 1e-12)
    ok("engine give-up counted on the engine side",
       excl["engine"]["gave-up"] == 1 and sum(excl["engine"].values()) == 1)
    ok("pcrec-side unsupported attributed to pcrec",
       excl["pcrec"]["unsupported"] == 1 and sum(excl["pcrec"].values()) == 1)
    ok("boundary: touching ranges tie",
       F.classify(cell(100, 90, 110), cell(300, 110, 400))[1] == "tie")
    ok("sig rounds half to even", F.sig(0.125, 2) == "0.12" and F.sig(0.135, 2) == "0.14")
    ok("sig keeps magnitude", F.sig(78412.0, 3) == "78400" and F.sig(1.0, 3) == "1.00")
    ok("pct rounds half to even", F.pct(1, 8) == "12.5%" and F.pct(1, 16) == "6.2%")

    ok("big: thousands separators, 3 s.f.", F.big(28512.3) == "28,500" and F.big(1234567) == "1,230,000")
    ok("slower_by inverts", F.slower_by(1 / 28512.3) == "×28,500")

    class T:  # a minimal summary
        def __init__(self, name, mode, ver, tid):
            self.te = dict(engine_name=name, engine_mode=mode, engine_version=ver)
            self.testee_id = tid
    ok("label JIT", F.label(T("libpcre2", "jit", "10.46", "x")) == "PCRE2 10.46 JIT")
    ok("label pcrec", F.label(T("pcrec", "auto", "abc123", "x")) == "pcrec 0.2.0-beta+abc123")
    ok("label utf8 suffix", F.label(T("re2", "default", "11.0.0", "re2_x_default-caps-simdna_utf8")).endswith("UTF-8"))
    try:
        F.label(T("newengine", "m", "1", "newengine_1_m"))
        ok("unmapped testee fails loudly", False)
    except SystemExit:
        ok("unmapped testee fails loudly", True)

    text = "intro\n<!-- frontpage:x:begin -->\nOLD\n<!-- frontpage:x:end -->\noutro\n"
    new = F.splice(text, {"x": "NEW"}, "t")
    ok("splice replaces only the region",
       new == "intro\n<!-- frontpage:x:begin -->\nNEW\n<!-- frontpage:x:end -->\noutro\n")
    ok("splice is idempotent", F.splice(new, {"x": "NEW"}, "t") == new)
    try:
        F.splice("no markers", {"x": "NEW"}, "t")
        ok("missing marker refused", False)
    except SystemExit:
        ok("missing marker refused", True)

    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "ledger.md")
        open(src, "w").write("the cause is  a long\nreason here")
        rel = os.path.relpath(src, F.ROOT)
        why = [dict(pattern_id="p", engine="e", regime="", cite=rel,
                    quote="a long reason")]
        ok("why quote found (whitespace-normalised)",
           "a long reason" in F.why_for(why, "p", "e", "short"))
        ok("no why row -> not analysed",
           F.why_for(why, "q", "e", "short") == "cause not yet analysed")
        why[0]["quote"] = "absent text"
        try:
            F.why_for(why, "p", "e", "short")
            ok("unfound quote refused", False)
        except SystemExit:
            ok("unfound quote refused", True)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
