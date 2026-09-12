#!/usr/bin/env python3
"""Reproduce docs/dev/measurements/2026-09-12-rxt-format-probes-d34c9131.txt.

[B42] lane b42rxtneeds, 2026-09-12. Twenty PARSE-ONLY probes of pcrec's
`.rxt` source grammar at the pinned binary, written for
`docs/design/rxt_needs_v1.md` §1.9 — the note that carries this project's
`.rxt` capability feedback to pcrecdev1. Each probe writes a tiny `.rxt`
fixture to a temp directory, runs `pcrec --list-source` on it, and prints
the fixture, the exit code, every data row and (where the probe is about
byte fidelity) the decoded pattern column against the bytes that went in.

NOTHING HERE IS A TIMING. No compile, no artifact, no dlopen, no driver,
no engine run — `--list-source` parses and prints. So this file's archive
carries no load samples and no gate verdict, and the box's state cannot
affect a single character of it. That is the one respect in which it
departs from this directory's rule 3, and it departs by having nothing to
report rather than by omitting something.

    python3 docs/dev/measurements/probe_rxt_format.py

Defaults to the pin's binary under `build/`; override with $PCREC_BIN.
Run from a git WORKTREE, `build/` belongs to the main checkout, so the
resolver also looks one level up from the git common directory.
"""

import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
PIN_REL = os.path.join("build", "pcrec-d34c9131", "build", "pcrec")


def default_bin():
    """The pin's binary. `build/` lives in the MAIN checkout, so a run from
    a worktree falls back to the git common directory's parent."""
    cands = [os.path.join(ROOT, PIN_REL)]
    try:
        common = subprocess.run(
            ["git", "-C", ROOT, "rev-parse", "--git-common-dir"],
            capture_output=True, text=True).stdout.strip()
        if common:
            if not os.path.isabs(common):
                common = os.path.join(ROOT, common)
            cands.append(os.path.join(os.path.dirname(common), PIN_REL))
    except Exception:                                         # noqa: BLE001
        pass
    for c in cands:
        if os.path.exists(c):
            return c
    return cands[0]

# `--list-source`'s own TSV-safety escaping (columns 4/5/15), decoded here
# so a pattern column can be compared against the fixture's raw bytes.
# Same vocabulary tools/export_rxt.py's decode_rxt_escape implements; kept
# separate and byte-level so a non-UTF-8 column never has to become str.
_E = {ord("\\"): 0x5C, ord("t"): 0x09, ord("n"): 0x0A, ord("r"): 0x0D}
_H = set(b"0123456789abcdefABCDEF")


def decode(b):
    out, i, n = bytearray(), 0, len(b)
    while i < n:
        if b[i] == 0x5C and i + 1 < n:
            c2 = b[i + 1]
            if c2 in _E:
                out.append(_E[c2]); i += 2; continue
            if c2 == ord("x") and i + 3 < n and b[i + 2] in _H and b[i + 3] in _H:
                out.append(int(b[i + 2:i + 4], 16)); i += 4; continue
        out.append(b[i]); i += 1
    return bytes(out)


