# lane `b36read` — the [B36] syntax@0.1 first-sample OUTLIER READ

Branch `lane/b36read`, worktree `worktrees/b36read`, read-only with
respect to `store/`, `bench/syntax/` and `~/pcrec`. Nothing was re-run:
this is a read of the six records commit `28cb034` landed.

## What was produced

**Report group** (three files, `reports/`), rendered from
`~/pcrec-bench/store` at 160 records, reporter `v15 (2026-09-05)`
unchanged, no committed report regenerated:

- `2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.md` (955,983 B)
- `2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.subject-grain.md` (10,153,186 B)
- `2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv` (1,836,213 B)

Query on all three (grain/format aside), explicit `--since`/`--until`
PAIR + the six-id roster per the 2026-08-30 rule and KB-5:

```
report --subbench syntax --version 0.1
  --since 2026-09-07T00:00:00Z --until 2026-09-07T05:00:00Z
  --testee libpcre2_10.46_interp-caps-simdna
  --testee libpcre2_10.46_jit-caps-simdna
  --testee pcrec_d34c9131_auto-caps-simdna
  --testee pcrec_d34c9131_auto-nocaps-simdna
  --testee pcrec_d34c9131_vm-caps-simdna
  --testee pcrec_d34c9131_vm-in-caps-simdna
```

6 records matching, 6 included, 0 superseded. Rendered IN-PROCESS (store
loaded and validated once — **748 s**, the longest yet: this set's records
carry 35,859–41,800 rows each; the three renders then took 118 s).

**Ledger**: `docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md`
(§0 sample, §1 R0, §2 R1, §3 R2, §4 R3, §5 R4/R5/R6/R7, §6 P1–P13 scored,
§7 the I-55 fold-pair ask, §8 the floor, **§9 the twelve ranked
questions**, §10 the next-sample checklist, §11 bench-side follow-ups).

**Directory docs**: a `[B36] reports` wave section at the top of
`reports/CLAUDE.md` and a row in `docs/dev/ledgers/CLAUDE.md`.

Naming note: the brief said `2026-09-06/07-…`; a `/` is not a filename,
and the directory's convention is the LATER date of a window (the
[B34] 2026-09-04/05 window is `2026-09-05-…`). The window's record
timestamps are all 2026-09-07 UTC.

## Findings per rule

| rule | cells | of which questions |
|---|---|---|
| **R0** wrong answers | 9 on `pcre2-jit`, 11 on each pcrec arm (20 distinct) | **3 mechanisms, all three the INSTRUMENT's** |
| **R1** refusal on a built row | 1 pattern (`mod-x`, whole-subject form only) | 1 (the wrapper) |
| — the `unsupported` block | 14 patterns × 2 forms × 4 testees | not ranked |
| **R2** JIT band | 24 on the `auto` route (23 slow, 1 fast), 66 on forced VM, 298 over all five non-JIT testees | 5 ranked (Q4, Q6, Q7, Q8, and `rec-define`'s ×0.040 win) |
| **R3** spelling groups > ×1.5 | 32 group-cells | 3 (`\G`, `(?+1)`, the capture/`shape` pair) |
| **R4** family > ×3 | 133 | folded into Q9 and the anchors (P5) |
| **R5** compile / size cliffs ×10 | **0** | — (P13 confirmed; worst ×2.08 / ×1.90) |
| **R6** engine-selection surprises | 4 REGULAR patterns on the VM + 7 route flips on the capture axis | 2 (Q5, Q7) |
| **R7** sweep outside [0.7, 1.4] | 31 (16 of them P5 working at exactly 0.0625) | 2 (Q9, Q12) |

## The ranked question list (full detail in ledger §9)

**Tier A — the instrument.** Nothing below is trustworthy until these are
answered.

1. **Q1 — the find-all loop reports a mid-loop GIVE-UP as a shorter match
   count.** Nine cells (`rec-r-uc`/`rec-1`/`rec-name` × three runs) read
   `expected 116 non-overlapping match(es); observed 5` on `pcre2-jit`
   AND all four pcrec arms. A read-only ctypes probe on the same subject,
   with the drivers' own advance rule, returns **`PCRE2_ERROR_JIT_STACKLIMIT`
   (−46)** at the sixth start after five spans identical to the
   interpreter's. Both drivers
   (`testees/pcre2/driver.c:321-340`, `testees/pcrec/driver.c:714-731`)
   read `if (rc < 0) { if (count == 0) <giveup> = rc; break; }` — a
   negative return after the first match is discarded. Consequence: five
   of six testees vanish silently from three of the census's 285
   rankings. Falsifiable by distinguishing NOMATCH from other negatives
   and re-running the nine cells.
2. **Q2 — the whole-subject form cannot report a match start other than
   0.** `asr-k-uc` (`key=\K\w+`) / `f-kv` reads `[0,9]` where the oracle
   says `[4,9]`, on all four pcrec arms; libpcre2 answers correctly.
   `testees/pcrec/driver.c`'s anchored branch hard-codes
   `first_s = 0; first_e = (long)r;`. P9 refuted, and the fault is ours.
3. **Q3 — should the `(?:<pattern>)\z` wrapper be built lexically at
   all?** One mechanism, three failure modes across three syntax
   families: P2's `(?R)`-into-the-wrapper wrong answer (confirmed exactly,
   controls clean), `\K` (Q2), and `mod-x` (`(?x) c a t # comment`)
   becoming UNCOMPILABLE because the `/x` comment swallows `)\z`.

