# lane b65attrib — [B65] the altwide rung attribution (inbox I-80)

Branch `lane/b65attrib`, worktree `worktrees/b65attrib`. Compile-only;
box was free throughout (bounded 65535-cap census aside, no timing was
taken by this lane at all, so box load never entered it).

## 1. Task

Plan row [B65] / inbox I-80: [B63]'s window found `bench/altwide@0.2`'s
DFA/auto compile-time refusal set shrank from 18 patterns at pcrec
d34c9131 to 4 at 25b1984f (`docs/dev/lanes/b63window_report.md` §3) —
14 newly-compiling patterns. This project's own committed prose
(`reports/CLAUDE.md`, outbox O-40) attributed the shrink to a
**stated-unproven hypothesis**: cf0962e3's `[OPT-DIAL]`/K59 "premul
drop-ladder rung" alone. pcrec's own reading (inbox I-80) corrects
this: the mechanism is `Ctx.size_drop_rung`, a **two-rung** retry
ladder (`RX_ENGINE_SEL "size-cap-retry"`) — rung 1 (K53-SELRETRY,
fixed 2026-09-10: drops the optional anchored match-here machine)
fires first; rung 2 (K59, fixed 2026-09-17: additionally drops the
premultiplied DFA table) fires only where rung 1 alone still
overflows. **`RX_DFA_TABLE "mixed"` is NOT evidence rung 2 fired** —
I-80's own live witness (`ci-512`) reads `mixed` under rung 1 alone.

The brief: identify the 14 patterns by deriving the set from the two
altwide pcrec-auto store records' own compile-row outcomes, re-emit
each with the pinned 25b1984f binary under `pcrec-auto`'s real flags
(the [B58] `-fcomments` protocol token included), record each
compile's `pcrec: note:` line(s) verbatim and the rungs they name, plus
each artifact's `RX_ENGINE_SEL`/`RX_DFA_TABLE` stamps and emit sizes —
attributed from the note lines only, never from `dfa_table` alone.
Deliver the D35 measurement, correct the size-books provenance on the
LIVE surfaces (not the append-only lane report), and draft O-41.

## 2. The 14 patterns, derived (not assumed)

Read both altwide `pcrec-auto` store records' `kind=compile` rows
directly (`store/records/altwide@0.2/pcrec_d34c9131_auto-caps-simdna/
…20260906T162430Z.jsonl` and `…pcrec_25b1984f_auto-caps-simdna/
…20260921T053254Z.jsonl`): a pattern is in the set iff every one of its
d34c9131 compile rows reads `compile_outcome != "compiled"` and every
one of its 25b1984f compile rows reads `compile_outcome == "compiled"`.
That query returns exactly:

    ci-256, ci-512, cnt-64, nar4-512, pfx3-512, sfx-512, sh1-512,
    srt-256, srt-512, w-256, w-384, w-512, wb-256, wb-512

14 patterns — matching b63window_report.md's own list and its
18 − 4 = 14 reconciliation, independently confirmed rather than copied.

Four of the fourteen (`ci-256`, `cnt-64`, `srt-256`, `w-256`) had their
PLAIN form already compiling at d34c9131 (5 of 6 old compile rows
`compiled`, the sixth `did-not-compile`) — only their whole-subject
form was refused. The other ten had BOTH forms refused at d34c9131 (2
of 2 rows `did-not-compile`). Every one of the 28 (pattern, form) cells
compiles at 25b1984f.

## 3. Re-emission and rung attribution

Script: `docs/dev/measurements/probe_altwide_rung_attribution.py`.
Archive: `docs/dev/measurements/2026-09-21-altwide-rung-attribution-
25b1984f.txt`. Method: for each of the 14 patterns, both forms (plain
and `(?:<pattern>)\z`), re-emit with `build/pcrec-25b1984f/build/pcrec`
under the exact argv `testees/pcrec/adapter.py`'s phase 1 sends
(`-p rx -fcomments --features all -o artifact.c -- <pattern>`, the
[B58] `-fcomments` protocol token, per-cell `artifact.c` basename so
byte counts compare directly), pattern text verified against the
pattern's own `canonical_sha256` in the d34c9131 record before
emitting anything, `pcrec: note:`/`pcrec: warning:` lines captured
verbatim from stderr, `RX_ENGINE_SEL`/`RX_DFA_TABLE`/`RX_DFA_MATCH`/
`RX_DFA_PREFILTER`/`RX_ENGINE` read off the emitted `.c`'s `#define`
lines (comments on, so the macros — CODE, not comment text — are
present regardless of [EMIT-VERB]).

**Fidelity check**: every one of the 28 cells' `emit_bytes` (the
warning line's own number) matches the corresponding 25b1984f store
record's `engine_metadata.emit_bytes` byte-for-byte (28/28 — checked
programmatically, not eyeballed). The reproduction is the same
artifact the store's window actually built, not a look-alike.

