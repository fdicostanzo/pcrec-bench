# b139gaps report: answer to pcrec I-156 (B4 landing gaps)

Lane b139gaps, read-only fact lane, 2026-10-24. Pin 6b2dbd3e (abi 76). No timing was run. No counter was read.
All files named below are under `/var/tmp/pcrecbench/b139gaps/` (manager commits what it wants to keep).

## 1. What was read, and which cells B4 is judged on

Docs read (pcrec, read-only, via `git show`):
- Branch `lane/memfn-b4prep`. I-156 cites `@0f3c115fa`. The branch tip is `3dd9850c5` (nine commits later). I read the TIP.
  The two differ in the files that matter here: tip adds `expected_losses.md` section 3e (the SHORT-SUBJECT class, L <= 64 B,
  any gap, any regularity; SS1-SS3) and the matching bullet in `r17b_prime.md` 9.2a. The regular-landing rule itself
  (condition 1: B4 mover at OFF; condition 2: regular landings, mean gap <= 8 B) is unchanged between the two.
- `docs/design/memfn/r17b_prime/b4prep/expected_losses.md` (sections 1, 2, 3b, 3e, 4, 5) and
  `docs/design/memfn/r17b_prime.md` 9.2 and 9.2a (lines 2510-2607 of the tip), 1.3a (the table B4 builds), 3.5 (which artifacts move), 8.1 (G1).

