"""tools/trend_html.py -- the trend report's HUMAN form ([B130], R8, Q2, Q5).

Self-contained HTML (inline CSS + inline SVG, no script, no external fetch;
works from file://). One page per pin that has comparable deltas
(`pins/<pin>.html`) plus `index.html` (the newest such pin, with the list of
pages) and `index.md` (a markdown copy of the headline tables).

Everything printed is read from the generator's own rows (`trend.Out`): no
number is computed here except chart geometry and the chained timeline index
(a product of the committed pairwise geomeans). The AI interpretation slot
renders `reports/trend/interpretation/<pin>.md` when it exists and every
`[#row-id]` it cites exists in the TSVs generated in the same run
(tools/trend_cite_check.py, which shares no source with this module or the
generator); otherwise it renders a placeholder or a rejection banner.
"""

import html
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trend_cite_check as CC  # noqa: E402

CSS = """
:root{color-scheme:light;--bg:#fcfcfb;--fg:#0b0b0b;--fg2:#52514e;--rule:#dcdbd6;
--faster:#2a78d6;--slower:#eb6834;--noise:#8a8983;--warn:#b25000;--card:#f3f2ee}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
--bg:#1a1a19;--fg:#ffffff;--fg2:#c3c2b7;--rule:#3a3a37;--faster:#3987e5;
--slower:#d95926;--noise:#8a8983;--warn:#e0a060;--card:#242423}}
:root[data-theme="dark"]{color-scheme:dark;--bg:#1a1a19;--fg:#ffffff;--fg2:#c3c2b7;
--rule:#3a3a37;--faster:#3987e5;--slower:#d95926;--noise:#8a8983;--warn:#e0a060;--card:#242423}
body{background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,sans-serif;margin:0;padding:16px;max-width:1100px;margin:auto}
h1{font-size:1.5em}h2{font-size:1.2em;margin-top:2em;border-bottom:1px solid var(--rule)}h3{font-size:1.02em}
table{border-collapse:collapse;font-size:13px;margin:.5em 0;width:100%}
th,td{border-bottom:1px solid var(--rule);padding:3px 6px;text-align:right;vertical-align:top}
th:first-child,td:first-child,td.l,th.l{text-align:left}
code{font-size:12px;word-break:break-all}.card{background:var(--card);padding:8px 12px;border-radius:6px;margin:.6em 0}
.flag{color:var(--warn);font-weight:600}.muted{color:var(--fg2)}
.f{color:var(--faster);font-weight:600}.s{color:var(--slower);font-weight:600}
svg text{fill:var(--fg2);font-size:11px}svg .ax{stroke:var(--rule)}svg .one{stroke:var(--fg2);stroke-dasharray:3 3}
.wrap{overflow-x:auto}nav a{margin-right:.8em}
"""

LEGEND = ('<p class="muted"><span class="f">&#9679; faster</span> (disjoint trial '
          'ranges, beyond the identical-program band) &nbsp; <span class="s">'
          '&#9650; slower</span> &nbsp; &#9675; within noise / band. '
          'Ratio = new / old (&lt; 1 faster).</p>')


def e(x):
    return html.escape(str(x), quote=True)


def on(v):
    return str(v) in ("1", "True")


def fl(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def ratio_txt(x):
    v = fl(x)
    return "" if v is None else (f"x{v:.3f}" if v >= 0.01 else f"x{v:.4f}")


def ns_txt(x):
    v = fl(x)
    if v is None:
        return ""
    if v >= 1e6:
        return f"{v/1e6:.2f} ms"
    if v >= 1e3:
        return f"{v/1e3:.1f} us"
    return f"{v:.0f} ns"


# --------------------------------------------------------------- SVG charts

def strip_chart(rows, title):
    """Dot strip of log10 ratio per cell; deterministic jitter by index."""
    W, H, L, R_ = 640, 120, 40, 14
    lo, hi = -2.0, 1.0   # x10 .. /100: clip outside
    def x(v):
        v = max(lo, min(hi, math.log10(v)))
        return L + (v - lo) / (hi - lo) * (W - L - R_)
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="{e(title)}">',
           f'<text x="{L}" y="12">{e(title)}</text>']
    for tick in (0.01, 0.1, 0.5, 1, 2, 10):
        if lo <= math.log10(tick) <= hi:
            xx = x(tick)
            cls = "one" if tick == 1 else "ax"
            out.append(f'<line class="{cls}" x1="{xx:.1f}" x2="{xx:.1f}" y1="20" y2="{H-22}"/>')
            out.append(f'<text x="{xx:.1f}" y="{H-8}" text-anchor="middle">{tick:g}</text>')
    for i, r in enumerate(rows):
        v = fl(r["ratio"])
        if not v or v <= 0:
            continue
        y = 30 + (i * 7) % 60
        xx = x(v)
        t = f'<title>{e(r["pattern"])} {ratio_txt(v)} ({e(r["verdict"])})</title>'
        vd = r["verdict"]
        if vd == "faster":
            out.append(f'<circle cx="{xx:.1f}" cy="{y}" r="3.5" fill="var(--faster)">{t}</circle>')
        elif vd == "slower":
            out.append(f'<path d="M{xx-4:.1f} {y+3.5} L{xx+4:.1f} {y+3.5} L{xx:.1f} {y-4} Z" '
                       f'fill="var(--slower)">{t}</path>')
        else:
            out.append(f'<circle cx="{xx:.1f}" cy="{y}" r="2.5" fill="none" '
                       f'stroke="var(--noise)">{t}</circle>')
    out.append("</svg>")
    return "".join(out)


