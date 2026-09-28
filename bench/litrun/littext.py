"""littext.py -- the literal-run sub-bench's one shared module: the L-sweep's
alphabet and length ladder (kept in exactly one place so `gen_patterns.py`,
`gen_subjects.py`, `gen_throughput_subjects.py` and `gen_pattern_facts.py`
can never disagree about what `lit-l<L>`'s literal text is), and
`pcrecbench.periodic`'s re-export (the manifest `periodic` column's one
definition, shared with every other sub-bench -- bench/loglines/logtext.py's
precedent).

NO RANDOMNESS PRIMITIVE. Unlike every other generator sub-bench under
`bench/`, this module carries no `Rng`: every pattern and every subject here
is an explicit, named, deterministic construction (`gen_patterns.py`'s own
header explains why), so there is nothing a seeded draw would do that a
constant would not do more legibly.
"""
import os
import string
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench.periodic import periodic_field  # noqa: F401,E402

# The SAME alphabet and length ladder `gen_patterns.py` builds `lit-l<L>`
# from -- imported, not retyped, so the two files cannot drift.
ALPHABET = (string.ascii_lowercase + string.ascii_uppercase).encode("ascii")
L_SWEEP = (2, 3, 4, 7, 8, 10, 16, 31, 40)

# The floor byte (`gen_patterns.py`'s `floor.rx`), used here as the ONE
# guard byte the L-sweep's near-miss units are built from -- imported so a
# future edit to the floor pattern cannot silently desync the two.
FLOOR_BYTE = b"#"


def literal(length):
    """The `lit-l<length>` pattern's own literal text: the first `length`
    bytes of ALPHABET. `length` must be <= len(ALPHABET) (52) for the
    no-internal-repeat property `gen_patterns.py` asserts to hold."""
    if length > len(ALPHABET):
        raise ValueError("length %d exceeds the %d-byte alphabet"
                          % (length, len(ALPHABET)))
    return bytes(ALPHABET[:length])


# ---- the L-sweep's three throughput UNIT shapes (S7.2) --------------------
#
# Each is exactly `length` bytes; `gen_throughput_subjects.py` tiles one of
# these back-to-back to build a dense subject. The proof that tiling any of
# these three units produces EXACTLY the intended match/mismatch behaviour
# at every window offset (aligned or not) is in that file's own docstring.

def unit_match(length):
    """The literal itself -- every aligned window is a full match."""
    return literal(length)


def unit_first_byte_flip(length):
    """The literal's own tail (bytes 1..length-1) with byte 0 replaced by
    the floor byte -- every window (aligned or not) fails to match, and an
    ALIGNED window fails at the very first byte compared."""
    lit = literal(length)
    return FLOOR_BYTE + lit[1:]


def unit_last_byte_flip(length):
    """The literal's own head (bytes 0..length-2) with the last byte
    replaced by the floor byte -- every window fails to match, and an
    ALIGNED window matches length-1 bytes before failing on the last."""
    lit = literal(length)
    return lit[:-1] + FLOOR_BYTE
