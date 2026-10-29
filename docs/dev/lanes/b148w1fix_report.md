# b148w1fix report (2026-10-29)

Lane b148w1fix, branch `lane/b148w1fix`, worktree `worktrees/b148w1fix`. Writer, Sonnet. Not merged
(tonight's window runs from master). No store/ write, no timing run; smoke only (`trials 1 iters 1`,
scratch, `synthetic`).

## 1. The verbatim cscan / wild-json-validate on pcrec (I-170)

**Finding.** Both members use `(?(DEFINE)...)` and NO other conditional (source scan in
`tools/check_w1fix.py`, with a control that the scan does see `(?(1)a|b)`). They were tagged
`requires-conditionals`; pcrec cannot declare general `conditionals` (`(?(n)...)` is still refused),
so only the `-onig` twins ran on pcrec.

**Fix (engine-neutral, R-BENCH-4).** One new REQUIRES token, `conditional-define` ("`(?(DEFINE)...)`
as a group of definitions that is never matched"), in `pcrecbench/capability.py` REQUIRES_VOCAB and
`bench/unusual/gen_patterns.py` VOCAB_REQUIRES. `members.py`: cscan and wild-json-validate require it
instead of `conditionals`. `gen_patterns.py` DERIVES the declarations (nothing typed per engine):
every block that declares `conditionals` also gets `conditional-define` (the specific form is a subset
of the general one), plus `DEFINE_ONLY` = the four native pcrec configs (deep arms inherit through
`src`). `bench/capability` is untouched. Regenerated: `patterns.rxt`, `subbench.toml` (generator
`--check` clean).

**Admission matrix, every (member, testee): 500 cells.** Frozen BEFORE (HEAD 43860330) vs AFTER:
files `docs/dev/measurements/2026-10-29-b148w1fix-admission-{before,after}.tsv`, script
`...-matrix.py`.

| class | cells |
|---|---|
| admission flips refused -> ADMIT | 12 = {cscan, wild-json-validate} x {pcrec-auto, pcrec-auto-deep, pcrec-nocaps, pcrec-vm, pcrec-vm-deep, pcrec-vm-in} |
| admission unchanged, refusal token renamed `conditionals` -> `conditional-define` | 12 = the same two members x {re2-default, rust-default, vectorscan-block-som} and their `-assist-v01` arms (the refusal text/`declaration_ref` names the new token; they are refused exactly as before) |
| byte-identical | 476 |

pcre2-interp/jit(+deep, assist) and onig-default(+deep, assist) ADMIT before and after (they declare
both tokens). Note onig still admits cscan/wild-json-validate as before (its answer on the DEFINE
witness is the known false-no-match, unchanged).

**pcrec compiles and answers both verbatim members**, through the real adapter (`run_cell`, 161 short
subjects x 2 members, oracle-judged): pcrec-auto-deep 322/322 matched-as-expected, 0 give-ups;
pcrec-vm 320 matched-as-expected + 2 `gave-up` (cscan/cs-nest-100, wild-json-validate/js-deep-arr:
pcrec's default stack-resident frame limit, the deep arm's reason to exist; pcrec-auto also checked
by hand: same 2). pcre2-jit 322/322 as a control. Compile outcome `compiled` for both forms.

## 2. js-1m first touch (I-170)

**Why driver.c:24 does not cover it.** That comment describes the *configured* `-in` arms
(`--buffer-frames/--buffer-trail`, `alloc_region` memsets). The `deep` arm uses `--buffer-bytes` and
`alloc_untouched` (driver.c:570) BY RULING (unusual_set_v1.md 6.2 / M-9: "NOT pre-touched ... page
faults of first use are inside iteration 1 and stated"). The same ruling leaves libpcre2-jit's 1 GiB
JIT stack and the interp/Onig heaps untouched. So js-1m's one iteration pays the faults of the ~339 MB
the match grows into.

**Fix.** Pre-touching storage stays ruled out (a measurement of its own; it would pin maxrss at the
cap). Instead every `deep` arm runs the driver's own, already-existing `--prime` (one UNTIMED execution
of the timed loop body per subject) in the `throughput` regime only. No C change (all three drivers and
BD16's `timed.c` already implement `--prime`; the adapter passes it). `pcrecbench/adapters.py`:
`deep_prime_argv(handle, regime)` + `STORAGE_PRIME_OPTION`; the three adapters' `measure()` call it and
their deep testee blocks carry runtime option `storage_prime = throughput-per-subject`. Not primed:
`call-stream` (one process, many calls; `--prime` has no meaning there), `--mem-pass`, a harness-primed
`quick --prime` cell (not doubled), short regimes (no cache-warming side effect on microsecond cells),
and every non-deep arm.

**Where it is recorded.** `testee.runtime_options` (existing schema place; confirmed: a scratch record
for pcrec-auto-deep, pcre2-jit-deep, pcre2-interp-deep, onig-default-deep went through
`store.write` validation and carries the option). No schema change was needed, so no stop. It is
NOT in the testee_id (like `limits`' value it rides in runtime_options; the deep ids already carry
`lim-ceil1g`). No pinned deep record exists yet, so nothing stored changes identity.

**Caveats the manager should rule on or read.**
1. This AMENDS 6.2 / M-9 (the design note now has an AMENDED paragraph). It is what the brief asked
   for, but it is a design change to a Frank-ruled paragraph; flag to Frank if desired.
2. Asymmetry: priming persists a caller buffer (pcrec) and a JIT stack (pcre2-jit); pcre2-interp's heap
   and Onig's match stack are malloc'd per call, so their growth is largely still re-paid inside the
   timed call. The note says so. Applying `--prime` uniformly was chosen over per-engine special cases.
3. UNMEASURED: no timing was allowed. Whether js-1m drops from x21.9 toward x5.9 is W1's first read.
   Smoke only: the driver accepts `--prime` with `--buffer-bytes --find-all` on js-1m and js-near-1m
   (4 deep arms, matched-as-expected).

## 3. Checks

New `tools/check_w1fix.py`, section `w1fix` of `make check-unusual` (20 checks, ~27 s, run twice:
20/20). Controls: general-conditional scan; a synthetic `requires-conditionals` pattern refused on
pcrec and admitted on pcre2-jit; pcrec still lacks `conditionals`; matrix delta is EXACTLY the declared
12 + 12; six `deep_prime_argv` negative cases; five real adapters' `measure` argv carry `--prime` at
throughput and not at search; `limits` marker present on exactly the five deep arms. Full
`tools/check_unusual.py` (all sections): 151 passed, 0 failed, 279 s, rc=0 (log `/var/tmp/pcrecbench/b148w1fix/full.log`, `DONE rc=0`).

## 4. Charter-vs-committed checklist

| promise | artifact |
|---|---|
| engine-neutral smallest fix for DEFINE, capability token | `conditional-define`: capability.py, gen_patterns.py, members.py, regenerated patterns.rxt/subbench.toml |
| before/after admission matrix over every (member, testee), others EXACT | the two TSVs + script; check_w1fix asserts live == AFTER and delta = 12 flips + 12 renames, 476 identical |
| wild-json-validate other conditionals? | no, only DEFINE (check_w1fix scan) |
| pcrec compiles + answers both verbatim members vs oracle via real adapter | check_w1fix (f); numbers in section 1 |
| R-BENCH-4 | no pcrec-specific shape in set surfaces: the token is a feature name; only the roster declaration (DEFINE_ONLY) names pcrec, as every capability matrix does |
| js-1m: find why | section 2 (alloc_untouched + 6.2 ruling) |
| fix outside timed region for every applicable engine, no special-casing | `--prime` on all five deep arms at throughput |
| record what was done | `testee.runtime_options storage_prime`; design 6.2 AMENDED; no schema change |
| self-checks with controls in check-unusual | `tools/check_w1fix.py`, section `w1fix` |
| CLAUDE.md updates | bench/unusual, pcrecbench, tools, docs/dev/measurements |
| no store/, no merge, no timing | honoured |
| OWED | (a) `make check-harness` / `make check` were not run (manager's launch); (b) the js-1m timing effect, W1; (c) whether the 6.2 amendment needs Frank's confirmation; (d) throughput-only vs all non-stream regimes is a judgment call, one-line change in `deep_prime_argv` |
