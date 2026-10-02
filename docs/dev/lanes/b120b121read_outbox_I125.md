# DRAFT — a whole answer to inbox I-125 (for the manager; not written to outbox_to_pcrec.md)

Full derivation: `docs/dev/ledgers/2026-10-02-b120-b121-fc719ca4.md`.
This supersedes lane `b121asks`'s own draft
(`docs/dev/lanes/b121asks_outbox_draft.md`) now that A5's real window
has run — the numbers below are the WHOLE answer to I-125's A1-A5 and
the 12 bench-only questions, carrying forward everything from that
draft that is unchanged and replacing A2(2)/A2(3)/A4's own ratios and
A5's own status with real numbers, plus the two corrections the manager
asked for on Q5/Q12.

---

**A1/Q1 — unchanged, already satisfied.** `bench/email`'s
`t-d-prose-sparse-addrs` ([B17], email-specimen@0.2) is the non-periodic
1 MiB address-bearing subject: 496 matches on `orig`, generator
`gen_throughput_subjects.py`'s `build_prose`, seed 20260828, sha256
`d55c0e8f...9d94242`. The timed cell is now IN HAND (email-specimen
@0.2's own A5 re-measure, below) — `orig`/`pcrec-auto`/find-all against
`pcre2-jit`/`rust` at this pin, same report.

**A2(1)/Q7 — unchanged.** One real `(?:ab){m,n}`-shaped counted repeat
corpus-wide: `bench/utf8`'s `qnt-counted-3b`, `(?:日本){2,}`.
`bench/bounded`'s `nest2-*`/`nest3-*` family is a DIFFERENT mechanism
shape (`(?:CLASS{p,q}){m,n}`), confirmed by a real structural parse.
Ask stands: is [OPT-5]'s period-k trigger meant for the nest family's
own shape, or specifically the literal-string repeat?

**A2(2) — the timed ratio is now IN HAND, and it INVERTS your own
framing.** `qnt-counted-3b`, large-subject-throughput, ns/B (1,638,400 B
total across the seven throughput subjects):

| testee | ns/B |
|---|---|
| `pcrec-auto`/`pcrec-nocaps` (DFA) | **0.0890** |
| `pcrec-vm` (forced) | 2.6407 |
| `pcre2-jit` | 1.4858 |
| `re2-utf8` | 1.6200 |
| `oniguruma-utf8` | 0.2792 |
| `vectorscan-block-nosom-utf8` | 0.0457 |
| `rust-default` | **0.0407 (fastest)** |

Your own question was "is the DFA scan-edge ladder losing to the VM's
counter loop on this shape?" — **no: `auto`'s DFA route is already
×29.7 faster than forced VM** on this one witness, and only ×2.19/×1.95
behind the two fastest algorithmic engines (rust, vectorscan). If
[OPT-5]'s period-k mechanism is built, it needs to beat your OWN
already-dominant DFA route here, not rescue a losing position.

**A2(3) — the timed ratio is now IN HAND: flat, confirms the standing
reading.** All eleven loglines@0.1 patterns, both regimes, default vs
`-fno-scan-edge`: max move 1.44% (on `iso-ts`, the one pattern with a
real 8-search/4-match scan-edge stamp), inside this project's own
same-pin repeatability floor (~1.32%, measured previously). No cost,
no win, at this pin — confirms this repo's standing reading ("the scan
edge is a spelling-not-count decision with no measured win").

**A3/Q6 — unchanged, confirmed, one witness.** `wild-waf-crs-942360-
concat-sqli` is still the only non-top-level-`^` pattern corpus-wide
(real structural parse, zero parse failures). Stays a single-witness
candidate.

**A4/Q8 — the timed ratio is now IN HAND, and it is far larger than the
compile-only census alone implied.** `altwide@0.3`'s class-tail family
vs the plain ladder at the same width, forced-VM route:

| width | regime | plain ladder (VM) | class-tail (VM) | ratio |
|---|---|---|---|---|
| 64 | thr | 13,402,239 ns | 338,564,367-339,074,641 ns | **×25.3** |
| 256 | thr | 16,570,802 ns | 2,089,207,567-2,091,659,410 ns | **×126** |
| 64 | match-compliance | 365.5 ns | 12,567.7 ns | **×34.4** |
| 256 | match-compliance | 408.6 ns | 93,634.3 ns | **×229** |

**Your own P20 prediction is confirmed, at a far larger margin than
the compile-only stamps alone suggested**: the class-tail shape pays
the VM's serial-try chain cost, not the shared-trie island cost — at
width 256 the forced-VM route is two orders of magnitude slower than
the plain ladder's own island arm. `auto` routes identically to the
plain ladder (DFA, same prefilter, ≤0.5% apart in timing — P21
confirmed) and 0/all cells read a wrong answer (P19 confirmed). We did
not have a `pcrec-vm-noisland`-on-altwide@0.3 arm in this window's own
roster, so the EXACT control your ask names (class-tail forced-VM vs
`w-256`'s own DENIED-island VM arm) is not directly measured — the
comparison above is against `w-256`'s real DEFAULT VM arm, which
already HAS the island, so the ×126-229 figure is a LOWER bound on the
island's own contribution. Say if you want that exact control built
next.

**Q2/Q3 — unchanged in substance; Q3's "reverse population" is now
CONFIRMED empty in TIMING too, not only in compile identity.** Direct
timing comparison on every (pattern,regime,form) cell where BOTH
`pcrec-dfa-nocaps` and `pcrec-auto-nocaps` rank: 191 common cells on
syntax@0.1 (ZERO movers >5%), 83 on capability@0.1 (2 movers, both at
the ~20-30 ns timer-floor scale on program-identical artifacts — noise,
not a real difference). **Nowhere does forced-DFA beat `auto`, on
either corpus, in real timing** — `auto` already picks the DFA
whenever it can represent the pattern, and the two are the same
artifact wherever both compile.

**Q4 — unchanged.** `lka-neg` is match-dense, `lka-pos` match-sparse,
by ~60-110×.

**Q5 — the manager's correction, replacing our own earlier reasoning.**
The citation `esc-octal-0 1.047×` still could not be located verbatim;
asking you to name the report/date/testee. **The SUBSTANCE is
different from what we first wrote**: it is not the v1.4 trial-
agreement gate that puts a pinned record's small ratios above O-69's
floor — it is that a PINNED cell runs under `taskset` on its OWN target
core with each measured loop calibrated to >= 50 ms (`pcrecbench/
harness.py`'s Contract 3, `TARGET_LOOP_SECONDS`; `quiet.taskset_
prefix(pinning)` sets the CPU affinity before the driver launches), so
it is structurally NEVER exposed to O-69's single-process-LAUNCH
governor lottery the way a one-shot scratch probe is — this lane's own
Step 0 measurement proved exactly this mechanism directly (pinning a
launch to one core removes the bimodal split entirely, 0/15 slow
launches either arm, where unpinned launches split 71%/7% fast-state
draws). A ratio in the 1.03-1.23× range on a `measured` pinned record
is therefore not comparable to a raw single-launch artifact at all,
for a structural reason (CPU pinning + long calibrated loops), not
because the statistical gate happens to catch contamination after the
fact.

**Q9/Q10 — unchanged.** No DD-13 consumer; `floor` still collides
cross-set only. `bench/capability@0.1` declares no `match` regime at
all — a realistic (1 KiB-64 KiB) match-regime subject for the 17
capture-forced hybrids is a real ask, not built here.

**Q11 — answered in our I-124 answer (item 2).** `lka-pos` is a
syntax@0.1 cell; the window measured it under auto, the reseed denial
and forced-VM.

**Q12 — the manager's correction.** Citing I-35 precisely: Frank's
ruling (inbox I-35, 2026-09-02) is "your blocking measurement windows
run overnight; pcrec's lanes, `make test` runs and union batteries run
during the day, one heavy suite at a time" — our own daytime BUILD work
(serial compiles, `make check` bursts) is load, not a hold. That
partition is already in force; no separate non-colliding slot needed to
find. This window ran 2026-10-01T14:36→2026-10-02T04:22 EDT at the unchanged
fc719ca4 pin, starting by day only because your I-126 handed us the box
through [B117]; the standing partition is otherwise unchanged.

---

**A5 — the standing re-measure RAN.** 20 A5 cells (of the window's 26),
19 measured at attempt 1 (`syntax`'s `pcrec-vm-nocaps` cell `inconclusive-spread` TWICE — see
below). Seven report groups committed:
`reports/2026-10-02-{syntax,capability,utf8}-0.1-...-fc719ca4.{tsv,md}`,
`reports/2026-10-02-{loglines-0.1,bounded-0.3,email-specimen-0.2,
altwide-0.3}-...-fc719ca4.{tsv,md}`, each with an interpreted sidecar.
Full per-cell numbers in the ledger.

**One real finding beyond the ask: `syntax`'s `pcrec-vm-nocaps` has NO
`measured` record at this pin**, and the ONE re-measure `run_window.sh`'s
own rule allows did not fix it. Re-derived directly from both record
JSONLs (not merely the report's "worst group" summary): the SAME TWO
groups disagree both times — `cls-h` (`key\h*=\h*value`, match-
compliance/whole-subject, a sub-microsecond-per-call VM class scan
likely susceptible to ordinary trial noise at that scale: d went
28→39 of 42 on the retry, i.e. WORSE) and `rec-define`
(`(?(DEFINE)(?<d>\d{2}))(?&d):(?&d)`, large-subject-throughput/plain —
a genuine recursion/subroutine-call pattern on three multi-millisecond
subjects, median 13.24 ms with an 11.44-13.26 ms per-trial RANGE, a
real ~14% run-to-run coefficient of variation that is not a timer-floor
artifact: d stayed 2-3 of 3 both times). If you want `pcrec-vm-nocaps`
at `measured` status on syntax@0.1, this cell needs more trials or a
longer per-trial budget specifically on `rec-define`-shaped recursion
patterns — not pursued further in this lane.

Nothing in this item changes a pinned tier or a pin; the window itself
already ran under the normal pinned-tier contract (quiet gate, 5
trials, v1.4 agreement).
