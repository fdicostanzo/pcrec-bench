# [B38] — THE .rxt SET EXPORTER

Lane `b38rxt`, 2026-09-07 (branch `lane/b38rxt`). Frank's chartered order for
this session: [B40] then [B33] then **[B38]** then [B13] then [B7] — [B40]
and [B33] item (1)+(2) are done; this lane is [B38].

## What was built

- `tools/export_rxt.py` — the exporter. `python3 tools/export_rxt.py
  <bench-dir> [-o out.rxt] [--verify [PCREC_BIN]]` reads a `bench/<name>/`
  sidecar through `pcrecbench.subbench` (never a second parser), enumerates
  patterns in the sidecar's own order (`Subbench.patterns`, i.e. the TOML
  array order == file order in `subbench.toml`), and writes a `.rxt`
  SOURCE file: one `target = <name>` head row per pattern followed by one
  `pattern <text>` / `name <id>` block per pattern, matching the shape of
  pcrec's own `tests/definitions/composed.rxtin` example minus the `m`/`n`
  case lines (this is pure SOURCE, no test assertions). No
  `config`/`flags`/`engine`/`budget`/`encoding` line is ever written (rule
  5). `--verify` round-trips the export against `PCREC_BIN --list-source`
  (default: the pinned binary via the pcrec adapter's `pin_binary(build=
  False)` — refuses if it is not already built, never triggers a build).
- `tools/selfcheck.py`'s new `check_rxt_export` — wired into `make
  check-harness` (see "the standalone-vs-check-harness decision" below).
- Five committed exports, `bench/<name>/export/<name>.rxt` (the directory
  name, not the sidecar's own `id` — see "naming" below): `altwide.rxt`
  (33), `bounded.rxt` (43), `email.rxt` (3), `loglines.rxt` (11),
  `syntax.rxt` (95). **33+43+3+11+95 = 185**, matching the corpus-wide
  count (`ls bench/*/patterns/ | wc -l`-style enumeration, confirmed
  before writing any code).
- CLAUDE.md updated: `tools/CLAUDE.md` (the file-role table + a `[B38]`
  narrative block) and all five `bench/<name>/CLAUDE.md` (one row each,
  documenting the `export/<name>.rxt` location).

## Rules (1)-(7), re-verified at the CURRENT 185-pattern corpus

I-43 (2026-09-04) measured 90 ids across four sets; bench/syntax (95 more)
did not exist yet. Every rule was re-checked here against the real,
current sidecars — not cited from I-43's numbers — via a direct script
over `pcrecbench.subbench.find()` for all five sets before any exporter
code was written:

1. **Block-name grammar** `[A-Za-z_][A-Za-z0-9_.-]*` — **all 185 ids
   pass**, none needs a name map. (`NAME_RE` in `export_rxt.py`; the check
   is also re-run live by `check_rxt_export`'s call into `build_rxt`, which
   raises `ExportError` naming the offending id and set if this ever
   regresses.)
2. **`target = <name>` derives the prefix, `-`/`.` → `_`, one row per
   pattern** — implemented in `derive_prefix`; the exporter never writes a
   hand mapping.
3. **Two names → one prefix is a REFUSAL naming both.** Re-verified: NO
   within-set collision exists in any of the five sets today (checked by
   deriving every pattern's prefix per set and looking for a collision
   with a different source name). More than that — **it is currently
   unreachable, not merely unseen**: every pattern id is constrained by
   the record schema's own slug rule (`^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`,
   enforced at `Subbench.__init__` time since KB-12/[B36]), an alphabet
   containing neither `.` nor `_`. Since `derive_prefix` only rewrites `-`
   and `.` to `_`, and no valid slug can already contain a `_`, the map is
   PROVABLY INJECTIVE over that alphabet — two distinct valid slugs can
   never land on one prefix. This is why the collision-refusal control
   (below) has to use a hand-built stand-in rather than a real sidecar.
   The one collision I-43 found (`floor`) is unaffected by any of this: it
   is not a *derivation* collision, it is the same literal name `floor`
   declared in more than one set — and it is now a **five-way** cross-set
   collision (bench/syntax also declares a `floor` pattern; I-43 saw it in
   four sets). Exporting PER SUB-BENCH still avoids it completely, exactly
   as I-43 concluded.
4. **`name <id>` keeps the id unchanged**, `-` and all — implemented
   directly (`"name %s" % n`, no transformation).
5. **No `config`/`flags`/`engine`/`budget`/`encoding` lines** — none are
   ever emitted; `build_rxt` has no code path that could write one.
6. **The pattern line is written VERBATIM, RAW BYTES, with no escaping —
   period, not conditionally.** This is where this lane's reading departs
   from a literal reading of the brief's own wording ("if any pattern...
   DOES contain a tab/newline/non-ASCII byte, the .rxt escape vocabulary
   must be applied on export"). Before writing any exporter code I read
   `docs/spec/rxt_format.md`'s own words on the `pattern` production:
   *"`<regex>` is everything after the first space on the line, taken
   verbatim to the end of the line (**no quoting, no escaping**)"* — and
   confirmed it empirically against the pin (d34c9131):

       $ printf 'target = t1\n\npattern ^\\d+\\t$\nname t1\n' > t.rxtin
       $ pcrec --list-source t.rxtin | grep -v '^#'
       target  1  t1  t1
       pattern 3  t1     ^\\d+\\t$

   The SOURCE line `pattern ^\d+\t$` is seven literal characters — `^`,
   `\`, `d`, `+`, `\`, `t`, `$` — read with **no** escape decoding at all;
   `--list-source`'s dump then escapes each literal backslash as `\\`
   because THAT column is what needs TSV-framing protection, not because
   the source line was ever unescaped on the way in. A second test with a
   REAL tab byte (0x09) in the pattern confirms the same thing from the
   other side: the raw tab is legal, unescaped, rest-of-line content in
   the `.rxt` SOURCE, and only becomes `\t` in `--list-source`'s own
   dump. If the exporter applied the escape vocabulary on WRITE, a
   pattern containing a literal backslash (i.e. almost every regex in
   this corpus — `\d`, `\b`, `\w`, …) would round-trip as a literal
   two-character `\\` instead of one backslash, corrupting every pattern
   that needs one. **Writing raw bytes verbatim is therefore not merely
   sufficient for today's ASCII/tab-free corpus — it is the only correct
   behavior the format supports**, and the escape vocabulary belongs
   entirely to the ROUND-TRIP CHECK's decoder (`decode_rxt_escape`, the
   exact inverse of pcrec's own `put_escaped` in
   `src/parse/rxt_source.c`), which undoes `--list-source`'s TSV-safety
   escaping on its `pattern`/`value`/`pcrec` columns before comparing
   against `Subbench.pattern_bytes()`. Re-verified at the current corpus:
   **0 of 185 patterns contain a tab, CR, newline, or non-ASCII byte** —
   the `witnesses` list `build_rxt` returns (patterns that "needed
   flagging", i.e. carried a byte outside plain-ASCII-printable) is empty
   on every one of the five sets, printed explicitly by both the CLI and
   `check_rxt_export`'s PASS line ("N pattern(s), none needed escaping").
   The one byte sequence the format genuinely CANNOT represent in a
   `pattern` line — a literal embedded newline or CR, since the format is
   line-oriented and a newline ends the line — is a hard `ExportError`
   naming the pattern; none of the 185 hits it.
7. **A hyphenated name is buildable as a `target` but not callable from a
   pattern** (`(?&some-id)`, PCRE2's group-name grammar). Checked
   precisely, not just grepped: `grep -rl '(?&'` DOES find three files
   (`bench/email/patterns/factored.rx`,
   `bench/syntax/patterns/{rec-define,rec-name}.rx`), but every `(?&...)`
   in them names a group DEFINED INSIDE THAT SAME PATTERN's own text
   (`atom`/`qchar`/`label`/`octet` in `factored.rx`; `d` in
   `rec-define.rx`; `p` in `rec-name.rx`) — ordinary PCRE2 same-pattern
   recursive subroutine calls, resolved entirely within one pattern's own
   compile, unrelated to the `.rxt` file's cross-BLOCK composition
   mechanism rule 7 is actually about (which needs a `lib`/`target`
   apparatus none of our exports declare — rule 5 rules that out by
   construction). None of those local group names collides with any
   sidecar pattern id either. So: **no pattern in any of the five sets
   calls another PATTERN BLOCK by id** through the mechanism rule 7
   concerns, and since none of our exports compose across blocks at all
   (rule 5), the question does not arise today. Noted here for whoever
   adds the first cross-pattern reference.

## Round-trip result, per sub-bench

Every set round-trips clean against the pinned binary
(`/home/duxevents/pcrec-bench/build/pcrec-d34c9131/build/pcrec
--list-source`, never built by this lane — confirmed already present
before any check ran):

| sub-bench | patterns | round-trip |
|---|---:|---|
| altwide | 33 | OK |
| bounded | 43 | OK |
| email (`email-specimen`) | 3 | OK |
| loglines | 11 | OK |
| syntax | 95 | OK |
| **total** | **185** | **185/185 OK** |

`--list-source` on the largest set (syntax, 95 patterns) measured ~2 ms;
`check_rxt_export`'s full pass over all five sets plus both collision
controls measured **0.15 s** wall-clock (`time python3 -c ...
check_rxt_export()`), python-startup-dominated.

## The collision-refusal control

Since rule 3's refusal is provably unreachable through any real
`bench/<name>/` sidecar (see rule 3 above), the control in
`check_rxt_export` calls `export_rxt.build_rxt` directly on a hand-built,
duck-typed stand-in for `Subbench` (`.id`, `.root`, `.version`,
`.patterns` of stub objects carrying `.name`, and a `.pattern_bytes()`
method) — never a real `bench/` directory, never through
`pcrecbench.subbench.check_id`'s gate. Two arms:

- **Colliding**: ids `a-b` and `a.b` (pcrec's own spec's canonical
  example: "`a-b` and `a.b` both give `a_b`") — refused, message names
  both ids and the shared prefix `a_b`:

      rxt-export-collision-control: pattern ids 'a-b' and 'a.b' both
      derive the target prefix 'a_b' (inbox I-43 rule 3) -- ...

- **Control**: ids `a-b` and `c-d` (no collision) — builds fine (893
  bytes), proving the refusal above is not simply firing on every input.

Same technique this codebase already uses for a rule that is untestable
through a real fixture file (`pcrecbench/CLAUDE.md`'s R3 tier note on the
[B9] reporter's tier column).

## The standalone-vs-check-harness decision

**Wired into `check-harness`, not a standalone `make` target.**
`--list-source` is parse-only — no compile, no C emission, no gcc — and
was measured at ~2 ms for the largest set (95 patterns) and 0.15 s wall
for the whole check function (five sets + two collision-control arms,
python-startup-dominated). This is negligible against `check-harness`'s
existing ~20-minute budget, unlike `make cc-gate-census` ([B33]), which
compiles every corpus pattern under two engine axes and is deliberately
kept OUT of `make check` for exactly that cost (`tools/CLAUDE.md`/
`Makefile`'s own stated reasoning). There is no proportional argument for
giving this one its own target: it has none of `cc-gate-census`'s
wall-clock problem, and folding it into `check-harness` means a re-pin
(which already re-runs `check-harness`) automatically re-verifies the
round-trip against the new binary with zero extra ceremony.

## Validation

- `make check-schema`: **4/72/0** (unchanged; this lane touches no schema
  file).
- `make check-harness`: **344/344, 0 FAILED** (full run, background log
  `/tmp/.../scratchpad/b38rxt-checkharness.log`, `DONE rc=0`). The
  root CLAUDE.md STATUS text's "324" was stale, as the brief warned it
  might be -- the actual pre-lane baseline (independently confirmed by
  the team lead reading the same log) was **337**; this lane's
  `check_rxt_export` adds exactly the predicted **7** PASS lines (5
  sub-bench round-trips + 2 collision-control arms), landing at
  337 + 7 = **344**, matching to the check.
- `check_rxt_export()` run standalone (both before and after a header-
  format bug fix, see below, and again as part of the full suite above):
  **7/7 PASS, 0 FAIL** every time.

### One bug found and fixed during validation

The exporter's header-comment builder mixed Python `bytes` and `str`
formatting (`b"...%r..." % (id.encode("ascii"),)`), which rendered the
sidecar id as its Python bytes-repr (`b'email-specimen'`) instead of the
plain string (`email-specimen`) in the generated file's own header
comment. Caught by inspecting the first generated file
(`bench/email/export/email.rxt`) by eye before committing; fixed by
building the header as plain `str` lines and encoding the whole line at
once. All five files were regenerated and re-verified after the fix
(`--verify` still 185/185 OK). No behavior outside the header comment
text was affected — the `target`/`pattern`/`name` body lines were never
touched by the bug.

## Naming convention

The five files are named after their **directory** (`bench/<name>/`), not
their sidecar's own `id` field — the two differ only for email
(`email-specimen`). Chosen because every other cross-reference in this
codebase (CLAUDE.md prose, `--subbench` CLI resolution, `bench/*/`
enumeration) already speaks the directory name as the set's primary
handle, and `email-specimen.rxt` sitting next to four files all named
after their directory would be the odd one out for no reader benefit.

## Do-not-touch confirmed

No bench sidecar content was modified (only each set's `CLAUDE.md`, plus
the new `export/` subdirectory). No pcrec source or build tree was
touched — the pinned binary at
`/home/duxevents/pcrec-bench/build/pcrec-d34c9131/build/pcrec` was already
present before this lane started and was never rebuilt (`pin_binary
(build=False)` is what both the CLI's `--verify` and `check_rxt_export`
call). No `store/` records were written — this lane produces no
measurement.

## Files touched

- `tools/export_rxt.py` (new)
- `tools/selfcheck.py` (`check_rxt_export`, wired into `main()`)
- `tools/CLAUDE.md`
- `bench/{altwide,bounded,email,loglines,syntax}/export/*.rxt` (new,
  committed)
- `bench/{altwide,bounded,email,loglines,syntax}/CLAUDE.md`
- `docs/dev/lanes/b38rxt_report.md` (this file)

## Process note

The all-content work (exporter, gate, five exports, docs) was done and
committed before the background `make check-harness` run finished; the
run's completion marker (`DONE rc=0` in the scratchpad log) landed at
17:10 EDT but sat unchecked for several hours before the team lead
flagged it -- the marker was in a plain `until grep -q ...; sleep 15`
background Bash task rather than something that pushed a notification
proactively on its own, and it was not re-checked until the lead's
message prompted it. Finalized (this section, the validation numbers
above, and the commit) immediately once flagged. No other background
jobs were outstanding at that point.
