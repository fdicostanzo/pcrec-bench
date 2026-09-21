#!/usr/bin/env python3
"""tools/viewer_export.py -- [B66] the results viewer's data exporter.

`docs/design/results_viewer_v1.md` 2: walks `store/index.tsv`, loads each
set's newest record per (testee_id, machine) -- plus every older PIN's own
newest record too under `--all-pins` -- and reduces to SET GRAIN by calling
the SAME `pcrecbench.reduce` functions the reporter calls
(`reduce_set_cell`, `cells_from_record`), so a viewer cell equals the
committed report cell byte-for-value. It never reimplements a median.

MEMORY (docs/dev/lanes/BOILERPLATE.md, this lane's brief): one record is
loaded, reduced and discarded before the next is opened -- never the whole
store at once (the reporter's own whole-store load is ~3.6 GB at 160
records, KB-16). This module never calls `pcrecbench.report.build_report`
for exactly that reason: `build_report` accumulates every selected record's
RAW rows across the whole query before reducing anything (see its own
`match_rows_by_key`/`set_rows_by_key` accumulators), which is the right
shape for a query that must compare many records against each other at
once but the wrong one for an exporter that can reduce one record at a
time and keep only the numbers. The record-DEDUP step below (which testee
identity's newest record to open at all) is answered from `index.tsv`
alone -- no record file is opened to make that decision.

WHICH RECORDS ARE INCLUDED (mirrors `report.py`'s R2/OD-B15 dedup, and
`reports/CLAUDE.md`'s [B61] canonical-identity convention):

  1. Per (subbench@version, testee_id, machine_id): the newest record with
     `status == measured`, or (if none is measured) the newest record
     overall. Exactly `build_report`'s own rule, computed here from
     `index.tsv`'s own `timestamp`/`status` columns without opening a file.
  2. Default (no `--all-pins`): a further collapse across PINS of the same
     CANONICAL identity -- `(engine_name, config_slug)` parsed from
     `testee_id` (`<engine>_<version>_<config>`, the same split
     `report.py`'s `_parse_testee_config` uses) -- keeping only the
     newest-timestamped pin. `--all-pins` skips this collapse: every
     distinct testee_id (and therefore every pin) that survives step 1
     becomes its own column.

PATTERN TEXT ([B67] 9.8): each set's payload also carries `patterns`, a
`{pattern_id: {text, omitted, truncated, full_bytes}}` map -- ONE entry
per pattern (factored out of the per-row data; a pattern's text is
invariant across every row that shares it). `text` is the record's own
`patterns[].canonical_text` (record_schema.md), truncated to
`PATTERN_TEXT_MAX_BYTES` (~2 KB) with `truncated`/`full_bytes` naming
the cut honestly; `omitted` is true when the RECORD itself carries no
`canonical_text` at all (the schema's own free_text-cap fallback, KB-7 --
`full_bytes` is `None` in that case, since nothing anywhere states the
true length of an omitted field). First record processed for a set wins
each pattern_id (canonical per sub-bench, so every record that reaches
it should agree).

STATUS PER ROW, in priority order (design note 2's vocabulary: measured |
refused | unsup | wrong | gave-up | timed-out | inconclusive-*):

  1. the RECORD's own status, when not `measured` (inconclusive-load,
     inconclusive-spread, harness-failure) -- no numbers on such a row,
     the standing "statuses other than measured are never ranked" rule.
  2. a compile-row outcome `did-not-compile` -> `refused`,
     `unsupported-by-declaration` -> `unsup` (report.py's own
     `did_not_compile_by_pattern`/`unsupported_by_pattern` logic, applied
     per record); `crashed`/`timed-out` at compile time pass through by
     name. One row per (pattern, form) is built here with regime empty
     (mirrors [B52]'s F26 shape for a pattern that never reached a
     regime); `_fold_and_classify` (below, [B70] `results_viewer_v1.md`
     10) then FOLDS it into every regime this SET's rows actually carry
     for that (pattern, form) -- the blank-regime row survives only in
     the true F26 case, no regime anywhere -- and, for `refused` rows,
     attaches `refusal_reason` (one of `REFUSAL_REASON_TOKENS`,
     `wrap-artifact` decided structurally, everything else from the
     diagnostic text).
  3. a match SetCell that fails its own expectation
     (`SetCellReduction.expectation_failing`): `wrong` if any subject's
     answer disagreed, else `gave-up` if any subject gave up, else the
     dominant hazard outcome found in the failing subjects' own
     `MatchCellReduction.outcome_counts` (`timed-out` / `crashed`), else
     `excluded` (no timed trials at all).
  4. otherwise `measured`, carrying `median_ns`/`spread_lo_ns`/
     `spread_hi_ns`/`n_subjects`/`subject_bytes_total`.

Run: `python3 tools/viewer_export.py` (== `make viewer-data`); `--sets
loglines,email-specimen` narrows to a slice for development (the design
note's data files are independent per set, so a partial export is a
partial `viewer/data/` -- never a corrupt one: files this run does not
touch are left as they are, and `manifest.js` lists only the sets it
actually wrote this run plus whatever the CALLER says to keep, via
`--keep-existing-manifest`, for a slice run that must not blank out the
other sets' manifest entries).
"""

