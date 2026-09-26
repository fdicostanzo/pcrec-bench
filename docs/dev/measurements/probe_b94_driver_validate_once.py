#!/usr/bin/env python3
"""probe_b94_driver_validate_once.py -- [B94]/BD15's own timing evidence,
run through the REAL adapter's build of testees/pcre2/driver.c (never a
hand-rolled prototype -- rule 4 of docs/dev/measurements/CLAUDE.md).

Builds the pcre2 driver via `pcrecbench.adapters.discover()["pcre2"]
.prepare_driver()` (the same gcc -O2 -std=gnu11 -ldl build the harness
itself uses) and times `.` (find-all, PCRE2_UTF) over bench/utf8's
throughput subjects, on interp/jit/dfa, twice each: the default
VALIDATE-ONCE path, and `--utf-always-check` (the control-only flag that
restores the pre-[B94] always-check behaviour). Also runs the ill-formed-
subject refusal on both paths, and the search/match single-call path's own
scaling with `--iters`, to show it is linear-in-iters (not quadratic in
subject length) and negligible at bench/utf8's real (<=30 B) subject sizes.

Run from the repo root: python3 docs/dev/measurements/probe_b94_driver_validate_once.py
"""
import os
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from pcrecbench import adapters as _ad                      # noqa: E402
from pcrecbench.subbench import load as _load_sb             # noqa: E402


def run(argv, timeout=120):
    t0 = time.monotonic()
    out = subprocess.run(argv, capture_output=True, text=True, timeout=timeout)
    return out, time.monotonic() - t0


def main():
    adapter = _ad.discover()["pcre2"]
    tmp = tempfile.mkdtemp(prefix="pcrecbench-b94probe-")
    drv = adapter.prepare_driver(tmp)
    dot = os.path.join(tmp, "dot.rx")
    with open(dot, "wb") as f:
        f.write(b".")

    sb = _load_sb(os.path.join(ROOT, "bench", "utf8"))
    print("# bench/utf8 subjects (manifest_throughput.tsv):")
    for s in sb.subjects_for("throughput"):
        print("#   %-10s %10d B  sha256=%s" % (s.subject_id, s.length, s.sha256))
    print()

    print("== find-all over `.` under PCRE2_UTF: validate-once vs always-check ==")
    for engine_flags, label in ((["--utf"], "interp"),
                                (["--utf", "--jit"], "jit"),
                                (["--utf", "--dfa"], "dfa")):
        for sub in sb.subjects_for("throughput"):
            if sub.length > 1048576:
                continue
            base = [drv, "--pattern", dot, "--list", None, "--mode", "search",
                    "--find-all", "--utf8", "--iters", "1"] + engine_flags
            # one-subject list file per subject (kept identical to the
            # adapter's own --list protocol -- id<TAB>path, no header)
            lp = os.path.join(tmp, "one-%s.tsv" % sub.subject_id)
            with open(lp, "w", encoding="utf-8") as f:
                f.write("%s\t%s\n" % (sub.subject_id, sub.path))
            argv_once = [a if a is not None else lp for a in base]
            out_once, wall_once = run(argv_once)
            argv_always = argv_once + ["--utf-always-check"]
            skip_always = sub.length > 262144   # > 256 KB: minutes, skip
            if skip_always:
                print("%-6s %-10s %8d B  validate-once=%9.6f s  "
                      "always-check=SKIPPED (quadratic, minutes)"
                      % (label, sub.subject_id, sub.length, wall_once))
                continue
            out_always, wall_always = run(argv_always, timeout=180)
            row_once = [ln for ln in out_once.stdout.splitlines()
                       if ln.startswith("subject\t")][0]
            row_always = [ln for ln in out_always.stdout.splitlines()
                         if ln.startswith("subject\t")][0]
            same = (row_once.split("\t")[:7] + row_once.split("\t")[9:]
                   == row_always.split("\t")[:7] + row_always.split("\t")[9:])
            print("%-6s %-10s %8d B  validate-once=%9.6f s  "
                  "always-check=%9.6f s  ratio=%8.1fx  answers-identical=%s"
                  % (label, sub.subject_id, sub.length, wall_once, wall_always,
                     (wall_always / wall_once) if wall_once else float("inf"),
                     same))

    print()
    print("== ill-formed subject: refused by name, both paths ==")
    ill = os.path.join(tmp, "ill.bin")
    with open(ill, "wb") as f:
        f.write(("a" + "été " * 64).encode("utf-8") + b"\xff")
    ill_list = os.path.join(tmp, "ill.tsv")
    with open(ill_list, "w", encoding="utf-8") as f:
        f.write("ill\t%s\n" % ill)
    for always in (False, True):
        argv = [drv, "--pattern", dot, "--list", ill_list, "--mode", "search",
                "--find-all", "--utf", "--utf8", "--iters", "1"]
        if always:
            argv.append("--utf-always-check")
        out, _ = run(argv, timeout=30)
        row = [ln for ln in out.stdout.splitlines()
              if ln.startswith("subject\t")][0]
        print("  always_check=%-5s -> %s" % (always, row.split("\t")[2]))

    print()
    print("== search regime (single call/iteration, mode=search, no "
          "--find-all): scaling with --iters, on the LARGEST real "
          "bench/utf8 short subject vs the 256 KB throughput subject ==")
    largest_short = max(sb.subjects_for("search_short"), key=lambda s: s.length)
    t256 = [s for s in sb.subjects_for("throughput")
           if s.subject_id == "t-256k"][0]
    for sub, label in ((largest_short, "largest short (%d B)" % largest_short.length),
                       (t256, "t-256k (%d B)" % t256.length)):
        lp = os.path.join(tmp, "search-%s.tsv" % sub.subject_id)
        with open(lp, "w", encoding="utf-8") as f:
            f.write("%s\t%s\n" % (sub.subject_id, sub.path))
        for iters in (1, 1000):
            argv = [drv, "--pattern", dot, "--list", lp, "--mode", "search",
                    "--utf", "--iters", str(iters)]
            out, wall = run(argv, timeout=60)
            row = [ln for ln in out.stdout.splitlines()
                  if ln.startswith("subject\t")][0]
            secs = float(row.split("\t")[8])
            print("  %-28s iters=%-5d elapsed=%9.6f s  per-call=%12.9f s"
                  % (label, iters, secs, secs / iters))


if __name__ == "__main__":
    main()
