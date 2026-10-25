"""toolrun.py -- the TOOLS tier's process runner ([B140] build-order step 4,
docs/design/subst_bench_v1.md 3.2 and 8a item 7; record schema v1.9
`testee.invocation` = `process`, `match.process`).

ENGINE-NEUTRAL BY CONSTRUCTION (R-BENCH-4). Nothing here names a case; the
five tools the set times (GNU sed -E, perl -p, a python whole-file re.sub
script, sd, ripgrep --passthru) differ only in `build_argv()`'s one table of
command shapes. `testees/tools/adapter.py` is the thin adapter; the gate, the
unsupported-by-declaration rows and the record shape are `substrun.py`'s and
`harness.py`'s, REUSED, not forked.

WHAT ONE TRIAL IS (ruling 7):

  1. an UNTIMED correctness pass (trial 1 only): the command, stdout to a
     real output file, no sink. The harness hashes that file against
     expectations.tsv (substrun's gate, unchanged). Its size is the
     VALIDATED size.
  2. a TIMED run, every trial including trial 1: `tool ... | wc -c`, the tool
     pinned to core N and wc to ANOTHER core (X40), spawned by
     `os.posix_spawn` with the pipe wired by file actions -- NO SHELL in the
     path. The clock is `time.perf_counter_ns()` from just before the TOOL's
     spawn (wc is spawned first and sits blocked on its read) to the second
     `wait4` returning, so it covers process start, the file read, the
     transform, the write into the pipe and wc's drain. The tool's rusage
     (user/sys CPU, maxrss) comes from its own `wait4`; it is provenance, not
     a rank.
  3. the SINK CHECK: wc's byte count must equal the validated size. A run
     whose count differs FAILS BY NAME (`SinkMismatch`, raised, nothing
     written): this is what closes the "the tool notices /dev/null and skips
     work" hole on every run and catches a nondeterministic tool.

Page cache: WARM by construction. Before each timed launch the input is read
end to end (a `cat > /dev/null` equivalent, untimed) and `fincore` must
report it 100 % resident; the measured fraction is stored on the row
(`page_cache_resident`). A cold-cache variant needs root and is out of scope
(stated in the set's notes, not hidden).

Cores: the tool runs on the harness's `--pin-cpu` core; wc on a core that is
neither that core nor its SMT sibling (`pick_cores`). With no `--pin-cpu` the
cores are chosen here and the adapter says so in a note -- the process object
needs two integers either way.
"""

import os
import re
import shutil
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)

from . import quiet                               # noqa: E402
from .substrun import SubstError                  # noqa: E402

#: the environment every tool runs under (LC_ALL=C: the subject is ASCII and
#: subst_bench_v1.md 1 says "tools run under LC_ALL=C"); nothing is inherited,
#: so a user's RIPGREP_CONFIG_PATH, PERL5OPT or PYTHONSTARTUP cannot leak in.
TOOL_ENV = {"LC_ALL": "C", "LANG": "C", "PATH": "/usr/bin:/bin"}

#: the sink. A module attribute so the sabotage control can substitute a
#: command that prints the wrong count (check_subst section 11).
SINK_ARGV = ["wc", "-c"]

PY_SCRIPT = os.path.join(os.path.dirname(HERE), "testees", "tools", "subst_py.py")


class ToolError(Exception):
    """A tool could not be run at all (missing binary, taskset absent...)."""


class SinkMismatch(SubstError):
    """The `| wc -c` count differs from the validated output size."""


# --------------------------------------------------------------- binaries

def which(name):
    p = shutil.which(name, path=TOOL_ENV["PATH"])
    if p is None:
        raise ToolError("%s not found on %s" % (name, TOOL_ENV["PATH"]))
    return p


def sha256_file(path):
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def probe(argv, env=None):
    """-> stdout+stderr first line of a `--version` style call."""
    r = subprocess.run(argv, capture_output=True, env=env or TOOL_ENV,
                       timeout=30)
    out = (r.stdout or r.stderr).decode("utf-8", "replace")
    return out.splitlines()[0] if out else ""


# ----------------------------------------------------------------- argv

#: the command shapes, by kind. `stdin` = "file" (the input is the tool's
#: stdin, `sd`) or "null" (the input is a path in argv).
KINDS = ("sed", "perl", "python", "sd", "rg")


def _slash_escaped(pat):
    # the delimiter is `/`; the cases' own patterns carry unescaped slashes
    return pat.replace(b"/", b"\\/")


