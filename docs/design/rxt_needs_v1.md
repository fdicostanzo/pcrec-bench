# What the capability survey set needs from the `.rxt` format

**[B42], lane `b42rxtneeds`, 2026-09-12. This note is FEEDBACK TO pcrec
(`pcrecdev1`), not a design of this project's own.** It says, need by
need, what a capability survey set built ON `.rxt` requires; which
existing W1/W2/W3 production carries each need and whether that
production's designed semantics actually fit; where no production exists
at all; and what this project will VERIFY when pcrecdev1 delivers.

---

## 0. Purpose, the ruling, and how to read this

### 0.1 The ruling this note exists to serve

Frank ruled on 2026-09-12 (plan row `[B42]`, RULINGS Q3):

> **Q3 `.rxt` = THE SET IS A DRIVER OF THE FORMAT**: build on `.rxt` for
> real, not the hybrid; when the effort hits an `.rxt` capability
> roadblock it PARKS, this project sends pcrecdev1 DETAILED FEEDBACK on
> the needed capabilities (against `~/pcrec/docs/spec/rxt_format.md` +
> `dd13_format/`), pcrecdev1 builds them, the effort RESTARTS and this
> project REVIEWS and VERIFIES that work.

Frank's framing, quoted by the manager: *"This is as much a driver of the
rxt format as anything."*

Two consequences bind everything below.

1. **The hybrid is off the table.** `docs/dev/research/2026-09-12-b42-rxt-as-source.md`
   (N3) §6 recommended Option B — `.rxt` holds pattern text and identity,
   a sidecar holds the rest — and `docs/design/capability_set_v1.md` §9.1
   ADOPTED it. Frank's ruling supersedes both. This note is written for
   Option A: **the set's own truth lives in `.rxt`**, and where it cannot,
   that is a format need, not a sidecar workaround. Where a need could
   still be met in the sidecar for one release, the table says so in the
   `priority` column and §4 sequences it; that is a scheduling
   observation, not a reopening of the ruling.
2. **The roadblock is not a failure.** The set PARKS at each one. This
   note's job is to make the parked list complete and precise enough that
   pcrecdev1 can build against it without a second round of discovery.

### 0.2 What was read, and what was MEASURED

Read in full: `~/pcrec/docs/spec/rxt_format.md` (the as-built contract),
`~/pcrec/docs/spec/cli.md` §1 (`--source`/`--target`/`--lib-path`),
`~/pcrec/docs/design/dd13_format/requirements.md` §5 (R-BENCH-1..9),
`~/pcrec/docs/design/dd13_format/format_design.md` §§1.3, 1.4, 2.8-2.10,
4.5, 6.2 and §7's open questions, and `~/pcrec/src/parse/rxt_source.c`
where the spec was silent. On this side: `docs/design/capability_set_v1.md`
v0.1 (§3-§6, §9, §12), the three R5 critic files, `docs/design/
subbench_directory_model.md` ([B29]), `pcrecbench/subbench.py`,
`tools/export_rxt.py`, `bench/syntax/subbench.toml`,
`bench/altwide/subbench.toml`, `schema/record.schema.json`.

**Eleven facts in this note were MEASURED against the pinned binary**
(`build/pcrec-d34c9131/build/pcrec --list-source`, pin d34c9131, abi 23 —
parse-only, no compile, nothing built) rather than inferred from the
spec. They are marked **MEASURED** where they appear, and §1.9 collects
them. Two of them contradict a claim a committed document in this repo
makes today (§1.9 items M2 and M11).

### 0.3 Relationship to R-BENCH-1..9

`~/pcrec/docs/design/dd13_format/requirements.md:316-411` states this
project's needs as R-BENCH-1..9, evidenced from APPROACH.md and Frank's
inputs. Every one of the nine is answered TODAY by a sidecar field
(`subbench_directory_model.md:127-140`). This note's relationship to them:

| id | the original ask (`requirements.md:<line>`) | this note |
|---|---|---|
| R-BENCH-1 | per-case feature tier, hazard class, size class, VERIFICATION METHOD (`:321-340`) | **CONFIRMS and EXTENDS.** The four fields fold into `tag` (W2) as `format_design.md:1825-1908` §4.5 already works out. The EXTENSION is that a capability set needs three more per-case field families the ask did not anticipate: PROVENANCE (§1.3, nine fields), REQUIRES capability tags with a CLOSED, validated vocabulary (§1.4), and `role` (§1.2 N-9). The verification-method half is confirmed as needed and found **INSUFFICIENT as specified**: `tag method=<name>` carries the method's NAME but not the oracle's VERSION, which a cross-engine correctness claim needs (§1.6 N-22) |
| R-BENCH-2 | a section keyed per TESTEE: what to include, which options (`:341-350`) | **CONFIRMS**, and finds one hazard the ask did not: D93 makes a `config` in a set file BEAT the command line, and this repo's whole testee matrix is command-line flags. A set that carries a testee roster needs a stated SCOPING rule (§1.7 N-29) |
| R-BENCH-3 | first-class "unsupported by this testee", counted, never silent (`:351-359`) | **CONFIRMS.** W3's `variant <testee> unsupported <reason>` is the right shape. EXTENDED: the capability set decides `unsupported` from a DECLARATION (`capability_set_v1.md` §5.3) rather than per-pattern-per-testee by hand, so the format needs to carry the REQUIRES tag the declaration reads (§1.4), not only the per-pair refusal |
| R-BENCH-4 | expectations strong enough to adjudicate correctness, NOT pcrec-shaped (`:360-367`) | **CONFIRMS**, and finds the sharpest gap in this note: expectations today are TESTEE-BLIND, one row per (pattern, subject, regime), and a POSIX-leftmost-longest engine's different-but-correct answer has nowhere to live (§1.6 N-12 — R5 finding B1's format half) |
| R-BENCH-5 | a per-CASE matching-convention tag (`:368-374`) | **CONFIRMS as necessary and INSUFFICIENT.** A convention TAG says which convention an expectation follows. It does not supply the SECOND expectation an engine with another convention is scored against. The tag without the alternate answer is unusable (§1.6 N-11, N-12) |
| R-BENCH-6 | subjects by REFERENCE, not inline (`:375-384`) | **CONFIRMS.** W2's `@file:` is the production. EXTENDED with two asks: an integrity hash on the reference (§1.5 N-14) and a statement of NUL-safety on the reference path (§1.5 N-15) |
| R-BENCH-7 | per-library pattern tweaks DECLARED, impossible to miss (`:385-393`) | **CONFIRMS.** W3's `variant` is the production. EXTENDED: `variant_kind`, `objective_preserved` and `capture_map` are three separate fields the sidecar carries today and `variant`'s designed body carries only two of (§1.7 N-27) |
| R-BENCH-8 | import from pcrec's own oracle-verified `.rxt` corpora (`:394-400`) | **CORRECTED.** `subbench_directory_model.md:554-560` Q4 states the import direction is lossless because "`foo_bar` is a legal slug". **It is not** — the record schema's slug rule forbids `_` (§1.9 M11). Every pcrec block name that is a C identifier with an underscore is an ILLEGAL bench `pattern_id` today. This is this project's problem to solve, not pcrec's, but the format note should not carry the wrong claim forward |
| R-BENCH-9 | the same section concept serves pcrec's own multi-config builds (`:401-411`) | **UNTOUCHED.** Nothing this set needs bears on it |

Two needs in §1 have no R-BENCH ancestor at all and are new with this
set: **per-pattern provenance** (§1.3) and **the capability/REQUIRES
model** (§1.4). Both come from Frank's `[B42]` charter items (1) and the
capability clause, which postdate DD-13a by two and a half weeks.

### 0.4 How to read §1's table

Seven columns, one row per need:

- **need** — stated precisely enough to check.
- **today** — where it lives in this project now, cited `file:line`.
- **production** — the EXISTING `.rxt` production that would carry it,
  spelled exactly as `format_design.md` §1.3 spells it, or **NEW** where
  none does.
- **fits?** — whether that production's DESIGNED semantics actually serve
  the need. `yes` / `partial (<what is missing>)` / `no`.
- **wave / status at d34c9131** — `BUILT`, `REFUSED BY NAME` (designed,
  in a later wave, refused as NOT IN THIS BUILD — `rxt_format.md:57-62`),
  or `ABSENT` (no production in any wave).
- **priority** — `MUST` (the set cannot ship a first sample without it),
  `SHOULD` (the set ships but a stated capability is missing), `COULD`.

Where `format_design.md`'s intent is ambiguous the row says so in the
`fits?` cell rather than resolving it; §5 collects those as questions for
pcrecdev1.

---

## 1. THE NEED TABLE

Fifty needs in eight blocks, numbered N-1..N-53 (three rows — N-29,
N-51, N-53 — are recorded for completeness and ask the format for
nothing). Counts by priority: **36 MUST** (one of them conditional on
N-42 landing), **9 SHOULD**, **5 COULD**. Counts by status at the pin:
**14 BUILT**, **2 BUILT AND LOSSY**, **20 REFUSED BY NAME** (designed, a
later wave), **15 ABSENT** (no production in any wave).

