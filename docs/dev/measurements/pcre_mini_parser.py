"""docs/dev/measurements/pcre_mini_parser.py -- a SHARED, minimal
recursive-descent structural parser for the two [B121] probes
(probe_b121_counted_repeats.py, A2/Q7; probe_b121_nontop_caret.py,
A3/Q6) that both need real regex STRUCTURE (group nesting, alternation
branches) rather than a flat text regex over `[^()]*`. Not a full PCRE
parser: it does not interpret quantifier/anchor/class SEMANTICS beyond
what each probe needs (group boundaries, alternation branches at each
depth, `^` positions, character-class extents, `\\Q...\\E` quoting,
escape-pair skipping) -- exactly the structural facts both asks turn
on. Deliberately conservative: `(?...)` prefix characters (`?:`, `?=`,
`?<name>`, `?i`, ...) are parsed as ordinary literal atoms inside the
group's own body scan, which is harmless for every purpose here (none
of those prefix characters are `(`, `)`, `|`, `^`, or `[`) except
`(?#...)` comments, handled explicitly (no structure inside).

AST nodes (plain objects, no behaviour beyond what the probes read):
  Alt(branches: list[Seq])          -- `a|b|c`
  Seq(atoms: list[Atom], span)      -- a flat run between `|`/`)`/start/end
  Group(inner: Alt, span)           -- a group whose BODY was parsed as
                                        real structure: `(...)` (capturing),
                                        `(?:...)`, `(?=...)`, `(?!...)`,
                                        `(?<=...)`, `(?<!...)`, `(?<name>...)`,
                                        `(?P<name>...)`, `(?'name'...)` -- the
                                        PREFIX TOKEN ITSELF (`?:`, `?<name>`,
                                        ...) is consumed and never appears as
                                        a literal atom inside `inner` (the
                                        bug this module's own self-test
                                        caught: naively parsing `?`/`:` as
                                        ordinary literal atoms defeats the
                                        "is this group the SOLE atom of its
                                        containing Seq" check every
                                        non-capturing/lookaround group needs)
  Caret(pos)                        -- a real `^` anchor atom
  Literal(text, span)               -- one or more literal characters
                                        (an escape pair, a `\\Q...\\E`
                                        run, or one ordinary character)
  CharClass(span)                   -- `[...]`, opaque (its content is
                                        never scanned for `(`/`)`/`|`/`^`)
  Comment(span)                     -- `(?#...)`, opaque
  Opaque(span)                      -- any OTHER `(?...)` construct this
                                        module does not give real structure
                                        to (conditionals `(?(...)...)`,
                                        branch-reset `(?|...)`, recursion
                                        `(?R)`/`(?1)`/`(?-1)`/`(?+1)`,
                                        subroutine calls `(?&name)`/
                                        `(?P>name)`, named backreferences
                                        `(?P=name)`, callouts `(?C...)`,
                                        inline-flag-only groups `(?i)` etc.,
                                        extended classes `(?[...])`) --
                                        found via a BALANCED paren/escape/
                                        class scan to the matching `)`, with
                                        NO recursion inside: a `^` inside one
                                        of these is INVISIBLE to
                                        `find_carets` by construction. This
                                        is checked EMPTY over the real
                                        corpus by `check_no_caret_in_opaque`
                                        below, not merely assumed -- every
                                        probe that imports this module calls
                                        it once and fails loudly if it ever
                                        finds a `^` byte inside an Opaque
                                        span, rather than silently
                                        under-reporting A3/Q6.

`span` is the (start, end) byte offset pair in the ORIGINAL text
(end exclusive), used to test "this group spans the whole pattern".
"""


class Alt:
    __slots__ = ("branches",)
    def __init__(self, branches):
        self.branches = branches


class Seq:
    __slots__ = ("atoms", "span")
    def __init__(self, atoms, span):
        self.atoms = atoms
        self.span = span


class Group:
    __slots__ = ("inner", "span")
    def __init__(self, inner, span):
        self.inner = inner
        self.span = span


class Caret:
    __slots__ = ("pos",)
    def __init__(self, pos):
        self.pos = pos


class Literal:
    __slots__ = ("text", "span")
    def __init__(self, text, span):
        self.text = text
        self.span = span


class CharClass:
    __slots__ = ("span",)
    def __init__(self, span):
        self.span = span


class Comment:
    __slots__ = ("span",)
    def __init__(self, span):
        self.span = span


class Opaque:
    __slots__ = ("span",)
    def __init__(self, span):
        self.span = span


class ParseError(Exception):
    pass


def parse(text):
    """-> Alt. `text` MUST be `str` (decode pattern bytes with
    `.decode("latin-1")` first -- a lossless, 1-byte-per-char mapping,
    so every offset in the returned AST is a byte offset into the
    ORIGINAL bytes unchanged). Raises ParseError on an unbalanced
    structure (unmatched `(`/`)`, an unterminated `[...]`) -- a probe
    treats that pattern as UNPARSEABLE and reports it by name rather
    than guessing."""
    if isinstance(text, bytes):
        raise TypeError("parse() takes str (decode latin-1 first), got bytes")
    alt, i = _parse_alt(text, 0)
    if i != len(text):
        raise ParseError("trailing unparsed text at offset %d: %r"
                          % (i, text[i:i + 20]))
    return alt


