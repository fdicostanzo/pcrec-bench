#!/usr/bin/env python3
"""[B135] state-3 window (2026-10-10 20:21 EDT -> 2026-10-11 13:03 EDT) read.
Source: store/records/<set>@<ver>/<testee>/*.jsonl -- window 3 = records stamped
>= 20261011T000000Z (pcrec b8337c33 abi 74 [START-LANDING], and 7388f1c0 abi 73
REPEATED as the cross-window control); window 1 = the states 1+2 window
(20261010T16..23Z: a15fb77b abi 72, 7388f1c0 abi 73).
Arithmetic: pcrecbench.reduce (reduce_match_cell: one subject's median/min/max
over trials; reduce_set_cell: per-trial sum over subjects, then median/min/max)
-- the reporter's own. "ov" = the two [min,max] trial ranges overlap, "DISJ" =
they do not. Ratios are computed from those medians.
Run from the repo root:
    python3 docs/dev/measurements/2026-10-11-b135-state3-analysis.py MODE [ARGS]
MODE: sentinel | control | movers | threestate | tail | grok | sfx | som | fit
"""
import glob, json, os, statistics, sys
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from pcrecbench import reduce as R

STORE = os.environ.get("STORE", "store")
SETS = {"capability": "0.2", "loglines": "0.1", "email-specimen": "0.2", "litrun": "0.1",
        "utf8": "0.1", "syntax": "0.1", "bounded": "0.3", "altwide": "0.3", "sentinel": "0.1"}
TIER1 = ("capability", "loglines", "email-specimen", "litrun")
STAMPS = ("engine", "engine_sel", "dfa_scan", "dfa_start", "dfa_prefilter", "dfa_match",
          "req_why", "end_window", "dfa_scan_edge", "dfa_uniform_folds", "scan_edges",
          "vm_prefilter", "vm_entry_shape")
_cache = {}


def tid(pin, cfg, sb):
    return "pcrec_%s_auto-%s-simdna%s" % (pin, cfg, "_utf8" if sb == "utf8" else "")


def files(sb, testee):
    return sorted(glob.glob("%s/records/%s@%s/%s/*.jsonl" % (STORE, sb, SETS[sb], testee)))


def fts(f):
    return os.path.basename(f).rsplit("__", 1)[1].split(".")[0]  # 20261011T005755Z


def window_of(ts):
    if ts < "20261010T200000Z":
        return "w1"
    if ts < "20261011T000000Z":
        return "w1"
    return "w3"


def pick(sb, testee, window):
    fs = [f for f in files(sb, testee) if window_of(fts(f)) == window and fts(f) >= "20261010T160000Z"]
    if not fs:
        return None
    return fs[-1]


def load(f):
    if f in _cache:
        return _cache[f]
    setup, rows = R.read_record(f)
    comp = {}
    for r in rows:
        if r.get("kind") == "compile":
            comp[(r["pattern_id"], r.get("form", "plain"))] = r
    out = (setup, R.cells_from_record(rows), comp)
    _cache[f] = out
    return out


def ov(a, b):
    return not (b.max_ns < a.min_ns or b.min_ns > a.max_ns)


def md(comp, key):
    return (comp.get(key) or {}).get("engine_metadata", {})


