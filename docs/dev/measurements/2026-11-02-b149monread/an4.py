# b149monread an4: remaining unusual detail (12 slow/fast large cells, pass-twin at both pins, _in/default by pattern, timed-out rows, streams).
import sys, collections, statistics
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
R = {n: load(n)[0] for n in NAMES}
print("== all large cells with cb32/614 ratio < 0.8 or > 1.1 (auto)")
for k, rows in sorted(R["auto"][2].items()):
    if k[1] != "large-subject-throughput": continue
    o = R["auto614"][2][k]
    if o[0]["o"] == rows[0]["o"] == "matched-as-expected":
        r = med(rows) / med(o)
        if r < 0.8 or r > 1.1: print(f"  x{r:.3f} {k[0]:22s} {k[2]:16s} 614={med(o):.5g} cb={med(rows):.5g}   vm: {med(R['vm'][2][k]) / med(R['vm614'][2][k]):.3f}")
print("\n== pass-twin and real-pass (1 MB subjects, ns per call) at 614d45eb3 vs cb32eda28, separate-TU, vm route")
for fam, sub in (("co-luhn", "co-luhn-1m"), ("co-isbn", "co-isbn-1m"), ("co-member", "co-member-1m")):
    for a in ("vm614", "vm"):
        g = lambda p: med(R[a][2][(p, "large-subject-throughput", sub, "plain")])
        print(f"  {fam:10s} {a:6s} real={g(fam):.0f} pass={g(fam+'-pass'):.0f} twin={g(fam+'-twin'):.0f} pass-twin={g(fam+'-pass')-g(fam+'-twin'):.0f} real-pass={g(fam)-g(fam+'-pass'):.0f}")
print("\n== _in / default (short cells) by pattern, auto: median ratio, plus the cells with ratio <0.5 or >1.4")
by = collections.defaultdict(list); odd = []
for k, rows in R["auto_in"][2].items():
    if k[1] != "short-subject-search": continue
    o = R["auto"][2][k]
    if o[0]["o"] == rows[0]["o"] == "matched-as-expected" and med(o) and med(rows):
        r = med(rows) / med(o); by[k[0]].append(r)
        if r < 0.5 or r > 1.4: odd.append((r, k, med(o), med(rows)))
for p, v in sorted(by.items()): print(f"  {p:24s} n={len(v)} median={statistics.median(v):.3f} min={min(v):.3f} max={max(v):.3f}")
for r, k, a, b in sorted(odd)[:10] + sorted(odd)[-6:]: print(f"   odd x{r:.3f} {k[0]} {k[2]} default={a:.4g} in={b:.4g}")
print("\n== timed-out rows (deep arms): elapsed per row")
for n in ("interp_deep", "onig_deep"):
    for k, rows in sorted(R[n][2].items()):
        if rows[0]["o"] == "timed-out": print(f"  {n:11s} {k[0]:22s} {k[2]:16s} trials={len(rows)} diag={rows[0]['diag'][:60]} ns={[r['ns'] for r in rows][:2]} it={rows[0]['it']}")
print("\n== deep-arm sexp ladder (wild-sexp-balanced nest-paren-*): onig_deep / interp_deep / jit_deep / auto_in medians")
for s in ("nest-paren-128", "nest-paren-512", "nest-paren-2k", "nest-paren-8k", "nest-paren-32k", "nest-paren-100k", "sx-1m"):
    k = ("wild-sexp-balanced", "large-subject-throughput", s, "plain")
    if k not in R["onig_deep"][2]: continue
    print(f"  {s:15s}", "  ".join(f"{n}={R[n][2][k][0]['o'][:7]}:{(med(R[n][2][k]) or 0):.4g}" for n in ("jit_deep", "interp_deep", "onig_deep", "auto_in")))
print("\n== wrong rows (onig_deep) observed vs expected")
for k, rows in sorted(R["onig_deep"][2].items()):
    if rows[0]["o"] == "wrong-span-or-captures": print("  ", k, rows[0]["obs"], rows[0]["diag"])
print("\n== callout compile rows: binding / spec per testee (first co-luhn row)")
for n in ("auto", "auto_inl", "vm_inl", "auto614"):
    c = R[n][1][("co-luhn", "plain")][0]; em = c["engine_metadata"]
    print(f"  {n:9s} binding={em.get('callout_binding')} bindings={em.get('callout_bindings')!r} code_langs={em.get('code_langs')} emit={em.get('emit_bytes')} code={em.get('emit_code_bytes')} art={c['artifact_bytes']} prog={em.get('vm_program_bytes')} shape={em.get('vm_entry_shape')}")
print("\n== inline vs sep emit/artifact bytes per callout compile row (plain/whole), auto")
for pat in ("co-luhn", "co-luhn-pass", "co-isbn", "co-isbn-pass", "co-member", "co-member-pass", "co-netstr"):
    for f in ("plain", "whole-subject"):
        s = R["auto"][1].get((pat, f)); i = R["auto_inl"][1].get((pat, f))
        if s and i:
            a, b = s[0]["engine_metadata"], i[0]["engine_metadata"]
            print(f"  {pat:16s} {f:13s} sep emit={a.get('emit_bytes')} code={a.get('emit_code_bytes')} art={s[0]['artifact_bytes']} | inl emit={b.get('emit_bytes')} code={b.get('emit_code_bytes')} art={i[0]['artifact_bytes']}  gcc_ms sep={[p['elapsed_ns'] for p in (s[0]['cost'] or {}).get('phases', []) if p['name']=='gcc']} inl={[p['elapsed_ns'] for p in (i[0]['cost'] or {}).get('phases', []) if p['name']=='gcc']}")
print("\n== inline arm: the 4 vars members' compile row (outcome/diag)")
for pat in ("va-route", "va-tenant", "va-term", "va-term-bang"):
    for f in ("plain", "whole-subject"):
        for n in ("auto", "auto_inl"):
            c = R[n][1].get((pat, f))
            print(f"  {n:9s} {pat:13s} {f:13s}", None if not c else (len(c), c[0]["compile_outcome"], (c[0]["diagnostic"] or "")[:80]))
