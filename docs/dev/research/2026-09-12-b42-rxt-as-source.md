# [B42] research note 3 — `.rxt` AS THE SOURCE OF A BENCH SET

**Lane b42rxt, 2026-09-12.** Scope: phase (a) of [B42] (the capability
survey set), research question 3 only — precisely what pcrec's `.rxt`
format can and cannot carry for a bench set today, and what the
source-of-truth options are. Not a design; no code, no schema change, no
sidecar change. Every claim is cited `file:line`; where pcrec's own intent
is unclear this note says so rather than infer it.

**Relationship to existing work.** [B29]'s `docs/design/
subbench_directory_model.md` (2026-09-01) already scoped the directory
model against `--source`/`--target`/`--lib-path` at pcrec's then-pin (abi
15, [DD-13b.W1.2]) and recommended "do nothing until the descriptive
waves land." This note re-verifies that finding at the CURRENT pin
(d34c9131, abi 23; six more re-pins since [B29]), finds one of [B29]'s own
counts now STALE (§2.3 below), and answers a narrower and different
question [B29] did not: not "should the adapter compile via `--source`"
but "should `.rxt` be authored as this project's SOURCE OF TRUTH for a
set's patterns" — the question [B42]'s charter states as a REQUIREMENT
("(4) BUILT ON THE .rxt FILE FORMAT"), not a design option to accept or
decline.

---

## 0. Method and the format-movement check

Read in full: `~/pcrec/docs/spec/rxt_format.md` (the contract, at the
d34c9131 pin's tree); `~/pcrec/docs/design/dd13_format/requirements.md`
(DD-13a, §5 R-BENCH-1..9); `~/pcrec/docs/design/dd13_format/
format_design.md` (DD-13b, the grammar/semantics design, §§1-7);
`~/pcrec/docs/design/dd13_format/w1_impl.md` (headings, for build status);
`~/pcrec/docs/design/dd13_format/usecases_and_outline.md` (headings);
this repo's `docs/design/subbench_directory_model.md`,
`docs/design/requirements.md`, `docs/design/record_schema.md` (pattern
sections), `pcrecbench/subbench.py`, `tools/export_rxt.py`, and
`bench/syntax/`, `bench/altwide/` (CLAUDE.md + sidecar + generators).

**Format movement since the pin, checked directly:**

```
$ git -C ~/pcrec log -1 --format='%H %ad' d34c9131   # 2026-09-06 10:23
$ git -C ~/pcrec log -1 --format='%H %ad' origin/main # 2026-09-11 (818a871)
$ git -C ~/pcrec merge-base --is-ancestor d34c9131 origin/main   # true
$ git -C ~/pcrec log --oneline d34c9131..origin/main -- \
    src/parse/rxt_source.c docs/design/dd13_format/ \
    docs/spec/rxt_format.md docs/spec/cli.md
