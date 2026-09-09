"""The INTERPRETER (part 1) -- `pcrecbench interpret`, [B13].

A deterministic fact-finder over a committed report TSV and
`store/index.tsv`. Specified by `docs/design/interpreter_v1.md` (v1.2);
the rules themselves live in `catalogue/rules.toml`, which is the
contract this module is checked against by `make check-interpret`.

Three properties this file exists to keep (interpreter_v1.md §7):

  * every sentence it can emit is a `str.format` of one rule's declared
    `template`, one rule's declared `no_fire` sentence, a validated
    `links` line, a heading, or the stamp -- there is no free-text
    channel;
  * every rule function is handed a VIEW that raises `UndeclaredColumn`
    on any column outside that rule's own declared `inputs`;
  * no rule introduces a threshold of its own: each reads a token or a
    number `report.py`/`reduce.py` already computed and printed, or
    compares two measured quantities from the same report, and cites
    the source in the catalogue's `threshold_src`.

Determinism: every `open()` passes `encoding="utf-8"` explicitly
(interpreter_v1.md §12 -- `delta_verdict` carries U+00D7 and U+2192 and
`report.py`'s own `main()` sets `LC_ALL=C`), and every sort key is
built from strings compared bytewise.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import math
import os
import re
import sys
import tomllib
from collections import defaultdict

INTERPRET_VERSION = "v1"

# The report TSV's 18 data columns (report.py `render_tsv`'s own
# `header` list). Read from the source at load time by
# `report_columns_from_source()` and checked against this list by
# `make check-interpret` section 1.
REPORT_COLUMNS = [
    "section", "pattern", "subject_or_na", "regime_or_na", "form", "fact",
    "testee", "status", "tier", "rank_or_na", "metric", "value", "n",
    "pass_rate", "n_gave_up", "n_wrong", "gave_up_summary", "delta_verdict",
]

# `store/index.tsv`'s eight columns (its own line 1).
INDEX_COLUMNS = ["path", "subbench", "version", "testee_id", "machine_id",
                 "timestamp", "status", "rows"]

SECTIONS = ("record", "rank", "excluded", "not_ranked", "scratch",
            "did_not_compile", "compile", "compile_stamp")

# The known-key list for §2.1's NORMATIVE known-key header split. It is
# DERIVED from `report.py`'s own header block (see
# `header_keys_from_source`) rather than retyped; this constant is the
# frozen expectation `make check-interpret` compares the derived list
# against, so a reporter bump that adds a key fails the check instead of
# silently re-joining the new key into the previous key's value.
HEADER_KEYS = [
    "reporter", "filters", "source", "records", "excluded_invalid",
    "superseded", "newer_not_measured", "subbench_versions", "machines",
    "schema_versions", "grain", "single_subject_regimes",
    "include_unmeasured", "include_scratch", "all_records", "x13_rules",
    "mixed_x13", "include_provenance", "worst_other_core_busy",
    "floor_pattern",
]

DID_NOT_FIRE_TOKENS = ("no-matching-rows", "input-absent", "grain",
                       "reporter-version", "no-registered-signatures",
                       "retired")

RULE_FIELDS = ("id", "title", "class", "since", "grain", "aggregate",
               "inputs", "predicate", "threshold", "threshold_src", "slots",
               "arith", "template", "no_fire", "links", "example")

KEY_COLUMNS = ("pattern", "subject_or_na", "regime", "form", "testee",
               "record_id", "prediction_id")

FACTS_COLUMNS = ["rule_id", "fired", "firing_seq", "pattern", "subject_or_na",
                 "regime", "form", "testee", "record_id", "prediction_id",
                 "slot", "value"]


class InterpretError(Exception):
    """A malformed input, an unresolvable link, a catalogue/code
    mismatch, a pin absent from `[[pin_order]]`. Exit code 2."""


class UndeclaredColumn(InterpretError):
    """A rule function touched a column outside its declared `inputs`
    (interpreter_v1.md §3.2.2). A bug in the rule or its declaration."""


# ------------------------------------------------------------ utilities

def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def fmt_ns(v):
    """The ONE formatter for a nanosecond slot (§7.2: fixed precision, so
    two renders of one input cannot differ in a digit)."""
    return f"{v:,.1f}"


def fmt_ratio(v):
    """The ONE formatter for a ratio slot."""
    return f"{v:.2f}"


def fmt_num(v):
    """The ONE formatter for any other measured number."""
    if isinstance(v, int) or (isinstance(v, float) and float(v).is_integer()
                              and abs(v) < 1e15):
        return f"{int(v):,}"
    return f"{v:.6f}"


# ------------------------------------------------- the report TSV input

def header_keys_from_source(report_py=None):
    """The known-key list, DERIVED from `report.py`'s own header block.

    §2.1 rules the known-key split NORMATIVE and §8(1) requires the list
    not be retyped from the design note. The header keys are an
    f-string block inside `render_tsv` -- the one part of the input that
    cannot be read out of `render_tsv`'s `header` list -- so they are
    read from the source of that block, in emission order.
    """
    if report_py is None:
        report_py = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "report.py")
    src = _read(report_py)
    i = src.find('lines.append("# " + "; ".join(')
    if i < 0:
        raise InterpretError(f"{report_py}: no header block in render_tsv")
    j = src.find('header = [', i)
    if j < 0:
        raise InterpretError(f"{report_py}: header block does not terminate")
    block = src[i:j]
    keys = []
    for m in re.finditer(r'["\']([a-z0-9_]+): ', block):
        if m.group(1) not in keys:
            keys.append(m.group(1))
    if not keys:
        raise InterpretError(f"{report_py}: no header keys found")
    return keys


def report_columns_from_source(report_py=None):
    """The 18 data columns, read from `render_tsv`'s own `header` list."""
    if report_py is None:
        report_py = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "report.py")
    src = _read(report_py)
    i = src.find('lines.append("# " + "; ".join(')
    j = src.find('header = [', i)
    k = src.find(']', j)
    if i < 0 or j < 0 or k < 0:
        raise InterpretError(f"{report_py}: no render_tsv header list")
    return re.findall(r'"([a-z_]+)"', src[j:k])


def split_header(line, known_keys):
    """§2.1's NORMATIVE known-key split.

    `; ` is not a sufficient delimiter: `x13_rules`'s own value is built
    with `"; ".join(...)` and three committed reports carry a two-clause
    value, so a naive split shifts every later key by one. This splits
    only BEFORE a name already on the known-key list, which fails safe on
    an unrecognised VALUE shape.
    """
    text = line.lstrip("#").strip()
    cuts = []
    for key in known_keys:
        for m in re.finditer(r"(?:^|; )" + re.escape(key) + r": ", text):
            start = m.start() if m.start() == 0 else m.start() + 2
            cuts.append((start, key))
    cuts.sort()
    out = {}
    for n, (start, key) in enumerate(cuts):
        end = cuts[n + 1][0] - 2 if n + 1 < len(cuts) else len(text)
        out[key] = text[start + len(key) + 2:end]
    return out


class ReportTsv:
    """A parsed report TSV: the header comment and the 18-column rows."""

    def __init__(self, path, known_keys=None):
        self.path = path
        known_keys = known_keys or HEADER_KEYS
        text = _read(path)
        lines = text.split("\n")
        if not lines or not lines[0].startswith("#"):
            raise InterpretError(f"{path}: no header comment line")
        self.header = split_header(lines[0], known_keys)
        cols = lines[1].split("\t")
        if cols != REPORT_COLUMNS:
            raise InterpretError(f"{path}: unexpected column list {cols}")
        self.rows = []
        for ln in lines[2:]:
            if not ln:
                continue
            f = ln.split("\t")
            if len(f) != len(REPORT_COLUMNS):
                raise InterpretError(
                    f"{path}: row with {len(f)} fields, expected "
                    f"{len(REPORT_COLUMNS)}: {ln[:80]!r}")
            self.rows.append(dict(zip(REPORT_COLUMNS, f)))
        self.by_section = defaultdict(list)
        for r in self.rows:
            self.by_section[r["section"]].append(r)

    @property
    def grain(self):
        return self.header.get("grain", "set")


class IndexTsv:
    def __init__(self, path):
        self.path = path
        self.rows = []
        lines = _read(path).split("\n")
        if not lines:
            raise InterpretError(f"{path}: empty index")
        cols = lines[0].split("\t")
        if cols != INDEX_COLUMNS:
            raise InterpretError(f"{path}: unexpected index columns {cols}")
        for ln in lines[1:]:
            if not ln:
                continue
            f = ln.split("\t")
            if len(f) != len(INDEX_COLUMNS):
                raise InterpretError(f"{path}: malformed index row {ln[:80]!r}")
            self.rows.append(dict(zip(INDEX_COLUMNS, f)))


def record_id_of(index_row):
    """The join key (§2.2): a `record` row's `testee` column is the
    basename of the index row's `path` without `.jsonl`. The only join,
    and it is exact."""
    return os.path.basename(index_row["path"])[:-len(".jsonl")] \
        if index_row["path"].endswith(".jsonl") \
        else os.path.basename(index_row["path"])


# ------------------------------------------------------ the view contract

class Row(dict):
    """A report or index row that raises on an undeclared column."""

    def __init__(self, data, allowed, rule_id):
        super().__init__(data)
        self._allowed = allowed
        self._rule = rule_id

    def __getitem__(self, key):
        if key not in self._allowed:
            raise UndeclaredColumn(
                f"{self._rule}: column {key!r} is not in the rule's declared "
                f"inputs (declared: {sorted(self._allowed)})")
        return dict.__getitem__(self, key)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default


