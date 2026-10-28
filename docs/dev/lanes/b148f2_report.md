# b148f2 report -- [B148] F2 SQLite subjects (docs/design/unusual_set_v1.md 4.2)

Branch lane/b148f2. No timing, no downloads (the vendored xz only), ~/pcrec untouched.

## What was built
- `gen_streams.py` gains `sqlite-bodies` and `sqlite-bodies-s` (F1 shape: `manifest_streams.tsv`
  row + `calls/<id>.tsv` + `streams/<id>.bin`). The xz is decompressed IN MEMORY after checking
  its sha256 against `vendor/sqlite3.c.xz.sha256`; nothing decompressed is written outside the
  gitignored `streams/` tree. F1 rows (seg-s, seg-l) are byte-identical to before.
- Locator (regex-free, `unusual_lib.ref_scan` as judge): a function opens at a column-0 line
  ending in `{` (not struct/union/enum/typedef/extern) or a lone `{`; it closes at the next line
  starting `}` and counts only if that line is exactly `}`. Segment = `(?{ <body with braces> })`,
  kept iff `ref_scan` accepts it whole.
- `--check` materializes missing outputs (verified: deleted the -s stream + calls, `--check`
  restored them) and compares present ones.

## Numbers (SQLite 3.54.1, 271,132 lines)
| | sqlite-bodies | sqlite-bodies-s |
|---|---|---|
| calls | 4,971 | 311 |
| stream bytes | 5,451,204 | 377,590 |
| segment bytes (denominator) | 5,023,466 | (see manifest) |
| local refusals | 0 | 0 |
| matched / nomatch | 4,971 / 0 | 311 / 0 |

- BODY COUNT: 4,971, not the design's ~10^4 / ~7 MB (the file has 5,103 column-0 `}` lines).
  9 candidates were refused by the scanner (excluded, never calls: line numbers e.g. 51071,
  51151, 97181 -- not investigated further), 106 column-0 brace blocks closed by `};`/`} name;`
  (initializers/types) were not functions.
- Sample rule (P14): bodies with 0-based index = 0 mod 16 in source order = 311; its filler has
  its own seed (20261030; full stream 20261029), filler = the F1 filler.
- Every call matches by construction (all located bodies are scanner-valid), so these streams
  carry no negative calls; the F1 streams carry the no-match population.

## Expectations
`expectations_stream.tsv`: 8 rows (4 streams x cscan, cscan-onig), method
`libpcre2-differential`: libpcre2 (interpreter) AND `ref_scan` agree per call on the full span
and group 1 (any disagreement aborts). Both methods answer all 2 x (4,971 + 311) calls, no
declines needed: libpcre2 cost on these bodies is negligible (probe: 311 calls 0.09 s, worst
call 2.8 ms at a 55 KB body). Whole `gen_expectations.py` run 2:24, RSS 724 MB; the pre-existing
ORACLE_DECLINED set (nest-brace-100k x2) unchanged.

## Other edits
`skipped_subjects.tsv` (sqlite ids removed; 5 kernel ids remain), `NOTES.md`, `CLAUDE.md`,
`gen_patterns.py` description text + regenerated `subbench.toml`, `check_set.py`: stream row
count 5 -> 9; item 6 no longer RUNS `fetch_sqlite.py` (it is pinned now and would DOWNLOAD) --
it checks the vendored xz sha256, `fetch_kernel.py` refusal, the 5 kernel skips and the sqlite
stream invariants.

## Checks
`check_set.py --full`: 18 checks, 0 failed (includes `gen_expectations --check`, 2999 rows, 8
stream rows; log /var/tmp/pcrecbench/b148f2/chk.log). Not run: the repo-wide `make check`.

## Findings / owed
- `gen_subjects.py`/`gen_throughput_subjects.py --check` do NOT materialize missing subject
  trees (only the stream generator does); `gen_expectations.py` fails on a fresh worktree until
  they are run without `--check`. Not touched here.
- The viewer/trend/frontpage skip tables, drivers and the harness consume the new streams
  unchanged (generic over `manifest_streams.tsv`); no cell was run.
