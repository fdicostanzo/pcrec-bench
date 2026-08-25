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

Options offered to the panel were: (a) leave it documented; (b) define
the regime as "the engine's own whole-subject test, however spelled";
(c) `unsupported-by-declaration`.

**RESOLVED 2026-08-25, and better than any of them.** From the pcrec
manager: for the match regime the pcrec adapter compiles a SECOND
artifact from `(?:<pattern>)\z` and uses the anchored entry on it;
`search_short` and `throughput` keep the plain artifact. `\z` and not
`$` because at `options = 0` `$` also matches before a final newline;
`(?:...)` so a top-level alternation binds to the anchor. Schema v1.1
adds an optional `form` enum (`plain` | `whole-subject`) on compile and
match rows so the two artifacts never share a row, and pcrec emits
compile rows for both forms of every pattern. pcrec's missing
end-anchored entry is a ratified but unbuilt generation axis upstream
([OS-4]) and is being raised there; this bench is its first customer.

**The asymmetry was NOT theoretical, and the resolution is measured.**
Constructed control: pattern `a|ab`, subject `ab`. The plain artifact's
anchored entry returns length 1, so `== n` answers NO, where libpcre2
under `ANCHORED|ENDANCHORED` answers `((0, 2), ())`. The `(?:a|ab)\z`
artifact answers `match [0,2)`. It is the `make check` control for the
idiom. The email sub-bench's own patterns never hit it (85/85 agreed on
the plain artifact), which is precisely why a constructed case was
needed.

Two things the measurement established that the ruling did not assume
(details in `testees/pcrec/CLAUDE.md`): `orig`'s `\z` form still selects
the DFA engine, and its byte-class skip prefilter is still present with a
byte-identical start-class table — but with a **weaker skip loop**, which
can never skip the final byte because the end-of-subject view must be
evaluated. And a gap: **the DFA prefilter is not observable through any
structured stamp**, so `engine_metadata` cannot report it. That is a
candidate request to the pcrec manager, because requirements §4.2's
"bucket outliers by MECHANISM" needs it and this sub-bench's headline
mechanism is exactly that prefilter.

## 10. Give-ups — RESOLVED as a schema change