**Tier B — general engine mechanisms.**

4. **Q4 — the forced VM anchors `^` and `\A` and does not anchor `\G`.**
   `anc-g-uc` / throughput / `pcrec_d34c9131_vm` = **1,219,696.7 ns/set**
   against `anc-caret`'s **15.1** on the same testee (**×80,784**; report
   line 331), ×11,457 the JIT, flat at 0.886 ns/B over 64 KB / 256 KB /
   1 MB. The `auto` route is unaffected (18.7 ns, `dfa_scan=attempt`).
   **The three forced-VM artifacts' mechanism stamps are IDENTICAL** but
   for `vm_program_bytes` (801/801/814) — the ask that travels with it is
   a stamp that can see this.
5. **Q5 — a CAPTURE requirement moves the route; is the price right in
   every regime?** Seven patterns compile `engine=vm` on `auto` and
   `engine=dfa` on `auto-nocaps` (the one-variable control already in the
   roster). `auto ÷ nocaps` = **match 0.519–0.628** (the VM route ×1.6–1.9
   FASTER), **search 1.181–1.228**, **throughput 1.099–1.158**. 23 of 285
   set cells differ >5 % between the arms; all 23 are those seven.
6. **Q6 — `shape=inline` is ×1.78 FASTER on one pair and ×2.9–5.1 SLOWER
   on another.** Forced VM: `(cat)` `inline` 961,162.7 vs `cat` `forward`
   1,714,697.1 (identical language, verified identical answers). `auto`
   hybrids: `lkb-pos` `inline/frameless=1` 4,033,554.7 vs `lkb-neg`
   `plain/frameless=0` 791,530.2 (×5.09), `lka-pos` vs `lka-neg` ×2.91,
   with the pairs otherwise agreeing on prefilter, offsets, lang and
   frames. `lkb-pos` at `auto ÷ jit` = **×20.06** is the worst `auto` cell
   in the census. The pos/neg hit-density confound is stated in the
   ledger; the ask is an entry-shape deny flag.
