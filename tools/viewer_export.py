#!/usr/bin/env python3
"""tools/viewer_export.py -- [B66] the results viewer's data exporter.

`docs/design/results_viewer_v1.md` 2: walks `store/index.tsv`, loads each
set's newest record per (testee_id, machine) -- plus every older PIN's own
newest record too under `--all-pins` -- and reduces to SET GRAIN by calling
the SAME `pcrecbench.reduce` functions the reporter calls
(`reduce_set_cell`, `cells_from_record`), so a viewer cell equals the
committed report cell byte-for-value. It never reimplements a median.

MEMORY (docs/dev/lanes/BOILERPLATE.md, this lane's brief): one record is
loaded, reduced and discarded before the next is opened -- never the whole
store at once (the reporter's own whole-store load is ~3.6 GB at 160
records, KB-16). This module never calls `pcrecbench.report.build_report`
for exactly that reason: `build_report` accumulates every selected record's
RAW rows across the whole query before reducing anything (see its own
`match_rows_by_key`/`set_rows_by_key` accumulators), which is the right
shape for a query that must compare many records against each other at
once but the wrong one for an exporter that can reduce one record at a
time and keep only the numbers. The record-DEDUP step below (which testee
identity's newest record to open at all) is answered from `index.tsv`
alone -- no record file is opened to make that decision.

WHICH RECORDS ARE INCLUDED (mirrors `report.py`'s R2/OD-B15 dedup, and
`reports/CLAUDE.md`'s [B61] canonical-identity convention):

  1. Per (subbench@version, testee_id, machine_id): the newest record with
     `status == measured`, or (if none is measured) the newest record
     overall. Exactly `build_report`'s own rule, computed here from
     `index.tsv`'s own `timestamp`/`status` columns without opening a file.
  2. Default (no `--all-pins`): a further collapse across PINS of the same
     CANONICAL identity -- `(engine_name, config_slug)` parsed from
     `testee_id` (`<engine>_<version>_<config>`, the same split
     `report.py`'s `_parse_testee_config` uses) -- keeping only the
     newest-timestamped pin. `--all-pins` skips this collapse: every
     distinct testee_id (and therefore every pin) that survives step 1
     becomes its own column.

STATUS PER ROW, in priority order (design note 2's vocabulary: measured |
refused | unsup | wrong | gave-up | timed-out | inconclusive-*):

  1. the RECORD's own status, when not `measured` (inconclusive-load,
     inconclusive-spread, harness-failure) -- no numbers on such a row,
     the standing "statuses other than measured are never ranked" rule.
  2. a compile-row outcome `did-not-compile` -> `refused`,
     `unsupported-by-declaration` -> `unsup` (report.py's own
     `did_not_compile_by_pattern`/`unsupported_by_pattern` logic, applied
     per record); `crashed`/`timed-out` at compile time pass through by
     name. One row per (pattern, form), regime empty (mirrors [B52]'s F26
     shape for a pattern that never reached a regime).
  3. a match SetCell that fails its own expectation
     (`SetCellReduction.expectation_failing`): `wrong` if any subject's
     answer disagreed, else `gave-up` if any subject gave up, else the
     dominant hazard outcome found in the failing subjects' own
     `MatchCellReduction.outcome_counts` (`timed-out` / `crashed`), else
     `excluded` (no timed trials at all).
  4. otherwise `measured`, carrying `median_ns`/`spread_lo_ns`/
     `spread_hi_ns`/`n_subjects`/`subject_bytes_total`.

Run: `python3 tools/viewer_export.py` (== `make viewer-data`); `--sets
loglines,email-specimen` narrows to a slice for development (the design
note's data files are independent per set, so a partial export is a
partial `viewer/data/` -- never a corrupt one: files this run does not
touch are left as they are, and `manifest.js` lists only the sets it
actually wrote this run plus whatever the CALLER says to keep, via
`--keep-existing-manifest`, for a slice run that must not blank out the
other sets' manifest entries).
"""

import argparse
import csv
import json
import os
import sys
import tempfile
from collections import defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from pcrecbench.report import _get_record_validator, load_record  # noqa: E402
from pcrecbench.reduce import (  # noqa: E402
    cells_from_record,
    reduce_set_cell,
)

DEFAULT_STORE = os.path.join(ROOT, "store")
DEFAULT_OUT = os.path.join(ROOT, "viewer", "data")

