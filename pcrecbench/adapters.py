"""adapters.py -- the Adapter interface, testee discovery, and THE DRIVER
PROTOCOL (harness contract 3).

=============================================================================
THE DRIVER PROTOCOL
=============================================================================

Both drivers implement exactly this, so that a difference between two
engines' numbers is the ENGINE and not the harness. A third driver copies the
shape, not the engine.

INVOCATION
    driver --pattern FILE          the canonical pattern, RAW BYTES
           --list SUBJECTS.tsv     `id<TAB>path` per line, no header
           --mode search|match     search = unanchored from offset 0;
                                   match  = whole-subject (anchored AND
                                            end-anchored)
           --iters N               iterations of the per-subject operation
           [--find-all]            search mode only: loop the whole subject
                                   counting NON-OVERLAPPING matches with
                                   `pos = max(end, pos+1)`. This is the
                                   throughput regime's operation, and the
                                   count is what its expectation states.
           [--compile-trials T]    compile T times, timing every phase; T-1
                                   of them are thrown away except for their
                                   timings (default 1)
           [--subject-timeout S]   per-SUBJECT alarm, seconds (0 = none)
           [--skip N]              start at the Nth subject of the list
                                   (how python RESUMES after a driver death)

    The driver reads EVERY subject into memory first, compiles once (timed,
    per phase), then for each subject takes one monotonic clock reading,
    loops `iters` times, and takes another. Never a clock per call and never
    an external per-call wrapper: this box's `timeout` alone costs ~108.7 ms
    per call (requirements 3, C5), which at these sizes is the whole signal.

OUTPUT -- TSV on stdout, LINE-BUFFERED (python reads it as a liveness and
crash-attribution channel, so a buffered driver would lose the attribution):

    info<TAB>NAME<TAB>VALUE
        engine facts probed from the library/artifact. `version` is
        mandatory. Everything else becomes `engine_metadata` if the
        adapter DECLARES it (record_schema.md 7 rule 1).

    compile<TAB>TRIAL<TAB>PHASE<TAB>SECONDS
        one line per phase per trial, TRIAL 1-based. (The contract sketched
        a 3-column `compile PHASE SECONDS`; the trial number is added
        because the record keeps RAW trials -- record_schema.md X9 requires
        dense 1..N per pattern, and a parser counting repeats to recover the
        number would silently mis-attribute a phase the driver skipped.)

    subject<TAB>ID<TAB>ANSWER<TAB>START<TAB>END<TAB>NCAPS<TAB>CONSUMED<TAB>ITERS<TAB>SECONDS<TAB>NMATCHES<TAB>CAPS
        ANSWER   match | nomatch | giveup:<code> | timedout | error:<text>
        START,END  the FIRST match's span, or `-`
        NCAPS    capture slots the engine delivered (0 when none)
        CONSUMED subject bytes the engine was given and accepted, or `-`
                 when the API does not expose it (each adapter's CLAUDE.md
                 states its convention -- requirements 4.4, A7)
        ITERS    the loop's N as actually run
        SECONDS  wall seconds for the WHOLE loop (%.9f)
        NMATCHES non-overlapping match count under --find-all, else `-`
        CAPS     `s:e,s:e,...` 1-based groups, `-1:-1` unset, or `-`
        (The contract's column list omitted CAPS and NMATCHES; contract 3
        requires `caps` in what measure() returns, and the throughput
        expectation IS a count, so both are columns rather than a second
        protocol.)

    error<TAB>TEXT     a fatal the driver could not attribute to a subject

EXIT   0 all subjects reported; 2 usage/IO; 3 the pattern did not compile
       (with `error` lines carrying the engine's diagnostic).

TIMEOUTS come in two layers and they measure different things. The
per-SUBJECT alarm inside the driver is what makes record_schema.md's
per-subject `timed-out` possible at all -- requirements 4.4 wants to know
WHICH subject hung. `gnutimeout` on the driver PROCESS is the outer
backstop for a driver that hangs somewhere else (requirements 3).
"""

import importlib.util
import os
import tomllib

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTEES_ROOT = os.path.join(REPO_ROOT, "testees")


class AdapterError(Exception):
    pass


class CompileResult:
    """What `Adapter.compile()` returns for ONE pattern.

    `phase_seconds` is `[{phase: seconds, ...}, ...]`, one dict per trial, in
    trial order; `engine_metadata` is the `pattern`-scoped pairs
    (record_schema.md 7 rule 2); `handle` is whatever `measure()` needs and
    is opaque to the harness."""

    __slots__ = ("outcome", "diagnostic", "phase_seconds", "engine_metadata",
                 "handle", "artifact_bytes", "declaration_ref")

    def __init__(self, outcome, phase_seconds=None, diagnostic=None,
                 engine_metadata=None, handle=None, artifact_bytes=None,
                 declaration_ref=None):
        self.outcome = outcome
        self.phase_seconds = phase_seconds or []
        self.diagnostic = diagnostic
        self.engine_metadata = engine_metadata or {}
        self.handle = handle
        self.artifact_bytes = artifact_bytes
        self.declaration_ref = declaration_ref


