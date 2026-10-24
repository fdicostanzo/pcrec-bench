"""subst_template.py -- the NEUTRAL TEMPLATE of the substitution set
([B140], docs/design/subst_bench_v1.md 5.2 and 8a item 4): parse it, give it
a reference meaning, and render it to each engine's replacement dialect.

PURE PYTHON, no engine imported: the set's cases (`bench/subst/cases/<id>/
TEMPLATE.neutral`) name no engine (R-BENCH-4), and every driver/adapter that
later needs a dialect imports THIS module, so "one template" stays true
across eight dialects. The IR spec is `bench/subst/NOTES.md` "The neutral
template (IR)"; this docstring is its machine-side twin.

THE IR. One segment per line, fields TAB-separated, a line starting `#`
is a comment, a blank line is ignored:

    lit<TAB>TEXT     literal bytes; TEXT is raw except the backslash
                     escapes  \\\\  \\n  \\t  \\xHH  (anything else after a
                     backslash is an error, so a stray dialect escape in a
                     template file cannot pass for data)
    grp<TAB>N        capture group N (N >= 1; group 0 is not offered)
    upper<TAB>N      capture group N with ASCII letters forced to upper case
    cond<TAB>N       open a conditional: the segments up to `else`/`end`
                     are emitted iff group N PARTICIPATED in the match
    else             (optional) the segments from here to `end` are emitted
                     iff it did not
    end              close the innermost conditional

`cond` blocks nest. A `grp`/`upper` of group N that is reachable with group
N unset is the template author's error in engines that refuse an unset
reference by default (PCRE2: -55); `unset_refs(ir)` lists the references
that are NOT guarded by a `cond` on the same group so a case can assert it
has none (the oracle is then run WITHOUT PCRE2_SUBSTITUTE_UNSET_EMPTY).

DIALECTS (`render(ir, dialect)`):
    pcre2 | pcrec   `${N}`, `\\\\U${N}\\\\E`, `${N:+yes:no}`; with
                    EXTENDED (implied by upper/cond) a literal `\\\\ $ : }`
                    is escaped, without it only `$` is
    rust | sd | rg  `${N}`, literal `$` as `$$`; no case operators
    re2             `\\\\N` (N <= 9), literal backslash `\\\\\\\\`; no case
                    operators
    sed             GNU `s/../../` right-hand side: `\\\\N` (N <= 9), `\\\\U\\\\N\\\\E`;
                    `/ & \\\\` and newline escaped
    perl            `s///` replacement (double-quotish): `${N}`,
                    `\\\\U${N}\\\\E`; `$ @ \\\\ /` escaped
    python          bytes `re.sub` template: `\\\\g<N>`; backslash doubled; no
                    case operators
A construct a dialect has no spelling for raises `Unsupported(token)`
(tokens: no-case-operators, no-conditional, group-over-9) -- the
`unsupported_reason` the report shows, never a silent approximation.

`evaluate(ir, groups)` is the IR's REFERENCE MEANING (pure python, no
regex): `groups` maps N -> bytes or None (unset); the unit tests render a
hostile template to every dialect whose engine this box has, run that
engine, and require its output to equal `evaluate`'s.
"""

import re

KEYWORDS = ("lit", "grp", "upper", "cond", "else", "end")


class TemplateError(ValueError):
    pass


class Unsupported(Exception):
    """The dialect has no spelling for this IR construct. `.token` is the
    closed `unsupported_reason` vocabulary."""

    def __init__(self, token, detail=""):
        super().__init__("%s%s" % (token, (": " + detail) if detail else ""))
        self.token = token


# ------------------------------------------------------------------ parse

def _unescape(text, where):
    out = bytearray()
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c != 0x5C:
            out.append(c)
            i += 1
            continue
        if i + 1 >= n:
            raise TemplateError("%s: trailing backslash" % where)
        d = text[i + 1]
        if d == 0x5C:
            out.append(0x5C)
            i += 2
        elif d == ord("n"):
            out.append(0x0A)
            i += 2
        elif d == ord("t"):
            out.append(0x09)
            i += 2
        elif d == ord("x") and i + 3 < n + 0 and re.fullmatch(
                rb"[0-9A-Fa-f]{2}", text[i + 2:i + 4]):
            out.append(int(text[i + 2:i + 4], 16))
            i += 4
        else:
            raise TemplateError("%s: unknown escape \\%s"
                                % (where, chr(d)))
    return bytes(out)


