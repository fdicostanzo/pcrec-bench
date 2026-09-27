# lane b106threads — thread tracking for the upstream-findings pipeline

Branch `lane/b106threads`, worktree `worktrees/b106threads`, branch point
`82337fc` (master). Task: Frank ("track the ids of the issue threads,
then a script to check for comments in case there are questions or
discussion"), following the two GitHub issues just filed from his
account: `PCRE2Project/pcre2#1015` (carries U1/U2/U4) and
`VectorCamp/vectorscan#416` (U7). A measurement window (`build/windows/
suite_b104_*`) was running on the box for the whole lane; nothing here
touched `make check-harness`/`check-report`/`check-interpret` or ran
anything on the box beyond `python3` and a handful of read-only `gh api`
GETs, per the brief's own note.

## Deliverables, against the brief

1. **`docs/dev/upstream/threads.tsv` — the committed THREAD REGISTRY.**
   Columns exactly as specified: `thread url ids filed state labels
   comments_seen last_seen_comment_id last_seen_at last_checked`. Seeded
   with both real threads, fetched live via `gh api` at seed time (both
   `open`, 0 comments, no labels — confirmed below) and re-fetched again
   after `--record` to confirm state:
   ```
   thread                       url                                                  ids       filed       state  labels comments_seen last_seen_comment_id last_seen_at last_checked
   PCRE2Project/pcre2#1015      https://github.com/PCRE2Project/pcre2/issues/1015     U1;U2;U4  2026-09-27  open   -      0             -                    -            2026-09-27T14:23:34Z
   VectorCamp/vectorscan#416    https://github.com/VectorCamp/vectorscan/issues/416   U7        2026-09-27  open   -      0             -                    -            2026-09-27T14:23:35Z
   ```
2. **`tools/upstream.py threads` subcommand**, same interface, stdlib +
   `gh` CLI via `subprocess`, no new deps. `[--thread OWNER/REPO#N]
   [--record] [--json]` exactly as specified. For each thread: `gh api
   repos/{o}/{r}/issues/{n}` (the issue), `.../issues/{n}/comments`
   (paginated, `_gh_api_paginated`), `.../issues/{n}/timeline`
   (best-effort — a failure there never fails the whole check, since the
   design note calls it "if cheap" rather than required). Prints ONLY
   what is NEW since the registry row (`_diff_thread`): each new/edited
   comment (author, `author_association`, time, url, full body),
   state/label changes, new cross-references (`cross-referenced`/
   `closed`/`reopened`/`labeled`/`unlabeled` timeline events past the
   row's own `last_checked` cutoff). A comment containing `?` or
   `@fdicostanzo` is flagged `[NEEDS-ANSWER]`. Exit codes exactly as
   specified: 0 = nothing new, 10 = something new, 2 = a `gh`/network
   error (`_gh_api`/`_gh_api_paginated` raise `RuntimeError` on any
   failure — gh missing, timeout, non-zero exit, unparseable JSON —
   which `cmd_threads` turns into 2, never a silent 0). `--record` writes
   the new seen-state back (state, labels, comment count, the newest
   comment id/time, `last_checked`) ONLY on explicit request, same
   posture as `repro --record`. Never posts: every GitHub call is `gh
   api <path>` with no verb flag, i.e. a GET; there is no code path that
   calls `gh issue comment`/`--method POST`/`--method PATCH` anywhere in
   the module.
3. **`check` extended** (`check_threads_registry` +
   `check_tracker_thread_linkage`, both pure functions, no fixed paths):
   `check_threads_registry` validates threads.tsv's own shape
   (THREAD-COLUMNS, THREAD-FORMAT — a `thread` cell not `OWNER/REPO#N`,
   THREAD-URL — the `url` cell not matching the `thread` cell,
   THREAD-DUP, THREAD-BAD-ID — an `ids` token that isn't a real
   findings.tsv id). `check_tracker_thread_linkage` is the two-way rule
   the brief asked for: every finding at REPORTED/FIXED/KNOWN-UPSTREAM
   whose `tracker` is a GitHub issue URL must have a threads.tsv row
   naming that URL AND carrying the finding's id in `ids`
   (THREAD-MISSING); a non-GitHub tracker (a mailing-list URL, a bare
   `searched:<date>:none-found` citation) is never required to have one.
   Both wired into `cmd_check`/`make check-upstream`. Self-tests: 10 new
   cases in `tools/tests/test_upstream.py` (5 for
   `check_threads_registry`, 4 for `check_tracker_thread_linkage`
   including a below-REPORTED control proving the rule doesn't
   over-fire), same "good fixture + one-field sabotage named for the
   rule it must fire alone" posture the existing 13 findings.tsv cases
   use. `test_upstream.py`'s `main()` now runs all three checker groups;
   **23/23 cases OK**.
4. **`new`/`status` path documented and automated.** `status U<n>
   REPORTED --tracker <GitHub issue URL>` now calls
   `_ensure_thread_row()`: if the URL is unseen, a new threads.tsv row is
   created (`ids` = the one finding); if the URL already has a row, the
   finding's id is appended to its `ids` if not already there (a
   multi-finding thread, e.g. U1/U2/U4 all on the same pcre2 issue);
   idempotent if the id is already listed. Verified directly (not just
   read): a fresh call creates a row, a second call with a different id
   on the same URL grows `ids` to `U99;U100`, a third call with the same
   id is a no-op ("unchanged"), and a non-GitHub tracker is a clean
   no-op (`None`) — see the transcript in "Validation" below. Documented
   in the skill's **Approve / send** step, `docs/dev/upstream/CLAUDE.md`'s
   `threads.tsv` file entry, and `tools/CLAUDE.md`'s `upstream.py` row.
5. **Scheduled-use note.** New **Watch** procedure in
   `.claude/skills/pcrec-bench-upstream/SKILL.md`: run `tools/upstream.py
   threads` at session wake (added to the **Session checklist** too) and
   by a heartbeat if one exists; read exit codes 0/10/2 (2 is never
   "quiet" — investigate); state/label/cross-ref changes go into the
   finding's narrative section; an informational comment (no
   `[NEEDS-ANSWER]`) is noted in the narrative, no reply; a
   `[NEEDS-ANSWER]` comment gets a draft reply written to
   `docs/dev/upstream/notes/replies/<thread-with-slashes-as-dashes>-
   <YYYY-MM-DD>.md`, sent ONLY on Frank's approval, exactly like a note
   — the skill never posts on its own reading of "this seems fine."
   `--record` closes out a handled batch. Mirrored (shorter) in
   `docs/dev/upstream/CLAUDE.md`'s new `threads.tsv`/`notes/replies/`
   file entries and in `tools/CLAUDE.md`'s `upstream.py` row.

