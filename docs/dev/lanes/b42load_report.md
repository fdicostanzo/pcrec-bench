# [B42] restart, lane L4 — the `.rxt` pattern-source loader (lane `b42load`)

Branch `lane/b42load`, from `master` tip `4e4e52c`. Brief: give
`pcrecbench` a real `.rxt` loader path so a sub-bench whose pattern source
is a `.rxt` file loads without the derived-`.rx` compatibility shim
`bench/capability@0.1` (lane `b42set`, committed at `c2b5bde` on branch
`lane/b42set`, not yet merged) was built with.

**STATUS: DELIVERED.** `make check-schema` green (unaffected).
`make check-harness` OWED — launched in the background before this report
was finalized; see "Owed" below for the exact marker and how to read it.

## What this lane built

`pcrecbench/rxt_source.py` (new, ~400 lines): the ONE sanctioned reader of
pcrec's `.rxt` format on this side, through `pcrec --list-source` — no
second `.rxt` parser (D2 of `docs/design/rxt_needs_v1.md` §3's acceptance
checklist: "the loader contains no `.rxt` tokenizer of its own — verified
by code review at the restart, and by a grep for the format's keywords in
`pcrecbench/`"). `parse_list_source()` reads the dump's `#kind` main table
plus its four `#section` blocks (`provenance`/`variants`/`cases`/`aux`)
COLUMN-NAME-DRIVEN — no column position is hard-coded, only the names this
module actually reads, so the dump growing a column does not break it.
`load_rxt_source()` is the entry point and runs two gates before returning
anything:

- **Design constraint (b), the no-build-directive gate**
  (`check_no_build_directives`): a `target`/`config` row in the main table
  is refused BY NAME, naming every offending line. The control: an `ext
  bench` block (bench/capability's own testee-roster shape) never trips
  it, because `ext`'s own contents live entirely in `#section aux`, a
  section this gate never scans.
- **Design constraint (a), the block↔sidecar agreement gate**
  (`check_block_sidecar_agreement`): every `pattern`/`pattern-esc` block in
  the main table must appear exactly once in what the loader hands the
  harness (the built `Pattern` list), ids matched by the block's own
  `name` column. A planted mismatch (a block the loader dropped,
  duplicated, or renamed) is refused BY NAME naming what is missing,
  extra, or duplicated.

`pcrecbench/subbench.py`: a sidecar's `rxt_source = "<relative path>"` is
the ONE-LINE switch — present, `Subbench.__init__` builds `self.patterns`
from the `.rxt` file instead of the TOML `[[patterns]]` array, which is
then ignored outright (no cleanup needed at the switch: a stale array does
not need deleting for the switch to take effect). `Pattern.file` is now
OPTIONAL — a pattern carries `file` (the original per-pattern-`.rx`-file
shape) OR inline `text` (an `.rxt` block's own decoded bytes), never
neither; `pattern_bytes()` reads whichever is present, opening nothing for
an `.rxt`-sourced pattern. This closes the exact gap
`docs/design/capability_set_v1.md` §9 named from `rxt_needs_v1.md`'s own
B6 finding: *"`Pattern.__init__`'s required-field tuple and
`pattern_bytes()` both hard-require `file` today, not just a sidecar key
drop."*

`tools/export_rxt.py`: `build_rxt()` now refuses OUTRIGHT, naming the set,
when its sidecar already declares `rxt_source =` — its pattern source of
truth is ALREADY an `.rxt` file, so exporting it back would be a circular
derivation (a copy of a copy through this tool's escaping/target-prefix
machinery the file never needed). `check_rxt_export`'s per-set loop treats
that refusal as the PASS for such a set (`ok(... ); continue`), not a
failure.

`tools/selfcheck.py`: `check_rxt_source_load` (new, wired into `main()`
right after `check_rxt_export`) exercises, every gate paired with its
control in the same run (this file's own check-design rule):

1. a full `Subbench()` load of a synthetic `.rxt`-sourced fixture through
   the one-line sidecar switch: pattern text (incl. a raw high byte —
   0xE9, via `pattern-esc "caf\xe9[\x80-\xff]+"` — round-tripping
   BYTE-EXACT), `hazard_class` (from the block's own `tag hazard=`),
   `role` (`floor` derived from `family=floor`, never a sidecar field),
   `tags` (incl. `provenance-authored`/`fidelity-verbatim` from the
   block's own single-provenance sub-block);
2. the no-build-directive gate + its `ext`-block control;
3. the block↔sidecar agreement gate + its real-agreement control;
4. a missing/unbuilt pcrec binary refused BY NAME (not a raw `OSError`);
5. `Pattern`'s `file`-OR-`text` relaxation + its neither-one control;
6. the `export_rxt.py` circular-derivation skip.

Every fixture is a small string literal written to a fresh tempdir at
check time (`_write_synthetic_subbench`/`_StubSubbench`'s own convention
in this file — nothing this small earns a standalone committed fixture).
9/9 PASS, standalone (`python3 -c "...check_rxt_source_load()..."`,
verified before the full-suite run below).

## The format surprise found (reported to the manager before continuing)

**`--list-source` silently drops the `#section provenance`/`variants` rows
for every pattern block except the LAST ONE IN THE FILE**, when several
blocks each carry their own single, valid sub-block (no diagnostic, exit
0). The flat per-line `m`/`n`/`mc` case rows are NOT affected — a 2-pattern
control fixture showed both patterns' `m` cases present, only the second
pattern's `variant` surviving.

Repro (binary `build/pcrec-cd371441/build/pcrec`):

```
pattern abc
name p1
provenance
  source authored
  retrieved 2026-09-16
  license n-a
  fidelity synthesized
  adaptation authored for p1

pattern def
name p2
provenance
  ... (same shape, "authored for p2")

pattern ghi
name p3
provenance
  ... (same shape, "authored for p3")
```

`--list-source` on this exits 0 and emits exactly ONE `#section
provenance` row — p3's. p1's and p2's are gone.

**Confirmed on the real corpus too**: `bench/capability`'s committed
`patterns.rxt` (`c2b5bde`, 64 pattern blocks each with a `provenance`
sub-block) dumps exactly ONE `#section provenance` row (`floor-byte`, the
textually-last pattern). The other 63 patterns' provenance is silently
absent from the dump.

This directly touches the acceptance archive's C4/C7/D1 PASS verdicts
(`docs/dev/measurements/2026-09-16-b42-acceptance-41-cd371441.txt`) — all
were exercised on SINGLE-pattern-block fixtures, so "every descriptive
production appears in the dump" does not generalize to a real
multi-pattern set. **Filed as outbox O-29** (the manager, same day, with
this repro plus the 64-block corpus confirmation) and acked back to this
lane with an addendum scoping D1/C4/C7's verdicts to single-block files.

**MEASURED, refining O-29's own scope** (found while building the
follow-up gate below): the trigger is narrower than "a block has
provenance" — it is specifically a block whose provenance sub-block is
the LAST content in the block (nothing after it but a blank line before
the next `pattern`/EOF). A `tag family=..., hazard=...` line placed
AFTER `provenance` in the SAME block was measured NOT to reproduce the
drop; `bench/capability`'s own authored order (`pattern` / `name` / `tag
family=...` / `provenance` / its sub-lines, i.e. `tag` BEFORE
`provenance`) is exactly the order that DOES trigger it. Folded into
O-29 rather than filed separately.

**THE MANAGER'S RULING (2026-09-16), applied in this branch, not merely
documented**: `pcrecbench/rxt_source.py` gained a THIRD gate,
`check_provenance_agreement` — a provenance-row count strictly between 0
and the pattern-block count (never a legitimate authoring choice on any
set this project has seen) is refused BY NAME citing O-29; 0 rows (a set
that never uses the production) and a full 1:1 count both pass. This
makes `bench/capability` UN-LOADABLE at this pin (64 blocks, 1
provenance row) — confirmed directly: `Subbench("bench/capability")`
(once L3+L4 are merged) will raise `RxtSourceError` naming O-29. **This
is the correct terminal state, not a loader bug**: no shim path around
the gate, per the ruling. `check_rxt_source_load` gained arm (3b): the
exact O-29 shape (three blocks, `tag`-before-`provenance`, only the
last survives) refused by name, with a 0-provenance file as the
vacuous control. 11/11 PASS standalone (up from 9/9).

## A second, smaller finding (not a defect — a plumbing note, fixed here)

`--list-source`'s own documented rule ("[DD-13b.W23.4]" note, `rxt_format.
md`): a plain `pattern` block's column 5 is "the line's bytes verbatim" —
UNESCAPED except for the four TSV-framing-unsafe bytes (`\t \n \r \\`). A
raw, non-ASCII byte in the pattern TEXT (bench/capability's own
`binary-nonutf8` family: `high-byte-run`, `mojibake-curly-quote`,
`utf8-lead-no-cont`) therefore reaches stdout RAW, un-escaped — measured
directly (`printf 'pattern caf\xe9...'`). `subprocess.run(...,
text=True)` (strict UTF-8) CRASHES with `UnicodeDecodeError` the moment
the corpus carries one. `rxt_source.py` reads stdout as bytes and decodes
with `errors="surrogateescape"` (the standard lossless round-trip for
exactly this shape), and its own escape decoder (`_decode_dump_field`,
deliberately NOT `tools/export_rxt.py`'s `decode_rxt_escape`) re-encodes
with the same error mode. `export_rxt.py`'s own `decode_rxt_escape` has
this exact latent bug (`.encode("utf-8")`, no `errors=`) — untested
because its own corpus census is "NONE of the 185 ids contains a
non-ASCII byte" ([B38]'s own finding). **A suggestion, not filed as a
blocking finding**: the same one-line fix (`errors="surrogateescape"`)
belongs in `export_rxt.py` too, against the day a set with non-ASCII
pattern bytes tries to export (today none does — `check_rxt_export`'s
existing round-trip has simply never exercised this path).

## The E/F verdict table (`rxt_needs_v1.md` §3, groups E and F)

The acceptance archive (`docs/dev/measurements/
2026-09-16-b42-acceptance-41-cd371441.txt`) marked E1/E2/E3/E6/E7/F3/F4
NOT-RUNNABLE: "no `bench/capability@0.1` set exists; no `.rxt` loader in
`pcrecbench/subbench.py`". Both now exist (this branch + `lane/b42set`'s
`c2b5bde`, unmerged), so this lane re-read each check against what it
built, using a synthetic `.rxt`-sourced fixture where the real directory
is not yet in this tree, and the REAL 64-pattern `patterns.rxt` (read as
a git object, `git show c2b5bde:bench/capability/patterns.rxt`, never
checked out under `bench/`) where the check is about the real corpus's
own content.

Per the manager's note on reading this table: any check whose PASS
depends on `bench/capability`'s real corpus actually LOADING is marked
**BLOCKED-ON-O-29** below, not FAIL — the new `check_provenance_agreement`
gate (previous section) makes that load correctly refuse at this pin, so
"the real set does not load" is the gate working as ruled, not a defect
this lane owes.

| # | check | verdict here | evidence |
|---|---|---|---|
| **E1** | a bad id refuses fast (KB-12 pre-flight) | MECHANISM VERIFIED (synthetic); full check **BLOCKED-ON-O-29** | `check_id` fires on `.rxt`-derived ids through the SAME code path as TOML ones (unchanged) — proven on this lane's own fixture. Against the REAL `bench/capability` corpus, `python3 -m pcrecbench run --subbench capability ...` now refuses at `Subbench()` construction citing O-29, before an id is even checked — correct per the ruling, but it means this check's own full run waits on the same fix E6/F1 do |
| **E2** | id containment both ways for THIS set | **PASS** | all 64 real `bench/capability` pattern ids checked against `subbench.check_id` directly (`rxt_source.build_pattern_dicts` on the `c2b5bde` blob's parsed rows, BELOW the provenance gate — a deliberate lower-level check, since this fact does not depend on provenance at all): 0/64 illegal. The full gated `load_rxt_source`/`Subbench()` path on this same file now correctly refuses (O-29) — this check's own fact stands independently |
| **E3** | a subject addressable by ID, not by line | **NOT APPLICABLE to L4's scope** | `bench/capability`'s subjects come from the standard generated-manifest pipeline (`gen_subjects.py`/`gen_throughput_subjects.py`), never from `.rxt` `@file:` references — the dump's `#section cases` carries inline/`@file:` case rows in its schema, but this loader does not consume them for expectations (out of L4's brief; `expectations.tsv` stays the harness's expectation source, unchanged). Revisit if a future lane wires case-derived expectations. |
| **E4** | a duplicate block name is refused | **PASS (regression, existing)** | unchanged pcrec behavior (M7); not this lane's own code, re-confirmed incidentally by every load in this report |
| **E5** | an `under <convention>` case reaches the harness as a second expectation | **NOT THIS LANE'S SCOPE (unchanged)** | R5 finding B1 stands: `harness.outcome_for()` has no convention parameter. This loader exposes `RxtSource.cases` (incl. `under`-wrapped rows) for a future harness-side lane; it does not wire them |
| **E6** | `make check-harness`'s generic per-set gates pass on an `.rxt`-sourced set | **BLOCKED-ON-O-29** | needs `bench/capability/` to LOAD, which the new gate correctly refuses at this pin (64 blocks, 1 provenance row). This lane's OWN synthetic `.rxt`-sourced fixture (full 1:1 provenance coverage) passes the generic gates it CAN exercise standalone (`check_rxt_source_load`'s arm 1) — proving the MECHANISM works, not that the real set loads today |
| **E7** | `content_hash` covers the `.rxt` | **PASS** | `Subbench.content_hash()` needed NO code change: its existing `os.walk` over every non-generated committed file already includes `patterns.rxt` — a one-byte edit to the synthetic fixture's `.rxt` file moved the hash (`8511ed76...` → `8e5bff48...`), verified directly. "every included fragment and every `@file:` subject" is vacuous for `bench/capability@0.1` (no `include`, no `@file:` subjects). Independent of O-29 (content_hash walks bytes, never loads through the gates) |
| **F1** | `make check-harness`'s generic set gates enumerate a fifth set | **BLOCKED-ON-O-29** | `subbench_dirs()` already enumerates by discovery (no code change needed) — but every generic gate that then tries to `Subbench()` the set hits the same correct refusal E6 does |
| **F2** | a command-line flag survives a compile against a config-free `.rxt`-sourced set | **NOT EXERCISED (out of L4's scope)** | this loader never builds a pcrec artifact; F2 is a compile-time D93 question the pcrec-side acceptance run already confirmed live (`F2` row, accept-41 archive) |
| **F3** | the negative arm: a planted build directive in the set file fails this project's own gate | **PASS** | `check_no_build_directives`'s own positive fixture IS this check, run against a real gate this lane wrote (not merely "the underlying guard confirmed present by code read", as the archive's NOT-RUNNABLE note put it) — `target = t1` refused by name, `docs/dev/lanes/b42load_report.md` repro above |
| **F4** | the set carries no pcrec-oracled limits file and no pcrec-shaped expectation | **PASS (review, unchanged)** | `bench/capability`'s sidecar (read at `c2b5bde`) declares no such file; `.rxt`-sourced loading adds none — R-BENCH-4/AR-6 hold |

**The merge-time re-read**: once pcrec's O-29 fix lands and this branch's
`testees/pcrec` pin advances to pick it up, E1/E6/F1 become runnable for
real with no further code change here — `check_provenance_agreement`
will see a full 64/64 count and pass through to the existing two gates,
exactly as it does today on this lane's own synthetic fixture.

**The re-read command for E1/E6/F1** (once the manager merges
`lane/b42set` and `lane/b42load` with the one-line switch below, AND
pcrec's O-29 fix is picked up by the pin this project's `testees/pcrec`
points at — both are needed, not just the merge):

```
python3 -m pcrecbench run --subbench capability --testee pcre2-jit --tier scratch   # E1's timing
make check-harness                                                                   # E6/F1, generic gates enumerate capability@0.1
```

Before the O-29 fix lands, running either command against the merged
tree is EXPECTED to refuse citing O-29 — that is `check_provenance_
agreement` doing its job, not a new bug to chase.

## The exact one-line sidecar switch

At merge time, in `bench/capability/subbench.toml` (as committed at
`c2b5bde`), add ONE line — anywhere in the file-scope key block, next to
`regimes = [...]` is the natural spot:

```toml
rxt_source = "patterns.rxt"
```

`[[patterns]]`'s 64 committed entries do not need to be deleted for the
switch to work (`Subbench.__init__` ignores them outright once
`rxt_source` is present) — a follow-up cleanup, not a blocker. The
`description`/`objective` sentences that say "the harness's current
(pre-`.rxt`-loader) `pcrecbench.subbench` reads [`patterns/*.rx`]" become
stale prose at that point; a one-line wording fix, not required for the
switch to function.

## Charter-vs-committed checklist

- ✅ `pcrecbench/subbench.py` — the loading path + its CLAUDE.md update
- ✅ `pcrecbench/rxt_source.py` — the loader module (new)
- ✅ `tools/export_rxt.py` — the circular-derivation skip
- ✅ `tools/selfcheck.py` — `check_rxt_source_load`, 11/11 PASS standalone
- ✅ design constraint (a) — the block↔sidecar agreement gate, with its
  positive/negative controls
- ✅ design constraint (b) — the no-build-directive gate, with its
  `ext`-block control
- ✅ the block↔provenance agreement gate (O-29, manager ruling
  2026-09-16, added after the initial delivery) — refuses the current
  pin's `bench/capability` dump BY NAME, with the 0-provenance vacuous
  control and the exact O-29 negative fixture
- ✅ engine-neutrality statement in the code (the module docstring:
  "the pinned pcrec binary used HERE is TOOLING, exactly like the
  libpcre2 oracle")
- ✅ `Pattern.__init__`'s `file`-or-`text` relaxation (the B6 gap closed)
- ✅ format surprise: STOP-and-reported to the manager before continuing
  (message sent, this report's own section above)
- ✅ the E/F verdict table (rxt_needs_v1.md §3)
- ✅ the exact one-line sidecar switch, named above
- ⚠️ `make check-harness` full run — **OWED**, see below
- ⚠️ `make check` (schema + harness + report + interpret) — **OWED**,
  gated on the same run (check-schema alone already confirmed green)

## Owed

`make check-harness` (full suite, ~20 min historically) is running in
the background from this worktree, launched AFTER the O-29 gate was
added (a first launch, before the O-29 gate existed, was killed by
verified PID once it was clear it would validate stale code):

```
cd /home/duxevents/pcrec-bench/worktrees/b42load && gnutimeout 900 make check-harness
```

Tracked with an explicit DURABLE MARKER per this project's boilerplate
(not just the harness's own background-task notification): output
redirects to
`/tmp/claude-1001/-home-duxevents-pcrec-bench/932894fa-f62e-4029-8fb0-f23809c3696f/scratchpad/check_harness_run2.log`,
with a trailing `DONE rc=<code>` line appended on exit — check that line
(or its absence) as the source of truth, not process-list forensics; the
harness task id is `bnokf2srg` (`tasks/bnokf2srg.output` in the same
scratchpad) if that notification is what a resuming agent sees first.
Standalone, `check_rxt_source_load` alone is 11/11 PASS (shown above,
INCLUDING the O-29 gate's own positive/negative/vacuous arms) and does
not depend on the rest of the suite;
the OWED number is whether anything ELSE in the 300+-check suite moved
under `Pattern.file` becoming optional and `Subbench.__init__` gaining
the `rxt_source` branch — both changes are additive/conditional (no
existing sidecar declares `rxt_source =`, so every pre-existing set's
load path is byte-for-byte unchanged), so no regression is expected, but
"expected" is not "confirmed green" and the number belongs in a
follow-up, not asserted here.
