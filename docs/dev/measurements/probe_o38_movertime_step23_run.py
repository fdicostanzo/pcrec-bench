#!/usr/bin/env python3
"""probe_o38_movertime_step23_run.py -- [B62] STEPS 2-3, THE REAL RUN,
lane b62run, inbox I-79 (ii).2-3.

BACKGROUND: docs/dev/lanes/b62witness_report.md's STEP 2 section found
there is no "wrapper era" to cross -- testees/pcrec/shim.c and driver.c,
and the box's gcc, are UNMOVED between the two historical windows that
produced the two records O-38's mover (+509.14 ns / x1.08 on
`wild-datetime-moment-iso8601` / `short-subject-search` /
`pcrec-vm-in`) compares. So this script answers the question that
remains: does the effect reproduce in a SAME-SESSION, same-wrapper,
same-toolchain, INTERLEAVED comparison of the two pcrec pins
(cf0962e3, 25b1984f) on that one cell, and does it correlate with the
caller-provided buffer's own placement (ASLR heap address mod 64)?

MECHANISM. `pcrec-vm-in` is a PINNED testee (one committed pin), so the
ordinary harness code path only ever reaches one pcrec binary. This
script reuses `docs/dev/measurements/probe_o38_movertime_step23_prep.py`'s
approach (committed, smoke-tested 2026-09-20): inject two SYNTHETIC,
in-memory-only `local: True` (scratch-tier-by-construction) testee
entries into a fresh `testees.pcrec.adapter.Adapter`, each pointed at one
pinned binary via its own `$PCREC_BIN_*`, with `pcrec-vm-in`'s own
buffer capacities (32768 frames / 131072 trail). Unlike the prep script,
this one does NOT go through `pcrecbench.harness.run_cell` (which would
average trials into set-grain medians and drop the raw per-trial buffer
placement) -- it calls `Adapter.compile()` directly once per pin to get
a `handle` (the driver path, the .so, the buffer args), builds a
SCRATCH-ONLY patched copy of `driver.c` (two `fprintf(stderr, ...)`
lines after each `alloc_region()` call -- the real driver.c is never
touched), swaps `handle["driver"]` to that patched binary, and then
calls `pcrecbench.harness.calibrate()` (the REAL calibration function)
once per pin to choose `iters`, followed by TRIALS independent driver
PROCESS launches per pin, INTERLEAVED at the trial granularity
(cf, 25, cf, 25, ...) rather than the prep script's block granularity,
so a same-session order effect cannot land entirely on one pin's side.

Each driver launch is one PROCESS, and `driver.c`'s `alloc_region()`
allocates both caller-provided regions via `posix_memalign` ONCE PER
PROCESS -- so every trial gets its own ASLR placement, with no source or
toolchain change at all. This script pairs each trial's SUM of
per-subject `elapsed_ns` (divided by that trial's iters, constant across
subjects within one trial -- the same quantity `pcrecbench.reduce`'s
set-grain reduction sums, verified against `elapsed_ns` being computed
at one calibrated `iters` for the whole subject list) with that same
trial's two buffer addresses' `% 64` from its own stderr.

THE DECISION RULE (agreed both sides, inbox I-79 ack / plan.md [B62]):
interleave does NOT reproduce x1.08 (the two pins' medians agree within
the report.py R8 cross-pin rule -- no more than 2x the larger stddev
apart) -> a between-session placement/box effect, NOTHING is filed as a
pcrec item, the result still goes out as a measurement + outbox closure.
DOES reproduce, with identical objects -> the buffer-placement print IS
the finding.

Usage:
    python3 docs/dev/measurements/probe_o38_movertime_step23_run.py \\
        --trials 10                  # the real run (default 10, exceeding
                                      # the original cell's 5)

Writes nothing to any store (scratch tier by construction, and this
script does not even call `store.write` -- it never builds a record).
Run from the repo root or a worktree; needs both pinned binaries already
built (`build/pcrec-cf0962e3`, `build/pcrec-25b1984f`).
"""

import argparse
import os
import statistics
import subprocess
import sys

ROOT = subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True
).strip()
COMMON = subprocess.check_output(
    ["git", "rev-parse", "--git-common-dir"], text=True
).strip()
if not os.path.isabs(COMMON):
    COMMON = os.path.abspath(os.path.join(ROOT, COMMON))