ff8fed78 [msgtrim] shorten four .rxt-source refusal messages ...
dd3eda6f WIP stage 5: docs — ... (utf8, unrelated)
f79296ec WIP [M5.0 stage 4]: ... (utf8, unrelated)
467e0dcf WIP [M5.0 stage 3]: ... (utf8, unrelated)
```

**Finding: no grammar or spec movement.** Five days and several commits
past the pin, the only change touching the `.rxt` source parser is a
diagnostic-message shortening (`ff8fed78`); the three `M5.0` commits are
UTF-8 backend work, unrelated to `.rxt`. `docs/design/dd13_format/` has no
commits at all in this range. **The grammar this note describes against
d34c9131 is current as of 2026-09-11.**

---

## 1. What `.rxt` carries today, and what it does not

### 1.1 The wave split — BUILT vs DESIGNED-not-built

The format's own grammar table assigns every production a wave
(`format_design.md:316-424`), and the wave table (`:459-465`) states who
is waiting on each:

| wave | productions | status at d34c9131 | who is waiting |
|---|---|---|---|
| **W1** | `name`, `description` (file/def/target/data-block; one-line only in a pattern block, `:434-448`), `lib`, `target … [with]`, `encoding`, `features only`, `config` (`pcrec`/`flags`/`features`/`encoding`/`engine`/`budget`, **and `from`**), AST composition + the three pattern-level extensions (numbered group, scope prefix, delivering call), `--emit-composed`, `rx_info.name`/`nentries` | **BUILT** (`[DD-13b.W1]` `STATE:started`… W1.1-W1.3 landed per this repo's own [B37]/[B39] pins) | `[LIB]`, `[DD-14]`'s multi-pattern files |
| **W2** | `include`, `@file:` subjects, `mc`, `tag`, the `freq` data block, `config`'s `analysis` line | **NOT BUILT** | `[ENG-PGO]`'s findings file, and explicitly **"the first in-format sub-bench"** |
| **W3** | `use`, `oracle`, `variant`, `config`'s `testee`/`option` | **NOT BUILT** | explicitly **"pcrec-bench sub-benches with a non-pcrec testee"** |

The current spec text is unambiguous that W2/W3 are refused, not merely
undocumented: *"Keywords belonging to a later wave of this format
(`include`, `tag`, `freq`, `use`, `oracle`, `analysis`, `testee`,
`option`, `mc`, `variant`) are recognised and refused **by name, as NOT
IN THIS BUILD**"* (`rxt_format.md:57-62`). That list is, almost item for
item, the list of things `subbench.toml` carries (`subbench_directory_
model.md:162-165` makes the same observation at the earlier pin; it still
holds).

### 1.2 Carries today (all W1, confirmed BUILT and in this repo's own use)

- **Pattern text**, verbatim, rest-of-line, no quoting/no escaping
  (`rxt_format.md:210-212`; `pattern <regex>`).
- **A block `name`** — the WIDER definition-name grammar, "a first byte
  that is a letter or `_`, then letters, digits, `_`, `-` or `.`"
  (`rxt_format.md:278-282`), explicitly **not** a PCRE2 group name or a C
  identifier, and explicitly widened for exactly this project's shape:
  *"The wider set exists because an exported set of patterns carries ids
  a person chose (`cls-upto-64`, `w-512`), and requiring an identifier
  would force every such export to carry a name map beside it"*
  (`:290-296`). **This is a format-movement finding this note re-verified
  and B29 could not have had**: at [B29]'s pin (abi 15, W1.2) the name
  grammar was still PCRE2-group-name-AND-C-identifier, giving 63 of 77
  patterns illegal as a block name (`subbench_directory_model.md:300-319`).
  Re-run against the CURRENT corpus and CURRENT grammar just now:

  ```
  email: 3 patterns, 0 illegal   loglines: 11, 0 illegal
  bounded: 43, 0 illegal          altwide: 33, 0 illegal
  syntax: 95, 0 illegal           TOTAL 185, 0 illegal
  ```

  **[B29]'s §3.3 finding is superseded, not merely aged.** [B38]'s own
  exporter docstring already recorded the same result at 185 ids
  (`tools/export_rxt.py:20-22`), so this is a re-confirmation, not new
  information — but [B29] itself (still the only design note in this
  repo that states the old count) should be read with that correction in
  mind by whoever writes [B42]'s design note.
- **`target <prefix> = <name> [with <c1,c2>]`** — a file-level build
  declaration, prefix derived from the name by `-`/`.` → `_`
  (`rxt_format.md:104-110`), one artifact per target, D88's rule that N
  targets are N separate translation units, never one multi-pattern unit
  (`format_design.md:1104`, `subbench_directory_model.md:181-187`).
- **`config <name> [from …]`** with `pcrec`/`flags`/`features`/
  `encoding`/`engine`/`budget` lines, composing under `with` (flat,
  later-wins) then against the block by KIND: `features` unions unless
  the block writes `features only`; `flags`/`encoding`/`engine`/`budget`
  are more-specific-wins; raw `pcrec` flags accumulate; size-limit
  overrides are max-wins regardless of order (`format_design.md:
  1059-1100`, table at `:1077-1084`).
- **`description`** as a machine-readable FIELD (not a comment), at
  file/definition/target/data-block scope, with a YAML-style `|` block
  scalar at HEAD scope only — a pattern block's own `description` is
  one-line (`format_design.md:1.2`, the W1.1 correction at `:434-448`).
- **`lib "path"`** — existence-resolved only, contents not read
  (`rxt_format.md:47`).
- **Composition** (D87): a numbered group, a scope-prefixed subroutine
  call, a delivering call (`(?&site=name)` / `(?&=name)` / `(?&*=name)`),
  all measured against libpcre2 10.46 to guarantee no legal PCRE2 pattern
  changes meaning (`format_design.md:489-550`).
- **`rx_info.name`** (never NULL; the block's `name` or the artifact's
  own prefix) and **`rx_info.nentries`** (rows in `groups[]`, equal to
  `nnames` until composition injects a definition's groups)
  (`match_api.md` as cited at `subbench_directory_model.md:209-224`).

### 1.3 Does NOT carry today (all W2/W3, DESIGNED but refused by name)

| missing thing | wave | extension point today |
|---|---|---|
| subjects / haystacks | W2 (`@file:"path"`) | **none** — a quoted inline subject only; `@file:` is designed (§2.8 below) but refused by name |
| expectations + oracle method | W3 (`oracle python\|pcre2\|none <reason>`) | **none for method**; `oracle` names the ENGINE only — the verification METHOD (R-BENCH-1's "derived-law-plus-induction" etc.) is a separate `tag method=<name>` (§2.9 below), also W2/refused |
| per-pattern tags/families/roles | W2 (`tag <label\|k=v> …`, repeatable, accumulating) | **none** — no comment convention is defined as a substitute; `#` comments are non-machine-readable by R-RXT-2 |
| per-engine spelling variants | W3 (`variant <testee> <text>` / `variant <testee> unsupported <reason>`) | **none** |
| capability/requires tags | not in any wave's production list as such | folds into `tag` (W2) generically; no dedicated capability keyword exists in any wave |
| regimes | not a named production; format_design.md's own absorption (§4.5) folds a bench "regime" into `tag regime=<label>` (W2) + a block-per-regime pattern (a name'd definition + a wrapper block per regime calling `(?&name)`) | `tag` (W2) |
| provenance (source URL/licence) | partially: the `freq` data block has REQUIRED provenance fields (`exemplar`, `bytes`, `sha256`, `analyzer`, `date`, W2 §2.10) but that family exists for exemplar-analysis findings, not for a pattern's own origin; no pattern-level provenance field exists in any wave | none dedicated; `description`'s free prose (W1, BUILT) is the only place today, and it is prose, not a structured field |

