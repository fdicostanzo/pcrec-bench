# pcrec references — the map of what this project builds on in ~/pcrec

Read-only pointers into the sibling repository. The pcrec documents are
the truth; this file only says where to look and why it matters here.
Line numbers are as of pcrec main `fc126af` (2026-08-24) and drift —
grep the id if a line has moved. Compiled 2026-08-24 from the pcrec
manager session's (pcrecdev1) reference dump plus this session's own
reading; add rows as new dependencies appear.

Convention: `pcrec D52` = ~/pcrec/docs/dev/decisions.md entry D52;
`pcrec [BENCH-1]` = a ~/pcrec/docs/dev/plan.md row.

## 1. Charter and rulings

| id | where | why it matters here |
|---|---|---|
| pcrec D52 | docs/dev/decisions.md:4404 | pcrec-bench is a SIBLING repo; the scope mandate covers both; boundary rules (:4419-4422): NOT pcrec's regression gate; dependencies live HERE never in pcrec; pcrec is pinned by tag/commit like every other testee. Also the grounding measurement: libpcre2 is not a terminating oracle in the K23 hazard band; a linear-time engine (RE2 / rust regex) is the terminating-oracle candidate. |
| seeding record | docs/dev/dev_journal.md:9443-9500 (twenty-ninth session) and :9717 ("shim = dependency = pcrec-bench territory") | how the four founding principles were stated; the RE2 cell owed to pcrec's altcls work because no C ABI/headers were on the box — an early example of a bench-side obligation. |
| pcrec CLAUDE.md:7 | ~/pcrec/CLAUDE.md | the mandate naming both directories. |
| pcrec D12 | docs/dev/decisions.md:322 | bench budgets come from MEASURED medians; the discipline behind every number. |
| pcrec D14 | docs/dev/decisions.md:521 | `make bench` distinguishes CLEAN from NOT-MEASURED (a harness failure is not a budget failure). |
| pcrec D15 | docs/dev/decisions.md:539 | every optimization needs a bench case that EXERCISES it — the shape a feedback row into pcrec must take. |
| pcrec D17 / R3.x | docs/dev/decisions.md (grep D17), tests/bench/compare/CLAUDE.md | per-case margins from measured spread; never widen a margin to make red green; ratios vs other engines are NOT a regression gate (they flip sign run to run — R2-B1). |
| pcrec D35 | docs/dev/decisions.md (grep D35), docs/measurements/CLAUDE.md, scripts/measure.sh | the archived-probe discipline: stable file names, verbatim output, a source-information header. Artifacts here should carry the same provenance. |
| pcrec D26 | docs/dev/decisions.md (grep D26) | PCRE2 is the semantic source of truth, effort tiered by distance from the core — the same tiering applies to how correctness verdicts are scored here. |

## 2. Plan rows in pcrec that pcrec-bench serves or is served by

