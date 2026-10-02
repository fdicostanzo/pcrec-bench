"""docs/dev/measurements/probe_b120b121read_resecompat_bucket.py -- lane
b120b121read, step 1 ([B120] item 3's own reading): buckets every
pattern of a pcrec DEFAULT/`-fno-hyb-reseed` pair by its OWN per-pattern
`vm_reseed` x `vm_frameless` compile stamps (read DIRECTLY from the
record JSONL -- the report's `compile_stamp` TSV section prints only ONE
SAMPLE per testee, which is misleading for a config like `pcrec-auto`
that routes per pattern, the exact trap b117read's own lesson names),
then joins each bucket against a report TSV's `rank` section median_ns
for both testees, printing the ratio and flagging anything >5% slower
under default than denied.

Usage:
    python3 docs/dev/measurements/probe_b120b121read_resecompat_bucket.py \
        --default-record PATH --denied-record PATH \
        --report-tsv PATH --default-testee ID --denied-testee ID \
        [--regime large-subject-throughput] [--form plain]

Read-only: no compile, no run, no timing. Imports `pcrecbench.report`'s
own `load_record` (the shared validator) for the record side; the report
TSV is parsed directly (stdlib csv, tab-delimited) since `interpret.py`'s
own `ReportTsv` is grain-aware in ways this cross-join does not need.
"""
import argparse
import csv
import sys
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from pcrecbench import report as report_mod  # noqa: E402


def compile_stamps_by_pattern(record_path):
    """-> {(pattern_id, form): {vm_reseed, vm_frameless, engine, engine_sel}}"""
    rv = report_mod._get_record_validator()
    rec = report_mod.load_record(record_path, rv, check_filename=False)
    out = {}
    for row in rec.rows:
        if row.get("kind") != "compile":
            continue
        meta = row.get("engine_metadata") or {}
        key = (row.get("pattern_id"), row.get("form") or "plain")
        if key in out:
            continue  # first sample is representative; compile is trial-uniform
        out[key] = {
            "vm_reseed": meta.get("vm_reseed"),
            "vm_frameless": meta.get("vm_frameless"),
            "engine": meta.get("engine"),
            "engine_sel": meta.get("engine_sel"),
            "outcome": row.get("compile_outcome"),
        }
    return out


def rank_medians(tsv_path, testee_id):
    """-> {(pattern_id, regime, form): median_ns} for `rank` section rows,
    metric median_ns, this testee -- one row per the TSV's own key tuple
    (pattern/regime_or_na/form/testee)."""
    out = {}
    with open(tsv_path, newline="", encoding="utf-8") as fh:
        rdr = csv.reader(fh, delimiter="\t")
        header = None
        for row in rdr:
            if not row or row[0].startswith("#"):
                continue
            if header is None:
                header = row
                continue
            d = dict(zip(header, row))
            if d.get("section") not in ("rank", "rank_yes", "rank_no"):
                continue
            if d.get("metric") != "median_ns":
                continue
            if d.get("testee") != testee_id:
                continue
            key = (d.get("pattern"), d.get("regime_or_na"), d.get("form") or "plain")
            try:
                out[key] = float(d.get("value"))
            except (TypeError, ValueError):
                continue
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--default-record", required=True)
    ap.add_argument("--denied-record", required=True)
    ap.add_argument("--report-tsv", required=True)
    ap.add_argument("--default-testee", required=True)
    ap.add_argument("--denied-testee", required=True)
    args = ap.parse_args()

    print("=== source: docs/dev/measurements/probe_b120b121read_resecompat_bucket.py ===")
    print("=== default record: %s ===" % args.default_record)
    print("=== denied record: %s ===" % args.denied_record)
    print("=== report tsv: %s ===" % args.report_tsv)

    dflt = compile_stamps_by_pattern(args.default_record)
    den = compile_stamps_by_pattern(args.denied_record)
    dflt_rank = rank_medians(args.report_tsv, args.default_testee)
    den_rank = rank_medians(args.report_tsv, args.denied_testee)

    all_keys = sorted(set(dflt) | set(den))
    print("=== PER-PATTERN COMPILE STAMPS (default vs denied) ===")
    print("pattern\tform\tdflt_reseed\tdflt_frameless\tden_reseed\tden_frameless\tagree")
    for key in all_keys:
        a = dflt.get(key, {})
        b = den.get(key, {})
        agree = "yes" if (a.get("engine") == b.get("engine")
                          and a.get("vm_frameless") == b.get("vm_frameless")) else "DIFFERS"
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (
            key[0], key[1], a.get("vm_reseed"), a.get("vm_frameless"),
            b.get("vm_reseed"), b.get("vm_frameless"), agree))

    print()
    print("=== ADAPTIVE* CELLS, TIMING RATIO (default/denied), BUCKETED by (vm_reseed, vm_frameless) ===")
    print("pattern\tregime\tform\tvm_reseed\tvm_frameless\tdflt_median_ns\tden_median_ns\tratio\tflag")
    adaptive_rows = []
    for key in all_keys:
        pat, form = key
        a = dflt.get(key, {})
        reseed = a.get("vm_reseed")
        if not reseed or not reseed.startswith("adaptive"):
            continue
        frameless = a.get("vm_frameless")
        for (p2, regime, f2), dm in sorted(dflt_rank.items()):
            if p2 != pat or f2 != form:
                continue
            nm = den_rank.get((p2, regime, f2))
            if nm is None or nm == 0:
                continue
            ratio = dm / nm
            flag = "SLOWER>5%" if ratio > 1.05 else ("faster" if ratio < 0.95 else "flat")
            print("%s\t%s\t%s\t%s\t%s\t%.3f\t%.3f\t%.4f\t%s" % (
                pat, regime, form, reseed, frameless, dm, nm, ratio, flag))
            adaptive_rows.append((pat, regime, form, reseed, frameless, ratio, flag))

    print()
    print("=== CLAMPED CELLS: does the timing move at all? (1c prediction) ===")
    print("pattern\tregime\tform\tvm_reseed\tratio\tflag")
    for key in all_keys:
        pat, form = key
        a = dflt.get(key, {})
        reseed = a.get("vm_reseed")
        if reseed != "clamped":
            continue
        for (p2, regime, f2), dm in sorted(dflt_rank.items()):
            if p2 != pat or f2 != form:
                continue
            nm = den_rank.get((p2, regime, f2))
            if nm is None or nm == 0:
                continue
            ratio = dm / nm
            flag = "MOVED>5%" if (ratio > 1.05 or ratio < 0.95) else "unmoved"
            print("%s\t%s\t%s\t%s\t%.4f\t%s" % (pat, regime, form, reseed, ratio, flag))

    print()
    print("=== SUMMARY ===")
    slower = [r for r in adaptive_rows if r[-1] == "SLOWER>5%"]
    print("adaptive* cells total: %d" % len(adaptive_rows))
    print(">5%% slower under default: %d" % len(slower))
    for r in slower:
        print("  ", r)


if __name__ == "__main__":
    main()
