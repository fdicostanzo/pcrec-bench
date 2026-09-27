#!/usr/bin/env python3
"""One-off: pull subject-grain rows + compile stamps for the manager's
auto-selection-on-short-whole-subject-matches ask (b104 outbox draft).
Reads store JSONL records directly (already-committed, validator-accepted
at write time) via pcrecbench.reduce -- no full store load."""
import sys, os, statistics
sys.path.insert(0, '.')
from pcrecbench import reduce as red

STORE = "store"

SYNTAX_PATTERNS = ["grp-cap", "grp-named", "grp-named-quote",
                   "rec-back", "rec-py", "rec-g-angle", "rec-fwd", "bak-2"]
ALTWIDE_PATTERNS = ["cnt-64", "w-64"]

SYNTAX_FILES = {
    "auto-caps": "store/records/syntax@0.1/pcrec_751b9c6d_auto-caps-simdna/syntax@0.1__pcrec_751b9c6d_auto-caps-simdna__budu-ryzen1600__20260927T113954Z.jsonl",
    "auto-nocaps": "store/records/syntax@0.1/pcrec_751b9c6d_auto-nocaps-simdna/syntax@0.1__pcrec_751b9c6d_auto-nocaps-simdna__budu-ryzen1600__20260927T122553Z.jsonl",
    "vm-caps": "store/records/syntax@0.1/pcrec_751b9c6d_vm-caps-simdna/syntax@0.1__pcrec_751b9c6d_vm-caps-simdna__budu-ryzen1600__20260927T130452Z.jsonl",
}
ALTWIDE_FILES = {
    "auto-caps": "store/records/altwide@0.2/pcrec_751b9c6d_auto-caps-simdna/altwide@0.2__pcrec_751b9c6d_auto-caps-simdna__budu-ryzen1600__20260927T103042Z.jsonl",
    "vm-caps": "store/records/altwide@0.2/pcrec_751b9c6d_vm-caps-simdna/altwide@0.2__pcrec_751b9c6d_vm-caps-simdna__budu-ryzen1600__20260927T110911Z.jsonl",
}


def compile_stamp(rows, pattern_id, form):
    for r in rows:
        if r.get("kind") == "compile" and r.get("pattern_id") == pattern_id and r.get("form", "plain") == form:
            m = r.get("engine_metadata", {})
            return {
                "engine": m.get("engine"),
                "engine_sel": m.get("engine_sel"),
                "dfa_prefilter": m.get("dfa_prefilter"),
                "vm_entry_shape": m.get("vm_entry_shape"),
                "vm_frameless": m.get("vm_frameless"),
                "dfa_match": m.get("dfa_match"),
                "req_why": m.get("req_why"),
                "end_window": m.get("end_window"),
                "emit_bytes": m.get("emit_bytes"),
                "emit_code_bytes": m.get("emit_code_bytes"),
                "program_sha256": m.get("program_sha256"),
                "outcome": r.get("compile_outcome"),
            }
    return None


def report_set(label, files, patterns, form, regime):
    print(f"\n=== {label} ({form}/{regime}) ===")
    per_config = {}
    for cfg, path in files.items():
        setup, rows = red.read_record(path)
        per_config[cfg] = rows
    for pat in patterns:
        print(f"\n-- {pat} --")
        for cfg, rows in per_config.items():
            cs = compile_stamp(rows, pat, form)
            print(f"  [{cfg}] compile: {cs}")
        cells = {}
        for cfg, rows in per_config.items():
            grouped = red.cells_from_record(rows)
            key = (pat, regime, form)
            if key in grouped:
                cells[cfg] = grouped[key]
        subj_ids = set()
        for cfg, subs in cells.items():
            subj_ids |= set(subs.keys())
        for sid in sorted(subj_ids):
            line = [f"  subject={sid}"]
            nbytes = None
            for cfg, subs in cells.items():
                if sid not in subs:
                    continue
                rs = subs[sid]
                if nbytes is None:
                    nbytes = rs[0].get("subject_bytes")
                vals = [red.ns_per_call(r) for r in rs if red.ns_per_call(r) is not None]
                if vals:
                    med = statistics.median(vals)
                    line.append(f"{cfg}={med:.2f}ns(n={len(vals)})")
            if nbytes is not None:
                line.insert(1, f"bytes={nbytes}")
            print(" ".join(line))


if __name__ == "__main__":
    report_set("syntax", SYNTAX_FILES, SYNTAX_PATTERNS, "whole-subject", "match-compliance")
    report_set("syntax (bak-2 short/large controls)", SYNTAX_FILES, ["bak-2"], "plain", "short-subject-search")
    report_set("altwide", ALTWIDE_FILES, ALTWIDE_PATTERNS, "whole-subject", "match-compliance")
    report_set("altwide (w-64 whole control)", ALTWIDE_FILES, ["w-64"], "whole-subject", "match-compliance")
