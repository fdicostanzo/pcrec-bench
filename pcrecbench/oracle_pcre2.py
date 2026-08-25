"""oracle_pcre2.py -- a minimal python/ctypes binding to the PCRE2 8-bit
RUNTIME: pcrec-bench's expectation ORACLE (requirements 5, method
`libpcre2-differential`).

COPIED VERBATIM, then extended, from pcrec
docs/design/eng_brep_measurements/probes/pcre2_ctypes.py (read-only origin;
attribution per the harness contract 2). The original header comment follows
unchanged because its reasoning is unchanged; pcrec-bench's ADDITIONS are
listed after it.

ADDITIONS for pcrec-bench (everything else is the origin's text):
  * `PCRE2_ANCHORED` / `PCRE2_ENDANCHORED` match options and a `match()`
    method, so the sub-bench's MATCH regime (anchored + end-anchored,
    harness contract 3) can be oracled by the same binding as SEARCH;
  * `find_all()` -- the count of NON-OVERLAPPING matches and the FIRST
    match's span, which is what a throughput subject's expectation is;
  * an explicit `giveup` surface: a negative rc that is not NOMATCH is
    raised rather than folded into "no match", so a match-limit give-up can
    never be silently recorded as an expectation.

pcrec is NOT the source of truth here and neither is pcrec-bench: PCRE2 is
(pcrec CLAUDE.md's Compatibility Standard, D26). `version()` is read live off
the loaded library and lands in `expectations.tsv`; nothing is hand-typed.

--- the origin's header, verbatim ---

"""

import ctypes
import ctypes.util
import platform

PCRE2_ZERO_TERMINATED = ctypes.c_size_t(-1).value
PCRE2_UNSET = ctypes.c_size_t(-1).value
PCRE2_ERROR_NOMATCH = -1
PCRE2_ERROR_NOMEMORY = -48

# Compile-time option bits actually used here (pcre2.h, 8-bit build).
PCRE2_MULTILINE = 0x00000400
PCRE2_UTF = 0x00080000  # not used: this module stays byte-oriented like pcrec

_CANDIDATES = ["libpcre2-8.so.0", "libpcre2-8.so"]


def _load():
    last_err = None
    for name in _CANDIDATES:
        try:
            return ctypes.CDLL(name)
        except OSError as e:                       # noqa: PERF203
            last_err = e
            continue
    found = ctypes.util.find_library("pcre2-8")
    if found:
        try:
            return ctypes.CDLL(found)
        except OSError as e:
            last_err = e
    raise RuntimeError(
        "libpcre2-8 runtime not found (tried %r, ctypes.util %r): %s -- "
        "install libpcre2-8-0, or skip the libpcre2 half of this probe."
        % (_CANDIDATES, found, last_err))


_lib = _load()

_lib.pcre2_compile_8.restype = ctypes.c_void_p
_lib.pcre2_compile_8.argtypes = [
    ctypes.c_char_p, ctypes.c_size_t, ctypes.c_uint32,
    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_size_t),
    ctypes.c_void_p]

_lib.pcre2_match_data_create_from_pattern_8.restype = ctypes.c_void_p
_lib.pcre2_match_data_create_from_pattern_8.argtypes = [
    ctypes.c_void_p, ctypes.c_void_p]

_lib.pcre2_match_8.restype = ctypes.c_int
_lib.pcre2_match_8.argtypes = [
    ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_size_t,
    ctypes.c_uint32, ctypes.c_void_p, ctypes.c_void_p]

_lib.pcre2_get_ovector_pointer_8.restype = ctypes.POINTER(ctypes.c_size_t)
_lib.pcre2_get_ovector_pointer_8.argtypes = [ctypes.c_void_p]

_lib.pcre2_match_data_free_8.restype = None
_lib.pcre2_match_data_free_8.argtypes = [ctypes.c_void_p]

_lib.pcre2_code_free_8.restype = None
_lib.pcre2_code_free_8.argtypes = [ctypes.c_void_p]

