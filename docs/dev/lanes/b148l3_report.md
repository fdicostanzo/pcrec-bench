# Lane b148l3 report -- bench/unusual skeleton (L3 of unusual_set_v1.md section 10)

Branch `lane/b148l3` (worktree `worktrees/b148l3`). Tier: set construction. NO timing, NO downloads
(nothing fetched; the two fetchers are written and refuse), `~/pcrec` read-only (cscan copied from main
614d45eb3 byte-verbatim, `vendor/pcrec/PROVENANCE.md`). Touched: `bench/unusual/` (new), one row in
`bench/CLAUDE.md`, three lines in `.gitignore` (`bench/*/streams/`, `bench/*/calls/`), this report. NOT touched:
`bench/unusual/assists/` (L2), `schema/`, `pcrecbench/` (L1).

## Checklist (charter -> committed artifact)

| charter item | state | where |
|---|---|---|
| sidecar in the shape of other sets | DONE, generated | `subbench.toml` (22 `[[patterns]]`; regimes `search_short` + `throughput`; `call-stream` not declarable until L1) |
| section 2 members: cscan, wild-sexp-balanced, wild-json-validate, callout members, vars members, floor | DONE (22 patterns; vars = text only) | `members.py`, `patterns/*.rx`, `provenance.tsv` |
| section 3.1 cscan + declared Onig syntax-only variant + `(?{x})DEFINE` witness | DONE; variant derived mechanically, equals cscan on all 73+3 cases and every stream call | `cscan-onig`, `cs-define`, `define-witness` |
| the Onig variant for the JSON member (2.1 "needs the 3.1 mechanism") | DONE (added beyond the member table: `wild-json-validate-onig`) | `members.py` |
| section 4.1 F1 segment-stream generator | DONE, deterministic, sha256 manifest | `gen_streams.py`, `unusual_text.py`, `manifest_streams.tsv` |
| section 4.2 F2 sqlite/kernel | SKIPPED BY NAME; fetchers written, UNRUN, empty pin tables | `fetch_sqlite.py`, `fetch_kernel.py`, `skipped_subjects.tsv` |
| section 4.3 F3 pathologicals + depth ladder | DONE | `gen_throughput_subjects.py` |
| section 8 reference scanner + host references | DONE | `unusual_lib.py` (`ref_scan`, `sexp_first`, `json_ok`, `host_first`, `netstr_first`) |
| section 8 oracle + `expectations.tsv` + `expectations_stream.tsv` | DONE (vars rows OWED to L7) | `gen_expectations.py` |
| NOTES.md with predictions incl. E-1 declared before any run | DONE | `NOTES.md` section 4 (D-1..D-4), outlier rule R0-R5 |
| bench/unusual/CLAUDE.md | DONE | |
| `gen_*.py --check` reproduce manifests; set checks | DONE | `check_set.py` (16 checks, 0 failed, 28 s) |

## Members (provenance)