def build_argv(kind, binary, pattern, template, input_path,
               pattern_file=None, template_file=None):
    """-> (argv: list[bytes|str], stdin_is_input: bool, display: list[str]).

    `pattern` is the case's raw pattern bytes; `template` the replacement
    ALREADY rendered in the tool's dialect (subst_template.render). `display`
    is the argv with every path elided to a token, for `match.process.cmd`
    (the pattern and template text stay: they are the command)."""
    if kind == "sed":
        script = b"s/" + _slash_escaped(pattern) + b"/" + template + b"/g"
        argv = [binary, "-E", script, input_path]
        disp = [binary, "-E", script, "@IN@"]
        return argv, False, _text(disp)
    if kind == "perl":
        script = b"s/" + _slash_escaped(pattern) + b"/" + template + b"/g"
        argv = [binary, "-pe", script, input_path]
        disp = [binary, "-pe", script, "@IN@"]
        return argv, False, _text(disp)
    if kind == "python":
        if pattern_file is None or template_file is None:
            raise ToolError("python needs a pattern file and a template file")
        argv = [binary, "-I", PY_SCRIPT, pattern_file, template_file,
                input_path]
        disp = [binary, "-I", "subst_py.py", "@PATTERN@", "@TEMPLATE@", "@IN@"]
        return argv, False, _text(disp)
    if kind == "sd":
        argv = [binary, pattern, template]
        disp = [binary, pattern, template, "<@IN@"]
        return argv, True, _text(disp)
    if kind == "rg":
        argv = [binary, "--no-config", "--passthru", "-N", "--no-heading",
                "--color", "never", "-j1", "-r", template, pattern,
                input_path]
        disp = [binary, "--no-config", "--passthru", "-N", "--no-heading",
                "--color", "never", "-j1", "-r", template, pattern, "@IN@"]
        return argv, False, _text(disp)
    raise ToolError("unknown tool kind %r (have %s)" % (kind, ", ".join(KINDS)))


def _text(items):
    return [x.decode("latin-1") if isinstance(x, bytes) else x for x in items]


# ----------------------------------------------------------------- cores

def pick_cores(pin_core=None):
    """-> (tool_core, sink_core, note_or_None).

    The tool core is the harness's `--pin-cpu` when given (else the highest
    allowed core, and a NOTE says the adapter chose it); the sink core is
    the highest allowed core that is neither the tool core nor its SMT
    sibling (override: `$PCRECBENCH_TOOLS_SINK_CPU`)."""
    allowed = sorted(os.sched_getaffinity(0))
    note = None
    if pin_core is None:
        tool = allowed[-1]
        note = ("tools tier: no --pin-cpu was given, so the runner chose "
                "core %d for the tool" % tool)
    else:
        tool = int(pin_core)
        if tool not in allowed:
            raise ToolError("--pin-cpu %d is not in this process's allowed "
                            "cores %s" % (tool, allowed))
    env = os.environ.get("PCRECBENCH_TOOLS_SINK_CPU")
    if env:
        sink = int(env)
        if sink == tool or sink not in allowed:
            raise ToolError("$PCRECBENCH_TOOLS_SINK_CPU=%d must be an allowed "
                            "core other than the tool's (%d)" % (sink, tool))
        return tool, sink, note
    sib = set(quiet.smt_siblings(tool))
    rest = [c for c in allowed if c != tool and c not in sib]
    if not rest:
        raise ToolError("no allowed core is distinct from the tool's core %d "
                        "and its SMT sibling; the sink needs its own (X40)"
                        % tool)
    return tool, rest[-1], note


# ------------------------------------------------------------ page cache

def warm(path):
    """Read the whole input (untimed): the `cat > /dev/null` of 3.2."""
    with open(path, "rb", buffering=0) as f:
        while f.read(1 << 22):
            pass


def resident_fraction(path):
    """`fincore`'s resident bytes / size, in [0, 1]."""
    r = subprocess.run([which("fincore"), "-b", "-n", "-o", "RES,SIZE", path],
                       capture_output=True, text=True, env=TOOL_ENV,
                       timeout=60)
    if r.returncode != 0 or not r.stdout.split():
        raise ToolError("fincore failed on %s: %s" % (path, r.stderr.strip()))
    res, size = (int(x) for x in r.stdout.split()[:2])
    return 1.0 if size == 0 else min(1.0, res / size)


class NotResident(SubstError):
    """The input is not 100 % page-cache resident after a warm read."""


def warm_resident(path):
    warm(path)
    frac = resident_fraction(path)
    if frac < 1.0:
        warm(path)
        frac = resident_fraction(path)
    if frac < 1.0:
        raise NotResident(
            "PAGE CACHE NOT RESIDENT: %s is %.4f resident after two warm "
            "reads; the tools tier times a WARM cache (subst_bench_v1.md 3.2) "
            "and will not time a partly cold input" % (path, frac))
    return frac


# -------------------------------------------------------------- spawning

