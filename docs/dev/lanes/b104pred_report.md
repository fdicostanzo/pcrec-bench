# lane b104pred report — predictions for [B104]'s I-112 window (751b9c6d)

**Task**: write the PREDICTIONS for [B104]'s window (docs/dev/plan.md [B104];
inbox I-112, `docs/dev/inbox_from_pcrec.md`, read in full), committed BEFORE
any cell runs. Mirror the format and discipline of the last predictions lane
(`docs/dev/lanes/b101pred_report.md`) and `docs/dev/predictions/` (TSV schema,
scoring conventions).

**Branch**: `lane/b104pred` (worktree `worktrees/b104pred`), off master
`d213e75` (NOT off `lane/b104repin`, which was not yet merged when this lane
started — the re-pin's own facts were read from that branch read-only via
`git show lane/b104repin:...`, never merged or built from here).

## 0. What the window is, and what this file predicts

The window (per [B104]'s plan row and inbox I-112) is TWO things at the SAME
pcrec pin, 751b9c6d (abi 39), one night:

1. **utf8@0.1's O-60 acceptance re-measure** — the `-e utf8` lit-* surface,
   split by whether each subject CONTAINS the pre-check's own scanned byte
   (I-112's own ask, for the [OPT-LITSCAN] F3 attribution).
2. **O-62 §2-6's pcrec-only re-measure** — email-specimen@0.2, loglines@0.1,
   bounded@0.3, altwide@0.2, syntax@0.1, the four canonical pcrec configs
   only, against the existing 25b1984f fullroster baseline (O-62's own
   framing: "this is a REFRESH from abi 27, so we make no per-cell
   predictions" except one hypothesis, syntax's anc-z-lc/anc-dollar).

Six files, one per set (utf8 combined; email/loglines/bounded/altwide/syntax
each their own, per the b63/b64 window precedent for a multi-set wave):

- `docs/dev/predictions/utf8-0.1-b104-751b9c6d.tsv` — 18 clause rows / 5
  parents.
- `docs/dev/predictions/email-specimen-0.2-b104-751b9c6d.tsv` — 4 rows.
- `docs/dev/predictions/loglines-0.1-b104-751b9c6d.tsv` — 4 rows.
- `docs/dev/predictions/bounded-0.3-b104-751b9c6d.tsv` — 4 rows.
- `docs/dev/predictions/altwide-0.2-b104-751b9c6d.tsv` — 4 rows.
- `docs/dev/predictions/syntax-0.1-b104-751b9c6d.tsv` — 6 rows (the extra
  two are I-112's own anc-z-lc/anc-dollar hypothesis).

Both `docs/dev/predictions/CLAUDE.md`'s "Files" section and the two archived
probes below are committed alongside.

## 1. utf8@0.1 — the lit-* CONTAINS-LITERAL split (I-112's own ask)

I-112's own instruction: classify every (lit-* pattern × subject) as
CONTAINS-LITERAL vs NOT, using "the pattern matches in the subject, or the
pre-check byte ... occurs in it — derive both and say which rule you used".
Both rules were derived (`docs/dev/measurements/probe_b104_utf8_litcontains.py`
→ `2026-09-27-b104-utf8-litcontains-census.txt`, 686 cells = 7 patterns ×
98 subjects, both regimes):

- **Rule A** (oracle match): `bench/utf8/expectations.tsv`'s own `expected`
  column.
- **Rule B** (byte occurrence): the single pre-check byte I-112 stamped by
  value at 751b9c6d (from `b104repin_report.md` §0.4) present anywhere in
  the subject's raw bytes (regenerated from the committed generators,
  reproduced byte-identical against the committed manifests before
  classifying).

**A=yes/B=no is impossible by construction** (a full match necessarily
contains the scanned byte, one of the literal's own bytes) — checked: **0**
of 686 cells. **A=no/B=yes is real and large** (68 cells): a false-positive
byte hit with no full match, exactly the population the pre-check's own
false-acceptance cost lives in.

**Beyond I-112's own ask**, this lane also derived the SAME Rule-B
classification at the OLD (ce658cb7, abi 33, leftmost-byte) scan position,
so every cell gets a FLIP class against the NEW (rightmost-byte) rule:
`flip_to_fast` (old present, new absent — a genuine improvement witness),
`flip_to_slow` (the reverse — **a regression risk I-112's own text does not
name**), `stays_slow`/`stays_fast` (unmoved). Corpus-wide:
**59 flip_to_fast, 49 flip_to_slow, 47 stays_slow, 531 stays_fast**.

**One finding worth flagging explicitly**: `lit-run-3` (日本語) has **no
flip subject in the throughput regime** — its old lead byte (0xE6) and new
tail byte (0x9E) occur in exactly the same four of seven throughput subjects
(the three mixed-corpus rungs + the CJK-heavy one) and are absent from the
same three (asc/cyr/lat). I-112's own cited "×15 lit-run-3" figure (their
"Mac proxy") cannot be reproduced from THIS bench's own throughput corpus —
it only flips at `search_short` grain (10 of 91 flip_to_fast, 2 flip_to_slow),
where the whole pair's effect is independently known to be small (the first
sample's own P1.a finding, 2026-09-26 ledger §2.1: "the effect lives at
THROUGHPUT grain"). Stated in the predictions file's own P2/P3 notes, not
silently absorbed.

`utf8-0.1-b104-751b9c6d.tsv`'s 18 clauses (5 parents):

- **P1** — I-112's own "0 changes anywhere" transcribed literally:
  `n_wrong eq 0` on `pcrec_751b9c6d_*_utf8`, wildcard pattern.
- **P2.a-e** — IMPROVE (5 `flip_to_fast` throughput witnesses, incl. I-112's
  own named `lit-offset-at-tail`/`t-64k-lat`): `ratio_to(ce658cb7 same cell)
  lt 0.33` or `0.5`, a CONSERVATIVE floor well under I-112's cited ~15-50x.
- **P3.a-d** (`.i`/`.ii` each) — RESIDUAL (4 `stays_slow` throughput
  witnesses): `.i` predicts no large win (`ratio_to(ce658cb7) gte 0.5`),
  `.ii` predicts the residual gap TO RUST stays above a conservative floor
  (a third of the ce658cb7-window ratio).
- **P4.a-b** — REGRESSION RISK (2 `flip_to_slow` witnesses, the new
  finding): `ratio_to(ce658cb7) gt 1.2`, a modest, honestly-scoped floor.
- **P5.a-b** — a WEAK `search_short`-grain band (`between 0.5 2.0`),
  answering I-112's "THROUGHPUT and search cells" ask for the regime with
  no measurable effect rather than dropping it.
- **ci-\*/alt-\*/asr-\*/cls-dot-rep**: NO prediction, per I-112's own text —
  no row, matching this directory's "must not happen" rule for an
  ungrounded claim.

Every P2-P5 clause needs the read lane's report to embed BOTH the existing
`pcrec_ce658cb7_*_utf8` records (and, for P3.ii, `rust_1.13.1_default-
caps-simdna`) and the new `pcrec_751b9c6d_*_utf8` ones in ONE query — the
same cross-pin structural need every prior `ratio_to`-across-pins file in
this directory states (`docs/dev/predictions/CLAUDE.md`'s own
`capability-0.1-pin-25b1984f-confirm.tsv` entry, etc.); `check_stated_utc`'s
F27 re-anchor will need the same `evaluate_predictions` bypass those files
document, since `utf8@0.1` has measured records long before this file's
`stated_utc`.

## 2. O-62 §2-6 — the structural predictor

The team lead's brief asks for a program-identity census at 25b1984f vs
751b9c6d over each pattern × form × config, to ground which cells should
fall inside a cross-window null band vs where a real move is expected.
`docs/dev/measurements/probe_b104_o62_identity.py` (adapted from lane
`b104repin`'s own `probe_b104_census.py`) runs this: every
`bench/{email,loglines,bounded,altwide,syntax}/patterns/*.rx` file × THREE
distinct compiled configs (`auto-caps`/`auto-nocaps`/`vm-caps` — `vm-in-caps`
is compile-identical to `vm-caps`, the same fact `b104repin`'s own `cap`
population already relies on) × BOTH forms = 1,110 cells, compared by v2
program identity (`tools/program_identity.py`, called directly — no store
record exists for either pin on these five sets' pcrec testees).

**One live fix this lane's first run found necessary**: 25b1984f PREDATES
pcrec's D118 CLI reshape (landed at abi 29, 8d716693) — its own CLI takes
`--` positional, never `--pattern`. The first run (before this fix)
refused EVERY 25b1984f job (`refusal-mover:25b1984f` on 998/1,110 rows).
Fixed by probing each pin's own CLI shape live
(`program_identity._cli_shape`, never hard-coded) and passing it through
each job tuple explicitly rather than reading it as a module global inside
a worker — this project's Python defaults `ProcessPoolExecutor` to the
`forkserver` start method, whose workers fork from an import-time template
and do not see a global a parent's `main()` sets afterward (confirmed live:
`multiprocessing.get_start_method()` reads `forkserver` on this box). The
identical class of mistake the CLI-shape fix itself was, caught before
archiving rather than after.

**[NUMBERS OWED — the census was launched in the background (tracked,
`run_in_background: true`) and had not completed when this report was
written; see the marker below.]** <!-- FILLED IN ONCE THE JOB COMPLETES -->

## 3. syntax's anc-z-lc/anc-dollar hypothesis

I-112's own text: "syntax anc-z-lc / anc-dollar collapse from ×6,500 the
way capability's semdiv-dollar did (end-anchor work since abi 27)." Both
patterns are simple literal+end-anchor forms (`done\z`, `done$`).
Grounding read directly from the committed report (never invented):
`reports/2026-09-21-syntax-0.1-budu-ryzen1600-fullroster-25b1984f.tsv`
(the REAL 25b1984f syntax fullroster — NOT the stale `...-fullroster-
d34c9131.tsv` file whose name predates the re-measure but whose pcrec
column is d34c9131, checked directly from its own header/rows before use):
`anc-dollar` pcrec-auto-caps 512,844.883 ns vs rust 80.831573 ns (×6,345.4,
matching O-62's own ×6,343 to rounding); `anc-z-lc` 520,367.888889 ns vs
79.878756 ns (×6,514.6, matching O-62's own ×6,514). The analogous
capability collapse (O-62 §1): `wild-semdiv-dollar-trailing-newline` moved
from ×1,401 to ×0.50 (FASTER than rust) between the SAME two pins.

`syntax-0.1-b104-751b9c6d.tsv`'s P2/P3: `ratio_to(rust) lt 65` — a
CONSERVATIVE bound (at least ×100 reduction from the current ~6,343-6,514×,
still far short of the full collapse-below-1 the capability witness
shows), so a refutation is meaningful without overclaiming the exact
magnitude. If it does not hold, O-62's own text already says what that
means: "they are the first cells we would read."

## 4. Testee ids — independently confirmed, not guessed

Every testee id used (`pcrec_751b9c6d_{auto-caps,auto-nocaps,vm-caps,
vm-in-caps}-simdna[_utf8]`, `pcrec_ce658cb7_*_utf8`,
`pcrec_25b1984f_{...}-simdna`, `rust_1.13.1_default-caps-simdna`) was
checked against real store paths (`store/records/utf8@0.1/pcrec_ce658cb7_
*` for the utf8 ones; `store/index.tsv`'s own rows, grepped directly, for
every 25b1984f one across all five O-62 sets — confirmed PIN-UNIFORM: all
five sets already carry a full four-testee 25b1984f record today), never
copied from prose or assumed by the naming rule alone.

## 5. Validation

- `interpret.load_predictions(path)` on all six files: **18/18** (utf8),
  **4/4** (email/loglines/bounded/altwide), **6/6** (syntax) — zero
  closed-set errors.
- `python3 catalogue/check_interpret.py`: **212 passed, 0 FAILED**,
  unchanged from a clean `HEAD` run of the same command — confirms these
  six new files move nothing in the catalogue/code correspondence (the
  catalogue itself is untouched by this lane).
- **NOT scorable via the normal CLI path, same precedent as every prior
  cross-pin file in this directory**: no `751b9c6d` record exists yet for
  any of these six sets (the window has not run), so `pcrecbench interpret
  --predictions ... <report>` has no report to take; separately,
  `check_stated_utc`'s F27 re-anchor will refuse the normal path once one
  does exist, since every one of these six (subbench, version) pairs has
  measured records long before this file's `stated_utc` — the same
  documented gap `docs/dev/predictions/CLAUDE.md`'s own precedent (the
  25b1984f-confirm files, the noreqbyte-twin file) already states and
  bypasses via a direct `interpret.evaluate_predictions` call.
- `check_testee_globs` (Q6 (ii)) was deliberately NOT run pre-window, same
  precedent as those files: every named (subbench, version) already has
  measured records at older pins, so the check is not vacuous, and an
  exact not-yet-measured `751b9c6d` testee id would read as a false-positive
  authoring defect until the window writes the first record — at which
  point it passes for the ordinary reason.

## 6. OWED

- **The O-62 identity census's full identical/changed/refused counts**,
  per set and per config — the background job (tracked,
  `run_in_background: true`, NOT a disowned `setsid`) was launched from
  this worktree:

      cd /home/duxevents/pcrec-bench/worktrees/b104pred
      gnutimeout 1800 python3 docs/dev/measurements/probe_b104_o62_identity.py \
          /var/tmp/b104scratch/b104_o62_identity.tsv \
          > /var/tmp/b104scratch/b104_o62_identity.log 2>&1
      echo "DONE rc=$?" >> /var/tmp/b104scratch/b104_o62_identity.log

  Completion marker: the log's own last line, `DONE rc=<n>`. A fresh agent
  (or this lane, resumed) should check
  `/var/tmp/b104scratch/b104_o62_identity.log`'s tail before relying on any
  count. Once it completes: archive its stdout as
  `docs/dev/measurements/2026-09-27-b104-o62-identity-census.txt` (source
  header per convention — bench commit, both pin binaries' sha256, no
  timing/load relevance since it is compile-only), fold the per-set
  identical/changed/refused-both counts into each O-62 predictions file's
  own `delta_verdict` clause notes (replacing the `[identity census
  pending]` placeholder text currently in all five files), and update
  `docs/dev/predictions/CLAUDE.md`'s own entry with the real numbers.
- **The window itself** (utf8 + O-62 §2-6, per I-112's own ask and
  [B104]'s plan row) is explicitly NOT this lane's — the brief says
  predictions come BEFORE the run, which the manager schedules.

## 7. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 1 | read `docs/dev/lanes/BOILERPLATE.md`, follow it | DONE | this report |
| 2 | read `docs/dev/plan.md` [B104], inbox I-112 in full | DONE | §0 |
| 3 | mirror `b101pred_report.md` / `docs/dev/predictions/` format+discipline | DONE | §5, file shapes |
| 4 | utf8 A: transcribe I-112's "0 changes anywhere" | DONE: P1 | `utf8-...tsv` |
| 5 | utf8 A: classify every (lit-* × subject) CONTAINS-LITERAL, both rules derived, state which used | DONE: both derived, Rule B used for the timing split (the mechanistic driver), Rule A cited for the sanity invariant | `probe_b104_utf8_litcontains.py`, census file |
| 6 | commit the classification table under docs/dev/measurements/, source header | DONE | `2026-09-27-b104-utf8-litcontains-census.txt` |
| 7 | predict (a) NOT cells improve, (b) CONTAINS cells residual gap, cite I-112's ×50/×15 | DONE: P2 (a), P3 (b); ×15 lit-run-3 found NOT reproducible at throughput grain, stated honestly | §1 |
| 8 | ci-\*/alt-\*/asr-\*/cls-dot-rep: no prediction | DONE: no row, stated | `utf8-...tsv` note |
| 9 | O-62 §2-6: no per-cell predictions except the syntax hypothesis | DONE: only P2/P3 in the syntax file are per-cell | five O-62 files |
| 10 | O-62 §2-6: structural predictor — program identity 25b1984f vs 751b9c6d, per pattern×form×config | DONE (script, launched); numbers OWED (§6) | `probe_b104_o62_identity.py` |
| 11 | O-62 §2-6: predict identical→null band, changed→direction where a landed mechanism explains it, else "changed, direction not predicted" | PARTIALLY DONE: the delta_verdict structural clauses are in place; the per-pattern identical/changed fold-in is OWED (§6) | five O-62 files |
| 12 | list O-62 §2-6 losses >×2 as the read lane's own priority | DONE (below, not a TSV row — not a prediction) | §8 |
| 13 | commit, hand back, end | DOING | this section |

## 8. What the read lane should look at first (O-62's own list, restated — not a prediction)

Per O-62's own "suggested order": `trim-nested-star` short (capability,
already re-measured, ×5,110 standing), `evil-alt-nested` large; on the FIVE
sets THIS window re-measures: loglines `kv-quoted` (×67.7/×56.0 at
25b1984f), `level-context` (×10.0/×7.8); bounded `ctx-lazy-*`/`ctx-greedy-256`
large (×8.8-9.1, flat across counts); altwide's w-512 whole-subject band
(×3.6-16.5 vs rust); syntax's lookaround band (`lkb-pos` ×20.1, `lka-verb`/
`lka-pos` ×8.0) and the ×2.1-2.7 flat band O-62 itself flags as "one shared
per-byte scan cost, a hypothesis."
