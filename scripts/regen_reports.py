#!/usr/bin/env python3
"""scripts/regen_reports.py -- regenerate every committed report group IN
PLACE from its own header query. Written for the reporter-v24 wave ([B91],
lane b91views); reusable at any reporter bump. The full run is long and
loads the store group by group: the MANAGER launches it (detached, with a
DONE marker), never a lane.

Run from the repository root (a checkout that has merged lane/b91views):

    python3 scripts/regen_reports.py [--only SUBSTRING ...] [--list] [--pin-until-from-git]

For every committed report GROUP under reports/ (base name G with a G.tsv),
re-renders IN PLACE, from G.tsv's OWN header query (filters, grain, the
include_* flags), every sibling that exists:

    G.tsv                -- --format tsv at the header's grain
    G.md                 -- --format md, same grain
    G.subject-grain.md   -- --grain subject --format md
    G.subject-grain.tsv  -- --grain subject --format tsv, PLAIN if the
                            committed file carries `compile` rows (the
                            three 2026-09-23 capability groups, per [B87]),
                            else --subject-grain-slice
    G.matrix.tsv         -- --format matrix --grain set
    G.matrix.html        -- scripts/matrix_page.py G.matrix.tsv

Records are loaded ONCE per group (the KB-16 prefilter, exactly as
`report.main` does). One broken group never stops the others. Prints one
line per file (`OK`/`FAIL`, seconds) and ends with a summary line; chain a
DONE marker after it. It does NOT regenerate sidecars -- run
`python3 scripts/regen_sidecars.py` after it -- and does NOT classify
diffs: see the lane report for the expected classes and the GNU-diff
classification step (never difflib: b53regen's incident).

A G.md with no G.tsv (none today) is listed as SKIP: its query must
be re-rendered by hand from the .md's own `- filters:` line.
"""
import argparse
import gc
import os
import re
import subprocess
import sys
import time

ROOT = os.getcwd()
sys.path.insert(0, ROOT)
os.environ.setdefault("LC_ALL", "C")
from pcrecbench import report  # noqa: E402

REP = os.path.join(ROOT, "reports")


def header_argv(line):
    """The CLI argv a committed TSV header line encodes."""
    m = re.search(r"filters: (.*?); source:", line)
    filt = m.group(1) if m else "(none)"
    argv = []
    if filt != "(none)":
        for part in filt.split(", "):
            if part == "include-synthetic":
                argv.append("--include-synthetic")
                continue
            if part.startswith("where "):
                argv += ["--where", part[len("where "):]]
                continue
            k, _, v = part.partition("=")
            argv += [f"--{k}", v]
    flags = dict(re.findall(r"(\w+): (True|False)", line))
    if flags.get("include_unmeasured") == "True":
        argv.append("--include-unmeasured")
    if flags.get("include_scratch") == "True":
        argv.append("--include-scratch")
    if flags.get("all_records") == "True":
        argv.append("--all-records")
    if flags.get("include_provenance") == "True":
        argv.append("--include-provenance")
    g = re.search(r"grain: (\w+)", line)
    return argv, (g.group(1) if g else "set")


