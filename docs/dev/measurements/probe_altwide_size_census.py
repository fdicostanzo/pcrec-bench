#!/usr/bin/env python3
"""probe_altwide_size_census.py -- [B35] (7) / [B39]: the altwide RAISED-CAP
SIZE CENSUS, turned into a stable, RE-RUNNABLE, PIN-PARAMETRIZED probe.

THE ONE-OFF THIS REPLACES. `docs/dev/measurements/2026-09-02-altwide-raised-
cap-sizes.txt` section 1 is a hand-run, pin-1989c62-only script (`census.py`,
reproduced verbatim at its own foot): every `bench/altwide@0.1` pattern x
both FORMS (`plain`, `whole-subject`) x both pcrec engine MODES (`auto`,
`vm`), compiled TWICE -- once at pcrec's DEFAULT emitted-size caps (the
`bench/altwide` refusal, verbatim) and once under a probe RAISE far above
anything the set could need -- recording pcrec's own emitted-size numbers
(`testees/pcrec/adapter.py`'s `emit_size` port) and the refusal wall clocks.
No timing regime, no measurement window: compile-only wall clocks, kept
because the COST of a refusal is itself one of that file's findings.

WHY IT NEEDED TO BECOME A SCRIPT RATHER THAN STAY A ONE-OFF. pcrec inbox
I-50 (docs/dev/ledgers/2026-09-05-b37-denysplit-after-334fd10e.md section 5
item 5) found the 2026-09-02 census STALE on the VM route by -18...-26 % per
rung at pin 334fd10e: [ENG-ISL] STEP 1's alternation-island trie (abi 17-18)
shrinks a VM artifact's emitted code by lowering a flat literal alternation
as a byte trie instead of `vm_alt`'s serial resume chain (the same section's
1.2/1.5), and [CC-DIFF] STEP 2 (abi 22) moves it back up by +68.5 B mean the
other way. Every future re-pin that touches VM code SHAPE will move these
numbers again, so [B39]'s plan row and [B35] (7) ask for a re-derivation
that takes the PIN as an argument instead of a hand-edited constant, so the
next re-pin's own work absorbs the re-census rather than opening a window
for it.

WHAT THIS SCRIPT DOES, per (pattern, form, mode) cell -- one call per pin,
same shape as the 2026-09-02 script:

    1. compile at pcrec's DEFAULT caps (no raise flags): outcome, which cap
       refused (if any) and the bytes pcrec quoted, and the wall clock;
    2. compile again under `--max-emit-bytes=N --max-emit-code-bytes=N` at
       `--probe-raise` (default 100,000,000, matching 2026-09-02): pcrec's
       own `emit_bytes` / `emit_code_bytes` (the `adapter.emit_size` port),
       the artifact's raw .c+.h byte count, and the wall clock.

The two are always run as a pair (default cap first, so a regression in the
DEFAULT-cap refusal boundary is caught even when `--probe-raise` is never
read) and merged into ONE output row, in the 2026-09-02 file's own column
order plus a leading `pin` column:

    pin  pattern  form  mode  emit_bytes  emit_code_bytes  raw_bytes
    raised_s  default_outcome  default_cap  default_bytes  default_s

THE PIN, THE PATTERNS, THE DEFAULTS -- all READ, never typed:

  - `--pin <sha>` resolves through `testees/pcrec/pin.sh --path <sha>` (the
    ONE place this repo computes a pin's build path; `pin.sh` is never
    asked to BUILD here -- `--path` only prints where a build would be,
    which is why it is safe to call even when the box belongs to another
    session's battery). A missing binary is refused BY NAME unless
    `--dry-run` is given, in which case the argv the run WOULD make is
    still printed against the unbuilt path -- a re-pin's own work can
    review the command shape before its build finishes.
  - the pattern set is READ from `bench/altwide/subbench.toml` via
    `pcrecbench.subbench.Subbench` (the harness's own loader, not a second
    parser of the sidecar) -- every pattern in the sidecar's own order,
    `floor` included, exactly as the 2026-09-02 `ORDER` list did by hand.
    `--set-version` only LABELS the output (the sidecar has no per-version
    pattern subdirectory to select between); it defaults to whatever
    version is checked out.
  - the default caps are READ from `testees/pcrec/list_limits.tsv`
    (`PCREC_MAX_EMIT_BYTES` / `PCREC_MAX_VM_EMIT_CODE_BYTES`), the pin's
    own `--list-limits` archive -- never retyped as a second copy of a
    pcrec constant that could fall out of step. This assumes the archive
    was re-archived at THIS pin already (the standing "re-archive at every
    re-pin" rule, testees/pcrec/CLAUDE.md); a probe-raise below either
    default is refused by name before anything compiles, mirroring the
    adapter's own raise-only rule for the same axis ([B31]).

`--compare <old-file>` reads a PREVIOUS census's own `#pattern\tform\t
mode\t...` table (this script's own `--out`, or the 2026-09-02 file, which
predates the `pin` column and parses the same way) and prints, per
(pattern, form), the OLD vs NEW `emit_bytes` / `emit_code_bytes` with a
delta in both bytes and percent, split into two sections -- one per ROUTE
(`auto`, `vm`) -- because the two routes moved in OPPOSITE directions
across 334fd10e (I-50) and a single merged table would hide that.

SELF-TEST (no pcrec binary, no compile, run 2026-09-05): `--compare`'s
parser was run against the real 2026-09-02 file with `--dry-run` (so the
"new" side is the empty table `--dry-run` produces) and confirmed it prints
"0 patterns compared" rather than crashing -- the "empty new table" case
the brief calls out. The arithmetic itself was checked separately, by
importing this module's `parse_census_table` / `compare_tables` functions
un-imported-as-`__main__` and feeding a hand-built SYNTHETIC new table
copied from the parsed 2026-09-02 rows with `w-512`'s `vm` emit_bytes
scaled by 0.80 (an -18...-26 % stand-in for I-50's finding) and `w-512`'s
`auto` row left untouched: the printed `vm` section showed
`678315 -> 542652  -135663  -20.00%` and the `auto` section showed `0` and
`0.00%` for the same pattern -- the sign, the route split and the
arithmetic all read correctly. No pcrec pin, no artifact and no timing was
touched by either check.

HOW TO RUN (serial, one pcrec exec at a time, each under
`/usr/bin/gnutimeout 600`; ~6 min on a quiet box, compile-only, NEVER a
measurement):

    python3 docs/dev/measurements/probe_altwide_size_census.py \\
        --pin <sha> \\
        --out docs/dev/measurements/<date>-altwide-size-census-<sha>.txt \\
        --compare docs/dev/measurements/2026-09-02-altwide-raised-cap-sizes.txt

Run from the repo root. `--dry-run` prints every argv (both the default-cap
and the raised-cap compile of every cell) without invoking pcrec at all.
"""

