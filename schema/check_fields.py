#!/usr/bin/env python3
"""check_fields.py -- the design note and the JSON Schema must agree FIELD FOR
FIELD, and a claim like that is worth nothing while a human is the only thing
checking it (pcrec's check-design lesson: a check with no failing case proves
nothing, and a claim with no check is not a check at all).

This walks schema/record.schema.json into a set of dotted field paths per line
kind, walks docs/design/record_schema.md's field tables into a second set, and
diffs them. The two sources are genuinely independent -- one is hand-written
JSON, the other is a hand-written markdown table -- so a disagreement means one
of them drifted, which is exactly what this exists to catch.

Usage:
    python3 schema/check_fields.py            # diff note vs schema, exit 0/1
    python3 schema/check_fields.py --dump     # print the schema's paths only

Path spelling: `a.b` for a nested object member, `a[].b` for a member of an
array's element objects. The kind prefix (`setup`, `match`, `compile`) is the
table each path lives in, not part of the path.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCHEMA = os.path.join(HERE, "record.schema.json")
NOTE = os.path.join(ROOT, "docs", "design", "record_schema.md")

KINDS = {"setup": "#/$defs/setup",
         "match": "#/$defs/match_row",
         "compile": "#/$defs/compile_row"}


def resolve(schema, ref):
    node = schema
    for part in ref.lstrip("#/").split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        node = node[part]
    return node


def walk(schema, node, prefix, out, seen):
    """Collect dotted paths for every named property reachable from `node`."""
    if not isinstance(node, dict):
        return
    if "$ref" in node:
        ref = node["$ref"]
        # A $ref cycle would loop forever; the schema has none, but a future
        # edit could introduce one and an infinite loop is a bad way to learn.
        key = (ref, prefix)
        if key in seen:
            return
        seen = seen | {key}
        walk(schema, resolve(schema, ref), prefix, out, seen)
        return
    for combinator in ("oneOf", "anyOf", "allOf"):
        for sub in node.get(combinator, []):
            # `if`/`then` branches inside allOf constrain fields already named
            # by `properties`; they introduce no new NAMES, so only the plain
            # subschemas are walked.
            walk(schema, sub, prefix, out, seen)
    props = node.get("properties")
    if isinstance(props, dict):
        for name, sub in props.items():
            path = f"{prefix}.{name}" if prefix else name
            out.add(path)
            walk(schema, sub, path, out, seen)
    items = node.get("items")
    if isinstance(items, dict):
        walk(schema, items, prefix + "[]", out, seen)
    # `additionalProperties` with a schema means an OPEN map (engine_metadata,
    # run.env, the per-testee declaration): its members are data, not schema
    # fields, so its keys are not paths. Its VALUE shape is documented in the
    # note's prose, not as a field row -- deliberate, and the reason those
    # three maps have no `foo.<name>...` rows.


def schema_paths():
    schema = json.load(open(SCHEMA, encoding="utf-8"))
    result = {}
    for kind, ref in KINDS.items():
        out = set()
        walk(schema, resolve(schema, ref), "", out, frozenset())
        result[kind] = out
    return result


TABLE_RE = re.compile(r"^\|\s*`([^`]+)`\s*\|")
HEADING_RE = re.compile(r"^###\s+FIELD TABLE:\s*(setup|match|compile)\b")


def note_paths():
    result = {k: set() for k in KINDS}
    current = None
    with open(NOTE, encoding="utf-8") as fh:
        for line in fh:
            m = HEADING_RE.match(line)
            if m:
                current = m.group(1)
                continue
            if line.startswith("#") and not line.startswith("####"):
                current = None
                continue
            if current is None:
                continue
            m = TABLE_RE.match(line)
            if m:
                result[current].add(m.group(1))
    return result


def main():
    if "--dump" in sys.argv:
        for kind, paths in schema_paths().items():
            print(f"=== {kind} ({len(paths)}) ===")
            for p in sorted(paths):
                print(p)
        return 0
    if not os.path.exists(NOTE):
        print(f"check_fields: design note not found: {NOTE}", file=sys.stderr)
        return 1
    sp, np_ = schema_paths(), note_paths()
    bad = 0
    for kind in sorted(KINDS):
        only_schema = sorted(sp[kind] - np_[kind])
        only_note = sorted(np_[kind] - sp[kind])
        for p in only_schema:
            print(f"check_fields: {kind}: `{p}` is in the SCHEMA but has no row "
                  f"in the note's FIELD TABLE: {kind}", file=sys.stderr)
            bad += 1
        for p in only_note:
            print(f"check_fields: {kind}: `{p}` has a row in the note's FIELD "
                  f"TABLE: {kind} but is not in the SCHEMA", file=sys.stderr)
            bad += 1
        if not only_schema and not only_note:
            print(f"check_fields: {kind}: {len(sp[kind])} fields agree")
    if bad:
        print(f"check_fields: FAIL -- {bad} disagreement(s)", file=sys.stderr)
        return 1
    print("check_fields: OK -- the note and the schema agree field for field")
    return 0


if __name__ == "__main__":
    sys.exit(main())
