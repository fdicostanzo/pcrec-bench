#!/usr/bin/env python3
"""docs/dev/measurements/probe_b117_olevel_census.py -- [B117] (Frank,
2026-09-29; plan row [B117], lane b117prep) THE COMPILEE OPTIMIZATION-LEVEL
COMPILE-ONLY CENSUS: every compiling bench/capability@0.1 pattern (read
from the set's own patterns.rxt via `pcrecbench.subbench.find`, never
retyped) x {auto, vm} engine mode x five `-O` levels
(o0/o1/o2/o3/os -- o2 is the pre-existing `pcrec-auto`/`pcrec-vm` testee,
the fixed level every OTHER pcrec testee compiles at; the other four are
[B117]'s own `pcrec-{auto,vm}-o{0,1,3,s}` testees, `testees/pcrec/
configs.toml`).

For each (pattern, engine, level) cell, plain form only (SCOPE: this
project's charter question is about the COMPILEE's optimization level,
which cannot move pcrec's own choice of PLAIN vs whole-subject artifact
-- the whole-subject form doubles gcc's bill for no answer this question
needs):

  * phase-2 (`gcc`) compile WALL TIME, seconds -- the SAME quantity
    `testees/pcrec/adapter.py:_compile_one`'s own `phase_seconds["gcc"]`
    records into every compile row, read directly off the SAME
    `CompileResult` a real `pcrecbench run` would build (this script
    calls the real adapter, `Adapter.compile`, never a hand-rolled gcc
    invocation -- so this census's numbers and a future window's own
    compile-cost column are the SAME measurement, not two).
  * the compiled `.so`'s WHOLE-FILE size (`artifact_bytes`, the same
    field a compile row carries) and its ELF `.text` SECTION size (via
    binutils `size`, `testees/pcrec/adapter.py`'s own `emit_bytes` /
    `emit_code_bytes` are pcrec's EMIT-side size definition and are
    provably UNCHANGED by this axis -- [B35]'s own frozen-renderer proof
    -- so the compiled OBJECT's own size, which cflags CAN move, is a
    different, necessary column here).
  * ANSWER IDENTITY against the level's own engine-mode `-O2` build (the
    pre-existing `pcrec-auto` / `pcrec-vm` testee): every `search_short`
    subject of the set (`Subbench.subjects_for`, never a hand-picked
    subset) measured through the REAL driver (`Adapter.measure`, the
    contract every timing window uses) and compared row for row --
    `matched`/`start`/`end` -- against the O2 baseline's own answers for
    the SAME pattern and engine mode. A mismatch here would mean the
    `-O` LEVEL broke codegen correctness (undefined behaviour a lower or
    higher optimization tier exposed differently), which is exactly the
    control [B35]'s own `pcrec-auto-align64` arm 4 and this project's
    `check_olevel_axis` (tools/selfcheck.py) already run on ONE hand-
    chosen witness each; this census widens that control to the WHOLE
    corpus rather than asserting it once and hoping it generalises.

COMPILE-ONLY, NO STORE WRITE, NO TIMING WINDOW: this is a correctness +
compile-cost + object-size SURVEY, not a measurement of MATCH time (the
`--trials`/`--iters`-averaged quantity a real `pcrecbench run` records).
Reading whether the compilee `-O` level moves MATCH time at all is the
window this script's own report hands to the manager
(docs/dev/lanes/b117prep_report.md's exact invocation).

Uses the REAL adapter end to end (`pcrecbench.adapters.discover()`,
`Adapter.prepare`/`Adapter.compile`/`Adapter.measure`) against the pin's
own built binary (`testees/pcrec/pin.sh` must already have built it --
this script never builds pcrec itself, the same posture every other
probe under this directory takes). `Adapter.compile()`'s PLAIN-form
result is read via `CompiledPattern.get(pcrecbench.adapters.FORM_PLAIN)`
-- the public API, never `_compile_one` directly, so a future adapter
refactor that keeps the public contract intact does not silently break
this script.

Run from the repo root:

    python3 docs/dev/measurements/probe_b117_olevel_census.py OUT.tsv
    python3 docs/dev/measurements/probe_b117_olevel_census.py --dry-run

`--dry-run` prints the job count and the first few jobs without running
anything (no gcc, no driver, no pcrec exec) -- for reviewing the SCOPE
before spending the box's time. `--jobs N` (default 4) parallelizes
across patterns with a process pool (each worker opens its own workdir,
so two workers never share one pcrec compile's scratch directory -- the
same rule `pcrecbench.adapters.Adapter.compile`'s own docstring states
for why a cell needs a fresh directory per pattern). `--limit N` caps the
pattern count (for a quick sanity run before spending the full census's
time). `--engines auto,vm` and `--levels o0,o1,o3,os` narrow the sweep.

Archived output (once run): docs/dev/measurements/2026-09-29-b117-olevel-census.txt
(the manager's own run, not this lane's -- see docs/dev/lanes/b117prep_report.md).
"""
import argparse
import concurrent.futures as cf
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from pcrecbench import adapters as _ad        # noqa: E402
from pcrecbench import subbench as _sb        # noqa: E402