Which sets? The docs do NOT name them. They say only "the sets B4 will be judged on" (9.2a, bench's cells), "the bench patterns"
(8.1, B17), and "the official verdict is a bench run on the targeted hardware" (9.2 item 4, D144 add. 4).
My reading, stated so the kit can narrow it:
- Judged sets = every set under `bench/` that has a committed pcrec record at the canonical pin 6b2dbd3e on the 7700X box
  (`ryzen7700x`, the [B138] re-baseline; the store has them): altwide@0.3, bounded@0.3, capability@0.2, email-specimen@0.2,
  litrun@0.1, loglines@0.1, syntax@0.1, utf8@0.1, plus sentinel@0.1 (sentinel cells with a site: none were in the store for the
  core configs, so none survive). This is the [B138] tier 1 + tier 2 roster (`docs/dev/lanes/b138_chain.sh`).
- Judged configs = the CORE pcrec roster: `pcrec-auto` (cfg `auto`), `pcrec-nocaps` (`nocaps`), `pcrec-vm` (`vm`). utf8 uses the `_utf8` siblings.
- Judged regimes = the PLAIN-form search regimes `search_short` and `throughput`. The `match` regime runs the whole-subject
  form (anchored, one attempt at position 0): it has no candidate-landing sequence, so it is excluded.
- This is a SUPERSET. The kit's filter (condition 1: mover at OFF, cover <= 2 terms) is applied by the kit; I give my own
  cover-class flag per row (section 4) but did not reproduce the kit's cover search.

## 2. Result: cells with a set-FIND site, mean landing gap <= 8 B, one dominant gap value

Definitions I used (the docs give none for "one dominant gap value"): landings = every subject position whose byte the site's
emitted table admits; gaps = differences of consecutive landings; "one dominant gap value" = the most common gap covers MORE THAN
HALF of the gaps (share > 0.5), and the cell has >= 16 landings (>= 15 gaps; with fewer, one gap is 100 %, so the share means nothing).
Those thresholds are mine; the full numbers are in the files so the kit can apply others.

Headline counts (cell = config x set x pattern x regime x subject, only cells that exist in the committed store at 6b2dbd3e):
- Cells whose artifact has a set-FIND site: 37,526 (auto 9,228; nocaps 9,228; vm 19,070). Of these, 20,346 have < 2 landings (no gap).
- QUALIFYING (mean gap <= 8, share > 0.5, >= 16 landings): **5,717 cells**. 138 of them are the VM hat at |S| = 1 (B5's F2 cells, not B4).
  Remaining B4-eligible by site kind: 5,579 cells = 2,644 VM hat (|S| >= 2), 2,264 DFA byte-class, 556 DFA first-class-bounded,
  69 VM byte-class, 18+18 byte-class-bounded (VM, DFA), 10 VM first-class-bounded.
- By my cover class (1 / 2 / 3+ terms): 2,650 / 1,812 / 1,117 among the B4-eligible. The 3+ rows should fall out under the kit's condition 1.
- Dominant gap value: **gap 1 in 5,488 of the 5,717** (the table admits almost every byte: dense text, case-insensitive letter classes,
  digit/hex classes over digit-rich subjects). Gap >= 2 in 229 cells (109 at gap 2, 40 at 3, 25 at 4, 28 at 8, 27 at 7).
  Those 229 are listed in full in `groups_qualifying_domgap_ge2.md` (46 groups); the g = 2 and g = 8 families are the ones
  grid2 measured, so read that file first.
- Subject size: 944 of the qualifying cells (869 B4-eligible) have a subject >= 64 KiB (all `throughput`); 1,456 B4-eligible cells have L <= 64 B
  (the 3e short-subject class takes those at ANY gap, so for them the landing filter is not the criterion; `qualifying.tsv` and
  `small_n.tsv` carry `len`).
- Sets with B4-eligible qualifying cells: altwide 1,808; loglines 1,159; bounded 1,116; capability 623; syntax 447; utf8 321; email 105. litrun only at |S| = 1 (B5).
  483 of the eligible cells sit on sets of |S| >= 128 bytes (`.`-like and negated classes); they qualify arithmetically.

Per-cell deliverables (cell id = cfg, set@version, pattern, regime, subject; site kind; subject length; landings; mean gap; dominant gap; share):
- `qualifying.tsv` (5,717 rows, columns `cfg set pattern regime subject len site setsize cover landings mean_gap dom_gap dom_share class`).
- `small_n.tsv` (8,488 rows: < 16 landings; 8,007 of them have mean gap <= 8; NOT reported as qualifying, kept for audit).
- Grouped (per set, pattern, site) tables below and in `groups_qualifying.md` (221 groups; cfg `auto,nocaps` are identical tables
  and are merged; `B5` marks a VM hat with |S| = 1; "regime cells" counts per config, so merged rows show 2x).

The cells whose dominant gap is NOT 1 (the g = 2 / g = 8 style families): 229 cells in 46 groups, all in `groups_qualifying_domgap_ge2.md`.
Of these, 124 are the |S| = 1 VM hat (B5): 121 on litrun@0.1 (65 KiB throughput subjects, gaps 2-8, share 1.00) and 3 on utf8@0.1. The B4-eligible 105 are:
- utf8@0.1 throughput subjects (65,536 B to 1 MiB), dominant gap 2 (or 3), share 0.55-0.92, mean 1.8-7.4, on both DFA byte-class and the VM hat:
  alt-cyr-64, cls-high-range, prp-cyrillic, prp-lu, qnt-class-run (gap 2, up to 1 MiB, mean up to 7.4); ci-neg-fold, cls-dot, cls-neg-single,
  qnt-dot-bounded, cls-neg-cjk, cls-mixed, prp-l, alt-distinct-lead, prp-han (65,536 B, gap 2 or 3).
- syntax@0.1 `unp-p-uc` (77 B subject, 18 landings, gap 4, share 0.65, cover 3+).
No other set contributes a gap >= 2 cell with >= 16 landings.

## 3. Near-misses (so the filter is auditable)

- `groups_nearmiss.md`: 104 groups, 659 cells with 8 < mean gap <= 16 (any share), >= 16 landings.
- `groups_denseirregular.md`: 76 groups, 574 cells with mean gap <= 8 but NO dominant gap (share <= 0.5): dense and irregular.
- `nearmiss.tsv`: the per-cell rows for both (1,233 rows).
- Cells with mean gap > 16: 1,742 (not tabulated). Cells with < 16 landings: `small_n.tsv`.
The two grouped tables follow in appendices B and C; the qualifying groups in appendix A.

## 4. Method, simplifications, controls

Method (all scripts in the lane dir, each with a source header, archive-ready):
1. `compile_all.py`: pinned `build/pcrec-6b2dbd3e/build/pcrec`, the adapter's own argv shape (`-p rx -fcomments --features all [--no-captures | --engine=vm] [-e utf8] -o X.c --pattern BYTES`, `LC_ALL=C`), emit-c only, no gcc, no run. 1,101 compiles (70 refused, by name in `c/manifest.json`).
2. `landings.py`: reads each artifact's own stamps and the site byte table AS EMITTED:
   `RX_DFA_PREFILTER` byte-class / byte-class-bounded -> `rx_can_begin_match[256]`; first-class-bounded (DFA or VM) -> `rx_start_bytes[256]`;
   `RX_VM_START_SCAN` first-class -> `rx_start_set[256]`. Subjects read from the generated trees under `bench/<set>/subjects|throughput` via `pcrecbench.subbench`.
3. `aggregate.py`, `group.py`, `summ.py`, `report_tables.py`: universe control against the store, grouping, tables.

What counts as a set site (and what does not): the one-byte family is NOT a set-FIND site and is excluded: `memchr`, `memchr-bounded`,
`first-memchr-bounded`, `handoff`, `run-pinned`, and `offset-set` / `offset-set-bounded` (checked in the emitted C: in all of them the scanned
offset is a `memchr` on one byte; the `rx_ofs_k0` table is only a candidate verifier). DFA artifacts with `RX_DFA_PREFILTER "none"` carry no site. Excluded artifact counts, auto config: 208 one-byte/none (63 prefilter none, 41 memchr, 41 offset-set, 33 run-pinned, 14 handoff, 10 offset-set-bounded, 2+2 memchr-bounded/first-memchr-bounded, 2 VM no-stamp), 24 refused.

SIMPLIFICATIONS (every one):
1. Landings are every admitted position over the WHOLE subject in one pass. I did not simulate the walk. In the DFA walk, after a landing the forward DFA consumes bytes and the skip loop resumes only when the state returns to the start state, so the walk's actual landings can be SPARSER than the admitted positions (bytes inside a consumed run are admitted but not landed on). For the VM hat (an attempt at every admitted position of a failing path) the two coincide. So DFA-site means are lower bounds on the walk's gap in matching or partly-matching stretches.
2. For a subject with a match, a real search stops at the first match; I computed over the whole subject (as find-all / failing search would).
3. `*-bounded` sites (byte-class-bounded, first-class-bounded, memchr-bounded): the bound (a window limit) is ignored; the byte set is the same table.
4. Hybrid / VM-with-DFA-prefilter artifacts: ONE table per artifact, the one named by the stamps. No artifact in the population carries two of the three table names.
5. A multi-subject cell: not summarised. Every (subject) is its own row; the grouped tables give min-max ranges and the dominant-gap tally across rows.
6. Cover class (1 / 2 / 3+ terms over RANGE, EQ and CUBE terms) is my own exact search over the table's byte set, a flag for condition 1, NOT the kit's cover search (K = 4 limit, term definitions in `terms.c` not reproduced).
7. `auto` and `nocaps` produce identical rows except where the engine route differs; the grouped tables merge them. `vm` is the forced-VM config, so its sites are all VM hats.
8. Only the plain form. The whole-subject form's VM hat exists but its subjects are the `match` regime (excluded above).
9. The "share > 0.5" and ">= 16 landings" thresholds and the cutoffs for the near-miss table are mine.

Controls (both share no code with `landings.py`'s parsing):
- Stamps: my compile-only `(engine, dfa_prefilter, vm_start_scan)` vs the committed store's compile-row `engine_metadata`, plain form, 6b2dbd3e, ryzen7700x: **1,309 equal, 9 differ**. The 9 are 3 utf8 patterns x 3 configs (`cls-d-ucp`, `cls-s-ucp`, `ci-ucp-invariance`) that the store REFUSED (they need `--ucp` per declared pattern, which I did not pass); they are dropped from the cell list (490 cells), as are 5 sentinel patterns not present in the store at this pin (375 cells).
- Table vs facts: for every artifact with a table site I asked the same binary for `--emit-facts` `start_set` and compared the bitmaps byte for byte: **416 equal, 3 differ, 1 no fact**. The 3: capability `wild-codegrammar-json-number-extended` and `wild-semdiv-empty-alt-repeat-pcre2` (fact 11 bytes, table 10) and email `factored` (fact 256, table 56): the emitted table is narrower than the fact. The report uses the emitted table, as the brief asked. `syntax/rec-fwd` has no fact row.
- Hand check: two cells recomputed in a plain Python loop from the C table (bounded `year4` auto, altwide `w-1024` vm): landings, mean, dominant gap and share identical.
- Cell universe: 37,526 of my 38,391 computed cells are in the committed store's match rows (the other 865 are the dropped patterns above).

NO COUNTERS. `perf stat` works for this user in USER mode on this box right now (`perf_event_paranoid` is 2, `branch-misses:u` and `branches:u` read: 2,705 and 27,395 on `true`), so the older "perf is refused" note is not true today for `:u` events. I did NOT read any counter, because reading branch misses per landing means building and running the artifacts, which the lane's no-timing, compile-only scope excludes. The answer is therefore the gap sequence alone, marked `selected-without-counters` in the rule's wording. A follow-up lane could take `branch-misses:u` per landing on the qualifying cells if the manager clears it.

## 5. Draft outbox paragraph (answers I-156)

> O-xx, answer to I-156 (B4 landing gaps). I read branch lane/memfn-b4prep at its tip, 3dd9850c5, not 0f3c115fa. The rule is unchanged between them; the tip adds the short-subject class. The docs do not name the judged sets, so I took every bench set with a committed record at 6b2dbd3e on the 7700X (altwide, bounded, capability, email, litrun, loglines, syntax, utf8) and the three core configs (auto, nocaps, vm), plain-form search regimes only. For each cell with a byte-class, first-class or VM-hat table site, I took the table as emitted and listed every subject position it admits. I did no timing and read no counters; perf does work in user mode here, but I did not use it. With at least 16 landings, a mean gap of at most 8 bytes and one gap value covering more than half the gaps, 5,717 cells qualify; 138 are the one-byte VM hat (B5, not B4). In 5,488 of the 5,717 the dominant gap is 1, because the table admits almost every byte. 229 cells have a dominant gap of 2 or more: the 65 KiB to 1 MiB utf8 throughput subjects at gap 2 or 3, and one 77 B syntax subject (unp-p-uc, gap 4). The per-cell rows, the near-miss rows (mean gap up to 16, or dense with no dominant gap) and the scripts are in the lane files. I simulated no walk, so DFA means are lower bounds. Offset-set and memchr prefilters are one-byte sites and are left out. The kit applies condition 1 and its own regularity test.

## 6. Charter-vs-delivered checklist

| item in the brief | delivered |
|---|---|
| Read BOILERPLATE first | done |
| Read I-156 verbatim | done (docs/dev/inbox_from_pcrec.md, "## I-156") |
| Say which branch rev was read, cited vs tip | done: tip 3dd9850c5 vs cited 0f3c115fa, diff stated (section 1) |
| Filter rule from r17b_prime.md 9.2a | done (section 1, quoted conditions) |
| Judged sets/cells, with reading and source lines when ambiguous | done, ambiguity stated with the lines (r17b_prime.md 2537, 2593-2596, 1.3a, 8.1; b138_chain.sh) |
| Site kind from stamps and/or emitted C | done: stamps from compile-only probes, cross-checked against the store (1,309/1,318) |
| Landings from the actual byte set as emitted | done (tables from the emitted C; cross-checked with `--emit-facts` start_set 416/419) |
| Mean gap, dominant gap, share | done for every cell (`cells.tsv`, `qualifying.tsv`) |
| Report cells with mean gap <= 8 and one dominant gap | done (section 2, `qualifying.tsv`, appendix A) |
| Near-miss table (mean <= 16) | done (section 3, appendices B and C, `nearmiss.tsv`) |
| Per cell: id, site kind, subject and length, mean, dominant, share | in `qualifying.tsv` (grouped views inline) |
| Counters: say plainly | done: none taken; perf works at user level (section 4) |
| No direction stated or hinted for any cell | done |
| Every simplification stated | done (section 4, nine items) |
| Probe script kept with a source header | done: all `.py` files in the lane dir carry one |
| Report file at /var/tmp/pcrecbench/b139gaps/report.md | done |
| Draft outbox paragraph | done (section 5) |
| No pcrec writes, no build, no timing, no worktree | done; only /var/tmp/pcrecbench/b139gaps/ written (a scratch copy of the pcrec doc at /var/tmp/r17.md was made and removed) |

OWED: nothing. Optional follow-up (manager's call): `branch-misses:u` per landing on the qualifying cells; a walk simulation for the DFA sites.


## Appendix A. Qualifying groups (mean gap <= 8, share > 0.5, >= 16 landings)

| set | pattern | cfg | site | cover/|S| | subjects (regime cells) | len B | landings | mean gap | dominant gap (cells) | share |
|---|---|---|---|---|---|---|---|---|---|---|
| altwide@0.3 | ci-256 | auto,nocaps | dfa-byte-class | 2/52 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.29) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | ci-256 | vm | vm-hat-first-class | 2/52 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.29) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | ci-512 | auto,nocaps | dfa-byte-class | 2/52 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.29) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | clsa-256 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | clsa-256 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | clsa-64 | auto,nocaps | dfa-byte-class | 2/24 | 27 (ss 46,tp 8) | 18-524288 | 17-377114 | 1.06-1.60 (med 1.40) | 1 x54 | 0.71-0.94 |
| altwide@0.3 | clsa-64 | vm | vm-hat-first-class | 2/24 | 27 (ss 23,tp 4) | 18-524288 | 17-377114 | 1.06-1.60 (med 1.40) | 1 x27 | 0.71-0.94 |
| altwide@0.3 | clsd-256 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | clsd-256 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | clsd-64 | auto,nocaps | dfa-byte-class | 2/24 | 27 (ss 46,tp 8) | 18-524288 | 17-377114 | 1.06-1.60 (med 1.40) | 1 x54 | 0.71-0.94 |
| altwide@0.3 | clsd-64 | vm | vm-hat-first-class | 2/24 | 27 (ss 23,tp 4) | 18-524288 | 17-377114 | 1.06-1.60 (med 1.40) | 1 x27 | 0.71-0.94 |
| altwide@0.3 | cnt-64 | auto,nocaps | dfa-byte-class | 2/24 | 27 (ss 46,tp 8) | 18-524288 | 17-377114 | 1.06-1.60 (med 1.40) | 1 x54 | 0.71-0.94 |
| altwide@0.3 | cnt-64 | vm | vm-hat-first-class | 2/24 | 27 (ss 23,tp 4) | 18-524288 | 17-377114 | 1.06-1.60 (med 1.40) | 1 x27 | 0.71-0.94 |
| altwide@0.3 | s-2048 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | s-256 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | s-256 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | s-512 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | s-512 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | sfx-256 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | sfx-512 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | sfx-64 | vm | vm-hat-first-class | 2/25 | 28 (ss 24,tp 4) | 16-524288 | 16-392796 | 1.00-1.51 (med 1.35) | 1 x28 | 0.78-1.00 |
| altwide@0.3 | srt-256 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | srt-256 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | srt-512 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | srt-512 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | w-1024 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | w-128 | auto,nocaps | dfa-byte-class | 2/25 | 28 (ss 48,tp 8) | 16-524288 | 16-393078 | 1.00-1.53 (med 1.35) | 1 x56 | 0.77-1.00 |
| altwide@0.3 | w-128 | vm | vm-hat-first-class | 2/25 | 28 (ss 24,tp 4) | 16-524288 | 16-393078 | 1.00-1.53 (med 1.35) | 1 x28 | 0.77-1.00 |
| altwide@0.3 | w-192 | auto,nocaps | dfa-byte-class | 2/25 | 28 (ss 48,tp 8) | 16-524288 | 16-393078 | 1.00-1.53 (med 1.35) | 1 x56 | 0.77-1.00 |
| altwide@0.3 | w-192 | vm | vm-hat-first-class | 2/25 | 28 (ss 24,tp 4) | 16-524288 | 16-393078 | 1.00-1.53 (med 1.35) | 1 x28 | 0.77-1.00 |
| altwide@0.3 | w-256 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | w-256 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | w-384 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | w-384 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | w-512 | auto,nocaps | dfa-byte-class | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | w-512 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | w-64 | auto,nocaps | dfa-byte-class | 2/24 | 27 (ss 46,tp 8) | 18-524288 | 17-377114 | 1.06-1.60 (med 1.40) | 1 x54 | 0.71-0.94 |
| altwide@0.3 | w-64 | vm | vm-hat-first-class | 2/24 | 27 (ss 23,tp 4) | 18-524288 | 17-377114 | 1.06-1.60 (med 1.40) | 1 x27 | 0.71-0.94 |
| altwide@0.3 | w-96 | auto,nocaps | dfa-byte-class | 2/25 | 28 (ss 48,tp 8) | 16-524288 | 16-393078 | 1.00-1.53 (med 1.35) | 1 x56 | 0.77-1.00 |
| altwide@0.3 | w-96 | vm | vm-hat-first-class | 2/25 | 28 (ss 24,tp 4) | 16-524288 | 16-393078 | 1.00-1.53 (med 1.35) | 1 x28 | 0.77-1.00 |
| altwide@0.3 | wb-256 | auto,nocaps | dfa-first-class-bounded | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | wb-256 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| altwide@0.3 | wb-512 | auto,nocaps | dfa-first-class-bounded | 1/26 | 28 (ss 48,tp 8) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x56 | 0.81-1.00 |
| altwide@0.3 | wb-512 | vm | vm-hat-first-class | 1/26 | 28 (ss 24,tp 4) | 16-524288 | 16-408549 | 1.00-1.47 (med 1.30) | 1 x28 | 0.81-1.00 |
| bounded@0.3 | cls-atleast-4096 | auto,nocaps | dfa-byte-class | 1/26 | 22 (ss 38,tp 6) | 16-65536 | 16-65536 | 1.00-2.48 (med 1.03) | 1 x44 | 0.60-1.00 |
| bounded@0.3 | cls-atleast-4096 | vm | vm-hat-first-class | 1/26 | 22 (ss 19,tp 3) | 16-65536 | 16-65536 | 1.00-2.48 (med 1.03) | 1 x22 | 0.60-1.00 |
| bounded@0.3 | csv5 | vm | vm-hat-first-class | 2/255 | 35 (ss 30,tp 5) | 16-65536 | 16-65536 | 1.00-1.00 (med 1.00) | 1 x35 | 1.00-1.00 |
| bounded@0.3 | dig-exact-16 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | dig-exact-16 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | dig-exact-2 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | dig-exact-2 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | dig-exact-32 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | dig-exact-32 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | dig-exact-8 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | dig-exact-8 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | dig-upto-16 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | dig-upto-16 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | dig-upto-2 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | dig-upto-2 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | dig-upto-32 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | dig-upto-32 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | dig-upto-4 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | dig-upto-4 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | dig-upto-8 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | dig-upto-8 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | dotted4 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | hex32 | auto,nocaps | dfa-byte-class | 2/16 | 17 (ss 30,tp 4) | 16-16384 | 16-16384 | 1.00-2.35 (med 1.00) | 1 x34 | 0.52-1.00 |
| bounded@0.3 | hex32 | vm | vm-hat-first-class | 2/16 | 17 (ss 15,tp 2) | 16-16384 | 16-16384 | 1.00-2.35 (med 1.00) | 1 x17 | 0.52-1.00 |
| bounded@0.3 | line-80 | auto,nocaps | dfa-byte-class | 2/255 | 35 (ss 60,tp 10) | 16-65536 | 16-65536 | 1.00-1.00 (med 1.00) | 1 x70 | 1.00-1.00 |
| bounded@0.3 | line-80 | vm | vm-hat-first-class | 2/255 | 35 (ss 30,tp 5) | 16-65536 | 16-65536 | 1.00-1.00 (med 1.00) | 1 x35 | 1.00-1.00 |
| bounded@0.3 | nest2-4 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | nest2-4 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | nest2-64 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | nest2-64 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | nest2-letters-6 | auto,nocaps | dfa-byte-class | 1/26 | 22 (ss 38,tp 6) | 16-65536 | 16-65536 | 1.00-2.48 (med 1.03) | 1 x44 | 0.60-1.00 |
| bounded@0.3 | nest2-letters-6 | vm | vm-hat-first-class | 1/26 | 22 (ss 19,tp 3) | 16-65536 | 16-65536 | 1.00-2.48 (med 1.03) | 1 x22 | 0.60-1.00 |
| bounded@0.3 | nest3-16 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | nest3-16 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | nest3-3 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | nest3-3 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| bounded@0.3 | pw-8-64 | auto,nocaps | dfa-byte-class | 2/255 | 35 (ss 60,tp 10) | 16-65536 | 16-65536 | 1.00-1.00 (med 1.00) | 1 x70 | 1.00-1.00 |
| bounded@0.3 | pw-8-64 | vm | vm-hat-first-class | 2/255 | 35 (ss 30,tp 5) | 16-65536 | 16-65536 | 1.00-1.00 (med 1.00) | 1 x35 | 1.00-1.00 |
| bounded@0.3 | year4 | auto,nocaps | dfa-byte-class | 1/10 | 16 (ss 28,tp 4) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x32 | 0.54-1.00 |
| bounded@0.3 | year4 | vm | vm-hat-first-class | 1/10 | 16 (ss 14,tp 2) | 16-16384 | 16-16384 | 1.00-4.11 (med 1.00) | 1 x16 | 0.54-1.00 |
| capability@0.2 | currency-lookbehind-fixed | vm | vm-hat-first-class | 1/10 | 5 (ss 4,tp 1) | 20-4096 | 19-1845 | 1.00-2.22 (med 1.60) | 1 x5 | 0.60-1.00 |
| capability@0.2 | doubled-word | auto,nocaps,vm | vm-hat-first-class | 3+/63 | 34 (ss 75,tp 27) | 18-1048576 | 16-870459 | 1.00-1.50 (med 1.16) | 1 x102 | 0.73-1.00 |
| capability@0.2 | dup-param-detect | auto,nocaps,vm | vm-hat-first-class | 3+/63 | 34 (ss 75,tp 27) | 18-1048576 | 16-870459 | 1.00-1.50 (med 1.16) | 1 x102 | 0.73-1.00 |
| capability@0.2 | float-literal-bound | auto,nocaps | dfa-first-class-bounded | 1/10 | 5 (ss 8,tp 2) | 20-4096 | 19-1845 | 1.00-2.22 (med 1.60) | 1 x10 | 0.60-1.00 |
| capability@0.2 | float-literal-bound | vm | vm-hat-first-class | 1/10 | 5 (ss 4,tp 1) | 20-4096 | 19-1845 | 1.00-2.22 (med 1.60) | 1 x5 | 0.60-1.00 |
| capability@0.2 | hex8-bounded | auto,nocaps | dfa-first-class-bounded | 2/16 | 10 (ss 18,tp 2) | 18-4096 | 17-2701 | 1.00-2.07 (med 1.06) | 1 x20 | 0.78-1.00 |
| capability@0.2 | hex8-bounded | vm | vm-hat-first-class | 2/16 | 10 (ss 9,tp 1) | 18-4096 | 17-2701 | 1.00-2.07 (med 1.06) | 1 x10 | 0.78-1.00 |
| capability@0.2 | phone-palindrome-6 | auto,nocaps,vm | vm-hat-first-class | 1/10 | 5 (ss 12,tp 3) | 20-4096 | 19-1845 | 1.00-2.22 (med 1.60) | 1 x15 | 0.60-1.00 |
| capability@0.2 | tail-digits-eol | vm | vm-hat-first-class | 1/10 | 5 (ss 4,tp 1) | 20-4096 | 19-1845 | 1.00-2.22 (med 1.60) | 1 x5 | 0.60-1.00 |
| capability@0.2 | tail-dotstar-txt | vm | vm-hat-first-class | 2/255 | 43 (ss 32,tp 11) | 16-1048576 | 16-1031596 | 1.00-1.11 (med 1.00) | 1 x43 | 0.90-1.00 |
| capability@0.2 | tail-ext-lower-txt | vm | vm-hat-first-class | 1/26 | 27 (ss 18,tp 9) | 18-1048576 | 17-756399 | 1.00-2.37 (med 1.25) | 1 x27 | 0.65-1.00 |
| capability@0.2 | tail-space-eol | vm | vm-hat-first-class | 2/6 | 3 (ss 1,tp 2) | 20-61440 | 19-61440 | 1.00-1.00 (med 1.00) | 1 x3 | 1.00-1.00 |
| capability@0.2 | tail-word-eoz | vm | vm-hat-first-class | 3+/63 | 34 (ss 25,tp 9) | 18-1048576 | 16-870459 | 1.00-1.50 (med 1.16) | 1 x34 | 0.73-1.00 |
| capability@0.2 | wild-codegrammar-json-number-extended | auto,nocaps | dfa-byte-class | 1/10 | 5 (ss 8,tp 2) | 20-4096 | 19-1845 | 1.00-2.22 (med 1.60) | 1 x10 | 0.60-1.00 |
| capability@0.2 | wild-codegrammar-json-number-extended | vm | vm-hat-first-class | 2/11 | 7 (ss 5,tp 2) | 20-1048576 | 16-133434 | 1.00-7.86 (med 1.33) | 1 x7 | 0.57-1.00 |
| capability@0.2 | wild-datetime-datefinder-alternation | nocaps | dfa-byte-class | 3+/38 | 31 (ss 20,tp 11) | 18-1048576 | 17-809318 | 1.00-1.91 (med 1.30) | 1 x31 | 0.53-1.00 |
| capability@0.2 | wild-logparse-base10num-grok | auto,nocaps | vm-byte-class-bounded | 3+/13 | 9 (ss 10,tp 8) | 20-1048576 | 16-151346 | 1.00-7.37 (med 2.00) | 1 x18 | 0.58-1.00 |
| capability@0.2 | wild-logparse-base10num-grok | vm | vm-hat-first-class | 3+/13 | 9 (ss 5,tp 4) | 20-1048576 | 16-151346 | 1.00-7.37 (med 2.00) | 1 x9 | 0.58-1.00 |
| capability@0.2 | wild-logparse-base10num-noatomic | auto,nocaps | dfa-byte-class-bounded | 3+/13 | 9 (ss 10,tp 8) | 20-1048576 | 16-151346 | 1.00-7.37 (med 2.00) | 1 x18 | 0.58-1.00 |
| capability@0.2 | wild-logparse-base10num-noatomic | vm | vm-hat-first-class | 3+/13 | 9 (ss 5,tp 4) | 20-1048576 | 16-151346 | 1.00-7.37 (med 2.00) | 1 x9 | 0.58-1.00 |
| capability@0.2 | wild-logparse-syslogbase-expanded | auto,nocaps | vm-first-class-bounded | 3+/16 | 5 (ss 10) | 18-93 | 17-83 | 1.00-1.02 (med 1.00) | 1 x10 | 0.99-1.00 |
| capability@0.2 | wild-logparse-syslogbase-expanded | vm | vm-hat-first-class | 3+/16 | 5 (ss 5) | 18-93 | 17-83 | 1.00-1.02 (med 1.00) | 1 x5 | 0.99-1.00 |
| capability@0.2 | wild-logparse-winpath-grok | auto,nocaps | vm-byte-class | 3+/53 | 30 (ss 42,tp 18) | 18-1048576 | 17-771215 | 1.00-2.37 (med 1.19) | 1 x60 | 0.65-1.00 |
| capability@0.2 | wild-logparse-winpath-grok | vm | vm-hat-first-class | 3+/53 | 30 (ss 21,tp 9) | 18-1048576 | 17-771215 | 1.00-2.37 (med 1.19) | 1 x30 | 0.65-1.00 |
| capability@0.2 | wild-secrets-aws-access-key-id | vm | vm-hat-first-class | 1/1 B5 | 1 (ss 1) | 93-93 | 41-41 | 1.00-1.00 (med 1.00) | 1 x1 | 1.00-1.00 |
| capability@0.2 | wild-semdiv-dollar-trailing-newline-pcre2 | vm | vm-hat-first-class | 1/1 B5 | 5 (ss 5) | 18-93 | 17-60 | 1.00-2.05 (med 1.00) | 1 x5 | 0.98-1.00 |
| capability@0.2 | wild-semdiv-empty-alt-repeat-pcre2 | nocaps | dfa-byte-class | 1/10 | 5 (ss 4,tp 1) | 20-4096 | 19-1845 | 1.00-2.22 (med 1.60) | 1 x5 | 0.60-1.00 |
| capability@0.2 | wild-semdiv-empty-alt-repeat-pcre2 | auto | vm-byte-class | 1/10 | 5 (ss 4,tp 1) | 20-4096 | 19-1845 | 1.00-2.22 (med 1.60) | 1 x5 | 0.60-1.00 |
| capability@0.2 | wild-semdiv-empty-alt-repeat-pcre2 | vm | vm-hat-first-class | 2/11 | 14 (ss 10,tp 4) | 18-1048527 | 16-149337 | 1.00-7.02 (med 1.72) | 1 x14 | 0.53-1.00 |
| capability@0.2 | wild-validator-uuid-grok | vm | vm-hat-first-class | 3+/22 | 11 (ss 10,tp 1) | 18-4096 | 17-2701 | 1.00-2.35 (med 1.05) | 1 x11 | 0.52-1.00 |
| email@0.2 | factored | auto,nocaps | dfa-byte-class | 3+/56 | 21 (ss 32,tp 10) | 19-1048576 | 16-1048576 | 1.00-1.47 (med 1.18) | 1 x42 | 0.53-1.00 |
| email@0.2 | orig | auto,nocaps | dfa-byte-class | 3+/56 | 21 (ss 32,tp 10) | 19-1048576 | 16-1048576 | 1.00-1.47 (med 1.18) | 1 x42 | 0.53-1.00 |
| email@0.2 | orig | vm | vm-hat-first-class | 3+/56 | 21 (ss 16,tp 5) | 19-1048576 | 16-1048576 | 1.00-1.47 (med 1.18) | 1 x21 | 0.53-1.00 |
| litrun@0.1 | alt-foo-tails | vm | vm-hat-first-class | 1/1 B5 | 6 (tp 6) | 65534-65536 | 8192-9362 | 7.00-8.00 (med 7.50) | 7 x3, 8 x3 | 1.00-1.00 |
| litrun@0.1 | ctrl-abc-dollar | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | floor | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l10 | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l16 | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l2 | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l3 | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l31 | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l4 | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l40 | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l7 | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l8 | vm | vm-hat-first-class | 1/1 B5 | 10 (tp 10) | 65534-65536 | 8192-32768 | 2.00-8.00 (med 4.00) | 2 x2, 3 x2, 4 x2 | 1.00-1.00 |
| litrun@0.1 | wild-secrets-github-pat | vm | vm-hat-first-class | 1/1 B5 | 5 (tp 5) | 65534-65536 | 8192-9362 | 7.00-8.00 (med 8.00) | 8 x3, 7 x2 | 1.00-1.00 |
| loglines@0.1 | bignum | auto,nocaps | dfa-first-class-bounded | 1/10 | 122 (ss 220,tp 24) | 279-1048651 | 76-281681 | 2.66-4.87 (med 3.72) | 1 x244 | 0.52-0.68 |
| loglines@0.1 | bignum | vm | vm-hat-first-class | 1/10 | 122 (ss 110,tp 12) | 279-1048651 | 76-281681 | 2.66-4.87 (med 3.72) | 1 x122 | 0.52-0.68 |
| loglines@0.1 | hex32-id | auto,nocaps | dfa-first-class-bounded | 2/16 | 85 (ss 154,tp 16) | 279-1048621 | 133-467549 | 1.99-2.38 (med 2.21) | 1 x170 | 0.50-0.63 |
| loglines@0.1 | hex32-id | vm | vm-hat-first-class | 2/16 | 85 (ss 77,tp 8) | 279-1048621 | 133-467549 | 1.99-2.38 (med 2.21) | 1 x85 | 0.50-0.63 |
| loglines@0.1 | ipv4 | vm | vm-hat-first-class | 1/10 | 122 (ss 110,tp 12) | 279-1048651 | 76-281681 | 2.66-4.87 (med 3.72) | 1 x122 | 0.52-0.68 |
| loglines@0.1 | ipv6 | vm | vm-hat-first-class | 2/16 | 85 (ss 77,tp 8) | 279-1048621 | 133-467549 | 1.99-2.38 (med 2.21) | 1 x85 | 0.50-0.63 |
| loglines@0.1 | iso-ts | vm | vm-hat-first-class | 1/10 | 122 (ss 110,tp 12) | 279-1048651 | 76-281681 | 2.66-4.87 (med 3.72) | 1 x122 | 0.52-0.68 |
| loglines@0.1 | kv-quoted | vm | vm-hat-first-class | 2/27 | 124 (ss 112,tp 12) | 279-1048651 | 100-507161 | 1.29-2.70 (med 2.11) | 1 x124 | 0.72-0.82 |
| loglines@0.1 | uuid | vm | vm-hat-first-class | 2/16 | 85 (ss 77,tp 8) | 279-1048621 | 133-467549 | 1.99-2.38 (med 2.21) | 1 x85 | 0.50-0.63 |
| syntax@0.1 | bak-1 | auto,nocaps,vm | vm-hat-first-class | 3+/63 | 14 (ss 33,tp 9) | 23-1048576 | 18-797953 | 1.08-1.64 (med 1.31) | 1 x42 | 0.64-0.92 |
| syntax@0.1 | bak-2 | auto,nocaps,vm | vm-hat-first-class | 3+/63 | 14 (ss 33,tp 9) | 23-1048576 | 18-797953 | 1.08-1.64 (med 1.31) | 1 x42 | 0.64-0.92 |
| syntax@0.1 | bak-g-rel | auto,nocaps,vm | vm-hat-first-class | 3+/63 | 14 (ss 33,tp 9) | 23-1048576 | 18-797953 | 1.08-1.64 (med 1.31) | 1 x42 | 0.64-0.92 |
| syntax@0.1 | bak-py | auto,nocaps,vm | vm-hat-first-class | 3+/63 | 14 (ss 33,tp 9) | 23-1048576 | 18-797953 | 1.08-1.64 (med 1.31) | 1 x42 | 0.64-0.92 |
| syntax@0.1 | cls-d | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x2 | 0.52-0.52 |
| syntax@0.1 | cls-d | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | cls-posix | auto,nocaps | dfa-byte-class | 2/52 | 14 (ss 22,tp 6) | 23-1048576 | 18-727766 | 1.08-1.93 (med 1.39) | 1 x28 | 0.64-0.92 |
| syntax@0.1 | cls-posix | vm | vm-hat-first-class | 2/52 | 14 (ss 11,tp 3) | 23-1048576 | 18-727766 | 1.08-1.93 (med 1.39) | 1 x14 | 0.64-0.92 |
| syntax@0.1 | cls-s-uc | auto,nocaps | dfa-byte-class | 3+/250 | 15 (ss 24,tp 6) | 23-1048576 | 18-871233 | 1.08-1.35 (med 1.21) | 1 x30 | 0.69-0.92 |
| syntax@0.1 | cls-s-uc | vm | vm-hat-first-class | 3+/250 | 15 (ss 12,tp 3) | 23-1048576 | 18-871233 | 1.08-1.35 (med 1.21) | 1 x15 | 0.69-0.92 |
| syntax@0.1 | cls-w | auto,nocaps | dfa-byte-class | 3+/63 | 14 (ss 22,tp 6) | 23-1048576 | 18-797953 | 1.08-1.64 (med 1.31) | 1 x28 | 0.64-0.92 |
| syntax@0.1 | cls-w | vm | vm-hat-first-class | 3+/63 | 14 (ss 11,tp 3) | 23-1048576 | 18-797953 | 1.08-1.64 (med 1.31) | 1 x14 | 0.64-0.92 |
| syntax@0.1 | grp-atomic-alt | vm | vm-hat-first-class | 1/1 B5 | 1 (ss 1) | 58-58 | 47-47 | 1.17-1.17 (med 1.17) | 1 x1 | 0.91-0.91 |
| syntax@0.1 | grp-atomic-rep | vm | vm-hat-first-class | 1/1 B5 | 1 (ss 1) | 58-58 | 47-47 | 1.17-1.17 (med 1.17) | 1 x1 | 0.91-0.91 |
| syntax@0.1 | grp-noncap | vm | vm-hat-first-class | 1/1 B5 | 1 (ss 1) | 58-58 | 47-47 | 1.17-1.17 (med 1.17) | 1 x1 | 0.91-0.91 |
| syntax@0.1 | mod-a | auto,nocaps | dfa-byte-class | 3+/63 | 14 (ss 22,tp 6) | 23-1048576 | 18-797953 | 1.08-1.64 (med 1.31) | 1 x28 | 0.64-0.92 |
| syntax@0.1 | mod-a | vm | vm-hat-first-class | 3+/63 | 14 (ss 11,tp 3) | 23-1048576 | 18-797953 | 1.08-1.64 (med 1.31) | 1 x14 | 0.64-0.92 |
| syntax@0.1 | mod-j-uc | auto,nocaps,vm | vm-hat-first-class | 3+/63 | 14 (ss 33,tp 9) | 23-1048576 | 18-797953 | 1.08-1.64 (med 1.31) | 1 x42 | 0.64-0.92 |
| syntax@0.1 | qnt-plus | vm | vm-hat-first-class | 1/1 B5 | 1 (ss 1) | 58-58 | 47-47 | 1.17-1.17 (med 1.17) | 1 x1 | 0.91-0.91 |
| syntax@0.1 | qnt-plus-ctl | vm | vm-hat-first-class | 1/1 B5 | 1 (ss 1) | 58-58 | 47-47 | 1.17-1.17 (med 1.17) | 1 x1 | 0.91-0.91 |
| syntax@0.1 | qnt-poss-brace | vm | vm-hat-first-class | 1/1 B5 | 1 (ss 1) | 58-58 | 47-47 | 1.17-1.17 (med 1.17) | 1 x1 | 0.91-0.91 |
| syntax@0.1 | qnt-poss-plus | vm | vm-hat-first-class | 1/1 B5 | 1 (ss 1) | 58-58 | 47-47 | 1.17-1.17 (med 1.17) | 1 x1 | 0.91-0.91 |
| syntax@0.1 | qnt-poss-quest | vm | vm-hat-first-class | 1/1 B5 | 1 (ss 1) | 58-58 | 47-47 | 1.17-1.17 (med 1.17) | 1 x1 | 0.91-0.91 |
| syntax@0.1 | qnt-poss-star | vm | vm-hat-first-class | 1/2 | 1 (ss 1) | 58-58 | 51-51 | 1.08-1.08 (med 1.08) | 1 x1 | 0.92-0.92 |
| syntax@0.1 | rec-back | nocaps | dfa-byte-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-back | auto | vm-byte-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-back | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-fwd | nocaps | dfa-byte-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-fwd | auto | vm-byte-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-g-angle | nocaps | dfa-byte-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-g-angle | auto | vm-byte-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-g-angle | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-py | nocaps | dfa-byte-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-py | auto | vm-byte-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | rec-py | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 86-86 | 22-22 | 3.76-3.76 (med 3.76) | 1 x1 | 0.52-0.52 |
| syntax@0.1 | unp-p-lc | auto,nocaps | dfa-byte-class | 3+/117 | 14 (ss 22,tp 6) | 23-1048576 | 18-729106 | 1.08-1.93 (med 1.37) | 1 x28 | 0.64-0.92 |
| syntax@0.1 | unp-p-lc | vm | vm-hat-first-class | 3+/117 | 14 (ss 11,tp 3) | 23-1048576 | 18-729106 | 1.08-1.93 (med 1.37) | 1 x14 | 0.64-0.92 |
| syntax@0.1 | unp-p-uc | auto,nocaps | dfa-byte-class | 3+/139 | 3 (ss 6) | 41-86 | 18-43 | 1.32-4.12 (med 1.90) | 1 x4, 4 x2 | 0.65-0.74 |
| syntax@0.1 | unp-p-uc | vm | vm-hat-first-class | 3+/139 | 3 (ss 3) | 41-86 | 18-43 | 1.32-4.12 (med 1.90) | 1 x2, 4 x1 | 0.65-0.74 |
| utf8@0.1 | alt-cyr-64 | auto,nocaps | dfa-byte-class | 1/2 | 4 (tp 8) | 65536-1048576 | 9050-141508 | 2.29-7.41 (med 7.21) | 2 x8 | 0.74-0.75 |
| utf8@0.1 | alt-cyr-64 | vm | vm-hat-first-class | 1/2 | 4 (tp 4) | 65536-1048576 | 9050-141508 | 2.29-7.41 (med 7.21) | 2 x4 | 0.74-0.75 |
| utf8@0.1 | alt-distinct-lead | auto,nocaps | dfa-byte-class | 3+/3 | 1 (tp 2) | 65536-65536 | 20279-20279 | 3.23-3.23 (med 3.23) | 2 x2 | 0.55-0.55 |
| utf8@0.1 | alt-distinct-lead | vm | vm-hat-first-class | 3+/3 | 1 (tp 1) | 65536-65536 | 20279-20279 | 3.23-3.23 (med 3.23) | 2 x1 | 0.55-0.55 |
| utf8@0.1 | asr-b-cyr | vm | vm-hat-first-class | 1/1 B5 | 1 (tp 1) | 65536-65536 | 20279-20279 | 3.23-3.23 (med 3.23) | 2 x1 | 0.55-0.55 |
| utf8@0.1 | ci-class-range | auto,nocaps | dfa-byte-class | 3+/54 | 5 (tp 10) | 65536-1048576 | 24051-388879 | 1.18-2.72 (med 2.70) | 1 x10 | 0.69-0.83 |
| utf8@0.1 | ci-class-range | vm | vm-hat-first-class | 3+/54 | 5 (tp 5) | 65536-1048576 | 24051-388879 | 1.18-2.72 (med 2.70) | 1 x5 | 0.69-0.83 |
| utf8@0.1 | ci-moskva | vm | vm-hat-first-class | 1/1 B5 | 1 (tp 1) | 65536-65536 | 20279-20279 | 3.23-3.23 (med 3.23) | 2 x1 | 0.55-0.55 |
| utf8@0.1 | ci-neg-fold | auto,nocaps | dfa-byte-class | 2/179 | 9 (ss 4,tp 14) | 16-1048576 | 16-743934 | 1.00-2.61 (med 1.41) | 1 x14, 2 x2, 3 x2 | 0.60-1.00 |
| utf8@0.1 | ci-neg-fold | vm | vm-hat-first-class | 2/179 | 9 (ss 2,tp 7) | 16-1048576 | 16-743934 | 1.00-2.61 (med 1.41) | 1 x7, 2 x1, 3 x1 | 0.60-1.00 |
| utf8@0.1 | cls-boundary-range | auto,nocaps | dfa-byte-class | 2/33 | 5 (tp 10) | 65536-1048576 | 24530-398028 | 1.20-2.66 (med 2.63) | 1 x10 | 0.70-0.83 |
| utf8@0.1 | cls-boundary-range | vm | vm-hat-first-class | 2/33 | 5 (tp 5) | 65536-1048576 | 24530-398028 | 1.20-2.66 (med 2.63) | 1 x5 | 0.70-0.83 |
| utf8@0.1 | cls-dot | auto,nocaps | dfa-byte-class | 3+/178 | 8 (ss 2,tp 14) | 16-1048576 | 16-743934 | 1.00-2.61 (med 1.41) | 1 x12, 2 x2, 3 x2 | 0.69-1.00 |
| utf8@0.1 | cls-dot | vm | vm-hat-first-class | 3+/178 | 8 (ss 1,tp 7) | 16-1048576 | 16-743934 | 1.00-2.61 (med 1.41) | 1 x6, 2 x1, 3 x1 | 0.69-1.00 |
| utf8@0.1 | cls-high-range | auto,nocaps | dfa-byte-class | 1/31 | 4 (tp 8) | 65536-1048576 | 9097-142264 | 2.28-7.37 (med 7.18) | 2 x8 | 0.74-0.75 |
| utf8@0.1 | cls-high-range | vm | vm-hat-first-class | 1/31 | 4 (tp 4) | 65536-1048576 | 9097-142264 | 2.28-7.37 (med 7.18) | 2 x4 | 0.74-0.75 |
| utf8@0.1 | cls-mixed | auto,nocaps | dfa-byte-class | 3+/29 | 6 (tp 12) | 65536-1048576 | 28624-536915 | 1.20-2.29 (med 1.95) | 1 x10, 2 x2 | 0.57-0.83 |
| utf8@0.1 | cls-mixed | vm | vm-hat-first-class | 3+/29 | 6 (tp 6) | 65536-1048576 | 28624-536915 | 1.20-2.29 (med 1.95) | 1 x5, 2 x1 | 0.57-0.83 |
| utf8@0.1 | cls-neg-allhigh | auto,nocaps | dfa-byte-class | 1/128 | 6 (ss 2,tp 10) | 16-1048576 | 16-512291 | 1.00-2.06 (med 1.62) | 1 x12 | 0.88-1.00 |
| utf8@0.1 | cls-neg-allhigh | vm | vm-hat-first-class | 1/128 | 6 (ss 1,tp 5) | 16-1048576 | 16-512291 | 1.00-2.06 (med 1.62) | 1 x6 | 0.88-1.00 |
| utf8@0.1 | cls-neg-cjk | auto,nocaps | dfa-byte-class | 3+/174 | 7 (ss 2,tp 12) | 16-1048576 | 16-696689 | 1.00-1.79 (med 1.51) | 1 x12, 2 x2 | 0.73-1.00 |
| utf8@0.1 | cls-neg-cjk | vm | vm-hat-first-class | 3+/174 | 7 (ss 1,tp 6) | 16-1048576 | 16-696689 | 1.00-1.79 (med 1.51) | 1 x6, 2 x1 | 0.73-1.00 |
| utf8@0.1 | cls-neg-single | auto,nocaps | dfa-byte-class | 2/179 | 9 (ss 4,tp 14) | 16-1048576 | 16-743934 | 1.00-2.61 (med 1.41) | 1 x14, 2 x2, 3 x2 | 0.60-1.00 |
| utf8@0.1 | cls-neg-single | vm | vm-hat-first-class | 2/179 | 9 (ss 2,tp 7) | 16-1048576 | 16-743934 | 1.00-2.61 (med 1.41) | 1 x7, 2 x1, 3 x1 | 0.60-1.00 |
| utf8@0.1 | cls-posix-alpha | auto,nocaps | dfa-byte-class | 2/52 | 5 (tp 10) | 65536-1048576 | 24004-388123 | 1.18-2.72 (med 2.70) | 1 x10 | 0.69-0.83 |
| utf8@0.1 | cls-posix-alpha | vm | vm-hat-first-class | 2/52 | 5 (tp 5) | 65536-1048576 | 24004-388123 | 1.18-2.72 (med 2.70) | 1 x5 | 0.69-0.83 |
| utf8@0.1 | cls-w-ascii | auto,nocaps | dfa-byte-class | 3+/63 | 5 (tp 10) | 65536-1048576 | 24118-390637 | 1.18-2.71 (med 2.68) | 1 x10 | 0.69-0.83 |
| utf8@0.1 | cls-w-ascii | vm | vm-hat-first-class | 3+/63 | 5 (tp 5) | 65536-1048576 | 24118-390637 | 1.18-2.71 (med 2.68) | 1 x5 | 0.69-0.83 |
| utf8@0.1 | lit-cyr-run | vm | vm-hat-first-class | 1/1 B5 | 1 (tp 1) | 65536-65536 | 20279-20279 | 3.23-3.23 (med 3.23) | 2 x1 | 0.55-0.55 |
| utf8@0.1 | prp-cyrillic | auto,nocaps | dfa-byte-class | 3+/12 | 4 (tp 8) | 65536-1048576 | 9321-146000 | 2.28-7.18 (med 7.03) | 2 x8 | 0.73-0.75 |
| utf8@0.1 | prp-cyrillic | vm | vm-hat-first-class | 3+/12 | 4 (tp 4) | 65536-1048576 | 9321-146000 | 2.28-7.18 (med 7.03) | 2 x4 | 0.73-0.75 |
| utf8@0.1 | prp-han | auto,nocaps | dfa-byte-class | 3+/12 | 1 (tp 2) | 65536-65536 | 20212-20212 | 3.24-3.24 (med 3.24) | 3 x2 | 0.92-0.92 |
| utf8@0.1 | prp-han | vm | vm-hat-first-class | 3+/12 | 1 (tp 1) | 65536-65536 | 20212-20212 | 3.24-3.24 (med 3.24) | 3 x1 | 0.92-0.92 |
| utf8@0.1 | prp-l | auto,nocaps | dfa-byte-class | 3+/97 | 7 (tp 14) | 65536-1048576 | 23371-619766 | 1.18-2.80 (med 1.70) | 1 x10, 2 x2, 3 x2 | 0.51-0.83 |
| utf8@0.1 | prp-l | vm | vm-hat-first-class | 3+/97 | 7 (tp 7) | 65536-1048576 | 23371-619766 | 1.18-2.80 (med 1.70) | 1 x5, 2 x1, 3 x1 | 0.51-0.83 |
| utf8@0.1 | prp-latin | auto,nocaps | dfa-byte-class | 3+/71 | 5 (tp 10) | 65536-1048576 | 25372-411758 | 1.18-2.58 (med 2.55) | 1 x10 | 0.71-0.83 |
| utf8@0.1 | prp-latin | vm | vm-hat-first-class | 3+/71 | 5 (tp 5) | 65536-1048576 | 25372-411758 | 1.18-2.58 (med 2.55) | 1 x5 | 0.71-0.83 |
| utf8@0.1 | prp-lu | auto,nocaps | dfa-byte-class | 3+/47 | 4 (tp 8) | 65536-1048576 | 10836-171760 | 2.28-6.10 (med 6.03) | 2 x8 | 0.62-0.75 |
| utf8@0.1 | prp-lu | vm | vm-hat-first-class | 3+/47 | 4 (tp 4) | 65536-1048576 | 10836-171760 | 2.28-6.10 (med 6.03) | 2 x4 | 0.62-0.75 |
| utf8@0.1 | qnt-class-run | auto,nocaps | dfa-byte-class | 1/4 | 4 (tp 8) | 65536-1048576 | 9050-141508 | 2.29-7.41 (med 7.21) | 2 x8 | 0.74-0.75 |
| utf8@0.1 | qnt-class-run | vm | vm-hat-first-class | 1/4 | 4 (tp 4) | 65536-1048576 | 9050-141508 | 2.29-7.41 (med 7.21) | 2 x4 | 0.74-0.75 |
| utf8@0.1 | qnt-dot-bounded | auto,nocaps | dfa-byte-class | 3+/178 | 8 (ss 2,tp 14) | 16-1048576 | 16-743934 | 1.00-2.61 (med 1.41) | 1 x12, 2 x2, 3 x2 | 0.69-1.00 |
| utf8@0.1 | qnt-dot-bounded | vm | vm-hat-first-class | 3+/178 | 8 (ss 1,tp 7) | 16-1048576 | 16-743934 | 1.00-2.61 (med 1.41) | 1 x6, 2 x1, 3 x1 | 0.69-1.00 |

## Appendix B. Near-miss groups (8 < mean gap <= 16, >= 16 landings)

| set | pattern | cfg | site | cover/|S| | subjects (regime cells) | len B | landings | mean gap | dominant gap (cells) | share |
|---|---|---|---|---|---|---|---|---|---|---|
| altwide@0.3 | nar4-256 | auto,nocaps | dfa-byte-class | 3+/4 | 21 (ss 34,tp 8) | 219-524288 | 16-62973 | 8.12-12.00 (med 9.09) | 1 x14, 4 x10, 2 x8 | 0.13-0.30 |
| altwide@0.3 | nar4-256 | vm | vm-hat-first-class | 3+/4 | 21 (ss 17,tp 4) | 219-524288 | 16-62973 | 8.12-12.00 (med 9.09) | 1 x7, 4 x5, 2 x4 | 0.13-0.30 |
| altwide@0.3 | nar4-512 | auto,nocaps | dfa-byte-class | 3+/4 | 21 (ss 34,tp 8) | 219-524288 | 16-62973 | 8.12-12.00 (med 9.09) | 1 x14, 4 x10, 2 x8 | 0.13-0.30 |
| altwide@0.3 | nar4-512 | vm | vm-hat-first-class | 3+/4 | 21 (ss 17,tp 4) | 219-524288 | 16-62973 | 8.12-12.00 (med 9.09) | 1 x7, 4 x5, 2 x4 | 0.13-0.30 |
| altwide@0.3 | nar4-64 | auto,nocaps | dfa-byte-class | 3+/4 | 21 (ss 34,tp 8) | 219-524288 | 16-62973 | 8.12-12.00 (med 9.09) | 1 x14, 4 x10, 2 x8 | 0.13-0.30 |
| altwide@0.3 | nar4-64 | vm | vm-hat-first-class | 3+/4 | 21 (ss 17,tp 4) | 219-524288 | 16-62973 | 8.12-12.00 (med 9.09) | 1 x7, 4 x5, 2 x4 | 0.13-0.30 |
| altwide@0.3 | w-8 | auto,nocaps | dfa-byte-class | 3+/6 | 1 (ss 2) | 226-226 | 26-26 | 8.28-8.28 (med 8.28) | 2 x2 | 0.12-0.12 |
| altwide@0.3 | w-8 | vm | vm-hat-first-class | 3+/6 | 1 (ss 1) | 226-226 | 26-26 | 8.28-8.28 (med 8.28) | 2 x1 | 0.12-0.12 |
| bounded@0.3 | ctx-greedy-256 | auto,nocaps | vm-first-class-bounded | 3+/3 | 9 (ss 12,tp 6) | 202-65536 | 17-7780 | 8.24-14.29 (med 9.00) | 1 x12, 8 x2, 2 x2 | 0.11-0.29 |
| bounded@0.3 | ctx-greedy-256 | vm | vm-hat-first-class | 3+/3 | 9 (ss 6,tp 3) | 202-65536 | 17-7780 | 8.24-14.29 (med 9.00) | 1 x6, 8 x1, 2 x1 | 0.11-0.29 |
| bounded@0.3 | ctx-lazy-1024 | auto,nocaps | vm-first-class-bounded | 3+/3 | 9 (ss 12,tp 6) | 202-65536 | 17-7780 | 8.24-14.29 (med 9.00) | 1 x12, 8 x2, 2 x2 | 0.11-0.29 |
| bounded@0.3 | ctx-lazy-1024 | vm | vm-hat-first-class | 3+/3 | 9 (ss 6,tp 3) | 202-65536 | 17-7780 | 8.24-14.29 (med 9.00) | 1 x6, 8 x1, 2 x1 | 0.11-0.29 |
| bounded@0.3 | ctx-lazy-256 | auto,nocaps | vm-first-class-bounded | 3+/3 | 9 (ss 12,tp 6) | 202-65536 | 17-7780 | 8.24-14.29 (med 9.00) | 1 x12, 8 x2, 2 x2 | 0.11-0.29 |
| bounded@0.3 | ctx-lazy-256 | vm | vm-hat-first-class | 3+/3 | 9 (ss 6,tp 3) | 202-65536 | 17-7780 | 8.24-14.29 (med 9.00) | 1 x6, 8 x1, 2 x1 | 0.11-0.29 |
| bounded@0.3 | ctx-lazy-64 | auto,nocaps | vm-first-class-bounded | 3+/3 | 9 (ss 12,tp 6) | 202-65536 | 17-7780 | 8.24-14.29 (med 9.00) | 1 x12, 8 x2, 2 x2 | 0.11-0.29 |
| bounded@0.3 | ctx-lazy-64 | vm | vm-hat-first-class | 3+/3 | 9 (ss 6,tp 3) | 202-65536 | 17-7780 | 8.24-14.29 (med 9.00) | 1 x6, 8 x1, 2 x1 | 0.11-0.29 |
| capability@0.2 | currency-lookbehind-fixed | vm | vm-hat-first-class | 1/10 | 6 (tp 6) | 65536-1048576 | 7617-130462 | 8.04-10.56 (med 9.58) | 1 x6 | 0.58-0.79 |
| capability@0.2 | float-literal-bound | auto,nocaps | dfa-first-class-bounded | 1/10 | 6 (tp 12) | 65536-1048576 | 7617-130462 | 8.04-10.56 (med 9.58) | 1 x12 | 0.58-0.79 |
| capability@0.2 | float-literal-bound | vm | vm-hat-first-class | 1/10 | 6 (tp 6) | 65536-1048576 | 7617-130462 | 8.04-10.56 (med 9.58) | 1 x6 | 0.58-0.79 |
| capability@0.2 | phone-palindrome-6 | auto,nocaps,vm | vm-hat-first-class | 1/10 | 6 (tp 18) | 65536-1048576 | 7617-130462 | 8.04-10.56 (med 9.58) | 1 x18 | 0.58-0.79 |
| capability@0.2 | tail-digits-eol | vm | vm-hat-first-class | 1/10 | 6 (tp 6) | 65536-1048576 | 7617-130462 | 8.04-10.56 (med 9.58) | 1 x6 | 0.58-0.79 |
| capability@0.2 | tail-space-eol | vm | vm-hat-first-class | 2/6 | 1 (tp 1) | 4096-4096 | 267-267 | 15.30-15.30 (med 15.30) | 9 x1 | 0.49-0.49 |
| capability@0.2 | wild-codegrammar-json-constant | auto,nocaps | dfa-first-class-bounded | 2/3 | 8 (tp 16) | 16385-1048576 | 1859-105498 | 8.78-12.68 (med 9.94) | 1 x16 | 0.11-0.16 |
| capability@0.2 | wild-codegrammar-json-constant | vm | vm-hat-first-class | 2/3 | 8 (tp 8) | 16385-1048576 | 1859-105498 | 8.78-12.68 (med 9.94) | 1 x8 | 0.11-0.16 |
| capability@0.2 | wild-codegrammar-json-number-extended | auto,nocaps | dfa-byte-class | 1/10 | 6 (tp 12) | 65536-1048576 | 7617-130462 | 8.04-10.56 (med 9.58) | 1 x12 | 0.58-0.79 |
| capability@0.2 | wild-codegrammar-json-number-extended | vm | vm-hat-first-class | 2/11 | 5 (tp 5) | 65536-1048527 | 7806-99252 | 8.04-10.56 (med 10.56) | 1 x5 | 0.57-0.79 |
| capability@0.2 | wild-logparse-base10num-grok | auto,nocaps | vm-byte-class-bounded | 3+/13 | 3 (tp 6) | 1048522-1048527 | 116575-116583 | 8.99-8.99 (med 8.99) | 1 x6 | 0.69-0.69 |
| capability@0.2 | wild-logparse-base10num-grok | vm | vm-hat-first-class | 3+/13 | 3 (tp 3) | 1048522-1048527 | 116575-116583 | 8.99-8.99 (med 8.99) | 1 x3 | 0.69-0.69 |
| capability@0.2 | wild-logparse-base10num-noatomic | auto,nocaps | dfa-byte-class-bounded | 3+/13 | 3 (tp 6) | 1048522-1048527 | 116575-116583 | 8.99-8.99 (med 8.99) | 1 x6 | 0.69-0.69 |
| capability@0.2 | wild-logparse-base10num-noatomic | vm | vm-hat-first-class | 3+/13 | 3 (tp 3) | 1048522-1048527 | 116575-116583 | 8.99-8.99 (med 8.99) | 1 x3 | 0.69-0.69 |
| capability@0.2 | wild-semdiv-empty-alt-repeat-pcre2 | nocaps | dfa-byte-class | 1/10 | 6 (tp 6) | 65536-1048576 | 7617-130462 | 8.04-10.56 (med 9.58) | 1 x6 | 0.58-0.79 |
| capability@0.2 | wild-semdiv-empty-alt-repeat-pcre2 | auto | vm-byte-class | 1/10 | 6 (tp 6) | 65536-1048576 | 7617-130462 | 8.04-10.56 (med 9.58) | 1 x6 | 0.58-0.79 |
| capability@0.2 | wild-waf-crs-942140-dbnames | auto,nocaps | dfa-first-class-bounded | 3+/14 | 1 (tp 2) | 4096-4096 | 392-392 | 10.40-10.40 (med 10.40) | 1 x2 | 0.15-0.15 |
| capability@0.2 | wild-waf-crs-942140-dbnames | vm | vm-hat-first-class | 3+/14 | 1 (tp 1) | 4096-4096 | 392-392 | 10.40-10.40 (med 10.40) | 1 x1 | 0.15-0.15 |
| capability@0.2 | wild-waf-crs-942160-sleep-benchmark | auto,nocaps | dfa-byte-class | 2/4 | 5 (tp 10) | 16385-1048527 | 1311-67914 | 12.48-15.44 (med 15.44) | 5 x6, 1 x4 | 0.08-0.11 |
| capability@0.2 | wild-waf-crs-942160-sleep-benchmark | vm | vm-hat-first-class | 2/4 | 5 (tp 5) | 16385-1048527 | 1311-67914 | 12.48-15.44 (med 15.44) | 5 x3, 1 x2 | 0.08-0.11 |
| litrun@0.1 | alt-foo-tails | vm | vm-hat-first-class | 1/1 B5 | 6 (tp 6) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x3, 16 x3 | 1.00-1.00 |
| litrun@0.1 | ctrl-abc-dollar | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | floor | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l10 | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l16 | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l2 | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l3 | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l31 | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l4 | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l40 | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l7 | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | lit-l8 | vm | vm-hat-first-class | 1/1 B5 | 4 (tp 4) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x2, 16 x2 | 1.00-1.00 |
| litrun@0.1 | wild-secrets-github-pat | vm | vm-hat-first-class | 1/1 B5 | 6 (tp 6) | 65530-65536 | 4096-6553 | 10.00-16.00 (med 13.00) | 10 x3, 16 x3 | 1.00-1.00 |
| loglines@0.1 | stack-frame | vm | vm-hat-first-class | 1/1 B5 | 2 (ss 2) | 358-361 | 21-27 | 12.85-15.85 (med 14.35) | 2 x1, 8 x1 | 0.15-0.25 |
| syntax@0.1 | alt-nested | auto,nocaps | dfa-byte-class | 1/2 | 3 (tp 6) | 65536-1048576 | 4590-73180 | 14.28-14.41 (med 14.33) | 3 x6 | 0.08-0.09 |
| syntax@0.1 | alt-nested | vm | vm-hat-first-class | 1/2 | 3 (tp 3) | 65536-1048576 | 4590-73180 | 14.28-14.41 (med 14.33) | 3 x3 | 0.08-0.09 |
| syntax@0.1 | alt-two | auto,nocaps | dfa-byte-class | 1/2 | 3 (tp 6) | 65536-1048576 | 4590-73180 | 14.28-14.41 (med 14.33) | 3 x6 | 0.08-0.09 |
| syntax@0.1 | alt-two | vm | vm-hat-first-class | 1/2 | 3 (tp 3) | 65536-1048576 | 4590-73180 | 14.28-14.41 (med 14.33) | 3 x3 | 0.08-0.09 |
| syntax@0.1 | cls-d | auto,nocaps | dfa-byte-class | 1/10 | 3 (tp 6) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x6 | 0.57-0.57 |
| syntax@0.1 | cls-d | vm | vm-hat-first-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | grp-atomic-alt | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 4523-73054 | 14.27-14.49 (med 14.35) | 5 x3 | 0.11-0.11 |
| syntax@0.1 | grp-atomic-rep | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 4523-73054 | 14.27-14.49 (med 14.35) | 5 x3 | 0.11-0.11 |
| syntax@0.1 | grp-noncap | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 4523-73054 | 14.27-14.49 (med 14.35) | 5 x3 | 0.11-0.11 |
| syntax@0.1 | qnt-plus | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 4523-73054 | 14.27-14.49 (med 14.35) | 5 x3 | 0.11-0.11 |
| syntax@0.1 | qnt-plus-ctl | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 4523-73054 | 14.27-14.49 (med 14.35) | 5 x3 | 0.11-0.11 |
| syntax@0.1 | qnt-poss-brace | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 4523-73054 | 14.27-14.49 (med 14.35) | 5 x3 | 0.11-0.11 |
| syntax@0.1 | qnt-poss-plus | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 4523-73054 | 14.27-14.49 (med 14.35) | 5 x3 | 0.11-0.11 |
| syntax@0.1 | qnt-poss-quest | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 4523-73054 | 14.27-14.49 (med 14.35) | 5 x3 | 0.11-0.11 |
| syntax@0.1 | qnt-poss-star | vm | vm-hat-first-class | 1/2 | 3 (tp 3) | 65536-1048576 | 5017-81399 | 12.81-13.06 (med 12.88) | 5 x3 | 0.12-0.12 |
| syntax@0.1 | rec-back | nocaps | dfa-byte-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-back | auto | vm-byte-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-back | vm | vm-hat-first-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-fwd | nocaps | dfa-byte-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-fwd | auto | vm-byte-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-g-angle | nocaps | dfa-byte-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-g-angle | auto | vm-byte-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-g-angle | vm | vm-hat-first-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-py | nocaps | dfa-byte-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-py | auto | vm-byte-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| syntax@0.1 | rec-py | vm | vm-hat-first-class | 1/10 | 3 (tp 3) | 65536-1048576 | 4519-70187 | 14.38-14.93 (med 14.69) | 1 x3 | 0.57-0.57 |
| utf8@0.1 | alt-distinct-lead | auto,nocaps | dfa-byte-class | 3+/3 | 3 (tp 6) | 65536-1048576 | 8130-128224 | 8.06-8.18 (med 8.10) | 2 x6 | 0.43-0.44 |
| utf8@0.1 | alt-distinct-lead | vm | vm-hat-first-class | 3+/3 | 3 (tp 3) | 65536-1048576 | 8130-128224 | 8.06-8.18 (med 8.10) | 2 x3 | 0.43-0.44 |
| utf8@0.1 | alt-mixed-width | auto,nocaps | dfa-byte-class | 3+/4 | 2 (tp 4) | 65536-65536 | 4103-7546 | 8.68-15.97 (med 12.33) | 3 x2, 5 x2 | 0.07-0.13 |
| utf8@0.1 | alt-mixed-width | vm | vm-hat-first-class | 3+/4 | 2 (tp 2) | 65536-65536 | 4103-7546 | 8.68-15.97 (med 12.33) | 3 x1, 5 x1 | 0.07-0.13 |
| utf8@0.1 | asr-b-cyr | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 6406-100202 | 10.16-10.46 (med 10.24) | 2 x3 | 0.55-0.56 |
| utf8@0.1 | asr-lb-class | auto,nocaps | vm-byte-class | 2/6 | 4 (tp 8) | 65536-1048576 | 7138-113807 | 9.08-9.21 (med 9.18) | 7 x8 | 0.17-0.22 |
| utf8@0.1 | asr-lb-class | vm | vm-hat-first-class | 2/6 | 4 (tp 4) | 65536-1048576 | 7138-113807 | 9.08-9.21 (med 9.18) | 7 x4 | 0.17-0.22 |
| utf8@0.1 | ci-ascii-control | vm | vm-hat-first-class | 1/2 | 1 (tp 1) | 65536-65536 | 4168-4168 | 15.72-15.72 (med 15.72) | 5 x1 | 0.07-0.07 |
| utf8@0.1 | ci-e-acute | vm | vm-hat-first-class | 1/1 B5 | 1 (tp 1) | 65536-65536 | 4652-4652 | 14.09-14.09 (med 14.09) | 3 x1 | 0.13-0.13 |
| utf8@0.1 | ci-moskva | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 6406-100202 | 10.16-10.46 (med 10.24) | 2 x3 | 0.55-0.56 |
| utf8@0.1 | cls-neg-allhigh | auto,nocaps | dfa-byte-class | 1/128 | 2 (tp 4) | 65536-65536 | 4900-7670 | 8.54-13.36 (med 10.95) | 7 x2, 1 x2 | 0.22-0.65 |
| utf8@0.1 | cls-neg-allhigh | vm | vm-hat-first-class | 1/128 | 2 (tp 2) | 65536-65536 | 4900-7670 | 8.54-13.36 (med 10.95) | 7 x1, 1 x1 | 0.22-0.65 |
| utf8@0.1 | cls-s-nbsp | vm | vm-hat-first-class | 1/1 B5 | 1 (tp 1) | 65536-65536 | 4103-4103 | 15.97-15.97 (med 15.97) | 5 x1 | 0.07-0.07 |
| utf8@0.1 | lit-1ch-2b | vm | vm-hat-first-class | 1/1 B5 | 1 (tp 1) | 65536-65536 | 4652-4652 | 14.09-14.09 (med 14.09) | 3 x1 | 0.13-0.13 |
| utf8@0.1 | lit-cyr-run | vm | vm-hat-first-class | 1/1 B5 | 3 (tp 3) | 65536-1048576 | 6406-100202 | 10.16-10.46 (med 10.24) | 2 x3 | 0.55-0.56 |
| utf8@0.1 | lit-offset-at-tail | vm | vm-hat-first-class | 1/1 B5 | 1 (tp 1) | 65536-65536 | 4652-4652 | 14.09-14.09 (med 14.09) | 3 x1 | 0.13-0.13 |
| utf8@0.1 | prp-han | auto,nocaps | dfa-byte-class | 3+/12 | 3 (tp 6) | 65536-1048576 | 4604-73613 | 14.21-14.43 (med 14.24) | 3 x6 | 0.86-0.87 |
| utf8@0.1 | prp-han | vm | vm-hat-first-class | 3+/12 | 3 (tp 3) | 65536-1048576 | 4604-73613 | 14.21-14.43 (med 14.24) | 3 x3 | 0.86-0.87 |
| utf8@0.1 | prp-lu | auto,nocaps | dfa-byte-class | 3+/47 | 1 (tp 2) | 65536-65536 | 5636-5636 | 11.63-11.63 (med 11.63) | 3 x2 | 0.11-0.11 |
| utf8@0.1 | prp-lu | vm | vm-hat-first-class | 3+/47 | 1 (tp 1) | 65536-65536 | 5636-5636 | 11.63-11.63 (med 11.63) | 3 x1 | 0.11-0.11 |
| utf8@0.1 | prp-n | auto,nocaps | dfa-byte-class | 3+/21 | 1 (tp 2) | 65536-65536 | 5790-5790 | 11.32-11.32 (med 11.32) | 3 x2 | 0.53-0.53 |
| utf8@0.1 | prp-n | vm | vm-hat-first-class | 3+/21 | 1 (tp 1) | 65536-65536 | 5790-5790 | 11.32-11.32 (med 11.32) | 3 x1 | 0.53-0.53 |
| utf8@0.1 | prp-notl | auto,nocaps | dfa-byte-class | 3+/109 | 2 (tp 4) | 65536-65536 | 7931-7942 | 8.25-8.26 (med 8.26) | 7 x2, 3 x2 | 0.22-0.55 |
| utf8@0.1 | prp-notl | vm | vm-hat-first-class | 3+/109 | 2 (tp 2) | 65536-65536 | 7931-7942 | 8.25-8.26 (med 8.26) | 7 x1, 3 x1 | 0.22-0.55 |
| utf8@0.1 | prp-zs | auto,nocaps | dfa-byte-class | 3+/5 | 2 (tp 4) | 65536-65536 | 5606-7475 | 8.77-11.69 (med 10.23) | 7 x2, 3 x2 | 0.22-0.63 |
| utf8@0.1 | prp-zs | vm | vm-hat-first-class | 3+/5 | 2 (tp 2) | 65536-65536 | 5606-7475 | 8.77-11.69 (med 10.23) | 7 x1, 3 x1 | 0.22-0.63 |
| utf8@0.1 | qnt-lazy-2b | vm | vm-hat-first-class | 1/1 B5 | 1 (tp 1) | 65536-65536 | 4652-4652 | 14.09-14.09 (med 14.09) | 3 x1 | 0.13-0.13 |
| utf8@0.1 | qnt-plus-2b | vm | vm-hat-first-class | 1/1 B5 | 1 (tp 1) | 65536-65536 | 4652-4652 | 14.09-14.09 (med 14.09) | 3 x1 | 0.13-0.13 |

## Appendix C. Dense, no dominant gap (mean gap <= 8, share <= 0.5, >= 16 landings)

| set | pattern | cfg | site | cover/|S| | subjects (regime cells) | len B | landings | mean gap | dominant gap (cells) | share |
|---|---|---|---|---|---|---|---|---|---|---|
| altwide@0.3 | nar4-256 | auto,nocaps | dfa-byte-class | 3+/4 | 5 (ss 10) | 226-240 | 26-35 | 6.21-8.00 (med 6.68) | 1 x10 | 0.13-0.20 |
| altwide@0.3 | nar4-256 | vm | vm-hat-first-class | 3+/4 | 5 (ss 5) | 226-240 | 26-35 | 6.21-8.00 (med 6.68) | 1 x5 | 0.13-0.20 |
| altwide@0.3 | nar4-512 | auto,nocaps | dfa-byte-class | 3+/4 | 5 (ss 10) | 226-240 | 26-35 | 6.21-8.00 (med 6.68) | 1 x10 | 0.13-0.20 |
| altwide@0.3 | nar4-512 | vm | vm-hat-first-class | 3+/4 | 5 (ss 5) | 226-240 | 26-35 | 6.21-8.00 (med 6.68) | 1 x5 | 0.13-0.20 |
| altwide@0.3 | nar4-64 | auto,nocaps | dfa-byte-class | 3+/4 | 5 (ss 10) | 226-240 | 26-35 | 6.21-8.00 (med 6.68) | 1 x10 | 0.13-0.20 |
| altwide@0.3 | nar4-64 | vm | vm-hat-first-class | 3+/4 | 5 (ss 5) | 226-240 | 26-35 | 6.21-8.00 (med 6.68) | 1 x5 | 0.13-0.20 |
| altwide@0.3 | w-8 | auto,nocaps | dfa-byte-class | 3+/6 | 25 (ss 42,tp 8) | 219-524288 | 33-93875 | 4.25-6.06 (med 5.56) | 1 x36, 2 x10, 3 x4 | 0.14-0.32 |
| altwide@0.3 | w-8 | vm | vm-hat-first-class | 3+/6 | 25 (ss 21,tp 4) | 219-524288 | 33-93875 | 4.25-6.06 (med 5.56) | 1 x18, 2 x5, 3 x2 | 0.14-0.32 |
| bounded@0.3 | cls-atleast-4096 | auto,nocaps | dfa-byte-class | 1/26 | 1 (ss 2) | 64-64 | 19-19 | 3.22-3.22 (med 3.22) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | cls-atleast-4096 | vm | vm-hat-first-class | 1/26 | 1 (ss 1) | 64-64 | 19-19 | 3.22-3.22 (med 3.22) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | ctx-greedy-256 | auto,nocaps | vm-first-class-bounded | 3+/3 | 1 (ss 2) | 154-154 | 18-18 | 7.76-7.76 (med 7.76) | 1 x2 | 0.29-0.29 |
| bounded@0.3 | ctx-greedy-256 | vm | vm-hat-first-class | 3+/3 | 1 (ss 1) | 154-154 | 18-18 | 7.76-7.76 (med 7.76) | 1 x1 | 0.29-0.29 |
| bounded@0.3 | ctx-lazy-1024 | auto,nocaps | vm-first-class-bounded | 3+/3 | 1 (ss 2) | 154-154 | 18-18 | 7.76-7.76 (med 7.76) | 1 x2 | 0.29-0.29 |
| bounded@0.3 | ctx-lazy-1024 | vm | vm-hat-first-class | 3+/3 | 1 (ss 1) | 154-154 | 18-18 | 7.76-7.76 (med 7.76) | 1 x1 | 0.29-0.29 |
| bounded@0.3 | ctx-lazy-256 | auto,nocaps | vm-first-class-bounded | 3+/3 | 1 (ss 2) | 154-154 | 18-18 | 7.76-7.76 (med 7.76) | 1 x2 | 0.29-0.29 |
| bounded@0.3 | ctx-lazy-256 | vm | vm-hat-first-class | 3+/3 | 1 (ss 1) | 154-154 | 18-18 | 7.76-7.76 (med 7.76) | 1 x1 | 0.29-0.29 |
| bounded@0.3 | ctx-lazy-64 | auto,nocaps | vm-first-class-bounded | 3+/3 | 1 (ss 2) | 154-154 | 18-18 | 7.76-7.76 (med 7.76) | 1 x2 | 0.29-0.29 |
| bounded@0.3 | ctx-lazy-64 | vm | vm-hat-first-class | 3+/3 | 1 (ss 1) | 154-154 | 18-18 | 7.76-7.76 (med 7.76) | 1 x1 | 0.29-0.29 |
| bounded@0.3 | dig-exact-16 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | dig-exact-16 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | dig-exact-2 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | dig-exact-2 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | dig-exact-32 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | dig-exact-32 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | dig-exact-8 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | dig-exact-8 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | dig-upto-16 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | dig-upto-16 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | dig-upto-2 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | dig-upto-2 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | dig-upto-32 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | dig-upto-32 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | dig-upto-4 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | dig-upto-4 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | dig-upto-8 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | dig-upto-8 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | dotted4 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | hex32 | auto,nocaps | dfa-byte-class | 2/16 | 9 (ss 12,tp 6) | 110-65536 | 32-15238 | 2.01-4.34 (med 4.05) | 1 x12, 2 x6 | 0.19-0.47 |
| bounded@0.3 | hex32 | vm | vm-hat-first-class | 2/16 | 9 (ss 6,tp 3) | 110-65536 | 32-15238 | 2.01-4.34 (med 4.05) | 1 x6, 2 x3 | 0.19-0.47 |
| bounded@0.3 | nest2-4 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | nest2-4 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | nest2-64 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | nest2-64 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | nest2-letters-6 | auto,nocaps | dfa-byte-class | 1/26 | 1 (ss 2) | 64-64 | 19-19 | 3.22-3.22 (med 3.22) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | nest2-letters-6 | vm | vm-hat-first-class | 1/26 | 1 (ss 1) | 64-64 | 19-19 | 3.22-3.22 (med 3.22) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | nest3-16 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | nest3-16 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | nest3-3 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | nest3-3 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| bounded@0.3 | year4 | auto,nocaps | dfa-byte-class | 1/10 | 1 (ss 2) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x2 | 0.50-0.50 |
| bounded@0.3 | year4 | vm | vm-hat-first-class | 1/10 | 1 (ss 1) | 254-254 | 41-41 | 5.28-5.28 (med 5.28) | 1 x1 | 0.50-0.50 |
| capability@0.2 | hex8-bounded | auto,nocaps | dfa-first-class-bounded | 2/16 | 9 (ss 2,tp 16) | 56-1048576 | 23-371083 | 2.45-4.36 (med 3.16) | 1 x18 | 0.24-0.50 |
| capability@0.2 | hex8-bounded | vm | vm-hat-first-class | 2/16 | 9 (ss 1,tp 8) | 56-1048576 | 23-371083 | 2.45-4.36 (med 3.16) | 1 x9 | 0.24-0.50 |
| capability@0.2 | tail-space-eol | vm | vm-hat-first-class | 2/6 | 6 (tp 6) | 65536-1048576 | 9094-160739 | 6.52-7.21 (med 6.85) | 7 x6 | 0.24-0.38 |
| capability@0.2 | wild-datetime-datefinder-alternation | nocaps | dfa-byte-class | 3+/38 | 1 (ss 1) | 39-39 | 19-19 | 1.94-1.94 (med 1.94) | 1 x1 | 0.50-0.50 |
| capability@0.2 | wild-logparse-syslogbase-expanded | auto,nocaps | vm-first-class-bounded | 3+/16 | 14 (ss 10,tp 18) | 39-1048576 | 16-270784 | 2.29-6.25 (med 3.87) | 1 x26, 2 x2 | 0.17-0.40 |
| capability@0.2 | wild-logparse-syslogbase-expanded | vm | vm-hat-first-class | 3+/16 | 14 (ss 5,tp 9) | 39-1048576 | 16-270784 | 2.29-6.25 (med 3.87) | 1 x13, 2 x1 | 0.17-0.40 |
| capability@0.2 | wild-semdiv-empty-alt-repeat-pcre2 | vm | vm-hat-first-class | 2/11 | 3 (tp 3) | 65536-1048576 | 10135-168957 | 6.21-6.47 (med 6.32) | 1 x3 | 0.44-0.45 |
| capability@0.2 | wild-validator-uuid-grok | vm | vm-hat-first-class | 3+/22 | 9 (ss 1,tp 8) | 48-1048576 | 16-375241 | 2.79-4.36 (med 2.99) | 1 x8, 3 x1 | 0.24-0.35 |
| capability@0.2 | wild-waf-crs-942140-dbnames | auto,nocaps | dfa-first-class-bounded | 3+/14 | 9 (ss 2,tp 16) | 81-1048576 | 18-233078 | 3.71-4.55 (med 4.48) | 1 x12, 2 x6 | 0.26-0.30 |
| capability@0.2 | wild-waf-crs-942140-dbnames | vm | vm-hat-first-class | 3+/14 | 9 (ss 1,tp 8) | 81-1048576 | 18-233078 | 3.71-4.55 (med 4.48) | 1 x6, 2 x3 | 0.26-0.30 |
| loglines@0.1 | hex32-id | auto,nocaps | dfa-first-class-bounded | 2/16 | 39 (ss 70,tp 8) | 303-1048651 | 94-431970 | 2.21-3.82 (med 2.39) | 1 x74, 2 x4 | 0.28-0.50 |
| loglines@0.1 | hex32-id | vm | vm-hat-first-class | 2/16 | 39 (ss 35,tp 4) | 303-1048651 | 94-431970 | 2.21-3.82 (med 2.39) | 1 x37, 2 x2 | 0.28-0.50 |
| loglines@0.1 | http-5xx | vm | vm-hat-first-class | 1/1 B5 | 5 (ss 5) | 334-1269 | 16-16 | 5.07-5.40 (med 5.27) | 2 x5 | 0.40-0.40 |
| loglines@0.1 | ipv6 | vm | vm-hat-first-class | 2/16 | 39 (ss 35,tp 4) | 303-1048651 | 94-431970 | 2.21-3.82 (med 2.39) | 1 x37, 2 x2 | 0.28-0.50 |
| loglines@0.1 | uuid | vm | vm-hat-first-class | 2/16 | 39 (ss 35,tp 4) | 303-1048651 | 94-431970 | 2.21-3.82 (med 2.39) | 1 x37, 2 x2 | 0.28-0.50 |
| syntax@0.1 | unp-p-uc | auto,nocaps | dfa-byte-class | 3+/139 | 4 (ss 2,tp 6) | 75-1048576 | 30-319470 | 2.55-3.30 (med 3.28) | 1 x8 | 0.41-0.42 |
| syntax@0.1 | unp-p-uc | vm | vm-hat-first-class | 3+/139 | 4 (ss 1,tp 3) | 75-1048576 | 30-319470 | 2.55-3.30 (med 3.28) | 1 x4 | 0.41-0.42 |
| utf8@0.1 | asr-lb-class | auto,nocaps | vm-byte-class | 2/6 | 2 (tp 4) | 65536-65536 | 9216-10163 | 6.45-7.11 (med 6.78) | 5 x2, 7 x2 | 0.17-0.21 |
| utf8@0.1 | asr-lb-class | vm | vm-hat-first-class | 2/6 | 2 (tp 2) | 65536-65536 | 9216-10163 | 6.45-7.11 (med 6.78) | 5 x1, 7 x1 | 0.17-0.21 |
| utf8@0.1 | cls-neg-cjk | auto,nocaps | dfa-byte-class | 3+/174 | 1 (tp 2) | 65536-65536 | 11101-11101 | 5.90-5.90 (med 5.90) | 3 x2 | 0.40-0.40 |
| utf8@0.1 | cls-neg-cjk | vm | vm-hat-first-class | 3+/174 | 1 (tp 1) | 65536-65536 | 11101-11101 | 5.90-5.90 (med 5.90) | 3 x1 | 0.40-0.40 |
| utf8@0.1 | prp-notl | auto,nocaps | dfa-byte-class | 3+/109 | 5 (tp 10) | 65536-1048576 | 10131-167058 | 4.14-6.47 (med 6.28) | 3 x8, 7 x2 | 0.18-0.21 |
| utf8@0.1 | prp-notl | vm | vm-hat-first-class | 3+/109 | 5 (tp 5) | 65536-1048576 | 10131-167058 | 4.14-6.47 (med 6.28) | 3 x4, 7 x1 | 0.18-0.21 |
| utf8@0.1 | prp-zs | auto,nocaps | dfa-byte-class | 3+/5 | 5 (tp 10) | 65536-1048576 | 8288-132528 | 6.16-7.91 (med 7.88) | 7 x8, 5 x2 | 0.15-0.21 |
| utf8@0.1 | prp-zs | vm | vm-hat-first-class | 3+/5 | 5 (tp 5) | 65536-1048576 | 8288-132528 | 6.16-7.91 (med 7.88) | 7 x4, 5 x1 | 0.15-0.21 |
