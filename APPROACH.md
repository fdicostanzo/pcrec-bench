# pcrec-bench — a comparative regex-engine benchmark, seeded 2026-08-17

STATUS: SEED. Charter written at project creation (Frank's four principles,
2026-08-17); no code yet. Build begins after pcrec's scale work ([M4.6]/
[M4.7]) completes. Frank rules on the open questions in §8 before the first
runner is written.

## 1. Mission

Measure regex engines against each other — pcrec among them — on a test set
that is deliberately HARDER and WIDER than the usual microbenchmark fare,
and do it in a way that feeds engineering: every result must be traceable to
a case, a testee version, and a test-set version, so "X is fast at Y" is a
reproducible, inspectable claim rather than a chart bar.

This repo is NOT pcrec's regression gate. pcrec keeps its own internal
floors (tests/bench/compare, the D12 discipline) guarding its own changes.
pcrec-bench is positioning, comparison, and cross-engine learning; it runs
on a different cadence and its numbers are attributable to pinned versions.

## 2. The four founding principles (Frank, 2026-08-17)

1. **A larger test set than normal.** Not just `a+b` over a log file:
   backrefs and the full feature spread, plus the difficult classes —
   ambiguous-decomposition shapes (pcrec's K23 class), catastrophic-
   backtracking shapes, exact-minimum boundaries, large-count quantifiers,
   big subjects, pathological alternations. Cases where engines genuinely
   diverge in approach are the interesting ones.
2. **Standardized per-testee output artifacts, compared statically.** Each
   testee run emits one artifact in a fixed, versioned schema. Comparison
   is an OFFLINE operation over artifacts — no live head-to-head required,
   artifacts from different machines/dates are first-class citizens (with
   their environment recorded), and pcrec's own artifact is just one more
   file in the pile.
3. **Favor open source.** When a testee wins a case, we want to open its
   source and learn why. Closed engines may be admitted later but the core
   roster is open: the point is transferable understanding, not a
   scoreboard.
4. **Agreed, versioned test sets — and versioned testees.** Results only
   compare within the same test-set version. A testee is an (engine,
   version, build-configuration) triple — pcrec itself will appear as
   several testees (scalar vs simd, DFA vs VM vs auto, captures on/off),
   and that axis is first-class, not a footnote.

## 3. Architecture sketch

Four components, deliberately decoupled:

- **The test set** (`set/`): versioned corpora of (pattern, subject,
  expectation, tags). Tags carry: feature tier (base / captures / backrefs
  / lookaround / unicode / ...), hazard class (none / exponential-
  backtracking / ambiguous-decomposition / ...), size class, and the
  expectation's verification method (which oracle, or a derived law — see
  §5). Grows partly by import from pcrec's oracle-verified .rxt corpora
  (including the D27 blinded sets), partly by cases written here.
- **Testee adapters** (`testees/<name>/`): one thin shim per engine that
  compiles/loads a pattern, runs the set, and emits the standard artifact.
  Each adapter pins its engine version and records the exact build flags.
  Adapters are allowed to say "unsupported" per case — a first-class
  result, never an error (an engine that refuses backrefs is not wrong
  about backrefs; it is honest, exactly pcrec's "requires module X"
  philosophy).
