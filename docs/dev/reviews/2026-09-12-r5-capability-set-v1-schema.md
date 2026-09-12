# R5 critic panel — `capability_set_v1.md`, the SCHEMA / HARNESS / REPORTER / .rxt CONSISTENCY lens

Reviewer: read-only critic lane `r5critic-schema`, 2026-09-12. Target:
`docs/design/capability_set_v1.md` v0.1 "draft for panel" (1,361 lines,
[B42] phase (b), merged 08b1815). Grounding read: `schema/record.schema.json`,
`schema/validate.py`, `docs/design/record_schema.md` (full field tables §7-§9),
`pcrecbench/subbench.py`, `pcrecbench/harness.py` (`outcome_for`,
`derive_status`, the compile loop), `pcrecbench/reduce.py`
(`judge_trial_agreement`), `pcrecbench/record.py`, `pcrecbench/report.py`
(grepped exhaustively for `variant`, `convention`, `tags`), `tools/export_rxt.py`,
`tools/CLAUDE.md`, `testees/pcre2/configs.toml`, `testees/pcrec/configs.toml`,
`docs/dev/predictions/CLAUDE.md`, `scripts/run_window.sh`, and
`~/pcrec/docs/spec/rxt_format.md` (full, §"The head" through §"`--list-source`").

**The lens.** Assume the design is approved as-is; does every "no schema
change", "already legal", "already built" and "one new generator" claim
hold against the code and specs as they exist today. I did not build,
run `make`, or touch `bench/`, `schema/`, `pcrecbench/` or `testees/`.

---

## Summary of severities

| # | severity | finding |
|---|---|---|
| B1 | BLOCKING | §5.6's "testees scored against their own convention" is requirements-only prose with zero implementation; family 11 (v1, 6 target members) cannot be measured correctly as designed, and no lane in §11 proposes building the missing machinery |
| B2 | BLOCKING | §5.7's claim that `variant.kind` rendering is "Already built" is false — `report.py` never reads `patterns[].variant` at all. L5's "many-variant rendering check" understates the work as a stress test of something that does not exist |
| B3 | BLOCKING | §4.1's plan to bucket wild-vs-designed via `patterns[].tags` violates the schema's own explicit FILTERABLE/DIAGNOSTIC rule, and an identical `key:value` tag convention (`tier:`, `convention:`) already exists in every record today and is provably never read by the reporter |
| B4 | SHOULD-FIX | §8.1's "no schema change" claim for a zero-match-row **pinned** record is technically true but conceals that such a record can never reach `status: measured` under the current harness decision table — it is permanently `inconclusive-spread` |
| B5 | SHOULD-FIX | §9.4's "no build directives" gate is described as checking for a distinct line/row *kind*; `flags`/`engine`/`budget`/`encoding` are block-scoped attributes of the `pattern`-kind row's own columns, not separate `--list-source` row kinds — buildable, but the gate's actual shape needs restating for L4 |
| B6 | WORTH-NOTING | §9.3 undersells the `subbench.py` surface the .rxt loader touches: `Pattern.__init__`'s required-field tuple and `pattern_bytes()` both hard-require `file` today, not just an "entries drop their `file` key" edit |
| B7 | WORTH-NOTING | `unsupported-by-declaration` and `testee.conventions` are both schema-legal today with **zero** production use anywhere in the harness/adapters/validator cross-rules; this design is their first real exercise, which raises the bar on L5's witness-check arm |

**Overall verdict:** the design's schema/harness claims are accurate where
they describe *shapes that already exist and are exercised* (record
identity, `declaration_ref`, the compile-row cost model, `index.tsv`, the
report TSV header, the `.rxt` head grammar, `subbench.content_hash`,
`gen_*.py --check`, the prediction format's `n_wrong eq 0` constraint,
`run_window.sh`'s `SUBBENCH`/`CELL_CAP`/sidecar-regeneration contract — all
confirmed byte-for-byte against the code). It is **wrong in three places
where it treats a schema FIELD's mere existence as a working MECHANISM**:
convention-based scoring, variant rendering, and tag-based bucketing. All
three sit on the same fault line — `testee.conventions`, `patterns[].variant`
and `patterns[].tags` are schema-legal, declared, and in two of three cases
already populated on every record — and none of the three has ever been
*read* by anything that reduces, scores or renders a record. The design
inherited this blind spot honestly (it is citing real requirements/schema
text), but v0.1 presents Q3/Q4/§5.6/§5.7 as settled machinery rather than as
machinery this project would be building **for the first time**, which
understates what L3/L5 actually cost and, for B1, undermines a v1-chartered
family's correctness.

