# pcrec-bench requirements note — [B1]

STATUS: DRAFT v1, written 2026-08-24 from the requirements discussion
with Frank (first session, pcrecdev2). Every ruling below is his unless
marked "manager"; the "(Frank)" tags carry his words or a close
paraphrase. Next: the D6 critic panel (§12's attack list), then Frank
adopts. Until adopted this is a proposal; APPROACH.md stays the charter
and this note refines it — where they differ, this note is the newer
statement and APPROACH.md §8 is amended by §11 below.

## 1. Purpose — the loop, positioning second (R1)

pcrec-bench exists first to serve pcrec's optimization loop (Frank,
2026-08-24: set up the bench → gather data across regex implementations
over a variety of patterns → pick the outliers where pcrec loses → find
GENERAL optimizations → repeat). Positioning and cross-engine learning
are second. Every design choice is judged by one question: does it
produce RELATABLE DATA TO TAKE ACTION ON — attributable, comparable,
reproducible numbers that point at a mechanism in pcrec. Published
rankings (APPROACH §8 Q4) are deferred; the report (§8) is an
engineering document.

## 2. Vocabulary

- **Sub-bench** — the unit of work: a self-contained directory with a
  GOAL ("is this engine good at RFC 5322 email validation?"), holding
  one or several RELATED patterns, their subjects/data files, their
  expectations, and engine-specific notes and declared pattern
  adjustments. Versioned as a unit. (§5)
- **Testee** — an (engine, version, build/run configuration) triple with
  a CATEGORIZATION (§4.3). pcrec appears as several testees. (§4)
- **Record** — the artifact produced by applying ONE sub-bench to ONE
  testee on ONE machine on ONE date: a general-setup layer plus N raw
  results. Saved; never edited. (§6)
- **Store** — the accumulated records, from any machine and date.
- **Report** — the answer to a QUERY over the store, with filters over
  the record dimensions and a reduction of raw results to comparables.
  (§8)
- **Comparables** — the reduced statistics a report shows per cell
  (median/min/max/stddev/spread/trial count — the set is OD-B1).

## 3. What is measured (R2)

Three subject regimes, each a first-class result kind; a sub-bench
declares which it exercises:

- **Large-subject throughput** — search over big subjects (MB scale);
  bytes/second; the classic axis.
- **Short-subject search** — search over ~256-byte subjects (log lines,
  fields); per-call cost dominates; time-to-first-match and per-call
  overhead are what real workloads pay.
- **Match (compliance)** — full-string match over very-short-to-medium
  subjects, 10 through 1000 bytes in bands (bands TBD, OD-B2), e.g.
  "match this list of emails to see which are compliant"; both the
  accepted and the rejected subjects are timed.

Separately on every record: **compile/setup cost** — the time a testee
pays before its first match (pcrec: gcc once; JIT: warm-up; interpreter:
pcre2_compile per pattern) — recorded on its own axis and never folded
into match time (APPROACH §3). Deferred, recorded if free but not
scored: memory high-water, artifact/code size. Manager's open question
carried, not ruled: a scan mode (all matches in a big subject) — OD-B3.

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

### 4.2 pcrec is the special case

The bench exists to benefit pcrec, so pcrec's VARIATIONS are set up as
separate testee engines — `--engine=auto/dfa/vm`, captures on/off,
later SIMD optimizations on/off and whatever [ENG-*] adds — each just
another roster entry with its pcrec commit pinned. A pcrec record
additionally carries the artifact's MECHANISM STAMPS per pattern
(engine chosen, `RX_VM_PREFILTER`, `RX_VM_RUNGS`, ...; pcrecdev1's
proposal) so outliers bucket by mechanism, not by pattern shape.

### 4.3 Testee dimensions (enumerable, not free text)

Every testee record carries: engine name; engine version (and pcrec
commit); build configuration (flags, features); **categorization** —
execution model (interpretive / compiled-AOT / JIT) and automaton class
(DFA-only / NFA-simulation / backtracking / hybrid / SIMD-multipattern);
**openness** (open source / closed) with license; matching CONVENTION
(Perl leftmost-first / POSIX leftmost-longest / all-ends); and the
environment: hardware id, CPU model, kernel, compiler (for compiled
testees), date. Controlled vocabularies (OD-B4) so reports can filter
reliably (§8).

### 4.4 The outcome axis — not every rx fits every engine

