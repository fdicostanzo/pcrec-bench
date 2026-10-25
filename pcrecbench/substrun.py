"""substrun.py -- the SUBSTITUTION regime's cell logic ([B140],
docs/design/subst_bench_v1.md 3.1, 3.1.1, 3.1.2, 4; record schema v1.9,
record_schema.md 6.12).

ENGINE-NEUTRAL BY CONSTRUCTION (R-BENCH-4). Nothing here names an engine: a
testee is whatever its adapter's `subst_support()` says (a template dialect, the
name its divergence rows use) and whatever its `measure_subst()` returns (one
trial of `--mode subst`, one `MatchRow` per subject with the `out` line's
path and length attached). The harness (`harness.run_cell`) calls two
functions in here:

  plan_case()     per case, BEFORE compiling: render the neutral template in
                  the testee's dialect, consult the set's divergences.tsv, and
                  say either "unsupported, here is the token and the citation"
                  (a compile row `unsupported-by-declaration`, X44, and NO
                  match rows) or "run it, with this template and these flags".
  measure_cell()  per supported case: for each subject, for each trial, one
                  driver run; the correctness gate on trial 1's output;
                  trials 2..N checked by output length and substitution count.
                  Returns the rows' content; the harness stamps `seq` and the
                  record shape.

THE GATE (subst_bench_v1.md 4). The sha256 of the output is taken ONCE per
(cell, subject, case), on trial 1's output file, outside every clock, and
compared with bench/<set>/expectations.tsv's. Equal -> `agrees`
(`matched-as-expected`, timed). Different -> `divergent-declared` iff the
set's divergence table says so for this (case, testee), else `wrong`
(`did-not-match-as-expected`, NEVER timed -- X11/X37) with the first
differing byte offset and both lengths from a lazily recomputed oracle
output. A wrong cell stops after trial 1 (the remaining trials are not run:
"a competitor that fails the gate is not timed for that case"); its other
trials' rows repeat trial 1's, because X43 wants the cell's identity constant
across trials and the trial numbering dense.

TRIALS 2..N never write a file (the driver is not given --out-dir): they are
checked against trial 1 by BYTES and NMATCHES. A difference is a DETERMINISM
FAULT, by name, and is raised -- nothing is written, because no record could
carry two different "validated outputs" for one cell (X43).

A SCHEMA GAP, stated where it bites. `match.subst` is REQUIRED on every
`substitution` row (X36) and "describes the VALIDATED output", but a row
whose outcome is `gave-up` / `crashed` / `timed-out` has no output to
describe. Such a row carries PLACEHOLDERS -- gate `wrong`, nsubst 0,
out_bytes 0, out_sha256 = sha256(b"") -- and says so in its `diagnostic`.
The placeholders are never read as an output (the outcome is not
`matched-as-expected`); the proper fix is the schema owner's (make the
object optional for outcomes that produced no output, or add a gate value),
and it is on the b140drv report's list.
"""

import hashlib
import os
import shutil
import tempfile

from . import subst_template as st

EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
OUT_ROOT_DEFAULT = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "build", "subst-out")


class SubstError(Exception):
    """A substitution-tier failure the harness turns into a HarnessError."""


class DeterminismFault(SubstError):
    """Trial k's output length or substitution count differs from trial 1's."""


def out_root():
    """Where trial 1's output files go: `$PCRECBENCH_SUBST_OUT` (a 360 MB
    output belongs under /var/tmp/pcrecbench/<lane>/, never /tmp) or
    `build/subst-out/`."""
    root = os.environ.get("PCRECBENCH_SUBST_OUT") or OUT_ROOT_DEFAULT
    os.makedirs(root, exist_ok=True)
    return root


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


# ------------------------------------------------------------------ planning

class CasePlan:
    """What the harness needs to compile (or not) and measure one case."""

    __slots__ = ("case", "template", "flags", "unsupported", "declaration_ref",
                 "template_file")

    def __init__(self, case, template=None, flags="none", unsupported=None,
                 declaration_ref=None):
        self.case, self.template, self.flags = case, template, flags
        self.unsupported = unsupported          # None, or a diagnostic string
        self.declaration_ref = declaration_ref
        self.template_file = None       # set by write_template()


