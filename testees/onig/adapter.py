r"""testees/onig/adapter.py -- the Oniguruma adapter (harness contract 3).

Provides `onig-default` only (execution model `interpretive`) --
`onig-lowretry` is documented in testees/onig/CLAUDE.md and the design
note's roster table (capability_set_v1.md 8) as a LATER config; this lane
does not wire it.

COMPILE COST (requirements 3, per execution-model class): one phase,
`compile` -- `onig_new`, timed in-driver. Oniguruma has no separate JIT
step, the same shape as `pcre2-interp`.

TWO FORMS, PER Adapter.compile()'s CONTRACT: Oniguruma has no runtime
end-anchor option (no PCRE2_ENDANCHORED equivalent), so the `match` regime
is answered on a SECOND artifact compiled from `(?:<pattern>)\z`
(`pcrecbench.record.whole_subject_text`, the SAME bytes pcrec's own
whole-subject artifact uses) -- see testees/onig/driver.c's header and
testees/onig/CLAUDE.md for the `onig_match`-at-offset-0 mechanism that
supplies the START anchor.
"""

import ctypes
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench import adapters as _ad          # noqa: E402
from pcrecbench import record as _rec           # noqa: E402
from pcrecbench.driverrun import build_driver, run_driver, per_trial  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

# record_schema.md 7 rule 1: DECLARE BEFORE USE. `onig_number_of_captures`
# and `onig_number_of_names` are the driver's own `[measured]` block
# (driver.c's header comment); both are structural, compile-time facts
# about what the pattern COULD deliver, exactly the same class of fact
# pcre2's `capturecount` is.
METADATA_DECL = {
    "capturecount": {
        "type": "integer", "scope": "pattern",
        "source": "onig_number_of_captures(reg)",
        "description": "lexical capturing groups in the pattern (unnamed "
                       "and named together; ONIG_SYN_CAPTURE_ONLY_NAMED_"
                       "GROUP under ONIG_SYNTAX_PERL_NG changes which "
                       "groups the ENGINE reports at match time when the "
                       "pattern mixes named and unnamed groups, never "
                       "this compile-time count -- testees/onig/CLAUDE.md",
    },
    "names": {
        "type": "integer", "scope": "pattern",
        "source": "onig_number_of_names(reg)",
        "description": "distinct named capture groups in the pattern",
    },
    "refusal_class": {
        "type": "string", "scope": "pattern",
        "source": "the ONIGERR_* code onig_new returned on a did-not-compile "
                  "outcome, bucketed by this adapter (capability_set_v1.md "
                  "5.5: 'declared ONLY by a config whose engine gives a "
                  "closed, structural signal' -- Oniguruma's ONIGERR_* is "
                  "exactly that)",
        "description": "'size-limit' for ONIGERR_PARSE_DEPTH_LIMIT_OVER "
                       "(-16, a compile-time parse-nesting budget); 'syntax' "
                       "for every other refusal code this adapter can parse "
                       "out of the diagnostic; ABSENT (never a third value) "
                       "when the diagnostic carries no parseable code -- an "
                       "honest omission is not a wrong classification",
    },
}

_REFUSAL_SIZE_LIMIT_CODES = frozenset({-16})  # ONIGERR_PARSE_DEPTH_LIMIT_OVER


def _refusal_class(diagnostic):
    """The `refusal_class` pair for a did-not-compile row, from this
    adapter's own diagnostic text (`onig_new failed (code %d): ...`,
    driver.c's own spelling) -- never a second parse of Oniguruma's
    output, just this file's own printf. `None` when no code parses,
    which the caller must not turn into a fabricated `syntax` guess."""
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
        code = int(diagnostic[i + len(marker):j])
    except ValueError:
        return None
    return "size-limit" if code in _REFUSAL_SIZE_LIMIT_CODES else "syntax"

# The RESOURCE-LIMIT refusals: negative onig_search/onig_match returns
# where the engine declined to answer because a configured budget ran out,
# as opposed to answering wrongly or failing. Schema v1.1's per-subject
# `gave-up` outcome is for exactly these; every other negative code is
# `crashed`.
#
# [measured] 2026-09-17, this lane, by DIRECT SOURCE READ of this box's
# installed Oniguruma 6.9.10 (/usr/include/oniguruma.h, byte-identical to
# the upstream v6.9.10 tag; src/regexec.c cross-referenced at the same
# tag -- see testees/onig/CLAUDE.md for the full derivation and line
# numbers). NOT probed blind: every code below is where regexec.c's own
# `MATCH_AT_ERROR_RETURN`/direct `return` sites raise it.
GAVE_UP_CODES = {
    -15: "ONIGERR_MATCH_STACK_LIMIT_OVER",
    -17: "ONIGERR_RETRY_LIMIT_IN_MATCH_OVER",     # DEFAULT budget 10,000,000
    -18: "ONIGERR_RETRY_LIMIT_IN_SEARCH_OVER",
    -19: "ONIGERR_SUBEXP_CALL_LIMIT_IN_SEARCH_OVER",
}
# Deliberately NOT in the set, each for a stated reason (mirroring
# testees/pcre2/adapter.py's own convention):
#   -5  ONIGERR_MEMORY -- an allocation failure, not a configured budget;
#       the box ran out, the engine did not decline. `crashed`.
#   -16 ONIGERR_PARSE_DEPTH_LIMIT_OVER -- raised in src/regparse.c, i.e. at
#       COMPILE time (a parse-nesting-depth budget, DEFAULT 4096) -- lands
#       on the ordinary `did-not-compile` path via onig_new's own return
#       code, never reaches this driver's match loop, and is therefore not
#       a per-subject code at all.
#   -1  ONIG_MISMATCH -- an answer, not a refusal.


