# [B42] restart lane L3 — bench/capability@0.1, the SET (lane `b42set`)

Branch `lane/b42set`, worktree `worktrees/b42set`, from `master` tip
`4e4e52c`. Brief: turn L1's wild imports (`curation/wild/`) and L2's
designed members (`curation/designed/`) into the real, runnable sub-bench
`bench/capability@0.1`, built ON pcrec's delivered `.rxt` format
(pin cd371441, abi 25) as the pattern source of truth. Nothing measured;
generators + smoke only.

**STATUS: DELIVERABLES BUILT AND SMOKE-CHECKED. One item OWED — see
"Owed" below.**

## What this lane built

- `bench/capability/patterns.rxt` — 64 pattern blocks (63 members + the
  floor), each with a native `provenance` sub-block (the format's own
  nine pattern-scope fields) and a `tag family=/hazard=/requires=`
  line, plus one file-scope `vocabulary`/`ext bench` head. **Passes
  `pcrec --list-source patterns.rxt` cleanly (exit 0)** and every
  block's decoded `pattern` column round-trips byte-for-byte against
  the authoring table's own canonical bytes — checked programmatically
  in `gen_patterns.py --check` (the DD-13b.W23.5 dump-value seam),
  including the one genuinely raw-non-UTF-8-byte member
  (`mojibake-curly-quote`, `pattern-esc` with `\x93`/`\x94`).
