#!/usr/bin/env python3
"""Generate the interpreter's rule fixtures — interpreter_v1.md §8(4).

    python3 catalogue/fixtures/gen.py            # (re)generate
    python3 catalogue/fixtures/gen.py --check    # re-derive and diff

The pattern is `schema/examples/bad/`'s, which `gen_example_14.py
--check` already pins: a GENERATED BASE plus ONE DECLARED MUTATION. The
base of every fixture here is a REAL reporter-produced slice, projected
out of a committed report by the selector in `fixtures.toml`; a control
is the same slice with exactly one declared field changed. The generator
therefore shares source with `report.py`'s OUTPUT and with nothing in
`interpret.py`'s rule functions -- pcrec D35's controls-share-no-source
discipline where it matters.

The one exception is `CLEAN__all-measured`, the §10 Report D null
control, which is SYNTHETIC by construction: a report on which the tool
must stay quiet cannot be projected out of a real one, because
R-STATUS-5 and R-FLOOR-1 fire on essentially every committed report.
"""

import argparse
import os
import sys
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)

from pcrecbench.interpret import (REPORT_COLUMNS, INDEX_COLUMNS,  # noqa: E402
                                  PRED_COLUMNS, record_id_of)


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _matches(row, select):
    # A `record` row is ALWAYS kept unless the selector names `section`
    # itself: it carries the population (every R-STATUS rule reads it and
    # R-BUCKET-SPAN joins it to the index), and its key columns are empty,
    # so a testee-scoped selector would otherwise drop it.
    if row["section"] == "record" and "section" not in select:
        return True
    for col, want in select.items():
        got = row[col]
        if got == "":
            continue                    # the column does not apply here
        if isinstance(want, list):
            if got not in want:
                return False
        elif got != want:
            return False
    return True


def _where_hit(row, where):
    return all(row.get(k) == v for k, v in where.items())


def project_report(path, select, mutate=None, mutate_header=None):
    text = read(path)
    lines = text.split("\n")
    header, columns = lines[0], lines[1]
    if mutate_header:
        key, value = mutate_header["key"], mutate_header["value"]
        parts = []
        for clause in header.lstrip("# ").split("; "):
            if clause.startswith(key + ": "):
                clause = f"{key}: {value}"
            parts.append(clause)
        header = "# " + "; ".join(parts)
    out = [header, columns]
    done = False
    for ln in lines[2:]:
        if not ln:
            continue
        row = dict(zip(REPORT_COLUMNS, ln.split("\t")))
        if select and not _matches(row, select):
            continue
        if mutate and (mutate.get("all") or not done):
            if _where_hit(row, mutate.get("where", {})):
                row[mutate["column"]] = mutate["value"]
                done = True
        out.append("\t".join(row[c] for c in REPORT_COLUMNS))
    return "\n".join(out) + "\n"


def project_index(path, report_text, mutate_index=None):
    lines = read(path).split("\n")
    rows = [dict(zip(INDEX_COLUMNS, ln.split("\t")))
            for ln in lines[1:] if ln]
    header = {}
    for clause in report_text.split("\n")[0].lstrip("# ").split("; "):
        k, _s, v = clause.partition(": ")
        header[k] = v
    pairs = set()
    for sv in header.get("subbench_versions", "").split(","):
        if "@" in sv:
            pairs.add(tuple(sv.strip().rsplit("@", 1)))
    machines = {m.strip() for m in header.get("machines", "").split(",")}
    out = [lines[0]]
    done = False
    for r in rows:
        if (r["subbench"], r["version"]) not in pairs:
            continue
        if r["machine_id"] not in machines:
            continue
        if mutate_index and (mutate_index.get("all") or not done):
            if _where_hit(r, mutate_index.get("where", {})):
                r[mutate_index["column"]] = mutate_index["value"]
                done = True
        out.append("\t".join(r[c] for c in INDEX_COLUMNS))
    return "\n".join(out) + "\n"


def project_predictions(path, ids, mutate=None):
    lines = read(path).split("\n")
    out = [lines[0]]
    done = False
    for ln in lines[1:]:
        if not ln.strip():
            continue
        row = dict(zip(PRED_COLUMNS, ln.split("\t")))
        if row["prediction_id"] not in ids:
            continue
        if mutate and (mutate.get("all") or not done):
            if _where_hit(row, mutate.get("where", {})):
                row[mutate["column"]] = mutate["value"]
                done = True
        out.append("\t".join(row[c] for c in PRED_COLUMNS))
    return "\n".join(out) + "\n"


# --------------------------------------------- the synthetic null control

CLEAN_HEADER = (
    "# reporter: v16 (2026-09-08); filters: subbench=clean-null, version=1.0; "
    "source: catalogue/fixtures/CLEAN__all-measured/index.tsv "
    "(1 record(s) matching this query); records: 1; excluded_invalid: 0; "
    "superseded: 0; newer_not_measured: 0; subbench_versions: clean-null@1.0; "
    "machines: budu-ryzen1600; schema_versions: 1.5; grain: set; "
    "single_subject_regimes: ; include_unmeasured: False; "
    "include_scratch: False; all_records: False; "
    "x13_rules: v1.4 X13 (pre-flight + trial agreement) on 1; "
    "mixed_x13: False; include_provenance: False; "
    "worst_other_core_busy: n/a; floor_pattern: none")

CLEAN_RECORD = "clean-null@1.0__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260909T000000Z"


