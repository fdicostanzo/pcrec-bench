# Lane `b111roster` — the capability roster gap as a make-check gate

Branch `lane/b111roster`, worktree `worktrees/b111roster` off `master` at
`4f42420`. Mandate: `pcrec-bench` and `~/pcrec` only, `~/pcrec` read-only
(untouched here); no `store/`/`reports/` writes, per the brief.

## Findings first

`bench/capability`'s `ext bench` roster (`EXT_BENCH_ROSTER` in
`bench/capability/gen_patterns.py`) was hand-listed per testee id with no
gate checking it against the real testee population. Every testee id
absent from it satisfies NOTHING under `pcrecbench/capability.py`'s
fail-closed rule (5.2), so a pinned testee missing from the roster reads
`unsupported-by-declaration` on all 27 of the set's 64 `requires-*`-tagged
patterns — a `did-not-compile`-shaped outcome with no real compile
attempt behind it. This has already happened twice in three days:
`pcrec-auto-nolitrun` (fixed in `fef55af`, outbox O-64 → O-65) and, the
very next day, the two `[B110]` `align64loops` testees (outbox O-67 item
4).

**The audit (below) found the gap was total for every pinned testee added
since the roster's last touch, not just the two [B110] rows the brief
named**: of 48 pinned testee ids across all seven `testees/*/configs.toml`
files, only 16 were on `EXT_BENCH_ROSTER` before this lane. The other 32
split into two clean categories, neither of which needed a fresh
witness-compile census to settle:

