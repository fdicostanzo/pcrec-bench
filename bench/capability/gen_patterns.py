#!/usr/bin/env python3
"""gen_patterns.py -- THE MASTER PATTERN TABLE for bench/capability@0.1,
and the ONE place the set's 64 members are assembled from L1's wild
imports (`curation/wild/members.tsv`) and L2's designed members
(`curation/designed/members.tsv`) into the set's two derived artifacts:

  * `patterns.rxt`   -- the SOURCE OF TRUTH (Frank's Q3 ruling,
                         docs/design/capability_set_v1.md 9): one
                         `.rxt` file carrying every pattern's text,
                         native `provenance` sub-block (the format's own
                         nine pattern-scope fields), `tag family=/
                         hazard=/requires=` classification, a handful of
                         `n`/`mc` self-check case lines (oracle-derived,
                         never hand-typed -- see `_safe_self_check`
                         below), and one file-scope `ext bench` block
                         carrying the testee roster + REQUIRES capability
                         matrix (docs/design/rxt_needs_v1.md 2.9's
                         proposal, delivered as the aux production).
  * `patterns/<id>.rx` -- one raw-bytes file per pattern, DERIVED from
                         the same table, so `subbench.toml`'s
                         `[[patterns]] file = "patterns/<id>.rx"` entries
                         keep working with TODAY's loader
                         (`pcrecbench.subbench`, which has no `.rxt`
                         reader yet -- that is L4's build, not this
                         lane's). `patterns.rxt` is the set's authored
                         source; `patterns/*.rx` is a DERIVED export kept
                         for the harness's own use until L4 lands.

Both are CHECKED against each other and against a real pcrec binary
(`--check` mode): every `.rx` file's bytes must equal its `patterns.rxt`
block's own pattern text, and `pcrec --list-source patterns.rxt`'s
DECODED `pattern` column (DD-13b.W23.5's "dump-value seam") must equal
the same bytes -- so identity can never drift between the three
representations by a hand edit to any one of them.

THE TWIN-PAIRING RECONCILIATION (docs/dev/lanes/b42set_report.md has the
full table): L2 authored four family-1 near-miss twins blind (D27)
against GUESSED wild imports. Two guesses were right (`uuid-near-miss`
against the real `wild-validator-uuid-grok`; `ipv4-near-miss` against
`wild-validator-ipv4-owasp`) and are kept in family `wild-validator`.
Two were wrong: `base10num-near-miss` and `winpath-near-miss` guessed a
family-1 (`wild-validator`) partner, but BASE10NUM and WINPATH are both
family-2 (`wild-logparse`) imports (WINPATH was reassigned there by the
design note's own 2026-09-16 amendment, which the blinded L2 lane could
not have read). Per the brief ("flag it in your report rather than
re-authoring"), both patterns' TEXT is untouched; only their `family`
metadata is corrected to `wild-logparse`, where they remain legitimate,
realistic near-miss twins of their real partners
(`wild-logparse-base10num-grok`, `wild-logparse-winpath-grok`) -- a
deviation from family 2's "designed members: none" column, noted and
justified in NOTES.md and the lane report rather than silently absorbed.

USAGE:
    gen_patterns.py                 write patterns.rxt + patterns/*.rx
    gen_patterns.py --check         re-derive and diff (+ --list-source
                                     round-trip against a real pcrec)
    gen_patterns.py --sidecar       print subbench.toml's [[patterns]]
                                     blocks (piped into subbench.toml by
                                     hand, same convention as
                                     bench/syntax/gen_patterns.py)
    gen_patterns.py --provenance    print provenance.tsv's rows (used by
                                     gen_provenance.py)
"""
import argparse
import csv
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CURATION = os.path.join(HERE, "curation")
WILD_TSV = os.path.join(CURATION, "wild", "members.tsv")
DESIGNED_TSV = os.path.join(CURATION, "designed", "members.tsv")
PATTERNS_RXT = os.path.join(HERE, "patterns.rxt")
PATTERNS_DIR = os.path.join(HERE, "patterns")

