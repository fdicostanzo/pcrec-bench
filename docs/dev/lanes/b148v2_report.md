# b148v2 -- lane report ([B148], unusual_set_v1.md v0.1 -> v0.2)

2026-10-27, design only: no builds, timing, downloads or engine probes; ~/pcrec
read only (git log + docs). Deliverable: `docs/design/unusual_set_v1.md` v0.2
(change log at its top maps C1-C10 + Q1 to sections and lists PROPOSED
P1-P14), `docs/design/CLAUDE.md` entry updated.

## C1-C10 checklist

| item | where | state |
|---|---|---|
| C1 | 2, 2.1, 3.0, 3.2, 4.2, 5.1, 10, 11 | applied; the JSON member's source OWED (below) |
| C2 | 5.5, 7.4 | applied (P4, P5) |
| C3 | 7.2, 7.4 (X51), 10 L1 | applied (P6) |
| C4 | 4, 7.1, 7.3 | applied; row durations OWED to L4's dry run |
| C5 | 2.2, 3.2 | applied (P3) |
| C6 | 3.3, 5.3 | applied (P13); nested-unset rule asked of pcrec (Q-C) |
| C7 | 4.3, 6.1-6.3, 6.5 | applied (P10, P11); `CELL_CAP_unusual` OWED to L4 |
| C8 | 6.4 | applied; record fit OWED to L1 |
| C9 | 3.0, 3.1 | applied |
| C10 | 3.0, 7.3-7.5, 10 (L1, L8) | applied (P7, P8, P9, P12); expectations_stream run time OWED to L3 |
| Q1 | 6.1, 6.2, 8 | applied as ruled |

## OWED

- `wild-json-validate` source: candidate Stack Overflow q2583472's
  `(?(DEFINE)...)` answer (CC BY-SA); not on the box or in either repo, so
  not transcribed. Owner L3, gate Frank (URL + licence shown). If refused,
  the member is dropped from v0.1.
- Measured values the note defers: L4 dry-run durations and
  `CELL_CAP_unusual`, Onig match-stack unit, L3 sqlite call count and the
  `expectations_stream` re-derive time, L1 record fit for 6.4.

## Notes

- cscan source: pcrec main 614d45eb3 (cired2) found the CI red on 9ea9c4a76
  in test pins, "no pcrec bug"; `tests/recursion/cscan.rxt` is unchanged since
  66f9a8560, so the 9ea9c4a76 text stands.
- No validation run applies (a prose note); the stale-text grep (`OQ-` not
  RULED, `families =`, "no wild", "to WITNESS", "per feature per engine")
  is clean except the deliberate withdrawal sentence in 7.3.
