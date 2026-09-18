# THE LEDGER — capability@0.1's cf0962e3 AFTER + the five new-engine first samples

Read-only extraction over the 2026-09-17/18 window: two windows,
`build/windows/window_capability_20260918T011018Z.log` (21:10:18 EDT →
01:19:30 EDT, 9 cells attempted, 8 written + one refusal) and
`build/windows/window_capability_20260918T052141Z.log` (01:21:42 →
01:37:11 EDT, the KB-21 re-run of the ninth cell) — **9/9 cells
eventually measured**, store `index.tsv` **169 → 178**. Four are the
pcrec CROSS-PIN AFTER at pcrec pin **cf0962e3** (abi 26) against the
2026-09-17 a770139e first sample; five are the **FIRST SAMPLE** of the
five newly-wired ext-bench engines (`re2-default`, `re2-longest`,
`onig-default`, `tre-default`, `vectorscan-block-nosom`) on
`bench/capability@0.1`. Scored against: `docs/dev/wake.md`'s work-queue
item 2 (the two I-72 erratum cells, the three KB-20 give-up cells, the
crs-942500 post-F1-fix check), `docs/dev/known_issues.md` KB-20/KB-21,
`docs/dev/inbox_from_pcrec.md` I-72/I-73, `bench/capability/CLAUDE.md`'s
b46tags REQUIRES-tag correction table, `testees/re2/CLAUDE.md`'s
capability census, and `docs/dev/ledgers/2026-09-17-capability-0.1-first-a770139e.md`
(the BEFORE this window's four pcrec cells are read against).

**No predictions file exists for THIS window specifically.**
`docs/dev/predictions/capability-0.1-first.tsv` (P1-P10) is the ONLY
predictions file for `subbench=capability, version=0.1`, and
`pcrecbench interpret` matches a predictions file by
`(subbench, version)` alone (§2 of `docs/design/interpreter_v1.md`),
so it is picked up automatically on both sidecars below even though it
was authored for the FIRST sample's seven-testee roster, not for a
cross-pin AFTER or a five-new-engine population — see §5 for how that
plays out on each report. No new prediction rows were authored before
this window ran; this is stated here per `docs/dev/predictions/CLAUDE.md`'s
own convention rather than a predictions file being back-filled after
the fact.

Numbers only; the manager's interpretation and the outbox item are not
this lane's to write.

**Ratio convention: `A ÷ B`, so > 1 means A is SLOWER (or larger),
unless stated otherwise (the reporter's own `ratio_vs_baseline`/
`ratio_vs_best`/cross-pin-Δ columns are cited as printed).**

**CONTEXT-AROUND-NUMBERS (Frank's directive, memory
`feedback-context-around-numbers`): every population this ledger reads
is stated explicitly below, not only its result.** The two reports below
are SET-GRAIN, both-carry-a-`.subject-grain.tsv`-slice populations
(§0.2); a rule or number scoped to `rank`-section-only rows structurally
cannot see an `excluded` row's population, and §5's P5/P8 reading below
says so by name rather than reporting the machine's tally alone.

---

## 0. SOURCES, SAMPLE SHAPE, HYGIENE

### 0.1 Records and windows

| cell | testee | timestamp | status |
|---|---|---|---|
| 1 | `pcrec_cf0962e3_auto-caps-simdna` | 2026-09-18T01:10:54Z | measured |
| 2 | `pcrec_cf0962e3_auto-nocaps-simdna` | 2026-09-18T01:41:38Z | measured |
| 3 | `pcrec_cf0962e3_vm-caps-simdna` | 2026-09-18T02:10:57Z | measured |
| 4 | `pcrec_cf0962e3_vm-in-caps-simdna` | 2026-09-18T02:51:49Z | measured |
| 5 | `re2_11.0.0_default-caps-simdna` | 2026-09-18T03:33:45Z | measured |
| 6 | `re2_11.0.0_longest-caps-simdna` (attempt 1) | 2026-09-18T00:02:13-04:00 (LOG:1764) | **refused at store.write, KB-21** — nothing written |
| 6′ | `re2_11.0.0_longest-caps-simdna` (attempt 2, the retry) | 2026-09-18T05:22:17Z | measured |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | 2026-09-18T04:02:33Z | measured |
| 8 | `tre_0.9.0_default-caps-simdna` | 2026-09-18T04:39:31Z | measured |
| 9 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2026-09-18T04:59:24Z | measured |

(`store/index.tsv`, grepped directly — cell 6's first attempt wrote
NOTHING to the store per KB-21's own account, so it carries no
index row at all; the "9/9 eventually measured" count is 9 index rows
+ one non-writing refusal.) Per-cell wall time (LOG:1, 330, 657, 980,
1303, 1534, 1764, 2087, 2326, 2561, 2570 in the first log; LOG2:1, 238,
247 in the second): `pcrec-auto` 31.0 min, `pcrec-nocaps` 29.3 min,
`pcrec-vm` 40.9 min, `pcrec-vm-in` 41.9 min, `re2-default` 15.0 min,
`re2-longest` attempt 1 14.2 min (rc=1), `onig-default` 37.0 min,
`tre-default` 19.9 min, `vectorscan-block-nosom` 19.9 min,
`re2-longest` attempt 2 (retry) 15.5 min. Total window wall
21:10:18 → 01:37:11 EDT (window 1: 4h9m12s; window 2: 15m29s,
starting 2m12s after window 1 closed).

### 0.2 Reports and their queries

| cite | file |
|---|---|
| `A-TSV:<line>` | `reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.tsv` (the pcrec cross-pin AFTER) |
| `A-SIDE:<line>` | `reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.interpretation.md` (catalogue 2.0, reporter v17) |
| `B-TSV:<line>` | `reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.tsv` (the five-new-engine first sample) |
| `B-SIDE:<line>` | `reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.interpretation.md` |
| `LOG:<line>` | `build/windows/window_capability_20260918T011018Z.log` |
| `LOG2:<line>` | `build/windows/window_capability_20260918T052141Z.log` |
| `KB:<n>` | `docs/dev/known_issues.md` |
| `NOTES:<Pn>` | `bench/capability/NOTES.md` |
| `LEDGER-1:<§>` | `docs/dev/ledgers/2026-09-17-capability-0.1-first-a770139e.md` |
| `REC:<path>` | a direct read of the record's own JSONL (used only where the reporter's own rule deliberately excludes the fact, named each time) |

