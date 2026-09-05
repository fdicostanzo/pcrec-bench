#!/usr/bin/env python3
"""gen_patterns.py -- `patterns/*.rx` and `coverage.tsv` for the syntax
census: the ninety-five patterns, TYPED here as a table, and the derivation of
which seed construct each one exercises.

    python3 bench/syntax/gen_patterns.py            # write both
    python3 bench/syntax/gen_patterns.py --check     # re-derive + diff both,
                                                     # and check the sidecar
    python3 bench/syntax/gen_patterns.py --sidecar   # print the [[patterns]]
                                                     # block the sidecar
                                                     # must carry

WHY THE PATTERNS ARE A TABLE HERE AND NOT LOOSE FILES. The census's claim is
COVERAGE -- that every construct pcrec's `--list-syntax` registry enumerates
(the SEED, `list_syntax_<pin>.tsv`, pcrec's file copied verbatim) is either
exercised by a pattern or left out FOR A STATED REASON -- and a claim like
that has to be derived, not asserted. So each pattern names the seed rows it
exercises (`constructs`, the seed's own `syntax` spellings), `coverage.tsv`
is derived from the table x the seed, and `--check` fails BY NAME on a seed
row nobody covers and nobody excuses. Re-seeding at a later pin (pcrec's rows
move: at abi 23 `\\x{...}` and utf8 moved to the base grammar) is therefore
`--seed <new file>` and reading the failures.

THE SEED IS USED TO ENUMERATE AND FOR NOTHING ELSE (requirements R-BENCH-4).
Only `kind`, `syntax`, `status` and `family` are read: `status` says whether
PCRE2 accepts the construct at all (`rejected` rows get no pattern -- the
oracle cannot state an expectation for them), `family` says which rows are
spellings of one construct (the seed's own column, so `(*pla:...)` is
`covered-by-family` when `(?=...)` is covered). The `built`, `module` and
`engines` columns are copied into coverage.tsv as the seed's OWN values at
its pin, labelled `seed_*`, for a reader of the first sample -- they shape
nothing here.

ONE CONSTRUCT IN AN OTHERWISE PLAIN BODY (inbox I-42, the D27 discipline).
Every body is drawn from censustext.py's vocabulary so a subject typed for
one pattern is a plain miss for the rest, and every construct's cost can be
read against a body another pattern spells WITHOUT it: `a++ab` against
`a+ab`, `(?>a+)b` against `a+b`, `(?i)cat` against `cat` (the group
patterns), `item\\ndone` against `item\\Rdone`, the five subroutine-call
spellings against each other. The author wrote these from the PCRE2
reference (`man pcre2pattern`) and the seed's construct list, blind to
pcrec's emitter and to this repo's adapters (NOTES.md, "Origin").

THE BASE GRAMMAR IS COVERED TOO. The seed enumerates escapes, group
openers, verbs, class brackets and possessive suffixes; it does NOT list
`.`, `[...]`, `|`, `*`, `+`, `?` or `{n,m}` because they are the base
grammar every row builds on. The census exercises them anyway (families
`classes`, `quantifiers`, `alternation`) with `constructs = ()` and a note
saying so, and `coverage.tsv`'s second block lists them.
"""
import argparse
import os
import sys
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "patterns")
COVERAGE = os.path.join(HERE, "coverage.tsv")
SIDECAR = os.path.join(HERE, "subbench.toml")
SEED = os.path.join(HERE, "list_syntax_334fd10e.tsv")

# The family slugs, in the order the sidecar lists them, and the tag each
# pattern carries (`fam-<slug>`). A family is a MECHANISM class, not a seed
# module: `anchors` holds `^` (a seed `bare` row), `\A` (module
# `assertions`) and `(?m)^` (module `modifiers`) because a reader ranking
# outliers wants "anchoring" in one place.
FAMILIES = ("literal", "anchors", "assertions", "classes", "quantifiers",
            "groups", "alternation", "backrefs", "lookaround", "conditionals",
            "recursion", "modifiers", "escapes", "misc", "uniprop", "verbs",
            "extclass", "floor")

