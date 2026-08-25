"""testees/pcrec/adapter.py -- the pcrec adapter (harness contract 3).

Provides `pcrec-auto`, `pcrec-nocaps`, `pcrec-vm`, and the caller-provided
frame-buffer variants `pcrec-auto-in` / `pcrec-vm-in`, all at the pin in
`configs.toml` -- and `pcrec-local`, a PROVIDED binary at no pin at all.

THE LOCAL TESTEE (Frank's I-4 (c), [B10]; record_schema.md 6.2 and 6.8).
`$PCREC_BIN` names the binary, `$PCREC_LOCAL_FLAGS` adds flags; pin.sh is
never called. `describe()` reports `engine_version = local:<first 12 hex of
the binary's sha256>`, plus `+<git describe --always --dirty --tags>` when a
repository sits beside the binary (walking up from its directory to a `.git`
FILE or directory -- a pcrec worktree has a file; a `git archive` pin has a
`PIN.tsv` and no repository, and the walk stops there), `engine_commit` =
HEAD when that tree is clean and null when it is dirty, `tier: scratch`, and
`testee.binary` = {path, sha256}. SCRATCH BY CONSTRUCTION: the harness reads
`tier()` before it gates or measures, and the store refuses the record into
the canonical tree. `engine_mode` and `captures` are DERIVED from the
effective flags (`--engine=vm` -> `vm`, `--no-captures` -> `off`) so the
testee_id says what ran. Everything after describe() -- emit-c / gcc / load,
shim.c, driver.c, the metadata, the `_in` buffers -- is the same code path as
the pinned testees: `binary_for()` is the one place the binary is chosen.

THE `_in` TESTEES (pcrec docs/spec/match_api.md 10, [DD-14.FB]): a config
carrying `buffer_frames = N` and `buffer_trail = M` -- CAPACITIES in frames
and trail entries, never bytes -- makes the driver allocate two regions once
per run and call `<prefix>_search_in` / `<prefix>_match_caps_in` with them in
every regime. The sizes are THE KNOB and they go in the record twice: as
`testee.runtime_options` (the configuration) and as the `buffer_frames` /
`buffer_trail` engine_metadata pairs on the compile row (what the driver
actually ran with; ABSENT means the stamped default storage ran, which is
also what happens on a DFA artifact, whose stamped frame size is 0 and which
takes no buffers at all -- 10.4). requirements 4.2: it is a separate
(engine, version, configuration) triple, hence a separate roster entry with
its own engine_mode slug (`auto-in`, `vm-in`) so the derived testee_id is
distinct.

COMPILE COST -- AOT, THREE PHASES (requirements 3: "pattern -> C -> gcc ->
loadable object, all phases, each timed"):

    emit-c   the `pcrec` CLI turning the pattern into artifact.c/.h   [python]
    gcc      $CC -O2 -fPIC -shared shim.c (which #includes artifact.c)
             -> artifact-N.so                                         [python]
    load     dlopen of that .so                                       [driver]

Each TRIAL builds its own `artifact-<trial>.so`. That is not tidiness: the
dynamic loader caches by path, so a second dlopen of one path is free and a
per-trial `load` number taken that way would be a measurement of the cache.

ENGINE METADATA comes from the artifact's STRUCTURED fields only
(requirements 4.2) -- `rx_info` read through `shim.c`, and the D46 `RX_VM_*`
preprocessor stamps read the same way. The prose `RX_ENGINE_WHY` is
explicitly NOT a metadata pair: it lands in the compile row's unindexed
`diagnostic`, which is where record_schema.md 7 puts it.
"""

import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench import adapters as _ad                       # noqa: E402
from pcrecbench import record as _rec                        # noqa: E402
from pcrecbench.driverrun import (C_ENV, build_driver,       # noqa: E402
                                  per_trial, run_driver)

HERE = os.path.dirname(os.path.abspath(__file__))
PIN_SH = os.path.join(HERE, "pin.sh")
PCREC_SRC = os.environ.get("PCREC_SRC", "/home/duxevents/pcrec")
BENCH_ROOT = os.path.dirname(os.path.dirname(HERE))

