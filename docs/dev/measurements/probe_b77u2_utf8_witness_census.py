#!/usr/bin/env python3
"""docs/dev/measurements/probe_b77u2_utf8_witness_census.py -- the
reproducing script behind 2026-09-25-b77u2-utf8-witness-census.txt.

Lane b77u2 ([B77] U2, docs/design/utf8_set_v1.md 7 + 13's U2 row + 15's
R2): the WITNESS COMPILE per (config, REQUIRES token) that must exist
BEFORE any UTF-8 config's capability declaration ships -- the L5 lesson
(bench/capability's first cut shipped three wrong pcrec-* declarations
that a witness compile would have caught; docs/dev/lanes/b42cap_report.md
2). Everything goes through the REAL adapters (`Adapter.compile()` then
`Adapter.measure()`), never a second parser, and every expected answer is
DERIVED from the libpcre2 oracle under the utf8 set's own option word
(PCRE2_UTF, plus PCRE2_UCP where the pattern spells `(*UCP)`) -- never
hand-typed.

FIVE SECTIONS:

  A. THE THREE NEW TOKENS (utf8_set_v1.md 7.5) on every config the utf8
     set's roster can hold: the ten new UTF-8 configs, the two unchanged
     ones (`rust-default`, `tre-default`), and every BYTE config as the
     control the `utf8-encoding` token is defined against ("unsatisfied by
     every BYTE-mode config"). A token is SATISFIED iff every one of its
     witnesses compiles AND answers as the oracle does on every subject
     (match/nomatch, and the span where the engine reports one); a
     compile refusal or a wrong answer is NOT, with the witness named.
     `unicode-class-scope` is witnessed in the SET'S OWN SPELLING,
     `(*UCP)` (utf8_set_v1.md 5(a)/(c)/(e)); an informational row beside
     it reads each engine's NATIVE `\\w` scope, so "widens natively but
     cannot parse the set's spelling" is visible rather than conflated.
  B. unicode-properties, RE-CENSUSED on every UTF-8 config (onig-default
     withholds it BECAUSE of its ASCII encoding, testees/onig/CLAUDE.md;
     7.1 names the re-census) -- general categories.
  C. THE SCRIPT / SCRIPT_EXTENSIONS SPELLINGS (7.4's UNCONFIRMED row, 15
     R2): every spelling family (f) uses or might, on every UTF-8 config,
     over `α` and U+0342 COMBINING GREEK PERISPOMENI (Script=Inherited,
     Script_Extensions={Greek}) -- so a bare `\\p{Greek}` that reads
     Script_Extensions answers `match` on U+0342 and one that reads Script
     answers `nomatch`: the SEMANTICS, not only the parse.
  D. THE OTHER FOURTEEN compile-witness tokens (the pre-[B77] vocabulary
     minus the three execution-model facts), on the ten new configs: a
     byte sibling's declaration carries over to its UTF-8 sibling ONLY if
     the same witness also compiles under UTF-8 -- the declaration is the
     sibling's AND this pin's compile, never inherited unwitnessed.
  E. THE THREE EXECUTION-MODEL tokens (span-reporting, captures,
     non-utf8-subject) on the ten new configs, by MATCH witnesses: `(a)(b)`
     over `xab` (a span and two capture spans), and `a` over the INVALID
     UTF-8 subject `\\xffa\\xff` (a byte engine answers [1,2); a UTF-8
     engine may refuse the subject, which is exactly what
     `non-utf8-subject` names).

  F. THE SET'S OWN SPELLINGS (informational): `\\x{...}`, the four
     lookbehind members, multiline `^`/`$`, `\\A...\\z`, `\\B`, counted
     repeats of 4-byte and `.` units -- per-pattern refusals U4/U5 should
     know before the first window, NOT capability verdicts.

TWO RULES the verdicts follow, both stated where they are applied:
  * a pcrec SIZE refusal ("pattern too large", the emitted-size cap) is
    NOT a missing capability -- it is R4/P7's finding and must reach the
    set as a first-class did-not-compile row (onig's `recursion`
    precedent), so it does not unset the token;
  * `non-utf8-subject` is NOT, BY RULE, on every UTF-8 config: the
    subject contract is valid UTF-8 (PCRE2 refuses invalid input;
    Vectorscan/Oniguruma document it as undefined), whatever one witness
    happens to answer.

Then THE DECLARATIONS: one row per (new or unchanged config, token), the
verdict and the witness it rests on -- what bench/utf8's `ext bench`
matrix (lane U4) transcribes.

Run: python3 docs/dev/measurements/probe_b77u2_utf8_witness_census.py
(from the repo root; builds every driver it needs into a temp dir; the
pcrec rows need the pin's binary, `testees/pcrec/pin.sh`). Compile-only
plus one smoke match per subject: no timing is read, no quiet box needed.
"""
import importlib.util
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)

