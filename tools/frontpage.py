#!/usr/bin/env python3
"""tools/frontpage.py -- the public front page's generator ([B127]).

Rewrites ONLY the regions between `<!-- frontpage:NAME:begin -->` and
`<!-- frontpage:NAME:end -->` in README.md and docs/methodology.md (hand-
written prose outside the markers is preserved byte for byte), writes the
speedup-distribution SVG and a provenance TSV listing every record path a
number on the page was reduced from. Every number is computed here from the
canonical store; none is typed anywhere.

THE METRIC (manager's ruling, [B127]):
  * pcrec's representative is `pcrec-auto` (config tail `auto-caps-simdna`,
    or `..._utf8` on the utf8 set) at the pin named on the command line.
  * A CASE = one (pattern, regime) PLAIN-form set-grain cell where BOTH
    sides have a numeric set-grain median. The cell arithmetic is
    `pcrecbench.reduce.cells_from_record` / `reduce_set_cell`, the
    reporter's own; nothing is reimplemented here.
  * speedup = competitor median / pcrec median (> 1: pcrec faster).
  * TIE when the two cells' closed [min, max] trial ranges overlap;
    otherwise a win (pcrec faster) or a loss.
  * excluded = a pair in the universe (every (pattern, regime) any selected
    testee has a cell for) that is not a case. Attributed to the PCREC side
    first, else the competitor's: wrong answer / gave up / unsupported or
    refused (compile row) / not measured.
  * headline win rate = wins / (wins + losses + ties) over all pairs.
  * only `measured` records; the latest per testee (pcrec: the given pin);
    one machine.
  * rounding: Decimal ROUND_HALF_EVEN to fixed significant digits, one
    function (`sig`), used for every displayed ratio.

No new dependency (stdlib + the repo's own `pcrecbench.reduce`).
"""

import argparse
import csv
import difflib
import hashlib
import math
import os
import re
import statistics
import sys
from decimal import Decimal, ROUND_HALF_EVEN

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from pcrecbench import reduce as R  # noqa: E402

PCREC_TAILS = ("auto-caps-simdna", "auto-caps-simdna_utf8")
REASONS = ("wrong", "gave-up", "unsupported", "not-measured")
REASON_TEXT = {"wrong": "wrong answer", "gave-up": "gave up",
               "unsupported": "unsupported or refused",
               "not-measured": "not measured"}


# ------------------------------------------------------------- formatting

def sig(x, n=3):
    """x to n significant digits, half-even, as a plain decimal string."""
    if x is None:
        return "n/a"
    d = Decimal(repr(float(x)))
    if d == 0:
        return "0"
    exp = d.adjusted() - (n - 1)
    q = d.quantize(Decimal(1).scaleb(exp), rounding=ROUND_HALF_EVEN)
    s = format(q, "f")
    return s


def times(x):
    return "×" + sig(x)


def pct(num, den):
    if not den:
        return "n/a"
    d = (Decimal(num) * 100 / Decimal(den)).quantize(
        Decimal("0.1"), rounding=ROUND_HALF_EVEN)
    return format(d, "f") + "%"


def dur(ns):
    if ns is None:
        return "n/a"
    for unit, div in (("s", 1e9), ("ms", 1e6), ("µs", 1e3)):
        if ns >= div:
            return sig(ns / div) + " " + unit
    return sig(ns) + " ns"


# ------------------------------------------------------------------ store

