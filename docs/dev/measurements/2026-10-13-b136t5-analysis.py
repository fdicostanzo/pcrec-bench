#!/usr/bin/env python3
"""[B136] tier 5 read (lane b136read5): the follow-up window 2026-10-13 09:23-14:39 EDT
(records stamped >= 20261013T130000Z unless a mode says otherwise). Reads committed
records only (nothing is timed); arithmetic = pcrecbench.reduce (the reporter's own),
reusing the helpers of 2026-10-13-b136-analysis.py. "ov" = the two [min,max] trial ranges
overlap, "DISJ" = they do not.
    python3 docs/dev/measurements/2026-10-13-b136t5-analysis.py MODE
MODE: utf8 | utf8all | cap | capall | bounded | email | sentinel
"""
import importlib.util, os, statistics, sys, glob
here = os.path.dirname(os.path.realpath(__file__))
spec = importlib.util.spec_from_file_location("a1", os.path.join(here, "2026-10-13-b136-analysis.py"))
A = importlib.util.module_from_spec(spec); sys.argv_saved = sys.argv; spec.loader.exec_module(A)
R, B, N, C, TP, SS = A.R, A.B, A.N, A.C, A.TP, A.SS
T5 = "20261013T130000Z"
MC = "match-compliance"


def rec(sb, testee, lo=A.WIN, hi="99999999T000000Z"):
    fs = [f for f in A.files(sb, testee) if lo <= A.fts(f) < hi]
    return A.load(fs[-1]) if fs else None


def regname(r):
    return {TP: "tp", SS: "ss"}.get(r, r)


def cellrows(sb, a, b, label, thr=1.03, show=None):
    """b/a over every set cell; returns list of (key, ratio, disj)."""
    out = []
    for key in sorted(a[1]):
        if key not in b[1]:
            continue
        ca, cb = A.sc(a[1], key), A.sc(b[1], key)
        if not ca or not cb or not ca.median_ns or not cb.median_ns:
            continue
        out.append((key, cb.median_ns / ca.median_ns, not A.ov(ca, cb), ca, cb))
    return out


def summarize(out, label, thr=1.03):
    rs = [x[1] for x in out]
    print("%s: n=%d DISJ=%d  %s" % (label, len(out), sum(x[2] for x in out), A.dist(rs)))
    over = [x for x in out if x[1] > thr]
    print("   > +%d%%: %d" % (round((thr - 1) * 100), len(over)))
    for k, r, dj, ca, cb in sorted(over, key=lambda x: -x[1]):
        print("     %-44s %-18s %-13s x%.3f %s  %s -> %s" % (k[0], A.R and k[1], k[2], r, "DISJ" if dj else "ov", A.fm(ca), A.fm(cb)))


def wrongs(q, label):
    w = []
    for k, v in q.items():
        if not v:
            continue
        for key, subs in v[1].items():
            c = R.reduce_set_cell(subs)
            if (c.pass_rate is not None and c.pass_rate < 1) or c.median_ns is None:
                w.append((k, key, c.pass_rate))
    print("%s: cells with pass_rate<1 or no number: %d" % (label, len(w)))
    for x in w[:20]:
        print("   ", x)
    return w