import argparse
import csv
import json
import os
import re
import sys
import tempfile
from collections import defaultdict
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from pcrecbench.report import _get_record_validator, load_record  # noqa: E402
from pcrecbench.reduce import (  # noqa: E402
    cells_from_record,
    reduce_set_cell,
)
from pcrecbench.record import FORM_WHOLE_SUBJECT  # noqa: E402

DEFAULT_STORE = os.path.join(ROOT, "store")
DEFAULT_OUT = os.path.join(ROOT, "viewer", "data")

# record.schema.json $defs/record_status: the non-"measured" tokens a
# whole RECORD can carry (never a per-cell number).
_NON_MEASURED_RECORD_STATUS = {"harness-failure", "inconclusive-load", "inconclusive-spread"}

# record.schema.json $defs/compile_outcome, mapped to the viewer's own
# status vocabulary (design note 2): `did-not-compile` reads oddly as a
# per-cell status word, so it renders as `refused` (what a reader calls a
# testee that would not build this pattern at all); `unsupported-by-
# declaration` as `unsup` ([B42] L5's own advance-declaration fact, never
# an engine failure); `crashed`/`timed-out` pass through by name, same as
# a match-row hazard outcome.
_COMPILE_STATUS = {
    "did-not-compile": "refused",
    "unsupported-by-declaration": "unsup",
    "crashed": "crashed",
    "timed-out": "timed-out",
}

# The sink order a non-measured row falls to (design note 4's own list,
# and the viewer's sort rule): worse findings sink further. `viewer.html`
# reads this same order out of the exported meta so the two never drift.
STATUS_SINK_ORDER = ["measured", "wrong", "refused", "unsup", "gave-up",
                      "timed-out", "crashed", "inconclusive-load",
                      "inconclusive-spread", "harness-failure", "excluded"]


# ---------------------------------------------------- [B70] 10.2/10.3: refusals

# The CLOSED refusal-reason token set, §10.2's "first cut", seeded from
# `docs/dev/measurements/2026-09-21-capability-refusal-census.txt` (the
# [B69] census) plus two prior, already-committed, MEASURED diagnostics
# this project has stated elsewhere by name (cited per rule below) --
# never invented ahead of a real diagnostic. `wrap-artifact` is NOT a
# text rule at all: it is decided STRUCTURALLY, in `_fold_and_classify`,
# before any diagnostic is read (see that function's docstring). `other`
# is the honest fallback -- a diagnostic this set has not measured yet,
# not a dumping ground for one this set HAS measured and a rule missed.
REFUSAL_REASON_TOKENS = ("too-large", "too-complex", "syntax", "unsupported",
                          "wrap-artifact", "other")

_REFUSAL_REASON_RULES = [
    # Seed: the census, `wild-datetime-datefinder-alternation`, all four
    # `pcrec_25b1984f` configs (both forms): "pcrec: pattern too large:
    # 670159 bytes of emitted code (limit 500000), which gcc cannot
    # compile in reasonable time. ..." -- pcrec's emitted-CODE-size cap
    # (checked ahead of `too-complex` below: both diagnostics start
    # "pattern too large", this one alone names "bytes of emitted code").
    ("too-large", re.compile(r"pattern too large:\s*\d+\s*bytes of emitted code")),
    # Seed: NOT in the [B69] census (no capability@0.1 pattern hits this
    # cap) -- from `docs/dev/outbox_to_pcrec.md` O-9 / `testees/pcrec/
    # CLAUDE.md`'s own quoted text, bench/bounded's `cls-upto-65535`
    # rung: "pcrec: pattern too large (NFA exceeds 131072 states) ...".
    # A STATE/ELEMENT cap, distinct from the emitted-size cap above.
    ("too-complex", re.compile(
        r"NFA exceeds \d+ states|state-set elements|subset construction exceeds")),
    # Seed: the census, `mojibake-curly-quote`, `rust_1.13.1`: "pattern is
    # not valid UTF-8 at byte N: ..." -- a structural pattern-SOURCE
    # encoding constraint (rust-regex takes `&str`, never `&[u8]`), not a
    # regex-grammar parse error.
    ("unsupported", re.compile(r"not valid UTF-8")),
    # Seed: the census -- `balanced-parens-rec` / oniguruma ("unmatched
    # close parenthesis"), the CASE-1 wrap patterns' own three non-
    # structural-match diagnostics ("end pattern with unmatched
    # parenthesis", "missing closing ) for group", "Unterminated
    # comment.", "regex parse error:"), and `wild-*` / tre's
    # ("Invalid character range", testees/tre/CLAUDE.md item 4). Every
    # genuine PARSE-time rejection this census measured.
    ("syntax", re.compile(
        r"unmatched (close |)parenthes|missing closing \)|Unterminated comment"
        r"|regex parse error|Invalid character range")),
]


