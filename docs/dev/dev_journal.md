# pcrec-bench Development Journal

Append-only log for restart/status recovery. Newest entries at the bottom.
Each entry: date — summary; accomplishments, issues, decisions, next steps.
Cross-reference docs/dev/plan.md row ids ([Bn]) and docs/dev/decisions.md
ids (BDn); pcrec's as `pcrec D52` / `pcrec [BENCH-1]`.

---

## 2026-08-24 (EDT), first session (pcrecdev2) — housekeeping; the requirements discussion opens

Context: Frank opened a SECOND manager session on the box (`claude -n
pcrecdev2`, started in ~/pcrec for access to its docs) and assigned it
~/pcrec-bench, which had sat at its 2026-08-17 seed (APPROACH.md +
CLAUDE.md, two commits, no code) while pcrec built its feature spine.
The pcrec manager session (pcrecdev1, the thirty-ninth pcrec session,
mid-[DD-14] with waves A-F merged, wave G and a D27 landing in flight, a
`make san` on main) is live on the same box; Frank asked the two to
coordinate directly. pcrecdev1 sent its box rules (load, git, /tmp, no
pkill -f, report failures) — accepted and recorded as BD2/BD3 — and a
complete reference dump of every pcrec-bench mention in pcrec (now
docs/dev/pcrec_references.md).

Accomplished ([B0], archived to plan_completed.md):
- docs/{dev,design} in pcrec's shape: plan.md ([B1] started, [B2]-[B7]
  placeholders from APPROACH §8 Q5, explicitly not commitments),
  plan_completed.md, this journal, decisions.md (BD1-BD3), wake.md
  (gitignored), pcrec_references.md (the map: D52, D12/D14/D15/D17/D35,
  [BENCH-1], [BENCH-CEIL], [ENG-PGO]'s profile cross-note, [DD-13]'s
  R-BENCH-1..9 and Frank's format inputs, the email specimen harness,
  the libpcre2 ctypes binding, learnings §1-3, K31/K32/[TT-10]).