# record.schema.json $defs/record_status: the non-"measured" tokens a
# whole RECORD can carry (never a per-cell number).
_NON_MEASURED_RECORD_STATUS = {"harness-failure", "inconclusive-load", "inconclusive-spread"}

# record.schema.json $defs/compile_outcome, mapped to the viewer's own
# status vocabulary (design note 2): `did-not-compile` reads oddly as a
# per-cell status word, so it renders as `refused` (what a reader calls a
# testee that would not build this pattern at all); `unsupported-by-
# declaration` as `unsup` ([B42] L5's own advance-declaration fact, never
# an engine failure); `crashed`/`timed-out` pass through by name, same as
# a match-row hazard outcome.
_COMPILE_STATUS = {
    "did-not-compile": "refused",
    "unsupported-by-declaration": "unsup",
    "crashed": "crashed",
    "timed-out": "timed-out",
}

# The sink order a non-measured row falls to (design note 4's own list,
# and the viewer's sort rule): worse findings sink further. `viewer.html`
# reads this same order out of the exported meta so the two never drift.
STATUS_SINK_ORDER = ["measured", "wrong", "refused", "unsup", "gave-up",
                      "timed-out", "crashed", "inconclusive-load",
                      "inconclusive-spread", "harness-failure", "excluded"]


def utcnow_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------- index.tsv

def read_index(store_dir):
    path = os.path.join(store_dir, "index.tsv")
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t")), sum(1 for _ in open(path)) - 1


def parse_testee_id(testee_id):
    """(engine_name, version_slug, config_slug) -- the same three-way split
    `report.py`'s `_parse_testee_config` uses (record_schema.md 6.4), kept
    as a small local copy rather than importing a private, underscore-
    prefixed function from another module. `None` for a testee_id that
    does not split into exactly three `_`-separated segments."""
    base = testee_id.split("@", 1)[0]
    parts = base.split("_", 2)
    if len(parts) != 3:
        return None
    return tuple(parts)


def dedup_newest_per_testee(index_rows):
    """Step 1 of the module docstring's inclusion rule: per (subbench@
    version, testee_id, machine_id), the newest MEASURED index row, or (if
    none is measured) the newest row overall -- `report.py`'s own R2/
    OD-S15 rule, computed here purely from `index.tsv` columns."""
    groups = defaultdict(list)
    for row in index_rows:
        sb = f"{row['subbench']}@{row['version']}"
        key = (sb, row["testee_id"], row["machine_id"])
        groups[key].append(row)
    kept = []
    for _key, entries in groups.items():
        entries.sort(key=lambda r: r["timestamp"])
        measured = [r for r in entries if r["status"] == "measured"]
        kept.append(measured[-1] if measured else entries[-1])
    return kept


def collapse_to_newest_pin(rows):
    """Step 2 (default mode only): collapse across PINS of one canonical
    (engine_name, config_slug) identity, keeping the newest-timestamped
    row -- `reports/CLAUDE.md`'s [B61] rule, generalised past pcrec's own
    ablation testees to every engine (a rust/re2/libpcre2 re-run with a
    changed `engine_version` collapses the identical way)."""
    groups = defaultdict(list)
    for row in rows:
        sb = f"{row['subbench']}@{row['version']}"
        parsed = parse_testee_id(row["testee_id"])
        canon = (row["testee_id"] if parsed is None
                 else (parsed[0], parsed[2]))
        groups[(sb, canon, row["machine_id"])].append(row)
    kept = []
    for _key, entries in groups.items():
        entries.sort(key=lambda r: r["timestamp"])
        kept.append(entries[-1])
    return kept


# ---------------------------------------------------------- per-record cut

def _engine_variant(testee_block):
    mode = testee_block.get("engine_mode") or ""
    extra = testee_block.get("config_extra")
    return f"{mode}-{extra}" if extra else mode


def _failing_kind(red):
    """The dominant status word for one FAILING SetCellReduction (its own
    `expectation_failing` already True): `wrong` ahead of `gave-up` (a
    wrong answer is the stronger finding when a cell somehow carries
    both, same order `_matrix_cell` uses), else the dominant hazard
    outcome found among the failing subjects' own MatchCellReduction
    outcome_counts, else `excluded` (no timed trial at all -- `n_trials
    == 0` on every failing subject)."""
    if red.n_wrong:
        return "wrong"
    if red.n_gave_up:
        return "gave-up"
    hazard_counts = defaultdict(int)
    for sub_red in red.failing_detail.values():
        for outcome in ("timed-out", "crashed"):
            hazard_counts[outcome] += sub_red.outcome_counts.get(outcome, 0)
    if hazard_counts.get("timed-out"):
        return "timed-out"
    if hazard_counts.get("crashed"):
        return "crashed"
    return "excluded"


