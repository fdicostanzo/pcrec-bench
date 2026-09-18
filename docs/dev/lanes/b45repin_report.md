# lane b45repin report — the [B42]-tail RE-PIN to cf0962e3 (abi 26)

**Task**: inbox I-73's checkpoint pin. Re-pin the sixteen pinned pcrec
testee configs from `a770139e` (abi 25) to `cf0962e3` (abi 26, the
dial+K59 checkpoint pin), re-archive and diff all four registry surfaces,
append the pin to `catalogue/rules.toml`'s `[[pin_order]]`, decompose the
size-book delta to zero residue, verify the shim floor and abi-sabotage
arms, check for cap-adjacent stderr rescue notes, update docs, and run
`make check` once, detached, on the merged result.

**Branch**: `lane/b45repin`, `worktrees/b45repin`, three commits so far
(`c719e86` registries, `4037204` size books, `613a21a` docs); this report
is the fourth.

## Charter-vs-committed checklist

1. **Build the pin.** DONE. `sh testees/pcrec/pin.sh cf0962e3` under
   `gnutimeout 900`, succeeded first try:
   `build/pcrec-cf0962e3/build/pcrec`. Confirmed abi 26 and
   `#define RX_TUNE "balanced"` on a plain `abc` witness.

2. **Re-archive and diff all four registry surfaces.** DONE, commit
   `c719e86`.
   - `list_axes.tsv`: **BYTE-IDENTICAL** (78 rows / 27 axes) below the
     re-stamped header.
   - `list_definitions.tsv`: **BYTE-IDENTICAL** (50 rows) — the ninth pin
     running.
   - `list_limits.tsv`: **BYTE-IDENTICAL** (57 rows) — the dial/K59 train
     added no numeric limit.
   - `list_schema.tsv`: **ONE ROW ADDED**, 70 → 71 data rows (`# schema-
     rows: 66` → `67`): `config	tune	token	false	none	at-most-one		format	pcrec	1`
     — a config-scoped `.rxt` directive at wave 1. This is a registry
     delta beyond the +27-byte-stamp/abi-digit movers I-73's item 3
     predicted, but it is EXPLAINED, not silently absorbed: verified
     directly against pcrec's own read-only `docs/spec/rxt_format.md`
     ("`tune <position>` — config-scoped: the SPEED-VS-SIZE DIAL... THE
     FILE WINS OVER AN EXPLICIT CLI `--tune=`") and `--list-source`
     column 20's own description ("the `tune` position AS WRITTEN"). It
     is [OPT-DIAL]'s own `.rxt` grammar addition landing in the same
     train as the corpus-wide stamp — not a finding that needs an ask,
     just one that needed reporting rather than folding into "byte-
     identical" by omission.

3. **Append the pin to `catalogue/rules.toml`'s `[[pin_order]]`.** DONE,
   commit `c719e86`. `catalogue_version` 1.3 → **1.4** (MINOR: a
   `[[pin_order]]` append, per the catalogue's own versioning rule — no
   predicate, threshold or rule inputs moved). `pins` gains `cf0962e3`
   after `a770139e`, in the same commit as the re-pin.

4. **Adjust the size books by the +27 B `RX_TUNE` stamp constant,
   decomposed and verified, not assumed.** DONE, commit `4037204`. Built
   four witnesses at BOTH pins (a matching output basename each) spanning
   every artifact kind `tools/selfcheck.py`'s tables track:

   | witness | kind | Δ `.c` | Δ `.h` |
   |---|---|---|---|
   | `foo\|bar`, `--engine=vm` | forced-VM, non-hybrid, no DFA scan | +27 | +0 |
   | `@` (the `floor` witness pattern) | plain DFA | +27 | +0 |
   | `a(b\|c)+d` | VM HYBRID | +27 | +0 |
   | `[a-z]{0,64}` (pinned) | DFA, TWO scan-edge machines | +27 | +0 |

   A byte diff of each pair shows only two hunks: the inserted
   `#define RX_TUNE "balanced"` line and the `.abi` digit (25→26, same
   character count, 0 net). **Zero residue on all four, including the
   scan-edge-bearing one with two machines** — unlike the previous
   re-pin's `B42_PORTFIX_SEMI_PER_MACHINE` (which scaled per scan-edge
   machine), this stamp is a single file-scope `#define`, so it is
   **ONE flat constant, `B45_RX_TUNE_STAMP_LINE = 27`**, added exactly
   once per artifact regardless of engine, route or scan-edge-machine
   count. Corroborates pcrec's own corpus-wide sweep
   (`~/pcrec/docs/dev/dialtrain_byteid.md`, read-only: 1,500 of 3,938
   pattern lines moved, every one by exactly +27 bytes, zero exceptions,
   zero newly-fixed/broken patterns). Applied at all 30 existing
   `B42_STARTPOS_GUARD_LINES` usage sites in `tools/selfcheck.py` (every
   site already carries a flat per-artifact addition reaching the same
   population this new stamp reaches) — none of the 40 `emit_bytes`/
   `emit_code_bytes`/`warned_emit_bytes` assertion sites lacked
   `B42_STARTPOS_GUARD_LINES`, so no site was missed and none needed a
   different treatment.

