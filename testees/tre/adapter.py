r"""testees/tre/adapter.py -- the TRE adapter (harness contract 3).

Provides `tre-default` ONLY -- TRE has no space/speed dial at all (its
three bounds, `TRE_MAX_RE`/`TRE_MAX_STRING`/`TRE_MAX_STACK`, are fixed
compile-time constants with no `tre_set_*`-shaped configuration function
anywhere in `tre.h`/`regcomp.c`; docs/dev/research/2026-09-12-b42-engine-
landscape.md (5), capability_set_v1.md 8) -- so there is no second config
to propose the way `pcre2-jit`/`pcre2-dfa` or `pcrec-vm` exist beside their
own siblings.

COMPILE COST (requirements 3): one phase, `compile` -- `tre_regncompb`,
timed in-driver. TRE has no separate JIT/DFA-construction step (the same
execution-model class as pcre2-interp/onig-default).

TWO FORMS, PER Adapter.compile()'s CONTRACT: TRE has no runtime
end-anchored mode, so the `match` regime is answered on a SECOND artifact,
`^(?:<pattern>)$` -- NOT `pcrecbench.record.whole_subject_text()`'s
`(?:<pattern>)\z`, because TRE has no `\z` token at all (confirmed absent
from its escape switch; a literal `\z` in a TRE pattern compiles as
literal "z"). See testees/tre/driver.c's header and testees/tre/CLAUDE.md
for the full derivation of why `^(?:...)$ ` gives the same anchoring
contract `\z` gives pcrec's/onig's own wrap.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench import adapters as _ad          # noqa: E402
from pcrecbench.driverrun import build_driver, run_driver, per_trial  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

# record_schema.md 7 rule 1: DECLARE BEFORE USE. The driver's own
# `[measured]`-equivalent header comment is testees/tre/driver.c's own
# docstring; `capturecount` and `has_backrefs` are both structural,
# compile-time facts read straight off the compiled `regex_t`.
METADATA_DECL = {
    "capturecount": {
        "type": "integer", "scope": "pattern",
        "source": "regex_t.re_nsub, after tre_regncompb",
        "description": "lexical capturing groups in the pattern (excludes "
                       "the whole-match group 0 -- the same convention "
                       "testees/pcre2/'s capturecount and testees/onig/'s "
                       "capturecount both hold)",
    },
    "has_backrefs": {
        "type": "integer", "scope": "pattern",
        "source": "tre_have_backrefs(preg), after tre_regncompb",
        "description": "1 if the compiled pattern contains a backreference "
                       "(TRE falls back to a backtracking matcher for these "
                       "-- testees/tre/CLAUDE.md's gave-up section), else 0",
    },
    "refusal_class": {
        "type": "string", "scope": "pattern",
        "source": "the REG_* code tre_regncompb returned on a "
                  "did-not-compile outcome, bucketed by this adapter "
                  "(capability_set_v1.md 5.5: TRE's reg_errcode_t is "
                  "exactly the 'closed, structural signal' that section "
                  "requires before a config may declare refusal_class)",
        "description": "'size-limit' for REG_ESPACE (code 12) WHEN this "
                       "pattern's own byte length exceeds TRE_MAX_RE "
                       "(65536) -- the driver's own `pattern_bytes` info "
                       "line is what lets this adapter tell TRE's OVERLOADED "
                       "REG_ESPACE (compile-time length cap OR a genuine "
                       "allocation failure, indistinguishable by code alone "
                       "-- testees/tre/driver.c's header) apart from a real "
                       "out-of-memory; 'syntax' for every other refusal "
                       "code; ABSENT (never a guessed third value) for "
                       "REG_ESPACE under the length cap or for a code this "
                       "adapter's diagnostic parser cannot read",
    },
}

# `_REFUSAL_SYNTAX_CODES` -- every reg_errcode_t value that is unambiguously
# a SYNTAX refusal (tre/tre.h's own enum, verbatim; [B7]/L6b, this lane,
# 2026-09-17, cross-checked against a live tre_regerror() call for each).
# REG_ESPACE (12) is handled separately below because TRE overloads it
# (testees/tre/driver.c's header; docs/dev/research/2026-09-12-b42-engine-
# landscape.md (5): "if (n > TRE_MAX_RE) return REG_ESPACE;" in regcomp.c,
# same code as a genuine allocation failure). REG_NOMATCH (1) never reaches
# this path (it is not a compile-time code).
_REFUSAL_SYNTAX_CODES = frozenset({2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14})
# REG_BADPAT=2 REG_ECOLLATE=3 REG_ECTYPE=4 REG_EESCAPE=5 REG_ESUBREG=6
# REG_EBRACK=7 REG_EPAREN=8 REG_EBRACE=9 REG_BADBR=10 REG_BADRPT=13
# REG_BADMAX=14
_REG_ESPACE = 12
_TRE_MAX_RE = 65536  # lib/tre-internal.h, laurikari/tre master -- FIXED,
                     # no public header defines it (it is a PRIVATE bound);
                     # cited from source, docs/dev/research/2026-09-12-b42-
                     # engine-landscape.md (5).


def _refusal_class(code, pattern_bytes):
    """The `refusal_class` pair for a did-not-compile row. `None` (the
    caller must not fabricate a value) when the code is not one of TRE's
    own closed compile-time set, or when it is the ambiguous REG_ESPACE
    case below TRE_MAX_RE (a genuine allocation failure looks identical by
    code alone -- testees/tre/driver.c's header, testees/onig/adapter.py's
    own 'an honest omission is not a wrong classification' rule)."""
    if code is None:
        return None
    if code == _REG_ESPACE:
        return "size-limit" if pattern_bytes is not None and \
            pattern_bytes > _TRE_MAX_RE else None
    return "syntax" if code in _REFUSAL_SYNTAX_CODES else None


def _parse_code(diagnostic):
    """Pulls the integer code out of this driver's own
    `tre_regncompb failed (code %d): ...` diagnostic -- never a second
    parse of TRE's message text, the same convention
    testees/onig/adapter.py's `_refusal_class` helper uses."""
    if not diagnostic:
        return None
    marker = "(code "
    i = diagnostic.find(marker)
    if i < 0:
        return None
    j = diagnostic.find(")", i)
    if j < 0:
        return None
    try:
        return int(diagnostic[i + len(marker):j])
    except ValueError:
        return None