**Report A** (cross-pin, pcrec only): query `--subbench capability
--version 0.1 --since 2026-09-17T00:00:00Z --until 2026-09-18T03:00:00Z`
plus the explicit ELEVEN-testee roster (three pcre2 baselines + the four
pcrec testee_ids at EACH of the two pins) — **12 record(s) matching this
query; 11 included; 1 superseded** (A-TSV:1: the superseded row is the
`libpcre2_10.46_dfa-nocaps-simdna` `inconclusive-spread` history row from
the FIRST sample's own pre-flight retry, kept as history, never ranked —
same row LEDGER-1 §0.1 already named). `--until 2026-09-18T03:00:00Z` is
the boundary that keeps `re2-default` (03:33:45Z) and everything after it
out of this report; a looser bound would silently turn this into a
mixed pcrec/engine report the [B28] KB-5 roster discipline exists to
prevent. `worst_other_core_busy: 49.26%` (A-TSV:1,
`pcrec_cf0962e3_vm-caps-simdna` / `logparse-atomic-removed` /
large-subject-throughput). Schema versions in this population: `1.5,1.6`
(A-TSV:1) — the a770139e records are schema 1.5, the cf0962e3 ones 1.6
(`testee.grain`, absent on every pcrec row here since none is
boolean-grain). **No wrong answer or give-up in this population came
from a record older than a770139e** (A-SIDE:20-23, R-STATUS-2: the one
non-measured record outside this report's population is the same
superseded `inconclusive-spread` row, named by key).

`.subject-grain.tsv` slice generated for this group (catalogue 2.0's
grain=subject machinery, [B47]) — 10,008,788 B raw
(`--grain subject --format tsv --subject-grain-slice`), consulted by
both sidecars' `R-BUCKET-DOMINATED` rule and by any `grain=subject`
prediction clause (none fired against a P1-P10 clause this window; see
§5).

**Report B** (five new engines, no pcrec, no pcre2): query `--subbench
capability --version 0.1 --since 2026-09-18T03:00:00Z --until
2026-09-18T06:00:00Z` plus the explicit five-testee roster — **5
record(s) matching this query; 5 included; 0 superseded** (B-TSV:1).
The lower bound excludes every pcrec/pcre2 record from Report A; the
upper bound is generous headroom past `re2-longest`'s 05:22:17Z retry.
`worst_other_core_busy: 76.52%` (B-TSV:1, `vectorscan-block-nosom` /
`wild-semdiv-altorder-foo-foobar-rustregex` / large-subject-throughput
— a single reading on one cell, not shown to move any number in §4/§5
below). Schema version: `1.6` on all five (B-TSV:1) — the first
population in this store where `testee.grain` matters for real:
`vectorscan_5.4.11_block-nosom-nocaps-simd`'s own setup row reads
`grain: boolean`; the other four carry no `grain` key at all (`full` by
absence, `docs/design/record_schema.md` §6.10) — confirmed by a direct
read of each record's setup row (`REC:` — the reporter prints no
`grain` column on any table, so this fact does not appear in either
TSV; it is asserted here from the record itself, same discipline as
LEDGER-1's Finding F full-diagnostic read).

### 0.3 Hygiene

