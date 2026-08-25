"""driverrun.py -- build a driver, run it, parse the protocol, and RESUME
after a driver death.

The protocol itself is specified at the top of `pcrecbench/adapters.py`. This
module is the python half of it, shared by every adapter so that two engines'
numbers come out of the same loop shape.

THE RESUME RULE, which is the only subtle thing here. A driver that dies
mid-list (a crash, or the outer `gnutimeout`) has reported every subject up to
the one that killed it, because the protocol requires line-buffered output.
So the killer is IDENTIFIABLE: it is the first unreported subject. The runner
attributes exactly that outcome to exactly that subject -- `crashed` or
`timed-out`, per record_schema.md 5's ADDITION 1, whose whole point is that
"which subject hung" must be recorded -- and then RESTARTS the driver on the
remainder with `--skip`. It does NOT mark the remainder as crashed: a subject
that was never attempted has no outcome, and inventing one would put the most
alarming value in the record for the least reason.

`MAX_RESTARTS` bounds the loop. A cell that exhausts it stops, and the
subjects still unreported are absent from the record -- which the reporter
sees as coverage below 100% and must show N and pass-rate beside
(requirements 8, B5).
"""

import os
import shutil
import subprocess
import sys
import tempfile

from . import adapters as _ad

MAX_RESTARTS = 8
GNUTIMEOUT = "gnutimeout"

C_ENV = dict(os.environ, LC_ALL="C", LANG="C")


class DriverOutput:
    def __init__(self):
        self.info = {}
        self.rows = []
        self.compile_lines = []
        self.errors = []
        self.returncode = 0
        self.timed_out = False
        self.stderr = ""

    @property
    def phase_seconds(self):
        """-> [{phase: seconds}, ...] indexed by trial-1, dense."""
        by_trial = {}
        for trial, phase, secs in self.compile_lines:
            by_trial.setdefault(trial, {})[phase] = secs
        return [by_trial[t] for t in sorted(by_trial)]

    def diagnostic(self):
        parts = [e for e in self.errors]
        if self.stderr.strip():
            parts.append(self.stderr.strip())
        return "\n".join(parts) or None


def _timeout_argv(seconds):
    """`gnutimeout` on the driver PROCESS (requirements 3/9). NOT the box's
    default `timeout`, which costs ~108.7 ms of wall per call on this box
    (pcrec docs/testing.md:2372) -- irrelevant here because it wraps the whole
    driver rather than a call, but the project uses one spelling everywhere so
    nobody has to remember which is which."""
    if not seconds or shutil.which(GNUTIMEOUT) is None:
        return []
    return [GNUTIMEOUT, "-k", "5", str(int(seconds))]


def run_driver(argv, timeout=None, cwd=None, pin=None):
    """Run one driver invocation to completion and parse its output."""
    out = DriverOutput()
    full = (pin or []) + _timeout_argv(timeout) + list(argv)
    try:
        proc = subprocess.run(full, capture_output=True, text=True,
                              env=C_ENV, cwd=cwd,
                              timeout=(timeout + 30) if timeout else None)
    except subprocess.TimeoutExpired as e:
        out.timed_out = True
        out.returncode = 124
        out.stderr = "python-level timeout: %s" % (e,)
        return out
    out.returncode = proc.returncode
    out.stderr = proc.stderr or ""
    # gnutimeout's own exit code for a killed child (124), and the shell's
    # 128+SIGKILL/SIGTERM, all mean the same thing here.
    out.timed_out = proc.returncode in (124, 137, 143)
    for line in (proc.stdout or "").splitlines():
        kind, payload = _ad.parse_driver_line(line)
        if kind == "subject":
            out.rows.append(payload)
        elif kind == "compile":
            out.compile_lines.append(payload)
        elif kind == "info":
            out.info[payload[0]] = payload[1]
        elif kind == "error":
            out.errors.append(payload)
    return out


def build_driver(source, output, extra=None, cflags=None):
    """Build a driver if the binary is missing or older than its source.

    Returns the binary path. `$CC` and `$CFLAGS` are honoured so the record's
    `environment.compiler` and the driver's actual toolchain are the same
    thing (record_schema.md 6.7)."""
    if (os.path.exists(output)
            and os.path.getmtime(output) >= os.path.getmtime(source)):
        return output
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    cc = os.environ.get("CC", "gcc")
    flags = (cflags or os.environ.get("CFLAGS", "-O2 -std=gnu11")).split()
    argv = [cc] + flags + ["-o", output, source] + list(extra or [])
    proc = subprocess.run(argv, capture_output=True, text=True, env=C_ENV,
                          timeout=600)
    if proc.returncode != 0:
        raise _ad.AdapterError("building %s failed:\n%s\n%s"
                               % (source, " ".join(argv), proc.stderr))
    return output


def write_list(subjects, path):
    """The driver's `--list` file: `id<TAB>abspath` per line, no header."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for s in subjects:
            f.write("%s\t%s\n" % (s.subject_id, os.path.abspath(s.path)))
    return path


def _run_list_with_resume(argv, subjects, timeout, cwd, pin, subject_timeout):
    """One trial over `subjects`, restarting after a driver death. Returns
    (rows, info, notes) with rows in SUBJECT-LIST order, one per subject that
    got an outcome."""
    tmpdir = tempfile.mkdtemp(prefix="pcrecbench-list-")
    try:
        listfile = write_list(subjects, os.path.join(tmpdir, "subjects.tsv"))
        rows, info, notes = [], {}, []
        skip = 0
        for attempt in range(MAX_RESTARTS + 1):
            full = list(argv) + ["--list", listfile]
            if subject_timeout:
                full += ["--subject-timeout", str(int(subject_timeout))]
            if skip:
                full += ["--skip", str(skip)]
            out = run_driver(full, timeout=timeout, cwd=cwd, pin=pin)
            info.update(out.info)
            rows.extend(out.rows)
            done = skip + len(out.rows)
            if done >= len(subjects):
                return rows, info, notes
            if out.returncode == 0 and not out.timed_out:
                notes.append("the driver exited cleanly after %d of %d "
                             "subjects; the remainder have no outcome"
                             % (done, len(subjects)))
                return rows, info, notes
            # the driver died ON the first unreported subject.
            victim = subjects[done]
            answer = "timedout" if out.timed_out else "crashed"
            rows.append(_ad.MatchRow(
                victim.subject_id, answer, iters=0, seconds=0.0,
                detail=(out.diagnostic()
                        or "the driver did not survive this subject "
                           "(exit %s)" % out.returncode)))
            notes.append("subject %s %s the driver (exit %s); restarting at "
                         "the next subject"
                         % (victim.subject_id, answer, out.returncode))
            skip = done + 1
            if skip >= len(subjects):
                return rows, info, notes
        notes.append("gave up after %d driver restarts; %d subject(s) have no "
                     "outcome" % (MAX_RESTARTS, len(subjects) - skip))
        return rows, info, notes
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def per_trial(argv, subjects, trials, timeout=None, cwd=None, pin=None,
              subject_timeout=None):
    """Run the driver once per TRIAL over the whole subject list -- contract 3:
    "the driver ONCE per (regime, trial)". Returns
    (list_of_row_lists, info, notes)."""
    all_rows, info, notes = [], {}, []
    for _t in range(trials):
        rows, i, n = _run_list_with_resume(argv, subjects, timeout, cwd, pin,
                                           subject_timeout)
        all_rows.append(rows)
        info.update(i)
        notes.extend(n)
    return all_rows, info, notes