def utf8():
    q = {"B": rec("utf8", A.tid(B, "caps", "utf8"), A.WIN, T5), "N": rec("utf8", A.tid(N, "caps", "utf8"), A.WIN, T5),
         "C": rec("utf8", A.tid(C, "caps", "utf8"), A.WIN, T5),
         "D": rec("utf8", A.tid(N, "caps", "utf8", "noreqhandoff"), T5),
         "D3": rec("utf8", A.tid(N, "caps", "utf8", "noreqhandoff"), A.WIN, T5)}
    for k, v in q.items():
        print("# %s record %s rows-cells %d compile-rows %d" % (k, v[3] if v else None, len(v[1]) if v else 0, len(v[2]) if v else 0))
    d = q["D"]
    pats = sorted({k[0] for k in d[1]})
    print("# DENY (tier 5) patterns with cells: %d  %s" % (len(pats), pats))
    print("# DENY tier-3 record patterns with cells: %d" % len({k[0] for k in q["D3"][1]}))
    print("\n# ci-strasse / ci-ascii-control (and floor): set cells BASE | NEW | DENY | CANON, ns median[min..max]")
    for pat in ("ci-strasse", "ci-ascii-control", "asr-b-ascii", "floor"):
        for reg in (TP, SS, MC):
            for form in ("plain", "whole-subject"):
                key = (pat, reg, form)
                c = {k: (A.sc(v[1], key) if v else None) for k, v in q.items() if k != "D3"}
                if not any(c.values()):
                    continue
                print("%-18s %-26s %-13s B %s | N %s | D %s | C %s | N/B %s D/B %s D/N %s C/N %s %s" % (
                    pat, reg, form, A.fm(c["B"]), A.fm(c["N"]), A.fm(c["D"]), A.fm(c["C"]), A.rs(A.ratio(c["B"], c["N"])),
                    A.rs(A.ratio(c["B"], c["D"])), A.rs(A.ratio(c["N"], c["D"])), A.rs(A.ratio(c["N"], c["C"])),
                    "D/N " + ("ov" if c["D"] and c["N"] and A.ov(c["N"], c["D"]) else "DISJ")))
    print("\n# stamps (compile rows) for the two cells: B | N | D | C")
    for pat in ("ci-strasse", "ci-ascii-control"):
        for form in ("plain", "whole-subject"):
            for k in ("B", "N", "D", "C"):
                m = A.md(q[k][2], (pat, form)) if q[k] else {}
                if m:
                    print("%-18s %-13s %s engine=%s prefilter=%s K(req_handoff)=%s start=%s scan=%s req_byte=%s req_run=%s prog=%s" % (
                        pat, form, k, m.get("engine"), m.get("dfa_prefilter"), m.get("req_handoff"), m.get("dfa_start"), m.get("dfa_scan"),
                        m.get("req_byte"), m.get("req_run"), (m.get("program_sha256") or "")[:12]))
    print("\n# per-subject (ci-strasse, ci-ascii-control; plain) tp + ss: B N D C ns")
    for pat in ("ci-strasse", "ci-ascii-control"):
        for reg in (TP, SS):
            key = (pat, reg, "plain")
            sids = sorted(set().union(*[set(v[1].get(key, {})) for k, v in q.items() if v and k != "D3"]))
            rowsout = []
            for sid in sids:
                vals = []
                for k in ("B", "N", "D", "C"):
                    s = q[k][1].get(key, {}).get(sid) if q[k] else None
                    c = R.reduce_match_cell(s) if s else None
                    vals.append(c)
                if all(vals):
                    rowsout.append((sid, vals))
            print("## %s %s: %d subjects" % (pat, regname(reg), len(rowsout)))
            if reg == TP:
                for sid, v in rowsout:
                    print("   %-28s B %.1f N %.1f D %.1f C %.1f  N/B %.3f D/N %.3f" % (sid, v[0].median_ns, v[1].median_ns, v[2].median_ns, v[3].median_ns,
                          v[1].median_ns / v[0].median_ns, v[2].median_ns / v[1].median_ns))
            else:
                nb = [v[1].median_ns / v[0].median_ns for s, v in rowsout]
                dn = [v[2].median_ns / v[1].median_ns for s, v in rowsout]
                print("   N/B", A.dist(nb)); print("   D/N", A.dist(dn))


