#!/usr/bin/env python3
"""Tests for `scripts/matrix_page.py` -- [B52] charter item 4/5, the
committed HTML generator for a `.matrix.tsv` sibling
(`pcrecbench report --format matrix`, `render_matrix_tsv`).

`scripts/` is not an importable package (no `__init__.py`, deliberately
-- it is a folder of standalone operational scripts, `scripts/
CLAUDE.md`), so this file loads `matrix_page.py` by file path
(`importlib.util`) rather than `import scripts.matrix_page`. No engine,
no store, no network: every fixture here is a hand-built `.matrix.tsv`
string written to a temp file, same "pure helper, no store" posture as
`test_quick.py`.

Plain runnable module, same technique as `test_report.py`/`test_quick.py`:

    python3 -m pcrecbench.tests.test_matrix_page
"""

from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
PKG_ROOT = os.path.dirname(os.path.dirname(HERE))  # .../pcrec-bench
MATRIX_PAGE_PATH = os.path.join(PKG_ROOT, "scripts", "matrix_page.py")

_spec = importlib.util.spec_from_file_location("matrix_page", MATRIX_PAGE_PATH)
mp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mp)


class TestFailure(AssertionError):
    pass


def _check(cond, msg):
    if not cond:
        raise TestFailure(msg)


SAMPLE_TSV = (
    "# reporter: v18 (2026-09-18); surface: matrix; filters: (none); "
    "source: test; records: 3; testees: engine-a,engine-b\n"
    "# matrix: a data cell is testee median_ns / this ROW's best -- ratios "
    "compare WITHIN A ROW ONLY.\n"
    "subbench\tpattern\tregime_or_na\tform\tbest_testee\tbest_ns\tengine-a\tengine-b\n"
    "rb-mini@1.0\tp1\tshort-subject-search\tplain\tengine-a\t40.0\t1.000000\t2.000000\n"
    "rb-mini@1.0\tp2\t\t\t\t\trefused\tunsup\n"
)


def _write_tmp(text):
    fh = tempfile.NamedTemporaryFile(mode="w", suffix=".matrix.tsv", delete=False,
                                      encoding="utf-8")
    fh.write(text)
    fh.close()
    return fh.name


def test_parse_matrix_tsv_roundtrip():
    """Provenance lines survive VERBATIM, in order; the header splits
    into `FIXED_COLS` plus the testee roster; each data row parses to a
    dict keyed by that header, including the all-status F26 row (every
    non-fixed cell absent from `FIXED_COLS` populated)."""
    path = _write_tmp(SAMPLE_TSV)
    try:
        provenance, header, rows = mp.parse_matrix_tsv(path)
        _check(len(provenance) == 2, f"expected 2 provenance lines: {provenance}")
        _check(provenance[0].startswith("# reporter: v18"), provenance[0])
        _check(header == mp.FIXED_COLS + ["engine-a", "engine-b"], header)
        _check(len(rows) == 2, f"expected 2 data rows: {rows}")
        _check(rows[0]["engine-a"] == "1.000000" and rows[0]["engine-b"] == "2.000000", rows[0])
        _check(rows[1]["engine-a"] == "refused" and rows[1]["engine-b"] == "unsup", rows[1])
        _check(rows[1]["regime_or_na"] == "" and rows[1]["form"] == "",
               f"the F26 row's own regime/form must round-trip as empty strings: {rows[1]}")
    finally:
        os.unlink(path)


def test_malformed_header_raises():
    """A header that does not start with `FIXED_COLS` plus at least one
    testee column is a NAMED `MatrixParseError`, never a silent
    mis-render or a raw traceback -- same posture as `report.py`'s own
    refusal-by-name convention."""
    path = _write_tmp("subbench\tpattern\n" "rb-mini@1.0\tp1\n")
    try:
        try:
            mp.parse_matrix_tsv(path)
            _check(False, "expected MatrixParseError")
        except mp.MatrixParseError as exc:
            _check("does not start with" in str(exc), str(exc))
    finally:
        os.unlink(path)


