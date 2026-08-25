# R2 — critic panel on the merged record schema (2026-08-25)

Subject: docs/design/record_schema.md + schema/ as merged at 9fd9d4a
(lane b2schema b37122b). Two read-only sonnet critics, distinct lenses:
S1 = data model vs consumers (wrote 12 new sabotaged records and ran
validate.py on them); S2 = measurement provenance / reproducibility
(probed this box for every environment field). 22 findings; all
accepted; carried by lane b2fix (schema 1.0 → 1.1, brief
scratchpad/brief_b2fix.md). Manager dispositions below; the fix lane's
delivery message records what actually landed.

## S2 — provenance (13 + one example defect)

| # | sev | finding | disposition |
|---|---|---|---|
| S2-1 | HIGH | lazy-JIT "trial 1 minus steady state" is NOT computable: trials restart per (pattern, subject, regime) and row order is declared insignificant | FIX 1: required per-row `seq`; derive over the lowest seq of the pattern |
| S2-2 | HIGH | `load` carries no raw evidence; `measured` claimable on fabricated numbers | FIX 2: loadavg_raw + sampled_at per sample; X-rule parsed == numbers |
| S2-3 | HIGH | occupancy sampled once while load is before/after — the poisoned-core lesson reopened | FIX 3: occupancy before/after; harness re-samples both |
| S2-4 | HIGH | contract promises the iteration calibration is recorded; no field exists | FIX 4: per-row `calibration` {target_ns, probe_iterations, probe_elapsed_ns} + X-rule |
| S2-5 | MED | engine_commit optional despite "pcrec ALWAYS pinned" | FIX 5: required when the version is not a release-tag shape |
| S2-6 | MED | no driver build flags recorded | FIX 6: run.driver_build_flags + run.driver_compiler |
| S2-7 | MED | subjects[].sha256 optional vs patterns' required | FIX 7: required |
| S2-8 | MED | quiet_attestation inert and used inconsistently in the lane's own example | FIX 8: dropped |
| S2-9 | MED | §6 normalization rules are prose, unchecked | FIX 9: implement + check, or mark asserted-not-derived with the reason |
| S2-10..13 | LOW | cpu MHz, clock source, hugepages, chrt+taskset | FIX 10: cpu_mhz optional, clock_source required enum, pinning value; hugepages listed as an absence |
| S2-ex | — | the lazy-JIT example's `tier` metadata has no described adapter mechanism | FIX 11: removed or replaced |

## S1 — data model (9)

| # | sev | finding | disposition |
|---|---|---|---|
| S1-1 | HIGH | consumed_length unbounded (999999999 on a 1 MB subject ACCEPTED) | FIX 13: X-rule ≤ bytes_offered |
| S1-2 | HIGH | by-index-map without index_map ACCEPTED | FIX 14: if/then |
| S1-3 | HIGH (doctrine) | X5/X7/X8/X12/X16 have no positive control | FIX 15: controls from S1's templates |
| S1-4 | MED | role=single with n_subjects=5 ACCEPTED | FIX 16: const 1 |
| S1-5 | MED | measured with occupancy=unavailable | FIX 17 (RULING): measured requires pass both samples; unavailable/fail ⇒ inconclusive-load |
| S1-6 | MED | content hash fragile to reformatting/autocrlf | FIX 18: .gitattributes `*.jsonl -text` + a §3 sentence |
| S1-7 | MED | pattern_id/subject_id cross-record stability unstated | FIX 19: §10.1 invariant |
| S1-8 | LOW | hash proves byte integrity, not truth | FIX 20: one sentence |
| S1-9 | LOW | -<n> disambiguator not stated atomic | to the harness lane: O_EXCL claim; §3 states it is the writer's obligation |

S1 also confirmed: every query shape the requirements name is
answerable from the fields; R1's A1-A11 closed except A7's numeric half
(= S1-1); no pcrec-specific shape in a top-level field. S2 confirmed:
run.harness_commit present; the pcrec three-phase compile rows
reconstruct per-phase medians; governor/turbo probeable on this (AMD)
box via the cpufreq/boost fallback; X9/X11/X14 correctly built from
their bad examples.

## Lessons

A schema author's "for the panel" list found the two rulings; the
critics found the holes the author could not see from inside: rules
with no failing example, a derivation that assumed an order the author
had declared insignificant, and evidence fields that were verdicts
without samples. Every check needs its sabotage; every verdict needs
its raw.
