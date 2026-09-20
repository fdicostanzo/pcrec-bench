#!/usr/bin/env python3
r"""probe_rust_policy_vs_census_diff.py -- ([B58], lane b58census) THE
PATTERN-NAME-LEVEL RECONCILIATION of rust-default's capability@0.1
compile-outcome split.

The 2026-09-19 rust-first report's matrix reads 22 unsup + 1 refused + 2
wrong + 39 compiled-and-clean over the 64 patterns (reports/CLAUDE.md).
The 22 "unsup" come from `pcrecbench.capability`'s PRE-COMPILE policy
(REQUIRES(pattern) not-subset-of capabilities(rust-default) ->
`unsupported-by-declaration`, decided before any compile). The 22
"refused" the 2026-09-19 r1131 census (`probe_rust_capability_census.py`)
found calls the driver DIRECTLY, bypassing the policy -- so the two "22"
counts are not proof the two SETS are equal; this script derives the set
difference by name, using the REAL harness functions (`pcrecbench.
capability.pattern_requires`/`capabilities_for`/`missing_capabilities`,
never a re-typed copy of REQUIRES_VOCAB or the roster row) against the
REAL loaded sub-bench (`pcrecbench.subbench.load`, which resolves
`bench/capability`'s `rxt_source = "patterns.rxt"` sidecar key and
therefore reads patterns.rxt -- NOT the `subbench.toml` `[[patterns]]`
array, which `subbench.py`'s own loader IGNORES OUTRIGHT once
`rxt_source` is set (`pcrecbench/subbench.py`'s `Subbench.__init__`)).

A SEPARATE finding this script surfaces as a side effect (not asked for,
recorded because it would silently mislead a future reader): the
`subbench.toml` `[[patterns]]` array is STALE relative to `patterns.rxt`
-- it predates the b46tags REQUIRES-tag correction wave
(`bench/capability/NOTES.md`, `bench/capability/gen_patterns.py`'s own
comment above the `vectorscan-block-nosom` roster row) and is missing
`requires-backrefs` on `tag-depth3-bound` and several `requires-*`
tokens on five other patterns. This is HARMLESS at runtime (the sidecar
array is dead code once `rxt_source` is set) but would give a WRONG
answer to anyone who reads `subbench.toml` by hand instead of asking the
loaded `Subbench` object -- which is exactly what this script does, and
what a first pass at this task (reading `subbench.toml` with a bare
`tomllib.load`) got wrong before this was noticed and corrected.

Read-only: no compile, no timing, no store. It re-derives four census
facts by re-running the REAL adapter's `compile()` (needs the pinned
`rustc`/`cargo` toolchain per `testees/rust/CLAUDE.md`; ~1s) for exactly
the ONE pattern this script's own derivation flags as a policy/census
DISAGREEMENT, `balanced-parens-rec`, plus its isolated `(?R)`-shape
witnesses, to settle by a real run (not by re-reading the archived
census's prose) both (a) that it really compiles, and (b) what it
actually MATCHES -- the archived r1131 census only recorded COMPILED/
REFUSED, not a match-grain witness, and "compiles" alone does not say
whether `(?R)` inside it does anything resembling recursion.

Run from the repo root:
    python3 docs/dev/measurements/probe_rust_policy_vs_census_diff.py
"""
import os
import re
import sys
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, REPO_ROOT)

from pcrecbench import subbench as _sb              # noqa: E402
from pcrecbench import capability as _cap           # noqa: E402
from pcrecbench import adapters as _ad              # noqa: E402

TESTEE = "rust-default"
CENSUS_ARCHIVE = os.path.join(
    REPO_ROOT, "docs", "dev", "measurements",
    "2026-09-19-rust-capability-census-r1131.txt")
WORKDIR = os.path.join(REPO_ROOT, "build", "work", "rust-policy-diff")