def index_rows(store):
    with open(os.path.join(store, "index.tsv"), encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def config_tail(testee_id):
    parts = testee_id.split("_", 2)
    return parts[2] if len(parts) == 3 else ""


def engine_of(testee_id):
    return testee_id.split("_", 1)[0]


def latest_measured(rows, subbench, version):
    best = {}
    for r in rows:
        if r["subbench"] != subbench or r["version"] != version \
                or r["status"] != "measured":
            continue
        t = r["testee_id"]
        if t not in best or r["timestamp"] > best[t]["timestamp"]:
            best[t] = r
    return best


def pick_testees(rows, setid, pin):
    """-> (pcrec_row, [competitor rows]) for set@version. pin None: the
    latest pcrec-auto record of any pin."""
    sb, ver = setid.split("@")
    best = latest_measured(rows, sb, ver)
    pc = [r for t, r in best.items() if engine_of(t) == "pcrec"
          and config_tail(t) in PCREC_TAILS
          and (pin is None or t.split("_")[1].startswith(pin[:8]))]
    if not pc:
        return None, []
    pc.sort(key=lambda r: r["timestamp"])
    pcrec = pc[-1]
    comps = [r for t, r in sorted(best.items()) if engine_of(t) != "pcrec"
             and r["machine_id"] == pcrec["machine_id"]]
    return pcrec, comps


class Summary:
    """One record, reduced: plain-form set cells + compile outcomes."""

    def __init__(self, store, row):
        self.row = row
        self.path = "store/" + row["path"]
        setup, rows = R.read_record(os.path.join(store, row["path"]))
        self.setup = setup
        te = setup["testee"]
        self.testee_id = te["testee_id"]
        self.te = te
        self.env = setup["environment"]
        self.timestamp = setup["run"]["timestamp"]
        self.content_hash = setup["content_hash"]["value"]
        self.ta = setup.get("trial_agreement") or {}
        self.regimes = setup["subbench"].get("regimes", [])
        self.cells = {}
        self.max_trials = 0
        for (pid, regime, form), by_subj in R.cells_from_record(rows).items():
            if form != "plain":
                continue
            c = R.reduce_set_cell(by_subj)
            self.cells[(pid, regime)] = dict(
                median=c.median_ns, lo=c.min_ns, hi=c.max_ns,
                n_wrong=c.n_wrong, n_gave_up=c.n_gave_up,
                n_trials=c.n_trials, n_subjects=c.n_subjects)
            self.max_trials = max(self.max_trials, c.n_trials)
        self.calibration_target_ns = None
        for r in rows:
            if r.get("kind") == "match" and r.get("calibration"):
                self.calibration_target_ns = r["calibration"].get("target_ns")
                break
        per = {}
        self.compile_outcome = {}
        for r in rows:
            if r.get("kind") != "compile" or r.get("form") not in (None, "plain"):
                continue
            pid = r["pattern_id"]
            self.compile_outcome.setdefault(pid, r["compile_outcome"])
            if r["compile_outcome"] == "compiled":
                per.setdefault(pid, []).append(r["cost"]["total_ns"])
        self.compile_ns = {p: statistics.median(v) for p, v in per.items()}
        self.compile_class = next((r.get("cost_class") for r in rows
                                   if r.get("kind") == "compile"), None)

    def numeric(self, key):
        c = self.cells.get(key)
        return c if c and c["median"] is not None else None

    def reason(self, key):
        """Why this side has no number for key."""
        c = self.cells.get(key)
        if c is not None:
            if c["n_wrong"] > 0:
                return "wrong"
            if c["n_gave_up"] > 0:
                return "gave-up"
            return "not-measured"
        out = self.compile_outcome.get(key[0])
        if out in ("unsupported-by-declaration", "did-not-compile"):
            return "unsupported"
        return "not-measured"


# ---------------------------------------------------------------- compare

def classify(pc, cp):
    """-> speedup, class ('win'|'loss'|'tie') for two numeric cells."""
    sp = cp["median"] / pc["median"]
    if max(pc["lo"], cp["lo"]) <= min(pc["hi"], cp["hi"]):
        return sp, "tie"
    return sp, ("win" if cp["median"] > pc["median"] else "loss")


def compare(pcrec, comp, universe):
    cases, excl = [], {"pcrec": dict.fromkeys(REASONS, 0),
                       "engine": dict.fromkeys(REASONS, 0)}
    for key in sorted(universe):
        a, b = pcrec.numeric(key), comp.numeric(key)
        if a and b:
            sp, cl = classify(a, b)
            cases.append(dict(key=key, speedup=sp, cls=cl, pcrec=a, comp=b))
        elif not a:
            excl["pcrec"][pcrec.reason(key)] += 1
        else:
            excl["engine"][comp.reason(key)] += 1
    return cases, excl


def stats(cases):
    sps = [c["speedup"] for c in cases]
    n = len(sps)
    return dict(
        n=n, win=sum(c["cls"] == "win" for c in cases),
        loss=sum(c["cls"] == "loss" for c in cases),
        tie=sum(c["cls"] == "tie" for c in cases),
        median=statistics.median(sps) if n else None,
        geo=math.exp(sum(math.log(s) for s in sps) / n) if n else None)


def excl_text(excl):
    parts = []
    for side, label in (("pcrec", "pcrec side"), ("engine", "engine side")):
        bits = [f"{excl[side][k]} {REASON_TEXT[k]}" for k in REASONS
                if excl[side][k]]
        if bits:
            parts.append(label + ": " + ", ".join(bits))
    return "; ".join(parts) if parts else "none"


PCREC_BASE_VERSION = "0.2.0-beta"   # lib/pcrec.h PCREC_VERSION at the pin (checked by hand)

# (engine_name, engine_mode) -> (label template, kind, kind source). {v} = the
# record's engine_version; a "_utf8" testee gets " UTF-8" appended. An unmapped
# testee is a hard error (label_entry), never a fallback.
ENGINES = {
    ("libpcre2", "interp"): ("PCRE2 {v} interpreter", "interpreter (backtracking)",
        "testees/pcre2/CLAUDE.md; record automaton_class backtracking"),
    ("libpcre2", "jit"): ("PCRE2 {v} JIT", "JIT",
        "testees/pcre2/CLAUDE.md; record execution_model eager-jit"),
    ("libpcre2", "dfa"): ("PCRE2 {v} DFA", "DFA",
        "testees/pcre2/CLAUDE.md pcre2-dfa section (pcre2_dfa_match, breadth-first scan)"),
    ("re2", "default"): ("RE2 {v}", "automata (lazy DFA etc.)",
        "testees/re2/CLAUDE.md line 44: RE2's DFA is built lazily at first match"),
    ("re2", "longest"): ("RE2 {v} (longest-match)", "automata (lazy DFA etc.)",
        "testees/re2/CLAUDE.md line 44; mode longest = set_longest_match(true)"),
    ("rust", "default"): ("Rust regex {v}", "automata (lazy DFA etc.)",
        "testees/rust/CLAUDE.md line 104: the crate's lazy DFA"),
    ("oniguruma", "default"): ("Oniguruma {v}", "interpreter (backtracking)",
        "testees/onig/CLAUDE.md (a): interpretive backtracking engine"),
    ("tre", "default"): ("TRE {v}", "interpreter (POSIX matcher, backtracking fallback)",
        "testees/tre/CLAUDE.md: TNFA / backtracking form built in one call; record automaton_class hybrid"),
    ("vectorscan", "block-nosom"): ("Vectorscan {v} (no SOM)", "automata (SIMD multi-pattern)",
        "record automaton_class simd-multipattern; testees/vectorscan/CLAUDE.md"),
    ("vectorscan", "block-som"): ("Vectorscan {v} (SOM)", "automata (SIMD multi-pattern)",
        "record automaton_class simd-multipattern; testees/vectorscan/CLAUDE.md"),
    ("pcrec", "auto"): ("pcrec " + PCREC_BASE_VERSION + "+{v}", "AOT",
        "record execution_model compiled-aot"),
}


def label_entry(s):
    key = (s.te["engine_name"], s.te["engine_mode"])
    ent = ENGINES.get(key)
    if ent is None:
        raise SystemExit(f"frontpage: no ENGINES entry for testee {s.testee_id} "
                         f"(engine_name={key[0]}, engine_mode={key[1]}); add one "
                         f"with a kind source")
    return ent


def label(s):
    return (label_entry(s)[0].format(v=s.te["engine_version"]) +
            (" UTF-8" if s.testee_id.endswith("_utf8") else ""))


def kind(s):
    return label_entry(s)[1]


def big(x, n=3):
    """n significant digits, half-even, thousands separators."""
    ip, dot, fp = sig(x, n).partition(".")
    return f"{int(ip):,}" + dot + fp


def slower_by(speedup):
    return "×" + big(1.0 / speedup)


class Analysis:
    def __init__(self, store, setid, pin, rows):
        self.setid = setid
        prow, crows = pick_testees(rows, setid, pin)
        if prow is None:
            raise SystemExit(f"frontpage: no measured pcrec-auto record for "
                             f"{setid}" + (f" at pin {pin}" if pin else ""))
        self.pcrec = Summary(store, prow)
        self.comps = [Summary(store, r) for r in crows]
        self.universe = set(self.pcrec.cells)
        for c in self.comps:
            self.universe |= set(c.cells)
        for c in self.comps + [self.pcrec]:
            self.universe |= {(p, rg) for (p, rg) in c.cells}
        self.per = []
        for c in self.comps:
            cases, excl = compare(self.pcrec, c, self.universe)
            self.per.append((c, cases, excl, stats(cases)))
        self.all_cases = [x for _, cs, _, _ in self.per for x in cs]
        self.total = stats(self.all_cases)

    def summaries(self):
        return [self.pcrec] + self.comps

    def families(self):
        sb = self.setid.split("@")[0]
        p = os.path.join(ROOT, "bench", sb, "provenance.tsv")
        if not os.path.exists(p):
            return {}
        with open(p, encoding="utf-8") as f:
            return {r["pattern_id"]: r["family"]
                    for r in csv.DictReader(f, delimiter="\t")}


# ------------------------------------------------------------- renderers

def md_table(head, body, align=None):
    align = align or ["---"] * len(head)
    out = ["| " + " | ".join(head) + " |",
           "|" + "|".join(a if a.startswith(":") or a.endswith(":") else a
                          for a in align) + "|"]
    for r in body:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out)


