#!/usr/bin/env python3
"""probe_gate_shape.py -- what the quiet gate's AFTER-sample rejects versus
what the trials themselves say (the 2026-08-30 gate-shape test run, BD7 and
the schema v1.4 proposal that follows it).

Reads PINNED RECORDS (never measures anything) and prints, per record:

  * the stamped `status`, the occupancy instrument (`environment.occupancy
    .tool`), and both samples' judged `max_busy_pct` + verdict;
  * the OLD 1-s gate's verdict RECOMPUTED from the per-second peaks a BD7
    record carries in `occupancy.after.raw` ("per-second peak busy% of the
    busiest non-target core: ..."): `first-second` is the closest analogue
    of the old `mpstat -P ALL 1 1` (its one interval), `any-second` is the
    worst case the old gate could have drawn. A pre-BD7 record (tool
    `... 1 1`) has no peaks: its stamped verdict IS the old gate's.
  * the TRIAL-SPREAD distribution over every timed match row: for each
    (pattern, regime, subject) the per-trial ns/iteration, spread =
    (max - min) / median across the trials; reported as the median, p90 and
    max spread over the cell's rows, and how many rows exceed 20 % / 50 %.

D35 rules (docs/dev/measurements/CLAUDE.md): stable name, verbatim output,
the source header below, NEVER a ranking input (nothing here is a record).

    python3 docs/dev/measurements/probe_gate_shape.py store/records/bounded@0.1/*/*.jsonl
"""
import glob
import json
import os
import statistics
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def header(paths):
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                                capture_output=True, text=True).stdout.strip()
    except OSError:
        commit = "unknown"
    with open("/proc/loadavg") as fh:
        load = fh.read().strip()
    print("== probe_gate_shape.py -- run %s" % time.strftime("%Y-%m-%dT%H:%M:%S%z"))
    print("bench commit %s; records read only; load at run: %s" % (commit, load))
    print("records: %d" % len(paths))
    print()


def peaks_from_raw(raw):
    for line in (raw or "").splitlines():
        if line.startswith("per-second peak busy%"):
            vals = line.split(":", 1)[1].split()
            return [float(v) for v in vals]
    return None


def fmt(v):
    return "n/a" if v is None else "%.2f" % v


def one(path):
    with open(path) as fh:
        setup = json.loads(fh.readline())
        rows = [json.loads(l) for l in fh]
    env = setup["environment"]
    occ = env["occupancy"]
    limit = occ.get("limit_busy_pct", 10.0)
    tool = occ.get("tool", "?")
    print("-- %s" % os.path.basename(path))
    print("   testee %s  status %s  tool '%s'  limit %.2f%%"
          % (setup["testee"].get("testee_id", "?"), setup["status"], tool, limit))
    print("   load1 before/after %.2f / %.2f (%s)"
          % (env["load"]["before"]["load1"], env["load"]["after"]["load1"],
             env["load"]["verdict"]))
    for when in ("before", "after"):
        s = occ[when]
        peaks = peaks_from_raw(s.get("raw"))
        line = "   occupancy %-6s judged %s%% -> %s" % (when, fmt(s.get("max_busy_pct")), s.get("verdict"))
        if peaks:
            first = peaks[0]
            worst = max(peaks)
            line += ("  | per-second peaks %s | old 1-s gate: first-second %s (%.2f%%), any-second %s (%.2f%%)"
                     % (" ".join("%.2f" % p for p in peaks),
                        "fail" if first > limit else "pass", first,
                        "fail" if worst > limit else "pass", worst))
        else:
            line += "  | pre-BD7 instrument: the stamped verdict is the old gate's"
        print(line)
    # trial spread
    per = {}
    for r in rows:
        if r.get("kind") != "match" or not r.get("timing"):
            continue
        t = r["timing"]
        if t["iterations"] <= 1:
            continue
        key = (r["pattern_id"], r["regime"], r["subject_id"])
        per.setdefault(key, []).append(t["elapsed_ns"] / t["iterations"])
    spreads = []
    for key, vals in per.items():
        if len(vals) < 2:
            continue
        med = statistics.median(vals)
        if med > 0:
            spreads.append((max(vals) - min(vals)) / med * 100.0)
    if spreads:
        spreads.sort()
        n = len(spreads)
        p90 = spreads[min(n - 1, int(round(0.9 * (n - 1))))]
        print("   trial spread over %d rows (%.0f trials/row): median %.1f%%  p90 %.1f%%  max %.1f%%  rows >20%%: %d  >50%%: %d"
              % (n, statistics.mean(len(v) for v in per.values()),
                 statistics.median(spreads), p90, spreads[-1],
                 sum(1 for s in spreads if s > 20), sum(1 for s in spreads if s > 50)))
    else:
        print("   trial spread: no timed rows")
    print()


def main(argv):
    paths = []
    for a in argv or ["store/records/bounded@0.1/*/*.jsonl"]:
        paths.extend(sorted(glob.glob(a)))
    header(paths)
    for p in paths:
        one(p)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
