#!/usr/bin/env python3
"""utf8@0.1 first sample at pcrec ce658cb7: R2-R7 of bench/utf8/NOTES.md's
outlier rule (R0/R1/R8 already scored in the 2026-09-26 ledger). Backs the
addendum docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7-addendum-r2r7.md.

Source: lane b97read ([B97] follow-up read), 2026-09-26. Reads ONLY
committed files -- no store access, no report render:
  G.tsv                (set grain, reporter v24; "rank" section holds the
                        (pattern, regime, testee) CELL median_ns aggregated
                        over every subject in the regime -- used for R2, R7;
                        "compile" section holds the compile-time completion
                        of R5 for the seven non-pcrec compiling testees)
  G.subject-grain.tsv  (per-subject median_ns -- used for R3, R4, and R7's
                        t-1m/t-64k pair)
where G = reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.
bench/utf8/subject_facts.tsv gives the byte length of each throughput
subject (ns/byte = median_ns / len). No measurement is run; run from the
repo root.
"""
import csv
import statistics
import sys
from collections import defaultdict

G = "reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7"
csv.field_size_limit(1 << 30)

JIT = "libpcre2_10.46_jit-caps-simdna_utf8"

SUBJ_LEN = {
    "t-64k": 65536, "t-256k": 262144, "t-1m": 1048576,
    "t-64k-lat": 65536, "t-64k-cyr": 65536, "t-64k-cjk": 65536, "t-64k-asc": 65536,
}
SCRIPT_SUBJS = ("t-64k-lat", "t-64k-cyr", "t-64k-cjk", "t-64k-asc")


def rows(path):
    with open(path, encoding="utf-8") as fh:
        next(fh)  # the '# reporter: ...' filter-header line
        yield from csv.DictReader(fh, delimiter="\t")


def load_cell_median(path):
    """(pattern, regime, testee) -> (median_ns, n_wrong) from the SET-grain
    'rank' section (subject_or_na == '(set)', one row per regime)."""
    out = {}
    for r in rows(path):
        if r["section"] == "rank" and r["metric"] == "median_ns":
            out[(r["pattern"], r["regime_or_na"], r["testee"])] = (
                float(r["value"]), int(r["n_wrong"]) if r["n_wrong"] else 0)
    return out


def load_subject_median(path):
    """(pattern, subject, testee) -> median_ns from the SUBJECT-grain
    'rank' section."""
    out = defaultdict(dict)
    for r in rows(path):
        if r["section"] == "rank" and r["metric"] == "median_ns":
            out[(r["pattern"], r["testee"])][r["subject_or_na"]] = float(r["value"])
    return out


def load_compile_time(path):
    """testee -> {(pattern, form): median_total_ns or None (refusal)}"""
    out = defaultdict(dict)
    for r in rows(path):
        if r["section"] == "compile" and r["metric"] == "median_total_ns":
            v = r["value"]
            out[r["testee"]][(r["pattern"], r["form"])] = float(v) if v else None
    return out


print(f"# source: {G}.tsv / {G}.subject-grain.tsv (reporter v24); bench/utf8/subject_facts.tsv")
print("# no store access; no report render; lane b97read, 2026-09-26\n")

cell = load_cell_median(f"{G}.tsv")
patterns = sorted({k[0] for k in cell})
print(f"# cell_median: {len(cell)} rows ({len(patterns)} patterns x 2 regimes x <=11 testees)\n")

# ---------------------------------------------------------------- R2 ----
print("=" * 78)
print("R2 -- pcre2-utf-jit band: cell/jit ratio > 2 (worse) or < 1/20 (better)")
print("=" * 78)
per_t = defaultdict(lambda: [0, 0, 0])
per_t_r = defaultdict(lambda: [0, 0, 0])
hits = []
for (p, regime, t), (ns, nw) in cell.items():
    if t == JIT:
        continue
    jk = (p, regime, JIT)
    if jk not in cell:
        continue
    jns, jnw = cell[jk]
    if jns <= 0:
        continue
    ratio = ns / jns
    per_t[t][2] += 1
    per_t_r[(t, regime)][2] += 1
    if ratio > 2.0:
        per_t[t][0] += 1
        per_t_r[(t, regime)][0] += 1
        hits.append((p, regime, t, ratio, ns, jns))
    elif ratio < 1.0 / 20.0:
        per_t[t][1] += 1
        per_t_r[(t, regime)][1] += 1
        hits.append((p, regime, t, ratio, ns, jns))