def parse_inputs(entries, rule_id):
    """§3.2.2's grammar.

        inputs entry := <file> ":" <section> [ "?" <col> "=" <val>
                                {"&" <col> "=" <val>} ]
                                [ "." <column> | "." "{" <column>{,<column>} "}" ]
        <file>       := "report" | "index"
        <section>    := a `section` value, or "header"

    An `index` entry carries no section (`index.{a,b,c}`).
    Returns (report_entries, header_columns, index_columns) where a
    report entry is (section, filters dict, columns set).
    """
    report_entries = []
    header_cols = set()
    index_cols = set()
    for raw in entries:
        if raw.startswith("index."):
            body = raw[len("index."):]
            index_cols |= _parse_column_list(body, rule_id, raw)
            continue
        if not raw.startswith("report:"):
            raise InterpretError(f"{rule_id}: inputs entry {raw!r} names no "
                                 f"known file")
        body = raw[len("report:"):]
        head, dot, cols = _split_on_column_dot(body)
        section = head
        filters = {}
        if "?" in head:
            section, q = head.split("?", 1)
            for clause in q.split("&"):
                if "=" not in clause:
                    raise InterpretError(
                        f"{rule_id}: inputs entry {raw!r} has a filter clause "
                        f"{clause!r} that is not <col>=<val>")
                c, v = clause.split("=", 1)
                if c not in REPORT_COLUMNS:
                    raise InterpretError(
                        f"{rule_id}: inputs entry {raw!r} filters on unknown "
                        f"column {c!r}")
                filters[c] = v
        if section == "header":
            if not dot:
                raise InterpretError(f"{rule_id}: header entry {raw!r} names "
                                     f"no key")
            header_cols |= _parse_column_list(cols, rule_id, raw, header=True)
            continue
        if section not in SECTIONS:
            raise InterpretError(f"{rule_id}: inputs entry {raw!r} names "
                                 f"unknown section {section!r}")
        columns = _parse_column_list(cols, rule_id, raw) if dot else set()
        report_entries.append((section, filters, columns | set(filters)))
    return report_entries, header_cols, index_cols


def _split_on_column_dot(body):
    """Split `rank?metric=median_ns.{a,b}` into head and column list."""
    depth = 0
    for i, ch in enumerate(body):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif ch == "." and depth == 0:
            return body[:i], True, body[i + 1:]
    return body, False, ""


def _parse_column_list(spec, rule_id, raw, header=False):
    spec = spec.strip()
    if spec.startswith("{") and spec.endswith("}"):
        names = [s.strip() for s in spec[1:-1].split(",")]
    else:
        names = [spec]
    out = set()
    for n in names:
        if not n:
            raise InterpretError(f"{rule_id}: empty column in {raw!r}")
        if header:
            if n not in HEADER_KEYS:
                raise InterpretError(
                    f"{rule_id}: {raw!r} names header key {n!r}, which the "
                    f"reporter does not emit")
        elif raw.startswith("index."):
            if n not in INDEX_COLUMNS:
                raise InterpretError(
                    f"{rule_id}: {raw!r} names index column {n!r}")
        elif n not in REPORT_COLUMNS:
            raise InterpretError(f"{rule_id}: {raw!r} names report column "
                                 f"{n!r}")
        out.add(n)
    return out


class RuleView:
    """The three-method view of §3.2.2, raising on any undeclared key."""

    def __init__(self, rule, report, index):
        self.rule_id = rule["id"]
        self._report = report
        self._index = index
        (self._entries, self._header_cols,
         self._index_cols) = parse_inputs(rule["inputs"], self.rule_id)

    # -- report rows -----------------------------------------------------
    def rows(self, section, **eq):
        entries = [e for e in self._entries if e[0] == section]
        if not entries:
            raise UndeclaredColumn(
                f"{self.rule_id}: section {section!r} is not in the rule's "
                f"declared inputs")
        compatible = []
        for _s, filters, columns in entries:
            if any(k in eq and eq[k] != v for k, v in filters.items()):
                continue
            compatible.append((filters, columns))
        if not compatible:
            raise UndeclaredColumn(
                f"{self.rule_id}: rows({section!r}, {eq!r}) matches no "
                f"declared inputs entry")
        for k in eq:
            if k not in REPORT_COLUMNS:
                raise UndeclaredColumn(f"{self.rule_id}: filter on unknown "
                                       f"column {k!r}")
            if not any(k in f for f, _c in compatible) and \
                    not any(k in c for _f, c in compatible):
                raise UndeclaredColumn(
                    f"{self.rule_id}: filter column {k!r} is not declared for "
                    f"section {section!r}")
        allowed = set()
        for _f, cols in compatible:
            allowed |= cols
        allowed.add("section")
        out = []
        for r in self._report.by_section.get(section, ()):
            if all(r[k] == v for k, v in eq.items()):
                out.append(Row(r, allowed, self.rule_id))
        return out

    # -- one header value ------------------------------------------------
    def header(self, key):
        if key not in self._header_cols:
            raise UndeclaredColumn(
                f"{self.rule_id}: header key {key!r} is not in the rule's "
                f"declared inputs")
        return self._report.header.get(key, "")

    # -- index rows ------------------------------------------------------
    def index_rows(self, **eq):
        if not self._index_cols:
            raise UndeclaredColumn(f"{self.rule_id}: this rule declares no "
                                   f"index inputs")
        if self._index is None:
            raise InterpretError(f"{self.rule_id}: no index supplied")
        for k in eq:
            if k not in self._index_cols:
                raise UndeclaredColumn(
                    f"{self.rule_id}: index filter column {k!r} is not "
                    f"declared")
        out = []
        for r in self._index.rows:
            if all(r[k] == v for k, v in eq.items()):
                out.append(Row(r, self._index_cols, self.rule_id))
        return out


# ------------------------------------------------- declared decompositions

_TS_SUFFIX = re.compile(r"@\d.*$")


def is_reference(testee_id):
    """report.py `_is_reference`, copied verbatim (§7.2's declared
    decomposition): strip a possible `@<timestamp>` suffix, then
    `startswith("libpcre2_") and "_interp-" in base`."""
    base = testee_id.split("@", 1)[0]
    return base.startswith("libpcre2_") and "_interp-" in base


def split_testee(testee_id):
    """record_schema.md §6.4's composition rule, split from the RIGHT
    (§4.4): `<engine>_<version_slug>_<config_slug>[_<config_extra>]`,
    `config_slug = <mode>-<caps>-<simd>` where simd is the last hyphen
    field, caps the one before it and mode is everything before that (so
    `vm-in` keeps its hyphen). Returns
    (engine, version_slug, mode, caps, simd, extra), `extra` `(none)`
    when absent, or None when the id does not decompose."""
    base = testee_id.split("@", 1)[0]
    parts = base.split("_")
    if len(parts) < 3:
        return None
    engine, version = parts[0], parts[1]
    rest = "_".join(parts[2:])
    if "_" in rest:
        config_slug, extra = rest.split("_", 1)
    else:
        config_slug, extra = rest, "(none)"
    fields = config_slug.rsplit("-", 2)
    if len(fields) != 3:
        return None
    mode, caps, simd = fields
    return engine, version, mode, caps, simd, extra


def config_of(testee_id):
    """`config` = the testee id with its version_slug decomposed OUT
    (§7.2, cross-review I-58 edit 4)."""
    parts = split_testee(testee_id)
    if not parts:
        return None
    engine, _version, mode, caps, simd, extra = parts
    slug = f"{mode}-{caps}-{simd}"
    return f"{slug}" if extra == "(none)" else f"{slug}_{extra}"


def clauses_of(delta_verdict):
    """`delta_verdict` is a `; `-separated LIST of independent clauses,
    not a token (§2.1). Every R-DELTA rule matches its anchor against
    each CLAUSE."""
    return [c for c in delta_verdict.split("; ") if c]


def candidates_from_source(source_value):
    """§7.2: the candidate count in `(N record(s) matching this query)`
    (KB-8's own rendering); the whole value when the shape is absent."""
    m = re.search(r"\((\d+) record\(s\) matching this query\)", source_value)
    return m.group(1) if m else source_value


# --------------------------------------------------------------- firings

class Firing:
    __slots__ = ("slots", "keys", "nums", "seq")

    def __init__(self, slots, nums=None, **keys):
        self.slots = slots
        self.nums = nums or {}
        self.keys = {k: keys.get(k, "") for k in KEY_COLUMNS}
        self.seq = 0

    def key_tuple(self):
        return tuple(self.keys[k] for k in KEY_COLUMNS)

    def key_label(self):
        vals = [self.keys[k] for k in KEY_COLUMNS if self.keys[k]]
        return " / ".join(vals)


def fire(slots, nums=None, **keys):
    return Firing(slots, nums, **keys)


# ----------------------------------------------------------- the rules
#
# One function per `[[rule]]`, named `r_<id>` with `-` -> `_` lowercased.
# Each returns a list of Firing, or a did-not-fire TOKEN string.

def r_status_1(view, ctx):
    status_by_rid = {}
    for ir in view.index_rows():
        status_by_rid[record_id_of(ir)] = (ir["testee_id"], ir["status"])
    out = []
    for r in view.rows("record", metric="agreement"):
        rid = r["testee"]
        hit = status_by_rid.get(rid)
        if hit is None or hit[1] == "measured":
            continue
        out.append(fire({"record_id": rid, "testee": hit[0],
                         "status": hit[1]},
                        testee=hit[0], record_id=rid))
    return out


