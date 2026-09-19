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

**RULED 2026-09-02: Frank agrees with the recommendation** ("agree",
inbox; also stated directly at the top of this lane's brief). **CLOSED
2026-09-02 (lane b30cap, [B30], schema v1.5).** `schema/record.schema.json`
`$defs.free_text.maxLength` raised 8192 → 1,048,576 (1 MiB);
`x-record-schema-version` and `pcrecbench.record.SCHEMA_VERSION` both
1.4 → 1.5; the omission fallback for `patterns[].canonical_text` above
the cap is UNCHANGED (never truncates — record_schema.md §10.1, the
sha256 + `subbench.content_hash` stay the identity), just further away.
The reasoning this KB owed is now recorded in `record_schema.md` §4.1,
under the new 1.4 → 1.5 paragraph: a MINOR bump by §4's plain first
rule, not the rule-revision clause X13 needed, because `maxLength` is a
single JSON Schema number applied with no version branching — a string
valid under the old 8192 bound is valid under the new one, so no
record's meaning or verdict moves for any earlier minor. The two
`diagnostic` fields KB-7 point 2 flagged as candidates keep their own,
separate 8192 bound — Frank's ruling addressed `free_text` by name,
and they are not `$defs/free_text` fields. No new `schema/examples/`
record was added, following the 1.3 precedent (an additive bump with no
new field needs no new fixture); the accept-side witness for the wider
bound is bench/altwide's real 8.7-24 KB patterns (`tools/selfcheck.py`
`check_pattern_text_cap`, now asserting `canonical_text` PRESENT on
them), and the omission arm now needs — and gets — a SYNTHETIC >1 MiB
pattern built inside the check, since nothing in this bench's corpus
reaches a megabyte of pattern text. The two other checks built on the
OLD cap's shape (`check_note_length_guard`, `check_status_sentence_
never_elided`, R-4) are scaled to actually exceed the new cap rather
than asserting against a number that no longer overflows.

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

**REPORTER HALF FIXED 2026-09-02 (lane b32rep, [B32] (b), reporter v12).**
The `record source` line's count is now `len(selected)` -- every record
THIS QUERY's own filters admit (subbench/version/regime/machine/since/
until/where/testee/synthetic-inclusion, `matches_filters`), computed in
`build_report` -- instead of `len(paths)`, the WHOLE store's candidate
count `main()` used to bake into `args._source_desc` before calling
`build_report`. Worded `(N record(s) matching this query)`. Stable under
any store growth OUTSIDE the query's own bounded range, same property
the `--since`/`--until` rule above buys back for the query's CONTENT;
this closes it for the header's own COUNT. `args._source_desc` now
carries the bare store label (`main()`); `build_report` appends the
count. `test_source_desc_query_filtered_kb8` (`pcrecbench/tests/
test_report.py`) covers a narrower `--testee` filter changing the count
and a record OUTSIDE that filter not moving it. `REPORTER_VERSION`
bumped to `v12 (2026-09-02)`; every committed report regenerated (the
count and the version line move on every file -- see `reports/
CLAUDE.md`).

## KB-9 (2026-09-02) — the compile phase is named `gcc` on a `-clang` testee

[B24] kept the phase NAME fixed (`emit-c` / `gcc` / `load`) so a clang
testee's phase column compares against its gcc sibling's, and put the
compiler in `build_flags` and the testee_id (`cc-clang`). A reader of the
compile-cost table therefore sees a `gcc` column on `pcrec-vm-clang`. The
ledger of the first cc window (2026-09-02 §5) reads it correctly but had
to say so. Options for a reporter wave: rename the phase to `cc` with the
compiler in the legend, or keep `gcc` and add a per-row `cc=` note where
the testee's cc is not gcc. Plan row [B32] (b).

**FIXED 2026-09-02 (lane b32rep, [B32] (b), reporter v12).** Chosen fix:
keep the phase name `gcc` exactly as the record has it (no record
touched -- the RECORD is correct by [B24]'s own design, comparing a
clang testee's phase against its gcc sibling's needs the shared name)
and append a per-row `(clang cc)` note to that one `gcc ns` cell wherever
the ROW's own testee declares a non-gcc `cc`, plus one legend line (once
per table) stating the rule. `_cc_from_testee_id` reads `config_extra`'s
`cc-<name>` token, which testees/pcrec/CLAUDE.md ("Composition with cc")
guarantees is the FIRST axis when present (chartering order, cc first
then the caps, append-only) -- so `startswith("cc-")` is enough, with no
case yet in the store where a second axis's own slug could be mistaken
for it. `test_cc_clang_phase_note_kb9` covers the firing case (the
clang row's cell, distinct from its gcc sibling's in the SAME table) and
controls (an explicit `cc-gcc` token, a non-pcrec testee_id, an
unparseable one, and a gcc-only table carrying neither the suffix nor
the note). `REPORTER_VERSION` bumped to `v12 (2026-09-02)`; only the
`2026-09-02-*-cc-1989c62.*` reports' rendering actually moves beyond the
version/count lines (the only committed reports with a `cc-clang`
testee) -- see `reports/CLAUDE.md`.

## KB-10 (2026-09-02) — `quick --vs <testee>` ERRORS when the comparison arm did not compile, instead of printing `refused`

Found by lane b31cap while smoke-testing the raised-cap axis: `quick
--subbench altwide --pattern w-512 --regime search_short --testee
pcrec-vm-bigcap --vs pcrec-vm` writes BOTH records correctly (the bigcap
one `measured` and validated, carrying the raise in its testee_id, its
runtime_options and the artifact's own stamps; the plain one a first-class
`did-not-compile` row with pcrec's refusal text and zero match rows), then
fails at the comparison step (`pcrecbench/__main__.py`, "expected one cell
for (w-512, short-subject-search) ... found 0") because the `--vs` arm has
no measured cell. Pre-existing, not introduced by [B31]; it bites on every
altwide wide rung and on bounded's 65535 rung. The fix belongs in `quick`
(or the shared reduction): a `--vs` arm whose only row is a refusal prints
`refused (<diagnostic>)` in the comparable's place and exits 0 — the
records are already right. Queued on plan.md [B32] (h).

**FIXED 2026-09-02 (lane b32rep, [B32] (b)/(h)).** `pcrecbench/
__main__.py`'s cell-lookup loop is now `_split_quick_cells` (a
module-level, unit-tested helper `cmd_quick` calls): a `--vs`-only arm
(never the PRIMARY `--testee` arm, index 0, always the caller's own
target) whose only row for (pattern, regime) is a `did-not-compile`
compile row becomes a `refused` entry instead of an error, printed as
`refused (<diagnostic, first line>)` in the comparable's table row (and
its ratio line) with the record's path still shown, `quick` exiting 0.
An empty cell for any OTHER reason -- a typo'd pattern/regime, two forms
both present, or the primary arm itself refusing -- is still the old
"expected one cell ... found N" error. `pcrecbench/tests/test_quick.py`
(new file, 7 tests) covers the firing case, the diagnostic's
first-line-only truncation, and three controls (a clean two-arm run
unaffected, a primary-arm refusal still erroring, an unexplained empty
`--vs` cell still erroring). Not `report.py` -- no `REPORTER_VERSION`
implication, but bundled into the same [B32] (b) reporter-v12 commit
since it is the same plan row and lane.

## KB-11 (2026-09-06) — one `pcrecbench report` invocation takes ~11 min on a 154-record store: the loader re-validates EVERY record against the JSON Schema through jsonschema's `referencing` resolver

OBSERVED (lane b39read, the [B39] AFTER's reports): a single committed
query (`report --subbench loglines --version 0.1 --since ... --until ...
--testee ... --testee ...`, 2 records selected) ran 10 min 51 s wall on
this box; the lane's in-process rendering of all five groups took one
store load of 640 s and then 91 s for the fifteen files. The same
mechanism makes `make check-report` 7-10 min (its `_load_real_store()`
runs once per process) and made a 600 s gnutimeout kill it beside
check-harness on 2026-09-06 (journal, eleventh session part 2). A
standalone `faulthandler` dump caught `test_plain_entry_capacities_r1`
inside `referencing/_core.py:pointer` at 60 s — the time is schema
`$ref` resolution per record, not the reduction or the rendering.

WHY IT MATTERS: the loader validates the WHOLE store before the
`--subbench`/`--since`/`--testee` filters apply (records the query will
never rank), and the cost is linear in store size — 154 records today,
growing by 6-30 per window. The reporter's correctness is unaffected
(validation is what makes a record admissible; X1..X33 must still run
on every record that RANKS).

FIX DIRECTION (not started; queue on the reporter's next wave with
KB-8/KB-9 — plan.md [B13]/[B12]): (a) filter by path/index BEFORE
validating — `store/index.tsv` already carries subbench, version,
testee_id, machine and timestamp, so the query's roster can be cut
there and only the selected records validated (the index is
regenerated by `pcrecbench index` and is the store's own contract);
(b) build the `referencing` registry / compiled validator ONCE per
process (`jsonschema.Draft202012Validator` with a pre-resolved registry)
instead of per record, if the validator is re-created per call in
`schema/validate.py`; (c) a `--no-validate` is NOT acceptable — the
"wrong answers excluded" guarantee rides on validation. Measure before
and after with the same 154-record store; the acceptance number is the
loglines query above under 60 s.

## KB-12 (2026-09-06) — bench/syntax@0.1's first-sample window ran six cells and wrote ZERO records: pattern/subject ids were never checked against the record schema before a measurement ran

OBSERVED (plan [B36]'s first-sample window, 2026-09-06): all six cells
(bench/syntax@0.1 × its six pinned testees) ran to completion -- 259
minutes wall -- and every one was refused at `store.write()`'s
validator, after the fact: the record schema's id rule
(`schema/record.schema.json`'s `$defs/slug`,
`^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`) forbids uppercase, and the set had
ten uppercase pattern ids (`anc-A anc-G asr-K cls-N mod-J mod-U msc-C
msc-R msc-X rec-R`) and two uppercase subject ids (`f-CAT f-Cat`) that
nobody had checked before the run. The first refused cell's validator
output alone ran 31,747 lines (jsonschema's own per-record error
detail, repeated across the whole record). Nothing else in the harness
checks a sidecar's or a manifest's ids before a cell runs: `make
check`'s one-cell validator smoke (`check_floor_pattern`'s scratch-tier
`quick` cell) exercised bench/email's ids only, so it could not have
caught this on any OTHER set either.

WHY IT MATTERS: a set's ids are typed once at authoring time and never
touched again until a record tries to carry them -- by which point
every trial of every pattern × subject × regime has already run. A
sub-bench with a bad id is not a slow failure, it is a WASTED one: the
harness has no way to tell the author before the box time is spent.

**FIXED 2026-09-06 (lane b36ids, plan [B36]).** Two changes, delivered
together: (1) bench/syntax@0.1's twelve ids RENAMED to lowercase,
case-unambiguous forms following the set's own `-uc`/`-lc` convention
(bench/syntax/CLAUDE.md item 4) -- `anc-A`→`anc-a-uc`,
`anc-G`→`anc-g-uc`, `asr-K`→`asr-k-uc`, `cls-N`→`cls-n-uc`,
`mod-J`→`mod-j-uc`, `mod-U`→`mod-u-uc`, `msc-C`→`msc-c-uc`,
`msc-R`→`msc-r-uc`, `msc-X`→`msc-x-uc`, `rec-R`→`rec-r-uc`,
`f-CAT`→`f-cat-uc`, `f-Cat`→`f-cat-mixed`; pattern BYTES, subject BYTES
and every expectation answer are UNCHANGED (ids only, git-tracked as
pure renames for the `.rx` files), so NO version bump -- no record ever
carried the old ids, the refused ones never entered the store; (2) THE
PRE-FLIGHT, in the harness: `pcrecbench.subbench.Subbench.__init__` now
checks every pattern and subject id against the schema's `$defs/slug`
rule (`check_id`, `_slug_pattern` -- the regex is READ from
`schema/record.schema.json`, never retyped) and raises `SubbenchError`
naming the id, the set and the rule, so `run`/`quick` refuse in under a
second. `tools/selfcheck.py` gained `check_id_preflight` (a GENERIC gate
over every `bench/*/`, plus the negative control both directions for
both id kinds, on a synthetic never-committed sidecar built fresh under
`build/`) and `check_floor_pattern`'s one-cell validator smoke was
WIDENED off bench/email alone to enumerate every set (one `quick` cell
per set's own floor pattern) -- closing the second gap the incident
found (KB-11's neighbour: `make check`'s validator smoke had never
covered any set but the first one built). `make check-harness`: 324 → 337 (9 new `check_id_preflight` lines + 4
from widening `check_floor_pattern`'s one-cell validator smoke from a
single bench/email line into one line per set). See
docs/dev/lanes/b36ids_report.md for the full validation and the actual
printed total.

## KB-13 (2026-09-07) — BOTH drivers' find-all loop reports a MID-LOOP GIVE-UP as a shorter match count, with no indication a give-up happened: five of six testees can vanish silently from a ranking

OBSERVED (lane b36read's [B36] syntax@0.1 outlier read, ledger
docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md §1.1, Q1): nine
cells (`rec-r-uc`/`rec-1`/`rec-name` × the three regimes) read `expected
116 non-overlapping match(es); observed 5` on `pcre2-jit` AND all four
pcrec arms. A read-only ctypes probe reproducing the drivers' own
advance rule against the same subject and `libpcre2-8` returns
`PCRE2_ERROR_JIT_STACKLIMIT` (-46) at the sixth match start, after five
spans identical to the interpreter's. Both drivers share the defect,
independently written:

    testees/pcre2/driver.c:321-340 (find_all loop):
        int rc = p_match(code, s->buf, s->len, pos, opts, md, NULL);
        if (rc < 0) { if (count == 0) rc_final = rc; break; }
        ...
        count++;

    testees/pcrec/driver.c (find_all loop, same shape):
        if (r == 0) break;
        if (r < 0) { if (count == 0) giveup = r; break; }
        ...
        count++;
    nmatch = count;   /* the record's reported match count */