def export_rows_for_record(path, rv):
    """Load ONE record (`report.load_record`, the reporter's own loader:
    JSON parse + schema validation in one pass), reduce it, and return a
    list of viewer row dicts -- then the caller drops `loaded`/`rows`
    before opening the next file. Returns `[]` for an invalid/unreadable
    record (never raises: the same "excluded, not fatal" posture
    `build_report` takes for `excluded_invalid`)."""
    rec = load_record(path, rv, check_filename=True)
    if rec.setup is None or rec.problems:
        return []
    setup = rec.setup
    sb = f"{setup['subbench']['id']}@{setup['subbench']['version']}"
    testee = setup["testee"]
    testee_id = testee["testee_id"]
    engine_family = testee.get("engine_name") or (parse_testee_id(testee_id) or (None,))[0]
    engine_variant = _engine_variant(testee)
    pin = testee.get("engine_version")
    record_id = setup["record_id"]
    measured_utc = setup.get("run", {}).get("timestamp")
    record_status = setup.get("status", "measured")
    subject_bytes = {s["subject_id"]: s.get("bytes_offered")
                      for s in setup.get("subjects", []) or []}

    def base_row(pattern_id, regime, form):
        return {
            "pattern": pattern_id, "regime": regime, "form": form or "plain",
            "testee_id": testee_id, "engine_family": engine_family,
            "engine_variant": engine_variant, "pin": pin,
            "record_id": record_id, "measured_utc": measured_utc,
            "median_ns": None, "spread_lo_ns": None, "spread_hi_ns": None,
            "subject_bytes_total": None, "n_subjects": None,
        }

    out = []

    # Compile-row refusals/declines: one row per (pattern_id, form) that
    # never reached a match regime at all -- report.py's own
    # did_not_compile_by_pattern/unsupported_by_pattern logic, applied to
    # this one record's raw compile rows.
    compile_diag = {}  # (pattern_id, form) -> (status, diagnostic)
    for row in rec.rows:
        if row.get("kind") != "compile":
            continue
        outcome = row.get("compile_outcome")
        status = _COMPILE_STATUS.get(outcome)
        if status is None:
            continue
        form = row.get("form") or "plain"
        key = (row["pattern_id"], form)
        if key not in compile_diag:
            compile_diag[key] = (status, row.get("diagnostic"))

    matched_pattern_forms = set()
    for (pattern_id, regime, form), by_subject in cells_from_record(rec.rows).items():
        matched_pattern_forms.add((pattern_id, form or "plain"))
        row = base_row(pattern_id, regime, form)
        if record_status != "measured":
            row["status"] = (record_status if record_status in _NON_MEASURED_RECORD_STATUS
                              else "excluded")
            out.append(row)
            continue
        red = reduce_set_cell(by_subject)
        if red.expectation_failing:
            row["status"] = _failing_kind(red)
            row["n_subjects"] = red.n_subjects
            out.append(row)
            continue
        byte_vals = [subject_bytes.get(sid) for sid in by_subject]
        row["status"] = "measured"
        row["median_ns"] = red.median_ns
        row["spread_lo_ns"] = red.min_ns
        row["spread_hi_ns"] = red.max_ns
        row["n_subjects"] = red.n_subjects
        row["subject_bytes_total"] = (sum(byte_vals) if byte_vals and
                                        all(v is not None for v in byte_vals) else None)
        out.append(row)

    for (pattern_id, form), (status, diagnostic) in compile_diag.items():
        if (pattern_id, form) in matched_pattern_forms:
            continue  # this testee DID reach a regime on this pattern/form
        row = base_row(pattern_id, "", form)
        row["status"] = status
        row["diagnostic"] = diagnostic
        out.append(row)

    return out


# -------------------------------------------------------------- rendering

