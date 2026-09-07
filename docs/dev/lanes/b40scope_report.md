# [B40] scope check — does KB-13 or KB-14 explain any PRIOR store anomaly?

Lane `b40scope`, 2026-09-07. Read-only: no driver, schema, or store change.
Method: query `store/` directly with a small one-off python script (no
committed tool added — the queries are inline in this report and reproducible
from the counts given).

## Fresh anomaly counts

Full-store scan of every `kind == "match"` row across all nine
`store/records/<subbench>@<version>/` trees (1,507,285 match rows total):

| `match_outcome` | count |
|---|---|
| `matched-as-expected` | 1,506,630 |
| `gave-up` | 360 |
| `wrong-span-or-captures` | 245 |
| `timed-out` | 30 |
| `did-not-match-as-expected` | 20 |

These match wake.md's 2026-09-07-morning figures (245 / 20 / 360) exactly —
the store has not grown since. (`timed-out`, 30, is out of scope for both
KB-13 and KB-14 and not investigated further here.)

## KB-13 scope (find-all mid-loop give-up masked as a shorter count)

**Regime scope, confirmed against source, not assumed**: `--find-all` is
passed by both adapters (`testees/pcre2/adapter.py:243-244`,
`testees/pcrec/adapter.py:3525-3526`) if and only if `regime == "throughput"`
(record enum `large-subject-throughput`). `search_short` and `match` never
invoke find-all. Every `bench/*/subbench.toml` declares `throughput` as a
regime (`altwide`, `bounded`, `email`, `loglines`, `syntax` all do), so the
loop is exercised store-wide, not just in syntax.

**Where the bug can surface in a record**: `pcrecbench/harness.py:177-183`
flags `regime == "throughput"` count mismatches as `wrong-span-or-captures`
with diagnostic `"expected %d non-overlapping match(es); observed %d"` —
this is NOT silent at the harness level; the harness DOES compare
`row.nmatches` against `expectation.nmatches` and flags a disagreement. What
KB-13 makes silent is the *driver's own attribution* — the record correctly
shows a mismatch, but gives no way to tell "genuinely fewer matches" from
"the loop gave up mid-way" (no `gave-up` outcome, no diagnostic naming a
limit code). So the query for KB-13-affected records is: every match row
with `match_outcome == "wrong-span-or-captures"` and a diagnostic containing
`"non-overlapping match"`.

**Result: 225 rows, 45 unique (subbench, testee, pattern, subject, regime)
cells, ALL in `syntax@0.1`, none elsewhere.**

The 45 cells are exactly the 9 (pattern × subject) combinations named in
KB-13 (`rec-r-uc`/`rec-1`/`rec-name` × `t-64k`/`t-256k`/`t-1m`) × the 5
testees named there (`pcre2-jit`, `pcrec-auto`, `pcrec-auto-nocaps`,
`pcrec-vm`, `pcrec-vm-in`) × 5 trials = 225. No new cell, no other
sub-bench, no testee beyond the five already named in
`docs/dev/known_issues.md` KB-13 and ledger
`docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md` §1.1.

