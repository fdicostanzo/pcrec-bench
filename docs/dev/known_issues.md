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

**FIXED 2026-09-01 (lane b28kb4, [B28], adapter + reporter halves).**
`testees/pcrec/adapter.py`'s `_compile_one` already computed `t1 - t0`
around the pcrec exec (phase 1, `emit-c`) BEFORE checking its exit
code; the fix is carrying that number forward on both `did-not-compile`
paths — pcrec's own refusal (the `-p rx` exit) and the gcc/clang
refusal one level down (pcrec succeeded; only the compiler refused) —
as `phase_seconds=[{"emit-c": t1 - t0}]`, the SAME one-dict-per-trial
shape `phase_seconds` carries for a `compiled` result (harness.py's
existing `phase_seconds[t-1]` read needed no change). `pcrecbench/
record.py`'s `compile_row` gained the non-`compiled` branch that turns
that into `cost = {"total_ns": ...}` — DELIBERATELY carrying no
`cost.phases` array: rule X12 requires `phases[].name` to equal the
testee's declared `compile_phases` EXACTLY whenever the key is present
at all, and a refusal by construction never ran every declared phase,
so `total_ns` alone (summed over whatever phases were actually timed —
today always just `emit-c`) is the only schema-legal shape, matching
`schema/examples/...20260830T120000Z.jsonl`'s own KB-4 row. The
`compile_cost_definition` text gained one clause naming this (I-20's
ruling: pcrec prints no timing on any path, so a refusal's cost is the
BENCH's clock). Reporter: `_phase_medians` now also reads a
`did-not-compile` row's `cost.total_ns` — recognised by the absence of
a `phases` array — as its `emit-c` contribution, so the compile-cost
table's `emit-c ns` column shows a real number on a testee whose ONLY
rows for a pattern are refusals (`gcc ns`/`load ns` stay `-`, correctly
— those phases never ran). `REPORTER_VERSION` UNCHANGED at `v11
(2026-09-01)`: no record in `store/` carries a `cost` on a
`did-not-compile` row yet (checked directly), so every committed report
renders byte-identical; the rendering fires the next time a refusing
cell is measured. `pcrecbench/tests/test_report.py` gained
`test_kb4_refusal_cost_in_phase_medians` (62 total): the firing case,
a compiled row's shape unchanged (control), a did-not-compile row whose
`cost` DOES carry a `phases` array is NOT read for `emit-c` (control —
that shape belongs to a compiled row), a did-not-compile row with no
`cost` at all renders as before (control — the shape every stored
record still has), and the rendered table row end to end.
`tools/selfcheck.py`'s `check_mechanism_stamps` extends its existing
bounded `cls-upto-65535` refusal-by-name block: the `CompileResult`
itself carries the timed `emit-c` phase, the `record.compile_row` built
from it carries a positive `cost.total_ns` with NO `phases` key and
validates against the schema's own `compile_row` definition, and a
compiled witness's row is checked to carry its cost UNCHANGED in shape
(four new checks; 221/221 total, `make check` green: check-schema
4/72/0, check-harness 221/221, 62 reporter tests).

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

**FIXED 2026-09-01 (lane b28report, [B28], commit 18ad03a0cdfdfe730befc77493288d8a4cda52ed).**
`pcrecbench/report.py` gained `--testee TESTEE_ID` exactly as the
candidate fix above proposed: repeatable, exact match on the literal
`testee.testee_id`, OR'd within its own occurrences and AND'd with
every other filter. One addition beyond the candidate: an id matching
NO record anywhere in the loaded store (checked before any other filter
narrows the selection) REFUSES, naming the unknown id(s) and the known
ones, rather than silently rendering an empty report — every other
filter here narrows silently, but a committed roster query is worth
protecting from a typo that would otherwise produce a quietly-empty
table. Printed in the Query header as `testee=<id>` per occurrence.
`REPORTER_VERSION` bumped to `v11 (2026-09-01)`; the flag is additive
(no committed query used it, so no existing report's rendering moved).
`test_testee_filter_kb5` (`pcrecbench/tests/test_report.py`) covers the
narrow, the OR, the AND-with-another-filter case, the unknown-id
refusal and the known+unknown mix. Documented in `report.py`'s module
docstring, `--help`, `pcrecbench/CLAUDE.md` and `reports/CLAUDE.md`.

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

**FIXED 2026-09-01 (lane b28report, [B28], commit 18ad03a0cdfdfe730befc77493288d8a4cda52ed).**
`_dfa_scan_edge_display` renders `edge=<range|bitmap|mixed|none>` on
the legend line, placed directly after the `dfa: scan=... prefilter=...
table=... [offsets=...]` composite clause — the SAME scope
(`dfa-scan`: every artifact whose DFA scan is stamped, VM hybrids
included, testees/pcrec/adapter.py's `STAMP_SCOPE`) as that clause and
`offsets=`, not `dfa_match`'s narrower dfa-only scope; conditional
(absent on a forced-VM artifact, a non-hybrid VM artifact, or any
record from before abi 13). A legend note names the four values,
printed once under the lines that carry the clause. `REPORTER_VERSION`
bumped to `v11 (2026-09-01)`; every committed report under `reports/`
regenerated — the twelve `pcrec_a7e0bdf` reports' mechanism legends
change (the `edge=` clause and the new note), no other report's
rendering moves. `test_dfa_scan_edge_legend_kb6` covers the firing
case, the VM-hybrid case (edge present, no `match=`), the forced-VM
control (no scope, no clause), the abi-12 control (no pair), and the
note's presence/absence.

The MECHANISM-BUCKETING QUESTION this row's last paragraph raised is
answered as a RECOMMENDATION, not a code change: scan-edge is a fact
about the machine's transition-table SHAPE, stamped unconditionally
regardless of whether `auto` fell back to anything, so folding it into
`_engine_sel_display`'s fallback bucket would conflate two independent
facts (a `range` scan sits on a `sel=selected` artifact or a
`sel=overflowed-dfa` one alike); it also does not obviously belong in
the [B16] R1-R8 ranking-group bucketing, which groups rows for RANKING
rather than carrying a per-row legend fact (same footing as
`dfa_prefilter`, never bucketed on). See `report.py`'s module
docstring, "[B28]" section, for the full reasoning — left for the
manager to rule on if a future finding wants rows grouped by scan-edge
shape.

## KB-7 (2026-09-01) — the record schema's `free_text` cap (8192 characters) is UNJUSTIFIED and may limit the bench unnecessarily — Frank's ruling owed

`schema/record.schema.json` defines `free_text` as `{"type": "string",
"maxLength": 8192}` and eighteen record fields are declared with it —
descriptions, notes, diagnostics, option strings, raw captured output,
and `patterns[].canonical_text`, the reproducibility-only copy of the
pattern bytes. NO document records why 8192: not `record_schema.md`,
not the r2 schema review, not `decisions.md` (grep'd 2026-09-01). It
is OUR limit, not an engine's: libpcre2 compiled every affected pattern.

It bit for the first time today ([B11.2], bench/altwide): four
wide-alternation rungs are 8.7-24 KB of pattern text, so every cell
over them would have been measured and then REJECTED by the validator
on write. The lane's fix (b5b0248) keeps the cap and OMITS
`canonical_text` above it (never truncates; sha256 + content_hash
remain the identity), with a gate reading the cap from the schema. That
is correct under the cap as written, but Frank's reading (2026-09-01,
~20:0x): "it seems arbitrary … I am unclear if we are limiting ourselves
unnecessarily". The discussion this needs:

1. WHAT the cap protects. Candidates: record size in the store (a 24 KB
   pattern copied into every record that measures it — altwide's is
   ~50 KB of pattern text per record, against records of ~2-4 MB of
   rows, so <2 %); the reporter's and validator's memory (jsonschema
   validates every record on load — length is not the cost, count is);
   a stray binary blob landing in a text field. None of these is 8192-
   shaped; a 64 KB or 1 MB bound would protect them equally.
2. WHICH fields deserve a bound at all. `canonical_text` arguably
   deserves NONE: it is a copy of a committed file whose size the
   sub-bench already bounds, and a record that cannot carry its own
   pattern is a record that is harder to read alone — the field's one
   purpose. Diagnostics (a compiler's error text on a 24 KB pattern can
   itself exceed 8 KB) and `raw` captures are the other two to consider.
3. WHAT a change costs. `maxLength` is a validator rule: raising it is
   a schema version bump under record_schema.md §4's rule-revision
   clause (v1.4 → v1.5), every `schema/examples/` still validates, and
   NO existing record changes (a looser bound rejects nothing it
   accepted). The [B11.2] omission gate then becomes the check that
   the field is present iff the pattern fits the NEW cap — or is
   retired if `canonical_text` becomes unbounded.

RECOMMENDATION for the ruling: raise `free_text` to a bound that is
clearly about hygiene, not content (1 MiB), keep the omission fallback
as the schema's documented behaviour for anything above it, and record
the reason in record_schema.md this time. Until ruled: the cap stands,
altwide's four rungs carry no `canonical_text`, and nothing measured
depends on it. Plan row [B30].

## KB-8 (2026-09-02) — an OPEN `--since` query drifts on every store growth: unpinned pcre2 ids re-select the newest record, and a `--testee` roster cannot bound TIME (the correction to KB-5's fix)

Found by the [B26] (c) re-render invariant (lane b26reports, f66f2cd)
over the 48 report files committed before the wave: SIX drifted — all
three `-after-96e44c2` groups (bounded-0.1, email-specimen-0.2,
loglines-0.1) pulled the 2026-09-02 night's pcre2 records in through
their open `--since 2026-08-30T11:00:00Z`. The loglines group had
ALREADY been pinned to a six-id `--testee` roster by [B28] (KB-5's
fix) and drifted anyway: the two libpcre2 testee_ids carry no pin, so
newest-measured-wins picks whichever pcre2 record is newest at render
time. A roster bounds WHICH ids; only `--until` bounds WHEN. Fixed for
the three groups with `--until 2026-08-30T15:00:00Z` (their `-repin`
siblings' own bound); no number, ranking, verdict or record list moved.
RULE (reports/CLAUDE.md, the wave paragraph): every committed query
carries BOTH a `--since` and an `--until`; a `--testee` roster is for
scoping arms, never for freezing time. Beside it, the smaller nit: the
report header's `record source: store/index.tsv (N candidate file(s))`
line moves on every store growth, so a byte-identical re-render is
only ever "identical modulo that line" — reports/CLAUDE.md rules that
acceptable; a future reporter wave may print the FILTERED count (which
a bounded query keeps stable) instead of the store's total.