def date_of(s):
    return s.timestamp[:10]


def render_headline(an):
    t = an.total
    pairs = t["win"] + t["loss"] + t["tie"]
    pc = an.pcrec
    ds = sorted(date_of(c) for c in an.comps)
    names = ", ".join(sorted({c.te["engine_name"] for c in an.comps}))
    excluded = sum(sum(v.values()) for _, _, ex, _ in an.per for v in ex.values())
    return (
        f"On `{an.setid}` ({len(an.universe)} pattern-regime cells), "
        f"{label(pc)} (config `pcrec-auto`, measured "
        f"{date_of(pc)}) is faster in {t['win']} of {pairs} compared cases "
        f"({pct(t['win'], pairs)}), tied in {t['tie']} ({pct(t['tie'], pairs)}) "
        f"and slower in {t['loss']} ({pct(t['loss'], pairs)}); a further "
        f"{excluded} pairs have no verified number on one side and are "
        f"excluded (counted below). Competitors: "
        f"{len(an.comps)} configurations of {len(set(c.te['engine_name'] for c in an.comps))} "
        f"engines ({names}). Match time, compile excluded."
        f"[^rate]\n\n"
        f"[^rate]: Win rate = wins / (wins + losses + ties) over all "
        f"competitor × case pairs; a case is one (pattern, regime) cell where "
        f"both engines produced a verified number; a tie is overlapping "
        f"[min, max] trial ranges. Competitor records were measured "
        f"{ds[0]} to {ds[-1]}, pcrec's on {date_of(pc)}, all on one machine "
        f"(`{pc.env['machine_id']}`)."
    )


