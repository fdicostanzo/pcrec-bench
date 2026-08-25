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

import os
import sys
import time

from . import adapters as _ad
from . import env, quiet, record, store
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


# ------------------------------------------------------------- the judging

def outcome_for(row, expectation, regime, subject):
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
        return ("did-not-match-as-expected",
                {"matched": False, "span": None, "captures": None},
                "the engine gave up rather than answering: %s" % row.answer)
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
    """Choose `iters` (contract 3: "chosen so one subject's loop is >= 50 ms,
    auto-calibrated by python from a probe run, recorded in the record").

    THE RULE, because "one subject" needs saying which. The probe measures
    every subject at a small fixed `iters`; the MEDIAN per-iteration cost sets
    the number, so the median subject's loop reaches the target. Calibrating
    on the fastest subject would multiply the slowest one's cost by orders of
    magnitude; calibrating on the slowest would leave the fast ones under the
    clock's resolution. The chosen `iters` is then capped so the PREDICTED
    total sweep stays inside TRIAL_BUDGET_SECONDS -- one pathological subject
    must not turn a cell into an overnight run -- and the number that was
    actually used lands in every row's `timing.iterations`."""
    if requested is not None:
        return int(requested), "requested on the command line"
    probe_iters = PROBE_ITERS.get(regime, 100)
    rows_by_trial, _info, _notes = adapter.measure(
        handle, regime, subjects, probe_iters, 1, timeout=timeout)
    rows = rows_by_trial[0] if rows_by_trial else []
    per_iter = sorted(r.seconds / max(r.iters, 1) for r in rows
                      if r.seconds > 0 and r.iters)
    if not per_iter:
        return 1, "the probe run produced no timing; falling back to iters=1"
    median = per_iter[len(per_iter) // 2]
    total = sum(per_iter)
    iters = max(1, int(TARGET_LOOP_SECONDS / median))
    capped = max(1, int(TRIAL_BUDGET_SECONDS / total)) if total > 0 else iters
    if capped < iters:
        return capped, ("median subject would need iters=%d for %.0f ms, "
                        "capped to %d by the %.0f s per-trial budget"
                        % (iters, TARGET_LOOP_SECONDS * 1000, capped,
                           TRIAL_BUDGET_SECONDS))
    return iters, ("median per-iteration %.3f us over %d subject(s) -> "
                   "iters=%d for a %.0f ms loop"
                   % (median * 1e6, len(per_iter), iters,
                      TARGET_LOOP_SECONDS * 1000))


# ----------------------------------------------------------------- the run

def run_cell(subbench_name, testee_id, regimes=None, trials=5, iters=None,
             force_unquiet=False, store_root=None, machine_id=None,
             pin_cpu=None, subject_timeout=60, driver_timeout=900,
             command_line=None, note=None, synthetic=False, workdir=None,
             progress=None):
    """The whole of contract 4. Returns (path, record_id, setup, rows)."""
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
    load_before, occ = quiet.check(exclude_cpu=pin_cpu)
    reasons = quiet.gate(load_before, occ, force=force_unquiet)
    pinning = quiet.pinning(pin_cpu)

    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    environment = env.describe(store_root, machine_id=machine_id,
                               timestamp=timestamp)
    environment["pinning"] = pinning
    environment["occupancy"] = occ
    environment["quiet_attestation"] = not reasons

    # (3) prepare, compile, measure ----------------------------------------
    workdir = workdir or os.path.join(store.REPO_ROOT, "build", "work",
                                      testee_id)
    os.makedirs(workdir, exist_ok=True)
    say("preparing %s ..." % testee_id)
    adapter.prepare(testee_id, workdir)
    testee_block = adapter.describe(testee_id, workdir)

    notes = list(reasons)
    rows = []
    handles = {}
    compiled_ok = {}
    options = (sb.testee_notes.get(adapter.name, {}) or {}).get("options", {})

    for p in sb.patterns:
        say("compiling %s / %s (%d trial(s)) ..." % (testee_id, p.name, trials))
        cr = adapter.compile(testee_id, sb.pattern_bytes(p.name), options,
                             trials, workdir)
        compiled_ok[p.name] = (cr.outcome == "compiled")
        phases = testee_block["compile_phases"]
        n = len(cr.phase_seconds) if cr.outcome == "compiled" else 1
        for t in range(1, max(n, 1) + 1):
            ps = cr.phase_seconds[t - 1] if t - 1 < len(cr.phase_seconds) else None
            rows.append(record.compile_row(
                p.name, t, cr.outcome, testee_block["execution_model"],
                phases=phases, phase_seconds=ps,
                engine_metadata=cr.engine_metadata,
                diagnostic=cr.diagnostic,
                artifact_bytes=cr.artifact_bytes,
                declaration_ref=cr.declaration_ref))
        if cr.outcome == "compiled":
            handles[p.name] = cr.handle
        else:
            notes.append("%s did not compile %s: %s"
                         % (testee_id, p.name, cr.diagnostic))

    subject_ids = {}
    for p in sb.patterns:
        if p.name not in handles:
            continue
        for regime in regimes:
            subjects = sb.subjects_for(regime)
            if not subjects:
                continue
            handle = dict(handles[p.name])
            handle["pin"] = quiet.taskset_prefix(pinning)
            handle["subject_timeout"] = subject_timeout
            if iters is None:
                say("calibrating %s / %s / %s ..." % (testee_id, p.name, regime))
            n_iters, why = calibrate(adapter, handle, regime, subjects, iters,
                                     driver_timeout, subject_timeout)
            notes.append("iters for (%s, %s) = %d: %s" % (p.name, regime,
                                                          n_iters, why))
            say("measuring %s / %s / %s: %d subject(s) x %d iter(s) x %d "
                "trial(s)" % (testee_id, p.name, regime, len(subjects),
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
                    outcome, observed, diag = outcome_for(r, exp, regime,
                                                         subj)
                    timing = None
                    if outcome == "matched-as-expected" and compiled_ok[p.name]:
                        timing = {
                            "elapsed_ns": int(round(r.seconds * 1e9)),
                            "iterations": max(int(r.iters), 1),
                            "bytes_processed": subj.length * max(int(r.iters), 1),
                        }
                    rows.append(record.match_row(
                        p.name, r.subject_id, enum, trial, outcome,
                        timing=timing, consumed=r.consumed,
                        truncation=truncation_for(regime, r, subj),
                        observed=observed, diagnostic=diag))

    # (4) load AFTER --------------------------------------------------------
    load_after = quiet.loadavg()
    environment["load"] = quiet.load_block(load_before, load_after)

    # (5) the record --------------------------------------------------------
    status = "measured"
    if environment["load"]["verdict"] != "quiet" or occ["verdict"] == "fail":
        status = "inconclusive-load"
    if occ["verdict"] == "unavailable" and not force_unquiet:
        status = "inconclusive-load"
    if not all(compiled_ok.values()):
        # X14: `measured` requires a compile row for every pattern -- there
        # IS one, saying it did not compile, so the record stays honest and
        # `measured` still means "the run completed".
        pass

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
    path, rid = store.write(store_root, setup, rows)
    store.index(store_root)
    return path, rid, setup, rows


def _git_commit():
    import subprocess
    try:
        out = subprocess.run(["git", "rev-parse", "HEAD"], cwd=store.REPO_ROOT,
                             capture_output=True, text=True, timeout=30)
        c = (out.stdout or "").strip()
        return c if len(c) == 40 else "unknown"
    except (OSError, subprocess.SubprocessError):
        return "unknown"
