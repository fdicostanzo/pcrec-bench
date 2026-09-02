#!/usr/bin/env python3
"""probe_bounded_cross_version.py -- the CELL-AGAINST-CELL read of one
bench/bounded pattern set against the next, across a pcrec pin.

THIS IS A READ OF PINNED RECORDS, NOT A MEASUREMENT. Nothing here compiles,
runs or times anything: every number is arithmetic over records a window
already measured (`store/records/<set>/<testee>/*.jsonl`). The directory's
D35 rules 1-4 apply to the ARCHIVE this writes (stable name, source header,
committed script beside it); rule 5 applies as always -- no ranking input,
no schema, no reporter.

WHY IT EXISTS. `bench/bounded@0.2` and `@0.3` NEVER POOL (bench/bounded/
NOTES.md, "What 0.3 added"): 0.3 adds thirteen patterns and nineteen
subjects, so a set-grain sum over one is a sum over different work from a
sum over the other, and the reporter's `--version` filter keeps them apart
by construction. That leaves the [OPT-4.2]/abi-15 continuity question --
did anything move between pcrec a7e0bdf (abi 13) and 1989c62 (abi 15) on
the surface both sets share? -- with no reporter query that can answer it.
What IS comparable across the bump is stated by 0.3's own rule: "any
(pattern, subject, regime) cell whose pattern id and subject appear in
both, read cell against cell, never sum against sum." This script is that
reading, and it is also the STEP 2 BEFORE's anchor: the 1989c62 column is
the number STEP 2 will be measured against, and the ratio column is the
evidence that the two pins' numbers may be compared at all.

THE SELECTOR, stated so it can be argued with. A cell is emitted iff ALL
of the following hold, and every one is checked from the records
themselves rather than assumed:

  1. its `pattern_id` appears in BOTH sets' `setup.patterns[]`, and the
     two entries' `canonical_sha256` are EQUAL (0.3 promises every 0.2
     pattern keeps its id and its exact bytes; this checks the promise
     rather than trusting it);
  2. its `subject_id` appears in BOTH sets' `setup.subjects[]`, and the
     two entries' `sha256` and `bytes_offered` are EQUAL (0.3 draws its
     new subjects LAST so the old draws are the same stream prefix --
     again checked, not trusted);
  3. the (regime, form) pair exists on both sides for that (pattern,
     subject) -- `form` is part of the key because a `whole-subject`
     artifact is a DIFFERENT MACHINE from the `plain` one (record_schema
     5 ADDITIONS 3, pcrec [OS-4]), and the two must never share a row;
  4. both sides' records are `measured` and carry the same testee CONFIG
     (`auto-caps-simdna`, `auto-nocaps-simdna`, `vm-caps-simdna`,
     `vm-in-caps-simdna` -- the pin is stripped, everything else must
     match exactly, so a gcc arm is never paired with a clang one).

Every id-matched pair REJECTED by (1) or (2) is named in the header. A
cell whose either side has a failing or gave-up trial is emitted with its
outcome spelled in the `note` column and its ratio blank -- never folded
into a number.

THE COMPARABLE is `pcrecbench.reduce`'s own, imported rather than
re-derived: `reduce_match_cell` over the cell's trials, i.e. the median of
per-trial `elapsed_ns / iterations`. This is the arithmetic the reporter
ranks by and `pcrecbench quick` prints, so a number here and a number in a
report mean the same thing. `ratio` is AFTER / BEFORE (1989c62 / a7e0bdf),
so > 1 is SLOWER at the newer pin.

    python3 docs/dev/measurements/probe_bounded_cross_version.py \
        --before bounded@0.2:a7e0bdf --after bounded@0.3:1989c62 \
        --tsv docs/dev/measurements/2026-09-02-bounded-cls-rungs-0.2-a7e0bdf-vs-0.3-1989c62.tsv

Run from the repo root. With no `--tsv` it prints the table to stdout.
"""
import argparse
import glob
import json
import os
import subprocess
import sys

sys.path.insert(0, os.getcwd())

from pcrecbench.reduce import cells_from_record, read_record, reduce_match_cell  # noqa: E402

CONFIG_KEYS = ("auto-caps-simdna", "auto-nocaps-simdna",
               "vm-caps-simdna", "vm-in-caps-simdna")


def git_commit():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return "(not a git checkout)"


def config_of(testee_id, pin):
    """`pcrec_<pin>_<config>` -> `<config>`; None for anything else."""
    prefix = f"pcrec_{pin}_"
    if not testee_id.startswith(prefix):
        return None
    return testee_id[len(prefix):]


