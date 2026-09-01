#!/usr/bin/env python3
"""probe_hybrid_gained_edge.py -- the HYBRID-GAINED-EDGE CENSUS (outbox O-12
ask (v), inbox I-29 ask (v)): which cells' VM-hybrid prefilter DFA gained the
abi-13 `RX_DFA_SCAN_EDGE` at pcrec pin a7e0bdf, and what each of those cells
cost before and after.

THIS IS A READ OF PINNED RECORDS, NOT A MEASUREMENT. Nothing here compiles,
runs or times anything: every number below is arithmetic over
`store/records/<set>/<testee>/*.jsonl` that a window already measured. The
directory's D35 rules 1-4 apply to the ARCHIVE this writes (stable name,
source header, committed script); rule 5 applies as always -- no ranking
input, no schema, no reporter.

THE QUESTION. [OPT-5] STEP 1 (pcrec pin a7e0bdf, abi 13) replaces a maximal
run of scan states that differ only in how many bytes of one fixed class
have been counted with a bounded cursor loop, and stamps HOW the loop tests
that class as `RX_DFA_SCAN_EDGE` = `range` / `bitmap` / `mixed` / `none`.
The stamp's SCOPE is "every artifact that contains a DFA scan" -- every DFA
artifact AND every VM HYBRID (a VM body with a DFA prefilter). So a VM
artifact carrying a non-`none` edge is a hybrid whose PREFILTER gained the
edge while its match body stayed the VM's: that is the population Frank
asked to see enumerated before ruling the trade accepted or tunable
(ledger 2026-08-31-opt5-step1-acceptance-a7e0bdf.md 7.3/11 (v):
"thr x1.57-1.59 faster, match x1.04-1.05 slower").

THE SELECTOR, stated so it can be argued with:

    engine_metadata.engine == "vm"  AND
    engine_metadata.dfa_scan_edge not in (absent, "none")

`absent` is a pure-VM artifact with no DFA scan at all (the scope iff), and
`"none"` is a hybrid whose prefilter has a DFA scan but no scan edge in it.
Neither GAINED anything. The complement -- `engine == "dfa"` with an edge --
is the ladder's own population and is reported as a COUNT only: it is what
the acceptance ledger 3 already reads rung by rung.

WHICH REGIME EXERCISES WHICH ARTIFACT. `adapters.py:form_for_regime()`: the
`match` regime is measured on the WHOLE-SUBJECT form when the adapter built
one, every other regime on `plain`. So a whole-subject hybrid's only timed
cells are its `match-compliance` ones, and the throughput number reported
beside it in a ledger belongs to the SIBLING PLAIN artifact -- a different
machine. This script prints the sibling rows too, labelled `sibling-plain`,
because the trade is unreadable without them.

THE COMPARABLE is `pcrecbench.reduce`'s, imported rather than re-derived
(rule R5): per row `elapsed_ns / iterations`, summed over the set's subjects
per trial, median over trials. `ratio` is after / before, so > 1 is SLOWER
after; the `verdict` column spells that in words.

    python3 docs/dev/measurements/probe_hybrid_gained_edge.py \
        --set bounded@0.2 --after a7e0bdf --before 263b013 \
        --tsv docs/dev/measurements/2026-09-01-hybrid-gained-edge-census.tsv

Run from the repo root. With no `--tsv` it prints the table to stdout.
"""
import argparse
import glob
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)

from pcrecbench.reduce import (cells_from_record,  # noqa: E402
                               read_record, reduce_match_cell,
                               reduce_set_cell)

EDGE_KEY = "dfa_scan_edge"

HEADER = ("pattern\tform\tregime\tsubject\ttestee\tarm\tengine\tengine_sel"
          "\tdfa_prefilter\tdfa_scan\tedge_before\tedge_after"
          "\tmedian_ns_before\tmedian_ns_after\tratio\tverdict"
          "\tn_subjects\tstddev_ns_before\tstddev_ns_after")


# --------------------------------------------------------------- records

