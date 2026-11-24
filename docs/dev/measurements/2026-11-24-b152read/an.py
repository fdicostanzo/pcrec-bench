# b152read analysis: reads committed report TSVs + the b152prep census ONLY (no store load, no timing).
# usage: python3 an.py altwide|movers|sentinel  (run from the worktree root)
import csv, sys, math, collections, glob, re
R = "reports/2026-11-24-"
AUTO = "pcrec_d6c5e71a5_auto-caps-simdna"; VM = "pcrec_d6c5e71a5_vm-caps-simdna"
def rows(path):
    with open(path, newline="") as f:
        for r in csv.reader(f, delimiter="\t"):
            if r and not r[0].startswith("#"): yield r
def short(t):
    if t.startswith("pcrec"): return "pcrec-" + t.split("_")[2].split("-")[0]
    if t.startswith("libpcre2"): return "pcre2-" + t.split("_")[2].split("-")[0]
    return t.split("_")[0]
def altwide():
    T = R + "altwide-0.3-ryzen7700x-fullroster-d6c5e71a5.tsv"
    cells = collections.defaultdict(dict)   # (pat,regime,form) -> testee -> {metric: val}
    for r in rows(T):
        if r[0] == "rank":
            sec, pat, subj, reg, form, fact, tee = r[:7]
            tee = tee.split("@")[0]
            cells[(pat, reg, form)].setdefault(tee, {})[r[10]] = float(r[11]) if r[11] else None
    # class-pure caps best from rank_yes
    yes = collections.defaultdict(dict)
    for r in rows(T):
        if r[0] == "rank_yes":
            yes[(r[1], r[3], r[4])].setdefault(r[6].split("@")[0], {})[r[10]] = float(r[11]) if r[11] else None
    out = []
    for k in sorted(cells):
        c = cells[k]
        best = min(c, key=lambda t: c[t]["median_ns"])
        for who in (AUTO, VM):
            if who not in c: continue
            m = c[who]["median_ns"]; b = c[best]["median_ns"]
            sd = max(c[who].get("stddev_ns") or 0, c[best].get("stddev_ns") or 0)
            beyond = (m - b) > 2 * sd and who != best
            yb = None
            if k in yes and yes[k]:
                yb = min(yes[k], key=lambda t: yes[k][t]["median_ns"])
            ym = yes[k][yb]["median_ns"] if yb else None
            ybey = False
            if yb and who in yes[k] and yb != who:
                ysd = max(yes[k][who].get("stddev_ns") or 0, yes[k][yb].get("stddev_ns") or 0)
                ybey = (yes[k][who]["median_ns"] - ym) > 2 * ysd
            out.append((k, who, m / b, best, beyond, (m / ym) if ym else None, yb, ybey))
    return cells, out
def fam(p):
    m = re.match(r"([a-z0-9]+?)-(\d+)$", p)
    return (m.group(1), int(m.group(2))) if m else (p, 0)
