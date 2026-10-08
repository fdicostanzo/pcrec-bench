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

THE SECOND METHOD ([B125], capability@0.2; docs/design/expectation_methods_v1.md).
A set that declares `[expectations] fallback_methods = ["structural-alphabet", "libpcre2-dfa-fallback"]`
gets a second chance for exactly the triples the backtracker GAVE UP on:
`pcre2_dfa_match` from the same pinned libpcre2 (no backtracking, no match
limit). It is not the backtracker's equal. It reports the longest match at
the leftmost start and no captures, so it may state ONLY:

  (1) NOMATCH -- for a pattern whose DFA reading is exact (`dfa_features`
      finds no backreference, recursion, atomic group, possessive quantifier,
      \\K, \\C, verb, conditional, callout, branch reset, free-spacing or \\Q);
  (2) a MATCH, only when every match of the pattern provably starts at
      offset 0 and ends at the subject end (`fully_anchored`: a leading `^`,
      a trailing `\\z` or `$` at depth 0, no top-level alternation, no
      multiline, and -- for `$` -- a subject that does not end in "\\n"),
      so the span is (0, N) and a find-all count is 1.

Anything else stays DROPPED and is listed by name. The restriction is code
(`dfa_fallback`), not prose alone. Its CONTROL shares no matching algorithm
with what it checks: over every triple the backtracker DID answer, for every
DFA-compatible pattern, the dfa's existence answer and leftmost start must
agree with the backtracker's (and the span and count too, where the anchoring
rule applies) -- `DfaControl`; any disagreement fails the run.
Every other triple of the set keeps method `libpcre2-differential`,
byte-identical to a derivation without the fallback.
"""
import argparse
import os
import re
import sys

from . import capability as _cap
from . import oracle_pcre2 as oracle
from .subbench import FALLBACK_METHODS, load as load_subbench

HEADER = ("pattern\tsubject\tregime\texpected\tstart\tend\tnmatches"
          "\tmethod\toracle")
METHOD = "libpcre2-differential"
METHOD_DFA = "libpcre2-dfa-fallback"
assert METHOD_DFA in FALLBACK_METHODS   # subbench.py validates the sidecar key

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


# --------------------------------------------------------------------------
# [B125] the structural reading of a pattern's TEXT that the second method's
# restrictions rest on. Deliberately CONSERVATIVE: a construct it does not
# understand is reported as a feature that makes the pattern ineligible, so
# an error here can only cost a restoration, never record a wrong answer.
# --------------------------------------------------------------------------
_QUANT_RE = re.compile(rb"\{\d+(?:,\d*)?\}")
_RECURSE_RE = re.compile(rb"\(\?(?:R|&|[-+]?\d|P>)")
_FLAG_GROUP_RE = re.compile(rb"\(\?([a-zA-Z]*)(?:-([a-zA-Z]*))?([:)])")

# Features that make the DFA's reading of a pattern differ from the
# backtracker's (or an error): see the module docstring.
DFA_INCOMPATIBLE = frozenset((
    "backref", "recursion", "atomic", "possessive", "k-reset", "C", "G",
    "verb", "conditional", "callout", "branch-reset", "free-spacing",
    "quote", "unparsed"))


def pattern_structure(text):
    """-> (features, depth0_alt, multiline, last) for pattern bytes `text`.
    `last` is ("$"|"\\z"|"other", depth_at_it, index) for the final token."""
    t = bytes(text)
    n = len(t)
    feats = set()
    depth = 0
    depth0_alt = False
    multiline = False
    prev_quant = False           # the previous token was a quantifier
    last = ("other", 0, -1)
    in_class = False
    i = 0
    while i < n:
        c = t[i:i + 1]
        if in_class:
            if c == b"\\":
                i += 2
            elif c == b"[" and t[i + 1:i + 2] == b":":    # [:alpha:]
                j = t.find(b":]", i + 2)
                i = (j + 2) if j >= 0 else i + 1
            else:
                if c == b"]":
                    in_class = False
                i += 1
            continue
        tok = i
        is_quant = False
        kind = "other"
        if c == b"\\":
            d = t[i + 1:i + 2]
            if d == b"":
                feats.add("unparsed")
                break
            if d in b"123456789gk":
                feats.add("backref")
            elif d == b"K":
                feats.add("k-reset")
            elif d == b"C":
                feats.add("C")
            elif d == b"G":
                feats.add("G")
            elif d == b"Q":
                feats.add("quote")
            if d == b"z":
                kind = "\\z"
            i += 2
        elif c == b"[":
            in_class = True
            i += 1
            if t[i:i + 1] == b"^":
                i += 1
            if t[i:i + 1] == b"]":                        # leading literal ]
                i += 1
        elif c == b"(":
            i += 1
            if t[i:i + 1] == b"*":
                feats.add("verb")
            elif t[i:i + 1] == b"?":
                rest = t[i + 1:i + 2]
                two = t[i + 1:i + 3]
                if _RECURSE_RE.match(t, i - 1):
                    feats.add("recursion")
                elif two == b"P=":
                    feats.add("backref")
                elif rest == b">":
                    feats.add("atomic")
                elif rest == b"|":
                    feats.add("branch-reset")
                elif rest == b"(":
                    feats.add("conditional")
                elif rest == b"C":
                    feats.add("callout")
                elif rest == b"#":
                    j = t.find(b")", i)
                    if j < 0:
                        feats.add("unparsed")
                        break
                    i = j + 1
                    prev_quant = False
                    continue
                elif rest in (b"=", b"!") or two in (b"<=", b"<!"):
                    pass                                   # lookaround: fine
                elif rest in (b"<", b"'") or two == b"P<":
                    pass                                   # named group: fine
                else:
                    m = _FLAG_GROUP_RE.match(t, i - 1)
                    if not m:
                        feats.add("unparsed")
                    else:
                        on, off = m.group(1), m.group(2) or b""
                        if b"x" in on or b"x" in off:
                            feats.add("free-spacing")
                        if b"m" in on or b"m" in off:
                            multiline = True
                        if m.group(3) == b")":             # a flag setter
                            i = m.end()
                            prev_quant = False
                            continue
            depth += 1
        elif c == b")":
            depth -= 1
            i += 1
        elif c == b"|":
            if depth == 0:
                depth0_alt = True
            i += 1
        elif c in (b"*", b"+", b"?"):
            if prev_quant and c == b"+":
                feats.add("possessive")
            elif prev_quant and c == b"?":
                pass                                       # the lazy marker
            else:
                is_quant = True
            i += 1
        elif c == b"{":
            m = _QUANT_RE.match(t, i)
            if m:
                is_quant = True
                i = m.end()
            else:
                i += 1
        elif c == b"$":
            kind = "$"
            i += 1
        else:
            i += 1
        prev_quant = is_quant
        last = (kind, depth, tok)
    if in_class or depth != 0:
        feats.add("unparsed")
    return feats, depth0_alt, multiline, last


def dfa_features(text):
    """The set of DFA-incompatible features `text` carries (empty = the DFA's
    reading of the pattern is exact)."""
    feats, _alt, _ml, _last = pattern_structure(text)
    return sorted(feats & DFA_INCOMPATIBLE)


def fully_anchored(text, body):
    """Restriction (2): True iff EVERY match of `text` over `body` provably
    starts at offset 0 and ends at len(body). Never True for a pattern the
    DFA cannot read exactly."""
    t = bytes(text)
    feats, alt, multiline, last = pattern_structure(t)
    if feats & DFA_INCOMPATIBLE or alt or multiline:
        return False
    if not t.startswith(b"^") or t[1:2] in (b"*", b"+", b"?", b"{"):
        return False
    kind, depth, _idx = last
    if depth != 0:
        return False
    if kind == "\\z":
        return True
    if kind == "$":
        # `$` also matches before a FINAL newline: the end is then N or N-1.
        return not bytes(body).endswith(b"\n")
    return False


def dfa_fallback(rx, text, body, regime):
    """The second method's decision for ONE triple the backtracker gave up
    on. -> (row_fields, None) with row_fields = (expected, start, end, n),
    or (None, reason) when the triple must stay DROPPED."""
    if regime not in ("search_short", "throughput"):
        return None, "the fallback speaks for search_short/throughput only"
    bad = dfa_features(text)
    if bad:
        return None, "pattern not DFA-readable (%s)" % ",".join(bad)
    try:
        got = rx.dfa_search(body)
    except oracle.Pcre2Error as e:
        return None, "the dfa also gave up: %s" % e
    n_nomatch = "0" if regime == "throughput" else "-"
    if got is None:
        return ("nomatch", "-", "-", n_nomatch), None
    if not fully_anchored(text, body):
        return None, ("dfa found a match but its span/count are not "
                      "determined (pattern not fully anchored, or `$` with a "
                      "final newline)")
    if got != (0, len(body)):
        raise AssertionError(
            "the structural rule says every match is (0, %d) but the dfa "
            "reported %r -- the anchoring check is wrong" % (len(body), got))
    n = "1" if regime == "throughput" else "-"
    return ("match", "0", str(len(body)), n), None


# --------------------------------------------------------------------------
# [B125] THE STRUCTURAL ALPHABET RULE (method `structural-alphabet`), NOMATCH
# ONLY. SOUNDNESS ARGUMENT. Take a pattern `^BODY$` or `^BODY\z` (no flag
# group, so no multiline) in which BODY is built ONLY from literals, bracket
# classes, \s \d \w, groups, alternation inside groups and quantifiers. Every
# byte a match consumes is consumed by one atom of BODY, so it lies in the
# union alphabet A of BODY's atoms. The `^` pins the match start to 0 and
# there is no top-level alternation to escape it; `\z` pins the end to N,
# `$` pins it to N, or to N-1 when the subject ends in a newline (the
# default newline convention is LF; a trailing CR or CRLF is excluded as
# well, conservatively). So every byte of the subject, minus that one
# optional trailing newline under `$`, MUST be in A for a match to exist; a
# single byte outside A means NO match. The rule never states a match, and
# anything the parser does not fully understand DECLINES -- the parser is a
# whitelist, not a filter. It shares no matching algorithm with the oracle
# (set membership against a byte set), and `DfaControl` checks its verdict
# against the backtracker's on every triple the backtracker answered.
# --------------------------------------------------------------------------
METHOD_STRUCT = "structural-alphabet"

_SET_S = frozenset(b"\t\n\x0b\x0c\r ")
_SET_D = frozenset(b"0123456789")
_SET_W = frozenset(b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
_ALL = frozenset(range(256))
_CLASS_ESC = {ord("s"): _SET_S, ord("d"): _SET_D, ord("w"): _SET_W}
_CTRL_ESC = {ord("t"): 9, ord("n"): 10, ord("r"): 13, ord("f"): 12}
_PLAIN_SPECIAL = frozenset(b"\\^$.|?*+()[]{}")


class _Decline(Exception):
    pass


class _AlphaParser:
    def __init__(self, t):
        self.t = t
        self.i = 0
        self.alpha = set()

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else None

    def alt(self, depth):
        self.seq(depth)
        while self.peek() == ord("|"):
            if depth == 0:
                raise _Decline("top-level alternation")
            self.i += 1
            self.seq(depth)

    def seq(self, depth):
        while True:
            c = self.peek()
            if c is None or c == ord("|") or c == ord(")"):
                return
            self.atom(depth)
            self.quant()

    def esc(self, in_class):
        # at a backslash
        self.i += 1
        d = self.peek()
        if d is None:
            raise _Decline("trailing backslash")
        self.i += 1
        if d in _CLASS_ESC:
            return _CLASS_ESC[d], None
        if d in _CTRL_ESC:
            return None, _CTRL_ESC[d]
        if d < 128 and not chr(d).isalnum() and chr(d) != "_":
            return None, d                  # an escaped punctuation literal
        raise _Decline("escape \\%s" % chr(d))

    def atom(self, depth):
        c = self.peek()
        if c == ord("("):
            self.i += 1
            if self.peek() == ord("?"):
                if self.t[self.i:self.i + 2] != b"?:":
                    raise _Decline("group kind")
                self.i += 2
            self.alt(depth + 1)
            if self.peek() != ord(")"):
                raise _Decline("unbalanced")
            self.i += 1
        elif c == ord("["):
            self.cls()
        elif c == ord("\\"):
            st, lit = self.esc(False)
            self.alpha |= st if st is not None else {lit}
        elif c in _PLAIN_SPECIAL:
            raise _Decline("special %s" % chr(c))
        else:
            self.alpha.add(c)
            self.i += 1

    def cls(self):
        self.i += 1
        neg = False
        if self.peek() == ord("^"):
            neg = True
            self.i += 1
        if self.peek() == ord("]"):
            raise _Decline("leading ] in class")
        members = set()
        prev = None                          # last single byte (range start)
        while True:
            c = self.peek()
            if c is None:
                raise _Decline("unterminated class")
            if c == ord("]"):
                self.i += 1
                break
            if c == ord("["):
                raise _Decline("posix class / nested [")
            if c == ord("\\"):
                st, lit = self.esc(True)
                if st is not None:
                    members |= st
                    prev = None
                    continue
                cur = lit
            else:
                cur = c
                self.i += 1
            # a range `prev-cur2`?
            if self.peek() == ord("-") and self.t[self.i + 1:self.i + 2] not in (b"]", b""):
                self.i += 1
                hi = self.peek()
                if hi == ord("\\"):
                    st, hlit = self.esc(True)
                    if st is not None:
                        raise _Decline("class escape as range end")
                    hi = hlit
                else:
                    if hi in (ord("["),):
                        raise _Decline("range end [")
                    self.i += 1
                if hi < cur:
                    raise _Decline("reversed range")
                members |= set(range(cur, hi + 1))
                prev = None
            else:
                members.add(cur)
                prev = cur
        self.alpha |= (_ALL - members) if neg else members

    def quant(self):
        c = self.peek()
        if c in (ord("*"), ord("+"), ord("?")):
            self.i += 1
        elif c == ord("{"):
            import re as _re
            m = _QUANT_RE.match(self.t, self.i)
            if not m:
                raise _Decline("bare {")
            self.i = m.end()
        else:
            return
        if self.peek() == ord("?"):
            self.i += 1                      # lazy marker
        elif self.peek() == ord("+"):
            raise _Decline("possessive")
        if self.peek() in (ord("*"), ord("+"), ord("?"), ord("{")):
            raise _Decline("stacked quantifier")


def structural_alphabet(text):
    """-> (alphabet frozenset, end_kind "$"|"\\z") for a pattern in the rule's
    scope, or raises _Decline(reason)."""
    t = bytes(text)
    if not t.startswith(b"^"):
        raise _Decline("no leading ^")
    def _bs_before(n):          # backslashes immediately before index n
        k = 0
        while n - 1 - k >= 0 and t[n - 1 - k] == ord("\\"):
            k += 1
        return k

    if t.endswith(b"\\z") and _bs_before(len(t) - 2) % 2 == 0:
        kind, body = "\\z", t[1:-2]
    elif t.endswith(b"$") and _bs_before(len(t) - 1) % 2 == 0:
        kind, body = "$", t[1:-1]
    else:
        raise _Decline("no trailing $ or \\z")
    p = _AlphaParser(body)
    p.alt(0)
    if p.i != len(body):
        raise _Decline("unparsed tail at %d" % p.i)
    return frozenset(p.alpha), kind


def structural_nomatch(text, body):
    """-> (True, None) when the rule PROVES `text` has no match over `body`;
    (False, reason) when it declines or the subject lies inside A."""
    try:
        alpha, kind = structural_alphabet(text)
    except _Decline as e:
        return False, "structural-alphabet declines: %s" % e
    covered = bytes(body)
    if kind == "$":
        for tail in (b"\r\n", b"\n", b"\r"):
            if covered.endswith(tail):
                covered = covered[:-len(tail)]
                break
    if not covered:
        return False, "structural-alphabet: nothing to refute"
    if covered.translate(None, bytes(sorted(alpha))):
        return True, None
    return False, "structural-alphabet: every subject byte is inside the alphabet"


class DfaControl:
    """The control's tally. `disagreements` non-empty fails the run."""

    def __init__(self):
        self.answered = 0          # backtracker-answered triples seen
        self.compat = 0            # ... of DFA-readable patterns
        self.incompat = {}         # feature -> triples skipped
        self.exist_agree = 0       # existence AND leftmost start agree
        self.span_checked = 0      # fully anchored: span (and count) agree
        self.dfa_errors = []       # the dfa raised (not a disagreement)
        self.disagreements = []
        self.struct_applies = 0    # triples where structural-alphabet PARSES
        self.struct_nomatch = 0    # ... and states nomatch
        self.struct_agree = 0      # ... and the backtracker agrees

    def feed(self, name, subject_id, regime, rx, text, body, bt_first, bt_count):
        self.answered += 1
        # The structural rule is cheap: checked on EVERY answered triple.
        try:
            structural_alphabet(text)
            self.struct_applies += 1
            hit, _why = structural_nomatch(text, body)
            if hit:
                self.struct_nomatch += 1
                if bt_first is None:
                    self.struct_agree += 1
                else:
                    self.disagreements.append(
                        (name, subject_id, regime, bt_first,
                         "structural-alphabet said nomatch"))
        except _Decline:
            pass
        bad = dfa_features(text)
        if bad:
            for f in bad:
                self.incompat[f] = self.incompat.get(f, 0) + 1
            return
        self.compat += 1
        try:
            got = rx.dfa_search(body)
        except oracle.Pcre2Error as e:
            self.dfa_errors.append((name, subject_id, regime, str(e)))
            return
        want = bt_first
        if (got is None) != (want is None) or (
                got is not None and got[0] != want[0]):
            self.disagreements.append((name, subject_id, regime, want, got))
            return
        self.exist_agree += 1
        if fully_anchored(text, body):
            self.span_checked += 1
            if got is not None and got != want:
                self.disagreements.append((name, subject_id, regime, want, got))
            if bt_count is not None and bt_count != (0 if got is None else 1):
                self.disagreements.append(
                    (name, subject_id, regime, "count %d" % bt_count, got))

    def summary(self):
        return ("dfa control: %d backtracker-answered triple(s); %d on "
                "DFA-readable patterns, %d skipped (%s); existence+start "
                "agree on %d; span+count agree on %d anchored; dfa errors "
                "%d; structural-alphabet: parses on %d, states nomatch on %d, "
                "oracle agrees on %d; DISAGREEMENTS %d"
                % (self.answered, self.compat, self.answered - self.compat,
                   ", ".join("%s %d" % kv for kv in sorted(self.incompat.items()))
                   or "none", self.exist_agree, self.span_checked,
                   len(self.dfa_errors), self.struct_applies,
                   self.struct_nomatch, self.struct_agree,
                   len(self.disagreements)))


