# pcrec trend report — requirements (v0.1, DRAFT for comment)

Status: DRAFT, 2026-10-09. Asked for by Frank. Sent to pcrecdev1 for comment as
outbox O-93. Nothing is built yet. Plan row [B130].

## 1. Purpose

A STANDARD report that regenerates on every pinned bench run and answers one
question: **how did pcrec's numbers move, version by version?** It comes in two
forms over one dataset:

- **A. AI data:** machine-readable pcrec values per pin, with the change from
  the previous pin wherever the comparison is like for like. pcrec's sessions
  and the interpreter read it; nobody has to parse prose.
- **B. Human report:** highlights, charts, and an AI interpretation that is
  clearly labelled as such and cites the A-form rows it rests on.

Today this question is answered by hand, as the cross-pin probes behind O-12,
O-16 and O-92. This report makes it routine.

## 2. Scope

- **Subject:** pcrec testees only, every pinned config (auto, nocaps, vm,
  deny-flag twins, ...). Other engines appear only as DRIFT CONTROLS (R5).
- **Sets:** every `bench/*` set with pcrec records at two or more pins. The
  set@version boundary is handled by R3.
- **Axes:** match time per set cell; compile time; artifact size
  (`emit_bytes` / `emit_code_bytes`); correctness counts (wrong / gave-up /
  unsupported); and the route stamps (engine, prefilter, start, ...), so a
  move can be read beside the mechanism that moved.
- **Out of scope:** cross-engine rankings (the front page and `reports/` do
  that) and pcrec's own regression gate (pcrec's tests/bench/compare).

## 3. Requirements

**R1. One source, the store.**
- Every number comes from `store/` through `pcrecbench.reduce`, the reporter's
  own arithmetic.
- Every row carries the record paths it came from.
- Nothing is typed by hand (the front-page rule, [B127]).

**R2. Pin order.**
- Versions are ordered by `catalogue/rules.toml [[pin_order]]`.
- "Previous" means the newest EARLIER pin that has a comparable record for the
  same config and cell. A pin with no records, e.g. 60366d747 today, is
  skipped and named as skipped.

**R3. Like for like only.**
- A Δ is computed only on cells whose pattern bytes and subject bytes are
  identical across the two records (`canonical_sha256` plus subject sha), on
  the common subjects only. This is the rule O-92 used across
  capability@0.1 -> 0.2.
- A cell that is new or changed reads `new` / `not comparable`, never a Δ.

**R4. Noise rule.**
- A move counts only when the two cells' trial [min, max] ranges are disjoint
  (the front page's tie rule).
- Otherwise it reads `within noise`, and the ratio is still printed.

**R5. Drift control.**
- Each Δ table carries the same-cell ratio of a non-pcrec engine measured in
  both windows (default pcre2-jit, whose version is unchanged). This puts a
  number on box drift.
- If the control's median ratio leaves a declared band (proposed 0.97-1.03),
  the pair is flagged `drift-suspect`.

**R6. Attribution hints, not claims.**
- Each Δ row carries the abi span and the [[pin_order]] notes between the two
  pins, plus whether the program is identical (`program_sha256`, v2 identity).
- Program-identical with a moved time means drift or layout. Program changed
  means pcrec's own change. The report never names a cause beyond these facts.

**R7. Form A, the AI data.**
- TSV files under `reports/trend/`, schema-stable and versioned:
  - `cells.tsv`: one row per (set@ver, config, pattern, regime, form, pin),
    with value, trial min/max, correctness and stamps;
  - `deltas.tsv`: one row per comparable (cell, pin, previous pin), with
    ratio, noise verdict, control ratio, identity and abi span;
  - `summary.tsv`: per (set, config, pin pair): moved-faster, moved-slower,
    within-noise, median and geomean ratio, the largest movers.
- A header carries the generator version, the index sha and the generation
  time.

**R8. Form B, the human report.**
- One page per new pin, plus a rolling index page:
  - top highlights: the largest improvements and regressions beyond noise,
    and correctness changes, especially gave-up -> judged and judged -> wrong;
  - charts: per-set ratio distributions per pin pair, and a per-config
    timeline of the set median;
  - an "AI interpretation" section, labelled as such.
- Published like the front page: HTML on the Pages site, with a markdown copy
  in `reports/`.

**R9. AI interpretation discipline.**
- The interpretation is GROUNDED: every sentence cites `deltas.tsv` /
  `summary.tsv` row ids, or interpreter facts (`pcrecbench interpret`).
- It may connect facts to attribution hints (R6) and name what is NOT known.
- It never states a cause as fact without a citation.
- The deterministic facts are generated first; the prose is generated from
  them, and a check verifies that every cited id exists.

**R10. Updates with runs.**
- `make trend-report` regenerates both forms.
- `scripts/run_window.sh` and the window-close routine call it after a pinned
  window, the way the interpretation sidecars regenerate today ([B41]).
- It runs detached, because it loads the store (KB-16).
- `--check` detects drift between the committed files and the store.

**R11. Corrections.** When a record is superseded, e.g. an
inconclusive-spread record followed by a re-measure, the report uses the
superseding record and says so. It never silently mixes the two.

## 4. Open questions (for pcrecdev1 / Frank)

- **Q1.** Which pcrec configs matter for the TREND view: all pinned configs, or
  auto / nocaps / vm plus the twins of the current acceptance items?
- **Q2.** Should compile time and artifact size get their own highlight
  section, or only appear in A-form data?
- **Q3.** Is pcre2-jit the right single drift control, or should each set name
  its own?
- **Q4.** Does pcrec want the A-form deltas pushed to the outbox at each pin,
  as an O-n pointer, or just committed?
- **Q5.** Should the trend use a single "headline config", pcrec-auto, as the
  front page does, plus a full table?
- **Q6.** Anything pcrec's optimisation loop needs that a per-pin delta table
  does not give? For example, a per-pattern history across many pins, or
  movers grouped by mechanism stamp.

## 5. Not decided here

The TSV column lists, the chart forms and the HTML layout come at build time.
The interpretation's model and prompt get their own short design note before
they are built.