**No comment-convention extension point exists for any of the above.**
`docs/testing.md`/`rxt_format.md`'s comment rule is whole-line `#` only,
data everywhere else, and R-RXT-2 (DD-13a, cited at
`requirements.md:59-64`) treats comment-encoded machine state as the
exact failure mode the format's discipline exists to avoid — a
convention smuggled into `#` lines would be undocumented, unparsed by
pcrec's own tools, and exactly the kind of thing `description`'s
promotion to a real field (§1.2 above) was ruled to replace
(`format_design.md:450-457`, overturning the FIRST version's own
recommendation to put prose in comments). **The only sanctioned
extension mechanism is a new production in a future wave**, not a
side-channel inside an existing one.

---

## 2. Source-of-truth options, with consequences

### Option A — `.rxt` is THE source; everything else generated from it

A loader parses `.rxt` and derives the sidecar, manifests, and
expectations from it.

**What the loader must parse.** For the HEAD (file-level declarations),
pcrec's own binary is the only implementation and the design deliberately
makes this a SEAM: *"pcrec owns the head grammar and is its only
implementation; `tests/harness/run.sh` keeps its own body parser and
gains no head arms at all... the head is an untouched byte range whose
boundary comes from the one head parser, and the two cannot drift"*
(`rxt_format.md:418-423`). **`pcrec --list-source FILE` can be that
parser for us** — it is a documented, table-contract TSV over exactly
the head declarations we would need (`rxt_format.md:411-450`), and it is
already how this repo's own round-trip check works in the OTHER
direction (`tools/selfcheck.py`'s `check_rxt_export`, cited at
`docs/dev/plan_completed.md` [B38] row, re-derives an export and diffs it
against `pcrec --list-source` at the pin). **Writing an independent
`.rxt` head parser of our own would be exactly the second, uncontrolled
implementation the SEAM design exists to prevent** — the same "one
derivation, two readers" hazard `format_design.md:1585` names for
`--list-*` surfaces generally. Shelling to the pinned binary, not
reimplementing, is the available reuse.

