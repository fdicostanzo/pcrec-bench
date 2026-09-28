# lane b108pred report — fix litrun predictions after re-pin

**Task**: the manager's review of lane `b108set`'s
`docs/dev/predictions/litrun-0.1-first.tsv` (written before the
`b108repin` re-pin's eight new pinned testees existed): fix the
`pcrec_*_...`-style testee selectors to the real derived ids, re-aim
P5's L-sweep at the correct pre-check pair with a labelled default-pair
second row, restate the L=31 WATCH cell for this box's toolchain, add
the S7.1 2x2's TIMING half (P6), and add cross-set predictions for
I-113 items 1-3 on bounded/loglines/capability's own named cells.

**Branch**: `lane/b108set` (worktree `worktrees/b108set`), commit
`4dc8b60`. First merged `lane/b108repin` (84b79af..2fd0f82, the re-pin
to a32bc86e/abi 41 + the eight new pinned testees) and `master`
(3bc25bc, 6c0962a — U7's vectorscan build + the x86 gcc-15 memcmp
lowering measurement this lane's own probe builds on) into it; both
merges were clean, no conflicts (disjoint work, confirmed by
`git merge-base` before merging).

## 0. Findings first

1. **The manager's diagnosis was right in spirit but the mechanism is
   subtler than "wrong glob".** `pcrec_*_vm-caps-simdna_nolitrun`
   *does* structurally match the real id
   `pcrec_a32bc86e_vm-caps-simdna_nolitrun` (checked directly against
   `pcrecbench.interpret._glob_match`) — it is not a syntax bug. The
   real defect is a FUTURE hazard: every deny testee this project has
   ever added (`-noreqbyte`, `-noclsfold`, `-noedge`, …) has survived
   every later re-pin unchanged, so a `pcrec_*_..._nolitrun` wildcard
   would also match a LATER pin's own `-nolitrun` sibling the moment a
   report spans two pins, silently pooling two different programs under
   one `ratio_to` — the same class of defect [B87]/I-108 fixed for the
   null-control band's own cross-class query (`_query_pin_pair_ok`).
   Confirmed the fix by finding the established convention directly:
   `capability-0.1-noreqbyte-twin-02902356.tsv` (a same-pin twin
   predictions file, the closest precedent) spells BOTH sides as exact
   ids (`pcrec_02902356_auto-caps-simdna` / `..._noreqbyte`), never a
   wildcard. Every `testee=` selector in the four files this lane wrote
   or edited now does the same, derived via
   `pcrecbench.record.derive_testee_id` fed real `describe()` output
   from `testees/pcrec/adapter.py` (not typed by hand) — the pin's
   `PIN.tsv` (written by `pin.sh` at the b108repin build) resolves to
   the SHORT hash `a32bc86e`, not a `git describe --always` tag string,
   confirmed against the shared build root.
2. **Every named cell in the three new cross-set files was checked to
   actually be VM under `auto` before committing to a `pcrec-auto`/
   `pcrec-auto-nolitrun` pair** — the brief's own "vm vs vm-nolitrun
   where the named cells are VM" turned out to be moot for ALL fifteen
   named cells (four bounded, one loglines, ten capability): every one
   compiles to `RX_ENGINE "vm"` with `RX_VM_LIT_RUNS > 0` under `auto`
   at this pin (direct build against `build/pcrec-a32bc86e/build/pcrec`,
   `--features all`), so `auto`/`auto-nolitrun` already IS the pair
   that isolates S2a — no forced `--engine=vm` testee needed anywhere.
   Three DFA-routed controls for I-113 item 3's NULL claim were found
   the same way (`cls-upto-64`, `iso-ts`, `router-prefix-order`, all
   `RX_ENGINE "dfa"`).
3. **The L=31 WATCH cell's own new archived probe reproduces the
   synthetic-loop finding on the REAL artifact, not just a stand-in.**
   `docs/dev/measurements/2026-09-27-x86-gcc15-memcmp-lowering.txt`
   (merged from master) already showed a hand-written
   `memcmp(p,q,31)==0` function fully inlined by this box's gcc 15.2 at
   -O2. This lane went one step further and built the REAL `lit-l31`
   forced-VM artifact through `testees/pcrec/adapter.py`'s own
   `Adapter._compile_one` (config `pcrec-vm`, exactly the compile path
   the harness itself uses), then checked the resulting `.so` three
   ways (`objdump -T`, `readelf -r`, `objdump -d`) — zero memcmp
   references, same as `lit-l16`'s control. Archived as
   `2026-09-27-litrun-l31-artifact-memcmp.txt` /
   `probe_b108_litrun_l31_memcmp.py`. P5.c is restated accordingly
   (split into `c.matlbf`/`c.fbf`, reusing the L=16/L=40 thresholds
   instead of a hand-picked regression band) rather than merely noting
   the caveat in prose.
4. **`wild-secrets-aws-access-key-id`'s sign-flip question is scored
   `op present`, not a coin-flip direction.** The brief was explicit
   that inventing a direction here would be wrong; the predictions
   format's own `present`/`absent` op vocabulary (`_op_holds`: `value
   is not None`) is exactly the honest instrument — it asserts the
   ratio is MEASURABLE without asserting which way it points. Used on
   all four of that pattern's P6 cells (both routes × both factoring
   columns).
5. **`check_testee_globs` genuinely fails today for all three new
   cross-set files, and that is EXPECTED, not a defect left unfixed.**
   `bounded`/`loglines`/`capability@0.1` already carry OTHER pins'
   measured records in `store/index.tsv`, so the check is
   NON-VACUOUS and correctly reports that `pcrec_a32bc86e_...` matches
   none of them yet (the window hasn't run). Confirmed this is the
   normal, temporary state of a fresh-pin predictions file authored
   before its own window: `capability-0.1-noreqbyte-twin-02902356.tsv`
   would have failed the identical way at ITS OWN authoring time, and
   now passes because 02902356 has SINCE been measured (checked: its
   testee ids ARE in `store/index.tsv` today). `litrun-0.1-first.tsv`
   itself stays vacuous either way (litrun@0.1 has no measured record
   at any pin, old or new).
6. **P2's two `wild-logparse-*` patterns needed a name correction.**
   I-113's own text says `quotedstring-grok`/`syslogbase-expanded`;
   grepping every `bench/*/patterns.rxt`/`subbench.toml` found them
   ONLY as `wild-logparse-quotedstring-grok` /
   `wild-logparse-syslogbase-expanded` in `bench/capability`. Both
   sides of `bench/litrun/NOTES.md`'s own P2 transcription (which
   already existed, unedited by this lane until now) and the new
   predictions file spell the real ids; noted in both places so a
   future reader is not confused by I-113's own elided prefix.
7. **`docs/dev/predictions/litrun-0.1-first.tsv` grew from 24 to 53
   rows**: the wildcard fix touched every existing row (24), P5 grew
   from one pair to two labelled pairs (a/b/c/d re-aimed at the primary
   pair, e/f/g new on the default pair — 41 rows total after this
   split, up from 24), and P6 (the S7.1 timing half, 12 rows) is
   entirely new. 41 + 12 = 53.

## 1. Charter-vs-committed checklist (the brief's five numbered items)

| # | brief item | status | where |
|---|---|---|---|
| 1 | replace `pcrec_*_..._nolitrun`-style selectors with real derived ids, checked against convention + `load_predictions` | DONE — every `testee=` in all four files is an exact id, derived via `pcrecbench.record.derive_testee_id` against real `describe()` output, never typed by hand; 53+5+3+13 rows load with 0 errors | §0.1, the four TSVs |
| 2 | P5 primary pair = `noreqbyte-noreqrun` vs its `-nolitrun` sibling; ADD a labelled default-pair second row (mat faster, fbf/lbf NULL) | DONE — P5.a/b/c/d re-aimed at the primary pair; P5.e (mat, faster)/f (lbf, NULL)/g (fbf, NULL) new on the default pair | `litrun-0.1-first.tsv`, `bench/litrun/NOTES.md` |
| 3 | P5.c restated for x86 gcc15 (objdump the real a32bc86e artifact for lit-l31 + lit-l16 control, archive with source header, cite in the clause) | DONE — `probe_b108_litrun_l31_memcmp.py` / `2026-09-27-litrun-l31-artifact-memcmp.txt`; P5.c split into `c.matlbf`/`c.fbf`, both cite the probe and the merged-in synthetic-loop measurement | §0.3, the archived probe |
| 4 | P4 TIMING 2x2 (median_ns, all 4 corners, both routes) on alt-foo-tails/aws-access-key-id (lit-run faster per factoring column) and the two controls (factoring NULL); aws-access-key-id's sign-flip left open, not invented | DONE — new P6, 12 rows (a-d alt-foo-tails `lt`, e-h aws-key `present`/no direction, i-l controls `between`) | §0.4, `litrun-0.1-first.tsv` P6 |
| 5 | P1-P3 cross-set clauses (pcrec-auto vs -nolitrun, or vm vs vm-nolitrun where VM) for bounded/loglines/capability's named cells, one file per set per [B104]'s precedent | DONE — three new files, every named cell confirmed VM-under-auto by direct build first (§0.2), so no forced-vm testee needed anywhere; one DFA-routed null control per set for P3 | `bounded-0.3-litrun-a32bc86e.tsv`, `loglines-0.1-litrun-a32bc86e.tsv`, `capability-0.1-litrun-a32bc86e.tsv` |

## 2. Validation

- **`interpret.load_predictions`**: all four files, **zero errors**
  (`litrun-0.1-first.tsv` 53/53, `bounded-0.3-litrun-a32bc86e.tsv` 5/5,
  `loglines-0.1-litrun-a32bc86e.tsv` 3/3,
  `capability-0.1-litrun-a32bc86e.tsv` 13/13).
- **The `lo`/`hi`/op-shape check** (the exact defect class
  `syntax-0.1-rust-first.tsv`'s own history documents catching after a
  window started, and this lane's own predecessor already guarded
  against): a small script confirmed every `between` row carries both
  `lo` and `hi`, every `present` row carries neither, and every other
  op carries `hi` only — **zero violations** across all four files.
- **`make check-interpret`** (`gnutimeout 600`, from the worktree
  root): **174 passed, 50 FAILED** — every failure is a
  `re-renders byte-identical` sidecar-freshness failure (section 3,
  the catalogue 3.11→3.12 bump from `b108repin`'s own merge), the
  EXACT set and count the brief named as "expected and NOT yours to
  fix". Confirmed no OTHER failure appeared (none of the 50 FAIL lines
  mentions `litrun` or a predictions-load error); sections 1/2/4/5/6
  are fully green (21/8/139/4/1 = 173, plus `gen.py`'s own "ok" line —
  matches the 174 passed count).
- **`check_testee_globs`**: run directly against `store/index.tsv` for
  all four files — `litrun-0.1-first.tsv` OK (vacuous, litrun@0.1 has
  never been measured); the three cross-set files FAIL today by name
  (`pcrec_a32bc86e_auto-caps-simdna` matches none of the 30-39
  currently-measured testees per set) — expected per §0.5, not fixed
  (nothing to fix: the window hasn't run yet).

## 3. OWED

None from this lane's own brief — every numbered item is DONE and
verified above. Two things the NEXT reader should know, not owed work:

- **`check_testee_globs` will start passing for the three cross-set
  files the moment the `a32bc86e` window measures
  `bounded@0.3`/`loglines@0.1`/`capability@0.1`** — no action needed
  before then; this is the ordinary temporal order every fresh-pin
  predictions file in this directory has had (§0.5).
- **The measurement window itself** (litrun@0.1's first sample, plus
  the `a32bc86e` re-measure of bounded/loglines/capability that scores
  these cross-set files) is explicitly not this lane's — same as
  `b108repin`'s and `b108set`'s own reports both said, the manager
  schedules it.

## 4. Files

- `docs/dev/predictions/litrun-0.1-first.tsv` — revised, 24 → 53 rows.
- `docs/dev/predictions/bounded-0.3-litrun-a32bc86e.tsv`,
  `loglines-0.1-litrun-a32bc86e.tsv`,
  `capability-0.1-litrun-a32bc86e.tsv` — new.
- `docs/dev/predictions/CLAUDE.md` — the `litrun-0.1-first.tsv` entry
  rewritten for the revision, three new file entries added.
- `bench/litrun/NOTES.md` — the Predictions section rewritten: P1-P3's
  cross-set scoring pointers, P4's DEFAULT-pair note, the new P6
  section, P5's PRIMARY/DEFAULT pair split and the P5.c restatement,
  the exact-id rationale, the `check_testee_globs` vacuity note.
- `docs/dev/measurements/probe_b108_litrun_l31_memcmp.py`,
  `2026-09-27-litrun-l31-artifact-memcmp.txt` — new archived probe.
- `docs/dev/measurements/CLAUDE.md` — two new rows for the probe above.
