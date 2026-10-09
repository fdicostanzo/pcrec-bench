# [B132] lane report: is O-92's short-search slowdown the bench's own shim layout?

Lane b132shim, 2026-10-09, branch lane/b132shim. Archive:
docs/dev/measurements/2026-10-09-b132-shim-layout-ab.txt (+ scripts there).
Scratch tier only, nothing in store/. pcrec NOT rebuilt (pin 255bcdd8 via pin.sh --path).

## Verdict: (a), with the mechanism located one file wider than hypothesised

The slowdown is the BENCH's own instrument, not pcrec. Swapping only
testees/pcrec/{shim.c,driver.c} (c4c70f2c-era 26eebfa -> the 10-08 window-era
e46e326) at the SAME pin 255bcdd8, same artifacts, reproduces O-92 cell for cell.
It is mostly driver.c, not shim.c.

A/B/A/B, OLD vs NEW (master), 22 cells (11 per config), 5 trials, core 11, 75 short subjects:
- Both repetitions agree to <1% (OLD2/OLD1, NEW2/NEW1 inside noise). 0 failed runs.
- The 3+3 controls of O-92 (waf-942360 both configs, keyword-prefix-order, file-ext-order,
  bracket-array-define) are flat (0.99-1.03); the movers move: winpath 1.248/1.254 (O-92
  1.205), trim-nested-star 1.108 (1.170), numeric-id 1.098 (1.145), phone-list 1.10/1.11
  (1.145), us-zip 1.13/1.16 (1.136), base10num 1.075-1.085 (1.118-1.127), ipv4 1.09-1.13 (1.10),
  semdiv 1.065 (1.09-1.10), uuid 1.085/1.096 (1.08).
- (currency-lookbehind-fixed is not program-identical in either config; not a cell here.)

Factor split (9 cells; OLD, MID = shim@master+driver@26eebfa, WIN = BOTH files exactly as of
e46e326, i.e. the window-era adapter before [B129]; NEW = master):
- MID/OLD (the shim alone): ~1.00 on 7 of 9 cells; winpath 1.149, uuid 1.019.
- WIN/OLD: winpath 1.204 (O-92 1.205), trim-nested-star 1.175 (1.170), numeric-id 1.148
  (1.145), us-zip 1.134 (1.136), ipv4 1.098 (1.098), uuid 1.082 (1.080), base10num 1.125
  (1.118); controls flat (waf 0.995, keyword 1.005). The window-era files reproduce O-92 to
  ~1-2 points on every cell: that adapter state IS the 10-08 slowdown.
- WIN/MID (driver.c's 37 added lines, the [B124]/[B126] `info` getters): +10-17% on seven cells,
  roughly +40-50 ns per call, near-constant in ns.
- NEW/WIN (the [B129] prime change on top): 0.95-1.04, mixed; not the cause (it postdates the window).

Layout facts: in every one of 14 artifacts compared (7 patterns x caps/nocaps) the artifact's
own rx_search is at the IDENTICAL address (and size) in both shim arms. The shim's .text grows
exactly +160 B (the five new getter pairs), shifting only the shim's per-call wrappers
pb_search / pb_match_caps (mod 64 changes, e.g. winpath pb_search 16 -> 48, but equally for the
non-moving keyword-prefix-order 48 -> 16, so the wrapper's mod 64 does not separate movers
from controls). The driver's main() grows 12,609 -> 13,479 B (-> 13,686 on master) at the same
start address; its timed loop lies inside main. So the shim-layout hypothesis is only partly
supported (winpath alone, +15%); the bulk is the driver, and WHICH mechanism inside main (loop
placement vs code generation of the timed loop with more live getters) is NOT isolated: no
perf here (paranoid=4) and no address of the loop was extracted. That is OWED if wanted.

## Proposal only (not implemented)
Keep the timed loop out of the translation unit that grows with every re-pin: move the timed
loop into a small, separately compiled function (own object, `__attribute__((noinline,
aligned(64)))`, fixed -O2) called by main, and move the `info`-printing getters into a second
file or a cold section (`__attribute__((cold))`). Then adding stamps changes no timed code and
the bench cannot move a pcrec cross-pin Delta. Add a regression control: a program-identical
reference cell (the waf-like 7 us cells are too insensitive; use winpath-near-miss) timed under
the previous and current driver at every re-pin ([B79]'s null band would then be bench-clean).
Consequence for O-92/O-93: the 2-4% median shift on the program-identical subset is bench
instrument drift from the 10-05 -> 10-08 adapter change and should be struck from the
pcrec-attributable findings; cross-pin comparisons across [B124]/[B126] on short cells carry
that bias in all other cells too, pcre2/other engines' drivers excluded (the pcre2-jit control
flat is consistent with this).

## Method notes (what exactly was run)
- Mechanism: second/third/fourth git worktrees (b132shim-old/-mid/-win, now removed) at 49409c3
  with only testees/pcrec/{shim.c,driver.c} replaced from git (26eebfa / mixed / e46e326), run
  via `python3 -m pcrecbench quick` from each tree (the adapter compiles shim.c/driver.c from
  its own directory). 26eebfa's shim cannot stamp abi 61-66, so OLD and MID needed ONE
  uncommitted adapter.py line (the missing-stamp raise gated on $B132_OLDSHIM; archived as
  2026-10-09-b132-oldshim-adapter.patch). WIN needed none. Nothing committed to master paths.
- Cells selected by engine_metadata.program_sha256 equality (v2) across the O-92 records;
  note a pattern's 2 sha values (plain/whole forms) are compared as sets.
- Layout script initially failed with a relative path; fixed (realpath) and rerun; the archived
  output is the rerun.

## Charter-vs-committed checklist
- [x] worktree b132shim, no push, no store/ writes: done
- [x] program-identity split re-derived and archived: 2026-10-09-b132-select-cells.py
      (identical cells: caps 15, nocaps 24 of 61/62)
- [x] A/B/A/B OLD,NEW,OLD,NEW per cell, quick, search, all short subjects, 5 trials, core 11:
      22 cells (top 8 + controls per config) in -shim-layout-ab-run.sh/-analysis.py
- [x] per-cell NEW/OLD ratio with overlap, reproduction of O-92, beside layout facts: archive sec 1, 3
- [x] .so `size -A` .text size/alignment, hot function mod 64/4096 (nm), 7 patterns x 2 configs:
      archive sec 3 + raw file
- [x] verdict and layout-stable proposal: above
- [x] additional factor split (shim vs driver vs window-era) beyond the brief, because the A/B
      alone confounded two files: archive sec 2
- OWED (not requested): isolate the in-driver mechanism (loop address / disassembly of the timed
  loop between 26eebfa and e46e326 drivers); trial of the proposed isolation.
- Box: ~45 min, one heavy job at a time, load 0.3-0.5 before each launch.
