# The upstream-findings pipeline — v1 (design)

Status: DESIGN, 2026-09-27 (thirty-fifth session, manager; Frank: "consider
it as an ongoing process with consistent interface/reports and any helper
scripts … consider a skill if there is session work"). Plan row [B103].

## 1. Purpose

The bench keeps finding behaviour in OTHER engines: wrong answers,
performance cliffs, compatibility gaps. Today these sit as narrative
sections in `docs/dev/upstream_findings.md` (U1-U11; two ids used twice,
none sent upstream). v1 makes this an ongoing process: every finding moves
through fixed stages, carries a minimal standalone reproduction that a
script can re-run, and ends as either a note sent upstream (on Frank's
approval) or a recorded reason for not sending one. The same interface
applies to every engine and every session.

pcrec is out of scope. Findings about pcrec go to the pcrec manager
(outbox), never here.

## 2. Surfaces

    docs/dev/upstream_findings.md       the NARRATIVE (kept; one `## U<n>` section per finding,
                                        evidence + reading; append-mostly, sections updated in place
                                        when status moves)
    docs/dev/upstream/findings.tsv      the REGISTRY: one row per finding, machine-read
    docs/dev/upstream/repro/U<n>/       the minimal standalone REPRODUCTION per finding
    docs/dev/upstream/notes/<engine>-<YYYY-MM-DD>.md
                                        per-engine NOTE DRAFTS bundling findings for one upstream
    docs/dev/upstream/CLAUDE.md         the directory map
    tools/upstream.py                   the helper CLI (§5)
    .claude/skills/pcrec-bench-upstream/SKILL.md
                                        the session procedure (§6)

### 2.1 `findings.tsv` columns (tab-separated, header row, one row per id)

| column | meaning |
|---|---|
| `id` | `U<n>`, never reused; a renumbered id keeps a `formerly` note in the narrative |
| `engine` | engine family token as in `testees/` (`pcre2`, `re2`, `vectorscan`, `tre`, `onig`, `rust`) |
| `engine_version` | the version the finding was observed on (e.g. `10.46`) |
| `route` | the specific API/route (`jit`, `interp`, `dfa`, `block-nosom`, …) or `-` |
| `kind` | `correctness` · `performance` · `compatibility` · `semantics` |
| `status` | §3 |
| `first_seen` | ISO date |
| `evidence` | ledger path(s) / record id(s), `;`-joined |
| `repro` | `docs/dev/upstream/repro/U<n>/` or `-` (required at status ≥ REPRODUCED) |
| `latest_checked` | the newest upstream release the repro was run against, `version@date`, or `-` |
| `tracker` | the upstream issue URL / search done (`searched:<date>:none-found`), or `-` |
| `note` | the note draft that carries it, or `-` |
| `summary` | one line, no tabs |

### 2.2 `repro/U<n>/` contents

- `README.md` — what it shows, the engine + version it targets, how it is
  built/run, the expected PRESENT output and what ABSENT (fixed) looks like.
- the reproduction itself: preferably the engine's own tool (`pcre2test`
  input file) — a maintainer runs it without our code; else the smallest
  self-contained C/C++/Rust file linking only the engine.