def utf8all():
    q = {"B": rec("utf8", A.tid(B, "caps", "utf8"), A.WIN, T5), "N": rec("utf8", A.tid(N, "caps", "utf8"), A.WIN, T5),
         "D": rec("utf8", A.tid(N, "caps", "utf8", "noreqhandoff"), T5)}
    wrongs(q, "utf8 B/N/D(tier5)")
    pats = sorted({k[0] for k in q["D"][1]})
    print("DENY pattern set (%d): %s" % (len(pats), pats))
    print("compile rows in D: %d, refused/none: %s" % (len(q["D"][2]), [k for k, r in q["D"][2].items() if r.get("outcome") not in (None, "compiled")][:10]))
    out = cellrows("utf8", q["N"], q["D"], "D/N")
    summarize(out, "utf8 DENY/NEW, all set cells")
    out = cellrows("utf8", q["B"], q["D"], "D/B")
    summarize(out, "utf8 DENY/BASE, all set cells")
    # stamp / program identity D vs N
    diff = []
    for key, rowd in q["D"][2].items():
        rown = q["N"][2].get(key)
        if rown:
            md, mn = rowd.get("engine_metadata", {}), rown.get("engine_metadata", {})
            if md.get("program_sha256") != mn.get("program_sha256"):
                diff.append((key, md.get("req_handoff"), mn.get("req_handoff"), md.get("dfa_prefilter"), mn.get("dfa_prefilter")))
    print("compile rows with program_sha256 D != N: %d" % len(diff))
    for x in diff[:30]:
        print("   ", x)


CAPD = "capability"


def cap():
    ct = lambda pin, cfg, extra="": A.tid(pin, cfg, "capability", extra)
    rb = rec(CAPD, ct(B, "nocaps"), T5); rn = rec(CAPD, ct(N, "nocaps"), T5)
    rb_old = rec(CAPD, ct(B, "nocaps"), "20261010T000000Z", T5)
    cb = rec(CAPD, ct(B, "caps"), A.WIN, T5); cn = rec(CAPD, ct(N, "caps"), A.WIN, T5); cc = rec(CAPD, ct(C, "caps"), A.WIN, T5)
    cd = rec(CAPD, ct(N, "caps", "noreqhandoff"), T5)
    for n, v in (("nocaps B (T5)", rb), ("nocaps N (T5)", rn), ("nocaps B previous", rb_old), ("caps B", cb), ("caps N", cn), ("caps C", cc), ("caps D (T5)", cd)):
        print("# %-18s %s" % (n, v[3] if v else None))
    print("\n# 15th mover by value, wild-secrets-username-password-pair (nocaps) and the caps contrast")
    pat = "wild-secrets-username-password-pair"
    for lab, v in (("nocaps B", rb), ("nocaps N", rn), ("caps B", cb), ("caps N", cn), ("caps D", cd), ("caps C", cc)):
        for form in ("plain", "whole-subject"):
            m = A.md(v[2], (pat, form)) if v else {}
            if m:
                print("%-9s %-13s engine=%s prefilter=%s req_handoff=%s start=%s scan=%s req_byte=%s req_run=%s prog=%s" % (
                    lab, form, m.get("engine"), m.get("dfa_prefilter"), m.get("req_handoff"), m.get("dfa_start"), m.get("dfa_scan"),
                    m.get("req_byte"), m.get("req_run"), (m.get("program_sha256") or "")[:12]))
    print("\n# its cells, nocaps BASE | NEW (and the 10-11 BASE record), caps B | N | D | C")
    for reg in (TP, SS, MC):
        for form in ("plain", "whole-subject"):
            key = (pat, reg, form)
            c = {k: (A.sc(v[1], key) if v else None) for k, v in (("nB", rb), ("nN", rn), ("nB0", rb_old), ("cB", cb), ("cN", cn), ("cD", cd), ("cC", cc))}
            if not any(c.values()):
                continue
            print("%-26s %-13s nocaps B %s | N %s | B(10-11) %s | N/B %s %s | N/B(10-11) %s || caps B %s N %s D %s C %s | N/B %s D/N %s" % (
                reg, form, A.fm(c["nB"]), A.fm(c["nN"]), A.fm(c["nB0"]), A.rs(A.ratio(c["nB"], c["nN"])),
                "ov" if c["nB"] and c["nN"] and A.ov(c["nB"], c["nN"]) else "DISJ", A.rs(A.ratio(c["nB0"], c["nN"])),
                A.fm(c["cB"]), A.fm(c["cN"]), A.fm(c["cD"]), A.fm(c["cC"]), A.rs(A.ratio(c["cB"], c["cN"])), A.rs(A.ratio(c["cN"], c["cD"]))))
    print("\n# per-subject throughput of the mover, nocaps B | N")
    key = (pat, TP, "plain")
    for sid in sorted(rb[1].get(key, {})):
        a = R.reduce_match_cell(rb[1][key][sid]); b = R.reduce_match_cell(rn[1][key][sid])
        print("   %-28s B %.1f N %.1f N/B %.3f %s" % (sid, a.median_ns, b.median_ns, b.median_ns / a.median_ns, "ov" if A.ov(a, b) else "DISJ"))
    print("\n# ALL nocaps handoff movers (compile rows with dfa_prefilter handoff at N, or K gained), BASE>NEW")
    for (p, form), row in sorted(rn[2].items()):
        mn = row.get("engine_metadata", {}); mb = A.md(rb[2], (p, form))
        if mn.get("dfa_prefilter") == "handoff" or (mn.get("req_handoff") not in (None, "none") and mb.get("req_handoff") in (None, "none")):
            print("  %-48s %-13s prefilter %s>%s K %s>%s engine %s" % (p, form, mb.get("dfa_prefilter"), mn.get("dfa_prefilter"), mb.get("req_handoff"), mn.get("req_handoff"), mn.get("engine")))
    print("\n# nocaps NEW/BASE: every set cell, and the REQ_HANDOFF-set cells")
    out = cellrows(CAPD, rb, rn, "N/B")
    summarize(out, "capability nocaps NEW/BASE (all set cells)")
    print("   median of ratios on program-identical cells (program_sha256 equal):")
    ident = []
    for x in out:
        k = x[0]
        mb, mn = A.md(rb[2], (k[0], k[2])), A.md(rn[2], (k[0], k[2]))
        if mb.get("program_sha256") and mb.get("program_sha256") == mn.get("program_sha256"):
            ident.append(x[1])
    print("   ", A.dist(ident))
    out0 = cellrows(CAPD, rb_old, rb, "B/B0")
    summarize(out0, "capability nocaps BASE this-day / BASE 10-11 (instrument)")


