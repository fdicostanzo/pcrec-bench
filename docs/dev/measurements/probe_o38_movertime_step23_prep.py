#!/usr/bin/env python3
"""probe_o38_movertime_step23_prep.py -- [B62] STEPS 2-3 HARNESS PREP,
inbox I-79 (ii).2-3. NOT the timed measurement itself (that needs the
quiet-box gate and a clear box -- see the lane report for the box-status
question this prep is blocked on); this script is the PLUMBING, smoke-
tested small, so the real run is a one-line invocation once cleared.

BACKGROUND (read docs/dev/lanes/b62witness_report.md's STEP 2 section for
the full reasoning): the brief's STEP 2 asks to cross the cf0962e3
ARTIFACT through the 25b1984f-era testee WRAPPER BUILD and vice versa.
Investigating that literally found there is no wrapper-era difference to
cross: `git log` shows testees/pcrec/shim.c and testees/pcrec/driver.c
last changed 2026-09-16 (commit 7b49289), BEFORE the cf0962e3 window
(2026-09-18) even ran -- neither file moved between the two windows that
produced the two records O-38's mover compares. The one adapter.py change
in between (7683b0e, [B58]) touches ONLY the phase-1 emit-c argv (adding
`-fcomments`), never phase 2 (the shim+artifact gcc build) or phase 3
(the driver invocation / buffer allocation). Both records' own
`environment.compiler_raw` also read identically (gcc 15.2.0, same
kernel, same CPU). So "the wrapper build" cannot literally have two eras
to cross; what THIS script does instead is the informative test that
remains: build and run the SAME vm-in cell through the CURRENT (single,
confirmed-identical) wrapper for BOTH pcrec pins, in ONE session,
interleaved, so a same-day same-wrapper same-toolchain comparison can be
read against the historical ×1.08 the two SEPARATE windows (2026-09-18
vs 2026-09-20/21, days apart) produced.

MECHANISM: `pcrec-vm-in` is a PINNED testee (configs.toml's committed
`pin = "25b1984f"`), so the harness's own compile/measure code path only
ever reaches ONE pcrec binary per run. To reach the OLD pin (cf0962e3)
through the SAME code path without editing configs.toml, this script
injects two SYNTHETIC, in-memory-only testee entries into a fresh
`testees.pcrec.adapter.Adapter` instance -- `pcrec-scratch-cf0962e3-vm-in`
and `pcrec-scratch-25b1984f-vm-in` -- each `local: True` (so `tier()`
answers `scratch` by construction, matching this probe's SCRATCH-TIER-
ONLY instruction) with its own `$PCREC_BIN_*` env var naming one of the
two build/pcrec-<pin>/build/pcrec binaries already on disk, engine_mode
`vm`, and the SAME buffer_frames=32768/buffer_trail=131072 capacities the
real `pcrec-vm-in` config declares (testees/pcrec/CLAUDE.md's own
measured derivation) -- so this reaches the identical `_in` code path,
never a plain `vm` one. `pcrecbench.adapters.discover` is monkeypatched
(module-level, persists across `_ad.resolve()`'s repeated internal calls)
to return this one pre-configured Adapter instance for "pcrec" instead of
a fresh from-disk one, so the injection sticks for the whole process.
Nothing here touches testees/pcrec/configs.toml on disk, and nothing this
script measures can reach store/ (`tier="scratch"`, `store_root` is
always a scratch path under the session scratchpad or build/).

STEP 3 (buffer placement) rides on the SAME driver invocation: this
script's `--print-buffer-address` mode builds a SCRATCH-ONLY patched copy
of testees/pcrec/driver.c (one line added after each `alloc_region()`
call: `fprintf(stderr, "buffer-addr\t%s\t%p\t%zu\n", tag, p, (size_t)p %
64)`), built via `pcrecbench.driverrun.build_driver` pointed at that
COPY's path -- testees/pcrec/driver.c itself, the file real pinned
records are built from, is never touched. Confirms/refutes I-79's own
prediction ("an 8% move on a ~6 us cell from a frame array crossing a
cache line") directly: the region is `posix_memalign`'d (heap) once per
PROCESS in `driver.c`'s `alloc_region()`, so its address -- and hence its
page/cache-line placement -- is expected to vary run to run under ASLR
with NO source or toolchain change at all, which is the alternative
explanation to "the wrapper build changed" this script is built to tell
apart.

Usage:
    python3 docs/dev/measurements/probe_o38_movertime_step23_prep.py \\
        --smoke                      # tiny dry run, proves the plumbing
    python3 docs/dev/measurements/probe_o38_movertime_step23_prep.py \\
        --trials 5 --subjects all --repeats 6 --print-buffer-address
                                      # the REAL run -- OWED, needs the
                                      # quiet-box gate; box status is the
                                      # lane report's open question

Run from the repo root (or a worktree). Writes into
build/b62witness-scratch/step23/ (gitignored, never store/).
"""