def pct(xs, p):
    xs = sorted(xs)
    if not xs:
        return float("nan")
    k = (len(xs) - 1) * p
    lo = int(k)
    hi = min(lo + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (k - lo)


def dist(xs):
    if not xs:
        return "n=0"
    return "n=%d min %.3f p5 %.3f p25 %.3f med %.3f p75 %.3f p95 %.3f max %.3f" % (
        len(xs), min(xs), pct(xs, .05), pct(xs, .25), pct(xs, .5), pct(xs, .75), pct(xs, .95), max(xs))


def setcells(sb, testee, window):
    f = pick(sb, testee, window)
    if not f:
        return None
    setup, cells, comp = load(f)
    return f, cells, comp


def sentinel():
    slots = ("w1open", "w1end", "w3open", "w3end", "w3end2")

    def slot2(ts):
        if ts < "20261010T200000Z":
            return "w1open" if ts < "20261010T200000Z" and ts <= "20261010T175000Z" else "w1end"
        if ts < "20261011T000000Z":
            return "w1end"
        if ts < "20261011T040000Z":
            return "w3open"
        if ts < "20261011T120000Z":
            return "w3end"
        return "w3end2"
    testees = sorted(os.path.basename(d) for d in glob.glob("%s/records/sentinel@0.1/*" % STORE))
    cells = {}
    stamps = {}
    for t in testees:
        for f in files("sentinel", t):
            ts = fts(f)
            s = slot2(ts)
            setup, cs, comp = load(f)
            stamps[(t, s)] = ts
            for key, subs in cs.items():
                if key[2] == "plain":
                    cells[(t, key[0], s)] = R.reduce_set_cell(subs)
    print("# sentinel@0.1: 15 patterns x 75 short subjects, set-grain sums, 5 trials; slot timestamps (UTC):")
    for (t, s), ts in sorted(stamps.items()):
        print("#   %-34s %-7s %s" % (t, s, ts))
    pairs = (("w3end", "w3open"), ("w3end2", "w3open"), ("w3end2", "w3end"))
    print("\n# per testee: ratio later/earlier over the 15 pattern cells (min / median / max, disjoint-range count)")
    rows = []
    for t in testees:
        for a, b in pairs + (("w3open", "w1open"), ("w3open", "w1end"), ("w1end", "w1open")):
            rs = []
            dj = 0
            n = 0
            for p in sorted({k[1] for k in cells if k[0] == t}):
                A, B = cells.get((t, p, a)), cells.get((t, p, b))
                if not A or not B or A.median_ns is None or B.median_ns is None:
                    continue
                n += 1
                rs.append(A.median_ns / B.median_ns)
                if not ov(A, B):
                    dj += 1
            if n:
                rows.append((t, a, b, n, min(rs), statistics.median(rs), max(rs), dj))
    for t, a, b, n, lo, med, hi, dj in rows:
        print("%-34s %-7s/%-7s n=%2d  min %.3f  median %.3f  max %.3f  DISJ %d" % (t, a, b, n, lo, med, hi, dj))
    print("\n# per cell (window 3 only): median ns [min..max] open | end | end2 and ratios")
    for t in testees:
        for p in sorted({k[1] for k in cells if k[0] == t}):
            c = [cells.get((t, p, s)) for s in ("w3open", "w3end", "w3end2")]
            if not all(c):
                continue
            print("%-34s %-42s | %s | end/open %.3f %s end2/open %.3f %s" % (
                t, p, " | ".join("%8.1f[%.1f..%.1f]" % (x.median_ns, x.min_ns, x.max_ns) for x in c),
                c[1].median_ns / c[0].median_ns, "ov" if ov(c[1], c[0]) else "DISJ",
                c[2].median_ns / c[0].median_ns, "ov" if ov(c[2], c[0]) else "DISJ"))


def control():
    print("# CROSS-WINDOW CONTROL: pcrec 7388f1c0 in window 3 (B, 2026-10-11) vs window 1 (A, 2026-10-10), same testee ids")
    print("# set | cfg | n cells | ratio B/A distribution | DISJ cells | outside +-5%% | outside +-10%%")
    allr = []
    detail = []
    for sb in TIER1:
        for cfg in ("caps", "nocaps"):
            t = tid("7388f1c0", cfg, sb)
            A = setcells(sb, t, "w1")
            B = setcells(sb, t, "w3")
            fa, ca, ka = A
            fb, cb, kb = B
            rs = []
            dj = 0
            for key in sorted(set(ca) & set(cb), key=lambda k: tuple(str(x) for x in k)):
                a = R.reduce_set_cell(ca[key])
                b = R.reduce_set_cell(cb[key])
                if a.median_ns is None or b.median_ns is None:
                    continue
                r = b.median_ns / a.median_ns
                d = not ov(a, b)
                rs.append(r)
                dj += d
                detail.append((sb, cfg, key, a, b, r, d, md(ka, (key[0], key[2])).get("program_sha256") == md(kb, (key[0], key[2])).get("program_sha256")))
            allr += rs
            print("%-15s %-6s %s | DISJ %d | >5%% %d | >10%% %d" % (
                sb, cfg, dist(rs), dj, sum(1 for r in rs if abs(r - 1) > .05), sum(1 for r in rs if abs(r - 1) > .10)))
    print("ALL tier-1 cells: %s" % dist(allr))
    print("\n# by regime (all four sets, caps+nocaps)")
    byreg = {}
    for sb, cfg, key, a, b, r, d, same in detail:
        byreg.setdefault((key[1], key[2]), []).append(r)
    for k, v in sorted(byreg.items()):
        print("%-30s %s" % (k, dist(v)))
    print("\n# by baseline scale (A median): <100ns / 100ns-1us / >=1us")
    for lab, lo, hi in (("<100ns", 0, 100), ("100ns-1us", 100, 1000), (">=1us", 1000, 1e18)):
        v = [r for sb, cfg, key, a, b, r, d, same in detail if lo <= a.median_ns < hi]
        print("%-10s %s" % (lab, dist(v)))
    print("\n# the cells outside +-5%, or DISJ with |ratio-1|>2%")
    for sb, cfg, key, a, b, r, d, same in sorted(detail, key=lambda x: -abs(x[5] - 1))[:40]:
        print("%-14s %-6s %-40s %-26s %-10s A %.1f[%.1f..%.1f] B %.1f[%.1f..%.1f] B/A %.3f %s same_prog=%s" % (
            sb, cfg, key[0], key[1], key[2], a.median_ns, a.min_ns, a.max_ns, b.median_ns, b.min_ns, b.max_ns, r, "DISJ" if d else "ov", same))


def movers_rows(sb, cfg):
    A = setcells(sb, tid("7388f1c0", cfg, sb), "w3")
    B = setcells(sb, tid("b8337c33", cfg, sb), "w3")
    fa, ca, ka = A
    fb, cb, kb = B
    out = []
    for key in sorted(set(ca) & set(cb), key=lambda k: tuple(str(x) for x in k)):
        a = R.reduce_set_cell(ca[key])
        b = R.reduce_set_cell(cb[key])
        pat, reg, form = key
        ma, mb = md(ka, (pat, form)), md(kb, (pat, form))
        same = (ma.get("program_sha256") == mb.get("program_sha256")) if ma and mb else None
        out.append(dict(sb=sb, cfg=cfg, pat=pat, reg=reg, form=form, a=a, b=b, ma=ma, mb=mb, same=same,
                        cls=("end-minus-width" if mb.get("dfa_start") == "end-minus-width" and ma.get("dfa_start") != "end-minus-width"
                             else "landing" if mb.get("dfa_start") == "landing" and ma.get("dfa_start") != "landing"
                             else "other-changed" if same is False else "identical")))
    return out


def movers():
    print("set | cfg | pattern | regime | form | class | A=7388f1c0 (w3) median [min..max] | B=b8337c33 | B/A | ov | stamp changes | program same")
    allrows = []
    for sb in ("capability", "loglines", "email-specimen", "litrun", "utf8", "syntax", "bounded"):
        for cfg in ("caps", "nocaps"):
            for m in movers_rows(sb, cfg):
                allrows.append(m)
                a, b = m["a"], m["b"]
                if a.median_ns is None or b.median_ns is None:
                    print("%s | %s | %s | %s | %s | %s | NO-NUMBER (pass %s / %s)" % (m["sb"], m["cfg"], m["pat"], m["reg"], m["form"], m["cls"], a.pass_rate, b.pass_rate))
                    continue
                ch = ["%s:%s>%s" % (k, m["ma"].get(k), m["mb"].get(k)) for k in STAMPS if m["ma"].get(k) != m["mb"].get(k)]
                print("%s | %s | %s | %s | %s | %s | %.1f [%.1f..%.1f] | %.1f [%.1f..%.1f] | %.3f | %s | %s | %s" % (
                    m["sb"], m["cfg"], m["pat"], m["reg"], m["form"], m["cls"], a.median_ns, a.min_ns, a.max_ns,
                    b.median_ns, b.min_ns, b.max_ns, b.median_ns / a.median_ns, "ov" if ov(a, b) else "DISJ",
                    ";".join(ch) or "-", m["same"]))
    print("\n# SUMMARY by (set, class): cells with numbers; better = B<A beyond overlap; worse = B>A beyond overlap; ov = ranges overlap")
    keyf = lambda m: (m["sb"], m["cls"])
    seen = {}
    for m in allrows:
        a, b = m["a"], m["b"]
        if a.median_ns is None or b.median_ns is None:
            continue
        seen.setdefault(keyf(m), []).append(m)
    for k in sorted(seen):
        v = seen[k]
        rs = [m["b"].median_ns / m["a"].median_ns for m in v]
        better = sum(1 for m in v if not ov(m["a"], m["b"]) and m["b"].median_ns < m["a"].median_ns)
        worse = sum(1 for m in v if not ov(m["a"], m["b"]) and m["b"].median_ns > m["a"].median_ns)
        print("%-15s %-16s n=%3d better %3d worse %3d overlap %3d | ratio %s" % (k[0], k[1], len(v), better, worse, len(v) - better - worse, dist(rs)))
    print("\n# SUMMARY by class, all sets, by regime")
    seen = {}
    for m in allrows:
        a, b = m["a"], m["b"]
        if a.median_ns is None or b.median_ns is None:
            continue
        seen.setdefault((m["cls"], m["reg"], m["form"]), []).append(m)
    for k in sorted(seen):
        v = seen[k]
        rs = [m["b"].median_ns / m["a"].median_ns for m in v]
        better = sum(1 for m in v if not ov(m["a"], m["b"]) and m["b"].median_ns < m["a"].median_ns)
        worse = sum(1 for m in v if not ov(m["a"], m["b"]) and m["b"].median_ns > m["a"].median_ns)
        print("%-16s %-28s %-6s n=%3d better %3d worse %3d | %s" % (k[0], k[1], k[2], len(v), better, worse, dist(rs)))
    return allrows


def threestate():
    print("# THREE STATES, tier-1 sets: set-cell medians ns: a15fb77b(w1) | 7388f1c0(w1) | 7388f1c0(w3, control) | b8337c33(w3)")
    print("# set | cfg | pattern | regime | form | dfa_start@b8337c33 | a15 | 7388 w1 | 7388 w3 | b8337 | r(7388w1/a15) | r(7388w3/7388w1) | r(b8337/7388w3) | r(b8337/7388w1)")
    for sb in TIER1:
        for cfg in ("caps", "nocaps"):
            a15 = setcells(sb, tid("a15fb77b", cfg, sb), "w1")
            w1 = setcells(sb, tid("7388f1c0", cfg, sb), "w1")
            w3 = setcells(sb, tid("7388f1c0", cfg, sb), "w3")
            b8 = setcells(sb, tid("b8337c33", cfg, sb), "w3")
            keys = set(a15[1]) & set(w1[1]) & set(w3[1]) & set(b8[1])
            for key in sorted(keys, key=lambda k: tuple(str(x) for x in k)):
                c = [R.reduce_set_cell(x[1][key]) for x in (a15, w1, w3, b8)]
                if any(x.median_ns is None for x in c):
                    continue
                m8 = md(b8[2], (key[0], key[2]))
                m73 = md(w1[2], (key[0], key[2]))
                moved = m8.get("dfa_start") != m73.get("dfa_start") or m8.get("program_sha256") != m73.get("program_sha256")
                # print only cells where any step moved >3% or a stamp moved at b8337c33
                rr = (c[1].median_ns / c[0].median_ns, c[2].median_ns / c[1].median_ns, c[3].median_ns / c[2].median_ns, c[3].median_ns / c[1].median_ns)
                if not moved and max(abs(x - 1) for x in rr) < 0.03:
                    continue
                print("%s | %s | %s | %s | %s | %s | %s | r %.3f %.3f %.3f %.3f%s" % (
                    sb, cfg, key[0], key[1], key[2], m8.get("dfa_start"),
                    " | ".join("%.1f" % x.median_ns for x in c), *rr, "  [program moved]" if moved else ""))


def tail():
    print("# TAIL FAMILY (capability@0.2 large-subject-throughput + short-subject-search): must be FLAT at b8337c33 (I-146)")
    pats = ("tail-digits-eol", "tail-word-eoz", "tail-space-eol", "tail-ext-lower-txt", "tail-dotstar-txt", "letters-bounded-tail-z")
    for cfg in ("caps", "nocaps"):
        w1 = setcells("capability", tid("7388f1c0", cfg, "capability"), "w1")
        w3 = setcells("capability", tid("7388f1c0", cfg, "capability"), "w3")
        b8 = setcells("capability", tid("b8337c33", cfg, "capability"), "w3")
        print("\n## set cells, %s: 7388 w1 | 7388 w3 | b8337 w3 | b8/7388w3 | ov | w3/w1 | stamps (dfa_scan/dfa_start, program same)" % cfg)
        for p in pats:
            for reg in ("large-subject-throughput", "short-subject-search"):
                key = (p, reg, "plain")
                if key not in b8[1]:
                    continue
                c = [R.reduce_set_cell(x[1][key]) for x in (w1, w3, b8)]
                m73, m8 = md(w3[2], (p, "plain")), md(b8[2], (p, "plain"))
                print("%-24s %-26s | %10.1f | %10.1f | %10.1f | %.3f %s | %.3f | %s/%s>%s/%s same=%s" % (
                    p, reg, c[0].median_ns, c[1].median_ns, c[2].median_ns, c[2].median_ns / c[1].median_ns,
                    "ov" if ov(c[1], c[2]) else "DISJ", c[1].median_ns / c[0].median_ns,
                    m73.get("dfa_scan"), m73.get("dfa_start"), m8.get("dfa_scan"), m8.get("dfa_start"),
                    m73.get("program_sha256") == m8.get("program_sha256")))
    print("\n## per-subject acceptance cells (large-subject-throughput): ns/call median [min..max]: 7388 w1 | 7388 w3 | b8337 w3 | b8/7388w3")
    for cfg in ("caps", "nocaps"):
        w1 = setcells("capability", tid("7388f1c0", cfg, "capability"), "w1")
        w3 = setcells("capability", tid("7388f1c0", cfg, "capability"), "w3")
        b8 = setcells("capability", tid("b8337c33", cfg, "capability"), "w3")
        bad = 0
        n = 0
        rs = []
        for p in pats:
            key = (p, "large-subject-throughput", "plain")
            for s in sorted(b8[1][key]):
                r = [R.reduce_match_cell(x[1][key][s]) for x in (w1, w3, b8)]
                if any(x.median_ns is None for x in r):
                    continue
                n += 1
                rr = r[2].median_ns / r[1].median_ns
                rs.append(rr)
                flag = "DISJ" if not ov(r[1], r[2]) else "ov"
                if flag == "DISJ":
                    bad += 1
                if s.startswith("t-tail") or s.startswith("t-trim") or s.startswith("t-evil") or flag == "DISJ":
                    print("%-6s %-24s %-24s | %9.2f[%.2f..%.2f] | %9.2f[%.2f..%.2f] | %9.2f[%.2f..%.2f] | %.3f %s" % (
                        cfg, p, s, r[0].median_ns, r[0].min_ns, r[0].max_ns, r[1].median_ns, r[1].min_ns, r[1].max_ns,
                        r[2].median_ns, r[2].min_ns, r[2].max_ns, rr, flag))
        print("-- %s: %d per-subject cells, b8337c33/7388f1c0(w3) %s; DISJ %d" % (cfg, n, dist(rs), bad))
    print("\n## stamps at b8337c33 (compile rows) for the tail patterns, both forms")
    for p in pats:
        for form in ("plain", "whole-subject"):
            b8 = setcells("capability", tid("b8337c33", "caps", "capability"), "w3")
            w3 = setcells("capability", tid("7388f1c0", "caps", "capability"), "w3")
            if (p, form) in b8[2]:
                print("%-24s %-14s 7388: %s | b8337: %s | prog same=%s" % (
                    p, form, " ".join("%s=%s" % (k, md(w3[2], (p, form)).get(k)) for k in ("dfa_scan", "dfa_start", "dfa_prefilter")),
                    " ".join("%s=%s" % (k, md(b8[2], (p, form)).get(k)) for k in ("dfa_scan", "dfa_start", "dfa_prefilter")),
                    md(w3[2], (p, form)).get("program_sha256") == md(b8[2], (p, form)).get("program_sha256")))


def grok():
    pat = "wild-logparse-quotedstring-grok"
    reg = "short-subject-search"
    print("# %s x %s (capability@0.2): set-cell median ns [min..max], then per-subject" % (pat, reg))
    for cfg in ("caps", "nocaps"):
        slots = (("a15fb77b w1", "a15fb77b", "w1"), ("7388f1c0 w1", "7388f1c0", "w1"), ("7388f1c0 w3", "7388f1c0", "w3"), ("b8337c33 w3", "b8337c33", "w3"))
        cs = []
        for lab, pin, w in slots:
            x = setcells("capability", tid(pin, cfg, "capability"), w)
            c = R.reduce_set_cell(x[1][(pat, reg, "plain")])
            m = md(x[2], (pat, "plain"))
            cs.append((lab, x, c, m))
            print("%-6s %-13s %9.1f [%.1f..%.1f]  engine=%s sel=%s emit=%s prog=%s vm_prog=%s" % (
                cfg, lab, c.median_ns, c.min_ns, c.max_ns, m.get("engine"), m.get("engine_sel"), m.get("emit_bytes"),
                (m.get("program_sha256") or "")[:12], m.get("vm_program_bytes")))
        for i, j in ((1, 2), (2, 3), (1, 3)):
            print("   %s -> %s : x%.3f %s" % (cs[i][0], cs[j][0], cs[j][2].median_ns / cs[i][2].median_ns, "ov" if ov(cs[i][2], cs[j][2]) else "DISJ"))
        # per-subject delta w3 -> b8337
        subs = sorted(cs[2][1][1][(pat, reg, "plain")])
        d = []
        for s in subs:
            a = R.reduce_match_cell(cs[2][1][1][(pat, reg, "plain")][s])
            b = R.reduce_match_cell(cs[3][1][1][(pat, reg, "plain")][s])
            d.append(b.median_ns - a.median_ns)
        print("   per-subject delta ns (b8337c33 - 7388f1c0 w3): %s; slower on %d of %d" % (dist(d), sum(1 for x in d if x > 0), len(d)))
        d2 = []
        for s in subs:
            a = R.reduce_match_cell(cs[1][1][1][(pat, reg, "plain")][s])
            b = R.reduce_match_cell(cs[2][1][1][(pat, reg, "plain")][s])
            d2.append(b.median_ns - a.median_ns)
        print("   per-subject delta ns (7388f1c0 w3 - w1): %s; slower on %d of %d" % (dist(d2), sum(1 for x in d2 if x > 0), len(d2)))
        d3 = []
        for s in subs:
            a = R.reduce_match_cell(cs[0][1][1][(pat, reg, "plain")][s])
            b = R.reduce_match_cell(cs[1][1][1][(pat, reg, "plain")][s])
            d3.append(b.median_ns - a.median_ns)
        print("   per-subject delta ns (7388f1c0 w1 - a15fb77b w1): %s; slower on %d of %d" % (dist(d3), sum(1 for x in d3 if x > 0), len(d3)))
    # other regimes for the same pattern
    print("\n# the same pattern in the other regimes / forms, caps: a15 w1 | 7388 w1 | 7388 w3 | b8337 w3")
    for key in sorted(k for k in setcells("capability", tid("b8337c33", "caps", "capability"), "w3")[1] if k[0] == pat):
        cs = []
        for pin, w in (("a15fb77b", "w1"), ("7388f1c0", "w1"), ("7388f1c0", "w3"), ("b8337c33", "w3")):
            x = setcells("capability", tid(pin, "caps", "capability"), w)
            cs.append(R.reduce_set_cell(x[1][key]) if key in x[1] else None)
        print(key, " | ".join("%.1f" % c.median_ns if c and c.median_ns else "-" for c in cs))


def sfx():
    print("# every loglines/* and altwide@0.3 sfx-* set cell at b8337c33: set | pattern | regime | form | cfg | median ns | min-max | engine | dfa_scan | dfa_start | dfa_prefilter | n_subjects")
    for sb in ("loglines", "altwide"):
        for cfg in ("caps", "nocaps"):
            x = setcells(sb, tid("b8337c33", cfg, sb), "w3")
            for key in sorted(x[1], key=lambda k: tuple(str(z) for z in k)):
                pat, reg, form = key
                if sb == "altwide" and not pat.startswith("sfx-"):
                    continue
                c = R.reduce_set_cell(x[1][key])
                m = md(x[2], (pat, form))
                if c.median_ns is None:
                    print("%s | %s | %s | %s | %s | NO-NUMBER pass_rate %.3f" % (sb, pat, reg, form, cfg, c.pass_rate))
                    continue
                print("%s | %s | %s | %s | %s | %.1f | %.1f-%.1f | %s | %s | %s | %s | %d" % (
                    sb, pat, reg, form, cfg, c.median_ns, c.min_ns, c.max_ns, m.get("engine"), m.get("dfa_scan"),
                    m.get("dfa_start"), m.get("dfa_prefilter"), c.n_subjects))


def som():
    print("# Vectorscan SOM (2026-10-08/09 window) vs pcrec-auto, capability@0.2 tail-* large-subject cells, per subject (ns/call median [min..max])")
    print("# CROSS-WINDOW: vectorscan records 2026-10-09T03:09Z (nosom) / 03:38Z (som); pcrec 7388f1c0 w1 2026-10-10, w3 2026-10-11 / b8337c33 w3 2026-10-11")
    vs = {}
    for lab, t in (("som", "vectorscan_5.4.11_block-som-nocaps-simd"), ("nosom", "vectorscan_5.4.11_block-nosom-nocaps-simd")):
        f = files("capability", t)[-1]
        vs[lab] = (f, load(f))
        print("# %s record %s" % (lab, os.path.basename(f)))
    pc = {}
    for lab, pin, w in (("auto 7388f1c0 w1", "7388f1c0", "w1"), ("auto 7388f1c0 w3", "7388f1c0", "w3"), ("auto b8337c33 w3", "b8337c33", "w3")):
        pc[lab] = setcells("capability", tid(pin, "nocaps", "capability"), w)
    pats = ("tail-digits-eol", "tail-word-eoz", "tail-space-eol", "tail-ext-lower-txt", "tail-dotstar-txt")
    reg = "large-subject-throughput"
    labs = ["som", "nosom"] + list(pc)
    print("pattern | subject | " + " | ".join(labs) + " | b8337c33 / som | nosom / som")
    setsum = {}
    for p in pats:
        key = (p, reg, "plain")
        subs = sorted(pc["auto b8337c33 w3"][1][key])
        for s in subs:
            vals = []
            for l in labs:
                cells = vs[l][1][1] if l in vs else pc[l][1]
                if key not in cells or s not in cells[key]:
                    vals.append(None)
                    continue
                vals.append(R.reduce_match_cell(cells[key][s]))
            fmt = ["%.1f[%.1f..%.1f]" % (v.median_ns, v.min_ns, v.max_ns) if v and v.median_ns is not None else ("fail(pass %.2f)" % v.pass_rate if v else "-") for v in vals]
            som_, nos, b8 = vals[0], vals[1], vals[4]
            r1 = "%.2f" % (b8.median_ns / som_.median_ns) if som_ and som_.median_ns and b8 and b8.median_ns else "-"
            r2 = "%.2f" % (nos.median_ns / som_.median_ns) if som_ and som_.median_ns and nos and nos.median_ns else "-"
            print("%s | %s | %s | %s | %s" % (p, s, " | ".join(fmt), r1, r2))
        print()
    print("# set cells (sum over the large-subject set): ns median [min..max]; ok = every subject judged correct")
    for p in pats:
        key = (p, reg, "plain")
        row = []
        for l in labs:
            cells = vs[l][1][1] if l in vs else pc[l][1]
            c = R.reduce_set_cell(cells[key]) if key in cells else None
            row.append("%s: %s" % (l, ("%.1f[%.1f..%.1f]" % (c.median_ns, c.min_ns, c.max_ns)) if c and c.median_ns else "excluded(%s)" % (c.failing_subjects if c else "absent")))
        print(p, " | ".join(row))


def fit():
    print("# FIT movers (utf8 prp-l, prp-notl) and START-LANDING on utf8: 7388f1c0 (w3) -> b8337c33 (w3)")
    for sb in ("utf8",):
        for cfg in ("caps", "nocaps"):
            for m in movers_rows(sb, cfg):
                if m["pat"] in ("prp-l", "prp-notl") or m["ma"].get("engine_sel") != m["mb"].get("engine_sel"):
                    a, b = m["a"], m["b"]
                    print("%s %s %-14s %-24s %-14s A %s B %s | sel %s>%s emit %s>%s start %s>%s" % (
                        sb, cfg, m["pat"], m["reg"], m["form"],
                        ("%.1f" % a.median_ns) if a.median_ns else "-", ("%.1f" % b.median_ns) if b.median_ns else "-",
                        m["ma"].get("engine_sel"), m["mb"].get("engine_sel"), m["ma"].get("emit_bytes"), m["mb"].get("emit_bytes"),
                        m["ma"].get("dfa_start"), m["mb"].get("dfa_start")))


if __name__ == "__main__":
    mode = sys.argv[1]
    globals()[mode]()