The MUST count is high because Frank's ruling makes it so: under the
hybrid, everything in blocks C through H could have stayed in a sidecar
and been a SHOULD. Built on the format for real, a set cannot express its
own patterns' provenance, tags, subjects or expectations without W2 and
W3, so those become MUSTs by the ruling rather than by this note's
judgment. §4 separates what blocks a FIRST SAMPLE from what blocks the
set's full claims.

### 1.1 Block A — pattern text

| # | need | today | production | fits? | wave / status | pri |
|---|---|---|---|---|---|---|
| **N-1** | one-line pattern text, raw bytes, no escaping | `patterns/<id>.rx`, read raw (`pcrecbench/subbench.py:242-246`) | `pattern` , ws , rest-of-line (`format_design.md:397`; `rxt_format.md:210-212`) | **yes** — MEASURED byte-exact for ASCII, tab, backslash, mid-line CR (§1.9 M4) | W1, **BUILT** | MUST |
| **N-2** | a pattern with a LITERAL NEWLINE — a `(?x)` free-spacing body authored across lines, which family 6's VS Code `number` rule is in its source (`capability_set_v1.md:183`, N1 §18) | not exercised: no `.rx` file contains a newline (`subbench_directory_model.md:69-70`) | **NEW** — `pattern` is one line with no continuation and no escaping, so a newline has NO representation at all | **no** | **ABSENT** | **MUST** |
| **N-3** | raw high bytes (non-UTF-8) in pattern text — family 12 (`capability_set_v1.md:189`) | `.rx` files are raw bytes, never decoded (`subbench.py:242-246`) | `pattern` rest-of-line | **yes** — MEASURED byte-exact through `--list-source` (§1.9 M3) | W1, **BUILT** | MUST |
| **N-4** | a literal NUL byte in pattern text | not exercised | `pattern` rest-of-line | **no — SILENTLY TRUNCATED.** MEASURED: `pattern ab<NUL>cd` dumps as `ab`, exit 0, no diagnostic (§1.9 M1). The parser slurps the file and splits it into NUL-TERMINATED C strings (`~/pcrec/src/parse/rxt_source.c:437-456`), so every rest-of-line value ends at the first NUL | W1, **BUILT AND LOSSY** | SHOULD |
| **N-5** | a pattern whose last byte is a CR | not exercised | `pattern` rest-of-line | **no — SILENTLY TRIMMED.** MEASURED (§1.9 M2): `\r\n` is trimmed to `\n` unconditionally (`rxt_source.c:450`), which is right for a Windows-edited file and wrong for a pattern that ends in CR. A CR anywhere ELSE in the line survives exactly | W1, **BUILT AND LOSSY** | COULD |
| **N-6** | a pattern larger than a comfortable line | `canonical_text` capped at 1 MiB by the RECORD, not by `.rxt` (`docs/design/record_schema.md` §4, KB-7) | `pattern` rest-of-line | **yes** — MEASURED: a 20,000-byte pattern line parses (§1.9 M9). `.rxt` imposes no line-length bound | W1, **BUILT** | COULD |

**Why N-2 is MUST and not SHOULD.** The charter's requirement (1) is
patterns from the wild. Free-spacing `(?x)` bodies authored across lines
are how real editor grammars, CRS rules and validators are actually
written; flattening one to a single line is a `fidelity: adapted` edit
whose correctness has to be proved by an oracle run
(`capability_set_v1.md:1089-1100`). Under Frank's Q3 ruling the set is
built on the format for real, so "flatten it because the format cannot
hold it" is exactly the kind of accommodation the ruling removes. **This
is roadblock #1.** MEASURED, the failure is at least LOUD: an indented
continuation line is refused by name ("a pattern block's lines are NOT
indented", §1.9 M8), not silently swallowed.

### 1.2 Block B — pattern identity and descriptive metadata

| # | need | today | production | fits? | wave / status | pri |
|---|---|---|---|---|---|---|
| **N-7** | a pattern id that is the RECORD's `pattern_id` with no second naming | `[[patterns]].name`, checked against the record schema's slug rule at load (`subbench.py:80-90, 161-162`) | `name` , ws , ident, widened to "a first byte that is a letter or `_`, then letters, digits, `_`, `-` or `.`" (`rxt_format.md:278-282`), unique in the file namespace | **yes.** The grammar was widened FOR this project (`rxt_format.md:290-296`). MEASURED: `crs-942.160` and `Upper.Name-1` both accepted; a duplicate name is refused by name (§1.9 M6, M7). The bench's slug rule is STRICTER (no `_`, no `.`, no uppercase) so every legal bench id is a legal `.rxt` name — the containment runs one way only, which matters for import (§1.9 M11) | W1, **BUILT** | MUST |
| **N-8** | a one-line human description per pattern | `[[patterns]]`'s TOML comment, not a field (`bench/syntax/subbench.toml:70`) | `description` , ws , rest-of-line, block-scoped, ONE-LINE ONLY (`rxt_format.md:297-298`; the W1.1 correction, `format_design.md:434-448`) | **partial.** One line is enough for a description. Two hazards: a SECOND `description` in one block SILENTLY OVERWRITES the first, last wins, no diagnostic (MEASURED, §1.9 M5); and the one-line rule means a provenance/adaptation sentence cannot live here (which is why §1.3 asks for fields, not prose) | W1, **BUILT** | MUST |
| **N-9** | per-pattern classification: `family`, `role` (`member`/`floor`), `hazard_class`, `size_class`, `feature_tier` | `[[patterns]]` five fields (`bench/syntax/subbench.toml:72-79`); `role` is `record_schema.md` §5 v1.3 | `tag` , ws , tag-item , { ws , tag-item } — repeatable, accumulating, bare labels and `k=v` pairs on one line (`format_design.md:420`, the U1 ruling at `:1843`) | **yes.** `format_design.md:1825-1908` §4.5 already maps all five. The bench's own vocabularies stay the bench's (AR-6) | W2, **REFUSED BY NAME** (MEASURED, §1.9 M10) | **MUST** |
| **N-10** | `hazard_class` is the field §6.3's whole rewrite rule keys on, and it must be a CLOSED set the format can refuse a typo in | closed enum in the record schema (`schema/record.schema.json:298`; `record_schema.md:381`) | `tag hazard=<label>` | **partial — no vocabulary declaration.** `tag-value` is free vocabulary by design (`format_design.md:341-343`; the AR-6 argument at `:1229`). A typo (`hazard=exponential-backtraking`) is a legal tag. R5 finding B3 makes the identical point about `patterns[].tags` on this side | W2, **REFUSED BY NAME** | **MUST** |

**Roadblock #2 is N-9 plus N-10 together.** `tag` is the production that
carries essentially every descriptive field the set has, and it is
refused by name at the pin. Its *shape* fits; what is missing is a way to
DECLARE a closed vocabulary and have the parser refuse a value outside
it. §2.2 proposes one.

### 1.3 Block C — per-pattern PROVENANCE (no production exists in any wave)

The charter's requirement (1): "provenance recorded per pattern".
`capability_set_v1.md:311-339` §4.1 fixes a CLOSED nine-field record, and
Frank's Q1 ruling adds a tenth obligation (an `inspired` pattern is
validated as not an actual copy of its source). N3 §1.3 establishes that
**no pattern-level provenance production exists in any wave** — the
`freq` data block has required provenance fields (`exemplar`, `bytes`,
`sha256`, `analyzer`, `date`; `format_design.md:1276-1288`) but that
family exists for exemplar-analysis findings, not for a pattern's origin.

| # | need | today | production | fits? | wave / status | pri |
|---|---|---|---|---|---|---|
| **N-11** | `source_name` — a registered source slug | — | **NEW** | no | **ABSENT** | MUST |
| **N-12** | `source_url` — the exact URL fetched | — | **NEW** | no | **ABSENT** | MUST |
| **N-13** | `source_ref` — file/rule/line inside the source (`rules/REQUEST-942-…conf#942160`) | — | **NEW** | no | **ABSENT** | MUST |
| **N-14** | `licence` — an SPDX id from the source's own LICENSE, fetched | — | **NEW** | no | **ABSENT** | MUST |
| **N-15** | `licence_note` — where a source's own licence metadata disagrees with itself (the Davis Zenodo/GitHub mismatch, `capability_set_v1.md:464-466`) | — | **NEW** | no | **ABSENT** | SHOULD |
| **N-16** | `retrieved_utc` — RFC 3339, the date of the fetch that produced THIS text | — | **NEW** | no | **ABSENT** | MUST |
| **N-17** | `fidelity` — `verbatim` / `adapted` / `inspired`, a CLOSED three-value set | — | **NEW** | no | **ABSENT** | MUST |
| **N-18** | `adaptation` — one checkable sentence, required when `fidelity ≠ verbatim` | — | **NEW** | no | **ABSENT** | MUST |
| **N-19** | `attribution` — required where the licence demands it (CC BY-SA 4.0) | — | **NEW** | no | **ABSENT** | MUST |

