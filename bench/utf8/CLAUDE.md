# bench/utf8/ — the UTF-8 encoding set (`utf8@0.1`, U3's row)

WHAT THIS DIRECTORY IS TODAY: **U3's deliverable only** — the SUBJECTS,
and nothing else. Design: `docs/design/utf8_set_v1.md` v0.2 (plan row
[B77], inbox I-90/I-94). **No `subbench.toml` sidecar exists yet**, so
`bench/utf8/` is deliberately NOT enumerated by `tools/selfcheck.py`'s
`subbench_dirs()` (it checks `os.path.exists(subbench.toml)`) and
therefore NOT touched by any of `make check-harness`'s generic `bench/*/`
gates — the same posture `bench/capability/` held between L1/L2 (curation
staging) and L3 (the runbench build), documented in `bench/CLAUDE.md`'s
own paragraph about it. This is a STATED CHOICE, not an oversight: U4
creates `subbench.toml` (the build plan, `utf8_set_v1.md` §13), and only
then does this directory become a real, checked sub-bench with a row in
`bench/CLAUDE.md`'s own table.

## What IS built (U3)

| file | role |
|---|---|
| `pool_lat.tsv`, `pool_cyr.tsv`, `pool_cjk.tsv`, `pool_asc.tsv`, `pool_mix.tsv` | the FIVE COMMITTED WORD POOLS (`utf8_set_v1.md` §4.1, Q2): `lat` (French/German/Spanish, Latin-1-Supplement-heavy, 198 words), `cyr` (Russian, 175 words), `cjk` (Japanese+Chinese, kana+han, 150 words), `asc` (byte-clean English, 363 words, the CONTROL vocabulary), and `mix` (NOT a fifth prose vocabulary — 99 emoji/symbol tokens, 80 from the Emoticons block U+1F600-U+1F64F plus 19 common symbols, that the `mix` corpus interleaves into sentences drawn from the other four, per §4.2's own description of what `mix` is). One word/token per line after a `word` header, deduplicated. `fidelity = synthesized` / `source_name = authored` in `capability`'s own provenance vocabulary (§4.1's Q2 ruling): individual common words of a natural language carry no URL to cite |
| `utf8text.py` | the shared xorshift64* primitive (copied, not imported, from `bench/syntax/censustext.py`'s / `bench/capability/captext.py`'s shape) + the five-corpus sentence grammar + **THE SIZE-FITTING BOUNDARY RULE** (`text()`: trim to the last complete UTF-8 character at or before the byte budget, pad with ASCII spaces `0x20` to the exact target size — §4.1, F-M1) + **THE DECODE GATE** (`decode_gate()`, raises `UnicodeDecodeError` on ill-formed input) |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv`: **91 typed short subjects** (90 = 15 per family (a)-(f) + 1 dedicated floor witness — see "The 90-vs-91 arithmetic" below), typed against `utf8_set_v1.md` §5's pattern TEXT directly (no `patterns.rxt` exists yet — see "What is NOT built" below). Every subject passes the decode gate before its manifest row is written. `--check` re-derives AND re-runs the DECODE-GATE NEGATIVE-ARM CONTROL (a fixture deliberately truncated mid-character must FAIL) |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv`: **seven throughput texts**, ~1.56 MB total — `t-64k`/`t-256k`/`t-1m` from the `mix` grammar, plus the per-script 64 KB arm (`t-64k-lat`/`t-64k-cyr`/`t-64k-cjk`/`t-64k-asc`). Same decode-gate negative-arm control as `gen_subjects.py` |
| `manifest.tsv`, `manifest_throughput.tsv` | committed: `id, len, sha256, description, periodic` (the standard four-or-five-column shape, `bench/CLAUDE.md`'s own rule) |
| `gen_subject_facts.py` | writes `subject_facts.tsv`: the per-subject UTF-8 LEAD-BYTE HISTOGRAM (`utf8_set_v1.md` §4.2 — "the histogram is unlike English" as a committed, re-derived FACT rather than a claim), over EVERY subject in both manifests. `--check` re-derives and diffs, and cross-checks each row's `len` against the owning manifest's own `len` column |
| `subject_facts.tsv` | committed: `id, source, len, n_chars, n_ascii, n_lead2, n_lead3, n_lead4, n_cont, pct_ascii, pct_multibyte, dominant_lead, avg_bytes_per_char` — MEASURED confirmation of §4.2's own claims: `t-64k-lat` dominant lead `0xc3` (Latin-1 Supplement), `t-64k-cyr` dominant `0xd0` (Cyrillic), `t-64k-cjk` dominant `0xe3` with a 3-byte lead spread and `avg_bytes_per_char` ≈ 2.6, `t-64k-asc`/`floor-hit` pure ASCII (`avg_bytes_per_char` = 1.0, `dominant_lead` = `n/a`) |
| `subjects/`, `throughput/` | GENERATED and gitignored (`.gitignore`'s existing `bench/*/subjects/` / `bench/*/throughput/` wildcard rules — no new gitignore entry was needed) |

REGENERATING. `python3 bench/utf8/gen_subjects.py`,
`gen_throughput_subjects.py`, `gen_subject_facts.py`, in that order
(subject_facts reads both subject trees). All three are deterministic and
support `--check`. **None of this runs under `make check` /
`make check-harness` yet** (no `subbench.toml` — see above); run them by
hand until U4 wires the sidecar in.

## The 90-vs-91 arithmetic, stated once

`utf8_set_v1.md` §4.3/§10.3 computes "90 typed short subjects" as
15 × 6 families and does not separately count the floor. This generator
states BOTH numbers rather than silently picking one convention:
**90 family subjects + 1 floor witness (`floor-hit`, the literal `~`) =
91 total**, printed by `gen_subjects.py`'s own stdout and asserted by
`build()`'s `N_TOTAL = 91` check. `bench/capability/gen_subjects.py`
folds its own floor witness into its stated "75" instead — this module
does not silently follow that precedent, because the design note's own
§10.3 arithmetic (`76 patterns × 6 passes × 90 subjects`) reads as 90
being the FAMILY total specifically, and U4/U5 should not have to
re-derive which convention applies to which count from context.

## What is NOT built here — U4 and U5's own rows

This directory is **not yet a runnable sub-bench**. In the build order
(`utf8_set_v1.md` §13):

- **`subbench.toml`** (the sidecar declaring `id`, `version`, `regimes`,
  `short_search_max_bytes`) — **U2/U4**. Until it exists, `--subbench
  utf8` resolves nothing and `tools/selfcheck.py`'s generic gates never
  see this directory (see above).
- **`patterns.rxt` / `patterns/*.rx`** (the 76 patterns — 75 members +
  floor — across families (a)-(f), each with `tag family=`/`requires=`
  and the file-scope `ext bench` roster block) — **U4**, depending on
  this lane's typed subjects and on U2's roster work. Every subject
  description above cites the PATTERN TEXT from `utf8_set_v1.md` §5
  directly (e.g. "`(?i)k` (ci-kelvin)"), never a `.rx` file, because none
  exists yet.
- **`expectations.tsv`** (oracle-verified match/no-match/find-all
  answers) — **U5**, once U1 lands the per-pattern UTF option word and
  the character-boundary find-all advance in `oracle_pcre2.py` (the
  shared harness change `utf8_set_v1.md` §8.4 calls "the sharpest harness
  change this set forces") and U4 builds the real patterns. Until then
  every subject's stated "hit"/"miss"/"near-miss" in this directory is a
  TYPED INTENT (`bench/capability/gen_subjects.py`'s own discipline —
  "this module only states the INTENT each subject was typed for"), not
  a verified answer.
- **`NOTES.md`** (the objective, the outlier rule R0-R8, the growth plan,
  the predictions TSV transcription) — **U5**.
- **Two subjects name a live U4 coordination point.** `alt-cyr64-hit`
  and `alt-cyr64-miss` are typed against an ASSUMPTION about
  `alt-cyr-64` (the 64-branch Cyrillic alternation, `utf8_set_v1.md`
  §5(d)) that does not exist yet — that its word list includes
  "дом" (house) and excludes an uncommon compound. Each subject's own
  `description` states the assumption; if U4's real 64-word list
  disagrees, these two subjects (not the rest of the corpus) are the
  ones to revisit.
- **`prp-ingreek`** (the REFUSAL witness, `utf8_set_v1.md` §5(f)/§9: a
  compile-axis `did-not-compile` row on every engine, no match rows —
  the same "legal today" shape `bench/bounded`'s 65535-cap rung sets,
  KB-4) has **no typed subject**, deliberately — a refusal has no speed,
  so nothing here needs to hit or miss it.

## The generic-gate question, answered directly

`make check-harness`'s generators-reproduce-manifests /
expectations-re-derive / floor-pattern-smoke gates enumerate `bench/*/`
via `subbench_dirs()`, which is gated on `subbench.toml`'s existence
(`tools/selfcheck.py:185-200`; see `bench/CLAUDE.md`). Since this
directory carries no sidecar, **those gates do not run against it at
all** — not a weakened check, and not a special-cased skip inside
`tools/selfcheck.py` either: the SAME predicate that already excludes
`bench/capability/` during its own L1/L2 staging window excludes this
directory today, unmodified. `gen_subjects.py --check`,
`gen_throughput_subjects.py --check` and `gen_subject_facts.py --check`
are run BY HAND in this lane's own validation (see
`docs/dev/lanes/b77u3_report.md`) and will start running under `make
check-harness` automatically, by the same enumeration, the moment U4
commits `subbench.toml` — no gate code changes when that happens.
