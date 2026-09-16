# Lane report: b42curate

Branch `lane/b42curate`. [B42] build lane L1 (import/curation) per
`docs/design/capability_set_v1.md` §11.1: fetch confirmed-permissive
sources for the capability survey set's six WILD families (1-6),
extract the wild members verbatim (or, where a mechanical adaptation is
needed, adapted with a stated one-sentence change), and record full
`docs/design/capability_set_v1.md` §4.1 provenance for every one. This
lane is NOT blinded — reading the sources is the task. It does not
build the sub-bench itself (that is L3), does not author families
7-12's designed members (that is L2), and touches nothing under
`pcrecbench/`, `testees/`, `schema/`, `store/` or any existing `bench/*/`
set.

## What I did

Read the boilerplate, `docs/design/capability_set_v1.md` §2-§4 and
Appendix A, and `docs/dev/research/2026-09-12-b42-rx-in-the-wild.md`
(the source survey, including its `b42wild2` follow-up) first. Then
direct-fetched (curl, not an AI-summarizing fetch tool — byte-exactness
was the point) every family-1-6 source the design note names, rather
than trusting the research note's already-two-sessions-old quotes:

- OWASP Validation Regex Repository (page, CC BY-SA 4.0 footer, three
  patterns re-extracted from the live page's own CDATA blocks)
- Elastic `logstash-patterns-core`'s `grok-patterns` file (raw, Apache-2.0
  LICENSE fetched directly) — read in full, not just the four lines the
  research note already quoted
- OWASP CRS's `REQUEST-942-APPLICATION-ATTACK-SQLI.conf` (raw,
  Apache-2.0 LICENSE fetched directly) — this closes Appendix A's one
  named gate on this lane ("CRS 942360's full text… re-fetch before
  use"): the current file's `942360` rule is complete, not truncated
- rebar's `noseyparker.txt` and `date.txt` (raw, Unlicense fetched
  directly) — this ALSO closes a gate Appendix A left open: contrary to
  the design note's own Appendix A row ("pattern text fetched? NO —
  categorical description only"), `noseyparker.txt` fetches as 96
  ordinary one-pattern-per-line regexes with no access restriction; the
  §3.1 table's claim that a prior pass (its "CB4/F1") already re-fetched
  and confirmed this appears, from this lane's own fetch, to be correct
  in substance even though the research note this lane could read still
  said "STILL NOT FETCHED" as of its own `b42wild2` follow-up — the
  discrepancy is moot now since this lane fetched it directly and
  quotes are verified below
- VS Code's `JSON.tmLanguage.json` (raw, MIT LICENSE.txt fetched
  directly) — re-fetched and re-parsed as JSON rather than trusting the
  prior HTML-flattened quotes, which matters here specifically because
  two of its five patterns are genuinely multi-line `(?x)` bodies
- moment.js's `src/lib/create/from-string.js` (raw, MIT LICENSE fetched
  directly) — a NEW source, not on N1/N2's shortlist, fetched because
  `wild-datetime`'s target of 2 members cannot be met from rebar's
  `date.txt` alone (see "Findings" below)

**Verification method**, stated because it matters for a lane whose
whole job is exact quoting: every value that could be read straight out
of a parsed source (grok's `name -> pattern` dict, the parsed VS Code
JSON, `date.txt`'s own bytes, the five CRS rules extracted
programmatically from the raw `.conf` by matching each `id:NNNNNN,`
line back to its own `@rx "..."` string) carries NO transcription risk
by construction. Everything else that was typed into the generator
script by hand (the four noseyparker.txt lines, the three OWASP
patterns, the one moment.js pattern) was independently re-extracted
programmatically from the raw fetched file straight afterward and
diffed against the hand-typed value; all matched byte for byte on the
first pass (no corrections needed — recorded here as a fact, not a
boast, since a mismatch would have been the more useful outcome).

## Findings (the kind this NOT-blinded lane exists to surface)