**Why prose in `description` is not an answer.** It is the answer the
format offers today (W1, BUILT) and `capability_set_v1.md:340-346`
already rejects it: a reviewer checking sixty attributions against sixty
prose sentences is the failure mode a derived, checkable table exists to
close. Three further reasons specific to the format: a block's
`description` is ONE LINE (`rxt_format.md:297-298`), nine fields do not
fit in one line; a second `description` silently overwrites the first
(§1.9 M5), so a two-line workaround loses data without saying so; and
conditional REQUIREDNESS (`adaptation` iff `fidelity ≠ verbatim`) is the
kind of rule the format already knows how to enforce structurally — the
`freq` block's `question`/`reader` lines are required and a block without
them is refused (`format_design.md:1251-1258`), which is the precedent
§2.1 builds on.

**Roadblock #3.** Nine fields, no production, and requirement (1) is the
charter's first item.

### 1.4 Block D — the capability model (REQUIRES, and the closed vocabulary)

The charter's standing clause: every pattern carries what an engine must
support to run it, and an engine that cannot is a recorded `unsupported`
outcome, never an error. `capability_set_v1.md:497-531` §5.1 fixes a
sixteen-tag vocabulary (fifteen in the table plus `true-end-anchor` added
at `:739`).

| # | need | today | production | fits? | wave / status | pri |
|---|---|---|---|---|---|---|
| **N-20** | per-pattern REQUIRES tags (`backrefs`, `lookaround`, `lookbehind-variable`, `atomic-possessive`, `recursion`, `conditionals`, `k-reset`, `control-verbs`, `unicode-properties`, `named-groups`, `free-spacing`, `callouts`, `span-reporting`, `non-utf8-subject`, `captures`, `true-end-anchor`) | nothing — this set is the first to need it; `[[patterns]].tags` is the nearest thing and is DIAGNOSTIC, not filterable (`record_schema.md:1025`, R5 B3) | `tag requires=<label>` (W2), by the same generic mechanism as N-9 | **partial.** The carrier fits. What does NOT fit is the CLOSED-SET requirement: `capability_set_v1.md:521-525` states "the vocabulary is CLOSED and validated at set load. A tag outside it is a load error naming the closed set", and `tag`'s value space is deliberately free | W2, **REFUSED BY NAME** | **MUST** |
| **N-21** | a DECLARATION of the closed vocabulary, in the file, that the parser enforces | — | **NEW** | no | **ABSENT** | **MUST** |
| **N-22** | per-CONFIG capability declarations — which tags a given (engine, version, config) SATISFIES; `pcre2-dfa` and `pcre2-interp` are one library at one version with different tag sets (`capability_set_v1.md:532-552`) | `testees/<engine>/configs.toml` would gain a `capabilities = [...]` key (proposed, unbuilt) | `config <name>` body + `testee`/`option` (W3) — the section concept R-BENCH-2/9 names | **partial.** W3's `config` body has `testee engine-ref` and `option tag-pair` (`format_design.md:376-377`) and nothing that says what an engine CAN do. `option capability=backrefs` would work syntactically and would be an abuse: `option` is "that engine's options" (`:377`), a build/runtime setting, not a capability claim | W3, **REFUSED BY NAME** | SHOULD |
| **N-23** | the pre-compile policy `REQUIRES(pattern) ⊄ capabilities(config) ⇒ unsupported-by-declaration` decided BEFORE any compile (`capability_set_v1.md:554-585`) | nothing emits that outcome today (R5 B7: it is schema-legal and has never been produced) | consumes N-20 + N-22; the OUTCOME is W3's `variant <testee> unsupported <reason>` | **yes once N-20/N-22 exist** — the outcome production is right; R-BENCH-3 and AR-3 already rule it (`format_design.md:2044`) | W3, **REFUSED BY NAME** | SHOULD |

**Note on where the capability declaration belongs.** It is genuinely
arguable that per-CONFIG capabilities are the bench's business and not
the format's: they describe an ENGINE, not a set. This note asks for them
in the format anyway, for one reason: `format_design.md`'s own §4.5 puts
`[testees.<id>]`'s whole content into `config` blocks with `testee`
lines, and a capability list is the one field of that section a reader of
the FILE needs in order to understand why a pattern has no result for a
testee. If pcrecdev1 prefers to leave it bench-side, that is a legitimate
answer and §5 Q4 asks it directly — but then the format owes nothing and
this project keeps a second file, which is the hybrid Frank's ruling
removed.

### 1.5 Block E — subjects

| # | need | today | production | fits? | wave / status | pri |
|---|---|---|---|---|---|---|
| **N-24** | small typed subjects inline | generated `subjects/<id>.bin` + `manifest.tsv` (`subbench.py:184-213`) | `quoted-subject` with the seven-escape vocabulary (`rxt_format.md:374-385`) | **yes** for short ASCII-ish subjects | W1, **BUILT** | MUST |
| **N-25** | LARGE subjects by reference — 64 KB to 1 MB throughput runs (`capability_set_v1.md:216-244`) | `throughput/` tree + `manifest_throughput.tsv` | `@file:"path"` (`format_design.md:325`, semantics at `:1183-1208`) | **yes** — local spelling only, relative to the naming file, the file's bytes ARE the subject, NUL-safe, no size limit | W2, **REFUSED BY NAME** | **MUST** |
| **N-26** | an INTEGRITY HASH on a subject reference — every subject this project measures carries a committed sha256 and `make check` re-derives it byte for byte (`subbench.py:184-213`; the generic manifest gate, `tools/CLAUDE.md`) | `manifest.tsv` columns `id len sha256 description [periodic]` | `@file:` | **no — DECLINED BY DESIGN.** `format_design.md:1205-1208`: "No content hash on a subject reference. ARGUED... provenance is required exactly where the source is not committed." The reasoning is sound for pcrec's corpus and does not transfer: our subject trees are GITIGNORED and regenerated (`subbench.py:37-40`), so a `.rxt` reference points at a file that is NOT committed and NOT reviewed. §2.5 asks for an optional hash, not a mandatory one | W2, **REFUSED BY NAME**, and the extension is **ABSENT** | **MUST** |
| **N-27** | subject METADATA — a stable subject id, byte length, a description, the `periodic` column ([B17]) | `manifest.tsv` | **NEW** — `@file:` carries a path and nothing else; there is no subject id at all, and a case's identity is `file:line` (`format_design.md:2279-2284`) | **no.** Every expectation key in this project is `(pattern, subject_id, regime)` (`subbench.py:268-271`); every report row and every interpreter fact names a subject by id. `file:line` is not a substitute — it moves when a line is inserted | **ABSENT** | **MUST** |
| **N-28** | subjects that are not valid UTF-8, and subjects containing NUL — family 12 (`capability_set_v1.md:189`) | raw bytes throughout | `@file:` | **yes, as designed** — `format_design.md:1195-1199` states file-subject bytes are taken raw, NUL-safe, no decoding. **UNVERIFIED at the pin** (the production is refused, so nothing could be measured). An INLINE quoted subject carries `\xHH` and so can express a high byte but the driver protocol passes subjects as `argv` strings, which "can carry neither a NUL nor a megabyte" (`:1200-1204`) | W2, **REFUSED BY NAME** | MUST |
| **N-29** | a SET-LOCAL generator beside its output, with the manifest re-derivable | `gen_subjects.py` + `gen_throughput_subjects.py` per set, gated by `make check-harness` | "the directory convention" (`format_design.md:1846`) — an explicit non-production | **yes, as a convention.** Nothing is asked of the format here; recorded so the list is complete | n/a | n/a |

### 1.6 Block F — expectations, conventions, and the oracle

This block contains the need this note is least able to route to an
existing production, and the one R5 finding B1 identified independently
on the harness side.

