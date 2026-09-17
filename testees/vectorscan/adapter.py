r"""testees/vectorscan/adapter.py -- the Vectorscan adapter (harness
contract 3), BOOLEAN GRAIN (capability_set_v1.md 5.6 option (B), Frank's
Q3 ruling, 2026-09-16).

Provides `vectorscan-block-nosom` only (block mode, no HS_FLAG_SOM_
LEFTMOST). `vectorscan-block-som` is documented in testees/vectorscan/
CLAUDE.md as a LATER config -- this lane does not wire it (capability_
set_v1.md 8's own roster row: SOM is "an unconditional space cost, not a
dial", gated on the span-grain scoring machinery boolean grain makes
unnecessary).

COMPILE COST (requirements 3, per execution-model class): one phase,
`compile` -- `hs_compile()`, timed in-driver. `execution_model =
"eager-jit"` (docs/dev/research/2026-09-12-b42-engine-landscape.md's own
recommendation: "the closest existing token: one explicit, timeable call
that produces a ready-to-run artifact" -- Vectorscan's own compiled
DATABASE, not machine code via a real compiler+linker, but the closest
class this schema has short of pcrec's own AOT).

BOOLEAN GRAIN, STATED HERE TOO (see testees/vectorscan/CLAUDE.md and
driver.c's header for the full derivation): this testee NEVER reports a
match span. `harness.outcome_for` has no boolean-grain accommodation
today -- its span comparison (`row.start != expectation.start or row.end
!= expectation.end`) fires on EVERY row where `row.matched` is true,
because this driver always reports `start=end=None` while a real
expectation row carries real oracle-derived integers. The practical
consequence, MEASURED against this adapter's own driver output: every
subject this testee genuinely MATCHES scores `wrong-span-or-captures`,
never `matched-as-expected`; every subject it correctly does NOT match
scores `matched-as-expected` normally (the span check is only reached
when `row.matched` is true). This is a real, documented gap in the
CURRENT harness, not a defect in this adapter -- exactly the same shape
`testees/pcre2/CLAUDE.md`'s own "pcre2-dfa" divergence table and its
"family 11" section describe for a testee whose correct, documented
answer the harness's own comparison marks wrong. Closing it needs a
harness-side `grain` declaration (the same shape `convention` already
has, R5 B1/CB1) that skips the span/capture comparison for a testee that
declares it never produces one -- out of scope for an adapter lane to
build unilaterally; flagged to the manager as a finding, not routed
around quietly here.

ESCALATION, MEASURED (see testees/vectorscan/CLAUDE.md's own section for
the full reproduction): this is not merely a scoring nuance. A record
whose `wrong-span-or-captures` branch builds `observed.span =
[None, None]` FAILS schema validation outright (`span`'s items must be
integers; the schema allows the WHOLE field `null`, never a two-element
array of nulls) -- `pcrecbench quick`/`run` REFUSE to write ANY record
for a cell where this testee matches at least one subject, on any set,
at any tier, today. A cell whose every subject is a genuine nomatch
writes fine.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench import adapters as _ad          # noqa: E402
from pcrecbench.driverrun import build_driver, run_driver, per_trial  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

# record_schema.md 7 rule 1: DECLARE BEFORE USE. Every name is the
# driver's own `info` line (driver.c's header + its hs_expression_info/
# hs_database_size block).
METADATA_DECL = {
    "min_width": {
        "type": "integer", "scope": "pattern",
        "source": "hs_expression_info(...)->min_width",
        "description": "minimum length in bytes of a match for the pattern "
                       "(Hyperscan's own capability probe unique to this "
                       "roster's engine, docs/dev/research/2026-09-12-b42-"
                       "engine-landscape.md's finding (6))",
    },
    "max_width": {
        "type": "integer", "scope": "pattern",
        "source": "hs_expression_info(...)->max_width",
        "description": "maximum length in bytes of a match for the "
                       "pattern; UINT_MAX (4294967295) when unbounded",
    },
    "unordered_matches": {
        "type": "integer", "scope": "pattern",
        "source": "hs_expression_info(...)->unordered_matches",
        "description": "1 iff this expression can produce matches not "
                       "returned in scan order (e.g. from assertions); "
                       "0/1 boolean stored as an integer",
    },
    "matches_at_eod": {
        "type": "integer", "scope": "pattern",
        "source": "hs_expression_info(...)->matches_at_eod",
        "description": "1 iff this expression can produce matches at "
                       "end-of-data",
    },
    "matches_only_at_eod": {
        "type": "integer", "scope": "pattern",
        "source": "hs_expression_info(...)->matches_only_at_eod",
        "description": "1 iff this expression can ONLY produce matches at "
                       "end-of-data -- true on every whole-subject "
                       "(`^(?:...)\\z`) artifact, structurally",
    },
    "compiled_size_bytes": {
        "type": "integer", "scope": "pattern",
        "source": "hs_database_size(db, &size)",
        "description": "size of the compiled Hyperscan database in bytes "
                       "-- requirements 4.2's 'program size' for this "
                       "engine, the same convention as pcre2's "
                       "compiled_size_bytes and onig's absence of one "
                       "(Oniguruma exposes no such accessor; Vectorscan "
                       "does)",
    },
}

# GAVE-UP CODES: the EMPTY SET. See driver.c's header, "GAVE-UP CODES:
# NONE" -- Vectorscan/Hyperscan's bounded automaton has no documented
# match-time resource-limit refusal to bucket here. `classify_giveup`
# reads this and therefore NEVER returns True for this testee: any
# negative hs_scan() return this driver did not itself cause (by its own
# callback requesting a stop) is `crashed`, correctly, because there is
# structurally nothing else it could be.
GAVE_UP_CODES = frozenset()


class Adapter(_ad.Adapter):
    name = "vectorscan"

    # ------------------------------------------------------------- describe

    def probe_version(self, workdir):
        """PROBED, never typed: `hs_version()` off the linked library."""
        drv = self.prepare_driver(workdir)
        out = run_driver([drv, "--pattern", os.path.join(HERE, "_probe.rx")],
                         timeout=60, cwd=workdir)
        for name, value in out.info.items():
            if name == "version":
                return value
        raise _ad.AdapterError("the vectorscan driver reported no version")

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        raw = self.probe_version(workdir or os.getcwd())
        version = raw.split()[0]
        return {
            "engine_name": "vectorscan",
            "engine_version": version,
            "engine_commit": None,
            "execution_model": "eager-jit",
            "automaton_class": "simd-multipattern",
            "openness": "open-source",
            "license_id": "BSD-3-Clause",
            # capability_set_v1.md 5.6: Vectorscan/Hyperscan is "explicitly
            # NOT leftmost-first-comparable at all" -- the `all-ends`
            # token this project's own conventions vocabulary carries for
            # exactly this engine. This is DECLARATIVE, not a claim this
            # driver exercises today: the boolean-grain config never asks
            # "which end" or "how many", only "did it match" -- see this
            # module's own docstring and testees/vectorscan/CLAUDE.md.
            "conventions": ["all-ends"],
            "captures": "off",   # Hyperscan has NO capturing groups at all
            "engine_mode": cfg["engine_mode"],
            "simd": "on",        # Vectorscan/Hyperscan's whole raison d'etre
            "build_flags": "distribution libhs.so.5 (%s), direct-linked "
                           "(-lhs, pkg-config libhs); driver built with "
                           "$CC -O2 -std=gnu11; HS_FLAG_UCP always set, "
                           "HS_FLAG_UTF8/HS_FLAG_SOM_LEFTMOST never "
                           "(testees/vectorscan/CLAUDE.md states the "
                           "choice and its consequences)" % raw,
            "runtime_options": [],
            "compile_cost_definition": (
                "eager, monolithic compile (requirements 3; docs/dev/"
                "research/2026-09-12-b42-engine-landscape.md's own "
                "characterization -- 'a huge compile-time investment for "
                "fast scanning', Vectorscan/Hyperscan's own well-known "
                "engineering tradeoff): the one call, timed in-driver -- "
                "hs_compile(). No separate JIT step is exposed to the "
                "caller (hs_compile's own database IS the ready-to-run "
                "artifact); `compile_phases = [\"compile\"]`, same shape "
                "as pcre2-interp/onig-default. Median of N with spread is "
                "the REPORTER's reduction."),
            "compile_phases": ["compile"],
            "warmup_trials": 0,
            "engine_metadata_declaration": dict(METADATA_DECL),
        }

    def binary_identity(self, testee_id, workdir=None):
        """`testee.binary` for a scratch-tier record (schema v1.2, X29):
        the distribution libhs.so.5 this driver links against, resolved
        the same way testees/pcre2/adapter.py and testees/onig/adapter.py
        resolve theirs (load it here via ctypes, then read
        /proc/self/maps for the mapped path)."""
        import ctypes
        soname = "libhs.so.5"
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
                    if os.path.basename(cand).startswith("libhs.so"):
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
                            os.path.join(workdir, "vectorscan_driver"),
                            extra=["-I/usr/include/hs", "-lhs"])

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
        r"""TWO artifacts per pattern: `plain` and `whole-subject`.

        Vectorscan block mode has NO runtime anchoring dial at all (unlike
        pcre2's PCRE2_ANCHORED|PCRE2_ENDANCHORED and unlike Oniguruma's
        onig_match-at-offset-0): `hs_scan()` scans the whole buffer for a
        match starting anywhere. So the `match` regime's artifact is NOT
        `pcrecbench.record.whole_subject_text()`'s bytes (`(?:pattern)\z`,
        which supplies only the END anchor) -- it needs a LEADING `^` too.
        `driver.c` builds that wider wrapper itself from the plain pattern
        text passed via `--form whole-subject`; this adapter passes the
        SAME plain pattern bytes for both forms and lets the driver do the
        wrapping, rather than pre-building `^(?:...)\z` here, so there is
        exactly one place (driver.c) that knows what the whole-subject
        artifact's real expression text is."""
        forms = {}
        for form in (_ad.FORM_PLAIN, _ad.FORM_WHOLE_SUBJECT):
            forms[form] = self._compile_one(testee_id, pattern_id, form,
                                            pattern, trials, workdir)
        return _ad.CompiledPattern(forms)

    def _compile_one(self, testee_id, pattern_id, form, pattern, trials,
                     workdir):
        drv = self.prepare_driver(workdir)
        # per-PATTERN, per-FORM scratch: see Adapter.compile's docstring
        # and testees/onig/adapter.py's own identical note.
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
            # NO `refusal_class`: capability_set_v1.md 5.5 declares that
            # pair "Never declared by Vectorscan or perl, whose refusal is
            # free text only" (hs_compile_error_t is `{message, expression
            # index}`, no closed reason enum -- docs/dev/research/2026-09-
            # 12-b42-engine-landscape.md's own table row). Declaring it
            # anyway would be exactly the dishonest invention
            # record_schema.md 7 rule 1 exists to prevent.
            diag = out.diagnostic() or "hs_compile failed"
            return _ad.CompileResult("did-not-compile", diagnostic=diag)
        if out.returncode != 0:
            return _ad.CompileResult(
                "crashed",
                diagnostic=out.diagnostic() or "driver exit %s" % out.returncode)

        meta = {}
        for name in METADATA_DECL:
            if name in out.info:
                meta[name] = int(out.info[name])
        handle = {"driver": drv, "pattern_file": patfile, "form": form,
                  "giveup_codes": set(GAVE_UP_CODES)}
        return _ad.CompileResult(
            "compiled", phase_seconds=out.phase_seconds,
            engine_metadata=meta, handle=handle,
            artifact_bytes=meta.get("compiled_size_bytes"))

    # -------------------------------------------------------------- measure

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        from pcrecbench.subbench import REGIME_MODE
        argv = [handle["driver"], "--pattern", handle["pattern_file"],
                "--form", handle["form"], "--mode", REGIME_MODE[regime],
                "--iters", str(iters)]
        if regime == "throughput":
            argv.append("--find-all")
        return per_trial(argv, subjects, trials, timeout=timeout,
                         pin=handle.get("pin"),
                         subject_timeout=handle.get("subject_timeout"))
