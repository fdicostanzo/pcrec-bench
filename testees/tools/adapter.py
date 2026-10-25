r"""testees/tools/adapter.py -- the TOOLS-tier adapter ([B140] build-order step 4,
docs/design/subst_bench_v1.md 3.2 and 8a items 6, 7, 10).

Five testees, each a COMMAND-LINE TOOL launched fresh per trial
(`testee.invocation = "process"`): GNU sed -E, perl -p, a committed python
whole-file re.sub script, sd 1.1.0 and `rg --passthru -r`. ONE adapter for all
five: they share a runner (`pcrecbench/toolrun.py`), a pin file (`tools.toml`)
and a protocol, and differ only in the command shape (`toolrun.build_argv`)
and the template dialect (`subst_template.render`).

WHAT A TRIAL IS. Trial 1 of a (case, subject): an UNTIMED correctness pass
writes the tool's real output to `out_dir/<ID>.out`; the harness's gate
(`substrun`, unchanged) hashes it against expectations.tsv. Then EVERY trial,
including trial 1, runs the TIMED pipeline `tool ... | wc -c`
(`toolrun.timed_pipeline`) and the byte count wc prints must equal the
validated size or the run fails BY NAME (`toolrun.SinkMismatch`, nothing is
written). A tool prints no substitution count, so `subst_support` says
`count = "oracle"` and `substrun._judge` takes the count from the expectation
when the output's sha256 equals the oracle's.

NO COMPILE ROW. A tool re-parses its pattern on every launch: the testee is
`interpretive`, `compile_phases` is empty, and `compile()` returns a handle
only; the harness omits the compiled row of a `process` testee (schema v1.9
S7 / X41) and writes `unsupported-by-declaration` rows for the cases
divergences.tsv declares unsupported (X44/X45).

PINNING (tools.toml). sd and ripgrep by BINARY SHA256, verified at
describe/prepare/run time (sd's `--version` is stale and never trusted); sed,
perl and python3 by the version string they must report, with the binary's
sha256 recorded live in `testee.binary`. wc, taskset and fincore are the
box's, recorded in `build_flags`.
"""

import os
import re
import subprocess
import sys
import tomllib

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench import adapters as _ad          # noqa: E402
from pcrecbench import toolrun                  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(os.path.dirname(HERE))


def _tool_roots():
    """Where a repo-relative `build/tools/...` path may live: this checkout,
    then (in a lane worktree, where the gitignored `build/` is not copied)
    the main checkout that owns the worktree. `$PCRECBENCH_TOOLS_ROOT`
    wins. The sha256 pin makes the choice of root immaterial."""
    roots = []
    env = os.environ.get("PCRECBENCH_TOOLS_ROOT")
    if env:
        roots.append(env)
    roots.append(REPO_ROOT)
    try:
        common = subprocess.run(
            ["git", "-C", REPO_ROOT, "rev-parse", "--path-format=absolute",
             "--git-common-dir"], capture_output=True, text=True,
            timeout=30).stdout.strip()
        if common:
            roots.append(os.path.dirname(common))
    except (OSError, subprocess.SubprocessError):
        pass
    return roots