- `run.sh` — builds (if needed) into a scratch directory given by
  `$UPSTREAM_SCRATCH` and runs it; exits **0 = PRESENT** (behaviour
  reproduced), **1 = ABSENT** (not reproduced / fixed), **2 = CANNOT-RUN**
  (engine or toolchain missing), and prints one final line
  `U<n> PRESENT|ABSENT|CANNOT-RUN <engine> <version> <evidence-number>`.
  Performance repros state their threshold (e.g. "PRESENT if the ratio
  ≥ 10×") and run single-core, short (seconds), median of ≥ 5.
- `expected.txt` — the verbatim output of the last PRESENT run, with a
  source-information header (date, box, engine version, pin) — D35 style.

Sources must not be generated at run time from the bench's store; a repro
is standalone by construction (a maintainer never sees our repo).

## 3. Status ladder

    OBSERVED      seen in bench records; a reading may exist, unverified
    REPRODUCED    repro/U<n>/ exists and returns PRESENT on the observed version
    UNDERSTOOD    cause confirmed (source reading, ablation, or maintainer answer)
    DRAFTED       included in a notes/ draft
    APPROVED      Frank approved sending that note (record the date in the narrative)
    REPORTED      sent; `tracker` holds the URL
    FIXED         upstream fixed it; `latest_checked` shows ABSENT on the fixed version
    terminal, not sent:
    NOT-A-BUG     documented/intended behaviour, or a semantics difference
    KNOWN-UPSTREAM an existing upstream issue already covers it (`tracker` holds it)
    STALE         ABSENT on the current upstream release before we sent anything

REPRODUCED and UNDERSTOOD may come in either order; the registry holds the
furthest reached. Nothing leaves the repo without APPROVED: sending is an
outward act in Frank's name, per note.

## 4. Notes (`notes/<engine>-<date>.md`)

One per upstream per batch, written for the maintainer, not for us: no
bench jargon, no pcrec references beyond one sentence of context, each
finding self-contained (version, minimal input, expected vs actual, the
repro inline or attached), performance findings with numbers + box + method
in two lines. A header block (ours) lists the ids, the target channel
(issue tracker / mailing list), and the approval line left blank until
Frank fills or confirms it.

## 5. `tools/upstream.py`

Stdlib python3, no store load, subcommands:

- `check` — validates `findings.tsv` (columns, tokens, unique ids, every
  id has a `## U<n>` narrative section and vice versa, repro dir present
  and complete at status ≥ REPRODUCED, `tracker` set at REPORTED/
  KNOWN-UPSTREAM, `note` set at ≥ DRAFTED). Wired into `make check` as
  `make check-upstream` (seconds; runs no engine).
- `list [--engine E] [--status S]` — the table, readable.
- `repro U<n>|--all [--engine-build PATH]` — runs `run.sh`, collects the
  PRESENT/ABSENT line; `--engine-build` points a repro at a different
  engine build (the latest-release check). Never writes the registry
  silently: `--record` updates `latest_checked` explicitly.
- `new --engine E --kind K --summary …` — allocates the next id, appends
  the registry row and a narrative stub, creates `repro/U<n>/README.md`.
- `status U<n> <STATUS> [--tracker URL] [--note PATH]` — moves a status,
  enforcing §3's prerequisites.

## 6. The skill (`pcrec-bench-upstream`)

Session work recurs: a read lane files a new finding; a new engine release
lands; a batch is ready to draft; Frank approves a note; an upstream
answers. The skill holds the procedure for each, so any session (or lane)
runs it the same way: file (`new`, narrative, evidence), reproduce (write
repro, run, `expected.txt`), check the tracker (search; record), draft (a
note per engine), after approval record sending, periodic re-verify
(`repro --all` against the newest releases, stale → STALE/FIXED). The
manager skill's review step points read lanes at it when they find
another engine's behaviour.

## 7. Migration (v1's first delivery)

- The two duplicate ids: the SECOND `## U2` and `## U3` become U12 and
  U13, each with a `formerly U2 (second entry)`-style line; every citation
  of them found by grep is updated.
- All thirteen findings enter `findings.tsv` at their current status
  (OBSERVED unless the narrative shows more; U3b is NOT-A-BUG; U11 is
  UNDERSTOOD; U9/U10 are NOT-A-BUG candidates — decided by the migrating
  lane from the narrative, stated).
- Proving batch: repro + tracker search + UNDERSTOOD-where-possible for the
  send-worthy ones — libpcre2 U1, U2, U4, U5; RE2 U8; vectorscan U7; TRE
  U6 — and one draft note per engine that has at least one REPRODUCED
  non-NOT-A-BUG finding. Nothing is sent.
