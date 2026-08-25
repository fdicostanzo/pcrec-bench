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

# =========================================================================
# THE SCHEMA VERSION, AND THE ONE PLACE THE RECORD IS NARROWED TO IT
# =========================================================================
#
# The harness BUILDS every record with the full v1.1 field set -- the load and
# occupancy samples with their provenance, the calibration numbers behind each
# `iters`, the driver's exact build command, the per-row `seq`, the clock
# source, the CPU MHz. It then PROJECTS that onto whatever `SCHEMA_VERSION`
# says, and `project()` below is the only code that knows the difference.
#
# The direction matters and is not symmetric. A field that was never MEASURED
# cannot be added to an old record afterwards; a field that was measured and
# not emitted costs one line to start emitting. So the sampling is always
# maximal and the emission is versioned.
#
# TO ADOPT v1.1: set SCHEMA_VERSION to "1.1" and delete the entries from
# V11_ONLY that the merged schema accepts. Nothing else moves.
SCHEMA_VERSION = "1.0"

#: Fields the harness computes that schema 1.0 does not accept
#: (`additionalProperties: false` everywhere, so emitting one is a hard
#: rejection). Each entry cites the v1.1 item it is waiting for.
V11_ONLY = {
    "row.seq":                  "v1.1 (1) monotonic emission order per row",
    "row.calibration":          "v1.1 (4) {target_ns, probe_iterations, probe_elapsed_ns}",
    "load.sample_detail":       "v1.1 (2) load.before/after become objects",
    "occupancy.before_after":   "v1.1 (3) occupancy gains before/after",
    "run.driver_build_flags":   "v1.1 (6) the driver's exact compile command",
    "run.driver_compiler":      "v1.1 (6)",
    "run.clock_source":         "v1.1 (9) clock_monotonic",
    "environment.cpu_mhz":      "v1.1 (10), optional",
}

#: What the drivers actually call. Both use `clock_gettime(CLOCK_MONOTONIC)`
#: around the batched loop -- never a wall clock, never a per-call timer.
CLOCK_SOURCE = "clock_monotonic"


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


# ------------------------------------------------------------- projection

def project(setup, rows, schema_version=None):
    """Narrow a fully-built record to the emitted schema version.

    THE ONLY place a v1.1 field is dropped. Everything above builds the full
    record; this decides what 1.0 is allowed to carry. Returns (setup, rows),
    both fresh objects -- the caller's full-fidelity versions are not mutated,
    so a caller that wants the measured-but-unemitted numbers (a log line, a
    future migration) still has them."""
    version = schema_version or SCHEMA_VERSION
    if version != "1.0":
        return setup, rows

    setup = json.loads(json.dumps(setup))
    env = setup.get("environment", {})

    # (2) load.before/after are three bare numbers at 1.0, objects at 1.1.
    load = env.get("load")
    if load:
        for end in ("before", "after"):
            v = load.get(end)
            if isinstance(v, dict):
                load[end] = v["loadavg"]

    # (3) occupancy is ONE object at 1.0. The combined verdict is already the
    # worse of the two samples (quiet.occupancy_block), so the gate does not
    # weaken -- only the two samples' separate provenance is lost, and the
    # `raw` text of both is kept because 1.0 has a place for it.
    occ = env.get("occupancy")
    if occ:
        for k in ("before", "after"):
            occ.pop(k, None)

    # (10) cpu_mhz has no home at 1.0.
    env.pop("cpu_mhz", None)

    # (6)+(9) the driver's provenance and the clock source have no home at 1.0.
    run = setup.get("run", {})
    for k in ("driver_build_flags", "driver_compiler", "clock_source"):
        run.pop(k, None)

    # (1)+(4) per-row seq and calibration.
    out_rows = []
    for r in rows:
        r = dict(r)
        r.pop("seq", None)
        r.pop("calibration", None)
        out_rows.append(r)
    return setup, out_rows


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
                artifact_bytes=None, declaration_ref=None, seq=None):
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
    if seq is not None:
        row["seq"] = seq
    return row


def match_row(pattern_id, subject_id, regime_enum, trial, outcome,
              timing=None, consumed=None, truncation=None, observed=None,
              diagnostic=None, seq=None, calibration=None):
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
    return row