def records_for(set_name, pin, store):
    """{testee_id: (path, setup, rows)} for every record of `set_name` whose
    testee id names `pin`. When a testee has more than one record the LATEST
    by record_id (the trailing UTC stamp) wins, and the discard is named in
    the header block, never dropped silently."""
    out, extra = {}, []
    pat = os.path.join(store, "records", set_name, "*%s*" % pin, "*.jsonl")
    for path in sorted(glob.glob(pat)):
        setup, rows = read_record(path)
        tid = setup["testee"]["testee_id"]
        if tid in out:
            keep, drop = sorted([out[tid][1]["record_id"], setup["record_id"]])
            extra.append("%s: kept %s, ignored the earlier %s"
                         % (tid, keep if keep > drop else drop,
                            drop if keep > drop else keep))
            if setup["record_id"] < out[tid][1]["record_id"]:
                continue
        out[tid] = (path, setup, rows)
    return out, extra


def compile_artifacts(rows):
    """{(pattern_id, form): engine_metadata} -- one entry per artifact. Every
    trial re-emits the same artifact, so the LAST trial's metadata is taken
    and a disagreement between trials is raised rather than averaged."""
    out = {}
    for r in rows:
        if r.get("kind") != "compile":
            continue
        key = (r["pattern_id"], r.get("form") or "plain")
        em = r.get("engine_metadata") or {}
        if key in out and out[key] != em:
            raise SystemExit("artifact metadata differs between trials for %r"
                             % (key,))
        out[key] = em
    return out


def set_medians(rows):
    """{(pattern_id, regime, form): SetCell} over a record's match rows."""
    return {k: reduce_set_cell(v) for k, v in cells_from_record(rows).items()}


# ---------------------------------------------------------------- census

def gained_edge(arts):
    """The selector, in one place: (pattern, form) whose artifact is a VM
    HYBRID that gained a scan edge."""
    return sorted(k for k, em in arts.items()
                  if em.get("engine") == "vm"
                  and em.get(EDGE_KEY) not in (None, "none"))


def edge_counts(arts):
    """The whole record's engine x edge census, for the reading note."""
    out = {}
    for em in arts.values():
        key = (em.get("engine") or "-", em.get(EDGE_KEY) or "absent")
        out[key] = out.get(key, 0) + 1
    return out


def fmt(v, nd=1):
    return "-" if v is None else ("%.*f" % (nd, v))


def verdict_for(ratio):
    if ratio is None:
        return "-"
    if ratio >= 1.02:
        return "slower x%.2f" % ratio
    if ratio <= 0.98:
        return "faster x%.2f" % (1.0 / ratio)
    return "unmoved (x%.3f)" % ratio


def rows_for(pattern, form, arm, after, before, per_subject=False):
    """One census row per regime that measured this (pattern, form), and --
    when `per_subject` -- one row per SUBJECT under each of them.

    The per-subject rows are what make an aggregate ratio arguable: a flat
    per-call term and a term proportional to the bytes scanned produce the
    same set-grain number and different per-subject ones."""
    a_path, a_setup, a_rows = after
    b_path, b_setup, b_rows = before
    a_art = compile_artifacts(a_rows).get((pattern, form), {})
    b_art = compile_artifacts(b_rows).get((pattern, form), {})
    a_sets, b_sets = set_medians(a_rows), set_medians(b_rows)
    a_cells, b_cells = cells_from_record(a_rows), cells_from_record(b_rows)
    stamps = (a_art.get("engine") or "-", a_art.get("engine_sel") or "-",
              a_art.get("dfa_prefilter") or "-", a_art.get("dfa_scan") or "-",
              b_art.get(EDGE_KEY) or "absent", a_art.get(EDGE_KEY) or "absent")
    tid = a_setup["testee"]["testee_id"]

    def row(regime, subject, b_ns, a_ns, n, b_sd, a_sd, this_arm):
        ratio = (a_ns / b_ns) if (a_ns and b_ns) else None
        return ((pattern, form, regime, subject, tid, this_arm) + stamps
                + (fmt(b_ns), fmt(a_ns),
                   "-" if ratio is None else "%.4f" % ratio,
                   verdict_for(ratio), str(n), fmt(b_sd), fmt(a_sd)))

    out = []
    regimes = sorted({r for (p, r, f) in a_sets if p == pattern and f == form})
    for regime in regimes:
        a_cell, b_cell = a_sets.get((pattern, regime, form)), \
            b_sets.get((pattern, regime, form))
        out.append(row(regime, "-", b_cell.median_ns if b_cell else None,
                       a_cell.median_ns if a_cell else None,
                       a_cell.n_subjects if a_cell else 0,
                       b_cell.stddev_ns if b_cell else None,
                       a_cell.stddev_ns if a_cell else None, arm))
        if not per_subject:
            continue
        a_by, b_by = (a_cells.get((pattern, regime, form)) or {},
                      b_cells.get((pattern, regime, form)) or {})
        for sid in sorted(a_by):
            a_m = reduce_match_cell(a_by[sid])
            b_m = reduce_match_cell(b_by[sid]) if sid in b_by else None
            out.append(row(regime, sid, b_m.median_ns if b_m else None,
                           a_m.median_ns, 1,
                           b_m.stddev_ns if b_m else None, a_m.stddev_ns,
                           arm + "/subject"))
    return out