# (id, family, constructs, text, note).
#   constructs: the seed rows' `syntax` spellings this pattern exercises, or
#               () for a base-grammar construct the seed does not list.
#   text:       the pattern, raw; written to patterns/<id>.rx without a
#               trailing newline. Every pattern is printable ASCII (Latin-1
#               bytes are spelled as escapes, never embedded).
PATTERNS = (
    # ---- the literal every `cat`-language spelling is read against
    ("lit-cat", "literal", (), r"cat",
     "base grammar: the three-byte literal. Fourteen patterns spell this "
     "language or a superset of it with one construct added (`(cat)`, "
     "`(?<w>cat)`, `\\x63at`, `(?x) c a t`, `ca(?#comment)t`, `(?n)(ca)t`, "
     "`c\\Xt`, ...); their cost minus this one's is the construct's"),

    # ---- anchors: where a match may start or end
    ("anc-caret", "anchors", ("^",), r"^item",
     "start of subject (no (?m)): the `bare` `^` row"),
    ("anc-dollar", "anchors", ("$",), r"done$",
     "end of subject OR before a final newline: `item done\\n` is the edge"),
    ("anc-A", "anchors", (r"\A",), r"\Aitem",
     "start of subject, the escape spelling"),
    ("anc-Z", "anchors", (r"\Z",), r"done\Z",
     "end of subject or before a final newline, like `$` outside (?m)"),
    ("anc-z", "anchors", (r"\z",), r"done\z",
     "end of subject ONLY: rejects `item done\\n` where `\\Z` and `$` take it"),
    ("anc-G", "anchors", (r"\G",), r"\Gitem",
     "the search start: find-all counts consecutive hits from the cursor"),
    ("anc-m-caret", "anchors", ("(?m)", "^"), r"(?m)^item",
     "`^` after an internal newline under multiline"),
    ("anc-m-dollar", "anchors", ("(?m)", "$"), r"(?m)done$",
     "`$` before an internal newline under multiline"),

    # ---- assertions: zero-width tests on the neighbourhood
    ("asr-wb", "assertions", (r"\b",), r"\bcat\b",
     "word boundary both sides: `concatenate` is the designed miss"),
    ("asr-nwb", "assertions", (r"\B",), r"\Bcat\B",
     "NOT a word boundary both sides: `cat` alone is the designed miss"),
    ("asr-K", "assertions", (r"\K",), r"key=\K\w+",
     "reset the reported start: the span begins after `key=`"),

    # ---- classes: one-character sets
    ("cls-d", "classes", (r"\d",), r"\d+", "a digit run"),
    ("cls-s", "classes", (r"\s",), r"cat\s+sat", "whitespace between two words"),
    ("cls-S", "classes", (r"\S",), r"\S+@\S+", "non-space runs around `@`"),
    ("cls-w", "classes", (r"\w",), r"\w+",
     "a word run; C-locale tables, so a Latin-1 byte ends it"),
    ("cls-h", "classes", (r"\h",), r"key\h*=\h*value",
     "horizontal whitespace (space, tab) around `=`"),
    ("cls-v", "classes", (r"\v",), r"item\v+done",
     "vertical whitespace: `\\n` one byte, `\\r\\n` two"),
    ("cls-N", "classes", (r"\N",), r"it\Nm",
     "any byte but newline, unaffected by (?s): `item` and `itxm`, never "
     "across a line end"),
    ("cls-posix", "classes", ("[[:alpha:]]",), r"[[:alpha:]]+",
     "a POSIX class: ASCII letters only under the default tables"),
    ("cls-negset", "classes", (), r"c[^aeiou]t",
     "base grammar: a negated bracket class (`cat` misses, `cxt` hits)"),
    ("cls-range", "classes", (), r"0x[0-9a-fA-F]+",
     "base grammar: a bracket class of three ranges"),
    ("cls-dot", "classes", (), r"c.t",
     "base grammar: `.` (any byte but newline without (?s))"),
    # ---- the FOLD-PAIR WITNESSES (manager's ask, 2026-09-05, from the
    # ---- [B39] prep lane: no other set carries a two-letter ASCII
    # ---- fold-pair class or `(?i)` on a class). Five patterns with
    # ---- `mod-i` (`(?i)cat`, the literal arm); the class arm here.
    ("cls-fold-pair", "classes", (), r"c[aA]t",
     "FOLD-PAIR WITNESS: a two-member class that IS an ASCII fold pair; "
     "the same language as `(?i:a)` in the middle of `cat`"),
    ("cls-pair-ctl", "classes", (), r"c[ac]t",
     "FOLD-PAIR WITNESS (the control): a two-member class that is NOT a "
     "fold pair -- the same class SIZE as `c[aA]t`, a different set"),
    ("cls-mixed-case", "classes", (), r"c[a-zA-Z]t",
     "FOLD-PAIR WITNESS: a mixed-case ranged class (52 members, every "
     "letter's fold pair present)"),
    ("cls-i-class", "classes", ("(?i)",), r"(?i)c[aeiou]t",
     "FOLD-PAIR WITNESS: `(?i)` over a CLASS (the option folds the class "
     "and the literals both); `mod-i` is the option over a literal"),

    # ---- quantifiers: greedy, lazy, possessive
    ("qnt-star", "quantifiers", (), r"ca*t",
     "base grammar: greedy star (`ct`, `cat`, `caaat`)"),
    ("qnt-plus", "quantifiers", (), r"a+b",
     "base grammar: greedy plus, the body the possessive/atomic shapes are "
     "read against"),
    ("qnt-quest", "quantifiers", (), r"colou?r", "base grammar: optional"),
    ("qnt-lazy", "quantifiers", (), r'".*?"',
     "base grammar: lazy star inside quotes (bench/bounded carries the "
     "counted forms)"),
    ("qnt-poss-star", "quantifiers", ("a*+",), r"a*+b", "possessive star"),
    ("qnt-poss-plus", "quantifiers", ("a++",), r"a++ab",
     "possessive plus with a body it can NEVER match (the plus keeps the "
     "last `a`): every subject is a miss, and `qnt-plus-ctl` is the control"),
    ("qnt-plus-ctl", "quantifiers", (), r"a+ab",
     "the CONTROL for `a++ab`: the same text minus the possessive suffix, "
     "which matches `aaab`"),
    ("qnt-poss-quest", "quantifiers", ("a?+",), r"a?+a",
     "possessive optional: needs two `a`s (the first is kept)"),
    ("qnt-poss-brace", "quantifiers", ("a{1,2}+",), r"a{1,2}+b",
     "possessive bounded repeat"),

    # ---- groups
    ("grp-cap", "groups", ("(a)",), r"(cat)",
     "a capturing group around the plain word (the `bare` row)"),
    ("grp-noncap", "groups", ("(?:...)",), r"(?:ab)+",
     "a non-capturing group under a repeat"),
    ("grp-named", "groups", ("(?<name>a)",), r"(?<w>cat)",
     "a named group, angle spelling; the other two spellings are exercised "
     "by the named backreference and the python-style call"),
    ("grp-named-quote", "groups", ("(?'name'...)",), r"(?'w'cat)",
     "a named group, quote spelling"),
    ("grp-atomic-rep", "groups", ("(?>...)",), r"(?>a+)b",
     "an atomic group over a repeat: same language as `a+b`"),
    ("grp-atomic-alt", "groups", ("(?>...)",), r"(?>a|ab)c",
     "an atomic group over an alternation: FAILS on `abc` (the first branch "
     "is committed) where `(?:a|ab)c` would match"),
    ("grp-comment", "groups", ("(?#...)",), r"ca(?#comment)t",
     "a comment group: the language is `cat`"),
    ("grp-branch-reset", "groups", ("(?|...)",), r"(?|(cat)|(dog))",
     "a branch-reset group: both alternatives capture as group 1"),
    ("grp-callout", "groups", ("(?C1)",), r"ca(?C1)t",
     "a numbered callout with no callout function installed: the language "
     "is `cat`"),

    # ---- alternation (base grammar)
    ("alt-two", "alternation", (), r"cat|dog",
     "base grammar: a two-branch literal alternation (bench/altwide carries "
     "the width ladder)"),
    ("alt-nested", "alternation", (), r"(?:c|d)(?:at|og)",
     "base grammar: two nested alternations, the same language as `cat|dog` "
     "plus `cog` and `dat`"),

    # ---- backreferences
    ("bak-1", "backrefs", (r"\1",), r"(\w+) \1",
     "a numbered backreference: a doubled word"),
    ("bak-2", "backrefs", (r"\2", r"\1"), r"(\w)(\w)\2\1",
     "two backreferences in reverse order: a four-byte palindrome"),
    ("bak-g-rel", "backrefs", (r"\g{-1}",), r"(\w+) \g{-1}",
     "a relative backreference: the same language as `bak-1`"),
    ("bak-k-named", "backrefs", (r"\k<name>", "(?<name>a)"),
     r"<(?<t>\w+)>[^<]*</\k<t>>",
     "a named backreference: a tag pair closed by its own name"),
    ("bak-py", "backrefs", ("(?P=n)", "(?P<name>a)"), r"(?P<t>\w+) (?P=t)",
     "the python-style named backreference: the same language as `bak-1`"),

    # ---- lookaround
    ("lka-pos", "lookaround", ("(?=...)",), r"item(?= done)",
     "positive lookahead: the span is `item`"),
    ("lka-neg", "lookaround", ("(?!...)",), r"item(?! done)",
     "negative lookahead"),
    ("lkb-pos", "lookaround", ("(?<=...)",), r"(?<=item )done",
     "positive lookbehind: the span is `done`"),
    ("lkb-neg", "lookaround", ("(?<!...)",), r"(?<!item )done",
     "negative lookbehind"),
    ("lka-nonatomic", "lookaround", ("(?*a)",), r"(?*item)item",
     "non-atomic positive lookahead over a literal: the same language as "
     "`item`"),
    ("lka-verb", "lookaround", ("(*pla:a)",), r"item(*pla: done)",
     "the alpha spelling of `lka-pos`: the same language, a different "
     "spelling"),

    # ---- conditionals
    ("cnd-group", "conditionals", ("(?(1)a|b)",), r"(<)?item(?(1)>)",
     "a group-number condition: `<item>` or `item`, never `<item`"),

    # ---- recursion and subroutine calls
    ("rec-R", "recursion", ("(?R)",), r"\((?:[^()]|(?R))*\)",
     "whole-pattern recursion: balanced parentheses"),
    ("rec-1", "recursion", ("(?1)",), r"(\((?:[^()]|(?1))*\))",
     "recursion into group 1: the same language as `rec-R`, the call "
     "target being the group and not the root"),
    ("rec-name", "recursion", ("(?&name)", "(?<name>a)"),
     r"(?<p>\((?:[^()]|(?&p))*\))",
     "recursion into a named group: the same language as `rec-R`"),
    ("rec-define", "recursion", ("(?(DEFINE)(?<w>a))", "(?&name)"),
     r"(?(DEFINE)(?<d>\d{2}))(?&d):(?&d)",
     "a DEFINE group called twice: `12:34`"),
    ("rec-g-angle", "recursion", (r"\g<1>",), r"(\d{2})\g<1>",
     "a subroutine call by number, angle spelling: four digits"),
    ("rec-py", "recursion", ("(?P>n)", "(?P<name>a)"), r"(?P<d>\d{2})(?P>d)",
     "the python-style subroutine call: the same language as `rec-g-angle`"),
    ("rec-fwd", "recursion", ("(?+1)(a)",), r"(?+1)(\d{2})",
     "a relative call FORWARD to the group to its right: four digits"),
    ("rec-back", "recursion", ("(a)(?-1)",), r"(\d{2})(?-1)",
     "a relative call BACK to the group to its left: four digits"),

    # ---- modifiers (option settings)
    ("mod-i", "modifiers", ("(?i)",), r"(?i)cat", "caseless"),
    ("mod-s", "modifiers", ("(?s)",), r"(?s)item.done",
     "dotall: the `.` spans the newline in `item\\ndone`; NO unbounded "
     "repeat under (?s) anywhere in this set"),
    ("mod-x", "modifiers", ("(?x)",), r"(?x) c a t # comment",
     "extended: the language is `cat`"),
    ("mod-n", "modifiers", ("(?n)",), r"(?n)(ca)t",
     "no auto-capture: the plain group stops capturing"),
    ("mod-U", "modifiers", ("(?U)",), r'(?U)".+"',
     "ungreedy: the same language as `qnt-lazy` by inverting `+`"),
    ("mod-J", "modifiers", ("(?J)", "(?<name>a)", r"\k<name>"),
     r"(?J)(?:(?<w>the)|(?<w>\w+)) \k<w>",
     "duplicate names allowed: the backreference resolves to whichever "
     "`w` set"),
    ("mod-a", "modifiers", ("(?a)",), r"(?a)\w+",
     "ASCII-restricted class escapes: under the default tables `\\w` is "
     "already ASCII, so the same language as `cls-w`"),
    ("mod-r", "modifiers", ("(?r)", "(?i)"), r"(?ir)cat",
     "caseless restricted to one script: in byte mode the same language "
     "as `mod-i`"),
    ("mod-reset", "modifiers", ("(?^)", "(?i)"), r"(?i)c(?^)at",
     "reset all options mid-pattern: `Cat` yes, `CAT` no"),
    ("mod-unset", "modifiers", ("(?-i)", "(?i)"), r"(?i)c(?-i)at",
     "unset one option mid-pattern: the same language as `mod-reset`"),

    # ---- escapes: single-byte spellings and quoting
    ("esc-tab", "escapes", (r"\t",), r"key\tvalue", "the tab escape"),
    ("esc-nl", "escapes", (r"\n",), r"item\ndone", "the newline escape"),
    ("esc-cr", "escapes", (r"\r", r"\n"), r"item\r\ndone",
     "carriage return + newline as two escapes: `msc-R` is the one-token "
     "spelling of the same pair"),
    ("esc-hex", "escapes", (r"\x41",), r"\x63at",
     "a bare two-digit hex escape: the language is `cat`"),
    ("esc-hex-braced", "escapes", (r"\x41",), r"caf\x{e9}",
     "the braced hex spelling of a Latin-1 byte (the seed's `\\x41` row "
     "names both spellings)"),
    ("esc-ctrl", "escapes", (r"\cX",), r"bell\cGend",
     "a control escape: `\\cG` is 0x07"),
    ("esc-octal-o", "escapes", (r"\o{101}",), r"\o{143}at",
     "the braced octal escape: the language is `cat`"),
    ("esc-octal-0", "escapes", (r"\0",), r"item\040done",
     "the `\\0dd` octal escape (never a backreference): a space"),
    ("esc-quote", "escapes", (r"\Q", r"\E"), r"\Qf(x)\E",
     "literal quoting: the parentheses are bytes"),

    # ---- misc escapes
    ("msc-R", "misc", (r"\R",), r"item\Rdone",
     "any newline sequence: `\\n` and `\\r\\n` both, as one token"),
    ("msc-X", "misc", (r"\X",), r"c\Xt",
     "an extended grapheme cluster: one byte in byte mode"),
    ("msc-C", "misc", (r"\C",), r"c\Ct", "one data unit"),

    # ---- unicode properties, in byte mode
    ("unp-p", "uniprop", (r"\p{L}",), r"\p{L}+",
     "letters by Unicode property: Latin-1 letters included, unlike `\\w`"),
    ("unp-P", "uniprop", (r"\P{L}",), r"\P{L}+", "non-letter runs"),

    # ---- backtracking verbs
    ("vrb-accept", "verbs", ("(*ACCEPT)",), r"item(*ACCEPT)done",
     "end the match early: the span is `item`, `done` never runs"),
    ("vrb-skip", "verbs", ("(*ACCEPT)",), r"a+(*SKIP)b",
     "on failure after the verb, skip the search to the verb's position"),

    # ---- extended character classes
    ("xcl-minus", "extclass", ("(?[[a]])",), r"(?[[a-z]-[aeiou]])+",
     "a set difference: consonant runs"),

    # ---- the floor
    ("floor", "floor", (), r"#",
     "requirements 5's per-call control: one literal byte, in `#42` and "
     "the order line only, absent from every run"),
)

