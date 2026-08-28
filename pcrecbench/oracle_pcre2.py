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
    never be silently recorded as an expectation;
  * `pattern_info()` ([B11.1]) -- PCRE2's own start-of-match analysis: the
    FIRST code unit and, the one a bench over failing subjects turns on, the
    REQUIRED code unit (`req_cu`: the byte that must occur somewhere in any
    match, on which `pcre2_match` dismisses a subject without running the
    automaton). A pattern with none is a pattern no required-byte precheck
    can help, and `bench/loglines` states that per pattern FROM HERE rather
    than from a reading of the syntax.

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


# PATTERN INFO: what PCRE2's own start-of-match analysis found ([B11.1]).
#
# [measured] The PCRE2_INFO_* codes below were read off THIS box's
# libpcre2-8.so.0 by the same discipline as PCRE2_CONFIG_VERSION (the -dev
# package is not installed, so the enum cannot be read from a header): probe
# `pcre2_pattern_info_8` with codes 0..25 on patterns whose answers are known
# by construction. `abc` gives 97 ('a') at code 5 and 99 ('c') at code 11,
# with 1 at codes 6 and 12; `[0-9]{4}` gives 0 at 6 AND at 12 with a non-null
# bitmap pointer at 7 -- a pattern with a first-code-unit BITMAP and NO
# required code unit. The __main__ self-check below re-runs exactly that, so a
# wrong code cannot pass silently.
PCRE2_INFO_FIRSTCODEUNIT = 5
PCRE2_INFO_FIRSTCODETYPE = 6
PCRE2_INFO_LASTCODEUNIT = 11
PCRE2_INFO_LASTCODETYPE = 12
PCRE2_INFO_MINLENGTH = 16

_lib.pcre2_pattern_info_8.restype = ctypes.c_int
_lib.pcre2_pattern_info_8.argtypes = [ctypes.c_void_p, ctypes.c_uint32,
                                      ctypes.c_void_p]


def _info_u32(compiled, code):
    v = ctypes.c_uint32(0)
    rc = _lib.pcre2_pattern_info_8(compiled._code, code, ctypes.byref(v))
    if rc != 0:
        raise Pcre2Error("pcre2_pattern_info(%d) error %d: %s"
                         % (code, rc, _errmsg(rc)))
    return v.value


def _pattern_info_impl(self):
    """PCRE2's own start-of-match analysis, as a dict.

    `required_code_unit` is the one a bench measuring FAILING subjects cares
    about: the byte PCRE2 knows must occur SOMEWHERE in any match, which lets
    `pcre2_match` dismiss a subject that does not contain it without running
    the automaton at all (upstream's `req_cu`). `first_code_unit` is the
    separate leading-byte analysis, and is None when PCRE2 has a start BITMAP
    or nothing instead of a single byte.

    A `*_code_type` of 0 means the analysis found nothing. For `required_` in
    particular that means NO required byte exists and a required-byte precheck
    cannot help the pattern at all -- which is a fact about the pattern that a
    sub-bench should be able to STATE from the engine rather than assert from
    a reading of the syntax."""
    ftype = _info_u32(self, PCRE2_INFO_FIRSTCODETYPE)
    ltype = _info_u32(self, PCRE2_INFO_LASTCODETYPE)
    return {
        "first_code_type": ftype,
        "first_code_unit": (_info_u32(self, PCRE2_INFO_FIRSTCODEUNIT)
                            if ftype == 1 else None),
        "required_code_type": ltype,
        "required_code_unit": (_info_u32(self, PCRE2_INFO_LASTCODEUNIT)
                               if ltype == 1 else None),
        "min_length": _info_u32(self, PCRE2_INFO_MINLENGTH),
    }


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
Compiled.pattern_info = _pattern_info_impl


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

    # pattern_info: the PCRE2_INFO_* codes, on two patterns whose analysis is
    # known by construction. `abc` must report a first unit 'a' AND a required
    # unit 'c'; `[0-9]{4}` must report NEITHER (a bitmap, and no req_cu) --
    # so a code that happened to name a different field cannot pass, and the
    # "no required byte" case this bench's control patterns rest on is
    # exercised here rather than trusted.
    i1 = compile(r"abc").pattern_info()
    assert i1["first_code_unit"] == ord("a"), i1
    assert i1["required_code_unit"] == ord("c"), i1
    assert i1["min_length"] == 3, i1
    i2 = compile(r"[0-9]{4}").pattern_info()
    assert i2["first_code_unit"] is None and i2["first_code_type"] == 0, i2
    assert i2["required_code_unit"] is None and i2["required_code_type"] == 0, i2
    assert i2["min_length"] == 4, i2
    print("pattern_info (first / required code unit): OK")
