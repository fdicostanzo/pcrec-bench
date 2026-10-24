# subst_bench_v1 -- the SUBSTITUTION mini-bench (plan row [B140], inbox I-157)

STATUS: DRAFT v0.1, 2026-10-24, lane b140design. DESIGN ONLY: nothing here is
built, installed, measured or pinned. Governing: Frank's request relayed in
inbox I-157 ("half a dozen cases, mostly reading large files and making edits,
then set up competitors"; sd and ripgrep approved in principle). Subject side:
pcrec's compiled substitution ([M4-SUBST], contract
`docs/spec/subst_api.md` on pcrec branch `lane/substland`, read at its tip on
2026-10-24; pin only after it lands on pcrec main -- I-157). Engine-neutral
where it must be (R-BENCH-4): the cases, subject and expectations name no
engine; each engine/tool gets its dialect of one neutral template.

## 0. What is new relative to every existing set

Every existing sub-bench times a MATCHER and compares ANSWERS (first span,
non-overlapping count). Substitution times a TRANSFORM: the answer is an
output byte string, hundreds of MB long, and the cost has three parts the
matcher benches never separate -- find, render, and write. Two consequences
drive the design: (1) the correctness gate is an output hash, not a span; (2)
two kinds of competitor exist that cannot share one ranking (an in-process
library call vs a process a user launches), so they are two TIERS, reported
separately and never in one column ordering.

## 1. The six cases

One subject (section 2), six (pattern, template) pairs. Patterns are written
in the common subset of PCRE2 / Rust regex (`unicode(false)`) / RE2 / POSIX ERE
(GNU sed -E) / perl / python re, so every engine reads the same pattern TEXT.
Templates are stored once in a NEUTRAL form (section 5.2) and rendered to each
dialect. All text is ASCII; tools run under `LC_ALL=C`.

| # | id | pattern | template (neutral) | density on the subject | what it isolates |
|---|----|---------|--------------------|------------------------|------------------|
| 1 | `literal` | `HTTP/1.1` | `H1` | ~1 per line on ~85 % of lines | the COPY-COST FLOOR: a pure literal, shortening replacement; every engine has a literal fast path, so this is mostly memchr/memmem + memcpy + write |
| 2 | `rare` | `/(?:phpmyadmin\|wp-admin)/[a-z]+\.php` | `/BLOCKED` | ~1 per 10,000 lines (planted, count in the manifest) | SEARCH-dominated: output is the input to within a few bytes; the cost is the scan over ~300 MB with a two-literal alternation prefix |
| 3 | `dense` | `[0-9]+` | `N` | ~25 per line, every line edited | OUTPUT-dominated: tens of millions of matches; per-match overhead and render/append cost |
| 4 | `reorder` | `([0-9]{2})/([A-Z][a-z]{2})/([0-9]{4})` | `$3-$2-$1` | exactly 1 per line (the `[17/May/2015:...]` stamp) | CAPTURE REARRANGEMENT: three groups, group order permuted, no case change (17/May/2015 -> 2015-May-17) |
| 5 | `mask-ipv4` | `\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b` | `x.x.x.x` | 1 per line (client address) + occasional referer/query addresses | CLASS-HEAVY masking: bounded counted classes, a word-boundary, a fixed-text replacement |
| 6 | `upper` | `/(blog\|images\|downloads\|static)/` | `/\U$1\E/` | ~60 % of lines | CASE CHANGE in the template (`\U`): PCRE2 `SUBSTITUTE_EXTENDED`, pcrec `subst-extended` module |

Notes per case:

