#!/usr/bin/env python3
"""tools/tests/test_upstream.py -- self-tests for `tools/upstream.py`'s
`check_registry()`, `check_threads_registry()` and
`check_tracker_thread_linkage()` (make check-upstream; the latter two,
[B106], validate threads.tsv's own shape and its two-way link with
findings.tsv).

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


# --------------------------------------------------------------------------
# check_threads_registry -- [B106]. Same posture: one small GOOD
# threads.tsv (the two real rows this project actually filed, U1/U2/U4
# on the pcre2 thread and U7 on the vectorscan one) that must pass with
# ZERO issues, then one-field sabotages named for the rule each must
# fire alone.
# --------------------------------------------------------------------------

def _good_threads_fixture():
    header = list(U.THREADS_COLUMNS)

    def row(**kw):
        r = {c: "-" for c in header}
        r.update(kw)
        return r

    rows = [
        row(thread="pcre2project/pcre2#1015", url="https://github.com/pcre2project/pcre2/issues/1015",
            ids="U1;U2", filed="2026-09-27", state="open", comments_seen="0"),
        row(thread="vectorcamp/vectorscan#416", url="https://github.com/vectorcamp/vectorscan/issues/416",
            ids="U7", filed="2026-09-27", state="open", comments_seen="0"),
    ]
    valid_ids = {"U1", "U2", "U7"}
    return header, rows, valid_ids


def _run_threads(mutate=None):
    header, rows, valid_ids = _good_threads_fixture()
    if mutate is not None:
        header, rows, valid_ids = mutate(header, [dict(r) for r in rows], set(valid_ids))
    return U.check_threads_registry(header, rows, valid_ids)


THREADS_CASES = []


def threads_case(name, expect_rules, mutate=None):
    THREADS_CASES.append((name, set(expect_rules), mutate))


threads_case("good-threads-fixture-clean", set())


def tmut_columns(header, rows, valid_ids):
    return header[:-1], rows, valid_ids  # drop "last_checked"


threads_case("threads-columns-mismatch", {"THREAD-COLUMNS"}, tmut_columns)


def tmut_format(header, rows, valid_ids):
    rows[0]["thread"] = "not-a-valid-thread-key"
    return header, rows, valid_ids


threads_case("thread-format-bad", {"THREAD-FORMAT"}, tmut_format)


def tmut_url(header, rows, valid_ids):
    rows[0]["url"] = "https://github.com/wrong/repo/issues/999"
    return header, rows, valid_ids


threads_case("thread-url-mismatch", {"THREAD-URL"}, tmut_url)


def tmut_dup(header, rows, valid_ids):
    rows.append(dict(rows[0]))  # the same thread key twice
    return header, rows, valid_ids


threads_case("thread-dup", {"THREAD-DUP"}, tmut_dup)


def tmut_badid(header, rows, valid_ids):
    rows[0]["ids"] = "U1;U99"  # U99 does not exist
    return header, rows, valid_ids


threads_case("thread-bad-id", {"THREAD-BAD-ID"}, tmut_badid)


# --------------------------------------------------------------------------
# check_tracker_thread_linkage -- the two-way findings.tsv <-> threads.tsv
# link `check` enforces: a REPORTED/FIXED/KNOWN-UPSTREAM finding with a
# GitHub tracker must have a threads.tsv row naming both the URL and the
# finding's own id.
# --------------------------------------------------------------------------

def _good_linkage_fixture():
    finding_rows = [
        {"id": "U1", "status": "REPORTED", "tracker": "https://github.com/pcre2project/pcre2/issues/1015"},
        {"id": "U6", "status": "NOT-A-BUG", "tracker": "searched:2026-09-27:none-found"},
        {"id": "U7", "status": "REPORTED", "tracker": "https://github.com/vectorcamp/vectorscan/issues/416"},
    ]
    thread_rows = [
        {"thread": "pcre2project/pcre2#1015", "url": "https://github.com/pcre2project/pcre2/issues/1015", "ids": "U1"},
        {"thread": "vectorcamp/vectorscan#416", "url": "https://github.com/vectorcamp/vectorscan/issues/416", "ids": "U7"},
    ]
    return finding_rows, thread_rows


def _run_linkage(mutate=None):
    finding_rows, thread_rows = _good_linkage_fixture()
    if mutate is not None:
        finding_rows, thread_rows = mutate(
            [dict(r) for r in finding_rows], [dict(r) for r in thread_rows]
        )
    return U.check_tracker_thread_linkage(finding_rows, thread_rows)


LINKAGE_CASES = []


def linkage_case(name, expect_rules, mutate=None):
    LINKAGE_CASES.append((name, set(expect_rules), mutate))


linkage_case("good-linkage-fixture-clean", set())


def lmut_missing_row(finding_rows, thread_rows):
    thread_rows.pop()  # the vectorscan row is gone entirely; U7 REPORTED is now orphaned
    return finding_rows, thread_rows


linkage_case("thread-missing-row", {"THREAD-MISSING"}, lmut_missing_row)


def lmut_missing_id(finding_rows, thread_rows):
    thread_rows[1]["ids"] = "-"  # the row exists but forgot to list U7
    return finding_rows, thread_rows


linkage_case("thread-missing-id", {"THREAD-MISSING"}, lmut_missing_id)


def lmut_not_required(finding_rows, thread_rows):
    finding_rows[0]["status"] = "OBSERVED"  # U1 no longer needs a thread row
    thread_rows.pop(0)                      # and its row is gone too -- clean
    return finding_rows, thread_rows


linkage_case("not-required-below-reported", set(), lmut_not_required)


def main():
    groups = [
        ("check_registry", CASES, _run),
        ("check_threads_registry", THREADS_CASES, _run_threads),
        ("check_tracker_thread_linkage", LINKAGE_CASES, _run_linkage),
    ]

    total = 0
    total_ok = 0
    for label, cases, runner in groups:
        print(f"-- {label} --")
        for name, expect_rules, mutate in cases:
            if runner is _run:
                with tempfile.TemporaryDirectory() as td:
                    issues = runner(Path(td), mutate)
            else:
                issues = runner(mutate)
            got_rules = {i.rule for i in issues}
            ok = got_rules == expect_rules
            total += 1
            total_ok += 1 if ok else 0
            status = "PASS" if ok else "FAIL"
            print(f"  {status}  {name:28s} got={sorted(got_rules)!r:40s} expect={sorted(expect_rules)!r}")

    print(f"test_upstream: {total_ok}/{total} cases OK")
    return 0 if total_ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
