# The hybrid-gained-edge census — the reading note

**What this is.** The population behind outbox O-12 ask (v) / inbox I-29 ask
(v): every cell in `bounded@0.2` whose VM-HYBRID prefilter DFA gained the
abi-13 `RX_DFA_SCAN_EDGE` at pcrec pin `a7e0bdf`, with what each cost before
(`263b013`) and after. Frank asked for the breakdown before ruling the trade
accepted or tunable.

**Sources.** `2026-09-01-hybrid-gained-edge-census.tsv` (the table; its own
header names every record read, byte for byte) and
`probe_hybrid_gained_edge.py` (the deriving script, beside it). **This is a
READ of eight pinned records, not a measurement** — nothing was compiled, run
or timed for it. The comparable is `pcrecbench.reduce`'s, imported rather than
re-derived: per row `elapsed_ns / iterations`, summed over the set's subjects
per trial, median over trials; `ratio = after / before`, so > 1 is slower
after.

**The selector**, so it can be argued with:
`engine_metadata.engine == "vm"` AND `dfa_scan_edge` not in (absent, `none`).
A VM artifact carrying a scan-edge stamp at all is by the stamp's own scope
rule a HYBRID — a VM match body with a DFA prefilter — so a non-`none` value
on one is a prefilter that gained the edge while the body stayed the VM's.
`absent` is a pure VM (no DFA scan; the scope iff), `none` is a hybrid whose
prefilter has a scan but no edge in it. Neither gained anything.

## 1. The population is four cells, two artifacts, one regime

| | |
|---|---|
| artifacts that gained the edge | **2**: `nest2-64` whole-subject, `nest3-16` whole-subject |
| testees carrying them | **2**: `pcrec-auto` (caps) and `pcrec-nocaps` — the same artifacts, twice |
| record cells | **4** |
| regimes exercising them | **`match-compliance` ONLY** |
| stamps, identical on all four | `engine=vm`, `engine_sel=collapsed-prefilter`, `dfa_prefilter=byte-class-bounded`, `dfa_scan=unanchored`, `dfa_scan_edge` **absent → `range`** |

Nothing else in the set qualifies. The rest of the AFTER artifact census, one
entry per pattern × form on each `auto` record: `dfa`/`range` 24,
`dfa`/`none` 13, `dfa`/`bitmap` 7, `vm`/`none` 8 (the four `ctx-*` rungs, both
forms — hybrids whose prefilter has a scan and no edge), `vm`/absent 4 (the
`declined-nullable` set), 2 refusals. The two forced-VM testees stamp `absent`
on all 60 forms: no DFA anywhere, so no edge anywhere.

## 2. The trade is between two DIFFERENT artifacts of the same pattern

`adapters.py:form_for_regime()` measures `match` on the WHOLE-SUBJECT artifact
and every other regime on `plain`. So:

| pattern | artifact | engine | regimes measured on it | after ÷ before |
|---|---|---|---|---|
| `nest2-64` | whole-subject (**the hybrid that gained the edge**) | vm | match | **1.048 / 1.051** (slower) |
| `nest2-64` | plain (sibling) | dfa | throughput | 0.630 (faster ×1.59) |
| `nest2-64` | plain (sibling) | search | dfa | 0.667 (faster ×1.50) |
| `nest3-16` | whole-subject (**the hybrid**) | vm | match | **1.033 / 1.037** (slower) |
| `nest3-16` | plain (sibling) | dfa | throughput | 0.633 / 0.637 (faster ×1.57–1.58) |
| `nest3-16` | plain (sibling) | search | dfa | 0.666 / 0.668 (faster ×1.50) |

**The ledger's "thr ×1.57–1.59 faster, match ×1.04–1.05 slower" is not one
artifact's trade.** The throughput and search wins belong to the plain DFA
artifact; the hybrid that gained the edge is only ever measured in `match`,
and there it only ever got slower. A reader who wants the hybrid's own
throughput number will not find one in this set: the whole-subject form has no
throughput cells by construction.

