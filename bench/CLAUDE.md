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

`subjects/` and `throughput/` are GENERATED and gitignored; the
generators and their sha256 manifests are committed, and `make check`
regenerates both and requires the manifests to reproduce byte for byte.
