#!/usr/bin/env python3
r"""tools/export_rxt.py -- THE .rxt SET EXPORTER ([B38], pcrec [DD-13b.W1.3]).

A ONE-WAY EXPORT: `tools/export_rxt.py <bench-dir> [-o out.rxt]` writes a
`.rxt` SOURCE file (pcrec's own import format, docs/spec/rxt_format.md) from
one bench sub-bench's sidecar, so pcrec's own harnesses can pull our
patterns into their battery as an import source (`pcrec --source FILE`).

THIS IS NOT A TEST-FILE EXPORT: no `m`/`n`/`ms`/`ns` case lines, no oracle
expectations -- a pure SOURCE file, one `target = <name>` head row and one
`pattern <text>` / `name <id>` block per pattern, nothing else. The sidecar
stays the source of truth (R-BENCH-4, engine-neutral); the `.rxt` is a
derived view for pcrec's own consumption only -- never checked for
correctness against anything but ROUND-TRIPPING the sidecar's own bytes
(`verify_roundtrip`, below).

THE RULES ARE inbox I-43's (docs/dev/inbox_from_pcrec.md, 2026-09-04,
FINAL), re-verified here at the CURRENT corpus (185 patterns across five
sets, 2026-09-07) rather than trusted from I-43's own 90-id census:

1. A block `name` is `[A-Za-z_][A-Za-z0-9_.-]*` (`NAME_RE`). Every one of
   the 185 current pattern ids passes (re-verified; none needs a map).
2. `target = <name>` derives the C prefix by replacing `-`/`.` with `_`,
   one row per pattern, never a hand mapping (`derive_prefix`). We do not
   write the prefix ourselves -- pcrec derives it from the `target =` row.
3. Two names colliding on one prefix is a REFUSAL naming both
   (`ExportError` from `build_rxt`). I-43 found exactly one collision
   (`floor`) and it was CROSS-SET, so exporting PER SUB-BENCH (one `.rxt`
   per `bench/<name>/`, never merged) avoids it; re-verified at 185 ids,
   still true (see the module docstring's per-set collision note below,
   and b38rxt_report.md for the cross-set census).
4. `rx_info.name` (the pattern id) is written UNCHANGED via `name <id>`,
   `-` and all.
5. NO `config`/`flags`/`engine`/`budget`/`encoding` lines are ever written
   (D93: a source's composed config wins over a command-line flag -- an
   `engine` line in a set would pin pcrec's testee matrix from inside the
   set. HOW a pattern is built stays on the harness's command line).
6. THE PATTERN LINE IS WRITTEN VERBATIM, RAW BYTES, ALWAYS -- never
   escaped. This is not a shortcut that happens to work on today's
   all-ASCII, tab-free, single-line corpus: it is what
   `docs/spec/rxt_format.md` REQUIRES. Its own words, read directly: "the
   pattern text is rest-of-line verbatim from the byte after that space
   ... (no quoting, no escaping)". Confirmed empirically against the pin
   (d34c9131): a `pattern \d+\t$` line round-trips through `--list-source`
   as the *seven literal characters* `\`,`d`,`+`,`\`,`t`,`$` (escaped as
   `\\d+\\t$` in the DUMP, because `--list-source` escapes its OWN output
   for TSV framing) -- if we escaped a backslash on the way IN, pcrec
   would read a literal two-character `\\` where the pattern meant one
   backslash. A real embedded TAB byte round-trips as a real tab in the
   SOURCE file and only becomes `\t` in `--list-source`'s dump. The
   escape vocabulary (`\t \n \r \\ \xNN`) therefore belongs to the
   ROUND-TRIP CHECK's decoder (`decode_rxt_escape`), which undoes
   `--list-source`'s own TSV-safety escaping before comparing against
   `Subbench.pattern_bytes()` -- never to this exporter's writer.
   A pattern containing a literal NEWLINE byte has no representation in a
   single `pattern <text>` line at all (the format is line-oriented; a
   newline ends the line) and is refused BY NAME rather than silently
   mangled. Re-verified at 185 ids: NONE contains a newline, a CR, a tab,
   or a non-ASCII byte (`ESCAPE_WITNESSES` below is empty on the real
   corpus; the code path exists for the day one is added).
7. A hyphenated `name` is buildable as a `target` but not callable from a
   `pattern` via `(?&some-id)` (PCRE2's group-name grammar refuses `-`).
   No pattern in any set here calls another by id, so this costs nothing
   today -- noted for whoever adds the first one.

Usage:

    python3 tools/export_rxt.py email                    # bench/email
    python3 tools/export_rxt.py bench/altwide -o /tmp/x.rxt
    python3 tools/export_rxt.py syntax --verify           # + round-trip
"""

import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from pcrecbench import subbench as _sb  # noqa: E402

# Rule 1's grammar, verbatim.
NAME_RE = re.compile(r'^[A-Za-z_][A-Za-z0-9_.-]*$')

