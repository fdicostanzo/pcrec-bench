# r9 critic file — SCHEMA / COMPARATOR / HARNESS + RULING COVERAGE lens (unusual_set_v1.md v0.1)

Critic r9sch (sonnet, read-only, 2026-10-27); verbatim from worktrees/.mgr/r9/sch.md.

# r9 critic: schema / comparator / harness consistency + ruling coverage
Target: docs/design/unusual_set_v1.md v0.1. Rulings: the [B148] row, docs/dev/plan.md:43.

S-1 (blocker) §5, §11 OQ-1: the note contradicts the OQ-1 ruling.
- The ruling is a budget per (MEMBER, engine). §5 "Granularity" (unusual_set_v1.md:310-314) says one assist per (feature, engine) serving every family member, and §11 still lists OQ-1 as open.
- The same assumption runs through the ledger (:316-319), authoring (:321), identity (:337-344) and §10 L6 (:434).
- Fix for v0.2: key assists.tsv and the author lanes by (member, engine).
  - One blinded author lane per (member, engine); the lane count in L6 becomes members x engines.
  - Keep the "shared assist" idea only as an author option, with its tokens counted once for each member it serves.
  - Delete the sentence that adding a member can flip a verdict (:446-447).

S-2 (blocker) §5, §7, §3: the identity and capability model cannot express per-member verdicts.
- Single assist object. testee.assist is one {feature, version, ...} object, and the single assist-<feature><n> token (:337-340, :387-389) cannot say which members are assisted. Under S-1, one libpcre2 config can be ASSISTED for va-tenant and NOT CAPABLE for va-term.
- Capability vocabulary. capability.py:88-101 has a closed per-pattern REQUIRES_VOCAB. It has `recursion` and `callouts` but no `vars`, so `requires-vars` is a vocabulary growth the note never mentions.
- Declaration granularity. capabilities(config) is declared per config and per token (capability.py:222-228). A per-member verdict needs one of: a per-member token (requires-member-<id>), or a per-config list of assisted members in the `ext bench` block.
- Proposed fix.
  - Make testee.assist an array of {member, tokens, lines, sha256} plus a set-level assist_version.
  - Use ONE identity token, assist-<setversion>. It must not vary with which members passed, or a re-authored member splits history. X-rule: present iff the token is present.
  - Keep per-member verdicts in assists.tsv, surfaced through declaration_ref.

S-3 (major) §7: the trial-agreement rule needs a revision the note omits.
- The gap. reduce.py:289-327 gives v1.10-group an iterations >= 1 floor for `substitution` only; every other regime keeps > 1. X32 is versioned by the record's schema_version (record_schema.md:212, X32).
- Two ways it goes wrong.
  - If a call-stream row runs one iteration, every trial is unjudged and trial_agreement is n/a-trials.
  - §3.3's memo "cleared at the start of every timed iteration" (:223) implies the iteration count could be above 1.
- Fix. §7 must state the call-stream iteration policy. If it is 1 per replay, add a v1.11-group rule version (the rule-revision clause, record_schema.md §4, as in [B144]) and update reduce.py:317, the validator mirror (validate.py:269) and the X32 text. Also state this in the L1 deliverables.

S-4 (major) §7, §10: the reporter and the other readers are not covered.
- Set-grain reduction. report.py:4343-4360 shows what the substitution regime needed: its own grain (report_subst.py), a refusal by name when mixed, and a header note. The note says nothing equivalent for call-stream.
- What the reducers do with a call-stream row.
  - reduce.py and frontpage.py:163 key cells by (pattern, regime, form, subject).
  - A call-stream row's ns is a whole stream, and MB/s would divide by subject bytes (cscan) or a line count (vars).
  - n_wrong and pass-rate would be read from match_outcome only, with stream.refused and results_sha256 invisible.
- Fix.
  - Specify the reporter treatment: either a --grain stream view like [B143], or set-grain with the metric declared as ns per stream plus calls/s. Name `calls` as the denominator.
  - Add call-stream to the viewer exporter, tools/trend.py and frontpage.py skip or handle tables. Today none of them mention `substitution` (grep found no hits), so how they treat unknown regimes needs checking in L1.
  - Say how interpret.py and the catalogue rules (R-RANK, R-FLOOR, R-ARM) behave on the new regime.

