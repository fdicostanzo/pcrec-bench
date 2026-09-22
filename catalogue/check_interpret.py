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
import tempfile
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


def run_interpret(report, index, predictions=None, fmt="tsv",
                  subject_grain=None):
    return I.interpret(report, index, CATALOGUE, predictions, subject_grain,
                       fmt)


def _pred_clause_id(line):
    """`prediction_id` + `clause` (e.g. `P2` + `.a` = `P2.a`) from one raw
    TSV data line -- `docs/dev/predictions/CLAUDE.md`'s own compound-id
    convention, read without going through `load_predictions` (which is
    exactly the function under test here)."""
    f = line.split("\t")
    return f[0] + (f[1] if len(f) > 1 else "")


def _tmp_predictions_file(path, keep):
    """A scratch temp predictions file: `path`'s own header plus only the
    rows whose `_pred_clause_id` is in `keep`. Caller unlinks it. Lets a
    fixture file carry several clauses (readable in one place, per the
    `predictions-inexpressible.tsv` precedent) while a check isolates one
    at a time -- `load_predictions` stops at its FIRST bad row, so a
    fixture with two independently-sabotaged rows needs this to prove
    each one's OWN reason rather than only ever seeing the first."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    header = lines[0]
    body = [ln for ln in lines[1:] if ln.strip() and _pred_clause_id(ln) in keep]
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".tsv", delete=False, encoding="utf-8")
    tmp.write(header + "\n" + "\n".join(body) + "\n")
    tmp.close()
    return tmp.name


def _load_predictions_with_named_exceptions(path, allowed, seen_allowed, name):
    """The one NAMED historical exception's own control, both directions:
    every clause in `path` OTHER than `allowed` (a set of clause ids)
    must load clean with the exception rows removed -- proving the
    exception does not silently widen to hide some OTHER, unrelated
    defect in this file -- and each allowed clause, loaded IN ISOLATION
    (its own header plus that one row), must fail with Q6 (i)'s own
    reason (never load clean, and never fail for a DIFFERENT reason) --
    adding `cid` to `seen_allowed` only when it does. Returns the clean
    row count. Never touches the committed file itself: every load runs
    against a scratch temp copy."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    header = lines[0]
    body = [ln for ln in lines[1:] if ln.strip()]

    def _tmp_load(text):
        tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".tsv", delete=False, encoding="utf-8")
        try:
            tmp.write(text)
            tmp.close()
            return I.load_predictions(tmp.name)
        finally:
            os.unlink(tmp.name)

    clean_lines = [ln for ln in body if _pred_clause_id(ln) not in allowed]
    rows = []
    try:
        rows = _tmp_load(header + "\n" + "\n".join(clean_lines) + "\n")
    except I.PredictionError as exc:
        bad(1, f"{name}: every clause OTHER than the named exception "
               f"loads clean", str(exc))

    for ln in body:
        cid = _pred_clause_id(ln)
        if cid not in allowed:
            continue
        try:
            _tmp_load(header + "\n" + ln + "\n")
            bad(1, f"{name}: {cid} fails with Q6 (i)'s reason",
                "loaded without error -- the named exception no longer "
                "reproduces; narrow or remove it")
        except I.PredictionError as exc:
            if "Q6 (i)" not in str(exc):
                bad(1, f"{name}: {cid} fails with Q6 (i)'s reason", str(exc))
            else:
                seen_allowed.add(cid)
    return len(rows)


# ------------------------------------------------------------ section 1