from pcrecbench import adapters as ad            # noqa: E402
from pcrecbench import oracle_pcre2 as oracle    # noqa: E402
from pcrecbench.capability import REQUIRES_VOCAB  # noqa: E402

NEW = ["pcre2-utf-interp", "pcre2-utf-jit", "pcre2-utf-dfa",
       "pcrec-auto-utf8", "pcrec-nocaps-utf8", "pcrec-vm-utf8",
       "pcrec-vm-in-utf8", "re2-utf8", "onig-utf8",
       "vectorscan-block-nosom-utf8"]
UNCHANGED = ["rust-default", "tre-default"]
BYTE = ["pcre2-interp", "pcre2-jit", "pcre2-dfa", "pcrec-auto",
        "pcrec-nocaps", "pcrec-vm", "pcrec-vm-in", "re2-default",
        "re2-longest", "onig-default", "vectorscan-block-nosom"]
SIBLING = {"pcre2-utf-interp": "pcre2-interp", "pcre2-utf-jit": "pcre2-jit",
           "pcre2-utf-dfa": "pcre2-dfa", "pcrec-auto-utf8": "pcrec-auto",
           "pcrec-nocaps-utf8": "pcrec-nocaps", "pcrec-vm-utf8": "pcrec-vm",
           "pcrec-vm-in-utf8": "pcrec-vm-in", "re2-utf8": "re2-default",
           "onig-utf8": "onig-default",
           "vectorscan-block-nosom-utf8": "vectorscan-block-nosom"}

U = lambda s: s.encode("utf-8")   # noqa: E731

# (label, pattern, [subjects]) -- expectations come from the oracle.
NEW_TOKEN_WITNESSES = {
    "utf8-encoding": [
        ("dot-is-one-char", r"^.$", ["é", "ab"]),
        ("negated-class-universe", r"[^é]", ["ü", "é"]),
        ("caseless-non-ascii", r"(?i)é", ["É", "e"]),
        ("multibyte-range", r"[α-ω]+", ["xαβγ", "abc"]),
    ],
    "ascii-class-scope": [
        ("w-ascii", r"\w+", ["Москва", "abc"]),
        ("d-ascii", r"\d{4}", ["٠١٢٣", "2026"]),
        ("s-ascii", r"a\sb", ["a b", "a b"]),
        ("posix-alpha-ascii", r"[[:alpha:]]+", ["é", "abc"]),
    ],
    "unicode-class-scope": [
        ("w-ucp", r"(*UCP)\w+", ["Москва", "--"]),
        ("d-ucp", r"(*UCP)\d{4}", ["٠١٢٣", "abcd"]),
        ("s-ucp", r"(*UCP)a\sb", ["a b", "ab"]),
    ],
}
# informational: each engine's NATIVE \w scope, no (*UCP) spelling; and
# the set's own `asr-b-cyr-ucp` shape, because utf8_set_v1.md 7.6 records
# that Vectorscan's UCP BREAKS `\b` (a flag-level A/B on bench/capability)
NATIVE_SCOPE = [("native-w", r"\w+", ["Москва"]),
                ("b-ucp", r"(*UCP)\bМосква\b", ["в Москва.", "Москвах"])]

