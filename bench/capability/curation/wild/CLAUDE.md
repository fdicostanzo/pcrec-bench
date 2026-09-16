# bench/capability/curation/wild/ — L1's delivery: families 1-6's wild members

Twenty-six wild candidate members for the capability survey set's six
"wild" families (`wild-validator`, `wild-logparse`, `wild-waf`,
`wild-secrets`, `wild-datetime`, `wild-codegrammar`;
`docs/design/capability_set_v1.md` §3.1). This is NOT the sub-bench —
there is no manifest, no oracle expectation, no `pattern_id` collision
check against a live `patterns.rxt` yet. L3 selects from and builds on
this table; it does not have to take every row.

Per lane brief and `docs/design/capability_set_v1.md` §4.1, every member
is one row in `members.tsv` plus, for a multi-line or otherwise
byte-hairy body, a sidecar file under `patterns/`.

## `members.tsv`

Tab-separated, one header row, one row per candidate member:

| column | what it is |
|---|---|
| `family` | one of the six wild family ids above |
| `pattern_id` | proposed slug, `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$` |
| `fidelity` | `verbatim` / `adapted` (closed vocabulary per the 2026-09-16 r6 correction, R6-1 — `synthesized` does not appear in this table since L1 imports and adapts, never authors from a description) |
| `hazard_class` | per §3.1's per-family table (`exponential-backtracking`, `ambiguous-decomposition`, or `none`) |
| `source_name` | a source slug. Two of §4.1's pre-registered eleven are used here (`owasp-validation`, `grok`, `crs`, `rebar-wild`, `vscode-json-grammar`); **one row uses `moment-js`, which is NOT in that pre-registered list** — see the lane report, this is a finding for L3/Frank, not silently folded into `authored` (moment.js's text is imported, not ours) |
| `source_url` | the exact URL this lane fetched (raw where a raw URL exists) |
| `source_ref` | the file/line/JSON-path inside the source |
| `license` | SPDX id (spelled `license`, not `licence` — the lane brief's explicit correction) |
| `license_note` | populated where something needs flagging (the `moment-js` slug gap; the delivered format's provenance schema draft's own gap) |
| `retrieved_utc` | RFC 3339, the fetch that produced the row's text (all rows: `2026-09-16T04:49:00Z`, one curation session) |
| `adaptation` | required and populated where `fidelity = adapted`; the one-sentence, reviewer-checkable description of the mechanical change |
| `attribution` | populated where the licence demands it (the four OWASP CC BY-SA 4.0 rows) |
| `text_location` | `inline` (the `pattern_text` column carries it) or `wild/patterns/<pattern_id>.txt` (multi-line bodies — the two VS Code `(?x)` patterns) |
| `canonical_sha256` | sha256 of the pattern text's exact bytes (UTF-8), whichever column/file carries it |
| `pattern_text` | the pattern, inline, for every row except the two `text_location != inline` rows (empty there) |

No row's pattern text contains a literal tab or newline byte — checked
at generation time (an assertion, not a hand audit) — which is why 24 of
26 rows are inline rather than sidecar files. The two VS Code entries
(`wild-codegrammar-json-number-extended`,
`wild-codegrammar-json-stringcontent-escape`) are genuinely multi-line
`(?x)` bodies with their own inline comments and are kept multi-line in
their sidecar file, verbatim, per Frank's F-Q2 ruling (never flatten a
free-spacing body to one line).

## `patterns/`

One file per multi-line/byte-hairy member, raw bytes, no trailing
newline added beyond what the source itself carries at that point in its
own file.

## `fetches/`

The fetched excerpts and full LICENSE/UNLICENSE texts backing every
`license` claim in `members.tsv`, each with a `Source:`/`Retrieved:`
header (D35 spirit): five LICENSE files fetched directly (Unlicense —
rebar; MIT — VS Code, moment.js; Apache-2.0 — grok's
`logstash-patterns-core`, OWASP CRS's `coreruleset`), one page-footer
excerpt (OWASP Validation Regex Repository's CC BY-SA 4.0 statement —
this source has no repo-level LICENSE file, only the wiki page's own
footer), and five source-content excerpts (the grok base patterns used,
the five CRS SecRule blocks in full, the four noseyparker.txt lines
used with their line numbers, the moment.js file's opening lines, and
the VS Code grammar's five imported JSON entries). `date.txt`'s own
excerpt is a fetch-provenance note only — that member IS the whole
6,348-byte file, already carried in full in `members.tsv`'s
`pattern_text` column, not duplicated in `fetches/`.

Every quoted line/rule/JSON value in `members.tsv` and `patterns/` was
either read straight out of a parsed source file (grok's dict lookup,
the parsed VS Code JSON, `date.txt`'s own bytes — no hand-transcription
possible) or, where a value WAS hand-transcribed into the generator
script (the five CRS rules, the four noseyparker lines, the three OWASP
patterns, the one moment.js pattern), independently re-verified
programmatically against the raw fetched file before being written —
see the lane report for the verification method.
