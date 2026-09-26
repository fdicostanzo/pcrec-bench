# b77u5 — [B77] U5: bench/utf8's expectations and NOTES.md

Lane `b77u5`, branch `lane/b77u5` off master 438ba8d, 2026-09-25/26.
Charter: `docs/design/utf8_set_v1.md` §13's U5 row (+ §12 R0-R8, §11
P1-P10, §6 growth). Worktree: `.claude/worktrees/agent-a43fc0412f9d70a2e`.
Scope held: nothing under `reports/`, `store/`, `docs/dev/ledgers/` or the
null-band code was touched. ~/pcrec was read only (`tests/uprops/
uprops_compare.py`).

## 0. The headline: the blocker was not what it looked like

The brief framed the cost as "one ctypes call per match". **Measured: the
ctypes call overhead is only ~1-3% of the cost.** The rest is libpcre2's
own UTF check. Without `PCRE2_NO_UTF_CHECK`, `pcre2_match` re-validates the
subject from the start offset to the END of the subject on every call
(pcre2api). A find-all loop is therefore QUADRATIC in subject length.

- In C, against the same library and option word, `.` over `t-256k` took
  **36.1 s** with the check on every call and **0.018 s** with the check on
  call 1 only, with the same count (185,769).
- The per-pattern model totals ~3,553 s (~59 min) for the set under the
  original §8.2; `t-1m` is ~90% of that.

So lever (a), a C helper under §8.2's letter, is sound as an oracle but
fixes nothing, and it was not built. Lever (b), a set-level cap, would have
cost the size sweep and R7.

I asked the manager for a ruling. **The ruling was VALIDATE-ONCE, YES**
(manager, 2026-09-25; to be recorded as a BD entry at merge and flagged to
Frank, who may overturn it). Its terms:

- §8.2 is amended in place.
- The flag goes only on calls 2..n of one find-all loop, after call 1
  (offset 0, no flag) has let libpcre2 validate the whole subject.
- Each flagged start offset is ASSERTED to be a character boundary.
- The three controls go in `make check`.
- The fix is made in the existing Python oracle, with no C helper, and
  t-1m stays in the set.

The full 76-pattern derivation now takes **~34 s**.

## 1. Charter-vs-committed checklist