def parse(source):
    """bytes (or str) -> a list of segments, each a tuple:
    ('lit', bytes) ('grp', n) ('upper', n) ('cond', n) ('else',) ('end',).
    Conditionals are checked balanced; at most one `else` per block."""
    if isinstance(source, str):
        source = source.encode("latin-1")
    segs = []
    stack = []                       # one bool per open cond: else seen?
    for ln, raw in enumerate(source.split(b"\n"), 1):
        if raw.endswith(b"\r"):
            raise TemplateError("line %d: CR in a template file" % ln)
        if raw == b"" or raw.startswith(b"#"):
            continue
        where = "line %d" % ln
        kw, _, rest = raw.partition(b"\t")
        kw = kw.decode("latin-1")
        if kw not in KEYWORDS:
            raise TemplateError("%s: unknown segment %r" % (where, kw))
        if kw == "lit":
            segs.append(("lit", _unescape(rest, where)))
        elif kw in ("grp", "upper", "cond"):
            if not re.fullmatch(rb"[1-9][0-9]*", rest):
                raise TemplateError("%s: %s needs a group number >= 1, got %r"
                                    % (where, kw, rest))
            segs.append((kw, int(rest)))
            if kw == "cond":
                stack.append(False)
        else:
            if rest:
                raise TemplateError("%s: %s takes no operand" % (where, kw))
            if not stack:
                raise TemplateError("%s: %s outside a cond" % (where, kw))
            if kw == "else":
                if stack[-1]:
                    raise TemplateError("%s: second else in one cond" % where)
                stack[-1] = True
            else:
                stack.pop()
            segs.append((kw,))
    if stack:
        raise TemplateError("unterminated cond (%d open)" % len(stack))
    return segs


def uses(ir):
    """The set of segment kinds in `ir` (for capability checks)."""
    return {s[0] for s in ir}


def needs_extended(ir):
    """True iff the IR needs PCRE2_SUBSTITUTE_EXTENDED (case operators or a
    conditional)."""
    return bool(uses(ir) & {"upper", "cond"})


def max_group(ir):
    return max([s[1] for s in ir if s[0] in ("grp", "upper", "cond")] or [0])


def unset_refs(ir, optional=None):
    """(group, kind) for every grp/upper reference to an OPTIONAL group that
    is NOT lexically inside a `cond` on the same group (in its `then` part)
    -- the references that explode when the group is unset (PCRE2: -55). A
    group is optional if `optional` says so, by default if some `cond` in
    the template guards it (the template's own statement that it may be
    unset); every other group is taken to participate in every match. An
    empty list = safe without UNSET_EMPTY."""
    if optional is None:
        optional = {s[1] for s in ir if s[0] == "cond"}
    bad = []
    guards = []                      # [group, in_then]
    for s in ir:
        k = s[0]
        if k == "cond":
            guards.append([s[1], True])
        elif k == "else":
            guards[-1][1] = False
        elif k == "end":
            guards.pop()
        elif k in ("grp", "upper") and s[1] in optional:
            if not any(g == s[1] and then for g, then in guards):
                bad.append((s[1], k))
    return bad


# ----------------------------------------------------------- the meaning

def evaluate(ir, groups):
    """The IR's reference meaning. `groups`: dict N -> bytes | None. A
    reference to an unset group outside a satisfied guard raises KeyError-
    like TemplateError (the PCRE2 -55 behaviour), never expands to empty."""
    out = bytearray()
    skip = []                        # stack of (emit_then_branch_active)
    emit = True
    state = []                       # per open cond: (parent_emit, was_set)
    for s in ir:
        k = s[0]
        if k == "cond":
            was_set = groups.get(s[1]) is not None
            state.append((emit, was_set))
            emit = emit and was_set
        elif k == "else":
            parent, was_set = state[-1]
            emit = parent and not was_set
        elif k == "end":
            emit = state.pop()[0]
        elif not emit:
            continue
        elif k == "lit":
            out += s[1]
        else:
            v = groups.get(s[1])
            if v is None:
                raise TemplateError("group %d is unset" % s[1])
            out += v.upper() if k == "upper" and False else v
            if k == "upper":
                out[-len(v):] = bytes(
                    b - 32 if 97 <= b <= 122 else b for b in v)
    return bytes(out)


