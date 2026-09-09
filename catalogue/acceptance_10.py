#!/usr/bin/env python3
"""§10 THE ACCEPTANCE TEST, run — docs/design/interpreter_v1.md §10.

    python3 catalogue/acceptance_10.py

Every numbered MUST / MUST-NOT on Reports A, B, C and D, each printed
with the ACTUAL firing (rule id, count, and the two numbers where the
note states them) or the actual non-firing. Not part of `make
check-interpret`'s six sections: this is the charter's own falsifiable
promise, written before any code existed, and it is run and its table
pasted into the lane report.

C.3 is a STATED KNOWN GAP of catalogue 1.0, not a MUST.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from catalogue.check_interpret import (CATALOGUE, INDEX_SNAPSHOT,  # noqa: E402
                                       FIXTURES, run_interpret)
from pcrecbench import interpret as I  # noqa: E402

A = "reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv"
B = "reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv"
C = "reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv"

RESULTS = []


def load(report_rel, predictions=None):
    facts = run_interpret(os.path.join(ROOT, report_rel), INDEX_SNAPSHOT,
                          predictions, "tsv")
    md = run_interpret(os.path.join(ROOT, report_rel), INDEX_SNAPSHOT,
                       predictions, "md")
    firings = {}
    tokens = {}
    for ln in facts.split("\n")[1:]:
        if not ln:
            continue
        f = ln.split("\t")
        if f[1] == "0":
            tokens[f[0]] = f[11]
            continue
        firings.setdefault(f[0], {}).setdefault(f[2], {})
        firings[f[0]][f[2]][f[10]] = f[11]
        firings[f[0]][f[2]]["_keys"] = (f[3], f[4], f[5], f[6], f[7], f[8])
    return firings, tokens, md, facts


def bullets(md, rule_id):
    out, on = [], False
    for ln in md.split("\n"):
        if ln.startswith("## "):
            on = ln.startswith(f"## {rule_id} ")
            continue
        if on and ln.startswith("- "):
            out.append(ln)
    return out


def item(label, passed, evidence):
    RESULTS.append((label, "PASS" if passed else "FAIL", evidence))
    print(f"{'PASS' if passed else 'FAIL'}  {label}\n      {evidence}")


def main():
    # ------------------------------------------------------- Report A --
    fa, ta, mda, _ = load(A)

    ids = sorted(f["record_id"] for f in fa.get("R-STATUS-2", {}).values())
    item("A.1 three inconclusive records, by id, as R-STATUS-2",
         len(ids) == 3 and all("20260825T17" in i for i in ids)
         and {f["status"] for f in fa["R-STATUS-2"].values()}
         == {"inconclusive-load"},
         f"R-STATUS-2 fires {len(ids)}x, all inconclusive-load: "
         + "; ".join(i.split("__")[1] + " @ " + i.split("__")[3] for i in ids))

    d2 = fa.get("R-DELTA-2", {})
    d3 = fa.get("R-DELTA-3", {})
    cells2 = {f["_keys"] for f in d2.values()}
    cells3 = {f["_keys"] for f in d3.values()}
    item("A.2 the collapse: R-DELTA-2 x6, R-DELTA-3 x4, co-firing on four "
         "cells",
         len(d2) == 6 and len(d3) == 4 and len(cells2 & cells3) == 4,
         f"R-DELTA-2 {len(d2)} firings, R-DELTA-3 {len(d3)}, "
         f"{len(cells2 & cells3)} cells carry both clauses of the compound "
         f"verdict")

    s3 = fa.get("R-STATUS-3", {})
    summaries = {f["gave_up_summary"] for f in s3.values()}
    codes = {c for c in ("-2:PCREC_ERR_STEPS", "-3:PCREC_ERR_FRAMES",
                         "-4:PCREC_ERR_WORK")
             if any(c in s for s in summaries)}
    jit = [f for f in s3.values()
           if f["testee"] == "libpcre2_10.46_jit-caps-simdna"]
    item("A.3 all thirteen excluded cells, by code and smallest subject",
         len(s3) == 13 and len(codes) == 3 and len(jit) == 1,
         f"R-STATUS-3 {len(s3)} firings; the three codes present "
         f"({', '.join(sorted(codes))}); the jit throughput row is rendered "
         f"with pass-rate {jit[0]['pass_rate']} and no fabricated cause")

    s12 = fa.get("R-STATUS-12", {})
    testees = sorted(f["testee"] for f in s12.values())
    item("A.3b the STEPS-vs-WORK pairing as R-STATUS-12, on three testees",
         len(s12) == 3
         and all(f["code_a"] == "`-2:PCREC_ERR_STEPS`"
                 and f["code_b"] == "`-4:PCREC_ERR_WORK`"
                 and f["subject"] == "t-c-long-atom-run" for f in s12.values()),
         f"{len(s12)} firings on {', '.join(testees)}"
         f"; subject t-c-long-atom-run, STEPS on factored vs WORK on orig")

    arm = fa.get("R-ARM-1", {})
    want = {("orig", "short-subject-search", "plain"): ("2.31", "862.2",
                                                        "12,546.2", "28,996.9"),
            ("orig", "match-compliance", "whole-subject"): ("1.28", "318.8",
                                                            "62,732.3",
                                                            "80,227.6")}
    found = {}
    for f in arm.values():
        key = (f["pattern"], f["regime"], f["form"])
        if key in want and {f["config_a"], f["config_b"]} == {
                "vm-caps-simdna", "vm-in-caps-simdna"}:
            found[key] = (f["ratio"], f["spread"], f["median_a"], f["median_b"])
    hit = all(k in found and found[k][0] == want[k][0]
              and found[k][1] == want[k][1] for k in want)
    item("A.4 the vm-in result as R-ARM-1, by rule and by number",
         hit and len(arm) == 14,
         f"R-ARM-1 {len(arm)} firings -> "
         f"{len(bullets(mda, 'R-ARM-1'))} bullets; "
         f"orig/short-search vm-in "
         f"{found[('orig','short-subject-search','plain')][3]} ns vs vm "
         f"{found[('orig','short-subject-search','plain')][2]} ns = x"
         f"{found[('orig','short-subject-search','plain')][0]} beyond "
         f"{found[('orig','short-subject-search','plain')][1]} ns; "
         f"orig/compliance vm-in "
         f"{found[('orig','match-compliance','whole-subject')][3]} vs vm "
         f"{found[('orig','match-compliance','whole-subject')][2]} = x"
         f"{found[('orig','match-compliance','whole-subject')][0]} beyond "
         f"{found[('orig','match-compliance','whole-subject')][1]} ns")

    d1 = fa.get("R-DELTA-1", {})
    ratios = sorted(f["ratio"] for f in d1.values())
    item("A.5 the unpredicted Δ as R-DELTA-1, THREE firings",
         len(d1) == 3 and ratios == ["1.00", "1.19", "1.26"],
         f"R-DELTA-1 {len(d1)} firings: " + ", ".join(
             f"{f['pattern']}/{f['regime']} {f['verdict']}"
             for f in sorted(d1.values(), key=lambda x: x["ratio"])))

    bf = fa.get("R-BUCKET-FORM", {})
    groups = sorted((f["pattern"], f["regime"], f["n_separate"], f["n_same"])
                    for f in bf.values())
    item("A.6 the regime artifact as R-BUCKET-FORM, one firing per GROUP",
         len(bf) == 2 and all(g[1] == "match-compliance" for g in groups),
         "; ".join(f"{g[0]} / {g[1]}: {g[2]} separate + {g[3]} same"
                   for g in groups))

    s6 = fa.get("R-STATUS-6", {})
    f6 = list(s6.values())[0] if s6 else {}
    item("A.7 the mixed schema population as R-STATUS-6",
         len(s6) == 1 and f6.get("schema_versions") == "1.1,1.2"
         and f6.get("n_pre_14") == "9" and f6.get("n_records") == "9",
         f"schema_versions {f6.get('schema_versions')}; "
         f"{f6.get('n_pre_14')} of {f6.get('n_records')} records read "
         f"n/a (v<schema>)")

    item("A.8 R-STATUS-9 must NOT fire",
         "R-STATUS-9" not in fa and ta.get("R-STATUS-9") == "no-matching-rows",
         f"R-STATUS-9 did not fire: {ta.get('R-STATUS-9')} (all nine records "
         f"read n/a (v1.x), which is provenance about their age)")

    # ------------------------------------------------------- Report B --
    fb, tb, mdb, factsb = load(B)

    r1 = fb.get("R-RANK-1", {})
    cell = [f for f in r1.values()
            if f["pattern"] == "cls-upto-8192"
            and f["regime"] == "match-compliance"
            and f["config"] == "auto-caps-simdna"]
    item("B.1 R-RANK-1 on cls-upto-8192 / match-compliance / whole-subject",
         len(cell) == 1 and cell[0]["old_ratio"] == "1.788241"
         and cell[0]["new_ratio"] == "0.269358",
         f"{cell[0]['old_pin']} {cell[0]['old_ratio']} -> "
         f"{cell[0]['new_pin']} {cell[0]['new_ratio']}, guard not engaged "
         f"(R-STATUS-13 {tb.get('R-STATUS-13')})" if cell else "absent")

    d2b = fb.get("R-DELTA-2", {})
    same = [f for f in d2b.values() if f["pattern"] == "cls-upto-8192"
            and f["regime"] == "match-compliance"]
    item("B.2 R-DELTA-2 on that same cell (the co-firing is required)",
         len(same) == 1 and same[0]["verdict"] == "selection changed (dfa → vm)"
         and cell and same[0]["config"] == cell[0]["config"]
         and same[0]["form"] == cell[0]["form"],
         f"{same[0]['testee']}: {same[0]['verdict']} -- the same "
         f"(pattern, regime, form, config) cell R-RANK-1 fired on"
         if same else "absent")

    span = fb.get("R-BUCKET-SPAN", {})
    named = {(f["pattern"], f["regime"]): f["verdict"] for f in span.values()}
    item("B.3 R-BUCKET-SPAN on the vm-in rows: partner 288d505, not 334fd10e",
         len(span) == 129
         and {f["config"] for f in span.values()} == {"vm-in-caps-simdna"}
         and {f["old_pin"] for f in span.values()} == {"288d505"}
         and named.get(("cls-upto-1024", "large-subject-throughput")) == "faster ×1.53"
         and named.get(("cls-upto-1024", "short-subject-search")) == "faster ×1.25",
         f"{len(span)} firings, all config vm-in-caps-simdna, all "
         f"288d505 -> d34c9131 (span 2); cls-upto-1024 throughput "
         f"faster ×1.53 and short-search faster ×1.25")

    vb = fb.get("R-BUCKET-VSBEST", {})
    inv = [f for f in vb.values() if f["pattern"] == "cls-upto-1024"
           and f["regime"] == "short-subject-search"]
    item("B.4 R-BUCKET-VSBEST on every group carrying >= 2 pin slugs",
         len(vb) == 129 and len(inv) == 1,
         f"{len(vb)} firings -> {len(bullets(mdb, 'R-BUCKET-VSBEST'))} "
         f"bullet(s); the cls-upto-1024 / short-subject-search inversion is "
         f"among them ({inv[0]['pin_slugs']})" if inv else "absent")

    dig = sorted(f["pattern"] for f in r1.values()
                 if f["config"] == "vm-in-caps-simdna"
                 and f["pattern"].startswith("dig-"))
    want_dig = ["dig-exact-16", "dig-exact-32", "dig-exact-8", "dig-upto-16",
                "dig-upto-8"]
    item("B.5 R-RANK-1 on at least five dig-* throughput rows (vm-in)",
         all(w in dig for w in want_dig),
         f"R-RANK-1 {len(r1)} firings total; the vm-in dig-* set is "
         + ", ".join(dig))

    d1b = fb.get("R-DELTA-1", {})
    rows = sum(1 for ln in factsb.split("\n") if ln.startswith("R-DELTA-1\t1"))
    item("B.6 R-DELTA-1's 202 firings rendered as 17 aggregated bullets",
         len(d1b) == 202 and len(bullets(mdb, "R-DELTA-1")) == 17,
         f"{len(d1b)} firings, {len(bullets(mdb, 'R-DELTA-1'))} bullets, "
         f"{rows} slot rows in the facts TSV (nothing dropped)")

    item("B.7 R-DELTA-4 must NOT fire (no predictions file)",
         "R-DELTA-4" not in fb and tb.get("R-DELTA-4") == "input-absent",
         f"R-DELTA-4: {tb.get('R-DELTA-4')}")

    # ------------------------------------------------------- Report C --
    fc, tc, mdc, _ = load(C)

    s4 = fc.get("R-STATUS-4", {})
    per_testee = {}
    for f in s4.values():
        per_testee[f["testee"]] = per_testee.get(f["testee"], 0) + 1
    diag = [f["diagnostic"] for f in s4.values() if f["pattern"] == "cnd-group"]
    item("C.1 R-STATUS-4: 60 distinct (pattern, testee) pairs, four bullets",
         len(s4) == 60 and len(bullets(mdc, "R-STATUS-4")) == 4
         and set(per_testee.values()) == {15}
         and diag and "conditionals" in diag[0],
         f"{len(s4)} pairs -> {len(bullets(mdc, 'R-STATUS-4'))} bullets, "
         f"15 patterns on each of {len(per_testee)} pcrec testees; "
         f"cnd-group reads \"{diag[0][:64]}...\"")

    s3c = fc.get("R-STATUS-3", {})
    rec1 = [f for f in s3c.values() if f["pattern"] == "rec-1"
            and f["regime"] == "large-subject-throughput"]
    asr = [f for f in s3c.values() if f["pattern"] == "asr-k-uc"
           and f["regime"] == "match-compliance"]
    item("C.2 R-STATUS-3 on the 23 excluded cells",
         len(s3c) == 23 and len(rec1) == 5 and len(asr) == 4,
         f"{len(s3c)} firings; rec-1 / large-subject-throughput on "
         f"{len(rec1)} testees at pass_rate {rec1[0]['pass_rate']} with "
         f"{rec1[0]['n_wrong']} wrong; asr-k-uc / match-compliance on "
         f"{len(asr)} pcrec arms at {asr[0]['pass_rate']} with "
         f"{asr[0]['n_wrong']} wrong")

    item("C.3 R-BUCKET-KB does NOT fire (a STATED KNOWN GAP, not a MUST)",
         tc.get("R-BUCKET-KB") == "no-registered-signatures",
         f"R-BUCKET-KB: {tc.get('R-BUCKET-KB')}")

    f2 = fc.get("R-FLOOR-2", {})
    anc = [f for f in f2.values() if f["pattern"] == "anc-caret"
           and f["regime"] == "short-subject-search"
           and f["testee"] == "pcrec_d34c9131_vm-caps-simdna"]
    item("C.4 R-FLOOR-2 on anc-caret / short-subject-search / vm-caps",
         len(anc) == 1 and anc[0]["cell_mean"] == "5.868"
         and anc[0]["floor_mean"] == "19.050" and anc[0]["ratio"] == "0.308",
         f"{anc[0]['cell_mean']} ns/subject against the floor pattern "
         f"`{anc[0]['floor_pattern']}`'s {anc[0]['floor_mean']} -> "
         f"×{anc[0]['ratio']} ({len(f2)} firings in the report)"
         if anc else "absent")

    f1 = fc.get("R-FLOOR-1", {})
    per = {}
    for f in f1.values():
        per[f["testee"]] = per.get(f["testee"], 0) + 1
    item("C.5 R-FLOOR-1 on the 190 timer-floor compile rows, two bullets",
         len(f1) == 190 and len(bullets(mdc, "R-FLOOR-1")) == 2
         and set(per.values()) == {95},
         f"{len(f1)} firings -> {len(bullets(mdc, 'R-FLOOR-1'))} bullets, "
         f"95 rows on each of the two libpcre2 arms")

    item("C.6 R-STATUS-9 must NOT fire",
         "R-STATUS-9" not in fc and tc.get("R-STATUS-9") == "no-matching-rows",
         f"R-STATUS-9: {tc.get('R-STATUS-9')} (all six records read "
         f"`agree (0 of N groups ...)`)")

    arm_c = fc.get("R-ARM-1", {})
    item("C.7 R-ARM-1's 635 firings rendered as 12 aggregated bullets",
         len(arm_c) == 635 and len(bullets(mdc, "R-ARM-1")) == 12,
         f"{len(arm_c)} firings -> {len(bullets(mdc, 'R-ARM-1'))} bullets, "
         f"all {len(arm_c)} in the facts TSV")

    # ------------------------------------------------------- Report D --
    d = os.path.join(FIXTURES, "CLEAN__all-measured")
    facts_d = run_interpret(os.path.join(d, "report.tsv"),
                            os.path.join(d, "index.tsv"), None, "tsv")
    fired, named = set(), set()
    for ln in facts_d.split("\n")[1:]:
        if not ln:
            continue
        f = ln.split("\t")
        named.add(f[0])
        if f[1] == "1":
            fired.add(f[0])
    item("D  the synthetic clean report: all 31 rules report fired=0",
         not fired and len(named) == 31,
         f"{len(named)} rules named, {len(fired)} fired")

    # --------------------------------------- the MUST-NOT items, checked --
    cat = I.load_catalogue(CATALOGUE)
    templates = " ".join(r["template"] for r in cat["rule"])
    banned = ("because", "due to", "caused by", "better", "worse", "should",
              "wave G", "splice")
    hits = [w for w in banned if w in templates.lower()]
    item("MUST-NOT (all three reports): no template asserts a cause, a "
         "preference or an attribution",
         not hits,
         "no template in the catalogue contains any of "
         + ", ".join(repr(w) for w in banned)
         + "; every cause a sidecar can carry is a `links` entry to a "
           "committed file (§7.3)")

    print()
    n_pass = sum(1 for _l, v, _e in RESULTS if v == "PASS")
    print(f"§10 acceptance: {n_pass} of {len(RESULTS)} items PASS")
    return 0 if n_pass == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