Every one of the 9 measured records reads `agreement: agree` (A-TSV:1
record rows; B-TSV:1 record rows — e.g. B-TSV's `re2_11.0.0_longest`
record row reads `agree (0 of 77 groups; 0 of 3034 rows; 8 unjudged;
k=1.5, 2/3; 5 trials)`, LOG2:246's tail). No `disagree`, no failed
after-sample, no scratch-tier row in either report (A-SIDE / B-SIDE
carry no R-STATUS-9/10/11 firing). Worst other-core readings, both
groups, are named above and are single-cell readings the reports do not
show moving any ranked number (no cell approached the pre-flight's 10%
gate at RUN time — these are AFTER-sample, provenance-only readings per
schema v1.4's own rule).

---

## 1. THE I-72 ERRATUM: BOTH NAMED CELLS VERIFIED, ONE ANSWER FIX AND ONE ARTIFACT FIX

Read `docs/dev/measurements/2026-09-17-mojibake-postfix-argv-bytes.txt`
first: it names the EXACT population this section verifies — "exactly
TWO patterns anywhere carry a raw byte >= 0x80, both in
`bench/capability`" — `mojibake-curly-quote` (0x93/0x94, ANSWERS were
wrong) and `wild-logparse-syslogbase-expanded` (a UTF-8 German umlaut
`\xc3\xa4` inside the alternation, whose ASCII-only subjects never
exercised an answer difference but whose COMPILED ARTIFACT differed
under the corrupted argv encoding — TIMINGS, per the file's own words).
Both fixes are bench-side (`testees/pcrec/adapter.py`'s I-72 fix,
`_compile_one`, raw-bytes argv), landed 2026-09-17 before this window,
at pcrec pin **a770139e unchanged** — no pcrec commit is involved in
either fix; the re-measure rides this window because the pinned records
are append-only (I-72's own ack line).

### 1.1 `mojibake-curly-quote` — the WRONG ANSWER is gone on all four pcrec configs

**At a770139e** (the BEFORE, unchanged, still in the store): `n_wrong =
5` (of 75, `short-subject-search`) on all four pcrec configs
(A-TSV:2660-2663, `excluded` section, `pass_rate 0.9867`) — the same
four rows LEDGER-1 §1.2 Finding A named.

**At cf0962e3** (the AFTER): **zero excluded rows for this pattern on
any `pcrec_cf0962e3_*` testee** (A-TSV grep for `mojibake-curly-quote`
in the `excluded` section returns only the four a770139e rows above;
none for cf0962e3) — the pattern now RANKS on all four configs, and the
reporter's own cross-pin rule states the flip by name, not this ledger's
inference: **`R-DELTA-3`, "a cell that is now measured"**, fires FOUR
times, once per config (A-SIDE:120-129):

- `auto-caps-simdna` rank 1, **now measured (was: wrong)** (A-SIDE:122)
- `auto-nocaps-simdna` rank 2, **now measured (was: wrong)** (A-SIDE:124)
- `vm-caps-simdna` rank 4, **now measured (was: wrong)** (A-SIDE:126)
- `vm-in-caps-simdna` rank 3, **now measured (was: wrong)** (A-SIDE:128)

**VERDICT: mojibake-curly-quote ANSWERS — FIXED, confirmed by value on
all four configs, both regimes** (the `short-subject-search` cell is
the one that was ever wrong; `large-subject-throughput` was already
correct at a770139e per LEDGER-1 §1.2 — see 1.3 below for what DID move
on that regime).

### 1.2 `wild-logparse-syslogbase-expanded` — TIMINGS: flat within the day's noise, and the artifact really did change

Set-grain cross-pin rank rows, both regimes, all eleven testees
(A-TSV:5618-5744): every `pcrec_cf0962e3_*` row's Δ column reads
**`unchanged (within spread)`** or a small **`slower ×1.01`–`×1.04`**:

| regime | testee | Δ | median ns |
|---|---|---|---|
| throughput | `auto-caps` | unchanged (within spread) | 3,989,379.1 (A-TSV:5630) |
| throughput | `auto-nocaps` | unchanged (within spread) | 3,989,467.5 (A-TSV:5636) |
| throughput | `vm-in-caps` | unchanged (within spread) | 41,342,241.7 (A-TSV:5666) |
| throughput | `vm-caps` | **slower ×1.03** | 41,499,179.0 (A-TSV:5672) |
| search | `auto-nocaps` | unchanged (within spread) | 3,578.3 (A-TSV:5684) |
| search | `auto-caps` | **slower ×1.01** | 3,797.2 (A-TSV:5702) |
| search | `vm-in-caps` | unchanged (within spread) | 40,969.4 (A-TSV:5744) |
| search | `vm-caps` | **slower ×1.04** | 39,975.6 (A-TSV:5738) |

No pass-rate ever moved (all four configs read 1.0000 pass-rate at both
pins, both regimes — the ANSWER never diverged on this pattern's
ASCII-only subjects, exactly as the measurement file predicted).

**The artifact DID change, confirmed from the compile section, not from
timing alone**: `emit_bytes`/`artifact_bytes` shrink by a small, uniform
amount on the DFA-route (`auto`) configs and by a smaller amount on the
forced-VM ones —

| testee | form | a770139e `artifact_bytes` | cf0962e3 `artifact_bytes` | Δ |
|---|---|---|---|---|
| `auto-caps` | plain | 180,072 | 175,976 | −4,096 |
| `auto-caps` | whole-subject | 180,168 | 180,168 | 0 |
| `auto-nocaps` | plain | 159,552 | 155,456 | −4,096 |
| `auto-nocaps` | whole-subject | 159,648 | 159,648 | 0 |
| `vm-caps`/`vm-in-caps` | either form | 105,728 | 105,728 | 0 (`.so` unchanged) |

(A-TSV, `compile` section, `artifact_bytes`/`emit_bytes` rows for
`wild-logparse-syslogbase-expanded` — grepped directly, both pins.) The
`emit_bytes` figures move by the same −4,096/-367 pattern
(`auto-caps` plain 536,222 → 526,348; `vm-caps` 297,093 → 296,726).
**READING**: the corrected (single, valid two-byte UTF-8) sequence
compiles to a slightly SMALLER DFA class table than the double-encoded,
corrupted one did — a real, small, and fully explained artifact change,
too small against a 1 MB throughput scan to read as anything but noise
on the WALL-CLOCK numbers above.

**VERDICT: wild-logparse-syslogbase-expanded TIMINGS — the erratum is
resolved as a real (small) artifact-size change with no measurable
wall-clock consequence outside the day's ordinary cross-pin noise band**
(§4 below quantifies that band at 2,706/2,904 = 93.2% of all Δ cells
reading `unchanged (within spread)`).

### 1.3 The one UNPREDICTED consequence of the fix: mojibake's forced-VM throughput cell got genuinely slower

`mojibake-curly-quote` / `large-subject-throughput` was ALREADY ranked
at a770139e (not excluded — the corrupted pattern still correctly
answered `nomatch` on the 1 MB text by coincidence). Its cross-pin Δ on
the two forced-VM arms reads **`slower ×2.00`** (A-TSV, rank rows:
`vm-caps` 407,560.4 → 814,717.8 ns; `vm-in-caps` 407,415.6 → 813,909.7
ns — both `A-SIDE:95` extremal, `A-SIDE:100-101`), while the
`auto-caps`/`auto-nocaps`/pcre2 rows on the SAME pattern/regime read
`unchanged (within spread)` (23,150.8 → 23,150.8 ns et al., A-TSV
rank rows). **READING**: the auto/DFA route dismisses the 1 MB subject
without ever comparing the pattern's own bytes (a required-first-byte
check clears it either way, flat cost); the forced-VM route now
performs a genuine byte-for-byte scan against the CORRECT two-byte
sequence across the whole subject where before it scanned for the
corrupted, coincidentally-cheaper one — a real ×2 cost of the argv fix
being CORRECT, isolated to the one testee class that cannot skip the
byte comparison. Not a regression to raise with pcrec (bench-side
adapter fix, not a pcrec change); flagged in §6 as a bench-side finding
worth a one-line note in `testees/pcrec/CLAUDE.md`'s I-72 history.

---

## 2. KB-20 CONFIRMED BY VALUE: `evil-alt-nested` × {auto-caps, vm-caps, vm-in-caps} — `timed-out` → `gave-up` NAMED

**At a770139e** (BEFORE the b43giveup fix, still in the store): all
three cells read `n_gave_up = 0`, `n_wrong = 0`, `gave_up_summary`
EMPTY (A-TSV:1495, 1497, 1498 — `pass_rate 0.9733`, no give-up code
recorded at all) — exactly the shape KB-20 names as the batched-give-up
artifact's signature: the harness could not tell a 540 s re-paid
give-up from a genuine wall-clock hang, so it recorded neither a
give-up count nor a code, only the pass-rate hole.

**At cf0962e3** (AFTER the fix): the SAME three cells now read
`n_gave_up = 10` (of 15 trials — 2 subjects × 5 trials each) and a
NAMED code, **`-2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss,
18 B)`** (A-TSV:1499, 1502, 1504):

| testee | a770139e | cf0962e3 |
|---|---|---|
| `auto-caps` | `n_gave_up=0`, summary empty (A-TSV:1495) | `n_gave_up=10`, `-2:PCREC_ERR_STEPS×2 (…)` (A-TSV:1499) |
| `vm-caps` | `n_gave_up=0`, summary empty (A-TSV:1497) | `n_gave_up=10`, `-2:PCREC_ERR_STEPS×2 (…)` (A-TSV:1502) |
| `vm-in-caps` | `n_gave_up=0`, summary empty (A-TSV:1498) | `n_gave_up=10`, `-2:PCREC_ERR_STEPS×2 (…)` (A-TSV:1504) |

`pass_rate` is unchanged at `0.9733` on all three both before and after
(the give-up count was always implicitly baked into the pass-rate hole;
what changed is whether the harness can NAME it). **VERDICT: the three
KB-20 cells CONFIRMED flipped exactly as predicted — `timed-out`
(opaque) → `gave-up: PCREC_ERR_STEPS` (named, graceful)** — the same
two subjects (`rd-evil-alt-near-miss`, `sd-empty-alt-hit`, per
LEDGER-1 §1.2 Finding C) on all three configs. `auto-nocaps` is
UNCHANGED at both pins (`n_wrong=10`, no give-up — A-TSV:1496, 1501 —
its own KB-20-unrelated wrong-answer path, LEDGER-1's own reading,
persists as designed).

---

## 3. THE F1 FIX CONFIRMED: `wild-waf-crs-942500-comment-obfuscation` NOW COMPILES ON BOTH `auto` ARMS

**At a770139e**: `did-not-compile` on `auto-caps` and `auto-nocaps`,
both regimes (4 rows total, A-TSV — the same gcc transcript LEDGER-1
§2 Finding F quoted in full, KB-18's fix keeping it un-truncated here
too). **At cf0962e3**: **zero `did_not_compile` rows for this pattern
on any testee** (A-TSV: the only four `did_not_compile` rows for this
pattern, at lines 7916-7917 and 7972-7973, are BOTH a770139e's — none
at cf0962e3). The pattern now RANKS on `auto-caps`/`auto-nocaps` at
cf0962e3, and it ranks FAST:

| testee | regime | median ns | rank | ratio vs JIT |
|---|---|---|---|---|
| `pcrec_cf0962e3_auto-caps` | throughput | 23,126.1 (A-TSV:7862) | 1 | ×0.0098 (JIT: 51,801.2, A-TSV:7874) |
| `pcrec_cf0962e3_auto-nocaps` | throughput | 23,154.4 (A-TSV:7868) | 2 | ×0.0098 |
| `libpcre2_jit` | throughput | 51,801.2 (A-TSV:7874) | 3 | 1.00 (baseline) |
| `libpcre2_dfa` | throughput | 1,949,356.0 (A-TSV:7880) | 4 | ×37.6 |
| `libpcre2_interp` | throughput | 2,354,099.0 (A-TSV:7886) | 5 | ×45.4 |
| `pcrec_cf0962e3_vm-caps` | throughput | 4,083,498.7 (A-TSV:7892) | 6 | ×78.8 |
| `pcrec_cf0962e3_vm-in-caps` | throughput | 4,086,986.2 (A-TSV:7910) | 8 | ×78.9 |
| `pcrec_cf0962e3_auto-caps` | search | 735.0 (A-TSV:7918) | 1 | ×0.26 (JIT: 2,811.0, A-TSV:7930) |

**VERDICT: crs-942500 post-F1-fix check — CONFIRMED CLEAN.** The DFA
route (`auto`) is not merely fixed but the FASTEST arm on both regimes,
×102 faster than the JIT on throughput and ×3.8 faster on search — the
pattern is a short, literal-anchored WAF rule that the DFA route was
always well suited to before the comment-escaping bug blocked it
outright. The forced-VM arms (unaffected by F1 — they never took the
DFA route) show `unchanged (within spread)` Δ across the pin
(A-TSV:7892, 7910), confirming the fix touched ONLY the DFA emitter's
comment generation, nothing else about this pattern's VM compilation.

---

## 4. THE REST OF THE CROSS-PIN POPULATION: FLAT, AND STATED AS A POPULATION

`R-DELTA-1`, cross-pin Δ outside spread, fires **33 times** on Report A,
aggregated to 13 by (regime × config × direction) (A-SIDE:84-102); the
raw Δ-column tally across every rank row that carries one:

| Δ verdict | count | share |
|---|---|---|
| `unchanged (within spread)` | 2,706 | 93.2% |
| `slower ×N` | 126 | 4.3% |
| `faster ×N` | 72 | 2.5% |
| `now measured (was: wrong)` | 24 | 0.8% (the mojibake flip, §1.1) |

(2,904 total Δ-bearing rows, `awk` over A-TSV column 18.) Every
`slower`/`faster` reading outside §1.1/§1.3's two named findings sits at
**×1.00–×1.04** (`awk` over the same column with the ratio stripped: 42
rows at ×1.00 slower, 36 at ×1.00 faster, 30 at ×1.01 slower, 24 at
×1.01 faster, 18 each at ×1.02/×1.03 slower, 6 at ×1.04 slower, 6 each
at ×1.02/×1.03 faster) — the single exception is the mojibake `×2.00`
pair (§1.3), which the ratio-size threshold catches precisely because
it is far outside this day's noise band, not because the predicate is
ratio-size-based (`A-SIDE:84`'s own legend: the rule fires on spread,
not ratio size — a tight-spread ×1.00 cell fires exactly as readily as
a genuine ×2.00 one, and both are shown above rather than only the
large one). **This is the day's noise floor for the [B48]-tail re-pin,
stated as a population, not a single number**: 2,706 of 2,904 Δ cells
(93.2%) read flat; the two exceptions (§1.1, §1.3) are both explained
by name, and nothing else in the population needed explaining.

---

## 5. THE FIVE NEW ENGINES: CAPABILITY CENSUS, CORRECTNESS, AND THE b46tags CROSS-CHECK

### 5.1 Compile census, direct from the records (the reporter's own bucket excludes this population by design)

`pcrecbench/report.py`'s own comment states the rule this section works
around: `did_not_compile_by_pattern` is built ONLY from rows whose
`compile_outcome == "did-not-compile"`, "deliberately NOT
`unsupported-by-declaration`, a testee's own advance declaration and a
different fact" (`pcrecbench/report.py:3336-3339`) — so the reporter's
TSV/MD carry NO section listing which patterns a testee declined by
capability. This census reads each record's own `compile`-kind rows
directly (`REC:`, one dedup per `pattern_id`, all 64 patterns):

| testee | compiled | unsupported-by-declaration | did-not-compile |
|---|---|---|---|
| `re2-default` | 39 | 25 | 0 |
| `re2-longest` | 39 | 25 | 0 |
| `onig-default` | 62 | 1 | 1 |
| `tre-default` | 41 | 20 | 3 |
| `vectorscan-block-nosom` | 40 | 22 | 2 |

`onig-default`'s one `did-not-compile` (`balanced-parens-rec`,
`onig_new failed (code -116): unmatched close parenthesis`) and one
`unsupported-by-declaration` (`negation-scope-lookbehind-var`, the
declared `lookbehind-variable` withhold) match `testees/onig/CLAUDE.md`'s
own two-refusal count exactly (62/64 compiled, both named refusals
reproducing their isolated-witness `ONIGERR_*` code — that adapter note's
claim, confirmed here on the real corpus run rather than re-derived).

### 5.2 The b46tags REQUIRES-tag correction: DOES the refusal reason match the corrected tags?

**YES, on every one of the six corrected patterns this window's roster
can exercise, and two flip a real behavioral witness exactly as
`bench/capability/CLAUDE.md`'s b46tags section predicted:**

| pattern | b46tags fix | this window's witness |
|---|---|---|
| `quoted-delim-match` | `backrefs` → `backrefs;lookaround` | `tre-default` cites `REQUIRES lookaround` ONLY (backrefs satisfied, lookaround is the actual blocker — the exact discrimination the b46tags census predicted, `testees/tre/CLAUDE.md` item (d).5) |
| `utf8-lead-no-cont` | `non-utf8-subject` → `non-utf8-subject;lookaround` | `tre-default`/`re2-*`/`vectorscan` all cite `REQUIRES lookaround` ONLY; `onig-default` compiles it clean (onig satisfies lookaround) |
| `tag-depth3-bound` | `-` → `backrefs` | `re2-*`/`vectorscan` cite `REQUIRES backrefs`; `tre-default`/`onig-default` compile it clean (both satisfy backrefs) |
| `codegrammar-xflag` | `free-spacing` → `free-spacing;named-groups` | `re2-*` cite `free-spacing` alone (RE2 satisfies named-groups); **`tre-default` cites `free-spacing, named-groups`** — the added token is TRE's REAL second blocker, invisible before the fix |
| `bracket-array-define` | `recursion;free-spacing` → `+named-groups` | `re2-*` cite `free-spacing, recursion` (named-groups satisfied); **`tre-default` cites `free-spacing, named-groups, recursion`**; `vectorscan` cites `recursion` alone (satisfies both spacing tokens) |
| `nested-comment-rec` | `recursion` → `recursion;lookaround` | `re2-*`/`tre-default`/`vectorscan` all cite `REQUIRES lookaround, recursion` together |

(Every cell in this table read from §5.1's direct-record census, `REC:`
— `tre-default` and `vectorscan-block-nosom` are the same two engines
`bench/capability/CLAUDE.md`'s b46tags section names as its behavioral
witnesses, and this window's real corpus run reproduces both live
flips: `codegrammar-xflag` and `bracket-array-define` on `tre-default`
now name `named-groups` as a real, additional blocker where the
PRE-fix tag would have attributed the whole refusal to `free-spacing`/
`recursion` alone.) **No pattern in this census cites a token the
b46tags table did not add or that the original tags already had** —
the corrected tags and the measured refusal reasons agree on every
checkable cell.

### 5.3 Vectorscan's boolean grain: renders correctly

Confirmed directly from the record (§0.2): `vectorscan-block-nosom`'s
setup row carries `testee.grain: "boolean"`; the reporter's own rank
rows for this testee carry pass-rate/wrong/give-up columns exactly like
any other testee (B-TSV, rank rows for e.g. `ipv4-near-miss` —
`pass_rate 1.0000`), and the schema's own X34 rule (a `boolean`-grain
testee's match rows never carry a non-null `observed.span`) is not
something either report can show directly (no span column exists in
either rendering) — asserted here as a schema-level fact the record
itself satisfies, not something read off the TSV.

### 5.4 Correctness — the standout finding is `evil-alt-nested`'s split across FOUR NEW response shapes, and TRE's own broader gap

`evil-alt-nested` (`^(([a-z]+)*)+$`) on the five new engines
(B-TSV:386-391):

| testee | outcome | detail |
|---|---|---|
| `onig-default` | **gave up, gracefully, on a NEW code** | `-17:retry×2 (smallest: rd-evil-alt-near-miss, 18 B)` (B-TSV:386) — `-17:retry` names Oniguruma's own retry/match-limit guard, a code this bench has not recorded before this window |
| `re2-default` | **wrong** | `n_wrong=10` (B-TSV:388) |
| `re2-longest` | **wrong** | `n_wrong=10` (B-TSV:389) |
| `tre-default` | **wrong** | `n_wrong=10` (B-TSV:390) |
| `vectorscan-block-nosom` | **wrong** | `n_wrong=10` (B-TSV:391) |

Read beside LEDGER-1 §1.2 Finding C's own three-way split
(PCRE2 graceful give-up / `pcre2-dfa`+`pcrec-nocaps` silently wrong /
captures-requiring pcrec TIMES OUT): **the wider roster adds a FOURTH
shape, not a fifth** — every one of the four non-backtracking
automaton-style engines here (RE2 ×2, TRE, Vectorscan — all
linear-time, none of them backtrack) returns a silently WRONG answer on
this adversarial pattern, exactly the shape `pcre2-dfa` and
`pcrec-auto-nocaps` already showed; only `onig-default` (a genuine
backtracker, like PCRE2) has a give-up guard to fall back on, and its
guard is a DIFFERENT named code (`-17:retry`) from PCRE2's own
`-47:match`. **No engine in this ten-testee superset hangs on this
pattern except pcrec's own captures-requiring VM arms** (LEDGER-1
Finding C) — the timeout is pcrec-specific, not a property of
"engines that struggle with this pattern" in general.