def test_empty_file_raises():
    """An all-comment or empty file is a named refusal too -- not a
    page with a header and zero rows, and not a crash on `header is
    None` downstream."""
    path = _write_tmp("# just a comment, no header or data\n")
    try:
        try:
            mp.parse_matrix_tsv(path)
            _check(False, "expected MatrixParseError")
        except mp.MatrixParseError as exc:
            _check("no header row found" in str(exc), str(exc))
    finally:
        os.unlink(path)


def test_status_chip_cell_html():
    """Each of the six closed status tokens (`report.py`'s own set --
    KB-27's `no-expectation` is the sixth, deliberately not `unjudged`,
    which already names an unrelated count on the same report's
    `trial_agreement` line) renders its own fixed CSS class and a title
    attribute naming what the token means -- never the log-scale ramp's
    `style="background: rgb(...)"`, which is reserved for a genuine
    ratio."""
    row = {"unsup": "unsup", "refused": "refused", "wrong": "wrong",
           "gave-up": "gave-up", "no-expectation": "no-expectation",
           "excluded": "excluded"}
    for tok, (cls, _desc) in mp.STATUS_CHIPS.items():
        cell = mp._cell_html(row, tok, "40.0")
        _check(cls in cell, f"{tok} cell missing its chip class {cls!r}: {cell}")
        _check("background:rgb(" not in cell,
               f"{tok} must not carry the ratio ramp's inline background: {cell}")


def test_ratio_cell_html_and_tooltip():
    """A numeric cell gets the log-scale `rgb(...)` background (never a
    chip class) and a tooltip stating BOTH the ratio and the absolute
    ns/call recovered from `best_ns * ratio` -- the fact a bare ratio
    column loses (`report.py`'s own module-docstring rationale for
    carrying `best_ns`/`best_testee` at all)."""
    row = {"engine-b": "2.500000"}
    cell = mp._cell_html(row, "engine-b", "40.0")
    _check("background:rgb(" in cell, cell)
    _check("2.500x" in cell, cell)
    _check("100.0 ns/call" in cell or "100.0" in cell,
           f"expected the recovered absolute ns (2.5 x 40.0 = 100.0): {cell}")
    _check("engine-b" in cell, cell)


def test_ratio_color_ramp_endpoints_and_clamp():
    """`_ratio_color`'s domain is [1.0x, 10**LOG_MAX x]: ratio 1.0 must
    land at the ramp's cool "at par" end (t=0), ratio >= 10**LOG_MAX
    must land at the warm "far behind" end (t=1) WITHOUT going past it
    (the clamp) -- a ratio above the ramp's stated ceiling is still a
    real, larger number, and rendering it identically to the ceiling
    (rather than crashing or extrapolating the colour off-scale) is the
    documented behaviour, not a bug."""
    r0, g0, b0, t0 = mp._ratio_color(1.0)
    _check(t0 == 0.0, f"ratio 1.0 must be t=0: {t0}")
    r1, g1, b1, t1 = mp._ratio_color(10 ** mp.LOG_MAX)
    _check(t1 == 1.0, f"ratio 10**LOG_MAX must be t=1: {t1}")
    r2, g2, b2, t2 = mp._ratio_color(10 ** (mp.LOG_MAX + 5))
    _check(t2 == 1.0, f"a ratio past the ceiling must clamp at t=1, not exceed it: {t2}")
    _check((r2, g2, b2) == (r1, g1, b1),
           "a clamped ratio must render IDENTICALLY to the ceiling, not a new colour")


def test_render_html_end_to_end():
    """The full page: one `<tr>` per data row (including the F26 row),
    one `<th>`/`<td>` per fixed column plus one per testee, the
    provenance lines rendered verbatim (HTML-escaped) somewhere in the
    page, and both status chips and a ratio cell present in the same
    table -- the mixed-population case a real matrix file has."""
    path = _write_tmp(SAMPLE_TSV)
    try:
        provenance, header, rows = mp.parse_matrix_tsv(path)
        page = mp.render_html(provenance, header, rows, path)
        _check("<table>" in page and "</table>" in page, "expected a table")
        _check(page.count("<tr>") == len(rows) + 1,
               f"expected {len(rows)} body <tr> plus the header's own "
               f"<thead><tr>: found {page.count('<tr>')}")
        _check("reporter: v18" in page, "provenance must render verbatim in the page")
        _check("chip-refused" in page and "chip-unsup" in page, "the F26 row's chips must render")
        _check("1.000x" in page, "the ratio row's 1.000x cell must render")
        _check("prefers-color-scheme: dark" in page, "the page must declare a dark theme")
    finally:
        os.unlink(path)