---

## B1 — BLOCKING: convention-based correctness scoring does not exist

**Claim (§5.6):** "`record_schema.md §5` already carries the three tokens
as `conventions[]`, and `requirements.md §7` already says convention is a
per-CASE expectation tag and testees are scored against their own.
Family 11 is the family that exercises this for the first time in this
repo." Family 11 (`semantics-divergence`, §3.1 row 11) is a **v1** family
with 6 target members, explicitly testing `a|ab` against `"ab"` where
`pcre2-dfa` (leftmost-first-but-decreasing-length-order, per pcre2's own
API), RE2 (`perl-leftmost-first` default / `posix-leftmost-longest` under
`re2-longest`) and TRE (`posix-leftmost-longest`, later) are all supposed
to be scored as CORRECT even though they answer differently from the
canonical pcre2-jit/pcrec oracle.

**What actually exists:**

- `testee.conventions` is a required schema enum field
  (`schema/record.schema.json:409,435`) with **no cross-line rule**
  anywhere in `schema/validate.py` (`grep -n conventions schema/validate.py`
  returns nothing) — it is declarative metadata a testee states about
  itself, never checked against anything, never read by anything.
- Correctness is decided by exactly one function,
  `pcrecbench/harness.py:106` `outcome_for(row, expectation, regime,
  subject, giveup_ok)`. It branches on `row.answer`/`row.consumed`/
  `row.detail` against a single `expectation` object. **It has no
  parameter for the testee's declared convention and no branch that reads
  one.**
- The expectation itself is looked up by
  `pcrecbench/subbench.py:268` `Subbench.expectation(self, pattern,
  subject_id, regime)` — keyed on **(pattern, subject_id, regime) only**.
  There is no testee axis and no variant axis in the lookup key, and
  `expectations.tsv` (built once by `gen_expectations.py` from the single
  libpcre2 oracle) has one row per that same triple. Every testee in a
  cell is graded against the identical row.
- `requirements.md §7`'s actual promised escape hatch — "a testee that
  cannot produce a case's convention either runs a declared variant with
  its own convention-tagged expectations or reports
  `unsupported-by-declaration`" — requires a **per-testee (or per-variant)
  alternate expected answer**. No such field exists:
  `patterns[].variant` (`record_schema.md:1026-1038`) carries `kind`,
  `text`, `options`, `objective_preservation`, `capture_correspondence`,
  and re-asserted `hazard_class`/`size_class` — **nothing that overrides
  the expected match/span for that variant.** The comparison in
  `harness.outcome_for` would still be against the single canonical
  `expectation` object regardless of which variant compiled.