def _parse_alt(text, i):
    branches = []
    seq, i = _parse_seq(text, i)
    branches.append(seq)
    while i < len(text) and text[i] == "|":
        i += 1
        seq, i = _parse_seq(text, i)
        branches.append(seq)
    return Alt(branches), i


def _parse_seq(text, i):
    start = i
    atoms = []
    n = len(text)
    while i < n:
        c = text[i]
        if c == "|" or c == ")":
            break
        atom, i = _parse_atom(text, i)
        atoms.append(atom)
    return Seq(atoms, (start, i)), i


def _parse_atom(text, i):
    n = len(text)
    c = text[i]
    if c == "^":
        return Caret(i), i + 1
    if c == "\\":
        if text[i:i + 2] == "\\Q":
            j = text.find("\\E", i + 2)
            end = (j + 2) if j != -1 else n
            return Literal(text[i:end], (i, end)), end
        end = min(i + 2, n)
        return Literal(text[i:end], (i, end)), end
    if c == "[":
        j = i + 1
        if j < n and text[j] == "^":
            j += 1
        if j < n and text[j] == "]":
            j += 1
        while j < n and text[j] != "]":
            if text[j] == "\\":
                j += 2
            else:
                j += 1
        if j >= n:
            raise ParseError("unterminated [...] starting at offset %d" % i)
        j += 1
        return CharClass((i, j)), j
    if c == "(":
        return _parse_group(text, i)
    return Literal(c, (i, i + 1)), i + 1


def _parse_group(text, i):
    """text[i] == '('. -> (node, next_i). Consumes any recognised
    `(?...` prefix token BEFORE recursing into the body, so the body's
    own Seq reflects only the real content (see the Group docstring
    above for why this matters)."""
    n = len(text)
    if text[i:i + 3] == "(?#":
        j = text.find(")", i + 3)
        if j == -1:
            raise ParseError("unterminated (?#...) starting at offset %d" % i)
        return Comment((i, j + 1)), j + 1
    if text[i + 1:i + 2] != "?":
        # plain capturing group: (...)
        return _parse_group_body(text, i, i + 1)
    j = i + 2
    if j < n and text[j] == ":":
        return _parse_group_body(text, i, j + 1)
    if j < n and text[j] in "=!>":
        return _parse_group_body(text, i, j + 1)
    if j < n and text[j] == "<" and j + 1 < n and text[j + 1] in "=!":
        return _parse_group_body(text, i, j + 2)
    if j < n and text[j] == "<":
        k = text.find(">", j)
        if k == -1:
            raise ParseError("unterminated (?<name> starting at offset %d" % i)
        return _parse_group_body(text, i, k + 1)
    if j + 1 < n and text[j] == "P" and text[j + 1] == "<":
        k = text.find(">", j + 2)
        if k == -1:
            raise ParseError("unterminated (?P<name> starting at offset %d" % i)
        return _parse_group_body(text, i, k + 1)
    if j < n and text[j] == "'":
        k = text.find("'", j + 1)
        if k == -1:
            raise ParseError("unterminated (?'name' starting at offset %d" % i)
        return _parse_group_body(text, i, k + 1)
    if j < n and text[j] == "(":
        # conditional (?(COND)yes|no) -- COND is skipped OPAQUELY (a
        # balanced scan, same rule any other construct's own nested
        # parens get), but the yes|no part gets REAL Alt structure, so
        # a `^` inside a conditional's branch is still found.
        cond_end = _find_matching_close(text, j)
        return _parse_group_body(text, i, cond_end)
    if j < n and text[j] in "imsxJUXun^-":
        # inline-flags directive: (?flags) resets/sets options for the
        # rest of the ENCLOSING group with no body of its own (treated
        # as a REAL, empty-body Group -- harmless, since it can never
        # contain a '^'), or (?flags:...) scopes a real body.
        k = j
        while k < n and text[k] in "imsxJUXun^-":
            k += 1
        if k < n and text[k] == ":":
            return _parse_group_body(text, i, k + 1)
        if k < n and text[k] == ")":
            return _parse_group_body(text, i, k)  # empty body, ')' right there
        # text[k] is something else ((?ia -- not a flag letter nor ':'
        # nor ')'): fall through to the opaque fallback below, which is
        # still SAFE (no flag letter is '^' used as an anchor).
    # everything else ((?|, (?R, (?1, (?-1, (?+1, (?&name),
    # (?P=name, (?P>name, (?C..., (?i)/(?i:/(?-i..., (?[...]) -- OPAQUE,
    # a balanced scan to the matching ')', no recursion inside.
    close = _find_matching_close(text, i)
    return Opaque((i, close)), close


