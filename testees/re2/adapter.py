"""testees/re2/adapter.py -- the RE2 adapter (harness contract 3; [B42] L6b,
2026-09-17, the first lane of capability_set_v1.md 11.1's per-new-engine
roster).

Provides `re2-default` (`RE2::Options::max_mem` at its library default,
8 MiB; `perl-leftmost-first`) and `re2-longest` (`set_longest_match(true)`;
`posix-leftmost-longest`) -- capability_set_v1.md 8's two v1 RE2 configs.
`re2-bigmem` is explicitly `later` (capability_set_v1.md 8) and is NOT
built here.

A DIRECT RE2 C++ driver, not `cre2` (docs/dev/research/2026-09-12-b42-
engine-landscape.md (2), CLOSED -- `libre2-dev` is already installed and
pkg-config-discoverable; `cre2` needs a four-package autotools bootstrap
this box lacks to build a project that has never been release-tagged).
`prepare()` runs its own g++/pkg-config compile+link step -- NOT
`pcrecbench.driverrun.build_driver()`, which assumes a C compiler and
knows nothing about `pkg-config --cflags --libs re2`'s dozen Abseil
libraries.

COMPILE COST (requirements 3, capability_set_v1.md 7.1/7.2): ONE phase,
`compile` -- the `RE2(pattern, options)` CONSTRUCTOR call, timed in-driver.
`execution_model = "eager-jit"`, the closest existing token
(capability_set_v1.md 7.1's own row for RE2: "an explicit, separately-
timeable construction call" -- the same test `requirements.md 3` uses to
define eager-jit) -- WITH THE STATED CAVEAT this project's own research
found and rules on (7.2's RECOMMENDATION): RE2's runtime DFA is NOT fully
built at construction -- it is built LAZILY at first match, cached, and
can be flushed and rebuilt under `max_mem` pressure. `ProgramSize()`/
`ReverseProgramSize()` measure the forward/reverse PROGRAM (re2.h's own
words: "a very approximate measure of a regexp's cost"), not the runtime
DFA. `testee.compile_cost_definition` states this caveat on every record
(the reporter's 7.2 footnote rule fires automatically when a report pools
RE2 beside pcre2-jit under one `eager-jit` table, since their
`compile_cost_definition` strings differ).
"""

import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench import adapters as _ad          # noqa: E402
from pcrecbench.driverrun import run_driver, per_trial, C_ENV  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

DEFAULT_MAX_MEM = 8 << 20  # RE2::Options::kDefaultMaxMem, re2.h

# record_schema.md 7 rule 1: DECLARE BEFORE USE.
METADATA_DECL = {
    "ncapturegroups": {
        "type": "integer", "scope": "pattern",
        "source": "RE2::NumberOfCapturingGroups()",
        "description": "lexical capturing groups in the pattern (the "
                       "overall match, group 0, is not counted -- re2.h's "
                       "own convention)",
    },
    "program_size": {
        "type": "integer", "scope": "pattern",
        "source": "RE2::ProgramSize()",
        "description": "the forward Prog's size -- requirements 4.2's "
                       "'program size' for this engine. re2.h's own words: "
                       "'a very approximate measure of a regexp's cost'. "
                       "NOT the runtime DFA, which is built lazily at "
                       "match time (capability_set_v1.md 7.1)",
    },
    "reverse_program_size": {
        "type": "integer", "scope": "pattern",
        "source": "RE2::ReverseProgramSize()",
        "description": "the reverse Prog's size, used as the second phase "
                       "of an unanchored search (re2.h); RE2 has two "
                       "programs where pcre2/pcrec have one, so this is "
                       "declared as its own pair rather than folded into "
                       "program_size",
    },
    # [B95] (2026-09-26): emitted by compile() on every did-not-compile row
    # since the adapter landed, but never DECLARED -- no committed re2
    # record had refused until utf8@0.1's prp-greek-sc / prp-ingreek, whose
    # record X15 then rejected at store.write. Same shape as rust's/onig's.
    "refusal_class": {
        "type": "string", "scope": "pattern",
        "source": "the RE2::ErrorCode name the driver embeds in its `error` "
                  "line on a did-not-compile outcome, bucketed by this "
                  "adapter's REFUSAL_CLASS table (capability_set_v1.md 5.5: "
                  "'declared ONLY by a config whose engine gives a closed, "
                  "structural signal' -- RE2::ErrorCode is exactly that)",
        "description": "'size-limit' for ErrorPatternTooLarge; 'syntax' for "
                       "every other named ErrorCode; ABSENT when the "
                       "diagnostic carries no parseable code",
    },
}

