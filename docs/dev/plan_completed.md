# pcrec-bench — completed plan rows (archive)

Rows move here verbatim when they reach STATE:completed, grouped by
completion date, newest group at the bottom.

## 2026-08-24

- [B0] STATE:completed — HOUSEKEEPING (first session, 2026-08-24): the
  docs/{dev,design} shape mirroring ~/pcrec/docs (plan, plan_completed,
  journal, decisions, gitignored wake brief, the pcrec references map),
  CLAUDE.md at every directory level, .gitignore, and the
  `pcrec-bench-manager` project skill (.claude/skills/) modelled on
  pcrec's `pcrec-manager` with this repo's references and the two-session
  box rules. No code.

## 2026-08-25

- [B1] STATE:completed 2026-08-25 (ADOPTED requirements.md v3 after the R1 panel; rulings: narrow blocking scope; variants must reproduce results exactly and preserve the sub-bench objective) — REQUIREMENTS: the overall-requirements discussion
  with Frank (opened 2026-08-24, first session; R1-R11 RULED the same
  evening — docs/design/requirements.md DRAFT v1 written from them;
  the D6 critic panel is the next step, then adoption). Inputs: APPROACH.md (the
  four principles, §8's five open questions), pcrec's R-BENCH-1..9
  (docs/design/dd13_format/requirements.md §5), pcrec [BENCH-1]/
  [BENCH-CEIL]/[ENG-PGO]'s cross-note, Frank's post-spine-loop direction
  (pcrec journal 2026-08-24), the pcrec manager's reference dump (all in
  docs/dev/pcrec_references.md). Output: docs/design/requirements.md —
  what is measured (axes: match throughput, compile/startup cost, latency
  on short subjects, memory later?), for whom (the pcrec optimization
  loop first; positioning second), the testee roster and its admission
  rule, the correctness policy, the artifact's minimum schema, the set's
  sources and versioning, the feedback shape into pcrec's plan, box/
  measurement discipline, public posture; §8 Q1-Q5 each ruled or
  explicitly deferred; then a D6 critic panel on the note before it is
  adopted.
- [B2] STATE:completed 2026-08-25 (MERGED from lane/b2schema b37122b, 6 commits: docs/design/record_schema.md 718 lines, schema/record.schema.json, validate.py X1-X17, check_fields.py, 2 synthetic examples + 15 named sabotages, make check-schema 2/15/0; accepted at merge: per-subject crashed/timed-out, dense trial numbering, lazy-JIT derivation row; S1/S2 critic panel running post-merge) — THE RECORD SCHEMA (APPROACH §3, §8 Q2; requirements.md §2, §4.2-4.4, §6):
  the versioned per-testee output file — environment header (CPU, kernel,
  compiler, load/quiet-box attestation, per-core occupancy), per-case
  compile outcome / match outcome / correctness verdict / timings with
  COMPILE and MATCH separated — plus the tiny validator the comparator
  shares. Design note → panel → ruled.