def render_table(an):
    head = ["Competitor", "Kind", "Cases", "pcrec wins", "Losses", "Ties",
            "Median speedup", "Geo-mean speedup", "Excluded"]
    body = []
    for c, cases, excl, st in an.per:
        ex = sum(sum(v.values()) for v in excl.values())
        body.append([label(c), kind(c), st["n"], st["win"], st["loss"],
                     st["tie"], times(st["median"]) if st["n"] else "n/a",
                     times(st["geo"]) if st["n"] else "n/a",
                     f"{ex} ({excl_text(excl)})" if ex else "0"])
    t = an.total
    body.append(["**all pairs**", "", t["n"], t["win"], t["loss"], t["tie"],
                 times(t["median"]), times(t["geo"]), ""])
    return (md_table(head, body, ["---", "---", "--:", "--:", "--:", "--:",
                                  "--:", "--:", "---"]) +
            "\n\nSpeedup = competitor median ÷ pcrec median, per case "
            "(> 1 means pcrec is faster); the median and geometric mean run "
            "over all of that engine's cases, ties included. Excluded cases "
            "are counted, never dropped silently; a pair failing on both "
            "sides is attributed to the pcrec side.")


# ------------------------------------------------------------------- SVG

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_svg(an):
    W, left, right, top = 880, 300, 30, 46
    rowh = 44
    rows = [(c, cases) for c, cases, _, _ in an.per if cases]
    H = top + rowh * len(rows) + 62
    vals = [x["speedup"] for _, cs in rows for x in cs]
    lo = math.floor(math.log10(min(vals + [1.0])))
    hi = math.ceil(math.log10(max(vals + [1.0])))
    if hi == lo:
        hi += 1
    px = lambda v: left + (math.log10(v) - lo) / (hi - lo) * (W - left - right)
    bg, fg, grid = "#ffffff", "#1f2328", "#d0d7de"
    cw, cl, ct = "#0b66b2", "#c4510a", "#6e7781"
    ref = "#8250df"   # the 1x line and the median bars
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" role="img" aria-label="Distribution of '
         f'per-case speedup of pcrec over each competitor engine, log scale">',
         f'<rect width="{W}" height="{H}" fill="{bg}"/>',
         f'<text x="16" y="24" font-family="sans-serif" font-size="14" '
         f'font-weight="bold" fill="{fg}">pcrec speedup per case, '
         f'{esc(an.setid)} (competitor ÷ pcrec; right of 1× = pcrec faster)'
         f'</text>']
    for e in range(lo, hi + 1):
        x = px(10.0 ** e)
        o.append(f'<line x1="{x:.1f}" y1="{top - 8}" x2="{x:.1f}" '
                 f'y2="{top + rowh * len(rows)}" stroke="{grid}" '
                 f'stroke-width="1"/>')
        lab = f"{10 ** e}×" if e >= 0 else f"1/{10 ** -e}×"
        o.append(f'<text x="{x:.1f}" y="{top + rowh * len(rows) + 18}" '
                 f'text-anchor="middle" font-family="sans-serif" '
                 f'font-size="12" fill="{fg}">{lab}</text>')
    x1 = px(1.0)
    o.append(f'<line x1="{x1:.1f}" y1="{top - 8}" x2="{x1:.1f}" '
             f'y2="{top + rowh * len(rows)}" stroke="{ref}" stroke-width="2.5" '
             f'stroke-dasharray="6 3"/>')
    for i, (c, cases) in enumerate(rows):
        cy = top + rowh * i + rowh / 2
        o.append(f'<text x="{left - 12}" y="{cy + 4:.1f}" text-anchor="end" '
                 f'font-family="sans-serif" font-size="12" fill="{fg}">'
                 f'{esc(label(c))} (n={len(cases)})</text>')
        sps = sorted(x["speedup"] for x in cases)
        if len(sps) >= 2:
            q = statistics.quantiles(sps, n=4, method="inclusive")
            o.append(f'<rect x="{px(q[0]):.1f}" y="{cy - 11:.1f}" '
                     f'width="{max(px(q[2]) - px(q[0]), 1):.1f}" height="22" '
                     f'fill="none" stroke="{fg}" stroke-width="1.2"/>')
        med = statistics.median(sps)
        o.append(f'<line x1="{px(med):.1f}" y1="{cy - 14:.1f}" '
                 f'x2="{px(med):.1f}" y2="{cy + 14:.1f}" stroke="{ref}" '
                 f'stroke-width="3.5"/>')
        for j, x in enumerate(cases):
            h = int(hashlib.sha256(f"{c.testee_id}{x['key']}".encode())
                    .hexdigest()[:4], 16)
            jy = cy + ((h % 17) - 8) * 1.1
            col = {"win": cw, "loss": cl, "tie": ct}[x["cls"]]
            o.append(f'<circle cx="{px(x["speedup"]):.1f}" cy="{jy:.1f}" '
                     f'r="2.6" fill="{col}" fill-opacity="0.75"/>')
    ly = H - 16
    for k, (col, txt) in enumerate(((cw, "win (pcrec faster)"),
                                    (cl, "loss"), (ct, "tie (ranges overlap)"))):
        lx = left + k * 190
        o.append(f'<circle cx="{lx}" cy="{ly - 4}" r="4" fill="{col}"/>'
                 f'<text x="{lx + 10}" y="{ly}" font-family="sans-serif" '
                 f'font-size="12" fill="{fg}">{txt}</text>')
    o.append(f'<text x="16" y="{ly}" font-family="sans-serif" font-size="12" '
             f'fill="{ref}">purple = 1×, median; box = quartiles</text>')
    o.append("</svg>")
    return "\n".join(o) + "\n"