A negative return AFTER the first match (`count > 0`) is silently
discarded: `giveup`/`rc_final` is only set when the give-up is the VERY
FIRST call (`count == 0`). The loop `break`s either way, and `nmatch`
(what the record reports as the answer) is just the count of matches
found before the give-up struck — indistinguishable from a subject that
genuinely has only that many matches. Verified against source directly
(not inferred); confirmed present in both `testees/pcre2/driver.c` and
`testees/pcrec/driver.c` on 2026-09-07.

WHY IT MATTERS: this is not confined to bench/syntax. Any find-all
regime, on any sub-bench, where a mid-subject give-up occurs (a
recursion/backtrack limit, a step budget, a JIT stack limit) produces a
record whose `match_outcome` and match count look like a normal,
correct, SHORTER match count rather than a give-up — no `wrong-answer`
flag, no `give-up` outcome, just quietly fewer matches than the oracle
expects on later calls, while earlier calls in the same loop (the ones
before the give-up) are correct. Whether this reached any PRIOR sample
(bench/loglines, bench/bounded, bench/altwide all have find-all
regimes) is UNKNOWN — not investigated here; a scope check across
existing store records for `nmatch` values disagreeing with their
oracle's expected count, specifically in find-all regimes, is owed
before any prior sample is trusted where this could bite. The fix (per
Q1) is to distinguish NOMATCH from any other negative code on every
non-first iteration, not just the first, and stamp a give-up outcome
accordingly.

