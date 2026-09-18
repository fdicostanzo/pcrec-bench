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

THIS IS THE COMMITTED VISUAL REFERENCE Frank's ruling names (docs/dev/
dev_journal.md, 2026-09-18 close, [B52] charter item 4): the ad hoc page
built for the reset-session reading of the capability window is what
this script is a maintained, from-a-`.matrix.tsv`, from-scratch
generator FOR -- it takes no input but the TSV file and writes no
`.tsv` of its own, so the TSV stays canonical (charter item 1) and this
HTML stays DERIVED, regenerable from it at any time.

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
import sys

FIXED_COLS = ["subbench", "pattern", "regime_or_na", "form", "best_testee", "best_ns"]

# The five CLOSED status tokens `render_matrix_tsv` ever prints in place
# of a ratio (its own module-docstring [B52] section) -- one fixed chip
# colour per token, deliberately NOT on the log-scale ramp: a status
# token is a FACT about why nothing was timed, not a magnitude to shade
# by. `checked in this order` in `report.py`'s docstring is a compile
# rule for `_matrix_cell`, not a display rule here -- this dict is keyed
# by the rendered string, order irrelevant.
STATUS_CHIPS = {
    "unsup": ("chip-unsup", "unsupported-by-declaration (the testee's own "
              "advance capability declaration, not an engine failure)"),
    "refused": ("chip-refused", "did-not-compile"),
    "wrong": ("chip-wrong", "excluded: n_wrong > 0 (a wrong answer)"),
    "gave-up": ("chip-gaveup", "excluded: n_gave_up > 0, no wrong answer"),
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
                if header[:len(FIXED_COLS)] != FIXED_COLS or len(header) <= len(FIXED_COLS):
                    raise MatrixParseError(
                        f"{path}:{lineno}: header {header!r} does not start with "
                        f"{FIXED_COLS!r} plus at least one testee column")
                continue
            if len(cols) != len(header):
                raise MatrixParseError(
                    f"{path}:{lineno}: row has {len(cols)} column(s), "
                    f"header has {len(header)}: {cols!r}")
            rows.append(dict(zip(header, cols)))
    if header is None:
        raise MatrixParseError(f"{path}: no header row found (file empty or all-comment)")
    return provenance_lines, header, rows


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
    if raw in STATUS_CHIPS:
        cls, title = STATUS_CHIPS[raw]
        return (f'<td class="cell {cls}" title="{html.escape(title)}">'
                f'{html.escape(raw)}</td>')
    try:
        ratio = float(raw)
    except ValueError:
        return f'<td class="cell chip-excluded" title="unparseable cell">{html.escape(raw)}</td>'
    r, g, b, t = _ratio_color(ratio)
    fg = "#0b0b0b" if t < 0.55 else "#fbfbfb"
    title_bits = [f"{ratio:.3f}x this row's best"]
    if best_ns:
        try:
            title_bits.append(f"~{ratio * float(best_ns):,.1f} ns/call ({testee})")
        except ValueError:
            pass
    title = " -- ".join(title_bits)
    return (f'<td class="cell" style="background:rgb({r},{g},{b});color:{fg}" '
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
.chip-excluded {{ background: #4b5563; color: #fff; text-align: center; }}
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
<div class="tablewrap">
<table>
<thead><tr>{head_row}</tr></thead>
<tbody>
{body_rows}
</tbody>
</table>
</div>
<footer>Generated by scripts/matrix_page.py from {source} -- dependency-free, regenerate on demand.</footer>
</body>
</html>
"""


def render_html(provenance_lines, header, rows, source_path):
    testees = header[len(FIXED_COLS):]
    title = f"Capability ratio matrix -- {os.path.basename(source_path)}"
    provenance = html.escape("\n".join(provenance_lines) or "(no provenance header found)")
    status_legend = "".join(
        f'<span><span class="swatch {cls}" style="width:1.1em;height:1.1em;'
        f'display:inline-flex;align-items:center;justify-content:center;'
        f'color:#fff;font-size:9px;border-radius:3px">{html.escape(tok)}</span> '
        f'{html.escape(desc)}</span>'
        for tok, (cls, desc) in STATUS_CHIPS.items())
    head_cells = ["<th>subbench</th>", "<th>pattern</th>", "<th>regime</th>", "<th>form</th>",
                  "<th>best_testee</th>", "<th>best_ns</th>"]
    head_cells += [f"<th>{html.escape(t)}</th>" for t in testees]
    body_rows = []
    for row in rows:
        best_ns = row.get("best_ns") or ""
        cells = [
            f'<th class="rowhead">{html.escape(row["subbench"])}</th>',
            f'<td>{html.escape(row["pattern"])}</td>',
            f'<td>{html.escape(row["regime_or_na"]) or "&mdash;"}</td>',
            f'<td>{html.escape(row["form"]) or "&mdash;"}</td>',
            f'<td>{html.escape(row["best_testee"]) or "&mdash;"}</td>',
            f'<td>{html.escape(best_ns) or "&mdash;"}</td>',
        ]
        cells += [_cell_html(row, t, best_ns) for t in testees]
        body_rows.append("<tr>" + "".join(cells) + "</tr>")
    return PAGE_TEMPLATE.format(
        title=html.escape(title), provenance=provenance, log_max=LOG_MAX,
        status_legend=status_legend, head_row="".join(head_cells),
        body_rows="\n".join(body_rows), source=html.escape(source_path))


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
    print(f"wrote {out_path} ({len(rows)} row(s), {len(header) - len(FIXED_COLS)} testee(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
