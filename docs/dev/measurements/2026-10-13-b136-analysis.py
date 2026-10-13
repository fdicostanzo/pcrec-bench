#!/usr/bin/env python3
"""[B136] window read (lane b136read): 2026-10-12 11:08 EDT -> 2026-10-13 07:56 EDT.
Source: store/records/<set>@<ver>/<testee>/*.jsonl -- THIS window = records stamped
>= 20261012T000000Z. Pins: BASE b8337c33 (abi 74), NEW 00c97769 (abi 75,
[REQ-HANDOFF-L1]), DENY = NEW with -fno-req-handoff, CANON 6b2dbd3e (abi 76, seam
helpers static inline). Earlier records of the same testee ids (the 2026-10-11
state-3 window for b8337c33, September for the peers) are the CROSS-WINDOW side.
Arithmetic: pcrecbench.reduce (reduce_match_cell: one subject's median/min/max over
trials; reduce_set_cell: per-trial sum over subjects, then median/min/max) -- the
reporter's own. "ov" = the two [min,max] trial ranges overlap, "DISJ" = they do not.
Nothing here times anything: it reads committed records and (landmark mode)
the generated subject trees read-only.
Run from the repo root:
    python3 docs/dev/measurements/2026-10-13-b136-analysis.py MODE
MODE: sentinel | control | table | smoke | movers | landmark | kv | litrun | seam
      | tail | grok | medians | peers | gap30 | split | jitrow
"""
import glob, json, os, re, statistics, sys
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
from pcrecbench import reduce as R

STORE = os.environ.get("STORE", "store")
MAIN = os.environ.get("MAINTREE", "/home/duxevents/pcrec-bench")
SETS = {"capability": "0.2", "loglines": "0.1", "email-specimen": "0.2", "litrun": "0.1",
        "utf8": "0.1", "syntax": "0.1", "bounded": "0.3", "altwide": "0.3", "sentinel": "0.1"}
WIN = "20261012T000000Z"
B, N, C = "b8337c33", "00c97769", "6b2dbd3e"
TP, SS = "large-subject-throughput", "short-subject-search"
JIT, INT = "libpcre2_10.46_jit-caps-simdna", "libpcre2_10.46_interp-caps-simdna"
_cache = {}


def tid(pin, cfg, sb, extra=""):
    u = "_utf8" if sb == "utf8" else ""
    if extra and sb == "utf8":
        return "pcrec_%s_auto-%s-simdna_%s-utf8" % (pin, cfg, extra)
    return "pcrec_%s_auto-%s-simdna%s%s" % (pin, cfg, ("_" + extra) if extra else "", u)


def peer(sb, base):
    return base + ("_utf8" if sb == "utf8" else "")


def files(sb, testee):
    return sorted(glob.glob("%s/records/%s@%s/%s/*.jsonl" % (STORE, sb, SETS[sb], testee)))


def fts(f):
    return os.path.basename(f).rsplit("__", 1)[1].split(".")[0]


def load(f):
    if f in _cache:
        return _cache[f]
    setup, rows = R.read_record(f)
    comp = {}
    for r in rows:
        if r.get("kind") == "compile":
            comp[(r["pattern_id"], r.get("form", "plain"))] = r
    out = (setup, R.cells_from_record(rows), comp, fts(f))
    _cache[f] = out
    return out


def win(sb, testee):
    fs = [f for f in files(sb, testee) if fts(f) >= WIN]
    return load(fs[-1]) if fs else None


def old(sb, testee, before=WIN):
    fs = [f for f in files(sb, testee) if fts(f) < before]
    return load(fs[-1]) if fs else None


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


def sc(cells, key):
    return R.reduce_set_cell(cells[key]) if key in cells else None


def fm(c):
    if c is None or c.median_ns is None:
        return "-"
    return "%.1f[%.1f..%.1f]" % (c.median_ns, c.min_ns, c.max_ns)


def ratio(a, b):
    if a is None or b is None or a.median_ns is None or b.median_ns is None:
        return None
    return b.median_ns / a.median_ns


def rs(r):
    return "-" if r is None else "%.3f" % r


def quad(sb):
    ts = [("B", tid(B, "caps", sb)), ("N", tid(N, "caps", sb)), ("D", tid(N, "caps", sb, "noreqhandoff")), ("C", tid(C, "caps", sb))]
    return {k: win(sb, t) for k, t in ts}


# --------------------------------------------------------------------------- sentinel
def sentinel():
    def slot(ts):
        if ts < "20261012T180000Z":
            return "open"
        if ts < "20261013T000000Z":
            return "end1"
        if ts < "20261013T040000Z":
            return "end2"
        return "end3"
    testees = sorted(os.path.basename(d) for d in glob.glob("%s/records/sentinel@0.1/*" % STORE))
    cells, stamps = {}, {}
    for t in testees:
        for f in files("sentinel", t):
            ts = fts(f)
            if ts < WIN:
                continue
            s = slot(ts)
            stamps[(t, s)] = ts
            for key, subs in load(f)[1].items():
                if key[2] == "plain":
                    cells[(t, key[0], s)] = R.reduce_set_cell(subs)
    print("# sentinel@0.1 (15 patterns x 75 short subjects, set-grain sums, 5 trials), THIS window; record timestamps (UTC):")
    for (t, s), ts in sorted(stamps.items()):
        print("#   %-36s %-5s %s" % (t, s, ts))
    pairs = (("end1", "open"), ("end2", "open"), ("end3", "open"), ("end2", "end1"), ("end3", "end2"))
    print("\n# per testee: ratio later/earlier over the 15 pattern cells (min / median / max, disjoint-range count)")
    for t in testees:
        for a, b in pairs:
            r, dj = [], 0
            for p in sorted({k[1] for k in cells if k[0] == t}):
                A, Bc = cells.get((t, p, a)), cells.get((t, p, b))
                if A and Bc and A.median_ns and Bc.median_ns:
                    r.append(A.median_ns / Bc.median_ns)
                    dj += not ov(A, Bc)
            if r:
                print("%-36s %-5s/%-5s n=%2d min %.3f median %.3f max %.3f DISJ %d" % (t, a, b, len(r), min(r), statistics.median(r), max(r), dj))
    print("\n# pcrec pins against each other in the SAME slot (program-identical patterns on the sentinel set): ratio over 15 cells")
    pins = [tid(B, "caps", "sentinel"), tid(N, "caps", "sentinel"), tid(C, "caps", "sentinel")]
    for s in ("open", "end1", "end2", "end3"):
        for x, y in ((1, 0), (2, 0), (2, 1)):
            r, dj = [], 0
            for p in sorted({k[1] for k in cells if k[0] == pins[0]}):
                A, Bc = cells.get((pins[x], p, s)), cells.get((pins[y], p, s))
                if A and Bc and A.median_ns and Bc.median_ns:
                    r.append(A.median_ns / Bc.median_ns)
                    dj += not ov(A, Bc)
            print("%-5s %s / %s n=%2d min %.3f median %.3f max %.3f DISJ %d" % (s, pins[x][6:14], pins[y][6:14], len(r), min(r), statistics.median(r), max(r), dj))
    print("\n# per cell: median ns [min..max] open | end1 | end2 | end3 for caps 6b2dbd3e, nocaps 6b2dbd3e, jit")
    for t in (tid(C, "caps", "sentinel"), tid(C, "nocaps", "sentinel"), JIT):
        for p in sorted({k[1] for k in cells if k[0] == t}):
            c = [cells.get((t, p, s)) for s in ("open", "end1", "end2", "end3")]
            if all(c):
                print("%-34s %-30s %s | end3/open %.3f %s" % (t, p, " | ".join(fm(x) for x in c), c[3].median_ns / c[0].median_ns, "ov" if ov(c[3], c[0]) else "DISJ"))


