#!/usr/bin/env python3
"""gen_vars.py -- the caller-VARIABLES streams of bench/unusual (lane L7;
docs/design/unusual_set_v1.md 3.3, 7.1, 8; review r9 C6).

    python3 -I bench/unusual/gen_vars.py --report     # stream table + counts, writes nothing

This module is IMPORTED by gen_streams.py (which writes the streams, the call
lists, the bindings tables and the manifest rows) and by gen_expectations.py
(which derives the per-call expectations). It holds:

  * `resolve()` -- vars.md section 2/5 in PYTHON, independent of every assist
    and of pcrec: the five operators, `${!name}`, a default `word` that is
    LITERAL text (variables_pattern.md:305) and is escaped like a value, a
    backslash in a word making the next byte literal, UNSET (None) distinct
    from EMPTY (b""), and the REFUSAL of a bare `${n}` on UNSET and of
    `${n:?}` on UNSET/EMPTY. A value matches AS ITSELF (vars.md section 1):
    every byte not [A-Za-z0-9_] is escaped (`\\xHH` for controls and bytes
    >= 0x80, incl. 0x00; a backslash before ASCII punctuation otherwise).
    The nested chain `${a:-${b}}` is DROPPED from v0.1 (b UNSET is unspecified
    in vars.md; Q-C is open with pcrec): resolve() refuses to parse it.
  * `STREAMS` -- five deterministic value streams over LINES of log text.

THE CALL (the host contract the problem statement restates): a call is one
LINE of the stream's subject -- bytes [offset, offset + length) -- plus a
BINDING (name -> bytes | EMPTY | UNSET). The engine matches the member's
resolved pattern against that line ALONE (a line is its own subject: `^` is
the line's start, offsets in the result are LINE-RELATIVE), first match.
Result token per call: `n` | `m:<s>,<e>` | `r` (REFUSED by the variables rule:
nothing was attempted). The throughput denominator is the sum of the lines'
byte lengths (`segment_bytes` = `length` per call).

THE STREAMS (stream length FIXED across the d4/d64/d4096 ladder, P13):

  tenant-d4 / -d64 / -d4096   va-tenant, 16,384 calls, ROUND-ROBIN over d
                              tenant values (d distinct resolved patterns =
                              the MISS COUNT of a memoizing engine, exactly d)
  route-zipf                  va-route, 4,096 calls over 108 bindings drawn
                              zipf-s1.1 (prefix UNSET / EMPTY / `api` all
                              resolve to the SAME pattern: the memo key is the
                              resolved pattern, not the binding)
  term-zipf                   va-term AND va-term-bang (one stream, two
                              spellings), 4,096 calls over 49 bindings, zipf-
                              s1.1: metacharacters, 0x00, a high byte, EMPTY
                              and UNSET values (REFUSED by `:?`); lines put a
                              word byte beside a non-word-ended term so `\\b`
                              can hold, and the opposite beside a word-ended one
                              for the boundary-fails near-misses
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from unusual_lib import Rng  # noqa: E402

UNSET = None
EMPTY = b""

NAME_RE = re.compile(rb"[A-Za-z_][A-Za-z0-9_]*\Z")


class VarsSyntax(Exception):
    pass


def parse(text):
    """-> [('lit', bytes) | ('var', name, op, word_bytes)]; op in
    '', '-', ':-', '+', ':+', ':?'. `${!n}` parses as `${n}` (vars.md 2)."""
    out, lit, i, n = [], bytearray(), 0, len(text)
    while i < n:
        if text[i:i + 2] == b"${":
            if lit:
                out.append(("lit", bytes(lit)))
                lit = bytearray()
            j = i + 2
            if text[j:j + 1] == b"!":
                j += 1
            k = j
            while k < n and (text[k:k + 1].isalnum() or text[k:k + 1] == b"_"):
                k += 1
            name = text[j:k]
            if not NAME_RE.match(name):
                raise VarsSyntax("bad variable name at %d" % j)
            op = b""
            for cand in (b":-", b":+", b":?", b"-", b"+"):
                if text[k:k + len(cand)] == cand:
                    op = cand
                    k += len(cand)
                    break
            word = bytearray()
            if op:
                while k < n and text[k:k + 1] != b"}":
                    if text[k:k + 1] == b"\\":
                        k += 1
                        if k >= n:
                            raise VarsSyntax("unterminated word")
                    if text[k:k + 2] == b"${":
                        raise VarsSyntax("a nested ${...} (Q-C: dropped from v0.1)")
                    word.append(text[k])
                    k += 1
            if text[k:k + 1] != b"}":
                raise VarsSyntax("unterminated ${")
            out.append(("var", name.decode(), op.decode(), bytes(word)))
            i = k + 1
        else:
            lit.append(text[i])
            i += 1
    if lit:
        out.append(("lit", bytes(lit)))
    return out


def names(text):
    seen = []
    for seg in parse(text):
        if seg[0] == "var" and seg[1] not in seen:
            seen.append(seg[1])
    return seen


def esc_pcre2(b):
    """Escape so the bytes match AS THEMSELVES under libpcre2 (no (?x))."""
    out = bytearray()
    for c in b:
        if (48 <= c <= 57) or (65 <= c <= 90) or (97 <= c <= 122) or c == 95:
            out.append(c)
        elif 33 <= c <= 126:
            out += b"\\" + bytes([c])
        else:
            out += b"\\x%02x" % c
    return bytes(out)


def esc_py(b):
    return re.escape(b)


def _value(op, word, v):
    """vars.md section 2's table -> ('refuse',) | ('text', bytes)."""
    if op == "":
        return ("refuse",) if v is UNSET else ("text", v)
    if op == "-":
        return ("text", word) if v is UNSET else ("text", v)
    if op == ":-":
        return ("text", word) if (v is UNSET or v == EMPTY) else ("text", v)
    if op == "+":
        return ("text", b"") if v is UNSET else ("text", word)
    if op == ":+":
        return ("text", b"") if (v is UNSET or v == EMPTY) else ("text", word)
    if op == ":?":
        return ("refuse",) if (v is UNSET or v == EMPTY) else ("text", v)
    raise AssertionError(op)