def line_chart(series, pins, title):
    """series: {label: [(pin_index, value)]}; log y."""
    W, H, L, R_, T, B = 640, 190, 44, 90, 20, 36
    vals = [v for pts in series.values() for _, v in pts if v and v > 0]
    if not vals or len(pins) < 2:
        return ""
    lo = math.log10(min(vals) * 0.9)
    hi = math.log10(max(vals) * 1.1)
    if hi - lo < 0.2:
        lo, hi = lo - 0.1, hi + 0.1
    def px(i):
        return L + i / max(1, len(pins) - 1) * (W - L - R_)
    def py(v):
        return T + (hi - math.log10(v)) / (hi - lo) * (H - T - B)
    cols = ["var(--faster)", "var(--slower)"]
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="{e(title)}">',
           f'<text x="{L}" y="12">{e(title)}</text>']
    for i, p in enumerate(pins):
        out.append(f'<text x="{px(i):.1f}" y="{H-8}" text-anchor="middle">{e(p[:7])}</text>')
        out.append(f'<line class="ax" x1="{px(i):.1f}" x2="{px(i):.1f}" y1="{T}" y2="{H-B}"/>')
    one = 0.0
    if lo < one < hi:
        out.append(f'<line class="one" x1="{L}" x2="{W-R_}" y1="{py(1):.1f}" y2="{py(1):.1f}"/>')
    for si, (label, pts) in enumerate(sorted(series.items())):
        c = cols[si % 2]
        dash = "" if si % 2 == 0 else ' stroke-dasharray="6 3"'
        path = " ".join(("M" if k == 0 else "L") + f"{px(i):.1f} {py(v):.1f}"
                        for k, (i, v) in enumerate(pts) if v and v > 0)
        out.append(f'<path d="{path}" fill="none" stroke="{c}" stroke-width="2"'
                   + dash + '/>')
        for i, v in pts:
            if v and v > 0:
                out.append(f'<circle cx="{px(i):.1f}" cy="{py(v):.1f}" r="3" fill="{c}">'
                           f'<title>{e(label)} {e(pins[i])}: {v:.3f}</title></circle>')
        if pts:
            i, v = pts[-1]
            out.append(f'<text x="{px(i)+6:.1f}" y="{py(v)+4 + si*10:.1f}">{e(label)}</text>')
    out.append("</svg>")
    return "".join(out)


# ----------------------------------------------------------------- page body

def table(cols, rows, labels=None, left=(), rid=None):
    labels = labels or cols
    h = ["<div class=\"wrap\"><table><tr>" + "".join(
        f'<th class="{"l" if c in left else ""}">{e(l)}</th>' for c, l in zip(cols, labels))
        + "</tr>"]
    for r in rows:
        idattr = f' id="{e(r[rid])}"' if rid and r.get(rid) else ""
        h.append(f"<tr{idattr}>" + "".join(
            f'<td class="{"l" if c in left else ""}">{r.get(c, "")}</td>' for c in cols) + "</tr>")
    h.append("</table></div>")
    return "".join(h)