def capall():
    ct = lambda pin, cfg, extra="": A.tid(pin, cfg, "capability", extra)
    cb = rec(CAPD, ct(B, "caps"), A.WIN, T5); cn = rec(CAPD, ct(N, "caps"), A.WIN, T5); cc = rec(CAPD, ct(C, "caps"), A.WIN, T5)
    cd = rec(CAPD, ct(N, "caps", "noreqhandoff"), T5)
    wrongs({"B": cb, "N": cn, "C": cc, "D": cd}, "capability caps B N C D")
    for lab, a, b in (("D/N", cn, cd), ("D/B", cb, cd), ("N/B", cb, cn)):
        summarize(cellrows(CAPD, a, b, lab), "capability caps " + lab)
        # program-identical subset
        out = cellrows(CAPD, a, b, lab); ident = []
        for x in out:
            k = x[0]
            ma, mb = A.md(a[2], (k[0], k[2])), A.md(b[2], (k[0], k[2]))
            if ma.get("program_sha256") and ma.get("program_sha256") == mb.get("program_sha256"):
                ident.append(x[1])
        print("   program-identical subset %s" % A.dist(ident))
    print("\n# D/N on the tail family and grok")
    for pat in A.TAILS + ("wild-logparse-quotedstring-grok",):
        for reg in (TP, SS, MC):
            for form in ("plain", "whole-subject"):
                key = (pat, reg, form)
                n, d, b = A.sc(cn[1], key), A.sc(cd[1], key), A.sc(cb[1], key)
                if n and d and b:
                    print("%-34s %-26s %-13s B %s N %s D %s | D/N %s %s D/B %s" % (pat, reg, form, A.fm(b), A.fm(n), A.fm(d), A.rs(A.ratio(n, d)), "ov" if A.ov(n, d) else "DISJ", A.rs(A.ratio(b, d))))
    print("\n# the 14 caps movers (REQ_HANDOFF set at N): D/N and D/B")
    for (p, form), row in sorted(cn[2].items()):
        mn = row.get("engine_metadata", {})
        if mn.get("req_handoff") in (None, "none") or form != "plain":
            continue
        for reg in (TP, SS):
            key = (p, reg, form)
            b, n, d = A.sc(cb[1], key), A.sc(cn[1], key), A.sc(cd[1], key)
            if b and n and d:
                print("%-44s %-3s K %s pref %s | N/B %s D/B %s D/N %s" % (p, regname(reg), mn.get("req_handoff"), mn.get("dfa_prefilter"), A.rs(A.ratio(b, n)), A.rs(A.ratio(b, d)), A.rs(A.ratio(n, d))))


