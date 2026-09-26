"""expectations.py -- derive a sub-bench's `expectations.tsv` from the
libpcre2 oracle. The GENERIC half of a `bench/<name>/gen_expectations.py`.

Method `libpcre2-differential` (requirements 5): the CANONICAL answers, for
every testee, taken from the installed libpcre2-8 runtime through
`oracle_pcre2.py`. The oracle VERSION is read live off the loaded library and
written into every row -- an expectation whose oracle is not named is not an
expectation.

One row per (pattern x subject x regime), for every pattern and every regime
the sub-bench DECLARES:

  * `match`        -- the short subjects, PCRE2_ANCHORED|PCRE2_ENDANCHORED at
                      offset 0 (harness contract 2: whole-subject match).
  * `search_short` -- the short subjects within `short_search_max_bytes`,
                      unanchored at offset 0 (contract 2: SEARCH semantics).
  * `throughput`   -- the throughput subjects, unanchored: the FIRST match's
                      span AND the count of NON-OVERLAPPING matches, both
                      recorded, found by pcrec match_api.md S3.1's find-all
                      loop (KB-17, docs/dev/known_issues.md): the advance is
                      off the match's own reported START, never off the
                      previous scan position -- the same rule both drivers
                      use.

The regime -> subject mapping is never re-implemented here: `Subbench
.subjects_for()` is the one place it lives (`subbench.py`).

WHY IT IS SHARED. This file is `bench/email/gen_expectations.py`'s body,
lifted whole when the second sub-bench arrived ([B11.1]) rather than copied
into it. The expectation chain is the sub-bench contract's, not any one
sub-bench's: two copies would be two chances for a set's expectations to be
derived by slightly different rules and no way to see it from either file.
The per-sub-bench script keeps only what is genuinely local -- its directory,
and whatever it wants to say about ITS patterns in `--report`.

WHAT IS NOT RECORDED, and why: capture-level expectations. `derive()` CHECKS
on every run that no capturing group participated in any match, on any
pattern, over every subject and regime, and says so on stderr -- so a set
that grows one is caught rather than silently under-specified. The general
capture-correspondence contract stays where requirements 12 puts it: OD-B9,
with the first non-PCRE2 adapter.

An oracle GIVE-UP (a match-limit or depth-limit error, never NOMATCH) is not
folded into "no match": the triple is dropped from the file and listed on
stderr, because an expectation derived from a give-up is a wrong answer
recorded as ground truth.
"""
import argparse
import os
import sys

from . import capability as _cap
from . import oracle_pcre2 as oracle
from .subbench import load as load_subbench

HEADER = ("pattern\tsubject\tregime\texpected\tstart\tend\tnmatches"
          "\tmethod\toracle")
METHOD = "libpcre2-differential"

# The order rows are written in. A sub-bench that declares a subset gets the
# subset, in this order -- so a file's row order is a property of the format
# and not of the order someone happened to list the regimes in the sidecar.
REGIME_ORDER = ("match", "search_short", "throughput")


def oracle_option_word(sb, pattern):
    """[B77] U1 (docs/design/utf8_set_v1.md 8.1, 14 Q9): the ORACLE OPTION
    WORD for ONE pattern of `sb` -- the parameter on the shared oracle
    module, decided in ONE place so the expectations and the drivers'
    find-all advance can never be told two different things:

      * PCRE2_UTF iff the SET declares `[expectations] encoding = "utf8"`
        (every pattern alike -- no per-subject or per-regime variation);
      * PCRE2_UCP iff the PATTERN declares the `unicode-class-scope`
        REQUIRES token (`requires-unicode-class-scope`).

    Multiline is NOT in the word: every set spells it inline (`(?m)`).
    For every set that declares neither (every set before bench/utf8) the
    word is 0 -- the byte oracle, byte-identical to the pre-[B77] one."""
    return oracle.option_word(
        utf=(sb.encoding == "utf8"),
        ucp=("unicode-class-scope" in _cap.pattern_requires(pattern)))


def utf8_advance(sb, pattern):
    """True iff `pattern`'s oracle word carries PCRE2_UTF -- the ONE fact
    that turns on the character-boundary find-all advance in the oracle
    AND (through `harness.run_cell` -> the handle's `utf8_advance` key ->
    each adapter's `--utf8` driver flag) in every driver."""
    return bool(oracle_option_word(sb, pattern) & oracle.PCRE2_UTF)


class OracleRefusalError(Exception):
    """An oracle COMPILE refusal the set did not declare, or a declared
    refusal the oracle compiled. Either way the set's own claim about which
    patterns libpcre2 refuses is false, and no expectations are written."""


