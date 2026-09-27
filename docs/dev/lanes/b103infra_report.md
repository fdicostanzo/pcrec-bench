# lane b103infra report — the upstream-findings pipeline's infrastructure + migration

**Task**: [B103], `docs/design/upstream_pipeline_v1.md` §2/§3/§5/§7 — build
`docs/dev/upstream/` (registry, `repro/`, `notes/`, CLAUDE.md), `tools/upstream.py`
(`check`/`list`/`repro`/`new`/`status` + `make check-upstream`), self-tests
in the repo's existing style, migrate `docs/dev/upstream_findings.md`'s two
duplicate ids (the second `## U2`/`## U3` → `## U12`/`## U13`) and populate
`findings.tsv` with all thirteen findings at the status their narrative
supports. Sibling lanes `b103pcre2`/`b103other` own repro-building for
U1/U2(first)/U4/U5 and U6/U7/U8 respectively — not touched here.

**Branch**: `lane/b103infra`, `worktrees/b103infra`.

## Charter vs. committed

| charter item | status |
|---|---|
| `docs/dev/upstream/findings.tsv` (§2.1 columns exactly) | **DONE** — 13 rows, `python3 tools/upstream.py check` clean |
| `docs/dev/upstream/repro/`, `notes/` (empty, `.gitkeep`) | **DONE** — deliberately empty; no repro dirs created for ANY id, including U11 (see "design decision" below) |
| `docs/dev/upstream/CLAUDE.md` | **DONE** |
| `tools/upstream.py`: `check`/`list`/`repro`/`new`/`status` per §5 | **DONE** — all five subcommands smoke-tested end to end in a throwaway copy (`new` → write `run.sh` → `status REPRODUCED` → `repro` → `repro --record` → `status REPORTED` refused without `--tracker` → retried with `--tracker`/`--note` → accepted), not just `check` |
| `make check-upstream` (Makefile + `make check`'s list + `make help`) | **DONE** — seconds-scale, never runs an engine (`repro` is the one subcommand that does, and is not part of the target) |
| Self-tests: a small fixture set (good + sabotaged, each rejected for the rule its name claims), in the repo's existing style | **DONE, with a stated adaptation** — see below |
| Migration: second `## U2`/`## U3` → `## U12`/`## U13`, `formerly` lines, repo-wide citation grep + updates | **DONE** — see "migration" below for exactly what moved and what deliberately did not |
| Header paragraph pointing at registry/design note/status ladder | **DONE**, prepended to `upstream_findings.md` |
| One registry row per finding U1-U13, status decided from the narrative, reasoning stated per row | **DONE** — see table below |
| Proving batch (repro + tracker search + UNDERSTOOD-where-possible for U1/U2/U4/U5/U6/U7/U8; draft notes) | **NOT THIS LANE'S — by brief.** b103pcre2 owns U1/U2(first)/U4/U5; b103other owns U6/U7/U8. Nothing sent. |
| Update `docs/dev/CLAUDE.md`, `tools/CLAUDE.md`, root `CLAUDE.md` | **DONE** |
| Do NOT write the skill file | **RESPECTED** — not touched |
| `make check-upstream` + `make check-schema` run; not the full `make check` | **DONE** — both green (13/13 self-test cases, 13/13 findings clean; check-schema 6/6 examples + 74/74 sabotages unaffected) |

## Self-tests: the one deliberate adaptation of "the repo's existing style"

`schema/examples/bad/`'s convention is one committed `.jsonl` file per
rule, named by its leading token, checked via `validate.py --expect-reject
--expect-rule`. For a 13-column TSV registry this would mean roughly a
dozen near-duplicate multi-row TSV files differing in one cell each — a
heavier, harder-to-audit restatement of the same eleven-row table below,
for something small enough that `tools/CLAUDE.md` already documents a
lighter precedent (`check_id_preflight`'s `_write_synthetic_subbench`,
`check_rxt_export`'s `_StubSubbench`: "nothing this small earns a
standalone committed fixture file"). `tools/tests/test_upstream.py`
follows that precedent: one good in-tempdir fixture (three findings, one
at each of OBSERVED/REPRODUCED/REPORTED) that must come back with zero
issues, and twelve one-field mutations of it, each named for — and
asserted to fire EXACTLY — the rule it targets:

| case | rule | mutation |
|---|---|---|
| `good-fixture-clean` | (none) | the necessary positive control |
| `columns-header-mismatch` | COLUMNS | drop the last column |
| `kind-bad-token` | KIND | `"correctness-ish"` |
| `status-bad-token` | STATUS | `"REPRODUCE"` (typo) |
| `engine-bad-token` | ENGINE | `"unknownengine"` |
| `dup-id` | DUP-ID | append a second row with an existing id |
| `id-format` | ID-FORMAT | append a row with id `"U1x"` |
| `tsv-orphan` | TSV-ORPHAN | append a valid row with no narrative section |
| `narrative-orphan` | NARRATIVE-ORPHAN | append a narrative section with no row |
| `repro-missing-column` | REPRO | a REPRODUCED row's `repro` column set to `-` |
| `repro-incomplete-dir` | REPRO | delete `run.sh` from a REPRODUCED row's repro dir |
| `tracker-missing` | TRACKER | a REPORTED row's `tracker` set to `-` |
| `note-missing` | NOTE | a REPORTED row's `note` set to `-` |

All 13/13 pass (`make check-upstream` output quoted below). Two cases
(`id-format`, `tsv-orphan`) deliberately ADD a fresh row rather than
mutating an existing one, specifically to avoid a cascade into a second
rule (renaming an existing row's id would orphan its own narrative
section too) — the isolation schema's own convention insists on
("a control that fails for two reasons is not a control",
`schema/examples/bad/CLAUDE.md`) is preserved by fixture design, not by a
looser assertion.

```
== check-upstream ==
  PASS  good-fixture-clean           got=[] expect=[]
  PASS  columns-header-mismatch      got=['COLUMNS'] expect=['COLUMNS']
  PASS  kind-bad-token               got=['KIND'] expect=['KIND']
  PASS  status-bad-token             got=['STATUS'] expect=['STATUS']
  PASS  engine-bad-token             got=['ENGINE'] expect=['ENGINE']
  PASS  dup-id                       got=['DUP-ID'] expect=['DUP-ID']
  PASS  id-format                    got=['ID-FORMAT'] expect=['ID-FORMAT']
  PASS  tsv-orphan                   got=['TSV-ORPHAN'] expect=['TSV-ORPHAN']
  PASS  narrative-orphan             got=['NARRATIVE-ORPHAN'] expect=['NARRATIVE-ORPHAN']
  PASS  repro-missing-column         got=['REPRO'] expect=['REPRO']
  PASS  repro-incomplete-dir         got=['REPRO'] expect=['REPRO']
  PASS  tracker-missing              got=['TRACKER'] expect=['TRACKER']
  PASS  note-missing                 got=['NOTE'] expect=['NOTE']
test_upstream: 13/13 cases OK

check-upstream: OK -- 13 finding(s), 0 issues
```

## A design decision worth flagging: `REPRO_REQUIRED` excludes UNDERSTOOD alone

The design note's `check` bullet says "repro dir present and complete at
status ≥ REPRODUCED". Read as a strict linear rank over the FULL status
ladder (`OBSERVED < REPRODUCED < UNDERSTOOD < DRAFTED < ...`), that would
require a `repro/U<n>/` at UNDERSTOOD too — but §3 states in the same
breath "REPRODUCED and UNDERSTOOD may come in either order", which is
exactly the case this migration's own U11 is in (UNDERSTOOD by a
`PCRE2_NO_UTF_CHECK` ablation and a standalone C probe already archived
under `docs/dev/measurements/`, with no `docs/dev/upstream/repro/U11/`
built — that would be new engineering, not migration, and the brief
named U11 UNDERSTOOD without asking for a repro dir). Requiring repro/ at
UNDERSTOOD alone would make "either order" structurally unsatisfiable,
so `tools/upstream.py`'s `REPRO_REQUIRED` constant is
`{REPRODUCED, DRAFTED, APPROVED, REPORTED, FIXED}` — UNDERSTOOD
deliberately absent, everything from DRAFTED on present regardless (a
note can never cite a repro that does not exist). Flagged here and in
`docs/dev/upstream/CLAUDE.md` for the manager/Frank to overrule if the
intended reading was the strict one; the fix is one line plus a new
self-test case if so.

## The thirteen findings, decided from the narrative

| id | status | reasoning |
|---|---|---|
| U1 | OBSERVED | narrative ends "Next: reproduce with pcre2test... if the JIT genuinely lacks the prescan... that is reportable" — nothing beyond OBSERVED is claimed |
| U2 (first) | OBSERVED | narrative's own last line: "Status: OBSERVED." |
| U3 (first) | OBSERVED | narrative's own last line: "Status: OBSERVED; a pcre2test find-all count... would separate..." |
| U4 | OBSERVED | reading is explicitly "(unverified)"; no elevation claimed |
| U5 | OBSERVED | "Not chased further here — a read lane's job was to surface it, not attribute it"; no cause confirmed |
| U6 | OBSERVED | narrative literally says "OBSERVED, now REPRODUCED" and "REPRODUCED" appears in its own title, but the pipeline's REPRODUCED specifically means a standalone `repro/U<n>/` exists (§3) — that is b103other's owed work (U6 is explicitly withheld from this lane), so entering REPRODUCED now would immediately fail `check`'s own REPRO rule until b103other lands. Kept at OBSERVED; b103other's `status U6 REPRODUCED` will both build the repro and pass `check` in the same act. |
| U7 | OBSERVED | same reasoning as U6 — b103other's id, no repro/ built here |
| U8 | OBSERVED | narrative: "Status: OBSERVED. Not checked against RE2's issue tracker or source." |
| U9 | **NOT-A-BUG** | narrative's own words: "A SEMANTICS difference... not a bug"; brief's own steer ("U9/U10 likely NOT-A-BUG") confirmed by re-reading |
| U10 | **NOT-A-BUG** | narrative's own words: "This is a documented semantics difference, not a bug" (narrative's `Status:` line actually says UNDERSTOOD, but the finding's own terminal disposition — a documented Unicode-property difference, never to be sent — is NOT-A-BUG per §3's definition; UNDERSTOOD is a rung on the way to REPORTED, and nothing here is headed there) |
| U11 | **UNDERSTOOD** | brief's explicit instruction; narrative's own "Status: UNDERSTOOD" line, backed by a `PCRE2_NO_UTF_CHECK` ablation (source-level confirmation without a maintainer's answer, exactly §3's definition) |
| U12 (formerly 2nd U2) | OBSERVED | narrative: "Not a bug; a shape where 'jit = faster' does not hold... Next: none owed" — a characterization, not a claim of understood mechanism or a bug report |
| U13 (formerly 2nd U3) | **NOT-A-BUG** | narrative's own title already says "(OBSERVED 2026-08-30; NOT-A-BUG)"; "Documented PCRE2 behaviour (a repeated group is unrolled...)" |

