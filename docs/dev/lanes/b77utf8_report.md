# Lane `b77utf8` — [B77], the `bench/utf8` design note

**2026-09-23. Branch `lane/b77utf8`. DESIGN ONLY.** Nothing built:
`bench/utf8/` was deliberately NOT created (the brief's own instruction
— the build lanes come after the panel), and no file under `bench/`,
`schema/`, `pcrecbench/`, `testees/` or `store/` is touched. No build,
no compile, no timed measurement — the box carried a CPU-heavy detached
sweep for this lane's whole window and nothing here read a clock.

## Delivered

| commit | what |
|---|---|
| `17f71da` | `docs/design/utf8_set_v1.md` v0.1 — fifteen sections |
| `8976c98` | `docs/design/CLAUDE.md` — the entry for it |
| `20cf28d` | the vectorscan correction (below) and a new §7.6 |

## Counts

- **74 patterns** = 73 members + the floor, in six first-release
  families: (a) classes 14, (b) multi-byte literals 12, (c) caseless 12,
  (d) alternation/quantifiers 12, (e) assertions 11, (f) properties 12.
  Every member is drafted with its id, its actual pattern text, the
  encoding-dependence axis it exercises and its control twin or designed
  near-miss.
- **5 growth stages** (g)-(k), each with a version: 0.2 = (g) find-all +
  (k) the `-e byte` mirror; 0.3 = (h) invalid UTF-8 + (i) startpos + (j)
  surrogates.
- **90 short subjects + 7 throughput subjects** over five generated
  script corpora; ~40-45 min/cell, ~2× `CELL_CAP` headroom, two
  pre-priced levers.
- **10 predictions** P1-P10, **9 outlier rules** R0-R8, **10 questions**
  Q1-Q10, **7 risks** R1-R7, **5 build lanes** U1-U5.

## The axis-coverage table's gaps, stated honestly

The set's completeness claim is I-90's own sentence — "the subbench
measures SPEED on the same axes" as `~/pcrec/tests/utf8/axis01-12` —
and §3.3 states where it does not hold:

1. **Axes 3 (invalid UTF-8), 10 (surrogates) and the caller half of 11
   are NOT in 0.1.** They are growth (h), (j), (i). All three need the
   same thing first — a policy for a subject the oracle will not answer
   under plain `PCRE2_UTF` (§8.3) — so they ship together at 0.3.
2. **Axis 5's 34-spelling `\p`-refusal census is permanently out**, and
   so is most of axis 4's 37 general-category spellings. One refusal
   witness (`prp-ingreek`) and six categories ship. A refusal has no
   speed, and the thirty-seventh `\p` spelling costs what the sixth
   does — the census is a CORRECTNESS instrument that
   `~/pcrec/tests/utf8` already owns. This is by design, not a
   sequencing gap.