def r_status_2(view, ctx):
    included = {r["testee"] for r in view.rows("record", metric="agreement")}
    pairs = set()
    for sv in view.header("subbench_versions").split(","):
        sv = sv.strip()
        if not sv or "@" not in sv:
            continue
        sb, ver = sv.rsplit("@", 1)
        pairs.add((sb, ver))
    machines = {m.strip() for m in view.header("machines").split(",") if m.strip()}
    out = []
    for ir in view.index_rows():
        if (ir["subbench"], ir["version"]) not in pairs:
            continue
        if ir["machine_id"] not in machines:
            continue
        if ir["status"] == "measured":
            continue
        rid = record_id_of(ir)
        if rid in included:
            continue
        out.append(fire({"record_id": rid, "testee": ir["testee_id"],
                         "timestamp": ir["timestamp"], "subbench": ir["subbench"],
                         "version": ir["version"], "machine": ir["machine_id"],
                         "status": ir["status"]},
                        testee=ir["testee_id"], record_id=rid))
    out.sort(key=lambda f: f.slots["record_id"])
    return out


def r_status_3(view, ctx):
    out = []
    for r in view.rows("excluded", metric="pass_rate"):
        out.append(fire({"pattern": r["pattern"], "regime": r["regime_or_na"],
                         "form": r["form"], "testee": r["testee"],
                         "pass_rate": r["pass_rate"], "n_wrong": r["n_wrong"],
                         "n_gave_up": r["n_gave_up"],
                         "gave_up_summary": "`" + r["gave_up_summary"] + "`"},
                        pattern=r["pattern"], regime=r["regime_or_na"],
                        form=r["form"], testee=r["testee"]))
    return out


def r_status_4(view, ctx):
    seen = {}
    for r in view.rows("did_not_compile"):
        seen.setdefault((r["pattern"], r["testee"]), r["gave_up_summary"])
    out = []
    for (pattern, testee), diag in sorted(seen.items()):
        out.append(fire({"pattern": pattern, "testee": testee,
                         "diagnostic": diag},
                        pattern=pattern, testee=testee))
    return out


def r_status_5(view, ctx):
    sup = view.header("superseded")
    nnm = view.header("newer_not_measured")
    inv = view.header("excluded_invalid")
    if not any(_int_or_zero(x) > 0 for x in (sup, nnm, inv)):
        return []
    return [fire({"candidates": candidates_from_source(view.header("source")),
                  "included": view.header("records"),
                  "superseded": sup, "newer_not_measured": nnm,
                  "excluded_invalid": inv})]


def _int_or_zero(s):
    try:
        return int(str(s).strip())
    except ValueError:
        return 0


def r_status_6(view, ctx):
    versions = view.header("schema_versions")
    members = [v for v in versions.split(",") if v.strip()]
    if len(members) < 2:
        return []
    recs = view.rows("record", metric="agreement")
    n_pre = sum(1 for r in recs if r["value"].startswith("n/a (v"))
    return [fire({"schema_versions": versions, "n_pre_14": str(n_pre),
                  "n_records": view.header("records")})]


def r_status_7(view, ctx):
    if view.header("mixed_x13").strip() != "True":
        return []
    return [fire({"x13_rules": view.header("x13_rules")})]


def r_status_8(view, ctx):
    v = view.header("worst_other_core_busy").strip()
    if not v or v == "n/a":
        return []
    return [fire({"worst_other_core_busy": v})]


def r_status_9(view, ctx):
    out = []
    for r in view.rows("record", metric="agreement"):
        if not r["value"].startswith("disagree"):
            continue
        out.append(fire({"record_id": r["testee"], "agreement": r["value"]},
                        record_id=r["testee"]))
    return out


def r_status_10(view, ctx):
    out = []
    for r in view.rows("record", metric="agreement"):
        dv = r["delta_verdict"]
        if not dv.startswith("after: "):
            continue
        out.append(fire({"record_id": r["testee"],
                         "after": dv[len("after: "):]},
                        record_id=r["testee"]))
    return out


def r_status_11(view, ctx):
    out = []
    for r in view.rows("scratch"):
        out.append(fire({"pattern": r["pattern"], "regime": r["regime_or_na"],
                         "form": r["form"], "testee": r["testee"]},
                        pattern=r["pattern"], regime=r["regime_or_na"],
                        form=r["form"], testee=r["testee"]))
    return out


def r_status_12(view, ctx):
    # (testee, regime, subject) -> {pattern: (code, bytes)}
    by_key = defaultdict(dict)
    for r in view.rows("excluded", metric="giveup_smallest"):
        key = (r["testee"], r["regime_or_na"], r["subject_or_na"])
        by_key[key][r["pattern"]] = (r["value"], r["n"])
    out = []
    for (testee, regime, subject), by_pattern in sorted(by_key.items()):
        for pa, pb in itertools.combinations(sorted(by_pattern), 2):
            code_a, bytes_a = by_pattern[pa]
            code_b, _bytes_b = by_pattern[pb]
            if code_a == code_b:
                continue
            out.append(fire({"subject": subject,
                             "subject_bytes": _fmt_bytes(bytes_a),
                             "code_a": "`" + code_a + "`", "pattern_a": pa,
                             "code_b": "`" + code_b + "`", "pattern_b": pb,
                             "testee": testee, "regime": regime},
                            subject_or_na=subject, regime=regime,
                            testee=testee))
    return out


def _fmt_bytes(s):
    try:
        return f"{int(s):,}"
    except (TypeError, ValueError):
        return s or "?"


def r_status_13(view, ctx):
    groups = defaultdict(list)
    for r in view.rows("rank", metric="median_ns"):
        groups[(r["pattern"], r["regime_or_na"])].append(
            (int(r["rank_or_na"]), r["testee"]))
    out = []
    for (pattern, regime), rows in sorted(groups.items()):
        if any(is_reference(t) for _rank, t in rows):
            continue
        best = min(rows)[1]
        out.append(fire({"pattern": pattern, "regime": regime,
                         "best_testee": best},
                        pattern=pattern, regime=regime))
    return out


# ---- R-DELTA ---------------------------------------------------------

def _delta_rows(view):
    """The (pattern, regime, form, testee) median_ns rank rows that carry
    a delta_verdict, with their stddev partner."""
    return [r for r in view.rows("rank", metric="median_ns")
            if r["delta_verdict"]]


_FASTER_SLOWER = re.compile(r"^(faster|slower) ×([0-9.]+)$")


def r_delta_1(view, ctx):
    out = []
    for r in _delta_rows(view):
        for clause in clauses_of(r["delta_verdict"]):
            m = _FASTER_SLOWER.match(clause)
            if not m:
                continue
            ratio = float(m.group(2))
            median = float(r["value"])
            out.append(fire({"pattern": r["pattern"],
                             "regime": r["regime_or_na"], "form": r["form"],
                             "testee": r["testee"], "verdict": clause,
                             "median_ns": fmt_ns(median),
                             "config": config_of(r["testee"]) or r["testee"],
                             "direction": m.group(1),
                             "ratio": fmt_ratio(ratio)},
                            nums={"ratio": ratio, "median_ns": median},
                            pattern=r["pattern"], regime=r["regime_or_na"],
                            form=r["form"], testee=r["testee"]))
    return out


def _delta_clause_rule(view, anchor):
    out = []
    for r in _delta_rows(view):
        for clause in clauses_of(r["delta_verdict"]):
            if not clause.startswith(anchor):
                continue
            out.append(fire({"pattern": r["pattern"],
                             "regime": r["regime_or_na"], "form": r["form"],
                             "testee": r["testee"], "rank": r["rank_or_na"],
                             "verdict": clause,
                             "config": config_of(r["testee"]) or r["testee"]},
                            pattern=r["pattern"], regime=r["regime_or_na"],
                            form=r["form"], testee=r["testee"]))
    return out


def r_delta_2(view, ctx):
    return _delta_clause_rule(view, "selection changed (")


def r_delta_3(view, ctx):
    return _delta_clause_rule(view, "now measured (was: ")


def r_delta_4(view, ctx):
    if ctx.predictions is None:
        return "input-absent"
    covered = ctx.prediction_coverage
    out = []
    for rid in ("R-DELTA-1", "R-RANK-1", "R-ARM-1", "R-FLOOR-2"):
        for f in ctx.firings.get(rid, ()):
            cell = (f.keys["pattern"], f.keys["regime"], f.keys["form"],
                    f.keys["testee"])
            if cell in covered:
                continue
            out.append(fire({"rule_id": rid, "pattern": cell[0],
                             "regime": cell[1], "form": cell[2],
                             "testee": cell[3],
                             "predictions_file": ctx.predictions_path},
                            pattern=cell[0], regime=cell[1], form=cell[2],
                            testee=cell[3]))
    return out


# ---- R-RANK ----------------------------------------------------------

