# docs/design/ — living design documents

Documents that describe a design AND the process/learning of building it —
panel-outcome blocks and refutations recorded inline rather than edited
away. Living: revised as the design is reviewed and built, unlike
docs/dev/'s append-only records.

## Files

None yet (2026-08-24). Expected first residents, in the order the plan
reaches them:

- `requirements.md` — the requirements note from the overall-requirements
  discussion with Frank ([B1]): what pcrec-bench must measure, for whom,
  fed back how; APPROACH.md §8's open questions with their rulings; the
  measured facts the requirements rest on.
- `artifact_schema.md` — the per-testee output artifact (APPROACH.md §3),
  versioned; the comparator's input contract.
- `set_format.md` — the bench set format position: what this project needs
  from pcrec's [DD-13] unified format (R-BENCH-1..9 in
  ~/pcrec/docs/design/dd13_format/requirements.md §5) and what it uses in
  the interim.
- `<engine>_adapter.md` — per-testee adapter notes where an engine's
  semantics or build needs recording (Vectorscan's no-leftmost-first
  caveat, TRE's POSIX convention, pcrec's testee matrix).
- `<topic>_measurements/` — measurement directories: scripts, raw logs,
  and a README that states the question, the method, and the numbers,
  in the shape of ~/pcrec/docs/design/subroutines_measurements/.

Maintenance: update this file when files are added/removed or change role.
