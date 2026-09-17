# lane l6bvs — the Vectorscan adapter (testees/vectorscan/)

Branch `lane/l6bvs`, worktree `worktrees/l6bvs`, branch point `c5180ed`
(master). [B7]/L6b wave 2 (capability_set_v1.md §11.1's per-engine lane
row; TRE + Vectorscan opened together, per plan.md's "L6b wave 2 open
(tre + vectorscan)"). This report touches nothing outside
`testees/vectorscan/`, `bench/capability/`, `docs/dev/measurements/`,
`docs/dev/lanes/`, `testees/CLAUDE.md`. The `EXT_BENCH_ROSTER`/
`patterns.rxt` edit in `bench/capability/` is the one place a merge seam
with sibling lanes (`l6bre2`, `l6bonig`, held merged; `l6btre` if it also
touches this file) is plausible — the manager's to resolve, not this
lane's, per the brief's own note.

**Session-start note**: this task's brief initially landed while this
session's cwd was pointed at a stray `worktrees/b42repdiag` (a different
lane's worktree, containing uncommitted work not mine) — flagged to
team-lead before touching anything; the environment corrected itself to
plain `master` on the next turn, `worktrees/l6bvs` was created fresh per
BOILERPLATE.md's own worktree ritual, and no b42repdiag file was ever
read or written by this lane.

## Deliverables, against the brief

1. **`testees/vectorscan/` built**: `adapter.py`, `driver.c`
   (direct-linked `#include <hs/hs.h>` / `-lhs`, `pkg-config libhs`
   verified working — this box has `libvectorscan-dev`, confirmed
   `libhyperscan-dev` NOT installed per the conflict warning),
   `configs.toml` (`vectorscan-block-nosom` only), `_probe.rx`,
   `CLAUDE.md` (all five required sections: (a) compile-cost definition,
   (b) `consumed_length` convention, (c) the config and the flag choice
   an A/B census DECIDED, (d) the boolean-grain `outcome_for` statement,
   (e) `hs_populate_platform`/SIMD notes). `driver.c` compiles clean
   under `gcc -O2 -std=gnu11` with the real pkg-config flags, zero
   warnings.
2. **Config**: `vectorscan-block-nosom` only, per Frank's Q3 boolean-
   grain ruling. `testee_id` derives to
   `vectorscan_5.4.11_block-nosom-nocaps-simd` (confirmed via
   `Adapter.describe()` + `schema/validate.py`'s own
   `derive_testee_id`, called through the real `pcrecbench testees`
   listing). `vectorscan-block-som` is documented in
   `testees/vectorscan/CLAUDE.md` and in `gen_patterns.py`'s own comment
   block as a LATER config, not wired — per the brief's instruction, and
   because it is gated on span-grain scoring machinery
   (capability_set_v1.md §5.6 option (A)) that does not exist yet.
3. **THE GOVERNING RULING, stated precisely, and ESCALATED past what the
   brief anticipated.** `testees/vectorscan/CLAUDE.md`'s "THE GOVERNING
   RULING" section states what a "correct" outcome means at boolean
   grain (a true nomatch scores normally; a true match reports
   `start=end=None`, never a real end offset even though Hyperscan's
   callback hands the driver one), how wrong-span-or-captures becomes
   structurally unreachable in its INTENDED sense (this testee never
   claims a specific wrong span — it claims none at all), and — the
   escalation — **how the record does NOT stay schema-valid today**:
   - **Level 1 (predicted by the brief): `harness.outcome_for` has no
     boolean-grain accommodation.** Reproduced directly against the real
     function (not merely read from source):
     ```
     TRUE MATCH row scored:   wrong-span-or-captures -- expected span [6,9]; observed [None,None]
     TRUE NOMATCH row scored: matched-as-expected -- None
     ```
     Every genuine match scores `wrong-span-or-captures`; every genuine
     nomatch scores correctly.
   - **Level 2 (found during this lane's own validation, NOT predicted
     by the brief): the record FAILS SCHEMA VALIDATION OUTRIGHT for any
     cell containing a real match, on any set, at any tier.**
     Reproduced end to end through the real harness (`pcrecbench quick
     --subbench email --pattern orig --regime search_short --testee
     vectorscan-block-nosom --subjects 5`, this lane, after generating
     bench/email's gitignored subject trees):
     ```
     pcrecbench quick: the record FAILED validation and was NOT written to the store -- this is a harness bug, not a measurement result (harness contract 4 step 5).
     validate.py: observed.span.0: None is not of type 'integer' [SCHEMA]
     validate.py: observed.span.1: None is not of type 'integer' [SCHEMA]
     ```
     `schema/record.schema.json`'s `span` field allows the WHOLE field
     to be `null`, but an array value's two items must each be
     `{"type": "integer", "minimum": 0}` — `harness.outcome_for`'s
     `wrong-span-or-captures` branch always builds `[row.start,
     row.end]` as an array, never `None` as a whole, so `[None, None]`
     is what this testee always produces on a match, and it is always
     schema-illegal. A pure-nomatch cell writes fine (confirmed: the
     span/observed machinery is never reached on that path). The
     rejected scratch artifact was deleted after inspection; nothing
     was committed or left in `build/`.
   - **Both are named as findings for the manager, not routed around.**
     Neither is fixable inside `testees/vectorscan/` alone: the fix
     needs a `grain`-shaped declaration on the harness side (the same
     precedent `convention`/R5-B1/CB1 already sets) that gives a
     boolean-grain testee's match rows a code path producing
     `observed.span = null` (schema-legal) and an honest outcome value,
     rather than attempting `wrong-span-or-captures`'s two-integer array
     unconditionally. This is shared `pcrecbench/harness.py` (and
     possibly `schema/record.schema.json`) — infrastructure this lane
     was told not to touch while pcrec's battery owns the box, and a
     schema/harness change needs a ruling regardless of the box being
     quiet.
4. **Capability witness census**: every `REQUIRES_VOCAB` token
   (compile-time ones as isolated witnesses; `span-reporting`/`captures`
   stated as execution-model facts) PLUS all 64 real `bench/capability`
   corpus patterns, through the real adapter —
   `docs/dev/measurements/probe_vectorscan_capability_census.py` +
   `2026-09-17-vectorscan-capability-witness-census-5.4.11.txt`. **5 of
   17 tokens SATISFIED** (`unicode-properties`, `named-groups`,
   `free-spacing`, `non-utf8-subject`, `true-end-anchor`) — the
   narrowest on the roster, as the brief predicted. **A genuine A/B
   finding that changed the shipped driver**: the first cut set
   `HS_FLAG_UCP` unconditionally (reasoning, unchecked, that `\p{...}`
   would need it); a real census showed `\p{L}` compiles IDENTICALLY
   with or without the flag, while setting it BREAKS `\b` compilation on
   5 real corpus patterns carrying no unicode-properties requirement at
   all (35/64 corpus compiles vs 40/64). Shipped: `VS_DRIVER_FLAGS = 0`.
   `unicode-properties` is the MIRROR-IMAGE finding of Oniguruma's own
   census (onig: `\p{Alpha}` works, `\p{L}` does not, under ASCII
   encoding; Vectorscan: the reverse — real Unicode categories work,
   POSIX names do not). One nuance kept in prose per this project's own
   precedent (pcre2-dfa's family-11 table, onig's recursion-spelling
   gap): `free-spacing`'s isolated witness compiles, but two real
   corpus patterns using genuine multi-line `(?x)` + `#`-comments refuse
   ("Unterminated comment") — the token stays SATISFIED, the two
   failures are documented, honest `did-not-compile` rows.
   `bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` gained the
   `vectorscan-block-nosom` row (regenerated into `patterns.rxt`,
   confirmed `--check`-clean); no other `bench/capability` generator
   needed regeneration (`gen_expectations.py --check`,
   `gen_variants.py --check`, `gen_provenance.py --check` all confirmed
   clean after the roster change — a capability-matrix-only edit).
5. **I-72 (pattern bytes end to end)**: this adapter passes the pattern
   via a FILE, exactly like pcre2/onig's own convention — there is no
   `str` conversion anywhere on the path (`_compile_one` writes with
   `open(patfile, "wb")` on the raw bytes `pcrecbench.subbench` hands
   it), so the latin-1/fsencode corruption I-72 found cannot occur here
   STRUCTURALLY, not merely "tested and passed". Verified live through
   the REAL adapter (`Adapter.compile()` + `Adapter.measure()`, not the
   raw driver binary alone) against the same witness pattern/subject
   pair pcrec's own guard uses (`\x93[\x20-\x7e]*\x94` /
   `\x93hello\x94`): `hb match 7` (consumed the full 7 bytes). The
   additive `check_high_byte_pattern_argv` arm is described in
   `testees/vectorscan/CLAUDE.md` as asserting `answer == "match"` ONLY
   (never a span — this testee cannot honestly assert one) but is **NOT
   YET added to `tools/selfcheck.py` itself** (shared harness
   infrastructure, the HARD RULE) — verified in isolation as instructed;
   the exact arm to add is spelled out in the CLAUDE.md section and in
   OWED below.
6. **Refusals first-class**: `hs_compile()` failure → `did-not-compile`
   with `hs_compile_error_t`'s own message, diagnostic never re-typed.
   **NO `refusal_class` pair** — capability_set_v1.md §5.5 states plainly
   this is "Never declared by Vectorscan or perl, whose refusal is free
   text only"; declaring one anyway would be the exact dishonest
   invention record_schema.md §7 rule 1 forbids (unlike
   `testees/onig/adapter.py`'s own `refusal_class`, which IS honest
   because Oniguruma's `ONIGERR_*` is a real closed enum). `GAVE_UP_CODES
   = frozenset()`: Vectorscan's whole architecture is a bounded
   automaton with no documented match-time resource-limit refusal to
   bucket — stated as a finding in itself (`testees/vectorscan/
   CLAUDE.md`'s own "gave-up: the EMPTY SET" section), not merely an
   empty table.

## Validation run (all within the small-smoke / isolated-arm budget the
brief and BOILERPLATE.md permit — nothing multi-minute, nothing
CPU-bound at corpus scale, no `make check`/`make check-harness`)

- `gcc -O2 -std=gnu11 $(pkg-config --cflags --libs libhs) driver.c` —
  clean compile, zero warnings.
- Direct driver smoke (no adapter): compile-only, search + match modes,
  a high-byte pattern/subject pair, a `\p{L}+` pattern, a backreference
  refusal, the `--mode`/`--form` cross-check's own die() path — all
  behaved as designed (transcripts in this lane's session, not
  re-pasted here; every behaviour they demonstrate is independently
  reproduced through the REAL adapter below).
- Full adapter smoke via a small standalone script (`describe()`,
  `compile()` both forms, `binary_identity()`, `measure()` at all three
  regimes): `describe()`'s every field printed and checked by eye
  against record_schema.md's enums; `compile()` on `foo|bar` produced
  `compiled` on both forms with real `hs_expression_info`/
  `hs_database_size` metadata; `measure()` on `search_short`,
  `throughput` and `match` all produced the expected `MatchRow`s
  (`start=end=None`, `NCAPS=0`, `NMATCHES=None` always, `consumed`
  correct); `binary_identity()` resolved `/usr/lib/x86_64-linux-gnu/
  libhs.so.5.4.11` with its sha256.
- `harness.outcome_for` called DIRECTLY with a fabricated boolean-grain
  `MatchRow` and a real-shaped `Expectation` — the Level-1 finding above,
  reproduced against the actual function, not inferred from reading it.
- `python3 docs/dev/measurements/probe_vectorscan_capability_census.py`
  — run TWICE (with and without `HS_FLAG_UCP`), the A/B finding that
  decided the shipped flags.
- `bench/capability/gen_patterns.py --check` — clean after regeneration;
  `gen_expectations.py --check`, `gen_variants.py --check`,
  `gen_provenance.py --check` (after generating the gitignored subject
  trees with `gen_subjects.py`/`gen_throughput_subjects.py`) — all clean,
  confirming the roster edit touched nothing else.
- `make check-schema` (~3 s, explicitly permitted) — 4 accepted / 72
  rejected-for-cause, unchanged: this lane's changes do not touch
  `schema/`.
- `python3 -m pcrecbench testees` — `vectorscan-block-nosom` listed with
  its full description.
- `python3 -m pcrecbench quick --subbench email --pattern orig --regime
  search_short --testee vectorscan-block-nosom --subjects 5` (a SCRATCH
  cell, never `store/`) — this is where Level 2 above was found; the
  rejected artifact under `build/scratch-store/` was inspected then
  deleted, nothing left behind, nothing in `store/` touched.

## OWED (exact commands, for the manager or a fresh agent to run once
the box is quiet / `make check-harness` is clear to run again)

1. **`make check-harness`** (and `make check` generally) — explicitly
   forbidden this session by the HARD RULE (pcrec's battery owns the
   box). Command: `make check-harness` from the repo root. Expected to
   pass for every check NOT specific to this lane's new files; this
   lane added no new generic-gate-covered generator beyond what's
   already exercised above by hand (`gen_patterns.py --check` etc.).
2. **The `check_high_byte_pattern_argv` arm for `vectorscan-block-nosom`
   in `tools/selfcheck.py`** — described precisely in
   `testees/vectorscan/CLAUDE.md`'s "The I-72 lesson" section (assert
   `answer == "match"` only, same pattern/subject pair as the existing
   pcrec/pcre2/onig arms). Not added because `tools/selfcheck.py` is
   shared `make check-harness` infrastructure and this session was told
   not to touch multi-minute/shared-check surfaces while the battery
   runs; verified in isolation instead (see "Validation run" above).
3. **A real `run --tier scratch` or pinned cell against a NOMATCH-heavy
   set** (e.g. `bench/loglines`, "mostly-FAILING log text" by design) to
   get a FIRST clean, schema-valid `vectorscan-block-nosom` record
   written end to end, since `bench/email`'s `orig` pattern genuinely
   matches and therefore cannot write today (Level 2 finding). Command:
   `python3 -m pcrecbench run --subbench loglines --testee
   vectorscan-block-nosom --tier scratch --trials 1` once a quiet-enough
   box is available (scratch tier still samples the box; no quiet GATE
   is required for scratch). Whether even a nomatch-only run writes
   depends on none of loglines' ten patterns matching ANY subject under
   vectorscan-block-nosom, which this lane has not checked.
4. **The Level-2 schema/harness fix itself** — a manager/Frank-level
   ruling and a shared-code change (`pcrecbench/harness.py`'s
   `outcome_for`, possibly `schema/record.schema.json`), not something
   an adapter lane builds unilaterally. Until it lands, `vectorscan-
   block-nosom` cannot be measured into `store/` (or even into a scratch
   store) on any set with at least one real match — a genuine blocker
   for [B7]'s roster completeness on this testee, worth surfacing to
   Frank ahead of the next capability-set measurement window.
5. **The `--find-all`/`NMATCHES` adapter-side reduction** the research
   note's own §11 describes (turning Hyperscan's one-pass all-ends
   callback into a KB-17-shaped non-overlapping count) — deliberately
   NOT built this lane (see `testees/vectorscan/CLAUDE.md`'s own
   "NMATCHES... also unavailable, also honest" section); `NMATCHES` is
   always `-` today.
6. **`vectorscan-block-som`** — documented, not wired, per the brief's
   own instruction. Needs the span-grain scoring machinery
   capability_set_v1.md §5.6 option (A) describes (a third driver
   invocation mode, a list-valued row shape, OD-B3) before it would
   answer a genuinely different question than `nosom` does; wiring it
   today would only add a config that ALSO cannot validate on a match,
   for a real memory/compile-time cost with no compensating benefit
   until that machinery exists.

## Files touched

- `testees/vectorscan/{adapter.py,driver.c,configs.toml,_probe.rx,CLAUDE.md}` — new
- `testees/CLAUDE.md` — new roster row
- `bench/capability/gen_patterns.py` — new `EXT_BENCH_ROSTER` entry + its long derivation comment
- `bench/capability/patterns.rxt` — regenerated (the one new `capabilities vectorscan-block-nosom` block; `--check`-clean)
- `docs/dev/measurements/{probe_vectorscan_capability_census.py,2026-09-17-vectorscan-capability-witness-census-5.4.11.txt}` — new
- `docs/dev/measurements/CLAUDE.md` — new entry
- `docs/dev/lanes/l6bvs_report.md` — this file

Not merged (the manager merges); branch `lane/l6bvs` is ready for review.
