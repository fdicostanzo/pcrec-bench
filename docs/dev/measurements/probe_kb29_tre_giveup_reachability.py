#!/usr/bin/env python3
"""SCRATCH measurement only (KB-29's TRE reachability question,
docs/dev/known_issues.md, lane b98kb29): builds probe_kb29_tre_
failmalloc.c (an LD_PRELOAD malloc/calloc/realloc call counter, with an
optional fault-injection failure point) and probe_kb29_tre_giveup_
reachability.c (a driver.c-shaped two-call find-all sequence: call 1
matches a leading literal, call 2 runs the pattern's own backreference
machinery against a long run of one byte), then runs a matrix of
(backreference-group-count, b-run-length) combinations, counting how
many malloc/calloc/realloc calls happen strictly between each MARK
line -- i.e. inside compile(), inside call 1, and inside call 2.

The question this answers: can testees/tre/driver.c's find-all loop's
SECOND-OR-LATER tre_regnexecb() call ever return REG_ESPACE (the only
non-OK/non-NOMATCH code TRE's own source can produce from an exec call,
per tre-mem.c/tre-stack.c: it is returned only when a real malloc() call
fails)? If call 2 makes ZERO allocations across the whole matrix, no
amount of malloc-failure fault injection targeted at "call 2" can ever
produce one on this build -- REG_ESPACE can only arise here, on this
pinned libtre, at compile time (already a first-class `did-not-compile`
via the existing refusal path).

Run from this directory: `python3 probe_kb29_tre_giveup_reachability.py`
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SO = "/tmp/probe_kb29_tre_failmalloc.so"
BIN = "/tmp/probe_kb29_tre_giveup_reachability"

# (label, pattern) -- one to seven backreference groups, each `(b*)`,
# referenced in the SAME order right before a trailing literal 'c' that
# never appears in the subject (so call 2 must fully explore before
# answering NOMATCH -- the worst case for "does it ever allocate").
PATTERNS = []
for k in (1, 3, 5, 7):
    groups = "".join("(b*)" for _ in range(k))
    refs = "".join("\\%d" % (i + 1) for i in range(k))
    PATTERNS.append((k, "X|a" + groups + refs + "c"))

# b-run lengths per group count -- capped per group count because the
# backtracking search's TIME (not its allocation count -- see below) is
# exponential in the group count x b-run length; a cell that would run
# past PER_CELL_TIMEOUT is skipped rather than blowing the whole census's
# wall time, and the skip is itself printed (a TIMEOUT row is still
# informative: it demonstrates the pattern IS exercising the backtracking
# matcher hard, without answering the allocation question for that cell).
PER_CELL_TIMEOUT = 8
BLENS_BY_GROUPS = {
    1: [10, 100, 1000, 20000, 200000, 1000000],
    3: [10, 100, 1000, 5000, 20000],
    5: [10, 50, 200, 1000],
    7: [10, 30, 100, 300],
}


def build():
    subprocess.run(["gcc", "-O2", "-fPIC", "-shared", "-o", SO,
                     os.path.join(HERE, "probe_kb29_tre_failmalloc.c"),
                     "-ldl"], check=True)
    subprocess.run(["gcc", "-O2", "-o", BIN,
                     os.path.join(HERE,
                                  "probe_kb29_tre_giveup_reachability.c"),
                     "-ltre"], check=True)


def run_one(pattern, blen):
    env = dict(os.environ)
    env["TRE_FAILMALLOC_VERBOSE"] = "1"
    env["LD_PRELOAD"] = SO
    try:
        p = subprocess.run([BIN, pattern, str(blen), "8"], env=env,
                            capture_output=True, text=True,
                            timeout=PER_CELL_TIMEOUT)
    except subprocess.TimeoutExpired as e:
        return (e.stdout or ""), (e.stderr.decode() if isinstance(
            e.stderr, bytes) else (e.stderr or "")), True
    return p.stdout, p.stderr, False


def count_between(lines, start_marker, end_marker):
    n = 0
    counting = False
    for line in lines:
        if start_marker in line:
            counting = True
            continue
        if end_marker in line:
            break
        if counting and line.startswith("[failmalloc] alloc #"):
            n += 1
    return n


def main():
    build()
    print("== KB-29 TRE reachability: allocation census per phase ==")
    print("libtre: 0.9.0-1build1 (libtre-dev, this box)")
    print("gcc:", subprocess.run(["gcc", "--version"], capture_output=True,
                                  text=True).stdout.splitlines()[0])
    print("box:", subprocess.run(["uname", "-a"], capture_output=True,
                                  text=True).stdout.strip())
    print("loadavg (before):",
          open("/proc/loadavg").read().strip())
    print()
    print("Subject: 'Xa' + N x 'b' (no trailing 'c') -- call 1 matches "
          "the leading 'X' alone; call 2 runs a(b*)(b*)...\\1\\2...c "
          "against 'a'+the b-run, which can never find the required "
          "'c' -- the worst case for the backtracking matcher to fully "
          "explore before answering NOMATCH.")
    print()
    header = "%-8s %-10s %-8s %-8s %-8s %-16s" % (
        "groups", "b-run-len", "compile#", "call1#", "call2#", "call2-result")
    print(header)
    print("-" * len(header))
    rows = []
    for k, pat in PATTERNS:
        for blen in BLENS_BY_GROUPS[k]:
            out, err, timed_out = run_one(pat, blen)
            lines = err.splitlines()
            n_compile = count_between(lines, "before-compile", "after-compile")
            n_call1 = count_between(lines, "before-call-1", "after-call-1")
            n_call2 = count_between(lines, "before-call-2", "after-call-2")
            if timed_out:
                call2_result = "TIMEOUT>%ds" % PER_CELL_TIMEOUT
            else:
                call2_result = "?"
                for l in out.splitlines():
                    if l.startswith("call2"):
                        call2_result = l.split(" ", 1)[1] if " " in l else l
            rows.append((k, blen, n_compile, n_call1, n_call2, call2_result,
                         timed_out))
            print("%-8d %-10d %-8d %-8d %-8d %-16s"
                  % (k, blen, n_compile, n_call1, n_call2, call2_result))
    print()
    # a timed-out cell's call2# is a lower bound only (the process was
    # killed mid-call); it is EXCLUDED from the total below and reported
    # separately, never silently folded in as if it were a completed 0.
    completed = [r for r in rows if not r[6]]
    skipped = [r for r in rows if r[6]]
    total_call2_allocs = sum(r[4] for r in completed)
    print("SUMMARY: %d cells run (%d completed, %d timed out at %ds and "
          "excluded from the total below); total malloc/calloc/realloc "
          "calls inside call 2 across the %d COMPLETED cells: %d"
          % (len(rows), len(completed), len(skipped), PER_CELL_TIMEOUT,
             len(completed), total_call2_allocs))
    for r in skipped:
        print("  TIMED OUT (excluded): groups=%d b-run-len=%d" % (r[0], r[1]))
    if total_call2_allocs == 0:
        print("Zero allocations occurred inside any COMPLETED call-2 "
              "invocation, across 1-7 backreference groups and the "
              "b-run lengths that completed within %ds (10 B up to "
              "1,000,000 B at 1 group). Since REG_ESPACE can only be "
              "returned when a malloc()/calloc()/realloc() call genuinely "
              "fails (tre-mem.c/tre-stack.c), and no such call is ever "
              "observed inside a tre_regnexecb() exec call in this build, "
              "a SECOND-OR-LATER find-all call cannot return REG_ESPACE "
              "(or any other code) on any of these cells -- only REG_OK "
              "or REG_NOMATCH. The skipped (timed-out) cells are NOT "
              "claimed to make zero allocations -- they simply ran too "
              "long to bracket; this lane's own separate interactive "
              "check under /usr/bin/time -v (not part of this script) "
              "found RSS flat at ~2.18 MB regardless of pattern/subject "
              "size on several of the same timed-out shapes, consistent "
              "with the same zero-allocation mechanism, but this file "
              "does not claim to have proven that for these specific "
              "cells." % PER_CELL_TIMEOUT)


if __name__ == "__main__":
    sys.exit(main())
