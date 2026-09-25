# [B77] lane U4 — bench/utf8/ patterns + sidecar — report

Worktree `agent-a9d8cc9be7828fcca`, branch
`worktree-agent-a9d8cc9be7828fcca` (this worktree's auto-provisioned
name, off master `0a11090`; not a `lane/b77u4` branch — the manager
should re-home the commit onto one at merge if that matters to the
merge workflow). Charter: `docs/design/utf8_set_v1.md` v0.2 §13's U4 row, the sections it
points at (§5 the families, §7 the roster), `docs/dev/lanes/b77u3_report.md`
and `docs/dev/lanes/b77u2_report.md` (the witness census this lane
transcribes from), `bench/capability` and `bench/syntax` as the format
precedent. Read in full before writing anything, per the brief.

## Charter-vs-committed checklist

| brief item | committed | notes |
|---|---|---|
| `patterns.rxt` as the source of truth, with its `ext bench` roster block | `bench/utf8/patterns.rxt` (917 lines, 76 blocks: 75 members + floor) | rendered by `gen_patterns.py`; `oracle pcre2`, `vocabulary family/hazard/requires` (the six tokens this set uses, a subset of `pcrecbench.capability`'s 20-token global vocabulary), `tag set=utf8, version=0.1`, the `ext bench` roster/capability matrix |
| `gen_patterns.py` rendering `patterns/*.rx` with `--check` | `bench/utf8/gen_patterns.py` (620 lines) + `bench/utf8/patterns/*.rx` (76 files) | `--check` re-derives `patterns.rxt`, every `.rx` file AND `provenance.tsv`, diffing all three against the table; no pcrec `--list-source` round-trip is wired (see "What was deliberately NOT built" below) |
| the sidecar / `subbench.toml` making `bench/utf8` ENUMERABLE by `make check`'s generic gates | `bench/utf8/subbench.toml` (842 lines) | `id="utf8"`, `version="0.1"`, `regimes=["search_short","throughput"]` (no `match`, per §10.1), `short_search_max_bytes=512`, `[expectations] encoding="utf8"` (U1's set-wide oracle flag), `[[patterns]]` array (`gen_patterns.py --sidecar`'s output, pasted by hand); no `rxt_source=` key (a deliberate deviation from `bench/capability`'s post-[B42]-switch model — see CLAUDE.md) |
| `provenance.tsv` | `bench/utf8/provenance.tsv` (77 lines) | one row per pattern, `pattern_id, family, provenance_source, source_url, source_ref, license, retrieved, fidelity, adaptation, attribution` — every row `authored`/`n-a`/`synthesized` (this is a correctness/encoding census, not a wild-provenance set) |
| fix `alt-cyr64-hit`/`-miss` once the 64-branch list exists, verified by the oracle under UTF | done — see "The alt-cyr-64 word list" below | |
| `prp-ingreek` has no subject BY DESIGN, stated explicitly | stated in `bench/utf8/CLAUDE.md` ("What is NOT built here") and, pre-existing from U3, in `bench/utf8/CLAUDE.md`'s U3 section and `gen_subjects.py`'s own docstring | U4 did not need to add this statement — U3 already made it; U4's own contribution is confirming `prp-ingreek`'s pattern block compiles cleanly as text (the `.rxt` block itself, not the oracle — see the U5 handoff note below) |
| `bench/utf8/CLAUDE.md` | rewritten (was U3-only) | full file listing, the STUB explanation, the alt-cyr-64 derivation, the ext-bench-roster corrections, the "why no `rxt_source`" note, regenerating instructions, what's NOT built (U5's scope) |
| `docs/design/utf8_set_v1.md` §13 U4 row brought to reality | NOT edited this lane — see "Owed" below | the design note's own U4 row already describes what U4 was chartered to build; I did not edit the design note itself (out of scope: the brief's deliverables list `bench/utf8/CLAUDE.md`, not the design note) |
| stub `expectations.tsv`/`NOTES.md` if the generic gates require one, smallest possible | `expectations.tsv` (98 rows, floor pattern only) + `gen_expectations.py` (a STUB, stated as such in its own docstring); `NOTES.md` NOT stubbed | the gates DO require an `expectations.tsv` stub (see "Why a stub was required" below); they do NOT require `NOTES.md` (confirmed by reading every `NOTES.md` reference in `tools/selfcheck.py` — none is a generic, enumeration-driven gate) |
| report with charter-vs-committed checklist + U5 cost estimate | this file | |