**Consequence:** as designed, a `pcre2-dfa` or (later) `re2-longest`/TRE
cell on family 11's `a|ab` case would be graded `did-not-match-as-expected`
— a wrong answer — by the existing harness, which is precisely the
mis-scoring family 11 exists to prevent (§5.6: "A testee is scored against
its own convention"). Nothing in §11's build plan (L1-L6b) proposes adding
a per-testee/per-variant expected-answer override to `Subbench.expectation`
or `outcome_for`. This is not a documentation gap; it is a missing harness
capability that a v1-chartered family's correctness depends on.

**Proposed fix:** either (a) add an explicit lane (before or inside L5)
to build a per-testee/variant expectation override — the natural shape is
a `variant`-scoped alternate `expectations.tsv` row or a `patterns[].
variant.expected_override` field, both of which are schema/harness
changes this design currently claims are unnecessary — or (b) narrow
family 11's v1 scope to testees that all share `perl-leftmost-first`
(pcre2-interp, pcre2-jit, pcrec, and even `pcre2-dfa`'s own decreasing-
length-order needs checking against this — see the note in §5.6 itself:
"this is a real semantic difference the adapter must state, not a
convention token", which reads as already anticipating scoring trouble)
and defer the RE2/TRE convention divergence to whichever lane finally
builds the override.

---

## B2 — BLOCKING: `variant.kind` is not rendered by the reporter today

**Claim (§5.7):** "Already built and already ruled, needing only a check
at this set's scale: — `patterns[].variant` is REQUIRED... `variant.kind`
... is informational (OD-B5) and **the reporter shows it beside the
number** (`requirements.md §4.5` closing)." §11's L5 lists only "**the
reporter's many-variant rendering check**" as the deliverable, i.e. a test
against an existing rendering path. §13 R7 states: "**Never exercised**
(N2 §7 item 4)... L5 checks it BEFORE the set ships, against a synthetic
report" — "never exercised" is being read as "exists but untested at
scale."

**What actually exists:** `patterns[].variant`/`variant.kind` is **never
read anywhere in `pcrecbench/report.py`.** An exhaustive grep
(`grep -n variant pcrecbench/report.py`) returns exactly two lines, 679
and 3276, both unrelated prose about "the [B26] (c) re-render invariant"
— not the schema field. `pcrecbench/reduce.py` has zero hits. The only
place `variant` appears at all in the harness package is
`pcrecbench/record.py:177-187`, which **writes** `"variant": None` when
building a record's `patterns[]` entry (the write side, confirmed by its
own comment: "requirements 4.5: a variant is never a silent fork, so the
record says so either way") — there is no reader.

**Consequence:** `requirements.md §4.5`'s closing sentence describes an
intended rendering rule that was never implemented; nothing in this
project's five existing sub-benches has ever exercised a testee variant
whose `variant.kind` needed showing. R7's framing ("never exercised") is
correct read literally but the design's own §5.7 header ("Already built")
directly contradicts it — one of the two is wrong, and the code confirms
§5.7 is the one that is wrong. L5 as scoped ("a check... before it
ships") sizes this as validating an existing code path; it actually needs
to design and build that code path from nothing — a materially larger L5
task, and one whose absence would silently make every one of family 2, 6,
7, 8's designed control-twin variants (or any future spelling-rewrite
testee) invisible in a rendered report table.

**Proposed fix:** correct §5.7 to state plainly that variant rendering is
UNBUILT, and add "design and build the `variant.kind` rendering" as an
explicit L5 deliverable (not a check), sized accordingly.

---

## B3 — BLOCKING: bucketing via `patterns[].tags` contradicts the schema's own filterability rule, and the exact mechanism already exists and is already unused

**Claim (§4.1):** "**What the RECORD carries.** No schema change.
`patterns[].tags` is an optional array of string, DIAGNOSTIC
(`record_schema.md` §8, patterns table), and the capability set puts two
tokens in it per pattern: `src:<source_name>` and `fid:<fidelity>`. **A
report can then bucket wild against designed without a schema MINOR.**"

**What the schema actually says about DIAGNOSTIC fields, in the same
document the design cites:** `docs/design/record_schema.md:841-846`,
the field-table preamble (governs every table below it, including the
`patterns[].tags` row at line 1025): "FILTERABLE means the reporter (§8 of
the requirements) may filter or group on it. **DIAGNOSTIC /
REPRODUCIBILITY-ONLY fields are free text ... and the reporter must NOT
offer them as filters** — the R1 A4 finding in reverse: what is filtered
must be enumerated or normalized." `patterns[].tags` itself is documented
at line 1025 as "req: o ... rule: DIAGNOSTIC ... why: the sub-bench's
other tags, **carried but not filtered until they are enumerated**."
Bucketing a report by wild-vs-designed is precisely "filter or group on
it" — the one operation the field's own rule says the reporter must not
perform.

**This is not a hypothetical tension — the identical mechanism already
exists in every record and is already never read.** `pcrecbench/
record.py:215-221` already writes `tier:<feature_tier>` and
`convention:<convention>` as `key:value` strings into `patterns[].tags`
on every record, today, for all five existing sub-benches. A second
exhaustive grep (`grep -n '"tags"\|\.tags\b' pcrecbench/report.py`)
returns **zero** hits: the reporter has never once read a `patterns[].
tags` value, for either of the two tag families that already exist. The
capability set's plan is to add a third and fourth tag family
(`src:`/`fid:`) to a field with a two-year (in project time) unbroken
track record of being write-only.

**A second, independent problem with the field even if the "must not
filter" rule were waived:** `patterns[].tags` has **no grammar** — it is
`{"type": "array", "items": {"type": "string", "maxLength": 64}}`
(`schema/record.schema.json:305`), an unconstrained string array, unlike
`hazard_class`/`size_class`, which are real closed enums checked by JSON
Schema. A typo (`src:owasp-validaton`) or an inconsistent prefix
(`source:owasp-validation`) would silently corrupt any wild/designed
bucketing built on top of it, with nothing in `make check-schema` able to
catch it — the exact "a typo that silently becomes a new tag is a
capability claim nobody checked" hazard §5.1 itself names for the
REQUIRES vocabulary, applied here to a field the design proposes to use
the same way without the same closed-set discipline.

**Proposed fix:** either (a) promote provenance bucketing to a real
enumerated, FILTERABLE field (e.g. `patterns[].provenance_source` as a
closed slug enum, `patterns[].fidelity` as the closed three-value enum
§4.1 already defines) — which **is** a genuine schema MINOR, directly
contradicting §4.1's "no schema change" framing and §1.1's traceability
row for requirement (1) — or (b) accept that wild-vs-designed bucketing
lives only in the set's own `provenance.tsv` and any ad hoc script that
reads it directly (never the general reporter), and correct §4.1 and
§10(d)'s "A report can then bucket..." framing to say so. Either way this
needs a ruling before L3/L5, because the two paths have different schema
consequences and L1's `provenance.tsv` design should match whichever is
chosen.

---

## B4 — SHOULD-FIX: a compile-only, zero-match-row **pinned** record can never be `status: measured`

**Claim (§8.1):** "**And a finding this note adds:** that shape needs
**no schema change and no 'partial regime' concept.** A record with
compile rows and NO match rows is already legal — `subjects[]` 'may be
empty (a record with no match rows)' (`record_schema.md §8`) and
`trial_agreement` is already defined for it (`n/a-trials` with `trials:
0`, required at ≥ 1.4 'even a record with no match rows'). So a
python/perl testee produces a record that is structurally complete and
simply carries no timings."

**Schema-VALIDITY is true; USABILITY is not, and the section does not
say so.** Tracing the actual arithmetic:

- `pcrecbench/reduce.py:271-297` `judge_trial_agreement(rows)`: with zero
  match rows, `match = []`, `trials = max((...), default=0) = 0`. Since
  `trials < TRIAL_AGREEMENT_MIN_TRIALS` (5), the block is stamped
  `"verdict": "n/a-trials"` — this part matches the design's claim
  exactly, and the record does validate.
- `pcrecbench/harness.py:400-426` `derive_status(reasons, agreement,
  tier)` is the function that turns that block into a `status`. Reading
  it directly: `if pinned: return STATUS_SPREAD, [ta_line] # n/a-trials,
  pinned (R-12)` (line 425) — **only** a **scratch**-tier record with
  `n/a-trials` gets `STATUS_MEASURED` (line 426, ruling `E-2`). A
  **pinned** record — which is exactly what a python-re/perl testee
  measured in a normal window would be, since neither has a `local:`
  binary shape (`record_schema.md §6.2/§6.8`) — is unconditionally
  `inconclusive-spread`.
- `docs/design/record_schema.md:1148`, rule X13 clause 4 (schema-level,
  independent confirmation): "`trial_agreement.verdict` = `agree` on a
  `pinned` record (`tier` absent = `pinned`) and ≠ `disagree` on a
  `scratch` one" — the pinned branch demands **strict `agree`**, which
  `n/a-trials` never satisfies (X31: `n/a-trials` fires precisely when
  `trials < 5`, and `agree`/`n/a-trials`/`disagree` are mutually
  exclusive).

**Consequence:** every pinned python-re/perl cell (§8's own roster
table marks them "later", but §8.1 is adopted now, and Q14 answers
"yes" with no caveat) would be written, validated, and indexed
successfully — and then be **permanently** `inconclusive-spread`:
excluded from ranking by default (`pcrecbench/CLAUDE.md`'s R1/OD-B14
rule — "a non-`measured` row is excluded from ranking by default"), and
`scripts/run_window.sh`'s "exit code 4... re-measures such a cell once"
contract (`docs/dev/plan.md`/`pcrecbench/CLAUDE.md`'s gate_shape_v14
summary) would spend a re-measure on these two cells every single window
night for a condition measurement can never resolve, since the record
structurally has zero match rows regardless of how many times it is
re-run.

**Proposed fix:** state plainly in §8.1/Q14 that these testees, run
pinned, are permanently `inconclusive-spread` and must always be queried
with `--include-unmeasured`, and consider whether `run_window.sh` should
special-case a zero-match-row cell to skip its one-retry contract (a
harness change §8.1 explicitly disclaims needing). This does not block
v1 (§8 marks python/perl "later"), but it must be resolved, or the "no
schema change" framing corrected, before L6b's python/perl lane opens
and before Q14 is treated as costless.

---

## B5 — SHOULD-FIX: the "no build directives" gate's mechanism needs restating

**Claim (§9.2 rule 1, §9.4):** "No `target`, no `config`, no block-level
`flags`/`engine`/`budget`/`encoding` line" and the gate "the file
contains no `target`, `config`, `flags`, `engine`, `budget` or `encoding`
line."

**What `--list-source`'s TSV actually shapes this as**
(`~/pcrec/docs/spec/rxt_format.md:425-442`, the sixteen-column table):
column 1 (`kind`) is one of exactly `lib | target | config | description
| pattern` — **`flags`/`engine`/`budget`/`encoding` are never row
*kinds*.** They are per-`pattern`-row *columns* (6 `flags`, 9 `encoding`,
10 `engine`, 11/12 `budget_steps`/`budget_frames`), populated only when a
pattern block itself used the block-scoped `flags i` / `engine vm` /
`budget steps=N` / `encoding <ident>` directives
(`~/pcrec/docs/spec/rxt_format.md:213-215,299-346`). So "the file
contains no ... line" is imprecise: the actual check is "every
`pattern`-kind row's `flags`/`features`/`encoding`/`engine`/
`budget_steps`/`budget_frames`/`features_only` columns are empty",
alongside "no row has `kind = target` or `kind = config`". This is
entirely buildable from the same TSV the design already plans to parse
for the block↔sidecar gate — it just needs the columns named correctly
so L4 does not go looking for a `kind=flags` row that will never appear.

**Proposed fix:** rewrite §9.2 rule 1 and §9.4's gate description to name
the actual check: "no `target`/`config`-kind row, and every `pattern`-kind
row's flags/features/encoding/engine/budget columns are empty" — same
outcome, correct mechanism for L4 to build against.

---

## B6 — WORTH-NOTING: §9.3 undersells the `subbench.py` change

**Claim (§9.3):** "The sidecar's `[[patterns]]` entries drop their `file`
key and key on `name` instead."

`pcrecbench/subbench.py:93-108`, the `Pattern` class, hard-requires
`file` today: `for req in ("name", "file", "hazard_class", "size_class"):
if not getattr(self, req): raise SubbenchError(...)`. And
`Subbench.pattern_bytes(name)` (`subbench.py:242-246`) opens
`self.pattern(name).file` directly — there is no code path today that
resolves pattern bytes any other way. Dropping `file` from the sidecar
is not merely "key on `name` instead" at the sidecar level; it requires
changing `Pattern`'s required-field list AND giving `pattern_bytes()` (or
its equivalent for an `rxt` set) a second implementation that reads from
the parsed `.rxt` block text rather than a per-pattern file. This is
squarely inside L4's stated scope ("the .rxt loader"), so it is not a
design defect, just an understatement of L4's surface area worth naming
so the lane is not surprised. (One thing that needs **no** change:
`Subbench.content_hash()` at `subbench.py:287-311` walks and hashes every
committed file under the sub-bench root generically — a single committed
`patterns.rxt` is covered exactly like any other file, with no special
case needed.)

