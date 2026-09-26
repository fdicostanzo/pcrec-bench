#!/usr/bin/env python3
"""utf8@0.1 first sample at pcrec ce658cb7 (abi 33): per-pattern COMPILE
times for every pcrec utf8 config, read from the canonical records.

Source: lane b95read ([B95] READ), 2026-09-26, pcrecdev1's ask (plan [B77]
row, O-58: "the five-trial numbers per pattern, for every pcrec utf8
config, go in the first-window ledger"). No measurement is run: this reads
store/records/utf8@0.1/pcrec_ce658cb7_*_utf8/*.jsonl (the four records the
report group 2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7 includes).

Per (config, pattern, form): the compile outcome, the trial count, the
median / min / max of cost.total_ns over the trials (spread = max/min),
the median of each cost phase (emit-c = pcrec itself, gcc, load), and the
stamps the record carries (engine, engine_sel, emit_bytes, warned
emit_bytes). A refusal is one row (the harness does not re-try a refusal;
its cost is the refused attempt's own). `form` '-' is the plain form.

Run from the repo root:  python3 docs/dev/measurements/2026-09-26-utf8-0.1-pcrec-compile-times.py
"""
import glob
import json
import statistics
import sys

CFG = {"auto-caps-simdna_utf8": "auto", "auto-nocaps-simdna_utf8": "nocaps",
       "vm-caps-simdna_utf8": "vm", "vm-in-caps-simdna_utf8": "vm-in"}


def med(xs):
    return statistics.median(xs) if xs else None


def s(ns):
    return "-" if ns is None else f"{ns / 1e9:.3f}"


def main():
    files = sorted(glob.glob("store/records/utf8@0.1/pcrec_ce658cb7_*_utf8/*.jsonl"))
    if len(files) != 4:
        sys.exit(f"expected 4 pcrec utf8 records, found {len(files)}")
    rows = {}
    for f in files:
        tid = f.split("/")[3]
        cfg = CFG[tid.split("pcrec_ce658cb7_", 1)[1]]
        for ln in open(f, encoding="utf-8"):
            o = json.loads(ln)
            if o.get("kind") != "compile":
                continue
            rows.setdefault((cfg, o["pattern_id"], o.get("form") or "-"), []).append(o)
    print("# source: " + " ".join(files))
    cols = ["config", "pattern", "form", "outcome", "n", "median_s", "min_s", "max_s",
            "spread", "emitc_med_s", "gcc_med_s", "load_med_s", "engine", "engine_sel",
            "emit_bytes", "warned_emit_bytes", "diagnostic"]
    print("\t".join(cols))
    order = ["auto", "nocaps", "vm", "vm-in"]
    for key in sorted(rows, key=lambda k: (k[1], k[2], order.index(k[0]))):
        cfg, pat, form = key
        rs = rows[key]
        outc = sorted({r["compile_outcome"] for r in rs})
        tot = [r["cost"]["total_ns"] for r in rs if "cost" in r]
        ph = {}
        for r in rs:
            for p in r.get("cost", {}).get("phases", []):
                ph.setdefault(p["name"], []).append(p["elapsed_ns"])
        em = rs[0].get("engine_metadata", {})
        diag = (rs[0].get("diagnostic") or "")
        diag = diag.replace("\t", " ").replace("\n", " ")[:120] if rs[0]["compile_outcome"] != "compiled" else ""
        spread = f"{max(tot) / min(tot):.3f}" if len(tot) > 1 and min(tot) > 0 else "-"
        print("\t".join(str(x) for x in [
            cfg, pat, form, "/".join(outc), len(rs), s(med(tot)), s(min(tot) if tot else None),
            s(max(tot) if tot else None), spread, s(med(ph.get("emit-c"))), s(med(ph.get("gcc"))),
            s(med(ph.get("load"))), em.get("engine", "-"), em.get("engine_sel", "-"),
            em.get("emit_bytes", "-"), em.get("warned_emit_bytes", "-"), diag or "-"]))


if __name__ == "__main__":
    main()
