"""unusual_lib.py -- the shared library of bench/unusual: a deterministic PRNG,
the REFERENCE SCANNER for cscan, the host references (S-expression, JSON,
Luhn, ISBN-13, member, netstring), and the libpcre2 oracle WITH a Python
callout function (the primary method for the callout members, section 8 of
docs/design/unusual_set_v1.md).

Nothing here times anything. Nothing here imports an engine other than the
installed libpcre2 (through pcrecbench/oracle_pcre2.py's own binding).

THE REFERENCE SCANNER (`ref_scan`) is regex-free, iterative (an explicit
stack, no recursion: a 100k-deep subject must not meet Python's recursion
limit) and written from inline_c.md 2.3 rules 1-5 plus cscan.rxt's three
header choices, NOT from the pattern's structure:
  1. phase-2 splices (backslash-newline) are removed before anything else is
     recognised -- the scanner works on a LOGICAL stream that remembers every
     character's original offset;
  2. "..." and '...' literals with backslash escapes, /* */ and // comments
     are opaque (a raw newline inside a literal is a refusal -- choice 1; a
     // comment that reaches the end of the subject is a refusal -- choice 2);
  3. a ' inside a pp-number is a C23 digit separator (a pp-number starts with
     a digit, or '.' then a digit; it continues over [eEpP][+-], identifier
     characters, '.', and a ' that is followed by an identifier character);
  4. depth starts at 1 after `(?{`; `{` and `<%` add one, `}` and `%>`
     subtract one; no trigraphs;
  5. the segment ends at the brace that reaches depth 0, which must be
     followed (splices skipped) by `)`.
  Group 1 is [start+3, original offset of the closing token): it includes any
  splice immediately before the closing brace (choice 3).
It answers for the SAME `\\G`-anchored call the pattern gets: the segment must
begin at the given offset.
"""
import ctypes
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from pcrecbench import oracle_pcre2 as O  # noqa: E402

NL = 10


# --------------------------------------------------------------------------
# PRNG: splitmix64, so no generator depends on the stdlib `random` module's
# algorithm staying put across Python releases.
# --------------------------------------------------------------------------
class Rng:
    M = (1 << 64) - 1

    def __init__(self, seed):
        if isinstance(seed, str):
            seed = int.from_bytes(hashlib.sha256(seed.encode()).digest()[:8], "big")
        self.s = seed & self.M

    def u64(self):
        self.s = (self.s + 0x9E3779B97F4A7C15) & self.M
        z = self.s
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & self.M
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & self.M
        return z ^ (z >> 31)

    def below(self, n):
        return self.u64() % n

    def between(self, lo, hi):          # inclusive
        return lo + self.below(hi - lo + 1)

    def chance(self, per_1000):
        return self.below(1000) < per_1000

    def choice(self, seq):
        return seq[self.below(len(seq))]

    def loguniform(self, lo, hi):
        import math
        u = (self.u64() >> 11) / float(1 << 53)
        return int(round(math.exp(math.log(lo) + u * (math.log(hi) - math.log(lo)))))


# --------------------------------------------------------------------------
# cscan: the reference scanner
# --------------------------------------------------------------------------
def _is_w(c):        # PCRE2 \w, byte mode, C locale tables
    return (48 <= c <= 57) or (65 <= c <= 90) or (97 <= c <= 122) or c == 95


def _is_idstart(c):
    return (65 <= c <= 90) or (97 <= c <= 122) or c == 95 or c == 36 or c >= 0x80


def _is_idcont(c):
    return _is_w(c) or c == 36 or c >= 0x80


class _Logical:
    """The subject from `start` with every backslash-newline pair removed,
    plus the map back to original offsets. With no splice in the tail the
    map is the identity (offset base) and costs nothing."""
    __slots__ = ("chars", "_pos", "base", "n")

    def __init__(self, subject, start, limit=None):
        limit = len(subject) if limit is None else limit
        tail = subject[start:limit]
        if b"\\\n" not in tail:
            self.chars, self._pos, self.base = tail, None, start
        else:
            import array
            chars = bytearray()
            pos = array.array("Q")
            i, n = start, limit
            while i < n:
                c = subject[i]
                if c == 92 and i + 1 < n and subject[i + 1] == NL:
                    i += 2
                    continue
                chars.append(c)
                pos.append(i)
                i += 1
            pos.append(n)
            self.chars, self._pos, self.base = bytes(chars), pos, 0
        self.n = len(self.chars)

    def orig(self, i):
        return self.base + i if self._pos is None else self._pos[i]


