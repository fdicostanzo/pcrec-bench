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
