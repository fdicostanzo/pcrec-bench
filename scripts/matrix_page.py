#!/usr/bin/env python3
"""scripts/matrix_page.py -- render a `.matrix.tsv` sibling (`pcrecbench
report --format matrix`, [B52], `pcrecbench/report.py`'s
`render_matrix_tsv`) into a single self-contained, dependency-free HTML
page: a sticky tests-x-engines table, one row per timing cell, one
column per testee, a log-scale colour ramp on every ratio cell and a
fixed chip per closed status token, a hover tooltip recovering each
ratio cell's absolute median (`best_ns` x the printed ratio) and its
testee id, the `.matrix.tsv`'s own provenance comment rendered verbatim,
and both a light and a dark theme (`prefers-color-scheme`, no toggle
needed).

[B82] (inbox I-99/I-100, 2026-09-23): when the file's roster spans BOTH
capture classes (`# capture_class: yes=...; no=...; undeclared=...`, a
provenance line `pcrecbench.report.render_matrix_tsv` emits), this page
renders TWO class-pure matrices -- caps vs caps, nocaps vs nocaps --
each with its OWN `best_testee`/`best_ns` RE-DERIVED from this file's
own numbers (`class_pure_row`: `absolute_ns(t) = ratio(t) x row's global
best_ns`, then a new class-local ratio), never a second reduction over
the store. A single-class roster (or a `.matrix.tsv` from before this
lane) renders the ORIGINAL single table, byte for byte. An `undeclared`
testee (I-99's fail-loud rule) is excluded from both tables and named in
its own note. This page never imports `pcrecbench` -- the classification
is read from the file's own provenance line, by regex, not re-derived.

THIS IS THE COMMITTED VISUAL REFERENCE Frank's ruling names (docs/dev/
dev_journal.md, 2026-09-18 close, [B52] charter item 4): the ad hoc page
built for the reset-session reading of the capability window is what
this script is a maintained, from-a-`.matrix.tsv`, from-scratch
generator FOR -- it takes no input but the TSV file and writes no
`.tsv` of its own, so the TSV stays canonical (charter item 1) and this
HTML stays DERIVED, regenerable from it at any time.

[B91] (Frank's ruling, 2026-09-25: "calculate best based on what is
currently selected"): the page carries a TESTEE SELECTION -- one checkbox
per testee -- and a small inline script that recomputes every table's
per-row best and every ratio over the checked testees only (the results
viewer's `computeBest` rule), hiding unchecked columns. Every ratio cell
carries its absolute median as `data-ns` (ratio x its table's best_ns),
so the recompute is exact arithmetic on the file's own numbers. The
reporter v24 header (`best_testee_pooled`/`best_ns_pooled` + the
class-pure `_yes`/`_no` pairs) and the pre-v24 six-column header are
both accepted.

WHY A HAND-ROLLED PARSER, NOT `csv`. The stdlib `csv` module is fine for
the TSV itself (`csv.reader(fh, delimiter="\\t")`, used below) --
what needs hand-rolling is nothing: the file's `#`-prefixed provenance
lines are read and kept VERBATIM (never re-derived, never re-worded --
see `report.py`'s own module docstring on why a rendering never
restates a fact a shared function already computed once), and the
first non-`#` line is the header row `render_matrix_tsv` itself
documents: `subbench, pattern, regime_or_na, form, best_testee, best_ns`
then one column per testee in the query's own roster.

USAGE:

    python3 scripts/matrix_page.py reports/<name>.matrix.tsv
    python3 scripts/matrix_page.py reports/<name>.matrix.tsv -o /tmp/out.html

Writes `<name>.matrix.html` beside the input by default (`-o` overrides
the path). Exits 1 naming the problem on a malformed file (a header row
that is not the 6 fixed columns plus at least one testee, a data row
whose column count disagrees with the header) rather than rendering a
silently-truncated table.
"""

from __future__ import annotations

import argparse
import csv
import html
import math
import os
import re
import sys

FIXED_COLS = ["subbench", "pattern", "regime_or_na", "form", "best_testee", "best_ns"]

