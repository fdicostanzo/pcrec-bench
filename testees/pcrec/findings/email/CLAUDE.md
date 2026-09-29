# testees/pcrec/findings/email/ — [B115] the email findings bundle

Scratch-tier support for FINDINGS-BENCH-TIERS (inbox I-118, outbox O-72
Q4): PROFILED only, on the generated-prose throughput pair
(`t-d-prose-sparse-addrs`/`t-e-prose-no-at`) — no shipped bundle fits
`bench/email`'s shape, so DECLARED is n/a here (see README.md).

| file | role |
|---|---|
| `email-prose-profiled.rxt` | the PROFILED bundle, built by `pcrec-analyze` from a TRAIN generation of t-d/t-e only (never committed) |
| `list_analysis_email-prose-profiled.tsv` | `pcrec --list-analysis email-prose-profiled -I .` archived verbatim |
| `disjointness.tsv` | sha256-level proof over all five throughput ids: t-d/t-e disjoint from committed, t-a/t-b/t-c unmoved by `--seed` (the hand-curated control) |
| `README.md` | the build recipe, the disjointness proof, and the prerequisite (a scratch-tier pcrec at commit f7f5a143, never a re-pin) |

See `testees/pcrec/findings/loglines/CLAUDE.md` for the shared rationale
(R-BENCH-4, the scratch-tier prerequisite); this directory is its sibling
for the one sub-bench where DECLARED is n/a and PROFILED is scoped to one
regime.
