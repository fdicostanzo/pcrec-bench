# pcrec-bench — comparative regex-engine benchmark

Sibling project to ~/pcrec. SEED STATE: APPROACH.md is the charter; no
build work yet — it begins after pcrec's scale work ([M4.6]/[M4.7])
completes, and §8's open questions are Frank's to rule first.

## MANDATE: repository scope

Work in this project touches ONLY the two mandated repositories
(~/pcrec and ~/pcrec-bench). Session-temporary files go in the session
scratchpad, never committed. Subagents inherit this mandate; state it in
their task briefs.

## What this repo is

Versioned test sets (harder and wider than usual microbenchmarks, backrefs
and hazard classes included), one thin adapter per open-source engine, a
standardized per-testee output artifact, and a static comparator over
artifacts. pcrec appears as several pinned testees (engine × options).
Read APPROACH.md first — it carries the four founding principles and the
architecture sketch.

What it is NOT: pcrec's regression gate (pcrec keeps its own internal
floors in tests/bench/compare). Dependencies live here, never in pcrec.

## Files

- `APPROACH.md` — the charter: principles, architecture, testee roster,
  correctness policy, pcrec relationship, open questions (§8).

Maintenance: update this file when files/subdirectories are added/removed
or their roles change. Every directory gets a CLAUDE.md.
