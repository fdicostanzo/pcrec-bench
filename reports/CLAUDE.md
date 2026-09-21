# reports/ — generated reports over the store

Each file is the output of one `python3 -m pcrecbench report ...` query,
committed beside the records it reduces so a reader can cite a number
with its query. Names: `<date>-<subbench>-<version>-<machine>[-<label>][.<grain>].md|tsv`.

## `.interpretation.md` sidecars ([B13.4])

Some report groups carry a fourth sibling,
`<name>.interpretation.md`, beside the `.tsv`/`.md`/`.subject-grain.md`.
It is the output of `pcrecbench interpret --render`
(`docs/design/interpreter_v1.md`): a deterministic, catalogue-driven
fact-finder over the report `.tsv` and `store/index.tsv` — never the
`.md` rendering — that names every fired rule from `catalogue/rules.toml`
with its rows and numbers, and every rule that did NOT fire with the
reason. It is a **sidecar, never a section of the report itself**: the
report stays a deterministic, diffable table and bumps its own
`REPORTER_VERSION` for its own reasons; the sidecar bumps with the
catalogue instead.

A sidecar is **generated and never hand-edited**. Its opening HTML
comment stamps the report path and its sha256, the index path and its
sha256, the predictions file (if any) and its sha256, the subject-grain
file (if any) and its sha256 ([B47], `interpret_subject_grain_v1.md` §6
Q10, unconditional since catalogue 2.0), the catalogue version, and the
`interpret`/`reporter` versions — `make check-interpret` section 3
re-renders every committed sidecar from that stamp and requires byte
equality, so a stale one is a `make check` failure. Regenerate one with
the skill, never by hand: `/pcrec-bench-interpret <report>`
(`.claude/skills/pcrec-bench-interpret/SKILL.md`), whose own text states
the full opinion-firewall rule — a wrong or missing finding is a
catalogue change (`catalogue/rules.toml`), not an edit to the rendered
file. Committed today: the three `docs/design/interpreter_v1.md` §10
acceptance reports (A, B, C) plus the capability-0.1 first sample; the
rest are generated on demand (§11 Q5).

## `.matrix.tsv` / `.matrix.html` siblings ([B52], 2026-09-18)

A group may also carry `<name>.matrix.tsv` — the CANONICAL tests-x-
engines ratio matrix (Frank's ruling, docs/dev/dev_journal.md, the
twenty-fifth session close): `pcrecbench report --format matrix` (same
query as the group's own `.tsv`/`.md`, `--grain set` — the format
refuses BY NAME at `--grain subject`, a matrix row has no subject
dimension). One row per timing cell `(subbench, pattern, regime_or_na,
form)`, one column per testee in the query's own roster, every cell
EITHER a `median_ns / row-best` ratio (six decimals) or one of five
CLOSED status tokens (`unsup`/`refused`/`wrong`/`gave-up`/`excluded`) —
NEVER blank. `best_testee`/`best_ns` columns carry the row's absolute
scale. **F26-immune by construction**
(`docs/design/predicate_audit_v1.md`): a pattern refused or declared
unsupported by every testee in the roster still gets one full row
(`regime_or_na=""`/`form=""`), where `render_tsv`'s own ranking-group
loop would have produced no row anywhere. The file's own two-line
header comment states the ratio definition, the within-row-only
comparability rule, the closed-token meanings and the F26-immunity
sentence — Frank's context-around-numbers directive
(`docs/dev/decisions.md`): what a cell means travels WITH the numbers,
not in a separate design note a Claude-consuming reader might not open.
Full design: `pcrecbench/CLAUDE.md`'s `[B52]` section, `report.py`'s own
module docstring.

`scripts/matrix_page.py` renders any `.matrix.tsv` into
`<name>.matrix.html` — a dependency-free, self-contained page (sticky
table, log-scale colour ramp, one chip per status token, a hover
tooltip recovering each cell's absolute median, light + dark themes).
The `.html` is DERIVED and regenerated on demand
(`python3 scripts/matrix_page.py <name>.matrix.tsv`), never hand-edited;
whether `.matrix.html` files are committed alongside their `.tsv` or
generated on demand only is a call for whichever window/manager session
first regenerates the full `reports/` set under reporter v18 — this
lane ships the capability, not the regen (see the note below).

**BACKED-FILLED 2026-09-18 (lane b53regen)** — [B52]'s own regen wave,
charter item 2 of Frank's matrix-standard ruling. All 45 committed
report groups (138 `.tsv`/`.md`/`.subject-grain.md`/`.subject-grain.tsv`
files) re-rendered from each file's own committed query (parsed from its
header line — KB-16 is closed, so every render is a narrow CLI
invocation, seconds to tens of minutes depending on the group's own
subject-grain size, never a whole-store load) and diff-classified
against the last commit. **Two expected classes only, on every changed
line, zero exceptions**: the `reporter: v17` → `v18` version-line
replace, and the new unconditional `baseline` bullet (`.md`) / row
(`.tsv`) — item 3's baseline-identity fact — on every rankable group.
Zero anomalies, zero subprocess failures, zero unexplained deltas. New:
one `.matrix.tsv` + `.matrix.html` sibling per group (45 + 45,
`scripts/matrix_page.py`, all rendered clean). The six committed
`reports/*.interpretation.md` sidecars were also regenerated
(`scripts/regen_sidecars.py`, 0 failures, all determinism-checked) and
the 65-fixture `catalogue/fixtures/` corpus re-derived against the moved
report content (same precedent as commit b6ee4e4's v17-bump fixture
regen; `gen.py --check` clean); `make check-interpret` 149/149.

**Two things a reader of this wave should know:**
- **The classifier itself was the wave's own incident.** The first pass
  used `difflib.SequenceMatcher` (an O(n²) worst case) and hung for ~4 h
  inside one group's multi-million-line `.subject-grain.md` diff before
  the manager caught it from outside (CPU/no-child-process forensics) and
  the lane replaced it with a linear two-pointer classifier (the two
  expected delta shapes are both locally resolvable by looking at only
  the current pair of lines — no alignment search is needed) and resumed
  from the stuck group, skipping the two sub-renders it had already
  landed correctly before the hang. KB-18's own lesson two waves ago was
  "a legitimate class the classifier missed"; this wave's is classifier
  *complexity* — a correct classifier that could not finish.
- **`scripts/regen_sidecars.py` had a real, separate, second-order bug**
  (KB-22, `docs/dev/known_issues.md`): it recovered a sidecar's
  `report`/`index`/`predictions` inputs from the sidecar's own stamp but
  never `subject_grain`, so regenerating either of the two
  `.subject-grain.tsv`-backed capability sidecars silently DROPPED
  R-BUCKET-DOMINATED's whole section (33 firings) while still passing
  its own determinism check — self-consistent, just wrong, and invisible
  until this wave was the first time the script ever ran against a
  subject-grain-stamped sidecar. Fixed in the same lane; both sidecars
  confirmed restored byte-identical below the stamp to their pre-regen
  content.

No committed report's TIMING NUMBERS moved — this wave changes only the
reporter's own rendering surface (the version stamp and the new
baseline fact), never a record, a query result, or a ranking.

## `.subject-grain.tsv` siblings ([B47], 2026-09-17)

A group may also carry `<name>.subject-grain.tsv` beside its
`.subject-grain.md` — the §6 Q4 SLICE
(`pcrecbench report --grain subject --format tsv --subject-grain-slice`,
`docs/design/interpret_subject_grain_v1.md` §6.7): every `record` row,
every `rank` row's `median_ns` metric (the other five per-cell metrics
dropped), and the `excluded`/`not_ranked`/`scratch`/`did_not_compile`
sections whole, with `compile`/`compile_stamp` dropped outright — same
18-column shape as the plain `.tsv`, ×4.8 its size rather than the full
`--grain subject`'s ×28.5. It is `interpret`'s second input
(`--subject-grain`), consulted by R-BUCKET-DOMINATED and by any
prediction clause whose selector names `grain=subject`. **No back-fill**
(§6 Q9): exactly one group carries one today,
`2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8` (chosen for
a real R-BUCKET-DOMINATED firing — `orig`/`large-subject-throughput`/
`libpcre2_10.46_interp-caps-simdna` at a 99.877% share on subject
`t-a-valid-addrs`); new samples and on-demand requests are the only
route to a second one.

**KB-18 (2026-09-17, lanes b42repdiag → b42repfin) regenerated EVERY
committed report against reporter `v17 (2026-09-17)`** (a did-not-compile
diagnostic is now carried FULL and verbatim, never truncated to its
first line -- docs/dev/known_issues.md KB-18, `pcrecbench/CLAUDE.md`'s
report.py entry). All 43 groups (129 files: 43 `.tsv` + 43 `.md` + 43
`.subject-grain.md`) re-rendered from their OWN committed query and
diffed against the LAST COMMIT before being written back:

- **41 groups are byte-identical but for the version-line stamp**
  (`reporter: v16 (2026-09-08)` -> `v17 (2026-09-17)`, one line, every
  file).
