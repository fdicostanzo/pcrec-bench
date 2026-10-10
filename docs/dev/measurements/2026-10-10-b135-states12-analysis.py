#!/usr/bin/env python3
"""[B135] states 1+2 window (2026-10-10, 12:13-19:19 EDT): acceptance + movers.
Source: store/records/{capability@0.2,loglines@0.1,email-specimen@0.2,litrun@0.1}/
pcrec_{a15fb77b,7388f1c0}_auto-{caps,nocaps}-simdna/*.jsonl (16 records, state 1 =
a15fb77b abi 72 BEFORE, state 2 = 7388f1c0 abi 73 [OPT-REVEND] AFTER).
Arithmetic: pcrecbench.reduce -- reduce_match_cell for one subject (median/min/max of
the per-trial ns/call), reduce_set_cell for a set cell (per-trial sum over subjects,
then median/min/max) -- the reporter's own. "ov" = the two [min,max] trial ranges
overlap. Predictions: pcrec inbox I-142 s1 (ns ranges per call, ratios).
Run from the repo root:  python3 THIS accept|movers [STORE_DIR]
"""
import glob, json, os, sys
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from pcrecbench import reduce as R

mode = sys.argv[1]
store = sys.argv[2] if len(sys.argv) > 2 else "store"
SETS = [("capability", "0.2"), ("loglines", "0.1"), ("email-specimen", "0.2"), ("litrun", "0.1")]
PINS = ("a15fb77b", "7388f1c0")
CFGS = ("caps", "nocaps")
STAMPS = ("engine", "engine_sel", "dfa_scan", "dfa_start", "dfa_prefilter", "dfa_match",
          "req_why", "end_window", "memfn_libc", "dfa_scan_edge", "vm_prefilter", "vm_entry_shape")


def load(sb, ver, pin, cfg):
    fs = glob.glob("%s/records/%s@%s/pcrec_%s_auto-%s-simdna/*.jsonl" % (store, sb, ver, pin, cfg))
    assert len(fs) == 1, (sb, pin, cfg, fs)
    setup, rows = R.read_record(fs[0])
    comp = {}
    for ln in open(fs[0]).read().split("\n")[1:]:
        if ln.strip():
            r = json.loads(ln)
            if r.get("kind") == "compile":
                comp[(r["pattern_id"], r.get("form", "plain"))] = r
    return setup, R.cells_from_record(rows), comp


def ov(a, b):
    return not (b.max_ns < a.min_ns or b.min_ns > a.max_ns)


