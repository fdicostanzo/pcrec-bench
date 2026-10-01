"""docs/dev/measurements/probe_b121_counted_repeats.py -- [B121], inbox
I-125 A2/Q7: every pattern in any bench/*/ whose text is (or contains)
a COUNTED repeat -- an explicit `{m,n}`/`{m,}`/`{m}` quantifier, never
a bare `*`/`+`/`?` -- of a GROUP whose body is either:

  MULTI-LITERAL: a single, flat run of 2+ ordinary literal characters
  (no backslash escapes, no classes, no nested groups, no
  alternation) -- the `(?:ab){m,n}` shape I-125's own text names.

  ALL-SINGLETON alternation: 2+ branches, each reducing to exactly one
  literal BYTE (a bare character, or a backslash-escaped literal
  metacharacter like `\\.`/`\\(` -- never a class shorthand such as
  `\\d`/`\\w`/`\\s`, which is not a single definite byte) -- the
  `(?:a|b){m,n}` shape.

Uses pcre_mini_parser.py's real group/alternation structure (never a
flat `[^()]*` text regex, which cannot see past one level of nesting
and would wrongly admit a group containing a NESTED group as if it
were flat). Scans for every `Group` node anywhere in the pattern,
classifies its body by the rule above, and checks whether a counted
quantifier `{...}` immediately follows the group's closing `)` in the
raw text (quantifier syntax itself is not part of the shared parser's
AST -- it is read directly off the text at the group's own end offset,
the one place this probe needs it).

Read-only, no compile, no timing. Run at `nice -n 19`."""
import os
import re
import sys

sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pcrecbench import subbench as _sb
import pcre_mini_parser as M

COUNTED_RE = re.compile(r"\{(\d+)(,(\d*)?)?\}[?+]?")

# backslash-escaped atoms whose second character is a DEFINITE single
# literal byte (either a non-alphanumeric metacharacter escape, or one
# of these recognised single-byte control letters) -- everything else
# (class shorthand d/w/s/D/W/S, anchors b/B/A/Z/z/G, \K/\N/\R/\X/\C,
# \p/\P properties, \Q/\E quoting markers, \g/\k backref syntax, a
# bare digit backreference) is NOT counted as a definite single byte.
SINGLE_BYTE_ESCAPE_LETTERS = set("nrtfae0")


def literal_char_len(atom_text):
    """-> 1 if `atom_text` (a Literal atom's raw text) is DEFINITELY
    exactly one literal byte; else None. A bare non-backslash character
    always qualifies; a 2-char backslash pair qualifies iff its second
    character is punctuation or one of SINGLE_BYTE_ESCAPE_LETTERS."""
    if len(atom_text) == 1 and atom_text != "\\":
        return 1
    if len(atom_text) == 2 and atom_text[0] == "\\":
        c = atom_text[1]
        if not c.isalnum() or c in SINGLE_BYTE_ESCAPE_LETTERS:
            return 1
    return None


def classify_group_body(inner):
    """`inner` is the Group's own Alt. -> "multi-literal", "all-singleton",
    or None (neither shape)."""
    if len(inner.branches) == 1:
        seq = inner.branches[0]
        if len(seq.atoms) < 2:
            return None
        lits = 0
        for atom in seq.atoms:
            if not isinstance(atom, M.Literal):
                return None
            if literal_char_len(atom.text) != 1:
                return None
            lits += 1
        return "multi-literal" if lits >= 2 else None
    if len(inner.branches) >= 2:
        for seq in inner.branches:
            if len(seq.atoms) != 1:
                return None
            atom = seq.atoms[0]
            if not isinstance(atom, M.Literal):
                return None
            if literal_char_len(atom.text) != 1:
                return None
        return "all-singleton"
    return None


def walk_groups(alt, out):
    for seq in alt.branches:
        for atom in seq.atoms:
            if isinstance(atom, M.Group):
                out.append(atom)
                walk_groups(atom.inner, out)


def subbench_dirs():
    root = os.path.join(os.getcwd(), "bench")
    out = []
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        if os.path.exists(os.path.join(path, "subbench.toml")):
            out.append((name, path))
    return out


def main():
    total = 0
    hits = []
    for name, _path in subbench_dirs():
        sb = _sb.find(name)
        for p in sb.patterns:
            total += 1
            raw = sb.pattern_bytes(p.name)
            text = raw.decode("latin-1")
            alt = M.parse(text)
            groups = []
            walk_groups(alt, groups)
            seen_spans = set()
            for g in groups:
                kind = classify_group_body(g.inner)
                if kind is None:
                    continue
                m = COUNTED_RE.match(text, g.span[1])
                if not m:
                    continue
                key = (g.span, m.span())
                if key in seen_spans:
                    continue
                seen_spans.add(key)
                hits.append((name, p.name, raw, kind, g.span, text[g.span[0]:m.end()],
                              list(sb.regimes)))
    print("patterns examined (all bench/*/): %d" % total)
    print("counted-repeat (multi-literal / all-singleton) hits: %d" % len(hits))
    print()
    for name, pname, raw, kind, span, snippet, regimes in hits:
        print("sub-bench: %s" % name)
        print("pattern:   %s" % pname)
        print("full text: %r" % raw)
        print("kind:      %s" % kind)
        print("matched:   %r  (span %r)" % (snippet, span))
        print("regimes:   %s" % regimes)
        print()


if __name__ == "__main__":
    main()