- **`2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.*` moves
  exactly as KB-18 intended** (5 lines changed in `.tsv`/`.md`, 157 in
  `.subject-grain.md`): the four `wild-waf-crs-942500-comment-
  obfuscation` did-not-compile rows (both `pcrec-auto`/`pcrec-auto-
  nocaps`, both `large-subject-throughput`/`short-subject-search`) now
  carry gcc's full transcript in place of `[truncated, diagnostic
  continues]` -- the finding KB-18 exists to fix.
- **`2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.*` ALSO moves**
  (85 lines in `.tsv`/`.md`, 2437 in `.subject-grain.md`) — diagnosed
  and CONFIRMED as NOT store drift before being accepted: the group's
  query already carries an explicit `--since 2026-09-07T00:00:00Z
  --until 2026-09-07T05:00:00Z` pair (the 2026-08-30 rule), and both the
  committed and the re-rendered header read `records: 6; excluded_invalid:
  0; superseded: 0; newer_not_measured: 0` — the identical six records,
  not a shifted population. The real cause is the SAME KB-18 escaping
  rule firing on ordinary single-line diagnostics: seven bench/syntax
  patterns' pcrec diagnostics quote a literal backslash-letter escape
  sequence with no embedded newline at all — `esc-ctrl` (`` \c ``),
  `esc-octal-o` (`` \o ``), `msc-c-uc` (`` \C ``), `msc-r-uc` (`` \R ``),
  `msc-x-uc` (`` \x ``), `unp-p-lc`/`unp-p-uc` (`` \p{...} ``) — each
  rendering e.g. `` \c `` as `` \\c `` for the SAME lossless-
  reversibility reason `_diagnostic_full`'s docstring states (a `\n`
  escape must render distinguishably from a real embedded newline, so
  EVERY backslash is escaped, not only ones beside a control character).
  Confirmed by `git diff` against the last commit: every one of the 85
  (resp. 2437) changed lines is a `did_not_compile` row (or its
  `subject-grain` expansion) or the bullet-list equivalent on one of
  those seven pattern ids, nothing else. Neither this lane's own
  one-record manual proof nor the disposable `regen_reports.py` scratch
  tool's diff classifier (which only recognised the OLD truncation
  marker as an expected class) anticipated this population before the
  regen ran; the `--until`-drift hypothesis considered first (the [B12]
  precedent) was RULED OUT by the unchanged record count and the
  already-present `--until` clause, then abandoned once the real cause
  was found in the diff content itself.
- **The four committed `reports/*.interpretation.md` sidecars were also
  regenerated** (`scripts/regen_sidecars.py`, 0 failures, all
  determinism-checked): the capability sidecar's own finding line now
  shows the full gcc transcript in place of the old truncation marker,
  proving the fix reaches the interpreter's fact-finding path, not only
  the reporter's own render.

**[B13.2] (2026-09-08, lanes b13pre → b13regen → b13regen2 → b13fin)
regenerated EVERY committed report against reporter `v16 (2026-09-08)`**
(docs/design/interpreter_v1.md §2.5's two reporter preconditions,
`pcrecbench/CLAUDE.md`'s report.py entry). All 42 groups (126 files: 42
`.tsv` + 42 `.md` + 42 `.subject-grain.md`) re-rendered from their OWN
committed query (parsed out of each `.tsv`'s own header line, the
interpreter design's §2.1 header-parsing rule) and diffed against the
committed content before being written back; every diff was explained
by one of four deltas, in ANY combination, before landing — never a
partial or silently-wrong regeneration:

- **The version-line stamp**, every file (126/126): `v12`/`v13`/`v14`/
  `v15` → `v16` (26 files were at `v12 (2026-09-02)`, 5 at `v13
  (2026-09-03)`, 5 at `v14 (2026-09-05)`, 6 at `v15 (2026-09-05)`).
- **P-1's `floor_pattern:` header key**, every `.tsv` (42/42): `floor`
  on 40 files (every set that has adopted [B15]'s floor pattern),
  `none` on the two pre-1.3 `email-specimen@0.1` files.
- **P-2's `giveup_smallest` rows**, `.tsv` only: 60 rows added across 8
  files — seven `email-specimen` groups (both `@0.1` files, five of
  six `@0.2` ones: 7+12+5+10+5+10+10 rows) and one `altwide` group
  (`2026-09-03-altwide-0.2-*-bigcap-1989c62`, +1 row); every other
  `.tsv` +0 — no other set's `excluded` section carries a give-up. Rows
  are wholly NEW lines (`$11 == "giveup_smallest"`); no existing row
  moved or changed.
- **The manager-ruled cwd-independent provenance-path fix**: exactly
  the ten 2026-09-05 groups named in `pcrecbench/CLAUDE.md`'s report.py
  entry (20 files: `.md` + `.subject-grain.md` siblings), each an
  11-line record-listing block (`../../store/records/...` →
  `store/records/...`) that shifts together under diff — not 11
  independent single-line replaces.
- **The v13/v14 → v16 legend-bullet backlog**: 8 files (4 groups × 2
  siblings — `2026-09-05-altwide-0.2-*-after-334fd10e`,
  `2026-09-05-bounded-0.3-*-fold-334fd10e`, `2026-09-05-loglines-0.1-*
  -noedge-334fd10e`, `2026-09-05-loglines-0.1-*-noedge-3pins-334fd10e`,
  every one `334fd10e`-stamped), 1 new legend line each: the `shape=`
  bullet gaining the `prog: N B` paragraph (I-50 §1's reconcile,
  shipped as part of v15 but never before regenerated onto a
  pre-v15-stamped file), byte-identical to the same-subbench v15
  reference (`2026-09-06-altwide-0.2-*-after-d34c9131.md` etc., read
  from `git show HEAD:` — the pre-regeneration committed content, never
  from disk after this wave started overwriting v15 stamps with v16).

**Proof**: the brief's own filtered `git diff` over `reports/*.tsv`
(strip the `reporter:` header line and any added `giveup_smallest` row)
prints nothing; an independent per-hunk classifier over `git diff -U0
-- reports/*.md` (disjoint-category matching against the four deltas
above) finds **zero unexplained deltas across all 84 `.md`/
`.subject-grain.md` files** — 20 with the cwd-path fix, 8 with a legend
line, every file with exactly one version-line change.

**Regenerated IN-PROCESS** (load and validate `store/`'s 160 records
ONCE — **751.0 s**, the store's current size, `[B36]`'s 748 s
precedent holding — reused for all 42 renders, split into two phases
by lane b13regen2 specifically so this cost is paid ONCE total across
however many classifier-fix iterations it takes: Phase A renders every
non-v16 group to a scratch cache; Phase B, no store load, classifies
the cache against `reports/` and writes on a clean classification,
safely re-runnable). The `2026-09-07-syntax-0.1-*-first-d34c9131`
group's `.subject-grain.md` (10.2 MB, ~108k lines) made
`difflib.SequenceMatcher` pathologically slow in the classifier itself
(100% CPU, still running after 100+ CPU-seconds; killed once by the
tracked-task memory heuristic, once by hand) — fixed with an equality
fast path (compare the normalized line lists directly, O(n) with
early-exit, before ever calling `difflib`) in both `classify_tsv_diff`
and `classify_md_diff`, which let that group finish in seconds; almost
every group's body is unchanged after normalization, so the fast path
fires on nearly all 42.

**[B36] reports (2026-09-07, lane b36read) ADDED ONE file group — the
2026-09-06/07 OVERNIGHT window at pcrec pin d34c9131 (abi 23), the
`bench/syntax@0.1` CENSUS's FIRST SAMPLE** — and changed NOTHING else here:
the reporter is unchanged at `v15 (2026-09-05)`, no committed report was
regenerated, no reporter code was touched. All three files carry an explicit
`--since`/`--until` PAIR *and* the six-id `--testee` roster (the 2026-08-30
rule and KB-5). The window: 6 cells, ALL `measured` at attempt 1 under BD7,
record timestamps 2026-09-07 00:32:11Z → 04:06:05Z (3 h 34 min end to
end; successive cell STARTS 35-54 min apart), store 155 → 161; the six records were committed on
master (`28cb034`) before these were rendered; this lane rendered from
`--store ~/pcrec-bench/store` and commits no store file.

RE-RENDER INVARIANT, checked the same two ways as the [B37] and [B39] waves,
because the three files were rendered IN-PROCESS (the 160-record store loaded
and validated ONCE — **748 s on this box**, the longest yet: this set's six
records carry 35,859-41,800 rows each — and reused for all three; the same
`build_report` / `render_markdown` / `render_tsv` calls a CLI invocation
makes; the three files then rendered in 118 s):

1. **CLI equivalence**, proven on
   `2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv`: that file was
   re-produced by a full `python3 -m pcrecbench report …` invocation of its
   own committed query and `cmp`s BYTE-IDENTICAL against the in-process
   render.
2. **Determinism over all three**: a second, independent in-process render
   into a scratch directory diffs clean on all three files (`cmp` on each).

FIVE THINGS A READER OF THIS WAVE SHOULD KNOW BEFORE THE NUMBERS:

- **THREE R0 CELLS ARE THE INSTRUMENT'S, NOT AN ENGINE'S**, and two of the
  three were not predicted. (i) The nine `rec-r-uc`/`rec-1`/`rec-name` ×
  throughput cells that read `expected 116 non-overlapping match(es);
  observed 5` on `pcre2-jit` AND all four pcrec arms are a **give-up the
  find-all loop cannot spell**: a read-only ctypes probe on the same subject
  returns `PCRE2_ERROR_JIT_STACKLIMIT` (−46) at the sixth start, after five
  spans identical to the interpreter's, and both drivers
  (`testees/pcre2/driver.c:321-340`, `testees/pcrec/driver.c:714-731`)
  discard a negative return that arrives after the first match. **Five of six
  testees are therefore silently absent from three of the 285 rankings**
  (report line 5229 ranks the interpreter alone, flagged `dominated`).
  (ii) `asr-k-uc` / `match-compliance` / `whole-subject` / `f-kv` reads
  `expected span [4,9]; observed [0,9]` on all four pcrec arms because the
  pcrec driver's anchored branch hard-codes `first_s = 0` — the
  whole-subject form cannot report a `\K`-reset start. (iii) `rec-r-uc` /
  `f-parens` / whole is P2's predicted wrapper wrong answer, confirmed with
  its two controls clean.
- **`mod-x` is an R1 refusal on the WHOLE-SUBJECT FORM ONLY** (report line
  4133, four `not ranked … missing closing ) for group` lines): wrapped,
  `(?x) c a t # comment` becomes `(?:(?x) c a t # comment)\z` and the `/x`
  comment swallows `)\z`. `esc-hex-braced` — P1's fifteenth predicted
  refusal — COMPILES, which is the abi-23 re-seed working as NOTES foresaw.
- **The `auto` route's throughput ratio against the JIT is a function of its
  own prefilter stamp**, monotone over six buckets and 55 DFA cells:
  `none` **0.158** → `memchr` **0.728** → `byte-class` **0.997** →
  `offset-set` **1.286** → `offset-set-bounded` **2.441** (six cells,
  2.393-2.719 — the tightest band in the set: `done$`, `done\Z`, `done\z`,
  `(?m)done$`, `\bcat\b`, `\Bcat\B`). The ONLY pattern anywhere in the
  census on the "better than ×20" side is `rec-define` — **×0.0398** on
  `auto` and ×0.0399 on `nocaps`, pcrec ×25.1 FASTER than the JIT on
  `(?(DEFINE)(?<d>\d{2}))(?&d):(?&d)`, compiled to a pure DFA.
- **`shape=inline` prints here for the first time in any committed report**,
  which supersedes the [B37] paragraph below ("`shape=` never prints
  `inline`") FOR THIS GROUP ONLY. It prints on 17 `auto` artifacts and on the
  three capturing `cat` spellings of the forced-VM arm — where it is ×1.78
  FASTER than `forward` on the same language (`(cat)` 961,162.7 vs `cat`
  1,714,697.1 ns/set) — while on the `auto` lookaround hybrids the same token
  travels with the ×2.9-5.1 SLOWER side of the `lka`/`lkb` pairs.
- **`anc-g-uc` (`\Gitem`) on the forced VM is the largest single ratio in the
  bench's history**: 1,219,696.7 ns/set against `anc-caret`'s 15.1 on the
  same testee (**×80,784**; report line 331), flat at 0.886 ns/B over all
  three runs, with the three artifacts' mechanism stamps IDENTICAL but for
  `vm_program_bytes` (801/801/814). The `auto` route is unaffected (18.7 ns).

- `2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.md` — the FIRST SAMPLE
  of `bench/syntax@0.1` ([B36], Frank's charter I-42) at pcrec **d34c9131**
  (abi 23): six cells, `libpcre2_10.46_{interp,jit}` and
  `pcrec_d34c9131_{auto,auto-nocaps,vm,vm-in}`, `--trials 5`, reporter v15.
  Query: `report --subbench syntax --version 0.1 --since
  2026-09-07T00:00:00Z --until 2026-09-07T05:00:00Z` plus the six `--testee`
  values — **6 records, 0 superseded.** READ `bench/syntax/NOTES.md`'s outlier
  rule R0-R7 and predictions P1-P13 FIRST; the census's output is a ranked
  list of QUESTIONS, not a verdict, and it lives in the ledger. 95 patterns ×
  3 regimes; the pcrec arms refuse 29 of 190 (pattern × form) compile cells
  covering 15 patterns (14 of them P1's named module refusals, plus `mod-x`
  whole-subject). Worst other-core reading of the window **30.15 %**
  (`interp` / `grp-atomic-alt` / throughput, report line 10) — above the 10 %
  pre-flight limit, which gates per CELL, not per row; no ledger question
  rests on an interp throughput cell as its primary number.
  `.subject-grain.md` (10.2 MB) carries the per-(pattern, subject, regime)
  rows the ledger's per-byte tables are read from; `.tsv` the set-grain query
  and the file the CLI-equivalence proof was run on. Ledger:
  `docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md`.

**[B48] reports (2026-09-18, lane b48read) ADDED two file groups — the
2026-09-17/18 capability window at pcrec pin cf0962e3 (abi 26)** — and
changed NOTHING else here: the reporter is unchanged at `v17
(2026-09-17)`, no committed report was regenerated, no reporter code was
touched. Both new groups carry an explicit `--since`/`--until` PAIR *and*
an explicit `--testee` roster (the 2026-08-30 rule and KB-5). The
window: two runs (`build/windows/window_capability_20260918T011018Z.log`,
21:10:18-01:19:30 EDT, 9 cells attempted; `..._20260918T052141Z.log`,
01:21:42-01:37:11 EDT, the KB-21 retry of `re2-longest`'s failed first
attempt), 9/9 cells eventually measured, store 169 → 178. The nine
records were committed on master before these were rendered; this lane
rendered from its own worktree's `store/` and commits no store file.

RE-RENDER INVARIANT not applicable (both groups are NEW, not
regenerations): each was CLI-generated directly (`python3 -m pcrecbench
report ...`, no in-process script needed — a KB-16-narrowed query over an
explicit roster loads only the matching records, seconds to tens of
seconds, not the whole-store cost KB-16 exists to warn about) and each
`.interpretation.md` sidecar was verified deterministic (a second,
independent `interpret` invocation to stdout diffs clean against the
committed file, both groups).

TWO THINGS A READER OF THIS WAVE SHOULD KNOW BEFORE THE NUMBERS:

- **Report A verifies three pcrec-side FIXES cross-pin, and finds one
  UNPREDICTED cost of the correct one.** The two I-72 erratum cells
  (`mojibake-curly-quote`'s wrong answer, `wild-logparse-syslogbase-
  expanded`'s artifact) and the F1 DFA-emitter comment-escape fix
  (`wild-waf-crs-942500-comment-obfuscation`) all confirm fixed by
  value — the reporter's own `R-DELTA-3` rule states the mojibake flip
  as "now measured (was: wrong)" on all four pcrec configs without this
  ledger inferring it. The one surprise: mojibake's forced-VM
  `large-subject-throughput` cell reads `slower ×2.00` cross-pin — the
  corrected byte pattern can no longer be dismissed as cheaply as the
  argv bug's corrupted one was, a real (and expected, once traced) cost
  of the fix being correct, not a regression.
- **Report B's compile census had to be read from the records directly.**
  `pcrecbench/report.py`'s own `did_not_compile_by_pattern` bucket is
  built ONLY from `compile_outcome == "did-not-compile"` rows,
  deliberately excluding `unsupported-by-declaration` — so NEITHER
  report renders which patterns a new engine declined by capability
  declaration. The ledger's §5.1/§5.2 census reads each record's
  `compile`-kind rows directly to confirm the b46tags REQUIRES-tag
  correction against the real corpus (not just the isolated witnesses
  the audit lane used) and to build the five-engine refusal table.

- `2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.md` — the
  pcrec **CROSS-PIN AFTER**, a770139e vs cf0962e3, plus the three pcre2
  baselines: eleven testees, four cells fresh (`pcrec_cf0962e3_
  {auto,auto-nocaps,vm,vm-in}-caps-simdna`, 01:10:54Z-02:51:49Z). Query:
  `report --subbench capability --version 0.1 --since
  2026-09-17T00:00:00Z --until 2026-09-18T03:00:00Z` plus the eleven
  `--testee` values (three pcre2 + four pcrec testee_ids at EACH pin) —
  **12 record(s) matching this query, 11 included, 1 superseded** (the
  `pcre2-dfa` `inconclusive-spread` history row from the first sample's
  own pre-flight retry). `worst_other_core_busy: 49.26%`. Read
  `docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md` §1-4 before
  the numbers: §1 the two I-72 cells, §2 the three KB-20 give-up flips,
  §3 the F1 fix, §4 the day's noise floor (93.2% of 2,904 Δ cells
  `unchanged (within spread)`). `.subject-grain.md`/`.subject-grain.tsv`
  (the catalogue-2.0 slice, [B47]) and `.tsv` the same query.
- `2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.md` — the
  **FIRST SAMPLE of the five ext-bench engines** on `bench/capability@0.1`:
  `re2-default`, `re2-longest`, `onig-default`, `tre-default`,
  `vectorscan-block-nosom`, five cells 03:33:45Z-05:22:17Z (the last a
  KB-21 retry — the first `re2-longest` attempt refused at `store.write`
  on a schema violation the same lane's own fix corrected same night, LOG
  line 1764). No pcrec pin is involved; the label carries `cf0962e3`
  as the WINDOW's own checkpoint identifier, not a claim that these
  testees are pinned to it. Query: `report --subbench capability
  --version 0.1 --since 2026-09-18T03:00:00Z --until
  2026-09-18T06:00:00Z` plus the five `--testee` values — **5 record(s)
  matching this query, 5 included, 0 superseded** (the failed first
  `re2-longest` attempt wrote nothing at all, per KB-21). `worst_
  other_core_busy: 76.52%`. Read the ledger's §5 before the numbers: the
  b46tags REQUIRES-tag cross-check (§5.2), the boolean-grain confirmation
  on `vectorscan-block-nosom` (§5.3, read from the record directly — no
  report column shows `testee.grain`), and the correctness census (§5.4:
  `evil-alt-nested`'s fourth response shape, the family-11 trio on both
  leftmost-longest engines, TRE's own wider gap). `.subject-grain.md`/
  `.subject-grain.tsv` and `.tsv` the same query.
  Ledger for both groups: `docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md`.

**[B54] reports (2026-09-19, lane b54extwindow) ADDED one file group —
the ext-bench roster's SECOND SAMPLE on `re2-default`/`tre-default`/
`vectorscan-block-nosom`**, the [B48] ledger's own next-sample checklist
item 2 (does TRE's `high-byte-run` correctness gap reproduce, or was it a
one-off box artifact) — and changed NOTHING else here: the reporter is
unchanged at `v18 (2026-09-18)`, no other committed report was
regenerated. Carries an explicit `--since`/`--until` pair *and* an
explicit `--testee` roster (the 2026-08-30 rule and KB-5), narrowed to
these three testee_ids only (no pcre2/pcrec baseline arms — the same
no-reference-arm shape the ext-first group used). Window:
`build/windows/window_capability_ext2_20260919T032134Z.log` (23:21:34 EDT
2026-09-18 → 00:16:31 EDT 2026-09-19, three cells, ALL `measured` at
attempt 1 rc=0 — re2-default 23:22:04-23:35:52, tre-default
23:36:07-23:55:32, vectorscan-block-nosom 23:55:47-00:16:16), store
178 → 181 (180 record(s) by the index's own count, header excluded).
A FIRST LAUNCH ATTEMPT the same evening (not committed, no store
change) refused all three cells instantly: the worktree had never run
`bench/capability/gen_subjects.py` / `gen_throughput_subjects.py` (the
gitignored subject trees), fixed by generating them before relaunch
(manifests reproduced byte-identical). `worst_other_core_busy: 33.33%`
(`re2_11.0.0_default-caps-simdna` / `logparse-atomic-removed` /
large-subject-throughput). All three records read `agree` (0 disagreeing
groups on 77+79+80). **`high-byte-run`'s TRE pass rate REPRODUCES
BYTE-IDENTICAL**: throughput `pass_rate 0.0000` (15/15 wrong — n=3
subjects × 5 trials, was 3/3 subjects wrong on the first sample), search
`pass_rate 0.4800` (195/375 wrong, unchanged); `tag-pair-match` and
`wild-waf-crs-942360-concat-sqli` also reproduce at `0.9867` (5/75
wrong) each, and the `did_not_compile` set for `tre-default` is the
SAME three patterns (`wild-datetime-datefinder-alternation`,
`wild-secrets-username-password-pair`,
`wild-waf-crs-942500-comment-obfuscation`). `re2-default` and
`vectorscan-block-nosom` both stay `pass_rate 1.0000` clean on
`high-byte-run`, unchanged from the first sample. Interpretation sidecar
generated against `docs/dev/predictions/capability-0.1-first.tsv`
ONLY — the newer `docs/dev/predictions/capability-0.1-ext-roster.tsv`
(lane b51preds) is deliberately NOT passed: it cannot be CLI-scored
until pcrec's F27 fix lands (`docs/dev/wake.md` standing fact, not a
file bug), so scoring it here would either silently mis-score or exit
on the known gate defect.

- `2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.md` —
  the ext-bench roster's SECOND SAMPLE, `re2-default`/`tre-default`/
  `vectorscan-block-nosom` only. Query: `report --subbench capability
  --version 0.1 --since 2026-09-18T06:00:00Z --until
  2026-09-19T05:00:00Z --testee re2_11.0.0_default-caps-simdna --testee
  tre_0.9.0_default-caps-simdna --testee
  vectorscan_5.4.11_block-nosom-nocaps-simd` — **3 record(s) matching
  this query, 3 included, 0 superseded**. `.tsv`/`.subject-grain.md`/
  `.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html` siblings all
  rendered the same query; `.interpretation.md` as described above.
  No ledger was written for this group (owed to the morning read lane
  per this lane's brief).

**[B57] reports (2026-09-19, lane b57rustwindow) ADDED one file group —
`rust-default`'s (the twelfth [B7] roster engine, `testees/rust/`) FIRST
PINNED SAMPLE on `bench/capability@0.1`** — and changed NOTHING else
here: the reporter is unchanged at `v18 (2026-09-18)`, no other
committed report was regenerated. `rust-default` is this report's ONLY
roster member (`--testee rust_1.13.1_default-caps-simdna` alone, no
pcre2/pcrec baseline arm) — DELIBERATE, not an oversight: F27's
re-anchored `check_stated_utc` (`docs/design/predicate_audit_v1.md`)
scopes its anchor to the (subbench, version, testee_id, machine_id)
tuples the report actually INCLUDES, so a second, already-measured
testee in the roster would pull an OLDER anchor in and refuse this
report's own pre-run predictions file. Window:
`build/windows/window_capability_rustfirst_20260919T173348Z.log`
(17:33:48-17:49:34 EDT, one cell, `measured` at attempt 1 rc=0), store
180 → 181. A duplicate `run_window.sh` launch (this lane's own retry
after a shell-output display glitch made a real first launch look
failed) was caught running concurrently within seconds — killed by
verified PID/cwd before it wrote anything (it was still in its
quiet-gate retry backoff, having read the FIRST launch's own CPU usage
on the target core as `NOT QUIET`) — so exactly one record exists for
this cell, not two.

The MATRIX surface is where this window's compile-outcome split is
actually legible: `render_tsv`'s own `did_not_compile` section is
STRUCTURALLY BLIND here (documented in `docs/dev/predictions/CLAUDE.md`'s
own entry for this window's predictions file) — with `rust-default` as
the sole roster member, none of its refused patterns has another testee
ranking it, so no ranking group exists for that section to attach a
bullet to. The `--format matrix` surface has no such gap (F26-immune by
construction): it reads **22 `unsup` + 1 `refused` + 2 `wrong` + 39
compiled-and-clean** across the 64-pattern corpus — the pre-compile
capability policy (`pcrecbench/capability.py`) intercepts 22 patterns
BEFORE the driver ever sees them (`unsupported-by-declaration`, never a
raw compiler refusal), and only `mojibake-curly-quote` (the one
requires-tag rust-default declares SATISFIED, per `testees/rust/
CLAUDE.md`'s I-72-adjacent finding) reaches the driver and refuses for
real. This 22+1=23 split does NOT match the r1131 census's raw
"22 refused" count one-for-one by SET — the census bypasses the
capability policy and calls the driver directly, so a pattern whose
compile-time policy withholds a token the driver would otherwise accept
syntactically (the same shape `possessive-quantifier`'s `a++` finding
already names) can show `unsup` here while reading `COMPILED` in the raw
census. **RE-DERIVED BY NAME** (lane `b58census`, 2026-09-19,
`docs/dev/measurements/2026-09-19-rust-policy-vs-census-diff.txt`): the
two 22-item sets share 21 members and differ by exactly one pattern
each way. `balanced-parens-rec` (`\((?:[^()]|(?R))*\)`) is `unsup` here
(its `recursion` token is withheld) but genuinely COMPILES in the raw
census — confirmed live through the real adapter, and shown NOT to
implement recursion at all (`(?R)` is a real rust-regex CRLF-mode inline
flag, not rejected syntax; matched against `(a(b)c)` it returns the
inner pair `[2,5)`, not the whole nested span `[0,7)` a real recursive
engine would give) — the corpus's own instance of the
`possessive-quantifier` shape, on a different token. `mojibake-curly-
quote` is the mirror case, already accounted for above: it is this
report's one `refused` row, not `unsup`, precisely because its token
(`non-utf8-subject`) is satisfied — the raw census's matching "refused"
entry for it is not a disagreement.

Predictions (`docs/dev/predictions/capability-0.1-rust-first.tsv`,
committed BEFORE the run): **3 parents / 5 clauses, 3/3 CONFIRMED, 0
refuted, 0 not-evaluable** — the first sidecar ever scored through F27's
re-anchored `check_stated_utc` on a population with no prior sample at
all (`docs/dev/predictions/capability-0.1-ext-roster.tsv`'s own
second-sample case exercised the SAME fix; this is the "population
literally never measured before" case the fix's own design note names
as still vacuous-anchor territory, and it scores clean here on the
non-vacuous branch instead — the anchor read `capability@0.1: anchor
2026-09-19T21:34:23Z, over 1 (testee_id, machine_id) tuple(s)`, this
record's own timestamp, safely after the file's `2026-09-19T21:32:08Z`
`stated_utc`). P1 (`high-byte-run`'s exact wrong-count, `n_wrong eq 10`)
confirmed exactly: the crate's default Unicode mode makes `\x80-\xff` a
Unicode-scalar-value class matched against its UTF-8 ENCODING (the
r1131 census's own discrimination witness), so of the pattern's two
should-match subjects, `nu-high-byte` (two raw bytes that never decode)
and `nu-lead-with-cont` (one valid codepoint, short of the pattern's
`{2,4}` repeat minimum) both read NOMATCH against the oracle's MATCH —
2 subjects × 5 trials. P2.a/.b/.c (the family-11 semantics-divergence
trio, `n_wrong eq 0` each) confirmed: rust-regex's `MatchKind::
LeftmostFirst` is hardcoded, not merely defaulted, so the convention
matches the oracle's own. P3 (`evil-alt-nested`, `n_wrong gt 0`)
confirmed at `n_wrong = 10`: the SAME family-10 non-backtracking-
automaton shape `docs/dev/predictions/capability-0.1-ext-roster.tsv`'s
P9.a documents `re2-default` independently wrong on — and, since this
driver structurally never emits a `giveup:` code
(`testees/rust/CLAUDE.md`), the disagreement could only ever render as
`n_wrong`, never `n_gave_up`. Sidecar determinism-checked (a second,
independent `interpret --render` invocation diffs byte-identical against
the committed file).

- `2026-09-19-capability-0.1-budu-ryzen1600-rust-first-cf0962e3.md` —
  `rust-default`'s first pinned sample on `bench/capability@0.1`. Query:
  `report --subbench capability --version 0.1 --testee
  rust_1.13.1_default-caps-simdna --format md` — **1 record(s) matching
  this query, 1 included, 0 superseded**. `worst_other_core_busy: 42.61%`
  (`rust_1.13.1_default-caps-simdna` / `keyword-prefix-order` /
  `large-subject-throughput`). `.tsv`/`.subject-grain.tsv`/`.matrix.tsv`/
  `.matrix.html` siblings all rendered the same query;
  `.interpretation.md` scored against
  `docs/dev/predictions/capability-0.1-rust-first.tsv` as described
  above. `cf0962e3` in the filename names the bench's own pcrec-pin
  checkpoint at authoring time, per this directory's own precedent for a
  non-pcrec-roster window (the ext-first/ext-second groups above) — no
  pcrec testee appears in this report's roster. No ledger was written for
  this single-cell group (the predictions file above and this entry carry
  the reading).

**[B59] reports (2026-09-20, lane b59rustwave) ADDING `rust-default`'s
REMAINING first-pinned-sample report groups** (wake queue item 3, after
`capability-0.1-rust-first.tsv`'s own [B57] first sample) — one set at a
time as each window completes; this entry is extended in place as later
sets land. Each group is `rust-default`'s SOLE roster member, for the
same F27 anchor reason `2026-09-19-capability-0.1-*-rust-first-cf0962e3.md`'s
own entry above states (a second, already-measured testee's own history
would pull an older anchor in and refuse the file's `check_stated_utc`);
no pcrec testee rides any of these cells, and the filename's pin suffix
(`25b1984f`) names the bench's own pcrec-pin checkpoint at authoring
time only, per the same non-pcrec-roster precedent. Predictions
(`docs/dev/predictions/<set>-<version>-rust-first.tsv`, all five
committed 2026-09-20 BEFORE any window, `442ebdd`) carry NO
did-not-compile clause for any of the five sets — the same solo-roster
`render_tsv` blindness the capability rust-first file's own entry
documents applies here too, spelled out in full in
`docs/dev/predictions/CLAUDE.md`'s own entry for these five files
(most visibly for `bench/syntax@0.1`, where 26 of 95 patterns are
grounded, construct-level-confirmed refusals that are nonetheless
unscorable in this shape).

- `2026-09-20-email-specimen-0.2-budu-ryzen1600-rust-first-25b1984f.md` —
  `rust-default`'s first pinned sample on `bench/email-specimen@0.2`.
  Query: `report --subbench email-specimen --version 0.2 --testee
  rust_1.13.1_default-caps-simdna --format md` — **1 record(s) matching
  this query, 1 included, 0 superseded**. `worst_other_core_busy: 10.81%`
  (`rust_1.13.1_default-caps-simdna` / `orig` / `large-subject-throughput`).
  `.tsv`/`.subject-grain.md`/`.subject-grain.tsv`/`.matrix.tsv`/
  `.matrix.html` siblings all rendered the same query; `.interpretation.md`
  scored against `docs/dev/predictions/email-specimen-0.2-rust-first.tsv`:
  **1 parent / 3 clauses, all CONFIRMED** — `orig` (the hand-inlined RFC
  5322 pattern) reads `n_wrong = 0` on all three regimes exactly as
  predicted (no refused construct, no possessive quantifier, no byte
  ≥0x80 anywhere in the file; the hardcoded leftmost-first convention
  matches the oracle's own). `factored` (the subroutine-call form,
  `(?&atom)`/`(?&qchar)`/`(?&label)`/`(?&octet)`) refuses to compile on
  BOTH forms exactly as the (unscored) recursion-family finding
  predicts — visible in the compile-cost table's `did-not-compile=1`
  rows and the matrix surface's `refused` cells (F26-immune), invisible
  to `render_tsv`'s own `did_not_compile` ranking-group section for the
  stated structural reason. No ledger was written for this single-cell
  group (the predictions file and this entry carry the reading).
- `2026-09-20-loglines-0.1-budu-ryzen1600-rust-first-25b1984f.md` —
  `rust-default`'s first pinned sample on `bench/loglines@0.1`. Query:
  `report --subbench loglines --version 0.1 --testee
  rust_1.13.1_default-caps-simdna --format md` — **1 record(s) matching
  this query, 1 included, 0 superseded** (6,930 rows: 110 compile, 6,820
  match). `worst_other_core_busy: 13.75%` (`rust_1.13.1_default-caps-simdna`
  / `iso-ts` / `large-subject-throughput`). `.tsv`/`.subject-grain.md`/
  `.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html` siblings all rendered
  the same query; `.interpretation.md` scored against
  `docs/dev/predictions/loglines-0.1-rust-first.tsv`: **2 parents / 7
  clauses, all CONFIRMED** — five short-subject-search witnesses
  (`ipv4`, `ipv6`, `uuid`, `level-context`, `kv-quoted`) and two
  large-subject-throughput ones (`level-context`, `ipv4`) all read
  `n_wrong = 0` exactly as predicted: grep of all ten real loglines
  patterns found zero refused constructs, zero possessive quantifiers
  and zero byte-range classes over 0x80 anywhere in the set, and
  rust-regex's hardcoded leftmost-first convention matches the oracle's
  own. No ledger was written for this single-cell group.
- `2026-09-20-altwide-0.2-budu-ryzen1600-rust-first-25b1984f.md` —
  `rust-default`'s first pinned sample on `bench/altwide@0.2`. Query:
  `report --subbench altwide --version 0.2 --testee
  rust_1.13.1_default-caps-simdna --format md` — **1 record(s) matching
  this query, 1 included, 0 superseded** (14,190 rows). `worst_other_core_busy:
  40.71%` (`rust_1.13.1_default-caps-simdna` / `w-8` / `short-subject-search`
  — an AFTER-sample provenance reading, not a gate verdict; the record's
  own pre-flight passed and `status: measured`). `.tsv`/`.subject-grain.md`/
  `.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html` siblings all rendered
  the same query; `.interpretation.md` scored against
  `docs/dev/predictions/altwide-0.2-rust-first.tsv`: **2 parents / 5
  clauses, all CONFIRMED** — `w-256`, `srt-256`, `ci-256` clean on
  match-compliance; `s-256` and `w-64` clean on their own regimes.
  **A genuine finding beyond the predictions file**: the matrix surface
  shows ALL 33 patterns x 3 regimes ranked at 1.000000 (self-only,
  `1.0` in every cell) — rust-regex compiles and measures the FULL
  altwide corpus with zero refusals, including `ci-512`, `s-4096` and
  `w-2048`, the exact widest rungs this project's own libpcre2/pcrec
  history refuses at (the DFA wall at `w-384`, the VM wall at
  `384 < w <= 512`, `ci-512` refusing both routes). rust-regex's default
  size limits (10 MiB compiled-program, 2 MiB lazy-DFA cache) are far
  more permissive than libpcre2's own compiled-size ceiling for this
  corpus's widest alternations — not probed for an exact boundary by
  this lane (no witnessed refusal exists to derive one from), stated
  here as an observation for a future census. No ledger was written for
  this single-cell group.
- `2026-09-20-syntax-0.1-budu-ryzen1600-rust-first-25b1984f.md` —
  `rust-default`'s first pinned sample on `bench/syntax@0.1`. Query:
  `report --subbench syntax --version 0.1 --testee
  rust_1.13.1_default-caps-simdna --format md` — **1 record(s) matching
  this query, 1 included, 0 superseded** (22,126 rows: 586 compile,
  21,540 match). `worst_other_core_busy: 33.33%`
  (`rust_1.13.1_default-caps-simdna` / `anc-dollar` /
  `large-subject-throughput`, an AFTER-sample provenance reading; the
  record's own pre-flight passed, `status: measured`). `.tsv`/
  `.subject-grain.md`/`.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html`
  siblings all rendered the same query; `.interpretation.md` scored
  against `docs/dev/predictions/syntax-0.1-rust-first.tsv` (one load-time
  bug found and fixed in the same commit — see below): **6 parents / 7
  clauses, 4 CONFIRMED (P1/P2/P3/P5), 1 REFUTED (P4), 1 PARTIAL (P6: .a
  refuted, .b confirmed)**.

  **TWO GENUINE, UNPREDICTED FINDINGS, both traced to a specific record
  and both now documented in `testees/rust/CLAUDE.md`** (not merely
  "the prediction was wrong" — each has a worked mechanism):

  1. **P4 refuted: `qnt-poss-brace` (`a{1,2}+b`) answers MATCH `[0,4)`
     on subject `f-aaab` ("aaab"), where BOTH the oracle (true PCRE
     possessive semantics) AND this lane's own "possessive suffix is a
     no-op" hypothesis (extrapolated from `testees/rust/CLAUDE.md`'s
     `a++`≡`a+` witness) predicted NOMATCH.** The only construction that
     fits the observed span is `X{n,m}+` parsing as `(X{n,m})+` —
     UNBOUNDED repetition of the BOUNDED group, not "the possessive `+`
     is dropped" — a distinction the plain `X+`/`X*`/`X?` witnesses
     (P2/P3, both CONFIRMED clean) structurally cannot make, because
     `(X+)+` / `(X*)+` / `(X?)+` are language-EQUIVALENT to their
     unsuffixed forms while `(X{1,2})+` is not. Full derivation:
     `testees/rust/CLAUDE.md`'s possessive-quantifier section,
     "CORRECTED/SHARPENED 2026-09-20" paragraph.
  2. **P6.a refuted: `unp-p-lc` (`\p{L}+`, the SATISFIED
     `unicode-properties` token) disagrees with the oracle on `f-cafe`
     (bytes `caf` + raw `0xE9`, Latin-1-encoded, NOT valid UTF-8) and
     `l-latin1`/`t-1m`/`t-256k`/`t-64k` (longer Latin-1 prose) — the
     SAME non-utf8-subject byte-vs-UTF-8-encoding mechanism the
     `capability@0.1` `high-byte-run` finding already documents for a
     raw BYTE-RANGE class, now shown to reach a Unicode PROPERTY class
     too: `\p{L}` needs a valid Unicode scalar value to test, and a
     lone invalid byte never decodes to one. `unicode-properties` stays
     SATISFIED (the mechanism is not new, only its reach); `unp-p-uc`
     (`\P{L}+`, P6.b) stayed clean on the same subjects, an asymmetry
     stated as an open observation, not derived. Full write-up:
     `testees/rust/CLAUDE.md`'s `non-utf8-subject` section.

  **A predictions-format BUG was found and fixed in the same commit**
  (`docs/dev/predictions/CLAUDE.md`'s own `op`/`lo`/`hi` column
  documentation): `interpret.py`'s `_op_holds` reads its threshold from
  `hi` for EVERY comparison op except `between` (never from `lo`, which
  `between` alone uses) — this file's original P1 clause (`op=gt`) put
  the threshold in `lo` by mistake, which crashes `_op_holds` with
  `ValueError: could not convert string to float: ''` rather than
  scoring anything. Fixed before the first successful score (swapped to
  `lo=""`/`hi="0"`, matching every other op=`eq`/`gt` clause across all
  five of this lane's files, which were correct from authoring). No
  ledger was written for this single-cell group (this entry and
  `testees/rust/CLAUDE.md`'s two updated sections carry the reading).
- `2026-09-20-bounded-0.3-budu-ryzen1600-rust-first-25b1984f.md` — the
  LAST of `rust-default`'s five remaining first pinned samples ([B59]
  complete): `bench/bounded@0.3`. Query: `report --subbench bounded
  --version 0.3 --testee rust_1.13.1_default-caps-simdna --format md` —
  **1 record(s) matching this query, 1 included, 0 superseded** (20,914
  rows: 414 compile, 20,500 match). `worst_other_core_busy: 14.81%`
  (`rust_1.13.1_default-caps-simdna` / `ctx-greedy-256` /
  `large-subject-throughput`). `.tsv`/`.subject-grain.md`/
  `.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html` siblings all
  rendered the same query; `.interpretation.md` scored against
  `docs/dev/predictions/bounded-0.3-rust-first.tsv`: **2 parents / 6
  clauses, 5 CONFIRMED, 1 NOT-EVALUABLE** (P1.c, `nest3-16` — see
  below; P1 rolls up `partial` on the arithmetic, but this is a witness
  choice landing on a real refusal, not a wrong prediction).

  **A genuine, unpredicted finding: TWO of the 42 real bounded patterns
  refuse to compile under `rust-default`** — `nest3-16`
  (`(?:(?:\d{1,16}){1,16}){1,16}`, P1.c's own selector) and `nest2-64`
  (`(?:\d{1,64}){1,64}`), both `[size-limit] CompiledTooBig: Compiled
  regex exceeds size limit of 10485760 bytes` on BOTH forms (plain and
  whole-subject) — visible in the compile-cost table and the matrix
  surface (F26-immune), invisible to `render_tsv`'s own `did_not_compile`
  section for the same solo-roster structural reason stated throughout
  this window. Neither refusal was in this lane's grounding (the grep
  that found "zero refused constructs" checked SYNTAX only — backrefs,
  lookaround, atomic groups etc. — never compiled SIZE, which is a
  property of the pattern's combinatorial expansion, not any single
  construct). The mechanism reads coherently against the rest of the
  set: the FLAT count-ladder (`cls-upto-*`, single-level bounded repeat)
  compiles clean all the way to `cls-upto-65535` — the exact rung
  libpcre2/pcrec's own NFA-cap history refuses at, per this project's
  earlier bounded samples, a boundary rust-regex's more permissive
  10 MiB default does not share — while the two NESTED bounded-repeat
  patterns (multiplicative combinatorics: `nest3-16`'s worst case is
  16^3 = 4,096 repeats of a compiled subexpression) hit the SAME 10 MiB
  ceiling from the opposite direction, at far smaller nominal counts.
  The three smaller nested-repeat patterns (`nest2-4`, `nest2-letters-6`,
  `nest3-3`) compile clean, consistent with the combinatorial-not-
  syntactic explanation. No ledger was written for this single-cell
  group. **[B59] itself is now COMPLETE**: five sets (email/loglines/
  altwide/syntax/bounded) sampled in one lane, three genuine unpredicted
  findings across two of them, one predictions-format bug found and
  fixed, `docs/dev/lanes/b59rustwave_report.md` has the full lane
  account.

**[B60] report (2026-09-20, lane b60pinconfirm) ADDED one file group —
the [B58] pin's (cf0962e3 -> 25b1984f, [EMIT-VERB]/D112) acceptance
AFTER on the MEASURED (time) axis, `bench/capability@0.1`'s only
genuine cf0962e3 sample.** Reporter unchanged at `v18 (2026-09-18)`; no
other committed report regenerated.

- `2026-09-20-capability-0.1-budu-ryzen1600-pinconfirm-25b1984f.md` —
  the pcrec CROSS-PIN acceptance AFTER, cf0962e3 vs 25b1984f, plus the
  three pcre2 baselines: eleven testees, four cells fresh
  (`pcrec_25b1984f_{auto,auto-nocaps,vm,vm-in}-caps-simdna`,
  22:34:10Z-2026-09-21T00:18:07Z), same KB-5 `--testee` roster shape as
  the [B48] AFTER precedent (`2026-09-18-*-after-cf0962e3.md`). Query:
  `report --subbench capability --version 0.1 --since
  2026-09-17T00:00:00Z --until 2026-09-21T01:10:00Z` plus the eleven
  `--testee` values (three pcre2 + four pcrec_cf0962e3_* + four
  pcrec_25b1984f_*) — **12 record(s) matching this query, 11 included,
  1 superseded** (the same pcre2-dfa `inconclusive-spread` history row
  the precedent superseded; the since/until bracket also spans the
  a770139e records from 2026-09-17, excluded by the explicit roster, not
  by date). `worst_other_core_busy: 58.96%`
  (`pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942140-dbnames` /
  `large-subject-throughput`). `.subject-grain.md`/`.subject-grain.tsv`
  (the catalogue-2.0 slice) and `.matrix.tsv`/`.matrix.html` (128 rows,
  11 testees) the same query.

  **Predictions (`docs/dev/predictions/capability-0.1-pin-25b1984f-
  confirm.tsv`, P1-P4, one per pcrec testee, each `delta_verdict
  eq-token unchanged (within spread)` over every ranked cell): all four
  REFUTED**, scored 2026-09-20 via a direct `interpret.evaluate_
  predictions` call (the documented F27 CLI gap — this population
  necessarily includes the already-measured cf0962e3 records) —
  738/750/732/732 ranked values per parent, every refutation a single
  `eq-token` mismatch on a non-"unchanged" delta_verdict token, exactly
  as the file's own grounding anticipated (a strict eq-token clause
  registers ordinary trial-level boundary jitter as refuted by
  construction; refutation alone is not a systematic-mover finding).
  **Scoring this file also found a NEW interpreter bug**
  (`docs/dev/known_issues.md` KB-24): `evaluate_predictions` crashes
  outright on any `quantity=delta_verdict` clause (the first ever
  authored) — `_measured_text` assumes every `identity`-reduced
  "num"-kind value is numeric, and `delta_verdict`'s values are string
  tokens; scored via a scratch monkeypatch of the broken formatting
  helper only, `_op_holds` (the real predicate) untouched.

  **R-DELTA-1 fired 32 times** (aggregated to 14 by regime × config ×
  direction in the sidecar), every ratio in [1.00, 1.08] — consistent
  with the historical ≤×1.04 ordinary-jitter ceiling except ONE
  genuine, tight, isolated mover: `wild-datetime-moment-iso8601` /
  `short-subject-search` / `pcrec_25b1984f_vm-in-caps-simdna` reads
  **slower ×1.08** (median 6,298.94ns cf0962e3 -> 6,808.08ns 25b1984f;
  stddev 2.78ns/1.77ns respectively — the delta is ~91× the rule's own
  2×stddev spread threshold) while the SAME pattern on
  auto-caps/auto-nocaps/vm-caps all read `unchanged (within spread)` —
  isolated to the caller-provided frame-buffer route
  (`pcrec-vm-in`). **FLAGGED for the manager's outbox, not absorbed**:
  this is the one cell in the whole cross-pin comparison too tight and
  too reproducible to be ordinary spread, and [EMIT-VERB]/D112's claim
  was that NOTHING measuring time moves. `docs/dev/lanes/
  b60pinconfirm_report.md` has the full derivation.

**[B61] reports (2026-09-20, lane b61matrix) ADDED six FULL-ROSTER file
groups — one per set ([B59]'s new `rust-default` samples folded into the
project's own standing cross-engine comparison for the first time)**:
`email-specimen@0.2`, `loglines@0.1`, `bounded@0.3`, `altwide@0.2`,
`syntax@0.1`, and — added in a charter extension once the [B60] merge
(8dde570) landed four fresh `pcrec_25b1984f_*` `capability@0.1` records —
`capability@0.1` itself. Frank's direct ask: build reports whose matrix
includes EVERY roster engine with records for each set, `rust-default`
among them, where every prior committed matrix for these six sets either
predates `rust-default` entirely or is scoped to `rust-default` ALONE (the
[B57]/[B59] solo-roster shape, chosen for the F27 anchor reason those
entries state). The reporter is unchanged at `v18 (2026-09-18)`; no
existing committed report was regenerated. This lane merged `master` into
`lane/b61matrix` after its first five sets landed (one conflict, in this
file — both sides had inserted a new wave paragraph at the same point;
resolved by keeping both, `[B60]`'s pinconfirm entry first, this entry
second, neither dropped) to pick up the [B60] records before rendering
the sixth group.

**ROSTER-SELECTION RULE STATED UP FRONT, because it is the one thing a
reader must not assume**: "full roster" here means the newest record of
each CANONICAL engine identity — `libpcre2-interp`, `libpcre2-jit`,
`pcrec-auto`, `pcrec-auto-nocaps`, `pcrec-vm`, `pcrec-vm-in`, and now
`rust-default` — never every distinct `testee_id` `store/index.tsv` has
ever recorded. The bench's own ablation testees (`-noedge`, `-noisland`,
`-noclsfold`, `-cc-clang`, `-bigcap`, `-align64`) are investigation arms,
not roster members, and are excluded here exactly as they are from every
prior `-after-<pin>` cross-pin group this directory already carries (see
e.g. the `2026-09-06-bounded-0.3-*-after-d34c9131` entry below, whose own
roster mixes `pcrec_288d505_vm-in-caps-simdna` with two `334fd10e` arms
and two `d34c9131` arms for the identical reason: the newest MEASURED pin
per canonical mode, not the newest pin overall). This lane's own roster
was derived by exactly that rule, mechanically, from `store/index.tsv`,
picking the newest record of each of the six canonical `testee_id`
suffixes (`auto-caps-simdna`, `auto-nocaps-simdna`, `vm-caps-simdna`,
`vm-in-caps-simdna`, the two `libpcre2` ids) ACROSS ALL PCREC PINS, plus
`rust_1.13.1_default-caps-simdna`'s own newest record.

**THE FINDING EVERY GROUP SHARES, STATED BEFORE ANY NUMBER**: pcrec's
canonical roster has NOT been re-measured on any of these five sets since
pin **d34c9131** (abi 23, 2026-09-06/07) — FOUR re-pins ago
(`cd371441` → `a770139e` → `cf0962e3` → **25b1984f**, today's abi-27
checkpoint per `testees/pcrec/CLAUDE.md`). Every filename below is
suffixed `d34c9131` because that is what the data actually is, not
because this lane chose it as an authoring-time label (contrast the
[B57]/[B59] solo-roster files, whose pin suffix names the bench's own
checkpoint precisely because NO pcrec testee rides those rows at all).
Three of the five groups mix PINS WITHIN THEIR OWN ROSTER, because not
every canonical mode was re-measured at every pin: `email-specimen@0.2`
and `loglines@0.1` carry `pcrec_d34c9131_auto-caps-simdna` alongside
`pcrec_1989c62_{auto-nocaps,vm,vm-in}-caps-simdna` (nocaps/vm/vm-in
untouched since 1989c62, five pcrec pins ago on this axis); `altwide@0.2`
carries `pcrec_d34c9131_{auto,vm}-caps-simdna` alongside
`pcrec_334fd10e_{auto-nocaps,vm-in}-caps-simdna` (one pin back);
`bounded@0.3` carries `pcrec_d34c9131_{auto,vm,vm-in}-caps-simdna`
alongside ONE holdout, `pcrec_288d505_auto-nocaps-simdna` (two pins
back — `auto-nocaps` was never re-measured on `bounded@0.3` at either
334fd10e or d34c9131). Only `syntax@0.1` is pin-uniform: all six pcrec
arms are the set's own single `d34c9131` census window, so this is the
one group where "the roster" and "the pin" say the same thing. Every
group's own `.tsv` header line names its full `--testee` roster and its
`--matrix.tsv` header restates it; no `--since`/`--until` bound was
needed (KB-5's roster convention already narrows to these seven ids by
name, and none of them has a second, unwanted record — the header's own
`superseded:` count on the mixed-pin groups (7, 6, 2) is exactly the
count of now-superseded OLDER records those seven ids' histories carry,
confirmed against the per-testee newest-record table this lane derived
from `store/index.tsv` before rendering, not a sign of drift).

Rendered foreground, one render at a time (KB-16 is closed — an
explicit-roster query loads only the matching records via the index
prefilter, so every set-grain/matrix render finished in 15-46 s; the two
subject-grain renders on the two largest sets, `loglines@0.1`'s
`.subject-grain.md` and `syntax@0.1`'s `.subject-grain.md`, took the
longest at 3 m 21 s and 2 m 13 s respectively — nowhere near KB-16's
old whole-store cost, because no query here loads more than seven
records). Every `.interpretation.md` sidecar is a FRESH file (these are
roster snapshots, not first samples — no `docs/dev/predictions/*.tsv`
file applies), rendered via `pcrecbench interpret ... --render --out`
against the group's own `.tsv` + `.subject-grain.tsv`, and each was
determinism-checked (a second, independent `interpret --render`
invocation to stdout diffs BYTE-IDENTICAL against every one of the five
committed sidecars). `make check-interpret` 166/166 (section 3, sidecar
freshness, covers all five).

**THREE THINGS A READER OF THIS WAVE SHOULD KNOW BEFORE THE NUMBERS**:

- **`rust-default` wins several matrix rows outright, on more than one
  set.** On `loglines@0.1` it is `best_testee` (fastest of the seven) on
  BOTH regimes of `hex32-id`, `ipv6`, `kv-quoted`, `level-context`, and
  the `short-subject-search` regime of `stack-frame` — five of ten
  patterns, beating `pcre2-jit` and every pcrec arm in the roster, not
  merely holding its own. On `altwide@0.2`'s `ci-256` /
  `match-compliance` / `whole-subject` row it is fastest at 1,066.2 ns
  against `pcrec_d34c9131_vm-caps-simdna`'s ×103.3 and
  `pcrec_334fd10e_auto-nocaps-simdna`'s outright REFUSAL on that exact
  (pattern, form) cell (both pcrec AUTO arms in the roster refuse the
  whole-subject wrapped form of `ci-256`; only the VM route compiles it,
  and rust-regex is ~94-103× faster than that VM artifact). On
  `wb-512` (512 branches each individually `\b`-wrapped) ALL FOUR pcrec
  roster arms refuse on EVERY regime and form — both pins, both routes —
  while `pcre2-interp`/`pcre2-jit` compile but run 318×/40× slower than
  `rust-default`, which is `best_testee` on all four of that pattern's
  rows. `wb-256` (below the known `w`-family DFA/VM wall at
  `w-384`/`384<w≤512`) ALSO refuses on all four pcrec arms — a smaller
  branch count than the plain `w`-ladder's own refusal boundary, because
  the per-branch `\b` wrapping is a different, apparently more expensive
  structure than a bare alternation of the same width. None of this is
  re-derived from source here (no pcrec diagnostic was traced); it is
  read directly off the matrix's `refused` tokens and is stated as an
  observation for a future census, per this lane's charter to report
  rather than diagnose.
- **`syntax@0.1`'s matrix surfaces SIX `rust-default` wrong-answer
  patterns beyond the two the [B59] rust-first report already
  documented by name.** That report's own predictions file (P4, P6.a)
  found and explained `qnt-poss-brace` and `unp-p-lc` wrong; this
  group's full roster, ranking `rust-default` against pcre2/pcrec on
  every pattern rather than the seven witnesses that file selected,
  reads `n_wrong > 0` (`wrong` token) on six more: `anc-dollar`,
  `cls-v`, `esc-hex-braced`, `qnt-poss-plus`, `qnt-poss-quest`, and
  `rec-r-uc` — eight patterns total, 19 matrix rows. None of these six
  is diagnosed here (no mechanism is claimed); they are named because
  the matrix is where they first became visible in a committed report,
  not because this lane traced any of them to a cause. `syntax@0.1` also
  shows `rust-default` REFUSED (compile-time, not wrong-answer) on 42
  patterns (169 rows) — consistent in COUNT with `testees/rust/CLAUDE.md`'s
  own capability-declaration census, not re-verified pattern-by-pattern
  here.
- **`bounded@0.3`'s and `altwide@0.2`'s pcrec-side refusals in this
  roster are the project's OWN known ones, not new**: `cls-upto-65535`
  refuses on both pcrec AUTO arms (the NFA-state cap, O-9's history);
  `nest2-64`/`nest3-16` refuse on `rust-default` alone, matching [B59]'s
  own bounded finding (`CompiledTooBig`, 10 MiB default) exactly. Read
  those cells as confirmation the matrix surface agrees with the
  narrower reports, not as this wave's own discovery.

- `2026-09-20-email-specimen-0.2-budu-ryzen1600-fullroster-d34c9131.md` —
  full roster: `libpcre2_10.46_{interp,jit}-caps-simdna`,
  `pcrec_d34c9131_auto-caps-simdna`,
  `pcrec_1989c62_{auto-nocaps,vm,vm-in}-caps-simdna`,
  `rust_1.13.1_default-caps-simdna`. Query: `report --subbench
  email-specimen --version 0.2` plus the seven `--testee` values —
  **7 record(s) matching this query, 7 included, 0 superseded** (the
  header's `superseded: 7` counts each id's own retired history, not a
  drift in this query's own result set). `worst_other_core_busy: 10.81%`
  (`rust_1.13.1_default-caps-simdna` / `orig` / `large-subject-throughput`).
  `factored` (the subroutine-call form) refuses on `rust-default` on all
  four regime/form rows, matching [B59]'s own email-specimen finding.
  `.tsv`/`.subject-grain.md`/`.subject-grain.tsv`/`.matrix.tsv`/
  `.matrix.html`/`.interpretation.md` all rendered/generated as described
  above.
- `2026-09-20-loglines-0.1-budu-ryzen1600-fullroster-d34c9131.md` — full
  roster: the same seven-id shape (pcrec nocaps/vm/vm-in at 1989c62,
  auto at d34c9131). Query: `report --subbench loglines --version 0.1`
  plus the seven `--testee` values — **7 record(s) matching this query,
  7 included, 0 superseded**. `worst_other_core_busy: 13.83%`
  (`libpcre2_10.46_jit-caps-simdna` / `stack-frame` /
  `short-subject-search`). See the `rust-default`-wins-five-of-ten
  finding above. `.tsv`/`.subject-grain.md`/`.subject-grain.tsv`/
  `.matrix.tsv`/`.matrix.html`/`.interpretation.md` all rendered/generated
  as described above.
- `2026-09-20-bounded-0.3-budu-ryzen1600-fullroster-d34c9131.md` — full
  roster: `pcrec_d34c9131_{auto,vm,vm-in}-caps-simdna` plus the one
  holdout `pcrec_288d505_auto-nocaps-simdna` (never re-measured on this
  set since 288d505), the two pcre2 baselines, `rust-default`. Query:
  `report --subbench bounded --version 0.3` plus the seven `--testee`
  values — **7 record(s) matching this query, 7 included, 0
  superseded**. `worst_other_core_busy: 100.0%`
  (`pcrec_288d505_auto-nocaps-simdna` / `dig-upto-32` /
  `large-subject-throughput` — an AFTER-sample provenance reading on a
  record measured 2026-09-05, not a gate verdict on this render; the
  record's own pre-flight passed, `status: measured`). `.tsv`/
  `.subject-grain.md`/`.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html`/
  `.interpretation.md` all rendered/generated as described above.
- `2026-09-20-altwide-0.2-budu-ryzen1600-fullroster-d34c9131.md` — full
  roster: `pcrec_d34c9131_{auto,vm}-caps-simdna` plus
  `pcrec_334fd10e_{auto-nocaps,vm-in}-caps-simdna` (one pin back), the
  two pcre2 baselines, `rust-default`. Query: `report --subbench altwide
  --version 0.2` plus the seven `--testee` values — **7 record(s)
  matching this query, 7 included, 0 superseded**. `worst_other_core_busy:
  40.71%` (`rust_1.13.1_default-caps-simdna` / `w-8` /
  `short-subject-search` — an AFTER-sample provenance reading, not a
  gate verdict; the record's own pre-flight passed, `status: measured`).
  See the `ci-256`/`wb-256`/`wb-512` findings above. `.tsv`/
  `.subject-grain.md`/`.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html`/
  `.interpretation.md` all rendered/generated as described above.
- `2026-09-20-syntax-0.1-budu-ryzen1600-fullroster-d34c9131.md` — full
  roster: all six pcrec arms at the set's own single census pin,
  `pcrec_d34c9131_{auto,auto-nocaps,vm,vm-in}-caps-simdna`, the two
  pcre2 baselines, `rust-default` — the one PIN-UNIFORM group in this
  wave. Query: `report --subbench syntax --version 0.1` plus the seven
  `--testee` values — **7 record(s) matching this query, 7 included, 0
  superseded**. `worst_other_core_busy: 33.33%`
  (`rust_1.13.1_default-caps-simdna` / `anc-dollar` /
  `large-subject-throughput` — an AFTER-sample provenance reading, not a
  gate verdict; the record's own pre-flight passed, `status: measured`).
  See the six-unpredicted-wrong-answers finding above. `.tsv`/
  `.subject-grain.md`/`.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html`/
  `.interpretation.md` all rendered/generated as described above.

**`capability@0.1`, THE SIXTH GROUP, IS A DIFFERENT SHAPE FROM THE OTHER
FIVE — read this before its bullet.** This is the widest [B7] roster
this project has ever put in one matrix: THIRTEEN testees, not seven,
because `capability@0.1` itself carries more than one canonical
identity per engine family — `libpcre2-dfa` alongside `-interp`/`-jit`,
`re2-default` alongside `re2-longest` — and every one of them now has a
record. This group is DISTINCT IN PURPOSE from
`2026-09-20-capability-0.1-budu-ryzen1600-pinconfirm-25b1984f.md` two
entries above ([B60], lane b60pinconfirm): that report is a CROSS-PIN
acceptance AFTER, eleven testees, three pcre2 baselines plus BOTH
`cf0962e3` and `25b1984f` pcrec arms side by side, built to answer
"did anything measuring time move across the [EMIT-VERB]/D112 re-pin."
This report is a FULL-ROSTER SNAPSHOT, thirteen testees, ONE pcrec pin
(25b1984f, now uniform across all four canonical modes — the four
[B60] records are also what makes every pcrec mode's newest sample
line up on a single pin for the first time in this set's history),
built to answer "how does every engine this project measures compare
right now." A reader who wants the pin-confirm finding (the isolated
`pcrec-vm-in` ×1.08 mover) should read that entry, not this one; a
reader who wants the cross-engine picture should read this one, not
that one.

- `2026-09-20-capability-0.1-budu-ryzen1600-fullroster-25b1984f.md` —
  full roster: `libpcre2_10.46_{interp,jit,dfa-nocaps}-*`,
  `pcrec_25b1984f_{auto,auto-nocaps,vm,vm-in}-caps-simdna` (pin-uniform
  — the [B60] merge's own four records), `oniguruma_6.9.10_default-caps-
  simdna`, `re2_11.0.0_{default,longest}-caps-simdna`,
  `rust_1.13.1_default-caps-simdna`, `tre_0.9.0_default-caps-simdna`,
  `vectorscan_5.4.11_block-nosom-nocaps-simd`. Query: `report --subbench
  capability --version 0.1` plus the thirteen `--testee` values —
  **13 record(s) matching this query, 13 included, 4 superseded** (each
  id's own retired history: the two older `libpcre2-dfa`/`re2-default`/
  `tre-default`/`vectorscan` samples this lane's newest-record rule
  already excludes by construction). `worst_other_core_busy: 58.96%`
  (`pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942140-dbnames` /
  `large-subject-throughput`).

  **The matrix's starkest row: `evil-alt-nested` / `short-subject-search`
  / `plain` has NO winner at all** — `best_testee`/`best_ns` are both
  empty because every one of the thirteen roster testees reads either
  `wrong` or `gave-up` on that exact cell (seven `wrong`: `libpcre2-dfa`,
  `pcrec_25b1984f_auto-nocaps-simdna`, `re2-default`, `re2-longest`,
  `rust-default`, `tre-default`, `vectorscan`; six `gave-up`:
  `libpcre2-interp`/`-jit`, `oniguruma`, `pcrec_25b1984f_{auto-caps,
  vm-caps,vm-in}-caps-simdna`). The same pattern's
  `large-subject-throughput` row DOES rank cleanly
  (`pcrec_25b1984f_auto-nocaps-simdna` wins at 27.3 ns), so the failure
  is specific to the search regime, not the pattern's compile step. Not
  diagnosed here — several of the individual engine failures behind
  this row are already named in the [B48]/[B54] ledgers (RE2's own
  family-11 trio, TRE's wider correctness gap); what is new here is
  seeing all thirteen fail SIMULTANEOUSLY on one row, which no
  narrower, single- or few-testee report could show.
  `libpcre2-dfa` carries the roster's own second-worst correctness
  count (5 `wrong` + 3 `gave-up` across 128 rows, `--dfa`'s documented
  leftmost-ALTERNATIVE-not-leftmost-first semantics per `testees/pcre2/
  CLAUDE.md`); `tre-default` the worst (9 `wrong` + 6 `refused`).
  `pcrec_25b1984f_auto-nocaps-simdna` carries exactly one `wrong` cell
  in the whole matrix (`evil-alt-nested`/search, named above) — not
  independently traced to a cause in this lane. `.tsv`/
  `.subject-grain.md`/`.subject-grain.tsv`/`.matrix.tsv`/`.matrix.html`/
  `.interpretation.md` all rendered/generated as described above.

Lane report: `docs/dev/lanes/b61matrix_report.md`.


**[B39] reports (2026-09-06, lane b39read) ADDED five file groups — the
2026-09-06 DAYTIME window at pcrec pin d34c9131 (abi 23), the [B39]
CLS-FOLD AFTER** — and changed NOTHING else here: the reporter is
`v15 (2026-09-05)` (lane b39prep's `clsfolds=` clause and the corrected
`prog:` note, merged before the window ran), no committed report was
regenerated, no reporter code was touched. Every one of the fifteen new
files carries an explicit `--since`/`--until` PAIR *and* an explicit
`--testee` roster (the 2026-08-30 rule and KB-5's roster). The window: 10
cells, ALL `measured`, NINE at attempt 1 and ONE at attempt 2 — the altwide
`pcrec-vm-noclsfold` cell's first pre-flight REFUSED (rc=3, nothing written:
busiest non-target core 20.12 %, target core cpu11 19.64 %, both over the
10 % limit) and its retry 15 minutes later passed; suite log
`build/windows/suite_b39_after_20260906T155452Z.log`, 11:54:52 → 15:12:47
EDT (3 h 18 min: altwide 38, bounded 132, loglines 17, email 10 min), store
144 → 154. The ten records were committed on master (99a0b60) before these
were rendered; this lane rendered from its own worktree's `store/` and
commits no store file.

RE-RENDER INVARIANT, checked the same two ways as the [B34] and [B37] waves,
because the fifteen files were rendered IN-PROCESS (the 154-record store
loaded and validated ONCE — **640 s on this box**, with another quiet-window
benchmark running beside it — and reused for all fifteen; the same
`build_report` / `render_markdown` / `render_tsv` calls a CLI invocation
makes; the five groups then rendered in 91 s):

1. **CLI equivalence**, proven on
   `2026-09-06-loglines-0.1-budu-ryzen1600-clsfold-d34c9131.md`: that file
   was FIRST produced by a full `python3 -m pcrecbench report …` invocation
   of its own committed query (10 min 51 s, all but ~20 s of it store
   validation) and the in-process render `cmp`s BYTE-IDENTICAL against it.
2. **Determinism over all fifteen**: a second, independent in-process render
   into a scratch directory diffs clean on all fifteen files (`cmp` on each).

FIVE THINGS A READER OF THIS WAVE SHOULD KNOW BEFORE THE NUMBERS:

- **The fold's whole surface in this wave is TWO artifacts.** `clsfolds=26`
  prints on exactly two legend lines — `ci-256` / `plain` and `ci-256` /
  `whole-subject` on `pcrec_d34c9131_vm-caps-simdna` (altwide clsfold file,
  lines 1013–1014) — and `clsfolds=0` on every one of the other 277 VM
  artifacts in the wave; a DFA artifact carries no clause at all. That is
  the corpus, not a harness gap: `bench/altwide`'s `ci-256` / `ci-512` are
  the only `(?i)` or two-letter-class patterns in any set.
- **The two `-clsfold-` pairs on loglines and email are NULL PAIRS BY
  CONSTRUCTION, and that is their job.** `pcrec-auto` compiles 20 DFA + 2 VM
  artifacts on loglines and 6 DFA + 0 VM on email; the deny arm's artifacts
  are identical to the fold arm's on all thirteen size and stamp fields
  (`emit_bytes`, `emit_code_bytes`, `artifact_bytes`, `vm_program_bytes`,
  engine, `sel=`, `clsfolds=`, `islands=`, `shape=`, `folds=`, `edge=`,
  `start=`, `match=`) on 22 of 22 and 6 of 6 (pattern × form) cells. Read
  them as THE DAY'S NOISE FLOOR: 22 loglines cells 0.9951–1.0134 (worst
  1.34 %, `kv-quoted` / search), 9 email cells 0.9970–1.0058 (worst 0.58 %).
- **On the one witness the fold is SMALLER and SLOWER**, so read the altwide
  clsfold file's size table and its ranking together: `ci-256` on the VM
  route is 359,502 vs 451,076 code bytes (×0.797), 351,053 vs 442,627
  program bytes, 96,832 vs 142,968 `.so` bytes (−32.3 %, pcrec's own
  __TEXT −31 % reproduced) and compiles in 2.45 s vs 6.16 s — and it runs
  ×1.0446 throughput / ×1.0273 search / ×1.0950 match SLOWER than the
  denied arm, far outside the day's 1.34 % floor.
- **The bounded AFTER file carries a SELECTION CHANGE, not only timings.**
  `cls-upto-8192` / `whole-subject` under `pcrec-auto` moved `dfa`
  (`sel=selected`, `start=reverse-pass`, `match=search-filter`, 937,591
  emitted bytes) → `vm` (`sel=declined-nullable`, `shape=forward`, 18,487
  bytes) across the pin, because [LIM-2] N1's 30,000,000-element auto budget
  now overflows where K7's 48,000,000 did not. Its match-compliance row
  reads `faster ×6.6` (12,422.7 → 1,871.2 ns) — that is a ROUTE, not a
  speed-up of the same machine, and [B16] R2's rule applies: say
  "selection changed (dfa → vm)" when citing it.
- **The bounded `vm-in` row's Δ partner is 288d505, not 334fd10e** — that
  arm was not measured on `bounded@0.3` at 334fd10e, so its cross-pin cell
  spans THREE abi steps (16 → 22 → 23) while the `auto` and `vm` rows span
  one. The READER'S CAVEAT on the a7e0bdf bounded entry below applies to
  every `vs best` cell in the two cross-pin files here: with two or three
  pins in one table, `vs best` inverts visually wherever an older pin's row
  ranks first — read same-pin rows or the Δ column.

- `2026-09-06-altwide-0.2-budu-ryzen1600-clsfold-d34c9131.md` — **THE FOLD
  PAIR**: `pcrec-vm` against `pcrec-vm-noclsfold` (the same config with
  `-fno-cls-fold`, deny bit 24) plus `pcrec-auto` as the DFA-route control,
  all three at d34c9131, three cells `measured` 11:55–12:33 EDT. Query:
  `report --subbench altwide --version 0.2 --since 2026-09-06T15:50:00Z
  --until 2026-09-06T16:30:00Z --testee pcrec_d34c9131_vm-caps-simdna
  --testee pcrec_d34c9131_vm-caps-simdna_noclsfold --testee
  pcrec_d34c9131_auto-caps-simdna` — **3 records, 0 superseded.** A
  ONE-VARIABLE pair (the deny word lives in `config_extra`; `build_flags`
  reads `pcrec flags --features all --engine=vm -fno-cls-fold` with the
  [B32] denied-axis sentence) whose ONLY moving cells are `ci-256`'s three:
  everything else is byte-identical on both arms (42 of 44 compiled VM
  artifacts equal to the byte, 22 refusals each including `ci-512` on both)
  and 62 of the 63 fold-free set cells read 0.9534–1.0561. THE ONE EXCEPTION
  worth a reader's
  eye is `w-8` / `match-compliance`, 370.8 (fold) vs 559.5 (denied) ns —
  ×0.66 on a pair of artifacts identical in every stamp and byte count,
  stable over all five trials on both arms (sd 20.6 / 1.3), and NOT a
  cls-fold effect; the ledger records it as unexplained. `.subject-grain.md`
  and `.tsv` the same query.
- `2026-09-06-altwide-0.2-budu-ryzen1600-after-d34c9131.md` — the
  **altwide@0.2 AFTER at d34c9131, CROSS-PIN against the 2026-09-05 sample
  at 334fd10e**: the three d34c9131 arms, the five 334fd10e arms (`auto`,
  `auto_noisland`, `auto-nocaps`, `vm`, `vm-in`) and the two libpcre2
  baselines of 2026-09-03. Query: `report --subbench altwide --version 0.2
  --since 2026-09-03T03:50:00Z --until 2026-09-06T16:30:00Z` plus TEN
  `--testee` values (`libpcre2_10.46_{interp,jit}-caps-simdna`,
  `pcrec_334fd10e_{auto,auto-nocaps,vm,vm-in}-caps-simdna` +
  `pcrec_334fd10e_auto-caps-simdna_noisland`, and
  `pcrec_d34c9131_{auto,vm}-caps-simdna` +
  `pcrec_d34c9131_vm-caps-simdna_noclsfold`) — **10 records, 0 superseded**
  (the `--since` cuts the 2026-09-03 1989c62 arms and the two bigcap
  records, which the roster would exclude anyway). The R8 Δ column reads
  d34c9131 against 334fd10e per config: **66 VM cells, median ×0.9993, all
  but two inside [0.9, 1.1]** — `sh1-64` search ×0.8798 and `ci-256` match
  ×1.1018 — and 53 auto cells median ×1.0009. The order pair is unmoved
  (`w-256` / `srt-256` on `vm` 15,902,716 / 15,949,646 ns throughput, both
  292,069 B of code = 292,043 + the 26-byte stamp line), `w-384` and
  `pfx3-512` still compile on the VM route (427,850 / 440,213 B) and
  `w-512` still refuses. `.subject-grain.md` and `.tsv` the same query.
- `2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.md` — the
  **bounded@0.3 AFTER at d34c9131**: `pcrec-auto`, `pcrec-vm` and
  `pcrec-vm-in` (the `_in` control owed from [B35] (6)/(9)) measured
  12:33–14:45 EDT, cross-pin against `pcrec_334fd10e_{auto,vm}` of
  2026-09-05 and — for the `_in` arm, which 334fd10e never measured on this
  set — `pcrec_288d505_vm-in` of 2026-09-04/05, plus the two libpcre2
  baselines of the same night. Query: `report --subbench bounded --version
  0.3 --since 2026-09-04T23:00:00Z --until 2026-09-06T18:10:00Z` plus EIGHT
  `--testee` values (`libpcre2_10.46_{interp,jit}-caps-simdna`,
  `pcrec_288d505_vm-in-caps-simdna`,
  `pcrec_334fd10e_{auto,vm}-caps-simdna`,
  `pcrec_d34c9131_{auto,vm,vm-in}-caps-simdna`) — **8 records, 0
  superseded** (the `--since 2026-09-04T23:00:00Z` admits the 288d505
  `vm-in` record and the roster keeps the other five 288d505 arms and the
  `cc-clang` / `align64` siblings out). Read the fourth and fifth bullets
  above first: the `auto` route is flat across the pin (126 cells, median
  ×1.0040) EXCEPT for the one route change, and the `vm-in` Δ spans three
  abi steps. THE `_in` CONTROL'S OWN ANSWER is in the `floor` rows: `vm`
  63,198.1 and `vm-in` 63,084.6 ns/set throughput at d34c9131 against
  63,140.3 (`vm`, 334fd10e) and 31,612.0 (`vm-in`, 288d505) — the two
  entries now TIE (×1.0018) and the ×2.0 tripwire is on BOTH.
  `.subject-grain.md` carries the per-(rung, subject) rows the ledger's
  `d-01024` / `r-01024` tables are read from; `.tsv` the set-grain query.
- `2026-09-06-loglines-0.1-budu-ryzen1600-clsfold-d34c9131.md` — the
  **PREDICTED-NULL pair on loglines@0.1**: `pcrec-auto` against
  `pcrec-auto-noclsfold`, two cells `measured` 14:45–15:02 EDT. Query:
  `report --subbench loglines --version 0.1 --since 2026-09-06T18:40:00Z
  --until 2026-09-06T19:00:00Z --testee pcrec_d34c9131_auto-caps-simdna
  --testee pcrec_d34c9131_auto-caps-simdna_noclsfold` — **2 records, 0
  superseded.** The prediction HELD: 22 of 22 (pattern × form) artifacts
  identical on every size and stamp field, `clsfolds=0` on the two VM ones
  (`level-context`'s [SEL-1] hybrid, `islands=2`), no clause on the 20 DFA
  ones, and the 22 set cells 0.9951–1.0134. This is the file to quote for
  the day's noise floor. `.subject-grain.md` carries the 16 KB–1 MB sweep
  per flavour; `.tsv` the same query.
- `2026-09-06-email-specimen-0.2-budu-ryzen1600-clsfold-d34c9131.md` — the
  **PREDICTED-NULL pair on email-specimen@0.2**, the same two arms, two
  cells `measured` 15:02–15:12 EDT. Query: as above with `--subbench
  email-specimen --version 0.2 --since 2026-09-06T19:00:00Z --until
  2026-09-06T19:15:00Z` — **2 records, 0 superseded.** Null for a stronger
  reason than loglines': all six artifacts are DFA, so `clsfolds=` prints
  NOWHERE in this file and the deny flag cannot reach anything. Nine set
  cells 0.9970–1.0058, the tightest pair of the wave. `.subject-grain.md`
  and `.tsv` the same query.
  Ledger for all five groups:
  `docs/dev/ledgers/2026-09-06-b39-clsfold-after-d34c9131.md`.

**[B37] reports (2026-09-05, lane b37read) ADDED five file groups — the
2026-09-05 DAYTIME window at pcrec pin 334fd10e (abi 22), the [B37]
DENY-FLAG-SPLIT AFTER** — and changed NOTHING else here: the reporter is
`v14 (2026-09-05)` (lane b37repin's `folds=` / `islands=` / `shape=` clauses,
merged before the window ran), no committed report was regenerated, no
reporter code was touched. Every one of the fifteen new files carries an
explicit `--since`/`--until` PAIR *and* an explicit `--testee` roster (the
2026-08-30 rule and KB-5's roster). The window: 10 cells, ALL `measured` at
attempt 1 under BD7, 03:48:36 → 07:22:14 EDT (suite log
`build/windows/suite_20260905T074836Z.log`), store 134 → 144; the ten
records were committed on master (344ebb6) before these were rendered; this
lane rendered from `--store ~/pcrec-bench/store` and commits no store file.

RE-RENDER INVARIANT, checked the same two ways as the 2026-09-03 and [B34]
waves, because the fifteen files were rendered IN-PROCESS (the 144-record
store loaded and validated ONCE — **582 s on this box** — and reused for
all fifteen; the same `build_report`/`render_markdown`/`render_tsv` calls a
CLI invocation makes; the five groups then rendered in 77 s total):

1. **CLI equivalence**, proven on
   `2026-09-05-altwide-0.2-budu-ryzen1600-island-334fd10e.md`: a fresh
   `python3 -m pcrecbench report …` invocation of that file's own committed
   query diffs BYTE-IDENTICAL against the committed file (`cmp` clean).
2. **Determinism over all fifteen**: a second, independent in-process render
   into a scratch directory diffs clean on all fifteen files (`cmp` on
   each).

FOUR THINGS A READER OF THIS WAVE SHOULD KNOW BEFORE THE NUMBERS:

- **The island PAIR is a NULL pair on altwide, by construction of the set,
  not by a harness fault.** `pcrec-auto` selects the DFA on all 34 (pattern
  × form) cells it compiles on `altwide@0.2` — there is no VM-selected form
  on the auto route of this set — so `-fno-alt-island` has nothing to deny:
  the island file's two records are byte-identical on every artifact
  (emit / code / `.so` bytes, every stamp; `islands=` prints on NEITHER),
  and the 53 shared set cells read 0.992–1.010. The island's EFFECT is
  readable only on the forced-VM arms, and only CROSS-PIN (the AFTER file,
  `pcrec_334fd10e_vm*` against `pcrec_1989c62_vm*`), where it travels with
  abi 17's `always_inline` (frameless-gated — every island artifact is
  `frameless=1`) and abi 22's `shape=shared` entry, so that reading is
  three pcrec changes, not one. The one-variable island reading in THIS
  wave is on bounded: the `ctx-*` hybrids stamp `islands=2` with
  `shape=plain`, `frameless=0` (neither abi 17 nor abi 22 touches them),
  and move ×0.65 on `match-compliance` across the pin.
- **The altwide AFTER file is CROSS-PIN against 1989c62, not 288d505**:
  altwide was never measured at 288d505, so the R8 `Δ vs previous version`
  column fires 334fd10e ↔ 1989c62 (it reads `faster ×121.57` on `w-256` /
  throughput / `vm`), and the pcre2 rows are the 2026-09-03 records (the
  pcre2 arms were not re-run: unpinned baselines). `vs best` mixes pins —
  read the Δ column or same-pin rows, never `vs best` across pins.
- **The bounded fold file's BEFORE for `pcrec-auto` is the 04:10:50Z ccboth
  record, not the 00:47:59Z six-testee one.** Both are `pcrec_288d505_auto`
  and newest-measured-wins cannot be told to prefer the older; a `--since`
  that admits the 00:47Z record also admits the 04:10Z one and the 04:10Z
  one ranks. The two agree to median 0.9998 over 126 cells (ledger
  2026-09-05 §4.3), and the ledger reads the plain ladder against BOTH and
  says which. The clang BEFORE is the same night's 04:50:54Z record.
- **`shape=` never prints `inline`** in any of these files, and prints
  `shared` only on altwide's islands (all > 4,096 program bytes);
  `forward` on every frameless bounded/altwide/loglines VM artifact,
  `plain` on every framed one — pcrec's AUTO rule holds on 100 % of the
  VM artifacts in the wave. The I-37 cell (`floor` / `match-compliance` /
  `pcrec-auto`) is a DFA artifact and carries NO `shape=` stamp: I-44's
  "read the stamp on your gcc arm" cannot be done on that cell.

- `2026-09-05-altwide-0.2-budu-ryzen1600-island-334fd10e.md` — the
  **ISLAND PAIR**: `pcrec-auto` against `pcrec-auto-noisland` (the same
  config with `-fno-alt-island`, deny bit 23) at 334fd10e, two cells
  `measured` 03:49–04:07 EDT back to back. Query: `report --subbench altwide
  --version 0.2 --since 2026-09-05T07:48:00Z --until 2026-09-05T08:00:00Z
  --testee pcrec_334fd10e_auto-caps-simdna --testee
  pcrec_334fd10e_auto-caps-simdna_noisland` — **2 records, 0 superseded.**
  A PAIR report, and a NULL one (the first bullet above): every legend line
  is identical between the arms but for the testee id, the compile table's
  sizes are byte-identical on all 34 compiled cells and the 32 refusals
  quote the same integers, and no `Δ` fires (the deny word lives in
  `config_extra`, not the pin). Read it as the CONTROL that the deny flag
  is inert where nothing is VM-selected — the reason the island's numbers
  are in the next file. `.subject-grain.md` and `.tsv` the same query.
- `2026-09-05-altwide-0.2-budu-ryzen1600-after-334fd10e.md` — the
  **altwide@0.2 AFTER at 334fd10e, CROSS-PIN against the 2026-09-03 first
  sample at 1989c62**: the five 334fd10e arms (`auto`, `auto_noisland`,
  `auto-nocaps`, `vm`, `vm-in`), the four `pcrec_1989c62_*` arms of
  2026-09-03 and the two libpcre2 baselines of 2026-09-03. Query: `report
  --subbench altwide --version 0.2 --since 2026-09-03T03:50:00Z --until
  2026-09-05T08:40:00Z` plus ELEVEN `--testee` values
  (`libpcre2_10.46_{interp,jit}-caps-simdna`,
  `pcrec_334fd10e_{auto,auto_noisland,auto-nocaps,vm,vm-in}-caps-simdna`
  — the noisland id is `pcrec_334fd10e_auto-caps-simdna_noisland` — and
  `pcrec_1989c62_{auto,auto-nocaps,vm,vm-in}-caps-simdna`) — **11 records,
  0 superseded** (the `--since` excludes nothing older on this set; the
  `--until` excludes the loglines/bounded cells of the same morning, which
  are other sub-benches anyway, and the two 2026-09-03 bigcap records are
  kept out by the roster). READ THE ORDER PAIR FIRST: `w-256` and `srt-256`
  on `pcrec_334fd10e_vm` are 15,886,650 vs 15,875,364 ns/set throughput
  (×1.0007; 1989c62 read ×8.87), both `islands=1`, `shape=shared (prog:
  305,686 B)`, 292,043 B of code — the 2026-09-03 ledger's ×8.87 branch-order
  effect is gone at the source, as I-43 predicted. `w-384` COMPILES on both
  VM arms (427,824 B, `faster` against a 1989c62 refusal has no Δ — the row
  simply ranks, 1st, ×24.9 under the JIT), and so does `pfx3-512`
  (440,187 B; not in [B37]'s build facts). The VM route's Δ column reads
  `faster ×13.71 … ×701.55` on 54 island-bearing cells, `slower ×2.00` on
  `floor` / throughput (both VM arms — the forced-VM floor tripwire of
  ledger 2026-09-05 §7.5, fired), `unchanged` on `ci-256` (no island). The
  DFA-route auto rows read `unchanged` / `faster ×1.03–1.04` on search and
  `faster ×1.09–1.75` on `match-compliance`. `.subject-grain.md` (`--grain
  subject`) carries the per-subject order pair (×0.9994–1.0014 on all four
  throughput subjects); `.tsv` the same set-grain query (no Δ column).
- `2026-09-05-loglines-0.1-budu-ryzen1600-noedge-334fd10e.md` — the
  **[OPT-EDGE] pair's THIRD SAMPLE and the abi-19/21 dispatch's AFTER**:
  `pcrec-auto` against `pcrec-auto-noedge` at 334fd10e, two cells
  `measured` 04:46–05:02 EDT back to back. Query: `report --subbench
  loglines --version 0.1 --since 2026-09-05T08:40:00Z --until
  2026-09-05T09:00:00Z --testee pcrec_334fd10e_auto-caps-simdna --testee
  pcrec_334fd10e_auto-caps-simdna_noedge` — **2 records, 0 superseded.** A
  PAIR report on the same terms as the 2026-09-03 and [B34] ones. `iso-ts`
  reads noedge ÷ auto **0.9846 search / 0.9945 throughput** against
  0.9157 / 0.9388 at 288d505 (I-43 predicted ×0.9995 for its own
  harness); `http-5xx` 0.981 / 0.999, `ipv6` 0.993 / 0.983; the eight
  zero-edge patterns 0.998–1.011. The legend still proves the arm
  one-variable (`edge=`/`edges=` to `none`/`0`, `folds=0` on all 22,
  `islands=2` on `level-context` both arms); the noedge artifact is now
  6,256 B SMALLER on `iso-ts` (34,185 vs 27,929 — the dispatch's +1,468 B
  sits on the auto side) and +6 B on every zero-edge pattern as before.
  `.subject-grain.md` carries the 16 KB–1 MB sweep per flavour; `.tsv` the
  set-grain query.
- `2026-09-05-loglines-0.1-budu-ryzen1600-noedge-3pins-334fd10e.md` — the
  same pair rendered CROSS-PIN against the 288d505 pair (2026-09-05
  03:48Z / 03:56Z) and the 1989c62 pair (2026-09-03), a roster of SIX
  (`pcrec_{334fd10e,288d505,1989c62}_auto-caps-simdna` and their
  `_noedge` siblings) with `--since 2026-09-03T03:50:00Z --until
  2026-09-05T09:00:00Z` — **6 records, 0 superseded.** The R8 Δ column
  fires per config against the NEXT-OLDER pin: `iso-ts` auto reads
  `faster ×1.06` throughput / `faster ×1.07` search (334fd10e vs 288d505)
  beside `unchanged` on the 288d505-vs-1989c62 row, and the three noedge
  rows read `unchanged` twice over — the deny arm is the flat control
  across all three pins (1,142,263 / 1,142,674 / 1,142,842 ns/set on
  `iso-ts` throughput). 73 of 88 Δ cells `unchanged (within spread)`.
- `2026-09-05-bounded-0.3-budu-ryzen1600-fold-334fd10e.md` — the
  **[CC-DIFF] FOLD WITNESSES, the vm-arm dispatch question and the I-37
  cell at 334fd10e**, CROSS-PIN against the 2026-09-05 288d505 records:
  `pcrec_334fd10e_{auto,vm,auto_cc-clang}` (05:03–07:22 EDT, 44.8 / 45.7 /
  48.2 min) against `pcrec_288d505_auto` (the **04:10:50Z ccboth record** —
  third bullet above), `pcrec_288d505_vm` (02:12:49Z, the six-testee pass)
  and `pcrec_288d505_auto_cc-clang` (04:50:54Z). Query: `report --subbench
  bounded --version 0.3 --since 2026-09-05T02:00:00Z --until
  2026-09-05T11:00:00Z` plus the six `--testee` values — **6 records, 0
  superseded** (the `--since 02:00Z` is the cut that EXCLUDES the 00:47:59Z
  auto record; a `--since` before it would admit it and the 04:10Z one
  would still rank). Three gcc/clang pairs of ONE config plus a forced-VM
  arm: the Δ column fires per config across the pin (`faster ×1.59` on
  `cls-upto-4` / throughput / auto — the fold witness; `faster ×1.29` on
  `dig-upto-16` / match / vm; `faster ×1.07` on BOTH arms of the I-37 cell,
  gcc 492.2 → 459.6, clang 231.5 → 217.1, ratio 0.4725; `slower ×2.00` on
  `floor` / throughput / vm — the tripwire); the gcc/clang division is the
  reader's own, never the Δ column's. `.subject-grain.md` carries the
  per-(rung, subject) rows the ledger's `d-01024` dispatch table is read
  from (`cls-upto-1024` / `d-01024`: vm 10.2 → 7.0 ns); `.tsv` the same
  set-grain query.
  Ledger for all five groups:
  `docs/dev/ledgers/2026-09-05-b37-denysplit-after-334fd10e.md`.

**[B34] reports (2026-09-05, lane s2read) ADDED five file groups — the
2026-09-04/05 window at pcrec pin 288d505 (abi 16, [OPT-5] STEP 2)** — and
changed NOTHING else here: the reporter is unchanged at `v13 (2026-09-03)`,
no committed report was regenerated, no reporter code was touched. Every one
of the fifteen new files carries an explicit `--since`/`--until` PAIR *and* an
explicit `--testee` roster (the 2026-08-30 rule and KB-5's roster). The
window: 12 cells, ALL `measured` at attempt 1 under BD7, 19:27:55 →
02:22:30 EDT (suite log `build/windows/suite_20260904T232755Z.log`), store
122 → 134. The records were UNCOMMITTED in master's tree when these were
rendered (the manager commits the store first; this lane rendered from
`--store ~/pcrec-bench/store` and commits no store file).

RE-RENDER INVARIANT, checked the same two ways as the 2026-09-03 wave, because
the fifteen files were rendered IN-PROCESS (the 134-record store loaded and
validated ONCE — **535 s on this box** — and reused for all fifteen; the same
`build_report`/`render_markdown`/`render_tsv` calls a CLI invocation makes):

1. **CLI equivalence**, proven on
   `2026-09-05-email-specimen-0.2-budu-ryzen1600-after-288d505.md`: a fresh
   `python3 -m pcrecbench report …` invocation of that file's own committed
   query diffs BYTE-IDENTICAL against the committed file (`cmp` clean; the
   CLI invocation took the same ~9 minutes, all of it store validation).
2. **Determinism over all fifteen**: a second, independent in-process render
   into a scratch directory diffs clean on the twelve files rendered in the
   first pass (`cmp` on each); the three bounded files are the second
   pass's own output (the first pass refused their query on a mistyped
   roster id — `--testee` REFUSES an unknown id BY NAME rather than
   narrowing silently, which is KB-5's contract working as designed).

THREE THINGS A READER OF THIS WAVE SHOULD KNOW BEFORE THE NUMBERS:

- **`start=` prints for the first time, and it does NOT read the way the
  pin's own inbox item predicted.** `start=pinned` fires on exactly FIFTEEN
  artifacts per auto-route bounded record — the PLAIN form of every
  `cls-upto-4 … cls-upto-16384` rung, `grp-upto-1024` and `cls-lazy-16384`
  — and `start=reverse-pass` on every whole-subject artifact (39/39),
  every hybrid (the `sel=collapsed-prefilter` rows), and every loglines and
  email artifact. The [OPT-5] STEP 2 customers named in ledger 2026-09-02
  §10 (the whole-subject `cls-upto-2048/4096/8192` search-filter rungs)
  stamp `reverse-pass`. `frameless=` prints on every VM artifact (0/1) and
  agrees with `resume_frames == 1` on all 100 VM artifacts of the two
  gcc arms.
- **The cross-pin bounded file's `vs best` mixes pins.** Read the READER'S
  CAVEAT on the 2026-08-31 a7e0bdf entry below: with ten testees from two
  pins in one table, `vs best` inverts visually wherever an older pin's row
  ranks first (it does, on many search-band cells, because the 288d505
  plain artifacts got faster). Read the R8 `Δ vs previous version` column,
  or same-pin rows, never `vs best` across pins.
- **The ccboth file is a PAIRS report, not a ranking** — three gcc/clang/
  gcc+`-falign-functions=64` arms of ONE config; read down each pair.

- `2026-09-05-bounded-0.3-budu-ryzen1600-step2-after-288d505.md` — the
  **[OPT-5] STEP 2 AFTER** on `bench/bounded@0.3` at pcrec **288d505** (abi
  16): six cells `measured` 2026-09-04 19:28 – 23:47 EDT (the two libpcre2
  baseline re-runs and `pcrec_288d505_{auto,auto-nocaps,vm,vm-in}`),
  rendered CROSS-PIN against the 2026-09-02 BEFORE
  (`2026-09-02-bounded-0.3-*-first-sample-1989c62.*`) so the R8 Δ column
  fires on every pcrec row. Query: `report --subbench bounded --version 0.3
  --since 2026-09-02T02:40:00Z --until 2026-09-05T03:50:00Z` plus TEN
  `--testee` values — `libpcre2_10.46_{interp,jit}-caps-simdna`,
  `pcrec_288d505_{auto,auto-nocaps,vm,vm-in}-caps-simdna` and
  `pcrec_1989c62_{auto,auto-nocaps,vm,vm-in}-caps-simdna` — **12 records
  matching, 10 included, 2 superseded** (the 2026-09-02 pcre2 pair,
  newest-measured-wins; the header reads `record source: … (12 record(s)
  matching this query)` / `records included: 10` / `superseded: 2`).
  THE `--until 2026-09-05T03:50:00Z` IS LOAD-BEARING: the same night's ccboth
  pass wrote a SECOND `pcrec_288d505_auto-caps-simdna` bounded record at
  04:10:50Z (the stability control), and a looser bound would make THAT the
  ranked auto record instead of the 00:47:59Z six-testee one. Read against
  ledger 2026-09-02 §10 and I-38: the whole-subject match customers are
  UNMOVED (`cls-upto-2048 ÷ cls-upto-1024` at r-01024 1.986 → 1.987; every
  whole-subject artifact `start=reverse-pass`), while the PLAIN `cls-upto-*`
  ladder (`start=pinned`) moved ×0.64 on `short-subject-search` and
  ×0.67-0.73 on `large-subject-throughput` (letters ×0.50 per byte, digits
  ×0.945) — the R8 column reads `faster ×1.36-1.57` on those rows. The
  `did-not-compile` set is unchanged (`cls-upto-65535`, both forms, both
  auto arms, `NFA exceeds 131072 states`). `.subject-grain.md` (`--grain
  subject`) carries the per-(rung, subject) match rows the ledger's rung
  table is read from; `.tsv` the same set-grain query (no Δ column).
  Ledger: `docs/dev/ledgers/2026-09-05-opt5-step2-after-288d505.md`.

- `2026-09-05-loglines-0.1-budu-ryzen1600-noedge-288d505.md` — the
  **[OPT-EDGE] pair's SECOND SAMPLE** ([B35] (2)): `pcrec-auto` against
  `pcrec-auto-noedge` at 288d505, two cells `measured` 23:48-00:04 EDT back
  to back. Query: `report --subbench loglines --version 0.1 --since
  2026-09-05T03:40:00Z --until 2026-09-05T04:00:00Z --testee
  pcrec_288d505_auto-caps-simdna --testee
  pcrec_288d505_auto-caps-simdna_noedge` — **2 records, 0 superseded.** A
  PAIR report on the same terms as the 2026-09-03 one: read each pattern's
  two rows against each other; the legend proves the arm is one-variable
  (`edge=`/`edges=` to `none`/`0`, everything else identical, every
  artifact +6 B on the noedge side). `iso-ts` reads noedge÷auto 0.916 search
  / 0.939 throughput against 0.918 / 0.937 on 2026-09-03. Every loglines
  artifact stamps `start=reverse-pass`. `.subject-grain.md` carries the
  16 KB-1 MB sweep per flavour; `.tsv` the set-grain query.
- `2026-09-05-loglines-0.1-budu-ryzen1600-noedge-vs-1989c62-288d505.md` —
  the same pair rendered CROSS-PIN against the 2026-09-03 pair at 1989c62,
  a roster of FOUR: the two ids above plus `pcrec_1989c62_auto-caps-simdna`
  and `pcrec_1989c62_auto-caps-simdna_noedge`, with `--since
  2026-09-03T03:50:00Z --until 2026-09-05T04:00:00Z` (the 2026-09-03 auto
  record, 09:11:45Z, is the newest 1989c62 auto record in range; the
  2026-09-02 one is excluded by the `--since`) — **4 records, 0
  superseded.** The R8 Δ column fires auto-vs-auto and noedge-vs-noedge
  (`unchanged (within spread)` on 20 of 22 rows; `faster ×1.01` on
  `hex32-id` thr and `http-5xx` search; `slower ×1.01` on `bignum`
  search). Same `vs best` caveat as every cross-pin file.

- `2026-09-05-email-specimen-0.2-budu-ryzen1600-after-288d505.md` —
  CONTINUITY on `email-specimen@0.2`: the one fresh cell
  `pcrec_288d505_auto` (00:05-00:10 EDT) rendered CROSS-PIN against its
  2026-09-02 predecessor and the two 2026-09-02 pcre2 baselines. Query:
  `report --subbench email-specimen --version 0.2 --since
  2026-09-02T02:40:00Z --until 2026-09-05T04:10:00Z --testee
  libpcre2_10.46_interp-caps-simdna --testee libpcre2_10.46_jit-caps-simdna
  --testee pcrec_288d505_auto-caps-simdna --testee
  pcrec_1989c62_auto-caps-simdna` — **4 records, 0 superseded.** Every Δ
  reads `unchanged (within spread)` or `faster ×1.00`; every artifact
  `start=reverse-pass`, +110 B. This is the file the CLI-equivalence proof
  above was run on.

- `2026-09-05-bounded-0.3-budu-ryzen1600-ccboth-288d505.md` — the **I-37
  CELL WITH BOTH ARMS IN ONE WINDOW plus the `-falign-functions=64` LAYOUT
  PROBE** ([B35] (1), pcrec I-39 (v)): `pcrec-auto` (a SECOND auto record
  the same night, 00:10-00:50 EDT — also the same-pin stability control
  against the six-testee pass's 20:47 EDT record), `pcrec-auto-clang`
  (00:50-01:38) and `pcrec-auto-align64` (01:38-02:22). Query: `report
  --subbench bounded --version 0.3 --since 2026-09-05T04:05:00Z --until
  2026-09-05T06:00:00Z --testee pcrec_288d505_auto-caps-simdna --testee
  pcrec_288d505_auto-caps-simdna_cc-clang --testee
  pcrec_288d505_auto-caps-simdna_cf-align-functions-64` — **3 records, 0
  superseded.** A PAIRS report, NOT A RANKING: three arms of one config
  differing only in the compilee toolchain (`cc-clang`) or OUR phase-2
  flags (`cf-align-functions-64`); read down the pairs, never across; the
  R8 Δ column never fires (the tokens live in `config_extra`, not the pin).
  `floor` / `match-compliance` reads gcc 492.2 / clang 231.5 / align64
  463.1 ns — clang÷gcc 0.470, align64÷gcc 0.941. KB-9's `(clang cc)` note
  fires on every clang `gcc ns` cell. The refusal set is identical on all
  three arms. `.subject-grain.md` and `.tsv` the same query.

**[B31] reports (2026-09-03) ADDED four file groups — the 2026-09-03
window at pcrec pin 1989c62** — and changed NOTHING else here: the reporter
is unchanged at `v12 (2026-09-02)`, no committed report was regenerated, and
no reporter code was touched by this lane. Every one of the twelve new files
carries an explicit `--since`/`--until` PAIR *and* an explicit `--testee`
roster, so each file's selection is exactly its own cells and no later store
growth can drift it (the 2026-08-30 rule, and KB-5's roster on top of it).

RE-RENDER INVARIANT, checked two ways rather than one, because the twelve
files were rendered IN-PROCESS (the 122-record store loaded and validated
ONCE, reused for all twelve — the same `build_report`/`render_markdown`/
`render_tsv` calls a CLI invocation makes; `reports/CLAUDE.md`'s [B32] (b)
paragraph explains why 66 CLI invocations were impractical and the same
arithmetic applies to twelve over a 122-record store):

1. **CLI equivalence**, proven on
   `2026-09-03-loglines-0.1-budu-ryzen1600-noedge-1989c62.md`: a fresh
   `python3 -m pcrecbench report …` invocation of that file's own committed
   query diffs BYTE-IDENTICAL against the committed file.
2. **Determinism over all twelve**: a second, independent in-process render
   into a scratch directory diffs clean on all twelve files.

Together those cover every file (the in-process path is proven equal to the
CLI path once, and every file is proven reproducible from its own query).
A per-file CLI re-render of the two altwide groups was ATTEMPTED and
ABANDONED, and this is recorded rather than glossed: one CLI invocation of
the altwide first-sample query exceeded a 570-second wall cap on a box the
peer manager session (`pcrecdev1`) held that morning, so it was not repeated.
The altwide `.md` files are large (33 patterns × 3 regimes × 6 testees), and
the store validation is paid per invocation.

TWO THINGS A READER OF THIS WAVE SHOULD KNOW BEFORE THE NUMBERS:

- **`scan_edges` prints for the first time.** Lane b32adp's
  `engine_metadata` pair (I-33's per-iteration compare COUNT, distinct from
  `dfa_scan_edge`'s single shape token) landed before this window ran, so
  every 2026-09-03 pcrec record carries it and every legend line in these
  four groups shows `edges=N` or `edges=N (match: M)`. `reports/CLAUDE.md`'s
  [B32] (b) note that "no file carries a `scan_edges` clause" is superseded
  FOR THESE FOUR GROUPS ONLY; the 66 older files still carry none.
- **`table=` finally MOVES, and only under the raised caps.** Every
  `RX_DFA_TABLE` stamp in every committed report before this wave reads
  `premultiplied`. The bigcap group is the first to show `mixed` and
  `indexed` — see its entry.

- `2026-09-03-altwide-0.2-budu-ryzen1600-first-sample-1989c62.md` — the
  FIRST SAMPLE of `bench/altwide@0.2` ([B31]) at pcrec **1989c62** (abi 15):
  six cells `measured` 2026-09-02 23:59 – 2026-09-03 02:45 EDT, all at
  attempt 1 under BD7, `--trials 5`, reporter v12. Query: `report --subbench
  altwide --version 0.2 --since 2026-09-03T03:50:00Z --until
  2026-09-03T10:20:00Z` plus the six `--testee` values
  `libpcre2_10.46_{interp,jit}-caps-simdna` and
  `pcrec_1989c62_{auto,auto-nocaps,vm,vm-in}-caps-simdna` — **6 records, 0
  superseded.** The roster is explicit because the same window's two
  raised-cap testees satisfy the same subbench/version/date filters and are
  the NEXT file's job. READ THE REFUSAL TABLE FIRST, as with altwide@0.1:
  `pcrec-auto`/`-nocaps` refuse 32 of 66 (pattern × form) compile cells at
  the TOTAL emitted-source cap (1,000,000 B) and `pcrec-vm`/`-vm-in` refuse
  26 of 66 at the CODE cap (500,000 B), both diagnostics printed verbatim by
  R10. The 0.2 dense ladder BRACKETS the boundary 0.1 could only place at
  "≥ 512": `w-256 plain` compiles on all four (977,055 B source / 341,111 B
  code) and **`w-384` refuses on all four** — 1,431,536 B source (43 % over)
  and 508,517 B code (**1.7 % over**). Read it with `bench/altwide/NOTES.md`'s
  P9-P18 and `docs/dev/measurements/2026-09-02-altwide-raised-cap-sizes.txt`
  (whose section-1 sizes this sample reproduces to the byte on every shared
  cell). READER'S CAVEAT: `s-512` COMPILES here on every config — the census's
  finding 5 was right and the NOTES' "thirteen wide rungs" is twelve.
  `.subject-grain.md` (`--grain subject`) and `.tsv` the same query.

- `2026-09-03-altwide-0.2-budu-ryzen1600-bigcap-1989c62.md` — the RAISED-CAP
  PAIR against their plain siblings, a four-testee roster of TWO
  gcc/gcc pairs differing only in `--max-emit-bytes` / `--max-emit-code-bytes`
  (both raised to 8,388,608 = 8 MiB, the census's own bound): `pcrec-auto` vs
  `pcrec-auto-bigcap` and `pcrec-vm` vs `pcrec-vm-bigcap`, four cells
  `measured` (the plain pair inside the six-testee pass above; the bigcap
  pair 2026-09-03 02:45-05:11 EDT under a raised `cell_cap=14400s`, which was
  NEEDED — `pcrec-vm-bigcap`'s cell ran 121.5 minutes, over the standing
  5,400 s cap). Query: as the first-sample entry but with the four
  `--testee` values `pcrec_1989c62_{auto,vm}-caps-simdna` and their
  `_emitcap-8388608-codecap-8388608` siblings — **4 records, 0 superseded.**
  READ DOWN EACH PAIR, never across the table: the ranking's `vs best` and
  `vs baseline` columns mix all four arms and only the same-engine
  default-cap/raised-cap division is a statement about the cap. This is the
  file the `RX_DFA_TABLE` transition is readable in, and the file P16 is
  scored on. The R8 `Δ vs previous version` column never fires between a
  plain arm and its bigcap sibling — the cap tokens live in `config_extra`,
  not the pin, exactly as the `-cc-` groups' clang siblings do — so the
  pair ratio is the reader's own division, and the delivery/ledger states it.
  `.subject-grain.md` and `.tsv` the same query.

- `2026-09-03-loglines-0.1-budu-ryzen1600-noedge-1989c62.md` — the
  **[OPT-EDGE] BEFORE/AFTER PAIR** (inbox I-33): `pcrec-auto` against
  `pcrec-auto-noedge` (the same config with `-fno-scan-edge`), two cells
  `measured` 2026-09-03 05:11-05:28 EDT back to back in one window, reporter
  v12. Query: `report --subbench loglines --version 0.1 --since
  2026-09-03T03:50:00Z --until 2026-09-03T10:20:00Z --testee
  pcrec_1989c62_auto-caps-simdna --testee
  pcrec_1989c62_auto-caps-simdna_noedge` — **2 records, 0 superseded.** A
  PAIR report, not a ranking, on the same terms as the `-cc-` groups: read
  each pattern's two rows against each other. The deny flag is a CLEAN
  one-variable control and the legend proves it — `edge=` and `edges=`
  move to `none`/`0` on every pattern, and `prefilter=`, `table=`, `match=`,
  `sel=` and `lang=` are unchanged on all eleven. loglines has TWO regimes
  (search and throughput), not three; there is no `match-compliance` group
  here. Read beside the 2026-09-02 full-suite ledger §7.2 (the regression
  family this arm is the counterfactual for) and the same-pin
  `pcrec-auto` numbers in
  `2026-09-02-loglines-0.1-budu-ryzen1600-after-1989c62.*`, which this
  window re-measured as an unasked-for stability control (22/22 cells
  within 1.32 %).
  `.subject-grain.md` carries the 16 KB-1 MB sweep per flavour; `.tsv` the
  set-grain query.

- `2026-09-03-bounded-0.3-budu-ryzen1600-cc-rerun-1989c62.md` — the **I-37
  RE-RUN** of the one cc-axis cell pcrec's [CC-DIFF] STEP 0 could not
  reproduce (`floor` / `match-compliance` / `auto`, clang ÷ gcc 0.432, marked
  PROVISIONAL in the 2026-09-02 ledger §5.4): `pcrec-auto-clang` re-measured
  2026-09-03 05:28-06:16 EDT against the UNCHANGED 2026-09-02 gcc arm.
  Query: `report --subbench bounded --version 0.3 --since
  2026-09-02T02:40:00Z --until 2026-09-03T10:20:00Z --testee
  pcrec_1989c62_auto-caps-simdna --testee
  pcrec_1989c62_auto-caps-simdna_cc-clang` — **2 records included, 1
  superseded** (the 2026-09-02 clang record, which newest-measured-wins
  replaces). The `--since` is DELIBERATELY wider than the other three groups'
  and is the reason the roster is only two ids: the gcc arm of this pair was
  measured in the 2026-09-02 overnight window and there is no 2026-09-03 gcc
  record to pair with.
  **THE CAVEAT THAT GOVERNS EVERY NUMBER IN THIS FILE: only the CLANG arm was
  re-measured.** The gcc column is the same 2026-09-02 record the provisional
  ledger row was computed from, so this file re-confirms clang's 217.5 ns and
  does NOT independently re-confirm gcc's 503.3 ns — which is the half
  pcrec's [CC-DIFF] disputes (it read 307 ns). A reading that says "0.432
  reproduced" must say which half reproduced.
  Same reading rule as the `-cc-` groups: down the pair, never across; KB-9's
  `(clang cc)` note fires on every `gcc ns` cell of the clang arm.
  `.subject-grain.md` and `.tsv` the same query.

**[B32] (b) (2026-09-02) regenerated EVERY committed report against
reporter `v12 (2026-09-02)`** (docs/dev/known_issues.md KB-8/KB-9,
ledger docs/dev/ledgers/2026-09-02-full-suite-1989c62.md §12 (d)). All
66 files re-rendered from their OWN recorded query (parsed out of each
file's own header, grain and format from its own name) and diffed
against the committed content; every diff was fully explained before
being written back (a per-file classifier: the version line, KB-8's
`record source` line moving from `(N candidate file(s))` — the whole
store's total — to `(N record(s) matching this query)` — this query's
own filtered count, KB-9's `(clang cc)` suffix + legend note, and the
new unconditional `worst other-core busy: ...` header line, and
NOTHING else). Per-file breakdown:

- **Every one of the 66 files**: the version line (`v11` → `v12`), the
  `record source`/`source:` line — its NUMBER moves too, from the
  store's WHOLE candidate-file count (81 or 111, depending on when the
  file was last rendered) to THIS QUERY's own filtered count (KB-8;
  e.g. the loglines AFTER report's twelve-testee roster over a 111-record
  store now reads `18` — every record any of those testee_ids ever
  wrote, before the newest-measured dedup narrows it to the 12 the
  ranking uses — not `111`) — and the new `worst other-core busy: N%
  (testee / pattern / regime)` (or `n/a`) header line, unconditional on
  every file regardless of `--include-provenance`. Neither moves any
  ranking, verdict, or other number in the report: KB-8's count and the
  provenance line are both header-only facts about the query and the
  run, not about the rows.
- **The two `cc-1989c62` groups only** (`2026-09-02-bounded-0.3-*-cc-
  1989c62.{md,subject-grain.md,tsv}`, `2026-09-02-loglines-0.1-*-cc-
  1989c62.{md,subject-grain.md,tsv}` — 6 files, the only committed
  reports with a `_cc-clang` testee in their roster): KB-9's `(clang
  cc)` suffix on every `pcrec_..._cc-clang` row's `gcc ns` cell, plus
  the legend note stating the rule once per table that carries at least
  one clang row. The `.tsv` files move on the version/count line only
  (the phase columns are markdown-only, `pcrecbench/CLAUDE.md`'s [B32]
  section).
- **No file** carries a `scan_edges` clause: no record in `store/` yet
  carries the pair (lane b32adp's own change), so that clause and its
  note print on none of the 66.
- **`make check-report` is 73/73** (66 `test_report.py` + 7 new
  `test_quick.py`, KB-10 — `pcrecbench/__main__.py`, not `report.py`,
  so it moves no committed report's rendering).

Regenerated IN-PROCESS (load and validate `store/`'s 111 records ONCE,
reuse for all 66 renders) rather than via 66 separate CLI invocations —
measured: one CLI invocation against the current store's `index.tsv`
takes minutes on its own (jsonschema validates the WHOLE store on every
`load_all`, regardless of how narrow the query's own filters are; the
[B12] test-suite note profiles this same cost at ~39 s for 26 records,
which scales to minutes at 111), so 66 of them sequentially would have
been impractical for one session. The in-process script paid the
validation cost once and reused the loaded, validated records for every
query — the SAME `report.build_report`/`render_markdown`/`render_tsv`
calls a fresh CLI invocation would make, just without re-validating the
store 66 times.

**[B26] (c) (2026-09-02) ADDED six file groups — the full-suite night at
pcrec pin 1989c62 (abi 15)** — and changed NOTHING else here: the reporter
is unchanged at `v11 (2026-09-01)`, no committed report was regenerated,
and the RE-RENDER INVARIANT was checked instead. All 48 report files
committed before this wave were re-rendered from their OWN committed query
(parsed out of each file's own header, grain and format from its own name)
and diffed against the committed content. **42 of the 48 are clean**: the
only line that moves is `record source: store/index.tsv (N candidate
file(s))`, 81 → 111, which is store growth and is explicitly NOT grounds to
reject a diff (the [B19] wave's rule, below). No number, ranking, verdict or
legend fact moved on any of them. `make check-report` is 62/62.

**THE OTHER SIX DRIFTED, and the fix is the 2026-08-30 RULE this directory
already carries.** `2026-08-30-email-specimen-0.2-*-after-96e44c2.*` and
`2026-08-30-loglines-0.1-*-after-96e44c2.*` were committed with a BARE
`--since 2026-08-30T11:00:00Z` and no upper bound, so the night's own
records (2026-09-02, the same sub-bench and version) satisfy their queries
and a bare re-render silently turned each single-pin AFTER report into an
undocumented cross-pin one: email picked up four `pcrec_1989c62_*` rows and
both newer pcre2 records (6 records → 10), loglines the same shape. This is
the THIRD sighting of the failure mode KB-5 names, and it shows the [B28]
fix was INCOMPLETE: loglines' file already carried the six `--testee`
values, and the roster did not save it, because the two pcre2 ids carry no
pin and newest-measured-wins pulled their 2026-09-02 records in regardless.
A ROSTER CANNOT BOUND TIME; only `--until` can. FIXED by giving all three
`-after-96e44c2` groups the upper bound their own sibling `-repin-96e44c2`
files have used since they were written, `--until 2026-08-30T15:00:00Z`
(every 96e44c2 window record is ≤ 14:36:42Z, so the bound excludes nothing
those files ever contained). `bounded-0.1-*-after-96e44c2.*` was NOT
drifting — its `--version 0.1` filter happens to protect it — but it has the
same open bound and is bounded here too rather than left as a landmine for
the next window. After the fix each of the nine files diffs against its
committed content on exactly two lines: its own `filters:`/header line
gaining `until=2026-08-30T15:00:00Z`, and the candidate count. Verified file
by file; no number, ranking, verdict or record list moved. The night's thirty records (28 from
`scripts/run_window.sh`, 2 re-run by hand — the two bounded@0.3 clang cells
the 3000 s per-cell cap killed) are all `measured`; every query below names
its roster with KB-5's `--testee` and carries an explicit `--since`/`--until`
pair, so none of them can drift when the store grows again.

TWO THINGS A READER OF THIS WAVE SHOULD KNOW BEFORE THE NUMBERS:

- **`declined-nullable-default` does not appear.** abi 14's eighth
  `RX_ENGINE_SEL` value — the one whose rendering `report.py` gained a
  conditional legend sentence for at [B26] (a) — is stamped by NO artifact
  in any of the four sets, exactly as the re-pin census predicted. So the
  legend's alternative bucket suffix (`prefilter declined, no cap hit`)
  still prints nowhere, and the note above about "the first report to print
  either is the one the [B26] window writes" is answered: it does not.
- **the `-cc-` files are PAIR reports, not rankings.** Each holds three
  gcc/clang pairs of ONE pcrec config; the comparison a reader wants is
  down each pair, not across the table. The `_cc-clang` suffix is part of
  the testee's CONFIG, not its pin, so the reporter's R8 `Δ vs previous
  version` column never fires between a gcc arm and its clang sibling (it
  matches on engine + config across pins) — the pair ratio is the reader's
  own division, and the delivery/ledger states it.

**Reports are RE-RENDERED when the reporter changes** ([B9], 2026-08-25):
the STORED RECORDS are the data; a report is a VIEW over them, and the
view is versioned separately (`reporter: vN (date)`, a header line every
render carries — `pcrecbench/report.py`'s `REPORTER_VERSION`). When
`report.py`'s rendering changes, every committed report is regenerated
with the SAME QUERY that produced it (named in its own header) so the
file keeps its identity (the same records, the same filters) while
picking up the new columns/rulings. `report … | diff - <file>` is empty
immediately after a regeneration — the reporter is deterministic, so a
non-empty diff after a bare rerun (no query change, no reporter change)
means either the store changed or the reporter regressed determinism.

**[B28] (2026-09-01) regenerated every report below against reporter
`v11 (2026-09-01)`. NOTE ([B26], the 1989c62 re-pin): the legend gains
one CONDITIONAL sentence and one alternative bucket suffix — pcrec abi
14's `declined-nullable-default` renders `sel=… (prefilter declined, no
cap hit)` rather than `(DFA fallback tripped)`, because nothing
overflowed on that path — and BOTH print only on a report whose records
carry the token. No stored record does, so every committed file below
still renders byte-identically and the version did NOT move; the first
report to print either is the one the [B26] window writes. Before that:
KB-5's `--testee` roster filter, KB-6's `edge=`
clause** (docs/dev/known_issues.md KB-5, KB-6). Same queries as before,
byte for byte (each file's own header query), with ONE deliberate
exception explained below. The diff on every file is the version line
(`v10` → `v11`); on the three `pcrec_a7e0bdf` bounded@0.2 files
(`2026-08-31-bounded-0.2-*-after-a7e0bdf.*`) it is ALSO the new `edge=`
clause on every `pcrec_a7e0bdf` legend line plus its legend note (110
lines changed on each `.md`, 3 on the `.tsv` — the KB-6 `compile_stamp`
row) — no number, ranking, verdict or other legend fact moved. Every
other file's diff is the version line alone. Classified per file by
`git diff --numstat` against the expected shape (2/2 for a bare version
bump; the a7e0bdf trio's larger, expected counts); zero unexplained
lines.

THE ONE EXCEPTION: regenerating `2026-08-30-loglines-0.1-budu-ryzen1600-
after-96e44c2.{md,subject-grain.md,tsv}` from its LITERAL committed
query (`subbench=loglines, version=0.1, since=2026-08-30T11:00:00Z` --
an OPEN upper bound) picked up two records this file never had: the
`pcrec_263b013` loglines KEEP-arm rows the 263b013 window measured the
NEXT day (`20260831T175140Z`/`20260831T180012Z`), which also satisfy
`since=2026-08-30T11:00:00Z` and were not yet in the store the last time
this file was rendered. That is real STORE GROWTH unrelated to this
wave's rendering rules — exactly the failure mode KB-5 exists to fix
(a `since`-only query has no ceiling, so it silently absorbs whatever
the store gains later), caught here reproducing on an OLDER report
than the one KB-5's own history names. Folding those two records in
under a bare version-bump regen would have violated this file's own
rule ("the ONLY diffs must be the version line") by smuggling in a
real content change, and would have quietly turned a single-pin AFTER
report into a second, undocumented cross-pin one. FIXED by using KB-5's
own new flag: the three files' query now ALSO carries the six
`--testee` values the original committed content named (unchanged
roster, explicit instead of implicit), so their diff is back to the
version line plus the query header's own `testee=` echo (3 lines
changed on the `.md`/`.subject-grain.md`, 1 on the `.tsv` — the header
comment). The three files' own header query line now reads the full
explicit roster; every other `since`-only or `until`-only report in
this directory was checked against today's store and confirmed stable
(no candidate file count / record count drift) before being classified
clean above.

**[B22] (2026-08-31) regenerated every report below against reporter
`v10 (2026-08-31)` — the VALUE-only fallback bucket** (pcrec pin 263b013;
inbox I-25: pcrec's [LIM-1] gave the size-cap rescue its own
`RX_ENGINE_SEL` token, so `_engine_sel_display`'s I-19 (3) interim rule —
bucketing a `selected` artifact on its `vm_prefilter_lang_why`'s
`size cap retry` prefix — is RETIRED and the bucket reads
`sel not in (selected, forced)` and nothing else). Same queries as
before, byte for byte (each file's own header query). The diff on every
file is exactly: the version line (`v9` → `v10`), and — only on the
twelve `96e44c2` `.md` files, the ones whose legends print a `sel=`
clause — the reworded legend-note bullet naming the five tokens. NO
number, ranking, verdict or other legend fact moved (no stored record
carries a size-cap rescue — the [B19] census — so the retired rule never
fired on a committed rendering); the `.tsv` files move only on the
version line ("sel" renders raw in TSV rows). Classified per file by
the same method as [B20]'s wave; zero unexplained lines.

**[B20] (2026-08-30) regenerated every report below against reporter
`v9 (2026-08-30)` — the schema v1.4 wave** (docs/design/gate_shape_v14.md
§6; the regeneration is forced by R3/R4/R4′/R5′ changing the rendering of
EXISTING records, not by the schema bump itself). Same queries as before,
byte for byte (each file's own header query, all 13 triplets re-rendered
into scratch first, the diff CLASSIFIED per file, then copied in). The
diff on every file is exactly: the version line (`v8` → `v9`); two new
legend lines (the `trial-agreement policy` bullet and the `status rule:`
line — every committed report reads `v1.1-1.3 X13 (both samples quiet)
on N record(s)`, since no v1.4 record exists in `store/` yet); each
header record line gaining `— agreement: n/a (v1.x)` (the record's own
schema version; the reporter never invents a block for a pre-1.4 record)
and, on the records whose AFTER sample failed under the old gate, the
unconditional `; after: load1 … / occ …%` clause (R5′ — the demoted
instrument kept visible); and, in the `.tsv` files, the header comment's
three new fields plus one `record` row per included record. NO number,
ranking, verdict or legend fact moved — 39 files, zero unexplained
lines under the classifier (`test_v13_record_still_renders` holds the
same rule over the fixture store). The first report with a real
`agreement: agree (… 5 trials)` line, a `measured@1.3`/`measured@1.4`
marker or an `inconclusive-spread` bullet will be the first v1.4
window's.

**[B19] scope addition (2026-08-30) regenerated every report below
against reporter `v8 (2026-08-30)`.** Same queries as before, with three
of them CHANGED (below): the abi-11 `K=<unroll_k>/<why>` and
`caps=<max_emit_code_bytes>/<max_emit_bytes>` legend clauses + note
(`pcrecbench/report.py`'s "[B19] SCOPE ADDITION" docstring paragraph)
render on any VM artifact's legend line whose record carries those
pairs — every `36d5963`-pinned pcrec record does (abi 11), so the three
sets built on it (`2026-08-30-bounded-0.1-*-first-sample-36d5963`,
`2026-08-29-*-repin-36d5963`) gain the clauses; the `8da6120` /
`692c2e8` / `35e1ab1` sets (abi 2/3/8, before those stamps existed) only
gain the version-line bump. **Also from this wave: every report's
`record source: store/index.tsv (N candidate file(s))` count moved with
the store's growth since it was last rendered — this is NOT a
reporter-version effect (verified across the store's whole regeneration
history: this count has moved on every prior wave while `records
included` never has) and is not itself grounds to reject a diff.**
Separately, the store gaining the abi-12 `96e44c2` AFTER sample the same
day ([B19], commit 33ee50f, index 68) broke the "no bound needed"/loose
`--until` premise of three queries whose filters do not exclude an
unpinned pcre2 record or a same-config pcrec record newer than their
sample window — `2026-08-29-email-specimen-0.2-*-repin-36d5963`,
`2026-08-29-loglines-0.1-*-repin-36d5963` (previously no date bound at
all) and `2026-08-30-bounded-0.1-*-first-sample-36d5963` (previously
`--until 2026-08-30T12:00:00Z`, which fell INSIDE the AFTER window and
admitted one partial record). All three now carry `--until
2026-08-30T11:00:00Z` (manager ruling, 2026-08-30): see each entry below
and the new rule paragraph near the `--until` explanation. With that
bound in place, the K=/caps= clauses and the version/candidate-count
lines are the ONLY diff each of the three shows against its previously
committed content — no record, ranking, or number moved.

**[B12] R10 (2026-08-29) regenerated every report below against reporter
`v7 (2026-08-29)`.** Same queries, same records — one ruling, and it
changes the rendering of exactly one file's RANKING content: a
did-not-compile compile cell now prints `not ranked: <testee> —
did-not-compile (<diagnostic>)` under its ranking table instead of
vanishing from the ranking silently (see `pcrecbench/report.py`'s
module docstring, "THE [B12] RULING"). Of the four report sets here,
only `2026-08-28-loglines-0.1-budu-ryzen1600-first-sample-35e1ab1.md`
(and its `.subject-grain.md`; the `.tsv` gets a `did_not_compile`
section row) has a live did-not-compile cell to show:
`level-context`/`pcrec-auto` did not compile at pcrec 35e1ab1, and its
`short-subject-search` and `large-subject-throughput` ranking tables now
each carry the bullet, naming the diagnostic verbatim ("pattern too
complex for the DFA engine (>32000 states; try --engine=vm) (pattern
offset 0)"). Every other committed report's only diff against its `v6`
render is the version-line bump (`reporter: v6 (2026-08-28)` →
`reporter: v7 (2026-08-29)`) — no did-not-compile cell exists in
email-specimen's records at any pin measured so far.

Every report below was regenerated at [B16] R9 (2026-08-28, later the
same day) against reporter `v6 (2026-08-28)` — the per-subject
sub-table keyed on the regime; and the two `-repin-692c2e8` files' query
gained `--version 0.1` when `email-specimen@0.2` records entered the
store (the SAME records as before: the version filter now says what the
store's contents used to imply). Before that, both sample sets were
regenerated at [B16] against reporter `v5 (2026-08-28)` (previously at [B14] against `v3` then `v4`
the same day — see the KB-2 note below; and at [B9] against `v2`): each
regeneration means these files no longer diff byte-identical against the
previous reporter's versions, but each still answers the SAME query as
before — see `pcrecbench/report.py`'s module docstring for the full
ruling list ([B9]'s R1-R9, [B14]'s R1-R10, [B16]'s R1-R8, [B12]'s R10 —
the ruling sets share numbers by coincidence of separate `R1..`
sequences, not by design; read each set's own dated section) and the
notes below for what each wave changed in these files specifically.

**RULE, added 2026-08-30 (the [B19] scope-addition wave, above):** every
report committed here from this date on is rendered with an EXPLICIT
`--until` (or a `--since`/`--until` pair) at render time, never a bare
unbounded query — the next measurement window always adds newer records
under the unpinned pcre2 testee_ids (and, as of [B19], under a matching
pcrec `engine`+`config` too), so an unbounded or loosely-bounded query
silently drifts out from under a report's own committed name the moment
the store grows again.

- `2026-08-25-email-specimen-0.1-budu-ryzen1600.md` — the FIRST
  PRODUCTION SAMPLE: email-specimen@0.1 × {pcre2-interp, pcre2-jit,
  pcrec-auto, pcrec-nocaps, pcrec-vm} at pin 8da6120, 5 trials, pinned
  to CPU 11, in a quiet window coordinated with the pcrec manager
  session (02:22-02:56 EDT); set grain. `.subject-grain.md` the
  per-subject drill-down; `.tsv` the machine-readable form. Query:
  `--subbench email-specimen --until 2026-08-25T07:00:00Z` — the
  `--until` bound is NOW REQUIRED to reproduce this exact 5-record
  snapshot ([B9] regeneration note): the store has since grown past this
  sample's original "only 5 records exist yet" window (the re-pin
  sample below, and OD-B15's newest-wins dedup, would otherwise pull
  later records of the SAME testee_ids into what this file's name
  claims is the pin-8da6120-only sample).
- `2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.md` — the
  RE-PIN SAMPLE ([B8]): the same six cells re-measured after pcrec's
  re-pin to `692c2e8` (the caller-provided frame-buffer testees added,
  `pcrec-vm-in` measured), alongside the surviving pin-8da6120 records
  and the store's own re-measurements: a second libpcre2-interp run
  (17:34, under load) landed `inconclusive-load` and, per OD-B15's
  AMENDED dedup rule ([B9], 2026-08-25 — a newer non-measured record is
  not evidence against an older measured one and does not supersede it),
  does NOT replace the original 06:22 measured record — it is listed
  under the header as "newer, not measured" instead, and the 06:22
  record is what the ranking tables actually use; a second libpcre2-jit
  run (17:41) DID land `measured`, so it supersedes the first jit record
  under the ordinary newest-measured-wins rule (see the header's
  "superseded records" line). Query: `--subbench email-specimen` (no
  bound needed: every record this sample was drawn from already existed
  when it was first generated). `.subject-grain.md` the per-subject
  drill-down; `.tsv` the machine-readable form. Read alongside
  `docs/dev/feedback_pcrecdev1_2026-08-25-repin.md` (the pcrec manager's
  reading that became [B9]'s R1-R9 rulings) and
  `docs/dev/feedback_pcrecdev1_2026-08-25.md`.

**[B14] (2026-08-25) regenerated both sample sets against reporter `v3
(2026-08-25)`** — docs/dev/feedback_pcrecdev1_2026-08-25-repin-v2.md (the
pcrec manager's second reading of the v2 rendering) was the spec, rulings
R1-R10 (`pcrecbench/report.py`'s module docstring has the full list; the
summary that matters for reading these files):

- a compile-cost table's per-testee CONSTANT facts (`engine`, `entry`,
  `prefilter`, `vm_rungs`, and the buffer/frame facts below) moved OFF
  the table into a one-line-per-testee LEGEND printed above it (R8) — a
  reader now checks the legend once per testee, not once per row;
- a plain-entry compile row states the STAMPED DEFAULT capacity it
  actually runs on (`buffers=2048/3072 (stamped default)`), not a blank
  (R1); the legend's `buffers`/`frame` facts read `n/s` (nothing stamped
  at that pin) or `0 (DFA)` (stamped, and zero because a DFA artifact
  takes no buffers) — never a bare `-`/`0` standing for either (R4);
- `jitter` is a computed ratio (`stddev/median`) or `timer-floor` under a
  20-microsecond floor, not a boolean, and the column disappears from a
  table where every row comes back empty rather than printing a wall of
  blanks (R5);
- every compile-cost row carries its `artifact bytes` (R7);
- a `large-subject-throughput` ranking row carries `ns/byte` beside
  `ns/call`, and a set of <=3 subjects (every throughput cell today)
  gets its own per-subject sub-table under the ranking row (R2);
- a `match-compliance` ranking group states `matches: m/n` when
  derivable, `matches: n/s` otherwise (R3 — see the KB-2 correction
  below: as of `v4` it is ALWAYS `n/s` in these files, honestly, not a
  fabricated fraction);
- a cross-pin `Δ detail` line names `worst now` and, only when it is a
  DIFFERENT subject, `largest Δ` beside it, instead of one ambiguous
  "worst subject" (R6);
- the Query header's superseded-record list collapsed to one summary
  line (`--all-records` still lists every id) (R8).

R9 (a `role: floor` pattern's short-subject-search table retitled a
per-call overhead CONTROL, with a `floor ns` figure on every other
pattern's row) reads `floor: n/a` unchanged in these files — bench/email
gained a real floor pattern in its SOURCE the same day (lane b15floor,
schema v1.3), but no MEASURED record of it exists in `store/` yet, so
this regeneration's own data has nothing to show. The wiring itself is
proven two ways in `pcrecbench/tests/test_report.py`: against hand-built
records (`test_floor_pattern_r9`) and, now that v1.3 makes `patterns[].
role` schema-legal, against a REAL schema-valid fixture file
(`test_floor_pattern_fixture_r9`, `pcrecbench/tests/fixtures/
floor_pattern/`) — ready for the day a real floor-pattern measurement
lands here.

**KB-2 correction (same day, before final merge; docs/dev/
known_issues.md; manager steer 2026-08-25): R3's `matches: m/n` moved
from "read `bench/email/expectations.tsv` live" to "derive from the
record alone."** The reporter must work from records alone — a record
measured on another box, or against a later sub-bench version, has no
sidecar checkout beside it to read. The record itself turns out to carry
no field this can be derived from either, for the common case:
`pcrecbench.harness.outcome_for` sets `observed = None` on a
`matched-as-expected` row (checked against these very files' own
records), so `pcrecbench.report._matching_subject_count` now always
returns `None` and every `match-compliance` group here reads `matches:
n/s`, pointing at KB-2 rather than a fabricated fraction. `report.py` no
longer imports `pcrecbench.subbench` at all. `REPORTER_VERSION` bumped
`v3` → `v4` the same day for this (its own rule: bump whenever rendering
changes).

**[B16] (2026-08-28) regenerated both sample sets against reporter `v5
(2026-08-28)`.** The re-pin to pcrec 35e1ab1 (abi 8) is the wave; the
reporter half of it is pcrec's inbox I-7 §3 and §5, and FOUR of its
rulings change what these committed files say about records that have
not moved. No number moved — the records are the same records — but two
verdicts and two annotations did:

- **the ×13.45 is gone, and what replaced it is the finding.** `factored`
  / `short-subject-search` / `pcrec-auto` read `faster ×13.45` at `v4`
  across 8da6120 → 692c2e8. It now reads `selection changed (vm → dfa)`
  ([B16] R4): at 8da6120 `auto` selected the VM for `factored` (its rows
  gave up with `-2:PCREC_ERR_STEPS`, a code only the VM can produce) and
  at 692c2e8 it selects the DFA. The ×13.45 was two engines, not one
  engine getting faster — pcrec I-7 §3 caught it by hand; the reporter
  catches it now. The same substitution happens in three more cells
  (`factored`'s throughput and compliance rows), where the verdict reads
  `selection changed (vm → dfa); now measured (was: gave-up)`: a
  selection change EXPLAINS a cell that used to be excluded, so both
  facts print, and only the faster/slower RATIO is suppressed.
- **the legend is scoped per (pattern, form) where a testee's cells
  disagree** ([B16] R3). `pcrec_8da6120_auto-caps-simdna` now gets one
  legend line per cell, because at that pin it compiled `orig` to a DFA
  artifact and `factored` to a VM one — the `v4` legend printed
  `engine=dfa` for the whole testee, which was `orig`'s measured value
  wearing `factored`'s name. Every testee whose cells agree still gets
  ONE line, with `(identical on all N (pattern, form) cells)` under it.
- **`jitter` gained `(max is trial 1)`** ([B16] R6) wherever the cell's
  maximum is its first trial — including the eager-JIT rows whose
  0.556/0.645 jitter was I-7 §5's example of a first-trial warm-up that
  a bare ratio could not distinguish from noise.
- **a `set composition` column** ([B16] R7) flags a set-grain ratio that
  is really one subject. In these files it fires on
  `libpcre2_10.46_interp-caps-simdna`'s two throughput rows:
  `t-a-valid-addrs` is 99.9 % of that set, so interp's "3.15× slower
  than JIT" is a ratio of that one subject — 144× FASTER on the other
  two, which the per-subject sub-table under the row shows.

The DFA mechanism columns ([B16] R1) and the fast-tier clause (R2) are
present in these files but have nothing to show: every record here is
from pcrec abi 2 or 3, before those stamps existed, so the legend reads
`dfa: n/s (pcrec abi 3, before the DFA stamps landed at abi 4)` and
`fast tier=n/a (pcrec abi 3: no tier existed before abi 5)`. Which
ABSENCE a missing stamp is gets decided from the record's own `abi`
pair, never guessed — the first record measured at the 35e1ab1 pin will
show the values instead.

**A note on what [B9]'s own rulings changed in this store's numbers**:
applying R1 (OD-B14: a non-`measured` row is excluded from ranking by
default) to the re-pin sample means two of the four `692c2e8` pcrec
testees (`auto-caps`, `auto-nocaps`) are `inconclusive-load` and have NO
measured record at all yet, so they are UNRANKED in every table (see
their "not ranked" lines) unless `--include-unmeasured` is passed — a
re-measure of those two on a quiet box would rank them. The DEFAULT
baseline testee (`libpcre2 engine_mode=interp`, named in every table
title) IS ranked, using its original 06:22 measured record: R2/OD-B15
was AMENDED (manager, 2026-08-25, before this lane's merge) specifically
because the first cut of the dedup rule — newest record wins regardless
of status — would have let interp's later `inconclusive-load` re-measure
silently displace its earlier measured one and vanish from every table's
baseline; the amended rule (newest MEASURED record wins; a newer
non-measured one is listed separately, never treated as evidence against
an older measured one) restores it.

- `2026-08-28-email-specimen-0.2-budu-ryzen1600-repin-35e1ab1.md` — the
  [B16] re-pin sample at pcrec **35e1ab1** (abi 8) on `email-specimen@0.2`
  (five throughput subjects: [B17]'s two non-periodic prose subjects
  beside the periodic three), six cells `measured` 2026-08-28 10:16-10:59
  EDT, `--trials 5`, quiet window, reporter v7 (this entry's own "v5" had
  drifted through the v6/[B16] R9 regeneration; corrected here at
  [B12] R10, no content beyond the version line changed for this file).
  Query:
  `report --subbench email-specimen --version 0.2 --until
  2026-08-29T00:00:00Z --format md` (the `--until` bound added
  2026-08-29 when the 36d5963 records entered the store: the pcre2
  testee_ids carry no pin, so newest-measured-wins would otherwise pull
  that day's pcre2 records into this file). The
  prediction ledger against the 692c2e8 records (journal, third session
  part 5) is read per SUBJECT because the throughput set grew — a 0.1
  set sum and a 0.2 set sum are different cells. `.subject-grain.md`
  (`--grain subject`) carries the periodic-vs-prose rows that answer
  pcrec's I-10; `.tsv` the same set-grain query as TSV.

- `2026-08-30-bounded-0.1-budu-ryzen1600-first-sample-36d5963.md` — the
  FIRST SAMPLE of sub-bench #4, `bench/bounded@0.1` ([B11.4]), at pcrec
  **36d5963** (abi 11): six cells `measured` — three in the window of
  2026-08-29/30 23:21-01:21 EDT (pcre2-interp, pcrec-nocaps, pcrec-vm; the
  1-s occupancy instrument) and three RE-RUN 05:22-06:17 EDT under BD7
  (pcre2-jit, pcrec-auto, pcrec-vm-in; their first runs are in the store
  as `inconclusive-load` history, OD-B12 → BD7 → [B20]); `--trials 5`,
  quiet windows, reporter v8. Query: `report --subbench bounded --version
  0.1 --until 2026-08-30T11:00:00Z --format md` (the `--until` bound
  present from the first render: the pcre2 testee_ids carry no pin. The
  bound MOVED 12:00Z → 11:00Z at the v8 regeneration, 2026-08-30, manager
  ruling: the original 12:00Z guess was set before the [B19] AFTER
  window's start time was known and landed INSIDE that window
  (11:12Z-14:45Z), admitting one `pcrec_96e44c2_auto-caps-simdna` record
  — measured 11:54:09Z — as a partial, inconsistent contamination; every
  36d5963 record is ≤ 2026-08-30T10:00:09Z, so 11:00Z is the shared
  boundary with the AFTER reports' `--since 2026-08-30T11:00:00Z` below).
  `.subject-grain.md` (`--grain subject`) and `.tsv` the same query. This
  is the [OPT-4] BEFORE (inbox I-18 (i)). Read beside
  `bench/bounded/NOTES.md`'s predictions and `oracle_limits.tsv`: the
  class ladder's `cls-upto-65535` is `did-not-compile` under both
  `pcrec-auto` and `pcrec-nocaps` (`pattern too large (NFA exceeds 131072
  states)` — the NFA cap, at every pin), while `cls-upto-32768` COMPILED
  as a plain-VM artifact (no prefilter, cursor rung) — the set's predicted
  abi-11 size-cap refusal at that rung did not fire; the ctx ladder and
  `cls-upto-16384`'s whole-subject form are VM artifacts (the DFA state
  cap in the engine role), their `plain` forms DFA. READING RULE (inbox I-20, after O-9 ask (ii)): the
  `dfa_match=search-filter` rows at the large counts are the documented
  [ENG-ABS] ceiling (`PCREC_ANCHORED_MAX_STATES` = 4096, no runtime
  raise), and the whole-subject `(?:BODY)\z` spelling HALVES the
  reachable `{0,n}` count (crossover 2047→2048 vs plain 4095→4096) —
  a rung's `plain` and `whole-subject` rows are DIFFERENT MACHINES, not
  the same pattern twice; the reporter's form caveat (pcrec [OS-4]) is
  literal here.

- `2026-08-28-loglines-0.1-budu-ryzen1600-first-sample-35e1ab1.md` — the
  FIRST SAMPLE of sub-bench #2, `bench/loglines@0.1` ([B11.1]), at pcrec
  **35e1ab1** (abi 8): six cells `measured` 2026-08-28 11:00-11:50 EDT,
  `--trials 5`, quiet window, reporter v7 (regenerated at [B12] R10; see
  above). Query: `report --subbench
  loglines --version 0.1 --until 2026-08-29T00:00:00Z --format md` (the
  `--until` bound added 2026-08-29, same reason as the entry above; the
  R10 bullets show that `pcrec-nocaps` did not compile `level-context`
  at 35e1ab1 either). This is the report pcrec's
  [OPT-5] was chartered to be decided on (journal third session part 6;
  outbox O-7 items 4-6): read the search-band ranking beside
  `bench/loglines/pattern_facts.tsv`'s presence counts; `pcrec-auto`
  has NO `level-context` rows because that artifact did not compile
  (the compile-cost table says `did-not-compile=1`; the ranking's
  `short-subject-search` and `large-subject-throughput` tables each carry
  `not ranked: \`pcrec_35e1ab1_auto-caps-simdna\` — did-not-compile
  (pattern too complex for the DFA engine (>32000 states; try
  --engine=vm) (pattern offset 0))` since [B12] R10). `.subject-grain.md`
  carries the 16 KB-1 MB sweep rows per flavour (fail / hit / syslog);
  `.tsv` the set-grain query.

- `2026-08-29-email-specimen-0.2-budu-ryzen1600-repin-36d5963.md` — the
  [B18] re-pin sample at pcrec **36d5963** (abi 11; inbox I-15/I-16/I-17
  absorbed as one adapter change) on `email-specimen@0.2`: six cells
  `measured` 2026-08-29 15:06-15:43 EDT plus two re-runs 16:39-16:55
  (the first `pcre2-interp` and `pcrec-vm` records of the day landed
  `inconclusive-load` — journal fourth session part 2 — and stay in the
  store as history; the report's newest-measured-wins rule picks the
  re-runs), `--trials 5`, quiet window with BOTH manager sessions idle,
  reporter v8. Query: `report --subbench email-specimen --version 0.2
  --until 2026-08-30T11:00:00Z --format md` — 10 records: the four
  35e1ab1 pcrec testees (the cross-pin Δ baseline), the four 36d5963
  ones, and the newest pcre2 pair. The `--until` bound was ADDED at the
  v8 regeneration (2026-08-30): the query originally needed none ("every
  record already existed when first generated"), but the [B19] AFTER
  sample landed in the store the same day (index 68) under the same
  unpinned pcre2 testee_ids and the same `email-specimen@0.2` filter, so
  a bare re-run now pulls in newer pcre2 records and four
  `pcrec_96e44c2_*` rows — the same boundary as bounded's entry above and
  the AFTER reports' `--since` below. This is the [ENG-ABS] ledger (inbox
  I-16: the `match` regime's DFA/VM ratios; the search rows are the flat
  control) — outbox O-8.
  `.subject-grain.md` (`--grain subject`) carries the per-subject match
  rows the ledger is read on; `.tsv` the set-grain query.
- `2026-08-29-loglines-0.1-budu-ryzen1600-repin-36d5963.md` — the [B18]
  re-pin sample at pcrec **36d5963** on `loglines@0.1`: six cells
  `measured` 15:43-16:37 EDT plus one re-run (`pcrec-nocaps`, 16:55),
  same protocol, reporter v8. Query: `report --subbench loglines
  --version 0.1 --until 2026-08-30T11:00:00Z --format md` — 10 records as
  above. The `--until` bound was ADDED at the v8 regeneration
  (2026-08-30), same reason and same boundary as the email-specimen
  0.2/36d5963 entry above (the [B19] AFTER sample landed in the store the
  same day under the same unpinned pcre2 testee_ids). This is the
  [OPT-K] ledger (inbox I-15: uuid / iso-ts / stack-frame the exercising
  rows, ipv4 / hex32-id / http-5xx the controls) and Frank's [SEL-1] row
  (`level-context` under `pcrec-auto`, a VM artifact now, vs pcre2-jit)
  — outbox O-8. `.subject-grain.md` carries the 16 KB-1 MB sweep per
  flavour; `.tsv` the set-grain query.

- `2026-08-30-{bounded-0.1,email-specimen-0.2,loglines-0.1}-budu-ryzen1600-repin-96e44c2.md` —
  the REPIN-FORM renders of the abi-12 AFTER sample: the same three sets
  queried with BOTH pins' records in one query, `report --subbench <set>
  --version <v> --since 2026-08-29T00:00:00Z --until 2026-08-30T15:00:00Z
  --format md` (10 records included per set: the four `pcrec_36d5963_*`
  and four `pcrec_96e44c2_*` ids plus the two pcre2 ids deduped
  newest-wins; the superseded 36d5963 pcre2 and inconclusive records
  listed under OD-B15), so the reporter's R8 `Δ vs previous version`
  column FIRES on every pcrec row (matched by testee-id root across the
  pins) and carries the spread verdicts the abi-12 ledger
  (docs/dev/ledgers/2026-08-30-abi12-after-96e44c2.md) had to compute by
  hand — its §6(a) is the reason these files exist. The `-after-96e44c2`
  files above stay the clean single-pin sample; read the two families
  side by side. `.subject-grain.md` and `.tsv` the same query (the TSV
  carries no Δ column). Rendered 2026-08-30 13:24-13:33 EDT by the
  manager on the merged v8 reporter, untimed, beside pcrecdev1's battery.
- `2026-08-30-bounded-0.1-budu-ryzen1600-after-96e44c2.md` — the [OPT-4]
  AFTER sample (inbox I-18 (i)) on `bench/bounded@0.1` at pcrec
  **96e44c2** (abi 12, the [B19] re-pin): six cells `measured` 07:12-10:45
  EDT 2026-08-30 (window: both managers idle, BD7's 5-s occupancy gate,
  18/18 cells across the three sets on attempt 1, zero retries), `--trials
  5`, reporter v8. Query: `report --subbench bounded --version 0.1
  --since 2026-08-30T11:00:00Z --until 2026-08-30T15:00:00Z --format md`
  (the `--until` ADDED at [B26] (c), 2026-09-02 — see that wave's paragraph
  at the top: a bare `--since` let the 1989c62 night's records into this
  file) — 6 records: the two
  libpcre2 baseline re-runs plus the four `pcrec_96e44c2_*` testees, none
  of the 36d5963 BEFORE records (the `--since` bound is the mirror of the
  first-sample entry's `--until` above — the two files share the
  2026-08-30T11:00:00Z boundary because the pcre2 testee_ids carry no
  pin). Read against `docs/dev/ledgers/2026-08-30-bounded-0.1-first-sample-36d5963.md`
  §6 (the BEFORE ledger's predictions) and the first-sample entry above:
  `cls-upto-65535` is still `did-not-compile` under both `auto` and
  `nocaps` (NFA cap, unchanged pin-to-pin). `.subject-grain.md`
  (`--grain subject`) and `.tsv` the same query.
- `2026-08-30-email-specimen-0.2-budu-ryzen1600-after-96e44c2.md` — the
  [OPT-4] AFTER sample on `email-specimen@0.2` at pcrec **96e44c2**,
  same window and protocol as the bounded entry above, reporter v8.
  Query: `report --subbench email-specimen --version 0.2 --since
  2026-08-30T11:00:00Z --until 2026-08-30T15:00:00Z --format md` (the
  `--until` ADDED at [B26] (c), 2026-09-02 — a bare `--since` had let the
  1989c62 night's four pcrec arms and both newer pcre2 records into this
  file; see that wave's paragraph at the top) — 6 records, same shape as bounded's
  (two libpcre2 + four `pcrec_96e44c2_*`). Read against the
  2026-08-29 `-repin-36d5963` report above (the [ENG-ABS] ledger) for the
  pin-to-pin comparison: no `sel=collapsed-prefilter (DFA fallback
  tripped)` cell fires in this set (only the legend NOTE mentions the
  bucket, since a note prints whenever any `sel=` clause appears in the
  table, matching the entry above's census — every `email-specimen`
  artifact here is `sel=forced` or `sel=selected`, not a fallback).
  `.subject-grain.md` (`--grain subject`) and `.tsv` the same query.
- `2026-08-30-loglines-0.1-budu-ryzen1600-after-96e44c2.md` — the
  [OPT-4] AFTER sample on `loglines@0.1` at pcrec **96e44c2**, same
  window and protocol, reporter v8. Query: `report --subbench loglines
  --version 0.1 --since 2026-08-30T11:00:00Z --until 2026-08-30T15:00:00Z
  --format md` (the `--until` ADDED at [B26] (c)) — 6 records,
  same shape. Read against the 2026-08-29 `-repin-36d5963` report above
  (the [OPT-K] ledger and Frank's [SEL-1] row): `level-context` under
  both `pcrec-auto` and `pcrec-nocaps` still selects the VM and now shows
  it structurally — `sel=collapsed-prefilter (DFA fallback tripped)`,
  `lang=count-collapsed (dfa overflow retry, exact nfa 462/463)` — the
  fact [B18]'s note called "readable only as prose" (pcrecbench/CLAUDE.md
  "THE [SEL-1] FALLBACK") is now a stamped, queryable field via [B19].
  `.subject-grain.md` (`--grain subject`) carries the 16 KB-1 MB sweep
  per flavour; `.tsv` the set-grain query.

- `2026-08-31-bounded-0.2-budu-ryzen1600-first-sample-263b013.md` — the
  [B22] WINDOW's FIRST SAMPLE of `bench/bounded@0.2` at pcrec **263b013**
  (abi 12 unchanged; inbox I-21-correction/I-22/I-25): six cells
  14:43-17:04 EDT (two libpcre2 baseline runs plus `pcrec_263b013_auto`/
  `auto-nocaps`/`vm`/`vm-in`), reporter v10. Query: `report --subbench
  bounded --version 0.2 --until 2026-09-01T00:00:00Z --format md` — 6
  records (bounded@0.2 has no earlier sample at any pin, so this bound is
  generous headroom, not a tight cut; the never-pool rule,
  bench/bounded/NOTES.md, means bounded@0.1 records never enter this
  query's set sums regardless of bound). `pcrec-vm-in`'s FIRST run
  (16:42:45Z) is the schema v1.4 wave's first production
  `inconclusive-spread` record (store commit 67ff0c2's own journal entry
  names it so): trial agreement `disagree` on 1 of 90 groups (13 of 1950
  rows), worst group `ctx-greedy-256` / `match-compliance` /
  `whole-subject` (d=13 of n=30); `scripts/run_window.sh`'s one-retry
  rule re-measured it (17:04:25Z, `agree`), which is the record this
  report ranks — the first run is listed under the header as superseded
  history (OD-B15), not pooled into any number. Compile cost:
  `cls-upto-65535` is still `did-not-compile` under both `auto` and
  `nocaps` (NFA cap, unchanged pin-to-pin, same diagnostic as every prior
  pin). Mechanism legend: 8 `sel=declined-nullable (DFA fallback
  tripped)` cells fire (both `auto`/`auto-nocaps`, `cls-lazy-16384` and
  `cls-upto-16384`'s `whole-subject` forms, `cls-upto-32768`'s `plain`
  and `whole-subject` forms) — the new [B22] token (inbox I-25:
  `RX_ENGINE_SEL`'s nullable-collapsed decline, `-fprefilter-collapse`
  DECLINED rather than shipping a rescue on a nullable collapsed
  language); no `sel=size-cap-retry` cell fires in this set. `.tsv` gets
  the same 6 records; `.subject-grain.md` the per-subject drill-down.

- `2026-08-31-loglines-0.1-budu-ryzen1600-after-263b013.md` — the [B22]
  WINDOW's two fresh cells on `loglines@0.1` at pcrec **263b013**:
  `pcrec_263b013_auto`/`vm` measured 17:51-18:00 EDT, reporter v10.
  Query: `report --subbench loglines --version 0.1 --until
  2026-09-01T00:00:00Z --format md`. NAMED "AFTER" BY THE SAME PATTERN AS
  THE 96e44c2 FILES ABOVE, BUT NOT THE SAME SHAPE — read this note before
  the numbers: those files' `--since` bound worked because that window
  remeasured all SIX loglines arms (2 pcre2 + 4 pcrec) fresh, so one
  bound cleanly cut off every older record. Today's window remeasured
  only 2 of the 6 arms (`auto`, `vm` — `nocaps`/`vm-in` were not rerun,
  and neither was pcre2). Dedup keys on the record's literal `testee_id`
  (`pcrecbench/report.py`'s `dup_groups`), which embeds the pin
  (`pcrec_263b013_...` vs `pcrec_96e44c2_...` etc.) — it never supersedes
  ACROSS pins. pcre2's newest record (2026-08-30 13:54-14:03Z) is
  chronologically OLDER than `pcrec_96e44c2`'s (2026-08-30 14:11-14:36Z),
  so no single `--since`/`--until` range admits "pcre2 08-30 +
  pcrec_263b013 08-31" while excluding `pcrec_96e44c2`/`36d5963`/
  `35e1ab1` — that needs two disjoint ranges, which the reporter's
  filters (a single AND'd range; `--where` is also AND-only) do not
  express. Rather than guess at a narrower query or hand-edit the
  rendering, this file is the literal bare `--until` the window brief
  asked for: **16 records** — the 2 newest pcre2 plus all FOUR surviving
  pcrec pins' testees (35e1ab1 ×4, 36d5963 ×4, 96e44c2 ×4, 263b013 ×2;
  `pcrec_36d5963_auto-nocaps`'s first run superseded by its
  20:55:45Z remeasure, OD-B15). This gives the reporter's R8 `Δ vs
  previous version` column real content (matched by testee-id root
  across all four pins, not just the newest two) alongside the newest
  pcre2 comparison arm the window brief asked for — read it as a
  four-pin history view, closer in shape to the `-repin-` files above
  than to the clean single-pin `-after-96e44c2` files. `level-context`
  under `pcrec_263b013_auto` still reads `sel=collapsed-prefilter (DFA
  fallback tripped)`, `lang=count-collapsed (dfa overflow retry, exact
  nfa 462/463)` — unchanged pin-to-pin, the count-collapsed rescue is
  still the KEEP case here (I-21-correction), distinct from bounded's
  DECLINE cases above. `level-context`/`pcrec_35e1ab1_auto*` is still
  `did-not-compile` (the abi-8 pin, before the [SEL-1] fallback landed;
  unchanged from its own first-sample entry). `.subject-grain.md`
  (`--grain subject`) carries the 16 KB-1 MB sweep per flavour;
  `.tsv` the same query (no Δ column, as the `-repin-` `.tsv`s above).

- `2026-08-31-bounded-0.2-budu-ryzen1600-after-a7e0bdf.md` — the [B25]
  WINDOW's ACCEPTANCE AFTER for `bench/bounded@0.2` at pcrec **a7e0bdf**
  (abi 13; inbox I-27, [OPT-5] STEP 1 shipped): the four pcrec arms
  (`auto`/`auto-nocaps`/`vm`/`vm-in`) measured 21:46-23:15 EDT (Aug 31),
  reporter v10 (unchanged — this lane made NO reporter code changes;
  [B25]'s commits touch only the pcrec adapter/testees/docs). Query:
  `report --subbench bounded --version 0.2 --until 2026-09-02T00:00:00Z
  --format md` — **10 records included** (2 pcre2 + 4
  `pcrec_263b013_*` + 4 `pcrec_a7e0bdf_*`), **1 superseded** listed under
  the header (`pcrec_263b013_vm-in-caps-simdna`'s FIRST run, the
  `inconclusive-spread` record from [B22]'s window — OD-B15 dedup keeps
  its 17:04:25Z retry instead), **11 records total** named in the file.
  DELIBERATELY CROSS-PIN, same shape as KB-5's finding
  (docs/dev/known_issues.md) even though this window is a FULL re-measure
  of all four pcrec arms rather than a partial one: the bare `--until`
  admits the surviving `pcrec_263b013_*` rows beside the fresh
  `pcrec_a7e0bdf_*` ones because dedup keys on the literal `testee_id`,
  which embeds the pin — a newer pin's rows never supersede an older
  pin's rows of the same engine config, by design (KB-5's "never
  supersedes ACROSS pins"). That is the POINT here, not an accident: the
  R8 `Δ vs previous version` column firing `pcrec_a7e0bdf_* vs
  pcrec_263b013_*` (matched by testee-id root) IS the [OPT-5] acceptance
  table I-27 (2) asked for, so no narrower `--testee`-style filter (KB-5's
  candidate fix, still unbuilt) is wanted even though one would apply
  cleanly this time (only two pins survive in this set, unlike loglines'
  four).

  R8 verdicts, `large-subject-throughput` set-grain rows: mixed —
  `auto`/`auto-nocaps` read `faster ×3.62` on `cls-atleast-4096` and
  `faster ×1.95`-`×1.97` on most `cls-upto-*` rungs, but `unchanged
  (within spread)` or a small `faster ×1.0x`/`slower ×1.0x` on `vm`/
  `vm-in` rows throughout (expected: [OPT-5] STEP 1 is a DFA-side
  emission change, not a VM change, and `auto`/`auto-nocaps` select the
  DFA on these rungs). Per-subject drill-down (the falsifiable frame,
  I-27 (2): letters `auto÷vm` drops to ~1.9-2.1 at every rung, digits
  within noise): computed directly from the `large-subject-throughput`
  per-subject sub-tables (`auto-caps` / `vm-caps`, a7e0bdf) —
  `t-letters-*` gives 1.76-1.79× at rungs 64/128, climbing to 1.97-2.00×
  at rungs 1024-16384 (INSIDE the predicted band at the larger rungs,
  below it at the two smallest), 2.11-2.72× on `cls-atleast-4096`
  (ABOVE the band — flagged, not silently averaged in), and COLLAPSES to
  ~1.00× at `cls-upto-32768` (OVERSHOOTS the prediction: `auto` and `vm`
  converge because `cls-upto-32768` is the [B22] `declined-nullable`
  rung — the DFA fallback declines and `auto` itself runs the VM, so
  `auto÷vm` measures the ~1.08× entry-cost gap, not the STEP-1 win).
  `t-digits-*` sits at `auto÷vm` ≈ 0.60 (auto ~1.67× FASTER than vm, not
  "noise-flat" — digits was never the collapse target, so this ratio is
  pin-INVARIANT: `pcrec_263b013`'s own digits ratios match to three
  figures) — WITH NO EXCEPTION: the `cls-upto-8192`
  "inversion" this entry originally flagged (≈1.77 digits / ≈0.13
  letters) was REFUTED by the ledger lane the same night
  (docs/dev/ledgers/2026-08-31-opt5-step1-acceptance-a7e0bdf.md §4,
  from the records): the rung's true ratios are letters
  1.967/1.993/2.000 and digits 0.601/0.602, exactly in line with its
  neighbors. The flagged 1.77 was the `vs best` CELL of the a7e0bdf
  vm row in a digits sub-table (the digits sub-tables are the only
  ones the OLD pin tops, so `vs best` there compares against
  263b013-auto and reads inverted), and the 0.13 was a CROSS-SUBJECT
  pairing (letters auto ÷ DIGITS vm). READER'S CAVEAT, general: in
  the per-subject sub-tables, `vs best` inverts VISUALLY wherever a
  superseded pin's row ranks first — read `auto÷vm` from same-pin
  same-subject rows, never from `vs best` across pins.
  Compile cost: `cls-upto-65535` is still `did-not-compile` under both
  `auto` and `auto-nocaps` at a7e0bdf (`pattern too large (NFA exceeds
  131072 states)`, byte-identical diagnostic to every prior pin — the NFA
  cap is untouched by [OPT-5]). Mechanism legend: the `sel=` token set on
  every `pcrec_a7e0bdf_*` row is exactly the four tokens already in the
  legend at 263b013 (`selected`, `forced`, `collapsed-prefilter (DFA
  fallback tripped)`, `declined-nullable (DFA fallback tripped)`) — no
  new `sel=` value fires. The new abi-13 `dfa_scan_edge` stamp (pcrec
  I-27's `RX_DFA_SCAN_EDGE`, [OPT-5] STEP 1's own field) is present in
  every record's `engine_metadata_declaration` block but is NOT rendered
  anywhere in this report — `report.py` has no legend clause for it yet
  (no reporter code changes were made to add one; flagged as a gap, not
  fixed). `.subject-grain.md` (`--grain subject`) carries the per-subject
  drill-down the ratios above are read from; `.tsv` the same set-grain
  query (10 `record` rows — the included set, the superseded record gets
  no row of its own — no Δ column, matching the `-repin-` `.tsv` shape
  above).

- `2026-09-02-bounded-0.3-budu-ryzen1600-first-sample-1989c62.md` — the
  FIRST SAMPLE of `bench/bounded@0.3` ([B27]) at pcrec **1989c62** (abi 15),
  and the **[OPT-5] STEP 2 BEFORE**: six cells `measured` 2026-09-02
  02:45-06:13 EDT, `--trials 5`, the full-suite overnight window ([B26] (b)).
  Query: `report --subbench bounded --version 0.3 --since
  2026-09-02T02:40:00Z --until 2026-09-03T00:00:00Z --testee
  libpcre2_10.46_interp-caps-simdna --testee libpcre2_10.46_jit-caps-simdna
  --testee pcrec_1989c62_auto-caps-simdna --testee
  pcrec_1989c62_auto-nocaps-simdna --testee pcrec_1989c62_vm-caps-simdna
  --testee pcrec_1989c62_vm-in-caps-simdna --format md` — 6 records. The
  roster is explicit rather than implied: bounded@0.3's three CLANG records
  from later the same day satisfy the same `--subbench`/`--version`/`--since`
  and would otherwise land in this file, which is the `-cc-` group's job.
  READ IT WITH `bench/bounded/NOTES.md` §"What 0.3 added" — the match-regime
  frame is a STAMP, not a rung list, and this sample re-reads it: under
  `pcrec-auto` the whole-subject artifacts of `cls-upto-4` … `cls-upto-1024`
  and `grp-upto-1024` carry `dfa_match=unwrapped`, `cls-upto-2048` /
  `-4096` / `-8192` and `cls-atleast-4096` carry `search-filter`, and
  `cls-upto-16384` / `-32768` / `cls-lazy-16384` are VM (no stamp — the
  scope iff), UNCHANGED from the a7e0bdf census the predictions were
  written against. P4 fires on the pinned tier here (the scratch-tier
  smoke in NOTES.md is superseded as evidence, not contradicted).
  Compile cost: `cls-upto-65535` is `did-not-compile` under both `auto` and
  `auto-nocaps` (`pattern too large (NFA exceeds 131072 states)`,
  byte-identical to every prior pin) and — KB-4's adapter half, first
  visible in a committed report here — each of those four refusal rows now
  carries a real `emit-c ns` figure (12.5-23.7 ms) instead of `-`, read
  from the row's `cost.total_ns` because a refusal carries no `phases`
  array. Mechanism legend: `sel=` is `forced` / `selected` /
  `collapsed-prefilter` / `declined-nullable` only — the abi-14
  `declined-nullable-default` token appears NOWHERE. `.subject-grain.md`
  (`--grain subject`) carries the per-(rung, subject) match rows P1-P5 are
  read from; `.tsv` the same set-grain query.

- `2026-09-02-bounded-0.3-budu-ryzen1600-cc-1989c62.md` — the **cc AXIS**
  ([B24]) on `bench/bounded@0.3`: the three gcc/clang PAIRS of one pcrec
  config each (`auto` vs `auto_cc-clang`, `auto-nocaps` vs its clang
  sibling, `vm` vs its clang sibling), six testees in one report, six cells
  `measured` (the three gcc arms in the overnight window, the three clang
  arms 2026-09-02 10:08-14:45 EDT — two of them RE-RUN BY HAND after
  `scripts/run_window.sh`'s 3000 s per-cell cap killed them, which is why
  the cap moved to 5400 s in d621079). Query: as the first-sample entry
  above but with the six `--testee` values `pcrec_1989c62_{auto-caps-simdna,
  auto-caps-simdna_cc-clang, auto-nocaps-simdna, auto-nocaps-simdna_cc-clang,
  vm-caps-simdna, vm-caps-simdna_cc-clang}` and no pcre2 arm (the baseline
  column is a pcrec arm here; a toolchain pair has no use for an engine
  the toolchain did not build). READ DOWN EACH PAIR, never across the
  table: the ranking's `vs best` and `vs baseline` columns mix all six
  arms, and only the same-config gcc/clang division is a statement about
  the toolchain. `pcrec-vm-in` has no clang sibling at this pin, so the
  fourth config is absent by design. THE REFUSAL SET IS IDENTICAL ON BOTH
  TOOLCHAINS: `cls-upto-65535` under `auto`/`auto-nocaps` and their clang
  siblings, same diagnostic, and NOTHING else refuses — the [CC-CLANG]
  frameless-VM refusal pcrec fixed at abi 14 does not return.
  `.subject-grain.md` and `.tsv` the same query.

- `2026-09-02-loglines-0.1-budu-ryzen1600-after-1989c62.md` — the AFTER
  sample on `loglines@0.1` at pcrec **1989c62**: four fresh pcrec arms plus
  two pcre2 baselines `measured` 2026-09-02 07:01-07:44 EDT, rendered
  CROSS-PIN. Query: `report --subbench loglines --version 0.1 --until
  2026-09-03T00:00:00Z` plus TWELVE `--testee` values — the six fresh ids
  and, for the Δ column, each fresh arm's own IMMEDIATELY-PREVIOUS measured
  pin on this set: `pcrec_263b013_{auto,vm}-caps-simdna` (2026-08-31) and
  `pcrec_96e44c2_{auto,auto-nocaps,vm,vm-in}-caps-simdna` (2026-08-30).
  **12 records included, 6 superseded.** THE Δ BASELINE IS NOT UNIFORM, and
  this is deliberate: `report.py`'s `_cross_pin_info` pairs a row with the
  NEWEST OLDER same-(engine, config) record in the report, so `auto` and
  `vm` are read against 263b013 while `auto-nocaps` and `vm-in` are read
  against 96e44c2 — because the 263b013 window only remeasured two of the
  four arms. There is no a7e0bdf loglines record at all (that window
  measured `bounded@0.2` alone), so "vs a7e0bdf" is not a query this store
  can answer; per-arm previous-pin is the nearest true reading and the
  ledger must name the pin beside each Δ. Read the READER'S CAVEAT on the
  a7e0bdf bounded entry above before using any `vs best` cell here: with
  four pins' rows in one table, `vs best` inverts visually wherever an
  older pin's row ranks first. No `did-not-compile` anywhere (`level-context`
  compiles under `auto` at every pin since [SEL-1]).
  `.subject-grain.md` carries the 16 KB-1 MB sweep per flavour; `.tsv` the
  set-grain query (no Δ column).

- `2026-09-02-loglines-0.1-budu-ryzen1600-cc-1989c62.md` — the **cc AXIS**
  on `loglines@0.1`: the same three gcc/clang pairs, six cells `measured`
  (gcc 07:19-07:44, clang 12:38-13:04 EDT). Query: `report --subbench
  loglines --version 0.1 --since 2026-09-02T02:40:00Z --until
  2026-09-03T00:00:00Z` plus the same six `--testee` values as bounded's
  `-cc-` file. Same reading rule: down each pair, never across. Nothing
  refuses on either toolchain.

- `2026-09-02-email-specimen-0.2-budu-ryzen1600-after-1989c62.md` — the
  AFTER sample on `email-specimen@0.2` at pcrec **1989c62**: four fresh
  pcrec arms plus the two pcre2 baselines `measured` 2026-09-02 07:53-08:30
  EDT, rendered CROSS-PIN against the LAST email sample, pcrec **96e44c2**
  (2026-08-30). Query: `report --subbench email-specimen --version 0.2
  --until 2026-09-03T00:00:00Z` plus TEN `--testee` values (the six fresh
  ids and the four `pcrec_96e44c2_*` ones). **10 records included, 7
  superseded.** Unlike loglines above, the Δ baseline here IS uniform —
  96e44c2 remeasured all four arms — so every pcrec row's Δ is one pin
  step. The two intervening pcrec pins (263b013, a7e0bdf) never measured
  this set, so a "one pin step" here spans three pcrec releases in wall
  time; say so when citing it. `.subject-grain.md` and `.tsv` the same
  query.

- `2026-09-02-altwide-0.1-budu-ryzen1600-first-sample-1989c62.md` — the
  FIRST SAMPLE of sub-bench #5, `bench/altwide@0.1` ([B11.2]), at pcrec
  **1989c62**: six cells `measured` 2026-09-02 08:37-10:07 EDT. Query:
  `report --subbench altwide --version 0.1 --since 2026-09-02T02:40:00Z
  --until 2026-09-03T00:00:00Z` plus the same six-testee roster as
  bounded's first-sample file — 6 records. READ IT WITH
  `bench/altwide/NOTES.md`'s eight predictions, and read the REFUSAL TABLE
  FIRST: pcrec refuses BOTH forms of every pattern at width 512 and above
  on ALL FOUR configs, `auto` included. Only `w-8`, `w-64`, `w-256`
  (`plain` only), `nar4-64`, `sfx-64`, `sh1-64`, `cnt-64` (`plain` only)
  and the floor pattern compile. The two refusal diagnostics are
  different mechanisms and the report prints both verbatim: `auto` /
  `auto-nocaps` hit the TOTAL emitted-source cap (`1000000` B — the
  premultiplied transition table is what fills it; `w-256 plain` emits
  977,055 B of which only 18,829 is code), `vm` / `vm-in` hit the CODE cap
  (`500000` B). That refutes P5's "no refusal at any rung for pcrec-auto"
  and caps the readable ladder at three rungs, so P2/P3/P4 are answered
  where they can be and are UNTESTABLE above `w-256` at this set version
  (`pfx3-512`'s predicted offset-set prefilter and `srt-512`'s order lever
  both live on refused patterns). P8 is refuted too: `dfa_scan_edge=range`
  on every compiled DFA artifact but the floor's. What the three readable
  rungs do show is P2's headline, cleanly. `.subject-grain.md` and `.tsv`
  the same query.

**[B63] reports (2026-09-21, lane b63window) ADDED one file group — the
pcrec re-measure wave 1, `bench/loglines@0.1`'s pcrec canonical roster
(auto/nocaps/vm/vm-in) at pin 25b1984f** — the [B61] staleness
burn-down's first set. Changed NOTHING else here: the reporter is
unchanged at v18 (2026-09-18). Carries an explicit `--since`/`--until`
pair *and* an explicit `--testee` roster (the 2026-08-30 rule and KB-5),
ten testees: the two pcre2 baselines (newest 2026-09-02), pcrec-auto's
own d34c9131 record (2026-09-06, already the single-variable
comparator [EMIT-VERB] predicts), pcrec-nocaps/vm/vm-in's own 1989c62
records (2026-09-02, five pins stale — see the predictions file's own
entry above for exactly which intervening pcrec steps this gap
crosses), and the four fresh 25b1984f records this window wrote.
Window: `build/windows/window_loglines_20260921T041451Z.log`
(2026-09-21 00:14:51-00:49:28 EDT, 4/4 cells attempt 1 rc=0), store
190 -> 194. Query: `report --subbench loglines --version 0.1 --since
2026-09-01T00:00:00Z --until 2026-09-21T05:00:00Z` plus the ten
`--testee` values — **10 record(s) matching this query, 10 included, 0
superseded**. `worst_other_core_busy: 13.83%`.

**THE FINDING**: R-DELTA-1 (34 firings) shows a clean split by route
that matches the predictions file's own stated grounding exactly —
`pcrec-auto`/`pcrec-nocaps` (already at or within one pin of d34c9131,
[EMIT-VERB]'s own single-variable claim) move only ×1.00-1.08 in either
direction, while `pcrec-vm`/`pcrec-vm-in` (the five-pin-stale pair,
crossing [OPT-5] STEP 2 among other VM-route work) read a real,
substantial **×1.29-1.57 FASTER** on every large-subject-throughput and
short-subject-search cell but one (`floor`, which reads **slower
×1.03-1.32 on ALL FOUR routes** — a flat, route-independent move,
read as measurement/box-state noise on the trivial baseline pattern
rather than a route-specific regression, stated here rather than
explained away). Predictions P1-P4 (`delta_verdict` eq-token
"unchanged (within spread)") all REFUTED, exactly as the strict-op
construction predicts for P1/P3 (small ordinary jitter) and as the
file's own honest-null framing anticipated for P2/P4 (a real,
documented-possible mover, now confirmed real and large). P5/P6 (the
same-pin structural "byte-identical artifact" claims, nocaps-vs-auto
and vm-in-vs-vm) were ALSO refuted — a genuine, unpredicted finding:
`--no-captures` moves `level-context`'s emit_bytes by ×2.425 (nocaps
LARGER) while shrinking `ipv4`'s whole-subject form by ×0.825 (a
real per-pattern route/selection effect, not the flat "nothing to
strip" null this lane predicted from the corpus's own capture-free
grammar), and `pcrec-vm-in` carries genuinely more emitted bytes than
`pcrec-vm` (×1.13-1.16, not ×1.00) — plausibly the caller-provided
buffer's own static sizing reaching the emitted source, not a pure
runtime parameter as predicted. P7 (a vm-in-vs-vm TIME clause) scored
against the WRONG pin by a selector-glob artifact (the bare
`testee=pcrec_*_vm-in-caps-simdna` selector matched the report's OLDER
1989c62 record instead of the fresh 25b1984f one) — a lesson for the
next same-pin structural clause, not a re-run (predictions are frozen
pre-run artifacts, per convention): pin the OUTER selector's testee_id
to the pin actually being measured when the report's roster spans more
than one pin for that config family. Full verdict table and the
selector-glob lesson: `docs/dev/lanes/b63window_report.md`.

- `2026-09-21-loglines-0.1-budu-ryzen1600-after-25b1984f.md` — pcrec's
  canonical loglines roster at 25b1984f, cross-pin against each
  testee's own most recent prior record (d34c9131 for auto, 1989c62 for
  nocaps/vm/vm-in). `.tsv`/`.subject-grain.md`/`.subject-grain.tsv`/
  `.matrix.tsv`/`.matrix.html` siblings all rendered the same query;
  `.interpretation.md` generated WITHOUT `--predictions` (the same F27
  gap `capability-0.1-pin-25b1984f-confirm.tsv`'s own entry documents:
  this population necessarily includes already-measured older-pin
  records) — predictions scored separately via a direct
  `interpret.evaluate_predictions` call, same precedent, worked around
  the same KB-24 `_measured_text` crash on `delta_verdict`'s string-kind
  values (a local monkeypatch of the formatting helper only; `_op_holds`
  untouched).

**[B63] reports (2026-09-21, lane b63window) ADDED a second file group —
`bench/altwide@0.2`'s pcrec canonical roster (auto/nocaps/vm/vm-in) at
pin 25b1984f**, wave 1's second set. Changed NOTHING else here: reporter
unchanged at v18. Ten testees: two pcre2 baselines, pcrec-auto/pcrec-vm's
own d34c9131 records (single-variable, [EMIT-VERB]'s own comparator),
pcrec-nocaps/pcrec-vm-in's own 334fd10e records (one pin short of
d34c9131's [FORM-CHAR] cls-fold step), and the four fresh 25b1984f
records. Window: `build/windows/window_altwide_20260921T053218Z.log`
(2026-09-21 01:32:18-02:37:59 EDT, 4/4 cells attempt 1 rc=0), store
194 -> 198. Query: `report --subbench altwide --version 0.2 --since
2026-09-01T00:00:00Z --until 2026-09-21T07:00:00Z` plus the ten
`--testee` values — **10 record(s) matching this query, 10 included, 0
superseded**. `worst_other_core_busy: 32.82%`.

**THE FINDING, NOT PREDICTED BY THIS LANE AND STATED PROMINENTLY**: the
DFA/auto route's refusal boundary on this set SHRANK DRAMATICALLY
between d34c9131 and 25b1984f — R-STATUS-4 (direct TSV grep confirms
the interpreter's own count) shows `pcrec_25b1984f_auto-caps-simdna`/
`auto-nocaps-simdna` refuse only **4 patterns** (`s-2048`, `s-4096`,
`w-1024`, `w-2048`) where the SAME roster refused **18** at d34c9131 —
`ci-256`, `ci-512`, `cnt-64`, `nar4-512`, `pfx3-512`, `sfx-512`,
`sh1-512`, `srt-256`, `srt-512`, `w-256`, `w-384`, `w-512`, `wb-256`,
`wb-512` all COMPILE now that did not before. Read directly from the
fresh record's own `engine_metadata`: `w-256` whole-subject's
`emit_bytes` dropped from 1,033,795 B (d34c9131, refused, over the
1,000,000 B cap) to **706,900 B** (25b1984f, compiles, -31.6%);
`ci-512`'s `dfa_table` stamp reads **`mixed`** (plain form,
emit_bytes 976,275) and **`indexed`** (whole-subject, emit_bytes
686,048) at 25b1984f, where it refused outright (over cap on BOTH
forms) at d34c9131. The mechanism this points to is cf0962e3's own
`[OPT-DIAL]`/K59 "premul drop-ladder rung" (landed between d34c9131 and
25b1984f, in the gap this window's `pcrec-auto` single-variable
comparator does NOT cross for the TIME axis but the `dfa_table` stamp
clearly does for SIZE) — a real, substantial, GOOD-NEWS rescue on the
DFA route's compiled-size ceiling, stated here as a finding for pcrec
to confirm or correct, not asserted as proven mechanism. The VM route's
refusal boundary is, by contrast, EXACTLY UNCHANGED — `pcrec_25b1984f_
vm-caps-simdna`/`vm-in-caps-simdna` refuse the identical 11-pattern set
d34c9131 (`vm`) and 334fd10e (`vm-in`) already refused, byte for byte
the same pattern names. This directly UPDATES the [B61] staleness
caveat's own "wb/ci refusal-boundary cells" headline: those cells are
NOT stale-but-probably-similar, they moved for real, in a direction
that increases the DFA route's usable ladder length.

**Predictions P8-P13** (the refusal-boundary `section=did_not_compile`
set-eq clauses) scored **not-evaluable**, not confirmed/refuted, for a
SELECTOR-AUTHORING reason found while scoring: `report.py`'s
`did_not_compile` rows carry a BLANK `form` column (confirmed by direct
`awk` on the TSV) — the `plain`/`whole-subject` split this lane's
grounding source (`docs/dev/measurements/2026-09-06-altwide-size-
census-d34c9131.txt`) carries is that PROBE SCRIPT's own column shape,
not `report.py`'s. Every P8-P13 selector named `form=plain`, which
matches nothing in this section, so all six read "nothing measurable"
rather than confirming or refuting — the finding above was read by
DIRECT TSV inspection instead, not through the predictions mechanism.
A lesson for the next refusal-boundary predictions file, not a
re-scored one (predictions are frozen pre-run artifacts). Predictions
P1-P4 (`delta_verdict`) refuted, all within ×1.00-×1.14 — the honest
timing null holds on this set (unlike loglines' VM route, altwide's
vm/vm-in gap is only one pin and does not cross [OPT-5] STEP 2).
Predictions P5-P6 (same-pin structural `compile:emit_bytes` ratio
claims) also refuted: `pcrec-nocaps` is NOT byte-identical to
`pcrec-auto` here either (×1.426 on `w-256`/`srt-256`, the SAME
direction and roughly the same magnitude loglines' P5 found), and
`pcrec-vm-in` carries real extra bytes over `pcrec-vm` (×1.25-1.95,
largest on `ci-256`) — the "nothing to strip"/"buffer is runtime-only"
hypotheses this lane predicted from the corpus's own capture-free
grammar do not hold at either testee pair, on either set. Full verdict
table: `docs/dev/lanes/b63window_report.md`.

- `2026-09-21-altwide-0.2-budu-ryzen1600-after-25b1984f.md` — pcrec's
  canonical altwide roster at 25b1984f, cross-pin against each testee's
  own most recent prior record (d34c9131 for auto/vm, 334fd10e for
  nocaps/vm-in). `.tsv`/`.subject-grain.md`/`.subject-grain.tsv`/
  `.matrix.tsv`/`.matrix.html` siblings all rendered the same query;
  `.interpretation.md` generated WITHOUT `--predictions` (the same F27
  gap); predictions scored separately via a direct
  `interpret.evaluate_predictions` call with the same KB-24 workaround
  as the loglines group above.
