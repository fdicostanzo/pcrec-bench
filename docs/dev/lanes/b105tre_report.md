# Lane b105tre — the tre bracket-escape declaration

Branch `lane/b105tre`, worktree `worktrees/b105tre`. Plan row [B105].

## Charter (from the brief)

> The tre testee receives PCRE-dialect `\`-escapes inside `[...]` and
> answers under POSIX rules, which gives silent wrong answers. The
> ruling: EXTEND tre's pre-compile declaration so that ANY bracket
> expression containing a backslash is refused as a named
> unsupported-by-declaration outcome, never a wrong answer. Translation
> is out of scope.
>
> Do: implement the refusal in the tre adapter's declaration path (the
> bracket scanner must handle `[]...]`, `[^]...]`, POSIX classes
> `[[:alpha:]]` and escaped/unescaped `]` correctly; test edge cases).
> Add a make-check control in tools/selfcheck.py: a bracket-with-backslash
> pattern is refused BY NAME, and a plain bracket pattern still compiles.
> Re-derive the census against the new declaration so every previously
> wrong row is now refused and no previously correct row newly refuses
> (list any that do, with the reason). Update testees/tre/CLAUDE.md. Run
> `make check-harness` detached (setsid, marker file, gnutimeout, ~30
> min). Check first with `uptime` that no heavy run is on the box, and
> watch the PID yourself until it finishes. Report the counts. Do not
> run a pinned window or write store/.

Amended mid-lane, twice, by the team lead: (1) do not launch
`make check-harness` myself while `b109twin` is timing the box — wait
for the slot, then launch and watch it (complied: killed my first,
in-flight launch by PID within ~80 s, relaunched once the slot cleared,
watched it to completion — **610/0**, confirmed by the team lead); (2)
after the team lead's own review caught a real over-refusal bug in the
scanner before merge, fix it, add the five named regression cases to
the selfcheck control, and re-derive the census over EVERY pattern in
every `bench/*/` set (not just the original 30-hit population),
archiving the before/after and every newly-declared pattern's bracket
text; re-run only the selfcheck function and the census, not the full
`make check-harness` again (the team lead's own call on whether to
re-run that).

## Charter-vs-committed checklist

| Item | Status | Where |
|---|---|---|
| Extend tre's pre-compile declaration: ANY bracket expr with a backslash → `unsupported-by-declaration` | **DONE** | `testees/tre/adapter.py` — `Adapter.compile()` checks `_bracket_backslash_content(pattern)` before ever calling `_compile_one` (`tre_regncompb`); only `FORM_PLAIN` carries the declaration row, matching `harness.run_cell`'s own central capability-decline shape |
| Bracket scanner handles `[]...]`, `[^]...]`, POSIX classes `[[:alpha:]]`, escaped/unescaped `]` | **DONE, and CORRECTED before merge** | `_find_bracket_spans`/`_bracket_backslash_content`, `testees/tre/adapter.py`. TWO-STATE scan: OUTSIDE a bracket, backslash keeps its ordinary ERE escaping power (`\[` never opens one, `\\` is one unit) — the manager's own review caught a real over-refusal bug in the first version, which gave backslash no power anywhere and so misread an escaped `\[` as a genuine open, wrongly declaring patterns like `\[\d+\]`/`a\[b` that contain no real bracket expression at all. INSIDE a genuine bracket, unchanged from the first version: a `]` right after `[`/`[^` is a literal first member; a `[:name:]`/`[.sym.]`/`[=c=]` sub-construct is skipped as one unit; backslash still has NO power (an escaped-looking `\]` closes the class early) |
| Test edge cases | **DONE** | `tools/selfcheck.py`'s `check_b105_tre_bracket_backslash_declaration`, Level 1: 14 scanner unit cases — the original 9 (`[^,\n]`, `[a-z]+`, `[]abc]`, `[^]abc]`, `[[:alpha:]]+`, `[[:alpha:]\d]`, `[a\]b]c`, empty pattern, unterminated `[`) plus the manager's 5 over-refusal regression cases (`\[\d+\]`/`a\[b` must NOT declare; `[\]]`/`[a\-z]`/`\\[\\]` must) |
| make-check control: bracket-with-backslash refused BY NAME, plain bracket still compiles | **DONE** | Same function, Level 2: real `Adapter.compile()` calls — a bracket-with-backslash pattern reads `unsupported-by-declaration` with `declaration_ref` citing `(d)4`/`[B105]` and no whole-subject artifact attempted; the "coincidentally safe" doubled-backslash idiom refuses too; a plain bracket pattern (no backslash) still compiles clean on both forms. Registered in `main()`. Standalone run after the fix: 4/4 PASS |
| Re-derive the census; list any newly-refused previously-correct row with reason | **DONE, TWICE** | (a) `probe_tre_bracket_escape_declaration_verify.py` + archived `.txt` — the original 30-pattern population through the real adapter: all 30 now `unsupported-by-declaration`, the four previously-wrong rows refused, exactly two previously-correct rows newly refuse by design (`codegrammar-flat`, `winpath-near-miss` — the "coincidentally safe" doubled-backslash idiom, no carve-out). (b) After the scanner fix, `probe_tre_bracket_escape_full_corpus_census.py` + archived `.txt` — EVERY pattern in EVERY `bench/*/` set (339 patterns, 8 sub-bench dirs, litrun/altwide included): the AFTER set is byte-for-byte the same 30 patterns; an old-buggy-vs-new-fixed scanner diff over all 339 finds **0** differences (the bug was real, proven by the 5 synthetic cases, but never fired on today's corpus — every `\[`-containing pattern also carries a separate genuine bracket elsewhere, traced by hand in the archive) |
| Update `testees/tre/CLAUDE.md` | **DONE, TWICE** | First pass: file-table row, item 4's FIXED note, the correctness table's superseded reading. Second pass (after the scanner fix): a new sub-note on item 4 documenting the over-refusal bug, the two-state fix, the five regression cases and the full-corpus census's 0-diff finding |
| Run `make check-harness` detached, watch PID, report counts | **DONE — 610/0** | Launched detached (`setsid bash -c 'gnutimeout 2400 make check-harness > LOG 2>&1; echo "DONE rc=$?" >> LOG; touch MARKER' & disown`) after `uptime` confirmed the box quiet (load average 0.29–0.50 range across both launches), watched by PID; confirmed by the team lead: **610/0**. (First launch predated the team lead's "wait for the slot" amendment and was killed by PID within ~80 s before it could interfere with `b109twin`'s timing window; relaunched cleanly once the slot cleared.) |
| No pinned window, no store/ write | **Confirmed not done** | — |

## Commits (branch `lane/b105tre`)

1. `d22e8c6` — the adapter change (the scanner + `compile()` hook)
2. `8acf078` — the make-check control
3. `adae9ab` — the re-derived census over the original 30-pattern population (probe + archive)
4. `3c5cea4` — `testees/tre/CLAUDE.md` documentation, first pass
5. `fa56cb2` — this report, first version
6. `43cfc52` — merge `master` (brings in KB-35's selfcheck row + [B109]'s reseed-twin work; no conflict with this lane's own files beyond a clean auto-merge in `docs/dev/measurements/CLAUDE.md`/`tools/selfcheck.py`)
7. (the post-merge `make check-harness` run, launched and killed once, relaunched and watched to completion — **610/0**, confirmed by the team lead)
8. `cd9251c` — the over-refusal fix: the two-state scanner, the five regression cases
9. `b5d1729` — the full-corpus census (probe + archive) over all 339 patterns, plus the `testees/tre/CLAUDE.md` second-pass documentation
10. this report, updated

## Not done, per the brief's own scope

- No pinned window, no `store/` write.
- No translation of any pattern's PCRE-dialect bracket syntax to a
  portable POSIX spelling — explicitly out of scope; every genuine hit
  is refused, unconditionally, with no exception for a spelling that
  happens to answer correctly today.