# Seed rows that get NO pattern, each with its reason. A row that is
# `rejected` by PCRE2, or a spelling of a covered family (the seed's own
# `family` column), needs no entry here; everything else must have one or
# `--check` fails by name.
NOT_EXERCISED = {
    r"\D": "the complement of `\\d`: the same class mechanism, set inverted",
    r"\W": "the complement of `\\w`: the same class mechanism, set inverted",
    r"\H": "the complement of `\\h`: the same class mechanism, set inverted",
    r"\V": "the complement of `\\v`: the same class mechanism, set inverted",
    r"\N{U+0041}": "UTF-only in PCRE2 (error 193 in byte mode): the utf "
                   "family's, not this set's (NOTES.md, `Room for a utf "
                   "family`)",
    r"\3": "a numbered backreference at a higher index: `\\1` and `\\2` "
           "witness that the index is read",
    r"\4": "as \\3", r"\5": "as \\3", r"\6": "as \\3", r"\7": "as \\3",
    r"\8": "as \\3 (and never octal: a parse fact, not a matcher one)",
    r"\9": "as \\8",
    r"\g'1'": "the quoted spelling of `\\g<1>`: one pattern per call "
              "spelling family, and the angle spelling is the witness",
    r"\a": "a fixed-byte escape: `\\t`, `\\n`, `\\r` and `\\cG` witness the "
           "mechanism",
    r"\e": "as \\a", r"\f": "as \\a",
    "(?0)": "the numbered spelling of `(?R)`: the same call target (the "
            "root); `(?1)` witnesses the numbered call",
    "(?)": "the empty option setting: a no-op spelling; `(?^)` and `(?-i)` "
           "witness the option-setting mechanism",
    "(?<*a)": "non-atomic positive LOOKBEHIND: `(?*a)` witnesses the "
              "non-atomic mechanism on the lookahead side",
}