Per (pattern, testee) the record states an OUTCOME from a closed set:
`compiled` / `did-not-compile` (with the engine's diagnostic) /
`crashed` / `timed-out` / `unsupported-by-declaration` (the sub-bench's
engine notes say this engine cannot express the intention) — and per
(pattern, subject): `matched-as-expected` / `did-not-match-as-expected`
/ `wrong-span-or-captures`. None is an error of the harness; all are
first-class results the report can filter on. Timing exists only for
`compiled` ∧ expectation-agreeing cells (§7).

### 4.5 The syntax-variant axis — same intention, adapted text (R3, R8)

The bench is NOT limited to PCRE2-exact engines. A sub-bench's pattern
is CANONICAL (PCRE2 spelling); a testee may run a DECLARED VARIANT of
it — the same pattern INTENTION expressed in that engine's syntax,
"modified a certain amount" (Frank) — recorded in the sub-bench's
engine notes, never a silent fork (pcrec R-BENCH-7). Each variant
carries a DEVIATION GRADE (manager's sharpening, grades OD-B5):
syntax-only rewrite / semantically-equivalent restructuring /
approximates the intention with stated differences. Reports show the
grade beside the number; an expectation mismatch on an "approximates"
variant is a stated difference, not an engine bug.

## 5. Sub-benches (R5, R6)

- A sub-bench is a DIRECTORY: goal statement; the canonical patterns
  (one or several, related); subjects — generated deterministically by
  a script with a committed manifest by default, real corpora only when
  licensing is clean (manager's default, Frank: "these sound fine to
  start"); expectations with their VERIFICATION METHOD per case (pcrec's
  oracle discipline: python re base tier, libpcre2 differential, a
  linear-time engine in the hazard bands, derived-law-plus-induction
  where nothing terminates); tags (feature tier, hazard class, size
  class, convention); per-engine notes and declared variants (§4.5);
  which regimes (§3) it exercises.
- Sources for the first sub-benches: the RFC 5322 email specimen
  (pcrec docs/design/subroutines_measurements/email_specimen — a
  ready-made unit with 85 subjects + three 1 MB throughput subjects and
  a libpcre2 reference harness); imports from pcrec's oracle-verified
  .rxt corpora; hand-designed hazard-class families (ambiguous
  decomposition / K23, catastrophic backtracking, exact-minimum
  boundaries, large counts, wide alternations); real-world-shaped
  pattern/corpus pairs (log lines, URLs, email).
- Versioning: a sub-bench version is a frozen snapshot; records compare
  only within the same sub-bench version; bumping is a deliberate,
  logged event.
- **Pattern/case FORMAT: BLOCKING on pcrec [DD-13]** (R6 — Frank: "i'm
  ok with blocking actually. the rxt should be coming pretty soon").
  No interim carrier is invented here. This project's needs are already
  stated to [DD-13] as R-BENCH-1..9; this note adds the sub-bench
  directory model, the outcome axis, the variant/deviation axis and
  the regime declaration as inputs for [DD-13b] (handed to the pcrec
  manager). Until the format lands: design the harness and the record,
  gather what can be gathered with the specimen's existing files, and
  STOP at the blocking point rather than fork a format.
- Independence: records are gathered one (sub-bench × testee) cell at a
  time or a chosen few — never the whole gamut (Frank). A run's unit is
  the cell.

## 6. The record (R7)

One file per record, JSONL, schema-versioned (APPROACH §8 Q2 ruled
JSONL), with a tiny validator the reporter shares. Two layers:

1. **General setup**, once: record id; schema version; sub-bench id +
   version + content hash; testee (§4.3 in full); environment — hardware
   id, CPU, kernel, compiler, LOAD at start and end, per-core occupancy
   check, quiet-box attestation; date/time; the harness's own version;
   command lines and flags as run.
2. **Results**, N rows: per pattern × subject-or-subject-set × regime ×
   trial — outcome (§4.4), the measured quantity with its unit, and for
   pcrec the mechanism stamps. RAW trials are kept; reduction happens in
   the report, so the comparables set can change without re-measuring.

Compile/setup cost is a result row of its own kind. A harness failure
(could not run) is a record-level status distinct from any result
(pcrec D14's clean-vs-not-measured distinction). Records are never
edited; a re-measurement is a new record.

## 7. Correctness policy (R8)

APPROACH §5 stands: a timing for a wrong answer is worse than no
timing; correctness gates the scoreboard; "unsupported" is honest;
conventions are tagged and testees are scored against their own. Tempered
by §1's goal: correctness is judged on the sub-bench's EXPECTATIONS
(intention → answers), not on pattern-text identity, so a declared
variant is comparable (§4.5). Disagreements between engines feed
docs/dev/upstream_findings.md; findings about pcrec go to the pcrec
manager for pcrec's known_issues.md.

## 8. Reporting (R9)

The deliverable is a REPORT that answers a QUERY over the store, e.g.
"results for sub-bench A1 considering only open-source, compiler-only".
The reporter provides filter (any §4.3 dimension, sub-bench id/version,
date range, hardware), group, and reduce (to comparables, OD-B1); shows
outcomes and deviation grades beside numbers; excludes
expectation-failing cells from rankings by default and lists them.
Reports are self-describing (the query, the record ids, the sub-bench
versions, the reduction used) so they stand alone. Delivery into pcrec
is CASE BY CASE for now — the pcrec manager session may not be running
when a report is produced — until the working model is clear; no fixed
pipeline is designed yet.

## 9. Box and measurement discipline (R10)

Check load and WAIT UNTIL QUIET before a measurement run (Frank); the
box's CPU-bounded numbers lie under load (pcrec K31/[TT-10]); coordinate
with the pcrec session (BD3). Record load and occupancy in the record;
median of N with spread; gnutimeout on everything; pinned cores after
an occupancy check; pcrec learnings.md §1 in full. Records from other
machines are first-class by construction (hardware id is a dimension)
but not needed for the first cut.

## 10. First cut (R11 — agreed in substance; may change with design)

M1, provisional: this note adopted after its panel → the record schema +
validator ([B2]) → the harness core: sub-bench directory conventions,
the run-one-cell driver, the store layout ([B3] re-scoped from "the set"
to "the sub-bench model and the store", format-blocked for authoring)
→ two adapters, libpcre2 (interp, jit) and pcrec (auto, no-captures,
forced VM) ([B4]) → the reporter MVP (filter/group/reduce, one query)
([B5]) → the first honest report on the email specimen ([B6]). Roster
growth, compilers, the hand-C arm: after ([B7]). Design considerations
may reorder this; the plan rows are updated when they do.

## 11. APPROACH.md §8 dispositions

| Q | disposition |
|---|---|
| Q1 set format | RESOLVED IN DIRECTION (2026-08-17): pcrec [DD-13]. RULED 2026-08-24: BLOCKING, no interim (§5). |
| Q2 artifact format | RULED: JSONL, schema-versioned, validator shared with the reporter (§6). |
| Q3 timing depth | RULED: three subject regimes + compile/setup cost in v1; memory/size recorded if free, not scored (§3). |
| Q4 public posture | DEFERRED: engineering tool first; rankings not a goal now (§1). |
| Q5 first milestone | RULED in substance, provisional (§10). |

## 12. Open-decision ledger (OD-B*)

- OD-B1 — the comparables set (median/min/max/stddev/spread/n; whether
  a robust dispersion like MAD is preferred) — decide at [B5].
- OD-B2 — the match-regime subject bands (10..1000 bytes: which cut
  points) — decide with the first compliance sub-bench.
- OD-B3 — a scan mode (all matches in a big subject) as a fourth regime
  — manager's question, unruled.
- OD-B4 — the controlled vocabularies for categorization, openness,
  convention, hardware id — decide at [B2].
- OD-B5 — the deviation grades for declared variants — decide at [B2]/
  first non-PCRE2 adapter.
- OD-B6 — the store layout (directory of records vs an index file; how
  records from other machines arrive) — decide at [B3].
- OD-B7 — the feedback delivery into pcrec once the model is clear —
  case by case until then.
- OD-B8 — what "quiet" means numerically (load threshold, occupancy) —
  measure on this box at [B4].

## 13. For the critic panel — attack list

1. Is the sub-bench/record/store/report vocabulary complete and
   non-overlapping? Where does a "run" live?
2. Does the record (§6) carry everything a report (§8) needs for every
   query shape Frank named, with no free-text dimension?
3. Does the outcome axis (§4.4) cover every way a testee can fail to
   produce a comparable number? What about partial support (compiles,
   matches, but ignores an option)?
4. Does the variant/deviation axis (§4.5) let a bad variant hide a bad
   engine — or a good engine hide behind "approximates"?
5. Is BLOCKING on [DD-13] (§5) consistent with the first cut (§10)? What
   exactly can be built and measured before the format lands, and what
   is the precise blocking point?
6. Compile/setup cost (§3): is one number honest across AOT/JIT/
   interpreter, or does each need its own definition?
7. Does anything here contradict APPROACH.md's four principles or pcrec
   D52's boundaries (not pcrec's gate; dependencies here; pin by commit)?
8. Measurement validity: what in §9 is asserted rather than measured on
   this box?