_NEED = object()        # the window ended before the scan could decide


def _scan(subject, start, limit):
    more = limit < len(subject)              # bytes beyond the window exist

    def eof():
        return _NEED if more else None

    lg = _Logical(subject, start + 3, limit)
    chars, m = lg.chars, lg.n
    i = 0
    depth = 1
    while True:
        if i >= m or (more and i >= m - 16):  # never decide within 16 bytes of a cut window
            return eof()
        c = chars[i]
        nx = chars[i + 1] if i + 1 < m else -1
        if _is_idstart(c):                   # identifier (prefixes are plain text)
            i += 1
            while i < m and _is_idcont(chars[i]):
                i += 1
            continue
        if (48 <= c <= 57) or (c == 46 and 48 <= nx <= 57):   # pp-number
            i += 1
            while i < m:
                d = chars[i]
                d2 = chars[i + 1] if i + 1 < m else -1
                if d in (101, 69, 112, 80) and d2 in (43, 45):
                    i += 2
                elif _is_w(d) or d == 46 or d == 36 or d >= 0x80:
                    i += 1
                elif d == 39 and d2 >= 0 and _is_w(d2):
                    i += 1
                else:
                    break
            continue
        if c == 34 or c == 39:               # string / character literal
            q = c
            i += 1
            while True:
                if i >= m:
                    return eof()             # unterminated (or the window ended)
                d = chars[i]
                if d == q:
                    i += 1
                    break
                if d == NL:
                    return None              # choice 1: raw newline in a literal
                if d == 92:
                    if i + 1 >= m:
                        return eof()
                    if chars[i + 1] == NL:
                        return None
                    i += 2
                else:
                    i += 1
            continue
        if c == 47 and nx == 42:             # block comment
            j = chars.find(b"*/", i + 2)
            if j < 0:
                return eof()                 # unterminated comment
            i = j + 2
            continue
        if c == 47 and nx == 47:             # line comment (to the newline)
            j = chars.find(b"\n", i + 2)
            i = m if j < 0 else j            # the newline itself is an ordinary byte
            continue
        if c == 123 or (c == 60 and nx == 37):   # { or <%
            depth += 1
            i += 1 if c == 123 else 2
            continue
        if c == 125 or (c == 37 and nx == 62):   # } or %>
            width = 1 if c == 125 else 2
            j = i + width                    # first logical index after the closer
            if depth > 1:
                depth -= 1
                i = j
                continue
            if j < m and chars[j] == 41:     # depth 0: must be followed by `)`
                return (start, lg.orig(j) + 1, start + 3, lg.orig(i))
            return None
        i += 1                               # everything else, one byte


def ref_scan(subject, start=0):
    """-> (match_start, match_end, body_start, body_end) in ORIGINAL offsets,
    or None (the refusal / no match). `subject` is bytes. The scan works on a
    window of the tail that grows 4x until the scan can decide, so a call costs
    O(segment), never O(rest of the subject)."""
    n = len(subject)
    if subject[start:start + 3] != b"(?{":
        return None
    w = 4096
    while True:
        r = _scan(subject, start, min(n, start + 3 + w))
        if r is not _NEED:
            return r
        w *= 4


# --------------------------------------------------------------------------
# host references (plain Python of each member's INTENTION)
# --------------------------------------------------------------------------
def sexp_first(subject, start=0):
    """Leftmost '(' that opens a balanced group -> (s, e) or None. Stack scan:
    the pairing is the one the pattern's possessive recursion gives."""
    stack = []
    best = None
    ends = {}
    for i in range(start, len(subject)):
        c = subject[i]
        if c == 40:
            stack.append(i)
        elif c == 41 and stack:
            j = stack.pop()
            ends[j] = i + 1
            if best is None or j < best:
                best = j
    return (best, ends[best]) if best is not None else None


def luhn_ok(digits):
    t = 0
    for k, ch in enumerate(reversed(digits)):
        d = ch - 48
        if k % 2:
            d *= 2
            if d > 9:
                d -= 9
        t += d
    return t % 10 == 0


def isbn13_ok(digits):
    if len(digits) != 13 or digits[:3] not in (b"978", b"979"):
        return False
    t = sum((ch - 48) * (3 if k % 2 else 1) for k, ch in enumerate(digits))
    return t % 10 == 0


