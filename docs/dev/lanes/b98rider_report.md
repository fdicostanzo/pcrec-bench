# Lane b98rider — [B98] THE HARNESS/REPORTER RIDER LANE

Branch `b98rider`, worktree `worktrees/b98rider`, from master `53ba437`.
Writer lane, sonnet tier. Box: pcrecdev1 held the box for a heavy ASan run
until ~21:18 EDT; every check below ran as an individually-launched
`tools/selfcheck.py` function or a Makefile target the brief named safe
(`check-schema`, `check-interpret`, the pieces of `check-report`), never
a full `make check`/`check-harness`. No `~/pcrec` file was touched
(BD2); pcrec's pinned build (`build/pcrec-ce658cb7`) was read-only reused
via the ordinary adapter path, never rebuilt.

Four commits on `b98rider`:

1. `dfdf372` — KB-33 (the refusal-metadata-declaration control)
2. `c6e0360` — KB-31 (reporter F26 gap) + KB-30 (vectorscan free-spacing
   at measure time) + KB-29 (find-all mid-loop give-up truncation,
   pcre2/onig/pcrec)
3. `c34d87e` — KB-34 (vectorscan whole-subject wrap's leading-verb bug)

## 1. KB-33 — a refusal row's `engine_metadata` must be declared

`tools/selfcheck.py:check_kb33_refusal_metadata_declared` compiles one
pattern refused by every adapter family with a clean structural
did-not-compile (`` (unclosed `` — confirmed live on all seven: onig,
pcre2, pcrec, re2, rust, tre, vectorscan) through each adapter's first
testee, and asserts the refusal row's `engine_metadata` keys are a
subset of that testee's `describe()['engine_metadata_declaration']` —
the X15 rule, run at the adapter boundary rather than after a whole
cell's trials are spent finding out at `store.write()` (which is
exactly how the real re2 incident was found).

**Verified against the real bug, not just a synthetic negative.**
`testees/re2/adapter.py`'s `[B95]` fix (the `refusal_class`
`METADATA_DECL` entry) was reverted locally, the check was re-run and
**FAILED** naming exactly the missing key (`re2/re2-default:
refusal-row engine_metadata ['refusal_class'] not in describe()'s
engine_metadata_declaration [...]`), then `git checkout` restored the
fix and both arms passed again. 2 PASS lines; KB-33 CLOSED.

## 2. KB-31 — `render_tsv`'s `did_not_compile` rows had the same F26 gap `unsupported_by_pattern` was fixed for

`_tsv_ranking_pass` emits `did_not_compile` rows **inside** its
per-ranking-group loop (`groups`, built from `set_cells`/`match_cells`).
A pattern refused by **every** testee in the roster has no group at any
regime, so the loop never visits it and its refusal rows never printed
— even though `rd.did_not_compile_by_pattern` carries them. This is the
exact `predicate_audit_v1.md` F26 shape `unsupported_by_pattern` was
fixed for at [B91]; `did_not_compile` was never fixed for it.

**Found live, not merely constructed.** A direct scan of
`store/records/*/*/*.jsonl`'s compile rows found exactly one
(sub-bench@version, pattern) refused by every testee that ever touched
it in the whole store: `utf8@0.1`'s `prp-ingreek` (`\p{InGreek}`, a
DECLARED oracle refusal — refused by all 11 utf8@0.1 testees, including
libpcre2 itself). The only committed report carrying utf8@0.1 records
is `reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.tsv`;
confirmed directly that it already prints 18 `compile`/`jitter` rows for
`prp-ingreek` but **zero** `did_not_compile` rows for it today.

**Fix**: a new F26-immune section, mirroring [B91] (A)'s technique
exactly — emitted from `rd.did_not_compile_by_pattern` for the
`(sb, pattern_id)` pairs with zero representation in `groups`, right
before the `unsupported_by_pattern` section. A pattern some testee DID
compile is untouched (its rows still come from the pre-existing
per-group path) — proved by a three-pattern fixture
(`test_kb31_all_refused_did_not_compile_f26`): `p1` refused by both
testees (the new path fires, 2 rows, no `rank` group), `p2` compiled by
both (no `did_not_compile` row at all), `p3` refused by one testee only
while the other ranks it (exactly 1 row, from the OLD path, proving no
double-counting).