def _classify_refusal_reason(diagnostic):
    """One of `REFUSAL_REASON_TOKENS` (never `wrap-artifact`, which is
    decided structurally, ahead of this call, in `_fold_and_classify`) --
    `other` when no rule's diagnostic-text pattern matches. Extending
    this list is how a FUTURE census finding grows the set; nothing here
    is invented ahead of a diagnostic this project has actually
    measured (see each rule's own seed comment above)."""
    if not diagnostic:
        return "other"
    for token, rx in _REFUSAL_REASON_RULES:
        if rx.search(diagnostic):
            return token
    return "other"


def _fold_and_classify(rows, compiled_by_testee=None):
    """[B70] `docs/design/results_viewer_v1.md` 10, items 1-3: fold every
    compile-refusal/unsup row (`regime == ""`) into the ranked rows, and
    classify every `refused` row's mechanism.

    FOLDING (item 1). A compile refusal or policy decline is
    regime-INDEPENDENT (no artifact -- or no attempt -- exists, so no
    regime ever timed it): report.py's own `render_matrix_tsv` reads
    exactly this fact through `_matrix_cell`'s fallback chain (a
    `did_not_compile_by_pattern`/`unsupported_by_pattern` entry answers
    EVERY regime row for its pattern, never just one) -- this function is
    the SAME rule applied to this module's own per-row shape (this module
    works row-by-row across records, report.py query-wide over a
    `ReportData`, so the rule is reimplemented here, not imported; the
    module docstring's own MEMORY discipline is why -- see `tools/
    CLAUDE.md`). For each (pattern, form) with at least one regime seen
    ANYWHERE in this set's rows, a blank-regime refusal/unsup row is
    replaced by one row per such regime, same testee/status/diagnostic.
    Where NO regime exists anywhere for that (pattern, form) -- every
    testee refused or declined it, `render_matrix_tsv`'s own F26 case
    (`docs/design/predicate_audit_v1.md`) -- the single blank-regime row
    is KEPT, since there is nothing to fold it into.

    CLASSIFICATION (items 2-3). Every `refused` row's mechanism is
    resolved to one of `REFUSAL_REASON_TOKENS`. `wrap-artifact` is
    decided FIRST and STRUCTURALLY, never from diagnostic text: a
    `whole-subject` refusal is `wrap-artifact` iff (a) the SAME testee's
    own `plain` twin of the SAME pattern compiled (any status but
    `refused`/`unsup`), and (b) every OTHER testee that ATTEMPTED (status
    != `unsup`) the SAME (pattern, `whole-subject`) also refused it --
    the [B69] census's own CASE-1-vs-CASE-2 rule (`docs/dev/lanes/
    b69census_report.md` 4-5): "every attempting engine refused" is
    `wrap-artifact`; a split refusal never is. This is per-(testee, row),
    not merely per-(pattern, form): the census's own two CASE-1 patterns
    have a THIRD refusing testee this rule correctly keeps OUT of
    `wrap-artifact` -- `vectorscan-block-nosom`'s `plain` (unwrapped) form
    of both patterns ALSO refuses with the identical "Unterminated
    comment." diagnostic (census raw JSON, testee
    `vectorscan_5.4.11_block-nosom-nocaps-simd`), which this census's own
    §4/§5 did not call out by name -- vectorscan cannot parse either
    pattern's trailing un-newline-terminated `(?x)` comment AT ALL, wrapped
    or not, so its `whole-subject` refusal is not CAUSED by the harness's
    wrapper the way the other six attempters' are: its `plain` twin never
    compiled, condition (a) fails, and it classifies `syntax` from the
    text rule instead -- a finding this lane's report states plainly,
    per the brief's own "if the census table shows a mechanism your
    rules miss, extend the rules, and say so" (the rules already handle
    it correctly; nothing needed EXTENDING, but the divergence from the
    census report's own per-pattern table is real and worth a reader
    knowing). Everything else (including every `wrap-artifact`-eligible
    row that fails the structural test) falls to `_classify_refusal_reason`.

    `compiled_by_testee` ({testee_id: {(pattern_id, form)}}, from
    `export_rows_for_record`'s own `compiled_forms` return) supplies the
    ONE fact `rows` alone cannot: a (pattern, form) this testee compiled
    CLEANLY but which left no row at all (a set-wide regime exclusion
    like `bench/capability@0.1`'s `match` means a clean `whole-subject`
    compile is never matched, so it produces neither a compile-refusal
    row nor a match row). Without it, `attempted`/`plain_compiled` can
    only see testees that left SOME row behind, silently narrowing
    "attempted" to "refused or matched" and turning a genuine SPLIT
    refusal into a false `wrap-artifact` the moment every OTHER
    attempter's success happens to be row-less -- MEASURED live on
    `wild-datetime-datefinder-alternation` before this parameter existed
    (see `export_rows_for_record`'s own docstring for the full account).
    """
    regimes_by_pf = defaultdict(set)
    for r in rows:
        if r["regime"]:
            regimes_by_pf[(r["pattern"], r["form"])].add(r["regime"])

    attempted = defaultdict(set)      # (pattern, form) -> {testee_id}, status != unsup
    refused_by = defaultdict(set)     # (pattern, form) -> {testee_id}, status == refused
    plain_compiled = defaultdict(set)  # pattern -> {testee_id whose plain form is not refused/unsup}
    for r in rows:
        if r["status"] == "unsup":
            continue
        key = (r["pattern"], r["form"])
        attempted[key].add(r["testee_id"])
        if r["status"] == "refused":
            refused_by[key].add(r["testee_id"])
        elif r["form"] == "plain":
            plain_compiled[r["pattern"]].add(r["testee_id"])
    for testee_id, forms in (compiled_by_testee or {}).items():
        for (pattern_id, form) in forms:
            attempted[(pattern_id, form)].add(testee_id)
            if form == "plain":
                plain_compiled[pattern_id].add(testee_id)

    def is_wrap_artifact(row):
        if row["form"] != FORM_WHOLE_SUBJECT:
            return False
        if row["testee_id"] not in plain_compiled.get(row["pattern"], ()):
            return False
        key = (row["pattern"], FORM_WHOLE_SUBJECT)
        atts = attempted.get(key, set())
        return bool(atts) and atts == refused_by.get(key, set())

    out = []
    for r in rows:
        if r["status"] == "refused":
            r["refusal_reason"] = ("wrap-artifact" if is_wrap_artifact(r)
                                     else _classify_refusal_reason(r.get("diagnostic")))
        if r["regime"] == "" and r["status"] in ("refused", "unsup"):
            targets = regimes_by_pf.get((r["pattern"], r["form"]))
            if not targets:
                out.append(r)  # F26 case: no regime exists anywhere for this
                continue        # (pattern, form) -- nothing to fold into
            for regime in sorted(targets):
                folded = dict(r)
                folded["regime"] = regime
                out.append(folded)
            continue
        out.append(r)
    return out