def load_users():
    with open(os.path.join(HERE, "values", "users.tsv"), "rb") as f:
        return frozenset(l.strip() for l in f if l.strip() and not l.startswith(b"#"))


_RE_LUHN = re.compile(rb"\b(\d{13,19})\b")
_RE_ISBN = re.compile(rb"\b(97[89]\d{10})\b")
_RE_USER = re.compile(rb"\buser=(\w++)")


def host_filter_first(rx, ok, subject, start=0):
    """The first candidate of `rx` at/after `start` whose group 1 passes `ok`;
    the match span is group 1's span (the callout site is zero-width)."""
    pos = start
    while True:
        m = rx.search(subject, pos)
        if m is None:
            return None
        if ok(m.group(1)):
            return (m.start(), m.end())
        pos = m.start() + 1


def host_first(kind, subject, start=0):
    if kind == "luhn":
        return host_filter_first(_RE_LUHN, luhn_ok, subject, start)
    if kind == "isbn":
        return host_filter_first(_RE_ISBN, isbn13_ok, subject, start)
    if kind == "member":
        users = load_users()
        return host_filter_first(_RE_USER, lambda g: g in users, subject, start)
    if kind == "netstr":
        return netstr_first(subject, start)
    raise KeyError(kind)


def netstr_first(subject, start=0):
    """Leftmost netstring `len:data,` (len 1-9 digits, data any bytes)."""
    n = len(subject)
    for s in range(start, n):
        if not (48 <= subject[s] <= 57):
            continue
        k = s
        while k < n and 48 <= subject[k] <= 57:
            k += 1
        L = k - s
        if L > 9 or k >= n or subject[k] != 58:
            continue
        d = k + 1 + int(subject[s:k])
        if d < n and subject[d] == 44:
            return (s, d + 1)
    return None


def host_find_all(first_fn, subject):
    """(first span, count): the find-all loop of oracle_pcre2._find_all_impl
    (advance off the match's own START for an empty match, else its end)."""
    pos, count, first = 0, 0, None
    n = len(subject)
    while pos <= n:
        got = first_fn(subject, pos)
        if got is None:
            break
        s, e = got
        if first is None:
            first = (s, e)
        count += 1
        pos = e if e > s else s + 1
    return first, count


# JSON: the regex's language, from RFC 8259 via json.loads, with the declared
# divergences (docs/design/unusual_set_v1.md 2.1).
def json_ok(subject):
    """True/False for 'one JSON value' by python json; None when python cannot
    answer (RecursionError on deep nesting, undecodable bytes)."""
    import json

    def refuse(_s):
        raise ValueError("nonstandard constant")
    try:
        text = subject.decode("utf-8")
        json.loads(text, parse_constant=refuse)
        return True
    except RecursionError:
        return None
    except UnicodeDecodeError:
        return None
    except ValueError:
        return False


# --------------------------------------------------------------------------
# the libpcre2 oracle, with an optional Python callout function
# --------------------------------------------------------------------------
class CalloutBlock(ctypes.Structure):
    # pcre2.h 10.46, version-2 block. Verified empirically in selfcheck().
    _fields_ = [("version", ctypes.c_uint32),
                ("callout_number", ctypes.c_uint32),
                ("capture_top", ctypes.c_uint32),
                ("capture_last", ctypes.c_uint32),
                ("offset_vector", ctypes.POINTER(ctypes.c_size_t)),
                ("mark", ctypes.c_void_p),
                ("subject", ctypes.c_void_p),
                ("subject_length", ctypes.c_size_t),
                ("start_match", ctypes.c_size_t),
                ("current_position", ctypes.c_size_t),
                ("pattern_position", ctypes.c_size_t),
                ("next_item_length", ctypes.c_size_t),
                ("callout_string_offset", ctypes.c_size_t),
                ("callout_string_length", ctypes.c_size_t),
                ("callout_string", ctypes.c_void_p),
                ("callout_flags", ctypes.c_uint32)]


_CALLOUT_FN = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(CalloutBlock), ctypes.c_void_p)
_lib = O._lib
_lib.pcre2_match_context_create_8.restype = ctypes.c_void_p
_lib.pcre2_match_context_create_8.argtypes = [ctypes.c_void_p]
_lib.pcre2_match_context_free_8.restype = None
_lib.pcre2_match_context_free_8.argtypes = [ctypes.c_void_p]
_lib.pcre2_set_callout_8.restype = ctypes.c_int
_lib.pcre2_set_callout_8.argtypes = [ctypes.c_void_p, _CALLOUT_FN, ctypes.c_void_p]