class Adapter(_ad.Adapter):
    name = "tools"

    def __init__(self, directory):
        self.dir = directory
        path = os.path.join(directory, "tools.toml")
        if not os.path.exists(path):
            raise _ad.AdapterError("no tools.toml in %s" % directory)
        with open(path, "rb") as f:
            self.cfg = tomllib.load(f)

    # ----------------------------------------------------------- binaries

    def binary_path(self, testee_id):
        """The absolute path of the tool's binary, its sha256 verified when
        the config pins one (a mismatch is an AdapterError BY NAME)."""
        cfg = self.config(testee_id)
        p = cfg["path"]
        if os.path.isabs(p):
            found = p
        else:
            cands = [os.path.join(r, p) for r in _tool_roots()]
            found = next((c for c in cands if os.path.isfile(c)), None)
            if found is None:
                raise _ad.AdapterError(
                    "%s: %s not found under %s -- the tool is installed "
                    "under build/tools/ (subst_bench_v1.md 9; this lane "
                    "never downloads)" % (testee_id, p, ", ".join(cands)))
        real = os.path.realpath(found)
        want = cfg.get("binary_sha256")
        if want:
            got = toolrun.sha256_file(real)
            if got != want:
                raise _ad.AdapterError(
                    "%s: BINARY SHA256 MISMATCH for %s: tools.toml pins %s, "
                    "the file is %s" % (testee_id, real, want, got))
        return real

    def probe_version(self, testee_id):
        """-> (engine_version, raw first line). A distro tool must report the
        pinned version; a hash-pinned one reports whatever it likes (sd
        1.1.0 prints 1.0.0) and the pin is the hash."""
        cfg = self.config(testee_id)
        binary = self.binary_path(testee_id)
        raw = toolrun.probe([binary] + list(cfg["version_argv"]))
        if cfg.get("reported_version_is_stale"):
            return cfg["version"], raw
        m = re.search(cfg["version_regex"], raw)
        got = m.group(1) if m else None
        if got != cfg["version"]:
            raise _ad.AdapterError(
                "%s: %s reports version %r (%s) but tools.toml pins %r -- a "
                "changed system tool is refused, never silently measured "
                "(subst_bench_v1.md 9.4)" % (testee_id, binary, got, raw,
                                             cfg["version"]))
        return got, raw

    # ----------------------------------------------------------- interface

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        binary = self.binary_path(testee_id)
        version, raw = self.probe_version(testee_id)
        sha = toolrun.sha256_file(binary)
        wc = toolrun.which("wc")
        try:
            wc_version = toolrun.probe([wc, "--version"])
        except (OSError, Exception):
            wc_version = "unknown"
        shape = {"sed": "sed -E s/PAT/REPL/g FILE",
                 "perl": "perl -pe s/PAT/REPL/g FILE",
                 "python": "python3 -I subst_py.py PATFILE TPLFILE FILE "
                           "(re.sub on bytes, whole file)",
                 "sd": "sd PAT REPL < FILE",
                 "rg": "rg --no-config --passthru -N --no-heading --color "
                       "never -j1 -r REPL PAT FILE"}[cfg["kind"]]
        opts = [{"name": "command", "value": shape},
                {"name": "sink", "value": "| wc -c, wc pinned to a core "
                 "other than the tool's"},
                {"name": "page_cache", "value": "warm, fincore-asserted "
                 "100 % resident before every timed launch"},
                {"name": "binary_sha256", "value": sha},
                {"name": "reported_version", "value": raw[:120]}]
        if cfg.get("reported_version_is_stale"):
            opts.append({"name": "reported_version_stale", "value": True})
        return {
            "engine_name": cfg["engine_name"],
            "engine_version": version,
            "engine_commit": None,
            "execution_model": "interpretive",
            "automaton_class": cfg["automaton_class"],
            "openness": "open-source",
            "license_id": cfg["license_id"],
            "conventions": [cfg["convention"]],
            "captures": "on",
            "engine_mode": "default",
            "simd": "n-a",
            "invocation": "process",
            "build_flags": (
                "command-line tool %s, binary %s sha256 %s; run under "
                "LC_ALL=C with an otherwise EMPTY environment, no shell, "
                "argv spawned by os.posix_spawn under `taskset -c N`; sink "
                "%s (%s); input warm in the page cache (fincore). %s"
                % (cfg["engine_name"], binary, sha, wc, wc_version,
                   cfg["description"])),
            "runtime_options": opts,
            "compile_cost_definition": (
                "none (interpretive, schema v1.9 S7): a command-line tool "
                "re-parses its pattern on every launch, so there is no "
                "separable compile; the pattern parse is inside the timed "
                "process wall time and no compile row is recorded"),
            "compile_phases": [],
            "warmup_trials": 0,
            "engine_metadata_declaration": {},
            "binary": {"path": binary, "sha256": sha},
        }

    def binary_identity(self, testee_id, workdir=None):
        binary = self.binary_path(testee_id)
        return {"path": binary, "sha256": toolrun.sha256_file(binary)}

    def prepare(self, testee_id, workdir):
        self.config(testee_id)
        self.binary_path(testee_id)
        self.probe_version(testee_id)
        for need in ("taskset", "wc", "fincore"):
            toolrun.which(need)

    def compile(self, testee_id, pattern_id, pattern, options, trials,
                workdir, requires_free_spacing=False):
        """No compile (interpretive): write the pattern file the python
        script reads and return a handle. The harness drops the row."""
        pdir = os.path.join(workdir, "p-" + pattern_id, "tools")
        os.makedirs(pdir, exist_ok=True)
        patfile = os.path.join(pdir, "pattern.rx")
        with open(patfile, "wb") as f:
            f.write(pattern)
        handle = {"testee_id": testee_id, "pattern": pattern,
                  "pattern_file": patfile, "form": _ad.FORM_PLAIN}
        return _ad.CompiledPattern({_ad.FORM_PLAIN: _ad.CompileResult(
            outcome="compiled", phase_seconds=[{} for _ in range(trials)],
            handle=handle)})

    # ------------------------------------------------ substitution ([B140])

    def subst_support(self, testee_id):
        cfg = self.config(testee_id)
        return {"dialect": cfg["dialect"], "competitor": cfg["competitor"],
                "sizing": "n/a", "count": "oracle"}

    def measure_subst(self, handle, subjects, bounds, out_dir, timeout=None):
        tid = handle["testee_id"]
        cfg = self.config(tid)
        binary = self.binary_path(tid)
        sub = handle["subst"]
        with open(sub["template_file"], "rb") as f:
            template = f.read()
        pin = handle.get("pin") or []
        pin_core = int(pin[2]) if len(pin) == 3 and pin[0] == "taskset" \
            else None
        tool_core, sink_core, core_note = toolrun.pick_cores(pin_core)
        ok_exit = tuple(cfg.get("ok_exit", [0]))
        limit = timeout or 900
        validated = sub.setdefault("validated", {})
        peaks = sub.setdefault("peak_rss_kb", {})
        rows, notes = [], []
        if core_note and out_dir:
            notes.append(core_note)
        for s in subjects:
            row = _ad.MatchRow(s.subject_id, "match", consumed=None, iters=1)
            argv, stdin_is_input, display = toolrun.build_argv(
                cfg["kind"], binary, handle["pattern"], template, s.path,
                pattern_file=handle["pattern_file"],
                template_file=sub["template_file"])
            if out_dir:
                # trial 1: the UNTIMED correctness pass
                out_path = os.path.join(out_dir, s.subject_id + ".out")
                rc, err, peak = toolrun.untimed_pass(
                    argv, stdin_is_input, s.path, out_path, tool_core, limit)
                if peak is not None:
                    peaks[s.subject_id] = peak
                if rc not in ok_exit:
                    row.answer = ("error:%s untimed pass exited %s: %s"
                                  % (cfg["engine_name"], rc, err.strip()[:300]))
                    rows.append(row)
                    continue
                validated[s.subject_id] = os.path.getsize(out_path)
                row.out_path = os.path.basename(out_path)
            want = validated.get(s.subject_id)
            if want is None:
                raise toolrun.ToolError(
                    "no validated size for %s: trial 1 never ran its "
                    "untimed pass" % s.subject_id)
            frac = toolrun.warm_resident(s.path)
            t = toolrun.timed_pipeline(argv, stdin_is_input, s.path,
                                       tool_core, sink_core, limit)
            if t["rc"] not in ok_exit or t["sink_bytes"] is None:
                row.answer = ("error:%s timed run exited %s, sink printed %r: "
                              "%s" % (cfg["engine_name"], t["rc"],
                                      t["sink_text"], t["stderr"].strip()[:300]))
                rows.append(row)
                continue
            if t["sink_bytes"] != want:
                raise toolrun.SinkMismatch(
                    "SINK MISMATCH: %s on %s: `| wc -c` counted %d bytes but "
                    "the validated output is %d bytes. A timed run whose "
                    "count differs from the validated size is not a "
                    "measurement (ruling 7, X39); nothing is written."
                    % (tid, s.subject_id, t["sink_bytes"], want))
            row.seconds = t["seconds"]
            row.out_bytes = t["sink_bytes"]
            row.process = {
                "cmd": display, "sink": "wc-c",
                "sink_bytes": t["sink_bytes"], "core": tool_core,
                "sink_core": sink_core, "user_s": t["user_s"],
                "sys_s": t["sys_s"],
                # the untimed pass's polled VmHWM when it saw one: wait4's
                # ru_maxrss is floored at the harness's own RSS (toolrun)
                "maxrss_kb": peaks.get(s.subject_id, t["maxrss_kb"]),
                "page_cache_resident": frac}
            rows.append(row)
        return rows, {}, notes
