r"""testees/rust/adapter.py -- the rust-regex adapter (harness contract 3;
[B7]/L6b, lane l6brust, 2026-09-19 -- the last unchartered engine on
capability_set_v1.md's roster).

Provides `rust-default` only (`RegexBuilder` at the crate's own documented
defaults -- capability_set_v1.md 8's `regex-default` roster row, renamed
to match this directory's own `<engine>-<mode>` convention, see
testees/rust/CLAUDE.md's naming note). `rust-smallsize` (a LOW
`size_limit`, exercising `CompiledTooBig` as a first-class refusal --
capability_set_v1.md 8's `regex-smallsize` row) is NOT built by this
lane; its brief named it explicitly as `rust-default` first, "more only
if the census motivates".

A NATIVE Rust driver (`src/main.rs`), never a C/C++ driver linked against
a C ABI -- the `regex` crate has none worth adding as a dependency
(`regex-capi`/`rure` is unmaintained tooling this project does not need,
per inbox I-76's own ruling: "no 'cargo install line' concern exists on
our side"). `prepare_driver()` runs `cargo build --release` --
NOT `pcrecbench.driverrun.build_driver()`, which assumes a C compiler.

COMPILE COST (requirements 3, capability_set_v1.md 7.1/7.2): ONE phase,
`compile` -- the `RegexBuilder::build()` call, timed in-driver.
`execution_model = "eager-jit"`, the same token RE2 uses, WITH THE SAME
CAVEAT (capability_set_v1.md 7.2's own recommendation, applied here
identically to testees/re2/adapter.py's docstring): the timed call parses
the pattern and builds the HIR/literal-prefilter analysis, but the lazy
DFA is built INCREMENTALLY AT MATCH TIME and cached (N2 5) -- not a full
eager machine-code compile the way `pcre2-jit`'s `pcre2_jit_compile` is.
`testee.compile_cost_definition` states this on every record; the
reporter's 7.2 footnote rule fires automatically when a report pools this
testee beside another `eager-jit` one whose `compile_cost_definition`
string differs.
"""

import os
import subprocess
import sys
import tomllib

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench import adapters as _ad          # noqa: E402
from pcrecbench import record as _rec           # noqa: E402
from pcrecbench.driverrun import run_driver, per_trial, C_ENV  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CARGO_TOML = os.path.join(HERE, "Cargo.toml")
CARGO_LOCK = os.path.join(HERE, "Cargo.lock")


def _rust_tool(name):
    """Resolve `cargo`/`rustc` robustly: rustup's standard install puts
    them in ~/.cargo/bin and reaches PATH only through the user's shell
    profile, so a bare name works interactively but FAILS in any shell
    that skipped the profile (a detached setsid runner, cron, a
    stranger's `make check` -- MEASURED: the first post-merge full
    `make check`'s check-harness died on FileNotFoundError: 'cargo'
    from exactly this, 2026-09-19). PATH first (an explicitly chosen
    toolchain wins), then the rustup home location, then a NAMED
    refusal pointing at the install step -- never a bare
    FileNotFoundError from deep inside subprocess."""
    import shutil
    found = shutil.which(name)
    if found:
        return name
    rustup_bin = os.path.join(os.path.expanduser("~"), ".cargo", "bin", name)
    if os.path.exists(rustup_bin):
        return rustup_bin
    raise _ad.AdapterError(
        f"{name} not found on PATH or in ~/.cargo/bin -- install the "
        f"pinned toolchain with rustup (testees/rust/CLAUDE.md, inbox "
        f"I-76) before running this testee")

# RegexBuilder's own documented defaults, mirrored from src/main.rs's own
# constants (the driver's compiled-in fallback if these flags are ever
# omitted) -- kept here too so configs.toml never has to repeat the raw
# numbers, and so a future `rust-smallsize` config states its override
# relative to a named default rather than a bare integer.
DEFAULT_SIZE_LIMIT = 10 << 20       # 10 MiB
DEFAULT_DFA_SIZE_LIMIT = 2 << 20    # 2 MiB