total_cmp = sum(v[2] for v in per_t.values())
total_hit = sum(v[0] + v[1] for v in per_t.values())
print(f"total: {total_hit} of {total_cmp} comparable cells trip R2")
print("\nper testee: slower(ratio>2)  faster(ratio<1/20)  comparable")
for t in sorted(per_t):
    s, f, n = per_t[t]
    print(f"  {t:55s} {s:4d}  {f:4d}  {n:4d}")
print("\nper (testee, regime):")
for (t, r) in sorted(per_t_r):
    s, f, n = per_t_r[(t, r)]
    print(f"  {t:55s} {r:26s} {s:4d}  {f:4d}  {n:4d}")
hits.sort(key=lambda h: -max(h[3], 1 / h[3]))
print(f"\nworst 15 by ratio (of {len(hits)} hits):")
for p, regime, t, ratio, ns, jns in hits[:15]:
    print(f"  {p:22s} {regime:26s} {t:55s} ratio={ratio:10.4f}  ns={ns:14.1f}  jit_ns={jns:14.1f}")

# ---------------------------------------------------------------- R7 ----
print()
print("=" * 78)
print("R7 -- t-1m/t-64k ns/byte ratio outside [0.7, 1.4], read on EVERY pattern")
print("=" * 78)
subj = load_subject_median(f"{G}.subject-grain.tsv")
r7_hits, r7_na = [], []
for (p, t), d in subj.items():
    if "t-1m" in d and "t-64k" in d:
        npb1m = d["t-1m"] / SUBJ_LEN["t-1m"]
        npb64 = d["t-64k"] / SUBJ_LEN["t-64k"]
        if npb64 <= 0:
            continue
        ratio = npb1m / npb64
        if ratio < 0.7 or ratio > 1.4:
            r7_hits.append((p, t, ratio, npb1m, npb64))
r7_hits.sort(key=lambda h: -abs(1 - h[2]))
n_pairs = sum(1 for d in subj.values() if "t-1m" in d and "t-64k" in d)
print(f"total: {len(r7_hits)} of {n_pairs} (pattern,testee) pairs trip R7")
print(f"\nall {len(r7_hits)} hits:")
for p, t, ratio, a, b in r7_hits:
    print(f"  {p:22s} {t:55s} ratio={ratio:8.4f}  t1m_ns/B={a:10.6f}  t64k_ns/B={b:10.6f}")

# ---------------------------------------------------------------- R3 ----
print()
print("=" * 78)
print("R3 -- encoding band: floor/ci-ascii-control/asr-b-ascii ns/byte vs t-64k-asc, >x3")
print("=" * 78)
R3_PATTERNS = ["floor", "ci-ascii-control", "asr-b-ascii"]
r3_hits = []
n_r3_cmp = 0
for (p, t), d in subj.items():
    if p not in R3_PATTERNS or "t-64k-asc" not in d:
        continue
    asc_npb = d["t-64k-asc"] / SUBJ_LEN["t-64k-asc"]
    if asc_npb <= 0:
        continue
    for s in ("t-64k-lat", "t-64k-cyr", "t-64k-cjk"):
        if s not in d:
            continue
        n_r3_cmp += 1
        npb = d[s] / SUBJ_LEN[s]
        ratio = npb / asc_npb
        if ratio > 3.0 or ratio < 1.0 / 3.0:
            r3_hits.append((p, t, s, ratio, npb, asc_npb))