**The `semantics-divergence` family (family 11) reproduces on EVERY
leftmost-longest engine in the roster, and on NO leftmost-first one** —
exactly as `bench/capability/NOTES.md`'s family-11 design intends, now
confirmed across engines rather than only on `pcre2-dfa`:

| pattern | `re2-longest` (POSIX longest) | `tre-default` (POSIX longest) | `re2-default` (Perl-first) | `onig-default` (Perl-first) | `vectorscan` (Perl-first) |
|---|---|---|---|---|---|
| `file-ext-order` | wrong, 5/75 (B-TSV:440) | wrong, 5/75 (B-TSV:441) | clean | clean | clean |
| `keyword-prefix-order` | wrong, 5/75 (B-TSV:672) | wrong, 5/75 (B-TSV:673) | clean | clean | clean |
| `router-prefix-order` | wrong, 5/75 (B-TSV:1029) | wrong, 5/75 (B-TSV:1030) | clean | clean | clean |

This is the SAME documented trio `testees/pcre2/CLAUDE.md` names for
`pcre2-dfa` (LEDGER-1 §1.1) — the convention axis, not the engine
identity, is what predicts the divergence, confirmed on a second and
third engine.

**TRE has a substantially wider correctness gap than any other new
engine**, on patterns OUTSIDE family 11 too:

