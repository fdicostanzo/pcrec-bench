# reports/trend/snapshots/ -- per-version snapshots ([B130.2])

One file per pinned pcrec version: `<pin>.tsv.gz`, written ONCE by
`make trend-snapshot PIN=<pin>` (`tools/trend.py snapshot`, format in
`tools/trend_snapshot.py`'s docstring and `docs/design/pcrec_trend_report_v0.md`
section 8). Deterministic gzip (mtime 0, level 9). IMMUTABLE: the command
refuses to overwrite one without `--force`, and a snapshot is never edited by
hand. Together with `../links.tsv` and `../config.toml` these are the ONLY
inputs of `make trend`; the record store is not read by the comparison, so a
record may be deleted from `store/` once its pin is snapshotted ([B96]).

A control or competitor record shared by several windows is stored inline in
the first snapshot that needed it and referenced (`data = ref:<pin>`) by later
ones, so a snapshot is not self-contained for those records: keep the files
together (they are all committed). Keep every version -- trends over time.
