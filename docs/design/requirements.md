# pcrec-bench requirements note — [B1]

STATUS: ADOPTED v3, 2026-08-25 (Frank: "narrow is fine to proceed" +
the two variant constraints in §4.5). v1 was written from the
requirements discussion (rulings R1-R11); v2 applied the R1 critic
panel's 29 findings (docs/dev/reviews/2026-08-24-r1-requirements.md);
v3 carries Frank's rulings on the two items the panel left to him.
Every ruling is Frank's unless marked "manager". APPROACH.md stays the
charter; this note refines it — where they differ this note is the
newer statement, and §11 lists exactly what it amends.

## 1. Purpose — the loop, positioning second (R1)

pcrec-bench exists first to serve pcrec's optimization loop (Frank,
2026-08-24: set up the bench → gather data across regex implementations
over a variety of patterns → pick the outliers where pcrec loses → find
GENERAL optimizations → repeat). Positioning and cross-engine learning
are second. Every design choice is judged by one question: does it
produce RELATABLE DATA TO TAKE ACTION ON — attributable, comparable,
reproducible numbers that point at a mechanism in pcrec. Published
rankings (APPROACH §8 Q4) are deferred; the report (§8) is an
engineering document. (This re-orders APPROACH §1's neutral mission
statement — an amendment, listed in §11.)

## 2. Vocabulary

- **Sub-bench** — the unit of work: a self-contained directory with a
  GOAL ("is this engine good at RFC 5322 email validation?"), holding
  one or several RELATED patterns, their subjects/data files, their
  expectations, and engine-specific notes and declared variants.
  Versioned as a unit. (§5)
- **Testee** — an (engine, version, build/run configuration) triple with
  a CATEGORIZATION (§4.3). pcrec appears as several testees. (§4)
- **Cell** — one (sub-bench version × testee) pair.
- **Run** — one harness invocation, on one machine, that measures one
  or more chosen cells. A run never means "the whole gamut" (Frank).
- **Record** — the artifact for ONE cell measured in ONE run: a
  general-setup layer plus N raw results. Identity = (testee id,
  sub-bench id + version, machine id, RFC 3339 timestamp of the run)
  plus a content hash; two same-day re-measurements are two records.
  Saved; never edited. (§6)
- **Trial** — one repetition of one measurement inside a record; raw
  trials are kept.
- **Store** — the accumulated records, from any machine and date.
- **Report** — the answer to a QUERY over the store, with filters over
  the record dimensions and a reduction of raw trials to comparables.
  (§8)
- **Comparables** — the reduced statistics a report shows per cell
  (median/min/max/stddev/spread/n — the set is OD-B1).

## 3. What is measured (R2)

Three subject regimes, each a first-class result kind; a sub-bench
declares which it exercises:

- **Large-subject throughput** — search over big subjects; bytes/second.
  Size: the email specimen's 1 MB subjects are a KNOWN-SMALLER departure
  from pcrec's own 8-64 MB convention (tests/bench/run_bench.sh,
  compare.sh at 8 MB); the standard size is set after spread at 1 MB vs
  8 MB is measured on this box (OD-B10), not inherited.
- **Short-subject search** — search over ~256-byte subjects (log lines,
  fields); per-call cost dominates; time-to-first-match and per-call
  overhead are what real workloads pay.
- **Match (compliance)** — full-string match over very-short-to-medium
  subjects, 10 through 1000 bytes in bands (OD-B2), e.g. "match this
  list of emails to see which are compliant"; accepted AND rejected
  subjects are timed.

