"""testees/pcre2/adapter.py -- the libpcre2 adapter (harness contract 3).

Provides `pcre2-interp` (execution model `interpretive`) and `pcre2-jit`
(`eager-jit`). One `driver.c`, built once per workdir; the two testees differ
only in whether it is invoked with `--jit`.

COMPILE COST (requirements 3, per execution-model class):
  * pcre2-interp -- one phase, `compile`: `pcre2_compile_8`, timed in-driver.
  * pcre2-jit    -- two phases, `compile` then `jit-compile`: the explicit
                    `pcre2_compile_8` + `pcre2_jit_compile_8(PCRE2_JIT_
                    COMPLETE)` pair. An EAGER JIT has a separable call, so
                    there is a number to take; `warmup_trials` is 0 because
                    nothing warms after the compile (that is the LAZY-JIT
                    protocol, and pcre2's JIT is not one).
"""

import os
import subprocess

import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench import adapters as _ad          # noqa: E402
from pcrecbench.driverrun import build_driver, run_driver, per_trial  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

# record_schema.md 7 rule 1: DECLARE BEFORE USE. Every name the driver can
# emit as an `info` line and the adapter forwards as a pattern-scoped pair is
# here, with its type and the source that produced it. The driver's own
# [measured] block is the evidence for the `pcre2_pattern_info_8` codes.
METADATA_DECL = {
    "capturecount": {
        "type": "integer", "scope": "pattern",
        "source": "pcre2_pattern_info_8(code, 4 /* PCRE2_INFO_CAPTURECOUNT */, &u32)",
        "description": "lexical capturing groups in the pattern",
    },
    "compiled_size_bytes": {
        "type": "integer", "scope": "pattern",
        "source": "pcre2_pattern_info_8(code, 22 /* PCRE2_INFO_SIZE */, &size_t)",
        "description": "size of the compiled pattern block -- requirements 4.2's "
                       "'program size' for this engine",
    },
    "jit_size_bytes": {
        "type": "integer", "scope": "pattern",
        "source": "pcre2_pattern_info_8(code, 10 /* PCRE2_INFO_JITSIZE */, &size_t)",
        "description": "size of the JIT-compiled machine code; absent on the "
                       "interpreter testee (an ABSENT pair is not an error, "
                       "an UNDECLARED one is)",
    },
}


# The RESOURCE-LIMIT refusals: negative `pcre2_match` returns where the
# engine declined to answer because a configured budget ran out, as opposed
# to answering wrongly or failing. Schema v1.1's per-subject `gave-up`
# outcome is for exactly these; every other negative code is `crashed`.
#
# [measured] 2026-08-25 against this box's libpcre2 10.46, by forcing each
# limit with pcre2_set_match_limit_8 / pcre2_set_depth_limit_8 on `^(a+)+$`
# over 200 `a`s and reading the returned code, then sweeping
# pcre2_get_error_message over -70..-1 to catch the siblings. NOT read from a
# header -- there is no pcre2.h on this box.
GAVE_UP_CODES = {
    -47: "PCRE2_ERROR_MATCHLIMIT",      # "match limit exceeded"      (forced)
    -53: "PCRE2_ERROR_DEPTHLIMIT",      # "matching depth limit ..."  (forced)
    -63: "PCRE2_ERROR_HEAPLIMIT",       # "heap limit exceeded"
    -46: "PCRE2_ERROR_JIT_STACKLIMIT",  # "JIT stack limit reached"
}
# Deliberately NOT in the set, and each for a stated reason:
#   -48 "no more memory"  -- an allocation failure, not a configured budget;
#        the box ran out, the engine did not decline. `crashed`.
#   -52 "nested recursion at the same subject position" -- a SEMANTIC refusal
#        (PCRE2 10.46's recursion-loop rule), not a resource limit.
#   -1  "no match"        -- an answer, not a refusal.