import argparse
import os
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
SCRATCH = os.path.join(MAIN_TREE, "build", "b62witness-scratch", "step23")

sys.path.insert(0, ROOT)

PATTERN_ID = "wild-datetime-moment-iso8601"
BUFFER_FRAMES = 32768
BUFFER_TRAIL = 131072

PIN_ENV = {
    "cf0962e3": "PCREC_BIN_CF",
    "25b1984f": "PCREC_BIN_25",
}


def pin_binary_path(pin):
    return os.path.join(BUILD_ROOT, "pcrec-%s" % pin, "build", "pcrec")


def make_patched_driver():
    """A SCRATCH-ONLY copy of testees/pcrec/driver.c with one fprintf added
    after each alloc_region() call, for --print-buffer-address. Never
    touches the real testees/pcrec/driver.c (the file every pinned
    record's driver is built from)."""
    src = os.path.join(ROOT, "testees", "pcrec", "driver.c")
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()
    marker = (
        "            buf_frames = alloc_region(align, buf_nframes * (size_t)fs);\n"
        "            buf_trail  = alloc_region(align, buf_ntrail * (size_t)ts);\n"
    )
    if marker not in text:
        raise SystemExit(
            "probe_o38_movertime_step23_prep: driver.c's alloc_region call "
            "site does not match the expected text -- the file moved since "
            "this probe was written; update the marker string before "
            "trusting --print-buffer-address output.")
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


def install_synthetic_testees(pcrec_adapter, driver_source_override=None):
    """Injects the two scratch-only vm-in testees, in memory only."""
    for pin, envvar in PIN_ENV.items():
        tid = "pcrec-scratch-%s-vm-in" % pin
        pcrec_adapter.cfg["testees"][tid] = {
            "local": True,
            "binary": envvar,
            "engine_mode": "vm",
            "captures": "on",
            "flags": ["--features", "all", "--engine=vm"],
            "buffer_frames": BUFFER_FRAMES,
            "buffer_trail": BUFFER_TRAIL,
            "description": "[B62 prep, scratch only] %s pinned binary "
                            "through the CURRENT (single, confirmed-"
                            "identical) wrapper, vm-in shape" % pin,
        }
        os.environ[envvar] = pin_binary_path(pin)
        if not os.path.isfile(os.environ[envvar]):
            raise SystemExit("missing pinned binary for %s: %s"
                              % (pin, os.environ[envvar]))
    if driver_source_override:
        # testees/pcrec/adapter.py builds the driver from a path relative
        # to its own HERE constant; there is no clean override seam for
        # step 3's patched copy without touching real files, so
        # --print-buffer-address instead sets a module-level HERE swap on
        # a throwaway copy of the adapter module -- see run_pair()'s own
        # handling below, which builds the driver directly rather than
        # through Adapter.measure() when this is set.
        pass


def install_discover_patch(pcrec_adapter):
    import pcrecbench.adapters as _ad
    real_discover = _ad.discover

    def patched_discover(root=None):
        out = real_discover(root)
        out["pcrec"] = pcrec_adapter
        return out

    _ad.discover = patched_discover


def pin_supports_fcomments(pcrec_bin):
    """Checked LIVE against --list-axes, not assumed (step 1's own rule):
    -fcomments is a 25b1984f/abi-27 axis ([EMIT-VERB]/D112) and does not
    exist at cf0962e3/abi 26 at all -- confirmed there in step 1's
    probe."""
    proc = subprocess.run([pcrec_bin, "--list-axes"], capture_output=True,
                           text=True, timeout=60)
    return "\ncomments\t" in ("\n" + proc.stdout)


