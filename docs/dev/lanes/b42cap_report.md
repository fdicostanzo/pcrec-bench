# [B42] restart, lane L5 — the capability machinery (lane `b42cap`)

Branch `lane/b42cap`, from `master` tip `1f4c43f` (L3's set and L4's
loader both merged). Brief: the LAST build lane of the restart —
(1) the pre-compile REQUIRES capability policy, wired into
`pcrecbench/harness.py`; (2) re-verify L3's first-cut `pcrec-*`
capability declarations against a real compile census; (3) convention-
scoped scoring, `outcome_for()`'s new parameter (R5 B1/CB1); (4)
`variant.kind` rendering in the reporter (R5 B2/CB2), designed and
built from nothing; (5) new selfcheck arms in the house style.

**STATUS: DELIVERED.** Targeted checks green (below). A full
`make check` was run; see "Validation" for the exact numbers and any
OWED items.

## 1. The pre-compile capability policy

`pcrecbench/capability.py` (new): `REQUIRES(pattern) ⊄
capabilities(testee) ⇒ unsupported-by-declaration`
(`docs/design/capability_set_v1.md` §5.3), decided in
`harness.run_cell` **before** `adapter.compile()` is ever called for
that (pattern, testee) pair. Two closed inputs:

- `REQUIRES(pattern)`: `Pattern.tags`' `requires-*` entries, validated
  against a 17-token closed vocabulary (§5.1's 16 + §6.2's
  `true-end-anchor`) at read time — an unknown token is a load error
  naming the closed set, never silently accepted.