MAIN_TREE = os.path.dirname(COMMON)
BUILD_ROOT = os.path.join(MAIN_TREE, "build")
SCRATCH = os.path.join(MAIN_TREE, "build", "b62run-scratch")

sys.path.insert(0, ROOT)

PATTERN_ID = "wild-datetime-moment-iso8601"
REGIME = "search_short"
BUFFER_FRAMES = 32768
BUFFER_TRAIL = 131072

PIN_ENV = {
    "cf0962e3": "PCREC_BIN_CF",
    "25b1984f": "PCREC_BIN_25",
}


def pin_binary_path(pin):
    return os.path.join(BUILD_ROOT, "pcrec-%s" % pin, "build", "pcrec")


def make_patched_driver_source():
    """A SCRATCH-ONLY copy of testees/pcrec/driver.c with one fprintf added
    after each alloc_region() call -- the real driver.c is never touched.
    Byte-identical marker/patch to probe_o38_movertime_step23_prep.py's
    own make_patched_driver(), duplicated here (not imported) so this
    script has no import-by-path dependency on the prep script's module
    layout."""
    src = os.path.join(ROOT, "testees", "pcrec", "driver.c")
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    marker = (
        "            buf_frames = alloc_region(align, buf_nframes * (size_t)fs);\n"
        "            buf_trail  = alloc_region(align, buf_ntrail * (size_t)ts);\n"
    )
    if marker not in text:
        raise SystemExit(
            "probe_o38_movertime_step23_run: driver.c's alloc_region call "
            "site does not match the expected text -- the file moved since "
            "this probe was written; update the marker string before "
            "trusting the buffer-address output.")
    patched = text.replace(
        marker,
        marker +
        '            fprintf(stderr, "buffer-addr\\tframes\\t%p\\t%zu\\n", '
        'buf_frames, (size_t)buf_frames % 64);\n'
        '            fprintf(stderr, "buffer-addr\\ttrail\\t%p\\t%zu\\n", '
        'buf_trail, (size_t)buf_trail % 64);\n'
    )
    os.makedirs(SCRATCH, exist_ok=True)
    out = os.path.join(SCRATCH, "driver_stepwitness.c")
    with open(out, "w", encoding="utf-8") as f:
        f.write(patched)
    return out


def pin_supports_fcomments(pcrec_bin):
    proc = subprocess.run([pcrec_bin, "--list-axes"], capture_output=True,
                          text=True, timeout=60)
    return "\ncomments\t" in ("\n" + proc.stdout)


def build_pin_handle(pin, patched_driver_src, sb):
    """-> (handle, iters, cal_why) for one pin: compiles the pattern
    through the REAL Adapter.compile() code path (so the .so and its
    engine_metadata are exactly what a real record would carry), then
    swaps in the patched driver and calibrates through the REAL
    `pcrecbench.harness.calibrate()`."""
    import testees.pcrec.adapter as pcrec_mod
    from pcrecbench import driverrun, harness

    ad = pcrec_mod.Adapter(os.path.join(ROOT, "testees", "pcrec"))
    tid = "pcrec-scratch-%s-vm-in" % pin
    envvar = PIN_ENV[pin]
    os.environ[envvar] = pin_binary_path(pin)
    if not os.path.isfile(os.environ[envvar]):
        raise SystemExit("missing pinned binary for %s: %s"
                          % (pin, os.environ[envvar]))
    ad.cfg["testees"][tid] = {
        "local": True,
        "binary": envvar,
        "engine_mode": "vm",
        "captures": "on",
        "flags": ["--features", "all", "--engine=vm"],
        "buffer_frames": BUFFER_FRAMES,
        "buffer_trail": BUFFER_TRAIL,
        "description": "[B62 run, scratch only] %s pinned binary, "
                       "vm-in shape, patched driver for buffer-address "
                       "correlation" % pin,
    }

    pcrec_bin = os.environ[envvar]
    if pin_supports_fcomments(pcrec_bin):
        pcrec_mod.EMIT_COMMENTS_FLAG = "-fcomments"
    else:
        # cf0962e3 predates the [EMIT-VERB] `-fcomments` axis entirely and
        # refuses it by name (step 1's own finding); `--tune=0` is a
        # documented byte-exact no-op token that pin genuinely supports
        # ([OPT-DIAL], shipped at its own re-pin).
        pcrec_mod.EMIT_COMMENTS_FLAG = "--tune=0"

    workdir = os.path.join(SCRATCH, "work-%s" % pin)
    os.makedirs(workdir, exist_ok=True)
    ad.prepare(tid, workdir)
    cp = ad.compile(tid, PATTERN_ID, sb.pattern_bytes(PATTERN_ID), {}, 1,
                    workdir)
    cr = cp.get("plain")
    if cr is None or cr.outcome != "compiled":
        raise SystemExit("pin %s: pattern did not compile (%s): %s"
                         % (pin, cr.outcome if cr else "?",
                            cr.diagnostic if cr else "?"))
    handle = dict(cr.handle)

    patched_bin = driverrun.build_driver(
        patched_driver_src,
        os.path.join(workdir, "pcrec_driver_patched"), extra=["-ldl"])
    handle["driver"] = patched_bin

    subjects = sb.subjects_for(REGIME)
    iters, why, cal = harness.calibrate(ad, handle, REGIME, subjects,
                                        None, 120, None)
    return ad, handle, subjects, iters, why


