# bench/utf8@0.1 — the UTF-8 encoding set: objective, oracle, outlier rule, predictions

Written 2026-09-25/26 by lane `b77u5` ([B77] U5), **before any `utf8@0.1`
cell has run** (`store/index.tsv` holds no `utf8` row at this commit). The
design of record is `docs/design/utf8_set_v1.md` v0.2; this file carries
the parts §6, §11 and §12 say must live HERE, transcribed against the
BUILT pattern and subject ids, plus what the build found. What each file in
this directory is: `CLAUDE.md`.

## Objective, and what would defeat it

Frank's charter (inbox I-90): *"any functionality which might be affected
by encoding — classes come to mind"*. The set measures, for SPEED, the
encoding-dependence axes pcrec's own `tests/utf8/axis01-12` test for
CORRECTNESS, across the twelve UTF-8-capable roster configs, over five
generated script corpora whose lead-byte histogram is a committed,
re-derived fact (`subject_facts.tsv`). Six families, 75 members + the floor
(`cls` 16, `lit` 12, `ci` 12, `alt-qnt` 12, `asr` 11, `prp` 12).

What would defeat it: a difference between two engines that is really a
difference in HOW THEY WERE TOLD the encoding (a harness artefact), or a
difference that is really the SUBJECT's prose statistics rather than its
bytes. The first is what [B77] U1's shared oracle word and
character-boundary find-all advance exist to prevent; the second is the
limitation below.

**The limitation, stated plainly (utf8_set_v1.md 4.1):** these are our
sentences made of real words. The set claims a realistic BYTE HISTOGRAM
and realistic character-width statistics — which is what every mechanism
under test actually reads (a required byte, a lead-byte scan, an offset-k
skip, a fold set) — and does NOT claim realistic prose statistics at the
word or sentence grain. A finding that depends on word-frequency structure
rather than byte structure is not this set's to make.

## Regimes

`search_short` (91 typed short subjects, all ≤ 512 B) + `throughput`
(seven texts: the `t-64k`/`t-256k`/`t-1m` mixed sweep and the per-script
64 KB arm `t-64k-lat`/`-cyr`/`-cjk`/`-asc`). No `match` regime
(utf8_set_v1.md 10.1): the patterns that need a whole-subject reading carry
their own anchors (`cls-dot-rep`, `lit-anchored-run`, `asr-a-z`,
`prp-l-anchored`).

## The oracle

**Method:** `libpcre2-differential`, libpcre2 10.46 (Unicode 16.0.0)
through `pcrecbench/oracle_pcre2.py`, `bench/utf8/gen_expectations.py` →
the shared `pcrecbench.expectations.derive`. **7,350 expectations** = 75
compiling patterns × (91 `search_short` + 7 `throughput`): 1,475 / 5,350
match / nomatch on `search_short`, 247 / 278 on `throughput`. No capturing
group participated in any match (checked by `derive` on every run), so the
span is the whole observable answer.

