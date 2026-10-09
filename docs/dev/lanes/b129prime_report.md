# [B129] priming A/B -- lane b129prime report (2026-10-09)

STATUS: COMPLETE for the SAMPLED A/B (Frank's change of plan); the full-cell run was started, stopped within minutes and is NOT done -- awaiting the manager's go.

## Charter-vs-committed checklist

| Brief item | State | Artifact |
|---|---|---|
| `--prime` on every driver (pcre2, pcrec, re2, rust, onig, tre, vectorscan) | DONE | `testees/*/driver.c|cc`, `testees/rust/src/main.rs`: the loop runs from `-prime`; the clock is re-read at `it == 0`; the primed pass is the loop body itself (same operation, find-all pass included), answer overwritten by the timed iterations. Without the flag: `prime = 0`, loop bounds and clock unchanged. |
| adapter handle kwarg | DONE | every `testees/*/adapter.py` appends `--prime` iff `handle["prime"]` |
| `run` / `quick` `--prime` | DONE | `pcrecbench/__main__.py`, `harness.run_cell(prime=)` |
| record sentence, no schema change | DONE | `harness.PRIME_NOTE` appended to the note |
| pinned-tier refusal by name | DONE | `harness.PRIME_PINNED_REFUSAL`, raised before the store rule |
| `check_prime_flag` + tools/CLAUDE.md | DONE | `tools/selfcheck.py` (registered in `main()`); 14 driver rows (7 engines x 2 regimes) + refusal + control PASS |
| check-report, check-frontpage | DONE | both rc 0 (detached run) |
| full 3 h A/B | NOT RUN (superseded, killed, partial store deleted) | -- |
| sampled A/B via `quick` | DONE | runner `docs/dev/measurements/2026-10-09-b129-prime-sample-run.sh`, log `build/b129-prime-sample.log` (80 calls, all rc 0, `DONE rc=0 2026-10-09T09:59:08`), 120 scratch records |
| analysis, archive | DONE | `2026-10-09-b129-prime-sample-analysis.py` -> `2026-10-09-b129-prime-sample.txt` (verbatim) |
| verdict, recommendation, methodology wording | DONE | below |

Not run (by instruction): the whole `make check-harness`.

## Design notes
- The primed pass uses the loop body unchanged, so "exactly one untimed
  execution of the same operation" holds by construction for single-match and
  find-all modes; rust's per-subject worker thread and the C drivers' alarm
  both cover the priming call (a priming call that exceeds the subject
  timeout is a timed-out subject, not a silent hang).
- Calibration passes (iters=1 sweeps) are primed too when `--prime` is set;
  the flag is a property of the whole cell.
- `check_prime_flag`'s control stops at a sentinel in `quiet.check`; an
  earlier draft let the control run a real cell on a quiet box (caught and
  fixed before the experiment).

## Sample as run
10 of the 12 asked-for patterns (trimmed to fit 20-30 min: tail-space-eol and
uuid-near-miss dropped): tail-digits-eol, tail-dotstar-txt, tail-ext-lower-txt,
tail-word-eoz, wild-secrets-github-pat, wild-secrets-aws-access-key-id,
wild-datetime-moment-iso8601, email-nested-plus, wild-validator-email-owasp,
wild-waf-crs-942140-dbnames. Both regimes (search --subjects 20; throughput,
all 11 subjects), re2-default + rust-default in one `quick` call and pcrec-auto
(control) in another, A then B back to back, 5 trials, pinned to core 11.
Caveats, all in the archive: email-nested-plus throughput has no number in any
arm for any testee; tail-digits-eol throughput is a wrong-answer cell for re2
and rust in both arms (excluded, unrelated to priming); one pcrec-auto record
(email-nested-plus, search, arm A) is `inconclusive-load` (kept, flagged);
scratch quick records, 5 trials, so the tie/disjoint rule is the front page's
but on a smaller sample.

## Results (all from the archive)
- Noise floor from the control: pcrec-auto (static code, nothing to warm) shows
  B/A 0.9495-1.007, median 0.9948; 8 of 19 cells DISJOINT, 7 of them "faster"
  (search_short: 6 of 10 faster, largest 0.9495). So a primed second run is
  ~2-5% faster on search_short for a engine with nothing to warm: an
  A-then-B order/warm-box effect, not priming.
- RE2: search_short B/A 0.9944-1.015 (median 1.001), 0 of 10 disjoint.
  throughput: 3 of 8 cells disjoint-faster, B/A 0.8341 (tail-dotstar-txt),
  0.8404 (tail-ext-lower-txt), 0.8746 (wild-datetime-moment-iso8601); these
  three cells are RE2 medians of order 1.2-1.9e3 ns, against pcrec's
  7e4-8.8e6 ns -- cells where RE2 already wins by orders of magnitude. The
  other five throughput cells are within 0.3%.
- Rust: B/A 0.9275-1.066; 10 of 18 disjoint (8 faster, 2 slower:
  tail-word-eoz search 1.066, tail-ext-lower-txt search 1.014), the same size
  as the control's drift except tail-ext-lower-txt throughput 0.9275.
- Front-page classification (frontpage.classify, sample cells only): RE2 vs
  pcrec-auto 13 pcrec wins / 5 losses / 0 ties in BOTH A and B; Rust 12/6/0 in
  both. The script lists every cell whose class differs A vs B: none.

## Verdict
In this sample priming changes no front-page conclusion: not one win/loss/tie
class flips for either competitor, and every search_short effect is inside
the control's own 2-5% drift. The only effects clearly above the control are
12-17% on three RE2 throughput cells, which are cells RE2 wins by two to
three orders of magnitude, so the class cannot move. Not shown by the sample:
cells outside these 10 patterns, and anything below the ~5% noise floor.

## Recommendation
(a): no measurable effect that matters for the headline; the full A/B is not
needed to answer Frank's question. If the manager still wants the full run,
the thing to look at is RE2's throughput cells with tiny medians (first-call
state building is visible there, 12-17%), not the search_short cells. A
cheap strengthening that is not the full run: re-run only those three RE2
cells with A/B/A order to separate warming from order drift. Do not start
anything without the manager's go.

