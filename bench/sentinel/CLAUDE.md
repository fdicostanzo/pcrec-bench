# bench/sentinel/ — the INSTRUMENT SENTINEL set (`sentinel@0.1`, [B133])

A small fixed list of short-call, program-identical cells measured FIRST in
every suite (scripts/run_suite.sh, `SENTINEL=0` skips) for pcrec-auto,
pcrec-nocaps and pcre2-jit; how to read it is NOTES.md. Everything here is a
byte copy of bench/capability@0.2 — nothing is authored.

| file | role |
|---|---|
| `subbench.toml` | sidecar; `[[patterns]]` blocks DERIVED from capability's (gen_patterns.py --check); regime `search_short` only |
| `gen_patterns.py` | copies the 14 members + floor-byte from bench/capability/patterns/; `--check` / `--sidecar` |
| `patterns/*.rx` | the 15 patterns, committed |
| `gen_subjects.py` | regenerates capability's 75 short subjects into `subjects/` (gitignored) via capability's own `build()`; `manifest.tsv` is byte-identical to capability's (checked) |
| `manifest.tsv` | committed |
| `gen_expectations.py`, `expectations.tsv` | the shared oracle derivation; 1,125 rows |
| `export/sentinel.rxt` | GENERATED (tools/export_rxt.py), round-tripped by `make check-harness` like every non-.rxt-sourced set |
| `NOTES.md` | objective, contents, the program-identity caveat, how a window report reads it |
