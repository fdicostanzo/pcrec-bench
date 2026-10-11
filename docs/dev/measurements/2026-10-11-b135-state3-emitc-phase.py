#!/usr/bin/env python3
"""[B135] state-3 read (lane b135read3): pcrec's own emit-c phase, 7388f1c0 -> b8337c33.
Source: store/records/<set>/pcrec_{7388f1c0,b8337c33}_auto-{caps,nocaps}-simdna[_utf8]/*.jsonl, window 3 (newest record).
Per (pattern, form): the median over trials of the compile row's cost.phases[name == 'emit-c'].elapsed_ns (a compile row
carries phases only where the pattern compiled). Prints per (set, cfg): n, median/p95/max of b8337c33 / 7388f1c0, and the
top ratios among patterns whose 7388f1c0 emit-c is >= 10 ms. Read-only; no engine run, no timing. Run from the repo root:
    python3 docs/dev/measurements/2026-10-11-b135-state3-emitc-phase.py
"""
import glob, json, statistics


def phases(f):
    d = {}
    for ln in open(f):
        if '"compile"' not in ln:
            continue
        r = json.loads(ln)
        if r.get("kind") != "compile":
            continue
        ph = (r.get("cost") or {}).get("phases")
        if ph:
            for p in ph:
                if p["name"] == "emit-c":
                    d.setdefault((r["pattern_id"], r.get("form", "plain")), []).append(p["elapsed_ns"])
    return {k: statistics.median(v) for k, v in d.items()}


for sb, ver in (("capability", "0.2"), ("syntax", "0.1"), ("utf8", "0.1"), ("bounded", "0.3"), ("loglines", "0.1"), ("litrun", "0.1")):
    suf = "_utf8" if sb == "utf8" else ""
    for cfg in ("caps", "nocaps"):
        fa = sorted(glob.glob("store/records/%s@%s/pcrec_7388f1c0_auto-%s-simdna%s/*.jsonl" % (sb, ver, cfg, suf)))[-1]
        fb = sorted(glob.glob("store/records/%s@%s/pcrec_b8337c33_auto-%s-simdna%s/*.jsonl" % (sb, ver, cfg, suf)))[-1]
        a, b = phases(fa), phases(fb)
        ks = [k for k in a if k in b]
        allr = sorted(b[k] / a[k] for k in ks)
        if not allr:
            print(sb, cfg, "no phases")
            continue
        big = sorted(((b[k] / a[k], k[0], k[1][:5], round(a[k] / 1e6), round(b[k] / 1e6)) for k in ks if a[k] > 1e7), reverse=True)[:3]
        print(sb, cfg, "emit-c b8337c33/7388f1c0 n=%d median %.3f p95 %.3f max %.3f" % (
            len(allr), statistics.median(allr), allr[int(.95 * (len(allr) - 1))], allr[-1]),
            "top(>=10ms):", [(round(x[0], 2),) + x[1:] for x in big])