1. **§3.1's family-1/family-2 grok assignment has an internal
   contradiction; this lane resolved it by moving one pattern.** The
   design note's family-1 row imports "grok UUID/BASE10NUM/WINPATH…four
   quoted verbatim" and states family 1's expected-unsupported column as
   "**none** — every roster engine runs these; the point is the
   baseline everything else reads against." But `WINPATH`'s own text
   (`(?>[A-Za-z]+:|\\)(?:\\[^\\?*]*)+`) contains an atomic group
   `(?>...)` — exactly the construct family 2's row says makes RE2,
   Rust `regex`, Vectorscan and TRE refuse. Importing WINPATH into
   family 1 verbatim would silently break family 1's own stated
   invariant. This lane assigned WINPATH to family 2 instead (where its
   atomic group is the point, alongside BASE10NUM and QUOTEDSTRING) and
   kept only UUID (construct-free) in family 1. This also resolves the
   arithmetic cleanly: family 1 = 4 wild (OWASP ×3, grok UUID) against a
   target of 8, exactly matching "one near-miss twin per imported
   validator" × 4; family 2 = 6 members against a target of 6 exactly
   (see below). Flagged for L3/Frank to confirm or override.

2. **`wild-datetime`'s target of 2 members cannot be met from the
   sources the design note names.** rebar's `date.txt` is ONE single
   6,348-byte alternation (confirmed by direct fetch — there is no
   second date-shaped file under `regexes/wild/` or
   `definitions/wild/`); Appendix A and §3.1 name no second wild
   datetime source. This lane sourced a second one itself: moment.js's
   `extendedIsoRegex` (MIT), a real production ISO-8601 parsing regex
   with the same "ambiguous decomposition" character the family's
   `hazard_class` names. This is a NEW `source_name` — `moment-js` — not
   in §4.1's pre-registered eleven-slug enum. Recorded plainly in
   `members.tsv`'s `license_note` rather than folded into `authored`
   (which would misstate a verbatim import as ours). **Needs the slug
   registered** by whoever owns the delivered `.rxt` provenance
   production, or by this note's own next revision.

3. **A macro-expanded compositional member for family 2, matching its
   own stress-mechanism description more directly than the two atomic-
   group witnesses do.** Family 2's stress mechanism is stated as TWO
   things: "macro-expanded compositional alternation… atomic groups the
   original author added to fight backtracking." BASE10NUM/QUOTEDSTRING/
   WINPATH cover the second half; nothing in the design note's source
   list covers the first. This lane built `SYSLOGBASE` fully expanded —
   grok's own real log-line-prefix parser, five macro references
   expanded recursively through their OWN transitive macros (down to
   MONTH, HOUR, IPV6, POSINT, …) into one self-contained 1,947-byte
   pattern with real named groups — `fidelity: adapted`, citing exactly
   the example §4.1 already names ("a `%{NAME}` grok macro expanded").