- **The artifact** (`schema/`): one file per (testee, test-set-version,
  machine, date). Records, per case: compile outcome, match outcome
  (match/nomatch + spans + captures where supported), correctness verdict
  against the expectation, and timing — with COMPILE TIME and MATCH TIME
  separated (pcrec is AOT and pays gcc once; JITs pay at first use;
  interpreters pay per compile — collapsing these axes would make the
  comparison meaningless). Plus an environment header: CPU, kernel,
  compiler, quiet-box attestation, per-core-occupancy check (the lesson
  from pcrec's poisoned-pinned-core incident travels here).
- **The comparator** (`compare/`): pure static analysis over two or more
  artifacts — rankings, per-case diffs, per-tag rollups, correctness
  disagreement tables. Never runs an engine. Disagreement output is
  designed to feed pcrec's docs/dev/upstream_issues.md / known_issues.md
  flow directly.

## 4. Candidate testee roster (open source first)

- libpcre2 (interpreted AND jit as separate testees) — the compatibility
  reference.
- RE2 — the linear-time reference; leftmost-first on the backref-free tier.
- Rust `regex` crate — the other linear-time reference, different lineage.
- Oniguruma — the other mainstream backtracker lineage.
- TRE — POSIX, approximate-match heritage; different semantics, admitted
  with its semantics tagged.
- Vectorscan (Hyperscan lineage) — SIMD multi-pattern; SEMANTICS CAVEAT:
  reports all match ends, no leftmost-first, no captures — only comparable
  on the tags where its semantics align; the adapter must record this,
  not paper over it.
- pcrec — several testees per §2.4 (engine × options × scalar/simd once
  [SIMD-META] work exists).
- python `re` / others — cheap to add as adapters, useful as semantic
  cross-checks even where slow.

## 5. Correctness before speed

A timing for a wrong answer is worse than no timing: every case's
expectation carries its verification method, imported from pcrec's oracle
discipline — python `re` where it terminates, libpcre2 differential,
linear-time engines (RE2/rust) for the bands where backtrackers explode,
and derived-law-plus-induction where no engine terminates (the K23-region
method: prove a closed-form law by exhaustive small-N induction, generate
expectations from the law, re-verify independently). Where engines
LEGITIMATELY disagree (POSIX leftmost-longest vs Perl leftmost-first), the
case is tagged with which convention its expectation follows and testees
are scored only against their own convention.

The artifact's correctness verdict is per-case and blocking for the
scoreboard: a testee's timing on a case it got WRONG is excluded from
rankings by default (visible in the diff view, excluded from the rollup).

## 6. Relationship to pcrec

- pcrec-bench PINS pcrec by tag/commit, like every other testee. Bumping
  the pin is a deliberate, attributable event.
- The oracle-audit loop: with all engines built here anyway, this repo is
  the natural place to run large-scale differential sweeps over pcrec's
  corpora; findings flow back to pcrec as upstream_issues/known_issues
  rows with archived transcripts (pcrec's D35 style: stable-named verbatim
  output with a source-information header).
- Dependencies stay HERE. pcrec keeps its plain-GNU-make, stranger's-make-
  must-work posture (its D2/R5-Q1); this repo may use whatever build
  machinery its testees demand (cmake, cargo, meson...), vendored or
  system, pinned either way.

## 7. Process conventions (inherited from pcrec where they apply)

- Every directory gets a CLAUDE.md describing purpose and files.
- Measurement discipline travels: quiet-box runs, median/spread not
  single-shot, per-core occupancy checked before pinned runs, `timeout` on
  every command of uncertain length, artifacts record their environment.
- Decision log and journal start when build work starts (dev/ mirroring
  pcrec's docs/dev/ shape, lighter weight).
- Subagent rules (worktrees for writers, scope mandate restated in briefs)
  apply across BOTH repos now — the mandate is ~/pcrec + ~/pcrec-bench
  (Frank, 2026-08-17).

## 8. Open questions for Frank (rule before build starts)

1. **Set format**: extend pcrec's .rxt (proven, importable, but bench needs
   per-case tags/metadata .rxt doesn't carry) vs a bench-native format with
   an .rxt importer. Lean: bench-native JSONL with an importer.
2. **Artifact format**: JSONL vs TSV. Lean: JSONL, schema-versioned, with a
   tiny validator the comparator shares.
3. **Timing depth in v1**: wall-clock match throughput only, or also
   memory high-water and compile-artifact size? Lean: throughput + compile
   time in v1; memory later.
4. **Public posture**: is pcrec-bench public from the start (like pcrec)
   and are published rankings a goal, or is it an internal engineering
   tool first? Affects how much methodology prose §3's artifact needs.
5. **First milestone cut**: proposed M1 = set format ruled + schema ruled +
   two adapters (pcrec, libpcre2) + comparator MVP producing its first
   honest diff. Everything else follows.
