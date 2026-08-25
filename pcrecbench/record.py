"""record.py -- build the record dict the schema describes.

Every DERIVED identifier is derived here by the SAME rule `schema/validate.py`
checks it against (record_schema.md 3, 6.4, X3/X5/X6) -- but by importing the
validator's own functions rather than reimplementing them. Two implementations
of one derivation is exactly the shape of bug pcrec's check-design lesson
warns about, one level up: a check whose expected value shares a source with
the thing it checks proves nothing.
"""

import hashlib
import importlib.util
import json
import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_VERSION = "1.0"


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
    try:
        entry["canonical_text"] = text.decode("utf-8")
    except UnicodeDecodeError:
        # REPRODUCIBILITY-ONLY and optional; a pattern with non-UTF-8 bytes
        # (this sub-bench's classes have them) is pinned by its sha256 and by
        # `subbench.content_hash`, which is the actual source of truth.
        pass
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
                patterns, subjects, status, status_detail=None, note=None):
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
    setup["testee"]["testee_id"] = derive_testee_id(setup["testee"])
    setup["record_id"] = derive_record_id(setup)
    setup["content_hash"] = {"algorithm": "sha256", "value": "0" * 64}
    return setup


def compile_row(pattern_id, trial, outcome, cost_class, phases=None,
                phase_seconds=None, engine_metadata=None, diagnostic=None,
                artifact_bytes=None, declaration_ref=None):
    row = {
        "kind": "compile",
        "pattern_id": pattern_id,
        "trial": trial,
        "compile_outcome": outcome,
        "cost_class": cost_class,
    }
    # record_schema.md: `cost` is present IFF outcome == compiled AND the
    # class is not lazy-jit. A lazy-jit row carries `derivation` instead --
    # neither adapter here is one, so that branch is stated and unbuilt.
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
    if artifact_bytes is not None:
        row["artifact_bytes"] = int(artifact_bytes)
    if engine_metadata:
        row["engine_metadata"] = dict(engine_metadata)
    if declaration_ref:
        row["declaration_ref"] = declaration_ref
    if diagnostic or outcome == "did-not-compile":
        row["diagnostic"] = diagnostic or "(the engine gave no diagnostic)"
    return row


def match_row(pattern_id, subject_id, regime_enum, trial, outcome,
              timing=None, consumed=None, truncation=None, observed=None,
              diagnostic=None):
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
    return row
