# b149w2read: read-only analysis helpers over the committed W2 (b149w2) records. No engine is run, nothing is timed.
# usage: python3 w2.py MODE   (run from anywhere; ROOT below is the lane worktree whose store/ holds the records)
import csv, collections, glob, json, os, statistics, sys

ROOT = os.environ.get("W2ROOT", "/home/pcrec/projects/pcrec-bench/worktrees/b149w2read")
S = ROOT + "/store/records"
CENSUS = ROOT + "/docs/dev/measurements/2026-10-30-b149prep-census.tsv"
CB, OLD = "cb32eda28", "614d45eb3"
# W2 record timestamps (UTC), 2026-11-01
CAP = {("cb", "caps"): "20261101T133920Z", ("cb", "nocaps"): "20261101T144104Z",
       ("old", "caps"): "20261101T154236Z", ("old", "nocaps"): "20261101T164505Z"}
SEN_OPEN = {"cb-caps": "20261101T125936Z", "old-caps": "20261101T130521Z", "cb-nocaps": "20261101T131109Z", "jit": "20261101T132823Z"}
SEN_CLOSE = {"cb-caps": "20261101T174951Z", "old-caps": "20261101T175549Z", "cb-nocaps": "20261101T180128Z", "jit": "20261101T180753Z"}
JIT = "libpcre2_10.46_jit-caps-simdna"
LARGE, SHORT = "large-subject-throughput", "short-subject-search"


def tid(which, cfg):
    return f"pcrec_{CB if which == 'cb' else OLD}_auto-{cfg}-simdna"


def path(sb, t, stamp):
    fs = glob.glob(f"{S}/{sb}/{t}/*{stamp}*.jsonl")
    assert len(fs) == 1, (sb, t, stamp, fs)
    return fs[0]


class Rec:
    def __init__(self, p):
        self.path = p
        self.setup = None
        self.comp = {}
        self.cells = collections.defaultdict(lambda: {"t": {}, "o": collections.Counter(), "bytes": None, "iters": {}})
        for l in open(p):
            d = json.loads(l)
            k = d.get("kind")
            if k == "setup":
                self.setup = d
            elif k == "compile":
                self.comp[(d.get("pattern_id"), d.get("form", "plain"))] = d
            elif k == "match":
                key = (d["pattern_id"], d["subject_id"], d["regime"], d.get("form", "plain"))
                c = self.cells[key]
                c["o"][d["match_outcome"]] += 1
                tm = d.get("timing")
                if tm and tm.get("iterations"):
                    c["t"][d["trial"]] = tm["elapsed_ns"] / tm["iterations"]
                    c["bytes"] = tm["bytes_processed"] / tm["iterations"]
                    c["iters"][d["trial"]] = tm["iterations"]

    def med(self, key):
        c = self.cells.get(key)
        if not c or not c["t"]:
            return None
        return statistics.median(c["t"].values())

    def clean(self, key):
        c = self.cells.get(key)
        return bool(c) and set(c["o"]) == {"matched-as-expected"} and len(c["t"]) == sum(c["o"].values())

    def setsum(self, pat, regime, form, subjects):
        """per-trial sums of ns/call over `subjects` (a list), trial index sorted; None if a trial is missing"""
        tr = collections.defaultdict(float)
        n = collections.Counter()
        for s in subjects:
            c = self.cells.get((pat, s, regime, form))
            if not c or not c["t"]:
                return None
            for t, v in c["t"].items():
                tr[t] += v
                n[t] += 1
        if len(set(n.values())) != 1 or len(tr) < 5:
            return None
        return [tr[t] for t in sorted(tr)]

    def subjects(self, pat, regime, form):
        return sorted({k[1] for k in self.cells if k[0] == pat and k[2] == regime and k[3] == form})


def load_cap(which, cfg):
    return Rec(path("capability@0.4", tid(which, cfg), CAP[(which, cfg)]))