def resolve(text, binding, esc=esc_pcre2):
    """-> the resolved, escaped pattern bytes, or None = the call is REFUSED."""
    out = bytearray()
    for seg in parse(text):
        if seg[0] == "lit":
            out += seg[1]
            continue
        _k, name, op, word = seg
        r = _value(op, word, binding.get(name, UNSET))
        if r[0] == "refuse":
            return None
        out += esc(r[1])
    return bytes(out)


# --------------------------------------------------------------------------
# value sets
# --------------------------------------------------------------------------
def tenant_value(k):
    m = k % 8
    if m == 3:
        return b"org.%d" % k
    if m == 5:
        return b"c++%d" % k
    if m == 6:
        return b"a|b%d" % k
    if m == 7:
        return b"(t%d)" % k
    return b"t%04x" % k


TERMS = [b"error", b"timeout", b"Retry", b"WARN", b"disk", b"node-1", b"x_y", b"cache", b"flush", b"Queue",
         b"a.b", b"c++", b"x|y", b"(foo)", b"[z]", b"a\x00b", b"$USD", b"^caret", b"back\\slash", b"q?",
         b"a*b", b"{2}", b"caf\xc3\xa9", b"100%", b"a b", b"k.v", b"ab", b"A", b"id#7", b"/tmp", b"x.*y", b"1+1",
         b"[a-z]+", b"(?i)", b"\\d", b"\\b", b"^$", b"a\tb", b"it's", b"say \"hi\"", b"p||q", b"z{1,2}",
         b"mixedCASE", b"ZZZ", b"tail"]
TERMS += [b"warn", b"Error"]          # case-twins of two others: DISTINCT bindings, distinct patterns
assert len(set(TERMS)) == len(TERMS)

PREFIXES = [UNSET, EMPTY, b"api", b"internal", b"ex.tra", b"v-1"]
RESES = [b"users", b"orders", b"items.list", b"a+b", UNSET, b"reports(2)"]
FMTS = [UNSET, EMPTY, b"x"]

NOISE = [b"the", b"request", b"from", b"host", b"failed", b"after", b"3", b"retries", b"on", b"shard", b"7", b"while",
         b"flushing", b"queue", b"status", b"ok", b"user", b"agent", b"id", b"path", b"and", b"then", b"done"]
MSGS = [b"connection reset by peer", b"upstream timed out", b"cache miss", b"retrying in 5s", b"quota exceeded",
        b"disk almost full", b"slow query", b"token refreshed"]


def zipf_cum(k):
    w = [int(1000000 / (r ** 1.1)) for r in range(1, k + 1)]
    cum, t = [], 0
    for x in w:
        t += x
        cum.append(t)
    return cum


def zipf_pick(rng, cum):
    import bisect
    return bisect.bisect_right(cum, rng.below(cum[-1]))


