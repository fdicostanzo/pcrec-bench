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

## 2026-08-30 (EDT, ~13:5x), fifth session (part 7) — reporter v8 and every report regenerated (lane reports96 merged 1de2ad0); make check green on master; [B20]'s design lane opened

LANE reports96 (sonnet, worktree; ~2 h 40 min, slowed by serial renders
under the battery until told to parallelise): REPORTER_VERSION v7 → v8
(the [B19] `K=`/`caps=`, `sel=`/`lang=` and emit-bytes clauses change
every committed report carrying abi-11+ pairs — precedent R10 → v7); all
21 committed reports regenerated in place with their own queries and a
CLASSIFIED diff per file: the 8da6120/692c2e8/35e1ab1 sets by the
version line + the store-index candidate count only; the three 36d5963
sets by those plus the `K=`/`caps=` clauses and the legend note. THE
LANE STOPPED ONCE, correctly: the three 36d5963 queries picked up the
[B19] AFTER sample that had entered the store the same morning — E and
F had NO date bound (their entries had said every record already
existed; no longer true) and G's `--until 2026-08-30T12:00:00Z` (my
guess, set after the 10:00Z re-run but before the AFTER window's start
was known) fell INSIDE the window and admitted one 96e44c2 record —
a half-contaminated file. Ruled `--until 2026-08-30T11:00:00Z` for all
three (every 36d5963 record ≤ 10:00:09Z; the AFTER's first is 11:12Z)
and the standing rule in reports/CLAUDE.md: EVERY report is rendered
with an explicit bound, because the next window always adds newer
records under the unpinned pcre2 ids. The three abi-12 AFTER reports
(`--since 2026-08-30T11:00:00Z`, 6 records each, ids verified) were
re-rendered after merging master (the I-19 bucket tweak 9e45d92 changed
the `sel=` legend note that prints only on abi-12 reports). `make check`
in the worktree and on master after the merge: 3/56/0 · 141/141 ·
54/54. Reviewed: two 36d5963 reports' diffs re-checked by class (no
disallowed line), the AFTER headers, the rule sentence (reports/
CLAUDE.md:88). Worktree removed.

STILL OWED for [B19]'s close: the repin-form AFTER reports (both pins in
one query, `--since 2026-08-29T00:00:00Z --until 2026-08-30T15:00:00Z`,
`…-repin-96e44c2.*`) so the reporter's R8 Δ column carries the verdicts
the abi-12 ledger computed by hand — rendering now, three sets in
parallel, untimed beside pcrecdev1's battery.

[B20] OPENED as a design lane (b20design, strong model, worktree): the
proposal becomes the SPEC — the ratified BD7 gate + Frank's item-1
second clause (the target core read before the run), X13 revised to the
pre-flight, the after-samples as provenance, `inconclusive-spread` with
a `trial_agreement` setup block whose numbers are recomputable (X30/X31
in X20's shape), and the rule's constants k and F MEASURED by a probe
over the store's 68 records (zero false positives on a store measured
quiet is the bar; the probe and its census archived under
docs/dev/measurements/ per D35) — then a critic panel.

## 2026-08-30 (EDT, ~14:0x), fifth session (part 8) — [B19] closed; [B20]'s SPEC merged with measured constants; the critic panel opened

[B19] COMPLETED (f0b56e7): the repin-form AFTER reports — both pins in
one query (`--since 2026-08-29T00:00:00Z --until 2026-08-30T15:00:00Z`,
10 records per set) — make the reporter's R8 `Δ vs previous version`
column fire on every pcrec row, so the abi-12 ledger's hand ratios now
have the reporter's own spread verdicts beside them (the TSV carries no
Δ column; the `-after-` files stay the clean single-pin sample). Root
STATUS updated; [B19] archived (19 completed rows).

[B20] DESIGN (lane b20design, strong model, worktree; ~30 min; merged
fa152d3 with the same plan.md hunk resolved by hand): gate_shape_v14.md
is the SPEC. The census (probe_trial_agreement.py, archived D35 as
2026-08-30-trial-agreement-census.txt): 68 records, 62,923 timed rows,
all with 5 trials; at k = 1.5 ZERO rows have two slow trials and ONE has
a fast outlier (a 3-2 split at 9-14 ns on the floor pattern); at 2.0
nothing; at 1.25 the clean spread is reached (21 slow pairs, 37 fast
outliers, 20 records touched). Rule `v1.4-1of5`: k = 1.5, F = 1 % — zero
false positives on the store, margin 4.9× (worst 1 of 490 rows vs 4
allowed); flags any two-pass disturbance of one group (every group has
≥ 23 subjects); the fast clause catches a moved median. The store's one
loaded record (email × interp 08-29 18:48Z, load1 11.4 after) has zero
disagreeing rows at 1.5 and its medians sit within 0.2-1.8 % of its
clean re-run — the competitor arrived as the cell ended; the rule's
silence is right, and k = 1.25 would have flagged good numbers. Honest
limit: no store record has numbers a competitor actually moved (Q3 asks
for one deliberate scratch-tier control). Decisions: the target-core
pre-flight as an optional `occupancy.<sample>.target_busy_pct` (X26
untouched); X13 versioned, reading load.before directly (X20 unchanged
— a v1.4 record can be `loaded` + `measured`, Q8); the `trial_agreement`
SETUP block required iff trials ≥ 2 (X33), X31 verdict-vs-fraction, X32
recomputation as a DELIBERATE second implementation in the validator
(the control that shares no source); precedence -load > -spread. Two
corrections to my brief: X30 exists (the new rules are X31-X33); the
historical inconclusive-load population is NINE (three more on
2026-08-25 + the loaded one), all left as history. Findings: trial-1
outliers exist store-wide (36 of 387 single-slow rows, the LEAST
frequent index — the test run's "never trial 1" was true of six
records); `harness-failure` is a status the harness never stamps (Q2).
Ten open questions.

THE PANEL (skill §6): three read-only opus critics, briefed to refute —
A measurement validity of the rule (the base rate under the clean
spread; is 1.5 at a cliff; the positive case constructed analytically;
the fast clause; N ≠ 5; small cells; the timer floor; the probe's row
selection), B schema/validator consistency (every hunk writable from
the text; X13-as-versioned vs v1.1/1.2/1.3 records; target_busy_pct
under additionalProperties: false; X32 vs record.py's "derivations are
imported, never reimplemented"; §10.3; the nine records; one bad
example per rule), C harness/reporter/checks/migration (the target-core
reading when judge_mpstat excludes the target; the status decision
table; the one derivation's input shape; R1/R2/R8 with inconclusive-
spread; each §8 check's control; whether v1.4 forces a report
regeneration; harness-failure's exception paths; KB-4 riding along).
Findings → docs/dev/reviews/2026-08-30-r3-gate-shape-v14.md with
dispositions (r1 requirements, r2 record schema exist). Watchdog cron
e18385c9. Keepalive cron still ticking.

## 2026-08-30 (EDT, ~14:1x), fifth session (part 9) — the [B20] panel: three verdicts, five blockers, the manager's rulings; the r3 compile-and-apply lane

THE PANEL (three read-only opus critics, ~15 min each; findings in the
scratchpad, to be consolidated into docs/dev/reviews/2026-08-30-r3-gate-
shape-v14.md by lane b20r3): all three say "the design is sound, not
implementable as written". BLOCKERS: A1 — F = 1 % lands EXACTLY on a
group boundary: disagreements are GROUP-quantised (a burst hits one pass
of one group, all its rows or none); email's throughput groups hold 5
subjects against F·N = 5.00/5.01 on seven real records (margin 0.00-0.01
rows), and no fraction-shaped F is safe (2 % silences a fully disturbed
30-subject bounded group) → a group-level rule with integer arithmetic;
B2 — target_busy_pct's "null iff unavailable" contradicts the harness's
own null case (a missing target row on a pass sample) and the schema's
three-branch allOf is not named → the hunk cannot be written; B3 — MINOR
is not defensible under record_schema.md's own rule ("a changed meaning"
is MAJOR) and MINOR is exactly the relation that pools a 1.3 measured
and a 1.4 measured in one table → a ruling; F2 — a missing target row
would stamp `measured` and be REJECTED at store.write after the whole
cell (the [B12] failure mode reintroduced) → a pre-flight refusal; F5 —
the status-deciding sentence lands LAST in the note list, exactly where
join_notes elides (bounded already over the cap) and _excerpt cuts at
120 chars → first, and R1 renders from the block. MUST-FIXES: the blind
band (3-4 of 5 passes slowed ≤ 1.5× moves the ranked median up to 49 %
and reads agree; 46 % of the store's ≥ 1.3× perturbations are below
1.5×); power unstated and non-monotone (P(flag) 0-2 % at 2 s, 57-92 %
at 30 s, 54-68 % at 600 s — a long competitor covers all five passes
and goes invisible); a PASS is 0.07-20.2 s, not "1-2 s"; one constant
denotes four rules across N (N = 3 cannot fire the slow clause; quick
defaults to 3); X32's arithmetic unpinned (six ambiguities; the failure
mode a destroyed pinned cell); the quiet CLI bypasses gate(); no exit
code for inconclusive-spread; exclude_cpu vs pinning.cpu; check_fields
needs 15 field-table rows; the examples plan is wrong about which
examples exist (no 1.3 good example); status_detail's meaning change.
REVERSED: Q9 — the single fast row is a REAL 51 % bimodality (12.2 vs
18.7 ms over 1.32 M iterations; flat in the other artifact), the rule's
only demonstrated true positive. ANSWERED: harness-failure is
unreachable (leave it); KB-4's schema half rides with v1.4; R3+R4 force
the regeneration, not the bump; k = 1.5 is 0.20 from a false positive
(the contaminated record clears at k ≥ 1.35) and the store is
uninformative in [1.55, 2.0]; the slowest-trial histogram is dominated by
one record (158 of 387 events).

THE RULINGS (R-1..R-20, docs/dev/reviews/2026-08-30-r3-rulings-gate-
shape-v14.md, copied verbatim from the scratchpad): MINOR with §4
amended for rule-versioning (the validator's X17 behaviour is the rule);
the target core as a tri-state field keyed on pinning.cpu with a
PRE-FLIGHT refusal on a missing row; §3.5 "the rule as arithmetic" with
integer-count comparison; the status sentence FIRST and R1 from the
block; today's note/status_detail split kept; exit code 4; the CLI
through gate(); harness-failure left unreachable; KB-4's schema half;
no sleep injection in the drivers; pinned requires N ≥ 5 and odd (else
n/a-trials, not measured); no timer-floor exemption (the fast row is
real); THE GROUP-LEVEL RULE replaces F (constants D_MIN and c chosen by
a recompute over the store, archived as a new census); the blind band
and A's power table stated in §3; the per-group /proc/stat occupancy
timeline accepted as PROVENANCE only; timed-out trials count as
disagreeing; k stays 1.5 with its margin stated. Lane b20r3 (strong
model, worktree) compiles r3 with these dispositions and applies them to
the spec; watchdog cron.

## 2026-08-30 (EDT, ~14:4x), fifth session (part 10) — r3 compiled and applied (2aca1cd): the GROUP rule; E-1..E-3; the implementation lane opened

LANE b20r3 (strong model, worktree, ~35 min): docs/dev/reviews/2026-08-
30-r3-gate-shape-v14.md — all 45 findings (A 11, B 17, C 17) in the r2
format with dispositions citing R-1..R-20: 29 accepted, 15 accepted-
amended, 1 deferred (C-F17, code comments), 0 rejected whole; the spec
rewritten §0-§9 with every accepted change (§H verbatim, §H.2 added).
THE GROUP RULE `v1.4-group`: a row disagrees at ≥ 2 slow trials
(> 1.5 × its median) or one fast (< median / 1.5) or a mixed timed-out
trial; a GROUP (pattern, regime, form) disagrees at d ≥ 2 AND 3·d ≥ n;
a record disagrees at ≥ 1 disagreeing group, judged only at N ≥ 5 and
odd. Constants from the group census (probe --groups; archived
2026-08-30-trial-agreement-census-groups.txt): at k = 1.5 the largest d
in any group in the store is 1, so every candidate gives zero
disagreeing groups; (2,3) and (2,4) are the only pairs flagging both
R-16 shapes (a whole-group two-pass disturbance and a half-pass
overlap) at n = 4/5/30/85/112 ((2,2) fails the half shape at odd n;
D_MIN = 3 fails at n = 4, 5); (2,3) chosen — margins over the store
2/1/10/29/38 rows; the k margin at group level: the loaded record
flags at k ≤ 1.40, clears at 1.45. ESCALATIONS RULED: E-1 — the store's
five timed-out rows are ALL-five-trials engine refusals (pcre2-jit ×
factored / 1 MB atom run — U1), not disturbances: a MIXED row
disagrees, an all-timed-out row is unjudged under
rows_unjudged_reasons.all_timed_out; E-2 — a scratch-tier n/a-trials
record keeps the pre-flight's status (quick and the smoke suite never
write inconclusive-spread; scratch is never ranked); E-3 — (2,3)
confirmed as the least sensitive pair flagging both shapes, (2,4)
recorded as the tighter option to revisit after the first v1.4 window.
Merged 2aca1cd (docs only).