`kind`: performance for every libpcre2/JIT-vs-interpreter/size finding
(U1-U5, U11-U13), correctness for U6 (wrong answers against the oracle,
not documented behavior), compatibility for U7 (refuses valid input other
engines accept), semantics for U8/U9/U10 (documented definitional
differences). `engine`/`engine_version` are `;`-joined for U10 (four
engines share one root cause) — a convention this lane extended from
`evidence`'s own `;`-join (§2.1), noted in `docs/dev/upstream/CLAUDE.md`.

## Migration: exactly what moved

In `docs/dev/upstream_findings.md`: the second `## U2` header →
`## U12` with a `(formerly the second U2 entry...)` line; the second
`## U3` header → `## U13` with the matching line; the one internal
self-reference inside the renamed U13 section ("Records as U2;") → "Records
as U12;"; a new header paragraph pointing at the registry, the design
note and the status ladder.

Repo-wide grep for `U2`/`U3` outside `store/` (excluded per the brief)
found the tokens heavily overloaded — `[B77]`'s UTF-8-set lane labels
U1-U5, an unrelated I-107 WAF-attribution test-numbering scheme (`U1/U2/U3`
in `outbox_to_pcrec.md`'s O-55 and this journal's own 2026-09-25 entry) —
so every hit was read in its full surrounding context before deciding,
never pattern-matched blind. Confirmed unambiguous citations of the
SECOND (duplicate) U2/U3, found ONLY in `docs/dev/dev_journal.md`:

- a session heading, 2026-08-30 fifth-session part 3: `"...KB-3/KB-4; U2/U3; docs/dev/ledgers/"`
- that session's body: `"U2 (pcre2-jit slower than interp on pure-scan find-all rows), U3 (PCRE2's group replication, NOT-A-BUG)."`
- the same day's part 6: `"...U2 re-measured. Reports lane: make check running; merge next."`

**These three were deliberately NOT edited.** `docs/dev/CLAUDE.md` states
`dev_journal.md` is append-only, and that is a stronger, structural repo
invariant than the migration brief's literal "update them... where they
unambiguously mean the second entry" — editing historical journal prose
would violate the one property (an unaltered crash-narrative record) the
file exists to guarantee. Instead this lane's own dev_journal.md entry
(this session, appended normally) states the correction and points back
here; nothing upstream of it changed. Flagging this explicitly since it
is a case where the brief's literal instruction and a stronger existing
convention pointed different ways, and the convention won.

Everything else found by the same grep was confirmed NOT to be the
duplicate ids and left untouched: `docs/dev/outbox_to_pcrec.md`'s
`"upstream_findings U2-U4"` (O-7, dated 2026-08-28 — the FIRST,
never-duplicated U2/U3/U4, predating the second U2/U3's 2026-08-30
creation) and its `"U2 the JIT lacks..."` line (also the first U2, the
required-code-unit finding); `docs/dev/known_issues.md`'s KB-30 `"not
introduced by U2"` ([B77]'s lane label, unrelated); `docs/design/CLAUDE.md`'s
two `[B77] U2` hits (same UTF-8 lane label); `docs/dev/ledgers/
2026-08-30-{bounded-0.1-first-sample-36d5963,abi12-after-96e44c2}.md`
(grepped directly — neither file contains the literal token `U2` or `U3`
anywhere, despite both being the ledgers that DERIVED the second U2/U3
findings; they describe the findings in prose without citing the id).
`docs/dev/plan.md`'s "upstream_findings U6" and `docs/design/upstream_pipeline_v1.md`'s
own `U1-U11`/`U2`/`U3` prose are about the pipeline design itself, not
stale citations to fix.

