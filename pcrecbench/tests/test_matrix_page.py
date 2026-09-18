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
    """Each of the five closed status tokens (`report.py`'s own set)
    renders its own fixed CSS class and a title attribute naming what
    the token means -- never the log-scale ramp's `style="background:
    rgb(...)"`, which is reserved for a genuine ratio."""
    row = {"unsup": "unsup", "refused": "refused", "wrong": "wrong",
           "gave-up": "gave-up", "excluded": "excluded"}
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


TESTS = [
    test_parse_matrix_tsv_roundtrip,
    test_malformed_header_raises,
    test_empty_file_raises,
    test_status_chip_cell_html,
    test_ratio_cell_html_and_tooltip,
    test_ratio_color_ramp_endpoints_and_clamp,
    test_render_html_end_to_end,
    test_main_writes_default_output_path,
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
