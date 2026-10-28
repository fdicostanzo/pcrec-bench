# Lane b148heldout -- first held-out correctness read of the 43 L6 assists (2026-10-28)

Branch `lane/b148heldout`, on master 027831aa. Tier: SCRATCH only (`--tier scratch
--force-unquiet --synthetic --trials 1 --iters 1`, `--subject-timeout 30`), stores under
`/var/tmp/pcrecbench/b148heldout/<testee>/store`; nothing written to `store/`, no assist edited,
~/pcrec untouched. Timing numbers are NOT results (loaded box, 1 trial, 1 iteration).

## How the NOT-CAPABLE members were exercised

The adapter runs only ASSISTED ledger rows. The probe (`docs/dev/measurements/2026-10-28-b148heldout-probe.py`)
copies `bench/unusual/assists` to a scratch dir, rewrites every ledger `verdict` to ASSISTED (assist files,
token counts and sha256 untouched, so the adapter's re-count still agrees) and sets `tokcount.BUDGET`
to 10**6 in-process only. `$PCRECBENCH_ASSISTS_DIR` points at the copy, which forces the scratch tier. So
all 43 (member, engine) pairs ran, 17 of them over the 300-token budget (NOT-CAPABLE in the real ledger;
marked NC below). Chain: `docs/dev/measurements/2026-10-28-b148heldout-chain.sh`; reader:
`2026-10-28-b148heldout-read.py OUT_DIR`.

## Result: 42 of 43 pairs matched every expectation; 1 pair has 2 mismatches

Regimes run per config: search_short (161 subjects/pattern), throughput (the 1 MB-class subjects),
call-stream (F1 streams, scored by results_sha256 against expectations_stream.tsv). Rows: pcre2-jit 521
match rows, onig 521, re2 2014, rust 2014, vectorscan 1366. Every row is `matched-as-expected` except two.
No gave-up, no timed-out, no crash, no compile failure on any pair (vectorscan `*-twin` arms are
`unsupported-by-declaration`: no captures, as designed).

| engine | members (NC = over budget in the ledger) | rows by regime | outcomes |
|---|---|---|---|
| pcre2-jit | va-tenant NC, va-route NC, va-term NC, va-term-bang NC, co-netstr | search 483, throughput 32, call-stream 6 | all as expected |
| onig-default | va-tenant NC, va-route NC, va-term NC, va-term-bang NC, co-netstr | same | all as expected |
| re2-default | cscan NC, wild-sexp-balanced, wild-json-validate NC, co-luhn, co-isbn, co-member, co-netstr, va-* x4 | search 1932, throughput 72, call-stream 10 | **cscan NC: 2 mismatches**, rest as expected |
| rust-default | cscan, wild-sexp-balanced, wild-json-validate NC, co-luhn/isbn/member/netstr, va-* x4 (all ASSISTED except json) | search 1932, throughput 72, call-stream 10 | all as expected |
| vectorscan-block-som | cscan NC, wild-sexp-balanced, wild-json-validate NC, co-luhn/isbn/member/netstr, va-* x4 NC | search 1288, throughput 68, call-stream 10 | all as expected |

(per-pair verdicts are those in `assists.tsv`; the va-* members have call-stream rows only, the co-*/
recursion members have search + throughput rows, cscan also call-stream.)

### Mismatches (re2 cscan, ledger verdict NOT-CAPABLE, 369 tokens, search_short)

| subject | bytes | expected (libpcre2 oracle) | assist returned | note |
|---|---|---|---|---|
| cs-21 (`digraph-close-top`) | `(?{ x; %>)` (10 B) | match, span [0,10) at offset 0 | nomatch | the `%>` digraph close is not recognised at the top level |
| cs-45 (`backslash-backslash-nl-comment`) | `(?{ // c \\<LF>})` (14 B) | nomatch | match, span [0,14) | `\\<LF>` inside a `//` comment is taken as a splice; the oracle ends the comment at the LF |

The same cscan problem passes 161/161 on rust (ASSISTED, 226 tokens) and vectorscan (NC, 755 tokens)
and all four call-streams (4 streams x 3 engines, results_sha256 equal). The two re2 failures are on a
NOT-CAPABLE member, which the real pinned-tier run declines anyway (`unsupported-by-declaration`), so no
ranked row is affected today. They do show that the NC re2 assist is not a correct implementation.

## Callout fire counts (throughput, `engine_metadata.callout_fires`, counting build)

| member / subject | native (b148l5_report) | re2 | rust | vectorscan |
|---|---|---|---|---|
| co-luhn / co-luhn-1m | 11,308 | 11,308 | 11,308 | 11,308 |
| co-isbn / co-isbn-1m | 8,429 | 8,429 | 8,429 | 8,429 |
| co-member / co-member-1m | 13,158 | 13,158 | 13,158 | 13,158 |
| co-netstr / co-netstr-1m | 10,971,980 | no field | no field | no field |

luhn/isbn/member are equal to the native count on all three assisted engines (the smaller subjects
fire 0/1/2 times, same on all three). co-netstr: the assisted netstring rows (pcre2, onig, re2, rust,
vectorscan) carry NO `callout_fires` (only the `-twin` row has a field, = 0): these assists do not call
the shared callee, so the 10,971,980 native number has no assisted counterpart to compare. If a fire
comparison for netstr is wanted, the assists would need to call `pred`/the callee, or the comparison is
against the host's own iteration count (not recorded).

## Box and wall times

Records are `inconclusive-load` by construction (`--force-unquiet`). Load average at start 8.7 (1 min),
5.9 at launch, 4.9 at the end; pcrec's sessions were running. Wall time per cell (whole `run`, assist
builds included; the rust cell includes the first cargo staticlib builds, builds are cached under
`build/assist/`):

| cell | wall s |
|---|---|
| pcre2-jit-assist-v01 | 14 |
| onig-default-assist-v01 | 13 |
| re2-default-assist-v01 | 15 |
| rust-default-assist-v01 | 63 |
| vectorscan-block-som-assist-v01 | 15 |

An earlier re2 search_short-only cell (discarded and re-run) took about the same. All cells are far
under the ~4 min detach line. At trials 1 / iters 1 these sizes say little about `CELL_CAP_unusual` at
5 trials with calibrated iterations; scale by the harness's calibration, not by this table.

## Not covered / owed

- Not run: mem pass and deep arm for assisted rows (refused by the runner by name, b148aw report).
- One trial, one iteration: nothing here checks run-to-run determinism of an assist's answer (a flaky
  assist would show only if it flipped on this single pass).
- The sexp and json recursion members have no mismatch on rust/vectorscan/re2 over 161 short subjects
  + the throughput texts, but those two sets are the only held-out evidence; the `problems/*-samples.tsv`
  public samples are separate (selftest).
