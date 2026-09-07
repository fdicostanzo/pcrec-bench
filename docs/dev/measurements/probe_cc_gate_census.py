#!/usr/bin/env python3
"""probe_cc_gate_census.py -- [B33] (1): THE CLANG COMPILE-ONLY GATE, made
repeatable.

THE ONE-OFF THIS REPLACES. At pin a7e0bdf (2026-08-31/09-01, [B24]'s lane)
a hand-run census compiled every bench pattern x 3 engine modes x 2 forms
under gcc and clang, compile-only, no timing, no quiet box, and found ONE
cause of clang divergence: a frameless VM artifact's indirect `goto
*label` in a function with no `&&label` expression ([CC-CLANG], fixed at
pcrec's abi 14). That census was NEVER scripted -- it lived in one lane's
throwaway work. Frank's ruling (inbox I-36, 2026-09-02) is to make it
PERMANENT: a re-pin-time script that enumerates every set, diffs clang's
refusal set against gcc's byte for byte, and archives the census per pin.

"3 MODES", CONFIRMED AGAINST THIS PROJECT'S OWN PRIOR USAGE, NOT THE
REGIME TOKENS. `pcrecbench/subbench.py`'s `REGIME_MODE` maps THREE regime
tokens (match/search_short/throughput) onto only TWO match semantics
(match/search) and has nothing to do with pcrec's engine selection --
crossing it with form would either produce duplicate compiles (search_short
and throughput both resolve to the PLAIN form) or need per-subbench
filtering by declared regimes, neither of which matches the ORIGINAL
census's own observed population (a refusal cause tied to FRAMELESS VM
artifacts, which only appears where the VM is forced or auto-selects it
broadly -- not tied to which regimes a set declares). This project's own
prior full-corpus census at this exact shape -- `testees/pcrec/CLAUDE.md`'s
[B26] entry: "the whole `RX_ENGINE_SEL` census -- 77 patterns x 2 forms
(plain, `(?:...)\\z`) x 3 ENGINE MODES (auto, nocaps, vm) = 462 cells per
pin" -- and `check_cc_axis`'s own `CC_KIND_CASES` (tools/selfcheck.py),
which pairs `pcrec-auto`/`pcrec-nocaps`/`pcrec-vm` against their `-clang`
siblings, both use "mode" for pcrec's THREE ENGINE CONFIGS. This script
follows that precedent: MODE is `auto` / `nocaps` / `vm` (the flags of
`pcrec-auto` / `pcrec-nocaps` / `pcrec-vm` in `testees/pcrec/configs.toml`,
read from there rather than retyped), FORM is `plain` / `whole-subject`
(`(?:pattern)\\z`) -- exactly the two pcrec compiles per pattern
(testees/pcrec/adapter.py `Adapter.compile`).

WHAT THIS SCRIPT DOES, per (subbench, pattern, mode, form) cell:

    1. emit-c ONCE (pcrec's own C output does not depend on which C
       compiler will consume it -- only on the pcrec FLAGS the mode picks
       and the pattern TEXT the form picks), at the pin's DEFAULT emitted-
       size caps (no raise: a set's own refusal boundary is part of what
       this gate reports, not a gap to paper over);
    2. if pcrec itself refuses (a real did-not-compile -- a size cap, the
       NFA-state cap, a feature gate under `--features all` that should
       never fire): ONE row, `gcc_result` == `clang_result` == that
       refusal's diagnostic -- no compiler ran, so there is nothing to
       diverge on;
    3. otherwise, build the SAME one-translation-unit shim+artifact
       command `testees/pcrec/adapter.py`'s phase 2 uses (shim.c
       `#include`s the artifact's `.c`), once under gcc and once under
       clang, recording each compiler's own outcome and diagnostic.

COMPILE-ONLY, NEVER A MEASUREMENT: no phase 3 (no dlopen, no driver, no
match run), no quiet-box gate, no timing collected beyond the wall clock
that lets a reader see where the time went (the same courtesy every
probe in this directory extends). Nothing here is a `pcrecbench run`
cell, so nothing here is a schema record.

THE GATE. `gcc_refusals` and `clang_refusals` are each the SET of cells
whose COMPILER (never pcrec) refused. The gate passes iff the two sets
are byte-identical; a cell is printed to stderr as a DIVERGENCE the
moment it is found, and the run's own exit code says pass/fail (0 parity,
1 divergence) -- a Makefile target can gate a re-pin on it. A divergence
is a FINDING to report (outbox), never something this script edits away.

THE PATTERNS, THE MODES, THE PIN -- all READ, never typed:

  - every `bench/<name>/` with a `subbench.toml` (`subbench_dirs()`,
    mirroring `tools/selfcheck.py`'s own enumeration rule: a gate that
    named a set would silently stop covering the day a new one landed).
  - each mode's FLAGS are read from `testees/pcrec/configs.toml`'s
    `pcrec-auto` / `pcrec-nocaps` / `pcrec-vm` entries (`load_mode_flags`),
    never retyped as a second copy that could drift from the roster.
  - the pin resolves through `testees/pcrec/pin.sh --path` (never asks it
    to BUILD -- safe to call even while the box belongs to another
    session's battery).

HOW TO RUN (serial, one compiler exec at a time, each under
`/usr/bin/gnutimeout <timeout>`; compile-only, NEVER a measurement):

    python3 docs/dev/measurements/probe_cc_gate_census.py \\
        --pin <sha> \\
        --out docs/dev/measurements/<date>-cc-gate-census-<sha>.txt

Run from the repo root. `--dry-run` prints every argv (emit-c, then gcc,
then clang, per cell) without invoking anything. `--subbench NAME`
(repeatable) restricts the sweep to named sets, for a quick rehearsal;
omitted, every set under `bench/` runs.
"""