cscan: pcrec scandog, MIT, verbatim. cscan-onig / wild-json-validate-onig: adapted (DEFINE respelled `{0}`).
wild-sexp-balanced: pcre2pattern(3) 10.46, BSD-3, adapted (`(?x)` prefix). wild-json-validate: Stack Overflow answer 3845829
(mario), CC BY-SA 4.0, adapted (PHP quoting undone, `/sx` -> inline `(?sx)`; the manager's research note records the fetch).
co-luhn/isbn/member x {real, -pass, -twin}, co-netstr {native `(?C"netstr,consume")`, -assist, -twin}, va-tenant/route/term/term-bang, floor: authored.
No `co-netstr-pass` (a stub cannot consume; design 3.2: no cross-arm subtraction on netstr).

## Subject sizes and call counts (section 4, M-13)

| set | n | bytes | calls |
|---|---|---|---|
| short (`manifest.tsv`) | 161 | 12-<=1024 each | 1 per cell |
| throughput F3 | 23 | comment-5m 5,000,011; unterminated-5m 5,000,006; idents-1m 1,000,007; splice-1m 1,000,009; literal-100k 100,014; nest-{brace,paren}-{128..100k} 267-200,011; nest-digraph-10k 40,011; define-witness 12 | ONE call at offset 0 |
| throughput other families | 7 | sx-1m 1,002,042; js-1m / js-near-1m 1,000,648; co-luhn-1m 1,000,017; co-isbn-1m 1,000,051; co-member-1m 1,000,066; co-netstr-1m 1,000,025 | find-all counts (expectations): sx 332, luhn 4,632 (twin 11,308), isbn 4,223, member 4,889, netstr 14,527 |
| F1 `seg-s` | 1 | 248,613 B, 225,602 segment bytes | 256 calls (5 local refusals) |
| F1 `seg-l` | 1 | 3,932,601 B, 3,582,729 segment bytes | 4,096 calls (47 local refusals) |

Deviation: design 4.1 says ~180 KB / ~3 MB; its own stated mix (log-uniform 20 B-5 KB + filler) gives mean ~960 B per call, so the
measured sizes are kept and stated (NOTES.md section 2).

## Oracle counts

`expectations.tsv`: 2,999 rows = 2,898 search_short + 101 throughput; methods libpcre2-differential 2,835, host-reference 162 (co-netstr
native spelling), reference-scanner 2 (the two declared oracle declines). 1,510 triples answered by BOTH methods and agreed (the
derivation aborts on any disagreement); 1,325 have no independent second method (plain twins, pass arms, floor). `expectations_stream.tsv`: 4 rows;
seg-s 251 matched / 5 nomatch, seg-l 4,049 / 47, `cscan` and `cscan-onig` token hashes IDENTICAL, oracle == reference scanner on all 4,352 calls,
no-match count == generated local refusals (generator validity control). pass == twin on every row (asserted). Reference scanner: 73 pcrec
start-0 cases + 3 start-offset cases == hand rule == libpcre2 == Onig-variant text.

FINDING (carry to the upstream pipeline, not filed): libpcre2 10.46 interpreter on cscan's per-brace-level recursion is super-quadratic:
depth 8,000 1.6 s, 16,000 7 s, 32,768 43-74 s, ~50 min extrapolated at 100,000. The two `nest-brace-100k` cells (cscan, cscan-onig) are therefore
ORACLE-DECLINED (reference scanner alone, method `reference-scanner`, listed in `gen_expectations.py` `ORACLE_DECLINED`). Full derivation ~6 min.

## Generic gates (run on this set only, through tools/selfcheck.py with `subbench_dirs` narrowed; scratch runner not committed)

PASS: check_manifests (all four generators + control), check_id_preflight, check_floor_pattern (quick cell, validated record, pcre2 AND pcrec
answer the floor by the oracle), check_rxt_source_load, check_capability_roster_coverage. FAIL, each needing L8's skip table, none hacked around:
1. `check_rxt_export`: "pattern 'cscan' contains a newline/CR byte" -- the `.rxt` `pattern` line cannot carry cscan (needs `pattern-esc`).
2. `check_capability_policy_noop_elsewhere`: asserts non-capability sets declare zero `requires-*` tags; this set needs them (5.5, per-pattern gating).
3. `check_vars_surface`: asserts no bench pattern contains `${`; the four `va-*` members do by design.
(`check_pattern_text_cap` also failed in my runner only because narrowing hid bench/altwide, its witness.) `gen_expectations.py --check` (the generic
check_expectations call, timeout 1800 s) is OWED a timed run, below.

## Dependencies and decisions the next lanes need

- L1: regime `call-stream`; `REQUIRES_VOCAB` += `vars`, `unusual-<member>` (vars tags are `needs-*` until then; rename); `twin_of` tag; the
  stream manifest columns (`manifest_streams.tsv`: id len sha256 description periodic calls segment_bytes calls_sha256 local_refusals) and
  `calls/<id>.tsv` (HEADER row + `call_id offset length segment_bytes binding_id`) are L3's proposed shapes for L4 to read or amend.
- Capability: `patterns.rxt` carries ONLY the `ext bench` matrix (10 library ids, blocks copied from bench/capability, `--check` fails on drift),
  fail-closed otherwise; `callouts` is declared for libpcre2 only (pcrec/Onig callouts are L5's). The pattern source is the sidecar, not `rxt_source`.
- `applies.tsv`: which large subject belongs to which pattern; `subjects_for()` does not know it (L4/L8).
- `values/users.tsv` (co-member's runtime set) is L3's because the oracle needs it; L5 passes it as `user`.
- Slip to disclose: I ran `pgrep -f` once (forbidden form) to find my own background job; it matched my own tool shell, killing it, and
  nothing else (I then killed the job by explicit PID). No foreign process was touched.

## The two download targets (NOT fetched; offline determination)

- sqlite3.c: the amalgamation is `https://www.sqlite.org/<year>/sqlite-amalgamation-<NNNNNNN>.zip` (<NNNNNNN> = 3, two-digit minor,
  two-digit patch, "00"; e.g. 3.46.1 = 3460100). I CANNOT determine the latest release offline (the box's python links 3.46.1 -- not evidence of
  latest; the last I can name from memory, unverified, is 3.51.0 = `https://www.sqlite.org/2025/sqlite-amalgamation-3510000.zip`). Show Frank the
  download page's current URL + the published hash; `fetch_sqlite.py` needs SQLITE_VERSION, ARCHIVE_URL, ARCHIVE_SHA256, SQLITE3C_SHA256.
- kernel files (latest stable tag undetermined offline; the box runs Ubuntu 7.0.0-38): `kernel/sched/core.c`, `mm/memory.c`, `fs/namei.c`,
  `net/core/dev.c`, `lib/vsprintf.c`; URL shape `https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/plain/<path>?h=<tag>`;
  `fetch_kernel.py` takes one approved (url, sha256) row per file plus KERNEL_TAG.

## OWED

- F2 subjects, the function-body locator for them (needs the files), and `sqlite-bodies`/`kernel-bodies` expectations: owner L3 continuation,
  trigger Frank's approval of each URL + sha256.
- vars members' expectations + value streams: L7. The `gen_expectations.py --check` full re-derivation timing (~6 min, > 4 min so not run
  in-lane as a foreground step): command `python3 -I bench/unusual/gen_expectations.py --check` from the worktree root, log
  `/var/tmp/pcrecbench/b148l3/check_full.log`, completion line `DONE rc=0`.