# record_schema.md 7 rule 1: DECLARE BEFORE USE.
METADATA_DECL = {
    "ncapturegroups": {
        "type": "integer", "scope": "pattern",
        "source": "Regex::captures_len() - 1",
        "description": "lexical capturing groups in the pattern (the "
                       "overall match, group 0, is not counted -- the "
                       "same convention testees/re2/adapter.py and "
                       "testees/onig/adapter.py already use)",
    },
    "named_count": {
        "type": "integer", "scope": "pattern",
        "source": "Regex::capture_names().filter(Option::is_some).count()",
        "description": "distinct named capture groups in the pattern "
                       "(testees/onig/adapter.py's `names` pair, same "
                       "shape)",
    },
    "refusal_class": {
        "type": "string", "scope": "pattern",
        "source": "the regex::Error variant name RegexBuilder::build() "
                  "returned on a did-not-compile outcome, bucketed by "
                  "this adapter (capability_set_v1.md 5.5: 'declared "
                  "ONLY by a config whose engine gives a closed, "
                  "structural signal' -- regex::Error's two named "
                  "variants, Syntax and CompiledTooBig, are exactly "
                  "that, and the type is #[non_exhaustive] so a third "
                  "variant added upstream degrades to `syntax` rather "
                  "than a crash)",
        "description": "'size-limit' for CompiledTooBig (size_limit or "
                       "dfa_size_limit exceeded); 'syntax' for every "
                       "other named variant, incl. the structural "
                       "'invalid UTF-8 pattern' refusal this adapter "
                       "raises itself before the regex crate ever sees "
                       "the pattern (see the I-72 section, "
                       "testees/rust/CLAUDE.md)",
    },
}

_ERROR_LINE_RE = None  # set below, after re import guard


def _compile_regex():
    import re as _re
    global _ERROR_LINE_RE
    if _ERROR_LINE_RE is None:
        _ERROR_LINE_RE = _re.compile(
            r"regex build failed \[(\w+)\]: (.*)", _re.S)
    return _ERROR_LINE_RE


def classify_refusal(diagnostic):
    """-> (refusal_class, variant_name) from the driver's own `error`
    line text (driver.rs's `error_variant_name`), or (None, None) if the
    line is not in the expected shape (a driver bug, never silently
    swallowed) -- OR the driver's OWN pre-regex-crate UTF-8 validation
    refusal, which carries no bracketed variant name at all and is
    always `syntax` (an encoding problem is a pattern-SYNTAX problem for
    this adapter's purposes, never a size one)."""
    if not diagnostic:
        return None, None
    if diagnostic.startswith("pattern is not valid UTF-8 at byte"):
        return "syntax", "InvalidUtf8Pattern"
    m = _compile_regex().search(diagnostic)
    if not m:
        return None, None
    name = m.group(1)
    return ("size-limit" if name == "CompiledTooBig" else "syntax"), name


def _read_cargo_lock_regex_version():
    """The PINNED `regex` crate version -- read from the COMMITTED
    Cargo.lock (real TOML, parsed with the stdlib's own tomllib, the same
    module configs.toml already uses), never typed. This is the
    `engine_version` this project's other adapters read from a live
    library probe (pcre2_config; onig_version(); RE2's pkg-config); the
    `regex` crate exposes no runtime version API of its own (confirmed
    absent, same class of fact testees/re2/adapter.py's `_probe_version`
    states for RE2 -- neither engine publishes a version-string symbol),
    so the durable, checkable substitute is the LOCKFILE inbox I-76's own
    ruling requires committing: 'the regex crate from crates.io at a
    pinned version with Cargo.lock committed'."""
    if not os.path.exists(CARGO_LOCK):
        raise _ad.AdapterError(
            "testees/rust/Cargo.lock is missing -- run `cargo build "
            "--release` in testees/rust/ once to generate and commit it "
            "(inbox I-76's own pin mechanism; HELD until pcrec's battery "
            "trailer shows DONE, per this lane's brief)")
    with open(CARGO_LOCK, "rb") as f:
        lock = tomllib.load(f)
    for pkg in lock.get("package", []):
        if pkg.get("name") == "regex":
            return pkg.get("version")
    raise _ad.AdapterError("testees/rust/Cargo.lock has no `regex` "
                           "package entry")