def bounded():
    bt = lambda pin, extra="": A.tid(pin, "caps", "bounded", extra)
    rB = rec("bounded", bt(B), A.WIN, T5); rN = rec("bounded", bt(N), A.WIN, T5); rD = rec("bounded", bt(N, "noreqhandoff"), A.WIN, T5)
    rC = rec("bounded", bt(C), T5)
    for n, v in (("B", rB), ("N", rN), ("D", rD), ("C(T5)", rC)):
        print("# %-6s %s" % (n, v[3] if v else None))
    wrongs({"B": rB, "N": rN, "D": rD, "C": rC}, "bounded")
    summarize(cellrows("bounded", rN, rC, "C/N"), "bounded C/NEW (all set cells)")
    summarize(cellrows("bounded", rB, rC, "C/B"), "bounded C/BASE (all set cells)")
    for lab, a in (("N", rN),):
        out = cellrows("bounded", a, rC, "C/N"); ident = []; chg = []
        for x in out:
            k = x[0]
            ma, mc = A.md(a[2], (k[0], k[2])), A.md(rC[2], (k[0], k[2]))
            (ident if ma.get("program_sha256") == mc.get("program_sha256") else chg).append(x)
        print("program-identical C/N cells: %s" % A.dist([x[1] for x in ident]))
        print("program-changed C/N cells: %d" % len(chg))
        for k, r, dj, ca, cb_ in sorted(chg):
            print("   %-36s %-26s %-13s x%.3f %s" % (k[0], k[1], k[2], r, "DISJ" if dj else "ov"))
    print("\n# the dotted4 cells and handoff movers: B N D C")
    for pat in ("dotted4",):
        for reg in (TP, SS):
            key = (pat, reg, "plain")
            c = [A.sc(v[1], key) for v in (rB, rN, rD, rC)]
            print(pat, regname(reg), " | ".join(A.fm(x) for x in c), "C/N", A.rs(A.ratio(c[1], c[3])), "N/B", A.rs(A.ratio(c[0], c[1])))
    prev = rec("bounded", bt(B), "20261011T000000Z", "20261012T000000Z")
    print("# instrument: bounded BASE 10-12 vs BASE 10-11 (%s): " % (prev[3] if prev else None))
    if prev:
        summarize(cellrows("bounded", prev, rB, "B/B0"), "bounded BASE 10-12 / BASE 10-11")


def email():
    et = lambda pin, cfg="caps": A.tid(pin, cfg, "email-specimen")
    rC = rec("email-specimen", et(C), T5)
    print("# email C record", rC[3] if rC else None)
    for pin, lab in ((B, "b8337c33"), ("7388f1c0", "7388f1c0"), ("a15fb77b", "a15fb77b")):
        fs = A.files("email-specimen", et(pin))
        for f in fs:
            r = A.load(f)
            out = cellrows("email-specimen", r, rC, "C/%s" % lab)
            ident = []
            for x in out:
                k = x[0]
                ma, mc = A.md(r[2], (k[0], k[2])), A.md(rC[2], (k[0], k[2]))
                if ma.get("program_sha256") and ma.get("program_sha256") == mc.get("program_sha256"):
                    ident.append(x[1])
            print("\n== C vs %s record %s" % (lab, r[3]))
            summarize(out, "email C/%s" % lab)
            print("   program-identical cells: %s" % A.dist(ident))
            chg = [x for x in out if x[0] not in [None] and A.md(r[2], (x[0][0], x[0][2])).get("program_sha256") != A.md(rC[2], (x[0][0], x[0][2])).get("program_sha256")]
            print("   program-changed cells: %d" % len(chg))
            for k, rr, dj, ca, cb_ in sorted(chg, key=lambda x: x[0])[:12]:
                print("     %-30s %-26s %-13s x%.3f %s" % (k[0], k[1], k[2], rr, "DISJ" if dj else "ov"))
    jt = A.JIT
    j0 = rec("email-specimen", jt, A.WIN)
    print("\n# jit in this window (tier 4): ", j0[3] if j0 else None)
    wrongs({"C": rC}, "email C")


