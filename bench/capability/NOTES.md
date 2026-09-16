# bench/capability@0.1 — the capability survey set: objective, families, predictions

Read this before touching a pattern, a subject or a generator. Design
authority: `docs/design/capability_set_v1.md` (v0.2, the family taxonomy,
provenance model, capability model, metrics, roster) and
`docs/design/rxt_needs_v1.md` (the `.rxt`-format restart this set is
built on). Curation authority: `bench/capability/curation/` (L1's wild
imports, L2's designed members) — kept as provenance-of-authorship, not
deleted now that L3 has built on it.

## Objective (§2 of the design)

A CAPABILITY CONTRAST across the [B7] engine roster: what each engine can
EXPRESS, what it REFUSES, and what the expressible patterns COST — over a
set built from real, deployed regex shapes wherever a permissive-licensed
source could be fetched, and authored fresh, held to the SAME realism
rule, where none exists. This is a new sub-bench, not an extension of
`bench/syntax`: the census is registry-enumerated and homogeneous-bodied
by design (§2.2), and a wild pattern is the opposite property on
purpose.

**BUILT ON `.rxt`.** Frank's Q3 ruling (2026-09-12) makes this set a
driver of pcrec's `.rxt` format: `patterns.rxt` is the pattern SOURCE OF
TRUTH (not a sidecar hybrid), authored by `gen_patterns.py` from L1's and
L2's curation tables. It passes `pcrec --list-source patterns.rxt`
cleanly (exit 0) and every block's decoded `pattern` column round-trips
byte-for-byte against the table's own canonical text — checked in
`gen_patterns.py --check`, not merely asserted. `patterns/*.rx` is a
DERIVED export kept beside it so `pcrecbench.subbench` (which has no
`.rxt` reader yet — that is L4's build, chartered separately) can load
this set with today's loader; `patterns.rxt` is authoritative, the `.rx`
files are its mechanical projection.

## Blinding statement, quoted from L2's own report

L1 (`curation/wild/`) fetched and adapted the six wild families' members
with full read access to the sources. L2 (`curation/designed/`) authored
families 7–12's designed members and every families-1–6 control twin
**blinded per pcrec D27**: `man pcre2pattern`, the engine docs,
`docs/design/capability_set_v1.md` and `docs/design/requirements.md`
only — no `testees/`, no `pcrecbench/adapters.py`, no `store/`, no
`reports/`, no ledgers, no other lane's worktree, no existing
`bench/*/` pattern file, and (critically) **no read of L1's own wild
pattern TEXT** before L2's own patterns were committed. L1 and L2 ran
concurrently; this lane (L3) is the first reader of both together.

## The twin-pairing reconciliation (this lane's own finding)

L2 authored four family-1 "near-miss twin" patterns *blind*, against
GUESSED wild imports named only by their macro/type (grok's UUID,
BASE10NUM, WINPATH; a canonical OWASP IPv4 shape). Reconciled against
L1's actual delivery:

| designed twin | guessed partner | actual wild partner | family | verdict |
|---|---|---|---|---|
| `uuid-near-miss` | grok UUID | `wild-validator-uuid-grok` | `wild-validator` | **CONFIRMED** — same family, isolates a real property (RFC 4122 version/variant nibbles) the wild import doesn't enforce |
| `ipv4-near-miss` | an OWASP IPv4 shape | `wild-validator-ipv4-owasp` | `wild-validator` | **CONFIRMED, but weaker than designed**: OWASP's actual pattern already range-bounds each octet (`25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?`), the SAME logic the twin uses — the two are **answer-identical on every subject tried** (both accept `192.168.1.1`, both reject `999.1.1.1`). The classic "naive `\d{1,3}`-per-octet" gotcha the twin was modeled on does not apply to the actual OWASP text; the pair still isolates real STRUCTURE cost (one pattern vs. a rewritten equivalent), just not an answer divergence. Stated here rather than silently claimed as a working near-miss |
| `base10num-near-miss` | grok BASE10NUM | `wild-logparse-base10num-grok` | `wild-logparse` (family 2), **NOT** `wild-validator` (family 1) | **MISMATCH, REPAIRED** — the pattern's family metadata is corrected to `wild-logparse`; its text is untouched. A real divergence exists: grok's BASE10NUM is an unanchored SEARCH macro with no leading-zero rule (`0123` is a hit), the near-miss twin is anchored + JSON-strict (`0123` is a miss) |
| `winpath-near-miss` | grok WINPATH | `wild-logparse-winpath-grok` | `wild-logparse` (family 2), **NOT** `wild-validator` (family 1) | **MISMATCH, REPAIRED**, same reason. Worse: the design note's own 2026-09-12 amendment *reassigned WINPATH from family 1 to family 2* (its atomic group contradicts family 1's "none unsupported" invariant) — a fact L2's blinded lane structurally could not have read, since the amendment postdates L2's blinding window. A real divergence exists: grok's WINPATH accepts any character but `\`/`?`/`*` in a path segment; the near-miss twin rejects all nine Windows-reserved characters |

Per the brief ("flag it in your report rather than re-authoring"): both
mismatched twins are **kept, with corrected family metadata only**. They
remain legitimate, realistic near-miss members of `wild-logparse` — a
deviation from that family's own "designed members: none" column
(§3.1: "the imports ARE the edge cases"), noted here rather than
silently absorbed. The full table is repeated in
`docs/dev/lanes/b42set_report.md`.

**Consequence for the family counts.** With the reassignment, family 1
(`wild-validator`) has 4 wild + 2 confirmed designed = 6 members (not
the design's target 8: no designed twin exists for `email` or `us-zip`
— L2's four twins covered only three of the four family-1 imports, and
one of those three turned out to belong to family 2). Family 2
(`wild-logparse`) gains the two reassigned twins on top of its native
`logparse-atomic`/`logparse-atomic-removed` pair, reaching 10 members
against a design target of 6. **Total membership is unaffected: 64
(63 + floor), matching the design's own arithmetic** (§3.1's 60-pattern
target was itself provisional pending the actual curation yield; §4.3's
ruling that the wild/designed split is a REALISM outcome, not a target
to hit, applies with equal force to family-level counts).

