#!/usr/bin/env python3
"""tools/tests/test_upstream.py -- self-tests for `tools/upstream.py`'s
`check_registry()` (make check-upstream).

Small in-tempdir fixtures, in the spirit of tools/CLAUDE.md's own
established precedent for a fixture too small to earn a committed file
(check_id_preflight's `_write_synthetic_subbench`, check_rxt_export's
`_StubSubbench`): one small GOOD registry (three findings, one at each
of OBSERVED / REPRODUCED / REPORTED, its own repro/ dirs written fresh
under a tempdir) that must pass with ZERO issues -- the necessary
positive control every sabotage below needs, since a checker that fails
everything would "pass" every one of them for the wrong reason
(schema/examples/bad/CLAUDE.md's own rule: "a control that fails for
two reasons is not a control").

Each BAD case is the good fixture with exactly ONE field mutated, named
for the rule it must fire -- schema/examples/bad/'s naming convention
adapted to code: a committed directory of a dozen near-duplicate TSV
files would only restate this same table in a heavier, harder-to-audit
form, so the mutation lives as a small function instead of a file, and
its name plays the file name's role. Where a mutation could cascade
into a SECOND rule (renaming a good row's id would orphan its narrative
section too), the fixture is built to avoid the cascade instead
(id-format and tsv-orphan each ADD a fresh row rather than mutating an
existing one) -- so every case below asserts the EXACT rule set fired,
not just "at least one".

    python3 tools/tests/test_upstream.py
"""
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))  # tools/ -- no package __init__, same
                                       # convention tools/CLAUDE.md documents
                                       # for export_rxt.py
import upstream as U  # noqa: E402


def _write_repro(root: Path, rid: str, readme=True, run_sh=True):
    d = root / rid
    d.mkdir(parents=True, exist_ok=True)
    if readme:
        (d / "README.md").write_text(f"# {rid} repro (fixture)\n", encoding="utf-8")
    if run_sh:
        (d / "run.sh").write_text("#!/bin/sh\necho fixture\n", encoding="utf-8")


def _good_fixture(tmp_path: Path):
    """Three findings: U1 OBSERVED (no repro/tracker/note needed), U2
    REPRODUCED (repro/ needed), U5 REPORTED (repro/ + tracker + note
    needed) -- one witness per requiring status, matching narrative
    sections, both required repro dirs written complete."""
    header = list(U.COLUMNS)

    def row(**kw):
        r = {c: "-" for c in header}
        r.update(kw)
        return r

    rows = [
        row(id="U1", engine="pcre2", engine_version="10.46", route="jit",
            kind="performance", status="OBSERVED", first_seen="2026-08-25",
            evidence="rec-1", summary="a timeout finding"),
        row(id="U2", engine="tre", engine_version="0.9.0", route="default",
            kind="correctness", status="REPRODUCED", first_seen="2026-09-18",
            evidence="rec-2", repro="docs/dev/upstream/repro/U2/",
            summary="a correctness gap"),
        row(id="U5", engine="re2", engine_version="11.0.0", route="default",
            kind="semantics", status="REPORTED", first_seen="2026-09-26",
            evidence="rec-5", repro="docs/dev/upstream/repro/U5/",
            tracker="https://example.invalid/issue/1",
            note="docs/dev/upstream/notes/re2-2026-09-27.md",
            summary="a semantics difference, sent upstream"),
    ]
    narrative = (
        "## U1 — a timeout finding (OBSERVED 2026-08-25)\n\nbody\n\n"
        "## U2 — a correctness gap (OBSERVED 2026-09-18, REPRODUCED 2026-09-19)\n\nbody\n\n"
        "## U5 — a semantics difference (OBSERVED 2026-09-26, REPORTED)\n\nbody\n"
    )
    repro_root = tmp_path / "repro"
    _write_repro(repro_root, "U2")
    _write_repro(repro_root, "U5")
    return header, rows, narrative, repro_root


def _run(tmp_path, mutate=None):
    header, rows, narrative, repro_root = _good_fixture(tmp_path)
    if mutate is not None:
        header, rows, narrative, repro_root = mutate(
            header, [dict(r) for r in rows], narrative, repro_root
        )
    return U.check_registry(header, rows, U.narrative_ids(narrative), repro_root)


CASES = []


def case(name, expect_rules, mutate=None):
    CASES.append((name, set(expect_rules), mutate))


