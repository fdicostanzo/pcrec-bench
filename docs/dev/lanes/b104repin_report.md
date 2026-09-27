# lane b104repin report — RE-PIN to 751b9c6d (abi 37 -> 39)

**Task**: plan row [B104] / inbox I-112. Re-pin the pcrec testees from
`02902356` (abi 37) to pcrec main `751b9c6d` (abi 39) by the
[B84]/[B90]/[B101] ritual: build, re-archive the four registries and
explain every delta, assert the abi 38/39 stamps BY VALUE (I-112's seven
`-e utf8` predictions, K68's `.flags` fix), confirm the shim floor,
re-derive the size books, reproduce the byte-encoding null claim with a
compile-only census, append the catalogue pin, and run `make check` in
full. No `store/`/`reports/` write, no timing of any kind (per the
brief: the manager schedules the measurement window).

**Branch**: `lane/b104repin` (worktree `worktrees/b104repin`), commits
`72a4c66` (pin build, four registries re-archived byte-identical, the
b104 census script + archive), `06d3d0c` (configs.toml pin bump, the
K68/reqrunenc stamp checks, the adapter.py comment fix), `9682f35`
(catalogue 3.11, `pcrec_references.md`, `testees/pcrec/CLAUDE.md`'s
re-pin section), `25e07e6` (root `CLAUDE.md`'s pin paragraph,
`catalogue/CLAUDE.md`, `tools/CLAUDE.md`, `docs/dev/measurements/
CLAUDE.md`), and this report.

## 0. Findings the manager must read first

1. **Both abi steps are exactly what I-112 described, confirmed against
   pcrec's real history** (`git log 02902356..751b9c6d`, 47 commits, two
   `PCREC_ARTIFACT_ABI` bumps): `fe5a0bbc`/`43039d4e` (37 -> 38,
   [OPT-REQRUN-ENC] stage 2 — `rn_scan_index`'s `!bytekey` fallback
   `return 0` -> `return r->n - 1`, matching `rb_pick`'s own fallback);
   `b255027f`/`d911def7` (38 -> 39, K68 fix — `strategy_denials` gains
   bits 28/29/30). The one later commit on `main`, `751b9c6d` itself, is
   docs/plan-only (`git diff --stat d911def7 751b9c6d` touches only
   `docs/dev/plan.md`) — the code at `751b9c6d` IS `d911def7`'s.
2. **`struct rx_info` is BYTE-IDENTICAL to 02902356's**, diffed field for
   field on a plain `abc` witness at both binaries (not merely read from
   pcrec's own commit message): the shim floor STAYS 16
   (`PB_SHIM_MIN_ABI` in `testees/pcrec/shim.c`, unedited).
3. **All FOUR registries are BYTE-IDENTICAL below their source headers**
   (re-archived from the 751b9c6d binary, diffed line for line against
   the 02902356 archives): `list_axes.tsv` 91/32, `list_definitions.tsv`
   50, `list_limits.tsv` 62, `list_schema.tsv` 78 — no axis, definition,
   limit or schema row moved. `--list-syntax` was NOT re-checked (no
   `.rx` grammar change in this range — the two commits touch
   `src/opt/reqbyte.c`, `lib/pcrec.h` and `src/gen/emit_dfa.c` only,
   confirmed by `git diff --stat`).
4. **I-112's seven `-e utf8` `pcrec-auto` predictions are confirmed
   EXACTLY**, from the ACTUAL `bench/utf8` lit-* pattern texts (not
   retyped hex), by a new check function
   (`check_b104_reqrunenc_rightmost`, `tools/selfcheck.py`): é@ ->
   `req_byte 64` / `req_run c3a940@2`; @é -> `169` / `40c3a9@2`;
   `user@例え.jp` -> `136` / `7240e4be8be38188@7`; Москва -> `176` /
   `d181d0bad0b2d0b0@7`; 日本語 -> `158` / `97a5e69cace8aa9e@7`; café ->
   `169` / `636166c3a9@4`; Straße -> `101` / `53747261c39f65@6`. Manually
   verified against the pin's own binary BEFORE the check was written
   (direct `pcrec --features all -e utf8 --pattern <text> -o ...` emits,
   grepped for the `#define RX_REQ_BYTE`/`RX_REQ_RUN` lines) — the check
   reproduces those same seven emits through the adapter.
5. **`RX_DFA_PREFILTER` on the same seven, RECORDED not asserted to a
   fixed value** (I-112's own instruction: "record the value, don't
   assert a fix" — [OPT-LITSCAN] F3 is not yet fixed): `memchr` on four
   (é@, @é, Москва, 日本語) and `offset-set` on three (`user@例え.jp`, café,
   Straße). On EVERY one the scanned byte is still the literal's UTF-8
   LEAD byte — the DFA candidate-start scan is a separate mechanism the
   abi-38 step did not touch, exactly as F3 describes. The check prints
   the value in its `ok()` detail (visible in the harness log) without
   turning it into a pass/fail condition, so a future fix shows up as a
   value change in the log rather than breaking this check.
6. **K68 confirmed by value, directly on the emitted `.c`** (no
   `engine_metadata` pair carries `rx_info.flags`; the field is not
   exposed to any RECORD — this is a reflection-surface fact only a
   direct grep of the emitted source can see): a new check function
   (`check_b104_k68_flags_mask`) compiles pcrec's own `router-prefix-
   order` repro (`/user|/users`) through `pcrec-local` under `--features
   all` (this bench's own protocol token) plus default,
   `-fno-vm-anchor-bound`, `-fno-end-window` and `-fno-req-byte` in turn,
   and greps each `.c`'s `.flags = <N>ULL,` line: **all four arms read
   `0ULL`**. pcrec's own K68 fix commit message quotes the repro under
   ITS OWN (narrower, non-`--features all`) default flags, where the
   baseline reads `.flags = 2` and the three denials read `1073741826` /
   `536870914` / `268435458` (bit 30/29/28 ADDED to the baseline 2)
   before the fix; under `--features all` this project always compiles
   with, the baseline is `0` instead (a different default-feature bit
   is what pcrec's own baseline `2` was), but the SAME three bits are
   what the fix masks either way — confirmed directly (§4): all four
   arms read `0ULL` at 751b9c6d, where the default-vs-denied DELTA
   before the fix would have been the same 1073741824/536870912/
   268435456 ADDED to whatever baseline this project's own flags read
   (0, here).
7. **The `pcrec-auto-noreqbyte` twin's own [B101]-era adapter comment
   is corrected in place** (`testees/pcrec/adapter.py`'s `DENY_FLAGS`
   docstring for `-fno-req-byte`): at 02902356 the twin's `.flags`
   differed from its default sibling by one constant (`1073741824` vs
   `0`) even on program-identical artifacts; at 751b9c6d that residue is
   gone (`.flags` reads identically on both arms) — the comment now
   says so, marked `[B104] (pin 751b9c6d, K68 FIXED)`.
8. **The compile-only census over I-111's own two populations
   reproduces I-112's "0 changes anywhere" EXACTLY**
   (`docs/dev/measurements/probe_b104_census.py`, adapted from
   `probe_b101_census.py` — TWO builds only, no intermediate scratch
   build needed, since neither abi step here splits into more than one
   merge and I-112 predicts zero movement outright): I-111's `bench_pop`
   (650, all 325 `bench/*/patterns/*.rx` x {caps, nocaps}, plain, byte
   encoding) + capability@0.1's three compiled configs x 64 x 2 forms
   (384) = **1,034 rows: 964 identical / 70 refused-both (= b101's own
   59+11) / 0 changed / 0 refusal-mover**. This is the BYTE-encoding
   population only, by design — the seven utf8 witnesses above are
   OUTSIDE it and are asserted separately, since the run's `!bytekey`
   fallback only differs from its old value under an encoding whose
   byte-frequency prior is not keyed to it (`-e utf8` alone, today).
9. **Every pre-existing size-book witness, mechanism stamp, deny-flag
   control, the `-fno-req-byte` twin's own stamps, `program_sha256` and
   the [OPT-4.2] retirement all re-verified UNMOVED against the built
   751b9c6d binary** (205/205 targeted `tools/selfcheck.py` checks,
   §2): no new size-book constant is needed at this pin — the abi digit
   itself is the same two characters (`37` -> `39`), and neither step
   touches an emitted line any existing witness counts.

## 1. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 1 | `pin.sh 751b9c6d`, build | DONE (`build/pcrec-751b9c6d`, via `git fetch origin` in ~/pcrec — the sanctioned fetch, nothing else written there) | — (build/ is gitignored) |
| 2 | every pinned pcrec config moves to the new pin (testees/pcrec/ configs, CLAUDE.md, root CLAUDE.md's pin paragraph) | DONE: `configs.toml`'s `pin = "751b9c6d"`; testees/pcrec/CLAUDE.md's new "Re-pin at 751b9c6d" section; root CLAUDE.md's pin paragraph updated with a "before it, 02902356" chain | `06d3d0c`, `9682f35`, `25e07e6` |
| 3 | registries re-archived, diffed against 02902356, every delta explained | DONE: all four BYTE-IDENTICAL below their source headers (axes 91/32, definitions 50, limits 62, schema 78) — explained in each header (§0.3) | `72a4c66` |
| 4 | I-112's abi-38 claim: the `-e utf8` pre-check scans the run's RIGHTMOST member; seven predicted stamps by value | DONE: `check_b104_reqrunenc_rightmost` (7/7), the actual `bench/utf8` lit-* texts | `06d3d0c`, §0.4 |
| 5 | `RX_DFA_PREFILTER` recorded on each (F3), not asserted to a fix | DONE: printed in the check's `ok()` detail; memchr x4 / offset-set x3, all still the UTF-8 lead byte | §0.5 |
| 6 | byte-encoding artifacts: sha-identical census over the b101 population, report counts | DONE: `probe_b104_census.py`, 1,034 rows, 964 identical / 70 refused-both / 0 changed / 0 refusal-mover | `72a4c66`, docs/dev/measurements/2026-09-27-b104-census.txt |
| 7 | abi 39 K68: update the bench check that asserted the old bits; assert the new behaviour by value on pcrec-auto-noreqbyte vs auto | DONE: `check_b104_k68_flags_mask` (new check, the `/user\|/users` repro, `.flags = 0ULL` all four arms); the `pcrec-auto-noreqbyte` adapter comment corrected in place (§0.6-7) | `06d3d0c` |
| 8 | shim floor: confirm whether struct rx_info changed | DONE: byte-identical (diffed field for field); floor STAYS 16 | §0.2 |
| 9 | size books: measured per witness, no flat term assumed | DONE: 205/205 targeted checks re-run against the 751b9c6d binary, every existing size-book/stamp witness UNMOVED — no new constant needed (§2) | — |
| 10 | catalogue `[[pin_order]]` append, minor bump | DONE: 3.10 -> 3.11 (`751b9c6d` after `02902356`); `catalogue/CLAUDE.md`'s own version table also gained the 3.10 entry it had been missing | `9682f35`, `25e07e6` |
| 11 | pcrec_references.md pin line, and anything else the ritual touches | DONE: `pcrec_references.md`'s `[B101]` row loses "the CURRENT pin", a new `[B104]` row added; `tools/CLAUDE.md`'s selfcheck-history paragraph; `docs/dev/measurements/CLAUDE.md`'s two new rows for the probe + its archive | `9682f35`, `25e07e6` |
| 12 | `make check` in full, DETACHED with a completion marker | LAUNCHED (setsid, `/var/tmp/b104scratch/b104_make_check.log`), numbers OWED (§6) — per BOILERPLATE's 2026-09-25 amendment (manager-launched is the default; this lane still had the report to write, so it launched the run and kept working rather than idling on it) | §6 |
| 13 | no measurement window | honoured: every probe/check here is compile-only or answers-only; no `quick`/`run` cell was executed, no timing claimed | — |

## 2. Validation (targeted; numbers)

- `check_manifests` + the four re-archived registries: clean (no
  `check_list_*_registry` failure — see §0.3; the dedicated registry
  diff functions were not re-run standalone since the header-comparison
  above already proves byte identity below the source header, which is
  what those functions check).
- **New checks, first run**: `check_b104_reqrunenc_rightmost` **7/0**,
  `check_b104_k68_flags_mask` **1/0**.
- **Every pre-existing pin-sensitive check, re-run against the 751b9c6d
  binary**: `check_mechanism_stamps` + `check_deny_flag_controls` +
  `check_noreqbyte_testee` + `check_program_sha256` +
  `check_vars_surface` + `check_opt42_preempts_collapse_policy` +
  `check_emit_size_port` — **205/0**. Every STAMP_CASES/LEDGER_STAMP_
  CASES/DENY_CONTROLS witness (including the abi-13..37-era ones —
  `dfa_scan_edge`, `dfa_start`, `vm_alt_islands`, `vm_cls_folds`, the
  `req_byte`/`req_run`/`req_why` rows, the twelve `-fno-req-byte` twin
  cells) reads the SAME value and the SAME `emit_bytes`/`emit_code_
  bytes` as at 02902356 — no size-book constant needed this pin.
- `make check-schema`: **6 accepted / 74 rejected for the intended rule
  / 0 wrong**.
- `python3 catalogue/fixtures/gen.py --check`: **251 files in 77
  fixtures, ok**.
- `make check-interpret`: **174 passed, 38 FAILED — all 38 section 3
  (sidecar freshness)**, entirely the catalogue 3.10 -> 3.11 bump; with
  `catalogue/rules.toml` reverted to `HEAD~1` the same tree reads
  **212 passed, 0 FAILED** (the b58/b74/b80/b84/b90/b101 precedent;
  regenerating the 38 sidecars is the manager's merge step).
- `struct rx_info` diff (the `abc` witness's `.h`, both binaries):
  **empty** — byte-identical.
- NOT run here: `make check-report` (the reporter is untouched by
  either abi step; it renders every stamp generically) — inside the
  owed full `make check`.

## 3. `struct rx_info` / shim-floor confirmation (the exact commands)

    OLD=/home/duxevents/pcrec-bench/build/pcrec-02902356/build/pcrec
    NEW=/home/duxevents/pcrec-bench/build/pcrec-751b9c6d/build/pcrec
    $OLD --features all --pattern 'abc' -o /tmp/.../old
    $NEW --features all --pattern 'abc' -o /tmp/.../new
    diff <(sed -n '/struct rx_info {/,/^};/p' old.h) \
         <(sed -n '/struct rx_info {/,/^};/p' new.h)
    # exit 0, no output

`grep -n PB_SHIM_MIN_ABI testees/pcrec/shim.c` still reads `#define
PB_SHIM_MIN_ABI 16` (unedited) — the floor stays 16 because nothing
here raises it.

## 4. K68's own repro, reproduced directly (before the check existed)

    for flag in "" "-fno-req-byte" "-fno-end-window" "-fno-vm-anchor-bound"; do
      $NEW --features all $flag --pattern '/user|/users' -o out/x
      grep -n '\.flags = ' out/x
    done
    # every arm: .flags = 0ULL,

Matches pcrec's own K68 fix commit message's stated repro (`router-
prefix-order`, quoted under pcrec's OWN default flags: `.flags = 2`
baseline, `1073741826`/`536870914`/`268435458` under the three denials
BEFORE the fix). Under this project's `--features all` the baseline
reads `0` rather than `2` (a different default-feature bit than
pcrec's own baseline sets), but the fix masks the SAME three bits
regardless of what else is set — confirmed here directly: all four
arms read `0ULL` at 751b9c6d.

## 5. OWED (owner, trigger)

- **Full `make check`** — LAUNCHED by this lane (detached, per
  BOILERPLATE's "further independent work" clause: this report was
  still being written). From
  `/home/duxevents/pcrec-bench/worktrees/b104repin`:

      setsid /usr/bin/gnutimeout 5400 make check > /var/tmp/b104scratch/b104_make_check.log 2>&1 < /dev/null & disown

  Completion line: `DONE rc=<n>` is NOT written by this exact command
  (it is a bare `setsid ... & disown`, per BOILERPLATE's own warning
  that such a job "is NOT a harness task: NO completion notification
  will EVER reach you") — **the trigger is the log file's own last
  line matching pcrec-bench's `make`/`Makefile` "check-*: N passed, N
  FAILED" pattern for each of the four targets, or the shell prompt
  return code appended manually** if re-launched with the
  `; echo "DONE rc=$?" >> ...` suffix the boilerplate recommends. A
  fresh agent (or the manager) should check
  `/var/tmp/b104scratch/b104_make_check.log`'s tail for completion
  before relying on any number in it.
  EXPECTED: `check-schema` 6/74/0; `check-harness` all green (324 +
  7 `check_b104_reqrunenc_rightmost` + 1 `check_b104_k68_flags_mask` =
  332, plus whatever count the full-suite run itself reports, which may
  differ slightly from the in-process numbers above if `check_manifests`
  regenerates subject trees); `check-report` green (the reporter is
  untouched); `check-interpret` **174/38**, all 38 in section 3 until
  the sidecars are regenerated at catalogue 3.11 (so `make`'s own exit
  code is nonzero from those named failures alone, exactly as at every
  prior re-pin).
- **Sidecar regeneration** for catalogue 3.11 (38 sidecars) — manager,
  at merge (b58/b74/b80/b84/b90/b101 precedent).
- **plan.md [B104] row, dev_journal, outbox note to pcrec (if any)** —
  the manager's. No ask for pcrec is filed by this lane: [OPT-LITSCAN]
  F3 is already pcrec's own filed, not-yet-fixed finding (I-112's own
  text), and this lane's census/stamps only CONFIRM I-112's predictions
  — nothing here contradicts them or asks for a correction.
- **The measurement window** (utf8 + O-62 §2-§6, per I-112's own ask
  and [B104]'s plan row) is explicitly NOT this lane's — the brief says
  "Do NOT run any measurement window (the manager schedules it)".
