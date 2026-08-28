"""periodic.py -- the smallest-period fact for a subject's bytes (I-10, [B17]).

pcrecdev1's I-10 finding: the three original 1 MB throughput subjects are
PERIODIC (constant-length repeating blocks), which makes a DFA loop's one
data-dependent branch perfectly history-predictable and flatters any
per-byte number measured on them. The fix is TWO-PART: (1) add non-periodic
subjects beside the periodic ones (gen_throughput_subjects.py's t-d/t-e),
(2) record the fact mechanically for every subject so a reader can tell
which is which without re-deriving it -- this module is that mechanism,
shared by both generators (gen_subjects.py, gen_throughput_subjects.py) so
the definition of "period" is the SAME wherever it appears in a manifest.

MOVED HERE FROM `bench/email/` when the second sub-bench landed ([B11.1]).
It began as one sub-bench's helper and is now the definition of a MANIFEST
COLUMN that every sub-bench writes, so it belongs to the harness package:
`bench/loglines/logtext.py` imports it too, and "the same column name and
semantics" is then a fact about the code rather than a claim in two NOTES
files that could drift apart.

Definition (I-10's own words): the smallest p, 1 <= p <= MAX_PERIOD, such
that s[i] == s[i+p] for every i in range(len(s) - p). `no` (this module
returns None) means no such p exists in that range -- NOT that the subject
is provably aperiodic for all p, only that it has none up to MAX_PERIOD,
which is the range I-10 asked for and large enough that a subject built
from a hand-written repeating unit (the three original throughput
subjects: 26, 55, 1 byte periods) is always caught.
"""

MAX_PERIOD = 4096


def smallest_period(data, max_period=MAX_PERIOD):
    """The smallest p in [1, max_period] with data[i] == data[i+p] for all
    valid i, or None if none exists. O(len(data) * candidates-tried); bytes
    slicing comparison is a C-level memcmp, so this is fast in practice --
    periodic data is confirmed by one full-length compare at the true
    period, aperiodic data is refuted for MOST candidates by an early
    mismatch within the first few bytes."""
    n = len(data)
    if n < 2:
        return None
    upper = min(max_period, n - 1)
    for p in range(1, upper + 1):
        if data[:-p] == data[p:]:
            return p
    return None


def periodic_field(data, max_period=MAX_PERIOD):
    """The manifest column value: the period as a decimal string, or the
    literal `no`."""
    p = smallest_period(data, max_period)
    return "no" if p is None else str(p)
