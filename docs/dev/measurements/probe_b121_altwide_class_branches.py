"""docs/dev/measurements/probe_b121_altwide_class_branches.py -- [B121],
inbox I-125 A4/Q8: every >=8-branch alternation, anywhere in any
bench/*/ pattern, where at least one branch contains a character class
(`[...]`) -- either as a CLASS TAIL (the branch's last atom is a
CharClass, e.g. `ab[cd]`/`foo[0-9]`) or as a CLASS MEMBER anywhere else
in the branch (e.g. `[ab]x`/`[ac]y`). Uses pcre_mini_parser.py's real
Alt/Seq structure (an Alt node's own `branches` list IS the
alternation; no text-regex guesswork about where one branch ends and
the next begins across nested groups).

Read-only, no compile, no timing. Run at `nice -n 19`."""
import os
import sys

sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pcrecbench import subbench as _sb
import pcre_mini_parser as M


def walk_alts(alt, out):
    out.append(alt)
    for seq in alt.branches:
        for atom in seq.atoms:
            if isinstance(atom, M.Group):
                walk_alts(atom.inner, out)


def classify_branch(seq):
    """-> "tail" if the branch's LAST atom is a CharClass, "member" if
    some OTHER atom is a CharClass, None if the branch has no class at
    all."""
    classes = [i for i, a in enumerate(seq.atoms) if isinstance(a, M.CharClass)]
    if not classes:
        return None
    return "tail" if classes[-1] == len(seq.atoms) - 1 else "member"


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
            root_alt = M.parse(text)
            alts = []
            walk_alts(root_alt, alts)
            for alt in alts:
                if len(alt.branches) < 8:
                    continue
                kinds = [classify_branch(seq) for seq in alt.branches]
                if any(k is not None for k in kinds):
                    hits.append((name, p.name, raw, len(alt.branches), kinds,
                                  list(sb.regimes)))
    print("patterns examined (all bench/*/): %d" % total)
    print(">=8-branch alternations with a class tail/member branch: %d"
          % len(hits))
    print()
    for name, pname, raw, nbranches, kinds, regimes in hits:
        print("sub-bench: %s" % name)
        print("pattern:   %s" % pname)
        print("full text: %r" % raw)
        print("branches:  %d" % nbranches)
        print("per-branch class kind: %s" % kinds)
        print("regimes:   %s" % regimes)
        print()
    if not hits:
        print("NONE FOUND.")


if __name__ == "__main__":
    main()