class MatchRow:
    """One driver `subject` line, parsed. The harness -- not the adapter --
    turns `answer` into a `match_outcome` against the sub-bench's
    expectation: an adapter that judged its own correctness would be
    marking its own homework."""

    __slots__ = ("subject_id", "answer", "start", "end", "ncaps", "consumed",
                 "iters", "seconds", "nmatches", "caps", "detail")

    def __init__(self, subject_id, answer, start=None, end=None, ncaps=0,
                 consumed=None, iters=0, seconds=0.0, nmatches=None,
                 caps=None, detail=None):
        self.subject_id, self.answer = subject_id, answer
        self.start, self.end, self.ncaps = start, end, ncaps
        self.consumed, self.iters, self.seconds = consumed, iters, seconds
        self.nmatches, self.caps, self.detail = nmatches, caps, detail

    @property
    def matched(self):
        return self.answer == "match"

    @property
    def is_giveup(self):
        return self.answer.startswith("giveup")


def _opt(v):
    return None if v in ("-", "", None) else v


def parse_driver_line(line):
    """-> ('subject', MatchRow) | ('compile', (trial, phase, seconds))
         | ('info', (name, value)) | ('error', text) | (None, line)"""
    cols = line.rstrip("\n").split("\t")
    if not cols:
        return None, line
    kind = cols[0]
    if kind == "subject":
        if len(cols) < 11:
            return None, line
        (_, sid, answer, start, end, ncaps, consumed, iters, seconds,
         nmatches, caps) = cols[:11]
        return "subject", MatchRow(
            sid, answer,
            start=None if _opt(start) is None else int(start),
            end=None if _opt(end) is None else int(end),
            ncaps=int(ncaps or 0),
            consumed=None if _opt(consumed) is None else int(consumed),
            iters=int(iters or 0), seconds=float(seconds or 0.0),
            nmatches=None if _opt(nmatches) is None else int(nmatches),
            caps=_opt(caps))
    if kind == "compile" and len(cols) >= 4:
        return "compile", (int(cols[1]), cols[2], float(cols[3]))
    if kind == "info" and len(cols) >= 3:
        # a value may itself contain tabs; the NAME never does.
        return "info", (cols[1], "\t".join(cols[2:]))
    if kind == "error":
        return "error", "\t".join(cols[1:])
    return None, line


# ------------------------------------------------------------------ Adapter

class Adapter:
    """Harness contract 3. Subclasses live in `testees/<name>/adapter.py` and
    are found by `discover()`."""

    name = None

    def __init__(self, directory):
        self.dir = directory
        cfg_path = os.path.join(directory, "configs.toml")
        if not os.path.exists(cfg_path):
            raise AdapterError("no configs.toml in %s" % directory)
        with open(cfg_path, "rb") as f:
            self.cfg = tomllib.load(f)

    # ---- the interface -----------------------------------------------

    def testees(self):
        """id -> config dict, from `configs.toml`'s `[testees.<id>]`."""
        return dict(self.cfg.get("testees", {}))

    def config(self, testee_id):
        try:
            return self.testees()[testee_id]
        except KeyError:
            raise AdapterError(
                "%s provides no testee %r (have: %s)"
                % (self.name, testee_id, ", ".join(sorted(self.testees()))))

    def describe(self, testee_id, workdir=None):
        """The record's `testee` block, every field, versions PROBED."""
        raise NotImplementedError

    def prepare(self, testee_id, workdir):
        """Build the driver / resolve the pin. Idempotent."""
        raise NotImplementedError

    def compile(self, testee_id, pattern_id, pattern, options, trials, workdir):
        """-> CompileResult.

        `pattern_id` is passed so each pattern gets its OWN scratch under
        `workdir`. It is not decoration: a sub-bench has several patterns, the
        harness compiles them ALL before measuring any, and an adapter that
        wrote `workdir/pattern.rx` or `workdir/artifact.so` would have the
        last pattern's artifact under the first pattern's handle. That bug
        was written, and it was invisible on this sub-bench because its two
        patterns agree on every subject -- so the interface makes it
        unwriteable instead of relying on an adapter author to remember."""
        raise NotImplementedError

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        """-> (rows_by_trial, info, notes).

        `rows_by_trial` is one list of MatchRow per TRIAL (contract 3: the
        driver runs once per (regime, trial)); `info` is the driver's `info`
        pairs; `notes` are harness-level remarks -- a driver restart, a
        subject with no outcome -- that land in the record's `status_detail`
        rather than being swallowed."""
        raise NotImplementedError


# ---------------------------------------------------------------- discovery

def _load_module(path, modname):
    spec = importlib.util.spec_from_file_location(modname, path)
    if spec is None or spec.loader is None:
        raise AdapterError("cannot load %s" % path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def discover(root=None):
    """-> {engine_name: Adapter}. Imports every `testees/*/adapter.py`."""
    root = root or TESTEES_ROOT
    out = {}
    if not os.path.isdir(root):
        return out
    for entry in sorted(os.listdir(root)):
        path = os.path.join(root, entry, "adapter.py")
        if not os.path.exists(path):
            continue
        mod = _load_module(path, "pcrecbench_testee_" + entry)
        cls = getattr(mod, "Adapter", None)
        if cls is None:
            raise AdapterError("%s defines no class Adapter" % path)
        out[entry] = cls(os.path.join(root, entry))
    return out


def resolve(testee_id, root=None):
    """-> (Adapter, config) for a testee id, searching every adapter."""
    adapters = discover(root)
    for a in adapters.values():
        if testee_id in a.testees():
            return a, a.testees()[testee_id]
    known = sorted(t for a in adapters.values() for t in a.testees())
    raise AdapterError("no adapter provides testee %r (have: %s)"
                       % (testee_id, ", ".join(known) or "<none>"))


def all_testees(root=None):
    out = {}
    for name, a in discover(root).items():
        for tid, cfg in a.testees().items():
            out[tid] = (name, cfg)
    return out