def utcnow_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------- index.tsv

def read_index(store_dir):
    path = os.path.join(store_dir, "index.tsv")
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t")), sum(1 for _ in open(path)) - 1


def parse_testee_id(testee_id):
    """(engine_name, version_slug, config_slug) -- the same three-way split
    `report.py`'s `_parse_testee_config` uses (record_schema.md 6.4), kept
    as a small local copy rather than importing a private, underscore-
    prefixed function from another module. `None` for a testee_id that
    does not split into exactly three `_`-separated segments."""
    base = testee_id.split("@", 1)[0]
    parts = base.split("_", 2)
    if len(parts) != 3:
        return None
    return tuple(parts)


def dedup_newest_per_testee(index_rows):
    """Step 1 of the module docstring's inclusion rule: per (subbench@
    version, testee_id, machine_id), the newest MEASURED index row, or (if
    none is measured) the newest row overall -- `report.py`'s own R2/
    OD-S15 rule, computed here purely from `index.tsv` columns."""
    groups = defaultdict(list)
    for row in index_rows:
        sb = f"{row['subbench']}@{row['version']}"
        key = (sb, row["testee_id"], row["machine_id"])
        groups[key].append(row)
    kept = []
    for _key, entries in groups.items():
        entries.sort(key=lambda r: r["timestamp"])
        measured = [r for r in entries if r["status"] == "measured"]
        kept.append(measured[-1] if measured else entries[-1])
    return kept


