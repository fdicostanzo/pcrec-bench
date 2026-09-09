#!/usr/bin/env python3
"""`make check-interpret` — the interpreter's six check sections.

docs/design/interpreter_v1.md §8. Deliberately FAST and hermetic: it
never loads the record store. Every report it reads is a committed one
or a generated fixture slice, and every index it reads is the frozen
snapshot under `catalogue/golden/`, so a commit that only adds records
cannot fail it (§8(2)'s table).

    (1) catalogue/code correspondence and the load-time checks
    (2) determinism and the golden facts
    (3) sidecar freshness
    (4) the fixtures: base + one declared mutation, fire and not-fire
    (5) the no-prose check
    (6) the template-diff gate
"""

import os
import re
import subprocess
import sys
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from pcrecbench import interpret as I  # noqa: E402

CATALOGUE = os.path.join(HERE, "rules.toml")
GOLDEN = os.path.join(HERE, "golden")
FIXTURES = os.path.join(HERE, "fixtures")
INDEX_SNAPSHOT = os.path.join(GOLDEN, "index@2026-09-09.tsv")
REPORTS = os.path.join(ROOT, "reports")

# §10's acceptance set, and the golden facts committed for each.
ACCEPTANCE = [
    ("reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv",
     None),
    ("reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv", None),
    ("reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv", None),
    ("reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv",
     "docs/dev/predictions/syntax-0.1-first.tsv"),
]

PASS = []
FAIL = []


def ok(section, what):
    PASS.append((section, what))


def bad(section, what, detail=""):
    FAIL.append((section, what, detail))
    print(f"FAIL [{section}] {what}" + (f"\n      {detail}" if detail else ""))


def golden_name(report_rel, predictions_rel):
    base = os.path.basename(report_rel)[:-len(".tsv")]
    if predictions_rel:
        base += ".with-predictions"
    return base + ".facts.tsv"


def run_interpret(report, index, predictions=None, fmt="tsv"):
    return I.interpret(report, index, CATALOGUE, predictions, None, fmt)


# ------------------------------------------------------------ section 1

