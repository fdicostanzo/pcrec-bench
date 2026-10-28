#!/usr/bin/env python3
"""gen_vars_samples.py -- the PUBLIC SELF-TEST SAMPLE of the vars family (lane
L7; docs/design/unusual_set_v1.md 5.4: "others: 20 cases per member; the corpus
held out"). Written to assists/problems/vars-samples.tsv for the blinded
assist authors of L6; the held-out corpus is the five streams of gen_vars.py,
which no sample line may equal (checked here).

    python3 -I bench/unusual/gen_vars_samples.py            # write
    python3 -I bench/unusual/gen_vars_samples.py --check    # re-derive + diff + held-out disjointness

Each row: case, member, bindings (`name=hex|UNSET|EMPTY`, `;`-joined, a name
absent from the list is UNSET), line_hex, line (a Python bytes repr, for
reading), expected (`n` | `m:<s>,<e>` | `r`, line-relative). The expected
token is the libpcre2 oracle over the resolved + escaped pattern
(gen_vars.resolve), cross-checked against Python `re` over re.escape'd values;
a disagreement aborts. Nothing here names an engine's API.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_vars as GV  # noqa: E402
from unusual_lib import Rx  # noqa: E402

OUT = os.path.join(HERE, "assists", "problems", "vars-samples.tsv")
U, E = GV.UNSET, GV.EMPTY

TENANT = [
    ({"tenant": b"acme"}, b"acme-0042 ERROR disk full"),
    ({"tenant": b"acme"}, b"acme-0042 INFO all well"),
    ({"tenant": b"acme"}, b"acme-042 WARN three digits"),
    ({"tenant": b"acme"}, b"xacme-0042 ERROR not at the start"),
    ({"tenant": b"a.c"}, b"a.c-1234 WARN dot is a dot"),
    ({"tenant": b"a.c"}, b"abc-1234 WARN dot is not a wildcard"),
    ({"tenant": b"a+"}, b"a+-0001 ERROR plus is a plus"),
    ({"tenant": b"a+"}, b"aaa-0001 ERROR plus is not a repeat"),
    ({"tenant": b"(x|y)"}, b"(x|y)-0001 WARN group is literal"),
    ({"tenant": b"(x|y)"}, b"x-0001 WARN alternation is literal"),
    ({"tenant": E}, b"-0001 ERROR empty is a value"),
    ({"tenant": E}, b"acme-0001 ERROR empty is not acme"),
    ({"tenant": U}, b"acme-0001 ERROR unset refuses"),
    ({"tenant": U}, b"-0001 ERROR unset does not widen to empty"),
    ({"tenant": b"ACME"}, b"acme-0001 ERROR case matters here"),
    ({"tenant": b"a\x00b"}, b"a\x00b-0007 WARN a NUL byte in the value"),
    ({"tenant": b"a\x00b"}, b"ab-0007 WARN the NUL is not dropped"),
    ({"tenant": b"$1"}, b"$1-0001 ERROR dollar one"),
    ({"tenant": b"^t"}, b"^t-0001 ERROR caret"),
    ({"tenant": b"t\\d"}, b"t\\d-0001 WARN backslash d, not a digit class"),
]
ROUTE = [
    ({"prefix": U, "res": b"users", "fmt": U}, b"/api/v1/users"),
    ({"prefix": E, "res": b"users", "fmt": U}, b"/api/v1/users?page=2"),
    ({"prefix": b"api", "res": b"users", "fmt": U}, b"/api/v2/users.json#top"),
    ({"prefix": b"internal", "res": b"users", "fmt": U}, b"/internal/v3/users"),
    ({"prefix": b"internal", "res": b"users", "fmt": U}, b"/api/v3/users"),
    ({"prefix": U, "res": b"users", "fmt": E}, b"/api/v1/users.json"),
    ({"prefix": U, "res": b"users", "fmt": E}, b"/api/v1/users"),
    ({"prefix": U, "res": b"users", "fmt": b"x"}, b"/api/v1/users.json?q=1"),
    ({"prefix": U, "res": b"users", "fmt": b"x"}, b"/api/v1/users.jsonx"),
    ({"prefix": U, "res": b"items.list", "fmt": U}, b"/api/v1/items.list"),
    ({"prefix": U, "res": b"items.list", "fmt": U}, b"/api/v1/itemsXlist"),
    ({"prefix": U, "res": b"a+b", "fmt": U}, b"/api/v10/a+b"),
    ({"prefix": U, "res": b"a+b", "fmt": U}, b"/api/v10/aab"),
    ({"prefix": b"ex.tra", "res": b"orders", "fmt": U}, b"/ex.tra/v2/orders/9"),
    ({"prefix": b"ex.tra", "res": b"orders", "fmt": U}, b"/ex.tra/v2/orders/9"),
    ({"prefix": U, "res": U, "fmt": U}, b"/api/v1/users"),
    ({"prefix": b"api", "res": E, "fmt": U}, b"/api/v1/"),
    ({"prefix": U, "res": b"reports(2)", "fmt": b"y"}, b"/api/v1/reports(2).json"),
    ({"prefix": U, "res": b"users", "fmt": U}, b"/api/vX/users"),
    ({"prefix": b"v-1", "res": b"users", "fmt": U}, b"/v-1/v1/users?"),
]
TERM = [
    ({"term": b"error"}, b"an error occurred"),
    ({"term": b"error"}, b"an ERROR occurred"),
    ({"term": b"error"}, b"terrors abound"),
    ({"term": b"a.b"}, b"see a.b here"),
    ({"term": b"a.b"}, b"see axb here"),
    ({"term": b"c++"}, b"uses c++ daily"),
    ({"term": b"c++"}, b"uses c++x daily"),
    ({"term": b"x|y"}, b"a x|y b"),
    ({"term": b"x|y"}, b"a y b"),
    ({"term": b"(foo)"}, b"call x(foo)x now"),
    ({"term": b"[z]"}, b"index x[z]x ok"),
    ({"term": b"a\x00b"}, b"has a\x00b inside"),
    ({"term": b"a\x00b"}, b"has ab inside"),
    ({"term": b"$USD"}, b"price in x$USD today"),
    ({"term": b"caf\xc3\xa9"}, b"un caf\xc3\xa9x noir"),
    ({"term": b"caf\xc3\xa9"}, b"un CAF\xc3\x89 noir"),
    ({"term": E}, b"an error occurred"),
    ({"term": U}, b"an error occurred"),
    ({"term": b"Tail"}, b"at the TAIL end"),
    ({"term": b"back\\slash"}, b"a back\\slash b"),
]


def cases():
    out = []
    for member, table in (("va-tenant", TENANT), ("va-route", ROUTE), ("va-term", TERM), ("va-term-bang", TERM)):
        for i, (b, line) in enumerate(table, 1):
            out.append((member, i, b, line))
    return out


def token(member, b, line):
    text = GV.member_texts()[member]
    pat, pyp = GV.resolve(text, b), GV.resolve(text, b, esc=GV.esc_py)
    if (pat is None) != (pyp is None):
        raise SystemExit("%s %r: resolutions disagree on refusal" % (member, b))
    if pat is None:
        return "r"
    got = Rx(pat).search(line, 0)
    pm = re.compile(pyp).search(line)
    if (got is None) != (pm is None) or (got is not None and got[0] != pm.span()):
        raise SystemExit("%s %r %r: libpcre2 %r vs python re %r" % (member, b, line, got and got[0], pm and pm.span()))
    return "n" if got is None else "m:%d,%d" % got[0]


def bind_text(b):
    return ";".join("%s=%s" % (k, "UNSET" if v is U else "EMPTY" if v == E else v.hex()) for k, v in b.items())


def render():
    out = ["case\tmember\tbindings\tline_hex\tline\texpected\n"]
    for member, i, b, line in cases():
        out.append("%s-%02d\t%s\t%s\t%s\t%s\t%s\n" % (member, i, member, bind_text(b), line.hex(), repr(line).replace("\t", "\\t"),
                                                    token(member, b, line)))
    return "".join(out).encode("ascii")


def heldout_clash():
    """-> the sample (binding, line) pairs that also occur as a call of a
    held-out stream (the same line under a different binding is a different
    case: a route line such as /api/v1/users recurs by construction)."""
    held = set()
    for st in GV.build_all():
        for (off, ln, _bid, k) in st.calls:
            held.add((tuple(sorted(st.bindings[k][1].items(), key=lambda kv: kv[0])), st.data[off:off + ln]))
    return sorted({(bind_text(b), line) for _m, _i, b, line in cases()
                   if (tuple(sorted(b.items(), key=lambda kv: kv[0])), line) in held})


def main(argv):
    data = render()
    clash = heldout_clash()
    if clash:
        sys.stderr.write("sample lines also in a held-out stream: %r\n" % clash[:5])
        return 1
    if "--check" in argv:
        have = open(OUT, "rb").read() if os.path.exists(OUT) else None
        print("vars-samples.tsv: %d case(s), %d difference(s)" % (data.count(b"\n") - 1, 0 if have == data else 1))
        return 0 if have == data else 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(data)
    print("wrote %d cases, %s" % (data.count(b"\n") - 1, OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