# ------------------------------------------------------------------ losses

def load_why(path):
    out = []
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader((ln for ln in f if not ln.startswith("#")),
                                delimiter="\t"):
            out.append(r)
    return out


def norm(s):
    return re.sub(r"\s+", " ", s)


def why_for(why, pattern, engine, regime):
    for w in why:
        if w["pattern_id"] not in (pattern, "*"):
            continue
        if w["engine"] not in (engine, "*"):
            continue
        if w.get("regime") not in ("", "*", regime, None):
            continue
        p = os.path.join(ROOT, w["cite"])
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                if norm(w["quote"]) in norm(f.read()):
                    return f'"{w["quote"]}" ([{w["cite"]}]({w["cite"]}))'
        raise SystemExit(f"frontpage: why row for {pattern}/{engine} cites "
                         f"{w['cite']} but the quote is not found there")
    return "cause not yet analysed"


def render_losses(an, why, top=20):
    fam = an.families()
    losses = [(x["speedup"], c, x) for c, cases, _, _ in an.per
              for x in cases if x["cls"] == "loss"]
    losses.sort(key=lambda t: (t[0], t[1].testee_id, t[2]["key"]))
    n_loss = len(losses)
    worst = losses[:top]
    byfam = {}
    for sp, c, x in worst:
        byfam.setdefault(fam.get(x["key"][0], "(no family metadata)"),
                         []).append((sp, c, x))
    note = ""
    if any("block-nosom" in c.testee_id for _, c, _ in worst):
        note = (" Vectorscan's `nosom` configuration reports only match or no "
                "match and its driver stops at the first match "
                "(testees/vectorscan/CLAUDE.md), so on a subject that matches "
                "it does less work than an engine that reports a span; read "
                "its rows with that in mind.")
    out = [f"The {len(worst)} worst of {n_loss} losing cases across all "
           f"competitors (pcrec slower, trial ranges disjoint; \"slower by\" is "
           f"pcrec median ÷ competitor median), "
           f"grouped by pattern family; families ordered by their worst case." + note]
    for f_, items in sorted(byfam.items(), key=lambda kv: kv[1][0][0]):
        out.append(f"\n**{f_}**\n")
        body = [[f"`{x['key'][0]}`", x["key"][1], label(c),
                 slower_by(sp), why_for(why, x["key"][0], c.te["engine_name"],
                                    x["key"][1])]
                for sp, c, x in items]
        out.append(md_table(["Pattern", "Regime", "Engine", "pcrec slower by", "Why"],
                            body, ["---", "---", "---", "--:", "---"]))
    # losses per family, all losses
    agg = {}
    for _, c, x in losses:
        agg.setdefault(fam.get(x["key"][0], "(no family metadata)"), 0)
        agg[fam.get(x["key"][0], "(no family metadata)")] += 1
    tot = {}
    for _, cases, _, _ in an.per:
        for x in cases:
            f_ = fam.get(x["key"][0], "(no family metadata)")
            tot[f_] = tot.get(f_, 0) + 1
    out.append("\nLosses by family, over every case:\n")
    out.append(md_table(["Family", "Cases", "Losses", "Loss rate"],
                        [[f_, tot[f_], agg.get(f_, 0), pct(agg.get(f_, 0), tot[f_])]
                         for f_ in sorted(tot, key=lambda k: -agg.get(k, 0) / tot[k])],
                        ["---", "--:", "--:", "--:"]))
    return "\n".join(out)


