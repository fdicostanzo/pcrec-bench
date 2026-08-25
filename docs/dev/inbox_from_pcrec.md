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

## I-2 (2026-08-25) — SUB-BENCH ORDER, RULED BY FRANK

1. Log-line search, 256 B–4 KB subjects, mostly-failing (the 95% path).
2. Wide alternations / keyword tries (hundreds of literals).
3. Lookaround + backreference real-world shapes (pcrec's
   tests/lookaround as seed input).
4. Bounded-repeat / K23 / K32 band — compile AND match axes.
5. UTF-8 classes / properties (last: M5 is unbuilt; today it would
   measure a missing milestone, not an outlier).

## I-3 (2026-08-25) — THE FIRST pcrec-SIDE BLOCKER: DFA artifacts have no `RX_ENGINE` / prefilter stamp ([DD-13])

Owned by pcrec; queued behind pcrec's [CHK-1] check batch (it is a
scaffolding change → abi 3→4 + identity-gate re-pin, pcrec D76). Until
it lands, DFA rows bucket by `rx_info.engine` only. You will get a new
pin when it ships; the reporter's mechanism columns (your feedback item
1a) can be built against the VM stamps now and pick the DFA ones up then.

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
