"""capture_class.py -- [B82] (inbox I-99/I-100/I-101): THE CAPTURE-CLASS
DECLARATION TABLE, report-time authority for "does this testee's timed
call assign per-group captures".

Frank's ruling (I-99, a D119 addendum on pcrec's side): "compare
capturing vs capturing and non-capturing vs non-capturing engine runs.
If an engine is run non-capturing on a pattern, then we can't compare
that to a capturing engine run -- they are almost completely different
things with different objectives." `pcrecbench/report.py`'s reporter
reads this module to render the two CLASS-PURE views and the standing
cross-class query; nothing here changes the record schema, the
harness, or any adapter -- this module works over ALREADY-COMMITTED
records by reading their `testee_id` alone.

WHY A TABLE, AND WHY IT DOES NOT TRUST `testee.captures` (the record's
own on/off field). Every adapter already derives its testee_id's
`-caps-`/`-nocaps-` token from that very field
(`schema/validate.py:derive_testee_id`), and for every config on the
roster BUT ONE the token already IS the run fact: libpcre2-dfa and
vectorscan declare `captures=off` because their engine genuinely cannot
assign one; every pcrec config, re2 config, oniguruma and tre config
declare `captures=on` and genuinely assign one on every call. The one
exception -- I-99's own finding -- is `rust-default`: its timed loop is
`find_at`-driven (no per-match capture assignment) with exactly ONE
`captures_at` call on the first match, for verification only, yet its
config declares `captures=on` (so its id says `-caps-`) because that is
what the *engine* is configured to do, not what the *timed call* does.
I-100's ruling: classify it NO for the views, DECLARE the one
`captures_at` as a fixed per-call cost, and NEVER rename the store id
to fix the mismatch (a store id is a record's identity; a rename severs
its history) -- "the table, not the id, is the authority for the
views". So this module is a TABLE, keyed on the pin-independent CONFIG
IDENTITY every testee_id encodes (`engine_name`, `engine_mode`, the
derived `caps`/`nocaps` token), each row an explicit `CaptureDeclaration`
that the roster's real facts back up. Nothing here infers a class from
a token it has not been told to trust for that exact (engine, mode,
caps-token) triple.

FAIL-LOUD ON THE UNKNOWN (I-99: "anything you cannot classify is a
question for us, not a guess"). `classify_testee` never falls back to
"trust the id" for a triple this table does not carry a row for -- it
returns `UNDECLARED`, and every caller (the two class-pure views, the
cross-class query, the matrix page) excludes an UNDECLARED testee from
every classified view rather than guessing. A new engine/mode/roster
config is invisible to the class-pure machinery until a row is added
here BY NAME.
"""

from collections import namedtuple

# ------------------------------------------------------------- the tuple

CaptureDeclaration = namedtuple(
    "CaptureDeclaration", ["captures_run", "how_told", "citation"])

ClassResult = namedtuple("ClassResult", ["bucket", "declaration", "identity"])

YES = "yes"
NO = "no"
UNDECLARED = "undeclared"


# ----------------------------------------------------- the config identity

def config_identity(testee_id):
    """(engine_name, engine_mode, caps_token) from a CONSTRUCTED
    testee_id, run BACKWARDS through `schema/validate.py:derive_testee_id`
    (`<engine>_<version>_<mode>-<caps|nocaps>-<simd>[_<extra>]`).

    This is the table's KEY rather than the testee_id verbatim on
    purpose: `engine_mode` + the derived caps token identify a CONFIG
    regardless of pin, `cc`, a raised size cap, a deny flag or any other
    `config_extra` axis (testees/pcrec/CLAUDE.md's "Composition with
    cc" et al. -- none of those axes moves `engine_mode` or `captures`),
    so a table keyed here does not go stale at every re-pin the way one
    keyed on the full testee_id would (I-100 (3): store ids are never
    renamed, and are not stable across pins either).

    Returns `None` for a testee_id that does not split into exactly
    three underscore-separated segments (mirrors
    `report.py:_parse_testee_config`), or whose config segment's
    second-to-last `-`-separated token is not `caps`/`nocaps` (mirrors
    `report.py:_engine_mode_from_testee`'s trailing-pair strip,
    generalised to every engine -- every adapter's `describe()` derives
    through the same `derive_testee_id`, so the shape is universal, not
    pcrec-specific)."""
    base = testee_id.split("@", 1)[0]
    parts = base.split("_", 2)
    if len(parts) != 3:
        return None
    engine_name, _version, config_slug = parts
    base_config = config_slug.split("_", 1)[0]  # drop config_extra, if any
    tail = base_config.split("-")
    if len(tail) < 2 or tail[-2] not in ("caps", "nocaps"):
        return None
    mode = "-".join(tail[:-2])
    if not mode:
        return None
    caps_token = tail[-2]
    return engine_name, mode, caps_token


# ------------------------------------------------------- the declaration table
#
# One row per (engine_name, engine_mode, caps_token) triple this project's
# roster is known to produce (testees/CLAUDE.md's roster table, and each
# engine's own configs.toml). `engine_mode` here is the CONFIG's mode,
# never the record's runtime engine SELECTION (`engine_metadata.engine`,
# e.g. pcrec `auto` choosing `dfa` or `vm` per pattern) -- a config's
# capture-run fact does not change with what `auto` picked.
#
# `pcrec-nocaps` and `pcrec-auto` collide in `engine_mode` ("auto") but
# not in `caps_token` ("nocaps" vs "caps"), which is exactly why the
# caps token is part of the key and not merely a cross-check on it.