def derive(sb, report=False, expected_refusals=frozenset(), refusals=None):
    """-> (rows, giveups, oracle_version). `rows` are TSV column tuples.

    ORACLE COMPILE REFUSALS ([B77] U5). A pattern libpcre2 refuses to
    compile carries NO expectation rows -- the refusal IS its answer, the
    first-class `did-not-compile` compile-axis outcome with no match rows
    (utf8_set_v1.md 5(f)'s `prp-ingreek`; bench/bounded's 65535 rung is the
    precedent, KB-4). It is legal ONLY where the calling set DECLARES it in
    `expected_refusals` (pattern names): an undeclared refusal, or a
    declared pattern that compiles, raises `OracleRefusalError` BY NAME --
    never a silent skip, never a crash with no pattern named. Each declared
    refusal is appended to `refusals` (when given) as `(pattern, message)`
    so the caller can print it."""
    version = oracle.version()
    rows = []
    giveups = []
    ncaps_seen = {}
    declared = set(expected_refusals)
    unknown = declared - {p.name for p in sb.patterns}
    if unknown:
        raise OracleRefusalError(
            "declared oracle refusal(s) %s name no pattern of %s"
            % (sorted(unknown), sb.id))

    for pat in sb.patterns:
        text = sb.pattern_bytes(pat.name)
        try:
            rx = oracle.compile(text, oracle_option_word(sb, pat))
        except oracle.Pcre2Error as e:
            if pat.name not in declared:
                raise OracleRefusalError(
                    "%s: pattern %r: the oracle REFUSED to compile it and "
                    "the set does not declare that refusal: %s"
                    % (sb.id, pat.name, e)) from e
            if refusals is not None:
                refusals.append((pat.name, str(e)))
            continue
        if pat.name in declared:
            raise OracleRefusalError(
                "%s: pattern %r is declared an oracle refusal but libpcre2 "
                "%s COMPILED it" % (sb.id, pat.name, version))
        for regime in REGIME_ORDER:
            if regime not in sb.regimes:
                continue
            for subj in sb.subjects_for(regime):
                body = sb.subject_bytes(subj.subject_id)
                try:
                    if regime == "match":
                        got = rx.match(body, 0)
                        span, groups = (got if got else (None, ()))
                        n = "-"
                    elif regime == "search_short":
                        got = rx.search(body, 0)
                        span, groups = (got if got else (None, ()))
                        n = "-"
                    else:
                        span, count = rx.find_all(body)
                        groups = ()
                        n = str(count)
                except oracle.Pcre2Error as e:
                    giveups.append((pat.name, subj.subject_id, regime, str(e)))
                    continue
                if groups:
                    ncaps_seen.setdefault(pat.name, set()).update(
                        i for i, g in enumerate(groups, 1) if g is not None)
                if span is None:
                    rows.append((pat.name, subj.subject_id, regime,
                                 "nomatch", "-", "-", n, METHOD, version))
                else:
                    rows.append((pat.name, subj.subject_id, regime,
                                 "match", str(span[0]), str(span[1]), n,
                                 METHOD, version))
    if report:
        for name in sorted(ncaps_seen):
            print("NOTE: pattern %r had participating capture groups %s in at "
                  "least one subject -- the 'span is the whole answer' claim "
                  "in this sub-bench's NOTES.md needs revisiting."
                  % (name, sorted(ncaps_seen[name])), file=sys.stderr)
        if not ncaps_seen:
            print("checked: no capturing group participated in any match, on "
                  "any pattern, over every subject and regime -- the span is "
                  "the whole observable answer for this sub-bench.",
                  file=sys.stderr)
    return rows, giveups, version


def main(here, argv=None, doc=None, expected_refusals=frozenset()):
    """The `gen_expectations.py` command line, for the sub-bench at `here`.
    `expected_refusals`: the pattern names this set DECLARES the oracle
    refuses to compile (see `derive`)."""
    ap = argparse.ArgumentParser(description=doc or __doc__.splitlines()[0])
    ap.add_argument("--out", default=os.path.join(here, "expectations.tsv"))
    ap.add_argument("--check", action="store_true",
                    help="re-derive and DIFF against the committed file "
                         "instead of writing it (the `make check` mode)")
    ap.add_argument("--report", action="store_true", default=True)
    args = ap.parse_args(argv)

    sb = load_subbench(here)
    refusals = []
    rows, giveups, version = derive(sb, report=args.report,
                                    expected_refusals=expected_refusals,
                                    refusals=refusals)
    for p, msg in refusals:
        print("ORACLE REFUSED (declared; no expectation rows, by design): "
              "%s: %s" % (p, msg), file=sys.stderr)

    for p, s, r, msg in giveups:
        print("ORACLE GAVE UP, triple DROPPED: %s / %s / %s: %s"
              % (p, s, r, msg), file=sys.stderr)

    text = HEADER + "\n" + "\n".join("\t".join(r) for r in rows) + "\n"

    if args.check:
        if not os.path.exists(args.out):
            print("gen_expectations --check: %s does not exist" % args.out,
                  file=sys.stderr)
            return 1
        with open(args.out, "r", encoding="utf-8") as f:
            have = f.read()
        if have != text:
            print("gen_expectations --check: %s does NOT re-derive from the "
                  "oracle (libpcre2 %s)" % (args.out, version), file=sys.stderr)
            hl, tl = have.splitlines(), text.splitlines()
            for i in range(max(len(hl), len(tl))):
                a = hl[i] if i < len(hl) else "<absent>"
                b = tl[i] if i < len(tl) else "<absent>"
                if a != b:
                    print("  line %d committed: %s" % (i + 1, a), file=sys.stderr)
                    print("  line %d derived  : %s" % (i + 1, b), file=sys.stderr)
                    break
            return 1
        print("gen_expectations --check: %d expectation(s) re-derive from "
              "libpcre2 %s" % (len(rows), version))
        return 0

    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("gen_expectations: %d expectation(s) from libpcre2 %s -> %s"
          % (len(rows), version, args.out))
    return 0