def r_rank_1(view, ctx):
    ratio = {}
    median = {}
    groups = defaultdict(set)
    for r in view.rows("rank", metric="ratio_vs_baseline"):
        k = (r["pattern"], r["regime_or_na"], r["form"], r["testee"])
        ratio[k] = float(r["value"])
        groups[(r["pattern"], r["regime_or_na"])].add(k)
    for r in view.rows("rank", metric="median_ns"):
        median[(r["pattern"], r["regime_or_na"], r["form"],
                r["testee"])] = float(r["value"])
    out = []
    for (pattern, regime), cells in sorted(groups.items()):
        testees = {k[3] for k in cells}
        if not any(is_reference(t) for t in testees):
            continue          # the R-STATUS-13 guard
        reference = sorted(t for t in testees if is_reference(t))[0]
        by_config = defaultdict(list)
        for k in cells:
            parts = split_testee(k[3])
            if not parts:
                continue
            engine, version = parts[0], parts[1]
            by_config[(engine, config_of(k[3]), k[2])].append((version, k))
        for (_engine, config, form), members in sorted(by_config.items()):
            if len({v for v, _k in members}) < 2:
                continue
            ordered = sorted(members, key=lambda vk: ctx.pin_index(vk[0]))
            for (v_a, k_a), (v_b, k_b) in itertools.combinations(ordered, 2):
                r_a, r_b = ratio[k_a], ratio[k_b]
                if (r_a - 1.0) * (r_b - 1.0) >= 0:
                    continue
                out.append(fire({"pattern": pattern, "regime": regime,
                                 "form": form, "config": config,
                                 "reference": reference,
                                 "old_pin": v_a, "old_ratio": f"{r_a:.6f}",
                                 "new_pin": v_b, "new_ratio": f"{r_b:.6f}"},
                                nums={"new_ratio": r_b, "old_ratio": r_a},
                                pattern=pattern, regime=regime, form=form,
                                testee=k_b[3]))
    return out


# ---- R-ARM -----------------------------------------------------------

def r_arm_1(view, ctx):
    median = {}
    stddev = {}
    groups = defaultdict(list)
    for r in view.rows("rank", metric="median_ns"):
        k = (r["pattern"], r["regime_or_na"], r["form"], r["testee"])
        median[k] = float(r["value"])
        groups[(r["pattern"], r["regime_or_na"])].append(k)
    for r in view.rows("rank", metric="stddev_ns"):
        stddev[(r["pattern"], r["regime_or_na"], r["form"],
                r["testee"])] = float(r["value"])
    token_names = ("mode", "caps", "simd", "extra")
    out = []
    for (pattern, regime), cells in sorted(groups.items()):
        for k_a, k_b in itertools.combinations(sorted(cells), 2):
            if k_a[2] != k_b[2]:
                continue                       # same form only
            t_a, t_b = k_a[3], k_b[3]
            if is_reference(t_a) or is_reference(t_b):
                continue                       # neither arm is the reference
            p_a, p_b = split_testee(t_a), split_testee(t_b)
            if not p_a or not p_b:
                continue
            if p_a[0] != p_b[0] or p_a[1] != p_b[1]:
                continue                       # same engine and pin
            diff = [i for i in range(4) if p_a[2 + i] != p_b[2 + i]]
            if len(diff) != 1:
                continue
            spread = 2 * max(stddev.get(k_a, 0.0), stddev.get(k_b, 0.0))
            m_a, m_b = median[k_a], median[k_b]
            if abs(m_a - m_b) <= spread:
                continue
            ratio = (max(m_a, m_b) / min(m_a, m_b)) if min(m_a, m_b) else float("inf")
            c_a, c_b = config_of(t_a), config_of(t_b)
            i = diff[0]
            out.append(fire({"pattern": pattern, "regime": regime,
                             "form": k_a[2], "pin": p_a[1],
                             "config_a": c_a, "median_a": fmt_ns(m_a),
                             "config_b": c_b, "median_b": fmt_ns(m_b),
                             "ratio": fmt_ratio(ratio),
                             "spread": fmt_ns(spread),
                             "token_name": token_names[i],
                             "token_a": p_a[2 + i], "token_b": p_b[2 + i],
                             "arm_pair": " vs ".join(sorted([c_a, c_b]))},
                            nums={"ratio": ratio, "median_a": m_a,
                                  "median_b": m_b, "spread": spread},
                            pattern=pattern, regime=regime, form=k_a[2],
                            testee=t_a))
    return out


# ---- R-FLOOR ---------------------------------------------------------

def r_floor_1(view, ctx):
    out = []
    for r in view.rows("compile", metric="jitter"):
        if r["value"] != "timer-floor":
            continue
        out.append(fire({"pattern": r["pattern"], "form": r["form"],
                         "testee": r["testee"]},
                        pattern=r["pattern"], form=r["form"],
                        testee=r["testee"]))
    return out


def r_floor_2(view, ctx):
    floor_pattern = view.header("floor_pattern").strip()
    if not floor_pattern or floor_pattern == "none" or "," in floor_pattern:
        return "no-matching-rows"
    rows = view.rows("rank", metric="median_ns")
    means = {}
    for r in rows:
        n = _int_or_zero(r["n"])
        if not n:
            continue
        means[(r["pattern"], r["regime_or_na"], r["form"],
               r["testee"])] = float(r["value"]) / n
    floor_mean = {}
    for (pattern, regime, _form, testee), mean in means.items():
        if pattern == floor_pattern:
            floor_mean[(regime, testee)] = mean
    out = []
    for key in sorted(means):
        pattern, regime, form, testee = key
        if pattern == floor_pattern:
            continue
        fm = floor_mean.get((regime, testee))
        if fm is None or not fm:
            continue
        ratio = means[key] / fm
        if ratio > 1.0:
            continue
        out.append(fire({"pattern": pattern, "regime": regime, "form": form,
                         "testee": testee,
                         "cell_mean": f"{means[key]:.3f}",
                         "floor_pattern": floor_pattern,
                         "floor_mean": f"{fm:.3f}",
                         "ratio": f"{ratio:.3f}"},
                        nums={"ratio": ratio},
                        pattern=pattern, regime=regime, form=form,
                        testee=testee))
    return out


def r_floor_3(view, ctx):
    out = []
    for r in view.rows("compile", metric="jitter"):
        v = r["value"]
        if v == "timer-floor":
            continue
        try:
            ratio = float(v.split(" ")[0])
        except ValueError:
            continue
        if ratio < 1.0:
            continue
        out.append(fire({"pattern": r["pattern"], "form": r["form"],
                         "testee": r["testee"], "jitter": v},
                        nums={"jitter": ratio},
                        pattern=r["pattern"], form=r["form"],
                        testee=r["testee"]))
    return out


# ---- R-BUCKET --------------------------------------------------------

def r_bucket_form(view, ctx):
    groups = defaultdict(list)
    for r in view.rows("rank", metric="median_ns"):
        groups[(r["pattern"], r["regime_or_na"])].append(r["fact"])
    out = []
    for (pattern, regime), facts in sorted(groups.items()):
        n_sep = sum(1 for f in facts if f == "separate artifact")
        n_same = sum(1 for f in facts if f == "same program")
        if not (n_sep and n_same):
            continue
        out.append(fire({"pattern": pattern, "regime": regime,
                         "n_separate": str(n_sep), "n_same": str(n_same)},
                        pattern=pattern, regime=regime))
    return out


def r_bucket_vsbest(view, ctx):
    groups = defaultdict(set)
    for r in view.rows("rank", metric="median_ns"):
        parts = split_testee(r["testee"])
        if not parts or parts[0] != "pcrec":
            continue
        groups[(r["pattern"], r["regime_or_na"])].add(parts[1])
    out = []
    for (pattern, regime), slugs in sorted(groups.items()):
        if len(slugs) < 2:
            continue
        out.append(fire({"pattern": pattern, "regime": regime,
                         "n_slugs": str(len(slugs)),
                         "pin_slugs": ", ".join(sorted(slugs))},
                        pattern=pattern, regime=regime))
    return out


def r_bucket_span(view, ctx):
    ts_by_testee = {}
    included = {r["testee"] for r in view.rows("record", metric="agreement")}
    for ir in view.index_rows():
        if record_id_of(ir) in included:
            ts_by_testee[ir["testee_id"]] = ir["timestamp"]
    out = []
    rows = view.rows("rank", metric="median_ns")
    by_cell = defaultdict(list)
    for r in rows:
        by_cell[(r["pattern"], r["regime_or_na"], r["form"])].append(r)
    for cell, cell_rows in sorted(by_cell.items()):
        for r in sorted(cell_rows, key=lambda x: x["testee"]):
            if not r["delta_verdict"]:
                continue
            parts = split_testee(r["testee"])
            if not parts:
                continue
            engine, version = parts[0], parts[1]
            cfg = config_of(r["testee"])
            mine = ts_by_testee.get(r["testee"])
            older = []
            for other in cell_rows:
                if other["testee"] == r["testee"]:
                    continue
                p2 = split_testee(other["testee"])
                if not p2 or p2[0] != engine or config_of(other["testee"]) != cfg:
                    continue
                if p2[1] == version:
                    continue
                ts = ts_by_testee.get(other["testee"])
                if mine is None or ts is None or ts >= mine:
                    continue
                older.append((ts, p2[1]))
            if not older:
                continue
            older.sort()
            prev_pin = older[-1][1]
            span = abs(ctx.pin_index(version) - ctx.pin_index(prev_pin))
            if span <= 1:
                continue
            out.append(fire({"pattern": cell[0], "regime": cell[1],
                             "form": cell[2], "testee": r["testee"],
                             "config": cfg, "old_pin": prev_pin,
                             "new_pin": version, "span": str(span),
                             "verdict": r["delta_verdict"]},
                            nums={"span": float(span)},
                            pattern=cell[0], regime=cell[1], form=cell[2],
                            testee=r["testee"]))
    return out