- **The option word** (utf8_set_v1.md 8.1, [B77] U1): `PCRE2_UTF` on every
  pattern (the sidecar's `[expectations] encoding = "utf8"`); `PCRE2_UCP`
  on exactly the five patterns declaring `requires-unicode-class-scope`
  (`cls-w-ucp`, `cls-d-ucp`, `cls-s-ucp`, `asr-b-cyr-ucp`,
  `ci-ucp-invariance`). Multiline is spelled inline. The throughput
  find-all advances to the next CHARACTER boundary after an empty match.
- **VALIDATE-ONCE** (utf8_set_v1.md 8.2 as AMENDED by the manager's ruling,
  2026-09-25; to be recorded as a BD entry, flagged to Frank):
  `PCRE2_NO_UTF_CHECK` is passed only on calls 2..n of one find-all loop
  over the same subject buffer, after call 1 (offset 0, no flag) let
  libpcre2 validate the whole subject; each flagged start offset is
  asserted a character boundary. Without it libpcre2 re-checks the
  subject from the start offset to the END on every call and the
  derivation is quadratic: ~59 min modelled for the set, 36.1 s vs 0.018 s
  measured for `.` over `t-256k` alone
  (`docs/dev/measurements/2026-09-25-b77u5-validate-once-probe.txt`). With
  it the full derivation is **~34 s**. The controls live in `make
  check-harness` (`check_utf8_validate_once`: the rows are byte-identical
  to the always-check path over every short and ≤64 KB subject, 7,200
  find-all cells, ~67 s; an ill-formed subject is refused BY NAME; byte
  sets pass no match option).
- **One DECLARED oracle refusal: `prp-ingreek`** (`\p{InGreek}` —
  libpcre2: "unknown property after \P or \p"). It carries NO expectation
  rows by design (utf8_set_v1.md 5(f); `bench/bounded`'s 65535 rung is the
  precedent). `gen_expectations.py` declares it
  (`EXPECTED_ORACLE_REFUSALS`); an UNDECLARED refusal, or this pattern
  compiling, fails the derivation by name (`OracleRefusalError`).

### What the oracle settled that the build had left open

- **The `prp-greek` / `prp-greek-sc` pair (Script vs Script_Extensions).**
  The typed witness `prp-greek-scx-witness` (α + U+0342) does NOT separate
  the pair at search grain: both spellings match the α at [0,2) before the
  combining mark is reached. The pair IS separated on
  `lit-nfc-decomposed-miss` (`cafe` + U+0301): `\p{Greek}` matches the
  U+0301 at [4,6) (its Script_Extensions include Greek), `\p{sc=Greek}`
  does not. U+0301 is NOT among the sixteen code points whose
  Script_Extensions moved between Unicode 16.0.0 and 17.0.0
  (`~/pcrec/tests/uprops/uprops_compare.py`'s `SCX_REVISED`), so the
  separating answer is stable across that boundary. No subject separates
  the pair at `throughput` (both `nomatch` everywhere). This is what P11
  below reads.
- **The known version-sensitive region, U+00B7 (MIDDLE DOT)**
  (utf8_set_v1.md 8.5/R6): its Script_Extensions set changed between
  Unicode 14.0.0 and 16.0.0. It is AVOIDED — checked: no subject in
  `subjects/` or `throughput/` contains the byte pair `C2 B7`. A
  re-derivation against a libpcre2 on a different Unicode version could
  still legitimately differ on any `SCX_REVISED` member; none of those
  appears in a separating position either.

## The outlier rule (R0-R8), stated before any run

A CELL is (pattern × regime × testee); a cell is listed under the FIRST
rule it trips. (utf8_set_v1.md 12, in `bench/syntax`'s and
`bench/capability`'s own shape.)

- **R0 — a wrong answer is read first**, before any speed comparison, on
  every cell (correctness before speed, APPROACH principle 1). P4, P6, P9,
  P10 and P11.b each predict `n_wrong eq 0` over a named population and
  P11.a predicts a named wrong answer; any other wrong answer is a
  question.
- **R1 — a refusal on a pattern whose REQUIRES the config claims to
  satisfy is a finding, not a footnote.** Every `requires=` tag is a
  machine-checkable claim against `patterns.rxt`'s `ext bench` roster.
  `prp-ingreek` is the one expected refusal on every engine; P7 names the
  expected size-cap ones.
- **R2 — the `pcre2-jit` band** (Frank's own, I-42 (3)): a cell against
  `pcre2-utf-jit`'s same cell, worse than ×2 or better than ×20, in either
  direction.
- **R3 — the ENCODING band, this set's own rule.** A pure-ASCII pattern
  (the floor, `ci-ascii-control`, `asr-b-ascii`) whose `throughput`
  ns/byte on one per-script 64 KB subject differs from the same cell on
  `t-64k-asc` by more than **×3**: the subject's byte structure reaching a
  mechanism that should not have noticed. Throughput grain only (F-M5): the
  short subjects are typed per family in one script, so there is no
  other-script `search_short` population to compare against.
- **R4 — the script band.** Within one family, a cell's ns/byte across the
  four per-script 64 KB subjects spread by more than **×4** — chosen
  against the encoded-length ratio the corpora carry (1 byte/char `asc`
  to ~3 `cjk`), so anything beyond it is not width.
- **R5 — compile and size cliffs** (compiled testees only): a pattern's
  compile time or `emit_bytes` beyond **×10** the testee's own median over
  the set. Family (f) is the predicted population (P7); an (a) or (c)
  member tripping it is the question.
- **R6 — engine-selection surprises**, read off the record's mechanism
  stamps: a declined prefilter on a pattern with a strong lead-byte set; a
  `memchr` arm chosen where the class has two lead bytes (`cls-lead-pair`
  — UD §6.3 says the bitmap arm must take it); an engine route that
  differs between a pattern and its control twin. The offset-skip rows
  beyond P1's pair (`lit-run-3`, `lit-mixed-ascii`, `alt-shared-char`) are
  read here (F-C6's declared narrowing).
- **R7 — a non-flat sweep.** `t-1m` ns/byte against `t-64k` ns/byte
  outside **[0.7, 1.4]** on one pattern and testee, read on EVERY pattern
  (`bench/capability`'s lesson: an unanchored negated class can go
  quadratic against a background lacking its terminator).
- **R8 — an `unsupported-by-declaration` share is a CENSUS finding, not
  missing data.** This set's share will be the largest in the repo
  (utf8_set_v1.md 7.4); read as a count per (engine, family), never as an
  absence. Read it off the `.matrix.tsv` sibling: the report TSV carries no
  unsupported section (see P5 below). **[B91] addendum (2026-09-26, after
  this rule was stated, before the first sample was READ):** reporter v24's
  report TSV now carries it -- the `unsupported_by_pattern` section, one row
  per (pattern, form, testee), readable by `interpret` (catalogue 3.9); the
  rule's meaning is unchanged.

**Ranking** (I-42, Frank: "algorithmically and generally first, SIMD at
the end"): R0, then R1, then any R2-R7 cell whose likely fix is a GENERAL
mechanism (a filter declined, a route chosen wrongly, a fold set lowered
expensively), then the rest, then anything whose fix would be a SIMD one.

## Predictions (P1-P11), 2026-09-26, before any run

The prose below is utf8_set_v1.md 11's P1-P10 on the built ids, plus P11
(the answer divergence utf8_set_v1.md 7.4 charges U5 to predict). The
machine-readable transcription is
`docs/dev/predictions/utf8-0.1-first.tsv` (15 clause rows over 10
parents, `stated_utc` 2026-09-26T00:30:00Z), DRY-RUN through `pcrecbench
interpret`'s own loader and evaluator before any window
(`docs/dev/measurements/2026-09-25-b77u5-predictions-dryrun.txt`: every
clause LOADS; against a synthetic input valued to confirm, 10/10 parents
confirm; valued to violate, 9/10 refute and P7 reads partial — its stated
residual). Testee globs: `pcrec_*_utf8` = the four `pcrec-*-utf8` configs;
`libpcre2_*_interp-caps-simdna_utf8` = `pcre2-utf-interp`.

- **P1 — the offset-skip ORDER PAIR** (I-90 §5's first customer).
  `lit-offset-at-head` (`@é`) and `lit-offset-at-tail` (`é@`) differ in
  `search_short` `median_ns` by more than ×1.5, either direction, on every
  `pcrec-*-utf8` config (clause P1.a, `ratio_max_min_over(pattern)`).
  **P1.b, prose only:** the two artifacts stamp DIFFERENT `RX_REQ_BYTE`
  values (FP §3.1: 0x40 for one ordering, 0xA9 — é's continuation byte —
  for the other), the mechanism behind P1.a.
- **P2 — the high necessary byte** (the second customer). `lit-run-3`
  (日本語) costs at least ×2 `lit-mixed-ascii` in `throughput` `median_ns`
  on the SAME `t-64k-cjk` subject, on `pcre2-utf-interp` and every
  `pcrec-*-utf8` (subject grain). FP §3.2's inversion as a cell.
- **P3 — its control.** On `t-64k-asc` the same ratio is within ×1.5 either
  way (both patterns find nothing there).
- **P4 — the fold sets** (the third customer). `ci-moskva`'s
  `compile:emit_bytes` exceeds `ci-ascii-control`'s by more than ×1.5 on
  every `pcrec-*-utf8` config (P4.a); no `ci-*` `search_short` cell is
  wrong on any roster testee (P4.b), in particular `ci-strasse` does NOT
  match `STRASSE` (P4.c) and `ci-turkish-i` does NOT match U+0130/U+0131
  (P4.d) — axis 7's simple folding as a cross-engine expectation.
- **P5 — the UCP census.** The five `unicode-class-scope` patterns are
  `unsupported-by-declaration` on all four `pcrec-*-utf8` configs (pcrec
  has no UCP axis, UD §4.5) — **P5.a, prose only** — and compile and
  answer on `pcre2-utf-interp`/`-jit` (P5.b, `n_wrong eq 0`).
- **P6 — encoded length.** `cls-dot-rep` (`^.{5}$`) answers correctly on
  every testee that compiles it (`cls-dot-rep-hit` 5 chars / 12 bytes,
  `cls-dot-rep-miss` 5 bytes / 3 chars).
- **P7 — the property size cliff.** At least one family-(f) pattern
  (`prp-ingreek` aside) is `did-not-compile` on a default-cap
  `pcrec-*-utf8` config (P7.a); `prp-l`'s `compile:emit_bytes` exceeds the
  family-(b) literal median by more than ×10 on every compiled
  `pcrec-*-utf8` config (P7.b). **The design's "compiles on the raised-cap
  sibling" half is prose only** — the roster has no `pcrec-*-bigcap-utf8`.
- **P8 — the floor is free** (`~` over `asc`, `pcrec-auto-utf8` vs
  `pcrec-auto` byte). **Scored at 0.2**, when (k)'s mirror arm exists; no
  row, by the design's own deferral. Stated now because it is the mirror's
  zero point.
- **P9 — rust is correct, not lucky.** `rust-default` reads `n_wrong eq 0`
  on every pattern it compiles EXCEPT `prp-greek` (P9.a); the
  `ascii-class-scope` patterns appear as `unsupported-by-declaration`, not
  as wrong answers (**P9.b, prose only**). A refuted P9 is a finding about
  this repo's byte-mode sets too.
- **P10 — vectorscan agrees at the grain it has.**
  `vectorscan-block-nosom-utf8` agrees with the oracle on every pattern it
  compiles EXCEPT `prp-greek` (P10.a); the population is expected SMALL,
  and that smallness is itself the census reading.
- **P11 — the Script vs Script_Extensions answer divergence.** On every
  engine that reads bare `\p{Greek}` as Script (`rust-default`,
  `re2-utf8`, `onig-utf8`, `vectorscan-block-nosom-utf8` — U2's measured
  finding), `prp-greek` is WRONG on at least one short subject (P11.a:
  the oracle, reading Script_Extensions, matches U+0301 in
  `lit-nfc-decomposed-miss`); on the engines that read it as
  Script_Extensions (`pcre2-utf-interp`/`-jit`, every `pcrec-*-utf8`) both
  spellings answer as the oracle (P11.b).

### What the transcription changed (the F-M2 step, before the window)

Every change was made at transcription, against the built ids; the dry
run then passed with no further fix.

1. **P1: "on the lat subjects" is not selectable at set grain** — the
   short subjects are typed per FAMILY, not per script (utf8_set_v1.md
   4.3), so P1.a reads the whole short set, and "differ" is scored
   direction-neutrally (`ratio_max_min_over`).
2. **Unsupported-by-declaration is INEXPRESSIBLE in the report TSV** —
   `render_tsv` has no unsupported section (only `--format matrix` carries
   `unsup`, and `interpret` does not read the matrix). P5.a and P9.b are
   prose, not rows, per the directory's "must not happen" rule
   (`docs/dev/predictions/CLAUDE.md`). The design's §11 proposed scoring
   them over an `unsupported_by_pattern` SECTION; no such section exists.
3. **P7's raised-cap half has no testee** — no `pcrec-*-bigcap-utf8` config
   exists. P7.a also inherits the known residual: zero refusals reads
   `not-evaluable`, never `refuted` (a `did_not_compile` count has no row
   to count).
4. **P5.b leaves out `pcre2-utf-dfa`** — its longest-at-leftmost-start
   convention can disagree with the leftmost-first oracle on ANSWERS, which
   is not what "compiles cleanly" claims.
5. **P9/P10 exclude `prp-greek`, and P11 is added** — U2's census measured
   that rust and vectorscan read bare `\p{Greek}` as Script, so the design's
   "n_wrong eq 0 on every pattern" was already refuted in advance on
   `prp-greek`; the divergence is predicted as itself (P11), as
   utf8_set_v1.md 7.4 requires, not left to refute P9/P10.

## Growth plan (utf8_set_v1.md 6; §14 Q7 the default)

| stage | adds | axis | version |
|---|---|---|---|
| (g) find-all / `next_pos` over multi-byte subjects at the search grain | empty-matching patterns over multi-byte text, a zero-width assertion repeated, the `\G` chain | 9 | **0.2** |
| (k) the `-e byte` MIRROR arm | the same patterns and subjects compiled `-e byte` (four pcrec configs; a large expected refusal census above 0xFF); scores P8 | 1b, 2b | **0.2** |
| (h) INVALID UTF-8 subjects | nine ill-formed kinds × three positions, a per-engine DOCUMENTED-BEHAVIOUR TABLE, never a ranked cell (§8.3; §14 Q10 BLOCKS at (h)) | 3 | **0.3** |
| (i) start-position-inside-a-character search | the reachable half only (engine-invented candidate starts) | 11 | **0.3** |
| (j) surrogate / overlong witnesses | the three surrogate encodings, the overlong forms | 10 | **0.3** |

A `tre-wide` configuration is ROSTER growth, not set growth. **No
`--startpos` protocol extension (§14 Q8):** axis 11's caller-supplied
mid-character start is `~/pcrec/tests/utf8/axis11`'s correctness question;
a protocol parameter one family of one set would use is a cost six other
sets pay.

## Engine neutrality (R-BENCH-4)

No pcrec-oracled limit, cap or refusal boundary appears in this set's
patterns, subjects or expectations: no `oracle_limits.tsv` (the axis is the
encoding, which has no rung ladder); `prp-ingreek`'s refusal is a
PCRE2/Unicode fact; the `\p` size cliff is a PREDICTION (P7), not a design
input; the `-e byte` mirror is a testee-config fact.

## Cell time

utf8_set_v1.md 10.3 (F-M3): ~41-53 min per cell, ~1.5-1.8× `CELL_CAP`
headroom. **Lever 1 (drop the per-script 64 KB throughput arm, ~4 min) is
PRE-COMMITTED** as the first-sample cut if the rehearsal cell exceeds
50 min. §14 Q6's first sample: `pcrec-*-utf8` ×4 + `pcre2-utf-interp` +
`pcre2-utf-jit` + `rust-default`. (Lever 1 would drop four subjects from
the set; every P above that reads a per-script subject — P2, P3, R3, R4 —
would then need re-stating before that window.)