class Adapter(_ad.Adapter):
    name = "pcre2"

    # ------------------------------------------------------------- describe

    def probe_version(self, workdir):
        """PROBED, never typed: the version string the loaded library reports.
        `pcre2_config(PCRE2_CONFIG_VERSION)` gives `10.46 2025-08-27`; the
        record's `engine_version` is a version_string (no spaces), so the
        release number is the first token and the date rides along in
        `build_flags`."""
        drv = self.prepare_driver(workdir)
        out = run_driver([drv, "--pattern", os.path.join(HERE, "_probe.rx")],
                         timeout=60, cwd=workdir)
        for name, value in out.info.items():
            if name == "version":
                return value
        raise _ad.AdapterError("the pcre2 driver reported no version")

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        raw = self.probe_version(workdir or os.getcwd())
        version = raw.split()[0]
        jit = bool(cfg.get("jit"))
        phases = ["compile", "jit-compile"] if jit else ["compile"]
        decl = dict(METADATA_DECL)
        if not jit:
            del decl["jit_size_bytes"]
        return {
            "engine_name": "libpcre2",
            "engine_version": version,
            "engine_commit": None,
            "execution_model": "eager-jit" if jit else "interpretive",
            "automaton_class": "backtracking",
            "openness": "open-source",
            "license_id": "BSD-3-Clause",
            "conventions": ["perl-leftmost-first"],
            "captures": cfg.get("captures", "on"),
            "engine_mode": cfg["engine_mode"],
            "simd": "n-a",
            "build_flags": "distribution libpcre2-8.so.0 (%s), loaded with "
                           "dlopen; driver built with $CC -O2 -std=gnu11" % raw,
            "runtime_options": [],
            "compile_cost_definition": (
                "eager JIT (requirements 3): the explicit compile calls, timed "
                "in-driver -- pcre2_compile_8 (`compile`) then "
                "pcre2_jit_compile_8(PCRE2_JIT_COMPLETE) (`jit-compile`). "
                "Median of N with spread is the REPORTER's reduction."
                if jit else
                "interpreter (requirements 3): the compile call, timed "
                "in-driver -- pcre2_compile_8 (`compile`). Median of N with "
                "spread is the REPORTER's reduction."),
            "compile_phases": phases,
            "warmup_trials": 0,
            "engine_metadata_declaration": decl,
        }

    def binary_identity(self, testee_id, workdir=None):
        """`testee.binary` for a scratch-tier record (schema v1.2, X29): the
        distribution libpcre2-8.so.0 the driver dlopens, resolved to the
        file the dynamic loader actually maps -- read from /proc/self/maps
        after loading it here, the same soname the driver asks for -- and
        its sha256. Not `find_library`, which returns a soname, not a
        path."""
        import ctypes
        soname = "libpcre2-8.so.0"
        try:
            ctypes.CDLL(soname)
        except OSError as e:
            raise _ad.AdapterError("cannot load %s: %s" % (soname, e))
        path = None
        try:
            with open("/proc/self/maps", "r", encoding="utf-8",
                      errors="replace") as f:
                for line in f:
                    cand = line.split()[-1] if line.strip() else ""
                    if os.path.basename(cand).startswith("libpcre2-8.so"):
                        path = cand
                        break
        except OSError:
            pass
        if not path or not os.path.exists(path):
            raise _ad.AdapterError(
                "loaded %s but could not find its file in /proc/self/maps; "
                "a scratch record must name the binary (X29)" % soname)
        return {"path": os.path.realpath(path),
                "sha256": _ad.sha256_file(path)}

    # -------------------------------------------------------------- prepare

    def prepare_driver(self, workdir):
        return build_driver(os.path.join(HERE, "driver.c"),
                            os.path.join(workdir, "pcre2_driver"),
                            extra=["-ldl"])

    def prepare(self, testee_id, workdir):
        self.config(testee_id)
        os.makedirs(workdir, exist_ok=True)
        probe = os.path.join(HERE, "_probe.rx")
        if not os.path.exists(probe):
            with open(probe, "wb") as f:
                f.write(b"a")
        self.prepare_driver(workdir)

    # -------------------------------------------------------------- compile

    def compile(self, testee_id, pattern_id, pattern, options, trials,
                workdir):
        cfg = self.config(testee_id)
        drv = self.prepare_driver(workdir)
        # per-PATTERN scratch: see Adapter.compile's docstring.
        pdir = os.path.join(workdir, "p-" + pattern_id)
        os.makedirs(pdir, exist_ok=True)
        patfile = os.path.join(pdir, "pattern.rx")
        with open(patfile, "wb") as f:
            f.write(pattern)
        argv = [drv, "--pattern", patfile, "--compile-trials", str(trials)]
        if cfg.get("jit"):
            argv.append("--jit")
        out = run_driver(argv, timeout=max(60, 30 * trials), cwd=workdir)

        def one(res):
            # libpcre2 anchors with RUNTIME OPTIONS
            # (PCRE2_ANCHORED|PCRE2_ENDANCHORED on the same compiled pattern),
            # so it needs no second artifact and emits only the `plain` form.
            # The schema reads an ABSENT `form` as `plain`, so its rows are
            # unchanged by v1.1's fix 22.
            return _ad.CompiledPattern({_ad.FORM_PLAIN: res})

        if out.timed_out:
            return one(_ad.CompileResult("timed-out",
                                         diagnostic=out.diagnostic()))
        if out.returncode == 3:
            return one(_ad.CompileResult("did-not-compile",
                                         diagnostic=out.diagnostic()
                                         or "pcre2_compile failed"))
        if out.returncode != 0:
            return one(_ad.CompileResult("crashed",
                                         diagnostic=out.diagnostic()
                                         or "driver exit %s" % out.returncode))

        meta = {}
        for name in METADATA_DECL:
            if name in out.info:
                meta[name] = int(out.info[name])
        # The MEASURED set of libpcre2 resource-limit refusals travels with
        # the handle, so harness.classify_giveup needs no engine knowledge.
        handle = {"driver": drv, "pattern_file": patfile,
                  "jit": bool(cfg.get("jit")),
                  "giveup_codes": set(GAVE_UP_CODES)}
        return one(_ad.CompileResult(
            "compiled", phase_seconds=out.phase_seconds,
            engine_metadata=meta, handle=handle,
            artifact_bytes=meta.get("compiled_size_bytes")))

    # -------------------------------------------------------------- measure

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        from pcrecbench.subbench import REGIME_MODE
        argv = [handle["driver"], "--pattern", handle["pattern_file"],
                "--mode", REGIME_MODE[regime], "--iters", str(iters)]
        if handle["jit"]:
            argv.append("--jit")
        if regime == "throughput":
            argv.append("--find-all")
        return per_trial(argv, subjects, trials, timeout=timeout,
                         pin=handle.get('pin'),
                         subject_timeout=handle.get('subject_timeout'))
