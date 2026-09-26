#!/usr/bin/env python3
"""docs/dev/measurements/probe_vectorscan_som_utf8_witness_census.py --
the reproducing script behind
2026-09-26-vectorscan-som-utf8-witness-census.txt.

[B99] (docs/dev/plan.md; [B92]'s own "No UTF-8 sibling yet" section in
testees/vectorscan/CLAUDE.md named this OWED): `vectorscan-block-som-utf8`
is `vectorscan-block-som`'s character-mode sibling, exactly the shape
[B77] U2 built for `vectorscan-block-nosom-utf8` -- hs_compile flags
HS_FLAG_UTF8 (driver `--encoding utf8`) ORed ONTO HS_FLAG_SOM_LEFTMOST,
never HS_FLAG_UCP. "The mechanism composes" ([B92]'s own smoke test) is
not the same claim as "the capability declaration and the UTF-8-specific
divergences are known" -- this is the witness census that closes that
gap, mirroring TWO existing censuses at once:

  * `probe_b77u2_utf8_witness_census.py` ([B77] U2) -- per-(config,
    REQUIRES token) witnesses, oracle-checked, BEFORE any UTF-8 config's
    capability declaration ships (the L5 lesson);
  * `probe_vectorscan_som_witness_census.py` ([B92]) -- the SOM-only
    compile restriction's real cost over `bench/capability`'s 64 corpus
    patterns, compared against its `nosom` sibling.

COMPILE/WITNESS-LEVEL ONLY: no timing is read, no quiet box is needed
(every U2/[B92] census before it states the same exemption). This
census carries NO capability declaration of its own to ship -- like
EVERY other `-utf8` config on this roster (`vectorscan-block-nosom-utf8`
included), a per-encoding config gets no `EXT_BENCH_ROSTER` row at all
(the roster is keyed by engine_mode; capability_set_v1.md never grew a
per-encoding row). This file is documentation for
`testees/vectorscan/CLAUDE.md`'s UTF-8/SOM sections, the same role
2026-09-25-b77u2-utf8-witness-census.txt plays for `-nosom-utf8`.

SEVEN SECTIONS:

  A. THE THREE UTF8-SET TOKENS (utf8-encoding, ascii-class-scope,
     unicode-class-scope) on `som-utf8`, span+NMATCHES checked BY VALUE
     against the libpcre2 oracle (FULL grain -- unlike U2's boolean-grain
     arm for `nosom-utf8`, which could only check `answer`).
  B. unicode-properties re-census (general categories), span-checked.
  C. Script / Script_Extensions spellings over `alpha`/U+0342/`a`
     (informational, compared against nosom-utf8's own known reading).
  D. THE THIRTEEN SYNTAX-REFUSAL TOKENS (compile-only): a sibling's
     declaration carries over to `som-utf8` ONLY if the same witness ALSO
     compiles under `som-utf8` -- sibling here is `vectorscan-block-som`
     (the BYTE config this is the UTF-8 sibling of), read live off
     `bench/capability/gen_patterns.py`'s own EXT_BENCH_ROSTER (never
     retyped).
  E. EXECUTION-MODEL tokens (span-reporting, captures, non-utf8-subject)
     via match witnesses -- `som-utf8` is FULL grain, so span-reporting
     is checked BY VALUE, not merely inherited.
  F. THE SOM-ONLY COMPILE RESTRICTION UNDER UTF-8: the isolated witness
     [B92]'s own selfcheck arm 5 uses, PLUS all 64 real bench/capability
     corpus patterns compiled under BOTH `nosom-utf8` and `som-utf8`
     (plain form) -- does UTF-8 encoding change which patterns SOM's own
     history-tracking restriction costs?
  G. THE DOCUMENTED DIVERGENCE (leftmost-longest vs leftmost-first)
     reproduced with a genuinely MULTI-BYTE alternation, to show the
     divergence survives UTF-8 encoding, not just single-byte ASCII.
  H. `(*UCP)`'s INTERACTION WITH SOM_LEFTMOST -- CLAUDE.md's own named
     unknown: does `(*UCP)\\w+` compile and report a real span under
     SOM+UTF8? Does the documented `\\b`-under-UCP breakage
     (utf8_set_v1.md 7.6, the measured A/B) reproduce identically here,
     orthogonally to SOM?

Run: python3 docs/dev/measurements/probe_vectorscan_som_utf8_witness_census.py
(from the repo root; needs the `vectorscan` adapter's driver, built on
demand -- libvectorscan-dev must be installed).
"""
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)

