# R1 — critic panel on docs/design/requirements.md DRAFT v1 (2026-08-24)

Three read-only sonnet critics, distinct lenses, briefed to refute:
A = data model / report; B = semantics / variant axis / charter
consistency; C = blocking point / first cut / measurement validity.
Subject: requirements.md at commit 2fa2b2b. Manager spot-verified the
load-bearing citations before triage (mpstat present at /usr/bin/mpstat;
uutils timeout ~108.7 ms/call at pcrec docs/testing.md:2372; GCC-TIME's
1.87× single-sample swing at pcrec tests/bench/CLAUDE.md:78-82; LC_ALL=C
lesson at learnings.md:31; `RX_VM_RUNGS`/`RX_VM_STRATS` are structured
masks, src/gen/emit_vm.c:7313). 29 findings; 0 disputed as false;
dispositions below. FIXED = applied in requirements.md v2 (commit after
this file); RULING = needs Frank; CARRIED = moved to the OD ledger or a
plan row.

## Dispositions

| # | sev | finding (short) | disposition |
|---|---|---|---|
| A1 | HIGH | record identity collides at date granularity | FIXED: record id = (testee id, sub-bench id+version, machine id, RFC 3339 timestamp) + content hash; §2 says "one timestamped run" |
| A2 | HIGH | "run" undefined, §5 self-contradictory | FIXED: run = one harness invocation producing one or more records; a record is one cell; §2 defines run and trial |
| A3 | HIGH | mechanism stamps have no shape; pcrec's engine_why is prose | FIXED (with B1): generic `engine_metadata` map of enumerated (name, value) pairs, populated from structured fields; prose diagnostics unindexed |
| A4 | HIGH | build configuration is free text but is the headline pcrec filter axis | FIXED: enumerable testee fields (captures, engine-mode, simd, ...) + a residual flags blob for reproducibility only |
| A5 | HIGH | compile/setup cost does not fit the result row shape | FIXED: its own row kind keyed (pattern, trial) |
| A6 | HIGH | lazy JIT has no separable compile call | FIXED: per-execution-model protocol (AOT / eager-JIT / lazy-JIT / interpreter); lazy-JIT compile cost = trial-1 minus steady state, trial 1 excluded from match stats |
| A7 | MED | no outcome for silent subject truncation | FIXED: `consumed_length` recorded when the API exposes it; `truncated-subject` outcome |
| A8 | MED | runtime compile OPTIONS differ per engine; the text-variant machinery never fires | FIXED: per-testee option set recorded per sub-bench; variants cover option-driven divergence |
| A9 | MED | scan mode needs list-valued rows | CARRIED to OD-B3 |
| A10 | LOW | cross-schema-version reduction policy | FIXED: the reporter refuses to reduce mixed schema versions into one cell unless a declared migration exists |
| A11 | LOW | OD-B4 conflates enums with open identifiers | FIXED: OD-B4 split into fixed enums vs normalization rules (CPU model from /proc/cpuinfo, hardware id rule) |
| B1 | HIGH | pcrec-only stamp field contradicts "one more file in the pile" | FIXED with A3 |
| B2 | HIGH | capture-restructuring variants have no capture-correspondence contract | FIXED: variant declaration must state capture correspondence (by name / by index map / not checked); OD-B9 tracks the general contract with [DD-13a] T-3 |
| B3 | HIGH | the middle deviation grade is undecidable | FIXED (manager ruling, Frank may veto): TWO grades — `syntax-only` (mechanically checkable) and `approximates` (stated differences ARE expectations, reviewed); no "semantically equivalent" claim without a differential against an oracle that speaks the dialect |
| B4 | MED | who verifies an approximating variant's own answers | FIXED with B3: stated differences carry a verification method |
| B5 | MED | a partial-pass population hides an easy-cases-only number | FIXED: N and pass-rate are mandatory report columns whenever any cell's coverage < 100% |
| B6 | MED | hazard-class tags do not survive translation | FIXED: hazard and size class re-assertable per (case × variant), default inherited |
| B7 | MED | per-testee vs per-case convention unreconciled | FIXED: convention is a per-CASE expectation tag; a testee declares the conventions it can produce; a case whose convention a testee cannot produce routes through the variant mechanism with its own convention-tagged expectation, or is `unsupported-by-declaration` |
| B8 | MED | BLOCKING applied more broadly than its reason supports (.rxt is a live format; DD-13 is a superset) | RULING for Frank (with C1, C3) — see "For Frank" |
| B9 | LOW | §1 amends APPROACH §1 without saying so | FIXED: §11 lists the §1 mission re-ordering as an amendment |
| C1 | HIGH | "the rxt should be coming pretty soon" is unsupported by pcrec's plan: [DD-13b/c] have no queue position; [DD-14] is unfinished and growing | RULING for Frank; §5 now states the measured distance |
| C2 | HIGH | pcrec-bench plan.md [B3] still proposes the interim carrier §5 forbids | FIXED: [B3] row text rewritten in the same commit |
| C3 | MED | "format blocked" conflated with "nothing can run" | FIXED: §5 states what is blocked (a general cross-sub-bench grammar) vs not (the directory model; per-specimen ad hoc files; the record; adapters; the reporter) — subject to Frank's B8/C1 ruling |
| C4 | HIGH | gcc compile cost is not a clean single number (1.87× single-sample swing) | FIXED: compile/setup cost is median-of-N with spread like every other quantity |
| C5 | HIGH | per-trial gnutimeout would dominate the short regimes (~108.7 ms/call) | FIXED: timing loops are batched IN-PROCESS; gnutimeout guards the outer process only |
| C6 | MED | per-core occupancy check exists only as an ad hoc mpstat fragment | FIXED: §9 names pinned_measure.sh's mpstat pattern as the starting point, requires a machine-readable pass/fail; mpstat verified installed |
| C7 | MED | load checked only before, not after | FIXED: load re-sampled after; a record whose after-load exceeds the threshold is flagged INCONCLUSIVE |
| C8 | LOW | LC_ALL=C absent | FIXED: standing convention for every script |
| C9 | MED | 1 MB throughput subjects are 8-64× smaller than pcrec's convention | FIXED: disclosed as the specimen's known-smaller size; spread at 1 MB vs 8 MB measured before a standard size is set (OD-B10) |
| C10 | LOW | OD-B8 has no owning row | FIXED: OD-B8 attached to [B3] (harness core) as an explicit task |