def census():
    out = {}
    for r in csv.DictReader((l for l in open(CENSUS) if not l.startswith("#")), delimiter="\t"):
        def pb(s):
            try:
                e, c = s.split(":")
                return int(e), int(c)
            except Exception:
                return None
        out[(r["set"], r["pattern_id"], r["config"], r["form"])] = dict(
            attr=r["attribution"], v3=r["v3"], old=pb(r["old_bytes:code"]), new=pb(r["new_bytes:code"]),
            stamps=r["stamp_moves"], nowin=r["nowindow_arm"], norh=r["noreqhandoff_arm"],
            old_scan=r["old_dfa_scan"], new_scan=r["new_dfa_scan"], old_pf=r["old_dfa_prefilter"], new_pf=r["new_dfa_prefilter"],
            new_engine=r["new_engine"], new_rh=r["new_req_handoff"])
    return out


def pct(v, q):
    v = sorted(v)
    return v[min(len(v) - 1, int(q * len(v)))]


def form_of(k):
    return "plain" if k[1] == "plain" else "whole"


# ---------------------------------------------------------------- modes
def mode_quality():
    fs = []
    for sb in ("capability@0.4", "sentinel@0.1"):
        for f in sorted(glob.glob(f"{S}/{sb}/*/*20261101T1[2-8]*.jsonl")):
            fs.append(f)
    for f in fs:
        d = json.loads(open(f).readline())
        e = d["environment"]
        ta = d.get("trial_agreement", {})
        o = e["occupancy"]
        r = d.get("run", {})
        print(f.split("/")[-1][:-6].replace("__ryzen7700x", ""))
        print("   status", d.get("status"), "| load b/a %.2f/%.2f (%s) | occ before %s max %.1f tgt %.1f | after %s max %.1f tgt %.1f | trials %s" % (
            e["load"]["before"]["load1"], e["load"]["after"]["load1"], e["load"]["verdict"], o["before"]["verdict"], o["before"]["max_busy_pct"],
            o["before"]["target_busy_pct"], o["after"]["verdict"], o["after"]["max_busy_pct"], o["after"]["target_busy_pct"], r.get("trials", "?")))
        print("   agreement:", {k: ta.get(k) for k in ("verdict", "rule", "worst_group") if k in ta}, "| harness", r.get("harness_commit"), "| schema", d.get("schema_version"))
        print("   driver flags tail:", str(r.get("driver_build_flags"))[-90:])


def sen_load(which, kind):
    m = SEN_OPEN if kind == "open" else SEN_CLOSE
    if which == "jit":
        return Rec(path("sentinel@0.1", JIT, m["jit"]))
    pin, cfg = which.split("-")
    return Rec(path("sentinel@0.1", f"pcrec_{CB if pin == 'cb' else OLD}_auto-{cfg}-simdna", m[which]))