# [B91] (reporter v24): the pooled pair is RENAMED `_pooled` and joined by
# the class-pure `_yes`/`_no` pairs. Both shapes are accepted; a v24 row
# is NORMALISED on parse so `row["best_testee"]`/`row["best_ns"]` always
# name the POOLED best (what every ratio cell in the file is relative
# to), and the class-pure pairs ride along under their own names.
FIXED_COLS_V24 = ["subbench", "pattern", "regime_or_na", "form",
                  "best_testee_pooled", "best_ns_pooled",
                  "best_testee_yes", "best_ns_yes",
                  "best_testee_no", "best_ns_no"]


def fixed_count(header):
    """How many leading fixed columns `header` carries (10 at reporter
    v24+, 6 before it) -- the testee roster is everything after."""
    if header[:len(FIXED_COLS_V24)] == FIXED_COLS_V24:
        return len(FIXED_COLS_V24)
    return len(FIXED_COLS)

# [B82] (inbox I-99/I-100): `pcrecbench.report.render_matrix_tsv` emits a
# `capture_class: yes=<t1,t2,...>; no=<t3,...>; undeclared=<t4,...>`
# clause inside one of its provenance lines. Parsed here BY REGEX rather
# than imported from `pcrecbench.capture_class` -- this script is
# deliberately DEPENDENCY-FREE and standalone (its own module docstring),
# and the classification is already a committed FACT in the file this
# script's whole contract is to read, never re-derive.
_CAPTURE_CLASS_RE = re.compile(
    r"capture_class: yes=([^;]*); no=([^;]*); undeclared=([^;]*)")

# The SIX CLOSED status tokens `render_matrix_tsv` ever prints in place
# of a ratio (its own module-docstring [B52] section, plus KB-27's
# `no-expectation` addition -- NOT called `unjudged`: that word already
# names an unrelated count on the SAME report's `trial_agreement` line,
# `pcrecbench.reduce.agreement_line`) -- one fixed chip colour per
# token, deliberately NOT on the log-scale ramp: a status token is a
# FACT about why nothing was timed, not a magnitude to shade by.
# `checked in this order` in `report.py`'s docstring is a compile rule
# for `_matrix_cell`, not a display rule here -- this dict is keyed by
# the rendered string, order irrelevant.
STATUS_CHIPS = {
    "unsup": ("chip-unsup", "unsupported-by-declaration (the testee's own "
              "advance capability declaration, not an engine failure)"),
    "refused": ("chip-refused", "did-not-compile"),
    "wrong": ("chip-wrong", "excluded: n_wrong > 0 (a wrong answer)"),
    "gave-up": ("chip-gaveup", "excluded: n_gave_up > 0, no wrong answer"),
    "no-expectation": ("chip-no-expectation", "excluded: n_no_expectation > 0, "
                        "no wrong answer or give-up (KB-27: no derived "
                        "expectation exists for this (pattern, subject, "
                        "regime) at all)"),
    "excluded": ("chip-excluded", "excluded for any other reason (a "
                 "non-measured status, a scratch-tier row not included, "
                 "a different form's own row, or this testee never ran "
                 "this pattern under this row's form at all)"),
}

# The ramp's own domain, stated once here because the tooltip and the
# legend both need to agree with it: ratio 1.0x (this row's own best,
# never shaded) through ratio 10**LOG_MAX x (the reddest cell the ramp
# has -- anything slower still renders at the same reddest colour, not
# clipped invisibly off top).
LOG_MAX = 7


class MatrixParseError(Exception):
    pass