# The five FOLD-PAIR WITNESSES carry one more tag (`fold-pair-witness`):
# the shapes pcrec's abi-23 [FORM-CHAR] STEP 1 turns into a masked compare,
# absent from every other set (manager, 2026-09-05). Plain PCRE, oracled
# like the rest; the tag is how a report finds the five.
FOLD_WITNESSES = ("mod-i", "cls-i-class", "cls-fold-pair", "cls-pair-ctl",
                  "cls-mixed-case")

# The tags every pattern carries beside its family tag. `encoding-bytes` is
# the ROOM for a utf family (NOTES.md): a sibling set's patterns would carry
# `encoding-utf8`, and a report can bucket on the pair.
COMMON_TAGS = ("encoding-bytes",)


# ----------------------------------------------------------------- the seed

def read_seed(path):
    """-> (columns, rows) with rows as dicts keyed by the `#kind` header."""
    cols, rows = None, []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            if line.startswith("#kind\t"):
                cols = line[1:].split("\t")
                continue
            if line.startswith("#"):
                continue
            if cols is None:
                raise SystemExit("%s: a data row before the #kind header" % path)
            vals = line.split("\t")
            if len(vals) != len(cols):
                raise SystemExit("%s: %d columns, header has %d: %r"
                                 % (path, len(vals), len(cols), line[:60]))
            rows.append(dict(zip(cols, vals)))
    if cols is None:
        raise SystemExit("%s: no #kind header line" % path)
    for need in ("kind", "syntax", "status", "family"):
        if need not in cols:
            raise SystemExit("%s: no %r column" % (path, need))
    return cols, rows