S-5 (major) §7, §10: the driver protocol and the harness plumbing are missing.
- The substitution tier added --mode subst with its own flags (adapters.py:72-100), subbench.py:28-38 (REGIME_TO_ENUM, REGIME_MODE), harness.py:684-693 (subst_only gating) and substrun.py.
- L4's "call-stream in every adapter" has no counterpart: no --mode calls, no --calls FILE and binding-table format, no per-call result output, no harness gating for engines that cannot run the mode. These must be specified in §7 or a new section.
- families = ["<feature>"] on a config (:342) is not an existing mechanism. `families` exists only as a pattern tag (subbench.py:159). The config-level analogue is subst_only (harness.py:684). Specify a config key and its harness check, and a refusal by name when run against the wrong set.
- Callout twin, pass and real arms need a per-pattern callee binding (callee id to function, `user` pointer). That is a driver-protocol field the note does not define.

S-6 (major) §2, §9: the wild-member ruling is not reflected.
- OQ-9 was ruled after v0.1: v0.1 ADDS 1-2 WILD members, a recursive JSON validator and a balanced S-expression matcher.
- v0.1 §2 (:81-87) says "No wild member in v0.1" and defers them to v0.2.
- v0.2 must add two `wild` rows with source and licence per capability_set_v1.md §4.1, admission-control entries and expectations, and remove the "PROPOSED: none" paragraph.
- capability's nested-comment-rec is already the cited recursion example (:49), so the new members must not duplicate it.

S-7 (minor) §4.2: the kernel-file and sqlite rulings are stale.
- Ruling OQ-3 is the latest sqlite3.c, xz-vendored, with URL and sha256 shown before download.
- OQ-4 is the five proposed kernel files at the latest stable tag, with URLs and sha256 shown before fetch.
- The note says "the release current at build" and "one tagged release". Pin both to the version resolved at fetch time and state the show-then-approve step for each file.

S-8 (minor) §3.2, §3.0, §11: OQ-7, OQ-10, OQ-11 and OQ-6 need folding in.
- OQ-7. Netstring on libpcre2 and Oniguruma is ASSISTED. §3.2 (:164-170) and the verdict table (:111, :114) call it NATIVE via a check-at-end syntax-only variant. Under S-1 it also becomes a per-member 300-token assist, and the "fire count is the result" argument goes.
- Variants. Requirements v3 says a variant must reproduce results exactly. The check-at-end spelling is a different callout semantic (one fire per byte), so it is no longer a valid syntax-only variant once it is not native.
- OQ-10. Oniguruma build-time witnesses are RULED, so §3.0 should say the verdict is witness-gated at build, not "to WITNESS".
- OQ-11. pass-nofn is ruled. §3.2 says "PROPOSED"; make it a ruled control arm, and state which driver option disables the callout function. That too is a protocol flag.
- OQ-6. The 20% flag and 40% resize thresholds are ruled. Strip the PROPOSED tags.

S-9 (minor) §6: the ceiling ruling is partly inconsistent.
- The ruling is CEIL = 1 GiB for every engine.
- The deep arm for libpcre2 interp sets pcre2_set_heap_limit(CEIL/1024) (:351). That unit is KiB and is consistent. But "counters at their type's maximum" is not a 1 GiB ceiling for match and depth limits.
- Oniguruma "unlimited" is not CEIL.
- For pcrec the _in entry buffer is 1 GiB by the ruling, but limits.md has step and work budgets raised separately. Say which "ceiling" each arm gets, and record the effective values for every engine.
- Also state that lim-ceil1g joins compose_config_extra as a sixth part appended LAST (testees/pcrec/CLAUDE.md:125-135 calls this append-only), and give the order relative to cu-unity and assist-*. For libpcre2, the composition lives in adapters.py:218-222, which has no equivalent compose function.

