# [B77] lane U3 — bench/utf8/ subjects — report

Branch `lane/b77u3`, worktree `agent-aacccdb2e1cce66a9`. Charter:
`docs/design/utf8_set_v1.md` v0.2 §4 (subjects, incl. §4.1's size-fitting
boundary rule), §2 (set identity), §13's U3 row, §15 (risks). Read in
full before writing anything. Coordinating lane: `b77u1` (the shared
oracle/driver harness change) runs in parallel and was NOT touched by
this lane, per the brief.

## Charter-vs-committed checklist

| brief item | committed | notes |
|---|---|---|
| the five word pools | `bench/utf8/pool_{lat,cyr,cjk,asc,mix}.tsv` | 198/175/150/363/99 words/tokens respectively (deduplicated); `mix` carries emoji (80, Emoticons block U+1F600-U+1F64F) + 19 common symbols, not a fifth prose vocabulary — utf8_set_v1.md 4.2's own description of what the `mix` corpus is |
| `utf8text.py` | `bench/utf8/utf8text.py` | shared xorshift64* (copied, not imported, from `bench/syntax/censustext.py`/`bench/capability/captext.py`'s shape); five-corpus sentence grammar; `_trim_to_char_boundary` + `text()`'s ASCII-space pad (the boundary rule); `decode_gate()` |
| `gen_subjects.py` / `gen_throughput_subjects.py` (deterministic) | both files, both re-run byte-identical | `gen_subjects.py`: 91 subjects (90 = 15 × six families (a)-(f) + 1 floor witness — see "The 90-vs-91 arithmetic" in `bench/utf8/CLAUDE.md`). `gen_throughput_subjects.py`: 7 texts, 1,638,400 B (~1.56 MB) — three `mix` sizes (64k/256k/1m) + the four-script 64 KB arm, matching utf8_set_v1.md 4.3's own arithmetic |
| the two sha256 manifests | `manifest.tsv` (91 rows), `manifest_throughput.tsv` (7 rows) | standard `id, len, sha256, description, periodic` five-column shape (`bench/CLAUDE.md`'s rule) |
| `subject_facts.tsv` with its `--check` | `bench/utf8/gen_subject_facts.py` + committed `subject_facts.tsv` (98 rows = 91 + 7) | the per-subject UTF-8 lead-byte histogram utf8_set_v1.md 4.2 calls for (a sixth manifest column is not accepted, `bench/CLAUDE.md`'s "the loader takes 4 or 5" — so it lives in its own facts table, `bench/bounded/gen_pattern_facts.py`'s own precedent). Cross-checks each row's `len` against the owning manifest |
| the size-fitting boundary rule | `utf8text._trim_to_char_boundary` + `text()`'s pad step | every one of the 7 throughput texts is EXACTLY its named byte size (`assert len(trimmed) == nbytes` in `text()`; independently confirmed: `manifest_throughput.tsv`'s `len` column reads 65536/262144/1048576/65536×4 exactly) |
| the decode-gate `--check` control | `_check_decode_gate_has_teeth()` in both `gen_subjects.py` and `gen_throughput_subjects.py` | builds a real multi-byte fixture that deliberately ENDS on a 3-byte CJK character (never on `text()`'s own ASCII pad, which the first draft of this control got wrong — see "What I got wrong" below), slices one byte off the end, and asserts `decode_gate` raises `UnicodeDecodeError`; both `--check` runs print "decode gate negative-arm control passed" |
| `bench/utf8/CLAUDE.md` naming what's NOT built | `bench/utf8/CLAUDE.md`, "What is NOT built here" section | states `subbench.toml` (U2/U4), `patterns.rxt`/`patterns/*.rx` (U4), `expectations.tsv` (U5), `NOTES.md` (U5), the `prp-ingreek` no-subject decision, and the two `alt-cyr-64` U4-coordination subjects, each with its own line |

## Mandate compliance

- **Untouched, as instructed:** `pcrecbench/oracle_pcre2.py`, `testees/`,
  `pcrecbench/capability.py` (U1's/U2's own scope), `store/`,
  `docs/dev/inbox_from_pcrec.md`, `docs/dev/outbox_to_pcrec.md`,
  `docs/dev/plan.md`. Confirmed by `git diff --stat master...HEAD` —
  only `bench/CLAUDE.md` (one new paragraph, the `utf8/` row's own
  "not enumerated" pointer, same shape as the existing `capability/`
  paragraph) and the fourteen new `bench/utf8/*` files.
- **Generated trees gitignored, not committed:** `bench/utf8/subjects/`
  and `bench/utf8/throughput/` are covered by the EXISTING `.gitignore`
  wildcards (`bench/*/subjects/`, `bench/*/throughput/`) — no
  `.gitignore` edit was needed or made. `git add -A -n` confirmed only
  the fourteen intended files stage.
- **~/pcrec untouched:** read nothing from it this lane (the design note
  already carries every pcrec citation this lane needed).

## The generic-gate concern, resolved by construction

`tools/selfcheck.py:185-200`'s `subbench_dirs()` — the ONE enumeration
`make check-harness`'s generator/manifest/expectation/floor-pattern gates
walk — checks `os.path.exists(os.path.join(path, "subbench.toml"))` per
directory. `bench/utf8/` carries no `subbench.toml` (U4's own
deliverable, per the build plan), so it is invisible to that enumeration
today — structurally, not by a special case added to the check. I
verified there is no SECOND, ungated enumeration that would catch it
anyway: grepped every `.py` file under the repo that both mentions
`bench` and calls `os.listdir`/`os.walk`/`glob(` (21 hits — mostly
per-set `gen_patterns.py` files and one-off measurement probes) and read
each generic harness/reporter/interpreter entry point
(`tools/selfcheck.py`, `catalogue/check_interpret.py`, `pcrecbench/
report.py`/`store.py`/`subbench.py`/`adapters.py`); none discovers
sub-benches by directory walk outside `subbench_dirs()`. `make
check-schema` and `make check-report` don't touch `bench/` at all (the
former validates `schema/examples/`, the latter runs against
`pcrecbench/tests/fixtures/store`, confirmed by reading `Makefile`'s own
targets). This satisfies the brief's instruction to explain rather than
weaken a gate — no gate code was touched.

`bench/utf8/CLAUDE.md` and `bench/CLAUDE.md` both state this in writing,
in the same terms `bench/capability/`'s own analogous paragraph already
established as this repo's precedent for a staged, not-yet-enumerable
set.

## Validation run (light checks only, per the brief)

```
$ python3 bench/utf8/gen_subjects.py
gen_subjects: 91 subjects (90 family + 1 floor; 692 B, 1..30) -> .../subjects, manifest -> .../manifest.tsv (decode gate negative-arm control passed)
$ python3 bench/utf8/gen_subjects.py --check
gen_subjects --check: OK (91 subjects, decode gate negative-arm control passed)

$ python3 bench/utf8/gen_throughput_subjects.py
gen_throughput_subjects: 7 text(s) (1638400 B total, ~1.56 MB) -> .../throughput, manifest -> .../manifest_throughput.tsv (decode gate negative-arm control passed)
$ python3 bench/utf8/gen_throughput_subjects.py --check
gen_throughput_subjects --check: OK (7 texts, decode gate negative-arm control passed)

$ python3 bench/utf8/gen_subject_facts.py
gen_subject_facts: 98 rows -> .../subject_facts.tsv
$ python3 bench/utf8/gen_subject_facts.py --check
gen_subject_facts --check: OK (98 rows)
```

The per-corpus lead-byte histogram MEASURES exactly what utf8_set_v1.md
4.2 predicts (read from the committed `subject_facts.tsv`):

| subject | dominant_lead | pct_multibyte | avg_bytes_per_char |
|---|---|---|---|
| `t-64k-lat` | `0xc3` | 15.76% | 1.0855 |
| `t-64k-cyr` | `0xd0` | 88.30% | 1.7928 |
| `t-64k-cjk` | `0xe3` | 92.51% | 2.6093 |
| `t-64k-asc` | `n/a` | 0.00% | 1.0000 |
| `floor-hit` | `n/a` | 0.00% | 1.0000 |

`0xc3` (Latin-1 Supplement lead), `0xd0`/Cyrillic and `0xe3`-spread/CJK
match §4.2's own worked claims exactly ("0xC3 near-universal" for `lat`,
"0xD0/0xD1" for `cyr`, "0xE3-0xE9" for `cjk`).