# ------------------------------------------------------------ methodology

def distinct(vals):
    seen = []
    for v in vals:
        if v not in seen:
            seen.append(v)
    return seen


def render_env(an):
    ss = an.summaries()
    e = lambda k: "; ".join(distinct(str(s.env.get(k)) for s in ss))
    pin = distinct(f"{s.env.get('pinning', {}).get('mode')} cpu {s.env.get('pinning', {}).get('cpu')}"
                   for s in ss)
    return md_table(["Item", "Value (from the records' `environment` blocks)"], [
        ["Machine", f"`{e('machine_id')}` ({e('hostname')})"],
        ["CPU", f"{e('cpu_model_raw')}, {e('cores')} hardware threads"],
        ["Kernel", e("kernel_raw")],
        ["Compiler for drivers and for pcrec's emitted C", e("compiler_raw")],
        ["Governor / turbo", f"{e('governor')} / {e('turbo')}"],
        ["Timed process pinning", "; ".join(pin)],
        ["Quiet-box pre-flight verdict", "; ".join(distinct(
            s.env["load"]["verdict"] for s in ss))],
    ])


def render_engines(an):
    body = []
    for s in an.summaries():
        te = s.te
        ta = s.ta
        body.append([label(s), f"`{s.testee_id}`", te["engine_version"], te["engine_mode"],
                     te["execution_model"], te["automaton_class"],
                     ", ".join(te.get("conventions") or []),
                     te.get("captures", ""), date_of(s),
                     ta.get("verdict", "n/a")])
    return md_table(["Engine", "Testee", "Version", "Mode", "Execution model",
                     "Automaton class", "Match semantics", "Captures",
                     "Measured", "Trial agreement"], body)


