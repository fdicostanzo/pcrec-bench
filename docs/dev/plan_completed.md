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
- [B2] STATE:completed 2026-08-25 (MERGED from lane/b2schema b37122b, 6 commits: docs/design/record_schema.md 718 lines, schema/record.schema.json, validate.py X1-X17, check_fields.py, 2 synthetic examples + 15 named sabotages, make check-schema 2/15/0; accepted at merge: per-subject crashed/timed-out, dense trial numbering, lazy-JIT derivation row; S1/S2 critic panel → 22 findings → schema v1.1 MERGED ae9b0d0 from lane/b2fix 1962ac8: 27 rules / 53 controls / check_rules.py; review docs/dev/reviews/2026-08-25-r2-record-schema.md) — THE RECORD SCHEMA (APPROACH §3, §8 Q2; requirements.md §2, §4.2-4.4, §6):
  the versioned per-testee output file — environment header (CPU, kernel,
  compiler, load/quiet-box attestation, per-core occupancy), per-case
  compile outcome / match outcome / correctness verdict / timings with
  COMPILE and MATCH separated — plus the tiny validator the comparator
  shares. Design note → panel → ruled.
- [B3] STATE:completed 2026-08-25 (MERGED 42c0557 from lane/b3harness f437952, 18 commits; make check 21/21 on master; docs/design/harness_notes.md + quiet_baseline.md; OD-B8 measured under load: occupancy is the detector, load1 the backstop — proposed limits busy ≤ 10 %, load1 < 2.0, re-measure quiet) — THE HARNESS CORE: the sub-bench DIRECTORY
  conventions (goal, canonical patterns, generated subjects + manifest,
  expectations with verification method, tags, engine notes and
  declared variants, regime declaration), the run-cells driver (one
  cell or a chosen few, never the gamut), the store layout + index
  (OD-B6), and the QUIET-BOX INSTRUMENT — load before/after, mpstat
  per-core occupancy machine-readable, the numeric meaning of "quiet"
  MEASURED on this box (OD-B8). The pattern/case FORMAT is owned by
  pcrec's [DD-13] and is NOT invented here (requirements.md §5); under
  Frank's NARROW blocking reading this row may parse today's `.rxt`
  as-is and wrap the email specimen's files as the first sub-bench with
  a plain per-sub-bench sidecar (R-BENCH-1..9 fields, no grammar);
  under the BROAD reading it wraps the specimen's files only.
- [B4] STATE:completed 2026-08-25 (MERGED with [B3] at 42c0557: testees/pcre2 interp+jit via a dlopen driver; testees/pcrec auto/nocaps/vm pinned at 8da6120 via pin.sh, the (?:P)\z whole-subject artifact with `form`, give-up range rule from the artifact's exported PCREC_ERR_FLOOR; pcre2 give-up set {−47,−53,−63,−46} measured; two pcrec findings filed with the pcrec manager: no DFA prefilter stamp, the \z skip loop cannot skip the last byte) — TESTEE ADAPTERS, first two (plus OD-B10, the large-subject size measured at 1 MB vs 8 MB): pcrec (as its
  several configuration testees, pinned by commit) and libpcre2 (interp AND
  jit as separate testees). Each pins its version and records build flags;
  "unsupported" is a first-class per-case result.
- [B5] STATE:completed 2026-08-25 (MERGED from lane/b5report 0d6ab1d: pcrecbench/report.py, --grain set|subject, gave-up apart from wrong, form beside numbers, lazy-JIT over lowest seq, 18 tests + v1.1 fixtures, make check-report; the manager resolved the Makefile/__main__/__init__/CLAUDE.md seams — report dispatched before argparse; make check on master = schema 2/53/0 + harness 21/21 + report 18/18) — THE REPORTER MVP: static over two or more
  artifacts — per-case diffs, per-tag rollups, correctness disagreement
  tables, rankings that exclude wrong answers by default. Never runs an
  engine.