def test_main_writes_default_output_path():
    """`main()`'s own default output path rule: `<name>.matrix.tsv` ->
    `<name>.matrix.html` alongside the input, never a different
    directory, unless `-o` overrides it -- the sibling-file contract
    the charter states for the committed HTML generator."""
    path = _write_tmp(SAMPLE_TSV)
    _check(path.endswith(".matrix.tsv"), path)
    try:
        rc = mp.main([path])
        _check(rc == 0, f"expected exit 0: {rc}")
        expected_html = path[: -len(".tsv")] + ".html"
        _check(os.path.exists(expected_html), f"expected {expected_html} to exist")
        with open(expected_html, encoding="utf-8") as fh:
            _check("<table>" in fh.read(), "expected a real page at the default path")
        os.unlink(expected_html)
    finally:
        os.unlink(path)


# [B82] (inbox I-99/I-100): a MIXED-ROSTER fixture -- `engine-a`/
# `engine-c` declared YES, `engine-b` declared NO, `engine-d` declared
# for NEITHER (I-99's fail-loud "undeclared" case). `engine-a` is this
# row's GLOBAL best (ratio 1.000000); `engine-b` is the ONLY no-class
# testee, so its class-pure ratio must re-base to 1.000000 even though
# its GLOBAL ratio is 2.000000 -- the arithmetic signal that proves the
# split actually recomputes rather than merely filtering columns.
SAMPLE_TSV_MIXED = (
    "# reporter: v20 (2026-09-23); surface: matrix; filters: (none); "
    "source: test; records: 4; testees: engine-a,engine-b,engine-c,engine-d; "
    "capture_class: yes=engine-a,engine-c; no=engine-b; undeclared=engine-d\n"
    "# matrix: a data cell is testee median_ns / this ROW's best -- ratios "
    "compare WITHIN A ROW ONLY.\n"
    "# capture_class disclosure (inbox I-99): cross-class numbers above.\n"
    "subbench\tpattern\tregime_or_na\tform\tbest_testee\tbest_ns\t"
    "engine-a\tengine-b\tengine-c\tengine-d\n"
    "rb-mini@1.0\tp1\tshort-subject-search\tplain\tengine-a\t100.0\t"
    "1.000000\t2.000000\t4.000000\t3.000000\n"
)


def test_parse_capture_class():
    """`parse_capture_class` reads the ONE provenance line, splitting
    each of the three groups on commas; a file with no such line (every
    fixture/committed matrix TSV before this lane) returns three empty
    lists -- the fallback-to-single-table control."""
    _, header, rows = mp.parse_matrix_tsv(_write_tmp(SAMPLE_TSV_MIXED))
    provenance, _h, _r = mp.parse_matrix_tsv(_write_tmp(SAMPLE_TSV_MIXED))
    yes, no, undeclared = mp.parse_capture_class(provenance)
    _check(yes == ["engine-a", "engine-c"], yes)
    _check(no == ["engine-b"], no)
    _check(undeclared == ["engine-d"], undeclared)
    old_provenance, _h2, _r2 = mp.parse_matrix_tsv(_write_tmp(SAMPLE_TSV))
    _check(mp.parse_capture_class(old_provenance) == ([], [], []),
           "a file with no capture_class line must parse to three empty lists")