| pattern | regime | pass-rate | detail |
|---|---|---|---|
| `high-byte-run` | throughput | **0.0000** (3/3 wrong, B-TSV:538) | ALL THREE throughput subjects wrong |
| `high-byte-run` | search | **0.4800** (195/375 wrong, B-TSV:563) | over half the short subjects wrong |
| `mojibake-curly-quote` | search | 0.9867 (5/75 wrong, B-TSV:800) | the same raw-high-byte pattern pcrec itself got wrong before its own I-72 fix (§1.1) |
| `tag-pair-match` | search | 0.9867 (5/75 wrong, B-TSV:1073) | a `backrefs`-only pattern TRE declares satisfied and compiles, but answers wrong on |
| `wild-waf-crs-942360-concat-sqli` | search | 0.9867 (5/75 wrong, B-TSV:2480) | a WAF SQLi rule, no unusual construct |

**READING**: `high-byte-run`'s 0%/48% wrong rate is the widest
correctness gap of anything measured in this bench's history for a
CAPABILITY-DECLARED-SATISFIED pattern (TRE never declined this pattern
by capability — it compiled it and then answered wrong on most or all
of its subjects). Combined with `mojibake-curly-quote`'s failure, the
pattern points at a SYSTEMATIC raw-high-byte handling gap in
`tre_regncompb`'s byte-mode matching, not a one-off; `tag-pair-match`
and `crs-942360-concat-sqli` show the gap is not confined to
non-UTF-8 bytes either. This is TRE's own standout finding from this
sample, distinct from and larger than the expected family-11
divergence.