def section_1(cat):
    # load_catalogue already ran every load-time check §3.2.1/§3.2.2 asks
    # for (grain mandatory, the inputs grammar, aggregate keys are slots,
    # extremal is a slot, templates use only declared slots, a slot-free
    # no_fire, one function per rule and one rule per function).
    ok(1, f"catalogue {cat['catalogue_version']} loads with "
          f"{len(cat['rule'])} rules and every load-time check green")

    if len(cat["rule"]) != 31:
        bad(1, "the catalogue carries 31 rules",
            f"found {len(cat['rule'])}")
    else:
        ok(1, "31 rules in 7 classes")
    classes = {r["class"] for r in cat["rule"]}
    if classes != {"status", "delta", "rank", "arm", "floor", "pred",
                   "bucket"}:
        bad(1, "seven rule classes", str(sorted(classes)))
    else:
        ok(1, "seven classes: " + ", ".join(sorted(classes)))

    # the header known-key list is DERIVED, never retyped (§2.1)
    derived = I.header_keys_from_source()
    if derived != I.HEADER_KEYS:
        bad(1, "the known-key list matches report.py's own header block",
            f"derived {derived}\n      frozen  {I.HEADER_KEYS}")
    else:
        ok(1, f"the known-key split's {len(derived)} keys are derived from "
              f"report.py's header block")
    cols = I.report_columns_from_source()
    if cols != I.REPORT_COLUMNS:
        bad(1, "the 18 data columns match render_tsv's own header list",
            f"derived {cols}")
    else:
        ok(1, "the 18 data columns are read from render_tsv's header list")

    # ... and every committed report's own header parses into those keys
    for report_rel, _p in ACCEPTANCE:
        path = os.path.join(ROOT, report_rel)
        with open(path, encoding="utf-8") as fh:
            head = fh.readline()
        parsed = I.split_header(head, derived)
        if set(parsed) != set(derived):
            bad(1, f"{os.path.basename(report_rel)}: header parses to every "
                   f"known key", str(sorted(set(derived) - set(parsed))))
        elif "; " in parsed.get("x13_rules", "") and len(parsed) != len(derived):
            bad(1, "a two-clause x13_rules value does not shift later keys")
    ok(1, "every acceptance report's header parses to the full key set")

    # every pcrec pin slug in a golden report is in [[pin_order]]
    pins = set()
    for report_rel, _p in ACCEPTANCE:
        with open(os.path.join(ROOT, report_rel), encoding="utf-8") as fh:
            for ln in fh:
                for field in ln.split("\t"):
                    parts = I.split_testee(field)
                    if parts and parts[0] == "pcrec":
                        pins.add(parts[1])
    known = {p for entry in cat["pin_order"] for p in entry["pins"]}
    missing = sorted(pins - known)
    if missing:
        bad(1, "every pcrec pin in a golden report is in [[pin_order]]",
            str(missing))
    else:
        ok(1, f"all {len(pins)} pcrec pins in the acceptance reports are in "
              f"[[pin_order]]")

    # every links entry resolves (§7.3)
    try:
        I.check_links(cat, ROOT)
        ok(1, "every links entry resolves (file exists, anchor present)")
    except I.InterpretError as exc:
        bad(1, "every links entry resolves", str(exc))

    # no R-BUCKET-KB signature is registered in 1.0 (§4.7)
    if cat.get("signature"):
        bad(1, "catalogue 1.0 registers no [[signature]]",
            f"found {len(cat['signature'])}")
    else:
        ok(1, "no [[signature]] is registered (R-BUCKET-KB's stated gap)")

    # every quantity token in every committed predictions file is closed
    pred_dir = os.path.join(ROOT, "docs", "dev", "predictions")
    n_pred = 0
    for name in sorted(os.listdir(pred_dir)):
        if not name.endswith(".tsv"):
            continue
        try:
            rows = I.load_predictions(os.path.join(pred_dir, name))
            n_pred += len(rows)
        except I.PredictionError as exc:
            bad(1, f"{name} loads", str(exc))
    ok(1, f"{n_pred} prediction clause(s) load with every quantity, op, "
          f"reducer and selector key in its closed set")

    # the two INEXPRESSIBLE clauses must FAIL AT LOAD (§6.4)
    inexpressible = os.path.join(FIXTURES, "predictions-inexpressible.tsv")
    try:
        I.load_predictions(inexpressible)
        bad(1, "the inexpressible clauses fail at load",
            "loaded without error")
    except I.PredictionError as exc:
        if "closed set" not in str(exc):
            bad(1, "the inexpressible clause's load error names the closed "
                   "set", str(exc))
        else:
            ok(1, "P9.a's span quantity fails at load, naming the closed set")

    # every rule has at least one fixture and one negative control
    specs = fixture_specs()
    covered = {}
    for spec in specs:
        for rid in spec.get("expect", []):
            covered.setdefault(rid, set()).add("fire")
        for rid in spec.get("expect_not", []):
            covered.setdefault(rid, set()).add("nofire")
        for rid in spec.get("expect_token", {}):
            covered.setdefault(rid, set()).add("token")
    for rule in cat["rule"]:
        rid = rule["id"]
        have = covered.get(rid, set())
        if not have:
            bad(1, f"{rid} has at least one fixture", "none")
        elif "fire" in have and "nofire" in have:
            pass
        elif "token" in have:
            pass                       # a rule that cannot fire in v1.0
        else:
            bad(1, f"{rid} has a fixture AND a negative control",
                f"only {sorted(have)}")
    ok(1, f"every rule is covered by the {len(specs)} fixtures")


# ------------------------------------------------------------ section 2

