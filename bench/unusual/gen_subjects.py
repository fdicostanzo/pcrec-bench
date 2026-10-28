#!/usr/bin/env python3
"""gen_subjects.py -- bench/unusual's SHORT subjects (regime search_short, <= 1024 B).

    python3 -I bench/unusual/gen_subjects.py          # write subjects/ + manifest.tsv
    python3 -I bench/unusual/gen_subjects.py --check  # regenerate, diff manifest (+ files)

Typed cases for every member family; every one is run against every
non-vars pattern (the full cross product is the null control: a JSON document
is a `nomatch` for cscan and the other way round).

  cs-NN         pcrec's own 73 start-0 cscan cases (vendor/pcrec/gen_cscan.py's
                `C` table, hand-written rule expectations there), NN = table order
  cs-nest-<d>   `(?{ ` + `{`*d + ` x; ` + `}`*d + ` })` for d = 19, 20, 21, 30, 100:
                the Oniguruma nest-level-20 witnesses (design 6.3, E-1: declared
                silent-wrong BEFORE any run, NOTES.md)
  cs-define     `(?{x})DEFINE` (design 3.1: the variant answers as PCRE2 does)
  sx-*          S-expression cases for wild-sexp-balanced
  js-*          JSON documents, valid and invalid, for wild-json-validate
  lu-* is-* me-* ns-*   the callout members' cases, each with the FIRST-CANDIDATE-
                FAILS control (design 3.2 return-code mapping)
  x-*           mixed text (a log line carrying several candidates)

Subjects are ids only; descriptions say what each is for. Deterministic: the
few generated digit strings come from unusual_lib.Rng with the constants below.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import members as MB  # noqa: E402
import subjgen  # noqa: E402
import unusual_text as T  # noqa: E402
from unusual_lib import Rng, luhn_ok, isbn13_ok  # noqa: E402


def short_subjects():
    g = MB.check_cscan_source()
    rows = []
    for i, (lab, subj, _exp) in enumerate(g.C):
        rows.append(("cs-%02d" % i, subj.encode("latin-1"), "cscan case %d: %s" % (i, lab.replace("\t", " "))))
    for d in (19, 20, 21, 30, 100):
        rows.append(("cs-nest-%d" % d, T.nest_brace(d), "brace nesting depth %d (Oniguruma nest-level-20 witness)" % d))
    rows.append(("cs-define", b"(?{x})DEFINE", "the (?(DEFINE) witness: Onig's regex condition reads xDEFINEy as a match"))

    sx = [
        ("simple", b"(a b c)", "one flat form"),
        ("nested", b"(a (b c) (d (e f)))", "nested forms"),
        ("prefix", b"foo (bar baz) qux", "balanced group after a prefix"),
        ("empty", b"()", "the empty form"),
        ("two", b"(a) (b)", "two forms, the first wins"),
        ("define", b"(define (f x) (+ x (* 2 3)))", "a Scheme definition"),
        ("unbal-open", b"(a (b c)", "an unclosed outer form: the inner group is the leftmost balanced one"),
        ("unbal-open2", b"((a)", "same, minimal"),
        ("unbal-close", b"a) (b)", "a stray closer before a form"),
        ("none", b"no parentheses at all", "no parenthesis"),
        ("deep-12", b"(" * 12 + b"x" + b")" * 12, "depth 12, balanced"),
        ("deep-drop", b"(" * 12 + b"x" + b")" * 11, "depth 12 with one closer dropped (the near miss)"),
        ("string", b'(print "hi there")', "a string atom"),
        ("lone-open", b"(", "a single opener"),
        ("lone-close", b")", "a single closer"),
        ("multi", b"(defun sq (x)\n  (* x x))\n\n(sq 4)\n", "two top-level forms over lines"),
    ]
    for k, b, d in sx:
        rows.append(("sx-" + k, b, "S-expression case: " + d))

    js = [
        ("obj-empty", b"{}", "empty object"),
        ("arr-empty", b"[]", "empty array"),
        ("obj-1", b'{"a":1}', "one pair"),
        ("arr-nums", b"[1,2.5,-3e+10,0]", "number forms"),
        ("nested", b'{"k":[true,false,null,{"x":"y"}]}', "nested document"),
        ("str-esc", b'"str\\n\\u00e9\\"q"', "a string with escapes"),
        ("ws-num", b"  12  ", "a number padded with whitespace"),
        ("ws-doc", b'{"a" : [ 1 , 2 ] }\n', "whitespace everywhere, trailing newline"),
        ("bad-trail-arr", b"[1,]", "trailing comma in an array"),
        ("bad-trail-obj", b'{"a":1,}', "trailing comma in an object"),
        ("bad-squote", b"{'a':1}", "single quotes"),
        ("bad-leading0", b"01", "leading zero"),
        ("bad-missing-comma", b"[1 2]", "missing comma"),
        ("bad-pair", b'{"a"}', "a key without a value"),
        ("bad-word", b"nul", "a truncated literal"),
        ("bad-unterm", b'"abc', "an unterminated string"),
        ("bad-ctrl", b'"a\x01b"', "a raw control character in a string"),
        ("bad-trailing", b"[1]x", "garbage after the value"),
        ("bad-brace2", b'{"a":1}}', "an extra closer"),
        ("bad-nan", b"[NaN]", "a non-JSON constant"),
        ("bad-dot", b"1.", "a number ending in a dot"),
        ("bad-minus", b"-", "a lone minus"),
        ("bad-exp", b"[1e5e5]", "a doubled exponent"),
        ("bad-escape", b'{"a":"\\x"}', "an invalid escape"),
        ("bad-bare-key", b"{a:1}", "an unquoted key"),
        ("deep-arr", b"[" * 40 + b"1" + b"]" * 40, "forty nested arrays"),
        ("unicode-esc", b'["\\u0041\\u00e9"]', "valid unicode escapes"),
        ("bad-unicode-esc", b'["\\u00g9"]', "an invalid unicode escape"),
    ]
    for k, b, d in js:
        rows.append(("js-" + k, b, "JSON case: " + d))

    rng = Rng("short-callouts")
    L = T.make_luhn
    v13 = L(rng, 13, b"4")
    v16 = b"4111111111111111"
    v19 = L(rng, 19, b"6011")
    assert luhn_ok(v16) and luhn_ok(v13) and luhn_ok(v19)
    bad16 = b"4111111111111112"
    assert not luhn_ok(bad16)
    lu = [
        ("valid", b"card " + v16 + b" ok", "one valid 16-digit number"),
        ("invalid", b"card " + bad16 + b" bad", "one Luhn-invalid 16-digit number"),
        ("first-fails", b"a " + bad16 + b" b " + v16 + b" c", "FIRST candidate fails the callee, the second passes (return-code control)"),
        ("both-valid", b"x " + v13 + b" y " + v19 + b" z", "13 and 19 digits, both valid"),
        ("short", b"num 411111111111 here", "12 digits: below the quantifier floor"),
        ("long-20", b"x 41111111111111111111 y", "20 digits: no candidate (no boundary inside the run)"),
        ("embedded", b"id" + v16 + b"x", "digits glued to letters: no word boundary"),
        ("lines", b"order 17 paid\ncard " + v16 + b"\ncard " + bad16 + b"\ntotal 12.50\n", "a few log lines"),
    ]
    for k, b, d in lu:
        rows.append(("lu-" + k, b, "Luhn case: " + d))

    isb = T.make_isbn
    r2 = Rng("short-isbn")
    iv = b"9780306406157"
    assert isbn13_ok(iv)
    ib = b"9780306406158"
    assert not isbn13_ok(ib)
    iv2 = isb(r2, b"979")
    isbs = [
        ("valid", b"ISBN " + iv + b" end", "a valid ISBN-13"),
        ("invalid", b"ISBN " + ib + b" end", "a bad check digit"),
        ("first-fails", b"ISBN " + ib + b" then " + iv + b" end", "FIRST candidate fails the callee, the second passes"),
        ("979", b"ISBN " + iv2 + b" end", "a 979 prefix"),
        ("isbn10", b"ISBN 0306406152 end", "ten digits: not a candidate"),
        ("14", b"ISBN " + iv + b"4 end", "a 14-digit run: no boundary after 13"),
        ("not-97", b"ISBN 9770306406153 end", "977 is not a bookland prefix"),
    ]
    for k, b, d in isbs:
        rows.append(("is-" + k, b, "ISBN case: " + d))

    me = [
        ("alice", b"GET / user=alice ok", "a member"),
        ("mallory", b"GET / user=mallory ok", "not a member"),
        ("first-fails", b"user=mallory user=bob", "FIRST candidate not a member, the second is"),
        ("empty", b"user= x", "an empty name"),
        ("glued", b"xuser=alice", "no word boundary before user="),
        ("hyphen", b"user=alice-smith", "\\w++ stops at the hyphen: `alice` is a member"),
        ("case", b"user=Alice", "case matters"),
        ("two-members", b"user=carol and user=dave", "both members: the first is the answer"),
    ]
    for k, b, d in me:
        rows.append(("me-" + k, b, "membership case: " + d))

    ns = [
        ("simple", b"5:hello,", "a netstring"),
        ("bad-len", b"5:hell,", "declared 5, data is 4"),
        ("zero", b"0:,", "the empty netstring"),
        ("comma-data", b"3:a,b,", "a comma inside the data"),
        ("run-start", b"1234:abcd,", "start 0 declares 1234; the leftmost WORKING start is inside the digit run"),
        ("newline", b"3:a\nb,", "a newline inside the data"),
        ("multi", b"3:abc,4:defg,", "two netstrings"),
        ("none", b"no netstring here", "no digit"),
        ("short-data", b"9:abc,", "declared 9, subject ends"),
        ("nine", b"000000003:abc,", "nine digits"),
        ("ten", b"0000000003:abc,", "ten digits: only the start at offset 1 works"),
        ("junk-first", b"junk 12 and 3:abc, end", "a number without a colon, then a netstring"),
        ("no-comma", b"3:abc;", "wrong terminator"),
    ]
    for k, b, d in ns:
        rows.append(("ns-" + k, b, "netstring case: " + d))

    rows.append(("x-log", b"10.0.0.7 served in 12 ms user=bob card " + v16 + b" ISBN " + iv + b" ref 5:hello, ok (a (b)) {\"k\":1}\n",
                 "one line carrying a candidate for every family"))
    rows.append(("x-plain", b"the quick brown fox jumps over the lazy dog", "plain text, no candidates"))
    return rows


def main(argv):
    rows = short_subjects()
    seen = set()
    for sid, b, _d in rows:
        assert sid not in seen and len(b) <= 1024, sid
        seen.add(sid)
    return subjgen.run(rows, os.path.join(HERE, "subjects"), os.path.join(HERE, "manifest.tsv"), "--check" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