if sys.argv[1] == "altwide":
    cells, out = altwide()
    print("## per-cell ratio to best (pooled roster), auto and vm; * = beyond noise (|diff|>2*max stddev, reporter R8 rule)")
    for k, who, ratio, best, beyond, yr, yb, ybey in out:
        print("\t".join([k[0], k[1], k[2], "auto" if who == AUTO else "vm", f"{ratio:.3f}", short(best), "*" if beyond else "", f"{yr:.3f}" if yr else "-", short(yb) if yb else "-"]))
    print("\n## NAMED LOSSES (ratio>1 beyond noise, pooled best)")
    for who, nm in ((AUTO, "auto"), (VM, "vm")):
        L = [o for o in out if o[1] == who and o[4]]
        print(f"# {nm}: {len(L)} of {sum(1 for o in out if o[1]==who)} cells")
        for k, w, ratio, best, bey, yr, yb, ybey in sorted(L, key=lambda o: -o[2]):
            print(f"{nm}\t{k[0]}\t{k[1]}\t{k[2]}\tx{ratio:.2f}\tbest={short(best)}")
    print("\n## NAMED LOSSES vs best CAPTURING engine (class-pure headline; ratio>1 AND beyond noise by the same 2*max(stddev) rule)")
    for who, nm in ((AUTO, "auto"), (VM, "vm")):
        L = [o for o in out if o[1] == who and o[5] and o[7]]
        print(f"# {nm}: {len(L)} of {sum(1 for o in out if o[1]==who and o[5])}")
        for k, w, ratio, best, bey, yr, yb, ybey in sorted(L, key=lambda o: -o[5]):
            print(f"{nm}\t{k[0]}\t{k[1]}\t{k[2]}\tx{yr:.2f}\tbest_caps={short(yb)}")
    print("\n## NAMED LOSSES vs best NON-PCREC CAPTURING-CLASS engine (re2, pcre2-jit, pcre2-interp; rust and vectorscan are capture_class=no in this roster), beyond noise; the honest 'other engine' reading")
    for who, nm in ((AUTO, "auto"), (VM, "vm")):
        L = []; tot = 0
        for k in sorted(cells):
            c = cells[k]
            if who not in c: continue
            oth = {t: v for t, v in c.items() if t.startswith(("re2", "libpcre2"))}
            if not oth: continue
            tot += 1
            bt = min(oth, key=lambda t: oth[t]["median_ns"]); b = oth[bt]
            sd = max(c[who].get("stddev_ns") or 0, b.get("stddev_ns") or 0)
            if c[who]["median_ns"] - b["median_ns"] > 2 * sd: L.append((c[who]["median_ns"] / b["median_ns"], k, bt))
        print(f"# {nm}: {len(L)} of {tot} cells")
        for r, k, bt in sorted(L, reverse=True): print(f"{nm}\t{k[0]}\t{k[1]}\t{k[2]}\tx{r:.2f}\tbest_other={short(bt)}")
    print("\n## geomean ratio-to-best by regime x form (cells where it compiled)")
    for who, nm in ((AUTO, "auto"), (VM, "vm")):
        g = collections.defaultdict(list)
        for o in out:
            if o[1] == who: g[(o[0][1], o[0][2])].append(o[2])
        for kk in sorted(g):
            print(nm, kk, len(g[kk]), f"geomean x{math.exp(sum(map(math.log,g[kk]))/len(g[kk])):.2f}", f"max x{max(g[kk]):.2f}", f"wins {sum(1 for v in g[kk] if v==1.0)}")
    print("\n## ladder by branch count: w-N plain, ratio to best (auto / vm), per regime")
    for reg in ("large-subject-throughput", "short-subject-search", "match-compliance"):
        for form in ("plain", "whole-subject"):
            print(f"# {reg} {form}")
            ks = sorted([k for k in cells if k[1] == reg and k[2] == form and fam(k[0])[0] == "w"], key=lambda k: fam(k[0])[1])
            for k in ks:
                d = {o[1]: o for o in out if o[0] == k}
                a = f"x{d[AUTO][2]:.2f}" if AUTO in d else "-"
                v = f"x{d[VM][2]:.2f}" if VM in d else "refused/-"
                b = short(min(cells[k], key=lambda t: cells[k][t]["median_ns"]))
                ay = f"x{d[AUTO][5]:.2f}" if AUTO in d and d[AUTO][5] else "-"
                vy = f"x{d[VM][5]:.2f}" if VM in d and d[VM][5] else "-"
                byc = short(d[AUTO][6]) if AUTO in d and d[AUTO][6] else (short(d[VM][6]) if VM in d and d[VM][6] else "-")
                print(f"  {k[0]:8s} auto {a:10s} vm {v:10s} best={b:12s} | caps-only: auto {ay:9s} vm {vy:9s} best_caps={byc}")
    # presence of cells where auto/vm absent
    print("\n## class-pure (caps-only roster) geomean/wins by regime x form")
    for who, nm in ((AUTO, "auto"), (VM, "vm")):
        g = collections.defaultdict(list)
        for o in out:
            if o[1] == who and o[5]: g[(o[0][1], o[0][2])].append(o[5])
        for kk in sorted(g):
            print(nm, kk, len(g[kk]), f"geomean x{math.exp(sum(map(math.log,g[kk]))/len(g[kk])):.2f}", f"max x{max(g[kk]):.2f}", f"wins {sum(1 for v in g[kk] if abs(v-1)<1e-9)}", f">1.25: {sum(1 for v in g[kk] if v>1.25)}")
    print("\n## cells with no auto or vm timing:")
    for k in sorted(cells):
        for who, nm in ((AUTO, "auto"), (VM, "vm")):
            if who not in cells[k]: print(nm, *k)