def r_bucket_dominated(view, ctx):
    if ctx.subject_grain is None:
        return "input-absent"
    totals = defaultdict(list)
    for r in view.rows("rank", metric="median_ns"):
        totals[(r["pattern"], r["regime_or_na"], r["testee"])].append(
            (float(r["value"]), r["subject_or_na"]))
    out = []
    for (pattern, regime, testee), members in sorted(totals.items()):
        total = sum(v for v, _s in members)
        if not total:
            continue
        top = max(members)
        share = top[0] / total
        if share <= 0.90:
            continue
        out.append(fire({"pattern": pattern, "regime": regime,
                         "testee": testee, "subject": top[1],
                         "share": f"{share * 100:.1f}%"},
                        nums={"share": share},
                        pattern=pattern, regime=regime,
                        subject_or_na=top[1], testee=testee))
    return out


def r_bucket_kb(view, ctx):
    if not ctx.catalogue.get("signature"):
        return "no-registered-signatures"
    raise InterpretError("R-BUCKET-KB: a signature is registered but "
                         "catalogue 1.0 defines no matching code; "
                         "registration is a MAJOR bump (§3.3)")


# ---- R-PRED ----------------------------------------------------------

def _pred_rule(view, ctx, want):
    if ctx.predictions is None:
        return "input-absent"
    out = []
    for parent in ctx.prediction_verdicts:
        if parent["verdict"] != want:
            continue
        p = parent["representative"]
        if want == "partial":
            out.append(fire({"prediction_id": parent["prediction_id"],
                             "source": p["source"],
                             "source_ref": p["source_ref"],
                             "n_confirmed": str(parent["n_confirmed"]),
                             "n_refuted": str(parent["n_refuted"]),
                             "n_not_evaluable": str(parent["n_not_evaluable"]),
                             "clause_verdicts": parent["clause_verdicts"]},
                            prediction_id=parent["prediction_id"]))
        elif want == "not-evaluable":
            out.append(fire({"prediction_id": parent["prediction_id"],
                             "source": p["source"],
                             "source_ref": p["source_ref"],
                             "reason": parent["reason"]},
                            prediction_id=parent["prediction_id"]))
        else:
            out.append(fire({"prediction_id": parent["prediction_id"],
                             "source": p["source"],
                             "source_ref": p["source_ref"],
                             "claim": parent["claim"],
                             "measured": parent["measured"]},
                            prediction_id=parent["prediction_id"]))
    return out


def r_pred_1(view, ctx):
    return _pred_rule(view, ctx, "confirmed")


def r_pred_2(view, ctx):
    return _pred_rule(view, ctx, "refuted")


def r_pred_3(view, ctx):
    return _pred_rule(view, ctx, "not-evaluable")


def r_pred_4(view, ctx):
    return _pred_rule(view, ctx, "partial")


def function_name(rule_id):
    """`R-DELTA-1` -> `r_delta_1` (§3.2: the executable predicate is a
    python function in this module named exactly `id` with `-` -> `_`,
    lowercased)."""
    return rule_id.lower().replace("-", "_")


def rule_function(rule_id):
    return globals().get(function_name(rule_id))


# ------------------------------------------------------- the catalogue

def load_catalogue(path):
    """Load `catalogue/rules.toml` with every load-time check §3.2.1,
    §3.2.2 and §8(1) require."""
    with open(path, "rb") as fh:
        cat = tomllib.load(fh)
    if "catalogue_version" not in cat:
        raise InterpretError(f"{path}: no catalogue_version")
    rules = cat.get("rule") or []
    if not rules:
        raise InterpretError(f"{path}: no [[rule]] blocks")
    seen = set()
    for rule in rules:
        rid = rule.get("id")
        if not rid:
            raise InterpretError(f"{path}: a [[rule]] with no id")
        if rid in seen:
            raise InterpretError(f"{path}: duplicate rule id {rid}")
        seen.add(rid)
        for field in RULE_FIELDS:
            if field not in rule:
                raise InterpretError(f"{path}: {rid} has no {field!r} field")
        if not rule["grain"] or any(g not in ("set", "subject")
                                    for g in rule["grain"]):
            raise InterpretError(f"{path}: {rid}'s grain must be a non-empty "
                                 f"subset of set/subject")
        if rule.get("retired_in"):
            continue
        fn = rule_function(rid)
        if fn is None:
            raise InterpretError(f"{path}: {rid} has no function "
                                 f"{function_name(rid)} in interpret.py")
        parse_inputs(rule["inputs"], rid)
        for slot in rule["aggregate"]:
            if slot not in rule["slots"]:
                raise InterpretError(f"{path}: {rid} aggregates on {slot!r}, "
                                     f"which is not one of its slots")
        if "extremal" in rule and rule["extremal"] not in rule["slots"]:
            raise InterpretError(f"{path}: {rid}'s extremal {rule['extremal']!r} "
                                 f"is not one of its slots")
        used = set(re.findall(r"\{([a-z_0-9]+)\}", rule["template"]))
        undeclared = used - set(rule["slots"])
        if undeclared:
            raise InterpretError(f"{path}: {rid}'s template uses undeclared "
                                 f"slot(s) {sorted(undeclared)}")
        if re.search(r"\{[a-z_0-9]+\}", rule["no_fire"]):
            raise InterpretError(f"{path}: {rid}'s no_fire sentence carries a "
                                 f"slot; it must be slot-free (§7.1)")
    # ... and every rule FUNCTION has a [[rule]] (§8(1)'s other
    # direction): a rule function is exactly a module-level callable
    # whose name round-trips to a rule id shape.
    for name, obj in list(globals().items()):
        if not callable(obj) or not re.fullmatch(
                r"r_(status|delta|rank|arm|floor|pred|bucket)_[a-z0-9]+", name):
            continue
        rid = name.upper().replace("_", "-")
        if _canonical_rule_id(rid, seen) is None:
            raise InterpretError(f"interpret.py: function {name} has no "
                                 f"[[rule]] in {path}")
    if not cat.get("pin_order"):
        raise InterpretError(f"{path}: no [[pin_order]] table")
    return cat


def _canonical_rule_id(candidate, ids):
    if candidate in ids:
        return candidate
    return None


def check_links(cat, repo_root):
    """§7.3: every `links` entry resolves -- the file exists, and an
    anchor appears as a literal string in it."""
    for rule in cat["rule"]:
        for link in rule.get("links", ()):
            path, _sep, anchor = link.partition("#")
            full = os.path.join(repo_root, path)
            if not os.path.exists(full):
                raise InterpretError(f"{rule['id']}: link {link!r} does not "
                                     f"resolve ({full} missing)")
            if anchor and anchor not in _read(full):
                raise InterpretError(f"{rule['id']}: link {link!r}'s anchor is "
                                     f"not in {path}")


# ------------------------------------------------------------ the engine

class Context:
    def __init__(self, cat, report, index, predictions=None,
                 predictions_path="(none)", subject_grain=None):
        self.catalogue = cat
        self.report = report
        self.index = index
        self.predictions = predictions
        self.predictions_path = predictions_path
        self.subject_grain = subject_grain
        self.firings = {}
        self.prediction_verdicts = []
        self.prediction_coverage = set()
        self._pin_pos = {}
        for entry in cat["pin_order"]:
            for i, pin in enumerate(entry["pins"]):
                self._pin_pos[(entry["engine"], pin)] = i
                self._pin_pos[pin] = i

    def pin_index(self, pin):
        if pin not in self._pin_pos:
            raise InterpretError(
                f"pin {pin!r} is not in the catalogue's [[pin_order]] table; "
                f"append it (interpreter_v1.md §4.7, Q10) and re-run")
        return self._pin_pos[pin]


# R-DELTA-4 is a CROSS-CLASS rule: its predicate reads other rules'
# firings (§4.2), so it is evaluated after all of them and then put back
# in its declaration position, which is what the output order is.
DEFERRED_RULES = ("R-DELTA-4",)


def run_rules(cat, report, index, ctx):
    """Run every rule in catalogue declaration order. Returns
    [(rule, firings_or_token)]."""
    results = []
    deferred = []
    for rule in cat["rule"]:
        rid = rule["id"]
        if rid in DEFERRED_RULES:
            deferred.append((len(results), rule))
            results.append((rule, "no-matching-rows"))
            continue
        if rule.get("retired_in"):
            results.append((rule, "retired"))
            continue
        if report.grain not in rule["grain"]:
            results.append((rule, "grain"))
            ctx.firings[rid] = []
            continue
        view = RuleView(rule, report, index)
        out = rule_function(rid)(view, ctx)
        if isinstance(out, str):
            if out not in DID_NOT_FIRE_TOKENS:
                raise InterpretError(f"{rid}: unknown did-not-fire token "
                                     f"{out!r}")
            ctx.firings[rid] = []
            results.append((rule, out))
            continue
        for f in out:
            missing = set(rule["slots"]) - set(f.slots)
            extra = set(f.slots) - set(rule["slots"])
            if missing or extra:
                raise InterpretError(
                    f"{rid}: firing carries slots {sorted(f.slots)}, declared "
                    f"{sorted(rule['slots'])} (missing {sorted(missing)}, "
                    f"extra {sorted(extra)})")
        check_extremal(rule, out)
        out.sort(key=lambda f: (f.key_tuple(),
                                tuple(sorted(f.slots.items()))))
        for i, f in enumerate(out, start=1):
            f.seq = i
        ctx.firings[rid] = out
        results.append((rule, out if out else "no-matching-rows"))
    for position, rule in deferred:
        results[position] = (rule, _run_one(rule, report, index, ctx))
    return results