import argparse
import importlib.util
import os
import re
import shlex
import subprocess
import sys
import time

# docs/dev/measurements/probe_altwide_size_census.py -> up four -> repo root
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

sys.path.insert(0, ROOT)

from pcrecbench.subbench import Subbench          # noqa: E402
from pcrecbench.record import whole_subject_text  # noqa: E402
from pcrecbench.driverrun import C_ENV            # noqa: E402

PIN_SH = os.path.join(ROOT, "testees", "pcrec", "pin.sh")
LIST_LIMITS = os.path.join(ROOT, "testees", "pcrec", "list_limits.tsv")
ALTWIDE = os.path.join(ROOT, "bench", "altwide")

GNUTIMEOUT = "/usr/bin/gnutimeout"

# The refusal diagnostics, byte for byte as census.py (2026-09-02) matched
# them -- pcrec's own two size-cap error strings.
REF_TOTAL = re.compile(r"pattern too large: (\d+) bytes of emitted C source "
                       r"\(limit (\d+)")
REF_CODE = re.compile(r"pattern too large: (\d+) bytes of emitted code "
                      r"\(limit (\d+)\)")

CENSUS_HEADER = ("pin", "pattern", "form", "mode", "emit_bytes",
                 "emit_code_bytes", "raw_bytes", "raised_s",
                 "default_outcome", "default_cap", "default_bytes",
                 "default_s")
