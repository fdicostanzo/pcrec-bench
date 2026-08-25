# Harness implementation notes — where the build differs from the contract

STATUS: written by the [B3]+[B4] lane, 2026-08-25, against
`harness_contract.md`. Every item is a place where the contract was
silent, ambiguous, or where the implementation deliberately did
something else. Nothing here is a decision the lane was entitled to
make alone; it is a list for the M1 panel and the manager to rule on.

The contract's own precedence rule applies throughout: *the schema wins
on field names and enums, the contract wins on interfaces.*

## 1. The two regime spellings — RESOLVED IN CODE, one place

The contract's sub-bench and CLI speak `match` / `search_short` /
`throughput` (§2, §4). `record_schema.md` §5's enum is
`match-compliance` / `short-subject-search` /
`large-subject-throughput`. Both are real and neither is wrong. The
mapping is `pcrecbench/subbench.py`'s `REGIME_TO_ENUM`, and it is the
only place either name is translated. **No ruling needed unless the
panel wants one spelling retired.**

## 2. `testee_id` has two id spaces, and that is forced

`--testee pcre2-jit` takes an adapter CONFIG id. The record and the
store path carry the DERIVED `testee_id`
(`libpcre2_10.46_jit-caps-simdna`), because record_schema.md §6.4
derives it and rule X5 checks it. A config id could not be used in the
record without breaking X5, and a derived id is not something a person
should have to type. `python3 -m pcrecbench testees` lists the config
ids and `run --help` says which is which.

## 3. Sidecar EXTENSION: a second generator/manifest pair

Contract §2 gives `[subjects]` as "(generator, manifest)" and says
"nothing else; a new field is a design change". But the same section's
directory layout mandates a `throughput/` tree with a committed
`manifest_throughput.tsv`. `bench/email/subbench.toml` therefore adds
`throughput_generator`, `throughput_manifest`, and
`short_search_max_bytes` (the ≤ 256 B cut the regime mapping needs).
**This is the design change §2 asks to be declared.**

## 4. Driver protocol: three added columns and a trial number

Contract §3's line shapes were extended, all three because the contract
elsewhere requires the datum:

- `compile` lines carry a TRIAL number (`compile TRIAL PHASE SECONDS`).
  The record keeps raw trials and X9 requires dense 1..N; a parser
  counting repeats to recover the number would mis-attribute a phase a
  driver skipped.
- `subject` lines carry `NMATCHES` — the throughput regime's
  expectation IS a count of non-overlapping matches — and `CAPS`, which
  §3 lists in what `measure()` returns but omitted from the column
  list.
- `--find-all`, `--skip` and `--subject-timeout` are added flags. See
  §5 and §6 below.

## 5. `measure()` returns three things, not a list

Contract §3 has `measure() -> list[MatchRow]`. It returns
`(rows_by_trial, info, notes)`: one row list per TRIAL (§3 itself says
the driver runs once per (regime, trial)), the driver's `info` pairs,
and harness-level NOTES — a driver restart, a subject left without an
outcome. The notes exist so those events land in the record's
`status_detail` instead of being swallowed.

## 6. Two timeout layers, and the resume rule

Contract §3 puts `gnutimeout` on the driver process. That alone cannot
say WHICH subject hung, which is precisely what record_schema.md §5's
`timed-out` addition exists to record. So the drivers also carry a
per-SUBJECT `alarm()`, and python RESUMES a died driver at the next
subject (`--skip`), attributing `crashed`/`timed-out` to the first
UNREPORTED subject and nothing to the ones never attempted.

## 7. `iters` calibration — the rule, since "one subject" needed a which

Contract §3: "`iters` chosen so one subject's loop is ≥ 50 ms,
auto-calibrated by python from a probe run". Implemented as: probe every
subject at a small fixed `iters`; the MEDIAN per-iteration cost sets the
number. Calibrating on the fastest subject would multiply the slowest
one's cost by orders of magnitude; on the slowest it would leave the
fast ones under the clock's resolution. The result is then capped so the
predicted whole-list sweep stays under 20 s per trial. Both the number
and the reason land in the record.

## 8. `consumed_length` — the same narrow claim from both testees

Neither libpcre2 nor a pcrec artifact exposes a scan high-water mark;
both take a `size_t` length. So `consumed_length` is *the length the
engine was given and accepted*, and `truncation_check = verified` means
*no byte was withheld or refused* — never *the engine looked at every
byte*. Both adapter CLAUDE.mds say so. **A future testee with a real
subject ceiling will make this field mean something sharper, and the
two meanings must not be reduced together.**

## 9. THE MATCH REGIME PRESUMES AN END-ANCHOR — pcrec has none

This is the one item with a real semantic hole in it.

Contract §2 defines the `match` regime as whole-subject, and §3 spells
it `PCRE2_ANCHORED | PCRE2_ENDANCHORED`. pcrec has no end-anchor
option, so `testees/pcrec` answers the question as
`<prefix>_match_caps(...) == n`. That is SUFFICIENT and not NECESSARY: a
pattern whose leftmost-first anchored match is a strict prefix, but
which could reach the subject's end by backtracking, answers *no* where
PCRE2 answers *yes*. Such a disagreement would be recorded as
`did-not-match-as-expected` — a finding about the HARNESS, not about
pcrec.

**MEASURED on `bench/email`: it does not bite.** `pcrec-auto` answers
85/85 as expected on `orig` in the match regime, and the five
disagreements on `factored` are budget give-ups, not this.