def twin_of(v):
    """A near-miss of `v` that an UNESCAPED interpolation would match but the
    as-itself match must not (the first regex metacharacter -> X), else a
    last-byte change."""
    for i, c in enumerate(v):
        if c in b".+|()[]{}*?^$\\":
            return v[:i] + b"X" + v[i + 1:]
    return v[:-1] + b"z" if v else b"z"


# --------------------------------------------------------------------------
# the streams
# --------------------------------------------------------------------------
def _tenant_line(rng, values, k):
    v = values[k]
    kind = rng.below(100)
    digits = b"%04d" % rng.below(10000)
    lvl = rng.choice([b"ERROR", b"WARN"])
    tv, pre = v, b""
    if kind < 8:
        lvl = b"INFO"
    elif kind < 14:
        digits = digits[1:]
    elif kind < 20:
        tv = twin_of(v)
    elif kind < 25:
        tv = values[(k + 1) % len(values)]
    elif kind < 28:
        pre = b" "
    return pre + tv + b"-" + digits + b" " + lvl + b" " + rng.choice(MSGS)


def _build_tenant(sid, seed, d, n):
    rng = Rng(seed)
    values = [tenant_value(k) for k in range(d)]
    assert len(set(values)) == d
    bindings = [("b%d" % k, {"tenant": values[k]}) for k in range(d)]
    lines, calls = [], []
    for i in range(n):
        k = i % d
        lines.append(_tenant_line(rng, values, k))
        calls.append(k)
    return lines, calls, bindings


def _route_line(rng, b):
    p = b["prefix"]
    prefix = p if (p is not UNSET and p != EMPTY) else b"api"
    res = b["res"] if b["res"] is not UNSET else b"users"
    kind = rng.below(100)
    if kind < 6:
        prefix = b"other"
    elif kind < 12:
        res = twin_of(res)
    ver = b"v%d" % rng.between(1, 3)
    if kind >= 96:
        ver = b"vX"
    ext = rng.choice([b".json", b".json", b"", b".json?x=1", b"?x=1", b".jsonx", b"/more", b".xml", b".json?"])
    return b"/" + prefix + b"/" + ver + b"/" + res + ext


def _build_route(sid, seed, n):
    rng = Rng(seed)
    combos = [(p, r, f) for p in PREFIXES for r in RESES for f in FMTS]
    for i in range(len(combos) - 1, 0, -1):          # Fisher-Yates, deterministic
        j = rng.below(i + 1)
        combos[i], combos[j] = combos[j], combos[i]
    bindings = [("b%d" % k, {"prefix": p, "res": r, "fmt": f}) for k, (p, r, f) in enumerate(combos)]
    cum = zipf_cum(len(bindings))
    lines, calls = [], []
    for _ in range(n):
        k = zipf_pick(rng, cum)
        lines.append(_route_line(rng, bindings[k][1]))
        calls.append(k)
    return lines, calls, bindings


def _case(rng, t):
    return rng.choice([t, t, t.upper(), t.lower(), t.swapcase()])


def _isword(c):
    return (48 <= c <= 57) or (65 <= c <= 90) or (97 <= c <= 122) or c == 95


def _fit(t):
    """(pre, post) NEIGHBOUR bytes that make `\\bTERM\\b` hold: \\b needs a
    word/non-word change, so a term whose first (last) byte is not a word byte
    needs a word byte before (after) it, and a word-ended one a non-word byte
    (the separating space). `bad` is the opposite pair (the boundary fails)."""
    pre = b"x" if t and not _isword(t[0]) else b""
    post = b"x" if t and not _isword(t[-1]) else b""
    bad_pre = b"" if t and not _isword(t[0]) else b"x"
    bad_post = b"" if t and not _isword(t[-1]) else b"x"
    return pre, post, bad_pre, bad_post


def _term_line(rng, v):
    t = v if (v is not UNSET and v != EMPTY) else b"error"
    words = [rng.choice(NOISE) for _ in range(rng.between(3, 8))]
    kind = rng.below(100)
    pre, post, bad_pre, bad_post = _fit(t)
    if kind < 10:
        pass                                   # no term at all
    else:
        if kind < 25:
            tt = bad_pre + _case(rng, t)                                # boundary fails before
        elif kind < 35:
            tt = pre + twin_of(t) + post                                # an unescaped reading would match
        elif kind < 45:
            tt = pre + _case(rng, t) + bad_post                         # boundary fails after
        else:
            tt = pre + _case(rng, t) + post
        words.insert(rng.below(len(words) + 1), tt)
    return b" ".join(words)