# record_schema.md 6.3's registry for pcrec: what `--engine=` may name.
ENGINE_MODES = ("auto", "dfa", "vm")

# record_schema.md 7's worked example, as a DECLARATION. Every pair the
# driver can emit is here with its type, scope and SOURCE; an undeclared pair
# is a validator error (X15), so this table and shim.c move together.
RXINFO_SRC = "rx_info.%s, read through testees/pcrec/shim.c's pb_%s()"
METADATA_DECL = {
    "engine": {
        "type": "enum", "scope": "pattern", "values": ["dfa", "vm", "unknown"],
        "source": "rx_info.engine (PCREC_ENGINE_DFA=1 / PCREC_ENGINE_VM=2)",
        "description": "the engine the artifact was built with",
    },
    "abi": {"type": "integer", "scope": "pattern",
            "source": RXINFO_SRC % ("abi", "abi"),
            "description": "the reflection struct's layout version"},
    "ncaps": {"type": "integer", "scope": "pattern",
              "source": RXINFO_SRC % ("ncaps", "ncaps"),
              "description": "caps[] slot count, all-in (== <PREFIX>_NCAPS)"},
    "ngroups": {"type": "integer", "scope": "pattern",
                "source": RXINFO_SRC % ("ngroups", "ngroups"),
                "description": "capturing groups in the pattern TEXT, a "
                               "lexical fact independent of --no-captures"},
    "nnames": {"type": "integer", "scope": "pattern",
               "source": RXINFO_SRC % ("nnames", "nnames"),
               "description": "named groups in rx_info.groups[]"},
    "step_budget": {"type": "integer", "scope": "pattern",
                    "source": RXINFO_SRC % ("step_budget", "step_budget"),
                    "description": "backtrack resumptions before "
                                   "PCREC_ERR_STEPS; -1 = none"},
    "work_budget": {"type": "integer", "scope": "pattern",
                    "source": RXINFO_SRC % ("work_budget", "work_budget"),
                    "description": "forward work units before PCREC_ERR_WORK; "
                                   "-1 = none"},
    "frame_capacity": {"type": "integer", "scope": "pattern",
                       "source": RXINFO_SRC % ("frame_capacity", "frame_capacity"),
                       "description": "resume-stack capacity; -1 = unbounded"},
    "subject_ceiling": {"type": "integer", "scope": "pattern",
                        "source": RXINFO_SRC % ("subject_ceiling", "subject_ceiling"),
                        "description": "stamped honest ceiling, 0 = unset"},
    "prefilter": {
        "type": "enum", "scope": "pattern", "values": ["hybrid", "none"],
        "source": "<PREFIX>_VM_PREFILTER, read through pb_vm_prefilter()",
        "description": "the [M4.6f] prefilter decision. VM artifacts ONLY: a "
                       "DFA artifact emits no such stamp, and an ABSENT pair "
                       "is not an error",
    },
    "vm_rungs": {
        "type": "mask", "scope": "pattern",
        "bits": ["PCREC_VM_RUNG_CURSOR", "PCREC_VM_RUNG_FRAMES_BOUNDED",
                 "PCREC_VM_RUNG_FRAMES_UNBOUNDED", "PCREC_VM_RUNG_REVDET",
                 "PCREC_VM_RUNG_COUNTER"],
        "source": "<PREFIX>_VM_RUNGS (D46), read through pb_vm_rungs()",
        "description": "the rungs used, OR'd per quantifier body",
    },
    "vm_strats": {
        "type": "mask", "scope": "pattern",
        "bits": ["PCREC_VM_STRAT_POSSESSIVE", "PCREC_VM_STRAT_BACKTRACKING"],
        "source": "<PREFIX>_VM_STRATS, read through pb_vm_strats()",
        "description": "the ladder's first-rung strategy, per quantifier",
    },
    "vm_prunes": {
        "type": "mask", "scope": "pattern",
        "bits": ["PCREC_VM_PRUNE_CLAMPED", "PCREC_VM_PRUNE_UNCLAMPED"],
        "source": "<PREFIX>_VM_PRUNES, read through pb_vm_prunes()",
        "description": "length-prune form, per quantifier",
    },
    # -- the caller-provided frame buffer's sizing surface (match_api.md
    # 10.4, abi 3). Stamped on EVERY artifact at abi 3, both engines; a DFA
    # artifact stamps 0 for all four ("this engine takes no buffers").
    "resume_frames": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_RESUME_FRAMES (== rx_info.resume_frames at abi 3), "
                  "read through pb_resume_frames()",
        "description": "the stamped DEFAULT resume-stack capacity, in FRAMES; "
                       "0 on a DFA artifact",
    },
    "trail_frames": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_TRAIL_FRAMES (== rx_info.trail_frames at abi 3), "
                  "read through pb_trail_frames()",
        "description": "the stamped DEFAULT trail capacity, in ENTRIES; 0 on "
                       "a DFA artifact",
    },
    "resume_frame_size": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_RESUME_FRAME_SIZE (== rx_info.resume_frame_size "
                  "at abi 3), read through pb_resume_frame_size()",
        "description": "bytes per resume frame FOR THIS ARTIFACT (per-artifact: "
                       "24 or 40 measured so far); 0 = the engine takes no "
                       "buffers",
    },
    "trail_frame_size": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_TRAIL_FRAME_SIZE (== rx_info.trail_frame_size at "
                  "abi 3), read through pb_trail_frame_size()",
        "description": "bytes per trail entry FOR THIS ARTIFACT; 0 = the "
                       "engine takes no buffers",
    },
    # -- what the driver actually ran with. Present ONLY when a caller-
    # provided buffer was in use for this artifact.
    "buffer_frames": {
        "type": "integer", "scope": "pattern",
        "source": "the driver's --buffer-frames, from configs.toml "
                  "`buffer_frames`, echoed as `info buffer_frames` only when "
                  "the regions were allocated and the _in entries used",
        "description": "the caller-provided resume-frame CAPACITY (frames, "
                       "not bytes) this testee ran with; ABSENT means the "
                       "default stamped buffers were used",
    },
    "buffer_trail": {
        "type": "integer", "scope": "pattern",
        "source": "the driver's --buffer-trail, from configs.toml "
                  "`buffer_trail`, echoed as `info buffer_trail` only when "
                  "the regions were allocated and the _in entries used",
        "description": "the caller-provided trail CAPACITY (entries, not "
                       "bytes) this testee ran with; ABSENT means the default "
                       "stamped buffers were used",
    },
}