def jitrow():
    print("# ask 7.4: the sentinel@0.1 pcre2-jit row, EVERY record in the store (sorted by time); 15 plain pattern cells, set-grain sum ns")
    fs = files("sentinel", JIT)
    cells0 = None
    for f in fs:
        setup, cells, comp, ts = load(f)
        cc = {k[0]: R.reduce_set_cell(v) for k, v in cells.items() if k[2] == "plain"}
        if cells0 is None:
            cells0 = cc
        r, dj = [], 0
        for p in sorted(cc):
            if p in cells0 and cc[p].median_ns and cells0[p].median_ns:
                r.append(cc[p].median_ns / cells0[p].median_ns)
                dj += not ov(cc[p], cells0[p])
        tot = sum(c.median_ns for c in cc.values() if c.median_ns)
        print("%s n=%2d vs-first min %.3f median %.3f max %.3f DISJ %2d | sum of 15 medians %.1f ns" % (ts, len(r), min(r), statistics.median(r), max(r), dj, tot))
    print("\n# same, adjacent pairs")
    prev = None
    for f in fs:
        setup, cells, comp, ts = load(f)
        cc = {k[0]: R.reduce_set_cell(v) for k, v in cells.items() if k[2] == "plain"}
        if prev:
            r = [cc[p].median_ns / prev[1][p].median_ns for p in cc if p in prev[1] and cc[p].median_ns and prev[1][p].median_ns]
            print("%s / %s median %.3f (min %.3f max %.3f)" % (ts, prev[0], statistics.median(r), min(r), max(r)))
        prev = (ts, cc)


# --------------------------------------------------------------------------- control
def control():
    print("# CROSS-WINDOW CONTROL: pcrec b8337c33 caps, THIS window (B) vs the 2026-10-11 state-3 window (A), same testee id")
    allr = []
    for sb in ("loglines", "altwide", "bounded", "syntax", "utf8", "capability"):
        t = tid(B, "caps", sb)
        Bw, Ao = win(sb, t), old(sb, t)
        if not Bw or not Ao:
            print("%-12s missing (%s %s)" % (sb, bool(Bw), bool(Ao)))
            continue
        r, dj = [], 0
        out = []
        for key in sorted(set(Bw[1]) & set(Ao[1]), key=lambda k: tuple(map(str, k))):
            a, b = R.reduce_set_cell(Ao[1][key]), R.reduce_set_cell(Bw[1][key])
            if a.median_ns and b.median_ns:
                r.append(b.median_ns / a.median_ns)
                dj += not ov(a, b)
                out.append((b.median_ns / a.median_ns, key, a, b))
        allr += r
        print("%-12s A %s B %s | %s | DISJ %d | >5%% %d | >10%% %d" % (sb, Ao[3], Bw[3], dist(r), dj, sum(abs(x - 1) > .05 for x in r), sum(abs(x - 1) > .10 for x in r)))
        for rr, key, a, b in sorted(out, key=lambda x: -abs(x[0] - 1))[:4]:
            print("      worst %.3f %s A %s B %s %s" % (rr, key, fm(a), fm(b), "ov" if ov(a, b) else "DISJ"))
    print("ALL: %s" % dist(allr))


# --------------------------------------------------------------------------- table (a)
PRED = {  # (set, pattern, regime): (new/base, deny/base)
    ("loglines", "ipv6", TP): (0.305, 1.000), ("loglines", "ipv6", SS): (0.325, None),
    ("loglines", "ipv4", TP): (0.196, 0.996), ("loglines", "ipv4", SS): (0.315, None),
    ("altwide", "sfx-64", TP): (0.068, 1.166),
    ("loglines", "kv-quoted", TP): (1.007, 13.78),
    ("bounded", "dotted4", TP): (1.003, 1.000), ("bounded", "dotted4", SS): (0.841, None),
}


