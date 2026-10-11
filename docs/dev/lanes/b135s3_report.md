# lane b135s3 report -- RE-PIN to b8337c33 (abi 74, [START-LANDING]), state 3 of [B135]

**Task**: plan row [B135] step (d), inbox I-145 (and I-142/I-143 for the history). Re-pin pcrec
7388f1c0 (abi 73) -> **b8337c33** (abi 74), keep a15fb77b and 7388f1c0 runnable as `also_pins`
(7388f1c0 = state 3's BEFORE and the cross-window control), and deliver the state-3 window plan.
Writer lane; no `store/` write, no `reports/` write beyond the 76 sidecars' catalogue-version
line, NO timed run (every number below is a compile, an emit or a registry read).

**Branch**: `lane/b135s3` in `worktrees/b135s3`, not merged, not pushed. Build (main tree's
shared `build/`): `build/pcrec-b8337c33/`. Scratch (deletable): `/var/tmp/b135s3/`.

## 0. An operational finding first: ~/pcrec did not contain the pin

`~/pcrec` (the pcrec manager's own checkout) is a detached HEAD at c4c70f2c6 and its last fetch is
10:57 EDT; `b8337c33` is not in its object store (`git cat-file -t b8337c33` fails), so
`pin.sh b8337c33` could not run as written. Writing there (a fetch) is forbidden (BD2). Resolution
inside the mandate: a throwaway clone, `git clone --bare https://github.com/fdicostanzo/pcrec.git`
then a no-checkout local clone, at `/var/tmp/b135s3/pcrec`, and `PCREC_SRC=/var/tmp/b135s3/pcrec
sh testees/pcrec/pin.sh b8337c33` (`pin.sh`'s own override; `adapter.py` reads `PCREC_SRC` too).
The resulting build lives at the normal path, `build/pcrec-b8337c33/build/pcrec`, so every later
run needs no override. The clone's `main` is at 432e00de; `7388f1c0..b8337c33` is 71 commits.
Anyone re-running `pin.sh` for a pin newer than ~/pcrec's last fetch needs the same override
(or the pcrec manager to fetch).

## 1. The abi 73 -> 74 step: pcrec's claim vs what I measured

pcrec (I-145; `docs/dev/history/abi_changelog.md` entry 74; main-line merge b8337c33 = lane
sltri containing lane slbuild, SL1-SL4): the RECOVER slot gains `end-minus-width` (every match is
one byte width W: start = verified end - W) and `landing` (start = where the forward scan's
candidate skip last landed, stepped past an ill-formed character under utf8) between `pinned` and
`reverse-pass`, first match wins; both carry NO reverse machine; deny bits 53/54, masked out of
`rx_info.flags`; where both rows apply only the PRODUCT of the denials reaches the reverse pass;
no struct offset moves, no answer moves.

| claim | MEASURED |
|---|---|
| two new `RX_DFA_START` values, `reverse-pass` to order 4, `attempt-start` unchanged | **Confirmed**: `abc` -> `end-minus-width` (emit 21,515 -> 18,717 B), `\d+` -> `landing` (24,261 -> 20,784 B); `--list-axes` `search-start` rows 1 pinned / 2 end-minus-width / 3 landing / 4 reverse-pass + the predicate row `attempt-start` (its own order 3), all `list` rows carrying their `-fno-` flag and bit |
| no reverse machine in those artifacts | **Confirmed** textually: the word `reverse` occurs 0 times in the emitted `.c` of `abc` / `\d+` (13 / 19 times under the product denial, and 13 in 7388f1c0's `abc`) |
| `struct rx_info` unchanged | **Confirmed**: the emitted struct (comments stripped, whitespace normalised) is byte-identical at 7388f1c0 and b8337c33 (md5 `11f44615bcfa6af1e48dd5b633c4f1c1`, 580 chars). **Shim floor STAYS 16**; the abi-sabotage arms (`abi == floor-1`, the abi-5 one) pass in `check_abi_floor_refusal`. No `shim.c`/`driver.c`/`timed.*` byte changed (`git diff master` empty) |
| bits 53/54 masked out of `rx_info.flags` | **Confirmed**: `.flags = 0ULL` on the default, the product-denied and the all-three-denied arm of `abc`, `\d+` and `a*` |
| only the PRODUCT reaches the reverse pass | **Confirmed**, three ways: `x` (both rows apply): default `end-minus-width`, `-fno-start-width` -> `landing` (+9 B), `-fno-start-landing` -> unchanged, both -> `reverse-pass` (== 7388f1c0 byte for byte); `\d` under `-e utf8` the same; census 46 end-minus-width rows land on a THIRD program under `-fno-start-width` alone |
| "from a `pinned` artifact with W = 0 all three denies are needed" | **Confirmed**: `a*` / `[a-z]*` stay `pinned` under the product (identical program to 7388f1c0 and to the default) and reach `reverse-pass` only with `-fno-start-pinned` added (22,159 B vs 18,701); census 30 of 30 pinned rows differ under the triple, 0 under the product |
| 298 of 734 compiles move, 210 `end-minus-width` / 88 `landing` | **Reproduced exactly** (section 5) |
| FIT movers: `(\p{Xwd})` and `\p{L}+` under utf8 no longer take their size rungs | **Confirmed by value** (section 5): both leave `size-cap-retry` for `selected` and GROW (41,213 -> 365,315 B hybrid; 471,796 -> 894,613 B) |
| answer-identical (checked against the reverse pass at every startpos and vs libpcre2 10.46) | **Not re-verified here** (compile-only lane, no timed or answer run). The window's own expectation check (every record's answers against the oracle's, wrong answers excluded from the scoreboard) is where this bench sees it; `make check`'s driver smokes ran |

## 2. Code changes

- **Pin**: `configs.toml` `pin = "b8337c33"`, `also_pins = ["a15fb77b", "7388f1c0"]`. No new
  pinned testee (the window's before/after IS the two pins; the denials are `DENY_FLAGS` entries
  reachable today as `PCREC_LOCAL_FLAGS="-fno-start-width ..."` at the scratch tier). Pinned-testee
  count unchanged.
- **adapter.py**: `dfa_start` declared values `pinned, end-minus-width, landing, reverse-pass,
  attempt-start` (the closed set, ONCE) with the source/description prose updated;
  `DENY_FLAGS += ("-fno-start-width", "nostartwidth", ...), ("-fno-start-landing",
  "nostartlanding", ...)` appended LAST. The registry cross-check of declared stamp values
  against `search-start` passes with no other change.
- **shim.c / driver.c / timed.***: UNTOUCHED (the stamp is a string macro the shim already reads
  generically; no new rx_info member).
- **tools/selfcheck.py**: the "dfa_start is not a constant" hard gate (ALL FIVE values on real
  artifacts; it printed `only [...all five...] seen` against the old three-value test until
  widened); STAMP_CASES `VM hybrid, non-nullable language KEPT` and ledger `bounded dig-upto-16`
  (now `landing`; label renamed) ; `B135S3_RESID` + `_b135s3_moved` (three ledger rows, MEASURED:
  -3,805 / -17,037 / -11,705 B emit) applied in the one place the ledger layers are applied;
  `B135_START_DENIES` added to `B124_LATER_DENIES` and to the NEW-pin side of the b124 and b126
  identity arms (the artifacts those compare against c4c70f2c / 60366d747 lost their reverse
  machine); `check_b135_stamps`' abi-73 arm now names 7388f1c0 BY NAME and `check_b135_two_pin_window`
  asserts 7388f1c0 / b8337c33 (canonical) ids; **`check_b135s3_stamps`** (15 checks: 14
  `B135S3_CASES` rows x {73, default, w, l, wl, wlp} by value incl. sizes, `dfa_uniform_folds` and
  `scan_edges` covariates, `.text(wl) == 7388f1c0`, plus the `search-start` registry rows and bits)
  and two **`DENY_CONTROLS`** rows (`-fno-start-width` on `x`, `-fno-start-landing` on `\d+`, each
  registry-read, `reg_arm default`).
- **pcrecbench/report.py**: `START_VALUE_LEGEND` -- one legend line each for `end-minus-width`,
  `landing`, `attempt-start`, printed ONLY when a row in the report carries the value (none does
  in any committed report, so NO committed report changes by a byte and the reporter version is
  NOT bumped; flagged for the manager: bump it with the first report that carries a new value);
  the module prose and `_dfa_start_display` docstring state the five-value set;
  `test_dfa_start_closed_set_b135` (both directions). **tools/trend*.py**: nothing -- `dfa_start`
  is a free-valued META/STAMP key there, values pass through.
- **Registries re-archived** (headers chained, bodies verbatim): `list_axes.tsv` MAIN 161/49 ->
  **163/49**; `#section memfn` 0 -> 3 rows (`vrun-w32/w16/kb`, [MEMFN] R-13's `--memfn=no-...`
  SIMD denies -- read by nothing here; every reader selects the MAIN table, exercised by the
  existing `check_list_axes_registry`); `list_definitions.tsv` (75) / `list_limits.tsv` (73) /
  `list_schema.tsv` (79) byte-identical.
- **Catalogue 3.18** (`[[pin_order]]` + `b8337c33`, rules.toml note, catalogue/CLAUDE.md) + the 76
  sidecars' `catalogue:` line (sed `3.17 -> 3.18`; see "merge note" below).
- **Docs**: root `CLAUDE.md` (status sentence + the testees pin paragraph),
  `testees/pcrec/CLAUDE.md` ("Re-pin at b8337c33"), `docs/dev/pcrec_references.md`,
  `docs/dev/measurements/CLAUDE.md`.

## 3. The new values BY VALUE (`check_b135s3_stamps`, 15/15)

default -> `-fno-start-width` / `-fno-start-landing` / both / both + `-fno-start-pinned`
(`dfa_start`; the sizes are in `B135S3_CASES`):

| witness | 7388f1c0 | b8337c33 default | w | l | wl | wlp |
|---|---|---|---|---|---|---|
| `x` (both rows) | reverse-pass | **end-minus-width** | landing | end-minus-width | reverse-pass | reverse-pass |
| `abc`, `[0-9]{4}`, `foo\|bar`, `(?i)abc` | reverse-pass | **end-minus-width** | reverse-pass | end-minus-width | reverse-pass | reverse-pass |
| `\d+`, `[^\n]+` | reverse-pass | **landing** | landing | reverse-pass | reverse-pass | reverse-pass |
| `\d` `-e utf8` (both rows) | reverse-pass | **end-minus-width** | landing | end-minus-width | reverse-pass | reverse-pass |
| `a*` (pinned, W = 0) | pinned | pinned | pinned | pinned | pinned | **reverse-pass** |
| `(?:a\|b)*c` (neither) | reverse-pass | reverse-pass | = | = | = | = |
| `^abc` | attempt-start | attempt-start | = | = | = | = |
| `abc$` (rev-end) | reverse-pass | reverse-pass | = | = | = | = |
| `abc` `--engine=vm` | -- | -- | -- | -- | -- | -- |

`wl` reproduces 7388f1c0's emit/code bytes EXACTLY on every row and its compiled `.text`; the
covariates move with the machine (`\d+`: `scan_edges` 2 -> 1; `[0-9]{4}`: `dfa_uniform_folds`
2 -> 1 and `scan_edges` 2 -> 1; `wl` restores both) -- a cross-pin bucket on `edges=`/`folds=`
moves these rows by definition, not by behaviour.

## 4. Registry deltas

| surface | 7388f1c0 | b8337c33 | delta |
|---|---|---|---|
| `--list-axes` MAIN | 161 rows / 49 axes | **163 / 49** | `search-start` +2 rows (end-minus-width, landing: stamp macro `RX_DFA_START`, deny bits 53/54, `-fno-start-width`/`-fno-start-landing`), `reverse-pass` order 2 -> 4 |
| `--list-axes` `#section memfn` | 0 | 3 | R-13's SIMD denies; unread here |
| `--list-limits` / `--list-definitions` / `--list-schema` | 73 / 75 / 79 | 73 / 75 / 79 | byte-identical |

Reader audit (I-145's five): selfcheck gate + fixtures, `list_axes.tsv`, `adapter.py` enum + prose,
`report.py` legend, trend META -- all five handled or shown to need nothing (section 2). A grep of
`reverse-pass` over `*.py/*.js/*.html/*.sh/*.toml` finds no other closed-set reader.

## 5. Census vs 7388f1c0 (docs/dev/measurements/2026-10-10-b135s3-census.txt)

Compile-only, `probe_b135s3_census.py`: 1,468 rows = 367 patterns of 9 sets x {plain, whole} x
{auto-caps, auto-nocaps}, each emitted at both builds (v2 program identity) and, at the new pin,
under four denials.

**The population I-145 means** (found by trying them): the PLAIN form x {caps, nocaps} = 367 x 2 =
**734 rows** (47 of them refused at both pins). The whole-subject form is the other 734 rows.

| form | rows | identical | changed | refused-both | refusal movers |
|---|---|---|---|---|---|
| plain (734) | 734 | 389 | **298** | 47 | 0 |
| whole-subject (734) | 734 | 688 | 0 | 46 | 0 |

The 298 = **210 `reverse-pass > end-minus-width` + 88 `reverse-pass > landing`**, caps and nocaps
alike (105 + 105, 44 + 44); EVERY changed row moves `dfa_start`, no unmoved row changes; **I-145's
numbers reproduce to the unit**. By set (caps + nocaps pooled): altwide 2, bounded 34 (14 e-m-w + 20
landing), capability 16, email-specimen 2, litrun 24, loglines 6, sentinel 2, syntax 98 (84 + 14),
utf8 114 (60 + 54). The 74 `attempt-start` rows and 30 `pinned` rows are unchanged from 7388f1c0.

**Every difference named**: 298 `dfa_start` moves; the four FIT rows below (also `dfa_match
search-filter > unwrapped`); nothing else -- `engine`, `dfa_scan`, `dfa_prefilter`, `req_why` move
on NO plain row. The whole form moves nothing at all: **[START-LANDING] does not touch the match
regime** (those artifacts are the `(?:...)\z` rev-end form), so a state-3 `match`-regime cell has
no mechanism to move.

**Denials at the pin vs 7388f1c0's v2 identity** (movers): `-fno-start-width` -> 164/210
end-minus-width rows `to-S73`, 46 a third program (the landing fallback), 88/88 landing rows
`same` (inert); `-fno-start-landing` -> 88/88 landing rows `to-S73`, 210/210 end-minus-width rows
inert; **both -> 298/298 `to-S73`**; both + `-fno-start-pinned` -> 298/298 `to-S73`. On the 389
unmoved compiled rows the product is inert (389/389 `same`), and the triple differs on exactly the
30 `pinned` rows (30 of 30).

**FIT movers** (a mover that drops the reverse machine fits a size rung it did not): `utf8
prp-l` and `utf8 prp-notl`, caps and nocaps (4 rows): `ENGINE_SEL size-cap-retry > selected`,
emitted 475,770 -> 899,193 B and 494,222 -> 878,735 B (they GROW; the cap that shed the machine no
longer fires), `-fno-start-landing` restores the retry on all four. I-145's own witnesses are not
bench patterns and are asserted by direct emit: `(\p{Xwd})` `-e utf8` 41,213 B VM (retry) -> a
selected hybrid, `landing`, 365,315 B (`emit_code_bytes` 23,894 -> 26,109); `\p{L}+` `-e utf8`
471,796 -> 894,613 B. A speed read of any set-grain mean over `utf8` mixes START-LANDING with the
restored prefilter/machine on those rows.

## 6. Size books (measured per witness; never a flat term)

The emitted-text bytes shrink on every non-FIT mover: `end-minus-width` n = 210, median -2,765 B
(min -20,939, max -2,546), median ratio 0.893; `landing` n = 84 non-FIT, median -3,667 B, median
ratio 0.871 (the four FIT rows grow, max +423,423). The ledger rows moved: `bounded dig-upto-16`
21,386 B (was 25,191: -3,805), `wild-secrets-github-pat` -17,037, `wild-validator-uuid-grok`
-11,705 (`B135S3_RESID`); every other asserted row was UNMOVED (the first run found 22 reds, 17 of
them identity-arm bookkeeping, 5 by-value rows; none was a flat term).

## 7. Validation

- Targeted groups, by the re-run list of b135prep: `check_mechanism_stamps`, `check_program_sha256`,
  `check_deny_flag_controls`, `check_b122/b124/b126/b135_stamps`, `check_b135s3_stamps`,
  `check_b135_two_pin_window`, the three registry checks, `check_emit_size_port`,
  `check_abi_floor_refusal`: first pass 244 pass / 22 red (all attributed in section 2); after the
  fixes every group green (`deny controls` 44/0 incl. the two new rows, `b135s3` 15/0, `b124`
  green, `mechanism_stamps` / `b122` / `b126` / `b135` / registries green in run2).
- `pcrecbench/tests/test_report.py`: 103 passed, 0 failed.
- **FINAL `make -k check` (log /var/tmp/b135s3/final_check.log, rc=2): check-schema 6/74/0; check-harness 770 passed, 4 FAILED = exactly the four known environmental reds; check-interpret 174 passed / 76 FAILED at that run, because the sidecars had been sed-edited (3.17 -> 3.18) and a sidecar re-render is not that edit. FIXED: `git merge master` (no conflicts), then `scripts/regen_sidecars.py` over all 80 sidecars (0 failures), then check-interpret 254 passed / 0 FAILED, check-report OK, check-trend ALL PASS (cite check 0 problems).** (Original text:) full run -- launched detached by this lane (the lane had further work to
  do), log `/var/tmp/b135s3/final_check.log`, last line `DONE rc=<n>`; the numbers are in section 9
  if filled, else the manager reads the log. Expected: the four known pruned-build reds
  (`capability: gen_patterns.py --check` cd371441, `KB-35 build_census` and `KB-35 program_identity
  --check` 25b1984f, `b108 acceptance mover` 751b9c6d) and nothing else.

## 8. Findings pcrec did not state (candidate outbox items)

1. **~/pcrec lagged the pin** (section 0): the pcrec manager's checkout is a detached HEAD at an
   older commit, last fetched before the pin was named. Not a pcrec bug; an operating note.
2. **START-LANDING is a SEARCH-regime event only**: the whole-subject form (`(?:...)\z`, rev-end)
   moves in 0 of 734 rows, so the `match`-regime cells of the window cannot carry it.
3. **The window sets carry few movers**: capability 8 patterns, loglines 3, litrun 12, email ONE
   (the floor pattern) -- the O-91 acceptance tail patterns are rev-end and do NOT move at state 3.
   The populations START-LANDING actually reaches are `syntax` (49 patterns), `utf8` (57),
   `bounded` (17) (section 9).
4. **FIT growth**: four bench rows and both I-145 witnesses grow 1.8-8.9x in emitted bytes when the
   machine is dropped and the rung fits (section 5).
5. **Covariates**: `scan_edges`/`dfa_uniform_folds` fall on movers that lose the reverse machine
   (section 3) -- a legend-clause reader sees them as cross-pin movers.
6. `#section memfn` is no longer empty at this pin (3 SIMD-deny rows); the "0 rows" prose in
   earlier sections of testees/pcrec/CLAUDE.md is history.

## 9. WINDOW PLAN, STATE 3 (NOT RUN): docs/dev/lanes/b135s3_chain.sh

**Cells**: the same sets as the states 1+2 window (`/var/tmp/b135win/chain.sh`): `sentinel`,
`capability`, `loglines`, `email`, `litrun`, `sentinel:end` = 26 cells. **Testees**: `pcrec-auto`
and `pcrec-nocaps` at b8337c33 (bare entries) AND at 7388f1c0 (`@7388f1c0`, the cross-window
control; same testee ids as the states 1+2 window's 7388f1c0 records, so the store holds each
control cell twice). ABBA per set: `pcrec-auto@7388f1c0 pcrec-auto pcrec-nocaps
pcrec-nocaps@7388f1c0`. Sentinel first (`pcrec-auto@7388f1c0 pcrec-auto pcrec-nocaps
pcrec-nocaps@7388f1c0 pcre2-jit`) and last (`pcrec-auto pcrec-auto@7388f1c0 pcrec-nocaps@7388f1c0
pcrec-nocaps pcre2-jit`, `run_suite.sh` prepends the first and the script names the closing pass).

**Exact script**: `docs/dev/lanes/b135s3_chain.sh` (committed; syntax-checked with `bash -n`). In
short, from the MAIN tree after merge, detached: preconditions (`pin.sh --path` of both pins,
`bench/sentinel/gen_subjects.py`, `pcrecbench quiet --samples 5`), then

    SUITE="sentinel capability loglines email litrun sentinel:end" \
    TESTEES_sentinel="pcrec-auto@7388f1c0 pcrec-auto pcrec-nocaps pcrec-nocaps@7388f1c0 pcre2-jit" \
    TESTEES_sentinel_end="pcrec-auto pcrec-auto@7388f1c0 pcrec-nocaps@7388f1c0 pcrec-nocaps pcre2-jit" \
    TESTEES_capability="pcrec-auto@7388f1c0 pcrec-auto pcrec-nocaps pcrec-nocaps@7388f1c0" \
    TESTEES_loglines=<same>  TESTEES_email=<same>  TESTEES_litrun=<same> \
    NOTE="[B135] START-LANDING state 3: b8337c33 (abi 74) vs 7388f1c0 (abi 73) repeated as the cross-window control" \
    scripts/run_suite.sh

(do NOT set `PIN` or `PCRECBENCH_PCREC_PIN`). Optional `RUN_AB=1 AB_REV=<master tip>` inserts the
[B133] instrument A/B/A/B; default OFF because `driver.c`/`shim.c`/`timed.*` are byte-identical to
master's, so the A/B would time identical sources and the sentinel pair (first and last) is the
instrument control. Before the first cell: `sha256sum build/work/pcrec-auto/pcrec_driver
build/work/pcrec-nocaps/pcrec_driver` equal and unchanged at the close (one driver for all four
testee entries -- the workdir carries no pin).

**Estimated duration** (the states 1+2 window's MEASURED set minutes, same cells, same four testee
entries): sentinel 35 + capability 194 + loglines 36 + email 26 + litrun 60 + sentinel:end 37 =
**388 min = 6.5 h** (+ ~35 min if `RUN_AB=1`; the previous chain's A/B took 12:13-12:48). Per-cell
cap 5,400 s is above every cell (worst: capability auto, ~52 min). **Completion**: `CHAIN_DONE
suite_rc=0` in `/var/tmp/b135win3/chain.log`; the suite log ends SUITE_RUN_COMPLETE with six `set
<name> rc=0`; expect `WINDOW_RUN_COMPLETE cells=5/5, 4/4, 4/4, 4/4, 4/4, 5/5`.

**What to read** (what the census predicts, nothing is pcrec's own prediction): MOVER cells at
b8337c33 vs the 7388f1c0 control, caps config: capability `wild-validator-uuid-grok`, `hex8-bounded`,
`wild-secrets-aws-access-key-id`, `wild-secrets-github-pat`, `wild-codegrammar-json-array-begin`,
`wild-codegrammar-json-object-begin`, `utf8-lead-no-cont`, `floor-byte`; loglines `uuid`, `hex32-id`,
`floor`; email `floor`; litrun all twelve (`lit-l2 ... lit-l40`, `wild-secrets-aws-access-key-id`,
`wild-secrets-github-pat`, `floor`) -- every one `end-minus-width` (24 DFA-routed capability
patterns have no landing mover). The cross-window CONTROL is every other cell (O-91's tail cells are
rev-end and do not move): the 7388f1c0 pair must reproduce the states 1+2 numbers within the
window-to-window null band; a state-3 cell that moves WITHOUT a stamp move is the window, not the
engine. Verify per record that `dfa_start` reads `end-minus-width` / `reverse-pass` on the
mover/control side before reading any ratio. `match`-regime cells cannot move (section 5).
**Tier 2, appended behind `STOP_AT` only**: the populations START-LANDING really reaches --
`syntax` (49 mover patterns; prep estimate 4 x ~43 min), `utf8` (57; ~4 x 40 min, and its
`prp-l`/`prp-notl` FIT rows make a speed read ambiguous), `bounded` (17; ~4 x 50 min) -- estimates
from the b135prep plan, UNMEASURED. `email` (one mover, the floor) is the cheapest cut if the
window must shrink (-26 min).

**TIER 2 (manager's extension; script revised, same file).** Tier 1 is unchanged (26 cells +
altwide@0.3, ending `sentinel:end`, 424 min). Tier 2 runs the populations START-LANDING actually
reaches, each ABBA with `pcrec-auto`/`pcrec-nocaps` at b8337c33 and `@7388f1c0` (the BEFORE), in
decreasing mover count, then a closing `sentinel:end2` (its own `run_suite.sh` call, so `STOP_AT` can
never skip it):

| set | testees | movers (patterns; caps = nocaps) | est. (min) |
|---|---|---|---|
| `utf8@0.1` | `pcrec-{auto,nocaps}-utf8` x {b8337c33, @7388f1c0} (ids `pcrec_{b8337c33,7388f1c0}_auto-{caps,nocaps}-simdna_utf8`, `@pin` verified through `describe()`) | **57**: 30 end-minus-width + 27 landing (incl. FIT rows `prp-l`, `prp-notl`) | 2 x 38.6 + 2 x 39 = ~156 (+regen) |
| `syntax@0.1` | `pcrec-{auto,nocaps}` x 2 pins | **49**: 42 end-minus-width + 7 landing | 2 x 41 + 2 x 43 = ~170 |
| `bounded@0.3` | same | **17**: 7 end-minus-width + 10 landing | 4 x 48 = ~192 |
| `sentinel:end2` | auto, auto@, nocaps@, nocaps, pcre2-jit | -- | ~37 |

Estimates are the 2026-10-05 c4c70f2c cell lengths from the window logs (utf8 auto 38.6 / nocaps
~39; syntax auto 41.0 / nocaps 43.3; bounded auto 47.8; the sentinel set's measured 37 min) -- the
`-utf8` and `@7388f1c0` arms are assumed to run as long as their byte / canonical siblings, and
UNMEASURED at these pins. **Per-tier**: tier 1 = 424 min (7.1 h); tier 2 = ~555 min (9.3 h);
**total ~979 min = 16.3 h** (two nights; the box is not quiet-gated across the gap, each cell is
pre-flighted). Movers by set in the census count the PLAIN form only (the `search` regime); the
`match` regime moves 0 rows everywhere. Census movers for `utf8` were taken under `-e utf8`; for
`syntax` and `bounded` in byte mode, as their testees run. Read: a mover cell's `dfa_start` must
read `end-minus-width`/`landing` on the b8337c33 record and `reverse-pass` on the @7388f1c0 one
before any ratio is read; `utf8 prp-l`/`prp-notl` also change engine_sel and grow (FIT).

**Where STOP_AT sits.** Never on tier 1 (`STOP_AT` skips every set that would START after it,
`sentinel:end` included). For tier 2 set `STOP_AT_T2="$(date -d '<deadline minus 3h10m>')"` in the
environment: it applies to the tier-2 suite call only, skips whole sets that would start after it
(order utf8, syntax, bounded: bounded, the fewest movers, is the first lost), and the closing
`sentinel:end2` still runs because it is a separate call. A run that is cut mid-set is bounded by
`CELL_CAP` (5,400 s) per cell, not by STOP_AT.

**ADDITION (manager, for pcrecdev1's [ENG-TACTICS] recount): `altwide` at b8337c33.** The set is
`altwide@0.3` now (the brief said 0.2). `pcrecbench run` has NO per-pattern filter (only `quick` does,
and it is scratch-tier), so the WHOLE set runs; `sfx-64/256/512` are inside it. Added to the chain
after `loglines` (so pcrecdev1's data lands early) as `TESTEES_altwide="pcrec-auto pcrec-nocaps"` at
b8337c33 only. Duration: the last altwide window (c4c70f2c, 2026-10-05) measured `pcrec-auto` at
17.7 min a cell (06:36-06:54) and `pcrec-vm` 18.7 min; nocaps assumed ~18 -> **+36 min**, new total
**424 min = 7.1 h** (still one night). **Control arm: NO by default.** pcrecdev1's read is same-pin
(b8337c33 medians), so the 7388f1c0 arm adds nothing to it, and altwide moves only 2 patterns at
START-LANDING (`altwide` 2 rows in the census) while 7388f1c0 shows six whole-form refusal movers vs
a15fb77b that are irrelevant to a same-pin read. If the manager wants the control anyway (a
window-drift check on a set that does not move), add `pcrec-auto@7388f1c0 pcrec-nocaps@7388f1c0`
(+36 min). **STOP_AT**: altwide sits before the closing `sentinel:end`, and `STOP_AT` skips every
set that would START after it, the closing sentinel included, so do NOT set STOP_AT for the tier-1
chain; use it only on the tier-2 sets appended after `sentinel:end`.

## 10. Charter-vs-committed checklist

| brief item | status |
|---|---|
| read BOILERPLATE; worktree `lane/b135s3`; WIP commits; no push/merge | done (`git log lane/b135s3`) |
| no `store/` write, no timed run | none; compile/emit only; the sidecars' `catalogue:` line is the one `reports/` touch |
| pin.sh b8337c33 | done via `PCREC_SRC=/var/tmp/b135s3/pcrec` (section 0); `build/pcrec-b8337c33` |
| canonical pin b8337c33; a15fb77b + 7388f1c0 `also_pins` | `configs.toml`; `check_b135_two_pin_window` |
| read abi 73->74 and 7388f1c0..b8337c33; claim vs measured | sections 0, 1 (71 commits; changelog entry 74) |
| `dfa_start` widened ONCE to the five values at every reader I-145 lists | selfcheck gate + fixtures, list_axes.tsv, adapter.py enum + prose, report.py legend, trend META (needs none) -- section 2 |
| `end-minus-width` and `landing` BY VALUE on witnesses | `check_b135s3_stamps` 15/15, section 3 |
| `-fno-start-width` / `-fno-start-landing` as DENY_FLAGS + DENY_CONTROLS; product-only; each denial reproduces 7388f1c0 where it should | adapter.py, DENY_CONTROLS rows, `check_b135s3_stamps`, census (298/298 `to-S73` under the product) |
| reproduce 298 of 734 (210 / 88); say which population; name every difference; FIT movers | section 5 (plain form x caps/nocaps; 0 whole-form movers; 4 FIT bench rows + 2 witnesses) |
| struct rx_info / shim floor, abi-sabotage arms | unchanged, floor 16; `check_abi_floor_refusal` green |
| registries re-archived | four `testees/pcrec/list_*.tsv` |
| size books per witness | section 6; `B135S3_RESID`, `B135S3_CASES` |
| compile-only census vs 7388f1c0 | section 5 + the archive |
| catalogue `[[pin_order]]` + sidecar version lines | 3.18; 76 sidecars |
| `make check` (4 known reds expected), check-interpret, check-report | DONE, see section 7 (harness 770/4 known, interpret 254/0 after regen, report OK, trend PASS); was: launched detached, `/var/tmp/b135s3/final_check.log`, marker `DONE rc=`; targeted groups and `test_report.py` (103/0) are green |
| CLAUDE.md lines in the existing style | root, testees/pcrec, catalogue, measurements, pcrec_references |
| STATE-3 WINDOW PLAN (not run): same cells/sets, 4 testee entries ABBA, sentinel first and last, exact chain script, duration | section 9 + `docs/dev/lanes/b135s3_chain.sh` |
| report with this checklist | this file |
| OWED | (1) -- (done, section 7); (2) the window itself (manager); (3) reporter version bump with the first report carrying a new `start=` value; (4) plan.md/journal STATE edits (manager); (5) -- (done: master merged, all 80 sidecars regenerated, not sed-edited) |
