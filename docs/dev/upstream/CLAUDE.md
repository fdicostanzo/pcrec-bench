# docs/dev/upstream/ — the upstream-findings pipeline's machine-read half

[B103], `docs/design/upstream_pipeline_v1.md` (design of record). The
NARRATIVE half stays `../upstream_findings.md` (one `## U<n>` section
per finding, prose, evidence, reading); this directory is everything
that reads or writes it as data. pcrec is out of scope here — findings
about pcrec go to the pcrec manager's outbox, never this directory.

## Files

- `findings.tsv` — the REGISTRY: one row per finding, tab-separated,
  columns `id engine engine_version route kind status first_seen
  evidence repro latest_checked tracker note summary` (design note
  §2.1). `id` is `U<n>`, never reused (a renumbered id keeps a
  `formerly` line in the narrative — see U12/U13, 2026-09-27's
  migration). `engine`/`engine_version` may be `;`-joined when one
  finding spans several engines (U10); `route` is illustrative, not a
  closed vocabulary, so it is never validated. `status` is the design
  note's closed ladder (§3): `OBSERVED → REPRODUCED/UNDERSTOOD (either
  order) → DRAFTED → APPROVED → REPORTED → FIXED`, or one of the three
  terminal outcomes `NOT-A-BUG` / `KNOWN-UPSTREAM` / `STALE`. Edited
  only through `tools/upstream.py new`/`status`, or by hand followed by
  `make check-upstream`.
- `repro/U<n>/` — the STANDALONE reproduction per finding (§2.2):
  `README.md` (what it shows, engine + version, build/run, expected
  PRESENT vs ABSENT), the reproduction itself (preferably the engine's
  own tool, e.g. a `pcre2test` input file), `run.sh` (builds into
  `$UPSTREAM_SCRATCH`, runs, exits 0/1/2 = PRESENT/ABSENT/CANNOT-RUN,
  prints one final line `U<n> PRESENT|ABSENT|CANNOT-RUN <engine>
  <version> <evidence-number>`), and `expected.txt` (the verbatim
  output of the last PRESENT run, D35-style source header) once one has
  been run. Never generated from the bench's store at run time — a
  maintainer must be able to run it with no access to this repo beyond
  the one directory. Empty today (`.gitkeep` only): b103infra built the
  registry and the tool; repro/ directories are the two sibling lanes'
  and Frank's own proving-batch work (design note §7), not created here.
- `notes/<engine>-<YYYY-MM-DD>.md` — per-engine NOTE DRAFTS bundling
  findings for one maintainer submission (§4): a header block (the ids,
  the target channel, an approval line left blank until Frank fills or
  confirms it) plus one self-contained write-up per finding, in the
  maintainer's terms, not this project's. Empty today (`.gitkeep` only)
  — nothing is drafted before at least one finding here reaches
  REPRODUCED/UNDERSTOOD with a tracker search done.

## Tooling

`../../../tools/upstream.py` (see its own module docstring and
`tools/CLAUDE.md`) is the one interface onto `findings.tsv` and its
narrative twin: `check` (validates both files against each other and
the closed vocabularies, `make check-upstream`, never runs an engine),
`list`, `repro U<n>|--all` (the only subcommand that runs anything),
`new` (allocates the next id, stubs the row + narrative section +
`repro/U<n>/README.md`), `status` (moves a finding along the ladder,
refusing a move whose prerequisite — a complete `repro/`, a tracker, a
note — is not yet on disk).

## Design decision worth flagging

`check`'s repro-completeness rule reads the design note's "repro dir
present and complete at status ≥ REPRODUCED" as applying to
REPRODUCED/DRAFTED/APPROVED/REPORTED/FIXED but deliberately NOT to
UNDERSTOOD alone: §3 states "REPRODUCED and UNDERSTOOD may come in
either order", and U11 (this migration's own UNDERSTOOD row, confirmed
by a `PCRE2_NO_UTF_CHECK` ablation with no `repro/U11/` yet built) is
exactly the case that reading exists to allow. If a future reading of
the design note disagrees, `tools/upstream.py`'s `REPRO_REQUIRED`
constant is the one place to change it, and `tools/tests/test_upstream.py`
is the self-test that would need a case added for it.
