"""record.py -- build the record dict the schema describes.

Every DERIVED IDENTIFIER is derived here by the SAME rule `schema/validate.py`
checks it against (record_schema.md 3, 6.4, X3/X5/X6) -- but by importing the
validator's own functions rather than reimplementing them. Two implementations
of one derivation is exactly the shape of bug pcrec's check-design lesson
warns about, one level up: a check whose expected value shares a source with
the thing it checks proves nothing.

That rule is SCOPED to derivations-of-convention (gate_shape_v14.md 4 V6,
panel B B14): X3/X5/X6 derive identifiers FROM A CONVENTION -- there is no
fact of the matter to check, and a second implementation only creates drift
that rejects honest records. The v1.4 `trial_agreement` block is the other
case: X32 checks A VERDICT THE HARNESS STAMPED BESIDE ROWS IT ALSO WROTE --
X20's and X26's situation exactly -- so there the validator carries its OWN
implementation of the arithmetic (validate.py `judge_trial_agreement`), and
the harness's (`pcrecbench/reduce.py`'s) is deliberately not imported by it.
"""

import hashlib
import importlib.util
import json
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The schema version this harness emits. Bumping it is a deliberate act: the
# fields below and `schema/record.schema.json` move together, and
# `make check` is what proves they did.
SCHEMA_VERSION = "1.5"

#: What the drivers actually call. Both use `clock_gettime(CLOCK_MONOTONIC)`
#: around the batched loop -- never a wall clock, never a per-call timer.
CLOCK_SOURCE = "clock_monotonic"

#: The schema's `free_text` cap (`schema/record.schema.json` $defs.free_text,
#: maxLength 1048576 since schema v1.5, KB-7, record_schema.md 4.1). `note`
#: and `status_detail` are both free_text, and the harness fills them from a
#: per-cell LIST of sentences whose length grows with the set:
#: bench/bounded@0.1's 24 patterns x 3 regimes made 72 calibration sentences
#: (~12 KB) and a 21-minute cell was measured and then REJECTED at
#: validation against the ORIGINAL 8192 cap (2026-08-29, the first bounded
#: window). The join below is the only way those lists reach a record.
#:
#: The cap was raised from 8192 to 1048576 (1 MiB) at [B30] (2026-09-02,
#: Frank's ruling on KB-7): it is HYGIENE against a stray blob landing in a
#: text field, not a limit on legitimate content, and 8192 was never derived
#: from anything -- no document justified it. `patterns[].canonical_text`
#: (below) is the field the old bound bit first (bench/altwide's 8.7-24 KB
#: alternation patterns, [B11.2]); the omission fallback for a pattern still
#: over THIS cap is unchanged, just further away.
FREE_TEXT_MAX = 1048576
NOTE_SEP = "; "


def join_notes(notes, prefix=None, first=None, limit=FREE_TEXT_MAX):
    """Join the harness's per-cell sentences into ONE string that VALIDATES.

    `prefix` (the operator's `--note`) comes first, then the sentences joined
    by NOTE_SEP. If the whole would exceed `limit`, sentences are dropped from
    the END and the string ends with an explicit marker saying how many were
    elided -- silently truncating a diagnostic would be worse than losing it,
    and the per-row `calibration` blocks carry the calibration facts anyway.
    A prefix that alone exceeds `limit` is cut hard with the same marker.

    `first` (v1.4, ruling R-4): the STATUS-DECIDING sentence(s) -- the gate's
    reasons or the trial-agreement line. They are placed at offset 0 of the
    body (after `prefix`) and are NEVER elided: the drop-from-the-end rule
    can only ever remove `notes` -- the calibration / adapter sentences --
    and the elision marker names that class, because under this ordering it
    is the only class it can drop. The sentence that explains a status must
    survive the sentences that merely annotate it.
    """
    notes = [str(n) for n in (notes or [])]
    first = [str(n) for n in (first or [])]
    prefix = str(prefix) if prefix else ""

    def build(kept, elided):
        parts = []
        if prefix:
            parts.append(prefix)
        body = NOTE_SEP.join(first + kept)
        if elided:
            body = (body + NOTE_SEP if body else "") + (
                "[+%d calibration/adapter note(s) elided to fit the schema's "
                "%d-byte free_text cap; the per-row calibration blocks carry "
                "the calibration facts]" % (elided, limit))
        if body:
            parts.append(body)
        return " | ".join(parts)

    for keep in range(len(notes), -1, -1):
        out = build(notes[:keep], len(notes) - keep)
        if len(out) <= limit:
            return out
    # Even zero sentences did not fit: the prefix (or a `first` sentence)
    # itself is over the cap -- cut hard, and say so.
    head = build([], 0)
    marker = " [cut to fit the schema's %d-byte free_text cap]" % limit
    return head[:max(limit - len(marker), 0)] + marker


