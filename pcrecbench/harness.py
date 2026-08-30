"""harness.py -- run one CELL and produce one RECORD (harness contract 4).

The seven steps of contract 4, in order, and each is one function below:

  (1) load the sub-bench            `subbench.find`
  (2) `quiet.check()` + the gate    refuse (exit 3) unless quiet or forced
  (3) prepare + compile + measure   the adapter
  (4) sample load AFTER             requirements 9(a): a box that went busy
                                    partway is just as compromised
  (5) build the record, VALIDATE    a record that fails validation is never
                                    written -- the failure is a harness bug
  (6) write it                      store.write, never silently clobbering
  (7) `index`                       store.index

THE TIER (schema v1.2, record_schema.md 6.8; Frank's I-4). `run_cell` takes
`tier`; an adapter whose testee is scratch BY CONSTRUCTION (`pcrec-local`)
forces it. A scratch run: goes to the scratch store unless a root was named;
is REFUSED into the canonical store before anything else happens; skips the
quiet GATE (`--force-unquiet` implied) but still SAMPLES the box at both ends
and computes `status` honestly; and stamps `tier: scratch` plus
`testee.binary` on the record. The same seven steps, the same record shape,
the same judging -- a scratch number is a real number kept out of the
rankings by its tier, not a lesser measurement.

`pcrecbench quick` (I-4 (b)) is `run_cell` with the knobs it needed and no
second code path: `patterns=` (one), `regimes=` (one), `subject_limit=`
(the first k), `tier="scratch"`, `budget=` (the per-trial calibration cap,
seconds instead of the default 20).

THE JUDGING RULE, which is the thing worth reading twice. The ADAPTER reports
what the engine answered; the HARNESS decides what that means against the
sub-bench's expectation. An adapter that judged its own correctness would be
marking its own homework, so `outcome_for()` below is the only place an
answer becomes a `match_outcome`, and it is engine-independent by
construction.
"""

import itertools
import os
import sys
import time

from . import adapters as _ad
from . import driverrun, env, quiet, record, store
from .subbench import REGIME_TO_ENUM, REGIME_MODE
from . import HARNESS_VERSION

# Contract 3: `iters` is chosen so a subject's loop is >= this. The number is
# the contract's; the calibration RULE is this file's and is stated in
# `calibrate()`.
TARGET_LOOP_SECONDS = 0.050
# ... and no trial's whole sweep may be predicted to exceed this, so one
# pathological subject cannot turn a cell into an overnight run.
TRIAL_BUDGET_SECONDS = 20.0
PROBE_ITERS = {"throughput": 1, "search_short": 200, "match": 200}


class HarnessError(Exception):
    pass


class RunResult:
    """What `run_cell` returns. `setup`/`rows` are what was WRITTEN (narrowed
    to the emitted schema version); `full_setup`/`full_rows` are what was
    BUILT, with every v1.1 field the harness measures."""

    __slots__ = ("path", "record_id", "setup", "rows", "full_setup",
                 "full_rows")

    def __init__(self, path, record_id, setup, rows, full):
        self.path, self.record_id = path, record_id
        self.setup, self.rows = setup, rows
        self.full_setup, self.full_rows = full

    def __iter__(self):
        """Unpacks as the old 4-tuple, so existing callers keep working."""
        return iter((self.path, self.record_id, self.setup, self.rows))


# ------------------------------------------------------------- the judging