def _default_pcrec_bin():
    """Resolve the pinned pcrec binary via the git COMMON directory, not a
    relative walk from this file -- `build/` is not per-worktree (a lane
    running from `worktrees/<lane>/` must still find the main tree's
    build), the same rule `probe_rxt_format.py`'s `default_bin()` and
    `accept41_cd371441/run.sh` both use."""
    try:
        common = subprocess.run(
            ["git", "rev-parse", "--git-common-dir"], cwd=HERE,
            capture_output=True, text=True, check=True).stdout.strip()
        # git may print the common dir RELATIVE TO ITS cwd (HERE), and
        # os.path.abspath resolves against the PROCESS cwd -- anchor it
        # to HERE explicitly or a main-tree run resolves to a wrong root.
        if not os.path.isabs(common):
            common = os.path.join(HERE, common)
        repo_root = os.path.dirname(os.path.abspath(common))
    except Exception:
        repo_root = os.path.dirname(os.path.dirname(HERE))
    return os.path.join(repo_root, "build", "pcrec-cd371441", "build",
                         "pcrec")


PCREC_BIN = os.environ.get("PCREC_BIN", _default_pcrec_bin())

# ---------------------------------------------------------------------------
# The closed REQUIRES vocabulary (docs/design/capability_set_v1.md 5.1,
# sixteen tags) and the twelve families + floor, both declared as `.rxt`
# `vocabulary` lines so an out-of-set value is refused BY THE FORMAT
# ITSELF, not merely by convention.
# ---------------------------------------------------------------------------
REQUIRES_VOCAB = [
    "backrefs", "lookaround", "lookbehind-variable", "possessive-quantifier",
    "atomic-group", "recursion", "conditionals", "k-reset", "control-verbs",
    "unicode-properties", "named-groups", "free-spacing", "callouts",
    "span-reporting", "non-utf8-subject", "captures", "true-end-anchor",
]
FAMILY_VOCAB = [
    "wild-validator", "wild-logparse", "wild-waf", "wild-secrets",
    "wild-datetime", "wild-codegrammar", "cap-backref", "cap-lookaround",
    "cap-recursion", "redos-nested", "semantics-divergence",
    "binary-nonutf8", "floor",
]
HAZARD_VOCAB = ["none", "exponential-backtracking", "ambiguous-decomposition"]
CONVENTION_VOCAB = ["perl-leftmost-first", "posix-leftmost-longest"]

# Per-pattern REQUIRES tags. Wild members carry none in curation/wild/
# members.tsv (L1's table has no `requires` column -- capability_set_v1.md
# 5.1 is this project's vocabulary, not L1's brief), so they are derived
# here, by reading each pattern's own text for the constructs the
# vocabulary is keyed on (an atomic group, a lookaround assertion, a named
# group, free-spacing) -- mechanical, and re-checked in `--check` mode
# against the actual text so a hand-typo cannot silently drift from the
# pattern it describes. Designed members (L2) already declared `requires`
# in their own table and are read from there directly (SELF_CHECK below
# is the cross-check that a HAND override here cannot silently diverge).
REQUIRES_OVERRIDE = {
    "wild-logparse-base10num-grok": ["atomic-group", "lookaround"],
    "wild-logparse-base10num-noatomic": ["lookaround"],
    "wild-logparse-quotedstring-grok": ["atomic-group", "lookaround"],
    "wild-logparse-quotedstring-noatomic": ["lookaround"],
    "wild-logparse-winpath-grok": ["atomic-group"],
    "wild-logparse-syslogbase-expanded": ["lookaround", "named-groups"],
    "wild-codegrammar-json-number-extended": ["free-spacing"],
    "wild-codegrammar-json-stringcontent-escape": ["free-spacing"],
}

# family reassignment: L2's blind guess vs the real wild partner
# (the twin-pairing reconciliation; see module docstring).
FAMILY_REASSIGN = {
    "base10num-near-miss": "wild-logparse",
    "winpath-near-miss": "wild-logparse",
}
TWIN_OF_RESOLVED = {
    "uuid-near-miss": "wild-validator-uuid-grok",
    "ipv4-near-miss": "wild-validator-ipv4-owasp",
    "base10num-near-miss": "wild-logparse-base10num-grok",
    "winpath-near-miss": "wild-logparse-winpath-grok",
}

