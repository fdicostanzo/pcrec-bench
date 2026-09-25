#!/usr/bin/env python3
"""gen_patterns.py -- THE MASTER PATTERN TABLE for bench/utf8@0.1 ([B77]
U4, docs/design/utf8_set_v1.md 5), the ONE place the set's 75 members +
floor are assembled and rendered into the set's two derived artifacts:

  * `patterns.rxt`     -- the SOURCE OF TRUTH: one `.rxt` file carrying
                          every pattern's text, a native `provenance`
                          sub-block, `tag family=/hazard=/requires=`
                          classification, and one file-scope `ext bench`
                          block carrying the twelve-config UTF-8 roster +
                          REQUIRES capability matrix (utf8_set_v1.md 7 --
                          transcribed from lane b77u2's own witness
                          census, `docs/dev/measurements/
                          2026-09-25-b77u2-utf8-witness-census.txt`, never
                          re-guessed).
  * `patterns/<id>.rx` -- one raw-bytes file per pattern, DERIVED from the
                          same table (`subbench.toml`'s `[[patterns]]`
                          entries point at these). `patterns.rxt` sits
                          beside `subbench.toml` with no `rxt_source =`
                          key, so `pcrecbench.capability` reads its own
                          `ext bench` block through the SIDECAR/SHIM path
                          (`rxt_source.load_aux_rows()`, capability.py's
                          own path (b)) while the [[patterns]] array
                          stays the harness's LOADED pattern source --
                          the same two-artifact split bench/capability
                          used before its own [B42] sidecar switch, kept
                          here deliberately rather than adopting
                          `rxt_source =` (untested against this set, and
                          not asked for by the U4 brief).

Every pattern's text is authored FRESH, transcribed verbatim from
`docs/design/utf8_set_v1.md` 5's own tables (this is a correctness/
encoding census, not a wild-provenance set -- capability_set_v1.md's
realism rule does not apply here). `provenance.source = "authored"` on
every member; `fidelity = "synthesized"`; `retrieved = "2026-09-25"`.

ONE EXCEPTION: `alt-cyr-64` (family d) is not literally transcribed --
its 64-branch Cyrillic word list is DERIVED here from the committed
`pool_cyr.tsv` (the last 64 of its 175 rows, file order), chosen so that
"дом" (house) -- the word `alt-cyr64-hit` (bench/utf8/gen_subjects.py,
lane b77u3) was typed assuming is present -- IS in the list (row 144 of
176, inside the last-64 slice) and "квинтэссенция" -- the word
`alt-cyr64-miss` assumes is absent -- is not in the pool AT ALL, so no
selection could include it. Verified against the real oracle, not
merely asserted structurally: see this lane's own report.

USAGE:
    gen_patterns.py                 write patterns.rxt + patterns/*.rx
    gen_patterns.py --check         re-derive and diff (structural only;
                                     no pcrec --list-source round-trip is
                                     wired -- see the report for why)
    gen_patterns.py --sidecar       print subbench.toml's [[patterns]]
                                     blocks (pasted into subbench.toml by
                                     hand, same convention as
                                     bench/capability/gen_patterns.py)
    gen_patterns.py --provenance    print provenance.tsv's rows
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATTERNS_RXT = os.path.join(HERE, "patterns.rxt")
PATTERNS_DIR = os.path.join(HERE, "patterns")
POOL_CYR = os.path.join(HERE, "pool_cyr.tsv")

# ---------------------------------------------------------------------------
# The closed vocabularies, declared as `.rxt vocabulary` lines so an
# out-of-set value is refused by the format itself. `REQUIRES_VOCAB` here
# is the SUBSET of pcrecbench.capability's 20-token global vocabulary this
# set's own 76 patterns actually use (six tokens); declaring only the used
# subset matches bench/capability's own practice of listing what a file
# actually spells; a token this set never uses (e.g. "backrefs") is simply
# absent, harmless (pcrecbench.capability.REQUIRES_VOCAB is the true
# closed set a load error is checked against, not this line).
# ---------------------------------------------------------------------------
FAMILY_VOCAB = ["cls", "lit", "ci", "alt-qnt", "asr", "prp", "floor"]
HAZARD_VOCAB = ["none"]
REQUIRES_VOCAB = ["utf8-encoding", "ascii-class-scope", "unicode-class-scope",
                  "lookaround", "true-end-anchor", "unicode-properties"]


def size_class(nbytes):
    if nbytes < 16:
        return "tiny"
    if nbytes < 256:
        return "small"
    return "medium"


class Pattern:
    __slots__ = ("id", "family", "hazard_class", "requires", "text",
                 "adaptation", "isolates")

    def __init__(self, id, family, text, requires, adaptation, isolates):
        self.id = id
        self.family = family
        self.hazard_class = "none"
        self.requires = list(requires)
        self.text = text.encode("utf-8")
        self.adaptation = adaptation
        self.isolates = isolates

    @property
    def nbytes(self):
        return len(self.text)


def _alt_cyr_64_words():
    with open(POOL_CYR, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    words = lines[1:]  # drop the `word` header
    assert len(words) == 175, (
        "pool_cyr.tsv: expected 175 words, got %d -- alt-cyr-64's "
        "last-64 slice and the дом/квинтэссенция guarantee below both "
        "depend on this exact count" % len(words))
    last64 = words[-64:]
    assert "дом" in last64, "alt-cyr-64: 'дом' not in the chosen 64 words"
    assert "квинтэссенция" not in words, (
        "alt-cyr-64: pool_cyr.tsv now carries 'квинтэссенция' -- "
        "re-check the alt-cyr64-miss subject's own assumption")
    return last64


# ---------------------------------------------------------------------------
# THE 76 PATTERNS -- text transcribed verbatim from utf8_set_v1.md 5's own
# tables (id, family, pattern text, requires tokens, "what it isolates").
# ---------------------------------------------------------------------------

def all_patterns():
    pats = []

    def add(id, family, text, requires=(), isolates=""):
        pats.append(Pattern(
            id=id, family=family, text=text, requires=requires,
            adaptation=("utf8_set_v1.md 5(%s): %s -- %s"
                        % (family, id, isolates)),
            isolates=isolates))

    U = ("utf8-encoding",)

    # ---- (a) CLASSES -- cls-*, 16 members ----
    add("cls-boundary-range", "cls", "[a-\u00e9]+", U,
        "a range SPANNING the 1-byte/multi-byte boundary")
    add("cls-high-range", "cls", "[\\x{100}-\\x{2000}]+", U,
        "a wholly-multi-byte range crossing the 2-byte/3-byte width "
        "boundary at U+0800")
    add("cls-neg-single", "cls", "[^\u00e9]", U,
        "negation of ONE non-ASCII character; complement within "
        "[0, 0x10FFFF]")
    add("cls-neg-allhigh", "cls", "[^\\x{80}-\\x{10FFFF}]+", U,
        "the negation whose complement is exactly ASCII")
    add("cls-mixed", "cls", "[a-z\u00e9\\x{430}-\\x{44F}]+", U,
        "ASCII + Latin-1 Supplement + Cyrillic in one class")
    add("cls-dot", "cls", ".", U, "'.' is ONE CHARACTER, not one byte")
    add("cls-dot-rep", "cls", "^.{5}$", U,
        "the sharpest encoded-length witness")
    add("cls-w-ascii", "cls", "\\w+", U + ("ascii-class-scope",),
        "\\w WITHOUT UCP: ASCII-scoped")
    add("cls-w-ucp", "cls", "(*UCP)\\w+", U + ("unicode-class-scope",),
        "the UCP twin of cls-w-ascii")
    add("cls-d-ascii", "cls", "\\d{4}", U + ("ascii-class-scope",),
        "designed NEAR-MISS against four Arabic-Indic digits")
    add("cls-d-ucp", "cls", "(*UCP)\\d{4}", U + ("unicode-class-scope",),
        "the UCP twin of cls-d-ascii: the SAME digits become a HIT")
    add("cls-s-nbsp", "cls", "a\\sb", U + ("ascii-class-scope",),
        "designed NEAR-MISS against a U+00A0 b")
    add("cls-s-ucp", "cls", "(*UCP)a\\sb", U + ("unicode-class-scope",),
        "the UCP twin of cls-s-nbsp: the SAME subject becomes a HIT")
    add("cls-posix-alpha", "cls", "[[:alpha:]]+", U + ("ascii-class-scope",),
        "the POSIX-class spelling of the same scope question")
    add("cls-lead-pair", "cls", "[\u03b1-\u03c9]+", U,
        "a TWO-lead-byte class (0xCE, 0xCF); memchr cannot filter it")
    add("cls-neg-cjk", "cls", "[^\\x{4E00}-\\x{9FFF}]+", U,
        "a negated 3-byte range, mostly FAILING over the cjk corpus")

    # ---- (b) LITERALS of multi-byte characters -- lit-*, 12 members ----
    add("lit-1ch-2b", "lit", "\u00e9", U, "one 2-byte character (C3 A9)")
    add("lit-1ch-3b", "lit", "\u65e5", U, "one 3-byte character (E6 97 A5)")
    add("lit-1ch-4b", "lit", "\U0001f600", U,
        "one 4-byte character (F0 9F 98 80)")
    add("lit-run-3", "lit", "\u65e5\u672c\u8a9e", U,
        "a 9-byte run of 3-byte characters; every necessary byte is HIGH")
    add("lit-mixed-ascii", "lit", "user@\u4f8b\u3048.jp", U,
        "mixed widths with an ASCII @ and . available as the necessary "
        "byte -- the CONTROL for lit-run-3")
    add("lit-cyr-run", "lit", "\u041c\u043e\u0441\u043a\u0432\u0430", U,
        "a 12-byte run whose every lead byte is 0xD0 or 0xD1")
    add("lit-offset-at-tail", "lit", "\u00e9@", U,
        "THE FIRST CUSTOMER: FP 3.1's live offset-skip witness")
    add("lit-offset-at-head", "lit", "@\u00e9", U,
        "its ORDER PAIR: the same three bytes, the other order")
    add("lit-nearmiss-run", "lit", "\u65e5\u672c\u8a9e", U,
        "the designed NEAR-MISS reading of lit-run-3 (against a subject "
        "sharing six of nine bytes)")
    add("lit-anchored-run", "lit", "^\u65e5\u672c\u8a9e$", U,
        "the anchored reading of lit-run-3")
    add("lit-nfc-pair", "lit", "caf\u00e9", U,
        "a designed MISS against a DECOMPOSED subject (no normalization "
        "claim)")
    add("lit-sharp-s", "lit", "Stra\u00dfe", U,
        "the German 2-byte \u00df in an otherwise ASCII literal")

    # ---- (c) CASELESS over non-ASCII -- ci-*, 12 members ----
    add("ci-e-acute", "ci", "(?i)\u00e9", U,
        "the simplest non-ASCII fold pair (U+00E9 / U+00C9)")
    add("ci-moskva", "ci", "(?i)\u043c\u043e\u0441\u043a\u0432\u0430", U,
        "a six-character Cyrillic fold set")
    add("ci-greek-run", "ci", "(?i)\u03b1\u03b2\u03b3", U,
        "a Greek fold set in a different lead-byte group")
    add("ci-kelvin", "ci", "(?i)k", U,
        "the closure reaching OUTSIDE the range: k/K plus U+212A KELVIN "
        "SIGN")
    add("ci-long-s", "ci", "(?i)s", U,
        "the same shape with U+017F LATIN SMALL LETTER LONG S")
    add("ci-class-range", "ci", "(?i)[a-z]+", U,
        "fold over a RANGE, pulling in partners outside it")
    add("ci-neg-fold", "ci", "(?i)[^\u00e9]", U,
        "FOLD BEFORE NEGATE: the closure applies before the complement")
    add("ci-strasse", "ci", "(?i)stra\u00dfe", U,
        "designed NEAR-MISS: must NOT match STRASSE (simple folding "
        "only)")
    add("ci-sigma", "ci", "(?i)\u03c3", U,
        "\u03c3/\u03a3/\u03c2 fold together under simple folding")
    add("ci-turkish-i", "ci", "(?i)i", U,
        "designed NEAR-MISS: must NOT match U+0130 or U+0131")
    add("ci-ascii-control", "ci", "(?i)abc", (),
        "the CONTROL: a pure-ASCII fold, byte-safe for TRE")
    add("ci-ucp-invariance", "ci", "(*UCP)(?i)\u00e9",
        U + ("unicode-class-scope",),
        "the control that says the fold is NOT UCP-gated")

    # ---- (d) ALTERNATION and QUANTIFIERS -- alt-*/qnt-*, 12 members ----
    add("alt-shared-char", "alt-qnt", "\u65e5\u672c|\u65e5\u66dc|\u65e5\u4ed8",
        U, "three branches sharing the whole first CHARACTER")
    add("alt-shared-lead", "alt-qnt", "\u03b1|\u03b2|\u03b3", U,
        "three branches sharing only the LEAD BYTE (0xCE)")
    add("alt-distinct-lead", "alt-qnt",
        "\u65e5\u672c|\u041c\u043e\u0441\u043a\u0432\u0430|caf\u00e9", U,
        "three branches, three lead-byte groups")
    add("alt-mixed-width", "alt-qnt", "a|\u00e9|\u65e5|\U0001f600", U,
        "one branch per encoded length: 1/2/3/4 bytes")
    add("alt-cyr-64", "alt-qnt", "|".join(_alt_cyr_64_words()), U,
        "the BRIDGE rung to bench/altwide@0.2's own width curve -- ONE "
        "rung, not a ladder")
    add("alt-nearmiss", "alt-qnt", "\u65e5\u672c\u8a9e|\u65e5\u672c\u56fd",
        U, "designed NEAR-MISS against a subject sharing six of nine "
        "bytes on both branches")
    add("qnt-plus-2b", "alt-qnt", "\u00e9+", U,
        "a quantified 2-byte character; BYTE-DECOMPOSED under byte mode")
    add("qnt-lazy-2b", "alt-qnt", "\u00e9+?", U,
        "the lazy twin of qnt-plus-2b")
    add("qnt-counted-3b", "alt-qnt", "(?:\u65e5\u672c){2,}", U,
        "a counted repeat of a two-character (6-byte) group")
    add("qnt-bounded-4b", "alt-qnt", "\U0001f600{2,4}", U,
        "a counted repeat of a 4-byte character: 8 to 16 bytes")
    add("qnt-dot-bounded", "alt-qnt", ".{3,8}", U,
        "a counted repeat of '.' -- characters, not bytes")
    add("qnt-class-run", "alt-qnt", "[\\x{400}-\\x{4FF}]{4,16}", U,
        "a counted repeat over a multi-byte CLASS")

    # ---- (e) ASSERTIONS -- asr-*, 11 members ----
    add("asr-b-ascii", "asr", "\\bcat\\b", (),
        "the pure-ASCII CONTROL, byte-safe for TRE")
    add("asr-b-cyr", "asr", "\\b\u041c\u043e\u0441\u043a\u0432\u0430\\b",
        U + ("ascii-class-scope",),
        "designed NEAR-MISS: without UCP a Cyrillic letter is NOT a "
        "word character")
    add("asr-b-cyr-ucp", "asr",
        "(*UCP)\\b\u041c\u043e\u0441\u043a\u0432\u0430\\b",
        U + ("unicode-class-scope",),
        "the UCP twin and control pair of asr-b-cyr")
    # (this lane's own reading of b77u2's finding 4: every \\b/\\B member
    # is class-scope-dependent -- \\B over \u00e9 answers match [0,0) under
    # the ASCII-\\w oracle and nomatch under a Unicode-\\w config
    # (onig-utf8, rust-default). Tagged ascii-class-scope so those two
    # configs read a clean unsupported-by-declaration census row instead
    # of a WRONG ANSWER on R0 -- see this lane's report.)
    add("asr-b-midchar", "asr", "\\B", U + ("ascii-class-scope",),
        "the only reachable half of axis 11 (K50's own witness shape)")
    add("asr-lb-fixed", "asr", "(?<=\u00e9)x", U + ("lookaround",),
        "fixed CHARACTER width 1, BYTE width 2")
    add("asr-lb-varwidth", "asr", "(?<=a|\u00e9)x", U + ("lookaround",),
        "branches of differing BYTE width at identical CHARACTER width")
    add("asr-lb-neg", "asr", "(?<!\u65e5)\u672c", U + ("lookaround",),
        "negative lookbehind over a 3-byte body")
    add("asr-lb-class", "asr", "(?<=[\\x{400}-\\x{4FF}])\\s",
        U + ("lookaround",), "a lookbehind over a multi-byte CLASS")
    add("asr-caret-ml", "asr", "(?m)^\u65e5", U,
        "multiline ^ over lines beginning with a 3-byte character")
    add("asr-dollar-ml", "asr", "(?m)\u8a9e$", U,
        "multiline $ at the end of a multi-byte line")
    add("asr-a-z", "asr", "\\A\u65e5\u672c\u8a9e\\z",
        U + ("true-end-anchor",), "true-end anchor over a multi-byte "
        "subject")

    # ---- (f) PROPERTIES -- prp-*, 12 members ----
    P = U + ("unicode-properties",)
    add("prp-l", "prp", "\\p{L}+", P,
        "the general category every \\p user reaches for first")
    add("prp-lu", "prp", "\\p{Lu}", P, "47 lead bytes -- a usable bitmap "
        "filter")
    add("prp-n", "prp", "\\p{N}+", P,
        "numbers incl. non-ASCII digits; the positive twin of cls-d-ascii")
    add("prp-notl", "prp", "\\P{L}+", P,
        "the negated category: complement over the whole universe")
    add("prp-zs", "prp", "\\p{Zs}", P,
        "space separators incl. U+00A0/U+3000; positive twin of "
        "cls-s-nbsp")
    add("prp-l-anchored", "prp", "^\\p{L}{4}$", P,
        "a counted property class: four CHARACTERS of unknown byte width")
    add("prp-cyrillic", "prp", "\\p{Cyrillic}+", P,
        "a script with two lead bytes -- the strongest script filter")
    add("prp-han", "prp", "\\p{Han}+", P,
        "a script with a wide 3-byte lead spread")
    add("prp-latin", "prp", "\\p{Latin}+", P,
        "a script spanning the 1-byte/multi-byte boundary")
    add("prp-greek", "prp", "\\p{Greek}", P,
        "the SPELLING PAIR half one: Script | Script_Extensions")
    add("prp-greek-sc", "prp", "\\p{sc=Greek}", P,
        "half two: Script alone")
    add("prp-ingreek", "prp", "\\p{InGreek}", P,
        "the REFUSAL WITNESS: PCRE2 10.46 refuses block names with "
        "error 147; no InGreek property exists")

    # ---- the floor ----
    add("floor", "floor", "~", (),
        "the floor pattern -- byte-safe for TRE, the one member whose "
        "compiled pcrec artifact should be identical under -e utf8 and "
        "-e byte")

    ids = [p.id for p in pats]
    assert len(ids) == len(set(ids)), "duplicate pattern id in the table"
    assert len(pats) == 76, "expected 76 patterns (75 + floor), got %d" \
        % len(pats)
    for p in pats:
        assert p.family in FAMILY_VOCAB, (p.id, p.family)
        assert p.hazard_class in HAZARD_VOCAB, (p.id, p.hazard_class)
        for r in p.requires:
            assert r in REQUIRES_VOCAB, (p.id, r)
    return pats


# ---------------------------------------------------------------------------
# `.rxt` rendering -- pattern_esc/needs_esc/render_provenance/
# render_pattern_block follow bench/capability/gen_patterns.py's own shape
# byte for byte (the format's seven-escape subject vocabulary), simplified
# for this set's uniform provenance (every member is authored, none has a
# URL/ref/attribution/twin/license beyond "n-a").
# ---------------------------------------------------------------------------

_ESC = {0x22: '\\"', 0x5c: "\\\\", 0x0a: "\\n", 0x09: "\\t", 0x0d: "\\r",
        0x0c: "\\f", 0x0b: "\\v"}


def pattern_esc(raw):
    out = []
    for b in raw:
        if b in _ESC:
            out.append(_ESC[b])
        elif 0x20 <= b <= 0x7e and b != 0x22 and b != 0x5c:
            out.append(chr(b))
        else:
            out.append("\\x%02x" % b)
    return '"' + "".join(out) + '"'


def needs_esc(raw):
    if b"\x00" in raw:
        raise AssertionError("NUL byte in pattern text -- refused by format")
    if b"\n" in raw or b"\r" in raw:
        return True
    for b in raw:
        if b < 0x20 or b > 0x7e:
            if b == 0x09:
                continue
            return True
    return False


def render_provenance(p):
    lines = ["provenance"]
    lines.append("  source authored")
    lines.append("  retrieved 2026-09-25")
    lines.append("  license n-a")
    lines.append("  fidelity synthesized")
    lines.append("  adaptation |")
    for ln in p.adaptation.splitlines() or [p.adaptation]:
        lines.append("    " + ln)
    return lines


def render_pattern_block(p):
    lines = []
    if needs_esc(p.text):
        lines.append("pattern-esc %s" % pattern_esc(p.text))
    else:
        lines.append("pattern %s" % p.text.decode("utf-8"))
    lines.append("name %s" % p.id)
    tag_items = ["family=%s" % p.family, "hazard=%s" % p.hazard_class]
    for r in p.requires:
        tag_items.append("requires=%s" % r)
    lines.append("tag " + ", ".join(tag_items))
    lines.extend(render_provenance(p))
    return lines


# ---------------------------------------------------------------------------
# The `ext bench` roster -- TRANSCRIBED from lane b77u2's witness census
# (docs/dev/measurements/2026-09-25-b77u2-utf8-witness-census.txt, its
# DECLARATIONS block) and utf8_set_v1.md 7.4's table, never re-guessed.
# Six tokens only (this set's own REQUIRES_VOCAB, above): the three new
# [B77] U1 tokens (utf8-encoding/ascii-class-scope/unicode-class-scope,
# the census's own S/-/- summary table) plus lookaround, true-end-anchor
# and unicode-properties, carried over from each engine's EXISTING
# capability (bench/capability/patterns.rxt's own EXT_BENCH_ROSTER for the
# byte-mode siblings) with two corrections this lane made on its own
# evidence, stated here rather than silently inherited:
#   * tre-default does NOT get true-end-anchor here, though
#     bench/capability/patterns.rxt's own roster declares it for
#     tre-default -- testees/tre/CLAUDE.md's OWN measured finding is that
#     TRE has NO \z/\A/\Z tokens at all (a literal \z compiles as literal
#     z), and utf8_set_v1.md 7.4 cites exactly this fact for asr-a-z's
#     exclusion. This lane's report flags the capability set's own
#     declaration as a candidate finding for that lane's owner, not fixed
#     here (out of this lane's scope: touching bench/capability is not
#     part of the utf8 U4 brief).
#   * onig-utf8/re2-utf8/vectorscan-...-utf8's unicode-class-scope
#     satisfaction is the b77u2 RE-CENSUS result (vectorscan: SATISFIED
#     via inline (*UCP), corrected from utf8_set_v1.md 7.6's v0.2 draft
#     prediction; onig/re2: NOT satisfied, (*UCP) refused outright).
# ---------------------------------------------------------------------------
EXT_BENCH_ROSTER = [
    ("pcre2-utf-interp", ("utf8-encoding", "ascii-class-scope",
                         "unicode-class-scope", "lookaround",
                         "true-end-anchor", "unicode-properties")),
    ("pcre2-utf-jit", ("utf8-encoding", "ascii-class-scope",
                       "unicode-class-scope", "lookaround",
                       "true-end-anchor", "unicode-properties")),
    ("pcre2-utf-dfa", ("utf8-encoding", "ascii-class-scope",
                       "unicode-class-scope", "lookaround",
                       "true-end-anchor", "unicode-properties")),
    ("pcrec-auto-utf8", ("utf8-encoding", "ascii-class-scope",
                         "lookaround", "true-end-anchor",
                         "unicode-properties")),
    ("pcrec-nocaps-utf8", ("utf8-encoding", "ascii-class-scope",
                           "lookaround", "true-end-anchor",
                           "unicode-properties")),
    ("pcrec-vm-utf8", ("utf8-encoding", "ascii-class-scope",
                       "lookaround", "true-end-anchor",
                       "unicode-properties")),
    ("pcrec-vm-in-utf8", ("utf8-encoding", "ascii-class-scope",
                         "lookaround", "true-end-anchor",
                         "unicode-properties")),
    ("re2-utf8", ("utf8-encoding", "ascii-class-scope",
                 "true-end-anchor", "unicode-properties")),
    ("onig-utf8", ("utf8-encoding", "lookaround", "true-end-anchor",
                  "unicode-properties")),
    ("vectorscan-block-nosom-utf8", ("utf8-encoding", "ascii-class-scope",
                                     "unicode-class-scope",
                                     "true-end-anchor",
                                     "unicode-properties")),
    ("rust-default", ("utf8-encoding", "true-end-anchor",
                      "unicode-properties")),
    ("tre-default", ("ascii-class-scope",)),
]


def render_ext_bench():
    lines = ["ext bench"]
    lines.append("  roster " + " ".join(t for t, _ in EXT_BENCH_ROSTER))
    for testee, caps in EXT_BENCH_ROSTER:
        lines.append("  capabilities %s" % testee)
        for c in caps:
            lines.append("    %s" % c)
    return "\n".join(lines)


def render_rxt(pats):
    out = []
    out.append("description |")
    out.append("  bench/utf8@0.1 -- the UTF-8 encoding set ([B77],")
    out.append("  inbox I-90). Seventy-five patterns in six")
    out.append("  encoding-dependence families plus the floor, BUILT ON")
    out.append("  this format as its pattern source of truth. See")
    out.append("  docs/design/utf8_set_v1.md and bench/utf8/NOTES.md.")
    out.append("")
    out.append("oracle pcre2")
    out.append("vocabulary family " + " ".join(FAMILY_VOCAB))
    out.append("vocabulary hazard " + " ".join(HAZARD_VOCAB))
    out.append("vocabulary requires " + " ".join(REQUIRES_VOCAB))
    out.append("tag set=utf8, version=0.1")
    out.append(render_ext_bench())
    out.append("")
    for p in pats:
        out.extend(render_pattern_block(p))
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def write_rx_files(pats, check=False):
    problems = []
    for p in pats:
        path = os.path.join(PATTERNS_DIR, p.id + ".rx")
        if check:
            if not os.path.exists(path):
                problems.append("missing patterns/%s.rx" % p.id)
                continue
            with open(path, "rb") as f:
                have = f.read()
            if have != p.text:
                problems.append("patterns/%s.rx does not match the table"
                                 % p.id)
        else:
            with open(path, "wb") as f:
                f.write(p.text)
    if os.path.isdir(PATTERNS_DIR):
        have_ids = {fn[:-3] for fn in os.listdir(PATTERNS_DIR)
                   if fn.endswith(".rx")}
        want_ids = {p.id for p in pats}
        if check:
            stale = have_ids - want_ids
            if stale:
                problems.append("stale patterns/*.rx not in the table: %s"
                                 % sorted(stale))
    return problems


def render_sidecar(pats):
    out = []
    for p in pats:
        tags = ["family-%s" % p.family, "hazard-%s" % p.hazard_class,
                "provenance-authored", "fidelity-synthesized"]
        for r in p.requires:
            tags.append("requires-%s" % r)
        out.append("[[patterns]]")
        out.append('name = "%s"' % p.id)
        out.append('file = "patterns/%s.rx"' % p.id)
        out.append('feature_tier = "base"')
        out.append('hazard_class = "%s"' % p.hazard_class)
        out.append('size_class = "%s"' % size_class(p.nbytes))
        out.append('convention = "perl-leftmost-first"')
        out.append("tags = [" + ", ".join('"%s"' % t for t in tags) + "]")
        out.append('role = "%s"' % ("floor" if p.family == "floor"
                                     else "member"))
        out.append("")
    return "\n".join(out)


def render_provenance_tsv(pats):
    cols = ["pattern_id", "family", "provenance_source", "source_url",
            "source_ref", "license", "retrieved", "fidelity", "adaptation",
            "attribution"]
    rows = ["\t".join(cols)]
    for p in pats:
        rows.append("\t".join([
            p.id, p.family, "authored", "", "", "n-a", "2026-09-25",
            "synthesized", p.adaptation.replace("\t", " "), ""]))
    return "\n".join(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--sidecar", action="store_true")
    ap.add_argument("--provenance", action="store_true")
    args = ap.parse_args()

    pats = all_patterns()

    if args.sidecar:
        print(render_sidecar(pats))
        return 0
    if args.provenance:
        print(render_provenance_tsv(pats))
        return 0

    rxt_text = render_rxt(pats)
    problems = []
    if args.check:
        if not os.path.exists(PATTERNS_RXT):
            problems.append("patterns.rxt does not exist")
        else:
            with open(PATTERNS_RXT, "r", encoding="utf-8") as f:
                have = f.read()
            if have != rxt_text:
                problems.append("patterns.rxt does not re-derive from the "
                                 "table (gen_patterns.py)")
        problems.extend(write_rx_files(pats, check=True))
        prov_path = os.path.join(HERE, "provenance.tsv")
        if os.path.exists(prov_path):
            with open(prov_path, "r", encoding="utf-8") as f:
                have_prov = f.read()
            if have_prov.rstrip("\n") != render_provenance_tsv(pats):
                problems.append("provenance.tsv does not re-derive from "
                                "the table (gen_patterns.py --provenance)")
        else:
            problems.append("provenance.tsv does not exist")
    else:
        os.makedirs(PATTERNS_DIR, exist_ok=True)
        with open(PATTERNS_RXT, "w", encoding="utf-8", newline="\n") as f:
            f.write(rxt_text)
        write_rx_files(pats, check=False)

    if problems:
        for p in problems:
            print("gen_patterns --check: %s" % p, file=sys.stderr)
        return 1
    n = len(pats)
    by_fam = {}
    for p in pats:
        by_fam.setdefault(p.family, 0)
        by_fam[p.family] += 1
    print("gen_patterns: %d pattern(s) across %d families -> %s, "
          "patterns/*.rx" % (n, len(by_fam), PATTERNS_RXT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
