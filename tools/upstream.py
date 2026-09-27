#!/usr/bin/env python3
"""tools/upstream.py -- the upstream-findings pipeline's helper CLI.

[B103], docs/design/upstream_pipeline_v1.md §5. The bench keeps finding
behaviour in OTHER engines (pcrec is out of scope -- its findings go to
the pcrec manager's outbox, never here). This tool is the one interface
onto docs/dev/upstream/findings.tsv (the REGISTRY, §2.1) and its
narrative twin docs/dev/upstream_findings.md, so the same procedure
runs whether a manager session or a lane files, reproduces, drafts or
sends a finding.

Subcommands (design note §5, plus `threads`, [B106]):
    check                          validate findings.tsv (make check-upstream)
    list [--engine E] [--status S] print the registry, filtered
    repro U<n>|--all [--engine-build PATH] [--record]
                                    run repro/U<n>/run.sh, parse its result line
    new --engine E --kind K --summary "..."
                                    allocate the next id, stub the registry
                                    row + narrative section + repro/README.md
    status U<n> STATUS [--tracker URL] [--note PATH]
                                    move a finding's status, enforcing §3's
                                    prerequisites (never silently); moving to
                                    REPORTED with a GitHub tracker also starts
                                    (or grows) that URL's threads.tsv row
    threads [--thread OWNER/REPO#N] [--record] [--json]
                                    check every filed GitHub thread (or one)
                                    for new comments/state/labels/cross-refs
                                    since the last --record, via `gh api`
                                    (read-only: GET only, never posts)

`check` never runs an engine and never shells out -- it is pure file
reading, which is what makes `make check-upstream` a seconds-scale gate
(Makefile's own rule for check-schema/check-harness). `repro` and
`threads` are the two subcommands that DO run something (`repro` a
local build+run, `threads` a `gh api` call), and only on explicit
request; `threads` never posts (no `gh issue comment`, no POST/PATCH).

Exit codes: `check` 0/1 (issues found); `repro` 0/1 (a repro ABSENT or
unparseable is not itself a failure of the TOOL, only `--all`'s
skip-unbuilt case differs from a named id's hard error); `threads` 0 =
nothing new, 10 = something new since the last check, 2 = a `gh`/
network error (never a silent 0 on error, so a cron or a session
polling the exit code can't mistake "gh failed" for "nothing changed").

The pure functions a caller (or a test) can use directly, with no CLI
and no fixed paths: `check_registry()` / `narrative_ids()` (findings.tsv
+ the narrative), `check_threads_registry()` (threads.tsv's own shape)
and `check_tracker_thread_linkage()` (the two-way findings<->threads
link) -- see tools/tests/test_upstream.py.
"""
import argparse
import csv
import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
UPSTREAM_DIR = ROOT / "docs" / "dev" / "upstream"
FINDINGS_TSV = UPSTREAM_DIR / "findings.tsv"
REPRO_ROOT = UPSTREAM_DIR / "repro"
NOTES_DIR = UPSTREAM_DIR / "notes"
NARRATIVE = ROOT / "docs" / "dev" / "upstream_findings.md"
THREADS_TSV = UPSTREAM_DIR / "threads.tsv"

# §2.1's column list, in order. `check`'s COLUMNS rule fires if a live
# findings.tsv's header ever drifts from this.
COLUMNS = [
    "id", "engine", "engine_version", "route", "kind", "status",
    "first_seen", "evidence", "repro", "latest_checked", "tracker",
    "note", "summary",
]

# §2.1: "engine family token as in testees/ (pcre2, re2, vectorscan,
# tre, onig, rust)" -- a closed six, unlike `route`'s "(jit, interp,
# dfa, block-nosom, ...)", which is illustrative, not closed, so `route`
# is never validated against a fixed set here. A multi-engine finding
# (one root cause shown on several engines, e.g. U10) uses a
# `;`-joined engine cell, the same join convention §2.1 already gives
# `evidence`; each token is checked against this set independently.
ENGINES = {"pcre2", "re2", "vectorscan", "tre", "onig", "rust"}

KINDS = {"correctness", "performance", "compatibility", "semantics"}

# §3's status ladder. The MAIN path is linear for rank purposes even
# though the note is explicit that "REPRODUCED and UNDERSTOOD may come
# in either order" -- see REPRO_REQUIRED below for what that means for
# the repro/ requirement. The three TERMINAL statuses are reachable
# directly from OBSERVED and carry no rank at all.
STATUS_LADDER = [
    "OBSERVED", "REPRODUCED", "UNDERSTOOD", "DRAFTED", "APPROVED",
    "REPORTED", "FIXED",
]
STATUS_TERMINAL = ["NOT-A-BUG", "KNOWN-UPSTREAM", "STALE"]
STATUSES = set(STATUS_LADDER) | set(STATUS_TERMINAL)
RANK = {s: i for i, s in enumerate(STATUS_LADDER)}

