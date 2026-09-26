# Lane b91views — [B91] report (2026-09-26)

Branch `lane/b91views`. One reporter change, three parts, one bump:
**`REPORTER_VERSION` v23 → `v24 (2026-09-26)`**, **catalogue 3.8 → 3.9**
(MINOR). Nothing merged by the lane; no committed report regenerated (only the
35 sidecars, whose stamp names the catalogue version).

## (A) `unsupported_by_pattern`, a new report-TSV section

- **Shape** (utf8_set_v1.md §11's F-M2 name; b77u5 finding 1): one row per
  (pattern, form, testee) whose compile row reported
  `unsupported-by-declaration`. Columns: `section=unsupported_by_pattern`,
  `pattern`, `subject_or_na=""`, `regime_or_na=""` (a compile outcome has no
  regime), `form`, `fact`, `testee`, `status` (the record's own status, which
  is what the column means everywhere else), `tier`, `metric=compile_outcome`,
  `value=unsupported-by-declaration`, `gave_up_summary` = the verbatim
  diagnostic (for example `REQUIRES unicode-class-scope; pcrec-auto-utf8 declares
  none of it`). Source: the new `ReportData.unsupported_by_cell`, keyed per
  form. The existing per-pattern `unsupported_by_pattern` dict, which the
  matrix uses, is unchanged.
- **Placement: after `compile_stamp`, outside the ranking-group loop.** This
  makes it F26-immune by construction: a pattern that no testee compiled still
  gets its rows. `did_not_compile` is still F26-exposed (not in this charter;
  noted below).
- **Nothing is emitted when the population is empty.** A set with no
  declarations therefore renders byte-identically to v23 apart from the
  version line (proof below).
- **The subject-grain slice** passes the section through unchanged, because
  it is a row filter that drops only `compile`/`compile_stamp`.
- **Markdown**: no new section. The charter named the TSV, and a markdown
  section would break byte-identity for the capability reports.
- **interpret**:
  - `SECTIONS` and `_ELSEWHERE` gain `unsupported_by_pattern`.
  - The four R-PRED rules' `inputs` gain `report:unsupported_by_pattern.{…}`
    (`catalogue/rules.toml`). Without it, `RuleView` refuses the section.
  - A clause can now use `section=unsupported_by_pattern` with quantity
    `section` and reducer `count`/`set_of(<key>)`.
  - A default-read clause whose cell sits only in that section now names it in
    R-PRED-3's "the selected cell is in the … section" and in (β)'s "also
    present in".
  - This is MINOR: no fact moves on an unchanged input, because no pre-v24
    report carries the rows. Section 6 (prose) is untouched: no template,
    no_fire or legend edits.
- **Fixtures (a sabotage and a control)**: `R-PRED-1__unsupported-count-confirmed`
  and `R-PRED-2__unsupported-count-refuted` (the base plus one declared
  mutation, `hi` 6 → 5).
  - Their source, `report_f`, is a REAL v24 render committed as
    `catalogue/fixtures/sources/capability-0.1-rust-first-cf0962e3.v24.tsv`.
    It is the rust-first capability query plus `--until 2026-09-20T00:00:00Z`,
    and carries 22 unsupported rows (equal to the committed matrix's 22 `unsup`
    cells).
  - It sits under `catalogue/` because the `reports/` group is at v18 and
    belongs to the wave.
  - The clause is `catalogue/fixtures/predictions-unsupported.tsv` UNS1
    (`section=unsupported_by_pattern;pattern=wild-logparse-*;form=plain;testee=rust_*`,
    count eq 6), and it is fixture-only.
  - Under the pre-[B91] interpreter the confirmed fixture would read R-PRED-3,
    because the section is not in `SECTIONS`. The fixture therefore
    discriminates the change.
- **Expressibility on the real utf8 data.** Scratch clauses were run through
  the real `interpret` CLI against the dry render; all three CONFIRMED:
  - P5.a as `section=unsupported_by_pattern;pattern=cls-w-ucp|cls-d-ucp|cls-s-ucp|asr-b-cyr-ucp|ci-ucp-invariance;form=plain;testee=pcrec_*_utf8`,
    count eq 20. Confirmed at exactly 20.
  - P9.b as the six ascii-class-scope ids with `testee=rust_*`, count eq 6.
    Confirmed.
  - The R8 population as `section=unsupported_by_pattern`,
    `set_of(testee)` `set-eq` the four pcrec-utf8 plus rust. Confirmed. (`set-eq`
    lists are `|`-separated.)

  The committed `docs/dev/predictions/utf8-0.1-first.tsv` is **NOT amended**.
  Its `stated_utc` precedes the window, so a clause added now would be written
  after the data exists. The manager rules whether to add P5.a, P9.b and R8 as
  a dated post-hoc census (see OWED).

## (B) The matrix's best follows the selection (Frank, 2026-09-25)

- **`render_matrix_tsv`**:
  - `best_testee`/`best_ns` are RENAMED `best_testee_pooled`/`best_ns_pooled`.
  - They are followed by `best_testee_yes`/`best_ns_yes`/`best_testee_no`/`best_ns_no`:
    the same `_matrix_best` over the roster's capture-class yes / no testees
    only. The columns are empty where the class has no rankable cell;
    undeclared testees are in neither.
  - The ratio cells stay pooled.
  - The disclosure line is rewritten to name all three and the identity
    `class ratio = ratio x best_ns_pooled / best_ns_<class>`.
  - The F26 row is unchanged: all best columns are empty and every cell is a
    token.
- **`scripts/matrix_page.py`**:
  - It adds a testee selection (checkbox per shown testee, all/none, "n of N
    selected"), plus an inline script. For every table and every row, the
    script recomputes best = the lowest `data-ns` among the SELECTED ratio
    cells, which is the viewer's `computeBest` (status tokens are never
    candidates). It then rewrites each ratio, its ramp colour and tooltip, and
    hides unselected columns.
  - Every ratio cell carries `data-t` and `data-ns` (absolute ns = ratio × its
    table's best_ns).
  - Class-split pages offer exactly the testees shown; undeclared testees are
    not selectable.
  - Both headers are accepted: the v24 10-column one and the pre-v24 6-column
    one. v24 rows are normalised so `best_*` = pooled.
  - The JS ramp is a copy of `_ratio_color` (same stops, same LOG_MAX, same
    0.55 text flip).
  - The script passes `node --check`. A fake-DOM run in node (scratch) gave:
    selection {b, c} over ns {a:100, b:200, c:400} → best b 200.0, b 1.000x,
    c 2.000x `rgb(63,156,246)` (= python's ramp at 2.0), a hidden. An all-token
    row gave best "—".
- **Tests**:
  - `test_matrix_class_pure_best_columns_b91` (hand-computed pooled/yes/no
    bests incl. an undeclared pooled winner; single-class control).
  - `test_matrix_page.py` +3:
    - v24 header parse/normalise with a 6-column control.
    - Selection over the shipped `data-ns`: a full selection reproduces the
      static best; a YES-only selection = the file's `best_ns_yes`; a NO-only
      selection = `best_ns_no`; tokens carry no `data-ns`; the ramp constants
      match.
    - Class-split selectable set and absolute `data-ns`.
  - The F26 test (`test_matrix_all_refused_pattern_f26`) and the other matrix
    tests pass through the updated header parser; `_matrix_rows_by_key` now
    asserts the 10 fixed columns.

## (C) The identity bullet, per side (the owed [B90] fix)

The null band's `- identity:` bullet now reads:

> the records' own `engine_metadata.program_sha256` ([B88], schema v1.7)
> where BOTH compile rows of a cell carry it; otherwise OUR OWN census (…).
> Which records carry the field, per side: `pcrec 6ef76820 -> ce658cb7`: the
> BEFORE (`6ef76820`) records carry NO `program_sha256` (0 of 497 compiled
> cell(s)), the AFTER (`ce658cb7`) records carry `program_sha256` (497 of 497
> compiled cell(s)).

The quote is the real render of the committed after-ce658cb7 query.
`_field_carriage` counts compiled cells, meaning cells whose compile row
carries engine_metadata. Refusals and declarations are not counted.
`test_identity_bullet_per_side_b91` is new. `test_b88_…`'s one-sided control
now compares the band section minus that bullet and asserts the bullet's two
per-side phrases.

## Byte-identity proof (v23 code vs v24 code, same loaded records)

Each committed report's OWN query was rendered in-process by master's v23
`report.py` (775b39b, loaded as a temporary module) and by v24, from the same
loaded records. Driver: scratch `prove_identity.py`; outputs are in scratch
`b91/proof/`.

| query (committed group) | recs | .tsv | .md | .matrix.tsv |
|---|---|---|---|---|
| email-specimen@0.2 fullroster-25b1984f | 7 | **version line only** | **version line only** | expected (below) |
| loglines@0.1 fullroster-25b1984f | 7 | **version only** | **version only** | expected |
| bounded@0.3 fullroster-25b1984f | 7 | **version only** | **version only** | expected |
| altwide@0.2 fullroster-25b1984f | 7 | **version only** | **version only** | expected |
| syntax@0.1 fullroster-25b1984f | 7 | **version only** | **version only** | expected |
| capability@0.1 rust-first-cf0962e3 | 1 | version + 22 appended `unsupported_by_pattern` rows | version only | expected |
| capability@0.1 after-ce658cb7 | 8 | version + 8 appended rows (`negation-scope-lookbehind-var` × 8 pcrec configs) | version + the identity bullet | expected |
| utf8@0.1 first (7 records) | 7 | version + 35 appended rows (20 pcrec UCP, 15 rust) | version only | expected |

**Matrix "expected"** means that on every one of the 8 queries (scratch
`check_matrix_delta.py`):
- every data row minus the 4 new columns is byte-identical to v23;
- exactly 3 comment lines changed (version, ratio-definition wording, the
  disclosure);
- the header is the rename plus the 4 new names;
- every class-pure best re-derives from the row's own pooled ratio ×
  best_ns_pooled within print rounding. That is 1,819 class-best cells over
  1,088 rows.

The 5 fullroster queries have NO `--until`, so a fresh render sees rust's
2026-09-22 re-measure. The proof compares code on the SAME records, so this
does not affect it. It does affect the wave (below).

## Validation

- `make check-report`: test_report **101/0**, test_quick 7/0,
  test_matrix_page **15/0**, fixture validation and CLI smokes OK
  (`check-report: OK`).
- `make check-interpret`: **209 passed, 0 FAILED**. Section 4 is 139 (+6: the
  two new fixtures); section 3 is fresh after the sidecar regen.
- `python3 catalogue/fixtures/gen.py --check`: 251 files / **77 fixtures, ok**.
- `make check-schema`: 6 accepted, 74 sabotages rejected for their rule, 0
  wrong.
- Sidecars: `scripts/regen_sidecars.py` gave 35/35 regenerated with 0
  failures. The diff is exactly 35 × 2 lines (`catalogue: 3.8→3.9` and the
  "Generated by … catalogue 3.9" sentence).
- NOT run by the lane: the full `make check` (check-harness is ~20 min and
  untouched by this change). **OWED to the manager**, command below.

## The utf8@0.1 first-sample DRY render (for the reading lane)

Written in this worktree, NOT committed (`build/` is gitignored):

    /home/duxevents/pcrec-bench/.claude/worktrees/agent-af29a6c03e968fcc3/build/b91-dry/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.{tsv,md,matrix.tsv,matrix.html,subject-grain.tsv}

It covers 7 records with 0 superseded, rendered at v24 (~165 s in-process,
one load). The invocation, from the repo root of a v24 checkout:

    Q="--subbench utf8 --version 0.1 --since 2026-09-26T00:00:00Z --until 2026-09-26T12:00:00Z"
    G=reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7
    python3 -m pcrecbench report $Q --format tsv    > $G.tsv
    python3 -m pcrecbench report $Q --format md     > $G.md
    python3 -m pcrecbench report $Q --format matrix > $G.matrix.tsv
    python3 -m pcrecbench report $Q --grain subject --format tsv --subject-grain-slice > $G.subject-grain.tsv
    python3 scripts/matrix_page.py $G.matrix.tsv

A one-load equivalent is the scratch `b91/dry_utf8.py`.

**FINDING for the reading lane:**
`python3 -m pcrecbench interpret <G>.tsv --predictions docs/dev/predictions/utf8-0.1-first.tsv --subject-grain <G>.subject-grain.tsv`
**exits 2 at load**. Q6 (ii)'s testee-glob check refuses P10.a's
`vectorscan_*_utf8`, which matches none of the 7 measured testees. P11.a
names `re2_*_utf8`/`oniguruma_*_utf8`/`vectorscan_*_utf8` too. The first
sample ran no re2, onig or vectorscan utf8 config. This is not a [B91] defect.
It needs a ruling: a sanctioned narrowing like [B93]'s, or waiting for those
cells. Also visible in the data: rust declares `unicode-class-scope`
unsupported too (5 rows), besides the 6 ascii-class-scope and 4 lookaround
rows.

## Regeneration owed for the version bump (MANAGER launches)

Every committed report group moves at v24:
- **all 74 `.matrix.tsv` + `.matrix.html`**: new columns, and a new page with
  the selection;
- **the 12 capability groups with declarations**: their `.tsv` gains
  `unsupported_by_pattern` rows. Groups: first-a770139e, after-cf0962e3,
  ext-first-cf0962e3, ext-second-cf0962e3, rust-first-cf0962e3,
  fullroster-25b1984f, pinconfirm-25b1984f, wrapfix-25b1984f, after-6ef76820,
  after-8d716693, after-b1885a83, after-ce658cb7;
- **every cross-pin `.md` with a null band**: the identity bullet (the four
  2026-09-23/25 capability after-* groups at least);
- every other file: the version line.

69 of the 74 groups are at v18 and 1 is at v21. Regenerating them also carries
every v19–v23 rendering change they have not yet received. Those are expected
classes documented in reports/CLAUDE.md and pcrecbench/CLAUDE.md, not v24's.

**Hazard:** 18 committed queries have no `--until`:
- 2026-08-25 email repin-692c2e8;
- all 2026-09-19/20/21 `rust-first-*` and `fullroster-*` groups.

A plain regen pulls in records measured since, at least rust's 2026-09-22
re-measure. `--pin-until-from-git` pins each to the UTC time of the commit
that first added its `.tsv`. It was tested on rust-first-cf0962e3:
`--until 2026-09-19T22:58:39Z`. This adds an `until=` to the header's
`filters:` line. Whether to pin is the manager's call.

Command, from the repo root after merging lane/b91views (detached, as
KB-16 requires):

    cd /home/duxevents/pcrec-bench && setsid gnutimeout 14400 sh -c \
      'python3 scripts/regen_reports.py --pin-until-from-git > /var/tmp/b91regen.log 2>&1; \
       python3 scripts/regen_sidecars.py >> /var/tmp/b91regen.log 2>&1; \
       echo "DONE rc=$?" >> /var/tmp/b91regen.log' > /dev/null 2>&1 < /dev/null & disown

- **Completion line:** `DONE rc=…` in `/var/tmp/b91regen.log`. The driver's
  own summary line is `regen_reports: 74 group(s), N file(s) written, 0 group
  failure(s), 0 skipped (md-only)`.
- **Duration:** unmeasured for the whole set. Per group, it is 8 s
  (1-record) to several minutes (7–13 records). The utf8 group alone is
  ~165 s; the capability subject-grain PLAIN groups are the heaviest.
- **Then:**
  - diff-classify with GNU `diff` (never difflib, per b53regen);
  - `python3 catalogue/fixtures/gen.py --check` (`report_e` =
    after-b1885a83 moves: regenerate fixtures with `gen.py` if it reports
    drift);
  - `make check`.

Then `make check` itself (OWED):

    cd /home/duxevents/pcrec-bench && gnutimeout 3600 make check > /var/tmp/b91check.log 2>&1; echo "DONE rc=$?" >> /var/tmp/b91check.log

## Findings / not done

1. `did_not_compile` is still F26-exposed in `render_tsv`, because it lives
   inside the ranking-group loop. The new section shows the fix shape.
   Charter-adjacent, not done.
2. The committed utf8 predictions file refuses at load on the first sample
   (above).
3. P5.a, P9.b and R8 are now expressible, but the committed predictions file
   is not amended (ruling).
4. Rust declares unicode-class-scope unsupported on utf8 (5 rows). This is
   a data fact for the reading lane.

## Charter-vs-committed checklist

| charter item | status | artifact |
|---|---|---|
| (A) `unsupported_by_pattern` TSV section, per (pattern, form, testee) | DONE | `pcrecbench/report.py` `render_tsv` tail, `ReportData.unsupported_by_cell`; `test_unsupported_by_pattern_section_b91` |
| (A) interpret reads it; predictions can quantify | DONE | `interpret.py` `SECTIONS`/`_ELSEWHERE`; `rules.toml` R-PRED-1..4 inputs; demo P5.a/P9.b/R8 confirmed on the dry render |
| (A) catalogue MINOR bump + sabotage/control fixtures | DONE | catalogue 3.9; `R-PRED-1__unsupported-count-confirmed` / `R-PRED-2__unsupported-count-refuted`; `fixtures/sources/`, `predictions-unsupported.tsv` |
| (A) byte-identical for undeclared sets, proven per set | DONE | the proof table (email, loglines, bounded, altwide, syntax: version line only) |
| (B) matrix page selection, best + ratios recomputed client-side | DONE | `scripts/matrix_page.py` (`_selection_html`, `SELECTION_SCRIPT`, `data-ns`); `test_matrix_page.py` +3 |
| (B) TSV class-pure `best_*_yes/_no`, pooled column labelled pooled | DONE | `render_matrix_tsv`; `test_matrix_class_pure_best_columns_b91` |
| (B) F26 immunity proof + matrix tests green, extended | DONE | `test_matrix_all_refused_pattern_f26` (10-col parser), 101/0 and 15/0 |
| (C) identity bullet states per side who carries `program_sha256` | DONE | `_field_carriage(_text)`; `test_identity_bullet_per_side_b91`; `test_b88` amended |
| one REPORTER_VERSION bump | DONE | `v24 (2026-09-26)`; `test_reporter_version_pin` |
| validation: check-report, check-interpret, gen --check, check-schema | DONE | numbers above |
| utf8@0.1 dry render, path + invocation | DONE (not committed) | `build/b91-dry/…` in this worktree; the reading lane commits it |
| list reports needing regen + the command | DONE | above; `scripts/regen_reports.py` (new, committed) |
| the regen wave itself | OWED (manager) | command above; trigger: merge of lane/b91views |
| full `make check` | OWED (manager) | command above; trigger: after the wave |
| utf8 predictions load refusal (P10.a/P11.a globs) | OWED (ruling) | finding 2; owner manager/Frank; trigger: before the reading lane scores P1–P11 |
| P5.a/P9.b/R8 clauses in the committed file | OWED (ruling) | finding 3 |
| `docs/dev/plan.md` [B91] STATE | left to the manager (merge-time edit) | |