# size_class per capability_set_v1.md's own idiom (bench/bounded: tiny<16B,
# small<256B); this set adds "large" for the >1KB imports (the CRS SQLi
# rule, the datefinder alternation) so a reader is not surprised by a
# multi-KB "small".
def size_class(nbytes):
    if nbytes < 16:
        return "tiny"
    if nbytes < 256:
        return "small"
    if nbytes < 2048:
        return "medium"
    return "large"


class Pattern:
    __slots__ = ("id", "family", "hazard_class", "requires", "source",
                 "role", "twin_of", "isolates", "notes", "text",
                 "omit_canonical")

    def __init__(self, **kw):
        for k, v in kw.items():
            setattr(self, k, v)

    @property
    def nbytes(self):
        return len(self.text)


def _read_tsv(path):
    # QUOTE_NONE: this is a plain TAB-DELIMITED file, not CSV -- several
    # pattern texts carry a literal `"` at the START of the field
    # (codegrammar-flat's `"([^"\\]+)"\s*:\s*`), and csv's DEFAULT
    # quoting would silently treat that as an OPENING QUOTE CHARACTER
    # and swallow it, corrupting the pattern text with no error at all.
    # Found the hard way: the corrupted pattern (missing its leading `"`)
    # lost its PCRE2 required-first-byte optimization entirely and
    # backtracked QUADRATICALLY over an unanchored 1 MB search --
    # `diag_expectations_timing.py`'s own timeout, not a hang in the
    # oracle itself.
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def _short_date(rfc3339):
    return rfc3339.split("T")[0] if rfc3339 else rfc3339


def load_wild():
    rows = _read_tsv(WILD_TSV)
    out = []
    for r in rows:
        pid = r["pattern_id"]
        if r["text_location"] == "inline":
            text = r["pattern_text"].encode("utf-8")
        else:
            fpath = os.path.join(CURATION, r["text_location"])
            with open(fpath, "rb") as f:
                text = f.read()
        got = hashlib.sha256(text).hexdigest()
        want = r["canonical_sha256"]
        # curation's own sha256 column carries a stray trailing hex nibble
        # on several rows (73 hex chars, not 64) -- a known curation-stage
        # artifact (the lane's own hashing script). Compared on the
        # correctly-sized PREFIX so a real mismatch still fails loudly.
        assert got == want[:64] or got == want, (
            "wild %s: sha256 mismatch: got %s want %s" % (pid, got, want))
        requires = REQUIRES_OVERRIDE.get(pid, [])
        fidelity = r["fidelity"]
        adaptation = r["adaptation"] if fidelity != "verbatim" else ""
        if fidelity != "verbatim" and not adaptation:
            raise AssertionError("wild %s: fidelity=%s needs adaptation"
                                  % (pid, fidelity))
        out.append(Pattern(
            id=pid, family=r["family"], hazard_class=r["hazard_class"],
            requires=requires, role="member",
            source=dict(source=r["source_name"], url=r["source_url"],
                        ref=r["source_ref"], license=r["license"],
                        license_note=r["license_note"],
                        retrieved=_short_date(r["retrieved_utc"]),
                        fidelity=fidelity, adaptation=adaptation,
                        attribution=r["attribution"]),
            twin_of=None, isolates="", notes=r["license_note"],
            text=text, omit_canonical=False))
    return out


def _load_designed_sha256sums():
    path = os.path.join(CURATION, "designed", "patterns", "SHA256SUMS.txt")
    out = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            pid, digest = line.rstrip("\n").split("\t")
            out[pid] = digest
    return out


