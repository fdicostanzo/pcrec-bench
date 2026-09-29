# testees/pcrec/findings/loglines/ — [B115] the loglines findings bundles

Scratch-tier support for FINDINGS-BENCH-TIERS (inbox I-118, outbox O-72):
never read by a pinned config, never in `store/`. Nothing here is
bench-shaped ([B31]'s R-BENCH-4 — pcrec-shaped files live under
`testees/`, not `bench/`).

| file | role |
|---|---|
| `loglines-profiled.rxt` | the PROFILED bundle, built by `pcrec-analyze` from a TRAIN generation (never committed — see README.md) |
| `list_analysis_weblog.tsv` | `pcrec --list-analysis weblog` archived verbatim (DECLARED arm 1) |
| `list_analysis_log.tsv` | `pcrec --list-analysis log` archived verbatim (DECLARED arm 2) |
| `list_analysis_loglines-profiled.tsv` | `pcrec --list-analysis loglines-profiled -I .` archived verbatim (the PROFILED arm) |
| `disjointness.tsv` | sha256-level proof: 0 TRAIN/TEST collisions on both the search band and throughput manifests |
| `README.md` | the DECLARED/PROFILED build recipe, the disjointness proof, the grep-for-a-bench-path control, and the prerequisite (a scratch-tier pcrec at commit f7f5a143, never a re-pin) |

Regenerating: `scripts/findings_tiers.sh` (or the README's own commands by
hand). The `.rxt` file is the only artifact of this directory a compile
ever reads; the four TSVs are provenance, read by a person or by
`tools/selfcheck.py:check_b115_tune_analysis_axis`'s cross-check, never by
`pcrecbench` itself.