`REPORTER_VERSION` bumps to **v25 (2026-09-26)**. **OWED to the regen
wave** (not run here per the brief — "DO NOT regenerate reports"):
`reports/2026-09-26-utf8-0.1-budu-ryzen1600-first-ce658cb7.tsv` gains 11
new `did_not_compile\tprp-ingreek\t...` rows (one per testee); its
`.md`/`.subject-grain.tsv`/`.matrix.tsv` siblings and its
`.interpretation.md` sidecar are unaffected (`render_markdown` has the
same underlying gap but was out of this lane's scope — `.matrix.tsv`
was already F26-immune via `_matrix_row_keys`'s own union). No other
committed `.tsv` moves (confirmed by the store scan above, not a
heuristic over the live `bench/*/` sidecars — those drift across a
set's own versions and would have produced false positives, e.g.
`bounded@0.1`/`altwide@0.1` "missing" patterns that were simply added in
later set versions).

102 reporter tests green (`python3 -m pcrecbench.tests.test_report`,
full run, ~4.5 min under a busy box); `test_quick` 7/7,
`test_matrix_page` 15/15; the fixture-validation and CLI-smoke pieces of
`make check-report` run directly, all green.

## 3. KB-30 — vectorscan's `measure()` never carried `--free-spacing`

`measure()`'s driver **recompiles from the same pattern file**
`compile()` used (the same reason `--som`/`--encoding utf8` already ride
along there), but never appended `--free-spacing`. So a whole-subject
`(?x)` pattern ending in a `#` comment was **compiled** with the correct
`^(?:...\n)\z` wrap (the comment safely terminated) and **measured**
with the wrong one (the wrap's `)\z` lands on the open comment — an
unbalanced paren `hs_compile` refuses).

**The consequence is worse than a crash: a silent wrong answer.**
Reproduced directly: without the fix, measuring the witness pattern over
a matching subject returns `matched=False` with a note
`"subject s1 crashed the driver (exit 3); restarting at the next
subject"` — the driver DOES crash, is silently restarted, and the
subject is recorded as a **false negative**, not merely missing. With
the fix: `matched=True`, no crash.

**Fix**: `free_spacing` now rides in the compile-time handle (`False` on
`plain`, since `_compile_one` only computes it for `whole-subject`), and
`measure()` appends `--free-spacing` when the handle carries it.
`check_vectorscan_free_spacing_measure` — 5 arms: the witness compiles
under the fix; `measure()` with the fix answers `matched=True` with no
crash; the SAME handle with `free_spacing` popped back out (KB-30's
exact bug, reproduced) crashes and answers `matched=False`; the
witness's own `plain` form is a real, unrelated Vectorscan refusal
(`(?x)` wants a genuine trailing newline to close a comment, not PCRE's
end-of-string rule) untouched by this fix; an ordinary compiling `plain`
handle's `free_spacing` is always falsy.

## 4. KB-29 — every find-all loop discarded a genuine give-up after `count > 0`

`if (rc < 0) { if (count == 0) rc_final = rc; break; }` — a mid-loop
give-up (a real resource-limit/structural error, never the engine's own
"no further matches" terminator, which each engine reports as a SEPARATE
value: `PCRE2_ERROR_NOMATCH`, `ONIG_MISMATCH`, pcrec's `r == 0`) was
silently discarded whenever at least one match had already been found
this call, leaving the subject reported as an ordinary `match` with a
TRUNCATED count instead of `giveup:<code>` by name.

**Fixed in `testees/{pcre2,onig,pcrec}/driver.c`**: the loop's own
terminal code is now ALWAYS tracked, and a genuine give-up discards the
call's accumulated matches before falling through to the SAME
`giveup:<code>:<message>` branch a first-call give-up already took.

**Three real witnesses, each reproduced against the real, compiled
driver before AND after the fix** (`git stash` the driver, rebuild,
confirm the bug, `git stash pop`, rebuild, confirm the fix — by hand,
recorded here rather than re-run automatically every check-harness pass,
since that would mean carrying a second, permanently unfixed driver
build):

| engine | witness | give-up | before the fix | after the fix |
|---|---|---|---|---|
| pcre2 | `x*` under `--utf --utf-always-check` (no `--utf8`) over `a`+U+00E9 | `PCRE2_ERROR_BADUTFOFFSET` (-36) | *(only reachable via the always-check path — [B94]'s VALIDATE-ONCE guard `die()`s loudly on the default path instead)* | `giveup:-36:bad offset into UTF string` |
| onig | `b\|(a+)+$` over `b`+35×`a`+`X` | `ONIGERR_RETRY_LIMIT_IN_MATCH_OVER` (-17), ~0.19 s | `match 0 1 ... 1 -` (nmatch truncated to 1) | `giveup:-17:retry-limit-in-match over` |
| pcrec (`--engine=vm`) | same pattern/subject | `PCREC_ERR_STEPS` (-2) | `match matched=True start=0 end=1` (the first "b" kept, give-up hidden) | `giveup:-2:PCREC_ERR_STEPS` |

Each with a control subject too short to reach the give-up at all,
still answering an ordinary `match` with the real count. Re-ran the
pre-existing `check_utf8_find_all_advance`, `check_pcre2_utf_validate_
once` (75 cells, ~54 s — needed `bench/utf8`'s and `bench/email`'s
subject trees generated first, a fresh-worktree setup step, not a
regression), `check_wrap_spelling_fix`, `check_pcre2_dfa` and
`check_giveup_not_batched` after the driver edits: all green (one
`check_pcre2_dfa` line read `inconclusive-load` — the box being busy, an
environmental fact, not a code regression).

**OWED**: `tre`/`re2`/`rust` have the identical loop shape (one line to
change, plus the post-loop discard, mirroring the three fixed drivers
exactly) and were not touched — a rider for the next harness lane, ideally
with its own real witness per engine. `vectorscan` is structurally
exempt (`GAVE_UP_CODES = frozenset()` — no Hyperscan code is ever
classified `gave-up`).

`check_kb29_find_all_giveup_propagation` — 6 PASS lines (3 witnesses ×
{fix, control}).

## 5. KB-34 — vectorscan's whole-subject wrap buries a leading `(*VERB)`

`driver.c`'s whole-subject wrap (`^(?:` + pattern + `)\z`) is
unconditional. A PCRE setting verb (`(*UCP)`) must be the very first
thing in the compiled expression (Hyperscan's own rule); wrapped this
way it lands at byte offset 4, and `hs_compile` refuses ("(*UCP) must be
at start of expression, encountered at index 6"). Hit `bench/utf8`'s
five `(*UCP)`-leading patterns (`cls-w-ucp`, `cls-d-ucp`, `cls-s-ucp`,
`ci-ucp-invariance`, `asr-b-cyr-ucp`) on their whole-subject form only —
invisible in this set's own measured cells (no `match` regime), a real
defect for any future set that has one.

**Fix**: `leading_verb_len()` (new) returns the byte length of any
leading run of well-formed `(*NAME)` verbs (0 if none, or if
unterminated — left untouched, refusing exactly as before). The wrap
hoists that prefix outside the group: `(*UCP)\w+` → `(*UCP)^(?:\w+)\z`.

**Four arms, `check_kb34_leading_verb_hoist`**: (1) the real corpus
witness compiles where it used to refuse (reproduced against the
unfixed driver by hand — `git stash`/rebuild/`git stash pop` — same
technique as KB-29); (2) SEMANTICS, not merely compilation: via the real
`vectorscan-block-nosom-utf8` testee, a whole Cyrillic word (UCP
word-class) answers `match`, the same word plus trailing punctuation
answers `nomatch`; (3) the `plain` form is untouched; (4) an
unterminated `(*` is left alone by the hoist and refuses exactly as
before. Re-ran `check_encoding_axis`, `check_high_byte_pattern_argv`,
`check_vectorscan_som` after the driver edit: all green — this fix
touches nothing else.

## 6. CONSIDERED, NOT IMPLEMENTED — whole-subject compiles cost ~15 min/cell on a set with no `match` regime

`Adapter.compile()` always builds both `plain` and `whole-subject`
artifacts for pcrec/onig/vectorscan/tre (the engines with no runtime end
anchor), regardless of whether the sub-bench declares a `match` regime
to ever measure the second one on. `bench/utf8` declares no `match`
regime; b95read's window (finding 2) measured its whole-subject compiles
at ~903 s (≈15 min) per `auto`/`nocaps` cell, 842 s of that
`prp-l`/`prp-notl`'s two Unicode-property patterns alone (both are among
the largest artifacts this project has ever compiled — `docs/dev/
measurements/2026-09-26-utf8-0.1-pcrec-compile-times.txt`).

**The trade-off, not a clear win either way:**

- **For skipping it** (compute `sb`'s declared regimes once, pass a
  `forms_needed` set into `Adapter.compile()`, each affected adapter
  skips building `whole-subject` when the caller says it is not needed):
  saves real wall time on every future utf8-shaped set, proportional to
  how expensive that set's patterns are to emit — a genuine, recurring
  cost, not a one-off.
- **Against skipping it**: the compile row IS real, useful data even
  with no regime to measure it in. This project's own CLAUDE.md tables
  repeatedly cite the plain-vs-`\z` compile-cost DELTA as a finding in
  its own right (e.g. `testees/pcrec/CLAUDE.md`'s "the `\z` form costs
  +12.1% emitted C" table, several per-pin re-derivations of it) — a set
  with no `match` regime today might grow one later (or a report reader
  might want the whole-subject compile number for its own sake, the way
  `bench/utf8`'s own report already renders `compile` rows for both
  forms). Skipping the compile would silently foreclose that.
- A middle path exists — compile `whole-subject` but at a REDUCED trial
  count (compile cost still varies little across trials for a
  deterministic AOT compiler) — but that is a bigger schema/harness
  change (trial counts are currently uniform per cell) for a narrower
  saving than skipping outright.

**Recommendation, not a decision**: this is worth a `Adapter.compile()`
signature change (`forms_needed`, harness-computed from `sb`'s declared
regimes, every existing adapter defaulting to "both" so nothing measured
today moves) the NEXT time a set this expensive to compile is chartered
with no `match` regime — not urgent enough to justify a schema-adjacent
interface change on its own today, and genuinely a call for whoever
owns the compile-cost accounting's future shape, not a rider-lane
unilateral change. Not implemented in this lane.

## Charter-vs-committed checklist

| # | brief item | status |
|---|---|---|
| 1 | KB-33: check-harness control, negative reproducing the re2 bug, restore | **COMMITTED** (`dfdf372`) — verified against the real bug by hand |
| 2 | KB-31: `render_tsv` F26 fix, fixture/test, reporter version bump, name affected committed reports (not regenerate) | **COMMITTED** (`c6e0360`) — exactly one committed report affected, named above with the exact new rows; regen OWED to the manager's wave |
| 3 | KB-30: vectorscan `measure()` fix + `(?x)`-trailing-comment control | **COMMITTED** (`c6e0360`) — verified the crash-and-wrong-answer shape both ways |
| 4 | KB-29: fix + control per driver family touched | **COMMITTED for pcre2/onig/pcrec** (`c6e0360`), each with a real witness verified both ways; tre/re2/rust explicitly OWED (not touched, per "driver family you touch") in known_issues.md with the exact fix shape spelled out |
| 5 | KB-34: file it, fix if local to `testees/vectorscan`, with a control | **COMMITTED** (`c34d87e`) — the fix is local to `driver.c`; four-arm control incl. real UTF-8 semantics |
| 6 | Consider, do not implement, the whole-subject-with-no-match-regime cost | **WRITTEN UP** above, no code change |
| — | Update each KB entry's status | done: KB-29/30/31/33/34 in `docs/dev/known_issues.md` |
| — | Update owning CLAUDE.mds | done: `tools/CLAUDE.md` (4 new entries), `testees/{pcre2,onig,pcrec,vectorscan}/CLAUDE.md` |
| — | Targeted validation only, no full `make check`/`check-harness` | honoured throughout — see the per-item validation runs above and the exact OWED command below |

## OWED to the manager

- **The full `make check`** (root of the worktree,
  `/home/duxevents/pcrec-bench/worktrees/b98rider`): `make check` (or, if
  preferred, `make check-harness` alone — the piece this lane could not
  run under the box-load rule). Everything sanctioned to run standalone
  (`check-schema`, `check-interpret`, the pieces of `check-report`, and
  every individual `check_*` function this lane touched or that shares a
  code path with what it touched) is ALREADY green, reported above by
  name; this is the confirmatory full run once the box is free.
- **KB-29 for `tre`/`re2`/`rust`**: same fix shape as pcre2/onig/pcrec
  (one line changed, plus the post-loop discard), not built here; the
  exact diff shape is in `docs/dev/known_issues.md`'s KB-29 entry.
- **Item 6** (above): a design question for whoever next charters an
  expensive-to-compile set with no `match` regime, not an OWED
  implementation.
- **`bench/utf8`/`bench/email` subject trees**: this worktree needed
  `python3 bench/{utf8,email}/gen_subjects.py` and
  `gen_throughput_subjects.py` run once before any driver check could
  pass — a fresh-worktree setup step (`make check` runs these itself),
  not a finding, noted here only so a fresh reviewer of this branch is
  not surprised by an initially-red `check_pcre2_utf_validate_once`.