def collapse_to_newest_pin(rows):
    """Step 2 (default mode only): collapse across PINS of one canonical
    (engine_name, config_slug) identity, keeping the newest-timestamped
    row -- `reports/CLAUDE.md`'s [B61] rule, generalised past pcrec's own
    ablation testees to every engine (a rust/re2/libpcre2 re-run with a
    changed `engine_version` collapses the identical way)."""
    groups = defaultdict(list)
    for row in rows:
        sb = f"{row['subbench']}@{row['version']}"
        parsed = parse_testee_id(row["testee_id"])
        canon = (row["testee_id"] if parsed is None
                 else (parsed[0], parsed[2]))
        groups[(sb, canon, row["machine_id"])].append(row)
    kept = []
    for _key, entries in groups.items():
        entries.sort(key=lambda r: r["timestamp"])
        kept.append(entries[-1])
    return kept


# ---------------------------------------------------------- per-record cut

def _engine_variant(testee_block):
    """FALLBACK ONLY (a testee_id that does not parse into the standard
    three `_`-separated segments, record_schema.md 6.4) -- see
    `engine_variant_for` below for the real derivation, [B67] 9.1's fix.
    Kept lossy on purpose (mode + config_extra, no captures/simd) since
    it is never reached for a real record; a real one always parses."""
    mode = testee_block.get("engine_mode") or ""
    extra = testee_block.get("config_extra")
    return f"{mode}-{extra}" if extra else mode


def engine_variant_for(testee_id, testee_block):
    """THE testee_id's OWN config identity ([B67] 9.1's root-cause fix).

    `derive_testee_id` (schema/validate.py 175) builds testee_id as
    `<engine>_<version_slug>_<engine_mode>-<caps>-<simd>[_<config_extra>]`
    -- everything after the SECOND underscore (`parse_testee_id`'s third
    segment) is already the engine's own unique configuration identity,
    by construction: two testees with the same engine_mode but different
    captures (`pcrec-auto` engine_mode=auto captures=on vs `pcrec-nocaps`
    engine_mode=auto captures=off) get DIFFERENT config_slugs
    (`auto-caps-simdna` vs `auto-nocaps-simdna`) because `caps` is baked
    into config_slug, not into `config_extra` at all.

    The OLD `_engine_variant()` reconstructed a "variant" label from only
    `engine_mode` + `config_extra`, silently DROPPING the caps/simd
    component -- so `pcrec-auto` and `pcrec-nocaps` (same engine_mode
    "auto", both with no config_extra) BOTH produced the label "auto".
    Two distinct testee_ids sharing one viewer-side "variant" string is
    exactly the bug `viewer.html`'s tree->column code could not survive
    (docs/design/results_viewer_v1.md 9.1): a family-checkbox toggle (or
    any tree leaf) that reconstructs a testee_id from
    (family, variant, pin) finds only ONE of the two real testee_ids for
    that collided label, so the OTHER testee's column never gets
    reachable through the tree at all -- it renders as a same-labelled
    "duplicate" column and, worse, survives a "deselect this family"
    click untouched, which is precisely what Frank saw.

    Using the config_slug segment directly is not just a label fix: it
    is testee_id's OWN identity component, so two testees can never
    collide on it (they would be the SAME testee_id if they did)."""
    parsed = parse_testee_id(testee_id)
    if parsed is None:
        return _engine_variant(testee_block)
    return parsed[2]


# [B67] 9.8: the viewer's own export bound on ONE pattern's canonical
# text, independent of (and much tighter than) the record schema's own
# free_text cap (1,048,576 chars, v1.5/KB-7). The design note states
# "~2 KB" for the popover; this is where that number lives. A pattern
# longer than this is TRUNCATED here, on a byte boundary, with the
# viewer told the TRUE original length so it can render "truncated,
# full N bytes" honestly rather than silently.
PATTERN_TEXT_MAX_BYTES = 2000


