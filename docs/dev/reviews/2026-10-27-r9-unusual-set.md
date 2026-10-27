# r9 — critic panel on docs/design/unusual_set_v1.md v0.1 ([B148])

Panel 2026-10-27, three read-only critics, distinct lenses:
measurement validity (r9meas, sonnet; `-meas.md`, M-1..M-15), engine
semantics (r9eng, opus; `-semantics.md`, E-1..E-14), schema / comparator /
harness + ruling coverage (r9sch, sonnet; `-schema.md`, S-1..S-14).
43 raw findings: 5 blockers, 20 major, 18 minor. Consolidated by the
manager; every disposition below is the manager's unless marked
ESCALATED. The authority for every ruling cited is the [B148] row of
docs/dev/plan.md (Frank, 2026-10-27).

Dispositions: `accepted` (v0.2 applies it as the critic's fix),
`accepted-amended` (applied with the stated change), `merged into X`
(same defect, one fix), `escalated` (Frank must rule), `deferred`.

## Consolidated defects (what v0.2 must do)

**C1 — Ruling drift (S-1, S-6, S-7, S-8, M-11, M-12, E-9).** v0.1 was
written before OQ-1/3/4/6/7/9/10/11 were ruled. v0.2: budget and assist
ledger keyed per (MEMBER, engine), one author lane per pair, the
"adding a member flips a verdict" text deleted (S-1); two WILD members
(recursive JSON validator, balanced S-expression matcher) with source,
licence and admission entries, not duplicating capability's
nested-comment-rec (S-6); sqlite3.c and kernel pins resolved at fetch
with show-then-approve per file (S-7); netstring on libpcre2/Onig
ASSISTED, its check-at-end spelling no longer a syntax-only variant,
OQ-6/10/11 de-PROPOSED (S-8, M-11).

**C2 — Identity and capability model for per-member verdicts (S-2,
S-11).** `testee.assist` becomes an array `{member, tokens, lines,
sha256}` + set-level `assist_version`; ONE identity token
`assist-<setversion>` that never varies with which members passed;
per-member verdicts in `assists.tsv`. `REQUIRES_VOCAB` grows `vars`.
NOT-CAPABLE's count rides `declaration_ref` as `…assists.tsv:<row>
tokens=N budget=300`; NOT-CAPABLE stays distinct from did-not-compile.

**C3 — The spread rule and iteration unit for `call-stream` (M-1, S-3).**
One iteration = one full replay; ship rule `v1.11-group` under
record_schema.md §4's rule-revision clause (the [B144] precedent),
updating reduce.py, validate.py and X32's text; iteration calibration
defined for streams. L1 deliverable.

**C4 — Call-stream semantics (M-7, M-13, S-10).** Bytes = sum of segment
lengths, not subject size; `calls` the named denominator; an L4
pre-flight proving a refused call costs O(segment) on every engine, else
explicit anchoring; result tokens into a preallocated array, hashed after
the clock; expected call counts and row durations stated; subject load
outside timing. The stream token carries group 0 + group 1 only (E-2b);
only `vectorscan-block-som[-utf8]` run this set (boolean grain cannot
produce a span); "refused" defined engine-neutrally (host code returns
it).

**C5 — Callout arms (M-2, M-3, M-4, M-5, M-10, E-5, E-6, E-8, S-12).**
`pass` = the full per-engine wrapper + a stub callee; pcrec's twin also
under `pcrec-vm`; `callout_fires` recorded per arm per engine and `real -
pass` reported only where fires match; each engine's own fire-view log
drives its callee share (an upper bound, cross-checked by `(real - pass) /
fires`); the share computed on EVERY engine, flagged when any exceeds 40%,
pcre2-jit's 20/40 kept as the reference (OQ-6 unchanged); `callees.o`
built once with fixed flags, sha256 recorded, `cu-unity` declared as a
recompile; `pass-nofn` named pcre2-only; no cross-arm subtraction on
co-netstr. The RETURN-CODE MAPPING table (FAIL → pcrec −1, PCRE2 +1,
Onig +1) with a first-candidate-fails control; the assisted netstring
pattern `(\d{1,9}):(?>(?s:.)*?(?C4)),` and pcrec's consume callee
returning RX_FAIL on an overlong length; twins written in the common
subset (`\w+`). WHO computes the arm comparisons: a check-harness gate for
pass == twin answers, a set-sidecar column for the cost split, `twin_of`
added to the tag vocabulary.

**C6 — Variables assist (M-6, M-14, E-7, E-13).** The report states the
stream ranks mostly by compile cost and prints pcrec's break-even call
count; regex/JIT free placed identically for every engine; keying,
container and assist sha256 in the ledger, and the readout says an
assisted time measures that assist; stream length fixed across the d4/
d64/d4096 ladder, miss count printed. Rust assists compile `unicode(false)`
(declared); va-term's case variants ASCII in v0.1. vars.md fidelity:
`${!name}`, default words are literal and escaped
(variables_pattern.md:305), the nested-unset chain dropped from v0.1 and
asked of pcrec; vectorscan spells NUL as `\x00`.

**C7 — Deep nesting (M-8, M-9, E-1, E-3, E-4, E-10, E-12, S-9).** The
default arm reported as a depth-of-failure table by limit name with rungs
128/512/2k/8k/32k added; per-engine predictions (interp likely MATCHES
nest-100k at defaults; JIT and pcrec give up; Onig silently wrong past 20).
Oniguruma's default nest level 20 fails SILENTLY (wrong span / false
no-match): declared in NOTES.md before any run, raised in the deep arm
through the global setter; all six Onig defaults read back; −5/−18
named; the setters in driver.c outside the timed loop (no BD16 edit). JIT
deep also sets match_limit (−46 vs −47 recorded). Buffers created once
before the timed loop, pre-touch stated; a dry-run duration per engine and
arm, `CELL_CAP_unusual`, and a timed-out pathological's record defined;
pathologicals in fresh processes. Each engine's effective limits recorded;
"1 GiB" stated as not like-for-like in depth. **The interp heap question
is ESCALATED (Q1).**

**C8 — Memory high-water (M-15).** `deep_mem_method` = canary |
counting-alloc | mincore | rss-delta in engine_metadata; never ranked
across methods; bytes per nesting level beside the absolute; an UNTIMED
fresh-process pass with instrumentation off in the timed arm; a
known-depth control (it also settles sljit's grow-by-touch question) and a
no-recursion floor per method; the default arm reports frame count for
pcrec; the record's fit for subject-grain integers checked in L1.

**C9 — Oniguruma cscan fidelity (E-2, E-14).** A declared syntax-only Onig
variant replacing `(?(DEFINE)...)` with `(?<sp>...){0}(?<items>...){0}`
plus a witness subject `(?{x})DEFINE`; the OQ-10 witnesses recorded as
probed (callout spelling `(?{...})`, `(*name)` needs registration before
`onig_new`, `[\x80-\xff]` and `\G` behave); verdict stays NATIVE (rule 1:
the feature is in Onig's syntax; a respelling is the variant mechanism).

**C10 — Readers, protocol, build order, bump mechanics (S-4, S-5, S-13,
S-14, E-11).** Reporter treatment (a `--grain stream` view on the
[B143] model, refusing mixed input by name) + the viewer/trend/frontpage
and interpret/catalogue behaviour on the new regime; driver protocol
`--mode calls`, the calls-file and callee-binding format, per-call output,
a config key gating the set (the `subst_only` analogue) with a refusal by
name; UNUSUAL_GATE_SKIPS + self-test, `tools/check_unusual.py`, `make
check-unusual` in `make check`, expectations_stream re-derive with a run
time; Frank approval gates shown in the build order (sqlite, kernel
files); X47-X5n each with a negative example, the history entry, whether
an assisted engine has a compile row, the validator's limit on
results_sha256. pcre2-dfa's exclusion reason restated (no captures).

## Escalated to Frank

**Q1 (E-3, S-9) — the 1 GiB ceiling on pcre2-interp LOWERS its limit.**
libpcre2's compiled-in heap limit on this box is ~19 GiB (20,000,000
KiB), so "raise to 1 GiB" is a cut for the interpreter only. Options:
(a) a CAP of 1 GiB for every engine (equal budget; the interp's `deep` is
tighter than its `default`, said so); (b) max(default, 1 GiB) per engine
(every arm a raise; budgets unequal). Manager recommends (a): the point
of one ceiling is that a give-up means "needs more than 1 GiB" on every
engine, and the default arm already shows the library's own setting.

## Deferred

- E-1's silent wrong span at Oniguruma's nest limit: a candidate for the
  upstream pipeline (`/pcrec-bench-upstream`), triaged only after checking
  Oniguruma's documentation says nothing of the behaviour (report only
  unambiguous bugs). Owner: manager, after v0.2.
- E-13's nested-unset rule: asked of pcrec (outbox) with v0.2.

## By-id completeness (43/43)

| id | → | id | → | id | → |
|---|---|---|---|---|---|
| M-1 | C3 | E-1 | C7, deferred (upstream) | S-1 | C1 |
| M-2 | C5 | E-2 | C9, C4 | S-2 | C2 |
| M-3 | C5 | E-3 | C7, Q1 | S-3 | C3 |
| M-4 | C5 | E-4 | C7 | S-4 | C10 |
| M-5 | C5 | E-5 | C5 | S-5 | C10 |
| M-6 | C6 | E-6 | C5 | S-6 | C1 |
| M-7 | C4 | E-7 | C6 | S-7 | C1 |
| M-8 | C7 | E-8 | C5 | S-8 | C1 |
| M-9 | C7 | E-9 | C1 | S-9 | C7, Q1 |
| M-10 | C5 | E-10 | C7 | S-10 | C4 |
| M-11 | C1 | E-11 | C10 | S-11 | C2 |
| M-12 | C1 | E-12 | C7 | S-12 | C5 |
| M-13 | C4 | E-13 | C6, deferred (pcrec) | S-13 | C10 |
| M-14 | C6 | E-14 | C9 | S-14 | C10 |
| M-15 | C8 | | | | |

All accepted (none rejected). Q1 is the only open item; v0.2 is written
with Q1's answer.