def write_template(plan, directory):
    """Put the rendered template on disk (RAW BYTES, no trailing newline added)
    for the driver's `--template FILE`; returns the path."""
    if plan.template is None:               # an unsupported case: nothing to run
        return None
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "template")
    with open(path, "wb") as f:
        f.write(plan.template)
    plan.template_file = path
    return path


def plan_case(sb, p, support, template_override=None):
    """-> CasePlan for pattern `p` (a substitution case) and a testee whose
    adapter answered `support` ({"dialect", "competitor", ...}).

    The two sources of "unsupported" must AGREE: the renderer raising
    `Unsupported` for a construct the dialect cannot spell, and the set's
    divergences.tsv row for (case, competitor) saying `unsupported:<token>`.
    A table that says the testee `agrees` while the renderer cannot spell the
    template (or the reverse for the renderer's own tokens) is a broken set,
    raised by name -- never resolved silently in either direction.
    `template_override` (bytes of IR source) lets the gate's negative control
    run a deliberately wrong template through the SAME path."""
    case = p.case
    ir_src = template_override if template_override is not None \
        else sb.template_bytes(p.name)
    ir = st.parse(ir_src)
    row = sb.divergence(case, support["competitor"])
    declared = None
    if row is not None and row[0].startswith("unsupported:"):
        declared = (row[0].split(":", 1)[1], row[1], row[3])
    try:
        rendered = st.render(ir, support["dialect"])
        token = None
    except st.Unsupported as e:
        rendered, token = None, e.token
    if token is not None and declared is None:
        raise SubstError(
            "case %s: the %s dialect cannot spell the template (%s) but "
            "divergences.tsv has no `unsupported:` row for (%s, %s) -- the "
            "table and the renderer disagree"
            % (case, support["dialect"], token, case, support["competitor"]))
    if declared is not None:
        if token is not None and token != declared[0]:
            raise SubstError(
                "case %s: divergences.tsv says unsupported:%s but the "
                "renderer's token is %s" % (case, declared[0], token))
        return CasePlan(case, unsupported="declared unsupported (%s): %s"
                        % (declared[0], declared[1]),
                        declaration_ref=declared[2])
    if isinstance(rendered, str):
        rendered = rendered.encode("latin-1")
    return CasePlan(case, template=rendered,
                    flags="extended" if st.needs_extended(ir) else "none")


# ------------------------------------------------------------------ diagnosis

def diagnose_wrong(sb, p, plan, subj, support_dialect, out_path):
    """The first differing byte offset and both lengths against the oracle's
    own output, with a short window either side (subst_bench_v1.md 4.2).
    Recomputed lazily -- only on the failure path -- through the SAME oracle
    entry point that wrote expectations.tsv."""
    from . import oracle_pcre2 as oracle
    with open(subj.path, "rb") as f:
        data = f.read()
    ir = st.parse(sb.template_bytes(p.name))
    tpl = st.render(ir, "pcre2", extended=st.needs_extended(ir))
    _n, want = oracle.compile(sb.pattern_bytes(p.name)).substitute(
        data, tpl, extended=st.needs_extended(ir))
    want = bytes(want)
    with open(out_path, "rb") as f:
        got = f.read()
    n = min(len(got), len(want))
    off = next((i for i in range(0, n, 1 << 16)
                if got[i:i + (1 << 16)] != want[i:i + (1 << 16)]), None)
    if off is None:
        off = n
    else:
        end = min(off + (1 << 16), n)
        off = next(i for i in range(off, end) if got[i] != want[i]) \
            if got[off:end] != want[off:end] else end
    lo = max(off - 60, 0)
    return ("output differs from the oracle's at byte %d; observed %d bytes, "
            "expected %d; observed[%d:%d]=%r expected[%d:%d]=%r"
            % (off, len(got), len(want), lo, off + 60, got[lo:off + 60],
               lo, off + 60, want[lo:off + 60]))


# ------------------------------------------------------------------ measuring