def _spawn(argv, stdin_fd, stdout_fd, stderr_fd, core, env):
    """posix_spawn `taskset -c core argv...` with fds wired. -> pid."""
    taskset = which("taskset")
    exe = [taskset, "-c", str(core)] + [
        a if isinstance(a, (bytes, str)) else str(a) for a in argv]
    fa = [(os.POSIX_SPAWN_DUP2, stdin_fd, 0),
          (os.POSIX_SPAWN_DUP2, stdout_fd, 1),
          (os.POSIX_SPAWN_DUP2, stderr_fd, 2)]
    return os.posix_spawn(taskset, exe, env, file_actions=fa)


def _resolve(argv):
    """The first element must be an absolute path (never rely on PATH)."""
    first = argv[0]
    if not os.path.isabs(first):
        argv = [which(first)] + list(argv[1:])
    return argv


def _decode_status(status):
    if os.WIFEXITED(status):
        return os.WEXITSTATUS(status)
    if os.WIFSIGNALED(status):
        return -os.WTERMSIG(status)
    return status


def _watchdog(pids, seconds):
    """Kill by PID if the run exceeds `seconds` (a firing timeout is a
    FINDING; the caller sees the kill in the status)."""
    fired = []

    def kill():
        fired.append(True)
        for p in pids:
            try:
                os.kill(p, 9)
            except ProcessLookupError:
                pass
    t = threading.Timer(seconds, kill)
    t.daemon = True
    return t, fired


def untimed_pass(argv, stdin_is_input, input_path, out_path, core,
                 timeout=900):
    """The correctness pass: `tool ... > out_path`, no sink. -> (rc, stderr)."""
    argv = _resolve(argv)
    err_path = out_path + ".err"
    in_fd = os.open(input_path if stdin_is_input else os.devnull, os.O_RDONLY)
    out_fd = os.open(out_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    err_fd = os.open(err_path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        pid = _spawn(argv, in_fd, out_fd, err_fd, core, TOOL_ENV)
    finally:
        for fd in (in_fd, out_fd, err_fd):
            os.close(fd)
    timer, fired = _watchdog([pid], timeout)
    timer.start()
    try:
        _, status, _ru = os.wait4(pid, 0)
    finally:
        timer.cancel()
    rc = _decode_status(status)
    with open(err_path, "rb") as f:
        err = f.read(2000).decode("utf-8", "replace")
    os.unlink(err_path)
    if fired:
        rc = "timeout"
    return rc, err


def timed_pipeline(argv, stdin_is_input, input_path, tool_core, sink_core,
                   timeout=900):
    """ONE timed `tool ... | wc -c`. -> dict(seconds, rc, sink_rc,
    sink_bytes, user_s, sys_s, maxrss_kb, stderr)."""
    argv = _resolve(argv)
    sink = _resolve(SINK_ARGV)
    in_fd = os.open(input_path if stdin_is_input else os.devnull, os.O_RDONLY)
    pipe_r, pipe_w = os.pipe()
    cnt_r, cnt_w = os.pipe()
    err_r, err_w = os.pipe()
    null_fd = os.open(os.devnull, os.O_RDONLY)
    pids = []
    try:
        # wc first: it blocks on its read, so its exec is outside the clock
        wc_pid = _spawn(sink, pipe_r, cnt_w, err_w, sink_core, TOOL_ENV)
        pids.append(wc_pid)
        timer, fired = _watchdog(pids, timeout)
        timer.start()
        t0 = time.perf_counter_ns()
        tool_pid = _spawn(argv, in_fd, pipe_w, err_w, tool_core, TOOL_ENV)
        pids.append(tool_pid)
        # the parent must drop its copies, or wc never sees EOF
        os.close(pipe_w)
        pipe_w = -1
        _, tool_status, ru = os.wait4(tool_pid, 0)
        _, wc_status, _ru2 = os.wait4(wc_pid, 0)
        t1 = time.perf_counter_ns()
        timer.cancel()
    finally:
        for fd in (in_fd, pipe_r, pipe_w, cnt_w, err_w, null_fd):
            if fd >= 0:
                try:
                    os.close(fd)
                except OSError:
                    pass
    os.set_blocking(cnt_r, False)
    os.set_blocking(err_r, False)
    try:
        count_text = os.read(cnt_r, 4096).decode("ascii", "replace")
    except BlockingIOError:
        count_text = ""
    try:
        err = os.read(err_r, 4096).decode("utf-8", "replace")
    except BlockingIOError:
        err = ""
    os.close(cnt_r)
    os.close(err_r)
    m = re.match(r"\s*(\d+)\b", count_text)
    return {"seconds": (t1 - t0) / 1e9,
            "rc": "timeout" if fired else _decode_status(tool_status),
            "sink_rc": _decode_status(wc_status),
            "sink_bytes": int(m.group(1)) if m else None,
            "sink_text": count_text.strip(),
            "user_s": ru.ru_utime, "sys_s": ru.ru_stime,
            "maxrss_kb": int(ru.ru_maxrss), "stderr": err}
