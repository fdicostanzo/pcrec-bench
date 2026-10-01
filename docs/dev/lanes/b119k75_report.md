# lane b119k75 report — [B119], inbox I-123 (K75): no `-e utf8` cell of ours can carry an ill-formed subject

**Branch**: `lane/b119k75`, worktree `worktrees/b119k75`, from master
`bfa27e6`. Read/measurement lane only (a byte-level census, no engine
build, no `pcrecbench run`, no timing of any kind) — no code change,
because the answer to the charter question is NO.

## 1. The question (I-123, verbatim intent)

pcrec's find-all loop now aligns the resume position past UTF-8
continuation bytes after a NON-EMPTY match (match_api.md S3.1.1, K75,
D132): `pos = end`, then skip bytes `0x80-0xBF`. Our own formula (every
`pcrecbench/oracle_pcre2.py:next_start` call site and the identical
`utf8_next_start()` in every `testees/*/driver.c`) only does this for
the EMPTY-match arm; the non-empty arm is plain `pos = end`, no skip.
pcrec's ask: say whether any `-e utf8` cell of ours can have an
ill-formed subject. If none can, nothing changes on our side.

## 2. What "a `-e utf8` cell" means here, derived structurally

Our `--utf8` driver protocol flag (the thing that turns on the
character-boundary advance at all, in the oracle AND in every driver —
`pcrecbench/harness.py:901-902`, `pcrecbench/expectations.py:
utf8_advance`) fires **iff the sub-bench's OWN sidecar declares
`[expectations] encoding = "utf8"`** (`pcrecbench/subbench.py`'s
`SET_ENCODINGS`) — a property of the SET, never of which testee runs
it. This is NOT the same fact as a testee's own `encoding` key
(`pcrecbench/adapters.py:config_encoding`, pcrec's own `-e utf8` compile
flag): that is the ENGINE's identity, orthogonal to the oracle word and
to the find-all advance.

Grepping every `bench/*/subbench.toml` for `^encoding` (the eight
committed sets: `altwide`, `bounded`, `capability`, `email`, `litrun`,
`loglines`, `syntax`, `utf8`) finds exactly ONE declaration — `bench/
utf8@0.1`'s `encoding = "utf8"` (`bench/utf8/subbench.toml:81`). The
other seven default to `byte`, and `make check-harness`'s
`check_utf8_find_all_advance` confirms this LIVE, not just by grep:

    PASS  option word: 0 on every pattern of every byte set    7 set(s): altwide, bounded, capability, email, litrun, loglines, syntax

So "a `-e utf8` cell" reduces, exactly, to "any cell on `bench/utf8@0.1`"
— regardless of which testee (character-mode or byte-mode) runs it, and
regardless of whether a character-mode testee is paired with some OTHER
set (see §4). The population this question is ever about is bench/
utf8@0.1's own 98 subjects (91 `search_short` + 7 `throughput`).

## 3. Is bench/utf8@0.1's population well-formed? Yes, three independent ways

1. **By construction.** `bench/utf8/utf8text.py:text()` trims back to
   the LAST COMPLETE CHARACTER (`_trim_to_char_boundary`, a decode-and-
   truncate walk-back) before padding with ASCII spaces to the exact
   target size, then passes every subject through `decode_gate()` before
   its manifest row is written. `gen_subjects.py`/`gen_throughput_
   subjects.py` each carry a committed NEGATIVE-arm control
   (`_check_decode_gate_has_teeth`) proving the gate actually rejects a
   deliberately truncated byte string. Both `--check` modes are green in
   this worktree (`gen_subjects --check: OK (91 subjects, decode gate
   negative-arm control passed)`; `gen_throughput_subjects --check: OK
   (7 texts, decode gate negative-arm control passed)`).
2. **By the existing `make check-harness` gate**, run directly in this
   worktree (not merely read): `check_utf8_validate_once` re-derives all
   7,200 find-all cells (75 patterns × 96 subjects) byte-identical to the
   always-check path, and separately proves a DELIBERATELY ill-formed
   subject (a trailing `0xFF`) is REFUSED by name at the oracle
   ("UTF-8 error: illegal byte (0xfe or 0xff)"), never silently answered
   — i.e. if a committed subject WERE ill-formed, expectation derivation
   would have failed loudly, not produced a wrong count.
3. **By this lane's own from-scratch byte-level scan**
   (`docs/dev/measurements/probe_b119k75_utf8_wellformedness_census.py`):
   a UTF-8 validator written against RFC 3629's shape directly (lead
   byte decides sequence length; every continuation byte must be
   `0x80-0xBF`; overlong encodings, surrogate code points
   `U+D800-U+DFFF`, and code points above `U+10FFFF` all rejected) that
   shares no source with `decode_gate()` or with Python's own
   `bytes.decode("utf-8")` — cross-checked against the latter anyway, so
   the two independent opinions had to agree; every subject is also
   checked for byte-for-byte size and sha256 against its own manifest
   row BEFORE the scan, so "checked" means the exact file the manifest
   claims. Result: **0/98 ill-formed** on `bench/utf8`. Archived:
   `docs/dev/measurements/2026-10-01-b119k75-utf8-wellformedness-census.txt`.

The "invalid UTF-8 subjects" growth item (`docs/design/utf8_set_v1.md`
table row **(h)**) is explicitly PARKED for a future `bench/utf8@0.3`
("never a ranked cell", blocked at §14 Q10) — `bench/utf8/subbench.toml`
is still at `version = "0.1"`, and `@0.1` carries none of (h)'s
deliberately ill-formed shapes.