7. **Q7 — should a possessive quantifier or an atomic alternation force
   the VM on a finite language?** `(?>a|ab)c` and `a?+a` are REGULAR by
   `pattern_facts.tsv` and take the VM while their twins take the DFA:
   `qnt-poss-quest` throughput 2,005,118.9 vs `qnt-star` 858,659.6
   (×2.34); `grp-atomic-alt` ×1.22 its atomic twin and ×2.46 the JIT;
   `a++ab` ×2.01 `a+ab` on search (P4's refutation). Three of the four
   possessive suffixes take the DFA — the split is not the suffix.
8. **Q8 — why is `dfa_prefilter=offset-set-bounded` a ×2.4 tier?** The
   `auto` route's throughput ratio against the JIT is monotone in its own
   prefilter stamp over six buckets and 55 DFA cells: `none` **0.158** →
   `memchr` **0.728** → `byte-class` **0.997** → `offset-set` **1.286** →
   `offset-set-bounded` **2.441** (six cells in a 2.393–2.719 band —
   `done$`, `done\Z`, `done\z`, `(?m)done$`, `\bcat\b`, `\Bcat\B`).

**Tier C — upstream (libpcre2 10.46).**

9. **Q9 — the interpreter is quadratic on balanced-paren recursion.**
   870.4 → 2,061.6 → **8,704.8 ns/B** over 64 KB → 1 MB (R7 ratio
   10.0–10.4), set total **9.7 s** for 1.3 MB, ×109 the backref family
   (P11 refuted), against a match count that is LINEAR in size. Also:
   `(?+1)` costs its three verified-identical spelling twins ×13.88
   (search) on the interpreter and ×2.24 on the JIT, where pcrec's `auto`
   makes the four call spellings free to **×1.001** (P3 refuted on pcre2,
   held on the ahead-of-time compiler).

**Tier D — the scan tier, where "SIMD would help" is honest.**

10. **Q10 — single-literal scan.** `auto ÷ jit` `lit-cat` **1.534**,
    `it\Nm` 1.608, `cat\s+sat` 2.529 on a `dfa/memchr` artifact. The
    forced-VM half is larger and is a mechanism: `floor` (`#`, a
    full-length miss) is **0.622 ns/B** on `vm` against **0.0177** on
    `auto` (×35.2) and 0.0397 on the JIT, on a `shape=forward prog=236 B`
    artifact carrying **no prefilter stamp at all**. Read beside
    [B35] (9') / O-21.
11. **Q11 — the dense-class cells are the largest cost and pcrec already
    leads them.** `auto ÷ jit` on `\w+` **0.537**, `[[:alpha:]]+` 0.560,
    `(?a)\w+` 0.532. Listed last so the big numbers are not mistaken for
    the open questions. `\p{L}+` / `\P{L}+` / `(?[…])+` are pcrec
    refusals, so those arms are unmeasurable at this pin.
12. **Q12 — `auto`'s per-byte cost rises 1.42–1.74× from 64 KB to 1 MB on
    five sparse-hit patterns; the JIT's does not.**

## Predictions: 9 confirmed, 4 refuted, 1 half-untestable

Full table in ledger §6. The two that reorder a reader's model:

- **P3 REFUTED on libpcre2 and HELD on pcrec-auto** — the clause the
  author was most confident in ("PCRE2 compiles spellings to one opcode
  stream") failed at ×13.88, and the one NOTES called "the prediction with
  the least confidence in this list" held to ×1.001.
- **P5 REFUTED on 2 of 6 testees** — an anchor an engine does not
  recognise is not a cheap cell, it is the most expensive cell in the set.

Also: **P1 scores 13/15** (`esc-hex-braced` compiles — the abi-23 re-seed
working as NOTES foresaw; `mod-x` added on one form), **P13 confirmed**
(R5 fires nowhere), **P2's first clause confirmed to the letter**.

## The I-55 directed ask: the five fold-pair witnesses

Answered on a **controlled quartet** — `lit-cat`, `cls-fold-pair`,
`cls-pair-ctl`, `cls-mixed-case` share identical `pattern_facts.tsv` rows
(`match 1/42`, `search 5/42`, `tput 3/3`, first `c`, required `t`,
min_length 3), and the `auto` DFA route is a natural control because it
cannot see a fold.

`vm_cls_folds` on the forced-VM route: **`mod-i` 3, `mod-r` 3,
`cls-i-class` 2, `cls-fold-pair` 1, `cls-pair-ctl` 0, `cls-mixed-case` 0.**

- An explicit `[aA]` **folds without `(?i)`** — program 560 B vs the
  control's 610, `emit_code_bytes` 17,978 vs 18,029 (−51 B).
- A 52-member class in which every letter's pair is present is **not**
  lowered: the rule is "class of exactly two members that are a fold
  pair", not "class closed under case folding".
- `(?ir)cat` is byte-identical to `(?i)cat` at the artifact (`folds=3`,
  prog 635 both) — `(?r)` inert at this pin, confirmed.
- **`c[aA]t ÷ c[ac]t` on the VM = ×0.796** (throughput) with the DFA
  control at **×1.003**, trial spreads ≤ 0.60 %. In absolute terms
  `c[aA]t` costs **×1.0013** what `cat` costs on the same route: **the
  fold makes a two-member fold-pair class free.**
- Under `(?i)` the ratio inverts by route — the auto DFA's prefilter drops
  `memchr` → `byte-class` and pays ×1.62, the VM's masked compare ×1.26 —
  which is Q8's question, not a selection one.
- Upstream note: libpcre2's JIT special-cases the fold pair harder —
  `c[aA]t` at 436,863.8 is ×0.849 of its own `cat` and ×0.379 of
  `c[ac]t`.

`vm ÷ auto` on the five witnesses, per regime, is in ledger §7.3; the
`match` column is flat at 0.59–0.65 on all five AND on `lit-cat`, so that
column is a route effect, not a fold effect.

## Validation

**COMPLETE for the analysis; the re-render invariant was still running at
handback** (see "What is owed" below).

- Every number in the ledger is derived from the six store records
  (`store/records/syntax@0.1/*/*.jsonl`) via `pcrecbench.reduce`'s own
  `reduce_set_cell` / `reduce_match_cell` / `cells_from_record` — the same
  arithmetic the reporter uses (`pcrecbench/reduce.py`'s module docstring,
  rule R5 of [B10]) — and cross-checked against the rendered report at the
  line numbers the ledger cites.
- The Q1 probe is a scratch-only ctypes script over
  `bench/syntax/throughput/t-64k.bin` and `libpcre2-8`; it writes nothing,
  builds nothing, and touches no repository file. Its output is quoted
  verbatim in ledger §1.1.
- Q2's and Q3's causes were read out of `testees/pcrec/driver.c` and
  `testees/pcre2/driver.c` (line numbers in the ledger), not inferred.

## What is owed

1. **The re-render invariant check had not printed when this lane
   handed back.** It runs as a detached script,
   `<scratchpad>/verify.sh` → `<scratchpad>/verify.log`, and does two
   things: a full `python3 -m pcrecbench report …` CLI invocation of the
   committed `.tsv` query `cmp`'d against the in-process render (CLI
   equivalence), then a second independent in-process render of all three
   files into `<scratchpad>/rerender/` `cmp`'d against the committed ones
   (determinism). Each pass pays the 748 s store validation. The log
   prints `CLI-EQUIV-TSV: OK|FAIL`, three `DETERMINISM <file>: OK|FAIL`
   lines and `VERIFY-DONE`. **The manager should read that log before
   merging**, and the `reports/CLAUDE.md` paragraph this lane wrote claims
   both checks passed — if either says FAIL, that paragraph is wrong and
   the group must be re-rendered.
2. **Not written, deliberately** — they belong to the manager's channels,
   not a read lane's: `docs/dev/known_issues.md` entries for Q1 / Q2 / Q3
   (three KB rows; ledger §11 has the exact source lines), a
   `docs/dev/upstream_findings.md` entry for Q9 (U-class, libpcre2 10.46's
   quadratic recursion + the JIT stack-limit give-up), the
   `docs/dev/outbox_to_pcrec.md` O-n item for Q4–Q8, and the
   `docs/dev/plan.md` [B36] STATE tag.
3. **One correction to `bench/syntax/NOTES.md` is owed** (ledger §11.4):
   "The set has no backtracking hazard by design" is refuted by Q9. Not
   made here — the brief forbade touching `bench/syntax/`.
