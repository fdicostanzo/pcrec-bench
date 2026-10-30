# b148l9rread report -- the READ of [B148] L9's RE-RUN window (b148l9r, pcrec 614d45eb3)

Lane b148l9rread (Sonnet), branch `lane/b148l9rread`, 2026-10-30. Read-only over the scratch store and the window logs;
no timing, no `pcrecbench run/quick`, no `callout_calib`, no pcrec build, `store/` untouched, nothing under `bench/` touched,
no script cap changed (so `make check` / `make check-unusual` were not run: docs, measurements and helper scripts only). No
store-loading job was started (every number comes from streaming the JSONL records directly; no reporter render), so there
is no detached job and no OWED marker. The derivation is the ledger
`docs/dev/ledgers/2026-10-30-unusual-0.1-l9r-scratch-addendum.md` (section numbers below are its); L9's ledger is unedited.

## Charter-vs-committed checklist

| brief item | where |
|---|---|
| 1(a) status of each of the 7 cells, with the pre-flight and target-core readings | ledger 2(a) |
| 1(b) numbers of now-`measured` cells vs L9's IL ones, size of each move, effect on L9 verdicts 1(a)-(g) as CONFIRMED / AMENDED / UNREAD | ledger 2(b) (distribution table, headline table, per-verdict table) |
| 1(c) cell walls vs L9 and vs the 7200 s CELL_CAP | ledger 2(c) |
| 1(d) fresh calibration: callee shares per member/engine against L9 verdict 5; do the >40 % flags survive | ledger 2(d) |
| every verdict states what was read and what was not | ledger 2(b) closing paragraph, 2(d) tail, section 3 |
| 2 calibration archived verbatim with a D35 header | `docs/dev/measurements/2026-10-29-b148-l9r-callout-calib.txt` |
| 2 scratch report groups under `measurements/2026-10-30-b148-l9r-*` only if rendered | NOT rendered (stated in the ledger header); the helper scripts are `docs/dev/measurements/2026-10-30-b148-l9r-scripts/` |
| 2 update `measurements/CLAUDE.md` and `ledgers/CLAUDE.md` | done (and `lanes/CLAUDE.md` for this report) |
| 3 this report with checklist, verdicts, OUTBOX DRAFT, upstream CANDIDATES, outbox and `upstream_findings.md` NOT written | below |

## Verdicts (each: what was read, what was not)

1. **4 of 7 re-run cells are now `measured`** (rust-default, onig-default-assist-v01, pcrec-auto, pcre2-interp; pre-flight
   busiest other core 8.65 / 3.01 / 1.80 / 2.61 %, target core 0.0-5.0 %); **3 stayed `inconclusive-load` on three different
   clauses** (onig-default-deep: a 16.80 % non-target core; rust-default-assist-v01: the TARGET core at 12.97 % and another core at
   15.99 %; pcre2-interp-deep: load1 2.24 > 2.00 with the busiest other core at only 2.01 %). 7/7 at attempt 1, trial agreement
   `agree` with 0 disagreeing groups on all seven. The standing 5-6 % background persists (timeline medians 5.4-6.5 %); it
   is the 10-17 % bursts landing in the 5 s pre-flight that cost the status, and the opening `quiet` again read NOT QUIET (2 of 5
   failed). NOT read: which process the bursts are.
2. **The L9 IL numbers were right.** Outcomes are IDENTICAL cell for cell in all seven (15,374 cells, 0 outcome-set
   differences, including the 24 + 8 + 3 pcrec default-arm `PCREC_ERR_FRAMES` give-ups, the 2 all-timed-out groups on interp /
   interp-deep / onig-deep, the Onig silent wrongs); the per-testee, per-regime MEDIAN of the cell ratios new/old is 0.985-1.005 and the p5-p95 band 0.967-1.070, headline cells within x0.976-x1.045 (the largest: wild-json-validate js-1m on onig-deep x1.045,
   comment-5m onig-deep x1.024, co-isbn interp x0.976). The same holds for the three cells that stayed IL, so an IL status
   in this window pair was NOT a biased timing. One unexplained exception: pcre2-interp `cscan` throughput on `nest-paren-128/512/1k`
   (default arm) and `nest-paren-128/512/1k/2k` (deep arm) reads x1.16-1.22 slower in the re-run (10.0 -> 8.5 MB/s), the same
   pair of two-level values on both arms inside each window, nothing on 8k-100k and nothing on the headline
   `nest-paren-32k` (9.9 MB/s both); mechanism not isolated.
3. **L9 verdicts 1(a)-(g):** (a) CONFIRMED for the 7 cells, UNREAD for the other 12; (a') CONFIRMED (D-1, D-2 outcomes cell for
   cell); (b) AMENDED (the roaming-competitor reading holds but "coin flip at the threshold" is sharpened to real busy cores, and
   a load1 cause appears); (c) CONFIRMED (both 100k groups time out again, the quadratic ladder reproduces: interp 32k
   31.03 -> 31.23 s, onig-deep 9.20 -> 9.22 s); (d) CONFIRMED; (e) fire counts CONFIRMED, shares AMENDED; (f) CONFIRMED where a re-run
   exercised it (rust-assist vars: R10B-5/6 not seen, a second sample), UNREAD for R10B-10/11 and R10A-7; (g) CONFIRMED
   (interp 146.2 -> 145.4 MB/s on comment-5m; the pcrec default arm's stream give-ups 100/256, 1,723/4,096, 163/311,
   2,620/4,971 reproduce with byte-identical `results_sha256`).