def prep_mover(r):
    d = dict(r)
    d["ratio_h"] = ratio_txt(r["ratio"])
    d["old"] = ns_txt(r["ns_prev"])
    d["new"] = ns_txt(r["ns_new"])
    d["pattern_h"] = e(r["pattern"]) + ("" if r["form"] == "plain" else f' <span class="muted">[{e(r["form"])}]</span>')
    d["id_h"] = f'<code>{e(r["row_id"])}</code>'
    flags = []
    if r["identical"] == "yes":
        flags.append("identical-program")
    if r["identical"] == "unknown-abi67":
        flags.append("identity unknown (abi 67)")
    if on(r["instrument_changed"]):
        flags.append("instrument-changed")
    if on(r["cell_drift_suspect"]):
        flags.append("cell drift")
    d["flags"] = e("; ".join(flags))
    return d


def page(cfg, meta, out, pin, pins_with_pages, outdir, files_ids, depth, is_index):
    pre = "../" * depth
    sums = [r for r in out.summary if r["pin"] == pin]
    dels = [r for r in out.deltas if r["pin"] == pin]
    body = []
    nav = " ".join(f'<a href="{pre}pins/{e(p)}.html">{e(p)}</a>' for p in pins_with_pages)
    body.append(f'<h1>pcrec trend report &mdash; pin <code>{e(pin)}</code></h1>')
    home = "" if is_index else '<a href="' + pre + 'index.html">index</a> '
    body.append('<nav>' + home + 'pins: ' + nav + '</nav>')
    body.append(f'<p class="muted">as of {e(meta["as_of"])} &middot; snapshots sha '
                f'<code>{e(meta["snapshots_sha256"][:12])}</code> &middot; config sha '
                f'<code>{e(meta["config_sha256"][:12])}</code> &middot; {e(meta["direction"])}. '
                f'Machine data: <a href="{pre}summary.tsv">summary.tsv</a>, '
                f'<a href="{pre}deltas.tsv">deltas.tsv</a>, <a href="{pre}cells.tsv">cells.tsv</a>, '
                f'<a href="{pre}movers_by_stamp.tsv">movers_by_stamp.tsv</a>, '
                f'<a href="{pre}compile_deltas.tsv">compile_deltas.tsv</a>, '
                f'<a href="{pre}deny_twins.tsv">deny_twins.tsv</a>.</p>')
    body.append(f'<p class="muted">Program-identity criterion: {e(meta["identity_criterion"])}. '
                f'Pins with no records: {e(meta["pins_without_records"]) or "none"}.</p>')

    # --- data-quality flags
    flagged = [s for s in sums if on(s["instrument_changed"]) or on(s["wide_gap"])
               or on(s["drift_suspect"])]
    body.append("<h2>Read this first: pair flags</h2>")
    if flagged:
        seen = {}
        for s in flagged:
            k = (s["set_ver"], s["prev_set_ver"], s["prev_pin"])
            f = seen.setdefault(k, set())
            if on(s["instrument_changed"]):
                f.add("instrument-changed (" + e(s["instrument_changed_files"]) + ")")
            if on(s["wide_gap"]):
                f.add(f'wide-pin-gap (abi span {s["abi_span"]} &gt; {cfg["wide_gap_abi"]})')
            if on(s["drift_suspect"]):
                f.add("drift-suspect")
        body.append('<div class="card flag"><ul>' + "".join(
            f'<li>{e(k[0])} vs {e(k[1])} @ <code>{e(k[2])}</code>: {"; ".join(sorted(v))}</li>'
            for k, v in sorted(seen.items())) + "</ul>"
            '<span class="muted">instrument-changed: the bench\'s own shim.c/driver.c differ between '
            'the two records (R19) &mdash; a move in a program-identical cell is the bench, not pcrec. '
            'wide-pin-gap: many abi steps in one pair, causes cannot be separated (R18).</span></div>')
    else:
        body.append("<p>No pair at this pin carries an instrument-changed, wide-pin-gap or drift-suspect flag.</p>")

    # --- headline per class
    configs = list(cfg["headline_configs"]) + list(cfg.get("extra_configs", []))
    for config in configs:
        cs = [s for s in sums if s["config"] == config]
        label = {"auto-caps-simdna": "auto-caps (headline)",
                 "auto-nocaps-simdna": "auto-nocaps (headline)"}.get(config, config)
        body.append(f"<h2>{e(label)}</h2>")
        if not cs:
            body.append('<p class="muted">no comparable pair at this pin.</p>')
            continue
        view = []
        for s in cs:
            v = dict(s)
            v["pair"] = f'{s["prev_set_ver"]} @ {s["prev_pin"]} &rarr; {s["set_ver"]}'
            v["pair"] = e(v["pair"]).replace("&amp;rarr;", "&rarr;")
            v["id_h"] = f'<code>{e(s["row_id"])}</code>'
            view.append(v)
        body.append(table(
            ["pair", "regime", "n_numeric", "n_faster", "n_slower", "n_within_noise",
             "n_within_identical_band", "geomean_ratio", "median_ratio", "n_identical",
             "n_identical_moved", "band", "control_median_ratio", "n_drift_suspect_cells",
             "id_h"],
            view,
            ["pair", "regime", "cells", "faster", "slower", "noise", "in-band",
             "geomean", "median", "ident.", "ident. moved", "band", "control", "drift cells", "row id"],
            left=("pair", "regime", "id_h"), rid="row_id"))
        body.append('<p class="muted">Regimes are never pooled (R15). "ident. moved" is the '
                    'per-pair noise estimate (R6+): program-identical cells whose trial ranges are '
                    'disjoint. "band" = q95 of |ratio-1| over program-identical cells (or the declared '
                    'fallback).</p>')
        for s in cs:
            ds = [d for d in dels if d["config"] == config and d["set_ver"] == s["set_ver"]
                  and d["prev_pin"] == s["prev_pin"] and d["regime"] == s["regime"]
                  and fl(d["ratio"])]
            body.append(f'<h3>{e(s["set_ver"])} &middot; {e(s["regime"])} &middot; vs '
                        f'<code>{e(s["prev_pin"])}</code></h3>')
            body.append('<div class="wrap">' + strip_chart(
                ds, f'{s["set_ver"]} {s["regime"]} ({len(ds)} cells)') + "</div>")
            movers = [d for d in ds if d["verdict"] in ("faster", "slower")
                      and d["identical"] != "yes"]
            top = cfg["highlight_top"]
            for vd, rev, nm in (("faster", False, "Largest improvements"),
                                ("slower", True, "Largest regressions")):
                l = sorted([d for d in movers if d["verdict"] == vd],
                           key=lambda d: fl(d["ratio"]), reverse=rev)[:top]
                if l:
                    body.append(f"<p><b>{nm}</b> (beyond noise, program not identical)</p>")
                    body.append(table(["pattern_h", "ratio_h", "old", "new", "flags", "id_h"],
                                      [prep_mover(d) | {"row_id": d["row_id"]} for d in l],
                                      ["pattern", "ratio", "old", "new", "flags", "row id"],
                                      left=("pattern_h", "flags", "id_h"), rid="row_id"))
        body.append(LEGEND)
        corr = [d for d in dels if d["config"] == config and d["transition"]]
        if corr:
            body.append("<p><b>Correctness / state changes</b></p>")
            body.append(table(["pattern_h", "transition", "set_ver", "id_h"],
                              [prep_mover(d) | {"row_id": d["row_id"]} for d in corr[:40]],
                              ["pattern", "transition", "set", "row id"],
                              left=("pattern_h", "transition", "set_ver", "id_h"), rid="row_id"))

    # --- movers by stamp (headline only)
    mv = [m for m in out.movers if m["pin"] == pin and m["config"] in cfg["headline_configs"]
          and on(m["changed"])]
    body.append("<h2>Movers grouped by mechanism stamp (R13)</h2>")
    if mv:
        view = [dict(m, set=e(m["set_ver"]), grp=e(f'{m["stamp"]}: {m["prev_value"] or "-"} > {m["new_value"] or "-"}'))
                for m in mv]
        body.append(table(["config", "set", "regime", "grp", "n_movers", "n_faster", "n_slower", "geomean_ratio"],
                          view, ["config", "set", "regime", "stamp change", "movers", "faster", "slower", "geomean"],
                          left=("config", "set", "regime", "grp")))
        body.append('<p class="muted">Grouping by stamp value, not a cause (R13). Full table: movers_by_stamp.tsv.</p>')
    else:
        body.append('<p class="muted">no beyond-noise mover sits in a cell whose stamp changed.</p>')

    # --- size / compile (Q2)
    ks = [k for k in out.compile if k["pin"] == pin and k["config"] in cfg["headline_configs"]
          and (k["highlight_size"] or k["highlight_compile"] or k["outcome_changed"])]
    body.append(f'<h2>Size and compile highlights (Q2)</h2><p class="muted">emit_code_bytes change '
                f'&ge; {cfg["size_threshold"]:.0%}; compile time change &ge; {cfg["compile_threshold"]:.0%} '
                f'with disjoint trial ranges; any outcome change.</p>')
    if ks:
        ks = sorted(ks, key=lambda k: -abs((fl(k["emit_code_bytes_ratio"]) or 1) - 1))[:cfg["highlight_top"] * 3]
        view = [dict(k, pat=e(k["pattern"]), idh=f'<code>{e(k["row_id"])}</code>') for k in ks]
        body.append(table(["config", "pat", "outcome_prev", "outcome_new", "emit_code_bytes_prev",
                           "emit_code_bytes_new", "emit_code_bytes_ratio", "compile_ratio", "identical", "idh"],
                          view, ["config", "pattern", "was", "now", "code B was", "code B now",
                                 "size ratio", "compile ratio", "ident.", "row id"],
                          left=("config", "pat", "idh"), rid="row_id"))
    else:
        body.append("<p>No cell crosses a size or compile threshold at this pin.</p>")

    # --- timeline
    body.append("<h2>Timeline of the headline configs</h2>")
    body.append('<p class="muted">Chained index: 1.0 at the first pin, multiplied at each pin by the '
                'pair\'s geomean ratio (the pairs that carry the most cells). A visual aid over '
                'summary.tsv, never a measurement of its own; a wide-gap or instrument-changed step is '
                'marked in the tooltip-less data, see summary.tsv.</p>')
    for config in cfg["headline_configs"]:
        sets = sorted({s["set_ver"].split("@")[0] for s in out.summary if s["config"] == config})
        for sn in sets:
            series, pinlist = chain_series(out.summary, config, sn)
            if series and len(pinlist) >= 2:
                body.append('<div class="wrap">' + line_chart(series, pinlist, f"{config} - {sn}") + "</div>")

    # --- deny twins
    tw = [t for t in out.twins if t["pin"] == pin]
    body.append("<h2>Deny twins at this pin (NEW vs DENY, R17)</h2>")
    if tw:
        agg = {}
        for t in tw:
            k = (t["set_ver"], t["base_config"], t["deny_config"], t["regime"])
            a = agg.setdefault(k, [0, 0, 0, t["cross_window"], t["window_gap_hours"]])
            a[0] += 1
            if on(t["ranges_disjoint"]):
                a[1 if fl(t["ratio_deny_over_base"]) > 1 else 2] += 1
        view = [{"set": e(k[0]), "base": e(k[1]), "deny": e(k[2]), "regime": e(k[3]),
                 "n": a[0], "slower": a[1], "faster": a[2],
                 "win": "cross-window" if on(a[3]) else "same-window",
                 "gap": a[4]} for k, a in sorted(agg.items())]
        body.append(table(["set", "base", "deny", "regime", "n", "slower", "faster", "win", "gap"], view,
                          ["set", "base", "deny config", "regime", "cells", "deny slower", "deny faster",
                           "window", "gap h"], left=("set", "base", "deny", "regime", "win")))
        body.append('<p class="muted">deny/base &gt; 1: the denied mechanism was helping. Per-cell rows: deny_twins.tsv.</p>')
    else:
        body.append('<p class="muted">no deny twin is pinned alongside its base at this pin.</p>')

    # --- cells of interest
    body.append("<h2>Cells of interest (pcrec-supplied, R17)</h2>")
    ir = [r for r in out.interest_rows if r["pin"] == pin]
    if ir:
        mechs = sorted({r["mechanism"] for r in ir})
        for m in mechs:
            body.append(f"<h3>{e(m)}</h3>")
            rows = [dict(r, pat=e(r["pattern"]), rt=ratio_txt(r["ratio"]), idh=f'<code>{e(r["delta_row_id"])}</code>')
                    for r in ir if r["mechanism"] == m]
            body.append(table(["role", "config", "pat", "regime", "rt", "verdict", "identical", "idh"], rows,
                              ["role", "config", "pattern", "regime", "ratio", "verdict", "ident.", "row id"],
                              left=("role", "config", "pat", "regime", "verdict", "idh")))
    else:
        body.append('<p class="muted">cells_of_interest.tsv has no row matching this pin '
                    '(fill reports/trend/cells_of_interest.tsv to get one section per mechanism).</p>')

    # --- AI interpretation slot
    body.append("<h2>AI interpretation</h2>")
    body.append(interpretation_block(outdir, pin, files_ids))

    # --- full table
    body.append("<h2>Full table: every pcrec config at this pin</h2>")
    full = [dict(s, set=e(s["set_ver"]), prev=e(s["prev_pin"])) for s in sums]
    body.append(table(["config", "set", "prev", "regime", "n_numeric", "n_faster", "n_slower",
                       "geomean_ratio", "n_identical_moved", "instrument_changed", "wide_gap"],
                      full, ["config", "set", "vs pin", "regime", "cells", "faster", "slower", "geomean",
                             "ident. moved", "instr.", "wide"], left=("config", "set", "prev", "regime")))
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<title>pcrec trend {e(pin)}</title><style>{CSS}</style></head><body>"
            + "".join(body) + "</body></html>\n")


