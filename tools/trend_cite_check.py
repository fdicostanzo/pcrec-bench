#!/usr/bin/env python3
"""tools/trend_cite_check.py -- the AI interpretation's citation check ([B130], R9/R9+).

    python3 tools/trend_cite_check.py reports/trend/interpretation/<pin>.md [--dir reports/trend]

An interpretation sidecar cites TSV rows as `[#<row_id>]` (ids of deltas.tsv,
summary.tsv, cells.tsv, compile_deltas.tsv, deny_twins.tsv). The check:
  1. every cited id exists in a row_id column of those TSVs, read FROM THE
     TSV FILES (or their texts) by this module's own parser;
  2. every paragraph / bullet / table-free text block carries at least one
     citation, unless it starts with `NOT KNOWN:` (R9 allows naming what is
     not known) or is a heading.
It deliberately imports NOTHING from tools/trend.py or tools/trend_html.py
(R9+: the check shares no source with what it checks); the only coupling is
the TSV file format (`#` header lines, tab-separated, a `row_id` column).
Exit 0 clean, 1 on any problem.
"""
import html
import os
import re
import sys

CITE = re.compile(r"\[#([^\]\s]+)\]")
ID_FILES = ("deltas.tsv", "summary.tsv", "cells.tsv", "compile_deltas.tsv",
            "deny_twins.tsv")


def ids_from_texts(files):
    """{relative name: text} -> set of row ids."""
    ids = set()
    for name, text in files.items():
        if os.path.basename(name) not in ID_FILES:
            continue
        col = None
        for ln in text.split("\n"):
            if not ln or ln.startswith("#"):
                continue
            cells = ln.split("\t")
            if col is None:
                col = cells.index("row_id") if "row_id" in cells else -1
                continue
            if col >= 0 and col < len(cells):
                ids.add(cells[col])
    return ids


def ids_from_dir(d):
    files = {}
    for n in ID_FILES:
        p = os.path.join(d, n)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                files[n] = f.read()
    return ids_from_texts(files)


def blocks(text):
    """Text blocks that must be cited: paragraphs and list items."""
    out, cur = [], []
    for ln in text.split("\n"):
        s = ln.strip()
        if not s:
            if cur:
                out.append(" ".join(cur))
                cur = []
        elif s.startswith("#"):
            if cur:
                out.append(" ".join(cur))
                cur = []
        elif s[:2] in ("- ", "* ") or re.match(r"\d+\. ", s):
            if cur:
                out.append(" ".join(cur))
            cur = [s]
        else:
            cur.append(s)
    if cur:
        out.append(" ".join(cur))
    return out


def check_text(text, ids):
    """-> list of problems (strings)."""
    errs = []
    for m in CITE.finditer(text):
        if m.group(1) not in ids:
            errs.append("unknown id: " + m.group(1))
    for b in blocks(text):
        body = re.sub(r"^([-*]|\d+\.)\s+", "", b)
        if body.startswith("NOT KNOWN:") or body.startswith("<!--"):
            continue
        if not CITE.search(b):
            errs.append("uncited: " + body[:60])
    return errs


def render_md(text, ids):
    """Minimal markdown to HTML; a cited id becomes an in-page link when the
    id is on the page (the caller's anchors), else a <code> chip."""
    out = []
    in_list = False
    for ln in text.split("\n"):
        s = ln.rstrip()
        esc = html.escape(s)
        esc = CITE.sub(lambda m: f'<a href="#{html.escape(m.group(1))}"><code>'
                       f'{html.escape(m.group(1))}</code></a>',
                       esc.replace("[#", "[#"))
        esc = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc)
        if s.startswith("#"):
            if in_list:
                out.append("</ul>")
                in_list = False
            lvl = min(len(s) - len(s.lstrip("#")) + 2, 5)
            out.append(f"<h{lvl}>{esc.lstrip('# ')}</h{lvl}>")
        elif s[:2] in ("- ", "* "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{esc[2:]}</li>")
        elif not s:
            if in_list:
                out.append("</ul>")
                in_list = False
        else:
            out.append(f"<p>{esc}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("sidecar")
    ap.add_argument("--dir", default=os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports", "trend"))
    a = ap.parse_args(argv)
    with open(a.sidecar, encoding="utf-8") as f:
        text = f.read()
    errs = check_text(text, ids_from_dir(a.dir))
    for e_ in errs:
        print("trend_cite_check:", e_)
    print(f"trend_cite_check: {a.sidecar}: {len(errs)} problem(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
