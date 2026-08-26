# bench/email — engine notes, declared variants, and what the numbers mean

Requirements §4.5 and §5: the per-engine notes, the declared variants, and
the statement of what this sub-bench exists to exercise.

## The objective, and what would defeat it

> RFC 5322-shaped email validation: the hand-inlined original and its
> subroutine-factored form; the factored form's objective is
> calls-as-factoring (a testee may not run the inlined original in its
> place).

`orig.rx` and `factored.rx` describe **the same language** — verified,
not assumed: the libpcre2 oracle gives byte-identical answers for the two
patterns on all 330 (pattern × subject × regime) cells this sub-bench
declares (0 disagreements; `gen_expectations.py` re-derives it on every
`make check`). That is what makes the pair a measurement: any difference
a testee shows between `orig` and `factored` is a difference in what the
engine PAYS for the factoring, not in what it is asked to recognise.

So the objective (requirements §4.5 constraint 2) is specifically the
CALLS. A testee that ran `orig.rx`'s text — or any inlining of
`factored.rx`'s four `(?&name)` call sites — in place of `factored.rx`
would reach the same answers and measure nothing: it must report
`unsupported-by-declaration` for the `factored` pattern instead. An
engine with no subroutine-call construct is exactly that case.

## Declared variants: none

Both patterns are canonical PCRE2 spellings and both adapters run the
canonical text byte for byte. Every record therefore carries
`patterns[].variant = null`, which requirements §4.5 requires to be
STATED rather than assumed.

One thing that is deliberately NOT a variant: pcrec's `--features all`.
pcrec's default feature set (`std1`) excludes the `named-groups` and
`recursion` modules, so `factored.rx` is refused under the default with
`requires module 'named-groups'` (MEASURED 2026-08-25 against pin
8da6120, re-verified at 692c2e8). `--features all` is a build/run flag of the TESTEE — it changes
which modules the compiler has, not what the pattern says — and the
pattern text handed to pcrec is identical either way. It lives in
`testees/pcrec/configs.toml` flags and in `testee.build_flags`.

## Per-engine notes

- **libpcre2 (`pcre2-interp`, `pcre2-jit`)** — none needed. libpcre2 is
  the oracle, so it runs the canonical text under the canonical
  semantics by construction. Its `consumed_length` convention is in
  `testees/pcre2/CLAUDE.md`.
- **pcrec (`pcrec-auto`, `pcrec-nocaps`, `pcrec-vm`)** — none needed for
  the patterns. Two behaviours a reader of the numbers should expect,
  both already measured by pcrec's own srEmail lane and neither a
  correctness problem with this sub-bench:
  - **Engine selection moved between pins.** At pin 8da6120 `orig.rx`
    selected pcrec's DFA and `factored.rx` the VM (the `{0}` definitions'
    named groups were captures, which forced VM, with no prefilter). At
    pin 692c2e8 (pcrec wave G: dead-capture elision, prefilter restored
    for call-bearing patterns) **both patterns select the DFA under
    `pcrec-auto` and `pcrec-nocaps`, in both forms** — MEASURED
    2026-08-25, `testees/pcrec/CLAUDE.md` has the table. Only `pcrec-vm`
    still runs a VM artifact here. A before/after of `factored` across
    the two pins compares two engines, not two versions of one.
  - the pathological subjects and the `t-c-long-atom-run` throughput
    subject can exhaust pcrec's step/frame budgets — on a VM artifact.
    At 692c2e8 that is `pcrec-vm` only: five deep subjects (s-058,
    s-059, s-061, s-063, s-064) give up with `PCREC_ERR_FRAMES` on
    `factored` in the match regime (MEASURED); `pcrec-auto` gives up
    nowhere. A budget give-up is recorded as `gave-up` with the give-up
    code in the row's `diagnostic` — see "give-ups" below.

## The match regime runs a SECOND pcrec artifact

