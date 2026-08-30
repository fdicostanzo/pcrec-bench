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

**[B12] R10 (2026-08-29) regenerated every report below against reporter
`v7 (2026-08-29)`.** Same queries, same records — one ruling, and it
changes the rendering of exactly one file's RANKING content: a
did-not-compile compile cell now prints `not ranked: <testee> —
did-not-compile (<diagnostic>)` under its ranking table instead of
vanishing from the ranking silently (see `pcrecbench/report.py`'s
module docstring, "THE [B12] RULING"). Of the four report sets here,
only `2026-08-28-loglines-0.1-budu-ryzen1600-first-sample-35e1ab1.md`
(and its `.subject-grain.md`; the `.tsv` gets a `did_not_compile`
section row) has a live did-not-compile cell to show:
`level-context`/`pcrec-auto` did not compile at pcrec 35e1ab1, and its
`short-subject-search` and `large-subject-throughput` ranking tables now
each carry the bullet, naming the diagnostic verbatim ("pattern too
complex for the DFA engine (>32000 states; try --engine=vm) (pattern
offset 0)"). Every other committed report's only diff against its `v6`
render is the version-line bump (`reporter: v6 (2026-08-28)` →
`reporter: v7 (2026-08-29)`) — no did-not-compile cell exists in
email-specimen's records at any pin measured so far.

Every report below was regenerated at [B16] R9 (2026-08-28, later the
same day) against reporter `v6 (2026-08-28)` — the per-subject
sub-table keyed on the regime; and the two `-repin-692c2e8` files' query
gained `--version 0.1` when `email-specimen@0.2` records entered the
store (the SAME records as before: the version filter now says what the
store's contents used to imply). Before that, both sample sets were
regenerated at [B16] against reporter `v5 (2026-08-28)` (previously at [B14] against `v3` then `v4`
the same day — see the KB-2 note below; and at [B9] against `v2`): each
regeneration means these files no longer diff byte-identical against the
previous reporter's versions, but each still answers the SAME query as
before — see `pcrecbench/report.py`'s module docstring for the full
ruling list ([B9]'s R1-R9, [B14]'s R1-R10, [B16]'s R1-R8, [B12]'s R10 —
the ruling sets share numbers by coincidence of separate `R1..`
sequences, not by design; read each set's own dated section) and the
notes below for what each wave changed in these files specifically.

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

**[B16] (2026-08-28) regenerated both sample sets against reporter `v5
(2026-08-28)`.** The re-pin to pcrec 35e1ab1 (abi 8) is the wave; the
reporter half of it is pcrec's inbox I-7 §3 and §5, and FOUR of its
rulings change what these committed files say about records that have
not moved. No number moved — the records are the same records — but two
verdicts and two annotations did:

- **the ×13.45 is gone, and what replaced it is the finding.** `factored`
  / `short-subject-search` / `pcrec-auto` read `faster ×13.45` at `v4`
  across 8da6120 → 692c2e8. It now reads `selection changed (vm → dfa)`
  ([B16] R4): at 8da6120 `auto` selected the VM for `factored` (its rows
  gave up with `-2:PCREC_ERR_STEPS`, a code only the VM can produce) and
  at 692c2e8 it selects the DFA. The ×13.45 was two engines, not one
  engine getting faster — pcrec I-7 §3 caught it by hand; the reporter
  catches it now. The same substitution happens in three more cells
  (`factored`'s throughput and compliance rows), where the verdict reads
  `selection changed (vm → dfa); now measured (was: gave-up)`: a
  selection change EXPLAINS a cell that used to be excluded, so both
  facts print, and only the faster/slower RATIO is suppressed.
- **the legend is scoped per (pattern, form) where a testee's cells
  disagree** ([B16] R3). `pcrec_8da6120_auto-caps-simdna` now gets one
  legend line per cell, because at that pin it compiled `orig` to a DFA
  artifact and `factored` to a VM one — the `v4` legend printed
  `engine=dfa` for the whole testee, which was `orig`'s measured value
  wearing `factored`'s name. Every testee whose cells agree still gets
  ONE line, with `(identical on all N (pattern, form) cells)` under it.
- **`jitter` gained `(max is trial 1)`** ([B16] R6) wherever the cell's
  maximum is its first trial — including the eager-JIT rows whose
  0.556/0.645 jitter was I-7 §5's example of a first-trial warm-up that
  a bare ratio could not distinguish from noise.
- **a `set composition` column** ([B16] R7) flags a set-grain ratio that
  is really one subject. In these files it fires on
  `libpcre2_10.46_interp-caps-simdna`'s two throughput rows:
  `t-a-valid-addrs` is 99.9 % of that set, so interp's "3.15× slower
  than JIT" is a ratio of that one subject — 144× FASTER on the other
  two, which the per-subject sub-table under the row shows.

The DFA mechanism columns ([B16] R1) and the fast-tier clause (R2) are
present in these files but have nothing to show: every record here is
from pcrec abi 2 or 3, before those stamps existed, so the legend reads
`dfa: n/s (pcrec abi 3, before the DFA stamps landed at abi 4)` and
`fast tier=n/a (pcrec abi 3: no tier existed before abi 5)`. Which
ABSENCE a missing stamp is gets decided from the record's own `abi`
pair, never guessed — the first record measured at the 35e1ab1 pin will
show the values instead.

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

- `2026-08-28-email-specimen-0.2-budu-ryzen1600-repin-35e1ab1.md` — the
  [B16] re-pin sample at pcrec **35e1ab1** (abi 8) on `email-specimen@0.2`
  (five throughput subjects: [B17]'s two non-periodic prose subjects
  beside the periodic three), six cells `measured` 2026-08-28 10:16-10:59
  EDT, `--trials 5`, quiet window, reporter v7 (this entry's own "v5" had
  drifted through the v6/[B16] R9 regeneration; corrected here at
  [B12] R10, no content beyond the version line changed for this file).
  Query:
  `report --subbench email-specimen --version 0.2 --until
  2026-08-29T00:00:00Z --format md` (the `--until` bound added
  2026-08-29 when the 36d5963 records entered the store: the pcre2
  testee_ids carry no pin, so newest-measured-wins would otherwise pull
  that day's pcre2 records into this file). The
  prediction ledger against the 692c2e8 records (journal, third session
  part 5) is read per SUBJECT because the throughput set grew — a 0.1
  set sum and a 0.2 set sum are different cells. `.subject-grain.md`
  (`--grain subject`) carries the periodic-vs-prose rows that answer
  pcrec's I-10; `.tsv` the same set-grain query as TSV.

- `2026-08-30-bounded-0.1-budu-ryzen1600-first-sample-36d5963.md` — the
  FIRST SAMPLE of sub-bench #4, `bench/bounded@0.1` ([B11.4]), at pcrec
  **36d5963** (abi 11): six cells `measured` — three in the window of
  2026-08-29/30 23:21-01:21 EDT (pcre2-interp, pcrec-nocaps, pcrec-vm; the
  1-s occupancy instrument) and three RE-RUN 05:22-06:17 EDT under BD7
  (pcre2-jit, pcrec-auto, pcrec-vm-in; their first runs are in the store
  as `inconclusive-load` history, OD-B12 → BD7 → [B20]); `--trials 5`,
  quiet windows, reporter v7. Query: `report --subbench bounded --version
  0.1 --until 2026-08-30T12:00:00Z --format md` (the `--until` bound
  present from the first render: the pcre2 testee_ids carry no pin, and
  the abi-12 window at 96e44c2 ([B19]) enters the store next).
  `.subject-grain.md` (`--grain subject`) and `.tsv` the same query. This
  is the [OPT-4] BEFORE (inbox I-18 (i)). Read beside
  `bench/bounded/NOTES.md`'s predictions and `oracle_limits.tsv`: the
  class ladder's `cls-upto-65535` is `did-not-compile` under both
  `pcrec-auto` and `pcrec-nocaps` (`pattern too large (NFA exceeds 131072
  states)` — the NFA cap, at every pin), while `cls-upto-32768` COMPILED
  as a plain-VM artifact (no prefilter, cursor rung) — the set's predicted
  abi-11 size-cap refusal at that rung did not fire; the ctx ladder and
  `cls-upto-16384`'s whole-subject form are VM artifacts (the DFA state
  cap in the engine role), their `plain` forms DFA.

- `2026-08-28-loglines-0.1-budu-ryzen1600-first-sample-35e1ab1.md` — the
  FIRST SAMPLE of sub-bench #2, `bench/loglines@0.1` ([B11.1]), at pcrec
  **35e1ab1** (abi 8): six cells `measured` 2026-08-28 11:00-11:50 EDT,
  `--trials 5`, quiet window, reporter v7 (regenerated at [B12] R10; see
  above). Query: `report --subbench
  loglines --version 0.1 --until 2026-08-29T00:00:00Z --format md` (the
  `--until` bound added 2026-08-29, same reason as the entry above; the
  R10 bullets show that `pcrec-nocaps` did not compile `level-context`
  at 35e1ab1 either). This is the report pcrec's
  [OPT-5] was chartered to be decided on (journal third session part 6;
  outbox O-7 items 4-6): read the search-band ranking beside
  `bench/loglines/pattern_facts.tsv`'s presence counts; `pcrec-auto`
  has NO `level-context` rows because that artifact did not compile
  (the compile-cost table says `did-not-compile=1`; the ranking's
  `short-subject-search` and `large-subject-throughput` tables each carry
  `not ranked: \`pcrec_35e1ab1_auto-caps-simdna\` — did-not-compile
  (pattern too complex for the DFA engine (>32000 states; try
  --engine=vm) (pattern offset 0))` since [B12] R10). `.subject-grain.md`
  carries the 16 KB-1 MB sweep rows per flavour (fail / hit / syslog);
  `.tsv` the set-grain query.

- `2026-08-29-email-specimen-0.2-budu-ryzen1600-repin-36d5963.md` — the
  [B18] re-pin sample at pcrec **36d5963** (abi 11; inbox I-15/I-16/I-17
  absorbed as one adapter change) on `email-specimen@0.2`: six cells
  `measured` 2026-08-29 15:06-15:43 EDT plus two re-runs 16:39-16:55
  (the first `pcre2-interp` and `pcrec-vm` records of the day landed
  `inconclusive-load` — journal fourth session part 2 — and stay in the
  store as history; the report's newest-measured-wins rule picks the
  re-runs), `--trials 5`, quiet window with BOTH manager sessions idle,
  reporter v7. Query: `report --subbench email-specimen --version 0.2
  --format md` — 10 records: the four 35e1ab1 pcrec testees (the
  cross-pin Δ baseline), the four 36d5963 ones, and the newest pcre2
  pair. This is the [ENG-ABS] ledger (inbox I-16: the `match` regime's
  DFA/VM ratios; the search rows are the flat control) — outbox O-8.
  `.subject-grain.md` (`--grain subject`) carries the per-subject match
  rows the ledger is read on; `.tsv` the set-grain query.
- `2026-08-29-loglines-0.1-budu-ryzen1600-repin-36d5963.md` — the [B18]
  re-pin sample at pcrec **36d5963** on `loglines@0.1`: six cells
  `measured` 15:43-16:37 EDT plus one re-run (`pcrec-nocaps`, 16:55),
  same protocol, reporter v7. Query: `report --subbench loglines
  --version 0.1 --format md` — 10 records as above. This is the [OPT-K]
  ledger (inbox I-15: uuid / iso-ts / stack-frame the exercising rows,
  ipv4 / hex32-id / http-5xx the controls) and Frank's [SEL-1] row
  (`level-context` under `pcrec-auto`, a VM artifact now, vs pcre2-jit)
  — outbox O-8. `.subject-grain.md` carries the 16 KB-1 MB sweep per
  flavour; `.tsv` the set-grain query.