elif sys.argv[1] == "movers":
    D = "docs/dev/measurements/"
    def load(f):
        d = {}
        for r in rows(D + f):
            if r[0] == "set": continue
            d[(r[0], r[1], r[2], r[3])] = r[6]
        return d
    c152 = load("2026-11-23-b152prep-census.tsv"); c149 = load("2026-10-30-b149prep-census.tsv"); c147 = load("2026-10-27-b147prep-census.tsv")
    sets = [("capability", "capability-0.4", 1), ("syntax", "syntax-0.2", 1), ("bounded", "bounded-0.3", 3), ("loglines", "loglines-0.1", 3), ("email-specimen", "email-specimen-0.2", 3), ("litrun", "litrun-0.1", 3)]
    for sb, nm, nstep in sets:
        T = R + nm + "-ryzen7700x-d6c5e71a5.tsv"
        print(f"\n=== {nm}  (previous pin {'cb32eda28: census b152prep only' if nstep==1 else '9ae59f5d4: censuses b147prep + b149prep + b152prep chained'})")
        cnt = collections.Counter()
        for r in rows(T):
            if r[0] != "d119": continue
            pat, subj, reg, form = r[1], r[2], r[3], r[4]
            v = r[11]
            kv = dict(x.split("=", 1) for x in r[16].split("; ") if "=" in x) if len(r) > 16 else {}
            ident = kv.get("identity"); d = float(kv.get("delta_pct", "nan")); bar = kv.get("bar_pct")
            cnt[(v, ident)] += 1
            if v in ("regress", "improve"):
                ck = (sb, pat, "caps", "whole" if form == "whole-subject" else "plain")
                parts = [("b152", c152.get(ck, "NOCENSUS"))]
                if nstep == 3: parts = [("b147", c147.get(ck, "NOCENSUS")), ("b149", c149.get(ck, "NOCENSUS"))] + parts
                attr = " | ".join(f"{a}:{b}" for a, b in parts if b != "-")
                tiny = "TINY" if abs(d) < 3 else ""
                print(f"{v}\t{pat}\t{reg}\t{form}\tdelta={d:+.1f}%\tbar={bar}\tidentity={ident}\tafter_ns={kv.get('after_ns')}\t{tiny}\tattr={attr or 'NO PROGRAM CHANGE IN ANY CENSUS'}")
        print("# verdict x identity:", dict(cnt))
elif sys.argv[1] == "sentinel":
    def med(path):
        d = {}
        for r in rows(path):
            if r[0] == "rank" and r[10] == "median_ns":
                d[(r[1], r[3], r[6])] = float(r[11])
        return d
    new = med(R + "sentinel-0.1-ryzen7700x-d6c5e71a5.tsv")
    old = med("reports/2026-11-02-sentinel-0.1-ryzen7700x-first-cb32eda28.tsv")
    def ts(t): return t.split("@")[1]
    tees = sorted({k[2] for k in new}); pats = sorted({(k[0], k[1]) for k in new})
    print("records tonight:", *tees, sep="\n  ")
    def idx(prefix, i): return sorted([t for t in tees if t.startswith(prefix)], key=ts)[i]
    CB0, CB1, D0, D1, J0, J1 = idx("pcrec_cb32", 0), idx("pcrec_cb32", 1), idx("pcrec_d6c5", 0), idx("pcrec_d6c5", 1), idx("libpcre2", 0), idx("libpcre2", 1)
    def g(vals): return math.exp(sum(math.log(v) for v in vals) / len(vals))
    def table(name, a, b, sel=None):
        rs = {}
        for p in pats:
            if (p[0], p[1], a) in new and (p[0], p[1], b) in new: rs[p] = new[(p[0], p[1], b)] / new[(p[0], p[1], a)]
        for reg in ("short-subject-search", "large-subject-throughput"):
            v = [x for (pp, rg), x in rs.items() if rg == reg]
            if v: print(f"{name:34s} {reg:26s} n={len(v):2d} geomean x{g(v):.4f} min x{min(v):.3f} max x{max(v):.3f}")
        return rs
    print("\n-- in-window drift, close / open")
    table("cb32eda28 close/open", CB0, CB1); table("d6c5e71a5 close/open", D0, D1); table("pcre2-jit close/open", J0, J1)
    print("\n-- in-window pin delta d6c5e71a5 / cb32eda28")
    table("open", CB0, D0); table("close", CB1, D1)
    print("\n-- sentinel patterns beyond 1.10 either way, pin delta at open / close")
    for nm, a, b in (("open", CB0, D0), ("close", CB1, D1)):
        for p in pats:
            r = new[(p[0], p[1], b)] / new[(p[0], p[1], a)]
            if abs(math.log(r)) > math.log(1.10): print(f"  {nm}\t{p[0]}\t{p[1]}\tx{r:.3f}")
    print("\n-- cross-window offset: tonight / 11-01..02 W2+monday records (same pin cb32eda28; jit as control)")
    oldt = sorted({k[2] for k in old}); print("  old records:", *oldt, sep="\n    ")
    for pref, tn in (("pcrec_cb32", [CB0, CB1]), ("libpcre2", [J0, J1])):
        for ot in [t for t in oldt if t.startswith(pref) and "nocaps" not in t]:
            for t in tn:
                rs = {p: new[(p[0], p[1], t)] / old[(p[0], p[1], ot)] for p in pats if (p[0], p[1], ot) in old and (p[0], p[1], t) in new}
                for reg in ("short-subject-search", "large-subject-throughput"):
                    v = [x for (pp, rg), x in rs.items() if rg == reg]
                    if v: print(f"  {ts(t)[:15]} / {ts(ot)[:15]} ({pref[:6]}) {reg:26s} n={len(v)} geomean x{g(v):.4f} range x{min(v):.3f}-x{max(v):.3f}")
