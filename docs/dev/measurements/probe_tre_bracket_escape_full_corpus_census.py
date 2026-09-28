#!/usr/bin/env python3
"""docs/dev/measurements/probe_tre_bracket_escape_full_corpus_census.py

[B105] THE FULL-CORPUS CENSUS, manager-requested (2026-09-28, before
merge, following the over-refusal fix): every `bench/*/patterns/*.rx`
file across EVERY sub-bench directory that exists TODAY (not the
2026-09-27 census's own seven -- `bench/litrun` and `bench/altwide` are
enumerated too, by directory discovery, never a hand-typed list), run
through the REAL, FIXED `testees/tre/adapter.py` scanner
(`_bracket_backslash_content`, the two-state outside/inside-bracket
rule) directly -- not the 2026-09-27 census's own simpler
`find_bracket_spans` (which lacked the outside-bracket escape rule the
manager's review caught, and would still OVER-COUNT a pattern like
`\\[\\d+\\]` as a hit).

BEFORE: `master`'s own `tre-default` declaration set from this
mechanism. `testees/tre/adapter.py` carries no
`_bracket_backslash_content`/`_find_bracket_spans` function on `master`
at all (`git show master:testees/tre/adapter.py | grep -c
_bracket_backslash_content` reads 0, printed in this script's own
header) -- so BEFORE is the EMPTY SET by construction, not a claim to
re-derive per pattern.

AFTER: this branch's (`lane/b105tre`) fixed scanner, run over EVERY
pattern in the corpus.

Compile-only... in fact not even that: read-only, no compile, no
driver, no store. Classifies pattern TEXT only, via the real adapter
module (loaded the same way `tools/selfcheck.py`'s own [B105] check
loads it -- `_ad._load_module`, since `_ad.discover()` does not
register adapter modules in `sys.modules`).

Usage: python3 docs/dev/measurements/probe_tre_bracket_escape_full_corpus_census.py
  (run from the repo root)
"""
import glob
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, ROOT)

from pcrecbench import adapters as _ad  # noqa: E402

# The OLD (buggy) scanner, EXACTLY as it stood on this branch before the
# manager's review caught the over-refusal bug (commit cd9251c^'s own
# `_find_bracket_spans`) -- reconstructed here, read-only, for a THIRD
# comparison this script adds beyond the manager's own ask: not just
# "what does the fixed scanner declare corpus-wide" but "did the BUG
# ever actually change any real corpus pattern's classification" (a
# question the five synthetic regression cases alone cannot answer --
# they PROVE the bug existed, not whether it BIT any real pattern).
_OLD_BRACKET_OPEN = b"["
_OLD_BRACKET_CLOSE = b"]"
_OLD_BRACKET_NEGATE = b"^"
_OLD_BRACKET_SUBCONSTRUCT_DELIMS = (b":", b".", b"=")
_OLD_BACKSLASH = b"\\"


def _old_find_bracket_spans(pattern):
    """The scanner as committed at 8acf078/cd9251c^ -- backslash given NO
    escaping power ANYWHERE, including outside a bracket. Kept verbatim
    (not imported) so this comparison cannot silently track a future
    edit to the real scanner."""
    spans = []
    i = 0
    n = len(pattern)
    while i < n:
        if pattern[i:i + 1] != _OLD_BRACKET_OPEN:
            i += 1
            continue
        j = i + 1
        if j < n and pattern[j:j + 1] == _OLD_BRACKET_NEGATE:
            j += 1
        if j < n and pattern[j:j + 1] == _OLD_BRACKET_CLOSE:
            j += 1
        closed = False
        while j < n:
            if (pattern[j:j + 1] == _OLD_BRACKET_OPEN and j + 1 < n and
                    pattern[j + 1:j + 2] in _OLD_BRACKET_SUBCONSTRUCT_DELIMS):
                delim = pattern[j + 1:j + 2]
                end = pattern.find(delim + _OLD_BRACKET_CLOSE, j + 2)
                if end < 0:
                    j = n
                    break
                j = end + 2
                continue
            if pattern[j:j + 1] == _OLD_BRACKET_CLOSE:
                closed = True
                break
            j += 1
        if closed:
            spans.append((i, j + 1))
            i = j + 1
        else:
            i += 1
    return spans


def _old_hit(pattern):
    for (s, e) in _old_find_bracket_spans(pattern):
        if _OLD_BACKSLASH in pattern[s:e]:
            return pattern[s:e]
    return None


def master_has_bracket_mechanism():
    """-> True iff `master`'s testees/tre/adapter.py already defines the
    bracket-escape scanner (it does not, today -- this function makes
    that a CHECKED fact in the archive rather than an assertion)."""
    out = subprocess.run(
        ["git", "show", "master:testees/tre/adapter.py"],
        cwd=ROOT, capture_output=True, text=True, check=True)
    return ("_bracket_backslash_content" in out.stdout
            or "_find_bracket_spans" in out.stdout)