import argparse
import os
import re
import shlex
import subprocess
import sys
import time

# docs/dev/measurements/probe_cc_gate_census.py -> up four -> repo root
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from pcrecbench.subbench import Subbench          # noqa: E402
from pcrecbench.record import whole_subject_text  # noqa: E402
from pcrecbench.driverrun import C_ENV            # noqa: E402

PIN_SH = os.path.join(ROOT, "testees", "pcrec", "pin.sh")
CONFIGS_TOML = os.path.join(ROOT, "testees", "pcrec", "configs.toml")
SHIM_C = os.path.join(ROOT, "testees", "pcrec", "shim.c")
BENCH_ROOT = os.path.join(ROOT, "bench")

GNUTIMEOUT = "/usr/bin/gnutimeout"

MODES = ("auto", "nocaps", "vm")
FORMS = ("plain", "whole-subject")
CENSUS_HEADER = ("subbench", "pattern", "mode", "form",
                 "gcc_result", "clang_result", "diagnostic")


def subbench_dirs():
    """Every `bench/<name>/` with a `subbench.toml`, sorted, by discovery --
    mirroring `tools/selfcheck.py`'s `subbench_dirs()` so a set that lands
    without an edit here is covered from its first commit."""
    out = []
    for name in sorted(os.listdir(BENCH_ROOT)):
        path = os.path.join(BENCH_ROOT, name)
        if os.path.exists(os.path.join(path, "subbench.toml")):
            out.append((name, path))
    return out


def load_mode_flags():
    """-> {mode: [flags]} for auto/nocaps/vm, read from
    `testees/pcrec/configs.toml`'s own `pcrec-auto`/`pcrec-nocaps`/
    `pcrec-vm` entries -- never a second copy of the roster's flags."""
    import tomllib
    with open(CONFIGS_TOML, "rb") as f:
        cfg = tomllib.load(f)
    testees = cfg["testees"]
    want = {"auto": "pcrec-auto", "nocaps": "pcrec-nocaps", "vm": "pcrec-vm"}
    out = {}
    for mode, tid in want.items():
        entry = testees.get(tid)
        if entry is None:
            raise SystemExit("%s: no [testees.%s] entry -- the mode roster "
                             "moved; update MODES/load_mode_flags"
                             % (CONFIGS_TOML, tid))
        out[mode] = list(entry.get("flags", []))
    return out


def resolve_pcrec(pin):
    """-> build/pcrec-<pin>/build/pcrec via `pin.sh --path` (never
    `pin.sh <pin>` -- this probe must never trigger a BUILD)."""
    proc = subprocess.run(["/bin/sh", PIN_SH, "--path", pin],
                          capture_output=True, text=True, timeout=30)
    if proc.returncode != 0:
        raise SystemExit("pin.sh --path %s failed: %s"
                         % (pin, proc.stderr.strip()))
    return proc.stdout.strip()


def load_all_patterns(names):
    """-> [(subbench_name, pattern_name, plain_bytes), ...] in each
    sidecar's own pattern order -- `pcrecbench.subbench.Subbench` is the
    harness's own loader (rule R5: a comparable is imported, never
    re-derived), so this probe reads exactly what a `pcrecbench run` cell
    would compile."""
    out = []
    for name, path in subbench_dirs():
        if names and name not in names:
            continue
        sb = Subbench(path)
        for p in sb.patterns:
            out.append((name, p.name, sb.pattern_bytes(p.name)))
    return out