## Design notes not spelled out in the brief

- **Edit detection without a per-comment history column.** The columns
  the brief specified give one `last_seen_comment_id` (the highest id
  seen) and one `last_seen_at`/`last_checked` per thread, not a
  per-comment ledger. A comment is NEW if its id exceeds
  `last_seen_comment_id`; it is EDITED if its id is already seen but its
  `updated_at` is newer than the row's own `last_checked` cutoff — cheap,
  no extra state, and correct for the common case (an edit after the
  last time a session looked). A row with `last_checked = "-"` (never
  checked) treats every existing comment as NEW once, which only matters
  for a hand-seeded row that already carries history — the two real rows
  here started at 0 comments, so this path is inert for them today.
- **`--thread` on an unregistered URL is a read-only, ad hoc check** (a
  session sanity-checking a candidate thread before filing it): it
  fetches and diffs against an all-`-` synthetic row (so everything
  currently on the issue reads as new), and `--record` for that case
  prints a stderr note and writes nothing, since there is no registry
  row to persist into — filing (`status ... REPORTED --tracker URL`) is
  what creates the row.
- **THREAD-MISSING's status set is REPORTED ∪ FIXED ∪ KNOWN-UPSTREAM**,
  not REPORTED alone — reasoning in `docs/dev/upstream/CLAUDE.md`'s
  "Design decision worth flagging" section (FIXED is reached FROM
  REPORTED so its thread is still worth watching; KNOWN-UPSTREAM points
  at an issue we never filed but still want an answer from).

## Validation