class OracleRefusalError(Exception):
    """An oracle COMPILE refusal the set did not declare, or a declared
    refusal the oracle compiled. Either way the set's own claim about which
    patterns libpcre2 refuses is false, and no expectations are written."""


def derive(sb, report=False, expected_refusals=frozenset(), refusals=None,
           fallbacks=None, control=None):
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
    so the caller can print it.

    THE SECOND METHOD ([B125]). When the set declares `fallback_methods` (tried in order), a
    triple the backtracker gave up on goes to `dfa_fallback`; a row it can
    state is written with method `libpcre2-dfa-fallback` and appended to
    `fallbacks` (when given) as `(pattern, subject, regime, expected, method, why-it-gave-up)`; one it
    cannot stays in `giveups`, now as `(pattern, subject, regime, message)`
    with the reason appended. `control` (a `DfaControl`, when given) is fed
    every triple the backtracker ANSWERED. A set without `fallback_methods`
    is derived exactly as it was."""
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
                    if sb.fallback_methods:
                        why_all = []
                        for meth in sb.fallback_methods:
                            if meth == METHOD_STRUCT:
                                hit, why = structural_nomatch(text, body)
                                fb = (("nomatch", "-", "-",
                                       "0" if regime == "throughput" else "-")
                                      if hit and regime != "match" else None)
                            else:
                                fb, why = dfa_fallback(rx, text, body, regime)
                            if fb is not None:
                                rows.append((pat.name, subj.subject_id,
                                             regime, fb[0], fb[1], fb[2],
                                             fb[3], meth, version))
                                if fallbacks is not None:
                                    fallbacks.append((pat.name, subj.subject_id,
                                                      regime, fb[0], meth,
                                                      str(e)))
                                break
                            why_all.append(why)
                        else:
                            giveups.append((pat.name, subj.subject_id, regime,
                                            "%s; fallbacks declined: %s"
                                            % (e, " | ".join(why_all))))
                        continue
                    giveups.append((pat.name, subj.subject_id, regime, str(e)))
                    continue
                if control is not None and regime != "match":
                    control.feed(pat.name, subj.subject_id, regime, rx, text,
                                 body, span,
                                 int(n) if regime == "throughput" else None)
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
    ap.add_argument("--no-control", action="store_true",
                    help="skip the dfa control (a set with `fallback_methods` "
                         "runs it on every derivation otherwise)")
    args = ap.parse_args(argv)

    sb = load_subbench(here)
    refusals = []
    fallbacks = []
    control = DfaControl() if sb.fallback_methods and not args.no_control else None
    rows, giveups, version = derive(sb, report=args.report,
                                    expected_refusals=expected_refusals,
                                    refusals=refusals, fallbacks=fallbacks,
                                    control=control)
    for p, s_, r, x, meth, msg in fallbacks:
        print("ORACLE GAVE UP, RESTORED by %s: %s / %s / %s -> %s (%s)"
              % (meth, p, s_, r, x, msg), file=sys.stderr)
    if control is not None:
        print(control.summary())
        for d in control.dfa_errors:
            print("dfa control: the dfa itself errored (not a disagreement): "
                  "%s / %s / %s: %s" % d, file=sys.stderr)
        if control.disagreements:
            for d in control.disagreements:
                print("DFA CONTROL DISAGREEMENT: %s / %s / %s: backtracker %r, "
                      "dfa %r" % d, file=sys.stderr)
            print("gen_expectations: the dfa control FAILED -- the second "
                  "method is not trustworthy for this set; nothing written",
                  file=sys.stderr)
            return 2
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