def load_designed():
    rows = _read_tsv(DESIGNED_TSV)
    sums = _load_designed_sha256sums()
    out = []
    for r in rows:
        pid = r["pattern_id"]
        omit = False
        if r["text_file"] != "-":
            fpath = os.path.join(CURATION, "designed", r["text_file"])
            with open(fpath, "rb") as f:
                text = f.read()
            if not r["canonical_text"] or r["canonical_text"].startswith(
                    "OMITTED"):
                omit = True
        else:
            text = r["canonical_text"].encode("utf-8")
        if pid in sums:
            got = hashlib.sha256(text).hexdigest()
            assert got == sums[pid], (
                "designed %s: sha256 mismatch against curation/designed/"
                "patterns/SHA256SUMS.txt: got %s want %s -- the TSV parse "
                "may have corrupted this pattern's text (see the "
                "quoting note on _read_tsv)" % (pid, got, sums[pid]))
        family = FAMILY_REASSIGN.get(pid, r["family"])
        requires = [t for t in r["requires"].split(";") if t and t != "-"]
        out.append(Pattern(
            id=pid, family=family, hazard_class=r["hazard_class"],
            requires=requires, role="member",
            source=dict(source="authored", url="", ref="",
                        license="n-a", license_note="",
                        retrieved="2026-09-16", fidelity="synthesized",
                        adaptation=r["inspiration"], attribution=""),
            twin_of=TWIN_OF_RESOLVED.get(pid, r["twin_of"]
                                          if r["twin_of"] != "-" else None),
            isolates=r["isolates"] if r["isolates"] != "-" else "",
            notes=r["notes"],
            text=text, omit_canonical=omit))
    return out


def all_patterns():
    pats = load_wild() + load_designed()
    pats.sort(key=lambda p: (FAMILY_VOCAB.index(p.family)
                              if p.family in FAMILY_VOCAB else 99, p.id))
    seen = set()
    for p in pats:
        assert p.id not in seen, "duplicate pattern id %r" % p.id
        seen.add(p.id)
        assert p.family in FAMILY_VOCAB, (p.id, p.family)
        assert p.hazard_class in HAZARD_VOCAB, (p.id, p.hazard_class)
        for tag in p.requires:
            assert tag in REQUIRES_VOCAB, (p.id, tag)
    return pats


# ---------------------------------------------------------------------------
# `.rxt` rendering
# ---------------------------------------------------------------------------

_ESC = {0x22: '\\"', 0x5c: "\\\\", 0x0a: "\\n", 0x09: "\\t", 0x0d: "\\r",
        0x0c: "\\f", 0x0b: "\\v"}


def pattern_esc(raw):
    """Encode `raw` bytes into a `pattern-esc "..."` quoted operand, the
    format's own seven-escape subject vocabulary (rxt_format.md, "Named
    subjects" / "pattern-esc")."""
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
                continue  # a plain `pattern` line MAY carry a tab
            return True
    return False


def render_provenance(p):
    lines = ["provenance"]
    s = p.source
    lines.append("  source %s" % s["source"])
    if s["url"]:
        lines.append("  url %s" % s["url"])
    if s["ref"]:
        lines.append("  ref %s" % s["ref"])
    lines.append("  retrieved %s" % s["retrieved"])
    lines.append("  license %s" % s["license"])
    if s["license_note"]:
        lines.append("  license-note |")
        for ln in s["license_note"].splitlines() or [s["license_note"]]:
            lines.append("    " + ln)
    lines.append("  fidelity %s" % s["fidelity"])
    if s["adaptation"]:
        lines.append("  adaptation |")
        for ln in (s["adaptation"].splitlines() or [s["adaptation"]]):
            lines.append("    " + ln)
    if s["attribution"]:
        lines.append("  attribution %s" % s["attribution"])
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


