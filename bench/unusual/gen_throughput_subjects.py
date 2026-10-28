#!/usr/bin/env python3
"""gen_throughput_subjects.py -- bench/unusual's LARGE subjects (regime throughput).

    python3 -I bench/unusual/gen_throughput_subjects.py          # write throughput/ + manifest_throughput.tsv
    python3 -I bench/unusual/gen_throughput_subjects.py --check

Two kinds, both applicable only to the patterns applies.tsv names:

  F3 PATHOLOGICALS (cscan family: one call at offset 0, first match; design 4.3)
    comment-5m          `(?{ /*` + 5 MB + `*/ })`
    literal-100k        a 100,000-character "..." literal
    nest-brace-<d>      `(?{ ` + `{`*d + ` x; ` + `}`*d + ` })`
    nest-paren-<d>      the same with parentheses: cscan treats them as plain
                        bytes (the no-recursion control for that depth), and
                        wild-sexp-balanced recurses d+1 levels through them
    nest-digraph-10k    `<%` x 10000 ... `%>` x 10000
    idents-1m           1 MB of identifiers and spaces
    splice-1m           a 1 MB identifier spliced after every byte
    define-witness      `(?{x})DEFINE`
    unterminated-5m     `(?{ /*` + 5 MB, no `*/` (NO match)
  depth labels: 128, 512, 1k = 1024, 2k = 2048, 8k = 8192, 10k = 10000,
  32k = 32768, 100k = 100000 (the manifest description states each depth).

  ONE LARGE TEXT PER OTHER FAMILY (~1 MB, first match + find-all count)
    sx-1m   js-1m   js-near-1m   co-luhn-1m   co-isbn-1m   co-member-1m   co-netstr-1m
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import subjgen  # noqa: E402
import unusual_text as T  # noqa: E402

RUNGS = [("128", 128), ("512", 512), ("1k", 1024), ("2k", 2048), ("8k", 8192),
         ("10k", 10000), ("32k", 32768), ("100k", 100000)]
ONE_MB = 1000000


def rows():
    yield ("comment-5m", T.comment_big(5000000), "F3: (?{ /* then 5 MB of comment body (body period 10), closed */ })")
    yield ("literal-100k", T.literal_big(100000), "F3: a 100,000-character string literal full of braces (body period 4)")
    for lab, d in RUNGS:
        yield ("nest-brace-" + lab, T.nest_brace(d), "F3: brace nesting depth %d (cscan recurses per level; the opener run is period 1)" % d)
    for lab, d in RUNGS:
        yield ("nest-paren-" + lab, T.nest_paren(d), "F3: parenthesis nesting depth %d (cscan: plain bytes; wild-sexp-balanced: recursion depth %d)" % (d, d + 1))
    yield ("nest-digraph-10k", T.nest_digraph(10000), "F3: digraph nesting depth 10000 (<% %>)")
    yield ("idents-1m", T.idents_big(ONE_MB), "F3: 1 MB of identifiers and spaces inside one segment")
    yield ("splice-1m", T.splice_big(ONE_MB), "F3: an identifier spliced (backslash-newline) after every byte, 1 MB (body period 3)")
    yield ("define-witness", b"(?{x})DEFINE", "F3: the (?(DEFINE) witness (design 3.1)")
    yield ("unterminated-5m", T.comment_big(5000000, close=False), "F3: (?{ /* then 5 MB (body period 10), never closed (NO match)")
    yield ("sx-1m", T.sexp_text(ONE_MB), "S-expression text: nested forms, comments, stray and unclosed parentheses between forms")
    js = T.json_big(ONE_MB)
    yield ("js-1m", js, "one valid JSON document, an array of nested objects")
    last = js.rstrip(b"\n")
    assert last.endswith(b"]")
    yield ("js-near-1m", last[:-1] + b"}\n", "the same document with the final ] replaced by } (fails at the last byte)")
    yield ("co-luhn-1m", T.luhn_text(ONE_MB), "log-like lines with 13-24 digit numbers: 30% Luhn-valid, 30% invalid, rest noise")
    yield ("co-isbn-1m", T.isbn_text(ONE_MB), "log-like lines with ISBN-13 candidates: valid, bad check digit, 10 digits, 15 digits")
    yield ("co-member-1m", T.member_text(ONE_MB), "access-log lines with user=<name>: 40% members, 40% unknown, 20% upper-case")
    yield ("co-netstr-1m", T.netstr_text(ONE_MB), "netstrings (70%), wrong-length netstrings (20%) and junk (10%)")


def main(argv):
    return subjgen.run(rows(), os.path.join(HERE, "throughput"), os.path.join(HERE, "manifest_throughput.tsv"), "--check" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