def _build_term(sid, seed, n):
    rng = Rng(seed)
    vals = list(TERMS) + [EMPTY, UNSET]
    for i in range(len(vals) - 1, 0, -1):
        j = rng.below(i + 1)
        vals[i], vals[j] = vals[j], vals[i]
    bindings = [("b%d" % k, {"term": v}) for k, v in enumerate(vals)]
    cum = zipf_cum(len(bindings))
    lines, calls = [], []
    for _ in range(n):
        k = zipf_pick(rng, cum)
        lines.append(_term_line(rng, bindings[k][1]["term"]))
        calls.append(k)
    return lines, calls, bindings


# id -> (builder args..., members that run it, reuse order)
STREAMS = [
    ("tenant-d4", ("va-tenant",), "round-robin", lambda: _build_tenant("tenant-d4", 20261101, 4, 16384)),
    ("tenant-d64", ("va-tenant",), "round-robin", lambda: _build_tenant("tenant-d64", 20261102, 64, 16384)),
    ("tenant-d4096", ("va-tenant",), "round-robin", lambda: _build_tenant("tenant-d4096", 20261103, 4096, 16384)),
    ("route-zipf", ("va-route",), "zipf-s1.1", lambda: _build_route("route-zipf", 20261104, 4096)),
    ("term-zipf", ("va-term", "va-term-bang"), "zipf-s1.1", lambda: _build_term("term-zipf", 20261105, 4096)),
]


def member_texts():
    import members as MB
    return {m.id: m.text for m in MB.members() if m.route == "vars"}


class Built:
    """One built stream: subject bytes, calls [(offset, length, binding_id)],
    the bindings table, and the facts the manifest / values table carry."""

    def __init__(self, sid, members, reuse, parts):
        lines, picks, bindings = parts
        self.sid, self.members, self.reuse = sid, members, reuse
        self.bindings = bindings                      # [(binding_id, {name: value})]
        self.lines = lines
        buf, self.calls = bytearray(), []
        for ln, k in zip(lines, picks):
            assert b"\n" not in ln
            self.calls.append((len(buf), len(ln), bindings[k][0], k))
            buf += ln + b"\n"
        self.data = bytes(buf)
        self.picks = picks
        self.segment_bytes = sum(c[1] for c in self.calls)

    def calls_text(self):
        return ("call_id\toffset\tlength\tsegment_bytes\tbinding_id\n"
                + "".join("%d\t%d\t%d\t%d\t%s\n" % (i, o, ln, ln, b)
                          for i, (o, ln, b, _k) in enumerate(self.calls))).encode("ascii")

    def bindings_text(self):
        """`binding_id name value`: value is lowercase HEX, or the literal
        `UNSET` / `EMPTY` (the note's `value_hex|UNSET` plus EMPTY, because a
        zero-length hex field is not a TSV cell a reader can rely on)."""
        out = ["binding_id\tname\tvalue\n"]
        for bid, d in self.bindings:
            for name, v in d.items():
                out.append("%s\t%s\t%s\n" % (bid, name, "UNSET" if v is UNSET else "EMPTY" if v == EMPTY else v.hex()))
        return "".join(out).encode("ascii")

    def resolved(self, member):
        """-> per call: resolved pattern bytes or None (refused)."""
        text = member_texts()[member]
        cache, out = {}, []
        for _o, _l, _b, k in self.calls:
            if k not in cache:
                cache[k] = resolve(text, self.bindings[k][1])
            out.append(cache[k])
        return out

    def facts(self, member):
        r = self.resolved(member)
        return {"refused": sum(1 for x in r if x is None), "distinct_resolved": len({x for x in r if x is not None})}


def build_all():
    return [Built(sid, mem, reuse, fn()) for sid, mem, reuse, fn in STREAMS]


def main(argv):
    ms = member_texts()
    for t in ms.values():
        parse(t)
    print("stream\tmember\tcalls\tbytes\tsegment_bytes\tbindings\tdistinct_values\tdistinct_resolved\trefused\treuse")
    for s in build_all():
        dv = len({tuple(sorted((k, v) for k, v in d.items())) for _b, d in s.bindings})
        for m in s.members:
            f = s.facts(m)
            print("%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%s" % (s.sid, m, len(s.calls), len(s.data), s.segment_bytes,
                                                              len(s.bindings), dv, f["distinct_resolved"], f["refused"], s.reuse))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