def section_1(cat):
    # load_catalogue already ran every load-time check §3.2.1/§3.2.2 asks
    # for (grain mandatory, the inputs grammar, aggregate keys are slots,
    # extremal is a slot, templates use only declared slots, a slot-free
    # no_fire, one function per rule and one rule per function).
    ok(1, f"catalogue {cat['catalogue_version']} loads with "
          f"{len(cat['rule'])} rules and every load-time check green")

    if len(cat["rule"]) != 33:
        bad(1, "the catalogue carries 33 rules",
            f"found {len(cat['rule'])}")
    else:
        ok(1, "33 rules in 7 classes")
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

    # every quantity token in every committed predictions file is closed --
    # EXCEPT one NAMED, historical exception (below): `load_predictions`
    # grew a NEW load-time rule at Q6 (i) (interpret_subject_grain_v1.md
    # §6 Q6, RATIFIED: "both, under Frank's stated general posture 'fail
    # loudly generally'") that correctly catches a genuine, ALREADY-
    # DIAGNOSED authoring defect in ONE already-committed file --
    # `capability-0.1-first.tsv`'s P2.a/P2.b, Cause B in the design note's
    # own §1.2 ("regime_or_na=n/a against the compile section's EMPTY
    # string... fixed by no grain change"). `docs/dev/predictions/
    # CLAUDE.md`'s own entry for this file states the project's rule
    # explicitly: "Predictions are stated-PRE-RUN artifacts... and this
    # format defines no revision mechanism for an already-scored file" --
    # this file is NOT edited to satisfy the new check, the same way its
    # already-documented recommended fix (b42predhyg's) was deliberately
    # NOT applied to it. The exception is scoped to EXACTLY these two
    # clause ids in EXACTLY this file, quoting the reason Q6 (i) gives, so
    # a NEW predictions file with the same defect still fails loudly here
    # -- the check's whole point.
    _KNOWN_HISTORICAL_LOAD_DEFECTS = {
        "capability-0.1-first.tsv": {"P2.a", "P2.b"},
    }
    pred_dir = os.path.join(ROOT, "docs", "dev", "predictions")
    n_pred = 0
    for name in sorted(os.listdir(pred_dir)):
        if not name.endswith(".tsv"):
            continue
        allowed = _KNOWN_HISTORICAL_LOAD_DEFECTS.get(name, set())
        path = os.path.join(pred_dir, name)
        if not allowed:
            try:
                rows = I.load_predictions(path)
                n_pred += len(rows)
            except I.PredictionError as exc:
                bad(1, f"{name} loads", str(exc))
            continue
        # A file with a named exception: every clause OTHER than the
        # allowed ones must still load clean, and the allowed ones must
        # fail with EXACTLY Q6 (i)'s own reason (a control against the
        # exception silently widening to cover a future, different bug).
        seen_allowed = set()
        n_pred += _load_predictions_with_named_exceptions(
            path, allowed, seen_allowed, name)
        missing = allowed - seen_allowed
        if missing:
            bad(1, f"{name}: the named historical exception(s) fired",
                f"expected {sorted(allowed)}, saw {sorted(seen_allowed)} "
                f"fail with Q6 (i)'s reason")
    ok(1, f"{n_pred} prediction clause(s) load with every quantity, op, "
          f"reducer and selector key in its closed set (the one NAMED "
          f"historical exception above excepted, and checked to fail for "
          f"exactly its own stated reason)")

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

    # F27/r7code-1 (docs/design/predicate_audit_v1.md, ratified
    # 2026-09-19): check_stated_utc is RE-ANCHORED to the report's own
    # included (subbench, version, testee_id, machine_id) population.
    # Fixture pair, both sides -- same precedent as the inexpressible
    # check just above (a dedicated predictions file, checked directly,
    # since a load-time raise is not a rendered firing `expect`/
    # `expect_not` can assert on).
    syntax_report_path = os.path.join(
        ROOT, "reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv")
    syntax_report = I.ReportTsv(syntax_report_path, I.header_keys_from_source())
    syntax_index = I.IndexTsv(INDEX_SNAPSHOT)
    try:
        preds = I.load_predictions(os.path.join(FIXTURES,
                                                 "predictions-utc-before.tsv"))
        I.check_stated_utc(preds, syntax_index, syntax_report)
        ok(1, "a stated_utc legitimately BEFORE this report's own "
              "population passes check_stated_utc (§6.5, r7code-1)")
    except I.InterpretError as exc:
        bad(1, "a stated_utc before the report's own population passes",
            str(exc))
    try:
        preds = I.load_predictions(os.path.join(FIXTURES,
                                                 "predictions-utc-after.tsv"))
        I.check_stated_utc(preds, syntax_index, syntax_report)
        bad(1, "a stated_utc after the report's own population is refused "
               "BY NAME", "loaded without error")
    except I.PredictionError as exc:
        if "r7code-1" not in str(exc):
            bad(1, "the refusal names §6.5/r7code-1", str(exc))
        else:
            ok(1, "a stated_utc AFTER this report's own population is "
                  "refused BY NAME (§6.5, r7code-1)")

    # interpret_subject_grain_v1.md §6 Q6 (i), RATIFIED: a `compile:`
    # quantity's selector may not name `subject_or_na`/`regime_or_na`.
    # Fixture pair, same precedent as the inexpressible/utc checks above.
    compile_scope = os.path.join(FIXTURES, "predictions-compile-scope.tsv")
    try:
        preds = I.load_predictions(compile_scope)
        bad(1, "a compile: quantity's selector naming subject_or_na/"
               "regime_or_na fails at load (Q6 (i))",
            f"loaded {len(preds)} clause(s) without error")
    except I.PredictionError as exc:
        if "Q6 (i)" not in str(exc) or "regime_or_na" not in str(exc):
            bad(1, "the refusal names Q6 (i) and the offending key",
                str(exc))
        else:
            ok(1, "Q6I.bad-regime fails at load, naming Q6 (i) and "
                  "regime_or_na (the FIRST bad row -- load_predictions "
                  "stops there; Q6I.bad-subject's own shape is proven by "
                  "the fixture's declared intent, not a second load)")
    # the CLEAN control row, alone, must load fine (a compile: quantity
    # naming no subject/regime dimension at all is not the defect).
    try:
        clean_only = _tmp_predictions_file(
            compile_scope, keep={"Q6I.clean"})
        try:
            I.load_predictions(clean_only)
            ok(1, "Q6I.clean (a compile: quantity with no subject/regime "
                  "key) loads without error (the control)")
        finally:
            os.unlink(clean_only)
        bad_subject_only = _tmp_predictions_file(
            compile_scope, keep={"Q6I.bad-subject"})
        try:
            I.load_predictions(bad_subject_only)
            bad(1, "Q6I.bad-subject fails at load, naming Q6 (i) and "
                   "subject_or_na", "loaded without error")
        except I.PredictionError as exc:
            if "Q6 (i)" not in str(exc) or "subject_or_na" not in str(exc):
                bad(1, "Q6I.bad-subject fails at load, naming Q6 (i) and "
                       "subject_or_na", str(exc))
            else:
                ok(1, "Q6I.bad-subject fails at load, naming Q6 (i) and "
                      "subject_or_na")
        finally:
            os.unlink(bad_subject_only)
    except Exception as exc:  # noqa: BLE001
        bad(1, "predictions-compile-scope.tsv fixture setup", str(exc))

    # interpret_subject_grain_v1.md §6 Q6 (ii), RATIFIED: every `testee=`
    # glob must match >= 1 MEASURED index testee for its own (subbench,
    # version); vacuous when unmeasured. `check_testee_globs` is store-free
    # (index only, `syntax_index` above -- the frozen snapshot), never
    # wired into `load_predictions` itself (a testee glob needs the
    # index, which `load_predictions` deliberately never reads).
    testee_glob_fixture = os.path.join(FIXTURES, "predictions-testee-glob.tsv")
    preds = I.load_predictions(testee_glob_fixture)
    clean = [p for p in preds if p["clause"] == ".clean"]
    bad_row = [p for p in preds if p["clause"] == ".bad"]
    vacuous = [p for p in preds if p["clause"] == ".vacuous"]
    try:
        I.check_testee_globs(clean, syntax_index)
        ok(1, "Q6II.clean's testee glob (matches real measured syntax@0.1 "
              "pcrec testees) passes check_testee_globs (Q6 (ii))")
    except I.PredictionError as exc:
        bad(1, "Q6II.clean passes check_testee_globs", str(exc))
    try:
        I.check_testee_globs(bad_row, syntax_index)
        bad(1, "Q6II.bad's testee glob (the P4.a defect shape) is refused "
               "by check_testee_globs (Q6 (ii))", "loaded without error")
    except I.PredictionError as exc:
        if "Q6 (ii)" not in str(exc):
            bad(1, "the refusal names Q6 (ii)", str(exc))
        else:
            ok(1, "Q6II.bad's testee glob is refused BY NAME "
                  "(Q6 (ii)) -- matches none of syntax@0.1's real "
                  "measured pcrec testees")
    try:
        I.check_testee_globs(vacuous, syntax_index)
        ok(1, "Q6II.vacuous (the SAME malformed glob against an "
              "unmeasured (subbench, version)) does NOT raise -- vacuous, "
              "per Q6 (ii)'s own stated qualifier")
    except I.PredictionError as exc:
        bad(1, "Q6II.vacuous does not raise for an unmeasured population",
            str(exc))
    # index=None makes every clause vacuous too (same rule check_stated_utc
    # already applies for the identical reason).
    try:
        I.check_testee_globs(bad_row, None)
        ok(1, "check_testee_globs(preds, index=None) is a no-op (same "
              "rule check_stated_utc already applies)")
    except I.PredictionError as exc:
        bad(1, "check_testee_globs(preds, index=None) is a no-op", str(exc))

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


