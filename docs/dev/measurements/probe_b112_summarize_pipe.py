#!/usr/bin/env python3
"""summarize_pipe.py -- companion to summarize_b112.py for the OTHER printf
format used by run_diag.sh's sections 0/1/2 and 3e/3f: one line per CELL,
"<label...> min=.. med=.. max=.. | v1 v2 v3 ...". Classifies each v_i as
slow if > 1.5x the cell's own minimum.
"""
import re, sys, statistics as st

def main(argv):
    for path in argv[1:]:
        print(f"--- {path} ---")
        with open(path) as f:
            for line in f:
                if '|' not in line or 'min=' not in line:
                    continue
                label, rest = line.split('|', 1)
                vals = [float(x) for x in rest.split()]
                if not vals:
                    continue
                lo = min(vals)
                thr = 1.5 * lo
                slow = [v for v in vals if v > thr]
                pct = 100.0 * len(slow) / len(vals)
                slowstr = f"slow_med={st.median(slow):.3f}" if slow else "slow_med=n/a"
                print(f"{label.strip():<45} n={len(vals):<3} slow={len(slow):<3} ({pct:5.1f}%) min={lo:.3f} {slowstr}")
        print()

if __name__ == "__main__":
    main(sys.argv)