**Second check (the "silent" case named in the brief)** — a record whose
`nmatch` is lower than the oracle's expected count but carries NO flag at
all (i.e. `matched-as-expected` despite an undercount): this would require
`expectation.nmatches` or `row.nmatches` to be `None` on a throughput row
(the harness's guard `if ... nmatches is not None ... nmatches is not None`
at `harness.py:177-178` — the check is skipped entirely when either side is
absent). No such row exists: every `wrong-span-or-captures` row in a
`large-subject-throughput` regime store-wide carries the
`"non-overlapping match(es)"` diagnostic (i.e., the "both sides populated,
mismatch fires" path is the only one ever taken in this store) — so there is
no silently-passing undercount to report.

**`gave-up` records structurally excluded from KB-13**: 135 of the 360
`gave-up` rows are in `large-subject-throughput` regime (the rest,
225, are `match-compliance` give-ups, irrelevant to find-all). Per
`testees/pcrec/driver.c:714-719` and the mirrored pcre2 loop
(`testees/pcre2/driver.c:321-340`), `giveup`/`rc_final` is set **only** when
the negative return arrives at `count == 0` — i.e. every `gave-up` row in
this store is, by construction of the source the harness ran, the
first-attempt case KB-13 does **not** affect (a mid-loop give-up with
`count > 0` cannot produce a `gave-up` outcome — it silently shortens
`nmatch` instead and is caught by the wrong-span-or-captures path above).
This find-all loop shape has been unchanged in both drivers since their
original commits (`testees/pcrec/driver.c` since `a0ac4e0` [B3];
`testees/pcre2/driver.c` since `91e9575` [B3] — `git log --follow` on both
files shows no rewrite of the find-all/anchored branches between then and
now), so this holds for every pre-syntax pin too. The 135
`large-subject-throughput` `gave-up` rows are spread across
`email-specimen@0.1`, `email-specimen@0.2` and `altwide@0.2` (5 different
pcrec pins from `692c2e8` through `1989c62`, all `vm`/`vm-in` testees) —
none of them are misattributed; they are all correctly-flagged first-call
give-ups (mostly `PCREC_ERR_FRAMES` on the VM route, per [B3]'s commit
message and the `pcrec-auto has zero give-ups on bench/email` line in
`docs/dev/outbox_to_pcrec.md:78`).

**Conclusion for KB-13**: zero prior-sample records are misattributed. Every
KB-13-signature record in the store was created THIS SESSION by
`bench/syntax@0.1`'s first sample, and is already correctly attributed in
`docs/dev/known_issues.md` KB-13, the ledger, and `reports/CLAUDE.md`
(quoted below).

## KB-14 scope (pcrec whole-subject match START hard-coded to 0)

**Where the bug lives**: `testees/pcrec/driver.c:676` sets
`anchored = !strcmp(mode, "match")` — the buggy branch
(`first_s = 0` hard-coded, `testees/pcrec/driver.c:710`) fires for **every**
pcrec record in `match-compliance` regime (record enum for the `match`
short name), regardless of the schema's `form` field (`plain` vs
`whole-subject`) — `form` only says which *compiled artifact* was measured,
not which driver branch ran. The brief's framing ("whole-subject form") is
the common case but not the only one the source-verified bug touches; I
queried both `form` values to be safe.

**Query**: every pcrec `match-compliance`-regime row with
`match_outcome == "wrong-span-or-captures"`.

**Result: 20 rows, 4 unique (subbench, testee, pattern, subject, form)
cells, ALL in `syntax@0.1`:**

```
syntax@0.1  pcrec_d34c9131_auto-caps-simdna     asr-k-uc  f-kv  whole-subject  "expected span [4,9]; observed [0,9]"
syntax@0.1  pcrec_d34c9131_auto-nocaps-simdna   asr-k-uc  f-kv  whole-subject  "expected span [4,9]; observed [0,9]"
syntax@0.1  pcrec_d34c9131_vm-caps-simdna       asr-k-uc  f-kv  whole-subject  "expected span [4,9]; observed [0,9]"
syntax@0.1  pcrec_d34c9131_vm-in-caps-simdna    asr-k-uc  f-kv  whole-subject  "expected span [4,9]; observed [0,9]"
```

This is exactly the one witness already named in KB-14 (`asr-k-uc`/`f-kv`,
pattern `key=\K\w+`, `\K` present) × the 4 pcrec testees × 5 trials = 20.
**Both checks the brief asks for agree**: the pattern contains `\K`, and the
disagreement is exactly the predicted shape (reported start 0, oracle's
expected start 4 > 0). No other pcrec `wrong-span-or-captures` record exists
anywhere in the store — `225 (KB-13) + 20 (KB-14) = 245`, the store's entire
`wrong-span-or-captures` population. There is no record where a pattern with
`\K`/lookbehind produced a `wrong-span-or-captures` disagreement that does
NOT match the predicted shape, and no `wrong-span-or-captures` record on a
pattern without `\K`/lookbehind — nothing to rule out beyond confirming
these four cells match on both counts.