def _parse_group_body(text, i, body_start):
    inner, k = _parse_alt(text, body_start)
    n = len(text)
    if k >= n or text[k] != ")":
        raise ParseError("unmatched ( at offset %d" % i)
    return Group(inner, (i, k + 1)), k + 1


def _find_matching_close(text, i):
    """text[i] == '('. -> the offset right AFTER its matching ')',
    via a balanced depth scan that still respects escapes and
    `[...]` classes (so a class like `[)]` or an escaped `\\)` inside
    an opaque construct's own sub-parens, e.g. a callout argument,
    cannot desynchronise the count)."""
    n = len(text)
    depth = 0
    j = i
    while j < n:
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if c == "[":
            k = j + 1
            if k < n and text[k] == "^":
                k += 1
            if k < n and text[k] == "]":
                k += 1
            while k < n and text[k] != "]":
                if text[k] == "\\":
                    k += 2
                else:
                    k += 1
            j = k + 1
            continue
        if c == "(":
            depth += 1
            j += 1
            continue
        if c == ")":
            depth -= 1
            j += 1
            if depth == 0:
                return j
            continue
        j += 1
    raise ParseError("unmatched ( at offset %d (opaque scan)" % i)


def all_carets_text(text):
    """-> the set of byte offsets of every LITERAL '^' character in
    `text` outside any \\-escape and outside any [...] class -- a
    second, independent, much simpler scan used only to cross-check
    `find_carets`'s own population (every real Caret atom it finds)
    plus `check_no_caret_in_opaque` (every '^' inside an Opaque span)
    together account for every one."""
    out = set()
    n = len(text)
    j = 0
    while j < n:
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if c == "[":
            k = j + 1
            if k < n and text[k] == "^":
                k += 1
            if k < n and text[k] == "]":
                k += 1
            while k < n and text[k] != "]":
                if text[k] == "\\":
                    k += 2
                else:
                    k += 1
            j = k + 1
            continue
        if c == "^":
            out.add(j)
        j += 1
    return out


def opaque_spans(alt, out=None):
    """-> every Opaque/Comment/CharClass node's span in `alt`, walked
    recursively through every real Group -- what check_no_caret_in_opaque
    scans for a stray '^' byte."""
    if out is None:
        out = []
    for seq in alt.branches:
        for atom in seq.atoms:
            if isinstance(atom, (Opaque, Comment, CharClass)):
                out.append(atom.span)
            elif isinstance(atom, Group):
                opaque_spans(atom.inner, out)
    return out


def check_no_caret_in_opaque(text, alt):
    """Raises ParseError if any Opaque/Comment span in `alt` contains a
    literal, UNESCAPED '^' byte outside its own nested `[...]` classes
    -- the guard named in the module docstring. CharClass spans are
    EXCLUDED from this scan entirely: a class's '^' (negation, at
    relative offset 1 in `[^...]`) is not an anchor and was never a
    candidate for `find_carets` in the first place, by the same rule
    `_parse_atom`'s own `[` handling already applies everywhere else."""
    bad = []
    for (s, e) in opaque_spans(alt):
        if text[s] == "[":
            continue  # a CharClass span: its own '^' is negation, not an anchor
        span_text = text[s:e]
        j = 0
        n = len(span_text)
        while j < n:
            c = span_text[j]
            if c == "\\":
                j += 2
                continue
            if c == "[":
                k = j + 1
                if k < n and span_text[k] == "^":
                    k += 1
                if k < n and span_text[k] == "]":
                    k += 1
                while k < n and span_text[k] != "]":
                    if span_text[k] == "\\":
                        k += 2
                    else:
                        k += 1
                j = k + 1
                continue
            if c == "^":
                bad.append(s + j)
            j += 1
    if bad:
        raise ParseError("'^' found inside an opaque (unparsed) span at "
                          "offset(s) %r -- pcre_mini_parser needs a real "
                          "rule for this construct" % bad)


def find_carets(alt, flag=False, out=None):
    """-> list of (pos, flagged) for every real ^ anchor atom in `alt`.
    `flagged` is True iff an ancestor Alt has >1 branches, OR an
    ancestor Group is not the sole atom of its own containing Seq --
    the A3/Q6 predicate, shared verbatim by both probes that need it
    (only probe_b121_nontop_caret.py reports it; A2 does not need carets
    at all, but keeping this one function in the shared module avoids
    two copies of the same walk)."""
    if out is None:
        out = []
    branch_flag = flag or (len(alt.branches) > 1)
    for seq in alt.branches:
        sole = (len(seq.atoms) == 1)
        for atom in seq.atoms:
            if isinstance(atom, Caret):
                out.append((atom.pos, branch_flag))
            elif isinstance(atom, Group):
                group_flag = branch_flag or (not sole)
                find_carets(atom.inner, group_flag, out)
    return out
