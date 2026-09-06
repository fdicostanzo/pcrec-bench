#!/usr/bin/env python3
"""gen_expectations.py -- `expectations.tsv` for the syntax census, from the
libpcre2 oracle (method `libpcre2-differential`, requirements 5).

The derivation itself is `pcrecbench/expectations.py` -- the sub-bench
contract's chain, shared, not copied (see that module's header). This script
is the entry point and the place the sub-bench's own directory is named.

90 patterns x (42 match + 42 search_short + 3 throughput) subject slots.

CAPTURES PARTICIPATE HERE, ON PURPOSE. The shared derivation prints a NOTE
per pattern whose capture groups participated in a match; in this set that
is every backreference, recursion, named-group and conditional pattern --
the construct under census IS the capture -- so the NOTES are expected and
the span stays the recorded answer (capture correspondence is requirements
12's OD-B9, unchanged). The derivation is seconds: the throughput texts are
1.3 MB in total and nothing here is a backtracking hazard.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

from pcrecbench.expectations import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main(HERE, doc=__doc__.splitlines()[0]))