LANE b20impl OPENED (strong model, worktree): the implementation in
five committed steps — schema + validator (1.4, the tri-state target
field, the block, X13 versioned, X31-X33, KB-4's schema half,
record_schema.md's §4 clause and tables, the examples against the real
store), harness (the target clause + missing-row refusal, the quiet CLI
through gate(), ONE derivation in reduce.py, the status table, the note
order, exit code 4, run_window's single retry), reporter (the agreement
legend, R1 from the block, the mixed 1.3+1.4 fixture, v9 iff the
rendering changes → every report regenerated and classified), the §8
checks each with its control, docs. Box rule: check-harness and the
regeneration wait for "box free" (pcrecdev1's battery to ~15:45-16:00).
Watchdog cron. The r3 lane's delivery file and the panel files stay in
the scratchpad.

## 2026-08-30 (EDT, ~16:4x), fifth session (part 11) — [B20] COMPLETE: schema v1.4 merged green; the I-21 correction; [B23]

BATTERY DONE 15:46:59 (green by diagnosis; no abi change; pin 96e44c2
stands) → "box free" to lane b20impl, which closed out in ~50 min: make
check GREEN in the worktree and then ON MASTER after the merge
(8b6d585; one plan.md conflict resolved) — check-schema 4/72/0 (the
generated 1.4 example + 16 one-rule sabotages), check-harness 170/170,
check-report 59. All 13 committed report triplets (39 files — the
brief's ~25 undercounted) re-rendered at reporter v9 with their own
header queries and classified: 39/39 clean, zero unexplained lines, no
number moved. Zero escalations; eight deliberate calls all confirmed
(the §3.6 timeline only when pinned; the v1.1-1.3 rule label; the
advisory warm-up; the reported-not-asserted quick verdict; the
simulated-quiet exit-4 check; TSV reusing columns; the one-row fixture
witnessing R-16; the two identity-preserved unbounded queries). THE
FIRST LIVE FIRING of the target clause: the rehearsal's pre-flight
named pcrecdev1's battery on cpu11 (66.20 % over the 5-s average) —
the uniform competitor trial agreement cannot see, caught before the
run by the clause Frank's item 1 asked for. Two pre-existing checks
took premise updates (6ea51e3, verified genuine). [B20] ARCHIVED;
follow-ups: Q1 → [B22]'s first v1.4 window; Q3 → [B23] NEW (the
measured positive control, gated on Frank's perf hold); KB-4's other
halves stay filed.

THE I-21 CORRECTION (ce8fca9, landed mid-merge): [OPT-4.1]'s
code-derived minw analysis corrects the prediction — the nest wholes
(minw 1) are NON-nullable and KEEP their rescue (a named residual under
pcrec D77); the decline set is exactly the nullable cls-* cells
(cls-upto-32768 both forms, cls-upto-16384 whole, cls-lazy-16384
whole), and a decline stamps `RX_ENGINE_SEL "declined-nullable"` — a
SIXTH engine-route value the adapter reads at the [OPT-4.1] re-pin
([B22]: enum, scope, by-value controls, the list-axes row);
`_LANG_WHY "nullable collapsed language"` exists only under
-fprefilter-collapse. Acked 842599b.

Frank's performance-test hold (relayed ~15:3x) stands: no windows until
lifted; [B21]/[B22]/[B23] queued. I-22 (asks ii-v by probe) still owed.

## 2026-08-30 (EDT, ~19:5x), fifth session (part 12) — bounded@0.2 CUT and merged; I-22 acked earlier; battery 5 runs on the pin candidate

LANE b21cut (blinded, D27, ~55 min incl. its own check-harness under
battery-5 load): bench/bounded@0.2 — six knee rungs (cls-upto-64 / 128
/ 512 / 1024 / 2048 / 8192; the class ladder is now 11 factor-of-2
rungs 64..65535), the group-vs-class pair completed WITHOUT a seventh
pattern (the lane saw that cls-upto-1024 IS the class half against
grp-upto-1024 — tagged group-pair), t-digits-004k appended LAST in the
generator so all four 0.1 runs reproduce byte for byte (sha256s
unchanged; every 0.1 pattern byte-identical — 0.2 records stay
comparable per cell, and NOTES states the never-pool rule for set
sums), 1,950 oracle expectations with zero give-ups, oracle_limits
extended without touching the 0.1 probe content, sidecar 0.2, NOTES
"What 0.2 added" with the oracle-side knee curve (find-all counts
65/33/17/9/5/3… down the letters ladder — the 1/n curve; digit runs
flat) and the updated cell-time (~12-15 min per cell, floor 8.1 min).
The diff's footprint: bench/bounded/ only — the blinding held. Merged
(this commit's parent), worktree removed; check-harness 170/170 in the
worktree at identical content, so master's full re-check waits for the
next code change. [B21] STATE:started — the window is gated on the
[OPT-4.1] pin (battery 5 on cdaae0b, ~21:50) and Frank's perf hold.

## 2026-08-30 (EDT, ~20:2x), fifth session (part 13, CLOSE)

Frank: "do a session close and we'll pick up with new work next time."
State at close: master 28ea2ad + this commit, tree clean; make check
green at 4/72/0 · 170/170 · 59 (verified on master after the [B20]
merge; [B21]'s cut re-verified 170/170 in its worktree at identical
content). No lanes, no worktrees (b19repin, reports96, b20design,
b20r3, b20impl, b21cut all merged and removed), no monitors, no crons
after this entry (the keepalive deleted at close). Store 68 (schema
1.1×11 / 1.2×3 / 1.3×54; new records write 1.4); pin 96e44c2 (abi 12);
the [OPT-4.1] pin candidate cdaae0b under pcrecdev1's battery 5 at the
time of writing (~21:50 green expected; the pin line and BATTERY DONE
arrive as cross-session messages the NEXT session will not see — the
durable copy lands in the inbox). Frank's performance-test hold STANDS.

The day, in one paragraph: the fifth session ran ~20 h across a night
and a day — the hold for [OPT-4]'s battery; bounded@0.1's first window
(which found the note-cap harness bug and the one-shot after-sample
defect, fixed as 3bda38b and BD7); the gate-shape test run that
ratified BD7; the abi-12 re-pin ([B19]) and its 18/18 AFTER sample;
the two ledgers and O-9/O-10 (the [OPT-4] split on nullability that
became pcrec's [OPT-4.1]); Frank's v1.4 ruling carried through spec →
three-critic panel → rulings R-1..R-20 → the group rule → the
implementation, merged green with every committed report regenerated
twice (v8 then v9) and classified clean both times; I-18..I-22 acked
with two corrections absorbed; bounded@0.2 cut blinded and merged;
[B22]/[B23]/[B24] chartered. Six lanes, three critics, two windows,
zero lost cells after BD7.

## 2026-08-31 (EDT, ~09:2x), sixth session (part 1) — wake; I-23..I-26 acked; hold lifted; [B22] re-pin lane launched at pin 263b013

Wake per the skill: wake.md, inbox, journal, plan. Four new inbox
items acked in e1c9358: I-23 (pin fa01910, superseded), I-24 (FRANK
LIFTED THE PERF HOLD), I-25 (THE PIN IS 263b013 — [LIM-1]; adds
--list-limits as a third registry archive target and a DISTINCT
RX_ENGINE_SEL value for the size-cap rescue, replacing the "selected"
mislabel: the bucket reads the value now), I-26 ([OPT-5] STEP 0: the
letters/digits split is address-only vs data-dependent loop-carried
registers — mechanism-backed TWO FLAT LINES predicted for [B21]'s
rungs, NO count crossover, not a limits row; perf_event_paranoid=4
box note appended to quiet_baseline.md). Handshake with pcrecdev1:
263b013 confirmed still the pin (main's commits above it are doc-only);
their one light lane (quoting) runs concurrently, compiles fine; their
next battery (~3.6 h) SEQUENCED AFTER our windows; window protocol =
message WINDOW OPEN, they halt by .hold artifact and confirm QUIET,
sentinel-only monitors, WINDOW CLOSED to release. Lane b22repin
spawned (worktree worktrees/b22repin): pin.sh 263b013, the three
registry archives, declined-nullable + the distinct rescue value in
adapter/reporter, the corrected decline/keep by-value controls, the
K7-vs-state-cap _WHY split, the same-pin emit-byte re-comparison
(I-22 (ii), their counting rule opt41_report.md §15), year4's
alignment note (I-22 (iii)). Watchdog cron up (10 min). Windows held
until the lane lands and is reviewed.

## 2026-08-31 (EDT, ~10:5x), sixth session (part 2) — [B22]'s re-pin half MERGED (a7f0938); windows next

LANE b22repin delivered in ~75 min, five commits, reviewed and merged.
The registry surprise: list_axes 54 → 63/21 (not 61+1) — engine-route
5→7 (declined-nullable, size-cap-retry), size-term 2→7 now WITH
stamp_values ([B18]'s documented gap closed by pcrec [REG-SV]), table
+none/+mixed. list_definitions byte-identical (50); list_limits.tsv
NEW (44 rows, third registry archive + check). All 11 I-21-corrected
points by value; the size-cap rescue reads its OWN token
(size-cap-retry) and the ask-(b) bucket is VALUE-only in adapter and
reporter v10 — the [B19] _LANG_WHY-prefix rule retired; 39 reports
regenerated, zero numbers moved (census: no stored record carries the
old why shape). Emit-byte same-pin re-comparison BYTE-EXACT on the
declined {0,32768} (18,291 plain / 18,496 whole, emit == code — no
table initializers on a declined plain-VM artifact). YEAR4 CLOSED and
RE-ATTRIBUTED (docs/dev/measurements/2026-08-31-year4-elf-page-
alignment.txt): pcrec's source grew +33 B (I-22's ~+220 was high); the
+4,320 .so step = our OWN [B19] shim's +384 B pushing the RW segment's
offset across one 0x1000 page — era-correct shim rebuild reproduces it
exactly, one-shim control byte-identical → the trigger is BENCH-side,
zero pcrec pages; goes to O-11. One honest first-run red: nest3-16
whole keeps K=1 via the size model (expectation fixed, a finding kept).
make check on the lane's tree 4/72/0 · 185/185 · 59; full re-check on
merged master running at write time. NEXT: WINDOW OPEN handshake →
bounded@0.2 × 6 testees (first v1.4 window: read the target-core
pre-flight distribution, §9 Q1) + loglines@0.1 × auto/vm (the KEEP
points), against ledger §8 + I-26's two-flat-lines frame.

## 2026-08-31 (EDT, ~14:2x), sixth session (part 3) — THE [B22] WINDOW: 8/8 cells at 263b013; §9 Q1 read

The window ran 10:43-14:08 EDT under the agreed handshake (pcrecdev1
halted its lane by .hold and confirmed QUIET; WINDOW CLOSED sent at
14:1x, their battery queues behind us). bounded@0.2's first sample: six
cells, every gate passed on ATTEMPT 1 (BD7 again; cells ~19-27 min,
above the 12-15 min estimate — the 0.2 cut is simply bigger). One
honest v1.4 outcome: pcrec-vm-in came back rc=4 `inconclusive-spread`
on attempt 1 (record kept per R-6), the once-only re-measure agreed
and stamped `measured` — the spread rule's first production firing,
and it behaved exactly per contract. Then loglines@0.1 × pcrec-auto /
pcrec-vm (the [OPT-4.1] KEEP-point arms), both attempt-1 measured.
Nine records committed (67ff0c2), all schema 1.4; store 67 measured /
9 inconclusive-load / 1 inconclusive-spread. §9 Q1 (gate_shape_v14,
first v1.4 window): the target-core pre-flight distribution over the
nine records is 0.4-2.6 %, mean 1.58 % — the target-core clause never
approached its 10 % bar on a held box; the bar is generous but the
instrument reads clean; no refusal, no missing row. Monitor lesson:
the log Monitor missed/delayed the bounded WINDOW_RUN_COMPLETE
sentinel (~24 min lost); the keepalive cron's log-tail caught it —
the fallback earned its keep, and the loglines monitor added the
"window run end" line as a second completion signature. NEXT: lane
b22reports (sonnet) renders the two report files; then the read-only
ledger lane against ledger §8 + I-21-corrected + I-26's two flat
lines; then O-11.

## 2026-08-31 (EDT, ~16:1x), sixth session (part 4) — the ledger read; O-11 SENT; [B21]+[B22] COMPLETED and archived

Lane b22ledger (read-only) delivered the 591-line ledger
(docs/dev/ledgers/2026-08-31-opt41-after-263b013.md, committed
4863c23): THE TEN POINTS 10/10 — the 8 declined-nullable cells return
to the BEFORE (search 3,088→834 ns/set, throughput = the forced VM's
1.930 ns/B, the rescue bytes gone; the two non-nullable nest wholes
keep theirs byte-identical and stay flat), the KEEP set holds within
spread with the R8 Δ column's FIRST production firing saying so
structurally. THE KNEE: none, either axis — letters DFA-loses at all
nine rungs (3.65-6.05, I-26's ratios to two decimals), digits DFA-wins
flat; the small-rung bend is ~27 ns/match VM dispatch tracking the 1/n
oracle curve; [OPT-5]'s fix promoted to candidate 1 with bounded@0.2
as a 9-rung acceptance surface. grp≡cls (+7 B, 0 ns — our §8
interpolation refuted, the good direction). New compile-axis facts:
the K7 subset route 1.8-1.9 s vs the 41 ms state-cap bail; search-
filter now three rungs ×6.9; 937,216 = 93.7 % of the emit cap; the
62→41 B/count break (ask iii). v1.4 instrument verified (pre-flight
band 0.4-2.6 %; the spread record 1/90 groups d=13/30, clean retry).
O-11 SENT (65a055c, five asks; W1.2 declared unblocked; pcrecdev1
notified live and by the durable copy). Earlier in the hour: reports
merged 115d59c — the loglines AFTER is the first CROSS-PIN report
(KB-5 filed 5c19291: no roster filter; candidate fix a repeatable
--testee). [B21] and [B22] STATE:completed, rows archived verbatim to
plan_completed under 2026-08-31; [B23]/[B24] unblocked in place
(Frank starts them). Lanes today: b22repin, b22reports (sonnet),
b22ledger — all merged/landed and torn down; watchdog cron deleted
after this entry. The day so far: one re-pin, one 8/8 window, two
report sets, one ledger, O-11, two plan rows closed.

## 2026-08-31 (EDT, ~16:3x), sixth session (part 5, CLOSE-IN-PLACE)

Frank: "do the end of session routine in case but keep the context
cache active and wait." State at close: master 31c6b3a + this commit,
tree clean; make check 4/72/0 · 185/185 · 59 (verified post-merge
this afternoon). No lanes, no worktrees (b22repin, b22reports,
b22ledger all landed and removed), no monitors; ONE keepalive cron
(created at this close, minimal read-only tick, off-minute marks) so
the session can wait warm — delete it at the true end. Pin 263b013;
store 77 (67 measured / 9 inconclusive-load / 1 inconclusive-spread).
pcrecdev1 released at WINDOW CLOSED ~14:10 and may be running its
~3.6 h battery. Owed/next: pcrec's answers to O-11 asks (i)-(v) as
I-27+ (likely [OPT-5] step 1 or the W1.2/abi-13 pin); [B23]/[B24]
unblocked awaiting Frank; [B11.2]; KB-2/KB-4/KB-5. wake.md rewritten
from scratch.

The day, in one paragraph: the sixth session ran the whole [B22] arc
end to end in one day — wake and four inbox acks (the pin moving
fa01910 → 263b013 under Frank's lifted hold); the re-pin lane
(declined-nullable + size-cap-retry by value, the third registry
archive, reporter v10, year4 closed as OUR shim's ELF page); the 8/8
window under the .hold handshake (the v1.4 spread rule's first
production firing, re-measured clean); the reports (the first
cross-pin render, KB-5, the R8 Δ column's first firing); the 591-line
ledger (ten points 10/10; NO KNEE — I-26 confirmed to two decimals;
grp≡cls); O-11 with five asks and W1.2 unblocked. Three lanes, zero
lost cells, two plan rows closed.

## 2026-09-01 (EDT, ~00:3x), sixth session (part 6) — [B25] COMPLETE: the [OPT-5] STEP 1 acceptance, measured and ACCEPTED the same day the fix shipped

The whole arc ran 20:45-00:30: I-27 (pin a7e0bdf, abi 13 — pcrec built
our rank-1 candidate the same day O-11 named it) and I-28 (Frank's
proceed) acked; lane b25repin (77 min: RX_DFA_SCAN_EDGE by value on
every stamp case, the -fno-scan-edge deny row as the warn-capture
positive witness, registries 69/23 / 50 / 45, shim floor stays 10 with
the rx_info byte-identity proof, the counted ladder's emitted source
FLAT at compile time, 187/187) — its landing taken over by the manager
after the second lost-notification stall of the day; the acceptance
window 21:46-23:15 (4/4 attempt-1, no spread); lane b25reports (the
cross-pin acceptance report — and a flagged "8192 inversion");
lane b25ledger, which ACCEPTED STEP 1 on both axes at all nine rungs
(letters 3.65-6.05 → 1.76-2.00, the 64/128 rungs BETTER than
predicted; digits 0.596-0.604 with the entry cost systematic at
x1.04-1.06 inside I-27's 1.08 bound) and REFUTED the 8192 flag as a
vs-best/cross-subject mis-reading — the correction and a reader's
caveat are committed prose now (bca42b2). Unpredicted finds: the
search band moved x1.69-2.24; the whole-form ladder did NOT collapse
(edge=none — both surviving warns live there, ask iii); a small
regression family at the entry cost's face (year4/dotted4 at/above
the stated x1.08, ask ii); the first pre-flight reading outside the
old quiet band (5.21%, limit 10%, record stands — band now 0.4-5.21%
n=13). O-12 sent (4d7dc4f, five asks incl. the two-pass charter — the
9-rung surface held stable and discriminated exactly as designed).
KB-6 filed (no reporter clause for dfa_scan_edge). [B25] archived.
NEXT in I-28's cleared order: [B23] (needs the box idle — pcrecdev1's
validation lanes run tonight), [B24], [B11.2].

## 2026-09-01 (EDT, ~04:2x), sixth session (part 7) — [B23] COMPLETE: the instrument proven, both directions

Lane b23control (~50 min incl. the change-request arm): the v1.4 spread
rule's positive control, D35-archived with every prediction written
BEFORE its run. Arm (a): a 64 MiB-copy competitor on CPU 5 for two
passes of the pre-named group (email x pcre2-interp, factored/
short-subject-search, n=77) — FLAGGED, d=77/77 vs threshold 26,
inconclusive-spread, exit 4; the §3.6 timeline located the competitor
independently (sibling 55.69% on the target item). Negative control
clean. Arm (b), the designed MISS: the same competitor over all five
passes — d=4/77, measured, exit 0, the ranked number ~1.77x WRONG and
stamped measured, only the timeline showing it (sibling 99.62%). Two
findings: blind band 1 is REAL at SMT-execution magnitudes (a pure
busy-loop sibling slows the cell ~1.45x < k=1.5 — unflagged; the
demonstration needed the memory-bandwidth shape), and the fast clause
caught 7 rows the slow-pair clause missed — the two clauses closing on
one disturbance from both sides. gate_shape_v14.md §9 Q3 stamped
MEASURED with the pointer. The lane's design deviation (event-scoped
competitor window off the run's own stderr, PID-killed at the next
group's line) was stated in the archive before running — the right
call, avoiding both boundary artifacts. Fourth dropped background
notification of the session (the lane's waiter) — nudged, recovered.
[B23] archived. HELD BEFORE [B24]: cleared by I-28 and the box is
free, but Frank signalled budget-consciousness at pcrecdev1's close —
[B24] (a full clang-variant build + window) waits for his morning go;
the wake queue says so.

## 2026-09-01 (EDT, ~15:5x), seventh session (part 1) — I-29: Frank's full-suite directive; three build lanes opened

Woke to inbox I-29 (534c8e1, pcrecdev1 ~15:0x): Frank's rulings on all
five O-12 asks — (i) recorded; (ii) DEFERRED TO A MEASUREMENT we build
(a low-rung ladder extension + the year4/dotted4-shaped short-run
family); (iii) the whole-form scan edge is STEP 3 territory, the two
size warns stay; (iv) the TWO-PASS fix CHARTERED ("no downside") — the
9-rung surface is its acceptance instrument, match-regime cells owed;
(v) bundled with (ii) plus a census of the hybrid-gained-edge cells.
State: cc/o42 merged to pcrec main (abi 14; the battery caught a real
tier-1 miscompile en route, fixed), w12 merges tonight (abi 15), THE
FINAL PIN comes as I-30 late evening; Frank's directive (a usage
windfall): build the full suite today, run it tonight. pcrecdev1
answered my footprint message within minutes: abi 14 adds exactly one
shim-visible thing (the eighth RX_ENGINE_SEL value
`declined-nullable-default`, no _LANG pair, engine-route order 2), cc
adds no stamp, pcrec has NO clang selector (we invoke clang on the
emitted C ourselves), abi 15 appends `name`/`nentries` to rx_info; only
its full test stages are load-marginal and it will ping START/DONE.

Acked I-29 at 2349432: [B24] STARTED (lane b24cc — per-config `cc`,
three `-clang` configs, our compile of the emitted C, the a7e0bdf
clang refusals read as findings), [B26] NEW (the re-pin absorbing abi
14+15, the overnight full suite in priority order, morning reports/
ledger/O-13), [B27] NEW (bounded@0.3: match-regime cells for STEP 2,
cls-upto-4/8/16/32 + the short-run family, the ask-(v) census; lane
b27bounded), [B11.2] expanded (wide alternations, blinded; lane
b112alt), [B28] (KB-5/KB-6/KB-4 — after the adapter lanes land),
[B29] optional. Window budget from the ledgers: email ~8 min/cell,
loglines ~10, bounded ~22 → ~10 h for the whole suite incl. the new
set and clang configs; order bounded@0.2 (cls AFTER) → loglines →
email → bounded@0.3 → the new set → clang cells. Stall watchdog cron
up (10 min); no keepalive (the session is active).

## 2026-09-01 (EDT, ~16:3x), seventh session (part 2) — [B24] and [B27] merged; the two-pass residual confirmed on one pin, and a bigger effect behind it

[B24] (lane b24cc, 3 commits, ec838a6): the cc axis is a per-config
`cc` in configs.toml — absent is byte-identical to before (proven
against a committed production record), present is an identity
(`cc-clang` in the derived testee_id, the compiler + version line in
build_flags, a contradicting $CC refused by name); three `-clang`
configs; the driver stays on $CC so a pair differs in exactly one
variable; 18 named checks (205/205). The finding: at a7e0bdf clang
21.1.8 refuses 50 of 264 (pattern × mode × form) cells with ONE cause
(a frameless VM artifact's indirect goto into a function with no
&&label — the [CC-CLANG] step-1 fix at abi 14), 0 of 264 at the
ae3e6ca scratch build. So the clang cells are measured only after the
re-pin. run_suite.sh (fe41292) chains several sets through
run_window.sh in priority order, rehearsed dry over two sets.

[B27] (lane b27bounded, b61ed9a): bounded@0.3 — the STEP 2 match
instrument is letters runs 4..1024 B as MATCH-ONLY subjects (the
short manifest, `short_search_max_bytes` 512 → 258; no regime, no
schema change; caveat 2's arithmetic re-done at Σ/median ≈ 50), the
low rungs cls-upto-4/8/16/32, the short-run digit family
dig-exact/dig-upto at 2..32, 19 subjects, 0.2 byte-identical;
predictions P1-P4 committed before any run. The ask-(v) census: four
cells, two artifacts (nest2-64 / nest3-16 whole-subject × the auto
testees), match only; the ledger's "trade" was between two DIFFERENT
artifacts; the edge costs +6..12 ns fixed per matching call. Then P4
fired on a scratch smoke (inconclusive-load, a flag): the ladder's
whole-subject artifacts split by match_form (64..1024 unwrapped;
2048/4096/8192 + atleast-4096 search-filter; 16384+ VM), and one rung
apart on the same subject cls-upto-2048/1024 is ×2.0 on matching runs
(the reverse pass — the acceptance ledger's residual, confirmed
without a second pin) and ×37 on a FAILING 1024 B run: the
search-filter entry scans the whole subject for candidate starts
before rejecting, O(subject) where [ENG-ABS] promises O(divergence).
Relayed to pcrecdev1 live (its STEP 2 design note is being written
today) with two asks: is search-filter on those four artifacts
deliberate, and does STEP 2 remove the failing-call scan too. I-29
(iv)'s frame is restated: the unwrapped rungs will not move. Lane
b28report (KB-5/KB-6) opened in the freed slot; b112alt on its second
make check.

## 2026-09-01 (EDT, ~17:1x), seventh session (part 3) — build-out complete: four lanes merged, master green 4/72/0 · 217/217 · 61; waiting for I-30

[B11.2] (lane b112alt, blinded, 8a2a4b7): bench/altwide@0.1 — 20
patterns on width × structure × order × wrapper, the oracle's own
compiled-size ceiling capping the 3-12 B ladder at 2048 (the short-
word pool carries 4096), srt-512 as the falsifiable ALTCLS pair; a
BLOCKER found and fixed in record.py — four rungs exceed the schema's
8192 B free_text cap on canonical_text, now OMITTED above the cap
(never truncated) with a gate reading the cap from the schema; make
check ~5 → ~11-15 min (1600 interpreter expectations — a future
wave's cache). [B28] (lane b28report, sonnet): KB-5's --testee
roster filter and KB-6's edge= clause, reporter v11, 61 tests, every
report regenerated, and one drift caught — an open-ended --since
query on the 2026-08-30 loglines file had silently grown two next-day
263b013 records; pinned by roster. Master 2a8051f + this merge: the
final tree's make check 4/72/0 · 217/217 (11 min under the peer's
load). Lessons today: wait for a lane's FINAL message before
removing its worktree (b27bounded's confirming check died under it);
a `pgrep -f` on a command string matches the shell issuing it —
filter by PID and pattern; a lane told to "wait for a background
task" goes idle and is lost — briefs must say "block in the
foreground with a bounded poll". The night: tonight's suite is
bounded(0.3) → loglines → email → altwide → bounded:clang →
loglines:clang via scripts/run_suite.sh (rehearsed dry), ~8-10 h;
the cls-* AFTER reads cell-against-cell on 0.3's byte-identical cls
rungs (the harness takes a set's version from its sidecar only). The
re-pin brief is drafted; launched the minute I-30 lands.

## 2026-09-01 (EDT, ~20:1x), seventh session (part 4) — re-pinned to 1989c62 (abi 15); three findings before the window

Lane b26repin (opus, ~50 min, one commit 5862a0a): pin 1989c62, the
eighth RX_ENGINE_SEL value with both directions of the §6.3 iff, rx_info
name/nentries as provenance (floor 10 → 15, a floor-1 sabotage arm),
registries 70/23 · 50 · 45, the clang refusal set EMPTY at the pin,
227/227 · 62. Its census (462 cells per pin, archived) says NO bench
artifact stamps `declined-nullable-default`: the cls-* hybrids I-29
item 4 expected are DFA-engine under auto, so [OPT-4.2] has no bench
customer tonight — the witness is hand-chosen `(?=abc)x*` (−27.8 % B)
vs `(?=abc)x+`. The [B22] `nullable collapsed language` witness is now
unreachable (o42 declines earlier; structural) — the force control is
retired for an inert-flag check, an ask for pcrec. The size books
moved UP +202/+105 B flat (abi 15's rx_info fields); the "519 B fix
moves emit_bytes" line in I-29 was wrong by the measure's definition.
altwide's ci-512 is refused by the 1,000,000 B emit cap at both pins —
the set's first compile-axis refusal, a did-not-compile row with cost
tonight. Earlier this evening: O-13 sent on pcrecdev1's D78 request
(the durable copy of the scratch-tier readings, with the withdrawal
rule); KB-7/[B30] filed on Frank's reading of the 8192-char free_text
cap ("seems arbitrary") — a ruling row. pcrecdev1's battery is in
san/lint/mech; WINDOW OPEN + I-30 projected 21:30-22:00.

## 2026-09-01 (EDT, ~22:5x), seventh session (part 5) — WINDOW OPEN: the full-suite night launched at 1989c62

I-30 landed (995ab71): the final pin is 1989c62, battery-proven; our
three re-pin findings are recorded on pcrec's side (item 4 withdrawn,
the two o42 witness shapes named, `nullable collapsed language`
retired in tuning.md §2.17 with a re-opening condition); the r49
panel kept STEP 2's start-pinned mechanism and CLOSED our failing-call
ask with a soundness witness — the unwrapped entry cannot be bolted
onto the wrapped machine (`a*b` on "aab"), so [OPT-VEDGE] owns those
rungs. Pre-flight: tree clean, no peer process by cwd, load 0.50,
`quiet` verdict quiet. Launched `scripts/run_suite.sh` under setsid in
the rehearsed order: bounded@0.3 × 6, loglines × 6, email × 6, altwide
× 6, then the three clang configs on bounded and loglines; trials 5,
NOTE names the pin and I-30. Budget ~8-10 h → done by ~07:00-09:00.
Monitors: the suite log's per-set rc lines + SUITE_RUN_COMPLETE, each
window log's WINDOW_RUN_COMPLETE, and a 40-min cron reading both (our
own background waiters die at the 10-min cap). Both sessions restarted
at 20:26 tonight; nothing was lost on either side (the peer's battery
was setsid-detached, our state was all committed). Earlier this
evening: the re-pin (part 4), O-13, KB-7/[B30].

## 2026-09-02 (EDT, ~09:1x), seventh session (part 6) — the full-suite night RAN: 27 of 29 cells measured at attempt 1; two clang cells lost to the per-cell cap, re-running by hand

SUITE_RUN_COMPLETE at 09:04 (launched 22:45, 10 h 19 min): bounded@0.3
× 6 (256 min), loglines × 6 (51), email × 6 (43), altwide × 6 (91),
bounded × 3 clang (150), loglines × 3 clang (25) — every cell that
finished did so on attempt 1, no gate refusal, no spread (index: 109
records, measured 99). TWO cells were LOST: bounded@0.3 ×
pcrec-nocaps-clang and × pcrec-vm-clang, both killed at exactly 50:00
by run_window.sh's 3000 s per-cell cap (rc 124, no record; the
nocaps cell was on its second-to-last pattern). The suite summary
could not show it (a set's rc is the index's) — the per-attempt rc
line could. Cap raised to 5400 (d621079) with the reason in the
script; both cells re-running by hand under setsid (cap 5400, the
same NOTE + the reason), window still OPEN, expected done ~10:50; the
peer holds until my explicit CLOSED (its new session, after the 20:26
restart, confirmed). Cell-time facts for the books: bounded@0.3
pcre2-interp 42 min, pcre2-jit 30, pcrec-auto 45, nocaps 42, vm 48,
vm-in 48, auto-clang 49; altwide pcre2-interp 42 (est. 18), jit 30,
auto 5, nocaps 5, vm 4 (most rungs refuse under the forced VM — a
morning reading), vm-in 4; loglines ~8.5/cell; email ~7/cell.

## 2026-09-02 (EDT, ~11:0x), seventh session (part 7) — WINDOW CLOSED: 29/29 measured; the reports lane opens

The hand re-run finished 10:48 (nocaps-clang 49 min, vm-clang 53 min,
both attempt 1) — so the full suite at 1989c62 is 29 of 29 cells
`measured`, all first attempt, no spread, no gate refusal; store 111
records (101 measured / 9 inconclusive-load / 1 inconclusive-spread,
the last two counts unchanged from before the night). WINDOW CLOSED
sent to pcrecdev1's new session (it holds until CLOSED, not 09:00).
Lane b26reports launched (six report groups + the cell-against-cell
bounded cls table under docs/dev/measurements/); b26ledger follows on
its delivery; O-14 from the ledger.

## 2026-09-02 (EDT, ~14:1x), seventh session (part 8) — [B26] COMPLETE: the night read, O-14 sent

Lanes b26reports (opus; six report groups + the 7,670-cell 0.2/0.3
cross-version table; its re-render invariant caught THREE
-after-96e44c2 groups drifting through open --since queries — a
--testee roster cannot bound time, KB-8; its "biggest flag", the
forced-VM ×9, was confirmed by pcrec as I-31 within the hour) and
b26ledger (opus; the 1,136-line ledger, twelve sections, everything
cited) landed; O-14 written from the ledger. The night's verdicts: O-13
confirmed in every section and withdrawn nowhere (the STEP 2 BEFORE:
×1.986-2.036 matching, ×37.1 failing, VM control 0.999; auto picks the
slower engine on that axis from 1024 up — a new [SEL-1] question); the
auto route FLAT across the pin (0/832 artifacts stamp the new
engine-route value); the forced-VM route ×9 on failing scans on
exactly the resume_frames == 1 population (−402/+105/+202 B by frame
count and DFA presence — the re-pin census's "flat" sentence, quoted in
part 4 above and in the plan/root status, was a SUMMARY ERROR: its own
rows split three ways; corrected where quoted, the D35 file untouched),
gcc-only; the scan edge a spelling-and-form decision at k = 2-4 with no
measured win and a measured cost on three loglines patterns; the cc
axis regime-shaped (clang wins short DFA match cells, loses
collapsed-prefilter hybrids, level-context ×1.69); altwide 12/20
refused at pcrec's two caps with P2 emphatic (auto FLAT over w-8..256
while every other testee rises 74-90×) → [B31]. Follow-ups [B32]; KB-9.
[B26] archived. Lessons: a lane's "final" can lag its delivery by an
hour while it keeps improving the work — merge the delivered head,
keep the worktree, and say so; two hands on the same fix (mine and the
lane's on the 96e44c2 files) was a near-collision resolved by taking the
lane's superset; the suite summary's per-set rc hides a killed cell —
grep the per-attempt rc lines after every window.

## 2026-09-02 (EDT, ~15:3x), eighth session (part 1) — wake; [B30] ruled, [B31] cleared (limits file OUT of the set); I-34 acked; three lanes opened

Woke at 58c7cf7 (clean, green from the seventh session's last full
run; the I-32/I-33 acks of 2026-09-02 ~14:4x went into plan.md at
3389a3c/58c7cf7 without a journal line — this is it). No new inbox
item at wake; pcrec main 39 commits past our pin (plan/journal
traffic; STEP 2 lane opt5i and [OPT-VMFL] step 0 building; [OPT-NEG]
and [FEAT-VAR] filed there from Frank's ideas). Frank's rulings this
session: [B30] "agree" — schema v1.5 raises `free_text` to a 1 MiB
hygiene bound, the omission fallback stays, the reason is written down
(65e5a5d); [B31] CLEARED, and "I agree with your limits file proposal"
— NO pcrec-oracled `pcrec_limits.tsv` in bench/altwide: the sets stay
engine-neutral (R-BENCH-4) and pcrec's first refusing widths live in
the reports and ledgers where they already are (6ca3024). I-34 landed
on master from pcrecdev1 mid-session (742c6bc: the ×9 population
reading exact on our four sets, 0 under-counts; the direct-branch
dispatcher not a win, D77 unmet; `RX_VM_FRAMELESS` drafted) — acked on
[B32] (g) as the future covariate/column that replaces the grep
(3e88435). Three lanes, disjoint footprints, worktrees off 742c6bc:
b31alt (opus, BLINDED as 0.1's — bench/altwide@0.2: the dense
w-96/128/192/384 ladder, the structure arms twinned at 256 incl.
srt-256 as the compilable ALTCLS pair, predictions before any run
incl. the wide rungs under the raise, byte-identical 0.1); b31cap
(opus — the raised-cap config axis in testees/pcrec: optional
`max_emit_bytes` / `max_emit_code_bytes` keys → pcrec's raise-only
flags, an identity in testee_id/build_flags composed with `cc`, the
BOUND measured by compiling all 20 altwide@0.1 patterns under a probe
raise at 1989c62 and archived under docs/dev/measurements/, the w-512
VM control, `pcrec-auto-bigcap` / `pcrec-vm-bigcap`); b30cap (sonnet
— schema v1.5, the synthetic >1 MiB "above" witness, KB-7 closed).
Footprint sent to pcrecdev1 (build lanes only, no window); stall
watchdog cron up (10 min). Nothing measured today; altwide@0.2's
window is a later session's, after [B31] merges and the cell-time
estimate is checked against the 5400 s cap.

## 2026-09-02 (EDT, ~16:1x), eighth session (part 2) — three lanes merged in ninety minutes; master GREEN 4/72/0 · 243/243 · 62; [B30] COMPLETE; [B31] built, unmeasured

b31alt (opus, blinded; 103682e + one manager commit, merged 0149ac7):
altwide@0.2 = 0.1 byte-identical (verified independently: every 0.1
.rx untouched, the manifest a two-row append, all 1,600 expectation
rows inside 2,772) + w-96/128/192/384, the seven structure arms at
256 (srt-256 = the ALTCLS order pair as two compilable artifacts),
s-256/s-512 (the byte-vs-count probe: s-512 predicted at 414-547 KB of
VM code against the 500,000 B cap — P13, a knife edge), two carriers;
P9-P18 before any run; check-harness 449 → 501 s. The manager's one
correction on merge: the lane charged every refusal five trials per
form, but the adapter returns on the first refusing trial (harness
forces the trial count to 1 on a non-compiled outcome) — the plain
auto budget now rests on 0.1's measured 30-min cell: ~35-40 min.
b31cap (opus; ba3cf17, merged b5634f7): `max_emit_bytes` /
`max_emit_code_bytes` per config → pcrec's raise-only flags riding in
`flags`, the values in config_extra composed AFTER cc
(`compose_config_extra`, append-only), a below-default value refused by
name against the archived list_limits.tsv (no second copy of a pcrec
constant); pcrec-auto-bigcap / pcrec-vm-bigcap at 8,388,608 B, the bound
from an 80-compile census of altwide@0.1 under a 100 MB probe (80/80
compiled; max s-4096 whole-subject VM 3,741,164 B; at the defaults 50/80
refuse — 26 auto at the total cap costing 0.07-40.23 s each, 24 VM at
the code cap costing <0.1 s; the size port byte-exact with pcrec on all
61 advisory rows; docs/dev/measurements/2026-09-02-altwide-raised-cap-
sizes.txt); the raise is an AXIS (it moves the size-term abort bound
too); 13 checks; the bigcap pair belongs to altwide's window alone
($TESTEES_altwide). Its tail found KB-10 (`quick --vs` errors on a
refused arm) and the stale roster table ([B32] (h)/(i); the table
refreshed by the manager, 3acf800). b30cap (sonnet; cf240b7, merged
848a442): schema v1.5 — free_text 8192 → 1,048,576, a MINOR bump by the
plain §4 rule (no version branching, nothing re-stamped, no new example
per the 1.3 precedent), the omission fallback re-witnessed on a
synthetic cap+1 pattern, altwide's patterns now carry canonical_text,
the note/status guards grow to the live cap, one collateral fix (a
hard-coded "1.4" in check_smoke_block_na_trials), KB-7 closed; the two
standalone `diagnostic` bounds left at 8192 (Frank named free_text
only). Merged tree: make check 4/72/0 · 243/243 · 62 in 15 min under
the census's load (build/check-eighth-master.log). [B30] archived.
STILL RUNNING: b31cap's gcc census on the four largest raised artifacts
(w-512 vm-bigcap both forms = 12.2 s of gcc → ~24 min projected for the
whole vm-bigcap compile term, the optimistic end of altwide's 12-91).
Lessons: a blinded author cannot know the harness's refusal-trial rule
— hand it over in the brief next time; a lane comparing one rung to a
thirteen-rung total called a good estimate wrong by "two to three
orders" — like with like; two lanes idled on monitors again despite the
brief (b30cap, b31cap) — the nudge works within a minute, but the
brief's wording still does not.

## 2026-09-02 (EDT, ~16:3x), eighth session (part 3) — the gcc census lands; the vm-bigcap cell does not fit; session paused

b31cap's section 2 (427ea4d, merged d37b906): five cells through the
adapter's own compile path, both forms, one trial, all under gnutimeout
600, none timed out. The two routes have OPPOSITE cost structures — a
forced-VM artifact is straight-line C pcrec writes in 0.01-0.06 s and
gcc pays for (w-512 5.1/7.0 s, w-2048 61.7/91.8, s-4096 183/334, per
form), SUPERLINEAR in emitted CODE bytes (exponent ~1.8 to w-2048 and
steeper beyond; both of the NOTES' linear-in-pattern-bytes models
refuted 1.5-1.8× on the third cell, predicted before measured); an
auto-route artifact is a table the subset construction pays for (11-37
s) and gcc barely notices (<1 s). Per-rung projection at five trials:
pcrec-vm-bigcap 4,499 s = 75 min of compile alone (OVER the 5400 s cap
before matching; w-2048 + s-4096 are 75 % of it), pcrec-auto-bigcap
705 s = 12 min. s-512 COMPILES at the default caps (474,312 code B /
843,165 total) — P13's bracket confirmed, twelve rungs need the raise.
Folded into NOTES.md (a measured-after paragraph) and plan.md [B31]
with the window options (A: a per-cell cap variable, recommended; B:
--trials 3; C: a run --patterns filter) — Frank's ruling owed; the
window not run. wake.md rewritten; watchdog deleted; worktrees kept
for the next session to remove. Master 9b45f31, clean.

## 2026-09-02 (EDT, ~18:1x), eighth session (part 4) — Frank: build by day, windows at night; [B32] built as two lanes and merged; master GREEN 4/72/0 · 253/253 · 66+7; tonight's window plumbed

Frank (~16:3x): "I don't want to block development on bench runs during
the day … having everything stop for four hours isn't the best use of
time" — windows at night, lanes by day, rulings inline (saved as a
feedback memory). [B32] opened as two disjoint lanes off dc277df.
b32adp (opus; six commits, bca4f42, merged b9cf668): (a)
`pcrec-auto-noedge` — `-fno-scan-edge` riding in `flags`, the axis
derived from effective flags, the `noedge` token LAST in config_extra
(→ `pcrec_1989c62_auto-caps-simdna_noedge`), `runtime_options` now
reads single-dash `-f...` tokens as flags (absent configs proven
byte-identical against a frozen renderer); (f) `scan_edges` (rx_search
+ a hybrid's rx_prefilter) / `scan_edges_match` (rx_match) counted by
the emitter's `[OPT-5] SCAN EDGE:` marker, a marker anywhere else
RAISES; iso-ts 8/4 = I-33's numbers, http-5xx 1/1, ipv6 1/0, floor 0/0,
forced-VM and denied 0; agreed with an independent reader over 338
compiles (docs/dev/measurements/2026-09-02-scan-edge-attribution-
census.txt); (j) `CELL_CAP` (default 5400 with its reason; printed on
every attempt line; rc=124 named as the cap) + `CELL_CAP_<set>[_<label>]`
through a subshell in run_suite.sh; (e) the cell-length table in
scripts/CLAUDE.md; ten checks. A scratch `quick` on a loaded box put
noedge ×1.70 FASTER than pcrec-auto on iso-ts search (inconclusive-load,
a signal, not a number). b32rep (sonnet; 3b313c5, merged 9f4b5d4):
reporter v12 — KB-8's filtered count, KB-9's `(clang cc)` suffix, the
worst-other-core header line, the `edges=` clause, KB-10's `refused`
arm (`_split_quick_cells`, test_quick.py); 66 reports regenerated in
one process (header lines only; the two cc groups' suffix); tests 62 →
66 + 7; KB-8/9/10 closed. Merged tree: 4/72/0 · 253/253 · 66+7 in ~15
min. [B32] has only (g) left (the frameless column at abi 16).
TONIGHT'S WINDOW is plumbed and on the plan row (option A): SUITE
"altwide altwide:bigcap loglines:noedge", the six pinned on altwide@0.2,
the bigcap pair under CELL_CAP_altwide_bigcap=14400, pcrec-auto +
pcrec-auto-noedge on loglines in the same window (the lane's point: one
window apart, iso-ts the row to read first); ~5-6 h; Frank's go owed.
Lessons: "you will not be woken" in the brief did NOT stop b32rep
idling on its make check — the nudge did, within a minute; the brief
should give the exact foreground command (`gnutimeout N tail --pid=P -f
/dev/null`) rather than a rule. A lane's report can name a stale
number in the root CLAUDE.md (221 was long fixed) — verify before
editing. A merged lane's worktree can hold an uncommitted edit; look
before `remove --force`.

## 2026-09-02 (EDT, ~23:5x), eighth session (part 5) — the hold, and WINDOW OPEN at 23:58

Inbox I-35/I-36/I-37 (~16:3x-18:3x) acked at de98e98: the clock split
recorded on pcrec's side; Frank's cc ruling → [B33] NEW (clang as a
compile-only gate on every pin with the refusal set diffed against
gcc's, the timed clang arms out of the nightly, periodic re-runs on the
named triggers); [CC-DIFF] step 0 — clang's wins are two reproducible
transformations (always_inline on the frameless entry chain 0.611, the
uniform-table fold 0.589), one ledger cell (floor/match/auto 0.432) did
not reproduce → marked PROVISIONAL in ledger §5.4, a re-run owed. Frank
(~18:5x): "Yes to both" — tonight's window AND the re-run pass.
pcrecdev1's STEP 2 battery (STAGE START ~18:3x; STEP 2 merged on pcrec
main, abi 16 with RX_VM_FRAMELESS) held the box; a keepalive cron
(11,51) carried the hold; one status question at 21:20 after an hour
of low load (it was san's single-threaded phase — a [TT-12] finding on
their side, not idleness). STAGE DONE 23:56 (strict/san/lint GREEN,
test rc=2 with three diagnosed reds fixed for a morning re-run, mech
218 rows 0 anomalies + one unexpected row under reading). Quiet gate
23:58: load1 0.13, max core 6 %, VERDICT quiet. LAUNCHED under setsid
at 1989c62: SUITE "altwide altwide:bigcap loglines:noedge
bounded:clangrerun" (six pinned on altwide@0.2; the bigcap pair under
CELL_CAP 14400; pcrec-auto + pcrec-auto-noedge on loglines; bounded@0.3
× pcrec-auto-clang last); suite log
build/windows/suite_20260903T035832Z.log. WINDOW OPEN sent; expected
finish ~06:30-07:00; a 30-min progress cron (23,53) reads the
per-attempt rc lines. Nothing of ours needs the abi-16 pin tonight;
the pin comes with pcrecdev1's morning WINDOW OPEN after their re-run.

## 2026-09-03 (EDT, ~06:4x), eighth session (part 6) — THE WINDOW RAN: 11/11 cells measured at attempt 1; store 122; the reading opens

Suite 23:58 → 06:16 (6 h 18 min): altwide@0.2 × six pinned 166 min
(interp 62, jit 52, auto 9, nocaps 9, vm 18, vm-in 17 — the plain auto
cell is 9 min, NOT the 35-40 budgeted from 0.1's 30-min cell: the
census's ~2 min of refusals per form pair was right and 0.1's figure
needs explaining), the bigcap pass 145 min under CELL_CAP 14400
(auto-bigcap 24, vm-bigcap 122 — the census projected 12 and 75 of
compile; both inside their caps), loglines × {auto, noedge} 16 min,
bounded@0.3 × pcrec-auto-clang 48 min (the I-37 re-run). No gate
refusal, no spread, no cap kill; every per-attempt rc line rc=0.
WINDOW CLOSED 06:26 (with a count correction: 11 cells, not the 13 I
first wrote). Store committed a7a0d26 (122: 112 measured / 9
inconclusive-load / 1 inconclusive-spread; the first schema-1.5
records; the first records whose testee_id carries `_emitcap-…`,
`_noedge`). Lane b31reports (opus) opened for the four report groups
(altwide first sample vs P9-P18; the bigcap pair vs their siblings and
the census; the noedge pair with the edges= covariate; the clang
re-run with the I-37 cell's verdict); the ledger and O-15 follow. The
b32 worktrees removed (checked clean first).

## 2026-09-03 (EDT, ~08:5x), eighth session (part 7) — the window READ (lane b31reports: four report groups + the ledger), O-15 sent, [B31] COMPLETE; I-38: the STEP 2 pin 288d505 (abi 16), lane b34repin re-pinning

b31reports (opus; reports 471ab02, ledger b7dfd1a; merged dffccd1 /
230ab1e): the 969-line ledger 2026-09-03-altwide-0.2-noedge-ccrerun-
1989c62.md. Verdicts: the refusal boundary is 256 < w ≤ 384 on BOTH
routes (w-384: 1,431,536 B source, 43 % over; 508,517 B code, 1.7 %
over); P9 confirmed to 256 (auto flat 2.2-3.5 ms; interp slope 1.0, JIT
1.39), P11 confirmed (vm/jit 6.5-9.6, no crossing), P12 CONFIRMED —
srt-256 byte-identical on the DFA and ×8.87 faster on the VM (11.5 %
smaller; ×20.1 at 512 under the raise, the only cells where a pcrec VM
beats the JIT), P13 half (s-512 compiles at 94.9 % of the code cap),
P10 untestable at the defaults but READ under the raise (RX_DFA_TABLE
premultiplied → mixed at 512 → indexed at 1024; match=search-filter at
1024 — two stamps explain the two steps, neither is width; the flat
line survives at ×627 the JIT at w-2048), P15 refuted (pfx3-256 →
memchr), P17 half (ci-256 stamps edge=bitmap). The noedge pair: every
edge-taking pattern faster without the edge, the zero-edge ones flat;
the PINNED figure on iso-ts is ×1.089 — the scratch ×1.70 did not
survive (a lesson: an inconclusive-load quick on a loaded box is not a
number, as b32adp itself said). The I-37 cell: 0.432 reproduces to
three decimals on the clang arm (217.6 → 217.5 ns); the gcc half stays
measured once. One misread caught: "0.1's auto cell was 30 min" was the
JIT's cell (auto was 4.8; 0.2's is 8.8) — corrected in NOTES.md and the
2026-09-02 ledger with dated notes; the 6× planning rule withdrawn. O-15
written from §1-§9 (six candidates: [OPT-EDGE] on ×1.09; the branch-
order lever; the two caps; [LIM-2] priced ×190; the \b wrapper's ×1.26;
pfx3-256; five asks, ALTCLS stamps first). [B31] COMPLETE and archived;
[B35] the follow-ups. Meanwhile I-38 (07:5x): STEP 2 battery-proven at
pin 288d505 (abi 16: RX_DFA_START, rx_info.search_form,
-fno-start-pinned bit 22, RX_VM_FRAMELESS) → [B34] started, lane
b34repin (opus) re-pinning by day; the bounded@0.3 AFTER tonight on
Frank's word here (pcrecdev1 relayed his go; a relay is not the user's
approval in this session).

## 2026-09-03 (EDT, ~11:4x), eighth session (part 8) — [B34] re-pinned to 288d505 (abi 16) and merged; three lanes and two API overloads; the ALTCLS read

I-38 (07:5x): STEP 2 battery-proven, pin 288d505. Lane b34repin (opus)
made four WIP commits (pin + registries; shim/driver/adapter reading
RX_DFA_START / search_form / RX_VM_FRAMELESS; the stamps by value with
the size books; the reporter's start=/frameless= clauses) and then died
three times on API 529 overloads; I committed its reporter work and the
doc pin lines. I-39 (08:5x) said the ALTCLS stamps ALREADY EXIST and
our shim never read them — added to the lane's scope, but b34altcls
(opus) died on a 529 before starting; b34altcls2 (sonnet) delivered it
(4ae00fe/335f421): both stamps common to both routes, merges 0 on all
of altwide (P1 holds), factored 11 on w-256 vs 57 on srt-256 with the
DFA artifacts byte-identical except that stamp line — the ×8.87 order
effect's mechanism, read. pcrecdev1 asked for a make-check hold
10:07-10:50, then to 11:30 (three load-comparable test-stage shapes;
K44 retires by measurement, its test stage moves to -j4/PROCS=3); our
lane's check was stopped by PID twice (once it had started a check
"because the box quieted" — the hold is a CLOCK, not a load reading;
`selfcheck.py --help` is NOT a help flag, it runs the whole suite), then
CLOSED; I ran the check myself after DONE (11:10). The first run was
red on two arms of my own [B31]/[B32] design: "every COMMITTED record at
this pin re-derives" is VACUOUS at a fresh re-pin (no 288d505 records
yet) — fixed to render against the previous pin's records with the pin
printed (70efda2). Second run 4/72/0 · 270/270 · 68+7; merged aca987f.
Findings: vm_frameless ≠ resume_frames == 1 (the lookaround witnesses
stamp frameless with a two-frame capacity — I-34's over-count
population, exactly); STEP 2 takes 3,392 B off cls-upto-16384's pinned
artifact; a search-start axis (two rows) is the only registry change.
Lessons: give lanes the exact command for a wait (they idle on
monitors regardless of prose); a hold is a clock; a model pool can be
overloaded while another is fine — switch models rather than retry;
a check that proves a renderer against committed records must say what
it does at a pin with no records.

## 2026-09-03 (EDT, ~12:5x), eighth session (part 9) — Frank's ruling on bundling (one change per pin per night), the cflags axis merged, tonight's four-pass suite fixed

Frank asked whether re-pinning for STEP 2 alone forecloses bundling
other items into the night; the answer he agreed with: the acceptance
stays single-variable (one pcrec change per pin and per night — the
one-variable rule and D77's expectation), re-pins are cheap now (~3 h),
so future pcrec items get their own pins and nights, and the REST of a
night is filled with SAME-PIN cells that confound nothing (saved as a
feedback memory). Tonight at 288d505: bounded × six pinned (the STEP 2
AFTER against ledger 2026-09-02 §10 / I-38's targets), loglines ×
{auto, noedge} (the search band's AFTER + the noedge pair's second
sample), email × auto (continuity), bounded × {auto, auto-clang,
auto-align64} (the both-arms re-run of the 0.432 cell with I-39 (v)'s
layout probe); ~7.3 h, launch at pcrecdev1's end-of-day DONE
(~18:30-19:00, their [CC-DIFF] STEP 1 battery). Lane b35align (sonnet,
5ec667c, merged a111b64) built the COMPILEE-FLAGS axis in 45 min: a
per-config `cflags` list appended to OUR phase-2 $CC argv after
`-shared` (never pcrec's argv, never the driver), the token
`cf-align-functions-64` composed LAST in config_extra, build_flags
naming the flags verbatim, `pcrec-auto-align64`, seven checks (the
twelve pre-[B35] configs untouched incl. every committed record's
build_flags; the flag seen in the REAL gcc argv; the aligned artifact
answered by the oracle; a scratch record carrying the token); make
check 4/72/0 · 277/277 · 68+7. Thirteen pinned pcrec configs. No lanes,
no worktrees; a keepalive cron carries the hold to DONE.

## 2026-09-03 (EDT, ~12:5x), eighth session (part 10) — CLOSE; Frank restarts the session before tonight's launch

Frank: "If you're done, close your session and I'll restart it before
tonight." Closed at master 7fe3649 + this entry: clean, green (4/72/0 ·
277/277 · 68+7), pin 288d505 (abi 16), thirteen pinned pcrec configs,
store 122, schema 1.5, reporter v13. No lanes, worktrees or crons. The
next session's first job is tonight's four-pass suite at pcrecdev1's
end-of-day DONE (~18:30-19:00; the peer has been told the session
restarts before then) — the command is in wake.md verbatim. The
session's arc, for the record: [B30] ruled and done; [B31] built,
measured and read (O-15; I-39 answered it); [B32] built (the frameless
column now real at abi 16); [B34] re-pinned; [B35] (1) built; two
windows' worth of rulings from Frank (build by day / windows at night;
one change per pin per night) saved as memories.

## 2026-09-04 (EDT, ~14:1x), ninth session — THE HOLD: pcrecdev1's DONE rescinded, an evening and a morning of its batteries, I-40..I-43 acked, [B36]/[B37]/[B38] opened, the repo pushed to GitHub; CLOSE without a run

Frank opened the session (2026-09-03 ~17:xx) with "hold; I'll wake you",
then the manager skill with "wait (cache keepalive) until pcrecdev1 gives
the go-ahead, then run". pcrecdev1's I-41 DONE (15:5x, "three hours
early") had arrived first — and Frank RESCINDED it ("wait for the next
one"): the box was in fact busy (load1 12.6 at 18:38, pcrecdev1's isl1
worktree validating). pcrecdev1 then reported Frank had handed pcrec the
box for the evening: three lane branches validated SERIALLY (isl1, edge1,
w13), merged in order, one battery — load1 swung 0.3-30 through the
night; battery_v5 ran 09:25-13:28 (I-43: GREEN at the abi-20 pin
251bb117 — [ENG-ISL] STEP 1 the alternation island abi 18, [OPT-EDGE]
STEP 1 the scan-edge dispatch abi 19, [DD-13b.W1.3] .rxt composition abi
20, on top of [CC-DIFF] STEP 1 abi 17). The box stays pcrecdev1's for four
serial lane timings (lim2 → edge2 → ccd2 → form0) until ~18:00 EDT or
later; its LIVE "box free" line is tonight's go. The 288d505 STEP 2
AFTER never launched this session.

Done, all doc-only: I-40/I-41/I-42 acked (5027bb5) — I-42 is Frank's
charter for the SYNTAX CENSUS, [B36] (registry-seeded via
`--list-syntax`, blinded patterns, ~60-90 × six × three in one night on
the existing instrument, the outlier rule stated before the run, a
ranked list of mechanism QUESTIONS; algorithmic/general first, SIMD
last); I-43 acked (817362e) — O-15's asks (i)-(v) answered and the
island's altwide facts on [B35] (w-256/srt-256 within 2 B: the ×8.87
order effect gone at the source; w-384 compiles on the VM route; ci-*
declined), [B37] NEW = the re-pin to 251bb117 (FOUR abi steps in one pin:
one-change-per-pin cannot hold for the pin, so the AFTER splits by DENY
FLAG inside it — -fno-alt-island / -fno-scan-edge / the [CC-DIFF]
witnesses; Frank rules the shape; after the STEP 2 AFTER is read),
[B38] NEW = the .rxt set exporter under I-43's seven rules (per set; no
config lines; `floor` collides cross-set only). The repo gained its
GitHub remote: origin = fdicostanzo/pcrec-bench, master pushed by Frank
(the push is classifier-blocked from the session; the remote add was
not); master is the default branch; the 20 old lane branches stay local.

Lessons: a peer's DONE is not the go when Frank has said hold — the
peer's own "nothing runs" was wrong within the hour (its next lane
started). The keepalive cron (11,51) held the cache across 20 hours of
ticks at one `uptime` each; the tick's one-line reply format worked.
`git push` is blocked by the auto-mode classifier — ask Frank to run it
with `!`; `git remote add` is fine.

CLOSE ~14:1x: master 817362e + this entry, clean, pushed. No lanes, no
worktrees; the keepalive cron deleted at close. pcrecdev1 told. Frank
restarts before the next bench run; that session's first job is the
288d505 STEP 2 AFTER on pcrecdev1's live line (wake.md).

## 2026-09-04 (EDT, 19:2x-19:4x), tenth session part 1 — I-44 acked (the box is the bench's from NOW; pcrec moves to another machine), the 288d505 STEP 2 AFTER LAUNCHED 19:28

Wake at 19:26: `git log` showed one commit after the ninth session's close —
inbox I-44 (8cfa9c8, 18:4x): pcrecdev1 DONE at the abi-22 pin 334fd10e
(the union chain answer-identical on 24 axes, 22,455/22,455 keys; three
reds were test-infrastructure defects fixed at 8fc1580c), "the box is
YOURS from NOW", and the machine move — pcrec development leaves this box,
so from the next pcrec session the inbox/outbox files are the ONLY channel
and there is no nightly handshake to wait for. Four pcrec rows merged
2026-09-04: [LIM-2] STEP 1 WITHDRAWN on its own census (no src change —
O-15's refusal-timing ask is answered: w-2048 refuses in ~10.8 s unchanged;
11/12 census blocks are our altwide patterns, max shrink 1.5 %), [OPT-EDGE]
STEP 1.1 (abi 21), [CC-DIFF] STEP 2 + [OPT-DIAL] STEP 0 (abi 22:
`--vm-entry-shape`, the `RX_VM_ENTRY_SHAPE` / `RX_VM_PROGRAM_BYTES` stamps
on every VM artifact), [FORM-CHAR]/[OPT-CLSPACK] STEP 0 (docs only). Acked
(5036f39): [B34] carries the launch; [B37] retargeted 251bb117 → 334fd10e
(six abi steps in one pin now; the shim will read the two entry-shape
stamps; the gcc arm of I-37's cell to be run at that pin for (v)); [B35]
notes that pcrec's timings from its new machine are never compared to
ours. Frank's window-shape ruling for [B37] is still open; I-44 says run
it as proposed otherwise.

The launch: quiet gate VERDICT quiet (five samples, load1 0.17-0.24, max
core 2.4-5.2 %), no pcrec process on the box (ListAgents showed the local
pcrecdev1 idle and a Remote Control twin on the other machine; ps showed
only editors and the two claude sessions). WINDOW OPEN sent live to the
local pcrecdev1 (addressed by ref — two sessions carry the name now); it
acknowledged, said nothing of pcrec's will start, and closed. The suite
(wake.md's command verbatim, Frank's go of 2026-09-03 standing) went up
under setsid at 19:27:55 EDT: SUITE = bounded (six pinned) + loglines:after
{auto, noedge} + email:after {auto} + bounded:ccboth {auto, auto-clang,
auto-align64}; PID 3170465; suite log build/windows/suite_20260904T232755Z.log;
~7.3 h, done ~03:00 EDT. A 30-min progress cron (23,53; job 9407fce9) tails
the suite log and greps the per-attempt rc lines; no keepalive is needed
while it runs. Nothing else runs on the box tonight — no builds, no make
check, no lanes.

Morning (the reading, against ledger 2026-09-02 §10 and I-38's targets):
every rc line (124 = a cap kill, named), `python3 -m pcrecbench index`,
the reports with --since 2026-09-04T23:27:00Z, the ledger, O-16 (the
[OPT-5] row closes on it), WINDOW CLOSED written to the outbox (the only
channel from here), then push via Frank (`! git push`).

## 2026-09-05 (EDT, 02:2x-02:5x), tenth session part 2 — THE SUITE COMPLETE: 12/12 measured at attempt 1; two lanes spawned (s2read: reports + ledger; b37repin: the abi-22 re-pin)

The 288d505 STEP 2 AFTER suite ended 02:22:30 EDT: SUITE_RUN_COMPLETE,
bounded rc=0 259 min (interp 46, jit 34, auto 42, nocaps 42, vm 47, vm-in
48), loglines:after rc=0 17 min, email:after rc=0 5 min, bounded:ccboth
rc=0 132 min (auto 40, clang 48, align64 44); every cell attempt 1, no
rc=124/3/4 anywhere; load1 1.00 flat through the night (the twelve
progress ticks at 23,53 saw nothing else on the box). `index`: store 122
→ 134 (124 measured / 9 inconclusive-load / 1 inconclusive-spread — the
old ones). The progress cron deleted. Evening channel traffic while it
ran: I-45 (BD8), I-46 (BD8 amendment: push after every channel commit —
Frank granted the push from the session), I-47 (Frank: [B37] APPROVED as
proposed; the box the bench's, continuous benches at our discretion),
I-48 (pcrec's batteries return by slot request, the handshake inverted —
BD8's second amendment; a provisional 13:00-17:00 slot offered for the
[MACPORT] battery, firm in O-16). Master pushed at each.

02:4x: two lanes up in worktrees — `s2read` (reports for the four
groups + the ledger docs/dev/ledgers/2026-09-05-opt5-step2-after-288d505.md
scored against the 2026-09-02 ledger §10 and I-38; its §8 is O-16's
source) and `b37repin` (the re-pin to 334fd10e / abi 22, Frank's go;
make check is the one heavy job on the box). The manager writes O-16
from the ledger, then WINDOW CLOSED in the outbox.

## 2026-09-05 (EDT, 03:0x-03:4x), tenth session part 3 — THE READING: s2read merged, O-16 sent, [B34] CLOSED, WINDOW CLOSED, the [MACPORT] slot granted

Lane s2read delivered at 03:0x (branch merged ccd3b2b: five report groups
under reports/2026-09-05-*, the ledger
docs/dev/ledgers/2026-09-05-opt5-step2-after-288d505.md, reports/CLAUDE.md
entries; rendered in-process at 535 s of store validation per process,
CLI equivalence proven on the email file). THE FINDING, against pcrec's
own I-38: the match-axis customers did NOT move — cls-upto-2048 ÷
cls-upto-1024 at r-01024 1.986 → 1.987 (target 0.90-1.10); the 15
`pinned` artifacts are every PLAIN form of the ladder, 0 of 39
whole-subject artifacts and 0 of 7 hybrids pin; the whole-subject
customers stamp reverse-pass at +110 B. The plain ladder HALVED on
letters instead, unpredicted (I-38: "search-band unmoved"): ×0.506 at
cls-upto-1024, auto ÷ vm 1.97 → 0.99 from rung 512, auto ÷ jit search
0.672 → 0.409. The forced `vm` arm's failing dispatch moved +0.6 ns
(×1.12 on floor match) with `vm-in` flat; year4 ×1.16 on both VM arms.
The noedge pair reproduced (iso-ts 0.916/0.939); email 0.980-1.001; the
I-37 cell with both arms in one window 0.470 (clang +6.4 % across the
pin, gcc 492-503 on three records) and -falign-functions=64 ×0.941 —
I-39 (v)'s ×1.6 layout hypothesis refuted. Pinned −3,384…−3,393 B (the
re-pin's −3,392 right, I-38's −3,232 short). frameless= ==
resume_frames==1 on 100/100. The [B34] row's own "whole-subject ... stamp
pinned" sentence was pcrec's prediction repeated; the selfcheck rows
always asserted plain (b37repin fixes the pcrec CLAUDE.md line).

O-16 (7eeaaf8, pushed): the reading in seven sections, three asks
((i) why the `(?:BODY)\z` spelling declines the pin and whether the
customers are reachable; (ii) is the ×0.5 the pinned start alone —
scan_edges 2 → 1; (iii) what touches `_match` and not `_in` in abi 16),
I-44..I-48 acked, WINDOW CLOSED 02:22, the [MACPORT] battery slot
GRANTED 13:00-17:00 EDT today (our make check off the box then; the
[B37] AFTER window after their DONE). [B34] COMPLETED and archived;
[B35] (1) closed on the ccboth group. b37repin is at WIP A (pin
334fd10e, registries re-archived) and continues.

## 2026-09-05 (EDT, 03:5x), tenth session part 4 — [B37] MERGED (pin 334fd10e / abi 22, 305/305); its deny-flag AFTER LAUNCHED 03:48 in the gap before pcrec's 13:00 slot

Lane b37repin delivered at 03:4x and MERGED (2199212) after review: the
shim reads RX_DFA_UNIFORM_FOLDS (abi 17), RX_VM_ALT_ISLANDS (abi 18) and
the abi-22 pair RX_VM_ENTRY_SHAPE / RX_VM_PROGRAM_BYTES; abi 19/20/21
stamp nothing (iso-ts keeps 8/4 edges through the dispatch); NO rx_info
field across the six steps so the floor STAYS 16; `pcrec-auto-noisland`
(-fno-alt-island, bit 23) is the fourteenth pinned testee and a FOUR-pair
deny control on foo|bar; registries 72/24 → 74/25 · 50 · 45 → 55; the
altwide ORDER PAIR w-256 == srt-256 BYTE-IDENTICAL on the VM route
(292,043 B each; 288d505: 341,201 vs 302,047); I-43's island/chain ratios
reproduced to three decimals; the VM refusal wall moved to 384 < w ≤ 512
(w-384 compiles as an island, refused again under the denial), the DFA
wall unmoved; the fold witnesses' -O2 objects (cls-upto-4 loses its
.rodata; the numbers are this box's, the mechanism transfers); reporter
v14 (folds=, islands=, shape= (prog: N B)); make check 4/72/0 · 305/305 ·
70+7. O-17 findings noted on the row (no --list-axes row for
--vm-entry-shape; RX_VM_PROGRAM_BYTES can exceed emit_code_bytes; the
-fno-scan-edge warn witness 2,587 B from silence; the island's BYTE win
over the sorted chain is 3 %, so ×8.87's removal is a time claim).
Pushed at d93fdbd. The 13:00-17:00 slot confirmed FIRM to pcrecdev1
(its I-49 tonight names the SHA — at abi 23; our pin is a SHA, untouched).

THE AFTER, launched 03:48 EDT under setsid on a quiet gate (load1 0.13,
max core < 6 %): SUITE="altwide:isl loglines:edge bounded:fold" —
altwide × {auto, noisland, nocaps, vm, vm-in} (the pcre2 arms omitted:
unpinned, and the island question is pcrec-only; the reports use the
2026-09-03 pcre2 records), loglines × {auto, noedge}, bounded × {auto,
vm, auto-clang} (the fold witnesses, the vm-arm dispatch question, the
I-37 gcc arm reading its entry shape); ~3.6 h, done ~07:30, PID 3358631,
suite log build/windows/suite_20260905T074836Z.log; progress cron
(23,53). Read against ledger 2026-09-05 §7 and I-43's predictions
(w-256/srt-256 within 2 B — now 0; the ×8.87 gone at the source;
[OPT-EDGE] iso-ts ×0.9995). WINDOW OPEN sent live.

## 2026-09-05 (EDT, 07:3x), tenth session part 5 — THE [B37] AFTER COMPLETE: 10/10 at attempt 1 (store 144); lane b37read reads it; I-49 acked ([B39] opened)

The deny-flag AFTER at 334fd10e ended 07:22:14 EDT: SUITE_RUN_COMPLETE,
altwide:isl rc=0 57 min (auto 9.5, noisland 9.2, nocaps 8.8, vm 14.7,
vm-in 14.8), loglines:edge rc=0 16 min, bounded:fold rc=0 139 min (auto
45, vm 46, clang 48); every cell attempt 1, load1 ~1.0 throughout;
store 134 → 144 (134 measured), committed 344ebb6 and pushed. Five and
a half hours clear of pcrec's 13:00 slot. While it ran: inbox I-49
(05:3x, pcrecdev1's overnight close) acked (c3e0724) — the slot's
target SHA 37f5ae02 at abi 23; O-16 ask (i) ANSWERED (the whole-subject
customers decline the pinned start BY CONSTRUCTION — precondition (3),
the end-anchored position view; I-38 over-promised against pcrec's own
design texts; our 0/39 · 0/7 census is the correct reading; [OPT-VEDGE]
owns that population), ask (ii) ANSWERED (the ×0.506 is the deleted
reverse machine — [OPT-2] STEP 2 had measured the reverse pass at ~50 %
on matching subjects; the win is real on the plain surface), ask (iii)
OWED as I-50's Linux probe; the --list-syntax seed at 334fd10e (144
rows) landed on pcrec's origin/main for [B36]; [B39] NEW = the abi-23
re-pin (RX_VM_CLS_FOLDS on every VM artifact, -fno-cls-fold as the
control, registry rows moving with utf8 + \x{...}). THE [OPT-5] STEP 2
READING IS CLOSED on our side.

07:3x: lane b37read up (worktrees/b37read): four report groups (the
island pair, the altwide cross-pin ranking vs 1989c62 + the pcre2
arms, the noedge third sample, the bounded fold/dispatch/I-37 group)
+ the ledger docs/dev/ledgers/2026-09-05-b37-denysplit-after-334fd10e.md
scored against ledger 2026-09-05 §7 and I-43/I-44's predictions; its
§7 is O-17's source. Deadline: rendering done by 12:30 EDT. Then O-17,
WINDOW CLOSED, push; pcrec's battery 13:00-17:00; then the evening is
open (Frank's continuous-bench grant) — the next window shape waits on
the reading.

## 2026-09-05 (EDT, 08:1x), tenth session part 6 — THE abi-22 AFTER READ: b37read merged, O-17 sent, [B37] CLOSED, WINDOW CLOSED; the box idle until pcrec's 13:00 slot

Lane b37read delivered 07:55 and MERGED (be45246): five report groups,
the ledger docs/dev/ledgers/2026-09-05-b37-denysplit-after-334fd10e.md.
THE READING: the island pair is a NULL pair on altwide — pcrec-auto
selects the DFA on 34/34 cells, the deny flag moves nothing; the
one-variable island reading is bounded's ctx-* hybrids (match ×0.65-0.68,
throughput ×1.015 slower). The ×8.87 ORDER EFFECT IS GONE on the VM
route (w-256 ÷ srt-256 = 1.0007, both 292,043 B). w-384 and, unpredicted,
pfx3-512 compile on the VM route (wall 384 < w ≤ 512; DFA wall unmoved).
The VM beats libpcre2's JIT on 32/44 altwide cells (3/40 at 1989c62;
w-256 ×0.0082). THE FORCED-VM FLOOR TRIPWIRE FIRED: ×2.0 on both sets
(shape=forward, 236 B — the only forward artifact slower). noedge iso-ts
0.985/0.995 (I-44's prediction met on throughput). The vm dispatch
10.2 → 7.0 on the forward cls rungs with floor match 5.6 kept. The plain
ladder's digits ×0.70; cls-upto-32 letters ×1.14 slower. The I-37 cell
is a DFA artifact — no entry-shape stamp exists on it (gcc 459.6 / clang
217.1 = 0.4725). Hygiene: 0 disagreeing rows of 23,424, a first.
O-17 (seven asks, the four re-pin findings, WINDOW CLOSED) pushed;
[B37] COMPLETED and archived; [B35] gains (6)-(8). No lanes, no crons.
The box is idle until pcrec's 13:00-17:00 slot (SHA 37f5ae02).

## 2026-09-05 (EDT, 14:1x), tenth session part 7 — pcrec's battery on the box (from 11:45, early on Frank's word); I-50 acked; three box-free lanes on Frank's relayed question

Frank (11:2x): keepalive every half hour (now 21,51); hand the box to
pcrecdev1 at once rather than at 13:00 — done; its battery launched 11:45
at 37f5ae02 (battery_v5; then the utf8-owed items and the probe set;
DONE late afternoon). I-50 (11:42) acked (469558a): every O-17 ask
answered from source at our pin — the floor ×2.0 is the rung-free 236 B
program under the new always_inline entry chain (hypothesis; OUR
discriminating cell: `floor` forced-VM at --vm-entry-shape=1/2/3), the
digits ×0.70 is the scan-edge dispatch rewrite, the DFA `_match`
×0.57-0.92 has the uniform-table fold as primary suspect (pcrec's
two-pin probe), the program-bytes stamp counts the VM region WITH
comments; [B35] (9)-(13), the census re-derivation onto [B39].
14:0x: pcrecdev1 relayed Frank's question "what bench work is available
while you're idle" with three box-free tasks; three lanes spawned:
`censusprep` (sonnet: the altwide size census as a pin-parametrized
probe, fires with [B39]), `b36census` (opus: bench/syntax@0.1 from the
334fd10e seed — read from ~/pcrec's origin/main, verbatim with a source
header; seed-agnostic generator; blinded authorship; the outlier rule
before the run; a utf family slot; MERGE WAITS ON FRANK'S CLEAR),
`b39prep` (opus: the abi-23 re-pin prepared without a build — shim/
adapter/config/reporter, check rows drafted with expected= placeholders,
the reading frame; build + check + window after DONE and Frank's go).
Stall watchdog */10; keepalive 21,51. No box time used by any of them.

## 2026-09-05 (EDT, 15:3x), tenth session part 8 — the three box-free lanes landed: censusprep MERGED, b39prep and b36census DELIVERED on their branches (unmerged by design)

censusprep (sonnet) merged 727529c: docs/dev/measurements/
probe_altwide_size_census.py — the altwide size census as a stable
probe, `--pin <sha>` via pin.sh --path, caps from the archived registry,
`--compare` per route, `--dry-run`; self-tested against the 2026-09-02
table and a synthetic −20 % VM row; fires with [B39]'s re-pin.
b39prep (opus) delivered branch b39prep (4 commits, NOT merged — it
moves configs.toml's pin to 37f5ae02, unbuilt here): the floor STAYS 16
(abi 23 adds a macro, no rx_info member); RX_VM_CLS_FOLDS unconditional
on every VM artifact; -fno-cls-fold = bit 24, VM route only → two
siblings (pcrec-auto-noclsfold predicted a null pair; pcrec-vm-noclsfold
the AFTER's pair); the corpus's ONLY fold-pair witnesses were altwide's
ci-256/512 (the plan's "(?i) in email/loglines" was wrong); reporter
v15 (clsfolds=; the prog: note corrected per I-50 §1), 71 tests; check
rows drafted with DRAFT/TBD placeholders; the build sequence on the row.
b36census (opus) delivered branch b36census (3 commits, NOT merged —
Frank's clear + make check on a free box first): bench/syntax@0.1, 95
patterns / 18 families / 8,265 expectations, coverage derived from the
seed with a by-name re-seed gate, the outlier rule R0-R7 and P1-P13
before any run, the five fold-pair witnesses added on the manager's
request (so abi 23's surface is wider than two altwide patterns), a utf
sibling convention documented. All three lanes used no box time. No
crons but the keepalive (21,51). pcrec's battery still on the box.

## 2026-09-05 (EDT, 18:3x), tenth session — CLOSE (Frank: "prep for session end")

The tenth session ran 2026-09-04 19:26 → 2026-09-05 18:3x EDT. Two
windows RUN and READ: the 288d505 STEP 2 AFTER (12/12; O-16 — the
customers unreachable by construction, the ×0.5 plain-ladder win real,
per I-49) and the 334fd10e deny-flag AFTER (10/10; O-17 — the order
effect gone, the VM over the JIT 32/44, the floor ×2.0 tripwire). One
re-pin BUILT and merged ([B37], abi 22). Three box-free lanes on Frank's
relayed question: the census probe merged; [B39]'s abi-23 prep and
[B36]'s bench/syntax@0.1 on their branches. Inbox I-44..I-50 acked; BD8
+ two amendments (the machine move, the remote as read transport, the
inverted slot handshake); Frank's push grant and the 30-min keepalive
saved as memories. Store 122 → 144. Master 8612b17 + this entry, clean,
pushed. Worktree worktrees/b36census KEPT (for its pre-merge make check
on a free box); branch b39prep kept without a worktree. No crons. pcrec's
battery/probes may still be on the box; its DONE lands in the inbox.

Lessons: `pcrecdev1` resolves to two sessions after a Remote Control
attach — address the remote one by ref. A lane's delivery can cross a
manager's amendment — re-check the deliverable for the ask, then resend.
A prep lane that moves the pin must NOT be merged before the build. A
peer relaying Frank's question is a go to build, not to merge — say so
on the row. The lane brief's "you will not be woken" held for all six
lanes today.

## 2026-09-06 (EDT, 10:2x-11:3x), eleventh session part 1 — I-51/I-52 acked; [B36] bench/syntax@0.1 CHECKED GREEN, RE-SEEDED and MERGED; [B39] re-targeted to d34c9131, built, registries re-archived (every delta as predicted)

Wake: master clean at 954fdd9 with two new inbox items. I-51 (pcrec's
DONE): the battery at 37f5ae02 green after same-day repairs, K49 fixed
(byte path byte-identical, abi 23 unchanged), K50 filed as a FUTURE abi
event, ask (vii)'s verdict NEEDED on this box's gcc 15.2, ask (i) both
halves — the floor forced-VM ×2.0 does NOT reproduce under pcrec's
instrument here (plain 0.2945 / forward 0.2943 ns/B; `shared` ~5×) nor on
ARM (a tie; `shared` ~3×), so the [B39] window re-runs the cell under OUR
instrument and the variable, if it persists, is the regime. I-52 (Frank):
[B39]'s pin ADVANCES to tip d34c9131 (the rebase = a target-SHA edit);
[B36] CLEARED FULLY (check + merge + first sample night); the
`--list-syntax` re-seed at 9a1583ba differs from the 334fd10e seed by ONE
description row (no machine-read column). Both acked (d94c678, pushed).
~/pcrec lacked d34c9131; pcrecdev1 fetched it there on a live ask (BD2:
we never write ~/pcrec's refs) — GitHub's tip is already 1c4c91b4, one
docs commit past the pin. Box quiet (load1 0.15, max busy 3.6 %).

[B36]: `make check` on worktrees/b36census on the free box — 4/72/0 ·
312/312 (the fifth set's seven checks) · 70+7, EXIT 0, ~19 min. Then the
re-seed on the branch (f19026b): `list_syntax_9a1583ba.tsv` verbatim
under the source header, the old seed retired, SEED repointed,
coverage.tsv re-derived (77/32/19/5/5 unchanged; only its header line
moved), pattern_facts unchanged, both `--check` modes green. Merged
--no-ff (398d5bb; the plan.md [B36] row resolved as the lane's row + the
acks + the merge note), worktree removed, root CLAUDE.md's paragraph
updated (31fb624), pushed.

[B39]: worktree worktrees/b39 on b39prep, master merged (the [B39] row
conflict resolved as the lane's full row + the manager note + the acks),
37f5ae02 → d34c9131 in the fourteen prep files (2438d61; plan.md keeps
the historical "prepared from the 334fd10e..37f5ae02 diff" wording).
`pin.sh d34c9131` built in ~1 min. The THREE REGISTRIES re-archived from
the binary (522ad39), bodies verified byte-verbatim: axes 74/25 → 76/26
(`cls-fold`: order 1 `fold`, deny bit 24 `-fno-cls-fold`, stamp
RX_VM_CLS_FOLDS, no stamp_value; order 2 `denied`), definitions 50
BYTE-IDENTICAL (the sixth pin running), limits 55 → 56
(PCREC_MAX_AUTO_DFA_ELEMS 30,000,000 `-D` after PCREC_MAX_SUBSET_ELEMS —
[LIM-2] N1, the AUTO route's DFA-attempt work budget — and three rows'
`override` none → flag with new raise-only flags --max-nfa-states /
--max-dfa-states-goto / --max-subset-elems, DFA_STATES_TABLE re-worded
"NOT RAISABLE"). EVERY delta is what the b39prep lane predicted from the
source diff; nothing unpredicted. The altwide size-census probe at
d34c9131 is running (compile-only). Next: `make check` on b39 (the DRAFT
rows fire by name, the TBD sizes print), fill and strip, merge; the
abi-23 AFTER window this afternoon; bench/syntax's first sample tonight.

## 2026-09-06 (EDT, 11:0x-11:5x), eleventh session part 2 — [B39] CHECKED (324/324), documented, MERGED (5582850); O-18 sent; the abi-23 AFTER window STARTED 11:55

The build sequence's back half. The altwide size census ran at
d34c9131 (compile-only, 132 rungs, ~10 min: the large auto refusals are
the slow rungs) — VM route −15.6 % median vs 2026-09-02, ci-256 forced-VM
359,507 B (the check's own count 359,502: −20.3 % from 334fd10e's
451,050), auto emit flat / code +3.2 % as a cross-pin sum, the refusal
boundary unchanged; documented in measurements/CLAUDE.md; [B35] (7)
CLOSED. `make check` on the b39 worktree: the FIRST run was killed by
the harness's background-task memory heuristic (the box had 12 GB
available; the kernel logged no OOM) and, python's stdout being
block-buffered into the log, lost its output — reruns go `setsid nohup`
with PYTHONUNBUFFERED=1 and a poll loop as the waiter. The rerun:
check-harness 322 passed / 2 FAILED — both the SAME finding: on bounded
cls-upto-32768's `(?:...)\z` form under auto, the DFA attempt now
overflows by [LIM-2] N1's PCREC_MAX_AUTO_DFA_ELEMS (30M, "-D" only)
before K7's 48M — RX_ENGINE_WHY "subset construction exceeds 30000000
elements (N1 auto budget)" — same outcome (declined-nullable, the VM
built), a different limits row by name, +4 B (18,485 → 18,489). Every
[B39] DRAFT(v) row PASSED by value: folds 3 on `(?i)abc` (634 program /
18,045 B; denied 18,196, +151), 26 on ci-256 (351,053 / 359,502 B;
plain, frameless 0, islands 0), 0 on every fold-free VM artifact (35 VM
with, 26 DFA without), the structure rows (as many `(b | 0x20) == N`
constants as the stamp says, 0 bitmaps), the four-pair deny control;
w-256 292,043 → 292,069 (+26 exactly). The two red rows re-aimed at the
N1 prose (asserted by value, distinct from the plain form's STATE cap);
every DRAFT/TBD placeholder retired to its measured value (the machinery
kept for the next prepared re-pin); the third run 324/324. check-report
71+7 OK — run ALONE after a 600 s gnutimeout killed it beside the
harness; its ~7-10 min is jsonschema's `referencing` pointer resolution
validating the 144-record store (a standalone faulthandler dump caught
it there at 60 s) — slow, not hung. Lane b39docs (sonnet, worktree
b39docs) converted twelve files' PREPARED/NOT BUILT prose to the measured
facts (prose only — AST-verified for report.py; adapter.py's diff is
inside string constants); one correction of its correction: the limits
delta is FOUR re-worded rows (three gain a raise-only flag +
DFA_STATES_TABLE "NOT RAISABLE"). O-18 written (§1 the re-pin, §2 the
stamps by value, §3 the N1 finding with two asks, §4 the census, §5
[B36] merged, §6 today's windows). Merged --no-ff (5582850), pushed;
worktree removed. Box quiet (load1 0.15); the AFTER window launched
11:54:52 under setsid via run_suite.sh: altwide × {vm, vm-noclsfold,
auto}, bounded × {auto, vm, vm-in}, loglines × {auto, auto-noclsfold},
email × {auto, auto-noclsfold}; suite log
build/windows/suite_b39_after_20260906T155452Z.log; ~3.6 h expected.
pcrecdev1 told live (O-18 pushed, the box is ours until the night is
closed). NEXT: read the AFTER (reports + ledger + O-19), launch
bench/syntax's first sample tonight (SUITE=syntax, the six pinned).

## 2026-09-06 (EDT, 12:0x-15:3x), eleventh session part 3 — the abi-23 AFTER window RAN (10/10 measured); I-53/I-54 acked; bench/syntax's ids made case-unambiguous and its FIRST SAMPLE launched 15:27

THE AFTER WINDOW (suite_b39_after_20260906T155452Z.log): 11:54:52 →
15:13 EDT, 10/10 cells `measured` — altwide × {vm, vm-noclsfold, auto}
(38 min; the vm-noclsfold cell's attempt 1 was refused by the pre-flight,
cpu11 19.64 % busy at 12:09:26 — the box-free rename lane's generator
run is the likely competitor: a "box-free" lane still trips the gate
for a few seconds; attempt 2 clean), bounded × {auto, vm, vm-in} (132
min, all attempt 1), loglines × {auto, auto-noclsfold} (17 min), email ×
{auto, auto-noclsfold} (10 min). Store 154 (144 measured; the 9
inconclusive-load + 1 spread are historical), records committed 99a0b60.
Reading delegated to lane b39read (opus, worktree b39read): five report
groups first (the same-pin fold pair, the altwide and bounded cross-pin
AFTERs against 334fd10e, the two null pairs as the noise floor), then
the ledger 2026-09-06-b39-clsfold-after-d34c9131.md scored against P-a..P-f
(the fold pair on ci-256; ci-512 refusing on all arms; the null pairs
≈1.00; the same-pin fill ≈1.00 within the 2026-09-05-b37 §6 bands; the
`\z` cls-upto-32768 compile FASTER under N1; the `_in` control and the
floor ×2.0 under our instrument). O-19 is the manager's after the ledger.

I-53 (pcrecdev1, ~12:4x): the N1-before-K7 ordering is INTENDED
(limits.md §3.3: a smaller auto-only budget reaching the same fallback
before the full K7 spend; `--engine=dfa` unaffected); our "-D-only"
premise was FALSE — `--max-auto-dfa-elems` exists (raise-only, verified
live 40M/1000) and the `override` column's `-D` is pcrec's rendering
drift on a two-lever row ([LIM-OVR] chartered; read desc on BUILD_D
rows); one unit, two spellings, harmonized only at a future abi event.
Acked (f9f6713); list_limits.tsv's header note corrected in place (body
still byte-verbatim). Live from pcrecdev1 the same hour: a PORTABILITY
finding — three bench/syntax pattern-file pairs differ only in case
(anc-Z/z, cls-S/s, unp-P/p; one file each on APFS/NTFS; the only such
pairs across the five sets). Lane b36rename (sonnet, box-free: no
gen_expectations, no compiles) renamed them to `-uc`/`-lc` suffixes —
six pure git renames, expectations id-only (522 of 8,265 rows, verified
row-for-row), coverage/facts counts unchanged, the convention written
into bench/syntax/CLAUDE.md; the manager ran gen_expectations --check
(8,265 re-derive; the worktree needed its gitignored subject trees
generated first) + the two other --check modes in the gap, merged
--no-ff (before any record carried the old ids: no version bump).
I-54 (Frank, via pcrecdev1 ~18:1x UTC): THE MANAGER SESSION RUNS AS SONNET
from its next start; per-lane tiering unchanged (opus for blinded/design
lanes); the watch-item is turning a red check into the right question —
promote a deliverable to an opus lane and say so, never thin the
analysis. Acked as a STANDING note atop plan.md's rows (1192416).
A non-fast-forward push refusal (I-54 had landed on origin) was merged
in (a4beee9) — the new channel flow means fetch before every push.

bench/syntax@0.1 FIRST SAMPLE launched 15:26:55 under setsid
(suite_b36_first_20260906T192655Z.log; SUITE=syntax, the default six
pinned testees; the main tree's gitignored syntax subjects generated
first; box quiet, load1 0.44): ~5 h, done ~20:30. The 20-min watchdog
cron (7,27,47) watches it. Lesson of the day for the box: the harness's
background-task memory heuristic kills long Bash tasks AND trivial
waiter loops regardless of real memory (12 GB available, no kernel OOM)
— every run longer than a few minutes goes `setsid nohup` with
PYTHONUNBUFFERED=1 and is polled by the cron, not by a waiter.

## 2026-09-06 (EDT, 15:4x-17:0x), eleventh session part 4 — the abi-23 AFTER READ (lane b39read) and O-19 sent; [B39] COMPLETE and archived; Frank's lifecycle/watchdog doctrine adopted mid-session

Lane b39read (opus) delivered de865b2: five report groups (the fold pair,
the altwide and bounded cross-pin AFTERs, the two null pairs) and ledger
2026-09-06-b39-clsfold-after-d34c9131.md (622 lines, P-a..P-f scored, the
2026-09-05-b37 §6 bands re-scored). Merged 17d0922. THE READING (O-19):
(1) THE FOLD IS SLOWER on its one witness — ci-256 forced-VM fold ÷
denied ×1.0446 throughput / ×1.0273 search / ×1.0950 match against a
1.34 % noise floor (the two null pairs: loglines 22/22 artifacts
identical, 0.995-1.013; email 6/6) — while code 359,502 vs 451,076 B
(×0.797), .so −32.3 %, compile ×0.40: I-49's speed claim refuted on this
surface, its size claim confirmed; the corpus has exactly TWO fold
artifacts (clsfolds=26; 0 on 277 VM, absent on 189 DFA). Asks (i)-(iii):
per-site instruction counts, a REPEATED fold-class customer, the default.
(2) [LIM-2] N1 moved a SECOND rung — cls-upto-8192 `\z` under auto went
dfa→vm (the 937 KB WARNED DFA had been selected where the VM is ×6.6
faster on match; compile ×0.147; the r-01024 customer 3,780 → 622 ns) —
ask (iv): AUTO declining a warned-size DFA when a VM form exists. (3) THE
`_in` CONTROL: floor throughput vm 0.5934 / vm-in 0.5924 ns/B — a tie,
both ×2.00 vs 288d505's 0.2968; pcrec's instrument ties at 0.2945 — OUR
SCALE IS ×2.01 THEIRS. The hypothesis that fits all four numbers: a FIXED
per-call cost of ~31.6 µs (our subject is 106.5 KB; theirs 1 MB dilutes it
to +0.03 ns/B) introduced abi 16→22 — ask (v): their instrument at ~100 KB;
ours: the floor at 64 KB/256 KB/1 MB on the syntax sweep tomorrow ([B35]
(9')). (4) Flat elsewhere: altwide VM cross-pin median 0.9993 (66 cells),
bounded auto 1.004 / vm 1.001, the order pair ×0.9971 at 292,069 B both,
nest2-4's regression undone (×0.741), a new nest2-letters-6 throughput
×1.138, stamps identical over 270 artifacts but the one route change; one
instrument oddity (w-8 match whole ×0.66 on byte-identical artifacts, the
denied arm the outlier) recorded. The lane also found the window was 9/10
at attempt 1 (the vm-noclsfold pre-flight refusal at 12:09 — our own
box-free lane's generator; the retry cleared) — the journal's part 3
"10/10 measured" stands, "all attempt 1" did not (corrected here). KB-11
filed: one `report` invocation validates the whole store (640 s at 154
records, 10m51s per CLI run) — fix direction: filter by index first, one
validator per process. [B39] STATE:completed, archived to plan_completed.md.

DOCTRINE (pcrecdev1 pushed 58778c0 + 91a528a with Frank's direct
authorization — the skill rewritten, docs/dev/lanes/BOILERPLATE.md +
CLAUDE.md created): the prompt-firing stall-watchdog cron is DEAD (each
tick re-read the manager's whole context; ~73M cache-read tokens across
two pcrec sessions) → stall watching is a ZERO-MODEL background script
that exits only on actionable state; lanes never keepalive (5-min TTL),
work continuously to a committed report (docs/dev/lanes/<lane>_report.md)
and END; CLOSURE IS THE MANAGER'S ACT (TaskStop after accepting a
delivery; sweep at every acceptance and at pause; every lane STOPPED
before a window); briefs start "Read docs/dev/lanes/BOILERPLATE.md FIRST"
and carry only task/tier/pointers/deliverable; the main-session keepalive
during a hold stays legitimate (1-h TTL), two off-minute marks under an
hour apart. Applied at once: the 20-min watchdog cron deleted; a
persistent Monitor (no timeout; a Bash background task is capped at 10
min) emits one event on the syntax suite's completion / stale window /
process gone; the keepalive cron at 17,47 with the minimal prompt;
b39docs, b36rename and b39read TaskStop'd after acceptance. The syntax
first sample is on cell 2-3 of 6 (~20:30 finish).