def _run_one(rule, report, index, ctx):
    rid = rule["id"]
    if report.grain not in rule["grain"]:
        ctx.firings[rid] = []
        return "grain"
    out = rule_function(rid)(RuleView(rule, report, index), ctx)
    if isinstance(out, str):
        if out not in DID_NOT_FIRE_TOKENS:
            raise InterpretError(f"{rid}: unknown did-not-fire token {out!r}")
        ctx.firings[rid] = []
        return out
    for f in out:
        missing = set(rule["slots"]) - set(f.slots)
        extra = set(f.slots) - set(rule["slots"])
        if missing or extra:
            raise InterpretError(
                f"{rid}: firing carries slots {sorted(f.slots)}, declared "
                f"{sorted(rule['slots'])}")
    check_extremal(rule, out)
    out.sort(key=lambda f: (f.key_tuple(), tuple(sorted(f.slots.items()))))
    for i, f in enumerate(out, start=1):
        f.seq = i
    ctx.firings[rid] = out
    return out if out else "no-matching-rows"


def render_facts_tsv(results):
    lines = ["\t".join(FACTS_COLUMNS)]
    for rule, out in results:
        rid = rule["id"]
        if isinstance(out, str):
            lines.append("\t".join([rid, "0", "0", "", "", "", "", "", "", "",
                                    "", out]))
            continue
        for f in out:
            for slot in rule["slots"]:
                lines.append("\t".join(
                    [rid, "1", str(f.seq), f.keys["pattern"],
                     f.keys["subject_or_na"], f.keys["regime"],
                     f.keys["form"], f.keys["testee"], f.keys["record_id"],
                     f.keys["prediction_id"], slot, f.slots[slot]]))
    return "\n".join(lines) + "\n"


def render_one(rule, firing):
    return rule["template"].format(**firing.slots)


def _group_key(rule, firing):
    return tuple(firing.slots[s] for s in rule["aggregate"])


def check_extremal(rule, firings):
    """§5.2's invariant, enforced where the firings are: a rule that
    aggregates and carries a numeric slot MUST declare which slot is
    "biggest"; a rule that declares one must actually produce it.

    The RENDER itself reads only the declared `extremal` name and parses
    the number back out of the rendered slot string, so the sidecar is a
    function of the facts TSV alone (§8(5))."""
    numeric = set()
    for f in firings:
        numeric |= set(f.nums)
    if "extremal" in rule:
        if rule["extremal"] not in numeric:
            raise InterpretError(f"{rule['id']}: declared extremal "
                                 f"{rule['extremal']!r} is not a numeric slot "
                                 f"of its firings")
    elif numeric and rule["aggregate"]:
        raise InterpretError(
            f"{rule['id']}: aggregates on {rule['aggregate']} and carries "
            f"numeric slot(s) {sorted(numeric)} but declares no `extremal` "
            f"(§5.2)")


def slot_number(text):
    """The number inside a rendered numeric slot -- the ONE formatter's
    output read back (`6,291.5` -> 6291.5, `12.000` -> 12.0). Ordering
    reads this, never the unrounded float, so a render built from the
    facts TSV is byte-identical to the direct one."""
    try:
        return float(str(text).replace(",", "").replace("%", ""))
    except ValueError:
        return 0.0


def render_bullets(rule, firings):
    """§5.2's counted collapse. `aggregate = []` is one bullet per
    firing; otherwise one bullet per group, carrying the count, then the
    extremal firing (and the minimum where the group has more than two
    members) for a rule with a numeric slot or the full sorted list of
    the group's firing keys for a rule with none, then a pointer to the
    facts TSV."""
    bullets = []
    links = ["\n  See: " + link for link in rule.get("links", ())]
    link_text = "".join(links)
    if not rule["aggregate"]:
        for f in firings:
            bullets.append("- " + render_one(rule, f) + link_text)
        return bullets
    extremal = rule.get("extremal")
    groups = defaultdict(list)
    for f in firings:
        groups[_group_key(rule, f)].append(f)
    for key in sorted(groups):
        members = groups[key]
        label = " × ".join(key)
        n = len(members)
        head = f"- **{label}** — {n} firing(s)."
        if extremal is None:
            ordered = sorted(members, key=lambda f: f.key_tuple())
            body = f"{head} First by key: " + render_one(rule, ordered[0])
            if n > 1:
                rest = "; ".join(f.key_label() for f in ordered[1:])
                body += f"\n  Also: {rest}."
            body += f"\n  All {n} in the facts TSV." + link_text
            bullets.append(body)
            continue
        ordered = sorted(members, key=lambda f: (slot_number(f.slots[extremal]),
                                                 f.key_tuple()))
        body = (f"{head} Extremal by `{extremal}`: "
                + render_one(rule, ordered[-1]))
        if n > 2:
            body += (f"\n  Minimum by `{extremal}`: "
                     + render_one(rule, ordered[0]))
        body += f"\n  All {n} in the facts TSV." + link_text
        bullets.append(body)
    return bullets


def results_from_facts(cat, facts_text):
    """Reassemble [(rule, firings_or_token)] from a facts TSV, by
    `(rule_id, firing_seq)` -- §8(5)'s own reassembly, which is why
    §5.1 carries the `firing_seq` column."""
    by_rule = {}
    tokens = {}
    lines = facts_text.split("\n")
    if lines[0].split("\t") != FACTS_COLUMNS:
        raise InterpretError("facts TSV: unexpected column list")
    for ln in lines[1:]:
        if not ln:
            continue
        f = ln.split("\t")
        if len(f) != len(FACTS_COLUMNS):
            raise InterpretError(f"facts TSV: malformed row {ln[:80]!r}")
        row = dict(zip(FACTS_COLUMNS, f))
        rid = row["rule_id"]
        if row["fired"] == "0":
            tokens[rid] = row["value"]
            continue
        firing = by_rule.setdefault(rid, {}).get(row["firing_seq"])
        if firing is None:
            firing = Firing({}, {}, pattern=row["pattern"],
                            subject_or_na=row["subject_or_na"],
                            regime=row["regime"], form=row["form"],
                            testee=row["testee"], record_id=row["record_id"],
                            prediction_id=row["prediction_id"])
            firing.seq = int(row["firing_seq"])
            by_rule[rid][row["firing_seq"]] = firing
        firing.slots[row["slot"]] = row["value"]
    results = []
    for rule in cat["rule"]:
        rid = rule["id"]
        if rid in tokens:
            results.append((rule, tokens[rid]))
            continue
        firings = [by_rule[rid][k] for k in
                   sorted(by_rule.get(rid, {}), key=int)]
        results.append((rule, firings if firings else "no-matching-rows"))
    return results


def render_markdown(results, ctx, stamp):
    out = ["<!-- pcrecbench interpret"]
    for k, v in stamp:
        out.append(f"{k + ':':<17}{v}")
    out.append("-->")
    out.append("")
    name = os.path.basename(ctx.report.path)
    if name.endswith(".tsv"):
        name = name[:-4]
    out.append(f"# Interpretation — {name}")
    out.append("")
    out.append(f"Generated by `pcrecbench interpret` against catalogue "
               f"{ctx.catalogue['catalogue_version']}. Every sentence below "
               f"is a rule template. No sentence is generated.")
    out.append("")
    not_fired = []
    for rule, res in results:
        if isinstance(res, str):
            not_fired.append((rule, res))
            continue
        bullets = render_bullets(rule, res)
        n = len(res)
        if rule["aggregate"]:
            head = (f"## {rule['id']} — {rule['title']} ({n} firing(s), "
                    f"aggregated to {len(bullets)} by "
                    f"{' × '.join(rule['aggregate'])})")
        else:
            head = (f"## {rule['id']} — {rule['title']} ({n} firing(s), "
                    f"not aggregated)")
        out.append(head)
        out.append("")
        out.extend(bullets)
        out.append("")
    out.append("## Rules that did not fire")
    out.append("")
    out.append("| rule | reason |")
    out.append("|---|---|")
    for rule, token in not_fired:
        out.append(f"| {rule['id']} | {token} ({rule['no_fire']}) |")
    out.append("")
    return "\n".join(out)


# ------------------------------------------------------- the predictions

PRED_COLUMNS = ["prediction_id", "clause", "source", "source_ref",
                "stated_utc", "subbench", "version", "selector", "quantity",
                "reducer", "op", "lo", "hi", "unit", "note"]

QUANTITIES = {"median_ns", "min_ns", "max_ns", "stddev_ns",
              "ratio_vs_baseline", "ratio_vs_best", "rank_in_group",
              "pass_rate", "n_gave_up", "n_wrong", "delta_verdict", "status",
              "section", "compile:median_total_ns", "compile:artifact_bytes",
              "compile:emit_bytes", "compile:emit_code_bytes"}

OPS = {"lt", "lte", "gt", "gte", "between", "eq", "neq", "eq-token",
       "neq-token", "set-eq", "set-subset", "present", "absent"}

REDUCERS = {"identity", "ratio_to", "ratio_to_median_over",
            "ratio_max_min_over", "rank_over", "count", "set_of", "max",
            "min", "median"}

SELECTOR_KEYS = {"pattern", "subject_or_na", "regime_or_na", "form", "testee",
                 "section"}


class PredictionError(InterpretError):
    pass


def parse_selector(text, where):
    out = {}
    for clause in text.split(";"):
        clause = clause.strip()
        if not clause:
            continue
        if "=" not in clause:
            raise PredictionError(f"{where}: selector clause {clause!r} is not "
                                  f"<key>=<glob>")
        k, v = clause.split("=", 1)
        if k not in SELECTOR_KEYS:
            raise PredictionError(
                f"{where}: selector key {k!r} is not one of the closed set "
                f"{sorted(SELECTOR_KEYS)}")
        out[k] = v
    return out