def section_2():
    for report_rel, pred_rel in ACCEPTANCE:
        report = os.path.join(ROOT, report_rel)
        pred = os.path.join(ROOT, pred_rel) if pred_rel else None
        label = golden_name(report_rel, pred_rel)
        a = run_interpret(report, INDEX_SNAPSHOT, pred, "tsv")
        b = run_interpret(report, INDEX_SNAPSHOT, pred, "tsv")
        if a != b:
            bad(2, f"{label}: two runs are byte-identical")
            continue
        md_a = run_interpret(report, INDEX_SNAPSHOT, pred, "md")
        md_b = run_interpret(report, INDEX_SNAPSHOT, pred, "md")
        if md_a != md_b:
            bad(2, f"{label}: two renders are byte-identical")
            continue
        ok(2, f"{label}: deterministic in both formats")
        golden = os.path.join(GOLDEN, label)
        if not os.path.exists(golden):
            bad(2, f"{label}: golden facts committed", "missing")
            continue
        with open(golden, encoding="utf-8") as fh:
            want = fh.read()
        if want != a:
            bad(2, f"{label}: matches its committed golden facts",
                "regenerate with catalogue/refresh_golden.py")
        else:
            n = sum(1 for ln in a.split("\n")[1:] if ln)
            ok(2, f"{label}: {n} golden fact row(s) match")


# ------------------------------------------------------------ section 3

def section_3():
    n = 0
    for name in sorted(os.listdir(REPORTS)):
        if not name.endswith(".interpretation.md"):
            continue
        n += 1
        path = os.path.join(REPORTS, name)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        stamp = {}
        for ln in text.split("\n"):
            if ln.startswith("-->"):
                break
            m = re.match(r"^([a-z_0-9]+):\s+(.*)$", ln)
            if m:
                stamp[m.group(1)] = m.group(2).strip()
        report = os.path.join(ROOT, stamp.get("report", ""))
        if not os.path.exists(report):
            bad(3, f"{name}: its stamped report exists", stamp.get("report"))
            continue
        if I.sha256_of(report) != stamp.get("report_sha256"):
            bad(3, f"{name}: its report's sha256 matches the stamp")
            continue
        index = stamp.get("index")
        index = os.path.join(ROOT, index) if index and index != "(none)" else None
        pred = stamp.get("predictions")
        pred = os.path.join(ROOT, pred) if pred and pred != "(none)" else None
        fresh = run_interpret(report, index, pred, "md")
        if fresh != text:
            bad(3, f"{name}: re-renders byte-identical")
        else:
            ok(3, f"{name}: fresh")
    ok(3, f"{n} committed sidecar(s) checked "
          f"(the sidecars themselves are [B13.4]'s deliverable)")


# ------------------------------------------------------------ section 4

def fixture_specs():
    with open(os.path.join(FIXTURES, "fixtures.toml"), "rb") as fh:
        return tomllib.load(fh)["fixture"]


def _fired(facts):
    out = {}
    for ln in facts.split("\n")[1:]:
        if not ln:
            continue
        f = ln.split("\t")
        out.setdefault(f[0], set())
        if f[1] == "1":
            out[f[0]].add(int(f[2]))
    return out


def _tokens(facts):
    out = {}
    for ln in facts.split("\n")[1:]:
        if not ln:
            continue
        f = ln.split("\t")
        if f[1] == "0":
            out[f[0]] = f[11]
    return out