## For Frank (rulings owed before adoption)

1. **The blocking scope (B8, C1, C3).** Your R6 ruled "block on the
   rxt — it should be coming pretty soon". The panel measured: in
   pcrec's plan, [DD-13a] completed 2026-08-17; [DD-13b] (design) and
   [DD-13c] (panel + ruling) are `not-started` with no queue position,
   and the row says nothing starts unprompted; the spine ahead of it
   ([DD-14]) is still producing waves. Two readings of "block": (i)
   BROAD — no case carrier at all until [DD-13] lands; the first cut
   then reduces to the record schema and an adapter exercised only on
   the email specimen's ad hoc files; or (ii) NARROW — what is blocked is
   AUTHORING a new cross-sub-bench grammar; parsing today's `.rxt` (a
   live, oracle-verified format that [DD-13] extends as a dialect,
   R-COMPAT-1) and wrapping per-specimen files in the sub-bench
   directory model are allowed. Manager recommendation: (ii), with the
   sub-bench's per-case tags and engine notes held in a plain sidecar
   whose fields are exactly R-BENCH-1..9 — no directives, no grammar —
   so [DD-13] absorbs them mechanically. v2 is written for (ii) with the
   sidecar marked as YOUR CALL.
2. **The deviation grades (B3)** — collapsed to two (syntax-only /
   approximates with stated differences as expectations). Veto if you
   want the three-way taxonomy back.

## Panel record

Critics ran read-only; no builds, no measurements, no files written.
Reports received 2026-08-25 03:18-03:2x UTC (2026-08-24 evening EDT).
Every finding's citation that the triage depends on was re-read by the
manager; none was found false. Critic A's record-size estimate
(0.5-2 MB per record, thousands of raw rows) is carried into OD-B6.