# The bit VALUES, from pcrec docs/spec/match_api.md 2 (the emitted
# PCREC_RX_ABI_H block). record_schema.md 7 rule 3: a `mask` value is an
# ARRAY OF BIT NAMES, never the integer -- the reporter must not need pcrec's
# bit table to filter on it.
MASK_BITS = {
    "vm_rungs": [("PCREC_VM_RUNG_CURSOR", 0x1),
                 ("PCREC_VM_RUNG_FRAMES_BOUNDED", 0x2),
                 ("PCREC_VM_RUNG_FRAMES_UNBOUNDED", 0x4),
                 ("PCREC_VM_RUNG_REVDET", 0x8),
                 ("PCREC_VM_RUNG_COUNTER", 0x10)],
    "vm_strats": [("PCREC_VM_STRAT_POSSESSIVE", 0x1),
                  ("PCREC_VM_STRAT_BACKTRACKING", 0x2)],
    "vm_prunes": [("PCREC_VM_PRUNE_CLAMPED", 0x1),
                  ("PCREC_VM_PRUNE_UNCLAMPED", 0x2)],
}
INT_PAIRS = ("abi", "ncaps", "ngroups", "nnames", "step_budget",
             "work_budget", "frame_capacity", "subject_ceiling",
             "resume_frames", "trail_frames", "resume_frame_size",
             "trail_frame_size", "buffer_frames", "buffer_trail")