# repro/U<n>/ is required from REPRODUCED on -- EXCEPT at UNDERSTOOD
# alone. §3 says "REPRODUCED and UNDERSTOOD may come in either order";
# a finding can be UNDERSTOOD (cause confirmed by source-reading or an
# ablation) before anyone has built a standalone, maintainer-runnable
# repro/U<n>/ -- this project's own U11 is exactly that case (an
# archived C probe under docs/dev/measurements/, not yet a repro/).
# Requiring repro/ at UNDERSTOOD would make "either order" impossible
# to satisfy, so this set deliberately excludes it; DRAFTED and
# everything after it DOES require repro/ regardless (a note can never
# cite a repro that does not exist).
REPRO_REQUIRED = {"REPRODUCED", "DRAFTED", "APPROVED", "REPORTED", "FIXED"}
TRACKER_REQUIRED = {"REPORTED", "KNOWN-UPSTREAM"}
NOTE_REQUIRED = {"DRAFTED", "APPROVED", "REPORTED", "FIXED"}

ID_RE = re.compile(r"^U(\d+)$")
NARRATIVE_HEADER_RE = re.compile(r"^## (U\d+)\b", re.M)
RESULT_LINE_RE = re.compile(
    r"^(U\d+) (PRESENT|ABSENT|CANNOT-RUN) (\S+) (\S+) (\S+)\s*$"
)

# --------------------------------------------------------------------------
# threads.tsv -- [B106], "track the ids of the issue threads, then a
# script to check for comments" (Frank, 2026-09-27). One row per FILED
# GitHub thread (a subset of findings.tsv's own `tracker` cells that
# happen to be GitHub issue URLs -- a thread can carry several ids,
# §2.1's `;`-join convention, the same one `evidence`/`engine` already
# use for a multi-finding row).
# --------------------------------------------------------------------------

THREADS_COLUMNS = [
    "thread", "url", "ids", "filed", "state", "labels",
    "comments_seen", "last_seen_comment_id", "last_seen_at", "last_checked",
]

# OWNER/REPO#N -- gh's own shorthand for an issue, used as the row key so
# a session can type `--thread PCRE2Project/pcre2#1015` instead of a URL.
THREAD_KEY_RE = re.compile(r"^([^/\s]+)/([^#\s]+)#(\d+)$")
GITHUB_ISSUE_URL_RE = re.compile(r"^https://github\.com/([^/\s]+)/([^/\s]+)/issues/(\d+)$")

# statuses at which `check`'s THREAD-MISSING rule requires a threads.tsv
# row: everything past "we sent this" -- REPORTED itself, FIXED (a
# REPORTED finding the ladder moved further along, never losing its
# tracker) and KNOWN-UPSTREAM (an existing issue we point at but never
# filed ourselves -- still worth watching for an answer).
THREAD_STATUSES_NEEDING_THREAD = {"REPORTED", "FIXED", "KNOWN-UPSTREAM"}

# a comment addressed to the reporter, or asking anything at all, is a
# NEEDS-ANSWER candidate (skill's own triage step, never auto-answered).
NEEDS_ANSWER_RE = re.compile(r"\?|@fdicostanzo", re.I)


def check_threads_registry(header, rows, valid_finding_ids):
    """Pure function: no file I/O, no fixed paths -- validates
    threads.tsv's own shape, independent of findings.tsv beyond the id
    set the caller hands it (tools/tests/test_upstream.py calls this
    directly, same posture as check_registry()). An empty/missing
    threads.tsv (no header at all) is a valid state -- nothing has been
    filed yet -- and returns no issues.

    Rules, each producing one named Issue.rule:
      THREAD-COLUMNS  header != THREADS_COLUMNS
      THREAD-FORMAT   a `thread` cell that is not OWNER/REPO#N
      THREAD-URL      `url` does not match the OWNER/REPO#N the row names
      THREAD-DUP      a `thread` key used by more than one row
      THREAD-BAD-ID   an `ids` token that is not a real findings.tsv id
    """
    issues = []
    if not header:
        return issues
    if header != THREADS_COLUMNS:
        issues.append(
            Issue("THREAD-COLUMNS", None, f"threads.tsv header is {header!r}, expected {THREADS_COLUMNS!r}")
        )
        return issues

    seen = set()
    for row in rows:
        key = row.get("thread", "")
        m = THREAD_KEY_RE.match(key)
        if not m:
            issues.append(Issue("THREAD-FORMAT", key or "?", f"thread {key!r} is not OWNER/REPO#N"))
            continue
        owner, repo, num = m.groups()
        if key in seen:
            issues.append(Issue("THREAD-DUP", key, "thread appears more than once in threads.tsv"))
        seen.add(key)

        expected_url = f"https://github.com/{owner}/{repo}/issues/{num}"
        if row.get("url", "") != expected_url:
            issues.append(
                Issue("THREAD-URL", key, f"url {row.get('url','')!r} != {expected_url!r} (derived from the thread cell)")
            )

        for tok in row.get("ids", "").split(";"):
            if tok and tok != "-" and tok not in valid_finding_ids:
                issues.append(Issue("THREAD-BAD-ID", key, f"id {tok!r} is not a findings.tsv id"))

    return issues