from pcrecbench import adapters as ad          # noqa: E402
from pcrecbench import oracle_pcre2 as oracle  # noqa: E402
from pcrecbench import subbench as sbmod       # noqa: E402

U = lambda s: s.encode("utf-8")   # noqa: E731

# Section A -- the same three witnesses U2's own census uses.
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
        ("s-ascii", r"a\sb", ["a b", "a b"]),
        ("posix-alpha-ascii", r"[[:alpha:]]+", ["é", "abc"]),
    ],
    "unicode-class-scope": [
        ("w-ucp", r"(*UCP)\w+", ["Москва", "--"]),
        ("d-ucp", r"(*UCP)\d{4}", ["٠١٢٣", "abcd"]),
        ("s-ucp", r"(*UCP)a\sb", ["a b", "ab"]),
    ],
}

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
    ("Script=Greek", r"\p{Script=Greek}", GREEK_SUBJ),
    ("Script_Extensions=Greek", r"\p{Script_Extensions=Greek}", GREEK_SUBJ),
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

# The isolated SOM-only-refusal witness [B92]'s own
# tools/selfcheck.py:check_vectorscan_som arm 5 and
# probe_vectorscan_som_witness_census.py both use.
SOM_ONLY_REFUSAL_WITNESS = rb".*a.{40,}"

NEW = "vectorscan-block-som-utf8"
SIBLING_ENCODING = "vectorscan-block-nosom-utf8"   # the encoding sibling
SIBLING_SOM = "vectorscan-block-som"               # the SOM byte sibling


class Subj:
    def __init__(self, i, path, n):
        self.subject_id, self.path, self.length = "s-%d" % i, path, n


def oracle_answer(pat, subj):
    """-> (answer, start, end, count) under the utf8 set's own word:
    PCRE2_UTF; PCRE2_UCP arrives inline from the pattern's own `(*UCP)`
    spelling."""
    try:
        rx = oracle.compile(U(pat), oracle.option_word(utf=True))
    except oracle.Pcre2Error as e:
        return ("refused", str(e)[:60], None, None)
    m = rx.search(subj)
    if m is None:
        return ("nomatch", None, None, None)
    first, count = rx.find_all(subj)
    return ("match", first[0], first[1], count)


def run_one(adapters, tid, tmp, label, pat, subjects, find_all=False):
    """-> (outcome, diagnostic, rows): rows = per-subject
    (answer, start, end, nmatches, caps)."""
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
    h["utf8_advance"] = True      # [B77] U1's handle, inert unless --som
    regime = "throughput" if find_all else "search_short"
    try:
        got, _i, _n = a.measure(h, regime, subj, 1, 1, timeout=120)
    except Exception as e:                                  # noqa: BLE001
        return "measure-error", str(e)[:160], []
    rows = [(r.answer, r.start, r.end, r.nmatches, r.caps)
            for r in (got[0] if got else [])]
    return "compiled", "", rows


def compile_only(adapters, tid, tmp, name, pat):
    a = adapters[tid]
    cp = a.compile(tid, name, pat, {}, 1, tmp)
    r = cp.get(ad.FORM_PLAIN)
    return r.outcome, r.diagnostic


def judge_full(rows, subjects, pat, find_all=False):
    """-> (ok, text): FULL-grain agreement -- answer, real span, and (if
    find_all) NMATCHES, all checked against the oracle."""
    parts, ok = [], True
    for (ans, st, en, nm, _c), s in zip(rows, subjects):
        exp_ans, exp_st, exp_en, exp_n = oracle_answer(pat, s)
        span_ok = (ans != "match") or (st not in (None, "-")
                                       and (int(st), int(en)) == (exp_st, exp_en))
        n_ok = (not find_all) or (nm not in (None, "-")
                                  and int(nm) == exp_n)
        good = ans == exp_ans and span_ok and n_ok
        ok = ok and good
        span = "" if st in (None, "-") else "[%s,%s)" % (st, en)
        parts.append("%s%s%s%s" % (ans, span,
                                   "" if not find_all else "/n=%s" % nm,
                                   "" if good else "!=oracle(%s[%s,%s)/n=%s)"
                                   % (exp_ans, exp_st, exp_en, exp_n)))
    if len(rows) != len(subjects):
        ok = False
        parts.append("rows %d != subjects %d" % (len(rows), len(subjects)))
    return ok, " ".join(parts)


