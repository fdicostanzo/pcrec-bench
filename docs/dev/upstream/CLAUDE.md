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
  the one directory. b103infra built the registry and the tool with
  `repro/` empty (`.gitkeep` only); `repro/U1/`, `U2/`, `U4/`, `U5/`
  (2026-09-27, lane b103pcre2, the proving batch's libpcre2 quarter)
  are the first populated ones — each with README.md/run.sh/
  expected.txt, confirmed PRESENT on both the box's system libpcre2
  10.46 and a from-source PCRE2 10.48 build (the current release);
  U6-U8 (TRE/vectorscan/RE2) are the proving batch's other sibling
  lanes, per design note §7. `U7/run.sh` (2026-09-27, lane u7vs5413)
  gained `$UPSTREAM_ENGINE_BUILD` support (a vectorscan install prefix:
  `include/hs/hs.h` + `lib/libhs.so*`) so `tools/upstream.py repro U7
  --engine-build PATH --record` can point it at a from-source build,
  same convention as U1/U2/U4/U5; `U7/probe_5413_build.txt` is the
  archived from-source-build probe (D35-style header: tag, commit sha,
  every fetched-tool/dependency's own pin, compiler, CMake options) —
  the pattern for archiving a from-source engine build's confirmation
  beside a source-diff-only one.
- `notes/<engine>-<YYYY-MM-DD>.md` — per-engine NOTE DRAFTS bundling
  findings for one maintainer submission (§4): a header block (the ids,
  the target channel, an approval line left blank until Frank fills or
  confirms it) plus one self-contained write-up per finding, in the
  maintainer's terms, not this project's. `notes/pcre2-2026-09-27.md`
  (2026-09-27, lane b103pcre2) is the first one written, bundling
  U1/U2/U4/U5 for GitHub issues; its approval line is blank — nothing
  is drafted before at least one finding here reaches
  REPRODUCED/UNDERSTOOD with a tracker search done, and nothing is
  sent without Frank's word.
- `notes/replies/<thread-with-slashes-as-dashes>-<YYYY-MM-DD>.md` —
  ([B106]) DRAFT REPLIES to a `[NEEDS-ANSWER]` comment on an already-filed
  thread (a maintainer's question, or something addressed to
  `@fdicostanzo`), same posture as `notes/`: written for the maintainer,
  self-contained, and sent only on Frank's explicit word — `tools/
  upstream.py threads` never posts anything itself.
  `VectorCamp-vectorscan-416-2026-09-27.md` (2026-09-27, lane u7vs5413)
  is the first one drafted: markos's "could you please test against
  5.4.13?" (comment id 5859185642), answered with a real from-source
  5.4.13 build's confirmation (`repro/U7/probe_5413_build.txt`) — not
  yet sent.
- `threads.tsv` — ([B106], "track the ids of the issue threads, then a
  script to check for comments", Frank 2026-09-27) THE THREAD REGISTRY:
  one row per FILED GitHub thread (a thread can carry several finding
  ids, `;`-joined — the same convention `findings.tsv`'s own
  `engine`/`evidence` cells use), columns `thread` (`OWNER/REPO#N`,
  gh's own shorthand), `url`, `ids`, `filed`, `state` (`open`/`closed` as
  last seen), `labels` (`;`-joined, `-` if none), `comments_seen`,
  `last_seen_comment_id`, `last_seen_at` (the newest comment's own
  timestamp), `last_checked` (ISO time of the last successful
  `threads --record`). Seeded 2026-09-27 (lane b106threads) with the two
  threads Frank filed from his own GitHub account the same day:
  `PCRE2Project/pcre2#1015` (U1/U2/U4) and `VectorCamp/vectorscan#416`
  (U7). Grown automatically by `status U<n> REPORTED --tracker <GitHub
  issue URL>` (a new row if the URL is unseen, the id appended to an
  existing row's `ids` if not) — tracking starts at filing time, no
  separate step. Edited only through `tools/upstream.py status`/
  `threads --record`, or by hand followed by `make check-upstream`.

## Tooling

`../../../tools/upstream.py` (see its own module docstring and
`tools/CLAUDE.md`) is the one interface onto `findings.tsv`/its
narrative twin AND `threads.tsv`: `check` (validates all three against
each other and the closed vocabularies, `make check-upstream`, never
runs an engine), `list`, `repro U<n>|--all` (runs `repro/U<n>/run.sh`),
`new` (allocates the next id, stubs the row + narrative section +
`repro/U<n>/README.md`), `status` (moves a finding along the ladder,
refusing a move whose prerequisite — a complete `repro/`, a tracker, a
note — is not yet on disk; `… REPORTED --tracker <GitHub URL>` also
starts/grows that URL's `threads.tsv` row), and `threads [--thread
OWNER/REPO#N] [--record] [--json]` ([B106]) — the ONLY other subcommand
that runs something: one `gh api` GET per thread (the issue, its
comments paginated, its timeline best-effort), diffed against the row's
own stored state and printed as what is NEW (a state/label change, a
cross-reference, each new-or-edited comment with a `[NEEDS-ANSWER]` flag
when it contains a `?` or addresses `@fdicostanzo`). Exit 0 = nothing
new, 10 = something new, 2 = a `gh`/network error — `--record` is the
only thing that writes the seen-state back, same posture as `repro
--record`. Strictly read-only against GitHub: GET only, never a POST/
PATCH, so it can never itself comment, close, or label an issue.

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

`check`'s THREAD-MISSING rule ([B106]) requires a `threads.tsv` row at
REPORTED, FIXED **and** KNOWN-UPSTREAM (`THREAD_STATUSES_NEEDING_THREAD`)
— not REPORTED alone. FIXED is reached FROM REPORTED, so its tracker is
already a thread worth having kept watching (the maintainer's own
closing comment/commit is exactly the kind of thing `threads` surfaces);
KNOWN-UPSTREAM is a thread this project never filed but still points at
by URL, and an existing issue can still get a relevant answer worth
seeing. A non-GitHub tracker (a mailing-list URL, a bare
`searched:<date>:none-found` citation) is never required to have a row —
`threads.tsv`/`tools/upstream.py threads` only knows how to watch GitHub.