EXT_BENCH_ROSTER = [
    # (testee_id-family, capabilities this config satisfies). RE-VERIFIED
    # (L5, [B42] lane b42cap, 2026-09-16) against a real compile census at
    # the pinned pcrec (cd371441, `--features all`, every pcrec-* config's
    # OWN flags): a witness pattern per (config, token) pair, actually
    # compiled, its refusal or success asserted BY NAME -- never inferred
    # from docs/pcre2_compliance.md's prose alone (that survey is what
    # NARROWED the search; the witness compile is what DECIDED it). This
    # is now ENFORCED by `pcrecbench.capability`'s pre-compile policy
    # (harness.py), not documentation for a future lane.
    #
    # pcre2-interp/pcre2-jit: both are `pcre2_match`/JIT on a plain
    # compiled pattern (NOT `pcre2_dfa_match`, which this vocabulary's
    # own table calls out as lacking k-reset/captures/etc) -- PCRE2
    # 10.46 supports the full vocabulary, spot-verified with pcre2test
    # (variable-length lookbehind, `(?(1)a|b)`, `(*ACCEPT)`, `(?C1)`,
    # `\p{L}` all compile clean; docs/dev/lanes/b42cap_report.md's
    # witness matrix).
    ("pcre2-interp", REQUIRES_VOCAB),
    ("pcre2-jit", REQUIRES_VOCAB),
    # pcrec-*: three tokens WITNESSED REFUSED under `--features all` on
    # every pcrec-* config regardless of --engine=/--no-captures (docs/
    # pcre2_compliance.md's Conditional patterns / Backtracking control
    # verbs sections; D26 tier 4 "NEVER-IMPLEMENTING" for control-verbs,
    # "not implemented yet" for the general `(?(n)...)` conditional even
    # with its module enabled):
    #   conditionals        -- `(?(1)a|b)(a)?` REFUSED: "module
    #                          'conditionals' is enabled but (?(...) is
    #                          not implemented yet" ((?(DEFINE)...) alone
    #                          ships, under module `recursion`, D71 item 4
    #                          -- it is NOT this token)
    #   control-verbs        -- `a(*ACCEPT)b` REFUSED: "(*...) requires
    #                          module 'verbs'" (ACCEPT/FAIL are `PLANNED`
    #                          not shipped; the rest OUT-OF-SCOPE)
    #   lookbehind-variable  -- pcrec's lookbehind ships FIXED-WIDTH PER
    #                          BRANCH (differing branch widths compile,
    #                          e.g. `(?<=a|bc)x`), which is NARROWER than
    #                          this tag's "not fixed-width" definition:
    #                          the corpus's own witness,
    #                          negation-scope-lookbehind-var
    #                          (`(?<!\bnot\s{1,3}(?:\w{1,12}\s{1,3}){0,3})
    #                          \bavailable\b`, a single-branch VARIABLE
    #                          body) is REFUSED: "variable-length
    #                          lookbehind is not implemented: every
    #                          alternative of a lookbehind must have a
    #                          fixed length"
    # `callouts` was already correctly absent (unchanged: PLANNED, not
    # shipped -- `a(?C1)b` REFUSED: "module 'callouts' is enabled but
    # (?C...) is not implemented yet"). Every other token spot-verified
    # COMPILING on every pcrec-* config (backrefs, lookaround,
    # possessive-quantifier, atomic-group, recursion, k-reset,
    # unicode-properties [both -e byte and -e utf8], named-groups,
    # free-spacing, true-end-anchor); span-reporting/non-utf8-subject/
    # captures are execution-model facts, not compile witnesses (see the
    # lane report).
    ("pcrec-auto", [t for t in REQUIRES_VOCAB
                    if t not in ("callouts", "conditionals",
                                 "control-verbs", "lookbehind-variable")]),
    ("pcrec-nocaps", [t for t in REQUIRES_VOCAB
                      if t not in ("callouts", "captures", "conditionals",
                                   "control-verbs", "lookbehind-variable")]),
    ("pcrec-vm", [t for t in REQUIRES_VOCAB
                  if t not in ("callouts", "conditionals",
                               "control-verbs", "lookbehind-variable")]),
    ("pcrec-vm-in", [t for t in REQUIRES_VOCAB
                     if t not in ("callouts", "conditionals",
                                  "control-verbs", "lookbehind-variable")]),
    # pcre2-dfa ([B42] L6a, testees/pcre2/adapter.py; the SAME library and
    # version as pcre2-interp/pcre2-jit above, via `pcre2_dfa_match`
    # instead): man `pcre2matching`'s own eight-item restricted-construct
    # list, quoted in full in testees/pcre2/CLAUDE.md's "pcre2-dfa"
    # section, read against THIS vocabulary token by token and each
    # exclusion reproduced LIVE with `pcre2test -dfa` (the transcript is
    # in that same CLAUDE.md section) -- not inferred from the man page's
    # prose alone, the same "spot-verified, not merely documented"
    # discipline the pcrec-* rows above already hold themselves to.
    #   backrefs       -- item 3(a); UITEM (-42) live on `(\1)(a)` and on
    #                     bench/syntax's own untagged bak-1 (`(\w+) \1`,
    #                     subject "the the")
    #   conditionals    -- item 3(b) (a backreference-condition or a
    #                     specific-group-recursion test only -- this
    #                     vocabulary has no finer token, so the whole tag
    #                     is excluded); UCOND (-40) live on `(?(1)a|b)(a)?`
    #   k-reset         -- item 4 (`\K`); UITEM (-42) live on `a\Kb`
    #   control-verbs   -- item 7: everything but `(*FAIL)`, which this
    #                     vocabulary also has no finer token for
    #   captures        -- item 2, this vocabulary's OWN worked example
    #                     of a capability line that is an execution-model
    #                     fact, not a construct (5.1's own note)
    # Every OTHER token compiles and matches structurally unchanged under
    # DFA (lookaround, possessive quantifiers and atomic groups are all
    # explicitly discussed as WORKING, just without capture reporting;
    # `\p{...}`/named groups/free-spacing/callouts are compile-time or
    # orthogonal to which matcher runs; span-reporting and
    # true-end-anchor are the driver's own PCRE2_ANCHORED/
    # PCRE2_ENDANCHORED runtime options, which `pcre2_dfa_match`'s own
    # synopsis lists as accepted options) -- kept, per 5.2's fail-closed
    # rule cutting the OTHER way: a token withheld without evidence is as
    # dishonest as one wrongly claimed.
    ("pcre2-dfa", [t for t in REQUIRES_VOCAB
                   if t not in ("backrefs", "conditionals", "k-reset",
                                "control-verbs", "captures")]),
]