def _probe_rustc_version():
    """PROBED, never typed: `rustc --version`'s full line, the exact
    toolchain pin inbox I-76 asks this file to record (`rustup`'s
    `stable` channel AS IT RESOLVED at charter/build time)."""
    try:
        out = subprocess.run([_rust_tool("rustc"), "--version"],
                             capture_output=True,
                             text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        raise _ad.AdapterError("rustc --version failed: %s -- is rustup "
                               "installed under this user's home? (inbox "
                               "I-76: home-only, no sudo)" % e)
    return out


class Adapter(_ad.Adapter):
    name = "rust"

    # ------------------------------------------------------------- describe

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        regex_version = _read_cargo_lock_regex_version()
        rustc_version = _probe_rustc_version()
        return {
            "engine_name": "rust",
            "engine_version": regex_version,
            "engine_commit": None,
            "execution_model": "eager-jit",
            "automaton_class": "nfa-simulation",
            "openness": "open-source",
            "license_id": "MIT OR Apache-2.0",
            "conventions": ["perl-leftmost-first"],
            "captures": "on",
            "engine_mode": cfg["engine_mode"],
            "simd": "n-a",
            "build_flags": (
                "%s; `regex` crate %s (crates.io, pinned by the "
                "COMMITTED testees/rust/Cargo.lock, inbox I-76); driver "
                "built with `cargo build --release`; "
                "regex::bytes::RegexBuilder (byte-haystack mode -- "
                "satisfies non-utf8-subject at the SUBJECT level; the "
                "PATTERN must still be valid UTF-8, a different, "
                "structural constraint -- see testees/rust/CLAUDE.md's "
                "I-72 section)" % (rustc_version, regex_version)),
            "runtime_options": [
                {"name": "size_limit", "value": cfg.get(
                    "size_limit", DEFAULT_SIZE_LIMIT)},
                {"name": "dfa_size_limit", "value": cfg.get(
                    "dfa_size_limit", DEFAULT_DFA_SIZE_LIMIT)},
            ],
            "compile_cost_definition": (
                "eager-jit-adjacent (capability_set_v1.md 7.1/7.2): the "
                "explicit RegexBuilder::build() call, timed in-driver "
                "(`compile`). CAVEAT: like re2-default/re2-longest, this "
                "call does NOT build the runtime DFA -- the `regex` "
                "crate's lazy DFA is built INCREMENTALLY at match time "
                "and cached (N2 5). A reader pooling this testee beside "
                "pcre2-jit under one eager-jit table is comparing two "
                "different compile-cost SHAPES that happen to share a "
                "class token; the reporter's 7.2 footnote fires on "
                "exactly this definition-string mismatch. Median of N "
                "with spread is the REPORTER's reduction."
            ),
            "compile_phases": ["compile"],
            "warmup_trials": 0,
            "engine_metadata_declaration": dict(METADATA_DECL),
        }

    def binary_identity(self, testee_id, workdir=None):
        """`testee.binary` for a scratch-tier record (X29): the built
        driver BINARY itself, sha256'd -- unlike pcre2/onig/re2 (which
        dlopen/link a SHARED library this method resolves separately),
        the `regex` crate is STATICALLY linked into the cargo binary (no
        `libregex.so` exists anywhere on this box), so the driver binary
        IS the artifact whose identity this field names -- the same
        shape `testees/pcrec/adapter.py` uses for pcrec's own compiled
        `.so`/binary artifacts, not the dlopen convention pcre2/onig/re2
        share with each other."""
        drv = self.prepare_driver(workdir or os.getcwd())
        return {"path": os.path.realpath(drv),
               "sha256": _ad.sha256_file(drv)}

    # -------------------------------------------------------------- prepare

    def prepare_driver(self, workdir):
        """Build with `cargo build --release`, NOT
        pcrecbench.driverrun.build_driver() (a C-compiler assumption) --
        the same "an adapter's own prepare() may run its own build step"
        route testees/re2/adapter.py's g++/pkg-config step already sets
        precedent for. Requires testees/rust/Cargo.lock to already exist
        (committed, per inbox I-76) so the resolved `regex` version this
        build produces is the SAME one describe() reads -- `cargo build
        --locked` enforces this at the tool level rather than trusting
        convention."""
        out_dir = os.path.join(workdir, "rust_target")
        argv = [_rust_tool("cargo"), "build", "--release", "--locked",
               "--manifest-path", CARGO_TOML, "--target-dir", out_dir]
        # Registered even on the cached path (pcrecbench.driverrun.
        # build_driver's own discipline, quoted by testees/re2/
        # adapter.py): the record must state how the driver that
        # produced its numbers was built.
        from pcrecbench import driverrun as _dr, env as _env
        drv = os.path.join(out_dir, "release", "rust_regex_driver")
        _dr.DRIVER_BUILDS[os.path.abspath(drv)] = {
            "command_line": list(argv),
            "compiler": _env.canon_compiler(_env.compiler_raw(_rust_tool("rustc"))),
        }
        src_mtime = max(
            os.path.getmtime(os.path.join(HERE, "src", "main.rs")),
            os.path.getmtime(CARGO_TOML), os.path.getmtime(CARGO_LOCK))
        if os.path.exists(drv) and os.path.getmtime(drv) >= src_mtime:
            return drv
        os.makedirs(out_dir, exist_ok=True)
        proc = subprocess.run(argv, capture_output=True, text=True,
                              env=C_ENV, timeout=600)
        if proc.returncode != 0:
            raise _ad.AdapterError("building %s failed:\n%s\n%s"
                                   % (CARGO_TOML, " ".join(argv),
                                      proc.stderr))
        return drv

    def prepare(self, testee_id, workdir):
        self.config(testee_id)
        self.prepare_driver(workdir)

    # -------------------------------------------------------------- compile

    def compile(self, testee_id, pattern_id, pattern, options, trials,
               workdir, requires_free_spacing=False):
        r"""TWO artifacts per pattern, `plain` and `whole-subject` -- same
        two-artifact shape testees/onig/adapter.py's own compile()
        docstring states, for a DIFFERENT structural reason: the `regex`
        crate exposes NO runtime anchored-search option at all (unlike
        pcre2/RE2's runtime anchor flags, or even Oniguruma's
        onig_match-at-a-fixed-position call), so `whole-subject` is NOT
        `pcrecbench.record.whole_subject_text(pattern)` (`(?:pattern)\z`)
        -- that wrap alone would UNDER-anchor here, matching a SUFFIX of
        the subject rather than the whole thing, since `find()` always
        scans unanchored from position 0 forward. This adapter bakes
        BOTH anchors into the compiled text itself: `\A(?:pattern)\z`
        (or `\A(?:pattern\n)\z` when `requires_free_spacing` -- [B70],
        the SAME conditional rule `record.whole_subject_text` states in
        full, applied here because this wrap is NOT built through that
        shared function). See testees/rust/CLAUDE.md and src/main.rs's
        own header for the full derivation; TRE's own lane set the
        precedent for building an adapter-specific wrap rather than
        reusing the shared helper, for its own different reason (no `\z`
        spelling at all)."""
        ws_pattern = pattern + b"\n" if requires_free_spacing else pattern
        forms = {}
        for form, text in (
                (_ad.FORM_PLAIN, pattern),
                (_ad.FORM_WHOLE_SUBJECT, rb"\A(?:" + ws_pattern + rb")\z")):
            forms[form] = self._compile_one(testee_id, pattern_id, form,
                                            text, trials, workdir)
        return _ad.CompiledPattern(forms)

    def _compile_one(self, testee_id, pattern_id, form, pattern, trials,
                     workdir):
        cfg = self.config(testee_id)
        drv = self.prepare_driver(workdir)
        # per-PATTERN, per-FORM scratch: testees/onig/adapter.py's own
        # note applies verbatim -- two different compiles of different
        # text must never share a directory.
        pdir = os.path.join(workdir, "p-" + pattern_id, form)
        os.makedirs(pdir, exist_ok=True)
        patfile = os.path.join(pdir, "pattern.rx")
        # RAW BYTES, end to end (inbox I-72's lesson): the pattern
        # travels as a FILE, never a subprocess argv element, so this
        # adapter is not exposed to the fsencode/latin-1 mojibake class
        # the pcrec adapter hit. The file write is BINARY,
        # unconditionally -- see testees/rust/CLAUDE.md's I-72 section
        # for the DIFFERENT, structural limitation this project's shared
        # high-byte witness pattern exposes here (the pattern must still
        # be valid UTF-8 for THIS engine specifically, checked by the
        # DRIVER, not this adapter -- this adapter never inspects the
        # bytes it writes).
        with open(patfile, "wb") as f:
            f.write(bytes(pattern))
        size_limit = cfg.get("size_limit", DEFAULT_SIZE_LIMIT)
        dfa_size_limit = cfg.get("dfa_size_limit", DEFAULT_DFA_SIZE_LIMIT)
        argv = [drv, "--pattern", patfile, "--form", form,
               "--compile-trials", str(trials),
               "--size-limit", str(size_limit),
               "--dfa-size-limit", str(dfa_size_limit)]
        out = run_driver(argv, timeout=max(60, 30 * trials), cwd=workdir)

        if out.timed_out:
            return _ad.CompileResult("timed-out", diagnostic=out.diagnostic())
        if out.returncode == 3:
            diag = out.diagnostic() or "regex build failed"
            rclass, name = classify_refusal(diag)
            return _ad.CompileResult(
                "did-not-compile", diagnostic=diag,
                engine_metadata=({"refusal_class": rclass} if rclass
                                 else {}))
        if out.returncode != 0:
            return _ad.CompileResult(
                "crashed",
                diagnostic=out.diagnostic()
                          or "driver exit %s" % out.returncode)

        meta = {}
        for name in METADATA_DECL:
            if name in out.info and name != "refusal_class":
                meta[name] = int(out.info[name])
        handle = {"driver": drv, "pattern_file": patfile, "form": form,
                 "size_limit": size_limit,
                 "dfa_size_limit": dfa_size_limit,
                 "giveup_codes": set()}  # never fires -- see driver.rs's header
        return _ad.CompileResult(
            "compiled", phase_seconds=out.phase_seconds,
            engine_metadata=meta, handle=handle)

    # -------------------------------------------------------------- measure

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        from pcrecbench.subbench import REGIME_MODE
        argv = [handle["driver"], "--pattern", handle["pattern_file"],
               "--form", handle["form"], "--mode", REGIME_MODE[regime],
               "--iters", str(iters),
               "--size-limit", str(handle["size_limit"]),
               "--dfa-size-limit", str(handle["dfa_size_limit"])]
        if regime == "throughput":
            argv.append("--find-all")
        return per_trial(argv, subjects, trials, timeout=timeout,
                         pin=handle.get("pin"),
                         subject_timeout=handle.get("subject_timeout"))