def run_one_trial(handle, subjects, iters, listfile):
    """One driver PROCESS launch: parses BOTH the protocol stdout (via
    driverrun.run_driver, giving MatchRow objects with per-subject
    elapsed_ns/iters) and the patched driver's stderr buffer-addr lines.
    Returns (total_ns_per_call, n_ok_subjects, buffer_info) where
    buffer_info is {"frames": (ptr, mod64), "trail": (ptr, mod64)} or
    None if the lines were not found (a DFA artifact, or a build that did
    not patch -- neither expected here, checked)."""
    from pcrecbench import driverrun

    argv = ([handle["driver"], "--lib", handle["lib"], "--mode", "search",
            "--iters", str(iters)] + list(handle.get("buffer_args") or [])
            + ["--list", listfile])
    out = driverrun.run_driver(argv, timeout=120, pin=handle.get("pin"))
    if out.returncode != 0 or out.timed_out:
        raise SystemExit("driver trial failed (rc=%s, timed_out=%s): %s"
                         % (out.returncode, out.timed_out, out.diagnostic()))
    total_elapsed_ns = 0
    n_ok = 0
    for row in out.rows:
        if row.seconds > 0 and row.iters:
            total_elapsed_ns += row.seconds * 1e9
            n_ok += 1
    if n_ok == 0 or iters == 0:
        raise SystemExit("driver trial produced no usable timing rows")
    ns_per_call = total_elapsed_ns / iters

    buffer_info = {}
    for line in out.stderr.splitlines():
        cols = line.split("\t")
        if len(cols) == 4 and cols[0] == "buffer-addr":
            _tag, tag, ptr, mod64 = cols
            buffer_info[tag] = (ptr, int(mod64))
    return ns_per_call, n_ok, (buffer_info or None)