_lib.pcre2_get_error_message_8.restype = ctypes.c_int
_lib.pcre2_get_error_message_8.argtypes = [
    ctypes.c_int, ctypes.c_char_p, ctypes.c_size_t]

_lib.pcre2_config_8.restype = ctypes.c_int
_lib.pcre2_config_8.argtypes = [ctypes.c_uint32, ctypes.c_void_p]

# [measured] PCRE2_CONFIG_VERSION is 11 on this box's pcre2.h (10.46), read
# by probing pcre2_config_8 with codes 0..15 and picking the one that returns
# a version-looking string ("10.46 2025-08-27") -- the -dev package is not
# installed so the enum could not be read from the header itself.
PCRE2_CONFIG_VERSION = 11


def version():
    """The libpcre2 version string this module actually loaded, for
    source-information headers -- never hand-typed, always read live."""
    buf = ctypes.create_string_buffer(64)
    n = _lib.pcre2_config_8(PCRE2_CONFIG_VERSION, buf)
    return buf.value[:max(n - 1, 0)].decode("latin-1") if n > 0 else "unknown"


class Pcre2Error(Exception):
    pass


def _errmsg(code):
    buf = ctypes.create_string_buffer(256)
    n = _lib.pcre2_get_error_message_8(code, buf, 256)
    return buf.value[:max(n, 0)].decode("latin-1", "replace")


class Compiled:
    """A compiled PCRE2 8-bit pattern. Byte-oriented like pcrec (no UTF)."""

    __slots__ = ("_code",)

    def __init__(self, pattern, options=0):
        if isinstance(pattern, str):
            pattern = pattern.encode("latin-1")
        errcode = ctypes.c_int(0)
        erroff = ctypes.c_size_t(0)
        code = _lib.pcre2_compile_8(
            pattern, len(pattern), options,
            ctypes.byref(errcode), ctypes.byref(erroff), None)
        if not code:
            raise Pcre2Error("pcre2_compile failed at offset %d: %s"
                              % (erroff.value, _errmsg(errcode.value)))
        self._code = code

    def __del__(self):
        if getattr(self, "_code", None):
            _lib.pcre2_code_free_8(self._code)
            self._code = None

    def search(self, subject, start=0):
        """Leftmost match starting the scan at `start`, PCRE2's own
        subject-anchored-at-cursor semantics (like `pcre2_match` with
        startoffset) -- NOT python re.search's re-tries-every-start-position
        behaviour beyond what PCRE2 already does internally for an
        unanchored pattern. Returns (span, groups) like probe_possess.py's
        python-side tuples, or None on no match, so callers can compare
        tuples directly. `groups` is a tuple of (start,end) or None per
        capture group, 1-based order (group 0 excluded, matching
        `re.Match.groups()`)."""
        if isinstance(subject, str):
            subject = subject.encode("latin-1")
        md = _lib.pcre2_match_data_create_from_pattern_8(self._code, None)
        if not md:
            raise MemoryError("pcre2_match_data_create_from_pattern failed")
        try:
            rc = _lib.pcre2_match_8(
                self._code, subject, len(subject), start, 0, md, None)
            if rc == PCRE2_ERROR_NOMATCH:
                return None
            if rc < 0:
                raise Pcre2Error("pcre2_match error %d: %s"
                                  % (rc, _errmsg(rc)))
            ov = _lib.pcre2_get_ovector_pointer_8(md)
            # rc == 0 means the ovector was too small for all groups; the
            # match_data was sized from the pattern's own group count
            # (pcre2_match_data_create_from_pattern_8), so this should not
            # happen -- surfaced rather than silently truncated if it does.
            npairs = rc if rc > 0 else 1
            pairs = [(ov[2 * i], ov[2 * i + 1]) for i in range(npairs)]
            span = (pairs[0][0], pairs[0][1])
            groups = tuple(
                None if s == PCRE2_UNSET else (s, e)
                for s, e in pairs[1:])
            return span, groups
        finally:
            _lib.pcre2_match_data_free_8(md)


def compile(pattern, options=0):                    # noqa: A001 - mirrors re.compile
    return Compiled(pattern, options)




