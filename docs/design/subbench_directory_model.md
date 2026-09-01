# The sub-bench directory model against pcrec's `--source` — a scoping note

**[B29], 2026-09-01. DESIGN NOTE ONLY: no code, no schema change, no
sidecar change.** Chartered by inbox I-29 item 8 as OPTIONAL work: scope
the sub-bench DIRECTORY model's pcrec half against pcrec's new
`--source` / `--target` / `--lib-path` ([DD-13b.W1.2]), and say what it
buys, what it costs, and what should be done about it.

Every claim below is cited to a `file:line` in this repo or to a section
of a pcrec spec document. pcrec is READ-ONLY from here (root `CLAUDE.md`,
BD2); every pcrec citation was read with `git show`.

## 0. The pin the brief named, and the three corrections it needs

The brief described W1.2 as "merging to pcrec main tonight as abi 15",
on branch `lane/w12` (head `d03bcaa`). Verified against the tree:

1. **It has already merged.** `lane/w12` merged to pcrec `main` as
   `6dbdf41`, followed by `81fb773` ("codegen: re-pin identity gate (B)
   to the w12 merge 6dbdf41 — abi 15, D94 site list moved by grep"),
   which is `main`'s head. The merged text, not the lane branch, is what
   this bench would pin, so this note cites `main` wherever the two
   agree and says so where they do not. On every document this note
   cites, the two agree line for line.
2. **abi 15 is right, and it was 14 on the lane.** `lane/w12` stamps
   `.abi = 14` (`src/gen/emit_dfa.c:1476` on the lane); `main` stamps
   `.abi = 15` (`src/gen/emit_dfa.c:1514`). The lane's own report said
   the manager assigns the final number at merge because other lanes
   carry bumps (`docs/dev/lanes/w12_report.md` §4). **14 went to
   [CC-CLANG]** (`docs/spec/match_api.md:1650`) — the very change
   `testees/pcrec/configs.toml:110` already anticipates by name, as the
   fix that will turn this bench's clang `did-not-compile` rows into
   numbers. So the next pcrec re-pin crosses TWO abi bumps at once, and
   the clang refusals and the `--source` surface arrive together.
3. **D93 exists and is ratified.** The brief called file-wins-over-flag
   "D93"; on `lane/w12` no such decision existed (`docs/dev/decisions.md`
   ends at D92) and the lane listed it as a call the manager might
   reverse (`docs/dev/lanes/w12_report.md` §3.2). On `main` it is
   ratified by Frank the same day: `docs/dev/decisions.md:6428`, D93 —
   "a `.rxt` source's composed config wins over a command-line flag on
   the same axis". §4.4 below is about what that costs this bench.

None of the three changes the recommendation. All three change what a
re-pin lane would have to check, so they are recorded here rather than
left for that lane to rediscover.

---

## 1. What the bench's directory model IS today

### 1.1 The directory

A sub-bench is a self-contained directory
(`docs/design/requirements.md:212-221`; the layout is
`docs/design/harness_contract.md:22-39`): the sidecar `subbench.toml`,
one `patterns/<name>.rx` per canonical pattern in PCRE2 spelling as raw
bytes, a deterministic `gen_subjects.py` writing a gitignored
`subjects/` tree plus a committed `manifest.tsv`, the same pair again for
the large `throughput/` tree, `gen_expectations.py` and a committed
`expectations.tsv` carrying a verification method per row, a `NOTES.md`
of per-engine notes and declared variants, and a `CLAUDE.md`.

Four exist: `bench/email/`, `bench/loglines/`, `bench/bounded/`,
`bench/altwide/`.

Two properties of the pattern files matter to everything below, and both
were measured for this note rather than assumed:

- **No `.rx` file contains a newline.** All 77 pattern files across the
  four sub-benches are single-line, and none carries a trailing newline.
- **All 77 are pure ASCII with no tab.** The `pattern_bytes` accessor
  reads the whole file as RAW BYTES and never decodes it
  (`pcrecbench/subbench.py:190-194`), precisely because the specimen's
  classes were expected to carry non-UTF-8 bytes; today none does.

### 1.2 The sidecar, and the rule that governs it

`subbench.toml` carries exactly the fields requirements §5 names, listed
at `docs/design/harness_contract.md:41-55`: `id`, `version`, `objective`
+ `objective_kind`, `description`, `regimes`, an array of
`[[patterns]]` (name, file, feature tier, hazard class, size class,
convention, tags, role), `[subjects]` (generator, manifest, the
throughput pair, `short_search_max_bytes`), `[expectations]` (file,
default method), and optional `[testees.<id>]` sections carrying
`variant`, `variant_kind`, `objective_preserved`, `capture_map`,
`options` and `unsupported`. The contract closes the list: "Nothing
else; a new field is a design change" (`:54-55`). The sidecar's own
header states the position: "Fields only, no grammar, no directives, no
includes -- [DD-13]'s territory is deliberately untouched, so the
unified format absorbs this mechanically when it lands"
(`bench/bounded/subbench.toml:1-4`, `bench/altwide/subbench.toml:1-4`).

That is Frank's narrow blocking ruling of 2026-08-25
(`docs/design/requirements.md:244-263`). BLOCKED is authoring cases in a
new cross-sub-bench grammar. NOT blocked is the directory model itself,
the record, the adapters, the reporter, parsing today's `.rxt` as-is, and
a plain sidecar of fields.

### 1.3 What the record carries out of it

The record's setup layer carries a `subbench` block of exactly five
required fields plus one optional — `id`, `version`, `content_hash`,
`objective`, `regimes`, `source_ref`
(`schema/record.schema.json:388-403`) — and a `patterns[]` array whose
entries are `pattern_id`, `canonical_sha256`, optional `canonical_text`,
`hazard_class`, `size_class`, `tags`, `variant`, `role`
(`schema/record.schema.json`, `$defs.pattern_entry`).

`content_hash` is a sha256 over every COMMITTED file in the directory,
path-sorted and path-prefixed, generated trees excluded
(`pcrecbench/subbench.py:235-260`). Any file added to a sub-bench
directory — an exported `.rxt` included — changes it, and records
compare only within one sub-bench version
(`docs/design/requirements.md:230-232`).

`pattern_id` is a `slug`: `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`
(`schema/record.schema.json:20-24`). Hyphens are legal and used
everywhere. §3.3 shows why that one line is the sharpest obstacle in
this whole note.

### 1.4 What R-BENCH-1..9 asked of the unified format

pcrec's `docs/design/dd13_format/requirements.md` §5 states this
project's needs, evidenced from APPROACH.md and Frank's inputs
(`:316-411`). In one line each:

| id | the ask | where it lives in the sidecar today |
|---|---|---|
| R-BENCH-1 | per-CASE feature tier, hazard class, size class, verification method | `[[patterns]]` four fields + `[expectations].default_method` |
| R-BENCH-2 | a section keyed per TESTEE holding what to include and which options to apply | `[testees.<id>]` |
| R-BENCH-3 | first-class "unsupported by this testee", counted, never silent | `[testees.<id>].unsupported` + the record's `unsupported-by-declaration` outcome |
| R-BENCH-4 | expectations strong enough to adjudicate correctness, and NOT pcrec-shaped | `expectations.tsv` + its method column |
| R-BENCH-5 | a per-CASE matching-convention tag | `[[patterns]].convention` |
| R-BENCH-6 | subjects by REFERENCE, not inline strings — corpora are large | `[subjects]` generator + manifest, and a `throughput/` tree |
| R-BENCH-7 | per-library pattern tweaks DECLARED and impossible to miss | `[testees.<id>].variant` + `variant_kind` + `objective_preserved` |
| R-BENCH-8 | import from pcrec's oracle-verified `.rxt` corpora | not exercised yet; the `.rx` files are hand-authored or copied |
| R-BENCH-9 | the same section concept serves pcrec's own multi-config builds | `[testees.<id>]` is the bench half of it |

Every one of the nine is answered today by a sidecar field. That is the
baseline any format proposal has to beat.

---

## 2. What W1.2 delivers

Precisely, from `main` (identical on `lane/w12`).

### 2.1 The `.rxt` head — four declarations

`docs/spec/rxt_format.md:41-62`. A `.rxt` file has a HEAD and a BODY; the
head ends at the first `pattern` line and nothing file-level may appear
after it (`:25-31`). Four head declarations exist: `lib "path"` (a
subpattern library, resolved as far as EXISTENCE only — contents never
read, so no pattern can call a definition inside it; `lib <store>`
refused as not in this build, `:47`); `target <prefix> = <definition>
[with <c1,c2>]`, **BUILT** since W1.2 (`:48`); `config <name> [from
<c1,c2>]` with an indented body of `pcrec` / `flags` / `features` /
`encoding` / `engine` / `budget` lines (`:49`, `:52-55`); and
`description <text>`, a machine-readable prose FIELD rather than a
comment (`:50`).

**Everything a later wave owns is refused BY NAME, as not in this
build**: `include`, `tag`, `freq`, `use`, `oracle`, `analysis`, `testee`,
`option`, `mc`, `variant` (`:57-62`). That list is worth reading twice —
it is very nearly the list of things the bench sidecar carries.

### 2.2 `--source`, `--target`, `--lib-path`

`docs/spec/cli.md:252-350`.

`pcrec --source FILE -o OUT` compiles the file's `target` declarations.
It is a COMPILE MODE, honours every compile flag, and writes artifacts
(`:254-256`). **It takes no pattern argument** and cannot be composed
with any query surface (`:258-261`).

- **Which artifacts get built**: the `target` lines in file order, one
  artifact each; or, with no `target` and exactly ONE UNNAMED pattern
  block, the implicit `target rx`. A file with no `target` and anything
  else **builds NOTHING** at exit 0 — a library ships nothing by itself,
  and that is a different observable from a refusal (`:263-270`).
- **`-o` has three forms chosen by the SHAPE of its value** (`:278-291`):
  an existing DIRECTORY gives `<dir>/<prefix>.c` and `.h` per target, any
  number of targets; any other name gives that one `.c` plus its `.h`,
  exactly one target; `-` gives one self-contained `.c` on stdout,
  exactly one. `-o FILE` with several targets is REFUSED. **Each target
  is a separate compile writing its own translation unit** — "there is no
  code path that could produce a multi-artifact TU (D88)" (`:289-291`).
- **`--target NAME`** builds only the target with that PREFIX (`:293`).
  **`--lib-path DIR`** is repeatable and order-significant, the one
  accumulating flag in the CLI; both apply to `--source` alone
  (`:297-304`).

### 2.3 Composition, and D93

Two mechanisms, not one rule at two scales (`docs/spec/cli.md:306-319`):
`with c1, c2` composes CONFIGS by a flat LATER-WINS rule, and the
resulting config then composes against the pattern block's own directives
BY KIND — `features` is the UNION of the two unless the block wrote
`features only`, and `flags`, `encoding`, `engine`, `budget` are
MORE-SPECIFIC-WINS, i.e. the block.

**THE FILE WINS OVER THE COMMAND LINE, on the axes the target actually
speaks about, and only those** (`docs/spec/cli.md:321-336`; ratified as
pcrec D93, `docs/dev/decisions.md:6428`). A flag on an axis the file does
not set reaches the compile untouched. Frank's framing in the decision:
treat `.rxt` files like C source files — "you wouldn't change a C
function name via cli options".

### 2.4 `rx_info.name`, `nentries`, abi 15

`docs/spec/match_api.md:1407-1453`. Two members appended to `struct
rx_info`, no existing offset moved:

- `name` — the block's `name`, or the artifact's own `<prefix>` when the
  block is unnamed. **Never NULL, as a contract**, so every artifact
  pcrec ever emitted carries one. It answers a different question from
  `prefix`: `<prefix>` says what the symbols are called, `name` says what
  the artifact IS, so one definition built under three configs is three
  artifacts, three prefixes and ONE name (`:1420-1441`).
- `nentries` — rows in `groups[]`, ALL of them, where `nnames` counts
  only the primary pattern's own. **Equal on every artifact pcrec emits
  today**; what will make them differ is `.rxt` composition injecting a
  definition's named groups, which is W1.3 (`:1442-1453`).

`rx_info.abi` is 15 on `main` (`:1647`).

### 2.5 What W1.2 does NOT deliver, and where the bench's needs sit

The format's own wave table
(`docs/design/dd13_format/format_design.md:459-465`) assigns:

| wave | productions | who is waiting |
|---|---|---|
| W1 | `name`, `description`, `lib`, `target … with`, `encoding`, `features only`, `config`, composition, `rx_info.name` | [LIB]; [DD-14]'s multi-pattern files |
| W2 | `include`, `@file:` subjects, `mc`, `tag`, the `freq` block, `config`'s `analysis` | [ENG-PGO]; **"the first in-format sub-bench"** |
| W3 | `use`, `oracle`, `variant`, `config`'s `testee` / `option` | **"pcrec-bench sub-benches with a non-pcrec testee"** |

The format itself names the bench's own arrival at W2 and W3. W1.2 is a
BUILD surface; the bench's sidecar is a DESCRIPTION surface, and the
descriptive productions are two waves away. `[DD-13b.W1]` is
`STATE:started` on pcrec's plan (W1.3 and W1.4 remain); W2 and W3 are
unchartered.

---

## 3. The mapping

### 3.1 Sidecar field → `.rxt` counterpart

| sidecar field | `.rxt` counterpart today | wave |
|---|---|---|
| `id` | none (a file has no id; the filename is it) | — |
| `version` | none | — |
| `objective`, `description` | head `description <text>`, block scalar form (`rxt_format.md:50`, `:149-156`) | W1, LANDED |
| `objective_kind` | none | — |
| `regimes` | none | — |
| `[[patterns]].name` | block `name <ident>` (`rxt_format.md:231-235`) | W1, LANDED — **but see §3.3** |
| `[[patterns]].file` | the `pattern <regex>` line itself, inline (`:163-165`) | W1 |
| `[[patterns]].tags` | `tag` — **refused by name, not in this build** (`:57-62`) | W2 |
| `feature_tier`, `hazard_class`, `size_class`, `convention`, `role` | no counterpart; all four are R-BENCH-1/5 asks and none has a production in any wave table | unassigned |
| `[subjects]` generator + manifest | `@file:` subject references | W2 |
| `[expectations].file` / `default_method` | `oracle` — refused by name | W3 |
| `[testees.<id>]` options | `config`'s `testee` / `option` lines — refused by name | W3 |
| `[testees.<id>].variant` | `variant` — refused by name | W3 |
| `[testees.<id>].unsupported` | none (R-BENCH-3) | unassigned |
| `short_search_max_bytes` | none | — |
| — | head `target <prefix> = <def> [with …]` | no sidecar counterpart: the bench has no notion of a symbol prefix in the set |
| — | head `lib` / `config` | no sidecar counterpart; §4.4 argues the bench must never write `config` |

**Seven sidecar concepts have no counterpart in any pcrec wave table**:
`objective_kind`, `regimes`, the four per-pattern tag fields
(`feature_tier`, `hazard_class`, `size_class`, `convention`), `role`,
`short_search_max_bytes`, and the declared-unsupported field. Some fold
naturally into a general `tag` (W2); `role = floor`, `regimes` and the
byte cap do not — they are harness semantics, not case metadata.

### 3.2 Could a bench pattern set be EMITTED as one `.rxt` source?

**The pattern TEXT: yes, byte for byte, and that is measured.** A
`pattern` line takes exactly one space and then rest-of-line verbatim to
the end of the line, no quoting and no escaping
(`docs/spec/rxt_format.md:145-148`, `:163-165`). All 77 `.rx` files are
single-line with no trailing newline (§1.1), so `"pattern " + bytes` is a
lossless encoding and `pattern_bytes()`'s raw-bytes contract survives it.

The one case that tests the rule is `bench/altwide/patterns/floor.rx`,
whose entire content is the single byte `#`. Comments are whole-line
only, and "a `#` anywhere but column 1 is data"
(`docs/spec/rxt_format.md:102-104`), so `pattern #` is a pattern, not a
comment. The rule holds, exactly.

**Multi-pattern files: they build TODAY.** A file with N pattern blocks
and N `target` lines produces N artifacts under `-o <dir>`
(`docs/spec/cli.md:280-284`). The brief's "multi-pattern files are
[DD-14]" refers to the corpus files that carry several patterns
referencing EACH OTHER; cross-block subroutine composition is W1.3 and
is not landed. Nothing the bench needs depends on composition — the
bench's patterns are independent by construction.

**The names: no.** A block `name <ident>` must be a PCRE2 group name AND
a C identifier — first byte a letter or `_`, then letters, digits or `_`
(`docs/spec/rxt_format.md:231-235`) — and a `target`'s `<prefix>` is a C
symbol prefix. The bench's pattern names are slugs with hyphens
(`schema/record.schema.json:20-24`). Counted for this note:

| sub-bench | patterns | names illegal as a C identifier |
|---|---|---|
| altwide | 20 | 19 |
| bounded | 43 | 38 |
| email | 3 | 0 |
| loglines | 11 | 6 |
| **total** | **77** | **63** |

So 63 of 77 pattern names cannot be written as a `.rxt` block name at
all. `w-8`, `cls-upto-1024`, `pw-8-64`, `iso-ts`, `http-5xx` are all
illegal. An exporter must therefore carry a NAME MAP (`cls_upto_1024` ↔
`cls-upto-1024`), and the moment it does, `rx_info.name` stops being the
bench's `pattern_id` and becomes a third name for the same thing. That
is a real cost and it is the reason §5 does not recommend adoption.

### 3.3 What the pcrec adapter would do differently

Today the adapter runs **one `pcrec` exec per (pattern, form, trial)**.
`compile()` builds TWO artifacts per pattern — `plain` and
`whole-subject`, the latter from `(?:<pattern>)\z` because pcrec has no
end-anchored generation axis (`testees/pcrec/adapter.py:1497-1520`,
`docs/design/harness_contract.md:75-84`) — and `_compile_one` loops the
trials, each building its own `artifact-<trial>.so` because the dynamic
loader caches by path and a reused path would measure the cache
(`testees/pcrec/adapter.py:59-61`). The exec is
`[pcrec, "-p", "rx"] + flags + ["-o", art_c, "--", pattern]`
(`:1551-1552`).

Three phases are timed separately (`:51-57`, requirements §3 at
`docs/design/requirements.md:76-88`): `emit-c` (the CLI), `gcc` (the
shim, which `#include`s the artifact, into a `.so`), `load` (the dlopen,
timed inside the driver).

Under `--source` the adapter would change in four ways:

1. **Only `emit-c` batches.** D88 means N targets are N separate
   translation units (`docs/spec/cli.md:289-291`), so `gcc` and `load`
   stay strictly per artifact. One process call would cover N patterns'
   emit-c and nothing else.
2. **The prefix stops being `rx`.** `shim.c` hard-codes it —
   `#define PB_SEARCH rx_search`, `PB_MATCH_CAPS rx_match_caps`,
   `PB_INFO rx_info` (`testees/pcrec/shim.c:164-176`) — and the adapter
   always passes `-p rx` (`adapter.py:1551`). Under `-o <dir>` every
   target gets its OWN prefix and duplicate prefixes are refused
   (`docs/design/dd13_format/format_design.md` §2.7), so the shim would
   have to become prefix-parametric: a `-DPB_PREFIX=` build, i.e. a new
   token-pasting layer in the one file whose job is to be trivially
   readable against `struct rx_info`.
3. **The whole-subject form doubles the file.** The `\z` text is derived
   bench-side (`adapter.py:1499-1516`), so an exported `.rxt` would need
   2N blocks and would then encode a bench-side derivation into a file
   pcrec reads — or drop the match regime from the exported form.
4. **`testee_id` and the pin are unaffected.** The testee is still an
   (engine, version, configuration) triple
   (`docs/design/requirements.md:108-123`); `--source` is a different
   invocation of the same pinned binary, not a new testee. A `--source`
   compile mode would be an ADAPTER-internal choice, which is exactly
   where an engine-shaped thing belongs.

---

## 4. What this buys the bench, and what it costs

### 4.1 The compile-cost axis the bench cannot give up

Requirements §3 is unambiguous: compile/setup cost is its own axis, never
folded into match time, and it is a MEDIAN OF N WITH SPREAD like every
other quantity (`docs/design/requirements.md:76-88`). The record enforces
it structurally: `compile_row` is keyed `pattern_id` × `trial` × `form`
(`schema/record.schema.json:642-650`), and rule X27 refuses a
whole-subject match row without its own whole-subject compile row
(`schema/validate.py:596-609`).

A single `--source` build of N targets produces ONE wall clock. There is
no per-target timing in the CLI contract, and splitting one number across
N patterns would be an invented attribution — the exact thing "never
folded" forbids.

And the phase that would be batched is the one carrying the signal.
Measured in this project's own ledgers:

| cell | total | gcc | emit-c |
|---|---|---|---|
| `cls-upto-8192` whole-subject | 9,034.5 ms | 309.4 ms | ≈ 8.72 s |

`docs/dev/ledgers/2026-08-31-opt41-after-263b013.md:313`; the same
ledger's §3 puts the K7 subset walk at 1.8-1.9 s against a forced-VM
emit-c of 1.4-4.2 ms (`:318`), and the abi-12 ledger states the ratio
plainly — "×28.6, so gcc is still not the cost"
(`docs/dev/ledgers/2026-08-30-abi12-after-96e44c2.md:314`).

`bench/bounded` and `bench/altwide` exist to sweep exactly this: the
count at which an engine refuses, and the width at which it does
(`bench/bounded/subbench.toml:9-18`,
`bench/altwide/subbench.toml:9-18`). Batching emit-c across a set would
collapse the axis those two sub-benches were built to measure. **This is
the decisive cost, and it is not negotiable by design taste.**

### 4.2 What it does buy

Three things, all real but none urgent. **`rx_info.name`** gives an
artifact a self-declared identity readable without knowing the prefix
(`docs/spec/match_api.md:1420-1441`) — provenance rather than
capability, since the bench already knows what it compiled. **A `.rxt`
export would be a consumer artifact pcrec can use**: pcrec could build
this corpus with one command for its own acceptance surveys, replacing
the [ART-SIZE] bench-acceptance probe's ad hoc pattern list
(`docs/dev/pcrec_references.md`, the [ART-SIZE] row) with a file the
bench maintains. And **R-BENCH-8's import direction gets a proven
encoding**: §3.2 shows the `.rx` ↔ `pattern`-line encoding is lossless
in this corpus, which is the first half of importing pcrec `.rxt` cases
INTO a sub-bench.

### 4.3 Does W1.2 change the "fields only, no grammar" position?

**No, and it slightly strengthens it.** The ruled scope permits a plain
sidecar whose fields are "exactly R-BENCH-1..9 plus this note's
additions, no directives, no grammar, so [DD-13] absorbs them
mechanically when it lands" (`docs/design/requirements.md:257-261`).
W1.2 landed a BUILD grammar — `target`, `config`, `with`, `from`, `lib`
— and explicitly refused every DESCRIPTIVE keyword the sidecar would need
(`tag`, `oracle`, `variant`, `testee`, `option`, `@file:` subjects), by
name (`docs/spec/rxt_format.md:57-62`), while the wave table names the
bench itself as W2's and W3's waiting consumer
(`format_design.md:464-465`). The thing the sidecar holds a place for has
not arrived; what arrived is orthogonal to it.

### 4.4 Engine neutrality, and a sharp consequence of D93

R-BENCH-4 and requirements §4.2 both bind: the record schema stays
engine-neutral, pcrec's artifact is "one more file in the pile"
(`docs/design/requirements.md:108-123`). Nothing pcrec-shaped may enter
`subbench.toml` — no `target`, no `config`, no prefix, no `.rxt` path as
a first-class sidecar field.

D93 makes this sharper than it looks. If an exported bench `.rxt` carried
a `config` block, the FILE would beat the adapter's command line on every
axis it names (`docs/spec/cli.md:321-336`). The pcrec testee matrix is
built from command-line flags — `--engine=vm`, `--no-captures`,
`--features all` (`testees/pcrec/configs.toml:74-89`) — and the testee
axis is the bench's own first-class dimension (§4.2). A `config` in the
set file that named `engine` would silently pin every testee to one
engine, because `engine` composes more-specific-wins.

**Rule for any exporter, stated now so it is not rediscovered later: a
bench-exported `.rxt` declares NO `config` and NO block-level `flags`,
`engine`, `budget` or `encoding` directive.** `features` alone would be
safe, because it composes as a UNION (`docs/spec/cli.md:311-314`), but
there is no reason to write it either: `--features all` is already on
every pcrec testee config.

---

## 5. Recommendation

Three options were considered. **Option A now, Option B on an ask,
Option C not before W3.**

### Option A — do nothing until the descriptive waves land (RECOMMENDED)

Keep the sidecar exactly as it is, keep the adapter's one-exec-per-
pattern compile, and revisit when W2 (`tag`, `@file:`) or W3 (`oracle`,
`variant`, `testee`) is chartered in pcrec.

- **Why**: the compile-cost axis (§4.1) rules out `--source` as the
  bench's compile path regardless of anything else, and the sidecar's
  seven unmapped concepts (§3.1) mean the format cannot absorb the
  directory model yet. The blocking ruling already says exactly this and
  nothing in W1.2 disturbs it (§4.3).
- **Cost**: none. The 63-of-77 name problem (§3.3) and the D93 config
  rule (§4.4) are recorded here so a future lane does not re-derive
  them.
- **Ruling it needs**: this manager's, to file the note and leave [B29]
  closed. No Frank ruling and no pcrec ask.

### Option B — an OPTIONAL exporter, `bench/<set>/ → <set>.rxt`

A script (`tools/export_rxt.py` or a per-set `gen_rxt.py`) emitting one
`.rxt` per sub-bench as a pcrec-side CONSUMER artifact: head
`description`, one `pattern` block per canonical pattern with a
name-mapped `name` and a one-line `description`, and one `target` line
per block. **No harness change, no adapter change, no sidecar change**;
the harness never reads the file.

- **Why**: it gives pcrec a one-command build of this bench's corpus for
  its own acceptance surveys (§4.2), and it is the natural place to
  prove the §3.2 encoding stays lossless as sets grow.
- **Cost**: an exported file placed IN the sub-bench directory changes
  `subbench.content_hash` (`pcrecbench/subbench.py:235-260`) and so
  forces a version bump — a deliberate, logged event
  (`docs/design/requirements.md:230-232`) invalidating cross-version
  comparison for every set it touches. **Mitigation: emit under
  `build/` or `tools/`, never into `bench/<set>/`**, which keeps the
  hash and the store intact at no cost. Separately, the name map is a
  third naming of every pattern (§3.3) and must be generated.
- **Rulings it needs**: (a) the pcrec manager, on whether pcrec actually
  wants this artifact — it is worth building only if there is a consumer;
  (b) this manager, on the emit location, if (a) is yes. **Do not build
  it speculatively**: D77's "nothing is built to be ready" applies here.

### Option C — adopt `--source` in the adapter as a second compile mode

A `pcrec-source` testee compiling the whole set in one `--source -o <dir>`
call beside the per-pattern one.

- **Why it is tempting**: it measures a real user's build path, and a
  "whole-set build cost" is a genuine quantity.
- **Why not now**: it cannot fill the record. One clock for N targets
  cannot produce N `compile_row`s without an invented attribution, and
  the folding prohibition is a requirement, not a preference (§4.1). It
  also needs a prefix-parametric shim (§3.3 item 2), 2N blocks for the
  whole-subject form (item 3), the name map (§3.3), and a new record
  shape — a per-SET compile row, i.e. a schema change ([B2]'s
  territory) — for a number no current pcrec plan row asks for.
- **Rulings it needs, in order**: Frank, on whether a whole-set build
  cost is a quantity this bench should carry at all; then the schema
  question; then pcrec, on per-target timing in `--source` (Q3). **Not
  worth opening until W3 gives the format the descriptive half**, since
  until then the exported file cannot carry a testee section anyway.

---

## 6. Open questions

**Q1 — Does the `set_format.md` slot survive?** `docs/design/CLAUDE.md`
lists `set_format.md` as an expected next resident: "the bench set format
position: what this project needs from pcrec's [DD-13] unified format
(R-BENCH-1..9) and what it uses in the interim". This note answers a
narrower question (the pcrec half of the directory model against W1.2)
and does not replace it. *Needs: this manager — either keep both slots,
or fold the planned `set_format.md` into a later revision of this file.*

**Q2 — Should the bench send W1.2 findings to pcrec as an outbox item?**
Three findings here are useful on pcrec's side: the 63-of-77 name-
legality count against a real consumer corpus, the D93-plus-testee-matrix
interaction (§4.4), and the fact that the format's own wave table names
pcrec-bench as W2's and W3's waiting consumer while the bench has now
shipped four sub-benches without them. *Needs: this manager, on whether
an outbox item is warranted; the pcrec manager receives it.*

**Q3 — Would pcrec add per-target timing to `--source`?** The bench
cannot use `--source` for compile-cost measurement without it (§4.1). It
is a small surface (a per-target elapsed line on stderr, or a `--timing`
TSV under the `table_contract.md` rules), and it would make Option C
merely expensive instead of impossible. *Needs: the pcrec manager. Ask
only if this manager wants Option C on the table at all — this note
recommends not asking yet.*

**Q4 — Does the block-name identifier rule bind an importer too?**
R-BENCH-8's import direction (pcrec `.rxt` → a bench sub-bench) inherits
the reverse problem: pcrec block names are C identifiers, bench
`pattern_id`s are slugs, and `foo_bar` is a legal slug so the import
direction is lossless where the export direction is not. Worth
confirming before any import work. *Needs: no ruling; a check at the
time.*

**Q5 — Which re-pin lane absorbs abi 14 AND 15?** The next pcrec re-pin
crosses two bumps: [CC-CLANG] (14), which turns this bench's clang
`did-not-compile` rows into numbers exactly as
`testees/pcrec/configs.toml:100-111` predicts, and W1.2 (15), which adds
`rx_info.name` and `nentries` to `struct rx_info` and therefore touches
`testees/pcrec/shim.c`'s reflection block. The clang half is a MEASURED
prediction this bench wrote down in advance and can now check by value.
*Needs: this manager, when scheduling the re-pin row.*

**Q6 — Is `rx_info.name` worth reading at that re-pin?** It is never
NULL, and on every artifact this bench builds it would read `"rx"` (the
prefix, since the adapter passes `-p rx` and no `.rxt` name exists). A
stamp whose value is constant across the whole corpus is a weak metadata
pair, and requirements §4.2 wants pairs that BUCKET outliers. *Needs:
this manager. The honest answer is probably "read it, assert it equals
the prefix, and do not record it as a pair".*