def _pattern_text_entry(canonical_text):
    """-> {"text", "omitted", "truncated", "full_bytes"} for one pattern's
    `canonical_text` (record_schema.md's `patterns[].canonical_text`,
    OPTIONAL -- a record may OMIT it under the schema's own free_text cap,
    KB-7's fallback; `full_bytes` is `None` in exactly that case, since an
    omitted field carries no length to report -- there is no second field
    anywhere in the schema that would give us one). `canonical_text is
    None` is the omission case; anything else is a real (possibly empty)
    string this bench further truncates to `PATTERN_TEXT_MAX_BYTES`."""
    if canonical_text is None:
        return {"text": None, "omitted": True, "truncated": False, "full_bytes": None}
    encoded = canonical_text.encode("utf-8")
    full_bytes = len(encoded)
    if full_bytes <= PATTERN_TEXT_MAX_BYTES:
        return {"text": canonical_text, "omitted": False, "truncated": False,
                "full_bytes": full_bytes}
    # Cut on a byte boundary (patterns are typically ASCII regex syntax,
    # but never assume it) -- errors="ignore" silently drops a partial
    # trailing multi-byte character rather than raising or corrupting the
    # cut; the `truncated`/`full_bytes` pair is what keeps this honest,
    # not the decode itself.
    truncated_text = encoded[:PATTERN_TEXT_MAX_BYTES].decode("utf-8", errors="ignore")
    return {"text": truncated_text, "omitted": False, "truncated": True,
            "full_bytes": full_bytes}


def _failing_kind(red):
    """The dominant status word for one FAILING SetCellReduction (its own
    `expectation_failing` already True): `wrong` ahead of `gave-up` (a
    wrong answer is the stronger finding when a cell somehow carries
    both, same order `_matrix_cell` uses), else the dominant hazard
    outcome found among the failing subjects' own MatchCellReduction
    outcome_counts, else `excluded` (no timed trial at all -- `n_trials
    == 0` on every failing subject)."""
    if red.n_wrong:
        return "wrong"
    if red.n_gave_up:
        return "gave-up"
    hazard_counts = defaultdict(int)
    for sub_red in red.failing_detail.values():
        for outcome in ("timed-out", "crashed"):
            hazard_counts[outcome] += sub_red.outcome_counts.get(outcome, 0)
    if hazard_counts.get("timed-out"):
        return "timed-out"
    if hazard_counts.get("crashed"):
        return "crashed"
    return "excluded"