---

## B7 — WORTH-NOTING: two schema values this design would exercise for the first time in the harness's history

- **`compile_outcome = "unsupported-by-declaration"`** appears in
  `schema/record.schema.json` (lines 122, 690-692) and in prose in
  `pcrecbench/report.py` (lines 416, 3239, both describing it, neither
  producing it), but grepping every adapter (`testees/*/adapter.py`) and
  `pcrecbench/harness.py` for the string finds it **nowhere as a value
  any code path currently emits.** The pre-compile policy (§5.3) would be
  its first real producer.
- **`testee.conventions`** (see B1) is required by every existing record
  today, but is never read by any validator rule or reducer — pure
  declarative metadata until this design.

Neither is a defect — both are exactly the kind of "first-class capability
this repo has never exercised" the design elsewhere states clearly (e.g.
§5.6's own "for the first time in this repo," §9's `.rxt` Option B for
"the first non-pcrec-shaped sub-bench"). Flagging both here because §5.3's
"a check with no failing case proves nothing" discipline should apply with
extra weight to a check whose POSITIVE case (a real `unsupported-by-
declaration` compile row surviving `store.write()`) has literally never
existed in the store before, and because it strengthens B1's point that
`conventions[]` is declared-but-inert machinery, not exercised-and-working
machinery.

