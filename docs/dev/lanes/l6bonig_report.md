# lane l6bonig — the Oniguruma adapter (testees/onig/)

Branch `lane/l6bonig`, worktree `worktrees/l6bonig`, HEAD `18d7452`
(single commit; `9fb9ac4` is the branch point). [B7]/L6b, second lane of
the wave chartered at the 2026-09-17 reset (capability_set_v1.md §11.1's
per-engine lane row). Sibling lane `l6bre2` builds `testees/re2/`
concurrently in its own worktree/branch — this report touches nothing
outside `testees/onig/`, `bench/capability/`, `docs/dev/measurements/`,
`docs/dev/lanes/`, `testees/CLAUDE.md` and `tools/selfcheck.py`; the
`EXT_BENCH_ROSTER`/`patterns.rxt` edit in `bench/capability/` is the one
place a merge seam with `l6bre2` is plausible (a second `("re2-*", ...)`
row appended the same way) — the manager's to resolve at merge, not
this lane's.

## Deliverables, against the brief

1. **`testees/onig/` built**: `adapter.py`, `driver.c` (direct-linked
   `#include <oniguruma.h>` / `-lonig` — this box has `libonig-dev`, so
   no dlopen/hand-declared-prototype shim was needed, unlike
   `testees/pcre2/`'s runtime-only situation), `configs.toml`
   (`onig-default` only), `_probe.rx`, `CLAUDE.md` (all four required
   sections: compile-cost definition, `consumed_length` convention, the
   syntax choice and every known divergence this lane found, the
   encoding choice and its consequences). Compiles clean under
   `-Wall -Wextra`, zero warnings.
2. **Config**: `onig-default` only, `testee_id` derives to
   `oniguruma_6.9.10_default-caps-simdna` (confirmed via a real `quick`
   run — record_schema.md §6.4's composition rule, unmodified).
3. **CB5/CB6, mandatory, resolved BEFORE any declaration**:
   - **CB5 (atomic-group)**: SATISFIED, UNCONDITIONALLY. Direct read of
     Oniguruma 6.9.10's `src/regparse.c` (fetched from the upstream
     `v6.9.10` git tag, diffed BYTE-IDENTICAL against this box's
     installed `/usr/include/oniguruma.h` before reading anything):
     `(?>...)` at `regparse.c:7886-7888` carries NO `IS_SYNTAX_OP2`
     guard (unlike its neighbouring cases), so it is parsed under every
     syntax profile; the `BAG_STOP_BACKTRACK` node it compiles to is
     fully wired (7 further references in `regparse.c`, including
     possessive-quantifier lowering reusing the SAME node; 13 in
     `regcomp.c` across optimization/length/emission). Live: `(?>a*)b`
     compiles (reused verbatim from pcrec's own census witness for
     direct comparability).
   - **CB6 (k-reset, `\K`)**: SATISFIED, and ARCHITECTURALLY EQUIVALENT
     to PCRE's own `\K` — not an approximation. `\K` compiles to a
     `SAVE_KEEP` gimmick under `ONIG_SYN_OP2_ESC_CAPITAL_K_KEEP`
     (present in Perl/Perl_NG/Python/Oniguruma/Ruby syntaxes); at match
     time the current position is pushed onto Oniguruma's own
     BACKTRACKABLE stack (`regexec.c:4319-4351`), and on overall match
     success that saved position overrides the reported match START
     (`regexec.c:3070,3121,3127,3141`) without moving the actual search
     anchor — precisely PCRE's mechanism. Live: `a\Kb` compiles;
     `bench/email`'s own `quick --regime match` (5/5 subjects agreeing
     with the oracle on the whole-subject artifact) is independent
     end-to-end corroboration.
   - Full derivation with exact line numbers:
     `testees/onig/CLAUDE.md`'s "ext bench" section and
     `docs/dev/measurements/2026-09-17-onig-capability-witness-census-
     6.9.10.txt`.