1. **Twenty pcrec testees whose ONLY difference from an already-declared
   config (`pcrec-auto` / `pcrec-nocaps` / `pcrec-vm` /
   `pcrec-auto-nolitrun`) is an axis that never reaches the PARSER** — a
   compiler choice (`cc`), a caller-provided frame buffer (`-in`), an
   emitted-size cap raise (`-bigcap`), a compilee-only alignment flag
   (`cflags`), or an emit-/selection-side deny flag
   (`-fno-scan-edge`/`-fno-alt-island`/`-fno-cls-fold`/`-fno-lit-run`/
   `-fno-altcls-factor`/`-fno-req-run`, every one of which rides beside
   `-fno-req-byte`, already on the roster with the identical reasoning in
   its own comment: "an EMIT-side denial ... so it satisfies exactly
   pcrec-auto's tokens"). Each `configs.toml` comment for these axes
   independently states the same fact ("OUR OWN phase-2 command line",
   "never passed to pcrec", "an EMIT-side denial"), and the PARSE-time
   refusals the four withheld REQUIRES tokens name
   (`callouts`/`conditionals`/`control-verbs`/`lookbehind-variable`) are
   already proven invariant across `--engine=`/`--no-captures` by the
   pre-existing `pcrec-auto`/`pcrec-nocaps`/`pcrec-vm` rows sharing one
   exclusion set. These twenty rows are ADDED to `EXT_BENCH_ROSTER`,
   citing this reasoning once rather than twenty times.
2. **Twelve testees genuinely EXCLUDED, each for a reason already
   established elsewhere in the codebase or structurally true of the
   testee**: `pcrec-local` (no fixed pin, scratch tier by construction,
   never enters `store/` or a ranking — record_schema.md §6.8) and all
   eleven `-utf8` engine-encoding siblings (`pcrec-{auto,nocaps,vm,vm-in}
   -utf8`, `pcre2-utf-{interp,jit,dfa}`, `onig-utf8`, `re2-utf8`,
   `vectorscan-block-{nosom,som}-utf8`). The UTF-8 exclusion is not a new
   ruling — `testees/vectorscan/CLAUDE.md`'s own `vectorscan-block-som
   -utf8` row already states "no `EXT_BENCH_ROSTER` row, same convention
   as every other `-utf8` config"; this lane makes that convention
   MACHINE-CHECKED rather than merely documented, and gives it one
   citable reason (`bench/capability` declares no `[expectations]
   encoding = "utf8"` and tags no pattern with any of the three
   UTF-8-scoped REQUIRES tokens — it is chartered byte-mode-only,
   `bench/utf8` is where `-utf8` configs are declared and run).

36 roster rows + 12 excluded = 48, exactly `pcrecbench.adapters.
all_testees()`'s count — checked programmatically, not just by hand
count (see "Verification" below).

## The audit table

Every pinned testee id in every `testees/*/configs.toml`, its
disposition, and why. (`roster` rows also carry their declared REQUIRES
token count; the four withheld tokens on every pcrec row are
`callouts`/`conditionals`/`control-verbs`/`lookbehind-variable`, minus
`captures` on the three `nocaps*` configs — unchanged from the
pre-existing `pcrec-auto`/`pcrec-nocaps`/`pcrec-vm` rows.)

### onig (`testees/onig/configs.toml`)

| testee id | disposition | reason |
|---|---|---|
| `onig-default` | roster (pre-existing) | 13/17 tokens; witness census `docs/dev/measurements/2026-09-17-onig-capability-witness-census-6.9.10.txt` |
| `onig-utf8` | EXCLUDED (new) | `-utf8` engine-encoding sibling; see above |

### pcre2 (`testees/pcre2/configs.toml`)

| testee id | disposition | reason |
|---|---|---|
| `pcre2-interp` | roster (pre-existing) | 17/17 tokens |
| `pcre2-jit` | roster (pre-existing) | 17/17 tokens |
| `pcre2-dfa` | roster (pre-existing) | 12/17 tokens (man `pcre2matching`'s eight-item restriction list) |
| `pcre2-utf-interp` | EXCLUDED (new) | `-utf8` engine-encoding sibling |
| `pcre2-utf-jit` | EXCLUDED (new) | `-utf8` engine-encoding sibling |
| `pcre2-utf-dfa` | EXCLUDED (new) | `-utf8` engine-encoding sibling |

### pcrec (`testees/pcrec/configs.toml`) — 31 testees

| testee id | disposition | reason |
|---|---|---|
| `pcrec-auto` | roster (pre-existing) | 13/17 tokens (base) |
| `pcrec-nocaps` | roster (pre-existing) | 12/17 tokens (base, minus `captures`) |
| `pcrec-vm` | roster (pre-existing) | 13/17 tokens (base) |
| `pcrec-auto-clang` | roster (new) | `cc` axis only — same tokens as `pcrec-auto` |
| `pcrec-nocaps-clang` | roster (new) | `cc` axis only — same tokens as `pcrec-nocaps` |
| `pcrec-vm-clang` | roster (new) | `cc` axis only — same tokens as `pcrec-vm` |
| `pcrec-auto-in` | roster (new) | frame-buffer axis only — same tokens as `pcrec-auto` |
| `pcrec-vm-in` | roster (pre-existing) | frame-buffer axis, already rostered at `pcrec-vm`'s tokens |
| `pcrec-local` | EXCLUDED (new) | no fixed pin; scratch tier by construction, never ranked |
| `pcrec-auto-bigcap` | roster (new) | emitted-size cap raise only — same tokens as `pcrec-auto` |
| `pcrec-vm-bigcap` | roster (new) | emitted-size cap raise only — same tokens as `pcrec-vm` |
| `pcrec-auto-noedge` | roster (new) | `-fno-scan-edge` (DFA machine codegen) — same tokens as `pcrec-auto` |
| `pcrec-auto-align64` | roster (new) | `cflags` (compilee alignment) only — same tokens as `pcrec-auto` |
| `pcrec-auto-align64loops` | roster (new) | `cflags` only — same tokens as `pcrec-auto` (the brief's own trigger) |
| `pcrec-auto-nolitrun-align64loops` | roster (new) | `cflags` on top of `pcrec-auto-nolitrun` — same tokens (the brief's own trigger) |
| `pcrec-auto-noisland` | roster (new) | `-fno-alt-island` (VM lowering) — same tokens as `pcrec-auto` |
| `pcrec-auto-noclsfold` | roster (new) | `-fno-cls-fold` (VM lowering) — same tokens as `pcrec-auto` |
| `pcrec-vm-noclsfold` | roster (new) | `-fno-cls-fold` — same tokens as `pcrec-vm` |
| `pcrec-auto-noreqbyte` | roster (pre-existing) | `-fno-req-byte`, measured 4/64 refused-both, 0 movers |
| `pcrec-auto-nolitrun` | roster (pre-existing) | `-fno-lit-run` — same tokens as `pcrec-auto` |
| `pcrec-vm-nolitrun` | roster (new) | `-fno-lit-run` — same tokens as `pcrec-vm` |
| `pcrec-auto-noaltclsfactor` | roster (new) | `-fno-altcls-factor` — same tokens as `pcrec-auto` |
| `pcrec-vm-noaltclsfactor` | roster (new) | `-fno-altcls-factor` — same tokens as `pcrec-vm` |
| `pcrec-auto-noaltclsfactor-nolitrun` | roster (new) | both denials — same tokens as `pcrec-auto` |
| `pcrec-vm-noaltclsfactor-nolitrun` | roster (new) | both denials — same tokens as `pcrec-vm` |
| `pcrec-vm-noreqbyte-noreqrun` | roster (new) | both pre-check denials — same tokens as `pcrec-vm` |
| `pcrec-vm-noreqbyte-noreqrun-nolitrun` | roster (new) | three denials — same tokens as `pcrec-vm` |
| `pcrec-auto-utf8` | EXCLUDED (new) | `-utf8` engine-encoding sibling |
| `pcrec-nocaps-utf8` | EXCLUDED (new) | `-utf8` engine-encoding sibling |
| `pcrec-vm-utf8` | EXCLUDED (new) | `-utf8` engine-encoding sibling |
| `pcrec-vm-in-utf8` | EXCLUDED (new) | `-utf8` engine-encoding sibling |

### re2, rust, tre (`testees/re2,rust,tre/configs.toml`)

| testee id | disposition | reason |
|---|---|---|
| `re2-default` | roster (pre-existing) | 6/17 tokens |
| `re2-longest` | roster (pre-existing) | 6/17 tokens (RE2's own census: identical to `re2-default`) |
| `re2-utf8` | EXCLUDED (new) | `-utf8` engine-encoding sibling |
| `rust-default` | roster (pre-existing) | 7/17 tokens |
| `tre-default` | roster (pre-existing) | 5/17 tokens |

### vectorscan (`testees/vectorscan/configs.toml`)

| testee id | disposition | reason |
|---|---|---|
| `vectorscan-block-nosom` | roster (pre-existing) | 5/17 tokens, boolean grain |
| `vectorscan-block-som` | roster (pre-existing) | 6/17 tokens (`nosom` + `span-reporting`) |
| `vectorscan-block-nosom-utf8` | EXCLUDED (new) | `-utf8` engine-encoding sibling |
| `vectorscan-block-som-utf8` | EXCLUDED (new) | `-utf8` engine-encoding sibling |

**Total: 48 testee ids, 36 on the roster (16 pre-existing + 20 new), 12
excluded (0 pre-existing + 12 new, though the `-utf8` convention was
already documented prose before this lane). Zero unaccounted for.**

## The gate

`tools/selfcheck.py:check_capability_roster_coverage` (wired into `make
check-harness`, called from `main()` after
`check_capability_policy_noop_elsewhere`):

1. `_capability_roster_gap(testee_ids, roster_ids, excluded_ids)` — the
   one predicate both the real check and its negative control call, so
   they cannot silently define "covered" two different ways.
2. Loads `bench/capability/gen_patterns.py` as a module (the same
   `spec_from_file_location` shape `_pcrec_adapter_module` already uses)
   and enumerates every real testee id via `pcrecbench.adapters.
   all_testees()` — the SAME discovery `python3 -m pcrecbench testees`
   and the harness itself use, never a second hand-typed list.
3. Asserts no id is both rostered and excluded, every `EXCLUDED_TESTEES`
   reason is non-blank, every real testee id is in one of the two sets
   (fails BY NAME on any gap), and — the negative control — that the
   SAME predicate reports a synthetic `z-selfcheck-unlisted-testee` id
   when it is added to the population.

Standalone run (before the full suite): **4/4 checks pass**, including
the negative control:

```
-- [B111] every pinned testee is on the capability roster, or excluded by name --
   PASS  no testee id is both rostered and excluded           36 roster, 12 excluded
   PASS  every EXCLUDED_TESTEES entry carries a non-empty reason 12 entries
   PASS  every real pinned testee id is rostered or excluded  48 testee id(s) checked (onig, pcre2, pcrec, re2, rust, tre, vectorscan)
   PASS  CONTROL: an unlisted testee id is reported by name   ['z-selfcheck-unlisted-testee']
```

## Charter vs. committed

| brief item | committed |
|---|---|
| (1) Add roster rows for `pcrec-auto-align64loops` / `pcrec-auto-nolitrun-align64loops` | done — same syntax tokens as their unaligned namesakes, `cflags` is compilee-only |
| (1) Audit EVERY pinned testee in EVERY `testees/*/configs.toml` against the roster | done — the audit table above, 48/48 accounted for |
| (1) For each: roster row (measured where cheap / reasoned from an existing measured row) or EXCLUDED with a one-line reason | done — twenty new roster rows citing the parse-invariance reasoning already established by `pcrec-auto-noreqbyte`/`pcrec-auto-nolitrun`'s own comments (no fresh witness-compile census run: the brief's "or" is satisfied by the REASONED branch, and re-running a census that four pre-existing comments already state would not add information); twelve EXCLUDED entries |
| (2) A `make check-harness` gate: unlisted testee id FAILS BY NAME, negative control | done — `check_capability_roster_coverage`, 4/4 including the control |
| (3) Regenerate `patterns.rxt`, `--check` clean | done — `python3 bench/capability/gen_patterns.py` then `--check`, exit 0 both |
| (3) Update `bench/capability/CLAUDE.md` and `testees/*` CLAUDE.mds | done — `bench/capability/CLAUDE.md` (a `[B111]` section with the procedure), `testees/CLAUDE.md` (a new-testee rule), `testees/pcrec/CLAUDE.md` (a pointer at the RE-PIN CHECKLIST's neighbour) |
| (4) Run `make check-harness` in the worktree DETACHED, poll the marker | OWED — launched `setsid bash -c '.../gnutimeout 3600 make check-harness > LOG 2>&1; echo "DONE rc=$?" >> LOG' & disown`, PID group cwd-verified in this worktree; log path `/tmp/claude-1001/.../scratchpad/b111_check_harness.log`; STILL RUNNING at report-write time (stdout is buffered under file redirection, so the log has zero bytes until the run finishes or flushes) — see "OWED" below |
| No `store/`/`reports/` writes | true — none made |

## OWED

**The full `make check-harness` run was launched but had not reached its
`DONE rc=` marker by lane end.** The standalone run of the new check
(above) is 4/4 green, and `python3 bench/capability/gen_patterns.py
--check` is independently clean, so the new gate and the roster/excluded
data are proven correct on their own; what is owed is the FULL suite's
count (previously 344 checks / 324 harness + interpreter etc. per the
project CLAUDE.md's last-recorded figure — this lane adds ONE new check
function contributing 4 PASS rows, so the expected new total is the
prior count + 4) and confirmation that nothing else in the corpus
regressed from the `patterns.rxt` regeneration.

- Command: `cd worktrees/b111roster && make check-harness`
- Log: `/tmp/claude-1001/-home-duxevents-pcrec-bench/171b3c1f-9ee4-429b-9a22-732cbcde0af5/scratchpad/b111_check_harness.log`
- Completion line: `DONE rc=<N>` appended after the script's own `check-harness: <PASS> check(s) passed, <FAIL> FAILED` line
- Trigger: poll the log for the `DONE rc=` line (a fresh agent resuming
  this lane, or the manager, checks it directly — `grep -q '^DONE rc=' LOG`)

## Verification

The roster/excluded/real-population arithmetic was checked
programmatically, not by manual count, both before and after
`gen_patterns.py`'s own generation:

```
$ python3 -c "
import sys; sys.path.insert(0, '.')
from pcrecbench import adapters as ad
import bench.capability.gen_patterns as g
roster = set(t for t,_ in g.EXT_BENCH_ROSTER)
excl = set(g.EXCLUDED_TESTEES)
all_t = set(ad.all_testees().keys())
print('total testees', len(all_t))
print('missing:', sorted(all_t - roster - excl))
print('extra:', sorted((roster | excl) - all_t))
"
total testees 48
missing: []
extra: []
```

No pcrec binary rebuild was needed for the standalone/`--check` runs
above (`build/pcrec-a32bc86e` already exists from a prior pin); the full
`make check-harness` run (OWED) uses the same pre-built binary.

## Manager close (2026-09-28)

The OWED full `make check-harness` finished: `check-harness: 599 check(s) passed, 0 FAILED`, `DONE rc=0` (log above). Nothing owed.
