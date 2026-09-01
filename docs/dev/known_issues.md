# pcrec-bench known issues — bugs in this project's own harness, adapters and reporter

Rows `KB-n`, never deleted; a fixed row says so in place with the commit.

## KB-1 (2026-08-25) — `runtime_options` records a bare flag whose value is the NEXT argv token as `{"--features": true}`

testees/pcrec/adapter.py splits flags on `=` only, so `["--features",
"all"]` records `{"name": "--features", "value": true}` and the value
`all` is lost (it is still in `build_flags` as text). Found by lane
b10loop. Fix: pair a bare flag with a following non-flag token. Owner:
the pcrec adapter; a one-line change plus a check. Not urgent — the
testee_id and build_flags carry the truth.

**FIXED 2026-08-25 (lane/b15floor, commit 3f5131da54cacb23203553ff9f98116c1708c46a).**
`testees/pcrec/adapter.py` gained `runtime_options(flags)`: it walks the
flag list and pairs a BARE flag (no `=`) with the token that follows it
when that token is not itself a flag — `["--features", "all"]` now
records `{"name": "--features", "value": "all"}`. An `=` flag
(`--engine=vm`) is unchanged; a trailing bare flag, or one immediately
followed by another flag, is still `{"value": true}`. Checked by
`tools/selfcheck.py`'s `check_kb1_runtime_options` (`pcrec-auto`'s
`describe()` must show `--features` paired with `"all"`).

## KB-2 (2026-08-25) — the record carries NO expected answer on an agreeing match row, so `matches m/n` cannot be derived from records; the reporter prints `n/s` until the schema says it

History: reporter v3 ([B14] R3) read the count from bench/<dir>/
expectations.tsv (a sidecar — the reporter must work from RECORDS
alone); the first draft of this row claimed the count is derivable from
`match_outcome` + `observed`. Lane b14report MEASURED that it is not: on
a `matched-as-expected` row the harness writes `observed: null` (it is
populated only on a DISAGREEING row), so deriving m from records would
undercount systematically. Reporter v4 (c07d0f6) therefore prints
`matches: n/s` and imports no sidecar. FIX (a schema/harness change,
v1.4 additive): every match row carries the EXPECTED answer class
(`expected: match | nomatch`, plus the expected span when known) — the
expectation's verification method already travels with the sub-bench,
and the record is then self-describing; the reporter's m/n returns,
records-only. Owner: the next schema/harness row; small.

## KB-3 (2026-08-30) — the reporter rendered NONE of the abi-11 [ART-SIZE] stamps (`unroll_k`, `unroll_k_why`, `max_emit_bytes`, `max_emit_code_bytes`) the adapter records on every VM artifact

Found by the bounded first-sample ledger (docs/dev/ledgers/2026-08-30-
bounded-0.1-first-sample-36d5963.md §1.6, §4(a)): `grep -c UNROLL` on
reports/2026-08-30-bounded-0.1-*-first-sample-36d5963.md is 0 while the
records carry `engine_metadata.unroll_k` etc. on all 48 VM artifacts;
the sample's only K movement (`nest3-16` = K=1 / size-model on every VM
form; `nest2-64` at the same count product stays K=8 / default) had to
be read from the JSONL. The axis bench/bounded was built for ([B11.4]
number (1)) was invisible in its own committed report. FIX IN FLIGHT:
[B19]'s lane extends the compile-legend line with `K=<k>/<why>` and
`caps=<code>/<total>` for VM artifacts (absent on DFA artifacts by
design) and a legend clause; the AFTER report is the first rendered with
it. Lesson: a stamp the adapter reads is not a finding until the reporter
renders it — [B18] (e) added five reads and zero renders.

## KB-4 (2026-08-30) — a `did-not-compile` compile row carries no `cost`: the time pcrec spends before REFUSING a pattern is not in the record

