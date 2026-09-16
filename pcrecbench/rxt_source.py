"""rxt_source.py -- THE .rxt PATTERN-SOURCE LOADER ([B42] lane b42load, L4).

Gives a `bench/<name>/` sub-bench a real loading path for a pattern source
written directly in pcrec's own `.rxt` format (docs/spec/rxt_format.md at
pin cd371441, abi 25 -- delivered per inbox I-68/I-69, W23 first-delivery
scope), so a set built ON `.rxt` (Frank's Q3 ruling,
docs/design/capability_set_v1.md 9; docs/design/rxt_needs_v1.md) does not
need the derived-`.rx`-per-pattern compatibility shim `bench/capability`
was built with while this loader did not exist yet.

THE ONE RULE THIS MODULE EXISTS TO KEEP: no second `.rxt` parser
(rxt_needs_v1.md 2.12's N-52 ask; check D2 of the restart acceptance
checklist, docs/design/rxt_needs_v1.md 3). Every fact this module produces
is read from `pcrec --list-source`'s own TSV dump -- pcrec's reference
implementation of the format, "THE SEAM" (rxt_format.md:418-423) -- and
decoded with the SAME escape vocabulary `tools/export_rxt.py`'s
`decode_rxt_escape` already decodes (imported, never reimplemented). This
module contains no `.rxt` keyword, no grammar rule, and no format-specific
tokenizing beyond splitting the DUMP's own TSV rows and its `#section` /
`#kind` / `#line` header lines -- a table format, not the source format.

ENGINE NEUTRALITY (R-BENCH-4) holds for the SET's own content: the pinned
pcrec binary used HERE is TOOLING, exactly like the libpcre2 oracle
`pcrecbench/oracle_pcre2.py` binds against to derive expectations -- it
reads a file format pcrec happens to own the only implementation of, and
it never becomes part of what any engine (pcrec included) is MEASURED
against. The binary is resolved through the SAME path
`tools/export_rxt.py --verify`'s default already uses
(`pcrecbench.adapters.discover()["pcrec"].pin_binary(build=False)`,
testees/pcrec/pin.sh's own resolution) -- never a second rule, and never a
build: a missing pin is a refusal BY NAME (`RxtSourceError`), never a
silent fallback to a `.rx` shim.

KNOWN GAP (found by this lane, 2026-09-16, reported to the manager before
this module was written): at pin cd371441, `--list-source` silently drops
the `#section provenance` and `#section variants` rows for every pattern
block EXCEPT THE LAST ONE IN THE FILE, when multiple blocks each carry
their own single, valid `provenance`/`variant` sub-block (no diagnostic,
exit 0; the flat per-line `m`/`n`/`mc` case rows are NOT affected).
Reproduced on a synthetic 3-pattern fixture and on the real
`bench/capability` corpus (64 patterns, 1 provenance row survives). This
module does not work around it -- doing so would mean inventing data
`--list-source` never emitted, which is exactly the second-parser hazard
this module exists to avoid. It reads the dump FAITHFULLY: a pattern
block's provenance is whatever `#section provenance` says it is, `None`
when the dump does not carry a row for that `block_line`. A set that
wants per-pattern provenance back needs the upstream fix (outbox item
pending); this loader's own block<->sidecar agreement gate (below) is
about PATTERN blocks, not provenance rows, precisely because the dump
cannot promise the latter today.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


class RxtSourceError(Exception):
    pass


# THE ESCAPE DECODER. Deliberately NOT `tools/export_rxt.py`'s
# `decode_rxt_escape` -- same four-escape table (\t \n \r \\, plus a
# pattern-esc block's re-emitted \xNN), but that function's fallback
# branch (`c.encode("utf-8")`, no `errors=`) silently CORRUPTS a byte
# that began life as a raw, unescaped non-ASCII byte in the dump -- a
# case export_rxt.py's own corpus census has never exercised (185 ids,
# "NONE contains a non-ASCII byte") and this lane's does immediately
# (bench/capability's `binary-nonutf8` family, by design). MEASURED
# (this lane, printf 'pattern caf\xe9...'): a plain `pattern` block's
# column 5 is documented as "the line's bytes verbatim"
# (rxt_format.md's [DD-13b.W23.4] note) -- pcrec escapes ONLY the four
# TSV-framing-unsafe bytes (`\t \n \r \\`) and passes every other byte,
# high ones included, straight through RAW. `subprocess.run(...,
# text=True)` therefore crashes with `UnicodeDecodeError` the moment the
# corpus carries one; this module reads stdout as BYTES and decodes it
# with `errors="surrogateescape"` (the standard, lossless round-trip for
# exactly this shape -- every byte that is not valid UTF-8 becomes one
# reversible surrogate codepoint), and `_decode_dump_field` re-encodes
# with the SAME error mode on its way back to real bytes. Not a pcrec
# defect -- the dump is doing exactly what its own doc sentence says --
# but a real plumbing gap this lane is reporting for `export_rxt.py`
# too (see the lane report; `check_rxt_export`'s round-trip has simply
# never been asked to carry a non-ASCII byte).
_ESCAPE_DECODE_2 = {"\\": 0x5C, "t": 0x09, "n": 0x0A, "r": 0x0D}
_HEXDIGITS = set("0123456789abcdefABCDEF")


def _decode_dump_field(s):
    """Byte-exact inverse of `--list-source`'s own escaping on a
    `value`/`pattern`/`pcrec` column: the four TSV-framing escapes plus
    a `pattern-esc` block's `\\xNN` spelling; every other character
    (including a surrogateescape-decoded raw byte) is re-encoded
    losslessly. `s` is a `str` produced by decoding the dump with
    `errors="surrogateescape"` -- see the module note above."""
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
        out.extend(c.encode("utf-8", errors="surrogateescape"))
        i += 1
    return bytes(out)


# Columns 4 (`value`), 5 (`pattern`) and 15 (`pcrec`) are the dump's own
# escaped columns (rxt_format.md:425-442, the [DD-13b.W23.4] note); every
# other column is plain text as written. Named here so a caller need not
# know the column POSITIONS, only which fields need decoding.
_ESCAPED_MAIN_COLUMNS = ("value", "pattern", "pcrec")

# capability_set_v1.md 9's restart procedure / rxt_needs_v1.md group F
# (F2/F3): a pattern-SOURCE file -- what this loader reads -- declares no
# build directive, ever. `ext` blocks (aux section rows) are NOT
# directives (I-67's ruling) and never reach this set at all: they live
# entirely in `#section aux`, never in the main table this gate scans.
_BUILD_DIRECTIVE_KINDS = frozenset({"target", "config"})

_PATTERN_KINDS = frozenset({"pattern", "pattern-esc"})


# --------------------------------------------------------- binary resolution

def resolve_pcrec_bin():
    """-> the pinned pcrec binary's path, via the adapter's OWN resolution
    (testees/pcrec/pin.sh, the same rule `export_rxt.py --verify`'s default
    already uses) -- never a second lookup rule. Never builds. A pin that
    is not built yet is a refusal BY NAME, not a silent shim fallback."""
    from pcrecbench import adapters as _ad
    try:
        adapter = _ad.discover()["pcrec"]
    except Exception as e:                             # noqa: BLE001
        raise RxtSourceError(
            "cannot discover the pcrec adapter (testees/pcrec/adapter.py): "
            "%s" % e)
    binary = adapter.pin_binary(build=False)
    if not binary or not os.path.exists(binary):
        raise RxtSourceError(
            "the pinned pcrec binary is not built (%r) -- an `.rxt` "
            "pattern source is loaded through `pcrec --list-source`, "
            "pcrec-bench's only sanctioned reader of this format "
            "(rxt_needs_v1.md 2.12's N-52 ask); build the pin first "
            "(testees/pcrec/pin.sh %s)" % (binary, adapter.pin()))
    return binary


def run_list_source(rxt_path, pcrec_bin=None, timeout=30):
    """Run `pcrec --list-source <rxt_path>` and return its stdout text.
    Never swallows a parse refusal -- a non-zero exit is an
    `RxtSourceError` naming the code and stderr."""
    if not os.path.exists(rxt_path):
        raise RxtSourceError(".rxt source file not found: %s" % rxt_path)
    binary = pcrec_bin or resolve_pcrec_bin()
    try:
        proc = subprocess.run([binary, "--list-source", rxt_path],
                              capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise RxtSourceError(
            "pcrec --list-source timed out after %ss on %s" % (timeout, rxt_path))
    except OSError as e:
        # A caller-provided `pcrec_bin` that does not exist or is not
        # executable (the ordinary path, `resolve_pcrec_bin`, already
        # checked existence before returning) -- refused BY NAME, never
        # a raw OSError leaking past this module's own error type.
        raise RxtSourceError(
            "cannot run pcrec --list-source with binary %r: %s" % (binary, e))
    if proc.returncode != 0:
        raise RxtSourceError(
            "pcrec --list-source %s failed (rc=%d): %s"
            % (rxt_path, proc.returncode,
               proc.stderr.decode("utf-8", errors="replace").strip()))
    # BYTES, decoded with surrogateescape -- see the module note above
    # `_decode_dump_field`: `--list-source`'s stdout is not guaranteed
    # valid UTF-8 (a plain `pattern` block's raw high bytes pass through
    # unescaped), and a strict UTF-8 decode crashes on exactly the
    # corpus this loader exists to read.
    return proc.stdout.decode("utf-8", errors="surrogateescape")


# --------------------------------------------------------------- TSV parsing

def parse_list_source(text):
    """Parse `--list-source`'s dump: the main table (header line starting
    `#kind`) plus zero or more `#section <name>` blocks, each with its own
    header line (`#line\\t...`). Returns `(main_cols, main_rows, sections)`:
    `main_rows` a list of `{column: value}` dicts in file order;
    `sections` a dict `{section_name: (cols, rows)}`.

    Column-name driven, not position driven -- a column the format adds
    later is simply present in the dict; nothing here hard-codes a column
    INDEX, only column NAMES this module actually reads (rxt_needs_v1.md
    2.12's own D2/D3 asks: the reader must survive the dump growing)."""
    main_cols = None
    main_rows = []
    sections = {}
    cur_name = None
    cur_cols = None
    cur_rows = None

    def _flush():
        if cur_name is not None:
            sections[cur_name] = (cur_cols, cur_rows)

    for raw_line in text.split("\n"):
        line = raw_line
        if not line:
            continue
        if line.startswith("#section "):
            _flush()
            cur_name = line[len("#section "):].strip()
            cur_cols = None
            cur_rows = []
            continue
        if line.startswith("#kind\t") or line == "#kind":
            main_cols = line[1:].split("\t")
            continue
        if line.startswith("#line\t") or line == "#line":
            if cur_name is None:
                raise RxtSourceError(
                    "--list-source: a #line header appeared outside any "
                    "#section block")
            cur_cols = line[1:].split("\t")
            continue
        if line.startswith("#"):
            continue  # prose / doc comment line -- not data
        cols = line.split("\t")
        if cur_name is None:
            if main_cols is None:
                raise RxtSourceError(
                    "--list-source: a data row appeared before the #kind "
                    "header -- malformed dump")
            if len(cols) != len(main_cols):
                raise RxtSourceError(
                    "--list-source: a main-table row has %d field(s), the "
                    "#kind header declares %d: %r"
                    % (len(cols), len(main_cols), raw_line))
            main_rows.append(dict(zip(main_cols, cols)))
        else:
            if cur_cols is None:
                raise RxtSourceError(
                    "--list-source: a #section %s row appeared before its "
                    "#line header" % cur_name)
            if len(cols) != len(cur_cols):
                raise RxtSourceError(
                    "--list-source: a #section %s row has %d field(s), its "
                    "#line header declares %d: %r"
                    % (cur_name, len(cols), len(cur_cols), raw_line))
            cur_rows.append(dict(zip(cur_cols, cols)))
    _flush()
    return main_cols, main_rows, sections


def _decode_main_row(row):
    """Decode the escaped columns of one main-table row IN PLACE-equivalent
    (returns a new dict) -- `value`/`pattern`/`pcrec`, whichever the row
    actually carries; a column absent from this dump's header is simply
    not in `row` and is skipped."""
    out = dict(row)
    for col in _ESCAPED_MAIN_COLUMNS:
        if col in out and out[col]:
            out[col] = _decode_dump_field(out[col])
    return out


# ------------------------------------------------------------------ tags

def parse_tag_value(raw):
    """Decode one row's `tags` column: a comma-joined list of bare labels
    and `key=value` pairs (MEASURED, acceptance check A5: `tag` lines
    ACCUMULATE and mix both forms freely, `format_design.md:1846`'s own
    ruling). -> `{"_labels": [...], "<key>": ["<v1>", "<v2>", ...], ...}` --
    a repeated key accumulates a list, matching the format's own rule."""
    labels = []
    kv = {}
    if raw:
        for item in raw.split(","):
            item = item.strip()
            if not item:
                continue
            if "=" in item:
                k, _, v = item.partition("=")
                kv.setdefault(k.strip(), []).append(v.strip())
            else:
                labels.append(item)
    kv["_labels"] = labels
    return kv


# ------------------------------------------------------------------ gates

def check_no_build_directives(main_rows, source_path):
    """capability_set_v1.md 9's restart procedure / rxt_needs_v1.md group F
    (F2/F3): a PATTERN-SOURCE `.rxt` file declares no `target` and no
    `config` row, ever -- refused BY NAME naming every offending line. An
    `ext` block's own contents never reach the MAIN TABLE this scans (they
    live only in `#section aux`), which is the built-in CONTROL: a set
    that uses `ext bench` for a testee roster (bench/capability's own
    shape) never trips this gate."""
    bad_rows = [r for r in main_rows if r.get("kind") in _BUILD_DIRECTIVE_KINDS]
    if bad_rows:
        lines = ", ".join(sorted({r.get("line", "?") for r in bad_rows}))
        kinds = ", ".join(sorted({r.get("kind", "?") for r in bad_rows}))
        raise RxtSourceError(
            "%s: a .rxt PATTERN SOURCE may declare no build directive "
            "(no `target`, no `config` row, ever) -- found %d such row(s) "
            "(kind(s): %s) at line(s): %s" % (source_path, len(bad_rows), kinds, lines))


def check_block_sidecar_agreement(main_rows, patterns, source_path):
    """DESIGN CONSTRAINT (a): every pattern/pattern-esc BLOCK in the .rxt
    main table appears EXACTLY ONCE in what this loader hands the harness
    (`patterns`), ids matched by the derivation rule (a block's `name`
    column IS the bench `pattern_id`, unchanged, checked separately against
    the record schema's slug rule by `subbench.check_id`). A mismatch --
    the loader dropped a block, duplicated one, or renamed one -- is
    refused BY NAME, naming what is missing, extra, or duplicated, rather
    than silently reconciled or truncated."""
    block_names = [r["name"] for r in main_rows if r.get("kind") in _PATTERN_KINDS]
    got_names = [p["name"] for p in patterns]
    dupes = sorted({n for n in block_names if block_names.count(n) > 1})
    if sorted(block_names) != sorted(got_names) or dupes:
        missing = sorted(set(block_names) - set(got_names))
        extra = sorted(set(got_names) - set(block_names))
        raise RxtSourceError(
            "%s: block<->loader agreement FAILED -- %d pattern block(s) in "
            "the .rxt main table, %d pattern(s) handed to the harness "
            "(missing=%r extra=%r duplicate block name(s)=%r)"
            % (source_path, len(block_names), len(got_names), missing, extra, dupes))


# --------------------------------------------------------------- assembly

def build_pattern_dicts(main_rows):
    """-> a list of dicts, one per `pattern`/`pattern-esc` main-table row,
    in FILE ORDER: `name`, `block_line`, `text` (decoded raw bytes),
    `esc` (bool: which spelling wrote it), `tags` (parse_tag_value's
    dict), `oracle` (per-block override, or None -- the file-level
    `oracle` row is a separate, head-scope fact, see `parse_head`)."""
    out = []
    for row in main_rows:
        if row.get("kind") not in _PATTERN_KINDS:
            continue
        name = row.get("name")
        if not name:
            raise RxtSourceError(
                "a %s row at line %s has no name" % (row.get("kind"), row.get("line")))
        decoded = _decode_main_row(row)
        out.append({
            "name": name,
            "block_line": row.get("line"),
            "text": decoded.get("pattern") or b"",
            "esc": row.get("kind") == "pattern-esc",
            "tags": parse_tag_value(row.get("tags") or ""),
            "oracle": row.get("oracle") or None,
        })
    return out


def parse_head(main_rows):
    """-> the file-level (head-scope: `name` column empty) facts a set
    typically carries: `description` (decoded), `oracle`, and
    `vocabulary`/`tag` rows (`{key: [values...]}`, `tag`'s own value
    column parsed the same way as a per-block `tags` column)."""
    head = {"description": None, "oracle": None, "vocabulary": {}, "tag": {}}
    for row in main_rows:
        if row.get("name"):
            continue  # block-scoped, not head
        kind = row.get("kind")
        if kind == "description":
            decoded = _decode_main_row(row)
            head["description"] = decoded.get("value")
        elif kind == "oracle":
            head["oracle"] = row.get("value") or None
        elif kind == "vocabulary":
            key = row.get("value")  # the vocabulary's own column layout
            # `vocabulary <key> <space-separated values>`: --list-source
            # puts the DECLARED key in `name` (unlike a pattern row, a
            # head row's `name` column is used for this), the value list
            # in `value`.
            vkey = row.get("name")
            vval = (row.get("value") or "").split()
            if vkey:
                head["vocabulary"][vkey] = vval
        elif kind == "tag":
            head["tag"] = parse_tag_value(row.get("value") or "")
    return head


def _index_single(section):
    """`(cols, rows)` -> `{block_line: row}` for a section where each
    pattern block carries AT MOST one row (provenance, by design: C7
    refuses a second one in the same block)."""
    if section is None:
        return {}
    _cols, rows = section
    out = {}
    for r in rows:
        out[r.get("block_line")] = r
    return out


def _index_multi(section):
    """`(cols, rows)` -> `{block_line: [row, ...]}` for a section where a
    pattern block may carry several rows (variants, cases)."""
    if section is None:
        return {}
    _cols, rows = section
    out = {}
    for r in rows:
        out.setdefault(r.get("block_line"), []).append(r)
    return out


class RxtSource:
    """The loaded `.rxt` file: `patterns` (list of dicts, `build_pattern_
    dicts`'s shape, in file order), `provenance`/`variants`/`cases` indexed
    by `block_line` (a pattern's own `line` column in the main table),
    `aux_rows` (the `#section aux` rows verbatim -- interpreted by nothing
    here, same posture as pcrec's own dump: a future L5 lane reads the
    `ext bench` roster/capabilities tree out of this), and `head` (file-
    level description/oracle/vocabulary/tag facts)."""

    __slots__ = ("path", "patterns", "provenance", "variants", "cases",
                 "aux_rows", "head", "main_rows")

    def __init__(self, path, patterns, provenance, variants, cases,
                 aux_rows, head, main_rows):
        self.path = path
        self.patterns = patterns
        self.provenance = provenance
        self.variants = variants
        self.cases = cases
        self.aux_rows = aux_rows
        self.head = head
        self.main_rows = main_rows

    def provenance_for(self, block_line):
        return self.provenance.get(block_line)


def load_rxt_source(path, pcrec_bin=None):
    """THE ENTRY POINT: load and gate one `.rxt` pattern-source file.
    `pcrecbench.subbench.Subbench` calls this when a sidecar declares
    `rxt_source = <relative path>`. Raises `RxtSourceError` naming exactly
    what is wrong on any gate failure -- no partial result is ever
    returned."""
    text = run_list_source(path, pcrec_bin=pcrec_bin)
    main_cols, main_rows, sections = parse_list_source(text)
    if main_cols is None:
        raise RxtSourceError(
            "%s: --list-source produced no #kind header -- empty or "
            "malformed dump" % path)
    check_no_build_directives(main_rows, path)
    patterns = build_pattern_dicts(main_rows)
    if not patterns:
        raise RxtSourceError("%s: no pattern block found" % path)
    check_block_sidecar_agreement(main_rows, patterns, path)
    provenance = _index_single(sections.get("provenance"))
    variants = _index_multi(sections.get("variants"))
    cases = _index_multi(sections.get("cases"))
    aux_cols, aux_rows = sections.get("aux", (None, []))
    head = parse_head(main_rows)
    return RxtSource(path=path, patterns=patterns, provenance=provenance,
                     variants=variants, cases=cases, aux_rows=aux_rows,
                     head=head, main_rows=main_rows)
