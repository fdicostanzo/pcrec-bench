# Lane b148l5 -- [B148] L5, the callout arms (2026-10-28)

Branch `lane/b148l5`, on master 05560ed9 (L1-L4 merged). Design:
`docs/design/unusual_set_v1.md` v0.2 section 3.2, r9 C5 / C9, section 10's L5 row.
Tier: code + checks + scratch smoke runs. Nothing was written to `store/` or
`reports/`. No timing window ran.

## 1. Charter vs committed

| charter item (3.2 / C5 / C9 / the brief) | state | where |
|---|---|---|
| one shared C body per callee, pure functions (luhn, isbn13, member, netstr, stub; plus netstr-end) | DONE | `bench/unusual/callees/callees.{h,c}` |
| `callees.o` built ONCE with fixed flags, sha256 recorded | DONE: `-O2 -fno-lto -fPIC -std=gnu11` (`-fPIC` added so the one object links into pcrec's `.so` too); cached by key; `callees_sha256` on every callout compile row (508db3eb...) | `pcrecbench/callees.py` |
| counting build `-DUB_COUNT`, never in a timed binary | DONE, checked: `UB_FIRE_LOG` absent from every timed object/binary, present in every counting one | `check_callouts` (1)(2) |
| `cu-unity` declared as a recompile | DECLARED ONLY (the `callees_sha256` description says it is absent on a unity build); the arm is NOT built -- OWED | -- |
| per-engine wrappers + RETURN-CODE MAPPING | DONE: pcre2 `callout_wrap.c`, onig `callout_wrap.c`, pcrec separate-TU binding (`callee_binding_source`) | section 2 |
| first-candidate-fails control | DONE on all five native configs + the oracle's negative control (unmapped -1 abandons) | `check_callouts` (2) |
| arms twin / pass / real; `pass-nofn` pcre2-only | DONE: 3 new `-nofn` patterns (25 patterns, 3,485 expectation rows); `--no-callout-fn` | `members.py`, `gen_patterns.py`, pcre2 `driver.c` |
| pcrec twin also under pcrec-vm | DONE (the gate runs every arm on pcrec-auto AND pcrec-vm) | `check_callouts` (3) |
| no pass arm for co-netstr; assisted netstring `(\d{1,9}):(?>(?s:.)*?(?C4)),` | DONE (unchanged from L3; `4=netstr-end` binds it) | sidecar `[callouts]` |
| pcrec consume callee returns RX_FAIL on an overlong length | DONE, checked (`9:ab,2:cd,` -> the second netstring, = the host reference) | `check_callouts` (2) |
| pcrec REAL bindings in a separate TU replacing [B147]'s pass-through for the callout arms (match_api 11.2-11.4) | DONE: `callout_binding` = `separate-tu-callee`; without the option `separate-tu-pass` unchanged (checked) | `testees/pcrec/adapter.py` |
| counting builds + per-engine fire logs, `callout_fires` per arm per engine | DONE: `harness.fire_pass` after the trials, one fresh process per subject, iters 1; `callout_fires` + `callout_views_sha256` on real/pass match rows | section 3 |
| real - pass reported only where fires match | DONE in the calibration tool (column `real_minus_pass_per_fire`) | section 4 |
| calibration microbench, share on EVERY engine, 20 %/40 % flags, numbers WITH box load | DONE (indicative: box load 8-12 on 16 cores) | section 4 |
| Onig witnesses `(?{...})`, `(*name)` before onig_new, `[\x80-\xff]`, `\G` as a gate | DONE, 4/4 | `testees/onig/callout_witness.c`, `check_callouts` (5) |
| natives only: pcre2 interp/jit, pcrec auto/vm, onig | DONE (deep arms inherit the declarations; `pcre2-dfa` has no arm) | `gen_patterns.py` `UNUSUAL_DELTA` |
| checks wired into check-harness; `pass == twin` a gate | DONE: `tools/check_callouts.py` via `selfcheck.py` `check_callouts_set` (D-3 amended: the gate is L5's now, not L8's) | -- |
| BD16: regular drivers unchanged | DONE, proven: `timed_run` AND `main` instruction-identical, same mod 64, 11 invocations identical | `docs/dev/measurements/2026-10-28-b148l5-instrument-additivity.{py,txt}` |
| full `make check` | OWED (manager launches it; section 6) | -- |

## 2. The return-code mapping (as built)

| callee verdict | pcrec | libpcre2 | Oniguruma |
|---|---|---|---|
| CONTINUE (0) | 0 (`RX_PASS`) | 0 | `ONIG_CALLOUT_SUCCESS` |
| FAIL (-1) | -1 (`RX_FAIL`, identity) | **+1** (backtrack) | `ONIG_CALLOUT_FAIL` (1) |
| CONSUME n (>0) | n (netstr only) | never bound | never bound |

First-candidate-fails control, subject `card 4111111111111112 then 4111111111111111 end`:
real arm answers `(27,43)` and the stub arm `(5,21)` on pcre2-interp, pcre2-jit,
pcrec-auto, pcrec-vm, onig-default. The oracle's negative control: a libpcre2 callout
returning -1 unmapped gives NO match; +1 gives `(27,43)`.

## 3. Fire counts (one iteration, the counting build)

The throughput subjects (1 MB, find-all), the same on EVERY engine:

| member | real fires | pass fires | twin | nofn |
|---|---|---|---|---|
| co-luhn (co-luhn-1m) | 11,308 | 11,308 | 0 (no site) | no counting build (no function) |
| co-isbn (co-isbn-1m) | 8,429 | 8,429 | 0 | -- |
| co-member (co-member-1m) | 13,158 | 13,158 | 0 | -- |
| co-netstr-assist (co-netstr-1m) | 10,971,980 (pcre2-jit: 7,152, then gave up -46) | no pass arm | -- | -- |
| co-netstr, pcrec only (co-netstr-1m) | 24,764 | no pass arm | -- | -- |

Short subjects: `check_callouts` (4) compares the fire DIGESTS (count + sha256 of the
sorted views) over 8 subjects: one group, all five engines identical. The fire-view
multisets on the throughput subjects were compared by COUNT only.

## 4. Calibration (`tools/callout_calib.py`, box load stated)

`docs/dev/measurements/2026-10-28-b148l5-callout-calibration.txt` (the committed run):
`taskset -c 7`, 11 fresh launches per arm, load 8.63 before / 10.70 after (16 cores),
core 7 82.8 % busy over 133 s (mostly this run). NOT a gated measurement.

| member | share range over the six configs | pcre2-jit |
|---|---|---|
| co-luhn | 0.030-0.192 | 0.106 (deep 0.160) |
| co-isbn | 0.028-0.138 | 0.125 |
| co-member | 0.034-0.135 | 0.128 |
| co-netstr (pcrec) | 0.073-0.087 | -- |
| co-netstr-assist | 0.198-0.826, FLAG > 40 % on pcre2-jit-deep (0.736) and pcrec-auto (0.826) | gave up `-46` |

Three runs were taken; the netstr-assist share on the pcrec arms moved 0.37-0.83 between
runs (load), the filter members by a few points. ns/fire from the replay: luhn ~15-20,
isbn ~6-9, member ~5-9, netstr-end ~4-7. `(real - pass)/fires` is noisy under this load
(negative on four rows), so the replay-vs-in-situ cross-check (3.2 item 3) is NOT
established by this run.

## 5. Checks

- `tools/check_callouts.py`: **31/31** (standalone, `/var/tmp/pcrecbench/b148l5/cc2.log`), ~4 min.
- `bench/unusual/check_set.py`: 15/16. The failure is not this lane's (finding 1).
- `gen_patterns.py --check`: 28 files, 0 differences.
- scratch smoke: `quick --subbench unusual --pattern co-member --regime search_short
  --testee pcrec-vm --vs onig-default --subjects 20`: 20/20 pass both, fire pass ran;
  `run_cell` x 4 configs inside `check_callouts` (7), validator-accepted.

## 6. OWED

- FULL `make check`. Command, run from the worktree:
  `cd /home/pcrec/projects/pcrec-bench/worktrees/b148l5 && setsid gnutimeout 7200 make check > /var/tmp/pcrecbench/b148l5/makecheck.log 2>&1; echo "DONE rc=$?" > /var/tmp/pcrecbench/b148l5/makecheck.done`
  (log `/var/tmp/pcrecbench/b148l5/makecheck.log`, marker `.../makecheck.done`). The email
  quick-cell check is load-sensitive; if that is the only red, it is the load.
- The `cu-unity` arm (declared, not built).
- Fire-view multiset comparison on the throughput subjects (counts only here).

## 7. Findings

1. **`check_set.py` triggers a REAL DOWNLOAD.** Since f8c66a01 pinned `fetch_sqlite.py`,
   check 6 (`fetch_sqlite.py refuses by name (table empty)`) runs the fetcher, which
   downloads the pinned SQLite archive whenever `build/unusual/sqlite/dl` is empty (it
   did in this worktree: pinned URL, sha256-verified, vendor files byte-identical to the
   committed ones). On a second run it refuses ("dl is not empty") and the check FAILS.
   The check needs to change to "the pinned fetch is verified" or stop invoking it; not
   changed here (L3's file, a fetch policy question).
2. **pcre2-jit gives up `-46` JIT_STACKLIMIT on co-netstr-assist x co-netstr-1m** at the
   default 32 KiB JIT stack. pcre2-jit-deep answers (`match`, 14,527). A pinned
   pcre2-jit cell will read `gave-up` on that row.
3. **The assisted netstring is O(declared length) per candidate, not O(1).** 3.2 says a
   bad candidate "stops at `len` bytes". It does, but `len` is up to 9 digits: on
   co-netstr-1m one candidate (`g1=[7995,8001)`) fires 955,085 times. 10.97 M fires
   against pcrec's native 24,764. That puts the share over R2's 40 % on two configs. 3.2
   says a share over 40 % on pcre2-jit means resizing before pinned promotion, so the
   co-netstr-1m subject (or the assist) needs that decision before a pinned window.
4. **The expectation oracle uses PYTHON callees** (`unusual_lib.Rx`), not the shared C
   body through ctypes (section 8). End-to-end agreement is shown by the `run_cell`
   rows (C callees, every row matched-as-expected) and by `check_set`'s
   oracle == host reference on 161 subjects.
5. **P3 tension:** the assist's check-at-end callee (`netstr-end`) was written in this lane.
   P3 says it is authored blind and token-counted like any assist (L6).
6. **pcrec-auto's twin and pcrec-vm's twin differ in time** (co-luhn-twin 1.37 ms vs 0.62 ms
   on co-luhn-1m). The route was not read here; M-2 is why the twin runs under vm too.
7. Onig: `(?CN)` is respelled `(?{N})` by the adapter (recorded `callout_respell`); no
   `pass-nofn` arm (an unregistered contents callout is not a defined state).