### 5.5 Predictions: NONE of P1-P10 evaluate on this five-engine population

`B-SIDE:260-268` (`R-PRED-3`, "a prediction that cannot be evaluated")
fires **9 times**, and **no `R-PRED-1`/`R-PRED-2` firing exists in
Report B at all** — every P1-P10 clause names a testee_id or a
selector shape from the ORIGINAL seven-testee roster
(`docs/dev/predictions/capability-0.1-first.tsv`), and none of those
testee_ids exist in this five-new-engine query's population, so every
clause reads "no row in this report matches the selector." **This is
expected and not a gap in this window**: P1-P10 were never authored
against `re2`/`onig`/`tre`/`vectorscan`, and §6.3's next-sample-checklist
item names writing a NEW prediction set for the ext-bench roster as the
next-sample task, not a retrofit of the existing file.

On Report A, the same six not-evaluable clauses persist from LEDGER-1
(`A-SIDE:263-271`, unchanged: P2/P3/P4/P6/P7/P10, the same set-grain-only
gap LEDGER-1 §3 already read), and the two evaluable ones read the SAME
verdicts as the first sample:

- **P1 — still CONFIRMED** (`A-SIDE:254-256`): the same three named
  patterns still read `n_wrong = 0` across the union of both pins'
  records.
- **P5 — still the interpreter FALSE-POSITIVE, still refuted on
  `evil-alt-nested`** (`A-SIDE:258-259`): the selector reads the `rank`
  section only, which by construction excludes every `excluded` row
  (§1's own evil-alt-nested rows, §2's KB-20 flip); `A-SIDE:258` states
  the machine's own "confirmed" reading over 321 `rank`-section values,
  and this ledger repeats LEDGER-1 §3's own correction: P5's true
  population (§2 of this ledger) still shows `evil-alt-nested` wrong on
  `libpcre2_10.46_dfa-nocaps-simdna` — REFUTED on that pattern, same as
  before.
