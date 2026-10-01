"""docs/dev/measurements/probe_b121_nontop_caret.py -- [B121], inbox
I-125 A3/Q6: every pattern in any bench/*/ whose text contains a `^`
that is NOT at the pattern's structural top level -- inside an
alternation branch (at ANY depth, including the pattern's own top-level
alternation: `a|^b` counts) or inside a group that does not span the
whole pattern. PARSED PROPERLY via pcre_mini_parser.py's real
recursive-descent structure (group nesting, alternation branches,
`(?...)` prefix consumption, `\\Q...\\E` quoting, escape pairs,
char-class extents) -- never a flat `[^()]*`-shaped text regex, which
cannot see past one level of nesting and cannot tell a CLASS's `[^...]`
negation marker from a real anchor.

A `^`'s FLAGGED status is pcre_mini_parser.find_carets's own rule:
flagged iff an ancestor Alt has more than one branch, OR an ancestor
Group's own containing Seq is not JUST that group (so the group is not
"the whole pattern" at its own nesting level). Validated clean over the
whole corpus by probe_b121_parser_selftest.py first (0 parse failures,
0 opaque-caret misses, 0 cross-check mismatches against an independent
dumb text scan) -- this probe trusts that result rather than
re-deriving it.

Reports every (sub-bench, pattern) with >=1 flagged `^`, its raw text,
every flagged offset, and the sub-bench's declared regimes (shared by
every pattern in that set, pcrecbench.subbench.Subbench.regimes --
there is no per-pattern regime subset in today's schema). Read-only, no
compile, no timing. Run at `nice -n 19`."""
import os
import sys

sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pcrecbench import subbench as _sb
import pcre_mini_parser as M


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
            M.check_no_caret_in_opaque(text, alt)
            carets = M.find_carets(alt)
            flagged = [pos for pos, fl in carets if fl]
            if flagged:
                hits.append((name, p.name, raw, flagged, list(sb.regimes)))
    print("patterns examined (all bench/*/): %d" % total)
    print("patterns with >=1 non-top-level '^': %d" % len(hits))
    print()
    for name, pname, raw, flagged, regimes in hits:
        print("sub-bench: %s" % name)
        print("pattern:   %s" % pname)
        print("text:      %r" % raw)
        print("flagged offset(s): %s" % flagged)
        print("regimes:   %s" % regimes)
        print()


if __name__ == "__main__":
    main()