# [B72smalls] OPEN CONFLICT, FILED FOR A RULING, NOT DECIDED HERE:
# Q6 (i)'s "fail loudly generally" load check (interpret_subject_grain_
# v1.md §6 Q6, ratified) correctly refuses `capability-0.1-first.tsv` at
# load -- P2.a/P2.b's ALREADY-DIAGNOSED Cause-B defect
# (regime_or_na=n/a against a compile: quantity). `docs/dev/predictions/
# CLAUDE.md`'s own entry for that file states this project's rule
# explicitly: predictions files are stated-PRE-RUN artifacts with "no
# revision mechanism for an already-scored file" -- so the file is not
# edited (section 1's own named exception, above, covers `load_
# predictions` alone). But FOUR committed `.interpretation.md` sidecars
# are STAMPED against this exact predictions file
# (`grep -l capability-0.1-first.tsv reports/*.interpretation.md`), and
# `interpret()` now refuses to run for ANY of them -- so this section's
# own "every committed sidecar re-renders byte-identical" invariant
# (catalogue/CLAUDE.md: "every bump regenerates every committed sidecar
# in the same commit") can never again be SATISFIED for these four,
# through no fault of a future bump: fixing the ratified check made
# fixing the file's own defect load-bearing, and fixing the file is
# exactly what the immutability rule above forbids. THREE of this
# project's own standing rules are in genuine tension (Q6 fail-loudly;
# predictions immutability; sidecar regenerability) and picking among
# them is not this lane's call. NAMED here, not silently absorbed: these
# four are counted SEPARATELY from the ordinary pass count below, never
# folded into "fresh", so a reader of `make check-interpret`'s own
# output sees the exact gap rather than a false green.
_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_RULING = {
    "reports/2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.interpretation.md",
    "reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.interpretation.md",
    "reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.interpretation.md",
    "reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.interpretation.md",
}