PIN = "fc719ca4"  # [B118] re-pin a32bc86e -> fc719ca4; label only, testee
                  # ids below are read from configs.toml, never keyed here
ENGINES = {
    "auto": {"o0": "pcrec-auto-o0", "o1": "pcrec-auto-o1",
             "o2": "pcrec-auto", "o3": "pcrec-auto-o3",
             "os": "pcrec-auto-os"},
    "vm": {"o0": "pcrec-vm-o0", "o1": "pcrec-vm-o1",
           "o2": "pcrec-vm", "o3": "pcrec-vm-o3",
           "os": "pcrec-vm-os"},
}
LEVELS = ("o0", "o1", "o2", "o3", "os")


def _text_size(so_path):
    """-> the ELF `.text` section's byte size (binutils `size`), or None."""
    try:
        proc = subprocess.run(["size", so_path], capture_output=True,
                              text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None
    if proc.returncode != 0:
        return None
    lines = [ln for ln in proc.stdout.splitlines() if ln.strip()]
    if len(lines) < 2:
        return None
    try:
        return int(lines[1].split()[0])
    except (ValueError, IndexError):
        return None


def population(limit=None):
    sb = _sb.find("capability")
    names = [p.name for p in sb.patterns]
    if limit:
        names = names[:limit]
    return sb, names


def _rows_key(rows):
    """-> a tuple keyed by subject id -> (matched, start, end), so two
    row-lists compare by SUBJECT rather than by list position (a driver
    restart, KB-29-shaped, could otherwise reorder nothing but a caller
    should not rely on that)."""
    out = {}
    for r in rows:
        matched = str(r.answer).startswith("match")
        out[str(r.subject_id)] = (matched, r.start if matched else None,
                                  r.end if matched else None)
    return out


def one_engine_pattern(job):
    """-> list of TSV rows for one (engine, pattern) across all five
    levels: compiles each level once, builds the o2 baseline's answers
    once, and diffs every other level's answers against it."""
    engine, pid, levels = job
    sb = _sb.find("capability")
    pattern_bytes = sb.pattern_bytes(pid)
    subjects = sb.subjects_for("search_short")
    adapter = _ad.discover()["pcrec"]
    rows = []
    baseline_answers = None
    # o2 FIRST, always -- every other level's answer-identity column is a
    # diff against it, so it must exist before any other level can be
    # scored (an o2 refusal makes every sibling's identity column N/A).
    with tempfile.TemporaryDirectory(dir=os.environ.get("B117_SCRATCH")) as tmp:
        for level in ("o2",) + tuple(l for l in levels if l != "o2"):
            testee = ENGINES[engine][level]
            adapter.prepare(testee, tmp)
            cp = adapter.compile(testee, pid, pattern_bytes, {}, 1, tmp)
            cr = cp.get(_ad.FORM_PLAIN)
            row = {"engine": engine, "pattern": pid, "level": level,
                  "testee": testee, "outcome": cr.outcome if cr else "?"}
            if cr is None or cr.outcome != "compiled":
                row.update(gcc_wall_s="", so_bytes="", text_bytes="",
                          emit_bytes="", emit_code_bytes="",
                          answer_identity="n/a-refused",
                          diagnostic=(cr.diagnostic or "")[:200] if cr else "")
                rows.append(row)
                if level == "o2":
                    baseline_answers = None
                continue
            gcc_s = (cr.phase_seconds or [{}])[0].get("gcc", "")
            so_path = (cr.handle or {}).get("lib")
            so_bytes = os.path.getsize(so_path) if so_path and os.path.exists(so_path) else ""
            text_bytes = _text_size(so_path) if so_path else ""
            meta = cr.engine_metadata or {}
            got, _info, _notes = adapter.measure(dict(cr.handle), "search_short",
                                                 subjects, 1, 1, timeout=300)
            answers = _rows_key(got[0] if got else [])
            if level == "o2":
                baseline_answers = answers
                identity = "baseline"
            elif baseline_answers is None:
                identity = "n/a-no-baseline"
            else:
                diffs = [sid for sid, v in answers.items()
                        if baseline_answers.get(sid) != v]
                identity = "identical" if not diffs else \
                    "DIFFERS:" + ",".join(diffs[:5])
            row.update(gcc_wall_s="%.4f" % gcc_s if gcc_s != "" else "",
                      so_bytes=so_bytes, text_bytes=text_bytes if text_bytes else "",
                      emit_bytes=meta.get("emit_bytes", ""),
                      emit_code_bytes=meta.get("emit_code_bytes", ""),
                      answer_identity=identity, diagnostic="")
            rows.append(row)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("out", nargs="?", default=None,
                   help="output TSV path (required unless --dry-run)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--limit", type=int, default=None,
                    help="cap the pattern count (sanity runs)")
    ap.add_argument("--engines", default="auto,vm")
    ap.add_argument("--levels", default="o0,o1,o3,os",
                    help="always includes o2 as the baseline regardless "
                        "of this list")
    args = ap.parse_args()

    engines = [e.strip() for e in args.engines.split(",") if e.strip()]
    levels = [l.strip() for l in args.levels.split(",") if l.strip()]
    for e in engines:
        if e not in ENGINES:
            sys.exit("unknown engine %r (want auto/vm)" % e)
    for l in levels:
        if l not in LEVELS:
            sys.exit("unknown level %r (want one of %s)" % (l, LEVELS))

    sb, names = population(args.limit)
    jobs = [(e, pid, tuple(levels)) for e in engines for pid in names]

    print("population: %d pattern(s) x %d engine(s) x %d level(s) "
         "(+ o2 baseline) = %d compile cell(s)"
         % (len(names), len(engines), len(levels) + 1,
            len(names) * len(engines) * (len(levels) + 1)))
    if args.dry_run:
        print("first jobs:")
        for e, pid, lv in jobs[:10]:
            print("  engine=%s pattern=%s levels=o2,%s" % (e, pid, ",".join(lv)))
        return

    if not args.out:
        sys.exit("an output path is required unless --dry-run")

    os.makedirs(os.environ.get("B117_SCRATCH", "/var/tmp/b117scratch"),
               exist_ok=True)
    os.environ.setdefault("B117_SCRATCH", "/var/tmp/b117scratch")

    hdr = ["engine", "pattern", "level", "testee", "outcome", "gcc_wall_s",
          "so_bytes", "text_bytes", "emit_bytes", "emit_code_bytes",
          "answer_identity", "diagnostic"]
    n_compiled = n_refused = n_differs = 0
    with open(args.out, "w") as fh:
        fh.write("# [B117] compilee optimization-level census, pin %s\n" % PIN)
        fh.write("\t".join(hdr) + "\n")
        with cf.ProcessPoolExecutor(max(1, args.jobs)) as ex:
            for rows in ex.map(one_engine_pattern, jobs, chunksize=1):
                for r in rows:
                    fh.write("\t".join(str(r.get(k, "")) for k in hdr) + "\n")
                    if r["outcome"] != "compiled":
                        n_refused += 1
                    else:
                        n_compiled += 1
                        if str(r["answer_identity"]).startswith("DIFFERS"):
                            n_differs += 1
    print("DONE rows written; compiled=%d refused=%d answer_mismatches=%d"
         % (n_compiled, n_refused, n_differs))


if __name__ == "__main__":
    main()