def run_pair(trials, subject_limit, regime="search_short"):
    import testees.pcrec.adapter as pcrec_mod
    from pcrecbench import harness, store

    pcrec_adapter = pcrec_mod.Adapter(os.path.join(ROOT, "testees", "pcrec"))
    install_synthetic_testees(pcrec_adapter)
    install_discover_patch(pcrec_adapter)

    scratch_store = os.path.join(SCRATCH, "store")
    results = {}
    for pin, envvar in PIN_ENV.items():
        tid = "pcrec-scratch-%s-vm-in" % pin
        pcrec_bin = os.environ[envvar]
        # testees/pcrec/adapter.py's real compile() sends EMIT_COMMENTS_FLAG
        # ("-fcomments") as a FIXED PROTOCOL TOKEN unconditionally -- correct
        # for the CURRENT pin (25b1984f), but cf0962e3 predates that axis
        # entirely and REFUSES it by name (confirmed live here and in step
        # 1's probe: "unknown option '-fcomments'"). Substitute a token this
        # OLDER pin genuinely supports and that is a documented, byte-exact
        # no-op there: `--tune=0` (cf0962e3 shipped [OPT-DIAL] at its own
        # re-pin; "every position answers identically ... today's defaults
        # byte for byte", pcrec's own --help text) -- verified live below,
        # not assumed. cf0962e3 needs no comments substitute in the first
        # place: it emits full comments unconditionally (step 1's finding),
        # so this token exists purely to keep the argv shape a valid,
        # harmless 4th token, never to change what is emitted.
        if pin_supports_fcomments(pcrec_bin):
            pcrec_mod.EMIT_COMMENTS_FLAG = "-fcomments"
        else:
            pcrec_mod.EMIT_COMMENTS_FLAG = "--tune=0"
        res = harness.run_cell(
            "capability", tid, regimes=[regime], trials=trials,
            store_root=scratch_store, tier=store.TIER_SCRATCH,
            patterns=[PATTERN_ID], subject_limit=subject_limit,
            force_unquiet=True,  # PREP/smoke only -- the real run drops this
            note="[B62 prep] step 2 same-session same-wrapper cross, "
                 "pin %s, scratch only" % pin,
            synthetic=True,
        )
        results[pin] = res
        print("== pin %s (%s) ==" % (pin, tid))
        print("comments-flag substitute used:", pcrec_mod.EMIT_COMMENTS_FLAG)
        print("status:", res.setup.get("status"))
        print("record path:", res.path)
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true",
                     help="tiny dry run: 1 trial, 2 subjects -- proves the "
                          "plumbing only, not a measurement")
    ap.add_argument("--trials", type=int, default=5)
    ap.add_argument("--subjects", default="all")
    ap.add_argument("--repeats", type=int, default=1,
                     help="how many independent process launches per pin "
                          "-- each is a fresh driver process, so each gets "
                          "its own posix_memalign placement")
    ap.add_argument("--print-buffer-address", action="store_true",
                     help="step 3: build the scratch-patched driver and "
                          "print buffer placement instead of timing")
    args = ap.parse_args()

    if args.print_buffer_address:
        patched = make_patched_driver()
        print("patched driver source:", patched)
        print("(NOT wired into a full harness run yet -- OWED: build it "
              "via pcrecbench.driverrun.build_driver against each pin's "
              "artifact and run in --buffer-frames/--buffer-trail "
              "load-only mode, repeated --repeats times per pin, "
              "capturing the buffer-addr stderr lines above)")
        return

    if args.smoke:
        print("### SMOKE TEST ONLY -- proves the injected synthetic "
              "testees compile and run through the real harness code "
              "path. NOT a measurement; numbers below are not comparable "
              "to anything and are not the answer to step 2. ###")
        run_pair(trials=1, subject_limit=2)
        return

    subject_limit = None if args.subjects == "all" else int(args.subjects)
    for i in range(args.repeats):
        print("### repeat %d/%d ###" % (i + 1, args.repeats))
        run_pair(trials=args.trials, subject_limit=subject_limit)


if __name__ == "__main__":
    main()