# informational: the SET'S OWN spellings that are neither a token witness
# nor a property (families (a)/(e) of utf8_set_v1.md 5), so U4 can tag
# and U5 can predict the per-pattern refusals before the first window
SET_SPELLINGS = [
    ("x-brace-range", r"[\x{100}-\x{2000}]+", ["āĀ", "abc"]),
    ("lb-fixed-2byte", r"(?<=é)x", ["éx", "ex"]),
    ("lb-varbyte-samechar", r"(?<=a|é)x", ["éx", "ax", "bx"]),
    ("lb-neg-3byte", r"(?<!日)本", ["日本", "本"]),
    ("lb-class", r"(?<=[\x{400}-\x{4FF}])\s", ["ж ", "a "]),
    ("caret-ml", r"(?m)^日", ["a\n日", "a日"]),
    ("dollar-ml", r"(?m)語$", ["語\nb", "語b"]),
    ("A-z", r"\A日本語\z", ["日本語", "日本語x"]),
    ("B-midchar", r"\B", ["é"]),
    ("emoji-bounded", r"😀{2,4}", ["😀😀", "😀"]),
    ("dot-bounded", r".{3,8}", ["日本語", "ab"]),
]

SIZE_REFUSAL = "pattern too large"   # pcrec's emitted-size cap wording

PROPS_WITNESSES = [
    ("L", r"\p{L}", ["é", "1"]),
    ("Lu", r"\p{Lu}", ["É", "é"]),
    ("N-plus", r"\p{N}+", ["٣", "x"]),
    ("notL-plus", r"\P{L}+", ["1", "é"]),
    ("Zs", r"\p{Zs}", ["　", "x"]),
]

GREEK_SUBJ = ["α", "͂", "a"]
SCRIPT_WITNESSES = [
    ("Greek", r"\p{Greek}", GREEK_SUBJ),
    ("sc=Greek", r"\p{sc=Greek}", GREEK_SUBJ),
    ("Script=Greek", r"\p{Script=Greek}", GREEK_SUBJ),
    ("scx=Greek", r"\p{scx=Greek}", GREEK_SUBJ),
    ("Script_Extensions=Greek", r"\p{Script_Extensions=Greek}", GREEK_SUBJ),
    ("Cyrillic", r"\p{Cyrillic}+", ["Москва", "abc"]),
    ("Han", r"\p{Han}+", ["日本", "abc"]),
    ("Latin", r"\p{Latin}+", ["café", "日本"]),
    ("InGreek", r"\p{InGreek}", ["α"]),
]

OLD_TOKEN_WITNESSES = {
    "backrefs": [r"(a)\1"],
    "lookaround": [r"(?=a)a", r"(?<=a)b"],
    "lookbehind-variable": [r"(?<=a|bc)x"],
    "possessive-quantifier": [r"a*+"],
    "atomic-group": [r"(?>a*)b"],
    "recursion": [r"(a(?1)?b)"],
    "conditionals": [r"(?(1)a|b)(a)?"],
    "k-reset": [r"a\Kb"],
    "control-verbs": [r"a(*FAIL)|b"],
    "named-groups": [r"(?<name>a)"],
    "free-spacing": ["(?x) a b c"],
    "callouts": [r"a(?C1)b"],
    "true-end-anchor": [r"a\z"],
}


class Subj:
    def __init__(self, i, path, n):
        self.subject_id, self.path, self.length = "s-%d" % i, path, n


def oracle_answer(pat, subj):
    """-> (answer, start, end) under the utf8 set's own word: PCRE2_UTF;
    PCRE2_UCP arrives inline from the pattern's own `(*UCP)` spelling,
    exactly as it would for the set (utf8_set_v1.md 8.1)."""
    try:
        rx = oracle.compile(U(pat), oracle.option_word(utf=True))
    except oracle.Pcre2Error as e:
        return ("refused", str(e)[:60], None)
    m = rx.search(subj)
    if m is None:
        return ("nomatch", None, None)
    return ("match", m[0][0], m[0][1])


