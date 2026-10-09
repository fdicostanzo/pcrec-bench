---
name: pcrec-bench-report-trend
description: Generate the pcrec TREND REPORT at a measurement window's close -- snapshot the new pcrec pin(s) from the store, propose cross-version links, run `make trend` / `make trend-check`, write the grounded AI interpretation `reports/trend/interpretation/<pin>.md`, run `make check-trend`, and commit with explicit paths. Use when a window has closed and the store/index has new pcrec records, when asked to refresh the trend report, or to interpret a pin's trend page. First member of the `pcrec-bench-report-<kind>` family (other reports later).
---

# /pcrec-bench-report-trend [<pin> ...]

Runs the whole window-close procedure for the pcrec trend report
(`docs/design/pcrec_trend_report_v0.md` section 8, interpretation rules in
`docs/design/trend_interpretation_v0.md`). Run every command from the
**repository root**. `<pin>` defaults to every `[[pin_order]]` pin that has
records in `store/index.tsv` but no `reports/trend/snapshots/<pin>.tsv.gz`.

## Preconditions (check, do not assume)

- The window is CLOSED: no `pcrecbench run` or lane timing job is running
  (BD3: one heavy suite at a time). The snapshot reads the store; the
  comparison does not.
- `store/index.tsv` is current (`python3 -m pcrecbench index` ran at close)
  and the new pin is appended to `catalogue/rules.toml` `[[pin_order]]`.
- Every long step below runs DETACHED with a completion marker, checked by a
  command (`setsid -w ... ; echo "DONE rc=$?" >> log`, or `nohup` under a
  tracked background task; `setsid` without `-w` returns at once). Never a
  blocking foreground call, never `ps` forensics.

## Steps, in order

1. **Snapshot** each new pin (the ONLY step that reads `store/`; nice 19;
   snapshots are IMMUTABLE and the command refuses to overwrite one):

       nice -n 19 setsid -w gnutimeout 3000 make trend-snapshot PIN=<pin> \
           > build/trend-snapshot.log 2>&1; echo "DONE rc=$?" >> build/trend-snapshot.log

   Then `python3 -c "import sys; sys.path.insert(0,'tools'); import trend_snapshot as T; print(T.verify_snapshot('reports/trend/snapshots/<pin>.tsv.gz'))"`
   must print `[]` (every stored set-grain row recomputes from its
   per-subject rows). Snapshot several new pins in `[[pin_order]]` order: a
   control/competitor record shared by several windows is stored inline once
   and referenced (`ref:<pin>`) by later snapshots.
   A snapshot written wrongly is never edited: `--force` is for a snapshot the
   manager has said to replace, and its diff must be reviewed.
2. **Links.** `make trend-links` prints the cross-version links the
   comparison would use but `reports/trend/links.tsv` lacks (a set moved to a
   new version over byte-identical subjects, ...). Review each proposed row
   (is the pattern/subject identity real? the `reason` column carries the
   cell counts), then append with `make trend-links ARGS=--write`. They land
   as `source=inferred`; they are in force at once, and the manager/Frank
   flips them to `confirmed` by editing the column. Until a link exists the
   pair is reported `unlinked` (never guessed): report any `unlinked` cells
   in the hand-back (`# unlinked_cells:` in `deltas.tsv`'s header).
3. **Compare.** `make trend` (reads snapshots + links + config only; a few
   minutes) then `make trend-check` (exit 0, 0 drifted). If a pre-existing
   TSV drifted, that is a finding: stop and read the diff (history files are
   append-only; a rewritten body is never expected).
4. **Interpretation** (`reports/trend/interpretation/<pin>.md`), per
   `trend_interpretation_v0.md` -- your inputs are ONLY the committed TSVs in
   `reports/trend/` and `config.toml`; not the store, not pcrec's source, not
   memory of earlier pins. Every paragraph/list item cites `[#<row_id>]` or
   starts `NOT KNOWN:`. Lead with the pair flags (`instrument-changed`,
   `drift-suspect`, `wide-pin-gap`, `unlinked`) BEFORE any pcrec reading;
   ratios are new/old; regimes and auto-caps/auto-nocaps are never pooled.
   A cause beyond the stamp/identity columns is a hypothesis, said so. Do not
   write one for a pin whose window the manager has not called clean.
5. **Check.** `python3 tools/trend_cite_check.py reports/trend/interpretation/<pin>.md`
   then `make check-trend` (the tests + every sidecar). Re-run `make trend` so
   the page renders the new sidecar; `make trend-check` again.
6. **Commit with EXPLICIT PATHS** (never `git commit -a`/`git add -A`: a window
   dirties `store/index.tsv` by design):

       git add reports/trend/snapshots/<pin>.tsv.gz reports/trend/links.tsv \
           reports/trend/*.tsv reports/trend/history reports/trend/index.html \
           reports/trend/index.md reports/trend/pins reports/trend/interpretation
       git commit -m "reports/trend: <pin> snapshot + regenerated ..."

   (`cells.tsv` is gitignored.) Push per the standing rule.

## Never

- Edit or rewrite an existing snapshot to make a number come out.
- Open `store/` from anything but `make trend-snapshot`.
- Hand-edit a generated TSV/HTML, or write an uncited claim.
- Invent a link: a pair without a link row is `unlinked`.
