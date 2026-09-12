# [B42] research note 1: regexes in the wild

Read-mostly online survey for [B42] phase (a) (plan.md's [B42] row, Frank's
2026-09-12 charter, inbox — the successor to [B36]'s syntax census and
pcrec [BENCH-1]'s "capability map" intent). Requirement (1) of the charter:
patterns from the WILD where possible, provenance recorded per pattern.
This note surveys sources; it proposes nothing about set format or engine
handling (that is notes 2 and 3, and then the [B42] design note itself).

All URLs below were fetched this session (WebFetch/WebSearch), not recalled
from training data, EXCEPT where marked "not verified this session" — a
handful of well-known facts (mostly licenses) I already knew and could not
get a tool to confirm against a live page; those are flagged so the design
lane re-checks before relying on them.

## Method and honesty notes

- I read `docs/dev/plan.md`'s `[B42]` row and `APPROACH.md` §§1-4 before
  starting (mandate, principles, the testee roster in §5: libpcre2
  interp/JIT + pcrec committed; RE2, Rust `regex`, Oniguruma, TRE,
  Vectorscan, python `re`, perl in the design population — the "[B7]
  roster" the charter's family taxonomy asks me to reason about).
- I skimmed `bench/syntax/NOTES.md` and `bench/syntax/CLAUDE.md` (the
  existing syntax census) so §4 below states what is already covered
  rather than re-discovering it.
- I did NOT fetch: the actual TOML text of more than one rebar curated
  benchmark file, the Davis et al. corpus itself (I could not find a
  public download link in the time available — see its row), the
  Chapman & Stolee corpus (same), the GNU grep test suite's directory
  listing (Savannah's git web UI did not resolve for me; I have the
  gnulib regex module but not grep's own `tests/` tree confirmed), or
  regexlib.com's actual pattern rows (I found the site and its GitHub
  mirror of the *site source*, not a scrape of its pattern database).
  These are named as gaps, not glossed over.
- Every source below states what I read vs. what I am summarizing from
  a search snippet — WebSearch results are themselves summaries by a
  fetcher I don't control, so where I did not WebFetch the primary page
  I say so.

## Sources surveyed

### 1. BurntSushi/rebar — regex engine benchmark harness

- **URL(s) fetched**: <https://github.com/BurntSushi/rebar>,
  `FORMAT.md` (raw), `benchmarks/regexes/wild/date.txt` (raw).
- **Licence**: Unlicense (public domain dedication) — fetched from the
  repo's own description page. Redistribution/import is unrestricted.
- **Dialect**: multi-engine by design — the harness runs the SAME
  logical benchmark against ~16 engines (Rust `regex`/`regex-lite`,
  PCRE2 interp/JIT, .NET, V8, Go `regexp`, RE2, Hyperscan, Python
  `re`/`regex`, Perl, ICU, Java, D, …), so its patterns are written
  once and only entered for engines that can run them.
- **Size**: 14 benchmark categories/groups (per the WebFetch summary);
  each group holds several named benchmarks. Not a huge pattern count
  (this is a hand-curated barometer, not a corpus) but each one is
  chosen to be representative of one mechanism, which is exactly the
  census shape this bench already uses.
- **Evidence of real use**: explicit — the repo's own description
  names *production* sources per benchmark: the Ruff Python linter, the
  Veryl hardware-description-language parser, the Nosey Parker secrets
  scanner, and the `datefinder` Python library. I fetched
  `benchmarks/regexes/wild/date.txt` directly: it is `datefinder`'s
  actual natural-language date/time regex (ISO 8601, `YYYYMMDD`,
  ordinal words, day/month names in English/Spanish/Danish, timezone
  abbreviations) — a single very large alternation, a real "wild"
  pattern with all the mess that implies (mixed vocabulary, deep
  alternation, the kind of shape a hand-authored census would never
  invent).
- **Subject/haystack data**: real text corpora named in the fetch
  summary — CPython source, OpenSubtitles, the Unicode Character
  Database — plus synthetic haystacks built to trigger specific
  algorithmic behavior (quadratic blowup, etc.). Licence of the
  haystacks was not individually checked (OpenSubtitles in particular
  has its own terms; flag for the design lane if any haystack text
  itself is imported rather than regenerated).
- **Edge-case value**: HIGH and explicit — rebar's own category list
  (from the fetch) includes ReDoS-class patterns, quadratic-behavior
  cases, large alternations, and compile-time-vs-search-time splits;
  this is close to a second capability census already built by someone
  with deep engine knowledge.
- **Importability**: HIGH. Patterns are self-contained TOML with a
  `regex` field (`FORMAT.md`, fetched: string/array/table forms,
  `literal`/`prepend`/`append`/whitespace-trim controls), a `haystack`
  (inline or file), and a `count` field that IS the expected result —
  exactly the "self-contained, known expected result" shape [B42] needs.
  Its `engines` array is closed-world INCLUSION ("specifying engines
  constitutes inclusion — only those listed will be measured"), which
  answers half of family-taxonomy item (ii) below: rebar's own author
  has already decided, per benchmark, which of ~16 engines can run it,
  and its docs give named reasons ("doesn't support Unicode-aware case
  insensitive matching", "the regex is too large", "times out") — a
  ready-made model for our own `unsupported` outcome vocabulary.
- **Sample patterns** (Unlicense; quoting freely): the `date.txt`
  alternation is too large to quote in full (it is one benchmark's
  entire haystack-independent pattern, effectively a mini-DSL of
  date/time vocabulary); representative fragment:
  `(-?(:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])`
  as one alternative among many in the same pattern. I did not fetch
  the other named benchmark files (AWS-key detection, the lexer
  benchmark, the Unicode-word benchmark) verbatim this session — OWED
  if the design lane wants more than the one sample.

### 2. mariomka/regex-benchmark

- **URL(s) fetched**: <https://github.com/mariomka/regex-benchmark/blob/master/README.md>.
- **Licence**: MIT (per the README, "MIT © Mario Juárez").
- **Dialect**: one pattern set, re-implemented per language's native
  regex engine (17 languages) — so it is really a cross-LANGUAGE speed
  comparison using PCRE-ish syntax, not a multi-engine harness.
- **Size**: 3 patterns (email, URI, IPv4).
- **Evidence of real use**: WEAK — these are commonly-seen "toy"
  validation patterns, not sourced from a real project; the README
  itself (per the fetch) admits the haystack (concatenated "Learn X in
  Y minutes" text) "may not be the most representative test corpus."
  Useful as a well-known REFERENCE point (many blog comparisons cite
  it) more than as evidence of real-world usage.
- **Subject/haystack data**: the "Learn X in Y Minutes" corpus,
  concatenated — its own licence is per-language-page (Creative
  Commons on the learnxinyminutes site, not independently confirmed
  here).
- **Edge-case value**: LOW. All three patterns are simple, unanchored,
  single-alternative constructs; no possessive/atomic/lookaround/
  backref content.
- **Importability**: HIGH mechanically (three short, well-known
  patterns, MIT), but low marginal value since the syntax census and
  requirements already exercise emails/IPs at more depth (`bench/email`
  is the RFC 5322 specimen; `bench/syntax`'s `cls-*` family already
  covers character-class-heavy validation shapes).
- **Sample patterns** (MIT, quoted verbatim from the fetch):
  - Email: `[\w\.+-]+@[\w\.-]+\.[\w\.-]+`
  - URI: `[\w]+://[^/\s?#]+[^\s?#]+(?:\?[^\s#]*)?(?:#[^\s]*)?`
  - IPv4: `(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9])`

### 3. regex-redux (Computer Language Benchmarks Game)

- **URL(s)**: found via WebSearch (benchmarksgame-team.pages.debian.net
  description page); not independently WebFetched this session, so its
  licence statement is not directly confirmed — flag.
- **Dialect**: DNA/FASTA 8-mer matching; patterns are small
  case-insensitive alternations over the 4-letter DNA alphabet plus
  IUPAC ambiguity codes.
- **Size**: 9 fixed patterns (the ones the search summary lists) plus a
  handful of substitution patterns for IUPAC-code expansion.
- **Evidence of real use**: it's a benchmark-game task, not a
  production pattern, but it models a REAL workload class (genomic
  substring/motif search) rather than a contrived string.
- **Subject data**: large synthetic FASTA files generated by a sibling
  benchmark-game task (`fasta`), not real genomic data; no licence
  concern since it's generated, but it is DNA-alphabet only — of
  limited use to a general capability census beyond "narrow alphabet,
  large subject, small alternation" as one throughput shape (which
  `bench/altwide` and `bench/loglines`'s throughput regime already
  cover in spirit, just not on a 4-letter alphabet).
- **Edge-case value**: LOW-MODERATE — mainly interesting as a "small
  alternation, huge subject, narrow alphabet" throughput point; the
  benchmark's own constraint ("must use the same algorithm to calculate
  the result") makes it more an algorithm competition than a regex
  capability probe.
- **Importability**: MODERATE. Patterns are trivial to transcribe;
  value is mostly as ONE extra throughput/alphabet-narrowness cell, not
  as a family generator.
- **Sample patterns** (from the WebSearch summary, DNA 8-mer forms):
  `agggtaaa|tttaccct`, `[cgt]gggtaaa|tttaccc[acg]`,
  `a[act]ggtaaa|tttacc[agt]t` (three of the nine listed).

### 4. RE2's own testdata/benchmarks (`google/re2`)

- **URL(s) fetched**: `re2/testing/regexp_benchmark.cc` (raw content via
  WebFetch).
- **Licence**: BSD-style (RE2's own LICENSE, quoted header: "Copyright
  2006-2008 The RE2 Authors... governed by a BSD-style license").
- **Dialect**: RE2 syntax (a close, deliberately-restricted subset of
  PCRE — no backrefs, no lookaround; this is itself a capability-survey
  DATUM, not just a pattern source).
- **Size**: a handful of named micro-patterns (Easy0/1/2, Medium, Hard,
  Fanout, Parens) rather than a corpus; this is RE2's own perf-tuning
  suite, hand-authored by its maintainers to isolate specific automaton
  behaviors (backtracking blowup on `Hard`, branching fanout, group
  count scaling on `Parens`).
- **Evidence of real use**: these are ENGINE-AUTHOR microbenchmarks,
  contrived on purpose to isolate one automaton behavior — valuable as
  edge cases, not as "wild" evidence. Positioned correctly in the
  taxonomy as an edge-case source, not a real-usage source.
- **Subject data**: none of substance beyond what each benchmark
  generates inline (not fetched in detail; OWED if needed).
- **Edge-case value**: MODERATE-HIGH for backtracking-engine stress
  specifically: `Hard` (`[ -~]*ABCDEFGHIJKLMNOPQRSTUVWXYZ$`) is a
  textbook "leading unanchored star, late anchor" shape that forces
  O(n²) behavior on naive backtrackers — exactly the ambiguous-
  decomposition class APPROACH.md §2 principle 1 already asks for, and
  a useful CONTROL against `bench/syntax`'s `lit-cat` idea (one
  construct, otherwise plain body) at a much larger scale.
- **Importability**: HIGH — tiny, self-contained, BSD, textual.
- **Sample patterns** (BSD, quoted from the fetch):
  - `ABCDEFGHIJKLMNOPQRSTUVWXYZ$` (Easy0)
  - `A[AB]B[BC]C[CD]D[DE]E[EF]F[FG]G[GH]H[HI]I[IJ]J$` (Easy1)
  - `(?i)ABCDEFGHIJKLMNOPQRSTUVWXYZ$` (Easy2)
  - `[XYZ]ABCDEFGHIJKLMNOPQRSTUVWXYZ$` (Medium)
  - `[ -~]*ABCDEFGHIJKLMNOPQRSTUVWXYZ$` (Hard)

### 5. Rust `regex` crate's `testdata/` (engine-independent TOML tests)

- **URL(s) fetched**: `rust-lang/regex` tree listing for `testdata/`
  (WebFetch summary of the directory + its README).
- **Licence**: MIT/Apache-2.0 dual, as for the rest of `rust-lang/regex`
  (not independently re-confirmed by fetching a LICENSE file this
  session — the crate's licensing is extremely well documented
  elsewhere, flagged as "not verified this session" per the honesty
  rule above, but very low risk of being wrong).
- **Dialect**: an ENGINE-INDEPENDENT TOML test format explicitly
  designed to drive `regex`, `regex-automata`, and `regex-lite` from
  ONE set of cases — directly relevant to [B42] requirement (4)'s
  question of what a shared pattern/case source format should look
  like (this is note 3's subject, but the precedent belongs here too).
- **Size**: 25+ TOML files by the fetch's count, spanning anchoring,
  empty matches, Unicode/UTF-8, word boundaries, multiline, "expensive"
  patterns, overlapping matches, CRLF, and a `fowler/` subdirectory —
  which is the well-known Glenn Fowler / AT&T regex conformance suite,
  itself derived from decades of POSIX/AT&T regex test history and
  reused across many engines (Tcl, Perl's own test suite draws on
  related material).
- **Evidence of real use**: these are CONFORMANCE tests, not
  "found in the wild" usage evidence, but the `fowler/` subset in
  particular has decades of cross-engine pedigree — it is closer to a
  shared reference corpus than to any one engine's private test data.
- **Subject data**: inline per test case (small strings), not separate
  corpora.
- **Edge-case value**: HIGH for CORRECTNESS edge cases specifically
  (empty matches, CRLF boundary handling, leftmost-first vs
  leftmost-longest divergences) rather than performance edge cases —
  complements rebar and RE2's benchmark file, which are performance-
  shaped.
- **Importability**: HIGH mechanically, but this is a conformance
  corpus, and [B42] is chartered as a CAPABILITY/performance survey,
  not a second correctness suite (this bench already leans on the
  libpcre2 oracle for correctness per `requirements.md` §7) — best used
  as a SOURCE of unusual-but-real anchoring/empty-match/multiline
  shapes for the edge-case catalogue (§3 below), not wholesale import.

### 6. Hyperscan / Vectorscan corpora and benchmark tooling

- **URL(s) fetched**: `intel.github.io/hyperscan` tools page,
  `hyperscan/tools/hsbench/scripts/CorpusBuilder.py` (via WebSearch
  summary, not independently WebFetched line-by-line), VectorCamp's
  `vectorscan` README/LICENSE search results.
- **Licence**: Hyperscan (up to 5.4, the last open-source Intel
  release) and Vectorscan (its portable fork, ARM/Power support) are
  both BSD-3-Clause (per the search summaries; not independently
  fetched as a raw LICENSE file this session — flag as "not verified
  this session").
- **Dialect**: PCRE-syntax-following but with Hyperscan's own
  restrictions (it is a MULTI-PATTERN, streaming, SIMD engine; it
  REJECTS constructs it cannot support in its execution model —
  backreferences among them). This maps directly onto [B7]'s Vectorscan
  entry and its "all-ends semantics, tagged" note in APPROACH.md §5.
- **Size**: not a fixed public corpus of "real" patterns so much as
  tooling (`hsbench`, `hscollider` for validating match behavior
  against PCRE, `hscheck` for pattern compilation, `CorpusBuilder.py`
  for building haystacks) — Hyperscan's own regression/QA harness is
  the closer analogue to what a "corpus" would mean here, and its
  REGRESSION SUITE is reportedly large (used in every release's QA per
  the search summary) but I did not get a pattern count or licence
  confirmation for the regression corpus specifically — OWED.
  Snort/Suricata rule sets (below) are Hyperscan's most commonly cited
  REAL usage source (Suricata's MPM engine can use Hyperscan), which
  makes those rule sets doubly valuable: real patterns AND a
  Hyperscan-relevant capability check in one source.
- **Evidence of real use**: Hyperscan ships in Suricata, Snort 3
  (as an MPM backend option) and various commercial DPI/WAF products —
  strong indirect evidence, but the patterns it's fed in production are
  the rule-set patterns (item 8/9 below), not a corpus Hyperscan itself
  publishes.
- **Subject data**: `hsbench`'s `CorpusBuilder.py` builds haystacks
  from a target directory of sample files — infrastructure, not
  content; nothing to import directly.
- **Edge-case value**: HIGH for the CAPABILITY dimension specifically —
  what Hyperscan/Vectorscan REFUSE (backrefs, some lookaround forms,
  unbounded-width patterns with certain SOM tracking requirements) is
  itself the edge-case data point [B42] wants for the family taxonomy,
  independent of any pattern corpus.
- **Importability**: LOW as a pattern corpus (nothing public and
  pattern-shaped to import wholesale); HIGH as a capability reference
  (its docs enumerate unsupported constructs, useful for note 2's
  engine-landscape survey).
- **Samples**: none captured — Hyperscan does not publish a
  quotable "real patterns" file the way rebar or grok-patterns do.

### 7. Snort / Suricata community rule sets (`pcre:` option)

- **URL(s) fetched**: `github.com/OISF/suricata` payload-keywords doc
  (WebFetch), `detect-pcre.c` (found, not content-fetched), a sample
  `decoder-events.rules` file (WebFetch — confirmed NO pcre content, a
  useful negative result: most Suricata rules use faster non-regex
  keywords like `content:`/`decode-event:`, and `pcre:` is reserved for
  cases a literal/prefix match cannot express).
- **Licence**: MIXED and rule-range-dependent (found via WebSearch, not
  independently verified against a current LICENSE file): older
  Emerging Threats sids are GPLv2; sids 2000000-2799999 are BSD-
  licensed; the current Emerging Threats Open ruleset (Proofpoint ET
  Open) is described as MIT in `suricata-update`'s own index config.
  IMPORTANT: this is a MIXED bag by rule range and needs a per-file
  check before import, not a blanket assumption — a real licensing
  hazard for [B42] requirement (1) if rules are imported wholesale.
- **Dialect**: PCRE (Suricata explicitly documents `pcre:` as running a
  PCRE-syntax match with Perl-compatible modifier flags: `A`, `E`, `G`,
  etc., plus Suricata-specific buffer-selection modifiers).
- **Size**: the ET Open ruleset runs to tens of thousands of rules
  total; only a MINORITY carry a `pcre:` option (most rules use
  `content:` byte/string matching for speed, falling back to PCRE only
  when a fixed string or simple wildcard cannot express the check) —
  this minority-with-pcre subset is exactly the "wild PCRE actually run
  against real traffic" population [B42] wants, and it is a POPULATION
  I did not get an exact size for this session (OWED: grep a checked-
  out ruleset for `pcre:` rule count).
- **Evidence of real use**: about as strong as it gets — these are
  regexes evaluated against live/replayed network traffic in
  production IDS/IPS deployments, under a byte budget hostile actors
  can probe (making them ALSO adversarially interesting: a ReDoS in an
  IDS rule is itself a known attack class against the IDS).
- **Subject data**: none shipped (rules match against traffic, not a
  bundled corpus); a pcap-derived haystack would need to come from
  elsewhere (a licence-clean pcap corpus, e.g. a public CTF or lab
  capture) — genuinely useful subject data for THIS family would need
  its own sourcing pass, flagged as a design question (§5).
- **Edge-case value**: HIGH — `pcre:` rules commonly combine anchoring
  modifiers, byte-offset buffer selection, and case-insensitivity over
  BINARY (not just text) payloads; a realistic "regex over raw bytes,
  including non-UTF8 content" edge case this bench's existing sets
  (email/loglines/bounded/altwide, all textual) do not exercise.
- **Importability**: MODERATE — self-contained pattern extraction is
  mechanical (`pcre:"/PATTERN/flags"` is a fixed grammar to parse out
  of a `.rules` file) but licence auditing per rule RANGE is required,
  and Suricata's own PCRE dialect carries buffer-selection semantics
  (which capture group, which protocol field) that do not carry over
  to a plain string-matching sub-bench without translation — a design
  question, not a blocker.
- **Samples**: I did not find a `pcre:`-bearing rule in the one file I
  fetched (by design, most rules don't use it); OWED — a targeted fetch
  of a rules file known to carry `pcre:` (e.g. an HTTP/app-layer rule
  file) would produce quotable samples; not done this session for time.

### 8. ModSecurity / OWASP Core Rule Set (CRS)

- **URL(s)**: found via WebSearch (`github.com/coreruleset/coreruleset`,
  the CRS's current home); not independently WebFetched for rule
  content this session.
- **Licence**: Apache License 2.0 (per WebSearch summary of the
  project's own description — commonly cited and low-risk, but not
  independently confirmed against a LICENSE file this session).
- **Dialect**: ModSecurity's own regex dialect, which is PCRE-based
  (ModSecurity links libpcre/PCRE2 for its `@rx` operator).
- **Size**: CRS ships hundreds of rules across attack-category files
  (SQLi, XSS, RCE, protocol anomalies, etc.); a large fraction use
  `@rx` with substantial alternations (SQLi keyword lists, XSS tag/
  attribute lists) — genuinely large, genuinely real-use WAF patterns.
- **Evidence of real use**: very strong — CRS is deployed in front of
  production web applications worldwide (Apache/Nginx ModSecurity,
  Coraza); these patterns are executed against untrusted, adversarial
  HTTP request bodies constantly, making them BOTH real-use and
  ADVERSARIALLY-TESTED (attackers actively probe CRS regexes for
  bypasses and for ReDoS, so any known-slow CRS rule is a documented,
  citable incident, not a hypothetical).
- **Subject data**: none bundled (rules run against live HTTP traffic);
  a synthetic "malicious-looking" HTTP body corpus would need its own
  construction (OWASP has separate "attack payload" test lists, e.g.
  in its Web Security Testing Guide, which could seed haystacks — not
  investigated this session).
- **Edge-case value**: VERY HIGH — CRS is widely reported (in security
  research, not fetched here) as a source of accidentally-quadratic
  regexes because its alternations grow over years of community
  patches; this is precisely the "wild pathological pattern, found not
  invented" class [B42] wants, with a real incentive structure (attacker
  interest) behind why any slow rule gets found and fixed eventually.
- **Importability**: MODERATE — patterns are embeddable in
  `SecRule ... "@rx PATTERN"` directives, mechanically extractable, but
  many rely on ModSecurity-specific transformation chains (`t:lowercase`
  etc.) applied BEFORE the regex runs, so a faithful import needs to
  either strip those (changing what "real use" means) or note the
  pattern is tested post-transformation — a design question, not a
  blocker, and worth asking Frank about (§5).
- **Samples**: none fetched verbatim this session (Apache-2.0 permits
  quoting; OWED — a targeted fetch of one CRS rule file, e.g. the SQLi
  rules, would produce 3-6 quotable patterns for the design note).

### 9. OWASP Validation Regex Repository

- **URL(s) fetched**: `community.owasp.org/OWASP_Validation_Regex_Repository`
  (after a 308 redirect from `owasp.org`, followed).
- **Licence**: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA
  4.0), per the page's own footer statement, fetched directly. CC
  BY-SA requires attribution and share-alike on redistribution — usable
  for [B42] with an attribution note per pattern, not silently.
- **Dialect**: stated as engine-neutral but "mainly PCRE syntax" (the
  page's own words, per the fetch).
- **Size**: a modest hand-curated page (dozens, not thousands) covering
  common validators: email, URL, IP, US zip, dates, and similar
  everyday shapes.
- **Evidence of real use**: MODERATE — these are widely COPIED
  reference patterns (the page exists specifically so people copy from
  it), which is a different kind of "real use" than mined-from-a-
  repository evidence: it's evidence of INTENDED reuse, not measured
  reuse, but it is exactly the kind of "validator regex a developer
  actually pastes into production code" the charter's framing
  describes.
- **Subject data**: none (validator patterns only, no bundled test
  corpus — though each has an obvious hand-authored test set: valid/
  invalid emails, IPs, etc., which a design lane would need to author
  anyway).
- **Edge-case value**: LOW-MODERATE — mostly straightforward class/
  alternation-heavy validators, useful more as "common shapes" than as
  edge-case stressors, though the DATE pattern (noted as "complex...
  with leap year validation" in the fetch) is a good example of an
  everyday validator that is secretly a large, easy-to-get-wrong
  alternation — a real-world near-miss of the ReDoS class without being
  a deliberately pathological one.
- **Importability**: HIGH — short, self-contained, one-line-per-pattern,
  CC BY-SA (attribution-friendly).
- **Sample patterns** (CC BY-SA 4.0, quoted verbatim from the fetch):
  - Email: `^[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$`
  - IPv4: `^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`
  - US Zip: `^\d{5}(-\d{4})?$`

### 10. Elastic Logstash grok patterns (`logstash-patterns-core`)

- **URL(s) fetched**: `raw.githubusercontent.com/logstash-plugins/logstash-patterns-core/main/patterns/legacy/grok-patterns`.
- **Licence**: Apache License 2.0 (per WebSearch summary of the
  project's own README — "fully free and open source"; not
  independently re-confirmed against a LICENSE file this session, but
  Elastic's Apache-2.0 licensing of this plugin is extremely well
  documented).
- **Dialect**: Oniguruma-flavored regex (grok patterns are Ruby-Onig
  under the hood, composed via `%{NAME}` macro expansion into a single
  regex at match time) — directly relevant since Oniguruma is on the
  [B7] roster.
- **Size**: the fetched file alone has 40+ base patterns (`USERNAME`,
  `EMAILADDRESS`, `IPV4`, `IPV6`, `URI` and its sub-parts, `MONTH`,
  timestamp formats, …), and this is only the "legacy" base file —
  the full `logstash-patterns-core` repo has many more per-application
  pattern files (nginx, apache, java, linux-syslog, mcollective,
  postgresql, redis, …), each real-world log-format-specific.
- **Evidence of real use**: VERY STRONG — these patterns are shipped in
  Logstash and run against real production log streams at scale
  continuously; they are also COMPOSITIONAL (`%{IP}` expands into
  `%{IPV6}|%{IPV4}`, which itself expands further), so importing them
  exercises both the patterns AND a realistic "macro-expanded, deeply
  nested alternation of alternations" shape that a hand-written census
  would be unlikely to produce on its own.
- **Subject data**: none bundled directly (grok is applied to
  operational log lines, which aren't published alongside the
  patterns), but `bench/loglines` ALREADY generates log-shaped text —
  strong overlap; a design question is whether grok patterns should run
  against `bench/loglines`'s existing subjects rather than new ones.
- **Edge-case value**: HIGH — several patterns here use possessive/
  atomic constructs explicitly for PERFORMANCE reasons (e.g.
  `BASE10NUM`'s `(?>...)` atomic group, `QUOTEDSTRING`'s heavy atomic-
  group nesting to avoid backtracking blowup on quote-escape parsing) —
  this is a real author fighting catastrophic backtracking in
  production and leaving the fix in the pattern, which is a genuinely
  different edge case from a synthetically-constructed ReDoS: it shows
  what the FIX looks like, not just the vulnerability.
- **Importability**: HIGH for the base patterns (self-contained after
  macro expansion, Apache-2.0), MODERATE for the macro-composed forms
  (need the macro expander or a flattening step — `bench/loglines`'s
  own generator may already do something similar; check before
  reinventing).
- **Sample patterns** (Apache-2.0, quoted verbatim from the fetch):
  - `BASE10NUM = (?<![0-9.+-])(?>[+-]?(?:(?:[0-9]+(?:\.[0-9]+)?)|(?:\.[0-9]+)))`
  - `QUOTEDSTRING = (?>(?<!\\)(?>"(?>\\.|[^\\"]+)+"|""|(?>'(?>\\.|[^\\']+)+')|''|(?>`(?>\\.|[^\\`]+)+`)|``))`
  - `UUID = [A-Fa-f0-9]{8}-(?:[A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}`
  - `WINPATH = (?>[A-Za-z]+:|\\)(?:\\[^\\?*]*)+`

### 11. regexlib.com / RegExr community patterns

- **URL(s) fetched**: `regexlib.com` (search-confirmed live), GitHub
  mirror `ardalis/RegExLib.com` (site SOURCE CODE, not the pattern
  database content).
- **Licence**: NOT independently confirmed — the GitHub repo is the
  ASP.NET site's own source, not a data export; the pattern DATABASE
  itself (user-submitted patterns) would need its own terms-of-use
  check before any import — the site is a community submission board,
  and individual submitters' rights are unclear without reading its
  ToS directly (not done this session). Flag as a licensing-unknown
  source until checked.
- **Dialect**: mixed/unstated per submission (.NET regex historically,
  since the site itself is ASP.NET, but submitters write from whatever
  language they used).
- **Size**: thousands of community-submitted patterns across many
  categories, per general knowledge of the site (not independently
  counted this session).
- **Evidence of real use**: WEAK-to-unverifiable — this is a "paste
  your regex" community board; a pattern being on regexlib.com is
  evidence someone wrote it and thought it useful, not evidence it runs
  in production. Quality and correctness are inconsistent (long-
  standing reputation issue with the site, not independently verified
  here).
- **Subject data**: none.
- **Edge-case value**: LOW — value would be volume and variety of
  everyday shapes, not edge cases specifically; regexlib's own
  reputation issue (untested/incorrect submissions) makes it a poor
  source without an independent oracle pass on every pattern, which
  this bench already requires for EVERY imported pattern anyway
  (`requirements.md` §7 — correctness gates the scoreboard) so it's not
  disqualifying, just low-value relative to effort.
- **Importability**: LOW-MODERATE given the licensing unknown; not
  recommended as a near-term source.
- **Samples**: none fetched (could not get pattern-database content
  through available tools this session).

### 12. Davis et al., "Why Aren't Regular Expressions a Lingua Franca?" (ESEC/FSE 2019) — the polyglot regex corpus

- **URL(s) fetched**: `arxiv.org/abs/2105.04397` (abstract page).
- **Licence**: NOT confirmed — the abstract page does not state whether
  the 537,806-regex corpus itself is publicly downloadable or under
  what terms; a companion artifact may exist (the same author group's
  `vuln-regex-detector` tool, item 13 below, is a separate public repo)
  but I did not find a corpus download link this session. OWED: check
  the paper's own "Artifact Available" badge / a Zenodo or GitHub link
  in the full PDF (not fetched — arXiv HTML rendering of the PDF body
  was not attempted this session).
- **Dialect**: eight languages — JavaScript, Java, PHP, Python, Ruby,
  Go, Perl, Rust — i.e., patterns as WRITTEN for each language's own
  engine, which is directly useful for the [B7] capability-landscape
  question (note 2) even without importing pattern text.
- **Size**: 537,806 regexes from 193,524 projects — by far the LARGEST
  source surveyed, several orders of magnitude past anything else here.
- **Evidence of real use**: VERY STRONG BY CONSTRUCTION — mined
  directly from real open-source projects across major package
  ecosystems, which is the closest thing to a ground-truth "regexes as
  actually written" sample in this survey.
- **Subject data**: none (this is a pattern-mining study, not a
  matching-workload study).
- **Edge-case value**: HIGH INDIRECTLY — the paper's OWN findings are
  edge-case gold even without the corpus text: 15% of mined regexes
  exhibit semantic differences when ported across language engines and
  10% exhibit performance differences, and the authors found actual
  engine bugs in V8, Python, Ruby, and Rust while doing this — every
  one of those is a candidate "known divergence" case worth hand-
  curating into the [B42] set with attribution to the paper, even
  without bulk-importing the corpus.
- **Importability**: UNKNOWN pending the artifact-availability check
  above; if available, importing even a stratified SAMPLE (by
  complexity/construct) would be extremely valuable and is the single
  biggest opportunity in this survey if the licence permits it.
- **Samples**: none fetched (abstract only; full paper not fetched this
  session — OWED).

### 13. `vuln-regex-detector` / ReDoS corpora (Davis's group's tooling)

- **URL(s) fetched**: WebSearch summary of
  `github.com/davisjam/vuln-regex-detector`; a cited Zenodo artifact
  DOI (`10.5281/zenodo.5916441`) found via search, not independently
  fetched.
- **Licence**: the `vuln-regex-detector` REPO's own licence not
  independently confirmed this session (GitHub default view did not
  surface a LICENSE badge in the search summary — OWED). The Zenodo
  artifact's licence also not confirmed.
- **Dialect**: JS/PCRE-family, per the tool's stated purpose (detect
  ReDoS in real project regexes).
- **Size**: the cited Zenodo artifact is described (per the search
  summary) as a dataset of regexes found in web forms and API
  specifications, with vulnerability analysis reports — size not
  captured this session.
- **Evidence of real use**: STRONG if the same "mined from real
  projects" methodology as item 12 (same research group) — not
  independently confirmed for this specific artifact.
- **Subject data**: not investigated.
- **Edge-case value**: VERY HIGH BY DESIGN — this is explicitly a
  catalogue of regexes KNOWN to exhibit catastrophic/ambiguous
  backtracking, which is precisely the "nested quantifier ReDoS" family
  the edge-case catalogue (§3) needs concrete, attributed, real-world
  examples for, rather than hand-inventing `(a+)+b`-class toys.
- **Importability**: UNKNOWN pending licence check (OWED).
- **Samples**: none fetched (need the Zenodo artifact or repo content
  directly — not done this session).
- **Related, lighter-weight alternative**: `engn33r/awesome-redos-
  security` (found via search) — a curated LIST of ReDoS CVEs and
  resources, which is a good STARTING INDEX for hand-picking a handful
  of well-documented, attributable, real ReDoS incidents (each with its
  own CVE, its own licence-free pattern text since CVE descriptions are
  factual/public) without needing the bulk corpus's licensing resolved
  at all — worth treating as its own mini-source. Not deep-fetched this
  session; OWED if the design lane wants specific CVE patterns quoted.

### 14. Chapman & Stolee, "Exploring Regular Expression Usage and Context in Python" (ISSTA 2016)

- **URL(s)**: found via WebSearch (ACM DL, Semantic Scholar, DBLP); not
  independently WebFetched (ACM DL is paywalled; abstract-level summary
  only from search snippets).
- **Licence**: N/A directly — this is academic-study evidence, not a
  pattern export. No indication in the search results that a raw
  corpus was released alongside it (unlike Davis et al.); OWED to check
  the paper itself for a released dataset link, not done this session.
- **Dialect**: Python `re`.
- **Size**: not captured (mined "properties of open source
  repositories on GitHub," size unstated in the snippets available).
- **Evidence of real use**: STRONG BY METHOD (static analysis of real
  GitHub Python code + an 18-developer survey), but without a released
  corpus this is USE-AS-EVIDENCE (cite its findings in the design note)
  rather than USE-AS-PATTERN-SOURCE.
- **Edge-case value**: MODERATE, indirectly — its survey results (pain
  points developers report) are useful for justifying WHICH edge cases
  matter to real authors, a framing point for the design note rather
  than a pattern source.
- **Importability**: LOW (no corpus found to import).
- **Samples**: none available.

### 15. PCRE2's own test data (`PCRE2Project/pcre2`, `testdata/`)

- **URL(s)**: found via WebSearch (RunTest script, pcre2test docs); not
  independently WebFetched for file listing/content this session.
- **Licence**: PCRE2 itself is BSD-licensed — WELL KNOWN but NOT
  independently verified against a fetched LICENCE file this session
  (a direct fetch attempt at one candidate URL 404'd); flag for the
  design lane to confirm against the actual pin's `LICENCE` file before
  relying on it (this project already vendors/tracks a PCRE2 oracle
  version per `bench/syntax`'s notes, so the licence is almost
  certainly already on file somewhere in this repo or its dependency
  records — check there first rather than re-fetching).
- **Dialect**: PCRE2, obviously — and this is the ORACLE this bench
  already uses (`oracle_pcre2.py`), so PCRE2's testdata is really an
  EXTENSION of an already-trusted dependency, lower marginal risk than
  any other source here.
- **Size**: PCRE2's `testdata/` directory holds many `testinputN`/
  `testoutputN` file pairs (the RunTest harness runs pcre2test against
  each) — this is PCRE2's OWN conformance/regression suite, likely
  hundreds to low thousands of individual pattern/subject cases,
  covering essentially every documented PCRE2 construct plus years of
  accumulated regression cases from real bug reports.
- **Evidence of real use**: MIXED — largely constructed test cases (by
  PCRE2's own maintainers) rather than mined from external projects,
  BUT a meaningful fraction of any mature engine's regression suite
  consists of cases filed BECAUSE a real user hit a bug — those
  specific cases are "found in the wild" by a different route (a bug
  report) even though the file as a whole is maintainer-authored.
- **Subject data**: inline per test case, PCRE2's own `pcre2test`
  script format (`/pattern/` then subject lines with expected results)
  — a FORMAT already adjacent to what this bench already parses via
  its PCRE2 oracle tooling, likely the cheapest of all sources here to
  mechanically ingest.
- **Edge-case value**: VERY HIGH for SYNTAX coverage depth (this is
  precisely the same registry `bench/syntax` was seeded from — pcrec's
  `--list-syntax`, which is itself built against the PCRE2 reference —
  so PCRE2's testdata is the NEXT layer down: not just "which
  constructs exist" but "which combinations and edge byte-values have
  actually broken something before").
- **Importability**: HIGH — same dialect as the existing oracle, same
  general shape as `bench/syntax`'s approach, BSD-permissive (pending
  the flagged re-check).
- **Samples**: none fetched (file listing/content not retrieved this
  session — OWED, and probably the single most mechanically-cheap OWED
  item here given the existing oracle tooling).

### 16. Oniguruma's own test suite (`kkos/oniguruma`)

- **URL(s)**: repo found via WebSearch; the specific test file (`test.c`
  or similar) was NOT located this session (search did not surface it
  directly — GitHub's file-listing search is not reliable via
  WebSearch; a direct repo browse would be needed, not attempted this
  session due to time). OWED.
- **Licence**: Oniguruma is BSD-2-Clause — WELL KNOWN, NOT independently
  verified this session; flag.
- **Dialect**: Oniguruma's own syntax (configurable; PCRE-like by
  default, and this is the SAME engine grok patterns (item 10) and
  TextMate grammars (item 17) both run on, so it sits at the center of
  a real usage cluster even without its own test file confirmed).
- **Size/evidence/subject/edge-case value/importability/samples**: NOT
  ASSESSED this session beyond the above — genuine gap, OWED. Given
  that Oniguruma is on the [B7] roster and its two "wild" usage
  clusters (grok, TextMate) are both independently well covered above,
  this is lower priority than PCRE2's testdata but should still be
  checked before the design note is written.

### 17. GNU grep / sed test suites

- **URL(s)**: `git.savannah.gnu.org/grep.git` located via WebSearch
  (mirrors only; the Savannah git web UI itself did not resolve for
  direct fetch this session), plus `coreutils/gnulib`'s `regex.c`/
  `regex.h` (found, not content-fetched for test cases specifically).
- **Licence**: GNU grep is GPLv3 — WELL KNOWN, not independently
  verified this session. IMPORTANT: GPLv3 is COPYLEFT — unlike every
  BSD/MIT/Apache/Unlicense source above, importing GPLv3-covered test
  patterns into this repo (which does not otherwise carry a GPL
  obligation) is a REAL licensing question, not a formality — flag
  prominently for Frank (§5) rather than assuming the design lane can
  just decide.
- **Dialect**: POSIX BRE/ERE (grep's default and `-E`) plus GNU
  extensions and, via `-P`, PCRE through libpcre — directly useful for
  the TRE/POSIX entry on the [B7] roster (APPROACH.md §5: "TRE (POSIX,
  tagged)"), since BRE/ERE-vs-Perl divergence is exactly what a
  POSIX-tagged testee needs distinguishing cases for.
- **Size**: not captured this session (test suite location itself not
  confirmed — genuine gap).
- **Evidence of real use**: grep is about as "real use" as regex usage
  gets (a POSIX utility used continuously across the entire Unix
  ecosystem), but its TEST SUITE specifically is maintainer-authored
  conformance testing, similar in character to PCRE2's testdata (item
  15) — valuable for BRE/ERE edge cases, not for "wild patterns."
- **Subject/edge-case value/importability/samples**: NOT ASSESSED this
  session beyond the licence flag above — genuine gap, OWED, and given
  the GPLv3 flag, this source needs a Frank ruling before any import
  effort is spent on it regardless of technical value.

### 18. TextMate grammars / syntax highlighters (Oniguruma-dialect regexes in the wild)

- **URL(s) fetched**: WebSearch results only (`textmate/textmate.tmbundle`,
  `microsoft/vscode-textmate`); no grammar file content fetched this
  session.
- **Licence**: per-grammar-repo (varies — `vscode-textmate` itself is
  MIT per Microsoft's usual OSS licensing, not independently confirmed
  this session; individual LANGUAGE grammar repos, e.g. for a specific
  programming language's syntax highlighting, carry their OWN licences
  and would need per-grammar checking before import — this is a
  many-small-sources problem, not a single-source licence question).
- **Dialect**: Oniguruma (confirmed by search: "TextMate grammars use
  the Oniguruma dialect for regex patterns... `\k<n>` for capture group
  references").
- **Size**: potentially very large in aggregate (every VS Code
  language extension ships a `.tmLanguage.json` full of regexes) but
  no single canonical "the TextMate regex corpus" was found — it would
  need assembling from many per-language grammar repos.
- **Evidence of real use**: VERY STRONG — every keystroke in a VS Code
  or Sublime Text editor with syntax highlighting enabled runs these
  regexes, continuously, on arbitrary (including adversarial-length)
  source files — a genuinely different "real use" character from a
  server-side WAF or log parser: LATENCY-SENSITIVE, INTERACTIVE, and
  run on UNTRUSTED-LENGTH input (a very long single line, e.g. a
  minified JS file, is a known trigger for TextMate-grammar
  slowdowns in editors — a real, reported problem class, e.g. VS Code
  issue trackers, not independently cited here).
- **Subject data**: source code in the target language — trivially
  available, no licensing concern for GENERATED or well-known open-
  source sample files.
- **Edge-case value**: HIGH for a family this bench does not currently
  have at all: MANY SMALL PATTERNS applied REPEATEDLY per line/token
  boundary (a grammar is dozens-to-hundreds of regexes each tried in
  sequence per line) — closer to `bench/loglines`'s "search over
  mostly-failing text" shape but with the added twist of MULTIPLE
  patterns in a priority-ordered list, which none of the existing sets
  model (every existing set measures one pattern at a time per
  APPROACH.md's testee-adapter model, unless Vectorscan's "regex set"
  workload, mentioned in the brief, already covers this — see note 2).
- **Importability**: MODERATE — mechanically simple (single JSON file,
  `match`/`begin`/`end` keys carry the regex text) but per-grammar
  licence auditing is needed, and Oniguruma-specific syntax
  (`\h`, `\k<name>`, Ruby-style property names) needs a per-engine
  spelling table exactly as [B42]'s charter already anticipates
  (allowed "slight syntactic adjustment... when semantics are
  preserved").
- **Samples**: none fetched verbatim this session (would need a
  specific grammar file, e.g. a JSON language grammar, fetched
  directly — not done this session, OWED, low cost if wanted).

## Additional context: GNU grep/sed and the licensing shape of this survey generally

Across the eighteen sources, licence terms split roughly:
public-domain/permissive (rebar's Unlicense, mariomka's MIT, RE2's BSD,
OWASP's CC BY-SA, Elastic's Apache-2.0, ModSecurity CRS's Apache-2.0,
PCRE2/Oniguruma's BSD when confirmed) vs. copyleft (GNU grep's GPLv3) vs.
genuinely unknown (regexlib.com, the two academic corpora, Suricata rules
by range, TextMate grammars per-repo). The [B42] design note should treat
"licence confirmed permissive" as a real filter on the shortlist, not an
afterthought — several of the HIGHEST edge-case-value sources (Suricata
rules, CRS) are also the ones with the MOST licensing homework still owed.

## (i) Shortlist, ranked

1. **BurntSushi/rebar** — highest overall value: multi-engine-aware by
   construction, Unlicense, explicit real-vs-synthetic labeling per
   benchmark, an existing model for the `unsupported`-engine vocabulary
   [B42] needs, and one confirmed genuinely-wild pattern (`datefinder`'s
   date regex) already in hand. Should be read in FULL (not just this
   session's partial fetch) before the design note is drafted.
2. **PCRE2's own testdata** — cheapest to ingest (same dialect as the
   existing oracle, same tooling family this bench already trusts),
   very high construct-combination depth, likely-BSD (pending a
   one-file re-check this repo probably already has on hand via its
   PCRE2 dependency records). The single best "do this first" item.
3. **Elastic grok patterns** — very strong real-use evidence, Apache-2.0,
   Oniguruma dialect (covers a [B7] roster gap), and — notably —
   patterns where the ORIGINAL AUTHOR already fought and fixed
   catastrophic backtracking (the atomic-group patterns), which is a
   genuinely rare and valuable kind of "wild" evidence.
4. **Davis et al.'s polyglot corpus** — the single biggest potential
   win IF the artifact is available and licensable (537,806 real
   regexes, 8 languages, with published findings on cross-engine
   divergence already pointing at specific interesting cases) — ranked
   4th rather than 1st only because availability/licence is UNCONFIRMED
   this session; re-rank to #1 if confirmed.
5. **ModSecurity OWASP CRS** — very high edge-case value (adversarially
   tested for years), Apache-2.0, but needs a transformation-chain
   design decision before import (do we strip `t:lowercase` etc.).
6. **RE2's `regexp_benchmark.cc`** — small but free, BSD, hand-picked by
   an engine author specifically to isolate ambiguous-decomposition
   blowup; import wholesale, it's cheap.
7. **Suricata/ET rule sets** — high edge-case value (binary payloads,
   real adversarial pressure) but the licence is the messiest of any
   permissive-leaning source (mixed by sid range) and needs its own
   audit pass; don't block the design note on it, but don't drop it.
8. **OWASP Validation Regex Repository** — CC BY-SA, small, easy,
   moderate value; good FILLER for the "everyday shapes" side of the
   taxonomy rather than a centerpiece.
9. **rust-lang/regex `testdata/`** (incl. the Fowler suite) — best used
   for the CORRECTNESS edge-case catalogue (§3), not as a capability-
   survey pattern source per se, given this bench's existing oracle
   approach already covers correctness.
10. **mariomka/regex-benchmark, regex-redux** — low marginal value
    given existing set overlap (email/IP already covered by
    `bench/email`/`bench/syntax`); include only as well-known REFERENCE
    points if the public-facing interface (charter item (7), later)
    ever wants a "how do we compare to famous benchmarks" framing.
11. **GNU grep test suite** — hold pending a licence ruling (GPLv3);
    real technical value for the POSIX/TRE testee but not worth
    surveying further until Frank rules on copyleft import.
12. **regexlib.com, Chapman & Stolee, Hyperscan's own corpus** —
    deprioritized: licensing-unknown or content-inaccessible with the
    tools available this session; revisit only if a specific gap in
    the family taxonomy isn't otherwise filled.
13. **TextMate grammars** — interesting for the NEW "regex set applied
    in priority order per line" family (ties to Vectorscan's own "regex
    set" workload concept named in the brief — see note 2), but needs
    its own small side-investigation (which grammar, what licence)
    rather than a general recommendation.

## (ii) Proposed family taxonomy for the capability-survey set

Each family names its stress MECHANISM, an example pattern (sourced
above where possible), and which [B7] roster engines are expected to be
UNABLE to run it and why. "[B7] roster" = RE2, Rust `regex`, Vectorscan,
Oniguruma, TRE/POSIX, pcre2, pcrec (APPROACH.md §5).

| family | mechanism | example (source) | expected `unsupported` |
|---|---|---|---|
| `wild-validators` | everyday shapes as actually pasted into code (email/IP/date/UUID) | OWASP validation regex, grok `BASE10NUM`/`UUID` | none — every roster engine should run these |
| `wild-log-parse` | compositional macro-expanded alternation, sparse-hit search over log text | grok patterns over `bench/loglines`-shaped text | none by construction, but PERFORMANCE should diverge sharply (this is the point) |
| `wild-waf` | large keyword alternations over adversarial input, post-transform semantics | ModSecurity CRS `@rx` rules | RE2/Vectorscan should run (no exotic constructs typically); TRE may lack case-fold parity for some forms — verify |
| `wild-ids-binary` | regex over raw/binary payload, byte-offset anchoring | Suricata `pcre:` rules | Vectorscan is the ENGINE THESE ARE WRITTEN FOR — include specifically to see if pcrec/others match its semantics |
| `wild-date-nlp` | huge multi-language alternation, ambiguous decomposition | rebar's `datefinder` pattern | none should refuse to COMPILE; compile TIME and artifact SIZE are the interesting axis |
| `redos-nested-quantifier` | `(a+)+`, `(a\|a)+`, `(.*)*` classes | curated from `awesome-redos-security` CVEs | RE2, Rust `regex`, Vectorscan should all be IMMUNE by construction (linear-time guarantee) — the headline capability contrast |
| `redos-alternation-overlap` | overlapping alternation branches forcing backtrack retries | CRS-style keyword lists, hand-reduced | same immunity expectation as above |
| `huge-bounded-repeat` | `{0,65535}`-class counts at scale | already `bench/bounded`'s territory — cite, don't duplicate | pcrec's own NFA-state/element caps (already measured, [B11.4]); RE2 has its own program-size limits |
| `wide-alternation` | thousands of literal/branch alternatives | already `bench/altwide`'s territory — cite, don't duplicate | libpcre2's compiled-size ceiling; pcrec's emit-size caps |
| `deep-nesting` | deeply nested groups/alternations (recursion-adjacent) | `bench/syntax`'s `recursion` family, extended | RE2/Vectorscan lack general recursion (`(?R)`, `(?1)`) entirely — a clean unsupported bucket |
| `backref` | `\1`, named backrefs, doubled-word/palindrome shapes | grok's implicit patterns, `bench/syntax`'s `backrefs` family (cite) | RE2, Vectorscan, Rust `regex` ALL refuse — the single cleanest, best-documented capability line in the whole roster |
| `lookaround-chains` | multiple/nested lookahead+lookbehind | Suricata negative-lookahead-style filtering rules (if found), `bench/syntax`'s `lookaround` family (cite) | RE2, Rust `regex` refuse general lookaround; Vectorscan supports a restricted subset — verify in note 2 |
| `unicode-property` | `\p{...}`, case-folding across scripts, not just Latin-1 | rust-regex `testdata/unicode*` | TRE/POSIX C-locale engines behave differently, not necessarily "unsupported" — a semantic-divergence case, not a refusal |
| `case-fold-pair` | ASCII and non-ASCII fold pairs | `bench/syntax`'s fold-pair witnesses (cite; pcrec's [FORM-CHAR] optimization already measured against these) | none refuse; PERFORMANCE mechanism divergence is the point (already partly measured) |
| `empty-match-loop` | patterns that can match the empty string inside a repeat | rust-regex `testdata/`'s empty-match files | correctness/infinite-loop-avoidance divergence, not a refusal — every engine must define SOME behavior |
| `long-literal-prefilter` | very long fixed-literal runs, testing required-code-unit / prefilter dismissal | `bench/loglines`'s own territory (cite) | none refuse; mechanism (DFA/prefilter route) divergence is the point |
| `binary-nonutf8` | regex over bytes that are not valid UTF-8 | Suricata rule payloads | Rust `regex`'s default `str`-based API refuses non-UTF8 input outright (must use its `bytes` API) — a real, citable capability line |
| `regex-set-priority` | many patterns matched against one input in priority/first-match order | TextMate grammars, Vectorscan/Hyperscan's own "regex set" workload (named in the brief) | this is a NEW measurement shape (multi-pattern-per-cell), not just a new pattern family — flag for the design note as a possible scope decision, not assumed in |

## (iii) Edge-case catalogue with a source per shape

- **ReDoS-class nested quantifiers** (`(a+)+b`, `(a|a)*`, `(.*)*`) —
  sourced from `awesome-redos-security`'s CVE index and Davis et al.'s
  findings (items 13, 12); RE2's `regexp_benchmark.cc` `Hard` pattern is
  a related-but-distinct "unanchored leading star, late anchor" shape
  (ambiguous decomposition without a repeated GROUP) worth keeping
  SEPARATE in the taxonomy from true nested-quantifier ReDoS, since
  they stress different automaton properties.
- **Huge counted repeats** (`{0,65535}` and beyond) — already
  `bench/bounded`'s territory (`bench/bounded/NOTES.md`, not re-read in
  full this session but its role is stated in `APPROACH.md`/plan.md);
  no new source needed, cite and extend if the capability set wants a
  cross-engine (not just pcrec-vs-pcre2) reading of the same rungs.
- **Wide alternations** — already `bench/altwide`'s territory; grok's
  `MONTH`/timezone-name lists and rebar's `datefinder` pattern are good
  WILD examples of "alternation that grew organically" to contrast with
  `bench/altwide`'s synthetic ladder.
- **Deep nesting** — `bench/syntax`'s `recursion` family (balanced
  parens, `(?R)`/`(?1)`/named-subroutine spellings) is the existing
  source; TextMate grammars (item 18) are a WILD source of deeply
  nested `begin`/`end`/`patterns` grammars, though the nesting there is
  at the GRAMMAR level (multiple patterns), not necessarily inside one
  regex's own group structure — a distinction worth being precise about
  in the design note.
- **Unicode properties** — rust-regex's `testdata/unicode*.toml` files
  (item 5) and `bench/syntax`'s existing `uniprop` family
  (`\p{L}+`/`\P{L}+`, currently over Latin-1 bytes only per NOTES.md);
  the charter's room for a `bench/syntaxutf` sibling (already named in
  `bench/syntax/CLAUDE.md`) is the natural home for a deeper pass.
- **Case-folding** — grok's/OWASP's validators (ASCII-only folding) vs.
  rust-regex's unicode test files (full Unicode case folding) give a
  natural ASCII-vs-full-Unicode contrast pair; `bench/syntax`'s five
  fold-pair witnesses (NOTES.md) are the existing narrow-scope version.
- **Empty-match loops** — rust-regex `testdata/`'s dedicated empty-match
  test files (item 5) are the best-documented source; PCRE2's testdata
  almost certainly has its own (unconfirmed this session, OWED).
- **Long literals** — grok's `WINPATH`/`URIPATH` and Suricata's
  `content:`-preferred-over-`pcre:` convention are both indirect
  evidence that "long literal, prefilter-dismissable" is the COMMON
  case in real use, not an edge case — worth stating plainly in the
  design note rather than treating it as exotic; `bench/loglines`
  already covers this mechanism directly.
- **Anchors with multiline** — `bench/syntax`'s `anchors` family already
  covers `^`/`$`/`\A`/`\Z`/`\z`/`\G`/`(?m)` distinctions; grok patterns
  are typically single-line (log lines), so add little new here;
  TextMate grammars, which ARE inherently line-oriented multiline
  matching over a whole buffer, are the more interesting wild source if
  this family gets extended.
- **Lazy vs. greedy** — `bench/syntax`'s `quantifiers` family already
  covers this narrowly (`".*?"` vs `.*`); grok's `DATA`/`GREEDYDATA`
  pair (item 10, lines 15-16 of the sample) is a directly-named WILD
  instance of exactly this distinction, used deliberately by grok's own
  authors as two DIFFERENT named patterns for the two behaviors — a
  nice real-world confirmation that the distinction matters in practice.
- **Lookaround chains** — `bench/syntax`'s `lookaround` family (single
  lookarounds); a genuinely CHAINED/nested multi-lookaround wild
  example was not found this session (OWED — Suricata's HTTP rules or
  CRS's more elaborate rules are the most likely place to look next).

## (iv) What the existing bench already covers (do not duplicate)

- `bench/syntax` (@0.1, [B36]) already does a REGISTRY-DRIVEN construct
  census: 95 patterns, 18 mechanism families (literal, anchors,
  assertions, classes, quantifiers, groups, alternation, backrefs,
  lookaround, conditionals, recursion, modifiers, escapes, misc,
  uniprop, verbs, extclass, floor), each ONE construct in an otherwise
  plain body, with control-pair discipline (R3) and five fold-pair
  witnesses already tied to a measured pcrec optimization ([FORM-CHAR]).
  [B42] should NOT re-do this; it should ask what `bench/syntax`
  structurally CANNOT do (one construct at a time, hand-authored
  bodies, no wild provenance) and fill exactly that gap.
- `bench/altwide` (@0.2) already does the wide-alternation depth probe
  (8..4096 branches × first-byte/prefix/suffix structure).
- `bench/bounded` (@0.3) already does the counted-repeat depth probe
  (a count ladder to PCRE2's 65535 ceiling, refusal as a first-class
  outcome, near-miss match shapes).
- `bench/loglines` (@0.1) already does mostly-failing search-text
  throughput, shaped around PCRE2's required-code-unit dismissal.
- `bench/email` (RFC 5322 specimen) already does one canonical
  real-world-shaped pattern family in depth, with a floor pattern and
  periodic/non-periodic large subjects.
- None of the five existing sets claim WILD PROVENANCE — every pattern
  in every existing set is hand-authored (from `man pcre2pattern`, from
  the registry seed, or from first-principles) per each set's own
  NOTES.md/blinding statement. [B42] requirement (1) is therefore
  genuinely NEW work, not an overlap risk, provided the design note
  keeps mechanism-level overlaps (backrefs, alternation, bounded
  repeats, uniprop) CITING the existing depth sets rather than
  re-measuring them shallowly.
- The record schema, harness, adapters, and reporter are ALL already
  built and general ([B1]-[B34] per plan.md) — [B42] is a NEW sub-bench
  (or `bench/syntax` extension, per the charter's own open question) on
  EXISTING infrastructure, not a new component.

## (v) Questions for Frank

1. **Licensing floor.** Several of the highest-value sources (Suricata/
   ET rules, ModSecurity CRS, GNU grep's test suite) carry licence
   complications ranging from "mixed by rule range" to "GPLv3
   copyleft." Should [B42] (a) import verbatim patterns only from
   sources with an unambiguous permissive licence confirmed per-file,
   (b) treat a small number of individually-attributed patterns
   (quoted for illustration/research, as CVE descriptions or single
   named rules) as fine regardless of the source repo's overall
   licence, or (c) something else? This determines whether GNU grep and
   the messier parts of the Suricata rule sets stay in scope at all.
2. **How much wild vs. designed.** The existing five sets are 100%
   hand-designed (deliberately, per each one's blinding statement) —
   should [B42] be majority-wild (most patterns carry an external
   provenance citation) or a MINORITY of wild "anchor" patterns
   alongside a majority of hand-designed edge cases INSPIRED by wild
   findings (e.g., a ReDoS shape inspired by a CVE but written fresh to
   avoid the licence question entirely)? The charter's wording
   ("patterns from the WILD where possible") reads as a preference, not
   a fixed ratio — a number or rough ratio would help size phase (e).
3. **Subject-data provenance.** Several of the strongest wild-pattern
   sources (Suricata, CRS) have NO bundled haystacks — real subject
   data would need to come from traffic captures or attack-payload
   corpora with their own licensing questions, or from SYNTHETIC
   subjects typed to the pattern (as every existing set already does).
   Should subject text for wild-provenance patterns be (a) synthetic
   and hand-typed like today's sets (safest, most consistent with
   existing discipline, but loses "wild data too" as a property), or
   (b) drawn from a specific public, license-clear corpus per family
   (e.g. CPython source for code-shaped patterns, a public pcap corpus
   for IDS-shaped patterns) — and if (b), does Frank have a preferred
   corpus per family, or should the design note propose one per family
   for review?
4. **Davis et al.'s corpus specifically.** This is the single biggest
   potential source (537,806 regexes) and its availability/licence is
   the biggest open question in this survey. Worth a dedicated OWED
   follow-up (fetching the full paper PDF and checking for an
   artifact/Zenodo link) before the design note is drafted — should
   that follow-up happen now (a short focused re-check) or does Frank
   already know its status?
5. **The `regex-set-priority` family** (§ii's last row: many patterns
   matched in priority order against one input, as TextMate grammars
   and Vectorscan's own "regex set" workload both do) is a genuinely
   NEW measurement SHAPE — every existing pcrec-bench cell is one
   pattern against one testee. Is a multi-pattern-per-cell measurement
   in scope for [B42] at all, or should it be named as future work and
   left out of the v1 design (given requirement (7)'s explicit
   "later effort" framing already applies to the public interface —
   should regex-sets get the same "not now" treatment)?

## What I could not fetch (honesty summary)

- Davis et al.'s actual corpus file/artifact (only the arXiv abstract).
- Chapman & Stolee's paper body and any released dataset (ACM
  paywalled; search snippets only).
- The Zenodo ReDoS artifact's content and licence.
- regexlib.com's actual pattern-database rows (only confirmed the site
  is live and found its site-source GitHub mirror).
- PCRE2's `testdata/` directory listing and file content (found the
  RunTest/pcre2test tooling description, not the files themselves).
- Oniguruma's test suite file (repo found, test file not located).
- GNU grep's own `tests/` tree (only gnulib's shared `regex.c`/`.h`
  found; grep's own test suite location not confirmed).
- A `pcre:`-bearing Suricata rule file (fetched one rules file, which
  by chance carried no `pcre:` rules — a real, reported result, not a
  failure, but it means no Suricata sample pattern is quoted above).
- A ModSecurity CRS rule file's actual content (found the project and
  its licence, not a rule file).
- A TextMate grammar file's actual regex content.
- Rebar's other named benchmark files beyond `date.txt` (AWS-key
  detection, the lexer benchmark, the Unicode-word benchmark).
- Independent LICENSE-file confirmation for: PCRE2, Oniguruma,
  Hyperscan/Vectorscan, rust-lang/regex, GNU grep, Elastic's plugin,
  ModSecurity CRS — all stated above from well-known general knowledge
  or a WebSearch snippet, flagged individually where used, and each one
  low-risk to be wrong but NOT independently verified against a fetched
  LICENSE file this session, per the "fetched, not remembered" bar this
  task set. A short dedicated pass fetching just the LICENSE files for
  the sources on the final shortlist (rebar, PCRE2, grok patterns, CRS,
  RE2) would close this gap cheaply before the design note is written.