def section_3():
    n = 0
    n_blocked = 0
    for name in sorted(os.listdir(REPORTS)):
        if not name.endswith(".interpretation.md"):
            continue
        rel = f"reports/{name}"
        if rel in _SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_RULING:
            n_blocked += 1
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
        # [B47] interpret_subject_grain_v1.md §6 Q10 (ratified,
        # UNCONDITIONALLY): the stamp gap fix. Before this, a sidecar
        # rendered WITH --subject-grain would re-render WITHOUT it here
        # -- a live latent defect, unexposed only because no committed
        # sidecar used the flag. `subject_grain` is `(none)` on every
        # sidecar committed before this fix, so this is a no-op there.
        sg = stamp.get("subject_grain")
        sg = os.path.join(ROOT, sg) if sg and sg != "(none)" else None
        fresh = run_interpret(report, index, pred, "md", subject_grain=sg)
        if fresh != text:
            bad(3, f"{name}: re-renders byte-identical")
        else:
            ok(3, f"{name}: fresh")
    ok(3, f"{n} committed sidecar(s) checked "
          f"(the sidecars themselves are [B13.4]'s deliverable)")
    if n_blocked:
        ok(3, f"{n_blocked} sidecar(s) SKIPPED, NOT counted as fresh -- "
              f"BLOCKED ON A RULING (see the module-level comment above "
              f"section_3: Q6 (i)'s load refusal vs. predictions-file "
              f"immutability vs. sidecar regenerability)")


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
        sg = os.path.join(d, "subject_grain.tsv")
        sg = sg if os.path.exists(sg) else None
        try:
            facts = run_interpret(os.path.join(d, "report.tsv"),
                                  os.path.join(d, "index.tsv"), pred, "tsv",
                                  subject_grain=sg)
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
        # [B47] `mutate_subject_grain` joins the differing-mutation set
        # (a one-field VALUE change on the subject-grain slice, same
        # shape as `mutate`/`mutate_index`); `subject_grain` itself (the
        # SOURCE key naming which slice a fixture uses) joins `report`/
        # `select`/`synthetic` in the SHARED set -- interpret_subject_
        # grain_v1.md §2.1: "a subject-grain slice is a second BASE, not
        # a mutation", so a base/control pair must agree on it.
        keys = ("mutate", "mutate_header", "mutate_index",
                "mutate_predictions", "predictions_select",
                "mutate_subject_grain")
        differing = [k for k in keys if spec.get(k) != other.get(k)]
        shared = [k for k in ("report", "select", "synthetic", "subject_grain")
                  if spec.get(k) != other.get(k)]
        if shared:
            bad(4, f"{name}: shares its base's slice", f"differs on {shared}")
        if len(differing) != 1:
            bad(4, f"{name}: exactly one declared mutation differs from "
                   f"{base}", f"{differing}")
            continue
        columns = set()
        rows_differ = False
        for fname in ("report.tsv", "index.tsv", "predictions.tsv",
                     "subject_grain.tsv"):
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

    # the NULL CONTROL: all 33 rules quiet on the synthetic clean report
    clean = facts_by_name.get("CLEAN__all-measured")
    if clean is None:
        bad(4, "the null control runs")
    else:
        fired = {rid for rid, seqs in _fired(clean).items() if seqs}
        if fired:
            bad(4, "Report D (the null control): all 33 rules report fired=0",
                f"{sorted(fired)} fired")
        else:
            n = len(_tokens(clean))
            if n != 33:
                bad(4, "Report D names all 33 rules", f"named {n}")
            else:
                ok(4, "Report D (the null control): all 33 rules report "
                      "fired=0, and all 33 are named")