def outcome_for(row, expectation, regime, subject, giveup_ok=True):
    """(match_outcome, observed, diagnostic) for one driver answer.

    Requirements 4.4's per-(pattern, subject) set, plus the two [B2]
    ADDITIONS. A GIVE-UP -- an engine declining to answer within its budget --
    is `did-not-match-as-expected`: from the bench's point of view the
    expected answer was not produced, and there is no `gave-up` value because
    a wrong answer and a refused one are both "not the expected answer"
    (bench/email/NOTES.md states this where a reader of the numbers is)."""
    if row.answer == "timedout":
        return "timed-out", None, (row.detail or
                                   "the per-subject alarm fired")
    if row.answer == "crashed":
        return "crashed", None, (row.detail or "the driver did not survive")
    if row.is_giveup:
        # `gave-up` (schema v1.1 fix 21): the engine REFUSED on a resource
        # limit. Counted separately from a wrong answer, because an engine
        # that declined to answer and an engine that answered wrongly are
        # different findings -- and a per-subject refusal is this bench's
        # headline hazard class. Not timed either way.
        #
        # The classification is the ADAPTER's, by RANGE against the engine's
        # own bounds, never by a list kept in step by hand. A code outside
        # the give-up range is `crashed`: pcrec's PCREC_ERR_INTERNAL says
        # outright that it is not a give-up, and a reserved code must never
        # be laundered into one.
        outcome = "gave-up" if giveup_ok else "crashed"
        return (outcome,
                {"matched": False, "span": None, "captures": None},
                "the engine %s rather than answering: %s"
                % ("gave up" if giveup_ok else "failed", row.answer))
    if row.answer.startswith("error"):
        return ("crashed", {"matched": False},
                row.detail or row.answer)
    if (row.consumed is not None and subject is not None
            and row.consumed < subject.length):
        # requirements 4.4: the engine consumed fewer bytes than offered. Not
        # a wrong answer -- a REFUSED question, and the answer it did give is
        # to a different one. Neither testee here can produce it (both take a
        # size_t length), which is why it is a positive control in
        # `make check` rather than something the corpus exercises.
        return ("truncated-subject",
                {"matched": row.matched,
                 "span": [row.start, row.end] if row.matched else None,
                 "captures": None},
                "offered %d bytes, the engine took %d"
                % (subject.length, row.consumed))
    if expectation is None:
        return ("did-not-match-as-expected",
                {"matched": row.matched,
                 "span": [row.start, row.end] if row.matched else None,
                 "captures": None},
                "no expectation exists for this (pattern, subject, regime) -- "
                "the sub-bench must state one before the cell can be judged")

    if row.matched != expectation.matched:
        return ("did-not-match-as-expected",
                {"matched": row.matched,
                 "span": [row.start, row.end] if row.matched else None,
                 "captures": None},
                "expected %s, observed %s"
                % (expectation.expected,
                   "match" if row.matched else "nomatch"))

    if row.matched and (row.start != expectation.start
                        or row.end != expectation.end):
        return ("wrong-span-or-captures",
                {"matched": True, "span": [row.start, row.end],
                 "captures": None},
                "expected span [%s,%s]; observed [%s,%s]"
                % (expectation.start, expectation.end, row.start, row.end))

    if (regime == "throughput" and expectation.nmatches is not None
            and row.nmatches is not None
            and row.nmatches != expectation.nmatches):
        return ("wrong-span-or-captures",
                {"matched": row.matched,
                 "span": [row.start, row.end] if row.matched else None,
                 "captures": None},
                "expected %d non-overlapping match(es); observed %d"
                % (expectation.nmatches, row.nmatches))

    return "matched-as-expected", None, None


def classify_giveup(answer, handle):
    """Is this driver `giveup:<code>[:<name>]` answer a RESOURCE-LIMIT refusal
    (-> `gave-up`) or something else (-> `crashed`)?

    The bounds come from the ADAPTER, which reads them from the engine: pcrec
    exports `[PCREC_ERR_FLOOR, -2]` out of the artifact itself, and pcre2
    supplies the measured set of its limit codes. A range or a measured set,
    never a literal list in this file -- a give-up code an engine adds later
    must classify correctly with nobody editing the harness."""
    try:
        code = int(answer.split(":")[1])
    except (IndexError, ValueError):
        return False
    codes = (handle or {}).get("giveup_codes")
    if codes is not None:
        return code in codes
    lo, hi = (handle or {}).get("giveup_range", (None, None))
    if lo is None:
        return False
    return lo <= code <= hi


def truncation_for(regime, row, subject):
    """record_schema.md `truncation_check`, required on a
    large-subject-throughput row.

      verified                  -- the engine was given, and accepted, every
                                   offered byte (its own length argument
                                   equals `bytes_offered`)
      unverified-for-truncation -- the API exposes no such number
      not-applicable            -- the question does not arise for this
                                   regime (a 40-byte compliance subject)

    Neither C-ABI testee reports a scan HIGH-WATER MARK, so `verified` is the
    narrow claim "no byte was withheld or refused", never "the engine looked
    at every byte". Each adapter's CLAUDE.md says so."""
    if regime != "throughput":
        return "not-applicable"
    if row.consumed is None:
        return "unverified-for-truncation"
    # `verified` says the CHECK WAS MADE, not that nothing was truncated: a
    # cell that was checked and found short is `verified` here and
    # `truncated-subject` in `match_outcome`. Folding the two would let one
    # field answer two questions.
    return "verified"