case("good-fixture-clean", set())


def mut_columns(header, rows, narrative, repro_root):
    return header[:-1], rows, narrative, repro_root  # drop "summary"


case("columns-header-mismatch", {"COLUMNS"}, mut_columns)


def mut_kind(header, rows, narrative, repro_root):
    rows[0]["kind"] = "correctness-ish"
    return header, rows, narrative, repro_root


case("kind-bad-token", {"KIND"}, mut_kind)


def mut_status(header, rows, narrative, repro_root):
    rows[1]["status"] = "REPRODUCE"  # typo, not a real token
    return header, rows, narrative, repro_root


case("status-bad-token", {"STATUS"}, mut_status)


def mut_engine(header, rows, narrative, repro_root):
    rows[0]["engine"] = "unknownengine"
    return header, rows, narrative, repro_root


case("engine-bad-token", {"ENGINE"}, mut_engine)


def mut_dupid(header, rows, narrative, repro_root):
    dup = dict(rows[1])
    dup["status"], dup["repro"] = "OBSERVED", "-"  # keep the dup itself requirement-free
    rows.append(dup)
    return header, rows, narrative, repro_root


case("dup-id", {"DUP-ID"}, mut_dupid)


def mut_idformat(header, rows, narrative, repro_root):
    # A fresh row with a bad id, rather than renaming a good one: an
    # ill-formed id is never added to tsv_ids (check_registry `continue`s
    # before that), so it cannot also orphan a narrative section --
    # renaming an existing row WOULD (its old narrative header would
    # become orphaned too), which is exactly the cascade this fixture
    # design avoids.
    rows.append({c: "-" for c in header} | {
        "id": "U1x", "engine": "pcre2", "kind": "performance",
        "status": "OBSERVED", "summary": "bad id",
    })
    return header, rows, narrative, repro_root


case("id-format", {"ID-FORMAT"}, mut_idformat)


def mut_tsv_orphan(header, rows, narrative, repro_root):
    rows.append({c: "-" for c in header} | {
        "id": "U9", "engine": "pcre2", "kind": "performance",
        "status": "OBSERVED", "summary": "no narrative section",
    })
    return header, rows, narrative, repro_root


case("tsv-orphan", {"TSV-ORPHAN"}, mut_tsv_orphan)


def mut_narrative_orphan(header, rows, narrative, repro_root):
    narrative += "\n## U9 — an orphaned section (OBSERVED 2026-09-27)\n\nbody\n"
    return header, rows, narrative, repro_root


case("narrative-orphan", {"NARRATIVE-ORPHAN"}, mut_narrative_orphan)


def mut_repro_missing_column(header, rows, narrative, repro_root):
    rows[1]["repro"] = "-"  # U2 stays REPRODUCED but "forgets" to record the path
    return header, rows, narrative, repro_root


case("repro-missing-column", {"REPRO"}, mut_repro_missing_column)


def mut_repro_incomplete_dir(header, rows, narrative, repro_root):
    (repro_root / "U2" / "run.sh").unlink()
    return header, rows, narrative, repro_root


case("repro-incomplete-dir", {"REPRO"}, mut_repro_incomplete_dir)


def mut_tracker_missing(header, rows, narrative, repro_root):
    rows[2]["tracker"] = "-"  # U5 stays REPORTED with no tracker
    return header, rows, narrative, repro_root


case("tracker-missing", {"TRACKER"}, mut_tracker_missing)


def mut_note_missing(header, rows, narrative, repro_root):
    rows[2]["note"] = "-"  # U5 stays REPORTED with no note
    return header, rows, narrative, repro_root


case("note-missing", {"NOTE"}, mut_note_missing)


def main():
    results = []
    for name, expect_rules, mutate in CASES:
        with tempfile.TemporaryDirectory() as td:
            issues = _run(Path(td), mutate)
        got_rules = {i.rule for i in issues}
        ok = got_rules == expect_rules
        results.append((name, ok, got_rules, expect_rules))

    for name, ok, got, expect in results:
        status = "PASS" if ok else "FAIL"
        print(f"  {status}  {name:28s} got={sorted(got)!r:40s} expect={sorted(expect)!r}")

    n_ok = sum(1 for _, ok, _, _ in results if ok)
    print(f"test_upstream: {n_ok}/{len(results)} cases OK")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