def mode_sentinel():
    print("== sentinel closing/opening, same window (W2), per testee")
    for w in ("cb-caps", "cb-nocaps", "old-caps", "jit"):
        o, c = sen_load(w, "open"), sen_load(w, "close")
        keys = [k for k in o.cells if k in c.cells and o.med(k) and c.med(k)]
        r = [c.med(k) / o.med(k) for k in keys]
        so, sc = collections.defaultdict(float), collections.defaultdict(float)
        for k in keys:
            so[(k[0], k[2])] += o.med(k)
            sc[(k[0], k[2])] += c.med(k)
        sr = [sc[k] / so[k] for k in so]
        print(f"{w}: subject-cells n={len(r)} median {statistics.median(r):.4f} p5 {pct(r, .05):.3f} p95 {pct(r, .95):.3f} min {min(r):.3f} max {max(r):.3f}; "
              f"set-cells n={len(sr)} median {statistics.median(sr):.4f} min {min(sr):.3f} max {max(sr):.3f} |dev|>5%: {sum(abs(x - 1) > .05 for x in sr)}")
    print("\n== in-window cb / 614 (caps), opening and closing; patterns program-identical (v3) only")
    for kind in ("open", "close"):
        a, b = sen_load("cb-caps", kind), sen_load("old-caps", kind)
        allp = {p for p, f in a.comp}
        chg = sorted({p for (p, f), x in a.comp.items() if (p, f) in b.comp and x["engine_metadata"]["program_sha256_v3"] != b.comp[(p, f)]["engine_metadata"]["program_sha256_v3"]})
        ident = allp - set(chg)  # identical = no form of the pattern changed
        keys = [k for k in a.cells if k in b.cells and a.med(k) and b.med(k) and k[0] in ident]
        r = [a.med(k) / b.med(k) for k in keys]
        print(f"{kind}: identical patterns {len(ident)} of {len({p for p, f in a.comp})}; changed {chg}; subject-cells n={len(r)} cb/614 median {statistics.median(r):.4f} p5 {pct(r, .05):.3f} p95 {pct(r, .95):.3f}")
        # nocaps vs caps cb
    print("\n== cross-window control: the SAME pin 614d45eb3 / libpcre2 jit, W2 vs 2026-10-28 (sentinel@0.1)")
    old28 = {"open": "20261028T161100Z", "close": "20261028T224116Z"}
    jit28 = {"open": None, "close": None}
    fsj = sorted(glob.glob(f"{S}/sentinel@0.1/{JIT}/*20261028T*.jsonl"))
    fso = sorted(glob.glob(f"{S}/sentinel@0.1/pcrec_{OLD}_auto-caps-simdna/*20261028T*.jsonl"))
    fsn = sorted(glob.glob(f"{S}/sentinel@0.1/pcrec_{OLD}_auto-nocaps-simdna/*20261028T*.jsonl"))
    print("   10-28 614 caps files:", [f.split("__")[-1][:-6] for f in fso], "jit:", [f.split("__")[-1][:-6] for f in fsj])
    for name, f28, w in (("614 auto-caps", fso, "old-caps"), ("jit", fsj, "jit")):
        for i, kind in enumerate(("open", "close")):
            a = Rec(f28[i])  # the older window
            b = sen_load(w, kind)
            keys = [k for k in a.cells if k in b.cells and a.med(k) and b.med(k)]
            r = [b.med(k) / a.med(k) for k in keys]
            sa, sb = collections.defaultdict(float), collections.defaultdict(float)
            for k in keys:
                sa[(k[0], k[2])] += a.med(k)
                sb[(k[0], k[2])] += b.med(k)
            sr = [sb[k] / sa[k] for k in sa]
            print(f"{name} {kind}: W2/10-28 subject-cells n={len(r)} median {statistics.median(r):.4f} p5 {pct(r, .05):.3f} p95 {pct(r, .95):.3f}; set-cells median {statistics.median(sr):.4f} min {min(sr):.3f} max {max(sr):.3f}")
    # setup comparison (harness commit / driver flags) between the windows
    a = Rec(fso[0]).setup
    b = sen_load("old-caps", "open").setup
    for pth in (("run", "harness_commit"), ("run", "driver_build_flags"), ("environment", "kernel"), ("environment", "compiler")):
        def g(s):
            for p in pth:
                s = s.get(p, {}) if isinstance(s, dict) else {}
            return s
        print(pth, "\n   10-28:", str(g(a))[-160:], "\n   W2   :", str(g(b))[-160:])
    ca, cb_ = Rec(fso[0]).comp, sen_load("old-caps", "open").comp
    d = [cb_[k]["artifact_bytes"] - ca[k]["artifact_bytes"] for k in ca if k in cb_]
    print("614 sentinel artifact_bytes W2 - 10-28: median", statistics.median(d), "min", min(d), "max", max(d))
    same = sum(ca[k]["engine_metadata"]["program_sha256_v3"] == cb_[k]["engine_metadata"]["program_sha256_v3"] for k in ca if k in cb_)
    print("614 sentinel program_sha256_v3 identical across windows:", same, "of", len(d))