def sentinel():
    ts = sorted(glob.glob("%s/records/sentinel@0.1/*/*.jsonl" % A.STORE))
    want = [f for f in ts if A.fts(f) >= A.WIN]
    slots = {}
    for f in want:
        t = f.split("/")[-2]; s = A.fts(f)
        if s >= "20261013T170000Z":
            slot = "close5"
        elif s >= T5:
            slot = "open5"
        elif s >= "20261013T040000Z":
            slot = "end3"
        elif s >= "20261013T000000Z":
            slot = "end2"
        elif s >= "20261012T180000Z":
            slot = "end1"
        else:
            slot = "open1"
        slots[(t, slot)] = f
    cells = {}
    for (t, slot), f in slots.items():
        for key, subs in A.load(f)[1].items():
            if key[2] == "plain":
                cells[(t, key[0], slot)] = R.reduce_set_cell(subs)
    tests = sorted({t for t, _ in slots})
    print("# sentinel records per (testee, slot):")
    for (t, s), f in sorted(slots.items()):
        print("   %-44s %-7s %s" % (t, s, A.fts(f)))
    pairs = (("close5", "open5"), ("open5", "open1"), ("close5", "open1"), ("close5", "end3"), ("open5", "end3"))
    print("\n# ratio later/earlier over the 15 pattern cells (min / median / max, DISJ)")
    for t in tests:
        for a, b in pairs:
            r, dj = [], 0
            for p in sorted({k[1] for k in cells if k[0] == t}):
                x, y = cells.get((t, p, a)), cells.get((t, p, b))
                if x and y and x.median_ns and y.median_ns:
                    r.append(x.median_ns / y.median_ns); dj += not A.ov(x, y)
            if r:
                print("%-44s %-7s/%-7s n=%2d min %.3f median %.3f max %.3f DISJ %d" % (t, a, b, len(r), min(r), statistics.median(r), max(r), dj))
    print("\n# pcrec pins in the same slot (program-identical on sentinel): later pin / BASE")
    for slot in ("open5", "close5"):
        for t in tests:
            if "pcrec" not in t:
                continue
        pins = [t for t in tests if "pcrec_b8337c33_auto-caps" in t]
        for t in tests:
            if "pcrec" in t and t not in pins:
                r = []
                for p in sorted({k[1] for k in cells if k[0] == t}):
                    x, y = cells.get((t, p, slot)), cells.get((pins[0], p, slot)) if pins else None
                    if x and y and x.median_ns and y.median_ns:
                        r.append(x.median_ns / y.median_ns)
                if r:
                    print("%-7s %-44s / BASE caps: n=%d median %.3f min %.3f max %.3f" % (slot, t, len(r), statistics.median(r), min(r), max(r)))
    print("\n# jit row, all slots: sum of 15 medians")
    for slot in ("open1", "end1", "end2", "end3", "open5", "close5"):
        vals = [cells[(A.JIT, p, slot)].median_ns for p in sorted({k[1] for k in cells if k[0] == A.JIT}) if (A.JIT, p, slot) in cells]
        if vals:
            print("   %-7s sum %.0f ns (n=%d)" % (slot, sum(vals), len(vals)))
    print("\n# per cell: caps 6b2dbd3e open1|end3|open5|close5 medians and close5/open5")
    t = A.tid(C, "caps", "sentinel")
    for p in sorted({k[1] for k in cells if k[0] == t}):
        c = [cells.get((t, p, s)) for s in ("open1", "end3", "open5", "close5")]
        if all(c):
            print("   %-30s %s | close5/open5 %.3f %s" % (p, " | ".join(A.fm(x) for x in c), c[3].median_ns / c[2].median_ns, "ov" if A.ov(c[3], c[2]) else "DISJ"))


if __name__ == "__main__":
    globals()[sys.argv[1]]()