def chain_series(summary, config, setname):
    rows = [s for s in summary if s["config"] == config
            and s["set_ver"].split("@")[0] == setname and fl(s["geomean_ratio"])]
    pins = []
    by = {}
    for s in rows:
        by.setdefault((s["pin"], s["regime"]), []).append(s)
    order = sorted({s["pin"] for s in rows}, key=lambda p: min(
        rows.index(x) for x in rows if x["pin"] == p))
    # pin order by summary row order (sorted by pin_order index in the generator)
    first_prev = None
    for s in rows:
        first_prev = s["prev_pin"]
        break
    pinlist = ([first_prev] if first_prev else []) + order
    pinlist = list(dict.fromkeys(pinlist))
    series = {}
    for rg in sorted({s["regime"] for s in rows}):
        v = 1.0
        pts = [(0, 1.0)]
        for p in order:
            cand = by.get((p, rg))
            if not cand:
                continue
            best = max(cand, key=lambda s: int(s["n_numeric"]))
            v *= fl(best["geomean_ratio"])
            pts.append((pinlist.index(p), v))
        series[rg] = pts
    return series, pinlist


def interpretation_block(outdir, pin, files_ids):
    p = os.path.join(outdir, "interpretation", pin + ".md")
    if not os.path.exists(p):
        return ('<div class="card"><b>AI interpretation: not yet written.</b> Owed to the '
                'manager session (a Claude session grounded only in the TSV row ids on this '
                'page; docs/design/trend_interpretation_v0.md). Nothing on this page depends on it.</div>')
    with open(p, encoding="utf-8") as f:
        text = f.read()
    errs = CC.check_text(text, files_ids)
    if errs:
        return ('<div class="card flag"><b>Interpretation REJECTED:</b> it cites ids that do not '
                'exist in the TSVs generated with this page.<ul>' +
                "".join(f"<li><code>{e(x)}</code></li>" for x in errs[:20]) +
                "</ul></div>")
    return ('<div class="card"><span class="muted">AI-written, grounded: every cited row id '
            'exists in this run\'s TSVs (checked by tools/trend_cite_check.py). Read the rows, '
            'not the prose, for anything that matters.</span>' + CC.render_md(text, files_ids) + "</div>")