def mode_census():
    cen = census()
    for cfg in ("caps", "nocaps"):
        a, b = load_cap("old", cfg), load_cap("cb", cfg)
        tot = agree = same_n = chg_n = nocen = 0
        mism, refm = [], []
        byattr = collections.Counter()
        for k in sorted(set(a.comp) | set(b.comp)):
            x, y = a.comp.get(k), b.comp.get(k)
            if not x or not y:
                mism.append((k, "missing in one record"))
                continue
            if x["compile_outcome"] != "compiled" or y["compile_outcome"] != "compiled":
                if x["compile_outcome"] != y["compile_outcome"]:
                    refm.append((k, x["compile_outcome"], y["compile_outcome"]))
                continue
            tot += 1
            mx, my = x["engine_metadata"], y["engine_metadata"]
            same = mx["program_sha256_v3"] == my["program_sha256_v3"]
            same_n += same
            chg_n += (not same)
            c = cen.get(("capability", k[0], cfg, form_of(k)))
            if c is None:
                nocen += 1
                mism.append((k, "no census row"))
                continue
            cs = c["v3"] == "identical"
            de, dc = my["emit_bytes"] - mx["emit_bytes"], my["emit_code_bytes"] - mx["emit_code_bytes"]
            cd = (c["new"][0] - c["old"][0], c["new"][1] - c["old"][1]) if c["old"] and c["new"] else None
            if same != cs:
                mism.append((k, "identity differs", c["attr"]))
            elif same and (de, dc) != (0, 0):
                mism.append((k, "identical but bytes moved", de, dc))
            elif not same and cd and (de, dc) != cd:
                mism.append((k, "delta differs", (de, dc), cd, c["attr"]))
            else:
                agree += 1
                byattr[c["attr"]] += 1
        print(f"capability@0.4 {cfg}: compiled-both rows {tot}; v3 identical {same_n}, changed {chg_n}; agree with census (identity + emit/code deltas) {agree}; mismatches {len(mism)}; refusal movers {refm}")
        print("   agreeing rows by census attribution:", dict(byattr))
        for m in mism[:15]:
            print("    ", m)
        # emit byte offset vs census (bench's constant +7 B?)
    # constant offset check
    a, b = load_cap("old", "caps"), load_cap("cb", "caps")
    offs = collections.Counter()
    for k, x in b.comp.items():
        c = cen.get(("capability", k[0], "caps", form_of(k)))
        if c and x["compile_outcome"] == "compiled" and c["new"]:
            offs[x["engine_metadata"]["emit_bytes"] - c["new"][0]] += 1
    print("emit_bytes record minus census (cb32eda28, caps):", dict(offs.most_common(5)))
    # K134 size: emit delta distribution of k134-attributed rows
    d = collections.defaultdict(list)
    for k, x in b.comp.items():
        c = cen.get(("capability", k[0], "caps", form_of(k)))
        y = a.comp.get(k)
        if c and y and x["compile_outcome"] == "compiled" and y["compile_outcome"] == "compiled" and c["attr"] != "-":
            d[c["attr"]].append(x["engine_metadata"]["emit_bytes"] - y["engine_metadata"]["emit_bytes"])
    for at, v in d.items():
        print(f"   caps emit_bytes delta [{at}] n={len(v)} min {min(v)} median {statistics.median(v)} max {max(v)}")


def mode_answers():
    for cfg in ("caps", "nocaps"):
        a, b = load_cap("old", cfg), load_cap("cb", cfg)
        keys = sorted(set(a.cells) | set(b.cells))
        diff = [k for k in keys if a.cells[k]["o"] != b.cells[k]["o"]]
        nonexp = collections.Counter()
        for r, nm in ((a, OLD), (b, CB)):
            for k, c in r.cells.items():
                for o, n in c["o"].items():
                    if o != "matched-as-expected":
                        nonexp[(nm, o, k[0], k[1])] += n
        print(f"== {cfg}: match cells old {len(a.cells)} cb {len(b.cells)}; cells whose outcome multiset differs between pins: {len(diff)}")
        for k in diff[:10]:
            print("   DIFF", k, dict(a.cells[k]["o"]), dict(b.cells[k]["o"]))
        print("   non-expected outcomes (pin, outcome, pattern, subject: rows):")
        for k, n in sorted(nonexp.items()):
            print("    ", k, n)


def setgrain(cfg):
    """{(pat, regime, form): dict(old=[sums], cb=[sums], subjects, identity, attr)} over common clean subjects"""
    a, b = load_cap("old", cfg), load_cap("cb", cfg)
    cen = census()
    out = {}
    pats = sorted({k[0] for k in a.cells} | {k[0] for k in b.cells})
    for p in pats:
        for rg in (LARGE, SHORT):
            frm = "plain"
            subj = [s for s in a.subjects(p, rg, frm) if s in set(b.subjects(p, rg, frm))]
            subj = [s for s in subj if a.clean((p, s, rg, frm)) and b.clean((p, s, rg, frm))]
            if not subj:
                continue
            sa, sb = a.setsum(p, rg, frm, subj), b.setsum(p, rg, frm, subj)
            if not sa or not sb:
                continue
            x, y = a.comp.get((p, "plain")), b.comp.get((p, "plain"))
            ident = None
            if x and y and x["compile_outcome"] == "compiled" and y["compile_outcome"] == "compiled":
                ident = x["engine_metadata"]["program_sha256_v3"] == y["engine_metadata"]["program_sha256_v3"]
            c = cen.get(("capability", p, cfg, "plain"), {})
            out[(p, rg)] = dict(old=sa, cb=sb, subj=subj, ident=ident, attr=c.get("attr", "?"), n=len(subj), x=x, y=y)
    return out