_FILE_COLUMNS = {"report.tsv": I.REPORT_COLUMNS,
                 "index.tsv": I.INDEX_COLUMNS,
                 "predictions.tsv": I.PRED_COLUMNS,
                 "subject_grain.tsv": I.REPORT_COLUMNS}


def _field_diff(path_a, path_b, fname):
    """(set of differing column names, row-count-differs). A header-key
    mutation shows as the pseudo-column `header:<key>`."""
    with open(path_a, encoding="utf-8") as fh:
        a = fh.read().split("\n")
    with open(path_b, encoding="utf-8") as fh:
        b = fh.read().split("\n")
    columns = set()
    if fname in ("report.tsv", "subject_grain.tsv") and a[0] != b[0]:
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
    # F27/r7code-1: the anchor-identity line's population is (index,
    # report) alone -- independent of what the predictions actually
    # say -- so the re-render-from-facts path computes the SAME anchor
    # the direct render did, one call, no re-derivation of its own.
    if pred_path:
        ctx.utc_anchor, ctx.utc_anchor_tuples = I._utc_anchor(index, report)
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

PROSE_FIELDS = ("template", "no_fire", "legend", "links", "no_fire_reasons")


def section_6():
    """The template-diff gate: a diff that touches a `template`,
    `no_fire`, `legend` or `links` field, or adds a `[[signature]]`, must
    carry a reviewer's approval line in the commit message naming the
    rule ids reviewed. The check cannot judge prose; what it can do is
    refuse to let prose change invisibly.

    Reads `HEAD~1..HEAD` of whatever commit is checked out -- so in a
    lane's own worktree, mid-development, this section legitimately fails
    on a WIP commit that touches one of these fields: a lane is not the
    reviewer. The approval line belongs on the commit the manager writes
    at merge (`docs/dev/lanes/b41_report.md` [B41] (c)) -- the commit
    that becomes `HEAD` on the integrated history, which is what this
    check actually reads once merged."""
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
               if re.match(r"^[+-]\s*(template|no_fire_reasons|no_fire|legend"
                           r"|links)\s*=", ln)
               or re.match(r"^\+\s*\[\[signature\]\]", ln)]
    if not touched:
        ok(6, "HEAD touches no template, no_fire, no_fire_reasons, legend "
              "or links field")
        return
    msg = subprocess.run(["git", "-C", ROOT, "log", "-1", "--format=%B"],
                         capture_output=True, text=True, timeout=30).stdout
    if not re.search(r"[Tt]emplate/no_fire/links reviewed|"
                     r"[Tt]emplate.*reviewed:", msg):
        bad(6, "a commit touching template/no_fire/legend/links carries a "
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