4. **Full capability witness census** (the L5 lesson: "three wrong
   first-cut declarations"), archived with a reproducing script
   (`docs/dev/measurements/probe_onig_capability_census.py` +
   `2026-09-17-onig-capability-witness-census-6.9.10.txt`):
   - **Pass 1** — one or more isolated witnesses per REQUIRES token (17
     tokens). **13 SATISFIED**: `backrefs`, `lookaround`,
     `possessive-quantifier`, `atomic-group`, `recursion`,
     `conditionals`, `k-reset`, `named-groups`, `free-spacing`,
     `span-reporting`, `non-utf8-subject`, `captures`,
     `true-end-anchor`. **4 NOT**: `lookbehind-variable` (all
     alternatives of one lookbehind must share ONE fixed width, stricter
     than per-branch-fixed), `control-verbs` (`(*ACCEPT)` refused;
     `(*FAIL)`/`(*SKIP)` compile only by REGISTRY COINCIDENCE with
     Oniguruma's own, semantically different callout mechanism —
     withheld wholesale per the same precedent `pcre2-dfa`'s own row
     sets), `unicode-properties` (**the census's own "wrong first-cut"
     catch**: `\p{Alpha}` compiles but `\p{L}` — a REAL Unicode category,
     the shape every PCRE corpus pattern actually uses — does not, under
     `ONIG_ENCODING_ASCII`; a narrower, different vocabulary, not a
     subset by spelling coincidence), `callouts` (PCRE's `(?Cn)` spelling
     not recognised at all).
   - **Pass 2** — all 64 real `bench/capability` corpus patterns through
     the real adapter: **62/64 compile**. The two refusals
     (`negation-scope-lookbehind-var`, tagged `requires-lookbehind-
     variable`; `balanced-parens-rec`, tagged `requires-recursion`)
     reproduce their isolated witness's EXACT `ONIGERR_*` code, and
     `balanced-parens-rec`'s refusal is specifically PCRE's `(?R)`
     shorthand — `(?1)`/`(?&name)`/`(?0)`/`\g<n>` all compile, confirmed
     on the corpus's OTHER two `requires-recursion` patterns, which
     compile clean. `recursion` therefore stays SATISFIED and this one
     pattern is left to fail HONESTLY as its own `did-not-compile`
     (`refusal_class: syntax`) rather than being hidden behind a
     wholesale token withhold — a documented SPELLING gap, not a
     capability gap.
   - `bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` gains the
     `onig-default` row; `patterns.rxt` regenerated (diff scoped to
     exactly the new roster block — 15 lines) and `--check` clean (also
     re-ran `gen_provenance.py --check`, `gen_variants.py --check`,
     `gen_expectations.py --check` — all green, nothing else moved).
5. **The I-72 lesson (mandatory)**: pattern bytes travel end to end via
   a FILE (`_compile_one`'s `patfile`), never argv text — the same
   convention `testees/pcre2/adapter.py` uses, so this adapter was never
   exposed to I-72's mojibake bug class (a `str` argv element's
   `os.fsencode` re-encoding) in the first place. Confirmed LIVE with
   the exact same pattern/subject pair `check_high_byte_pattern_argv`
   uses for pcrec (`\x93[\x20-\x7e]*\x94` over `\x93hello\x94`, matched
   `[0,7)`), both as an isolated driver invocation and through
   `pcrecbench quick` end to end. Wired into
   `tools/selfcheck.py:check_high_byte_pattern_argv` as a third arm
   (`onig-default`, gated on `"onig" in _ad.discover()` so the check
   degrades gracefully if the adapter were ever absent) — verified
   passing directly (see "Validation" below).
6. **`make check` stays green — OWED, running detached, DO-THEN-FINISH**.
   `make check-harness` launched in the l6bonig worktree at commit
   `18d7452`, background PID tracked by the harness (Bash
   `run_in_background: true`), log
   `/tmp/claude-1001/-home-duxevents-pcrec-bench/18ca7e26-4ced-4281-a92d-0330c831ba9e/scratchpad/check_harness_out.txt`,
   completion line `DONE rc=<code>` appended at the end. Expected ~20
   min per the Makefile's own stated estimate; this new adapter adds no
   new check function to the suite (no `bench/*/` set is onig-specific,
   and the one selfcheck edit is additive to an existing function), so
   the ONLY numbers this run should move are the total PASS count (+1,
   the new onig arm inside `check_high_byte_pattern_argv`) and nothing
   else — verified independently in isolation already (see
   "Validation"). **If the manager or a fresh agent resumes this lane:
   check the marker line in that log file first** — a `DONE rc=0` means
   green with the expected +1 count; anything else is a real finding to
   read from the same file's tail, not re-run blind.
7. **Scratch only, `store/` untouched**: every `quick`/direct-adapter
   exercise in this lane wrote to `build/scratch-store/` (the default)
   or nowhere at all (bare python calls with `tmp = tempfile.mkdtemp`);
   `git status` on `store/` is unchanged (see below).

## Validation run so far (before the detached check-harness completes)

All of the following were run directly in this worktree, this session,
and are NOT part of `make check` — they are the lane's own end-to-end
confirmation, quoted here so the handback is self-contained:

- **Driver smoke** (`gcc -O2 -std=gnu11 -Wall -Wextra`, zero warnings):
  compile-only (plain + whole-subject, 1 and 2 trials), `search` mode
  over two subjects (captures, consumed_length, NCAPS all correct),
  `match` mode via the whole-subject artifact (a full match and a
  correctly-REJECTED partial match — `abcbdX` under `(?:a(b|c)+d)\z`
  answers `nomatch`, proving the end-anchor is real), `--find-all`
  (NMATCHES=3 on `ab` over `ababab`), the I-72-style high-byte witness,
  and the ReDoS gave-up witness (below).
- **Adapter-level smoke** (through `pcrecbench.adapters.discover()`,
  bypassing the CLI): `describe()` renders a complete, schema-shaped
  testee block; `binary_identity()` resolves the real
  `/usr/lib/x86_64-linux-gnu/libonig.so.5.5.0` + its sha256;
  `compile()` on a malformed pattern (`a(b`) returns `did-not-compile`
  with `refusal_class: syntax` (code -117); on a 5000-deep nested group
  returns `did-not-compile` with `refusal_class: size-limit` (code -16,
  `ONIGERR_PARSE_DEPTH_LIMIT_OVER`) — both branches of the
  `refusal_class` derivation exercised live.
- **Full harness integration** (`pcrecbench quick`, scratch tier, real
  records written under `build/scratch-store/`):
  - `--subbench email --pattern orig --regime search --testee
    onig-default --vs pcre2-interp --subjects 5` → **5/5 pass** both
    testees, `onig-default` 1.39× faster on this cell.
  - `--regime match` (exercises the whole-subject `\z`-wrapped form and
    the `onig_match`-at-zero mechanism) → **5/5 pass** both testees.
  - `--regime throughput` (`--find-all`) → **2/2 pass**.
  - Every run wrote to `build/scratch-store/records/email-specimen@0.2/
    oniguruma_6.9.10_default-caps-simdna/...jsonl` — `testee_id`
    correctly derived, never hand-typed.
- **The ReDoS gave-up witness**: `(a+)+$` over 40 `a`s + one
  non-matching byte, run through the raw driver with
  `--subject-timeout 20` — answered `giveup:-17:retry-limit-in-match
  over` in **0.21 s**, confirming Oniguruma's DEFAULT retry budget
  (10,000,000, `regint.h`'s `DEFAULT_RETRY_LIMIT_IN_MATCH` — NOT
  unlimited) is low enough to fire on a strong ReDoS witness with NO
  special configuration. This is the deliverable's own ask ("If
  retry-limit fires at default settings on a ReDoS witness, that is
  `gave-up` — record it, don't raise") confirmed, not merely
  documented.
- **`check_high_byte_pattern_argv`, run in isolation**: 5/5 PASS
  (the two pcrec arms, the new onig arm, the pcre2 reference, the
  UTF-8-corruption control).
- **`bench/capability` generators**: `gen_patterns.py` /
  `gen_patterns.py --check` / `gen_provenance.py --check` /
  `gen_variants.py --check` / `gen_expectations.py --check` — all exit
  0, all green, the `patterns.rxt` diff scoped to exactly the new
  `onig-default` roster block (no other pattern's bytes moved).

## Deviations from the brief, and why

- **`onig-lowretry` is documented, not wired** — exactly as the brief
  specified ("a LATER config: document it in your CLAUDE.md, do not
  wire it"). `testees/onig/CLAUDE.md`'s "gave-up" section states why it
  is not needed to demonstrate the mechanism: `onig-default`'s
  UNMODIFIED retry budget already gives up on a real ReDoS witness.
- **One incidental fix outside strict scope**: `testees/CLAUDE.md`'s
  `pcre2/` row was missing `pcre2-dfa` (a pre-existing omission from
  [B42] L6a, unrelated to this lane) — corrected while adding the
  `onig/` row in the same table, since leaving a visibly-wrong adjacent
  line in a file this lane was already editing seemed worse than a
  one-line accurate fix. Flagged here rather than left silent; trivial
  to revert if the manager prefers a narrower diff.
- **`refusal_class` (capability_set_v1.md §5.5) is IMPLEMENTED**, not
  merely documented — the design note lists Oniguruma among the engines
  whose `ONIGERR_*` gives "a closed, structural signal" fit for this
  declaration, and no other adapter in the repo has built it yet (grep
  confirmed zero prior uses of the key anywhere in `schema/`,
  `pcrecbench/`, `testees/`). Built here because the census's own
  `did-not-compile` witnesses (a syntax error, a parse-depth overflow)
  made the two-way classification straightforward and directly useful
  for a future reader distinguishing pcrec's own `did-not-compile`
  refusals from `onig-default`'s NOT NEEDING the pre-compile capability
  policy to explain a corpus refusal (`balanced-parens-rec`'s own
  `refusal_class: syntax` is exactly that signal). This is new
  machinery beyond the brief's explicit list — flagged for the manager's
  awareness, not hidden as if it were always there.
- **Did not build an `onig-utf8` config** or otherwise test
  `ONIG_ENCODING_UTF8` — out of scope (the brief names ASCII vs UTF8 as
  a documentation deliverable, "state ... its consequences", not a
  second config to build); `testees/onig/CLAUDE.md` names this
  explicitly as untested rather than implying the UTF8 encoding would
  behave identically.
- **Did not audit `control-verbs`' `(*FAIL)`/`(*SKIP)` compile-coincidence
  for BEHAVIORAL equivalence to PCRE** (would need a live-match witness
  with an actual backtracking control-verb effect, not just a compile
  check) — named as an open, unverified nuance in both
  `testees/onig/CLAUDE.md` and the archived census rather than silently
  assumed either way; the `control-verbs` DECLARATION is unaffected
  either way (withheld regardless, on `(*ACCEPT)`'s clean refusal
  alone).

## Files touched

- `testees/onig/{adapter.py,driver.c,configs.toml,_probe.rx,CLAUDE.md}`
  — new.
- `bench/capability/gen_patterns.py` — `EXT_BENCH_ROSTER` gains the
  `onig-default` row (with its own derivation comment).
- `bench/capability/patterns.rxt` — regenerated (the new roster block
  only).
- `bench/capability/CLAUDE.md` — one paragraph noting the roster
  addition and pointing at the census.
- `docs/dev/measurements/probe_onig_capability_census.py`,
  `2026-09-17-onig-capability-witness-census-6.9.10.txt` — new, the
  mandatory CB5/CB6/census archive.
- `docs/dev/measurements/CLAUDE.md` — index rows for the two files
  above.
- `testees/CLAUDE.md` — the new `onig/` row (+ the incidental
  `pcre2-dfa` fix noted above).
- `tools/selfcheck.py` — `check_high_byte_pattern_argv` gains the third
  (`onig-default`) arm.
- `docs/dev/lanes/l6bonig_report.md` — this file.

## Handback

Branch `lane/l6bonig` at commit `18d7452`, committed, report committed
in the same commit-set (this file will be committed alongside any
check-harness-result follow-up — see below). **`make check-harness` is
the one OWED item**: launched detached per DO-THEN-FINISH, log path and
completion-line contract stated above under deliverable 6. Everything
else in the brief is COMPLETE and independently validated (see
"Validation run so far"), not merely asserted.

Not merged — the manager merges, and this lane expects a merge seam
with `l6bre2` in `bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER`
(a second engine's row appended the same way) and possibly
`patterns.rxt`'s regenerated `ext bench` block, both trivially
resolvable by re-running `gen_patterns.py` after both rows are present
in one tree.
