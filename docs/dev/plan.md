# pcrec-bench Project Plan

Working plan derived from ../../APPROACH.md. Row ids carry a `B` prefix so
they never collide with pcrec's `[Mx.y]`/`[DD-n]` rows in cross-references.

## Step-state format (grep'able)

Every step line matches exactly:

    - [Bn] STATE:<state> — <title>

States: `not-started` | `started` | `completed` | `blocked` | `deferred`

Find work:

    grep -n "STATE:started" docs/dev/plan.md
    grep -n "STATE:not-started" docs/dev/plan.md
    grep -c "STATE:completed" docs/dev/plan_completed.md

Completed rows are archived in docs/dev/plan_completed.md (this file keeps
zero STATE:completed rows).

Rules: update the STATE tag in place when a step changes state; expand a
milestone into substeps only when work on it begins (replace its single
`[Bn]` line); note blockers inline after the title with `(blocked: reason)`.
Milestones start with Frank; nothing below [B1] starts unprompted.

## Queue

M1 ([B0]..[B6]) is COMPLETE and archived (2026-08-25). The rows below are
the M2 queue: [B8]..[B11] transcribe the pcrec manager's inbox items
I-1..I-4 (docs/dev/inbox_from_pcrec.md, Frank's rulings of 2026-08-25)
and pcrecdev1's feedback on the first sample
(docs/dev/feedback_pcrecdev1_2026-08-25.md); [B7] and [B12] carry the
older candidates. Proposed order (Frank confirms): [B8] → [B10] (ruled
"after the re-pin", in its (a)(b)(c) order) ∥ [B9] (a disjoint reporter
lane) → [B11] sub-bench #2 → the rest. Nothing starts unprompted.

- [B11] STATE:started — (2026-08-28: #2 begins as [B11.1] below; Frank's ruling that the pcrec manager may run bench sessions AS the bench when pcrecdev2 is down — one repo per session) SUB-BENCHES #2..#6, in Frank's ruled order
  (inbox I-2): (1) LOG-LINE SEARCH, 256 B–4 KB subjects, mostly-failing
  (the 95 % path): timestamps, IPv4/IPv6, key=value, quoted fields,
  typical ops patterns; (2) WIDE ALTERNATIONS / keyword tries (10, 100,
  1000 words; mixed lengths; common prefixes); (3) LOOKAROUND +
  BACKREFERENCE real-world shapes (password rules, HTML/XML tags, CSV
  with quoted fields, `(?<=...)` at 1 KB; pcrec's tests/lookaround as
  seed input, read-only); (4) BOUNDED-REPEAT / K23 / K32 band —
  compile AND match axes; (5) UTF-8 classes/properties — LAST (M5 is
  unbuilt in pcrec; today it would measure a missing milestone). Every
  set carries a per-call FLOOR control pattern (feedback §1d) and the
  give-up as a first-class outcome with the size at which it first
  fires (§1b: a size-sweep design item). Blinded set authors (D27-style)
  where the set has expectations to write. Expand into [B11.n] when
  work on the first begins.
- [B11.1] STATE:started — SUB-BENCH #2: LOG-LINE SEARCH (`bench/loglines/`, 2026-08-28). THE NUMBER THIS ROW EXISTS TO PRODUCE (inbox I-7 §1, pcrec [OPT-5]): on mostly-FAILING 256 B–4 KB subjects, what pcrec's DFA pays for having no REQUIRED-BYTE (any-position) precheck where pcre2-interp dismisses a subject at memchr speed — the regime where that dominates; the number decides pcrec's build (pcrec D77). Shape: typical ops patterns (timestamps, IPv4/IPv6, key=value, quoted fields, a status-code/level filter, a multi-token "error with context" shape), each with a documented REQUIRED literal where one exists and at least one pattern with NONE (the control: a required-byte precheck cannot help it); subjects = generated log lines, NON-PERIODIC by construction (drawn field lengths and vocab, seeded generator, seed + `periodic` fact recorded in the manifest — I-10), a matching-rate per pattern that is low (the 95 % path) but not zero; a size sweep for the give-up outcome (256 B → 4 KB → beyond, until any testee gives up, the first size recorded — I-2 §1b); the FLOOR pattern (one literal, `role = "floor"`, the rule since [B15]); oracle chain as bench/email (`gen_expectations.py` from libpcre2, `--check` mode, sha256 manifests, `make check` coverage). Patterns authored from the GOAL (D27-style: the author reads no pcrec source or corpus). Measured in a window after the [B16] re-pin so the number is at abi 8.
- [B16] STATE:started — RE-PIN to pcrec `35e1ab1` (abi 8; inbox I-5, I-6, I-11, I-12, I-13 — one adapter change for five pins, as I-5 asked). Adapter: `configs.toml` pin; the shim reads `RX_DFA_SCAN` / `RX_DFA_PREFILTER` (abi 4+), `RX_FAST_FRAMES` / `RX_FAST_TRAIL` (abi 5+, VM-only), `RX_DFA_TABLE` (abi 7+), and `rx_info.scan` / `.prefilter` (abi 6+, appended fields) — never inferring an engine from a stamp's ABSENCE (I-5's hazard); METADATA_DECL grows the same way. Reporter: the DFA mechanism columns; I-7 §3's two legend rules (an unstamped pin's engine printed as "inferred"; a give-up code that names the other engine, or a compile-cost class that contradicts it, turns a cross-pin Δ into "selection changed"); I-7 §5's "max is trial 1" fact beside jitter and the "dominated" flag on a set-grain ratio when one subject is >90 % of the sum. Then THE WINDOW (the manager runs it): six cells + the floor pattern at `email-specimen@0.1` against the 692c2e8 records — the ledger of predictions P1-P7 (I-7), P2's exact figure (I-8), P8'-P11' (I-11) tested one by one in the report/journal; the pinned floor row (P7). Reports re-rendered.
- [B17] STATE:started — NON-PERIODIC THROUGHPUT SUBJECTS (inbox I-10): `bench/email` gains at least one non-periodic 1 MB subject per throughput construction (matching-bearing prose with drawn word lengths and a low density of addresses; failing prose with no `@`), generated with a recorded seed, beside the periodic three (kept: they isolate the steady-state loop); `manifest_throughput.tsv` gains a `periodic` column (the period in bytes, or `no`) so the interpreter can flag "branch-predictor-friendly" beside a per-byte number; expectations re-derived. A SUBJECT change bumps the version (requirements §5): `email-specimen@0.2`; measured for the throughput regime in a second window after [B16]'s at 0.1 (the cross-pin ledger stays at 0.1; the periodic/non-periodic contrast is within-pin at 0.2).
- [B12] STATE:not-started — M1 CLOSE ITEMS (candidates, unordered):
  the M1 close panel (D6) over harness_contract.md + harness_notes.md +
  the report; U1's discriminating measurement (the pcre2 INTERPRETER
  with PCRE2_NO_START_OPTIMIZE on the same cell, K34-probe shape; then
  the pcre2test reproduction — docs/dev/upstream_findings.md); OD-B10
  (1 MB vs 8 MB spread).