def buffer_capacities(cfg):
    """-> (frames, trail) from a config's `buffer_frames` / `buffer_trail`,
    or None when the config has neither. Both or neither: a non-NULL
    descriptor requires BOTH regions (match_api.md 10.2), and the trail is
    the array that binds first, so a frames-only knob would be inert."""
    f, t = cfg.get("buffer_frames"), cfg.get("buffer_trail")
    if f is None and t is None:
        return None
    if f is None or t is None:
        raise _ad.AdapterError(
            "buffer_frames and buffer_trail go together (match_api.md 10.2: "
            "both regions are required); got frames=%r trail=%r" % (f, t))
    if not (isinstance(f, int) and isinstance(t, int)) or f < 1 or t < 1:
        raise _ad.AdapterError(
            "buffer_frames / buffer_trail must be positive integers -- "
            "CAPACITIES in frames and entries, never bytes; got %r / %r"
            % (f, t))
    return f, t


def buffer_args(cfg):
    """The driver's `--buffer-frames N --buffer-trail M`, or []."""
    caps = buffer_capacities(cfg)
    if caps is None:
        return []
    return ["--buffer-frames", str(caps[0]), "--buffer-trail", str(caps[1])]


def _mask_names(name, value):
    out = [bit for bit, mask in MASK_BITS[name] if value & mask]
    unknown = value & ~sum(m for _b, m in MASK_BITS[name])
    if unknown:
        raise _ad.AdapterError(
            "%s carries bit(s) 0x%x this adapter has no name for. pcrec grew "
            "a stamp bit; add it to MASK_BITS and to METADATA_DECL together, "
            "or the record would claim a mask it cannot spell." % (name, unknown))
    return out