## 4. The roster-gating question, and why it doesn't change the answer

The brief also asked whether the harness structurally refuses pairing a
character-mode testee with a set that isn't declared UTF-8. It does
not: nothing in `pcrecbench/harness.py`/`adapters.py` checks the (set,
testee) pair before running, and `scripts/run_window.sh` takes
`SUBBENCH`/`TESTEES` as free-form env vars with no cross-validation.
`store/index.tsv` confirms no such pairing has ever been MEASURED (every
`*_utf8` testee_id row is `subbench=utf8`), but the harness would not
stop someone from trying `pcrecbench run --subbench capability --testee
pcrec-auto-utf8` today.

This does not change §2's reduction, though, because the `--utf8`
PROTOCOL flag is driven by the SET alone (confirmed above): pairing a
character-mode testee with a byte-encoded set would still never set
`utf8_adv`/`PCRE2_UTF`, so the K75 alignment formula would never be
exercised there either way — fixing it would be a no-op on that
(hypothetical, never-run) pairing.

**One adjacent fact surfaced by the full-roster census, named so it is
not mistaken for an exposure.** Running the SAME from-scratch scanner
over every OTHER committed set's subjects (the brief's step 2, done for
completeness) finds real ill-formed byte sequences in three sets:
`bench/capability`'s `nu-high-byte`/`nu-mojibake`/`nu-lead-no-cont`
(three short subjects — `0x81 0x82`, a curly-quote byte pair `0x93`,
and a lead byte `0xc2` with no continuation byte, respectively; `bench/
capability/NOTES.md:168-169` documents these as intentional byte-mode
witnesses, "legitimate because subjects live [in byte-encoding tests]");
`bench/email`'s `s-019` (a literal `0xFF`); and `bench/syntax`'s
`f-cafe`/`l-latin1` short subjects plus all three of its throughput
texts (`t-64k`/`t-256k`/`t-1m` — syntax's own `censustext.py` grammar is
not UTF-8-constrained, having no reason to be). None of these is a
"`-e utf8` cell" by §2's structural definition: these sets never set
the oracle word's `PCRE2_UTF` bit, so `--utf8` never reaches a driver on
them no matter which testee is asked to run there. A SEPARATE,
pre-existing concern — whether a `-e utf8`-compiled pcrec artifact's own
`PCREC_ERR_STARTPOS` guard (pcrec [K50]: "only an artifact compiled for
an encoding with multi-byte characters can return it") could fire on
such a cross-pairing's find-all loop regardless of our driver flag,
since that guard is a property of the COMPILED ARTIFACT, not of
whether we told the driver `--utf8` — is noted here for completeness
but is explicitly OUT OF SCOPE for K75: that fix lives entirely inside
the `utf8_adv` branch of our formula, and nobody has asked us to support
that cross-pairing. No ask is attached to this paragraph; the manager
may decide whether it is worth a future roster-gating lane on its own
merits.

## 5. Decision and disposition

**No cell of ours can carry an ill-formed subject under `-e utf8`.**
Per the brief's own branching instruction ("If NO cell can carry an
ill-formed subject, by construction or by a guard, write the answer
with its evidence and change no code"): **no code was changed.**
`pos = end` on the non-empty find-all arm stays exactly as it is in
`pcrecbench/oracle_pcre2.py` and in every `testees/*/driver.c` — the
population it would ever matter for is proven empty. No `tools/
selfcheck.py` NEGATIVE was added either, for the same reason a positive
fix has nothing to guard: there is no reachable ill-formed-subject path
to assert against, and inventing a synthetic one to exercise a formula
we are not changing would test nothing this repo's own data does not
already test more directly (`check_utf8_validate_once`'s existing
refusal-by-name control already covers "what happens if a subject WERE
ill-formed", and it is not this lane's to duplicate).

## 6. Charter-vs-committed checklist

| brief item | status |
|---|---|
| 1. Enumerate which sub-benches each character-mode testee is run on, or could be run on; check for roster/set gating | DONE — §4; no gating found, `store/index.tsv` confirms no non-utf8 pairing has been measured |
| 2. Check every subject (short + throughput) byte-for-byte for UTF-8 well-formedness, across all character-mode-testee-eligible sets | DONE — §3/§4; all 8 sets scanned (587 subjects), archived under `docs/dev/measurements/` with a source header |
| 3. Check what the oracle, drivers and harness do today with an ill-formed subject under a UTF-8 testee | DONE — §3 item 2 (`check_utf8_validate_once`'s existing refusal-by-name control, re-run live in this worktree) |
| 4. Decide; if no cell can be ill-formed, write the answer with evidence and change no code | DONE — §5; no code changed |
| 5. Draft a short outbox answer (O-80) as `docs/dev/lanes/b119k75_outbox_draft.md`, never editing `docs/dev/outbox_to_pcrec.md` | DONE — drafted, not filed |
| Deliverable: this report, committed | DONE |

Nothing OWED. No long run, no build, no store write — this lane never
needed the box.

## Files touched

- `docs/dev/measurements/probe_b119k75_utf8_wellformedness_census.py` (new)
- `docs/dev/measurements/2026-10-01-b119k75-utf8-wellformedness-census.txt` (new)
- `docs/dev/measurements/CLAUDE.md` (two new table rows)
- `docs/dev/lanes/b119k75_outbox_draft.md` (new, O-80 draft)
- `docs/dev/lanes/b119k75_report.md` (this file)