`make check-upstream` (full output, both checker groups + the real
registries):
```
== check-upstream ==
-- check_registry --
  PASS  good-fixture-clean ... (13/13, unchanged)
-- check_threads_registry --
  PASS  good-threads-fixture-clean   got=[]                     expect=[]
  PASS  threads-columns-mismatch     got=['THREAD-COLUMNS']      expect=['THREAD-COLUMNS']
  PASS  thread-format-bad            got=['THREAD-FORMAT']       expect=['THREAD-FORMAT']
  PASS  thread-url-mismatch          got=['THREAD-URL']          expect=['THREAD-URL']
  PASS  thread-dup                   got=['THREAD-DUP']          expect=['THREAD-DUP']
  PASS  thread-bad-id                got=['THREAD-BAD-ID']       expect=['THREAD-BAD-ID']
-- check_tracker_thread_linkage --
  PASS  good-linkage-fixture-clean   got=[]                     expect=[]
  PASS  thread-missing-row           got=['THREAD-MISSING']      expect=['THREAD-MISSING']
  PASS  thread-missing-id            got=['THREAD-MISSING']      expect=['THREAD-MISSING']
  PASS  not-required-below-reported  got=[]                     expect=[]
test_upstream: 23/23 cases OK

check-upstream: OK -- 13 finding(s), 2 thread(s), 0 issues
```

Live run against both real threads (before `--record`; both freshly
filed, zero comments, no labels — matches `gh api` reality confirmed
independently in this lane):
```
$ python3 tools/upstream.py threads
== PCRE2Project/pcre2#1015 (https://github.com/PCRE2Project/pcre2/issues/1015) ==
  (no changes since ever)
== VectorCamp/vectorscan#416 (https://github.com/VectorCamp/vectorscan/issues/416) ==
  (no changes since ever)
$ echo $?
0
```

`--record`:
```
$ python3 tools/upstream.py threads --record
== PCRE2Project/pcre2#1015 (https://github.com/PCRE2Project/pcre2/issues/1015) ==
  (no changes since ever)
== VectorCamp/vectorscan#416 (https://github.com/VectorCamp/vectorscan/issues/416) ==
  (no changes since ever)
--record: threads.tsv updated for 2 thread(s)
$ echo $?
0
```

Second run, exits 0 (nothing new — the required proof that `--record`
actually moved the cutoff and a repeat check is quiet):
```
$ python3 tools/upstream.py threads
== PCRE2Project/pcre2#1015 (https://github.com/PCRE2Project/pcre2/issues/1015) ==
  (no changes since 2026-09-27T14:23:34Z)
== VectorCamp/vectorscan#416 (https://github.com/VectorCamp/vectorscan/issues/416) ==
  (no changes since 2026-09-27T14:23:35Z)
$ echo $?
0
```

`--thread` targeting one row, and `--json`, both verified working (see
tool-call transcript this lane produced; not reproduced here for space —
`--thread PCRE2Project/pcre2#1015` alone printed only that thread and
exited 0; `--json` emitted a well-formed array with one object per
thread carrying `thread`/`url`/`new`/`record`).

`_ensure_thread_row` verified directly against a scratch `THREADS_TSV`
path (never the committed file): first call on an unseen URL creates a
row (`ids=U99`); second call on the same URL with a different id grows
it (`ids=U99;U100`); third call with an already-listed id is a no-op
("unchanged"); a non-GitHub tracker (`searched:...`) returns `None` and
touches nothing.

## Charter vs. committed

| brief item | status |
|---|---|
| 1. `threads.tsv` seeded, both real threads fetched | COMMITTED |
| 2. `threads` subcommand: fetch, diff, print-only-new, NEEDS-ANSWER flag, exit 0/10/2, `--record` | COMMITTED |
| 3. `check` extended (two rules) + self-tests | COMMITTED (23/23) |
| 4. `new`/`status` path: documented + automated | COMMITTED |
| 5. scheduled-use note in skill + two CLAUDE.mds | COMMITTED |
| `make check-upstream` green | COMMITTED (23/23 + real registries clean) |
| live run against both real threads, pasted | COMMITTED (above) |
| `--record`, then a second run exiting 0 | COMMITTED (above) |
| report with charter-vs-committed checklist | THIS FILE |

Nothing OWED. No long run launched (nothing in this lane crosses the
~4-minute DO-THEN-FINISH threshold — `make check-upstream` is
seconds-scale and the `gh api` calls are a handful of GETs). No other
`make check-*` target run, per the brief's box-load note — the running
measurement window was never touched.
