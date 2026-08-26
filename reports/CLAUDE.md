# reports/ — generated reports over the store

Each file is the output of one `python3 -m pcrecbench report ...` query,
committed beside the records it reduces so a reader can cite a number
with its query. Names: `<date>-<subbench>-<version>-<machine>[-<label>][.<grain>].md|tsv`.

**Reports are RE-RENDERED when the reporter changes** ([B9], 2026-08-25):
the STORED RECORDS are the data; a report is a VIEW over them, and the
view is versioned separately (`reporter: vN (date)`, a header line every
render carries — `pcrecbench/report.py`'s `REPORTER_VERSION`). When
`report.py`'s rendering changes, every committed report is regenerated
with the SAME QUERY that produced it (named in its own header) so the
file keeps its identity (the same records, the same filters) while
picking up the new columns/rulings. `report … | diff - <file>` is empty
immediately after a regeneration — the reporter is deterministic, so a
non-empty diff after a bare rerun (no query change, no reporter change)
means either the store changed or the reporter regressed determinism.

Both sample sets below were regenerated at [B14] (2026-08-25) against
reporter `v4 (2026-08-25)` (`v3` on the same day, then `v4` for a same-day
correction — see the KB-2 note below; previously regenerated at [B9]
against `v2`): each regeneration means these files no longer diff
byte-identical against the previous reporter's versions, but each still
answers the SAME query as before — see `pcrecbench/report.py`'s module
docstring for the full ruling list ([B9]'s R1-R9, [B14]'s R1-R10 — the
two ruling sets share numbers by coincidence of two separate `R1`..`R9`
sequences, not by design; read each set's own dated section) and the
note below for what [B14] changed in these files specifically.

- `2026-08-25-email-specimen-0.1-budu-ryzen1600.md` — the FIRST
  PRODUCTION SAMPLE: email-specimen@0.1 × {pcre2-interp, pcre2-jit,
  pcrec-auto, pcrec-nocaps, pcrec-vm} at pin 8da6120, 5 trials, pinned
  to CPU 11, in a quiet window coordinated with the pcrec manager
  session (02:22-02:56 EDT); set grain. `.subject-grain.md` the
  per-subject drill-down; `.tsv` the machine-readable form. Query:
  `--subbench email-specimen --until 2026-08-25T07:00:00Z` — the
  `--until` bound is NOW REQUIRED to reproduce this exact 5-record
  snapshot ([B9] regeneration note): the store has since grown past this
  sample's original "only 5 records exist yet" window (the re-pin
  sample below, and OD-B15's newest-wins dedup, would otherwise pull
  later records of the SAME testee_ids into what this file's name
  claims is the pin-8da6120-only sample).
- `2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.md` — the
  RE-PIN SAMPLE ([B8]): the same six cells re-measured after pcrec's
  re-pin to `692c2e8` (the caller-provided frame-buffer testees added,
  `pcrec-vm-in` measured), alongside the surviving pin-8da6120 records
  and the store's own re-measurements: a second libpcre2-interp run
  (17:34, under load) landed `inconclusive-load` and, per OD-B15's
  AMENDED dedup rule ([B9], 2026-08-25 — a newer non-measured record is
  not evidence against an older measured one and does not supersede it),
  does NOT replace the original 06:22 measured record — it is listed
  under the header as "newer, not measured" instead, and the 06:22
  record is what the ranking tables actually use; a second libpcre2-jit
  run (17:41) DID land `measured`, so it supersedes the first jit record
  under the ordinary newest-measured-wins rule (see the header's
  "superseded records" line). Query: `--subbench email-specimen` (no
  bound needed: every record this sample was drawn from already existed
  when it was first generated). `.subject-grain.md` the per-subject
  drill-down; `.tsv` the machine-readable form. Read alongside
  `docs/dev/feedback_pcrecdev1_2026-08-25-repin.md` (the pcrec manager's
  reading that became [B9]'s R1-R9 rulings) and
  `docs/dev/feedback_pcrecdev1_2026-08-25.md`.

**[B14] (2026-08-25) regenerated both sample sets against reporter `v3
(2026-08-25)`** — docs/dev/feedback_pcrecdev1_2026-08-25-repin-v2.md (the
pcrec manager's second reading of the v2 rendering) was the spec, rulings
R1-R10 (`pcrecbench/report.py`'s module docstring has the full list; the
summary that matters for reading these files):

- a compile-cost table's per-testee CONSTANT facts (`engine`, `entry`,
  `prefilter`, `vm_rungs`, and the buffer/frame facts below) moved OFF
  the table into a one-line-per-testee LEGEND printed above it (R8) — a
  reader now checks the legend once per testee, not once per row;
- a plain-entry compile row states the STAMPED DEFAULT capacity it
  actually runs on (`buffers=2048/3072 (stamped default)`), not a blank
  (R1); the legend's `buffers`/`frame` facts read `n/s` (nothing stamped
  at that pin) or `0 (DFA)` (stamped, and zero because a DFA artifact
  takes no buffers) — never a bare `-`/`0` standing for either (R4);
- `jitter` is a computed ratio (`stddev/median`) or `timer-floor` under a
  20-microsecond floor, not a boolean, and the column disappears from a
  table where every row comes back empty rather than printing a wall of
  blanks (R5);
- every compile-cost row carries its `artifact bytes` (R7);
- a `large-subject-throughput` ranking row carries `ns/byte` beside
  `ns/call`, and a set of <=3 subjects (every throughput cell today)
  gets its own per-subject sub-table under the ranking row (R2);
- a `match-compliance` ranking group states `matches: m/n` when
  derivable, `matches: n/s` otherwise (R3 — see the KB-2 correction
  below: as of `v4` it is ALWAYS `n/s` in these files, honestly, not a
  fabricated fraction);
- a cross-pin `Δ detail` line names `worst now` and, only when it is a
  DIFFERENT subject, `largest Δ` beside it, instead of one ambiguous
  "worst subject" (R6);
- the Query header's superseded-record list collapsed to one summary
  line (`--all-records` still lists every id) (R8).

R9 (a `role: floor` pattern's short-subject-search table retitled a
per-call overhead CONTROL, with a `floor ns` figure on every other
pattern's row) reads `floor: n/a` unchanged in these files — bench/email
gained a real floor pattern in its SOURCE the same day (lane b15floor,
schema v1.3), but no MEASURED record of it exists in `store/` yet, so
this regeneration's own data has nothing to show. The wiring itself is
proven two ways in `pcrecbench/tests/test_report.py`: against hand-built
records (`test_floor_pattern_r9`) and, now that v1.3 makes `patterns[].
role` schema-legal, against a REAL schema-valid fixture file
(`test_floor_pattern_fixture_r9`, `pcrecbench/tests/fixtures/
floor_pattern/`) — ready for the day a real floor-pattern measurement
lands here.

**KB-2 correction (same day, before final merge; docs/dev/
known_issues.md; manager steer 2026-08-25): R3's `matches: m/n` moved
from "read `bench/email/expectations.tsv` live" to "derive from the
record alone."** The reporter must work from records alone — a record
measured on another box, or against a later sub-bench version, has no
sidecar checkout beside it to read. The record itself turns out to carry
no field this can be derived from either, for the common case:
`pcrecbench.harness.outcome_for` sets `observed = None` on a
`matched-as-expected` row (checked against these very files' own
records), so `pcrecbench.report._matching_subject_count` now always
returns `None` and every `match-compliance` group here reads `matches:
n/s`, pointing at KB-2 rather than a fabricated fraction. `report.py` no
longer imports `pcrecbench.subbench` at all. `REPORTER_VERSION` bumped
`v3` → `v4` the same day for this (its own rule: bump whenever rendering
changes).

**A note on what [B9]'s own rulings changed in this store's numbers**:
applying R1 (OD-B14: a non-`measured` row is excluded from ranking by
default) to the re-pin sample means two of the four `692c2e8` pcrec
testees (`auto-caps`, `auto-nocaps`) are `inconclusive-load` and have NO
measured record at all yet, so they are UNRANKED in every table (see
their "not ranked" lines) unless `--include-unmeasured` is passed — a
re-measure of those two on a quiet box would rank them. The DEFAULT
baseline testee (`libpcre2 engine_mode=interp`, named in every table
title) IS ranked, using its original 06:22 measured record: R2/OD-B15
was AMENDED (manager, 2026-08-25, before this lane's merge) specifically
because the first cut of the dedup rule — newest record wins regardless
of status — would have let interp's later `inconclusive-load` re-measure
silently displace its earlier measured one and vanish from every table's
baseline; the amended rule (newest MEASURED record wins; a newer
non-measured one is listed separately, never treated as evidence against
an older measured one) restores it.