def render_trials(an):
    ss = an.summaries()
    trials = distinct(str(s.max_trials) for s in ss)
    tgt = distinct(str(s.calibration_target_ns) for s in ss)
    rules = distinct(f"{s.ta.get('rule')} (k={s.ta.get('k')}, d_min={s.ta.get('d_min')}, share_c={s.ta.get('share_c')})" for s in ss)
    return (f"Trials per cell in these records: {', '.join(trials)}. "
            f"Per-row calibration target (ns of timed work per trial): "
            f"{', '.join(tgt)}. Trial-agreement rule in these records: "
            f"{'; '.join(rules)}.")


def render_compile(an):
    pc = an.pcrec
    body = []
    for s in an.summaries():
        ns = list(s.compile_ns.values())
        common = [pc.compile_ns[p] / s.compile_ns[p]
                  for p in s.compile_ns if p in pc.compile_ns and s is not pc]
        body.append([label(s), s.compile_class or "", len(ns),
                     dur(statistics.median(ns)) if ns else "n/a",
                     (times(statistics.median(common)) if common else
                      ("—" if s is pc else "n/a"))])
    return (md_table(["Engine", "Cost class", "Patterns compiled",
                      "Median compile cost", "pcrec compile ÷ this engine (median over common patterns)"],
                     body, ["---", "---", "--:", "--:", "--:"]) +
            "\n\nMedian over patterns of each pattern's median `cost.total_ns` "
            "across trials, plain form, compile rows only. A ratio above ×1 "
            "means pcrec's compile is slower. pcrec's figure includes the C "
            "compiler run that turns the emitted source into a loadable object.")


# --------------------------------------------------------------- other sets

def render_other(store, rows, setids, prov):
    body, notes = [], []
    for sid in setids:
        try:
            an = Analysis(store, sid, None, rows)
        except SystemExit:
            notes.append(f"`{sid}`: no measured pcrec-auto record in the store.")
            continue
        engines = sorted({c.te["engine_name"] for c in an.comps})
        notes.append(f"`{sid}`: competitors measured: "
                     f"{', '.join(engines) if engines else 'none'}.")
        for s in an.summaries():
            prov.append(("other-set", sid, s))
        for c, cases, excl, st in an.per:
            ex = sum(sum(v.values()) for v in excl.values())
            body.append([f"`{sid}`", label(c),
                         f"{an.pcrec.te['engine_version']} ({date_of(an.pcrec)})",
                         date_of(c), st["n"], st["win"], st["loss"], st["tie"],
                         times(st["median"]) if st["n"] else "n/a",
                         f"{ex} ({excl_text(excl)})" if ex else "0"])
        del an
    out = [md_table(["Set", "Competitor", "pcrec-auto (pin, date)",
                     "Competitor date", "Cases", "Wins", "Losses", "Ties",
                     "Median speedup", "Excluded"], body,
                    ["---", "---", "---", "---", "--:", "--:", "--:", "--:",
                     "--:", "---"])] if body else []
    out.append("\n" + "\n".join("- " + n for n in notes))
    return "\n".join(out)


