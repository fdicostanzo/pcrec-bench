# data_management_v1.md — the data-management white paper

**Status: DESIGN NOTE, v1.0, 2026-09-17 (lane `b45datamgmt`). Nothing
here is enacted.** No policy is in force, no file is moved, no loader is
changed, no threshold binds anything. §6 ends with eleven numbered
questions for Frank, each self-contained and each carrying this lane's
recommendation.

Chartered by Frank live, 2026-09-17, in the session that ratified the
subject-grain rulings: the store is growing fast; *"we are going to have
to cull at some point"*; *"truth — this should be a database but I don't
want to use one."* Five axes named: (1) culling, (2) compression, (3)
git pruning, (4) policy, (5) the case for a DB.

Every number below was measured on `budu-ryzen1600` on 2026-09-17
between 15:30 and 16:10 EDT, at commit `77bc390`, with pcrec's solo
battery holding the box (load average 3.75 / 7.64 / 7.20 on 12 cores);
every probe was `nice -n 19` and of the `du`/`git`/`wc`/small-compressor
class the window permitted. Anything not measured is marked
**UNMEASURED** with the command that would settle it. Per Frank's
context-around-numbers directive of the same session, each number is
stated with what it sits inside.

---

## 0. The two results that reframe the charter

Two of the five axes turned out, on measurement, to point the opposite
way from the intuition that chartered them. Both are stated here so a
reader who goes no further has the load-bearing facts.

**(A) There is almost nothing to cull.** The store's natural cold class
— records the reporter itself calls SUPERSEDED — is 32 records / 96.9 MB,
13.7% of the store's 706.7 MB. But **25 of those 32 are named by
filename in a committed report** (§1.3), and re-rendering a committed
report is a `make check-report` gate. The records that are cold *and*
cited by nothing are **7 records / 18.4 MB — 2.6% of the store**, and
every one of them is a failed-gate record (`inconclusive-load` or
`inconclusive-spread`) that no report ever used. Culling is not the
lever. At 26.6 MB/day of new store, the entire safe cull recovers
**16 hours of growth.**

**(B) Compressing the committed store would make the repository
LARGER.** Measured on fourteen real records committed write-once into a
throwaway git repo (§2.2): plain JSONL packs to 390,207 B; the same
fourteen records as `zstd -3` blobs pack to 449,720 B — **+15.3%**. Git
already achieves 20.1× on the store's plain record blobs, and 149 of the
168 record blobs in the live pack are stored as *deltas against other
records*. Compression buys the working tree (674 MB → ~29 MB) and costs
the history, permanently. The two are separable, and §2 argues both
sides of exactly that trade.

What the measurement does support is §4's taxonomy (cheap, clarifying,
zero risk), §3's routine `git gc` (a measured ~30 MB sitting in loose
objects today), and §5's SQLite derived cache (a filter-aggregate over
the *whole* store in an extrapolated ~2.5 s, against the 116.78 s
KB-16 measured for rendering *one seven-record report*).

---

## 1. CULLING

### 1.1 What may never be deleted

The append-only contract is stated in three places and is not this
note's to revise:

- `store/CLAUDE.md`: *"Records are DATA and are committed (requirements
  §6; OD-B6 revisits when size demands). They are written once and never
  edited — a re-measurement is a new record."*
- `docs/design/record_schema.md:18`: *"once and never edited; a
  re-measurement is a new record (§6)."*
- `record_schema.md` §3: every record carries `content_hash.value`, a
  sha256 over line 1 canonicalised without the hash member plus every
  row line in file order. **A record's bytes are self-verifying.** That
  matters below: anything moved can be proved unchanged on arrival.

Three provenance chains bind records to committed prose, and each is a
`make check` gate or a citation a reader follows:

1. **Report → record, by path.** Every committed report `.md` names
   every record it included, with its full store path. The
   2026-09-17 capability report's header lists seven such lines, e.g.
   `store/records/capability@0.1/pcrec_a770139e_auto-caps-simdna/capability@0.1__pcrec_a770139e_auto-caps-simdna__budu-ryzen1600__20260917T020152Z.jsonl`.
   `reports/CLAUDE.md`'s regeneration discipline re-renders reports from
   their own committed query; a record its query selects must be
   loadable.
2. **Sidecar → index, by sha256.** Each `.interpretation.md` stamps
   `index_sha256:` in its opening HTML comment, and
   `make check-interpret` section 3 re-renders every committed sidecar
   from that stamp and **requires byte equality**. Any edit to
   `store/index.tsv` — including adding a column or removing a row —
   invalidates all four committed sidecars at once. ([B41] already
   carries "regenerate the sidecars at every window's close" as a
   standing follow-up for exactly this reason.)
3. **Ledger → report → record.** Measured: the twelve files under
   `docs/dev/ledgers/` cite reports by name and line, not records by id
   — a grep for the record-id shape across all twelve returns **0
   hits**, and only three of the twelve mention a `store/records` path
   at all (`2026-09-17-capability-0.1-first-a770139e.md`, three times).
   So the ledger layer is insulated: it breaks only if a *report*
   breaks. That is a genuinely helpful structural fact — the chain has
   one narrow waist, the report file, and protecting that waist protects
   everything above it.

### 1.2 The natural cold class, and exactly how the code defines it

`pcrecbench/report.py:3117-3150` (OD-B15, amended 2026-08-25) groups
valid records by the triple `(subbench@version, testee_id, machine_id)`
— note `testee_id` encodes the pcrec pin, so records at different pins
are never in the same group — sorts by `run.timestamp`, keeps the
**newest `measured`** entry, and calls every entry older than the kept
one SUPERSEDED (`rd.superseded`, rendered in the header as
`- superseded: N record(s) (OD-B15; --all-records lists them)`,
`report.py:3538-3545`). An entry *newer* than the kept one that is not
`measured` is listed separately as "newer, not measured"
(`newer_not_measured`) and does not supersede anything. The interpreter
reads the same header key (`interpret.py:615`, `catalogue/rules.toml`
`slots = ["candidates", "included", "superseded", …]`).

Applying that exact rule to the live index (168 records in 136 groups):

| class | records | MB | share of store bytes |
|---|---|---|---|
| kept (the ranking population) | 136 | 609.8 | 86.3% |
| **superseded** | **32** | **96.9** | **13.7%** |
| newer-not-measured | 0 | 0.0 | 0% |

Status histogram over all 168: `measured` 157, `inconclusive-load` 9,
`inconclusive-spread` 2.

The superseded cohort is dominated by the libpcre2 reference arms
(`libpcre2_10.46_interp` / `_jit`), re-measured in window after window
against the same set on the same box — 19 of the 32. That is the cold
class working as designed: the same cell, re-run.

### 1.3 Why "superseded" is NOT a safe cull predicate — the measurement