## The twelve families, as built

| # | family | members (wild / designed) | what it measures |
|---|---|---|---|
| 1 | `wild-validator` | 4 / 2 | everyday validator shapes (email, IPv4, US ZIP, UUID) vs. RFC-strict twins |
| 2 | `wild-logparse` | 6 / 4 | grok's atomic-group defence against backtracking, its own non-atomic control, and two reassigned near-miss twins (see above) |
| 3 | `wild-waf` | 5 / 0 | OWASP CRS SQLi rules — the imports ARE the edge cases |
| 4 | `wild-secrets` | 4 / 0 | short, first-byte-distinct secret-token shapes (rebar's noseyparker corpus) |
| 5 | `wild-datetime` | 2 / 0 | one enormous alternation (rebar's `datefinder`) + one MIT ISO-8601 import (moment.js) — the COMPILE-time and SIZE axis. **A finding this lane's own oracle run surfaced (see below): the datefinder alternation's THROUGHPUT cost is real and large, not just a compile-time concern** |
| 6 | `wild-codegrammar` | 5 / 2 | VS Code's JSON grammar + an authored `(?x)`/flattened control pair |
| 7 | `cap-backref` | 0 / 5 | deployed backreference idioms (doubled-word, tag pairs, palindrome phone numbers, quoted delimiters, HTTP parameter pollution) |
| 8 | `cap-lookaround` | 0 / 5 | chained lookahead (password strength), fixed lookbehind (currency), one VARIABLE lookbehind (bounded negation window) |
| 9 | `cap-recursion` | 0 / 4 | `(?R)`, `(?(DEFINE)...)`, `(?1)`, and a depth-3 NON-recursive control that isolates nesting depth from the recursion construct |
| 10 | `redos-nested` | 0 / 6 | six nested-quantifier ReDoS shapes, each modeled on a real advisory (Kubeflow, ua-parser-js CVE-2022-25927, moment.js CVE-2017-18214/CVE-2022-31129, awesome-redos-security's catalogue) |
| 11 | `semantics-divergence` | 3 / 3 | leftmost-first vs. leftmost-longest alternation order (three designed router/lexer bugs + a genuine rust-regex `leftmost-all.toml` witness), plus PCRE2's own empty-match-in-repeat and `$`-before-trailing-newline testdata cases |
| 12 | `binary-nonutf8` | 0 / 3 | byte-class shapes over non-UTF-8 subjects; `mojibake-curly-quote` is the one member whose `canonical_text` is genuinely omitted (S10's rule — raw 0x93/0x94 bytes, not `\x` escapes) |
| — | `floor` | 0 / 1 | `~`, the per-call overhead control |

**Total: 64 patterns (63 members + the floor)**, across 13 `tag family=`
values (12 + `floor`).

## What this lane did NOT build (deferred, by brief and by design)

- **Family 11's cross-convention SCORING machinery** — grading an
  RE2-longest or TRE testee against its OWN correct answer — is UNBUILT
  (CB1, `capability_set_v1.md` §5.6). Every `semantics-divergence`
  pattern here still compiles and gives a real answer under the shared
  `perl-leftmost-first` population (pcre2-interp/jit, pcrec); the three
  designed alternation-order patterns and the rust-regex witness carry
  no `under posix-leftmost-longest` case lines in v1's `patterns.rxt`
  (the `under` production exists in the delivered format and pcrec's own
  harness treats it as "a COUNTED, LABELLED SKIP", but there is no
  reason to author qualified answers this project's own harness cannot
  score yet — a future lane building the missing expectation-override
  machinery is where they belong).
- **The pre-compile capability policy** (§5.3: `REQUIRES(pattern) ⊄
  capabilities(config) ⇒ unsupported-by-declaration`) is NOT wired into
  `pcrecbench/harness.py`. This lane's `ext bench` block in
  `patterns.rxt` carries a first-cut capability matrix for the roster
  (six pinned pcre2-\*/pcrec-\* configs) as DOCUMENTATION for that future
  wiring (L5's scope) — it is a faithfully-dumped `ext` aux block
  ("pcrec parses the structure... and interprets nothing",
  `rxt_format.md`), never enforced today. **Caveat, stated plainly**:
  the pcrec capability entries (callouts marked unsupported;
  control-verbs, k-reset marked supported) are inferred from
  `bench/syntax`'s own census findings and pcrec's D26 PCRE2-compatibility
  posture, NOT independently re-derived from a real compile census the
  way §5.1's engine-notes table demands for a production capability
  declaration. L5 should re-verify every `pcrec-*` row before this
  matrix is trusted for real routing.
- **`variant.kind` rendering** (CB2) and the harness's own REQUIRES
  vocabulary validation are both unbuilt — outside this lane's scope
  (L5).
- **`gen_variants.py`'s table is deliberately EMPTY.** No testee in v1's
  roster needs a per-engine spelling rewrite; see that file's own
  docstring.
- **The `.rxt` loader** (`pcrecbench.subbench` reading `patterns.rxt`
  directly) is L4's build. `subbench.toml`'s `[[patterns]]` entries
  still point at `patterns/*.rx` for now.

## Subjects

**75 typed short subjects** (not the design's nominal 36 — see "Deviation
from the design's subject count" below) + **3 throughput texts** (64 KB /
256 KB / 1 MB, `captext.py`'s mixed log/HTTP/source/prose grammar,
deterministic per seed). Subjects are grouped and typed BY FAMILY, not
against one shared vocabulary (`bench/syntax`'s R3/R4 outlier rules —
spelling groups, a shared body — do not transfer to a wild-provenance
set; see "The outlier rule" below). Three subjects carry genuinely raw
non-UTF-8 bytes for family 12 (`nu-high-byte`, `nu-mojibake`,
`nu-lead-no-cont`/`nu-lead-with-cont`), legitimate because subjects live
as raw `.bin` files, never TSV cells.

**Deviation from the design's subject count.** `capability_set_v1.md`
§3.4 specified "thirty-six typed short subjects". This lane authored 75:
one hit (or hit/miss pair) per pattern across all twelve families rather
than a shared-body census where one subject types many patterns at once
— the natural consequence of 64 *heterogeneous* real-world patterns
versus the syntax census's homogeneous "cat" vocabulary, where a single
subject legitimately serves a dozen patterns. **Re-derived cell-time
arithmetic**: §3.5's own model (50 ms × n_subjects per (pattern, regime,
trial)) scales linearly in subject count, so `search_short` grows from
the design's ~11 min estimate to roughly (75/36)×11 ≈ 23 min per cell;
`throughput` is unaffected (subject count there is fixed at 3). Against
`CELL_CAP`'s 5,400 s (90 min) default this is still comfortable margin —
smaller than the design's original ~5× headroom, closer to ~2-2.5×, but
not a cap risk. Stated here as a deliberate, checked adjustment rather
than a silent overrun.

## A finding from this lane's own oracle-derivation run (CORRECTED)

**The real cause of the multi-hour `gen_expectations.py` run was a TSV
CSV-QUOTING BUG in `gen_patterns.py`, not a slow pattern.** First
foreground attempt at deriving `expectations.tsv` ran past 1h39m before
the manager intervened (killed by verified PID, per the lane
boilerplate); this lane's own `diag_expectations_timing.py`
(per-pattern `gnutimeout`-wrapped, timing every cell) isolated the true
culprit: `codegrammar-flat` (the family-6 `(?x)`/flattened control
twin, `"([^"\\]+)"\s*:\s*`) alone timed out at 90 s on just the 64 KB
throughput text, having completed all 77 other cells in milliseconds.

**Root cause**: `gen_patterns.py`'s `_read_tsv()` used Python's
`csv.DictReader` with its DEFAULT quoting rules on a plain
TAB-DELIMITED file. `codegrammar-flat`'s canonical text is the one
field, across both curation TSVs, that STARTS with a literal `"`
(`"([^"\\]+)"\s*:\s*`) — csv's default quoting silently treated that as
an OPENING QUOTE CHARACTER and swallowed it, so the actually-compiled
pattern was `([^\\]+)"\s*:\s*`, missing its leading `"`. Without that
leading literal, PCRE2 has NO required-first-byte optimization at all
(the pattern now starts with a capturing group matching almost every
byte), so an unanchored search over background text with no `"`
anywhere backtracks QUADRATICALLY over the whole unbroken run — 37 s on
64 KB, i.e. hours projected at 1 MB. **Fixed two ways**: (1)
`_read_tsv()` now passes `quoting=csv.QUOTE_NONE` (TSV is not CSV, and
no other field in either curation table was affected — checked by
grep, one field total across 64 rows × ~15 columns); (2) `load_designed()`
now cross-checks every text against `curation/designed/patterns/
SHA256SUMS.txt`'s own independently-staged hash, so a future parsing
regression of this shape fails loudly at generation time rather than
silently compiling the wrong pattern. **A second, independent
belt-and-braces fix**: `captext.py`'s `_source_line` now emits a
double-quoted string literal in roughly half its lines (a genuinely
common real source-code shape, `log.info("word_123")`), which bounds
ANY future `[^"...]+`-shaped pattern's worst-case unanchored backtrack
to one line's length instead of the whole subject — so this class of
hazard cannot recur even from a DIFFERENT cause.

With both fixes, the full `gen_expectations.py` run (4,990 rows) takes
**12.7 seconds**, not hours; the diagnostic sweep's own re-run confirms
zero pattern times out and the slowest single pattern
(`wild-datetime-datefinder-alternation`, genuinely the largest
alternation in the set) completes all 79 of its own cells in 9.3 s —
real, but nowhere near the runaway the first attempt suggested. My
original hypothesis (blamed on the datefinder alternation's breadth)
was WRONG and is corrected here rather than left standing.

**A second, smaller finding from the same corrected run**: the oracle
GAVE UP (PCRE2's own match-limit, not a hang) on two triples —
`evil-alt-nested` (`^(([a-z]+)*)+$`) against its own SHORT near-miss
subject (`rd-evil-alt-near-miss`, 17 `a`s + `!`) and against
`sd-empty-alt-hit` (60 `a`s + a digit, authored for a DIFFERENT
pattern's PCRE2-testdata case). Both are DROPPED from `expectations.tsv`
and listed on stderr, per the shared derivation's own existing rule —
the correct, honest outcome for a genuinely nested-quantifier pattern
meeting an adversarial-shaped subject, not a bug. It confirms
`evil-alt-nested` needs no SEPARATE calibration mitigation beyond what
already exists (family 10's design-stated fixed-`--iters` plan, CB8):
the oracle-derivation stage already demonstrates the pattern is
immune to a real hang, only to PCRE2's own bounded give-up.

## The outlier rule (R0–Rn, stated before any run)

Following `bench/syntax`'s own discipline, and departing from it exactly
where this design predicted departure would be needed
(§11.3: "rules R3 ... and R4 ... do not apply to wild bodies"):

- **R0 — a wrong answer is read first**, before any speed comparison, on
  every cell.
- **R1 — a refusal on a pattern whose REQUIRES the config claims to
  satisfy is a finding, not a footnote.** This set's version is sharper
  than the census's: every `requires=` tag on a pattern is a
  machine-checkable claim (`tag requires=<vocab-value>`, closed against
  `vocabulary requires` in `patterns.rxt`), so "should have compiled"
  is a fact the record itself can be checked against, not a reviewer's
  guess.
- **R2 — the `pcre2-jit` band.** A `pcre2-jit` cell inside its usual
  compile-time / match-time band relative to `pcre2-interp` is not a
  finding; outside it is.
- **R3/R4 are RETIRED for this set** (unlike `bench/syntax`): there is
  no shared body and no spelling-group taxonomy across 64 heterogeneous
  wild+designed patterns. The families table above is this set's own
  grouping instrument, and a family's members are compared to EACH
  OTHER and to their own control twins, never pooled across families.
- **R5 — compile/size cliffs.** Any pcrec compile row whose
  `emit_bytes`/`artifact_bytes` jumps by an order of magnitude against a
  same-family sibling (the datefinder alternation, the largest pattern
  in the set by source bytes, is the leading candidate) is read before
  any speed number from that row.
- **R6 — a non-flat throughput sweep, on EVERY pattern, not one named
  candidate.** This lane's own diagnostic finding (NOTES.md, "A finding
  from this lane's own oracle-derivation run") is that the set's real
  first-sample risk is not one slow pattern but a QUADRATIC-BACKTRACK
  HAZARD any unanchored `[^X]+`-shaped pattern can hit against
  background text lacking its terminator `X` — found once
  (`codegrammar-flat`, a TSV-parsing bug, now fixed and guarded two
  ways) and not assumed absent elsewhere. Any throughput cell whose
  ns/byte is NOT flat across the three sizes is read FIRST, for every
  pattern, as this rule's own positive case.
- **R7 — an `unsupported-by-declaration` share is a CENSUS finding, not
  missing data.** Per §13 R2, roughly a third of the set's members carry
  a REQUIRES tag that RE2/Rust/Vectorscan/TRE fail; those four engines
  are not in v1's roster (§11.4), so this rule is dormant until [B7]'s
  adapters land, and is stated here so it is not silently invented then.
- **R8 — the twin-pairing reconciliation above is itself a control.**
  `ipv4-near-miss` reading answer-IDENTICAL to `wild-validator-ipv4-owasp`
  on every subject is the expected, checked finding (§13 R1: "if they
  agree everywhere, that IS the finding"), not a broken pair — do not
  "fix" it by authoring a new near-miss twin without re-reading this
  file's reconciliation table first.

## The predictions (P1–P10)

Stated before any cell runs, per `docs/dev/predictions/CLAUDE.md`'s
fifteen-column format; see `docs/dev/predictions/capability-0.1-first.tsv`
for the machine-readable transcription. All eight pinned candidates
(pcre2-interp, pcre2-jit, and the four pcrec configs this design names as
v1's roster: auto, nocaps, vm, vm-in) are assumed unless stated.

- **P1.** Every pattern in families 3 (`wild-waf`), 4 (`wild-secrets`)
  and 6 (`wild-codegrammar`) compiles cleanly on every roster testee —
  none of these three families' imports use a construct any roster
  engine refuses (§3.1's own "expected unsupported: none" column).
- **P2.** `pcre2-jit` compiles measurably slower than `pcre2-interp` on
  `wild-waf-crs-942360-concat-sqli` and `wild-datetime-datefinder-
  alternation` specifically (the two largest patterns in the set by
  source bytes) and is within the usual small band everywhere else.
- **P3.** `codegrammar-flat`'s `throughput` regime cost is measurably
  the highest ns/byte of any `wild-codegrammar`/family-6 member (the
  pattern whose quadratic-backtrack hazard this lane's own diagnostic
  sweep found and fixed at generation time — see "A finding from this
  lane's own oracle-derivation run"): even with the fix, a per-position
  greedy negated-class scan is intrinsically more expensive per byte
  than the set's other short, literal-anchored codegrammar members.
- **P4.** `logparse-atomic` compiles to a smaller or equal artifact than
  `logparse-atomic-removed` on every pcrec config, and the ATOMIC form's
  `search_short` cost on `lp-atomic-nonmatch` (the crafted near-miss) is
  LOWER than the non-atomic form's — the family's whole point, restated
  as a checkable pair.
- **P5.** Every `redos-nested` pattern's `search_short` cell completes
  with `n_wrong eq 0` on every roster testee (none refuses to compile;
  none of the ReDoS witnesses actually exhibits catastrophic growth on
  the SHORT near-miss subjects authored here — they are deliberately
  bounded to ≤ 20 bytes, per `gen_subjects.py`'s own design note).
- **P6.** `uuid-near-miss` and `wild-validator-uuid-grok` diverge (give
  different `match`/`nomatch` answers) on `v-uuid-badnibble` and agree
  on `v-uuid-valid` — the pair's designed contrast, oracle-confirmed.
- **P7.** `ipv4-near-miss` and `wild-validator-ipv4-owasp` give IDENTICAL
  answers on every subject in this set (`v-ipv4`, `v-ipv4-oor`) — the
  reconciliation finding above, restated as a checkable prediction
  rather than left as prose.
- **P8.** No pcrec config's compile row for any pattern in this set
  carries `compile_outcome = did-not-compile` — every construct used
  here (backreferences, lookaround incl. one variable-width lookbehind,
  recursion/DEFINE/subroutine calls, `(?x)`, raw high bytes) is a
  construct `bench/syntax`'s own first sample already confirmed pcrec
  builds.
- **P9.** `mojibake-curly-quote`'s record carries no `patterns[].
  canonical_text` field for that pattern (S10's omission rule) and its
  identity is checkable only via `canonical_sha256` — this is a
  structural prediction about the RECORD, checkable once the schema
  promotion (CB3) and a future measurement land, named here so it is
  not overlooked.
- **P10.** `nu-lead-no-cont` (`\xc2X`, a lead byte with no valid
  continuation) matches and `nu-lead-with-cont` (`\xc3\xa9`, a
  well-formed two-byte sequence) does not — `utf8-lead-no-cont`'s
  designed contrast, oracle-confirmed at generation time (this lane's
  own `gen_expectations.py` run is the check).

## What is engine-neutral here (R-BENCH-4)

No pcrec-oracled limit, cap or refusal boundary appears anywhere in this
set's patterns, subjects or expectations — every expectation is derived
from libpcre2 (`method = libpcre2-differential`), and the `ext bench`
capability matrix is documentation for a future harness policy, never a
gate this set's own generators enforce.

## Room left, not built

- Family 11's cross-convention scoring (above).
- The Davis et al. corpus (`capability_set_v1.md` §4.5) — explicitly OUT
  of v1, a stated `@0.2` candidate.
- `pcre2-dfa` as a fourth testee (§8, L6a) — this set's patterns and
  subjects make no assumption that would block it; `captures` and
  `k-reset` REQUIRES tags exist on several patterns specifically because
  `pcre2-dfa` is the one testee in the design's roster table that fails
  both.
- The six [B7] non-pcre2/pcrec adapters (RE2, Rust `regex`, Oniguruma,
  TRE, Vectorscan, python/perl) — R7 above is dormant until they land.