# (id, description, fixture bytes, expected pattern bytes or None)
PROBES = [
    ("M1", "a literal NUL inside a pattern line",
     b"pattern ab\x00cd\nname h\n", b"ab\x00cd"),
    ("M2", "a pattern line ending CRLF",
     b"pattern abc\r\nname h\n", b"abc\r"),
    ("M3", "raw high bytes (not valid UTF-8) in a pattern",
     b"pattern caf\xe9[\x80-\xff]+\nname h\n", b"caf\xe9[\x80-\xff]+"),
    ("M4a", "a literal TAB mid-pattern",
     b"pattern a\tb\nname h\n", b"a\tb"),
    ("M4b", "a doubled backslash",
     b"pattern a\\\\b\nname h\n", b"a\\\\b"),
    ("M4c", "a CR that is NOT before the line end",
     b"pattern a\rb\nname h\n", b"a\rb"),
    ("M4d", "trailing spaces after a pattern (rest-of-line is data)",
     b"pattern abc   \nname h\n", b"abc   "),
    ("M5", "two `description` lines in one pattern block",
     b"pattern abc\nname p1\ndescription first\ndescription second\n", None),
    ("M6a", "a block name carrying `-` and `.` (the widened grammar)",
     b"pattern abc\nname crs-942.160\n", None),
    ("M6b", "a block name carrying uppercase",
     b"pattern abc\nname Upper.Name-1\n", None),
    ("M7", "two blocks with the same name",
     b"pattern abc\nname dup\npattern def\nname dup\n", None),
    ("M8", "a (?x) pattern continued on an indented second line",
     b"pattern (?x) a  # comment\n  b\nname freespc\n", None),
    ("M9", "a 20,000-byte pattern line",
     b"pattern " + b"a" * 20000 + b"\nname long1\n", None),
    ("M10a", "`tag` at block scope (W2)",
     b"pattern abc\nname t1\ntag family=wild hazard=none\n", None),
    ("M10b", "`variant` at block scope (W3)",
     b"pattern abc\nname t1\nvariant re2 unsupported no backrefs\n", None),
    ("M10c", "`oracle` at head scope (W3)",
     b"oracle pcre2\npattern abc\nname t1\n", None),
    ("M10d", "`include` at head scope (W2)",
     b'include "frag.rxt"\npattern abc\nname t1\n', None),
    ("M12", "an authored head + two blocks, NO target and NO config",
     b"# capability@0.1\ndescription |\n  The capability survey set.\n"
     b"  Second line.\n\npattern ^a+$\nname wild-one\n"
     b"description first member\n\npattern b|c\nname wild-two\n", None),
    ("M13", "`pattern #` -- a floor pattern, not a comment",
     b"pattern #\nname floor\n", b"#"),
    ("X1", "a case line carrying a REFUSED W2 `@file:` subject",
     b'pattern abc\nname t1\nm @file:"subj.bin" 0 3\n', None),
]


def main():
    binary = os.environ.get("PCREC_BIN") or default_bin()
    if not os.path.exists(binary):
        print("no pcrec binary at %s (set $PCREC_BIN)" % binary, file=sys.stderr)
        return 1
    # pcrec has no --version flag. The PIN is carried by the build
    # directory's own name (`build/pcrec-<pin>/`), which is what
    # testees/pcrec/adapter.py's pin_binary() constructs -- so the name is
    # the provenance, not a claim about whatever that clone's HEAD is now.
    pin = os.path.basename(os.path.dirname(os.path.dirname(binary)))
    bench = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"],
                           capture_output=True, text=True).stdout.strip()
    print("# pcrec --list-source probes -- the .rxt source grammar, PARSE ONLY")
    print("# binary:  %s" % binary)
    print("# pin:     %s (abi 23)" % pin)
    # The bench commit is PROVENANCE and is the one field that legitimately
    # moves between a re-run and the committed archive; everything else is a
    # function of the binary and the fixtures.
    print("# bench:   %s  (the one field a re-run may differ on)" % (bench or "unknown"))
    print("# script:  docs/dev/measurements/probe_rxt_format.py")
    print("# for:     docs/design/rxt_needs_v1.md 1.9 ([B42], lane b42rxtneeds)")
    print("# box:     NOT GATED and it does not matter -- no compile, no")
    print("#          artifact, no driver, no timing anywhere in this file.")
    print()
    # A FIXED directory name, not mkdtemp's random one: pcrec's diagnostics
    # quote the file path, so a random component would put noise in the
    # archive and make a re-run diff against it for no reason. Emptied and
    # recreated on every run; honours $TMPDIR (BD3: never /tmp root for
    # anything large -- these fixtures are at most a few hundred bytes).
    tmp = os.path.join(tempfile.gettempdir(), "rxtprobe")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp)
    for pid, desc, body, want in PROBES:
        path = os.path.join(tmp, pid + ".rxt")
        with open(path, "wb") as f:
            f.write(body)
        r = subprocess.run([binary, "--list-source", path], capture_output=True)
        rows = [l for l in r.stdout.splitlines() if not l.startswith(b"#")]
        print("=== %s: %s" % (pid, desc))
        print("    fixture: %r" % body)
        print("    exit:    %d" % r.returncode)
        for l in rows:
            print("    row:     %r" % l)
        if r.stderr:
            first = r.stderr.decode("utf-8", "replace").strip().splitlines()[0]
            print("    stderr:  %s" % first[:200])
        if want is not None:
            got = None
            for l in rows:
                if l.startswith(b"pattern\t"):
                    got = decode(l.split(b"\t")[4])
            print("    want:    %r" % want)
            print("    got:     %r" % got)
            print("    EXACT:   %s" % (got == want))
        print()
    print("# fixtures written under %s (fixed name, emptied each run)" % tmp)
    return 0


if __name__ == "__main__":
    sys.exit(main())