`report.py` computes supersession **over the query's selected set**, and
every committed report carries its own `since`/`until`/`testee=` filters
(the 2026-09-17 capability report's are
`since=2026-09-17T00:00:00Z, until=2026-09-17T08:00:00Z` plus seven
explicit `testee=` terms). A record that is superseded *globally* — by
a re-measurement three weeks later — can be, and often is, the record a
narrower committed query kept.

Grepping the 32 superseded record ids against every committed
`reports/*.md` and `reports/*.tsv`:

> **25 of 32 superseded records are named in a committed report.**

Named examples include
`email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__…20260825T175131Z`,
`bounded@0.3__pcrec_288d505_auto-caps-simdna__…20260905T004759Z`, and
`capability@0.1__libpcre2_10.46_dfa-nocaps-simdna__…20260917T054738Z`
— which is superseded *within its own window*, less than an hour after
it was written (the v1.4 spread rule's re-measure). Archiving by the
reporter's own superseded predicate would break the re-render of a large
fraction of the 43 committed report groups.

**The safe predicate is intersection, not supersession:** superseded
AND named by no committed report. Measured, that is:

| | records | MB | share |
|---|---|---|---|
| superseded ∩ uncited | **7** | **18.4** | **2.6%** of store |

and — a small, clean result — the set of records cited by *no* committed
report at all is **the same 7 records**. Every one is a failed-gate
record:

```
  4.2 MB inconclusive-spread bounded@0.2__pcrec_263b013_vm-in-caps-simdna__…20260831T164245Z
  3.3 MB inconclusive-load   bounded@0.1__pcrec_36d5963_vm-in-caps-simdna__…20260830T050354Z
  3.1 MB inconclusive-load   bounded@0.1__pcrec_36d5963_auto-caps-simdna__…20260830T040352Z
  3.0 MB inconclusive-load   bounded@0.1__libpcre2_10.46_jit-caps-simdna__…20260830T034510Z
  2.7 MB inconclusive-load   loglines@0.1__pcrec_36d5963_auto-nocaps-simdna__…20260829T201…
  1.1 MB inconclusive-load   email-specimen@0.2__pcrec_36d5963_vm-caps-simdna__…20260829T192…
  1.1 MB inconclusive-load   email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__…2026082…
```

These are the records the gate rejected — the ones whose *existence* is
the evidence that the gate fired (KB-4, the v1.4 spread rule's first
production firing, BD7's five one-shot after-sample losses). They are
the cheapest thing in the store to keep and among the more interesting
things to lose.

**Contested cell, stated both ways.** *For archiving them:* they carry
no number anyone will ever rank, and 18.4 MB is 18.4 MB. *Against:* they
are 2.6% of the store, they are the gate's own audit trail, and moving
them costs an index change that invalidates every sidecar (§1.1 chain 2)
plus an archive-resolution path in `store.py`. This lane's reading is
that the ratio is not close: the mechanism costs more than the space it
recovers, **today**. That is a statement about today's numbers, not a
principle — §1.5 states what changes it.

### 1.4 The ARCHIVE TIER proposal — culling as MOVE, never LOSS

Proposed for the day §1.5's trigger fires, not for now. Sketch only; no
implementation is designed here.

- **Where.** A `store/archive/<cohort>.tar.zst` per archived cohort,
  committed — OR an `archive/` branch in the same repository, never
  merged, holding the records at their original paths. (§2.4 argues
  these two against each other; the branch wins on git-internal grounds
  and the tarball wins on reviewer-legibility, and the choice is Q6.)
- **Never external.** No object store, no LFS, no service — "no
  external infra" is a project value, stated explicitly in §3.4.
- **The index keeps the row.** `store/index.tsv` gains one column,
  `location` (`live` | `archive:<cohort>`), and the archived record's
  row stays in place with every other column unchanged — subbench,
  version, testee_id, machine_id, timestamp, status, rows. The KB-16
  prefilter (`report.py`'s `index_row_could_match`) therefore keeps
  working on archived rows unchanged, and a query that would have
  selected one can *say so by name* instead of silently rendering a
  smaller report. **A report whose query selects an archived record
  REFUSES rather than renders** — silently dropping a record from a
  ranking is precisely the failure the whole status/supersession
  apparatus exists to prevent.
- **Provenance stays resolvable.** The record id is the filename
  (`validate.py --check-filename`, rule X4), so a report's committed
  path plus the index's `location` column locates the archived bytes
  exactly; `content_hash` proves them unchanged on extraction.
- **Restoring is a command, not an archaeology exercise.** `pcrecbench
  archive restore <record_id>` puts the file back under
  `store/records/…` and flips the column.

**Cost that is not in the space budget:** one schema/index change (which
invalidates all committed sidecars at once, §1.1 chain 2), one
`store.py` resolution path, one refusal path in the reporter, and a new
`make check` arm proving an archived record round-trips byte-identically
and that a query selecting one refuses by name. Call it comparable to
[B31] or [B32] in size. **UNMEASURED**; the honest comparison is against
the 18.4 MB it would recover today.

### 1.5 The trigger question

This lane recommends **no threshold on the store's size at all**, and
one on a *consequence* instead. Size alone has not hurt anything: the
store is 674 MB in the working tree and 35.2 MB in the pack, and the
operation that actually hurt (KB-16's 765.67 s / 3.84 GiB whole-store
validation) was **closed on 2026-09-11** by reading the index first, not
by making the store smaller. A size threshold would fire on a number
that is not the problem.

The consequence-shaped triggers, in the order this lane expects them:

| trigger | measured today | this lane's threshold |
|---|---|---|
| a full `git clone` becomes slow enough to change how the project works | pack 48.39 MiB + 47.68 MiB loose | pack > 500 MB |
| the working tree exceeds a routine laptop/CI checkout | 674 MB store, 843 MB repo working tree | working tree > 5 GB |
| a *committed* query again selects most of a large store (KB-16's own stated revisit condition) | no committed query does | the day one does |

Whose ruling: **Frank's, on a named trigger, not a lane's discretion.**
Q1 and Q5 in §6 put both halves of that to him.

---

## 2. COMPRESSION

### 2.1 What the data compresses to

Twenty records sampled across all ten sub-bench versions (for each set:
its largest record and one chosen at random with a fixed seed),
106.1 MB of JSONL, each compressed as its own file, single-threaded,
`nice -n 19`, on the loaded box:

| codec | 106.1 MB → | ratio | wall | throughput |
|---|---|---|---|---|
| `gzip -6` | 5.00 MB | 21.23× | 0.9 s | 119.3 MB/s |
| `zstd -3` | 4.36 MB | **24.34×** | 0.4 s | 269.2 MB/s |
| `zstd -9` | 3.74 MB | 28.39× | 1.5 s | 68.5 MB/s |
| `zstd -19` | 2.97 MB | 35.71× | 68.0 s | 1.6 MB/s |

Ratios this extreme are not luck: a record is 1 setup row + N compile
rows + M match rows, and the match rows are near-identical JSON objects
differing in a few integers. The largest record in the store
(`bounded@0.3__pcrec_1989c62_vm-caps-simdna_cc-clang__…`, 9,230,605 B)
is **1 setup line (78,164 B), 430 compile lines (966 B each), and
21,500 match lines (406 B each)** — 94.7% of its bytes are match rows.
Across the whole store the figure is remarkably stable: **408 bytes per
row**, and per-set means run 0.38–0.44 KB/row over ten sets. Store size
is, to within ±8%, a linear function of row count.

**Cross-record redundancy adds little.** One `tar | zstd -3` over a
whole set, versus summing per-file `zstd -3`:

| set | raw | per-file zstd-3 | one tar.zst |
|---|---|---|---|
| `email-specimen@0.1` (14 records) | 10.5 MB | 0.45 MB (23.6×) | 0.38 MB (27.9×) |
| `altwide@0.1` (6 records) | 11.9 MB | 0.60 MB (19.7×) | 0.53 MB (22.3×) |

So bundling buys ~15% more compression and costs per-file
addressability. Per-file is the right unit if compression happens at
all.

### 2.2 THE GIT-DELTA TRAP — measured, both ways

The trap, stated: a compressed blob is high-entropy, so git can neither
zlib it further nor delta it against its neighbours. The usual mitigating
answer is *"but the store is write-once, so there is nothing to delta
against."* **That answer is wrong here, and the live pack says so.**

Mapping every blob in the repository to its path and reading
`%(objectsize:disk)` and `%(deltabase)`:

| surface | blobs | logical | on disk | ratio | of which deltas |
|---|---|---|---|---|---|
| `store/records/*.jsonl` | 168 | 706.7 MB | 35.20 MB | **20.1×** | **149 of 168** |
| `store/index.tsv` | 15 | 0.3 MB | 0.01 MB | 48.2× | 14 of 15 |
| `reports/*.subject-grain.md` | 218 | 477.7 MB | 24.52 MB | 19.5× | 159 of 218 |
| `reports/*.tsv` | 220 | 83.4 MB | 3.34 MB | 25.0× | 170 of 220 |
| `reports/*.md` (non-grain) | 275 | 56.5 MB | 4.25 MB | 13.3× | 193 of 275 |

**149 of the 168 record blobs are deltas** — and since each record file
is committed exactly once, those deltas are against *other records*:
different testees, different runs, different sets. Git is exploiting the
same cross-record redundancy §2.1 measured, across the whole store at
once, for free.

Two controlled experiments, each a throwaway `git init` in the
scratchpad:

**(i) Same path, successive versions** (the three `email-specimen@0.1 /
libpcre2_10.46_interp` records, committed one after another to the same
filename — the shape a *mutable* file has):

| | per-version logical | git pack after `gc --aggressive` |
|---|---|---|
| plain JSONL | 737,785 B × 3 | **92,334 B** |
| `zstd -3` | 30,656 B × 3 | **93,795 B** |

The compressed version is 24× smaller on disk and **1.6% larger in
git**.

**(ii) Write-once, many different records** (all fourteen
`email-specimen@0.1` records, one commit, `git repack -adq` — the shape
the *real store* has):

| | logical | git pack |
|---|---|---|
| plain JSONL | 10,536,064 B | **390,207 B** (27.0×) |
| `zstd -3` | 445,844 B | **449,720 B** (+15.3%) |

Experiment (ii) was re-run with `git repack -adf --window=250
--depth=250` on both arms, to rule out the result being an artifact of
default packing: **390,360 B plain vs 449,721 B zstd (+15.2%)** — the
plain arm moved by 153 bytes, the compressed arm by one. Git's default
window already finds every delta there is to find here.

So the trap holds in **both** regimes, and the write-once escape hatch
does not exist for this data. Committing the store compressed would cost
about 15% more pack, forever, and would also make `git clone` transfer
more bytes, not fewer (a clone ships the pack).

**The honest other side.** Compression is a large win for exactly one
resource: **the working tree.** 674 MB of `store/` becomes ~29 MB at
`zstd -3` (706.7 / 24.34). At the 500-record projection in §4.3 that is
3.3 GB versus 137 MB. If the day comes when a checkout's *size on disk*
is the binding constraint — a small CI runner, a laptop, a container
image — that is a real and decisive argument, and it is worth 15% of a
pack. It is not a real argument today, when the whole repository working
tree is 843 MB on a box with the store on it anyway.

**Which surfaces could be compressed safely, if any.** Only write-once
ones, and even there §2.2(ii) says the gain is negative in git. The
surfaces that must stay plain regardless:

- `reports/*` — regenerated wholesale at every reporter bump (§3.2);
  compressed blobs would turn 713 well-delta'd report blobs into 713
  incompressible ones. This is the single worst place to apply
  compression in the repository.
- `store/index.tsv` — rewritten every `index` run, 48.2× in the pack
  today, and diffed by humans.
- Anything `make check` re-derives byte-for-byte.

### 2.3 What compression does NOT do for KB-16

KB-16 (`docs/dev/known_issues.md:610`) is **CLOSED** as of 2026-09-11
([B41] (e)): `report.py` prefilters candidate records from
`store/index.tsv` rows before opening anything, and the measured
before/after on one committed query (six of the store's largest records,
35,859–41,800 rows each) was **765.67 s → 116.78 s (×6.55) and
4,027,148 KB → 762,940 KB RSS (×5.28)**, with the TSV byte-identical.
The brief that chartered this note carried KB-16 as a live problem; it
is not, and the note records that.

For the residual 116.78 s, compression is irrelevant, and the
measurement is unambiguous. On the store's largest record (9,230,605 B),
warm page cache, same box:

| operation | time |
|---|---|
| read the plain file | 0.002 s |
| **`compression.zstd.decompress` the whole record** | **0.014 s** (517 MB/s) |
| **`json.loads` every line** | **0.222 s** |

Decompression costs **6.3% of what parsing costs**, so reading records
compressed would add roughly 6% to a load that is already
parse-dominated — and the parse itself is not where the 116.78 s goes
either: extrapolating 0.222 s per 9.2 MB across the whole 706.7 MB
store gives ~17 s of `json.loads` for *everything*, against KB-16's
116.78 s for *six records*. The remaining cost is jsonschema validation
and Python object construction, which no storage format touches. KB-16's
own unaken candidates (b) validate-lazily and (c) load-large-fields-lazily
name the same two costs.

**Compression is a disk-space tool here, not a performance tool.** §5 is
where the performance argument lives.

### 2.4 Loader integration cost

Cheaper than expected, with one real caveat.

- **The dependency is already satisfied, on this box.** `python3 -VV`
  reports **Python 3.14.4**, and `import compression.zstd` succeeds —
  PEP 784 put zstd in the **standard library** in 3.14. No
  `zstandard` wheel, no `requirements.txt` change (which today pins
  exactly one package, `jsonschema==4.19.2`).
- **The caveat, and it is real.** `pyproject.toml` declares the project
  compatible with **Python ≥ 3.11**, so a 3.11/3.12/3.13 reader has
  `gzip` and `lzma` but *not* `compression.zstd`. Compressing the store
  would either raise the floor to 3.14 — narrowing "a stranger's `make`
  must work" (pcrec D2's posture, inherited) — or need a gzip fallback
  at 21.2× instead of 24.3×. **UNMEASURED:** whether anything but this
  box has ever run the harness.
- **Touch points** are narrow: `store.py`'s `serialize`/`write` (348
  lines total) and `report.py`'s `_read_lines`. `validate.py` works on a
  stream and would not care.
- **What would need proving** in `make check`: a compressed record
  validates identically, `content_hash` is over the *uncompressed*
  bytes (so the hash is a property of the record, not of its storage),
  and `--check-filename`/X4 still identifies a record from its path.

---

## 3. GIT PRUNING

### 3.1 The measured non-problem, and the one measured easy win

`git count-objects -vH` at `77bc390`:

```
count: 2257          size: 47.68 MiB      (loose)
in-pack: 6097        size-pack: 48.39 MiB packs: 1
prune-packable: 0    garbage: 0
```

The pack is 48.39 MiB holding 1,549.3 MB of logical blob content —
**16.8× overall, and 25.1× across packed blobs alone.** That is not a
repository in trouble.

But the split is worth looking at, because it contains the one cheap win
in this whole note:

| | logical | on disk | ratio |
|---|---|---|---|
| blobs **packed** | 1,256.0 MB | 49.98 MB | **25.1×** |
| …of which are deltas | 1,098.6 MB | 38.84 MB | 28.3× |
| blobs **loose** | 293.3 MB | 42.24 MB | **6.9×** |

The single pack is dated **Sep 9**; everything committed since sits
loose, at zlib-only 6.9× instead of the packed 25.1×. Those 2,257 loose
objects are why `du -sh .git` says 100 MB while `size-pack` says 48.39
MiB.

**Recommendation: run `git gc` as routine hygiene** — after every
regeneration wave and at every session close. `git gc --auto` will not
do it for you: its loose-object threshold is 6,700 and the repo is at
2,257.

**PROJECTION, NOT MEASURED:** 293.3 MB of loose logical content repacked
at the pack's measured 25.1× is ~11.7 MB, against 42.24 MB today — a
saving of roughly **30 MB**, taking `.git` from ~100 MB to ~65-70 MB.
The loose objects are the newest versions of frequently-rewritten files
(reports), which delta *well* against their predecessors, so 25.1× is a
fair-to-conservative basis. This lane did **not** run `git gc`: it
mutates `.git`, which is shared with every live worktree, and repacking
1.5 GB of logical content is a multi-minute CPU-bound job that the
battery window forbids. Verify with
`git clone --no-hardlinks --local . /var/tmp/gcprobe && git -C /var/tmp/gcprobe gc && git -C /var/tmp/gcprobe count-objects -vH`
on a quiet box.

### 3.2 Where the history actually comes from — reports, not records

The surprise in the pack, and a direct input to §4's policy:

| top-level dir | blobs | logical | on disk |
|---|---|---|---|
| `store/` | 187 | 707.0 MB | 35.21 MB |
| **`reports/`** | **713** | **617.6 MB** | **32.12 MB** |
| `docs/` | 1000 | 62.6 MB | 12.20 MB |
| everything else | ~1,850 | ~71 MB | ~8 MB |

`reports/` holds **43 report groups / 151.5 MB live**, yet has produced
**713 blob versions and 32.12 MB of pack — 91% of what the entire store
costs** — because `reports/CLAUDE.md`'s standing rule regenerates every
committed report at every reporter bump. The oldest report group
(`2026-08-25-email-specimen-0.1-…-repin-692c2e8`) has **15 committed
versions** of its `.tsv` and 15 of its `.md`; `reports/CLAUDE.md` itself
has 34. 48 commits touch `reports/`; 22 touch `store/`.

Live composition of `reports/`:

| suffix | files | MB | MB/file |
|---|---|---|---|
| `.subject-grain.md` | 43 | **117.6** | 2.73 |
| `.tsv` | 43 | 20.6 | 0.48 |
| `.md` (set grain) | 43 | 13.0 | 0.30 |
| `.interpretation.md` | 4 | 0.3 | 0.06 |

`.subject-grain.md` is **77.6% of `reports/` by bytes** and the
fastest-growing derived surface. Frank's Q9 ruling in
`docs/design/interpret_subject_grain_v1.md` §6 — *"new samples plus on
demand, no back-fill"* — already declined a ~240 MiB back-fill on review-
weight grounds; the pack numbers say it also declined 218 blobs'
worth of future regeneration cost on every subsequent reporter bump. The
newest group (`2026-09-17-capability-0.1-…`) is 8.11 MB across four
files, of which the subject-grain slice is 6.12 MB.

**This is the growth input the charter did not name**, and it is the
second-largest one. It is also the *good* kind: 159 of 218
subject-grain blobs are deltas, so a regeneration wave that changes a
clause costs a delta, not a copy. Regeneration is affordable **because
the files are plain text** — which is §2's argument from the other
direction.

### 3.3 The NO-HISTORY-REWRITE position

Measured cost of a rewrite: grepping `docs/dev/ledgers/`,
`docs/design/`, `plan.md`, `dev_journal.md` and `outbox_to_pcrec.md` for
7-to-12-hex tokens and testing each against `git cat-file -e
<sha>^{commit}`:

> **248 distinct short SHAs cited in committed prose resolve to commits
> in this repository.** (Restricting to `docs/dev/ledgers/` alone: 21 of
> the 40 distinct hex tokens there.)

A `filter-repo`/`filter-branch` pass rewrites every commit id after the
rewrite point, so every one of those 248 citations becomes a dangling
reference — in the ledgers that are the manager's readings of record,
in `plan.md`'s `[Bn]` rows that cite the merge commit, and in
`outbox_to_pcrec.md` items **that pcrecdev1 has already read and acted
on in a repository this project must not touch**. The cross-repository
half is decisive on its own: BD2 makes ~/pcrec read-only from here, so a
rewrite here would silently invalidate citations there with no way to
repair them.

**Position: history is never rewritten.** Not for size, not for
tidiness. The store's own append-only contract has exactly this shape,
and the history that records it should not have a weaker one.

### 3.4 What would reopen it, and what the options would be

Reopened only by the §1.5 clone trigger — **pack > 500 MB**, against
48.39 MiB today, which at §4.3's growth rate is not this year. Options
at that point, with this project's posture stated:

- **Shallow / partial clone for routine work** (`--depth`, or
  `--filter=blob:none` with `--sparse` excluding `store/`). *Pro:* zero
  repository change, zero policy, reversible, and the full history stays
  intact for anyone who wants it. *Con:* a shallow checkout cannot run
  `make check-report`'s regenerate-and-diff pass. **This lane's
  recommendation if the trigger fires.**
- **An `archive/` branch** holding cold cohorts, never merged into
  `master`. The blobs stay in the same object database (so nothing is
  lost and no external infra appears) but `master`'s tree stops carrying
  them, which shrinks a checkout without shrinking a clone. Pairs
  naturally with §1.4.
- **git-lfs.** *Pro:* built for exactly this shape. *Con, and this lane
  reads it as disqualifying:* LFS requires a server, so a clone of this
  repository would stop being self-contained — **no external infra is a
  project value here**, and the whole `pin.sh`/vendored-dependency
  posture ("dependencies live here, vendored or system, pinned either
  way") is built on it. LFS also defeats delta compression exactly as
  §2.2 measured, and the store's *value* is that `git grep` and `git
  log -p` reach it.

---

## 4. POLICY — a declared retention taxonomy

Proposed, not enacted. The point of writing it down is that today every
directory's retention is implicit, and an implicit rule cannot be cited
in a review.

### 4.1 The three classes

**SOURCE OF TRUTH — append-only, archive-never-delete.** Produced by a
measurement or a human decision, not derivable from anything else in the
repository. Losing one loses information permanently. May be *moved* to
an archive tier under §1.4; may never be deleted or edited.

**DERIVED-BUT-CITABLE — regenerable, and kept because it is the cited
surface.** Mechanically reproducible from a source of truth plus a
committed query, but committed anyway, because prose and rulings cite it
by name and line. Regenerated wholesale when its generator's version
changes. Deletable in principle, and in practice never deleted, because
deleting it breaks citations (§3.3's argument at report scale).

**DISPOSABLE — never committed.** Reproducible at any time by running a
command; gitignored.

### 4.2 Every committed directory, assigned

| directory | class | why | retention |
|---|---|---|---|
| `store/records/` | source of truth | measurements; irreproducible (a pin, a box, a night) | append-only; archive per §1.4 |
| `store/index.tsv`, `machines.tsv` | source of truth | `machines.tsv` is a registry whose ids may never be reused (`store/CLAUDE.md`); the index is regenerable but sha256-stamped by sidecars | append/regenerate in place |
| `docs/dev/ledgers/` | source of truth | the manager's reading; "never edited after its O-n is sent" | append-only |
| `docs/dev/measurements/` | source of truth | archived probes, verbatim, under a source header | append-only |
| `docs/dev/dev_journal.md`, `decisions.md`, `inbox*`, `outbox*` | source of truth | append-only by their own charters | append-only |
| `docs/dev/predictions/` | source of truth | stated and committed BEFORE a run; the whole value is that it cannot be revised after | append-only |
| `bench/*/` (patterns, manifests, expectations) | source of truth | authored sets + oracle-verified expectations; `make check` re-derives them, so they are *checked* but not *derived* | versioned, never deleted (an old `@0.1` is the BEFORE of every cross-version reading) |
| `bench/*/subjects/` | **disposable** | generated + gitignored; `gen_subjects.py` reproduces them byte-for-byte under `make check` | regenerate |
| `reports/*.tsv`, `*.md`, `*.subject-grain.md` | derived-but-citable | reproducible from store + the query in the file's own header; cited by every ledger | regenerate on reporter bump; never delete |
| `reports/*.interpretation.md` | derived-but-citable | `make check-interpret` §3 re-renders and requires byte equality | regenerate on catalogue/index change |
| `catalogue/golden/`, `catalogue/fixtures/` | source of truth | a FROZEN snapshot deliberately decoupled from the live store | frozen; changed only deliberately |
| `schema/examples/`, `examples/bad/` | source of truth | the sabotage corpus; each bad record must be rejected *for the rule its name claims* | append-only |
| `testees/*/list_*.tsv` | source of truth | registry surfaces archived verbatim at a pin; diffed against the pin by `make check-harness` | one set per pin, never deleted |
| `build/`, `build/scratch-store/` | **disposable** | scratch tier by construction; the `.canonical` marker refuses them into `store/` | gitignored |
| `worktrees/` | **disposable** | lane worktrees | gitignored |
| session scratchpad | **disposable** | never committed (BD2/BD3) | — |

Two assignments are worth flagging as judgement calls rather than
readings: `store/index.tsv` is *derived* from the records yet behaves as
a source of truth because four committed sidecars stamp its sha256; and
`bench/*/` is authored-and-checked rather than derived, which is why an
old set version is kept forever rather than regenerated.

### 4.3 A growth budget with named triggers

Measured growth, 2026-08-25 → 2026-09-17 (23 days, 168 records,
1,732,154 rows, 706.7 MB):

- **30.7 MB/day** averaged over the whole span; **26.6 MB/day** over the
  last 13 days (45 records, 345.3 MB) — the rate is flat, not
  accelerating, and the per-record mean has risen (0.75 MB/record on
  2026-08-25 to 7.67 MB/record recently) because the *sets* grew, not
  because anything is leaking.
- **408 bytes/row**, stable across all ten sets (0.38–0.44 KB/row).
  Rows, not records, are the unit that predicts size.
- `.git` grows at roughly 26.6 / 20.1 ≈ **1.3 MB/day** from the store,
  plus report regeneration waves.

Projecting forward from today's 706.7 MB at 7.67 MB per new record (the
recent mean; early small records make a from-zero projection
overstate):

| store reaches | records | working tree | ≈ pack contribution | at 26.6 MB/day |
|---|---|---|---|---|
| today | 168 | 707 MB | 35 MB | — |
| 1 GB | ~206 | 1.0 GB | ~50 MB | ~38 days |
| 2 GB | ~336 | 2.0 GB | ~100 MB | ~75 days |
| 5 GB | ~727 | 5.0 GB | ~250 MB | ~5.5 months |

Proposed budget lines, each naming a consequence rather than a number
for its own sake:

1. **Working tree > 5 GB** → the §1.4 archive tier is built (≈5.5 months
   at today's rate).
2. **Pack > 500 MB** → §3.4's clone options are examined (not reached on
   this trajectory within a year).
3. **A committed query selects > 100 records** → revisit KB-16's
   unaken candidates (b) and (c), which that KB already names as its own
   revisit condition.
4. **Any single report group > 25 MB** → revisit the subject-grain
   slice's granularity (newest group today: 8.11 MB).

### 4.4 Who rules exceptions

**Frank, one question at a time.** Concretely: the *taxonomy* in §4.1-4.2
is a lane's proposal and becomes policy only by ruling; each *trigger*
in §4.3 is a proposal whose firing opens a question rather than
authorising an action; and no record is ever moved out of
`store/records/` without a ruling naming the cohort. The manager may run
`git gc` (§3.1) without asking — it changes no committed byte.

---

## 5. THE CASE FOR A DATABASE

Frank's framing was *"truth — this should be a database but I don't want
to use one."* Both halves are right, and they are about different
things.

### 5.1 The store IS a database workload

- **The shape is relational and always has been.** One record is 1
  `setup` row + N `compile` rows + M `match` rows; measured on the
  store's largest record, 1 / 430 / 21,500, with match rows 94.7% of
  bytes. That is a dimension table and a fact table.
- **Every consumer is a filter-aggregate query.** `report.py` filters on
  six index columns, groups by (pattern, regime, form, testee), and
  reduces to a median with spread. `reduce.py` exists precisely because
  `quick` and the reporter must compute the same aggregate. `interpret.py`
  runs 31 catalogue rules over a rendered table. These are `WHERE` /
  `GROUP BY` / percentile.
- **KB-16 was a missing index, diagnosed and fixed as one.** The fix
  ([B41] (e)) reads `store/index.tsv` as *rows* and prefilters
  candidates on the index-derivable half of the filter predicate before
  opening a file — that is a covering index and a pushdown predicate,
  hand-written. It bought ×6.55 and ×5.28 RSS. The project already built
  a query planner; it just built it out of a TSV.
- **Supersession is a window function.** `report.py:3117-3150` groups by
  a triple, sorts by timestamp, and takes the last row matching a
  predicate. In SQL that is one `ROW_NUMBER() OVER (PARTITION BY … ORDER
  BY …)`.

A prototype, to put a number on it. Eight real records (six
`email-specimen@0.1`, two `bounded@0.3`), 52,900 match rows, 21.4 MB of
JSONL, into stdlib `sqlite3` with one three-column index, `nice -n 19`
on the loaded box:

| | |
|---|---|
| build (parse + insert, single-threaded) | **0.7 s** |
| create index | 0.1 s |
| db size | 15.8 MB (0.74× the raw JSONL) |
| **full `GROUP BY` over all 52,900 rows** | **0.076 s** (147 groups) |
| indexed point query | 0.0002 s |

Extrapolated to the whole store (1,732,154 rows): build ~23 s, size
~520 MB, and **a filter-aggregate across every row in the store in
~2.5 s** — against 116.78 s to render *one seven-record report* today.
Both extrapolations are linear-scaling **PROJECTIONS** from an
eight-record sample; the aggregate is the one this lane would want
re-measured before anything is built on it, and the 0.74× size figure
reflects a deliberately naive schema (every column `TEXT`) and would
fall substantially with typed columns and interned strings.

### 5.2 What JSONL-in-git buys, that a database does not

Stated at full strength, because this is the side the project has
already chosen and the side this lane ends up recommending it keep:

- **Diffable.** `git log -p` over a record is readable. The [B26] census
  concluded "462 census cells byte-identical to a7e0bdf" — a sentence a
  database makes harder, not easier, to write.
- **Greppable.** `grep -r` over the store answers questions nobody
  designed a query for. §1.3's central finding — 25 of 32 superseded
  records are cited in a report — came from grepping ids against report
  text; there is no schema in which that join was anticipated.
- **Schema-validated at write.** `schema/validate.py` enforces X1..X33 —
  including X3 (the id equals the id derived from five fields) and X4
  (filename equals id) — and `make check-schema` proves every
  `examples/bad/` record is rejected *for the rule its name claims*.
  That is a constraint system with a sabotage corpus, and it is stronger
  than what a hand-rolled SQLite schema would carry.
- **Self-verifying bytes.** `content_hash` (§1.1) covers every byte of
  every record.
- **Zero infrastructure.** No server, no daemon, no port, no version
  drift, nothing to be down at 03:00 during a window.
- **Survives tooling loss.** If `pcrecbench` vanished tomorrow, the
  records would still be readable with `cat`, and `record_schema.md`
  documents every field. A `.sqlite` file without its schema is a
  liability; this project's discipline documents are written as though
  the reader has lost the tools (`docs/dev/CLAUDE.md`: the journal is
  "the primary restart/status-recovery record").
- **It is already the review surface.** `make check` has 4/72/0 ·
  324/324 · 71+7 · 132 checks built on these files being files.

### 5.3 THE COMPROMISE, to examine: SQLite as a DERIVED CACHE

Not a recommendation to adopt — a recommendation to *examine*, with its
invariants written down first so that adopting it later cannot quietly
become adopting a database.

**Shape.** A single `store/.cache.sqlite`, **gitignored**, built and
refreshed by `pcrecbench index` from the JSONL it already walks
(`store.iter_records`). `report.py` and `interpret.py` read the cache;
the JSONL stays canonical. Stdlib `sqlite3` only — no new dependency,
consistent with `requirements.txt`'s single pin.

**Invariants, non-negotiable if it is ever built:**

1. **The cache is never a source of truth.** It is in `.gitignore`, it
   is in §4.1's disposable class, and a fresh clone with no cache must
   produce byte-identical reports (slowly) from the JSONL alone.
2. **Any divergence means rebuild, never repair.** The cache stores each
   record's `content_hash` and the index's sha256; a mismatch drops the
   cache and rebuilds. There is no reconciliation path, because a
   reconciliation path is how a cache becomes a database.
3. **The validator still gates writes.** `store.write()` is unchanged;
   nothing enters the cache that did not pass X1..X33 on its way into a
   file first.
4. **The cache never decides anything the report renders.** It may
   answer *which records* and *which rows*; the reduction, the
   supersession rule, the status policy and the trial-agreement rule all
   stay in Python, shared, exactly as `reduce.py` is shared today.
5. **Byte-identity is the acceptance test.** Every committed report
   re-renders byte-for-byte from the cache and from the JSONL. That is
   the same proof [B41] used for KB-16 and [B13.2] used for the v16
   regeneration; the project already has the harness for it.

**What it likely does for KB-16's residual.** The 116.78 s is
validation + object construction over six records. A cache that stores
already-validated rows removes both from the hot path, leaving query
time. **PROJECTION** from §5.1's prototype: seconds, not minutes.
**UNMEASURED**, and the honest version is that nobody has yet shown a
*committed query* that hurts today.

**The risks, and the one that matters.**

- **Dual-read-path drift** — the real one. Two paths that compute "the
  same" aggregate diverge silently, and a wrong number in a report is
  the worst failure this project can have. The mitigation already
  exists as practice: `reduce.py` is the shared reduction precisely so
  that `quick` and the reporter cannot disagree, and `make check-harness`
  checks a `quick` cell's printed median against a hand-computed one
  from its own file. Extending that discipline means the cache supplies
  *rows*, never *aggregates* — invariant 4 — and one `make check` arm
  renders a committed report both ways and `cmp`s them.
- **A stale cache silently answering.** Mitigated by invariant 2, and by
  making the staleness check cheap (sha256 of `index.tsv` plus record
  count) rather than thorough.
- **Scope creep into a source of truth.** The failure mode is social,
  not technical: someone writes a row to the cache that is not in a
  record. Invariant 1 plus `.gitignore` is the whole defence, and it is
  the reason the cache must be *deletable at any moment without loss*.
- **~520 MB of gitignored file** on a box that already holds the store
  (**PROJECTION**, naive schema).

**No served database.** Frank has ruled that posture out, and this note
does not reopen it. The distinction that makes SQLite-as-cache a
different proposal: there is no server, no port, no daemon, no
migration, and no state that survives `rm`.

---

## 6. SYNTHESIS — phases, and the questions

### 6.1 Phases

**Phase 0 — now, cheap, no ruling needed beyond Q1/Q2.**

| action | cost | status |
|---|---|---|
| Adopt §4's retention taxonomy as declared policy | one design-note ruling; no code | measured cost: zero |
| `git gc` as routine hygiene after regeneration waves and at session close | one command, minutes on a quiet box | saving ~30 MB **PROJECTED** (§3.1) |
| Record the growth law (408 B/row, 26.6 MB/day) and the four triggers in §4.3 | prose | measured |
| Adopt the no-history-rewrite position formally | prose | 248 SHA citations measured as the cost |

**Phase 1 — on a named trigger, not a date.**

| trigger | action | cost |
|---|---|---|
| working tree > 5 GB (~5.5 months) | build the §1.4 archive tier | ≈ one [B31]-sized lane; **UNMEASURED** |
| a committed query selects > 100 records | examine §5.3's SQLite cache | ≈ one lane + a byte-identity gate; **UNMEASURED** |
| pack > 500 MB (not on this trajectory this year) | §3.4's shallow/partial clone | small; **UNMEASURED** |

**Phase 2 — explicitly NOT proposed.** Compressing the committed store
(§2.2: +15.3% pack, measured). Rewriting history (§3.3: 248 citations).
A served database (ruled out). Culling by the superseded predicate
(§1.3: would break 25 of 32).

### 6.2 What this lane would do if it could do exactly one thing

Adopt §4.2's table, and run `git gc`. Everything else is a trigger away.

### 6.3 QUESTIONS FOR FRANK

Each is self-contained and carries a recommendation.

---

**Q1. Adopt §4.1-4.2's retention taxonomy — source-of-truth /
derived-but-citable / disposable, with every committed directory
assigned — as declared project policy?**

*Recommend: YES.* It costs nothing, changes no file, and makes every
later question answerable by citation instead of argument. Today the
rules exist (append-only records, regenerate-every-report, scratch never
enters the store) but are scattered across five CLAUDE.mds; the table
puts them in one place. The two judgement calls worth your eye are
`store/index.tsv` (derived, but treated as source-of-truth because four
sidecars stamp its sha256) and `bench/*/` (authored-and-checked, so an
old `@0.1` set is kept forever as the BEFORE of every cross-version
reading).

**RULED 2026-09-19 (Frank, live): YES** — §4.1-4.2's taxonomy is
declared project policy, both judgment calls as stated.

---

**Q2. Make `git gc` routine — after every report-regeneration wave and
at every session close?**

*Recommend: YES, and it needs no further ruling after this one.* The
repository has 2,257 loose objects holding 293.3 MB of logical content
at 6.9×, where the pack achieves 25.1×; `git gc --auto` will not fire
because its threshold is 6,700. Projected saving ~30 MB, taking `.git`
from ~100 MB to ~65-70 MB. It changes no committed byte and is
reversible in the sense that nothing is lost. Not run by this lane: it
mutates a `.git` shared with live worktrees and is CPU-bound, and
pcrec's battery owned the box.

**RULED 2026-09-19 (Frank, live): YES — "only because making it
periodic would be more work."** The manual-at-boundaries shape (after a
regen wave, at session close, never mid-lane) is adopted as the
low-effort option, not as hygiene enthusiasm: if this ever grows into
automation proposals, that is more work than Frank wanted, and the
ruling does not cover it.

---

**Q3. Adopt the no-history-rewrite position formally — history is never
rewritten, for any reason including size?**

*Recommend: YES.* Measured cost of ever doing it: **248 distinct short
SHAs cited in committed prose resolve to commits in this repository**,
across ledgers, `plan.md` rows, the journal and `outbox_to_pcrec.md`.
The outbox half is the decisive one — those items have been read and
acted on by pcrecdev1, in a repository BD2 makes read-only from here, so
a rewrite would invalidate citations we could not then repair. §3.4's
shallow/partial clone gets the same benefit with none of the cost, if a
trigger ever fires.

**RULED 2026-09-19 (Frank, live): YES** — history is never rewritten,
for any reason including size. Frank's follow-up question answered for
the record: a committed-then-deleted large file DOES remain in local
history forever (the blob stays reachable from every historical commit;
gc never touches reachable objects) and IS copied into every ordinary
clone; only shallow (`--depth`) or partial (`--filter=blob:none`)
clones avoid transferring it, clone-side, and only the now-forbidden
history rewrite removes it at origin. Hence pre-commit size discipline
(Q4) is the one cheap point of control.

---

**Q4. Confirm that compressing the committed store is OFF the table —
that the working-tree saving does not justify the history cost?**

*Recommend: YES, off the table, and revisited only if a checkout's size
on disk ever becomes a binding constraint.* Measured on fourteen real
records committed write-once: plain packs to 390,207 B, `zstd -3` to
449,720 B — **+15.3%**, because 149 of the store's 168 record blobs are
currently stored as deltas against *other records*. Git already gets
20.1× on the plain store. What compression would buy is the working tree
(674 MB → ~29 MB), and what it would cost is 15% of the pack forever, a
larger `git clone`, a Python floor raised from 3.11 to 3.14 (zstd is
stdlib only from 3.14), and a loader change. The trade flips only if
checkout size becomes the constraint; it is not today, at 843 MB total.

---

**Q5. Are §4.3's four growth triggers the right ones — and is a
*consequence* threshold (checkout size, clone size, query breadth) the
right shape, rather than a threshold on the store's size?**

*Recommend: YES to consequence-shaped triggers.* The store's raw size
has not hurt anything: the one operation that actually hurt (KB-16's
765.67 s / 3.84 GiB) was fixed by reading the index first, not by
shrinking the store, and the store has grown since. The four proposed:
working tree > 5 GB (~5.5 months at 26.6 MB/day) → build the archive
tier; a committed query selecting > 100 records → examine the SQLite
cache; pack > 500 MB (48.39 MiB today) → examine clone options; any
single report group > 25 MB (8.11 MB today) → revisit the subject-grain
slice.

---

**Q6. When the archive tier is eventually built, which form — an
`archive/` branch never merged into master, or committed
`store/archive/<cohort>.tar.zst` tarballs?**

*Recommend: the BRANCH, and this is a ruling worth making in advance so
the trigger does not arrive with an open question attached.* A branch
keeps blobs in the same object database (nothing leaves, no external
infra) while `master`'s tree stops carrying them, and the archived
records stay individually addressable, greppable and delta-compressed.
A committed tarball is a single high-entropy blob: git cannot delta it,
and every addition to a cohort re-blobs the whole thing (§2.2's trap in
its worst form). The tarball's one advantage is that a reviewer can see
one file rather than a branch, which does not outweigh it.

---

**Q7. Does an archived record's absence from a report's query REFUSE the
render, or render a smaller report with a note?**

*Recommend: REFUSE, by name.* Silently dropping a record from a ranking
is exactly the failure that OD-B14 (status policy), OD-B15
(supersession) and the v1.4 spread rule all exist to prevent — each of
them makes a set-aside record *visible* rather than absent. An archived
record should behave the same way: the reporter names it and stops, and
`pcrecbench archive restore <record_id>` is a one-line fix. This is a
small ruling with a large blast radius, which is why it is separate from
Q6.

---

**Q8. Is the store's failed-gate cohort — 9 `inconclusive-load` and 2
`inconclusive-spread` records, of which 7 are cited by nothing —
worth keeping indefinitely?**

*Recommend: YES, keep.* They are 18.4 MB, 2.6% of the store, and 16
hours of growth at the current rate. They are also the only durable
evidence that the gate fires: BD7's five one-shot after-sample losses,
the v1.4 spread rule's first production firing, KB-4. Archiving them is
the *only* globally-safe cull available today (§1.3), which is precisely
the argument that culling is not worth mechanising yet — the safe set is
this small. If you rule the other way, they are the cohort to start
with.

---

**Q9. Charter a lane to examine SQLite-as-derived-cache (§5.3) — a
design note with a measured prototype, not an implementation?**

*Recommend: NOT YET — hold it behind Q5's "a committed query selects >
100 records" trigger.* The prototype numbers are attractive (8 records /
52,900 rows: build 0.7 s, full `GROUP BY` 0.076 s; extrapolated to the
whole store, ~23 s to build and ~2.5 s to aggregate every row, against
116.78 s to render one seven-record report today). But KB-16 is closed,
no committed query hurts today, and the cost is a second read path —
the one risk in this note that can put a wrong number in a report. §5.3
writes the five invariants down now so that if the trigger fires, the
lane starts from them rather than inventing them under pressure.

---

**Q10. Does the subject-grain slice need a growth ruling of its own?**

*Recommend: NOT YET, and here is the number your Q9 ruling was worth.*
`.subject-grain.md` is **117.6 MB of `reports/`'s 151.5 MB — 77.6%** —
across 43 groups, and `reports/` has produced 713 blob versions and
32.12 MB of pack against `store/`'s 187 versions and 35.21 MB, because
every reporter bump regenerates every group. Your "new samples plus on
demand, no back-fill" ruling declined ~240 MiB of committed TSV *and*
218 blobs of future regeneration on every subsequent bump. At 6.12 MB
for the newest group's slice, §4.3's trigger 4 (any group > 25 MB) is
the one to watch.

---

**Q11. Is `docs/design/data_management_v1.md` the right home for this,
and should it go to a D6 panel before any of Q1-Q10 is ruled?**

*Recommend: the file is the right home; NO panel before Q1-Q3.* Q1-Q3
are cheap, reversible and measured, and each would survive a panel
unchanged. The parts that would benefit from a panel are §1.4's archive
tier and §5.3's cache — both of which are Phase 1, behind triggers, and
both of which should be paneled *when their trigger fires*, against the
numbers that fired it rather than today's.

---

## 7. Appendix — every claim's provenance

Measured 2026-09-17, 15:30-16:10 EDT, `budu-ryzen1600`, commit
`77bc390`, under pcrec's battery (load 3.75/7.64/7.20 on 12 cores), all
probes `nice -n 19`.

| § | claim | how |
|---|---|---|
| 0, 1.2 | 168 records, 1,732,154 rows, 706.7 MB, 408 B/row | `store/index.tsv` + `os.path.getsize` per row |
| 0, 2.2 | store 674 MB working tree; reports 145 MB; `.git` 100 MB | `du -sh --apparent-size` |
| 1.2 | superseded 32 / 96.9 MB; kept 136; newer-not-measured 0 | `report.py:3117-3150`'s exact rule re-implemented over the index |
| 1.3 | **25 of 32 superseded records named in a committed report** | grep of record ids against all `reports/*.md` + `*.tsv` |
| 1.3 | safe cold set = 7 records / 18.4 MB / 2.6% | intersection of the two above |
| 2.1 | zstd-3 24.34×, gzip-6 21.23×, zstd-19 35.71× | 20 records (largest + one seeded-random per set), 106.1 MB |
| 2.1 | 1 setup / 430 compile / 21,500 match rows, 94.7% match bytes | line-kind census of the store's largest record |
| 2.1 | tar.zst buys ~15% over per-file | two sets, `tar \| zstd -3` vs per-file sum |
| 2.2 | 149 of 168 store blobs are deltas; per-surface ratios | `git cat-file --batch-all-objects --batch-check` with `%(deltabase)`, joined to `git rev-list --objects --all` |
| 2.2 | same-path: 92,334 B plain vs 93,795 B zstd | throwaway repo, 3 versions, `gc --aggressive` |
| 2.2 | **write-once: 390,207 B plain vs 449,720 B zstd (+15.3%)** | throwaway repo, 14 records, one commit, `repack -adq` |
| 2.2 | same, aggressive: 390,360 B vs 449,721 B (+15.2%) | re-run with `repack -adf --window=250 --depth=250` on both arms |
| 2.3 | decompress 0.014 s vs `json.loads` 0.222 s | store's largest record, warm cache, best of 3 |
| 2.3 | KB-16 CLOSED; 765.67 s → 116.78 s, 3.84 GiB → 745 MiB | `docs/dev/known_issues.md:634-672`, measured by lane b41 |
| 2.4 | Python 3.14.4; `compression.zstd` in stdlib; `pyproject` floor 3.11 | `python3 -VV`, import probe, `pyproject.toml` |
| 3.1 | pack 48.39 MiB / 6,097; loose 47.68 MiB / 2,257; 25.1× vs 6.9× | `git count-objects -vH` + the blob census, split by loose-object presence on disk |
| 3.1 | **~30 MB gc saving** | **PROJECTION** from the two ratios; not run |
| 3.2 | reports 713 blobs / 32.12 MB pack vs store 187 / 35.21 MB | the blob census, grouped by top-level dir |
| 3.2 | 15 versions of the oldest report `.tsv`; 48 vs 22 commits | `git rev-list --count HEAD -- <path>` |
| 3.2 | `.subject-grain.md` 117.6 MB = 77.6% of `reports/` | `os.path.getsize` by suffix |
| 3.3 | **248 short SHAs in committed prose resolve to commits here** | grep `[0-9a-f]{7,12}` over ledgers/design/plan/journal/outbox, each tested with `git cat-file -e <sha>^{commit}` |
| 4.3 | 30.7 MB/day overall; 26.6 MB/day last 13 days | index timestamps + file sizes |
| 5.1 | 8 records / 52,900 rows: build 0.7 s, db 15.8 MB, GROUP BY 0.076 s | stdlib `sqlite3` prototype, one index |
| 5.1 | whole store ~23 s build, ~520 MB, ~2.5 s aggregate | **PROJECTION**, linear from the above |

Unmeasured and named as such: the `git gc` saving (§3.1); the archive
tier's build cost (§1.4); the SQLite cache's effect on a real report
render (§5.3); whether any box but this one has run the harness (§2.4).