def row_key(row):
    return row["family"] or row["syntax"]


# ----------------------------------------------------------- the derivation

def derive_patterns():
    """-> [(filename, bytes)] in table order."""
    seen = set()
    out = []
    for pid, fam, _cs, text, _note in PATTERNS:
        if pid in seen:
            raise SystemExit("duplicate pattern id %r" % pid)
        seen.add(pid)
        if fam not in FAMILIES:
            raise SystemExit("%s: unknown family %r" % (pid, fam))
        body = text.encode("ascii")   # every pattern is printable ASCII
        out.append((pid + ".rx", body))
    return out


def derive_coverage(seed_path):
    """-> (text, problems). One row per seed row, then the base-grammar
    block; `problems` lists what --check must fail on."""
    cols, rows = read_seed(seed_path)
    by_syntax = {}
    for pid, _fam, cs, _t, _n in PATTERNS:
        for c in cs:
            by_syntax.setdefault(c, []).append(pid)
    seed_syntaxes = {r["syntax"] for r in rows}
    problems = []
    for c in by_syntax:
        if c not in seed_syntaxes:
            problems.append("pattern(s) %s name construct %r, which is not a "
                            "`syntax` in the seed" % (by_syntax[c], c))
    covered_keys = {}
    for r in rows:
        if r["syntax"] in by_syntax:
            covered_keys.setdefault(row_key(r), []).extend(by_syntax[r["syntax"]])

    extra = [c for c in ("module", "engines", "built") if c in cols]
    header = ["kind", "syntax", "key", "seed_status"] + ["seed_" + c for c in extra] \
        + ["coverage", "patterns", "reason"]
    lines = ["\t".join(header)]
    counts = {}
    for r in rows:
        syn, st = r["syntax"], r["status"]
        if syn in by_syntax:
            cov, pats, why = "covered", " ".join(by_syntax[syn]), ""
        elif st == "rejected":
            cov, pats, why = "pcre2-rejects", "-", (
                "PCRE2 refuses this construct (the seed's `expect`: %s); the "
                "oracle can state no expectation" % r.get("expect", ""))
        elif row_key(r) in covered_keys:
            cov, pats = "covered-by-family", " ".join(covered_keys[row_key(r)])
            why = "a spelling of `%s` (the seed's `family` column)" % row_key(r)
        elif syn in NOT_EXERCISED:
            cov, pats, why = "not-exercised", "-", NOT_EXERCISED[syn]
        elif row_key(r) in NOT_EXERCISED:
            cov, pats = "not-exercised-by-family", "-"
            why = ("a spelling of `%s`, which is not exercised: %s"
                   % (row_key(r), NOT_EXERCISED[row_key(r)]))
        else:
            cov, pats, why = "UNCOVERED", "-", "no pattern and no stated reason"
            problems.append("seed row %s %r (status %s) is covered by no "
                            "pattern and excused by no reason" % (r["kind"], syn, st))
        counts[cov] = counts.get(cov, 0) + 1
        lines.append("\t".join([r["kind"], syn, row_key(r), st]
                               + [r[c] for c in extra] + [cov, pats, why]))
    unused = sorted(set(NOT_EXERCISED) - seed_syntaxes)
    for u in unused:
        problems.append("NOT_EXERCISED names %r, which is not in the seed" % u)

    lines.append("")
    lines.append("#base-grammar constructs with no seed row, exercised by these "
                 "patterns (constructs = ())")
    lines.append("pattern\tfamily\ttext\tnote")
    for pid, fam, cs, text, note in PATTERNS:
        if not cs:
            lines.append("\t".join([pid, fam, text, note]))
    summary = ", ".join("%s %d" % (k, counts[k]) for k in sorted(counts))
    lines.insert(0, "#coverage of the seed %s by bench/syntax's %d patterns: %s"
                 % (os.path.basename(seed_path), len(PATTERNS), summary))
    return "\n".join(lines) + "\n", problems