4. **Walls repeat within 6 %** (225 / 232 / 675 / 1,085 / 2,795 / 2,964 / 2,981 s against L9's 227 / 237 / 718 / 1,093 / 2,794 /
   2,965 / 3,009). The re-run ran at `cell_cap=7200s`; the worst cell used 41.4 % of it (x2.42 headroom). The `CELL_CAP_unusual=7200`
   proposal is CONFIRMED. Total 3 h 06 min for 7 cells + the 41 s calibration.
5. **The >40 % callee-share flags do not survive the fresh calibration.** Taken at load 1.23 (vs 8.6-10.7), after the payload
   fix, the co-netstr-assist ns/fire is 2.99-3.03 on all six arms (it was 3.57-6.71). L9's flagged rows fall: pcre2-jit 41.0 -> 34.5 %,
   pcre2-jit-deep 76.7 -> 36.8, pcrec-auto 78.1 / 79.3 -> 35.3 / 35.7, pcrec-vm 49.4 / 51.4 -> 33.8 / 35.1. What stays: the
   check-at-end spelling spends about a third of its time in the callee (above R2's 20 % bar for pcre2-jit, below the 40 % bar for
   every other arm); the filter members stay 2.8-15.6 % (pcrec-vm co-luhn 23.7 -> 18.2 %); pcrec's native `consume` is 6.5-6.6 %.
   NOT read: a repeat calibration (one run, no spread), a pinned-tier-quiet calibration (the chain's opening quiet sample a minute
   earlier read NOT QUIET).

## OUTBOX DRAFT for pcrec (findings about pcrec only; the manager writes O-n)

The re-run does not change a finding of O-112; it changes one STATUS sentence in it and adds a confirmation. Short erratum-form draft:

> **O-? DRAFT -- erratum + confirmation for O-112 (unusual@0.1 at 614d45eb3).** O-112 said pcrec-auto was one of the 7
> `inconclusive-load` cells. It was re-run on 2026-10-29 (19:52-20:11 EDT, scratch, cpu 7, five trials) and is now `measured`
> (pre-flight busiest other core 1.80 %, target 0.40 %). Every number in O-112 is reproduced: the 24 + 8 + 3 default-arm
> `PCREC_ERR_FRAMES` give-ups on `cscan-onig`, `wild-sexp-balanced`, `wild-json-validate-onig` are the SAME cells, and the compiler's
> call-stream give-ups are 100/256, 1,723/4,096, 163/311 and 2,620/4,971 again with byte-identical result hashes; per-cell median
> times differ by x0.984-x1.021 over the p5-p95 of 2,574 short and 47 throughput cells (testee median 1.000); the vars streams read 197.6 / 205.1 /
> 223.0 us at 4 / 64 / 4,096 bindings (O-112: 194 -> 219 us). The `_in` figures (items 3 and 4) come from `pcrec-auto-in` / `vm-in`,
> which were already `measured` and were not re-run. New, with a calibration taken at load 1.2: the check-at-end co-netstr spelling
> spends 33.8-36.8 % of its time in the callee on the four arms that run it natively (pcrec-auto 35.3 %, pcrec-vm 33.8 %), and
> pcrec's native `consume` spelling 6.5 %; the earlier 78-79 % / 49-51 % in our ledger were a stale load-10 calibration and are
> withdrawn. No new ask.

(Whether this warrants an O-n at all is the manager's call: it changes no ask. It could ride the next pcrec item as a one-line
erratum instead.)

## Upstream-finding CANDIDATES (other engines; unambiguous bugs only)

None new. The three L9 closes-as-NOT-A-BUG stand and are reproduced: the libpcre2 10.46 interpreter's quadratic ladder on deep
subroutine recursion (31.03 -> 31.23 s at nest-brace-32k, again two timed-out groups at 100k), the JIT `-46` stack limit at 512
levels (not re-run), and Oniguruma's silent nest-level-20 no-match (not re-run in its default arm; the deep arm's quadratic ladder
reproduced). The interp `cscan` `nest-paren-128..2k` x1.16-1.22 two-level effect is a within-library, window-to-window
observation of unknown cause and is NOT a candidate.

## Reader / harness findings (bench-side, for the KB list)

- The scratch store now holds TWO records per re-run testee; the reporter's scratch-tier groups pick up both. A reader rendering
  `--grain stream|set` over `build/scratch-store` sees the older (L9) record beside the newer one with no dedup rule (the
  pinned-tier dedup is by status and timestamp; not exercised here because no report was rendered).
- The calibration's own `flag` column marks only `over-budget>20%` on pcre2-jit (34.21 %); it has no 40 % flag, so the L9 ">40 %"
  flags came from the reader/ledger step, not from the file.
- `b148l9r_chain.sh` ran `callout_calib` ungated right after an advisory NOT QUIET sample; the calibration process holds the target
  core 27 % busy for its 41 s by its own work, which a future calibration's pre-flight reading would need to account for.

## OWED (owner / trigger)

- no store-loading or long job outstanding (none launched);
- the three still-IL cells (onig-default-deep, pcre2-interp-deep, rust-default-assist-v01) are a manager decision: a third attempt,
  or accept them as indicative on the strength of the L9/re-run agreement (+-1 % median) — the scratch tier cannot make them `measured`
  without a pre-flight that passes;
- a second calibration run for a spread on the ns/fire (manager), if the shares are to be cited beyond "about a third";
- pcrec's answer to O-112 ask 2 (`conditionals` / `(?(DEFINE)`) before any pinned unusual@0.1 sample (unchanged from L9's OWED).