def run_one(adapters, tid, tmp, label, pat, subjects):
    """-> (outcome, diagnostic, rows): rows = [(answer, start, end, caps)]
    per subject (bytes), measured on the PLAIN artifact in `search_short`."""
    a = adapters[tid]
    pid = ("%s-%s" % (tid, label)).replace("=", "-").replace("_", "-")[:60]
    try:
        cp = a.compile(tid, pid, U(pat), {}, 1, tmp)
    except Exception as e:                                  # noqa: BLE001
        return "adapter-error", str(e)[:160], []
    cr = cp.get(ad.FORM_PLAIN)
    if cr.outcome != "compiled":
        return cr.outcome, (cr.diagnostic or "")[:160], []
    if not subjects:
        return "compiled", "", []
    subj = []
    for i, s in enumerate(subjects):
        p = os.path.join(tmp, "%s-s%d.bin" % (pid, i))
        with open(p, "wb") as f:
            f.write(s)
        subj.append(Subj(i, p, len(s)))
    h = dict(cr.handle)
    h["utf8_advance"] = True      # the utf8 set's handle (U1), inert here
    try:
        got, _i, _n = a.measure(h, "search_short", subj, 1, 1, timeout=120)
    except Exception as e:                                  # noqa: BLE001
        return "measure-error", str(e)[:160], []
    rows = [(r.answer, r.start, r.end, r.caps) for r in (got[0] if got else [])]
    return "compiled", "", rows


def judge(rows, subjects, pat):
    """-> (ok, text): every row agrees with the oracle (answer, and the
    span where the engine reports one -- a boolean-grain engine reports
    none, `-`)."""
    parts, ok = [], True
    for (ans, st, en, _c), s in zip(rows, subjects):
        exp = oracle_answer(pat, s)
        span = "" if st in (None, "-") else "[%s,%s)" % (st, en)
        good = ans == exp[0] and (span == "" or ans != "match"
                                  or (int(st), int(en)) == (exp[1], exp[2]))
        ok = ok and good
        parts.append("%s%s%s" % (ans, span, "" if good else
                                 "!=oracle(%s%s)" % (exp[0], "" if exp[1] is None
                                                     else "[%d,%d)" % (exp[1], exp[2]))))
    if len(rows) != len(subjects):
        ok = False
        parts.append("rows %d != subjects %d" % (len(rows), len(subjects)))
    return ok, " ".join(parts)


