# b45datamgmt — lane report

**Lane:** `b45datamgmt` (Opus design lane), branch `lane/b45datamgmt`,
worktree `worktrees/b45datamgmt`, forked off `master` at `77bc390`.
**Charter:** Frank's data-management white paper, chartered live
2026-09-17 — five axes (culling, compression, git pruning, policy, the
case for a DB), DESIGN NOTE ONLY, nothing enacted.
**Delivered:** `docs/design/data_management_v1.md` (v1.0, 1,064 lines)
plus its `docs/design/CLAUDE.md` entry. Two commits. Nothing merged —
the manager merges.

## Delivery checklist (charter vs committed)

| brief item | where |
|---|---|
| §1 culling: never-delete contract, superseded class with symbols, archive tier, trigger | note §1.1-1.5 |
| §2 compression: measured ratio, the git-delta trap both ways, which surfaces stay plain, loader cost, KB-16 | note §2.1-2.4 |
| §3 git pruning: measured non-problem, routine gc, no-rewrite with SHA-citation cost, reopening threshold + options, no-external-infra stated | note §3.1-3.4 |
| §4 policy: retention taxonomy with every committed directory assigned, growth budget with named triggers, Frank rules exceptions | note §4.1-4.4 |
| §5 the DB case both ways + SQLite-as-derived-cache with invariants and risks; no served DB | note §5.1-5.3 |
| §6 synthesis: phased proposal, each phase costed or marked unmeasured, numbered questions for Frank | note §6.1-6.3, **eleven questions** |
| measure what you assert; per-set growth curves; real zstd/gzip ratios; git-pack delta behaviour verified; record-count-vs-size projections | note §7 appendix maps every claim to its probe |
| context-around-numbers directive | every figure carries its population/window/box state |
| D6-panel-ready: citable or marked unmeasured, both sides of contested cells | four claims carry **PROJECTION/UNMEASURED**; contested cells argued both ways in §1.3, §2.2, §5.2-5.3 |
| update `docs/design/CLAUDE.md` | done |
| branch + lane report committed, handback complete on its own | this file + handback |

**Nothing is OWED.** No background job was launched; every number in the
note was taken in-lane and is reproducible from the appendix.

## Validation

- `make check-schema`: **4 examples accepted / 72 sabotages rejected for
  the intended rule / 0 wrong**, rc=0. (The docs-only change cannot
  affect `check-harness`/`check-report`/`check-interpret`, and the
  store-loading ones were off-limits under the battery window.)
- `git diff --stat master --`: exactly two files, both under
  `docs/design/`, 1,104 insertions, 0 deletions. No file outside the
  worktree was touched; `~/pcrec` was never read or written.

## Box discipline

Every probe ran `nice -n 19` while pcrec's solo battery held the box
(15:30-16:10 EDT, load average 3.75 / 7.64 / 7.20 on 12 cores). The
heaviest single command was a `zstd -19` pass over 106 MB (68 s,
single-threaded, niced) — the rest were `du`/`git cat-file`/`wc`-class
or sub-second. **Nothing loaded the store.** `git gc` was deliberately
NOT run: it mutates a `.git` shared with every live worktree and is
CPU-bound. Throwaway git repos and compression outputs went to the
session scratchpad.

## The two results that changed the charter's premises

Both were the opposite of the intuition behind the axis, and both are
stated in the note's §0 so a reader who stops there has them.

**(1) There is almost nothing to cull — 2.6%, not 13.7%.** The
reporter's SUPERSEDED class (`report.py:3117-3150`, OD-B15: group by
`(subbench@version, testee_id, machine_id)`, keep the newest `measured`)
is **32 records / 96.9 MB / 13.7%** of the store's 706.7 MB. But
supersession is computed over a *query's selected set*, and every
committed report carries its own `since`/`until`/`testee=` filters — so
a globally-superseded record is routinely the one a narrower committed
query kept. Grepping the 32 ids against every `reports/*.md` and
`*.tsv`: **25 of 32 are named in a committed report.** Archiving by the
superseded predicate would break the re-render of a large fraction of
the 43 committed groups. The safe predicate is superseded ∩ uncited =
**7 records / 18.4 MB / 2.6%**, and all seven are failed-gate records
(`inconclusive-load` ×6, `inconclusive-spread` ×1) — the gate's own
audit trail. At 26.6 MB/day, the entire safe cull recovers 16 hours of
growth.

**(2) Compressing the committed store would make the repository
LARGER.** The usual defence of compressing a write-once store is "there
is nothing to delta against"; the live pack refutes it — **149 of the
168 record blobs are stored as deltas**, and since each record file is
committed exactly once, those are deltas against *other records*.
Controlled, on 14 real `email-specimen@0.1` records committed write-once
into a throwaway repo:

| | worktree | git pack |
|---|---|---|
| plain JSONL | 10,536,064 B | **390,207 B** (27.0×) |
| `zstd -3` | 445,844 B | **449,720 B** (+15.3%) |

Re-run with `repack -adf --window=250 --depth=250` on both arms:
390,360 vs 449,721 B (+15.2%) — the plain arm moved 153 bytes, the
compressed arm one. A same-path/successive-version control (3 versions
of one record) gives 92,334 B plain vs 93,795 B zstd, so the trap holds
in both regimes. Compression buys only the working tree (674 MB →
~29 MB) and costs ~15% of the pack forever, a larger `git clone`, and a
Python floor raised 3.11 → 3.14.