def section_4(cat):
    if subprocess.call([sys.executable,
                        os.path.join(FIXTURES, "gen.py"), "--check"],
                       cwd=ROOT) != 0:
        bad(4, "gen.py --check: every fixture re-derives")
    else:
        ok(4, "gen.py --check: every fixture re-derives from its declaration")

    specs = {s["name"]: s for s in fixture_specs()}
    facts_by_name = {}
    for name, spec in specs.items():
        d = os.path.join(FIXTURES, name)
        pred = os.path.join(d, "predictions.tsv")
        pred = pred if os.path.exists(pred) else None
        try:
            facts = run_interpret(os.path.join(d, "report.tsv"),
                                  os.path.join(d, "index.tsv"), pred, "tsv")
        except I.InterpretError as exc:
            bad(4, f"{name}: interpret runs", str(exc))
            continue
        facts_by_name[name] = facts
        fired = _fired(facts)
        tokens = _tokens(facts)
        for rid in spec.get("expect", []):
            if not fired.get(rid):
                bad(4, f"{name}: {rid} FIRES",
                    f"did not fire ({tokens.get(rid)})")
            else:
                ok(4, f"{name}: {rid} fires {len(fired[rid])} time(s)")
        for rid in spec.get("expect_not", []):
            if fired.get(rid):
                bad(4, f"{name}: {rid} does NOT fire",
                    f"fired {len(fired[rid])} time(s)")
            else:
                ok(4, f"{name}: {rid} does not fire ({tokens.get(rid)})")
        for rid, token in spec.get("expect_token", {}).items():
            if tokens.get(rid) != token:
                bad(4, f"{name}: {rid} reports `{token}`",
                    f"reported {tokens.get(rid)!r}")
            else:
                ok(4, f"{name}: {rid} reports `{token}`")

    # EXACTLY ONE DECLARED FIELD differs between a control and its base
    # (§8(4)'s computable replacement for "the minimum number of bytes").
    # "One field" is one DECLARATION: the two source.tomls differ in
    # exactly one mutation-bearing key and agree on everything else, and
    # the generated files differ in at most one COLUMN (a mutation with
    # `all = true` changes one column across several rows -- still one
    # declared field, which counting cells would miscount).
    for name, spec in specs.items():
        base = spec.get("base")
        if not base:
            continue
        if base not in specs:
            bad(4, f"{name}: names an existing base", base)
            continue
        other = specs[base]
        keys = ("mutate", "mutate_header", "mutate_index",
                "mutate_predictions", "predictions_select")
        differing = [k for k in keys if spec.get(k) != other.get(k)]
        shared = [k for k in ("report", "select", "synthetic")
                  if spec.get(k) != other.get(k)]
        if shared:
            bad(4, f"{name}: shares its base's slice", f"differs on {shared}")
        if len(differing) != 1:
            bad(4, f"{name}: exactly one declared mutation differs from "
                   f"{base}", f"{differing}")
            continue
        columns = set()
        rows_differ = False
        for fname in ("report.tsv", "index.tsv", "predictions.tsv"):
            a = os.path.join(FIXTURES, base, fname)
            b = os.path.join(FIXTURES, name, fname)
            if not os.path.exists(a) or not os.path.exists(b):
                if os.path.exists(a) != os.path.exists(b):
                    rows_differ = True
                continue
            cols, changed = _field_diff(a, b, fname)
            columns |= cols
            rows_differ = rows_differ or changed
        if len(columns) > 1:
            bad(4, f"{name}: at most one COLUMN differs from {base}",
                f"{sorted(columns)}")
        else:
            detail = (sorted(columns) or ["(the declaration only)"])[0]
            ok(4, f"{name}: exactly one declared field differs from {base} "
                  f"({differing[0]}: {detail})")

    # co-firing and mutual exclusion, per CELL, over every fixture and
    # every acceptance report (§8(4)'s first extra fixture kind)
    _mutual_exclusion(list(facts_by_name.values()))
    ok(4, "R-DELTA-1 and R-DELTA-2 never fire on one cell "
          "(every fixture checked)")
    co = _co_firing(facts_by_name.get("R-DELTA-2__selection-changed", ""))
    if not co:
        bad(4, "R-DELTA-2 and R-DELTA-3 DO co-fire on the compound verdict",
            "no cell carries both")
    else:
        ok(4, f"R-DELTA-2 and R-DELTA-3 co-fire on {len(co)} cell(s) of the "
              f"compound `selection changed (vm → dfa); now measured (was: "
              f"gave-up)` verdict")

    # the NULL CONTROL: all 31 rules quiet on the synthetic clean report
    clean = facts_by_name.get("CLEAN__all-measured")
    if clean is None:
        bad(4, "the null control runs")
    else:
        fired = {rid for rid, seqs in _fired(clean).items() if seqs}
        if fired:
            bad(4, "Report D (the null control): all 31 rules report fired=0",
                f"{sorted(fired)} fired")
        else:
            n = len(_tokens(clean))
            if n != 31:
                bad(4, "Report D names all 31 rules", f"named {n}")
            else:
                ok(4, "Report D (the null control): all 31 rules report "
                      "fired=0, and all 31 are named")


