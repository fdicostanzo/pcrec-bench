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

## Charter-vs-committed checklist

| Item | Status | Where |
|---|---|---|
| Extend tre's pre-compile declaration: ANY bracket expr with a backslash → `unsupported-by-declaration` | **DONE** | `testees/tre/adapter.py` — `Adapter.compile()` checks `_bracket_backslash_content(pattern)` before ever calling `_compile_one` (`tre_regncompb`); only `FORM_PLAIN` carries the declaration row, matching `harness.run_cell`'s own central capability-decline shape, so every regime (incl. `match`, which falls back to `plain` when no `whole-subject` key exists) reads the declined result |
| Bracket scanner handles `[]...]`, `[^]...]`, POSIX classes `[[:alpha:]]`, escaped/unescaped `]` | **DONE** | `_find_bracket_spans`/`_bracket_backslash_content`, `testees/tre/adapter.py`. POSIX rules throughout: a `]` right after `[`/`[^` is a literal first member; a `[:name:]`/`[.sym.]`/`[=c=]` sub-construct is skipped as one unit so its own interior `]` cannot be mistaken for the outer close (guards `bench/syntax/patterns/cls-posix.rx` / `bench/utf8/patterns/cls-posix-alpha.rx`, both `[[:alpha:]]+`); backslash is given NO escaping power anywhere in the scan (an escaped-looking `\]` closes the class EARLY under real POSIX/TRE rules — confirmed by test case, not assumed) |
| Test edge cases | **DONE** | `tools/selfcheck.py`'s `check_b105_tre_bracket_backslash_declaration`, Level 1: 9 scanner unit cases (`[^,\n]`, `[a-z]+`, `[]abc]`, `[^]abc]`, `[[:alpha:]]+`, `[[:alpha:]\d]`, `[a\]b]c` — the escaped-`]`-closes-early case, empty pattern, unterminated `[`) |
| make-check control: bracket-with-backslash refused BY NAME, plain bracket still compiles | **DONE** | Same function, Level 2: real `Adapter.compile()` calls — a bracket-with-backslash pattern reads `unsupported-by-declaration` with `declaration_ref` citing `(d)4`/`[B105]` and no whole-subject artifact attempted; the "coincidentally safe" doubled-backslash idiom refuses too; a plain bracket pattern (no backslash) still compiles clean on both forms. Registered in `main()`. Standalone run: 4/4 PASS |
| Re-derive the census; list any newly-refused previously-correct row with reason | **DONE** | `docs/dev/measurements/probe_tre_bracket_escape_declaration_verify.py` + archived `2026-09-28-tre-bracket-escape-declaration-verify.txt`. All 30 of the original census's hits now read `unsupported-by-declaration`. The four previously-wrong rows (`high-byte-run`, `tag-pair-match`, `wild-waf-crs-942360-concat-sqli`, `mojibake-curly-quote`) are refused. **Exactly two previously-correct rows newly refuse**, named and reasoned in both the archive and `testees/tre/CLAUDE.md`: `codegrammar-flat` (`[^"\\]`) and `winpath-near-miss` (`[^<>:"/\\|?*]`) — the census's own "coincidentally safe" doubled-backslash idiom (n_wrong=0 at cf0962e3); the ruling is "ANY bracket expression containing a backslash", with no carve-out for a spelling that happens to answer right today. Three more rows reclassify `did-not-compile` → `unsupported-by-declaration` (same (d)4 mechanism, caught earlier — not a correctness move) |
| Update `testees/tre/CLAUDE.md` | **DONE** | File-table row for `adapter.py`; item 4 gets a FIXED note with the full derivation; the correctness table's "systematic raw-high-byte handling gap" reading is superseded with a note identifying all four wrong rows as the same bracket-backslash mechanism, now closed |
| Run `make check-harness` detached, watch PID, report counts | **OWED — see below** | |
| No pinned window, no store/ write | **Confirmed not done** | — |

## The one deviation from the brief: `make check-harness` is OWED to the manager

I launched `make check-harness` detached exactly as briefed (`uptime` checked
quiet first: load average 0.15/0.24/0.18; `setsid bash -c '/usr/bin/gnutimeout
2400 make check-harness > LOG 2>&1; echo "DONE rc=$?" >> LOG; touch MARKER' &
disown`) and began watching the PID. Mid-run, the team lead sent an amendment:
**do not launch `make check-harness` on my own** — lane `b109twin` is timing
on this box, and my run would contend with it. I killed the run immediately
by PID (verified each PID's `cwd` was this worktree first, per BD3 — never
`pkill -f`): `kill -TERM` on the `setsid bash` wrapper, `gnutimeout`, `make`,
the `sh -c` and the `python3 tools/selfcheck.py` process, all five confirmed
gone within a second. I removed the stale log/marker files and stopped the
background poll task I had also started (`TaskStop`) so nothing keeps
watching for a marker that will never appear from that killed run.

**Owed**: the full `make check-harness` run, once the manager clears the box
of `b109twin`'s timing window. Exact command (run from
`/home/duxevents/pcrec-bench/worktrees/b105tre`):

```
uptime   # confirm quiet first
LOG=<scratchpad>/b105tre-checkharness.log
MARKER=<scratchpad>/b105tre-checkharness.done
rm -f "$LOG" "$MARKER"
setsid bash -c "/usr/bin/gnutimeout 2400 make check-harness > '$LOG' 2>&1; echo \"DONE rc=\$?\" >> '$LOG'; touch '$MARKER'" < /dev/null &
disown
```

Then poll `$MARKER` (a background `run_in_background: true` until-loop, not a
blocking foreground sleep) and report the final `check-harness: N check(s)
passed, M FAILED` line plus the pass/fail count for the new
`check_b105_tre_bracket_backslash_declaration` control specifically. The
control was verified standalone (see above, 4/4 PASS) and the rest of the
suite is untouched by this lane's changes (no other file besides
`testees/tre/adapter.py`, `tools/selfcheck.py`, `testees/tre/CLAUDE.md`,
`docs/dev/measurements/{CLAUDE.md,probe_tre_bracket_escape_declaration_verify.py,
2026-09-28-tre-bracket-escape-declaration-verify.txt}` changed), so the
expected full-suite delta is "+1 check, 0 regressions" — but that expectation
is unverified against the real suite count until the run happens.

## Commits (branch `lane/b105tre`)

1. `d22e8c6` — the adapter change (the scanner + `compile()` hook)
2. `8acf078` — the make-check control
3. `adae9ab` — the re-derived census (probe + archive)
4. `3c5cea4` — `testees/tre/CLAUDE.md` documentation
5. this report

## Not done, per the brief's own scope

- No pinned window, no `store/` write.
- No translation of any pattern's PCRE-dialect bracket syntax to a
  portable POSIX spelling — explicitly out of scope; every hit is
  refused, unconditionally.