3. **Axis 11's caller-supplied mid-character `startpos` is
   STRUCTURALLY UNREACHABLE at any release.** The driver protocol has
   no `--startpos`: every measured call starts at offset 0 and later
   positions come from the find-all advance. The half that IS reachable
   — the positions the ENGINE invents during an unanchored scan, which
   is what K50 was actually about — ships at 0.1 as `asr-B-midchar`.
   Naming a `--startpos` protocol extension is a harness question (Q8;
   recommendation: don't).
4. **The `byte`-mirror axes** are reachable only under growth (k), and
   only for the sub-population pcrec compiles under `-e byte` —
   `\x{...}` above 0xFF is range-refused there, so much of family (a)
   has no mirror cell at all. §6(k) states the expected refusal census
   rather than promising a full mirror.
5. **UCP has no pcrec axis** (utf8_design.md §4.5, quoted), so every
   `unicode-class-scope` pattern is `unsupported-by-declaration` on
   every pcrec config. That is P5, and a census row, not a hole.

## Roster decisions

Every adapter in this repo is deliberately BYTE-mode today and each one
says so in its own file — three of them naming `bench/capability`'s
family 12 as the reason. So this is a SECOND CONFIG per engine, not a
mode to turn on.

| engine | decision | adapter change |
|---|---|---|
| pcre2 ×3 | three new `pcre2-utf-*` configs | `driver.c:325` hard-codes the compile options word to `0`; needs `--utf`/`--ucp` argv flags, plus the §8.4 find-all fix |
| pcrec ×4 | four new `-e utf8` configs | `configs.toml` rows only — `flags` already land in `build_flags` AND the derived `testee_id`, so the encoding becomes an identity the way `-bigcap` is |
| **rust** | **`rust-default` UNCHANGED, and already correct** | **zero.** `RegexBuilder::unicode` defaults true and `regex::bytes` matches a code point against its UTF-8 ENCODING in the haystack — `testees/rust/CLAUDE.md`'s own measured section. The finding worth stating: rust's presence in this repo's BYTE sets is the anomaly, not its presence here |
| re2 | one new `re2-utf8` | `driver.cc:220` overrides RE2's own UTF-8 default to `EncodingLatin1`; one argv flag. The cheapest change on the roster |
| onig | one new `onig-utf8`, plus a re-census | `driver.c:91` is a compile-time `#define`; needs a runtime choice between two `OnigEncoding` pointers. `unicode-properties` is withheld today under ASCII encoding and is expected to flip — witness required before the declaration changes |
| vectorscan | one new config, BOOLEAN GRAIN ONLY | `driver.c:125` `VS_DRIVER_FLAGS` is 0; flags from argv. Frank's Q3 ruling unchanged |
| **tre** | **EXCLUDED from v1** | — |

### The TRE ruling I propose (§7.3)

**`tre-default` runs NO (a)-(f) cell in `utf8@0.1`, excluded by an
unsatisfied `utf8-encoding` REQUIRES token** — so every pattern is a
clean `unsupported-by-declaration` compile row citing the token by name,
a CENSUS row rather than an absence. Three reasons:

1. **There is no byte-mode UTF-8 in TRE.** `tre_regncompb` is
   byte-literal by construction and `testees/tre/driver.c:19` states the
   convention this project adopted for it ("a byte ≥ 0x80 is one
   [character]"). Every (a)-(f) pattern would get a BYTE-DECOMPOSED
   reading — a different question's answer, sitting in the same ranking
   column as the right one.
2. **The only UTF-8 path is the wide-character family and it is a
   second driver model.** `/usr/include/tre/tre.h:207-236` declares
   `tre_regwcomp`/`tre_regwexec`/`tre_regwncomp`/`tre_regwnexec`, all
   `wchar_t`. Using them means transcoding pattern and every subject,
   calling `setlocale(LC_CTYPE, …)` inside the driver (so behaviour
   becomes a property of the process environment rather than the
   config), and a length unit of CHARACTERS — which breaks the
   `consumed_length` convention `testees/tre/CLAUDE.md` (b) states and
   makes every per-byte throughput number non-comparable.
3. **The honest alternative is already covered.** Byte-mode TRE over
   UTF-8 subjects measures what a byte engine does to UTF-8 text —
   exactly what growth (k)'s `pcrec -e byte` mirror measures, more
   cheaply and with a SAME-ENGINE control on the other side of one
   variable.

`tre-wide` is NAMED as roster growth, not built; the two things to
settle first are in reason 2.

### Three new REQUIRES tokens (§7.5)

`utf8-encoding`, `ascii-class-scope`, `unicode-class-scope`. Class scope
is made a PATTERN property with two tokens rather than a per-config
dial, so each pattern keeps one canonical answer and the shipped
`unsupported-by-declaration` machinery scores it — the cross-convention
scoring `bench/capability` family 11 is still waiting on is exactly what
a dial would have required.

## One correction this lane made to itself

§7.4 first marked "does Vectorscan accept `\p{...}` at all?" UNCONFIRMED.
It is not: `testees/vectorscan/driver.c:50-53` carries a MEASURED A/B
already in this repo — `\p{L}` compiles identically with and without
`HS_FLAG_UCP`, while setting UCP **BREAKS `\b` on five real corpus
patterns** (40/64 corpus compiles at flags 0 against 35/64 under UCP).
Corrected in `20cf28d`, which also adds **§7.6**: `unicode-class-scope`
is NOT satisfiable on vectorscan by setting the flag (a "dial" that
widens class scope and simultaneously makes five `\b` patterns refuse is
not the dial `PCRE2_UCP` is), so `asr-b-cyr-ucp` becomes a
`pcre2-utf-*`-only row — and this is the sharpest available argument for
the two-token decision above.

## The sharpest thing the note found (§8.4)

`pcrecbench/oracle_pcre2.py:308`'s own docstring says *"Byte encoding:
… `start + 1` (every position is a character boundary); this bench never
compiles a utf8 artifact."* That sentence stops being true, and both
halves of it matter:

- `s + 1` after an EMPTY match at a multi-byte character lands
  MID-CHARACTER; PCRE2 under `PCRE2_UTF` rejects a mid-character
  `startoffset` with `PCRE2_ERROR_BADUTFOFFSET`.
- Every DRIVER's find-all loop has the same shape (KB-17 adopted
  pcrec's `match_api.md` S3.1 rule by reference), so a byte-stepping
  driver and a character-stepping one would report different
  `NMATCHES` — a harness difference masquerading as an engine
  difference, which is the one thing the shared protocol exists to
  prevent.

This is a HARNESS change to shared code six sets depend on, it must land
and be checked (with a negative arm: a byte-stepping advance must FAIL
the check) BEFORE the first expectation is derived, and it is why build
lane U1 blocks everything and owes a byte-identical re-derivation of
every existing set's `expectations.tsv` as its FIRST deliverable.

## The Q-list

| # | question | recommendation | mark |
|---|---|---|---|
| Q1 | Does the byte-clean ASCII control corpus RANK, or is it provenance-only? (Frank's own flagged item) | **RANK it** — it is the encoding-cost control (R3) and the mirror's zero point (P8); provenance-only makes both unscoreable | DEFAULT |
| Q2 | Is a hand-authored per-script WORD POOL "generated" or "sourced"? | **Generated**; commit the pools, `fidelity = synthesized` / `source_name = authored`, and state the limitation sentence | DEFAULT |
| Q3 | REQUIRES vocabulary global or per-set? Three tokens touch shared code | **Global; add the three** — a capability token is a cross-engine fact | DEFAULT |
| Q4 | The TRE ruling above | **Yes, as proposed** | DEFAULT |
| Q5 | Does `bench/utf8/` RETIRE `bench/syntax/NOTES.md`'s reserved `bench/syntaxutf/` slot? | **Both stand** — different sets (§2.2), and `syntaxutf` gets cheaper on this one's machinery. One pointer sentence added to the reservation | **BLOCK** (a documented commitment) |
| Q6 | Which cells are the FIRST sample? Twelve configs ≈ 8.5 h is more than one night | **Seven cells** (pcrec ×4 + `pcre2-utf-interp`/`-jit` + `rust-default`, ≈ 5 h) — carries all three of I-90 §5's first customers plus the widest capability contrast | DEFAULT |
| Q7 | Growth ordering 0.2 = (g)+(k), 0.3 = (h)+(i)+(j)? | **Yes** — (h)/(i)/(j) share one policy and one subject problem | DEFAULT |
| Q8 | Is a driver-protocol `--startpos` worth it for axis 11's caller half? | **No**, and say so in `NOTES.md` | DEFAULT |
| Q9 | Per-pattern oracle option word: a parameter on the shared `oracle_pcre2.py`, or a second oracle module? | **A parameter on the shared module** — `bench/syntax/NOTES.md` predicted exactly this. U1 then owes the byte-identical re-derivation check | DEFAULT |
| Q10 | At growth (h): may `PCRE2_MATCH_INVALID_UTF` be a SECOND canonical expectation? | **Documented-behaviour-only** | **BLOCK at (h)** |

## Validation

Design-only lane: no test suite is in scope and nothing was run that
touches the box. What WAS validated, by re-reading each cited file:

- **Every `file:line` citation in the note was re-derived by grep after
  writing**, not carried from memory: `oracle_pcre2.py:47` and `:308`,
  `testees/pcre2/driver.c:325` (options word hard-coded `0`),
  `testees/re2/driver.cc:220`, `testees/onig/driver.c:91`,
  `testees/vectorscan/driver.c:50-59` and `:125`,
  `/usr/include/tre/tre.h:207-236`, `testees/tre/driver.c:19`,
  `pcrecbench/capability.py:87`, `testees/pcrec/adapter.py:2370`. All
  ten confirmed; the vectorscan re-read is what produced the correction
  above.
- The twelve axis names and properties come from each `axisNN_*.rxt`
  header in `~/pcrec/tests/utf8/` plus that directory's `CLAUDE.md`,
  read this session.
- `utf8_design.md` §2.6, §3.3, §3.4, §4.1, §4.2, §4.5, §6.3 and §9.2
  and `reqbyte_freq_pick.md` §3 (read at `main` c051a69b via
  `git cat-file`, the file not being present at the checkout's HEAD)
  are quoted rather than paraphrased where a claim rests on them.

**OWED: nothing.** No background job was launched; no number in this
report is pending.

## What a reviewer should push on

1. **§4.1's generated-corpus decision.** The note narrows the claim to
   byte and character-width statistics and says so twice, but a panel
   should test whether the five word pools can carry the lead-byte
   distributions §4.2 asserts — particularly `cjk`'s ASCII minority.
2. **§10.3's ~2× `CELL_CAP` headroom**, the thinnest of any set. The
   levers are named and pre-priced; the arithmetic should be re-checked
   against a real calibration rather than the model.
3. **§8.3's documented-behaviour-table policy for (h)/(i)/(j).** It is
   the right answer if there really is no cross-engine canonical answer
   — which the note asserts from three engines' postures and admits it
   has not established for RE2, Rust or Vectorscan.
4. **Whether 74 patterns is "somewhat complete, not small"** against
   Frank's own words, or whether family (a) at 14 members under-serves
   the example he named first.