class Adapter(_ad.Adapter):
    name = "tre"

    # ------------------------------------------------------------- describe

    def probe_version(self, workdir):
        """PROBED, never typed: `tre_version()` off the loaded library --
        `"TRE 0.9.0 (BSD)"`. NOTE (measured live, this lane): the version
        NUMBER is token INDEX 1, not 0 (unlike pcre2's/onig's own
        `raw.split()[0]` convention) -- `tre_version()`'s first token is
        the literal word "TRE", not a number."""
        drv = self.prepare_driver(workdir)
        out = run_driver([drv, "--pattern", os.path.join(HERE, "_probe.rx")],
                         timeout=60, cwd=workdir)
        for name, value in out.info.items():
            if name == "version":
                return value
        raise _ad.AdapterError("the tre driver reported no version")

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        raw = self.probe_version(workdir or os.getcwd())
        parts = raw.split()
        version = parts[1] if len(parts) > 1 else raw
        return {
            "engine_name": "tre",
            "engine_version": version,
            "engine_commit": None,
            "execution_model": "interpretive",
            # capability_set_v1.md 7.1 (S9): TRE gets its own
            # `automaton_class` column -- a TNFA (Thompson-construction,
            # linear-time) for BACKREFERENCE-FREE patterns, but a
            # BACKTRACKING fallback once a backreference is present
            # (`has_backrefs`, this file's own METADATA_DECL; testees/tre/
            # CLAUDE.md's gave-up section). No SINGLE token in
            # `record_schema.md`'s enum captures a pattern-dependent
            # automaton switch, so this is stated in PROSE here rather
            # than invented as a new enum value -- the same restraint
            # testees/pcre2/adapter.py exercises for `pcre2-dfa`'s own
            # semantic divergence.
            # `automaton_class` is a CLOSED enum (record_schema.md 4.3:
            # dfa-only/nfa-simulation/backtracking/hybrid/simd-
            # multipattern) -- caught by this lane's own `quick` smoke
            # test when an earlier draft here carried a free-text prose
            # value instead (SCHEMA rejection, "is not one of [...]").
            # `hybrid` is the closest single token: TRE's actual
            # automaton is PATTERN-DEPENDENT (a linear-time TNFA for
            # backreference-free patterns, a backtracking fallback
            # bounded by TRE_MAX_STACK once a backreference is present --
            # `has_backrefs`, this file's own METADATA_DECL), which no
            # single one of the other four tokens describes honestly.
            # testees/tre/CLAUDE.md's own "automaton_class" section
            # carries the full explanation this one-word field cannot.
            "automaton_class": "hybrid",
            "openness": "open-source",
            "license_id": "BSD-2-Clause",
            # capability_set_v1.md 5.6 / N2 2.2-2.3: TRE targets POSIX
            # leftmost-longest submatch semantics by specification --
            # DISTINCT from the perl-leftmost-first population the rest of
            # this roster (pcre2/pcrec/onig) shares. Confirmed live, this
            # lane: `a|ab` against "ab" -- the LONGEST alternative wins
            # under tre-default, not the FIRST one tried (see the witness
            # census). Schema token `posix-leftmost-longest`
            # (record_schema.md 5) is exactly this.
            "conventions": ["posix-leftmost-longest"],
            "captures": cfg.get("captures", "on"),
            "engine_mode": cfg["engine_mode"],
            "simd": "n-a",
            "build_flags": "distribution libtre.so.5 (%s), direct-linked "
                           "(-ltre); driver built with $CC -O2 -std=gnu11; "
                           "REG_EXTENDED, no REG_NEWLINE (testees/tre/"
                           "CLAUDE.md states the choice and its two stated "
                           "consequences)" % raw,
            "runtime_options": [],
            "compile_cost_definition": (
                "interpreter (requirements 3): the one call, timed "
                "in-driver -- tre_regncompb. No separate JIT/DFA-"
                "construction step exists (the same execution-model class "
                "as pcre2-interp/onig-default). Median of N with spread is "
                "the REPORTER's reduction."),
            "compile_phases": ["compile"],
            "warmup_trials": 0,
            "engine_metadata_declaration": dict(METADATA_DECL),
        }

    def binary_identity(self, testee_id, workdir=None):
        """`testee.binary` for a scratch-tier record (schema v1.2, X29):
        the distribution `libtre.so.5` this driver links against, resolved
        to the file the dynamic loader actually maps -- same technique as
        testees/pcre2/adapter.py's and testees/onig/adapter.py's own
        `binary_identity` (load it here via ctypes, then read
        /proc/self/maps for the mapped path)."""
        import ctypes
        soname = "libtre.so.5"
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
                    if os.path.basename(cand).startswith("libtre.so"):
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
                            os.path.join(workdir, "tre_driver"),
                            extra=["-ltre"])

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
                workdir, requires_free_spacing=False):
        r"""TWO artifacts per pattern: `plain` and `whole-subject` -- same
        reasoning as testees/onig/adapter.py's own `compile()` docstring:
        TRE has no end-anchored runtime option, so "does the WHOLE subject
        match" needs its own artifact -- `^(?:<pattern>)$`, NOT the shared
        `pcrecbench.record.whole_subject_text()` (TRE has no `\z`).

        `requires_free_spacing` ([B70]) is UNUSED and unreachable in
        practice: `tre-default` never declares the `free-spacing`
        capability (`REQUIRES_VOCAB`), so the pre-compile capability
        policy (`harness.run_cell`) already turns any free-spacing
        pattern into an `unsupported-by-declaration` row before this
        method is ever called -- confirmed on the [B69] census's own two
        CASE-1 patterns, which `tre-default` never attempts at all."""
        del requires_free_spacing
        forms = {}
        for form, text in ((_ad.FORM_PLAIN, pattern),
                           (_ad.FORM_WHOLE_SUBJECT, pattern)):
            forms[form] = self._compile_one(testee_id, pattern_id, form,
                                            text, trials, workdir)
        return _ad.CompiledPattern(forms)

    def _compile_one(self, testee_id, pattern_id, form, pattern, trials,
                     workdir):
        drv = self.prepare_driver(workdir)
        # per-PATTERN, per-FORM scratch: see Adapter.compile's docstring
        # (the last-pattern's-artifact-under-the-first-pattern's-handle
        # bug) and testees/onig/adapter.py's own note for why the FORM
        # must not share a directory either.
        pdir = os.path.join(workdir, "p-" + pattern_id, form)
        os.makedirs(pdir, exist_ok=True)
        patfile = os.path.join(pdir, "pattern.rx")
        with open(patfile, "wb") as f:
            f.write(pattern)
        # The `^(?:...)$` wrap happens INSIDE the driver (testees/tre/
        # driver.c's own `--form whole-subject` branch), not here -- the
        # file on disk is always the bare pattern text, exactly like
        # testees/onig/adapter.py hands its driver the bare pattern and
        # lets IT append `(?:...)\z`. This keeps the wrap logic in ONE
        # place (the C driver) rather than duplicated in python and C.
        argv = [drv, "--pattern", patfile, "--form", form,
                "--compile-trials", str(trials)]
        out = run_driver(argv, timeout=max(60, 30 * trials), cwd=workdir)

        if out.timed_out:
            return _ad.CompileResult("timed-out", diagnostic=out.diagnostic())
        if out.returncode == 3:
            diag = out.diagnostic() or "tre_regncompb failed"
            code = _parse_code(diag)
            pattern_bytes = None
            if "pattern_bytes" in out.info:
                try:
                    pattern_bytes = int(out.info["pattern_bytes"])
                except ValueError:
                    pattern_bytes = None
            rc = _refusal_class(code, pattern_bytes)
            return _ad.CompileResult(
                "did-not-compile", diagnostic=diag,
                engine_metadata=({"refusal_class": rc} if rc else None))
        if out.returncode != 0:
            return _ad.CompileResult(
                "crashed",
                diagnostic=out.diagnostic() or "driver exit %s" % out.returncode)

        meta = {}
        for name in ("capturecount", "has_backrefs"):
            if name in out.info:
                meta[name] = int(out.info[name])
        # GAVE-UP: `harness.classify_giveup` treats a driver `giveup:<code>`
        # answer as `gave-up` only when `code in giveup_codes` -- an EMPTY
        # set would silently turn every one of this driver's `giveup:`
        # rows into `crashed` instead, which is the OPPOSITE of the
        # driver's own contract (testees/tre/driver.c's header: any
        # exec-time return that is neither REG_OK nor REG_NOMATCH IS, by
        # POSIX's own contract for these functions, a gave-up). So the
        # declared set is TRE's full non-OK/non-NOMATCH reg_errcode_t
        # range (2..14 -- REG_BADPAT..REG_BADMAX, tre/tre.h's own enum)
        # rather than a measured subset the way testees/pcre2/adapter.py's
        # GAVE_UP_CODES and testees/onig/adapter.py's GAVE_UP_CODES are:
        # this driver's OWN generic-classification design (its header's
        # "no fixed code table is hardcoded here") is what decides which
        # codes can even reach a subject row as `giveup:` in the first
        # place, so the adapter's job is only to agree, not to narrow
        # further. UNWITNESSED on this lane's own corpus (testees/tre/
        # CLAUDE.md's gave-up section states this plainly) -- provisioned,
        # not confirmed live the way onig's retry-limit code is.
        handle = {"driver": drv, "pattern_file": patfile, "form": form,
                  "giveup_codes": set(range(2, 15))}
        return _ad.CompileResult(
            "compiled", phase_seconds=out.phase_seconds,
            engine_metadata=meta, handle=handle)

    # -------------------------------------------------------------- measure

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        from pcrecbench.subbench import REGIME_MODE
        argv = [handle["driver"], "--pattern", handle["pattern_file"],
                "--form", handle["form"], "--mode", REGIME_MODE[regime],
                "--iters", str(iters)]
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
