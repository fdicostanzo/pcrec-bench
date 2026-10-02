# Lane smallfix report

Task (team lead brief): two small fixes, nothing timed, box under a
window until ~03:00 so CPU use kept minimal (`nice 19` on the one
`make check-interpret` run; no reporter load, no `make check-harness`,
no census run).

## 1. The litrun P5 grain fix

Charter: dev_journal.md line ~6198 says `docs/dev/predictions/
litrun-0.1-first.tsv`'s P5 lacked `grain=subject` on its selector, so
the committed sidecar reads it `not evaluable` (a scratch re-score gave
32/37). Fix P5's selector, regenerate ONLY that report's sidecar via the
`/pcrec-bench-interpret` skill's exact invocation, run `make
check-interpret`, report before/after.

**Root cause, confirmed structurally before editing**: the report
`reports/2026-09-28-litrun-0.1-budu-ryzen1600-first-a32bc86e.tsv` is
`grain: set` (its own header line). Every P5 clause's selector matches
on `subject_or_na=<id>` (e.g. `mat-l4|lbf-l4`), but a set-grain report's
`subject_or_na` column is always the literal string `(set)` — confirmed
by `awk` over the TSV — so every P5 clause structurally cannot match a
row there. The committed `reports/2026-09-28-litrun-0.1-budu-ryzen1600-
first-a32bc86e.subject-grain.tsv` sidecar (grain: subject) already
exists and carries real `subject_or_na` values (`mat-l4`, `lbf-l4`, …)
— `grain=subject` is exactly the selector key that routes a clause to
that file instead (`docs/dev/predictions/CLAUDE.md`'s own documented
key), and it was simply never added to P5's 37 clause rows when the
file was authored.

**Committed fix**: appended `;grain=subject` to all 37 of P5's clause
selectors in `docs/dev/predictions/litrun-0.1-first.tsv` (every row had
no prior `grain=` key — confirmed before editing — so this is a pure
addition, never an overwrite). No other prediction id in the file was
touched.

**Regenerated** `reports/2026-09-28-litrun-0.1-budu-ryzen1600-first-
a32bc86e.interpretation.md` via the skill's exact invocation:

    python3 -m pcrecbench interpret reports/2026-09-28-litrun-0.1-budu-ryzen1600-first-a32bc86e.tsv \
        --index store/index.tsv \
        --predictions docs/dev/predictions/litrun-0.1-first.tsv \
        --subject-grain reports/2026-09-28-litrun-0.1-budu-ryzen1600-first-a32bc86e.subject-grain.tsv \
        --render --out reports/2026-09-28-litrun-0.1-budu-ryzen1600-first-a32bc86e.interpretation.md

Determinism check (step 4 of the skill) passed: the same command without
`--out`, printed to stdout, is byte-identical to the written file.

**Before/after P5 verdict**:

- Before: `R-PRED-3` (not evaluable), 37/37 clauses "no row in this
  report matches the selector".
- After: `R-PRED-4` (a compound prediction whose clauses disagree),
  **partial: 32 clause(s) confirmed, 5 refuted, 0 not evaluable** —
  P5a.l10, P5b.l40, P5c.fbf, P5d.l31, P5d.l40 refuted; every other
  clause confirmed.

This matches the journal's own "scratch re-score 32/37" exactly.

`make check-interpret` (nice 19): **234 passed, 0 FAILED** (section 1:
21, section 2: 8, section 3: 61 — including a clean re-render of the
regenerated sidecar, proving no staleness — section 4: 139, section 5:
4, section 6: 1). The 132-check figure in root CLAUDE.md is from an
earlier catalogue version; this project's check count has grown since
([B118]'s catalogue 3.13) — 234 is simply the current total, not a
regression.

Files touched: `docs/dev/predictions/litrun-0.1-first.tsv`,
`reports/2026-09-28-litrun-0.1-budu-ryzen1600-first-a32bc86e.interpretation.md`.

## 2. The [B33] cc-gate-census probe's protocol tokens

Charter: the brief states the probe (`docs/dev/measurements/
probe_cc_gate_census.py`, `make cc-gate-census`) does not pass
`--features all`, unlike every other pcrec invocation in this project,
and asks to make its argv match the adapter's protocol tokens — without
running the census (OWED for the manager, with the expected effect
stated).

**Investigation, before editing anything**: I confirmed via a
`--dry-run` argv dump (no pcrec/gcc/clang exec) that `--features all`
is **already present** on every emitted cell's argv today, via
`load_mode_flags()` reading it straight out of `testees/pcrec/
configs.toml`'s `[testees.pcrec-auto]` / `-nocaps` / `-vm` entries
(`flags = ["--features", "all"]` on all three — confirmed present since
the very FIRST commit of that file, `a0ac4e0`, [B3]'s own original pin;
never removed at any re-pin since). So the literal flag named in the
brief was not actually missing at this commit.

What **was** missing, and what I fixed: `testees/pcrec/adapter.py`'s own
phase-1 compile call (`_compile_one`, ~line 3960) passes a SECOND,
separate token on every exec — `EMIT_COMMENTS_FLAG` (`-fcomments`,
[B58]/[EMIT-VERB]) — described in the adapter's own comment as "a FIXED
PROTOCOL TOKEN on every phase-1 exec … alongside `-p rx`, never inside
`cfg['flags']`". Because it is deliberately kept out of `cfg["flags"]`
(so it never shows up in `testee_id`/`build_flags`/`config_extra`), it
is invisible to `load_mode_flags()`, which only ever reads
`cfg["flags"]` — so the probe's own from-scratch `emit_argv` construction
never carried it. This is the actual protocol-token gap the brief's
underlying concern ("make its pcrec argv match the adapter's protocol
tokens") names, even though the specific flag cited was the wrong one.

**Committed fix**: imported `testees.pcrec.adapter` (precedent:
`probe_b108_litrun_l31_memcmp.py` already does `from testees.pcrec
import adapter as pa`) and inserted `pcrec_adapter.EMIT_COMMENTS_FLAG`
into `census_cell`'s `emit_argv`, in the same position the adapter uses
(`[pcrec, "-p", "rx", EMIT_COMMENTS_FLAG] + flags + [...]`), with a
comment explaining both halves of the finding (what was actually
missing, and what was already present and not actually a gap). Verified
with a syntax check (`ast.parse`) and a `--dry-run` argv dump: the cell
now reads `pcrec -p rx -fcomments --features all -o … --pattern …`.

**Expected effect once the census is run** (OWED, not run here): per
[B58]'s own measured note (re-pin `25b1984f`, archived in `testees/
pcrec/CLAUDE.md`), `-fcomments` is a *provable no-op* on compile/refuse
outcome, object bytes and comment-excluded size on every artifact kind
checked there — and this census only ever reads `gcc_result`/
`clang_result` (compiled vs. did-not-compile), never `emit_bytes`. So
**no cell's outcome is expected to change** when the manager next runs
`make cc-gate-census`; the fix is a protocol-hygiene correction (any
future reader diffing this probe's emitted artifacts against a real
adapter-produced one now gets the same `.c` modulo nothing), not a
parity-result mover.

**A separate, larger, genuinely UNFIXED gap, found while investigating
and left OWED rather than touched**: `docs/dev/plan.md`'s own [B33] row
already carries an "OWED (low)" note from 2026-09-28 ("the probe
compiles byte-mode without `--features all` … utf8's 72 refusals (and
syntax's verb/module ones) are byte-mode/feature refusals"). Re-reading
that note against the structural fact above, its "`--features all`"
half does not hold (confirmed, as above, present since the first
commit) — but its "byte-mode" half does: the probe's `MODES = ("auto",
"nocaps", "vm")` tuple has no `-e utf8` arm at all, so every
`bench/utf8` pattern is compiled BYTE-MODE ONLY in this gate, unlike
the real `pcrec-*-utf8` testees. That is a materially bigger change
(a fourth mode dimension, new `mode_flags` entries, almost certainly
restricted to the one sub-bench that declares UTF-8 encoding) than
"add the missing protocol token" — out of this lane's scope and NOT
attempted here. Left for the manager to charter separately if wanted;
plan.md's own row already names it.

Files touched: `docs/dev/measurements/probe_cc_gate_census.py`.

## Charter-vs-committed checklist

| charter item | status |
|---|---|
| Fix litrun P5's selector so it resolves | COMMITTED |
| Regenerate ONLY that report's sidecar, via the skill's exact invocation, at nice 19 | COMMITTED (determinism check passed) |
| Run `make check-interpret` | COMMITTED — 234 passed, 0 FAILED |
| Report before/after P5 verdict + new score | COMMITTED — above (not-evaluable 0/37 scored → partial 32/5/0, matching the journal's "32/37") |
| Find the [B33] probe and make its pcrec argv match the adapter's protocol tokens | COMMITTED — `-fcomments` added; `--features all` found ALREADY present (documented, not a silent no-op left unexplained) |
| Do NOT run the census | HELD — not run |
| Leave it OWED for the manager, state expected effect | COMMITTED — above: no outcome change expected from this fix; the real byte-mode/utf8 gap is a separate, larger, still-open item named in plan.md's own [B33] row |
| Write docs/dev/lanes/smallfix_report.md, committed | COMMITTED (this file) |

No worktree left behind to clean up at merge (per the standing
"remove worktrees at merge" rule) — the manager removes
`worktrees/smallfix` after merging `lane/smallfix`.