# ------------------------------------------------------------ calibration

def calibrate(adapter, handle, regime, subjects, requested, timeout,
              subject_timeout, budget=None):
    """Choose `iters`. -> (iters, why, calibration).

    `budget` is the per-trial cap in seconds (default TRIAL_BUDGET_SECONDS);
    `quick` passes ~2 s so a cell stays inside "seconds, not minutes". The
    cap is the SAME rule at a different number -- rule X21's
    `calibration_note` says when it bound.

    Contract 3: "chosen so one subject's loop is >= 50 ms, auto-calibrated by
    python from a probe run, RECORDED IN THE RECORD". The third return value
    is that recording -- schema v1.1 puts `{target_ns, probe_iterations,
    probe_elapsed_ns}` on every match row whose loop ran more than once
    (rule X21), so the number behind the number is never lost. Rule X21 also
    requires the probe to have MET its target, or a `calibration_note` saying
    why it could not; both cases below set one.

    THE RULE, because "one subject" needs saying which. The probe measures
    every subject at a small fixed `iters`; the MEDIAN per-iteration cost sets
    the number, so the median subject's loop reaches the target. Calibrating
    on the fastest subject would multiply the slowest one's cost by orders of
    magnitude; calibrating on the slowest would leave the fast ones under the
    clock's resolution. The chosen `iters` is then capped so the PREDICTED
    total sweep stays inside TRIAL_BUDGET_SECONDS -- one pathological subject
    must not turn a cell into an overnight run -- and the number that was
    actually used lands in every row's `timing.iterations`.

    TWO THINGS THIS FUNCTION GOT WRONG, both found by X21 rejecting a real
    record (pcre2-jit, factored, large-subject-throughput, 2026-08-25):

    1. **The count was floored, and the rule needs a ceiling.** A probe of
       24.79 ms against a 50 ms target gives 2.017, and `int()` chose 2 --
       predicting 49.58 ms, just under target. `iters` is now the smallest
       count that MEETS the target, computed by ceiling division.

    2. **The recorded probe described a different quantity from the one the
       decision was made on.** `probe_elapsed_ns` was the SUM over every
       subject in the probe sweep, while `iters` came from the MEDIAN
       subject. X21 recomputes `probe_elapsed_ns / probe_iterations x
       iterations` and compares it to the target, so those two have to be the
       same quantity or the rule is checking arithmetic the harness never
       did. They coincided in the failing case only because one 24.8 ms
       subject dominated two sub-0.1 ms siblings, which is what made it look
       like pure rounding. The probe recorded now is the MEDIAN SUBJECT'S own
       elapsed and its own iteration count -- a real measurement of the
       subject that actually chose the number.

    The count is then verified against X21's exact expression before it is
    returned, so the two can never silently drift apart again."""
    target_ns = int(TARGET_LOOP_SECONDS * 1e9)
    budget = TRIAL_BUDGET_SECONDS if budget is None else float(budget)
    if requested is not None and int(requested) <= 1:
        # Rule X21 asks for a calibration on any row whose loop RAN more than
        # once. A single-iteration loop was not calibrated and does not claim
        # to have been, so it carries none -- and no probe is run for it,
        # which is what keeps a smoke a smoke.
        return int(requested), "requested on the command line (iters=1)", None
    probe_iters = PROBE_ITERS.get(regime, 100)
    rows_by_trial, _info, _notes = adapter.measure(
        handle, regime, subjects, probe_iters, 1, timeout=timeout)
    rows = rows_by_trial[0] if rows_by_trial else []

    # Sort by per-iteration cost, keeping the ROW, so the median's own
    # measurement -- not a statistic over all of them -- becomes the record.
    timed = sorted(((r.seconds / max(r.iters, 1), r) for r in rows
                    if r.seconds > 0 and r.iters),
                   key=lambda pair: pair[0])
    if not timed:
        cal = {"target_ns": target_ns, "probe_iterations": max(probe_iters, 1),
               "probe_elapsed_ns": 0,
               "calibration_note": "the probe produced no usable timing, so "
                                   "the count fell back to 1"}
        return 1, "the probe run produced no timing; falling back to iters=1", cal

    median_per_iter, median_row = timed[len(timed) // 2]
    probe_n = max(int(median_row.iters), 1)
    probe_ns = max(int(round(median_row.seconds * 1e9)), 1)
    cal = {"target_ns": target_ns, "probe_iterations": probe_n,
           "probe_elapsed_ns": probe_ns}

    if requested is not None:
        # A FIXED count still gets a REAL probe, because X21 compares the
        # probe against the target and a fabricated probe would be a number
        # with nothing behind it. The note says the count was not derived.
        cal["calibration_note"] = (
            "iterations fixed at %d on the command line; the probe was run "
            "for provenance and did not choose the count" % int(requested))
        return int(requested), "requested on the command line", cal

    iters = _iters_meeting_target(target_ns, probe_ns, probe_n)
    total = sum(per_iter for per_iter, _row in timed)
    capped = max(1, int(budget / total)) if total > 0 else iters
    if capped < iters:
        why = ("the median subject would need iters=%d for %.0f ms, capped to "
               "%d by the %g s per-trial budget"
               % (iters, TARGET_LOOP_SECONDS * 1000, capped, budget))
        # X21: the target was NOT met, and the record must say why rather
        # than leave a reader to infer it from two numbers.
        cal["calibration_note"] = why
        return capped, why, cal
    return iters, ("median per-iteration %.3f us (subject %s) -> iters=%d for "
                   "a %.0f ms loop"
                   % (median_per_iter * 1e6, median_row.subject_id, iters,
                      TARGET_LOOP_SECONDS * 1000)), cal


def _iters_meeting_target(target_ns, probe_ns, probe_n):
    """The smallest iteration count whose PREDICTED loop meets `target_ns`.

    Computed with X21's own expression -- `probe_elapsed_ns /
    probe_iterations x iterations` -- from the same integers the record will
    carry, rather than from the floats the probe produced. That is the point:
    a count chosen from one arithmetic and validated by another is how the
    original bug survived, so the prediction is made here in exactly the terms
    the rule will re-make it in.

    Ceiling division, then a defensive re-check: the ceiling is exact for
    integers, and the loop costs nothing when it is already right, but it
    means the returned count CANNOT fail X21 even if either side's rounding
    changes."""
    iters = max(1, -(-target_ns * probe_n // probe_ns))
    while probe_ns / probe_n * iters < target_ns:
        iters += 1
    return iters


# ----------------------------------------------------------------- the run

def run_cell(subbench_name, testee_id, regimes=None, trials=5, iters=None,
             force_unquiet=False, store_root=None, machine_id=None,
             pin_cpu=None, subject_timeout=60, driver_timeout=900,
             command_line=None, note=None, synthetic=False, workdir=None,
             progress=None, tier=store.TIER_PINNED, patterns=None,
             subject_limit=None, budget=None):
    """The whole of contract 4. Returns a `RunResult`.

    It carries BOTH the record as written and the FULL pre-projection one, so
    a caller (and `make check`) can see that the v1.1 fields are really being
    measured rather than merely provided for. A projection nobody can inspect
    is a projection nobody can tell is dead.

    v1.2 knobs (the `quick` surface, and the tier):
      tier           `pinned` (default) or `scratch`; an adapter's own
                     `tier()` can force `scratch`
      patterns       a subset of the sub-bench's pattern ids (default all)
      subject_limit  the FIRST k subjects of each regime's set (default all)
      budget         the per-trial calibration cap in seconds (default 20)
      store_root     None = the tier's default store: canonical for
                     `pinned`, `$PCRECBENCH_SCRATCH_STORE` or
                     build/scratch-store/ for `scratch`"""
    from .subbench import find as find_subbench

    say = progress or (lambda *_a: None)

    # (1) the sub-bench -----------------------------------------------------
    sb = find_subbench(subbench_name)
    regimes = list(regimes or sb.regimes)
    unknown = [r for r in regimes if r not in sb.regimes]
    if unknown:
        raise HarnessError("%s does not declare regime(s) %s (it declares %s)"
                           % (sb.id, ", ".join(unknown), ", ".join(sb.regimes)))
    missing = sb.missing_subject_files(regimes)
    if missing:
        raise HarnessError(
            "%d subject file(s) are missing, starting with %s.\nThe subject "
            "trees are GENERATED and gitignored -- run the sub-bench's "
            "generators:\n  python3 bench/%s/gen_subjects.py\n"
            "  python3 bench/%s/gen_throughput_subjects.py"
            % (len(missing), missing[0], subbench_name, subbench_name))
    if patterns:
        have = {p.name for p in sb.patterns}
        unknown = [p for p in patterns if p not in have]
        if unknown:
            raise HarnessError("%s has no pattern(s) %s (it has %s)"
                               % (sb.id, ", ".join(unknown),
                                  ", ".join(sorted(have))))
        cell_patterns = [p for p in sb.patterns if p.name in set(patterns)]
    else:
        cell_patterns = list(sb.patterns)
    if subject_limit is not None and int(subject_limit) < 1:
        raise HarnessError("subject_limit must be >= 1, got %r" % subject_limit)

    adapter, cfg = _ad.resolve(testee_id)

    # (1b) THE TIER, and the early refusal ---------------------------------
    # An adapter whose testee is scratch by construction (a provided binary)
    # forces the tier; the store's rule is then applied BEFORE the gate, the
    # registry or a driver -- a refused run touches nothing.
    forced = adapter.tier(testee_id)
    if forced == store.TIER_SCRATCH:
        tier = store.TIER_SCRATCH
    if tier not in store.TIERS:
        raise HarnessError("unknown tier %r (the tiers are %s)"
                           % (tier, ", ".join(store.TIERS)))
    if store_root is None:
        store_root = store.default_store_for(tier)
    store.check_tier_allowed(store_root, tier)
    scratch = tier == store.TIER_SCRATCH
    if scratch:
        # The GATE is not applied at the scratch tier (record_schema.md 6.8):
        # a quick cell runs on the box as it is. The INSTRUMENT still runs,
        # below, and `status` is still what the samples say.
        force_unquiet = True

    # (2) the quiet gate ----------------------------------------------------
    say("checking the box (mpstat takes ~1 s)...")
    load_before, occ_before = quiet.check(exclude_cpu=pin_cpu)
    reasons = quiet.gate(load_before, occ_before, force=force_unquiet)
    pinning = quiet.pinning(pin_cpu)

    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    # A scratch store borrows the canonical registry's machine id (6.5):
    # one box, one id, and a quick cell must not demand a fresh --machine-id
    # for a box the canonical store already names.
    fallback = () if store.is_canonical(store_root) else (store.DEFAULT_STORE,)
    environment = env.describe(store_root, machine_id=machine_id,
                               timestamp=timestamp, fallback_roots=fallback)
    environment["pinning"] = pinning
    # `quiet_attestation` was DROPPED in schema v1.1 (fix 8): a boolean the
    # harness set from its own reasons list was a claim beside a measurement,
    # and it could only ever agree with the gate that produced it. The
    # measurements -- load and occupancy, both ends, with their raw evidence
    # -- are what the record carries now.

    # (3) prepare, compile, measure ----------------------------------------
    workdir = workdir or os.path.join(store.REPO_ROOT, "build", "work",
                                      testee_id)
    os.makedirs(workdir, exist_ok=True)
    say("preparing %s ..." % testee_id)
    adapter.prepare(testee_id, workdir)
    testee_block = adapter.describe(testee_id, workdir)
    # `tier` is a SETUP field, not a testee field; an adapter that forces it
    # says so in describe() too, and the two must agree.
    described = testee_block.pop("tier", None)
    if described == store.TIER_SCRATCH and not scratch:
        raise HarnessError(
            "%s.describe(%r) says tier scratch but %s.tier(%r) said %r; the "
            "adapter is inconsistent and the early refusal would have been "
            "skipped" % (adapter.name, testee_id, adapter.name, testee_id,
                         forced))
    if scratch and "binary" not in testee_block:
        # X29: a scratch record says what the binary was.
        testee_block["binary"] = adapter.binary_identity(testee_id, workdir)

    notes = list(reasons)
    if scratch:
        notes.append("tier scratch: the quiet GATE was not applied "
                     "(record_schema.md 6.8); the box was still sampled and "
                     "status is what the samples say")
    rows = []
    compiled = {}
    # v1.1 (1): a monotonic emission order across the WHOLE record, compile
    # and match rows alike. Row order is not significant to the schema, so
    # without this the sequence a harness actually ran things in -- which is
    # what a thermal-drift or warm-up question needs -- is unrecoverable.
    seq = itertools.count(1)
    options = (sb.testee_notes.get(adapter.name, {}) or {}).get("options", {})

    for p in cell_patterns:
        say("compiling %s / %s (%d trial(s)) ..." % (testee_id, p.name, trials))
        cp = adapter.compile(testee_id, p.name, sb.pattern_bytes(p.name),
                             options, trials, workdir)
        compiled[p.name] = cp
        phases = testee_block["compile_phases"]
        for form, cr in cp.forms.items():
            n = len(cr.phase_seconds) if cr.outcome == "compiled" else 1
            for t in range(1, max(n, 1) + 1):
                ps = (cr.phase_seconds[t - 1]
                      if t - 1 < len(cr.phase_seconds) else None)
                rows.append(record.compile_row(
                    p.name, t, cr.outcome, testee_block["execution_model"],
                    phases=phases, phase_seconds=ps,
                    engine_metadata=cr.engine_metadata,
                    diagnostic=cr.diagnostic,
                    artifact_bytes=cr.artifact_bytes,
                    declaration_ref=cr.declaration_ref,
                    seq=next(seq), form=form))
            if cr.outcome != "compiled":
                notes.append("%s did not compile %s (%s form): %s"
                             % (testee_id, p.name, form, cr.diagnostic))

    subject_ids = {}
    for p in cell_patterns:
        cp = compiled.get(p.name)
        if cp is None:
            continue
        for regime in regimes:
            subjects = sb.subjects_for(regime)
            if subject_limit is not None:
                subjects = subjects[:int(subject_limit)]
            if not subjects:
                continue
            # WHICH ARTIFACT this regime must be measured on. `match` is the
            # whole-subject question and uses the whole-subject artifact when
            # the adapter built one; everything else uses `plain`. The two
            # never share a row (X27 checks the compile row exists).
            form = cp.form_for_regime(regime)
            cr = cp.get(form)
            if cr is None or cr.outcome != "compiled":
                continue
            handle = dict(cr.handle)
            handle["pin"] = quiet.taskset_prefix(pinning)
            handle["subject_timeout"] = subject_timeout
            if iters is None:
                say("calibrating %s / %s / %s ..." % (testee_id, p.name, regime))
            n_iters, why, cal = calibrate(adapter, handle, regime, subjects,
                                          iters, driver_timeout,
                                          subject_timeout, budget=budget)
            # The routine calibration ("median per-iteration X -> iters=N")
            # is NOT a note: every row's `calibration` block and
            # `timing.iterations` carry it, and one sentence per (pattern,
            # form, regime) blew the schema's free_text cap on a 24-pattern
            # set (record.FREE_TEXT_MAX says when). Only a calibration that
            # did NOT meet its target is worth a sentence a reader sees first.
            if cal is not None and cal.get("calibration_note"):
                notes.append("calibration for (%s, %s, %s) = %d iters: %s"
                             % (p.name, form, regime, n_iters, why))
            say("measuring %s / %s [%s] / %s: %d subject(s) x %d iter(s) x %d "
                "trial(s)" % (testee_id, p.name, form, regime, len(subjects),
                              n_iters, trials))
            rows_by_trial, _info, mnotes = adapter.measure(
                handle, regime, subjects, n_iters, trials,
                timeout=driver_timeout)
            notes.extend(mnotes)

            enum = REGIME_TO_ENUM[regime]
            for trial, trial_rows in enumerate(rows_by_trial, start=1):
                for r in trial_rows:
                    subj = sb.subject(r.subject_id)
                    subject_ids[r.subject_id] = subj
                    exp = sb.expectation(p.name, r.subject_id, regime)
                    outcome, observed, diag = outcome_for(
                        r, exp, regime, subj,
                        giveup_ok=classify_giveup(r.answer, handle))
                    timing = None
                    if outcome == "matched-as-expected":
                        timing = {
                            "elapsed_ns": int(round(r.seconds * 1e9)),
                            "iterations": max(int(r.iters), 1),
                            "bytes_processed": subj.length * max(int(r.iters), 1),
                        }
                    rows.append(record.match_row(
                        p.name, r.subject_id, enum, trial, outcome,
                        timing=timing, consumed=r.consumed,
                        truncation=truncation_for(regime, r, subj),
                        observed=observed, diagnostic=diag,
                        seq=next(seq), form=form,
                        # X21: a calibration belongs on a row whose loop ran
                        # more than once. A one-iteration loop was never
                        # calibrated and does not claim to have been.
                        calibration=(cal if timing and
                                     timing["iterations"] > 1 else None)))

    # (4) load AND OCCUPANCY after ------------------------------------------
    # Both instruments, at both ends, by the same call that took the before
    # sample. A box that was quiet at the start and got busy partway through
    # is just as load-compromised (requirements 9(a), C7) -- and the measured
    # finding of docs/design/quiet_baseline.md is that the instrument which
    # actually notices that is the per-core one, not load1.
    say("re-checking the box after the run (mpstat takes ~1 s)...")
    load_after, occ_after = quiet.check(exclude_cpu=pin_cpu)
    environment["load"] = quiet.load_block(load_before, load_after)
    # `limit_busy_pct` travels WITH the samples (X26): the verdict on each is
    # recomputed from its own number against this threshold, so a threshold
    # change is re-judgeable later without re-measuring.
    occ = quiet.occupancy_block(occ_before, occ_after)
    environment["occupancy"] = occ

    # (5) the record --------------------------------------------------------
    # `measured` requires BOTH ends clean, on BOTH instruments. `occ` already
    # carries the WORSE of the two occupancy samples, so this reads as one
    # test and enforces two.
    status = "measured"
    if environment["load"]["verdict"] != "quiet":
        status = "inconclusive-load"
    occ_ok, occ_reasons = quiet.occupancy_ok(occ)
    if not occ_ok:
        status = "inconclusive-load"
        notes.extend(occ_reasons)
        if occ_before["verdict"] != occ_after["verdict"]:
            notes.append("occupancy differed across the run: before=%s "
                         "after=%s -- the box changed while it was measured"
                         % (occ_before["verdict"], occ_after["verdict"]))
    driver_flags, driver_cc = driverrun.driver_build_provenance()
    run_block = {
        # `run.run_id` is a schema SLUG (lowercase), so the stamp is
        # lowercased -- the id shared by every record of one invocation.
        "run_id": ("run-%s-%d" % (time.strftime("%Y%m%dt%H%M%Sz",
                                                time.gmtime()), os.getpid())).lower(),
        "timestamp": timestamp,
        "harness_version": HARNESS_VERSION,
        "harness_commit": _git_commit(),
        "command_line": list(command_line or sys.argv),
        "env": {k: v for k, v in os.environ.items()
                if k in ("CC", "CFLAGS", "LC_ALL", "PCRECBENCH_BUILD_ROOT")},
        # v1.1 (6)+(9). Built always; emitted when the schema has a home.
        "driver_build_flags": driver_flags,
        "driver_compiler": driver_cc,
        "clock_source": record.CLOCK_SOURCE,
    }

    setup = record.build_setup(
        sb, testee_block, environment, run_block,
        [REGIME_TO_ENUM[r] for r in regimes],
        [record.pattern_entry(sb, p.name) for p in cell_patterns],
        [record.subject_entry(subject_ids[k]) for k in sorted(subject_ids)],
        status,
        status_detail=(record.join_notes(notes)
                       if notes and status != "measured" else None),
        note=note)
    if synthetic:
        setup["synthetic"] = True
    # Stamped on EVERY record, both tiers: absent means pinned by the schema,
    # but a record that says which tier it is beats one that implies it.
    setup["tier"] = tier
    if notes and "status_detail" not in setup:
        setup["note"] = record.join_notes(notes, prefix=note)

    # (6)+(7) write and index ----------------------------------------------
    # PROJECT to the emitted schema version LAST, so everything above worked
    # with the full-fidelity record and only the write is versioned.
    full = (setup, rows)
    path, rid = store.write(store_root, setup, rows)
    store.index(store_root)
    return RunResult(path, rid, setup, rows, full)


def _git_commit():
    import subprocess
    try:
        out = subprocess.run(["git", "rev-parse", "HEAD"], cwd=store.REPO_ROOT,
                             capture_output=True, text=True, timeout=30)
        c = (out.stdout or "").strip()
        return c if len(c) == 40 else "unknown"
    except (OSError, subprocess.SubprocessError):
        return "unknown"
