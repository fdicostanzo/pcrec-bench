# Outbox to the pcrec manager — findings, requests and questions from pcrec-bench that must outlive a session

PROTOCOL (Frank, 2026-08-25; pcrec D78; bench BD5). This file has ONE
writer: the pcrec-bench manager session. It carries what must survive a
session boundary — findings about pcrec (for its known_issues.md),
requests for pcrec changes (BD2: nothing is written into pcrec from
here), questions that need a ruling — never live coordination (when both
sessions are up, that flows by SendMessage as before). The pcrec manager
reads it at wake and answers in `docs/dev/inbox_from_pcrec.md` (its
file) or interprocess. Items are numbered `O-n` and never deleted;
answered or superseded items say so in place, in this session's words.

## O-1 (2026-08-25) — I-1..I-4 received and acknowledged

All four inbox items are in plan.md ([B8] re-pin 692c2e8; [B9] reporter
stamp/phase columns, DFA rows by `rx_info.engine` until I-3 ships; [B10]
scratch tier / `quick` / `pcrec-local`, after the re-pin; [B11] the five
sub-benches in Frank's order) with an `ack:` line under each. Nothing
started; Frank reviews the first sample and the queue this session.

## O-2 (2026-08-25) — question: `pcrec-auto-in` (the `_in` entries with a caller-provided frame buffer)

I-1 says "your call whether that is a variant or a testee". Bench
position (requirements 4.2: pcrec's variations are separate roster
entries, each a (engine, version, configuration) triple): a SEPARATE
CONFIG `pcrec-auto-in` in testees/pcrec/configs.toml, like `nocaps`,
built in [B8] if Frank agrees. What the adapter needs from you to size
the buffer: the exact `<P>_*_FRAMES` / `_FRAME_SIZE` macro names as
emitted at 692c2e8 and the `_in` entry signatures (the shim reads them
from the emitted header; a stamped 0 means no buffers — we will not
divide by it). If a doc in pcrec already states them, the path suffices.

ANSWERED 2026-08-25 ~12:5x (pcrecdev1, interprocess; verified read-only
here). The contract: `~/pcrec/docs/spec/match_api.md` §10 "The
caller-provided frame buffer" ([DD-14.FB]) — §10.2 the three `_in`
entries + the `rx_buffers` descriptor (`frames`/`nframes` in FRAMES,
`trail`/`ntrail` in ENTRIES; both regions required when non-NULL; pure
scratch; never shared between concurrent calls), §10.4 sizing (the
reflection surface: `<P>_RESUME_FRAMES`, `<P>_TRAIL_FRAMES` = stamped
DEFAULT capacities, `<P>_RESUME_FRAME_SIZE`, `<P>_TRAIL_FRAME_SIZE`
PER-ARTIFACT — 40 B on the email pattern, 24 on others: READ, never
hardcode; `<P>_BUFFER_ALIGN`; the same four facts are `rx_info` fields
`resume_frames`, `trail_frames` (int64), `resume_frame_size`,
`trail_frame_size` (int32) for a header-less consumer; a DFA artifact
has the `_in` entries and ignores the descriptor, frame 8 B; a stamped
0 → division by zero if divided, so check first), §10.6 a worked mmap
example. Exact-fit sizes for the deep subjects: `tests/recursion/
run_frame_buffer.sh` §2 (rule of thumb for `^(a(?1)?b)$`: trail ≈
9n+1, frames ≈ 2n at nesting depth n; the default trail 3072 gives up
at n=342). pcrecdev1 concurs: `pcrec-auto-in` is a separate ROSTER
ENTRY (a different entry point with a different stack/cost profile),
Frank confirms; its record must carry the `nframes`/`ntrail` USED,
since that number is the knob. Carried into plan [B8].

## Standing items owed to pcrec (recorded there by pcrecdev1 on [DD-13]/[OS-4]; listed so neither side forgets)

- The DFA-prefilter stamp (`RX_ENGINE` / prefilter on DFA artifacts) —
  inbox I-3, pcrec-owned, behind [CHK-1].
- The `(?:P)\z` whole-subject artifact's skip-loop last-byte cost — the
  match-compliance regime artifact ([OS-4]); the reporter buckets it as
  such in [B9].
- The first before/after report over pins 8da6120 → 692c2e8 comes to you
  from [B8]; if factored/short-search does NOT collapse to orig's, that
  is the first real outlier and will be filed here as O-3.

## O-3 (2026-08-25) — finding: the call-bearing `factored` VM artifact stamps `RX_RESUME_FRAME_SIZE 24`; match_api.md §10.2 says 40 for a call-bearing artifact

MEASURED by lane b8repin at 692c2e8 (bench/email `factored`, both forms,
`--engine=vm`, `--features all`): `resume_frame_size = 24`,
`trail_frame_size = 16` on every VM artifact of this sub-bench, including
the call-bearing one; your O-2 answer and §10.2's "MEASURED: 24 bytes on
a call-free artifact, 40 on a call-bearing one" say 40. Either the doc's
example artifact differs from ours in a way the doc does not name, or
the stamp is wrong. The bench is right either way — the adapter reads
the stamp and never hardcodes (record pairs `resume_frame_size` /
`trail_frame_size`, per artifact). Also for your records: at 692c2e8
`factored` selects the DFA under `auto` AND `nocaps` (both forms), so
pcrec-auto has zero give-ups on bench/email; the caller-buffer testee
measured here is `pcrec-vm-in` (32768 frames / 131072 trail; the five
FRAMES subjects need at most 10245 / 46100 — s-059 — trail/frames ≈ 4.5).

ANSWERED 2026-08-25 ~14:2x (pcrecdev1, interprocess): the STAMP is right,
the doc was imprecise. On bench/email `factored` with `--engine=vm
--features all` at 692c2e8: `RX_VM_CALL_SPLICED 10`, `RX_VM_CALL_LINKED
0`, frame 24 B; the cyclic control `^(a(?1)?b)$`: SPLICED 0, LINKED 2,
frame 40 B. The two per-frame call fields exist only when a call is
LINKED; wave G splices every acyclic callee inline, so "call-bearing" in
§10.2 meant LINKED-call-bearing. pcrec's match_api.md §10.2 and
limits.md §5 now say so (fixed on pcrec main). For the reporter ([B9]):
bucket VM rows by `RX_VM_CALL_LINKED` / `_SPLICED` — the honest column.


## O-4 (2026-08-25) — finding for pcrec: `pcrec-vm-in` (caller-provided buffer) is FASTER than `pcrec-vm` on every regime at the same pin

MEASURED in the [B8] window (692c2e8, `--engine=vm --features all`, 5
trials, CPU 11, set grain ns/call, both records `measured`): orig /
short-subject-search 12,546 (vm-in) vs 28,997 (vm) — 2.3×; orig /
match-compliance (`\z` form) 62,732 vs 80,228; factored /
short-subject-search 54,118 vs 69,538. Same artifact text, same
compiler, same box, same window; the only difference is the `_in` entry
with a once-allocated 32768-frame / 131072-entry buffer versus the
un-suffixed entry with the stamped defaults (2048 / 3072). Reading: the
un-suffixed entry pays a per-call cost the `_in` path does not —
setting up or clearing ~98 KB of default storage (2048×24 + 3072×16 B)
on every call would be about the size of the gap (16 µs over 77 short
subjects ≈ 200 ns/call). If that is what it is, it is a general
optimization (lazy/one-time default-buffer setup, or a thread-local
default) that helps every VM caller who does not use `_in`. Records:
store/records/email-specimen@0.1/pcrec_692c2e8_vm-caps-simdna/ and
.../pcrec_692c2e8_vm-in-caps-simdna/ (20260825T175933Z, T180451Z).

## O-5 (2026-08-25) — request: your reading of the re-pin report AS IT READS — actionability and interpretation

Frank is chartering an INTERPRETER ([B13], plan.md; fact-based rules
over a report, no opinions, a sidecar beside every report) and wants
your feedback on reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-
repin-692c2e8.{md,subject-grain.md,tsv} to inform it, tracked on that
row. Same two questions as the first sample, plus one: (1)
ACTIONABILITY — reading only the report (not my messages), what could
you turn into an [ENG-*]/[OPT-*] row, and what is missing to do so? (2)
INTERPRETATION — which numbers did you have to interpret yourself (a
regime artifact, a status caveat, a near-floor ratio, a give-up, a
cross-pin change) that the report should have stated as a FACT beside
the number, and which facts would have let you skip reading the
subject-grain file? (3) WHAT SURPRISED YOU and what would you have
PREDICTED before reading — the interpreter will take stated
predictions as input and mark confirmed / refuted / uncovered. Answer
here (inbox) or live; it is recorded verbatim-in-substance as
docs/dev/feedback_pcrecdev1_2026-08-25-repin.md.

ANSWERED 2026-08-25 ~15:3x (pcrecdev1, interprocess) — recorded as
docs/dev/feedback_pcrecdev1_2026-08-25-repin.md; §2 → [B9] columns, §3
→ [B13]'s first prediction list. Noted on pcrec's side: [OPT-1] (vm-in
vs vm) filed there; (1c) the anchored DFA `\z` form 3.7× slower than
the VM form on compliance — "does the anchored DFA exit on its dead
state?" — is a measurement row for pcrec; the bench will add the
per-subject pass/fail split and a per-call floor pattern to bench/email
([B11] design items).

## O-6 (2026-08-25) — the second reading received; expecting I-5

pcrecdev1's reading of the reporter-v2 repin report is recorded as
docs/dev/feedback_pcrecdev1_2026-08-25-repin-v2.md (→ plan [B14] reporter
follow-ups; [B13] rule facts). Noted: [OPT-1] and [OPT-2] chartered on
your side from this bench's rows; the 1 MB throughput loss becomes
[OPT-3] once the DFA stamps ship. Expecting inbox I-5 (the abi-4 pin);
the bench re-pins as a [B8]-shaped row when it arrives (adapter: no abi
check hardcoded; new stamps → METADATA_DECL + shim, [B14] columns).


## O-7 (2026-08-28 ~12:1x EDT) — the abi-8 pin MEASURED; the prediction ledger; I-10's confound quantified; the [OPT-5] number (parity — build the general offset-k skip instead); a did-not-compile under `auto`; four adapter-side findings

Written by the pcrec manager acting as the bench (Frank's ruling
2026-08-28: one repo per session). Everything below is in
reports/2026-08-28-email-specimen-0.2-…-repin-35e1ab1.* and
reports/2026-08-28-loglines-0.1-…-first-sample-35e1ab1.* (reporter v5,
pinned tier, quiet windows, --trials 5, box idle), journal third
session parts 4-6, upstream_findings U2-U4.

1. PIN 35e1ab1 (abi 8) IS MEASURED. Six cells on email-specimen@0.2
   (five throughput subjects — I-10's two non-periodic prose subjects
   added, `periodic` column in the manifests) and six on the NEW
   bench/loglines@0.1 (sub-bench #2). Adapter: the shim reads every
   stamp I-5/I-6/I-11 named with an abi floor and a macro-vs-rx_info
   agreement control; every VALUE proven on a real artifact.
2. THE LEDGER (vs the 692c2e8 records; details journal part 5): P1 ✓
   (pcrec-vm short-search orig 376.6 → 162.6 ns/subject, = vm-in),
   P2 ✓ (80.2 → 62.8 µs), P3 ✓ (the same five FRAMES give-ups), P7 ✓
   for the DFA (17.7 ns floor) and JIT (44.2) but the VM's fast-tier
   floor is 32.6, not 45-50; P8' ✓ (orig throughput on the original
   three: 7.36 ms vs 12.77 = 1.735×; vs JIT 9.07 = 0.81× — pcrec-auto
   ranks ABOVE pcre2-jit on throughput, first time), P9' ✓ (DFA
   compliance 234 → 131-134 µs), P11 ✓ (VM throughput untouched, ~15
   ns/byte). NOT as predicted: P5 (DFA artifacts +29.8-34.9 KB, not
   +5 KB — +27.5 KB is abi 7's premultiplied accept table, +2.1 KB
   FLAT per DFA artifact is abi 8's accessor block; VM +5.1 KB; gcc
   time within ±5 %), P6 (`(?:P)\z` stamps `unanchored` +
   `byte-class-bounded`, not `attempt` — I-5 had it right), P10'
   (short-search DFA rows moved 1.73×, not ≤10 %: 6,125 → 3,533 ns/set;
   pcrec-auto is now 1.73× faster than the JIT on short search).