## A/B/A follow-up (approved by the manager; appended verbatim to the sample archive)
Three RE2 throughput cells + pcrec-auto as the drift control, A1 / B(primed) /
A2, back to back, 5 trials, 18 `quick` calls, all rc 0, all `measured`.
- RE2 is REAL WARMING, not drift: B/A1 0.8179 / 0.8286 / 0.8835 and B/A2
  0.8368 / 0.8072 / 0.8716 (tail-dotstar-txt / tail-ext-lower-txt /
  wild-datetime-moment-iso8601), every one with disjoint trial ranges, while
  the unprimed repeat A2/A1 is 0.9774 / 1.027 / 1.014 (ranges overlap).
- pcrec-auto control: all nine ratios within 0.9992-1.001; no drift to
  explain it.
- Size: 12-19% of an RE2 median that is 1.2-2.0 microseconds for the
  whole 11-subject set, i.e. tens of ns per subject, the first-call state
  building of the lazy DFA. These cells are RE2 wins over pcrec by a
  factor of hundreds, so no class can move.
Note: the sample's 2-5% pcrec drift was on search_short cells, which the
A/B/A did not re-test (throughput only); the throughput control here shows
none.

## Methodology-page wording (either outcome)
"Each engine is timed on a loop of repeated calls after its pattern is
compiled; lazy-cache engines (RE2, Rust regex) build part of their automaton
on the first call. We checked whether an untimed warm-up call per subject
changes results by re-measuring a 10-pattern sample both ways: no
win/loss/tie classification changed. The one measurable effect is on RE2's
large-subject throughput cells whose whole-set time is only a few
microseconds, where warm-up makes RE2 12-19% faster (confirmed by a
repeat unprimed run, which differed by under 3%); RE2 already leads pcrec on
those cells by orders of magnitude. Elsewhere differences were within the
~5% run-to-run spread. The published numbers are unprimed."

## Manager change request: prime pass OUTSIDE the timed loop (done)
The first implementation put `if (prime && it == 0) t0 = now();` inside the
timed loop. Now, on all seven drivers, the timed inner loop and its body are
exactly master's (C: `for (long it = 0; it < n_it; it++)` with a `volatile
long n_it`, the same volatile bound load as master's `iters`; Rust: `for _ in
0..n_it`); the only new code is an OUTER two-pass loop (`pass` 0 = the single
untimed call, only with the flag) and one `t0 = now()` per subject outside the
loop. The body is not re-indented (diff kept to the wrapper lines).
- `check_prime_flag` re-run on the restructured drivers: 16 PASS, 0 FAIL
  (build/b129-primecheck2.log; it builds fresh drivers in a temp dir).
- Unchanged-behaviour proof: pcrec-auto and re2-default, one search cell
  (tail-ext-lower-txt, 20 subjects) and one throughput cell (tail-dotstar-txt),
  master driver vs fixed driver, both WITHOUT `--prime`, M,F,M,F, 5 trials:
  F/M medians 0.9925-1.0069 over the eight pairs; the pooled min-max ranges
  overlap in all four cells (three single repetitions had disjoint ranges at
  <= 0.75% apart). One fixed-arm record is `inconclusive-load` (kept). Appended
  verbatim to the sample archive.
- The A/B/A and sample numbers above were measured with the FIRST (in-loop)
  implementation. The primed arm is the same single untimed call followed by
  the same timed loop, so the primed semantics are unchanged; they were not
  re-measured (no full re-run requested).

## OWED
Nothing for the sample or the A/B/A. The full-cell A/B is not run (manager's go required).
`--prime` stays scratch-tier only until the schema records it.