def parse_census_corpus(path, header):
    """-> {pattern_name: "COMPILED"|"REFUSED"} for the
    `== corpus census: rust-default over bench/capability@0.1 ... ==`
    block in the archived census file. Parses the ARCHIVE, not a live
    re-run of the corpus census (the corpus pass is not re-run here --
    it already exists, witnessed, in the committed archive; only the ONE
    disagreement this script finds is re-run live, below)."""
    out = {}
    in_block = False
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.strip() == header:
                in_block = True
                continue
            if in_block:
                if line.strip().startswith("->"):
                    break
                m = re.match(r"^\s*(\S+)\s+(COMPILED|REFUSED)\b", line)
                if m:
                    out[m.group(1)] = m.group(2)
    return out


def main():
    sb = _sb.load(os.path.join(REPO_ROOT, "bench", "capability"))
    print("# sb.rxt loaded: %s (rxt_source=%r)"
         % (sb.rxt is not None, sb.cfg.get("rxt_source")))
    caps = _cap.capabilities_for(sb, TESTEE)
    print("# capabilities_for(%s) = %s" % (TESTEE, ", ".join(sorted(caps))))
    print()

    census = parse_census_corpus(
        CENSUS_ARCHIVE,
        "== corpus census: rust-default over bench/capability@0.1 (64 patterns) ==")
    print("# parsed %d rows from the archived r1131 corpus-census block"
         % len(census))
    assert len(census) == 64, "expected 64 parsed rows, got %d" % len(census)

    rows = []
    for p in sb.patterns:
        requires = _cap.pattern_requires(p)
        missing = _cap.missing_capabilities(sb, TESTEE, p)
        intercepted = bool(missing)
        census_outcome = census[p.name]
        if intercepted and census_outcome == "REFUSED":
            bucket = "1-intercepted+census-refused (agree)"
        elif intercepted and census_outcome == "COMPILED":
            bucket = "2-intercepted BUT census-COMPILES (disagree)"
        elif not intercepted and census_outcome == "REFUSED":
            bucket = "3-reaches-driver-and-refuses"
        else:
            bucket = "4-compiles-both"
        rows.append((p.name, sorted(requires), sorted(missing), intercepted,
                    census_outcome, bucket))

    rows.sort(key=lambda r: (r[5], r[0]))
    from collections import Counter
    counts = Counter(r[5] for r in rows)

    print()
    print("# per-pattern classification (%d rows)" % len(rows))
    print("%-45s %-45s %-30s %-10s %s" %
         ("pattern", "REQUIRES(pattern)", "missing (withheld tokens)",
          "census", "bucket"))
    for name, requires, missing, intercepted, outcome, bucket in rows:
        print("%-45s %-45s %-30s %-10s %s" %
             (name, ",".join(requires) or "-", ",".join(missing) or "-",
              outcome, bucket))

    print()
    print("# bucket counts")
    for b in sorted(counts):
        print("  %-45s %d" % (b, counts[b]))
    total = sum(counts.values())
    print("  %-45s %d" % ("TOTAL", total))
    assert total == 64

    unsup_names = sorted(r[0] for r in rows if r[3])
    print()
    print("# intercepted-by-policy set (%d): %s"
         % (len(unsup_names), ", ".join(unsup_names)))
    assert len(unsup_names) == 22, (
        "expected 22 policy-intercepted patterns (matches the committed "
        "matrix's 22 unsup rows), got %d" % len(unsup_names))

    census_refused_names = sorted(n for n, v in census.items() if v == "REFUSED")
    print("# census-refused set (%d): %s"
         % (len(census_refused_names), ", ".join(census_refused_names)))
    assert len(census_refused_names) == 22

    disagree = [r for r in rows if r[5].startswith("2-")]
    only_census_refused = [r for r in rows if r[5].startswith("3-")]
    print()
    print("# SET DIFFERENCE, by name:")
    print("#   in policy's unsup set but NOT in census's refused set (%d): %s"
         % (len(disagree), ", ".join(r[0] for r in disagree)))
    print("#   in census's refused set but NOT in policy's unsup set (%d): %s"
         % (len(only_census_refused), ", ".join(r[0] for r in only_census_refused)))

    # ------------------------------------------------------------------
    # Live re-run of the ONE disagreement, through the REAL adapter
    # (never the raw driver invoked by hand), to confirm it compiles and
    # to settle what `(?R)` actually MATCHES inside it -- a fact the
    # archived census's COMPILED/REFUSED grain cannot show.
    # ------------------------------------------------------------------
    assert len(disagree) == 1 and disagree[0][0] == "balanced-parens-rec", (
        "this script's live re-run section is written for exactly the "
        "one disagreement found at authoring time (balanced-parens-rec); "
        "the derivation above changed -- update this section before "
        "trusting its output")

    print()
    print("== live re-run: balanced-parens-rec, through testees/rust/adapter.py ==")
    adapter = _ad.discover()["rust"]
    adapter.prepare(TESTEE, WORKDIR)
    bpr = next(p for p in sb.patterns if p.name == "balanced-parens-rec")
    pat_bytes = sb.pattern_bytes(bpr.name)
    print("pattern bytes: %r" % pat_bytes)
    cp = adapter.compile(TESTEE, "c-balanced-parens-rec", pat_bytes, {}, 1, WORKDIR)
    res = cp.get(_ad.FORM_PLAIN)
    print("outcome: %s" % res.outcome)
    assert res.outcome == "compiled", "expected COMPILED, matching the r1131 census"

    def match_one(pattern_id, subject_bytes):
        tmp = tempfile.mkdtemp(prefix="rust-policy-diff-subj-")
        subj_path = os.path.join(tmp, "s.bin")
        with open(subj_path, "wb") as f:
            f.write(subject_bytes)

        class S:
            subject_id, path, length = "s", subj_path, len(subject_bytes)

        rows, _i, _n = adapter.measure(dict(res.handle), "search_short", [S()],
                                       1, 1, timeout=60)
        return rows[0][0]

    print()
    print("-- witness match grain (is (?R) doing recursion, or nothing?) --")
    for label, subj in (
            ("flat \"(abc)\" -- one pair, no nesting", b"(abc)"),
            ("nested \"(a(b)c)\" -- a REAL recursive engine matches [0,7)",
             b"(a(b)c)"),
            ("unbalanced \"(\"", b"(")):
        row = match_one(label, subj)
        print("  %-55s %-8s start=%s end=%s"
             % (label, row.answer, row.start, row.end))

    print()
    print("VERDICT: if the nested-subject match starts at 0 and ends at 7, "
         "(?R) performs real recursion; if it starts/ends anywhere else "
         "(e.g. matching only the INNER \"(b)\" pair), (?R) is a no-op "
         "here and the pattern is NOT actually testing recursion despite "
         "compiling -- the syntax-accepted/semantics-wrong shape the "
         "task brief's possessive-quantifier precedent describes, found "
         "instead on this corpus pattern.")

    print()
    print("== isolated (?R) shape witnesses, via the raw driver binary "
         "(never through the harness compile row) ==")
    drv = os.path.join(REPO_ROOT, "testees", "rust", "target", "release",
                       "rust_regex_driver")
    if not os.path.exists(drv):
        print("  (skipped: %s not built)" % drv)
        return
    import subprocess
    tmp = tempfile.mkdtemp(prefix="rust-policy-diff-isolated-")
    subj_path = os.path.join(tmp, "s.txt")
    with open(subj_path, "wb") as f:
        f.write(b"x")
    list_path = os.path.join(tmp, "list.tsv")
    with open(list_path, "w") as f:
        f.write("s1\t%s\n" % subj_path)
    for label, pat in (("(?R) alone", b"(?R)"),
                       ("(?R)* -- quantified directly", b"(?R)*"),
                       ("(?R)? -- quantified directly", b"(?R)?"),
                       ("a(?R) -- unquantified, in sequence", b"a(?R)"),
                       ("a(?R)?b -- the REQUIRES_VOCAB witness pattern",
                        b"a(?R)?b")):
        pat_path = os.path.join(tmp, "p.txt")
        with open(pat_path, "wb") as f:
            f.write(pat)
        r = subprocess.run([drv, "--pattern", pat_path, "--list", list_path,
                           "--mode", "search", "--iters", "1"],
                          capture_output=True, text=True)
        lines = [l for l in r.stdout.splitlines()
                if l.startswith("compile") or l.startswith("error")]
        print("  %-45s rc=%d  %s" % (label, r.returncode, lines))


if __name__ == "__main__":
    main()