def clean_report():
    """§10 Report D: every record `measured`, no excluded cell, no
    did-not-compile row, no Δ outside spread, no arm pair outside
    spread, one pin, one schema version, `mixed_x13: False`,
    `worst_other_core_busy: n/a`, `floor_pattern: none`. All 31 rules
    must report `fired=0`."""
    rows = [CLEAN_HEADER, "\t".join(REPORT_COLUMNS)]

    def row(**kw):
        r = {c: "" for c in REPORT_COLUMNS}
        r.update(kw)
        rows.append("\t".join(r[c] for c in REPORT_COLUMNS))

    row(section="record", testee=CLEAN_RECORD, metric="agreement",
        value="agree (0 of 2 groups; 0 of 10 rows; 0 unjudged; k=1.5, 2/3; "
              "5 trials)")
    # One ranking group, one rankable arm -- the reference arm itself, so
    # R-BUCKET-FORM (one fact), R-ARM-1 (no second arm), R-RANK-1 and
    # R-STATUS-13 (the reference IS present) all stay quiet.
    for metric, value in (("median_ns", "1000.000000"),
                          ("min_ns", "990.000000"),
                          ("max_ns", "1010.000000"),
                          ("stddev_ns", "5.000000"),
                          ("ratio_vs_baseline", "1.000000"),
                          ("ratio_vs_best", "1.000000")):
        row(section="rank", pattern="lit", subject_or_na="(set)",
            regime_or_na="short-subject-search", form="plain",
            fact="same program", testee="libpcre2_10.46_interp-caps-simdna",
            status="measured", tier="pinned", rank_or_na="1", metric=metric,
            value=value, n="4", pass_rate="1.0000", n_gave_up="0", n_wrong="0")
    # One compile cell whose jitter is a real ratio well under 1.0.
    row(section="compile", pattern="lit", form="plain",
        fact="same program", testee="libpcre2_10.46_interp-caps-simdna",
        metric="median_total_ns", value="4000000.000000", n="5")
    row(section="compile", pattern="lit", form="plain",
        fact="same program", testee="libpcre2_10.46_interp-caps-simdna",
        metric="jitter", value="0.020")
    return "\n".join(rows) + "\n"


def clean_index():
    return ("\t".join(INDEX_COLUMNS) + "\n"
            + "\t".join([f"records/clean-null@1.0/"
                         f"libpcre2_10.46_interp-caps-simdna/"
                         f"{CLEAN_RECORD}.jsonl",
                         "clean-null", "1.0",
                         "libpcre2_10.46_interp-caps-simdna",
                         "budu-ryzen1600", "2026-09-09T00:00:00Z",
                         "measured", "12"]) + "\n")


# ------------------------------------------------------------------ main

def build(spec, decl):
    """Return {filename: text} for one fixture."""
    if spec.get("synthetic"):
        return {"report.tsv": clean_report(), "index.tsv": clean_index()}
    report_path = os.path.join(ROOT, decl["report_" + spec["report"]])
    text = project_report(report_path, spec.get("select"),
                          spec.get("mutate"), spec.get("mutate_header"))
    files = {"report.tsv": text,
             "index.tsv": project_index(os.path.join(ROOT, decl["index"]),
                                        text, spec.get("mutate_index"))}
    if spec.get("predictions_select"):
        files["predictions.tsv"] = project_predictions(
            os.path.join(ROOT, decl["predictions"]),
            set(spec["predictions_select"]), spec.get("mutate_predictions"))
    return files


def source_toml(spec):
    """The fixture's own `source.toml`, materialised from the one
    authored declaration in `fixtures.toml` so each directory carries
    its own record of what it is."""
    out = ["# GENERATED by catalogue/fixtures/gen.py from "
           "catalogue/fixtures/fixtures.toml -- do not edit.",
           "# interpreter_v1.md §8(4): a generated base plus at most one "
           "declared mutation."]
    for key in ("name", "base", "report", "synthetic", "select", "mutate",
                "mutate_header", "mutate_index", "predictions_select",
                "mutate_predictions", "expect", "expect_not", "expect_token"):
        if key in spec:
            out.append(f"{key} = {_toml(spec[key])}")
    return "\n".join(out) + "\n"


def _toml(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'
    if isinstance(value, list):
        return "[" + ", ".join(_toml(v) for v in value) + "]"
    if isinstance(value, dict):
        return "{ " + ", ".join(f"{k} = {_toml(v)}"
                                for k, v in value.items()) + " }"
    raise TypeError(value)


def load_declaration():
    with open(os.path.join(HERE, "fixtures.toml"), "rb") as fh:
        return tomllib.load(fh)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="re-derive and diff instead of writing")
    args = ap.parse_args(argv)
    decl = load_declaration()
    bad = 0
    n_files = 0
    names = set()
    for spec in decl["fixture"]:
        name = spec["name"]
        if name in names:
            print(f"FAIL duplicate fixture name {name}")
            bad += 1
        names.add(name)
        directory = os.path.join(HERE, name)
        files = dict(build(spec, decl))
        files["source.toml"] = source_toml(spec)
        for fname, text in sorted(files.items()):
            n_files += 1
            path = os.path.join(directory, fname)
            if args.check:
                if not os.path.exists(path):
                    print(f"FAIL {name}/{fname}: missing")
                    bad += 1
                elif read(path) != text:
                    print(f"FAIL {name}/{fname}: does not re-derive")
                    bad += 1
            else:
                os.makedirs(directory, exist_ok=True)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(text)
        # a directory holding files the declaration does not name is stale
        if os.path.isdir(directory):
            for fname in sorted(os.listdir(directory)):
                if fname not in files:
                    print(f"FAIL {name}/{fname}: not declared")
                    bad += 1
    verb = "checked" if args.check else "wrote"
    print(f"gen.py: {verb} {n_files} file(s) in {len(names)} fixture(s)"
          + (f" -- {bad} FAILURE(S)" if bad else " -- ok"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