def load_side(store, spec):
    """spec is `<subbench>@<version>:<pin>`. Returns
    (records_by_config, discarded, label)."""
    setver, pin = spec.split(":", 1)
    pattern = os.path.join(store, "records", setver, f"pcrec_{pin}_*", "*.jsonl")
    by_config, discarded = {}, []
    for path in sorted(glob.glob(pattern)):
        setup, rows = read_record(path)
        tid = setup["testee"]["testee_id"]
        cfg = config_of(tid, pin)
        if cfg is None:
            continue
        if setup.get("status") != "measured":
            discarded.append(f"{os.path.basename(path)} (status "
                             f"{setup.get('status')}) -- not `measured`")
            continue
        prev = by_config.get(cfg)
        if prev is not None:
            older, newer = sorted([prev, (setup, rows, path)],
                                  key=lambda t: t[0]["run"]["timestamp"])
            discarded.append(f"{os.path.basename(older[2])} -- superseded by "
                             f"{os.path.basename(newer[2])} (same config, newer)")
            by_config[cfg] = newer
        else:
            by_config[cfg] = (setup, rows, path)
    return by_config, discarded, (setver, pin)


def index_by_id(entries, key):
    return {e[key]: e for e in entries}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--store", default="store")
    ap.add_argument("--before", default="bounded@0.2:a7e0bdf",
                    metavar="SET@VER:PIN")
    ap.add_argument("--after", default="bounded@0.3:1989c62",
                    metavar="SET@VER:PIN")
    ap.add_argument("--tsv", default=None,
                    help="write the table here instead of stdout")
    args = ap.parse_args()

    before, disc_b, (bset, bpin) = load_side(args.store, args.before)
    after, disc_a, (aset, apin) = load_side(args.store, args.after)

    header = []
    add = header.append
    add("# bench/bounded ACROSS A SET VERSION AND A PIN -- a READ of pinned "
        "records, not a measurement.")
    add(f"# script       : docs/dev/measurements/{os.path.basename(__file__)}")
    add(f"# bench commit : {git_commit()}")
    add(f"# BEFORE       : {bset}  at pcrec {bpin}")
    add(f"# AFTER        : {aset}  at pcrec {apin}")
    add("# rule         : the two sets NEVER POOL (bench/bounded/NOTES.md). Only "
        "cells whose pattern id AND subject id")
    add("#                exist in both -- with EQUAL pattern canonical_sha256 and "
        "EQUAL subject sha256/bytes -- are")
    add("#                emitted, one row per (pattern, subject, regime, form, "
        "testee config). Cell against cell, never sum against sum.")
    add("# comparable   : pcrecbench.reduce.reduce_match_cell -- median over trials "
        "of per-row elapsed_ns/iterations;")
    add("#                ratio = after / before, so > 1 is SLOWER at the newer pin. "
        "A cell with any failing or gave-up")
    add("#                trial on either side carries its outcome in `note` and NO "
        "ratio.")
    add("# forms        : match-compliance is measured on the WHOLE-SUBJECT "
        "artifact, every other regime on `plain`")
    add("#                (adapters.py:form_for_regime); the two are different "
        "machines and never share a row.")
    add("# CAVEAT       : `iterations` is calibrated per (pattern, regime) over "
        "the WHOLE subject set of that regime")
    add("#                (harness.calibrate), and 0.3 changed both pools -- it "
        "appends match-only subjects up to 1024 B")
    add("#                and moves `short_search_max_bytes` 512 -> 258. So the "
        "two sides of a row may be timed at")
    add("#                DIFFERENT iteration counts even where the work is "
        "byte-identical: the `before_iters` /")
    add("#                `after_iters` columns carry them, and a ratio whose two "
        "sides differ by a large factor there is")
    add("#                a candidate calibration effect, not a pin effect. This "
        "file states the fact; it does not rule.")
    add("# records read :")
    for label, side in (("BEFORE", before), ("AFTER ", after)):
        for cfg in sorted(side):
            setup, _rows, path = side[cfg]
            add(f"#   {label} {setup['record_id']}  ({path}, machine "
                f"{setup['environment']['machine_id']}, status {setup['status']})")
    for line in disc_b + disc_a:
        add(f"# discarded   : {line}")

    # ---- the shared pattern / subject surface, checked not assumed
    any_b = next(iter(before.values()))[0]
    any_a = next(iter(after.values()))[0]
    pb = index_by_id(any_b["patterns"], "pattern_id")
    pa = index_by_id(any_a["patterns"], "pattern_id")
    sb = index_by_id(any_b["subjects"], "subject_id")
    sa = index_by_id(any_a["subjects"], "subject_id")

    shared_patterns, rejected_p = set(), []
    for pid in sorted(set(pb) & set(pa)):
        if pb[pid].get("canonical_sha256") != pa[pid].get("canonical_sha256"):
            rejected_p.append(f"pattern {pid}: canonical_sha256 differs "
                              f"({pb[pid].get('canonical_sha256')} vs "
                              f"{pa[pid].get('canonical_sha256')})")
        else:
            shared_patterns.add(pid)
    shared_subjects, rejected_s = set(), []
    for sid in sorted(set(sb) & set(sa)):
        if (sb[sid].get("sha256") != sa[sid].get("sha256")
                or sb[sid].get("bytes_offered") != sa[sid].get("bytes_offered")):
            rejected_s.append(f"subject {sid}: sha256/bytes differ")
        else:
            shared_subjects.add(sid)

    add(f"# patterns     : {len(pb)} in BEFORE, {len(pa)} in AFTER, "
        f"{len(set(pb) & set(pa))} ids in common, {len(shared_patterns)} "
        f"byte-identical (the emitted surface)")
    add(f"# subjects     : {len(sb)} in BEFORE, {len(sa)} in AFTER, "
        f"{len(set(sb) & set(sa))} ids in common, {len(shared_subjects)} "
        f"byte-identical (the emitted surface)")
    for line in rejected_p + rejected_s:
        add(f"# REJECTED     : {line}")
    if not rejected_p and not rejected_s:
        add("# REJECTED     : none -- every shared id is byte-identical on both "
            "sides (0.3's own no-drift promise, checked here)")

    # ---- the cells
    rows_out = []
    for cfg in CONFIG_KEYS:
        if cfg not in before or cfg not in after:
            add(f"# unpaired     : config {cfg} present on "
                f"{'BEFORE' if cfg in before else 'AFTER'} only -- no rows emitted")
            continue
        b_cells = cells_from_record(before[cfg][1])
        a_cells = cells_from_record(after[cfg][1])
        for key in sorted(set(b_cells) & set(a_cells)):
            pid, regime, form = key
            if pid not in shared_patterns:
                continue
            for sid in sorted(set(b_cells[key]) & set(a_cells[key])):
                if sid not in shared_subjects:
                    continue
                rb = reduce_match_cell(b_cells[key][sid])
                ra = reduce_match_cell(a_cells[key][sid])
                notes = []
                if rb.expectation_failing:
                    notes.append("before: " + ",".join(
                        f"{k}={v}" for k, v in sorted(rb.outcome_counts.items())))
                if ra.expectation_failing:
                    notes.append("after: " + ",".join(
                        f"{k}={v}" for k, v in sorted(ra.outcome_counts.items())))
                ok = (not notes and rb.median_ns and ra.median_ns)
                ratio = (ra.median_ns / rb.median_ns) if ok else None
                rows_out.append([
                    pid, sid, str(sb[sid].get("bytes_offered")), regime, form, cfg,
                    f"{rb.median_ns:.3f}" if rb.median_ns is not None else "",
                    f"{ra.median_ns:.3f}" if ra.median_ns is not None else "",
                    f"{ratio:.4f}" if ratio is not None else "",
                    f"{rb.stddev_ns:.3f}" if rb.stddev_ns is not None else "",
                    f"{ra.stddev_ns:.3f}" if ra.stddev_ns is not None else "",
                    str(rb.n_trials), str(ra.n_trials),
                    ",".join(str(i) for i in (rb.iters or [])),
                    ",".join(str(i) for i in (ra.iters or [])),
                    "; ".join(notes),
                ])

    add(f"# rows         : {len(rows_out)}")
    cols = ["pattern_id", "subject_id", "subject_bytes", "regime", "form",
            "testee_config", f"before_median_ns_{bpin}", f"after_median_ns_{apin}",
            "ratio_after_over_before", "before_stddev_ns", "after_stddev_ns",
            "before_trials", "after_trials", "before_iters", "after_iters",
            "note"]

    out = "\n".join(header) + "\n" + "\t".join(cols) + "\n"
    out += "".join("\t".join(r) + "\n" for r in rows_out)
    if args.tsv:
        with open(args.tsv, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"wrote {args.tsv} ({len(rows_out)} rows)")
    else:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