# ------------------------------------------------------------- the sidecar

def sidecar_block():
    """The [[patterns]] entries the sidecar must carry, derived from the
    table so the two cannot drift: `--check` compares them."""
    out = []
    for pid, fam, cs, text, note in PATTERNS:
        size = "tiny" if len(text) < 16 else "small"
        tags = ["fam-" + fam] + list(COMMON_TAGS)
        if cs:
            tags.append("seed-row")
        else:
            tags.append("base-grammar")
        if pid in FOLD_WITNESSES:
            tags.append("fold-pair-witness")
        out.append(
            "[[patterns]]\n"
            "# %s\n"
            "name = \"%s\"\n"
            "file = \"patterns/%s.rx\"\n"
            "feature_tier = \"base\"\n"
            "hazard_class = \"none\"\n"
            "size_class = \"%s\"\n"
            "convention = \"perl-leftmost-first\"\n"
            "tags = [%s]\n"
            "role = \"%s\"\n"
            % (note.replace("\n", " "), pid, pid, size,
               ", ".join("\"%s\"" % t for t in tags),
               "floor" if fam == "floor" else "member"))
    return "\n".join(out)


def check_sidecar():
    """The sidecar's [[patterns]] must be the table's, entry for entry."""
    with open(SIDECAR, "rb") as f:
        cfg = tomllib.load(f)
    have = cfg.get("patterns", [])
    problems = []
    if [p.get("name") for p in have] != [p[0] for p in PATTERNS]:
        problems.append("the sidecar lists %d pattern(s) in an order that is "
                        "not the table's %d" % (len(have), len(PATTERNS)))
        return problems
    for entry, (pid, fam, cs, text, _note) in zip(have, PATTERNS):
        want_role = "floor" if fam == "floor" else "member"
        want_size = "tiny" if len(text) < 16 else "small"
        want_tags = {"fam-" + fam, *COMMON_TAGS,
                     "seed-row" if cs else "base-grammar"}
        if pid in FOLD_WITNESSES:
            want_tags.add("fold-pair-witness")
        if entry.get("file") != "patterns/%s.rx" % pid:
            problems.append("%s: file %r" % (pid, entry.get("file")))
        if entry.get("role", "member") != want_role:
            problems.append("%s: role %r, want %r" % (pid, entry.get("role"), want_role))
        if entry.get("size_class") != want_size:
            problems.append("%s: size_class %r, want %r"
                            % (pid, entry.get("size_class"), want_size))
        if entry.get("hazard_class") != "none":
            problems.append("%s: hazard_class %r" % (pid, entry.get("hazard_class")))
        if not want_tags <= set(entry.get("tags", [])):
            problems.append("%s: tags %r lack %r"
                            % (pid, entry.get("tags"), sorted(want_tags)))
    return problems


