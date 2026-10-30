# bench/capability@0.4 — the capability survey set: objective, families, predictions

(@0.4, [B172], 2026-10-30: the LAST section is the 0.4 text; 0.4 changes no pattern, no short subject, no 0.1-0.3 throughput text, and appends two query-string subjects.)
(@0.3, [B123], 2026-10-25: the LAST section is the 0.3 text; 0.3 changes no pattern, no short subject, no 0.1/0.2 throughput text.)
(@0.2, [B125], 2026-10-08: read the section "capability@0.2" at the END of this file first for what
changed; everything above it is the @0.1 text, still true of the first 64 patterns, 75 short subjects
and 3 throughput texts, all byte-identical in 0.2.)

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
  capabilities(config) ⇒ unsupported-by-declaration`) is now WIRED into
  `pcrecbench/harness.py` (`pcrecbench/capability.py`, lane `b42cap`,
  L5, 2026-09-16), decided BEFORE `adapter.compile()` is ever called for
  a pattern whose REQUIRES tokens are not a subset of the testee's
  declared capabilities. The `ext bench` block in `patterns.rxt` is the
  declaration it reads (via `pcrecbench.rxt_source.load_aux_rows`, which
  does not run into outbox O-29 — that gate is scoped to per-pattern
  `provenance`/`variants` rows, and the `ext` aux block sits outside the
  main pattern table entirely; see `docs/dev/lanes/b42cap_report.md` for
  which load path each check exercises, since `bench/capability` itself
  is NOT rxt-loadable as a whole at this pin).
- **L5's re-verification (2026-09-16) corrected three wrong `pcrec-*`
  declarations.** This lane's own caveat above was right to distrust the
  first cut: it was inferred from `bench/syntax`'s census and pcrec's
  D26 posture, not from a real compile census. A witness compile per
  (config, token) pair at the pinned pcrec (`--features all`, each
  config's own `--engine=`/`--no-captures` flags) found `conditionals`
  and `control-verbs` WRONGLY marked satisfied on every `pcrec-*` config
  (both are `REJECTED`/"not implemented yet" even with their module
  enabled — `(?(1)a|b)(a)?` and `a(*ACCEPT)b` both refuse, D26 tier 4 for
  the verb; `(?(DEFINE)...)` alone ships, under module `recursion`, and
  is NOT this token) and `lookbehind-variable` WRONGLY marked satisfied
  (pcrec's lookbehind ships FIXED-WIDTH PER BRANCH — differing branch
  widths compile, e.g. `(?<=a|bc)x`, but this set's OWN
  `negation-scope-lookbehind-var` witness, a single-branch variable-width
  body, is refused: "variable-length lookbehind is not implemented").
  `callouts` was already correctly marked unsupported. Every other token
  was spot-verified compiling on every `pcrec-*` config. `gen_patterns.py`'s
  `EXT_BENCH_ROSTER` table is the fix (never hand-edit `patterns.rxt`);
  the full (config, token) witness matrix is
  `docs/dev/lanes/b42cap_report.md`.
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

## The REQUIRES-tag correction wave (lane b46tags, 2026-09-17)

[B42] set hygiene, per Frank's ruling that capability-set completion is
the priority: a mechanical + eyes-on audit of every one of the 64
patterns' `requires-*` tags against the constructs its own canonical
text actually uses (PCRE2 `pcre2_pattern_info`'s `NAMECOUNT`/
`BACKREFMAX` for `backrefs`/`named-groups`, a textual construct scan for
the rest, cross-checked by inspection), triggered by lane `l6btre`'s
census finding two under-tagged members. **Six patterns were
under-tagged; none were over-tagged.** All six fixes are in
`curation/designed/members.tsv`'s `requires` column (every affected
pattern is a DESIGNED member; no `REQUIRES_OVERRIDE` entry in
`gen_patterns.py` needed a change):

| pattern | old `requires` | new `requires` | evidence |
|---|---|---|---|
| `quoted-delim-match` | `backrefs` | `backrefs;lookaround` | body is `(["'])(?:(?!\1)[^\\]|\\.)*\1` — the refusal cause on an engine that satisfies `backrefs` but not `lookaround` is the embedded `(?!\1)` negative lookahead, not the backreference (`l6btre`'s census finding, `testees/tre/CLAUDE.md` item (d).5) |
| `utf8-lead-no-cont` | `non-utf8-subject` | `non-utf8-subject;lookaround` | body is `[\xc2-\xdf](?![\x80-\xbf])` — same shape, the `(?!...)` negative lookahead (`l6btre`'s census finding) |
| `tag-depth3-bound` | `-` (none) | `backrefs` | body is `<(\w+)>(?:[^<]\|<(\w+)>(?:[^<]\|<(\w+)>[^<]*</\3>)*</\2>)*</\1>` — three numbered backreferences (`\1`/`\2`/`\3`), confirmed via `pcre2_pattern_info(PCRE2_INFO_BACKREFMAX)` = 3; independently already flagged in `gen_patterns.py`'s own `vectorscan-block-nosom` comment as "a pre-existing corpus tagging gap" |
| `codegrammar-xflag` | `free-spacing` | `free-spacing;named-groups` | body contains `(?<key> ... )`, a genuine named capturing group used inside `(?x)` mode — confirmed via `pcre2_pattern_info(PCRE2_INFO_NAMECOUNT)` = 1 |
| `bracket-array-define` | `recursion;free-spacing` | `recursion;free-spacing;named-groups` | the `(?(DEFINE) (?<brackets> ... ) )` subroutine target is a named group `(?&brackets)` calls by name — `PCRE2_INFO_NAMECOUNT` = 1 |
| `nested-comment-rec` | `recursion` | `recursion;lookaround` | body `(/\*(?:[^*/]\|\*(?!/)\|/(?!\*)\|(?1))*\*/)` carries two negative lookaheads (`\*(?!/)`, `/(?!\*)`) alongside the numbered subroutine call `(?1)` |

**No live roster witness currently flips for the `named-groups`/
`lookaround`-on-`nested-comment-rec` additions**: every `ext bench` row
that satisfies `recursion` also already satisfies `free-spacing`,
`named-groups` and `lookaround` together (`pcre2-*`, `pcrec-*`,
`onig-default`) — there is no config today that would have compiled
these three patterns wrongly-attributed before the fix. The fix is
still correct (a future roster engine with `recursion` but not
`named-groups`, or `lookaround` without a lookbehind story, would need
it) and is evidenced structurally, not behaviorally, for these three.
The other three fixes (`quoted-delim-match`, `utf8-lead-no-cont` on
`tre-default`; `tag-depth3-bound` on `vectorscan-block-nosom`) WERE
witnessed flipping from what would have been a raw driver-level refusal
to a clean `unsupported-by-declaration` compile row citing the missing
token by name — `docs/dev/lanes/b46tags_report.md` has the full
transcripts, including the raw `libtre.so.5`/direct-ctypes compile
proving the isolated construct (not the backreference) is what refuses.
Every satisfied engine (`pcre2-interp`, `pcrec-auto` on the two
`tre-default` witnesses) was re-run and confirmed UNCHANGED — still a
real, measured match cell, not a refusal.

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

## capability@0.2 ([B125], 2026-10-08) -- the additions, the second method, the predictions

Origin: outbox O-87/O-88 and inbox I-136 (Frank-approved, plan [B125]). The
revision is in place, in the altwide@0.1 -> 0.2 manner: every 0.1 pattern keeps
its exact bytes, every 0.1 short subject and throughput text reproduces byte for
byte (`gen_throughput_subjects.py` asserts the three 0.1 sha256s), and every 0.1
expectation row survives unchanged (checked: the 0.1 file is a subset of the 0.2
file, plus the two restored triples). The new subjects draw from fresh `Rng`
seeds (`0xC0FFEE11`...`0xC0FFEE21`) and are APPENDED to the throughput manifest.

**Which regime.** Every new subject is longer than `short_search_max_bytes`
(512), so it belongs to the THROUGHPUT regime only, and the throughput regime is
"every pattern x every throughput subject": all 71 patterns run on each new
subject (the oracle derivation proves none hangs; cost below). No new subject
enters `search_short`. The two restored triples ARE `search_short`.

New patterns (7, family `wild-logparse`, provenance `authored`/`synthesized`, sourced to I-136):
`letters-bounded-tail-z` `(?:[a-z]{0,1024})\z`, `tail-digits-eol` `\d+$`,
`tail-word-eoz` `\w+\z`, `tail-space-eol` `\s+$`, `tail-ext-lower-txt`
`[a-z]+\.txt$`, `tail-dotstar-txt` `.*\.txt$`, `hex8-bounded`
`\b[0-9a-f]{8}\b`. The two `\z` ones carry `requires=true-end-anchor` (all 51
roster rows declare it; TRE via the adapter's own wrap). Engine-neutral
(R-BENCH-4): none is a pcrec-shaped pattern, each is a deployed-shape check.
NB I-136 says capability "has hex32-id"; it has no such pattern (the UUID pair is
hyphen-delimited, the secrets are prefixed), so `hex8-bounded` fills a real gap.

New subjects (8, all throughput): `t-evil-match-60k` (61,440 B of random [a-z]) /
`t-evil-nearmiss-16k` (its first 16 KiB plus `!`), `t-trim-match-60k` (61,440 B
of mixed `\s`, ending in a space) / `t-trim-nearmiss-16k` (its first 16 KiB plus
`x`), `t-mixed-runs-4k` (4,096 B of interleaved short letter/digit/hex/decimal/
separator runs, ending in a letter -- the first non-pure-run subject here), and
`t-tail-{digits,txt,space}-1m` (~1 MiB of generated prose with digits, `name.ext`
mentions and 8-hex ids, one body, three different last lines). The tail truth
table (a match and a non-match per pattern) is in each manifest description.

**The expectation methods** are `docs/design/expectation_methods_v1.md`
(precedence: differential -> `structural-alphabet` -> `libpcre2-dfa-fallback`
-> dropped by name; the soundness argument for the structural rule is there).
Findings of this lane, stated here because they bound the set: the DFA is
itself ~n^2.8 on nested quantifiers (0.26 s at n=1000, 14 s at n=4000), so it
cannot answer the long near-misses; the structural rule can, because
`!` is not in `[a-z]` and `x` is not in `\s`. Result: the two short dropped
triples and the two long near-misses (`evil-alt-nested` x `t-evil-nearmiss-16k`,
`trim-nested-star` x `t-trim-nearmiss-16k`) carry method `structural-alphabet`;
the DFA fallback is declared and tested but, by precedence, restores nothing in
this set. Two triples stay DROPPED BY NAME (no required-literal rule this
revision): `email-nested-plus` x `t-evil-match-60k` and x `t-evil-nearmiss-16k`.
`.*\.txt$` over 1 MiB is NOT a give-up for the backtracker (0.02 s per
find-all), so the tail family is all `libpcre2-differential`.

**Predicted pcre2 cell cost, recorded not avoided.** `\s+$` against a long
whitespace run plus one non-space is QUADRATIC for the backtracker (the repeat
is auto-possessified, so it is slow rather than limited): MEASURED at the oracle,
1.83 s per find-all on `t-trim-nearmiss-16k` (25 s at the original 60 KiB, why
the near-misses were cut to 16 KiB); pcre2-interp and pcre2-jit cells for
`tail-space-eol` x `t-trim-nearmiss-16k` should be predicted at order seconds
per call, a real PCRE2 property (the CVE-2022-25927 shape). Other new triples
over 1 s per oracle call: `tail-ext-lower-txt` x `t-evil-match-60k` 1.7 s,
`letters-bounded-tail-z` x `t-evil-match-60k` 1.2 s, and `wild-waf-crs-942360-
concat-sqli` x `t-trim-match-60k` 1.7 s (an existing pattern on a new subject);
`wild-datetime-datefinder-alternation` x each `t-tail-*-1m` 6.8 s (existing
pattern, 1 MiB like `t-1m`).

### Predictions (stated before any run; scored by the window, not here)

- P11 (the matching tax). On `t-evil-match-60k` and `t-trim-match-60k` no engine
  gives up and every row is the whole-subject match / count 1; backtrackers take
  the first greedy path (linear). pcrec-auto at a pin >= 02db3811 ([NULLABLE-ANCH])
  is within 3x of pcre2-jit there.
- P12 (the near-miss split). On `t-evil-nearmiss-16k` and `t-trim-nearmiss-16k`
  pcre2-interp and pcre2-jit GIVE UP (match limit) -- their rows are `gave up`,
  not wrong -- while pcre2-dfa, the re2 rows, vectorscan and pcrec's DFA route
  answer `nomatch`. The two ReDoS patterns' triples HAVE expectations now (method
  `structural-alphabet`), so those cells are judged: a give-up is `gave up`, not
  wrong. Only `email-nested-plus` x the two evil subjects has none
  (`n_no_expectation`).
- P13 (design-quadratic). `tail-space-eol` x `t-trim-nearmiss-16k` (1.83 s per oracle call): pcre2-interp
  and pcre2-jit are >= 100x any linear engine (re2, vectorscan, pcrec DFA) on that
  cell, and the pcre2 per-call time is seconds, not microseconds.
- P14 (the end-anchored tails, I-136 item 2). `tail-*` x `t-tail-*-1m` agree with
  the truth table; for the five patterns the cross-engine spread is the
  reverse-/end-anchored-search story: engines that scan forward pay the megabyte,
  an engine that can anchor at the end pays the tail. No claim about which pcrec
  route is faster is made here (the pcrec manager owns that prediction).
- P15 (hex8). `hex8-bounded` finds counts 131 (`t-mixed-runs-4k`) and 264/263/263
  (the three tails), 0 on the four 60 KiB runs; a `\b` pair costs nothing on the
  pure-letter runs (no hex-only 8-run).
- P16 (bounded end-anchor, I-136 item 1). `letters-bounded-tail-z` costs a
  backtracker ~1024 steps per start offset on the 60 KiB letter runs (oracle:
  ~1.3 s per find-all, count 2: the 1024-byte tail and the empty match at the
  end) and almost nothing on `t-mixed-runs-4k` (short runs bound the per-start
  work): per byte, the pure-letter subjects cost >= 50x the mixed one.

### Outlier-rule additions

- R9. A cell at a 0.2 subject is compared across engines at 0.2 only; the 0.1
  cells are untouched and a cross-version delta is not a ranking.
- R10. A cell whose whole point is a backtracker's give-up or quadratic cost
  (the near-miss triples, `tail-space-eol` x `t-trim-nearmiss-16k`) is
  reported as that cell's finding, never as an outlier engine.
- R11. A throughput subject with a dropped (no-expectation) triple for a pattern
  excludes that pattern's cell at that subject's set-grain pass rate; the number
  of such triples is stated on the report (it is 2 by the derivation).

## capability@0.3 ([B123], 2026-10-25) -- the capture-forced-hybrid match subjects

Origin: pcrec inbox I-125 Q10 / I-127 [BENCH-ASKS-PENDING] (2) ("is there a
realistic-size match-regime subject, 1 KiB - 64 KiB, for the 17 capture-forced
hybrid patterns, or shall one be added?"; our answer in
`docs/dev/lanes/b121asks_report.md` Q10 was "none exists; adding one is a real
ask"). Frank cleared it 2026-10-25. The revision is in place, 0.1 -> 0.2 -> 0.3:
the 71 patterns, 75 short subjects, the eleven 0.1/0.2 throughput texts
(sha256s asserted) and every existing expectation row are byte-identical; six
subjects are APPENDED to the throughput manifest (fresh seeds
`0xC0FFEE31`..`0xC0FFEE36`, `captext.hyb_*`).

**Which regime, and why no `match` regime.** The set still declares no `match`
regime (capability_set_v1.md 3.5: the lexical `(?:pattern)\z` wrapper's three
defects). The "match-regime subject" pcrec asked for is read as a subject the
pattern MATCHES at realistic size, so it enters the THROUGHPUT regime
(find-all; every pattern x every throughput subject, as for 0.2's subjects).
For an anchored pattern the find-all count is 1 and the match IS the whole
subject (or its prefix) -- the same cell a whole-subject match regime would
time, at the same size.

**The 17, by the rule Q10 states** (`RX_VM_PREFILTER "hybrid"` AND
`RX_ENGINE_WHY` containing `"capture group"`; pcrec's own census file is
`docs/dev/optloop/capsurvey_census.tsv`, which this repo does not hold, so the
list is I-125's literal one): codegrammar-flat, codegrammar-xflag,
date-nested-plus, email-nested-plus, logparse-atomic, logparse-atomic-removed,
numeric-id-nested-plus, phone-list-nested-plus, wild-datetime-moment-iso8601,
wild-logparse-syslogbase-expanded, wild-secrets-aws-access-key-id,
wild-secrets-github-pat, wild-secrets-slack-webhook-url,
wild-secrets-username-password-pair, wild-semdiv-empty-alt-repeat-pcre2,
wild-validator-ipv4-owasp, wild-validator-us-zip-owasp. (Whether the list
still holds at pin 9ae59f5d4 is pcrec's census to re-run; this lane did not
compile.)

**The subjects, and which pattern each is the MATCHING subject of.**

| subject | bytes | seed | find-all MATCHES (count at the oracle) |
|---|---|---|---|
| `t-hyb-embed-1k` | 1,024 | 0xC0FFEE31 | the eight embedded patterns + `email-nested-plus` once at offset 0 |
| `t-hyb-embed-8k` | 8,192 | 0xC0FFEE32 | same nine |
| `t-hyb-embed-64k` | 65,536 | 0xC0FFEE33 | same nine |
| `t-hyb-logline-16k` | 16,384 | 0xC0FFEE34 | `logparse-atomic`, `logparse-atomic-removed`: the WHOLE subject, count 1 |
| `t-hyb-datepath-16k` | 16,384 | 0xC0FFEE35 | `date-nested-plus`: the whole subject, count 1 |
| `t-hyb-digits-4k` | 4,096 | 0xC0FFEE36 | `numeric-id-nested-plus`, `phone-list-nested-plus`: the whole subject, count 1 |

The embed ladder is one log/config/JSON grammar (the 0.1 background's four line
kinds plus six PLANTS: a JSON line, a syslog line, an AWS key id, a GitHub PAT,
a Slack webhook URL, a username/password pair) at three sizes. The first seven
lines carry one of each plant, so even the 1 KiB rung holds every instance;
afterwards one line in four is a plant. The oracle's counts at generation
(`captext.hyb_embed`, probed 2026-10-25): codegrammar 4 / 36 / 188, aws 1 / 13 /
75, github 2 / 8 / 64, slack 1 / 8 / 56, pair 1 / 7 / 62, syslog 1 / 7 / 58,
`(a|)*\d` 105 / 1,003 / 8,231 -- so the ladder is a SIZE ladder at a
fixed-ish match density, matches per KiB roughly constant from 8 KiB up (the
1 KiB rung is plant-heavy by construction). The unanchored `[^"\\]+` class of
codegrammar stays bounded because source lines keep a quote every few lines
(the 0.1 grammar's own reason). The `^`-anchored ReDoS patterns attempt offset 0
only, and the first run of their alphabet there is a few bytes long in every
subject by construction (`2025/`, `kern.err`, the address line, the first digit
group), so no new subject is a catastrophic near-miss for the family; the
generator's `_redos_safety_check` runs over all seventeen texts.

**Not covered, by design: 3 of the 17.** `wild-validator-ipv4-owasp`
(`^...$`, 7-15 B), `wild-validator-us-zip-owasp` (`^\d{5}(-\d{4})?$`, 5 or 10 B)
and `wild-datetime-moment-iso8601` (`^\s*DATE(TIME)?$`, ~30 B) have bounded
languages: no 1-64 KiB subject matches them as a whole, and the one place an
unbounded run exists (the leading `\s*`) is exactly the `^(\s+)*$` family's
catastrophic near-miss at length. They keep their search_short matches.
Adding a long pad would test the trim-nested pathology, not the hybrid's
second pass. Reported to pcrec as "14 of 17, and why".

**Prediction P17-P20 (stated before any run).**

- P17 (answers). Every new triple has a libpcre2-differential expectation (no
  fallback method is needed: the digits-4k x `email-nested-plus` triple is
  dismissed by PCRE2's required-code-unit '@' check in 0.0 s, measured through
  the oracle); every testee that answers agrees; R0 empty for the new subjects.
- P18 (the second pass, Q10 itself). For the 14 covered patterns on their
  matching subject, `pcrec-auto` (caps) / `pcrec-nocaps` is in 1.3-4x: the
  capture-assigning VM pass is a real share of a hybrid-exact artifact's time
  (pcrec's M-B measured it on the 5-93 B literals). On the three whole-subject
  shapes the ratio at 16 KiB is no lower than at 93 B: a longer whole match
  makes the VM pass LONGER, not cheaper per byte.
- P19 (size flatness). On the embed ladder, per-byte cost (ns/B) at 1 KiB is
  at most 3x the 64 KiB rung's for pcre2-jit and pcrec-auto (a fixed per-call
  share, plant-heavy rung), and the 8 KiB and 64 KiB rungs agree within 25%
  for the five secrets/JSON/syslog patterns (matches per KiB is constant
  there).
- P20 (nothing gives up). On the six new subjects no testee gives up on any
  pattern: pcre2-interp/jit take the first greedy path on the three
  whole-subject matches (linear, as on P11's subjects) and dismiss the
  `email-nested-plus` x digits triple by the required-code-unit check. A
  give-up here is a finding (an engine without the check), not an expected cell.

**Outlier-rule addition.** R12: a cell at a 0.3 subject is compared across
engines at 0.3 only; the 0.1/0.2 cells are untouched and a cross-version delta
is not a ranking.

**Cell time.** The 0.2 records give a per-subject floor of ~7 s of timed work
(t-mixed-runs-4k: 6.8 s on pcrec-auto, 8.2 s on pcre2-jit over ~345 rows) plus
~0.15 s per KiB; the six subjects (109 KiB) are ~42 s + ~16 s = **~1 minute of
timed work, ~2-3 minutes of wall per testee** on a ~47-49 minute cell (+5%).
No cell cap moves.

## capability@0.4 ([B172], 2026-10-30) -- the URL query-string subjects (pcrec I-172)

Stated BEFORE anything is measured (no engine timing was run for this section;
the only runs are the generator and the libpcre2 oracle).

**Why.** pcrec's reverse-landmark VM stage has `dup-param-detect`,
`\b(\w+)=[^&]*&(?:[^&]*&)*\1=`, as its only measured mover, and none of the
0.1-0.3 throughput texts contains an `&`, so the pattern only ever ran on one
short subject (`br-dup-param`, 11 B). 0.4 appends two throughput subjects
(`gen_throughput_subjects.qs_subjects`, `captext.qs_text`); no pattern, short
subject, 0.1-0.3 text or expectation row moves (the six `t-hyb-*` and eleven
earlier sha256s are asserted by the generator).

**The semantics the generator is built around.** `[^&]` matches the newline, so
`dup-param-detect` is LINE-BLIND: a key repeated on a later line is a duplicate
to it, and `(?:[^&]*&)*` is greedy, so a match runs from the first occurrence
of a key to the LAST `key=` in the subject. With a realistic vocabulary
(`id`, `page`, `utm_source` on most lines) the very first key would "duplicate"
the last line's and one match would swallow the file. So each key TEXT is
used at most once per subject: a stem's first use is the bare stem (`id`),
later uses carry a short base-36 tag (`id_k3f`, `utm_source_9qz`), the way
services mint custom parameters. The only repeated keys are the declared,
planted duplicates. This is a deliberate departure from "keys repeat across
lines", and it is the reason the duplicate share below is a property of the
subject and not of the vocabulary.

**The generator (seeded xorshift64*, fresh Rng per subject).**

- Lines: whole lines only, `k=v&k=v...`, no `?`, no trailing `&`; 2-10 params
  per line, one line in 300 a LONG line of 150-400 params.
- Key vocabulary: 30 stems, weighted (`id` 6; `page`, `q`, `filter` 4;
  `utm_source`/`utm_medium`/`utm_campaign`/`sort`/`ref`/`cat`/`tag`/`item` 3;
  `utm_term`, `utm_content`, `cb`, `fbclid`, `gclid`, `lat`, `lng` 1; the
  rest 2), then the tag rule above.
- Values: empty 8 %; decimal integer < 10^6 30 %; 8-32 hex chars 17 %; a plain
  word 25 %; two words joined by a percent-encoded byte (`%20 %2F %3A %2C %40
  %C3%A9 %E2%9C%93 %2B %3F %23`) 12 %; a percent-encoded e-mail (`name%40word.com`)
  8 %. No raw `&`, `=` or `?` in a value.
- Duplicates: a line plants one with probability 35,000 ppm (3.5 %). The
  planted key recurs exactly once, with a fresh value: on the SAME line 2-31
  params later (40 %), on the NEXT line (25 %), 2-40 lines later (30 %), or
  300-3,000 lines later (5 %, the FAR duplicates, tens to hundreds of KB
  apart). A duplicate scheduled past the end of the subject is dropped, so the
  realised share is a measured number, not the ppm.

**The two subjects.**

| subject | bytes | seed | what it is |
|---|---|---|---|
| `t-qs-1m` | 1,048,501 | 0xC0FFEE41 | the MATCHING subject: 7,799 lines, 52,936 params, 302 duplicate keys, 298 lines (3.8 %) carry a second occurrence, longest line 386 params |
| `t-qs-nearmiss-256k` | 262,092 | 0xC0FFEE42 | the NEAR-MISS: 1,628 lines, 13,206 params, ZERO duplicate keys; unique keys share prefixes/suffixes with earlier ones (`id`, `idx`, `ids`, `id_2`, `id_k3f`) |

**Why a near-miss pair, and why it is 256 KiB.** The set's convention is a
match/near-miss pair per hazard (`t-evil-match-60k`/`-nearmiss-16k`,
`t-trim-*`; twin patterns `winpath-near-miss`, `ipv4-near-miss`), and a
pattern's failing path is the cost the reverse stage targets: every start
(each `k=` is a candidate) scans `(?:[^&]*&)*` to the END of the subject and
backtracks through every `&` looking for `\1=`, so a failing subject costs
O(params x remaining params), QUADRATIC in size. At the oracle (one core),
256 KiB costs about 2.6 s, the matching 1 MiB subject about 14 s (the matches
swallow spans, which bounds the failing starts), so a 1 MiB near-miss would be
about 16x the 256 KiB one, ~40 s per find_all per trial per engine. The
near-miss is therefore a quarter-size and its cost is a finding to read, not a
cell cap to hit. R0 applies as ever: a testee that gives up or times out on it
is a finding.

**Predictions P21-P23 (stated before any run).**

- P21 (answers). Every new (pattern, subject) triple has a libpcre2-differential
  expectation (no fallback method needed unless a ReDoS-family pattern gives
  up; the `^`-anchored family attempts offset 0 only); every testee that
  answers agrees; R0 empty for the new subjects. `dup-param-detect` on
  `t-qs-nearmiss-256k`: `nomatch`, count 0, by construction (no key text occurs
  twice, and `\1=` needs the whole key).
- P22 (the stage's trigger). On `t-qs-1m` the `dup-param-detect` match count is
  in the low hundreds (the oracle's, recorded in b172qs_report.md), far below
  the 302 planted pairs because far and long-range spans swallow nearer ones;
  pcre2-interp/jit pay the most on the near-miss (quadratic failing starts),
  and any engine with a reverse landmark walk is expected to flatten that
  quadratic. This is the cell pcrec's I-172 asked for; the prediction
  about pcrec's own number is pcrec's to state.
- P23 (nothing else cares). The other 70 patterns on these two subjects are
  ordinary: the texts contain no `@`, no long uniform run in any ReDoS
  family's alphabet at offset 0 (the first bytes are a stem name and a value),
  so the `_redos_safety_check` over all 19 texts passes under its 2 s guard.

**Outlier-rule addition.** R13: a cell at a 0.4 subject is compared across
engines at 0.4 only; the 0.1-0.3 cells are untouched and a cross-version delta
is not a ranking.

**Cell time (estimate, not a measurement).** The oracle's one-core find_all
time for `dup-param-detect` is ~14 s (matching) and ~2.6 s (near-miss); an
engine that backtracks like libpcre2's interpreter pays that per trial, so the
two subjects add ~17 s of timed work per trial for the interpreter-class
testees (five trials: ~1.5 min) and well under that for JIT/DFA-class ones.
Other patterns on 1.3 MiB of text are ~0.15 s per KiB-class costs from the 0.2
records (~1-3 min of timed work per testee in total). The manager sets any
`CELL_CAP` change.
