# bench/ — the sub-benches

One directory per sub-bench (harness contract §2, requirements §5): a
self-contained unit with a GOAL, its canonical patterns, its
deterministically generated subjects, its oracle-verified expectations,
and its per-engine notes. Versioned as a unit; records compare only
within one `id@version`.

`pcrecbench/subbench.py` is the loader and the ONE place the regime →
subject mapping and the two regime spellings (the directory's
`match`/`search_short`/`throughput` and the record schema's
`match-compliance`/`short-subject-search`/`large-subject-throughput`)
are translated.

| directory | what it is |
|---|---|
| `email/` | the RFC 5322 specimen: `orig.rx` (hand-inlined) and `factored.rx` (the same language via `(?&name)` calls), 85 short subjects + five 1 MB throughput subjects (three periodic + two generated-prose non-periodic, [B17]/I-10) |
| `loglines/` | LOG-LINE SEARCH over mostly-failing text ([B11.1], inbox I-7 §1): ten patterns operators grep logs with + the floor, 112 chunks of mixed-format log text at 279-3772 B (~93 % of the member cells `nomatch`) and a 16 KB - 1 MB size sweep in three flavours. Shaped around ONE axis -- whether PCRE2's required-code-unit dismissal is available for a pattern -- with three patterns where it is not available at all as the control; the measurement pcrec's [OPT-5] is built or not on. Declares `search_short` + `throughput` only, and `short_search_max_bytes = 4096` |

`subjects/` and `throughput/` are GENERATED and gitignored; the
generators and their sha256 manifests are committed, and `make check`
regenerates both and requires the manifests to reproduce byte for byte --
for EVERY directory here, by enumeration (`tools/selfcheck.py`'s
`subbench_dirs()`, [B11.1]), never by name. The same pass re-derives each
sub-bench's `expectations.tsv` and any other `gen_*.py --check` table the
directory carries, and smokes a real driver on each set's floor pattern
against the oracle.

A sub-bench declares WHICH REGIMES it exercises and a SUBSET is legitimate:
`loglines` declares no `match` regime (a chunk of log lines is not a
candidate string to validate whole -- its NOTES.md says so at length), and
`subbench.py`'s `subjects_for()`, `harness.run_cell()` and the record schema
(`regimes`, `minItems: 1`) all take the declared subset as-is.

The manifests may carry COLUMNS BEYOND the contract's four: `periodic`
(inbox I-10) is the first. The loader reads the header and carries the
extras by name (`Subject.extra`, `Subject.periodic`); a four-column manifest
parses exactly as it always did.
