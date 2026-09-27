#!/usr/bin/env python3
"""docs/dev/measurements/probe_tre_bracket_escape_census.py

U6 follow-up (manager review, 2026-09-27): which bench/*/patterns/*.rx
files contain a bracket expression `[...]` with a backslash inside it --
the exact shape TRE (and glibc's own POSIX regcomp -- confirmed AGREEING,
docs/dev/upstream/repro/U6/) parses with backslash carrying NO special
meaning, per POSIX.1-2017 XBD 9.3.5. Read-only: no pattern is compiled
here, this only classifies pattern TEXT. Never loads the record store;
cross-referencing against measured store rows is a SEPARATE manual step
(see the archived .txt's own annotations, not this script's output).

Bracket-span extraction mirrors the POSIX/PCRE-shared convention: a `]`
immediately after `[` or `[^` is a literal member, not the closing
bracket -- everything else is scanned char-by-char with backslash given
NO escaping power while inside the class (the very reading this census
exists to find, not assumed away).

Usage: python3 docs/dev/measurements/probe_tre_bracket_escape_census.py
  (run from the repo root; no arguments, no side effects)
"""
import glob
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def find_bracket_spans(text):
    """Yield (start, end, content) for each top-level [...] span in
    TEXT, POSIX-style: a `]` right after `[` or `[^` doesn't close it."""
    spans = []
    i = 0
    n = len(text)
    while i < n:
        if text[i] == "[":
            j = i + 1
            if j < n and text[j] == "^":
                j += 1
            if j < n and text[j] == "]":
                j += 1  # literal ] as first member
            while j < n and text[j] != "]":
                j += 1
            if j < n:  # found closing ]
                spans.append((i, j + 1, text[i + 1:j]))
                i = j + 1
                continue
        i += 1
    return spans


def main():
    rows = []
    for rxfile in sorted(glob.glob(os.path.join(ROOT, "bench", "*", "patterns", "*.rx"))):
        subbench = os.path.basename(os.path.dirname(os.path.dirname(rxfile)))
        pattern_id = os.path.splitext(os.path.basename(rxfile))[0]
        with open(rxfile, "rb") as f:
            raw = f.read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = raw.decode("latin-1")
        for (_s, _e, content) in find_bracket_spans(text):
            if "\\" in content:
                rows.append((subbench, pattern_id, content))

    print("subbench\tpattern_id\tbracket_content_with_backslash")
    for (subbench, pattern_id, content) in rows:
        disp = content.replace("\t", "\\t").replace("\n", "\\n")
        print(f"{subbench}\t{pattern_id}\t[{disp}]")

    distinct = sorted(set((r[0], r[1]) for r in rows))
    print(f"\n# total: {len(rows)} bracket-span hits across "
          f"{len(distinct)} distinct (subbench, pattern) pairs",
          file=sys.stderr)
    by_subbench = {}
    for (sb, pid) in distinct:
        by_subbench.setdefault(sb, []).append(pid)
    for sb in sorted(by_subbench):
        print(f"#   {sb}: {len(by_subbench[sb])} pattern(s) -- "
              f"{', '.join(sorted(by_subbench[sb]))}", file=sys.stderr)


if __name__ == "__main__":
    main()