- **P8 — still REFUTED**, and the measured set-subset is now
  ATTRIBUTABLE BY PIN: `{wild-datetime-datefinder-alternation,
  wild-waf-crs-942500-comment-obfuscation}` is what `A-SIDE:262`
  reports over the WHOLE population (both pins), but §3 above shows the
  crs-942500 half belongs ONLY to a770139e's rows — at cf0962e3 alone,
  the refused set is `{wild-datetime-datefinder-alternation}` alone
  (the size-cap refusal, unrelated to F1, still present at both pins —
  §2 Finding E's own reading, unmoved). **Stating what P8's own
  population can and cannot see**: the sidecar's per-pin attribution is
  not something `R-PRED-2`'s selector expresses (it names a `did-not-
  compile` set over the query's WHOLE population), so this per-pin split
  is read here from §3's direct TSV citation, not from the prediction
  scoring.

---

## 6. RANKED FINDINGS

1. **Both I-72 erratum cells verified fixed, one behaviorally and one
   structurally.** `mojibake-curly-quote` answers correctly on all four
   pcrec configs (§1.1, R-DELTA-3 firing by value); `wild-logparse-
   syslogbase-expanded`'s artifact shrinks by a small, fully-explained
   amount with no measurable wall-clock consequence (§1.2). **A NEW,
   unpredicted bench-side finding rides along**: the fix's OWN cost is
   real on the forced-VM route — `mojibake-curly-quote`'s
   `large-subject-throughput` cell is `slower ×2.00` at cf0962e3
   specifically because the VM route can no longer skip a genuine
   byte-for-byte scan the corrupted pattern used to dismiss for free
   (§1.3). Worth a one-line addendum to `testees/pcrec/CLAUDE.md`'s I-72
   history — not a pcrec ask, a bench-side note.
2. **The three KB-20 give-up cells CONFIRMED by value**: `timed-out`
   (opaque, `n_gave_up=0`) → `gave-up: PCREC_ERR_STEPS×2` (named,
   `n_gave_up=10`) on `auto-caps`/`vm-caps`/`vm-in-caps`, exactly as
   the fix's own account predicted (§2). `auto-nocaps`'s unrelated
   wrong-answer path is unmoved, the fix's own no-op argument holding.
3. **The F1 DFA-emitter comment-escape fix CONFIRMED clean**:
   `wild-waf-crs-942500-comment-obfuscation` now compiles on both
   `auto` arms and RANKS FASTEST of all seven testees on both regimes
   (§3) — a genuine "fixed AND fast" outcome, not merely "no longer
   refuses."
4. **`evil-alt-nested` splits into FOUR response shapes across the
   ten-testee superset, not five**: every non-backtracking automaton
   engine (RE2 ×2, TRE, Vectorscan) returns silently WRONG; the one
   backtracking new engine (Oniguruma) gives up gracefully on its OWN
   named code (`-17:retry`, new to this bench); pcrec's captures-
   requiring VM arms remain the only ones that hang (§5.4). Nothing here
   changes LEDGER-1's asks to pcrec; it widens the evidence base for
   ask 3 (whether pcrec's VM route should carry a graceful step-limit
   give-up).
5. **TRE's own correctness gap is the sample's standout finding for a
   new engine**: `high-byte-run` reads 0% pass on throughput and 48% on
   search — the widest wrong-answer rate this bench has recorded for a
   capability-declared-satisfied pattern — plus `tag-pair-match` and
   `wild-waf-crs-942360-concat-sqli` wrong at the family-11-typical
   5/75 rate on constructs TRE declares fully satisfied. Worth a
   `testees/tre/CLAUDE.md` addendum naming the raw-high-byte hypothesis
   as unconfirmed but consistent across three independent patterns.
6. **The b46tags REQUIRES-tag correction is confirmed live on the real
   corpus, not just on the isolated witnesses the audit lane used**:
   every one of the six corrected patterns' refusal reason matches the
   corrected tag exactly, and `codegrammar-xflag`/`bracket-array-define`
   on `tre-default` reproduce the EXACT behavioral flip
   (`free-spacing`-only → `free-spacing, named-groups`) the b46tags
   report predicted (§5.2).

---

## 7. CANDIDATE ASKS (for the manager's outbox item, not sent by this lane)

1. Bench-side note (no pcrec ask): document mojibake-curly-quote's
   `×2.00` forced-VM throughput cost as the I-72 fix's own known,
   accepted price in `testees/pcrec/CLAUDE.md`.
2. Bench-side: add a `testees/tre/CLAUDE.md` finding for the
   `high-byte-run`/`tag-pair-match`/`crs-942360` correctness gap (§5.4/§6
   item 5) — not a pcrec ask.
3. Consider surfacing `onig-default`'s `-17:retry` give-up code in
   `pcrecbench/reduce.py`'s `giveup_code` naming table if it is not
   already named there (this ledger did not check; the report already
   renders it by its raw code, which may already be sufficient).
4. A new predictions file for the ext-bench roster (§8 checklist item 1)
   is a bench-side authoring task, not an ask to pcrec.
5. No new pcrec-facing ask arises from this window beyond LEDGER-1's
   existing three (the nullable-collapse capture boundary, the VM
   step-budget question, the mojibake span follow-up) — this window's
   own findings are either CONFIRMATIONS of pcrec's own fixes (F1) or
   bench-side/new-engine findings with no pcrec action implied.

---

## 8. NEXT-SAMPLE CHECKLIST

1. Author a predictions file for the ext-bench roster
   (`docs/dev/predictions/capability-0.1-ext-roster.tsv` or similar) so
   a future `re2`/`onig`/`tre`/`vectorscan` sample is machine-scored
   rather than reading `R-PRED-3` on every clause (§5.5).
2. If `re2-default`/`tre-default`/`vectorscan-block-nosom` measure this
   set again, re-check whether TRE's `high-byte-run` gap is
   reproducible or was a one-off box artifact (§5.4/§6 item 5) — the
   pass-rate split (0% throughput, 48% search) is itself worth
   understanding before treating it as TRE's settled behavior.
3. Confirm `onig-default`'s `-17:retry` code against Oniguruma's own
   documented retry-limit option (not checked here — this ledger reads
   the code as printed, not the library's own semantics for it).
4. The `wild-datetime-datefinder-alternation` size-cap refusal is
   UNCHANGED at cf0962e3 on all three refusing pcrec arms (§5.5 P8) —
   still an open LEDGER-1 candidate (ask 6 there) if a `-bigcap`-style
   testee is ever added to this set's roster.
5. Re-run the b46tags cross-check (§5.2) at the NEXT re-pin or engine
   addition to confirm the correspondence holds as the corpus or the
   roster grows — this window checked it against the SIX corrected
   patterns only, on the FIVE engines this window measured.

---

## Source header (D35 style)

This file is a READING of the two committed reports and their
interpretation sidecars, never a measurement. Sources:
`reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.{md,tsv,
subject-grain.md,subject-grain.tsv,interpretation.md}`,
`reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.{md,
tsv,subject-grain.md,subject-grain.tsv,interpretation.md}` (sha256 stamps
in each sidecar's own header), `store/index.tsv`,
`build/windows/window_capability_20260918T011018Z.log`,
`build/windows/window_capability_20260918T052141Z.log`,
`docs/dev/known_issues.md` (KB-20, KB-21), `docs/dev/inbox_from_pcrec.md`
(I-72, I-73), `docs/dev/outbox_to_pcrec.md` (O-31 and its addendum),
`docs/dev/wake.md`, `bench/capability/CLAUDE.md`, `bench/capability/
NOTES.md`, `testees/re2/CLAUDE.md`, `testees/onig/CLAUDE.md` (read for
its own two-refusal count, not quoted in full here),
`docs/dev/measurements/2026-09-17-mojibake-postfix-argv-bytes.txt`,
`docs/dev/ledgers/2026-09-17-capability-0.1-first-a770139e.md`. Direct
reads of individual records (`REC:` citations, §0.2 and §5.1) were
needed twice: once to confirm `vectorscan-block-nosom`'s `testee.grain`
field (no report renders it) and once to build the `unsupported-by-
declaration` census the reporter's own `did_not_compile_by_pattern`
bucket deliberately excludes (`pcrecbench/report.py:3336-3339`'s own
comment, quoted in §5.1). No store file, report, or code was modified by
this lane.