def mode_sets():
    for cfg in ("caps", "nocaps"):
        g = setgrain(cfg)
        print(f"\n===== {cfg}: set cells (clean common subjects) cb32eda28 / 614d45eb3, 5-trial per-trial sums, median ratio and per-trial ranges")
        groups = collections.defaultdict(list)
        for (p, rg), v in sorted(g.items()):
            r = statistics.median(v["cb"]) / statistics.median(v["old"])
            groups[(v["attr"] if v["ident"] is False or v["attr"] != "-" else "-", rg)].append((p, rg, r, v))
        for (at, rg), lst in sorted(groups.items()):
            rs = [x[2] for x in lst]
            print(f"-- attribution {at} / {rg}: n={len(lst)} median ratio {statistics.median(rs):.4f} min {min(rs):.3f} max {max(rs):.3f}")
            if at != "-":
                for p, rg2, r, v in sorted(lst, key=lambda t: t[2]):
                    mo, mc = statistics.median(v["old"]), statistics.median(v["cb"])
                    print(f"     {p:44s} x{r:.3f}  old {mo:14.1f} [{min(v['old']):.0f}-{max(v['old']):.0f}]  cb {mc:14.1f} [{min(v['cb']):.0f}-{max(v['cb']):.0f}] n_subj={v['n']}")


def mode_null():
    for cfg in ("caps", "nocaps"):
        g = setgrain(cfg)
        print(f"\n===== {cfg}: program-identical set cells (v3), cb/614 ratio")
        for rg in (LARGE, SHORT, None):
            lst = [(p, r, statistics.median(v["cb"]) / statistics.median(v["old"]), v) for (p, r), v in g.items() if v["ident"] and (rg is None or r == rg)]
            ds = sorted((x[2] - 1) * 100 for x in lst)
            if not ds:
                continue
            print(f" {rg or 'both'}: n={len(ds)} median {statistics.median(ds):+.2f}% p5 {pct(ds, .05):+.2f} p95 {pct(ds, .95):+.2f} min {ds[0]:+.2f} max {ds[-1]:+.2f}; |d|>5%: {sum(abs(x) > 5 for x in ds)}; >10%: {sum(abs(x) > 10 for x in ds)}; >20%: {sum(abs(x) > 20 for x in ds)}")
            worst = sorted(lst, key=lambda t: -abs(t[2] - 1))[:6]
            for p, r, ratio, v in worst:
                print(f"     {p:40s} {r[:5]} x{ratio:.3f} old [{min(v['old']):.0f}-{max(v['old']):.0f}] cb [{min(v['cb']):.0f}-{max(v['cb']):.0f}]")


def mode_k134():
    cen = census()
    for cfg in ("caps", "nocaps"):
        g = setgrain(cfg)
        print(f"\n===== {cfg}: K134 (abi93-k134) rows: set-cell ratios and the identical-control ratio in the same regime")
        for rg in (LARGE, SHORT):
            k = [(p, statistics.median(v["cb"]) / statistics.median(v["old"])) for (p, r), v in g.items() if r == rg and v["attr"] == "abi93-k134"]
            ctl = [statistics.median(v["cb"]) / statistics.median(v["old"]) for (p, r), v in g.items() if r == rg and v["ident"]]
            kr = [x[1] for x in k]
            print(f" {rg}: K134 n={len(k)} median x{statistics.median(kr):.4f} min x{min(kr):.3f} max x{max(kr):.3f} | identical control n={len(ctl)} median x{statistics.median(ctl):.4f}")
            for p, r in sorted(k, key=lambda t: t[1]):
                v = g[(p, rg)]
                print(f"     {p:40s} x{r:.3f}  old {statistics.median(v['old']):.1f} cb {statistics.median(v['cb']):.1f}")