* Case 1 is the one place a "literal" engine path matters; keep the pattern a
  true literal (no metacharacters, so `sd -F`/`rg -F` equivalence is not
  needed -- they get the same text and treat it as a regex that happens to be a
  literal; the tools' own literal optimisations are the thing under test).
* Case 2's pattern is chosen because both alternatives start with `/` and are
  followed by a class run: it does not reduce to one memmem, so it exercises
  each engine's multi-literal prefilter without being a single literal.
* Case 3: `[0-9]+` has one answer under leftmost-first and leftmost-longest
  alike (greedy = longest), so POSIX sed agrees by construction. Output is a
  FEW bytes per match, so the output is shorter than the input.
* Case 4: no `\s` and no negated class anywhere in cases 1-6, so no match can
  span a newline -- the whole-buffer engines (library tier, python block mode)
  and the line-streaming tools (sed, perl -p, sd 1.1, rg) see the same matches.
  The generator ensures the only `dd/Mon/yyyy` in a line is the timestamp.
* Case 5: the realistic false-positive is a four-part version in a UA string
  (`Chrome/32.0.1700.77`); with `\b` and `{1,3}` it does NOT match (the third
  part has four digits), and all engines agree. The gate would catch it
  otherwise. An e-mail masking variant (`[A-Za-z0-9._]+@[A-Za-z0-9.]+\.[a-z]+`)
  is a possible case-5b; left to Frank (Q4) because it needs a planted-email
  density decision.
* Case 6 is the only case with a per-engine support split (section 1.1).

### 1.1 Expected divergences, by case and competitor (declared BEFORE any run)

`bench/subst/divergences.tsv` (one row per DECLARED expectation of difference;
an undeclared difference found by the gate is a FAILURE of the set, not a
result):

| case | competitor | expectation | reason |
|------|-----------|-------------|--------|
| 1-5 | all | agree (output sha256 == PCRE2's) | patterns unambiguous under both disciplines (leftmost-first == leftmost-longest here); no cross-line match possible |
| 6 | GNU sed -E | agrees, dialect `\U\1\E` | GNU extension; supported |
| 6 | perl | agrees, dialect `\U$1\E` | native |
| 6 | python `re.sub` | `unsupported` (template) | `re` templates have no case operators; a callable (`lambda m: ...`) is a DIFFERENT feature, not recorded as the template case (Q5 asks whether to add it as an informational row) |
| 6 | Rust `regex`, RE2, sd, ripgrep | `unsupported` | no case forcing in the replacement syntax; Rust's `Replacer` closure is the same situation as python's callable |
| 6 | pcre2-interp / jit | agrees, `SUBSTITUTE_EXTENDED` | the baseline (the expectation is derived from it) |
| 6 | pcrec | agrees, `subst-extended` module compiled with `\U$1\E` | contract section 2 paragraphs 7 and 14; [`\U` regions persist to `\E` or the end]. Under `-e byte` ASCII case only -- our subject is ASCII |
| all | any | line-final: subject ends with exactly one `\n` | removes the "missing final newline" divergence class (sed/perl preserve it, python/sd treat it variously) |
| 1-6 | `rg --passthru -r` | agrees on content; verify NO added/removed bytes | rg may add a trailing newline to the last line if absent; same remedy |

An `unsupported` competitor is a first-class outcome (like `did-not-compile`
in the bounded set): the row exists, carries a reason token, is excluded from
timing and from the ranking, and is SHOWN in the report -- not dropped (I-157).

The sed leftmost-longest hazard I-157 names is real in general
(`foo|foobar` would differ) but none of the six patterns has a prefix-ambiguous
alternation: case 2's alternatives diverge at the first byte after `/`, case 6's
likewise. The design records this as a pattern-authoring rule for any later
case: "an alternation's alternatives must not be prefixes of one another" --
checked mechanically by the gate, not by reading.

## 2. The subject

### 2.1 Choice: a deterministic GENERATOR, not a tiled sample

Candidates examined (pcrec `third_party/`, read 2026-10-24):

* `elastic-examples-apache-logs-bc53b584/apache_logs.txt` -- real Apache
  combined log, Apache-2.0 (redistribution permitted, LICENSE vendored), but
  only a 1,000,000-byte TRIM of a 2,370,789-byte original. Reaching a few
  hundred MB means tiling 130-330 copies: a perfectly periodic file (the
  `periodic` hazard [B17] already flagged: exact repetition lets branch
  predictors and caches learn the whole file's match structure, and every
  `dense`/`rare` count becomes N x a constant).
* `synth-log-lines-v1/synthetic_log_lines.txt` -- 999,960 B, MIT (authored
  there), HDFS-DataNode shape: 6-digit `YYMMDD` dates, IPv4:port pairs, no
  `dd/Mon/yyyy` stamp, no URL paths, no e-mail. It fits cases 3 and 5 only;
  it lacks the timestamp shape of case 4 and the path shapes of cases 2 and 6.

Decision: **a new generator in `bench/subst/`** (`gen_subjects.py`, seeded,
MIT as authored here, no third-party text copied) producing an Apache
combined-format access log. The real elastic sample is used ONLY as a
structural cross-check (line-length distribution, field presence, status mix),
cited in the provenance note, not redistributed and not tiled. Reasons: (a)
non-periodic by construction at any size; (b) all six shapes are present with
planted, countable densities; (c) the same recipe scales (a 16 MB gate slice
and the full file are prefixes of one stream); (d) no licence entanglement.
The combined format matches what "reading large files and making edits" means
to an operator (access logs are the canonical case).

Line shape: `IP - - [dd/Mon/yyyy:HH:MM:SS +0000] "METHOD /path HTTP/1.x" STATUS BYTES "REFERER" "UA"\n`
with vocabularies authored in the generator (paths under
`/blog|/images|/downloads|/static|/presentations|/...`, ~40 user agents,
status mix 200/304/404/500). Planted: the `/phpmyadmin/*.php`, `/wp-admin/*.php`
lines at exactly 1 in 10,000 (case 2); the IPv4 appears as client address on
every line and in the referer on ~3 % of lines (case 5).

### 2.2 Size and manifest

Target about 320 MB (1,600,000 lines at ~200 B/line; exact bytes fixed when the
generator is built and recorded in the manifest). "A few hundred MB" is Frank's
number; the table of Q1 offers 256 / 320 / 512 MB. Two files from ONE stream:

| id | lines | bytes (approx) | role |
|----|-------|----------------|------|
| `acc-gate` | 80,000 | ~16 MB | the correctness gate + smoke subject: cheap enough to run in `make check` (all six cases x every competitor, seconds) |
| `acc-main` | 1,600,000 | ~320 MB | the timed subject; `acc-gate` is a byte prefix of it |

`manifest.tsv` (as bench/loglines): `id, bytes, lines, sha256, periodic=no`,
plus a per-case planted-count column set (`n_rare`, `n_date`, `n_ipv4`) so the
gate can state its own expected match counts independent of any engine. The
files are GENERATED and GITIGNORED (like bench/email subjects); `make check`
re-derives `acc-gate` and compares its sha256 to the manifest, and checks that
`acc-main`'s first N bytes equal `acc-gate` WITHOUT generating all of
`acc-main` (the generator is a stream, so it can stop at the line count).

## 3. The two tiers

The tiers differ in WHAT they time, so they are two sub-bench regimes' worth of
testees with separate report sections. The same six cases, the same subject,
the same expectation file; never one ranking.

### 3.1 LIBRARY tier -- "times only the work"

In-process, the subject read once into one memory buffer (untimed), the
transform timed, output into memory (untimed afterwards: hashed or written for
the gate on a separate, untimed final pass, section 6).

| testee | call | notes |
|--------|------|-------|
| `pcre2-jit`, `pcre2-interp` (BASELINE) | `pcre2_substitute(code, s, n, 0, PCRE2_SUBSTITUTE_GLOBAL [\| PCRE2_SUBSTITUTE_EXTENDED for case 6], md, NULL, repl, repl_len, out, &outlen)` | the compatibility baseline named in I-157. Output buffer pre-sized to a bound (cap = n + matches*max_growth; section 3.1.1) so NO NOSPACE retry in the timed loop -- libpcre2's retry re-matches (contract section 9 #7) and would otherwise be a timing artifact. `pcre2_substitute` uses JIT automatically when the code was JIT-compiled and the match data/context allow; `pcre2-interp` is the same call without `pcre2_jit_compile`. `pcre2_substitute` in 10.46 and ill-formed input: not relevant (ASCII) |
| `pcrec-auto`, `-vm`, ... | `rx_subst_replace_all(rx->next_n, &it, &info, &ctx, map, flags, &o, out, cap, &len)` (contract 6.8/6.9) | per the contract: one compiled artifact = pattern + template (`pcrec -p NAME --subst TEMPLATE`), caller buffer. Two reported timings per cell (3.1.1): render-only with a known capacity, and size-then-render (`out == NULL, cap == 0`, then the real call) |
| `rust-regex` | `regex::bytes::Regex::replace_all(&[u8], &[u8])` | `bytes::Regex` built with `unicode(false)` so `\b`, `[0-9]` are byte-level and the engines agree. The returned `Cow<[u8]>` allocates inside the timed region -- intrinsic to the API; documented as a reading note, not engineered away (a hand loop over `captures_iter` into a reserved `Vec` would be a different, non-idiomatic competitor) |
| `re2-default` | `RE2::GlobalReplace(std::string*, const RE2&, StringPiece rewrite)` | rewrite syntax is `\1`..`\9`, `\0`; `$` is literal -- the neutral template's per-dialect render handles it. GlobalReplace edits a `std::string` IN PLACE: each timed iteration needs a fresh copy of the 320 MB subject, made OUTSIDE the clock (a `memcpy` before the first read; the iteration count is 1 per trial anyway, section 3.1.2). Matching is Perl-leftmost-first (the `re2-default` config), so agreement with PCRE2 holds on all six patterns |
| Oniguruma, TRE, Vectorscan | sit out | no usable substitute API (I-157). Listed in the report's header as `not in this set`, not as `unsupported` per case |

Case 6 on Rust and RE2: `unsupported` (1.1).

#### 3.1.1 Output sizing, and pcrec's sizing mode

The contract's two modes map onto two honest usage patterns, so BOTH are
timed and reported as separate testee-labelled columns rather than one:

* **bound** -- caller supplies cap >= a provable upper bound. For these cases
  that is `n + matches * extra`, with the largest per-match growth computed
  from the template (cases 1-3 shrink; 4-6 keep length or grow by at most
  7 B). The bench uses cap = `n + 8 * n_matches_upper` where `n_matches_upper`
  is the PLANTED/oracle count -- an engine-neutral number from the manifest,
  so no competitor is advantaged by a bound it computed. pcre2 and pcrec both
  run this way; RE2/Rust allocate for themselves.
* **size-first** -- pcrec `out == NULL, cap == 0` returns the length, then a
  second call renders (the contract's NOSPACE-free path); the PCRE2 analogue
  is `PCRE2_SUBSTITUTE_OVERFLOW_LENGTH`, whose NOSPACE retry re-matches. These
  two are reported as `pcrec-*-sizefirst` and `pcre2-*-sizefirst` (the
  contract's section 9 #6/#7 differences are exactly what this column
  measures: pcrec's size pass renders pieces once and the second call
  flattens the same pieces; pcre2's retry searches twice).

pcrec's `support` unit (`--emit-support`, contract section 10) is compiled
once into the driver; `PCREC_SUPPORT_STATIC` per section 10 para 3a so the
driver carries a private copy. The artifact per case is compiled in the
adapter's compile step (a new artifact kind: pattern + template, two inputs).

#### 3.1.2 What the driver protocol must grow (section 5 details the records)

`pcrecbench/adapters.py` documents ONE protocol: `--pattern FILE --list
SUBJECTS.tsv --mode search|match --iters N [--find-all]`, output lines
`info`, `compile`, `subject`, `error`. A substitution driver needs, additively:

* `--mode subst` with `--template FILE` (raw bytes, already in that engine's
  dialect -- the adapter renders the neutral template) and `--subst-flags
  extended|none`. `--find-all` is meaningless there (inert/refused).
* the 11-column `subject` line is reused with: ANSWER = `match` if the number
  of substitutions > 0 else `nomatch`; START/END = `-`; NCAPS = 0;
  CONSUMED = subject bytes; ITERS = 1 (see below); SECONDS = the timed
  region; **NMATCHES = the number of substitutions** (the existing column,
  same meaning: matches replaced), CAPS = `-`.
* one NEW line kind, emitted after the subject's timing, outside the clock:
  `out<TAB>ID<TAB>PATH<TAB>BYTES` -- the driver writes its final output to
  `--out-dir/PATH` and the harness hashes it (sha256), then deletes it. This
  keeps SHA-256 out of four drivers (C x3, C++, Rust) and out of the timed
  loop. Parsers that do not know `out` lines must ignore them; the harness
  parser is taught the kind in the same change. Since a hash of a 320 MB
  buffer in python is ~0.5 s, it is done once per (cell, case), not per trial:
  trial 1 writes the output; trials 2..N write nothing but are checked by
  OUTPUT LENGTH + NMATCHES (cheap, and a length/count change vs trial 1 is a
  determinism fault).
* **iters = 1.** A 320 MB transform takes 0.3-30 s; the existing `iters`
  calibration (many iterations per clock reading) is for 100 ns operations.
  Trials (5, odd, to meet the v1.4 trial-agreement rule's N >= 5) are the
  repetition. The `timed_run()` instrument files (`timed.c`/`timed.cc`/the
  rust-timed crate, BD16) are INSTRUMENTS: this needs a new `timed_subst()`
  per driver and a plan row + re-pin-control run per BD16.

Each existing driver grows a subst mode (pcre2: ~120 lines C around
`pcre2_substitute`; pcrec: shim + driver around the subst artifact and the
support unit, plus the two-input compile in `adapter.py`; rust: a `bytes`
replace_all branch; re2: GlobalReplace branch). No existing mode changes by a
byte (additive, like `--prime`).

### 3.2 TOOLS tier -- "what a user would run"

Wall time of the whole process, including process start, file read, the
transform, and output file write. The measurement unit is the COMMAND.

| tool | command (case 3 as the example) | notes |
|------|---------------------------------|-------|
| GNU sed 4.9 | `sed -E 's/[0-9]+/N/g' acc-main > out` | leftmost-longest (POSIX ERE); line-streaming; `\U` supported (GNU extension) |
| perl 5.40.1 | `perl -pe 's/[0-9]+/N/g' acc-main > out` | `-p` line loop; PCRE-class backtracking engine; `\U..\E` native |
| python 3.14.4 | `python3 subst.py CASE acc-main out` (a committed 15-line script doing `re.sub` on BYTES, `re.ASCII`) | whole-file `data = f.read(); out = re.sub(pat, repl, data)` -- the idiomatic "edit a file" script; a streaming variant is Q6. Include interpreter start (~20 ms: honest, and small against seconds) |
| sd (v1.1.0) | `sd 'PAT' 'REPL' acc-main` is IN-PLACE by default; the bench uses `sd 'PAT' 'REPL' < acc-main > out` (stdin to stdout) | to keep every tool reading a file and writing a file on the same footing: stdin redirected from the file, stdout to `out`. sd 1.1.0 processes line-by-line by default, `--across`/`-A` for whole-buffer (release notes) -- the bench records WHICH it ran (default) in the testee description. Regex: Rust `regex` syntax; replacement `$1`/`${1}`; no case operators |
| ripgrep 15.2.0 | `rg --no-config --passthru -N --no-heading --color never -r REPL PAT acc-main > out` | `--passthru` prints every line, replaced where matching; `-N` no line numbers, `--no-heading`, `--color never` and `--no-config`/no `RIPGREP_CONFIG_PATH` so output is exactly the transformed file; Rust regex; replacement `$1`/`${1}`; no case operators. Binary-file detection: input has no NUL, so none triggers |

Measurement protocol for the tier (one cell = one tool x one case):

* **Fresh launches:** 5 per (tool, case) -- the v1.4 trial-agreement rule needs
  N >= 5 odd; each launch is a new process (the cost under test). Round-robin
  INTERLEAVED across the tools within a case and across the six cases'
  rotations, so a drifting thermal/governor state does not sit on one tool.
  Wall seconds of 320 MB runs are large against launch jitter; the real risk
  is cache state, below.
* **Core:** `taskset -c N` on the same single quiet core the other windows use
  (BOILERPLATE: schedutil makes cold-core runs unreliable; pin). `taskset`
  pins the whole process tree (python, perl are single-threaded; rg and sd
  parallelise by file, and with ONE input file rg uses a single search thread
  -- recorded, and `-j1` is passed to rg anyway so thread-count is not a
  confound; sd has no threads on one file). The harness gate's pre-flight
  (occupancy of the target core) applies unchanged.
* **Page cache:** WARM, by construction and recorded: one untimed `cat
  acc-main > /dev/null` immediately before each tool's block, then `fincore`
  (util-linux, present on the box -- verify at build time) on the input
  asserting 100 % resident, value stored in the record. A cold-cache variant
  would need root (`drop_caches`) or a larger-than-RAM file; the box has no
  root -- recorded as out of scope, not hidden. The file is 320 MB against a
  RAM large enough to hold subject + output twice (check at build time).
* **Output:** to a FILE on the same filesystem as the input (`/var/tmp/
  pcrecbench/subst/`, disk-backed, NOT the 7.6 GB per-user tmpfs `/tmp`, which
  a 320 MB output x several concurrent sets would exhaust), because a user
  editing a file writes a file. The timed command includes the redirect. Then,
  untimed: `sha256sum out` for the gate (once per (tool, case), the first
  trial; later trials check `stat` size and are not re-hashed -- section 3.1.2's
  determinism rule), delete. A **`/dev/null` variant** (the same command with
  `> /dev/null`) is an OPTIONAL second column `-null` that separates the
  write cost; it doubles the cells so it is Q7, default OFF.
* **What is clocked:** `os.posix_spawn` of `taskset -c N <cmd>` from the
  harness, `time.perf_counter_ns()` around spawn..wait4, and `wait4`'s rusage
  (user+sys CPU, maxrss) STORED as provenance. The `taskset` exec itself is
  <1 ms; `os.wait4` gives rusage without `/usr/bin/time` (not guaranteed
  installed). No shell in the path: argv list, the redirect done by opening the
  output fd in python and passing it as stdout (so `sh -c` start cost is not in
  the number).
* **Memory is reported, not ranked:** maxrss is shown beside wall time (python
  holds ~1 GB for read + sub; sed/perl/rg hold KBs-MBs; sd 1.1 line-by-line vs
  `-A` would differ by orders).

TOOLS-tier case 6: sed and perl run; python, sd, rg are `unsupported`.

## 4. The correctness gate (before ANY timing)

1. **Expectations** (`bench/subst/expectations.tsv`): per (case, subject) the
   PCRE2 oracle's output length, SHA-256 and substitution count, derived by
   `pcrecbench/oracle_pcre2.py` grown a `substitute()` (ctypes over
   `pcre2_substitute`, SUBSTITUTE_GLOBAL, EXTENDED for case 6) -- the same
   `libpcre2-differential` method as every other set, one more entry point in
   the same module (no second oracle). Alongside it, an ORACLE-INDEPENDENT
   count (the planted counts from the manifest; case 3 and 4's counts also
   re-derived by a 20-line python loop with no regex) to catch a PCRE2 error
   from being the "truth" for everyone.
2. **The gate:** for every competitor x case on `acc-gate` (always) and
   `acc-main` (pinned tier): sha256 of its output == the expectation's. A
   mismatch is recorded as the cell's `answer` = `wrong` (the existing
   scoreboard excludes wrong answers from rankings -- APPROACH), with the first
   differing byte offset and the lengths (so a divergence is diagnosable: first
   120 bytes either side).
3. **Declared divergences** (1.1): a row whose mismatch is in
   `divergences.tsv` is recorded `divergent-declared` (shown, not ranked, not
   a failure of the set); a mismatch NOT in the file is `wrong` and fails the
   `make check` slice.
4. **Order:** gate (acc-gate, all competitors) -> gate (acc-main, once per
   competitor x case, untimed) -> only then timing. A competitor that fails
   the gate on `acc-main` is not timed for that case.
5. **Timing runs never gate each other:** the sha256 is taken on trial 1's
   output; all trials agree in output length and substitution count.

## 5. How the record schema carries it (proposed minimum; NOT implemented)

Current schema v1.8 (record_schema.md; schema/). Principle: reuse every
existing record, row kind and rule; add the least that lets a transform be a
first-class cell. Proposed **v1.9** (additive; v1.8 records stay valid):

### 5.1 The proposals

| # | change | why |
|---|--------|-----|
| S1 | `regime` enum += `substitution` (`setup.subbench.regimes`, `match_row.regime`) | a third thing to time; not comparable to the other regimes (the schema already says regimes are not comparable to each other, section 3) |
| S2 | `setup.testee.invocation` enum `library` (default when absent) / `process`; FILTERABLE | the TIER. The reporter never mixes values in one ordering |
| S3 | `match_row.subst` object, REQUIRED iff `regime` = `substitution`: `case` (string id), `nsubst` (int, the substitution count), `out_bytes` (int), `out_sha256` (64 hex), `gate` enum `agrees` `wrong` `divergent-declared` `unsupported` | the output is the answer. `answer` keeps its role (`match` = ran), and the existing rule X-style cross-check is "`out_sha256` equals the expectation's iff gate = agrees" |
| S4 | `match_row.unsupported_reason` (string token) for `gate` = `unsupported` | a dropped-by-design cell must say why; mirrors how `did-not-compile` carries its refusal class |
| S5 | `match_row.process` object, REQUIRED iff `testee.invocation` = `process`: `cmd` (argv array, with the subject/output paths elided to tokens), `wall_ns`... (the trial's seconds IS the existing `seconds` field -- wall including start), `user_s`, `sys_s`, `maxrss_kb`, `page_cache_resident` (fraction from `fincore`), `core` | provenance, not ranked, like the occupancy timeline |
| S6 | `setup.testee.engine_name` accepts the tool names; `engine_version` is the tool's `--version` string (normalisation rules extended to `sed (GNU sed) 4.9`, `perl v5.40.1`, `Python 3.14.4`, `sd 1.1.0`, `ripgrep 15.2.0`) | testee_id derivation (6.4) stays mechanical |
| S7 | compile rows: for `process` testees there is no separable compile; the tool is `interpretive` (re-parses the pattern each launch) and its compile row is OMITTED -- needs one rule relaxation: compile rows are optional when `invocation` = `process` (X-rule change). For LIBRARY testees the compile row is unchanged: pcrec's `compile` phases (emit-c, cc, subst artifact), pcre2's `compile`/`jit`, `cost_class` as today | the Tools tier's number already includes pattern compile; saying so is the honest alternative to inventing a compile figure |
| S8 | no change needed: `iters` = 1 is already legal, and a 320 MB `subjects[]` entry is how throughput subjects are carried already (`periodic` = no) | |

Validator impact: X-rules for (S3) presence/absence by regime, (S5) by
invocation, (S7) the compile-row relaxation, and a cross-check that the number
of match rows per (case, trial) is dense. `schema/examples/` gets one valid
subst record (library) and one (process); `examples/bad/` one per new rule.
`free_text` caps unchanged. S1-S8 are one design decision (v1.9).

### 5.2 The neutral template

`patterns/` holds, per case, `PATTERN.rx` (the pattern text) and
`TEMPLATE.neutral`: a tiny line-oriented IR, one segment per line --
`lit<TAB>TEXT`, `grp<TAB>N`, `upper<TAB>N` (group N upper-cased) -- rendered by
each adapter to its dialect: PCRE2/pcrec `$N` and `\U$N\E` (with `$$` for a
literal `$`); Rust/sd/rg `${N}`; RE2 `\N` (and `\\` for a literal backslash);
sed/python `\N` (python bytes template; `\g<N>` where a digit follows); perl
`${N}` with `\U${N}\E`. A literal `$`, `\`, `&` or `/` in a segment is escaped
per dialect by the adapter (none occurs in the six cases; the renderer's
escaping is exercised by a unit test with a deliberately hostile template,
the way KB-1's test was). Rendering from IR is what keeps "one template" true
across eight dialects.

## 6. The reporter view

New section kind, one table per tier, never merged:

* **LIBRARY** (rows = cases 1-6, columns = pcre2-jit [baseline], pcre2-interp,
  pcrec-auto, pcrec-vm, rust-regex, re2; second block `size-first` for pcrec and
  pcre2): median seconds, **MB/s of subject** (subject bytes / seconds -- the
  figure comparable across cases), and ratio vs the baseline cell
  (`pcre2-jit`), with the trial-agreement status (v1.4) in the cell's legend
  and the gate result as a glyph/word (`agrees` blank, `unsupported` shown as
  the word, `wrong`/`divergent-declared` shown with the diff offset). Matches
  per case printed under the case name (`n_subst`), since cases 3 vs 2 differ
  by ~5 orders of magnitude and the reader needs that to interpret anything.
* **TOOLS**: the same grid for sed/perl/python/sd/rg, each cell
  `median wall s (x.x MB/s)` with `maxrss` as a second line; the page-cache
  fraction and core in the header. Tool-tier ratios are vs `sed` (the
  traditional tool). No cross-tier ratio is printed by default (Q8): the
  report states "the tiers are not comparable".
* One summary row per case at the foot: the pcrec LIBRARY / best-other-library
  ratio, the only number pcrec's manager wants for outlier extraction
  (feeds the "outliers back to pcrec" loop, APPROACH) -- plus the rule that a
  `wrong`/`unsupported` cell is excluded from "best-other".
* Interpreter rules (catalogue) and the trend report are NOT touched; a new
  catalogue minor bump is a follow-up if Frank wants substitution cells in
  them.

Reporter code: a new `--grain subst` view (reduction = median over trials,
reusing `reduce.py`'s agreement logic), a legends block, and a regeneration of
no existing report (v-bump only for the new view).

## 7. Interactions and constraints

* **Box discipline:** timing needs a window cleared with Frank (I-157). A tools
  run of 5 tools x 6 cases x 5 launches on 320 MB: estimated 30-60 min dominated
  by python and sd (whole-file / per-line overhead of 1.6 M lines). The library
  tier is cheaper (<=15 min). The window script gets a `CELL_CAP` row for the
  new cells (the b32adp pattern).
* **Disk:** subject 320 MB + one output at a time (deleted after hashing);
  `/var/tmp/pcrecbench/subst/`; gitignored.
* **pcrec pin:** pinned only after [M4-SUBST] lands on pcrec main (I-157); the
  adapter work can begin against the `lane/substland` branch as a SCRATCH
  testee (`pcrec-local`, the provided-binary mechanism) without a pin.
* **Not in this set:** UTF-8 character mode (ASCII subject, byte engines;
  `bench/utf8` has the character-mode story), in-place editing (`sed -i`,
  `sd` default), multi-file trees (`rg` shines there; out of scope), stdin
  pipelines, multi-line patterns.

## 8. Open questions for Frank

1. **Size.** 256 MB / 320 MB / 512 MB? (Design assumes ~320 MB, 1.6 M lines;
   larger makes the Tools tier slower mostly for python and sd.)
2. **Subject.** Generator (recommended, 2.1) vs the real elastic Apache log
   tiled (rejected: periodic) vs tiled-with-offsets/rewrites (a hybrid that
   keeps real vocabulary but is more machinery). Approve the generator?
3. **Case 3 as `[0-9]+`** (output-dominated, ~25 matches/line, shortens) vs a
   density closer to "an edit on nearly every line" (one match per line,
   e.g. the status code). The design chose many-matches/line because that is
   the output-dominated regime I-157 names; one-per-line is case 4/5's shape.
4. **E-mail masking** (case 5b) alongside IPv4? Needs a planted-email density.
5. **Case 6 and callables:** record python/Rust closure replacement as an
   informational `callable` variant row, or keep strictly `unsupported`
   (recommended: unsupported; a closure is user code, not a template)?
6. **python tool:** whole-file `re.sub` (design) vs line-streaming loop vs both.
7. **`/dev/null` column** in the Tools tier (separates the output write)? Default OFF.
8. **Cross-tier ratios.** Print none (design) or an optional "process vs
   library" overhead column (start + I/O share)? It would be informative for
   pcrec as a command-line tool but invites unfair ranking.
9. **pcrec as a TOOL?** A tools-tier `pcrec`-generated binary (compile the
   artifact + a tiny main, run it as a process) would complete the picture
   (the "grep -r replacement" use) but is a different testee kind; defer?
10. **sd version/route:** sd's latest release (1.1.0) publishes no checksum
    file and is not on crates.io (crate stops at 1.0.0, whose default is
    whole-file, not line-by-line). See the manifest, section 9, and its
    decision request.
11. **pcre2_substitute and 320 MB:** `PCRE2_SIZE` output is size_t, fine; but
    pcre2 match data / JIT stack for a single 320 MB subject with 40 M matches
    needs a measured JIT-stack setting (`pcre2_jit_stack_create`) -- a build-time
    probe, flagged so the first dry run does not mistake a JIT-stack error
    (-46) for a result.

## 9. INSTALL MANIFEST (requested for approval; nothing downloaded or installed)

Rule (CLAUDE.md, I-157): pinned release, official source, published checksum
or crates.io `--locked`, installed inside the pcrec-bench tree only, never
system-wide; the exact files are approved by Frank before anything is fetched.
Looked up 2026-10-24 via `gh api` (release metadata) and `curl` of two small
text files (the ripgrep `.sha256` file, the crates.io index entries); no
binary was downloaded.

### 9.1 ripgrep 15.2.0 (BurntSushi/ripgrep)

* Latest stable release: **15.2.0**, published 2026-07-15T16:26:10Z; tag
  object `6ec72defacfb042f203ca0b4bf2513a0a5505a7e`.
* Artifact: `ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz` (2,265,718 B,
  static musl build -- no libc coupling to the box).
  URL: `https://github.com/BurntSushi/ripgrep/releases/download/15.2.0/ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz`
* **sha256 `33e15bcf1624b25cdd2a55813a47a2f95dbe126268203e76aa6a585d1e7b149c`**
  PUBLISHED by the project as a release asset:
  `https://github.com/BurntSushi/ripgrep/releases/download/15.2.0/ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz.sha256`
  (content: `33e15bcf...149c  ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz`;
  it also equals GitHub's own recorded asset digest -- two sources agree).
* Alternative (crates.io, `--locked`): crate `ripgrep` 15.2.0, checksum
  `a30750b6d0743bfdd2656ebbaf4555aa278c43144b84bc389bcbfa399485ec71`
  (`https://index.crates.io/ri/pg/ripgrep`, MSRV 1.85), `cargo install --locked
  --version 15.2.0 ripgrep --root <tree>/build/tools/ripgrep-15.2.0`. Needs
  compiling ~40 dependency crates (network at build time); NOT proposed since
  the checksummed static binary exists.

### 9.2 sd 1.1.0 (chmln/sd)

* Latest stable release: **v1.1.0**, published 2026-02-25T19:27:05Z; tag
  `v1.1.0` -> commit `4a7b216552d64134c0fa17a59b9d557d89019f0f`.
* Artifact: `sd-v1.1.0-x86_64-unknown-linux-gnu.tar.gz` (988,815 B; dynamic
  glibc) or `sd-v1.1.0-x86_64-unknown-linux-musl.tar.gz` (1,049,511 B; static;
  recommended for the same reason as rg).
  URLs: `https://github.com/chmln/sd/releases/download/v1.1.0/sd-v1.1.0-x86_64-unknown-linux-musl.tar.gz`
  (and the `-gnu` twin).
* **Checksum situation: sd publishes NO checksum file** (the release has the
  tarballs only). The only digest is the one GitHub computes and shows for each
  asset (API field `digest`, a property of the hosting platform, not an
  author-signed value):
  musl `sha256:02f00f4777d43e8e95b7b8d49e1a0d6e502fed4b8e79c1c8b8063857a30caa2e`,
  gnu `sha256:3613eca74cd686739bb5a6d68319aa56c747e7315274d02323a2ca2b1c5d82d2`.
* The crates.io route does NOT reach 1.1.0: the crate's newest published
  version is **1.0.0**, checksum
  `70613c41881ca1e5b69e6bb110f2ac499739c03a151b00e41e16090974b826a8`
  (`https://index.crates.io/2/sd`, MSRV 1.70.0), and per the 1.1.0 release
  notes 1.1.0 CHANGED the default (line-by-line, `--across/-A` for the old
  whole-file), so 1.0.0 would be a different competitor from "the latest sd".
* **Proposal / decision request:** per the rule ("or crates.io with --locked")
  the strictly compliant route is sd **1.0.0** via
  `cargo install --locked --version 1.0.0 sd --root <tree>/build/tools/sd-1.0.0`
  (checksum above; build needs the dependency crates from crates.io). The
  convenient route is the 1.1.0 musl tarball verified against GitHub's digest
  and then recorded by OUR sha256 in the manifest. These are different
  tools; Frank/Frank's rule-holder chooses. Recommendation: **1.1.0 musl tarball
  with the GitHub digest accepted as the published checksum for sd only**, the
  deviation recorded in the testee notes -- because benchmarking the version a
  user installs today is the point; if the rule is strict, fall back to 1.0.0
  from crates.io and declare the line-handling difference.

### 9.3 Install location

`build/tools/<name>-<version>/` inside the pcrec-bench tree: `build/` is
already gitignored (it holds `build/pcrec-<pin>` trees), so the binaries are
never committed, `make clean`-style removal is one directory, and the harness
resolves them from a fixed relative path (a new `testees/tools/tools.toml`
pinning name, version, sha256, path; the adapter REFUSES to run a binary whose
sha256 differs from the pin, the same posture as the pcrec pin script). Not
`third_party/` (that is for vendored SOURCE this project builds from) and not
`$HOME`/system paths. An `install_tools.sh` (to be written after approval)
downloads to a fresh empty directory, verifies the sha256 BEFORE extraction,
extracts there, copies only the binary into `build/tools/...`, and is
idempotent; it is run by the manager, once, and its output archived.

### 9.4 Tools already on the box (candidates for pinning; recorded, not installed)

| tool | version (probed 2026-10-24) |
|------|-----------------------------|
| GNU sed | `sed (GNU sed) 4.9` |
| perl | `perl 5, version 40, subversion 1 (v5.40.1) built for x86_64-linux-gnu-thread-multi` |
| python3 | `Python 3.14.4` |
| rustc / cargo (for the rust testee) | `rustc 1.98.1 (48a229cea 2026-09-01)`, `cargo 1.98.1 (797e8a9bc 2026-08-05)` |

System-pinned libraries the EXISTING testees use (library tier):

| library | version | where pinned |
|---------|---------|--------------|
| libpcre2-8 | `10.46-1build1` (Ubuntu package; `pkg-config` 10.46) | apt system package, probed live by `pcre2_config(PCRE2_CONFIG_VERSION)` per testees/pcre2 |
| RE2 | `libre2-11 / libre2-dev 20250805-1build3` (pkg-config 11.0.0 = the SONAME) | apt system package, `pkg-config`-discovered by testees/re2 |
| Rust `regex` crate | `1.13.1` | `testees/rust/Cargo.lock` (committed) |
| pcrec | none yet for subst: lane `lane/substland`, pin to follow | I-157 |

Since the sed/perl/python on the box are distro-provided and change with
`apt upgrade`, pinning means RECORDING the version string in every record
(S6) and refusing a record when it differs from the pinned manifest value (the
same discipline as the pcre2 testee's live-probed version) -- not installing
copies.

### 9.5 Ready-to-paste outbox paragraph

> **O-? (b140design, 2026-10-24) -- [B140] install manifest for I-157: please
> approve the exact files.** Nothing has been downloaded. Install location,
> both: `build/tools/<name>-<version>/` inside pcrec-bench (gitignored),
> sha256-verified before extraction, binary path pinned in a new
> `testees/tools/tools.toml`. (1) ripgrep **15.2.0**:
> `https://github.com/BurntSushi/ripgrep/releases/download/15.2.0/ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz`,
> sha256 `33e15bcf1624b25cdd2a55813a47a2f95dbe126268203e76aa6a585d1e7b149c`,
> published by the project in the release asset
> `ripgrep-15.2.0-x86_64-unknown-linux-musl.tar.gz.sha256` (and equal to
> GitHub's digest). (2) sd **1.1.0** (latest; the project publishes NO
> checksum file, and the crates.io crate stops at 1.0.0 with a different
> default): `https://github.com/chmln/sd/releases/download/v1.1.0/sd-v1.1.0-x86_64-unknown-linux-musl.tar.gz`,
> GitHub's recorded asset digest `sha256:02f00f4777d43e8e95b7b8d49e1a0d6e502fed4b8e79c1c8b8063857a30caa2e`
> (platform-computed, not author-published) -- decision needed: accept that
> digest for sd, or use the strictly rule-compliant crates.io route, sd
> **1.0.0** `cargo install --locked --version 1.0.0 sd` (crates.io checksum
> `70613c41881ca1e5b69e6bb110f2ac499739c03a151b00e41e16090974b826a8`; needs
> the dependency crates fetched at build time; whole-file default instead of
> 1.1.0's line-by-line). Existing tools to be pinned by recorded version, not
> installed: sed 4.9, perl 5.40.1, python 3.14.4.

## 10. Build order once approved (not started)

1. `bench/subst/` skeleton: sidecar, six `PATTERN`/`TEMPLATE.neutral` pairs,
   `gen_subjects.py`, manifest, `divergences.tsv`, `make check-harness` slice on
   `acc-gate` only (oracle `substitute()` in `oracle_pcre2.py`).
2. Schema v1.9 (section 5) + validator rules + examples.
3. Driver subst modes (pcre2 first as the baseline), then rust, re2, pcrec
   (after the landing).
4. Tools-tier runner (`pcrecbench/toolrun.py`) + `testees/tools/` adapters.
5. Reporter `--grain subst`; a scratch dry run; then the window.