# RE2::ErrorCode (re2.h, fetched verbatim by docs/dev/research/2026-09-12-
# b42-engine-landscape.md 3, reproduced here for classification only --
# the NAME is what the driver embeds in its `error` line's brackets, e.g.
# "RE2 construction failed [ErrorMissingParen]: missing )"). ONE code is
# size-shaped ("pattern too large (compile failed)" -- re2.h's own
# comment); every other code is a genuine parse/syntax error. RE2 exposes
# no third, resource-limit-shaped compile refusal the way pcre2's
# MATCHLIMIT/DEPTHLIMIT family does -- there is nothing budget-shaped to
# decline at RE2 CONSTRUCTION time beyond parsing and this one size cap
# (docs/design/capability_set_v1.md 5.5's own "declared ONLY by a config
# whose engine gives a closed, structural signal" rule -- RE2 is named in
# that list by name).
REFUSAL_CLASS = {
    "ErrorPatternTooLarge": "size-limit",
    # every other named code is a syntax error:
    "ErrorInternal": "syntax", "ErrorBadEscape": "syntax",
    "ErrorBadCharClass": "syntax", "ErrorBadCharRange": "syntax",
    "ErrorMissingBracket": "syntax", "ErrorMissingParen": "syntax",
    "ErrorUnexpectedParen": "syntax", "ErrorTrailingBackslash": "syntax",
    "ErrorRepeatArgument": "syntax", "ErrorRepeatSize": "syntax",
    "ErrorRepeatOp": "syntax", "ErrorBadPerlOp": "syntax",
    "ErrorBadUTF8": "syntax", "ErrorBadNamedCapture": "syntax",
    "ErrorInternal ": "syntax",
}

_ERROR_LINE_RE = re.compile(r"RE2 construction failed \[(\w+)\]: (.*)", re.S)


def classify_refusal(diagnostic):
    """-> (refusal_class, error_code_name) from the driver's own `error`
    line text, or (None, None) if the line is not in the expected shape
    (a driver bug, never silently swallowed)."""
    if not diagnostic:
        return None, None
    m = _ERROR_LINE_RE.search(diagnostic)
    if not m:
        return None, None
    code = m.group(1)
    return REFUSAL_CLASS.get(code, "syntax"), code


def _pkg_config(*args):
    out = subprocess.run(["pkg-config"] + list(args), capture_output=True,
                         text=True, check=True)
    return out.stdout.split()