# --------------------------------------------------------------- dialects

def _lit_pcre2(b, extended):
    out = bytearray()
    for c in b:
        ch = bytes([c])
        if ch == b"$":
            out += b"$$"
        elif not extended:
            out += ch
        elif ch in b"\\:}":
            out += b"\\" + ch
        elif ch == b"\n":
            out += b"\\n"
        else:
            out += ch
    return bytes(out)


def _lit_rust(b):
    return b.replace(b"$", b"$$")


def _lit_re2(b):
    return b.replace(b"\\", b"\\\\")


def _lit_sed(b):
    out = bytearray()
    for c in b:
        ch = bytes([c])
        if ch in b"\\/&":
            out += b"\\" + ch
        elif ch == b"\n":
            out += b"\\n"
        else:
            out += ch
    return bytes(out)


def _lit_perl(b):
    out = bytearray()
    for c in b:
        ch = bytes([c])
        if ch in b"\\$@/":
            out += b"\\" + ch
        elif ch == b"\n":
            out += b"\\n"
        else:
            out += ch
    return bytes(out)


def _lit_python(b):
    return b.replace(b"\\", b"\\\\")


def render(ir, dialect, extended=None):
    """-> the replacement text (bytes) in `dialect`."""
    k = set(uses(ir))
    mg = max_group(ir)
    if dialect in ("pcre2", "pcrec"):
        if extended is None:
            extended = needs_extended(ir)
        out = bytearray()
        for s in ir:
            if s[0] == "lit":
                out += _lit_pcre2(s[1], extended)
            elif s[0] == "grp":
                out += b"${%d}" % s[1]
            elif s[0] == "upper":
                out += b"\\U${%d}\\E" % s[1]
            elif s[0] == "cond":
                out += b"${%d:+" % s[1]
            elif s[0] == "else":
                out += b":"
            else:                                   # end
                out += b"}"
        # a cond with no `else` still needs no trailing colon: `${n:+yes}`
        return bytes(out)
    if "cond" in k:
        raise Unsupported("no-conditional", "dialect %s" % dialect)
    if dialect in ("rust", "sd", "rg"):
        if "upper" in k:
            raise Unsupported("no-case-operators", "dialect %s" % dialect)
        return b"".join(_lit_rust(s[1]) if s[0] == "lit" else b"${%d}" % s[1]
                        for s in ir)
    if dialect in ("re2", "sed", "python"):
        if dialect != "python" and mg > 9:
            raise Unsupported("group-over-9", "dialect %s" % dialect)
    if dialect == "re2":
        if "upper" in k:
            raise Unsupported("no-case-operators", "dialect re2")
        return b"".join(_lit_re2(s[1]) if s[0] == "lit" else b"\\%d" % s[1]
                        for s in ir)
    if dialect == "sed":
        out = bytearray()
        for s in ir:
            if s[0] == "lit":
                out += _lit_sed(s[1])
            elif s[0] == "grp":
                out += b"\\%d" % s[1]
            else:
                out += b"\\U\\%d\\E" % s[1]
        return bytes(out)
    if dialect == "perl":
        out = bytearray()
        for s in ir:
            if s[0] == "lit":
                out += _lit_perl(s[1])
            elif s[0] == "grp":
                out += b"${%d}" % s[1]
            else:
                out += b"\\U${%d}\\E" % s[1]
        return bytes(out)
    if dialect == "python":
        if "upper" in k:
            raise Unsupported("no-case-operators", "dialect python")
        return b"".join(_lit_python(s[1]) if s[0] == "lit"
                        else b"\\g<%d>" % s[1] for s in ir)
    raise TemplateError("unknown dialect %r" % dialect)


DIALECTS = ("pcre2", "pcrec", "rust", "sd", "rg", "re2", "sed", "perl",
            "python")