def check_tracker_thread_linkage(finding_rows, thread_rows):
    """Pure function: every finding row at REPORTED/FIXED/KNOWN-UPSTREAM
    (THREAD_STATUSES_NEEDING_THREAD) whose `tracker` is a GitHub issue
    URL must have a threads.tsv row naming that exact URL AND carrying
    the finding's own id in its `ids` cell -- the two-way link `check`
    enforces so a REPORTED finding can never silently go untracked.
    A non-GitHub tracker (a mailing-list URL, a `searched:...` citation)
    is never required to have a thread row.

    Rule: THREAD-MISSING.
    """
    issues = []
    by_url = {}
    for t in thread_rows:
        by_url.setdefault(t.get("url", ""), []).append(t)

    for row in finding_rows:
        rid = row.get("id", "")
        status = row.get("status", "")
        tracker = row.get("tracker", "-")
        if status not in THREAD_STATUSES_NEEDING_THREAD:
            continue
        if not GITHUB_ISSUE_URL_RE.match(tracker):
            continue
        candidates = by_url.get(tracker, [])
        if not any(rid in t.get("ids", "").split(";") for t in candidates):
            issues.append(
                Issue("THREAD-MISSING", rid, f"status {status} with GitHub tracker {tracker} has no threads.tsv row naming it")
            )
    return issues


class Issue:
    """One `check` finding: which rule, which id (or None for a
    file-level rule like COLUMNS), and a human-readable message. Rule
    ids are uppercase tokens so a self-test can name exactly the one it
    expects, the way schema/examples/bad/'s file-name convention names
    a rule for its own checker (schema/CLAUDE.md; the naming is by
    string here, not by file, since one TSV holds every finding)."""

    __slots__ = ("rule", "id", "message")

    def __init__(self, rule, id_, message):
        self.rule, self.id, self.message = rule, id_, message

    def __str__(self):
        where = f"{self.id}: " if self.id else ""
        return f"[{self.rule}] {where}{self.message}"

    def __repr__(self):
        return f"Issue({self.rule!r}, {self.id!r}, {self.message!r})"


# --------------------------------------------------------------------------
# TSV I/O
# --------------------------------------------------------------------------

def read_tsv_rows(path: Path):
    """Returns (header, rows): header is a list of column names (empty
    list if the file is missing or empty); rows is a list of dicts.
    Never raises on a missing file -- an empty registry is a valid,
    if unlikely, state."""
    if not path.exists():
        return [], []
    with path.open(newline="", encoding="utf-8") as fh:
        raw = list(csv.reader(fh, delimiter="\t"))
    if not raw:
        return [], []
    header, data = raw[0], raw[1:]
    rows = []
    for r in data:
        if not r or (len(r) == 1 and r[0] == ""):
            continue  # tolerate a trailing blank line
        rows.append(dict(zip(header, r)))
    return header, rows


def write_tsv_rows(path: Path, header, rows):
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        for r in rows:
            w.writerow([r.get(c, "") for c in header])


def narrative_ids(text):
    """The `## U<n>` ids a narrative document declares, in file order
    (duplicates preserved -- that IS the bug `check` reports as a live
    finding when it happens, per record_schema.md-style "a check with
    no failing case proves nothing": U2/U3 were used twice for years
    before this pipeline existed to catch it)."""
    return [m.group(1) for m in NARRATIVE_HEADER_RE.finditer(text)]


def repro_complete(repro_dir: Path):
    """§2.2's minimum for a repro/U<n>/ that a maintainer could actually
    read and run: README.md + run.sh both present. expected.txt is NOT
    required here -- it only exists after a repro has actually been RUN
    once (`repro --record` or a prior `repro` invocation), which `check`
    -- which never runs anything -- cannot itself have caused."""
    return (repro_dir / "README.md").is_file() and (repro_dir / "run.sh").is_file()


# --------------------------------------------------------------------------
# check
# --------------------------------------------------------------------------

