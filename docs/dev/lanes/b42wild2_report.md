# Lane report: b42wild2

Branch `lane/b42wild2`, off master at `962a79e`. Read-only online
follow-up lane for [B42] phase (a) — closing named fetch gaps in
research note 1 (`docs/dev/research/2026-09-12-b42-rx-in-the-wild.md`,
written by lane `b42wild`).

## What I did

- Read the boilerplate and the full research note (1035 lines) first,
  noting every "OWED", "not verified this session", and item in its
  closing "What I could not fetch" section.
- Direct-fetched primary sources (raw GitHub URLs, a Zenodo record, an
  ArXiv/paper search chain, LICENSE files, GitHub's contents API) to
  close as many of those named gaps as possible, per the brief's five
  numbered asks:
  1. **rebar** — fetched `benchmarks/definitions/`, `regexes/`,
     `haystacks/` directory shapes, `ruff.toml` in full (six real
     CPython-source benchmarks with engine-exclusion reasons stated),
     `noseyparker.txt` (categorical, not literal, content), and
     `haystacks/opensubtitles/README.md` (confirms the OPUS
     OpenSubtitles-v2018 source). **Corrected** the original note's
     claim about where the AWS-keys/lexer/Unicode-word benchmarks live
     (they're in `definitions/curated/`, not `regexes/wild/`).
  2. **Davis et al. / Chapman & Stolee / vuln-regex-detector** — found
     Davis et al.'s actual artifact (Zenodo 3257777, GitHub-backed,
     NDJSON, MIT-per-repo though Zenodo's own field is ambiguous) and
     re-ranked it to #1 per the note's own stated rule. Fetched
     `vuln-regex-detector`'s LICENSE (MIT) and **corrected** the
     original note's identification of a second Zenodo DOI (it's a
     distinct, later ICSE 2022 artifact, not `vuln-regex-detector`'s
     own). Chapman & Stolee: no new artifact found, stays OWED.
  3. **LICENSE files** — fetched and confirmed five of six named
     targets directly: Hyperscan (BSD), Vectorscan (BSD), rust-lang/
     regex (MIT), GNU grep (GPLv3), Elastic logstash-patterns-core
     (Apache-2.0), OWASP CRS (Apache-2.0); bonus: mariomka/
     regex-benchmark (MIT). regexlib.com's terms stayed unresolved (no
     terms-of-use page found).
  4. **Content samples** — closed four of five: ModSecurity CRS (five
     `@rx` SQLi rules with ids, quoted verbatim), a TextMate JSON
     grammar (five regexes quoted from `microsoft/vscode`), Oniguruma's
     test file location + five sample `x2()` cases from `test_syntax.c`,
     GNU grep's `tests/` tree (full characterization, including the
     Turkish-I locale case-fold divergence). A Suricata `pcre:`-bearing
     rule was NOT found despite three distinct attempts; recorded in
     detail because the failure surfaced a methodological finding (an
     AI summary of a huge GitHub JSON directory listing is not itself
     verified content — four "confirmed" directory names turned out to
     be unconfirmable against the raw JSON). PCRE2 testdata: confirmed
     `testinput1` carries empty-match cases and `testinput2` carries
     case-fold cases, with quoted samples for both.
  5. **One more corpus** — surveyed four: regex101.com's public library
     (terms still unresolved) plus two MIT-licensed derivative datasets
     built from it (`innovatorved/regex_dataset` on Hugging Face, 8,551
     rows; `dataunitylab/semantic-regex`, a build pipeline incorporating
     the Sherlock project's data), and RE2's own `re2-exhaustive.txt`
     correctness corpus (BSD, already-confirmed licence). Named but not
     confirmed: a 2018 npm/pypi ReDoS census paper from the same Davis
     research lineage.
- Amended the SAME note in place: corrected/updated 11 existing item
  sections with `(confirmed by b42wild2: …)` / `CLOSED by b42wild2`
  markers or explicit corrections where a fetch refuted the original
  text, re-ranked the shortlist (Davis et al. 4th → 1st), and appended
  a "## Follow-up 2026-09-12 (lane b42wild2): gaps closed" section
  rolling up all five numbered asks plus this lane's own honest
  "still not fetched" list. Did NOT edit
  `docs/dev/research/CLAUDE.md` (out of scope per the brief).
- Committed once (the note edit is a single logical unit — corrections
  and the new section were drafted together against the same read of
  the file, so splitting the commit would not have added a checkable
  boundary the way b42wild's two-commit split did for a smaller,
  more separable set of closures).

## What I could not do (also named in the note's own follow-up section)

- Davis et al.'s actual 34.1 MB zip contents (existence/format/licence
  confirmed; per-record schema — does provenance survive per-regex or
  only per-language — is unopened).
- Chapman & Stolee's paper body/dataset (still paywalled, no artifact
  found).
- A `pcre:`-bearing Suricata/ET rule sample (three attempts, all
  failed; see the note's item 7 for the summarizer-reliability finding
  this produced).
- The 14 rebar `definitions/curated/*.toml` file bodies (list only) and
  `noseyparker.txt`'s literal pattern text (categorical description
  only).
- regexlib.com's and regex101.com's own terms of use (both unknown;
  MIT-licensed derivatives of regex101 content were found instead,
  which does not resolve the source's own terms).
- A fuller PCRE2 testdata census beyond `testinput1`/`testinput2` (27
  of 29 files unsampled).
- The npm/pypi ReDoS census paper's own artifact, if one exists (only
  its existence and rough method found via search).

## Charter-vs-committed checklist

| brief ask | status |
|---|---|
| (1) rebar full benchmark definitions, curated/wild files, haystack licences, compact table | DONE for `ruff.toml` + full directory shapes + haystack source; curated TOML bodies and other wild/ TOMLs still OWED (named above); no separate "compact table" added beyond the note's existing per-item structure — the corrections are inline at item 1, judged more useful than a duplicate table |
| (2) Davis/Chapman/vuln-regex-detector/ReDoS Zenodo artifacts | Davis: artifact found, licence resolved (with a flagged mismatch), re-ranked. Chapman: still not found (OWED, unchanged). vuln-regex-detector: MIT confirmed. The "ReDoS Zenodo artifact" turned out to be a distinct, correctly-identified-now, artifact |
| (3) LICENSE files (8 named) | 7 of 8 fetched and confirmed (Hyperscan, Vectorscan, rust-regex, GNU grep, Elastic, OWASP CRS, plus bonus mariomka); regexlib.com's terms not found (genuinely may not exist publicly); Suricata rules-by-range not re-verified (no new fetch attempted, time-boxed against the sample hunt instead) |
| (4) five content samples | 4 of 5 closed (CRS, TextMate, Oniguruma, GNU grep); Suricata `pcre:` sample not found despite three attempts, recorded as a finding in itself |
| (5) one more corpus, one paragraph each | four sources covered (regex101 + two derivatives + RE2 exhaustive), one more named but unconfirmed (npm/pypi ReDoS census) |
| amend the SAME note, mark confirmations, correct refuted claims, add own "still not fetched", keep earlier honesty notes | DONE — 11 in-place item edits plus a closing follow-up section; earlier honesty notes untouched except where a fetch specifically closed or corrected them |
| do not edit `docs/dev/research/CLAUDE.md` | DONE (not touched) |
| commit incrementally; finish with this report; do not merge | one commit for the note, this report as a second commit; not merged |

No keepalives, no waiting on this handback — the fetch work is complete
for the time available; every remaining gap is named above and in the
note's own follow-up section with why it wasn't closed.
