# b130snap report -- [B130.2] the trend report on per-version snapshots

Branch lane/b130snap (worktree worktrees/b130snap). Charter-vs-committed checklist:

1. SNAPSHOT -- DONE. `tools/trend.py snapshot --pin P | --all-pins` (+ `make trend-snapshot PIN=`),
   format and deterministic gzip in `tools/trend_snapshot.py` (schema `trend-snapshot-1`,
   mtime 0, level 9). Per record: REC (role, machine, timestamp, status, disposition, harness commit,
   era-aware instrument, abi, record path), PAT (pattern sha), CMP (compile outcome, compile ns, R13 stamps,
   program_sha256, emit bytes, engine_sel), CEL (set-grain median/min/max, wrong/gave-up/no-expectation,
   pattern sha, subject-set sha), SUBJ (per-subject sha, median, full per-trial list). Same-window
   controls (nearest pcre2-jit per used pcrec record) and ALL used competitors per set@version are in the
   snapshot (deviation: R12 takes the best of all competitors per cell, so "the fastest per set" is stored
   as the whole competitor set, not one record). Shared control/competitor records are stored inline once and
   `ref:<pin>`-ed afterwards (see the size note below). Overwrite refused
   without `--force` (tested); `--all-pins` is resumable.
2. COMPARE FROM SNAPSHOTS ONLY -- DONE. `make trend` = `tools/trend.py` reads snapshots + links.tsv +
   config.toml (+ catalogue/rules.toml pin order). Test: the synthetic store is deleted before the compare and
   every `open()` is traced (none under store/). All R-rules and row ids unchanged. Compare takes ~80 s (was ~5 min).
3. LINKS -- DONE. `reports/trend/links.tsv`: kinds `set-version` (undirected pair) and `config-rename`;
   columns kind/from/to/source/reason. Seeded by `trend.py links --write` from the old implicit walk: 5
   rows, all `inferred` (altwide 0.2~0.3, bounded 0.1~0.2 and 0.2~0.3, capability 0.1~0.2, email-specimen
   0.1~0.2; reasons carry cell counts) -- the manager/Frank flips them to `confirmed`. An unlisted pair
   reads verdict `unlinked` (no ratio, `why` names the pair, `# unlinked_cells: N` in the deltas header);
   0 unlinked on the real data. No config renames were being inferred, so none seeded.
4. BACKFILL -- DONE. 24 snapshots (v1 report said 25: CLAUDE.md was counted), one per pin with records (60366d747 has none), generated DETACHED at nice 19
   (log /var/tmp/b130snap/backfill.log, `DONE rc=0`). Snapshot-based output vs the committed reports/trend/ (made from
   the store): every TSV body (deltas, summary, compile_deltas, deny_twins, movers_by_stamp, interest, records,
   all 5x history files) and the untracked cells.tsv (24,683 rows) IDENTICAL; the HTML pages and index.md
   differ ONLY in the header sha text. Headers changed by design (`index_sha256` -> `snapshots_sha256`,
   `links_sha256`, `links`, `# unlinked_cells` in deltas). The common-subject rule changed no row (it was already
   per-subject). Not carried: records.tsv rows for `excluded-unknown-pin` (a pcrec pin outside pin_order) have no
   snapshot to live in; none exist in today's store (records.tsv bodies identical).
   `make trend-check` 106 files, 0 drifted; every snapshot passes `verify_snapshot`.
5. SKILL -- DONE. `.claude/skills/pcrec-bench-report-trend/SKILL.md` (window-close procedure; no interpretation
   written, per Frank), listed in `.claude/skills/CLAUDE.md`; trend_interpretation_v0.md now names it.
6. TESTS/DOCS -- DONE. `tools/tests/test_trend.py`: 64 checks, ALL PASS (snapshot round trip/verify, per-subject
   rows, ref storage, deterministic gzip, immutability, store-free open trace with the store deleted, links-only
   incl. unlinked/config-rename/proposals, headers). `make check-trend` green. Docs: reports/trend/CLAUDE.md,
   reports/trend/snapshots/CLAUDE.md, tools/CLAUDE.md row, design note section 8, Makefile targets
   (`trend-snapshot`, `trend-links`). Root CLAUDE.md untouched (no new top-level thing).

OWED: (a) manager flips the 5 `inferred` links to `confirmed` (trigger: review). (b) a future semantic check of
quoted numbers vs cited rows (already owed by trend_interpretation_v0.md section 3). (c) plan.md [B130.2] row state is the
manager's edit. (d) snapshots are 81 MB; if that is too heavy for git, the lever is dropping the per-trial `diag`
and rounding -- not done, would break byte-identity with the store-based output.

## Size revision (manager review, trend-snapshot-2)
81 MB -> **29.9 MB** (24 files), lossless, no rounding. Changes: REC rows keyed by integer `rid` (body rows no longer repeat
the record path); one file-wide `SB` subject table (id + sha stored once, not per cell row); outcome-code table (`OUT`);
trials as `trial:code:elapsed[:diag]` text instead of JSON; ns/call stored as the measured integer `elapsed_ns` over a
per-row `iters` and RECOMPUTED as elapsed/iters (checked equal bit for bit at write time, `f<float>` escape otherwise);
the per-subject median column dropped (derived by `subject_median`); CEL/SUBJ lost their set_ver/config/shas columns.
Digest cache key bumped (DIGEST_VERSION d2; build_digest now keeps elapsed/iters in `rawt`).
Re-proof after the re-run backfill (detached, nice 19, `DONE rc=0`): every snapshot passes `verify_snapshot`;
snapshot-based output vs the store-based output: every TSV body identical, cells.tsv 24,683 rows identical to the
store-based file in the main tree, HTML/md differ only in the sha text; `make trend-check` 106 files, 0 drifted;
test_trend.py ALL PASS (adds the trial codec round trip: exact elapsed/iters, f-path, None, escaped diag; and a check
that SUBJ rows carry no JSON and no path).
Where the bytes are (uncompressed / compressed, all 24 files): SUBJ trial rows 77.8 MB / ~25 MB (4.55 M trial values,
about 5.5 compressed bytes each); CEL 7.3/1.6; CMP 6.4/1.3; SB 0.4/0.2; PAT 1.0/0.15; REC 0.2/0.03. The ~25 MB is the
timing noise itself (the low digits of 4.5 M measured elapsed_ns); going lower losslessly would need per-subject delta
coding against the first trial, gaining perhaps 10-20 % -- not done. 29.9 MB is above the ~25 MB you named for that reason.
links.tsv untouched (5 `inferred` rows, yours to confirm).