## 3. The slowdown is a FIXED per-call term, not a proportional one

Per subject (both `auto` testees agree to within 0.03 on every row; figures
below are `auto-caps`):

| pattern | subject | before ns | after ns | Δ ns | ratio |
|---|---|---|---|---|---|
| `nest3-16` | `f-year-4` (4 digits) | 24.0 | 36.5 | **+12.5** | 1.523 |
| `nest3-16` | `f-year-3` (3 digits) | 23.1 | 35.1 | +12.0 | 1.515 |
| `nest3-16` | `d-00016` | 33.4 | 41.3 | +7.9 | 1.235 |
| `nest3-16` | `d-00256` | 249.3 | 257.6 | +8.3 | 1.034 |
| `nest2-64` | `f-year-4` | 17.7 | 23.7 | +6.0 | 1.338 |
| `nest2-64` | `d-00016` | 24.8 | 30.7 | +5.9 | 1.239 |
| `nest2-64` | `d-00017` | 25.4 | 31.3 | +5.9 | 1.231 |
| `nest2-64` | `d-00027` | 31.1 | 37.2 | +6.1 | 1.198 |
| `nest2-64` | `d-00028` | 31.7 | 37.9 | +6.2 | 1.193 |
| `nest2-64` | `d-00256` | 223.9 | 231.8 | +7.9 | 1.035 |

Three readings, all from the table:

1. **The absolute delta is flat.** On `nest2-64` it is +5.9 to +7.9 ns across
   subjects spanning 4 to 256 digits and 17.7 to 223.9 ns of work — a
   ×13 span of call cost against a ×1.3 span of delta. The ratio moves only
   because the denominator does.
2. **It fires exactly on the cells that MATCH, and on no others.** The seven
   moved subjects are the seven pure-digit ones (`f-year-3`, `f-year-4`,
   `d-00016`, `-00017`, `-00027`, `-00028`, `-00256`) — every subject in the
   set that these two nests match whole. The other 23 are unmoved at
   ×0.98–1.01, and that includes subjects that ENTER the digit run before
   failing: the dotted quads and CSV records (+0.1 to +1.6 ns) and the hex
   fields, which came out 0.7–1.0 ns FASTER. Failing calls did not pay; the
   spread of their base costs (12.7 / 23.3 / 41.6 / 143 ns, by how far each
   gets before it fails) is unchanged pin to pin.
3. **Therefore the ×1.53 worst case is the ×1.08 entry cost seen on a 24 ns
   call**, not a second effect. `f-year-4` is a FOUR-BYTE digit run: the
   shortest MATCHING call in the set, and the one where a fixed ~+6–12 ns
   lands hardest.

## 4. What this says to ask (v), and what it does not

- **The population is small and named**: two whole-subject nest artifacts, no
  everyday shape, no ladder rung. If the trade is ruled "accepted", it is
  accepted for two cells.
- **The cost has the shape of a knob, not of a design consequence**: a fixed
  entry term paid per MATCHING call, with the loss concentrated
  entirely on runs short enough that the term is a large fraction of the call.
  A skip-below-k-count rule would remove it where it hurts and keep it where
  the ×1.5–1.6 wins are, which is the same conclusion ask (ii) reaches from
  `year4` and `dotted4` — **one term explains both**, as O-12 (v) guessed.
- **What this cannot say**: where the boundary is. The set has digit runs at
  3, 4, 16, 17, 27, 28 and 256 only, and every one of them is on the wrong
  side of it. `bounded@0.3`'s low-rung sweep and its short-run digit family
  (`bench/bounded/NOTES.md`, "What 0.3 added") are the instrument that reads
  the crossing point off a ladder instead of interpolating it from six points.
- **What this is not**: a ranking input, a record, or a reporter surface
  (`docs/dev/measurements/CLAUDE.md` rule 5). The numbers are re-reductions of
  records the 2026-08-31/09-01 windows already measured and the acceptance
  ledger already read.
