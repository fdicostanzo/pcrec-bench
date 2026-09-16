# bench/capability/curation/ — L1 + L2 staging

Raw materials for the capability survey set ([B42]), staged before L3
builds the actual sub-bench. Nothing here is loaded by the harness; there
is no `subbench.py` entry point for this directory and none is expected
until L3 lands.

- `wild/` — L1's delivery: families 1-6's WILD members (fetched from a
  confirmed-permissive source, quoted or mechanically adapted, with full
  provenance), plus a 2026-09-16 follow-up lane's three family-11
  (`semantics-divergence`) wild members closing the gap between L1's
  family-1-6 scope and L2's 3-of-6 designed-member delivery for that
  family. See its own CLAUDE.md and
  `docs/dev/lanes/b42fam11_report.md`.
- `designed/` — L2's delivery: families 7-12's DESIGNED members
  (synthesized, blinded per D27). See its own CLAUDE.md.

Every member's fidelity, licence and adaptation are recorded in full in
`wild/members.tsv` per `docs/design/capability_set_v1.md` §4.1. L3 is the
consumer: it re-derives `patterns[].provenance_source` /
`patterns[].fidelity` (the two schema-MINOR record fields §4.1 promotes)
from this directory's rows, and the full provenance row stays here rather
than being duplicated into the record (the sub-bench's `content_hash`
covers this directory already, `subbench_directory_model.md` §1.3).