**Rung classification**: every note line matched one of the two known
texts exactly (K53's "dropped the optional anchored match-here
machine…" / K59's "dropped the premultiplied DFA transition table…").
**Zero STOP-and-flag rows** — no note line was absorbed without a
match.

### The full table (all 28 cells)

| pattern | form | d34c9131 | rungs fired | `engine_sel` | `dfa_table` | `emit_bytes` |
|---|---|---|---|---|---|---|
| ci-256 | plain | compiled | — | selected | premultiplied | 990,153 |
| ci-256 | whole-subject | **refused** (1,045,834 B > 1,000,000) | **[1]** | size-cap-retry | premultiplied | 712,917 |
| ci-512 | plain | **refused** (1,590,488 B) | **[1]** | size-cap-retry | **mixed** | 976,275 |
| ci-512 | whole-subject | **refused** (1,668,864 B) | **[1, 2]** | size-cap-retry | indexed | 686,048 |
| cnt-64 | plain | compiled | — | selected | premultiplied | 839,877 |
| cnt-64 | whole-subject | **refused** (1,108,228 B) | **[1]** | size-cap-retry | premultiplied | 821,464 |
| nar4-512 | plain | **refused** (1,608,641 B) | **[1, 2]** | size-cap-retry | indexed | 491,738 |
| nar4-512 | whole-subject | **refused** (1,673,397 B) | **[1, 2]** | size-cap-retry | indexed | 520,407 |
| pfx3-512 | plain | **refused** (1,089,110 B) | **[1]** | size-cap-retry | premultiplied | 687,458 |
| pfx3-512 | whole-subject | **refused** (1,122,863 B) | **[1]** | size-cap-retry | premultiplied | 710,255 |
| sfx-512 | plain | **refused** (1,332,391 B) | **[1]** | size-cap-retry | premultiplied | 940,558 |
| sfx-512 | whole-subject | **refused** (1,370,237 B) | **[1]** | size-cap-retry | premultiplied | 967,679 |
| sh1-512 | plain | **refused** (1,525,451 B) | **[1]** | size-cap-retry | premultiplied | 964,848 |
| sh1-512 | whole-subject | **refused** (1,577,014 B) | **[1, 2]** | size-cap-retry | indexed | 481,898 |
| srt-256 | plain | compiled | — | selected | premultiplied | 978,112 |
| srt-256 | whole-subject | **refused** (1,033,793 B) | **[1]** | size-cap-retry | premultiplied | 706,900 |
| srt-512 | plain | **refused** (1,578,446 B) | **[1]** | size-cap-retry | **mixed** | 970,257 |
| srt-512 | whole-subject | **refused** (1,656,822 B) | **[1, 2]** | size-cap-retry | indexed | 680,030 |
| w-256 | plain | compiled | — | selected | premultiplied | 978,112 |
| w-256 | whole-subject | **refused** (1,033,793 B) | **[1]** | size-cap-retry | premultiplied | 706,900 |
| w-384 | plain | **refused** (1,432,392 B) | **[1]** | size-cap-retry | premultiplied | 969,481 |
| w-384 | whole-subject | **refused** (1,514,859 B) | **[1, 2]** | size-cap-retry | indexed | 506,680 |
| w-512 | plain | **refused** (1,578,445 B) | **[1]** | size-cap-retry | **mixed** | 970,256 |
| w-512 | whole-subject | **refused** (1,656,821 B) | **[1, 2]** | size-cap-retry | indexed | 680,029 |
| wb-256 | plain | **refused** (1,233,146 B) | **[1]** | size-cap-retry | premultiplied | 798,679 |
| wb-256 | whole-subject | **refused** (1,260,385 B) | **[1]** | size-cap-retry | premultiplied | 816,845 |
| wb-512 | plain | **refused** (2,345,817 B) | **[1, 2]** | size-cap-retry | indexed | 905,831 |
| wb-512 | whole-subject | **refused** (2,395,032 B) | **[1, 2]** | size-cap-retry | indexed | 926,030 |

**Totals**: 4 cells never needed a rung (the 4 patterns' plain forms,
already compiled at d34c9131); of the 24 rescued cells, **15 fire rung
1 (K53) only** and **9 fire both rungs**. Rung 2 NEVER fires alone —
consistent with I-80's ordinal/compose statement.

**The `dfa_table=mixed` caution, reproduced on THREE witnesses, not
just I-80's own one**: `ci-512` plain, `srt-512` plain, and `w-512`
plain all read `RX_DFA_TABLE "mixed"` under **rung 1 alone** (one note
line each). Reading `mixed` as premul-rung evidence would have
misattributed all three.

## 4. Size-books provenance correction (LIVE surfaces only)

`reports/CLAUDE.md` carried the K59-only hypothesis in two places (the
[B63] altwide report-group entry's headline finding, and the bounded
window's negative-result paragraph that names it in passing). Both
corrected in place, citing I-80 and this measurement:

- The altwide entry's mechanism sentence now states the two-rung
  ladder, the ordinal rule, the `mixed`-is-not-evidence caution
  (reproduced on `ci-512`), and points at this file's archive for the
  full table.
- The bounded window's negative-result paragraph (which found bounded's
  own class-ladder DFA tables did NOT move under whatever rescued
  altwide) now names `Ctx.size_drop_rung` rather than "the K59
  premul-drop-ladder mechanism" — its actual finding (neither bounded
  witness ever refused at d34c9131, so neither rung had a cap to retry
  against) is unchanged, only the mechanism's name is corrected.

