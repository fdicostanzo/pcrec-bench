#!/usr/bin/env python3
"""Regenerate `catalogue/golden/*.facts.tsv` — interpreter_v1.md §8(2).

Run this ONLY as part of a commit that is entitled to move a golden
fact: a `catalogue_version` bump, a `REPORTER_VERSION` bump (which
regenerates the reports the goldens are derived from), or a refresh of
the frozen index snapshot. A commit that only adds records must never
need it -- that is what the frozen snapshot is for.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from catalogue.check_interpret import ACCEPTANCE, GOLDEN, INDEX_SNAPSHOT, \
    ROOT, golden_name, run_interpret  # noqa: E402

for report_rel, pred_rel in ACCEPTANCE:
    report = os.path.join(ROOT, report_rel)
    pred = os.path.join(ROOT, pred_rel) if pred_rel else None
    text = run_interpret(report, INDEX_SNAPSHOT, pred, "tsv")
    out = os.path.join(GOLDEN, golden_name(report_rel, pred_rel))
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {os.path.relpath(out, ROOT)} "
          f"({len(text.splitlines()) - 1} row(s))")
