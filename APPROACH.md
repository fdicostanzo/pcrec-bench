# pcrec-bench — a comparative regex-engine benchmark

MAINTAINED high-level statement of what the bench is, how it works, its
architecture and its focus (Frank, 2026-08-25: keep this current with the
requirements; keep details in the referenced files). Seeded 2026-08-17;
rewritten 2026-08-25 after the requirements were adopted. Detail lives
in: `docs/design/requirements.md` (the adopted requirements, every
ruling cited), `docs/design/record_schema.md` (the record), later design
notes per component, `docs/dev/decisions.md` (BD1..), and
`docs/dev/pcrec_references.md` (what this project builds on in pcrec).

## 1. Mission and focus

Measure regex engines against each other — pcrec, the ahead-of-time
PCRE→C compiler, among them — on a test population that is deliberately
harder and wider than the usual microbenchmark fare, and produce
RELATABLE DATA TO TAKE ACTION ON.

The first customer is pcrec's optimization loop: gather data across
implementations over a variety of patterns → find the outliers where
pcrec loses → find GENERAL optimizations in pcrec → repeat. Positioning
and cross-engine learning come second. Every result is attributable to
a sub-bench version, a testee version, a machine and a timestamp, so
"X is fast at Y" is a reproducible, inspectable claim.

This repo is NOT pcrec's regression gate — pcrec keeps its own absolute
floors (its tests/bench/compare). pcrec-bench runs on its own cadence;
its numbers are comparisons between pinned versions.

## 2. The four founding principles (Frank, 2026-08-17)

1. **A larger test set than normal.** Not just `a+b` over a log file:
   the full feature spread including backrefs and subroutines, and the
   difficult classes — ambiguous decomposition, catastrophic
   backtracking, exact-minimum boundaries, large counts, big subjects,
   pathological alternations. Cases where engines genuinely diverge in
   approach are the interesting ones.
2. **Standardized per-testee output artifacts, compared statically.**
   Each measurement emits one record in a fixed, versioned schema.
   Comparison is an offline operation over records; records from
   different machines and dates are first-class (their environment is
   recorded); pcrec's record is just one more file in the pile.
3. **Favor open source.** When a testee wins a case we want to open its
   source and learn why. Closed engines may be admitted later, tagged.
4. **Agreed, versioned test units — and versioned testees.** Results
   compare only within the same sub-bench version. A testee is an
   (engine, version, build/run configuration) triple; pcrec appears as
   several testees (engine mode, captures on/off, later SIMD on/off),
   and that axis is first-class.

## 3. How the bench works

The unit of work is the **sub-bench**: a self-contained directory with
a declared OBJECTIVE (the mechanism it exists to exercise), one or
several related canonical patterns, generated subjects with a manifest,
oracle-verified expectations, tags, and per-engine notes. Applying one
sub-bench to one **testee** on one machine produces one **record** — a
general-setup layer (testee, environment, load, timestamp) plus raw
per-trial results — saved into the **store** and never edited. Records
are gathered one cell at a time, never "the whole gamut". A **report**
answers a query over the store ("sub-bench A1, open-source, compilers
only"), filtering on the recorded dimensions and reducing raw trials to
comparables. Details and vocabulary: requirements.md §2.

Three subject regimes are measured (requirements §3): large-subject
throughput; short-subject search (~256 B, per-call cost); and
match/compliance over 10..1000 B subjects. Compile/setup cost is its own
axis, defined per execution model (AOT / eager JIT / lazy JIT /
interpreter) and never folded into match time.

Not every rx fits every engine. Per (pattern, testee) the record states
an OUTCOME (compiled / did-not-compile / crashed / timed-out /
unsupported-by-declaration; per subject: as-expected / not /
wrong-span-or-captures / truncated-subject) — first-class results,
never harness errors. An engine that is not PCRE2-exact may run a
DECLARED VARIANT of a canonical pattern, under two constraints: the
results must be identical on every subject, and the sub-bench's
objective must still be exercised (requirements §4.4-4.5).

Correctness gates the scoreboard: a timing for a wrong answer is
excluded from rankings by default and shown in the diff; every
expectation carries its verification method; matching conventions
(Perl leftmost-first, POSIX leftmost-longest, all-ends) are tagged per
case and testees are scored against their own (requirements §7).

## 4. Architecture

Four decoupled components, each with its own design note when built:

- **Sub-benches** (`bench/<name>/`) — the versioned units above. Their
  pattern/case FORMAT is owned by pcrec's unified format work ([DD-13],
  grown from .rxt) and is not invented here; until it lands, today's
  .rxt is parsed as-is and per-sub-bench metadata lives in a plain
  sidecar of fields (no grammar) — requirements §5.
- **Testee adapters** (`testees/<name>/`) — one thin shim per engine
  that compiles a pattern, runs the sub-bench's regimes with batched
  in-process timing, and emits the record. Each pins its engine version
  and records build flags and runtime options; pcrec's adapters also
  record the artifact's mechanism stamps (engine, prefilter, rungs) as
  enumerated `engine_metadata` pairs so outliers bucket by mechanism.
  Adapters may need their engine's own build machinery; dependencies
  live here, never in pcrec.
- **The record** (`schema/`) — JSONL, schema-versioned, with a
  validator the reporter shares. Setup layer + MATCH rows + COMPILE
  rows; raw trials, no statistics. Design: docs/design/record_schema.md.
- **The store and the reporter** (`store/`, `report/`) — the store is
  the accumulated records with an index; the reporter is pure static
  analysis over records: filter, group, reduce to comparables, show N
  and pass-rate beside every number whose coverage is below 100%,
  self-describing output. It never runs an engine.

## 5. Testee roster

The harness comes first; the roster grows over time and includes
regex-to-code compilers as well as libraries. Committed for the first
cut: libpcre2 (interp and JIT as separate testees) and pcrec (several
configurations). Design population: RE2 and Rust `regex` (linear-time;
also the terminating-oracle tier for hazard bands), Oniguruma, TRE
(POSIX, tagged), Vectorscan (all-ends semantics, tagged), python `re`,
perl. A hand-written-C ceiling arm (pcrec's [BENCH-CEIL]) is a natural
later testee; not in the first cut.

## 6. Measurement discipline

Inherited from pcrec (its docs/dev/learnings.md §1-3, D12/D14/D15/D17/
D35) and binding: wait until the box is quiet, sample load before AND
after, per-core occupancy checked machine-readably, medians of N with
spread, batched in-process timing for short regimes, `gnutimeout` only
on the outer process, `LC_ALL=C`, environment recorded in every record,
harness failures counted apart from slow results, controls that share
no source with what they control. Requirements §9; BD3 for the
shared-box rules.

## 7. Relationship to pcrec

pcrec-bench pins pcrec by commit like every other testee; bumping the
pin is a deliberate, logged event. Findings flow back as reports
(case by case until the working model is clear) that become pcrec plan
rows with the bench case as the exercising case. Findings about other
engines are filed here (docs/dev/upstream_findings.md, archived
transcripts); findings about pcrec go to the pcrec manager. pcrec is
read-only from this project (BD2). Process conventions are pcrec's,
lighter (BD1): a CLAUDE.md per directory, the plan's grep'able STATE
rows, an append-only journal, a decision log, adversarial critic panels
on designs.

## 8. Status and open decisions

Status is `docs/dev/plan.md` ([B2] the record schema in progress as of
2026-08-25). The open decisions are requirements.md §12 (OD-B1..B10);
the disposition of this document's original open questions is
requirements.md §11. The project language is python 3 (BD4).