if mode == "accept":
    # I-142 s1: (pattern, subject) -> (lo, hi) predicted ns per call (rev-end), steps
    P = {}
    nm, s4, s9, s11, s20 = (7, 24), (13, 42), (19, 60), (22, 66), (33, 98)
    for pat, d in (("tail-digits-eol", {"digits": s9, "txt": nm, "space": nm}),
                   ("tail-word-eoz", {"digits": s9, "txt": s4, "space": nm}),
                   ("tail-space-eol", {"digits": nm, "txt": nm, "space": s4}),
                   ("tail-ext-lower-txt", {"digits": nm, "txt": s11, "space": nm}),
                   ("tail-dotstar-txt", {"digits": nm, "txt": s20, "space": nm})):
        for k, v in d.items():
            P[(pat, "t-tail-%s-1m" % k)] = v
    P[("tail-space-eol", "t-trim-nearmiss-16k")] = (7, 24)
    print("# acceptance cells: ns per call, median [min..max] over 5 trials; ratio = a15fb77b / 7388f1c0 median")
    print("# columns: pattern | subject | cfg | pred lo-hi | A=a15fb77b | B=7388f1c0 | ratio | pred ratio (A/hi..A/lo) | verdict | sig>150 | sig40-60")
    out = []
    data = {}
    for pin in PINS:
        for cfg in CFGS:
            data[(pin, cfg)] = load("capability", "0.2", pin, cfg)
    for (pat, sub), (lo, hi) in sorted(P.items()):
        for cfg in CFGS:
            a = R.reduce_match_cell(data[(PINS[0], cfg)][1][(pat, "large-subject-throughput" if sub != "t-trim-nearmiss-16k" else "large-subject-throughput", "plain")][sub])
            b = R.reduce_match_cell(data[(PINS[1], cfg)][1][(pat, "large-subject-throughput", "plain")][sub])
            v = "inside" if lo <= b.median_ns <= hi else ("above" if b.median_ns > hi else "below")
            out.append((pat, sub, cfg, lo, hi, a, b, v))
            print("%-20s %-22s %-6s %3d-%-3d | A %12.1f [%.1f..%.1f] | B %7.2f [%.2f..%.2f] | x%-10.0f | pred x%.0f..x%.0f | %-6s | %s | %s" % (
                pat, sub, cfg, lo, hi, a.median_ns, a.min_ns, a.max_ns, b.median_ns, b.min_ns, b.max_ns,
                a.median_ns / b.median_ns, a.median_ns / hi, a.median_ns / lo, v,
                "SIG>150" if b.median_ns > 150 else "-", "SIG40-60" if 40 <= b.median_ns <= 60 else "-"))
    print()
    print("# body-size check: the five patterns on every throughput subject, B (7388f1c0) ns/call, caps | nocaps")
    subs = ["t-64k", "t-256k", "t-1m", "t-tail-digits-1m", "t-tail-txt-1m", "t-tail-space-1m"]
    for pat in ("floor-byte", "tail-digits-eol", "tail-word-eoz", "tail-space-eol", "tail-ext-lower-txt", "tail-dotstar-txt"):
        for pin in PINS:
            row = []
            for cfg in CFGS:
                cells = data[(pin, cfg)][1][(pat, "large-subject-throughput", "plain")]
                row.append(" ".join("%s=%.1f" % (s, R.reduce_match_cell(cells[s]).median_ns) for s in subs if s in cells))
            print("%-20s %s  caps: %s\n%-20s %s  nocaps: %s" % (pat, pin, row[0], "", pin, row[1]))
    print()
    print("# stamps at both pins (compile rows), the five tail patterns, caps")
    for pat in ("tail-digits-eol", "tail-word-eoz", "tail-space-eol", "tail-ext-lower-txt", "tail-dotstar-txt"):
        for cfg in CFGS:
            for pin in PINS:
                m = data[(pin, cfg)][2][(pat, "plain")]["engine_metadata"]
                print("%-20s %-6s %s " % (pat, cfg, pin) + " ".join("%s=%s" % (k, m.get(k)) for k in STAMPS if k in m)
                      + " emit=%s prog=%s" % (m.get("emit_bytes"), m.get("program_sha256", "")[:8]))
elif mode == "movers":
    print("set | cfg | pattern | regime | form | A=a15fb77b median ns [min..max] | B=7388f1c0 | B/A | ov | stamp changes | program same")
    for sb, ver in SETS:
        for cfg in CFGS:
            sa, ca, ka = load(sb, ver, PINS[0], cfg)
            sbb, cb, kb = load(sb, ver, PINS[1], cfg)
            for key in sorted(set(ca) & set(cb), key=lambda k: tuple(str(x) for x in k)):
                A = R.reduce_set_cell(ca[key]); B = R.reduce_set_cell(cb[key])
                pat, reg, form = key
                if A.median_ns is None or B.median_ns is None:
                    print("%s | %s | %s | %s | %s | NO-NUMBER A:%s B:%s" % (sb, cfg, pat, reg, form,
                          A.pass_rate if A.median_ns is None else "ok", B.pass_rate if B.median_ns is None else "ok"))
                    continue
                ma = (ka.get((pat, form)) or {}).get("engine_metadata", {})
                mb = (kb.get((pat, form)) or {}).get("engine_metadata", {})
                ch = ["%s:%s>%s" % (k, ma.get(k), mb.get(k)) for k in STAMPS if ma.get(k) != mb.get(k)]
                same = (ma.get("program_sha256") == mb.get("program_sha256")) if ma and mb else None
                print("%s | %s | %s | %s | %s | %.1f [%.1f..%.1f] | %.1f [%.1f..%.1f] | %.3f | %s | %s | %s" % (
                    sb, cfg, pat, reg, form, A.median_ns, A.min_ns, A.max_ns, B.median_ns, B.min_ns, B.max_ns,
                    B.median_ns / A.median_ns, "ov" if ov(A, B) else "DISJ", ";".join(ch) or "-", same))