CONTINUE, FAIL = 0, 1          # the libpcre2 column of the return-code table (3.2)


class Fire:
    """What a callee sees: the engine-neutral view of one callout."""
    __slots__ = ("number", "subject", "pos", "caps")

    def __init__(self, number, subject, pos, caps):
        self.number, self.subject, self.pos, self.caps = number, subject, pos, caps


class Rx:
    """A compiled pattern (interpreter, library defaults) + an optional
    callout function `fn(Fire) -> CONTINUE | FAIL`."""

    def __init__(self, pattern, options=0, callout=None):
        self.c = O.compile(pattern, options)
        self.callout = callout
        self.fires = 0

    def search(self, subject, start=0, options=0):
        """-> ((s, e), groups) or None; raises O.Pcre2Error on a give-up."""
        c = self.c
        md = _lib.pcre2_match_data_create_from_pattern_8(c._code, None)
        mctx = None
        keep = None
        try:
            if self.callout is not None:
                mctx = _lib.pcre2_match_context_create_8(None)
                fn = self.callout

                def tramp(blk, _data):
                    b = blk.contents
                    ov = b.offset_vector
                    caps = [(ov[2 * i], ov[2 * i + 1]) for i in range(b.capture_top)]
                    self.fires += 1
                    return fn(Fire(b.callout_number, subject, b.current_position, caps))
                keep = _CALLOUT_FN(tramp)
                _lib.pcre2_set_callout_8(mctx, keep, None)
            rc = _lib.pcre2_match_8(c._code, subject, len(subject), start, options, md, mctx)
            if rc == O.PCRE2_ERROR_NOMATCH:
                return None
            if rc < 0:
                raise O.Pcre2Error("pcre2_match error %d: %s" % (rc, O._errmsg(rc)))
            ov = _lib.pcre2_get_ovector_pointer_8(md)
            npairs = rc if rc > 0 else 1
            pairs = [(ov[2 * i], ov[2 * i + 1]) for i in range(npairs)]
            groups = tuple(None if s == O.PCRE2_UNSET else (s, e) for s, e in pairs[1:])
            return (pairs[0][0], pairs[0][1]), groups
        finally:
            _lib.pcre2_match_data_free_8(md)
            if mctx:
                _lib.pcre2_match_context_free_8(mctx)

    def find_all(self, subject):
        pos, count, first = 0, 0, None
        n = len(subject)
        while pos <= n:
            got = self.search(subject, pos)
            if got is None:
                break
            (s, e), _g = got
            if first is None:
                first = (s, e)
            count += 1
            pos = e if e > s else s + 1
        return first, count


# the callees as the primary method sees them: pure filters on group 1
def callee_for(kind):
    users = load_users() if kind == "member" else None

    def fn(f):
        g = f.caps[1]
        text = f.subject[g[0]:g[1]]
        if kind == "luhn":
            ok = luhn_ok(text)
        elif kind == "isbn":
            ok = isbn13_ok(text)
        elif kind == "member":
            ok = text in users
        elif kind == "netstr":                       # the check-at-end assist (3.2)
            ok = f.pos - (g[1] + 1) == int(text)
        elif kind == "pass":
            ok = True
        else:
            raise KeyError(kind)
        return CONTINUE if ok else FAIL
    return fn


def selfcheck():
    """Empirical check of the callout block layout and the return-code table."""
    seen = []

    def fn(f):
        seen.append((f.number, f.pos, list(f.caps)))
        return CONTINUE
    rx = Rx(rb"(ab)(?C7)c", callout=fn)
    got = rx.search(b"xxabc")
    assert got == ((2, 5), ((2, 4),)), got
    assert seen == [(7, 4, [(0, 0), (2, 4)])] or seen[0][0] == 7 and seen[0][1] == 4 and seen[0][2][1] == (2, 4), seen
    r2 = Rx(rb"(ab)(?C7)c", callout=lambda f: FAIL)
    assert r2.search(b"xxabc") is None
    r3 = Rx(rb"(ab)(?C7)c", callout=lambda f: -1)      # negative abandons: NOMATCH (-1)
    assert r3.search(b"xxabc") is None
    return True


def sha256(b):
    return hashlib.sha256(b).hexdigest()


if __name__ == "__main__":
    print("callout layout + return codes:", selfcheck())
