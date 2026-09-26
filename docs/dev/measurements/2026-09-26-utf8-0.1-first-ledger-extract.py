#!/usr/bin/env python3
"""utf8@0.1 first sample at pcrec ce658cb7: the numbers the ledger
(docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7.md) scores P1-P11 and
R0/R1/R8 on, per row -- the interpreter's sidecar prints only the WORST
value per clause; this prints every value behind it.

Source: lane b95read ([B95] READ), 2026-09-26. Reads ONLY committed files:
  G.tsv                (set grain, reporter v24; rank/compile/excluded/
                        did_not_compile/unsupported_by_pattern sections)
  G.subject-grain.tsv  (the subject-grain slice; P2/P3)
  store/records/utf8@0.1/*/*.jsonl (the stamps + wrong-answer diagnostics
                        the TSV does not carry: req_byte/req_run/engine,
                        the observed spans)
where G = reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.
No measurement is run.  Run from the repo root.
"""
import csv
import glob
import json
import statistics
import sys
from collections import defaultdict

G = "reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7"
csv.field_size_limit(1 << 30)


def rows(path):
    with open(path, encoding="utf-8") as fh:
        next(fh)
        yield from csv.DictReader(fh, delimiter="\t")


def short(t):
    return (t.replace("_default-caps-simdna", "").replace("-simdna", "").replace("_10.46", "")
            .replace("_ce658cb7", "").replace("_utf8", "-utf8"))


SET = list(rows(G + ".tsv"))
PCREC = sorted({r["testee"] for r in SET if r["testee"].startswith("pcrec_")})
ALL = sorted({r["testee"] for r in SET if r["section"] in ("rank_yes", "rank_no", "excluded")})


def cell(pattern, regime, testee, metric="median_ns"):
    for r in SET:
        if (r["section"] in ("rank_yes", "rank_no", "excluded") and r["pattern"] == pattern
                and r["regime_or_na"] == regime and r["testee"] == testee and r["metric"] == metric
                and r["form"] == "plain"):
            return float(r["value"])
    return None


def nwrong(pattern, regime, testee):
    for r in SET:
        if (r["section"] in ("rank_yes", "rank_no", "excluded") and r["pattern"] == pattern
                and r["regime_or_na"] == regime and r["testee"] == testee and r["form"] == "plain"
                and r["n_wrong"] != ""):
            return int(r["n_wrong"])
    return None


def compile_metric(pattern, testee, metric, form="plain"):
    for r in SET:
        if (r["section"] == "compile" and r["pattern"] == pattern and r["testee"] == testee
                and r["metric"] == metric and r["form"] == form):
            return r["value"]
    return None


def stamps():
    out = {}
    for f in sorted(glob.glob("store/records/utf8@0.1/pcrec_*/*.jsonl")):
        tid = f.split("/")[3]
        for ln in open(f, encoding="utf-8"):
            o = json.loads(ln)
            if o.get("kind") == "match":
                break
            if o.get("kind") == "compile" and o.get("trial") == 1 and "engine_metadata" in o:
                out[(tid, o["pattern_id"], o.get("form") or "plain")] = o["engine_metadata"]
    return out


ST = stamps()
SS, SL = "short-subject-search", "large-subject-throughput"

print("## P1.a  lit-offset-at-head vs -tail, search_short set median_ns (max/min) + P1.b stamps")
for t in PCREC:
    h, tl = cell("lit-offset-at-head", SS, t), cell("lit-offset-at-tail", SS, t)
    mh, mt = ST[(t, "lit-offset-at-head", "plain")], ST[(t, "lit-offset-at-tail", "plain")]
    print(f"{short(t)}\thead {h:.2f}\ttail {tl:.2f}\tmax/min {max(h, tl) / min(h, tl):.3f}"
          f"\thead req_byte={mh.get('req_byte')} run={mh.get('req_run')} why={mh.get('req_why')} eng={mh.get('engine')}"
          f"\ttail req_byte={mt.get('req_byte')} run={mt.get('req_run')} why={mt.get('req_why')} eng={mt.get('engine')}")
