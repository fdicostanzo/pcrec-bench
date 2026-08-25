# reports/ — generated reports over the store

Each file is the output of one `python3 -m pcrecbench report ...` query,
committed beside the records it reduces so a reader can cite a number
with its query. Names: `<date>-<subbench>-<version>-<machine>[-<label>][.<grain>].md|tsv`.

**Reports are RE-RENDERED when the reporter changes** ([B9], 2026-08-25):
the STORED RECORDS are the data; a report is a VIEW over them, and the
view is versioned separately (`reporter: vN (date)`, a header line every
render carries — `pcrecbench/report.py`'s `REPORTER_VERSION`). When
`report.py`'s rendering changes, every committed report is regenerated
with the SAME QUERY that produced it (named in its own header) so the
file keeps its identity (the same records, the same filters) while
picking up the new columns/rulings. `report … | diff - <file>` is empty
immediately after a regeneration — the reporter is deterministic, so a
non-empty diff after a bare rerun (no query change, no reporter change)
means either the store changed or the reporter regressed determinism.

Both sample sets below were regenerated at [B9] (2026-08-25) against
reporter `v2 (2026-08-25)`: new columns (`status`, `fact`, `vs best`,
mechanism stamps, phase splits, etc. — see `pcrecbench/report.py`'s
module docstring for the full R1-R9 ruling list) mean these files no
longer diff byte-identical against their pre-[B9] versions, but each
still answers the SAME query as before.

- `2026-08-25-email-specimen-0.1-budu-ryzen1600.md` — the FIRST
  PRODUCTION SAMPLE: email-specimen@0.1 × {pcre2-interp, pcre2-jit,
  pcrec-auto, pcrec-nocaps, pcrec-vm} at pin 8da6120, 5 trials, pinned
  to CPU 11, in a quiet window coordinated with the pcrec manager
  session (02:22-02:56 EDT); set grain. `.subject-grain.md` the
  per-subject drill-down; `.tsv` the machine-readable form. Query:
  `--subbench email-specimen --until 2026-08-25T07:00:00Z` — the
  `--until` bound is NOW REQUIRED to reproduce this exact 5-record
  snapshot ([B9] regeneration note): the store has since grown past this
  sample's original "only 5 records exist yet" window (the re-pin
  sample below, and OD-B15's newest-wins dedup, would otherwise pull
  later records of the SAME testee_ids into what this file's name
  claims is the pin-8da6120-only sample).
- `2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.md` — the
  RE-PIN SAMPLE ([B8]): the same six cells re-measured after pcrec's
  re-pin to `692c2e8` (the caller-provided frame-buffer testees added,
  `pcrec-vm-in` measured), alongside the surviving pin-8da6120 records
  and the store's own re-measurements (a second libpcre2-interp run
  landed `inconclusive-load`, a second libpcre2-jit run landed
  `measured` and supersedes the first under OD-B15's newest-wins dedup —
  see the header's "superseded records" line). Query: `--subbench
  email-specimen` (no bound needed: every record this sample was drawn
  from already existed when it was first generated). `.subject-grain.md`
  the per-subject drill-down; `.tsv` the machine-readable form. Read
  alongside `docs/dev/feedback_pcrecdev1_2026-08-25-repin.md` (the
  pcrec manager's reading that became [B9]'s R1-R9 rulings) and
  `docs/dev/feedback_pcrecdev1_2026-08-25.md`.

**A note on what [B9]'s own rulings changed in this store's numbers**:
applying R1 (OD-B14: a non-`measured` row is excluded from ranking by
default) together with R2 (OD-B15: the NEWEST record per testee_id+
machine ranks by default) to the re-pin sample has a real consequence —
`libpcre2_10.46_interp-caps-simdna`'s newest record (17:34, a re-measure
under load) is `inconclusive-load`, so the DEFAULT baseline testee
(`libpcre2 engine_mode=interp`, named in every table title) is now
UNRANKED in most tables of the re-pin report unless
`--include-unmeasured` is passed; two of the four `692c2e8` pcrec
testees (`auto-caps`, `auto-nocaps`) are `inconclusive-load` for the
same reason and vanish from ranked rows they used to occupy. This is
the two rulings composing as specified, not a bug — see the "not ranked"
lines under the affected tables — but it means the re-pin report's
ranked rows look noticeably sparser than before [B9]; a re-measure of
those three cells on a quiet box would restore them to ranked status.
