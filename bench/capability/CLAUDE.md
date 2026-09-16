# bench/capability/ — the capability survey set ([B42]), STAGING ONLY

**This is not a runnable sub-bench.** There is no `subbench.toml`, no
generator, no manifest, no `NOTES.md` objective statement here yet, and
`make check-harness`'s generic `bench/*/` enumeration does not expect
anything runnable under this directory until L3 lands it. What lives here
today is CURATION: the raw materials L3 will build the set from, staged by
two lanes (L1 import/curation, L2 designed-member authoring) per
`docs/design/capability_set_v1.md` §11.1's lane plan.

Design authority: `docs/design/capability_set_v1.md` (the family
taxonomy, provenance model, capability model, metrics, roster) and
`docs/design/rxt_needs_v1.md` (the `.rxt`-format restart this set is now
built on, per the design note's Q3 supersession of its own old §9).

- `curation/` — L1's and L2's staging output. See its own CLAUDE.md.

## Restart state (read before adding anything else here)

The design's build was PARKED 2026-09-12 pending pcrec's `.rxt` delivery
(outbox O-26) and reopened after the acceptance run at pin cd371441
(31 PASS / 0 FAIL / 1 DISSOLVED / 9 NOT-RUNNABLE, `docs/dev/lanes/
b42accept_report.md` and its kin). L1 (this lane's own delivery,
`curation/wild/`) and L2 (families 7-12's designed members, authored
blind per D27) run in parallel; L3 consumes both to build the actual
`subbench.toml`, generators, and `NOTES.md`. Neither L1 nor L2 writes
anything under `pcrecbench/`, `testees/`, `schema/`, `store/` or any
other existing `bench/*/` set — see the lane boilerplate's scope mandate
and each lane's own brief.