# The escape vocabulary `--list-source` applies to its OWN dump (columns
# 4, 5, 15; docs/spec/rxt_format.md, put_escaped() in
# src/parse/rxt_source.c) -- used only by the ROUND-TRIP CHECK to decode
# that dump back to raw bytes, never by the exporter's writer (rule 6).
_ESCAPE_DECODE_2 = {"\\": 0x5C, "t": 0x09, "n": 0x0A, "r": 0x0D}
_HEXDIGITS = set("0123456789abcdefABCDEF")


class ExportError(Exception):
    pass


def derive_prefix(name):
    """Rule 2: `-`/`.` -> `_`, every other byte copied. Mirrors pcrec's own
    derivation (docs/spec/rxt_format.md "Building from a source file") --
    never a second, hand-maintained mapping."""
    return name.replace("-", "_").replace(".", "_")


def build_rxt(sb):
    """-> (bytes, list[str]) the `.rxt` SOURCE file content for one
    Subbench, and the list of pattern ids that needed something other than
    a plain verbatim write (empty on today's corpus; see rule 6). Sidecar
    order is preserved throughout (`sb.patterns`, i.e. the TOML array
    order == file order in `subbench.toml`) -- both for the head's
    `target =` rows and for the pattern blocks, matching the shape
    pcrec's own composed.rxtin example uses."""
    names = [p.name for p in sb.patterns]

    for n in names:
        if not NAME_RE.match(n):
            raise ExportError(
                "%s: pattern id %r violates the .rxt block-name grammar "
                "%s (inbox I-43 rule 1) -- needs a name map before this "
                "set can export" % (sb.id, n, NAME_RE.pattern))

    prefix_of = {}
    for n in names:
        pref = derive_prefix(n)
        if pref in prefix_of and prefix_of[pref] != n:
            raise ExportError(
                "%s: pattern ids %r and %r both derive the target prefix "
                "%r (inbox I-43 rule 3) -- a per-set export was chosen "
                "specifically because the corpus's one known collision "
                "(`floor`) is CROSS-SET; a WITHIN-SET collision like this "
                "one needs a disambiguator on one of the two ids"
                % (sb.id, prefix_of[pref], n, pref))
        prefix_of[pref] = n

    witnesses = []
    dirname = os.path.basename(sb.root)
    default_out_rel = os.path.relpath(
        os.path.join(sb.root, "export", "%s.rxt" % dirname), ROOT)
    header_text = [
        "# %s.rxt -- GENERATED by tools/export_rxt.py, DO NOT EDIT BY HAND." % dirname,
        "#",
        "# Source: bench/%s (sidecar id %r, version %s)." % (dirname, sb.id, sb.version),
        "# Regenerate: python3 tools/export_rxt.py %s -o %s" % (dirname, default_out_rel),
        "#",
        "# A one-way EXPORT (pcrec [DD-13b.W1.3]) for pcrec's own harnesses",
        "# to pull this set's patterns into their battery via `--source`.",
        "# PURE SOURCE: no m/n/ms/ns cases, no config/flags/engine/budget/",
        "# encoding (inbox I-43 rule 5 -- D93: a source's composed config",
        "# wins over a command-line flag, so declaring any of those here",
        "# would pin pcrec's testee matrix from inside the set). The",
        "# sidecar (bench/%s/subbench.toml) stays the source of truth" % dirname,
        "# (R-BENCH-4); this file is a derived, regeneratable view.",
        "",
    ]

    lines = [line.encode("ascii") for line in header_text]
    for n in names:
        lines.append(("target = %s" % n).encode("ascii"))
    lines.append(b"")

    for n in names:
        raw = sb.pattern_bytes(n)
        if b"\n" in raw or b"\r" in raw:
            raise ExportError(
                "%s: pattern %r contains a newline/CR byte -- the .rxt "
                "`pattern` line is rest-of-line verbatim with NO "
                "escaping (docs/spec/rxt_format.md) and has no way to "
                "represent one; this pattern cannot be exported as "
                "written" % (sb.id, n))
        if b"\t" in raw or any(b < 0x20 or b == 0x7F for b in raw) or not raw.isascii():
            # No special handling needed on the WRITE side (rule 6): the
            # byte is legal rest-of-line content and round-trips through
            # `--list-source`'s own escaping unchanged. Recorded only so
            # the report can say whether this path was ever exercised.
            witnesses.append(n)
        lines.append(b"pattern " + raw)
        lines.append(("name %s" % n).encode("ascii"))
        lines.append(b"")

    return b"\n".join(lines) + b"\n", witnesses


def default_output(sb):
    dirname = os.path.basename(sb.root)
    return os.path.join(sb.root, "export", "%s.rxt" % dirname)


def _load(bench_arg):
    """Resolve `bench_arg` as a `bench/<name>` directory name (via
    `pcrecbench.subbench.find`) or a path, exactly like the harness CLI's
    `--subbench`."""
    if os.sep in bench_arg or os.path.isdir(bench_arg):
        return _sb.load(bench_arg)
    return _sb.find(bench_arg)


# ------------------------------------------------------------ round-trip

