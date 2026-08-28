# bench/loglines/ — the log-line search sub-bench (`loglines@0.1`)

WHAT IT IS FOR. The mostly-FAILING regime: what an engine pays to establish
that a chunk of log lines does NOT contain what an operator is grepping for.
It is the row inbox I-7 §1 asked for and the measurement pcrec's **[OPT-5]**
(a general required-byte precheck for its DFA) is BUILT OR NOT on — so the set
is shaped around one axis: whether PCRE2's required-code-unit dismissal is
available for a pattern, and three of the eleven patterns are the control
where it is not available at all.

**Read `NOTES.md` first** — the objective, the required-literal table, the
m/n per pattern, why the `match` regime is not declared, the size sweep and
its three flavours, the floor pattern, and the cell-time estimate.

WHERE IT CAME FROM. Nothing is copied. The patterns are authored from the
GOAL by an author blinded to pcrec's `tests/`, `src/` and corpora ([B11.1]'s
brief, pcrec's D27 discipline): only pcrec's `docs/spec/` was read, for the
module roster and the `--features` gate. The subjects are generated here.

| file | role |
|---|---|
| `subbench.toml` | the SIDECAR: fields only, no grammar ([DD-13] untouched). Declares `search_short` + `throughput` (NOT `match`) and `short_search_max_bytes = 4096` |
| `patterns/*.rx` | the ten members + `floor.rx`, raw bytes, no trailing newline. Every group is `(?:…)`: no capture participates anywhere |
| `logtext.py` | the log-line GRAMMAR both generators draw from: the near-miss background, the ten shape injections, the single-source syslog stream, and `smallest_period()` (the `periodic` column's definition) |
| `gen_subjects.py` | writes `subjects/` (gitignored) + `manifest.tsv`; 112 chunks, 279–3772 B, seed 20260828. Match counts are ALLOCATED exactly, not drawn per subject |
| `gen_throughput_subjects.py` | writes `throughput/` (gitignored) + `manifest_throughput.tsv`; 16 KB/64 KB/256 KB/1 MB × `fail` / `syslog` / `hit`, seed 20260829 |
| `manifest.tsv`, `manifest_throughput.tsv` | committed: id, len, sha256, description, **periodic** (inbox I-10; `no` on all 124) |
| `gen_expectations.py` | the entry point; the derivation is shared (`pcrecbench/expectations.py`). `--check` re-derives and diffs |
| `expectations.tsv` | 1364 rows: 11 patterns × 124 subjects × the declared regime for each |
| `gen_pattern_facts.py` | derives `pattern_facts.tsv` from PCRE2's own start-of-match analysis (`pcre2_pattern_info`) |
| `pattern_facts.tsv` | per pattern: first code unit, **required code unit or NONE**, min length, how many subjects contain that byte, m/n, and which large subjects do NOT contain it |
| `NOTES.md` | the objective, the tables, the engine notes, the cell-time estimate |

REGENERATING. `python3 bench/loglines/gen_subjects.py`,
`gen_throughput_subjects.py`, `gen_expectations.py`, `gen_pattern_facts.py`.
All four are deterministic; `make check` runs the first two and re-derives the
last two in `--check` mode, over every sub-bench under `bench/` by
enumeration (`tools/selfcheck.py:subbench_dirs`), and fails on any drift.

TWO THINGS A FUTURE EDITOR SHOULD NOT UNDO WITHOUT READING WHY (both in
`NOTES.md`, both MEASURED):

1. `logtext._shortid` forces one `a`–`f` into every 12-hex id. An all-digit
   12-hex id is a 12-digit number that `bignum` matches; unconstrained it
   happens once in ~290 ids, which is ~35 accidental matches in a 1 MB subject
   whose entire value is that no member pattern matches it.
2. The `t-<size>-syslog` flavour is the only one where a required-byte
   precheck can fire on a large subject. On MIXED log text every required unit
   in this set is structural, so `-fail` alone measures "both engines scan"
   and could not produce the comparison this sub-bench was opened for.

BUMPING THE VERSION is a deliberate, logged event (requirements §5): any
change to a pattern, a subject, or an expectation makes existing records
incomparable, so `version` in `subbench.toml` goes up in the same commit and
the reason goes in the journal. Note that a change to `logtext.py` changes
BOTH subject trees.