def _probe_version():
    """PROBED, never typed -- but RE2 itself exposes NO runtime version
    query (no RE2_VERSION symbol, no version-string API; confirmed absent
    by reading /usr/include/re2/re2.h in full). The closest honest
    equivalent this project's other adapters use (pcre2: pcre2_config;
    pcrec: git describe on the pinned commit) is the INSTALLED PACKAGE's
    own metadata -- pkg-config's `re2.pc` Version field (the shared
    library's ABI/soname version, e.g. "11.0.0") is the probed
    `engine_version`; the Debian package version (RE2's actual upstream
    snapshot date, e.g. "20250805-1build3", Google's own date-based
    release convention -- RE2 has no semantic version) rides along in
    `build_flags` for full provenance, exactly as pcre2-jit's build date
    does. Neither is typed into configs.toml; both are read here, live,
    from the box's package database at describe() time."""
    try:
        modver = subprocess.run(["pkg-config", "--modversion", "re2"],
                                capture_output=True, text=True,
                                check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        raise _ad.AdapterError("pkg-config --modversion re2 failed: %s" % e)
    pkgver = None
    try:
        pkgver = subprocess.run(
            ["dpkg-query", "-W", "-f=${Version}", "libre2-dev"],
            capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass  # non-Debian box: modver alone is still a real probe
    return modver, pkgver


class Adapter(_ad.Adapter):
    name = "re2"

    # ------------------------------------------------------------- describe

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        enc, enc_extra = _ad.config_encoding(testee_id, cfg)
        modver, pkgver = _probe_version()
        build_note = ("RE2 has no runtime version API (confirmed absent, "
                      "re2.h read in full); engine_version is pkg-config's "
                      "re2.pc Version field (the library's soname/ABI "
                      "version). The Debian package %s (RE2's own "
                      "upstream snapshot date, its de facto release "
                      "identifier) rides here for full provenance."
                      % (pkgver or "version unavailable"))
        if enc == "utf8":
            # [B77] U2: named in build_flags ONLY for the utf8 config, so
            # every Latin-1 config's build_flags is byte-identical to its
            # pre-[B77] rendering.
            build_note += ("; ENGINE ENCODING utf8 ([B77] U2, utf8_set_v1.md "
                           "7.1): RE2::Options::EncodingUTF8 -- RE2's own "
                           "default, which every other config of this "
                           "adapter overrides to EncodingLatin1 (driver "
                           "--encoding utf8)")
        block = {
            "engine_name": "re2",
            "engine_version": modver,
            "engine_commit": None,
            "execution_model": "eager-jit",
            "automaton_class": "nfa-simulation",
            "openness": "open-source",
            "license_id": "BSD-3-Clause",
            "conventions": ([ "posix-leftmost-longest" ] if cfg.get("longest")
                            else ["perl-leftmost-first"]),
            "captures": "on",
            "engine_mode": cfg["engine_mode"],
            "simd": "n-a",
            "build_flags": build_note,
            # schema named_value objects, never bare strings (KB-21: the
            # re2-longest first sample's whole cell measured, then the
            # record was refused at store.write -- 'longest_match=true'
            # is not of type 'object'. pcre2/pcrec emit [] here, so no
            # prior testee ever exercised a non-empty entry's shape).
            "runtime_options": (([{"name": "longest_match", "value": True}]
                                 if cfg.get("longest") else [])
                                + ([{"name": "encoding", "value": "utf8"}]
                                   if enc == "utf8" else [])),
            "compile_cost_definition": (
                "eager-jit-adjacent (capability_set_v1.md 7.1/7.2): the "
                "explicit RE2(pattern, options) CONSTRUCTOR call, timed "
                "in-driver (`compile`). CAVEAT: unlike pcre2-jit's "
                "pcre2_jit_compile, this call does NOT build the runtime "
                "DFA -- RE2's DFA is built LAZILY at first match, cached, "
                "and can be flushed and rebuilt under max_mem pressure "
                "(re2.h). A reader pooling this testee beside pcre2-jit "
                "under one eager-jit table is comparing two different "
                "compile-cost SHAPES that happen to share a class token; "
                "the reporter's 7.2 footnote fires on exactly this "
                "definition-string mismatch. Median of N with spread is "
                "the REPORTER's reduction."
            ),
            "compile_phases": ["compile"],
            "warmup_trials": 0,
            "engine_metadata_declaration": dict(METADATA_DECL),
        }
        # [B77] U2: the ENGINE encoding is an identity -- `re2-utf8` derives
        # `re2-default`'s id plus `_utf8`; absent on every Latin-1 config.
        if enc_extra:
            block["config_extra"] = enc_extra
        return block

    def binary_identity(self, testee_id, workdir=None):
        """`testee.binary` for a scratch-tier record (X29): the installed
        libre2.so this driver links against, resolved the same way
        testees/pcre2/adapter.py resolves its dlopen'd library -- except
        RE2 is LINKED, not dlopen'd, so the path is read from the built
        driver's own dynamic section via `ldd` rather than
        /proc/self/maps (no process of this python interpreter has libre2
        mapped)."""
        drv = self.prepare_driver(workdir or os.getcwd())
        proc = subprocess.run(["ldd", drv], capture_output=True, text=True,
                              check=True)
        path = None
        for line in proc.stdout.splitlines():
            if "libre2.so" in line and "=>" in line:
                cand = line.split("=>", 1)[1].strip().split()[0]
                if cand and cand != "not":
                    path = cand
                    break
        if not path or not os.path.exists(path):
            raise _ad.AdapterError(
                "cannot find libre2.so in `ldd %s`; a scratch record must "
                "name the binary (X29)" % drv)
        return {"path": os.path.realpath(path),
                "sha256": _ad.sha256_file(os.path.realpath(path))}

    # -------------------------------------------------------------- prepare

    def prepare_driver(self, workdir):
        """Build driver.cc with g++ + pkg-config, NOT
        pcrecbench.driverrun.build_driver() -- that helper assumes a C
        compiler and a flat `extra` link-flags list; RE2 needs `pkg-config
        --cflags --libs re2` (a dozen-plus Abseil libraries, order-
        sensitive on some linkers), which is exactly the "an adapter's own
        prepare() may run its own g++ step" route docs/dev/research/
        2026-09-12-b42-engine-landscape.md (2) recommends."""
        src = os.path.join(HERE, "driver.cc")
        out = os.path.join(workdir, "re2_driver")
        cxx = os.environ.get("CXX", "g++")
        cflags = _pkg_config("--cflags", "re2")
        libs = _pkg_config("--libs", "re2")
        argv = ([cxx, "-O2", "-std=c++17"] + cflags
               + ["-o", out, src] + libs)
        # Registered even on the cached path (pcrecbench.driverrun.
        # build_driver's own discipline, quoted): the record must state
        # how the driver that produced its numbers was built, not only
        # how one that happened to be rebuilt this run was.
        from pcrecbench import driverrun as _dr, env as _env
        _dr.DRIVER_BUILDS[os.path.abspath(out)] = {
            "command_line": list(argv),
            "compiler": _env.canon_compiler(_env.compiler_raw(cxx)),
        }
        if (os.path.exists(out)
                and os.path.getmtime(out) >= os.path.getmtime(src)):
            return out
        os.makedirs(workdir, exist_ok=True)
        proc = subprocess.run(argv, capture_output=True, text=True,
                              env=C_ENV, timeout=600)
        if proc.returncode != 0:
            raise _ad.AdapterError("building %s failed:\n%s\n%s"
                                   % (src, " ".join(argv), proc.stderr))
        return out

    def prepare(self, testee_id, workdir):
        self.config(testee_id)
        self.prepare_driver(workdir)

    # -------------------------------------------------------------- compile

    def compile(self, testee_id, pattern_id, pattern, options, trials,
               workdir, requires_free_spacing=False):
        # [B70]: unused -- RE2's `FullMatch` anchors the `match` regime
        # against the SAME artifact, no `whole-subject` wrap to fix.
        del requires_free_spacing
        cfg = self.config(testee_id)
        drv = self.prepare_driver(workdir)
        # per-PATTERN scratch: see Adapter.compile's docstring -- the same
        # bug class (a shared workdir/pattern.rx clobbered by the next
        # pattern) is possible here as it was for pcre2.
        pdir = os.path.join(workdir, "p-" + pattern_id)
        os.makedirs(pdir, exist_ok=True)
        patfile = os.path.join(pdir, "pattern.rx")
        # RAW BYTES, end to end (inbox I-72's lesson): the pattern is
        # written to a FILE, never placed on a subprocess argv element, so
        # this adapter is not exposed to the fsencode/latin-1 mojibake
        # class the pcrec adapter hit (its pattern travels on argv,
        # testees/pcrec/adapter.py's own I-72 fix comment) -- but the file
        # write itself must still be BINARY, unconditionally, or the same
        # class of corruption re-enters through a text-mode encode.
        with open(patfile, "wb") as f:
            f.write(bytes(pattern))
        argv = [drv, "--pattern", patfile, "--compile-trials", str(trials)]
        if cfg.get("longest"):
            argv.append("--longest")
        max_mem = cfg.get("max_mem", DEFAULT_MAX_MEM)
        argv += ["--max-mem", str(max_mem)]
        utf = _ad.config_encoding(testee_id, cfg)[0] == "utf8"
        if utf:
            argv += ["--encoding", "utf8"]      # [B77] U2
        out = run_driver(argv, timeout=max(60, 30 * trials), cwd=workdir)

        def one(res):
            # RE2 anchors with the Match() call's own `Anchor` parameter
            # (UNANCHORED / ANCHOR_BOTH), a RUNTIME choice on the same
            # compiled RE2 object -- exactly pcre2's PCRE2_ANCHORED|
            # PCRE2_ENDANCHORED shape, so RE2 needs no second artifact and
            # emits only the `plain` form.
            return _ad.CompiledPattern({_ad.FORM_PLAIN: res})

        if out.timed_out:
            return one(_ad.CompileResult("timed-out",
                                         diagnostic=out.diagnostic()))
        if out.returncode == 3:
            diag = out.diagnostic() or "RE2 construction failed"
            rclass, code = classify_refusal(diag)
            meta = {}
            decl_ref = None
            # refusal_class is PATTERN-scoped engine_metadata (5.5) --
            # attached even on a did-not-compile row, same convention
            # pcre2's own GAVE_UP_CODES classification documents (a
            # structural fact about WHY, not an outcome of its own).
            return one(_ad.CompileResult(
                "did-not-compile", diagnostic=diag,
                engine_metadata=({"refusal_class": rclass} if rclass
                                 else {}),
                declaration_ref=decl_ref))
        if out.returncode != 0:
            return one(_ad.CompileResult("crashed",
                                         diagnostic=out.diagnostic()
                                         or "driver exit %s" % out.returncode))

        meta = {}
        for name in METADATA_DECL:
            if name in out.info and name != "refusal_class":
                meta[name] = int(out.info[name])
        handle = {"driver": drv, "pattern_file": patfile,
                  "longest": bool(cfg.get("longest")),
                  "max_mem": max_mem, "utf": utf}
        return one(_ad.CompileResult(
            "compiled", phase_seconds=out.phase_seconds,
            engine_metadata=meta, handle=handle,
            artifact_bytes=meta.get("program_size")))

    # -------------------------------------------------------------- measure

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        from pcrecbench.subbench import REGIME_MODE
        argv = [handle["driver"], "--pattern", handle["pattern_file"],
                "--mode", REGIME_MODE[regime], "--iters", str(iters),
                "--max-mem", str(handle["max_mem"])]
        if handle["longest"]:
            argv.append("--longest")
        if handle.get("utf"):
            # [B77] U2: the measure-time driver rebuilds the RE2 object, so
            # the ENGINE encoding rides here too -- never a Latin-1 stand-in.
            argv += ["--encoding", "utf8"]
        if regime == "throughput":
            argv.append("--find-all")
        if handle.get("utf8_advance"):
            # [B77] U1: the character-boundary find-all advance (the
            # driver protocol, pcrecbench/adapters.py), set by the harness
            # from the SAME fact as the oracle word's PCRE2_UTF.
            argv.append("--utf8")
        return per_trial(argv, subjects, trials, timeout=timeout,
                         pin=handle.get("pin"),
                         subject_timeout=handle.get("subject_timeout"))
