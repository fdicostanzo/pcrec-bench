# bench/unusual -- notes (unusual@0.1, lane b148l3 = L3)

Design: `docs/design/unusual_set_v1.md` v0.2 (section numbers below are its).
STATUS 2026-10-27: the SKELETON is built -- patterns, subjects, oracle,
expectations. Nothing here has been timed; no engine other than the installed
libpcre2 10.46 (as the ORACLE) has been run; the declarations in sections 4 and
5 were written before any engine measured anything, and a later edit to them
is a dated amendment, never a rewrite.

## 1. The members (22 patterns)

| id | arm / role | route | provenance |
|---|---|---|---|
| `cscan` | recursion | libpcre2 + reference scanner | pcrec `tests/recursion/cscan.rxt` @614d45eb3, MIT, verbatim (vendor/pcrec/PROVENANCE.md) |
| `cscan-onig` | the declared syntax-only variant (3.1) | libpcre2, must equal `cscan` | adapted: `(?(DEFINE)...)` respelled `(?<n>...){0}` |
| `wild-sexp-balanced` | recursion, WILD | libpcre2 + stack scan | pcre2pattern(3) 10.46 "RECURSIVE PATTERNS", BSD-3, `(?x)` prefixed |
| `wild-json-validate` | recursion, WILD | libpcre2 + python json | Stack Overflow answer 3845829 (mario), CC BY-SA 4.0, adapted (PHP quoting undone, `/sx` -> inline `(?sx)`); docs/dev/research/2026-10-27-b148-json-validator-source.md |
| `wild-json-validate-onig` | the same variant mechanism | libpcre2, must equal the original | adapted |
| `co-luhn` `co-isbn` `co-member` | callouts, REAL arm (site + real callee) | libpcre2 + Python callee, host reference | authored |
| `co-luhn-pass` `co-isbn-pass` `co-member-pass` | PASS arm (site + stub callee) | stub callee; MUST equal the twin | authored |
| `co-luhn-twin` `co-isbn-twin` `co-member-twin` | TWIN arm (site removed, common subset) | libpcre2 | authored |
| `co-netstr` | pcrec's native `(?C"netstr,consume")` spelling | host reference (not libpcre2 syntax); must equal `-assist` | authored |
| `co-netstr-assist` | the check-at-end spelling for libpcre2 / Onig `(?{4})` (P3) | libpcre2 + the check-at-end callee | authored |
| `co-netstr-twin` | `(\d{1,9}):` -- a DIFFERENT language, a scan-cost floor only | libpcre2 | authored |
| `va-tenant` `va-route` `va-term` `va-term-bang` | vars | NO short/throughput rows: per-call expectations over the five declared value streams (`expectations_stream.tsv`; libpcre2 over the resolved + escaped pattern, cross-checked against Python `re`; section 8) | authored |
| `floor` | `\(\?\{` (role = floor) | libpcre2 | authored |