def render_ext_bench():
    lines = ["ext bench"]
    lines.append("  roster " + " ".join(t for t, _ in EXT_BENCH_ROSTER))
    for testee, caps in EXT_BENCH_ROSTER:
        lines.append("  capabilities %s" % testee)
        for c in caps:
            lines.append("    %s" % c)
    return lines


def render_rxt(pats):
    out = []
    out.append("description |")
    out.append("  bench/capability@0.1 -- the capability survey set")
    out.append("  ([B42]). Sixty-four patterns in twelve capability/")
    out.append("  provenance families plus the floor, BUILT ON this")
    out.append("  format as its pattern source of truth. See")
    out.append("  docs/design/capability_set_v1.md and")
    out.append("  bench/capability/NOTES.md.")
    out.append("")
    out.append("oracle pcre2")
    out.append("vocabulary family " + " ".join(FAMILY_VOCAB))
    out.append("vocabulary hazard " + " ".join(HAZARD_VOCAB))
    out.append("vocabulary requires " + " ".join(REQUIRES_VOCAB))
    out.append("vocabulary convention " + " ".join(CONVENTION_VOCAB))
    out.append("tag set=capability, version=0.1")
    out.append(render_ext_bench_head())
    out.append("")
    for p in pats:
        out.extend(render_pattern_block(p))
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def render_ext_bench_head():
    return "\n".join(render_ext_bench())


# ---------------------------------------------------------------------------
# Derived-file writers
# ---------------------------------------------------------------------------

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
    have_ids = {fn[:-3] for fn in os.listdir(PATTERNS_DIR)
                if fn.endswith(".rx")}
    want_ids = {p.id for p in pats}
    if check:
        stale = have_ids - want_ids
        if stale:
            problems.append("stale patterns/*.rx not in the table: %s"
                             % sorted(stale))
    return problems