r3_hits.sort(key=lambda h: -max(h[3], 1 / h[3]))
print(f"total: {len(r3_hits)} of {n_r3_cmp} (pattern,testee,script) triples trip R3")
print(f"\nall {len(r3_hits)} hits:")
for p, t, s, ratio, npb, asc_npb in r3_hits:
    print(f"  {p:18s} {t:55s} {s:11s} ratio={ratio:9.4f}  npb={npb:10.6f}  asc_npb={asc_npb:10.6f}")

# ---------------------------------------------------------------- R4 ----
print()
print("=" * 78)
print("R4 -- script band: max/min ns/byte over the 4 per-script 64KB subjects, per (pattern,testee), >x4")
print("=" * 78)
r4_hits, r4_na = [], []
for (p, t), d in subj.items():
    have = [s for s in SCRIPT_SUBJS if s in d]
    if len(have) < 4:
        if have:
            r4_na.append((p, t, sorted(have)))
        continue
    npbs = {s: d[s] / SUBJ_LEN[s] for s in SCRIPT_SUBJS}
    mx, mn = max(npbs.values()), min(npbs.values())
    if mn <= 0:
        continue
    ratio = mx / mn
    if ratio > 4.0:
        hi = max(npbs, key=npbs.get)
        lo = min(npbs, key=npbs.get)
        r4_hits.append((p, t, ratio, hi, npbs[hi], lo, npbs[lo]))
r4_hits.sort(key=lambda h: -h[2])
n_r4_full = sum(1 for (p, t), d in subj.items() if all(s in d for s in SCRIPT_SUBJS))
print(f"total: {len(r4_hits)} of {n_r4_full} (pattern,testee) pairs with all 4 subjects trip R4")
print(f"(pattern,testee) pairs missing >=1 of the 4 subjects (excluded; see R0 cross-check below): {len(r4_na)}")
for p, t, have in r4_na:
    print(f"  MISSING  {p:18s} {t:55s} have={have}")
print(f"\nworst 40 of {len(r4_hits)} hits:")
for p, t, ratio, hi, hiv, lo, lov in r4_hits[:40]:
    print(f"  {p:22s} {t:55s} ratio={ratio:10.4f}  hi={hi}({hiv:.6f})  lo={lo}({lov:.6f})")

# cross-check: are the R4-missing pairs exactly the R0 (wrong-answer) population?
print("\ncross-check -- excluded-section rows (n_wrong>0) for the R4-missing pairs:")
excluded_wrong = set()
for r in rows(f"{G}.subject-grain.tsv"):
    if r["section"] == "excluded" and r["n_wrong"] and int(r["n_wrong"]) > 0:
        excluded_wrong.add((r["pattern"], r["testee"]))
for p, t, have in r4_na:
    print(f"  {p:18s} {t:55s} in excluded(n_wrong>0) section: {(p, t) in excluded_wrong}")

# ------------------------------------------------------- R5 completion --
print()
print("=" * 78)
print("R5 completion -- compile median_total_ns cliff (>x10 testee's own median),")
print("the 7 non-pcrec compiling testees (pcrec's 4 configs already scored in the")
print("first ledger's section 6/7)")
print("=" * 78)
ctime = load_compile_time(f"{G}.tsv")
for t in sorted(ctime):
    if t.startswith("pcrec_"):
        continue
    plain = {k: v for k, v in ctime[t].items() if k[1] == "plain" and v is not None}
    refused = [k[0] for k, v in ctime[t].items() if k[1] == "plain" and v is None]
    if not plain:
        continue
    med = statistics.median(plain.values())
    hits = [(k[0], v, v / med) for k, v in plain.items() if med > 0 and v / med > 10.0]
    hits.sort(key=lambda h: -h[2])
    print(f"\n{t}: n={len(plain)} plain-form median={med:.1f} ns; "
          f"{len(hits)} cliffs (>x10); {len(refused)} refused (median_total_ns absent): {refused}")
    for pat, v, r in hits:
        print(f"    {pat:20s} {v:14.1f} ns  x{r:8.2f}")