def cross_pin_within_spread(median_a, stddev_a, median_b, stddev_b):
    """report.py's own R8 cross-pin rule (module docstring, [B9] R8): two
    medians are `unchanged (within spread)` when they differ by no more
    than 2x the LARGER stddev; otherwise `faster`/`slower xN.NN`. Ported
    here rather than imported -- report.py's version operates on a
    LoadedRecord's reduced cells, not on raw trial lists, and importing
    it would need building two throwaway records for no benefit; the
    ARITHMETIC is the one thing that must match, and it does, verbatim."""
    spread = 2.0 * max(stddev_a, stddev_b)
    if abs(median_a - median_b) <= spread:
        return "unchanged (within spread)", None
    ratio = median_b / median_a if median_a else float("inf")
    return ("faster x%.2f" % (1.0 / ratio) if ratio < 1.0
            else "slower x%.2f" % ratio), ratio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=10,
                    help="trials PER PIN, interleaved cf/25/cf/25/... "
                         "(default 10, exceeding the original cell's 5)")
    args = ap.parse_args()

    from pcrecbench import subbench, driverrun

    sb = subbench.load(os.path.join(ROOT, "bench", "capability"))
    patched_src = make_patched_driver_source()
    print("patched driver source:", patched_src)

    handles = {}
    subjects_by_pin = {}
    iters_by_pin = {}
    for pin in ("cf0962e3", "25b1984f"):
        ad, handle, subjects, iters, why = build_pin_handle(
            pin, patched_src, sb)
        handles[pin] = handle
        subjects_by_pin[pin] = subjects
        iters_by_pin[pin] = iters
        print("== pin %s ==" % pin)
        print("  driver (patched):", handle["driver"])
        print("  lib:", handle["lib"])
        print("  buffer_args:", handle.get("buffer_args"))
        print("  calibration:", why)
        print("  iters:", iters)
        print("  n subjects (%s):" % REGIME, len(subjects))

    listfiles = {}
    for pin in handles:
        listfiles[pin] = driverrun.write_list(
            subjects_by_pin[pin],
            os.path.join(SCRATCH, "subjects-%s.tsv" % pin))

    results = {"cf0962e3": [], "25b1984f": []}
    print("\n== INTERLEAVED TRIALS (cf0962e3, 25b1984f, cf0962e3, ...) ==")
    for t in range(1, args.trials + 1):
        for pin in ("cf0962e3", "25b1984f"):
            ns, n_ok, buf = run_one_trial(
                handles[pin], subjects_by_pin[pin], iters_by_pin[pin],
                listfiles[pin])
            results[pin].append((t, ns, n_ok, buf))
            buf_str = (("frames%%64=%d trail%%64=%d"
                       % (buf["frames"][1], buf["trail"][1]))
                      if buf and "frames" in buf and "trail" in buf
                      else "NO BUFFER-ADDR LINES FOUND")
            print("trial %2d  pin %-9s  ns/call=%12.2f  n_subjects=%3d  %s"
                 % (t, pin, ns, n_ok, buf_str))

    print("\n== PER-PIN SUMMARY ==")
    summary = {}
    for pin, rows in results.items():
        vals = [r[1] for r in rows]
        med = statistics.median(vals)
        sd = statistics.stdev(vals) if len(vals) > 1 else 0.0
        summary[pin] = (med, sd)
        print("%-9s  n=%d  median=%.2f ns/call  stddev=%.2f ns (%.3f%%)"
             % (pin, len(vals), med, sd,
                100.0 * sd / med if med else float("nan")))

    verdict, ratio = cross_pin_within_spread(
        summary["cf0962e3"][0], summary["cf0962e3"][1],
        summary["25b1984f"][0], summary["25b1984f"][1])
    print("\n== CROSS-PIN VERDICT (report.py R8 rule) ==")
    print("cf0962e3 -> 25b1984f:", verdict,
         ("(ratio %.4f)" % ratio) if ratio is not None else "")
    historical_delta_ns = 509.14
    historical_ratio = 1.08
    print("historical (two separate windows, days apart): +%.2f ns / x%.2f"
         % (historical_delta_ns, historical_ratio))

    print("\n== BUFFER PLACEMENT CORRELATION ==")
    for pin, rows in results.items():
        print("-- pin %s --" % pin)
        for t, ns, n_ok, buf in rows:
            if buf and "frames" in buf and "trail" in buf:
                print("  trial %2d  ns/call=%12.2f  frames_addr=%s (%%64=%d)"
                     "  trail_addr=%s (%%64=%d)"
                     % (t, ns, buf["frames"][0], buf["frames"][1],
                        buf["trail"][0], buf["trail"][1]))
            else:
                print("  trial %2d  ns/call=%12.2f  NO BUFFER-ADDR LINES"
                     % (t, ns))

    print("\n== THE DECISION RULE (plan.md [B62], agreed both sides) ==")
    if verdict == "unchanged (within spread)":
        print("Interleaved comparison does NOT reproduce the historical "
             "x1.08 -- the two pins agree within spread in this "
             "same-session run. Per the agreed rule: a between-session "
             "placement/box effect, NOTHING is filed as a pcrec item. "
             "The result goes out as a measurement + outbox closure.")
    else:
        print(("Interleaved comparison DOES reproduce a cross-pin "
              "difference outside spread (%s). Per the agreed rule: since "
              "step 1 proved the emitted objects are byte-identical "
              "modulo the abi stamp, the buffer-placement print above IS "
              "the finding -- read the per-trial addr%%64 vs ns/call table "
              "for the correlation.") % verdict)


if __name__ == "__main__":
    main()