## The other measurements worth the manager's eye

- **`reports/` is the second-largest history input, and the charter did
  not name it.** 43 live groups / 151.5 MB, but **713 blob versions and
  32.12 MB of pack — 91% of what the entire store costs** (`store/`: 187
  blobs, 35.21 MB), because the regeneration standing rule rewrites every
  group at every reporter bump. The oldest report `.tsv` has 15 committed
  versions. `.subject-grain.md` is **117.6 MB = 77.6% of `reports/`** —
  Frank's Q9 "no back-fill" ruling declined ~240 MiB of TSV *and* 218
  blobs of regeneration on every subsequent bump.
- **One cheap win exists and it is `git gc`.** 2,257 loose objects hold
  293.3 MB of logical content at **6.9×**, where packed blobs achieve
  **25.1×** (deltas alone 28.3×). `git gc --auto` will not fire — its
  threshold is 6,700. **PROJECTED** saving ~30 MB, `.git` ~100 MB →
  ~65-70 MB. Not run (shared `.git`, CPU-bound, battery window).
- **KB-16 is CLOSED** (2026-09-11, [B41] (e)) — the brief carried it as
  live. Measured 765.67 s → **116.78 s** and 3.84 GiB → 745 MiB RSS on
  one committed query. Its residual is validation + object construction,
  not I/O: on the store's largest record, `zstd` decompression costs
  **0.014 s** against `json.loads`'s **0.222 s**. Compression is a
  disk-space tool here and never a performance one.
- **History rewriting costs 248 citations.** 248 distinct short SHAs in
  committed prose (ledgers, `plan.md`, journal, `outbox_to_pcrec.md`)
  resolve to commits in this repo. The outbox half is decisive: those
  items were read and acted on by pcrecdev1, in a repo BD2 makes
  read-only from here.
- **The growth law is rows, not records: 408 B/row, ±8% across all ten
  sets.** 168 records / 1,732,154 rows / 706.7 MB; 30.7 MB/day over 23
  days, 26.6 MB/day over the last 13 — flat, not accelerating. The
  per-record mean rose 0.75 → 7.67 MB because the *sets* grew.
- **The DB case, with a number.** A stdlib `sqlite3` prototype over 8
  real records / 52,900 match rows / 21.4 MB: build 0.7 s, one index
  0.1 s, db 15.8 MB (0.74× raw, naive all-TEXT schema), **full
  `GROUP BY` 0.076 s**, indexed point query 0.0002 s. Extrapolated
  (**PROJECTION**) to the whole store: ~23 s to build, ~520 MB, **~2.5 s
  to aggregate every row** — against 116.78 s to render one seven-record
  report today. The note recommends this be **held behind a trigger**,
  not built: KB-16 is closed, no committed query hurts, and the one real
  risk (dual-read-path drift putting a wrong number in a report) is the
  worst failure this project can have.
- **Record anatomy, the DB argument in one line:** the store's largest
  record is **1 setup row (78,164 B) + 430 compile rows (966 B each) +
  21,500 match rows (406 B each)** — 94.7% of bytes are match rows. A
  dimension table and a fact table.

## What the note proposes (nothing enacted)

**Phase 0**, cheap and measured: adopt §4's retention taxonomy
(source-of-truth / derived-but-citable / disposable, with every committed
directory assigned); make `git gc` routine; record the growth law and
four consequence-shaped triggers; adopt no-history-rewrite formally.

**Phase 1**, behind named triggers: the archive tier (working tree >
5 GB, ≈5.5 months away); the SQLite derived cache (a committed query
selecting > 100 records); clone options (pack > 500 MB, not this year).

**Phase 2, explicitly NOT proposed:** compressing the committed store,
rewriting history, a served database, culling by the superseded
predicate.

## Eleven questions for Frank (note §6.3)

Each self-contained with a recommendation, in his one-at-a-time style.
Short form: **Q1** adopt the retention taxonomy (YES) · **Q2** routine
`git gc` (YES) · **Q3** no-history-rewrite formally (YES) · **Q4**
compressing the store is off the table (YES) · **Q5** are the four
consequence-shaped triggers right (YES to the shape) · **Q6** archive
form — branch vs committed tarballs (BRANCH, ruled in advance) · **Q7**
does an archived record refuse the render or render smaller (REFUSE, by
name) · **Q8** keep the failed-gate cohort indefinitely (YES, keep) ·
**Q9** charter the SQLite-cache lane (NOT YET, hold behind Q5's trigger)
· **Q10** does the subject-grain slice need its own growth ruling (NOT
YET) · **Q11** right home, and panel before ruling (right home; no panel
before Q1-Q3 — panel the Phase 1 items when their triggers fire).

## For the manager

- Q6 and Q7 are worth ruling **in advance** even though the archive tier
  is months away: they are the two open questions that would otherwise
  arrive attached to a trigger, under time pressure.
- Q2 (`git gc`) is the only item with a measured saving available today
  and needs no design work — it could be folded into the session-close
  routine on a one-line ruling.
- §1.3's finding (25 of 32) is the one a future lane is most likely to
  re-derive the hard way; it is the reason "superseded" must never be
  used as a cull predicate, and it is stated in the note's §0 for that
  reason.
- The note asserts KB-16 is CLOSED, correcting the brief's baseline.
