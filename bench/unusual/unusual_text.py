"""unusual_text.py -- the deterministic text generators of bench/unusual
(docs/design/unusual_set_v1.md section 4): C segment bodies (F1), the F3
pathologicals, S-expression / JSON / callout / netstring corpora.

Everything here is a pure function of a seed (unusual_lib.Rng, splitmix64);
no wall clock, no stdlib `random`, no dict-order dependence. The manifests'
sha256 columns pin the output byte for byte (`--check` in every gen_*.py).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from unusual_lib import Rng, luhn_ok, isbn13_ok, load_users  # noqa: E402

# --------------------------------------------------------------------------
# C bodies
# --------------------------------------------------------------------------
IDENTS = [b"x", b"count", b"buf", b"len", b"ptr", b"i", b"n", b"result", b"state", b"idx",
          b"flags", b"tmp", b"value", b"node", b"head", b"tail", b"size", b"offset", b"mask",
          b"ctx", b"key", b"val", b"next", b"prev", b"err", b"rc"]
KEYWORDS = [b"if", b"else", b"for", b"while", b"return", b"switch", b"case", b"break", b"int",
            b"char", b"static", b"const", b"void", b"struct", b"unsigned", b"do", b"goto"]
WORDS = [b"the", b"count", b"closing", b"brace", b"here", b"note", b"fixme", b"loop", b"until",
         b"done", b"check", b"bounds", b"first", b"then", b"retry", b"cache", b"flush", b"}", b"{",
         b"(", b")", b"x", b"y", b"len"]
PUNCT = [b"+", b"-", b"*", b"/", b"=", b";", b",", b"(", b")", b"[", b"]", b"<", b">", b"!", b"&",
         b"|", b"?", b":", b"^", b"~", b"==", b"!=", b"<=", b">=", b"&&", b"||", b"->", b"++"]
STRPIECES = [b"abc", b"value", b" ", b"%d", b"%s", b"\\n", b"\\t", b"\\\"", b"\\\\", b"{", b"}", b"x=", b"/*", b"//"]
HIGH = [b"\xc3\xa9", b"\xe4\xb8\xad", b"\xff", b"\x80", b"\xc3\xbc"]


def _ident(rng, hi_per_1000):
    r = rng.below(10)
    if r < 3:
        return rng.choice(KEYWORDS)
    base = rng.choice(IDENTS)
    if r < 5:
        base = base + b"_" + rng.choice(IDENTS)
    if r == 5:
        base = base + b"%d" % rng.below(100)
    if rng.chance(hi_per_1000):
        base = base + rng.choice(HIGH)
    return base


def _number(rng):
    r = rng.below(8)
    if r < 3:
        return b"%d" % rng.between(0, 999999)
    if r == 3:
        return b"0x%x" % rng.between(0, 0xFFFFFFFF)
    if r == 4:
        return b"%d.%de%s%d" % (rng.below(10), rng.below(1000), rng.choice([b"+", b"-"]), rng.below(30))
    if r == 5:
        return b".%d" % rng.between(1, 99999)
    if r == 6:                                            # C23 digit separators
        return b"%d'%03d'%03d" % (rng.between(1, 999), rng.below(1000), rng.below(1000))
    return b"0x%X'%04X" % (rng.below(256), rng.below(65536))


def _string(rng):
    prefix = rng.choice([b"", b"", b"", b"L", b"u8", b"u", b"U"])
    parts = b"".join(rng.choice(STRPIECES) for _ in range(rng.between(0, 5)))
    return prefix + b'"' + parts + b'"'


def _char(rng):
    prefix = rng.choice([b"", b"", b"L", b"u", b"U"])
    return prefix + b"'" + rng.choice([b"x", b"}", b"{", b"\\'", b"\\n", b"\\\\", b"0", b"\"", b"%"]) + b"'"


def _bcomment(rng):
    return b"/* " + b" ".join(rng.choice(WORDS) for _ in range(rng.between(1, 8))) + b" */"


def _lcomment(rng):
    return b"// " + b" ".join(rng.choice(WORDS) for _ in range(rng.between(1, 8))) + b"\n"


def _ppline(rng):
    if rng.chance(500):
        return b"\n#define M%d(a) { a; }\n" % rng.below(1000)
    return b"\n#define L%d(a) \\\n  do { a; } while (0)\n" % rng.below(1000)


def _splice_in(rng, tok):
    """An interior backslash-newline (phase-2 splice) at a random cut of
    `tok`; a no-op for a token shorter than two bytes."""
    if len(tok) < 2:
        return tok
    cut = rng.between(1, len(tok) - 1)
    return tok[:cut] + b"\\\n" + tok[cut:]


def c_body(rng, target, splice_per_1000=15, hi_per_1000=20, max_depth=6, refuse=None):
    """A balanced C-ish body of about `target` bytes: tokens separated by one
    space (or a newline), nested {} / <% %> blocks to `max_depth`, splices
    at a declared rate (interior of a token, or a space-splice-space
    separator that can never form a digraph), and, when `refuse` is
    'dq-newline' / 'sq-newline', one raw newline inside a literal (the
    scanner's local refusal) at a random token boundary."""
    out = bytearray()
    stack = []                                    # closers of the open nested blocks
    refuse_at = rng.between(0, max(1, target // 3)) if refuse else None
    refused = False
    while True:
        need = len(out) + sum(len(c) + 1 for c in stack) + 3
        if need >= target and not stack:
            break
        if need >= target:                        # wind down: close the open blocks
            out += b" " + stack.pop()
            continue
        if refuse and not refused and len(out) >= refuse_at:
            out += (b' "abc\ndef"' if refuse == "dq-newline" else b" 'a\nb'")
            refused = True
            continue
        r = rng.below(100)
        if r < 28:
            tok = _ident(rng, hi_per_1000)
        elif r < 40:
            tok = _number(rng)
        elif r < 48:
            tok = _string(rng)
        elif r < 52:
            tok = _char(rng)
        elif r < 58:
            tok = _bcomment(rng)
        elif r < 62:
            tok = _lcomment(rng)
        elif r < 64:
            tok = _ppline(rng)
        elif r < 72 and len(stack) < max_depth:
            if rng.chance(150):
                out += b" <%"
                stack.append(b"%>" if rng.chance(900) else b"}")
            else:
                out += b" {"
                stack.append(b"}" if rng.chance(950) else b"%>")
            continue
        elif r < 76 and stack:
            out += b" " + stack.pop()
            continue
        else:
            tok = rng.choice(PUNCT)
        if rng.chance(splice_per_1000):
            tok = _splice_in(rng, tok)
        sep = b" \\\n " if rng.chance(splice_per_1000 // 3) else b" "
        out += sep + tok
    if refuse and not refused:                    # target tiny: force the refusal in
        out += (b' "abc\ndef"' if refuse == "dq-newline" else b" 'a\nb'")
    return bytes(out)


def c_segment(rng, target, **kw):
    refuse = None
    if rng.chance(10):                            # ~1 % local refusals
        refuse = rng.choice(["dq-newline", "sq-newline"])
    body = c_body(rng, max(target - 6, 8), refuse=refuse, **kw)
    return b"(?{" + body + b" })", refuse is not None


FILLER_FRAGS = [b"(?:foo|bar)+", b"\\d{2,4}", b"[a-z_]\\w*", b"^\\s*#", b"(?<n>\\w+)=\\k<n>",
                b"\\b(?:GET|POST)\\b", b"[^\"]*", b"\\.\\w{1,8}$", b"(?i)select\\b", b"x*?y", b"\\s+",
                b"(?=\\d)", b"[0-9a-f]{8}", b"\\$\\{name}", b"a|b|c", b"\\)\\(", b"[(){}]"]


def filler(rng, lo=8, hi=300):
    target = rng.loguniform(lo, hi)
    out = bytearray()
    while len(out) < target:
        out += rng.choice(FILLER_FRAGS) + (b"\n" if rng.chance(120) else b" ")
    assert b"(?{" not in out
    return bytes(out)


def segment_stream(seed, ncalls, seg_lo=20, seg_hi=5000):
    """-> (subject bytes, [(offset, length, refusal_flag)]) for the F1 stream:
    filler, segment, filler, segment, ..., filler."""
    rng = Rng(seed)
    out = bytearray()
    calls = []
    for _ in range(ncalls):
        out += filler(rng)
        seg, refused = c_segment(rng, rng.loguniform(seg_lo, seg_hi))
        calls.append((len(out), len(seg), refused))
        out += seg
    out += filler(rng)
    return bytes(out), calls


# --------------------------------------------------------------------------
# F3 pathologicals
# --------------------------------------------------------------------------
def nest_brace(d):
    return b"(?{ " + b"{" * d + b" x; " + b"}" * d + b" })"


def nest_paren(d):
    return b"(?{ " + b"(" * d + b" x; " + b")" * d + b" })"


def nest_digraph(d):
    return b"(?{ " + b"<%" * d + b" x; " + b"%>" * d + b" })"


def comment_big(n, close=True):
    body = (b"x } { * / " * ((n // 10) + 1))[:n]
    return b"(?{ /*" + body + (b"*/ })" if close else b"")


def literal_big(n):
    return b'(?{ s = "' + (b"ab}{" * ((n // 4) + 1))[:n] + b'"; })'


def idents_big(n, seed="idents"):
    rng = Rng(seed)
    out = bytearray(b"(?{ ")
    while len(out) < n:
        out += rng.choice(IDENTS) + b"_" + b"%d" % rng.below(100000) + b" "
    return bytes(out) + b"})"


def splice_big(n):
    unit = b"a\\\n"
    return b"(?{ " + unit * ((n // len(unit)) + 1) + b" })"


# --------------------------------------------------------------------------
# S-expressions, JSON, callout corpora
# --------------------------------------------------------------------------
SYMS = [b"define", b"lambda", b"let", b"if", b"cond", b"car", b"cdr", b"cons", b"+", b"-", b"*", b"x",
        b"y", b"n", b"acc", b"loop", b"list", b"map", b"filter", b"fold", b"else", b"#t", b"#f", b"0", b"1", b"42"]


def sexp_form(rng, depth, budget):
    if depth <= 0 or rng.chance(250):
        return rng.choice(SYMS)
    parts = [rng.choice(SYMS)]
    for _ in range(rng.between(1, 4)):
        parts.append(sexp_form(rng, depth - 1, budget))
    return b"(" + b" ".join(parts) + b")"


def sexp_text(n, seed="sexp"):
    rng = Rng(seed)
    out = bytearray()
    while len(out) < n:
        out += sexp_form(rng, rng.between(2, 8), 0) + b"\n"
        r = rng.below(100)
        if r < 6:
            out += b";; a comment about nothing in particular\n"
        elif r < 8:
            out += b")\n"                         # a stray closer between forms
        elif r < 10:
            out += b"(unclosed form\n"
    return bytes(out)


def json_value(rng, depth):
    r = rng.below(100)
    if depth <= 0 or r < 40:
        k = rng.below(6)
        if k == 0:
            return b"%d" % rng.between(-100000, 100000)
        if k == 1:
            return b"%d.%03d" % (rng.below(1000), rng.below(1000))
        if k == 2:
            return rng.choice([b"true", b"false", b"null"])
        if k == 3:
            return b"%de%d" % (rng.below(10), rng.below(20))
        return b'"' + rng.choice([b"alpha", b"beta", b"gamma", b"line\\nbreak", b"q\\\"uote", b"\\u00e9t\\u00e9", b"plain text", b"x"]) + b'"'
    if r < 70:
        items = [json_value(rng, depth - 1) for _ in range(rng.between(0, 5))]
        return b"[" + b",".join(items) + b"]"
    keys = [b"id", b"name", b"tags", b"meta", b"value", b"ok", b"items"]
    fields = [b'"' + rng.choice(keys) + b'": ' + json_value(rng, depth - 1) for _ in range(rng.between(1, 5))]
    return b"{" + b", ".join(fields) + b"}"


def json_big(n, seed="json"):
    rng = Rng(seed)
    out = bytearray(b"[\n")
    first = True
    while len(out) < n:
        if not first:
            out += b",\n"
        first = False
        out += b"  " + json_value(rng, 4)
    out += b"\n]\n"
    return bytes(out)


def make_luhn(rng, total, prefix=b""):
    """A digit string of length `total` starting with `prefix` and passing Luhn."""
    body = bytearray(prefix)
    while len(body) < total - 1:
        body.append(48 + rng.below(10))
    for d in range(10):
        cand = bytes(body) + bytes([48 + d])
        if luhn_ok(cand):
            return cand
    raise AssertionError


def make_isbn(rng, prefix=b"978"):
    body = bytearray(prefix)
    while len(body) < 12:
        body.append(48 + rng.below(10))
    for d in range(10):
        cand = bytes(body) + bytes([48 + d])
        if isbn13_ok(cand):
            return cand
    raise AssertionError


def _bad(rng, good):
    """`good` with the last digit changed so the check fails."""
    d = good[-1] - 48
    return good[:-1] + bytes([48 + (d + 1 + rng.below(8)) % 10])


LOGWORDS = [b"request", b"served", b"in", b"ms", b"from", b"cache", b"miss", b"hit", b"order", b"invoice",
            b"ref", b"id", b"total", b"paid", b"queued", b"retry", b"session", b"opened", b"closed"]


def _noise(rng):
    return b" ".join(rng.choice(LOGWORDS) for _ in range(rng.between(2, 7)))


def luhn_text(n, seed="luhn"):
    rng = Rng(seed)
    out = bytearray()
    while len(out) < n:
        k = rng.below(10)
        if k < 3:
            num = make_luhn(rng, rng.between(13, 19))
        elif k < 6:
            num = _bad(rng, make_luhn(rng, rng.between(13, 19)))
        elif k < 8:
            num = b"%d" % rng.between(10 ** rng.between(3, 12), 10 ** 13)      # 4-13 digit noise
        else:
            num = make_luhn(rng, rng.between(20, 24))                          # too long: never a candidate
        out += _noise(rng) + b" " + num + b" " + _noise(rng) + b"\n"
    return bytes(out)


def isbn_text(n, seed="isbn"):
    rng = Rng(seed)
    out = bytearray()
    while len(out) < n:
        k = rng.below(10)
        if k < 3:
            num = make_isbn(rng, rng.choice([b"978", b"979"]))
        elif k < 6:
            num = _bad(rng, make_isbn(rng))
        elif k < 8:
            num = b"%d" % rng.between(10 ** 9, 10 ** 10 - 1)                   # 10 digits
        else:
            num = b"1" + make_isbn(rng) + b"2"                                  # 15 digits: no boundary
        out += _noise(rng) + b" ISBN " + num + b" " + _noise(rng) + b"\n"
    return bytes(out)


def member_text(n, seed="member"):
    rng = Rng(seed)
    users = sorted(load_users())
    out = bytearray()
    while len(out) < n:
        k = rng.below(10)
        if k < 4:
            name = rng.choice(users)
        elif k < 8:
            name = b"u" + b"%d" % rng.below(100000)
        else:
            name = rng.choice(users).upper()
        out += b"%d.%d.%d.%d " % (10, rng.below(256), rng.below(256), rng.below(256)) + _noise(rng) + b" user=" + name + b" " + _noise(rng) + b"\n"
    return bytes(out)


def netstr(data):
    return b"%d:" % len(data) + data + b","


def netstr_text(n, seed="netstr"):
    rng = Rng(seed)
    out = bytearray()
    while len(out) < n:
        k = rng.below(10)
        # no ':' in a payload ([B148] 2026-10-28, Frank): a payload digit run followed by ':' was a
        # false candidate declaring up to 999,999,999 bytes, and the assisted spelling's per-byte
        # callout then walked to the subject's end (~11M fires on 1 MB, callee share > 40 %)
        data = bytes(rng.choice(b"abcdefghij ,\n0123456789") for _ in range(rng.between(0, 60)))
        if k < 7:
            out += netstr(data)
        elif k < 9:
            out += b"%d:" % (len(data) + rng.between(1, 5)) + data + b","       # wrong declared length
        else:
            out += b" junk" + b"%d" % rng.below(1000) + b" "
    return bytes(out)
