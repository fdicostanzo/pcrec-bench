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

- [B11] STATE:started — (2026-08-28: #2 DONE as [B11.1], archived. 2026-08-29: #4 BOUNDED-REPEAT ruled NEXT — inbox I-14 (iv) recommended, I-15 (c) and I-17 (c) confirmed with Frank's "advance these bench requests" — expanded as [B11.4] below; #3 wide alternations follows it as [B11.2]; Frank's ruling that the pcrec manager may run bench sessions AS the bench when pcrecdev2 is down — one repo per session) SUB-BENCHES #2..#6, in Frank's ruled order
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
- [B18] STATE:started — RE-PIN pcrec **36d5963** (abi 11; inbox I-17 superseding I-15 8ab6152 abi 9 and I-16 808740c abi 10) — lane b18repin, 2026-08-29. ONE adapter change absorbing three pins, as [B16] did: (e) `shim.c`/`adapter.py`/`driver.c` read the abi 9-11 stamps BY VALUE — `RX_DFA_PREFILTER`'s new values `offset-set` / `offset-set-bounded` (I-15), the unconditional `<P>_DFA_PREFILTER_OFFSETS` (`"0,8*,13"` / `"none"`), `RX_DFA_MATCH` ∈ {`unwrapped`, `search-filter`} on DFA artifacts only + `rx_info.match_form` (I-16), `<P>_MAX_EMIT_CODE_BYTES` / `<P>_MAX_EMIT_BYTES` on every artifact and `<P>_UNROLL_K` / `<P>_UNROLL_K_WHY` (seven values) on every VM artifact (I-17); the deny flags `-fno-offset-skip` (bit 16), `-fno-anchored-dfa` (bit 17), `-fno-size-term` (bit 18) as the CONTROL builds; the flag/stamp map derived from (or checked against) `pcrec --list-axes` (47 rows / 19 axes at abi 11) instead of a hand table; `PB_SHIM_MIN_ABI` raised iff the shim reads a field appended after 6; `make check-harness` asserts the new stamps by value on a real artifact of each kind (a k-set skip artifact — loglines `uuid` should stamp `"0,8*,13"`, `iso-ts` `"0,4*"`, `stack-frame` `"0,1*"`; a declined one `"none"`; `unwrapped` vs `search-filter`; `K=8`/`default`), the `-fno-*` controls reaching the other value, and the sabotaged-abi refusal as before; the [SEL-1] fallback: loglines `level-context` under `pcrec-auto` now COMPILES as a VM artifact with `RX_ENGINE_WHY "dfa overflowed: …"` — the reporter must bucket it (the mechanism stamp), and [B12]'s did-not-compile ranking line stays for the next such cell. (a) THE WINDOW: re-measure email-specimen@0.2 (six cells) and loglines@0.1 (six cells) at 36d5963 into `store/`; reports `reports/2026-08-29-*-repin-36d5963.*`. THE LEDGER (pcrec's stated predictions, read PER SUBJECT against the 35e1ab1 records): [OPT-K] on loglines search band — stack-frame 10.18×/6.19× (match/fail arms), uuid 4.45×/9.58×, iso-ts 6.13×/5.75× faster than at abi 8; ipv4 1.02×, hex32-id 1.00×, http-5xx 1.01× (controls within spread); ipv6/kv-quoted/bignum declined (`"none"`); the three outliers to within 2× of pcre2-jit on the search band (I-14 (ii)); BOTH email patterns declined — email search rows flat; DFA artifacts +1.4-1.9 KB where selected, +40 B declined; gcc time ±5 %. [ENG-ABS] on email MATCH regime — matching subjects DFA/VM 1.031× [r41 1.036×] from 2.077×; the 35 short valid emails 0.482× [0.489×] (DFA 2.07× faster than VM, from 1.207× behind); ALL 85 2.132× → 1.161×; non-matching 2.306× → 1.550×; SEARCH rows flat (nothing in `_search` moved at abi 10 or 11); DFA artifacts +2,605 B source median but `.o` +2-11 % of that; VM +63 B. [ART-SIZE]: 54/54 bench emits accept, 0 K movements (every VM artifact `K=8`/`default`), largest artifact 76,304 B, `level-context` 22,905 B; ordinary compile cost unchanged. (b) FRANK'S ASK (I-15 b, I-17 b): for every pattern where auto's DFA fallback trips (`RX_ENGINE_WHY` starts "dfa overflowed"), pcrec-auto (a VM artifact) vs pcre2-jit — `level-context` first, out of the loglines window (at 35e1ab1 the VM was 1.55 ms/set vs the JIT's 115 µs, 13.4× behind — the prediction is that pcrec-auto now equals pcrec-vm there). (d) I-16 (c) / I-17 (d): a LONG-SUBJECT FAILING-`_match` probe — a failing anchored match at byte ~3 of a 1 MB subject (pcrec: 5.5 ns flat at every length vs 1.99 ms before, O(divergence)); bench/email's `throughput` regime is search-only and adding `match` to it would bump the version and break (a)'s comparability, so this is a SCRATCH-tier probe first (`quick` if it can address the throughput subjects in the match regime; else an archived driver probe, D35 style) reported in O-8, and a set change only as a ruled item. Outbox O-8 carries the ledger outcomes, the fallback row and the probe.
- [B11.4] STATE:started — SUB-BENCH #4: BOUNDED-REPEAT (`bench/bounded/`, 2026-08-29, lane b114bounded, a BLINDED author — D27 discipline as [B11.1]). THE NUMBERS THIS ROW EXISTS TO PRODUCE: (1) the COMPILE axis of bounded repeats — pcrec's counter-rung body replication under NESTED bounded repeats is where every artifact-size outlier in pcrec's own census lives (inbox I-15 (c): `.o` median 6.8 KB / p99 14 KB over 2,772 patterns; I-17: two size caps + a K ladder now decide the artifact, and the `.o`-size column on THIS set is the design input for the size term); (2) the MATCH axis in the K23/K32 band — a bounded lazy repeat before a `\b` alternation reaching the DFA's 32,000-state cap under `auto` (loglines `level-context`, the [SEL-1] witness) and large DFA-side counts like `[a-z]{0,30000}` (pcrec [ENG-COUNT], filed unscheduled 2026-08-29, "would find its measured need here if one exists"); (3) the give-up / refusal as a FIRST-CLASS outcome with the count at which it first fires (I-2 §1b: a count sweep, not a size sweep, is this set's sweep). Shape: everyday shapes with bounded counts (fixed-width fields `\d{4}`, hex ids `[0-9a-f]{32}`, line-length and password rules `.{8,64}` / `.{80,}`, a bounded-context "error … cause" shape `.{0,200}?`), plus a count LADDER on a few skeletons (greedy/lazy, class/literal/group body, nested `(?:X{a,b}){c,d}`, `{n}` / `{n,m}` / `{n,}`), counts from small to huge; every set carries the FLOOR pattern; expectations oracle-verified by the shared chain (`pcrecbench/expectations.py`, `--check`, sha256 manifests, `make check` by enumeration); subjects generated, non-periodic (`periodic` column), matching and failing arms both present; no pattern copied from pcrec's tests or corpora (the author is denied them). Measured in a window after [B18] lands so the number is at abi 11.
- [B12] STATE:not-started — M1 CLOSE ITEMS (candidates, unordered): [ADDED 2026-08-28] a DID-NOT-COMPILE cell must appear under its ranking table as `not ranked: <testee> — did-not-compile (<diagnostic>)`, not only in the compile-cost table (loglines/level-context under pcrec-auto vanished from the ranking, journal part 6); the window script's post-cell gate transient (a `sleep 15` before the first sample; every cell after the first needed a retry on 2026-08-28) belongs in a committed `scripts/run_window.sh` rather than a scratchpad copy;
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