def markdown_copy(cfg, meta, out, pin):
    L = [f"# pcrec trend report: pin {pin}", "",
         f"as of {meta['as_of']}; snapshots sha {meta['snapshots_sha256'][:12]}; {meta['direction']}.", ""]
    for config in cfg["headline_configs"]:
        L += [f"## {config}", "",
              "| pair | regime | cells | faster | slower | noise | geomean | ident. moved | flags |",
              "|---|---|---|---|---|---|---|---|---|"]
        for s in out.summary:
            if s["pin"] == pin and s["config"] == config:
                fl_ = [n for n, k in (("instrument-changed", "instrument_changed"),
                                      ("wide-pin-gap", "wide_gap"), ("drift-suspect", "drift_suspect"))
                       if str(s[k]) == "1"]
                L.append(f"| {s['prev_set_ver']}@{s['prev_pin']} > {s['set_ver']} | {s['regime']} | "
                         f"{s['n_numeric']} | {s['n_faster']} | {s['n_slower']} | {s['n_within_noise']} | "
                         f"{s['geomean_ratio']} | {s['n_identical_moved']} | {', '.join(fl_)} |")
        L.append("")
    return "\n".join(L) + "\n"


def render_all(cfg, meta, out, outdir, files_text=None):
    pins = []
    seen = set()
    for s in out.summary:
        if s["pin"] not in seen:
            seen.add(s["pin"])
            pins.append(s["pin"])
    order = {p: i for i, p in enumerate(meta["pin_order"].split(","))}
    pins.sort(key=lambda p: order.get(p, 999))
    files = {}
    ids = CC.ids_from_texts(files_text or {})
    for p in pins:
        files[f"pins/{p}.html"] = page(cfg, meta, out, p, pins, outdir, ids, 1, False)
    if pins:
        files["index.html"] = page(cfg, meta, out, pins[-1], pins, outdir, ids, 0, True)
        files["index.md"] = markdown_copy(cfg, meta, out, pins[-1])
    return files