def check_registry(header, rows, narrative_ids_list, repro_root: Path):
    """Pure function: no file I/O, no fixed paths -- a caller (or
    tools/tests/test_upstream.py) hands it exactly what §5's `check`
    bullet lists. Returns a list of Issue, empty if the registry is
    clean.

    §5's rules, each producing one named Issue.rule:
      COLUMNS           header != the 13 declared columns
      ID-FORMAT         an id that is not `U<digits>`
      DUP-ID            an id used by more than one row
      ENGINE            an `;`-joined engine token outside the closed six
      KIND              a kind token outside the closed four
      STATUS            a status token outside the closed ladder+terminal set
      REPRO             status needs repro/U<n>/ (REPRO_REQUIRED) but the
                         column is `-` or the dir is missing README.md/run.sh
      TRACKER           status needs a tracker (TRACKER_REQUIRED) but it is `-`
      NOTE              status needs a note (NOTE_REQUIRED) but it is `-`
      TSV-ORPHAN        a registry row with no matching `## U<n>` narrative section
      NARRATIVE-ORPHAN  a narrative section with no matching registry row
    """
    issues = []
    if not header:
        issues.append(Issue("COLUMNS", None, "findings.tsv is empty or missing a header row"))
        return issues
    if header != COLUMNS:
        issues.append(
            Issue("COLUMNS", None, f"findings.tsv header is {header!r}, expected {COLUMNS!r}")
        )
        return issues  # column meanings are unreliable past this point

    seen = {}
    for row in rows:
        rid = row.get("id", "")
        m = ID_RE.match(rid)
        if not m:
            issues.append(Issue("ID-FORMAT", rid or "?", f"id {rid!r} does not match U<n>"))
            continue  # an ill-formed id never enters tsv_ids below
        if rid in seen:
            issues.append(Issue("DUP-ID", rid, "id appears more than once in findings.tsv"))
        seen[rid] = row

        for tok in row.get("engine", "").split(";"):
            if tok and tok not in ENGINES:
                issues.append(
                    Issue("ENGINE", rid, f"engine token {tok!r} not in {sorted(ENGINES)}")
                )

        kind = row.get("kind", "")
        if kind not in KINDS:
            issues.append(Issue("KIND", rid, f"kind {kind!r} not in {sorted(KINDS)}"))

        status = row.get("status", "")
        if status not in STATUSES:
            issues.append(Issue("STATUS", rid, f"status {status!r} not in {sorted(STATUSES)}"))
            continue  # the checks below all key off a valid status

        if status in REPRO_REQUIRED:
            repro_col = row.get("repro", "-")
            rdir = repro_root / rid
            if repro_col in ("-", ""):
                issues.append(
                    Issue("REPRO", rid, f"status {status} requires a repro/ dir but the repro column is '-'")
                )
            elif not repro_complete(rdir):
                issues.append(
                    Issue("REPRO", rid, f"status {status} requires {rdir} with README.md and run.sh")
                )

        if status in TRACKER_REQUIRED and row.get("tracker", "-") in ("-", ""):
            issues.append(Issue("TRACKER", rid, f"status {status} requires a tracker"))

        if status in NOTE_REQUIRED and row.get("note", "-") in ("-", ""):
            issues.append(Issue("NOTE", rid, f"status {status} requires a note"))

    tsv_ids = set(seen)
    narr_ids = set(narrative_ids_list)
    for rid in sorted(tsv_ids - narr_ids):
        issues.append(Issue("TSV-ORPHAN", rid, "registry row has no '## U<n>' narrative section"))
    for rid in sorted(narr_ids - tsv_ids):
        issues.append(Issue("NARRATIVE-ORPHAN", rid, "narrative section has no findings.tsv row"))

    return issues


def cmd_check(args):
    header, rows = read_tsv_rows(FINDINGS_TSV)
    narrative_text = NARRATIVE.read_text(encoding="utf-8") if NARRATIVE.exists() else ""
    issues = check_registry(header, rows, narrative_ids(narrative_text), REPRO_ROOT)

    valid_ids = {r["id"] for r in rows if ID_RE.match(r.get("id", ""))}
    t_header, t_rows = read_tsv_rows(THREADS_TSV)
    issues += check_threads_registry(t_header, t_rows, valid_ids)
    issues += check_tracker_thread_linkage(rows, t_rows)

    if issues:
        for i in issues:
            print(str(i), file=sys.stderr)
        print(f"check-upstream: {len(issues)} issue(s) over {len(rows)} finding(s), {len(t_rows)} thread(s)", file=sys.stderr)
        return 1
    print(f"check-upstream: OK -- {len(rows)} finding(s), {len(t_rows)} thread(s), 0 issues")
    return 0


# --------------------------------------------------------------------------
# list
# --------------------------------------------------------------------------