# ------------------------------------------------------------------ output

MARK = r"<!-- frontpage:{name}:{kind} -->"


def splice(text, regions, fname):
    for name, content in regions.items():
        b, e = MARK.format(name=name, kind="begin"), MARK.format(name=name, kind="end")
        i, j = text.find(b), text.find(e)
        if i < 0 or j < i:
            raise SystemExit(f"frontpage: {fname}: marker pair for '{name}' "
                             f"missing or out of order")
        text = text[:i + len(b)] + "\n" + content.strip("\n") + "\n" + text[j:]
    return text


def provenance_tsv(prov, store):
    out = ["section\tset\ttestee_id\trecord_path\trecord_timestamp\t"
           "engine_version\tmachine_id\tcontent_hash_sha256"]
    seen = set()
    for section, setid, s in prov:
        k = (section, setid, s.path)
        if k in seen:
            continue
        seen.add(k)
        out.append("\t".join([section, setid, s.testee_id, s.path, s.timestamp,
                              s.te["engine_version"], s.env["machine_id"],
                              s.content_hash]))
    return "\n".join(out) + "\n"


def build(args):
    store = os.path.join(ROOT, args.store)
    rows = index_rows(store)
    an = Analysis(store, args.set, args.pin, rows)
    why = load_why(os.path.join(ROOT, args.why))
    prov = [("primary", args.set, s) for s in an.summaries()]
    img = os.path.relpath(args.out_svg, os.path.dirname(args.out_readme) or ".")
    readme = {
        "headline": render_headline(an),
        "table": render_table(an),
        "chart": f"![Per-case speedup of pcrec over each competitor, log "
                 f"scale]({img})",
        "losses": render_losses(an, why),
    }
    method = {"env": render_env(an), "engines": render_engines(an),
              "trials": render_trials(an), "compile": render_compile(an)}
    other_set = None
    if args.other_sets:
        other_set = render_other(store, rows, args.other_sets, prov)
        readme["othersets"] = other_set
    return an, readme, method, provenance_tsv(prov, store)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--set", required=True, help="subbench@version")
    ap.add_argument("--pin", help="pcrec pin (prefix of the testee_id's)")
    ap.add_argument("--other-sets", nargs="*", default=[])
    ap.add_argument("--store", default="store")
    ap.add_argument("--out-readme", default="README.md")
    ap.add_argument("--out-methodology", default="docs/methodology.md")
    ap.add_argument("--out-svg", default="docs/img/speedup_distribution.svg")
    ap.add_argument("--out-provenance", default="docs/frontpage_provenance.tsv")
    ap.add_argument("--why", default="docs/frontpage_why.tsv")
    ap.add_argument("--check", action="store_true",
                    help="regenerate in memory, diff against disk, exit 1 on drift")
    args = ap.parse_args(argv)

    an, readme, method, prov = build(args)
    outputs = {}
    for path, regions in ((args.out_readme, readme),
                          (args.out_methodology, method)):
        p = os.path.join(ROOT, path)
        with open(p, encoding="utf-8") as f:
            cur = f.read()
        outputs[path] = splice(cur, regions, path)
    outputs[args.out_svg] = render_svg(an)
    outputs[args.out_provenance] = prov

    drift = 0
    for path, new in outputs.items():
        p = os.path.join(ROOT, path)
        old = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
        if old == new:
            continue
        if args.check:
            drift += 1
            sys.stdout.writelines(difflib.unified_diff(
                old.splitlines(True), new.splitlines(True), path, path + " (regenerated)", n=1))
        else:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(new)
            print("wrote", path)
    if args.check:
        print("frontpage --check:", "DRIFT in %d file(s)" % drift if drift else "clean")
        return 1 if drift else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