TIMING PROTOCOL for the two short regimes: a BATCHED IN-PROCESS loop
(N iterations inside the adapter process, reporting total and per-call
time — pcrec's bdriver.c convention), never a per-call external wrapper:
this box's default `timeout` alone costs ~108.7 ms of wall per call
(pcrec docs/testing.md:2372), which would be the entire signal at these
sizes. `gnutimeout` guards the OUTER adapter process only.

Separately on every record: **compile/setup cost** — what a testee pays
before its first match — on its own axis, never folded into match time
(APPROACH §3), MEDIAN OF N WITH SPREAD like every other quantity (pcrec's
single-sample GCC-TIME swung 1.87× on a quiet box, tests/bench/CLAUDE.md
:78). Its DEFINITION is per execution-model class, stated in the testee's
adapter note: AOT (pcrec: pattern → C → gcc → loadable object, all
phases, each timed); eager JIT (the explicit compile + jit-compile calls,
e.g. pcre2_jit_compile); LAZY JIT (no separable call: cost = trial 1
minus steady state, and trial 1 is EXCLUDED from match statistics);
interpreter (the compile call). Reports never reduce compile costs of
different classes into one cell without labelling the class.

Deferred, recorded if free but not scored: memory high-water,
artifact/code size. Not ruled: a scan mode (all matches in a big
subject) as a fourth regime — OD-B3; if ruled in, it needs a
LIST-VALUED row shape (per-match events), not the single-scalar row.

## 4. Testees (R3, R4, R8)

### 4.1 Harness first, roster later

The HARNESS is what is built first (Frank). A variety of engines matters
for DESIGN — the harness must accommodate them — but the roster grows
over time, and includes regex-to-code COMPILERS as well as libraries.
APPROACH §4's candidate roster stands as the design population (libpcre2
interp and JIT, RE2, Rust regex, Oniguruma, TRE, Vectorscan, python re,
perl); nothing beyond pcrec + libpcre2 is committed for the first cut
(§10). The hand-C ceiling arm (pcrec [BENCH-CEIL]) is NOT in the first
cut; the harness must leave room for a testee whose "engine" is a
directory of per-pattern C files — the shape a compiler testee produces
too.

### 4.2 pcrec is the special case — in the ROSTER, not in the schema

