# pcrec-bench — comparative regex-engine benchmark

Sibling project to ~/pcrec (the ahead-of-time PCRE→C regex compiler).
This repo measures regex engines against each other — pcrec among them,
as several pinned testees — on a harder and wider set than the usual
microbenchmarks, emits standardized per-testee artifacts, compares them
statically, and feeds the outliers back to pcrec as optimization work.

STATUS (2026-08-28): M1 COMPLETE — charter (APPROACH.md), requirements v3
([B1]), record schema v1.1 ([B2], `schema/`), the harness core, the
`bench/email/` specimen, the pcre2 and pcrec adapters ([B3]+[B4]), the
reporter ([B5], `pcrecbench/report.py`, `--grain set|subject`), and the
first production sample in `store/` + `reports/` ([B6], pcrec pin
8da6120). M2 is in progress. 2026-08-29: [B18] (e) re-pinned pcrec to
**36d5963** (abi 11) — one adapter change absorbing three pcrec pins
(inbox I-15/I-16/I-17): the shim reads `RX_DFA_PREFILTER`'s
`offset-set` values + `RX_DFA_PREFILTER_OFFSETS` (abi 9, [OPT-K]),
`RX_DFA_MATCH` + `rx_info.match_form` (abi 10, [ENG-ABS]; the shim's
abi FLOOR is now 10), `RX_UNROLL_K`/`_WHY` + the two `_MAX_EMIT_*` caps
(abi 11, [ART-SIZE]); every unconditional stamp is checked PRESENT in
its scope at the artifact's abi (`STAMP_SCOPE`), the three new deny
flags are `make check-harness` controls, `pcrec --list-axes` is
archived (`testees/pcrec/list_axes.tsv`) and diffed against the pin,
and loglines `level-context` under `pcrec-auto` now COMPILES as the
[SEL-1] VM fallback (100/100 harness checks). 2026-08-30: [B19] re-pinned
pcrec to **96e44c2** (abi 12; inbox I-18, [OPT-4] ruling B + [DD-11]) —
the shim reads `RX_ENGINE_SEL` on every artifact (the engine route as a
closed token; Frank's ask (b) buckets on `not in (selected, forced)`) and
`RX_VM_PREFILTER_LANG`/`_WHY` on every VM HYBRID (not every VM artifact —
the spec's iff, measured), `PB_SHIM_MIN_ABI` stays 10; every compile row
carries `emit_bytes` / `emit_code_bytes` (pcrec's own size definition,
ported and controlled byte-exactly against `--warn-emit-bytes`) and
`warned_emit_bytes` where the advisory line fired (never a failure);
`list_axes.tsv` re-archived (54/21), `list_definitions.tsv` archived; the
abi-12 stamps asserted BY VALUE (level-context = I-18's prediction to
the letter; the size-cap rescue stamps `sel=selected` — a finding), the
bits 19/20 controls, the reporter's `sel=`/`lang=` clauses and two
source-bytes columns, and the abi-11 `K=`/`caps=` clauses (141/141 harness checks, 54 reporter tests). The
windows at 96e44c2 RAN the same morning (07:12-10:45 EDT, 18/18 cells
measured on attempt 1 under BD7; store 68; reports at v8, the AFTER and
repin-form files; ledger docs/dev/ledgers/2026-08-30-abi12-after-96e44c2.md;
outbox O-10: [OPT-4] SPLITS — the ctx band 2.2-3.1× and level-context 4.6×
faster where structure survives the collapse, `[a-z]{0,32768}` 3.6× slower
where the collapsed language is nullable — one predicate for pcrec;
Frank's I-19: BD7 ratified, (2)-(4) the v1.4 spread rule → [B20],
IMPLEMENTED 2026-08-30 as record schema **v1.4**: the PRE-FLIGHT
(BD7's average + the TARGET core's own tri-state reading) decides
`inconclusive-load`, the AFTER samples are PROVENANCE, TRIAL AGREEMENT
(rule `v1.4-group`, k=1.5 d_min=2 share_c=3 N≥5 odd, constants measured
over the store's 68 records) decides `measured` vs the new
`inconclusive-spread` (exit code 4, re-measured once by the window
script) — X13 VERSIONED under record_schema.md §4's new rule-revision
clause, X31-X33, the `trial_agreement` block on every record, the
per-group `/proc/stat` timeline as provenance, KB-4's schema half,
reporter **v9**, ten new harness checks (docs/design/gate_shape_v14.md
→ IMPLEMENTED); bounded@0.2's knee rungs → [B21] with pcrec's
[OPT-5]). [B19] is
COMPLETE and archived. Before it, the same night: bench/bounded@0.1's FIRST SAMPLE at
36d5963 (6/6 measured, store 50, reports 2026-08-30-bounded-0.1-*; the
[OPT-4] BEFORE; ledger docs/dev/ledgers/, outbox O-9: 65535 refused by
the NFA cap while pcrec-vm builds it, the end-anchored search-filter DFA
×37 — I-20: the documented 4096-state [ENG-ABS] ceiling, the `\z`
spelling halving it — the counted DFA chosen where the VM is 6× faster,
the wasted DFA build ×315-×687, K moved once) after two harness fixes
the window found: the free_text note cap (3bda38b) and BD7 — the
occupancy sample is `mpstat -P ALL 1 5` judged on its Average (five one-
shot after-sample losses in two windows; the gate-shape test run
measured all three on attempt 1); Frank's wider gate ruling is the
schema v1.4 spec docs/design/gate_shape_v14.md ([B20], since IMPLEMENTED). Before it, the window (a)/(b) and
outbox O-8 were the manager's step after [B18]. Before it, [B16] re-pinned
pcrec to **35e1ab1** (abi 8) — one adapter change absorbing five
pcrec pins of new observability (pcrec inbox I-5/I-6/I-11/I-12/I-13):
the shim reads `RX_ENGINE`, `RX_DFA_SCAN`/`_PREFILTER`/`_TABLE`,
`RX_FAST_FRAMES`/`_TRAIL` and `rx_info.scan`/`.prefilter`, with an abi
FLOOR the driver refuses below by name and a macro-vs-field control on
every artifact, so a pcrec record can now be bucketed by its
candidate-start MECHANISM on both engines (the gap [B8] filed as pcrec
I-3, closed); the REPORTER is v5 with I-7 §3/§5's rulings ([B16]
R1-R8), which turned one committed `faster ×13.45` into `selection
changed (vm → dfa)`. Earlier in M2: [B8] re-pinned pcrec to **692c2e8** and added
the caller-provided frame-buffer testees (`pcrec-vm-in` measured,
`pcrec-auto-in` defined) and measured the six-cell re-pin sample — the
before/after is `reports/*-repin-692c2e8.*`; [B10] landed the EDIT-TEST
LOOP (schema **v1.2** record tiers `pinned`/`scratch`, `pcrecbench
quick`, the `pcrec-local` provided-binary testee); [B9]+[B14] the
REPORTER v3 (status per row, cross-pin Δ verdicts, mechanism stamps,
compile phases, legends); [B15] the FLOOR PATTERN in bench/email
(schema **v1.3** `patterns[].role`). 2026-08-28: [B17] added two
non-periodic 1 MB prose subjects and the `periodic` manifest column
(`email-specimen@0.2`); [B11.1] landed SUB-BENCH #2, `bench/loglines/`
(log-line search over mostly-failing text, 10 goal-authored patterns +
floor, 112 subjects + a 16 KB-1 MB sweep, `pattern_facts.tsv` from
pcre2_pattern_info). Both were MEASURED the same day
(six cells each, `reports/2026-08-28-*`; outbox O-7 carries the
findings to pcrec — the [OPT-5] precheck is parity, the offset-k skip
is the ask). 2026-08-29: [B11.4] landed SUB-BENCH #4, `bench/bounded/`
(bounded repeats on both axes: ten everyday shapes incl. a bounded lazy
gap before a `\b` alternation at three counts, a thirteen-rung count
ladder to PCRE2's own 65535 ceiling, 30 short subjects + four large
runs in a count-rung `throughput` regime, `pattern_facts.tsv` with the
count facts, `oracle_limits.tsv` with the oracle's own first refusal
per skeleton; the predicted first pcrec refusal is the abi-11 size cap
at the 32768 rung — a first-class `did-not-compile` outcome, to be
measured in a window next). [B18]'s WINDOW ran the same day: 12 cells
at 36d5963 on email-specimen@0.2 and loglines@0.1, every one `measured`
(store index 41); outbox O-8 (739ccdd) carries the ledger — [OPT-K] moved more than predicted on the search band, [ENG-ABS] three of four aggregates confirmed, level-context = the VM with a 0.5-0.7 s compile-time DFA attempt; the long-subject `_match` probe is archived under `docs/dev/measurements/`.
2026-08-31: [B22] re-pinned pcrec to **263b013** (abi 12 UNCHANGED — the
[OPT-4.1] + [LIM-1] pin; inbox I-21-correction/I-22/I-25): two new
`RX_ENGINE_SEL` VALUES read by the same shim — `declined-nullable` (the
count-collapsed rescue DECLINED where the collapsed language is nullable:
no prefilter, no language pair, the §6.3 iff both ways) and
`size-cap-retry` (the size rung's own token, closing the `sel=selected`
mislabel O-8/O-10 flagged) — the fallback bucket now reads the VALUE only
(five tokens; the [B19] `_LANG_WHY`-prefix rule retired, adapter +
reporter v10, every committed report regenerated); `_LANG_WHY` gains
`nullable collapsed language` (the `-fprefilter-collapse` POLICY,
a force control); the I-21-corrected DECLINE/KEEP sets asserted by value
(11/11 as pcrec predicted; the plain-vs-`\z` overflow routes distinct —
the state cap vs K7), `list_limits.tsv` archived as the THIRD registry
target (44 rows; `--list-axes` 54 → 63/21: engine-route 5 → 7, size-term
2 → 7 now WITH stamp_values, table + none/mixed — [B18]'s registry gaps
closed), the declined `{0,32768}` same-pin emit-byte re-comparison
(I-22 (ii)), and `year4`'s +4,096 B CLOSED by derivation (I-22 (iii):
ELF page alignment triggered by the [B19] shim's own +384 B; pcrec's
source +33 B; docs/dev/measurements/2026-08-31-year4-elf-page-alignment.txt).
The WINDOW at 263b013 RAN the same day
(10:43-14:08 EDT, 8/8 cells attempt-1 under BD7: bounded@0.2's first
sample × 6 testees + the loglines KEEP arms; the v1.4 spread rule's
first production firing re-measured clean per contract; store 67
measured, records at schema 1.4); reports at
`2026-08-31-*-263b013.*` (the loglines AFTER is the first CROSS-PIN
report — KB-5; the R8 Δ column's first firing); the ledger
docs/dev/ledgers/2026-08-31-opt41-after-263b013.md; outbox O-11:
[OPT-4.1] CLOSED 10/10, [OPT-5] NO KNEE at any of nine rungs (the fix
is candidate 1; bounded@0.2 is its 9-rung acceptance surface),
grp-upto-1024 ≡ cls-upto-1024, year4 was the bench's own shim bytes
(ELF page alignment), five asks; W1.2 unblocked. [B21]/[B22] archived.
Next: [B23] (spread-rule positive control) and [B24] (cc axis) are
unblocked awaiting Frank; [B11.2] wide alternations; [B13] the
interpreter is chartered. `make check`
is green (4/72/0, 187/187, 59 reporter tests — re-verified at [B25]'s
re-pin). Manager sessions start with the
`pcrec-bench-manager` skill (.claude/skills/).

## MANDATE: repository scope

Work in this project touches ONLY the two mandated repositories
(~/pcrec-bench and ~/pcrec). Session-temporary files go in the session
scratchpad, never committed. Subagents inherit this mandate; state it in
their task briefs.

**~/pcrec is READ-ONLY from here** (docs/dev/decisions.md BD2): read its
docs, harnesses and corpora freely; never write to its main, branches,
`worktrees/` or build trees. Changes pcrec-bench needs in pcrec go to the
pcrec manager session as a request. pcrec does not touch this repo
(pcrec D52: dependencies live here, never there).

## Two sessions, one box (2026-08-24)

A pcrec manager session (`pcrecdev1`) and this project's (`pcrecdev2`)
may run concurrently on the same 12-core box. Rules (BD3, all measured
lessons): ONE heavy suite on the box at a time — announce heavy runs to
the other session first; the box's CPU-bounded checks lie under load, so
bench on a quiet box and record load in the artifact; large scratch under
the session scratchpad or `/var/tmp`, never `/tmp` root (7.6 GB tmpfs,
per-user quota); NEVER `pkill -f` — kill by PID with the cwd verified;
report a pcrec test failure to the pcrec session before concluding
anything from it; `gnutimeout` on every command of uncertain length.

## What this repo is

Versioned test sets (feature spread, backrefs, hazard classes, big
subjects, real-world shapes), one thin adapter per open-source engine, a
standardized per-testee output artifact with compile and match time
separated and its environment recorded, and a static comparator over
artifacts whose scoreboard excludes wrong answers. Read APPROACH.md first
— the maintained high-level statement — then docs/design/requirements.md
for every ruling in detail.

What it is NOT: pcrec's regression gate (pcrec keeps its own absolute
floors in tests/bench/compare). Dependencies (engines, build systems,
bindings) live here, vendored or system, pinned either way.

## Where things are

- `APPROACH.md` — the MAINTAINED high-level statement (mission, how the
  bench works, architecture, focus); kept current with the requirements,
  details in the files it references (Frank, 2026-08-25).
- `pyproject.toml`, `requirements.txt` — the python project files (BD4).
- `docs/dev/` — plan.md (grep'able `[Bn] STATE:` rows), plan_completed.md,
  dev_journal.md (append-only), decisions.md (BDn), pcrec_references.md
  (the map of every pcrec document this project depends on), wake.md
  (gitignored hand-off brief). See docs/dev/CLAUDE.md.
- `docs/design/` — living design notes (requirements, the record schema,
  set format position, adapter notes, measurement dirs). See its CLAUDE.md.
- `schema/` — the RECORD format at **v1.4**: `record.schema.json` (JSON
  Schema draft 2020-12), `validate.py` (the validator the harness and the
  reporter share; rules X1..X33), `check_fields.py`, `check_rules.py`, and
  `examples/` + `examples/bad/` (records that must validate, and sabotaged
  ones that must not). Designed in `docs/design/record_schema.md`; the
  record TIERS (`pinned` / `scratch`) are its §6.8. See its CLAUDE.md.
- `pcrecbench/` — the HARNESS package: `harness.py` (run a cell; the
  v1.4 pre-flight, `derive_status`, the trial-agreement block),
  `subbench.py`, `adapters.py` (the interface + **the driver protocol, in
  full, at the top of the file**), `driverrun.py`, `record.py`, `store.py`
  (the two tiers, the `.canonical` marker), `reduce.py` (the set-grain
  reduction `quick` and the reporter share), `quiet.py`, `env.py`,
  `oracle_pcre2.py`, `report.py` (the reporter, [B5]), `__main__.py` (the
  CLI: `run`, `quick`, `index`, `quiet`, `testees`, `report`). Specified
  by `docs/design/harness_contract.md`. See its CLAUDE.md.
- `bench/<name>/` — the SUB-BENCHES: sidecar, patterns, deterministic
  generators + sha256 manifests, oracle-verified expectations, engine
  notes. `bench/email/` is the RFC 5322 specimen; `bench/loglines/` is the
  log-line search set ([B11.1]) -- mostly-FAILING log text, shaped around
  whether PCRE2's required-code-unit dismissal is available for a pattern,
  and the measurement pcrec's [OPT-5] is built or not on; `bench/bounded/`
  is the bounded-repeat set ([B11.4]) -- the compile axis as a count
  ladder with the refusal as a first-class outcome, the match axis as
  everyday shapes with near-misses that fail at the last repetition.
  `make check`'s generic gates enumerate `bench/*/` rather than naming a
  set. See their CLAUDE.mds.
- `testees/<name>/` — the ADAPTERS: `pcre2/` (interp, jit) and `pcrec/`
  (auto, nocaps, vm, the `-in` variants, at a pinned commit — a7e0bdf,
  abi 13 — with `list_axes.tsv`, `list_definitions.tsv` and
  `list_limits.tsv`, the pin's `--list-axes` / `--list-definitions` /
  `--list-limits` registry surfaces archived
  verbatim; and `pcrec-local`, a PROVIDED binary at no pin).
  See their CLAUDE.mds.
- `store/` — the CANONICAL record store (the `.canonical` marker):
  `records/<subbench>@<version>/<testee_id>/<record_id>.jsonl`,
  `index.tsv`, `machines.tsv`. Pinned records only; scratch records live
  in `build/scratch-store/` (or `$PCRECBENCH_SCRATCH_STORE`), never here.
  See its CLAUDE.md.
- `tools/` — `selfcheck.py`, the harness half of `make check`.
- `.claude/skills/pcrec-bench-manager/` — the manager-session skill.
- Planned (not yet created): `pcrecbench/report.py` ([B5]).

## Build & test

Python 3 (>=3.11) is the project language for the harness, validator,
store and reporter (BD4): `pyproject.toml` (compatibility ranges),
`requirements.txt` (exact pins measured on the box — `python3 -m venv
.venv && .venv/bin/pip install -r requirements.txt`).

    make                # == make check-schema (the default target)
    make check          # EVERYTHING: check-schema + check-harness
    make check-schema   # the record schema: the design note's field tables
                        # against the JSON Schema, every schema/examples/
                        # record accepted, every schema/examples/bad/ record
                        # rejected FOR THE RULE ITS NAME CLAIMS (counts
                        # printed; ~3 s, python3 + jsonschema only)
    make check-harness  # 187 checks: for EVERY sub-bench under bench/ (by
                        # enumeration, [B11.1]) the generators reproduce their
                        # committed manifests byte for byte, every other
                        # gen_*.py re-derives under --check (loglines'
                        # pattern_facts; bounded's pattern_facts and
                        # oracle_limits), the expectations
                        # re-derive from the libpcre2 oracle and a driver
                        # answers the set's floor pattern by the oracle;
                        # both drivers smoke, the
                        # deliberately-wrong fixture yields the outcome it
                        # must, the two patterns are shown NOT to be one
                        # artifact, a hanging subject comes back `timed-out`
                        # BY NAME, 8 racing writers each land their own
                        # record, the whole-subject artifact is shown to
                        # answer a constructed case differently from the
                        # plain one, every v1.1 provenance field is shown
                        # populated, and a full `run` of one cell into a
                        # SCRATCH store is validator-accepted, and the
                        # caller-provided frame-buffer path (`_in` entries)
                        # agrees with the plain one, a tiny buffer gives
                        # up PCREC_ERR_FRAMES BY NAME where the configured
                        # one matches, and a DFA artifact takes no buffer;
                        # and ([B10]) the tier rules fire by name, the
                        # canonical store refuses a scratch record on write
                        # and on index (planted by hand), the shared
                        # reduction matches a hand-computed median, a `quick`
                        # cell's printed median is recomputed from its file,
                        # and pcrec-local describes, runs and is refused
                        # into a canonical store; and ([B16]) the pcrec abi
                        # 4-8 mechanism stamps are asserted BY VALUE on a
                        # real artifact of each KIND (pure DFA, VM hybrid,
                        # non-hybrid VM, provably-empty), both directions of
                        # the _DFA_* scope iff, `-fno-premul-table` reaching
                        # RX_DFA_TABLE's other value (the control that keeps
                        # a stamp distinguishable from a constant), and an
                        # artifact whose rx_info.abi is SABOTAGED below
                        # shim.c's floor refused BY NAME with the unmodified
                        # one loading in the same run; and ([B18]/[B19]) the
                        # abi 9-12 stamps by value on the bench's own
                        # patterns at the values pcrec predicted, every
                        # deny/force flag as a control (the size-cap rung
                        # denied = a refusal BY NAME), the archived
                        # --list-axes / --list-definitions diffed against
                        # the pin, and the emit-size port checked against
                        # pcrec's own --warn-emit-bytes numbers
                        # and ([B22], pin 263b013) the I-21-corrected
                        # DECLINE/KEEP sets by value (declined-nullable on
                        # cls-upto-32768 both forms + the two 16384 wholes,
                        # no prefilter, no language pair; the ctx rungs and
                        # nest wholes keep their collapsed-prefilter rescue;
                        # the plain-vs-\z overflow ROUTES asserted distinct
                        # -- state cap vs the K7 subset-elements budget),
                        # the size-cap rescue by its OWN token
                        # (size-cap-retry) with the ask-(b) bucket VALUE-only,
                        # the -fprefilter-collapse nullability POLICY
                        # ("nullable collapsed language" on (x){0,5}),
                        # list_limits.tsv (the third registry archive)
                        # diffed against the pin, and the declined {0,32768}
                        # same-pin emit-size re-comparison
                        # and ([B25], pin a7e0bdf, abi 13) dfa_scan_edge by
                        # value on every stamp/ledger case (range down to
                        # the one-state [0-9]+ form; bitmap on ipv6; none
                        # on attempt/empty and untaken runs; absent where
                        # no DFA scan -- four _DFA_* pairs both directions),
                        # the 16384 rung re-derived as the [OPT-5] collapse
                        # (724,699 warning -> 16,352 silent; warned pair
                        # asserted ABSENT), the -fno-scan-edge deny row
                        # (the warning returns -- the warn-capture positive
                        # witness), and the 65535 NFA-cap refusal asserted
                        # unchanged by name
                        # and ([B20], schema v1.4) the gate's shape: the
                        # target-core pre-flight on synthetic captures
                        # (busy / idle / row ABSENT, each refusal BY NAME,
                        # inert unpinned), the quiet CLI agreeing with
                        # gate(), a failed AFTER sample leaving a record
                        # `measured` at 1.4 and REJECTED re-stamped 1.3,
                        # the hand-computed trial-agreement fixture pinned
                        # against validate.py's independent second
                        # implementation (boundary rows included), the
                        # status decision table + an inconclusive-spread
                        # record stamped through store.write (one slow
                        # trial per row stays measured), the status
                        # sentence never elided, the smoke block
                        # n/a-trials, quick carrying and printing the
                        # block, exit code 4 with the per-status index
                        # line, and the /proc/stat timeline (absent when
                        # unreadable)
                        # (~5 min; needs libpcre2-8-0 and a C compiler)
    make deps           # what the harness needs, and whether this box has it
    make help           # list the targets

`make check` is a SMOKE SUITE, never a measurement: `--trials 1 --iters 1`,
one regime, `--force-unquiet`, every record it writes marked `synthetic`
and written under `build/`. Nothing it prints is a number.

Measuring one cell (the PINNED tier — a committed engine revision, the
quiet gate, the window handshake, into `store/`):

    python3 -m pcrecbench testees            # the config ids
    python3 -m pcrecbench quiet --samples 5  # is the box quiet? (OD-B8)
    python3 -m pcrecbench run --subbench email --testee pcre2-jit --trials 5
    python3 -m pcrecbench index

The EDIT-TEST LOOP (the SCRATCH tier — Frank's I-4, [B10]; seconds, not
minutes; no quiet gate but the box is still sampled and `status` is
honest; records go to `build/scratch-store/`, never to `store/`, never
into a ranking):

    # one pattern x one regime x the first k subjects, one or two testees,
    # the comparable printed inline (the reporter's own set-grain reduction)
    python3 -m pcrecbench quick --subbench email --pattern orig \
        --regime search --testee pcre2-jit --vs pcre2-interp --subjects 10
    # a PROVIDED pcrec binary, no pin: scratch tier by construction
    PCREC_BIN=~/pcrec/worktrees/x/build/pcrec PCREC_LOCAL_FLAGS="--engine=vm" \
        python3 -m pcrecbench quick --subbench email --pattern orig \
        --regime search --testee pcrec-local --vs pcre2-jit
    # a whole cell at the scratch tier (e.g. a pinned testee on a busy box)
    python3 -m pcrecbench run --subbench email --testee pcrec-auto --tier scratch
    python3 -m pcrecbench index --store build/scratch-store   # its own index

A `run` exits 0 (written), 3 (the pre-flight refused, nothing written)
or 4 (v1.4: written and indexed as `inconclusive-spread` — the box was
quiet, the five trials did not agree; `scripts/run_window.sh`
re-measures such a cell once). `run --tier scratch --store store` (or
`--testee pcrec-local --store
store`) is REFUSED before anything is measured: the canonical store's
`.canonical` marker is what `store.py` checks, on write and on index.

The subject trees are GENERATED and gitignored — run
`python3 bench/email/gen_subjects.py` and
`python3 bench/email/gen_throughput_subjects.py` before the first run
(`make check` does it for you).

Plain GNU make for what is ours (pcrec's D2 posture: a stranger's `make`
must work). Each testee adapter under testees/<name>/ may use whatever its
engine demands (C shims, cmake, cargo), pinned there.

## Conventions (inherited from pcrec where they apply)

- Every directory has a CLAUDE.md describing purpose and files; update it
  when files are added/removed or change roles.
- Update the STATE tag in docs/dev/plan.md when starting/finishing a step;
  expand a milestone into substeps only when work on it begins; append a
  dev_journal.md entry after every significant session and at every stage
  boundary of an autonomous run (journal defensively).
- Measurement discipline travels from pcrec (its docs/dev/learnings.md
  §1-3, D12/D14/D15/D17/D35): quiet-box runs, medians with spread, per-core
  occupancy checked before pinned runs, environment recorded, archived
  probes with source headers, controls that share no source with what
  they control.
- Subagents as needed, lower models where the work fits; writers in
  worktrees under `worktrees/`; critics read-only; every brief restates
  the mandate and the box rules; long runs asynchronous with a stall
  watchdog. Details in the skill.
