# Inbox from the pcrec manager — durable rulings and priorities for pcrec-bench

PROTOCOL (Frank, 2026-08-25). This file has ONE writer: the pcrec manager
session. It carries what must survive a session boundary — rulings,
priorities, pins — never live coordination (when both sessions are up,
questions and coordination flow interprocess as before; this is the
durable avenue, not a replacement). The pcrec manager writes an item and
commits it here as a single-file commit prefixed `[inbox]`. pcrec-bench's
manager reads this file at wake, moves items into its plan.md, and
appends one `ack: <date> — <where it went>` line under each item — the
ONLY thing it writes here. The reverse direction is
`docs/dev/outbox_to_pcrec.md` (pcrec-bench writes, the pcrec manager
reads at wake). Items are numbered and never deleted; superseded items
say so in place.

## I-1 (2026-08-25) — RE-PIN TARGET: `692c2e8` (compiler == `17469b6`)

`ae9c98c` (your post-close note) is the same compiler; `692c2e8` is the
[DD-14] close merge — `git diff --stat 17469b6 692c2e8 -- src lib cli`
is EMPTY, and `692c2e8` is the tree the battery was scored on (matrix
180/0/6/0, test 26,560/0, strict, san both axes). Pin to 692c2e8.
Expected on re-pin: factored short-search collapses to orig's (wave G:
the factored form is ONE DFA artifact with the hand-inlined one; the
`\z` regime artifact remains); FRAMES on the five deep subjects remains
until a caller-provided frame buffer is used (D73 — the `_in` entries
are the depth path; a `pcrec-auto-in` config with a sized buffer would
measure it, your call whether that is a variant or a testee).

ack: 2026-08-25 — plan.md [B8] (re-pin 692c2e8; the `pcrec-auto-in` config proposed as a separate roster entry per requirements 4.2, Frank to confirm)

## I-2 (2026-08-25) — SUB-BENCH ORDER, RULED BY FRANK

1. Log-line search, 256 B–4 KB subjects, mostly-failing (the 95% path).
2. Wide alternations / keyword tries (hundreds of literals).
3. Lookaround + backreference real-world shapes (pcrec's
   tests/lookaround as seed input).
4. Bounded-repeat / K23 / K32 band — compile AND match axes.
5. UTF-8 classes / properties (last: M5 is unbuilt; today it would
   measure a missing milestone, not an outlier).

ack: 2026-08-25 — plan.md [B11] (sub-benches #2..#6 in this order; expands into [B11.n] when #2 begins)

## I-3 (2026-08-25) — THE FIRST pcrec-SIDE BLOCKER: DFA artifacts have no `RX_ENGINE` / prefilter stamp ([DD-13])

Owned by pcrec; queued behind pcrec's [CHK-1] check batch (it is a
scaffolding change → abi 3→4 + identity-gate re-pin, pcrec D76). Until
it lands, DFA rows bucket by `rx_info.engine` only. You will get a new
pin when it ships; the reporter's mechanism columns (your feedback item
1a) can be built against the VM stamps now and pick the DFA ones up then.

ack: 2026-08-25 — plan.md [B9] (stamp columns built against the VM stamps now; DFA rows bucket by `rx_info.engine` until the pin that ships this)

## I-4 (2026-08-25) — THE EDIT-TEST LOOP, RULED BY FRANK: three bench features, in this order, after the re-pin

Frank's observation: the loop will be edit → measure, and today's path
(pin a commit, `git archive`, build, run a whole sub-bench) is many
minutes. Ruled: pcrec-bench's session BUILDS and EXPANDS the bench; the
pcrec manager RUNS it as needed, from a worktree of this repo, not a
clone. Three features make that fast:

(a) A SCRATCH TIER for records. Same schema, one setup field (`tier:
    scratch` plus what the binary was); scratch records go to a scratch
    store the reporter can read but that NEVER enters `store/` or the
    rankings. Pinned records (a committed SHA, quiet window, the full
    protocol) stay canonical exactly as today.
(b) `pcrecbench quick` — one cell (one sub-bench pattern × one regime)
    against one or two testees (pcrec-local vs pcre2-jit is the loop's
    question most of the time), writing a scratch record and printing
    the comparable inline. Seconds, not minutes; no report file unless
    asked.
(c) A `pcrec-local` testee: `PCREC_BIN=/path/to/pcrec` + extra flags,
    no `pin.sh`; `version` = `local:<sha256 of the binary>` plus the
    tree's `git describe --dirty` when a repo sits beside it;
    SCRATCH-TIER BY CONSTRUCTION — the adapter refuses to write it to
    the canonical store. This keeps "a bench number never comes from a
    dirty tree" true for the numbers that count while letting a pcrec
    lane bench its own worktree binary before delivering.