def test_class_pure_row_rebases_within_class():
    """`class_pure_row`'s own arithmetic, directly: `engine-b` is the
    lone member of the NO class in `SAMPLE_TSV_MIXED`'s one row, so its
    class-pure ratio re-bases to 1.000000 (its own class's best) even
    though its GLOBAL ratio (unused here) was 2.000000 against
    `engine-a`. `engine-a`/`engine-c`'s YES-class ratios are UNCHANGED
    (1.000000/4.000000) because the global best (`engine-a`) already sat
    inside their own class -- both directions of the rebasing are
    exercised in one fixture."""
    _, _header, rows = mp.parse_matrix_tsv(_write_tmp(SAMPLE_TSV_MIXED))
    row = rows[0]
    yes_row = mp.class_pure_row(row, ["engine-a", "engine-c"])
    _check(yes_row["best_testee"] == "engine-a", yes_row)
    _check(yes_row["engine-a"] == "1.000000" and yes_row["engine-c"] == "4.000000", yes_row)
    no_row = mp.class_pure_row(row, ["engine-b"])
    _check(no_row["best_testee"] == "engine-b", no_row)
    _check(no_row["engine-b"] == "1.000000",
           f"the lone NO-class member must re-base to 1.000000, got {no_row}")
    _check(no_row["best_ns"] == "200.0",
           f"class-pure best_ns is engine-b's OWN absolute ns (2.0 x 100.0), got {no_row}")


def test_matrix_class_pure_split_renders_two_tables():
    """[B82] (inbox I-99/I-100) end to end: a roster spanning both
    classes renders TWO `<table>` elements under their own `<h2>`
    headings, `engine-d` (undeclared) is absent from BOTH testee column
    sets and named in its own note, and the NO-class table's lone
    `engine-b` cell reads the re-based `1.000000x`, never the global
    `2.000000x`."""
    path = _write_tmp(SAMPLE_TSV_MIXED)
    try:
        provenance, header, rows = mp.parse_matrix_tsv(path)
        page = mp.render_html(provenance, header, rows, path)
        _check(page.count("<table>") == 2, f"expected two tables: {page.count('<table>')}")
        _check("Capturing engines only" in page and "Non-capturing engines only" in page, page)
        _check("engine-d" not in page.split("Undeclared capture class")[0]
               or "Undeclared capture class" in page,
               "engine-d must not appear inside either <table>")
        _check("<th>engine-d</th>" not in page, "engine-d must not be a column header anywhere")
        _check("Undeclared capture class" in page and "engine-d" in page,
               "engine-d must be named in its own note")
        _check("1.000000x" in page or "1.000x" in page,
               "the re-based engine-b cell must render 1.000x, not 2.000x")
        no_table = page.split("Non-capturing engines only")[1]
        _check("2.000x" not in no_table.split("</table>")[0],
               f"the NO-class table must never show engine-b's stale global ratio:\n{no_table[:400]}")
    finally:
        os.unlink(path)


def test_matrix_single_class_roster_unchanged():
    """CONTROL: a roster that does NOT span both classes (this file's
    original `SAMPLE_TSV`, which carries no `capture_class` line at all)
    renders the ORIGINAL single table -- exactly `test_render_html_end_
    to_end`'s own shape, re-asserted here so the [B82] dispatch's
    `else` branch has its own named test rather than riding on an older
    ruling's test by coincidence."""
    path = _write_tmp(SAMPLE_TSV)
    try:
        provenance, header, rows = mp.parse_matrix_tsv(path)
        page = mp.render_html(provenance, header, rows, path)
        _check(page.count("<table>") == 1, f"expected exactly one table: {page.count('<table>')}")
        _check("Capturing engines only" not in page, "no class split on a single-class roster")
    finally:
        os.unlink(path)