| # | need | today | production | fits? | wave / status | pri |
|---|---|---|---|---|---|---|
| **N-30** | match / no-match with a byte span, per (pattern, subject, regime) | `expectations.tsv`, 9 columns (`subbench.py:124-138`) | `m` , ws , subject , ws , int , ws , int / `n` , ws , subject (`rxt_format.md:230-233`) | **yes** | W1, **BUILT** | MUST |
| **N-31** | a match from an explicit start position | not used by this project today | `ms` / `ns` (`rxt_format.md:234-237`) | yes | W1, **BUILT** | COULD |
| **N-32** | a FIND-ALL count over a subject (the throughput regime's `nmatches`) | `expectations.tsv`'s `nmatches` column | `mc` , ws , subject , ws , int (`format_design.md:419`) | **partial — the non-overlap rule is unstated.** This project's driver protocol fixes `pos = max(end, pos+1)` (`pcrecbench/adapters.py:20-22`). `mc`'s designed semantics are one integer beside a subject; whether it counts non-overlapping matches under the same rule is not stated anywhere I could find. Two engines counting differently would both "pass" | W2, **REFUSED BY NAME** | **MUST** |
| **N-33** | CAPTURE spans per case | not carried — `expectations.tsv` has no capture columns at all (MEASURED by pcrec, `format_design.md:1979`, and still true) | `g` / `gp` , ws , slot , ws , span (`rxt_format.md:239-267`) | **partial and pcrec-shaped.** `g` is scored against the artifact's own `RX_NCAPS` and `gp` has a pcrec-specific `pending-vm` bucket. T-3 flags exactly this (`format_design.md:2033`); the engine-neutral resolution is `variant … groups <name>=<n>` (W3). Not needed for v1 (this project's OD-B9 is unopened) but it is where capture checking would land | W1 (`g`/`gp`), **BUILT**; the neutral half W3, **REFUSED** | COULD |
| **N-34** | the MATCHING CONVENTION an expectation follows, per case — `perl-leftmost-first` / `posix-leftmost-longest` / `all-ends` | `[[patterns]].convention` (`bench/syntax/subbench.toml:76`), carried into the record's `testee.conventions` and never read by anything (R5 B1, B7) | `tag convention=<label>` (W2), as `format_design.md:1845` maps it | **yes as a TAG** | W2, **REFUSED BY NAME** | MUST |
| **N-35** | an expectation under a NON-canonical convention — the SECOND correct answer a `posix-leftmost-longest` engine gives to `a\|ab` on `"ab"` | **nothing.** `Subbench.expectation()` is keyed `(pattern, subject_id, regime)` with no testee axis (`subbench.py:268-271`); `harness.outcome_for()` has no convention parameter (R5 B1) | **NEW.** `m`/`n` carry no qualifier; `variant` supplies different pattern TEXT for a testee, never a different expected ANSWER for the same text | **no** | **ABSENT** | **MUST** |
| **N-36** | which ENGINE checked an expectation | `[expectations].default_method` conflates it with the method | `oracle` , ws , ( `python` \| `pcre2` \| `none` <reason> ), file-level or block-scoped, block wins (`format_design.md:1209-1241`) | **partial — a closed engine enum of two.** The set's roster is pcre2, RE2, Rust `regex`, Oniguruma, TRE, Vectorscan, python, perl (`capability_set_v1.md` §8). `oracle` admits `python` and `pcre2` and nothing else. A set whose family 11 needs a POSIX engine as ITS oracle cannot name one | W3, **REFUSED BY NAME** | **MUST** |
| **N-37** | the verification METHOD, per case — R-BENCH-1's own ask, including non-oracle methods | `[expectations].default_method = "libpcre2-differential"` | `tag method=<name>` — pcrec's own ruling that method and engine are TWO fields (`format_design.md:1850`, r44-consumers U3) | **yes** | W2, **REFUSED BY NAME** | MUST |
| **N-38** | the oracle's VERSION — "checked against libpcre2 **10.46**" | implicit: `pcrecbench/oracle_pcre2.py` binds whatever the box has; the record carries the engine version of the TESTEE, not of the oracle | **NEW.** `oracle pcre2` names an engine with no version slot; `engine-ref = ident , [ "/" , version-chars ]` exists but only for `testee` (`format_design.md:381`) | **no** | **ABSENT** | SHOULD |

**Roadblock #4, and it is the deepest one: N-35.** The set's family 11
(`semantics-divergence`, six members, v1) exists to measure engines that
answer DIFFERENTLY AND CORRECTLY. R5 finding B1 establishes that this
project's harness cannot score that today. This note adds the format
half: **`.rxt` cannot express it either.** A case line is one expected
answer for one (pattern, subject); `variant` changes the TEXT for a
testee, not the ANSWER. Whatever pcrecdev1 builds, the format needs a way
to say "under `posix-leftmost-longest` the answer to this case is
`0 2`, and a testee tagged with that convention is scored against it."
§2.4 sketches one.

### 1.7 Block G — per-testee variants and the testee roster

| # | need | today | production | fits? | wave / status | pri |
|---|---|---|---|---|---|---|
| **N-39** | a per-engine SPELLING variant of a pattern, declared beside it and impossible to miss | `[testees.<id>].variant` (`harness_contract.md:41-55`, quoted at `subbench_directory_model.md:85-86`) | `variant` , ws , ident , ws , rest-of-line (`format_design.md:422-424`) | **yes** for the text | W3, **REFUSED BY NAME** (MEASURED, §1.9 M10) | MUST |
| **N-40** | a per-engine DECLARED REFUSAL with a reason | `[testees.<id>].unsupported` | `variant <testee> unsupported <reason>` (`format_design.md:423`) | **yes** — one line kind for both halves of the axis, which `format_design.md:1875-1878` explicitly designed | W3, **REFUSED BY NAME** | MUST |
| **N-41** | `variant_kind` (`syntax-only` / `restructured`), `objective_preserved` (a reviewed statement), `capture_map` | three separate sidecar fields (`record_schema.md:1026-1038`) | `variant`'s body carries text and an optional `groups <name>=<n>` map (`format_design.md:423-424`); `objective_preserved` is `tag variant-note=…` (`format_design.md:1879-1883`) | **partial.** `capture_map` ↔ `groups` fits. `variant_kind` has NO carrier — it is a closed two-value enum this project's reporter is meant to show beside a number (`requirements.md §4.5`, and R5 B2 finds the reporter never implemented it). `tag variant-note=` carries prose but a `tag-value` may contain **no whitespace** (`format_design.md:342`), so a reviewer's sentence does not fit in one | W3 + W2, **REFUSED BY NAME**; `variant_kind` **ABSENT** | SHOULD |
| **N-42** | a testee ROSTER for NON-pcrec engines, with per-engine options | `[testees.<id>].options` (empty on every set today) | `config <name>` with `testee engine-ref` + `option tag-pair` lines, enumerated by a head `use config-list` (`format_design.md:376-377`, `:359`) | **yes in shape**, with the D93 hazard below | W3, **REFUSED BY NAME** | SHOULD |
| **N-43** | **a set file that declares NO pcrec `target` and NO pcrec `config`, legally and PERMANENTLY** | n/a — the exporter already writes such files (`tools/export_rxt.py:34-37` rule 5) | the absence of `target`/`config`; "No `target` and anything else builds NOTHING… It is not an error" (`rxt_format.md:126-127`) | **yes today** — MEASURED: an authored head-plus-blocks file with no `target` and no `config` parses and dumps cleanly (§1.9 M12). What is missing is a CONTRACT that this stays true | W1, **BUILT**; the guarantee **ABSENT** | **MUST** |
| **N-44** | a scoping rule so a set's own config can never pin this project's testee matrix | the exporter's rule 5 — never write `config`/`flags`/`engine`/`budget`/`encoding` (`tools/export_rxt.py:34-37`) | **NEW.** D93: "a `.rxt` source's composed config wins over a command-line flag on the same axis" (`subbench_directory_model.md:441-448`), and `engine` composes more-specific-wins (`rxt_format.md:133-136`) | **no.** The moment a set carries a `config … testee re2/2024-07-02` block (N-42) the file has configs, and a reader has no way to know that the `pcrec` half of those configs must never reach a build. §2.6 asks for the separation | **ABSENT** | **MUST if N-42 lands** |

**Roadblock #5 is the D93 interaction.** `format_design.md:2198-2284`
§6.2's worked bench file carries `config pcrec` / `config pcre2` /
`config re2` and a `use` line naming all three. Under D93 the `config
pcrec` block in a file this project treats as its corpus WINS over the
adapter's command line, and this project's entire sixteen-config pcrec
testee matrix is command-line flags (`testees/pcrec/configs.toml`). The
worked example and D93 are both right on their own and collide when the
file is a bench set. This is a DESIGN question for pcrecdev1, not a bug.

### 1.8 Block H — set-level identity, composition, and tooling