def export_rows_for_record(path, rv):
    """Load ONE record (`report.load_record`, the reporter's own loader:
    JSON parse + schema validation in one pass), reduce it, and return
    (rows, patterns_meta, compiled_forms) -- then the caller drops
    `loaded`/`rows` before opening the next file. `patterns_meta` is
    `{pattern_id: _pattern_text_entry(...)}` for every pattern this ONE
    record's own `setup.patterns[]` declares ([B67] 9.8) -- small (a
    handful of strings, each capped at PATTERN_TEXT_MAX_BYTES), so it is
    fine for this little a fragment to survive past this call the same
    way `rows` already does; the record's raw `rec.rows`/`rec.setup`
    themselves still do not.

    `compiled_forms` ([B70], the wrap-artifact structural detector's own
    need): `{(pattern_id, form)}` for every compile row this record
    carries with outcome `compiled` -- a fact `rows` alone CANNOT answer.
    `bench/capability@0.1` excludes the `match` regime SET-WIDE
    (`docs/design/capability_set_v1.md` 3.5), so a testee whose
    `whole-subject` artifact compiled CLEANLY but was never matched
    against (oniguruma/rust/vectorscan on most patterns) leaves ZERO
    trace anywhere in `rows` -- no compile row (only refusals are kept
    there) and no match row (the regime never ran). Without this set,
    `_fold_and_classify`'s "every ATTEMPTING testee refused" unanimity
    test can only see testees that left SOME row behind, which silently
    narrows "attempted" to "refused or matched" -- confirmed live on
    `wild-datetime-datefinder-alternation`'s `whole-subject` form: three
    of its five genuine attempters (oniguruma, rust, vectorscan) compile
    it fine and are invisible to a `rows`-only read, so a `rows`-only
    unanimity check misclassifies the pcrec/tre split refusal as
    `wrap-artifact` -- caught in this lane's own real-data verification,
    not a hypothetical.

    Returns `([], {}, set())` for an invalid/unreadable record (never
    raises: the same "excluded, not fatal" posture `build_report` takes
    for `excluded_invalid`)."""
    rec = load_record(path, rv, check_filename=True)
    if rec.setup is None or rec.problems:
        return [], {}, set()
    setup = rec.setup
    patterns_meta = {
        p["pattern_id"]: _pattern_text_entry(p.get("canonical_text"))
        for p in (setup.get("patterns") or [])
    }
    sb = f"{setup['subbench']['id']}@{setup['subbench']['version']}"
    testee = setup["testee"]
    testee_id = testee["testee_id"]
    engine_family = testee.get("engine_name") or (parse_testee_id(testee_id) or (None,))[0]
    engine_variant = engine_variant_for(testee_id, testee)
    pin = testee.get("engine_version")
    record_id = setup["record_id"]
    measured_utc = setup.get("run", {}).get("timestamp")
    record_status = setup.get("status", "measured")
    subject_bytes = {s["subject_id"]: s.get("bytes_offered")
                      for s in setup.get("subjects", []) or []}

    def base_row(pattern_id, regime, form):
        return {
            "pattern": pattern_id, "regime": regime, "form": form or "plain",
            "testee_id": testee_id, "engine_family": engine_family,
            "engine_variant": engine_variant, "pin": pin,
            "record_id": record_id, "measured_utc": measured_utc,
            "median_ns": None, "spread_lo_ns": None, "spread_hi_ns": None,
            "subject_bytes_total": None, "n_subjects": None,
        }

    out = []

    # Compile-row refusals/declines: one row per (pattern_id, form) that
    # never reached a match regime at all -- report.py's own
    # did_not_compile_by_pattern/unsupported_by_pattern logic, applied to
    # this one record's raw compile rows.
    compile_diag = {}  # (pattern_id, form) -> (status, diagnostic)
    compiled_forms = set()  # [B70]: (pattern_id, form) this testee compiled CLEANLY
    for row in rec.rows:
        if row.get("kind") != "compile":
            continue
        outcome = row.get("compile_outcome")
        form = row.get("form") or "plain"
        if outcome == "compiled":
            compiled_forms.add((row["pattern_id"], form))
            continue
        status = _COMPILE_STATUS.get(outcome)
        if status is None:
            continue
        key = (row["pattern_id"], form)
        if key not in compile_diag:
            compile_diag[key] = (status, row.get("diagnostic"))

    matched_pattern_forms = set()
    for (pattern_id, regime, form), by_subject in cells_from_record(rec.rows).items():
        matched_pattern_forms.add((pattern_id, form or "plain"))
        row = base_row(pattern_id, regime, form)
        if record_status != "measured":
            row["status"] = (record_status if record_status in _NON_MEASURED_RECORD_STATUS
                              else "excluded")
            out.append(row)
            continue
        red = reduce_set_cell(by_subject)
        if red.expectation_failing:
            row["status"] = _failing_kind(red)
            row["n_subjects"] = red.n_subjects
            out.append(row)
            continue
        byte_vals = [subject_bytes.get(sid) for sid in by_subject]
        row["status"] = "measured"
        row["median_ns"] = red.median_ns
        row["spread_lo_ns"] = red.min_ns
        row["spread_hi_ns"] = red.max_ns
        row["n_subjects"] = red.n_subjects
        row["subject_bytes_total"] = (sum(byte_vals) if byte_vals and
                                        all(v is not None for v in byte_vals) else None)
        out.append(row)

    for (pattern_id, form), (status, diagnostic) in compile_diag.items():
        if (pattern_id, form) in matched_pattern_forms:
            continue  # this testee DID reach a regime on this pattern/form
        row = base_row(pattern_id, "", form)
        row["status"] = status
        row["diagnostic"] = diagnostic
        out.append(row)

    return out, patterns_meta, compiled_forms


# -------------------------------------------------------------- rendering

def _json_for_js(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def atomic_write(path, text):
    d = os.path.dirname(path)
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".tmp-", suffix=".js")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        # mkstemp opens 0600; every other generated file in this repo (the
        # reporter's own reports/*.tsv included) is 0644 -- match that
        # rather than leaving a committed file owner-only-readable.
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def render_set_file(sb, subbench, version, rows, patterns_meta, generated_utc, index_rows_n):
    rows_sorted = sorted(rows, key=lambda r: (
        r["pattern"], r["regime"], r["form"], r["testee_id"]))
    payload = {
        "meta": {
            "generated_by": "tools/viewer_export.py",
            "generated_utc": generated_utc,
            "index_rows": index_rows_n,
            "set": sb,
        },
        "set": sb, "subbench": subbench, "version": version,
        "rows": rows_sorted,
        # [B67] 9.8: ONE entry per pattern_id, factored out of the rows
        # (a pattern's text is invariant across every testee/regime/form
        # row that shares it -- carrying it per row would multiply a
        # ~2 KB string by every row sharing that pattern, which on
        # bench/altwide's kB-scale corpus is a real size cost for no
        # reason). `viewer.html` looks this up by (set, pattern_id).
        "patterns": patterns_meta,
    }
    return "BENCH.load(" + _json_for_js(payload) + ");\n"