# ---------------------------------------------------------------------------
# pcrec-bench ADDITIONS
# ---------------------------------------------------------------------------

# [measured] Read off this box's libpcre2-8.so.0 by the same discipline as
# PCRE2_CONFIG_VERSION above: the two anchoring bits documented for
# pcre2_match's `options` argument. Verified below in __main__.
PCRE2_ANCHORED = 0x80000000
PCRE2_ENDANCHORED = 0x20000000


def _search_raw(compiled, subject, start, options):
    """The shared body of search/match: returns (span, groups) or None."""
    if isinstance(subject, str):
        subject = subject.encode("latin-1")
    md = _lib.pcre2_match_data_create_from_pattern_8(compiled._code, None)
    if not md:
        raise MemoryError("pcre2_match_data_create_from_pattern failed")
    try:
        rc = _lib.pcre2_match_8(compiled._code, subject, len(subject), start,
                                options, md, None)
        if rc == PCRE2_ERROR_NOMATCH:
            return None
        if rc < 0:
            # NOT folded into "no match": an expectation derived from a
            # give-up would be a wrong answer recorded as ground truth.
            raise Pcre2Error("pcre2_match error %d: %s" % (rc, _errmsg(rc)))
        ov = _lib.pcre2_get_ovector_pointer_8(md)
        npairs = rc if rc > 0 else 1
        pairs = [(ov[2 * i], ov[2 * i + 1]) for i in range(npairs)]
        groups = tuple(None if s == PCRE2_UNSET else (s, e) for s, e in pairs[1:])
        return (pairs[0][0], pairs[0][1]), groups
    finally:
        _lib.pcre2_match_data_free_8(md)


def _match_impl(self, subject, start=0):
    """The MATCH regime (harness contract 3): PCRE2_ANCHORED | ENDANCHORED,
    i.e. the whole subject from `start` must be the match."""
    return _search_raw(self, subject, start, PCRE2_ANCHORED | PCRE2_ENDANCHORED)


def _find_all_impl(self, subject, limit=None):
    """The THROUGHPUT regime's expectation: the FIRST match's span and the
    COUNT of non-overlapping matches, found by the same advance rule both
    drivers use (`pos = max(match_end, pos + 1)`), so the number the oracle
    states is the number a driver can reproduce."""
    if isinstance(subject, str):
        subject = subject.encode("latin-1")
    n = len(subject)
    pos = 0
    count = 0
    first = None
    while pos <= n:
        got = _search_raw(self, subject, pos, 0)
        if got is None:
            break
        (s, e), _g = got
        if first is None:
            first = (s, e)
        count += 1
        pos = e if e > pos else pos + 1
        if limit is not None and count >= limit:
            break
    return first, count


Compiled.match = _match_impl
Compiled.find_all = _find_all_impl


if __name__ == "__main__":
    # Self-check: U9's own witness (docs/dev/upstream_issues.md), so a
    # future reader can see this binding reproduces the recorded divergence
    # rather than trusting the doc.
    print("libpcre2 version:", version())
    rx = compile(r"a?(?:b){0,4}+a")
    m = rx.search("a")
    print("U9 witness a?(?:b){0,4}+a on 'a':", m, "(expected None on PCRE2 10.46)")
    rx2 = compile(r"a{1,3}?")
    print("a{1,3}? on 'aaaa':", rx2.search("aaaa"), "(expected (0,1), ())")

    # pcrec-bench ADDITIONS -- the two anchoring bits and find_all, each with
    # a case whose answer differs between search and match, so a wrong bit
    # value cannot pass by accident.
    rx3 = compile(r"a+")
    assert rx3.search("xaay") == ((1, 3), ()), rx3.search("xaay")
    assert rx3.match("xaay") is None, "ANCHORED must refuse a later start"
    assert rx3.match("aay") is None, "ENDANCHORED must refuse a short match"
    assert rx3.match("aaa") == ((0, 3), ()), rx3.match("aaa")
    assert rx3.find_all("aa b aaa") == ((0, 2), 2), rx3.find_all("aa b aaa")
    print("anchoring bits + find_all: OK")