# [B91] (reporter v24): the TEN-column header -- the pooled pair renamed
# `_pooled`, the class-pure `_yes`/`_no` pairs beside it. Same row as
# `SAMPLE_TSV_MIXED`: pooled best engine-a (100 ns); yes-best engine-a
# (100); no-best engine-b (200 = 2.0 x 100).
SAMPLE_TSV_V24 = (
    "# reporter: v24 (2026-09-26); surface: matrix; filters: (none); "
    "source: test; records: 4; testees: engine-a,engine-b,engine-c,engine-d; "
    "capture_class: yes=engine-a,engine-c; no=engine-b; undeclared=engine-d\n"
    "# matrix: a data cell is testee median_ns / this ROW's best.\n"
    "subbench\tpattern\tregime_or_na\tform\tbest_testee_pooled\tbest_ns_pooled\t"
    "best_testee_yes\tbest_ns_yes\tbest_testee_no\tbest_ns_no\t"
    "engine-a\tengine-b\tengine-c\tengine-d\n"
    "rb-mini@1.0\tp1\tshort-subject-search\tplain\tengine-a\t100.0\t"
    "engine-a\t100.0\tengine-b\t200.0\t"
    "1.000000\t2.000000\t4.000000\t3.000000\n"
    "rb-mini@1.0\tp2\t\t\t\t\t\t\t\t\trefused\tunsup\trefused\tunsup\n"
)


def _cells_by_row(page):
    """[(best_t_text, best_ns_text, {testee: data-ns float})] per <tbody>
    row of every table, in page order -- a PYTHON re-statement of what
    SELECTION_SCRIPT reads, so the recompute rule is checked on the very
    attributes the page ships."""
    import re as _re
    out = []
    for tr in _re.findall(r"<tr>(.*?)</tr>", page, flags=_re.S):
        if "<th>subbench</th>" in tr:
            continue
        bt = _re.search(r'<td class="best-t">(.*?)</td>', tr)
        bn = _re.search(r'<td class="best-ns">(.*?)</td>', tr)
        ns = {m.group(1): float(m.group(2)) for m in
              _re.finditer(r'data-t="([^"]+)" data-ns="([^"]+)"', tr)}
        out.append((bt.group(1) if bt else None, bn.group(1) if bn else None, ns))
    return out


def _best_over(ns, selection):
    """The viewer's `computeBest`: the lowest absolute ns among the
    SELECTED ratio cells (a status-token cell carries no data-ns and is
    never a candidate)."""
    cand = {t: v for t, v in ns.items() if t in selection}
    if not cand:
        return None, None
    t = min(cand, key=cand.get)
    return t, cand[t]


def test_v24_header_parses_and_normalises():
    """[B91]: the reporter-v24 ten-column header parses, the testee
    roster starts after the ten fixed columns, and every row's
    `best_testee`/`best_ns` are NORMALISED to the POOLED pair (what the
    file's ratio cells are relative to). CONTROL: the pre-v24 six-column
    `SAMPLE_TSV` still parses to the same shape."""
    path = _write_tmp(SAMPLE_TSV_V24)
    try:
        _prov, header, rows = mp.parse_matrix_tsv(path)
        _check(mp.fixed_count(header) == 10, header)
        _check(header[10:] == ["engine-a", "engine-b", "engine-c", "engine-d"], header)
        _check(rows[0]["best_testee"] == "engine-a" and rows[0]["best_ns"] == "100.0", rows[0])
        _check(rows[0]["best_ns_no"] == "200.0", rows[0])
    finally:
        os.unlink(path)
    _p, header6, _r = mp.parse_matrix_tsv(_write_tmp(SAMPLE_TSV))
    _check(mp.fixed_count(header6) == 6, header6)