def _glob_match(pattern, value):
    for alt in pattern.split("|"):
        rx = "^" + ".*".join(re.escape(p) for p in alt.split("*")) + "$"
        if re.match(rx, value):
            return True
    return False


def load_predictions(path):
    rows = []
    lines = _read(path).split("\n")
    if not lines:
        raise PredictionError(f"{path}: empty predictions file")
    cols = lines[0].split("\t")
    if cols != PRED_COLUMNS:
        raise PredictionError(f"{path}: columns {cols} != {PRED_COLUMNS}")
    for n, ln in enumerate(lines[1:], start=2):
        if not ln.strip():
            continue
        f = ln.split("\t")
        if len(f) != len(PRED_COLUMNS):
            raise PredictionError(f"{path}:{n}: {len(f)} fields, expected "
                                  f"{len(PRED_COLUMNS)}")
        row = dict(zip(PRED_COLUMNS, f))
        where = f"{path}:{n} ({row['prediction_id']}{row['clause']})"
        if row["quantity"] not in QUANTITIES:
            raise PredictionError(
                f"{where}: quantity {row['quantity']!r} is not in the closed "
                f"set the report TSV can answer. The TSV carries no answer, "
                f"span or capture (§6.4), so a prediction that needs one is a "
                f"load error, never a silent not-evaluable.")
        if row["op"] not in OPS:
            raise PredictionError(f"{where}: op {row['op']!r} is not in the "
                                  f"closed set {sorted(OPS)}")
        reducer = (row["reducer"] or "identity").strip()
        head = reducer.split("(", 1)[0]
        if head not in REDUCERS:
            raise PredictionError(f"{where}: reducer {reducer!r} is not in the "
                                  f"closed set {sorted(REDUCERS)}")
        row["_selector"] = parse_selector(row["selector"], where)
        row["_reducer"] = reducer
        row["_where"] = where
        rows.append(row)
    return rows


def check_stated_utc(predictions, index, where="predictions"):
    """§6.5, corrected by cross-review I-58: `stated_utc` must precede the
    EARLIEST index timestamp for this (subbench, version) population
    INCLUDING superseded rows -- not the report's own earliest, which a
    supersession window leaves open. The residual limit is stated in the
    note: it proves only that a prediction predates this population's
    first-ever measurement."""
    if index is None:
        return
    earliest = {}
    for r in index.rows:
        key = (r["subbench"], r["version"])
        ts = r["timestamp"]
        if key not in earliest or ts < earliest[key]:
            earliest[key] = ts
    for p in predictions:
        key = (p["subbench"], p["version"])
        first = earliest.get(key)
        if first is None:
            continue                    # never measured: the check is vacuous
        if p["stated_utc"] >= first:
            raise PredictionError(
                f"{p['_where']}: stated_utc {p['stated_utc']} does not precede "
                f"the earliest store/index.tsv timestamp for "
                f"{key[0]}@{key[1]} ({first}), superseded rows included "
                f"(§6.5)")


_QUANT_COLUMN = {"pass_rate": "pass_rate", "n_gave_up": "n_gave_up",
                 "n_wrong": "n_wrong", "delta_verdict": "delta_verdict",
                 "status": "status", "section": "section",
                 "rank_in_group": "rank_or_na"}
_QUANT_METRIC = {"median_ns": "median_ns", "min_ns": "min_ns",
                 "max_ns": "max_ns", "stddev_ns": "stddev_ns",
                 "ratio_vs_baseline": "ratio_vs_baseline",
                 "ratio_vs_best": "ratio_vs_best"}
_COMPILE_METRIC = {"compile:median_total_ns": ("median_total_ns",
                                               "derived_first_match_row_minus_"
                                               "steady_state_ns"),
                   "compile:artifact_bytes": ("artifact_bytes",),
                   "compile:emit_bytes": ("emit_bytes",),
                   "compile:emit_code_bytes": ("emit_code_bytes",)}


def _select(view, pred, sections=None):
    """The prediction's own selector, applied to the sections it names.

    A selector that names `section` reads exactly those sections. One
    that does not reads `rank` (or `compile` for a `compile:` quantity)
    -- and `_elsewhere` below is what finds the same cell in the
    excluded / not-ranked / did-not-compile / scratch sections so
    R-PRED-3 can say WHERE it went instead of "absent".
    """
    sel = dict(pred["_selector"])
    section = sel.pop("section", None)
    quantity = pred["quantity"]
    if sections is None:
        if quantity in _COMPILE_METRIC:
            sections = ["compile"]
        elif section:
            sections = [s for s in SECTIONS if _glob_match(section, s)]
        else:
            sections = ["rank"]
    rows = []
    for s in sections:
        for r in view.rows(s):
            if not all(_glob_match(g, r[k]) for k, g in sel.items()):
                continue
            rows.append(r)
    return rows


_ELSEWHERE = ("excluded", "not_ranked", "did_not_compile", "scratch")


def _elsewhere(view, pred):
    """The non-ranked sections a prediction's cell landed in, if any."""
    if "section" in pred["_selector"]:
        return set()
    rows = _select(view, pred, sections=list(_ELSEWHERE))
    return {r["section"] for r in rows}


def _value_of(row, quantity):
    if quantity in _QUANT_METRIC:
        if row["metric"] != _QUANT_METRIC[quantity]:
            return None
        return _float_or_none(row["value"])
    if quantity in _COMPILE_METRIC:
        if row["metric"] not in _COMPILE_METRIC[quantity]:
            return None
        return _float_or_none(row["value"])
    col = _QUANT_COLUMN[quantity]
    val = row[col]
    if quantity in ("pass_rate", "n_gave_up", "n_wrong", "rank_in_group"):
        return _float_or_none(val)
    return val


def _float_or_none(text):
    """An empty or non-finite cell is NOT a number: `render_tsv` writes
    `""` where a value is None and `nan` where a ratio has no baseline,
    and a prediction must not be scored against either."""
    try:
        v = float(text)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(v) or math.isinf(v) else v


def _keyed_values(view, pred):
    """[(key tuple, value)] for the prediction's selected rows."""
    out = []
    for r in _select(view, pred):
        v = _value_of(r, pred["quantity"])
        if v is None:
            continue
        out.append(((r["pattern"], r["subject_or_na"], r["regime_or_na"],
                     r["form"], r["testee"]), v, r))
    return out


_KEY_INDEX = {"pattern": 0, "subject_or_na": 1, "regime_or_na": 2,
              "form": 3, "testee": 4}


def _drop(key_tuple, name):
    """A key tuple with one named column removed -- the grouping key a
    `<reducer>_over(<key>)` reduces within."""
    return tuple(x for i, x in enumerate(key_tuple) if i != _KEY_INDEX[name])


