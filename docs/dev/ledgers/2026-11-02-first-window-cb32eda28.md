# [B149] first window ledger -- pcrec cb32eda28 (abi 93) vs 614d45eb3 (abi 89)

Lane `b149w2read`, plan row [B149] (the READ of window W2 = `b149w2`). Window: `/var/tmp/pcrecbench/b149w2/chain.log`, `CHAIN_START 2026-11-01T07:56:46 EST` (-05:00; 12:56:46Z)
to `CHAIN_DONE 2026-11-01T13:18:01 EST` (18:18:01Z), `WINDOW_DONE suite_rc=0 closing_rc=0`; machine `ryzen7700x`, core 7; store commit 69b9af2e. 12 cells, 13 records, all
`measured` except one `inconclusive-spread` sentinel record that the contract keeps beside its re-measure: capability@0.4 x {auto-caps, auto-nocaps} at cb32eda28 AND
at `@614d45eb3` (the same-window BEFORE), and the opening and closing sentinel passes (sentinel@0.1 x pcrec-auto cb32eda28, pcrec-auto@614d45eb3, pcrec-nocaps cb32eda28,
pcre2-jit). Nothing was timed by this lane; `store/` and ~/pcrec untouched. Every number below comes from the committed records or the committed reports.

Inputs, archived under `docs/dev/measurements/2026-11-02-b149w2read/` (`w2.py` the record readers, modes named per section, outputs in `out/`; `d119.py` reads the report TSV;
`gen.py` renders the groups; read-only over the records; arithmetic = per-trial set sums over the clean common subjects, then the median, the reporter's definition):

- reports `reports/2026-11-02-{capability-0.4,sentinel-0.1}-ryzen7700x-first-cb32eda28.*` (reporter **v28**; `--since 2026-11-01T12:00:00Z --until 2026-11-01T19:00:00Z`,
  `--machine ryzen7700x`, explicit `--testee` ids; capability: `.tsv .md .matrix.tsv .subject-grain.md .subject-grain.tsv`; sentinel: `.tsv .md .matrix.tsv` with
  `--all-records` so both passes and the spread record show) and one `.interpretation.md` sidecar each (catalogue 3.22, determinism `cmp` clean on both).
  The capability null band reads each record's own `program_sha256_v3` (273 cells, criterion v3, no census fallback), so no `reports/identity/` file was needed.
- The capability group is the only cross-pin one (614d45eb3 -> cb32eda28 within one sub-bench version, @0.4). 0.4 = 0.3 + two query-string throughput subjects
  (`t-qs-1m`, `t-qs-nearmiss-256k`); no pattern or short subject moved.

Notation. Medians over 5 trials. A set cell = the per-trial SUM over the regime's subjects of per-subject ns/call, then the median over trials. B = pcrec 614d45eb3 (abi 89), N = pcrec
cb32eda28 (abi 93). X/Y = N's median over B's (<1 = N faster). Capability records have the plain form only in their match rows. "caps"/"nocaps" = pcrec-auto / pcrec-nocaps.

## 0. What the window could and could not see

1. capability and sentinel ran caps and nocaps (sentinel: cb32eda28 caps + nocaps, 614d45eb3 caps) plus the libpcre2 JIT sentinel row; no other engine ran, so no report here ranks
   pcrec against a non-pcrec engine (every `baseline_identity` row reads `row-best-fallback -- interp absent`).
2. No forced-VM arm, no `-in` arm, no utf8 arm, no `-fno-*` arm ran. The abi-91 forced-VM `abc` witness, the `--memfn=no-window-search` arm and the `-fno-req-handoff` arm that
   O-116 §§1, 3 say a mechanism comparison needs were NOT in the roster: abi 92's `cover` is read as the 614d45eb3 -> cb32eda28 pair, not as an A/B on the one mechanism.
3. syntax, bounded, loglines, email, altwide, unusual and subst did not run: the K134 give-up flips on `bench/unusual` (24 + 8 + 3 subject cells, the ~342 -> ~763 depth boundary) are NOT measured here.
4. Section 9 collects "not read".

## 1. Was the window clean?

**The chain.** `quiet --samples 5` before the chain read NOT QUIET (load1 3.7-4.6, busiest other core 12.8-27.6%, target core 6.0-20.8%); the chain logs it and goes on by design, the per-cell
pre-flight decides. The log also holds a DRYRUN=1 rehearsal (07:05-07:39 EST, `store=/var/tmp/pcrecbench/b149w2/dry-store`, load1 up to 97 when it stopped inside the fourth capability
cell): nothing of it is in `store/`. Per cell (23 invocations, 12 cells): **7 of 12 passed the pre-flight at attempt 1** (sentinel 614d45eb3 open, sentinel nocaps open, capability x
{cb caps, cb nocaps, 614 caps}, closing sentinels 614d45eb3 and nocaps; the other 5 cells needed 2-5 attempts); **10 invocations were refused (rc=3, nothing written)**: sentinel cb caps open x3 (measured at attempt 4), sentinel jit
open x2 + one more after the spread re-measure (attempts 1, 2, 4), capability nocaps@614d45eb3 x2 (measured at attempt 3), closing sentinel cb caps x1, closing jit x1. **One invocation exited 4** (the
jit opening sentinel, attempt 3, 08:27): written and indexed `inconclusive-spread`, trial agreement `disagree`, worst group `wild-semdiv-dollar-trailing-newline-pcre2` / short-subject-search / plain
d = 43 of n = 75 rows; `run_window.sh` re-measured it once as the contract says (attempt 4 refused, attempt 5 `measured`, 08:37-08:38) and the first record stays in the store (it shows in the sentinel
report under `--all-records`). Walls: opening sentinel pass 41 min, capability 249 min (61-63 min per cell, one minute of refusals), closing pass 29 min; `CELL_CAP` (3600 s / 5400 s) never fired.
The index line after the window reads `measured 635, inconclusive-spread 14, inconclusive-load 9`.

**Per record** (`w2.py quality`, `out/quality.txt`): status `measured` on 12 of 13 (the spread record the 13th); trial agreement (rule `v1.11-group`) `agree` on 12 of 13, capability 0 of 138 / 140
groups failing (8-12 disagreeing rows of ~6,500, 4-5 unjudged); the BEFORE pre-flight sample passed on all 13 (busiest other core 1.8-9.9%, target core 0.2-5.8%). The AFTER samples are PROVENANCE under v1.4 and are
not clean: **capability cb32eda28 caps after-sample failed on occupancy (other core 10.10%, target 3.4%), cb32eda28 nocaps on occupancy (25.36%, target core 14.7%), 614d45eb3 caps and nocaps on load1 (2.09, 2.17)** --
R-STATUS-10 fires on all four capability records; sentinel: cb caps open (14.8 / 5.2), cb nocaps open (12.5 / 7.8), cb nocaps close (24.3 / **15.3 on the target core**), jit open (16.3 / 6.4). The reporter prints
the worst other-core busy as 47.06% (cb32eda28 caps, `wild-semdiv-dollar-trailing-newline-pcre2` large). The box is Frank's desktop; the window ran Sunday 07:56-13:18 EST. **Verdict: usable, not quiet at the
edges; every cell passed its own BEFORE gate and every record's trials agree; the in-window cb32eda28 vs 614d45eb3 pair is the only comparison taken at face value.**

**The driver is one build.** The chain's driver sha256 at start and at end are equal (`0e877032...`, auto and nocaps); that is the SAME hash the 10-28 window ended on (b147read ledger section 1), so
W2 re-used that driver binary (byte-identical at start and end, and to the 10-28 window's final one; a rebuild to identical bytes would not show, but there is no diff to explain). The
setup block differs only in `run.harness_commit` (`e0e68c3e` -> `e516461f`, Python-side).

**Sentinels (this window), closing / opening** (`w2.py sentinel`, `out/sentinel.txt`; 15 patterns x 75 short subjects = 1,125 subject-cells, 15 set-cells, all short regime):

| testee | subject-cell median | p5 - p95 | set-cell median | set-cell range |
|---|---|---|---|---|
| pcrec cb32eda28 auto-caps | 0.9965 | 0.957 - 1.061 | 0.9945 | 0.972 - 1.044 |
| pcrec cb32eda28 auto-nocaps | 0.9947 | 0.933 - 1.012 | 0.9935 | 0.926 - 1.001 |
| pcrec 614d45eb3 auto-caps | 1.0013 | 0.978 - 1.089 | 1.0091 | 0.976 - 1.036 |
| libpcre2 10.46 jit | 0.9981 | 0.741 - 1.155 | 0.9979 | 0.735 - 1.152 |

pcrec medians flat to 0.9% over 5 h; the jit row is noisier (2 set-cells beyond 5%, up to 0.735 / 1.152: its opening record carries a load1 2.50 AFTER sample and a 16.3% other-core reading and
follows a spread-refused attempt). In-window N/B on the **7 sentinel patterns whose every form is program-identical (v3)**: subject-cell median **1.0007 opening, 0.9993 closing** (n = 525, p5-p95 0.975-1.215 /
0.955-1.231); the 8 changed sentinel patterns split by cause, N/B median per pattern (opening / closing): abi92-cover `router-prefix-order` 0.947 / 0.976, `keyword-prefix-order` 0.954 / 0.951, `file-ext-order` 0.933 / 0.895,
`floor-byte` 0.936 / 0.906; abi93-K134 `trim-nested-star` 0.925 / 0.898, `numeric-id-nested-plus` 1.095 / 1.061, `phone-list-nested-plus` 1.018 / 0.980, `wild-validator-us-zip-owasp` 1.000 / 0.994.
Read: the 13 records' status/agreement/pre-flight/after fields, the chain log, the sentinel records. Not read: the per-minute `/proc/stat` timelines; the box queue's log; the dry-run's own store.

## 2. The cross-window control: 614d45eb3 this window vs 2026-10-28 -- CLEAN

The pin 614d45eb3 was measured in the previous window (capability@0.3 caps + nocaps, sentinel@0.1 caps + jit) and again here as the `@614d45eb3` BEFORE, so the b147read control (+4.0-4.4% on short cells,
sentinel pcrec +5.4%, jit flat) can be taken again at ONE pin across two windows (`w2.py xwin`, `out/xwin.txt`; capability: common clean subject-cells of @0.3 and @0.4, 1,170-5,250 per cell):

| config | regime | set-cells | median ratio (W2 / 10-28) | p5 - p95 (set) | subject-cell median |
|---|---|---|---|---|---|
| 614d45eb3 auto-caps | large | 69 | **1.0009** | 0.986 - 1.040 | 1.0002 |
| 614d45eb3 auto-nocaps | large | 70 | **1.0000** | 0.977 - 1.031 | 0.9998 |
| 614d45eb3 auto-caps | short | 69 | **0.9994** | 0.980 - 1.019 | 0.9998 |
| 614d45eb3 auto-nocaps | short | 70 | **0.9983** | 0.976 - 1.017 | 0.9989 |

Sentinel, W2 / 10-28 at 614d45eb3 caps: opening subject-cell median **1.0004**, closing **1.0038** (set-cells 0.9997 / 1.0103); libpcre2 jit 1.0068 / 0.9968. All 138 / 139 compile rows are `program_sha256_v3`-identical and `artifact_bytes` is
identical (delta 0 on every row); the driver binary is the same file (section 1). Set-cell outliers: `evil-alt-nested` large caps x1.254 (44,594 -> 55,941 ns) and `phone-list-nested-plus` large nocaps x1.738 (2,552 -> 4,437 ns), the bimodal family
(section 6), and `evil-alt-nested` short nocaps x1.211. **The +4-5% pcrec-side short-cell offset b147read found between 10-26 and 10-28 is ABSENT between 10-28 and 11-01** (same driver build, same artifacts): that fits b147read's
suspicion that the offset belonged to the 10-26 -> 10-28 driver/shim change and nothing else (its cause was never isolated; this window does not isolate it either, it only shows it is not a standing property of the box).
Consequence: cross-window pcrec comparisons between 10-28 and 11-01 are valid to about +-0.2% in the median; a single set-cell is still only as good as its own trial range.
Read: both pcrec sentinel passes and the jit row, the capability @0.3 / @0.4 614d45eb3 records, the compile rows. Not read: the 9ae59f5d4 or 6b2dbd3e records of earlier windows against W2.

## 3. The census, confirmed by value; answers unchanged

`docs/dev/measurements/2026-10-30-b149prep-census.tsv` (compile-only, 614d45eb3 -> cb32eda28): `w2.py census` compares EVERY compiled-both row of the four capability records against the census row: identity by `program_sha256_v3`,
`emit_bytes` and `emit_code_bytes` deltas. **capability caps 138 of 138 and nocaps 139 of 139 compiled-both rows agree (identity AND both byte deltas), 0 mismatches, 0 unattributed, 0 refusal movers** (v3-identical 94 / 112, changed 44 / 27).
By the census's attribution (caps / nocaps): abi93-k134 33 / 16, abi92-cover 9 / 9, abi92-pair-lookahead 1 / 2, the combined abi91+abi92-pair+abi93 row 1 / 0 (`wild-secrets-username-password-pair` plain, caps). The record's `emit_bytes` runs a constant +7 B over the census
at the new pin on all 138 caps rows (the same constant b147read saw). The sizes the census predicted are the sizes the records carry: K134 emit delta **+1,608..+1,882 B (median +1,815, n = 33)**, cover **-6,837..-2,404 B (median -4,286, n = 9)**, the pair look-ahead **+368 B**, the combined row +1,100 B.
The one refusal is `wild-datetime-datefinder-alternation` under caps at both pins ("pattern too large: 589,335 / 591,151 bytes of emitted code (limit 500,000)"), which compiles under nocaps at both: no refusal moved.

**Answers unchanged** (`w2.py answers`, `out/answers.txt`): 0 of 6,486 (caps) / 6,580 (nocaps) match cells have a different outcome multiset between the pins. The non-expected populations are the same cells, counts and kinds at both pins:
caps -- `email-nested-plus` x `t-evil-match-60k` and x `t-evil-nearmiss-16k` `did-not-match-as-expected` (the two dropped-expectation triples the report names), `date-nested-plus` x `t-hyb-datepath-16k` `gave-up` (`PCREC_ERR_FRAMES`), and
`dup-param-detect` x {`t-qs-1m`, `t-qs-nearmiss-256k`} `gave-up` (`PCREC_ERR_FRAMES`, section 4.5); nocaps -- the same minus `date-nested-plus` (which does not give up there). **K134 changed no capability give-up**: `date-nested-plus`
still gives up on the 16 KiB hybrid subject at cb32eda28 (a K134 row, FRAMES = live resume frames, not trail), as the prep report's "NOT predicted to flip" clause said.
Read: every compile row and every match row of the four records, the census TSV. Not read: capability whole-subject forms (no match rows exist), syntax / unusual compile rows.

## 4. Timing of the O-116 movers (capability, same-window N vs B, set cells)

Controls first. Program-identical set cells, N/B (`w2.py null`): caps large n = 42 median **+0.46%**, p5 -0.95 / p95 +1.93, range -5.51 .. +2.79 (the -5.51 is `tail-dotstar-txt`, a 73-ns cell); caps short n = 42 median **+0.14%**, p5 -1.65 / p95 +1.83,
range -7.06 .. +3.44; nocaps large n = 51 median **-0.08%**, p5 -2.61 / p95 +1.52 but min -36.64 (`phone-list-nested-plus`, trials 2,402-4,614 ns inside ONE record) and max +6.75 (`evil-alt-nested`, N trials 46,624-101,611); nocaps short n = 51 median **-0.13%**, p5 -2.35 /
p95 +1.69, range -13.77 .. +6.34. Excluding the three bimodal patterns the nocaps ranges tighten to -13.54 (a 63-ns cell) .. +2.52 (large) and -3.99 .. +6.34 (short). These are the numbers a mover is read against, not the reporter's band (section 6).

### 4.1 abi 92 `cover` (9 plain-form capability patterns x 2 configs; `\[` included)

| pattern | pattern text | large (caps / nocaps) | short (caps / nocaps) | stamps B -> N |
|---|---|---|---|---|
| `hex8-bounded` | `\b[0-9a-f]{8}\b` | **x0.423 / x0.423** (10,855,729 -> 4,588,137 ns) | **x0.570 / x0.567** | scan unanchored -> cover, prefilter first-class-bounded -> none, start end-minus-width -> attempt-start |
| `wild-codegrammar-json-array-begin` | `\[` | **x0.739 / x0.744** | x0.896 / x0.876 | prefilter memchr -> none, same three stamps |
| `keyword-prefix-order` | `in\|instanceof` | x0.873 / x0.894 | x0.940 / x0.932 | prefilter offset-set -> none, start reverse-pass -> attempt-start |
| `wild-codegrammar-json-object-begin` | `\{` | x0.997 / x1.007 | x0.892 / x0.880 | as `\[` |
| `router-prefix-order` | `/user\|/users` | x0.988 / x0.994 | x0.978 / x0.983 | |
| `file-ext-order` | `\.tar\|\.tar\.gz` | x1.007 / x1.000 | x0.911 / x0.952 | |
| `floor-byte` | `~` | x1.037 / x0.980 | x0.921 / x0.941 | |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `foo\|foobar` | x1.000 / x1.000 | x1.041 / x1.051 | |
| **`utf8-lead-no-cont`** | `[\xc2-\xdf](?![\x80-\xbf])` | **x1.954 / x1.941 SLOWER** (1,180,541 -> 2,307,278 ns) | **x1.202 / x1.189** | prefilter byte-class-bounded -> none, scan unanchored -> cover, start end-minus-width -> attempt-start |

Median over the nine: large x0.997 / x0.994, short x0.921 / x0.941. D119 (the reporter's own verdicts, `d119.py`): `hex8-bounded` large/short improve on both configs; `utf8-lead-no-cont` large/short **regress on both configs** (+95.4% / +94.1% large, +20.3% / +18.9% short);
the rest read `within`. Per subject (`w2.py subj`, `out/subj.txt`):

- **`\[` is faster only where the text carries `[`**: t-1m x0.621 and t-256k x0.596 (0.052 -> 0.032 ns/B); the six other 1 MB-class texts sit on the 7.6 us dismissal floor, x0.98-1.04. Short-subject median x0.899 (6.7 -> 5.7 ns on the 1-byte `cg-array-begin`).
  `\{` is the same shape on the short side (x0.876 median, 6.6 -> 5.7 ns).
- **`hex8-bounded`**: x0.33 on the three tail 1 MB texts (2.06 -> 0.67 ms, 1.96 -> 0.64 ns/B), x0.38 on t-1m, x0.70 / x0.69 on the two query-string texts; short per-subject median x0.361 -- **but `sd-empty-alt-hit` / `-miss` (60-61 B) get slower, 64.6 -> 99.2 ns and 63.5 -> 99.4 ns (x1.53-1.57)**.
- **`utf8-lead-no-cont` is slower on EVERY large subject by the same factor**: 0.192 -> 0.375 ns/B (x1.936-1.957 over the six 1 MB-class texts, x1.954 median over 19), and on short subjects +60-73% where the call is 14-21 ns (`sec-github-pat` 21.4 -> 37.0 ns, x1.727; short median x1.062 because
  other short subjects dismiss first). One cover mover changes sign and by ~2x -- the same two-signed picture b147read found for [SCANEDGE-SET].
- The short-regime gain on the tiny-subject cover movers is a near-constant -0.6..-0.9 ns per call (`floor-byte` 6.5 -> 5.8 ns on 1 B; `\{` 6.6 -> 5.7; `router`, `file-ext` x0.91-0.98): the sentinel reproduces it at both passes (cover patterns N/B 0.895-0.976, section 1).

**Verdict: abi 92 `cover` is faster on 5 of 9 plain-form patterns (largest `hex8-bounded` x0.423 large / x0.57 short, `\[` x0.74 / x0.90, `keyword-prefix-order` x0.87 / x0.94), flat on 3 large and slightly faster on short, and SLOWER on one (`utf8-lead-no-cont` x1.95 large, x1.20 short -- reproduced on both configs, disjoint trial ranges, all 19 large subjects).**
Read: the 9 patterns x 2 configs, both regimes, per-subject for the six largest contributors, the stamps on both pins, the D119 verdicts, the sentinel cover rows. Not read: the whole-subject forms (no match rows), any cover pattern outside capability (the census lists cover rows in syntax / utf8 / altwide / loglines / bounded / unusual /
litrun / subst: not in this window), an A/B against `--memfn=no-window-search` (no such arm ran), why cover is selected for `utf8-lead-no-cont`.

### 4.2 abi 93 K134 trail compaction (16 caps + 8 nocaps K134 rows)

The census lists 33 caps / 16 nocaps K134 compile rows over both forms; the match rows are plain-form, so 16 / 8 patterns (`w2.py k134`, `k134call`, `out/k134*.txt`):

| arm | regime | K134 cells n | K134 median | K134 range | program-identical control (same regime) |
|---|---|---|---|---|---|
| caps | large | 16 | x1.0025 | x0.654 .. x1.309 (bimodal family + `date-nested-plus`) | x1.0046 (n = 42) |
| caps | short | 16 | **x1.0191** | x0.817 .. x1.114 | x1.0014 |
| nocaps | large | 8 | x0.9991 | x0.977 .. x1.018 | x0.9992 (n = 51) |
| nocaps | short | 8 | **x1.0378** | x0.991 .. x1.077 | x0.9987 |

- **Large regime: no per-byte cost is distinguishable from the null.** The recursion specimens: `balanced-parens-rec` x1.012 / x1.018, `nested-comment-rec` x1.002 / x0.994, `quoted-delim-match` x0.995 / x1.000, `tag-depth3-bound` x1.022 / x0.977, the 15.1 ms
  `wild-semdiv-empty-alt-repeat-pcre2` x0.990 (caps). The K134 outliers are the bimodal family (`trim-nested-star` x1.309 with N trials 70,817-126,210 ns; `phone-list-nested-plus` x0.836; `evil-alt-nested` x0.888) and `date-nested-plus` x0.654 (a 1.7 us cell).
- **Short regime: a small fixed per-call term.** The set-sum difference divided by the 75 subjects: `bracket-array-define` +1.22 / +0.65 ns per call (10.8 -> 12.0 ns), `tag-depth3-bound` +0.69 / +0.49, `phone-list-nested-plus` +0.66 (caps), `numeric-id-nested-plus` +0.64 (caps),
  `dup-param-detect` +0.33 / +0.54, `nested-comment-rec` +0.34 / +0.17, `balanced-parens-rec` +0.23 / +0.41, `quoted-delim-match` +0.29 / +0.15; the rest within -0.3 .. +0.14 (the identical-cell control spans -0.49 .. +0.19 caps, -1.02 .. +2.30 nocaps). In percent: median +1.9% (caps) / +3.8% (nocaps),
  **8 of 24 K134 short cells beyond +4.3%** (the top of pcrec's D183 range: `bracket-array-define` +11.4 / +5.9%, `tag-depth3-bound` +10.3 / +7.4%, `numeric-id-nested-plus` +9.8%, `phone-list-nested-plus` +9.4%, `dup-param-detect` +7.7% nocaps, `balanced-parens-rec` +7.1% nocaps) because those calls cost 6-12 ns, so 0.5-1.2 ns reads as 5-11%.
  The per-byte cost is zero, the per-call term is the checkpoint-state initialisation (`trail_gc_floor` bound in the run-state, a field in the prep report's abi 93 description) -- that attribution is the shape of the numbers, not a diagnosis. The sentinel agrees on two of the K134 patterns (`numeric-id-nested-plus` N/B 1.095 / 1.061, `trim-nested-star` 0.925 / 0.898).
- **Against pcrec's stated figure** (D183: cscan +0.7-2.1% instructions, recursion shapes +1.6-4.3%): the SIZE cost is above it (emit +1,608..+1,882 B per K134 artifact against the stated +0.6-1.2 KB text; this confirms prep finding F5 on the 33 records), the large-subject TIME cost is below anything resolvable (<= +1.8% on the six recursion/capture specimens),
  the short-subject TIME cost has a median inside the stated range and a tail of eight cells above it, as a fixed ~0.2-1.2 ns/call.
- K134's behavioural claim (the default arm now answers) is not in capability: no capability cell changed outcome (section 3).

Read: the 16 + 8 K134 patterns' two regimes, set sums and per-call differences, the null, the sentinel K134 rows. Not read: the unusual-set cscan / stream cells (where K134 changes outcomes and costs +0.7-2.1%), a differently-shaped BEFORE (there is none: the `also_pins` arm is the only BEFORE), instruction counts (no `perf stat` was run).

### 4.3 The reqrun look-ahead (`wa = 128, wb = 128`, abi 92, unlisted in the stamp list; O-116 §2)

The census attributes `wild-secrets-username-password-pair` (plain; nocaps: this change alone) and `wild-waf-crs-942270-union-select` (plain, both configs) to `abi92-pair-lookahead`; emit +368 B (union-select) / +377 B (username-password-pair nocaps). **It is not a size-only change.**

| pattern | arm | large | short | note |
|---|---|---|---|---|
| `wild-secrets-username-password-pair` | nocaps | **x0.057** (5,641,010 -> 319,670 ns) | x0.939 | stamps unchanged (dfa, `handoff`, req_run `55534552@0`); t-qs-1m 5.27 ms -> 0.235 ms (x0.045), t-qs-nearmiss-256k 0.312 -> 0.031 ms (x0.101), the other 17 subjects 0.985-1.004 |
| | caps | x0.576 (550,444 -> 316,817 ns) | x1.003 | also abi 91 (`dfa_prefilter` byte-class -> handoff) and K134: t-qs-1m x0.576, t-qs-nearmiss-256k x0.360, t-hyb-embed-64k x0.841, the rest flat |
| `wild-waf-crs-942270-union-select` | caps / nocaps | **x1.159 / x1.152 SLOWER** | **x1.113 / x1.087** | stamps unchanged; per-subject x1.07-1.15 on the 1 MB texts, t-1m x1.572 (0.111 -> 0.172 ns/B), short `lp-winpath` 5.3 -> 9.2 ns, `sec-slack-webhook` x1.38 |

Both pair-lookahead movers have disjoint trial ranges. The nocaps username-password-pair change (the cleanest attribution: the pair look-ahead is the ONLY census-attributed difference) is a 17.6x improvement on the two query-string texts and nothing elsewhere; the union-select
change is a 7-16% cost on large and 9-11% on short. D119: the pair mover reads `improve` (`-94.33%` nocaps / `-42.44%` caps large), union-select reads `within` (+15.9% large caps against a +-36.64% band, +11.3% short against 13.77%) -- the band hides it (section 6).
Read: both patterns, both configs, 19 + 75 subjects, the stamps. Not read: the census's other pair-look-ahead rows (in sets that did not run), the emitted C, why the same look-ahead helps one pattern and costs the other.

### 4.4 abi 91 [REQRUN-VM] handoff (and the forced-VM `abc` witness)

**The `abc` forced-VM witness was not in this window.** Among the 71 capability patterns the only abi-91 mover under `auto` is `wild-secrets-username-password-pair` caps (`dfa_prefilter` byte-class -> `handoff`, `req_handoff` `0` on both pins); its caps change is inseparable here from the pair look-ahead and
K134 (all three in one row, section 4.3) and its large gain on the query-string texts matches the nocaps arm (which has only the look-ahead): caps x0.576 vs nocaps x0.057 on the same texts shows the ARMS differ at 614d45eb3 (caps already 0.40 ms there, nocaps 5.3 ms) and converge at cb32eda28 (0.23 ms both). The `7-url-tld-fix` and subst rows are
in sets that did not run. **Verdict: abi 91 is NOT separately timed by this window**; no deny arm (`-fno-req-handoff`) ran.
Read: the one mover's stamps and per-subject times on both pins. Not read: any abi-91 forced-VM or `-in` cell, `7-url-tld-fix`.

### 4.5 The I-172 query-string cells (`t-qs-1m`, `t-qs-nearmiss-256k`; `dup-param-detect`)

**Neither cell has a timing: `dup-param-detect` x both query-string subjects `gave-up` -- `giveup:-3:PCREC_ERR_FRAMES` -- on all five trials, on BOTH pins and BOTH configs** (4 x 2 x 5 = 40 rows, `w2.py qs`, `out/qs.txt`). The compile stamps are the same at both pins: `engine` vm, `engine_sel` selected, `req_handoff` none,
`req_why` emitted, `resume_frames` 2,048, `trail_frames` 3,072, `vm_program_bytes` 4,829 -> 4,851 (+22 B), emit 30,508 -> 32,323 B (+1,815, K134). The pattern `\b(\w+)=[^&]*&(?:[^&]*&)*\1=` backtracks one frame per `&` iteration; the matching subject has up to 386 params on a line and 52,936 in all,
so the 2,048 resume frames are exhausted -- K134 compacts the trail, not frames, and does not change it (prep report section 0.5: live-nesting give-ups stay). The reverse-landmark stage I-172 asked about is not in this pin (`req_handoff` none for this pattern), so the cell it targets could not be timed: what this window measures is **the give-up itself, the same at 614d45eb3 and cb32eda28**.
The 17 other subjects of the pattern (`dup-param-detect` large set cell, caps x1.002 / nocaps x0.977) are flat; its short regime reads x1.046 / x1.077 (the K134 term). The other 68-70 patterns on `t-qs-1m` (`w2.py qs`): median N/B 1.003 / 1.001, extremes -- besides `hex8-bounded` x0.70, `keyword-prefix-order` x0.80, `utf8-lead-no-cont` x1.95, `wild-secrets-username-password-pair` x0.576 / x0.045 (sections 4.1, 4.3) -- only a ~20 ns cell (`pwd-strength-chain` 18.9 -> 23.5 ns, trials 16-30 ns inside the N record).
Prediction P22 (NOTES) is not scoreable: it concerned the match count and costs; both subjects give up. P21 (answers: every testee that answers agrees; R0 empty) holds for the 68-70 other patterns (all `matched-as-expected`); `dup-param-detect` x qs is the R0 give-up on a hazard-family pattern, which NOTES says is a finding.
Read: all 5 trials x both subjects x 4 records, the compile rows. Not read: the elapsed time to the give-up (no timing exists on a `gave-up` row), the oracle's own times, any other engine on these subjects (none ran).

## 5. Unpredicted

1. **`utf8-lead-no-cont` is x1.95 SLOWER under `cover`** on all 19 large subjects and +20% on short (4.1) -- cover has a two-signed effect, like [SCANEDGE-SET] in the previous window.
2. **The reqrun look-ahead is a performance change**: nocaps `wild-secrets-username-password-pair` x0.057 (5.6 ms -> 0.32 ms) with no stamp moving, and `wild-waf-crs-942270-union-select` x1.15 SLOWER (4.3).
3. **The reporter's band is +-36.64% on large >= 1 us** (it was +-19.92% last window), set by ONE nocaps cell, `phone-list-nested-plus` (trials 2,402-4,614 ns in a record; IQR 44.2%); with it the reporter reads `within` for union-select (+15.9%), `trim-nested-star` (+30.9%), the K134 short tail (+10-11%) (section 6).
4. **`dup-param-detect` gives up on both I-172 subjects** at both pins (4.5): the stage that cell was built to measure is not at this pin.
5. **The cross-window control is clean this time** (section 2): the b147read +4-5% offset is not a property of the box or the pin.
6. **K134 costs +1.6-1.9 KB (above the stated +0.6-1.2 KB) but no per-byte time**; the time is a fixed ~0.2-1.2 ns per call (4.2).

## 6. The null band and the D119 verdicts

The reporter's `null_band` section (`reports/...capability-0.4...tsv`): 185 null cells of 273; strata `>=1us` large **band +-36.64%** (n = 73, min -36.64, max +6.75), `<100ns` large +-13.54% (n = 14), `>=1us` short +-6.34% (n = 10), `100ns-1us` short +-13.77% (n = 83), `100ns-1us` large insufficient (n = 5), `<100ns` short empty.
The band is the pooled MAX magnitude of the program-identical cells' deltas: the four widest are all single cells -- `phone-list-nested-plus` large nocaps -36.64%, `evil-alt-nested` short nocaps -13.77% and large nocaps +6.75%, `wild-semdiv-dollar-trailing-newline-pcre2` large nocaps -13.54% (a 63-ns cell). The caps-only identical population has |delta| <= 7.06%
(p5-p95 -1.65 / +1.93, n = 84); the pooled nocaps one carries the bimodal family. `d119.py` (`out/d119.txt`): 273 cells = 185 `null-control` + 76 `within` + **12 outside the bar**: improve 8 (`hex8-bounded` x4, `wild-secrets-username-password-pair` x2, `date-nested-plus` short caps -18.3%, `bracket-array-define` large caps -0.99% against an IQR-only bar of 0.85%),
regress 4 (`utf8-lead-no-cont` x4). **A mover is "beyond the null" in the report only above +-36.6% (large >= 1 us) / +-13.8% (short 100 ns-1 us); the better small-effect control is the identical-cell distribution of section 4 (caps p5-p95 about +-2% in both regimes).** Read against that, `wild-waf-crs-942270-union-select` (+15.9% / +15.2%
large, +11.3% / +8.7% short) and the K134 short tail are real moves the verdicts call `within`.
Read: all 273 d119 rows, the 7 null_band rows. Not read: the strata with n < 10.

## 7. Predictions scoreboard (b149prep section 0, prose; no machine-readable file covers capability@0.4)

abi 92 "a few dozen rows" cover -- census 169, capability 9 patterns (18 rows) **as the census says** (confirmed 18/18 by value); "no answer change" **confirmed** (0 differing cells); K134 "+0.6-1.2 KB" -- **under-called** (+1.6-1.9 KB, 33/33); K134 "+1-4% on cells that already answered" -- median **inside** on the short regime (+1.9 / +3.8%),
no per-byte cost, tail to +11% on eight short cells; K134 give-up flips -- **none in capability** (as predicted for live-nesting cells; the unusual cscan / stream flips are OWED); the abi 91 handoff moves `auto` rows with a required run -- one capability pattern, not separately timed; the pair look-ahead "+368..377 B on 5 rows" -- the bytes are right, the "no timing consequence" reading
is **refuted**: x0.057 and x1.15 (4.3). The census predicted no time; the prior-window controls: hold (section 2).

## 8. Asks for pcrec (the O-117 draft in the lane report carries the text)

(a) `utf8-lead-no-cont` under `cover`: why is the byte-class-bounded scan x1.95 faster than the window search on a 2-byte (class + negative-lookahead) window, what is the break-even, and why does `hex8-bounded` get x1.5 slower on the 60-B `sd-empty-alt-*` subjects while x0.2-0.4 faster on the others? (b) the reqrun look-ahead: intended as a speedup (nocaps username-password-pair x0.057 on the query-string texts) and is it expected to cost `union-select` x1.15 large / x1.11 short? (c) `dup-param-detect`
on the 1 MiB query-string subject gives up FRAMES at 2,048: is the reverse-landmark stage (I-172) coming to this pin, and is the frame cap the intended outcome for the near-miss? (d) K134: the +1.6-1.9 KB and the fixed ~0.2-1.2 ns/call on short subjects -- is the per-call `trail_gc_floor` bind avoidable on cycle-free calls?

## 9. What was NOT read

The `.md` renderings and the subject-grain files (only the sidecar headings and the TSVs); the 100% of whole-subject forms (capability has no whole-form match rows); per-subject structure of every mover except those printed in `out/subj.txt`; the sentinel's own per-pattern N/B beyond the 8 changed patterns; the per-minute `/proc/stat` timelines; the box-queue log; instruction counts or any `perf` event;
the emitted C of any mover; every set but capability and sentinel; every engine but the two pcrec configs and the jit sentinel row; the `-fno-*` arms and the forced-VM `abc` witness; whether the 08:27 jit spread was caused by the 15 s refusals around it (the AFTER sample reads load1 2.50). The sidecars of 114+ older reports are stale against the live index
(`make check-interpret` section 3: 117 stale, [B41]); this lane regenerated nothing but its two own.