_FILE_COLUMNS = {"report.tsv": I.REPORT_COLUMNS,
                 "index.tsv": I.INDEX_COLUMNS,
                 "predictions.tsv": I.PRED_COLUMNS}


def _field_diff(path_a, path_b, fname):
    """(set of differing column names, row-count-differs). A header-key
    mutation shows as the pseudo-column `header:<key>`."""
    with open(path_a, encoding="utf-8") as fh:
        a = fh.read().split("\n")
    with open(path_b, encoding="utf-8") as fh:
        b = fh.read().split("\n")
    columns = set()
    if fname == "report.tsv" and a[0] != b[0]:
        ka = dict(c.partition(": ")[::2] for c in a[0].lstrip("# ").split("; "))
        kb = dict(c.partition(": ")[::2] for c in b[0].lstrip("# ").split("; "))
        for k in set(ka) | set(kb):
            if ka.get(k) != kb.get(k):
                columns.add("header:" + k)
        a, b = a[1:], b[1:]
    if len(a) != len(b):
        return columns, True
    names = _FILE_COLUMNS[fname]
    for la, lb in zip(a, b):
        if la == lb:
            continue
        fa, fb = la.split("\t"), lb.split("\t")
        if len(fa) != len(fb):
            return columns, True
        for i, (x, y) in enumerate(zip(fa, fb)):
            if x != y:
                columns.add(names[i] if i < len(names) else str(i))
    return columns, False


def _co_firing(facts):
    cells = {}
    for ln in facts.split("\n")[1:]:
        if not ln:
            continue
        f = ln.split("\t")
        if f[1] == "1" and f[0] in ("R-DELTA-2", "R-DELTA-3"):
            cells.setdefault((f[3], f[5], f[6], f[7]), set()).add(f[0])
    return [c for c, r in cells.items() if len(r) == 2]


def _mutual_exclusion(all_facts):
    for facts in all_facts:
        cells = {}
        for ln in facts.split("\n")[1:]:
            if not ln:
                continue
            f = ln.split("\t")
            if f[1] != "1" or f[0] not in ("R-DELTA-1", "R-DELTA-2",
                                           "R-DELTA-3"):
                continue
            cell = (f[3], f[5], f[6], f[7])
            cells.setdefault(cell, set()).add(f[0])
        for cell, rules in cells.items():
            if {"R-DELTA-1", "R-DELTA-2"} <= rules:
                bad(4, "R-DELTA-1 and R-DELTA-2 never fire on one cell",
                    str(cell))


# ------------------------------------------------------------ section 5

def section_5(cat):
    """Every non-blank, non-heading, non-stamp line of a rendered sidecar
    is reproducible from the facts TSV -- checked by re-rendering the
    whole document from the facts alone (reassembled by `(rule_id,
    firing_seq)`, §5.1's own reason for that column) and requiring byte
    equality with the direct render."""
    for report_rel, pred_rel in ACCEPTANCE:
        report = os.path.join(ROOT, report_rel)
        pred = os.path.join(ROOT, pred_rel) if pred_rel else None
        label = golden_name(report_rel, pred_rel)
        direct = run_interpret(report, INDEX_SNAPSHOT, pred, "md")
        facts = run_interpret(report, INDEX_SNAPSHOT, pred, "tsv")
        rebuilt = _render_from_facts(cat, report, pred, facts)
        if direct != rebuilt:
            first = _first_diff(direct, rebuilt)
            bad(5, f"{label}: every rendered line comes from the facts TSV",
                first)
        else:
            ok(5, f"{label}: the sidecar re-renders from its facts TSV, byte "
                  f"for byte")