def _find_repo_beside(start):
    """The repository a binary sits in, or None: walk UP from `start` to a
    directory holding `.git` (a FILE in a worktree, a directory in a main
    tree). Two stops, both deliberate: a directory holding `PIN.tsv` is a
    `git archive` snapshot pin.sh made, which has no repository by design
    (the walk must not climb out of it into whatever tree holds build/);
    and this bench's own checkout is never "the repository beside a pcrec
    binary", however the binary got under it."""
    bench_tops = set()
    for d in (BENCH_ROOT,):
        try:
            proc = subprocess.run(["git", "-C", d, "rev-parse", "--show-toplevel",
                                   "--git-common-dir"], capture_output=True,
                                  text=True, env=C_ENV, timeout=30)
            for line in (proc.stdout or "").splitlines():
                line = line.strip()
                if line:
                    if not os.path.isabs(line):
                        line = os.path.join(d, line)
                    bench_tops.add(os.path.realpath(
                        line[:-5] if line.endswith("/.git") else line))
        except (OSError, subprocess.SubprocessError):
            pass
        bench_tops.add(os.path.realpath(d))
    d = os.path.realpath(start)
    while True:
        if os.path.exists(os.path.join(d, "PIN.tsv")):
            return None
        if os.path.realpath(d) in bench_tops:
            return None
        if os.path.exists(os.path.join(d, ".git")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def _git_at(repo, *args):
    """A READ-ONLY git query against the repository beside a local binary
    (BD2: pcrec's tree is never written from here; `describe` and
    `rev-parse` read)."""
    try:
        proc = subprocess.run(["git", "-C", repo] + list(args),
                              capture_output=True, text=True, env=C_ENV,
                              timeout=60)
    except (OSError, subprocess.SubprocessError):
        return ""
    return proc.stdout.strip() if proc.returncode == 0 else ""


def local_provenance(binary):
    """-> (engine_version, engine_commit, describe_raw, repo) for a provided
    binary (record_schema.md 6.2, the `local:` shape)."""
    sha = _ad.sha256_file(binary)
    version = "local:" + sha[:12]
    repo = _find_repo_beside(os.path.dirname(os.path.realpath(binary)))
    commit = None
    desc = ""
    if repo:
        desc = _git_at(repo, "describe", "--always", "--dirty", "--tags")
        if desc:
            dirty = desc.endswith("-dirty")
            slug = re.sub(r"[^a-z0-9._+-]", "-", desc.lower()).strip("-")
            version = (version + "+" + slug)[:64].rstrip("+-.")
            if not dirty:
                head = _git_at(repo, "rev-parse", "HEAD")
                commit = head if re.fullmatch(r"[0-9a-f]{40}", head) else None
    return version, commit, desc, repo


class Adapter(_ad.Adapter):
    name = "pcrec"

    # ------------------------------------------------------- local vs pinned

    def is_local(self, testee_id):
        return bool(_ad.Adapter.config(self, testee_id).get("local"))

    def config(self, testee_id):
        """The EFFECTIVE config. For a local testee the flags are the base
        list plus `$<extra_flags>` split on whitespace, and `engine_mode` /
        `captures` are DERIVED from them, so every consumer of `flags`,
        `engine_mode` and `captures` -- describe(), the compile phases, the
        buffer plumbing -- sees one truth and the derived testee_id says
        what actually ran."""
        cfg = dict(_ad.Adapter.config(self, testee_id))
        if not cfg.get("local"):
            return cfg
        flags = list(cfg.get("flags", []))
        extra_var = cfg.get("extra_flags")
        if extra_var:
            flags += os.environ.get(extra_var, "").split()
        cfg["flags"] = flags
        mode = cfg.get("engine_mode", "auto")
        for f in flags:
            if f.startswith("--engine="):
                mode = f.split("=", 1)[1].strip().lower()
        if mode not in ENGINE_MODES:
            raise _ad.AdapterError(
                "%s: --engine=%s is not a pcrec engine mode this adapter "
                "knows (%s; record_schema.md 6.3)"
                % (testee_id, mode, ", ".join(ENGINE_MODES)))
        cfg["engine_mode"] = mode
        cfg["captures"] = "off" if "--no-captures" in flags else "on"
        return cfg

    def local_binary(self, testee_id):
        """`$PCREC_BIN` (the variable is named by the config), checked."""
        cfg = _ad.Adapter.config(self, testee_id)
        var = cfg.get("binary") or "PCREC_BIN"
        path = os.environ.get(var, "")
        if not path:
            raise _ad.AdapterError(
                "%s needs $%s: the path of the pcrec binary to bench "
                "(e.g. %s=/home/you/pcrec/worktrees/x/build/pcrec). It is "
                "not set." % (testee_id, var, var))
        if not os.path.isfile(path) or not os.access(path, os.X_OK):
            raise _ad.AdapterError(
                "%s: $%s=%r is not an executable file" % (testee_id, var, path))
        return os.path.abspath(path)

    def binary_for(self, testee_id):
        """THE ONE PLACE the pcrec binary is chosen: the provided one for a
        local testee, the pin's for every other. Everything downstream
        (emit-c, gcc, load, the driver) is one code path."""
        if self.is_local(testee_id):
            return self.local_binary(testee_id)
        return self.pin_binary()

    def tier(self, testee_id):
        return "scratch" if self.is_local(testee_id) else "pinned"

    # ------------------------------------------------------------- the pin

    def pin(self):
        p = self.cfg.get("pin")
        if not p:
            raise _ad.AdapterError("testees/pcrec/configs.toml declares no pin")
        return p

    def pin_binary(self, build=True):
        """-> the path of the pinned `pcrec`. Delegates to pin.sh, which
        reuses an existing build and never writes inside pcrec's tree."""
        argv = [PIN_SH] + ([] if build else ["--path"]) + [self.pin()]
        proc = subprocess.run(argv, capture_output=True, text=True,
                              env=C_ENV, timeout=1200)
        if proc.returncode != 0:
            raise _ad.AdapterError("pin.sh %s failed:\n%s"
                                   % (self.pin(), proc.stderr))
        return proc.stdout.strip()

    def pin_provenance(self):
        """(full_commit, describe). From the pin tree's PIN.tsv when pin.sh
        wrote one; otherwise from a READ-ONLY git query against pcrec -- the
        commit is a fact about pcrec's history, not something to type."""
        tree = os.path.dirname(os.path.dirname(self.pin_binary(build=False)))
        tsv = os.path.join(tree, "PIN.tsv")
        if os.path.exists(tsv):
            d = {}
            with open(tsv, "r", encoding="utf-8") as f:
                for line in f:
                    k, _, v = line.rstrip("\n").partition("\t")
                    d[k] = v
            if d.get("commit"):
                return d["commit"], d.get("describe") or self.pin()
        full = self._git("rev-parse", "%s^{commit}" % self.pin())
        desc = self._git("describe", "--always", full) or self.pin()
        return full, desc

    def _git(self, *args):
        try:
            proc = subprocess.run(["git", "-C", PCREC_SRC] + list(args),
                                  capture_output=True, text=True, env=C_ENV,
                                  timeout=60)
        except (OSError, subprocess.SubprocessError):
            return ""
        return proc.stdout.strip() if proc.returncode == 0 else ""

    def binary_identity(self, testee_id, workdir=None):
        """`testee.binary` (schema v1.2, X29): the `pcrec` this testee runs
        -- the pin script's build, or the provided one -- and its sha256."""
        path = self.binary_for(testee_id)
        return {"path": os.path.realpath(path), "sha256": _ad.sha256_file(path)}

    # ------------------------------------------------------------- describe

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        local = self.is_local(testee_id)
        if local:
            binary = self.local_binary(testee_id)
            version, full, desc_raw, repo = local_provenance(binary)
            desc = ("%s (%s, %s)" % (desc_raw, "DIRTY" if desc_raw.endswith("-dirty")
                                     else "clean", repo)
                    if desc_raw else "no repository beside the binary")
        else:
            full, desc = self.pin_provenance()
        caps = buffer_capacities(cfg)
        buffer_note = ""
        runtime = [{"name": f.split("=")[0], "value":
                    f.split("=", 1)[1] if "=" in f else True}
                   for f in cfg.get("flags", []) if f.startswith("--")]
        if caps:
            buffer_note = ("; caller-provided frame buffer (match_api.md 10): "
                           "%d resume frames, %d trail entries -- CAPACITIES, "
                           "sized per artifact from its stamped frame sizes; "
                           "the _in entries used in every regime"
                           % caps)
            runtime += [{"name": "buffer_frames", "value": caps[0]},
                        {"name": "buffer_trail", "value": caps[1]}]
        # record_schema.md 6.2: where a testee is pinned to a VCS revision
        # rather than a release -- "which is pcrec ALWAYS" -- engine_commit
        # carries the 40-hex and engine_version a git-describe-shaped string,
        # and the binding rule is that the version be REPRODUCIBLE from the
        # commit. `git describe --always` is exactly that function of it.
        # A LOCAL binary has no such commit: its version is the `local:`
        # shape (the binary's own digest), computed above.
        if not local:
            version = re.sub(r"[^A-Za-z0-9._+-]", "-", desc)
        provenance = ("local binary $%s=%s (sha256 %s); %s"
                      % (_ad.Adapter.config(self, testee_id).get("binary", "PCREC_BIN"),
                         binary, _ad.sha256_file(binary)[:16], desc)
                      if local else "pin %s (%s)" % (self.pin(), desc))
        block = {
            "engine_name": "pcrec",
            "engine_version": version,
            "engine_commit": full or None,
            "execution_model": "compiled-aot",
            # pcrec ships both a DFA engine and a backtracking VM and chooses
            # per pattern (`--engine=auto`), so the TESTEE's class is hybrid
            # even where one artifact turns out to be pure DFA. Which engine
            # a given artifact used is the per-pattern `engine` metadata pair.
            "automaton_class": "hybrid",
            "openness": "open-source",
            "license_id": "MIT",
            "conventions": ["perl-leftmost-first"],
            "captures": cfg.get("captures", "on"),
            "engine_mode": cfg["engine_mode"],
            "simd": "n-a",
            "build_flags": "%s; pcrec flags %s; artifact built with "
                           "$CC -O2 -fPIC -shared%s"
                           % (provenance, " ".join(cfg.get("flags", [])),
                              buffer_note),
            "runtime_options": runtime,
            "compile_cost_definition": (
                "AOT (requirements 3): every phase from pattern text to a "
                "loadable object, each timed -- `emit-c` (the pcrec CLI), "
                "`gcc` (the artifact + shim into a .so), `load` (dlopen). Each "
                "trial builds its own .so, because the dynamic loader caches "
                "by path and a repeated dlopen of one path measures the cache. "
                "Median of N with spread is the REPORTER's reduction; the "
                "record keeps the raw trials."),
            "compile_phases": ["emit-c", "gcc", "load"],
            "warmup_trials": 0,
            "engine_metadata_declaration": dict(METADATA_DECL),
        }
        if local:
            # SCRATCH BY CONSTRUCTION (record_schema.md 6.8, X28/X29): the
            # harness lifts `tier` to the setup layer; `binary` stays here.
            block["tier"] = "scratch"
            block["binary"] = self.binary_identity(testee_id, workdir)
        return block

    # -------------------------------------------------------------- prepare

    def prepare(self, testee_id, workdir):
        self.config(testee_id)
        os.makedirs(workdir, exist_ok=True)
        self.binary_for(testee_id)
        build_driver(os.path.join(HERE, "driver.c"),
                     os.path.join(workdir, "pcrec_driver"), extra=["-ldl"])

    # -------------------------------------------------------------- compile

    def compile(self, testee_id, pattern_id, pattern, options, trials,
                workdir):
        r"""TWO artifacts per pattern: `plain` and `whole-subject`.

        pcrec has no end-anchored generation axis (a ratified but unbuilt
        option, pcrec [OS-4]), so "does the WHOLE subject match" cannot be
        answered by the plain artifact: its anchored entry returns the
        leftmost-first match at position 0, and testing `== n` is sufficient
        but NOT necessary. MEASURED: `a|ab` over `ab` returns length 1, so
        `== n` says NO where PCRE2 under ANCHORED|ENDANCHORED says YES.

        So the match/compliance regime gets its own artifact compiled from
        `(?:<pattern>)\z`, and BOTH are timed and given their own compile
        rows -- they are different compiles of different text, and folding
        their costs together would report a compile cost for an artifact the
        record does not witness (rule X27)."""
        forms = {}
        for form, text in ((_ad.FORM_PLAIN, pattern),
                           (_ad.FORM_WHOLE_SUBJECT,
                            _rec.whole_subject_text(pattern))):
            forms[form] = self._compile_one(testee_id, pattern_id, form, text,
                                            trials, workdir)
        return _ad.CompiledPattern(forms)

    def _compile_one(self, testee_id, pattern_id, form, pattern, trials,
                     workdir):
        import time
        cfg = self.config(testee_id)
        pcrec = self.binary_for(testee_id)
        drv = build_driver(os.path.join(HERE, "driver.c"),
                           os.path.join(workdir, "pcrec_driver"), extra=["-ldl"])
        cc = os.environ.get("CC", "gcc")
        bufargs = buffer_args(cfg)

        phase_seconds = []
        libs = []
        meta = {}
        engine_why = None
        artifact_bytes = None

        for t in range(1, trials + 1):
            # per-PATTERN, per-FORM, per-TRIAL scratch: see Adapter.compile's
            # docstring for the bug the per-pattern part exists to prevent,
            # and this method's for why the form must not share either.
            cdir = os.path.join(workdir, "p-" + pattern_id, form, "t%d" % t)
            os.makedirs(cdir, exist_ok=True)
            art_c = os.path.join(cdir, "artifact.c")

            # phase 1: emit-c ------------------------------------------------
            argv = ([pcrec, "-p", "rx"] + list(cfg.get("flags", []))
                    + ["-o", art_c, "--"] + [pattern.decode("latin-1")])
            t0 = time.monotonic()
            proc = subprocess.run(argv, capture_output=True, env=C_ENV,
                                  timeout=600)
            t1 = time.monotonic()
            if proc.returncode != 0:
                diag = (proc.stderr or b"").decode("utf-8", "replace").strip()
                return _ad.CompileResult("did-not-compile",
                                         diagnostic=diag or "pcrec exit %d"
                                         % proc.returncode)

            # phase 2: gcc ---------------------------------------------------
            so = os.path.join(cdir, "artifact-%d.so" % t)
            # ONE translation unit: shim.c #includes the artifact's .c, so
            # the D46 stamps (which pcrec emits into the .c only) are
            # preprocessor-visible. See shim.c's header comment.
            gargv = [cc, "-O2", "-std=gnu11", "-fPIC", "-shared", "-o", so,
                     os.path.join(HERE, "shim.c"),
                     "-DPB_ARTIFACT=\"%s\"" % art_c, "-I", cdir]
            g0 = time.monotonic()
            gproc = subprocess.run(gargv, capture_output=True, text=True,
                                   env=C_ENV, timeout=900)
            g1 = time.monotonic()
            if gproc.returncode != 0:
                return _ad.CompileResult(
                    "did-not-compile",
                    diagnostic="the artifact did not build:\n%s\n%s"
                               % (" ".join(gargv), gproc.stderr))

            # phase 3: load, timed by the driver -----------------------------
            # The buffer options ride along so the load-only run's `info`
            # block -- which is where the compile row's engine_metadata comes
            # from -- says what the measuring runs will actually use.
            out = run_driver([drv, "--lib", so, "--trial", str(t)] + bufargs,
                             timeout=120, cwd=cdir)
            if out.returncode != 0:
                return _ad.CompileResult("crashed",
                                         diagnostic=out.diagnostic()
                                         or "the driver could not load %s" % so)
            load_s = 0.0
            for _trial, phase, secs in out.compile_lines:
                if phase == "load":
                    load_s = secs
            phase_seconds.append({"emit-c": t1 - t0, "gcc": g1 - g0,
                                  "load": load_s})
            libs.append(so)
            if t == 1:
                meta, engine_why = self._metadata(out.info)
                self._giveup_bounds = (int(out.info.get("err_floor", -5)),
                                       int(out.info.get("err_giveup_top", -2)))
                artifact_bytes = os.path.getsize(so)

        handle = {"driver": drv, "lib": libs[0],
                  "giveup_range": getattr(self, "_giveup_bounds", (-5, -2)),
                  "buffer_args": bufargs}
        return _ad.CompileResult("compiled", phase_seconds=phase_seconds,
                                 engine_metadata=meta, handle=handle,
                                 artifact_bytes=artifact_bytes,
                                 diagnostic=engine_why)

    def _metadata(self, info):
        """The driver's `info` pairs -> declared engine_metadata, plus the
        prose `engine_why` which is returned SEPARATELY: requirements 4.2 is
        explicit that it is kept only as an unindexed diagnostic string."""
        meta = {}
        for name in INT_PAIRS:
            if name in info:
                meta[name] = int(info[name])
        if "engine" in info:
            meta["engine"] = info["engine"]
        if "prefilter" in info:
            meta["prefilter"] = info["prefilter"]
        for name in MASK_BITS:
            if name in info:
                meta[name] = _mask_names(name, int(info[name], 0))
        why = info.get("engine_why")
        return meta, ("RX_ENGINE_WHY: %s" % why) if why else None

    # -------------------------------------------------------------- measure

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        from pcrecbench.subbench import REGIME_MODE
        argv = [handle["driver"], "--lib", handle["lib"],
                "--mode", REGIME_MODE[regime], "--iters", str(iters)]
        if regime == "throughput":
            argv.append("--find-all")
        argv += list(handle.get("buffer_args") or [])
        return per_trial(argv, subjects, trials, timeout=timeout,
                         pin=handle.get("pin"),
                         subject_timeout=handle.get("subject_timeout"))