5. **Shim floor expectation.** DONE, verified not assumed:
   `struct rx_info` diffed directly between the two pins' emitted `.h`
   files (the `abc` witness) — byte-identical, zero hunks. `shim.c`'s
   `PB_SHIM_MIN_ABI` is unchanged source (161... no file edit needed —
   confirmed still `16`). The abi-sabotage arms in
   `check_abi_floor_refusal` need no change and are expected to pass
   unedited (verified in the `make check-harness` run below).

6. **Cap-adjacent stderr rescue notes.** FOUND, as the brief anticipated.
   K59's own filed witness, `[^\p{C}\p{M}\p{P}]` under
   `-e utf8 --features unicode-props`, is a real behavior change:

   - **At a770139e**: `pcrec: pattern too large: 1027174 bytes of
     emitted C source (limit 1000000, ~170 KB .o)...` — exit 1,
     `did-not-compile`.
   - **At cf0962e3**: exit 0, compiles at 453,528 B (12,411 code), with
     TWO new non-fatal `pcrec: note:` lines announcing the premul
     drop-ladder rung ("dropped the optional anchored match-here
     machine"; "dropped the premultiplied DFA transition table"),
     beside the pre-existing `pcrec: warning: large artifact:...` line.

   This witness is not in any bench sub-bench's corpus (no bench pattern
   uses `\p{...}` Unicode properties), so **no committed record is
   affected** and no bench pattern is expected to reach this rung today.
   Verified the harness would handle it gracefully if one ever did:
   `adapter.py`'s `parse_warn_line` scans stderr line by line for ONE
   specific regex (the `warning: large artifact:` line) and silently
   ignores any other line, `note:` lines included; `_compile_one` only
   treats a compile as `did-not-compile` on `proc.returncode != 0` — the
   rescued compile above exits 0, so it would proceed through phase 2
   exactly like an ordinary compile. **The rescue notes are advisory,
   never a failure, confirmed by reading the code path rather than by
   assumption**; they are not currently captured as structured record
   fields (only the one warning line is), which is consistent with
   every other unrecognized pcrec stderr line today, not a new gap this
   re-pin introduced.

7. **Update `testees/pcrec/CLAUDE.md`'s pin paragraph and other
   CLAUDE.mds whose facts moved.** DONE, commit `613a21a`.
   `testees/pcrec/CLAUDE.md` gains a dated section following the
   established per-re-pin narrative shape (findings 2-6 above, in
   prose). Root `CLAUDE.md`'s `testees/` bullet had a literal stale pin
   fact (`**a770139e, abi 25**`) that would mislead a grepping reader;
   corrected minimally to `**cf0962e3, abi 26**` with the a770139e
   history preserved beneath it, exactly as the previous re-pin
   preserved cd371441's — the surrounding STATUS narrative (and
   `docs/dev/plan.md`, per the brief) is left for the manager.

8. **Full `make check` on the merged result, run ONCE, detached.**
   **LAUNCHED, OWED.** Per BOILERPLATE's DO-THEN-FINISH rule (a run
   longer than ~4 minutes is the lane's last act; report first, launch
   after), this report is committed before the run starts. Launch
   command:

       cd /home/duxevents/pcrec-bench/worktrees/b45repin
       setsid gnutimeout 2400 make check \
         > build/b45repin_check.log 2>&1 \
         ; echo "DONE rc=$?" >> build/b45repin_check.log &
       disown

   **Marker/log**: `worktrees/b45repin/build/b45repin_check.log`
   (gitignored, per `build/`'s own rule). The ONLY evidence of
   completion is the line `DONE rc=<N>` appended to that file — check it
   with `tail -5 worktrees/b45repin/build/b45repin_check.log`, never by
   inferring from `ps`. Gate of record to beat (from the brief):
   check-schema 5/73/0 · check-harness 420/420 · check-report rc=0 ·
   check-interpret 133/133. This lane's own expectation, given items 1-6
   above: check-harness should read 420/420 UNCHANGED (no stamp, no
   axis, no check function moved — only a size-book constant, which the
   checks read via `B45_RX_TUNE_STAMP_LINE` rather than a hardcoded
   number); check-interpret should read 133/133 UNCHANGED (catalogue
   1.4 is a `[[pin_order]]` append only, no rule/predicate/threshold
   moved, so no golden fact should need re-deriving); check-report and
   check-schema are untouched by this lane's edits and are not expected
   to move.

## Not done / not applicable

- No committed store record needed re-deriving (this lane touches no
  `store/` record; the re-pin itself never runs a measurement window).
- No bench sub-bench pattern reaches K59's premul drop-ladder rung
  (item 6): nothing to re-measure there.
- `docs/dev/plan.md`'s `[B42]` tail is explicitly the manager's job per
  the brief; left untouched.

## For the manager, on review

- Please `tail -30 worktrees/b45repin/build/b45repin_check.log` (or
  wait for the `DONE rc=` line) before merging, and fold the actual
  tallies into your own delivery note — this report states the
  *expectation*, not the *result*, for item 8.
- The `list_schema.tsv` one-row delta (item 2) and the K59 rescue
  finding (item 6) are both worth a line in whatever you send back
  through the inbox ack — neither blocks the merge, but both are new
  facts pcrec's I-73 didn't fully anticipate (the schema delta) or was
  the whole point of the pin (the K59 rescue actually firing, witnessed
  outside the corpus).