print("  (other testees, context)")
for t in ALL:
    if t in PCREC:
        continue
    h, tl = cell("lit-offset-at-head", SS, t), cell("lit-offset-at-tail", SS, t)
    if h and tl:
        print(f"  {short(t)}\thead {h:.2f}\ttail {tl:.2f}\tmax/min {max(h, tl) / min(h, tl):.3f}")

SG = defaultdict(dict)
LITS = ("lit-run-3", "lit-mixed-ascii", "lit-offset-at-head", "lit-offset-at-tail")
for r in rows(G + ".subject-grain.tsv"):
    if r["metric"] == "median_ns" and r["regime_or_na"] == SL and r["form"] == "plain" and r["pattern"] in LITS:
        SG[(r["subject_or_na"], r["testee"])][r["pattern"]] = float(r["value"])
for subj, tag in (("t-64k-cjk", "P2.a (gte 2)"), ("t-64k-asc", "P3.a (0.6667..1.5)")):
    print(f"## {tag}  lit-run-3 / lit-mixed-ascii on {subj}, subject-grain median_ns")
    for t in ALL:
        d = SG.get((subj, t), {})
        if len(d) == 2:
            inpop = t in PCREC or "interp" in t
            print(f"{'*' if inpop else ' '} {short(t)}\tlit-run-3 {d['lit-run-3']:.1f}\tlit-mixed-ascii {d['lit-mixed-ascii']:.1f}\tratio {d['lit-run-3'] / d['lit-mixed-ascii']:.3f}")

print("## beyond P1.a: the ORDER PAIR at THROUGHPUT grain (subject grain), tail / head median_ns")
for subj in ("t-64k-lat", "t-64k-cyr", "t-64k-cjk", "t-64k-asc", "t-64k", "t-256k", "t-1m"):
    for t in ALL:
        d = SG.get((subj, t), {})
        if "lit-offset-at-head" in d and "lit-offset-at-tail" in d:
            print(f"{subj}\t{short(t)}\thead {d['lit-offset-at-head']:.1f}\ttail {d['lit-offset-at-tail']:.1f}\ttail/head {d['lit-offset-at-tail'] / d['lit-offset-at-head']:.3f}")
print("## lit-run-3 and lit-mixed-ascii per throughput subject (median_ns), every testee")
for subj in ("t-64k-lat", "t-64k-cyr", "t-64k-cjk", "t-64k-asc", "t-1m"):
    for t in ALL:
        d = SG.get((subj, t), {})
        if "lit-run-3" in d and "lit-mixed-ascii" in d:
            print(f"{subj}\t{short(t)}\tlit-run-3 {d['lit-run-3']:.1f}\tlit-mixed-ascii {d['lit-mixed-ascii']:.1f}")

print("## P4.a  ci-moskva / ci-ascii-control compile:emit_bytes (plain) + engine")
for t in PCREC:
    a, b = int(compile_metric("ci-moskva", t, "emit_bytes")), int(compile_metric("ci-ascii-control", t, "emit_bytes"))
    print(f"{short(t)}\tci-moskva {a}\tci-ascii-control {b}\tratio {a / b:.3f}"
          f"\tengines {ST[(t, 'ci-moskva', 'plain')].get('engine')}/{ST[(t, 'ci-ascii-control', 'plain')].get('engine')}"
          f"\tclsfolds {ST[(t, 'ci-moskva', 'plain')].get('vm_cls_folds', '-')}/{ST[(t, 'ci-ascii-control', 'plain')].get('vm_cls_folds', '-')}")

print("## n_wrong per (pattern, regime, testee), non-zero only (R0; P4.b-d, P5.b, P6, P9.a, P10.a, P11)")
for r in SET:
    if r["section"] in ("rank_yes", "rank_no", "excluded") and r["metric"] in ("median_ns", "pass_rate") and r["n_wrong"] not in ("", "0"):
        print(f"{r['pattern']}\t{r['regime_or_na']}\t{short(r['testee'])}\tn_wrong {r['n_wrong']}\tpass_rate {r['pass_rate']}\t({r['section']})")