def table():
    print("# I-147 section 2: BASE b8337c33 | NEW 00c97769 | DENY (-fno-req-handoff @00c97769) | CANON 6b2dbd3e, set-cell medians ns [min..max], this window, caps")
    print("set | pattern | regime | BASE | NEW | DENY | CANON | NEW/BASE | DENY/BASE | CANON/NEW | pcrec predicted NEW/BASE, DENY/BASE | NEW/BASE ov | stamps (BASE>NEW prefilter, K)")
    cells = [("loglines", "ipv6"), ("loglines", "ipv4"), ("loglines", "kv-quoted"), ("bounded", "dotted4"),
             ("altwide", "sfx-64"), ("altwide", "sfx-256"), ("altwide", "sfx-512")]
    for sb, pat in cells:
        q = quad(sb)
        for reg in (TP, SS):
            key = (pat, reg, "plain")
            c = {k: (sc(v[1], key) if v else None) for k, v in q.items()}
            pr = PRED.get((sb, pat, reg))
            mb, mn = md(q["B"][2], (pat, "plain")), md(q["N"][2], (pat, "plain"))
            print("%s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s>%s K %s>%s" % (
                sb, pat, "throughput" if reg == TP else "search_short", fm(c["B"]), fm(c["N"]), fm(c["D"]), fm(c["C"]),
                rs(ratio(c["B"], c["N"])), rs(ratio(c["B"], c["D"])), rs(ratio(c["N"], c["C"])),
                ("%s, %s" % pr) if pr else "-",
                ("ov" if c["B"] and c["N"] and ov(c["B"], c["N"]) else "DISJ"),
                mb.get("dfa_prefilter"), mn.get("dfa_prefilter"), mb.get("req_handoff"), mn.get("req_handoff")))
    print("\n# the hostile `a.{1,50000}z` row of I-147's table: where is it in the bench?")
    for sb in ("bounded", "syntax", "loglines", "altwide"):
        for fn in glob.glob("%s/bench/%s/patterns/*" % (MAIN, sb)):
            try:
                txt = open(fn, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            if "50000" in txt:
                print("  ", fn.replace(MAIN + "/", ""), repr(txt[:80]))


# --------------------------------------------------------------------------- smoke
def smoke():
    print("# I-147 ask 1 smoke: every cell of every pattern whose NEW compile row carries REQ_HANDOFF != none, NEW vs BASE (this window, caps)")
    print("# flag: NEW/BASE > 1.03 ('slow3'), and whether the trial ranges are disjoint")
    tot = 0
    flagged = []
    wrong = []
    for sb in ("loglines", "altwide", "bounded", "syntax", "utf8", "capability"):
        q = quad(sb)
        if not q["B"] or not q["N"]:
            continue
        for k, v in q.items():
            if not v:
                continue
            for key, subs in v[1].items():
                c = R.reduce_set_cell(subs)
                if (c.pass_rate is not None and c.pass_rate < 1) or c.median_ns is None:
                    wrong.append((sb, k, key, c.pass_rate, getattr(c, "failing_subjects", None)))
        for (pat, form), row in sorted(q["N"][2].items()):
            m = row.get("engine_metadata", {})
            kk = m.get("req_handoff")
            if kk in (None, "none"):
                continue
            for reg in (TP, SS):
                key = (pat, reg, form)
                b, n = sc(q["B"][1], key), sc(q["N"][1], key)
                if not b or not n or not b.median_ns or not n.median_ns:
                    continue
                tot += 1
                r = n.median_ns / b.median_ns
                d = sc(q["D"][1], key) if q["D"] else None
                row_ = (sb, pat, form, reg, kk, m.get("dfa_prefilter"), md(q["B"][2], (pat, form)).get("dfa_prefilter"),
                        b, n, d, r, not ov(b, n), sc(q["C"][1], key) if q["C"] else None)
                print("%s | %s | %s | %s | K %s | prefilter %s>%s | BASE %s | NEW %s | NEW/BASE %.3f %s | DENY/BASE %s | CANON/NEW %s" % (
                    sb, pat, form, "tp" if reg == TP else "ss", kk, row_[6], row_[5], fm(b), fm(n), r, "DISJ" if row_[11] else "ov",
                    rs(ratio(b, d)), rs(ratio(n, row_[12]))))
                if r > 1.03:
                    flagged.append(row_)
    print("\n# %d cells read (REQ_HANDOFF set at NEW); NEW/BASE > 1.03: %d" % (tot, len(flagged)))
    for f in flagged:
        print("  SLOW3 %s %s %s %s K %s NEW/BASE %.3f %s" % (f[0], f[1], f[2], f[3], f[4], f[10], "DISJ" if f[11] else "ov"))
    print("\n# cells with a failing subject / pass_rate < 1 / no number, in any of the B N D C records of the six sets: %d" % len(wrong))
    for w in wrong[:40]:
        print("  ", w)
    print("\n# K105 caveat: patterns shaped `[a-y]\\d{0,N}:` (hcolon) in the six sets")
    for sb in ("loglines", "altwide", "bounded", "syntax", "utf8", "capability"):
        for fn in glob.glob("%s/bench/%s/patterns/*" % (MAIN, sb)):
            try:
                txt = open(fn, encoding="utf-8", errors="replace").read().strip()
            except Exception:
                continue
            if re.search(r"\[a-y\].*\\d\{0,\d+\}:", txt):
                print("  ", fn.replace(MAIN + "/", ""), repr(txt[:80]))


# --------------------------------------------------------------------------- movers
def movers():
    print("# the `handoff` movers BY VALUE from the records: a compile row whose dfa_prefilter is `handoff`, with BASE / NEW / DENY / CANON values")
    n_plain = {}
    for sb in ("loglines", "altwide", "bounded", "syntax", "utf8", "capability", "litrun"):
        q = quad(sb)
        if sb == "litrun":
            q = {"B": None, "N": None, "D": None, "C": win(sb, tid(C, "caps", sb))}
        for form in ("plain", "whole-subject"):
            keys = set()
            for k, v in q.items():
                if v:
                    keys |= {pat for (pat, f) in v[2] if f == form}
            for pat in sorted(keys):
                vals = {k: md(v[2], (pat, form)) if v else {} for k, v in q.items()}
                hit = [k for k in "BNDC" if vals[k].get("dfa_prefilter") == "handoff"]
                kset = vals["N"].get("req_handoff") not in (None, "none") and vals["B"].get("req_handoff") in (None, "none")
                if hit or (form == "plain" and kset):
                    print("%s | %s | %s | prefilter B=%s N=%s D=%s C=%s | K B=%s N=%s D=%s C=%s | engine N=%s | handoff in %s" % (
                        sb, pat, form, *(vals[k].get("dfa_prefilter") for k in "BNDC"), *(vals[k].get("req_handoff") for k in "BNDC"),
                        vals["N"].get("engine") or vals["C"].get("engine"), "".join(hit)))
                    if ("N" in hit or (sb == "litrun" and "C" in hit)) and form == "plain":
                        n_plain.setdefault(sb, []).append(pat)
    print("\n# plain-form patterns with dfa_prefilter=handoff at NEW, by set:")
    tot = 0
    for sb, v in sorted(n_plain.items()):
        print("  %-10s %d %s" % (sb, len(v), ", ".join(v)))
        tot += len(v)
    print("  TOTAL %d (I-147 lists 14 under caps; the 15th, capability wild-secrets-username-password-pair, is a nocaps-only mover, and the window ran no capability nocaps record)" % tot)
    print("\n# whole-subject form: any handoff row at NEW?")
    wsum = 0
    for sb in ("loglines", "altwide", "bounded", "syntax", "utf8", "capability"):
        q = quad(sb)
        if q["N"]:
            wsum += sum(1 for (p, f), r in q["N"][2].items() if f != "plain" and r.get("engine_metadata", {}).get("dfa_prefilter") == "handoff")
    print("  whole-subject handoff rows at NEW across the six sets:", wsum)
    print("\n# patterns that gained a K (req_handoff none>value) but kept their prefilter (BASE>NEW):")
    for sb in ("loglines", "altwide", "bounded", "syntax", "utf8", "capability"):
        q = quad(sb)
        if not q["B"] or not q["N"]:
            continue
        for (pat, form), row in sorted(q["N"][2].items()):
            mb, mn = md(q["B"][2], (pat, form)), row.get("engine_metadata", {})
            if mb.get("req_handoff") in (None, "none") and mn.get("req_handoff") not in (None, "none") and mn.get("dfa_prefilter") != "handoff":
                print("  %s %s %s K %s prefilter %s>%s engine %s" % (sb, pat, form, mn.get("req_handoff"), mb.get("dfa_prefilter"), mn.get("dfa_prefilter"), mn.get("engine")))


# --------------------------------------------------------------------------- landmark (c)
def prior():
    p = {}
    f = os.path.join(MAIN, "build/pcrec-%s/src/findings/default.rxt" % C)
    for ln in open(f):
        m = re.match(r"\s+row ([0-9a-f]{2}) (\d+)\s*$", ln)
        if m:
            p[int(m.group(1), 16)] = int(m.group(2))
    assert len(p) == 256 and abs(sum(p.values()) - 1000000) < 5, (len(p), sum(p.values()))
    return p


def subject_path(sb, sid, tp):
    base = os.path.join(MAIN, "bench", sb)
    for d in (("throughput" if tp else "subjects"), ("subjects" if tp else "throughput")):
        for ext in (".bin", ""):
            p = os.path.join(base, d, sid + ext)
            if os.path.exists(p):
                return p
    return None


def landmark():
    pri = prior()
    print("# ask 2: landmark byte density of each mover's subjects vs the default prior (default.rxt of 6b2dbd3e, ppm summing to 1e6)")
    print("# landmark = REQ_BYTE (or REQ_RUN's window product); observed density = count/len per subject; dense = observed > prior")
    print("# 'cost bound' = x1.5 (I-147 ask 2) only when an ADMITTED re-entry meets denser text than the prior; this reads the text only")
    movers_ = {"loglines": ["ipv6", "ipv4", "kv-quoted"], "bounded": ["dotted4"], "altwide": ["sfx-64", "sfx-256", "sfx-512"],
               "syntax": ["cls-fold-pair", "cls-pair-ctl", "mod-i", "mod-r", "qnt-poss-brace", "grp-atomic-alt"],
               "utf8": ["ci-ascii-control", "ci-strasse", "cls-s-ucp"]}
    for sb, pats in movers_.items():
        q = quad(sb)
        N_ = q["N"]
        man = {}
        for fn, tp in (("manifest.tsv", False), ("manifest_throughput.tsv", True)):
            for ln in open(os.path.join(MAIN, "bench", sb, fn)).read().splitlines()[1:]:
                a = ln.split("\t")
                man[a[0]] = (tp, int(a[1]))
        data = {}
        for sid, (tp, ln) in man.items():
            pth = subject_path(sb, sid, tp)
            if pth:
                data[sid] = open(pth, "rb").read()
        for pat in pats:
            m = md(N_[2], (pat, "plain"))
            rb, rr = m.get("req_byte"), m.get("req_run")
            kk = m.get("req_handoff")
            if rr and rr != "none":
                hx, rest = rr.split("@")
                at = rest.split("/")[0]
                mk = bytes.fromhex(rest.split("/")[1]) if "/" in rest else b"\xff" * (len(hx) // 2)
                run = bytes.fromhex(hx)
                lab = "run %r@%s mask %s" % (run, at, mk.hex())
                h_prior = 1.0
                for b, m in zip(run, mk):
                    h_prior *= sum(pri[x] for x in range(256) if x & m == b) / 1e6
                rx = re.compile(b"".join(b"(?:" + b"|".join(re.escape(bytes([x])) for x in range(256) if x & m == bb) + b")"
                                         for bb, m in zip(run, mk)))
            elif rb and rb != "none":
                run = bytes([int(rb)])
                lab = "byte %d (%r)" % (int(rb), run)
                h_prior = pri[int(rb)] / 1e6
                rx = re.compile(re.escape(run))
            else:
                print("%s/%s: no byte or run landmark stamped (req_byte=%s req_run=%s)" % (sb, pat, rb, rr))
                continue
            dens = []
            for sid, d in data.items():
                if not d:
                    continue
                cnt = len(rx.findall(d)) if len(run) == 1 else sum(1 for _ in rx.finditer(d))
                dens.append((cnt * len(run) / len(d), sid, len(d), cnt))
            denser = [x for x in dens if x[0] > h_prior]
            print("\n%s/%s K=%s landmark %s prior hit rate %.5f (1/h = %.0f B between hits) | subjects %d, denser than prior: %d" % (
                sb, pat, kk, lab, h_prior, 1 / h_prior if h_prior else float("inf"), len(dens), len(denser)))
            for x in sorted(dens, reverse=True)[:5]:
                tp, ln = man[x[1]]
                key = (pat, TP if tp else SS, "plain")
                g = lambda k: (R.reduce_match_cell(q[k][1][key][x[1]]) if q[k] and x[1] in q[k][1].get(key, {}) else None)
                mb_, mn_, md_ = g("B"), g("N"), g("D")
                print("   densest: %-14s len %7d count %6d density %.5f (x%.2f prior) | NEW/BASE %s DENY/BASE %s" % (
                    x[1], x[2], x[3], x[0], x[0] / h_prior if h_prior else 0, rs(ratio(mb_, mn_)), rs(ratio(mb_, md_))))
            rows = []
            for sid, (tp, ln) in man.items():
                key = (pat, TP if tp else SS, "plain")
                rb_, rn_ = q["B"][1].get(key, {}).get(sid), q["N"][1].get(key, {}).get(sid)
                if rb_ and rn_:
                    a, b = R.reduce_match_cell(rb_), R.reduce_match_cell(rn_)
                    if a.median_ns and b.median_ns:
                        dd = next((x for x in dens if x[1] == sid), None)
                        rows.append((b.median_ns / a.median_ns, sid, tp, a, b, dd))
            rows.sort(reverse=True)
            for r, sid, tp, a, b, dd in rows[:3]:
                print("   slowest NEW/BASE: %-14s %.3f (BASE %s NEW %s) %s density %s" % (sid, r, fm(a), fm(b), "ov" if ov(a, b) else "DISJ", ("%.5f x%.2f" % (dd[0], dd[0] / h_prior)) if dd else "-"))


# --------------------------------------------------------------------------- kv-quoted (d)
def kv():
    print("# ask 3: loglines/kv-quoted (K=32 run handoff) -- the standing candidate for a gap to reverse-inner (rlhtwin Q3: rev-inner twin x0.913, NEW twin x1.013)")
    q = quad("loglines")
    for reg in (TP, SS):
        key = ("kv-quoted", reg, "plain")
        c = {k: sc(v[1], key) for k, v in q.items()}
        print("%s: BASE %s NEW %s DENY %s CANON %s | NEW/BASE %s DENY/BASE %s CANON/NEW %s (NEW/BASE %s)" % (
            reg, fm(c["B"]), fm(c["N"]), fm(c["D"]), fm(c["C"]), rs(ratio(c["B"], c["N"])), rs(ratio(c["B"], c["D"])), rs(ratio(c["N"], c["C"])),
            "ov" if ov(c["B"], c["N"]) else "DISJ"))
        for lab, t in (("pcre2-jit (this window)", JIT), ("pcre2-interp (this window)", INT), ("rust (2026-09)", "rust_1.13.1_default-caps-simdna")):
            r = win("loglines", t) or old("loglines", t)
            if r:
                cc = sc(r[1], key)
                print("   %-26s %s [%s] pcrec NEW/peer %s" % (lab, fm(cc), r[3], rs(ratio(cc, c["N"]))))
    print("\n# per-subject NEW vs BASE and vs rust on kv-quoted throughput")
    rr = old("loglines", "rust_1.13.1_default-caps-simdna")
    key = ("kv-quoted", TP, "plain")
    for sid in sorted(q["B"][1][key]):
        a = R.reduce_match_cell(q["B"][1][key][sid])
        b = R.reduce_match_cell(q["N"][1][key][sid])
        rst = R.reduce_match_cell(rr[1][key][sid]) if rr and sid in rr[1].get(key, {}) else None
        print("  %-14s BASE %s NEW %s NEW/BASE %s | rust %s NEW/rust %s" % (sid, fm(a), fm(b), rs(ratio(a, b)), fm(rst), rs(ratio(rst, b)) if rst else "-"))
    print("\n# NOT measured: a reverse-inner start exists in no pcrec build and no bench testee; its -8.7% is et1twin's SCRATCH figure (rlhtwin_report.md).")


# --------------------------------------------------------------------------- litrun (e)
def litrun():
    print("# ask 4: litrun@0.1 same-pin (6b2dbd3e) rev-end vs -fno-rev-end, caps and nocaps; set-grain, this window")
    print("# cell = per-trial SUM over the regime's subjects of per-subject ns/call (NOT one call); rev-end/norevend < 1 = rev-end faster")
    for cfg in ("caps", "nocaps"):
        a = win("litrun", tid(C, cfg, "litrun"))
        b = win("litrun", tid(C, cfg, "litrun", "norevend"))
        print("\n## %s: rev-end record %s, -fno-rev-end record %s" % (cfg, a[3], b[3]))
        pats = sorted({k[0] for k in a[1]})
        allr = {}
        regs = sorted({k[1] for k in a[1]})
        for pat in pats:
            for reg in regs:
                for form in ("plain", "whole-subject"):
                    key = (pat, reg, form)
                    x, y = sc(a[1], key), sc(b[1], key)
                    if not x or not y or not x.median_ns or not y.median_ns:
                        continue
                    r = x.median_ns / y.median_ns
                    allr.setdefault((reg, form), []).append(r)
                    ma, mb = md(a[2], (pat, form)), md(b[2], (pat, form))
                    print("%-22s %-26s %-14s revend %s norevend %s | revend/norevend %.3f %s | dfa_scan %s>%s start %s>%s" % (
                        pat, reg, form, fm(x), fm(y), r, "ov" if ov(x, y) else "DISJ", mb.get("dfa_scan"), ma.get("dfa_scan"), mb.get("dfa_start"), ma.get("dfa_start")))
        for k, v in sorted(allr.items()):
            print("-- %s %s %s: %s" % (cfg, k[0], k[1], dist(v)))


# --------------------------------------------------------------------------- seam (f)
def seam():
    print("# I-148 section 1 (seam helpers static inline): CANON 6b2dbd3e vs NEW 00c97769, set-grain medians, this window, caps")
    seam18 = {"syntax": ["bak-1", "bak-2", "bak-g-rel", "bak-k-named", "bak-py", "mod-j-uc", "lkb-pos", "lkb-neg"],
              "utf8": ["asr-lb-fixed", "asr-lb-varwidth", "asr-lb-neg", "asr-lb-class"],
              "capability": ["wild-doubled-word", "doubled-word", "dup-param-detect", "phone-palindrome-6", "quoted-delim-match", "tag-pair-match", "tag-depth3-bound"]}
    print("# predicted faster-by: bak-1 +13.5%, bak-2 +9.7%, mod-j-uc +5.6% (i.e. CANON/NEW about 0.88, 0.91, 0.95)")
    for sb, pats in seam18.items():
        q = quad(sb)
        for pat in pats:
            for reg in (SS, TP):
                key = (pat, reg, "plain")
                n, c = sc(q["N"][1], key), sc(q["C"][1], key)
                b = sc(q["B"][1], key)
                if n is None and c is None:
                    continue
                mn, mc = md(q["N"][2], (pat, "plain")), md(q["C"][2], (pat, "plain"))
                print("%s | %s | %s | NEW %s CANON %s | CANON/NEW %s %s | NEW/BASE %s | program same=%s emit %s>%s vm_prog %s>%s" % (
                    sb, pat, reg, fm(n), fm(c), rs(ratio(n, c)), ("ov" if n and c and ov(n, c) else "DISJ"), rs(ratio(b, n)),
                    mn.get("program_sha256") == mc.get("program_sha256"), mn.get("emit_bytes"), mc.get("emit_bytes"),
                    mn.get("vm_program_bytes"), mc.get("vm_program_bytes")))
    print("\n# which patterns changed program between NEW and CANON (program_sha256), by set, and their CANON/NEW per regime")
    for sb in ("loglines", "altwide", "bounded", "syntax", "utf8", "capability"):
        q = quad(sb)
        if not q["N"] or not q["C"]:
            continue
        chg = sorted({p for (p, f), r in q["N"][2].items() if f == "plain" and (p, f) in q["C"][2]
                      and md(q["N"][2], (p, f)).get("program_sha256") != md(q["C"][2], (p, f)).get("program_sha256")})
        print("%-12s program-changed plain patterns: %d %s" % (sb, len(chg), chg))
    print("\n# the null: CANON vs NEW on program-IDENTICAL cells per set -- ratio distribution, DISJ count")
    for sb in ("loglines", "altwide", "syntax", "utf8", "capability"):
        q = quad(sb)
        if not q["N"] or not q["C"]:
            continue
        r, dj, rr_ = [], 0, []
        for key in sorted(set(q["N"][1]) & set(q["C"][1]), key=lambda k: tuple(map(str, k))):
            pat, reg, form = key
            n, c = sc(q["N"][1], key), sc(q["C"][1], key)
            if not n or not c or not n.median_ns or not c.median_ns:
                continue
            if md(q["N"][2], (pat, form)).get("program_sha256") == md(q["C"][2], (pat, form)).get("program_sha256"):
                r.append(c.median_ns / n.median_ns)
                dj += not ov(n, c)
                rr_.append((abs(c.median_ns / n.median_ns - 1), key, n, c))
        print("%-12s program-identical cells: %s | DISJ %d | outside +-5%%: %d" % (sb, dist(r), dj, sum(abs(x - 1) > .05 for x in r)))
        for d, key, n, c in sorted(rr_, reverse=True)[:3]:
            print("      %s NEW %s CANON %s" % (key, fm(n), fm(c)))
    print("\n# the changed cells, CANON/NEW distribution (all 'program-changed' cells together, per set)")
    for sb in ("syntax", "utf8", "capability"):
        q = quad(sb)
        r = []
        for key in sorted(set(q["N"][1]) & set(q["C"][1]), key=lambda k: tuple(map(str, k))):
            pat, reg, form = key
            n, c = sc(q["N"][1], key), sc(q["C"][1], key)
            if n and c and n.median_ns and c.median_ns and md(q["N"][2], (pat, form)).get("program_sha256") != md(q["C"][2], (pat, form)).get("program_sha256"):
                r.append(c.median_ns / n.median_ns)
        print("%-12s %s" % (sb, dist(r)))


# --------------------------------------------------------------------------- tail / grok (g)
TAILS = ("tail-digits-eol", "tail-word-eoz", "tail-space-eol", "tail-ext-lower-txt", "tail-dotstar-txt", "letters-bounded-tail-z")


def tail():
    print("# (g) tail family, capability@0.2 caps, this window: BASE | NEW | CANON; none should move (I-147 ask 4)")
    q = {k: win("capability", tid(p, "caps", "capability")) for k, p in (("B", B), ("N", N), ("C", C))}
    for reg in (TP, SS, "match-compliance"):
        for pat in TAILS:
            for form in ("plain", "whole-subject"):
                key = (pat, reg, form)
                c = {k: sc(v[1], key) for k, v in q.items()}
                if not c["B"]:
                    continue
                print("%-24s %-26s %-14s B %s N %s C %s | N/B %s %s | C/N %s %s | C/B %s" % (
                    pat, reg, form, fm(c["B"]), fm(c["N"]), fm(c["C"]), rs(ratio(c["B"], c["N"])), "ov" if ov(c["B"], c["N"]) else "DISJ",
                    rs(ratio(c["N"], c["C"])), "ov" if ov(c["N"], c["C"]) else "DISJ", rs(ratio(c["B"], c["C"]))))
    print("\n# per-subject large-subject-throughput, tail family: DISJ count and ratio distribution")
    for lab, x, y in (("N/B", "B", "N"), ("C/N", "N", "C"), ("C/B", "B", "C")):
        r, dj, n = [], 0, 0
        for pat in TAILS:
            key = (pat, TP, "plain")
            for sid in sorted(q["B"][1].get(key, {})):
                a = R.reduce_match_cell(q[x][1][key][sid])
                b = R.reduce_match_cell(q[y][1][key][sid])
                if a.median_ns and b.median_ns:
                    n += 1
                    r.append(b.median_ns / a.median_ns)
                    dj += not ov(a, b)
        print("%s: %d cells, DISJ %d, %s" % (lab, n, dj, dist(r)))
    print("\n# the same, 10-11 b8337c33 record (state-3 window) vs this window's b8337c33: the instrument across a day")
    o = old("capability", tid(B, "caps", "capability"))
    r, dj = [], 0
    for pat in TAILS:
        key = (pat, TP, "plain")
        for sid in sorted(q["B"][1].get(key, {})):
            a = R.reduce_match_cell(o[1][key][sid])
            b = R.reduce_match_cell(q["B"][1][key][sid])
            if a.median_ns and b.median_ns:
                r.append(b.median_ns / a.median_ns)
                dj += not ov(a, b)
    print("this-window B / 10-11 B: %d cells, DISJ %d, %s" % (len(r), dj, dist(r)))
    print("\n# stamps and program identity across the three pins (tail, plain + whole)")
    for pat in TAILS:
        for form in ("plain", "whole-subject"):
            m = {k: md(v[2], (pat, form)) for k, v in q.items()}
            if m["B"]:
                print("%-24s %-14s prefilter %s/%s/%s start %s/%s/%s scan %s/%s/%s prog same B=N %s N=C %s" % (
                    pat, form, *(m[k].get("dfa_prefilter") for k in "BNC"), *(m[k].get("dfa_start") for k in "BNC"), *(m[k].get("dfa_scan") for k in "BNC"),
                    m["B"].get("program_sha256") == m["N"].get("program_sha256"), m["N"].get("program_sha256") == m["C"].get("program_sha256")))


def grok():
    pat = "wild-logparse-quotedstring-grok"
    print("# grok cross-window control: capability %s caps" % pat)
    slots = []
    for lab, p in (("b8337c33", B), ("00c97769", N), ("6b2dbd3e", C)):
        t = tid(p, "caps", "capability")
        o = old("capability", t)
        w = win("capability", t)
        if o:
            slots.append((lab + " 10-11", o))
        slots.append((lab + " 10-12", w))
    for reg in (SS, TP):
        print("\n## %s" % reg)
        key = (pat, reg, "plain")
        cs = []
        for lab, x in slots:
            c = sc(x[1], key)
            m = md(x[2], (pat, "plain"))
            cs.append((lab, c, x))
            print("%-16s %s  engine=%s emit=%s prog=%s" % (lab, fm(c), m.get("engine"), m.get("emit_bytes"), (m.get("program_sha256") or "")[:12]))
        for i in range(1, len(cs)):
            print("   %s / %s : %s %s" % (cs[i][0], cs[i - 1][0], rs(ratio(cs[i - 1][1], cs[i][1])), "ov" if ov(cs[i][1], cs[i - 1][1]) else "DISJ"))
    key = (pat, SS, "plain")
    ws = {lab: x for lab, x in slots}
    for a_, b_ in (("b8337c33 10-12", "00c97769 10-12"), ("00c97769 10-12", "6b2dbd3e 10-12"), ("b8337c33 10-11", "b8337c33 10-12")):
        if a_ in ws and b_ in ws:
            d = []
            for sid in sorted(ws[a_][1][key]):
                x, y = R.reduce_match_cell(ws[a_][1][key][sid]), R.reduce_match_cell(ws[b_][1][key][sid])
                if x.median_ns and y.median_ns:
                    d.append(y.median_ns - x.median_ns)
            print("per-subject delta ns (%s - %s): %s; slower on %d of %d" % (b_, a_, dist(d), sum(1 for z in d if z > 0), len(d)))


# --------------------------------------------------------------------------- medians (h)
def medians():
    print("# ask 5.2: loglines (all patterns) and altwide@0.3 medians at a post-START-LANDING pin: BASE b8337c33 | NEW 00c97769 | CANON 6b2dbd3e, caps, set-grain ns")
    for sb in ("loglines", "altwide"):
        q = quad(sb)
        print("\n## %s" % sb)
        keys = sorted(set(q["C"][1]), key=lambda k: tuple(map(str, k)))
        for key in keys:
            pat, reg, form = key
            if form != "plain":
                continue
            c = {k: sc(v[1], key) for k, v in q.items()}
            m = md(q["C"][2], (pat, form))
            print("%-26s %-26s B %s N %s C %s | C/B %s | n_subj %s | %s/%s/%s" % (
                pat, reg, fm(c["B"]), fm(c["N"]), fm(c["C"]), rs(ratio(c["B"], c["C"])), c["C"].n_subjects if c["C"] else "-",
                m.get("engine"), m.get("dfa_start"), m.get("dfa_prefilter")))
        for reg in (TP, SS):
            v = [sc(q["C"][1], k) for k in keys if k[1] == reg and k[2] == "plain"]
            v = [x.median_ns for x in v if x and x.median_ns]
            print("-- %s %s at CANON: n=%d median %.1f ns, min %.1f, max %.1f" % (sb, reg, len(v), statistics.median(v), min(v), max(v)))


# --------------------------------------------------------------------------- peers (i)
def peers():
    print("# ask 7.1: pcre2 jit/interp THIS window vs the previous (September) record of the same testee id; set-grain cells")
    allj, alli = [], []
    for sb in ("bounded", "loglines", "syntax", "utf8", "litrun", "email-specimen"):
        for lab, base in (("jit", JIT), ("interp", INT)):
            t = peer(sb, base)
            w, o = win(sb, t), old(sb, t)
            if not w or not o:
                print("%-14s %-6s missing %s %s" % (sb, lab, bool(w), bool(o)))
                continue
            r, dj = [], 0
            for key in sorted(set(w[1]) & set(o[1]), key=lambda k: tuple(map(str, k))):
                a, b = R.reduce_set_cell(o[1][key]), R.reduce_set_cell(w[1][key])
                if a.median_ns and b.median_ns:
                    r.append(b.median_ns / a.median_ns)
                    dj += not ov(a, b)
            (allj if lab == "jit" else alli).extend(r)
            print("%-14s %-6s old %s new %s | %s | DISJ %d | outside +-5%% %d, +-10%% %d" % (
                sb, lab, o[3], w[3], dist(r), dj, sum(abs(x - 1) > .05 for x in r), sum(abs(x - 1) > .10 for x in r)))
    print("ALL jit:    %s" % dist(allj))
    print("ALL interp: %s" % dist(alli))


def gap30():
    d = json.load(open(os.path.join(MAIN, "build/pcrec-%s/docs/dev/optloop/gapreport/run_2026-10-11/rank.json" % C)))
    cells = {}
    for g, v in d["groups"].items():
        for k in ("peer", "ceiling"):
            for c in v.get(k, []):
                cells[(c["set"], c["pattern"], c["regime"], c["form"], c["cmp"])] = c
    jit = [c for c in cells.values() if c["cmp"].startswith("libpcre2:jit")]
    tr = sorted([c for c in jit if 1 < c["ratio"] < 1.5], key=lambda c: (c["set"], c["pattern"], c["regime"]))
    print("# the gap report's %d sub-x1.5 trailing cells vs jit (rank.json of docs/dev/optloop/gapreport/run_2026-10-11): re-read with THIS window's jit" % len(tr))
    print("# old = gap report ratio (pcrec b8337c33 caps, 2026-10-11 window / jit September record); now = pcrec ns / this window's jit ns")
    print("# pcrec side = b8337c33 THIS window; litrun has no BASE in the window: 6b2dbd3e is used and marked")
    out = []
    for c in tr:
        sb = c["set"]
        reg = TP if c["regime"].startswith("large") else SS
        key = (c["pattern"], reg, c["form"])
        if sb in ("capability", "email-specimen"):
            out.append((c, None, None, None, "no new jit record (capability not in tier 4)"))
            continue
        jw = win(sb, peer(sb, JIT))
        pc = win(sb, tid(B, "caps", sb)) if sb != "litrun" else win(sb, tid(C, "caps", sb))
        if not jw or not pc:
            out.append((c, None, None, None, "missing"))
            continue
        j, p = sc(jw[1], key), sc(pc[1], key)
        if not j or not p or not j.median_ns or not p.median_ns:
            out.append((c, None, None, None, "no number"))
            continue
        out.append((c, p.median_ns / j.median_ns, j.median_ns / c["ns"], p.median_ns / c["auto_caps_ns"], "6b2dbd3e" if sb == "litrun" else "b8337c33"))
    for c, now, jd, pd, note in out:
        tag = "tp" if c["regime"].startswith("large") else "ss"
        if now is None:
            print("%-11s %-24s %-3s old x%.2f | now - (%s)" % (c["set"], c["pattern"], tag, c["ratio"], note))
        else:
            print("%-11s %-24s %-3s old x%.2f | now x%.2f | jit now/old %.3f | pcrec now/old %.3f | %s%s [%s]" % (
                c["set"], c["pattern"], tag, c["ratio"], now, jd, pd, "STILL TRAILS" if now > 1 else "FLIPPED to lead",
                " (>=1.5 now)" if now >= 1.5 else "", note))
    have = [o for o in out if o[1] is not None]
    print("\n# %d of 30 have a new jit number; %d without (capability: %d)" % (len(have), len(out) - len(have), sum(1 for o in out if o[0]["set"] == "capability")))
    print("# of the %d: still trail %d (of which >= x1.5: %d), flipped to lead %d" % (
        len(have), sum(1 for o in have if o[1] > 1), sum(1 for o in have if o[1] >= 1.5), sum(1 for o in have if o[1] <= 1)))
    print("# ratio moved by more than 10%% (|now/old - 1| > 0.10): %d; jit now/old: %s" % (
        sum(1 for o in have if abs(o[1] / o[0]["ratio"] - 1) > .10), dist([o[2] for o in have])))
    print("# pcrec-side now/old (the b8337c33 cross-window control on these cells): %s" % dist([o[3] for o in have]))


# --------------------------------------------------------------------------- split (j)
def split():
    print("# ask 7.2: per-subject split of capability@0.2 large-subject-throughput; newest records (pcrec 6b2dbd3e caps this window; jit/interp newest in the store)")
    jr = win("capability", JIT) or old("capability", JIT)
    pr = win("capability", tid(C, "caps", "capability"))
    ir = win("capability", INT) or old("capability", INT)
    print("# jit record %s, interp record %s, pcrec record %s" % (jr[3], ir[3] if ir else "-", pr[3]))
    man = {}
    for ln in open(os.path.join(MAIN, "bench/capability/manifest_throughput.tsv")).read().splitlines()[1:]:
        a = ln.split("\t")
        man[a[0]] = (int(a[1]), a[3][:70])
    for pat in ("wild-datetime-moment-iso8601", "wild-validator-email-owasp", "wild-waf-crs-942270-union-select"):
        key = (pat, TP, "plain")
        print("\n## %s" % pat)
        tj = tp_ = ti = 0
        for sid in sorted(pr[1][key]):
            p = R.reduce_match_cell(pr[1][key][sid])
            j = R.reduce_match_cell(jr[1][key][sid]) if sid in jr[1].get(key, {}) else None
            i = R.reduce_match_cell(ir[1][key][sid]) if ir and sid in ir[1].get(key, {}) else None
            tj += j.median_ns if j and j.median_ns else 0
            tp_ += p.median_ns if p.median_ns else 0
            ti += i.median_ns if i and i.median_ns else 0
            print("  %-26s len %8d | pcrec %s | jit %s | interp %s | pcrec-jit %s ns | pcrec/jit %s  %s" % (
                sid, man.get(sid, (0, ""))[0], fm(p), fm(j), fm(i),
                ("%.0f" % (p.median_ns - j.median_ns)) if j and j.median_ns and p.median_ns else "-",
                ("%.2f" % (p.median_ns / j.median_ns)) if j and j.median_ns and p.median_ns else "-", man.get(sid, (0, ""))[1]))
        print("  SUM pcrec %.0f jit %.0f interp %.0f ns -> pcrec/jit %.2f" % (tp_, tj, ti, tp_ / tj if tj else 0))


if __name__ == "__main__":
    globals()[sys.argv[1]]()