def decode_rxt_escape(s):
    """Inverse of pcrec's `put_escaped` (src/parse/rxt_source.c): undoes
    `--list-source`'s OWN TSV-safety escaping on columns 4/5/15 (`\\t \\n
    \\r \\\\ \\xNN`) to recover the raw bytes the dump describes. This is
    the ONLY place this vocabulary is decoded in this tool -- the exporter
    never encodes it (rule 6's whole point)."""
    out = bytearray()
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == "\\" and i + 1 < n:
            c2 = s[i + 1]
            if c2 in _ESCAPE_DECODE_2:
                out.append(_ESCAPE_DECODE_2[c2])
                i += 2
                continue
            if c2 == "x" and i + 3 < n and s[i + 2] in _HEXDIGITS and s[i + 3] in _HEXDIGITS:
                out.append(int(s[i + 2:i + 4], 16))
                i += 4
                continue
        out.extend(c.encode("utf-8"))
        i += 1
    return bytes(out)


def parse_list_source_pattern_rows(tsv_text):
    """-> {name: pattern_bytes} for every `pattern`-kind row in
    `--list-source`'s TSV (columns: kind, line, name, value, pattern, ...;
    docs/spec/rxt_format.md's 16-column table). Comment lines (`#...`) and
    blanks are skipped."""
    out = {}
    for line in tsv_text.splitlines():
        if not line or line.startswith("#"):
            continue
        cols = line.split("\t")
        if cols[0] != "pattern":
            continue
        name = cols[2]
        pattern_col = cols[4] if len(cols) > 4 else ""
        out[name] = decode_rxt_escape(pattern_col)
    return out


def verify_roundtrip(sb, rxt_bytes, pcrec_bin, timeout=60):
    """Runs `pcrec --list-source` on `rxt_bytes` (a freshly built export,
    never the committed file -- the gate re-derives) and checks that,
    for EVERY pattern in the sidecar, `--list-source`'s own `name` +
    (decoded) `pattern` columns match `Pattern.name` + `pattern_bytes()`
    exactly. Raises ExportError naming the first mismatch; returns the
    row count on success."""
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".rxt", delete=False) as f:
        f.write(rxt_bytes)
        path = f.name
    try:
        proc = subprocess.run([pcrec_bin, "--list-source", path],
                              capture_output=True, text=True, timeout=timeout)
    finally:
        os.unlink(path)
    if proc.returncode != 0:
        raise ExportError("%s: pcrec --list-source failed (rc=%d): %s"
                          % (sb.id, proc.returncode, proc.stderr[-500:]))
    rows = parse_list_source_pattern_rows(proc.stdout)
    names = [p.name for p in sb.patterns]
    missing = [n for n in names if n not in rows]
    if missing:
        raise ExportError("%s: --list-source is missing pattern row(s) %r"
                          % (sb.id, missing))
    for n in names:
        want = sb.pattern_bytes(n)
        got = rows[n]
        if got != want:
            raise ExportError(
                "%s: pattern %r round-trip MISMATCH: sidecar=%r "
                "--list-source(decoded)=%r" % (sb.id, n, want, got))
    if len(rows) != len(names):
        raise ExportError(
            "%s: --list-source reports %d pattern row(s), sidecar declares "
            "%d -- an extra row the sidecar does not name"
            % (sb.id, len(rows), len(names)))
    return len(names)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("subbench", help="bench/<name> directory name or path")
    ap.add_argument("-o", "--output", help="output .rxt path "
                    "(default: bench/<name>/export/<name>.rxt)")
    ap.add_argument("--verify", metavar="PCREC_BIN", nargs="?", const="",
                    help="round-trip the export against `PCREC_BIN "
                    "--list-source` (default: the pinned binary, "
                    "testees/pcrec/configs.toml, never built if missing)")
    args = ap.parse_args(argv)

    try:
        sb = _load(args.subbench)
        rxt_bytes, witnesses = build_rxt(sb)
    except _sb.SubbenchError as e:
        print("export_rxt: %s" % e, file=sys.stderr)
        return 1
    except ExportError as e:
        print("export_rxt: %s" % e, file=sys.stderr)
        return 1

    out_path = args.output or default_output(sb)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(rxt_bytes)
    print("%s: %d pattern(s) -> %s%s"
          % (sb.id, len(sb.patterns), out_path,
             " (%d needed no special handling but were flagged: %s)"
             % (len(witnesses), ", ".join(witnesses)) if witnesses else ""))

    if args.verify is not None:
        pcrec_bin = args.verify
        if not pcrec_bin:
            from pcrecbench import adapters as _ad
            try:
                pcrec_bin = _ad.discover()["pcrec"].pin_binary(build=False)
            except Exception as e:                # noqa: BLE001
                print("export_rxt: cannot resolve the pinned pcrec: %s" % e,
                      file=sys.stderr)
                return 1
            if not os.path.exists(pcrec_bin):
                print("export_rxt: pinned pcrec is not built yet: %s"
                      % pcrec_bin, file=sys.stderr)
                return 1
        try:
            n = verify_roundtrip(sb, rxt_bytes, pcrec_bin)
        except ExportError as e:
            print("export_rxt: ROUND-TRIP FAILED: %s" % e, file=sys.stderr)
            return 1
        print("%s: round-trip OK (%d pattern row(s) match --list-source)"
              % (sb.id, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
