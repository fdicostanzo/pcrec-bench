# THE LEDGER — `bench/capability@0.1`'s FIRST SAMPLE, pcrec pin `a770139e` (abi 25)

Read-only extraction over the 2026-09-16/17 window: `bench/capability@0.1`
([B42]) × seven testees (`pcre2-interp`, `pcre2-jit`, `pcrec-auto`,
`pcrec-nocaps`, `pcrec-vm`, `pcrec-vm-in`, `pcre2-dfa`), the FIRST
production sample of this set at pcrec **a770139e** (abi 25 unchanged —
the [B42] runbook re-pin). Scored against: `docs/design/
capability_set_v1.md` §11.4 (the charter's own cell-time/wall estimate)
and §13 R6 (the cell-cap risk); `bench/capability/NOTES.md`'s predictions
P1-P10 and outlier rule R0-R8; `bench/capability/CLAUDE.md` +
`testees/pcre2/CLAUDE.md` (the documented family-11/`pcre2-dfa`
divergence trio). Facts below come from the committed report and its
interpretation sidecar (never re-derived from records); every number is
cited to its source line.

Numbers only; the manager's interpretation goes to the outbox (O-31).

**Ratio convention: `A ÷ B`, so > 1 means A is SLOWER (or larger), unless
stated otherwise (the reporter's own `ratio_vs_baseline`/`ratio_vs_best`
columns are cited as printed).**

---

## 0. SOURCES, SAMPLE SHAPE, HYGIENE

**Records**: **7 measured, 1 superseded** (the `pcre2-dfa` cell's first
pre-flight attempt — `inconclusive-spread`, kept as history, never
ranked); schema 1.5, tier `pinned`, machine `budu-ryzen1600`, store
`index.tsv` **160 → 168** (SIDE:1-11, header stamp; TSV:2 `record source:
… (8 record(s) matching this query); records: 7; superseded: 1`; window
log tail: `index: 168 record(s) -> store/index.tsv`, `index: by status:
measured 157, inconclusive-load 9, inconclusive-spread 2`; `git show
fbb4639:store/index.tsv | wc -l` = 161 lines (160 records) vs
`HEAD:store/index.tsv` = 169 lines (168 records) — the +8 is 7 new
`measured` records plus the one retained `inconclusive-spread` history
row).

**Report** (rendered from its own committed query, `--since
2026-09-17T00:00:00Z --until 2026-09-17T08:00:00Z` plus the explicit
seven-testee roster, TSV:2):

| cite | file |
|---|---|
| `SIDE:<line>` | `reports/2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.interpretation.md` (`pcrecbench interpret`, catalogue 1.3, reporter v16) |
| `MD:<line>` | `reports/2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.md` (set grain) |
| `TSV:<line>` | `reports/2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.tsv` |
| `LOG:<line>` | `build/windows/window_capability_20260917T005018Z.log` |
| `NOTES:<Pn>` | `bench/capability/NOTES.md` |
| `PRED:<row>` | `docs/dev/predictions/capability-0.1-first.tsv` |
| `DSN:<§>` | `docs/design/capability_set_v1.md` |

No `.subject-grain.md` sibling exists for this report (grain: set only,
TSV:2's header `grain: set`) — every prediction clause whose selector
names a specific `subject_or_na` therefore cannot be evaluated against
this report by construction (§4, below); the sidecar's own rule
(`R-BUCKET-DOMINATED` did not fire: `input-absent (no subject-grain TSV
is supplied…)`, SIDE:201) states this explicitly.

**Interpretation sidecar stamp** (SIDE:1-11): `report_sha256
1b3df831…`, `index_sha256 9b2f464c…`, `predictions_sha256 915b42f5…`,
`catalogue: 1.3`, `interpret: v1`, `reporter: v16 (2026-09-08)`.

**Hygiene**: `agreement` fields on all 7 records read `agree` (LOG tail
and record-listing header rows in MD, e.g. `agree (0 of 116 groups; 5 of
4572 rows; 30 unjudged; k=1.5, 2/3; 5 trials)` for `pcre2-dfa`'s SECOND
attempt, `agree (0 of 126 groups; 52 of 4984 rows; 8 unjudged…)` for
`pcre2-interp`, `agree (0 of 128 groups; 0 of 4990 rows; 2 unjudged…)`
for `pcre2-jit` — TSV:3-5). Worst other-core reading of the window:
**48.39%** (`libpcre2_10.46_dfa-nocaps-simdna` / `email-local-nodup` /
`large-subject-throughput`, SIDE:64, TSV:2 header). No R-STATUS-9/10/11
firing (SIDE:188-190): no `disagree`, no failed after-sample, no
scratch-tier row in this report.

### 0.1 The spread-rule firing (pcre2-dfa)

`pcre2-dfa`'s first pre-flight cell ran to completion and was written
and indexed as **`inconclusive-spread`** (LOG:2268, `attempt 1 rc=4
cell_cap=5400s 2026-09-17T02:23:24-04:00`) — the v1.4 contract's own
retry rule (`scripts/run_window.sh`) re-measured it once; the retry
landed **`measured`, `agree`** at LOG:2579 (`attempt 2 rc=0 cell_cap=5400s
2026-09-17T03:05:28-04:00`). This is the record the report ranks
(TSV:2's `newer_not_measured: 0`; the superseded-1 count is exactly the
retained `inconclusive-spread` history row). No other cell in this
window retried.

### 0.2 Cell wall-times against the §11.4 estimate

§11.4's own model: **~1.7 h estimated wall** for 6-7 cells at "15-18
min/cell" (DSN §11.4 table). Per-cell wall clock, derived from LOG's
`== window run start` / `attempt N rc=… <timestamp>` lines (LOG:1,
338, 669, 988, 1311, 1634, 1957, 2268, 2579):

| testee | cell start (EDT) | attempt end (EDT) | wall | × the 15-18 min band |
|---|---|---|---|---|
| `pcre2-interp` | 20:50:18 | 21:33:13 | 42.9 min | **2.4-2.9×** |
| `pcre2-jit` | 21:33:13 | 22:01:32 | 28.3 min | 1.6-1.9× |
| `pcrec-auto` | 22:01:32 | 22:43:04 | 41.5 min | **2.3-2.8×** |
| `pcrec-nocaps` | 22:43:04 | 23:08:10 | 25.1 min | 1.4-1.7× |
| `pcrec-vm` | 23:08:10 | 00:28:36 | **80.4 min** | **4.5-5.4×** |
| `pcrec-vm-in` | 00:28:36 | 01:47:18 | **78.7 min** | **4.4-5.2×** |
| `pcre2-dfa` (attempt 1, spread) | 01:47:18 | 02:23:24 | 36.1 min | 2.0-2.4× |
| `pcre2-dfa` (attempt 2, measured) | 02:23:24 | 03:05:28 | 42.1 min | 2.3-2.8× |

Total window wall: **6 h 15 min 20 s** (LOG:1 `20:50:18` → LOG:2587
`03:05:38`) for 7 measured cells plus one retry — against an
extrapolated ~2.0 h at the charter's own per-cell band for 7-8 cell-runs.
**The estimate is refuted as stated, by a factor of roughly 3× overall
and up to 5.4× on the two forced-VM cells** — a finding about §11.4's
own model, not about the set: §3.5's model assumes `bench/syntax`'s flat
50 ms/subject shape, and this set's `redos-nested` family (§1.1 below)
is exactly the CB8-flagged risk §13 R6 named in advance ("a ReDoS
witness's own per-iteration cost … is what actually dominates the
cell's wall time, not the model's flat 50 ms", DSN line ~1548) —
confirmed empirically: the two slowest cells (`pcrec-vm`, `pcrec-vm-in`)
are exactly the two testees that hit the redos-nested family's
worst-case backtracking on the 1 MB throughput subjects (§1 below).
§13 R6's stated mitigation — the ~5× `CELL_CAP` headroom (5,400 s vs.
the estimate) — held: **no cell approached the cap** (the longest,
80.4 min = 4,824 s, is 89% of 5,400 s but did not trip it); R6's own
"any cell exceeding ~45 min" early-warning threshold FIRED on both
forced-VM cells, as designed.

---

## 1. CORRECTNESS FIRST — every wrong answer and give-up, attributed

The set declares only `short-subject-search` and `large-subject-
throughput` (no `match-compliance`, DSN §3.5 / `bench/capability/
CLAUDE.md`'s `subbench.toml` entry). R-STATUS-3 fires on every
`excluded` section row whose `metric` is `pass_rate` — by its own
predicate this is EVERY cell in the report with `pass_rate < 1`
(catalogue/rules.toml:136-150), so the **20 firings, aggregated to
nothing (SIDE:23-44)** are the EXHAUSTIVE list of non-clean cells in
this report; nothing outside them can be wrong or gave-up. The full
table (`excluded` section, TSV, one row per cell + one `giveup_smallest`
detail row per give-up subject; also MD:3174-3193):

| pattern | regime | testee | n | pass-rate | gave-up (trials) | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|
| `email-nested-plus` | search | `vm-caps` | 75 | 93% | 0 | 0 | 5× **timed-out** (`sd-empty-alt-hit`, `sd-empty-alt-miss`, `sec-github-pat`, `v-uuid-badnibble`, `v-uuid-valid`) |
| `email-nested-plus` | search | `vm-in-caps` | 75 | 93% | 0 | 0 | same 5, **timed-out** |
| `evil-alt-nested` | search | `dfa-nocaps` | 75 | 97% | 0 | **10** | `rd-evil-alt-near-miss`, `sd-empty-alt-hit` (**wrong**) |
| `evil-alt-nested` | search | `interp` | 75 | 97% | 10 | 0 | same 2, **gave-up** (`-47:match×2`) |
| `evil-alt-nested` | search | `jit` | 75 | 97% | 10 | 0 | same 2, **gave-up** (`-47:match×2`) |
| `evil-alt-nested` | search | `auto-caps` | 75 | 97% | 0 | 0 | same 2, **timed-out** |
| `evil-alt-nested` | search | `auto-nocaps` | 75 | 97% | 0 | **10** | same 2, **wrong** |
| `evil-alt-nested` | search | `vm-caps` | 75 | 97% | 0 | 0 | same 2, **timed-out** |
| `evil-alt-nested` | search | `vm-in-caps` | 75 | 97% | 0 | 0 | same 2, **timed-out** |
| `file-ext-order` | search | `dfa-nocaps` | 75 | 99% | 0 | 5 | `sd-fileext-short` (**wrong** — DOCUMENTED) |
| `keyword-prefix-order` | search | `dfa-nocaps` | 75 | 99% | 0 | 5 | `sd-keyword-short` (**wrong** — DOCUMENTED) |
| `router-prefix-order` | search | `dfa-nocaps` | 75 | 99% | 0 | 5 | `sd-router-short` (**wrong** — DOCUMENTED) |
| `mojibake-curly-quote` | search | `auto-caps` | 75 | 99% | 0 | 5 | `nu-mojibake` (**wrong**) |
| `mojibake-curly-quote` | search | `auto-nocaps` | 75 | 99% | 0 | 5 | `nu-mojibake` (**wrong**) |
| `mojibake-curly-quote` | search | `vm-caps` | 75 | 99% | 0 | 5 | `nu-mojibake` (**wrong**) |
| `mojibake-curly-quote` | search | `vm-in-caps` | 75 | 99% | 0 | 5 | `nu-mojibake` (**wrong**) |
| `wild-logparse-quotedstring-grok` | search | `dfa-nocaps` | 75 | 99% | 0 | 5 | `lp-quoted-escaped` (**wrong**) |
| `negation-scope-lookbehind-var` | throughput | `dfa-nocaps` | 3 | 0% | 15 (all) | 0 | `t-1m`,`t-256k`,`t-64k` — **gave-up** (`-42:pattern`) |
| `negation-scope-lookbehind-var` | search | `dfa-nocaps` | 75 | 80% | 75 (15 subj.) | 0 | 15 named subjects, all trials — **gave-up** (`-42:pattern`) |
| `tag-depth3-bound` | search | `dfa-nocaps` | 75 | 96% | 15 (3 subj.) | 0 | `br-tag-mismatch`,`br-tag-pair`,`rec-tag-depth3` — **gave-up** (`-42:pattern`) |

(TSV `excluded` rows, MD:3175-3193.)

### 1.1 The documented trio: CONFIRMED, and ONLY as documented

`bench/capability/CLAUDE.md` and `testees/pcre2/CLAUDE.md` (lines
230-258) declare **exactly three** cells where `pcre2-dfa`'s
leftmost-longest answer is a correct, documented divergence from the
NFA-oracled `expectations.tsv` row: `file-ext-order`/`sd-fileext-short`
([7,11) vs [7,14)), `keyword-prefix-order`/`sd-keyword-short` ([0,2) vs
[0,10)), `router-prefix-order`/`sd-router-short` ([0,5) vs [0,6)) — one
divergent subject each, `short-subject-search` only, `dfa-nocaps` only.
**The report shows exactly these three and no more on `dfa-nocaps`'s
"documented" list** (5 wrong = 1 subject × 5 trials each, matching).
**The other three `dfa-nocaps` non-clean cells are NOT on that list**:
`evil-alt-nested` (10 wrong — a DIFFERENT pattern, family
`redos-nested`), `wild-logparse-quotedstring-grok` (5 wrong, family
`wild-logparse`), `negation-scope-lookbehind-var` and `tag-depth3-bound`
(give-ups, not wrong, families `cap-lookaround`/`cap-recursion`).
**`testees/pcre2/CLAUDE.md` itself flags an "honest gap"** — the two
`router-prefix-order` `throughput` subjects were never checked for the
same divergence (line 235-236) — and this report shows `router-
prefix-order`'s `large-subject-throughput` cell on `dfa-nocaps` is
NOT in the excluded table at all (clean, 100% pass), so the gap the
adapter note names is now closed empirically for this set: no
divergence fires there.

**Verdict: the documented trio is CONFIRMED, exactly and only as
documented. Every other wrong answer or give-up below is an
UNDOCUMENTED finding.**

### 1.2 UNDOCUMENTED wrong answers (the correctness-first ranked findings)

**Finding A — `mojibake-curly-quote` is wrong on ALL FOUR pcrec
testees, and correct on all three pcre2 testees.** Pattern
`\x93[\x20-\x7e]*\x94` (family `binary-nonutf8`, `requires=non-utf8-
subject`; `bench/capability/patterns.rxt:811-816`). `nu-mojibake` reads
wrong under `auto-caps`, `auto-nocaps`, `vm-caps`, `vm-in-caps` (5/5
trials each, MD:3184-3187) and is absent from every pcre2 testee's
excluded rows. No pcre2 testee is wrong on this pattern; every pcrec
testee is. This is a raw-byte / non-UTF-8 handling divergence specific
to pcrec, on the one family this set built specifically to probe it
(`bench/capability/CLAUDE.md`'s item 5: "`mojibake-curly-quote` omits
`canonical_text`… its identity is `canonical_sha256` alone"). **The
report gives no `[span]` detail** (§4, the format's own expressiveness
limit) — the ledger can say pcrec disagrees with the oracle on this
byte pattern on all four configs, not in what way.

**Finding B — `wild-logparse-quotedstring-grok` is wrong on
`pcre2-dfa`, a SECOND undocumented DFA-vs-NFA divergence beyond the
declared trio.** `lp-quoted-escaped`, 5/5 trials (MD:3193). Not named
anywhere in `testees/pcre2/CLAUDE.md`'s divergence table (lines
230-238), which enumerates exactly six family-11 patterns and this is
not one of them (it is family `wild-logparse`, an atomic-group grok
import). A quoted-string grok pattern with an escaped-quote alternation
is exactly the shape where leftmost-first vs. leftmost-longest can
diverge on which quote the match closes at — plausible, but genuinely
new: pcre2-dfa's divergence surface on this set is at least FOUR cells,
not three.

**Finding C — `evil-alt-nested` (the canonical "evil regex"
`^(([a-z]+)*)+$`, `bench/capability/patterns.rxt:684-693`) fails
DIFFERENTLY on every arm of the roster, on the SAME two subjects
(`rd-evil-alt-near-miss`, `sd-empty-alt-hit`)**:
- `pcre2-interp` / `pcre2-jit`: **give up gracefully** at PCRE2's own
  match-limit (`-47:match`, MD:3178-3179) — the documented,
  well-behaved ReDoS-guard outcome.
- `libpcre2_10.46_dfa-nocaps-simdna`: **wrong answer**, not a give-up
  (MD:3176) — the DFA algorithm has no backtracking budget to exceed,
  so it simply returns an incorrect result rather than refusing.
- `pcrec-auto-nocaps`: **wrong answer** (MD:3181) — the SAME failure
  mode as `pcre2-dfa` on the same two subjects, and pcrec's own
  no-captures config is the only pcrec arm that gets this wrong rather
  than timing out.
- `pcrec-auto-caps`, `pcrec-vm-caps`, `pcrec-vm-in-caps`: **timed-out**
  (MD:3180, 3182-3183) — the harness's own wall-clock give-up, not a
  graceful PCRE2-style match-limit refusal.

  **The failure mode is gated by the CAPTURES axis on pcrec's own
  configs**: `-nocaps` → wrong answer, `-caps` → hang. A silent wrong
  answer and an uncontrolled hang are both worse outcomes than PCRE2's
  own graceful `-47` give-up on the identical adversarial input — this
  is the set's sharpest capability-contrast finding on `evil-alt-nested`
  and belongs in the outbox as an ask, ranked high (§5).

**Finding D — the redos-nested family's real hazard surface is
`large-subject-throughput`, not `short-subject-search`, and NOTES.md
never claimed otherwise there** (see §3, P5 below): `trim-nested-star`
(`^(\s+)*$`) reads **3,255,807.7 ns** under `pcrec-auto-caps` (rank 7 of
7, TSV:2452) against **15.2 ns** under `pcrec-auto-nocaps` (rank 1 of 7,
TSV:2416) — **×214,356** slower with captures required, on the SAME
`auto` engine-selection logic. Mechanism, read from the compile-cost
legend (MD:3260-3261 vs. MD:3380-3381): `auto-nocaps` SELECTS the DFA
(`engine=dfa, sel=selected, match=search-filter`) — immune to
backtracking; `auto-caps` DECLINES that rescue (`engine=vm, sel=
declined-nullable-default (prefilter declined, no cap hit)`) and falls
to the VM, which is exactly the engine vulnerable to `^(\s+)*$`'s
classic nested-star ReDoS shape on a large subject. **The capture
requirement is what removes the DFA rescue and re-exposes the
backtracking hazard pcrec's own auto-selection otherwise avoids** — a
finding squarely inside pcrec's own [OPT-4]/[OPT-4.2] nullable-collapse
machinery, at a factor exceeding 2×10^5 on this witness. `winpath-
near-miss` shows the mirror shape on `large-subject-throughput`: `auto-
caps` 20.2 ns (rank 1, TSV:5049) vs. forced `vm-caps` 4,908,974.8 ns
(rank 6, **×242,483**, TSV:5079) — here `auto`'s own selection logic
(not shown declining) stays fast while the bare forced-VM control does
not, the R-ARM-1 `auto vs vm` shape (SIDE:91-92, extremal firing of that
bucket, `winpath-near-miss / large-subject-throughput`).

By contrast, `phone-list-nested-plus` (`^(\d+\s*)+$`) shows `auto-caps`
staying FAST (28.5 ns, rank 2, ratio_vs_baseline 0.303, TSV:1879/1883)
even though its own legend reads `engine=vm, sel=selected, vm_prefilter=
hybrid, lang=exact (no counted repeat)` (MD:3246) — `auto`'s hybrid
prefilter defeats the hazard the bare forced VM does not: `vm-caps`
reads 3,866,744.1 ns (rank 7, ratio_vs_baseline 41,061.6, TSV:1909/1913)
and `vm-in-caps` 3,864,125.9 ns (rank 6, ratio 41,033.8, TSV:1903/1907)
— **×135,700-136,000** slower than `auto-caps` on the identical
pattern and subject. So `auto`'s own selection machinery sometimes
rescues a redos-nested pattern under captures (`phone-list-nested-plus`,
via a hybrid prefilter) and sometimes does not (`trim-nested-star`, via
a declined nullable-collapse) — the split between the two is itself a
finding worth pcrec's own read (§5).

### 1.3 The `codegrammar-flat` VM-arm split (a smaller, contained finding)

`codegrammar-flat` (family `wild-codegrammar`, the `(?x)`/flattened
control pair NOTES.md P3 is about) reads **1,999,677.3 ns** under
`vm-caps` (rank 4, TSV:280) vs. **4,446,367.4 ns** under `vm-in-caps`
(rank 6, TSV:292) on `large-subject-throughput` — **×2.22** slower on
the caller-provided-buffer entry point for the SAME forced-VM engine
(SIDE:103-105, the `vm vs vm-in` R-ARM-1 bucket's extremal firing on
this regime). The same pair on `short-subject-search` reads ×2.43
(SIDE:106-108, `vm-caps` 1,556.0 ns vs. `vm-in-caps` 3,782.0 ns) — a
smaller, cross-regime-consistent gap, unlike the `mode` (`auto vs vm`)
pairs above whose ratios run into the tens or hundreds of thousands. A
buffer-entry-point cost worth a smaller-scoped ask, not a headline.

---

## 2. THE REFUSAL SURFACE — every did-not-compile, named

R-STATUS-4 (SIDE:46-56): **5 firings, aggregated to 4 by testee** — this
set declares no `--max-emit-*` raise (no `-bigcap` testee in the
7-testee roster, DSN §11.4's table), so both refusals below hit the
STANDARD `pcrec-auto`/`pcrec-vm` code cap.

| pattern | testee | diagnostic | class |
|---|---|---|---|
| `wild-datetime-datefinder-alternation` | `auto-caps` | "pattern too large: 670,132 bytes of emitted code (limit 500,000)" | **cap** (code-size) |
| `wild-datetime-datefinder-alternation` | `vm-caps` | "pattern too large: 665,080 bytes of emitted code (limit 500,000)" | **cap** (code-size) |
| `wild-datetime-datefinder-alternation` | `vm-in-caps` | "pattern too large: 665,080 bytes of emitted code (limit 500,000)" | **cap** (code-size) |
| `wild-waf-crs-942500-comment-obfuscation` | `auto-caps` | "the artifact did not build: [truncated, diagnostic continues]" | **other** (a real compiler failure, not a declared cap) |
| `wild-waf-crs-942500-comment-obfuscation` | `auto-nocaps` | same, truncated | **other** |

(SIDE:48-56; TSV `did_not_compile` rows.)

**Finding E — the `wild-datetime-datefinder-alternation` refusal is
gated by CAPTURES, mirror-imaged against `wild-waf-crs-942500-comment-
obfuscation`'s refusal, which is gated by ENGINE ROUTE.** The datefinder
alternation (rebar's `datefinder` import, family `wild-datetime`)
refuses on `auto-caps` AND both forced-VM arms (`vm-caps`, `vm-in-caps`)
but **compiles cleanly under `auto-nocaps`**: `emit_code_bytes 20,411`
(well under the 500,000 cap), `median_total_ns 852,520,361` compile
time, `emit_bytes 889,500` (almost all DFA table data, not code) —
confirmed from the compile-cost rows (`awk` over the `.tsv`'s `compile`
section, `pcrec_a770139e_auto-nocaps-simdna` / `wild-datetime-datefinder-
alternation`). The no-captures DFA table representation is ~32-33×
smaller in code bytes than the captures-aware VM form the same pattern
needs when captures are required — enough to cross the cap. By
contrast, `wild-waf-crs-942500-comment-obfuscation` refuses on BOTH
`auto` arms (which select the DFA route) and compiles on neither
`vm-caps` nor `vm-in-caps` — i.e. it is refused wherever pcrec's emitter
takes the DFA route, and this is NOT a size cap: it is a genuine C
compile failure (below).

**Finding F — a pcrec DFA-emitter bug: the generated C artifact embeds
the pattern's own literal bytes unescaped inside a generated comment,
and the pattern's bytes happen to contain `/*` / `*/`, breaking the C
compile.** The full diagnostic (read from the record itself,
`store/records/capability@0.1/pcrec_a770139e_auto-caps-simdna/…jsonl`,
since the report's own row is truncated at "[truncated, diagnostic
continues]", MD:3187/3190 — **a harness/report truncation gap in its
own right**, noted for [B41]/reporter follow-up):

```
artifact.c:200:20: warning: missing terminating " character
  200 |      *    5  "/*!*/"   ACCEPTING
      |                    ^
artifact.c:200:20: error: missing terminating " character
artifact.c:201:7: error: expected expression before '/' token
  201 |      */
      |       ^
... (repeats at line 260-261; cascades into a third, unrelated error:
'rx_forward_next_state' undeclared, once the comment/string parsing has
desynchronized)
```

`wild-waf-crs-942500-comment-obfuscation` is a WAF SQLi-obfuscation
detection rule whose own subject matter is the SQL comment-obfuscation
idiom `/*!...*/` — pcrec's DFA-route emitter writes a human-readable
annotation comment naming the matched byte sequence at each DFA state
(`* 5 "/*!*/" ACCEPTING`) directly into `artifact.c`'s C comments,
**without escaping an embedded `*/`** in the pattern's own literal text.
The pattern's own subject matter (`/*!*/`) is exactly the byte sequence
that terminates the C comment early, corrupting the rest of the
generated file. This is a genuine pcrec code-generation defect — not a
declared cap, not "unsupported" — and is the single highest-value,
most concretely actionable finding in this sample (§5, ranked #1).

**P8 is REFUTED by exactly these two patterns** (SIDE:170, R-PRED-2):
predicted `section set-subset` (no pcrec did-not-compile row); measured
`{wild-datetime-datefinder-alternation, wild-waf-crs-942500-comment-
obfuscation}`.

---

## 3. PREDICTIONS P1-P10, ONE BY ONE

Per `docs/dev/predictions/CLAUDE.md`'s format; scored by
`pcrecbench interpret` against catalogue 1.3 (SIDE:163-179). The
sidecar's own tally: **2 confirmed, 1 refuted, 6 not evaluable** — six,
not one, because the interpreter reads the report's `.tsv`, which is
rendered at SET grain (a `.subject-grain.md` sibling WAS committed for
this window, but it is a markdown rendering `interpret` does not read)
and several clauses select a
`subject_or_na` or a `compile:`-scoped comparison the set-grain TSV
cannot answer (§6.3's own rule: "a selector that does not name `section`
reads the `rank` section… never every section at once",
`docs/design/interpreter_v1.md` line ~1742).

| # | verdict (sidecar) | reading |
|---|---|---|
| **P1** | **CONFIRMED** (SIDE:165) | `wild-waf-crs-942140-dbnames`, `wild-secrets-aws-access-key-id`, `wild-codegrammar-json-constant` all read `n_wrong = 0.000` on `pcre2-jit` (worst of 18 values each). None of P1's three named patterns appear anywhere in §1's excluded table — a TRUE confirm, not a scoring artifact. |
| **P2** | **NOT EVALUABLE** (SIDE:175) | selector's `regime_or_na=n/a` and `compile:median_total_ns` quantity target the `compile` section explicitly by name, but the row's own `regime_or_na` column is empty rather than the literal token `n/a` — "no row in this report matches the selector" on both clauses. This is a PREDICTION-AUTHORING / column-convention mismatch, not evidence about `pcre2-jit`'s compile time; the underlying compile rows DO exist and DO show `wild-waf-crs-942360-concat-sqli` compiling 5.3× slower on `jit` (386,192 ns) than `interp` (73,020 ns) and `wild-datetime-datefinder-alternation` refusing outright on every pcrec VM-route arm (§2) — read by hand from the `compile` section (TSV, `awk -F'\t' '$1=="compile" && $2=="wild-waf-crs-942360-concat-sqli"'`), P2.a's underlying claim HOLDS (386,192 ÷ 73,020 = 5.29 > 1) even though the machine scoring could not confirm it. |
| **P3** | **NOT EVALUABLE** (SIDE:176) | same mechanism: the `throughput`/`t-1m` compile-axis selector cannot be matched in a set-grain-only report. |
| **P4** | **NOT EVALUABLE** (SIDE:177) | `logparse-atomic` vs. `logparse-atomic-removed` clauses select `compile:artifact_bytes` (ratio_to) and a specific-subject `search_short` cell; neither resolves without the subject-grain sibling or a `compile:`-scoped selector match. |
| **P5** | **CONFIRMED, BUT A FALSE POSITIVE ON ITS OWN TERMS** (SIDE:166) | the sidecar reports "worst `date-nested-plus`/…/`pcrec_a770139e_auto-nocaps-simdna` = 0.000 over 198 value(s)" — but P5's selector does not name `section`, so per the interpreter's own rule it reads the `rank` section ONLY, and a cell with `n_wrong > 0` is by construction NEVER a `rank` row (R-STATUS-3 moves it to `excluded` instead, §1 above). **P5's own claim is FALSE for `evil-alt-nested`**, one of its six named patterns: §1.2 Finding C shows 10/75 wrong on `dfa-nocaps` and `auto-nocaps`, give-ups on `interp`/`jit`, and timeouts on `auto-caps`/`vm-caps`/`vm-in-caps` — all on `short-subject-search`, exactly P5's regime. The interpreter's mechanical "confirmed" is correct about the 198 `rank`-section values it read and silent about the population it structurally cannot see; the prediction as authored did not name `section=excluded` the way `interpret`'s own P2/P9 worked examples do (`docs/design/interpreter_v1.md` line ~1741, "found by their OWN mechanism, `_elsewhere`"). **Ledger verdict: REFUTED** (evil-alt-nested), with the caveat that P5's other five named patterns (`email-nested-plus`, `trim-nested-star`, `numeric-id-nested-plus`, `phone-list-nested-plus`, `date-nested-plus`) show no wrong answer of their own on `short-subject-search` in §1's table — only `email-nested-plus` shows a (timed-out, not wrong) exclusion on the two forced-VM arms. |
| **P6** | **NOT EVALUABLE** (SIDE:178) | subject-specific (`v-uuid-badnibble`) selector, no subject-grain sibling. |
| **P7** | **NOT EVALUABLE** (SIDE:179) | same shape (`v-ipv4`/`v-ipv4-oor`). |
| **P8** | **REFUTED** (SIDE:170, §2 above) | measured did-not-compile set = `{wild-datetime-datefinder-alternation, wild-waf-crs-942500-comment-obfuscation}`, not empty. |
| **P9** | (no row — P9 is the `mojibake-curly-quote` record-structure prediction, not scored by `interpret` at all; not in `capability-0.1-first.tsv`, PRED file has no P9 row) | Not transcribed to the machine-readable set (checked: `docs/dev/predictions/capability-0.1-first.tsv` has rows P1,P2,P6,P8,P5,P7,P10 with no P9 — a gap in the prediction file against NOTES.md's own P9, itself a structural claim about `canonical_text` omission this report format cannot speak to per §6.4's own inexpressibility rule). |
| **P10** | **NOT EVALUABLE** (SIDE:174) | both clauses select `subject_or_na=nu-lead-no-cont`/`nu-lead-with-cont`; same set-grain gap. `utf8-lead-no-cont` itself is clean in §1's table (no exclusion on any testee), so its underlying answer is at least consistent with P10 holding, unconfirmed by the machine. |

**Sidecar tally restated precisely: 1 true confirm (P1), 1 false-positive
confirm now read as refuted (P5, on `evil-alt-nested`), 1 refuted (P8),
6 not-evaluable due to the set-grain-only report (P2, P3, P4, P6, P7,
P10), and P9 absent from the machine-readable file entirely.**

---

## 4. THE PERFORMANCE READ

### 4.1 R-ARM-1 — arms one config token apart (SIDE:81-108, 285 firings
aggregated to 8 by arm-pair × regime)

The legend (SIDE:83): a firing reads "beyond 2×max(stddev)" — spread-
relative, not ratio-size-relative, so even a ×1.00 pair can fire if both
arms' spread is tight.

| arm pair | regime | firings | extremal ratio | minimum ratio |
|---|---|---|---|---|
| `auto-caps` vs `auto-nocaps` | throughput | 19 | `trim-nested-star` ×214,356 (§1.2 Finding D) | `tag-pair-match` ×1.00 |
| `auto-caps` vs `auto-nocaps` | search | 20 | `trim-nested-star` ×20,956 | `bracket-array-define` ×1.01 |
| `auto-caps` vs `vm-caps` | throughput | 51 | `winpath-near-miss` ×242,483 (§1.2 Finding D) | `currency-lookbehind-fixed` ×1.01 |
| `auto-caps` vs `vm-caps` | search | 48 | `phone-list-nested-plus` ×11,191 | `pwd-strength-chain` ×1.17 |
| `auto-caps` vs `vm-in-caps` | throughput | 52 | `winpath-near-miss` ×244,117 | `balanced-parens-rec` ×1.00 |
| `auto-caps` vs `vm-in-caps` | search | 54 | `phone-list-nested-plus` ×11,182 | `trim-nested-star` ×1.00 |
| `vm-caps` vs `vm-in-caps` | throughput | 7 | `codegrammar-flat` ×2.22 (§1.3) | `keyword-prefix-order` ×1.00 |
| `vm-caps` vs `vm-in-caps` | search | 34 | `codegrammar-flat` ×2.43 (§1.3) | `logparse-atomic-removed` ×1.00 |

(SIDE:85-108, aggregated tabulation.) The `auto vs vm`/`vm-in` pairs
carry the largest and most numerous extremes (51+52+48+54 = 205 of 285
firings): this is `auto`'s own engine-selection logic doing its job
against the raw forced-VM control on catastrophic-backtracking-prone
patterns, exactly the [OPT-4]/[OPT-4.2] rescue this bench already
tracks on other sets — this is the FIRST time it is read on a
`redos-nested`-shaped corpus rather than a bounded-repeat one.

### 4.2 R-FLOOR-2 — cells at or below `floor-byte` (SIDE:122-155, 145
firings aggregated to 12 by regime × testee)

`floor-byte` (the per-call overhead control, tag `family=floor`) reads
7,714.7-17,318.3 ns/subject on `large-subject-throughput` and 8.9-40.4
ns/subject on `short-subject-search` depending on testee (SIDE:124-155
extremal/minimum rows). The pcrec arms' floor is roughly 1,000× cheaper
per subject than the pcre2 arms' on `large-subject-throughput`
(`pcrec_a770139e_auto-caps-simdna` floor 7,722.0 ns vs. `libpcre2_
10.46_jit-caps-simdna` floor 17,318.3 ns, SIDE:130/133) and this ratio
recurs across every floor-relative reading; a pattern at or below the
floor (`base10num-near-miss` reads ×0.001-0.042 of the floor on four
different testees, SIDE:125-138) is running FASTER than the set's own
per-call overhead control implies is possible per byte — i.e. these are
patterns dismissed almost entirely by a required-first-byte / prefilter
check before any per-byte cost is paid, not an anomaly.

### 4.3 R-FLOOR-1 / R-FLOOR-3 — instrument-only exclusions (SIDE:110-120,
157-161)

`R-FLOOR-1` (159 firings, 3 testees): every one of `libpcre2_10.46_
{dfa-nocaps,interp,jit}`'s COMPILE-cost jitter cells on the majority of
patterns reads `timer-floor` (`min_ns` below the reporter's own timer
floor) — pcre2 compiles these patterns too fast to time meaningfully;
this is instrument-floor noise, not a finding, and is exactly why P2/P3
(compile-time comparisons) need the actual `compile` rows read by hand
rather than a bare ratio (§3). `R-FLOOR-3` (13 firings, `jit` only):
compile jitter ratio ≥ 1.0 on `file-ext-order` (1.970, worst) through
`logparse-atomic-removed` (1.004) — the JIT's own compile-time
measurement noise, consistent with R2's "pcre2-jit band" (NOTES §R2)
being about MATCH cost, not this.

### 4.4 What did NOT fire (SIDE:181-203)

No R-DELTA-1/2/3 (no faster/slower, selection-change, or now-measured
clause anywhere — this is a FIRST sample, no cross-pin baseline exists
yet for this set); no R-RANK-1, R-BUCKET-FORM/VSBEST/SPAN (no cross-pin
pairing is possible with one sample); R-BUCKET-KB "no-registered-
signatures" (catalogue 1.0 registers none yet). These are all EXPECTED
absences for a first sample, not gaps.

---

## 5. RANKED CANDIDATE FINDINGS FOR PCREC

1. **A DFA-emitter code-generation bug**: `wild-waf-crs-942500-comment-
   obfuscation`'s generated `artifact.c` embeds the pattern's own
   literal byte sequence (`/*!*/`) unescaped inside a generated
   annotation comment, and the pattern's own subject matter (SQL
   comment-obfuscation detection) happens to contain a C block-comment
   terminator — corrupting the rest of the generated file and cascading
   into unrelated compile errors. Refuses on BOTH `auto` arms (DFA
   route), compiles on both forced-VM arms. §2 Finding F, full
   diagnostic quoted from the record. **Concretely reproducible, highest
   confidence, highest value** — a general escaping bug in the DFA
   route's comment emitter, not specific to this one pattern.
2. **The captures axis removes the DFA rescue on classic ReDoS shapes,
   at factors of ×10^5-10^6**: `trim-nested-star` (`^(\s+)*$`) is
   ×214,356 slower with captures required than without, because `auto`
   declines its own nullable-collapse rescue under captures
   (`declined-nullable-default`) and falls to the backtracking-
   vulnerable VM (§1.2 Finding D). `winpath-near-miss` shows the same
   shape at ×242,483 against the forced-VM control. This is a real,
   large-magnitude cost of pcrec's own capture-support boundary on
   exactly the pattern shapes a "capability contrast" set exists to
   surface — worth pcrec's own read on whether the nullable-collapse
   rescue's capture-compatibility can be widened, per [OPT-4.2]'s own
   history on this bench.
3. **`evil-alt-nested` fails three different ways across the roster,
   and pcrec's own hang is the worst of the three**: PCRE2 gives up
   gracefully at its match-limit; `pcre2-dfa` and `pcrec-auto-nocaps`
   silently return a WRONG answer; `pcrec-auto-caps`/`vm-caps`/
   `vm-in-caps` TIME OUT (an uncontrolled hang, worse than either).
   §1.2 Finding C. Whether pcrec has (or should have) an analogous
   match-limit/step-budget on the VM route that this set's `--iters`
   calibration is masking is a direct, answerable question.
4. **`mojibake-curly-quote` is wrong on all four pcrec configs and
   right on all three pcre2 configs** — a raw non-UTF-8-byte handling
   divergence specific to pcrec, on the one pattern this set built to
   probe exactly that (§1.2 Finding A). No span/answer detail is
   expressible from this report (§6.4's own limit); a targeted `quick`
   comparison against the oracle is the natural follow-up, owed to
   whichever lane reads this next.
5. **A second, previously-undocumented `pcre2-dfa` leftmost-longest
   divergence**: `wild-logparse-quotedstring-grok`/`lp-quoted-escaped`
   (§1.2 Finding B) — not one of the six family-11 patterns
   `testees/pcre2/CLAUDE.md` enumerates. Worth adding to that adapter
   note's divergence table rather than leaving it to be rediscovered.
6. **`wild-datetime-datefinder-alternation`'s refusal is captures-
   gated, and the no-captures form compiles at 20,411 code bytes
   against the captures form's 665,080-670,132** (§2 Finding E) — a
   ~32-33× code-size multiplier from captures alone on a single huge
   alternation. Relevant to whether a `-bigcap`-style raised-cap
   testee should be added to this set's roster, or whether pcrec's own
   captures-VM code density for wide alternations has room to shrink
   (this bench's `bench/altwide` set already tracks a related question
   on ordinary alternations without the capture axis).

---

## 6. ASKS, RANKED

1. **Escape (or otherwise sanitize) any pattern-derived literal text
   pcrec's DFA-route emitter writes into a generated C comment**
   (Finding F, §2/§5.1) — `wild-waf-crs-942500-comment-obfuscation`'s
   own diagnostic, quoted in full, is the reproducer.
2. **State whether the nullable-collapse rescue ([OPT-4]/[OPT-4.2]) is
   intended to decline under `--captures` for a nullable, unbounded
   quantifier over `\s`/`.`-class bodies, and if so whether that
   boundary can be narrowed** — `trim-nested-star`'s ×214,356 gap
   (Finding D, §5.2) is the concrete witness; pcrec's own history on
   this bench ([OPT-4.2], `bench/bounded`) already has instrumentation
   for exactly this decision.
3. **Confirm whether pcrec's VM route has (or should adopt) a
   step/time budget analogous to PCRE2's match-limit**, given
   `evil-alt-nested` times out (hangs, from the harness's point of
   view) on every captures-requiring pcrec arm where PCRE2 gives up
   cleanly (Finding C, §5.3).
4. **A targeted look at `mojibake-curly-quote`'s raw-byte matching on
   every pcrec config** (Finding A, §5.4) — this bench can run a
   `quick` comparison against the oracle on request to narrow the
   divergence to a span, which this report's format cannot express.
5. **Add `wild-logparse-quotedstring-grok`/`lp-quoted-escaped` to
   `testees/pcre2/CLAUDE.md`'s `pcre2-dfa` divergence table** (Finding
   B, §5.5) — a bench-side ask (this project's own adapter note), listed
   here because it was found reading pcrec's own roster contrast.

---

## 7. NEXT-SAMPLE CHECKLIST

1. Give `interpret` a subject-grain input for this set's next sample —
   a subject-grain `.tsv` (the committed `.subject-grain.md` is a
   rendering `interpret` does not read), or an `interpret` extension
   over that grain — so P2/P3/P4/P6/P7/P10 become evaluable rather
   than six of ten predictions landing `not evaluable` by construction
   (§3). A catalogue/interpreter design question, not a rendering flag.
2. Re-transcribe P5 with an explicit `section=excluded` clause (or a
   companion `n_wrong` selector that does not default to the `rank`
   section) so a real wrong-answer/give-up/timeout population is
   checked, not silently skipped (§3, P5's false-positive confirm).
3. Add the missing `P9` row to `docs/dev/predictions/capability-0.1-
   first.tsv` (NOTES.md states it; the machine-readable file does not
   carry it) — or record explicitly why it is inexpressible per §6.4.
4. Re-measure `wild-waf-crs-942500-comment-obfuscation` once the DFA
   comment-escaping bug (ask 1) is fixed, on both `auto` arms, to
   confirm the refusal clears.
5. Re-measure `wild-datetime-datefinder-alternation` under a raised-cap
   testee (`-bigcap`-style) if one is added to this set's roster, to
   read the captures-VM form's actual cost rather than its refusal.
6. Follow up `mojibake-curly-quote`'s wrong answer with a `quick`
   comparison against `pcre2-jit` on `nu-mojibake` to narrow the span
   (ask 4).
7. If `evil-alt-nested`'s pcrec-side timeout persists at the next pin,
   read whether a step-limit stamp exists in `rx_info` that this
   adapter could surface as a graceful give-up rather than a harness
   timeout (ask 3).
8. Re-check `router-prefix-order`'s two `large-subject-throughput`
   subjects on `pcre2-dfa` explicitly (§1.1) — clean in this sample,
   but `testees/pcre2/CLAUDE.md` itself calls this an "honest gap" not
   yet closed by review of the pattern's structure, only by this one
   measurement.
9. Confirm §11.4's wall-time model against a SECOND sample before
   revising `CELL_CAP` or the per-cell estimate — one sample's ×3
   overrun (§0.2) is a single data point, though it lands exactly where
   §13 R6 predicted it would (the redos-nested family's throughput
   regime).

---

## Source header (D35 style)

This file is a READING of the committed report and its interpretation
sidecar, never a measurement. Sources: `reports/2026-09-17-capability-
0.1-budu-ryzen1600-first-a770139e.{md,tsv,interpretation.md}` (sha256
stamps in the sidecar's own header, SIDE:1-11), `store/index.tsv` at
commit `44f1607`, `build/windows/window_capability_20260917T005018Z.log`,
`bench/capability/NOTES.md`, `bench/capability/patterns.rxt`,
`bench/capability/CLAUDE.md`, `testees/pcre2/CLAUDE.md`,
`docs/design/capability_set_v1.md`, `docs/dev/predictions/
capability-0.1-first.tsv`, `docs/dev/predictions/CLAUDE.md`,
`docs/design/interpreter_v1.md`. One additional query was run outside
these committed files to recover a diagnostic the report itself
truncates (§2 Finding F): a direct read of `store/records/capability@0.1/
pcrec_a770139e_auto-caps-simdna/capability@0.1__pcrec_a770139e_auto-caps-
simdna__budu-ryzen1600__20260917T020152Z.jsonl`'s `wild-waf-crs-942500-
comment-obfuscation` row's `diagnostic` field, quoted verbatim in §2.
No store file, report, or code was modified by this lane.