- CLAUDE.md at every level (root rewritten from SEED to "housekeeping
  done, requirements open"; docs/, docs/dev/, docs/design/).
- .gitignore (wake.md, worktrees/, build trees).
- `.claude/skills/pcrec-bench-manager/SKILL.md` — the manager skill,
  modelled on pcrec's `pcrec-manager` with this repo's wake order, the
  two-session rules, and the delegation/watchdog/async conventions that
  pcrec paid for.

Read this session (pcrec, read-only): wake.md (pcrecdev1's mid-session
checkpoint), journal parts 1-18 of the thirty-ninth session, plan rows
[DD-14.*]/[BENCH-1]/[BENCH-CEIL]/[DD-13], D52/D71-D73, dd13_format
requirements §5 + frank_inputs.md, tests/bench + compare/ CLAUDE.md, the
email specimen README.

Facts worth carrying: (a) APPROACH §8 Q1 (set format) is resolved IN
DIRECTION — owned by pcrec's [DD-13], whose design/panel steps have not
started; an interim carrier is this project's problem. (b) No feedback
mechanism into pcrec's plan exists; pcrecdev1 proposes rows keyed by the
artifact's mechanism stamps (engine, RX_VM_PREFILTER, RX_VM_RUNGS) so
outliers bucket by mechanism. (c) Engines Frank has named: libpcre2 10.46,
perl 5.40.1, python re; no roster ruled. (d) The email specimen is a
ready-made first row with a dlopen libpcre2 throughput harness (no
pcre2.h on the box). (e) The box lies under load; bench on a quiet box.

Next: [B1] — the overall-requirements discussion with Frank (points to
put to him listed in wake.md), then docs/design/requirements.md and its
critic panel.

## 2026-08-24 (EDT), first session (part 2) — the requirements RULED (R1-R11); requirements.md DRAFT v1; the critic panel opens

Frank ruled the eleven requirement points in conversation (~22:5x-23:3x):
R1 loop-first (positioning second); R2 three subject regimes — large-
subject throughput, short-subject search (~256 B), and MATCH/compliance
on 10..1000 B subjects (bands TBD) — plus compile/setup cost on its own
axis; R3 HARNESS FIRST — the roster is for design and grows later,
COMPILERS included; per-(pattern, testee) OUTCOME is an axis (compiled /
did-not-compile / crashed / timed-out / unsupported), and a SYNTAX-VARIANT
axis admits engines that are not PCRE2-exact (same intention, declared
adaptation); testee dimensions = hardware, version, categorization
(interpretive/compiled/JIT; DFA/NFA/backtracking/hybrid); the hand-C
ceiling arm explained and ruled NOT in the first cut; R4 pcrec is the
special case — its variations are separate testee engines (later SIMD
on/off); R5 the SUB-BENCH is the unit: a self-contained DIRECTORY with a
goal, possibly several related patterns, data files, engine-specific
notes/adjustments; a RECORD = one sub-bench × one testee configuration
with all factors (date, hardware...); records gathered INDEPENDENTLY,
never the whole gamut; the product is data gathering + reporting; R6
the pattern format BLOCKS on pcrec's [DD-13] ("the rxt should be coming
pretty soon") — design and gather until blocked, then stop, no interim
carrier; R7 JSONL record with a general-setup layer + N raw results
reduced to comparables (min/max/stddev... TBD); R8 correctness as
chartered, tempered by the goal of RELATABLE, ACTIONABLE data — the same
pattern INTENTION may be expressed by a modified pattern per engine and
still compare (deviation grades = manager's sharpening, unruled); R9 the
deliverable is a QUERY-DRIVEN REPORT over the store ("sub-bench A1,
open-source, compiler-only"); delivery into pcrec case by case until the
model is clear (pcrecdev1 may not be running); R10 check load and wait
until quiet; R11 the first cut agreed in substance, changeable after
design.

Written: docs/design/requirements.md DRAFT v1 (13 sections: purpose,
vocabulary, regimes, testees + outcome + variant axes, sub-benches,
record, correctness, reporting, box discipline, first cut, APPROACH §8
dispositions, OD-B1..B8, the panel attack list). General rule from
Frank: commit often, push as needed (no remote configured yet; branch
here is `master`). Housekeeping committed 7789bd1. Next: the D6 panel
(three read-only sonnet critics: data model/report completeness;
semantics/variant axis/charter consistency; blocking point/first cut/
measurement validity) → triage → Frank adopts → [B2].

## 2026-08-24/25 (EDT), first session (part 3) — the R1 panel: 29 findings, 27 applied in requirements.md v2; two rulings owed

Three read-only sonnet critics (A data model/report, B semantics/
variant/charter, C blocking/first cut/measurement) returned 11 + 9 + 10
findings; the manager re-read every load-bearing citation (all held:
mpstat installed; uutils timeout ~108.7 ms/call; GCC-TIME 1.87× single-
sample swing; RX_VM_* are structured masks; the LC_ALL=C lesson). Record
docs/dev/reviews/2026-08-24-r1-requirements.md. The HIGHs, all fixed:
record identity collided at date granularity (→ timestamp + hash);
"run" undefined (→ run/cell/record/trial defined); pcrec-only mechanism
stamps contradicted "one more file in the pile" AND had no shape (→ a
generic enumerated engine_metadata map read from structured fields, the
prose RX_ENGINE_WHY unindexed); build config free text on the headline
filter axis (→ captures/engine_mode/simd as fields, flags blob for
reproducibility only); compile cost did not fit the row shape and lazy
JIT has no separable call (→ COMPILE rows keyed pattern×trial, a per-
execution-model protocol, trial 1 excluded for lazy JIT, median-of-N —
gcc is not a clean single number); per-trial gnutimeout would BE the
signal in the 10..1000 B regimes (→ batched in-process loops, timeout on
the outer process only); the middle deviation grade undecidable (→ TWO
grades, stated differences are expectations — manager ruling, vetoable);
capture-restructuring variants uncheckable (→ mandatory capture
correspondence, OD-B9); plan.md [B3] still proposed the interim carrier
§5 forbids (→ row rewritten). MEDIUMs: truncated-subject outcome +
consumed_length; runtime compile options recorded and covered by
variants; N + pass-rate mandatory on partial coverage; hazard/size tags
re-assertable per variant; convention per case with per-testee
capability; load sampled after as well as before (inconclusive-load
status); mpstat occupancy machine-readable; 1 MB subjects disclosed as
smaller than pcrec's 8-64 MB convention (OD-B10); LC_ALL=C; OD-B4 split
into enums vs normalization rules; OD-B8 given an owning row ([B3]).

OWED TO FRANK before adoption: (1) the BLOCKING SCOPE — the panel
measured that [DD-13b/c] have no queue position in pcrec's plan and
[DD-14] is still growing, so "the rxt should be coming pretty soon" is
not supported by the plan file; NARROW reading (block only a new cross-
sub-bench grammar; parse today's .rxt, wrap the specimen, plain sidecar
of R-BENCH fields) vs BROAD (no carrier at all; M1 shrinks to schema +
an adapter on the specimen's files) — manager recommends NARROW; (2) the
two-grade variant scheme (veto restores three).

## 2026-08-25 (EDT, ~00:0x), first session (part 4) — requirements ADOPTED (v3, 8c34498); [B1] closed; [B2] the record schema opens

Frank's two rulings: the blocking scope is NARROW ("narrow is fine to
proceed" — today's .rxt may be parsed as-is, the specimen wrapped, a
plain sidecar of R-BENCH fields; only a NEW cross-sub-bench grammar is
[DD-13]'s and blocked); and variants carry two CONSTRAINTS instead of
grades — (1) the results must be the SAME on every subject, no
variation (the "approximates" idea is gone; a differing variant is
unsupported-by-declaration or the testee is wrong), (2) the sub-bench's
OBJECTIVE must be achieved (a subroutine sub-bench may not be satisfied
by rewriting the subroutines out) — so the sub-bench gains a declared
OBJECTIVE field and a variant declaration states how it preserves it.
Note v3 written; [B1] archived; the [DD-13b] inputs (directory model,
objective, outcome enum, variant constraints, regime declaration) handed
to pcrecdev1 by message. [B2] opened: lane b2schema (opus, worktree
worktrees/b2schema, branch lane/b2schema, brief scratchpad/
brief_b2schema.md): docs/design/record_schema.md, schema/record.schema.
json (draft 2020-12; jsonschema 4.19.2 is installed), schema/validate.py
with cross-line rules, a SYNTHETIC example record + six sabotaged
rejects as positive controls, `make check-schema`, CLAUDE.md files.
Watchdog cron (10 min) up. Box: nothing heavy from this side; pcrecdev1
reports the box light until wave G delivers.

## 2026-08-25 (EDT, ~00:2x), first session (part 5) — AUTONOMOUS RUN AUTHORIZED: through the first sub-bench and a report, then close

Frank (~00:2x): "proceed autonomously through setting up first subbench
and generating some report. coordinate with pcrecdev1 of course but
also notify of results and request feedback — noting this is a
production sample. also, should ask about higher-priority subbench
areas. save open questions for later but go with recommendations for
now. journal defensively. then close session and i'll review results
with you in next session." Also today: BD4 python project files
(ab68080); APPROACH.md rewritten as the MAINTAINED high-level statement
(15854b0) with the maintenance rule in CLAUDE.md + the skill; component
directory names chosen — bench/, testees/, schema/, store/, report/ —
flagged to Frank, unobjected so far.

PLAN for the run: [B2] lands (lane b2schema is at its examples) →
review, merge, a 2-critic schema panel in parallel with [B3]+[B4] →
[B3] harness core (bench/ conventions, the email specimen wrapped as
bench/email/, the quiet-box instrument, the run-cells driver, the
store) and [B4] adapters (libpcre2 interp/jit via a dlopen C driver
with batched in-process loops; pcrec built from a PINNED commit via
`git archive` into a gitignored build dir — never pcrec's own tree) on
a manager-written adapter contract → [B5] the reporter MVP → [B6] cells
run on a quiet box in a window agreed with pcrecdev1 → the report sent
to pcrecdev1 as a production sample with a feedback request and the
question of higher-priority sub-bench areas → journal, wake.md, close.
Open questions are saved to the OD ledger, recommendations taken.

## 2026-08-25 (EDT, ~00:0x), first session (part 6) — [B2] MERGED (the record schema); [B3]+[B4] and [B5] lanes open; pin 8da6120 building; a quiet window promised ~03:00

Lane b2schema (opus) delivered in ~40 min: record_schema.md (718
lines — identity tuple + content hash with the circularity broken,
file name = record_id, schema versioning + mixing policy, OD-B4
answered in both halves, per-testee engine_metadata declarations with
pcrec worked from rx_info/RX_VM_* masks as bit-name arrays, 131 fields
checked field-for-field against the JSON Schema by check_fields.py,
cross-line rules X1-X17), validate.py, 2 synthetic examples, 15
sabotages each named for the rule it must fire (`--expect-rule`), the
gate itself sabotage-validated. Manager ran the gate (2/15/0 WRONG) and
merged. MERGE INCIDENT: two CLAUDE.md conflicts + a command chain that
continued past a heredoc committed a merge WITH CONFLICT MARKERS
(285cb39, never pushed); caught within a minute by grepping for
markers, reset to 64f4655, merged again by hand, verified. Lesson: a
`&&` chain does not extend across a heredoc terminator — commit steps
get their own command. Accepted at merge (Frank: go with
recommendations): per-subject `crashed`/`timed-out` (requirements §4.4
amended), dense trial numbering, the lazy-JIT compile row carrying a
derivation and no number. Post-merge panel: critS1 (data model vs
consumers; new sabotages the 15 controls miss), critS2 (provenance:
how each environment field is obtained on this box; what compare.sh
records that the schema lacks).

docs/design/harness_contract.md written (manager): package layout,
bench/<name>/ with a subbench.toml SIDECAR (fields only), the adapter
interface + a shared DRIVER PROTOCOL (batched in-process loops, phases
timed, TSV), store path = record_id.jsonl, CLI run/index/report, the
quiet instrument (OD-B8 measured at [B3]), self-checks. Lanes opened
from 7b57ad0: b3harness (opus: harness core + bench/email/ + pcre2 and
pcrec adapters) and b5report (sonnet: the reporter over fixtures).
pcrecdev1: PIN = 8da6120 (its diff-stat vs main over src/lib/cli/
Makefile is EMPTY — same compiler; battery-run tree); the pin build
started 00:00 (-j4, gnutimeout 900, build/pcrec-8da6120/, log in the
scratchpad) inside its 20-minute ask; QUIET WINDOW promised after wave
G's merge battery (~03:00 est.): it sends "WINDOW OPEN" with the load
reading, I reply "WINDOW CLOSED"; nothing heavy of its runs between.
Watchdog re-armed for both lanes + the build.

## 2026-08-25 (EDT, ~00:2x), first session (part 7) — the schema panel's S2 report: four provenance HIGHs; schema v1.1 lane opened

critS2 (measurement provenance) returned 13 findings + one example
defect. HIGH: (1) the lazy-JIT "trial 1 minus steady state" derivation
is NOT computable from a record — trial numbering restarts per
(pattern, subject, regime) and row order is declared insignificant, so
nothing identifies the chronologically first row that paid the JIT
cost (fix: a per-row `seq`; derive over the lowest seq); (2) `load` has
no raw evidence — `status: measured` is claimable on fabricated
numbers (fix: /proc/loadavg raw + timestamp per sample); (3) occupancy
is sampled ONCE while load is before/after — the poisoned-core lesson
re-opened for the dimension that caught it (fix: before/after); (4) the
harness contract promises the iteration calibration is "recorded in
the record" and no field exists (fix: a per-row calibration object).
MEDIUM: engine_commit optional despite "pcrec ALWAYS pinned"; no
driver build flags; subject sha256 optional vs pattern sha256 required;
`quiet_attestation` provably inert and used inconsistently in the
lane's own example (dropped); the §6 normalization rules are prose,
unchecked. LOW: cpu MHz, clock source, hugepages, chrt+taskset pinning.
All accepted (Frank: recommendations) → lane b2fix (opus, worktrees/
b2fix, brief_b2fix.md): schema version 1.0 → 1.1, one named control per
new rule, ≥ 25 sabotages. b3harness and b5report told what is coming.
critS1 went idle without delivering; asked to resend. Watchdog covers
three lanes.

## 2026-08-25 (EDT, ~00:4x), first session (part 8) — [B3]+[B4] DELIVERED (lane/b3harness 36c77ad); [B5] delivered with the set grain; v1.1 nearly done

b3harness (opus, ~45 min, 11 commits, +6085): pcrecbench/ (subbench,
quiet, env, adapters, driverrun, record, harness, store, CLI run/index),
bench/email/ (the specimen wrapped: sidecar, both patterns, generators
copied, manifests with sha256, 330 expectations re-derived from libpcre2
10.46 by gen_expectations.py --check, NOTES.md with the objective),
testees/pcre2 (dlopen driver, interp + jit) and testees/pcrec (driver +
shim, pin.sh reusing the manager's build, three configs), tools/
selfcheck.py = `make check` 15/15 with controls (manifest byte-diff,
wrong-expectation fixture, subject-timeout by name, TWO-PATTERNS
control). Manager re-ran make check in the worktree: 15/15, pcrec's
tree untouched. FINDINGS worth the record: (1) a hidden bug — both
patterns compiled into one workdir, the second measured under the
first's handle; the email expectations could not see it (both patterns
agree everywhere); found via engine_metadata (orig reporting VM
give-ups when it selects DFA); fixed by pattern_id in the interface and
guarded by the two-patterns control — the class of bug only a
mechanism check can see; (2) OD-B8 MEASURED under pcrecdev1's load:
load1 1.28-1.47 never tripped a 2.0 gate while per-core occupancy
refused 12/12 samples (worst core 62-81% idle) — occupancy is the
DETECTOR, load1 the backstop; proposed MAX_BUSY_PCT 10, LOAD1 2.0,
re-measure on a quiet box; (3) the smokes reproduce srEmail from
scratch (330/330 oracle agreement; five FRAMES give-ups on factored;
DFA+prefilter vs VM). Twelve contract deviations written up in
docs/design/harness_notes.md; RULED at review: sidecar extension
accepted; match regime = the engine's own whole-subject test (pcrec has
no end-anchored entry — raised with pcrecdev1 as a candidate finding);
give-ups get their own schema outcome `gave-up` (fix 21 to b2fix).
b5report (sonnet): reporter MVP eafb68f → 156da15 with `--grain
set|subject` (default set: per-trial sum of per-subject ns/call over the
set), 16/16 tests, fixtures restamped; holding for v1.1. b2fix: fixes
1-11 landed (23 rules, 36 controls, check_rules.py — five rules had had
no control through a merge and a panel), fixes 13-21 in progress.
Merge order: b2fix → b3harness (adapt records to v1.1) → b5report
(restamp) → cells on the quiet window → report.

## 2026-08-25 (EDT, ~00:5x), first session (part 9) — the whole-subject idiom measured; two pcrec findings filed; v1.1 at fix 21; window ~02:50

pcrecdev1 answered the whole-subject question from pcrec's docs, not
memory: PCRE2_ENDANCHORED is a RATIFIED, UNBUILT generation axis (D38,
[OS-4]); the bench is now its first named customer; the intended idiom
is `(?:P)\z` under the anchored entry (never `$` — it matches before a
final newline at options=0), a DIFFERENT artifact that must never share
a row with the plain one. Adopted: schema v1.1 fix 22 = `form` (plain |
whole-subject) on compile and match rows; pcre2 omits it (runtime flags
on the plain compile); pcrec compiles both forms and times both.
b3harness MEASURED it on 8da6120: orig's `\z` form keeps DFA (+12.4%
emitted C), factored stays VM; the `a|ab`/`ab` control proves the plain
anchored `==n` stand-in answers wrongly vs the oracle (the email corpus
never hits it). TWO pcrec FINDINGS from that measurement, sent to
pcrecdev1 as candidates: (1) the DFA prefilter has NO structured stamp
(RX_VM_PREFILTER is VM-only; DFA artifacts define only RX_ALTCLS_*), so
the email specimen's headline mechanism cannot be bucketed on DFA
records — request a DFA-side stamp; (2) the `\z` form's skip loop
cannot skip the final byte or early-exit (the end-of-subject view
state must be evaluated) — a slightly higher match-regime scan cost,
documented so it is not misread. b3harness also: store writes now
O_EXCL-claimed + staged + validated + os.replace (its own 8-writer race
control caught a shared staging dir: 6/8 → 8/8); occupancy sampled at
both ends, verdict = the worse; all v1.1 fields already MEASURED behind
a projection switch with a three-leg control; pin.sh's build path
exercised (cold 3.47 s, reuse 0.01 s, both pin binaries emit
byte-identical artifacts). b2fix: my first three messages never
reached it (lane inbox delivery unreliable tonight — ask for ACKs);
the consolidated resend landed; at fix 21 of 22. pcrecdev1: window
slips to ~02:50 (srG's rows at 0.8/min). Chain unchanged.

## 2026-08-25 (EDT, ~01:1x), first session (part 10) — SCHEMA v1.1 MERGED (ae9b0d0): 27 rules, 53 controls; both build lanes adapting

b2fix (opus, ~70 min, 21 commits, 64 files) landed all 22 fixes of the
R2 panel plus three of its own (X20 load verdict follows the numbers,
X24 bytes_processed bound, X26 occupancy verdict follows its limit):
seq, load/occupancy before+after with raw evidence, calibration,
engine_commit required for non-release versions (X22), driver build
flags/compiler/clock source, subjects sha256, quiet_attestation dropped,
normalization checked (X23), consumed_length bound (X25), `gave-up`,
`form` plain|whole-subject (X27, X9/X11/X14 keyed per (pattern, form)),
.gitattributes for the hash, check_rules.py (every §9 rule has a named
control — five had none through a merge and a panel). Gate re-validated
five ways at the final state. Lessons recorded by the lane: an
INDEX-KEYED sabotage mutator does not fail when the file shifts — it
silently sabotages a different row (eight mutators rewritten to locate
rows semantically); a control that fails for three reasons is not a
control (X21/X24 now skip iterations < 1 so the zero-iterations control
fires exactly the schema rule). Merge clean, gate 2/53/0 on master;
requirements §9(b) amended with the strict-occupancy ruling; harness
contract already carried the rest (2ac7fcf). Message delivery to lane
inboxes was unreliable in one direction tonight (three manager→b2fix
messages lost; lane→manager always arrived) — the consolidated resend
with an ACK request worked; briefs should ask for ACKs on rulings.
b3harness and b5report told to merge master and adapt (flip
SCHEMA_VERSION, form, gave-up range rule, a|ab control; fixtures
restamped, lazy-JIT over lowest seq). Window ~02:50.

## 2026-08-25 (EDT, ~01:1x), first session (part 11) — [B3]+[B4] MERGED (42c0557): the harness runs every cell; make check 21/21 on master

b3harness's v1.1 pass merged clean (18 commits total): SCHEMA_VERSION
1.1 emitted directly (the projection deleted), `form` on pcrec's rows
(pcre2 omits), `gave-up` via the range rule against the shim-exported
floor (pcrec floor −5 / top −2 / internal −6 MEASURED at the pin) and
pcre2's four configured-budget codes, `occupancy.limit_busy_pct`,
calibration on rows with iterations > 1, three new controls (the `a|ab`
control anchored to libpcre2's answer, not pcrec's; separate artifacts
per form so X27 is not vacuous; v1.1 fields populated on a real record
at --iters 2 so X21 triggers). Three staging assumptions the merged
schema overturned, recorded by the lane: no combined occupancy verdict
(each sample carries its own, X26 recomputes it); probe_iterations has
minimum 1, so fixed --iters runs a real probe and notes that the count
was not derived from it; env.py imports the normalizers from
validate.py (X23 checks them). During the pass the box went quiet
mid-run and the strict both-ends rule made pcrec-auto/-nocaps
`inconclusive-load` on the AFTER sample — the rule working; the window
must be idle throughout, not just at the start. Manager: make check on
master 21/21 + 2/53/0; worktree removed; pcrec's tree 0 status lines
throughout. [B3]/[B4] archived. Remaining before the report: b5report's
v1.1 restamp → merge → the window → run_window.sh → `report`.

## 2026-08-25 (EDT, ~01:3x), first session (part 12) — [B5] MERGED: the whole M1 tool chain is on master; make check = 2/53/0 + 21/21 + 18/18

b5report's v1.1 pass merged (four seams resolved by hand: Makefile
targets unioned with `check` depending on all three suites; the
harness's __init__/__main__ kept, `report` dispatched to
pcrecbench.report.main BEFORE argparse so the reporter owns its flags;
pcrecbench/CLAUDE.md combined). The reporter: --grain set (per-trial
sum of per-subject ns/call over the set) default, subject drill-down;
gave-up counted apart from wrong; form beside numbers only when a
non-plain form is present; lazy-JIT derived over the lowest seq (unit-
tested on rows where the lowest seq is NOT trial 1 of any cell);
mixed_version fixtures split into major_mismatch (1.1 vs 2.0 refused)
and minor_pair (a 1.0-shaped record is simply invalid under 1.1 and
drops via the per-record path). make check on master: schema 2/53/0,
harness 21/21, report 18/18. [B5] archived; [B6] started: the window
run is staged (scratchpad/run_window.sh); waiting for pcrecdev1's
"WINDOW OPEN" (~02:50). All three lanes' worktrees removed, branches
kept: lane/b2schema, lane/b2fix, lane/b3harness, lane/b5report.

## 2026-08-25 (EDT, ~01:3x), first session (part 13) — the window REHEARSAL: one registry gate, one real harness bug (X21 caught it), the reporter renders real records

Rehearsed the exact window script (scratchpad/run_window.sh; STORE/
EXTRA/LOG overrides added) into a scratch store, --trials 1 --synthetic
--force-unquiet, on the loaded box. Rehearsal #1: all five cells rc=1
in one second — the scratch store had no machines.tsv and the harness
refused an unregistered box (the registry gate working; the real store
carries it). Rehearsal #2: 4/5 cells wrote validated records (all
`inconclusive-load`, correctly: load1 3.4-4.3 against the 2.0 limit,
worst cores 30-60% busy); pcre2-jit was REJECTED by X21 and NOT written
— harness.py:252 computes iters = int(target/median) (truncation):
probe 24.79 ms/iter → 2 iters predicted at 49.58 ms < 50 ms target, no
calibration_note. The rule the R2 panel asked for (S2-4) caught a real
bug on the first real record it saw. Fix request to b3harness on
worktrees/b3fix (ceil + a note when the sweep cap lowers the count + a
control at the just-above-integer ratio). The reporter renders the four
real records (set grain, form shown, compile costs by class, excluded
table) — first sight of real numbers, none of them a measurement.

## 2026-08-25 (EDT, ~01:4x), first session (part 14) — both rehearsal findings fixed and merged (11d91d6, 7cf98b3); make check 24/24 + 20/20 + 2/53/0; staged for the window

Reporter (lane b5fix 5bf987b): `form` was a SPLIT key in the ranking, so
pcre2 (plain, runtime flags) and pcrec (whole-subject artifact) never
shared a compliance table — the regime's whole point; now form is a
per-row column within (pattern, regime) and a key only for compile-cost
cells; tests 20/20; the rehearsal report now ranks all four testees on
orig/match-compliance in one table. Harness (lane b3fix 46d44df): TWO
bugs under the X21 rejection — floor→ceil, and the recorded probe was
the sweep SUM while the count came from the MEDIAN subject; now the
count is chosen by X21's own expression over the integers the record
carries (smallest meeting the target) and the probe describes the
median subject; a three-leg control, sabotage-validated. The lane
corrected its own diagnosis en route: bug (2) was a FIDELITY bug, not a
validity one — with the count derived from the recorded integers X21
passes for any probe — found only by sabotaging the fixed code and
watching a leg pass that should have failed. Lesson for learnings: a
control is proven by the sabotage that makes it fire, not by the
diagnosis that motivated it. Also from the rehearsal: pcrec-vm posted
the fastest compliance number on orig (single trial, loaded box — NOT a
measurement; the window decides). Window ~02:50; run_window.sh staged
(5 cells, --trials 5, --pin 11; expect ~20-40 min).

## 2026-08-25 (EDT, ~03:0x), first session (part 15, CLOSE) — [B6] DONE: the first production sample measured, reported, sent; M1 complete

THE WINDOW: pcrecdev1 opened it early (02:21, load 0.42 — its sweep had
stopped on its own at row 48 and it held the resume). run_window.sh ran
02:22-02:49: pcre2-interp, pcre2-jit, pcrec-nocaps, pcrec-vm `measured`
(both occupancy samples pass); pcrec-auto REFUSED by the gate (rc 3) on
a 1-s transient (12.12 % on one core the second after the previous
cell exited); re-run refused again (28.71 %); a retry loop passed on its
second attempt (02:50-02:55) → `measured`. The transients are the two
claude sessions' own CPU (~6-8 % each) plus a stray `gh` — a real
finding for the gate (OD-B12: retry/multi-sample before loosening the
limit). WINDOW CLOSED 02:56, load 1.25; 34 min used of 45 promised.

THE REPORT (reports/2026-08-25-email-specimen-0.1-budu-ryzen1600.md, set
grain; the first `--subbench email` query matched nothing — the sidecar
id is `email-specimen`, OD-B13): orig/short-search pcrec-auto 6.13 µs ≈
pcre2-jit 6.28 µs (interp 65.7); orig/throughput jit 9.08 ms, pcrec-auto
13.40 ms (0.464x), interp 28.9 ms, pcrec-vm excluded (STEPS give-up on
the 'a'-run); orig/compliance (whole-subject) pcrec-vm 101 µs (0.188x)
BEATS pcrec's own DFA 235 µs (0.437x) 2.3× — the first outlier bucketed
by mechanism; pcre2 536-537 µs; factored: pcrec FRAMES give-ups on the
same 5 deep subjects in all three configs, STEPS on the 'a'-run, and a
5.4× loss on short search vs jit (the wave-G target) — srEmail's
findings reproduced as records; compile cost on its own axis (pcrec
118 / 420 ms; pcre2 14 µs / jit 160 µs). UPSTREAM U1: pcre2-JIT hit the
60 s per-subject alarm on factored × 1 MB 'a' (5/5 trials) where the
INTERPRETER answers in 17.8 µs/iteration — likely the interpreter's
start-of-match prescan; filed in docs/dev/upstream_findings.md with the
pcre2test reproduction as the next step. Records + index + reports
committed (bf4a415); the report sent to pcrecdev1 as the PRODUCTION
SAMPLE with Frank's two asks (feedback on the shape; a ranked list of
higher-priority sub-bench areas) — its answer arrives next session.

M1 ([B0]..[B6]) is complete in one session. Commits on master: 7789bd1
… b3ab30b (+ this close). Not done / owed: the M1 close panel over
harness_contract + harness_notes (D6); OD-B10 (1 MB vs 8 MB spread);
OD-B11/B12/B13; a re-pin of pcrec after wave G merges; the second
sub-bench (Frank's call after pcrecdev1's list); no remote configured
(branch `master`). Session closes here; Frank reviews next session.

## 2026-08-25 (EDT, ~03:3x), first session (part 16, addendum after close) — pcrecdev1's feedback on the sample, recorded for Frank

pcrecdev1 answered before I closed (docs/dev/feedback_pcrecdev1_2026-08-25.md,
verbatim in substance). Actionable: yes; missing — the artifact's
strategy stamps as bucket COLUMNS (the records carry them; the reporter
does not show them yet), give-ups as first-class with the SIZE at which
they first fire (a size-sweep design item), the compile axis SPLIT by
phase (the phases are in the rows; reporter), a per-call FLOOR control
pattern in every short-subject set. Distrust: the 2.3× "VM beats DFA"
on compliance is a REGIME ARTIFACT of the \z form's weaker skip loop —
bucket it so, keep it out of the outlier queue until [OS-4]; short-
search ratios sit near the timer floor; factored's 5.4× loss is
PRE-wave-G and should collapse on the re-pin (if not: the first real
outlier); U1 needs the discriminating measurement — the interpreter with
PCRE2_NO_START_OPTIMIZE on the same cell. RANKED sub-bench areas: (1)
log-line search 256 B–4 KB, (2) wide alternations / keyword tries, (3)
lookaround + backreference real-world shapes, (4) bounded-repeat /
ambiguous-decomposition band, (5) UTF-8 classes/properties. Re-pin:
wait for its battery-green SHA. Nothing acted on tonight — Frank
decides next session.

## 2026-08-25 (EDT, 07:45), post-close note — the re-pin target from pcrecdev1: ae9c98c (battery-green [DD-14] tree)

pcrecdev1: RE-PIN TO ae9c98c — compiler byte-identical to 17469b6 (the
[DD-14.FB] merge; everything after is tests/docs); evidence on that
compiler: full sabotage matrix 180 rows, make test 26,843/0 (the two
red checks = the load-sensitive 45 s resource-cap cells, solo 19/0),
make san clean both axes. What changed for the bench since 8da6120:
wave G (subroutine SPLICE + dead-capture elision + prefilter restored —
the email specimen's factored form now compiles to the SAME DFA artifact
as orig, so the factored/short-search 82 µs row should collapse to
orig's on re-measurement); wave FB (three `_in` entries taking a
caller-provided frame buffer; rx_info abi 2→3 with four sizing fields;
`<P>_*_FRAMES`/`_FRAME_SIZE` macros — a stamped 0 means no buffers,
check before dividing). ACTION FOR THE NEXT SESSION (not done tonight):
testees/pcrec/configs.toml pin → ae9c98c; any `abi == 2` read in the
adapter → 3; pin.sh builds the new snapshot; re-run the five cells in a
new window; the report over both pins is the first before/after.

## 2026-08-25 (EDT, ~12:4x), second session (part 1) — wake: the inbox acknowledged, the M2 queue drafted, BD5, the outbox created

Woke per the skill. Box quiet (load 0.38; pcrecdev1 up and busy).
Between the first session's close and now, the pcrec manager committed
inbox I-1..I-4 here (c576c5b), committed pcrec's D78 into THIS repo's
decisions.md by mistake (d12abed, reverted 91e9251 — D78 lives in pcrec
as aede6fd) and updated the manager skill (f4e65d3). The re-pin target
moved from ae9c98c (post-close note) to 692c2e8 (I-1: same compiler, the
tree the battery was scored on).

Done this part, one commit: plan.md gets the M2 queue — [B8] re-pin
692c2e8 + before/after (I-1), [B9] reporter follow-ups from pcrecdev1's
feedback (stamps as columns, compile phases, the regime-artifact bucket,
OD-B11..B13; I-3's DFA stamp gap noted on the row), [B10] the edit-test
loop (scratch tier, `quick`, `pcrec-local`; I-4, after [B8]), [B11] the
five sub-benches in Frank's order (I-2), [B12] the M1 close candidates
(close panel, U1's NO_START_OPTIMIZE probe, OD-B10); [B7] unchanged.
One `ack:` line under each inbox item. BD5 records the channel and the
division of labour as a pointer to pcrec D78 (why the copy here was
reverted). docs/dev/outbox_to_pcrec.md created: O-1 (acks), O-2 (the
`pcrec-auto-in` question — bench position: a separate roster entry per
requirements 4.2; needs the FB macro names / `_in` signatures at
692c2e8), and the standing items owed to pcrec. docs/dev/CLAUDE.md lists
both channel files. Verified: no `abi == 2` check exists in the adapter
(driver.c:199's `== 2` is the engine id), so the abi 2→3 step of [B8]
is a record-field check. Nothing else started — Frank reviews the first
sample and the queue order this session.

## 2026-08-25 (EDT, ~13:0x), second session (part 2) — O-2 answered by pcrecdev1: the frame-buffer contract is pcrec docs/spec/match_api.md §10

pcrecdev1 answered O-2 interprocess within minutes (the durable file
carries what outlives a session; live questions still flow live — D78
as intended). Recorded in place under O-2, in [B8]'s row, and as a
pcrec_references.md row (the spec's §10.2/§10.4/§10.6 verified present
at pcrec 6c676b2, read-only). The facts that shape the `pcrec-auto-in`
adapter: the `rx_buffers` descriptor (frames in FRAMES, trail in
ENTRIES, both required, pure scratch, never shared across concurrent
calls); the four sizing stamps are PER-ARTIFACT (`RX_RESUME_FRAME_SIZE`
is 40 B on the email pattern and 24 elsewhere) and mirrored as
`rx_info` fields — read them, never hardcode, and never divide by a
stamped 0; a DFA artifact has the `_in` entries and ignores the
descriptor. pcrecdev1 concurs with the separate-roster-entry reading of
requirements 4.2; the record must carry the buffer sizes USED. Box:
pcrecdev1 has three lanes up (-j4 builds, targeted suites), no heavy
suite until a merge battery, and will message WINDOW-style before
`make test`/mech/san — so a `[B8]` window is a request, not a given.
Awaiting Frank on the queue order and the roster entry.

## 2026-08-25 (EDT, ~13:4x), second session (part 3) — [B8] code landed: pin 692c2e8, the `_in` frame-buffer testees, 31 checks; the window requested

Frank: "proceed with your order"; budget note — finish the current set
([B8]) then pause with journal + wake (76 % of the weekly token budget
used; about a day's work for two devs left). Lane b8repin (worktree,
strong model) delivered lane/b8repin in three commits (733fae4, 995ec7f,
1c2ff01), merged as 08602ed.

FINDING THAT MOVED THE PREMISE (lane, smoke at --trials 1): at 692c2e8
`factored` compiles to a DFA artifact under BOTH `auto` and `nocaps`,
both forms (wave G's dead-capture elision) — pcrec-auto answers 170/170
with ZERO give-ups on bench/email; the five PCREC_ERR_FRAMES give-ups
(factored whole-subject s-058/059/061/063/064) remain only on the
VM-forced artifact. So the `pcrec-auto-in` entry both managers had in
mind is INERT here (a DFA artifact stamps frame size 0, the driver
passes NULL). RULED (me, pcrecdev1 concurring; Frank's word pending via
the inbox — pcrecdev1's "Frank confirms" was retracted as its own
recommendation): the `_in` machinery is generic (any config may carry
`buffer_frames`/`buffer_trail`, CAPACITIES never bytes, both or neither);
`pcrec-vm-in` is the roster entry measured on this sub-bench;
`pcrec-auto-in` stays DEFINED (the checks use it to prove the
DFA-artifact NULL path; it goes live on a sub-bench with VM-selected
patterns under auto, e.g. #4) but is NOT MEASURED on bench/email — an
entry measuring the same artifact as another is a trap for report
readers. Independent reproduction of wave G's bar (pcrec's specimen
check reads 12/0 on its side). The before/after on factored/short-search
is therefore DFA-vs-DFA, not wave-G-on-VM.

THE SIZING MEASUREMENT (lane, on the factored `\z` VM artifact, one
capacity held far above binding while the other is swept): s-058 needs
4005 frames / 20020 trail; s-059 10245 / 46100 (the maximum; 5 KB quoted
string); s-061 1504 / 5020; s-063 5122 / 23044; s-064 2053 / 18452 —
trail/frames ≈ 4.5 throughout. Smallest power-of-two pair clearing all
five: 16384 / 65536 (16384 / 32768 still loses s-059 on the trail).
Config: 32768 / 131072, one doubling above — 2.75 MiB per run, touched
once outside every timed loop. Recorded twice per record: as
`runtime_options` and as `buffer_frames`/`buffer_trail` metadata pairs
on every compile row whose artifact used them (absent = stamped defaults
ran). New pairs declared: resume_frames, trail_frames,
resume_frame_size, trail_frame_size (per-artifact; 0 on DFA).

CHECKS: 7 new PASS lines (check_frame_buffer): `_in` agrees with plain
(span AND captures); a tiny buffer (4/4) on a deep subject gives up
`giveup:-3:PCREC_ERR_FRAMES` BY NAME where the configured one matches
(sabotage proved once: the shim passing NULL made exactly the
"configured capacities MATCH" arm fail); a DFA artifact with buffers
requested takes none, no division by the stamped 0, answers identical;
abi reads 3; give-up bounds unchanged (-5/-2/-6). Old-vs-new driver
without options: subject lines identical on all 85 subjects, 3 modes.
make check on master: 2/53/0, 31/31, 20/20.

PCREC FINDING to carry (outbox O-3 at pause): the call-bearing factored
VM artifact stamps `RX_RESUME_FRAME_SIZE 24` where match_api.md §10.2
says 40 for a call-bearing artifact — a doc/measurement discrepancy on
pcrec's side (the adapter reads the stamp, so the bench is right either
way).

LANE MECHANICS: manager→lane messages arrived LATE — two steers
(config_extra naming; drop auto-in) were ACKed only after the lane had
declared itself complete and I had merged; I stopped its rework and
accepted its engine_mode slugs (`auto-in`, `vm-in`, registered in
record_schema.md §6.3) rather than spend budget on a rename. The lane
also reverted my plan.md STATE tag (told not to touch plan.md) — restored
in the merge commit. Lesson confirmed twice now: ask for an ACK of the
BRIEF's rulings at the start, and put the rulings that matter in the
brief, not in follow-ups.

NOW: window requested from pcrecdev1 (six cells, ~45 min, CPU 11; its
lanes must be idle — load is 2.7 with them up); a synthetic --trials 1
rehearsal of the exact run_window_b8.sh (pcrec-auto, pcrec-vm-in) into a
scratch store is running in the background.

## 2026-08-25 (EDT, ~14:5x), second session (part 4, PAUSE) — [B8] DONE: the re-pin sample measured and reported; two pcrec findings; the reporter's two gaps

THE WINDOW: pcrecdev1 opened it at 13:33 (load1 0.94, its three lanes
done, its battery held). run_window_b8.sh ran 13:34-14:10 (36 of 45
min): pcre2-interp, pcre2-jit, pcrec-auto, pcrec-nocaps, pcrec-vm,
pcrec-vm-in, every cell rc=0 on the first gate attempt. Three records
came back `inconclusive-load` (pcre2-interp, pcrec-auto, pcrec-nocaps):
the AFTER occupancy sample read 10.1 / 10.2 / 11.0 % on one core against
the 10 % limit — 1-s transients; pcrecdev1's audit of its side shows only
git commits and watchdog `ps` ticks inside the window. OD-B12 exactly;
pcrecdev1 suggests per-core busy AVERAGED over the cell or a load1/nproc
ratio. The rehearsal (synthetic, --trials 1) had caught one real setup
gap first: a fresh store has no machines.tsv and `run` refuses (rightly)
— seed it. WINDOW CLOSED 14:10; the battery started 14:11, so the three
cells are re-measured at the next boundary or next session.

THE BEFORE/AFTER (reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-
repin-692c2e8.{md,subject-grain.md,tsv}; set grain, median of 5,
ns/call): (1) factored/short-search COLLAPSED as I-1 predicted —
pcrec-auto 84,076 (8da6120) → 6,284 (692c2e8), nocaps 6,136, = orig's
6,125; pcre2-jit 15,364, so pcrec-auto is now 2.4× faster than the JIT
on factored where on orig it ties it. NOT an outlier: wave G confirmed
by an independent bench. (2) factored/match-compliance: pcrec-auto 100 %
(was excluded on five FRAMES give-ups) at 234,951 vs pcre2 1,833,524
(0.128×); pcrec-vm-in completes all 85 at 464,408; pcrec-vm still
excluded by its give-ups. (3) factored/throughput 1 MB: pcrec-auto
13.40 ms 100 % (was excluded); pcre2-jit absent (U1 reproduced 5/5).
(4) NEW: pcrec-vm-in BEATS pcrec-vm on every regime at the same pin —
orig/short-search 12,546 vs 28,997 (2.3×), orig/compliance 62,732 vs
80,228, factored/short-search 54,118 vs 69,538 — filed as outbox O-4
(reading: a per-call default-buffer setup cost the `_in` entry avoids;
~200 ns/call). (5) orig/compliance stays a regime artifact (VM forms
3-4× under the \z DFA form; [OS-4]). (6) orig otherwise unchanged
across pins within noise. O-3 answered by pcrecdev1: the 24-byte frame
is right — "call-bearing" meant LINKED-call-bearing, wave G splices the
acyclic calls; pcrec fixed its spec; the honest reporter column is
RX_VM_CALL_LINKED/_SPLICED.

REPORTER GAPS the sample exposed (→ [B9]; requirements OD-B14/B15): the
report marks NO record status, so the three inconclusive-load records
rank unmarked beside measured ones; and with two records of one
testee_id (pcre2 at two dates) it neither states nor lets the reader
choose pooled-vs-newest (the pcre2-jit orig/short-search median moved
6,28x → 6,124, so it is not simply the old record). Until [B9], read the
repin report with the index's status column beside it.

STATE AT PAUSE: [B8] completed and archived; master cfbfc7c+; store 11
records; make check 2/53/0, 31/31, 20/20; worktree removed, branch
lane/b8repin kept (its unmerged config_extra rework is 9cf19c8 in that
worktree's reflog only — gone with the worktree; the merged design is
engine_mode slugs `auto-in`/`vm-in`). Budget: Frank at ~76 % of the
weekly token budget at session start; this session used one strong
lane, one window, and the manager's own traffic. Next: [B10] (scratch
tier / quick / pcrec-local) ∥ [B9] (reporter: status, stamps incl.
LINKED/SPLICED, phases, regime-artifact bucket, OD-B11..B15), then
[B11] log-line search — Frank starts them.

## 2026-08-25 (EDT, ~15:5x), second session (part 5) — [B9] and [B10] DONE: reporter v2, the scratch tier, `quick`, `pcrec-local`; [B13] chartered

Frank: "proceed on b10/b9 and the re-measure when you can" (after the
interpreter conversation: [B13] chartered, not started; pcrecdev1's
reading of the repin report recorded as feedback_pcrecdev1_2026-08-25-
repin.md and folded into [B9]'s column list and [B13]'s prediction
list). Two lanes, disjoint by file ownership, both ACKed their briefs
first (the lesson applied; no late steers this time): b10loop (strong)
and b9report (sonnet). Merged in that order, no conflicts; master make
check 3/55/0, 50/50, 31/31; the repin report reproduces under reporter
v2. What landed is on the archived rows. Two rulings made en route: R2
amended — the newest MEASURED record wins per testee, a newer
non-measured record never supersedes it (a non-measured record is not
evidence against a measured one; pcre2 did not change between the two
dates) — without it the baseline vanished from the repin report; and
reduce.py's give-up spelling (`-3:PCREC_ERR_FRAMES`) adopted in the
report so quick and the reporter cannot disagree. Lane mechanics: b10loop
went idle twice mid-task (a nudge resumed it) and its first make check
failed 3 checks on its own registry-fallback regression (explicit
--machine-id refused) — diagnosed by the watchdog from the log before
the lane spoke, fixed by the lane, no check loosened. b9report found and
fixed a render bug of its own (a fully-excluded ranking group vanished
with its title). KB-1 filed (known_issues.md created). Waiting: the
16-min re-measure window after pcrecdev1's battery (~16:45-17:15).

## 2026-08-25 (EDT, ~18:4x), second session (part 6, PAUSE) — the three re-measured cells are `measured`; the repin sample is complete

pcrecdev1's battery finished 18:15 (green); WINDOW OPEN; load1 decayed
to 0.93 by 18:16; run_window_b8.sh with TESTEES="pcre2-interp pcrec-auto
pcrec-nocaps" ran 18:16-18:32: all three `measured` (nocaps: one BEFORE-
sample gate refusal, rc 3, passed on the script's second attempt — the
OD-B12 retry doing its job). WINDOW CLOSED 18:32, load1 1.11. store/ now
holds 14 records; reporter v2's newest-measured rule ranks the 18:xx
records and lists the 13:xx inconclusive-load ones as superseded. The
repin report re-rendered (all three files): every 692c2e8 cell ranked;
the headline numbers of part 4 stand (the auto/nocaps medians agree
with their inconclusive-load runs within spread — the gate had refused
records that were, in the event, fine, which is the OD-B12 argument for
an averaged-occupancy verdict). Session pauses here: [B8]-[B10] done,
[B13] chartered, next in the queue [B11] log-line search — Frank starts
it.

## 2026-08-25 (EDT, ~19:3x), second session (part 7) — pcrecdev1's second reading (reporter v2): two of four rows chartable as printed; [B14] opened

Frank asked for the closing feedback on the FINAL repin report. Recorded
as feedback_pcrecdev1_2026-08-25-repin-v2.md. [OPT-1] (vm-in vs vm) and
the VM compile-cost multiple are chartable from the report as printed;
the 1 MB throughput loss and the DFA `\z` gap wait on pcrec's I-3 stamps
plus two reporter facts (per-subject rows for tiny sets; matching-subject
count per compliance cell). All eight prediction verdicts stand after
the re-measure (measured vs refused values within noise). Column defects
and shortenings → [B14] (not started; sonnet-sized). Two interpreter
rule facts → [B13]: the cross-pin VM speedup (×1.19/×1.26, unattributed)
is exactly the "unpredicted Δ, flag as loudly as a regression" case;
STEPS-vs-WORK on the same subject = "a different budget binds on a
different spelling". pcrec's [DD-13] stamps land tonight (abi 4); I-5
expected — the next re-pin. Paused again.

## 2026-08-25 (EDT, ~21:4x), second session (part 8, CLOSE) — [B14] + [B15] merged; the session closes

Frank: "proceed to implement on feedback, 1-3 subagents as profitable"
then "close session when idle". Two sonnet lanes, both ACKed first,
disjoint by ownership: b15floor (bench/email `floor.rx` = `@` with
sidecar role floor; oracle-derived expectations 330 → 495; schema v1.3
`patterns[].role` + X30; KB-1 fixed; 56 harness checks) merged first;
b14report (reporter v3: the ten follow-ups from pcrecdev1's second
reading; 41 tests; both report sets re-rendered, reproduce) merged on
top. Master make check 3/56/0, 56/56, 41/41. One steer (R3: matches
from the record, not the sidecar) arrived after the lane had built it
the other way — accepted as delivered and filed as KB-2 rather than
spend a round; the record carries what is needed (`match_outcome` +
`observed`). Scratch, direction only: on the floor pattern pcre2-jit is
slower per call than pcrec-auto (≈45 vs 19 ns/call) — pcre2's per-call
setup, not the harness, is the floor; a pinned floor record is the next
window's business (the floor column will then fill on every short-
search row). Not done this session: [B11] log-line search (Frank
starts it); [B13] sitting; the re-pin when pcrec's I-5 (abi 4, DFA
stamps) arrives; a pinned run of bench/email including the floor
pattern. Session total, second session: [B8], [B9], [B10], [B14], [B15]
done; [B13] chartered; 16 commits of docs/records/reports; two windows
with pcrecdev1 (36 + 16 min); O-1..O-6 in the outbox; KB-1 fixed, KB-2
filed. Closes here.

