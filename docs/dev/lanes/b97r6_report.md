# Lane `b97r6` — close [B97]'s one OWED item: R6, read from per-record stamps

Branch `lane/b97r6`, worktree `worktrees/b97r6` off `master` at `16be34f`.
Docs only: a script + its archived output under `docs/dev/measurements/`,
one new ledger file under `docs/dev/ledgers/`, and the pointer/plan-log
updates the boilerplate requires. No code, no store, no report, no
catalogue touched; `~/pcrec` never read (this task needed only committed
bench-side files: the record store and `bench/utf8/patterns/*.rx`).

## Charter vs. committed

| brief item | committed |
|---|---|
| Read the addendum's §7 first, understand exactly what is missing | done — `compile_stamp` is a per-TESTEE legend (one row per config, empty pattern/subject columns), not per-pattern telemetry; confirmed directly against the report TSV before writing anything |
| Narrow streaming read of per-pattern compile-row `engine_metadata` (engine/engine_sel/prefilter/req_byte/req_run/whatever R6's text needs) from `store/records/utf8@0.1/*/*.jsonl`, modeled on the addendum's own extract script, NEVER the whole-store loader, NEVER a report render | done — `docs/dev/measurements/2026-09-26-utf8-0.1-r6-addendum-extract.py`: streams the four `pcrec_ce658cb7_*-utf8` JSONL files (136,048 lines / ~54 MB total) line by line, keeps only `kind=="compile" and trial==1` rows and only that row's `engine_metadata` dict — everything else, including every `match` row, is discarded immediately |
| Check RAM stays small (the records total 155 MB) | done — `/usr/bin/time -v python3 …`: 0.82 s wall, 99% CPU, **15,748 KB (15.7 MB) peak RSS**, printed verbatim in the archived `.txt`'s own header |
| Archive the script + its verbatim output there | done — `.py` and `.txt` both committed under `docs/dev/measurements/`, source-headed per that directory's D35-style rule |
| Write R6's scoring as a SECOND addendum file, the first addendum never edited | done — `docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7-addendum-r6.md`; confirmed `2026-09-26-utf8-0.1-first-ce658cb7-addendum-r2r7.md` untouched (`git status`/`git diff` clean on it before this lane's first commit) |
| Rule text as stated pre-run, cells selected by name with values, verdict, what was NOT read | §1-§8 of the new ledger |
| pcrec-directed findings listed as candidates for the manager only (no outbox) | §9 — zero pcrec-directed findings; one bench-side wording note about R6's own text and the forced-VM population (see below) |
| Pointer lines in `ledgers/` and `measurements/` CLAUDE.mds | both updated, same commit |
| End with the charter-vs-committed checklist | §10 of the new ledger |

## What R6 actually found

All four of R6's named sub-checks (the fourth, "the offset-skip rows...",
is F-C6's own declared narrowing of the rule, not a separate rule) came
back **clean — no engine-selection surprise on this sample**:

1. `cls-lead-pair` (UD §6.3's own worked witness) CONFIRMS the prediction
   exactly: `dfa_prefilter=byte-class` on both DFA-route configs, never
   `memchr` — checked against an unplanned control (`cls-high-range`,
   three lead bytes) reading the same mechanism, so it is not a
   two-lead-byte-specific coincidence.
2. The two control-twin families that actually compile on pcrec
   (`qnt-lazy-2b`/`qnt-plus-2b`; `ci-ascii-control` against its
   six-member fold family) show IDENTICAL `engine`/`engine_sel` on every
   member, on both the DFA-route and forced-VM configs. The one place the
   fold family's own `dfa_prefilter` VALUE splits (`byte-class` for the
   ASCII-fold members, `memchr` for the two Cyrillic/Greek ones) is not
   an engine-route divergence — it tracks a real byte-structure fact
   (does case-folding change the pattern's own lead byte?), explained in
   the ledger's §3 rather than flagged as a surprise.
3. The offset-skip population beyond P1 (`lit-run-3`, `lit-mixed-ascii`,
   `alt-shared-char`) reads mechanism-appropriate `req_byte`/`req_run`/
   `dfa_prefilter` stamps (the run capped at 8 bytes on `lit-run-3`, the
   3-byte common alternation prefix on `alt-shared-char`, the `offset-set`
   mechanism on `lit-mixed-ascii`'s ASCII-then-high-byte shape) with no
   divergence between `auto` and `nocaps`.
4. The corpus-wide "declined prefilter" census on the DFA route (4 of 69
   compiling plain-form patterns read `dfa_prefilter=none`) is fully
   explained by anchoring or a zero-width, matches-almost-everywhere
   assertion (`\A…\z`, `^…$`, `\B`) — none has an unfiltered strong
   lead-byte set.

**One thing worth flagging that is NOT a pcrec finding:** the forced-VM
route's `prefilter=none` reads 67 of 67 on BOTH `pcrec-vm-utf8` and
`pcrec-vm-in-utf8` — including the four lookbehind patterns that `auto`'s
own analysis gives a REAL hybrid prefilter to on the identical pattern
text. This is not a decline to score: `testees/pcrec/CLAUDE.md` line 13
already documents `--engine=vm` as "the VM forced, **prefilter off**, so
the VM derives the whole span independently" — the flag is defined to
skip the prefilter-build step entirely, not to attempt-and-decline it per
pattern. The ledger's §5 states this explicitly so a future R6 reading
does not mistake the forced-VM population's uniform `none` for 67
separate surprises; §9 lists it as a bench-side wording note for the
manager, not an outbox item.

## Validation

No `make check*` target reads `docs/dev/ledgers/` or
`docs/dev/measurements/`, so nothing to re-run there. The extraction
script's own numbers were spot-checked against a second, independent
`python3 -c` query (the four lookbehind patterns' `prefilter`/
`vm_prefilter_lang` values under `auto`, quoted in the ledger's §5) before
being cited, per the project's "controls that share no source" habit.

## Commits

Single lane, docs-only: the extract script + archive, the new addendum
ledger, the two CLAUDE.md pointers, and a `plan.md` note marking [B97]
ready for the manager to close (not closed by this lane — completion/
archival is the manager's call). Not merged; branch left for the manager.