There is no `co-netstr-pass`: a stub callee cannot consume, so a pass arm is not
the same language as its twin (design 3.2: no cross-arm subtraction on netstr).
Pattern texts are NEVER typed twice: `members.py` decodes cscan from the vendored
file (and fails if it differs from `gen_cscan.py`'s own string), derives both Onig
variants mechanically, and `gen_patterns.py --check` re-derives every file below it.

## 2. Subjects

- 161 SHORT subjects (`manifest.tsv`, regime `search_short`, <= 1024 B,
  `short_search_max_bytes = 1024`): the 73 start-0 cscan cases of pcrec's own table,
  five brace-nesting witnesses (19/20/21/30/100: the Oniguruma nest-level-20 probe),
  `cs-define`, and typed cases for every other family, each with the
  FIRST-CANDIDATE-FAILS control. Every non-vars pattern runs every short subject
  (a JSON document is the null control for cscan).
- 30 THROUGHPUT subjects (`manifest_throughput.tsv`): the F3 pathologicals (comment-5m,
  literal-100k, nest-brace / nest-paren x {128, 512, 1k=1024, 2k=2048, 8k=8192, 10k=10000,
  32k=32768, 100k=100000}, nest-digraph-10k, idents-1m, splice-1m, define-witness,
  unterminated-5m) and one ~1 MB text per other family (sx-1m, js-1m, js-near-1m,
  co-luhn-1m, co-isbn-1m, co-member-1m, co-netstr-1m). `applies.tsv` says which
  patterns each belongs to (the F3 set is the cscan family's; `nest-paren-*` is ALSO
  `wild-sexp-balanced`'s ladder: cscan reads parentheses as plain bytes, so on it
  cscan is the no-recursion control at the same size; the floor runs everything).
  `periodic` reads `no` for all by the whole-subject definition; the run-structured
  bodies (period 10 / 4 / 3 / 1) are stated in each description.
- 2 STREAMS (`manifest_streams.tsv`, regime call-stream, L1/L4 consume): `seg-s` 256
  calls / 248,613 B / 225,602 segment bytes / 5 local refusals; `seg-l` 4,096 calls /
  3,932,601 B / 3,582,729 segment bytes / 47 local refusals. Design 4.1's "approx
  180 KB / 3 MB" is smaller than its own stated 20 B - 5 KB log-uniform mix allows
  (mean segment ~880 B + ~80 B filler); the mix was kept, the sizes are the measured
  ones. Call lists in `calls/<id>.tsv` (header + `call_id offset length segment_bytes
  binding_id`, `-` for no binding); the throughput denominator is the sum of
  `segment_bytes`.
- F2 (sqlite3.c, kernel bodies) is SKIPPED BY NAME (`skipped_subjects.tsv`); `fetch_sqlite.py`
  / `fetch_kernel.py` are written, unrun, and refuse by name until Frank approves each
  exact URL + sha256.

## 3. Expectations (section 8)

`expectations.tsv` (9 columns, the existing format; throughput rows carry the find-all
count) and `expectations_stream.tsv` (`subject pattern calls matched nomatch refused
results_sha256 method`; a call's token is `n` or `m:<s>,<e>;<g1s>,<g1e>`, absolute
offsets, group 0 and group 1 only; `results_sha256` = sha256 of the tokens each followed
by `\n`). `gen_expectations.py` header states every method. In short: libpcre2 10.46
interpreter at library defaults is primary (callout members with a Python callee that
returns the +1 FAIL / 0 CONTINUE of the design's return-code table); the second method per
family (reference scanner, stack scan, python json, host Python of each intention)
must AGREE on every triple both answer or the derivation aborts.
ORACLE DECLINES: `cscan` and `cscan-onig` on `nest-brace-100k` -- libpcre2's interpreter cost
for cscan's per-level recursion is super-quadratic (measured here: depth 8000 1.6 s, 16000
7 s, 32768 74 s; ~50 min extrapolated at 100000), so those two cells are answered by the
reference scanner alone (method `reference-scanner`). The oracle itself is shown to agree
with the scanner at every rung up to 32768. This is a FINDING about libpcre2 10.46 (to be
carried to the upstream pipeline by the manager, not filed here): a nesting depth that the
matcher "supports" (heap frames, no limit hit) costs super-quadratic time.

## 4. DECLARATIONS BEFORE ANY ENGINE RUN (2026-10-27)

**D-1 (E-1, Oniguruma nest-level 20 is SILENT).** `onig_get_subexp_call_max_nest_level()`
defaults to 20 and is a MATCH-TIME cap that does not error. Probed (r9eng, 6.9.10,
Perl_NG/ASCII): `(?<p>\((?:[^()]|(?&p))*\))` on `(`^d`)`^d matches at 0 for d <= 20, at
offset 1 for d = 21, at 80 for d = 100, at 980 for d = 1000. DECLARED here, before any run:
`onig-default` (a) answers `cs-nest-21`, `cs-nest-30`, `cs-nest-100` and every
`nest-brace-<d>` rung >= 128 as a false no-match or a wrong group 1 -- NEVER as a
give-up -- because cscan recurses through `(?&items)` once per brace level plus `(?&sp)`
inside it; the exact threshold for cscan is 17-20 levels (the two extra call levels), so
`cs-nest-19` is declared UNCERTAIN and `cs-nest-20` wrong; (b) answers
`wild-sexp-balanced` on `nest-paren-<d>` (depth d+1 with the outer `(?{` paren) with the
INNER balanced group once d + 1 > 20; (c) is CORRECT on cscan over `nest-paren-<d>` at every
rung (parentheses are plain bytes to cscan -- no recursion). These rows are wrong answers,
excluded from rankings by the harness, and are the reason the `deep` arm raises the level
(6.2, `onig_set_subexp_call_max_nest_level(1000000)`). Whether it is an upstream bug is the
manager's (Q-D); this note does not decide it.

**D-2 (depth-of-failure, the `default` arm; 4.3's table made specific).**
`pcre2-interp`: answers every rung (heap limit 20,000,000 KiB) -- slowly at the top (the
oracle took 74 s at 32768); `pcre2-jit`: the 32 KiB JIT stack gives up -46 above some rung,
predicted first at 512 or 1k (no rung below 128 predicted to fail); `pcrec`: stack-resident
frames, `PCREC_ERR_FRAMES` predicted from the 512 rung up on cscan (limits.md 4: ~342 levels
for `^(a(?1)?b)$`, more frames per level here), every rung answered under the 1 GiB `_in`
arm up to a limit this note does not predict; `onig-default`: see D-1. `idents-1m`,
`splice-1m`, `comment-5m`, `literal-100k`, `unterminated-5m`: answered by every engine
(pcre2-jit may give up -47 on the two long ones; its match_limit applies to JIT).
**D-3.** `pass == twin` on every callout member (a `check-harness` gate in L8); `real - pass`
is read only where `callout_fires` are equal (3.2 item 5); co-netstr takes no cross-arm
subtraction (its `twin` is a different language).
**D-4.** The verdict table of 3.0 is a PREDICTION; section 5 (assist authoring and the
token counter) decides it, never this note. The vars readout ranks by miss-compile cost
(3.3).

## 5. Outlier rule (R0-R5, stated before any run)

R0 a wrong answer is excluded, never ranked (the D-1 rows included). R1 a (pattern, subject,
regime) cell is an outlier when an engine's median exceeds 3x the best non-excluded engine's.
R2 a callout (member, subject) is flagged when pcre2-jit's callee share exceeds 20 % or any
engine's exceeds 40 % (3.2 item 4). R3 a give-up names its limit; the `default` arm is read as
the depth-of-failure TABLE, not MB/s. R4 NATIVE and ASSISTED times are never merged into one
column without the verdict label; a vars stream ranks by miss-compile cost. R5 a stream is read
per call (calls/s) and per segment MB/s, never per subject byte.

## 6. Dependencies on the other lanes (what this set needs and does not have)

L1: regime `call-stream` in `subbench.py` / the schema; `REQUIRES_VOCAB` growing `vars` and
`unusual-<member>` (LANDED by L1; the vars members carry `requires-vars` + `requires-unusual-<member>`); `twin_of` (LANDED; the callout arms carry `twin_of-<root>`); the reader skip tables. L4: the `--mode calls` protocol over `calls/*.tsv`, the
O(segment) pre-flight, `CELL_CAP_unusual`. L5: `callees.c`/`callees.o`, the wrappers,
`pass-nofn`, pcrec's and Onig's callout declarations in the `ext bench` block (only libpcre2
declares `callouts` today). L7 (LANDED): the vars members' value streams (`gen_vars.py`, five streams, `values/`) and
their per-call expectations (there are NO vars rows in `expectations.tsv`). L8: `UNUSUAL_GATE_SKIPS` (the generic
floor / manifest / expectations gates do not know `manifest_streams.tsv`, `applies.tsv` or a
set whose expectation file is not the full cross product) and `make check-unusual`.

## 7. Checks

`python3 -I bench/unusual/check_set.py` (fast) and `--full` (re-derives every expectation:
minutes). `gen_*.py --check` reproduce the manifests; `gen_patterns.py --check` the sidecar.

## 8. The caller-variables streams (L7, lane b148l7)

THE CALL. A vars call is one LINE of the stream's subject (bytes `[offset, offset + length)`) plus a
BINDING; the engine matches the member's resolved pattern against that line ALONE (a line is its own
subject: `^` is its start, result offsets are LINE-RELATIVE), first match. Token: `n` | `m:<s>,<e>` | `r`
(REFUSED by the variables rule, vars.md 5: nothing was attempted). `segment_bytes` = `length` = the line, so
the throughput denominator is the sum of the lines. The protocol carries the bindings table as a FOURTH
column of the `--list` file (`id subject calls bindings`); the table is `binding_id name value`, value =
lowercase hex, `UNSET`, or `EMPTY` (a zero-length hex field is not a TSV cell a reader can rely on; this
amends the note's `value_hex|UNSET`).

| stream | members | calls | bindings | distinct resolved (= misses) | refused | reuse |
|---|---|---|---|---|---|---|
| `tenant-d4` | va-tenant | 16,384 | 4 | 4 | 0 | round-robin |
| `tenant-d64` | va-tenant | 16,384 | 64 | 64 | 0 | round-robin |
| `tenant-d4096` | va-tenant | 16,384 | 4,096 | 4,096 | 0 | round-robin |
| `route-zipf` | va-route | 4,096 | 108 | 40 | 983 | zipf-s1.1 |
| `term-zipf` | va-term, va-term-bang | 4,096 | 49 | 47 | 201 | zipf-s1.1 |

The stream length is FIXED at 16,384 across the ladder (P13), so the miss count (a memoizing engine's
compiles per replay) is the only thing that moves: 4 / 64 / 4,096, exact because the ladder is
round-robin. `route-zipf`'s 108 bindings resolve to 40 patterns (prefix UNSET / EMPTY / `api` are one
pattern: the memo key is the resolved pattern, not the binding); 983 of its calls are refused (an UNSET
`res`). `term-zipf` carries metacharacters, a NUL, a high byte, EMPTY and UNSET (refused by `:?`); its
lines put a word byte beside a non-word-ended term so `\b` can hold, and the opposite beside a
word-ended one. Every stream is a pure function of a seed (`gen_vars.py`), pinned by
`manifest_streams.tsv` and `values/streams.tsv` (stream, member, calls, bindings, distinct values, distinct
resolved, refused, reuse, bindings sha256).

EXPECTATIONS. Per call: `gen_vars.resolve` (vars.md 2/5 in Python: the five operators, `${!n}`, a default
word LITERAL and escaped, a backslash in a word, UNSET vs EMPTY, bare `${n}` refusing on UNSET and `${n:?}`
on UNSET/EMPTY, every byte of a value escaped so it matches as itself) builds the pattern, libpcre2 10.46
answers it; Python `re` over `re.escape`d values answers it independently and every call must AGREE
(abort otherwise). The nested chain `${a:-${b}}` is DROPPED from v0.1 (the rule for `b` UNSET is unspecified
in vars.md; Q-C is open with pcrec): `gen_vars.parse` refuses it. Regenerate in seconds with
`gen_expectations.py --streams-only` (the full derivation is minutes). The public sample for the blinded
assist authors (80 cases, 20 per member, disjoint from these streams) is
`assists/problems/vars-samples.tsv`, its problem statement `assists/problems/vars.md`.

D-5 (declared before any run). pcrec runs all five streams NATIVELY and answers every call as the oracle
does, on `pcrec-auto`, `-nocaps`, `-vm`, `-vm-in` and the `deep` arms. Predictions for the window: the
tenant ladder is FLAT across d (one compile, a per-call variable resolution whose cost does not depend on
how many distinct values the stream holds); every assisted engine's time grows with d (a miss compile per
distinct value) and pcrec's break-even call count against it falls as d rises. A refused call costs pcrec
the resolution and nothing else.
