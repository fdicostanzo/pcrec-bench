# Lane `b42rxtneeds` — report

**Opus lane, 2026-09-12. Branch `lane/b42rxtneeds`, rebased onto master
79d0206. NOT merged — the manager merges.** Deliverable:
`docs/design/rxt_needs_v1.md`, this project's detailed `.rxt` capability
feedback to pcrecdev1 under Frank's ruling of the same day (plan row
`[B42]`, RULINGS Q3: build on `.rxt` for real, PARK at each roadblock,
feed pcrecdev1 the needed capabilities, restart and verify).

## Charter-vs-committed checklist

| the brief asked for | committed | where |
|---|---|---|
| `docs/design/rxt_needs_v1.md`, §0 purpose, the ruling, how to read, relationship to R-BENCH-1..9 | **DONE** | the note §0; §0.3 is a nine-row table saying which of R-BENCH-1..9 the note CONFIRMS, EXTENDS, finds INSUFFICIENT (R-BENCH-1, R-BENCH-5) or CORRECTS (R-BENCH-8) |
| §1 THE NEED TABLE, seven columns, every need the brief enumerated | **DONE** | §1, fifty needs (N-1..N-53; three rows ask the format nothing) in eight blocks. Every need the brief named by hand is present — multi-line/`(?x)` patterns (N-2), raw high bytes and NUL in patterns and subjects (N-3, N-4, N-28), pattern identity (N-7, confirmed sufficient), description (N-8), the nine provenance fields (N-11..N-19), tags incl. family/role/hazard/size (N-9) and REQUIRES with its closed vocabulary (N-20, N-21), the semantics convention (N-34) and the non-canonical expectation (N-35), subjects inline and by reference with manifests/hashes (N-24..N-27), expectations incl. find-all and the oracle METHOD vs ENGINE (N-30..N-38), regime membership (N-48), variants and the testee roster (N-39..N-42), the D93 hazard and the permanence question (N-43, N-44), the head-only reader (N-52), `include` (N-50), the set header (N-45..N-47), comments-vs-fields (N-53) |
| priority + wave/status per need | **DONE** | 36 MUST / 9 SHOULD / 5 COULD; 14 BUILT, 2 BUILT AND LOSSY, 20 REFUSED BY NAME, 15 ABSENT |
| §2 grammar sketch + worked example + what pcrec's own harness gets, per NEW/MISMATCHED production | **DONE** | §2.1-§2.12, twelve proposals, each with an EBNF sketch in `format_design.md` §1.3's style, scope/repeatability/escape rules, a worked example on a real capability-set pattern (the CRS 942140 import carries provenance; family 11's `a\|ab` carries the convention; `config tre-default` carries a `capable` list), and a "what pcrec's own harness gets" paragraph. The brief's example asked for a CRS rule with provenance, REQUIRES, a TRE variant marked unsupported and a convention — those four appear across §2.1, §2.2, §2.3 and §2.4 rather than in one block, because they belong to four different proposals |
| §3 ACCEPTANCE CHECKLIST, runnable | **DONE** | §3, 41 checks in seven groups (parse, raw-byte round-trip, refusal-by-name with its control, `--list-source` columns, the set loading and measuring with no second parser, D93/neutrality, format regressions). Each names the need, the command and the pass criterion; the gating checks are paired with their negative arms; nine carry a MEASURED BEFORE |
| §4 sequencing: first sample vs later, a minimal W2/W3 subset, what the bench does in the interim | **DONE** | §4.1 Tier 1/2/3; §4.2 states candidly that Tier 1 is most of W2 plus part of W3 and names W2-alone as the honest smaller cut; §4.3 nothing under `bench/`, plus three R5 follow-ups that are ours regardless |
| §5 open questions for pcrecdev1 and for Frank | **DONE** | §5.1 nine (P-Q1..P-Q9), §5.2 three (F-Q1..F-Q3) |
| a row in `docs/design/CLAUDE.md` | **DONE** | a full entry, in the file's own house style |
| cite everything by `file:line` or spec section; say where intent is ambiguous rather than inferring | **DONE** | 59 `format_design.md` citations, 26 distinct `rxt_format.md` ranges, plus `requirements.md`, `rxt_source.c`, and this repo's own files — **every line number re-verified against the source in a dedicated pass** (commit `2c464e5`, 34 moved). Ambiguity is flagged in-place: `mc`'s overlap rule (§2.10, "not stated anywhere I could find"), `@file:`'s NUL-safety (N-28, "UNVERIFIED at the pin"), the head/body asymmetry against §2.1's own proposal (flagged as the proposal's own defect, P-Q1) |
| commit incrementally; finish with the report; do not merge | **DONE** | seven commits; this file; not merged |

**Nothing is OWED.** No background job, no pending run, no promised number.

## What went beyond the brief, and why

**Twenty parse-only probes of the pinned binary, archived.** The brief
said to read `src/parse/rxt_source.c` "where the spec is unclear". Three
questions could not be settled by reading (what a NUL does, what a
trailing CR does, whether an authored `target`-less file is really
accepted), and one of them — the NUL — was the exact risk research note
N3 §5 had left explicitly UNVERIFIED. Running `--list-source` on
six-line fixtures is parse-only: no compile, no artifact, no driver, no
timing, so it is not a measurement in the sense the box rules govern, and
it cost under a second. Archived per the D35 convention with its
reproducing script:

- `docs/dev/measurements/probe_rxt_format.py`
- `docs/dev/measurements/2026-09-12-rxt-format-probes-d34c9131.txt`
- a row in `docs/dev/measurements/CLAUDE.md`

**Three findings that change what the note says, and one that corrects a
committed document:**

1. **A literal NUL in a `pattern` line is SILENTLY TRUNCATED** —
   `pattern ab<NUL>cd` dumps as `ab`, exit 0, no diagnostic. The parser
   slurps the file and splits it into NUL-terminated C strings
   (`~/pcrec/src/parse/rxt_source.c:437-456`). N3 §5 called this
   "a low-probability, unverified risk"; it is a real silent-wrong-answer
   path, and the note ranks its REFUSAL above every feature it asks for
   (§2.7, check B3, P-Q7).
2. **A second `description` in one pattern block silently overwrites the
   first** — last wins, exit 0, no diagnostic. Outside the ask, filed as
   P-Q9 and as check C10.
3. **`format_design.md` §4.5 item 4's regime mechanism cannot be used by
   any set in this repository.** It writes one block per regime whose
   pattern is `(?&<name>)`, and `rxt_format.md:284-291` states that a
   definition whose name carries `-` or `.` cannot be called from a
   pattern at all. Every pattern id in all five sets here is a hyphenated
   slug. The widened name grammar (which exists for this project) and the
   regime mechanism are individually right and jointly unusable — §2.11,
   P-Q5, with three candidate resolutions and no pick.
4. **`subbench_directory_model.md:554-560` Q4 is WRONG** where it says
   the pcrec→bench import direction is lossless because "`foo_bar` is a
   legal slug". The record schema's slug rule is
   `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$` — no underscore. `iso_ts` is not a
   legal bench `pattern_id`. Ours to fix, not pcrec's; the note records
   it so R-BENCH-8 does not inherit the error (§1.9 M11). **[B29] itself
   is NOT edited by this lane** — that is the manager's call.

**A sixth roadblock the brief's enumeration did not separate out.**
`@file:` gives a subject a path and no stable ID, and the format's own
answer to case identity is `file:line` — which moves on every
regeneration of a generated fragment. Every expectation key, report row
and interpreter fact in this project names a subject by id. §1.5's
N-27, roadblock #4 in document order.

## What this lane did NOT do, deliberately

- **No edit to `docs/design/capability_set_v1.md`.** Its §9.1 adopts
  Option B, which Frank's ruling supersedes. The consolidated R5 panel
  already plans that repair and states its trigger ("the revision lane
  opens once `rxt_needs_v1.md` is merged so the two agree"), so editing
  it here would have raced that lane. Recorded in the note as F-Q3.
- **No edit to `docs/dev/research/2026-09-12-b42-rxt-as-source.md`.** N3
  §6's Option B recommendation is likewise stale; a research note is a
  dated input, not a living document, and this note supersedes its
  recommendation by citation rather than by rewriting it.
- **No `bench/`, `schema/`, `pcrecbench/` or `testees/` change**, and no
  build. `~/pcrec` was read only.

## Files

| file | lines | what |
|---|---|---|
| `docs/design/rxt_needs_v1.md` | 1,271 | the deliverable |
| `docs/dev/measurements/probe_rxt_format.py` | 184 | the twenty probes, re-runnable (`$PCREC_BIN` overrides; resolves `build/` through the git common dir from a worktree) |
| `docs/dev/measurements/2026-09-12-rxt-format-probes-d34c9131.txt` | 136 | their archive at d34c9131 |
| `docs/design/CLAUDE.md` | +56 | the note's row |
| `docs/dev/measurements/CLAUDE.md` | +32 | the probe's two rows |

## Validation run

- **Citation pass**: every `format_design.md`, `rxt_format.md`,
  `requirements.md` and bench-side `file:line` re-read against its source;
  34 corrected (commit `2c464e5`, then three more in `91b030d`).
- **Table hygiene**: a column-count check over every markdown table in
  the note — **0 mismatches**; two literal `|` characters inside table
  cells escaped.
- **The probe archive re-derives**: `python3 docs/dev/measurements/probe_rxt_format.py`
  exits 0 and reproduces the committed `.txt` BYTE FOR BYTE except its
  `# bench:` provenance line, verified by running it twice and diffing
  (the fixture directory has a fixed name for exactly this reason, so
  pcrec's path-quoting diagnostics do not put noise in the archive).
- **Branch cleanliness**: `git diff --stat master` shows **five files,
  1,662 insertions, 0 deletions** after rebasing onto master 79d0206 —
  checked deliberately, because a lane branched behind master renders a
  merged file as a deletion in its own diff.

**`make check` was NOT run**: this lane touches no code, no schema, no
sub-bench and no testee — only three prose files and one new probe script
under `docs/`. Nothing in `make check`'s 344 harness checks, 75 reporter
tests or 132 interpreter checks reads any of them.