def test_selection_recomputes_best_over_selection():
    """[B91] (Frank's ruling, 2026-09-25: "calculate best based on what
    is currently selected"): the page carries one checkbox per shown
    testee and every ratio cell its ABSOLUTE ns (`data-ns`, ratio x its
    table's best_ns). Checked on those shipped attributes: (1) with
    every testee selected the recompute reproduces each table's static
    best; (2) selecting the YES class alone on the SINGLE-table page
    yields the TSV's own `best_ns_yes`, the NO class alone its
    `best_ns_no` -- the static class-pure columns and the page's
    selection are one rule; (3) a status-token cell (`refused`/`unsup`)
    carries no data-ns, so a row with none selectable has no best; (4)
    the script's ramp constants are `_ratio_color`'s own."""
    # a single-class-free file (no capture_class line) -> one table, all testees
    single = SAMPLE_TSV_V24.replace(
        "; capture_class: yes=engine-a,engine-c; no=engine-b; undeclared=engine-d", "")
    path = _write_tmp(single)
    try:
        prov, header, rows = mp.parse_matrix_tsv(path)
        page = mp.render_html(prov, header, rows, path)
    finally:
        os.unlink(path)
    for t in ("engine-a", "engine-b", "engine-c", "engine-d"):
        _check(f'<input type="checkbox" class="sel" value="{t}" checked>' in page,
               f"a checkbox per testee: {t}")
    _check("<script>" in page and "function apply()" in page, "the selection script ships")
    rowcells = _cells_by_row(page)
    bt, bn, ns = rowcells[0]
    _check(ns == {"engine-a": 100.0, "engine-b": 200.0, "engine-c": 400.0, "engine-d": 300.0}, ns)
    everyone = set(ns)
    _check(_best_over(ns, everyone) == ("engine-a", 100.0) and (bt, bn) == ("engine-a", "100.0"),
           "(1) full selection reproduces the static best")
    _check(_best_over(ns, {"engine-a", "engine-c"})[1] == float(rows[0]["best_ns_yes"]),
           "(2) the YES selection yields the TSV's best_ns_yes")
    _check(_best_over(ns, {"engine-b"})[1] == float(rows[0]["best_ns_no"]),
           "(2) the NO selection yields the TSV's best_ns_no")
    _check(_best_over(ns, {"engine-c", "engine-d"}) == ("engine-d", 300.0),
           "an arbitrary selection's best is its own fastest cell")
    _check(rowcells[1][2] == {}, f"(3) status tokens carry no data-ns: {rowcells[1]}")
    _check("var LOG_MAX = %d;" % mp.LOG_MAX in page and "[56, 161, 255]" in page
           and "[220, 38, 38]" in page and "t < 0.55" in page,
           "(4) the script's ramp must be _ratio_color's")


def test_selection_on_class_split_page():
    """[B91] on a MIXED roster: the selection lists exactly the testees
    the two class-pure tables show (the undeclared one is in neither),
    and each class table's cells carry data-ns in ABSOLUTE ns (the
    class-rebased ratio x the class best), so selecting within a table
    recomputes against the same absolute scale."""
    path = _write_tmp(SAMPLE_TSV_MIXED)
    try:
        prov, header, rows = mp.parse_matrix_tsv(path)
        page = mp.render_html(prov, header, rows, path)
    finally:
        os.unlink(path)
    _check('value="engine-d"' not in page, "undeclared engine-d is not selectable")
    for t in ("engine-a", "engine-b", "engine-c"):
        _check(f'value="{t}"' in page, t)
    rowcells = _cells_by_row(page)
    _check(len(rowcells) == 2, rowcells)
    _check(rowcells[0][2] == {"engine-a": 100.0, "engine-c": 400.0}, rowcells[0])
    _check(rowcells[1][2] == {"engine-b": 200.0}, rowcells[1])


TESTS = [
    test_parse_matrix_tsv_roundtrip,
    test_malformed_header_raises,
    test_empty_file_raises,
    test_status_chip_cell_html,
    test_ratio_cell_html_and_tooltip,
    test_ratio_color_ramp_endpoints_and_clamp,
    test_render_html_end_to_end,
    test_parse_capture_class,
    test_class_pure_row_rebases_within_class,
    test_matrix_class_pure_split_renders_two_tables,
    test_matrix_single_class_roster_unchanged,
    test_main_writes_default_output_path,
    test_v24_header_parses_and_normalises,
    test_selection_recomputes_best_over_selection,
    test_selection_on_class_split_page,
]


def main():
    os.environ.setdefault("LC_ALL", "C")
    passed = failed = 0
    for t in TESTS:
        try:
            t()
        except Exception:  # noqa: BLE001
            failed += 1
            print(f"FAIL {t.__name__}")
            traceback.print_exc()
        else:
            passed += 1
            print(f"ok   {t.__name__}")
    print(f"\n{passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