Options for the panel: (a) leave it, documented, and re-check per
sub-bench; (b) define the match regime as "the engine's own
whole-subject test, however it spells it", making the asymmetry part of
what is measured; (c) treat an engine without an end-anchor as
`unsupported-by-declaration` for the regime, which would delete pcrec
from the compliance columns entirely. The lane implemented (a) and
recommends (b).

## 10. Give-ups have no outcome of their own

`match_outcome` has no `gave-up`. A budget give-up
(`PCREC_ERR_STEPS`/`_FRAMES`/`_WORK`) is recorded as
`did-not-match-as-expected` with the engine's own code in the row's
`diagnostic`, and is therefore not timed. The argument is in
`bench/email/NOTES.md`: from the bench's point of view, a wrong answer
and a refused one are both "not the expected answer", and a give-up
under a configurable budget is not `unsupported-by-declaration`
(nothing is inexpressible; a number was too small). **If the panel
disagrees this is a schema change, not a harness change.**

## 11. `subbench.content_hash` — the rule, which §8 left to [B3]

sha256 over every COMMITTED file in the sub-bench directory: for each
path in sorted order, `<relpath>\n<sha256hex>\n`, joined and hashed.
Generated trees (`subjects/`, `throughput/`, caches) are EXCLUDED —
they are reproduced byte for byte from a generator that is itself
hashed, and including them would make the hash depend on whether a
regenerable tree happened to be present. The manifests ARE hashed, so a
subject that drifted from its generator is still caught. Path-prefixed
and path-sorted, so a rename is a change and two files swapping
contents is a change.

## 12. Schema v1.1 — measured now, emitted on a one-line switch

The v1.1 amendment (provenance holes found by the post-merge schema panel)
is landing on another lane. This harness does not wait for it: it
**measures every v1.1 field today** and narrows the record to whatever
`record.SCHEMA_VERSION` says, at one projection point (`record.project`).

The asymmetry is the reason. A field that was never MEASURED cannot be
added to an old record afterwards; a field that was measured and not
emitted costs one line to start emitting. So sampling is maximal and
emission is versioned.

| v1.1 item | how it is measured today |
|---|---|
| (1) `seq` per row | a monotonic counter across compile AND match rows, dense 1..N |
| (2) `load.before/after` as objects | `quiet.load_sample()` always returns `{loadavg_raw, sampled_at, load1/5/15}` |
| (3) `occupancy` before/after | `quiet.check()` is called at BOTH ends by the same code path; `occupancy_block()` combines them, verdict = the WORSE |
| (4) per-row `calibration` | `calibrate()` returns `{target_ns, probe_iterations, probe_elapsed_ns}`; a fixed `--iters` records `probe_iterations: 0`, which is itself the fact that no probe stands behind the number |
| (5) `engine_commit` for non-release | ALREADY EMITTED — pcrec records `8da61208b1194966ed4e482fb61e4b44371cb5a8` |
| (6) `run.driver_build_flags` / `driver_compiler` | `driverrun.DRIVER_BUILDS` records the exact argv, including on the cached-build path |
| (7) `subjects[].sha256` required | ALREADY EMITTED from the committed manifests |
| (8) `quiet_attestation` dropped | still emitted (1.0 requires it); one line in `project()` when 1.1 lands |
| (9) `run.clock_source` | `clock_monotonic` — both drivers use `clock_gettime(CLOCK_MONOTONIC)` around the batched loop |
| (10) `environment.cpu_mhz` | `env.cpu_mhz()`, a spot reading of cpu0's scaling frequency |

**TO ADOPT:** set `SCHEMA_VERSION = "1.1"` and delete the corresponding
entries from `record.V11_ONLY`. Nothing else moves.

`make check` has a control for exactly the failure mode this arrangement
invites — a projection that strips a field the harness never built,
invisible while 1.0 is emitted and absent the day the version flips. It
asserts all three legs on a real run: the full record carries all 11
fields, projecting at 1.0 removes exactly them, projecting at 1.1 keeps
them.

`status: measured` already requires the occupancy verdict to be `pass`
at BOTH ends, per the panel's rule, and `unavailable` on either sample is
`inconclusive-load`. One residual wrinkle for the panel:
`quiet_attestation` is computed from the BEFORE gate only, so a run that
went busy partway through records `quiet_attestation: true` beside
`occupancy.verdict: fail`. That is record_schema.md §11.8's "a claim
beside a measurement, and a disagreement is a finding" working as
designed — and it stops being a question when (8) drops the field.

## 13. Store writes are atomic, and the first implementation was not

The name is claimed with `O_CREAT|O_EXCL` and the `-<n>` disambiguator
retried on `EEXIST`. An `os.path.exists`-then-write pair passes every
single-threaded test and fails in the field: two invocations of the same
cell in the same second both see the name free, both write, one is lost —
the exact outcome the disambiguator exists to prevent, reintroduced by the
way it was checked.

**The control earned its place immediately.** With 8 forked writers racing
on one cell, the first implementation landed 6 records and lost 2: every
writer staged its content in a single shared `.validating/` directory and
`rmdir`'d it on the way out, pulling the directory out from under writers
that had claimed a name but not yet written. Staging is now one `mkdtemp`
directory per write. The control is permanent (`make check`).

## 14. What is NOT built here

- `pcrecbench/report.py` — [B5]. `python3 -m pcrecbench report` exits 2
  with a message saying so.
- A lazy-JIT compile row (`derivation: trial-1-minus-steady-state`).
  `record.compile_row()` has the branch and no adapter reaches it;
  neither testee is a lazy JIT and modelling one as such would put a
  fabricated number on the compile axis.
- OD-B10 (1 MB vs 8 MB spread) — the contract puts it at [B4] and it
  needs a QUIET box, which this lane never had.