class Adapter(_ad.Adapter):
    name = "onig"

    # ------------------------------------------------------------- describe

    def probe_version(self, workdir):
        """PROBED, never typed: `onig_version()` off the loaded library."""
        drv = self.prepare_driver(workdir)
        out = run_driver([drv, "--pattern", os.path.join(HERE, "_probe.rx")],
                         timeout=60, cwd=workdir)
        for name, value in out.info.items():
            if name == "version":
                return value
        raise _ad.AdapterError("the onig driver reported no version")

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        version = self.probe_version(workdir or os.getcwd())
        return {
            "engine_name": "oniguruma",
            "engine_version": version,
            "engine_commit": None,
            "execution_model": "interpretive",
            "automaton_class": "backtracking",
            "openness": "open-source",
            "license_id": "BSD-2-Clause",
            # capability_set_v1.md 5.6: a backtracking, first-alternative-
            # wins engine -- the SAME token pcre2/pcrec/perl/python use.
            # testees/onig/CLAUDE.md states the one real divergence this
            # lane found (ONIG_SYN_CAPTURE_ONLY_NAMED_GROUP's effect on
            # MIXED named/unnamed capture groups) in prose, not a second
            # token -- exactly the precedent testees/pcre2/CLAUDE.md's
            # own "pcre2-dfa" section sets for a real, stated divergence
            # that has no vocabulary token of its own.
            "conventions": ["perl-leftmost-first"],
            "captures": cfg.get("captures", "on"),
            "engine_mode": cfg["engine_mode"],
            "simd": "n-a",
            "build_flags": "distribution libonig.so.5 (%s), direct-linked "
                           "(-lonig); driver built with $CC -O2 -std=gnu11; "
                           "ONIG_SYNTAX_PERL_NG / ONIG_ENCODING_ASCII "
                           "(testees/onig/CLAUDE.md states the choice and "
                           "its consequences)" % version,
            "runtime_options": [],
            "compile_cost_definition": (
                "interpreter (requirements 3): the one call, timed "
                "in-driver -- onig_new. No separate JIT step exists "
                "(the same execution-model class as pcre2-interp). "
                "Median of N with spread is the REPORTER's reduction."),
            "compile_phases": ["compile"],
            "warmup_trials": 0,
            "engine_metadata_declaration": dict(METADATA_DECL),
        }

    def binary_identity(self, testee_id, workdir=None):
        """`testee.binary` for a scratch-tier record (schema v1.2, X29):
        the distribution libonig.so.5 this driver links against, resolved
        to the file the dynamic loader actually maps -- same technique as
        testees/pcre2/adapter.py's own `binary_identity` (load it here via
        ctypes, then read /proc/self/maps for the mapped path), because
        the driver itself never reports its own linked library's path."""
        soname = "libonig.so.5"
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
                    if os.path.basename(cand).startswith("libonig.so"):
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
                            os.path.join(workdir, "onig_driver"),
                            extra=["-lonig"])

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
        reasoning as testees/pcrec/adapter.py's own `compile()` docstring:
        Oniguruma has no end-anchored runtime option, so "does the WHOLE
        subject match" needs its own artifact, `(?:<pattern>)\z` (or
        `(?:<pattern>\n)\z` when `requires_free_spacing` -- [B70],
        `record.whole_subject_text`'s own docstring), timed and recorded
        separately (rule X27)."""
        forms = {}
        for form, text in ((_ad.FORM_PLAIN, pattern),
                           (_ad.FORM_WHOLE_SUBJECT,
                            _rec.whole_subject_text(pattern, requires_free_spacing))):
            forms[form] = self._compile_one(testee_id, pattern_id, form,
                                            text, trials, workdir)
        return _ad.CompiledPattern(forms)

    def _compile_one(self, testee_id, pattern_id, form, pattern, trials,
                     workdir):
        drv = self.prepare_driver(workdir)
        # per-PATTERN, per-FORM scratch: see Adapter.compile's docstring
        # (the last-pattern's-artifact-under-the-first-pattern's-handle bug)
        # and testees/pcrec/adapter.py's own note for why the FORM must not
        # share a directory either -- two different compiles of different
        # text.
        pdir = os.path.join(workdir, "p-" + pattern_id, form)
        os.makedirs(pdir, exist_ok=True)
        patfile = os.path.join(pdir, "pattern.rx")
        with open(patfile, "wb") as f:
            f.write(pattern)
        argv = [drv, "--pattern", patfile, "--form", form,
                "--compile-trials", str(trials)]
        out = run_driver(argv, timeout=max(60, 30 * trials), cwd=workdir)

        if out.timed_out:
            return _ad.CompileResult("timed-out", diagnostic=out.diagnostic())
        if out.returncode == 3:
            diag = out.diagnostic() or "onig_new failed"
            rc = _refusal_class(diag)
            return _ad.CompileResult(
                "did-not-compile", diagnostic=diag,
                engine_metadata=({"refusal_class": rc} if rc else None))
        if out.returncode != 0:
            return _ad.CompileResult(
                "crashed",
                diagnostic=out.diagnostic() or "driver exit %s" % out.returncode)

        meta = {}
        for name in METADATA_DECL:
            if name in out.info:
                meta[name] = int(out.info[name])
        # The MEASURED set of Oniguruma resource-limit refusals travels
        # with the handle (this file's own GAVE_UP_CODES comment), so
        # `harness.classify_giveup` needs no engine knowledge -- the same
        # contract testees/pcre2/adapter.py's `giveup_codes` uses.
        handle = {"driver": drv, "pattern_file": patfile, "form": form,
                  "giveup_codes": set(GAVE_UP_CODES)}
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