| row | where | relation |
|---|---|---|
| [BENCH-1] | docs/dev/plan.md:1448 | Frank's FEATURE-SPANNING BENCHMARK EXPANSION + THE PRIORITIZER: per-feature-family case groups at graded complexities; a LATENCY / SHORT-SUBJECT group (time-to-first-match from process start, per-call overhead on short subjects); two instruments — absolute per-case floors as the GATE (stays in pcrec), a cross-engine RELATIVE ranking vs libpcre2 as the PRIORITIZER (informational, worst-first worklist); known head: case (f) at 0.151 relative. Much of the prioritizer's DATA is what this repo produces. |
| [BENCH-CEIL] | docs/dev/plan.md:1449 | the EXPERT-C CEILING ARM: hand-written C matchers as their own testee; same compiler/flags/box as pcrec so the gap decomposes into generator overheads; v1 scope DFA-tier; span-identical or INVALID; technique documented per case. "a hand-C testee triple is also natural THERE later" — i.e. here. |
| [ENG-PGO] cross-note | docs/dev/plan.md:706 | the `--profile` emission mode's SECOND customer is the bench loop: profile attachment by section (prefilter, VM, rungs) and finer increments to guide optimization priority. |
| [DD-13] / [DD-13a] | docs/dev/plan.md:1021; docs/design/dd13_format/requirements.md §5 (R-BENCH-1..9), §10-§12; docs/design/dd13_format/frank_inputs.md | the UNIFIED pattern-source/test file format — APPROACH.md §8 Q1 is resolved HERE: the bench SET format is owned by pcrec's [DD-13]. R-BENCH-1..9 are this project's stated needs (per-case tags: tier/hazard/size/verification-method; per-testee application sections with a last-reference-wins options cascade; first-class "unsupported"; engine-neutral expectations; POSIX-vs-Perl convention tag; subject-by-reference; declared per-library tweaks; import from .rxt; config sections shared with pcrec's build variants). [DD-13b/c] (design, panel) are NOT started. |
| [LIB], [V-E] | docs/dev/plan.md:489, :546, :1051 | subpattern libraries / compilation units cross-reference bench sets; PLANNED, not on the spine. |
| [TT-10], K31 addendum | docs/dev/plan.md:437; docs/dev/known_issues.md (K31) | this box's CPU-time inflation under load (>2×): CPU-bounded checks lie under load. Bench on a QUIET box and RECORD load in the artifact. |
| K32 | docs/dev/known_issues.md (K32) | the prefilter's quadratic compile on `X{4000}` — a bench-shaped finding (compile-time axis). |

## 3. Frank's direction (verbatim-adjacent, journal)

| where | what |
|---|---|
| docs/dev/dev_journal.md:13227-13235 (2026-08-24 ~10:5x) | the POST-SPINE LOOP: set up pcrec-bench → gather data across regex implementations over a variety of patterns → pick the outliers where pcrec loses → find GENERAL optimizations (no per-pattern special cases — the 2026-08-23 rule) → loop. Obscure PCRE2 features deferred. "Completing the spine" is open; ruled at [DD-14]'s close. Explicitly "not a decision — details later". |
| docs/dev/dev_journal.md, thirty-ninth session parts 12-13 (grep "profile attachment") | trace is for debugging, the PROFILE is for optimization; sections and finer increments; scenario sweeps. |
| plan.md:1448 quote | "whenever i see benchmarks, its usually a series of rather basic benchmarks that do not really exercise the capabilities". |
| plan.md:1449 quote | "for a set of (dfa?) patterns, i'd like to directly write performant C code … consider them one engine to compare against … understand how far off we are". |
| engines Frank has named so far | libpcre2 10.46 (the oracle and constant reference arm), perl 5.40.1 (the D27 Perl arm), python `re` (base-tier oracle; no subroutine calls). No bench roster beyond "various rx implementations" has been ruled — that is [B1]'s conversation. |

## 4. Harnesses and measurement assets to reuse or mirror

| asset | where | note |
|---|---|---|
| pcrec's own bench | tests/bench/run_bench.sh, bdriver.c, compare/compare.sh, compare/gate.sh, floors.tsv, run_history.tsv, results-*.md | budgets, throughput via the bdriver, D12 floors; the compare matrix pins a core, repeats BENCH_TRIALS, reports medians and spread, oracle-checks every span, emits a TSV block + a write-up. The closest existing thing to an artifact. |
| timeout defect | docs/testing.md:2407-2430 | uutils `timeout` cost ~108 ms/call and sat INSIDE bench numbers; use `/usr/bin/gnutimeout`. |
| the email specimen | docs/design/subroutines_measurements/email_specimen/ (README, orig.rx, factored.rx, factored_x.rx, gen_subjects.py + manifest.tsv, gen_throughput_subjects.py, driver.c, throughput_driver.c, pcre2_throughput.c, *_results.log) | the RFC 5322 pattern, 85 subjects + three 1 MB throughput subjects, a 5×-median throughput driver, and a dlopen libpcre2 reference harness (no pcre2.h on this box). READY-MADE FIRST BENCH ROW. Subjects are derived (gitignored), regenerated by the scripts, integrity via the committed manifest. |
| libpcre2 ctypes binding | docs/design/eng_brep_measurements/probes/pcre2_ctypes.py | the committed binding the whole oracle chain borrows (br_oracle.py → la_oracle.py → sr_oracle.py). |
| measurement style | docs/design/lookaround_measurements/, subroutines_measurements/ (probes/, out/ with source headers); out/leftrec.txt (a probe with its own guard), out/prefilter.txt (the 21×-350× prefilter cost table) | the style Frank expects: question, method, numbers, archived verbatim. |
| measurement discipline | docs/dev/learnings.md §1 (measurement), §2 (oracle strategy), §3 (check design) | quiet box, medians/spread, per-core occupancy before pinned runs, poisoned-pinned-core incident, controls that share no source with what they control. |
| the .rxt format | docs/testing.md | today's case carrier and the import source (R-BENCH-8). |
| oracle tiers | docs/testing.md; tests/registry (PC-3) | python `re` base tier, libpcre2 differential, the D27 blinded method; D52's linear-time third tier at need. |

## 5. Feedback into pcrec — no mechanism exists yet

Frank's loop implies: an outlier → a plan row under pcrec's [ENG-*]/[OPT-*]
family with the bench row as its exercising case (pcrec D15). pcrecdev1's
suggestion (2026-08-24): each bench row carries the pcrec commit AND the
artifact's stamps (`RX_VM_PREFILTER`, `RX_VM_RUNGS`, engine) so outliers
bucket by MECHANISM, not by pattern shape. The shape is proposed in [B1]'s
requirements conversation and recorded in docs/design/requirements.md.

Anything written INTO pcrec (a set format the harness reads, a plan row, a
known_issues row) goes through the pcrec manager session; everything in
pcrec-bench is this project's.
