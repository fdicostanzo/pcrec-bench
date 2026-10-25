"""THE ONE PROGRAM-IDENTITY CHOOSER ([B145], BD13 amendment).

A pcrec compile row carries up to two program hashes in its
`engine_metadata`:

  * `program_sha256`    -- normalization v2 ([B88], schema 1.7). Its meaning
                           is fixed forever; it is never recomputed.
  * `program_sha256_v3` -- normalization v3 ([B145], schema 1.10): v2 plus
                           the find-all scaffold and forwarder/twin pairs
                           folded away (tools/program_identity.py
                           `normalize_v3`), so it reads "the same program"
                           across the abi 77-84 emission changes.

EVERY comparison of two compile rows' program identity -- the reporter's
null band, the trend report, the viewer, the front page -- goes through
`same_program`, and through nothing else. The rule is the whole module:

  both sides carry v3  -> compare v3, criterion "v3"
  else both carry v2   -> compare v2, criterion "v2"
  else                 -> verdict "unknown", criterion "none"

A v2 hash is NEVER compared with a v3 hash. A side that carries v3 only
because the other side does not is compared by v2 (both v2 exist for every
pcrec row since 1.7). `tools/selfcheck.py check_identity_chooser` fails if a
raw `program_sha256` comparison is written anywhere outside this file.
"""

V2_FIELD = "program_sha256"
V3_FIELD = "program_sha256_v3"

IDENTICAL = "identical"
CHANGED = "changed"
UNKNOWN = "unknown"

CRIT_V3 = "v3"
CRIT_V2 = "v2"
CRIT_NONE = "none"


def _get(meta, field):
    v = (meta or {}).get(field)
    return v if isinstance(v, str) and v else None


def same_program(meta_a, meta_b):
    """-> (verdict, criterion): verdict in identical/changed/unknown,
    criterion in v3/v2/none (none iff unknown)."""
    for field, crit in ((V3_FIELD, CRIT_V3), (V2_FIELD, CRIT_V2)):
        a, b = _get(meta_a, field), _get(meta_b, field)
        if a and b:
            return (IDENTICAL if a == b else CHANGED), crit
    return UNKNOWN, CRIT_NONE


def compared_hashes(meta_a, meta_b):
    """-> (criterion, hash_a, hash_b): the two values `same_program` would
    compare (for DISPLAY next to its verdict); ("none", "", "") when unknown."""
    for field, crit in ((V3_FIELD, CRIT_V3), (V2_FIELD, CRIT_V2)):
        a, b = _get(meta_a, field), _get(meta_b, field)
        if a and b:
            return crit, a, b
    return CRIT_NONE, "", ""


def criterion_summary(criteria):
    """-> "v3" / "v2" / "mixed" / "none" over an iterable of per-comparison
    criteria (unknowns, criterion "none", are ignored unless all are)."""
    seen = {c for c in criteria if c != CRIT_NONE}
    if not seen:
        return CRIT_NONE
    return seen.pop() if len(seen) == 1 else "mixed"