## 2026-08-28 (EDT, ~09:1x), third session (part 1) — wake by the pcrec manager acting AS the bench (Frank's ruling); I-5..I-13 acked; [B16], [B17], [B11.1] opened and laned

pcrecdev2 is not running. Frank, in the pcrec session: "there is no
reason you couldn't slip over there and advance that cause as needed.
Do one repo or the other for focus … Be the bench though — use its
journal etc." So the pcrec manager runs THIS session by the bench's own
documents (skill, wake.md, plan, journal); the D78/BD5 file channel
keeps its shape (the bench writes outbox, pcrec writes inbox — the same
person on different days), BD2 holds (pcrec read-only from here).

WAKE: master at 6a12716 (the last write was pcrec's I-13). Nine inbox
items without an ack (I-5..I-13): five pcrec pins in two days (abi 4 →
8), the reporter-v4 reading with its prediction ledger (I-7/I-8/I-11),
the periodic-subject confound (I-10). All acked in 5faf9e5 into three
rows: [B16] RE-PIN to 35e1ab1 (abi 8) as ONE adapter change (stamps
RX_DFA_SCAN/PREFILTER/TABLE, RX_FAST_*, rx_info.scan/.prefilter; the
reporter's I-7 §3/§5 rules; then the window against the 692c2e8
records, testing P1-P7, P2's exact figure, P8'-P11'); [B17] NON-PERIODIC
throughput subjects (two 1 MB prose subjects, seeded; a `periodic`
manifest column; email-specimen 0.1 → 0.2 — a subject change bumps the
version, requirements §5; measured in a second window so the cross-pin
ledger stays at 0.1); [B11.1] SUB-BENCH #2 LOG-LINE SEARCH — the number
pcrec's [OPT-5] (required-byte precheck) is built or not on: 8-10
ops-style patterns each with its required literal documented and at
least one with NONE (the control a precheck cannot help), ~100-150
non-periodic generated log chunks of 256 B–4 KB with low match rates,
a 16 KB→1 MB size sweep for the give-up outcome, a floor pattern, the
libpcre2 oracle chain; patterns authored from the GOAL — the lane is
blinded to pcrec's tests/ and src/.

LANES (09:1x): b16repin (opus; testees/pcrec + report.py), b17prose
(sonnet; bench/email), b11loglines (opus; bench/loglines + generic
selfcheck coverage). Disjoint by directory; shared-file touches
(subbench.py, selfcheck.py, Makefile) declared minimal. No numbers
from lanes — the windows are mine, after merges: window A = [B16]'s
six cells + floor at 0.1; window B = throughput at 0.2; window C =
loglines cells at abi 8. Box idle at wake (load 0.02); libpcre2 10.46.
Stall watchdog cron b0dc29ec, 10 min.

## 2026-08-28 (EDT, ~09:5x), third session (part 2) — [B17] MERGED: email-specimen@0.2, the two prose subjects, the `periodic` column

Lane b17prose (sonnet) delivered in ~45 min, one commit (6dc9236),
merged as a78d1cc's parent. What landed: `t-d-prose-sparse-addrs`
(1 MB of seeded prose, vocabulary of 210 varied-length words, a valid
dot-atom address every 200-400 words — 496 addresses, checked three
ways: the generator's count, `bytes.count(b'@')`, the oracle's find-all
count) and `t-e-prose-no-at` (the same generator with insertion off,
zero `@`); `bench/email/periodic.py` (I-10's definition: the smallest
p ≤ 4096 with s[i]==s[i+p], else `no`), shared by both generators; a
`periodic` column on BOTH manifests — the three originals re-derive to
I-10's own 26 / 55 / 1 mechanically, the prose subjects `no`; of the 85
short subjects only s-060 (10 KB local part) is periodic (1). The
loader accepts 4- or 5-column manifests (a manifest that predates the
column still loads; any other width is refused). Version 0.1 → 0.2 with
the reason in the sidecar (requirements §5); expectations 501 rows,
`--check` clean; make check 3/56/0, 56/56, 42/42 — unchanged counts, no
new check (the manifest-reproduction and expectation checks cover the
new subjects by construction).

The lane's own honesty item: I-10's literal "every 200-400 words" gives
low hundreds of addresses per MB, not the "few thousand" my brief
guessed; it kept I-10's figure and reported the real count. Right call
— sparse is the point (t-a has 40,330 matches; t-d's 496 makes it the
matching-bearing subject whose cost is scan, not per-match restart).

Stale-prose sweep (the lane's grep): report.py's `tiny_set … <= 3`
per-subject-table threshold was "every throughput cell" and would
silently drop the sub-table at 0.2 — handed to b16repin (its file);
harness_contract §2's "three 1 MB" fixed in a78d1cc (the origin's
three, plus two since [B17]); requirements §5's mention describes the
ORIGIN and stays. Lane mechanics: the lane went idle twice with a
background make check in flight (a Monitor armed, no report) — two
pings; its ACK came as plain text, not a message. Brief line for next
time: "the ACK and the report are SendMessage calls."

## 2026-08-28 (EDT, ~10:0x), third session (part 3) — [B11.1] MERGED: bench/loglines@0.1; the set's finding BEFORE any number

Lane b11loglines (opus, blinded to pcrec's tests/ and src/) delivered
in ~50 min (b142c34; merged). The sub-bench: ten member patterns
authored from the goal — iso-ts, ipv4, ipv6, kv-quoted, level-context,
http-5xx, uuid, stack-frame, hex32-id, bignum — plus the floor `:`;
112 generated log chunks (26/28/29/29 across the 256-511 / 512-1023 /
1024-2047 / 2048-4096 B bands, every one `periodic: no`, mixed
syslog / nginx / JSON-lines / Java stack / k8s formats, a seeded
generator in logtext.py), match rates 6-9 % per pattern (the 95 % path
is FAILING text, and the background is near-misses, not first-byte
rejects); a size sweep 16 KB / 64 KB / 256 KB / 1 MB in THREE flavours
— fail, hit, and single-source BSD syslog; regimes search_short (max
4096 B) + throughput, no match regime (a subset — the loader accepts
it); expectations 1,364 rows from the libpcre2 oracle; make check
62 checks (was 50), the generic gates now ENUMERATE bench/*/ (never by
name); the oracle chain factored into pcrecbench/expectations.py;
periodic.py moved to pcrecbench/ (the lane hit the same shared change
[B17] made, took master's, deleted its own — they agreed exactly).
Cell-time estimate ≈ 9 min pcrec / 8 min pcre2 at --trials 5.

THE FINDING, from `pattern_facts.tsv` (pcre2_pattern_info's FIRST and
REQUIRED code unit per pattern, presence counts over the subjects,
re-derived by make check): on MIXED log text every required code unit
in the set is a STRUCTURAL byte — `:` (iso-ts, ipv6), `.` (ipv4), `-`
(uuid), `5` (http-5xx), `"` (kv-quoted), `)` (stack-frame) — and
`:` `.` `-` `5` occur in 112/112 search subjects; only `"` (absent in
35/112) and `)` (absent in 16/112) leave any room for a required-byte
dismissal to fire; level-context, hex32-id and bignum have NO required
unit at all (the control). The first cut of the sweep had every
required byte present in all eight large subjects — not one was the
analogue of t-b-no-at — so the lane added the syslog flavour (no `"`,
no `)`), on which kv-quoted and stack-frame are dismissible without a
scan. What this says to pcrec's [OPT-5] before a single timing: the
required-byte precheck's benefit on realistic log search is bounded by
those presence counts — near zero on mixed text, real only for
quote/paren-bearing shapes on single-source streams — and the
window's numbers should be read against the counts, not against
"failing text". Outbox item drafted at window time (O-7).

## 2026-08-28 (EDT, ~10:2x), third session (part 4) — [B16] MERGED: pin 35e1ab1 (abi 8), reporter v5; four pcrec-side findings from the lane

Lane b16repin (opus) delivered in ~75 min, nine commits incl. a merge
of master; merged. The adapter: `configs.toml` pin 35e1ab1 (PIN.tsv:
35e1ab168bf3…, archived 13:07:56Z); the shim reads RX_DFA_SCAN /
RX_DFA_PREFILTER (abi 4+, VM hybrids at 6+), RX_FAST_FRAMES / _TRAIL
(abi 5+, VM-only), RX_DFA_TABLE (abi 7+) and rx_info.scan / .prefilter
(abi 6+) — the fields are read but NOT recorded: they are the CONTROL
on the macros (`_check_agreement`: engine string vs int; prefilter
never NULL; DFA_SCAN present iff scan non-NULL and equal; prefilter ==
the DFA's vocabulary where a DFA scan exists, else the VM's) — and an
abi FLOOR (PB_SHIM_MIN_ABI 6, one definition, refused by name with
both numbers on a sabotaged `.abi = 5` fixture, the unmodified artifact
loading in the same run as the control). Every stamp's VALUE proven on
a real artifact of each kind (pure DFA, VM hybrid, forced VM,
provably-empty); `-fno-premul-table` moves dfa_table to `indexed` as
the control for the one value the corpus reaches. make check 3/56/0,
75/75, check-report OK (49 reporter tests). Reporter v4 → v5, [B16]
R1-R8 (pcrecbench/CLAUDE.md): the DFA mechanism legend per (testee,
pattern, form); the fast tier; `inferred (unstamped pin)`; a give-up
code that names the other engine turns a cross-pin ratio into
`selection changed (vm → dfa)`; the gcc-ms band as a WITNESS that
abstains between bands; "max is trial 1"; the >90 % `dominated` flag;
the version bump. reports/ re-rendered, byte-identical after the merge.

FOUR FINDINGS FOR pcrec (→ outbox O-7 with the window's numbers):
1. I-7 §3 was half right and the cause is OURS. The engine WAS stamped
   at 8da6120 (rx_info.engine exists since abi 2): the record says
   `engine: vm` for factored and `dfa` for orig at that pin. The legend
   printed `engine=dfa` for the whole testee because [B14] R8 sampled
   the FIRST compile row (orig sorts first) — another pattern's value
   under this pattern's name, not an inference from the config. Fixed
   (R3); the ×13.45 now reads `selection changed (vm → dfa)`.
2. P6 (I-7) is wrong on the whole-subject shape: `(?:P)\z` artifacts
   stamp RX_DFA_SCAN "unanchored" with RX_DFA_PREFILTER
   "byte-class-bounded" (floor: memchr → memchr-bounded), not
   `attempt` — `attempt` is the `^`/`\A` shape. Verified on all three
   email patterns. (I-5 had said exactly this; I-7's P6 contradicted
   it.) The plain-vs-`\z` skip-loop asymmetry [B8] read out of emitted
   C is now a stamp in the record.
3. I-11's compile-size prediction ("DFA +~5 KB, VM +1-2 KB")
   understates by ~6×: measured 692c2e8 → 35e1ab1, compile-only, same
   basename: DFA artifacts +29,807 B plain / +34,861 B `\z` on both
   email patterns (+66-69 %); VM +5,074 B flat. Pin by pin on
   orig/auto: abi 4→6 +171 B; abi 7 ([OPT-3] premul) +27,495 B; abi 8
   ([ENG-FORM]) +2,141 B — and on the tiny floor pattern abi 7 costs
   +846 B while abi 8 costs +2,139 B: [OPT-3] scales with the machine,
   [ENG-FORM] is ~2.14 KB FLAT per DFA artifact (the accessor block).
   Every value pcrec said we read is unchanged; the artifact grew.
4. My brief cited `pcrec/docs/guide/tuning.md`; pcrec has no docs/guide
   — tuning.md is docs/spec/tuning.md (§2.12, §2.13, §3 all present).
Bench-side correction: testees/pcrec/CLAUDE.md claimed the emitted
`.c` does not embed the output path — false of the BASENAME (`#include
"<basename>.h"`): `-o a.c` vs `-o aaaaaaaaaa.c` differ by 9 bytes; a
trap for size tables, corrected in place.

STATE: master = the [B16] merge; make check running on it (the lane's
merged-tree run was green); lanes 0; cron torn down. NEXT: window A/B
(email@0.2, six cells + floor, ~50 min), then window C (loglines).

## 2026-08-28 (EDT, ~11:0x), third session (part 5) — WINDOW A/B DONE: email-specimen@0.2 at pcrec 35e1ab1 (abi 8), six cells `measured`; the prediction ledger; I-10's confound measured

THE WINDOW: 10:16-10:59 (43 min), box idle, one cell at a time on core
11, --trials 5, into store/ (20 → 21 records). Every record `measured`.
Two mechanics: (1) the first launch (a harness background task) was
stopped seconds in and relaunched under `setsid` (the 10-min task
timeout would have cut a 50-min run; nothing was written — a cell
writes only at its end); (2) the pcre2-interp cell was refused three
times by the quiet gate (busiest core 47-100 %): the b16repin lane
was STILL ALIVE after delivery, had recreated its removed worktree and
was re-running `pcrecbench.tests.test_report` — stopped by TaskStop,
all three lanes stopped, worktrees removed; the cell re-ran at 10:50
(rc 0 first attempt). Two later cells needed a second gate attempt
(the 1-s transient right after the previous cell closes — OD-B12's
shape; a `sleep 15` before the first sample would remove it). The
lane's post-delivery diff (the `tiny_set` fix I asked for) is saved
in the scratchpad to apply after window C. Report:
reports/2026-08-28-email-specimen-0.2-budu-ryzen1600-repin-35e1ab1.{md,
subject-grain.md,tsv} (reporter v5; the `dominated` flag fires on
pcre2's floor/throughput rows — t-a is 90-97 % of those sets).

THE LEDGER (predictions from inbox I-7 / I-8 / I-11, vs the 692c2e8
records; same box, byte-identical subjects; set-grain ns/call unless
said; per-subject rows for the throughput set because the set grew
from 3 to 5 subjects at 0.2):
- P1 ✓ pcrec-vm short-search per-subject mean: orig 376.6 → 162.6 ns
  (predicted 160-175; vm-in 164.1 — CONVERGED); factored 903.1 → 699.4
  (predicted 700-740; vm-in 703.3).
- P2 ✓ pcrec-vm orig match-compliance 80.2 → 62.8 µs (predicted 63-70;
  vm-in 62.1 — the O-4 gap is closed on every regime).
- P3 ✓ pcrec-vm factored compliance still excluded: the same five
  PCREC_ERR_FRAMES subjects (s-058, s-059, s-061, s-063, +1; smallest
  2,008 B); vm-in completes all 85 at 456 µs (was 464).
- P5 ✗ artifact bytes: DFA +29.8-34.9 KB, VM +5.1 KB (journal part 4;
  I-11 said +5 KB / +1-2 KB). gcc time: DFA 124-140 → 127-146 ms
  (+~4 %, inside the ±5 %); VM 400-540 → 416-549 ms (inside).
- P6 ✗ the whole-subject artifacts stamp `unanchored` +
  `byte-class-bounded` (floor: `memchr-bounded`), not `attempt` — I-5
  had it right, I-7 contradicted it (part 4).
- P7 ✓/✗ the pinned floor (per-subject mean, short-search): pcrec-auto
  17.7 ns (predicted ≈19 ✓), pcre2-jit 44.2 (≈45 ✓), pcre2-interp
  96.9, pcrec-vm 32.6 / vm-in 32.9 — BETTER than the predicted 45-50
  (the abi-5 16 B-subject figure; the fast tier's floor is ~33 ns).
- P8' ✓ orig throughput on the ORIGINAL three: pcrec-auto 3.585 /
  1.895 / 1.879 ms (I-11's lane: 3.516 / 1.799 / 1.803 — within 2-5 %,
  the bench's own protocol), set 7.36 ms vs 12.77 at 692c2e8 = 1.735×
  (predicted 1.79×); pcre2-jit 3.685 / 2.564 / 2.819 = 9.07 ms, so
  pcrec-auto is 0.81× of JIT — ranks ABOVE pcre2-jit on the throughput
  regime for the first time, as predicted. factored: identical to orig
  to three digits (the DFA is the same machine).
- P9' ✓ DFA compliance 234 → 133.8 µs orig / 130.2 factored (~1.75×).
- P10' ✗ (good direction) short-search DFA rows moved 1.73×, not
  ≤10 %: pcrec-auto orig 6,125 → 3,533 ns/set (45.9 ns per subject
  against a 17.7 ns floor) — the scan portion of even a 30 B subject
  took the premultiplied table's gain; pcrec-auto is now 1.73× faster
  than pcre2-jit on short search (was parity), 3.5× faster than its
  own VM.
- P11 ✓ VM rows untouched on throughput (15.7-16.0 ms on every failing
  1 MB subject, ~15 ns/byte, 8.5× the DFA); the [OPT-1] gains above
  are the VM's only movement.

I-10's CONFOUND, MEASURED (the new prose subjects; orig; ns/byte):
- FAILING text: periodic t-b-no-at pcrec-auto 1.807, pcre2-jit 2.445
  (pcrec 0.739× of JIT); NON-PERIODIC t-e-prose-no-at pcrec-auto
  2.962, pcre2-jit 3.012 (pcrec 0.984× — PARITY). The periodic subject
  flattered pcrec's DFA loop by 1.64× and the JIT by 1.23×: the
  branch-prediction reading in I-10 is right and it is worth more to
  pcrec than to the JIT. Any [OPT-3] STEP 3 candidate must be measured
  on t-e, not t-b — and a run-speculation idea would have looked 1.6×
  better than the field on the old set.
- MATCHING prose (t-d, 496 addresses in 1 MB): pcrec-auto 2.994 ns/byte
  (= its failing-prose cost: bytes, not matches), pcre2-jit 5.690 —
  pcrec 0.526× of JIT; pcre2-interp 89.5 ns/byte (93.9 ms: the
  interpreter's backtracking on near-miss tokens — every word before
  a `.`), 30× the DFA. The JIT pays 2.8 ms MORE on prose with 496
  addresses than on prose without: ~5.6 µs per match, or near-miss
  backtracking on every `word.` token — an upstream_findings row.
- pcre2-interp dismisses t-e in 18.1 µs (no `@`; the required-code-unit
  check, same as t-b) — 172× the DFA's scan. Interp's set-grain
  throughput ratio is DOMINATED by t-a (96.7 %) and the report says so.

Everything I-11 claimed for the DFA holds on the bench's own protocol;
the compile-size prediction and P6 did not, and the periodic subjects
overstated the DFA's lead over the JIT on failing text by 1.6×.

## 2026-08-28 (EDT, ~12:0x), third session (part 6) — WINDOW C DONE: bench/loglines@0.1 at pcrec 35e1ab1, six cells `measured`; the [OPT-5] number; the NEXT OUTLIER is not [OPT-5]

THE WINDOW: 11:00-11:50 (50 min; cells 8.5 / 8.7 / 7.5 / 7.5 / 8.6 /
8.3 min — the lane's ≈9 min estimate held), --trials 5, core 11, six
records into store/ (21 → 27), all `measured`; every cell after the
first needed a second gate attempt (the post-cell transient; pcrec-auto
needed three, busiest core 10-15 % — the editor's `gh pr list` poll).
Reports: reports/2026-08-28-loglines-0.1-budu-ryzen1600-first-sample-
35e1ab1.{md,subject-grain.md,tsv} (reporter v5). Floors (per-subject
mean, search): pcrec-auto 18.2 ns, pcrec-vm 41.0, pcre2-jit 45.9,
pcre2-interp 100.7 — the DFA's per-call floor is 2.5× under the JIT's.

THE [OPT-5] NUMBER (the required-byte precheck; read against
pattern_facts.tsv's presence counts, journal part 3):
- 1 MB, required byte ABSENT and not the first byte (kv-quoted `"` /
  stack-frame `)` on t-1024k-syslog): pcre2-interp dismisses in 19.2 /
  17.9 µs; pcrec-auto scans 3.25 / 3.61 ms — 169× / 202×. pcre2-jit:
  2.11 ms / 68 µs (the JIT does not dismiss either; its stack-frame
  speed is a different mechanism, below).
- THE CONTROL THAT SAYS THE MECHANISM ALREADY HALF-EXISTS: http-5xx
  (required byte `"` IS the first byte, prefilter `memchr-bounded`) on
  the same syslog subject: pcrec-auto 17.6 µs = pcre2-interp's 17.8 —
  the memchr first-byte skip over a subject without the byte IS the
  dismissal. [OPT-5] is the k>0 case of a skip pcrec has at k=0.
- The SEARCH BAND (112 subjects of 256 B-4 KB — the regime that
  matters): kv-quoted pcrec-auto 501 µs vs pcre2-jit 335 (1.50× behind;
  `"` absent in 35/112 subjects, so a precheck saves at most ~35/112 of
  the scan ≈ 150 µs → parity, not a win); stack-frame pcrec-auto 558 µs
  vs JIT 17.6 (31.7× behind; `)` absent in 16/112 — a precheck cannot
  close 1/30th of that). Verdict for pcrec: a required-byte precheck
  is worth building only as the general "byte at offset k" skip below,
  never as its own mechanism (D77: the narrow number is ~parity).

THE OUTLIER THE SET ACTUALLY FOUND — pcrec-auto vs pcre2-jit, search
band, set ns/call over 112 subjects:
  stack-frame 558,756 vs 17,574 (31.8× BEHIND) · uuid 434,798 vs
  35,766 (12.2× behind) · iso-ts 213,267 vs 21,013 (10.1× behind) ·
  kv-quoted 1.50× behind · bignum 423,660 vs 394,927 (1.07× behind) ·
  hex32-id 1.14× AHEAD · ipv4 3.56× ahead · ipv6 4.39× ahead ·
  http-5xx 7,013 vs 104,980 (15.0× ahead; the JIT is even 1.8× slower
  than its own interpreter on this one — upstream row U4).
The JIT's 17-36 µs sets are 0.08-0.15 ns/byte over ~230 KB — SIMD
scanning speed. What the three losing patterns share and the parity
ones lack: a FIXED-LENGTH PREFIX WITH A SELECTIVE BYTE AT A KNOWN
OFFSET — `\d{4}-\d{2}-` (`-` at offsets 4 and 7), `[0-9a-f]{8}-…-`
(`-` at 8 and 13), `\bat ` (`a`,`t`,` ` at 0-2); hex32-id and bignum
are all-class prefixes with no selective position and sit at parity.
PCRE2's JIT scans the fixed-length prefix for its most selective
position pair with a SIMD char-pair search (its "fast forward first
N characters"); pcrec's DFA skip looks only at offset 0 — and at
offset 0 these patterns start with a digit/hex/letter, which is in
every line, so the skip never skips and the transition loop runs on
every byte (2.4 ns/byte on stack-frame). Same story at 1 MB: iso-ts
JIT 0.21 ms vs pcrec 1.94 (9×), uuid 0.48 vs 3.36 (7×), stack-frame
0.09 vs 3.90 (42×); ipv4 the other way (pcrec 1.89 vs JIT 6.05).
THE GENERAL MECHANISM (one, not three — memory `pcrec-general-
mechanisms-not-special-cases`): candidate-start derivation from ANY
fixed offset k inside the pattern's fixed-length prefix, choosing the
(k, byte-set) with the lowest expected frequency — the first-byte skip
is k=0, the required-byte precheck is "absent at every k → no match",
the JIT's pair scan is two k's at once; the frequency prior is D83's
exemplar findings file, with a static table as the fallback. Sent to
pcrec as the outbox's first outlier at O-7.

A pcrec FINDING (compile, not timing): `level-context` under `auto`
DID NOT COMPILE — "pattern too complex for the DFA engine (>32000
states; try --engine=vm)" — and auto did NOT fall back to the VM,
which compiles and runs the same pattern (1.55 ms/set, 13.4× behind
the JIT's 115 µs; JIT 0.71 ms at 1 MB vs interp 1.17). `\b(?:ERROR|
FATAL|CRIT)\b.{0,200}?\b(?:timeout|timed out|refused|denied|
unreachable)\b`: the bounded lazy repeat before a word-boundary
alternation is the K23/K32 band. Two things for pcrec: the SELECTOR's
contract when the DFA build overflows under auto (fall back, or
predict), and the state count itself. Bench-side gap: the reporter
shows `did-not-compile=1` only in the compile-cost table; the ranking
must list the cell as `not ranked: <testee> — did-not-compile
(<diagnostic>)` (→ [B12] item).

## 2026-08-28 (EDT, ~12:3x), third session (part 7, CLOSE) — R9 (reporter v6) applied; every report re-rendered; the store commits; the session closes

The b16repin lane's post-delivery diff was the `tiny_set` fix I had
asked for: the per-subject sub-table keyed on the REGIME
(large-subject-throughput always; a `dominated` cell always; a ≤ 3 set
still), with its own test. Applied by hand, `REPORTER_VERSION` v5 → v6,
[B16] R9 in report.py's docstring and pcrecbench/CLAUDE.md, the
version-pinning test moved to v6 (it caught the bump under make
check: 49/1, then 50/0). All twelve committed report files re-rendered
at v6 with the query in their own headers — the two `-repin-692c2e8`
queries gained `--version 0.1` now that 0.2 records share the store
(the same records; reports/CLAUDE.md says so); the 0.2 and loglines
set-grain reports gained the throughput per-subject sub-tables
(5 and 12 subjects) that R9 exists for. make check: 3/56/0, 75/75,
50/50. Store: 27 records (12 new today, committed with this entry).

Mechanics worth one line each: the harness's background task killed
two long runs (a make check twice; the first window launch) — every
long run today that finished ran under `setsid`; `test_report` alone
is > 2 min and block-buffers (`python3 -u`, gnutimeout 540); my R9
docstring insertion first landed past the closing quotes (a syntax
error that rendered twelve EMPTY reports before I caught it — re-render
and count `reporter: v6` headers, never trust the exit code of `>`).

STATE AT CLOSE: master = this commit; no lanes, no worktrees, no cron,
no monitors; box idle. wake.md rewritten. The deliverable to pcrec is
outbox O-7 (four asks). Next bench session: pcrec's answers, [B12]'s
two quick items, then [B11.2] or [B11.4] as ruled.

## 2026-08-29 (EDT, ~14:2x), fourth session (part 1) — wake; I-14..I-17 acked; [B18] and [B11.4] opened; three lanes

pcrecdev2 proper again (the third session was the pcrec manager acting
as the bench). Wake: wake.md, the inbox (four NEW items: I-14 Frank's
rulings on O-7 — the offset-k skip is pcrec [OPT-K], auto's overflow is
[SEL-1], bounded-repeat recommended next; I-15 pin 8ab6152 abi 9; I-16
pin 808740c abi 10 [ENG-ABS]; I-17 pin 36d5963 abi 11 [ART-SIZE] with
ONE consolidated worklist (a)-(e) superseding the earlier asks), the
journal tail, plan state. pcrecdev1 is up: nothing heavy on its side,
the box is ours for the window, coordination live, durable answers as
I-18 to our O-8. Box idle (load 0.31), tree clean at 88993b6.

Acked all four in the inbox and opened two rows (2db15bc): [B18] the
re-pin to 36d5963 — the adapter reads the abi 9-11 stamps by value
(`_DFA_PREFILTER_OFFSETS`, `RX_DFA_MATCH`/`match_form`, `_UNROLL_K`/
`_WHY`, `_MAX_EMIT_*`, the three new deny flags as controls, the map
checked against `--list-axes`), then the window re-measuring
email-specimen@0.2 and loglines@0.1 with pcrec's predictions copied
into the row as the ledger; (b) Frank's fallback-vs-JIT row on
`level-context`; (d) the long-subject failing-`_match` probe at the
SCRATCH tier (email's throughput regime is search-only, and adding
`match` to it would bump the version under the ledger's feet — a set
change only as a ruled item). [B11.4] bounded-repeat is ruled NEXT
(I-14 iv, I-15 c, I-17 c, "advance these bench requests"): three
numbers — the compile/size axis under nested bounded repeats (the
input to pcrec's size term), the K23/K32 match axis (the `level-
context` shape, `[a-z]{0,30000}`-class counts), and the refusal/give-up
as a first-class outcome with the first count at which it fires.

Three lanes, disjoint, in worktrees: b18repin (strong model) on the
adapter; b12close (sonnet) on R10 (the did-not-compile ranking line,
reporter v7), a committed `scripts/run_window.sh` with the `sleep 15`
gate fix, and the `test_report` runtime; b114bounded (strong model, a
BLINDED author denied ~/pcrec beyond docs/spec/ and this repo's
testees/, store/, reports/) on `bench/bounded@0.1`. Watchdog cron every
10 min. The window opens after b18repin merges; lanes get STOPPED
before it (last session's lesson).

## 2026-08-29 (EDT, ~16:4x), fourth session (part 2) — [B18] (e) merged; THE WINDOW at 36d5963: 12 cells, two HOLD breaches, the two-manager gate residue, three re-runs

Lane b18repin delivered in ~40 min and was merged as a541cbf: the shim
reads the abi 9-11 stamps by value (`_DFA_PREFILTER_OFFSETS`,
`RX_DFA_MATCH` + `rx_info.match_form` — the floor rises 6 → 10 because a
FIELD is read, the macros never move it — `_UNROLL_K`/`_WHY`, both
`_MAX_EMIT_*` caps), a `STAMP_SCOPE` table that makes a missing
unconditional stamp an AdapterError rather than a blank, `list_axes.tsv`
archived under a D35 header and diffed against the pin on every check,
four deny-flag controls (`-fno-offset-skip`, `-fno-anchored-dfa`,
`-fno-size-term`, `-fno-premul-table`) each reaching the other value,
thirteen LEDGER_STAMP_CASES on the bench's own patterns at pcrec's
predicted values (uuid `0,8*,13`, iso-ts `0,4*`, stack-frame `0,1*`, the
six declined loglines rows and both email patterns `none`, every DFA
artifact `unwrapped`, every VM artifact K=8/`default`, and the [SEL-1]
fallback: `level-context` under auto is a VM artifact stamped
`RX_ENGINE_WHY: dfa overflowed: >32000 states at pattern offset 0`).
make check 3/56/0 · 100/100 · 51. Four findings for O-8 (journal part 3
carries them with the numbers): `RX_MAX_EMIT_CODE_BYTES` is VM-only, not
"every artifact"; registry gaps (empty `stamp_value` on the size-term
rows, `table` lacks `none`/`mixed`, registry.md §6's 45/18 vs live
47/19); the DFA artifacts grew +5-20 KB and ALL of it is abi 10's third
machine (abi 9 and 11 exactly as predicted); the fallback's reason is
prose, not a stamp. Part (d): `quick` cannot address the throughput
subjects in the match regime (`Subbench.subjects_for()` maps `match` to
the short set); a regime addition is a version bump — deferred.

THE WINDOW. Lanes paused (b12close WIP-committed and idled on request;
b114bounded delivered, then stopped by TaskStop); pcrecdev1 told WINDOW
OPEN at 14:44. Launched under setsid at 14:45 (150-s lead): cell 1
(email × pcre2-interp) ran 14:48-14:57 — and at 14:56:30 pcrecdev1's
[OPT-4] lane started a `tests/harness/run.sh` section (load1 1.6 →
9.4) despite the HOLD; cell 2's gate refused twice, I killed my own
launcher by PID before the cascade (each refused cell costs a minute
and the next gate meets the same load), pcrecdev1 killed the section.
Relaunched 14:58 — and at 14:59 the same lane started
`tests/codegen/run_size_term.sh` under its watchdog (SECOND breach);
paused again, pcrecdev1 stopped the lane outright (TaskStop) and later
parked all three of its lanes and went idle. Relaunched 15:02; the
gate then refused on the RESIDUE: "busiest non-target core 11.11 %
busy (limit 10.00 %)" with load1 1.4 — the two claude processes
themselves (~9.5 % + ~6.5 % CPU while streaming); last session's
windows ran with ONE manager on the box and the per-core limit was
derived for that. Both sessions went silent; I widened the script's
gate budget from 3×20 s to 12×30 s and relaunched at 15:05. From then
every cell passed on attempt 2-3 (the first refusal after each cell is
the known 1-s post-cell transient — `sleep 15` does not cover it) and
loglines × pcre2-interp passed first time. Email 15:06-15:43 (five
cells), loglines 15:43-16:37 (six). 12 records, index 38.

THREE `inconclusive-load` RECORDS, read from their own environment:
email × pcre2-interp — genuinely loaded at its tail (after: load1 11.4,
a core 41 % busy — the 14:56 breach); email × pcrec-vm and loglines ×
pcrec-nocaps — load1 1.18 / 1.06 but the single 1-s post-cell occupancy
sample read 11.11 % / 13.0 %: OD-B12's false positive (the post-cell
transient has the same shape as a busy box; average it). Re-ran all
three in a second window (≈ 25 min) rather than argue with the status.

LESSONS (for wake.md and BD-n): a HOLD relayed to a lane is not a HOLD
until the lane's processes are gone — verify by cwd before OPEN, and
after every cell if the peer has lanes at all; the quiet gate's
per-core limit does not survive two streaming claude processes — both
managers must be IDLE for the window, not merely "not heavy"; the
script's gate budget is 12×30 s now (commit it in scripts/run_window.sh);
never grep the process table with a pattern that matches your own
command line (exit 144, twice); the launcher lives under setsid and a
kill-by-PID of one's own launcher is the right move the moment a gate
refuses for a reason that will not clear in 60 s.

## 2026-08-29 (EDT, ~18:0x), fourth session (part 3, CLOSE) — the ledger read; O-8; the probe; bench/bounded merged; make check 107/107

THE LEDGER (lane ledger36d extracted; reports/2026-08-29-*-repin-36d5963.*;
the numbers are in O-8 item by item). [OPT-K] on the loglines search
band moved MORE than pcrec predicted: uuid ×20.13 (predicted 4.45×/
9.58×) and now 1.65× AHEAD of the JIT; iso-ts ×10.30 (6.13×/5.75×) at
parity; stack-frame ×17.39 (10.18×/6.19×), 1.83× behind — "within 2×
of the JIT" holds on the band. At 1 MB uuid is ahead on all three
flavours, iso-ts 0.7-1.7×, stack-frame 3.0-6.5× BEHIND (scalar
memchr-at-k*+verify ≈ 0.4 ns/B vs the JIT's SIMD pair scan at 0.07-0.09).
Controls flat except http-5xx `slower ×1.03`. [ENG-ABS] on the email
match regime: matching 1.037 (pred 1.031), all-85 1.164 (1.161),
non-matching 1.539 (1.550) — three confirmed; the 35 short valid emails
0.566 (pred 0.482). pcrec-auto is now 7.3× faster than the JIT on the
match regime; search rows flat. [SEL-1]: level-context under auto = the
VM to four digits (13.4× behind the JIT on the band, 12.6-14.5× at
1 MB) — and its emit-c is 511/720 ms vs 1.6/3.4 ms for --engine=vm: the
DFA attempt to 32,000 states is paid before the fallback (313×). SIZE:
the compile table's `artifact bytes` is the .so (adapter.py:1063);
DFA .so +4.7-8.9 KB, VM +4.5-8.6 KB; gcc −4…+24 % (18/34 DFA pairs over
+5 %; VM within ±7.5 %). The pin-by-pin source attribution (b18repin):
abi 10's third machine is the whole DFA growth.

THE PROBE (lane b18probe, docs/dev/measurements/2026-08-29-engabs-
longsubject-match-probe.txt + its script; the directory is new, D35
rules in its CLAUDE.md): `(?:orig)\z` on the five 1 MB subjects + 64 KB
/ 4 KB prefixes, six arms, five interleaved trials, box not gated.
Unwrapped 12.3 ns FLAT at 4 KB / 64 KB / 1 MB where the machine dies at
byte 4; the -fno-anchored-dfa control 7.8 µs / 124 µs / 2.0 ms; 1.0×
where the machine is alive to the last byte. The driver's own floor
(the `@` pattern in the same form) is 10.3-10.6 ns — the number to hold
beside pcrec's 5.5 ns, not against it.

MERGES: b12-close (ef87b5d: R10 reporter v7; scripts/run_window.sh;
test_report 275 → 48 s via one cached real-store load) and b114-bounded
(485a230: bench/bounded@0.1, 24 patterns, 30 + 4 subjects, 1,536
expectations, oracle_limits.tsv, predictions on record; its author
recommends splitting the two axes into two sub-benches — a scope ruling
for the next session). The two 2026-08-28 report sets were re-rendered
at v7 WITH an `--until 2026-08-29T00:00:00Z` bound: the pcre2 testee_ids
carry no pin, so newest-measured-wins would otherwise have pulled
today's pcre2 records into the 35e1ab1 sample's files (reports/CLAUDE.md
says so). `make check` on master after the three merges: 3/56/0 ·
107/107 · check-report OK (51). O-8 committed (739ccdd) and pcrecdev1
told; BD6 records the two-manager window protocol. Gate budget 12×30 s
committed to scripts/run_window.sh.

STATE AT CLOSE: master clean at this commit; no lanes, no worktrees, no
cron, no monitors; the box is pcrecdev1's ([OPT-4] battery pending on
its side). Store 41 records (15 today). Next session: bench/bounded's
window (six cells ≈ 80 min, both managers idle), the [B12] OD-B12 fix,
pcrec's answers to O-8 as I-18, then [B11.2] wide alternations.

## 2026-08-30 (EDT, ~01:3x), fifth session (part 1) — the hold; bounded's first window; the note-length harness bug; five one-shot after-samples → BD7; Frank's gate-shape ruling → the v1.4 proposal

THE HOLD. Frank: "hold until pcrecdev1 give green light then proceed
with dev items". pcrecdev1's [OPT-4] merge battery (main ba69380, abi
12) ran 19:5x-22:49 EDT; a keepalive cron (Frank's ask) ticked `uptime`
at :11/:51. The battery found a corpus regression under [OPT-4]'s
default; Frank re-ruled it fallback-only (ruling B); battery 3 on
4d12a81 runs AFTER our CLOSED, I-18 with the abi-12 pin after its green.
Ruled during the hold, in wake.md: the window FIRST (bounded at 36d5963
as built — [OPT-4] is a bounded-repeat change, so this sample is its
BEFORE; no axis split before a first sample), the OD-B12 fix after.

THE WINDOW (bench/bounded@0.1, six testees, pin 36d5963, core 11).
"MECH DONE" at 22:4x was NOT a clear box: verify-by-cwd found pcrecdev1's
`make test-recursion-identity` (pid 318965, watchdog recidB, launched
22:35 before their HOLD) live at ~23 % of a core — BD6 exactly; not
touched; it exited 22:49:03 on its own; ALL CLEAR; re-verified; OPEN
22:49. Cell 1 (pcre2-interp) measured for 21 min and was REJECTED at
validation: `note` (schema free_text, maxLength 8192) carried one
"iters for (pattern, form, regime) = N: …" sentence per calibration —
72 on a 24-pattern set, ~12 KB (email: 9, loglines: 33 — it fit). A
harness bug (contract 4 step 5), every cell would have failed. Killed
my own launcher by PID (it was in a gate backoff, nothing measured),
told pcrecdev1 "PAUSED, relaunch by 23:40 or the box is yours". FIX
3bda38b: `record.join_notes(notes, prefix)` is the only path from the
per-cell list to `note`/`status_detail` — joins under
`record.FREE_TEXT_MAX`, drops from the end, ends with "[+N note(s)
elided …]"; the ROUTINE calibration sentence is no note at all (every
row's `calibration` block + `timing.iterations` carry it) — only a
capped / no-timing / fixed calibration remains a sentence.
`check_note_length_guard`: five controls, the cap read from the SCHEMA
JSON, the rejected record's own 72-sentence shape replayed; a bounded
`--dry-run` cell validated end to end; `make check-harness` 112/112;
committed; RE-OPENED 23:21. The rejected record went to the scratchpad,
never the store.

THE SIX CELLS: interp measured (23 min); jit `inconclusive-load`
(after-sample 10.10 % vs 10.00); auto `inconclusive-load` (20.20 %);
nocaps measured; vm measured at exactly 10.00 %; vm-in
`inconclusive-load` (10.10 %). Load quiet (1.0-1.2) at both ends of
every cell; before-samples clean. `pidstat -u 1` during cell 4 named
the bursts: the VS Code remote server (`~/.vscode-server/…/node`, ~40 %
of a core for a second when the store or the log changes), a `btop` on
Frank's pts/19 (closed on request), the sessions' status-line
`gh pr list` refreshers (~40 % for ~0.5 s; pcrecdev1 had Frank switch
them off), and MY OWN claude at ~9 % while I investigated — the BD6
residue applied to myself; I stopped, replaced the per-event Monitor
by a sentinel-only one, and stayed idle. A 120-s awk over mpstat
"found" 96 busy seconds — a 12-h-clock column shift in my shell's
locale; `pidstat` was the ground truth. CLOSED 01:21; store 47 (commit
of the six records); pcrecdev1's battery 3 launched ~01:2x (≈2.5 h).

BD7 (written during battery 3, edit-only): `quiet.occupancy()` runs
`mpstat -P ALL 1 5` and `judge_mpstat()` (pure) judges mpstat's own
`Average:` block — a 1-s 30 % burst averages to 7.6 % and passes, a
sustained 100 % core still fails, the bar stays 10 %, same instrument
both ends, `occupancy.tool` names the command (pre-BD7 records say
`… 1 1`), `raw` keeps the Average block + the per-second peaks + the
target's SMT SIBLING (CPU 5 for CPU 11, from sysfs) judged like any
core. `check_occupancy_average`: seven controls on a synthetic capture
(the burst second judged ALONE reads 30 % — the old rule's fail — so
the rule, not the fixture, passes it). quiet_baseline.md's 2026-08-30
section; decisions.md BD7; plan [B12] (i) DONE. `make check-harness`
OWED: it waits for "BATTERY 3 DONE" (edit/commit only meanwhile); the
harness commit follows it.

FRANK'S GATE-SHAPE RULING (via pcrecdev1, ~01:2x): coarse pre-flight
(load1 < ~4, nothing on the target or its SMT sibling), the after-sample
as provenance, TRIAL AGREEMENT decides measured vs inconclusive, a test
run on the three cells. My answer, accepted for I-18: items 2-4 are a
SCHEMA-RULE change — X13 (validator-enforced) makes `measured` require
both occupancy verdicts, and the status enum has no spread value — so
they are a v1.4 proposal for Frank to rule on WITH the test-run data
(`docs/design/gate_shape_v14.md`, P1-P4; plan row [B20]); one
correction: keep the PER-CORE pre-flight — a steady competitor (load1
≈ 2) lowers the measured core's boost clock uniformly and a sibling
competitor halves its resources, both invisible to trial agreement.
`docs/dev/measurements/probe_gate_shape.py` over the six records:
trial spread medians 1.3-4.0 %, p90 6-19 %, the three inconclusive
cells INSIDE the measured cells' profile — the after-sample verdict
has no visible relation to trial agreement. Per-row outliers (max
64-514 %, single rows) to characterise before any spread rule.

NEXT: on "BATTERY 3 DONE" — `make check-harness` (BD7's commit) →
the TEST RUN (jit, auto, vm-in at 36d5963 under BD7, ≈60 min, both
idle) → probe archive → the bounded first-sample report → I-18 ack →
[B19] (abi 12 re-pin). Tree: harness/BD7 changes uncommitted until the
check (wake.md says so).

## 2026-08-30 (EDT, ~06:5x), fifth session (part 2) — I-18; BD7 committed 119/119; the gate-shape TEST RUN 3/3 measured; bounded@0.1's 36d5963 sample complete; reports; two lanes

THE WAIT ended at 05:19: "BATTERY 3 DONE" (san 34/0, mech 189/0/6/0/0,
solo codegen 198/0 + cli 287/0 on the fix commit), NEW PIN 96e44c2 (abi
12), I-18 in the inbox (c52a74e, the peer's single-file commit — the
D78 channel working as designed): [OPT-4] ruling B (exact prefilter
default; count-collapsed as a ladder RESCUE), `_ENGINE_SEL` on every
artifact as the 6(d) ruling, `_VM_PREFILTER_LANG`/`_WHY`, two
source-bytes columns (ask iv: yes), `--warn-emit-bytes`, [DD-11]'s
`--list-definitions`, the class ladder MEASURED at the pin (32768
RESCUED as a 32 KB collapsed-prefilter VM artifact; 65535 refused by
the NFA cap at every pin; 16384 warns), Frank's gate ruling as the
durable copy with my spread data attached, [OPT-A] next, W1 chartered.
Acked into plan.md: [B19] (the re-pin, worklist a/c/d/e then b), [B20]
(I-19 awaited), [B11.4] (this sample's refusal rows re-read: 65535 = the
NFA cap, not the size cap).

BD7 COMMITTED (4e39c25) after `make check-harness` 119/119 on the free
box. THE TEST RUN (05:22-06:17, verified by cwd, pcrecdev1 idle): the
three inconclusive cells re-run under BD7 — pcre2-jit, pcrec-auto,
pcrec-vm-in ALL `measured` on attempt 1, every pre-flight passed first
time; after-samples 1.81 / 2.00 / 3.81 %; the OLD 1-s gate recomputed
from the recorded per-second peaks passes two of them on every second
and FAILS pcrec-vm-in on one of its five seconds (11.88 %) — a burst
BD7 absorbed; trial-spread medians match their first runs within 0.3
points (3.7/4.0, 1.5/1.6, 1.5/1.4 %). The inconclusive stamps carried
no information about the measurement. Archived:
docs/dev/measurements/2026-08-30-gate-shape-test-run.txt (b0fcb96).
Store 50 (7869b9d): bounded@0.1's 36d5963 sample is COMPLETE, 6/6 — the
[OPT-4] BEFORE. pcrecdev1 closed at 06:1x and re-woke at 06:2x; the box
plan agreed: their admin1 verification + a -j4 code lane now, my [B19]
worktree build beside it, a ~3.5 h abi-12 window (bounded AFTER +
email/loglines controls) announced before their next battery.

REPORTS (0c2d9a2): reports/2026-08-30-bounded-0.1-budu-ryzen1600-
first-sample-36d5963.{md,subject-grain.md,tsv}, `--until
2026-08-30T12:00:00Z` from the first render (the pcre2 ids carry no
pin; [B19]'s window is next). First reading, before the ledger:
`cls-upto-65535` did-not-compile under auto AND nocaps (`NFA exceeds
131072 states`) — the NFA cap; `cls-upto-32768` COMPILED as a plain-VM
artifact (no prefilter, cursor rung) — the set's predicted abi-11
size-cap refusal did not fire; the ctx ladder and cls-upto-16384's
whole-subject form are VM (the engine-role state cap), their plain
forms DFA; nest2-64 whole-subject is a counter-rung VM with fast-tier
escalation 88/50 → 128/73.

LANES: `ledgerbounded` (opus, read-only) extracts the ledger to a
scratchpad file (O-9 material); `b19repin` (worktree b19repin, branch
b19-repin) does I-18's worklist a/c/d/e with by-value controls on
level-context's predicted stamps, the two source-bytes columns, the
`--warn-emit-bytes` capture, `--list-definitions` archived. Stall
watchdog cron every 10 min. Keepalive cron still ticking.

## 2026-08-30 (EDT, ~07:4x), fifth session (part 3) — the bounded ledger read; O-9 sent; [B11.4] COMPLETED; KB-3/KB-4; U2/U3; docs/dev/ledgers/

THE LEDGER (lane ledgerbounded, opus, read-only, 15 min; archived as
docs/dev/ledgers/2026-08-30-bounded-0.1-first-sample-36d5963.md, 895
lines, the new directory's first file — the derivation behind an outbox
item, with report-line citations, so O-9's numbers trace to tables).
What bounded's first sample says at 36d5963, in the order O-9 sends it:
the set's predicted first refusal (the abi-11 emit cap at 32768) is
REFUTED twice — 32768 compiles under auto as a plain-VM artifact and the
first refusal is 65535 by the NFA cap (131,072 states), which `pcrec-vm`
builds in 2.9 ms and answers at 0.7-1.4× pcrec's best: auto refuses
what its own VM handles, the NFA cap checked before any [SEL-1] rung (a
ROUTING gap, candidate 4); all the ladder's compile growth is auto's DFA
build — emit-c O(n^1.8-2.0), the .so linear at ~12 B/count, gcc 3 % —
while pcrec-vm's compile is flat at every rung; the DFA→VM transition
per skeleton and form (whole-subject always the harder compile; ALL
FOUR ctx rungs VM in both forms, refuting NOTES.md's "64 fits"; the
greedy twin overflows too, byte-identical); the wasted DFA build ×315-
×687 on seven cells (2.2× level-context's), with eight labelled
overflow points for [SEL-1.2]'s missing correlation; RX_UNROLL_K moved
ONCE — nest3-16 K=1/size-model, nest2-64 at the same product K=8: depth
not product — and the reporter did not render it (KB-3, folded into
[B19]'s lane: K/why/caps on the compile legend); the match axis — auto
1st-or-2nd on 10/13/7 of 22 members in match/search/throughput, faster
than the JIT on 20/12/9; the cliffs ×18,400 (nest2-letters-6 r-00037)
and ×65,500 (nest3-3 d-00028) with auto FLAT across them and pcrec-vm
paying them in the JIT's class; the ctx band 4-5× behind the JIT in
search and throughput (a milder level-context), auto = vm on all 12 ctx
cells; the biggest non-cliff gap — an end-anchored DFA on
`dfa_match=search-filter` paying ×37 on one subject (cls-upto-4096
whole/l-07: 405.9 vs 10.9 ns) where [ENG-ABS]'s unwrapped form does not
reach (candidate 1); auto selecting the counted DFA on exactly the
rungs where the VM is 6× faster (cls-upto-16384 throughput 3.61 vs
0.61 ns/B; the 32768 rung, VM, 5.5× faster than 16384's DFA — candidate
2, a selection knee on the count); pcrec-vm with NO prefilter on any of
48 artifacts (2.67 ns/B for a pure miss, ×169 on the floor row — the
BEFORE of abi 12's `_VM_PREFILTER_LANG` rebuild, candidate 5); vm-in
1.15-1.49× SLOWER than vm on throughput (reverses O-4). 25 NOTES.md
predictions: 17 confirmed, 4 refuted, 2 half, 2 untestable; I-18's own
"32768 behind the JIT on search" already false at the BEFORE (0.52×).
O-9 carries all of it plus the test-run numbers for I-19 and six asks
(a refusal-reason stamp; is whole-subject search-filter intended; a
knee-locating 0.2; time a refused compile; the prediction; a 1024 class
rung). [B11.4] COMPLETED and archived (its three numbers produced);
[B11] notes #3 [B11.2] next after the abi-12 windows. KB-3 (the
reporter's [ART-SIZE] blindness — "a stamp read is not a finding until
rendered"; [B18] (e) added five reads and zero renders), KB-4 (a
did-not-compile row is untimed). U2 (pcre2-jit slower than interp on
pure-scan find-all rows), U3 (PCRE2's group replication, NOT-A-BUG).
b19repin still building; its scope gained the [ART-SIZE] legend line.

## 2026-08-30 (EDT, ~07:0x), fifth session (part 4) — I-20; [B19] delivered and MERGED (87f86b1): the abi-12 adapter, four letter-vs-artifact findings, the [ART-SIZE] legend

I-20 (b44ad7b, pcrecdev1's single-file commit): O-9 ask (ii) is a
DESIGN LIMIT — the [ENG-ABS] anchored machine caps at
`PCREC_ANCHORED_MAX_STATES` = 4096 with no runtime raise; measured
crossovers plain/whole `[a-z]{0,n}` 4095→4096 / 2047→2048 (our `(?:…)\z`
spelling HALVES the reachable `{0,n}` count: an EOF-aware sibling per
count-state), `{n,}` 4095/4094, nest2 63/14, nest3 15/6 — so a bounded
rung's plain and whole-subject rows are DIFFERENT MACHINES (the reading
rule now in reports/CLAUDE.md and [B19]'s frame); candidate 1 becomes a
D86 row proposal; (i) refusals bucket on exit code + the diagnostic's
leading clause, no token owed (D77); (iv) the refusal cost is the
bench's own clock — KB-4 is a bench-side fix; (v) acknowledged; (iii)/
(vi) and candidates 1/2/4 wait on Frank's D86 pick. Acked (d4e429a,
d574ca4). `--list-axes` at the PIN is 54/21; main's 61/21 is past it.

[B19] (lane b19repin, worktree, ~35 min build + ~25 min docs/controls;
delivery file in the scratchpad; merged 87f86b1 with one plan.md
conflict — the lane's progress note + my I-20 frame): pin 96e44c2 built
by pin.sh; `list_axes.tsv` 54/21 (the diff is exactly the seven new
rows), `list_definitions.tsv` 50 rows, both diffed against the pin;
the shim reads `RX_ENGINE_SEL` on every artifact and
`RX_VM_PREFILTER_LANG`/`_WHY` on VM HYBRIDS ONLY (match_api.md §6.3's
iff — I-18's "every VM artifact" and my brief's `lang=exact` for a
forced VM were both wrong: a forced artifact stamps neither; a new
exclusive `vm-hybrid` scope, agreement rules 8/9: `forced` iff the
CONFIG named `--engine=`, the token's only control); PB_SHIM_MIN_ABI
stays 10 (macros, no field). `emit_bytes`/`emit_code_bytes` by a PORT
of pcrec's `emit_size_measure`, controlled byte-exact (8/8 kinds ×
forms) against `--warn-emit-bytes`'s own numbers and REFUSING (an
AdapterError, never a number) any warned compile where the two
disagree; `warned_emit_bytes` + the line in the diagnostic, never a
failure. level-context MEASURED = I-18 (ii)'s prediction to the letter
(`collapsed-prefilter` / `count-collapsed` / "dfa overflow retry, exact
nfa 462"; the `\z` form 463); its artifact grew from a 32,761 B plain
VM `.c` to an 88,438 B hybrid — the rung now keeps a prefilter DFA.
FOUR LETTER-VS-ARTIFACT FINDINGS (for O-10): (1) the lang pair is on
hybrids only (above); (2) the SIZE-CAP rung's rescue stamps
`_ENGINE_SEL "selected"` (K41 witness 2: `count-collapsed`, "size cap
retry, exact 671050 > 500000") — per match_api.md's table, but Frank's
bucket `sel ∉ {selected, forced}` does NOT see it; its only trace is
`_LANG_WHY`'s prefix; the reporter's legend note names the gap; (3)
`-fno-prefilter-collapse` refuses only on the size-cap rung — on the
[SEL-1] rung the denied build is the 36d5963 shape (`overflowed-dfa`,
no prefilter, still compiled), so the brief's control asserts what IS
true and the refusal control moved to K41's witness; (4) `_LANG_WHY`
has a sixth value, `no counted repeat`. Plus, from the `--dry-run`
rehearsal of one bounded cell at the pin (synthetic, compile facts
only): `engine_sel` census `selected` 32 / `collapsed-prefilter` 14 —
the ctx four (both forms), cls-upto-32768 (both), and the `\z` forms
ONLY of cls-upto-16384, cls-lazy-16384, nest2-64, nest3-16 (K7's
48,000,000-element budget) — the nests' PLAIN forms are `selected`
DFAs where I-18 predicted `selected` VMs; `warned_emit_bytes` fires on
THREE forms (cls-upto-16384 plain 724,699 — I-18's 725,692 counts a
differently-named `#include`; cls-lazy-16384 plain; cls-upto-4096's `\z`
form, which I-18's plain-only table did not see); nest3-16's `\z` form
is K=1 / size-model. Reporter: `sel=`/`lang=` clauses, the derived `DFA
fallback tripped` bucket + legend note, `emit bytes`/`code bytes`
columns with `(warned)`, TSV rows, and the scope addition — `K=`/
`caps=` on the legend line for VM artifacts (KB-3 closed) — all
CONDITIONAL, v7 unchanged, every committed report byte-identical (the
re-render control runs with `make check` on master). Worktree
removed. `make check` on master (87f86b1, under setsid after a
harness-killed first attempt): 3/56/0 · 141/141 · 54/54, rc 0; the
committed bounded report re-rendered with the merged reporter diffs
275 lines against the committed file. Next: the abi-12 windows.

## 2026-08-30 (EDT, ~10:5x), fifth session (part 5) — THE ABI-12 WINDOWS: 18/18 measured on attempt 1 at 96e44c2; reporter v8 + the AFTER reports in a lane

THE WINDOW (07:12-10:45 EDT, one setsid chain over three sets, pin
96e44c2, core 11, both managers idle; pcrecdev1 had stopped its w11
lane and, on my verify-by-cwd, killed three leftovers of its own — a
tail/head/ugrep Monitor armed at 06:16 on MY rerun log from a shell
whose cwd was its since-deleted admin1 worktree; BD6 again, and the
peer's own kill-by-PID). bounded six cells → email-specimen@0.2 six →
loglines@0.1 six: EVERY cell measured on attempt 1 — zero gate
refusals, zero losses — where the 36d5963 windows had refused attempt 1
of almost every cell on the post-cell transient and lost three of six
to the one-shot after-sample. BD7's instrument, measured: the 5-s
average never saw the transient the 1-s sample tripped on. Store 68
(33ee50f). Cell timings (start-end EDT): bounded x pcre2-interp 07:12-07:35; bounded x pcre2-jit 07:35-07:53; bounded x pcrec-auto 07:54-08:14; bounded x pcrec-nocaps 08:14-08:33; bounded x pcrec-vm 08:33-08:51; bounded x pcrec-vm-in 08:51-09:09; email x pcre2-interp 09:10-09:18; email x pcre2-jit 09:18-09:29; email x pcrec-auto 09:29-09:34; email x pcrec-nocaps 09:34-09:39; email x pcrec-vm 09:39-09:46; email x pcrec-vm-in 09:46-09:53; loglines x pcre2-interp 09:53-10:02; loglines x pcre2-jit 10:02-10:11; loglines x pcrec-auto 10:11-10:19; loglines x pcrec-nocaps 10:19-10:27; loglines x pcrec-vm 10:28-10:36; loglines x pcrec-vm-in 10:36-10:44;
The chained launch + sentinel-only Monitor + keepalive-tick-only
activity kept this session's residue off the gate for 3.5 h.

AFTER the window: WINDOW CLOSED 10:45; pcrecdev1's battery follows.
Lane reports96 (sonnet, worktree reports96): REPORTER_VERSION v7 → v8
(the [B19] K=/caps= clauses change every committed report carrying
abi-11 pairs — the bounded first sample re-rendered diffs 275 lines,
all additions; by reports/CLAUDE.md's rule the committed files must
re-render empty, so every report is regenerated with its own query and
the diff CLASSIFIED per file — version line only for the pre-abi-11
sets, K/caps additions for the 36d5963 sets, anything else a stop), and
the three AFTER reports (`--since 2026-08-30T11:00:00Z`; the pcre2 ids
carry no pin, so the BEFORE/AFTER files are separated by their
--until/--since bounds). Then the [OPT-4] ledger lane over the AFTER
reports against docs/dev/ledgers/…§6 and I-18's table; O-10 with
[B19]'s four stamp-semantics findings. (This entry re-written once: an
unquoted heredoc had shell-substituted its backticked text — a lesson
for wake.md.)

## 2026-08-30 (EDT, ~13:4x), fifth session (part 6) — the abi-12 AFTER ledger read: [OPT-4] SPLITS; O-10 sent; I-19 acked ([B20] proceeds, [B21] opened)

I-19 (071638f): BD7 RATIFIED as the gate on the test-run evidence; Frank's
(2)-(4) become the v1.4 SPREAD RULE — [B20] proceeds (design + panel
after O-10); candidate 2 (the {0,n} class-count knee) is pcrec's [OPT-5]
behind [LIM-1] (a single limits table, `--list-limits`); O-9 asks
(iii)/(vi) chartered → [B21] bounded@0.2; the size-cap rescue's
`_ENGINE_SEL "selected"` folded into [LIM-1] — bucketed on the `_LANG_WHY`
prefix meanwhile (9e45d92, test + control).

THE AFTER LEDGER (lane ledgerafter, opus, read-only, ~25 min; archived
docs/dev/ledgers/2026-08-30-abi12-after-96e44c2.md, 872 lines; the AFTER
reports read from the reports96 worktree before their merge). [OPT-4]
SPLITS by whether anything survives the collapse: the ctx band (search
22,5xx → 8,1xx-8,8xx ns/set, 4.0-5.0× behind the JIT → 1.5-1.8×;
throughput 4.15 → 1.86 ns/B) and level-context (search ×4.60 faster,
13.44× → 2.92× behind the JIT; 1 MB 9.83 → 2.67 ns/B) WIN — the largest
gain the bench has measured on a pin — and the rescued fallback now beats
pcrec's own `--engine=vm` 2.2-4.6× (auto ÷ vm 1.00 → 0.32-0.45; vm flat):
checklist 13's finding fired. `[a-z]{0,32768}` LOSES 3.6×: `X{m,n}` →
`X{min(m,1),}` makes it `[a-z]*`, nullable, admitting at every position;
t-digits-016k, the subject I-18 said would dismiss, is ×1.65 slower; the
three `cls-*` hybrids stamp `dfa prefilter=none` beside
`vm_prefilter=hybrid` — the structured signal that separates the losing
shape. Ten labelled points, one predicate (non-nullability of the
collapsed language) — O-10 candidate 1, ask (i). Controls flat (+216/224
B stamp block everywhere; [OPT-K]/[ENG-ABS]/cliffs/floors unmoved;
cls-upto-65535 still refused; the wasted DFA builds unchanged; http-5xx's
×1.03 flag retired) except `year4` +4,096 B with identical stamps (ask
iii). The emit/code-bytes survey: the class ladder is 100 % table data
(code flat 11.6-12.7 KB; ~41-43 B of C and ~12 B of .so per count). The
[OPT-5] frame: the counted DFA loses 5.1-5.9× to the VM on letters at
EVERY rung from 256 and wins 1.75× on digits at every rung — the knee is
a property of the subject, not the count; [B21] adds rungs at 64/128 too
and asks for predictions per subject. Checklist 12/3/2/1. Reporter gap:
the AFTER reports hold one pin each, so R8's Δ column fired on 0 of
3,636 rows — a repin-form render with both pins follows ([B19] close-out).
O-10 (this commit) carries all of it plus [B19]'s four stamp findings and
six asks. U2 re-measured. Reports lane: make check running; merge next.