def main():
    adapters = {}
    for eng in ad.discover(root=os.path.join(ROOT, "testees")).values():
        for tid in eng.testees():
            adapters[tid] = eng
    tmp = tempfile.mkdtemp(prefix="b77u2-census-", dir=os.environ.get(
        "B77U2_TMP") or None)
    for tid in NEW + UNCHANGED + BYTE:
        adapters[tid].prepare(tid, tmp)

    spec = importlib.util.spec_from_file_location(
        "cap_gen", os.path.join(ROOT, "bench", "capability", "gen_patterns.py"))
    cap = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cap)
    sibling_decl = {t: set(c) for t, c in cap.EXT_BENCH_ROSTER}

    verdict = {}          # (tid, token) -> (bool, evidence)

    print("pcrec pin: %s" % adapters["pcrec-auto"].pin())
    print("oracle: libpcre2 %s, option word PCRE2_UTF (+ inline (*UCP))"
          % oracle.version())
    print()
    print("=== A. the three new tokens (utf8_set_v1.md 7.5) ===")
    print("config\ttoken\twitness\tpattern\toutcome\tanswers (vs the UTF oracle)")
    for tid in NEW + UNCHANGED + BYTE:
        for token, wits in NEW_TOKEN_WITNESSES.items():
            tok_ok, ev = True, []
            for label, pat, subs in wits:
                subjects = [U(s) for s in subs]
                out, diag, rows = run_one(adapters, tid, tmp, label, pat, subjects)
                if out != "compiled":
                    tok_ok = False
                    line = "%s: %s" % (out, diag.replace("\t", " ").replace("\n", " | "))
                    ev.append("%s %s" % (label, out))
                else:
                    good, line = judge(rows, subjects, pat)
                    tok_ok = tok_ok and good
                    ev.append("%s %s" % (label, "ok" if good else "WRONG"))
                print("%s\t%s\t%s\t%s\t%s" % (tid, token, label, pat,
                                              line if out != "compiled"
                                              else "compiled\t" + line))
            verdict[(tid, token)] = (tok_ok, "; ".join(ev))
        for label, pat, subs in NATIVE_SCOPE:
            subjects = [U(s) for s in subs]
            out, diag, rows = run_one(adapters, tid, tmp, label, pat, subjects)
            print("%s\t(native scope)\t%s\t%s\t%s" % (
                tid, label, pat, out if out != "compiled" else
                "compiled\t" + " ".join("%s[%s,%s)" % (r[0], r[1], r[2])
                                        if r[0] == "match" else r[0] for r in rows)))
    print()
    print("--- A summary: SATISFIED (S) / NOT (-) ---")
    toks = list(NEW_TOKEN_WITNESSES)
    print("config\t" + "\t".join(toks))
    for tid in NEW + UNCHANGED + BYTE:
        print(tid + "\t" + "\t".join("S" if verdict[(tid, t)][0] else "-"
                                     for t in toks))

    print()
    print("=== B. unicode-properties re-census (general categories) ===")
    for tid in NEW + UNCHANGED:
        tok_ok, ev = True, []
        for label, pat, subs in PROPS_WITNESSES:
            subjects = [U(s) for s in subs]
            out, diag, rows = run_one(adapters, tid, tmp, "p-" + label, pat, subjects)
            if out != "compiled" and SIZE_REFUSAL in diag:
                # A SIZE refusal is not a missing capability: the construct
                # is supported and the artifact exceeds pcrec's emitted-size
                # cap (utf8_set_v1.md 15 R4 / P7 -- a FINDING, which the
                # set must SEE as a first-class did-not-compile row, never
                # hide behind an unsatisfied token). Precedent: onig-
                # default's `recursion`, testees/onig/CLAUDE.md.
                ev.append("%s SIZE-REFUSED" % label)
                print("%s\t%s\t%s\t%s (size cap, not a capability): %s"
                      % (tid, label, pat, out, diag.replace("\n", " | ")[:120]))
            elif out != "compiled":
                tok_ok = False
                ev.append("%s %s" % (label, out))
                print("%s\t%s\t%s\t%s: %s" % (tid, label, pat, out,
                                             diag.replace("\n", " | ")))
            else:
                good, line = judge(rows, subjects, pat)
                tok_ok = tok_ok and good
                ev.append("%s %s" % (label, "ok" if good else "WRONG"))
                print("%s\t%s\t%s\tcompiled\t%s" % (tid, label, pat, line))
        verdict[(tid, "unicode-properties")] = (tok_ok, "; ".join(ev))

    print()
    print("=== C. Script / Script_Extensions spellings (7.4's UNCONFIRMED row) ===")
    print("subjects: 'α' (U+03B1, sc=Greek), U+0342 (sc=Inherited, "
          "scx={Greek}), 'a' -- oracle column = libpcre2's own reading")
    for label, pat, subs in SCRIPT_WITNESSES:
        exps = " ".join(oracle_answer(pat, U(s))[0] for s in subs)
        print("%s\t%s\t(oracle: %s)" % (label, pat, exps))
    for tid in NEW + UNCHANGED:
        for label, pat, subs in SCRIPT_WITNESSES:
            subjects = [U(s) for s in subs]
            out, diag, rows = run_one(adapters, tid, tmp, "sc-" + label, pat, subjects)
            if out != "compiled":
                print("%s\t%s\t%s: %s" % (tid, label, out,
                                          diag.replace("\n", " | ")[:140]))
            else:
                good, line = judge(rows, subjects, pat)
                print("%s\t%s\tcompiled\t%s%s" % (tid, label, line,
                                                  "" if good else "  <- DIVERGES"))

    print()
    print("=== D. the fourteen compile-witness tokens on the ten new configs ===")
    for tid in NEW:
        sib = SIBLING[tid]
        for token, pats in OLD_TOKEN_WITNESSES.items():
            comp = []
            for i, pat in enumerate(pats):
                out, diag, _rows = run_one(adapters, tid, tmp,
                                           "o-%s-%d" % (token, i), pat, [])
                comp.append(out == "compiled")
                print("%s\t%s\t%s\t%s%s" % (tid, token, pat, out,
                                            "" if out == "compiled" else
                                            ": " + diag.replace("\n", " | ")[:120]))
            sib_has = token in sibling_decl.get(sib, set())
            verdict[(tid, token)] = (
                sib_has and all(comp),
                "sibling %s %s; compile under UTF-8 %s"
                % (sib, "declares" if sib_has else "withholds",
                   "all" if all(comp) else "REFUSED"))

    print()
    print("=== E. execution-model tokens on the ten new configs ===")
    for tid in NEW:
        out, diag, rows = run_one(adapters, tid, tmp, "e-caps", r"(a)(b)", [b"xab"])
        r = rows[0] if rows else None
        print("%s\t(a)(b) over xab\t%s\t%s" % (tid, out, r if r else diag))
        span_ok = bool(r and r[0] == "match" and r[1] not in (None, "-"))
        caps_ok = bool(r and r[3] not in (None, "-", "", []))
        sib = SIBLING[tid]
        verdict[(tid, "span-reporting")] = (
            span_ok and "span-reporting" in sibling_decl[sib],
            "span %s; sibling %s" % ("reported" if span_ok else "not reported",
                                     "declares" if "span-reporting" in sibling_decl[sib]
                                     else "withholds"))
        verdict[(tid, "captures")] = (
            caps_ok and "captures" in sibling_decl[sib],
            "caps %r; sibling %s" % (r[3] if r else None,
                                     "declares" if "captures" in sibling_decl[sib]
                                     else "withholds"))
        out, diag, rows = run_one(adapters, tid, tmp, "e-nonutf8", r"a",
                                  [b"\xffa\xff"])
        r = rows[0] if rows else None
        print("%s\ta over \\xffa\\xff\t%s\t%s" % (tid, out, r if r else diag))
        # NOT, BY RULE, on every UTF-8 config, whatever the witness says:
        # the config's subject contract IS valid UTF-8 (PCRE2 refuses
        # invalid input outright, -23 above; HS_FLAG_UTF8 and
        # ONIG_ENCODING_UTF8 document invalid input as UNDEFINED, so a
        # `match` here is not a capability anyone promised), and the utf8
        # set runs no invalid subject at all (growth (h), Q10). The
        # witness row is recorded as information, never as the verdict.
        verdict[(tid, "non-utf8-subject")] = (
            False, "by rule (a UTF-8 config's subject contract is valid "
                   "UTF-8); witness: a over \\xffa\\xff -> %s"
                   % (r[0] if r else out))

    print()
    print("=== F. the set's own spellings (informational, for U4/U5) ===")
    for label, pat, subs in SET_SPELLINGS:
        exps = " ".join(oracle_answer(pat, U(s))[0] for s in subs)
        print("%s\t%s\t(oracle: %s)" % (label, pat, exps))
    for tid in NEW + UNCHANGED:
        for label, pat, subs in SET_SPELLINGS:
            subjects = [U(s) for s in subs]
            out, diag, rows = run_one(adapters, tid, tmp, "f-" + label, pat, subjects)
            if out != "compiled":
                print("%s\t%s\t%s: %s" % (tid, label, out,
                                          diag.replace("\n", " | ")[:140]))
            else:
                good, line = judge(rows, subjects, pat)
                print("%s\t%s\tcompiled\t%s%s" % (tid, label, line,
                                                  "" if good else "  <- DIVERGES"))

    print()
    print("=== THE DECLARATIONS (what bench/utf8's ext bench matrix transcribes) ===")
    all_tokens = sorted(REQUIRES_VOCAB)
    for tid in NEW + UNCHANGED:
        declared = []
        for tok in all_tokens:
            if (tid, tok) in verdict:
                ok, ev = verdict[(tid, tok)]
            elif tid in UNCHANGED:
                ok = tok in sibling_decl.get(tid, set())
                ev = "unchanged config: its committed bench/capability declaration"
            else:
                ok, ev = False, "NOT WITNESSED"
            if ok:
                declared.append(tok)
            print("%s\t%s\t%s\t%s" % (tid, tok, "SATISFIED" if ok else "not", ev))
        print("%s DECLARES %d/%d: %s" % (tid, len(declared), len(all_tokens),
                                         " ".join(declared)))
        print()
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