**`make check-harness` / `make check` were deliberately NOT run** — the
brief reserved that slot for another lane today; I ran only this lane's
own generators' `--check` modes and read the harness's enumeration code
to confirm the generic-gate claim above rather than exercising the whole
20-minute suite.

## What I got wrong the first time (worth a reader's two minutes)

The first cut of the decode-gate negative-arm control built its "good"
fixture from `utf8text.text(N, seed, "cjk")` directly and sliced its
LAST byte off. That fixture's true final byte is sometimes `text()`'s
own ASCII space pad (a well-formed 1-byte character on its own), so
dropping it left a still-well-formed string and the control silently
proved nothing — caught immediately because the assertion fired
("decode gate has no teeth"), not discovered later. Fixed in both
generators by appending one known 3-byte character (`日`) to the good
fixture before truncating, so `[:-1]` is guaranteed to land inside that
character. A check with no real failing case proves nothing — this
repo's own stated check-design lesson, and this lane tripped over it
once while building the very control meant to embody it.

## U4/U5 coordination points (also stated in `bench/utf8/CLAUDE.md`)

1. `alt-cyr64-hit` (`дом`) and `alt-cyr64-miss` (`квинтэссенция`) assume
   facts about `alt-cyr-64`'s real 64-word branch list that U4 has not
   authored yet. If U4's list disagrees, only these two subjects need a
   second look — everything else in family (d) is typed against the
   design note's own literal pattern text, which is already fixed.
2. `prp-greek-scx-witness` (`α` + U+0342 COMBINING GREEK PERISPOMENI) is
   typed to the DESIGN NOTE's own §8.5 recommendation (avoid U+00B7,
   the confirmed version-sensitive point; use U+0342 instead) — whether
   `prp-greek`/`prp-greek-sc` actually diverge on it is left to U5's
   oracle derivation, as utf8_set_v1.md itself says it must be.
3. `prp-ingreek` carries no subject at all (a REFUSAL witness on every
   engine, no match rows) — this is a deliberate zero, not an omission;
   stated in `bench/utf8/CLAUDE.md`.

## Outstanding / owed

Nothing owed from this lane. Every deliverable in the brief is committed
and its `--check` passes. U2 (roster + `effective_encoding()`), U4
(patterns + sidecar) and U5 (expectations + `NOTES.md`) are the next
rows in the build plan and are out of this lane's scope.