# The 2026-09-02 file's own header has no `pin` column -- this script's
# --compare must still parse it, so the OLD-file column set is the same
# tuple minus the first entry.
OLD_CENSUS_HEADER = CENSUS_HEADER[1:]


def emit_size_port():
    """-> pcrec's own two-quantity size port (`testees/pcrec/adapter.py`'s
    `emit_size`), loaded as a standalone module so this probe carries no
    second copy of the definition it measures against ([ART-SIZE])."""
    spec = importlib.util.spec_from_file_location(
        "pcrec_adapter_for_census",
        os.path.join(ROOT, "testees", "pcrec", "adapter.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.emit_size, mod.parse_warn_line


def resolve_pcrec(pin):
    """-> build/pcrec-<pin>/build/pcrec, via `pin.sh --path` (never
    `pin.sh <pin>` -- this probe must never trigger a BUILD; `--path` only
    prints where one would live, so it is safe to call even while the box
    belongs to another session's battery)."""
    proc = subprocess.run(["/bin/sh", PIN_SH, "--path", pin],
                          capture_output=True, text=True, timeout=30)
    if proc.returncode != 0:
        raise SystemExit("pin.sh --path %s failed: %s"
                         % (pin, proc.stderr.strip()))
    return proc.stdout.strip()


def read_default_caps():
    """-> (default_total, default_code), read from the pin's ARCHIVED
    `--list-limits` output (testees/pcrec/list_limits.tsv), never typed:
    PCREC_MAX_EMIT_BYTES / PCREC_MAX_VM_EMIT_CODE_BYTES. Assumes the
    archive was re-archived at the pin under test (the standing rule,
    testees/pcrec/CLAUDE.md's per-file table) -- this probe does not itself
    diff the archive against the live pin, `make check-harness` already
    does that."""
    want = {"PCREC_MAX_EMIT_BYTES": None, "PCREC_MAX_VM_EMIT_CODE_BYTES": None}
    with open(LIST_LIMITS, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            cols = line.rstrip("\n").split("\t")
            if cols and cols[0] in want:
                want[cols[0]] = int(cols[1])
    missing = [k for k, v in want.items() if v is None]
    if missing:
        raise SystemExit("%s: could not find %s (registry format changed?)"
                         % (LIST_LIMITS, ", ".join(missing)))
    return want["PCREC_MAX_EMIT_BYTES"], want["PCREC_MAX_VM_EMIT_CODE_BYTES"]


def load_patterns(set_version):
    """-> (version, [(name, bytes), ...]) in the sidecar's own order,
    `floor` included -- `pcrecbench.subbench.Subbench` is the harness's own
    loader (rule R5: a comparable is imported, never re-derived), so this
    probe reads exactly what a `pcrecbench run` cell would compile."""
    sb = Subbench(ALTWIDE)
    version = set_version or sb.version
    patterns = [(p.name, sb.pattern_bytes(p.name)) for p in sb.patterns]
    return version, patterns


def build_argv(pcrec_bin, art_c, text_bytes, mode, raised, probe_raise,
               timeout):
    flags = ["--features", "all"]
    if mode == "vm":
        flags.append("--engine=vm")
    if raised:
        flags += ["--max-emit-bytes=%d" % probe_raise,
                  "--max-emit-code-bytes=%d" % probe_raise]
    return ([GNUTIMEOUT, str(timeout), pcrec_bin, "-p", "rx"] + flags
            + ["-o", art_c, "--", text_bytes.decode("latin-1")])


def run_compile(argv, timeout):
    """One gnutimeout-wrapped pcrec exec. -> (rc, stderr_text, wall_s)."""
    t0 = time.monotonic()
    try:
        proc = subprocess.run(argv, capture_output=True, env=C_ENV,
                              timeout=timeout + 300)
        rc = proc.returncode
        err = (proc.stderr or b"").decode("utf-8", "replace")
    except subprocess.TimeoutExpired:
        rc, err = -9, "HARNESS TIMEOUT (wall > gnutimeout %s + 300s backstop)" % timeout
    return rc, err, round(time.monotonic() - t0, 3)


def classify_refusal(err):
    m = REF_CODE.search(err)
    if m:
        return "code", int(m.group(1)), int(m.group(2))
    m = REF_TOTAL.search(err)
    if m:
        return "total", int(m.group(1)), int(m.group(2))
    return "other", None, None


def census_row(pin, pcrec_bin, workdir, name, text, form, mode, probe_raise,
               timeout, emit_size, parse_warn_line, dry_run, argv_sink):
    """Both compiles (default, then raised) for one (pattern, form, mode)
    cell, merged into the 2026-09-02 file's own row shape."""
    text_bytes = text if form == "plain" else whole_subject_text(text)
    row = {"pin": pin, "pattern": name, "form": form, "mode": mode,
          "emit_bytes": "-", "emit_code_bytes": "-", "raw_bytes": "-",
          "raised_s": "-", "default_outcome": "-", "default_cap": "-",
          "default_bytes": "-", "default_s": "-"}

    # ---- pass 1: default caps, no raise
    d = os.path.join(workdir, "%s-%s-%s-default" % (name, form, mode))
    art = os.path.join(d, "artifact.c")
    argv = build_argv(pcrec_bin, art, text_bytes, mode, False, probe_raise,
                      timeout)
    if dry_run:
        argv_sink.append(argv)
    else:
        os.makedirs(d, exist_ok=True)
        rc, err, wall = run_compile(argv, timeout)
        row["default_s"] = "%.2f" % wall
        if rc == 0:
            row["default_outcome"] = "compiled"
        else:
            row["default_outcome"] = "did-not-compile"
            cap, bytes_, _limit = classify_refusal(err)
            row["default_cap"] = cap
            row["default_bytes"] = bytes_ if bytes_ is not None else "-"

    # ---- pass 2: the probe raise
    d2 = os.path.join(workdir, "%s-%s-%s-raised" % (name, form, mode))
    art2 = os.path.join(d2, "artifact.c")
    argv2 = build_argv(pcrec_bin, art2, text_bytes, mode, True, probe_raise,
                       timeout)
    if dry_run:
        argv_sink.append(argv2)
        return row
    os.makedirs(d2, exist_ok=True)
    rc, err, wall = run_compile(argv2, timeout)
    row["raised_s"] = "%.2f" % wall
    if rc != 0:
        # THE ONE population 2026-09-02 found empty (80/80 raised compiles
        # succeeded) -- kept as a live path rather than assumed, because a
        # re-pin is exactly the kind of change that could grow the emitted
        # size past even a 100 MB probe.
        row["emit_bytes"] = "REFUSED(raised): %s" % " ".join(err.split())[:120]
        return row
    files = [art2]
    h = art2[:-2] + ".h"
    if os.path.exists(h):
        files.append(h)
    total, code = emit_size(files)
    row["emit_bytes"] = total
    row["emit_code_bytes"] = code
    row["raw_bytes"] = sum(os.path.getsize(f) for f in files)
    for f in files:
        os.unlink(f)
    return row


# ------------------------------------------------------------- --compare

def parse_census_table(path):
    """-> {(pattern, form, mode): {col: value}} read out of a census file's
    own `#pattern\\tform\\tmode\\t...` table -- this script's `--out`, or
    the 2026-09-02 file (no `pin` column; both parse, keyed the same way).
    Stops at the first blank line or the next `#`-prose line after the
    header, exactly where the data table itself ends."""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    header_i = None
    for i, ln in enumerate(lines):
        if ln.rstrip("\n").lstrip("#").split("\t")[:4] == [
                "pattern", "form", "mode", "emit_bytes"]:
            header_i = i
            break
    if header_i is None:
        raise SystemExit("%s: no '#pattern\\tform\\tmode\\temit_bytes...' "
                         "census table header found" % path)
    cols = lines[header_i].rstrip("\n").lstrip("#").split("\t")
    rows = {}
    for ln in lines[header_i + 1:]:
        s = ln.rstrip("\n")
        if not s or s.startswith("#"):
            break
        parts = s.split("\t")
        if len(parts) != len(cols):
            continue
        rec = dict(zip(cols, parts))
        rows[(rec["pattern"], rec["form"], rec["mode"])] = rec
    return rows


def _num(rec, col):
    v = rec.get(col)
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def compare_tables(old_rows, new_rows, out):
    """Per-route (`auto`, `vm`) delta tables over keys present in BOTH
    sides, on `emit_bytes` and `emit_code_bytes` -- the two quantities that
    moved oppositely across 334fd10e (I-50)."""
    keys = sorted(set(old_rows) & set(new_rows))
    print("# --compare: %d rows in old table, %d in new, %d keys in both"
         % (len(old_rows), len(new_rows), len(keys)), file=out)
    if not keys:
        print("# 0 patterns compared", file=out)
        return
    for mode in ("auto", "vm"):
        mkeys = [k for k in keys if k[2] == mode]
        print("\n== route: %s (%d cells) ==" % (mode, len(mkeys)), file=out)
        print("#pattern\tform\told_emit_bytes\tnew_emit_bytes\td_bytes\td_pct"
             "\told_emit_code_bytes\tnew_emit_code_bytes\td_code_bytes"
             "\td_code_pct", file=out)
        for pattern, form, m in mkeys:
            o, n = old_rows[(pattern, form, m)], new_rows[(pattern, form, m)]
            ob, nb = _num(o, "emit_bytes"), _num(n, "emit_bytes")
            oc, nc = _num(o, "emit_code_bytes"), _num(n, "emit_code_bytes")
            if ob is None or nb is None or oc is None or nc is None:
                print("%s\t%s\t(non-numeric emit_bytes/emit_code_bytes on "
                     "one side -- a refused raised compile; see the row "
                     "verbatim)" % (pattern, form), file=out)
                continue
            db, dc = nb - ob, nc - oc
            pb = (db / ob * 100.0) if ob else float("nan")
            pc = (dc / oc * 100.0) if oc else float("nan")
            print("%s\t%s\t%d\t%d\t%+d\t%+.2f%%\t%d\t%d\t%+d\t%+.2f%%"
                 % (pattern, form, ob, nb, db, pb, oc, nc, dc, pc), file=out)


# ------------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pin", help="pcrec commit sha (required unless "
                    "--dry-run is the only thing you want)")
    ap.add_argument("--set-version", default=None,
                    help="label only; defaults to bench/altwide/"
                    "subbench.toml's own version")
    ap.add_argument("--probe-raise", type=int, default=100_000_000,
                    help="--max-emit-bytes / --max-emit-code-bytes value "
                    "for the raised pass (default: 100000000, matching "
                    "2026-09-02)")
    ap.add_argument("--timeout", type=int, default=600,
                    help="gnutimeout seconds per pcrec exec (default 600)")
    ap.add_argument("--out", default=None,
                    help="write the verbatim table here (also printed to "
                    "stdout); omit to print only")
    ap.add_argument("--compare", default=None, metavar="OLD_FILE",
                    help="print per-route deltas vs a previous census file")
    ap.add_argument("--workdir", default=None,
                    help="scratch dir for emitted artifacts (default: a "
                    "tempdir, cleaned as it goes)")
    ap.add_argument("--dry-run", action="store_true",
                    help="print every argv that would run and exit; makes "
                    "no pcrec exec at all")
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

    version, patterns = load_patterns(args.set_version)

    default_total = default_code = None
    if not args.dry_run:
        default_total, default_code = read_default_caps()
        if args.probe_raise < max(default_total, default_code):
            raise SystemExit(
                "--probe-raise=%d is below the pin's own default caps "
                "(total %d, code %d, from %s) -- pcrec's own caps are "
                "raise-only per compile ([ART-SIZE]); refusing before "
                "anything compiles." % (args.probe_raise, default_total,
                                       default_code, LIST_LIMITS))

    emit_size, parse_warn_line = emit_size_port()

    workdir = args.workdir
    cleanup = False
    if workdir is None:
        # NEVER the system /tmp (BD3, "large scratch under the session
        # scratchpad or /var/tmp, never /tmp root"): this script outlives
        # any one session, so the default lives under the repo's own
        # build/ rather than a session-specific scratchpad path.
        import tempfile
        os.makedirs(os.path.join(ROOT, "build"), exist_ok=True)
        workdir = tempfile.mkdtemp(prefix="altwide-census-",
                                   dir=os.path.join(ROOT, "build"))
        cleanup = True
    os.makedirs(workdir, exist_ok=True)

    out_f = open(args.out, "w", encoding="utf-8") if args.out else None
    sinks = [sys.stdout] + ([out_f] if out_f else [])

    def emit(line=""):
        for s in sinks:
            print(line, file=s)

    emit("# docs/dev/measurements/probe_altwide_size_census.py -- "
        "altwide raised-cap size census")
    emit("# pin: %s   set: altwide@%s   probe-raise: %d   timeout: %ds"
        % (args.pin, version, args.probe_raise, args.timeout))
    if default_total is not None:
        emit("# default caps (from %s): total %d, code %d"
            % (os.path.relpath(LIST_LIMITS, ROOT), default_total,
              default_code))
    emit("# " + "\t".join(CENSUS_HEADER))

    argv_sink = []
    new_rows = {}
    n = 0
    total_cells = len(patterns) * 2 * 2
    for name, text in patterns:
        for form in ("plain", "whole-subject"):
            for mode in ("auto", "vm"):
                n += 1
                row = census_row(args.pin, pcrec_bin, workdir, name, text,
                                 form, mode, args.probe_raise, args.timeout,
                                 emit_size, parse_warn_line, args.dry_run,
                                 argv_sink)
                if args.dry_run:
                    continue
                new_rows[(name, form, mode)] = {
                    k: str(v) for k, v in row.items() if k != "pin"}
                emit("\t".join(str(row[c]) for c in CENSUS_HEADER))
                print("  [%3d/%3d] %-12s %-13s %-4s %s"
                     % (n, total_cells, name, form, mode,
                       row["default_outcome"]), file=sys.stderr)

    if args.dry_run:
        for argv in argv_sink:
            print(shlex.join(argv))
        if args.compare:
            # SELF-TEST PATH (no pcrec binary needed): --dry-run computes
            # no rows at all, so `new_rows` is genuinely EMPTY here -- the
            # "empty/synthetic new table" case the probe's own header
            # docstring calls out. This proves parse_census_table() and
            # compare_tables() run end to end against a REAL old file
            # without crashing or dividing by a missing key; it is not a
            # substitute for the arithmetic self-test (see the docstring).
            old_rows = parse_census_table(args.compare)
            print("\n# --dry-run + --compare: SELF-TEST (0 new rows by "
                 "construction; proves the parser and the empty-diff path)")
            compare_tables(old_rows, {}, sys.stdout)
        if out_f:
            out_f.close()
        if cleanup:
            import shutil
            shutil.rmtree(workdir, ignore_errors=True)
        return

    if args.compare:
        old_rows = parse_census_table(args.compare)
        emit("")
        compare_tables(old_rows, new_rows, sys.stdout)
        if out_f:
            compare_tables(old_rows, new_rows, out_f)

    if out_f:
        out_f.close()
    if cleanup:
        import shutil
        shutil.rmtree(workdir, ignore_errors=True)


if __name__ == "__main__":
    main()