- [B13] STATE:not-started — THE INTERPRETER (Frank, 2026-08-25: "reads
  and provides interpretation to these reports as an add-on … no
  opinions, all based on facts"; agreed design, journal part 5). Two
  parts: (1) a DETERMINISTIC fact-finder, `pcrecbench interpret`, reading
  the report TSV + store/index.tsv (never the markdown), emitting the
  FIRED RULES with rows, numbers and record ids, plus the rules that did
  NOT fire; a versioned RULE CATALOGUE (id, definition, threshold WITH
  its source — spread-based, never a magic number — a worked example
  from a real report): status caveats (inconclusive-load, excluded
  cells, give-ups with code + subject), cross-pin deltas beyond spread,
  rank flips vs the reference arm, ratios inside the timer floor,
  PREDICTIONS vs OUTCOMES (the inbox's stated expectations as input:
  confirmed / refuted / result no prediction covered), registered
  buckets (known readings that are facts with a source, e.g. the `\z`
  regime artifact per feedback 2a); `make check-interpret` (same input →
  same facts; a sabotaged report fires the rule its name claims). (2) a
  project skill `/pcrec-bench-interpret <report>` that phrases the fired
  rules into a SIDECAR `reports/<name>.interpretation.md` stamped with
  the report's sha256 and the catalogue version — never a section in the
  report (the reporter stays deterministic and diffable); committed
  beside every report. OPINION FIREWALL: every sentence cites a fired
  rule; hypotheses appear only as LINKS to where they are already
  recorded (outbox, known_issues), never generated. Sits after [B9]
  (needs OD-B14 status per row and OD-B15 pooled-vs-newest). Frank:
  "let it sit a bit before we do it." INPUT TO COLLECT FIRST: pcrecdev1's
  feedback on the repin report as it reads — actionability and
  interpretation (outbox O-5; answer → docs/dev/feedback_pcrecdev1_
  <date>-repin.md, cited here). Blinded first test: catalogue v1 must
  find, unprompted, the collapse, the three inconclusive records, the
  give-ups and the vm-in result in the two existing reports.
- [B7] STATE:not-started — ROSTER EXPANSION (APPROACH §4): RE2, Rust
  `regex`, Oniguruma, TRE (POSIX-tagged), Vectorscan (semantics-tagged),
  python `re`, perl; the hand-C ceiling arm (pcrec [BENCH-CEIL]'s testee
  triple). One adapter per lane; each admits with its semantics recorded.
