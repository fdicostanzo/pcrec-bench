# b148probs report -- L6 problem statements (recursion, callouts, netstr)

Lane b148probs, branch lane/b148probs (from lane/b148land2). Docs + three small sample TSVs; nothing timed, nothing downloaded, ~/pcrec untouched. Files (all under `bench/unusual/assists/problems/`, plus the row in `assists/CLAUDE.md`): `recursion.md` + `recursion-samples.tsv`, `callouts.md` + `callouts-samples.tsv`, `netstr.md` + `netstr-samples.tsv`.

## What each statement covers

- **recursion.md** (cscan, wild-sexp-balanced, wild-json-validate; RE2, rust-regex, Vectorscan). Each member as a language: cscan's token/splice/depth rules restated from `unusual_lib.ref_scan` (no engine API, no pattern text of the pcrec file beyond the rules), the sexp leftmost-balanced-group rule, the JSON grammar written out with the pattern's quirks (fraction/exponent not consumed unless complete, raw bytes >= 0x7f in strings, `\A` = subject start). Call shape: `(subject, start)`, `\G` anchoring for cscan, O(segment) not O(tail), the driver's find-all loop for the `wild-*` throughput count. Tokens `n` / `m:s,e` / `m:s,e;b,c`; no refusal or give-up token (an assisted host is unbounded by construction, 6.5; engine limits are the shim's). "What the engine must still do": the regular parts through the engine's matcher, host code only for pairing (counter / explicit stack); no host recursion, no depth cap (subjects nest ~10^5).
- **callouts.md** (co-luhn, co-isbn, co-member; RE2, rust-regex, Vectorscan). Candidate pattern + predicate in words (Luhn, ISBN-13 weights, set membership), the first-passing-candidate semantics with the restart at candidate start + 1, the whole-subject CONTEXT RULE for `\b` (a restart on a slice is wrong; sample rows cover it), tokens, what fires when (`fires_first`, `fires_all` = predicate evaluations), find-all loop. The self-test set for co-member is inline (12 names, disjoint from `values/users.tsv`).
- **netstr.md** (co-netstr; libpcre2, Oniguruma, RE2, rust-regex, Vectorscan). The netstring language; Shape A (libpcre2/Oniguruma): the note's proposed pattern `(\d{1,9}):(?>(?s:.)*?(?C4)),` / `(?{4})`, the callee `netstr-end` stated as a contract ("pass iff run length == value of group 1") and said to be AUTHORED BY THE BLIND AUTHOR (P3; L5's copy provisional); Shape B (RE2/rust/Vectorscan): engine for `(\d{1,9}):`, host jump + `,` check. The failed-callout-is-not-an-abort trap, the start-inside-a-digit-run trap, the fire count as a check not a contract, no cross-arm subtraction.

## Samples: counts, derivation, disjointness

| file | rows | breakdown |
|---|---|---|
| recursion-samples.tsv | 125 | cscan 44 (36 match / 8 `n`), wild-sexp-balanced 25, wild-json-validate 56 (17 / 39) |
| callouts-samples.tsv | 48 | 16 per member |
| netstr-samples.tsv | 27 | 18 match / 9 `n` |