**Ruled out, not KB-13/KB-14**: the 20 `did-not-match-as-expected` rows (the
third anomaly bucket) are all `rec-r-uc` / `f-parens` /
`match-compliance` / `whole-subject`, diagnostic `"expected match, observed
nomatch"`, on the same 4 pcrec testees × 5 trials. This is **KB-15**, not
KB-13 or KB-14: `rec-r-uc` is `\((?:[^()]|(?R))*\)`
(`bench/syntax/subbench.toml`/ledger §1.3, Q3/P2), and the wrapper's `(?R)`
recurses into the `(?:...)\z` wrapper itself rather than the bare pattern —
a real wrong answer from the wrapper design question KB-15 already opens,
confirmed word-for-word in the ledger (`docs/dev/outbox_to_pcrec.md:168`,
"P2 ✓ ... the wrapper changes two answers, `(?R)` and `(*ACCEPT)`"). Named
here only for completeness of the anomaly-count reconciliation (245 + 20 +
360 accounted for in full: 245 = KB-13(225) + KB-14(20); 20 = KB-15; 360 =
135 throughput first-call give-ups (KB-13-immune, see above) + 225
match-compliance give-ups (real resource-limit give-ups, unrelated to either
bug)).

## Cross-reference against committed reports and outbox

Every `wrong-span-or-captures` and `did-not-match-as-expected` record in the
entire store belongs to `bench/syntax@0.1`, which did not exist before this
session (`[B36]` merged 2026-09-06, first sample measured and read
2026-09-07 — the same day this scope check runs). No sub-bench measured
*before* today (`email-specimen@0.1/0.2`, `loglines@0.1`, `bounded@0.1/0.2/
0.3`, `altwide@0.1/0.2`) has a single `wrong-span-or-captures` or
`did-not-match-as-expected` record in it — so no report committed before
today could possibly have drawn a conclusion from a KB-13/14/15-affected
row, because no such row existed yet.

Checked directly:
- `docs/dev/outbox_to_pcrec.md` O-22 (2026-09-07, the syntax@0.1 read) —
  already states, in its own words: *"the top three (find-all give-up
  mis-reported as a shorter match count, a driver hard-coding the
  whole-subject match start to 0, and a lexical `\z`-wrapper reaching
  `(?R)`/`\K`/`(?x)`) are OUR OWN test-driver bugs, filed as
  docs/dev/known_issues.md KB-13/14/15 — not sent here, not yours."* This
  conclusion is correct and needs no caveat.
- `reports/CLAUDE.md` (the wave-level reader's-caveat section for
  `2026-09-07-syntax-0.1-*`) already carries the exact finding verbatim,
  including source line numbers (`testees/pcre2/driver.c:321-340`,
  `testees/pcrec/driver.c:714-731`) and the ranking impact ("report line
  5229 ranks the interpreter alone, flagged `dominated`"). No caveat needed.
- `reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.md` itself:
  the reporter's own table (line 5512, `gave-up`/`wrong` count columns) is a
  mechanical pass/fail tally, not a causal claim — it correctly shows the
  anomaly counts without asserting a cause, so nothing in it is wrong; the
  causal attribution lives in the ledger/outbox/CLAUDE.md layer checked
  above, which already has it right.
- All other `reports/*.md` files that mention `gave-up`/`giveup` in a
  legend or `pcrec-auto has zero give-ups on bench/email` (outbox line 78)
  are about `match-compliance`-regime or first-call `large-subject-
  throughput` give-ups — both outside KB-13's reach per the driver-source
  argument above — so no caveat applies to them either.

No committed report or outbox item needs a correction.

## Bottom line

**The store's existing conclusions are safe.** Both bugs are real and stay
OPEN (this is not a fix), but their reach in `store/` is exactly the set of
records already known and already correctly captioned: KB-13 explains all
225 of the store's `large-subject-throughput` `wrong-span-or-captures`
rows (45 cells, 5 trials each, all in `syntax@0.1`) and KB-14 explains the
remaining 20 `wrong-span-or-captures` rows (1 cell, 4 testees, 5 trials,
also `syntax@0.1`) — together the *entire* 245-row `wrong-span-or-captures`
population, with zero rows left over and zero rows in any other sub-bench.
Every `gave-up` record in the store (360, spanning five pre-syntax pcrec
pins on `email-specimen` and `altwide`) is structurally immune to KB-13 by
the driver's own source (give-up is only ever stamped at `count == 0`), and
the 20 `did-not-match-as-expected` rows are a third, already-filed bug
(KB-15) unrelated to either. Nothing in `reports/` or
`docs/dev/outbox_to_pcrec.md` drew a conclusion from a misattributed record;
the one place these findings are narrated (this morning's `O-22` and
`reports/CLAUDE.md`) already states the correct attribution.
