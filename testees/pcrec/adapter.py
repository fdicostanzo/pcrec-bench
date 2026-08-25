"""testees/pcrec/adapter.py -- the pcrec adapter (harness contract 3).

Provides `pcrec-auto`, `pcrec-nocaps`, `pcrec-vm`, all at the pin in
`configs.toml`.

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
from pcrecbench.driverrun import (C_ENV, build_driver,       # noqa: E402
                                  per_trial, run_driver)

HERE = os.path.dirname(os.path.abspath(__file__))
PIN_SH = os.path.join(HERE, "pin.sh")
PCREC_SRC = os.environ.get("PCREC_SRC", "/home/duxevents/pcrec")

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
             "work_budget", "frame_capacity", "subject_ceiling")


def _mask_names(name, value):
    out = [bit for bit, mask in MASK_BITS[name] if value & mask]
    unknown = value & ~sum(m for _b, m in MASK_BITS[name])
    if unknown:
        raise _ad.AdapterError(
            "%s carries bit(s) 0x%x this adapter has no name for. pcrec grew "
            "a stamp bit; add it to MASK_BITS and to METADATA_DECL together, "
            "or the record would claim a mask it cannot spell." % (name, unknown))
    return out


class Adapter(_ad.Adapter):
    name = "pcrec"

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

    # ------------------------------------------------------------- describe

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        full, desc = self.pin_provenance()
        # record_schema.md 6.2: where a testee is pinned to a VCS revision
        # rather than a release -- "which is pcrec ALWAYS" -- engine_commit
        # carries the 40-hex and engine_version a git-describe-shaped string,
        # and the binding rule is that the version be REPRODUCIBLE from the
        # commit. `git describe --always` is exactly that function of it.
        version = re.sub(r"[^A-Za-z0-9._+-]", "-", desc)
        return {
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
            "build_flags": "pin %s (%s); pcrec flags %s; artifact built with "
                           "$CC -O2 -fPIC -shared"
                           % (self.pin(), desc, " ".join(cfg.get("flags", []))),
            "runtime_options": [{"name": f.split("=")[0], "value":
                                 f.split("=", 1)[1] if "=" in f else True}
                                for f in cfg.get("flags", [])
                                if f.startswith("--")],
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

    # -------------------------------------------------------------- prepare

    def prepare(self, testee_id, workdir):
        self.config(testee_id)
        os.makedirs(workdir, exist_ok=True)
        self.pin_binary()
        build_driver(os.path.join(HERE, "driver.c"),
                     os.path.join(workdir, "pcrec_driver"), extra=["-ldl"])

    # -------------------------------------------------------------- compile

    def compile(self, testee_id, pattern_id, pattern, options, trials,
                workdir):
        import time
        cfg = self.config(testee_id)
        pcrec = self.pin_binary()
        drv = build_driver(os.path.join(HERE, "driver.c"),
                           os.path.join(workdir, "pcrec_driver"), extra=["-ldl"])
        cc = os.environ.get("CC", "gcc")

        phase_seconds = []
        libs = []
        meta = {}
        engine_why = None
        artifact_bytes = None

        for t in range(1, trials + 1):
            # per-PATTERN, per-TRIAL scratch: see Adapter.compile's
            # docstring for the bug this shape exists to prevent.
            cdir = os.path.join(workdir, "p-" + pattern_id, "t%d" % t)
            os.makedirs(cdir, exist_ok=True)
            art_c = os.path.join(cdir, "artifact.c")
            patfile = os.path.join(cdir, "pattern.rx")
            with open(patfile, "wb") as f:
                f.write(pattern)

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
            out = run_driver([drv, "--lib", so, "--trial", str(t)],
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
                artifact_bytes = os.path.getsize(so)

        handle = {"driver": drv, "lib": libs[0]}
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
        return per_trial(argv, subjects, trials, timeout=timeout,
                         pin=handle.get("pin"),
                         subject_timeout=handle.get("subject_timeout"))
