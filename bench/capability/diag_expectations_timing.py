#!/usr/bin/env python3
"""diag_expectations_timing.py -- run `_diag_worker.py` ONE PATTERN AT A
TIME under `gnutimeout`, so a pathological (pattern, subject, regime)
cell is identified BY NAME instead of consuming the box indefinitely.
Diagnostic only (team-lead intervention, 2026-09-16): the committed
`gen_expectations.py` chain has no per-cell timeout by design (it is
shared, generic code, `pcrecbench/expectations.py`) -- this script
exists to FIND the hot cell(s) before deciding the structural fix.

Prints a running total and, for any pattern that times out, the LAST
timing line seen before the kill (the cell in progress).
"""
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench.subbench import load as load_subbench  # noqa: E402

PER_PATTERN_TIMEOUT_S = 90


def main():
    sb = load_subbench(HERE)
    slow = []
    timed_out = []
    for pat in sb.patterns:
        t0 = time.time()
        proc = subprocess.run(
            ["gnutimeout", str(PER_PATTERN_TIMEOUT_S), sys.executable, "-u",
             os.path.join(HERE, "_diag_worker.py"), pat.name],
            capture_output=True, text=True)
        wall = time.time() - t0
        lines = [l for l in proc.stdout.splitlines() if l.startswith("TIMING")]
        last = lines[-1] if lines else "<no cell completed>"
        if proc.returncode == 124:
            print("TIMEOUT  %-45s wall=%6.1fs  cells_done=%3d  stuck_after: %s"
                  % (pat.name, wall, len(lines), last))
            timed_out.append((pat.name, wall, len(lines), last))
            continue
        if proc.returncode != 0:
            print("ERROR    %-45s rc=%d  stderr=%s"
                  % (pat.name, proc.returncode, proc.stderr[:200]))
            continue
        print("done     %-45s wall=%6.2fs  cells=%3d  slowest=%s"
              % (pat.name, wall, len(lines),
                 max(lines, key=lambda l: float(l.split("\t")[4]))
                 if lines else "-"))
        if wall > 2.0:
            slow.append((pat.name, wall, len(lines)))

    print()
    print("=== summary ===")
    print("%d pattern(s) timed out at %ds:" % (len(timed_out),
                                                PER_PATTERN_TIMEOUT_S))
    for name, wall, n, last in timed_out:
        print("  %s (wall=%.1fs, %d cells done, stuck after: %s)"
              % (name, wall, n, last))
    print("%d pattern(s) over 2s wall:" % len(slow))
    for name, wall, n in sorted(slow, key=lambda t: -t[1]):
        print("  %-45s %6.2fs  (%d cells)" % (name, wall, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
