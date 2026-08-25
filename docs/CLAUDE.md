# docs/ — project working documents

Process and status documents for pcrec-bench. The charter itself lives in
../APPROACH.md; these files track execution against it. The layout
deliberately parallels ~/pcrec/docs/ (Frank, 2026-08-24) so a reader of
either project finds the same kinds of file in the same places — lighter
weight here, the same rules.

## Subdirectories

- `dev/` — development-process documents: the plan (grep'able STATE
  tags), the append-only journal, the decision log, the gitignored wake
  brief, and the map of pcrec documents this project depends on. See
  `dev/CLAUDE.md`.
- `design/` — living design documents: the requirements note, the
  artifact schema design, the set-format position, adapter designs, with
  panel outcomes and refutations recorded inline. See `design/CLAUDE.md`.

No `spec/` yet: a spec directory is chartered when the first user-facing
surface (the artifact schema, a CLI) is built and needs an as-built
contract separate from its design history.

Maintenance: update this file when files/subdirectories are added/removed
or their roles change. Every directory gets a CLAUDE.md.