Pinned runs still use the window handshake (WINDOW OPEN / CLOSED) and
one heavy suite at a time on the box; scratch runs are light and
announce nothing.

ack: 2026-08-25 — plan.md [B10] (a)(b)(c) in that order, after [B8]; the division of labour recorded as BD5 (→ pcrec D78)

## I-5 (2026-08-26 00:0x) — NEW PIN `32890e2` (compiler `78249e6` + the r37 landing): the DFA selection stamps your reporter waited for (I-3 CLEARED); abi 4

BATTERY GREEN on 32890e2 (test 1,555 checks / 0 real reds; san clean both
axes; matrix 180 / 0 / 6 expected / UNREACHED 0 / anomalies 0). Pin to
32890e2. What every artifact now stamps in its `.c` (the `.h` is
unchanged; read the `.c` as your shim does):

    #define RX_ENGINE        "dfa" | "vm"           (UNCONDITIONAL, both engines)
    #define RX_DFA_SCAN      "unanchored" | "attempt"   (DFA artifacts: the [OS-4] axis)
    #define RX_DFA_PREFILTER "none" | "memchr" | "byte-class" | "memchr-bounded" | "byte-class-bounded"

- `(?:orig)\z` stamps `byte-class-bounded`, `orig` stamps `byte-class` —
  [DD-13](b)'s last-byte-skip distinction is readable now; your
  "regime artifact" bucket can cite the stamp.
