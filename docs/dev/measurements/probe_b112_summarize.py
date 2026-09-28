#!/usr/bin/env python3
"""summarize_b112.py -- [B112] I-116 diagnostic: derives the summary table
at the bottom of docs/dev/measurements/2026-09-28-b112-bimodality-diagnostic.txt
from its own verbatim blocks. Numbers only (D35's rule 2): a launch is
classed SLOW if its best_us > 1.5x the minimum best_us seen for the same
(section, variant, subject) group; reports counts and, where the probe
printed freq0_khz, the mean freq for the fast vs slow class.
Usage: summarize_b112.py FILE [FILE...]
"""
import re, sys, statistics as st
from collections import defaultdict

BEST_RE = re.compile(r'best_us=([\d.]+)')
FREQ_RE = re.compile(r'freq0_khz=(-?\d+)')
CPU_RE = re.compile(r'cpu0=(\d+)')

def classify_file(lines, label):
    groups = defaultdict(list)  # key -> list of (best_us, freq0, cpu0, raw_line)
    for line in lines:
        m = BEST_RE.search(line)
        if not m or not line.strip():
            continue
        best = float(m.group(1))
        fm = FREQ_RE.search(line)
        freq = int(fm.group(1)) if fm else None
        cm = CPU_RE.search(line)
        cpu = int(cm.group(1)) if cm else None
        # group key: everything before the first '=' after the launch tag,
        # i.e. the leading label tokens (mode/variant/subject columns).
        key = tuple(line.split()[:4])
        groups[key].append((best, freq, cpu, line))
    print(f"--- {label} ---")
    for key, vals in groups.items():
        bests = [v[0] for v in vals]
        lo = min(bests)
        thr = 1.5 * lo
        slow = [v for v in vals if v[0] > thr]
        fast = [v for v in vals if v[0] <= thr]
        freqs_slow = [v[1] for v in slow if v[1] is not None and v[1] > 0]
        freqs_fast = [v[1] for v in fast if v[1] is not None and v[1] > 0]
        cpus = sorted(set(v[2] for v in vals if v[2] is not None))
        line = (f"{' '.join(key):<28} n={len(vals):<3} slow={len(slow):<3} "
                f"({100.0*len(slow)/len(vals):5.1f}%) min={lo:.3f} "
                f"slow_med={st.median([v[0] for v in slow]) if slow else float('nan'):.3f}")
        if freqs_fast or freqs_slow:
            line += (f" freq0_fast_mean_khz={st.mean(freqs_fast) if freqs_fast else float('nan'):.0f}"
                      f" freq0_slow_mean_khz={st.mean(freqs_slow) if freqs_slow else float('nan'):.0f}")
        if cpus:
            line += f" cpus_seen={cpus}"
        print(line)
    print()

def main(argv):
    for path in argv[1:]:
        with open(path) as f:
            lines = f.readlines()
        classify_file(lines, path)

if __name__ == "__main__":
    main(sys.argv)