def parse_matrix_tsv(path):
    """Returns `(provenance_lines, header, rows)`: `provenance_lines` is
    every leading `#`-prefixed line, VERBATIM, in file order;
    `header` is the parsed header row (`FIXED_COLS` + the testee
    roster); `rows` is a list of dicts, one per data row, `{col: value}`
    over that same header. Raises `MatrixParseError` naming the problem
    on anything that does not fit `render_matrix_tsv`'s own documented
    shape."""
    provenance_lines = []
    header = None
    rows = []
    with open(path, encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        for lineno, cols in enumerate(reader, start=1):
            if not cols:
                continue
            if header is None and cols[0].startswith("#"):
                # csv.reader already split the `#`-line on tabs, but a
                # provenance line has none -- rejoin with the delimiter
                # it was split on so the ORIGINAL line survives verbatim.
                provenance_lines.append("\t".join(cols))
                continue
            if header is None:
                header = cols
                shape = (FIXED_COLS_V24 if header[:len(FIXED_COLS_V24)] == FIXED_COLS_V24
                         else FIXED_COLS)
                if header[:len(shape)] != shape or len(header) <= len(shape):
                    raise MatrixParseError(
                        f"{path}:{lineno}: header {header!r} does not start with "
                        f"{FIXED_COLS_V24!r} (reporter v24+) or {FIXED_COLS!r} "
                        f"plus at least one testee column")
                continue
            if len(cols) != len(header):
                raise MatrixParseError(
                    f"{path}:{lineno}: row has {len(cols)} column(s), "
                    f"header has {len(header)}: {cols!r}")
            row = dict(zip(header, cols))
            if "best_ns_pooled" in row:
                row["best_testee"] = row["best_testee_pooled"]
                row["best_ns"] = row["best_ns_pooled"]
            rows.append(row)
    if header is None:
        raise MatrixParseError(f"{path}: no header row found (file empty or all-comment)")
    return provenance_lines, header, rows


def parse_capture_class(provenance_lines):
    """[B82]: `(yes, no, undeclared)`, each a list of testee ids (empty
    if the file predates this lane, or names none) -- the FIRST
    provenance line matching `_CAPTURE_CLASS_RE`, since
    `render_matrix_tsv` emits exactly one."""
    for line in provenance_lines:
        m = _CAPTURE_CLASS_RE.search(line)
        if m:
            yes = [t for t in m.group(1).split(",") if t]
            no = [t for t in m.group(2).split(",") if t]
            undeclared = [t for t in m.group(3).split(",") if t]
            return yes, no, undeclared
    return [], [], []


def class_pure_row(row, class_testees):
    """[B82] (inbox I-99): recompute ONE row's `best_testee`/`best_ns`
    and every `class_testees` cell's ratio WITHIN THE CLASS, from the
    row's OWN numbers alone -- `absolute_ns(t) = ratio(t) x row's global
    best_ns`, then `class_ratio(t) = absolute_ns(t) / class_best_ns`.
    This is a re-derivation from data already in the file, never a
    second reduction over the store: the class-pure page and the
    reporter's own `rank_yes`/`rank_no` TSV sections can therefore never
    disagree by a rounding choice this script made on its own. A
    STATUS-TOKEN cell (no ratio at all) is copied through unchanged and
    is never a `best`-of candidate, the same rule `_matrix_best`/
    `_matrix_cell` apply upstream. Returns a NEW row dict; the input is
    never mutated."""
    best_ns_global = row.get("best_ns") or ""
    absolute = {}
    for t in class_testees:
        raw = row.get(t, "")
        if raw in STATUS_CHIPS or not best_ns_global:
            continue
        try:
            absolute[t] = float(raw) * float(best_ns_global)
        except ValueError:
            continue
    new_row = dict(row)
    if not absolute:
        new_row["best_testee"] = ""
        new_row["best_ns"] = ""
        return new_row
    class_best_t = min(absolute, key=absolute.get)
    class_best_ns = absolute[class_best_t]
    for t, ns in absolute.items():
        new_row[t] = f"{ns / class_best_ns:.6f}" if class_best_ns else ""
    new_row["best_testee"] = class_best_t
    new_row["best_ns"] = f"{class_best_ns:.1f}"
    return new_row


def _ratio_color(ratio):
    """The log-scale ramp, ratio 1.0 (this row's own best, never worse)
    through 10**LOG_MAX (the reddest cell) -- `t` is the ramp position
    in [0, 1], clamped at both ends (a sub-1.0 ratio cannot happen by
    construction, but a clamp costs nothing and a NaN/negative value
    from a malformed file must not crash the render). Interpolates
    linearly in RGB between a light, cool "at par" colour and a warm
    "far behind" one -- readable in both themes because the TEXT colour
    (`_ratio_text_color`) is chosen from the same `t`, not fixed."""
    try:
        t = math.log10(max(ratio, 1.0)) / LOG_MAX
    except (ValueError, TypeError):
        t = 0.0
    t = max(0.0, min(1.0, t))
    # at-par: a cool green-blue; far behind: a warm red. Both chosen to
    # keep sufficient contrast with BOTH the light-theme near-white and
    # the dark-theme near-black page background at every point of the
    # ramp -- see the CSS `--matrix-fg-*` split below.
    lo = (56, 161, 255)   # #38a1ff, "at par"
    hi = (220, 38, 38)    # #dc2626, "far behind"
    r = round(lo[0] + (hi[0] - lo[0]) * t)
    g = round(lo[1] + (hi[1] - lo[1]) * t)
    b = round(lo[2] + (hi[2] - lo[2]) * t)
    return r, g, b, t


def _cell_html(row, testee, best_ns):
    """One `<td>` for one (row, testee) pair. `render_matrix_tsv`'s own
    NO-EMPTY-CELLS invariant means `raw` is always present and always
    either a status token or a parseable ratio -- this function trusts
    that invariant rather than re-checking it (a malformed upstream file
    is `parse_matrix_tsv`'s job to catch, at the row-shape level, not
    this function's to re-detect cell by cell)."""
    raw = row.get(testee, "")
    dt = f' data-t="{html.escape(testee)}"'
    if raw in STATUS_CHIPS:
        cls, title = STATUS_CHIPS[raw]
        return (f'<td class="cell {cls}"{dt} title="{html.escape(title)}">'
                f'{html.escape(raw)}</td>')
    try:
        ratio = float(raw)
    except ValueError:
        return (f'<td class="cell chip-excluded"{dt} title="unparseable cell">'
                f'{html.escape(raw)}</td>')
    r, g, b, t = _ratio_color(ratio)
    fg = "#0b0b0b" if t < 0.55 else "#fbfbfb"
    title_bits = [f"{ratio:.3f}x this row's best"]
    # [B91]: the cell's ABSOLUTE median (ratio x this table's best_ns),
    # carried as `data-ns` so the page's selection script can recompute
    # the row's best and every ratio over whatever testees are selected.
    data_ns = ""
    if best_ns:
        try:
            ns = ratio * float(best_ns)
            title_bits.append(f"~{ns:,.1f} ns/call ({testee})")
            data_ns = f' data-ns="{ns:.4f}"'
        except ValueError:
            pass
    title = " -- ".join(title_bits)
    return (f'<td class="cell"{dt}{data_ns} style="background:rgb({r},{g},{b});color:{fg}" '
            f'title="{html.escape(title)}">{ratio:.3f}x</td>')


PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root {{
  --bg: #f7f7f9; --fg: #1a1a1a; --border: #d8d8de; --head-bg: #eceef2;
  --sticky-bg: #ffffff; --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{
  :root {{ --bg: #14151a; --fg: #e8e8ea; --border: #34363f; --head-bg: #1d1f26; --sticky-bg: #191a20; }}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; padding: 1.25rem; background: var(--bg); color: var(--fg);
       font: 14px/1.4 -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; }}
h1 {{ font-size: 1.1rem; margin: 0 0 0.5rem; }}
pre.provenance {{ font-family: var(--mono); font-size: 11.5px; white-space: pre-wrap;
                  background: var(--head-bg); border: 1px solid var(--border);
                  border-radius: 6px; padding: 0.6rem 0.8rem; margin: 0 0 1rem;
                  max-height: 14rem; overflow: auto; }}
.legend {{ display: flex; flex-wrap: wrap; gap: 0.5rem 1rem; margin: 0 0 1rem; font-size: 12px; }}
.legend span.swatch {{ display: inline-block; width: 0.85em; height: 0.85em;
                       border-radius: 2px; margin-right: 0.35em; vertical-align: -0.1em; }}
.tablewrap {{ overflow: auto; max-height: 80vh; border: 1px solid var(--border);
             border-radius: 6px; }}
table {{ border-collapse: collapse; font-family: var(--mono); font-size: 12px; min-width: 100%; }}
th, td {{ padding: 0.3rem 0.55rem; border-bottom: 1px solid var(--border);
         border-right: 1px solid var(--border); white-space: nowrap; text-align: left; }}
thead th {{ position: sticky; top: 0; background: var(--head-bg); z-index: 2; }}
tbody th, td.rowhead {{ position: sticky; left: 0; background: var(--sticky-bg); z-index: 1; }}
td.cell {{ text-align: right; }}
.chip-unsup    {{ background: #8b8b8b; color: #fff; text-align: center; }}
.chip-refused  {{ background: #7c3aed; color: #fff; text-align: center; }}
.chip-wrong    {{ background: #b91c1c; color: #fff; text-align: center; }}
.chip-gaveup   {{ background: #d97706; color: #fff; text-align: center; }}
.chip-no-expectation {{ background: #0891b2; color: #fff; text-align: center; }}
.chip-excluded {{ background: #4b5563; color: #fff; text-align: center; }}
h2 {{ font-size: 1rem; margin: 1.25rem 0 0.5rem; }}
p.viewnote {{ font-size: 12.5px; margin: 0 0 0.75rem; max-width: 70ch; }}
fieldset.selection {{ border: 1px solid var(--border); border-radius: 6px; margin: 0 0 1rem;
                      padding: 0.5rem 0.8rem; }}
fieldset.selection legend {{ font-weight: 600; font-size: 12.5px; }}
.selboxes {{ display: flex; flex-wrap: wrap; gap: 0.25rem 1rem; font-size: 12px; }}
.selbtns {{ margin: 0 0 0.5rem; font-size: 12px; }}
.selbtns button {{ font: inherit; padding: 0.1rem 0.5rem; }}
footer {{ margin-top: 0.75rem; font-size: 11px; opacity: 0.7; }}
</style>
</head>
<body>
<h1>{title}</h1>
<pre class="provenance">{provenance}</pre>
<div class="legend">
  <span><span class="swatch" style="background:rgb(56,161,255)"></span>1.0x (at par)</span>
  <span><span class="swatch" style="background:rgb(220,38,38)"></span>&ge;10<sup>{log_max}</sup>x (far behind)</span>
  {status_legend}
</div>
{tables}
<footer>Generated by scripts/matrix_page.py from {source} -- dependency-free, regenerate on demand.</footer>
</body>
</html>
"""


def _table_html(rows, testees):
    """One `<table>...</table>` (sticky header/rowhead as before) over
    `rows`, restricted to `testees`' columns. Shared by the single-matrix
    render and each of the [B82] class-pure splits."""
    head_cells = ["<th>subbench</th>", "<th>pattern</th>", "<th>regime</th>", "<th>form</th>",
                  "<th>best_testee</th>", "<th>best_ns</th>"]
    head_cells += [f'<th data-t="{html.escape(t)}">{html.escape(t)}</th>' for t in testees]
    body_rows = []
    for row in rows:
        best_ns = row.get("best_ns") or ""
        cells = [
            f'<th class="rowhead">{html.escape(row["subbench"])}</th>',
            f'<td>{html.escape(row["pattern"])}</td>',
            f'<td>{html.escape(row["regime_or_na"]) or "&mdash;"}</td>',
            f'<td>{html.escape(row["form"]) or "&mdash;"}</td>',
            f'<td class="best-t">{html.escape(row["best_testee"]) or "&mdash;"}</td>',
            f'<td class="best-ns">{html.escape(best_ns) or "&mdash;"}</td>',
        ]
        cells += [_cell_html(row, t, best_ns) for t in testees]
        body_rows.append("<tr>" + "".join(cells) + "</tr>")
    return (f'<table>\n<thead><tr>{"".join(head_cells)}</tr></thead>\n'
            f'<tbody>\n{chr(10).join(body_rows)}\n</tbody>\n</table>')


def _selection_html(testees):
    """[B91] (Frank's ruling, 2026-09-25: "calculate best based on what
    is currently selected"): one checkbox per testee in the roster, all
    checked. The page script (`SELECTION_SCRIPT`) recomputes every
    table's per-row best and every ratio over the checked testees only --
    the results viewer's own `computeBest` rule (the lowest `data-ns`
    among the row's selected ratio cells; a status-token cell is never a
    candidate) -- and hides the unchecked columns. With scripting off
    the page is the full-roster render below, unchanged in meaning."""
    boxes = "".join(
        f'<label><input type="checkbox" class="sel" value="{html.escape(t)}" checked> '
        f'<code>{html.escape(t)}</code></label>'
        for t in testees)
    return (
        '<fieldset class="selection"><legend>Testee selection</legend>'
        '<p class="viewnote">Each row\'s best and every ratio are recomputed '
        "over the testees selected here (the lowest measured median among "
        "the SELECTED cells of that row and table; a status-token cell is "
        "never a candidate). Unselected columns are hidden. With scripting "
        "off, the tables show the file's own fixed bests: pooled over the "
        "whole roster, or class-pure in the split tables.</p>"
        '<div class="selbtns"><button type="button" data-act="all">all</button> '
        '<button type="button" data-act="none">none</button> '
        '<span class="selcount"></span></div>'
        f'<div class="selboxes">{boxes}</div></fieldset>')


# [B91]: the selection recompute, mirroring `_ratio_color`'s ramp exactly
# (log10(max(ratio, 1)) / LOG_MAX, clamped, linear RGB between the two
# stops; text colour flips at t = 0.55) so a recomputed cell is shaded
# the same way a static one is. With every testee selected the recompute
# reproduces the static render (same best, same ratios).
SELECTION_SCRIPT = """<script>
(function () {
  var LOG_MAX = %(log_max)d;
  function ramp(ratio) {
    var t = Math.log10(Math.max(ratio, 1.0)) / LOG_MAX;
    if (!isFinite(t)) t = 0;
    t = Math.max(0, Math.min(1, t));
    var lo = [56, 161, 255], hi = [220, 38, 38];
    var c = lo.map(function (v, i) { return Math.round(v + (hi[i] - v) * t); });
    return { bg: "rgb(" + c.join(",") + ")", fg: t < 0.55 ? "#0b0b0b" : "#fbfbfb" };
  }
  function selected() {
    var s = {};
    document.querySelectorAll("input.sel").forEach(function (b) { if (b.checked) s[b.value] = true; });
    return s;
  }
  function apply() {
    var sel = selected();
    var n = Object.keys(sel).length, total = document.querySelectorAll("input.sel").length;
    var cnt = document.querySelector(".selcount");
    if (cnt) cnt.textContent = n + " of " + total + " selected";
    document.querySelectorAll("th[data-t], td[data-t]").forEach(function (el) {
      el.style.display = sel[el.getAttribute("data-t")] ? "" : "none";
    });
    document.querySelectorAll("table tbody tr").forEach(function (tr) {
      var bestNs = null, bestT = null;
      tr.querySelectorAll("td[data-ns]").forEach(function (td) {
        var t = td.getAttribute("data-t");
        if (!sel[t]) return;
        var ns = parseFloat(td.getAttribute("data-ns"));
        if (bestNs === null || ns < bestNs) { bestNs = ns; bestT = t; }
      });
      var bt = tr.querySelector("td.best-t"), bn = tr.querySelector("td.best-ns");
      if (bt) bt.textContent = bestT === null ? "\u2014" : bestT;
      if (bn) bn.textContent = bestNs === null ? "\u2014" : bestNs.toFixed(1);
      if (bestNs === null || !(bestNs > 0)) return;
      tr.querySelectorAll("td[data-ns]").forEach(function (td) {
        var ns = parseFloat(td.getAttribute("data-ns"));
        var ratio = ns / bestNs, c = ramp(ratio);
        td.textContent = ratio.toFixed(3) + "x";
        td.style.background = c.bg;
        td.style.color = c.fg;
        td.title = ratio.toFixed(3) + "x this row's best (over the selection) -- ~" +
          ns.toLocaleString("en-US", { minimumFractionDigits: 1, maximumFractionDigits: 1 }) +
          " ns/call (" + td.getAttribute("data-t") + ")";
      });
    });
  }
  document.querySelectorAll("input.sel").forEach(function (b) { b.addEventListener("change", apply); });
  document.querySelectorAll(".selbtns button").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var on = btn.getAttribute("data-act") === "all";
      document.querySelectorAll("input.sel").forEach(function (b) { b.checked = on; });
      apply();
    });
  });
  apply();
})();
</script>"""


def render_html(provenance_lines, header, rows, source_path):
    testees = header[fixed_count(header):]
    title = f"Capability ratio matrix -- {os.path.basename(source_path)}"
    provenance = html.escape("\n".join(provenance_lines) or "(no provenance header found)")
    status_legend = "".join(
        f'<span><span class="swatch {cls}" style="width:1.1em;height:1.1em;'
        f'display:inline-flex;align-items:center;justify-content:center;'
        f'color:#fff;font-size:9px;border-radius:3px">{html.escape(tok)}</span> '
        f'{html.escape(desc)}</span>'
        for tok, (cls, desc) in STATUS_CHIPS.items())

    # [B82] (inbox I-99/I-100): TWO MATRICES when the file's roster spans
    # both capture classes, ONE (today's shape, byte for byte) otherwise
    # -- "compare capturing vs capturing and non-capturing vs
    # non-capturing... never a cross-class cell." An `undeclared` testee
    # (I-99's fail-loud rule) is excluded from BOTH tables and named in
    # its own note rather than guessed into either.
    yes_t, no_t, undeclared_t = parse_capture_class(provenance_lines)
    yes_t = [t for t in yes_t if t in testees]
    no_t = [t for t in no_t if t in testees]
    undeclared_t = [t for t in undeclared_t if t in testees]
    spans_both = bool(yes_t) and bool(no_t)

    if spans_both:
        yes_rows = [class_pure_row(r, yes_t) for r in rows]
        no_rows = [class_pure_row(r, no_t) for r in rows]
        tables_html = (
            '<p class="viewnote"><strong>Two class-pure matrices below '
            "(inbox I-99/I-100): a capturing config's ratio is never "
            "compared against a non-capturing config's -- each table's "
            "own best_testee/best_ns is recomputed WITHIN its class from "
            "this file's own ratio x best_ns (never a second reduction "
            "over the store). See the provenance's own \"capture_class "
            'disclosure\" note for what this file\'s FLAT columns above '
            "(unused here) would have mixed.</strong></p>\n"
            '<h2>Capturing engines only (caps vs caps)</h2>\n'
            '<div class="tablewrap">' + _table_html(yes_rows, yes_t) + '</div>\n'
            '<h2>Non-capturing engines only (nocaps vs nocaps)</h2>\n'
            '<div class="tablewrap">' + _table_html(no_rows, no_t) + '</div>')
        if undeclared_t:
            tables_html += (
                '\n<p class="viewnote">Undeclared capture class (I-99: '
                "never guessed -- excluded from both tables above): "
                + ", ".join(f"<code>{html.escape(t)}</code>" for t in undeclared_t)
                + "</p>")
    else:
        tables_html = '<div class="tablewrap">' + _table_html(rows, testees) + '</div>'

    # [B91]: the selection offers exactly the testees the tables show
    # (an undeclared testee in a class-split page is in neither table).
    selectable = (yes_t + no_t) if spans_both else testees
    page = PAGE_TEMPLATE.format(
        title=html.escape(title), provenance=provenance, log_max=LOG_MAX,
        status_legend=status_legend,
        tables=_selection_html(selectable) + "\n" + tables_html,
        source=html.escape(source_path))
    return page.replace("</body>", SELECTION_SCRIPT % {"log_max": LOG_MAX} + "\n</body>", 1)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("matrix_tsv", help="a `.matrix.tsv` file (pcrecbench report --format matrix)")
    ap.add_argument("-o", "--out", default=None,
                    help="output HTML path (default: alongside the input, .html)")
    args = ap.parse_args(argv)

    try:
        provenance_lines, header, rows = parse_matrix_tsv(args.matrix_tsv)
    except MatrixParseError as exc:
        print(f"matrix_page: {exc}", file=sys.stderr)
        return 1

    out_path = args.out
    if out_path is None:
        base = args.matrix_tsv
        if base.endswith(".matrix.tsv"):
            out_path = base[: -len(".tsv")] + ".html"
        else:
            out_path = base + ".html"

    page = render_html(provenance_lines, header, rows, args.matrix_tsv)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"wrote {out_path} ({len(rows)} row(s), {len(header) - fixed_count(header)} testee(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