Same ledger, §1.3 / §4(b): the six `cls-upto-65535` refusal rows (auto
and nocaps, both forms, `pattern too large (NFA exceeds 131072 states)`)
have `compile_outcome`, `cost_class`, `diagnostic`, `pattern_id`, `seq`,
`trial` and no `cost` object. On a set whose give-up axis IS the refusal
([B11.4] number (3)), the refusal's cost is a number worth having: the
adapter times the pcrec invocation only on success. Fix: time the
`emit-c` phase regardless of outcome and record it on the refusal row —
check whether schema v1.3 allows `cost` beside `did-not-compile` (the
compile-row rules in docs/design/record_schema.md) before changing the
adapter; if not, it is a v1.4 item beside [B20]. Outbox O-9 ask (iv) asked
pcrec for the number from its side; I-20 ANSWERED (2026-08-30): pcrec
prints no timing on any path and has no exit convention beyond 0/1 —
the cost of a refusal is the BENCH's clock around the pcrec exec (wall
+ rusage, regardless of exit). So this is a bench-side fix: the adapter
times the `emit-c` phase on every outcome; the schema question above
decides where the number lands on a `did-not-compile` row.
**Schema half DONE at v1.4 ([B20], 2026-08-30, gate_shape_v14.md §4
S5 / ruling R-9): `compile_row`'s "no cost for a compile that did not
happen" branch is REMOVED — `cost` may sit beside any `compile_outcome`
(still REQUIRED when `compiled` and not `lazy-jit`), and the 1.4
example carries a `did-not-compile` row with a `cost`. What remains of
KB-4 is the ADAPTER half (time the pcrec exec on every outcome and
record it on the refusal row) and the reporter half — their own plan
row, which can now land without a schema change.**

## KB-5 (2026-08-31) — no testee-roster filter: a PARTIAL re-measure window cannot be scoped to "the fresh pin + the unpinned baselines" in one committed query

Found by the b22reports lane rendering the loglines@0.1 AFTER at
263b013 ([B22]'s window re-measured only 2 of the set's 6 arms). The
reporter's newest-wins dedup keys on the literal `testee_id`, which
embeds the pin string — it never supersedes ACROSS pins — so a bare
`--until` admits every surviving pcrec pin's rows (16 records: 2 pcre2
+ 35e1ab1×4 + 36d5963×4 + 96e44c2×4 + 263b013×2). No single
`--since`/`--until` range fixes it (pcre2's newest records are
chronologically OLDER than the pin rows to be excluded — two disjoint
ranges would be needed) and `--where` is AND-only on one dotted path
(cannot express "pcre2 OR pin=263b013"). The committed file
(`reports/2026-08-31-loglines-0.1-budu-ryzen1600-after-263b013.*`) is
therefore the first production CROSS-PIN report — legitimate (every
row carries its pin; the R8 Δ column fires usefully), documented in
its reports/CLAUDE.md entry, but not the single-pin AFTER shape the
96e44c2 precedent files have.

Candidate fix: a repeatable `--testee <exact testee_id>` filter (OR
within the flag's occurrences, AND'd with everything else), letting a
committed query name its roster explicitly. Not urgent: full-set
windows (the common case) never hit this. Fix travels with the next
reporter wave; the flag's spelling should mirror `run --testee`.

## KB-6 (2026-08-31) — the reporter renders NO clause for the abi-13 `dfa_scan_edge` stamp

Found by the b25reports lane on the first a7e0bdf report: every
pcrec_a7e0bdf record carries the `dfa_scan_edge` pair (range / bitmap
/ mixed / none — [OPT-5] STEP 1's mechanism stamp, [B25]), but
`pcrecbench/report.py` has no legend clause for it, so a reader of the
committed report cannot see WHICH machine shape a counted-class cell
ran without opening the record. Same shape as KB-3 (the abi-11
[ART-SIZE] stamps, fixed in a reporter wave); fix travels with the
next reporter wave alongside KB-5's `--testee` roster filter. The
mechanism-bucketing rules ([B16] R1-R8) may also want the scan-edge
value in the `sel=` line's company — design call for that wave, not a
patch tonight.
