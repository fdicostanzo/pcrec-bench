# pcrec trend report: the AI interpretation (design note, v0)

Status: v0, 2026-10-09, plan row [B130]. Required by
`pcrec_trend_report_v0.md` §5 before the interpretation is built. The CHECK
and the page SLOT are built (`tools/trend_cite_check.py`,
`tools/trend_html.py`); the text itself is written by a Claude session
(the manager's), and none exists yet.

## 1. Who writes it, and from what

- **Writer:** a Claude session in the manager's role, once per pin that has
  a trend page, after the window-close regeneration (`make trend`). A
  skill, `/pcrec-bench-trend-interpret <pin>` (OWED: to be written by the
  manager when the first interpretation is commissioned; it should mirror
  `/pcrec-bench-interpret`'s shape), runs the steps below. Model tier: the
  manager's own; no subagent is needed.
- **Inputs it may read:** `reports/trend/{summary,deltas,cells,compile_deltas,
  deny_twins,movers_by_stamp,interest,records}.tsv`, `config.toml`, and the
  deterministic interpreter's facts (`pcrecbench interpret`) for a report it
  names. **Nothing else**: not the store, not pcrec's source, not memory of
  earlier pins. Whatever it needs to know about a pin (the abi span, what
  changed) must already be a TSV column, or it is "not known".
- **Output:** `reports/trend/interpretation/<pin>.md`, committed, rendered by
  the page's AI-interpretation section for that pin. It is a sidecar, never
  edited into the TSVs or the page by hand.

## 2. Grounding rules (R9, R9+)

1. **Citation syntax.** A cited row is written `[#<row_id>]`. Ids are the
   `row_id` column of `deltas.tsv` (`D:...`), `summary.tsv` (`S:...`),
   `cells.tsv` (`C:...`), `compile_deltas.tsv` (`K:...`), `deny_twins.tsv`
   (`T:...`).
2. **Every claim cites.** Each paragraph or list item carries at least one
   citation, or starts with `NOT KNOWN:` and names what the TSVs cannot
   answer (a cause, a mechanism, a cross-window effect). Headings are
   exempt.
3. **No cause as fact.** The prose may connect rows to the attribution
   hints already in them (`identical`, `abi_span`, `stamp_changes`,
   `instrument_changed`, `wide_gap`, `drift_suspect`) and must say a cause
   is a hypothesis when it goes beyond them. The writer leads with the
   pair flags: an `instrument-changed` or `drift-suspect` pair is stated
   BEFORE any pcrec reading, as O-94/O-95 require.
4. **Direction and regime.** Ratios are new/old; regimes are never pooled
   (R15); auto-caps and auto-nocaps are never pooled (Q1).
5. **Deterministic facts first.** The TSVs are generated first; the prose is
   generated from them and checked afterwards. The prose never feeds back
   into any TSV.

## 3. The check (built)

`python3 tools/trend_cite_check.py reports/trend/interpretation/<pin>.md`
fails when a cited id does not exist (unknown id) or a block is uncited.
R9+: the id set is read from the TSV files by the checker's OWN parser; the
module imports nothing from `tools/trend.py` or `tools/trend_html.py`, so a
generator bug that invents an id cannot also make the check pass. The page
builder re-runs the check against the TSVs of the SAME run and renders a
"Interpretation REJECTED" card, not the prose, if it fails. `make
check-trend` runs the checker over every committed sidecar against the
committed TSVs. `tools/tests/test_trend.py` has the three arms (real id
accepted, invented id rejected, uncited claim rejected) and the ids-from-TSV
control.

What the check does NOT establish: that a cited row supports the sentence
citing it. That is the reader's job, and why the page labels the section
AI-written and tells the reader to read the rows. A future semantic check
(each number quoted in the prose must equal a field of a cited row) is OWED;
trigger: the first interpretation committed.

## 4. Template of a sidecar

    ## Pair flags
    - capability@0.2 vs capability@0.1 at c4c70f2c is instrument-changed and
      wide-pin-gap (abi span 9) [#S:capability@0.2:auto-caps-simdna:255bcdd8:c4c70f2c:short-subject-search].
    ## What moved beyond noise
    - ... [#D:...]
    ## Correctness
    - ... [#D:...]
    NOT KNOWN: which of the nine abi steps moved evil-alt-nested.