4. **`spec's closed field-name spelling: `license`, not `licence`.**
   The design note's own prose spells the field `licence` throughout
   §4.1/§4.2 (British), but the brief's explicit correction ("note the
   spelling: license, not licence") was followed here — `members.tsv`'s
   column is `license`. Flagging because a reader of the design note
   who builds L3's schema mapping off its prose rather than the brief
   will spell it wrong.

## Per-family delivery vs §3.1's target counts

| family | target | delivered (wild) | shortfall / note |
|---|---|---|---|
| `wild-validator` | 8 | 4 | 4 designed near-miss twins (one per import) are OWED — not L1's scope per this lane's brief, and no lane in §11.1 is named for families 1-6's designed members (L2 is scoped to 7-12 only). Flagged as a lane-plan gap, not silently filled |
| `wild-logparse` | 6 | 6 | met exactly: 4 wild (BASE10NUM, QUOTEDSTRING, WINPATH, SYSLOGBASE-expanded) + 2 adapted atomic-group-removed controls (the design's own named control pair, in scope per the brief's "mechanical adaptation" example) |
| `wild-waf` | 5 | 5 | met exactly: all five CRS rules design names, none deferred |
| `wild-secrets` | 4 | 4 | met exactly: four structurally distinct noseyparker.txt patterns (AWS key alternation, GitHub PAT literal-prefix, Slack multi-segment webhook, generic username/password pair) |
| `wild-datetime` | 2 | 2 | met exactly, but via a source substitution — see finding 2 |
| `wild-codegrammar` | 5 | 5 | met exactly: all five VS Code JSON grammar entries the design names |
| **total** | **30** | **26** | four short, all in family 1, all explicitly deferred (not silently dropped) |

## Rejected / deferred candidates

- **Suricata/ET `pcre:` rules (family 12's real-use evidence).** Not
  this lane's family, but confirmed here (re-reading Appendix A and the
  research note) that no sample was ever obtained in three attempts
  across two prior sessions; not re-attempted this session since
  families 1-6 had confirmed-permissive alternatives.
- **GNU grep's `tests/` tree (Turkish-I fold, backref families).**
  GPLv3, licensing floor (c) forbids verbatim import; out of scope for
  families 1-6 anyway (it would land in families 7/10 if used at all,
  as `fidelity: synthesized` inspiration per the ruled licensing floor).
- **regexlib.com / regex101.com library content.** Terms of use still
  unresolved (confirmed unchanged from the research note); not a
  candidate for verbatim import under licensing floor (c), and no
  family 1-6 need was left unmet by it.
- **rebar's 14 `definitions/curated/*.toml` file bodies.** Never fetched
  in full by either research session or this lane (only the file
  listing); not needed once WINPATH/SYSLOGBASE closed family 2's target
  and moment.js closed family 5's.

## Deliverables (committed on this branch)

- `bench/capability/curation/wild/members.tsv` — 26 rows, header
  documented in `bench/capability/curation/wild/CLAUDE.md`.
- `bench/capability/curation/wild/patterns/` — 2 sidecar files (the two
  genuinely multi-line VS Code `(?x)` bodies, kept multi-line per
  Frank's F-Q2 ruling); the other 24 members are inline in
  `members.tsv` (verified to contain no literal tab/newline byte, so
  inlining is lossless).
- `bench/capability/curation/wild/fetches/` — 12 files: five LICENSE/
  UNLICENSE texts fetched directly (Unlicense, MIT ×2, Apache-2.0 ×2),
  one CC BY-SA 4.0 page-footer excerpt (OWASP has no repo-level LICENSE
  file), and six source-content excerpts backing the "pattern text
  fetched" claim for every row that isn't already self-evidently sourced
  (`date.txt`'s own excerpt is a provenance note only, since that member
  IS the whole file, already carried in full in `members.tsv`).
- `bench/capability/CLAUDE.md`, `bench/capability/curation/CLAUDE.md`,
  `bench/capability/curation/wild/CLAUDE.md` — all state plainly this is
  staging, not a runnable sub-bench; `bench/CLAUDE.md` gets one new
  paragraph noting `capability/` exists but is excluded from
  `subbench_dirs()` (confirmed by direct call, see Validation below) so
  it cannot silently break the generic gates.
- This report.

## Charter-vs-committed checklist

- Fetch confirmed-permissive sources for families 1-6 — **done**, six
  sources, five LICENSE files + one page footer fetched directly.
- Extract wild members verbatim — **done**, 20 of 26 rows `fidelity:
  verbatim`, independently re-verified against the raw fetch (see
  "Verification method").
- Record every §4.1 field for every member — **done**; two intentional
  gaps recorded IN the data rather than hidden: the `moment-js`
  unregistered source_name (finding 2) and family 1's shortfall against
  its target (deferred designed members, not this lane's scope).
- Mechanical-adaptation members with a one-sentence, reviewer-checkable
  adaptation — **done**, 3 of 26 rows `fidelity: adapted` (two
  atomic-group removals, one full grok macro expansion), each sentence
  names exactly what changed.
- `bench/capability/CLAUDE.md` + `curation/` described as staging —
  **done**.
- Lane report — **done** (this file).
- Nothing written under `pcrecbench/`, `testees/`, `schema/`, `store/`,
  or any existing `bench/*/` set — **confirmed** (see Validation).

Nothing is OWED by this lane. Family 1's four deferred near-miss twins
are explicitly NOT owed by L1 per the brief's own scoping ("you deliver
the raw materials for families 1-6's wild members"); they are named here
so L3/Frank can assign them rather than discover the gap late.

## Validation

- `python3 -c "...selfcheck.subbench_dirs()..."` from this worktree
  lists exactly the five pre-existing sets (`altwide`, `bounded`,
  `email`, `loglines`, `syntax`) — `capability/` is correctly absent, so
  this lane cannot have broken `make check-harness`'s generic gates.
- `members.tsv`'s 26 `pattern_id` values all match
  `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$` (checked programmatically at
  generation time).
- Every row asserted (at generation time) to contain no literal tab or
  newline byte in any TSV cell.
- `git status` on this branch shows changes only under
  `bench/capability/`, `bench/CLAUDE.md`, and this report — checked
  before commit.