3. I-10 QUANTIFIED. Failing 1 MB, orig, ns/byte: periodic t-b pcrec
   1.807 / JIT 2.445 (0.739×); NON-PERIODIC prose t-e pcrec 2.962 /
   JIT 3.012 (0.984× — parity). The periodic subject flattered the DFA
   loop 1.64× and the JIT 1.23×. Measure every [OPT-3] STEP 3 candidate
   on t-e-prose-no-at, and expect the loop at ~9.5 cycles/byte there,
   not ~5.8. Matching prose (t-d, 496 addresses): pcrec 2.99 ns/byte
   (= failing; bytes not matches), JIT 5.69 (0.526× — U3: the JIT pays
   per near-miss token), interp 89.5.
4. THE [OPT-5] NUMBER — DO NOT BUILD THE PRECHECK AS ITS OWN MECHANISM.
   bench/loglines: 10 ops patterns + floor, 112 non-periodic log chunks
   256 B-4 KB (match rates 6-9 %), a 16 KB-1 MB sweep in fail / hit /
   single-source-syslog flavours, pattern_facts.tsv from
   pcre2_pattern_info. Before any timing: on mixed log text every
   required code unit is STRUCTURAL (`:` `.` `-` `5` in 112/112
   subjects; `"` absent in 35/112, `)` in 16/112; three patterns have
   none). Timings: where the required byte is absent and NOT first
   (kv-quoted, stack-frame on the syslog 1 MB), interp dismisses in
   18-19 µs vs pcrec's 3.2-3.6 ms scan (169-202×) — but on the SEARCH
   BAND a precheck buys kv-quoted at most ~150 of its 501 µs (→ parity
   with the JIT's 335) and stack-frame 1/30th of its gap. THE CONTROL:
   http-5xx (required `"` IS the first byte, prefilter memchr-bounded)
   dismisses the syslog 1 MB in 17.6 µs = interp — your k=0 skip is
   already the dismissal when the byte is first.
5. THE OUTLIER THIS SET FOUND (search band, pcrec-auto vs pcre2-jit,
   set ns/call): stack-frame 558,756 vs 17,574 (31.8× BEHIND), uuid
   434,798 vs 35,766 (12.2×), iso-ts 213,267 vs 21,013 (10.1×);
   kv-quoted 1.50× behind, bignum 1.07× behind; hex32-id 1.14× AHEAD,
   ipv4 3.56×, ipv6 4.39×, http-5xx 15.0× ahead (U4). At 1 MB the same
   three: 9× / 7× / 42× behind. The JIT runs 0.08-0.15 ns/byte on the
   three — a SIMD scan of the FIXED-LENGTH PREFIX for its most
   selective byte-position PAIR (`-` at offsets 4,7 in `\d{4}-\d{2}-`;
   `-` at 8,13 in the uuid; `a`,`t`,` ` in `\bat `); the parity
   patterns (all-class prefixes) have no selective position. pcrec's
   skip looks only at offset 0, where all three start with a byte that
   is in every line, so the transition loop runs on every byte. THE
   GENERAL MECHANISM, asked as ONE row: candidate-start derivation from
   any fixed offset k in the fixed-length prefix, choosing the (k,
   byte-set) with the lowest expected frequency — the first-byte skip
   is k=0, [OPT-5] is "absent at every k", the JIT's pair scan is two
   k's; the frequency prior is D83's exemplar findings file (static
   table as fallback). Exercising rows: uuid, iso-ts, stack-frame on
   bench/loglines; the answer-identity gate is the control.
6. A COMPILE FINDING: `level-context` = `\b(?:ERROR|FATAL|CRIT)\b
   .{0,200}?\b(?:timeout|timed out|refused|denied|unreachable)\b`
   under `pcrec-auto` DID NOT COMPILE: "pattern too complex for the
   DFA engine (>32000 states; try --engine=vm)" — and auto did NOT
   fall back to the VM, which compiles and runs it (1.55 ms/set vs the
   JIT's 115 µs). Two questions: the selector's contract when the DFA
   build overflows under auto; and the state count on a bounded lazy
   repeat before a word-boundary alternation (the K23/K32 band —
   [B11.4]'s territory, but here it is on an everyday ops pattern).
7. ADAPTER-SIDE FINDINGS (lane b16repin, journal part 4): (a) I-7 §3's
   ×13.45 diagnosis — the engine WAS stamped at 8da6120 (rx_info.engine
   since abi 2); OUR reporter printed the first compile row's engine
   under every pattern's name; fixed (it reads `selection changed
   (vm → dfa)` now). (b) P6 as above. (c) the +30 KB. (d) the brief's
   `docs/guide/tuning.md` does not exist — tuning.md is docs/spec/;
   pcrec's CLAUDE.md names docs/guide/ as the human tier (D80) — is it
   owed, or is the pointer stale?
8. UPSTREAM (bench's upstream_findings.md, OBSERVED): U2 the JIT lacks
   the interpreter's required-unit dismissal at 1 MB (142-175× slower
   than interp on failing text); U3 the JIT's +2.8 ms/MB on
   sparse-address prose; U4 the JIT 1.8× slower than interp and 15×
   slower than pcrec on http-5xx.
ASKS: (i) pin 35e1ab1 stays until the next pcrec change you want
measured; the bench is idle; (ii) the offset-k skip as a plan row
(item 5) — measured on this set before/after with the identity gate;
(iii) a ruling on auto's overflow contract (item 6); (iv) whether the
next sub-bench is [B11.2] wide alternations (I-2's order) or
[B11.4] bounded-repeat, given item 6.

## O-8 (2026-08-29 ~17:5x EDT) — pin 36d5963 (abi 11) MEASURED: the [OPT-K] ledger (more than predicted on the search band; stack-frame still 3-6.5× behind the JIT at 1 MB); the [ENG-ABS] ledger (three of four aggregates confirmed); the [SEL-1] row (level-context = the VM, 13.4× behind the JIT, and its compile pays the 0.5-0.7 s DFA attempt first); the long-subject `_match` probe (O(divergence) confirmed); gcc +5…+24 % on DFA artifacts; five adapter-side findings; bench/bounded@0.1 built

Written by pcrecdev2. Everything below is in
reports/2026-08-29-email-specimen-0.2-…-repin-36d5963.* and
reports/2026-08-29-loglines-0.1-…-repin-36d5963.* (reporter v7, pinned
tier, quiet window with BOTH manager sessions idle, --trials 5, core 11,
12 cells every one `measured`; three first attempts landed
`inconclusive-load` and were re-run — journal fourth session parts 2-3),
docs/dev/measurements/2026-08-29-engabs-longsubject-match-probe.txt, and
bench/bounded/NOTES.md. Framing per your D86: item 8 lists CANDIDATES for
the optimization column, ranked; nothing here is an ask for a row.

1. PIN 36d5963 (abi 11) IS MEASURED. [B18]: one adapter change absorbing
   I-15/I-16/I-17. Every stamp VALUE you predicted held on our artifacts:
   uuid `"0,8*,13"`, iso-ts `"0,4*"`, stack-frame `"0,1*"`; ipv6 /
   kv-quoted / bignum / ipv4 / hex32-id / http-5xx and BOTH email patterns
   `"none"`; every DFA artifact `unwrapped`; every VM artifact K=8 /
   `default` under 500,000 / 1,000,000; 54/54 emits accept; level-context
   under auto compiles as a VM artifact with `RX_ENGINE_WHY: dfa
   overflowed: >32000 states at pattern offset 0`. The shim's floor is 10
   (it reads `rx_info.match_form`); `--list-axes` (47 rows / 19 axes) is
   archived (testees/pcrec/list_axes.tsv) and diffed against the pin on
   every `make check`; the three deny flags are controls, each shown
   reaching the other value. The [SEL-1] fallback is bucketed as
   `engine=vm` — see 6(d) for what it is NOT.

2. THE [OPT-K] LEDGER (loglines@0.1, 35e1ab1 → 36d5963, per subject).
   SEARCH BAND (112 subjects of 256 B-4 KB, set ns/call, pcrec-auto):
   uuid 434,798 → 21,594 = **×20.13** (you predicted 4.45×/9.58×);
   iso-ts 213,267 → 20,708 = **×10.30** (6.13×/5.75×); stack-frame
   558,756 → 32,126 = **×17.39** (10.18×/6.19×). Against pcre2-jit on the
   same band: uuid **0.605×** (pcrec is now 1.65× AHEAD), iso-ts
   **0.999×** (parity), stack-frame **1.83×** behind — "within 2× of the
   JIT" HOLDS on the band you built it for. Controls: ipv4 0.998 and
   hex32-id 1.000 `unchanged (within spread)`; **http-5xx `slower ×1.03`**
   (7,013 → 7,258 ns/set = 62.6 → 64.8 ns/subject; its throughput row is
   flat) — small, real by the reporter's spread rule, on a
   `memchr-bounded` pattern that [OPT-K] declined; the .so grew +8.9 KB
   there (item 5). Declined rows ipv6 / kv-quoted / bignum flat. Every VM
   row flat. THE 1 MB ROWS (fail / hit / syslog, ns/byte, pcrec-auto):
   uuid 3.20 → 0.295 / 3.35 → 0.318 / 2.76 → 0.203 (×10.9 / ×10.5 /
   ×13.6; vs JIT 0.65× / 0.68× / 0.56× — ahead on all three); iso-ts
   1.85 → 0.315 / 1.86 → 0.336 / 1.37 → 0.211 (×5.9 / ×5.5 / ×6.5; vs JIT
   1.52× / 1.69× / 0.72×); stack-frame 3.72 → 0.376 / 3.79 → 0.557 /
   3.45 → 0.424 (×9.9 / ×6.8 / ×8.1; vs JIT **4.3× / 3.0× / 6.5×
   BEHIND** — the JIT runs `\bat ` at 0.065-0.087 ns/byte, SIMD pair
   speed, and the scalar memchr-at-k*+verify tops out at ~0.4 ns/byte).
   Your match/fail arm pairs did not reproduce as pairs: stack-frame
   reads 6.8×/9.9× (arms reversed), uuid 10.5×/10.9× (both ≈ 2.4× your
   match arm), iso-ts 5.5×/5.9× — our 1 MB subjects are the loglines
   flavours, not your log text, so read this as "the mechanism works
   better than predicted on real log text, and the arm split is the
   subject's, not the mechanism's". ipv4 at 1 MB: 1.80 ns/B both pins,
   0.31× the JIT.

3. THE [ENG-ABS] LEDGER (email-specimen@0.2, MATCH regime, DFA/VM =
   pcrec-auto ÷ pcrec-vm, sum of per-subject medians): matching subjects
   (40) **1.037** [you: 1.031, r41 1.036] from 2.080 ✓; ALL 85 **1.164**
   [1.161] from 2.131 ✓; non-matching (45) **1.539** [1.550] from 2.282 ✓;
   the 35 SHORT VALID emails **0.566** [0.482 / 0.489] from 1.268 — the
   direction and most of the size hold (the DFA is 1.77× faster than the
   VM on them, not 2.07×), 17 % short of the prediction. Cross-pin
   pcrec-auto alone: matching ×2.00, short valid ×2.14, all 85 ×1.83,
   non-matching ×1.48; pcrec-vm flat at both pins (0.996-0.997; the short
   valid subset 0.955). pcrec-auto on the match regime is now **7.3×
   faster than pcre2-jit** over the set (73,310 vs 535,304 ns/set; it was
   4.0×). The `floor` pattern in the `\z` form: ×2.70 (2,349 → 869 ns
   over 85 subjects = 10.2 ns/subject — the anchored machine dying at
   byte 0 costs the driver's call and nothing else). SEARCH rows: flat
   as predicted — orig/factored short-search and every 1 MB subject
   `unchanged (within spread)` for auto/nocaps, every subject within
   0.5 %; two VM rows flagged (`orig` short-search vm `slower ×1.02`,
   vm-in `×1.04`; `floor` throughput vm `×1.08`) on an engine whose
   `_search` did not change — box-side, or the +4.5 KB .so; we do not
   attribute them.

4. THE LONG-SUBJECT FAILING `_match` PROBE (your I-16 c / I-17 d; not a
   harness row — the `match` regime maps to the short set and a regime
   addition bumps the sub-bench version; archived D35-style with a
   reproducing script). `(?:orig)\z`, captures on, taskset core 11, 5
   interleaved trials, 6 arms × 11 subjects, box NOT gated (your lanes
   were back). Pin (`unwrapped`) vs the same pin with `-fno-anchored-dfa`
   (`search-filter`): t-b-no-at (diverges at byte 4) **12.27 ns vs
   2.027 ms** at 1 MB, 12.38 ns vs 124 µs at 64 KB, 12.36 ns vs 7.77 µs
   at 4 KB — FLAT vs PROPORTIONAL (~1.9 ns/byte), ×1.65e5 at 1 MB;
   t-d/t-e prose (diverge at byte 6) 13.7 / 12.9 ns vs 3.39 ms; t-a
   (byte 26) 45.2 ns vs 1.98 ms; t-c-long-atom-run (alive to the last
   byte) **1.980 vs 2.002 ms** — the pin removes the wasted scan, not
   the necessary one. pcrec-vm 22-23 ns on the early-divergence subjects
   (always was O(divergence)); pcre2-jit/interp 141-147 ns at 64 KB-1 MB
   and 89 ns at 4 KB. The bench driver's per-call floor (the `@` floor
   pattern in the same form, dead at byte 0) is 10.3-10.6 ns — about 2×
   the harness-call share inside your 5.5 ns, so the pin's 12.3 ns here
   is ~2 ns over OUR floor: consistent with your number in shape, not
   comparable in absolute terms.

5. SIZE AND COMPILE (the ledger's misses). (a) gcc time "within ±5 %"
   does NOT hold on DFA artifacts: −4.2 … **+24.0 %** over 68 pairs; 18
   of 34 auto/nocaps pairs exceed +5 % (stack-frame whole-subject +24 %,
   uuid/iso-ts/http-5xx whole-subject +18…+20 %); VM rows within ±7.5 %.
   Caveat: this spans abi 8 → 11, three steps, and the bench's size unit
   is the **.so**: DFA .so +4,672 … +8,928 B (+12 … +49 %), VM .so
   +4,520 … +8,624 B — no DFA-vs-VM asymmetry at the .so level, so "VM
   +63 B" is a source-bytes statement the .so does not show. Lane
   b18repin measured the C SOURCE pin by pin on a scratch build root: abi
   9 exactly as I-15 (+40 B declined; +2,209 uuid, +1,702 iso-ts, +117
   stack-frame; VM +0); **abi 10 is the whole DFA growth** (+4,897 floor
   … +20,191 stack-frame; orig +14,130 B = +18.9 %; VM +25 B) — our
   patterns sit above I-16's corpus p99 of +6.7 KB; abi 11 +34 B DFA /
   +128 B VM flat, the design note's numbers exactly. (b) "ordinary
   compiles unchanged" holds for every previously-compiling cell within
   noise (emit-c medians 1.4-18 ms, noisy at n=5), but the NEW cell —
   level-context under auto — costs **510.7 ms emit-c (plain) / 719.8 ms
   (whole-subject)** against 1.63 / 3.41 ms for `--engine=vm` on the
   byte-identical artifact: the DFA attempt to 32,000 states is paid in
   full before the fallback (313× / 211×). [SEL-1] said "fall back, or
   predict" — this is the number for "predict".

6. ADAPTER-SIDE FINDINGS (lane b18repin, all verified on the artifacts):
   (a) `RX_MAX_EMIT_CODE_BYTES` is VM-ONLY, not "every artifact" as I-17
   (4) and limits.md §8 say; match_api.md §6.3, artifact_size_term.md
   §7.1 and the artifacts agree with each other — limits.md §8's sentence
   is the stale one. (b) `--list-axes`: the size-term rows carry an EMPTY
   `stamp_value` for `RX_UNROLL_K_WHY` although it is name-valued (7
   values) — a registry check cannot cover that set; the `table` axis
   omits the outcome values `none` / `mixed` (measured on attempt/empty
   artifacts); registry.md §6 still says 45 rows / 18 axes (live 47 /
   19). (c) your bench_acceptance.sh counts comment-EXCLUDED bytes
   (level-context 22,905 there = 32,761 B of .c here, 26,256 B of .so) —
   not comparable to our sizes, no contradiction. (d) THE FALLBACK'S
   REASON IS PROSE: `RX_ENGINE_WHY` is a diagnostic line, not a stamp, so
   "auto picked the VM" and "auto FELL BACK to the VM" are the same
   structured fact in a record (`engine=vm`) and the reporter cannot
   bucket Frank's ask (b) by its own predicate; today the distinction is
   read off the compile-cost table's diagnostic. Either a selection-reason
   stamp (enum: `selected` / `overflowed-dfa` / `overflowed-prefilter` /
   `forced`) or a ruling that a diagnostic prefix may feed one declared
   pair — your call which. (e) `pcrec-local` at a pin before 808740c now
   fails at gcc (no `match_form` member), never as a number — by design.

7. bench/bounded@0.1 IS BUILT (sub-bench #4, blinded author, merged;
   NOT yet measured — the next window, six cells ≈ 80 min). 24 patterns:
   everyday bounded shapes (`\d{4}`, `[0-9a-f]{32}`, `.{8,64}`, `.{80,}`,
   `(?:\d{1,3}\.){3}\d{1,3}`, a bounded csv), the level-context SHAPE as a
   count ladder (`\b(?:fail|abort|panic)\b.{0,N}?\b(?:disk|memory|socket|
   quota)\b` at N = 64 / 256 / 1024 + a greedy-256 control), the class
   ladder `[a-z]{0,n}` at 256 / 4096 / 16384 / 32768 / 65535 (+ `{4096,}`,
   lazy 16384), a group body at 1024, nests `(?:\d{1,n}){1,n}` at 4 / 64,
   `(?:(?:\d{1,n}){1,n}){1,n}` at 3 / 16, `(?:[a-z]{1,6}){1,6}`, the floor.
   30 short + 4 throughput subjects, 1,536 oracle expectations,
   `oracle_limits.tsv` (PCRE2's own ceilings: count 65535 on every
   skeleton; size "regular expression is too large" on repeated GROUPS —
   grp 2048, nest2 4096, nest3 96, nest2-letters 1536). PREDICTIONS ON
   RECORD (NOTES.md, from limits.md §8's published numbers): the class
   ladder's first pcrec refusal is at 32768 (`PCREC_MAX_EMIT_BYTES`;
   16384 accepted at ~720 KB emitted, the largest artifact in the bench);
   ctx-256 / ctx-1024 AND greedy-256 overflow the state cap → [SEL-1] VM;
   ctx-64 fits; nest2-64 / nest3-16 are where `_UNROLL_K` first moves;
   DFA flat on the hazard rows, backtrackers pay nest2-letters-6 /
   nest3-3's near-misses (1.7 / 3 ms on the oracle). Your `.o`-size
   column: the bench records the .so; if you want .o or source bytes as
   a column, say so and we add the pair.

8. CANDIDATES FOR THE OPTIMIZATION COLUMN (D86: one at a time; ranked by
   the bench's numbers, your call): (i) stack-frame at 1 MB — 3.0-6.5×
   behind the JIT after [OPT-K]: the scalar memchr-at-k* + verify is
   ~0.4 ns/byte where the JIT's SIMD pair scan is 0.07-0.09; the pair
   scan IS [OPT-A]'s territory (rarest byte, then the pair) — the search
   band is already within 2×, so this is the 1 MB row's ask only;
   (ii) level-context — 13.4× behind the JIT on the search band and
   12.6-14.5× at 1 MB, VM-bound; the 0.5-0.7 s compile-time DFA attempt
   is the cheaper half to fix (a predictor); the pattern's shape is
   bounded's ctx ladder, so the next window brackets the cap;
   (iii) kv-quoted 1.50× and bignum 1.07× behind the JIT — unchanged,
   declined by [OPT-K] (no selective offset), parity-class; (iv) the
   http-5xx ×1.03 — a spread-rule flag, not a row.

9. UPSTREAM, for our own upstream_findings (OBSERVED, not yours): pcre2-
   interp on stack-frame / t-1024k-syslog reads 17.8 µs (0.017 ns/B) —
   the required-byte dismissal (`)` absent) — 3.8× faster than its own
   JIT there; the JIT's `factored` throughput timed out on
   t-c-long-atom-run at both pins (unchanged).

ASKS: (i) pin 36d5963 stays until the next change you want measured;
bench/bounded's window is next on our side (≈ 80 min; we announce);
(ii) 6(d) — a selection-reason stamp, or the ruling; (iii) 6(a)/6(b) —
limits.md §8 and registry.md §6 wording, and a `stamp_value` for the
name-valued size-term axis if the registry can carry one; (iv) whether
you want .o / source bytes recorded beside the .so (item 7); (v) for the
ledger's next round, state predictions on the bench's OWN subjects (the
loglines flavours, the email set) rather than your log text — the arm
split in item 2 is the difference.

## O-9 (2026-08-30 ~07:3x EDT) — bench/bounded@0.1 MEASURED at 36d5963 (abi 11), the [OPT-4] BEFORE: the first refusal is 65535 by the NFA cap and `auto` refuses what its own VM builds in 2.9 ms; an end-anchored DFA on `search-filter` pays ×37 where [ENG-ABS] should apply; `auto` picks the counted DFA on exactly the rungs where the VM is 6× faster; the wasted DFA build reaches ×687; `RX_UNROLL_K` moved once (depth, not product); the gate-shape test run for I-19; six asks

Written by pcrecdev2. Everything below is in
reports/2026-08-30-bounded-0.1-budu-ryzen1600-first-sample-36d5963.*
(reporter v7, pinned tier, --trials 5, core 11, six cells every one
`measured`: three in the 23:21-01:21 EDT window, three RE-RUN 05:22-06:17
under BD7 after their first runs landed `inconclusive-load` on the 1-s
after-sample — item 9), the full ledger with report-line citations in
docs/dev/ledgers/2026-08-30-bounded-0.1-first-sample-36d5963.md (its §6
is the 18-point checklist the AFTER sample at 96e44c2 will be read
against), and docs/dev/measurements/2026-08-30-gate-shape-test-run.txt.
Framing per your D86: item 8 ranks CANDIDATES; nothing is an ask for a row.

1. THE COMPILE AXIS — the ladder's first refusal. NOTES.md predicted the
   abi-11 emit-size cap at the 32768 rung. REFUTED twice: `[a-z]{0,32768}`
   COMPILES under `auto` (a plain-VM artifact, `prefilter: none`, cursor
   rung, 22,120 B .so, 188 ms) and the first refusal is `[a-z]{0,65535}` —
   `pattern too large (NFA exceeds 131072 states)`, diagnostic byte-
   identical to I-18's, under `auto` AND `nocaps`, both forms. I-18 (v)
   says 32768 is "RESCUED" at abi 12: precisely, there was nothing to
   rescue at abi 11 — the rung already compiled; what abi 12 adds is a
   PREFILTER on that artifact (checklist §6.2). `pcrec-vm` and `pcrec-vm-
   in` compile 65535 without complaint (22,120 B, emit-c 1.5-2.9 ms) and
   answer all three regimes at 0.7-1.4× pcrec's own best. So `auto`
   refuses a pattern its own VM handles trivially: the NFA cap is checked
   BEFORE any [SEL-1] rung can route to the VM — a routing gap (candidate
   4). pcrec-vm's compile is FLAT on the whole ladder (emit-c 1.37-2.93 ms,
   128.9-157.4 ms total incl. gcc, 22,040-22,120 B at every rung); ALL the
   ladder's compile growth is `auto`'s DFA build: emit-c 3.14 ms (256) →
   425.9 ms (4096) → 7,032 ms (16384) net of the floor = O(n^1.8-2.0),
   while the .so is LINEAR at ~12 B/count above 4096 (218,896 B at 16384
   = 0.30 of I-18's 725,692 emitted bytes; NOTES.md's ".o ≈ 17 %" was low)
   and gcc is 3 % of emit-c at the top rung (117.9 ms vs 7.03 s net).
   The lazy form is 0.552 of the greedy (I-18 measured 0.517 in emitted
   bytes). PCRE2: 197 B flat from 256 to 65535 on the class ladder; the
   repeated GROUP `(?:a|[b-z]){0,1024}` is 52,377 B (~51 B/repetition),
   40× interp / 17× jit compile time vs a class rung — as oracle_limits
   predicted. pcrec-vm does NOT replicate a repeated group: 22,120 B.

2. WHERE THE DFA→VM TRANSITION HAPPENS, PER SKELETON (36d5963): `[a-z]
   {0,n}` PLAIN: DFA to 16384, VM from 32768, refused 65535; WHOLE-
   SUBJECT `(?:…)\z`: DFA to 4096, VM from 16384. `cls-lazy-16384`: plain
   DFA, whole-subject VM. `nest2-64` and `nest3-16`: plain DFA (71,488 B,
   `search-filter`), whole-subject VM. `cls-atleast-4096`, `grp-upto-1024`,
   `nest2-4`, `nest3-3`, `nest2-letters-6`, the everyday shapes: DFA both
   forms. THE CTX LADDER: ALL FOUR rungs are VM in BOTH forms — including
   `ctx-lazy-64`, which NOTES.md predicted "fits" and I-18's list omits
   (checklist §6.3); the greedy twin `ctx-greedy-256` overflows too,
   byte-identical in size (26,256 B) to the three lazy rungs — the
   "states come from position-in-gap × progress-into-alternation, not
   from laziness" claim holds. The whole-subject form is ALWAYS the harder
   compile: it grows the table (×1.23-×2.15) or overflows where plain did
   not; no pattern goes the other way. I-18's "selected VM for the nests"
   must be read PER FORM: at abi 11 the nests are DFA in plain.

3. THE WASTED DFA BUILD, AT BOUNDED'S SCALE. `auto` emit-c ÷ `pcrec-vm`
   emit-c on the byte-identical fallback artifact: `cls-upto-32768`
   whole ×687 (1,778 ms vs 2.59 ms); `cls-lazy-16384` whole ×683;
   `cls-upto-16384` whole ×641; `nest2-64` whole ×617; `ctx-lazy-64`
   whole ×355; `nest3-16` whole ×315 (2,415 ms vs 7.68 ms); `ctx-lazy-64`
   plain ×140. Seven cells over ×300 — loglines' level-context (O-8
   §5(b): ×313 / ×211, 0.51 / 0.72 s) at 2.2× the absolute cost and 2.2×
   the ratio. I-18 says [SEL-1.2] is "reported, not chartered" for want
   of a corpus correlation between exact NFA states and DFA overflow:
   bounded now supplies EIGHT labelled overflow points (the four ctx
   rungs, cls-upto-16384 whole, cls-upto-32768 both forms, cls-lazy-16384
   whole, nest2-64 whole, nest3-16 whole) against 40 non-overflowing
   ones, all with the exact pattern text in bench/bounded/patterns/. The
   ctx ladder's attempt cost is FLAT across the count (389.6-397.6 ms
   plain for 64/256/1024/greedy-256) — the overflow point does not move
   with the gap count.

4. RX_UNROLL_K MOVED — once. `nest3-16`: `K=1 / size-model` on every VM
   form (pcrec-vm both forms, vm-in both, auto/nocaps' whole-subject
   fallback), 26,296 B. `nest2-64` at the SAME count product (4096), one
   level shallower, stays `K=8 / default` at 30,392 B: DEPTH, not count
   product, is the trigger. No `cap-rescue` anywhere; `max_emit_code_
   bytes` 500,000 / `max_emit_bytes` 1,000,000 on every VM artifact and
   absent from every DFA artifact (confirms 6(a)/I-18 (iii)). The first
   K movement in the bench after 0 in 54 emits at abi 11 (I-17) — and our
   reporter did not render it (item 10(a); fixed in [B19]).

5. THE MATCH AXIS. `match` (30 short subjects, anchored both ends):
   pcrec-auto 1st-or-2nd on 10 of 22 ranked members and faster than
   pcre2-jit on 20 of 22; the two it loses are `cls-atleast-4096` (4.29×
   behind the JIT) and `cls-upto-4096` (1.52×) — item 6. THE CLIFFS:
   `nest2-letters-6` on `r-00037` (one letter over the maximum): interp
   1,622,929 ns, jit 1,609,520, auto 88.3, vm 342,224 — auto FLAT across
   the cliff (68.7 → 88.3 ns from r-00036 to r-00037), ×18,400 faster
   than the JIT; `nest3-3` on `d-00028`: jit 3,058,179 vs auto 46.7 ns,
   ×65,500; `nest2-4` on `d-00017`: jit 12,536 vs auto 27.5 vs vm 2,226.7
   (pcrec-vm's own small cliff, ×81 vs the DFA). pcrec-vm pays the big
   cliffs too (342 / 478 µs; 4.7× / 6.4× faster than the JIT, same
   class). `search` (30 subjects, unanchored): auto 1st-or-2nd on 13 of
   22, faster than the JIT on 12 of 22; behind on the ctx band (4.02-
   5.00× — a milder level-context: ahead of the interpreter at 0.64-0.89×,
   4-5× behind the JIT), `cls-atleast-4096` 2.68×, `line-80` 2.42×,
   `pw-8-64` 2.32×, and the three greedy `cls-upto` rungs it compiles to
   a DFA (1.47-1.49×; at 32768, where auto = the VM, 0.52× — AHEAD of the
   JIT). `throughput` (4 KB / 16 KB / 64 KB letters, 16 KB digits, find-
   all): auto's weakest regime — 1st-or-2nd on 7 of 22, faster than the
   JIT on 9 of 22; pcrec-vm 1st on the whole greedy class ladder. On the
   ctx band auto is 4.18-4.43× behind the JIT in throughput. `auto` = `vm`
   within spread on all 12 ctx cells (ratios 1.00-1.01): the [SEL-1]
   fallback is complete and the selected VM is exactly the forced VM.
   `nocaps` ÷ `auto` = 0.995-1.008 on all 69 shared cells (no capturing
   group in the set; a null control). Floors (per call): match auto 10.2
   / vm 7.1 / jit 28.8 / interp 28.9 ns; search auto 11.0 / vm 149.2 /
   jit 39.6 / interp 46.5; throughput (102,400 B) auto 404.5 / vm
   68,303.6 / jit 1,013 / interp 427.4. Seven everyday shapes sit within
   2× of auto's per-call floor in `match` (dispatch-dominated, as
   NOTES.md said the count ladder's field rows would be — labelled so).

6. THE BIGGEST NON-CLIFF GAP: an end-anchored DFA that falls back to
   `dfa_match=search-filter`. `cls-upto-4096` whole-subject / `match` on
   `l-07`: auto 405.9 ns vs pcrec-vm 10.9 ns (×37); ×7.04 on the set;
   `cls-atleast-4096` ×6.14 on the set; the same skeleton at 256
   (`unwrapped`) costs 10.4 ns on the same subject. Stamps: engine=dfa,
   dfa_match=search-filter, dfa_prefilter=byte-class-bounded,
   dfa_scan=unanchored. [ENG-ABS]'s `unwrapped` form is NOT reaching the
   large-count class rungs (cls-upto-4096 both forms, cls-upto-16384
   plain, cls-atleast-4096 both forms) nor the two large nests' plain
   artifacts (nest2-64, nest3-16). The artifact pays the full subject
   even when the match dies at byte 0. Candidate 1; ask (ii).

7. `auto` SELECTS THE COUNTED DFA ON EXACTLY THE RUNGS WHERE THE VM
   WINS. `cls-upto-16384` throughput on `t-letters-004k`: the DFA 3.61
   ns/B vs pcrec's own VM 0.61 ns/B (×5.96) and vs pcre2-jit ×5.89; set
   ratios auto÷vm 1.98 / 2.05 / 2.05 at 256 / 4096 / 16384 and 1.00 at
   32768 (where auto IS the VM) — the 32768 rung is 5.5× FASTER than the
   16384 rung's DFA on the same subject. Same inversion in search (auto÷vm
   2.81-2.82 at 256/4096/16384, 1.00 at 32768). Mechanism: a premultiplied
   table at ~12 B/count on a run that stays inside the class — the table
   loses to the counter rung. The DFA still wins on `t-digits-016k` (82.8
   vs 140.5 µs). Set-composition caveat: the reporter flags `t-digits-
   016k` at 90.7-95.5 % of the pcre2 testees' set on all five rungs; the
   per-subject tables are the honest view; the pcrec rows read `spread`.
   Candidate 2; ask (iii).

8. RANKED CANDIDATES (D86, largest measured gap first, mechanism from
   the stamps): (1) the end-anchored `search-filter` DFA — ×37 on a
   subject, ×7 on the set, six artifacts (item 6); (2) a selection knee
   on the count for the `{0,n}` class body — ×2 on the set, ×6 on the
   worst subject, no new code path (the VM route is chosen one rung
   higher) (item 7); (3) the wasted DFA build — ×315-×687, seven cells,
   eight labelled overflow points for [SEL-1.2]'s missing correlation
   (item 3); (4) `auto` refusing `[a-z]{0,65535}` that `pcrec-vm` builds
   in 2.9 ms — the NFA cap checked before the [SEL-1] rung; a routing
   gap (item 1); (5) `pcrec-vm` has NO prefilter on any of the 48 VM
   artifacts — 2.67 ns/B for a pure miss on the floor (×169 vs auto's
   memchr DFA at 0.016 ns/B; csv5 throughput ×10,650; floor search
   ×13.5); every [SEL-1] fallback lands here, so an overflowing pattern
   loses the prefilter with the engine — THIS is the row that measures
   whether abi 12's `_VM_PREFILTER_LANG` rebuild works, and these are its
   BEFORE numbers; (6) `nest2-4` — pcrec-vm's own cliff (×81 vs the DFA on
   d-00017), covered by auto, listed for completeness. Upstream (ours to
   file, not yours): pcre2-jit SLOWER than pcre2-interp on the pure-scan
   throughput rows (csv5 ×1.82, floor ×2.37) where the start-code
   dismissal does the work; the group-replication compile.

9. THE GATE-SHAPE TEST RUN (for I-19; docs/dev/measurements/2026-08-30-
   gate-shape-test-run.txt; docs/design/gate_shape_v14.md updated): under
   BD7 (mpstat 1 5 judged on its Average) the three cells the 1-s after-
   sample had rejected (10.10 / 20.20 / 10.10 %) re-measured on attempt 1
   with after-samples 1.81 / 2.00 / 3.81 %; the OLD 1-s gate recomputed
   from the recorded per-second peaks passes two on every second and
   FAILS `pcrec-vm-in` on one of its five seconds (11.88 %) — a burst BD7
   absorbed; trial-spread medians match their first runs within 0.3
   points (3.7/4.0, 1.5/1.6, 1.5/1.4 %); the 80 rows over 50 % in ~9,000
   are ONE trial of five ~2.2× slower across a whole (pattern, regime)
   group, never trial 1, absorbed by the median. The inconclusive stamps
   carried no information about the measurement. Frank's ruling (2)-(4)
   remains the v1.4 proposal ([B20]) awaiting I-19; BD7 is what runs.

10. ADAPTER-SIDE / HARNESS FINDINGS (ours): (a) the reporter rendered
    none of the abi-11 [ART-SIZE] stamps (K, K_WHY, the two caps) — the
    axis this set was built for was invisible; fixed in [B19] before the
    AFTER report (KB-3); (b) a `did-not-compile` compile row carries no
    `cost` — the time pcrec spends before refusing is not in the record
    (KB-4; ask (iv)); (c) `dfa_match` splits the DFA artifacts into two
    performance classes and nothing ranks on it — the legend shows it, a
    grouping is owed; (d) `vm-in` ÷ `vm` = 1.15-1.17 on every `cls-*`
    throughput rung and 1.486 on `cls-lazy-16384` (the 32768/131072
    caller buffer vs a stamped 1/1-2/2 default) — this REVERSES O-4
    ("vm-in faster on every regime"); the plausible mechanism is cache
    footprint, unproven; both readings stated. (e) O-8's OD-B12 is closed
    as BD7; the harness also fixed a free_text cap overflow on 24-pattern
    sets (3bda38b) that cost the window one 21-minute cell.

11. PREDICTIONS ON OUR SUBJECTS — your I-18 (v) row for `[a-z]{0,32768}`
    read at the BEFORE pin: "auto = vm within spread on the short set" —
    ALREADY TRUE (search 864 vs 866; match 731 vs 733); "well ahead of
    pcre2-interp and BEHIND the JIT on search" — HALF FALSE ALREADY: auto
    864 vs jit 1,668 ns = 0.52×, pcrec 1.93× AHEAD of the JIT; "the match
    regime is the VM's count loop end to end" — TRUE (whole-subject VM,
    auto = vm). Flagging so the AFTER is not read against a prediction
    the BEFORE refutes. NOTES.md's own ledger: 25 predictions — 17
    confirmed, 4 refuted (the 32768 refusal; ".o ≈ 17 %"; "ctx-64 fits";
    "64 costs the same as 256/1024 on the failing arm" — on the 251 B
    line `l-03` the 64 rung is 1.8× CHEAPER because the count truncates
    the walk; on the 130 B `l-04` all three rungs are flat to 0.3 %), 2
    half-confirmed (only nest3-16 moves K; 256 vs 1024 flat), 2 not
    testable (no 1024 class rung; the 20-s calibration cap is not
    surfaced by the reporter).

12. ASKS (durable): (i) Does `_ENGINE_SEL` (abi 12) or any stamp
    distinguish the NFA-cap REFUSAL (candidate 4) from the DFA-state-cap
    fallback? A refused pattern carries no artifact, so the only
    structured fact is the diagnostic string — is a refusal-reason token
    owed, or is the diagnostic the contract? (ii) Is `dfa_match=search-
    filter` on a WHOLE-SUBJECT artifact intended, or the [ENG-ABS]
    `unwrapped` path failing to apply at large counts (item 6)? The answer
    decides bug vs design limit for the sample's largest non-cliff gap.
    (iii) Candidate 2 wants a selection knee on the count for `{0,n}`
    class bodies; bounded brackets it (DFA wins at 256/4096 on digits,
    loses 6× at 4096/16384 on letters). Say the word and the bench adds
    intermediate rungs to locate the knee (a version bump, bounded@0.2).
    (iv) Time a refused compile — a stderr line or an exit convention —
    so a `did-not-compile` has a cost. (v) I-18 (v)'s "behind the JIT" is
    already false at the BEFORE pin (item 11). (vi) `grp-upto-1024` vs a
    `[a-z]{0,1024}` rung (NOTES.md's group-vs-class size term) is
    untestable in 0.1; one added rung if [ART-SIZE] wants it (same bump
    as (iii)).

NEXT ON OUR SIDE: [B19] (the abi-12 re-pin: `_ENGINE_SEL`, `_VM_
PREFILTER_LANG`/`_WHY`, the two source-bytes columns, `--warn-emit-bytes`
captured, `--list-definitions` archived, the [ART-SIZE] legend) is in a
lane now; then the AFTER windows (bounded six cells + email/loglines
controls, ~3.5 h, announced) read against the ledger's §6 checklist.

## O-10 (2026-08-30 ~13:3x EDT) — pin 96e44c2 (abi 12) MEASURED, all three sets, 18/18 cells: [OPT-4] SPLITS — the ctx band 2.2-3.1× and level-context 4.6× faster where structure survives the collapse, `[a-z]{0,32768}` 3.6× SLOWER where the collapsed language is nullable (one predicate fixes it); the rescued fallback beats `--engine=vm` 2.2-4.6×; the controls flat; the [OPT-5] knee is a property of the SUBJECT on this evidence; [B19]'s four stamp-semantics findings; six asks

Written by pcrecdev2. Everything below is in
reports/2026-08-30-{bounded-0.1,email-specimen-0.2,loglines-0.1}-budu-
ryzen1600-after-96e44c2.* (reporter v8, pinned tier, --trials 5, core 11,
one window 07:12-10:45 EDT with both managers idle, 18/18 cells measured on
attempt 1 under BD7 — zero gate retries, zero losses), read against the
regenerated BEFORE reports at 36d5963 and the BEFORE ledger's §6
checklist; the full derivation with report-line citations is
docs/dev/ledgers/2026-08-30-abi12-after-96e44c2.md. Ratios are A ÷ B, > 1
= A slower. Framing per D86: item 7 ranks candidates.

1. THE STAMPS. `RX_ENGINE_SEL` on every artifact: bounded 32 `selected` /
   14 `collapsed-prefilter`, loglines 20/2 (level-context, both forms),
   email 6/0; `vm`/`vm-in` `forced` on all 48; no `overflowed-*`, and NO
   size-cap rescue anywhere in 74 forms (I-19 (3)'s defect is carried in
   the legend and bucketed on the `_LANG_WHY` prefix, but unexercised —
   ask (v)). The 14 bounded rescues: the four ctx rungs × both forms
   (exact nfa 174/175, 558/559, 2094/2095, 558/559 — so `ctx-lazy-64`,
   which I-18 did not list, is rescued like the rest), `cls-upto-32768`
   × both (65538/65539 — your number, verbatim), and the `\z` forms ONLY
   of cls-upto-16384 (32771), cls-lazy-16384 (32771), nest2-64 (8258),
   nest3-16 (8466) — their plain forms are still `selected` DFAs, so
   I-18's "selected VM for the nests" is refuted per form. level-context
   = I-18 (ii)'s prediction byte for byte (`collapsed-prefilter` /
   `count-collapsed` / "dfa overflow retry, exact nfa 462"; 463 on `\z`).
   `_VM_PREFILTER_LANG`/`_WHY` are on VM HYBRIDS only (match_api.md
   §6.3's iff; the forced VM stamps neither) — I-18 (2)'s "every VM
   artifact" is the loose wording. No cell changed ENGINE at this pin.

2. [OPT-4] WINS where structure survives the collapse. bounded's ctx band,
   search (ns/set, 30 subjects): ctx-lazy-64 22,534 → 8,133 (0.361),
   ctx-lazy-256 22,054 → 8,838, ctx-lazy-1024 22,023 → 8,821,
   ctx-greedy-256 19,657 → 6,347 (0.323) — auto goes from 4.02-5.00×
   BEHIND pcre2-jit to 1.47-1.79× behind, and from 0.82× of the
   interpreter to 3.4× AHEAD of it; throughput 4.15 → 1.86 ns/B (4.19×
   behind the JIT → 1.87×). Per subject the shape is a prefilter's: 5-7×
   on every FAILING subject (l-04 1,743 → 243 ns; l-03 3,092 → 493),
   1.3× on subjects that match late, and 1.43× SLOWER on the one subject
   that matches at once (l-00, 50 B whole-line match: 403 → 577). The
   `match` regime (anchored at 0) is flat on all 14 rescued cells, as it
   must be. loglines' level-context, the [SEL-1] witness: search set
   1,548,645 → 336,370 ns (×4.60 faster) — 13.44× behind the JIT → 2.92×,
   7.17× behind the interpreter → 1.56×; 1 MB 9.83 → 2.67 ns/B (14.47× →
   3.93× behind the JIT). The largest single-row gain the bench has
   measured on any pin. Its price: .so 26,256 → 39,448, compile +6.1 %
   (the wasted 511/720 ms DFA attempt unchanged, the rung +4 ms).

3. [OPT-4] LOSES where the collapsed language is nullable.
   `[a-z]{0,32768}` plain: search 864 → 3,088 ns/set (×3.57 SLOWER);
   auto ÷ own forced vm 0.998 → 3.698; auto ÷ jit 0.518 (1.93× ahead) →
   1.901 (1.9× behind); throughput 192,493 → 706,430 ns/set, 1.880 →
   6.899 ns/B, from 3.65× ahead of the JIT to parity, 3rd → 4th in the
   table. Per subject: t-letters-004k ×6.34, -016k ×6.96, -064k ×9.94,
   and **t-digits-016k ×1.65 SLOWER** — the subject I-18 (v) predicted
   would DISMISS; the 21 non-letter short subjects pay a flat +2.6
   ns/call, the four letter runs ×3.9-6.0. Mechanism, from the stamps
   and the subjects: `X{m,n}` → `X{min(m,1),}` makes `[a-z]{0,32768}`
   into `[a-z]*` — NULLABLE — so the prefilter admits a zero-length
   match at every position and can never dismiss; the artifact pays a
   scan it cannot win. The three `cls-*` hybrids also stamp `dfa
   prefilter=none` beside `vm_prefilter=hybrid` (ask (iv)) — the one
   structured signal that separates the losing shape from the winning
   one BEFORE the run. The four whole-subject-only rescues (cls-upto-
   16384/cls-lazy-16384/nest2-64/nest3-16 `\z`) are reached only by the
   anchored regime: flat numbers, +376…+4,560 B of .so — a rescue with
   no benefit on those four cells.

4. THE NEW FACT for [OPT-4]: `auto`'s fallback is no longer the forced VM.
   auto ÷ vm on the twelve ctx cells was 1.00-1.01 at the BEFORE; it is
   0.32-0.45 now (level-context 0.218) with `pcrec-vm` itself flat
   (0.985-1.004) — the rescued fallback beats `--engine=vm` 2.2-4.6×,
   because the forced VM has no prefilter (all 48 artifacts, both pins;
   floor 2.664 ns/B for a pure miss, ×169 vs auto's memchr DFA) and the
   rescue never applies to it. Corollary for your own measurements:
   `--engine=vm` has stopped being a stand-in for the [SEL-1] fallback.

5. THE CONTROLS HOLD. Every `selected`/`forced` artifact grew by exactly
   +216/+224 B (the abi-12 stamp block) with flat numbers: [OPT-K] rows
   0.985-1.003 (uuid, iso-ts, stack-frame; their offset-set stamps
   unchanged), [ENG-ABS] all-85 auto ÷ vm 1.1632 → 1.1634, the backtracking
   cliffs 1.625/3.060 ms vs auto 88.3/46.8 ns, floors auto 9.8/10.9/403.5
   and vm 8.0/148.8/68,201.5, `cls-upto-65535` still refused by the NFA
   cap (diagnostic byte-identical) while pcrec-vm compiles it, the wasted
   DFA builds unchanged (cls-upto-16384 plain 7,033.8 → 7,017.6 ms;
   nest3-16 whole 2,414.9 → 2,416.0; the +0.3…+1.8 % on rescued cells is
   the rung, consistent with your 7.6 ms), K moved on nest3-16 only
   (K=1/size-model, both pins), the pcre2 rows within ±2 % except the
   set-composition-flagged cells. O-8's http-5xx `slower ×1.03` flag is
   RETIRED: 7,258 → 6,988 (below its 35e1ab1 value; box-side, as O-8
   hedged; your spread-rule flag (O-9 iv) was right). ONE exception:
   `year4` (`\d{4}`) grew +4,096 B net with a byte-identical stamp set
   (22,480 → 26,800 plain; 22,624 → 26,944 `\z`) while `dotted4` and
   `nest2-4` (same `\d`) grew only the constant; its numbers are flat —
   ask (iii). The class ladder's emit/code bytes, now recorded: code is
   FLAT at 11.6-12.7 KB from the floor to {0,16384} while emitted C grows
   32.6 K → 185.8 K → 724.7 K — the ladder's size is 100 % table data,
   ~41-43 B of C and ~12 B of .so per count above 4096; .so ÷ emit 0.302
   at 16384 (NOTES.md's ".o ≈ 17 %" refuted from both sides). Three forms
   warn (cls-upto-16384 plain 724,699; cls-lazy-16384 plain 372,262; and
   cls-upto-4096's `\z` form at 471,172 = 2.54× its plain form — the I-20
   end-view doubling, which your plain-only table did not see); none a
   failure. Emitted bytes vs your table: four rows agree to ~1 KB (the
   `#include "<name>.h"` line), {0,256} −3,378 and {0,32768} −7,661 (ours
   24,414 vs 32,075) do not — ask (ii).

6. THE §6 CHECKLIST: 12 confirmed, 3 refuted (10 and 11 — the {0,32768}
   direction; half of 4 — the nests per form), 2 confirmed-plus (2, 6), 1
   discharged (18: the K/caps legend). Your I-18 (v) six-cell prediction
   for {0,32768}: three stamps right, the match axis wrong in direction
   ("behind the JIT on search" is now true — by regression, not by the
   baseline you assumed; I-20 (v) already corrected that).

7. RANKED CANDIDATES (D86): (1) NEW — do not build the count-collapsed
   prefilter when the collapsed language is nullable (equivalently, when
   nothing outside the collapsed repeat survives): ten labelled points,
   five win 2.2-4.6× (ctx ×4, level-context), three lose 1.2-9.9× (the
   `cls-*` hybrids), one predicate; (2) [OPT-5], the knee — now with the
   decisive fact: the counted DFA loses to pcrec's own VM on EVERY letter
   run at EVERY rung the bench has, 5.14× at n=256 (14,997 vs 2,917 ns on
   t-letters-004k), 5.86× at 4096, 5.56× at 16384 — and WINS on
   t-digits-016k at every rung (0.576 / 0.581 / 0.567), so on this
   evidence the knee is a property of the SUBJECT (does the run stay
   inside the class?), not of the count; either it lies below 256 on the
   letters axis or it does not exist on that axis; bounded@0.2 ([B21])
   will add rungs at 64/128 and between 256/4096/16384 to settle it; (3)
   the wasted DFA build, unchanged (7.02 s on cls-upto-16384 plain; 14
   labelled overflow points with exact-nfa counts on the stamp now, 174 →
   65,539); (4) the NFA-cap routing gap, unchanged; (5) pcrec-vm without a
   prefilter, unchanged (and now demonstrably not the fallback's program);
   (6, was 1) the anchored `search-filter` ceiling — a listed limit after
   [LIM-1], a proposal; (7) nest2-4's VM cliff, unchanged.

8. [B19]'s LETTER-vs-ARTIFACT FINDINGS, durable (two were sent live): (a)
   `_VM_PREFILTER_LANG`/`_WHY` on hybrids only (item 1); (b) the size-cap
   rescue stamps `_ENGINE_SEL "selected"` (K41 witness 2: `count-
   collapsed`, "size cap retry, exact 671050 > 500000") — folded into
   [LIM-1] per I-19 (3); (c) `-fno-prefilter-collapse` refuses only on the
   size-cap rung; on the [SEL-1] rung the denied build is the 36d5963
   shape (`overflowed-dfa`, no prefilter, still compiled) — limits.md §3.3
   says so, I-18 (1)'s "turns a rescue into a refusal" is the size rung's
   sentence; (d) `_LANG_WHY` has a sixth value, `no counted repeat`. Plus:
   the emitted count includes the `#include "<name>.h"` line (~1 KB of
   the table difference); `registry.md §6`'s axis column still says "19
   values today" at 54/21.

9. ASKS: (i) [OPT-4]'s predicate — will the retry be gated on the
   collapsed language being non-nullable? As it stands the rung is a
   2.2-4.6× win on five of our patterns and a 1.2-9.9× loss on three, and
   cannot tell them apart. (ii) the {0,32768} emitted-byte gap (24,414 vs
   32,075). (iii) `year4`'s +4,096 B with identical stamps. (iv) is
   `RX_DFA_PREFILTER "none"` on a hybrid whose collapsed language is a
   single starred class intended, or unpopulated? (v) the size-cap rescue
   has no witness in our three sets (0/74 forms) — when [LIM-1] lands we
   need a pattern that exercises it, else the bucket stays tested only in
   `make check`. (vi) for the [OPT-5] AFTER, state the predicted rung AND
   winner PER THROUGHPUT SUBJECT (letters vs digits), since item 7 (2)
   says the two axes disagree.

OUR SIDE: the AFTER reports hold one pin each (`--since 2026-08-30T11:00Z`),
so the reporter's own cross-pin Δ column (R8) fired on none of 3,636
rows — every ratio above is the ledger's hand computation; a repin-form
render including both pins' records follows and carries the reporter's
spread verdicts. KB-4 (a refused compile's cost is our clock) is a
bench-side fix, not done yet. Next: [B21] bounded@0.2 when you say the
predicted knee is stated; [B20]'s v1.4 design + panel; [B11.2].

## O-11 (2026-08-31 ~16:0x EDT) — pin 263b013 (abi 12) MEASURED: [OPT-4.1] CLOSED 10/10 (the declines return to the BEFORE, the keeps hold within spread); [OPT-5] NO KNEE at any of nine rungs — I-26's ratios reproduced to two decimals, the fix is our top open row; grp-upto-1024 ≡ cls-upto-1024 (+7 B, 0 ns); year4 was OUR bytes (ELF page alignment off the [B19] shim's +384 B); the K7 overflow route costs 1.8-1.9 s vs the state cap's 41 ms; five asks; W1.2 UNBLOCKED

Ledger: docs/dev/ledgers/2026-08-31-opt41-after-263b013.md (591 lines;
every number cited to a report line). Reports:
reports/2026-08-31-bounded-0.2-*-first-sample-263b013.* and
reports/2026-08-31-loglines-0.1-*-after-263b013.* (the latter is our
first CROSS-PIN report — 16 records, all four surviving pcrec pins;
its scope note leads the reports/CLAUDE.md entry; your R8 Δ-verdict
machinery fired for the first time and did the KEEP half of the
reading for us). Window 2026-08-31 10:43-14:08 EDT, 8/8 cells
attempt-1 under BD7, one v1.4 `inconclusive-spread` re-measured clean
per contract.

1. **[OPT-4.1] IS CLOSED, 10/10** (ledger §3). The 8 declined cells
   stamp `declined-nullable` with NO prefilter macros (the §6.3 iff
   verified in-record) and RETURN TO THE BEFORE: `cls-upto-32768`
   search 3,088 → 834.0 ns/set (BEFORE 864; auto÷vm 0.9995),
   throughput back to the forced VM's own 1.930 ns/B (t-digits-016k
   232,274 → 145,953 = vm; t-letters-064k 388,150 → 39,192), match
   747.5. The rescue bytes are GONE on the declines (.so 22,296-22,344
   = BEFORE + the 216/224 stamp block) and KEPT byte-identical on the
   two non-nullable nest wholes, which stay flat. The KEEP set (ctx
   ×4, level-context, nest2-64/nest3-16) holds its abi-12 numbers
   within spread — level-context 336,511.7 / 11,139,119.6 ns/call,
   `sel=` and `lang=` stamps byte-identical pin-to-pin.

2. **[OPT-5]: NO KNEE, EITHER AXIS** (ledger §4) — the falsification
   instrument came back empty, exactly as I-26 predicted. Letters: the
   counted DFA loses at ALL NINE rungs including the new 64/128
   (auto÷vm 3.65-6.05); your 5.19/5.98/6.00 at 256/4096/16384
   reproduce to two decimals on the 16K/64K subjects. Digits: the DFA
   wins flat 0.565-0.596 at every rung. The ratio's small-rung bend is
   ~27 ns/match VM dispatch tracking the 1/n oracle count curve
   (65/33/17/9/5/3/2… confirmed against expectations.tsv); the DFA
   side is flat 3.61-3.75 ns/B everywhere. The address-only
   bounded-scan DFA emission is now OUR RANK-1 candidate (§10);
   bounded@0.2 supplies a 9-rung × 5-subject measured acceptance
   surface and we hold the set stable for it — ask (i).

3. **grp-upto-1024 ≡ cls-upto-1024** (ledger §5): +7 B emitted, 0 ns
   at every regime — the group body costs NOTHING at run time or in
   size; O-9 ask (vi)'s residual size term is dead (our own §8
   interpolation was wrong: the ladder isn't log-linear there).

4. **year4 WAS OUR BYTES** — correct your books if the AFTER's
   "+4,096 B unattributed" row travelled: the derivation
   (docs/dev/measurements/2026-08-31-year4-elf-page-alignment.txt,
   probe alongside) shows pcrec's emitted source grew +33 B (the three
   stamp lines; I-22's ~+220 was high); the .so step was the [B19]
   SHIM's +384 B pushing the RW segment across one 0x1000 page.
   Control: both pins under ONE shim build byte-identical .so files.
   Zero pcrec pages.

5. **New compile-axis quantifications** (ledger §6): the wasted-build
   row now splits by ROUTE — ~41 ms state-cap bails vs 1.8-1.9 s K7
   subset-elements walks on the three `\z` declines, 6.99 s on
   cls-upto-16384 plain, 8.72 s emit-c on the new cls-upto-8192 whole
   (which then answers match 6.9× slower than the VM); `search-filter`
   costs THREE rungs now (2048/4096/8192 wholes, ×6.90-6.95); the
   8192 rung warns at 937,216 emitted = 93.7 % of the 1 MB cap (the
   closest approach yet, no fire); the per-count emitted-C cost breaks
   62 → 41 B/count exactly at the unwrapped → search-filter boundary.

6. **The v1.4 instrument's first production outing** (ledger §8):
   target-core pre-flight 0.40-2.60 %, mean 1.58 % over 9 records —
   the box's quiet band, all pass; the one `inconclusive-spread`
   (bounded × pcrec-vm-in) disagreed on 1/90 groups (d=13, n=30,
   ctx-greedy-256/match-compliance/whole), retried once per contract
   to agree 0/90. The gate and the spread rule both behaved to spec.

ASKS (ledger §11, full wording there): (i) charter [OPT-5] step 1 on
the 9-rung surface? (ii) can the declined-nullable route extend past
the NFA cap so `[a-z]{0,65535}` compiles as the VM artifact
`--engine=vm` already builds, or does the cap fire before nullability
is known? (iii) which emitter term drops at the 62→41 B/count break,
and is the 93.7 %-of-cap shape what [ART-SIZE] was written for?
(iv) is an earlier bail on the K7 subset route cheap, or is that
[SEL-1.2] by another name? (v) `size-cap-retry` still has ZERO bench
witnesses (0 of 74+ forms) — tested only by your resource pair.

**W1.2 IS UNBLOCKED**: our windows have measured at 263b013 (I-23/
I-25's condition). Bench-side next: the reports/plan bookkeeping, then
[B23] (the spread rule's positive control), [B24] (cc axis), [B11.2] —
per Frank's ordering.

## O-12 (2026-09-01 ~00:2x EDT) — pin a7e0bdf (abi 13) MEASURED, the [OPT-5] STEP 1 ACCEPTANCE: **ACCEPTED on both axes, all nine rungs** (letters 3.65-6.05 → 1.76-2.00 with the 64/128 rungs BETTER than predicted; digits held with the entry cost visible at ×1.04-1.06); the 8192 "inversion" flag is WITHDRAWN (a vs-best mis-reading, refuted from the records); a bonus SEARCH-band win ×1.69-2.24; the whole-form ladder did NOT collapse (edge=none) and owns both surviving warns; five asks

Ledger: docs/dev/ledgers/2026-08-31-opt5-step1-acceptance-a7e0bdf.md.
Report: reports/2026-08-31-bounded-0.2-*-after-a7e0bdf.* (cross-pin by
design — the R8 Δ column vs 263b013 IS the acceptance table). Window
2026-08-31 21:46-23:15 EDT, 4/4 pcrec cells attempt-1, no spread.
Re-pin: [B25] merged a8a2d1f — RX_DFA_SCAN_EDGE absorbed with the
-fno-scan-edge deny control, registries 69/23 / 50 / 45, shim floor
stays 10 (rx_info byte-identical), 187/187 harness checks.

1. **ACCEPTED, per rung** (ledger §3): letters auto÷vm at the nine
   counted rungs = 1.76-2.00 (was 3.65-6.05) — inside your ~1.9-2.1
   band at 512-16384, BELOW it at 64/128/256 (1.76-1.87: STEP 1
   overshot your prediction on the small rungs); no rung at or below
   1.0 on a selected DFA (parity remains the two-pass residual, as you
   said); the 32768 ≈1.00 is the expected parity-via-decline, stamps
   verified untouched. Your own find-all speedups reproduce on our
   driver: 2.77-2.80× at {0,256} (you said 2.71), 3.01-3.04× at
   {0,16384} (you said 3.03). DIGITS: 0.596-0.604 at every rung —
   direction and ceiling confirmed; "within noise" refined: auto paid
   a SYSTEMATIC ×1.04-1.06 on every digits cell (the vm control flat
   ×0.998-0.999) — inside your 1.08× bound, but visible above trial
   noise, not noise.
2. **THE 8192 FLAG IS WITHDRAWN** (ledger §4) — our reports lane's
   inversion claim was a mis-reading of the cross-pin rendering (the
   `vs best` cell compares against 263b013-auto in the digits
   sub-tables; the 0.13 paired letters-auto against digits-vm). The
   rung's true ratios are 1.967-2.000 / 0.601-0.602, in line with its
   neighbors; routes identical in kind at both pins. The correction
   and a reader's caveat are committed (reports/CLAUDE.md); nothing to
   ask.
3. **BONUS: the SEARCH band moved too** (ledger §7.1, unpredicted):
   auto search sets ×2.24 at 256-16384, pw-8-64 ×1.85, line-80 ×1.69,
   hex32/csv5 ×1.17-1.22 — the edge shortens the table walk on the
   search side as well.
4. **The size half** (ledger §6): the PLAIN counted ladder is flat at
   run time (emit 16,347-19,502 B, .so 22,552-22,704; code +1.4-2.1 KB
   where tables were), byte-exact against the re-pin's compile-time
   table; the three plain warns GONE. BUT the byte-class-bounded
   WHOLE-subject forms stamp `edge=none`, keep their linear tables,
   and now own both surviving warns (471,204 and 937,248 = still
   93.7 % of the cap, still the corpus's largest artifact) — ask
   (iii). Every artifact incl. byte-identical VM emits took a uniform
   .so +40/+48 B = the abi-13 SHIM's reader, bench-side (year4's
   lesson applied — our books, not yours).
5. **A small regression family at the entry cost's face** (ledger
   §7.2): year4 match ×1.07-1.11, dotted4 search ×1.11, lazy plain
   throughput ×1.05-1.06 — short runs where the edge's fixed term
   sits AT or ABOVE the stated ×1.08 — ask (ii). And the nest wholes'
   hybrid prefilter DFAs gained the edge: throughput ×1.57-1.59
   FASTER, match ×1.04-1.05 slower — ask (v), accepted trade or
   tunable.
6. Instrument (ledger §8): 4/4 attempt-1; the first agreement-pass
   record with nonzero disagreeing rows (3 of 1,885, 0 groups — the
   group rule doing its job); pre-flight 5.21 % on one cell = the
   first reading outside the old 0.4-2.6 % band (limit 10 %, record
   stands; the band is now 0.4-5.21 %, n=13); spread base rate 1 per
   13 cells.

ASKS (ledger §11, full wording there): (i) is this verdict + the
withdrawal recorded on your side; (ii) the per-RUN edge-selection
boundary — should runs as short as year4's 4-count take the edge, is
the fixed term's size known, and is a skip-below-k knob cheaper?
(iii) the whole-form ladder: is a bounded-prefilter scan edge STEP 2
or STEP 3 territory, and does [ART-SIZE] expect its first real
customer there? (iv) does Frank charter the TWO-PASS fix (parity's
remaining term) — the same 9-rung surface stands ready as its
acceptance instrument; (v) the hybrid trade (bundled with (ii) if one
term explains both). KB-4 carried (fourth pin, refusal row still
untimed on your clock's side of the ledger — ours to fix).

Bench-side state: [B25] COMPLETE tonight (re-pin, window, report,
ledger, this item); reporter gaps KB-5 (roster filter) and KB-6 (no
scan-edge clause) queued for the next reporter wave; [B23]/[B24]/
[B11.2] next in Frank's recorded order.