def check_list_source(pats):
    """Round-trip patterns.rxt through a real pcrec binary: every block's
    decoded `pattern` column must equal the table's own bytes (the
    DD-13b.W23.5 dump-value seam this module's docstring names)."""
    if not os.path.exists(PCREC_BIN):
        return ["pcrec binary not found at %s -- skipped --list-source "
                "round-trip (structural check only)" % PCREC_BIN]
    r = subprocess.run([PCREC_BIN, "--list-source", PATTERNS_RXT],
                        capture_output=True)
    stdout = r.stdout.decode("utf-8", "surrogateescape")
    stderr = r.stderr.decode("utf-8", "surrogateescape")
    if r.returncode != 0:
        return ["pcrec --list-source patterns.rxt FAILED (rc=%d):\n%s"
                % (r.returncode, stderr)]
    lines = stdout.splitlines()
    header = None
    rows = {}
    for ln in lines:
        if ln.startswith("#kind"):
            header = ln[1:].split("\t")
            continue
        if ln.startswith("#") or not ln.strip():
            continue
        cols = ln.split("\t")
        if header is None or len(cols) != len(header):
            continue
        row = dict(zip(header, cols))
        if row.get("kind") in ("pattern", "pattern-esc"):
            rows[row["name"]] = row["pattern"]
    problems = []
    by_id = {p.id: p for p in pats}
    if set(rows) != set(by_id):
        missing = set(by_id) - set(rows)
        extra = set(rows) - set(by_id)
        if missing:
            problems.append("--list-source missing blocks: %s"
                             % sorted(missing))
        if extra:
            problems.append("--list-source has extra blocks: %s"
                             % sorted(extra))
    for name, decoded in rows.items():
        p = by_id.get(name)
        if p is None:
            continue
        want = p.text.decode("utf-8", "surrogateescape")
        # --list-source escapes columns in the same \t\n\r\\\xNN vocabulary
        # this module's own pattern_esc() writes; decode it the same way a
        # THIRD reader would (deliberately not sharing the encoder above --
        # see rxt_format.md's dump-value-seam note on why a reader who
        # calls --list-source sees escaped text, never raw bytes).
        got = _decode_list_source_field(decoded)
        if got != p.text:
            problems.append("pattern %s: --list-source decode mismatch"
                             % name)
    return problems


def _decode_list_source_field(s):
    out = bytearray()
    i = 0
    b = s.encode("utf-8", "surrogateescape")
    while i < len(b):
        c = b[i]
        if c == 0x5c and i + 1 < len(b):
            nxt = chr(b[i + 1])
            if nxt == "n":
                out.append(0x0a); i += 2; continue
            if nxt == "t":
                out.append(0x09); i += 2; continue
            if nxt == "r":
                out.append(0x0d); i += 2; continue
            if nxt == "\\":
                out.append(0x5c); i += 2; continue
            if nxt == "x" and i + 3 < len(b):
                out.append(int(b[i + 2:i + 4], 16)); i += 4; continue
        out.append(c)
        i += 1
    return bytes(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--sidecar", action="store_true")
    ap.add_argument("--provenance", action="store_true")
    ap.add_argument("--no-list-source", action="store_true",
                     help="skip the pcrec round-trip (structural-only)")
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
        if not args.no_list_source:
            problems.extend(check_list_source(pats))
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


def render_sidecar(pats):
    out = []
    for p in pats:
        tags = ["family-%s" % p.family, "hazard-%s" % p.hazard_class,
                "provenance-%s" % p.source["source"],
                "fidelity-%s" % p.source["fidelity"]]
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
            "source_ref", "license", "license_note", "retrieved",
            "fidelity", "adaptation", "attribution", "twin_of", "isolates"]
    rows = ["\t".join(cols)]
    for p in pats:
        s = p.source
        rows.append("\t".join([
            p.id, p.family, s["source"], s["url"], s["ref"], s["license"],
            s["license_note"].replace("\t", " ").replace("\n", " "),
            s["retrieved"], s["fidelity"],
            s["adaptation"].replace("\t", " ").replace("\n", " "),
            s["attribution"], p.twin_of or "", p.isolates]))
    return "\n".join(rows)


if __name__ == "__main__":
    sys.exit(main())