The lane recorded a budget give-up as `did-not-match-as-expected` and
argued that if the panel disagreed it was a schema matter, not a harness
one. **The manager agreed: schema v1.1 adds a per-subject `gave-up`
outcome** — the engine refused on a resource limit (pcrec
`PCREC_ERR_STEPS`/`_FRAMES`/`_WORK`; pcre2's match or depth limit) — with
the engine's code in `diagnostic`, not timed, and **counted separately
from wrong answers**. That separation is the improvement on the lane's
own position: an engine that declined to answer and an engine that
answered wrongly are different findings, and this sub-bench's headline
hazard class is the former.

### 10.1 The give-up CODE SPACE — ruled as a range, and measured on both engines

**RULED 2026-08-25 (manager):** `gave-up` iff the code lies in
`[PCREC_ERR_FLOOR, -2]`, read from the artifact's OWN constants; strictly
below the floor → `crashed`. A range beats an enumeration: a give-up code
pcrec adds later is classified correctly by an adapter nobody edited, and
a reserved or internal code can never be laundered into `gave-up` by a
list that fell behind.

`testees/pcrec/shim.c` now exports `pb_err_floor()`,
`pb_err_giveup_top()`, `pb_err_internal()` and `pb_err_name()`, and the
driver reports them as `info` rows. MEASURED against pin 8da6120:
`err_floor -5`, `err_giveup_top -2`, `err_internal -6`; a real give-up now
answers `giveup:-3:PCREC_ERR_FRAMES`.

Three facts read off the pinned artifact's own header, two of which
correct the ruling message's list:

- `PCREC_ERR_WORK` (-4) **is** a give-up and was missing from the list.
  The range rule includes it by construction.
- `PCREC_ERR_INTERNAL` (-6) is **not** a give-up — the artifact says so
  outright ("below PCREC_ERR_FLOOR: NOT a give-up") — and maps to
  `crashed`.
- `PCREC_ERR_RECURSE` (-5) is inside the range but has **no producer at
  this pin**, so it cannot fire today.

**pcre2's side needed the same treatment, and the ruled two-item list was
too narrow.** MEASURED on libpcre2 10.46 by forcing each limit
(`pcre2_set_match_limit_8` / `pcre2_set_depth_limit_8` on `^(a+)+$` over
200 `a`s) and then sweeping `pcre2_get_error_message` over -70..-1 —
there is no `pcre2.h` on this box, so nothing here is read from a header:

| code | message | disposition |
|---|---|---|
| -47 | match limit exceeded | `gave-up` (forced, confirmed) |
| -53 | matching depth limit exceeded | `gave-up` (forced, confirmed) |
| -63 | heap limit exceeded | `gave-up` |
| **-46** | **JIT stack limit reached** | **`gave-up`** |
| -48 | no more memory | `crashed` — an allocation failure, not a configured budget |
| -52 | nested recursion at the same subject position | `crashed` — a SEMANTIC refusal, not a resource limit |

**-46 is the one that matters here:** `pcre2-jit` is a roster testee, and
a JIT stack exhaustion recorded as `crashed` would read as a libpcre2 bug
rather than a budget. The set lives in `testees/pcre2/adapter.py` as
`GAVE_UP_CODES`, with the non-members and their reasons written beside
it. The pcre2 driver now answers `giveup:<code>:<pcre2's own message>`,
the message taken from `pcre2_get_error_message` rather than a table in
the driver, so it cannot fall out of step with the library.

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

## 12. Schema v1.1 — ADOPTED 2026-08-25

**MERGED and adopted.** `SCHEMA_VERSION` is `1.1`, and `record.project()`
/ `V11_ONLY` are DELETED: every field is emitted directly. The staging
arrangement did its job — because the harness had been measuring all of
them since before the schema existed, adoption was a merge and a set of
emission points, not a re-instrumentation.

The bet behind that arrangement, recorded here because it paid: a field
that was never MEASURED cannot be added to an old record afterwards, while
a field measured and not emitted costs one line. Sampling was maximal from
the start and only emission was versioned.

| v1.1 item | how it is measured today |
|---|---|
| (1) `seq` per row | dense 1..N across compile AND match rows (X18) |
| (2) `load.before/after` | `{loadavg_raw, sampled_at, load1/5/15}`, X19 re-parses the raw line |
| (3) `occupancy` before/after | both ends, each with its own verdict + `limit_busy_pct` (X20/X26) |
| (4) per-row `calibration` | on every row whose loop ran > once, with a note when the target was missed (X21) |
| (5) `engine_commit` | the pin's 40-hex (X22) |
| (6) `run.driver_build_flags` / `driver_compiler` | the exact argv, recorded on the cached-build path too |
| (7) `subjects[].sha256` | from the committed manifests |
| (8) `quiet_attestation` | DROPPED |
| (9) `run.clock_source` | `clock_monotonic` |
| (10) `environment.cpu_mhz` | cpu0's scaling frequency |
| fix 21 `gave-up` | by RANGE from the engine's own bounds (§10.1) |
| fix 22 `form` | pcrec both artifacts, pcre2 omits (§9) |

Three things changed shape at adoption and are worth naming, because none
was what the staging assumed:

1. **`occupancy` has no combined verdict.** Each sample carries its own,
   `limit_busy_pct` travels beside them, and rule X26 recomputes each
   verdict from its own number — so a stored combined verdict could
   disagree with the numbers under it and there is deliberately nowhere to
   put one. `quiet.occupancy_ok()` reduces the two for the STATUS gate and
   the record stores no reduction.
2. **`calibration.probe_iterations` has `minimum: 1`.** The staged
   "fixed-iters records `probe_iterations: 0`" is invalid. A fixed
   `--iters N > 1` now runs a REAL probe for provenance and carries a
   `calibration_note` saying the count was not derived from it; a
   1-iteration row carries no calibration at all, which is what X21 asks
   (a loop that ran once was never calibrated and does not claim to be).
3. **X23 checks the normalizers.** `env.py` now IMPORTS
   `normalize_cpu_model` / `_kernel` / `_compiler` from `validate.py`
   rather than keeping its own copies — the same rule `record.py` already
   followed for the derived ids, and the reason is the same: a check whose
   expected value shares an author's second guess with the thing it checks
   proves nothing.

`make check`'s v1.1 control is now a PRESENCE check on a real written
record, run at `--iters 2` on purpose so that X21's calibration
requirement is actually triggered. The validator can only reject what is
present and wrong; a field the harness quietly stopped filling in is
invisible to it wherever the schema made the field optional.

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