def _validator_module():
    """Import `schema/validate.py` as a module so the derivations here are
    LITERALLY the ones the validator will apply."""
    path = os.path.join(REPO_ROOT, "schema", "validate.py")
    spec = importlib.util.spec_from_file_location("pcrecbench_validate", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_V = None


def V():
    global _V
    if _V is None:
        _V = _validator_module()
    return _V


def derive_testee_id(testee):
    return V().derive_testee_id(testee)


def derive_record_id(setup):
    return V().derive_record_id(setup)


def stamp_content_hash(setup, rows):
    """record_schema.md 3. The row lines hashed are the ones that will be
    WRITTEN, so this serialises them exactly as store.serialize() does."""
    row_lines = [json.dumps(r, sort_keys=True, separators=(",", ":"),
                            ensure_ascii=False) for r in rows]
    value = V().compute_content_hash(setup, row_lines)
    out = dict(setup)
    out["content_hash"] = {"algorithm": "sha256", "value": value}
    return out


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


# ------------------------------------------------------------------ forms

#: `$defs/form` -- WHICH ARTIFACT of a pattern a row is about. `plain` is the
#: pattern as the sub-bench spells it. `whole-subject` is the separately
#: compiled anchored artifact a testee with no end-anchored mode must build
#: (pcrec: `(?:pattern)\z`). ABSENT means `plain`, so a testee that needs
#: only one artifact -- libpcre2, which anchors with runtime flags -- omits
#: the field entirely and its rows read exactly as they did before v1.1.
#:
#: The two forms NEVER share a row: they are different compiles of different
#: text driving different matchers. Rules X9/X11/X14 are keyed per form, and
#: X27 rejects a `whole-subject` match row whose record has no `whole-subject`
#: compile row -- a timing whose compile the record does not witness.
FORM_PLAIN = "plain"
FORM_WHOLE_SUBJECT = "whole-subject"


def whole_subject_text(pattern):
    r"""The `whole-subject` artifact's pattern text, as bytes.

    `\z` and not `$`: at `options = 0` PCRE2's `$` also matches before a
    final newline, so `$` would silently accept a subject with a trailing
    newline that the oracle rejects. `(?:...)` and not bare concatenation: a
    top-level alternation would otherwise bind the anchor to its last branch
    only -- `a|ab\z` is not `(?:a|ab)\z`."""
    return b"(?:" + pattern + rb")\z"


# --------------------------------------------------------------- the blocks

def pattern_entry(sb, name):
    """`setup.patterns[]`. `variant` is `null` and that is a STATEMENT
    (requirements 4.5: a variant is never a silent fork, so the record says
    which even when there is none)."""
    p = sb.pattern(name)
    text = sb.pattern_bytes(name)
    entry = {
        "pattern_id": name,
        "canonical_sha256": sha256_bytes(text),
        "hazard_class": p.hazard_class,
        "size_class": p.size_class,
        "variant": None,
    }
    # v1.3 ([B15]): ABSENT means `member`, exactly like `form` means `plain`
    # when absent -- a sidecar with no `role` key produces a record
    # identical to what it always produced.
    if getattr(p, "role", "member") != "member":
        entry["role"] = p.role
    # `canonical_text` is REPRODUCIBILITY-ONLY and OPTIONAL
    # (record_schema.md 8: "convenience for reading a record alone; the
    # sub-bench is the source of truth"). It is omitted, never mangled, in
    # the two cases where it cannot be carried honestly:
    #
    #   * a pattern with non-UTF-8 bytes (bench/email's classes have them);
    #   * a pattern LONGER THAN THE SCHEMA'S `free_text` CAP -- four of
    #     bench/altwide's wide-alternation rungs were 8.7-24 KB of pattern
    #     text ([B11.2], 2026-09-01), which is what found this branch; the
    #     cap moved to 1048576 at [B30] (2026-09-02, KB-7) so those rungs
    #     now CARRY their text -- the branch stays, for the pattern that
    #     someday is over a megabyte. Truncating would put a string in the
    #     record that is not the pattern, under a field name that says it
    #     is; the sha256 beside it and `subbench.content_hash` are the
    #     identity either way, which is why dropping it costs nothing.
    try:
        decoded = text.decode("utf-8")
    except UnicodeDecodeError:
        decoded = None
    if decoded is not None and len(decoded) <= FREE_TEXT_MAX:
        entry["canonical_text"] = decoded
    tags = list(p.tags)
    if p.feature_tier:
        tags.append("tier:" + p.feature_tier)
    if p.convention:
        tags.append("convention:" + p.convention)
    if tags:
        entry["tags"] = tags
    return entry


def subject_entry(subj):
    return {
        "subject_id": subj.subject_id,
        "role": "single",
        "n_subjects": 1,
        "bytes_offered": subj.length,
        "sha256": subj.sha256,
    }


def build_setup(sb, testee_block, environment, run_block, regimes,
                patterns, subjects, status, status_detail=None, note=None,
                trial_agreement=None):
    """The setup layer. `trial_agreement` (v1.4, X33: REQUIRED on every
    record this harness writes) is `reduce.judge_trial_agreement(rows)`,
    computed by the caller AFTER every row exists."""
    setup = {
        "kind": "setup",
        "schema_version": SCHEMA_VERSION,
        "status": status,
        "run": run_block,
        "subbench": {
            "id": sb.id,
            "version": sb.version,
            "content_hash": sb.content_hash(),
            "objective": sb.objective,
            "regimes": [regimes[r] for r in sorted(set(regimes))]
            if isinstance(regimes, dict) else list(regimes),
            "source_ref": "bench/%s (wrapped from pcrec "
                          "docs/design/subroutines_measurements/"
                          "email_specimen)" % os.path.basename(sb.root),
        },
        "testee": dict(testee_block),
        "environment": environment,
        "patterns": patterns,
        "subjects": subjects,
    }
    if status_detail:
        setup["status_detail"] = status_detail
    if note:
        setup["note"] = note
    if trial_agreement is not None:
        setup["trial_agreement"] = dict(trial_agreement)
    setup["testee"]["testee_id"] = derive_testee_id(setup["testee"])
    setup["record_id"] = derive_record_id(setup)
    setup["content_hash"] = {"algorithm": "sha256", "value": "0" * 64}
    return setup


def compile_row(pattern_id, trial, outcome, cost_class, phases=None,
                phase_seconds=None, engine_metadata=None, diagnostic=None,
                artifact_bytes=None, declaration_ref=None, seq=None,
                form=None):
    row = {
        "kind": "compile",
        "pattern_id": pattern_id,
        "trial": trial,
        "compile_outcome": outcome,
        "cost_class": cost_class,
    }
    # record_schema.md: `cost` is REQUIRED when outcome == compiled AND the
    # class is not lazy-jit (a lazy-jit row carries `derivation` instead --
    # neither adapter here is one, so that branch is stated and unbuilt).
    # Since v1.4 (KB-4's schema half) a refusal MAY carry `cost` too, and
    # KB-4's adapter half (docs/dev/known_issues.md, 2026-09-01) is what
    # fills it below: the bench's own clock around whichever phase(s)
    # actually ran before the refusal (I-20's ruling -- pcrec prints no
    # timing on any path, so this is the bench's clock, never pcrec's).
    if outcome == "compiled" and cost_class != "lazy-jit" and phase_seconds:
        total = sum(phase_seconds.get(p, 0.0) for p in (phases or []))
        row["cost"] = {
            "total_ns": int(round(total * 1e9)),
            "phases": [{"name": p,
                        "elapsed_ns": int(round(phase_seconds.get(p, 0.0) * 1e9))}
                       for p in (phases or [])],
        }
    elif outcome == "compiled" and cost_class == "lazy-jit":
        row["derivation"] = "trial-1-minus-steady-state"
    elif phase_seconds:
        # A refusal's cost NEVER carries a `phases` array: rule X12
        # requires `cost.phases[].name` to equal the testee's declared
        # `compile_phases` EXACTLY whenever the key is present at all, and
        # a refusal by construction never ran every declared phase -- so
        # `total_ns` alone (summed over whatever phases the caller DID
        # time) is the only schema-legal shape, matching
        # schema/examples/...20260830T120000Z.jsonl's KB-4 row.
        row["cost"] = {"total_ns": int(round(sum(phase_seconds.values()) * 1e9))}
    if artifact_bytes is not None:
        row["artifact_bytes"] = int(artifact_bytes)
    if engine_metadata:
        row["engine_metadata"] = dict(engine_metadata)
    if declaration_ref:
        row["declaration_ref"] = declaration_ref
    if diagnostic or outcome == "did-not-compile":
        row["diagnostic"] = diagnostic or "(the engine gave no diagnostic)"
    if seq is not None:
        row["seq"] = seq
    _stamp_form(row, form)
    return row


def match_row(pattern_id, subject_id, regime_enum, trial, outcome,
              timing=None, consumed=None, truncation=None, observed=None,
              diagnostic=None, seq=None, calibration=None,
              form=None):
    row = {
        "kind": "match",
        "pattern_id": pattern_id,
        "subject_id": subject_id,
        "regime": regime_enum,
        "trial": trial,
        "match_outcome": outcome,
    }
    if timing is not None:
        row["timing"] = timing
    row["consumed_length"] = consumed
    if truncation is not None:
        row["truncation_check"] = truncation
    if observed is not None:
        row["observed"] = observed
    if diagnostic:
        row["diagnostic"] = diagnostic
    if seq is not None:
        row["seq"] = seq
    if calibration is not None:
        row["calibration"] = dict(calibration)
    _stamp_form(row, form)
    return row


def _stamp_form(row, form):
    """`form` is stamped only when it is NOT `plain`.

    The schema reads an ABSENT `form` as `plain`, so an engine that needs one
    artifact -- every engine that anchors with runtime options -- keeps rows
    identical to their pre-v1.1 shape, and the field appears exactly where it
    carries information."""
    if form and form != FORM_PLAIN:
        row["form"] = form
