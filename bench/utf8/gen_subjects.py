#!/usr/bin/env python3
"""gen_subjects.py -- the utf8 set's short subjects: `subjects/` (gitignored)
+ `manifest.tsv` (committed).

TYPED, not drawn, per utf8_set_v1.md 4.3/10.1 and `bench/capability`'s own
precedent (`capability/gen_subjects.py`'s docstring): each subject is at
least one family member's designed HIT and, where the family has a
semantic edge, another member's designed near-miss or MISS. Fifteen per
family (a)-(f) = 90, plus one dedicated floor witness = 91 (the design
note's own arithmetic, utf8_set_v1.md 10.3, counts the family total as
90 and treats the floor separately -- `bench/capability`'s own SUBJECTS
table folds its floor witness INTO its stated "75"; this generator states
both numbers explicitly in its own printout and in CLAUDE.md/NOTES.md
rather than silently picking one convention).

WHAT THIS LANE (U3) DOES NOT KNOW YET. `bench/utf8/patterns.rxt` does not
exist -- U4 builds it, after this lane, from the SAME family tables in
`docs/design/utf8_set_v1.md` 5. Every subject below is typed against that
design note's own pattern TEXT (not against a `.rx` file, which does not
exist), so a subject's actual match/no-match answer is left to
`gen_expectations.py` (U5) once the real patterns are built -- exactly
`bench/capability/gen_subjects.py`'s own discipline ("this module only
states the INTENT each subject was typed for"). Two subjects
(`alt-cyr64-hit`, `alt-cyr64-miss`) additionally COORDINATE with U4: they
assume the 64-branch Cyrillic alternation (`alt-cyr-64`, utf8_set_v1.md
5(d)) is built from common words including "дом" ("house")
and excluding a rare compound -- stated in each subject's own description
so U4's author can either honor the assumption or correct these two
subjects when the real pattern lands.

Every subject is authored as a Python `str` (never a raw byte literal --
typing exotic UTF-8 byte sequences by hand invites exactly the silent
corruption utf8_set_v1.md 4.1 warns about) and encoded to UTF-8 at build
time; `build()` runs every subject through `utf8text.decode_gate()` (a
redundant confirmation -- `str.encode("utf-8")` cannot itself produce
ill-formed bytes, but the gate is exercised here anyway so the SAME
function this module's own `--check` also calls for its negative-arm
proof is exercised on every real subject the module writes).
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

import utf8text as ut  # noqa: E402

OUT = os.path.join(HERE, "subjects")
MANIFEST = os.path.join(HERE, "manifest.tsv")
MAX_LINE = 512  # short_search_max_bytes, once U4's sidecar declares it

# (id, description, text) -- 15 per family (a)-(f) + 1 floor witness = 91.
SUBJECTS = (
    # ---- family (a) CLASSES (cls-*), 15 subjects, 16 members ----------
    ("cls-boundary-range", "field/hit `[a-é]+` (cls-boundary-range): "
     "'café' -- every character (c,a,f,é) is in the range "
     "U+0061..U+00E9", "café"),
    ("cls-high-range", "field/hit `[\\x{100}-\\x{2000}]+` "
     "(cls-high-range): a Cyrillic word, entirely inside the range",
     "мир"),
    ("cls-neg-single-miss", "field/miss `[^é]` (cls-neg-single): the "
     "WHOLE subject is é alone -- no non-é character exists to "
     "match", "é"),
    ("cls-cyr-triple", "field/edge, THREE members at once: "
     "`[^\\x{80}-\\x{10FFFF}]+` (cls-neg-allhigh) MISSES (no ASCII byte "
     "anywhere); `\\w+` without UCP (cls-w-ascii) MISSES (Cyrillic "
     "letters are not ASCII word chars); `(*UCP)\\w+` (cls-w-ucp) HITS "
     "on the same text", "москва"),
    ("cls-mixed-hit", "field/hit `[a-zé\\x{430}-\\x{44F}]+` "
     "(cls-mixed) AND `[^\\x{4E00}-\\x{9FFF}]+` (cls-neg-cjk, none of "
     "these characters is Han): a, é, б in one run",
     "aéб"),
    ("cls-dot-hit", "field/hit `.` (cls-dot): one CJK character",
     "日"),
    ("cls-dot-rep-hit", "field/hit `^.{5}$` (cls-dot-rep): 5 CHARACTERS "
     "(4x 2-byte + 1x 4-byte) totalling 12 BYTES",
     "éééé\U0001f600"),
    ("cls-dot-rep-miss", "field/miss `^.{5}$` (cls-dot-rep): 3 "
     "characters (1+2+2 bytes = 5 BYTES) -- 5 bytes but only 3 "
     "characters, so it must NOT match", "aéè"),
    ("cls-w-ascii-posix-hit", "field/hit `\\w+` ascii-scoped "
     "(cls-w-ascii) and `[[:alpha:]]+` (cls-posix-alpha): plain ASCII",
     "hello123"),
    ("cls-digit-pair", "field/edge, digit ascii/ucp PAIR: four "
     "Arabic-Indic digits -- `\\d{4}` ascii-scoped (cls-d-ascii) MISSES, "
     "`(*UCP)\\d{4}` (cls-d-ucp) HITS", "٠١٢٣"),
    ("cls-space-pair", "field/edge, space ascii/ucp PAIR: 'a' NBSP 'b' -- "
     "`a\\sb` ascii-scoped (cls-s-nbsp) MISSES, `(*UCP)a\\sb` "
     "(cls-s-ucp) HITS", "a b"),
    ("cls-posix-straupperss", "field/edge `[[:alpha:]]+` "
     "(cls-posix-alpha): 'Straße' -- the ASCII-scoped run stops at "
     "ß (not an ASCII letter), a scope-boundary witness",
     "die Straße"),
    ("cls-lead-pair-hit", "field/hit `[α-ω]+` (cls-lead-pair): "
     "Greek alpha-beta-gamma, a class UD 6.3 says a two-lead-byte "
     "bitmap-skip arm must take", "αβγ"),
    ("cls-neg-cjk-miss", "field/miss `[^\\x{4E00}-\\x{9FFF}]+` "
     "(cls-neg-cjk): pure Han text -- every character IS in the negated "
     "range, so no run can match", "日本語"),
    ("cls-allhigh-ascii-hit", "field/hit `[^\\x{80}-\\x{10FFFF}]+` "
     "(cls-neg-allhigh): pure byte-clean ASCII", "plain text"),

    # ---- family (b) LITERALS (lit-*), 15 subjects, 12 members ---------
    ("lit-2b-hit", "field/hit `é` (lit-1ch-2b): one 2-byte "
     "character alone", "é"),
    ("lit-3b-hit", "field/hit `日` (lit-1ch-3b): one 3-byte "
     "character alone", "日"),
    ("lit-4b-hit", "field/hit `\U0001f600` (lit-1ch-4b): one 4-byte "
     "character alone", "\U0001f600"),
    ("lit-run3-hit", "field/hit `日本語` (lit-run-3) AND "
     "`^日本語$` (lit-anchored-run): the EXACT 9-byte run, "
     "nothing else", "日本語"),
    ("lit-nearmiss", "field/near-miss `日本語` "
     "(lit-nearmiss-run's own twin): shares two characters (six bytes) "
     "and fails at the third", "日本人"),
    ("lit-mixedascii-hit", "field/hit `user@例え.jp` "
     "(lit-mixed-ascii): the exact mixed-width literal, ASCII @ and . "
     "available as the necessary byte", "user@例え.jp"),
    ("lit-mixedascii-miss", "field/miss `user@例え.jp` "
     "(lit-mixed-ascii): the @ is replaced, breaking the literal",
     "user##example.jp"),
    ("lit-cyrrun-hit", "field/hit `Москва` "
     "(lit-cyr-run): the exact 12-byte run, every lead byte 0xD0/0xD1",
     "Москва"),
    ("lit-offset-tail-hit", "field/hit `é@` (lit-offset-at-tail): "
     "THE FIRST CUSTOMER (P1) -- the necessary byte at the TAIL",
     "é@"),
    ("lit-offset-head-hit", "field/hit `@é` (lit-offset-at-head): "
     "P1's order pair -- the necessary byte at the HEAD", "@é"),
    ("lit-nfc-decomposed-miss", "field/miss `café` PRECOMPOSED "
     "(lit-nfc-pair): a DECOMPOSED subject (e + COMBINING ACUTE, "
     "U+0301) -- byte-different from the precomposed pattern, no "
     "normalization happens anywhere on this roster",
     "café"),
    ("lit-nfc-precomposed-hit", "field/hit `café` PRECOMPOSED "
     "(lit-nfc-pair): the precomposed form, embedded in a sentence",
     "un café"),
    ("lit-sharps-hit", "field/hit `Straße` (lit-sharp-s): the "
     "exact literal with its 2-byte ß, embedded",
     "die Straße"),
    ("lit-sharps-miss", "field/miss `Straße` (lit-sharp-s): "
     "case-sensitive AND 'SS' != 'ß' -- neither substitution "
     "matches the literal", "DIE STRASSE"),
    ("lit-anchored-extra-miss", "field/edge `^日本語$` "
     "(lit-anchored-run): the run plus trailing content -- "
     "lit-run-3 still HITS (substring search) but the anchored form "
     "MISSES (extra suffix breaks the exact match)",
     "日本語です"),

    # ---- family (c) CASELESS (ci-*), 15 subjects, 12 members ----------
    ("ci-eacute-triple", "field/edge, THREE members at once: `(?i)é` "
     "(ci-e-acute) HITS on uppercase É; `(*UCP)(?i)é` "
     "(ci-ucp-invariance) agrees (the control); `(?i)[^é]` "
     "(ci-neg-fold) MISSES -- the whole subject folds to é, no "
     "non-é-fold character is present", "É"),
    ("ci-moskva-hit", "field/hit `(?i)москва`"
     " (ci-moskva): all-uppercase Cyrillic folds to the pattern",
     "МОСКВА"),
    ("ci-greek-hit", "field/hit `(?i)αβγ` (ci-greek-run): "
     "all-uppercase Greek folds to the pattern",
     "ΑΒΓ"),
    ("ci-kelvin-hit", "field/hit `(?i)k` (ci-kelvin): the fold CLOSURE "
     "reaching outside the written range -- U+212A KELVIN SIGN, a "
     "3-byte character, folds to ASCII k", "5K"),
    ("ci-longs-hit", "field/hit `(?i)s` (ci-long-s): U+017F LATIN "
     "SMALL LETTER LONG S, a 2-byte character, folds to ASCII s",
     "ſong"),
    ("ci-classrange-hit", "field/hit `(?i)[a-z]+` (ci-class-range): "
     "uppercase ASCII folding into the written lowercase range",
     "XYZ"),
    ("ci-negfold-hit", "field/hit `(?i)[^é]` (ci-neg-fold): an "
     "ASCII 'x' beside the fold-target É -- 'x' is NOT in the "
     "é fold class, so the negation matches it",
     "xÉ"),
    ("ci-strasse-hit", "field/hit `(?i)straße` (ci-strasse): the "
     "exact literal, lowercase", "straße"),
    ("ci-strasse-nearmiss", "field/near-miss `(?i)straße` "
     "(ci-strasse): the all-caps 'SS' spelling -- 10.46 does SIMPLE "
     "folding only, no one-to-many foldings, so this must NOT match",
     "STRASSE"),
    ("ci-sigma-final-hit", "field/hit `(?i)σ` (ci-sigma): a word "
     "carrying the FINAL SIGMA form (ς), which folds with σ/"
     "Σ under simple folding",
     "λόγος"),
    ("ci-sigma-capital-hit", "field/hit `(?i)σ` (ci-sigma): an "
     "all-caps Greek word carrying Σ", "ΣΙΓΜΑ"),
    ("ci-turkish-i-capital-miss", "field/miss `(?i)i` (ci-turkish-i): "
     "U+0130 LATIN CAPITAL I WITH DOT ABOVE -- locale-free simple "
     "folding does NOT fold this to ASCII i/I", "İstanbul"),
    ("ci-turkish-i-lower-miss", "field/miss `(?i)i` (ci-turkish-i): "
     "U+0131 LATIN SMALL LETTER DOTLESS I -- same simple-folding "
     "exclusion, the lowercase member of the pair",
     "ılık hava"),
    ("ci-ascii-control-hit", "field/hit `(?i)abc` (ci-ascii-control): "
     "the pure-ASCII fold, the cheapest member of the family",
     "ABC"),
    ("ci-ascii-control-miss", "field/miss `(?i)abc` (ci-ascii-control): "
     "pure ASCII with no 'abc' substring anywhere, in any case",
     "xyz789"),

    # ---- family (d) ALTERNATION/QUANTIFIERS (alt-*/qnt-*), 15, 12 -----
    ("alt-sharedchar-hit", "field/hit `日本|日曜|"
     "日付` (alt-shared-char): the first branch, sharing the "
     "whole first character with the other two",
     "日本"),
    ("alt-nearmiss-miss", "field/miss `日本語|日本"
     "国` (alt-nearmiss): shares six of nine bytes with both "
     "branches, matches neither", "日本人"),
    ("alt-sharedlead-hit", "field/hit `α|β|γ` "
     "(alt-shared-lead): the middle branch, all three sharing one "
     "lead byte (0xCE)", "β"),
    ("alt-distinctlead-hit", "field/hit `日本|"
     "Москва|café` "
     "(alt-distinct-lead): the third branch, three distinct lead-byte "
     "groups", "café"),
    ("alt-mixedwidth-1b", "field/hit `a|é|日|\U0001f600` "
     "(alt-mixed-width): the 1-byte branch",
     "a"),
    ("alt-mixedwidth-2b", "field/hit `a|é|日|\U0001f600` "
     "(alt-mixed-width): the 2-byte branch", "é"),
    ("alt-mixedwidth-3b", "field/hit `a|é|日|\U0001f600` "
     "(alt-mixed-width): the 3-byte branch", "日"),
    ("alt-mixedwidth-4b", "field/hit `a|é|日|\U0001f600` "
     "(alt-mixed-width): the 4-byte branch", "\U0001f600"),
    ("alt-cyr64-hit", "field/hit alt-cyr-64 (the 64-branch Cyrillic "
     "alternation, utf8_set_v1.md 5(d)): a common word "
     "('дом', house) -- U4 COORDINATION: assumes the "
     "64-word list includes this word; correct this subject if it "
     "does not", "дом"),
    ("alt-cyr64-miss", "field/miss alt-cyr-64: an uncommon compound "
     "word unlikely to be among the 64 chosen branches -- U4 "
     "COORDINATION, same caveat as alt-cyr64-hit",
     "квинтэссенц"
     "ия"),
    ("qnt-plus-lazy-hit", "field/hit `é+` (qnt-plus-2b) AND "
     "`é+?` (qnt-lazy-2b): three repeats of the 2-byte character",
     "ééé"),
    ("qnt-counted3b-hit", "field/hit `(?:日本){2,}` "
     "(qnt-counted-3b): two repeats of the two-character group",
     "日本日本"),
    ("qnt-bounded4b-hit", "field/hit `\U0001f600{2,4}` "
     "(qnt-bounded-4b): three repeats of the 4-byte character",
     "\U0001f600\U0001f600\U0001f600"),
    ("qnt-dotbounded-hit", "field/hit `.{3,8}` (qnt-dot-bounded): six "
     "CJK CHARACTERS (18 bytes) -- within the CHARACTER bound despite "
     "exceeding it in bytes", "日本語日本語"),
    ("qnt-classrun-hit", "field/hit `[\\x{400}-\\x{4FF}]{4,16}` "
     "(qnt-class-run): six characters, all in the Cyrillic block",
     "москва"),

    # ---- family (e) ASSERTIONS (asr-*), 15 subjects, 11 members -------
    ("asr-b-ascii-hit", "field/hit `\\bcat\\b` (asr-b-ascii): a "
     "bounded word", "the cat sat"),
    ("asr-b-ascii-miss", "field/miss `\\bcat\\b` (asr-b-ascii): 'cat' "
     "embedded with no boundary on either side", "concatenate"),
    ("asr-b-cyr-pair", "field/edge, the \\b UCP PAIR: `\\b"
     "Москва\\b` ascii-scoped (asr-b-cyr) "
     "MISSES (Cyrillic letters are not ASCII word chars, so \\b never "
     "fires); `(*UCP)\\bМосква\\b` "
     "(asr-b-cyr-ucp) HITS", "Москва"),
    ("asr-b-ascii-adjacent-multibyte", "field/hit `\\bcat\\b` "
     "(asr-b-ascii): the SAME bounded word beside multi-byte "
     "neighbours, confirming \\b's ASCII scope is unaffected by "
     "adjacent non-ASCII content", "café cat"),
    ("asr-B-midchar-hit", "field/hit `\\B` (asr-B-midchar): two "
     "adjacent ASCII word characters -- \\B fires at the ENGINE-"
     "invented non-boundary position between them", "xy"),
    ("asr-lb-fixed-hit", "field/hit `(?<=é)x` (asr-lb-fixed) AND "
     "`(?<=a|é)x` (asr-lb-varwidth, the é branch): fixed "
     "CHARACTER width 1, BYTE width 2", "éx"),
    ("asr-lb-fixed-miss", "field/miss `(?<=é)x` (asr-lb-fixed): "
     "a different preceding character", "áx"),
    ("asr-lb-varwidth-a-hit", "field/hit `(?<=a|é)x` "
     "(asr-lb-varwidth, the 'a' branch): BYTE width 1 at the same "
     "CHARACTER width as the é branch", "ax"),
    ("asr-lb-neg-hit", "field/hit `(?<!日)本` (asr-lb-neg): "
     "本 preceded by 山, not 日", "山本"),
    ("asr-lb-neg-miss", "field/miss `(?<!日)本` (asr-lb-neg): "
     "本 preceded by 日 -- the negative lookbehind fails there",
     "日本"),
    ("asr-lb-class-hit", "field/hit `(?<=[\\x{400}-\\x{4FF}])\\s` "
     "(asr-lb-class): a Cyrillic word ending the run, followed by a "
     "space", "два дня"),
    ("asr-caret-ml-hit", "field/hit `(?m)^日` (asr-caret-ml): a "
     "second LINE beginning with 日",
     "line one\n日本語のテスト"),
    ("asr-dollar-ml-hit", "field/hit `(?m)語$` (asr-dollar-ml): "
     "the first line ENDS with 語",
     "こんにちは語\nline two"),
    ("asr-a-z-hit", "field/hit `\\A日本語\\z` (asr-a-z): "
     "the EXACT whole subject, true-start to true-end",
     "日本語"),
    ("asr-a-z-miss", "field/miss `\\A日本語\\z` (asr-a-z): "
     "trailing content after the run breaks the true-end anchor",
     "日本語abc"),

    # ---- family (f) PROPERTIES (prp-*), 15 subjects, 11 members -------
    # (prp-ingreek is the REFUSAL witness, utf8_set_v1.md 5(f)/9: a
    # compile-axis `did-not-compile` row on every engine, no match rows
    # -- no subject is typed for it, the same "legal today" pattern
    # `bench/bounded`'s 65535-cap rung sets, KB-4.)
    ("prp-l-hit", "field/hit `\\p{L}+` (prp-l): one letter from each of "
     "four scripts, cross-script", "aé日б"),
    ("prp-l-miss", "field/miss `\\p{L}+` (prp-l): digits only, no "
     "letter present", "123"),
    ("prp-lu-hit", "field/hit `\\p{Lu}` (prp-lu): an uppercase Latin-1 "
     "Supplement letter", "Á"),
    ("prp-lu-miss", "field/miss `\\p{Lu}` (prp-lu): lowercase only",
     "abc"),
    ("prp-n-hit", "field/hit `\\p{N}+` (prp-n): non-ASCII digits -- the "
     "positive twin of cls-d-ascii's designed near-miss",
     "٤٥٦"),
    ("prp-notl-hit", "field/hit `\\P{L}+` (prp-notl): digits present "
     "(a non-letter run exists)", "123abc"),
    ("prp-notl-miss", "field/miss `\\P{L}+` (prp-notl): letters only, "
     "no non-letter character anywhere", "abc"),
    ("prp-zs-hit", "field/hit `\\p{Zs}` (prp-zs): U+00A0 NO-BREAK "
     "SPACE, the positive twin of cls-s-nbsp's near-miss",
     "x y"),
    ("prp-greek-scx-witness", "field/edge `\\p{Greek}` (prp-greek, "
     "Script | Script_Extensions) vs `\\p{sc=Greek}` (prp-greek-sc, "
     "Script alone): Greek alpha carries U+0342 COMBINING GREEK "
     "PERISPOMENI, the stable Script_Extensions flipper this set "
     "authors AROUND U+00B7 (the confirmed version-sensitive point, "
     "utf8_set_v1.md 8.5/F-S1) -- both spellings HIT on the base "
     "letter; the oracle (U5) settles whether they diverge on the "
     "combining mark alone", "ᾶ"),
    ("prp-l-anchored-hit", "field/hit `^\\p{L}{4}$` (prp-l-anchored): "
     "exactly 4 letters", "abcd"),
    ("prp-l-anchored-miss", "field/miss `^\\p{L}{4}$` (prp-l-anchored): "
     "3 letters, one short", "abc"),
    ("prp-cyrillic-hit", "field/hit `\\p{Cyrillic}+` (prp-cyrillic): "
     "the strongest script filter in the set, two lead bytes",
     "москва"),
    ("prp-han-hit", "field/hit `\\p{Han}+` (prp-han): pure kanji, no "
     "kana admixture", "日本語"),
    ("prp-han-miss", "field/miss `\\p{Han}+` (prp-han): pure katakana "
     "-- kana is NOT Han, so no run can match",
     "アイウ"),
    ("prp-latin-hit", "field/hit `\\p{Latin}+` (prp-latin): spans the "
     "ASCII / Latin-1-Supplement boundary in one property",
     "café"),

    # ---- the floor: `~`, one literal ASCII byte -------------------
    ("floor-hit", "field/hit the floor byte '~', per-call overhead "
     "control -- never inside a multi-byte sequence (0x7E cannot be a "
     "UTF-8 continuation or lead byte)", "~"),
)

N_FAMILY = 90
N_TOTAL = 91


def build():
    seen = set()
    for sid, desc, text in SUBJECTS:
        assert sid not in seen, sid
        seen.add(sid)
        assert "\t" not in desc, sid
        body = text.encode("utf-8")
        ut.decode_gate(body)  # every real subject passes the same gate
        assert len(body) <= MAX_LINE, (sid, len(body))
    assert len(SUBJECTS) == N_TOTAL, (
        "expected %d subjects (90 family + 1 floor), got %d"
        % (N_TOTAL, len(SUBJECTS)))
    return SUBJECTS


def _check_decode_gate_has_teeth():
    """THE NEGATIVE-ARM CONTROL (utf8_set_v1.md 4.1, a stated requirement
    of this lane): a mid-character-truncated fixture must FAIL the decode
    gate. Built by slicing a REAL multi-byte corpus at a raw byte offset
    that lands inside a character -- the exact failure mode the size-
    fitting boundary rule exists to prevent -- bypassing
    `_trim_to_char_boundary` on purpose."""
    # Deliberately ends on a 3-byte CJK character (never on the ASCII pad
    # `text()` may append), so `[:-1]` is guaranteed to cut that character
    # in half rather than merely drop a trailing pad byte.
    good = ut.text(256, 0xDEC0DE, "cjk") + "日".encode("utf-8")
    ut.decode_gate(good)  # the control: well-formed data passes
    truncated = good[:-1]  # one byte short of the trailing 3-byte 日
    try:
        ut.decode_gate(truncated)
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError(
            "decode gate has no teeth: a mid-character-truncated fixture "
            "(%d -> %d bytes, cjk corpus) was NOT rejected"
            % (len(good), len(truncated)))


def main():
    check = "--check" in sys.argv
    subjects = build()
    _check_decode_gate_has_teeth()
    if check:
        if not os.path.isdir(OUT) or not os.path.isfile(MANIFEST):
            print("gen_subjects --check: FAIL (no subjects/ or manifest.tsv "
                  "-- run without --check first)")
            return 1
        ok = True
        with open(MANIFEST, encoding="utf-8") as f:
            committed = f.read()
        rendered = _render(subjects)
        if committed != rendered:
            print("gen_subjects --check: FAIL (manifest.tsv does not "
                  "reproduce byte for byte)")
            ok = False
        for sid, _desc, text in subjects:
            path = os.path.join(OUT, sid + ".bin")
            body = text.encode("utf-8")
            if not os.path.isfile(path) or open(path, "rb").read() != body:
                print("gen_subjects --check: FAIL (%s does not reproduce)"
                      % sid)
                ok = False
        if ok:
            print("gen_subjects --check: OK (%d subjects, decode gate "
                  "negative-arm control passed)" % len(subjects))
        return 0 if ok else 1
    os.makedirs(OUT, exist_ok=True)
    for sid, _desc, text in subjects:
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(text.encode("utf-8"))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write(_render(subjects))
    sizes = [len(t.encode("utf-8")) for _s, _d, t in subjects]
    print("gen_subjects: %d subjects (%d family + 1 floor; %d B, %d..%d) "
          "-> %s, manifest -> %s (decode gate negative-arm control passed)"
          % (len(subjects), N_FAMILY, sum(sizes), min(sizes), max(sizes),
             OUT, MANIFEST))
    return 0


def _render(subjects):
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, desc, text in subjects:
        body = text.encode("utf-8")
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(), desc,
            ut.periodic_field(body)))
    return "\n".join(rows) + "\n"


if __name__ == "__main__":
    sys.exit(main())