pcrec has no end-anchor option, so for the `match` regime its adapter
compiles `(?:<pattern>)\z` as a separate artifact and uses the anchored
entry on it; `search_short` and `throughput` use the plain artifact. The
two never share a row (schema v1.1's `form` enum). libpcre2 needs none of
this — it passes `PCRE2_ANCHORED|PCRE2_ENDANCHORED` as runtime flags on
the one compiled pattern. Full rationale and measurements:
`testees/pcrec/CLAUDE.md`.

For a reader of THIS sub-bench's numbers, three consequences:

1. **pcrec's match-regime compile cost is a different artifact's** from
   its search/throughput compile cost. The record labels which; do not
   reduce them together.
2. **`orig`'s `\z` form still selects the DFA engine** (MEASURED against
   pin 8da6120 and re-verified at 692c2e8, both `pcrec-auto` and
   `pcrec-nocaps`; at 692c2e8 `factored`'s `\z` form does too), so the
   match regime is not secretly measuring the VM for the inlined pattern.
3. **The `\z` form's byte-class skip prefilter is present but weaker**:
   the same `rx_can_begin_match` table, but a skip loop that can never
   skip the final byte and cannot early-exit, because the end-of-subject
   view has to be evaluated. A small per-scan cost difference between
   pcrec's match-regime and search-regime numbers is expected and is
   this, not an engine change.

## Give-ups are wrong answers, not missing ones

**RULED 2026-08-25: schema v1.1 adds a per-subject `gave-up` outcome** —
the engine refused on a resource limit (pcrec `PCREC_ERR_STEPS`/
`_FRAMES`/`_WORK`; pcre2's match or depth limit) — with the engine's own
code in `diagnostic`. It is not timed, and it is counted SEPARATELY from
wrong answers, which is the point: an engine that declined to answer and
an engine that answered wrongly are different findings, and folding them
together would hide the bench's headline hazard class inside a bucket of
ordinary mismatches.

Until v1.1 lands such a row is `did-not-match-as-expected` with
`observed.matched = false` and the code in `diagnostic`. Either way it is
NOT timed (requirements §7: a timing for a wrong answer is worse than no
timing) and the reporter excludes it from rankings and lists it.

A give-up that the sub-bench's notes had DECLARED would instead be
`unsupported-by-declaration`; none is declared here, because a budget is a
configuration, not an inexpressible construct.

## What the expectations are, and are not

`expectations.tsv` carries the first match's SPAN (or `nomatch`) per
(pattern, subject, regime), plus the count of non-overlapping matches
for the throughput regime. Method `libpcre2-differential`, oracle version
recorded in every row (`10.46 2025-08-27` as committed).

**No capture-level expectation is recorded, and that is checked rather
than assumed.** `orig.rx` has no capturing group at all; `factored.rx`'s
four named groups are `{0}` definition groups reached only through
`(?&name)` calls, and a call's return restores every slot the callee
wrote. `gen_expectations.py` verifies on every run that no capturing
group participated in any match, on either pattern, over every subject
and regime, and says so on stderr — if that ever stops being true the
message changes and the claim in this section is stale. The general
capture-correspondence contract stays where requirements §12 puts it:
OD-B9, with the first non-PCRE2 adapter.

## Size and hazard tags

- `size_class` here is the PATTERN's size, banded: `tiny` < 16 B,
  `small` < 64 B, `medium` < 256 B, `large` < 1024 B, `huge` ≥ 1024 B.
  `orig.rx` is 426 B and `factored.rx` 459 B, so both are `large`.
- `hazard_class = exponential-backtracking` for both: the local part's
  `atom+(\.atom+)*` shape is the classic ambiguous-repetition form, and
  the `t-c-long-atom-run` subject (1 MB of `a`, no `@`) is the subject
  that exercises it. A DFA-class engine structurally cannot pay it; a
  backtracking engine can, and that difference is one of the things this
  sub-bench is for.

## Regime coverage

| regime | subjects | semantics | expectations |
|---|---|---|---|
| `match` | all 85 | `PCRE2_ANCHORED\|PCRE2_ENDANCHORED` at 0 | 80 of 170 cells match |
| `search_short` | the 77 of ≤ 256 B | unanchored at offset 0 | first-match span |
| `throughput` | the three 1 MB | unanchored, find-all | first span + count |

The eight subjects over 256 B (the 10 KB local part, the 2000-deep
`a.a.a…`, the 5 KB quoted strings, the 500-label domain, …) are in the
`match` regime only: `search_short` is defined by requirements §3 as
~256-byte subjects, and timing a 10 KB subject in that regime would put
a different cost class in the same column.

## The floor pattern

**What it is.** `patterns/floor.rx` is the one-byte literal `@`, no
anchors, no groups, tagged `role: floor` in the sidecar (schema v1.3,
`docs/design/record_schema.md` 5 ADDITIONS 7). It runs in all three
regimes over the SAME subjects `orig` and `factored` do: `search_short`
(the first `@` found within a handful of bytes on most subjects — that
is the point), `match` (does the WHOLE subject equal `@` — true on
exactly one of the 85, `s-082`, "just @ sign"), and `throughput`
(find-all `@` over the three 1 MB subjects — a memchr-class scan, not a
regex-engine one).

**Why.** pcrecdev1's reading of the first production sample
(`docs/dev/feedback_pcrecdev1_2026-08-25.md` item 1(d)): "a per-call
FLOOR control in every short-subject set (a one-literal pattern on the
same subjects) reported beside the number, so 6.13 us over 77 subjects
(80 ns/subject) reads against the harness's own overhead." Without it, a
set's summed timing has no baseline: is 80 ns/subject mostly the
pattern's own work, or mostly the harness's per-call loop, the driver's
dispatch, and the subject lookup? A one-literal pattern over the same
subject set isolates that overhead — the one component EVERY pattern in
the set pays regardless of what it is matching — so `orig` and
`factored`'s numbers can be read net of it.

**What it is NOT.** A ranking of engines. The floor's own number is
still an engine's number (pcre2's floor is not the same nanoseconds as
pcrec's floor — different dispatch, different loop, different subject
handling), so "engine X's floor is smaller than engine Y's" is a real
finding about per-call overhead, not evidence that X is "faster" at
regex matching; that comparison belongs to `orig`/`factored`, read net
of each engine's OWN floor. The floor is a baseline per (testee,
sub-bench), not a cross-engine handicap.

