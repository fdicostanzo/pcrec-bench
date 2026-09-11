---
name: pcrec-bench-interpret
description: Generate and commit the `.interpretation.md` sidecar for a pcrec-bench report by running `pcrecbench interpret` — the deterministic, opinion-free fact-finder over a report TSV and store/index.tsv. Use when asked to interpret a committed report, produce/refresh its findings sidecar, or regenerate a sidecar made stale by a catalogue or reporter bump. Never use it to write prose about a report by hand.
---

# /pcrec-bench-interpret

Invoked `/pcrec-bench-interpret <report>`, where `<report>` names a file
under `reports/` — a basename, a `.md` path, or a `.tsv` path all resolve
to the same `.tsv`. Implements docs/design/interpreter_v1.md §9.1
exactly. Run every command below from the **repository root**.

## What this skill does, in order, and nothing else

1. Resolve `<report>` to `reports/<name>.tsv`; refuse if it does not
   exist.
2. Look in `docs/dev/predictions/*.tsv` for a file whose rows'
   `subbench`/`version` columns match the report header's
   `filters: subbench=..., version=...`. At most one is expected on
   this project's corpus today; pass it if found, omit `--predictions`
   if not.
3. Run, with every path **repo-relative** (the stamp records paths
   exactly as given, and `check-interpret` section 3 re-resolves them
   from the repository root):

       python3 -m pcrecbench interpret reports/<name>.tsv \
           --index store/index.tsv \
           [--predictions docs/dev/predictions/<slug>.tsv] \
           --render --out reports/<name>.interpretation.md

4. Re-run the same command **without `--out`** (to stdout) and
   byte-compare it against the file just written — the determinism
   check. A mismatch means `interpret` itself is non-deterministic;
   stop and report it rather than editing the file to match.
5. Report the fired-rule headings and counts from the generated
   sidecar to the session, then commit it beside its report. Stop.

Nothing else. This skill does not read the report's markdown rendering,
does not run `make check-interpret`'s full suite, does not rank or
choose which report to interpret, and does not touch `catalogue/`.

## The opinion firewall — read before touching a sidecar

A sidecar is **fully generated**: every non-blank, non-stamp line is
`template.format(**slots)` for one rule in `catalogue/rules.toml`,
whose templates are reviewed prose gated by `make check-interpret`
section 6. `interpret` reads only the report TSV and `store/index.tsv`
(never the markdown), never re-derives a number the reporter did not
already print, and never asserts a cause — it flags a fact and stops
(interpreter_v1.md §0, §7, §9.1's own "does not summarise, rank,
explain, extend, or add a reader's note").

**Consequently: never hand-edit a `reports/*.interpretation.md` file.**
No added paragraph, no "reader's note" section, no ranking of findings
by importance, no sentence about *why* a number moved. If a fired (or
silently non-firing) rule looks wrong, or a fact you expected is
missing, that is a **catalogue change** — a new or revised `[[rule]]`
in `catalogue/rules.toml`, built and reviewed as its own lane
deliverable under `make check-interpret`'s fixtures and the template-
diff gate — never a patch applied to the rendered output. A future
agent "improving" a sidecar by hand defeats the entire design; route
the improvement through the catalogue instead.

## Regeneration: when a committed sidecar goes stale

`make check-interpret` section 3 re-renders every committed
`reports/*.interpretation.md` from the paths and sha256 values recorded
in its own stamp and requires byte equality — a stale sidecar is a
`make check` failure, not something a reader has to notice
(interpreter_v1.md §3.3, §8(3)). Section 3 re-renders against the
**paths named in the stamp**, `store/index.tsv` included — so on this
project's live-index default, a sidecar can also go stale from new
records landing in the store between generation and check, exactly as
R-STATUS-2's whole purpose intends. Regenerate — this skill, same
report — and commit the sidecar's diff in the SAME commit as whichever
of these caused it:

- a `catalogue_version` bump (a rule added/changed, a template's
  wording, a link, a `[[pin_order]]` append);
- a `REPORTER_VERSION` bump (which already regenerates the report
  itself, per `reports/CLAUDE.md`'s standing rule);
- a refresh of `catalogue/golden/index@<date>.tsv`, if it moves a fact
  (this affects `make check-interpret`'s golden comparison, not a
  committed sidecar directly, but the two commonly land together);
- new records in `store/index.tsv` moving what R-STATUS-2 (or any
  other rule reading the live index) reports for this report's
  population.

**The last cause is now automated ([B41] (a), 2026-09-11).**
`scripts/run_window.sh` regenerates every committed sidecar at its close
(`scripts/regen_sidecars.py`, run against the canonical store only, never
a rehearsal) — the SAME invocation this skill documents above (step 3),
plus this skill's own determinism check (step 4) — so a window that
writes new records no longer leaves `make check-interpret` section 3
failing until a human notices and runs this skill by hand. It fails
loudly: a non-zero exit is named in the window log
(`SIDECAR_REGEN_FAILED rc=...`) and becomes `run_window.sh`'s own exit
code, which `run_suite.sh`'s per-set summary line already surfaces. This
skill is still the tool for the other three causes above (a catalogue or
reporter bump, a golden refresh) and for regenerating one sidecar by
hand outside a window — `scripts/regen_sidecars.py` on its own
regenerates every committed sidecar the same way `run_window.sh` does,
if a manual all-sidecars refresh is ever wanted without invoking this
skill once per report.

## See also

- `docs/design/interpreter_v1.md` §9 — the design this skill implements.
- `catalogue/CLAUDE.md` — the rule catalogue and `make check-interpret`'s
  six sections.
- `docs/dev/predictions/CLAUDE.md` — the predictions file format.
- `scripts/CLAUDE.md`, `scripts/regen_sidecars.py` — the window-close
  automation of this skill's regeneration procedure ([B41] (a)).
- `reports/CLAUDE.md` — what the sidecars are, once one exists.