print("## the P4.b/P5.b/P6/P11.b populations: n_wrong over every testee that ran them (short-subject-search)")
for pat in ("ci-strasse", "ci-turkish-i", "cls-dot-rep", "cls-w-ucp", "cls-d-ucp", "cls-s-ucp", "asr-b-cyr-ucp", "ci-ucp-invariance", "prp-greek", "prp-greek-sc"):
    vals = {short(t): nwrong(pat, SS, t) for t in ALL}
    print(pat, "\t", " ".join(f"{k}={v}" for k, v in vals.items() if v is not None),
          "\t| no ranked row:", ",".join(k for k, v in vals.items() if v is None) or "-")

print("## P7.a  did_not_compile rows for family (f) on pcrec (section rows; prp-ingreek has no ranking group)")
for r in SET:
    if r["section"] == "did_not_compile" and r["testee"] in PCREC:
        print(f"{r['pattern']}\t{short(r['testee'])}\t{r['value'][:60]}")
print("## P7.b  prp-l emit_bytes / median(lit-* emit_bytes), plain")
for t in PCREC:
    lit = [int(r["value"]) for r in SET if r["section"] == "compile" and r["pattern"].startswith("lit-")
           and r["testee"] == t and r["metric"] == "emit_bytes" and r["form"] == "plain"]
    p = compile_metric("prp-l", t, "emit_bytes")
    m = statistics.median(lit) if lit else None
    print(f"{short(t)}\tprp-l {p}\tlit-* median {m} over {len(lit)}\tratio {int(p) / m:.3f}" if p else f"{short(t)}\tprp-l REFUSED (no emit_bytes)\tlit-* median {m} over {len(lit)}")

print("## R8 / P5.a / P9.b  unsupported_by_pattern census per (testee, family, requires)")
fam = lambda p: {"cls": "cls", "lit": "lit", "ci": "ci", "alt": "alt-qnt", "qnt": "alt-qnt", "asr": "asr", "prp": "prp"}.get(p.split("-")[0], p)
cen = defaultdict(list)
for r in SET:
    if r["section"] == "unsupported_by_pattern":
        req = r["gave_up_summary"].split(";")[0].replace("REQUIRES ", "")
        cen[(short(r["testee"]), fam(r["pattern"]), req)].append(r["pattern"])
for k in sorted(cen):
    print("\t".join(k), len(cen[k]), ",".join(sorted(cen[k])), sep="\t")
tot = defaultdict(int)
for (t, _, _), v in cen.items():
    tot[t] += len(v)
print("totals:", dict(sorted(tot.items())), "rows:", sum(tot.values()))

print("## context: every set cell where the best NON-pcrec FULL-GRAIN testee (vectorscan-block-nosom-utf8 is BOOLEAN grain -- it stops at the first match, so its throughput cells are not comparable and it is left out) beats pcrec auto-caps-utf8 by more than x2 (median_ns, plain, rankable rows only)")
med = defaultdict(dict)
for r in SET:
    if r["section"] in ("rank_yes", "rank_no") and r["metric"] == "median_ns" and r["form"] == "plain":
        med[(r["pattern"], r["regime_or_na"])][r["testee"]] = float(r["value"])
AUTO = "pcrec_ce658cb7_auto-caps-simdna_utf8"
out = []
for (p, rg), d in med.items():
    if AUTO not in d:
        continue
    others = {t: v for t, v in d.items() if not t.startswith("pcrec_") and not t.startswith("vectorscan_")}
    if not others:
        continue
    bt = min(others, key=others.get)
    ratio = d[AUTO] / others[bt]
    if ratio > 2:
        out.append((ratio, p, rg, d[AUTO], short(bt), others[bt]))
for ratio, p, rg, a, bt, b in sorted(out, reverse=True):
    print(f"{p}\t{rg}\tauto {a:.1f}\tbest-other {bt} {b:.1f}\tx{ratio:.2f}")
print(f"({len(out)} cells of {sum(1 for (p, rg), d in med.items() if AUTO in d)} with an auto-caps rankable row)")