The bench exists to benefit pcrec, so pcrec's VARIATIONS are set up as
separate testee engines — `--engine=auto/dfa/vm`, captures on/off, later
SIMD optimizations on/off and whatever [ENG-*] adds — each just another
roster entry with its pcrec commit pinned. The record schema stays
engine-neutral (APPROACH principle 2: pcrec's artifact is "one more file
in the pile"): every testee may populate a generic `engine_metadata`
map of ENUMERATED (name, value) pairs per pattern — pcrec's mechanism
stamps (engine chosen, prefilter on/off, rungs mask, ... read from the
artifact's STRUCTURED fields, `rx_info.engine` and the `RX_VM_*` masks,
never from the prose `RX_ENGINE_WHY` comment, which is kept only as an
unindexed diagnostic string), RE2's program size, Vectorscan's bytecode
size, ... Reports bucket outliers by these pairs — by MECHANISM, not by
pattern shape (pcrecdev1's proposal, generalised).

### 4.3 Testee and environment dimensions (enumerable where filtered)

Every record carries, as FIXED ENUMS: execution model (interpretive /
compiled-AOT / eager-JIT / lazy-JIT); automaton class (DFA-only /
NFA-simulation / backtracking / hybrid / SIMD-multipattern); openness
(open-source / closed) + license id; the CONVENTIONS the testee can
produce (Perl leftmost-first / POSIX leftmost-longest / all-ends); and
the headline configuration axes as their own fields — `captures`
(on/off), `engine_mode` (auto/dfa/vm/... per engine), `simd` (on/off/
n-a) — plus a residual `build_flags` blob kept for reproducibility ONLY,
never filtered on. As NORMALIZED IDENTIFIERS with a stated rule (OD-B4):
engine name; engine version (+ pcrec commit); hardware id; CPU model
(the /proc/cpuinfo model-name string, canonicalised); kernel; compiler.
Plus: the RUNTIME COMPILE OPTIONS the adapter passed for this sub-bench
(caseless, dotall, multiline, UTF/UCP, ... in the engine's own names) —
distinct from build flags, and the thing that makes two engines diverge
on byte-identical pattern text.

### 4.4 The outcome axis — not every rx fits every engine

Per (pattern, testee) the record states an OUTCOME from a closed set:
`compiled` / `did-not-compile` (with the engine's diagnostic) /
`crashed` / `timed-out` / `unsupported-by-declaration` (the sub-bench's
engine notes say this engine cannot express the intention). Per
(pattern, subject): `matched-as-expected` / `did-not-match-as-expected`
/ `wrong-span-or-captures` / `truncated-subject` / `crashed` /
`timed-out` / `gave-up` (crashed/timed-out added at the [B2] merge,
2026-08-25: a per-SUBJECT hang or crash is the bench's headline hazard
class and "which subject" must be recorded; `gave-up` added at schema
v1.1 the same day: the engine refused the subject on one of its OWN
resource limits — pcrec's STEPS/FRAMES/RECURSE give-ups, pcre2's
match/depth limits — with the engine's code in the diagnostic; not
timed, and counted apart from wrong answers, because a give-up is the
result the bench most wants to see) (the engine consumed
fewer bytes than offered — `consumed_length` is recorded whenever the
API exposes it, and a large-subject cell without it is marked
unverified-for-truncation). None is an error of the harness; all are
first-class results the report can filter on. Timing exists only for
`compiled` ∧ expectation-agreeing cells (§7).

### 4.5 The variant axis — same intention, adapted text or options (R3, R8; constrained 2026-08-25)

The bench is NOT limited to PCRE2-exact engines. A sub-bench's pattern
is CANONICAL (PCRE2 spelling, PCRE2 option semantics); a testee may run
a DECLARED VARIANT — the same pattern INTENTION expressed in that
engine's syntax and/or under that engine's options — recorded in the
sub-bench's engine notes, never a silent fork (pcrec R-BENCH-7). Two
CONSTRAINTS bound what a variant may be (Frank, 2026-08-25):

1. **The results must be the same — no variation in results.** A
   variant is valid only if it produces the sub-bench's expected
   answers (match/nomatch, spans, captures) on EVERY subject. There is
   no "approximates with stated differences" grade: a variant whose
   answers differ from the expectations anywhere is INVALID for that
   testee, and the cell is `unsupported-by-declaration` (or the testee
   is wrong at its own variant — either way, not timed). This also
   settles the oracle question: expectations are the CANONICAL ones,
   verified once by the sub-bench's method; a variant is checked
   against them directly.
2. **The sub-bench's objective must be achieved.** A sub-bench declares
   its OBJECTIVE — the mechanism(s) it exists to exercise (e.g. group
   subroutines, backreferences, a hazard class, a prefilter shape). A
   variant that reaches the same answers by rewriting the objective
   AWAY (e.g. inlining subroutine calls in a subroutine sub-bench)
   defeats the purpose of the bench and is not a variant: the testee
   reports `unsupported-by-declaration` for that sub-bench. The
   objective is a declared field of the sub-bench; the variant
   declaration states how it still exercises it, and that statement is
   reviewed like any other expectation.

A variant declaration therefore carries: the variant text/options; its
KIND, informational only (`syntax-only` — a mechanical re-spelling a
reviewer can check token by token — or `restructured`); how it
preserves the OBJECTIVE; a CAPTURE CORRESPONDENCE whenever group
structure or naming changes (by name / by an explicit index map) so
"same results" is checkable on captures too (OD-B9; [DD-13a] T-3); and
re-asserted HAZARD/SIZE class tags if the translation changes them
(a linear-time engine's translation of a catastrophic-backtracking case
is not measuring the hazard — and under constraint 2 such a translation
is usually not a variant at all; default = inherited). Runtime OPTION
differences (caseless, dotall, UTF defaults) are variants of the same
kind and obey the same constraints.

Reports show the variant kind beside the number, and N + pass-rate
beside any number whose coverage is below 100% (§8).

## 5. Sub-benches (R5, R6)

- A sub-bench is a DIRECTORY: goal statement; the canonical patterns
  (one or several, related); subjects — generated deterministically by
  a script with a committed manifest by default, real corpora only when
  licensing is clean; expectations with their VERIFICATION METHOD per
  case (pcrec's oracle discipline: python re base tier, libpcre2
  differential, a linear-time engine in the hazard bands,
  derived-law-plus-induction where nothing terminates); tags (feature
  tier, hazard class, size class, convention); per-engine notes,
  runtime options and declared variants (§4.5); which regimes (§3) it
  exercises.
- Sources for the first sub-benches: the RFC 5322 email specimen (pcrec
  docs/design/subroutines_measurements/email_specimen — a ready-made
  unit with 85 oracle-verified subjects + three 1 MB throughput
  subjects and a libpcre2 reference harness); imports from pcrec's
  oracle-verified .rxt corpora; hand-designed hazard-class families
  (ambiguous decomposition / K23, catastrophic backtracking,
  exact-minimum boundaries, large counts, wide alternations);
  real-world-shaped pattern/corpus pairs (log lines, URLs, email).
- Versioning: a sub-bench version is a frozen snapshot; records compare
  only within the same sub-bench version; bumping is a deliberate,
  logged event.
- Independence: a run measures one cell or a chosen few — never the
  whole gamut (Frank).

**THE FORMAT AND THE BLOCKING POINT (R6; scope RULED NARROW by Frank,
2026-08-25).** Frank ruled: block on pcrec's [DD-13] (the .rxt-grown
unified format) rather than invent an interim; "design and data gather
and stop when we're blocked". The R1 panel measured the distance:
[DD-13a] completed 2026-08-17; [DD-13b] (design) and [DD-13c] (panel +
ruling) are `not-started` with no queue position in pcrec's plan, and
the spine ahead of them ([DD-14]) is still producing waves. The RULED
scope: BLOCKED is authoring cases in a NEW cross-sub-bench grammar
(directives, includes, cascades — [DD-13]'s territory). NOT blocked:
the sub-bench DIRECTORY model (this note's own vocabulary); the record,
the adapters, the reporter; parsing TODAY'S `.rxt` as-is for imported
cases (a live, oracle-verified format that [DD-13] extends as a dialect
— R-COMPAT-1, R-BENCH-8); wrapping the email specimen's existing ad hoc
files as the first sub-bench; and a plain SIDECAR per sub-bench holding
the objective, the per-case tags, engine notes and variant declarations
— fields that are exactly R-BENCH-1..9 plus this note's additions, no
directives, no grammar, so [DD-13] absorbs them mechanically when it
lands. This note's inputs for [DD-13b] — the directory model, the
objective field, the outcome axis, the variant declaration and its two
constraints, the regime declaration — are handed to the pcrec manager.

## 6. The record (R7)

One file per record, JSONL, schema-versioned (APPROACH §8 Q2 ruled
JSONL), with a tiny validator the reporter shares. Two layers:

1. **General setup**, once: record id (§2); schema version; sub-bench id
   + version + content hash; testee (§4.3 in full, incl. runtime
   options); environment — hardware id, CPU, kernel, compiler, LOAD
   sampled BEFORE and AFTER (§9), per-core occupancy result
   (pass/fail/unavailable), quiet-box attestation; timestamp; the
   harness's own version; command lines and flags as run; record-level
   STATUS (`measured` / `harness-failure` / `inconclusive-load` — pcrec
   D14's clean-vs-not-measured distinction).
2. **Results**, N rows of two kinds: MATCH rows keyed pattern × subject-
   or-subject-set × regime × trial — outcome (§4.4), the measured
   quantity with its unit, `consumed_length` where known,
   `engine_metadata` pairs (§4.2); and COMPILE rows keyed pattern ×
   trial — the compile/setup cost with its execution-model class (§3).
   RAW trials are kept; reduction happens in the report, so the
   comparables set can change without re-measuring — for scalar-per-
   trial quantities; a future list-valued regime (OD-B3) gets its own
   row shape.

Records are never edited; a re-measurement is a new record. Size: a
realistic cell (5 patterns × ~88 subject slots × 5 trials) is ~2-6
thousand rows, ~0.5-2 MB — fine per file; the STORE needs an index or
cached reductions (OD-B6). The reporter refuses to reduce records of
different schema versions into one cell unless a declared migration
exists.

## 7. Correctness policy (R8)

APPROACH §5 stands: a timing for a wrong answer is worse than no
timing; correctness gates the scoreboard; "unsupported" is honest;
conventions are tagged and testees are scored against their own.
Tempered by §1's goal: correctness is judged on the sub-bench's
EXPECTATIONS (intention → answers), which are the CANONICAL ones for
every testee — a variant must reproduce them exactly (§4.5) — not on
pattern-text identity.
Convention is a per-CASE expectation tag (R-BENCH-5); a testee that
cannot produce a case's convention either runs a declared variant with
its own convention-tagged expectations or reports
`unsupported-by-declaration`. Disagreements between engines feed
docs/dev/upstream_findings.md; findings about pcrec go to the pcrec
manager for pcrec's known_issues.md.

## 8. Reporting (R9)

The deliverable is a REPORT that answers a QUERY over the store, e.g.
"results for sub-bench A1 considering only open-source, compiler-only".
The reporter provides filter (any §4.3 field, sub-bench id/version,
date range, hardware, record status), group, and reduce (to
comparables, OD-B1); shows outcomes, deviation grades, execution-model
class of compile costs, and — MANDATORY whenever any cell's coverage is
below 100% — N and pass-rate beside every number; excludes
expectation-failing cells from rankings by default and lists them.
Reports are self-describing (the query, the record ids, the sub-bench
versions, the reduction used, the schema versions) so they stand alone.
Delivery into pcrec is CASE BY CASE for now — the pcrec manager session
may not be running when a report is produced — until the working model
is clear (OD-B7).

## 9. Box and measurement discipline (R10)

Check load and WAIT UNTIL QUIET before a measurement run (Frank); the
box's CPU-bounded numbers lie under load (pcrec K31/[TT-10]); coordinate
with the pcrec session (BD3). Concretely: (a) `/proc/loadavg` sampled
before AND after the run, the after-sample re-checked against the
threshold — a record whose after-load exceeds it is `inconclusive-load`,
not measured (pcrec compare R3.10's lesson); (b) per-core occupancy via
`mpstat -P ALL 1 1` (installed on this box; the pattern is pcrec
docs/design/altcls_pinned_impl/pinned_measure.sh:59-64), made
MACHINE-READABLE pass/fail with `unavailable` when mpstat is missing —
recorded, never silently skipped — sampled BEFORE AND AFTER like load
(RULED 2026-08-25, schema v1.1 X13: `measured` requires `pass` on both
samples; `unavailable` or `fail` on either ⇒ `inconclusive-load`, so a
box without mpstat cannot produce a `measured` record — the intended
consequence, since [B3] measured that load1 never tripped while
occupancy refused the box 12/12); (c) what "quiet" is numerically is
MEASURED on this box, not assumed (OD-B8, a task on [B3]); (d) median of
N with spread; pinned cores after the occupancy check; (e) batched
in-process timing for the short regimes, gnutimeout on the outer
process only (§3); (f) `LC_ALL=C` in every script (pcrec learnings.md
:31 — a UTF-8 collation `sort -u` once merged 421 of 1030 distinct
patterns). Records from other machines are first-class by construction
(hardware id is a dimension) but not needed for the first cut.

## 10. First cut (R11 — agreed in substance; may change with design)

M1, provisional: this note adopted after its panel → the record schema +
validator ([B2]) → the harness core: sub-bench directory conventions,
the run-cells driver, the store layout, the quiet-box instrument ([B3])
→ two adapters, libpcre2 (interp, jit) and pcrec (auto, no-captures,
forced VM) ([B4]) → the reporter MVP (filter/group/reduce, one query)
([B5]) → the first honest report on the email specimen ([B6]). Under
the ruled NARROW blocking scope (§5) all of M1 can complete on the
specimen plus `.rxt` imports before [DD-13] lands. Roster growth,
compilers, the hand-C arm: after ([B7]).

## 11. APPROACH.md dispositions and amendments

| Q / § | disposition |
|---|---|
| §1 mission | AMENDED by §1 here: the pcrec optimization loop is the first purpose; positioning second (Frank R1). |
| §8 Q1 set format | RESOLVED IN DIRECTION (2026-08-17): pcrec [DD-13]. RULED 2026-08-24: BLOCKING, no interim grammar; SCOPE RULED NARROW 2026-08-25 (§5). |
| §8 Q2 artifact format | RULED: JSONL, schema-versioned, validator shared with the reporter (§6). |
| §8 Q3 timing depth | RULED: three subject regimes + compile/setup cost in v1; memory/size recorded if free, not scored (§3). |
| §8 Q4 public posture | DEFERRED: engineering tool first; rankings not a goal now (§1). |
| §8 Q5 first milestone | RULED in substance, provisional (§10). |

## 12. Open-decision ledger (OD-B*)

- OD-B1 — the comparables set (median/min/max/stddev/spread/n; MAD?) —
  at [B5].
- OD-B2 — the match-regime subject bands (10..1000 B cut points) — with
  the first compliance sub-bench.
- OD-B3 — a scan mode (all matches) as a fourth regime; needs a
  list-valued row shape — unruled.
- OD-B4 — (a) the FIXED ENUMS: execution model, automaton class,
  openness, convention, captures/engine_mode/simd values; (b) the
  NORMALIZATION RULES for open identifiers: engine name/version,
  hardware id, CPU model string, compiler — at [B2].
- OD-B5 — RULED 2026-08-25 (Frank): no deviation grades — a variant
  must reproduce the canonical results exactly and preserve the
  sub-bench's objective; the kind tag is informational (§4.5).
- OD-B6 — the store layout and index / cached reductions; how records
  from other machines arrive — at [B3].
- OD-B7 — feedback delivery into pcrec — case by case until the model
  is clear.
- OD-B8 — what "quiet" means numerically (load threshold, occupancy
  rule) — measured at [B3].
- OD-B9 — the capture-correspondence contract for variants and for
  engine-neutral expectations generally ([DD-13a] T-3) — with the first
  non-PCRE2 adapter; input to [DD-13b].
- OD-B10 — the standard large-subject size: spread at 1 MB vs 8 MB
  measured on this box — at [B4] (not yet measured; the sample used 1 MB).
- OD-B11 — CLOSED [B9] 2026-08-25: `_failure_label` (pcrecbench/report.py)
  now checks `crashed`/`timed-out` counts directly and names them (they
  combine with `+` when more than one reason applies to a subject's
  trials); `did-not-match-as-expected`-class outcomes still label
  `wrong`, `gave-up` still labels `gave-up`, and only a truly unnamed
  case (n_trials==0 with none of the above) falls back to `no-data`/
  `other`. Was: reporter labels `timed-out`/`crashed` cells as "(other)"
  in the excluded table; give each outcome its label (found 2026-08-25).
- OD-B12 — the occupancy gate's 10 % per-core limit vs the two manager
  sessions' own activity: two of six gate attempts in the first window
  were refused on 1-s transients (12 %, 29 %, 15 % on one core — the
  claude processes); a `--wait-quiet N` retry in the harness, and/or a
  2-3-sample gate, before the limit is loosened (found 2026-08-25).
- OD-B13 — CLOSED [B9] 2026-08-25: `report.resolve_subbench_arg`
  accepts EITHER the sidecar id (`email-specimen`) or the sub-bench
  DIRECTORY name (`email`), resolving the directory form via
  `bench/<dir>/subbench.toml`'s own `id` field (never a duplicated
  mapping); an unresolvable value passes through unchanged (matches
  nothing, same as before this ruling). Was: `--subbench` takes the
  sidecar id (`email-specimen`), not the directory name (`email`);
  accept either, or rename the directory.
- OD-B14 — CLOSED [B9] 2026-08-25 (R1): every ranking row shows the
  record's `status`; a row whose status is not `measured` is excluded
  from ranking by default (listed under its table as `not ranked:
  <testee> -- <status> (<status_detail excerpt>)`), and
  `--include-unmeasured` ranks it instead with `status` shown. Was: the
  reporter shows no record `status`; `inconclusive-load` records rank
  unmarked beside `measured` ones (seen in the [B8] sample, 2026-08-25).
- OD-B15 — CLOSED [B9] 2026-08-25 (R2, AMENDED by the manager before
  merge, same day): NEWEST *MEASURED* by default, never pooled. The
  NEWEST record whose `status` is `measured`, per (subbench@version,
  testee_id, machine), ranks -- a newer record that is NOT `measured` is
  not evidence against a measured one of the same testee and version, so
  it does NOT supersede it and is listed separately in the header as
  "newer, not measured: <record id> (<status>)"; only when no record in
  the group is measured does the newest one overall stand (itself
  unranked per R1/OD-B14 unless `--include-unmeasured`). Older-than-kept
  records are SUPERSEDED as before, named by record id in the report
  header, never silently pooled into one reduction; `--all-records` is
  unchanged and shows every record as its own row, its testee id
  suffixed `@<compact-timestamp>`. Was: two records of one testee_id in
  a query: pooled or newest? Unstated; must be ruled and printed in the
  report header.


## 13. For the next panel — attack list (v2)

1. The variant constraints (§4.5): is "objective preserved" checkable
   by a reviewer for every objective kind, or does it need a per-
   objective rule? Can a variant be `syntax-only` and still break the
   objective?
2. Is the record (§6) now sufficient for every query in §8 with no
   free-text filter? Enumerate the fields a "captures-off, compiled-AOT,
   open-source, hardware X, last 30 days" query touches.
3. The lazy-JIT protocol (§3): is "trial 1 minus steady state" sound
   when the JIT warms per pattern AND per subject shape?
4. §5's NARROW scope: does the sidecar amount to a grammar by another
   name? What is the smallest sidecar that is not?
5. §9: is the after-load re-sample enough, or must load be sampled
   during long throughput trials?