def _diag_first_line(text):
    s = " ".join((text or "").split())
    return s[:200]


def run_one(argv, timeout):
    """-> (rc, diagnostic, wall_s). gnutimeout-wrapped; a HARNESS TIMEOUT
    is reported as its own diagnostic rather than raising, so one hanging
    cell does not abort the whole sweep."""
    full = [GNUTIMEOUT, str(timeout)] + argv
    t0 = time.monotonic()
    try:
        proc = subprocess.run(full, capture_output=True, env=C_ENV,
                              timeout=timeout + 60)
        rc = proc.returncode
        err = (proc.stderr or b"").decode("utf-8", "replace")
    except subprocess.TimeoutExpired:
        rc, err = -9, "HARNESS TIMEOUT (wall > gnutimeout %s + 60s backstop)" % timeout
    return rc, err, round(time.monotonic() - t0, 3)


def census_cell(pcrec_bin, workdir, sb_name, pattern_name, text, mode, form,
                mode_flags, timeout, dry_run, argv_sink):
    """One (subbench, pattern, mode, form) cell: emit-c once, then gcc and
    clang each once IFF pcrec's own emit succeeded. -> dict matching
    CENSUS_HEADER."""
    text_bytes = text if form == "plain" else whole_subject_text(text)
    cdir = os.path.join(workdir, sb_name, pattern_name, mode, form)
    art_c = os.path.join(cdir, "artifact.c")
    row = {"subbench": sb_name, "pattern": pattern_name, "mode": mode,
          "form": form, "gcc_result": "-", "clang_result": "-",
          "diagnostic": ""}

    emit_argv = ([pcrec_bin, "-p", "rx"] + mode_flags
                + ["-o", art_c, "--", text_bytes.decode("latin-1")])
    if dry_run:
        argv_sink.append(emit_argv)
    else:
        os.makedirs(cdir, exist_ok=True)
        rc, err, wall = run_one(emit_argv, timeout)
        if rc != 0:
            diag = "pcrec refused (emit-c, %.2fs): %s" % (wall, _diag_first_line(err))
            row["gcc_result"] = row["clang_result"] = "did-not-compile"
            row["diagnostic"] = diag
            return row

    for cc, key in (("gcc", "gcc_result"), ("clang", "clang_result")):
        so = os.path.join(cdir, "artifact-%s.so" % cc)
        gargv = ([cc, "-O2", "-std=gnu11", "-fPIC", "-shared",
                 "-o", so, SHIM_C,
                 "-DPB_ARTIFACT=\"%s\"" % art_c, "-I", cdir])
        if dry_run:
            argv_sink.append(gargv)
            continue
        rc, err, wall = run_one(gargv, timeout)
        if rc == 0:
            row[key] = "compiled"
        else:
            row[key] = "did-not-compile"
            note = "%s refused (%.2fs): %s" % (cc, wall, _diag_first_line(err))
            row["diagnostic"] = (row["diagnostic"] + "; " + note).lstrip("; ")
    return row


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pin", help="pcrec commit sha (required unless "
                    "--dry-run is the only thing you want)")
    ap.add_argument("--subbench", action="append", default=None,
                    help="restrict to this bench/<name> (repeatable); "
                    "omitted runs every set under bench/")
    ap.add_argument("--timeout", type=int, default=300,
                    help="gnutimeout seconds per exec (default 300)")
    ap.add_argument("--out", default=None,
                    help="write the verbatim table here (also printed to "
                    "stdout); omit to print only")
    ap.add_argument("--workdir", default=None,
                    help="scratch dir for emitted artifacts (default: a "
                    "tempdir under build/, cleaned as it goes)")
    ap.add_argument("--dry-run", action="store_true",
                    help="print every argv that would run and exit; makes "
                    "no pcrec/gcc/clang exec at all")
    args = ap.parse_args()

    if not args.pin and not args.dry_run:
        ap.error("--pin is required (pass --dry-run with a placeholder "
                 "--pin to preview argv against an unbuilt path)")
    if not args.pin:
        args.pin = "UNSET"

    pcrec_bin = resolve_pcrec(args.pin)
    if not os.access(pcrec_bin, os.X_OK):
        msg = ("no pcrec binary at %s (build it first: testees/pcrec/"
              "pin.sh %s -- this probe never builds one itself)"
              % (pcrec_bin, args.pin))
        if args.dry_run:
            print("# WARNING: %s -- printing argv against the unbuilt "
                 "path anyway" % msg, file=sys.stderr)
        else:
            raise SystemExit(msg)

    mode_flags = load_mode_flags()
    patterns = load_all_patterns(args.subbench)
    if not patterns:
        raise SystemExit("no patterns found (bad --subbench filter?)")

    workdir = args.workdir
    cleanup = False
    if workdir is None:
        import tempfile
        os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
        workdir = tempfile.mkdtemp(prefix="cc-gate-census-",
                                   dir=os.path.join(ROOT, "build"))
        cleanup = True
    os.makedirs(workdir, exist_ok=True)

    out_f = open(args.out, "w", encoding="utf-8") if args.out else None
    sinks = [sys.stdout] + ([out_f] if out_f else [])

    def emit(line=""):
        for s in sinks:
            print(line, file=s)

    emit("# docs/dev/measurements/probe_cc_gate_census.py -- "
        "the clang compile-only gate census")
    emit("# pin: %s   sets: %s   timeout: %ds"
        % (args.pin, ",".join(n for n, _ in subbench_dirs()
                              if not args.subbench or n in args.subbench),
          args.timeout))
    emit("# gcc: %s" % subprocess.run(["gcc", "--version"], capture_output=True,
                                     text=True).stdout.splitlines()[0]
        if not args.dry_run else "# gcc: (dry-run, not queried)")
    if not args.dry_run:
        emit("# clang: %s" % subprocess.run(["clang", "--version"],
                                            capture_output=True,
                                            text=True).stdout.splitlines()[0])
    emit("# %d pattern(s) x %d mode(s) x %d form(s) = %d cell(s)"
        % (len(patterns), len(MODES), len(FORMS),
          len(patterns) * len(MODES) * len(FORMS)))
    emit("# " + "\t".join(CENSUS_HEADER))

    argv_sink = []
    rows = []
    n = 0
    total_cells = len(patterns) * len(MODES) * len(FORMS)
    gcc_refusals, clang_refusals = set(), set()
    t_start = time.monotonic()
    for sb_name, pattern_name, text in patterns:
        for mode in MODES:
            for form in FORMS:
                n += 1
                row = census_cell(pcrec_bin, workdir, sb_name, pattern_name,
                                  text, mode, form, mode_flags[mode],
                                  args.timeout, args.dry_run, argv_sink)
                if args.dry_run:
                    continue
                rows.append(row)
                emit("\t".join(row[c] for c in CENSUS_HEADER))
                key = (sb_name, pattern_name, mode, form)
                pcrec_refused = row["gcc_result"] == row["clang_result"] == \
                    "did-not-compile" and row["diagnostic"].startswith(
                        "pcrec refused")
                if not pcrec_refused:
                    if row["gcc_result"] == "did-not-compile":
                        gcc_refusals.add(key)
                    if row["clang_result"] == "did-not-compile":
                        clang_refusals.add(key)
                print("  [%4d/%4d] %-10s %-16s %-7s %-13s gcc=%s clang=%s"
                     % (n, total_cells, sb_name, pattern_name, mode, form,
                       row["gcc_result"], row["clang_result"]),
                     file=sys.stderr)

    if args.dry_run:
        for argv in argv_sink:
            print(shlex.join(argv))
        if out_f:
            out_f.close()
        if cleanup:
            import shutil
            shutil.rmtree(workdir, ignore_errors=True)
        return 0

    elapsed = time.monotonic() - t_start
    emit("")
    emit("# %d cell(s), %d refused (pcrec emit-c), gcc refused %d, "
        "clang refused %d, wall %.1fs"
        % (len(rows),
          sum(1 for r in rows if r["diagnostic"].startswith("pcrec refused")),
          len(gcc_refusals), len(clang_refusals), elapsed))
    only_gcc = sorted(gcc_refusals - clang_refusals)
    only_clang = sorted(clang_refusals - gcc_refusals)
    if only_gcc or only_clang:
        emit("# DIVERGENCE: gcc-only refusals=%d clang-only refusals=%d"
            % (len(only_gcc), len(only_clang)))
        for k in only_gcc:
            emit("#   gcc-only refusal: %s" % (k,))
        for k in only_clang:
            emit("#   clang-only refusal: %s" % (k,))
        parity = False
    else:
        emit("# PARITY: gcc and clang refusal sets are byte-identical "
            "(%d cell(s) each)" % len(gcc_refusals))
        parity = True

    if out_f:
        out_f.close()
    if cleanup:
        import shutil
        shutil.rmtree(workdir, ignore_errors=True)
    return 0 if parity else 1


if __name__ == "__main__":
    sys.exit(main())