def cmd_list(args):
    header, rows = read_tsv_rows(FINDINGS_TSV)
    if not header:
        print("(findings.tsv is empty or missing)")
        return 0
    shown = 0
    for r in rows:
        if args.engine and args.engine not in r.get("engine", "").split(";"):
            continue
        if args.status and r.get("status", "") != args.status:
            continue
        print(
            f"{r.get('id',''):<5} {r.get('engine',''):<24} {r.get('status',''):<15} "
            f"{r.get('kind',''):<13} {r.get('summary','')[:90]}"
        )
        shown += 1
    print(f"({shown}/{len(rows)} shown)")
    return 0


# --------------------------------------------------------------------------
# repro
# --------------------------------------------------------------------------

def run_one_repro(rid, engine_build=None):
    """Runs repro/<rid>/run.sh under $UPSTREAM_SCRATCH (default a fresh
    dir under build/upstream/<rid>/), returns (match, error) where match
    is a RESULT_LINE_RE match on success and error is a string on
    failure. Never raises for an ordinary "no repro" case."""
    rdir = REPRO_ROOT / rid
    run_sh = rdir / "run.sh"
    if not run_sh.is_file():
        return None, f"{rid}: no run.sh at {rdir}"
    scratch = Path(os.environ.get("UPSTREAM_SCRATCH", str(ROOT / "build" / "upstream" / rid)))
    scratch.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, UPSTREAM_SCRATCH=str(scratch))
    if engine_build:
        env["UPSTREAM_ENGINE_BUILD"] = engine_build
    try:
        proc = subprocess.run(
            ["bash", str(run_sh)], cwd=rdir, env=env,
            capture_output=True, text=True, timeout=600,
        )
    except subprocess.TimeoutExpired:
        return None, f"{rid}: run.sh timed out after 600s"
    lines = [ln for ln in proc.stdout.splitlines() if ln.strip()]
    last = lines[-1] if lines else ""
    m = RESULT_LINE_RE.match(last)
    if not m:
        stderr_tail = proc.stderr.strip().splitlines()[-1:] or [""]
        return None, (
            f"{rid}: run.sh exited {proc.returncode} with no parseable result line "
            f"(last stdout line: {last!r}; last stderr line: {stderr_tail[0]!r})"
        )
    return m, None


def cmd_repro(args):
    header, rows = read_tsv_rows(FINDINGS_TSV)
    if args.all:
        ids = [r["id"] for r in rows if ID_RE.match(r.get("id", ""))]
    elif args.id:
        ids = [args.id]
    else:
        print("error: give an id or --all", file=sys.stderr)
        return 2

    by_id = {r["id"]: r for r in rows}
    ok = True
    for rid in ids:
        rdir = REPRO_ROOT / rid
        if not rdir.is_dir():
            print(f"{rid}: no repro/{rid}/ -- skipped" if args.all else f"{rid}: no repro/{rid}/", file=sys.stderr)
            ok = ok and args.all  # --all tolerates unbuilt repros; a named id does not
            continue
        m, err = run_one_repro(rid, args.engine_build)
        if err:
            print(err, file=sys.stderr)
            ok = False
            continue
        _, outcome, engine, version, evidence = m.groups()
        print(f"{rid} {outcome} {engine} {version} {evidence}")
        if args.record and rid in by_id:
            by_id[rid]["latest_checked"] = f"{version}@{datetime.date.today().isoformat()}"

    if args.record:
        write_tsv_rows(FINDINGS_TSV, header, rows)
        print(f"--record: findings.tsv latest_checked updated for {len(ids)} id(s)")

    return 0 if ok else 1


# --------------------------------------------------------------------------
# new
# --------------------------------------------------------------------------

def cmd_new(args):
    header, rows = read_tsv_rows(FINDINGS_TSV)
    if not header:
        header = list(COLUMNS)

    if "\t" in args.summary or "\n" in args.summary:
        print("error: --summary must be one line with no tabs", file=sys.stderr)
        return 2

    nums = [int(m.group(1)) for r in rows if (m := ID_RE.match(r.get("id", "")))]
    nid = f"U{(max(nums) + 1) if nums else 1}"
    today = datetime.date.today().isoformat()

    row = {c: "-" for c in header}
    row.update(
        id=nid, engine=args.engine, kind=args.kind, status="OBSERVED",
        first_seen=today, summary=args.summary,
    )
    rows.append(row)
    write_tsv_rows(FINDINGS_TSV, header, rows)

    with NARRATIVE.open("a", encoding="utf-8") as fh:
        fh.write(
            f"\n## {nid} — {args.summary} (OBSERVED {today})\n\n"
            f"(narrative to be written)\n"
        )

    repro_dir = REPRO_ROOT / nid
    repro_dir.mkdir(parents=True, exist_ok=True)
    (repro_dir / "README.md").write_text(
        f"# {nid} repro\n\n"
        f"What it shows: (fill in)\n\n"
        f"Engine + version: {args.engine} (fill in exact version)\n\n"
        f"Build/run: (fill in -- run.sh does this)\n\n"
        f"Expected PRESENT output: (fill in once run.sh exists and has been run)\n\n"
        f"What ABSENT (fixed) looks like: (fill in)\n",
        encoding="utf-8",
    )
    print(f"allocated {nid}; findings.tsv row + narrative stub + repro/{nid}/README.md written")
    print(f"next: write repro/{nid}/run.sh, then 'tools/upstream.py status {nid} REPRODUCED'")
    return 0