# ---------------------------------------------------------------- header

def git_head():
    try:
        return subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"],
                              capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:                                   # pragma: no cover
        return "<not a git checkout>"


def source_header(args, after, before, extra, counts):
    """D35 rule 3, adapted: this probe RUNS NOTHING, so the header names the
    inputs (the records, byte for byte) instead of a box and a load."""
    L = ["# THE HYBRID-GAINED-EDGE CENSUS (O-12/I-29 ask (v)) -- a READ of "
         "pinned records, not a measurement.",
         "# script       : docs/dev/measurements/probe_hybrid_gained_edge.py",
         "# bench commit : %s" % git_head(),
         "# sub-bench    : %s" % args.set,
         "# pins         : AFTER %s vs BEFORE %s" % (args.after, args.before),
         "# selector     : engine_metadata.engine == 'vm' AND dfa_scan_edge "
         "not in (absent, 'none')",
         "# comparable   : pcrecbench.reduce.reduce_set_cell -- ns/call "
         "summed over the set's subjects per trial, median over trials;",
         "#                ratio = after / before, so > 1 is SLOWER after.",
         "# forms        : match-compliance is measured on the WHOLE-SUBJECT "
         "artifact, every other regime on `plain`",
         "#                (adapters.py:form_for_regime); `sibling-plain` "
         "rows are the same pattern's OTHER artifact.",
         "# records read :"]
    for tid in sorted(set(after) | set(before)):
        for label, side in (("AFTER ", after), ("BEFORE", before)):
            if tid in side:
                path, setup, _rows = side[tid]
                L.append("#   %s %s  (%s, machine %s, status %s)"
                         % (label, setup["record_id"],
                            os.path.relpath(path, ROOT),
                            setup["environment"]["machine_id"],
                            setup.get("status", "?")))
    for line in extra:
        L.append("# duplicate   : %s" % line)
    L.append("# artifact census (AFTER, engine x dfa_scan_edge, one entry "
             "per pattern x form):")
    for tid in sorted(counts):
        L.append("#   %s: %s" % (tid, ", ".join(
            "%s/%s=%d" % (e, edge, n)
            for (e, edge), n in sorted(counts[tid].items()))))
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--set", default="bounded@0.2")
    ap.add_argument("--after", default="a7e0bdf")
    ap.add_argument("--before", default="263b013")
    ap.add_argument("--store", default=os.path.join(ROOT, "store"))
    ap.add_argument("--tsv", help="write the table here instead of stdout")
    args = ap.parse_args(argv)

    after, extra_a = records_for(args.set, args.after, args.store)
    before, extra_b = records_for(args.set, args.before, args.store)
    if not after:
        raise SystemExit("no %s records for pin %s under %s"
                         % (args.set, args.after, args.store))

    counts, rows = {}, []
    for tid in sorted(after):
        a = after[tid]
        arts = compile_artifacts(a[2])
        counts[tid] = edge_counts(arts)
        hits = gained_edge(arts)
        if not hits:
            continue
        b = before.get(tid.replace(args.after, args.before))
        if b is None:
            print("warning: no BEFORE record for %s" % tid, file=sys.stderr)
            continue
        for pattern, form in hits:
            rows.extend(rows_for(pattern, form, "hybrid-gained-edge",
                                 a, b, per_subject=True))
            other = "plain" if form == "whole-subject" else "whole-subject"
            if (pattern, other) in arts:
                rows.extend(rows_for(pattern, other, "sibling-plain", a, b))

    text = (source_header(args, after, before, extra_a + extra_b, counts)
            + HEADER + "\n"
            + "\n".join("\t".join(r) for r in rows) + "\n")
    if args.tsv:
        with open(args.tsv, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("probe_hybrid_gained_edge: %d row(s) over %d testee record(s) "
              "-> %s" % (len(rows), len(after), args.tsv))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