def _reduce(view, pred, values):
    """Apply the prediction's declared reducer. Returns
    (list of (label, value), kind) where kind is 'num' or 'set'."""
    reducer = pred["_reducer"]
    head, _, arg = reducer.partition("(")
    arg = arg.rstrip(")")
    if head in ("identity", ""):
        return [("/".join(k), v) for k, v, _r in values], "num"
    if head == "count":
        return [("count", float(len(values)))], "num"
    if head == "set_of":
        if arg not in _KEY_INDEX:
            raise PredictionError(f"{pred['_where']}: set_of({arg}) is not a "
                                  f"key column")
        members = sorted({k[_KEY_INDEX[arg]] for k, _v, _r in values})
        return [("set", members)], "set"
    if head in ("max", "min", "median"):
        nums = sorted(v for _k, v, _r in values)
        if not nums:
            return [], "num"
        pick = {"max": nums[-1], "min": nums[0],
                "median": nums[len(nums) // 2]}[head]
        return [(head, pick)], "num"
    if head == "ratio_to":
        other = dict(pred)
        other["_selector"] = parse_selector(arg, pred["_where"])
        base = _keyed_values(view, other)
        if not base:
            return [], "num"
        # Join the two populations on every key column the two selectors
        # agree about; the ratio is then per (regime, form, testee) and
        # not one number over the whole report.
        join = [k for k in sorted(_KEY_INDEX)
                if pred["_selector"].get(k) == other["_selector"].get(k)]
        by_join = defaultdict(list)
        for k, v, _r in base:
            by_join[tuple(k[_KEY_INDEX[j]] for j in join)].append(v)
        out = []
        for k, v, _r in values:
            denom = by_join.get(tuple(k[_KEY_INDEX[j]] for j in join))
            if not denom:
                continue
            med = sorted(denom)[len(denom) // 2]
            if not med:
                continue
            out.append(("/".join(k), v / med))
        return out, "num"
    if head == "ratio_to_median_over":
        if arg not in _KEY_INDEX:
            raise PredictionError(f"{pred['_where']}: "
                                  f"ratio_to_median_over({arg}) is not a key "
                                  f"column")
        groups = defaultdict(list)
        for k, v, _r in values:
            groups[_drop(k, arg)].append(v)
        out = []
        for k, v, _r in values:
            vs = sorted(groups[_drop(k, arg)])
            med = vs[len(vs) // 2]
            if not med:
                continue
            out.append(("/".join(k), v / med))
        return out, "num"
    if head == "ratio_max_min_over":
        if arg not in _KEY_INDEX:
            raise PredictionError(f"{pred['_where']}: "
                                  f"ratio_max_min_over({arg}) is not a key "
                                  f"column")
        groups = defaultdict(list)
        for k, v, _r in values:
            gk = tuple(x for i, x in enumerate(k) if i != _KEY_INDEX[arg])
            groups[gk].append(v)
        out = []
        for gk, vs in sorted(groups.items()):
            lo, hi = min(vs), max(vs)
            if not lo:
                continue
            out.append(("/".join(gk), hi / lo))
        return out, "num"
    if head == "rank_over":
        if arg not in _KEY_INDEX:
            raise PredictionError(f"{pred['_where']}: rank_over({arg}) is not "
                                  f"a key column")
        # The POSITION of a selected row among every row that shares its
        # other key columns -- the population is the selector with the
        # ranked key wildcarded, so "the three cheapest cells IN THE SET"
        # is a rank among all of them, not among the three named.
        population = dict(pred)
        population["_selector"] = dict(pred["_selector"], **{arg: "*"})
        groups = defaultdict(list)
        for k, v, _r in _keyed_values(view, population):
            groups[_drop(k, arg)].append((v, k))
        pos_of = {}
        for gk, vs in groups.items():
            for pos, (_v, k) in enumerate(sorted(vs), start=1):
                pos_of[k] = float(pos)
        out = []
        for k, _v, _r in values:
            if k in pos_of:
                out.append(("/".join(k), pos_of[k]))
        return out, "num"
    raise PredictionError(f"{pred['_where']}: unhandled reducer {reducer!r}")


def _op_holds(pred, value):
    op = pred["op"]
    lo = pred["lo"].strip()
    hi = pred["hi"].strip()
    if op in ("present", "absent"):
        return (value is not None) if op == "present" else (value is None)
    if op in ("eq-token", "neq-token"):
        same = str(value) == hi
        return same if op == "eq-token" else not same
    if op == "set-eq":
        want = [x for x in hi.split("|") if x]
        return sorted(value) == sorted(want)
    if op == "set-subset":
        want = {x for x in hi.split("|") if x}
        return set(value) <= want
    v = float(value)
    if op == "between":
        return float(lo) <= v <= float(hi)
    bound = float(hi)
    return {"lt": v < bound, "lte": v <= bound, "gt": v > bound,
            "gte": v >= bound, "eq": v == bound, "neq": v != bound}[op]


def evaluate_predictions(cat, report, index, predictions, ctx):
    """Score every clause, then roll each parent prediction up by §4.6's
    arithmetic: all-confirmed -> R-PRED-1, all-refuted -> R-PRED-2, any
    mix -> R-PRED-4, no evaluable clause -> R-PRED-3."""
    rule = next(r for r in cat["rule"] if r["id"] == "R-PRED-1")
    view = RuleView(rule, report, index)
    by_parent = defaultdict(list)
    for p in predictions:
        by_parent[p["prediction_id"]].append(p)
    verdicts = []
    coverage = set()
    for pid in sorted(by_parent):
        clauses = sorted(by_parent[pid], key=lambda p: p["clause"])
        per = []
        for p in clauses:
            rows = _select(view, p)
            for r in rows:
                coverage.add((r["pattern"], r["regime_or_na"], r["form"],
                              r["testee"]))
            if not rows:
                other = _elsewhere(view, p)
                if other:
                    per.append((p, "not-evaluable",
                                f"{p['prediction_id']}{p['clause'] or ''}: the "
                                f"selected cell is in the "
                                + ", ".join(sorted(other)) + " section", ""))
                else:
                    per.append((p, "not-evaluable",
                                f"{p['prediction_id']}{p['clause'] or ''}: no "
                                f"row in this report matches the selector",
                                ""))
                continue
            values = _keyed_values(view, p)
            if not values:
                per.append((p, "not-evaluable", "the selected rows carry no "
                                                "value for this quantity", ""))
                continue
            reduced, kind = _reduce(view, p, values)
            if not reduced:
                per.append((p, "not-evaluable", "the reducer produced no "
                                                "value", ""))
                continue
            bad = [(lbl, v) for lbl, v in reduced if not _op_holds(p, v)]
            measured = _measured_text(p, reduced, bad, kind)
            per.append((p, "refuted" if bad else "confirmed", "", measured))
        n_c = sum(1 for _p, v, _r, _m in per if v == "confirmed")
        n_r = sum(1 for _p, v, _r, _m in per if v == "refuted")
        n_n = sum(1 for _p, v, _r, _m in per if v == "not-evaluable")
        rep = clauses[0]
        entry = {"prediction_id": pid, "representative": rep,
                 "n_confirmed": n_c, "n_refuted": n_r, "n_not_evaluable": n_n,
                 "clause_verdicts": "; ".join(
                     f"{p['prediction_id']}{p['clause'] or ''} {v}"
                     for p, v, _r, _m in per),
                 "claim": _claim_text(rep, per),
                 "measured": "; ".join(m for _p, _v, _r, m in per if m)
                             or "(nothing measurable)",
                 "reason": "; ".join(r for _p, _v, r, _m in per if r)}
        if n_c and not n_r and not n_n:
            entry["verdict"] = "confirmed"
        elif n_r and not n_c and not n_n:
            entry["verdict"] = "refuted"
        elif n_c == 0 and n_r == 0:
            entry["verdict"] = "not-evaluable"
        else:
            entry["verdict"] = "partial"
        verdicts.append(entry)
    ctx.prediction_verdicts = verdicts
    ctx.prediction_coverage = coverage
    return verdicts


def _claim_text(rep, per):
    bits = []
    for p, _v, _r, _m in per:
        band = p["hi"] if p["op"] != "between" else f"{p['lo']}..{p['hi']}"
        bits.append(f"{p['prediction_id']}{p['clause'] or ''}: "
                    f"{p['quantity']} {p['op']} {band}{p['unit']}")
    return "; ".join(bits)


def _measured_text(p, reduced, bad, kind):
    label = f"{p['prediction_id']}{p['clause'] or ''}"
    if kind == "set":
        return f"{label}: {{{', '.join(reduced[0][1])}}}"
    if bad:
        worst = max(bad, key=lambda lv: abs(lv[1]))
        return (f"{label}: worst {worst[0]} = {worst[1]:.3f} over "
                f"{len(reduced)} value(s)")
    extreme = max(reduced, key=lambda lv: lv[1])
    return (f"{label}: worst {extreme[0]} = {extreme[1]:.3f} over "
            f"{len(reduced)} value(s)")


# ------------------------------------------------------------------ CLI

def repo_root_for(catalogue_path):
    return os.path.dirname(os.path.dirname(os.path.abspath(catalogue_path)))


def interpret(report_path, index_path, catalogue_path, predictions_path=None,
              subject_grain_path=None, fmt="tsv", check_utc=True):
    cat = load_catalogue(catalogue_path)
    check_links(cat, repo_root_for(catalogue_path))
    known = header_keys_from_source()
    report = ReportTsv(report_path, known)
    index = IndexTsv(index_path) if index_path else None
    subject_grain = (ReportTsv(subject_grain_path, known)
                     if subject_grain_path else None)
    predictions = None
    if predictions_path:
        predictions = load_predictions(predictions_path)
        if check_utc:
            check_stated_utc(predictions, index)
    ctx = Context(cat, report, index, predictions,
                  predictions_path or "(none)", subject_grain)
    if predictions is not None:
        evaluate_predictions(cat, report, index, predictions, ctx)
    results = run_rules(cat, report, index, ctx)
    if fmt == "tsv":
        return render_facts_tsv(results)
    stamp = [
        ("report", report_path),
        ("report_sha256", sha256_of(report_path)),
        ("index", index_path or "(none)"),
        ("index_sha256", sha256_of(index_path) if index_path else "(none)"),
        ("predictions", predictions_path or "(none)"),
        ("predictions_sha256",
         sha256_of(predictions_path) if predictions_path else "(none)"),
        ("catalogue", cat["catalogue_version"]),
        ("interpret", INTERPRET_VERSION),
        ("reporter", report.header.get("reporter", "?")),
        ("query", report.header.get("filters", "?")),
    ]
    return render_markdown(results, ctx, stamp)


def build_argparser():
    ap = argparse.ArgumentParser(
        prog="pcrecbench interpret",
        description="Read a committed report TSV and store/index.tsv and "
                    "emit the FIRED catalogue rules with their rows, numbers "
                    "and record ids, and the rules that did NOT fire with the "
                    "reason each did not (docs/design/interpreter_v1.md).")
    ap.add_argument("report", help="the report .tsv (never the .md)")
    ap.add_argument("--index", default="store/index.tsv",
                    help="the record index (default: store/index.tsv; the "
                         "golden check passes a frozen snapshot instead)")
    ap.add_argument("--predictions", help="a docs/dev/predictions/<slug>.tsv")
    ap.add_argument("--subject-grain", help="a subject-grain report TSV")
    ap.add_argument("--catalogue", default="catalogue/rules.toml")
    ap.add_argument("--format", choices=("tsv", "md"), default="tsv")
    ap.add_argument("--render", action="store_true",
                    help="alias for --format md")
    ap.add_argument("--out", help="write here instead of stdout")
    return ap


def main(argv=None):
    args = build_argparser().parse_args(argv)
    fmt = "md" if args.render else args.format
    try:
        text = interpret(args.report, args.index, args.catalogue,
                         args.predictions, args.subject_grain, fmt)
    except InterpretError as exc:
        print(f"interpret: {exc}", file=sys.stderr)
        return 2
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
