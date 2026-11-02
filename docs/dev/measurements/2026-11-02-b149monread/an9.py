# b149monread an9: scan-edge stamps (compile rows) for the named capability/syntax rows, auto vs noedge vs 614d45eb3.
import sys
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
def go(sb, names, pats):
    R = {n: load(t, sb)[0] for n, t in names.items()}
    for p in pats:
        for f in ("plain", "whole-subject"):
            out = []
            for n, r in R.items():
                c = r[1].get((p, f))
                if not c: out.append(f"{n}=-"); continue
                em = c[0]["engine_metadata"] or {}
                out.append(f"{n}: eng={em.get('engine')} sel={em.get('engine_sel')} edge={em.get('dfa_scan_edge')} edges={em.get('scan_edges')}/{em.get('scan_edges_match')} scan={em.get('dfa_scan')} pf={em.get('dfa_prefilter')} start={em.get('dfa_start')} emit={em.get('emit_bytes')} {c[0]['compile_outcome'][:4]}")
            print(f"  {p:38s} {f:13s} " + " | ".join(out))
print("== capability@0.4")
go("capability@0.4", {"auto": "pcrec_cb32eda28_auto-caps-simdna", "noedge": "pcrec_cb32eda28_auto-caps-simdna_noedge", "p614": "pcrec_614d45eb3_auto-caps-simdna"},
   ["wild-logparse-base10num-noatomic", "wild-logparse-base10num-grok", "wild-secrets-username-password-pair", "tail-space-eol", "tail-word-eoz", "tail-digits-eol", "letters-bounded-tail-z"])
print("== syntax@0.2")
go("syntax@0.2", {"auto": "pcrec_cb32eda28_auto-caps-simdna", "noedge": "pcrec_cb32eda28_auto-caps-simdna_noedge", "p614": "pcrec_614d45eb3_auto-caps-simdna"},
   ["cls-s-uc", "cls-range", "cls-w", "cls-posix", "mod-a", "unp-p-lc", "cls-d", "rec-back"])
