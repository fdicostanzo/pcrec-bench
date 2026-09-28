#!/usr/bin/env python3
"""docs/dev/measurements/probe_tre_bracket_escape_declaration_verify.py

[B105] THE DECLARATION VERIFY: re-derives
`2026-09-27-tre-bracket-escape-census.txt`'s own 30-pattern population
(every `bench/*/patterns/*.rx` file containing a bracket expression with
a backslash inside it, `find_bracket_spans` reused UNCHANGED from that
census's own script -- never a second implementation of the bracket
scan) against the REAL `tre-default` adapter's `compile()` call, now
carrying [B105]'s pre-compile bracket-escape declaration
(`testees/tre/adapter.py`'s `_bracket_backslash_content`).

For every one of the 30 patterns: the PLAIN form's `compile_outcome`
today (this run), and where the original census cross-referenced
`bench/capability@0.1`'s 20 patterns against the committed cf0962e3
report (its three buckets -- 11 `unsupported_by_pattern` for an
unrelated declared token, 3 already `did-not-compile` on the
descending-range/POSIX-range bug, 6 `compiled and answered wrong`), the
BEFORE bucket is carried over from that file (read-only citation, not
re-measured) and compared against the AFTER outcome this script
actually gets from the real adapter, so the reclassification is stated
by name rather than merely asserted.

Compile-only: `adapter.prepare()` + `adapter.compile()` on the PLAIN
form of each pattern (needs libtre-dev; may build the tre driver once).
No store, no timing beyond what `compile()` itself takes (this probe
prints no numbers). Never runs against bounded/email/loglines/utf8's
subjects -- those four sets are UNMEASURED for tre-default (the original
census's own finding), so there is no "wrong answer" to re-derive there
either way; this script confirms only that their bracket-with-backslash
patterns are now declared unsupported the same way capability@0.1's are.

Usage: python3 docs/dev/measurements/probe_tre_bracket_escape_declaration_verify.py
  (run from the repo root; builds testees/tre's driver once if needed)
"""
import glob
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, ROOT)

from probe_tre_bracket_escape_census import find_bracket_spans  # noqa: E402
from pcrecbench import adapters as _ad                          # noqa: E402

# The original census's own cross-reference against the committed
# cf0962e3 report (2026-09-27-tre-bracket-escape-census.txt, verbatim
# citation, never re-measured here): bench/capability@0.1's 20 hit
# patterns split into three BEFORE buckets.
BEFORE_UNSUPPORTED_BY_PATTERN = frozenset({
    "bracket-array-define", "codegrammar-xflag", "float-literal-bound",
    "pwd-strength-chain", "quoted-delim-match", "utf8-lead-no-cont",
    "wild-codegrammar-json-stringcontent-escape",
    "wild-logparse-quotedstring-grok", "wild-logparse-quotedstring-noatomic",
    "wild-logparse-syslogbase-expanded", "wild-logparse-winpath-grok",
})
BEFORE_DID_NOT_COMPILE = frozenset({
    "wild-datetime-datefinder-alternation",
    "wild-secrets-username-password-pair",
    "wild-waf-crs-942500-comment-obfuscation",
})
BEFORE_COMPILED_WRONG = frozenset({
    "high-byte-run", "tag-pair-match", "wild-waf-crs-942360-concat-sqli",
    "mojibake-curly-quote",
})
BEFORE_COMPILED_COINCIDENTALLY_SAFE = frozenset({
    "codegrammar-flat", "winpath-near-miss",
})


def before_bucket(pattern_id):
    if pattern_id in BEFORE_UNSUPPORTED_BY_PATTERN:
        return "unsupported_by_pattern (unrelated declared token)"
    if pattern_id in BEFORE_DID_NOT_COMPILE:
        return "did-not-compile (descending POSIX range, (d)4)"
    if pattern_id in BEFORE_COMPILED_WRONG:
        return "compiled, answered WRONG"
    if pattern_id in BEFORE_COMPILED_COINCIDENTALLY_SAFE:
        return "compiled, coincidentally correct"
    return "not measured (no store record for tre-default on this set)"


def collect_hits():
    rows = []
    for rxfile in sorted(glob.glob(os.path.join(ROOT, "bench", "*", "patterns", "*.rx"))):
        subbench = os.path.basename(os.path.dirname(os.path.dirname(rxfile)))
        pattern_id = os.path.splitext(os.path.basename(rxfile))[0]
        with open(rxfile, "rb") as f:
            raw = f.read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("latin-1")
        hit = False
        for (_s, _e, content) in find_bracket_spans(text):
            if "\\" in content:
                hit = True
                break
        if hit:
            rows.append((subbench, pattern_id, raw))
    return rows


def main():
    rows = collect_hits()
    distinct = sorted(set((sb, pid) for (sb, pid, _raw) in rows))
    print("subbench\tpattern_id\tbefore\tafter_compile_outcome\tafter_declaration_ref_cites_b105\tnewly_refused")

    import tempfile
    tmp = tempfile.mkdtemp(prefix="pcrecbench-b105verify-")
    adapter = _ad.discover()["tre"]
    adapter.prepare("tre-default", tmp)

    newly_refused = []
    reclassified_did_not_compile = []
    all_refused = True
    for (sb, pid, raw) in rows:
        cp = adapter.compile("tre-default", pid, raw, {}, 1, tmp)
        cr = cp.get(_ad.FORM_PLAIN)
        outcome = cr.outcome if cr else "<no plain form>"
        cites_b105 = bool(cr and cr.declaration_ref and "(d)4" in cr.declaration_ref)
        before = before_bucket(pid)
        is_newly_refused = (before == "compiled, coincidentally correct"
                            and outcome == "unsupported-by-declaration")
        if is_newly_refused:
            newly_refused.append((sb, pid, before))
        if (before == "did-not-compile (descending POSIX range, (d)4)"
                and outcome == "unsupported-by-declaration"):
            reclassified_did_not_compile.append((sb, pid))
        if outcome != "unsupported-by-declaration":
            all_refused = False
        print("%s\t%s\t%s\t%s\t%s\t%s"
              % (sb, pid, before, outcome, cites_b105, is_newly_refused))

    print("\n# total: %d distinct (subbench, pattern) pair(s) re-derived"
          % len(distinct), file=sys.stderr)
    print("# every pattern's compile_outcome under tre-default: %s"
          % ("ALL unsupported-by-declaration"
             if all_refused else "SOME NOT unsupported-by-declaration"),
          file=sys.stderr)
    print("# previously WRONG (compiled, answered wrong) rows now refused: "
          "checked against BEFORE_COMPILED_WRONG (%d patterns)"
          % len(BEFORE_COMPILED_WRONG), file=sys.stderr)
    print("# previously did-not-compile rows now reclassified to "
          "unsupported-by-declaration: %s"
          % (reclassified_did_not_compile or "none"), file=sys.stderr)
    print("# previously CORRECT rows that NEWLY refuse "
          "('coincidentally safe' doubled-backslash idiom): %s"
          % (newly_refused or "none"), file=sys.stderr)


if __name__ == "__main__":
    main()