# ------------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--coverage", default=COVERAGE)
    ap.add_argument("--seed", default=SEED,
                    help="the registry seed to derive coverage from")
    ap.add_argument("--check", action="store_true",
                    help="re-derive and DIFF against the committed files, "
                         "and check the sidecar (the `make check` mode)")
    ap.add_argument("--sidecar", action="store_true",
                    help="print the [[patterns]] block the sidecar must carry")
    args = ap.parse_args(argv)

    if args.sidecar:
        print(sidecar_block())
        return 0

    files = derive_patterns()
    cov, problems = derive_coverage(args.seed)
    for p in problems:
        print("gen_patterns: %s" % p, file=sys.stderr)
    if problems:
        return 1

    if args.check:
        have = sorted(f for f in os.listdir(args.out) if f.endswith(".rx"))
        want = sorted(fn for fn, _b in files)
        if have != want:
            print("gen_patterns --check: %s holds %d file(s), the table derives "
                  "%d: extra %s, missing %s"
                  % (args.out, len(have), len(want),
                     sorted(set(have) - set(want)), sorted(set(want) - set(have))),
                  file=sys.stderr)
            return 1
        for fn, body in files:
            with open(os.path.join(args.out, fn), "rb") as f:
                got = f.read()
            if got != body:
                print("gen_patterns --check: %s does NOT re-derive (committed "
                      "%r, derived %r)" % (fn, got[:40], body[:40]),
                      file=sys.stderr)
                return 1
        if not os.path.exists(args.coverage):
            print("gen_patterns --check: %s does not exist" % args.coverage,
                  file=sys.stderr)
            return 1
        with open(args.coverage, "r", encoding="utf-8") as f:
            have_cov = f.read()
        if have_cov != cov:
            print("gen_patterns --check: %s does NOT re-derive from %s"
                  % (args.coverage, os.path.basename(args.seed)), file=sys.stderr)
            hl, tl = have_cov.splitlines(), cov.splitlines()
            for i in range(max(len(hl), len(tl))):
                a = hl[i] if i < len(hl) else "<absent>"
                b = tl[i] if i < len(tl) else "<absent>"
                if a != b:
                    print("  line %d committed: %s" % (i + 1, a), file=sys.stderr)
                    print("  line %d derived  : %s" % (i + 1, b), file=sys.stderr)
                    break
            return 1
        sp = check_sidecar()
        for p in sp:
            print("gen_patterns --check: sidecar: %s" % p, file=sys.stderr)
        if sp:
            return 1
        print("gen_patterns --check: %d pattern file(s) re-derive, coverage.tsv "
              "re-derives from %s (%s), the sidecar agrees with the table"
              % (len(files), os.path.basename(args.seed), cov.splitlines()[0][1:]))
        return 0

    os.makedirs(args.out, exist_ok=True)
    for fn, body in files:
        with open(os.path.join(args.out, fn), "wb") as f:
            f.write(body)
    with open(args.coverage, "w", encoding="utf-8", newline="\n") as f:
        f.write(cov)
    print("gen_patterns: %d pattern(s) -> %s; coverage -> %s (%s)"
          % (len(files), args.out, args.coverage, cov.splitlines()[0][1:]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
