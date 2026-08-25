#!/usr/bin/env python3
"""check_rules.py -- every cross-line rule in the design note's §9 table must
have a positive control in schema/examples/bad/, and every control there must
name a rule that exists.

The note has claimed since draft 1 that "each has at least one positive control
in `schema/examples/bad/`". At v1.1 that claim was found to be FALSE for five
of the rules that existed at that moment (X5, X7, X8, X12, X16), which had
never been seen to fire. The claim survived a merge and a critic panel because
a human was the only thing checking it -- which is pcrec's check-design lesson
exactly, one level up: a check with no failing case proves nothing, and a CLAIM
that every check has a failing case is itself a check, so it needs one too.

This is that check. Its own failing case: delete any file from
`examples/bad/` and `make check-schema` fails.

    python3 schema/check_rules.py         # exit 0/1
    python3 schema/check_rules.py --dump  # print the rule -> controls map

Deliberately NOT folded into check_fields.py: that one diffs the note's FIELD
tables against the JSON Schema. This diffs the note's RULE table against a
directory listing. Two independent pairs, two independent gates -- one file
that fails for either reason tells you less than two that each name their own.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NOTE = os.path.join(ROOT, "docs", "design", "record_schema.md")
BAD = os.path.join(HERE, "examples", "bad")

# `make check-schema` derives the rule a control must fire from the file name's
# leading token, uppercased (Makefile, check-schema). This must agree with it.
CONTROL_RE = re.compile(r"^([a-z0-9]+)-.*\.jsonl$")
RULE_ROW_RE = re.compile(r"^\|\s*(X\d+)\s*\|")
RULE_TABLE_HEADING_RE = re.compile(r"^##\s+9\.\s")

# `schema` is not a rule id in the note's table; it is the JSON Schema itself,
# which every line is validated against and which therefore needs no row.
NON_RULE_TOKENS = {"schema"}


def note_rules():
    """The rule ids of §9's table, in the order the note lists them."""
    rules, in_section = [], False
    with open(NOTE, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("## "):
                in_section = bool(RULE_TABLE_HEADING_RE.match(line))
                continue
            if not in_section:
                continue
            m = RULE_ROW_RE.match(line)
            if m and m.group(1) not in rules:
                rules.append(m.group(1))
    return rules


def controls():
    """token -> [file names], from the directory itself."""
    out = {}
    for name in sorted(os.listdir(BAD)):
        if not name.endswith(".jsonl"):
            continue
        m = CONTROL_RE.match(name)
        if not m:
            out.setdefault("(unparseable)", []).append(name)
            continue
        out.setdefault(m.group(1).upper(), []).append(name)
    return out


def main():
    rules = note_rules()
    have = controls()
    if "--dump" in sys.argv:
        for rule in rules:
            print(f"{rule:5s} {', '.join(have.get(rule, [])) or '(none)'}")
        for tok in sorted(set(have) - set(rules)):
            print(f"{tok:5s} {', '.join(have[tok])}")
        return 0

    if not rules:
        print("check_rules: no rule rows found in the note's §9 table -- the "
              "table moved or its shape changed; this gate is now blind",
              file=sys.stderr)
        return 1

    bad = 0
    for rule in rules:
        if rule not in have:
            print(f"check_rules: {rule} is a rule in the note's §9 table but "
                  f"NO file in schema/examples/bad/ is named for it; a rule "
                  f"that has never been seen to fire is not known to be a "
                  f"rule", file=sys.stderr)
            bad += 1
    for tok in sorted(set(have) - set(rules)):
        if tok.lower() in NON_RULE_TOKENS:
            continue
        names = ", ".join(have[tok])
        print(f"check_rules: {names} names rule {tok}, which is not in the "
              f"note's §9 table", file=sys.stderr)
        bad += 1
    if bad:
        print(f"check_rules: FAIL -- {bad} rule(s) without a control, or "
              f"control(s) without a rule", file=sys.stderr)
        return 1
    n = sum(len(v) for v in have.values())
    print(f"check_rules: OK -- {len(rules)} rules, {n} controls, every rule "
          f"has at least one")
    return 0


if __name__ == "__main__":
    sys.exit(main())