## Why a stub `expectations.tsv` was required (not optional)

The moment `subbench.toml` exists, `bench/utf8` is enumerated by
`tools/selfcheck.py`'s `subbench_dirs()` and TWO generic `make
check-harness` gates touch it unconditionally:

- `check_expectations()` runs `gen_expectations.py --check` on every
  enumerated sub-bench and fails if it errors or disagrees.
- `check_floor_pattern()` runs a REAL `pcrecbench quick --testee
  pcre2-jit --regime search --pattern floor --subjects 5` cell on every
  enumerated sub-bench's floor pattern, which needs a real expectation
  row for the floor pattern (`Subbench.expectation()` raises when none
  exists for the (pattern, subject, regime) triple it is asked about —
  confirmed by reading `pcrecbench/harness.py`, which reads expectations
  from the COMMITTED `expectations.tsv`, never a live oracle call).

`gen_expectations.py` here is a genuine, not-faked derivation — it
calls the SAME shared oracle chain every other set's generator uses
(`pcrecbench.expectations.derive`) — but restricted to the ONE pattern
those two gates actually need (the floor, `~`), over EVERY subject in
EVERY regime the set declares (91 search_short + 7 throughput = 98
rows). This is cheap (the floor is a single ASCII byte) and real. The
other 75 patterns carry no rows; a `quick`/`run` cell against any of
them will raise until U5's real derivation lands — stated in both the
generator's own docstring and `bench/utf8/CLAUDE.md`.

## The one id bug this lane found and fixed

Loading `bench/utf8` for the first time (once `subbench.toml` existed)
immediately raised: `asr-B-midchar` violates the record schema's slug
rule (`^[a-z0-9]([a-z0-9-]*[a-z0-9])?$` — lowercase only). The design
note's own table (`utf8_set_v1.md` §5(e)) spells the id with an
uppercase `B` for readability; the actual bench pattern id cannot carry
one. Renamed to `asr-b-midchar` everywhere: the pattern id
(`gen_patterns.py`), the subject id and its description
(`gen_subjects.py`, `asr-b-midchar-hit`), and every derived artifact
(`patterns/asr-b-midchar.rx`, `manifest.tsv`, `subject_facts.tsv`,
`provenance.tsv`). This is the kind of bug KB-12 (`bench/syntax`'s
incident) exists to catch early — caught here at `Subbench()`
construction time, before any cell ran, because `check_id_preflight`'s
generic gate is unconditional the moment a set is loadable.

## The alt-cyr-64 word list

`utf8_set_v1.md` §5(d) charters `alt-cyr-64` as "64 Cyrillic words,
`|`-joined" without naming them; b77u3's two coordinating subjects
(`alt-cyr64-hit` = "дом", `alt-cyr64-miss` = "квинтэссенция") were typed
against an ASSUMPTION about that list. `gen_patterns.py`'s
`_alt_cyr_64_words()` derives the 64 branches from the committed
`pool_cyr.tsv` (175 rows, one word per line after the header): **the
LAST 64 rows, in file order.** This was a deliberate choice, not an
arbitrary one — "дом" sits at row 144 of 176 (inside that slice) and
"квинтэссенция" is absent from the pool ENTIRELY (no selection could
include it), so this slice satisfies both coordination assumptions by
construction. Two structural asserts in `_alt_cyr_64_words()` enforce
this at every regeneration (the exact row count and both facts).

**Verified against the real libpcre2 oracle, not merely asserted
structurally**, as the brief required:

    pattern bytes: 663 (the rendered alt-cyr-64 .rx file)
    oracle.compile(pattern, PCRE2_UTF)
    search("дом".encode("utf-8"), 0)              -> match[0, 6)
    search("квинтэссенция".encode("utf-8"), 0)    -> nomatch

`gen_subjects.py`'s two descriptions were rewritten from
"assumes.../U4 COORDINATION" hedges to "CONFIRMED" (with the exact
match/nomatch facts above cited), and `manifest.tsv` was regenerated.

## The ext bench roster — transcription, and two corrections

Every `capabilities <config>` line in `patterns.rxt`'s `ext bench` block
is TRANSCRIBED from lane b77u2's own witness census
(`docs/dev/measurements/2026-09-25-b77u2-utf8-witness-census.txt`, its
DECLARATIONS block and summary table) and `utf8_set_v1.md` §7.4 — never
re-guessed, per the brief. Twelve roster configs, six REQUIRES tokens
(this set's own subset: `utf8-encoding`, `ascii-class-scope`,
`unicode-class-scope` from the census; `lookaround`, `true-end-anchor`,
`unicode-properties` carried over from each engine's pre-existing
capability, since those three are encoding-independent facts about the
engine, not new census findings).

Two places this lane's OWN evidence overrode a naive carry-forward,
stated in `bench/utf8/CLAUDE.md` and here:

1. **`tre-default` does NOT get `true-end-anchor`** in this set's
   roster, even though `bench/capability/patterns.rxt`'s own roster
   declares it for `tre-default`. `testees/tre/CLAUDE.md`'s measured
   finding is unambiguous: TRE has NO `\z`/`\A`/`\Z` tokens at all (a
   literal `\z` compiles as literal `z`), and `utf8_set_v1.md` §7.4
   itself cites exactly this fact for `asr-a-z`'s exclusion on TRE. I
   read `bench/capability`'s declaration as likely wrong (a stale
   over-declaration nobody's `asr-a-z`-shaped pattern ever tripped, since
   capability has no such pattern to test it against), not as evidence
   to follow. I did NOT fix `bench/capability`'s own file (out of this
   lane's mandate) — flagging it here as a candidate finding for
   whoever owns that set next.
2. **`onig-utf8`/`re2-utf8`/`vectorscan-block-nosom-utf8`'s
   `unicode-class-scope` satisfaction follows the b77u2 RE-CENSUS**, not
   `utf8_set_v1.md` §7.6's v0.2 draft prediction: vectorscan is
   SATISFIED (inline `(*UCP)` honoured per pattern under `HS_FLAG_UTF8`
   alone — the census's own §A correction), onig/re2 are NOT (`(*UCP)`
   refused outright by both).

Verified end to end (not just eyeballed): loading the real subbench and
calling `pcrecbench.capability.capabilities_for`/`missing_capabilities`
against several (config, pattern) pairs confirmed the matrix resolves as
intended — e.g. `tre-default` satisfies `{ascii-class-scope}` only, so
`asr-a-z` (`true-end-anchor` + `utf8-encoding`) is correctly
`unsupported-by-declaration` there with BOTH missing tokens named.

## Why no `rxt_source =`

`bench/capability/subbench.toml` sets `rxt_source = "patterns.rxt"`
(the [B42] sidecar switch), which makes `patterns.rxt` the FULLY LOADED
pattern source. This set does not set that key: `subbench.toml`'s own
`[[patterns]]` array (pointing at `patterns/*.rx`) is the loaded source,
and `patterns.rxt`'s `ext bench` block is read separately through
`pcrecbench.capability`'s SIDECAR/SHIM path (`rxt_source.
load_aux_rows()`, triggered by the file's mere presence beside
`subbench.toml` — no key needed; confirmed by reading
`pcrecbench/capability.py`'s own `_load_matrix()`, path (b)). This is
the two-artifact split `bench/capability` used BEFORE its own switch —
chosen here deliberately, not by oversight, since the full-loader path
was untested against a fresh set and switching to it is not what the
brief asked for. Stated in `bench/utf8/CLAUDE.md` as a named,
reconsiderable choice for a future lane.

## What was deliberately NOT built (and why each is a defensible cut)

- **No pcrec `--list-source` round-trip in `gen_patterns.py --check`.**
  `bench/capability/gen_patterns.py`'s own `check_list_source` resolves
  a HARDCODED build path (`build/pcrec-cd371441/build/pcrec`) that is
  now several re-pins stale at the current pin (6ef76820) — meaning that
  check likely already silently degrades to "binary not found" there.
  Rather than repeat a check that goes stale on every re-pin, this
  lane's `gen_patterns.py --check` is structural-only (the table
  re-derives `patterns.rxt` + `patterns/*.rx` + `provenance.tsv` byte
  for byte). The `ext bench` block's actual runtime correctness WAS
  verified, just via the harness's real loader (`pcrecbench.capability`
  through a real `Subbench()`) rather than a raw `pcrec --list-source`
  parse — see above.
- **`NOTES.md`** — not a generic-gate requirement (confirmed above);
  U5's charter item.
- **The real 76-pattern `expectations.tsv`** — U5's charter item; the
  stub is the smallest structurally-required substitute. See the cost
  estimate below for why doing this for real was out of scope for a
  single lane's time budget.
- **`docs/design/utf8_set_v1.md`'s own U4 row** — not edited; the brief's
  deliverable list did not include the design note, and the note already
  correctly describes what U4 was chartered to build.

## The U5 cost estimate (timed, not modeled)

The brief asked for a timed small sample extrapolated against the "UTF
derivation is ~30× slower than byte mode" claim. What was actually
measured, on this box, against the real `pcrecbench.expectations.derive`
(the same function `gen_expectations.py` calls, unrestricted per
pattern/regime — never the stub):

| what | result |
|---|---|
| `search_short` regime, ANY single pattern (91 subjects, all ≤ 512 B) | **2-10 ms** — six patterns sampled across families (floor, cls-dot, lit-run-3, ci-moskva, asr-lb-varwidth, cls-w-ucp), all near-instant |
| `throughput` regime, a NON-dense pattern (floor, lit-run-3: each matches a handful of times over ~1.6 MB) | **5-12 ms** |
| `throughput` regime, `cls-dot` (`.`, matches EVERY character) alone | **exceeded 300 s (killed by `gnutimeout 300`, exit 124), still running** |

The mechanism (read from `pcrecbench/oracle_pcre2.py`'s `_find_all_impl`):
each match advances `pos` by exactly one character and issues ONE
ctypes call into libpcre2 (`_search_raw`) per match — the same per-match
Python/ctypes overhead `bench/syntax/CLAUDE.md` already documents
("the six dense class patterns — `\w+`, `\p{L}+`, … — find-all ~200k
matches per MB through one ctypes call each"). `cls-dot` over this
set's ~1.6 MB `throughput` corpus is on the order of 1.5-1.6 MILLION
individual matches — a MUCH denser case than `bench/syntax`'s own `\w+`,
since `.` in UTF-8 mode matches every character with no filtering at
all, and the set's `mix`/`cjk`/`cyr` corpora are 1-3 bytes/character
rather than `bench/syntax`'s ASCII prose.

**A first attempt at a 10-pattern representative sample (all regimes,
unrestricted) exceeded 600 s (10 minutes) without finishing at all** —
the sample deliberately included several of the property/class family's
densest members (`prp-l`, `prp-notl`, `alt-cyr-64`) alongside cheap ones,
and was abandoned once the per-pattern breakdown above made the cause
clear.

**The honest extrapolation, stated as a bound rather than a fabricated
point estimate.** Of the 76 patterns, roughly 25-31 are structurally
"dense" over at least one throughput subject — every `+`/`{n,}`-quantified
class or property construct with no anchor and no narrow alphabet:
family (a)'s eleven `+`-quantified classes (`cls-boundary-range`,
`cls-high-range`, `cls-neg-allhigh`, `cls-mixed`, `cls-w-ascii`,
`cls-w-ucp`, `cls-posix-alpha`, `cls-lead-pair`, `cls-neg-cjk`, plus
`cls-dot`/`cls-dot-rep`), family (d)'s `qnt-dot-bounded`/`qnt-class-run`,
and most of family (f)'s twelve `\p`/`\P` members (`prp-l`, `prp-lu`,
`prp-n`, `prp-notl`, `prp-zs`, `prp-cyrillic`, `prp-han`, `prp-latin` —
`prp-l-anchored`/`prp-greek`/`prp-greek-sc` are cheaper, single-match or
anchored). If even HALF of those cost what `cls-dot` alone already
demonstrably costs (≥ 5 minutes each, extrapolating from the ~30×
byte-mode-slowdown figure the task brief cites and the measured
per-match ctypes overhead), **the real 76-pattern `expectations.tsv`
derivation is on the order of ONE TO SEVERAL HOURS, not minutes** — this
is a LOWER BOUND from measurement, not a fabricated total (a true upper
bound was not obtained; nothing was measured for the full corpus).

**Two concrete recommendations for U5, both cheap and neither
requiring new machinery:**

1. **Cap the property-class family's throughput subjects, or make
   `derive()` accept a per-pattern subject-count override.** Every
   `search_short` row is already near-free; the cost is ENTIRELY the
   `throughput` regime's find-all loop on dense patterns, and the
   design note's own §4.3 already allows a per-generator lever
   (`utf8_set_v1.md` §10.3's "drop the per-script 64 KB arm" precedent
   for a DIFFERENT cost problem — the SAME kind of lever applies here:
   derive the dense patterns' throughput rows against `t-64k` only,
   dropping `t-256k`/`t-1m`/the four per-script 64 KB arms for those
   patterns specifically, and say so in `NOTES.md`).
2. **Run the real derivation DETACHED, per the lane boilerplate's
   long-run rule**, not inline in a `--check` cycle — `gen_expectations.py
   --check` for this set must NOT be assumed to run in the same few
   seconds every other set's does; if U5 leaves the stub's structure in
   place but widens the pattern set, it should budget the run as a
   background job with a completion marker, not a foreground wait.

**A related compile-axis finding for U5, found while reasoning about
`prp-ingreek`:** `derive()`'s call to `oracle.compile(text,
oracle_option_word(...))` is OUTSIDE the per-subject try/except that
catches `oracle.Pcre2Error` — it only guards `match`/`search`/
`find_all`. `prp-ingreek` (`\p{InGreek}`) is DESIGNED to refuse at
compile time (error 147, no such Unicode block). If U5's real
`gen_expectations.py` simply widens this lane's stub to all 76 patterns
without change, deriving `prp-ingreek`'s row will likely CRASH the whole
derivation with an unhandled compile error rather than skip it
gracefully — U5 needs either a compile-refusal skip list (this pattern's
own row legitimately has NO expectations, `utf8_set_v1.md` §5(f)'s own
"no match rows" ruling for the refusal witness) or a try/except around
the `oracle.compile()` call itself. Not fixed here (U5's own scope, and
untested — this is a read of the code, not a reproduced crash, since
this lane's stub never reaches `prp-ingreek`).

## Validation run

**Targeted, per the brief** (`tools/selfcheck.py`'s functions called
directly, not the whole `make check-harness` suite):

    check_manifests()                          -- includes bench/utf8's
                                                   three generators' --check
    check_expectations()                       -- includes the STUB
    check_floor_pattern()                      -- a real quick cell on
                                                   utf8's floor pattern
    check_capability_policy()                  -- bench/capability's own
                                                   arm, unaffected
    check_capability_policy_noop_elsewhere()   -- SEE FIX BELOW
    check_encoding_axis()                      -- U2's arm, unaffected

Result before the fix: **78 passed, 1 FAILED**
(`check_capability_policy_noop_elsewhere`: bench/utf8 declares
`requires-*` tags, which the check's own docstring did not anticipate a
SECOND set doing). Fixed: `tools/selfcheck.py`'s hardcoded `name ==
"capability"` exclusion widened to `name in ("capability", "utf8")`,
with a comment explaining why utf8 is legitimately excluded from the
"no-op elsewhere" population rather than the check being wrong. Result
after the fix: **all six targeted checks pass, 83/83** (the same run
re-verified `check_capability_policy_noop_elsewhere` standalone: 5/5,
zero failed).

Also run in full (not targeted — both are cheap and unaffected by
`bench/utf8`'s size):

    make check-schema     -- 5 accepted, 73 sabotages rejected for the
                              intended rule, 0 wrong
    make check-interpret  -- 199 passed, 0 FAILED (six sections)

**`make check-harness` in full (the ~20-minute suite) was NOT run by
this lane** — the brief scoped validation to "the generic bench gates
for bench/utf8 run targeted... then make check-schema and
make check-interpret", which is exactly what ran. The full suite is
OWED to whoever runs the next `make check` (the manager, or the next
lane) — it should pass cleanly given the targeted subset above already
covers every generic gate `bench/utf8`'s existence newly triggers
(`check_manifests`, `check_expectations`, `check_floor_pattern`,
`check_capability_policy_noop_elsewhere`) plus the two arms this lane's
own additions could plausibly interact with
(`check_capability_policy`, `check_encoding_axis`).

## Commits

One commit on this branch (`2189302`): `[B77] U4: bench/utf8 patterns +
sidecar, ENUMERABLE by make check`. Full diff: `bench/utf8/patterns.rxt`
+ `gen_patterns.py` + `patterns/*.rx` (76 files) + `subbench.toml` +
`provenance.tsv` + `expectations.tsv` + `gen_expectations.py` (new);
`bench/utf8/CLAUDE.md` + `bench/CLAUDE.md` (rewritten sections);
`bench/utf8/gen_subjects.py` + `manifest.tsv` + `subject_facts.tsv`
(the `asr-b-midchar` rename + the alt-cyr-64 confirmation, regenerated);
`tools/selfcheck.py` (the one-line `check_capability_policy_noop_
elsewhere` exclusion widening, with its own explanatory comment).

## Outstanding / owed

- **U5**: the real `expectations.tsv` (76 patterns), `NOTES.md` (the
  objective, outlier rule R0-R8, growth plan, predictions TSV
  transcription per `utf8_set_v1.md` §11's F-M2 ruling — a dry run
  BEFORE the first window). See the cost estimate above for budgeting
  the derivation itself.
- **Manager/next window**: a full `make check-harness` run confirming
  the targeted subset generalizes (expected clean; not run by this
  lane per its scope).
- **A candidate finding for `bench/capability`'s own owner**: its
  `patterns.rxt` roster declares `tre-default` satisfies
  `true-end-anchor`, which `testees/tre/CLAUDE.md`'s own measured
  finding (no `\z`/`\A`/`\Z` at all) contradicts. Not fixed here (out
  of this lane's mandate — touching `bench/capability` was never part
  of the U4 brief).
- **This lane's branch is `worktree-agent-a9d8cc9be7828fcca`**, not a
  dedicated `lane/b77u4` branch (the worktree's auto-provisioned name).
  The manager should be aware of this when merging — the commit itself
  is correctly scoped and self-contained (verified: `git diff --stat
  master` touches only the 88 files listed above — patterns/*.rx,
  patterns.rxt, gen_patterns.py, subbench.toml, provenance.tsv,
  expectations.tsv, gen_expectations.py, the two CLAUDE.mds,
  gen_subjects.py + its two derived tables, and tools/selfcheck.py),
  but the branch name does not match the lane id.