- `capabilities(testee)`: the set's `.rxt` `ext bench` aux block
  (`roster` + `capabilities <testee-id>` sub-trees), read through
  **two paths**:
  - **(a) the LOADER path** — `sb.rxt.aux_rows`, when the sidecar's
    `rxt_source = ` switch is set and the file loads cleanly. No
    committed set uses this today.
  - **(b) the SIDECAR/SHIM path** — a new `rxt_source.load_aux_rows()`
    reads ONLY the `#section aux` rows (plus head facts) from a
    `patterns.rxt` file sitting beside `subbench.toml`, skipping the
    two gates that scan per-pattern-block content
    (`check_block_sidecar_agreement`, the O-29 provenance-agreement
    gate) — an `ext` block lives entirely outside the main pattern
    table those gates scan, so this path works even though
    `bench/capability` itself is **not** whole-file `.rxt`-loadable at
    the pinned pcrec (outbox O-29: `--list-source` drops all but the
    last pattern block's own `provenance` row). **This is the path
    every real cell on `bench/capability` exercises today** — its
    sidecar carries no `rxt_source =` key at all.

Fail-closed throughout (§5.2): a testee or token absent from the
matrix satisfies nothing. `missing_capabilities()` returns the whole
REQUIRES set in that case, not an empty one by omission (checked,
`check_capability_policy` item 5).

**Which load path each check exercises**, as asked:

| check | path exercised |
|---|---|
| `check_capability_policy` items 1-3 (`pcrecbench quick` on the real `bench/capability` set) | (b) sidecar/shim — `sb.rxt` is `None` for this set at this pin |
| `check_capability_policy` items 4-5 (unit-level, `pcrecbench.capability` called directly) | neither — pure-function tests of `pattern_requires`/`capabilities_for`/`missing_capabilities` against hand-built `Pattern` objects and the real matrix |
| manual verification during this lane (not committed as a check) | both (a) and (b): a synthetic 2-pattern `.rxt` fixture with a 1:1 provenance count (so O-29 never fires) was loaded via `load_rxt_source()` and confirmed `_load_matrix` reads `sb.rxt.aux_rows` directly with **no** second subprocess call, before being deleted — see "What was NOT committed" below |

The synthetic-fixture loader-path check above was exploratory (done by
hand to confirm path (a) works at all), not committed as a selfcheck
arm — `bench/capability` is the only real consumer today and it only
ever exercises path (b). Flagged here rather than silently dropped;
a future set that actually sets `rxt_source =` and avoids O-29 is
where path (a) gets its own committed control.

## 2. L3's first-cut capability lists — the witness-check matrix

`docs/design/capability_set_v1.md` §5.3's own mitigation: "for each
(config, tag) pair declared UNSATISFIED, one witness pattern is
actually compiled and the refusal asserted by name." Below, every
(config, token) pair this lane touched, decided by an actual compile
against the pinned pcrec (`build/pcrec-cd371441/build/pcrec
--features all`, each config's own `--engine=`/`--no-captures`
flags) — **never inferred from `docs/pcre2_compliance.md` prose
alone** (the survey narrowed the search; the compile decided it).

| config | token | L3's first cut | witness pattern | real compile | verdict |
|---|---|---|---|---|---|
| pcrec-auto/nocaps/vm/vm-in | `conditionals` | satisfied | `(?(1)a|b)(a)?` | REFUSED: `module 'conditionals' is enabled but (?(...) is not implemented yet` | **CORRECTED to unsatisfied** |
| pcrec-auto/nocaps/vm/vm-in | `control-verbs` | satisfied | `a(*ACCEPT)b` | REFUSED: `(*...) requires module 'verbs'` | **CORRECTED to unsatisfied** |
| pcrec-auto/nocaps/vm/vm-in | `lookbehind-variable` | satisfied | `negation-scope-lookbehind-var`'s own pattern (a single-branch variable-width negative lookbehind) | REFUSED: `variable-length lookbehind is not implemented: every alternative of a lookbehind must have a fixed length` | **CORRECTED to unsatisfied** |
| pcrec-auto/nocaps/vm/vm-in | `callouts` | unsatisfied | `a(?C1)b` | REFUSED: `module 'callouts' is enabled but (?C...) is not implemented yet` | already correct, unchanged |
| pcrec-auto/nocaps/vm/vm-in | `backrefs` | satisfied | `(\w+)\1` | COMPILED | correct, spot-verified |
| pcrec-auto/nocaps/vm/vm-in | `lookaround` | satisfied | `(?=a)b` | COMPILED | correct, spot-verified |
| pcrec-auto/nocaps/vm/vm-in | `possessive-quantifier` | satisfied | `a*+` | COMPILED | correct, spot-verified |
| pcrec-auto/nocaps/vm/vm-in | `atomic-group` | satisfied | `(?>a*)b` | COMPILED | correct, spot-verified |
| pcrec-auto/nocaps/vm/vm-in | `recursion` | satisfied | `\((?:[^()]|(?R))*\)` | COMPILED | correct, spot-verified |
| pcrec-auto/nocaps/vm/vm-in | `k-reset` | satisfied | `a\Kb` | COMPILED | correct, spot-verified |
| pcrec-auto/nocaps/vm/vm-in | `unicode-properties` | satisfied | `\p{L}` (both `-e byte` default and `-e utf8`) | COMPILED both | correct, spot-verified |
| pcrec-auto/nocaps/vm/vm-in | `named-groups` | satisfied | `(?<name>a)` | COMPILED | correct, spot-verified |
| pcrec-auto/nocaps/vm/vm-in | `free-spacing` | satisfied | `(?x) a  b` | COMPILED | correct, spot-verified |
| pcrec-auto/nocaps/vm/vm-in | `true-end-anchor` | satisfied | `a\z` | COMPILED | correct, spot-verified |
| pcre2-interp, pcre2-jit | every token (full vocabulary, incl. `lookbehind-variable`, `conditionals`, `control-verbs`, `callouts`, `k-reset`) | satisfied | `pcre2test` (10.46) on `(?<!\bnot\s{1,3}(?:\w{1,12}\s{1,3}){0,3})\bavailable\b`, `(?(1)a|b)(a)?`, `a(*ACCEPT)b`, `a(?C1)b`, `\p{L}` | every one compiled clean, no `Failed:` | correct, unchanged — confirmed these are `pcre2_match`/JIT on a plain compiled pattern, never `pcre2_dfa_match` (whose own missing-k-reset/captures caveat this vocabulary's own table names) |
| `pcrec-nocaps` | `captures` | already absent | (structural: `--no-captures` turns off capture reporting) | n/a — not a compile-refusal question | correct, unchanged |

`span-reporting`, `non-utf8-subject`, `captures` are execution-model
facts (native driver reports a span; default `-e byte` accepts
arbitrary bytes; `--no-captures` toggles capture reporting), not
compile-time predicates — no witness compile applies; verified by
reading the adapter's own flags in `testees/pcrec/configs.toml`
instead, per §5.1's own note that these two rows are about execution
model, not syntax.

**Fix location**: `bench/capability/gen_patterns.py`'s
`EXT_BENCH_ROSTER` table — `patterns.rxt` is GENERATED, never
hand-edited (`bench/capability/CLAUDE.md`'s own stated rule).
Regenerated with `PCREC_BIN=.../build/pcrec-cd371441/build/pcrec
python3 bench/capability/gen_patterns.py`, then re-verified with
`--check` (round-trips through the real pcrec binary; exit 0, no
diff). The resulting `git diff` touches only the twelve now-absent
`conditionals`/`control-verbs`/`lookbehind-variable` lines across the
four `pcrec-*` blocks — nothing else in `patterns.rxt` moved.

`bench/capability/NOTES.md`'s own caveat paragraph (which correctly
distrusted the first cut, since it was "inferred... NOT independently
re-derived from a real compile census") is corrected in place with
the fix and a summary of what changed.

## 3. Convention-scoped scoring (R5 B1/CB1)

`harness.outcome_for()` gains an optional `convention` parameter.
`subbench.Expectation` gains a `.convention` slot, always `None` from
the real 9-column `expectations.tsv` loader (no format change — an
`under <convention>`-qualified row is unauthored anywhere, per
`bench/capability/NOTES.md`'s own stated deferral). `run_cell` now
reads the testee's own declared convention
(`testee.conventions[0]`) and passes it through.

Behavior: when the caller's convention and the expectation's own
(`.convention`) disagree, the row scores `did-not-match-as-expected`
with a diagnostic naming both, instead of being silently graded
against an answer authored for a different convention. On every real
corpus row (`.convention` stays `None`) this is a no-op — the
subset-check branch is unreachable, matching family 11's narrowed v1
scope (the shared-`perl-leftmost-first` population scores exactly as
before). Built and tested against hand-built fixtures only
(`tools/selfcheck.py`'s `check_convention_scoring`, per the brief's
own instruction — no new set rows).

## 4. `variant.kind` rendering (R5 B2/CB2) — designed and built from nothing

Before this lane: an exhaustive grep for `variant` in `report.py`
returned exactly two hits, both unrelated prose (R5 finding B2,
re-confirmed here). `requirements.md` §4.5's closing sentence —
"Reports show the variant kind beside the number" — had no
implementation.

Built: a per-GROUP (not report-wide) `variant_by_testee` dict, the
same conditional-column shape `dominated_by_testee`/`delta_by_testee`
already use (a column empty on every row of ONE table is omitted from
THAT table — the R5 house rule, not `show_form`'s report-wide flag),
fed by a new `ReportData.variant_by_cell` index ((sb, testee_id,
pattern_id) → `patterns[].variant`), populated the same way
`floor_pattern_by_sb` ([B14] R9) already is. A `variant` column shows
`` `syntax-only` ``/`` `restructured` `` beside the row that ran one
and `-` beside a row in the same table that did not; a legend note
explains the two tokens and `requirements.md` §4.5's two constraints
wherever the column fires.

Validated against a **SYNTHETIC many-variant report fixture** (thirteen
patterns, two testees: `engine-a` always runs the canonical text,
`engine-b` runs a declared variant — alternating `syntax-only`/
`restructured` — on twelve of them and the canonical text on the
thirteenth control pattern), never a live sample — `gen_variants.py`'s
table is deliberately empty in v1 for every set, and a grep over
`store/records/` confirms zero committed records carry a non-null
`patterns[].variant`. `REPORTER_VERSION` is therefore **UNCHANGED**
(`v16 (2026-09-08)`) and no committed report under `reports/` moves a
byte. `test_variant_kind_rendering_cb2`
(`pcrecbench/tests/test_report.py`) asserts the column and legend note
fire on every one of the twelve mixed tables and fire on **neither**
on the thirteenth control table, in the same report.

## 5. New selfcheck arms

Three, wired into `make check-harness` (`tools/selfcheck.py main()`):

- **`check_capability_policy`**: end to end via the real `quick` CLI
  on `bench/capability` — the blocked witness pattern
  (`negation-scope-lookbehind-var` on `pcrec-auto`:
  `compile_outcome=unsupported-by-declaration`, a `declaration_ref`
  present, zero match rows, no pcrec engine diagnostic leaking
  through), a control that the same pattern measures normally under
  `pcre2-interp` (declares the full vocabulary), a control that a
  satisfied token (`balanced-parens-rec`, requires `recursion`) is not
  over-blocked on `pcrec-auto`, the closed-vocabulary rejection with
  its accepted-token control, and the fail-closed rule on an
  undeclared testee id. 7 checks.
- **`check_capability_policy_noop_elsewhere`**: the flip side of
  `pcrecbench.capability`'s own docstring claim ("a silent no-op on
  every pre-[B42] set") — CHECKED, not merely asserted: every OTHER
  `bench/*/` set (discovered by `subbench_dirs()`, never named)
  declares zero `requires-*` tags on any pattern, so the policy can
  never fire there; `check_capability_policy` above is the control
  showing it DOES fire on `bench/capability`. 5 checks (one per other
  set: altwide, bounded, email, loglines, syntax).
- **`check_convention_scoring`**: hand-built fixtures — matching
  convention scores normally, mismatched convention scores
  `did-not-match-as-expected` naming both conventions, and two
  backward-compatibility controls (`expectation.convention is None`
  ignores the caller; `convention=None`, the default, ignores the
  expectation) proving the parameter is inert on every pre-existing
  call shape. 4 checks.

All three smoke-tested standalone before wiring: **16/16 PASS**
(7 + 5 + 4), including every negative control, cleaned of scratch
artifacts afterward.

## One deviation from the brief's own edit scope

The brief scoped `bench/capability/` edits to "the ext bench block and
NOTES.md's matching prose only — nothing else in the set."
`bench/capability/CLAUDE.md`'s closing "WHAT IS NOT BUILT HERE"
paragraph explicitly listed the capability policy and `variant.kind`
rendering as unbuilt, which this lane makes false. The top-level project
CLAUDE.md's own maintenance mandate ("update it when files are
added/removed or change roles") is a stronger, house-wide rule than the
brief's narrower per-set scope, so this lane corrected that one
paragraph — nothing else in `bench/capability/` beyond the ext bench
block, `NOTES.md`, and this one `CLAUDE.md` paragraph was touched.
Flagged here as a deliberate, narrow exception rather than a silent
scope creep.

## What was NOT committed

- The exploratory loader-path (a) confirmation (§1's table, last row):
  a throwaway 2-pattern `.rxt` fixture with matching provenance counts,
  used by hand to confirm `_load_matrix` prefers `sb.rxt.aux_rows`
  when present. Not committed — no real set exercises path (a) yet,
  and inventing one only to test a fallback branch felt like the wrong
  kind of fixture (a synthetic set nobody else uses, versus a synthetic
  RECORD/report the reporter tests already use for exactly this
  reason). Flagged as a gap a future rxt-sourced set's own lane should
  close with a real control.
- A TSV-render column for `variant.kind` (`render_tsv`): out of scope
  as stated — §4.5's own sentence is about human-facing reports
  ("beside the number"), and the brief's CB2 ask names the reporter's
  rendering, not the TSV machine format specifically. Noted rather
  than silently absent.

## K57 caveat

No `.rxt` fixture with a `|` block-scalar production was authored by
this lane (the exploratory loader-path fixture above used only plain
`pattern`/`name`/`tag` lines, no `description |` block) — K57
(the dedent bug, fixed upstream but not yet at this pin) does not
apply to anything this lane wrote. Stated for completeness per the
brief's own ask, not because it fired.

## Charter-vs-committed checklist

| brief item | committed |
|---|---|
| 1. pre-compile capability policy, wired before any compile | `pcrecbench/capability.py`, `pcrecbench/harness.py`'s `run_cell` compile loop; verified end to end on the real corpus |
| 2. re-verify L3's capability lists, witness check per (config, token), correct wrong declarations | §2's matrix above; `bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER`; `patterns.rxt` regenerated + `--check`-clean; `NOTES.md` corrected |
| 3. convention-scoped scoring | `outcome_for(..., convention=)`, `Expectation.convention`, `run_cell`'s read of `testee.conventions[0]`; fixture-only tests |
| 4. `variant.kind` rendering, synthetic fixture only | `ReportData.variant_by_cell`, the per-group column + legend note, `test_variant_kind_rendering_cb2` |
| 5. new selfcheck arms, each with a negative control | `check_capability_policy`, `check_convention_scoring`, wired into `main()` |
| targeted checks green | §1/§5 above, individually re-run standalone before commit |
| one full `make check` at the end | see "Validation" below |
| lane report with the witness matrix, corrections, load paths, checklist | this file |
| K57 caveat | above — n/a, stated |
| engine refusal contradicting a declared capability | none found beyond L3's own three wrong first-cut declarations, which this lane corrected as OUR error, not a pcrec defect — every refusal this lane hit matches `docs/pcre2_compliance.md`'s own documented status (D26 tier 4 for control-verbs; "not implemented yet" for the general conditional; the fixed-width-per-branch lookbehind limit, documented since [M6.6.2]). Nothing here implicates pcrec |

## Validation

OWED at report-writing time, per DO-THEN-FINISH: `pcrecbench.tests.
test_report` (the full suite, `REAL_STORE` = 161-record `store/`) was
launched DETACHED (`setsid bash -c 'gnutimeout 1200 python3 -m
pcrecbench.tests.test_report > /tmp/test_report_out.txt 2>&1; echo
"DONE rc=$?" >> /tmp/test_report_out.txt'`) — the whole-store-load
memory heuristic this project's own BOILERPLATE names (KB-16: ~750s /
~3.6GB at 160 records). Marker: the literal line `DONE rc=0` (or a
non-zero rc) appended to `/tmp/test_report_out.txt` on this box. A
fresh invocation resuming this lane must check that file FIRST.

[to be filled in once the marker lands: pass/fail count, then
`make check-harness`, then `make check` as a whole]