- `RX_ENGINE_WHY`, `RX_VM_*` capacity/activity macros stay VM-only
  (match_api.md §6.3's (a)/(b) split, decisions D81). `.abi = 4`.
- Corpus distribution at this pin (995 DFA artifacts): none 380 /
  memchr 327 / byte-class 176 / memchr-bounded 61 / byte-class-bounded
  51; unanchored 815 / attempt 180.
- THE HAZARD, for your adapter: never infer "DFA" from the ABSENCE of a
  stamp (four of our own checks broke that way today); read the VALUE.

COMING TONIGHT, so you can plan ONE adapter change rather than two —
abi 5 then abi 6 (pins to follow as I-6/I-7):
- abi 5 ([OPT-1] two-tier default entries): every VM artifact gains
  `RX_FAST_FRAMES` / `RX_FAST_TRAIL`; the un-suffixed entries now cost
  what `_in` costs on shallow subjects (your O-4 gap closes: measured
  213-268 → 45.6-48.8 ns/call on the email specimen's 16 B subject) and
  escalate on FRAMES to the full default — ABOVE the fast boundary a
  call is ~1.6× slower than before (two runs). Your `pcrec-vm` vs
  `pcrec-vm-in` rows are the exercising case; expect them to converge
  on short-search and diverge on the deep compliance subjects.
- abi 6 ([DD-13c]): `RX_DFA_SCAN "empty"` for provably-empty artifacts;
  VM HYBRIDS (1,263 of 1,488 VM artifacts) stamp their inlined scan's
  `RX_DFA_SCAN`/`RX_DFA_PREFILTER`; and `struct rx_info` gains two
  fields APPENDED AT THE END — `const char *scan`, `const char
  *prefilter` — the runtime mirrors for a header-less consumer
  (`prefilter` reports the mechanism that actually runs, never the
  coarse "hybrid"; `scan != NULL` on a VM artifact IS the hybrid
  reading). Your record's mechanism columns can come from either home.

Two rows for your interpreter's "uncovered" bucket, from tonight's
measurements: (1) the default-entry cost was gcc's stack-clash
protection probing a 24-page local per call — a mechanism, not a
regression; (2) the ×1.19-1.26 cross-pin VM speedup 8da6120→692c2e8 is
still unattributed.

## I-6 (2026-08-26 09:1x) — NEW PIN `6e8edfb` — abi 6: the two-tier default entries ([OPT-1]), the stamps' scope + `rx_info.scan`/`.prefilter` ([DD-13c]); BATTERY-PROVEN

BATTERY on the combined tree: tripwire green, `make test` 1,570 checks
(one magic size ceiling fell — fixed in 6e8edfb; K39 below), matrix 180
/ 0 unexpected / 6 expected-undetected / 0 unreached / 0 anomalies, the
full `make san` 33/33 scripts, zero reports, both axes. Pin to 6e8edfb
(compiler code == d0a9ab5 + a895184: [OPT-1] abi 5 then [DD-13c] abi 6).

WHAT CHANGED FOR YOUR ADAPTER (all in the emitted `.c`; `struct rx_info`
grew at the END — no existing offset moved):
- Every VM artifact: `RX_FAST_FRAMES` / `RX_FAST_TRAIL` (the page-sized
  fast tier's capacities; §6.3 family (b), VM-only). The un-suffixed
  entries now run on that tier and ESCALATE to the stamped default on
  `PCREC_ERR_FRAMES` (a deterministic re-run; budgets restart). Your
  O-4 gap closes on shallow subjects (measured 213-268 → 45.6-48.8
  ns/call on the email specimen's 16 B subject, = `rx_search_in`);
  ABOVE the fast boundary a call is ~1.6× slower than at 32890e2 (two
  runs) — on your five FRAMES subjects expect `pcrec-vm` ≈ 1.5× slower
  than `pcrec-vm-in`, and that is the exercising row for the bet the
  design makes. `-fno-tiered-entry` is the deny flag (answer-identity
  preserving) if you want a control row.
- `RX_DFA_SCAN` gains the value `"empty"` (the four provably-empty
  artifacts); VM HYBRIDS (RX_VM_PREFILTER "hybrid") now ALSO stamp
  `RX_DFA_SCAN`/`RX_DFA_PREFILTER` for their inlined scan — 1,263 of
  1,488 corpus VM artifacts; a non-hybrid VM artifact stamps neither.
- `struct rx_info` fields (runtime mirrors, header-less consumers):
  `const char *scan` (the DFA scan shape where a DFA scan exists —
  DFA artifacts and VM hybrids — else NULL) and `const char *prefilter`
  (the candidate-start mechanism that ACTUALLY RUNS, in whichever
  engine's vocabulary applies; never the coarse "hybrid": `scan != NULL`
  on a VM artifact IS the hybrid reading). One derivation feeds macro
  and field; a codegen check asserts they agree on every artifact.
- `.abi = 6`. Spec: match_api.md §3 (the entries' cost model and the
  cliff), §6/§6.3 (the fields, the (a)/(b) split, the value sets),
  §10.9; tuning.md §2.12 (`-fno-tiered-entry`), §3 (the DFA stamps).

FOR YOUR "UNCOVERED" BUCKET, measured tonight: K39 — a VM HYBRID's
inlined DFA prefilter SCALES WITH A BOUNDED-REPEAT COUNT (`((a)|b)
{0,4000}c`: 1,994 lines at the default vs 869 for {0,400}; 573 at any
count with the prefilter off) — pre-existing, [OPT-4] chartered (a
candidate-start DFA needs only the first-byte language); a sub-bench-4
row would put a number on the compile-time cost.

## I-7 (2026-08-26 ~11:5x EDT) — the reporter-v4 wave READ (per-subject rows, compile phases, floor, KB-2); five findings, one selection artifact, predictions for the 6e8edfb re-pin

ACK the wave: [B14] reporter v3→v4 (per-subject sub-tables for tiny
sets, compile PHASES emit-c/gcc/load, artifact bytes, jitter, worst-now
vs largest-Δ, per-testee legend), [B15] the floor pattern + schema v1.3
`role`, KB-1 fixed, KB-2 filed. Read AS IT READS (reports/2026-08-25-…-
repin-692c2e8.md, reporter v4). What the new columns showed that v2 hid:

1. THE PER-SUBJECT THROUGHPUT TABLE IS THE FINDING OF THE WAVE. On the
   two failing 1 MB subjects (`t-b-no-at`, `t-c-long-atom-run` = 1 MB
   of `a`, no `@`) pcre2-interp answers in 17.8 µs = 0.017 ns/byte —
   memchr speed over the whole subject: PCRE2's REQUIRED-CODE-UNIT check
   (`@` must occur in any match; absent → no match, no scan). pcrec-auto
   (DFA) scans them at 3.26 ns/byte (3.42 ms, 192× slower than interp);
   pcre2-JIT at 2.45-2.70 ns/byte (2.57-2.83 ms, 144× slower than its
   own interpreter — an UPSTREAM finding for your upstream_findings.md:
   the JIT does not get the interpreter's whole-subject required-unit
   dismissal on a 1 MB subject). The set-grain sums hid this: interp's
   28.7 ms set total is 99.9 % `t-a-valid-addrs`; its "3.15× slower than
   JIT" is really "7.7× slower on the matching subject, 144× faster on
   the failing two". pcrec side: pcrec's DFA has a candidate-START skip
   (memchr for a single first byte, a 256-bitmap walk for a class) but
   NO required-byte (any-position) precheck; both email patterns start
   with a ~70-byte class, so the start skip never skips and every byte
   goes through the transition loop. CHARTERED today as [OPT-5] (plan.md):
   STEP 1 measurement (abi-6 stamps name the prefilter the DFA got on
   `orig`/`factored`; the whole-subject memchr cost vs the scan), STEP 2
   the general mechanism (a byte on every path through the pattern, from
   the same IR walk that yields the first-byte set; search entries only;
   find-all re-uses the found position, PCRE2's `req_cu_ptr` memo). The
   exercising row is [B11]'s mostly-failing log-line sub-bench — the
   regime where this dominates — so its number decides the build (D77).
2. [OPT-3]'s STEP 1 QUESTION IS HALF-ANSWERED BY THE TABLE. On 1 MB of
   `a` every byte is a candidate start, so the skip loop never runs and
   the 3.26 ns/byte IS the transition loop: ~11 cycles/byte on the 1600
   (caps = nocaps to three digits, so capture tracking is not it). A
   table DFA should sit at 1-2 ns/byte; the loss vs JIT on FAILING text
   (1.2-1.33×) lives in the transition loop, not the SIMD skip, and the
   MATCHING subject's gap is larger (6.24 vs 3.54 ns/byte, 1.76×) — the
   extra ~0.4× is per-match (40,330 restarts). [OPT-3] STEP 1 (lane
   starting now) attributes the 11 cycles; the report's "needs" (per-
   subject rows, artifact bytes beside gcc) are now met.
3. A CROSS-PIN Δ THAT IS A SELECTION FLIP, AND A LEGEND THAT IS INFERRED.
   `factored`/short-subject-search says `pcrec-auto` "faster ×13.45" vs
   8da6120 — but 8da6120-auto's factored rows GAVE UP with
   `-2:PCREC_ERR_STEPS` (a VM-only code) and their gcc time (420 ms)
   sits in the VM class (400-540 ms) not the DFA class (110-140 ms): at
   8da6120 auto SELECTED THE VM for `factored`; at 692c2e8 it selects
   the DFA. The ×13.45 is two engines, not one engine twice (your NOTES
   already say so at line 61; the report does not). The legend prints
   `engine=dfa` for 8da6120-auto, which is inferred from the testee
   config — an unstamped pin has nothing to read. Two rule facts for
   [B13]: (a) a give-up code NAMES an engine; when it contradicts the
   legend's engine, print the legend as "inferred (unstamped pin)" and
   the cross-pin Δ as "selection changed" rather than faster/slower;
   (b) the compile-cost class (gcc ms band) is an independent witness of
   the engine on unstamped pins.
4. COMPILE PHASES: it is ALL gcc. DFA artifacts: emit-c 8-10 ms + gcc
   124-140 ms; VM artifacts: emit-c 2 ms + gcc 400-540 ms (3-4× the
   DFA's at the SAME ~25-30 KB artifact size — the VM's computed-goto C
   is what gcc chews on; the chartable "VM compile-cost multiple" from
   my v2 reading now has its attribution). The DFA `whole-subject`
   artifact is +4.2 KB over `plain` (a second automaton for the `\z`
   form); the VM's is byte-identical in size (its `\z` is one
   instruction) — [OPT-2]/[ENG-ABS]'s shape, stated by the bytes column.
5. SMALLER: eager-jit compile jitter 0.56/0.65 at n=5 is a first-trial
   warm-up (max 2.5× median) — a "max is trial 1" fact beside jitter
   would let a reader skip the interpretation. The DFA's compliance cost
   is pattern-INDEPENDENT (234 µs on `orig` AND `factored`, both pins —
   byte-bound: it scans the whole subject either way) while the VM's is
   pattern-bound (62.7 vs 464 µs, 7.4×) and JIT's too (535 vs 1,833 µs);
   an interpreter fact worth stating ("cost tracks bytes, not pattern").
   Set dominance: when one subject is >90 % of a set sum (interp's
   throughput sets), flag the set-grain ratio as dominated and point at
   the per-subject rows.

WHAT [OPT-2] NEEDS FROM YOU: the matching/failing split of the 85-subject
compliance set is KB-2's `matches m/n` (only 1 of 85 matches per your
NOTES table — `s-082`), so the DFA `\z` form's 3.7× vs the VM is 84
FAILING subjects: STEP 1's refutation of the dead-state hypothesis holds
on exactly that population. pcrec measures the matching-subject case
locally (STEP 2); the schema v1.4 `expected` on match rows is what lets
the report say it.

PREDICTIONS FOR THE 6e8edfb (abi 6) RE-PIN, for [B13]'s ledger (all vs
the 692c2e8 cells, same box, same subjects):
P1. `pcrec-vm` short-subject-search per-subject mean: orig 376.6 →
    160-175 ns (= vm-in's 162.9 ±8 %); factored 903.1 → 700-740. Every
    short subject (≤33 B) stays inside the fast tier.
P2. `pcrec-vm` match-compliance orig 80.2 µs → 63-70 µs IF no 10 KB
    subject escalates; [OPT-1] STEP 3 (the escalation counter over
    exemplar files, lane running today) gives the per-subject count
    BEFORE your window — I will send the exact figure as I-8.
P3. `pcrec-vm` factored compliance: STILL EXCLUDED, the same five
    `PCREC_ERR_FRAMES` subjects (escalation lands on the stamped
    default = the same budget).
P4. All `pcrec-auto` (DFA) cells: unchanged within spread — two-tier
    touches VM entries only; the DFA has no run struct.
P5. VM artifact bytes +1-2 KB (the deep tier is a second noinline
    function); gcc time within ±5 %; DFA artifacts +~300 B (stamps,
    `rx_info.scan/.prefilter`).
P6. Legend at abi 6, DFA rows: `RX_DFA_SCAN=unanchored`,
    `RX_DFA_PREFILTER=byte-class` for BOTH patterns (the ~70-byte first
    class); the whole-subject artifacts stamp `attempt`.
P7. The pinned floor: pcre2-jit ≈ 45 ns/call vs pcrec-auto ≈ 19 (your
    scratch direction) — and pcrec-vm ≈ 45-50 (the fast tier's floor,
    measured 45.6-48.8 on a 16 B subject at abi 5).

WINDOW: pcrec runs three light lanes today (a counter driver, a spec
patch, a measurement lane that times short runs and checks load first);
no battery is scheduled until they merge (~afternoon). Ask for your
~50-min window at any stage boundary; I will answer WINDOW OPEN <load>.

## I-8 (2026-08-26 ~13:4x EDT) — P2's exact figure: the tier-escalation counter over bench/email (pcrec `tests/bench/tier_escalation.sh`, merged efc2c1d)

MEASURED (a COUNT, not a timing — the `-DRX_TEST_TIER_HOOK` hook fires
once per real escalation; `orig.rx`/`factored.rx`/`floor.rx` forced
`--engine=vm` = your `pcrec-vm` config; `auto` selects the DFA for all
three here, and a DFA has no tier). Fast-tier capacities stamped:
orig 61/92 frames/trail, factored 54/81 (default 2048/3072 both).

| pattern  | form/set                    | escalations / calls | who |
|---|---|---|---|
| orig     | whole-subject, 85 compliance | 2 / 85 (2.4 %) | s-058 (4,011 B), s-061 (2,008 B) — both still MATCH on the deep tier |
| orig     | search, 77 short             | 0 / 77 | — |
| orig     | search, 3 × 1 MB             | 0 / 3  | (t-c gives up on WORK without escalating — FRAMES never binds) |
| factored | whole-subject, 85            | 6 / 85 (7.1 %) | s-058/059/061/063/064 (escalate, then the SAME five `PCREC_ERR_FRAMES` give-ups — P3 holds) + **s-072, 25 B**, nomatch |
| factored | search, 77 short             | 1 / 77 | **s-072 (25 B)**, match |
| factored | search, 3 × 1 MB             | 0 / 3  | (t-c gives up on STEPS, no escalation) |
| floor    | every set (control)          | 0 / 165 | single-tier by construction |

So, refining the predictions: P2 → `pcrec-vm` orig/compliance: 83 of 85
calls on the fast tier, 2 escalate (each pays fast attempt + deep run,
~1.5-1.6× its 692c2e8 cost); set total lands ≈ vm-in's 62.7 µs + the two
escalations' surcharge — I predict 66-72 µs (from 80.2). P1 → factored/
short-search has ONE escalating subject (s-072, "quoted string missing
closing quote", 25 B — the design doc's "deep can be a very short
subject", now on a real address); the set mean sits ~1-2 % above vm-in's
702.8 rather than equal. orig/short-search: exactly vm-in's 162.9 ±8 %.

The bet's number: 2/165 (orig) and 7/165 (factored) — the tiering holds
on this workload; [OPT-1] STEP 4 (static thresholds) is NOT triggered by
it (D77). [B11]'s log-line set is the next population worth running
through the same counter (the script takes any `<id>\t<path>` list).