def mode_qs():
    for cfg in ("caps", "nocaps"):
        a, b = load_cap("old", cfg), load_cap("cb", cfg)
        print(f"\n===== {cfg}: the I-172 cells")
        for p in ("dup-param-detect", "balanced-parens-rec"):
            pass
        for s in ("t-qs-1m", "t-qs-nearmiss-256k"):
            for p in sorted({k[0] for k in b.cells if k[1] == s}):
                k = (p, s, LARGE, "plain")
                ca, cb_ = a.cells.get(k), b.cells.get(k)
                if not ca or not cb_:
                    continue
                ma, mb = a.med(k), b.med(k)
                print(f"  {p:42s} {s:20s} old {ma if ma is None else round(ma,1)} {sorted(round(v) for v in ca['t'].values())} {dict(ca['o'])} | cb {mb if mb is None else round(mb,1)} {sorted(round(v) for v in cb_['t'].values())} {dict(cb_['o'])} | ratio {'' if not (ma and mb) else round(mb/ma,3)}")
        # ids from the compile rows
        for k in (("dup-param-detect", "plain"), ("dup-param-detect", "whole-subject")):
            for nm, r in (("old", a), ("cb", b)):
                x = r.comp.get(k)
                if x and x["compile_outcome"] == "compiled":
                    m = x["engine_metadata"]
                    print("   compile", nm, k, {f: m.get(f) for f in ("engine", "engine_sel", "dfa_prefilter", "req_handoff", "req_why", "frame_capacity", "resume_frames", "trail_frames", "emit_bytes", "emit_code_bytes", "vm_program_bytes", "vm_frameless", "vm_trail_check")})
        for k in (("dup-param-detect", "t-qs-1m", LARGE, "plain"),):
            for nm, r in (("old", a), ("cb", b)):
                c = r.cells[k]
                print("   ", nm, k, "bytes", c["bytes"], "iters", c["iters"])
        # expected outcomes / the other 70 patterns on the qs subjects
        rows = []
        for p in sorted({k[0] for k in b.cells if k[1] == "t-qs-1m"}):
            k = (p, "t-qs-1m", LARGE, "plain")
            ma, mb = a.med(k), b.med(k)
            if ma and mb:
                rows.append((mb / ma, p))
        rs = [r for r, p in rows]
        print(f"   all patterns on t-qs-1m cb/old: n={len(rs)} median {statistics.median(rs):.4f} min {min(rs):.3f} max {max(rs):.3f}")


def mode_subj():
    """per-subject cb/614 ratios for the named movers (both configs), plus the compile stamps on both pins"""
    pats = ["utf8-lead-no-cont", "hex8-bounded", "wild-codegrammar-json-array-begin", "wild-codegrammar-json-object-begin", "keyword-prefix-order",
            "wild-secrets-username-password-pair", "wild-waf-crs-942270-union-select", "floor-byte"]
    sizes = {}
    for cfg in ("caps", "nocaps"):
        a, b = load_cap("old", cfg), load_cap("cb", cfg)
        for p in pats:
            for nm, r in (("614", a), ("cb ", b)):
                x = r.comp.get((p, "plain"))
                if x and x["compile_outcome"] == "compiled":
                    m = x["engine_metadata"]
                    print(f"[{cfg}] {p:38s} {nm} " + " ".join(f"{f}={m.get(f)}" for f in ("engine", "dfa_scan", "dfa_scan_edge", "dfa_prefilter", "dfa_start", "req_handoff", "req_why", "req_run", "req_byte", "emit_bytes", "vm_program_bytes")))
            for rg in (LARGE, SHORT):
                rows = []
                for s in sorted({k[1] for k in a.cells if k[0] == p and k[2] == rg}):
                    k = (p, s, rg, "plain")
                    ma, mb = a.med(k), b.med(k)
                    if ma and mb:
                        rows.append((s, ma, mb, a.cells[k]["bytes"]))
                tot_a = sum(r[1] for r in rows)
                top = sorted(rows, key=lambda r: -r[1])[:6] if rg == LARGE else sorted(rows, key=lambda r: -abs(r[2] - r[1]))[:5]
                rat = [r[2] / r[1] for r in rows]
                print(f"   {rg}: subjects {len(rows)}; per-subject ratio median {statistics.median(rat):.3f} min {min(rat):.3f} max {max(rat):.3f}")
                for s, ma, mb, by in top:
                    print(f"      {s:28s} {by if by is None else int(by):>9} B  614 {ma:12.1f} ns -> cb {mb:12.1f} ns  x{mb/ma:.3f}" + ("" if not by else f"  ({mb/by:.3f} ns/B vs {ma/by:.3f})"))