STATUS: OPEN. Not fixed here (a read lane's finding; fixing driver
semantics changes what future records look like and needs the
harness's own judgment on backward compatibility — a manager decision,
not a lane's). Reported to pcrec's side is NOT needed (this is our own
driver code, not pcrec's).

## KB-14 (2026-09-07) — pcrec's driver hard-codes the reported match START to 0 on the whole-subject (`anchored`) form, discarding the real start `\K` or a lookbehind produces

OBSERVED (lane b36read, same ledger §1.2, Q2): `asr-k-uc` (`key=\K\w+`)
on subject `f-kv` reads `[0,9]` on all four pcrec arms where the oracle
(and libpcre2, correctly) reads `[4,9]` — `\K` resets the reported match
start past the `key=` prefix, and pcrec's driver never reads it:

    testees/pcrec/driver.c (whole-subject/`anchored` branch):
        long long r = do_match_caps(s->buf, s->len, 0, caps);
        if (r < 0) {
            if (r < -1) giveup = (int)r;
        } else if ((size_t)r == s->len) {
            first_s = 0;              /* <-- hard-coded, not caps[0][0] */
            first_e = (long)r;
            memcpy(firstcaps, caps, (size_t)ncaps * sizeof *caps);
        }

`caps` DOES carry the real span (it is memcpy'd into `firstcaps` for the
capture-group check the same line), but `first_s`/`first_e` — the pair
the record reports as the top-level match span — are set from the
call's own end position and a hard-coded 0, never from `caps[0]`. This
is pcrec's driver ONLY; libpcre2's whole-subject path is unaffected.

WHY IT MATTERS: every whole-subject (`(?:...)\z`) pcrec record's
reported match START is wrong whenever the pattern can start its
reported match somewhere other than byte 0 of the attempt — `\K`,
lookbehind-based start adjustment, or (per Q3 below) anything the `\z`
wrapper itself perturbs. This is a CORRECTNESS bug in the driver, not a
timing one — a wrong-answer flag should already have caught it wherever
the schema's validator compares match spans against the oracle; whether
it silently passed anyway on any PRIOR whole-subject sample (only
bench/syntax exercises `\K` and lookbehind starts extensively; bench/
email's and bench/bounded's whole-subject forms may not) is unchecked.

STATUS: OPEN. Fix: read `first_s`/`first_e` from `caps[0]` in the
anchored branch, same as the search branch already does.

## KB-15 (2026-09-07) — the `(?:<pattern>)\z` whole-subject WRAPPER changes pattern semantics for three syntax families, not just the two the design anticipated

OBSERVED (lane b36read, same ledger §1.3, Q3): the wrapper this bench
uses to force a whole-subject match ([B15]'s floor-pattern design) is
LEXICAL — it wraps the pattern text, not the match call — and that
reaches inside the pattern for constructs whose meaning depends on
where the pattern ends or what encloses them. Three confirmed failure
modes across three mechanism families:
1. `(?R)` recursing into the WRAPPER itself rather than the bare
   pattern — a wrong answer, predicted by P2 before the run and
   confirmed exactly, with clean controls.
2. `\K` — KB-14 above (a driver bug compounding a wrapper design
   question: even a correctly-read `caps[0]` reports the span the
   WRAPPED pattern produced, and whether that is the semantics the
   census wants is a separate, still-open question).
3. `mod-x` (`(?x) c a t # comment`) becomes UNCOMPILABLE under the
   wrapper — pcrec refuses with "missing closing ) for group" because
   the `(?x)` free-spacing mode's `#`-comment silently swallows the
   wrapper's own `)\z`, a refusal libpcre2 does not share (it must
   handle the same text differently) — R1 in the ledger, the one
   `built`-per-seed refusal that is not in the 14-row unsupported
   block.

WHY IT MATTERS: this is a DESIGN question for the wrapper mechanism
itself (should it wrap textually, or should whole-subject matching be a
call-time flag instead?), not a single bug to patch — patching Q1/KB-13
and Q2/KB-14 does not resolve `(?R)`'s wrong answer or `mod-x`'s
refusal, both of which are the wrapper reaching where it should not.

STATUS: OPEN, unscoped — a design question for whoever owns the
whole-subject wrapper mechanism next, not a landing-bar fix.

## KB-16 (2026-09-08) — the reporter validates the WHOLE store on every load: ~750 s and ~3.6 GB RSS at 160 records / 597 MB, and the harness's memory heuristic kills it as a tracked background task

OBSERVED (lane b13pre, the [B13.2] regeneration, six attempts in one
night): `report.load_all` runs the jsonschema validator over every
record `store/index.tsv` names, regardless of the query's own filters
(`reports/CLAUDE.md`'s [B32] (b) entry measured ~39 s for 26 records at
[B12]; the syntax@0.1 records are ~15 MB each, six of them, and the
store is now 160 records / 597 MB on disk). Measured 2026-09-08:
`Loaded 160 records ... in 745.7s`, peak RSS ~3.6 GB. Under the Bash
tool's tracked `run_in_background`, the harness "stopped [the task]
because the system is running low on memory" TWICE during that load
(free 5 GB, available 11 GB, no kernel OOM), each time with the kill
notification arriving late or never; the same script survived every
time under `setsid`. Any consumer that loads the store pays this:
`make check-report` (7-10 min), every `report` CLI invocation, and the
[B13] interpreter's `make check-interpret` if it were ever pointed at
the live store (interpreter_v1.md §8(2) already pins it to a frozen
fixture snapshot for this reason).

WHY IT MATTERS: the cost scales with the store, which only grows; a
one-report render already costs 12+ minutes of validation for records
the query discards, and the memory footprint makes the operation
un-runnable as a tracked task on this box's page-cache state.

STATUS: **CLOSED (2026-09-11, [B41] (e), lane `b41`)**. Candidate (a)
taken: `report.py`'s `main()` now reads `store/index.tsv` as ROWS
(`discover_index`, not just paths) and prefilters candidate records with
`index_row_could_match` — every INDEX-DERIVABLE half of `matches_filters`
(subbench, version, machine, testee, since/until, all six columns
`store.index()` already writes from the same `setup` fields
`matches_filters` reads) — BEFORE calling `load_all`, so a record the
query's own filters could not possibly admit is never opened, never
`_read_lines`'d, never jsonschema-validated. `synthetic` and `--where`
stay decided on the loaded record exactly as before (not index columns);
`matches_filters` still runs, unchanged, on every record the prefilter
admits (defence in depth against a stale index). The KB-5 unknown-
`--testee` refusal keeps reading the WHOLE store's known ids (not
narrowed by the prefilter) via a new `build_report(..., known_testee_ids=)`
override, so a typo'd id still lists every id actually in the store, not
just the prefiltered slice's. KB-8's filtered-count header line is
unaffected (still `len(selected)`, computed after `matches_filters`, and
the prefilter can only ever admit a superset of what that function keeps).

**MEASURED, before/after, on ONE committed query** — the exact filters
from `reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv`'s
own header (6 records selected out of a store of 160 — `store/
index.tsv` unchanged in size since this KB's own finding; these six are,
per `reports/CLAUDE.md`, the LARGEST records in the store,
35,859-41,800 rows each, so this is a worst-case-record-size
demonstration). "Before" = `report.py` reverted to the commit before
this fix (`HEAD~1` at the fixing commit), same box, same store, same
query, `/usr/bin/time -v`, nothing else running (a competing tracked
`test_report` suite run was found mid-measurement and killed by PID
before the numbers below were taken):

| | wall clock | peak RSS | uptime/load at start |
|---|---|---|---|
| BEFORE | **765.67 s** (12:45.67; user 757.42 s) | **4,027,148 KB (~3.84 GiB)** | `13:02:36 up 29 days, 14:09, load average: 2.62, 1.83, 1.09` |
| AFTER | **116.78 s** (1:56.78) | **762,940 KB (~745 MiB)** | `13:00:21 up 29 days, 14:07, load average: 2.03, 1.25, 0.81` |
| ratio | **×6.55 faster** | **×5.28 less RSS** | — |

Both runs' TSV output `cmp`s BYTE-IDENTICAL against the committed
report (and against each other) — the fix changes what is opened, never
what is rendered. `pcrecbench/tests/test_report.py` gains
`test_kb16_query_never_opens_other_subbench_files` (76 reporter-side
tests total): monkeypatches `report._read_lines` to record every path
opened, runs `report.main()` against the real store with a `--subbench`
filter naming the smallest-record-count subbench, and asserts no opened
path belongs to any OTHER subbench (with a control that refuses to run
if the store held fewer than two subbenches). `make check-report`'s own
whole-store re-render-and-diff pass ran DETACHED once at the end
(the boilerplate's rule for any store-loading run) and is the
whole-corpus version of the same byte-identity proof.

Candidates (b) (validate lazily / cache by sha256) and (c) (load large
free-text fields only when the grain needs them) are NOT taken — (a)
alone gets the worst case measured here to under two minutes, and both
remaining candidates add real complexity (a cache invalidation story,
a lazy-field reader) for a query shape ((b)/(c) would only help a query
that still selects a great many records) this project's committed
queries do not exhibit today. Revisit if a committed query ever needs
to select most of a store larger than today's 160 records.

## KB-17 (2026-09-12, FIXED 2026-09-16 by [B42] restart step (4)/b42repin) — BOTH drivers' and the oracle's find-all advance rule `pos = max(end, pos+1)` DOUBLE-COUNTED an empty match found AHEAD of the scan position (was latent: no committed expectation was ever affected)

REPORTED by pcrecdev1 (live, 2026-09-12 evening, while absorbing O-26:
the W23 `.rxt` delivery will state the match-count rule BY REFERENCE to
pcrec's match-api §3.1, "which means one adapter edit on your side")
and CONFIRMED here the same hour against the libpcre2 oracle
(`pcrecbench.oracle_pcre2._find_all_impl`, the SAME rule both drivers
implement — `testees/pcre2/driver.c:338`, `testees/pcrec/driver.c:728`,
documented in `pcrecbench/adapters.py`'s protocol block as the
throughput regime's operation):

    (?=a)  on b"xax"   -> first (1, 1), count 2      standard walk: 1
    (?=a)  on b"aXa"   -> first (0, 0), count 3      standard walk: 2
    a*     on b"xax"   -> first (0, 0), count 4      standard walk: 4  (control)

MECHANISM: after an EMPTY match at `s > pos` (the engine skipped ahead
from the scan position to a zero-width hit), `end == s > pos` so
`pos = end = s` — and the next call finds the SAME empty match at `s`
again before `pos+1` finally moves past it. The `+1` is applied to the
SCAN position, not to the MATCH position; the rule is right only when
the empty match lies AT `pos`. The control (`a*`) is right by that
accident: a pattern that can match empty at EVERY position always
matches at `pos` itself.

WHAT IS AFFECTED TODAY: nothing committed. Census 2026-09-12 (oracle
`pattern_info().min_length == 0` over every pattern of every set, then
which of those run in a throughput regime): altwide 0/33, email 0/3,
loglines 0/11, syntax 0/95 (its lookaround witnesses all carry a
consuming body), bounded 17/43 — the `cls-upto-*` ladder (fifteen
rungs), `cls-lazy-16384` and `grp-upto-1024`, every one a `{0,N}` shape
that matches at every position, so its empty matches are always AT
`pos`. Their 37 throughput rows whose FIRST match is empty state
`nmatches = len + 1` (16385 / 4097 on `t-digits-016k` / `-004k`), the
all-positions walk — the same number the standard rule gives. Every
stored throughput count is therefore both internally consistent
(oracle and drivers share the rule, `expectations.py:19`) AND equal to
the standard count.

WHERE IT WILL FIRE: any throughput pattern that is zero-width at SOME
positions only — a lookaround-only pattern, a bare `\b`/`^`/`$` under
multiline, `(?=...)`-led shapes — i.e. exactly the wild-provenance
population [B42]'s capability set imports (docs/design/
capability_set_v1.md). A count off by the number of skipped-ahead empty
matches would be a WRONG ANSWER on every testee at once (all share the
rule), invisible to the expectation chain (the oracle shares it too),
and a cross-engine comparison of a number no other tool reproduces.

FIXED (2026-09-16, [B42] restart step (4), lane b42repin): §3.1's
protocol adopted BY REFERENCE in the three places that carried the
rule — `testees/pcre2/driver.c`, `testees/pcrec/driver.c`, and
`pcrecbench/oracle_pcre2.py`'s `_find_all_impl` — plus the driver-
protocol docstring in `pcrecbench/adapters.py` and the two comments in
`pcrecbench/expectations.py` / `bench/email/gen_expectations.py` that
restated the old (wrong) rule in prose. The advance is now off the
match's own reported START, never off the previous scan position: a
non-empty match still resumes at its END; an empty one resumes one past
its START (`start + 1` — this bench compiles no `utf8` artifact, so
match_api.md §3.1.1's `next_pos` residual is that constant everywhere
here).

Every set's `expectations.tsv` was re-derived under its
`gen_expectations.py --check` after the fix: email (501 rows), loglines
(1,364), bounded (4,300), altwide (2,772) and syntax all re-derive
BYTE-IDENTICAL to the committed files — ZERO committed counts moved,
confirming the census above by re-measurement rather than by
prediction alone. In particular bounded's 17 `{0,N}` min-length-0
patterns are the CONTROL this fix is judged against: their empty
matches are always AT `pos`, so the old and new rules agree there by
construction, and their counts did not move.

`tools/selfcheck.py`'s `check_kb17_find_all_advance` (new, `make
check-harness`) pins the two lookaround witnesses BY VALUE against the
libpcre2 oracle — `(?=a)` over `b"xax"` now reads first `(1, 1)`, count
`1` (was `2`); `(?=a)` over `b"aXa"` now reads first `(0, 0)`, count `2`
(was `3`); `a*` over `b"xax"` is unchanged at count `4` (the control) —
with the deliberately-wrong rule reproduced inline (never by calling
production code) as the negative control proving the retired rule still
gives the OLD wrong counts (2, 3), so the fix is shown to have changed a
real number rather than being a no-op.

## KB-18 (2026-09-17, FIXED same day by lane b42repdiag) — the reporter's did-not-compile diagnostic was truncated to its first line, dropping the rest silently past a stated marker

Flagged by `docs/dev/ledgers/2026-09-17-capability-0.1-first-a770139e.md`
§2 Finding F: `wild-waf-crs-942500-comment-obfuscation` (a WAF
SQLi-obfuscation detection rule whose own subject matter is the C-comment
idiom `/*!...*/`) does not compile on pcrec's DFA route — a genuine
pcrec DFA-emitter code-generation bug, not a declared cap: the generated
`artifact.c` embeds the pattern's own literal bytes, unescaped, inside a
human-readable annotation comment naming the matched byte sequence at
each DFA state, and the pattern's own `/*!*/` terminates that C comment
early, desynchronizing the rest of the file (two cascading errors follow
from the one `*/`). The ledger's author had to read the FULL gcc
diagnostic out of the raw record
(`store/records/capability@0.1/pcrec_a770139e_auto-caps-simdna/…jsonl`)
because the report's own `not ranked:` bullet read `"the artifact did
not build: [truncated, diagnostic continues]"` — `_diagnostic_first_line`
(`pcrecbench/report.py`, since [B12] R10) partitioned the diagnostic on
its first `\n` and discarded everything after it, printing that marker
in place of the rest rather than the rest itself. The marker made the
loss VISIBLE, which is more than silent truncation would have done, but
the information itself was still gone from the one place ([B41]'s own
premise) a reader is meant to be able to trust without re-opening the
JSONL.

FIXED (2026-09-17, lane b42repdiag): `_diagnostic_first_line` is
REPLACED by `_diagnostic_full` (`pcrecbench/report.py`) — the record's
own `diagnostic` string, VERBATIM and IN FULL, bounded only by
`record.FREE_TEXT_MAX` (1,048,576 characters, schema v1.5's hygiene
bound, [B30]) as a defensive ceiling (the schema caps a compile row's
`diagnostic` at 8192 characters today, well under it — this ceiling
exists for a future schema revision, not for any record this project
can write now). Both call sites — the markdown `not ranked: ...
did-not-compile (<diagnostic>)` bullet, and the TSV's `did_not_compile`
row — are one-physical-line contexts, so an embedded newline, tab or
backslash is rendered VISIBLY (backslash-escaped, backslash escaped
FIRST so the mapping is losslessly reversible rather than merely
readable) instead of executed; nothing is dropped to make that true.
`pcrecbench/__main__.py`'s OWN, separate `_diagnostic_first_line`
(KB-10's `quick --vs` refused-arm one-liner, a genuinely one-line-by-
design CLI printout) is a different function at a different call site
and is UNCHANGED.

`REPORTER_VERSION` bumps `v16 (2026-09-08)` → `v17 (2026-09-17)`; every
committed report under `reports/` and its `.interpretation.md` sidecar
is regenerated in the same commit (see `reports/CLAUDE.md` for the
diff classification — mechanically, only the version-stamp line and the
one pattern's did-not-compile diagnostic cell move, on the two committed
capability@0.1 reports). `pcrecbench/tests/test_report.py` gains
`test_diagnostic_full_kb18` (a multi-line diagnostic survives whole with
visibly-escaped newlines in both render formats; controls: an unchanged
single-line diagnostic, `None`/empty rendering `(no diagnostic)`, and a
diagnostic already containing the literal two characters `\n` rendering
distinguishably from a real embedded newline); `test_reporter_version_pin`
re-pins `v17`.
## KB-19 (2026-09-17, FIXED same day by [B42] L6b; filed as KB-18 in lane l6bre2, RENUMBERED at merge — KB-18 is the reporter truncation above) — `run.driver_compiler` joined EVERY driver built in the process, not just the current record's own, once a second compiler FAMILY existed on the roster

`pcrecbench/driverrun.py`'s `DRIVER_BUILDS` dict is process-global,
keyed by driver binary path, and `driver_build_provenance()` read it
UNSCOPED — every entry any adapter had registered so far in the current
process, joined with `", "` — into `run.driver_compiler`. This was a
silent no-op invariant for the project's whole prior history: every
testee's driver was built by the SAME compiler family (`gcc`), so "every
compiler used so far in this process" and "the compiler THIS record's
driver used" always happened to be the same one value.

`testees/re2/`'s driver ([B42] L6b) is the first built by a DIFFERENT
family, `g++`. A `quick --vs` comparing an `re2-*` testee against a
`pcre2-*` one (both testees prepared in ONE process) populated both
adapters' entries before either record was built, so the SECOND record's
`run.driver_compiler` read `"g-15.2.0, gcc"` — both, comma-and-space
joined — and failed `schema/validate.py`'s single-token pattern
(`^[a-z0-9][a-z0-9._-]*$`, which also excludes the bare `+` in a literal
`"g++"` even before the join). Reproduced: `quick --subbench email
--pattern orig --regime search --testee re2-default --vs pcre2-interp
--subjects 5` rejected the SECOND (pcre2-interp) record at
`store.write()` with exactly that message.

A separate, smaller issue in the same path: `g++`'s raw name cannot
satisfy the pattern at all (the `+` characters), so `run.driver_compiler`
must go through `record_schema.md §6.7`'s shared `env.canon_compiler`
normalization (the SAME function `environment.compiler` uses) rather
than the raw `$CC`/`$CXX` token — `"g++ (Ubuntu 15.2.0-16ubuntu1)
15.2.0"` normalizes to `"g-15.2.0"` (the `++` run collapsing to one
separator), which the pattern accepts. `record_schema.md §6.7`'s own
text already flags the underlying gap ("one `compiler` field may be the
wrong shape once a non-C testee lands") — this is that flagged case
landing for a C-FAMILY toolchain that is not literally `gcc`, not yet
the fully non-C case (rustc, a python interpreter) the note anticipated.

**Fixed** two ways: (1) `testees/re2/adapter.py`'s `prepare_driver`
registers `env.canon_compiler(env.compiler_raw(cxx))`, never the raw
`cxx` string, into `DRIVER_BUILDS`; (2) `pcrecbench/harness.py` clears
`DRIVER_BUILDS` immediately before `adapter.prepare(testee_id, workdir)`
for the CURRENT testee — since `prepare()` always re-registers its own
entry immediately afterward, this scopes the dict to one testee's own
build(s) by construction and is a strict no-op for every existing
single-compiler-family testee. Verified: the same `quick --vs` command
above now writes two valid records (`run.driver_compiler` = `"g-15.2.0"`
on the re2-default record, `"gcc-15.2.0"` on the pcre2-interp one), and
no existing committed record or test exercises two compiler families in
one process, so the fix moves no existing number.
## KB-20 (2026-09-17, FIXED by lane b43giveup) — the driver protocol's BATCHED iteration loop re-paid a per-call give-up's cost `iters` times, turning a cheap `gave-up` outcome into a `timed-out` one purely as an artifact of how many times the harness happened to ask

(NUMBERING NOTE: KB-18 is lane/b42repdiag's diagnostic-truncation row and
KB-19 is lane/l6bre2's `DRIVER_BUILDS` row, both pending merge as of this
lane's start — renumber on conflict at merge; this row's own content does
not depend on either number.)

REPORTED by pcrecdev1's F3 investigation (2026-09-17, their
`docs/dev/lanes/f3search_report.md`) and CONFIRMED here against the
records it names: `store/records/capability@0.1/pcrec_a770139e_{auto,vm,
vm-in}-caps-simdna/…jsonl`, pattern `evil-alt-nested`, subject
`rd-evil-alt-near-miss`. All three cells' five trials read
`match_outcome: timed-out`, `diagnostic: "the per-subject alarm fired"`
(re-verified in this lane, byte for byte, before the fix — every trial
of every one of the three testees).

THE BUG, precisely (pcrecdev1's numbers, confirmed against the driver
protocol's own text at the top of `pcrecbench/adapters.py`): pcrec's step
budget is one-per-search-call and fires CORRECTLY and CHEAPLY on its own
terms — a typed give-up in ~2.5-2.8 s per call on the 18-byte subject.
But the driver's per-subject loop (`testees/pcrec/driver.c`:
`for (it = 0; it < iters; it++) { ... }`) never breaks early on a
give-up — it resets and retries every iteration, keeping only the LAST
answer — and the calibration probe sizes this subject's batch at
`iters` ≈ 200 (`PROBE_ITERS["search_short"]`, `pcrecbench/harness.py`).
So EVERY one of ~200 iterations re-pays the ~2.7 s give-up: ≈540 s
against the 60 s per-subject alarm (`--subject-timeout`). From the
harness's point of view "the first timed iteration never returned" —
because the BATCH never returned, though each underlying call did — and
the row is recorded `timed-out` where the true outcome is `gave-up`.

WHY THIS IS THE BENCH'S OWN HAZARD, not pcrec's: the pcre2 reference arms
on the SAME (pattern, subject) recorded `gave-up` (via their own
match-limit refusal) only because pcre2's per-call give-up is cheap
enough that its ~200-iteration batch fits inside the 60 s alarm. So,
before this fix, the RECORDED OUTCOME for one (pattern, subject, regime)
cell depended on the ENGINE's own per-call give-up cost — exactly the
kind of harness artifact `APPROACH.md`'s comparator exists not to
produce: a scoreboard column ("timed-out" vs "gave-up") that measures
the harness's batching choice, not the engine.

FIXED (2026-09-17, lane b43giveup): `pcrecbench/harness.py` gains
`_first_call_outcomes` (one iters=1 driver call over every subject in a
regime, BEFORE any batch-sized call runs) and `measure_regime_cell`
(the new seam `run_cell`'s per-regime loop calls in place of the old
direct `calibrate()` + `adapter.measure()` pair). A subject whose first
call gives up is pulled out of `calibrate()`'s probe (so its inflated
per-iteration time can no longer skew the median that sets `iters` for
every OTHER subject in the cell either) and out of the batched timed
run, and is instead measured on its own, at iters=1, for every trial —
a give-up is now TERMINAL for its own (pattern, subject, regime) cell,
never re-paid `iters` times. The recorded outcome is still the DRIVER's
own typed answer (`giveup:<code>[:<name>]`, classified `gave-up` vs
`crashed` by `harness.classify_giveup`'s existing range rule) — nothing
about the row's SHAPE changes, because `record.match_row` never stamps a
`timing` block on any outcome but `matched-as-expected`; a give-up row
carries no timing today or after this fix. This is a WALL-TIME and
CORRECTNESS fix (the outcome itself stops depending on the engine's
give-up cost), never a schema change.

THE NO-OP ARGUMENT for every cell with no give-up subject: when
`_first_call_outcomes` finds nothing, `measure_regime_cell` calibrates
and measures over the FULL, UNCHANGED subject list — the exact two
calls (`calibrate()`, then `adapter.measure()`) `run_cell` made before
this fix, in the same order, over the same list. The only difference
from the pre-fix code path is the one extra iters=1 probe call, whose
rows are inspected and discarded: nothing it returns feeds calibration,
`n_iters`, or any row the function returns. Checked directly in
`tools/selfcheck.py`'s `check_giveup_not_batched` (below) with a
same-subject-list control run alone vs. inside a two-subject cell: both
reach the identical `n_iters` and the identical per-subject answers.

`tools/selfcheck.py`'s `check_giveup_not_batched` (new, `make
check-harness`) exercises the fix in ISOLATION against a stub
`Adapter.measure()` (never pcrec, never a compile — seconds, not the
540 s the bug's own arithmetic would cost to reproduce for real): a
give-up subject is NEVER handed a call asking for more than one
iteration; every trial's row for it reads `giveup:...` BY NAME (dense
1..N) and `outcome_for` judges it `gave-up`; a sibling "every subject
gives up" cell does not crash; and the DISTINCTNESS from `timed-out` is
checked against `check_subject_timeout` (unmodified by this fix: its
`s-hang` witness never emits a `giveup:` answer at all, so
`_first_call_outcomes` never touches it — the two paths are shown
separate, never merged into one).

RE-MEASURE CONSEQUENCE: the three `capability@0.1` first-sample cells
named above (`evil-alt-nested` × `pcrec-auto-caps`/`pcrec-vm-caps`/
`pcrec-vm-in-caps`) carry pinned, canonical `timed-out` rows that would
read `gave-up` under the fixed harness. Pinned records are APPEND-ONLY
(record_schema.md; this repo never edits or deletes one) — the
re-measure rides the NEXT capability window (the F1-fix checkpoint pin),
alongside the I-72 erratum cells it will already be re-running.

OWED: `make check-harness` (324+ checks, ~20 min; NOT run in this lane
per the manager's hard rule — pcrec's solo battery owns the box) —
exact command `make check-harness` from the repo root after `pin.sh`'s
build is in place; `check_giveup_not_batched` is verified standalone
above and is included in `main()`'s check list so it runs as part of
that target once granted.

## KB-21 (2026-09-18, FIXED same night by the manager) — the re2 adapter's `runtime_options` entries were BARE STRINGS (`'longest_match=true'`), not the schema's `named_value` objects; the re2-longest capability first-sample cell measured in full and was then refused at `store.write`

The overnight capability window's sixth cell (`re2-longest`, 2026-09-18
00:02 EDT) ran every trial and then failed validation at the write
(`testee.runtime_options.0: 'longest_match=true' is not of type
'object' [SCHEMA]`) — the never-write-invalid rule working exactly as
stated (harness contract §4 step 5): nothing invalid reached the store,
the rejected record is preserved under the cell's `.staging-*` directory,
and the window recorded `attempt 1 rc=1` and moved on. Why it survived
until the first real cell: `pcre2`'s and `pcrec`'s `describe()` blocks
emit `[]`/object-shaped entries here, so no prior testee ever exercised
a NON-EMPTY entry's shape, and no smoke check validates a new adapter's
`describe()` block against the schema before its first canonical write
(`re2-default` carries `[]` and wrote clean in the same window). Fix:
the entry is now `{"name": "longest_match", "value": true}`
(`testees/re2/adapter.py`). FOLLOW-UP worth a lane's time: a
`check-harness` arm that validates EVERY discovered testee's
`describe()` block against the schema's `testee` definition (one quick
synthetic record per config would have caught this at merge time, not
in a window) — the same class of gap KB-12 closed for pattern/subject
ids.

## KB-22 (2026-09-18, FIXED same lane) — `scripts/regen_sidecars.py` recovered `report`/`index`/`predictions` from a sidecar's own stamp but not `subject_grain`, silently dropping R-BUCKET-DOMINATED's input on every regeneration

Found by lane `b53regen` mid-wave, the v18 full-report regen's own
sidecar-refresh step: `regen_one()` parsed `stamp.get("report")`,
`stamp.get("index")` and `stamp.get("predictions")` to rebuild the exact
`pcrecbench interpret` invocation a committed sidecar was generated
with, but never read `stamp.get("subject_grain")` — so a sidecar whose
ORIGINAL stamp named a `.subject-grain.tsv` input (R-BUCKET-DOMINATED's
own second file, [B47]) regenerated WITHOUT `--subject-grain`, and
R-BUCKET-DOMINATED's whole section (33 firings on the capability-after
sidecar, 8 aggregated by testee) silently disappeared — the rendered
file still passed the skill's own determinism check (it agreed with
itself, just not with the ORIGINAL), so nothing failed loudly. Invisible
until now because only ONE sidecar carried a `subject_grain` stamp
before 2026-09-17 ([B47]'s own email-specimen witness, which itself was
generated WITHOUT `--subject-grain` from the start — a separate,
pre-existing gap this KB does not claim to explain) and this script was
never run against a `subject_grain`-stamped sidecar until this lane's
own regen wave hit the two capability sidecars ([B48], 2026-09-18).

Fix: `regen_one()` now also reads `stamp.get("subject_grain")` (absent
or `(none)` handled exactly like `predictions`; a stamped path that no
longer exists on disk is a NAMED failure, `... its stamped subject_grain
input is missing: ...`, never a silent narrowing) and passes
`--subject-grain <path>` when present. Verified: both affected sidecars
(`2026-09-18-capability-0.1-...-after-cf0962e3`,
`...-ext-first-cf0962e3`) regenerate with R-BUCKET-DOMINATED's section
restored, `subject_grain`/`subject_grain_sha256` stamped correctly, and
every line below the stamp byte-identical to the pre-regen committed
content but for the expected reporter-version/hash movement; `make
check-interpret` 149/149 after the fix (was 143/149 — section 3's
sha256 re-derive check catches a sidecar that silently lost content just
as reliably as one that never regenerated at all). FOLLOW-UP worth a
lane's time: a `make check-interpret` control that plants a synthetic
`subject_grain`-stamped sidecar and asserts `regen_sidecars.py`
round-trips it — this class of gap (an input silently dropped on
regeneration, self-consistent but wrong) is exactly what KB-18's
`reports/CLAUDE.md` lesson ("a legitimate class the classifier missed")
warns a next wave to check for, and this KB is that warning's second
instance in as many waves.
