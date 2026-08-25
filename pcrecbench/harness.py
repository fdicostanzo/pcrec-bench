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
              subject_timeout):
    """Choose `iters`. -> (iters, why, calibration).

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
    actually used lands in every row's `timing.iterations`."""
    target_ns = int(TARGET_LOOP_SECONDS * 1e9)
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
    probe_elapsed_ns = int(round(sum(r.seconds for r in rows) * 1e9))
    cal = {"target_ns": target_ns, "probe_iterations": probe_iters,
           "probe_elapsed_ns": probe_elapsed_ns}
    if requested is not None:
        # A FIXED count still gets a REAL probe, because X21 compares the
        # probe against the target and a fabricated probe would be a number
        # with nothing behind it. The note says the count was not derived.
        cal["calibration_note"] = (
            "iterations fixed at %d on the command line; the probe was run "
            "for provenance and did not choose the count" % int(requested))
        return int(requested), "requested on the command line", cal
    per_iter = sorted(r.seconds / max(r.iters, 1) for r in rows
                      if r.seconds > 0 and r.iters)
    if not per_iter:
        cal["calibration_note"] = ("the probe produced no usable timing, so "
                                   "the count fell back to 1")
        return 1, "the probe run produced no timing; falling back to iters=1", cal
    median = per_iter[len(per_iter) // 2]
    total = sum(per_iter)
    iters = max(1, int(TARGET_LOOP_SECONDS / median))
    capped = max(1, int(TRIAL_BUDGET_SECONDS / total)) if total > 0 else iters
    if capped < iters:
        why = ("median subject would need iters=%d for %.0f ms, capped to %d "
               "by the %.0f s per-trial budget"
               % (iters, TARGET_LOOP_SECONDS * 1000, capped,
                  TRIAL_BUDGET_SECONDS))
        # X21: the target was NOT met, and the record must say why rather
        # than leave a reader to infer it from two numbers.
        cal["calibration_note"] = why
        return capped, why, cal
    return iters, ("median per-iteration %.3f us over %d subject(s) -> "
                   "iters=%d for a %.0f ms loop"
                   % (median * 1e6, len(per_iter), iters,
                      TARGET_LOOP_SECONDS * 1000)), cal


# ----------------------------------------------------------------- the run

def run_cell(subbench_name, testee_id, regimes=None, trials=5, iters=None,
             force_unquiet=False, store_root=None, machine_id=None,
             pin_cpu=None, subject_timeout=60, driver_timeout=900,
             command_line=None, note=None, synthetic=False, workdir=None,
             progress=None):
    """The whole of contract 4. Returns a `RunResult`.

    It carries BOTH the record as written and the FULL pre-projection one, so
    a caller (and `make check`) can see that the v1.1 fields are really being
    measured rather than merely provided for. A projection nobody can inspect
    is a projection nobody can tell is dead."""
    from .subbench import find as find_subbench

    say = progress or (lambda *_a: None)
    store_root = store_root or store.DEFAULT_STORE

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

    adapter, cfg = _ad.resolve(testee_id)

    # (2) the quiet gate ----------------------------------------------------
    say("checking the box (mpstat takes ~1 s)...")
    load_before, occ_before = quiet.check(exclude_cpu=pin_cpu)
    reasons = quiet.gate(load_before, occ_before, force=force_unquiet)
    pinning = quiet.pinning(pin_cpu)

    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    environment = env.describe(store_root, machine_id=machine_id,
                               timestamp=timestamp)
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

    notes = list(reasons)
    rows = []
    compiled = {}
    # v1.1 (1): a monotonic emission order across the WHOLE record, compile
    # and match rows alike. Row order is not significant to the schema, so
    # without this the sequence a harness actually ran things in -- which is
    # what a thermal-drift or warm-up question needs -- is unrecoverable.
    seq = itertools.count(1)
    options = (sb.testee_notes.get(adapter.name, {}) or {}).get("options", {})

    for p in sb.patterns:
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
    for p in sb.patterns:
        cp = compiled.get(p.name)
        if cp is None:
            continue
        for regime in regimes:
            subjects = sb.subjects_for(regime)
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
                                          subject_timeout)
            notes.append("iters for (%s, %s, %s) = %d: %s"
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
        [record.pattern_entry(sb, p.name) for p in sb.patterns],
        [record.subject_entry(subject_ids[k]) for k in sorted(subject_ids)],
        status,
        status_detail="; ".join(notes) if notes and status != "measured" else None,
        note=note)
    if synthetic:
        setup["synthetic"] = True
    if notes and "status_detail" not in setup:
        setup["note"] = "; ".join(notes) if not note else note + " | " + "; ".join(notes)

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
