#!/usr/bin/env python3
"""_diag_worker.py -- ONE PATTERN's oracle derivation, run as its own
process so a wrapping `gnutimeout` can hard-kill it. Prints
`TIMING\\t<pattern>\\t<subject>\\t<regime>\\t<elapsed_ms>` to stdout,
UNBUFFERED, after every (subject, regime) cell -- so the last line seen
before a timeout names the cell in progress when it was killed.
Diagnostic only; not part of the committed generator chain.
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench import oracle_pcre2 as oracle  # noqa: E402
from pcrecbench.subbench import load as load_subbench  # noqa: E402

REGIME_ORDER = ("search_short", "throughput")


def main():
    pattern_id = sys.argv[1]
    sb = load_subbench(HERE)
    pat = next(p for p in sb.patterns if p.name == pattern_id)
    text = sb.pattern_bytes(pat.name)
    t0 = time.time()
    rx = oracle.compile(text)
    print("TIMING\t%s\t<compile>\t<compile>\t%.1f"
          % (pattern_id, (time.time() - t0) * 1000), flush=True)
    for regime in REGIME_ORDER:
        if regime not in sb.regimes:
            continue
        for subj in sb.subjects_for(regime):
            body = sb.subject_bytes(subj.subject_id)
            t0 = time.time()
            try:
                if regime == "search_short":
                    rx.search(body, 0)
                else:
                    rx.find_all(body)
            except oracle.Pcre2Error as e:
                print("TIMING\t%s\t%s\t%s\t%.1f\tGAVEUP:%s"
                      % (pattern_id, subj.subject_id, regime,
                         (time.time() - t0) * 1000, e), flush=True)
                continue
            print("TIMING\t%s\t%s\t%s\t%.1f"
                  % (pattern_id, subj.subject_id, regime,
                     (time.time() - t0) * 1000), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
