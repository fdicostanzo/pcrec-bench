#!/usr/bin/env python3
# b139gaps / landings.py -- source header (for archiving under docs/dev/measurements/)
# Lane b139gaps (pcrec-bench, 2026-10-24), answering pcrec inbox I-156 (B4 landing gaps; pcrec
# docs/design/memfn/r17b_prime.md 9.2a via b4prep/expected_losses.md 4). READ-ONLY, NO TIMING, NO COUNTERS.
#
# Input : the emitted C of compile_all.py (pin 6b2dbd3e, abi 76, plain form, PLAIN = the form every
#         search_short / throughput cell runs), the bench subject trees (generated, gitignored).
# Method: per (config, set, pattern) read the artifact's own stamps and the SITE BYTE TABLE as emitted:
#           RX_DFA_PREFILTER byte-class / byte-class-bounded -> rx_can_begin_match[256]
#           RX_DFA_PREFILTER first-class-bounded (DFA or VM)  -> rx_start_bytes[256]
#           RX_VM_START_SCAN first-class                      -> rx_start_set[256]
#         Everything else (memchr, memchr-bounded, first-memchr-bounded, offset-set(-bounded) whose scanned
#         offset is a memchr, run-pinned, handoff, none) is a ONE-BYTE / non-set site (D1 family, not a B4
#         set-FIND mover) and is only counted, not computed.
#         Per cell (set, pattern, regime, subject): landings = every subject position whose byte the table
#         admits (whole subject, one pass); gaps = differences of consecutive landings; mean gap, dominant
#         gap value and its share of the gaps.
# Cover class (term count <= 2 or >= 3) is MY OWN search over RANGE/EQ/CUBE terms (the kit's cover search
# is not reproduced); it is a flag for the rule's condition 1, not the kit's number.
import os, re, sys, json, glob, collections
import numpy as np
sys.path.insert(0, "/home/pcrec/projects/pcrec-bench")
from pcrecbench import subbench
ROOT = "/home/pcrec/projects/pcrec-bench"
CDIR = "/var/tmp/pcrecbench/b139gaps/c"
OUT = "/var/tmp/pcrecbench/b139gaps"
SETS = ["altwide", "bounded", "capability", "email", "litrun", "loglines", "sentinel", "syntax", "utf8"]
CFGS = ["auto", "nocaps", "vm"]
SRC_REGIMES = ("search_short", "throughput")   # plain-form regimes; `match` = whole-subject form (no landing site)

def stamp(t, k):
    m = re.search(r'#define %s "?([^"\n]*)"?' % k, t)
    return m.group(1) if m else None

def table(t, name):
    m = re.search(r'static const unsigned char %s\[256\] = \{(.*?)\};' % name, t, re.S)
    if not m:
        return None
    v = [int(x) for x in re.findall(r'-?\d+', m.group(1))]
    assert len(v) == 256, (name, len(v))
    return np.array([1 if x else 0 for x in v], dtype=np.uint8)

def site_of(t):
    """-> (kind, tablename) or (None, reason)"""
    eng, pf, vs = stamp(t, "RX_ENGINE"), stamp(t, "RX_DFA_PREFILTER"), stamp(t, "RX_VM_START_SCAN")
    if pf in ("byte-class", "byte-class-bounded"):
        return ("dfa-byte-class" if eng == "dfa" else "vm-byte-class") + ("-bounded" if pf.endswith("bounded") else ""), "rx_can_begin_match"
    if pf == "first-class-bounded":
        return ("dfa-first-class-bounded" if eng == "dfa" else "vm-first-class-bounded"), "rx_start_bytes"
    if vs == "first-class":
        return "vm-hat-first-class", "rx_start_set"
    return None, "%s/%s/%s" % (eng, pf, vs)