---

## What I did not find a problem with

Confirmed accurate against the code, cited here so the panel does not
re-derive them: `declaration_ref`'s conditional requirement on
`unsupported-by-declaration` (`record_schema.md:1108`, matches §5.3
exactly); the `did-not-compile` + `refusal_class` no-new-enum argument
(§5.4, matches the closed `compile_outcome` set at
`record_schema.md:372`); the `engine_metadata_declaration`'s three rules
(§7) as applied to `refusal_class`/`dfa_cache_flushed` (§5.5); `.rxt`'s
block grammar permitting a `name`/`description`/`pattern`-only block with
no head `target` line at all — confirmed against
`~/pcrec/docs/spec/rxt_format.md`'s own text ("No `target` and anything
else builds NOTHING. The file is a library of definitions... It is not
an error") and `--list-source`'s "prints the file AS WRITTEN" contract,
which lists `pattern`-kind rows regardless of whether any `target`
resolves them; `description`'s legality at block scope, one-line form
only (`rxt_format.md:297-298`, matching §9.2 exactly); the block `name`
grammar and its uniqueness-in-file-namespace rule (§9.1, matching
`rxt_format.md:278-296`); `capabilities = [...]` as a plausible new
per-config TOML key against the real shape of `testees/pcre2/
configs.toml` and `testees/pcrec/configs.toml`; the pre-compile policy's
natural home in `pcrecbench/harness.py`'s existing per-pattern compile
loop (`harness.py:576-597`, immediately before `adapter.compile()` is
called — exactly where a REQUIRES short-circuit would sit); `store/
index.tsv`'s literal header (`path subbench version testee_id machine_id
timestamp status rows`, byte-identical to §10's table); the report TSV's
18-column header and header-comment key list (byte-identical to
`render_tsv` at `report.py:4286-4319`, including P-1's `floor_pattern:`
last-key rule); the predictions format's `n_wrong eq 0` / "answer not
expressible" constraint (§11.3, matches `docs/dev/predictions/
CLAUDE.md` exactly); and §11.4's `SUBBENCH`/`CELL_CAP`/sidecar-regen
contract against `scripts/run_window.sh`.