# --------------------------------------------------------------------------
# status
# --------------------------------------------------------------------------

def cmd_status(args):
    header, rows = read_tsv_rows(FINDINGS_TSV)
    if not header:
        print("error: findings.tsv is empty or missing", file=sys.stderr)
        return 1
    if args.status not in STATUSES:
        print(f"error: unknown status {args.status!r}, not in {sorted(STATUSES)}", file=sys.stderr)
        return 2
    row = next((r for r in rows if r.get("id") == args.id), None)
    if row is None:
        print(f"error: {args.id} not found in findings.tsv", file=sys.stderr)
        return 1

    new_tracker = args.tracker if args.tracker is not None else row.get("tracker", "-")
    new_note = args.note if args.note is not None else row.get("note", "-")

    if args.status in REPRO_REQUIRED:
        rdir = REPRO_ROOT / args.id
        if not repro_complete(rdir):
            print(
                f"error: {args.id} -> {args.status} requires {rdir} with README.md "
                f"and run.sh, which is not there yet -- refusing",
                file=sys.stderr,
            )
            return 1
        row["repro"] = f"docs/dev/upstream/repro/{args.id}/"

    if args.status in TRACKER_REQUIRED and new_tracker in ("-", ""):
        print(f"error: {args.id} -> {args.status} requires --tracker", file=sys.stderr)
        return 1

    if args.status in NOTE_REQUIRED and new_note in ("-", ""):
        print(f"error: {args.id} -> {args.status} requires --note", file=sys.stderr)
        return 1

    row["status"] = args.status
    row["tracker"] = new_tracker
    row["note"] = new_note
    write_tsv_rows(FINDINGS_TSV, header, rows)
    print(f"{args.id} -> {args.status}")

    if args.status == "REPORTED" and new_tracker not in ("-", ""):
        note = _ensure_thread_row(new_tracker, args.id)
        if note:
            print(f"threads.tsv: {note}")

    return 0


def _ensure_thread_row(tracker_url, finding_id):
    """`status U<n> REPORTED --tracker <github issue URL>` auto-starts
    (or grows) that URL's threads.tsv row, so tracking begins at filing
    time rather than waiting for a session to remember `threads` exists
    (design note §7's 'file' step, grown here per [B106]). A no-op for
    any non-GitHub tracker (a mailing-list URL, a bare search citation).
    Returns a one-line note for the caller to print, or None."""
    m = GITHUB_ISSUE_URL_RE.match(tracker_url)
    if not m:
        return None
    owner, repo, num = m.groups()
    thread_key = f"{owner}/{repo}#{num}"

    header, rows = read_tsv_rows(THREADS_TSV)
    if not header:
        header = list(THREADS_COLUMNS)

    row = next((r for r in rows if r.get("thread") == thread_key), None)
    if row is None:
        row = {c: "-" for c in header}
        row.update(
            thread=thread_key, url=tracker_url, ids=finding_id,
            filed=datetime.date.today().isoformat(), state="-", labels="-",
            comments_seen="0", last_seen_comment_id="-", last_seen_at="-",
            last_checked="-",
        )
        rows.append(row)
        action = "created"
    else:
        ids = [t for t in row.get("ids", "-").split(";") if t and t != "-"]
        if finding_id in ids:
            action = "unchanged"
        else:
            ids.append(finding_id)
            row["ids"] = ";".join(ids)
            action = "grown"

    write_tsv_rows(THREADS_TSV, header, rows)
    return f"{thread_key} ({action})"


# --------------------------------------------------------------------------
# threads -- run `tools/upstream.py threads` at wake / by a heartbeat to
# check every filed GitHub thread for new comments, state changes, label
# changes and cross-references since the last `--record`. Never posts
# anything (read-only against GitHub: `gh api` GETs only).
# --------------------------------------------------------------------------

GH_API_TIMEOUT = 30