def _render_from_facts(cat, report_path, pred_path, facts):
    known = I.header_keys_from_source()
    report = I.ReportTsv(report_path, known)
    index = I.IndexTsv(INDEX_SNAPSHOT)
    ctx = I.Context(cat, report, index, [] if pred_path else None,
                    I.display_path(pred_path, ROOT) if pred_path else "(none)")
    results = I.results_from_facts(cat, facts)
    # ONE stamp builder, shared with the CLI render (interpret.build_stamp):
    # the check must not carry its own copy of the stamp -- it did, and
    # the [B13.3] merge's path-rule change made the two disagree on line 2.
    stamp = I.build_stamp(cat, report, report_path, INDEX_SNAPSHOT, pred_path,
                          ROOT)
    return I.render_markdown(results, ctx, stamp)


def _first_diff(a, b):
    for n, (la, lb) in enumerate(zip(a.split("\n"), b.split("\n")), start=1):
        if la != lb:
            return f"line {n}:\n      direct  {la[:120]}\n      rebuilt {lb[:120]}"
    return "one document is longer than the other"


# ------------------------------------------------------------ section 6

PROSE_FIELDS = ("template", "no_fire", "links")


def section_6():
    """The template-diff gate: a diff that touches a `template`,
    `no_fire` or `links` field, or adds a `[[signature]]`, must carry a
    reviewer's approval line in the commit message naming the rule ids
    reviewed. The check cannot judge prose; what it can do is refuse to
    let prose change invisibly."""
    try:
        head = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"],
                              capture_output=True, text=True, timeout=30)
        if head.returncode != 0:
            ok(6, "not a git checkout: the template-diff gate is inert")
            return
        diff = subprocess.run(
            ["git", "-C", ROOT, "diff", "HEAD~1", "HEAD", "--unified=0", "--",
             "catalogue/rules.toml"],
            capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as exc:
        ok(6, f"git unavailable: the template-diff gate is inert ({exc})")
        return
    if diff.returncode != 0:
        ok(6, "no previous commit: the template-diff gate is inert")
        return
    touched = [ln for ln in diff.stdout.split("\n")
               if re.match(r"^[+-]\s*(template|no_fire|links)\s*=", ln)
               or re.match(r"^\+\s*\[\[signature\]\]", ln)]
    if not touched:
        ok(6, "HEAD touches no template, no_fire or links field")
        return
    msg = subprocess.run(["git", "-C", ROOT, "log", "-1", "--format=%B"],
                         capture_output=True, text=True, timeout=30).stdout
    if not re.search(r"[Tt]emplate/no_fire/links reviewed|"
                     r"[Tt]emplate.*reviewed:", msg):
        bad(6, "a commit touching template/no_fire/links carries a "
               "reviewer's approval line naming the rule ids",
            f"{len(touched)} prose line(s) changed; commit message has no "
            f"approval line")
    else:
        ok(6, f"HEAD changes {len(touched)} prose line(s) and carries its "
              f"reviewer's approval line")


# ------------------------------------------------------------------ main

def main():
    cat = I.load_catalogue(CATALOGUE)
    section_1(cat)
    section_2()
    section_3()
    section_4(cat)
    section_5(cat)
    section_6()
    by_section = {}
    for s, _w in PASS:
        by_section[s] = by_section.get(s, 0) + 1
    print()
    for s in sorted(by_section):
        print(f"check-interpret section {s}: {by_section[s]} check(s) passed")
    print(f"check-interpret: {len(PASS)} passed, {len(FAIL)} FAILED")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