# ---- cover: minimal number of RANGE/EQ/CUBE terms (1, 2, or '3+') ----------------------------------
_terms = None
def terms():
    global _terms
    if _terms is None:
        T = set()
        for a in range(256):
            m = 0
            for b in range(a, 256):
                m |= 1 << b
                T.add(m)
        for mask in range(256):
            for v in range(256):
                if v & ~mask & 0xFF:
                    continue
                m = 0
                for b in range(256):
                    if b & mask == v:
                        m |= 1 << b
                T.add(m)
        _terms = sorted(T, key=lambda x: -bin(x).count("1"))
    return _terms
_cc = {}
def cover_class(tab):
    S = 0
    for b in np.flatnonzero(tab):
        S |= 1 << int(b)
    if S in _cc:
        return _cc[S]
    sub = [x for x in terms() if x & ~S == 0]
    r = "3+"
    if S in set(sub):
        r = "1"
    else:
        mx = []
        for x in sub:                    # maximal terms only
            if not any(y != x and (x & ~y) == 0 for y in mx):
                mx.append(x)
        ok = False
        for i, x in enumerate(mx):
            rest = S & ~x
            if any((rest & ~y) == 0 for y in mx[i:]) :
                ok = True; break
        r = "2" if ok else "3+"
    _cc[S] = r
    return r

def main():
    man = json.load(open(CDIR + "/manifest.json"))
    rc = {(m["cfg"], m["set"], m["pattern"]): m["rc"] for m in man}
    arts = {}      # (cfg,set,pat) -> dict
    skipped = collections.Counter()
    for (cfg, s, p), r in rc.items():
        if r:
            arts[(cfg, s, p)] = {"kind": "REFUSED"}
            continue
        t = open("%s/%s/%s/%s.c" % (CDIR, cfg, s, p), errors="replace").read()
        kind, tn = site_of(t)
        a = {"engine": stamp(t, "RX_ENGINE"), "pf": stamp(t, "RX_DFA_PREFILTER"), "vs": stamp(t, "RX_VM_START_SCAN")}
        if kind is None:
            a["kind"] = "none/one-byte (" + tn + ")"
        else:
            tab = table(t, tn)
            a["kind"] = kind; a["tab"] = tab; a["size"] = int(tab.sum()); a["cover"] = cover_class(tab)
        arts[(cfg, s, p)] = a
    json.dump({"%s|%s|%s" % k: {kk: vv for kk, vv in v.items() if kk != "tab"} for k, v in arts.items()},
              open(OUT + "/artifact_sites.json", "w"), indent=0)

    rows = []
    for s in SETS:
        sb = subbench.load("%s/bench/%s" % (ROOT, s))
        setid = "%s@%s" % (s, sb.version)
        cache = {}
        for reg in SRC_REGIMES:
            if reg not in sb.regimes:
                continue
            for sj in sb.subjects_for(reg):
                if not os.path.exists(sj.path):
                    skipped["missing-subject:" + setid] += 1
                    continue
                if sj.path not in cache:
                    cache.clear(); cache[sj.path] = np.frombuffer(open(sj.path, "rb").read(), dtype=np.uint8)
                data = cache[sj.path]
                for p in sb.patterns:
                    for cfg in CFGS:
                        a = arts[(cfg, s, p.name)]
                        if "tab" not in a:
                            continue
                        pos = np.flatnonzero(a["tab"][data])
                        n = len(pos)
                        if n < 2:
                            rows.append((cfg, setid, p.name, reg, sj.subject_id, len(data), a["kind"], a["size"], a["cover"], n, "", "", ""))
                            continue
                        g = np.diff(pos)
                        vals, cnt = np.unique(g, return_counts=True)
                        i = int(np.argmax(cnt))
                        rows.append((cfg, setid, p.name, reg, sj.subject_id, len(data), a["kind"], a["size"], a["cover"], n,
                                     "%.4f" % g.mean(), int(vals[i]), "%.4f" % (cnt[i] / len(g))))
    with open(OUT + "/cells.tsv", "w") as f:
        f.write("cfg\tset\tpattern\tregime\tsubject\tlen\tsite\tsetsize\tcover\tlandings\tmean_gap\tdom_gap\tdom_share\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")
    print(len(rows), "cells with a set site;", dict(skipped))

main()