def _placeholder(case):
    return {"case": case, "gate": "wrong", "nsubst": 0, "out_bytes": 0,
            "out_sha256": EMPTY_SHA256}


def measure_cell(adapter, handle, sb, p, plan, support, subjects, trials,
                 driver_timeout, classify_giveup, say=None):
    """Measure case `p` over `subjects` for `trials` trials -> (entries, notes).

    An entry is a dict with the keys the harness hands `record.match_row`:
    subject (a Subject), trial, outcome, timing, consumed, truncation,
    observed, diagnostic, subst. Order: trial-major, subjects in the given
    order within a trial -- the same drift-spreading order the other regimes
    use. `handle` is the compiled-pattern handle (a copy; this function adds
    `handle["subst"]`)."""
    say = say or (lambda *_a: None)
    handle = dict(handle)
    handle["subst"] = {"template_file": plan.template_file, "flags": plan.flags}
    case = plan.case
    exps, bounds = {}, {}
    for s in subjects:
        e = sb.subst_expectation(case, s.subject_id)
        if e is None:
            raise SubstError("no expectation for case %s on subject %s in "
                             "expectations.tsv -- the set must state one "
                             "before the cell can be gated"
                             % (case, s.subject_id))
        exps[s.subject_id] = e
        # 3.1.1: cap = n + 8 * (the oracle's count) + 1 -- an engine-neutral
        # bound; the +1 is libpcre2's terminating NUL (an engine that
        # allocates for itself ignores the number).
        bounds[s.subject_id] = s.length + 8 * e["nsubst"] + 1

    entries, notes = [], []
    first = {}          # subject_id -> trial 1's entry (the cell's identity)
    first_len = {}      # subject_id -> (out_bytes, nmatches) of trial 1
    stopped = set()
    root = out_root()
    for trial in range(1, trials + 1):
        for s in subjects:
            sid = s.subject_id
            if sid in stopped:
                rep = dict(first[sid])
                rep["trial"] = trial
                entries.append(rep)
                continue
            out_dir = tempfile.mkdtemp(prefix="subst-", dir=root) \
                if trial == 1 else None
            try:
                rows, _info, rnotes = adapter.measure_subst(
                    handle, [s], {sid: bounds[sid]}, out_dir,
                    timeout=driver_timeout)
                notes.extend(rnotes)
                row = rows[0] if rows else None
                entry = _judge(sb, p, plan, support, s, exps[sid], row,
                               trial, out_dir, handle, classify_giveup)
            finally:
                if out_dir:
                    shutil.rmtree(out_dir, ignore_errors=True)
            if trial == 1:
                first[sid] = entry
                if entry["subst"]["gate"] != "agrees" \
                        or entry["outcome"] != "matched-as-expected":
                    stopped.add(sid)
                    if trials > 1:
                        notes.append(
                            "case %s on %s: not timed beyond trial 1 (%s)"
                            % (case, sid, entry["outcome"]
                               if entry["outcome"] != "did-not-match-as-expected"
                               else "gate " + entry["subst"]["gate"]))
                first_len[sid] = (entry["subst"]["out_bytes"],
                                  entry["subst"]["nsubst"])
            else:
                want = first_len[sid]
                got = (entry["subst"]["out_bytes"], entry["subst"]["nsubst"])
                if entry["outcome"] != first[sid]["outcome"] or got != want:
                    raise DeterminismFault(
                        "DETERMINISM FAULT: case %s on %s, trial %d: "
                        "outcome %s, output %d bytes / %d substitutions; "
                        "trial 1: %s, %d bytes / %d substitutions. A cell's "
                        "trials must agree on the output (X43); nothing is "
                        "written." % (case, sid, trial, entry["outcome"],
                                      got[0], got[1], first[sid]["outcome"],
                                      want[0], want[1]))
            entries.append(entry)
    return entries, notes


