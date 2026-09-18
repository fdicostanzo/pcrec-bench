# lane b49docs — the 2026-09-18 capability-window ledger's §7 items 1-3

Branch `lane/b49docs`, worktree `worktrees/b49docs`, commit `dcf66ef`.
Read-only scope: `docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md`
§7 (candidate asks 1-3), and the cited §1.3 / §5.4 / §6 item 5 sections in
full before writing anything.

## Charter vs committed

| # | charter item | committed |
|---|---|---|
| 1 | `testees/pcrec/CLAUDE.md`: document mojibake-curly-quote's ×2.00 forced-VM throughput cost as the I-72 fix's own known, accepted price, adjacent to the I-72 fix discussion | DONE — commit `dcf66ef`. **Finding first**: no I-72 discussion existed anywhere in `testees/pcrec/CLAUDE.md` before this lane (`grep -n "I-72"` was empty); the fix itself lives only in `adapter.py`'s phase-1 comment (`_compile_one`, ~line 2960) and the inbox ack (`docs/dev/inbox_from_pcrec.md` I-72). Added a new "The I-72 fix: raw-bytes argv, and its own accepted cost" section (between "The compile-cost definition" and "The MATCH regime uses a SECOND artifact") that states the fix itself AND, in the same section, the ×2.00 cost cited from ledger §1.3 line-for-line (both forced-VM configs, the auto/pcre2 control reading unchanged, the mechanism reading) |
| 2 | `testees/tre/CLAUDE.md`: add the measured correctness-gap finding (high-byte-run 0%/48% + the other two patterns, §5.4/§6 item 5), with citation and the next-sample re-check caveat | DONE — commit `dcf66ef`. New "Correctness: the widest gap of any new engine, MEASURED on bench/capability@0.1" section at file end, after the existing `automaton_class` section: the four-row pass-rate table from §5.4, the `mojibake-curly-quote` cross-reference to item 1's new pcrec section, the ledger's own "systematic gap" reading, and the §8 item 2 re-check caveat stated explicitly (possible one-off box artifact, unconfirmed as settled behavior) |
| 3 | `pcrecbench/reduce.py`: check whether onig's `-17:retry` give-up code is named in the `giveup_code` naming table; add it if missing and a table exists, else make NO code change and report the evidence | NO-OP, reported here (no code change). **Evidence**: `reduce.py`'s `giveup_code` (line 71) has no per-engine or per-code naming table at all — it is a single generic regex, `_GIVEUP_RE = re.compile(r"giveup:(-?\d+)(?::([A-Za-z0-9_]+))?")`, that parses whatever `giveup:<code>[:<name>]` text a driver's OWN diagnostic already carries (the shared protocol spelling `adapters.py` documents, originally pcrec's). `testees/onig/driver.c` (~line 372-380) builds its diagnostic as `giveup:%d:%s` using `onig_error_code_to_str`'s OWN message text, never a bench-side name. Confirmed the actual message for `-17` (`ONIGERR_RETRY_LIMIT_IN_MATCH_OVER`) via `strings` on this box's `/usr/lib/x86_64-linux-gnu/libonig.so`: `"retry-limit-in-match over"`. The regex's `[A-Za-z0-9_]+` group stops at the first non-alnum/underscore character, so it captures only the leading run, `"retry"`, from that message — reproduced standalone: `reduce.giveup_code({"match_outcome": "gave-up", "diagnostic": "giveup:-17:retry-limit-in-match over"})` returns `"-17:retry"`, matching the ledger's own rendering exactly. This is "the raw-code rendering already the designed behavior" per the brief's own fallback clause: the name is not a table lookup, it is parsed live from the engine's own message, and it already renders correctly for onig's -17 with no bench-side addition needed. `report.py`'s separate `_GIVEUP_NAMES_ENGINE` table (line ~2256) is a DIFFERENT thing entirely — it maps four pcrec-specific `PCREC_ERR_*` token names to `"vm"` for engine-inference on an unstamped pin, has nothing to do with rendering a code's name, and does not apply to onig's numeric codes at all; confirmed it is not the table the ledger item meant and not a table that should gain an onig entry |

## Validation run

`make check-schema`: 5 example(s) accepted, 73 sabotage(s) rejected for
the intended rule, 0 sabotage(s) WRONG — green, unaffected by these
doc-only changes (expected; touched no schema/validator file).

Targeted `reduce.py` coverage, since it was the one file examined for a
possible edit (found via `grep tools/selfcheck.py` for `reduce`/`giveup`
checks; `check_reduction()` at `tools/selfcheck.py:1493` is the section
that covers `reduce.py`'s `giveup_code`/`reduce_set_cell`, runnable
standalone without a build):

    python3 -c "import tools.selfcheck as sc; sc.check_reduction()"
    -- the shared set-grain reduction (reduce.py) --
       PASS  set-grain reduction on the hand-computed fixture
       PASS  ... and one give-up EXCLUDES the set and names its code

Both PASS, unchanged (no `reduce.py` edit was made). Did NOT run
`make check-harness` (324+ checks, ~20 min) or `make check-interpret`
per the brief's "NOT full check-harness" instruction and the
boilerplate's no-heavy-runs rule — this lane made no change either
target's own checks would need to catch (no schema, harness, adapter,
or reduce.py code was touched).

## What this lane did NOT do

- Did not merge (the manager merges, per BOILERPLATE.md).
- Did not touch `pcrecbench/reduce.py` or `pcrecbench/report.py` (item 3
  concluded NO-OP after direct evidence; no speculative edit made).
- Did not re-run or regenerate any report, sidecar, or store record —
  this lane's two changes are pure adapter-directory documentation.
- Did not run any measurement window or box-heavy check.

## Delivery bar

Branch `lane/b49docs`, committed (`dcf66ef` + this report), targeted
validation run with results inline above. Every promise in the brief is
either committed (items 1-2) or answered as NO-OP with evidence (item
3) — nothing OWED.
