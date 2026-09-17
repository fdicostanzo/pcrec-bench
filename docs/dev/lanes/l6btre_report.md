# lane l6btre report — the TRE adapter (`testees/tre/`)

**Task**: [B7]/L6b wave 2 (`docs/design/capability_set_v1.md` §11.1) —
build a full TRE testee adapter: `tre-default` (TRE's whole roster — it
has no space/speed dial), a direct TRE C driver, capability declarations
from a real compile+match census, CS5 resolved by witness (not assumed),
the I-72 raw-bytes lesson, and validated smoke results.

**Branch**: `lane/l6btre`, three commits (`6d7996b`, `dd56a3d`, `d95cd10`),
`worktrees/l6btre`.

**A worktree/task mismatch was caught and corrected before any work
started**: this agent was spawned inside `worktrees/b42repdiag` (a spawn
glitch, per the manager) rather than a fresh `l6btre` worktree. Flagged to
the manager before touching anything; confirmed and corrected (option 1 —
create `worktrees/l6btre` fresh off master) before any file was written.
`worktrees/b42repdiag`'s own in-progress regen wave was never touched.

## What was built

- `testees/tre/driver.c` — a direct TRE C driver (`-ltre`,
  `#include <tre/tre.h>`) implementing the shared protocol
  (`pcrecbench/adapters.py`'s docstring) against `testees/pcre2/driver.c`'s
  and `testees/onig/driver.c`'s reference shape: same argv, same
  per-subject clock discipline, the same S3.1 find-all advance rule (KB-17),
  the same per-subject alarm/timeout mechanism, the same `--form`/`--mode`
  cross-check. TRE-specific: `tre_regncompb`/`tre_regnexecb` (the
  byte-literal, explicit-length API pair — I-72 immune by construction,
  the pattern travels as a FILE, never argv text); `REG_EXTENDED` with NO
  `REG_NEWLINE` (two stated consequences: `.` matches newline, `^`/`$`
  stay single-line); a `^(?:<pattern>)$` whole-subject wrap built inside
  the driver (NOT `pcrecbench.record.whole_subject_text()`'s `\z` form —
  TRE has no `\z` at all); a generic (not enumerated) gave-up
  classification, since POSIX's own contract for `regexec`-family
  functions recognizes only 0/`REG_NOMATCH` as answers.
- `testees/tre/adapter.py` — `describe`/`prepare`/`compile`/`measure`;
  `probe_version` parses `tre_version()`'s SECOND token (`"TRE 0.9.0
  (BSD)"` — not the first, unlike pcre2's/onig's own convention);
  `refusal_class` derivation that separates TRE's syntax-error codes from
  its OVERLOADED `REG_ESPACE` (compile-time length cap vs genuine OOM,
  indistinguishable by code alone — the driver reports the pattern's own
  byte length so the adapter can tell them apart by comparing against
  `TRE_MAX_RE`).
- `testees/tre/configs.toml` — `tre-default` ONLY. TRE's three bounds
  (`TRE_MAX_RE`/`TRE_MAX_STRING`/`TRE_MAX_STACK`) are fixed compile-time
  constants with no `tre_set_*`-shaped configuration function anywhere —
  there is no second config to propose.
- `testees/tre/CLAUDE.md` — the four required sections (a–d: compile-cost
  definition, `consumed_length` convention, the config and why it's the
  whole roster, the convention + every syntactic divergence this lane
  found), plus the whole-subject wrap derivation, the I-72 lesson, the
  `refusal_class`/gave-up design, and the `automaton_class` rationale.
- `bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` gains
  `tre-default`. `patterns.rxt` regenerated; `gen_patterns.py --check`,
  `gen_provenance.py --check`, `gen_variants.py --check` all pass
  unchanged (64 patterns, 13 families).
- `docs/dev/measurements/probe_tre_capability_census.py` +
  `2026-09-17-tre-capability-witness-census.txt` — three passes: one
  isolated witness per `REQUIRES_VOCAB` token (17), all 64
  `bench/capability` corpus patterns, and MATCH-GRAIN behavioral
  confirmations (not just compile/refuse) for every surprising finding
  below.
- `tools/selfcheck.py`'s `check_high_byte_pattern_argv` gains a
  `tre-default` arm — additive, verified in isolation.

## CS5 resolved by witness (the brief's own mandate)

**`named-groups`: UNSATISFIED.** Both spellings refuse outright:
`(?<name>a)` and `(?P<name>a)` both give `tre_regncompb failed (code 2):
Invalid regexp`.

**`free-spacing`: UNSATISFIED.** `(?x) a b c` refuses the same way (code 2).

Neither was assumed from TRE's POSIX ancestry — both compiled through the
real adapter before being declared either way.

## The capability declaration

**SATISFIED** (5 of 17 `REQUIRES_VOCAB` tokens, every one confirmed at
MATCH grain, not compile alone): `backrefs`, `span-reporting`,
`non-utf8-subject`, `captures`, `true-end-anchor`.

**UNSATISFIED** (12): `lookaround`, `lookbehind-variable`,
`possessive-quantifier`, `atomic-group`, `recursion`, `conditionals`,
`k-reset`, `control-verbs`, `unicode-properties`, `named-groups`,
`free-spacing`, `callouts`.

Corpus cross-check: 41/64 `bench/capability` patterns compile through
`tre-default`; every refusal is accounted for by the declared-missing set
(details and two under-tagged corpus patterns in `testees/tre/CLAUDE.md`
item (d).5).

## Four SILENT MISPARSE hazards found (none refuse — this is worse)

TRE compiles four PCRE-syntax constructs without complaint, silently
reinterpreting them rather than refusing, confirmed BEHAVIORALLY (a
compile-success verdict alone would have missed all four — the L5 lesson
`testees/onig/CLAUDE.md` names, applied here to something the onig census
didn't encounter):

1. **`\K` (k-reset)** — compiles, `a\Kb` MATCHES `"aKb"` literally
   (backslash before a non-special letter drops silently to the bare
   letter). NOMATCH on `"ab"` proves no keep-reset ever fires.
2. **`(*FAIL)`/`(*ACCEPT)`/`(*SKIP)` (control-verbs)** — each compiles as
   an ORDINARY CAPTURING GROUP with the leading `*` silently dropped:
   `a(*FAIL)` matches `"aFAIL"` literally (group 1 = `"FAIL"`), refuses
   `"a*FAIL"`. None ever behaves as a control verb.
3. **`\g<1>` (the one recursion spelling that compiles)** — same hazard
   as `\K`: matches `"ag<1>b"` literally, refuses the genuinely-recursive
   `"aabb"`. No recursion capability exists under ANY spelling tried
   (five spellings: two silently misparse, three refuse outright).
4. Beyond `REQUIRES_VOCAB`: **TRE has NO `\xHH` hex-escape at all**
   (`\x93` compiles as literal `"x93"`) — this is why the SHARED
   cross-engine I-72 witness (`\x93[\x20-\x7e]*\x94`) is the wrong
   pattern for TRE; this lane's own I-72 arm uses the raw bytes as a
   literal pattern instead.

## A corpus-level portability finding beyond the capability vocabulary

**POSIX bracket expressions give backslash NO special meaning at all.**
A PCRE-style `\-`/`\xHH` escape inside a class is read as a literal
backslash and can become a RANGE ENDPOINT: `[a-zA-Z0-9.@_\-+]` fails with
`REG_ERANGE` ("Invalid character range") because `\` (0x5C) to `+`
(0x2B) is a descending range. **Three `bench/capability` corpus patterns
hit this — all three tagged with NO `requires-*` token at all**
(`wild-waf-crs-942500-comment-obfuscation`,
`wild-secrets-username-password-pair`,
`wild-datetime-datefinder-alternation` — families 3/4/5's own "none
expected to refuse" invariant). The SAME mechanism also refuses
`bench/email`'s own RFC 5322 `orig.rx` pattern (its `\x01-\x08`-style
hex-escape ranges inside classes), confirmed live via `pcrecbench quick`.

## A real bug this lane found and fixed in its OWN code, before any measurement used it

**The whole-subject wrap's length arithmetic had an off-by-one**
(`wlen = patlen + 5` where `strlen("^(?:") + strlen(")$") == 6`, not 5) —
it silently TRUNCATED the trailing `$`, so `^(?:ab)$` was actually being
compiled as `^(?:ab)` with no end anchor at all. Caught by the
trailing-newline control (`"ab\n"` should NOT match a true end anchor,
and DID match before the fix) kept in the committed census specifically
because a plain match/no-match pair would not have caught it.

**`classify_giveup` would have silently misclassified every gave-up
row.** An earlier draft declared `giveup_codes = set()` (empty), and
`harness.classify_giveup`'s contract is `code in codes` — an empty set
means EVERY driver `giveup:<code>` answer reclassifies to `crashed`,
the opposite of the driver's own generic-classification design. Fixed to
`set(range(2, 15))` (TRE's full non-OK/non-NOMATCH `reg_errcode_t` range)
before any measurement used the handle.

**`automaton_class` was initially free prose**, which the schema's closed
enum rejects — caught by `pcrecbench quick`'s own validation pass, not by
manual review. Fixed to `"hybrid"` (the closest single token for a
pattern-dependent automaton), with the full explanation moved to
`testees/tre/CLAUDE.md` where prose belongs.

## Validation run (per the boilerplate delivery bar)

**COMPLETE**, no heavy runs launched (the battery's HARD RULE honored
throughout — no `make check-harness`, no `make check`, no multi-minute
CPU-bound run, not even detached):

- `python3 bench/capability/gen_patterns.py --check` — pass (64 patterns,
  13 families).
- `python3 bench/capability/gen_provenance.py --check` — pass (64 rows,
  licence/fidelity/attribution/similarity gate all clear).
- `python3 bench/capability/gen_variants.py --check` — pass (0 rows, v1
  unchanged).
- `make check-schema` — pass, 4 example(s) accepted, 72 sabotage(s)
  rejected for the intended rule, 0 wrong.
- `check_high_byte_pattern_argv` in isolation (python-level, ~seconds) —
  5/5 PASS, including the new `tre-default` arm.
- `pcrecbench quick` scratch cells (scratch tier, never the canonical
  store): `bench/email` `orig` × `search_short` — correctly
  `did-not-compile` (the bracket-escape finding above, confirmed by
  inspecting the written record); `bench/capability` `floor-byte` ×
  `search_short` (10 subjects, 3 trials) — 10/10 pass, tre-default 1.55×
  faster than pcre2-interp on this trivial witness; `floor-byte` ×
  `throughput` — 3/3 pass, 1.38× faster. Both scratch records validated
  and written (never rejected) after the `automaton_class` fix above.

## OWED (explicitly, per the delivery bar)

- **`make check-harness`** (the full 402+/133 gate this lane's changes
  touch: the generic `bench/*/` gates, the new roster row, the new
  selfcheck arm as part of the full suite) — NOT run, per the manager's
  HARD RULE (pcrec's ~7.5h solo battery owns the box). Exact command:
  `make check-harness` from the repo root after merge, on a quiet box.
- **`make check`** (the full suite, same reason) — exact command:
  `make check`.
- **Cross-lane roster reconciliation**: this branch adds `tre-default` to
  `EXT_BENCH_ROSTER` on master's base; sibling branches `lane/l6bre2` and
  `lane/l6bonig` each add their own row the same way. The manager
  re-runs `python3 bench/capability/gen_patterns.py` after all three
  merge to reconcile the final roster order and re-verify
  `gen_patterns.py --check` on the merged tree.
- **A pinned/store measurement of `tre-default`** — none was taken (scratch
  tier only, per this lane's scope); the first real capability-set sample
  including `tre-default` is a future window's job.

## Files touched

- `testees/tre/{adapter.py,driver.c,configs.toml,CLAUDE.md,_probe.rx}` —
  new.
- `testees/CLAUDE.md` — new `tre/` row.
- `bench/capability/gen_patterns.py`, `bench/capability/patterns.rxt` —
  the new roster row, regenerated.
- `tools/selfcheck.py` — the `tre-default` arm in
  `check_high_byte_pattern_argv`.
- `docs/dev/measurements/probe_tre_capability_census.py`,
  `docs/dev/measurements/2026-09-17-tre-capability-witness-census.txt` —
  new, the evidence behind every declaration above.