| # | need | today | production | fits? | wave / status | pri |
|---|---|---|---|---|---|---|
| **N-45** | set `id` and `version` — the frozen snapshot records compare within (`docs/design/requirements.md §5`) | `subbench.toml`'s `id`/`version` (`bench/syntax/subbench.toml:5-6`) | `tag id=capability version=0.1` file-level (`format_design.md:1837`) | **yes**, with N-10's caveat (free vocabulary; a typo in `version` is a legal tag) | W2, **REFUSED BY NAME** | MUST |
| **N-46** | set `objective` + `objective_kind` + `description` — multi-paragraph prose | `subbench.toml` (`bench/syntax/subbench.toml:7-49`) | head `description` with the `|` BLOCK SCALAR (`rxt_format.md:196-203`), plus `tag objective=<kind>` | **yes** — MEASURED: a head block scalar parses and dumps with `\n` escapes preserved (§1.9 M12) | W1, **BUILT** (the `tag` half W2) | MUST |
| **N-47** | the BLINDING / authorship statement — which discipline the author worked under (pcrec D27; `bench/syntax/NOTES.md`) | `NOTES.md` prose | head `description` block scalar, or `tag` | **yes as prose**; there is no structured carrier and this note does not ask for one | W1, **BUILT** | COULD |
| **N-48** | which REGIMES the set exercises, and per-pattern regime membership | `regimes = [...]` (`bench/syntax/subbench.toml:54`); every pattern runs every declared regime (`subbench.py:154-157, 258-266`) | `tag regime=search_short throughput` file-level, refined per block; and for a per-regime SUBJECT SET, `format_design.md:1884-1897` §4.5 item 4's mechanism: name the canonical pattern once as a definition and write one block per regime whose pattern is `(?&<name>)` | **NO for the per-regime mechanism, on this project's ids.** A definition whose name carries `-` or `.` **cannot be called from a pattern** — `(?&cls-upto-1024)` goes through PCRE2's own group-name grammar and is refused there (`rxt_format.md:284-291`). EVERY pattern id in this repo's five sets is a hyphenated slug. §4.5's own regime mechanism is therefore unusable for this project unless ids are renamed to identifiers — which re-introduces exactly the name map the widened grammar was created to abolish (`rxt_format.md:290-296`) | `tag` W2, **REFUSED**; the wrapper mechanism **BROKEN for our ids** | **MUST** |
| **N-49** | the regime → subject-set mapping, and `short_search_max_bytes` | `subbench.py:258-266`; `[subjects].short_search_max_bytes` | `tag short-search-max-bytes=256` (`format_design.md:1848`) | **partial.** The tag carries the number. The MAPPING (which subjects a regime sees) is harness semantics that `format_design.md` §4.5 resolves by giving each regime block its own subject list — which is N-48's broken mechanism | W2, **REFUSED**; the mapping **ABSENT** | SHOULD |
| **N-50** | a shared SUBJECT VOCABULARY across sets, or across a set's own fragments | not needed today; each set generates its own | `include` , ws , path-ref (`format_design.md:359`); fragments are blocks-only, no head (`format_design.md:2232`) | **yes in shape.** The capability set would want it for the generated-fragment split §6.2 models (one entry file, `include`d case fragments). Population accounting is designed (`format_design.md:1289-1300`) | W2, **REFUSED BY NAME** (MEASURED, §1.9 M10) | SHOULD |
| **N-51** | a CONTENT HASH over the whole set, so a record names exactly what was measured | `Subbench.content_hash()` over every committed file in the directory (`subbench.py:287-311`); carried as `subbench.content_hash` in every record | **nothing is asked of the format** — a `.rxt` file is a committed file and hashes like any other. Recorded so the list is complete; note that `include`d fragments and `@file:` subjects must ALL be inside the hashed directory, which is a bench-side rule | n/a | n/a | n/a |
| **N-52** | **a head-only READER that emits the descriptive productions as TSV**, so this project never writes a second parser | `pcrec --list-source` today, used in the export→verify direction (`tools/selfcheck.py`'s `check_rxt_export`, [B38]) | `--list-source`'s sixteen-column TSV (`rxt_format.md:425-442`) | **partial, and this is the tooling ask.** The dump has NO column for `tag`, `oracle`, `variant`, `mc`, `requires` or any provenance field, and none for a case line at all. `--list-source` is explicitly THE SEAM (`rxt_format.md:418-423`) and the reason the harness grows no head parser; the same argument applies to every descriptive production W2/W3 adds | W1 **BUILT**, the extension **ABSENT** | **MUST** |
| **N-53** | comments stay operational; every machine-readable fact is a FIELD | `subbench.toml` comments are prose only | R-RXT-2 (`requirements.md:59`) and the `description`-is-a-field ruling (`format_design.md:450-457`) | **yes — and this note endorses it without qualification.** No need below is proposed as a `#` convention. `rxt_format.md:149-150`: whole-line `#` only, a `#` elsewhere is data — MEASURED: `pattern #` is a pattern, not a comment (§1.9 M13), which is what makes `bench/altwide`'s and `bench/syntax`'s floor patterns expressible | W1, **BUILT** | n/a |

### 1.9 The thirteen MEASURED facts

Every one from `build/pcrec-d34c9131/build/pcrec --list-source` at pin
d34c9131 (abi 23), parse-only. Fixtures and the comparison script are in
the lane's scratchpad; each is one file of at most six lines and is
reproduced verbatim in §3's acceptance checklist so a reviewer can re-run
them.

| # | probe | result |
|---|---|---|
| **M1** | `pattern ab<NUL>cd` | **TRUNCATED to `ab`. Exit 0, no diagnostic.** The parser splits the slurped file into NUL-terminated C strings (`rxt_source.c:437-456`), so every rest-of-line value ends at the first NUL. **This resolves N3 §5's explicitly unverified risk: the answer is silent data loss, not refusal** |
| **M2** | `pattern abc\r\n` | dumps as `abc` — the CR is trimmed. Documented (`rxt_source.c:395-396`) and correct for a Windows-edited file; lossy for a pattern that ends in CR |
| **M3** | `pattern caf\xe9[\x80-\xff]+` | **byte-exact round trip** through the dump's `\xNN` escaping |
| **M4** | a literal TAB mid-pattern; a doubled backslash; a mid-line CR; trailing spaces | all **byte-exact**. Trailing spaces are kept (rest-of-line is data) |
| **M5** | two `description` lines in one block | **the second SILENTLY WINS.** No diagnostic, exit 0 |
| **M6** | `name crs-942.160`, `name Upper.Name-1` | both accepted — the widened grammar, confirmed |
| **M7** | two blocks with the same `name` | refused by name, exit 1: "duplicate block name 'dup' (already named …)" |
| **M8** | a `(?x)` pattern continued on an indented second line | refused by name, exit 1: "a pattern block's lines are NOT indented". **LOUD, which is the good half of N-2** |
| **M9** | a 20,000-byte `pattern` line | parses; no line-length bound |
| **M10** | `tag`, `variant`, `oracle`, `include` | each refused BY NAME with its wave: "'tag' is a wave-2 pattern-block declaration and is NOT IN THIS BUILD… the keyword is real, not a typo". Exactly as `rxt_format.md:57-62` promises |
| **M11** | this repo's slug rule `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$` against a pcrec-style block name | `iso_ts` is **NOT** a legal bench `pattern_id` (underscore is not in the slug alphabet); nor is `crs.942` or `Upper`. **`subbench_directory_model.md:554-560` Q4's claim that the import direction is lossless because "`foo_bar` is a legal slug" is WRONG.** Ours to fix, not pcrec's, but R-BENCH-8 should not inherit the error |
| **M12** | an authored file: head `description |` block scalar, two blocks with `name` + one-line `description`, **no `target`, no `config`** | parses; dumps one `description` head row and two `pattern` rows with `line`, `name`, `value` (the block description) and `pattern` columns filled. This is N-43's shape working today |
| **M13** | `pattern #` | a pattern, not a comment — the floor-pattern case |

One further measured observation with no probe number, because it is an
absence rather than a result: **`--list-source` accepted a block
containing `m @file:"subj.bin" 0 3` without complaint.** The head parser
recognises `m` as a block keyword and never reads its value
(`rxt_source.c:153-166`'s comment says so: "it reads none of their
values"), so a `@file:` subject inside a case line passes the dump
silently even though `@file:` is a refused W2 production. `--list-source`
is therefore not a validator for case-line content — which matters for
§3's acceptance checks and for N-52.

---

## 2. The productions this would need

Twelve proposals. Each gives a grammar sketch in `format_design.md`
§1.3's own EBNF style, states scope and repeatability, and says what
pcrec's OWN harness could do with it — because the format's stated stance
is one format for both repos (`format_design.md:1902-1907`: "what the
bench must still own… this note's contribution is that when they do, the
sidecar has somewhere to go"), and an ask that only serves one consumer
is a worse ask.

**These are sketches, not a specification.** Every one is pcrecdev1's to
accept, redesign or refuse. Where this note has a preference it says so;
where the choice is genuinely open it says that instead.

### 2.1 A `provenance` block — needs N-11..N-19

**The gap.** Nine required-or-conditional fields per pattern, no
production in any wave, and `description`'s one line cannot hold them
(§1.3).

**The precedent to copy, not invent.** The `freq` data block already does
exactly this shape: a keyword, a name, an indented body of `<key> <value>`
lines, with SOME LINES REQUIRED and a block missing them REFUSED
(`format_design.md:1242-1288`; the membership rule at `:1251-1258`). Its
own provenance half — `exemplar`, `bytes`, `sha256`, `analyzer`, `date`
— is required "because the exemplar is absent by design" (`:1279-1283`).
A wild pattern's source is absent by exactly the same logic: a URL fetched
on a date, a licence nobody committed into this repo.

**Grammar sketch** (W2; block-scoped; at most ONE per pattern block):

```ebnf
(* ---------- body: a pattern block ---------- *)
block-line  = … | provenance-block ;

provenance-block = "provenance" , eol , { INDENT , prov-line , eol } ;
prov-line =
      "source"     , ws , ident            (* a registered source slug, REQUIRED *)
    | "url"        , ws , rest-of-line     (* the exact URL fetched,    REQUIRED *)
    | "ref"        , ws , rest-of-line     (* file/rule/line inside it, conditional *)
    | "licence"    , ws , spdx-id          (* from the source's own LICENSE, REQUIRED *)
    | "licence-note" , ws , prose-value    (* optional *)
    | "retrieved"  , ws , iso-date         (* RFC 3339,                 REQUIRED *)
    | "fidelity"   , ws , ( "verbatim" | "adapted" | "inspired" )   (* REQUIRED *)
    | "adaptation" , ws , prose-value      (* REQUIRED iff fidelity != verbatim *)
    | "attribution", ws , prose-value ;    (* REQUIRED iff the licence demands it *)
```

**Scope and rules.**

- Block-scoped, at most one per pattern block. A SECOND `provenance`
  block in one block is REFUSED by name — not last-wins, which is the
  `description` hazard M5 measured.
- `source`, `url`, `licence`, `retrieved`, `fidelity` are REQUIRED; a
  block missing one is refused naming the missing line, exactly as a
  `freq` block without `question`/`reader` is.
- `ref` is REQUIRED unless `source` is the reserved slug `authored`.
- `adaptation` is REQUIRED iff `fidelity` is not `verbatim`. This is the
  one conditional the format would have to enforce and it is the whole
  value of making it structural: a mechanically-changed pattern with no
  stated change is the failure a reviewer cannot catch by reading.
- `attribution`'s conditionality on the LICENCE is a policy the format
  should NOT know (SPDX ids are an open set). Proposal: the format
  enforces nothing here and the consuming project's own gate does — but
  the FIELD must exist, because a CC BY-SA 4.0 pattern with nowhere to
  put its attribution is a licence breach with a format cause.
- **It carries a block scalar.** `adaptation` and `attribution` are
  prose, so they take `prose-value` — and here the head/body asymmetry
  bites: a block scalar is a HEAD form only (`rxt_format.md:196-203`),
  because a pattern block's lines are not indented. A `provenance` block
  is ITSELF indented continuation, which means it is a head-shaped
  construct living in the body. **This note flags that as the design
  problem in its own proposal and does not resolve it**; §5 Q1 asks it.
  The alternative, if the asymmetry must hold, is nine flat block-scoped
  lines (`prov-source`, `prov-url`, …) — uglier, no indentation, and it
  keeps the body's one rule intact.

**Worked example** — one real capability-set member, a CRS rule imported
verbatim (family 3, `capability_set_v1.md:180`):

```
pattern (?i)\b(?:d(?:atabas|b_nam)e[^0-9A-Z_a-z]*\(|schema_name\b)
name waf-sqli-keywords
description CRS 942140's database/schema keyword alternation
provenance
  source        crs
  url           https://raw.githubusercontent.com/coreruleset/coreruleset/v4.x/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf
  ref           rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf#942140
  licence       Apache-2.0
  retrieved     2026-09-12
  fidelity      adapted
  adaptation    the ModSecurity `@rx` wrapper and its transformation chain
                dropped; the regex body is byte-identical to the rule's
```

**What pcrec's own harness gets.** pcrec's corpus already carries
imported material whose origin lives only in a file header comment —
`tests/base/d27_*.rxt`'s generator provenance, the `# pcre2-only` marks
whose justification lives in `docs/dev/upstream_issues.md`
(`rxt_format.md:509-513`). A structured `provenance` block gives pcrec's
own imports (the Fowler suite, PCRE2 `testdata`-derived cases) the same
machine-readable origin, and makes "where did this block come from" a
`--list-source` column rather than a grep through comments. It is also
the natural home for the D27 blinded corpora's own authorship statement.

### 2.2 A vocabulary DECLARATION for closed tag keys — needs N-10, N-21, and N-20's closed half

**The gap.** `tag` is the carrier for family, role, hazard class, size
class, convention, regime, method and REQUIRES — eight key families —
and `tag-value` is free vocabulary by design (`format_design.md:341-343`).
A typo is a legal tag. `capability_set_v1.md:521-525` states the closed-set
requirement for REQUIRES in the strongest terms and R5 finding B3 makes
the identical point about this project's own `patterns[].tags`: "a typo
that silently becomes a new tag is a capability claim nobody checked."

**What is NOT being asked.** Not a fixed vocabulary in the format. AR-6
forbids putting engine-shaped enums in the format
(`format_design.md:2047`) and the bench's own vocabularies must stay the
bench's. What is asked is a way for a FILE to declare its own closed sets
and have the parser enforce them.

**Grammar sketch** (W2; head-only; repeatable, one per key):

```ebnf
decl-line = … | "vocabulary" , ws , tag-key , ws , tag-value , { ws , tag-value } ;
```

**Rules.** A `vocabulary <key> <v1> <v2> …` head line declares that
`tag <key>=<value>` may only take a listed value; a `tag` whose key is
declared and whose value is not listed is REFUSED BY NAME, naming the
key, the offending value and the declared set. A key with NO `vocabulary`
line keeps today's free-vocabulary behaviour exactly, so nothing in the
existing corpus changes and the production is purely additive. A
`vocabulary` line for a key no `tag` uses is legal (it is a declaration,
not an assertion) but a `--list-source` consumer can see it and warn.

**Worked example** (the head of the capability set):

```
vocabulary hazard   none exponential-backtracking ambiguous-decomposition \
                    exact-minimum-boundary large-count wide-alternation
vocabulary fidelity verbatim adapted inspired
vocabulary requires backrefs lookaround lookbehind-variable atomic-possessive \
                    recursion conditionals k-reset control-verbs \
                    unicode-properties named-groups free-spacing callouts \
                    span-reporting non-utf8-subject captures true-end-anchor
```

(The continuation shown here as `\` is illustrative only — a
`vocabulary` line is a head declaration, so INDENTATION IS CONTINUATION
already, `rxt_format.md:160-168`, and the real spelling wraps with an
indented second line. Stated because it is the kind of detail an
implementer should not have to guess.)

**Why `requires` should be a `tag` key and not its own production.** It
was tempting to ask for `requires <label> …` as a first-class block line.
Against it: `tag` already accumulates across repeated lines and already
mixes bare labels with pairs (`format_design.md:1843`, the U1 ruling), so
`tag requires=backrefs requires=lookaround` costs nothing new; and a
dedicated production would make the capability model a FORMAT concept,
which is exactly the engine-neutrality line AR-6 draws. With
`vocabulary`, the closed-set discipline is available to every key without
the format knowing what any of them mean.

**What pcrec's own harness gets.** pcrec's corpus has its own closed sets
that live in prose today — `gu`'s four give-up codes are enforced by the
parser, but a file-level convention like `tests/known_fail/`'s membership
rule is not. More directly: `vocabulary` is what makes
`format_design.md`'s own §4.5 mapping SAFE. That table sends
`hazard_class`, `size_class`, `convention` and `role` — four closed
record-schema enums — into free-vocabulary tags. Without a declaration
mechanism, the absorption silently downgrades four validated fields to
unvalidated strings, which is a regression the format should not have to
ship.

### 2.3 A per-config capability declaration — need N-22

**The gap.** W3's `config` body can say what an engine IS
(`testee pcre2/10.46`) and what options it takes (`option k=v`), but not
what it CAN DO. `capability_set_v1.md:532-552` establishes that the
declaration must be PER CONFIG, not per engine: `pcre2-dfa` and
`pcre2-interp` are one library at one version satisfying different tag
sets.

**Grammar sketch** (W3; a `config`-body line; repeatable, accumulating):

```ebnf
config-line = … | "capable" , ws , tag-value , { ws , tag-value } ;
```

**Rules.** Lists the vocabulary values (§2.2) this config SATISFIES.
Repeatable and accumulating, like `tag`. **Absent means NOTHING is
satisfied** — fail-closed, deliberately, so a new adapter cannot claim
capabilities by omission (`capability_set_v1.md:549-552`). Under §2.2's
`vocabulary requires …` declaration the values are checkable, which is
the point: a `capable backrefs` on a config beside a `vocabulary requires`
that does not list `backrefs` is a typo the parser can catch.

**Worked example:**

```
config pcre2-dfa
  testee pcre2/10.46
  option match-mode=dfa
  capable lookaround atomic-possessive recursion conditionals
  capable unicode-properties named-groups free-spacing true-end-anchor
  # NOT capable: captures, k-reset, backrefs, control-verbs
  # (man pcre2matching items 2, 4, 7)

config tre-default
  testee tre/0.8.0
  capable named-groups
```

**This is the proposal this note is least sure of** — see §1.4's own
note. A capability list describes an engine, and a format that carries it
is carrying engine knowledge. The counter-argument is that `config … testee`
ALREADY carries engine knowledge (a version string), and that a reader of
the file who sees a pattern with no result for `tre-default` needs the
reason in the same file. §5 Q4 puts it to pcrecdev1 as an open choice.

### 2.4 Convention-scoped expectations — need N-35 (the deepest gap)

**The gap.** One pattern, one subject, TWO different correct answers. `a|ab`
against `"ab"` is `0 1` under `perl-leftmost-first` and `0 2` under
`posix-leftmost-longest`. Today a case line is one expected answer, and
`variant` supplies different pattern TEXT for a testee rather than a
different ANSWER for the same text. R-BENCH-5 asked for the convention
TAG and got it designed; it did not ask for the second answer, and without
it the tag cannot be acted on.

**Grammar sketch** (W3; a case-line QUALIFIER, not a new case kind):

```ebnf
block-line = … | "under" , ws , tag-value , ws , case-line ;
case-line  = ( "m" | "n" | "ms" | "ns" | "mc" ) , … ;   (* today's, unchanged *)
```

**Rules.**

- An UNQUALIFIED case line means what it means today: the expectation
  under the file's or block's declared convention (`tag convention=…`),
  which is the canonical one.
- `under <convention> m "<subject>" <start> <end>` states the answer a
  testee tagged with THAT convention is scored against, for the same
  (pattern, subject). A testee whose convention has no `under` line for a
  case falls back to the unqualified line — so a set that declares no
  conventions behaves exactly as today, and the production is additive.
- `<convention>` is a `tag-value`, so §2.2's `vocabulary convention …`
  declaration closes it. The format does not know what
  `posix-leftmost-longest` means, which is the AR-6 line held.
- Two `under` lines for one (convention, subject) pair are REFUSED as a
  duplicate, not last-wins.

**Worked example** (family 11's separator case):

```
pattern a|ab
name sem-alt-order
description the leftmost-first / leftmost-longest separator
tag family=semantics-divergence hazard=none size=tiny role=member
tag convention=perl-leftmost-first
provenance
  source        authored
  url           n/a
  licence       n-a
  retrieved     2026-09-12
  fidelity      inspired
  adaptation    written from the leftmost-first vs leftmost-longest rule
                as stated in re2's own Syntax documentation
m "ab" 0 1
under posix-leftmost-longest m "ab" 0 2
```

**Why not `variant`.** `variant tre a|ab` would give TRE the same text and
still score it against `m "ab" 0 1`. Making `variant` carry an answer
would conflate two axes the format deliberately separates: a variant is
about SPELLING (R-BENCH-7), a convention is about SEMANTICS (R-BENCH-5).
`format_design.md:1237-1241` already states the rule that makes this
matter: "a testee's variant is checked against the *canonical*
expectations, which the *canonical* oracle produced." That rule is right
and it is exactly why conventions need their own carrier.

**What pcrec's own harness gets.** Less than the others, honestly —
pcrec is a single-convention engine and `tests/harness/run.sh` has one
oracle. Two things: `tests/assertions/`'s `verify_pcre2.py` differential
exists because several constructs "have no python equivalent at all"
(`rxt_format.md:516-522`), which is the same shape one step smaller — an
`under python …` line would let a divergence be STATED in the corpus
instead of parked behind a `# pcre2-only` mark plus an
`upstream_issues.md` entry. And `docs/testing.md`'s "Oracle exclusions"
list becomes data.

### 2.5 A subject reference with an id and an optional hash — needs N-26, N-27

**The gap.** `@file:"path"` gives a path. This project needs a stable
subject ID (every expectation key, report row and interpreter fact names
one) and an integrity hash (its subject trees are gitignored and
regenerated, so the referenced file is NOT committed and NOT reviewed —
which is precisely the condition under which `format_design.md:1205-1208`
itself says provenance IS required).

**Grammar sketch** (W2, extending `file-subject`):

```ebnf
file-subject = '@file:"' , path-chars , '"' , [ ws , "as" , ws , ident ]
                                            , [ ws , "sha256" , ws , hex64 ] ;
```

**Rules.** `as <id>` names the subject; the id is in a per-file subject
namespace and must be unique there, so a case can be cited as
`(pattern, subject-id)` rather than by line. `sha256 <hex64>` is OPTIONAL
and, when present, is CHECKED by whatever reads the subject: a mismatch
is a refusal naming the path, the expected and the actual digest. Absent
means today's behaviour, unchanged.

**Why optional rather than required.** `format_design.md:1205-1208`'s
argument against a hash is that a committed subject file "sits in the repo
beside the `.rxt` and is covered by the same review and the same history".
That argument is exactly right for pcrec's corpus and exactly wrong for a
generated subject tree. Optional keeps both true: pcrec writes none, this
project writes one on every reference, and neither has to argue.

**Worked example:**

```
m @file:"subjects/http-mixed-004.bin" as http-mixed-004 sha256 3f2a…  1284 1309
n @file:"subjects/http-mixed-005.bin" as http-mixed-005 sha256 91c0…
```

**What pcrec's own harness gets.** A named subject makes a failure line
`file:line: subject http-mixed-004: expected … got …`, which is more
useful than a line number when a corpus is generated and its line numbers
move on every regeneration. pcrec's own generated corpora
(`tests/recursion/gen_corpus.py`, the D27 sets) have exactly that
property.

### 2.6 A scoping rule that keeps a set's config out of pcrec's build — need N-44

**The gap, restated.** D93: a `.rxt` source's composed config WINS over a
command-line flag on the same axis
(`subbench_directory_model.md:441-448`; `rxt_format.md:133-136`). This
project's entire pcrec testee matrix — sixteen configs — is command-line
flags. `format_design.md:2198-2284` §6.2's own worked bench file carries
`config pcrec` with a `pcrec --features all` line and a `use pcrec, pcre2,
re2`. If that file is the corpus, every pcrec testee compiling from it is
silently pinned by the file. The exporter already refuses to write such a
line (`tools/export_rxt.py:34-37` rule 5) precisely for this reason.

**Three candidate resolutions**, in this note's order of preference.

1. **A file declares whether its configs are BUILD directives or TESTEE
   descriptions.** One head line, `configs describe` (default: `build`,
   today's meaning). Under `describe`, `config` blocks are read by
   consumers and IGNORED by `pcrec --source`, which then builds only what
   its command line says. A set file writes `configs describe` once and
   the collision cannot occur.
2. **A `config` carrying a `testee` line is inert for pcrec's own
   build.** No new production: the rule becomes "a config that names a
   foreign testee is a description, not a build config." Cheaper, but it
   leaves `config pcrec` in §6.2's example still winning, which is the
   actual hazard.
3. **The set writes no `config` at all**, as today's exporter does, and
   the testee roster lives somewhere else. This is the status quo and it
   is the hybrid Frank's ruling removed — recorded as the null option.

**What pcrec's own harness gets.** Resolution 1 also answers a question
`--source` has today: a file whose configs are descriptions can be listed,
diffed and reviewed without any risk that reading it changes what a build
does. It makes `--list-source`'s "AS WRITTEN, never resolved" stance
(`rxt_format.md:476-482`) into a property of the FILE rather than only of
the dump.

### 2.7 A pattern spelling that can carry a newline, a NUL or a trailing CR — needs N-2, N-4, N-5

**The gap.** `pattern` is rest-of-line, verbatim, unquoted, unescaped
(`rxt_format.md:210-212`). That is a GOOD rule — it is why this project's
185 patterns export byte-exactly with no escaping layer
(`tools/export_rxt.py:38-61` rule 6) — and it means three byte values
have no representation: `\n` (no continuation), `\0` (silently truncated,
MEASURED M1), and a CR immediately before the line end (silently trimmed,
MEASURED M2).

**What is NOT asked.** Do not change `pattern`. Every existing file and
every existing exporter depends on its verbatim rule.

**Grammar sketch** — a SECOND spelling, distinctly named (W2):

```ebnf
block-line = … | "pattern-esc" , ws , quoted-pattern ;
quoted-pattern = '"' , { subject-char | escape } , '"' ;   (* the SAME seven escapes *)
```

**Rules.** `pattern-esc "…"` starts a block exactly as `pattern` does and
means the same thing; its text is the decoded bytes, using the format's
OWN seven-escape subject vocabulary (`rxt_format.md:374-385`) and no
second vocabulary. A block carries one or the other, never both. Because
the escape table already includes `\n`, `\xHH` and `\\`, all three
unrepresentable cases become expressible with nothing new invented, and
`tests/harness/driver.c`'s existing `decode()` already implements the
decoder (`rxt_format.md:462-464` makes that point about the dump's
escaping).

**Worked example** (family 6's VS Code `number` rule, as authored):

```
pattern-esc "(?x)\n  -?  (?:0 | [1-9]\\d*)\n  (?: \\.\\d+ )?\n  (?: [eE][-+]?\\d+ )?\n"
name code-json-number
description VS Code JSON.tmLanguage's `number` rule, free-spacing, as written
```

**And a refusal, whichever way this goes.** Even if `pattern-esc` is
refused as a feature, **M1's silent truncation should become a refusal**.
A NUL in a `pattern` line today produces a shorter pattern, exit 0, no
diagnostic — a wrong artifact from a valid-looking file. `slurp_lines`
(`rxt_source.c:399-456`) already reads the whole file and knows every
byte; a scan for an embedded NUL before splitting would refuse by name at
no measurable cost. **This note ranks that refusal ABOVE `pattern-esc`
itself**: a missing capability is a known limit, a silent truncation is a
trap.

**What pcrec's own harness gets.** The NUL refusal is unambiguously
pcrec's own win — its corpus is hand-written and a stray NUL from a bad
editor or a botched generator would today produce a passing test of the
wrong pattern. `pattern-esc` is more marginal for pcrec, though
`tests/modifiers/`'s `(?x)` coverage is the one place its corpus has the
same shape as family 6.

### 2.8 `variant_kind`, and a tag value that can hold a sentence — need N-41

**Two small gaps in one place.** `variant`'s designed body carries the
replacement text and an optional `groups <name>=<n>` map
(`format_design.md:422-424`). This project carries three more fields:
`variant_kind` (a closed two-value enum, `syntax-only` / `restructured`,
which the reporter is meant to show beside the number), `objective_
preserved` (a reviewed sentence) and `capture_map` (↔ `groups`, fits).
`format_design.md:1879-1883` routes the reviewed sentence to
`tag variant-note=…` — but a `tag-value` may contain **no whitespace**
(`format_design.md:342`), so a sentence does not fit in one.

**Grammar sketch** (W3, extending `variant-body`; and W2 for the second half):

```ebnf
variant-body = "unsupported" , ws , rest-of-line
             | [ "kind" , ws , tag-value , ws ] , rest-of-line ,
               [ eol , "groups" , ws , group-map ] ;

(* and, for prose: *)
tag-item = tag-label | tag-pair | tag-prose ;
tag-prose = tag-key , "=" , quoted-subject ;   (* whitespace allowed inside quotes *)
```

**Rules.** `kind <value>` is optional and closed by §2.2's `vocabulary
kind …`. The quoted `tag-prose` form lets a reviewer's sentence be a tag
value without loosening the bare form's no-whitespace rule; the existing
seven escapes apply inside the quotes, so the vocabulary count stays at
one.

**What pcrec's own harness gets.** `tag-prose` is generally useful the
moment `tag` ships — a one-word tag value is a real constraint for any
descriptive key (`method=`, `question=`, an exclusion reason). The
`variant kind` half is bench-only.

### 2.9 An oracle that can name any engine, at a version — needs N-36, N-38

**The gap.** `oracle-spec = "python" | "pcre2" | "none" , ws ,
rest-of-line` (`format_design.md:365`) is a closed set of two engines. A
capability set's roster is eight, and family 11's POSIX cases want a
POSIX engine as their own oracle. Separately, no production names the
oracle's VERSION, and a cross-engine correctness claim that does not say
"libpcre2 10.46" is not reproducible.

**Grammar sketch** (W3, widening the existing production):

```ebnf
oracle-spec = "none" , ws , rest-of-line
            | engine-ref ;                 (* ident , [ "/" , version-chars ] *)
```

**Rules.** `oracle python` and `oracle pcre2` keep their exact meanings
(they are `engine-ref`s with no version), so nothing in pcrec's corpus
moves. `oracle pcre2/10.46` pins the version. `oracle tre/0.8.0` names an
engine a consumer may not have — which is already handled: R-VG-3's rule
is that "an absent oracle degrades to a labelled skip, never a silent
pass and never a hard failure" (`format_design.md:1220-1223`), and that
rule is what makes widening the enum safe rather than a portability
hazard.

**What pcrec's own harness gets.** A version on the oracle is the fact
`docs/testing.md`'s "Oracle exclusions" list is implicitly about — a
divergence is between pcrec and a SPECIFIC python or libpcre2 build, and
recording which one is what makes the exclusion re-checkable when the
oracle moves.

### 2.10 `mc`'s counting rule, stated — need N-32

**Not a new production — a semantics statement the spec owes.** `mc ,
ws , subject , ws , int` (`format_design.md:419`) is a match COUNT. Its
overlap rule is not stated anywhere this note could find. This project's
driver protocol fixes non-overlapping advancement as
`pos = max(end, pos+1)` (`pcrecbench/adapters.py:20-22`) — the `+1` is
what makes an empty match terminate. Two engines counting under different
rules would both satisfy the same `mc` line, which is R-BENCH-4's
adjudication requirement failing quietly.

**The ask is one paragraph in `rxt_format.md`**, not code: state whether
`mc` counts non-overlapping matches, and if so under which advancement
rule for an empty match. If the intended answer is "the harness's rule,
whatever it is", say that — it is still better than silence, because a
foreign-engine adapter then knows it must match the harness rather than
its own library's default (RE2's `FindAll`, PCRE2's `pcre2_match` loop
and Oniguruma's `onig_scan` do not all agree here).

### 2.11 Regime membership without the subroutine wrapper — need N-48

**The gap, and it is a real defect in a shipped design.**
`format_design.md:1884-1897` §4.5 item 4 resolves regimes by writing the
canonical pattern once as a `name`d definition and one block per regime
whose pattern is `(?&<name>)`. That mechanism **cannot be used by any set
in this repository**: a delivering or plain subroutine call goes through
PCRE2's own group-name grammar, which refuses `-` and `.`, and
`rxt_format.md:284-291` states it outright — "a definition whose name
carries `-` or `.` **cannot be called from a pattern**". Every pattern id
in all five sets here is a hyphenated slug (`cls-upto-1024`, `iso-ts`,
`w-256`, `anc-caret`). The widened name grammar exists precisely so those
ids need no map (`rxt_format.md:290-296`) — and the regime mechanism
needs the narrow grammar. The two rulings are individually right and
jointly unusable.

**Three ways out**, none of which this note picks for pcrecdev1:

1. **`tag regime=` alone, with the subject set attached to the case
   lines rather than to the block.** A block carries all its cases; each
   case is tagged with its regime. Needs a per-CASE scope, which Frank
   ruled against (`format_design.md:1884-1886`: "there is no case scope").
2. **A regime-scoped case group inside one block** — an indented
   `regime <label>` sub-block holding its own case lines. Same head/body
   indentation problem as §2.1.
3. **Let a definition be called by a NAME MAP the format derives**, the
   way `target =` already derives a C prefix by `-`/`.` → `_`
   (`rxt_format.md:107-110`). `(?&cls_upto_1024)` would reach
   `name cls-upto-1024` by the same rule. Cheap, uses machinery that
   already exists, and has one sharp edge: the derivation is deliberately
   NOT injective (`a-b` and `a.b` both give `a_b`, and the spec says the
   refusal is where that is paid for, `:111-119`), so a call would need
   the same collision refusal a duplicate `target` prefix gets.

**This note's observation, not a recommendation:** option 3 costs the
least and reuses a rule the format already defends. But the deeper point
for pcrecdev1 is that §4.5 item 4 should not be treated as settled — it
was measured against `bench/loglines`' eleven patterns, whose ids include
`iso-ts` and `level-context`, and the mechanism it proposes cannot
express either of them.

### 2.12 `--list-source`, extended to the descriptive productions — need N-52

**The gap, and why it matters more than it looks.** `--list-source` is
THE SEAM (`rxt_format.md:418-423`): pcrec owns the head grammar, is its
only implementation, and `tests/harness/run.sh` "gains no head arms at
all". This project relies on the same seam in the export direction today
(`tools/selfcheck.py`'s `check_rxt_export`, [B38]). The dump's sixteen
columns cover W1's head and the pattern block's W1 attributes and NOTHING
ELSE — no `tag`, no `oracle`, no `variant`, no `mc`, no provenance, and
no case lines at all. If W2/W3 land without extending it, a bench-side
loader must grow its own parser for exactly the productions the seam
exists to keep single-implementation. **That is the same hazard one wave
later, and it is the cheapest of the twelve asks to get wrong.**

**Two shapes, and this note prefers the second.**

1. **More columns.** A `tag` row kind and a `variant` row kind in the
   same stream, with the existing sixteen columns plus a few. Keeps one
   table; the column count grows toward thirty and most are empty on most
   rows.
2. **Sections.** `docs/spec/table_contract.md`'s `#section` mechanism
   exists for one command emitting several tables with different columns,
   and `rxt_format.md:483-491` DECLINES it here for a stated reason —
   head/body INTERLEAVING is what a consumer checks, and that is
   expressible only as row order in one stream — while naming the trigger
   that would earn it: "a data block whose rows cannot be columns of this
   table under any reading." A `provenance` block (§2.1) is exactly that:
   nine keyed lines that are not attributes of the `pattern` row. So the
   trigger the spec named is met by this note's own first ask, and
   adopting sections stays free ("a stream with no `#section` line is a
   single anonymous section").

**One thing the extension must not lose.** MEASURED (the observation
after §1.9): `--list-source` accepts a case line containing a REFUSED
`@file:` subject without complaint, because the head parser recognises
`m` as a keyword and reads none of its values. That is correct today and
becomes wrong the moment a consumer treats the dump as a validator for
the whole file. Whatever the extension does, it should say plainly which
productions it VALIDATES and which it merely recognises.

**What pcrec's own harness gets.** The same thing it got the first time:
`run.sh` never grows a parser for a production pcrec already parses. With
W2's `include`, the dump is also the only place the include CLOSURE is
visible without re-implementing resolution — which §2.11's population
accounting (`format_design.md:1289-1300`) will need a reader for.

---
