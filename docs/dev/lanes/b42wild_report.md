# Lane report: b42wild

Branch `lane/b42wild`, off master at `0d6e919`. Read-only online survey
lane for [B42] phase (a), research note 1 ("regexes in the wild").

## What I did

- Read `docs/dev/plan.md`'s `[B42]` row (the charter), `APPROACH.md`
  §§1-5 (mission, principles, architecture, testee roster / the [B7]
  roster), and skimmed `bench/syntax/NOTES.md` + `bench/syntax/CLAUDE.md`
  (the existing construct census) before starting, per the brief.
- Ran an online survey (WebSearch + WebFetch) of 18 sources: rebar,
  mariomka/regex-benchmark, regex-redux, RE2's own benchmark file, the
  Rust `regex` crate's `testdata/`, Hyperscan/Vectorscan, Snort/Suricata
  rule sets, ModSecurity OWASP CRS, the OWASP Validation Regex
  Repository, Elastic/Logstash grok patterns, regexlib.com, Davis et
  al.'s polyglot regex corpus (ESEC/FSE 2019), Chapman & Stolee (ISSTA
  2016), ReDoS-specific corpora/tooling (`vuln-regex-detector`,
  `awesome-redos-security`), PCRE2's own testdata, Oniguruma's test
  suite, GNU grep/sed's test suites, and TextMate grammars.
- Wrote `docs/dev/research/2026-09-12-b42-rx-in-the-wild.md` (the
  filename the charter's `docs/dev/research/CLAUDE.md` table already
  names — I did not edit that CLAUDE.md, per the brief's instruction
  that another lane owns it) with, per source: URL(s) fetched, licence,
  dialect, size, real-vs-contrived evidence, subject/haystack data and
  its licence, edge-case value, importability, and 3-6 verbatim sample
  patterns where the licence permits (obtained for: rebar, mariomka,
  RE2, OWASP validation-regex, grok patterns, regex-redux — six of the
  eighteen; the rest either had no quotable content fetched or are
  evidence-only academic sources, stated honestly per source).
- Added: (i) a ranked shortlist of 13 entries with what each
  contributes; (ii) a proposed family taxonomy (19 rows) crossing
  mechanism against the [B7] roster's expected `unsupported` engines;
  (iii) an edge-case catalogue (11 shapes) each with a cited source;
  (iv) what the five existing bench sets (`bench/syntax`, `bench/
  altwide`, `bench/bounded`, `bench/loglines`, `bench/email`) already
  cover, so the design note doesn't duplicate; (v) five questions for
  Frank (licensing floor for copyleft/mixed-licence sources, wild-vs-
  designed ratio, subject-data provenance for wild patterns, the Davis
  corpus's availability specifically, and whether a new "regex-set
  matched in priority order" measurement shape is in scope for v1).
- Closed two of the OWED items myself once the first draft was
  committed (both cheap, both improved the note materially): fetched
  PCRE2's actual `LICENCE.md` (BSD-3-Clause WITH PCRE2-exception,
  confirmed) and its `testdata/` directory listing (29 testinput/
  testoutput pairs + grep/fuzzing files, 60+ total), and fetched
  Oniguruma's `COPYING` (BSD 2-Clause, confirmed) — both were "well
  known but not verified this session" items in the first draft; now
  independently fetched. Committed as a second, separate commit so the
  first draft's honesty statements remain checkable against what
  actually changed.
- Committed incrementally: one commit for the research note, one for
  the two closed OWED items.

## What I could not do (still OWED, named in the note's closing section
too)

- Davis et al.'s actual corpus artifact/download (only the arXiv
  abstract page was reachable; no Zenodo/GitHub link surfaced this
  session) — the single biggest unresolved item, since that corpus
  (537,806 real regexes, 8 languages) is potentially the highest-value
  source in the whole survey if its licence permits use.
- Chapman & Stolee's paper body and any released dataset (ACM
  paywalled).
- The cited ReDoS Zenodo artifact's content and licence.
- regexlib.com's actual pattern-database content (found the live site
  and its site-source GitHub mirror, not a data export).
- Oniguruma's actual test file content (its licence IS now confirmed;
  the test file itself was not located).
- GNU grep's own `tests/` tree location (only gnulib's shared
  `regex.c`/`.h` found); its GPLv3 licence is flagged prominently in
  the note as a real import-scope question for Frank, separate from the
  content gap.
- A `pcre:`-bearing Suricata rule file (the one rules file I fetched
  had none — a real, reported result, not a failure, but it means no
  Suricata sample pattern is quoted).