**How many of the 85 subjects contain `@`.** 80 of 85 (byte-scanned).
The five that do not: `s-040` "invalid missing @ entirely", `s-060`
"pathological: 10KB local part, no @ (forces full scan, nomatch)",
`s-081` "empty subject", `s-083` "no match: random prose", `s-084` "no
match: digits only". (The three 1 MB throughput subjects are separate:
`t-a-valid-addrs` has 40330 `@`s, `t-b-no-at` and `t-c-long-atom-run`
have none.) The expectations derived from the libpcre2 oracle
(`gen_expectations.py`, 495 rows total, up from 330 with two patterns):

| regime | subjects | match | nomatch |
|---|---|---|---|
| `match` (whole-subject `@`) | 85 | 1 (`s-082`) | 84 |
| `search_short` (first `@`) | 77 | 73 | 4 |
| `throughput` (find-all `@`) | 3 | `t-a-valid-addrs`: first span [9,10), 40330 matches | `t-b-no-at`, `t-c-long-atom-run`: 0 matches each |

**MEASURED, scratch tier, under load — direction only, never a
measurement** (`pcrecbench quick --subbench email --pattern floor
--regime search --testee pcre2-jit --vs <pcrec config>`, 2026-08-25,
3 trials x 77 subjects, box shared with the pcrec manager session — both
records came back `inconclusive-load`):

| vs | pcre2-jit median ns/call | pcrec median ns/call | ratio |
|---|---|---|---|
| `pcrec-auto` | 3440.1 | 1467.8 | pcre2-jit 2.34x slower |
| `pcrec-vm` | 3601.9 | 2510.8 | pcre2-jit 1.43x slower |

Both numbers are labelled `tier: scratch` and `status:
inconclusive-load` in their records; they say a DIRECTION (pcrec's
dispatch loop over this one-literal pattern reads faster than pcre2-jit's
on this box, under load, on this pin) and nothing more. A pinned,
quiet-box measurement is what the next full re-pin sample owes the
reporter's `floor: n/a (no floor pattern in this set yet)` note
(`pcrecbench/report.py`, ruling R6) — this sub-bench now HAS one; wiring
it into that column is the reporter lane's ([B14]/[B9]) to pick up.

## Origin

Copied from pcrec `docs/design/subroutines_measurements/email_specimen/`
(read-only). The subject bytes are IDENTICAL to that origin's — verified
by regenerating both and comparing all 88 files — so pcrec's own
oracle-verified results for this corpus carry over.