def render_manifest(generated_utc, index_rows_n, set_entries, all_pins):
    payload = {
        "generated_utc": generated_utc,
        "store_rows": index_rows_n,
        "all_pins": all_pins,
        "status_sink_order": STATUS_SINK_ORDER,
        "files": [e["file"] for e in set_entries],
        "sets": set_entries,
    }
    return "BENCH.manifest(" + _json_for_js(payload) + ");\n"


# ------------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--store", default=DEFAULT_STORE)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--all-pins", action="store_true",
                     help="keep every pin's own newest record as its own "
                          "column, instead of collapsing to the newest pin "
                          "per canonical (engine, config) identity")
    ap.add_argument("--sets", default=None,
                     help="comma-separated subbench@version (or bare "
                          "subbench, matching every version) to export -- "
                          "a development slice; omitted = every set")
    ap.add_argument("--keep-existing-manifest", action="store_true",
                     help="merge this run's set list into the manifest "
                          "ALREADY on disk (for a --sets slice run that "
                          "must not blank out the other sets' entries)")
    args = ap.parse_args(argv)

    index_rows, index_rows_n = read_index(args.store)
    kept = dedup_newest_per_testee(index_rows)
    if not args.all_pins:
        kept = collapse_to_newest_pin(kept)

    sets_filter = None
    if args.sets:
        sets_filter = set()
        for tok in args.sets.split(","):
            tok = tok.strip()
            if tok:
                sets_filter.add(tok)

    by_set = defaultdict(list)
    for row in kept:
        sb = f"{row['subbench']}@{row['version']}"
        if sets_filter and sb not in sets_filter and row["subbench"] not in sets_filter:
            continue
        by_set[sb].append(row)

    rv = _get_record_validator()
    generated_utc = utcnow_iso()
    set_entries = []
    for sb in sorted(by_set):
        rows = []
        patterns_meta = {}  # pattern_id -> entry, FIRST record wins (canonical per sub-bench)
        compiled_by_testee = {}  # testee_id -> {(pattern_id, form)}, [B70]
        for idx_row in sorted(by_set[sb], key=lambda r: r["testee_id"]):
            path = os.path.join(args.store, idx_row["path"])
            record_rows, record_patterns_meta, compiled_forms = export_rows_for_record(path, rv)
            rows.extend(record_rows)
            for pattern_id, entry in record_patterns_meta.items():
                patterns_meta.setdefault(pattern_id, entry)
            if compiled_forms:
                compiled_by_testee[idx_row["testee_id"]] = compiled_forms
            # MEMORY: nothing from this record's raw rows/setup survives
            # past export_rows_for_record's return -- `rec`/`rec.rows`
            # went out of scope with that call.
        rows = _fold_and_classify(rows, compiled_by_testee)  # [B70] 10 items 1-3
        subbench, version = sb.split("@", 1)
        text = render_set_file(sb, subbench, version, rows, patterns_meta, generated_utc, index_rows_n)
        out_path = os.path.join(args.out, f"{sb}.js")
        atomic_write(out_path, text)
        set_entries.append({"set": sb, "subbench": subbench, "version": version,
                             "file": os.path.basename(out_path), "n_rows": len(rows)})
        print(f"wrote {out_path}: {len(rows)} row(s) from {len(by_set[sb])} record(s)")

    manifest_path = os.path.join(args.out, "manifest.js")
    if args.keep_existing_manifest and os.path.exists(manifest_path):
        prev = _read_prev_manifest_sets(manifest_path)
        written = {e["set"] for e in set_entries}
        for s, entry in prev.items():
            if s not in written:
                set_entries.append(entry)
        set_entries.sort(key=lambda e: e["set"])

    manifest_text = render_manifest(generated_utc, index_rows_n, set_entries, args.all_pins)
    atomic_write(manifest_path, manifest_text)
    print(f"wrote {manifest_path}: {len(set_entries)} set(s)")
    return 0


def _read_prev_manifest_sets(manifest_path):
    """Parse the previous run's `BENCH.manifest({...});` call back into
    {set: entry} -- used only by `--keep-existing-manifest` (a `--sets`
    slice run) so it can carry forward the OTHER sets' entries rather
    than dropping them from the manifest it writes."""
    with open(manifest_path, encoding="utf-8") as f:
        text = f.read()
    start = text.index("(")
    end = text.rindex(")")
    obj = json.loads(text[start + 1:end])
    return {e["set"]: e for e in obj.get("sets", [])}


if __name__ == "__main__":
    sys.exit(main())