| # | promise (brief / §13 U5 / the ruling) | status | where |
|---|---|---|---|
| 1 | solve the derivation-cost blocker; prefer (a) if sound, else say why | **DONE**: (a) is sound but ineffective (the cost is libpcre2's own validation, which a C helper inherits); VALIDATE-ONCE ruled YES instead; (b) dropped per the ruling | `pcrecbench/oracle_pcre2.py` `_find_all_impl`; probe below |
| 2 | ruling cond. 1: amend §8.2 IN PLACE, the old sentence visible as superseded, reason + archived probe with a source header | **DONE** | `docs/design/utf8_set_v1.md` §8.2; `docs/dev/measurements/2026-09-25-b77u5-validate-once-probe.txt` + `probe_b77u5_validate_once.c` + `probe_b77u5_cost_model.py` |
| 3 | cond. 2: a UTF error on call 1 is the recorded answer with no further call; boundaries ASSERTED | **DONE**: call 1 raises `Pcre2Error` (the existing give-up surface); an `AssertionError` fires before any flagged mid-character call | `_find_all_impl` |
| 4 | cond. 3 (i): validate-once rows byte-identical to always-check on the utf8 short + 64k subjects | **DONE**: 75 patterns × 96 subjects = 7,200 find-all cells identical, ~66 s | `tools/selfcheck.py check_utf8_validate_once` |
| 5 | cond. 3 (ii): an ill-formed subject is refused by name; a negative arm | **DONE**: `-23: UTF-8 error: illegal byte`. NEGATIVE 1: the same loop with the flag on call 1 too silently counts. NEGATIVE 2: a byte-stepping advance hits the boundary assertion by name | same |
| 6 | cond. 3 (iii): byte-mode sets provably untouched | **DONE**: a spy on the oracle's one `pcre2_match` site shows a byte word passes option 0 on every call (and the UTF control shows the flag exactly on calls 2..n). All six byte sets' `check_expectations` re-derive unchanged | same + `check_expectations` |
| 7 | cond. 4: in the Python oracle, no C helper, t-1m kept | **DONE** | — |
| 8 | guard `derive()` against a compile-time `Pcre2Error`; `prp-ingreek` gets the first-class outcome, not a crash | **DONE**, and tighter than a bare try/except. `derive(expected_refusals=, refusals=)` / `main(expected_refusals=)`: a DECLARED refusal gets no rows and is listed on stderr. An UNDECLARED refusal, or a declared pattern that compiles, raises `OracleRefusalError` by name. Default arguments leave every other set unchanged | `pcrecbench/expectations.py`; `bench/utf8/gen_expectations.py` `EXPECTED_ORACLE_REFUSALS` |
| 9 | the real `expectations.tsv`, oracle-derived, method recorded | **DONE**: 7,350 rows (75 × 98), 33.7 s. The floor's 98 rows are byte-identical to U4's stub. `cls-dot`'s counts equal the C probe's | `bench/utf8/expectations.tsv`, `gen_expectations.py` docstring, NOTES.md "The oracle" |
| 10 | `check_expectations` re-derives bench/utf8 within make check's budget; measure it | **DONE**: utf8 adds **33.4 s**. The full seven-set `check_expectations` took 358 s (altwide 136 s, syntax 170 s, capability 13 s, bounded/loglines/email ≤3 s each), plus 66 s for the new control | measured this lane |
| 11 | NOTES.md with R0-R8 and P1-P10 stated BEFORE any run | **DONE** (`store/index.tsv` has no `utf8` row). Also carries the objective, the §4.1 limitation, the oracle method, the growth plan, neutrality and cell time | `bench/utf8/NOTES.md` |
| 12 | the P1-P10 dry-run through interpret's loader against a synthetic/no-op input | **DONE**, stronger than asked; see §2 below | `docs/dev/predictions/utf8-0.1-first.tsv`; `docs/dev/measurements/probe_b77u5_predictions_dryrun.py` + `2026-09-25-b77u5-predictions-dryrun.txt` |
| 13 | CLAUDE.md files current | **DONE**: `bench/utf8/`, `pcrecbench/`, `docs/dev/predictions/`, `docs/dev/measurements/`, `docs/design/`, root | — |
| 14 | the design note's §13 U5 row brought to reality | **DONE** | `utf8_set_v1.md` §13 |
| 15 | validation: make check-schema, gen.py --check, make check-interpret, targeted harness gates for utf8 + check_expectations over every set | **DONE**, all green (§3) | — |
| 16 | full `make check` | **OWED to the manager** (the 2026-09-25 long-run rule); command in §4 | — |

## 2. The predictions dry run and what it found

`docs/dev/predictions/utf8-0.1-first.tsv` has **15 clauses over 10
parents** (P1-P7, P9-P11; P8 is deferred to 0.2 by the design). The real
`pcrecbench interpret --predictions` CLI was run on three inputs:

- (A) The CLEAN null fixture: every clause loads and reads not-evaluable.
- (B) A synthetic report valued to confirm: 10/10 confirmed. This exercises
  `ratio_to`'s nested selector and join, `ratio_max_min_over`, `count` over
  `did_not_compile`, and `grain=subject`.
- (C) The same report valued to violate: 9/10 refuted, and P7 reads
  partial. P7.a has no refusal row there, which is its stated residual.

The transcription changed five things (NOTES.md "What the transcription
changed"). Two of them are findings for the manager:

1. **`unsupported-by-declaration` cannot be expressed in the report TSV.**
   `render_tsv` has no unsupported section; only `--format matrix` carries
   `unsup`, and `interpret` does not read the matrix. The
   `unsupported_by_pattern` SECTION that §11 proposes (F-M2) does not
   exist. So P5.a (pcrec declares the five UCP patterns unsupported) and
   P9.b (rust declares the ascii-class-scope ones unsupported) are prose,
   not rows. They are also R8's whole population. If Frank wants them
   scored, that needs a reporter change: an `unsupported` TSV section, or
   `interpret` reading the matrix.
2. **P9/P10 as designed were already refuted on `prp-greek`.** U2's census
   measured that rust, re2, onig and vectorscan read bare `\p{Greek}` as
   Script. The oracle (Script_Extensions) matches the U+0301 in
   `lit-nfc-decomposed-miss` at [4,6); `\p{sc=Greek}` does not. So P9/P10
   exclude `prp-greek` (by an enumerated list), and **P11** predicts the
   divergence itself, with a pcre2/pcrec control. §7.4 charges U5 with
   exactly this.
   - Related oracle finding: the typed witness `prp-greek-scx-witness`
     (α + U+0342) does NOT separate the pair at search grain, because both
     spellings hit the α at [0,2) first. The separation happens only on
     `lit-nfc-decomposed-miss`.
   - U+0301 is not among `uprops_compare.py`'s 16 `SCX_REVISED` points, so
     that answer is stable from Unicode 16.0.0 to 17.0.0.
   - U+00B7 appears in no subject (checked).

The other three changes are narrowings:

- P1's "lat subjects" is not a set-grain population, and "differ" is
  scored direction-neutrally.
- P7's raised-cap half has no testee, since no `pcrec-*-bigcap-utf8`
  config exists.
- P5.b leaves `pcre2-utf-dfa` out for convention reasons.

## 3. Validation (this lane, all on lane/b77u5)

- `make check-schema`: 6 accepted, 74 sabotages rejected for their rule,
  0 wrong.
- `python3 catalogue/fixtures/gen.py --check`: 243 files in 75 fixtures,
  ok.
- `make check-interpret`: **199 passed, 0 failed**.
- Targeted harness gates (`tools/selfcheck.py` functions called directly):
  `check_manifests`, `check_id_preflight`, `check_pattern_text_cap`,
  `check_utf8_find_all_advance`, **`check_utf8_validate_once` (new, 5
  checks)**, `check_capability_policy`,
  `check_capability_policy_noop_elsewhere`, `check_floor_pattern` (utf8's
  floor answered by pcre2 and pcrec), and `check_expectations` (all seven
  sets re-derive, plus the sabotage control): **117 passed, 0 FAILED**.
  The box was shared with the concurrent b90ledger render
  (loadavg 0.8-3.1); none of these checks is a timing.

## 4. OWED: the full `make check` (the manager launches it)

- Working directory: the lane worktree
  `/home/duxevents/pcrec-bench/.claude/worktrees/agent-a43fc0412f9d70a2e`,
  or master after merge.
- Command:
  `setsid gnutimeout 3600 make check > /var/tmp/b77u5-makecheck.log 2>&1; echo "DONE rc=$?" >> /var/tmp/b77u5-makecheck.log`
- Completion line: `DONE rc=<n>` in `/var/tmp/b77u5-makecheck.log`.
- Expected: check-harness grows by the 5 new `check_utf8_validate_once`
  checks, plus about 66 s + 33 s of wall time. check-interpret 199/199.
  Numbers are OWED.

## 5. Items for the manager

- **A BD entry for the VALIDATE-ONCE ruling**, per the ruling's own
  "recorded as a BD entry at merge". Not written here because
  `decisions.md` is the manager's.
- The unsupported-section gap in item 2.1 above, if P5.a/P9.b/R8 should be
  machine-scored.
- `gen_subjects.py`'s `prp-greek-scx-witness` description still says "the
  oracle (U5) settles whether they diverge on the combining mark alone".
  It is now settled: they do not diverge on that subject at search grain.
  Changing the description would move `manifest.tsv`, so it was left alone
  and the settlement is recorded in NOTES.md.
- Cosmetic: `check_floor_pattern`'s utf8 line has a double space
  ("oracle  cls-boundary-range"), because the set has no leading hit
  subject. Harmless.

## Commits

- a68eeca: validate-once, declared refusals, the real expectations.
- f6b35d6: check_utf8_validate_once, §8.2 amended, probe archived.
- 2275d86: predictions and the dry run.
- 8bac867: NOTES.md, the CLAUDE.md files, §13.
- 35d6532 + this fix-up: root CLAUDE.md and this report.