Derivation: `gen_samples.py` (below; run from /var/tmp, not committed as a file because the brief allowed only the six paths). Hand-written edge cases plus generated ones from FRESH seeds, all strings `b148probs-*` (none used by any bench/unusual generator). Expected tokens are the **libpcre2 10.46 oracle** (`unusual_lib.Rx`, default options, the member's pattern from `members.py`; callout members with the Python callee of `unusual_lib`, netstr with the `co-netstr-assist` pattern), each CHECKED against an independent reference, every disagreement aborts: cscan vs `ref_scan` (44/44), sexp vs `sexp_first` stack scan (token and find-all count, 25/25), JSON vs a new iterative grammar checker in the generator that shares nothing with the pattern or `json.loads` (56/56, plus whole-subject span), callouts vs a host loop "twin search, predicate, restart at start+1" (token, find-all count, fires_first, fires_all, 48/48), netstr vs `netstr_first`/`host_find_all` (token span and count, 27/27).

Disjointness (every row checked, 0 failures): the whole subject is not equal to any of the 161 short subjects (`gen_subjects.short_subjects()`) or any manifest sha (`manifest.tsv`, `manifest_throughput.tsv`); for cscan the segment bytes `subject[start:end]` are not equal to any seg-s / seg-l segment (regenerated in memory) or any of the 4,971 SQLite bodies; for sexp/json/luhn/isbn/member/netstr the subject (when >= 6 bytes) is not a substring of the family's 1.2 MB generated throughput text (a superset prefix of the held-out 1 MB subject). First run found 23 collisions (the obvious `()`, `{}`, `{a:1}`, `[NaN]`, ...); those cases were respelled and the generated ones re-drawn until clean. The co-member sample set shares no name with `values/users.tsv`. The vars stream subjects are not touched.

## Open points for the manager (judgement calls I made in the statements)

1. **"The engine must still do"**: the note (3.0, 5) says only "host tokenizing loop + depth counter"; I wrote the rule that the regular parts go through the engine's matcher and a design that never calls the engine is `not-idiomatic`. A pure host scanner is otherwise the shortest assist and would measure the host language. Confirm or relax (recursion.md section 1, callouts.md section 1, netstr.md section 1).
2. **Setup vs clock**: the statements say the assist's fixed patterns are compiled once at setup, outside the clock (vars.md puts compile INSIDE because values vary; here they do not). Not stated in the note; the L4 shim's `calls` mode decides.
3. **Callout predicate / member set supplied or authored?** RULES.md says the shared callees and their wrappers are outside the count, which could make the Luhn/ISBN/set predicate free for an assisted engine through a wrapper. callouts.md leaves it to the lane's brief ("if your brief says supplied...").
4. **Netstr Shape A wrapper**: the statement says the author writes the callee against the engine's own callout argument; whether a `wrappers` fence is allowed around it is the brief's call.
5. **cscan sample vs note 5.4**: 5.4 says cscan's public sample is `gen_cscan.py`'s 76 cases, but 73 of them are the held-out short subjects `cs-00..`; I used 44 fresh cases (incl. start > 0, refusals, splices, digraphs) instead, per this brief.
6. `fires_*` for netstr come from libpcre2's default-option run, so no-match rows with 0 fires reflect its start optimization (said so in netstr.md section 3).

## Appendix: gen_samples.py (the exact generator; run `python3 -I gen_samples.py <worktree> [--check]`)

```python
#!/usr/bin/env python3
"""gen_samples.py (lane b148probs; kept in b148probs_report.md, not in the tree)

Writes recursion-samples.tsv, callouts-samples.tsv, netstr-samples.tsv under
<worktree>/bench/unusual/assists/problems/. Every expected token is the
libpcre2 10.46 oracle (bench/unusual/unusual_lib.py, default options) and is
CHECKED against an independent host reference; every sample is CHECKED
disjoint from the held-out data. Seeds are the strings "b148probs-*", none of
which any bench/unusual generator uses.

    python3 -I gen_samples.py WORKTREE [--check]
"""
import os
import sys

W = sys.argv[1]
U = os.path.join(W, "bench", "unusual")
OUT = os.path.join(U, "assists", "problems")
sys.path.insert(0, U)
sys.path.insert(0, W)
import members as MB            # noqa: E402
import unusual_lib as L          # noqa: E402
import unusual_text as T         # noqa: E402
import gen_subjects as GS        # noqa: E402
import gen_streams as GST        # noqa: E402

PAT = {m.id: m.text for m in MB.members()}
FAILS = []


def need(ok, what):
    if not ok:
        FAILS.append(what)


def tok(span, g1=None):
    if span is None:
        return "n"
    s = "m:%d,%d" % span
    if g1 is not None:
        s += ";%d,%d" % g1
    return s


# ---------------------------------------------------------------- held-out
SHORT = {b for _i, b, _d in GS.short_subjects()}
SEGS = set()
for _seed, _n in ((GST.STREAMS[0][1], 256), (GST.STREAMS[1][1], 4096)):
    data, calls = T.segment_stream(_seed, _n)
    for off, ln, _r in calls:
        SEGS.add(data[off:off + ln])
for s in GST.sqlite_bodies():
    SEGS.add(s)
ONE_MB = 1000000
HELD_TEXT = {
    "luhn": T.luhn_text(ONE_MB + 200000), "isbn": T.isbn_text(ONE_MB + 200000),
    "member": T.member_text(ONE_MB + 200000), "netstr": T.netstr_text(ONE_MB + 200000),
    "sexp": T.sexp_text(ONE_MB + 200000), "json": T.json_big(ONE_MB + 200000),
}
MAN = {}
for f in ("manifest.tsv", "manifest_throughput.tsv"):
    for line in open(os.path.join(U, f)).read().splitlines()[1:]:
        MAN[line.split("\t")[2]] = line.split("\t")[0]
import hashlib  # noqa: E402


def disjoint(subject, kind, what, segment=None):
    need(subject not in SHORT, "%s equals a held-out short subject" % what)
    need(hashlib.sha256(subject).hexdigest() not in MAN, "%s equals a manifest subject" % what)
    if segment is not None:
        need(segment not in SEGS, "%s segment equals a held-out stream segment" % what)
    if kind in HELD_TEXT and len(subject) >= 6:
        need(subject not in HELD_TEXT[kind], "%s is a substring of a held-out %s text" % (what, kind))


def hexs(b):
    return b.hex()


def rep(b):
    return repr(b).replace("\t", "\\t")


# ---------------------------------------------------------------- cscan
def cscan_cases():
    rng = L.Rng("b148probs-cscan")
    c = []

    def add(label, subj, start=0):
        c.append((label, subj, start))
    add("plain", b"(?{ y = 2; })")
    add("plain-offset", b"zz\n(?{ y = 2; })tail", 3)
    add("not-at-start", b"xx(?{ y = 2; })", 0)
    add("empty-body", b"(?{})\n")
    add("blank-body", b"(?{ })")
    add("nested-3", b"(?{ if (a) { b(); { c; { d; } } } })")
    add("digraph", b"(?{ int f() <% return 0; %> })")
    add("digraph-mixed", b"(?{ { y; %> })")
    add("digraph-brace-then-pct", b"(?{ <% y; } })")
    add("close-in-string", b'(?{ s = "}}"; })')
    add("close-in-char", b"(?{ ch = '}' + 1; })")
    add("escaped-quote", b'(?{ s = "b\\"}"; })')
    add("block-comment", b"(?{ /* } } */ x; })")
    add("line-comment", b"(?{ x; // }\n y; })")
    add("line-comment-eof", b"(?{ x; // no newline, no close")
    add("unterminated-block-comment", b"(?{ x; /* never closed })")
    add("unterminated-string", b'(?{ x = "abc; })')
    add("raw-newline-in-string", b'(?{ x = "ab\ncd"; })')
    add("spliced-newline-in-string", b'(?{ x = "ab\\\ncd"; })')
    add("splice-in-ident", b"(?{ ab\\\ncd = 1; })")
    add("splice-before-close", b"(?{ y; \\\n\\\n})")
    add("splice-in-comment-end", b"(?{ /* c *\\\n/ x; })")
    add("splice-line-comment", b"(?{ // c \\\n } still comment\n x; })")
    add("splice-in-digraph", b"(?{ <\\\n% y; %\\\n> })")
    add("digit-separator", b"(?{ n = 1'000'000; })")
    add("char-after-number", b"(?{ n = 7 'a'; })")
    add("pp-number-exp", b"(?{ f = 1e+5 + 0x1p-3; })")
    add("dot-number", b"(?{ f = .5e+3; })")
    add("high-bytes", b"(?{ \xc3\xa9t\xc3\xa9 = 1; })")
    add("less-than", b"(?{ if (a < b && c % d > e) x; })")
    add("division", b"(?{ q = a / b / c; })")
    add("extra-closer", b"(?{ } })")
    add("close-not-followed-by-paren", b"(?{ x; }]")
    add("close-at-eof", b"(?{ yy; }")
    add("paren-in-string", b'(?{ p = ")"; })')
    add("two-segments-first", b"(?{ a; })(?{ b; })")
    add("two-segments-second", b"(?{ a; })(?{ b; })", 9)
    add("tail-after", b"(?{ a; }) trailing text with } and )")
    for k in range(6):
        seg, _r = T.c_segment(rng, rng.between(40, 300))
        pre = T.filler(rng, 5, 60)
        post = T.filler(rng, 5, 60)
        add("generated-%d%s" % (k + 1, "-refused" if _r else ""), pre + seg + post, len(pre))
    rows = []
    for i, (label, subj, start) in enumerate(c):
        orc = L.Rx(PAT["cscan"]).search(subj, start)
        ref = L.ref_scan(subj, start)
        o_tok = "n" if orc is None else tok(orc[0], orc[1][0])
        r_tok = "n" if ref is None else tok((ref[0], ref[1]), (ref[2], ref[3]))
        need(o_tok == r_tok, "cscan %s: oracle %s != reference %s" % (label, o_tok, r_tok))
        rowseg = subj[start:] if ref is None else subj[start:ref[1]]
        disjoint(subj, "", "cscan-%s" % label, segment=rowseg)
        rows.append(("cscan-%02d" % (i + 1), "cscan", subj, start, o_tok, "-", label))
    return rows


# ---------------------------------------------------------------- sexp
def sexp_cases():
    rng = L.Rng("b148probs-sexp")
    c = [
        ("one-form", b"(alpha beta)"), ("flat-after-prefix", b"say (alpha beta) now"),
        ("nested", b"(a (b (c d)) e)"), ("empty", b"(  )"), ("two-forms", b"(a)(b) (c)"),
        ("unclosed-outer", b"(a (b c) d"), ("unclosed-outer-2", b"((a b) (c"),
        ("stray-closer-first", b"a) b) (c d)"), ("only-closers", b"))) x"),
        ("only-openers", b"((( x"), ("no-parens", b"nothing here at all"), ("empty-subject", b""),
        ("deep-9", b"(" * 9 + b"z" + b")" * 9), ("deep-9-short-1", b"(" * 9 + b"z" + b")" * 8),
        ("deep-9-short-1-tail", b"(" * 9 + b"z" + b")" * 8 + b" (q)"),
        ("interleaved", b")(x(y)z)("), ("multi-line", b"(def f\n  (g 1\n    (h 2)))\n(f)\n"),
        ("paren-in-string", b'(say "a ) b")'), ("adjacent-groups", b"((a)(b))(c)"),
        ("brackets-ignored", b"[a (b) c] {d}"), ("nul-and-high", b"(a\x00\xff (b))"),
    ]
    k = 0
    while k < 4:
        form = T.sexp_form(rng, rng.between(2, 6), 0)
        pre = rng.choice([b"", b") ", b"(", b"x "])
        subj = pre + form + rng.choice([b"", b" (tail)", b")"])
        if len(subj) < 8 or subj in HELD_TEXT["sexp"]:
            continue
        k += 1
        c.append(("generated-%d" % k, subj))
    rows = []
    for i, (label, subj) in enumerate(c):
        rx = L.Rx(PAT["wild-sexp-balanced"])
        first, count = rx.find_all(subj)
        ref = L.host_find_all(L.sexp_first, subj)
        need(first == ref[0] and count == ref[1], "sexp %s: oracle %s/%s != reference %s" % (label, first, count, ref))
        disjoint(subj, "sexp", "sexp-%s" % label)
        rows.append(("wild-sexp-balanced-%02d" % (i + 1), "wild-sexp-balanced", subj, 0, tok(first), str(count), label))
    return rows


# ---------------------------------------------------------------- json
WS = b"\t\n\r "


def json_host(s):
    """Independent iterative checker of the validator's GRAMMAR (not of RFC 8259)."""
    n = len(s)
    i = 0
    stack = []                     # b"[" or b"{"
    expect = "value"

    def ws(j):
        while j < n and s[j] in WS:
            j += 1
        return j

    def number(j):
        if j < n and s[j] == 45:
            j += 1
        if j < n and s[j] == 48:
            j += 1
        elif j < n and 49 <= s[j] <= 57:
            while j < n and 48 <= s[j] <= 57:
                j += 1
        else:
            return -1
        if j + 1 < n and s[j] == 46 and 48 <= s[j + 1] <= 57:
            j += 1
            while j < n and 48 <= s[j] <= 57:
                j += 1
        if j < n and s[j] in b"eE":
            k = j + 1
            if k < n and s[k] in b"+-":
                k += 1
            if k < n and 48 <= s[k] <= 57:
                while k < n and 48 <= s[k] <= 57:
                    k += 1
                j = k
        return j

    def string(j):
        if j >= n or s[j] != 34:
            return -1
        j += 1
        while j < n:
            c = s[j]
            if c == 34:
                return j + 1
            if c < 0x20:
                return -1
            if c == 92:
                if j + 1 >= n:
                    return -1
                d = s[j + 1]
                if d in b'"\\bfnrt/':
                    j += 2
                elif d == 117 and j + 5 < n + 0 and all(x in b"0123456789abcdefABCDEF" for x in s[j + 2:j + 6]) and len(s[j + 2:j + 6]) == 4:
                    j += 6
                else:
                    return -1
            else:
                j += 1
        return -1

    while True:
        i = ws(i)
        if expect == "value":
            if i >= n:
                return False
            c = s[i]
            if c == 91:
                i = ws(i + 1)
                if i < n and s[i] == 93:
                    i += 1
                    expect = "after"
                else:
                    stack.append(91)
                continue
            if c == 123:
                i = ws(i + 1)
                if i < n and s[i] == 125:
                    i += 1
                    expect = "after"
                else:
                    stack.append(123)
                    expect = "key"
                continue
            if c == 34:
                j = string(i)
            elif s[i:i + 4] == b"true" or s[i:i + 4] == b"null":
                j = i + 4
            elif s[i:i + 5] == b"false":
                j = i + 5
            else:
                j = number(i)
            if j < 0:
                return False
            i = j
            expect = "after"
        elif expect == "key":
            j = string(i)
            if j < 0:
                return False
            i = ws(j)
            if i >= n or s[i] != 58:
                return False
            i += 1
            expect = "value"
        else:                                   # after a value
            if not stack:
                return i >= n
            if i >= n:
                return False
            c = s[i]
            if c == 44:
                i += 1
                expect = "key" if stack[-1] == 123 else "value"
            elif (c == 93 and stack[-1] == 91) or (c == 125 and stack[-1] == 123):
                stack.pop()
                i += 1
            else:
                return False


def json_cases():
    rng = L.Rng("b148probs-json")
    c = [
        ("empty-object", b"{ }"), ("empty-array", b"[ ]"), ("object-two", b'{"p":1,"q":[true,null]}'),
        ("number-forms", b"[0,-0,12,-3.25,1E+5,2e-3,0.5e0]"), ("string-escapes", b'["a\\tb\\/c\\\\d\\"e\\u00Ff\\uABcd"]'),
        ("scalar-number", b" -17 "), ("scalar-string", b'"just a string"'), ("scalar-keyword", b"\tnull\n"),
        ("trailing-newline", b'{"a":[1,2,3]}\n'), ("crlf-inside", b'{\r\n "a" :\r\n [ 1 ,\r\n 2 ]\r\n}'),
        ("duplicate-keys", b'{"k":1,"k":2}'), ("high-bytes-in-string", b'["\xc3\xa9\xff"]'),
        ("deep-array-300", b"[" * 300 + b"0" + b"]" * 300),
        ("deep-array-300-short", b"[" * 300 + b"0" + b"]" * 299),
        ("deep-object-60", b'{"a":' * 60 + b"1" + b"}" * 60),
        ("empty-subject", b""), ("only-spaces", b"   "), ("two-values", b"1 2"), ("value-then-junk", b'{"a":1} x'),
        ("trailing-comma-array", b"[1,2,]"), ("trailing-comma-object", b'{"b":2,}'), ("leading-comma", b"[,1]"),
        ("missing-colon", b'{"a" 1}'), ("missing-comma", b'["a" "b"]'), ("unquoted-key", b"{b:1}"),
        ("single-quotes", b"['x']"), ("leading-zero", b"[012]"), ("minus-zero-zero", b"-00"),
        ("plus-sign", b"+1"), ("bare-dot", b"[.5]"), ("dot-no-digit", b"[1.]"), ("exp-no-digit", b"[1e]"),
        ("hex", b"[0x10]"), ("nan", b"[NaN, 1]"), ("infinity", b"-Infinity"), ("capital-true", b"[True]"),
        ("truncated-keyword", b"[tru]"), ("keyword-glued", b"[truefalse]"),
        ("control-in-string", b'["a\x1fb"]'), ("nul-in-string", b'["a\x00b"]'), ("raw-tab-in-string", b'["a\tb"]'),
        ("bad-escape", b'["\\q"]'), ("short-unicode", b'["\\u12"]'), ("non-hex-unicode", b'["\\u12G4"]'),
        ("unterminated-string", b'["abc'), ("unterminated-array", b"[1,2"), ("extra-closer", b"[1]]"),
        ("mismatched", b"[1}"), ("mismatched-2", b'{"a":1]'), ("nul-between", b"[1,\x002]"),
    ]
    # a few generated well-formed documents, and one broken copy of each
    k = 0
    while k < 3:
        doc = T.json_value(rng, 3)
        if doc[:1] not in (b"[", b"{"):
            doc = b"[" + doc + b"]"
        cut = doc[:-1] if len(doc) > 2 else doc + b","
        if len(doc) < 12 or doc in HELD_TEXT["json"] or cut in HELD_TEXT["json"]:
            continue
        k += 1
        c.append(("generated-%d" % k, doc))
        c.append(("generated-%d-broken" % k, cut))
    rows = []
    for i, (label, subj) in enumerate(c):
        rx = L.Rx(PAT["wild-json-validate"])
        first, count = rx.find_all(subj)
        host = json_host(subj)
        need((first is not None) == host, "json %s: oracle %s != host grammar %s" % (label, first, host))
        need(first is None or first == (0, len(subj)), "json %s: span %s is not the whole subject" % (label, first))
        disjoint(subj, "json", "json-%s" % label)
        rows.append(("wild-json-validate-%02d" % (i + 1), "wild-json-validate", subj, 0, tok(first), str(count), label))
    return rows


# ---------------------------------------------------------------- callouts
SAMPLE_USERS = [b"mona", b"nick", b"olga", b"pete", b"quinn", b"rhea", b"sam", b"tina", b"uma", b"vic", b"log-shipper", b"ci_runner"]
TWIN = {"luhn": rb"\b(\d{13,19})\b", "isbn": rb"\b(97[89]\d{10})\b", "member": rb"\buser=(\w++)"}
PRED = {"luhn": L.luhn_ok, "isbn": L.isbn13_ok, "member": lambda g: g in SAMPLE_USERS}


def host_fires(kind, subject):
    """(first span+g1, fires on the first-match search, find-all count, fires over the find-all)
    by the assist's own loop: twin candidate, predicate, restart after the candidate's start."""
    rx = L.Rx(TWIN[kind])
    n = len(subject)

    def first(start):
        fires = 0
        pos = start
        while True:
            m = rx.search(subject, pos)
            if m is None:
                return None, fires
            fires += 1
            (s, e), g = m
            if PRED[kind](subject[g[0][0]:g[0][1]]):
                return ((s, e), g[0]), fires
            pos = s + 1
    f0, fires0 = first(0)
    pos, count, allfires = 0, 0, 0
    while pos <= n:
        got, fr = first(pos)
        allfires += fr
        if got is None:
            break
        count += 1
        pos = got[0][1] if got[0][1] > got[0][0] else got[0][0] + 1
    return f0, fires0, count, allfires


def native(kind, pattern, subject, fn):
    rx = L.Rx(pattern, callout=fn)
    got = rx.search(subject, 0)
    f1 = rx.fires
    rx2 = L.Rx(pattern, callout=fn)
    first, count = rx2.find_all(subject)
    return got, f1, count, rx2.fires


def callout_cases():
    rng = L.Rng("b148probs-callouts")
    users = SAMPLE_USERS
    lu_ok = lambda total, pre=b"": T.make_luhn(rng, total, pre)           # noqa: E731
    lu_bad = lambda total, pre=b"": T._bad(rng, T.make_luhn(rng, total, pre))   # noqa: E731
    v13, v16, v19 = lu_ok(13, b"3"), lu_ok(16, b"5"), lu_ok(19, b"6")
    b16, b15 = lu_bad(16, b"4"), lu_bad(15, b"3")
    n12, n20 = lu_ok(12), lu_ok(20)
    cases = {"luhn": [
        ("valid-16", b"paid by " + v16 + b" ok"), ("invalid-16", b"paid by " + b16 + b" ok"),
        ("first-fails", b"a " + b16 + b" b " + v16 + b" c"), ("many-fail-then-pass", b" ".join([b16, b15, lu_bad(13), lu_bad(19), v13])),
        ("both-valid-first-wins", v19 + b" " + v13), ("12-digits", b"id " + n12 + b" end"),
        ("20-digits", b"id " + n20 + b" end"), ("glued-letter-before", b"x" + v16 + b" y"),
        ("glued-letter-after", v16 + b"x"), ("hyphenated", b"-".join([v16[0:4], v16[4:8], v16[8:12], v16[12:16]])),
        ("at-subject-start-and-end", v13), ("empty-subject", b""), ("newline-separated", b"one " + b16 + b"\ntwo " + v16 + b"\n"),
        ("nul-around", b"\x00" + v16 + b"\x00"), ("punct-around", b"[" + v16 + b"]," + b"(" + b16 + b")"),
        ("adjacent-by-space", v16 + b" " + v16),
    ], "isbn": []}
    isbn = lambda pre: T.make_isbn(rng, pre)         # noqa: E731
    i978, i979 = isbn(b"978"), isbn(b"979")
    ibad = T._bad(rng, isbn(b"978"))
    cases["isbn"] = [
        ("valid-978", b"ISBN " + i978 + b" ok"), ("valid-979", b"ref " + i979), ("bad-check-digit", b"ISBN " + ibad),
        ("first-fails", b"ISBN " + ibad + b" or " + i978), ("many-fail-then-pass", b" ".join([ibad, T._bad(rng, i979), i979])),
        ("977-prefix", b"ISBN 9770000000002 ok"), ("10-digits", b"ISBN 0123456789 ok"),
        ("14-digits", b"ISBN " + i978 + b"0 ok"), ("12-digits", b"ISBN " + i978[:12] + b" ok"),
        ("glued-letters", b"x" + i978 + b"y"), ("hyphenated", i978[:3] + b"-" + i978[3:] ),
        ("subject-start-end", i979), ("empty-subject", b""), ("two-valid", i978 + b"\n" + i979 + b"\n"),
        ("nul-around", b"\x00" + i978 + b"\x00"), ("invalid-then-glued", ibad + b" " + b"1" + i978),
    ]
    cases["member"] = [
        ("member", b"GET /x user=mona ok"), ("not-member", b"GET /x user=zed ok"),
        ("first-fails", b"user=zed user=nick"), ("both-members-first-wins", b"user=sam user=vic"),
        ("many-fail-then-pass", b"user=a user=b user=c user=d user=rhea"), ("empty-name", b"user= x user=uma"),
        ("glued-before", b"xuser=mona"), ("hyphen-stops-name", b"user=log-shipper"), ("underscore-name", b"user=ci_runner"),
        ("prefix-of-member", b"user=mon"), ("longer-than-member", b"user=monas"), ("case-matters", b"user=Mona"),
        ("subject-start-end", b"user=tina"), ("empty-subject", b""), ("nul-after-name", b"user=pete\x00 user=olga"),
        ("repeated-prefix", b"user=user=quinn"),
    ]
    rows = []
    callee_for = lambda kind: (lambda f: L.CONTINUE if PRED[kind](f.subject[f.caps[1][0]:f.caps[1][1]]) else L.FAIL)   # noqa: E731
    for kind, mid in (("luhn", "co-luhn"), ("isbn", "co-isbn"), ("member", "co-member")):
        for i, (label, subj) in enumerate(cases[kind]):
            got, f1, count, fall = native(kind, PAT[mid], subj, callee_for(kind))
            hf = host_fires(kind, subj)
            n_tok = "n" if got is None else tok(got[0], got[1][0])
            h_tok = "n" if hf[0] is None else tok(hf[0][0], hf[0][1])
            need(n_tok == h_tok, "%s %s: oracle %s != host %s" % (mid, label, n_tok, h_tok))
            need((f1, count, fall) == (hf[1], hf[2], hf[3]), "%s %s: native fires/count %s != host loop %s" % (mid, label, (f1, count, fall), hf[1:]))
            disjoint(subj, kind, "%s-%s" % (mid, label))
            rows.append(("%s-%02d" % (mid, i + 1), mid, subj, n_tok, str(count), str(f1), str(fall), label))
    return rows


# ---------------------------------------------------------------- netstr
def netstr_cases():
    rng = L.Rng("b148probs-netstr")
    ns = T.netstr
    junk = bytes(rng.choice(b"xyz,: \n\x00;0123") for _ in range(30))
    c = [
        ("one", ns(b"greetings")), ("empty-data", b"x 0:,"), ("two-adjacent", ns(b"ab") + ns(b"cdef")),
        ("after-prefix", b"log: " + ns(b"payload") + b" tail"), ("comma-in-data", ns(b"a,b,c")),
        ("colon-in-data", ns(b"k:v:w")), ("newline-and-nul-in-data", ns(b"l1\nl2\x00z")),
        ("data-looks-like-netstring", ns(b"3:abc,")), ("data-is-two-netstrings", ns(ns(b"x") + ns(b"yz"))),
        ("length-too-short", b"3:abcd,"), ("length-too-long", b"6:abcd,"), ("length-past-subject-end", b"8:xyz,"),
        ("wrong-terminator", b"4:abcd;"), ("missing-terminator", b"3:abc"), ("no-colon", b"12abc,"),
        ("no-digits", b":abc,"), ("leading-zeros", b"0005:hello,"), ("nine-digits", b"000000002:hi,"),
        ("ten-digits", b"0000000002:hi,"), ("start-inside-digit-run", b"77:5:world,"),
        ("start-inside-digit-run-2", b"123:xyz,"), ("bad-then-good", b"5:abc, then 4:good,"),
        ("huge-declared-then-good", b"999999999:" + ns(b"ok")), ("junk-only", junk),
        ("junk-then-netstring", junk + ns(b"after")), ("empty-subject", b""),
        ("signed-or-spaced-length", b"+3:abc, 3 :abc, 3:abc,"),
    ]
    rows = []
    fn = L.callee_for("netstr")
    for i, (label, subj) in enumerate(c):
        got, f1, count, fall = native("netstr", PAT["co-netstr-assist"], subj, fn)
        ref = L.host_find_all(L.netstr_first, subj)
        h_first = ref[0]
        n_span = None if got is None else got[0]
        need(n_span == h_first and count == ref[1], "netstr %s: oracle %s/%s != host %s" % (label, n_span, count, ref))
        disjoint(subj, "netstr", "netstr-%s" % label)
        t = "n" if got is None else tok(got[0], got[1][0])
        rows.append(("co-netstr-%02d" % (i + 1), "co-netstr", subj, t, str(count), str(f1), str(fall), label))
    return rows


def write(name, header, rows, fmt):
    lines = ["\t".join(header) + "\n"]
    for r in rows:
        lines.append("\t".join(fmt(r)) + "\n")
    data = "".join(lines).encode("ascii")
    path = os.path.join(OUT, name)
    if "--check" in sys.argv:
        have = open(path, "rb").read() if os.path.exists(path) else None
        print("%s: %d rows, %s" % (name, len(rows), "identical" if have == data else "DIFFERS"))
        return
    os.makedirs(OUT, exist_ok=True)
    open(path, "wb").write(data)
    print("wrote %s: %d rows" % (name, len(rows)))


def main():
    rec = cscan_cases() + sexp_cases() + json_cases()
    write("recursion-samples.tsv", ["case", "member", "subject_hex", "subject", "start", "expected", "findall", "note"], rec,
          lambda r: [r[0], r[1], hexs(r[2]), rep(r[2]), str(r[3]), r[4], r[5], r[6]])
    co = callout_cases()
    write("callouts-samples.tsv", ["case", "member", "subject_hex", "subject", "expected", "findall", "fires_first", "fires_all", "note"], co,
          lambda r: [r[0], r[1], hexs(r[2]), rep(r[2]), r[3], r[4], r[5], r[6], r[7]])
    nt = netstr_cases()
    write("netstr-samples.tsv", ["case", "member", "subject_hex", "subject", "expected", "findall", "fires_first", "fires_all", "note"], nt,
          lambda r: [r[0], r[1], hexs(r[2]), rep(r[2]), r[3], r[4], r[5], r[6], r[7]])
    print("checks failed: %d" % len(FAILS))
    for f in FAILS:
        print("  FAIL", f)
    return 1 if FAILS else 0


sys.exit(main())
```