`testees/pcrec/CLAUDE.md`'s 25b1984f pin paragraph does not discuss the
altwide boundary at all (it is scoped to [EMIT-VERB]/D112 only) — no
edit needed there. Its EARLIER cf0962e3 paragraph already names BOTH
rungs correctly on the `wb-512` witness ("the [K53-SELRETRY] anchored
match-here machine drop AND K59's new premultiplied-table drop, each
with its own `pcrec: note:` line") — that paragraph was already right
and is untouched.

`docs/dev/lanes/b63window_report.md` is append-only lane history per
the boilerplate — NOT edited; it still reads "cf0962e3's own
`[OPT-DIAL]`/K59 'premul drop-ladder rung'" as its own contemporaneous
reading, which is now superseded by this file and the corrected
`reports/CLAUDE.md`, exactly as lane-history entries are meant to be
read (a snapshot of what was known then, not a live surface).

## 5. Deliverables

1. `docs/dev/measurements/2026-09-21-altwide-rung-attribution-
   25b1984f.txt` + `probe_altwide_rung_attribution.py` beside it —
   DELIVERED, committed. Every one of the 14 patterns accounted for
   (28/28 cells), zero STOP-and-flag rows, `docs/dev/measurements/
   CLAUDE.md`'s index entry added.
2. The size-books provenance correction — DELIVERED on the two live
   `reports/CLAUDE.md` spots that carried the hypothesis; confirmed no
   other correction is owed in `testees/pcrec/CLAUDE.md`.
3. This lane report + the O-41 outbox draft below — DELIVERED.

## 6. Charter-vs-committed checklist

- Derive the 14-pattern set from the two store records' compile rows —
  DONE, §2, independently reconciled against b63window_report.md's own
  count (not copied from it).
- Re-emit each with the pinned binary under `pcrec-auto`'s real flags
  incl. `-fcomments` — DONE, §3; fidelity proven (28/28 emit_bytes
  match the store byte-exactly), not merely asserted.
- Record note lines verbatim, attribute rungs from them ONLY (never
  `dfa_table` alone) — DONE, §3's table; the `mixed`-is-not-evidence
  caution reproduced on three witnesses.
- Stamps + emit sizes per cell — DONE, table columns.
- STOP-and-flag any unrecognised note line — DONE, zero fired; the
  script's own classifier would have flagged one had it appeared.
- Size-books provenance correction on LIVE surfaces, citing I-80 +
  measurement, lane report/outbox left untouched — DONE, §4.
- Lane report with table + checklist, O-41 drafted (not sent) — DONE,
  this file + §7 below.
- Do not merge — the manager merges.

Nothing OWED.

## 7. O-41 (DRAFTED — the manager sends it)

---

**O-41 (2026-09-21, this session) — [B65] THE RUNG ATTRIBUTION DONE:
your I-80 correction CONFIRMED on all 14 rescued patterns, 28/28 cells,
byte-exact against the store; our O-40 "K59 alone" hypothesis was
wrong and is corrected**

Re-emitted all 14 altwide patterns [B63] found newly-compiling
(d34c9131 → 25b1984f), both forms, through the pinned 25b1984f binary
under `pcrec-auto`'s real argv, and read the `pcrec: note:` line(s) off
each compile verbatim. Your `Ctx.size_drop_rung` two-rung account
(I-80) is confirmed exactly: rung 1 (K53) fires on EVERY one of the 24
rescued cells (15 alone, 9 with rung 2 following); rung 2 (K59) never
fires without rung 1 having fired first, matching the ordinal/compose
rule. Our own O-40 hypothesis — crediting the shrink to "K59's premul
drop-ladder rung" alone — is WRONG and corrected in our committed
`reports/CLAUDE.md`, citing this measurement
(`docs/dev/measurements/2026-09-21-altwide-rung-attribution-
25b1984f.txt`).

Your `dfa_table=mixed`-is-not-evidence caution reproduced on THREE
witnesses, not just your own `ci-512`: `ci-512`/`srt-512`/`w-512`
plain all read `mixed` under rung 1 ALONE — reading `mixed` as premul
evidence would have misattributed all three.

Fidelity: every one of the 28 cells' `emit_bytes` matches the store's
own committed 25b1984f records byte-for-byte, so this is the same
artifact the window actually built. Zero note lines fell outside your
two known texts.

Nothing further asked; this closes [B65] on our side.

---