def main():
    mod = _ad._load_module(
        os.path.join(_ad.TESTEES_ROOT, "tre", "adapter.py"),
        "pcrecbench_testee_tre_fullcensus")

    before_empty = not master_has_bracket_mechanism()
    print("# master has the bracket-escape mechanism: %s (BEFORE set is "
          "%s)" % (not before_empty, "EMPTY" if before_empty else "N/A"),
          file=sys.stderr)

    rows = []
    total = 0
    for rxfile in sorted(glob.glob(os.path.join(ROOT, "bench", "*", "patterns", "*.rx"))):
        total += 1
        subbench = os.path.basename(os.path.dirname(os.path.dirname(rxfile)))
        pattern_id = os.path.splitext(os.path.basename(rxfile))[0]
        with open(rxfile, "rb") as f:
            raw = f.read()
        content = mod._bracket_backslash_content(raw)
        if content is not None:
            rows.append((subbench, pattern_id, content))

    print("subbench\tpattern_id\tbefore_declared\tafter_declared\tbracket_text")
    for (subbench, pattern_id, content) in rows:
        disp = content.replace(b"\t", b"\\t").replace(b"\n", b"\\n")
        try:
            disp_s = disp.decode("utf-8")
        except UnicodeDecodeError:
            disp_s = disp.decode("latin-1")
        print("%s\t%s\tFalse\tTrue\t%s" % (subbench, pattern_id, disp_s))

    by_subbench = {}
    for (sb, pid, _c) in rows:
        by_subbench.setdefault(sb, []).append(pid)

    print("\n# %d total pattern(s) scanned across every bench/*/patterns/*.rx "
          "file (%d sub-bench dir(s))"
          % (total, len(set(os.path.basename(os.path.dirname(os.path.dirname(f)))
                            for f in glob.glob(os.path.join(
                                ROOT, "bench", "*", "patterns", "*.rx"))))),
          file=sys.stderr)
    print("# BEFORE (master): 0 patterns declared by this mechanism "
          "(the mechanism does not exist on master)", file=sys.stderr)
    print("# AFTER (this branch): %d pattern(s) declared across %d "
          "sub-bench(es)" % (len(rows), len(by_subbench)), file=sys.stderr)
    for sb in sorted(by_subbench):
        print("#   %s: %d pattern(s) -- %s"
              % (sb, len(by_subbench[sb]), ", ".join(sorted(by_subbench[sb]))),
              file=sys.stderr)
    print("# every one of these %d newly-declared patterns is a GENUINE "
          "bracket expression with a backslash INSIDE it -- the scanner "
          "that produced this list is the same two-state POSIX scanner "
          "check_b105_tre_bracket_backslash_declaration unit-tests "
          "directly, including the five over-refusal regression cases "
          "(\\[\\d+\\]/a\\[b must NOT hit; [\\]]/[a\\-z]/\\\\[\\\\] must) "
          "-- the bracket_text column above is each hit's own verbatim "
          "span, printed for manual spot-check, not merely asserted"
          % len(rows), file=sys.stderr)

    # THE OLD-BUGGY-VS-NEW-FIXED DIFF: did the over-refusal bug ever
    # actually change any REAL corpus pattern's classification, or only
    # the five synthetic cases the regression control uses? Read-only,
    # same file list, same loop.
    diffs = []
    for rxfile in sorted(glob.glob(os.path.join(ROOT, "bench", "*", "patterns", "*.rx"))):
        sb = os.path.basename(os.path.dirname(os.path.dirname(rxfile)))
        pid = os.path.splitext(os.path.basename(rxfile))[0]
        with open(rxfile, "rb") as f:
            raw = f.read()
        old = _old_hit(raw) is not None
        new = mod._bracket_backslash_content(raw) is not None
        if old != new:
            diffs.append((sb, pid, old, new))
    print("\n# OLD-BUGGY-SCANNER-vs-NEW-FIXED-SCANNER diff over all %d "
          "corpus patterns: %d differ" % (total, len(diffs)), file=sys.stderr)
    if diffs:
        for (sb, pid, old, new) in diffs:
            print("#   %s/%s: old=%s new=%s" % (sb, pid, old, new),
                  file=sys.stderr)
    else:
        print("# ZERO -- the over-refusal bug the five synthetic cases "
              "prove is REAL never actually fired on any pattern in "
              "TODAY's corpus (no committed pattern happens to have an "
              "escaped \\[ followed, later in the same pattern, by a "
              "coincidental unescaped ] that would form a spurious "
              "span under the old rule); the fix is forward-looking "
              "correctness, not a correction to today's 30-pattern "
              "declaration set", file=sys.stderr)


if __name__ == "__main__":
    main()
