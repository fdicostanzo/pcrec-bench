# [B82] lane report — class-pure capture views + the standing cross-class query

Branch `lane/b82views`, commit `0939b40`. Inbox I-99 (Frank's ruling), I-100
(the FROZEN classification), I-101 (Frank's nuance, the standing query). Read
in full from `docs/dev/inbox_from_pcrec.md` before any code was written.

## Charter-vs-committed checklist (per the brief's seven design constraints)

1. **The declaration table is report-time authority; no schema/record/
   testee_id change.** DONE — `pcrecbench/capture_class.py` (new file), a
   Python dict keyed on `(engine_name, engine_mode, caps_token)` — the
   pin-independent identity every testee_id already encodes
   (`schema/validate.py:derive_testee_id`'s own shape run backwards) — never
   the full testee_id (which embeds a pin that changes every re-pin). `YES`:
   libpcre2 interp/jit, re2 default/longest, oniguruma, tre, every pcrec
   `-caps-` config. `NO`: libpcre2-dfa, vectorscan, pcrec `auto-nocaps`, and
   **rust-default via I-100's OVERRIDE** (its id says `-caps-`; the table
   says `no`, with the single `captures_at` call declared as a fixed
   per-call cost, citing `src/main.rs:255-266`). An id this table has no row
   for is `UNDECLARED`, never guessed — verified against the whole real
   `store/index.tsv` (86 distinct testee_ids, 0 undeclared) before writing
   any reporter code. The full table is reproduced verbatim below.
2. **The two class-pure views, headline; the mixed table demoted to
   third; no cross-class cell.** DONE in `pcrecbench/report.py`
   (`_dispatch_ranking_views`, `_render_ranking_pass` — the existing [B9]-
   [B52] ranking renderer, extracted into a closure and called once
   (unfiltered, byte-identical to before) or three times (class-pure ×2 +
   mixed, demoted, in that order) depending on whether the report's roster
   spans both classes). Each class-pure view gets its own baseline,
   ranking order, `vs baseline`/`vs best` ratios (recomputed WITHIN the
   filtered roster, not carried over from the mixed one) and Δ-vs-previous-
   version column — every column the single table already had. `render_tsv`
   gets the same three passes as new section values (`rank_yes`/
   `baseline_yes`, `rank_no`/`baseline_no`) ahead of the unchanged `rank`/
   `baseline` pass; the `excluded`/`not_ranked`/`scratch`/`did_not_compile`
   rows are NOT duplicated per class (one home, the unfiltered pass, so the
   exclusion narrative never forks). An undeclared testee is listed under
   its own `### Undeclared capture class` heading / `undeclared_capture_
   class` TSV rows and excluded from BOTH class-pure views.
   **"Row-best"/"D119 delta columns"**: I read these as the ALREADY-EXISTING
   `vs best` ratio and the R8 cross-pin `Δ vs previous version` column
   (`report.py`'s own [B9]/[B16] machinery) — both are preserved and now
   computed within each class. **"Threshold population"**: no D119 IQR/
   null-band machinery exists in `report.py` yet ([B79] is NOT-STARTED,
   `docs/dev/plan.md`), so I did not invent one; see item 3 below and the
   OWED note.
3. **The query (I-101), a fourth section, never a ranking.** DONE —
   `_cross_class_query_hits` (shared arithmetic, markdown + TSV render from
   the SAME list so the two formats can never disagree) walks every ranking
   group's measured, non-scratch rows and reports every cell where a
   YES-class config's median beats a `pcrec auto-nocaps` row's (any pin
   present in the report), with the ratio and the competitor named, and an
   unconditional count. **THE IQR/NULL-BAND CLEARANCE COLUMN I-101 ASKS FOR
   IS NOT COMPUTABLE**: [B79] (the null-control-band design) is NOT-STARTED,
   and the reduction objects `report.py` already holds
   (`SetCellReduction`/`MatchCellReduction`) carry median/min/max/stddev
   over TRIALS, never the raw per-trial values a Type-7 IQR needs. Both
   renderings state `not yet computable ([B79] not-started)` rather than
   fabricate a verdict — "Context around the numbers": state what was read
   and what was not. On the real `loglines@0.1` fullroster-25b1984f query
   (7 testees, both classes present) this fired **23 hits**, several
   genuinely large (`level-context`/`large-subject-throughput`: libpcre2-jit
   0.273× pcrec `auto-nocaps`) — a real finding for Frank's own "that would
   be surprising" concern, not a null result.
4. **The matrix page gains the class split.** DONE, as "two matrices"
   (the design brief's own alternative to a class column — testees are
   COLUMNS here, so a per-testee class COLUMN on each ROW made no sense).
   `render_matrix_tsv` gains ONE new provenance line (`# capture_class:
   yes=...; no=...; undeclared=...`) and an honest disclosure line stating
   that its existing `best_testee`/`best_ns`/ratio columns are computed
   ACROSS THE WHOLE roster (a pre-existing [B52] design choice, not
   introduced by this lane) — **the matrix's own cross-class-mixing defect
   is a FINDING, flagged and left OWED below, not silently fixed under this
   lane's own arithmetic.** `scripts/matrix_page.py` (deliberately
   dependency-free — no `import pcrecbench`) reads that provenance line by
   REGEX and, when both classes are present, renders TWO tables, each with
   its own `best_testee`/`best_ns` RE-DERIVED from the file's own numbers
   (`class_pure_row`: `absolute_ns(t) = ratio(t) × best_ns`, then a new
   class-local ratio) — a legitimate arithmetic identity over data already
   in the file, never a second reduction over the store, so the page's
   class-pure numbers can never drift from the reporter's own `rank_yes`/
   `rank_no` TSV rows by a rounding choice of its own. An undeclared testee
   is excluded from both tables and named in its own note. A single-class
   roster (or an older `.matrix.tsv` predating this lane) renders the
   ORIGINAL single table, byte for byte.
5. **The interpreter's catalogue stays green; awareness added.** DONE,
   minimally, per the brief's own steer ("leave it owed"). `catalogue/
   rules.toml` bumps to **3.5** (MINOR — no rule predicate/threshold/
   inputs/slots moved); `pcrecbench/interpret.py`'s `SECTIONS` tuple gains
   six names (`rank_yes`, `rank_no`, `baseline_yes`, `baseline_no`,
   `undeclared_capture_class`, `query_yes_beats_nocaps`) so a FUTURE rule
   can reference one without its own catalogue-side edit. `SECTIONS` gates
   rule-`inputs` PARSING only (checked at `catalogue/check_interpret.py`
   read time), never `ReportTsv` LOAD (confirmed directly: a real generated
   TSV carrying `rank_yes`/`rank_no`/`query_yes_beats_nocaps` rows loads
   clean under `pcrecbench.interpret.ReportTsv` with zero code changes
   needed there). **No interpretation RULE reads the new data** — a
   class-aware D119 verdict rule and a standing-query firing rule are
   INTERPRETATION WORK, explicitly OWED to a follow-up lane, not built here.
6. **REPORTER_VERSION v19 → v20; tests.** DONE. `REPORTER_VERSION = "v20
   (2026-09-23)"`; a new `[B82]` module-docstring section states the
   change. Tests, per the house sabotage/control style (constraint #6's
   four named minimums, ALL covered):
   - `test_report.py::test_capture_class_declaration_table` — the pure
     `pcrecbench.capture_class` unit test: every real roster row, rust-
     default's override (`is_override` true, `how_told` names the
     `captures_at` call), an unknown engine → UNDECLARED, an unparseable
     id → UNDECLARED.
   - `test_report.py::test_b82_capture_class_views_and_query` — a
     MIXED-ROSTER fixture (YES: `pcrec-auto`, `libpcre2-jit`; NO:
     `pcrec-auto-nocaps`, `rust-default`; UNDECLARED: `mystery`) asserting
     both views' correct memberships, the undeclared testee excluded from
     both and listed on its own, rust-default's declaration line rendering
     VISIBLY in the view it ranks in (design constraint (1)), the mixed
     table still listing everyone, the query firing on the constructed
     yes-beats-nocaps pattern (`p1`) and NOT on its CONTROL pattern (`p2`,
     where the YES config is deliberately slower), and markdown/TSV hit
     counts agreeing exactly.
   - `test_report.py::test_b82_single_class_roster_unchanged` — the
     CONTROL: a roster that does not span both classes renders NONE of the
     new headline text, and the query still renders (unconditional) with
     an honest `0 hits` sentence rather than disappearing.
   - `test_matrix_page.py`: `test_parse_capture_class` (the provenance-line
     parser, plus the empty-groups fallback control), `test_class_pure_row_
     rebases_within_class` (the arithmetic directly — a lone NO-class
     member re-bases 2.000× → 1.000×, a YES-class member whose global best
     was already in its own class stays unchanged — both directions in one
     fixture), `test_matrix_class_pure_split_renders_two_tables` (two
     `<table>`s, the undeclared testee absent from both column sets and
     named in its own note, the re-based cell rendering `1.000x` not
     `2.000x`), `test_matrix_single_class_roster_unchanged` (the CONTROL).
   7 new tests total (`test_report.py` 86 → **89**; `test_matrix_page.py`
   8 → **12**). Both standalone plain-runner suites confirmed GREEN:
   `python3 -m pcrecbench.tests.test_report` → 89 passed, 0 failed
   (~5m25s wall, ~1.4 GB peak RSS, run detached per the box's memory-
   heuristic rule); `python3 -m pcrecbench.tests.test_matrix_page` → 12
   passed, 0 failed.
7. **Committed reports are not regenerated by this lane; make check-harness
   is untouched.** DONE (deliberately). Confirmed: nothing this lane
   touches reaches an adapter, `testees/`, `harness.py`, `subbench.py` or
   any bench generator — `make check-harness` was NOT run (out of scope,
   per the brief).

## The declaration table, verbatim (`pcrecbench/capture_class.py`'s `DECLARED`)

| engine_name | engine_mode | caps_token | captures_run | how_told | citation |
|---|---|---|---|---|---|
| libpcre2 | dfa | nocaps | no | `pcre2_dfa_match()` cannot assign per-group captures at all (driver.c's own header comment) | I-99 ack |
| libpcre2 | interp | caps | yes | `pcre2_match()`; the ovector is assigned every call | I-99 ack |
| libpcre2 | jit | caps | yes | `pcre2_match()` (JIT-compiled); the ovector is assigned every call | I-99 ack |
| oniguruma | default | caps | yes | `onig_search()` with a region argument, populated every call | I-99 ack |
| pcrec | auto | caps | yes | the config's own `captures=on` | I-99 ack |
| pcrec | auto | nocaps | no | the config's own `captures=off` (`--no-captures`) | I-99 ack |
| pcrec | auto-in | caps | yes | the config's own `captures=on` (the frame-buffer axis does not touch captures) | I-99 ack |
| pcrec | vm | caps | yes | the config's own `captures=on` | I-99 ack |
| pcrec | vm-in | caps | yes | the config's own `captures=on` | I-99 ack |
| re2 | default | caps | yes | `driver.cc Match(..., submatch.data(), nsub)` with `nsub > 0` every call | I-99 ack |
| re2 | longest | caps | yes | the same `Match()` call, under `set_longest_match(true)` | I-99 ack |
| **rust** | **default** | **caps** | **no** | the timed loop is `find_at`-driven with exactly ONE `captures_at` call on the FIRST match per timed call, for verification only — a DECLARED fixed per-call cost (`src/main.rs:255-266`); the config's own `captures=on` names the ENGINE's capability, not this RUN's behaviour | **I-100 RULING (2), OVERRIDE** |
| tre | default | caps | yes | `tre_regnexecb()` with a `pmatch` array (`emit_caps`) | I-99 ack |
| vectorscan | block-nosom | nocaps | no | boolean grain by charter — Hyperscan has no capturing groups at all | I-99 ack |

`(cc-clang)`/size-cap/deny-flag/`-in` axes never change `engine_mode` or
`captures`, so every one of pcrec's sixteen pinned configs collapses onto
one of the four `pcrec` rows above by construction (verified against the
real `store/index.tsv`'s 86 distinct testee_ids: 0 undeclared). `pcrec-
local` (a provided binary, scratch tier, never in the canonical store) is
not enumerated separately — it derives `engine_mode`/`captures` from its
effective flags exactly as every pinned config does, so it reaches the same
`("pcrec", "auto"|"vm", ...)` rows.

## Symbols changed (for the interpreter record)

- New module: `pcrecbench/capture_class.py` (`CaptureDeclaration`,
  `ClassResult`, `YES`/`NO`/`UNDECLARED`, `config_identity`, `DECLARED`,
  `classify_testee`, `is_override`, `declaration_table_rows`).
- `pcrecbench/report.py`: `REPORTER_VERSION` v19 → v20; new functions
  `_class_membership`, `_base_ranking_heading_tail`, `_dispatch_ranking_
  views`, `_cross_class_query_hits`, `_render_cross_class_query`,
  `_NULL_BAND_NOT_COMPUTABLE`; `render_markdown`'s former inline ranking
  loop is now the nested closure `_render_ranking_pass(heading,
  testee_filter=None)`; `render_tsv`'s is now `_tsv_ranking_pass(
  rank_section, testee_filter=None, emit_extras=True)`; `render_matrix_tsv`
  gains the `capture_class`/disclosure provenance lines (no header/row
  shape change — old `.matrix.tsv` files parse unchanged).
- `scripts/matrix_page.py`: new `parse_capture_class`, `class_pure_row`,
  `_table_html`; `render_html`'s signature/template are unchanged from the
  caller's point of view, `PAGE_TEMPLATE`'s `{head_row}`/`{body_rows}`
  placeholders replaced by one `{tables}` placeholder (an internal
  refactor — no test called those two directly).
- `pcrecbench/interpret.py`: `SECTIONS` +6 names (see above).
- `catalogue/rules.toml`: `catalogue_version` 3.4 → 3.5 (MINOR, documented
  inline).

## Section names as rendered (markdown)

`## Ranking -- CAPTURING engines only, caps vs caps (<grain tail>)`,
`## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (<grain tail>)`,
`### Undeclared capture class (I-99: never guessed -- excluded from BOTH
class-pure views above)`, `## Ranking -- MIXED CLASSES, never compare
across cells (<grain tail>)`, `## Standing cross-class query (inbox I-101;
...)`. TSV section-column values added: `rank_yes`, `rank_no`,
`baseline_yes`, `baseline_no`, `undeclared_capture_class`,
`query_yes_beats_nocaps`.

## Validation run (numbers)

- `make check-schema`: **5 example(s) accepted, 73 sabotage(s) rejected,
  0 WRONG** — clean, untouched by this lane.
- `make check-report` (`pcrecbench.tests.test_report` +
  `test_matrix_page`): see the handback message for the final count —
  run in background per the box's memory-heuristic rule (KB-25's own
  ~1.4 GB RSS load, `run_in_background: true`, tracked).
- `make check-interpret`: **163 passed, 29 FAILED** — every failure is
  section 3 ("sidecar freshness", assertion name `re-renders byte-
  identical`), the SAME transitional class b58repin's and b74repin's own
  lane reports name and classify for a catalogue MINOR bump: "every
  committed `.interpretation.md` sidecar's own stamp carries
  `catalogue_version`, so a bump alone makes every sidecar's re-render
  differ from what is committed, with ZERO rule firing differently."
  Confirmed here the same way: sections 1/2/4/5/6 (21/8/127/4/1 = 161... )
  — full breakdown: section 1 = 21, section 2 = 8, section 3 = 2 PASS + 29
  FAIL, section 4 = 127, section 5 = 4, section 6 = 1; total 163 passed +
  29 failed = 192, matching [B74]'s own 190-total gate plus the two
  sidecars committed since ([`2026-09-23-capability-*-after-8d716693`],
  [`...-after-b1885a83`]). The 29 file names are listed in this lane's
  own scratch log (not committed — regeneration is the manager's step);
  ask the lane for the list if the manager wants it verbatim before the
  regen wave runs.
- `make check-harness`: **NOT RUN** (out of scope by the brief; nothing
  in this lane reaches `testees/`, `harness.py`, `subbench.py` or a bench
  generator).

## Owed to the manager at merge

1. **The sidecar regeneration wave** (`scripts/regen_sidecars.py`) for the
   catalogue 3.4 → 3.5 bump — the 29 files `make check-interpret` names,
   MINOR/additive, per the SAME standing precedent b58repin's and
   b74repin's own OWED-2 items describe (this lane does not regenerate
   them; the manager's merge-time step does).
2. **Committed report regeneration** for `REPORTER_VERSION` v19 → v20 —
   the standing precedent (`reports/CLAUDE.md`); per the brief's own item
   7, the manager regenerates the capability groups at merge so O-49's
   records get their two class-pure views (`bench/capability`'s roster
   is 11 testees across pcre2/pcrec/re2/onig/tre/vectorscan/rust — almost
   certainly spans both classes).
3. **Interpretation RULES over the new sections** — a class-aware D119
   verdict rule (reading `rank_yes`/`rank_no` instead of `rank` where a
   report is class-split) and a standing-query firing rule
   (`query_yes_beats_nocaps`'s `hit_count` as an R-STATUS-14-style
   standing check) are catalogue content this lane deliberately did not
   write (design constraint #5's own "leave it owed" steer) — a
   follow-up lane's work, not a defect here.
4. `docs/dev/plan.md`'s `[B82]` row and `docs/dev/dev_journal.md` are the
   manager's job per the standing precedent (b74repin/b58repin's own
   reports leave them untouched); not edited here.
5. **THE MATRIX'S OWN CROSS-CLASS RATIO ARITHMETIC (a finding, not fixed
   here).** `render_matrix_tsv`'s FLAT columns (`best_testee`/`best_ns`
   and every un-split ratio cell) still compute "this row's best" across
   the WHOLE roster, both classes pooled, when both are present — a
   pre-existing [B52] design choice this lane did NOT change (changing
   `_matrix_best`/`_matrix_cell`'s core arithmetic was out of this lane's
   scope and would have reopened the F26-immunity proof and its own test
   suite). The class-pure SPLIT PAGE (`scripts/matrix_page.py`) re-derives
   correct, class-pure numbers from the file's own data and is the
   authoritative reading; the FLAT file underneath still mixes classes in
   its `best_testee`/`best_ns`/un-split-ratio columns, now DISCLOSED in
   its own provenance line rather than silently. Whether `render_matrix_
   tsv` should also emit class-pure `best_ns_yes`/`best_ns_no` columns
   directly (removing the need for the page to re-derive) is a ruling for
   Frank/the manager, not decided here.