def build(argv, grain):
    args = report.build_argparser().parse_args(argv + ["--grain", grain])
    args.where = report._parse_where(args.where)
    args._subbench_alias_note = None
    if args.subbench:
        args.subbench, args._subbench_alias_note = report.resolve_subbench_arg(
            args.subbench, report.REPO_ROOT)
    rows, src = report.discover_index(args.store)
    args._source_desc = src
    return args, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--pin-until-from-git", action="store_true",
                    help="for a query with NO --until (18 groups today), add "
                         "--until = the UTC time of the commit that FIRST added "
                         "G.tsv, so records measured after the report was first "
                         "rendered (e.g. rust's 2026-09-22 re-measure) do not "
                         "silently enter it; printed per group")
    a = ap.parse_args()
    bases = sorted(f[:-4] for f in os.listdir(REP)
                   if f.endswith(".tsv") and not f.endswith((".matrix.tsv", ".subject-grain.tsv")))
    md_only = sorted(f[:-3] for f in os.listdir(REP)
                     if f.endswith(".md") and not f.endswith((".interpretation.md", ".subject-grain.md"))
                     and f[:-3] not in bases and f != "CLAUDE.md")
    for b in md_only:
        print(f"SKIP {b}: .md with no .tsv -- re-render by hand from its own '- filters:' line", flush=True)
    if a.only:
        bases = [b for b in bases if any(s in b for s in a.only)]
    if a.list:
        print("\n".join(bases))
        return 0
    n_ok = n_fail = 0
    for base in bases:
        p = lambda suf: os.path.join(REP, base + suf)  # noqa: E731
        try:
            with open(p(".tsv"), encoding="utf-8") as fh:
                head = fh.readline()
            argv, grain = header_argv(head)
            if a.pin_until_from_git and "--until" not in argv:
                iso = subprocess.check_output(
                    ["git", "log", "--diff-filter=A", "--format=%cI", "--",
                     os.path.join("reports", base + ".tsv")], text=True).strip().splitlines()[-1]
                from datetime import datetime, timezone
                until = datetime.fromisoformat(iso).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                argv += ["--until", until]
                print(f"PIN  {base}: --until {until} (first commit of its .tsv)", flush=True)
            t0 = time.time()
            args, rows = build(argv, grain)
            known = {r["testee_id"] for r in rows if r["testee_id"]}
            paths = [r["path"] for r in rows if report.index_row_could_match(r, args)]
            loaded = report.load_all(paths, check_filename=True)
            jobs = []
            rd, err = report.build_report(loaded, args, known_testee_ids=known)
            if err:
                raise RuntimeError(err)
            jobs.append((".tsv", report.render_tsv, rd))
            if os.path.exists(p(".md")):
                jobs.append((".md", report.render_markdown, rd))
            if grain == "set" and os.path.exists(p(".matrix.tsv")):
                jobs.append((".matrix.tsv", report.render_matrix_tsv, rd))
            for suf, fn, r in jobs:
                with open(p(suf), "w", encoding="utf-8") as fh:
                    fh.write(fn(r))
                print(f"OK   {base}{suf} ({time.time() - t0:.0f}s)", flush=True)
                n_ok += 1
            del rd
            gc.collect()
            if os.path.exists(p(".subject-grain.md")) or os.path.exists(p(".subject-grain.tsv")):
                sargs, _r = build(argv, "subject")
                srd, serr = report.build_report(loaded, sargs, known_testee_ids=known)
                if serr:
                    raise RuntimeError(serr)
                if os.path.exists(p(".subject-grain.md")):
                    with open(p(".subject-grain.md"), "w", encoding="utf-8") as fh:
                        fh.write(report.render_markdown(srd))
                    print(f"OK   {base}.subject-grain.md ({time.time() - t0:.0f}s)", flush=True)
                    n_ok += 1
                if os.path.exists(p(".subject-grain.tsv")):
                    with open(p(".subject-grain.tsv"), encoding="utf-8") as fh:
                        plain = any(ln.startswith("compile\t") for ln in fh)
                    fn = report.render_tsv if plain else report.render_tsv_subject_grain_slice
                    with open(p(".subject-grain.tsv"), "w", encoding="utf-8") as fh:
                        fh.write(fn(srd))
                    print(f"OK   {base}.subject-grain.tsv ({'plain' if plain else 'slice'}, "
                          f"{time.time() - t0:.0f}s)", flush=True)
                    n_ok += 1
                del srd
            del loaded
            gc.collect()
            if os.path.exists(p(".matrix.tsv")):
                rc = subprocess.call([sys.executable, "scripts/matrix_page.py", p(".matrix.tsv")],
                                     stdout=subprocess.DEVNULL)
                if rc:
                    raise RuntimeError(f"matrix_page.py rc={rc}")
                print(f"OK   {base}.matrix.html", flush=True)
                n_ok += 1
        except Exception as exc:  # noqa: BLE001
            n_fail += 1
            print(f"FAIL {base}: {exc!r}", flush=True)
    print(f"regen_reports: {len(bases)} group(s), {n_ok} file(s) written, {n_fail} group failure(s), "
          f"{len(md_only)} skipped (md-only)")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