DECLARED = {
    # -- libpcre2 (testees/pcre2/) --
    ("libpcre2", "interp", "caps"): CaptureDeclaration(
        YES, "pcre2_match(); the ovector is assigned every call",
        "I-99 ack classification table"),
    ("libpcre2", "jit", "caps"): CaptureDeclaration(
        YES, "pcre2_match() (JIT-compiled); the ovector is assigned every call",
        "I-99 ack classification table"),
    ("libpcre2", "dfa", "nocaps"): CaptureDeclaration(
        NO, "pcre2_dfa_match() cannot assign per-group captures at all "
            "(driver.c's own header comment)",
        "I-99 ack classification table"),

    # -- re2 (testees/re2/) --
    ("re2", "default", "caps"): CaptureDeclaration(
        YES, "driver.cc Match(..., submatch.data(), nsub) with nsub > 0 "
             "on every timed call",
        "I-99 ack classification table"),
    ("re2", "longest", "caps"): CaptureDeclaration(
        YES, "the same Match() call, under set_longest_match(true)",
        "I-99 ack classification table"),

    # -- oniguruma (testees/onig/) --
    ("oniguruma", "default", "caps"): CaptureDeclaration(
        YES, "onig_search() with a region argument, populated every call",
        "I-99 ack classification table"),

    # -- tre (testees/tre/) --
    ("tre", "default", "caps"): CaptureDeclaration(
        YES, "tre_regnexecb() with a pmatch array (emit_caps)",
        "I-99 ack classification table"),

    # -- vectorscan (testees/vectorscan/) --
    ("vectorscan", "block-nosom", "nocaps"): CaptureDeclaration(
        NO, "boolean grain by charter (Frank's Q3 ruling) -- Hyperscan "
            "has no capturing groups at all",
        "I-99 ack classification table"),

    # -- rust (testees/rust/) -- THE ONE OVERRIDE, I-100's ruling
    ("rust", "default", "caps"): CaptureDeclaration(
        NO,
        "the timed loop is find_at-driven (no per-match capture "
        "assignment) with exactly ONE captures_at call on the FIRST "
        "match per timed call, for verification only -- a DECLARED "
        "fixed per-call cost, never a per-match capture assignment "
        "(src/main.rs:255-266); the config's own `captures=on` (its id "
        "says `-caps-`) names the engine's capability, not this run's "
        "behaviour",
        "I-99 (rust-default QUESTION) / I-100 RULING (2): retires once "
        "rust-find (NO) / rust-captures (YES) land as separate configs"),

    # -- pcrec (testees/pcrec/) -- every config's `captures` field is the
    # run fact as-is; the roster's SIXTEEN pinned configs collapse to the
    # THREE distinct (engine_mode, caps_token) pairs below (the `cc`,
    # size-cap, deny-flag and cflags axes never move engine_mode/captures
    # -- testees/pcrec/CLAUDE.md's per-axis "ONE VARIABLE" sections).
    ("pcrec", "auto", "caps"): CaptureDeclaration(
        YES, "the config's own captures=on (record_schema.md 6.4's "
             "derived -caps- token)",
        "I-99 ack classification table"),
    ("pcrec", "auto", "nocaps"): CaptureDeclaration(
        NO, "the config's own captures=off (--no-captures on pcrec's argv)",
        "I-99 ack classification table"),
    ("pcrec", "vm", "caps"): CaptureDeclaration(
        YES, "the config's own captures=on",
        "I-99 ack classification table"),
    ("pcrec", "auto-in", "caps"): CaptureDeclaration(
        YES, "the config's own captures=on (the caller-provided frame "
             "buffer axis does not touch captures)",
        "I-99 ack classification table"),
    ("pcrec", "vm-in", "caps"): CaptureDeclaration(
        YES, "the config's own captures=on",
        "I-99 ack classification table"),
}


def classify_testee(testee_id):
    """The report-time classification of `testee_id`: a `ClassResult`
    whose `.bucket` is `YES`, `NO` or `UNDECLARED` (I-99's fail-loud
    rule -- an id this table has no row for is NEVER guessed at), whose
    `.declaration` is the matching `CaptureDeclaration` or `None`, and
    whose `.identity` is the `config_identity()` tuple or `None`."""
    identity = config_identity(testee_id)
    if identity is None:
        return ClassResult(UNDECLARED, None, None)
    decl = DECLARED.get(identity)
    if decl is None:
        return ClassResult(UNDECLARED, None, identity)
    return ClassResult(decl.captures_run, decl, identity)


def is_override(testee_id):
    """True iff `testee_id`'s OWN `-caps-`/`-nocaps-` token (the record
    schema's `captures` field, derived into the id by every adapter)
    DISAGREES with this table's declared `captures_run` -- today, only
    `rust-default` (I-100 ruling (2)). Callers use this to decide
    whether a declaration needs to be stated VISIBLY next to a testee's
    row (design constraint: "render that declaration visibly wherever
    rust-default appears in a view") -- a config whose id and table
    agree needs no such note; one that disagrees would otherwise read
    as a silent surprise ("why is a `-caps-` id in the non-capturing
    view?"). `False` for an undeclared testee (nothing to compare the
    id against)."""
    identity = config_identity(testee_id)
    if identity is None:
        return False
    decl = DECLARED.get(identity)
    if decl is None:
        return False
    _engine, _mode, caps_token = identity
    id_says = YES if caps_token == "caps" else NO
    return id_says != decl.captures_run


def declaration_table_rows():
    """Every declared row, sorted, for a rendered census (e.g. an ack or
    a design note) -- (engine_name, engine_mode, caps_token,
    captures_run, how_told, citation)."""
    return sorted(
        (engine, mode, caps, decl.captures_run, decl.how_told, decl.citation)
        for (engine, mode, caps), decl in DECLARED.items()
    )