def _json_for_js(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def atomic_write(path, text):
    d = os.path.dirname(path)
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".tmp-", suffix=".js")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        # mkstemp opens 0600; every other generated file in this repo (the
        # reporter's own reports/*.tsv included) is 0644 -- match that
        # rather than leaving a committed file owner-only-readable.
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def render_set_file(sb, subbench, version, rows, generated_utc, index_rows_n):
    rows_sorted = sorted(rows, key=lambda r: (
        r["pattern"], r["regime"], r["form"], r["testee_id"]))
    payload = {
        "meta": {
            "generated_by": "tools/viewer_export.py",
            "generated_utc": generated_utc,
            "index_rows": index_rows_n,
            "set": sb,
        },
        "set": sb, "subbench": subbench, "version": version,
        "rows": rows_sorted,
    }
    return "BENCH.load(" + _json_for_js(payload) + ");\n"


def render_manifest(generated_utc, index_rows_n, set_entries, all_pins):
    payload = {
        "generated_utc": generated_utc,
        "store_rows": index_rows_n,
        "all_pins": all_pins,
        "status_sink_order": STATUS_SINK_ORDER,
        "files": [e["file"] for e in set_entries],
        "sets": set_entries,
    }
    return "BENCH.manifest(" + _json_for_js(payload) + ");\n"


# ------------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--store", default=DEFAULT_STORE)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--all-pins", action="store_true",
                     help="keep every pin's own newest record as its own "
                          "column, instead of collapsing to the newest pin "
                          "per canonical (engine, config) identity")
    ap.add_argument("--sets", default=None,
                     help="comma-separated subbench@version (or bare "
                          "subbench, matching every version) to export -- "
                          "a development slice; omitted = every set")
    ap.add_argument("--keep-existing-manifest", action="store_true",
                     help="merge this run's set list into the manifest "
                          "ALREADY on disk (for a --sets slice run that "
                          "must not blank out the other sets' entries)")
    args = ap.parse_args(argv)

    index_rows, index_rows_n = read_index(args.store)
    kept = dedup_newest_per_testee(index_rows)
    if not args.all_pins:
        kept = collapse_to_newest_pin(kept)

    sets_filter = None
    if args.sets:
        sets_filter = set()
        for tok in args.sets.split(","):
            tok = tok.strip()
            if tok:
                sets_filter.add(tok)

    by_set = defaultdict(list)
    for row in kept:
        sb = f"{row['subbench']}@{row['version']}"
        if sets_filter and sb not in sets_filter and row["subbench"] not in sets_filter:
            continue
        by_set[sb].append(row)

    rv = _get_record_validator()
    generated_utc = utcnow_iso()
    set_entries = []
    for sb in sorted(by_set):
        rows = []
        for idx_row in sorted(by_set[sb], key=lambda r: r["testee_id"]):
            path = os.path.join(args.store, idx_row["path"])
            rows.extend(export_rows_for_record(path, rv))
            # MEMORY: nothing from this record's raw rows/setup survives
            # past export_rows_for_record's return -- `rec`/`rec.rows`
            # went out of scope with that call.
        subbench, version = sb.split("@", 1)
        text = render_set_file(sb, subbench, version, rows, generated_utc, index_rows_n)
        out_path = os.path.join(args.out, f"{sb}.js")
        atomic_write(out_path, text)
        set_entries.append({"set": sb, "subbench": subbench, "version": version,
                             "file": os.path.basename(out_path), "n_rows": len(rows)})
        print(f"wrote {out_path}: {len(rows)} row(s) from {len(by_set[sb])} record(s)")

    manifest_path = os.path.join(args.out, "manifest.js")
    if args.keep_existing_manifest and os.path.exists(manifest_path):
        prev = _read_prev_manifest_sets(manifest_path)
        written = {e["set"] for e in set_entries}
        for s, entry in prev.items():
            if s not in written:
                set_entries.append(entry)
        set_entries.sort(key=lambda e: e["set"])

    manifest_text = render_manifest(generated_utc, index_rows_n, set_entries, args.all_pins)
    atomic_write(manifest_path, manifest_text)
    print(f"wrote {manifest_path}: {len(set_entries)} set(s)")
    return 0


def _read_prev_manifest_sets(manifest_path):
    """Parse the previous run's `BENCH.manifest({...});` call back into
    {set: entry} -- used only by `--keep-existing-manifest` (a `--sets`
    slice run) so it can carry forward the OTHER sets' entries rather
    than dropping them from the manifest it writes."""
    with open(manifest_path, encoding="utf-8") as f:
        text = f.read()
    start = text.index("(")
    end = text.rindex(")")
    obj = json.loads(text[start + 1:end])
    return {e["set"]: e for e in obj.get("sets", [])}


if __name__ == "__main__":
    sys.exit(main())
