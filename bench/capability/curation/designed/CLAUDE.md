# bench/capability/curation/designed/ — L2's designed-member staging area

Staging output of lane `b42author` ([B42] restart step (5), L2 in
`docs/design/capability_set_v1.md` §11.1): families 7-12's DESIGNED
members, plus every families-1-6 control twin (§3.2). NOT the set
itself — `bench/capability/`'s real sidecar, generators and manifests are
L3's build, against whatever `.rxt` delivery the restart landed (see
`docs/design/capability_set_v1.md` §9/§11). This directory is INPUT to
that build, not a substitute for it.

**Authored BLINDED per pcrec D27**: `man pcre2pattern` and public engine
documentation, `docs/design/capability_set_v1.md`, and
`docs/design/requirements.md` only. No `testees/`, no
`pcrecbench/adapters.py`, no `store/`, no `reports/`, no ledgers, no
other lane's worktree, no existing `bench/*/` pattern file was read. Full
blinding statement in `docs/dev/lanes/b42author_report.md`.

## Files

- `members.tsv` — one row per L2-authored pattern: `family`, `pattern_id`
  (the proposed slug), `fidelity` (always `synthesized` here — nothing in
  this directory is a verbatim or adapted import; those are L1's), the
  pattern text inline (`canonical_text`) or a pointer to `text_file`
  under `patterns/`, `requires` (the §5.1 closed REQUIRES vocabulary,
  `;`-separated, `-` for none), `hazard_class` (per CB7's per-family
  assignment — `exponential-backtracking` on families 2 and 10's members
  only, `none` elsewhere), `inspiration` (the real source or documented
  bug class cited, never a source this pattern was copied from), and for
  every control twin: `twin_of` and `isolates` (which member it pairs
  with and the single property the pair separates). A `notes` column
  carries caveats, chiefly the families-1-6 twins' pairing uncertainty
  (see below).
- `patterns/` — one raw-bytes file per member too long or too
  byte-sensitive for a TSV cell: the two genuinely multi-line free-
  spacing bodies (`bracket-array-define.txt`, `codegrammar-xflag.txt`,
  both `(?x)`, kept multi-line per Frank's F-Q2 ruling — never
  flattened) and the one member whose canonical text is a real literal
  non-UTF-8 byte sequence (`mojibake-curly-quote.txt`, 0x93/0x94), which
  is why it OMITS `canonical_text` in `members.tsv` per S10's rule.
  `SHA256SUMS.txt` records a staging-only sha256 per pattern (inline
  cell bytes or file bytes) for identity tracking; it is NOT necessarily
  the schema's own `canonical_sha256` convention, which L3 must
  re-derive when it builds the set for real.
- `NOTES-draft.md` — 1-3 sentences per family stating the designed
  members' contrast, feeding L3's own `NOTES.md` verbatim or near-
  verbatim.
- `CLAUDE.md` — this file.

## What is NOT here, and why

- **Family 3 (`wild-waf`), 4 (`wild-secrets`), 5 (`wild-datetime`)**: the
  design's own §3.1 table states `none` in their "designed members"
  column ("the imports ARE the edge cases" / verbatim import suffices /
  no authored fallback needed). Nothing to author.
- **Expectations, the oracle, scoring**: explicitly out of scope per this
  lane's brief — that machinery is L3's/the harness's, and family 11's
  own convention-scoring gap (CB1) is unbuilt regardless.
- **A confirmed reconciliation against L1's actual wild imports**: L1 ran
  concurrently and blinding forbids reading its output before this
  lane's own patterns were committed. The four families-1-6 twins
  (`uuid-near-miss`, `base10num-near-miss`, `winpath-near-miss`,
  `ipv4-near-miss`) are best-guess pairings against the NAMED grok
  macros and the family's own stress-mechanism description, not a
  confirmed match — `members.tsv`'s `notes` column and
  `b42author_report.md` both flag this. L3 owns the reconciliation once
  L1's `provenance.tsv` exists.