def _gh_api(path):
    """Runs `gh api <path>` and parses its JSON. Raises RuntimeError on
    any failure (gh missing, network, rate limit, bad JSON) -- the
    caller turns that into exit code 2. Never returns a silent empty
    result for an error."""
    try:
        proc = subprocess.run(
            ["gh", "api", path], capture_output=True, text=True, timeout=GH_API_TIMEOUT,
        )
    except FileNotFoundError:
        raise RuntimeError("the `gh` CLI is not on PATH")
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"gh api {path} timed out after {GH_API_TIMEOUT}s")
    if proc.returncode != 0:
        raise RuntimeError(f"gh api {path} failed (rc={proc.returncode}): {proc.stderr.strip()[:500]}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"gh api {path} returned unparseable JSON: {e}")


def _gh_api_paginated(path, per_page=100):
    """Loops page=1.. over an array-returning endpoint, stopping on a
    short (or empty) page. Raises the same RuntimeError _gh_api does."""
    out = []
    sep = "&" if "?" in path else "?"
    page = 1
    while True:
        chunk = _gh_api(f"{path}{sep}per_page={per_page}&page={page}")
        if not isinstance(chunk, list):
            raise RuntimeError(f"gh api {path} page {page}: expected a JSON array, got {type(chunk).__name__}")
        out.extend(chunk)
        if len(chunk) < per_page:
            break
        page += 1
    return out


def _fetch_thread_state(owner, repo, num):
    """Returns (issue, comments, timeline). `timeline` is best-effort --
    a fetch failure there does not fail the whole thread check, since
    the design note calls it 'if cheap' rather than required."""
    issue = _gh_api(f"repos/{owner}/{repo}/issues/{num}")
    comments = _gh_api_paginated(f"repos/{owner}/{repo}/issues/{num}/comments")
    try:
        timeline = _gh_api_paginated(f"repos/{owner}/{repo}/issues/{num}/timeline")
    except RuntimeError:
        timeline = []
    return issue, comments, timeline


def _parse_gh_time(s):
    return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))


def _cutoff_dt(row):
    """None means 'never checked before' -- everything counts as new."""
    ts = row.get("last_checked", "-")
    if ts in ("-", ""):
        return None
    try:
        return _parse_gh_time(ts)
    except ValueError:
        return None


def _indent(text, prefix="    "):
    return "\n".join(prefix + ln for ln in text.splitlines()) if text else prefix + "(empty)"


def _diff_thread(row, issue, comments, timeline):
    """Returns (lines, record): `lines` are print-ready strings
    describing everything NEW since `row`'s own stored state (empty if
    nothing moved); `record` is the field dict --record writes back."""
    cutoff = _cutoff_dt(row)
    last_seen_id_s = row.get("last_seen_comment_id", "-")
    last_seen_id = int(last_seen_id_s) if last_seen_id_s not in ("-", "") else 0

    lines = []

    old_state = row.get("state", "-")
    new_state = issue.get("state", "-")
    if old_state not in ("-", "") and old_state != new_state:
        lines.append(f"STATE: {old_state} -> {new_state}")

    old_labels = {t for t in row.get("labels", "-").split(";") if t and t != "-"}
    new_labels = {l["name"] for l in issue.get("labels", [])}
    if old_labels or new_labels:
        added, removed = new_labels - old_labels, old_labels - new_labels
        if added:
            lines.append(f"LABELS ADDED: {', '.join(sorted(added))}")
        if removed:
            lines.append(f"LABELS REMOVED: {', '.join(sorted(removed))}")

    for c in comments:
        c_id = c["id"]
        is_new = c_id > last_seen_id
        is_edited = (not is_new) and cutoff is not None and _parse_gh_time(c["updated_at"]) > cutoff
        if cutoff is None and not is_new:
            is_new = True  # a hand-seeded row with pre-existing comments: report all of them once
        if not (is_new or is_edited):
            continue
        needs_answer = bool(NEEDS_ANSWER_RE.search(c.get("body", "")))
        tag = "EDITED" if is_edited else "NEW"
        flag = " [NEEDS-ANSWER]" if needs_answer else ""
        lines.append(
            f"COMMENT {tag}{flag} id={c_id} by {c['user']['login']} "
            f"({c.get('author_association', '?')}) at {c['created_at']} -- {c['html_url']}"
        )
        lines.append(_indent(c.get("body", "")))

    for ev in timeline:
        etype = ev.get("event")
        if etype not in ("cross-referenced", "closed", "reopened", "labeled", "unlabeled"):
            continue
        ev_time = ev.get("created_at") or ev.get("updated_at")
        if not ev_time:
            continue
        try:
            ev_dt = _parse_gh_time(ev_time)
        except ValueError:
            continue
        if cutoff is not None and ev_dt <= cutoff:
            continue
        if etype == "cross-referenced":
            src = ev.get("source", {}).get("issue", {})
            lines.append(f"CROSS-REF: {src.get('html_url', '?')} ({src.get('title', '')[:80]!r})")
        elif etype in ("closed", "reopened"):
            lines.append(f"EVENT: {etype} at {ev_time}")
        else:
            lines.append(f"EVENT: {etype} {ev.get('label', {}).get('name', '?')}")

    new_max_id = max([last_seen_id] + [c["id"] for c in comments]) if comments else last_seen_id
    newest_comment_time = max((c["updated_at"] for c in comments), default=None)

    record = {
        "state": new_state,
        "labels": ";".join(sorted(new_labels)) if new_labels else "-",
        "comments_seen": str(len(comments)),
        "last_seen_comment_id": str(new_max_id) if comments else row.get("last_seen_comment_id", "-"),
        "last_seen_at": newest_comment_time if newest_comment_time else row.get("last_seen_at", "-"),
    }
    return lines, record