S-10 (major) §7, §8: engine neutrality (R-BENCH-4) of the new fields.
- Not neutral. The results_sha256 token format (m:<s>,<e>[;<g1s>,<g1e>...]) assumes group 1 exists. A testee.grain = boolean Vectorscan config (X34: never a span) cannot produce it. State that only vectorscan-block-som/-som-utf8 run this set.
- Not neutral. callout_fires and assist_compiles as match-scope engine_metadata need a declared type per testee. Say the declaring adapter owns it and a testee that cannot count (JIT, no counting build) omits it.
- Fine. call-stream itself, stream.calls, matched, nomatch and refused are neutral.
- Fix. Add an engine-neutral statement of what a "refused" call means for an engine with no refusal concept (host code returns it, per §3.3).

S-11 (minor) §5: NOT-CAPABLE is carried only in free text, and the ranking exclusion is unstated.
- NOT-CAPABLE is unsupported-by-declaration with the token count held in assists.tsv, referenced only from the declaration_ref string. The count is not in the store, so the reporter and interpreter cannot show "exceeded at N tokens".
- Reuse is otherwise sound: report.py:1073, :1104 and :6598-6616 already count `unsup` as excluded, never as a wrong answer.
- Fix. Put the count and budget in the declaration_ref format, e.g. "...assists.tsv:<row> tokens=N budget=300", or add it to the compile row as an optional integer pair. State explicitly that NOT-CAPABLE and did-not-compile stay distinct (report.py:416).

S-12 (major) §3.2: twin, pass and real are three patterns, but the comparator has no arm concept.
- R-ARM compares testees one config token apart on the same pattern, not patterns related by twin_of. twin_of is a new tag with no reader.
- So "callout cost = real vs twin" and "pass == twin answers" (:149-150) are not computed by the reporter, interpreter or any gate.
- Fix. Specify who computes them: a check-harness gate for pass == twin, and either a new interpreter rule or a set-sidecar column for the cost split. Also add twin_of to the pattern-tag vocabulary.

S-13 (major) §10: the build order is missing steps.
- Generic gates. Without L1/L3 work the generic bench/*/ gates apply to this set automatically (selfcheck.py:219-240). They assume regimes the set may not use:
  - floor-quick-cell and floor-oracle-smoke need a matcher mode,
  - manifests runs gen_subjects,
  - the expectations re-derivation reads expectations.tsv.
  Add an UNUSUAL_GATE_SKIPS or a regime-aware equivalent of SUBST_GATE_SKIPS, with a self-test like check_subst_gate_skips.
- Own gate. There is no tools/check_unusual.py equivalent: counting build, calibration, pass == twin, assist ledger, memo counts, and each new X47-X49 negative example under schema/examples/bad/.
- Expectations format. The generic expectations re-derive reads expectations.tsv. State how expectations_stream.tsv is re-derived under make check-harness, and the expected run time (the utf8 set shows how large these get, check_utf8_validate_once ~66 s).
- Other readers. Catalogue rules and the interpret fixtures, and the viewer, trend and frontpage skip tables (S-4).
- Ordering. L2 (token counter and rules) and the ub_map.h helper are listed as parallel to L1, but L3 vendoring and L6 each need a Frank approval step (sqlite3.c URL and sha256, each kernel file) that the table does not show. Add them as explicit gates.
- Make. Add `make check-unusual` to `make check`'s target list.

S-14 (minor) §7: schema bump mechanics.
- Version note. v1.11 should carry the standard history entry in schema/record.schema.json:6 and record_schema.md:211-212.
- X-numbering. "X47-X49" is not enough for the rules the note adds: stream required iff regime, assist iff token, plus the iteration rule and any stream sum check (calls = matched + nomatch + refused). Use X47-X5n and list each with its negative example.
- Compile-row optionality. Say whether an assisted engine's compile row exists at all, since the assist's compile is inside the timed row.
- Validator limit. Say that the validator cannot hold results_sha256's expectation. The harness compares, as with X37.

v0.2 delta, in order
1. S-1 and S-2: per-(member, engine) budget and identity.
2. S-6: two wild members.
3. S-8: netstring ASSISTED, plus OQ-6/10/11 as ruled.
4. S-7: sqlite3.c and kernel pins.
5. S-9: the 1 GiB ceiling mapped per engine.
6. S-3 to S-5: iteration rule, readers, protocol.
7. S-10 to S-14: neutrality, NOT-CAPABLE count, arm checks, build steps and bump mechanics.
