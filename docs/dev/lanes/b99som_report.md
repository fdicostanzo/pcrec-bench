# Lane `b99som` — delivery report

[B99] ([B92]'s own OWED pair, `docs/dev/plan.md`): (a) build
`vectorscan-block-som-utf8`, the `vectorscan-block-som`/UTF-8
combination, exactly the way `vectorscan-block-nosom-utf8` was built at
[B77] U2 — its OWN witness census, compile/witness-level only, no
timing, no window; (b) `vectorscan-block-som`'s capability
`EXT_BENCH_ROSTER` declaration in `bench/capability/gen_patterns.py`
(plus whatever that regenerates, `gen_patterns.py --check` passing).

Worktree `worktrees/b99som`, branch `b99som` from `master` (per the
brief's own naming, not the boilerplate's default `lane/<lane>` — the
task named the branch explicitly). Base commit `53ba4375` (master, "plan:
[B97] [B98] [B99] started"). One commit:

- `fba0eac` — everything: the roster row + regenerated `patterns.rxt`,
  the new config + the `build_flags` accuracy fix, the census script +
  archive, all four CLAUDE.md updates, this report to follow.

Box: pcrecdev1's ASan battery held the box for the whole session
(load ~3.0-3.1 throughout — the run was granted until ~21:18 EDT, and my
session ran ~18:5x-19:0x EDT, so it was still live the entire time).
Nothing here needed the box quiet: every check below is either a
compile/witness census (the same stated exemption every prior
[B77]/[B92] census carries) or a targeted selfcheck function run
directly, none of them a timing.

## Order of work

(b) first, since (a)'s own census reads `vectorscan-block-som`'s roster
row live off `gen_patterns.py`'s `EXT_BENCH_ROSTER` for its own section D
(a UTF-8 sibling's declaration carries over from its BYTE sibling, never
re-witnessed from scratch) — the same discipline
`probe_b77u2_utf8_witness_census.py` used for every other `-utf8`
config's census.

## Charter-vs-committed checklist

### (b) `vectorscan-block-som`'s `EXT_BENCH_ROSTER` row — BUILT

Added right after `vectorscan-block-nosom`'s own row in
`bench/capability/gen_patterns.py`: `nosom`'s exact six-token exclusion
set MINUS `span-reporting` (i.e. `nosom`'s six SATISFIED tokens PLUS
`span-reporting`). Basis, all already-established evidence, none
re-derived from scratch:

- SOM changes nothing about which SYNTAX Hyperscan accepts — the eleven
  refused tokens (backrefs, lookaround, lookbehind-variable,
  possessive-quantifier, atomic-group, recursion, conditionals, k-reset,
  control-verbs, callouts, plus `captures`, withheld structurally) refuse
  for the identical reason on both configs; `hs_compile` never even sees
  `HS_FLAG_SOM_LEFTMOST` until parsing succeeds.
- What SOM changes is EXECUTION-MODEL: `span-reporting`, which `nosom`'s
  own row already flagged in its own comment ("the som config,
  documented not built, would satisfy [span-reporting]") — now BUILT,
  and witnessed live by `[B92]`'s own `check_vectorscan_som` (arms 3-4:
  real span/NMATCHES agreement with the oracle on three unambiguous
  witnesses, plus the documented leftmost-longest divergence asserted BY
  VALUE, never merely "differs").
- The SOM-only restriction's two corpus casualties (`evil-alt-nested`,
  `trim-nested-star`, both `family=redos-nested`) carry NO `requires-*`
  tag at all (checked directly against `patterns.rxt`), so this
  restriction touches none of the six declared tokens — confirmed, not
  assumed.

`python3 bench/capability/gen_patterns.py` regenerated `patterns.rxt`
(the ONLY diff: the new roster line + the new `capabilities
vectorscan-block-som` block, verified with `git diff --stat` — nothing
else moved, `patterns/*.rx` untouched). `gen_patterns.py --check` is
CLEAN (round-trips through the pinned `pcrec-ce658cb7` binary via
`--list-source`).

### (a) `vectorscan-block-som-utf8` — BUILT

`testees/vectorscan/configs.toml`: new `[testees.vectorscan-block-som-
utf8]` entry, `engine_mode = "block-som"`, `encoding = "utf8"` — the same
two-key shape every other `-utf8` config on this roster uses.

**No driver change was needed.** `driver.c`'s `--som` and `--encoding
utf8` were already independent argv flags (`hs_flags |=
HS_FLAG_SOM_LEFTMOST` applied AFTER the encoding is parsed, unconditional
on `som_mode` alone); `adapter.py`'s `_compile_one`/`measure` already
read `som` and `utf` off the config independently and append both flags
when both are true. [B92]'s own CLAUDE.md section had already stated
this composes "smoke-tested by hand" — confirmed here by the real
census (section G below), not merely trusted.

**One real code fix was needed**: `describe()`'s `build_flags` text.
Before this lane, the base clause was computed purely from `som`
(`"hs_compile flags HS_FLAG_SOM_LEFTMOST -- HS_FLAG_UCP/HS_FLAG_UTF8
never set"`) and the `enc == "utf8"` clause was appended UNCONDITIONALLY
in a form written for `som=False` (`"... in place of the 0 above"`) —
which, for `som=True, enc="utf8"`, would have produced accurate-sounding
but WRONG text: claiming `HS_FLAG_UTF8` "never set" in the same sentence
that then says it replaces "the 0" (there was no 0 — the base was
`HS_FLAG_SOM_LEFTMOST`). Fixed with a dedicated `som and enc == "utf8"`
branch, kept structurally separate from the other three combinations'
text so those three stay BYTE FOR BYTE unchanged — verified directly
(not merely by code inspection):

```
vectorscan-block-nosom       (unchanged text, verified against committed record via check_encoding_axis)
vectorscan-block-nosom-utf8  (unchanged text, verified against committed record via check_encoding_axis)
vectorscan-block-som         (unchanged text — no committed record exists yet, so this combination's
                               text was also free to fix, and IS fixed: "HS_FLAG_UCP/HS_FLAG_UTF8
                               never set" -> the census shows this is still literally true for som-byte,
                               so nothing needed to move there; only the enc==utf8 branch needed fixing)
vectorscan-block-som-utf8    NEW, accurate: "hs_compile flags HS_FLAG_SOM_LEFTMOST -- HS_FLAG_UCP
                               never set ...; hs_compile flags ALSO HS_FLAG_UTF8 ... beside
                               HS_FLAG_SOM_LEFTMOST above -- HS_FLAG_UCP still never set"
```

**Witness census** (compile/witness-level only, no timing, no window):
`docs/dev/measurements/probe_vectorscan_som_utf8_witness_census.py` +
its archive `2026-09-26-vectorscan-som-utf8-witness-census.txt`, mirroring
[B77] U2's per-(config, REQUIRES token) discipline AND [B92]'s own
SOM-vs-nosom corpus census at once, over EIGHT sections (A-H, the
script's own docstring numbers them). Findings:

- **Mechanically composes exactly as predicted.** Section G: `α|αβ` over
  UTF-8-encoded "αβ" (4 bytes) reads `[0,4)` count 1 under
  `som-utf8`(leftmost-longest) against the oracle's `[0,2)` count 1
  (leftmost-first) — the SAME divergence shape plain `som` shows on
  ASCII (`a|ab`/"ab"), now CONFIRMED on genuinely multi-byte content,
  not merely assumed to survive encoding.
- **ONE genuinely new finding, invisible to both parent censuses**:
  section H, `(*UCP)\w+` over Cyrillic text — clean under
  `vectorscan-block-nosom-utf8` (compiles, per the 2026-09-25 archive) —
  REFUSES under `som-utf8` with Hyperscan's own `"Pattern is too
  large."`, the IDENTICAL diagnostic HS_FLAG_SOM_LEFTMOST's
  history-tracking budget uses on the isolated `.*a.{40,}` witness both
  SOM censuses share. `(*UCP)\d{4}` and `(*UCP)a\sb` still compile fine
  under `som-utf8`. So `unicode-class-scope`, SATISFIED for
  `nosom-utf8`, is NOT satisfied for `som-utf8` — a real SOM x UTF-8 x
  `(*UCP)` interaction. `bench/capability`'s 64-pattern corpus contains
  NO `(*UCP)` pattern at all, so [B92]'s own corpus-only census could
  never have surfaced this, and U2's census never combined SOM with
  UTF-8 — this lane's census is the first place either mechanism was
  exercised together.
- **Everything else transfers unmoved** (sections C, F, H's second
  witness): the corpus SOM-only compile-cost census (section F, all 64
  `bench/capability` patterns, plain form) reproduces [B92]'s byte-mode
  finding EXACTLY — the SAME two patterns (`evil-alt-nested`,
  `trim-nested-star`), the SAME diagnostic text, since neither uses
  non-ASCII bytes or `(*UCP)`; the documented `\b`-under-UCP breakage
  (`(*UCP)\bМосква\b`, utf8_set_v1.md 7.6) reproduces IDENTICALLY on
  `som-utf8` and its `nosom-utf8` encoding sibling (section H); the
  `\p{Greek}` Script-vs-Script_Extensions reading (section C) is
  UNCHANGED by SOM (both read Script, not Script_Extensions — a
  divergence from the oracle shared with `nosom-utf8`, not new here).
- **No `EXT_BENCH_ROSTER` row for the new config** — the same convention
  every other `-utf8` config on this roster follows (no `-utf8` id
  appears in `EXT_BENCH_ROSTER` anywhere; the roster is keyed by
  `engine_mode`, never encoding). The census's own final section states
  what it WOULD declare if it had a row: 7/20 — `nosom-utf8`'s own 7
  MINUS `unicode-class-scope` (the new narrowing) PLUS `span-reporting`
  (SOM's own execution-model gain) — the union of both parents' own
  changes, nothing else moved.

## Documentation updated

- `testees/vectorscan/CLAUDE.md` — the `No UTF-8 sibling yet` section is
  REPLACED by a new `` `vectorscan-block-som-utf8` — [B99] `` section
  stating the build, the `build_flags` fix, and all census findings
  above.
- `testees/CLAUDE.md`'s per-engine roster table row for `vectorscan/` —
  extended with `vectorscan-block-som`'s new roster declaration and
  `vectorscan-block-som-utf8`'s own entry.
- `docs/dev/measurements/CLAUDE.md` — new bullet for the probe script +
  archive, in the file's existing chronological list.
- **`root CLAUDE.md`'s adapter paragraph is NOT touched** (the brief's
  own instruction — that paragraph is the manager's). Proposed wording
  for the manager to fold in at the next edit of that paragraph's
  `vectorscan/` clause (appending after the existing
  `vectorscan-block-nosom-utf8` mention):

  > and (since [B99], 2026-09-26) `vectorscan-block-som-utf8`
  > (`vectorscan-block-som`'s own UTF-8 sibling: HS_FLAG_UTF8 ORed onto
  > HS_FLAG_SOM_LEFTMOST, never HS_FLAG_UCP, FULL grain — mechanically
  > composes as predicted, and surfaces one new finding neither the SOM
  > nor the UTF-8 census alone could show: `(*UCP)\w+` refuses under
  > SOM+UTF-8 with Hyperscan's own size-budget diagnostic though it
  > compiles clean under plain UTF-8, so `unicode-class-scope` narrows
  > under SOM) — a vectorscan-only addition; the paragraph's "twenty
  > pinned pcrec configs" tally is unaffected (this lane touches no
  > pcrec config)

## Every pre-existing testee_id proven unmoved

`check_encoding_axis`'s own committed-record arm ("every COMMITTED
record a pre-existing config derives re-derives byte-identically") is
UNCHANGED and PASSES post-lane, including its one `vectorscan` row
(`vectorscan-block-nosom`'s own committed record) — this is the
strongest available proof `nosom`'s `build_flags`/`config_extra`/
`testee_id` never moved, since it compares against a REAL committed
record, not merely a fresh re-derivation. `vectorscan-block-nosom-utf8`
has a committed record too (`store/records/utf8@0.1/`) and is covered by
the SAME arm's `_B77U2_NEW` shape check (arm 2), also passing.
`vectorscan-block-som` (byte) has NO committed record yet, so there is
nothing for a byte-identity arm to check there — its own
`check_vectorscan_som` (identity + behavior) is the control instead, and
it is UNCHANGED and PASSES (6/6).

## Validation run (targeted; box busy — see below for what is OWED)

All run directly against the real code, `<4 min` each, no full suite:

- `python3 bench/capability/gen_patterns.py --check` — CLEAN (round-trips
  the pin).
- `check_capability_policy` + `check_capability_policy_noop_elsewhere`
  (`tools/selfcheck.py`) — 13/13 PASS; the roster addition does not
  disturb the pre-compile policy on any set.
- `check_vectorscan_som` — 6/6 PASS, unaffected by this lane's changes
  (both configs' identity/behavior unchanged).
- `check_encoding_axis` — 7/7 PASS, INCLUDING the committed-record arm
  (proves `nosom`/`nosom-utf8`'s text is byte-identical to before this
  lane's `build_flags` refactor).
- `check_high_byte_pattern_argv` — 9/9 PASS (unrelated to this lane;
  confirms the vectorscan adapter is otherwise healthy).
- Direct schema validation of both new configs' `describe()` blocks
  against `schema/record.schema.json`'s `testee` sub-schema — clean for
  both `vectorscan-block-som` and `vectorscan-block-som-utf8`.
- `pcrecbench quick --subbench capability --pattern floor-byte --regime
  search_short --testee vectorscan-block-som-utf8 --subjects 3 --iters 1
  --trials 1` — ran end to end (3/3 subjects measured, a scratch record
  written and schema-validated by `store.write`); `inconclusive-load` is
  expected and correct given the box's load (~3.0, pcrecdev1's battery)
  — this is a functional smoke, never a timing claim, and the record
  lives under the gitignored `build/scratch-store/`, never committed.

## OWED

- **The full `make check` / `make check-harness` run** — named exactly
  as the brief required, not attempted here (box busy with pcrecdev1's
  ASan battery through ~21:18 EDT; the brief capped individual checks at
  <4 min and forbade the full suite). Command: `make check` from the
  repo root (or `worktrees/b99som` once merged to `master`) once the box
  is free. No NEW check function was added by this lane (the census is
  documentation, never a gate), so `make check`'s counts should move by
  AT MOST the corpus-wide totals `check_capability_policy` prints for
  the new roster row — none moved in the targeted run above (13/13 PASS,
  same as before this lane's roster addition).
- **`root CLAUDE.md`'s adapter paragraph** — proposed wording above,
  the manager's own edit.
- A `vectorscan-block-som-utf8-utf8` third-order sibling does not exist
  and was never asked for; not applicable.

## Files touched

- `bench/capability/gen_patterns.py`, `bench/capability/patterns.rxt`
- `testees/vectorscan/configs.toml`, `testees/vectorscan/adapter.py`
- `testees/vectorscan/CLAUDE.md`, `testees/CLAUDE.md`,
  `docs/dev/measurements/CLAUDE.md`
- `docs/dev/measurements/probe_vectorscan_som_utf8_witness_census.py`
  (new), `docs/dev/measurements/2026-09-26-vectorscan-som-utf8-witness-census.txt`
  (new)