def cmd_threads(args):
    t_header, t_rows = read_tsv_rows(THREADS_TSV)
    if not t_header:
        t_header = list(THREADS_COLUMNS)

    ad_hoc = False
    if args.thread:
        m = THREAD_KEY_RE.match(args.thread)
        if not m:
            print(f"error: --thread must be OWNER/REPO#N, got {args.thread!r}", file=sys.stderr)
            return 2
        targets = [r for r in t_rows if r.get("thread") == args.thread]
        if not targets:
            ad_hoc = True
            owner, repo, num = m.groups()
            stub = {c: "-" for c in t_header}
            stub.update(thread=args.thread, url=f"https://github.com/{owner}/{repo}/issues/{num}")
            targets = [stub]
    else:
        targets = list(t_rows)

    if not targets:
        print("(threads.tsv is empty or missing -- nothing to check)")
        return 0

    any_new = False
    json_results = []
    for row in targets:
        m = THREAD_KEY_RE.match(row.get("thread", ""))
        if not m:
            print(f"error: malformed thread key {row.get('thread', '')!r} in threads.tsv", file=sys.stderr)
            return 2
        owner, repo, num = m.groups()
        try:
            issue, comments, timeline = _fetch_thread_state(owner, repo, num)
        except RuntimeError as e:
            print(f"error: {row.get('thread')}: {e}", file=sys.stderr)
            return 2

        lines, record = _diff_thread(row, issue, comments, timeline)
        if lines:
            any_new = True

        if args.json:
            json_results.append({"thread": row.get("thread"), "url": row.get("url"), "new": lines, "record": record})
        else:
            print(f"== {row.get('thread')} ({row.get('url')}) ==")
            if lines:
                for ln in lines:
                    print(f"  {ln}")
            else:
                last = row.get("last_checked", "-")
                print(f"  (no changes since {last if last != '-' else 'ever'})")

        if args.record:
            if ad_hoc:
                print(f"  --record: {row.get('thread')} is not in threads.tsv -- nothing to write", file=sys.stderr)
                continue
            row.update(record)
            row["last_checked"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            for i, r in enumerate(t_rows):
                if r.get("thread") == row.get("thread"):
                    t_rows[i] = row
                    break

    if args.json:
        print(json.dumps(json_results, indent=2))

    if args.record:
        write_tsv_rows(THREADS_TSV, t_header, t_rows)
        print(f"--record: threads.tsv updated for {len(targets)} thread(s)")

    return 10 if any_new else 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def build_parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check", help="validate findings.tsv (make check-upstream)")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("list", help="print the registry, filterable")
    p.add_argument("--engine")
    p.add_argument("--status")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("repro", help="run repro/U<n>/run.sh (or --all)")
    p.add_argument("id", nargs="?", help="e.g. U6")
    p.add_argument("--all", action="store_true", help="run every id with a repro/ dir")
    p.add_argument("--engine-build", help="point the repro at a different engine build (the latest-release check)")
    p.add_argument("--record", action="store_true", help="write the run's outcome into latest_checked")
    p.set_defaults(func=cmd_repro)

    p = sub.add_parser("new", help="allocate the next id and stub its files")
    p.add_argument("--engine", required=True, choices=sorted(ENGINES))
    p.add_argument("--kind", required=True, choices=sorted(KINDS))
    p.add_argument("--summary", required=True)
    p.set_defaults(func=cmd_new)

    p = sub.add_parser("status", help="move a finding's status, enforcing §3's prerequisites")
    p.add_argument("id")
    p.add_argument("status")
    p.add_argument("--tracker")
    p.add_argument("--note")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("threads", help="check filed GitHub threads for new comments/state/labels/cross-refs")
    p.add_argument("--thread", help="OWNER/REPO#N; default: every row in threads.tsv")
    p.add_argument("--record", action="store_true", help="write the new seen-state back into threads.tsv")
    p.add_argument("--json", action="store_true", help="machine-readable output instead of text")
    p.set_defaults(func=cmd_threads)

    return ap


def main(argv=None):
    ap = build_parser()
    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