def _judge(sb, p, plan, support, subj, exp, row, trial, out_dir, handle,
           classify_giveup):
    """One driver row -> one entry dict (see measure_cell)."""
    case = plan.case

    def entry(outcome, subst, timing=None, consumed=None, observed=None,
              diagnostic=None, truncation="not-applicable"):
        return {"subject": subj, "trial": trial, "outcome": outcome,
                "timing": timing, "consumed": consumed, "truncation": truncation,
                "observed": observed, "diagnostic": diagnostic, "subst": subst}

    if row is None:
        return entry("crashed", _placeholder(case), diagnostic=(
            "the driver reported no outcome for this subject; subst fields "
            "are placeholders (no output exists)"))
    if row.answer == "timedout":
        return entry("timed-out", _placeholder(case), diagnostic=(
            (row.detail or "the per-subject alarm fired")
            + "; subst fields are placeholders (no output exists)"))
    if row.answer == "crashed":
        return entry("crashed", _placeholder(case), diagnostic=(
            (row.detail or "the driver did not survive")
            + "; subst fields are placeholders (no output exists)"))
    if row.is_giveup or row.answer.startswith("error"):
        giveup = row.is_giveup and classify_giveup(row.answer, handle)
        return entry("gave-up" if giveup else "crashed", _placeholder(case),
                     observed={"matched": False},
                     diagnostic="the engine %s: %s; subst fields are "
                     "placeholders (no output exists)"
                     % ("gave up" if giveup else "failed", row.answer))
    if row.out_bytes is None or row.nmatches is None:
        return entry("crashed", _placeholder(case), diagnostic=(
            "the driver answered %r but reported no `out` line / count; subst "
            "fields are placeholders (no output exists)" % row.answer))
    consumed = row.consumed
    trunc = ("verified" if consumed is not None else "unverified-for-truncation")
    nsubst, nbytes = row.nmatches, row.out_bytes
    if consumed is not None and consumed < subj.length:
        return entry("truncated-subject",
                     {"case": case, "gate": "wrong", "nsubst": nsubst,
                      "out_bytes": nbytes, "out_sha256": EMPTY_SHA256},
                     consumed=consumed, truncation=trunc,
                     observed={"matched": nsubst > 0},
                     diagnostic="offered %d bytes, the engine took %d; "
                     "out_sha256 is a placeholder" % (subj.length, consumed))
    if trial > 1:
        # trials 2..N are checked by length + count only; the hash was taken
        # once, on trial 1's output (3.1.2). The identity fields below are
        # trial 1's by construction (measure_cell compares and raises on any
        # difference), so X43 holds on what is written.
        return entry("matched-as-expected",
                     {"case": case, "gate": "agrees", "nsubst": nsubst,
                      "out_bytes": nbytes, "out_sha256": exp["out_sha256"]},
                     timing={"elapsed_ns": int(round(row.seconds * 1e9)),
                             "iterations": 1, "bytes_processed": subj.length},
                     consumed=consumed, truncation=trunc)
    # ---- trial 1: the gate -------------------------------------------------
    if not row.out_path:
        return entry("crashed", _placeholder(case), diagnostic=(
            "trial 1 reported an output length but wrote no file; subst "
            "fields are placeholders"))
    path = os.path.join(out_dir, row.out_path)
    sha = sha256_file(path)
    if sha == exp["out_sha256"] and nbytes == exp["out_bytes"]:
        return entry("matched-as-expected",
                     {"case": case, "gate": "agrees", "nsubst": nsubst,
                      "out_bytes": nbytes, "out_sha256": sha},
                     timing={"elapsed_ns": int(round(row.seconds * 1e9)),
                             "iterations": 1, "bytes_processed": subj.length},
                     consumed=consumed, truncation=trunc)
    diag = diagnose_wrong(sb, p, plan, subj, support["dialect"], path)
    div = sb.divergence(case, support["competitor"])
    declared = div is not None and div[0].startswith("divergent")
    subst = {"case": case, "gate": "divergent-declared" if declared else "wrong",
             "nsubst": nsubst, "out_bytes": nbytes, "out_sha256": sha}
    if declared:
        subst["declaration_ref"] = div[3]
    return entry("did-not-match-as-expected", subst, consumed=consumed,
                 truncation=trunc, observed={"matched": nsubst > 0},
                 diagnostic="gate %s: %s" % (subst["gate"], diag))
