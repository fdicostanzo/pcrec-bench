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
| `bounded/` | BOUNDED REPEATS on both axes ([B11.4]): ten everyday bounded shapes (`\d{4}`, `[0-9a-f]{32}`, `.{8,64}`, `.{80,}`, a dotted quad, a CSV record, and a bounded lazy gap before a `\b` alternation at counts 64 / 256 / 1024 + its greedy twin) and a nineteen-rung COUNT LADDER (`[a-z]{0,n}` for n = 64 .. 65535 -- eleven factor-of-2 rungs to PCRE2's own ceiling, the @0.2/[B21] KNEE-bracketing ladder, with `[a-z]{0,1024}` beside the group body `(?:a|[b-z]){0,1024}` as the group-vs-class pair -- the open and lazy forms, two- and three-deep nests, an ambiguous letters nest) + the floor; 30 generated short subjects (fields with near-misses that fail at the last repetition, ≤ 256 B lines of near-miss ops prose, class runs on the rungs) and five large runs (a small and a large on BOTH content axes since @0.2) in a `throughput` regime that is the ladder's top rungs under find-all, NOT a size sweep. The give-up axis is the COUNT: the predicted first pcrec refusal (the abi-11 emitted-size cap) is at the 32768 rung, and the oracle's own edges per skeleton are a committed, re-derived table (`oracle_limits.tsv`). `short_search_max_bytes = 512` |

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
(`regimes`, `minItems: 1`) all take the declared subset as-is. The
`throughput` regime need not be a SIZE sweep either: `bounded` declares it
for four runs sitting on its count ladder's top rungs ([B11.4]).

The manifests may carry COLUMNS BEYOND the contract's four: `periodic`
(inbox I-10) is the first. The loader reads the header and carries the
extras by name (`Subject.extra`, `Subject.periodic`); a four-column manifest
parses exactly as it always did. A sixth column is NOT accepted (the loader
takes 4 or 5), which is why `bounded` puts a subject's family and ARM into
the `description` column in a fixed spelling rather than a column of its own.