def main():
    adapters = {}
    for eng in ad.discover(root=os.path.join(ROOT, "testees")).values():
        for tid in eng.testees():
            adapters[tid] = eng
    tmp = tempfile.mkdtemp(prefix="b99som-utf8-census-")
    for tid in (NEW, SIBLING_ENCODING, SIBLING_SOM):
        adapters[tid].prepare(tid, tmp)

    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "cap_gen", os.path.join(ROOT, "bench", "capability", "gen_patterns.py"))
    cap = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cap)
    roster = {t: set(c) for t, c in cap.EXT_BENCH_ROSTER}
    som_decl = roster[SIBLING_SOM]

    print("pcrec pin: n/a (vectorscan-only census)")
    print("vectorscan version: %s" % adapters[NEW].probe_version(tmp))
    print("oracle: libpcre2 %s, option word PCRE2_UTF (+ inline (*UCP))"
          % oracle.version())
    print("%s's own EXT_BENCH_ROSTER declaration (bench/capability): %s"
          % (SIBLING_SOM, sorted(som_decl)))
    print()

    verdict = {}

    print("=== A. the three utf8-set tokens on %s ===" % NEW)
    print("config\ttoken\twitness\tpattern\toutcome\tanswer (vs the UTF oracle, full grain)")
    for token, wits in NEW_TOKEN_WITNESSES.items():
        tok_ok, ev = True, []
        for label, pat, subs in wits:
            subjects = [U(s) for s in subs]
            out, diag, rows = run_one(adapters, NEW, tmp, label, pat, subjects)
            if out != "compiled":
                tok_ok = False
                line = "%s: %s" % (out, diag.replace("\t", " ").replace("\n", " | "))
                ev.append("%s %s" % (label, out))
            else:
                good, line = judge_full(rows, subjects, pat)
                tok_ok = tok_ok and good
                ev.append("%s %s" % (label, "ok" if good else "WRONG"))
            print("%s\t%s\t%s\t%s\t%s" % (NEW, token, label, pat,
                                          line if out != "compiled"
                                          else "compiled\t" + line))
        verdict[token] = (tok_ok, "; ".join(ev))
    print()
    print("--- A summary: SATISFIED (S) / NOT (-), %s, full grain ---" % NEW)
    for t in NEW_TOKEN_WITNESSES:
        print("%s\t%s" % (t, "S" if verdict[t][0] else "-"))

    print()
    print("=== B. unicode-properties re-census (general categories), span-checked ===")
    tok_ok, ev = True, []
    for label, pat, subs in PROPS_WITNESSES:
        subjects = [U(s) for s in subs]
        out, diag, rows = run_one(adapters, NEW, tmp, "p-" + label, pat, subjects)
        if out != "compiled" and "pattern too large" in (diag or ""):
            # a SIZE refusal is not a missing capability (R4/P7's rule,
            # restated in the U2 census) -- N/A here since vectorscan has
            # no emitted-size cap at all, kept for structural parity.
            ev.append("%s SIZE-REFUSED" % label)
            print("%s\t%s\t%s (size cap, not a capability): %s"
                  % (label, pat, out, diag.replace("\n", " | ")[:120]))
        elif out != "compiled":
            tok_ok = False
            ev.append("%s %s" % (label, out))
            print("%s\t%s\t%s: %s" % (label, pat, out, diag.replace("\n", " | ")))
        else:
            good, line = judge_full(rows, subjects, pat)
            tok_ok = tok_ok and good
            ev.append("%s %s" % (label, "ok" if good else "WRONG"))
            print("%s\t%s\tcompiled\t%s" % (label, pat, line))
    verdict["unicode-properties"] = (tok_ok, "; ".join(ev))
    print("unicode-properties: %s" % ("SATISFIED" if tok_ok else "NOT"))

    print()
    print("=== C. Script / Script_Extensions spellings (informational) ===")
    print("subjects: 'alpha' (U+03B1, sc=Greek), U+0342 (sc=Inherited, "
          "scx={Greek}), 'a' -- oracle column = libpcre2's own reading")
    for label, pat, subs in SCRIPT_WITNESSES:
        exps = " ".join(oracle_answer(pat, U(s))[0] for s in subs)
        subjects = [U(s) for s in subs]
        out, diag, rows = run_one(adapters, NEW, tmp, "sc-" + label, pat, subjects)
        if out != "compiled":
            print("%s\t%s\t(oracle: %s)\t%s: %s" % (label, pat, exps, out,
                                                    diag.replace("\n", " | ")[:140]))
        else:
            good, line = judge_full(rows, subjects, pat)
            print("%s\t%s\t(oracle: %s)\tcompiled\t%s%s"
                 % (label, pat, exps, line, "" if good else "  <- DIVERGES"))

    print()
    print("=== D. the thirteen syntax-refusal tokens on %s "
          "(sibling = %s's own EXT_BENCH_ROSTER row) ===" % (NEW, SIBLING_SOM))
    for token, pats in OLD_TOKEN_WITNESSES.items():
        comp = []
        for i, pat in enumerate(pats):
            out, diag = compile_only(adapters, NEW, tmp, "o-%s-%d" % (token, i), U(pat))
            comp.append(out == "compiled")
            print("%s\t%s\t%s%s" % (token, pat, out,
                                    "" if out == "compiled" else
                                    ": " + (diag or "").replace("\n", " | ")[:120]))
        sib_has = token in som_decl
        verdict[token] = (sib_has and all(comp),
                          "sibling %s %s; compile under som+UTF-8 %s"
                          % (SIBLING_SOM, "declares" if sib_has else "withholds",
                             "all" if all(comp) else "REFUSED"))

    print()
    print("=== E. execution-model tokens (span-reporting, captures, "
          "non-utf8-subject) ===")
    out, diag, rows = run_one(adapters, NEW, tmp, "e-caps", r"(a)(b)", [b"xab"])
    r = rows[0] if rows else None
    print("(a)(b) over xab\t%s\t%s" % (out, r if r else diag))
    span_ok = bool(r and r[0] == "match" and r[1] not in (None, "-"))
    caps_ok = bool(r and r[4] not in (None, "-", "", []))
    verdict["span-reporting"] = (span_ok, "span %s (full grain: real span "
                                 "expected, exactly like plain %s)"
                                 % ("reported" if span_ok else "NOT reported",
                                    SIBLING_SOM))
    verdict["captures"] = (caps_ok, "caps %r (Hyperscan has no capturing "
                           "groups regardless of SOM/encoding)"
                           % (r[4] if r else None))
    out, diag, rows = run_one(adapters, NEW, tmp, "e-nonutf8", r"a", [b"\xffa\xff"])
    r = rows[0] if rows else None
    print("a over \\xffa\\xff\t%s\t%s" % (out, r if r else diag))
    verdict["non-utf8-subject"] = (
        False, "by rule (a UTF-8 config's subject contract is valid "
               "UTF-8, utf8_set_v1.md); witness: a over \\xffa\\xff -> %s"
               % (r[0] if r else out))

    print()
    print("=== F. the SOM-only compile restriction UNDER UTF-8 encoding ===")
    outcome_nosom, diag_nosom = compile_only(
        adapters, SIBLING_ENCODING, tmp, "w-nosomutf8", SOM_ONLY_REFUSAL_WITNESS)
    outcome_som, diag_som = compile_only(
        adapters, NEW, tmp, "w-somutf8", SOM_ONLY_REFUSAL_WITNESS)
    print("isolated witness .*a.{40,}: %s=%-16s %s=%-16s"
         % (SIBLING_ENCODING, outcome_nosom, NEW, outcome_som))
    if outcome_nosom != outcome_som:
        print("    %s diag: %s" % (SIBLING_ENCODING, diag_nosom or ""))
        print("    %s diag: %s" % (NEW, diag_som or ""))

    sb = sbmod.Subbench(os.path.join(ROOT, "bench", "capability"))
    print()
    print("bench/capability's 64 corpus patterns, plain form, "
          "%s vs %s:" % (SIBLING_ENCODING, NEW))
    n_both = n_nosom_only = n_som_only = n_neither = 0
    divergences = []
    for p in sb.patterns:
        txt = p.text
        o_nosom, d_nosom = compile_only(adapters, SIBLING_ENCODING, tmp,
                                        "c-nu-" + p.name, txt)
        o_som, d_som = compile_only(adapters, NEW, tmp, "c-su-" + p.name, txt)
        ok_nosom, ok_som = o_nosom == "compiled", o_som == "compiled"
        if ok_nosom and ok_som:
            n_both += 1
        elif ok_nosom and not ok_som:
            n_nosom_only += 1
            divergences.append((p.name, d_som))
        elif ok_som and not ok_nosom:
            n_som_only += 1
            divergences.append((p.name, "compiles under %s but NOT %s -- "
                               "unexpected: %r" % (NEW, SIBLING_ENCODING, d_nosom)))
        else:
            n_neither += 1
    print("compiled under BOTH:                              %d" % n_both)
    print("compiled under %s ONLY (SOM's own restriction "
          "under UTF-8): %d" % (SIBLING_ENCODING, n_nosom_only))
    print("compiled under %s ONLY (unexpected):               %d"
         % (NEW, n_som_only))
    print("compiled under NEITHER:                            %d" % n_neither)
    if divergences:
        print()
        print("--- the restriction's cost, by pattern ---")
        for name, diag in divergences:
            print("  %-48s -> %s" % (name, diag))

    print()
    print("=== G. THE DOCUMENTED DIVERGENCE, over a genuinely multi-byte "
          "alternation ===")
    div_pat, div_subj = r"α|αβ", "αβ".encode("utf-8")
    exp_ans, exp_st, exp_en, exp_n = oracle_answer(div_pat, div_subj)
    out, diag, rows = run_one(adapters, NEW, tmp, "div", div_pat, [div_subj],
                              find_all=True)
    r = rows[0] if rows else None
    print("%r over %r (UTF-8, %d bytes)" % (div_pat, div_subj, len(div_subj)))
    print("  oracle (leftmost-first): %s [%s,%s) n=%s" % (exp_ans, exp_st, exp_en, exp_n))
    print("  %s (leftmost-longest):   %s" % (NEW, r if r else (out, diag)))

    print()
    print("=== H. (*UCP)'s interaction with SOM_LEFTMOST ===")
    ucp_pat, ucp_subj = r"(*UCP)\w+", "Москва".encode("utf-8")
    out, diag, rows = run_one(adapters, NEW, tmp, "ucp-w", ucp_pat, [ucp_subj])
    r = rows[0] if rows else None
    print("%r over %r: %s\t%s" % (ucp_pat, ucp_subj, out, r if r else diag))
    b_pat = r"(*UCP)\bМосква\b"
    out, diag = compile_only(adapters, NEW, tmp, "ucp-b", U(b_pat))
    print("%r: %s%s" % (b_pat, out, "" if out == "compiled" else
                        ": " + (diag or "").replace("\n", " | ")[:140]))
    out_sib, diag_sib = compile_only(adapters, SIBLING_ENCODING, tmp, "ucp-b-sib", U(b_pat))
    print("  %s (encoding sibling, no SOM): %s%s -- SAME breakage iff "
          "orthogonal to SOM" % (SIBLING_ENCODING, out_sib,
                                 "" if out_sib == "compiled" else
                                 ": " + (diag_sib or "").replace("\n", " | ")[:140]))

    print()
    print("=== THE DECLARATIONS (informational -- no EXT_BENCH_ROSTER row "
          "for any -utf8 config on this roster) ===")
    all_tokens = sorted(set(NEW_TOKEN_WITNESSES) | {"unicode-properties"}
                        | set(OLD_TOKEN_WITNESSES)
                        | {"span-reporting", "captures", "non-utf8-subject"})
    declared = []
    for tok in all_tokens:
        ok, ev = verdict.get(tok, (False, "NOT WITNESSED"))
        if ok:
            declared.append(tok)
        print("%s\t%s\t%s" % (tok, "SATISFIED" if ok else "not", ev))
    print("%s WOULD DECLARE %d/%d if it carried a roster row: %s"
         % (NEW, len(declared), len(all_tokens), " ".join(sorted(declared))))


if __name__ == "__main__":
    main()