For the BODY (pattern-block case lines: `m`/`n`/`g`/`gp`/`gu`/`perr`),
there is no equivalent seam — pcrec's OWN harness (`run.sh`) parses this
part itself in bash, and always will
(`rxt_format.md:418-423`: "gains no head arms at all" implies the body
stays the harness's own). Since W2/W3's descriptive productions
(`tag`, `oracle`, `variant`, `@file:`) live in the BODY-adjacent grammar
(block lines) and the HEAD (`use`, `oracle` as a head decl, `include`),
and **none of them is built**, a loader cannot read them from any
existing surface — there is nothing to shell out to. Building Option A
today for the DESCRIPTIVE fields means either (a) writing our own parser
for keywords `pcrec --list-source` does not yet recognize (a private
dialect indistinguishable, by construction, from guessing at pcrec's own
unshipped design — the exact keyword-collision risk `requirements.md`'s
own appendix flags, R27 F10, quoted at DD-13a "Appendix," §1063-1073 of
that note), or (b) waiting for W2/W3.

**Engine neutrality (R-BENCH-4).** The format's CONTENT is engine-neutral
where it matters: pattern text is PCRE2 syntax (portable across any
PCRE2-compatible engine, which is this bench's whole candidate roster,
`requirements.md:100-102`), spans are byte offsets, and `tag` values are
free vocabulary, not pcrec internals. What IS pcrec-specific is (a) the
`target`/`config`/`with` build machinery, which compiles a pcrec
artifact and has no meaning for RE2/Oniguruma, and (b) the `g`/`gp`
group-SLOT model, which DD-13a's own T-3 flags as potentially
pcrec-numbering-shaped — though `format_design.md`'s Attack 3 respons
finds this NOT live for us today (our `expectations.tsv` carries no
capture columns at all, `format_design.md:1979`) and, if it ever is,
resolves ENGINE-neutrally by NAME (`variant … groups <name>=<n>`, W3,
not built) rather than by pcrec's own numbering. **Conclusion: adopting
`.rxt`'s pattern-and-case grammar is not itself an R-BENCH-4 violation —
the grammar's case vocabulary does not encode pcrec internals.** What
WOULD violate R-BENCH-4/AR-6 (`subbench_directory_model.md:435-439`,
`requirements.md:114`) is writing `target`/`config` blocks INTO a file
this bench treats as its engine-neutral source, because those
declarations are pcrec build directives with no reading for any other
engine — and D93 makes this concrete and sharp (below).

**D93 — the file-wins-over-flag hazard.** *"A `.rxt` source's composed
config wins over a command-line flag on the same axis"*
(`docs/dev/decisions.md:6428` as cited at `subbench_directory_model.md:
441-448`; ratified the same day as W1.2). This repo's testee matrix is
built entirely from command-line flags (`--engine=vm`, `--no-captures`,
`--features all`, `testees/pcrec/configs.toml:74-89`). If a source file
we treat as the corpus ALSO carried a `config` block naming `engine`,
every testee compiling FROM that file would silently be pinned to one
engine, because `engine` composes more-specific-wins. **Any exporter or
authored `.rxt` this bench produces must therefore declare NO `config`
and no block-level `flags`/`engine`/`budget`/`encoding`** — exactly the
rule [B38]'s exporter already states and follows (`tools/export_rxt.py`
rule 5, "D93: a source's composed config wins over the command line — an
`engine` line in a set would pin the testee matrix from inside the
set"). This rule is not new to Option A; it is already load-bearing for
[B38]'s existing export and would bind identically if the direction of
authorship reversed.

**What changes in `subbench.py` / `make check` / the schema under Option
A**, concretely: `subbench.py` would need a new loader path parsing
`.rxt` (via `pcrec --list-source` for the head, our own reader for the
body's `name`/`description`/pattern-text lines only — no case lines,
since we do not use `.rxt`'s `m`/`n` vocabulary for our own
expectations, kept in a companion file per Option B below); `make
check-harness`'s existing round-trip gate ([B38]'s
`check_rxt_export`) would need to become a round-trip in BOTH
directions, or be replaced by a single-direction "the `.rxt` IS the
corpus, and the sidecar's derived `[[patterns]]` table matches it"
check, mirroring the shape `bench/syntax`'s own `gen_patterns.py --check`
already uses for its registry-derived table (`bench/syntax/CLAUDE.md`, the
`gen_patterns.py` row: "Writes `patterns/*.rx`... `--check` re-derives...
and checks the sidecar"). The record schema needs **no change**:
`patterns[].canonical_sha256`/`canonical_text` are already
format-agnostic (a hash and a text blob, `record_schema.md:1021-1022`),
and `subbench.source_ref` (optional, DIAGNOSTIC, `record_schema.md:891`)
is already the right place for a `.rxt` block citation
(`bench/<set>/patterns.rxt:name=w-256`) if wanted — nothing REQUIRES it.

### Option B — hybrid: `.rxt` holds patterns, a sidecar holds the rest

`.rxt` carries one block per pattern (`pattern`, `name`, `description`
only — no `target`/`config`, per the D93 rule above), human-authored and
committed as the canonical pattern text; a TOML/TSV sidecar (today's
`subbench.toml` shape, trimmed) carries subjects, expectations, tags,
hazard/size/tier, regime, variant, oracle method — keyed by the block's
`name`, which now doubles as `pattern_id` (both are the same slug-shaped
string once the name grammar is widened, §1.2).

**What changes**: `subbench.py`'s pattern loader reads `.rxt` blocks
instead of (or beside) `patterns/*.rx` files — a smaller change than
Option A, since the sidecar's shape is otherwise untouched. `make
check-harness` gains one new check (the sidecar's `[[patterns]].file`
field, or its replacement, matches a real `.rxt` block by `name`) —
structurally identical to the check `bench/syntax/gen_patterns.py
--check` already runs against ITS registry seed (`bench/syntax/CLAUDE.md`
`gen_patterns.py` row), so this is a known, already-practiced shape in
this repo, not a new kind of gate. **No schema change** (same reasoning
as Option A). **The per-engine variant question**: since `variant` (W3)
is not built, a per-engine spelling tweak stays exactly where it is
today — `[testees.<id>].variant` in the sidecar
(`record_schema.md:1026-1037`) — NOT in the `.rxt` file, until W3 lands;
the oracle binding for a variant is unaffected (the oracle checks the
CANONICAL text's expectations against the CANONICAL oracle, per
`format_design.md:1237-1241`, and a variant is checked for equivalence
against the same expectations — a rule this bench already implements at
`OD-B5`, `docs/design/requirements.md`: "no deviation grades — a variant
must reproduce the canonical results exactly").

This is, functionally, what `format_design.md` §4.5 already recommends
as the interim state, in its own words: *"What the bench must still own
... the record and its keys, the adapters, the reporter, and the
decision of when to move a sub-bench into the format. This note's
contribution is that when they do, the sidecar has somewhere to go"*
(`format_design.md:1903-1907`) — i.e. pcrec's own design note anticipates
a sidecar surviving beside a partial `.rxt` adoption, not disappearing on
day one.

### Option C — today's model kept, `.rxt` derived (status quo, [B29]'s recommendation)

Sidecar + generators stay the source; `tools/export_rxt.py` keeps
producing a DERIVED `.rxt` for pcrec's own consumption. **This is what
[B29] recommended in 2026-09-01 and it is not compatible with [B42]'s
charter as written** — item (4) states flatly "BUILT ON THE .rxt FILE
FORMAT," not "with an `.rxt` export available." Included here only so
the design note has the null option on record and can say explicitly why
it is rejected, rather than silently dropping it.

---

## 3. What pcrec's own harnesses do with `.rxt` — reusable vs not

- **`pcrec --list-source FILE`** is the reusable seam for the HEAD
  (§2 Option A above): a documented TSV, one row per head declaration and
  per pattern block, in file order (`rxt_format.md:411-450`). This repo
  already calls it, in the export→verify direction, from
  `tools/selfcheck.py`'s `check_rxt_export` ([B38]).
- **`tests/harness/run.sh` / `driver.c`** parse the BODY (case lines)
  themselves, in bash, and this is stated as permanent design, not a gap
  ("gains no head arms at all," `rxt_format.md:419-421`). Nothing here is
  reusable as a library — it is a shell script tied to pcrec's own build
  and driver ABI (`RX_NCAPS`, `<prefix>_search`), and it asserts
  expectations WE do not use (`m`/`n`/`g` are checked against a compiled
  pcrec artifact; this bench's expectations are checked per-testee by
  OUR adapters, `docs/design/harness_contract.md`).
- **`tests/harness/verify_rxt.py`** (the python-`re` oracle) is
  PCRE2-syntax-shaped but engine-generic in principle — it runs
  `compiled.search`/`match.span` against ordinary python `re`. Not
  wired to anything of ours today, and reusing it would mean depending
  on pcrec's own test tree as a runtime import, which the MANDATE (root
  `CLAUDE.md`, ~/pcrec READ-ONLY) does not forbid reading but this
  project's own oracle path (`pcrecbench/oracle_pcre2.py`) already covers
  the same ground independently. Not a clear win either way; flagged for
  the design note.
- **The corpus itself** (179 files / 3,265 blocks / 26,691 expectation
  lines as of 2026-08-29, `format_design.md:1512-1517`) is the asset
  R-BENCH-8 already names as an import source ("grows partly by import
  from pcrec's oracle-verified `.rxt` corpora"). Nothing in this note's
  scope required checking that import direction in depth; [B29]'s Q4
  flags it as the reverse of the name-legality problem (pcrec's C-identifier
  names import losslessly into a bench slug; not yet confirmed here).
- **`bench/syntax`'s own precedent is closer to reuse than `.rxt`
  itself**: it already imports FROM a pcrec registry surface
  (`--list-syntax`, archived as `list_syntax_9a1583ba.tsv`) as an
  authoring SEED, reading only `kind`/`syntax`/`status`/`family`
  (engine-neutral columns) and copying `module`/`engines`/`built` as
  inert provenance (`bench/syntax/CLAUDE.md`: "shape nothing (R-BENCH-4)").
  This is a real, already-shipped example of "take structure from pcrec's
  own tooling without becoming pcrec-shaped," and the capability-survey
  set's design note should look at it as a template for how a
  registry/format import can stay engine-neutral, independent of
  whatever `.rxt` itself resolves to.

---

## 4. Format asks — what pcrec would need to grant for Option A/B to be clean

Phrased as candidate outbox items; each states what we would do without
it.

1. **Ship W2's `@file:` subjects and `tag`.** Without it, subjects and
   per-case metadata (hazard/size/tier/regime) cannot live in `.rxt` at
   all under any option, and Option B's sidecar stays permanent rather
   than shrinking. `format_design.md`'s own Q5 already anticipates this
   exact ask: *"RECOMMENDED: ship W2 when the bench's 1,364-row
   expectation fragment needs it, and treat that set as the validating
   measurement"* (`:2482-2490`) — i.e. this ask is pre-approved in
   principle, contingent on us actually needing it, which [B42]'s charter
   now supplies as the trigger.
2. **Ship W3's `oracle`/`variant`/`use`/`testee`/`option`.** Without it,
   per-engine variants and the testee/config axis stay in the sidecar
   under any option; the format's own wave table already names
   pcrec-bench sub-benches with a non-pcrec testee as W3's consumer
   (`format_design.md:465`) — again a pre-named trigger, not a cold ask.
3. **A documented head-only reader mode for the descriptive productions**
   (parallel to `--list-source`, or an extension of it) once W2/W3 land,
   so a bench-side loader can keep shelling out rather than growing a
   second body-line parser for `tag`/`variant`/`oracle`. Without it,
   Option A's loader must parse those lines itself once they exist,
   which is a smaller but real re-implementation risk of the same shape
   `--list-source` was built to avoid for the head.
4. **Confirmation that a hand-authored `.rxt` with no `target`/`config`
   lines is a legitimate, permanent shape** (not merely a today-only
   absence pending some future requirement that every file declare a
   target) — i.e. that `name`-only, target-less blocks are not an
   anti-pattern pcrec's own tooling will one day warn about. Without it,
   we would design around an assumption that might be wrong; this is a
   confirmation ask, not a feature ask.

None of these four is a blocking ask for [B42]'s design pass — (1) and
(2) are pre-named triggers in pcrec's own document, and (3)/(4) are
questions, not requests for new work.

---

## 5. Risk list

- **Format churn while the set is being built.** §0 shows the format
  static over the last five days at the CURRENT pin, but W2/W3 landing
  mid-build would change the file shape underfoot — the same risk
  [B29]'s Q5 named and the reason its own recommendation was to wait.
  Mitigated for [B42] only if the design commits to Option B (sidecar
  survives W2/W3 landing unchanged; only the loader's SOURCE for
  pattern text moves).
- **The free_text cap (schema v1.5, 1 MiB, `record_schema.md:298-299`,
  KB-7).** `patterns[].canonical_text` is capped; nothing in `.rxt`
  itself imposes a size limit on a pattern LINE (rest-of-line, verbatim),
  so a pathologically large single pattern (unlikely for a capability
  survey, plausible for an adversarial one) would hit the record's own
  cap before `.rxt`'s. Not new — this is already true of the `.rx` files
  today.
- **Multi-line patterns**: `.rxt`'s `pattern` production is one line, no
  continuation (`rxt_format.md:192-195`, "pattern takes exactly one SPACE
  before its regex... rest-of-line"). A pattern with an embedded newline
  (e.g. `(?x)` free-spacing mode authored across lines) has NO
  representation in a single `pattern` line and would need to be written
  with `\n` inside quotes — except `pattern` text is UNQUOTED and
  UNESCAPED (`rxt_format.md:210-212`), so there is in fact no way to
  express a literal newline inside a `pattern` line at all. [B38]'s
  exporter already found and documented this exact gap for subjects (a
  literal-newline subject "has no representation... refused BY NAME
  rather than silently mangled," `tools/export_rxt.py` rule 6) but the
  SAME gap applies to the pattern text itself and is worth stating
  separately: **a capability-survey pattern using free-spacing mode
  across multiple lines cannot be written in `.rxt` at all**, under any
  option, without a design change on pcrec's side. Flagged for [B42]'s
  design note; not surveyed further here (no such pattern exists in this
  repo's corpus today, so it is a forward risk, not a current blocker).
- **Non-ASCII/binary patterns and subjects.** `.rx` files are raw bytes,
  read without decoding (`pcrecbench/subbench.py:190-194`,
  `subbench_directory_model.md:71-74`); `.rxt`'s `pattern` line is
  likewise raw rest-of-line bytes with NO escaping (confirmed by [B38],
  §1.2 above) — so a raw non-ASCII pattern byte round-trips losslessly.
  A raw NUL byte in a `pattern` line, however, would truncate at the
  line boundary only if the LINE-reading layer treats it as a
  terminator; this was not independently verified against pcrec's own
  `.rxt` line reader in this note's scope (out of time budget) and
  should be checked before [B42] commits to `.rxt` for any pattern that
  might carry one — capability-survey patterns are unlikely to need a
  literal NUL, so this is a low-probability, unverified risk rather than
  a known gap.
- **Name/target collisions ([B38] rule 3).** Already handled: `floor` is
  the one recorded cross-set collision, avoided by per-set export
  (§1.2). A capability-survey set drawing pattern ids from a wide net
  (many engines' documented feature names) has more surface for an
  accidental within-set collision (two constructs both deriving the
  prefix `x_y` from `x-y` and `x.y`) than the existing four/five sets —
  worth a check at authoring time, not a structural blocker.

---

## 6. Questions for Frank

Frank's ruling picks the option; this note recommends but does not
decide.

**Recommendation: Option B (hybrid), not A.** The charter's requirement
(4) is satisfied by making `.rxt` the canonical home of PATTERN TEXT —
the part of a set `.rxt` can express losslessly and engine-neutrally
today (§1.2, §2 Option A's engine-neutrality analysis) — while keeping
everything `.rxt` cannot yet express (subjects, expectations, tags,
hazard/size/tier, regime, oracle method, variants) in a sidecar exactly
as today, keyed by the `.rxt` block's `name`. This is not a compromise
invented for this note: it is what pcrec's OWN design note already
expects to happen (`format_design.md:1903-1907`, quoted in §2), it costs
nothing when W2/W3 eventually land (the sidecar's non-pattern fields
migrate into `tag`/`oracle`/`variant` lines one field at a time, exactly
as `format_design.md` §4.5's field-by-field table already works out for
`bench/loglines`), and it avoids two live hazards Option A cannot avoid
today: (a) writing a second, uncontrolled parser for keywords pcrec has
not shipped (the collision risk named in §2), and (b) the D93 hazard of
letting a pcrec build declaration (`config`/`target`) leak into a file
this bench treats as its engine-neutral source, which stays possible
under Option A (a `.rxt`-native loader is more tempting to also use for
building) and is structurally avoided under Option B (the file we author
never needs a `target`/`config` line at all, since we do not compile
FROM it — [B38]'s existing export, unchanged, keeps serving that need for
pcrec's own consumption). Option C is foreclosed by the charter as
written.

1. Is Option B's reading of requirement (4) — "`.rxt` is the source of
   pattern text and identity; a sidecar is the source of everything
   else, migrating field by field as W2/W3 land" — an acceptable
   satisfaction of "BUILT ON THE .rxt FILE FORMAT," or does the charter
   intend something closer to Option A (no sidecar surviving day one)?
2. Should the design note file the two W2/W3 asks (§4 items 1-2) to
   pcrec now, given `format_design.md` already names this bench's own
   needs as W2/W3's triggers — or wait until the design note's shape is
   itself settled, so the ask is concrete rather than speculative?
3. Is a `target`-less, `config`-less `.rxt` (Option B's shape) an
   acceptable long-term form, or does Frank want the capability-survey
   set ALSO buildable by pcrec's own `--source` from day one (which would
   require targets, and would re-open [B29]'s §4.1 compile-cost-axis
   objection — one `--source` build cannot fill N per-pattern
   `compile_row`s without an invented attribution)?