def mode_k134call():
    """K134: the short-regime set-sum delta per subject (a per-call ns term), and whether the large regime moves per byte"""
    for cfg in ("caps", "nocaps"):
        g = setgrain(cfg)
        print(f"== {cfg}: abi93-k134 rows, short-subject-search: (cb - 614) set-sum / n_subjects = ns per call; identical-control spread of the same quantity")
        ctl = [(statistics.median(v["cb"]) - statistics.median(v["old"])) / v["n"] for (p, r), v in g.items() if r == SHORT and v["ident"]]
        print(f"   identical control n={len(ctl)}: median {statistics.median(ctl):+.3f} ns/call, p5 {pct(ctl, .05):+.3f}, p95 {pct(ctl, .95):+.3f}, min {min(ctl):+.3f}, max {max(ctl):+.3f}")
        for (p, r), v in sorted(g.items()):
            if r == SHORT and v["attr"] == "abi93-k134":
                d = (statistics.median(v["cb"]) - statistics.median(v["old"])) / v["n"]
                print(f"   {p:40s} {d:+.3f} ns/call over {v['n']} subjects (old {statistics.median(v['old'])/v['n']:.2f} -> cb {statistics.median(v['cb'])/v['n']:.2f} ns/call mean)")


def mode_xwin():
    """cross-window control: the SAME pin 614d45eb3, W2 (capability@0.4, 2026-11-01) against capability@0.3 (2026-10-28), common clean subject-cells"""
    for cfg in ("caps", "nocaps"):
        old = Rec(path("capability@0.3", tid("old", cfg), "20261028T"))
        new = load_cap("old", cfg)
        keys = [k for k in old.cells if k in new.cells and old.clean(k) and new.clean(k) and old.med(k) and new.med(k)]
        for rg in (LARGE, SHORT):
            r = [new.med(k) / old.med(k) for k in keys if k[2] == rg]
            ss = collections.defaultdict(lambda: [0.0, 0.0])
            for k in keys:
                if k[2] == rg:
                    ss[k[0]][0] += old.med(k)
                    ss[k[0]][1] += new.med(k)
            sr = [v[1] / v[0] for v in ss.values()]
            print(f"{cfg} {rg}: 614d45eb3 W2 / 10-28; subject-cells n={len(r)} median {statistics.median(r):.4f} p5 {pct(r, .05):.3f} p95 {pct(r, .95):.3f}; set-cells n={len(sr)} median {statistics.median(sr):.4f} p5 {pct(sr, .05):.3f} p95 {pct(sr, .95):.3f} min {min(sr):.3f} max {max(sr):.3f} |dev|>5%: {sum(abs(x - 1) > .05 for x in sr)}")
        # program identity and harness fields
        same = sum(old.comp[k]["engine_metadata"]["program_sha256_v3"] == new.comp[k]["engine_metadata"]["program_sha256_v3"] for k in old.comp if k in new.comp and old.comp[k]["compile_outcome"] == "compiled" and new.comp[k]["compile_outcome"] == "compiled")
        tot = sum(1 for k in old.comp if k in new.comp and old.comp[k]["compile_outcome"] == "compiled" and new.comp[k]["compile_outcome"] == "compiled")
        d = [new.comp[k]["artifact_bytes"] - old.comp[k]["artifact_bytes"] for k in old.comp if k in new.comp and old.comp[k]["compile_outcome"] == "compiled"]
        print(f"   {cfg}: v3-identical compile rows {same} of {tot}; artifact_bytes delta median {statistics.median(d)} min {min(d)} max {max(d)}; harness {old.setup['run']['harness_commit'][:8]} -> {new.setup['run']['harness_commit'][:8]}")


if __name__ == "__main__":
    globals()["mode_" + sys.argv[1]]()