- `bench/capability/gen_patterns.py` — the master table: parses both
  curation TSVs, applies the twin-pairing reconciliation (below) and a
  REQUIRES-tag derivation, renders `patterns.rxt` + `patterns/*.rx`
  (a derived export for today's pre-`.rxt`-loader harness), and
  `--sidecar`/`--provenance` modes feeding `subbench.toml` and
  `gen_provenance.py`.
- `bench/capability/subbench.toml` — `id="capability"`, `version="0.1"`,
  `regimes = ["search_short", "throughput"]` (no `match`, per the
  design's own set-wide exclusion), `short_search_max_bytes = 512`,
  64 `[[patterns]]` entries.
- `bench/capability/captext.py`, `gen_subjects.py` (75 typed short
  subjects), `gen_throughput_subjects.py` (3 throughput texts, with an
  empirical redos-safety timing guard — see "Safety check" below).
- `bench/capability/gen_expectations.py` (entry point; the derivation is
  the shared `pcrecbench.expectations` chain) → `expectations.tsv`
  (**OWED, see below** — the background derivation had not finished
  before this report was written; a fresh agent resumes from the
  committed marker).
- `bench/capability/gen_provenance.py` → `provenance.tsv`: the licence
  allowlist, `fidelity`/`adaptation` and CC-BY-SA/`attribution` gates,
  plus the Q1 similarity-check arm (character-4-gram Jaccard against
  every `synthesized` pattern's cited inspiration, threshold 0.85) —
  **all clear on the real 64-pattern population**.
- `bench/capability/gen_variants.py` → `variants.tsv` (deliberately
  empty; no v1 testee needs a rewrite — see the file's own docstring).
- `bench/capability/NOTES.md` — objective, twelve families as built, the
  twin-pairing reconciliation, blinding statements, subjects, the
  outlier rule (R0-R8), predictions P1-P10, what is deferred.
- `bench/capability/CLAUDE.md` — rewritten from the staging stub.
- `docs/dev/predictions/capability-0.1-first.tsv` — 15 clause rows
  (P1.a-c, P2.a-b, P3, P4.a-b, P5.a, P6.a-b, P7, P8, P10.a-b), structurally
  validated against `pcrecbench.interpret.load_predictions` (loads
  clean, closed sets satisfied).

## The twin-pairing reconciliation

Full table in `NOTES.md`; summary:

| designed twin | guessed partner | real partner | verdict |
|---|---|---|---|
| `uuid-near-miss` | grok UUID | `wild-validator-uuid-grok` (family 1) | CONFIRMED — real divergence on a bad-nibble subject |
| `ipv4-near-miss` | an OWASP IPv4 shape | `wild-validator-ipv4-owasp` (family 1) | CONFIRMED but WEAKER than designed: the two are answer-identical on every subject tried (OWASP's own pattern already range-bounds each octet) — a finding, not a defect, per the design's own R1 rule ("if they agree everywhere, that IS the finding") |
| `base10num-near-miss` | grok BASE10NUM | `wild-logparse-base10num-grok` (family **2**, not 1) | **MISMATCH, REPAIRED**: family metadata corrected to `wild-logparse`, text untouched. A real divergence exists (leading-zero strictness) |
| `winpath-near-miss` | grok WINPATH | `wild-logparse-winpath-grok` (family **2**, not 1 — WINPATH was reassigned there by the design note's own 2026-09-16 amendment, which L2's blinded lane predates) | **MISMATCH, REPAIRED**, same shape. A real divergence exists (reserved-character rejection) |

Per the brief's own instruction ("flag it in your report rather than
re-authoring"): both mismatches are repaired by FAMILY METADATA CORRECTION
only, never by rewriting either pattern's text. This costs family 1 two
members against its design-stated target (8 → 6: no twin exists for
`email` or `us-zip`) and gains family 2 two members beyond its stated
"designed members: none" (6 → 10). **Total set membership is unaffected
(64)**; per Frank's Q2 ruling (realism, not a ratio), a per-family count
target was never binding.

## Deviations from the design, each stated and reasoned

1. **75 short subjects, not 36** (`capability_set_v1.md` §3.4). Sixty-four
   heterogeneous real-world patterns do not share one small vocabulary
   the way `bench/syntax`'s 95 do; typing one hit/miss pair per pattern
   across twelve families landed at 75. Re-derived cell-time arithmetic
   in `NOTES.md`: `search_short` grows from the design's ~11 min/cell
   estimate to roughly ~23 min/cell, still comfortably inside
   `CELL_CAP`'s 5,400 s default (~2-2.5× headroom rather than the
   design's ~5×, not a cap risk).
2. **The twin-pairing family corrections** (above).
3. **The `ext bench` capability matrix is a first cut**, inferred from
   `bench/syntax`'s census findings and pcrec's D26 compatibility
   posture, not independently re-derived from a real compile census the
   way §5.1 demands for a production declaration. Flagged in `NOTES.md`
   for L5 to re-verify before any harness wiring trusts it.
4. **`gen_variants.py`'s table is empty** — no v1 roster testee needs a
   rewrite (§6 exists for RE2/Rust/Vectorscan/TRE, none in v1's roster).

## Safety check: family 10 (`redos-nested`) and the oracle

Every one of the six `redos-nested` patterns is authored `^`-anchored,
which makes an unanchored `find_all` scan safe regardless of subject
size (a later scan position cannot match `^` at all, so only the first
position is ever a real attempt). Verified two ways:

1. `gen_subjects.py`'s own near-miss subjects are capped at ≤ 20 bytes
   (bounding worst-case backtracking during oracle derivation even if
   the anchor argument were somehow wrong).
2. `gen_throughput_subjects.py`'s `_redos_safety_check` empirically times
   every redos pattern's `find_all` against all three throughput texts
   (up to 1 MB) with a 2-second guard, run as part of generation itself
   — it passed on the real texts (see the committed generator output).

## A finding surfaced by this lane's own run

`wild-datetime-datefinder-alternation`'s throughput derivation is
substantially more expensive than `bench/syntax`'s comparable oracle
run (~3.3 min there; this lane's `gen_expectations.py` ran well past
ten minutes before this report was written — see "Owed"). The pattern
is a ~200-branch top-level alternation, UNANCHORED, over up to 1 MB of
text — the likely dominant cost, and a DIFFERENT mechanism from the
already-named ReDoS calibration risk (CB8): nothing here is
catastrophic backtracking, it is plain alternation breadth at scale.
Recorded in `NOTES.md` as finding + prediction P3, and flagged here for
the manager: **a real measurement window on this set should watch
`wild-datetime-datefinder-alternation`'s `throughput` cell time
specifically**, and `make check-harness`'s own future runtime will grow
by more than `bench/syntax`'s stated 3-4 minutes once this set's
`gen_expectations.py --check` is added to the generic gate loop.

## What ran (charter-vs-committed)

- `gen_patterns.py --check` (round-trips `patterns.rxt` against the real
  pinned binary `build/pcrec-cd371441/build/pcrec`, resolved via
  `git rev-parse --git-common-dir` — **a bug this lane found and fixed**:
  the default resolution originally walked a relative path from
  `__file__`, which is wrong inside a worktree since `build/` is not
  per-worktree; now matches `probe_rxt_format.py`'s/`run.sh`'s own rule):
  **PASS**.
- `gen_subjects.py`, `gen_throughput_subjects.py`: **PASS** (both,
  including the redos safety check).
- `gen_provenance.py --check`: **PASS** (64/64 rows, licence gate,
  similarity-check arm all clear).
- `gen_variants.py --check`: **PASS** (0/0, the checked-empty case).
- `tools/selfcheck.py`'s generic per-set gates, run individually rather
  than the full `make check-harness` (the brief's own allowance — the
  full suite was judged too heavy to run twice tonight given this
  lane's own `gen_expectations.py` cost): `check_manifests` (covers
  every `bench/*/` set by enumeration, including `capability`),
  `check_patterns_distinct`, `check_floor_pattern`,
  `check_id_preflight` — **all PASS for `capability`** except the one
  item still OWED below (the floor-pattern quick-cell smoke, which
  needs `expectations.tsv`). Every OTHER set's own generic gates were
  incidentally re-run by the same enumeration and stayed green
  (altwide, bounded, email, loglines, syntax) — not this lane's claim
  to make, but evidence nothing here broke the shared harness.
- `python3 -c "... pcrecbench.interpret.load_predictions(...)"`:
  structural validation of the predictions TSV — **PASS** (15 rows
  load clean).
- Full `make check` / `make check-harness`: **NOT run** — too heavy
  to run twice tonight per the brief's own allowance, and this lane's
  `gen_expectations.py` cost (see "Owed") makes a first full run risk
  a very long wall-clock without the marker discipline a background
  job needs. **OWED to whichever session next has box time.**

## Owed

**`bench/capability/expectations.tsv` and the floor-pattern quick-cell
smoke that depends on it.** `gen_expectations.py` (the shared libpcre2
oracle chain, `pcrecbench/expectations.py`) was launched under the Bash
tool's `run_in_background: true` (harness-tracked — it DOES notify on
completion, the boilerplate's own distinction from a disowned/setsid
job) and ran past thirteen CPU-minutes at a steady 99.9% CPU with no
crash and no hang signature (`ps -o etimes,time,pcpu` showed
monotonically increasing TIME throughout, i.e. genuinely working, not
blocked) before this report was written. The datefinder alternation's
throughput cost (above) is the leading explanation, not a bug in the
generator (every OTHER generator — `gen_patterns.py`, `gen_subjects.py`,
`gen_throughput_subjects.py`, `gen_provenance.py`, `gen_variants.py` —
completed in well under a second each). **Trigger**: the tracked
background run's own completion notification, or — for a fresh agent
resuming this lane without that notification in hand — check for the
process by re-running

    cd bench/capability && python3 gen_expectations.py

(idempotent; safe to re-run if the original process is gone) and treat
a long-but-steadily-CPU-bound run as WORKING, not hung, per this lane's
own observation above. Once it completes: commit `expectations.tsv`,
then re-run `check_floor_pattern` (or the generic-gates driver
`run_generic_gates.py` left in the worktree root — DELETE it once
`expectations.tsv` lands and the gate is confirmed green; it is a lane
scratch tool, not a deliverable) to confirm the floor-pattern quick
cell completes. Nothing else in this lane's deliverables depends on
this file being present to BE correct — `gen_provenance.py`,
`gen_variants.py` and the `patterns.rxt` round-trip all already pass
without it — but the sub-bench is not fully RUNNABLE until it exists.

## For L4 (the loader) — interim message already sendable

`patterns.rxt`'s STRUCTURE is stable: 64 blocks, the native `provenance`
sub-block, `tag family=/hazard=/requires=` (closed against
`vocabulary family`/`vocabulary hazard`/`vocabulary requires` at file
scope), one file-scope `ext bench` block (`roster <six testee ids>` +
one `capabilities <testee>` sub-block per roster member, each a list of
REQUIRES-vocabulary tokens). L4 can charter against this shape now;
`subbench.toml`'s `[[patterns]] file = "patterns/<id>.rx"` convention is
what L4's loader should be prepared to REPLACE with a direct `.rxt`
read (`patterns.rxt` is authoritative, `patterns/*.rx` is this lane's
own derived compatibility shim).

## Mandate compliance

Touched only `bench/capability/`, `docs/dev/predictions/`,
`docs/dev/lanes/b42set_report.md`, and (read/build only, never write)
the shared `build/pcrec-cd371441/` binary already delivered by the
restart's earlier lanes. `~/pcrec` was never read or written directly
by this lane (the binary was reached via `build/pcrec-cd371441/build/
pcrec`, a pcrec-bench-tree artifact). No `schema/`, `pcrecbench/` or
`testees/` file was touched — the schema-MINOR provenance-field
promotion (CB3) and the harness capability-policy wiring (L5) are both
named as future lanes' scope in `NOTES.md`, not built here.