## Verification run

```
$ make check-upstream
== check-upstream ==
  [13/13 self-test cases PASS, listed above]
check-upstream: OK -- 13 finding(s), 0 issues

$ make check-schema
[...]
check-schema: 6 example(s) accepted, 74 sabotage(s) rejected for the intended rule, 0 sabotage(s) WRONG
```

Also smoke-tested (in a throwaway `/tmp` copy, never touching the real
registry) every subcommand end to end: `new` allocated `U14`, wrote the
row + narrative stub + `repro/U14/README.md`; `check` correctly stayed
clean at that point (U14's status is OBSERVED, which does not require a
repro — not a bug, an OBSERVED row simply has no repro requirement yet);
writing `repro/U14/run.sh` by hand and running `status U14 REPRODUCED`
set the `repro` column and passed; `repro U14` parsed the result line;
`repro U14 --record` wrote `latest_checked`; `status U14 REPORTED`
without `--tracker` was refused by name; the same call with
`--tracker`/`--note` succeeded and left the registry clean.

## Not done (owed, by charter — other lanes' or the manager's)

- `repro/U1/`, `repro/U2/`, `repro/U4/`, `repro/U5/` — b103pcre2.
- `repro/U6/`, `repro/U7/`, `repro/U8/` — b103other.
- Tracker searches, UNDERSTOOD write-ups, draft notes per engine — after
  the two repro lanes land, per the design note's proving-batch (§7).
- `.claude/skills/pcrec-bench-upstream/SKILL.md` — explicitly the
  manager's to write, not this lane's.
- `docs/dev/plan.md`'s `[B103]` row STATE — left at `started`; this
  lane is one of three, and the manager is the one who knows when all
  three have landed.
