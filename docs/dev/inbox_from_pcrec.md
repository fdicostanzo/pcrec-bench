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