- ModSecurity CRS and TextMate grammar file content (project/licence
  confirmed for CRS; no rule/grammar file content fetched for either).
- Independent LICENSE-file fetches for Hyperscan/Vectorscan, rust-lang/
  regex, GNU grep, Elastic's plugin, and ModSecurity CRS (stated from
  well-known general knowledge or a WebSearch snippet instead, flagged
  individually in the note).

None of these block the deliverable — the brief asked for an honest
survey with a shortlist and open questions, not a complete corpus
import, and every gap above is named in the note itself (its final
section) as well as here.

## Charter-vs-committed checklist (session_discipline.md §7(c) shape)

| brief item | status |
|---|---|
| Read plan.md [B42] row, APPROACH.md §1-4, skim bench/syntax | DONE |
| Survey rebar (defs, real-world haystacks, unsupported-engine handling) | DONE — FORMAT.md + one benchmark file fetched |
| Survey mariomka/regex-benchmark | DONE |
| Survey regex-redux | DONE (WebSearch only, not independently WebFetched — noted) |
| Survey RE2 testdata/benchmarks | DONE — `regexp_benchmark.cc` fetched |
| Survey Rust regex crate bench/test suites | DONE (directory-level; not every TOML file opened) |
| Survey Hyperscan/Vectorscan corpora + "regex set" workloads | DONE at the tooling/capability level; no public pattern corpus found to characterize further (named) |
| Survey Snort/Suricata community rules (pcre:) | DONE; licence is mixed by rule range (flagged prominently); no `pcre:` sample fetched (OWED) |
| Survey ModSecurity OWASP CRS | DONE at licence/project level; no rule content fetched (OWED) |
| Survey Elastic/Logstash grok pattern libraries | DONE — 40+ patterns fetched verbatim |
| Survey OWASP validation-regex repository | DONE — patterns fetched verbatim, licence (CC BY-SA 4.0) confirmed |
| Survey regexlib.com / RegExr community patterns | DONE at site-existence level; no pattern content, licence unresolved (named) |
| Survey RFC validators as commonly deployed | Folded into the OWASP validation-regex + grok entries rather than a separate source; not separately surveyed as its own category |
| Survey Davis et al. / Chapman & Stolee / ReDoS corpora | DONE at abstract/metadata level; no corpus content (biggest OWED item, flagged as a question for Frank) |
| Survey PCRE2's own testdata | DONE — licence + directory listing confirmed by direct fetch |
| Survey Oniguruma's tests | DONE at licence level; test file content not located (OWED) |
| Survey GNU grep/sed test suites | Partial — repo located, test suite tree not confirmed, licence (GPLv3) flagged as a real scope question |
| Survey "any others judged relevant" (browser trees, WAF rules, TextMate grammars, linters) | DONE for TextMate grammars specifically; browser source trees and other WAF rule sets not separately surveyed (time budget) |
| Per-source: name/URL/licence/dialect/size/evidence/subject-data/edge-case-value/importability | DONE for all 18 |
| 3-6 verbatim samples per source where licence permits | DONE for 6 of 18 sources; rest either evidence-only or content not fetched (named per source) |
| (i) shortlist ranked | DONE — 13 entries |
| (ii) family taxonomy with expected per-engine `unsupported` | DONE — 19 families/rows |
| (iii) edge-case catalogue with a source per shape | DONE — 11 shapes |
| (iv) what existing bench sets already cover | DONE |
| (v) questions for Frank | DONE — 5 questions |
| Honesty about what could not be fetched | DONE — a dedicated closing section, plus per-source flags throughout |
| Deliverable at the named path | DONE — `docs/dev/research/2026-09-12-b42-rx-in-the-wild.md` |
| Did not edit `docs/dev/research/CLAUDE.md` | CONFIRMED — untouched |
| Commit incrementally | DONE — 2 commits |
| Lane report committed | DONE — this file |
| No merge | CONFIRMED — not merged, branch is `lane/b42wild` |

## Validation

This is a research lane: no build, no tests, no measurement to run. The
"validation" here is the honesty discipline itself — every claim in the
note is marked fetched-this-session vs. recalled-vs-search-snippet, and
the closing section names every gap. Two of the original "recalled, not
fetched" flags (PCRE2 and Oniguruma licences) were closed by direct
fetch in a second commit before this report was written, so the note's
own honesty markers are internally consistent with what was actually
verified at report time.

## Files touched

- `docs/dev/research/2026-09-12-b42-rx-in-the-wild.md` (new)
- `docs/dev/lanes/b42wild_report.md` (this file, new)

No other files in the worktree were modified.
