# The record schema — [B2]

STATUS: DRAFT 1, 2026-08-25. Written against
`docs/design/requirements.md` ADOPTED v3 and the R1 panel's findings
(`docs/dev/reviews/2026-08-24-r1-requirements.md`). Every field below
cites the requirements section or the R1 finding that put it there; a
field with no citation is an ADDITION and says so.

Artifacts: `schema/record.schema.json` (JSON Schema draft 2020-12),
`schema/validate.py` (the shared validator), `schema/examples/`,
`make check-schema`.

## 1. What a record is, and what this schema is not

A RECORD is the artifact for ONE CELL measured in ONE RUN
(requirements §2): one (sub-bench version × testee) pair, on one
machine, at one timestamp. One record is one file. A record is written
once and never edited; a re-measurement is a new record (§6).

The schema covers the record ONLY. It does not describe the sub-bench
(that is the sidecar, §5 of the requirements, and [DD-13]'s territory
once it lands), and it does not describe the store or the report
(OD-B6, [B3]/[B5]). Where the record must name a sub-bench fact — a
pattern's hazard class, a subject's size — it carries a COPY for
filterability and pins the source with `subbench.content_hash`; §10.1
states that rule and its risk.

Two properties are load-bearing and are stated here once so the rest of
the document can lean on them:

- **Raw trials, not reductions.** A record carries `elapsed_ns`,
  `iterations` and `bytes_processed` per trial. It never carries MB/s,
  ns/call, a median, a spread or an `n`. Those are the reporter's
  (requirements §6: "reduction happens in the report, so the
  comparables set can change without re-measuring"; the set itself is
  OD-B1, unruled). This is a deliberate DEPARTURE from pcrec's
  `compare.sh` TSV, which emits `value` + `metric` + `spread` columns
  already reduced (`tests/bench/compare/compare.sh:1129`) — that file
  is a report, this is a record.
- **Engine-neutral.** No top-level field is pcrec-specific. pcrec's
  mechanism stamps live only inside `engine_metadata`, under a
  declaration the testee supplies like any other testee (requirements
  §4.2; R1 finding B1: a pcrec-only field contradicts APPROACH
  principle 2's "one more file in the pile"). §7 is the worked example.

## 2. File layout and naming

JSONL, UTF-8, LF line endings, one JSON object per line, no trailing
blank line required (a trailing newline on the last row is normal and
is not a line).

    line 1      the SETUP layer          {"kind":"setup", ...}
    line 2..N   the RESULT rows          {"kind":"match", ...}
                                         {"kind":"compile", ...}

`kind` discriminates. Exactly one `setup` line, and it is line 1 —
the validator rejects a second one, which is what a concatenation of
two records looks like and is the realistic way two schema versions
end up in one file (§4).

Row ORDER IN THE FILE is free; `seq` carries the order. Every result
row carries a `seq` — dense and unique 1..N over ALL result rows of the
record, in EMISSION order (rule X18). File order and emission order are
therefore separable: a reader may sort the rows however it likes, and a
tool that rewrites a file cannot silently lose which measurement
happened first. That matters for more than tidiness: a lazy JIT's
compile cost is defined as its FIRST match minus steady state (§3 of the
requirements), and "first" has to mean something the file cannot
scramble. Writing compile rows before match rows is the natural harness
order and what the examples do; nothing depends on it any more.

**File name = `record_id` + `.jsonl`, verbatim.** The record id is
built from the identity tuple (§3) with `__` between components, and
every component's own character set excludes `__`, so the name parses
back into the tuple unambiguously. A reader can therefore identify a
record from its name alone, and a name that disagrees with the file's
own `record_id` is a validator error.

## 3. Record identity and the content hash

Identity (requirements §2, R1 finding A1 — a date-granularity id
collides):

    record_id = <subbench.id> "@" <subbench.version> "__"
                <testee.testee_id> "__"
                <environment.machine_id> "__"
                <stamp> [ "-" <n> ]

`<stamp>` is `run.timestamp` (RFC 3339, UTC, seconds) with `-` and `:`
removed: `2026-08-25T03:18:00Z` → `20260825T031800Z`. The validator
derives all four components from the fields and requires equality, so
the id cannot drift from what it names.

`-<n>` is the DISAMBIGUATOR for the residual collision: two runs of the
same cell on the same machine that begin in the same second. It is
never assigned pre-emptively; the harness assigns `-2`, `-3` … only on
a name that already exists, which is pcrec `compare.sh:1211-1217`'s
never-silently-clobber rule (losing a baseline snapshot is exactly how
a regression goes unnoticed) carried over.

**Content hash** — `content_hash.value`, sha256, lowercase hex. It
covers:

1. line 1's JSON object with the member `content_hash` REMOVED,
   re-serialized canonically: `json.dumps(obj, sort_keys=True,
   separators=(",", ":"), ensure_ascii=False)`;
2. then, for each row line in file order, that line's text with
   trailing whitespace stripped;

joined with `"\n"` and encoded UTF-8. Removing `content_hash` before
hashing is what breaks the circularity of hashing a document that
contains its own hash; canonicalising line 1 only (rows are hashed as
written) keeps the rule cheap for a file with thousands of rows while
still pinning every byte that carries a number.

The hash is a TAMPER/TRUNCATION check, not a de-duplication key: two
records of the same cell differ in their timestamps and therefore in
their ids regardless of hash. `schema/examples/bad/x6-tampered-hash.jsonl`
is the positive control.

## 4. Schema version, mixing, migration

`schema_version` is `MAJOR.MINOR`, on the setup line only. Rows carry
no version — they cannot mix within a file by construction, and a row
that repeated it would be 2-6 thousand copies of one fact (requirements
§6's own size estimate).

- **MINOR bump** — purely additive: a new OPTIONAL field, a new ENUM
  VALUE, a new declared `engine_metadata` name. A reader on an older
  minor MUST accept the file, and MUST treat an enum value it does not
  know as *un-filterable on that field*, never as a reason to drop the
  row. Growing any enum in §5 is a minor bump and requires a line in
  this note saying why.
- **MAJOR bump** — anything else: a removed or renamed field, a
  narrowed type, a changed meaning, a removed enum value.

**Mixing policy** (R1 finding A10). The reporter refuses to reduce
records of different schema versions into one cell unless a declared
migration exists. Concretely, and enforced by `validate.py`:

- WITHIN a file: impossible; a second setup line is an error.
- ACROSS files handed to one invocation: differing MAJOR versions are
  an error (`--allow-mixed-versions` to override, for the migration
  author). Differing MINORs are accepted — that is what "additive"
  buys.
- A MIGRATION is a documented, reviewed entry in this note naming the
  two versions and the rewrite. Absent one, a major-version boundary is
  a hard stop, not a warning.

### 4.1 Version history

| version | date | what |
|---|---|---|
| 1.0 | 2026-08-25 | draft 1, merged |
| 1.1 | 2026-08-25 | the post-merge panel's twelve findings (§11) |

**1.0 → 1.1 is a MINOR bump under a stated, one-time exception, and by
the rule above it should be a MAJOR one.** 1.1 adds REQUIRED fields
(`seq`, `run.clock_source`, `run.driver_build_flags`,
`run.driver_compiler`, `subjects[].sha256`, the new `load`/`occupancy`
sample shapes, `calibration` when `iterations` > 1), narrows one
(`testee.engine_commit` from 7-40 hex to 40), renames one enum value
(the lazy-JIT `derivation` const) and REMOVES one field
(`quiet_attestation`). Every one of those is a major change by §4's own
definition, and the definition is not being softened.

The exception is that MINOR exists to protect a POPULATION — readers on
an older minor that must keep accepting files — and on 2026-08-25 that
population is empty. No record has been written to any store: 1.0 was
merged the same day and the harness lane is writing its first records
against 1.1. A major bump would announce a migration for zero records
and would spend the 2.0 boundary, which is worth keeping for the first
change that breaks a record someone has actually measured.

The exception is one-time and expires the moment the first record is
stored. After that, §4's table is the whole rule and a change of this
shape is 2.0 with a migration entry beside it.

One consequence is load-bearing: a 1.0-stamped file is NOT readable as
1.1 (it will lack required fields), even though the minor-version rule
says a reader must accept it. That contradiction is real, it is a
property of this exception rather than of the schema, and it is
harmless only because no such file exists. `validate.py` still accepts
an older MINOR — `schema/examples/bad/x10-cost-class-mismatch.jsonl` is
stamped `1.0` while carrying 1.1's fields, deliberately, so that branch
has a live example and nobody "fixes" the minor comparison into
strictness.

## 5. The fixed enums (OD-B4 (a))

**Token spelling rule.** Every enum token is lowercase, ASCII, words
separated by `-`. This is the ONE transformation applied to the
requirements' spellings, so that a filter expression never has to guess
casing. The mapping is 1:1 and total:

There is exactly one exception, and it is deliberate:
`pinning.mode = chrt+taskset`. The `+` is doing work a `-` cannot — the
token names a COMPOSITION of two tools (a real-time scheduling class AND
a CPU mask), where `chrt-taskset` would read as the name of one tool.
An exception admitted once, in writing, is cheaper than a rule everyone
quietly stops believing.

| requirements §4.3/§4.4/§3/§6 spelling | token |
|---|---|
| interpretive / compiled-AOT / eager-JIT / lazy-JIT | `interpretive` `compiled-aot` `eager-jit` `lazy-jit` |
| DFA-only / NFA-simulation / backtracking / hybrid / SIMD-multipattern | `dfa-only` `nfa-simulation` `backtracking` `hybrid` `simd-multipattern` |
| open-source / closed | `open-source` `closed` |
| Perl leftmost-first / POSIX leftmost-longest / all-ends | `perl-leftmost-first` `posix-leftmost-longest` `all-ends` |
| Large-subject throughput / Short-subject search / Match (compliance) | `large-subject-throughput` `short-subject-search` `match-compliance` |

The enums, in full:

| enum | values | source |
|---|---|---|
| `execution_model`, and `cost_class` | `interpretive` `compiled-aot` `eager-jit` `lazy-jit` | §4.3 |
| `automaton_class` | `dfa-only` `nfa-simulation` `backtracking` `hybrid` `simd-multipattern` | §4.3 |
| `openness` | `open-source` `closed` | §4.3 |
| `conventions[]` | `perl-leftmost-first` `posix-leftmost-longest` `all-ends` | §4.3 |
| `captures` | `on` `off` | §4.3 |
| `simd` | `on` `off` `n-a` | §4.3 |
| `regime` | `large-subject-throughput` `short-subject-search` `match-compliance` | §3 |
| `status` | `measured` `harness-failure` `inconclusive-load` | §6 |
| `compile_outcome` | `compiled` `did-not-compile` `crashed` `timed-out` `unsupported-by-declaration` | §4.4 |
| `match_outcome` | `matched-as-expected` `did-not-match-as-expected` `wrong-span-or-captures` `truncated-subject` + `crashed` `timed-out` | §4.4 + ADDITION |
| `truncation_check` | `verified` `unverified-for-truncation` `not-applicable` | §4.4 + ADDITION |
| `variant.kind` | `syntax-only` `restructured` | §4.5 (OD-B5: informational) |
| `occupancy.verdict` | `pass` `fail` `unavailable` | §9(b) |
| `load.verdict` | `quiet` `loaded` | §9(a), naming the existing gate |
| `pinning.mode` | `taskset` `chrt+taskset` `none` `unavailable` | §9(d) |
| `clock_source` | `clock_monotonic` `clock_monotonic_raw` `other` | ADDITION (§9(e)) |
| `hazard_class` | `none` `exponential-backtracking` `ambiguous-decomposition` `exact-minimum-boundary` `large-count` `wide-alternation` | §5 list + APPROACH §3 |
| `size_class` | `tiny` `small` `medium` `large` `huge` | APPROACH §3 |
| `role` (subject) | `single` `set` | §6 ("subject-or-subject-set") |
| `capture_correspondence.mode` | `identical` `by-name` `by-index-map` `not-applicable` | §4.5, R1 finding B2 |
| `engine_metadata_declaration.*.type` | `enum` `integer` `string` `mask` | ADDITION (§7) |
| `engine_metadata_declaration.*.scope` | `pattern` `match` | ADDITION (§7) |

### ADDITIONS to an enum, and why

1. **`match_outcome` gains `crashed` and `timed-out`.** §4.4 spells
   these in the per-(pattern, testee) set but not the per-(pattern,
   subject) set — yet catastrophic backtracking is a HEADLINE hazard
   class of this bench (§5, APPROACH §2.1), and it is by definition a
   per-SUBJECT hang: the pattern compiled, 84 subjects answered, one
   ran past the timeout. With no such value the harness would have to
   lie (`did-not-match-as-expected` is a wrong answer, not a hang) or
   drop the row (silently deleting the most interesting datum in the
   bench). The two tokens are re-used verbatim from the sibling set
   rather than invented. **ACCEPTED at the [B2] merge (2026-08-25): requirements.md §4.4 is amended to carry `crashed`/`timed-out` per subject; see §11.1 (closed).**
2. **`truncation_check` gains `not-applicable`.** §4.4 gives
   `unverified-for-truncation` for a large-subject cell whose API does
   not expose the consumed length; the third state is a cell where the
   question does not arise (a match-compliance row over a 40-byte
   subject). Folding it into `unverified-for-truncation` would inflate
   the count of a flag that exists to be alarming.
3. **`hazard_class` / `size_class` are enumerated at all.** The
   requirements name these as sub-bench TAGS without fixing a
   vocabulary. They are filterable, and "filterable = enumerated or
   normalized", so a vocabulary had to be chosen; the values are §5's
   own hazard-family list. Growing either is a MINOR bump (§4).
4. **`load.verdict`, `pinning.mode`, `role`, and the two
   `engine_metadata_declaration` enums** are new names for facts §9,
   §6 and §4.2 require to be recorded but do not name.

`engine_mode` is deliberately NOT a fixed enum: §4.3 gives its values
as "auto/dfa/vm/... per engine", which is per-engine by construction. It
is a NORMALIZED IDENTIFIER with a per-engine registry (§6.3).

## 6. Normalization rules for the open identifiers (OD-B4 (b))

R1 finding A11 split these from the fixed enums: they are open sets, so
what is pinned is the RULE that produces the string, not the list.

**A rule stated only in prose is a rule nobody runs.** Three of the
rules below are MECHANICAL and are therefore CODE: `normalize_cpu_model`,
`normalize_kernel` and `normalize_compiler` in `validate.py`, checked
against their `_raw` siblings by rule X23. The rest are not mechanical
and say so explicitly:

| identifier | status |
|---|---|
| `cpu_model` | DERIVED from `cpu_model_raw`, checked (X23) |
| `kernel` | DERIVED from `kernel_raw`, checked (X23) |
| `compiler` | DERIVED from `compiler_raw`, checked (X23) |
| `machine_id` | ASSERTED — an assignment, not a derivation (§6.5); deliberately not derivable |
| `engine_name` | ASSERTED against a registry (§6.1); the source is a project's own name, which no function on this box can see |
| `engine_mode` | ASSERTED against a per-engine registry (§6.3) |
| `testee_id`, `record_id` | DERIVED from other RECORD fields, checked (X5, X3) — a different thing from normalizing an external string |

The `_raw` siblings are OPTIONAL, so X23 checks a field only when its
raw is present. That is the honest shape: the rule relates two things,
and with one of them missing there is nothing to check — but a harness
that omits the raw string has also given up the only evidence that its
normalized value was right.

### 6.1 `engine_name`

Lowercase ASCII, `[a-z0-9]([a-z0-9-]*[a-z0-9])?`. It names the ENGINE
only — never a version, never a configuration, never a binding
language. Registry (this note is the registry; adding a row is a minor
bump): `pcrec`, `libpcre2`, `re2`, `rust-regex`, `oniguruma`, `tre`,
`vectorscan`, `python-re`, `perl`. Rule for a new one: the project's
own name, lowercased, non-alphanumerics to `-`, a language binding
suffixed to the engine (`python-re`, not `re`).

### 6.2 `engine_version` and `engine_commit`

`engine_version` is the engine's own release string with a leading `v`
stripped and everything lowercased (`10.46`, `1.11.0`, `2024.08.1`).
Where the testee is pinned to a VCS revision rather than a release —
which is pcrec ALWAYS (requirements §4.2: "each just another roster
entry with its pcrec commit pinned") — `engine_commit` carries the full
40-hex commit and `engine_version` carries a `git describe`-shaped
string. The binding rule: **`engine_version` must be reproducible from
`engine_commit`**; where it is not, the version is not a version and
the testee is not pinned.

That rule is now CHECKED, which required naming what a release looks
like. **RELEASE-TAG SHAPE** is `^\d+\.\d+(\.\d+)?$`, optionally with a
single trailing letter revision (`8.45a`): `10.46`, `1.11.0`, `13.4.0`.
Anything else — a `git describe` string (`0.9.0-g1a2b3c4`), an `-rc1`,
a `+build` suffix — is NOT a release, and rule X22 then requires
`engine_commit` to carry the full 40-hex commit. The conservative call
is deliberate: a pre-release is exactly the kind of build that is worth
pinning, so making `1.0-rc1` require its commit costs an adapter one
field and buys a testee that can be rebuilt.

### 6.3 `engine_mode`

Lowercase slug, per-engine registry:

| engine | `engine_mode` values |
|---|---|
| `pcrec` | `auto`, `dfa`, `vm` (pcrec's `--engine=`; `lib/pcrec.h` `PCREC_ENGINE_AUTO/_DFA/_VM`) |
| `libpcre2` | `interp`, `jit` |
| others | declared when the adapter lands |

### 6.4 `testee_id`

A testee is an (engine, version, build/run configuration) TRIPLE
(requirements §2), so its id must carry all three or two records of
different pcrec commits would share an id. It is CONSTRUCTED, not
chosen:

    testee_id = <engine_name> "_" <version_slug> "_" <config_slug>
                              [ "_" <config_extra> ]

    version_slug = engine_version, every character outside [a-z0-9.]
                   replaced by "-"
    config_slug  = <engine_mode> "-" <caps> "-" <simd>
                   caps = "caps" if captures==on else "nocaps"
                   simd = "simd" | "nosimd" | "simdna"   (on | off | n-a)

Examples: `pcrec_0.9.0-g1a2b3c4_vm-caps-simdna`,
`libpcre2_10.46_jit-caps-simdna`.

`config_extra` is the escape hatch for two testees that differ ONLY in
`build_flags` (which is never filtered — §8): an author-chosen slug,
appended. The validator DERIVES the whole id from the fields and
requires equality — the id can never claim a configuration the record
does not carry.

### 6.5 `machine_id` (the hardware id)

A hand-assigned, stable slug per physical box (`[a-z0-9][a-z0-9-]{0,31}`),
recorded in the store's machine registry when [B3] creates it, never
reused for a different box. Deliberately NOT derived: a hash of
`/proc/cpuinfo` or DMI would change under a microcode or firmware
update and silently split one machine's history in two, and the
hostname is not stable either (containers share one, boxes get
renamed). `hostname`, `cpu_model_raw` and `kernel_raw` travel alongside
as the evidence that an assignment was right.

### 6.6 `cpu_model`

From `/proc/cpuinfo`'s `model name`, canonicalised, in this order:

1. delete `(R)`, `(TM)`, `(tm)`, `(r)`;
2. delete a trailing `@ <freq>`;
3. lowercase;
4. collapse every run of non-alphanumerics to a single `-`;
5. strip leading and trailing `-`.

E.g. `Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz` →
`intel-core-i7-9750h-cpu`. `cpu_model_raw` keeps the original string
verbatim (reproducibility) and X23 checks the derivation against it.

### 6.7 `kernel` and `compiler`

`kernel` = `uname -s` and `uname -r`, lowercased, joined by `-`:
`linux-7.0.0-29-generic`. Mechanically: strip the raw string, replace
every whitespace run with `-`, lowercase.

`compiler` = the FIRST line of `$CC --version` reduced to
`<name>-<version>`: `gcc-15.2.0`. Mechanically: the NAME is the first
whitespace-separated token, lowercased with non-alphanumeric runs
collapsed to `-`; the VERSION is the LAST token of that line which is a
bare dotted number, after stripping surrounding `(`, `)` and `,`. That
last clause is the whole rule: `gcc (Ubuntu 15.2.0-4ubuntu4) 15.2.0`
has two version-looking tokens and only one of them is the compiler's
version — a distribution's build string is not a version, and it is
excluded by being not-a-bare-dotted-number rather than by a
distribution-specific special case. `clang version 20.1.0 (…)` →
`clang-20.1.0`; `rustc 1.79.0 (129f3b996 2024-06-10)` → `rustc-1.79.0`.
If the line has no bare dotted number, the rule yields the name alone —
that is a finding about the rule, not an escape hatch, and it is
visible because X23 will then reject a record that carries anything
else. Raw strings in `kernel_raw` / `compiler_raw`.

`compiler` is an ENVIRONMENT dimension — the C toolchain of the box,
which is what an AOT testee such as pcrec actually pays and what
`compare.sh`'s machine-context table records. A testee whose engine is
built by a different toolchain (rustc, cargo, a Python interpreter)
records that toolchain in `testee.build_flags` and its version in
`engine_version`. **Flagged for the panel (§11.4)** — one `compiler`
field may be the wrong shape once a non-C testee lands.

## 7. `engine_metadata`: the per-testee declaration

Requirements §4.2 asks for a generic map of ENUMERATED (name, value)
pairs, populated from STRUCTURED fields, so reports can "bucket
outliers by MECHANISM, not by pattern shape". Three rules make that
real:

1. **Declare before use.** `testee.engine_metadata_declaration` is a
   map `name → {type, scope, values?, bits?, source, description}`.
   A pair on a row whose name is not declared is a validator error;
   so is a value of the wrong type, an `enum` value outside `values`,
   or a `mask` bit outside `bits`. An undeclared pair is free text with
   extra steps, and free text is not filterable.
2. **Scope.** `pattern`-scoped pairs live on the COMPILE row (which is
   keyed by pattern, and is where the fact is produced); `match`-scoped
   pairs live on MATCH rows. Requirements §6 lists `engine_metadata` on
   the match row and §4.2 calls the pairs per-pattern; both are honoured
   by scoping, and it avoids stamping 440 identical copies of one fact
   onto a realistic cell's match rows.
3. **A `mask` value is an ARRAY OF BIT NAMES, never the integer.**
   `0x13` is not filterable without pcrec's bit table, and the reporter
   must not need one. The declaration lists the bit names; the row
   carries the subset that was set.

**Worked example — pcrec.** Every source below is a STRUCTURED field of
the artifact (requirements §4.2's requirement); the prose
`<PREFIX>_ENGINE_WHY` is explicitly NOT a metadata pair — it goes in the
row's `diagnostic`, unindexed.

| name | type | scope | source in the pcrec artifact |
|---|---|---|---|
| `engine` | enum `dfa`,`vm` | pattern | `rx_info.engine` (`PCREC_ENGINE_DFA`=1 / `PCREC_ENGINE_VM`=2, emitted in every artifact's `PCREC_RX_ABI_H` block — `~/pcrec/src/gen/emit_dfa.c:462-497`) |
| `abi` | integer | pattern | `rx_info.abi` (2 today) |
| `ncaps` | integer | pattern | `rx_info.ncaps` |
| `ngroups` | integer | pattern | `rx_info.ngroups` |
| `step_budget` | integer | pattern | `rx_info.step_budget` (-1 = none) |
| `work_budget` | integer | pattern | `rx_info.work_budget` (-1 = none) |
| `prefilter` | enum `hybrid`,`none` | pattern | `<PREFIX>_VM_PREFILTER` (`~/pcrec/src/gen/emit_vm.c`, the [M4.6f] stamp) |
| `vm_rungs` | mask | pattern | `<PREFIX>_VM_RUNGS`, bits `PCREC_VM_RUNG_CURSOR`, `_FRAMES_BOUNDED`, `_FRAMES_UNBOUNDED`, `_REVDET`, `_COUNTER` (D46/[ABI-NS] D60) |
| `vm_strats` | mask | pattern | `<PREFIX>_VM_STRATS`, bits `PCREC_VM_STRAT_POSSESSIVE`, `_BACKTRACKING` |
| `vm_prunes` | mask | pattern | `<PREFIX>_VM_PRUNES`, bits `PCREC_VM_PRUNE_CLAMPED`, `_UNCLAMPED` |
| `root_minw_unbounded` | enum `yes`,`no` | pattern | presence of `<PREFIX>_VM_ROOT_MINW` at the analysis ceiling ([DD-14.EMPTY]) |

Two notes an adapter author must not lose:

- The `VM_*` stamps are emitted on VM artifacts ONLY (a DFA artifact
  has no separate prefilter/rung/strategy decision, and emitting them
  would break pcrec's own byte-identity gate). A DFA-engine pcrec
  testee therefore declares only the `rx_info`-sourced pairs. An
  ABSENT pair is not an error; an UNDECLARED one is.
- `rx_info` is a `.rodata` symbol, readable by linking against the
  artifact; the `<PREFIX>_*` stamps are preprocessor-visible at compile
  time. The adapter may read either, and must record which in the
  declaration's `source`.

Other testees populate the same map from their own structured facts —
RE2's program size, Vectorscan's bytecode size (requirements §4.2) —
with their own declarations. Nothing about the mechanism is pcrec's.

## 8. The fields

`req` column: **R** required, **o** optional, **c** conditionally
required (the condition is in the rule column and is enforced by the
schema or by `validate.py`).

That last clause was a CLAIM, not a fact, until v1.1: five of the `c`
rows were enforced in one direction or not at all. A record could
report `compiled` on an AOT compile row and carry no `cost` — the
compile axis silently empty for that pattern; could omit
`truncation_check` on a large-subject row, so requirements §4.4's
"marked `unverified-for-truncation`" marked nothing; could declare
`capture_correspondence.mode = by-index-map` with no map; could call a
subject `single` and claim four of them, making the reporter's
per-subject arithmetic wrong by 4×; and could carry an occupancy
verdict of `pass` with `max_busy_pct: null`, a judgement with nothing
behind it. All five are `if`/`then` branches in the schema now, each
with a control. `check_fields.py` cannot catch this class — it compares
field NAMES, and requiredness is not a name. Path spelling: `a.b` a nested member,
`a[].b` a member of an array element. `check_fields.py` diffs these
tables against `record.schema.json` on every `make check-schema`, so a
row here that is not in the schema (or the reverse) is a build failure,
not a review miss.

FILTERABLE means the reporter (§8 of the requirements) may filter or
group on it. DIAGNOSTIC / REPRODUCIBILITY-ONLY fields are free text and
the reporter must NOT offer them as filters — the R1 A4 finding in
reverse: what is filtered must be enumerated or normalized.

### FIELD TABLE: setup

#### Identity, version, status

| field | type | req | rule / enum | why |
|---|---|---|---|---|
| `kind` | const `"setup"` | R | line 1 only, exactly once | §2 the two-layer record; the discriminator |
| `schema_version` | string `M.m` | R | §4 | §6 "schema-versioned"; A10 |
| `record_id` | string | R | derived, §3 | §2 record identity; A1 |
| `content_hash` | object | R | §3 | §2 "plus a content hash" |
| `content_hash.algorithm` | const `"sha256"` | R | — | names the algorithm so a later one is a schema change, not a guess |
| `content_hash.value` | hex64 | R | §3's covering rule | as above |
| `status` | enum | R | `measured`/`harness-failure`/`inconclusive-load` | §6; pcrec D14's clean-vs-not-measured distinction |
| `status_detail` | string | o | DIAGNOSTIC | what failed, for a non-`measured` record |
| `synthetic` | boolean | o | default `false`; FILTERABLE | ADDITION: an example or a schema test must be unmistakable as a non-measurement, and prose in `note` is not machine-checkable. The reporter excludes `synthetic` records from every query |
| `note` | string | o | DIAGNOSTIC | §6 leaves room for a human sentence; the examples use it to say they are illustrative |

#### `run` — the invocation

| field | type | req | rule / enum | why |
|---|---|---|---|---|
| `run` | object | R | — | §2: a run is one harness invocation that may produce several records |
| `run.run_id` | slug | R | FILTERABLE; shared by every record of one invocation | A2: "run" was undefined; this is what makes the sibling records of one run findable |
| `run.timestamp` | RFC 3339 UTC `Z` | R | seconds granularity; FILTERABLE (date ranges, §8) | §2 identity; A1 |
| `run.harness_version` | string | R | FILTERABLE | §6 "the harness's own version" |
| `run.harness_commit` | 40-hex or `unknown` | R | FILTERABLE | as above; the version alone does not pin a working tree |
| `run.command_line` | array of string | R | REPRODUCIBILITY-ONLY | §6 "command lines and flags as run" |
| `run.clock_source` | enum | R | `clock_monotonic`/`clock_monotonic_raw`/`other`; FILTERABLE | ADDITION: §9(e)'s batched in-process loop is timed by SOME clock, and `_RAW` (no NTP slew) and `_COARSE`-class clocks do not produce the same nanoseconds. Two records timed by different clocks are not comparable, and nothing else in the record says which was used |
| `run.driver_build_flags` | string | R | REPRODUCIBILITY-ONLY — never filtered; `not-compiled` when the driver needs no compiler | ADDITION: `testee.build_flags` records how the ENGINE was built. The timing DRIVER is the other half of every number — `-O0` around a loop measures the loop, and `harness_contract.md` §3 requires both drivers to follow one protocol precisely so their numbers compare. The protocol is nothing without the command line that realized it |
| `run.driver_compiler` | string | R | §6.7's normalization, or `n-a` when `driver_build_flags` is `not-compiled` | ADDITION: as above, and separate from `environment.compiler` — the box's toolchain and the toolchain that built THIS driver are the same today and will not be once a testee arrives with its own |
| `run.env` | map string→string | o | REPRODUCIBILITY-ONLY | the env overrides that changed the run (`BENCH_TRIALS`, `CC`, …) |

#### `subbench` — what was measured

| field | type | req | rule / enum | why |
|---|---|---|---|---|
| `subbench` | object | R | — | §2, §5 |
| `subbench.id` | slug | R | FILTERABLE | §2 identity; §8 "results for sub-bench A1" |
| `subbench.version` | version string | R | FILTERABLE | §5 "records compare only within the same sub-bench version" |
| `subbench.content_hash` | hex64 | R | sha256 over the sub-bench directory, rule owned by [B3] | §5 versioning is a frozen snapshot; the hash is what proves the snapshot was not edited under a stale version |
| `subbench.objective` | string | R | DIAGNOSTIC | §4.5 constraint 2: "the objective is a declared field of the sub-bench"; copied so a record can be read alone |
| `subbench.regimes` | array of enum | R | FILTERABLE; every match row's `regime` must be in it | §3 "a sub-bench declares which it exercises" |
| `subbench.source_ref` | string | o | DIAGNOSTIC | where the sub-bench came from (e.g. the email specimen's path in pcrec) |

#### `testee` — who was measured (§4.3 in full)

| field | type | req | rule / enum | why |
|---|---|---|---|---|
| `testee` | object | R | — | §2, §4 |
| `testee.testee_id` | string | R | DERIVED, §6.4; FILTERABLE | §2 identity; the triple must be in the id |
| `testee.engine_name` | slug | R | §6.1; FILTERABLE | OD-B4(b) |
| `testee.engine_version` | version string | R | §6.2; FILTERABLE | OD-B4(b); §2 the triple |
| `testee.engine_commit` | 40 hex or null | c | REQUIRED when `engine_version` is not a release-tag shape (X22); FILTERABLE | §4.2 "each just another roster entry with its pcrec commit pinned". Full 40 hex only: a 7-hex prefix is a convenience for humans and an ambiguity for a pin |
| `testee.execution_model` | enum | R | FILTERABLE | §4.3 fixed enum; §3 selects the compile-cost protocol from it |
| `testee.automaton_class` | enum | R | FILTERABLE | §4.3 fixed enum |
| `testee.openness` | enum | R | FILTERABLE | §4.3; §8's worked query is "only open-source" |
| `testee.license_id` | string | R | SPDX id, or `proprietary`/`unknown`; FILTERABLE | §4.3 "openness + license id" |
| `testee.conventions` | array of enum | R | the conventions this testee CAN produce | §4.3; §7 "testees are scored against their own" |
| `testee.captures` | enum `on`/`off` | R | FILTERABLE | §4.3 headline axis; A4 |
| `testee.engine_mode` | slug | R | §6.3 registry; FILTERABLE | §4.3 headline axis; A4 |
| `testee.simd` | enum `on`/`off`/`n-a` | R | FILTERABLE | §4.3 headline axis; A4 |
| `testee.config_extra` | slug | o | appended to `testee_id`, §6.4 | the escape hatch for two testees differing only in unfiltered build flags |
| `testee.build_flags` | string | o | REPRODUCIBILITY-ONLY — never filtered | §4.3 "a residual `build_flags` blob kept for reproducibility ONLY" |
| `testee.runtime_options` | array of `{name,value}` | o | the engine's OWN option names | §4.3's last paragraph: the runtime compile options, distinct from build flags — "the thing that makes two engines diverge on byte-identical pattern text" (A8) |
| `testee.runtime_options[].name` | string | R | — | as above |
| `testee.runtime_options[].value` | string/int/bool | R | — | as above |
| `testee.compile_cost_definition` | string | R | DIAGNOSTIC | §3: the compile-cost definition "is per execution-model class, stated in the testee's adapter note" — carried in the record so a number is never read without its definition |
| `testee.compile_phases` | array of slug | R | the declared phase names, in order; a compile row's `cost.phases` must match exactly | §3 AOT: "all phases, each timed". Empty array for a class with no phase breakdown |
| `testee.warmup_trials` | integer ≥0 | R | leading trials per (pattern, subject) that are warm-up; `lazy-jit` ⇒ ≥1 | §3 "trial 1 is EXCLUDED from match statistics" (A6). RECORDED, not applied: the record keeps every raw trial and the reporter drops them |
| `testee.engine_metadata_declaration` | map name→decl | R | §7; may be empty `{}` | §4.2; A3/B1 |

#### `environment` (§6, §9)

| field | type | req | rule / enum | why |
|---|---|---|---|---|
| `environment` | object | R | — | §6 layer 1 |
| `environment.machine_id` | slug | R | §6.5; FILTERABLE | §2 identity; §9 "records from other machines are first-class" |
| `environment.hostname` | string | o | DIAGNOSTIC | evidence behind the `machine_id` assignment |
| `environment.cpu_model` | slug | R | §6.6; FILTERABLE | §4.3 normalized identifier; A11 |
| `environment.cpu_model_raw` | string | o | REPRODUCIBILITY-ONLY | the un-canonicalised `/proc/cpuinfo` line |
| `environment.cpu_mhz` | number >0 | o | `/proc/cpuinfo` `cpu MHz` at RUN START | ADDITION: `governor` and `turbo` record the frequency POLICY; this records what the clock was actually doing when the run began. A thermally-throttled box under a `performance` governor looks identical in the policy fields and is not the same machine |
| `environment.cores` | integer ≥1 | R | FILTERABLE | the load threshold is a function of it (`compare.sh`'s `max(2.0, cores/2)`) |
| `environment.kernel` | string | R | §6.7; FILTERABLE | §4.3 |
| `environment.kernel_raw` | string | o | REPRODUCIBILITY-ONLY | as above |
| `environment.compiler` | string | R | §6.7; FILTERABLE | §4.3; what an AOT testee pays |
| `environment.compiler_raw` | string | o | REPRODUCIBILITY-ONLY | as above |
| `environment.load` | object | R | — | §9(a) |
| `environment.load.before` | object | R | the `/proc/loadavg` sample taken BEFORE the run, with its evidence | §9(a); C7 |
| `environment.load.before.loadavg_raw` | string | R | the `/proc/loadavg` line VERBATIM | ADDITION: three bare numbers are an assertion. The line they were read from is the evidence, and X19 checks the parse against it — the check pcrec's own history says to write, because a number and its source in one hand-maintained place drift |
| `environment.load.before.sampled_at` | RFC 3339 UTC `Z` | R | when the sample was taken | ADDITION: "before" and "after" are claims about time; without stamps a record cannot show the two samples bracket the run rather than following each other by a millisecond |
| `environment.load.before.load1` | number ≥0 | R | parsed from `loadavg_raw` (X19); the number the verdict is judged on | §9(a) |
| `environment.load.before.load5` | number ≥0 | R | parsed from `loadavg_raw` (X19) | §9(a) |
| `environment.load.before.load15` | number ≥0 | R | parsed from `loadavg_raw` (X19) | §9(a) |
| `environment.load.after` | object | R | same shape, AFTER | §9(a): "a box that was quiet at the start but got busy partway through is just as load-compromised" (C7) |
| `environment.load.after.loadavg_raw` | string | R | as above | as above |
| `environment.load.after.sampled_at` | RFC 3339 UTC `Z` | R | as above | as above |
| `environment.load.after.load1` | number ≥0 | R | as above | as above |
| `environment.load.after.load5` | number ≥0 | R | as above | as above |
| `environment.load.after.load15` | number ≥0 | R | as above | as above |
| `environment.load.limit` | number >0 | R | the threshold THIS run used | OD-B8 is unruled — the number is data, not a schema constant |
| `environment.load.verdict` | enum | R | `loaded` iff either sample's `load1` exceeds `limit` (X20); FILTERABLE | §9(a); ties to `status` (§9 rule X13). X20 is what stops the verdict being an opinion beside the numbers |
| `environment.occupancy` | object | R | — | §9(b) |
| `environment.occupancy.tool` | string | o | DIAGNOSTIC; one tool for both samples | e.g. `mpstat -P ALL 1 1` |
| `environment.occupancy.before` | object | R | the per-core check BEFORE the run | §9(b) |
| `environment.occupancy.before.verdict` | enum | R | `pass`/`fail`/`unavailable` | §9(b) "machine-readable pass/fail with `unavailable` when mpstat is missing — recorded, never silently skipped" (C6) |
| `environment.occupancy.before.max_busy_pct` | number/null | R | the busiest non-target core; `null` iff `unavailable` | the number behind the verdict, so a threshold change is re-judgeable without re-measuring |
| `environment.occupancy.before.raw` | string | R | the mpstat block (pcrec `pinned_measure.sh:59-64`'s output), or why there is none | DIAGNOSTIC, and the evidence half of the verdict — required for the same reason `loadavg_raw` is |
| `environment.occupancy.after` | object | R | the per-core check AFTER the run | ADDITION: §9(a)'s own argument for the after-load applies unchanged to occupancy. A neighbour process that starts up midway is exactly the case a before-only check cannot see, and it is the case that moves a number |
| `environment.occupancy.after.verdict` | enum | R | as above | as above |
| `environment.occupancy.after.max_busy_pct` | number/null | R | as above | as above |
| `environment.occupancy.after.raw` | string | R | as above | as above |
| `environment.pinning` | object | R | — | §9(d) "pinned cores after the occupancy check" |
| `environment.pinning.mode` | enum | R | `taskset`/`chrt+taskset`/`none`/`unavailable` | pcrec degrades quietly when unprivileged (`compare.sh` `PIN_NOTE`); the record must say which |
| `environment.pinning.cpu` | integer/null | o | the pinned core | as above |
| `environment.governor` | string/null | o | DIAGNOSTIC | `compare.sh`'s machine-context table records it; frequency policy changes absolute numbers |
| `environment.turbo` | string/null | o | DIAGNOSTIC | as above |

#### `patterns[]` — the roster the rows reference

| field | type | req | rule / enum | why |
|---|---|---|---|---|
| `patterns` | array, ≥1 | R | — | rows key on `pattern_id`; "ids referenced by rows exist in setup" needs a roster |
| `patterns[].pattern_id` | slug | R | unique in the record; FILTERABLE | §6 rows are keyed by pattern |
| `patterns[].canonical_sha256` | hex64 | R | sha256 of the CANONICAL pattern text (UTF-8, no trailing newline) | §4.5 "a sub-bench's pattern is CANONICAL"; the hash is what makes "same pattern" checkable across records without carrying the text |
| `patterns[].canonical_text` | string | o | REPRODUCIBILITY-ONLY | convenience for reading a record alone; the sub-bench is the source of truth |
| `patterns[].hazard_class` | enum | R | COPIED from the sub-bench; FILTERABLE | §5 tags; §8 filters; B6 |
| `patterns[].size_class` | enum | R | COPIED; FILTERABLE | as above |
| `patterns[].tags` | array of string | o | DIAGNOSTIC | the sub-bench's other tags, carried but not filtered until they are enumerated |
| `patterns[].variant` | object/null | R | `null` = this testee runs the canonical text | §4.5: a variant is "never a silent fork" — the record states one either way |
| `patterns[].variant.kind` | enum | R | `syntax-only`/`restructured`; informational | §4.5; OD-B5 ruled it informational |
| `patterns[].variant.text` | string | R | REPRODUCIBILITY-ONLY | §4.5 "the variant text/options" |
| `patterns[].variant.options` | array of `{name,value}` | o | the variant's own runtime options | §4.5 "Runtime OPTION differences … are variants of the same kind" |
| `patterns[].variant.options[].name` | string | R | — | as above |
| `patterns[].variant.options[].value` | string/int/bool | R | — | as above |
| `patterns[].variant.objective_preservation` | string | R | REVIEWED text, not machine-checked | §4.5 constraint 2: "the variant declaration states how it still exercises it, and that statement is reviewed like any other expectation" |
| `patterns[].variant.capture_correspondence` | object | R | — | §4.5; B2 |
| `patterns[].variant.capture_correspondence.mode` | enum | R | `identical`/`by-name`/`by-index-map`/`not-applicable` | §4.5 "by name / by an explicit index map"; `identical` is the explicit claim that group structure did not change, which is the common case and must still be CLAIMED rather than assumed |
| `patterns[].variant.capture_correspondence.index_map` | map `"n"`→int | c | required when `mode` = `by-index-map` | §4.5 |
| `patterns[].variant.hazard_class` | enum | o | RE-ASSERTED; default = inherit `patterns[].hazard_class` | §4.5 "re-asserted HAZARD/SIZE class tags if the translation changes them"; B6 |
| `patterns[].variant.size_class` | enum | o | as above | as above |

#### `subjects[]` — the other roster

| field | type | req | rule / enum | why |
|---|---|---|---|---|
| `subjects` | array | R | may be empty (a record with no match rows) | match rows key on `subject_id` |
| `subjects[].subject_id` | slug | R | unique in the record; FILTERABLE | §6 "subject-or-subject-set" |
| `subjects[].role` | enum `single`/`set` | R | FILTERABLE | §6: a row may key on a subject SET (the 85-subject compliance list timed as one loop) |
| `subjects[].n_subjects` | integer ≥1 | R | 1 when `role` = `single` | lets the reporter compute per-subject cost without re-reading the sub-bench |
| `subjects[].bytes_offered` | integer ≥0 | R | total bytes OFFERED to the engine in one iteration | the denominator of throughput, and the number `consumed_length` is compared against (§4.4 truncation) |
| `subjects[].size_band` | string | o | RESERVED — becomes an enum when OD-B2 rules the cut points | §3's match regime "10 through 1000 bytes in bands (OD-B2)". Unruled, so no cut points are invented here |
| `subjects[].sha256` | hex64 | R | pins the exact bytes offered | §5's generated subjects are reproducible only if something says WHICH bytes. Optional made it the field a harness skips on the day the generator changes, which is the day it matters; §10.1's copied-facts risk applies to `bytes_offered` too and this is its only detectable half |

### FIELD TABLE: match

One row per (pattern × subject-or-subject-set × regime × trial)
(requirements §6).

| field | type | req | rule / enum | why |
|---|---|---|---|---|
| `kind` | const `"match"` | R | — | the discriminator |
| `seq` | integer ≥1 | R | dense and unique 1..N over ALL result rows of the record, in EMISSION order (X18) | ADDITION: §2's "file order is free" needs a carrier for the order that IS significant. Without it "the first match" — which is exactly how a lazy JIT's compile cost is defined (§3) — is a property of a file's line numbers, and a store that re-sorts rows changes a measurement |
| `pattern_id` | slug | R | must be in `setup.patterns[]` | §6 row key |
| `subject_id` | slug | R | must be in `setup.subjects[]` | §6 row key |
| `regime` | enum | R | must be in `setup.subbench.regimes`; FILTERABLE | §3: each regime is a first-class result kind and they are not comparable to each other |
| `trial` | integer ≥1 | R | 1..N contiguous per (pattern, subject, regime) | §2 "raw trials are kept"; §6 |
| `match_outcome` | enum | R | FILTERABLE | §4.4 per-(pattern, subject) set + the two ADDITIONS (§5) |
| `timing` | object | c | present IFF the cell is timed: `match_outcome` = `matched-as-expected` AND the pattern's compile rows say `compiled` | §7 "a timing for a wrong answer is worse than no timing"; §4.4 "Timing exists only for `compiled` ∧ expectation-agreeing cells" |
| `timing.elapsed_ns` | integer ≥0 | R | wall nanoseconds for the WHOLE batched loop | §3's timing protocol: a batched IN-PROCESS loop, never a per-call external wrapper (C5: this box's `timeout` alone costs ~108.7 ms/call, pcrec `docs/testing.md:2372`) |
| `timing.iterations` | integer ≥1 | R | the loop's N | as above; per-call cost is `elapsed_ns/iterations` and is the REPORTER's arithmetic |
| `timing.bytes_processed` | integer ≥0 | R | `bytes_offered × iterations`, or what the engine actually scanned | the throughput numerator; recorded raw so MB/s never appears in a record |
| `calibration` | object | c | required when `timing.iterations` > 1 | ADDITION: `iterations` is not a constant, it is CHOSEN — the harness probes the cell and picks N so one loop clears a target (`harness_contract.md` §3: ≥ 50 ms). The chosen N is in the record and the probe that chose it was not, which makes the loop length an unexplained free variable in every comparison. X21 checks the choice against its own target |
| `calibration.target_ns` | integer ≥1 | R | the loop length the probe was aiming for | as above |
| `calibration.probe_iterations` | integer ≥1 | R | iterations the probe ran | as above |
| `calibration.probe_elapsed_ns` | integer ≥0 | R | wall nanoseconds the probe took | as above; `probe_elapsed_ns / probe_iterations × iterations ≥ target_ns` is X21 |
| `calibration.calibration_note` | string | c | required when X21's inequality does NOT hold; DIAGNOSTIC | the escape hatch a real harness needs, and the reason X21 is a rule rather than a hope. A cell whose probe cannot predict its loop — a lazy JIT probed cold, a subject whose cost depends on where the previous match stopped — must SAY so; the alternative is a silent short loop that reads as a fast engine |
| `consumed_length` | integer/null | o | `null` = the API does not expose it | §4.4 "`consumed_length` is recorded whenever the API exposes it" (A7) |
| `truncation_check` | enum | c | required when `regime` = `large-subject-throughput` | §4.4: "a large-subject cell without it is marked unverified-for-truncation" |
| `observed` | object | c | required when `match_outcome` is `did-not-match-as-expected` or `wrong-span-or-captures`; DIAGNOSTIC | §7: a disagreement is a finding that feeds `upstream_findings.md`, and a finding with no observed value is not actionable |
| `observed.matched` | boolean | R | — | as above |
| `observed.span` | `[int,int]`/null | o | — | §4.4 `wrong-span-or-captures` |
| `observed.captures` | array of `[int,int]`/null | o | `-1` for an unset slot | as above; the capture correspondence (§4.5) is what makes this comparable across a variant |
| `engine_metadata` | map | o | every name declared with `scope` = `match` | §4.2, §7 rule 2 |
| `diagnostic` | string/null | o | DIAGNOSTIC, UNINDEXED | §4.2: pcrec's prose `RX_ENGINE_WHY` is "kept only as an unindexed diagnostic string" |

### FIELD TABLE: compile

One row per (pattern × trial) (requirements §6; R1 finding A5 — the
compile cost does not fit the match row's shape). This row also carries
the per-(pattern, testee) OUTCOME of §4.4, because that outcome is a
property of compiling, and this is the compiling row.

| field | type | req | rule / enum | why |
|---|---|---|---|---|
| `kind` | const `"compile"` | R | — | the discriminator |
| `seq` | integer ≥1 | R | one 1..N sequence shared with the match rows (X18) | ADDITION, as above. The sequence is per RECORD, not per row kind: interleaving compile and match rows is what a harness actually does, and the order between them is part of what happened |
| `pattern_id` | slug | R | must be in `setup.patterns[]` | §6 row key |
| `trial` | integer ≥1 | R | 1..N contiguous per pattern | C4: pcrec's single-sample GCC-TIME swung 1.87× on a quiet box (`~/pcrec/tests/bench/CLAUDE.md:78`), so compile cost is median-of-N with spread like everything else — which means N RAW trials here |
| `compile_outcome` | enum | R | FILTERABLE | §4.4 per-(pattern, testee) set |
| `cost_class` | enum | R | MUST equal `setup.testee.execution_model` | §3 "Reports never reduce compile costs of different classes into one cell without labelling the class"; the same four tokens are used on both fields so the check is literal equality and no mapping table can be got wrong |
| `cost` | object | c | present IFF `compile_outcome` = `compiled` AND `cost_class` ≠ `lazy-jit` | §3's per-class protocol (A6) |
| `cost.total_ns` | integer ≥0 | R | the whole compile/setup for this trial | §3 "on its own axis, never folded into match time" (APPROACH §3) |
| `cost.phases` | array | o | names and order must equal `setup.testee.compile_phases` | §3 AOT: "pattern → C → gcc → loadable object, all phases, each timed" |
| `cost.phases[].name` | slug | R | — | as above |
| `cost.phases[].elapsed_ns` | integer ≥0 | R | phases need not sum to `total_ns` (harness overhead between them) | as above |
| `derivation` | const `first-match-row-minus-steady-state` | c | present IFF `cost_class` = `lazy-jit`, and `cost` is then FORBIDDEN. The subtrahend is the GLOBALLY-FIRST match row of this pattern in this record — the one with the lowest `seq` — and the steady state is the rest | §3: a lazy JIT has "no separable call: cost = trial 1 minus steady state". That is a REDUCTION over match rows, and reductions do not belong in a record — so the row names the derivation and the reporter does the arithmetic from the raw match trials (A6 + "raw trials, not reductions"). The token says "first match row", not "trial 1", DELIBERATELY: `trial` is numbered per (pattern, subject, regime), so a pattern measured over 85 subjects has 85 rows numbered `trial: 1` and only ONE of them paid the JIT. `seq` is what distinguishes them |
| `artifact_bytes` | integer/null | o | recorded if free, NOT scored | §3 "Deferred, recorded if free but not scored: memory high-water, artifact/code size" |
| `declaration_ref` | string | c | required when `compile_outcome` = `unsupported-by-declaration` | §4.4: the outcome means "the sub-bench's engine notes SAY this engine cannot express the intention" — the row must cite the note, or the outcome is an unfalsifiable excuse |
| `diagnostic` | string/null | c | required when `compile_outcome` = `did-not-compile`; DIAGNOSTIC, UNINDEXED | §4.4 "(with the engine's diagnostic)" |
| `engine_metadata` | map | o | every name declared with `scope` = `pattern` | §4.2, §7 rule 2 — this is the canonical home of the mechanism stamps |

## 9. Cross-line rules — what `validate.py` enforces

JSON Schema validates a LINE. Everything that relates two lines, or a
line to a derivation, or a field to a normalization rule, is code.
These are the rules; each has at least one positive control in
`schema/examples/bad/` (pcrec's check-design lesson: a check with no
failing case proves nothing). At v1.1 there are 23 rules and 36
controls.

That claim — "each has at least one positive control" — was FALSE when
draft 1 was merged, and re-reading it is how it was found: X5, X7, X8,
X12 and X16 had no file in `examples/bad/` at all. Five of twenty-three
rules had never been seen to fire. They have controls now. The lesson
is the project's own, one level up: a check with no failing case proves
nothing, and a CLAIM that every check has a failing case is itself a
check — so it needs one too. `check_fields.py` compares the note's field
tables against the schema; `check_rules.py` now compares THIS table
against the directory, and fails the build for a rule with no control
or a control naming a rule that does not exist. It was sabotage-checked
both ways before being believed.

| id | rule | source |
|---|---|---|
| X1 | Line 1 is `kind: "setup"`; no other line is | §6 two layers; catches two records concatenated |
| X2 | Every line is a JSON object with a known `kind`. `match-list` is RESERVED and rejected with "reserved, not yet defined" | OD-B3 |
| X3 | `record_id` equals the id derived from `subbench.id`, `subbench.version`, `testee.testee_id`, `environment.machine_id`, `run.timestamp` (+ optional `-<n>`) | §3 |
| X4 | The file's basename equals `record_id + ".jsonl"` (skipped when validating a stream) | §2 |
| X5 | `testee.testee_id` equals the id derived from `engine_name`, `engine_version`, `engine_mode`, `captures`, `simd`, `config_extra` | §6.4 |
| X6 | `content_hash.value` equals the recomputed hash | §3 |
| X7 | Every row's `pattern_id` is in `setup.patterns[]`; every match row's `subject_id` is in `setup.subjects[]` | brief: "ids referenced by rows exist in setup" |
| X8 | Every match row's `regime` is in `setup.subbench.regimes` | §3 |
| X9 | Trials are exactly 1..N, no gaps, no duplicates, per (pattern, subject, regime) for match rows and per pattern for compile rows | §2 raw trials; a duplicate trial silently doubles a cell's weight in a median |
| X10 | `compile_row.cost_class` equals `testee.execution_model` | §3; brief |
| X11 | A match row carries `timing` only if `match_outcome` = `matched-as-expected` AND every compile row for that pattern has `compile_outcome` = `compiled` | §4.4/§7; brief |
| X12 | `cost.phases` names and order equal `testee.compile_phases` | §3 |
| X13 | `status` = `measured` requires `load.verdict` = `quiet` and NEITHER `occupancy.before.verdict` NOR `occupancy.after.verdict` = `fail`. `unavailable` does not disqualify — §9(b) makes it a thing to RECORD, not a thing to fail on, and a box without mpstat would otherwise be unable to produce a measured record at all | §9(a) "a record whose after-load exceeds it is `inconclusive-load`, not measured" (C7); §9(b) |
| X14 | `status` = `measured` requires a compile row for every pattern in the roster | makes `harness-failure` mean something: a record that stopped halfway cannot claim to be measured |
| X15 | Every `engine_metadata` name is declared; its `scope` matches the row kind; its value matches the declared type (`enum` value in `values`, `mask` bits in `bits`, integer, string) | §4.2, §7 rule 1 |
| X16 | `testee.warmup_trials` ≥ 1 when `execution_model` = `lazy-jit` | §3 (A6) |
| X17 | Across files given to one invocation: no two differing MAJOR `schema_version`s | §4, A10 |
| X18 | Every result row's `seq` is unique, and the record's seqs are exactly 1..N over ALL result rows | §2; the lazy-JIT derivation needs a well-defined "first" |
| X19 | Each load sample's `load1`/`load5`/`load15` equal the first three numbers of its own `loadavg_raw` | §9(a); the evidence rule — a parsed number that disagrees with the line it came from is the whole point of keeping the line |
| X20 | `load.verdict` is `loaded` iff either sample's `load1` exceeds `limit`, `quiet` otherwise | §9(a). Without it X13 is inert: a harness that stamps `quiet` beside a `load1` of 9.8 satisfies X13 and the record claims to be measured |
| X21 | `calibration.probe_elapsed_ns / probe_iterations × timing.iterations ≥ calibration.target_ns`, or `calibration_note` says why not | §3's batched-loop protocol; `harness_contract.md` §3's auto-calibration. A loop that fell short of its target is a shorter measurement than the record claims to have taken |
| X22 | `testee.engine_commit` is present and full 40-hex whenever `testee.engine_version` is not a release-tag shape (§6.2) | §4.2's "pinned"; §6.2's binding rule, which until now nothing enforced |
| X23 | `cpu_model`, `kernel` and `compiler` equal what §6.6/§6.7's rules produce from `cpu_model_raw`, `kernel_raw` and `compiler_raw`, when those are present | §6; A11. The normalization rules existed as prose only, which means the FILTERABLE half of each pair was un-checked against the reproducible half |

Messages name the line number (1-based, as an editor counts), the field
path, and the RULE ID in brackets. The rule id is not decoration: each
rule has a sabotaged record in `schema/examples/bad/` whose FILE NAME is
the rule it must fire (`x11-timing-on-uncompiled-cell.jsonl`,
`schema-wrong-enum.jsonl`), and `make check-schema` fails a control that
is rejected for some other reason. A control that rejects for the wrong
reason proves nothing about the rule it was written for — which is the
same failure mode as a check with no failing case, one level up. Every
sabotage is the good example with exactly ONE thing wrong and its hash
RESTAMPED, so X6 does not fire alongside the intended rule and mask it.

Two corollaries worth stating because they surprised the author:

- **X11 bites a pattern with no compile row at all.** "Every compile row
  for that pattern says `compiled`" is false when there are none, so a
  timed match row for a pattern the record never recorded compiling is
  rejected. That is intended: a timing whose compile the record does not
  witness is a timing with no provenance. It also means X14's control
  fires X11 as well, which is honest rather than noisy.
- **X6 makes the examples restampable, not editable.**
  `validate.py --print-hash FILE` prints the value an edited example
  needs. Records in the STORE are never edited (requirements §6); the
  examples are documents, and this is the one place the distinction
  matters.

The check-schema harness was itself sabotage-validated on 2026-08-25: a
valid record placed in `examples/bad/` makes it fail, and so does a
control renamed to claim a rule it does not fire. A gate that has never
been seen to fail is not known to be a gate.

RE-VALIDATED at v1.1 (2026-08-25), because a gate is only known to be a
gate at the version it was last seen failing at. Both sabotages above
still make `make check-schema` fail (the planted-valid record is
reported `NOT REJECTED AS INTENDED`; the renamed control reports
`expected rule X11 to fire, but the rules that fired were ['X23']`),
and one more was run for v1.1's own machinery: deleting
`calibration_note` from the v8 example's eight timed rows makes X21
reject it. That last one matters because the note is the only place in
this schema where a rule can be satisfied by writing a sentence (§11
item 10), and a sentence that is never checked for being load-bearing
is decoration.

## 10. Denormalization, extension points, what is absent

### 10.1 The copied sub-bench facts

`patterns[].hazard_class`, `patterns[].size_class`,
`subjects[].bytes_offered`, `subbench.objective` and
`patterns[].canonical_text` are COPIES of sub-bench facts. The copy
exists so a report can filter without loading every sub-bench version
it touches (and so a record read alone is intelligible). The risk is
the obvious one: a copy can disagree with its source. The mitigation is
`subbench.content_hash` — the copy is pinned to an exact snapshot, so a
disagreement is detectable by whoever holds both. It is NOT detectable
by `validate.py`, which sees only the record; a store-level check
belongs to [B3]. **Flagged for the panel (§11.3).**

### 10.2 Reserved, deliberately unbuilt

- **`kind: "match-list"`** — the list-valued row shape a scan regime
  (all matches in a big subject) would need (OD-B3, A9). The NAME is
  reserved and `validate.py` rejects it with a message saying so; no
  shape is defined, no fields are pre-built. If OD-B3 is ruled in, the
  shape is designed then.
- **`subjects[].size_band`** — a free string until OD-B2 rules the
  10..1000-byte cut points; then it becomes an enum (a minor bump).
- **`environment.load.limit`** carries whatever threshold the run used
  because OD-B8 (what "quiet" means numerically) is measured at [B3].
  The schema constrains it to be positive and present, nothing more.

### 10.3 Absent on purpose

- **Any statistic.** No median, min, max, stddev, spread, `n`,
  pass-rate, MB/s or ns/call. OD-B1 (the comparables set) can be
  re-ruled at [B5] without invalidating a single record.
- **Any correctness verdict beyond the outcome enums.** The
  expectation lives in the sub-bench; the record says which outcome was
  observed against it.
- **A per-row unit string.** Units are fixed by field NAME
  (`elapsed_ns`, `bytes_processed`, `artifact_bytes`). Requirements §6
  says "the measured quantity with its unit"; a unit carried as DATA
  means two rows in one cell can differ in unit, which is precisely
  what a reducer cannot handle safely.
- **Hugepage / THP state.** Considered at the v1.1 panel (2026-08-25)
  and deliberately NOT added. Transparent hugepages are a real confound
  for the large-subject regime — a 1 MB subject's TLB behaviour is not
  the same under `always` and `never` — but no instrument in
  `harness_contract.md` samples `/sys/kernel/mm/transparent_hugepage/*`,
  and a field no described mechanism fills is a claim wearing a
  schema's clothes (the same argument that removed the v8 example's
  `tier` pair, §7). It is listed HERE so its absence is a decision on
  the record rather than an oversight, and so the day a throughput
  outlier resists explanation, the first question has somewhere to
  start. Adding it later is a MINOR bump.
- **A coverage or `n` field.** §8 requires N and pass-rate beside every
  number when coverage < 100% (B5) — the reporter computes both from
  the roster (expected rows) against the rows present. Storing a count
  that the rows themselves determine is a second source of one truth.

## 11. For the panel — what I am least sure of

STATUS after the v1.1 panel (2026-08-25): items 1 and 8 are CLOSED (a
ruling and a removal). Items 2, 3, 4, 5, 6 and 7 stand as written and
are still the places to attack. The v1.1 work added four residuals of
its own, listed as items 9-12.

1. **`match_outcome` gained `crashed` and `timed-out`** (§5,
   ADDITIONS 1). This is the only place the schema exceeds requirements
   §4.4's closed set. The argument is that a per-subject hang is the
   bench's headline hazard class and has nowhere else to go; the
   counter-argument is that §4.4 says "closed set" and a per-subject
   timeout could instead be modelled as an ABSENT row plus a
   per-pattern compile-row outcome of `timed-out` — which loses which
   subject hung. RULED at the [B2] merge 2026-08-25: accepted, requirements §4.4 amended — closed.
2. **The lazy-JIT compile row carries no number at all** (§8, compile
   `derivation`). It is the only row kind whose quantity is not in the
   record, and it makes the reporter's job class-dependent. It follows
   from "raw trials, not reductions", but it also means a lazy-JIT
   testee's compile cost cannot be read from a record without reading
   its match rows — and requirements §13 attack-list item 3 already
   doubts the protocol itself (does a JIT warm per pattern AND per
   subject shape?). If that protocol changes, this row changes.
3. **The copied sub-bench facts** (§10.1): four fields duplicated for
   filterability, pinned only by a hash the validator cannot check.
   The alternative — the reporter joins every record against its
   sub-bench — is correct and slower, and pushes work into [B5].
4. **One `compiler` field** (§6.7). Fine for pcrec (AOT, gcc) and
   libpcre2 (C). Wrong-shaped the moment a rustc- or cargo-built testee
   lands: is the box's C compiler still an environment dimension, or
   does each testee carry its own toolchain?
5. **`trial` numbering must be dense 1..N** (X9). It is a strong check
   and it forbids a harness from discarding a trial mid-run (a trial
   killed by `gnutimeout`, say) without renumbering. Is renumbering
   acceptable, or should the rule be "unique, ascending" instead?
6. **`testee_id` is fully derived** (§6.4, X5). It buys a real check
   and costs flexibility: a testee that differs in a dimension the
   config slug does not name needs `config_extra`, which is
   author-chosen and therefore the one part of the id that can be
   inconsistent between two adapters.
7. **`engine_metadata` mask values are arrays of bit names.** Filterable
   and readable, but larger than an integer and it makes the record
   depend on the ADAPTER's spelling of pcrec's bit names. A wrong
   spelling is caught (X15, against the declaration) but a
   consistently-wrong spelling is not.
8. **`quiet_attestation` vs `load.verdict`** — a claim beside a
   measurement. Deliberate (a disagreement is a finding), but it is
   also a field a harness could set to `true` unconditionally, which
   would make it noise. RULED at the v1.1 panel 2026-08-25: the field
   is DROPPED — closed. The panel's argument is the stronger form of
   the doubt above: the "finding" the field was supposed to produce
   requires a harness that lies in one place and tells the truth in
   another, and the same harness writes both. `status` is already gated
   on the MEASURED verdicts (X13, X20), so nothing the field claimed is
   unrecorded and nothing it claimed was checkable. It is the exact
   shape pcrec's own check-design lesson warns about — a control whose
   source is the thing it controls. requirements §6's "quiet-box
   attestation" is discharged by `load` + `occupancy` + `status`.
9. **X21 checks that the calibration met its target, not that
   `iterations` was DERIVED from the probe.** A harness that probes
   correctly and then picks a wildly larger N passes. The stronger rule
   — `iterations` is within some factor of `target_ns × probe_iterations
   / probe_elapsed_ns` — was not written because no measurement on this
   box says what that factor should be, and a threshold invented at a
   desk is the thing §9's OD-B8 exists to avoid. [B3] measures it.
10. **`calibration_note` is free text and X21 accepts any non-empty
   string.** It is the one place in the schema where a rule can be
   satisfied by writing a sentence. The alternative — an enum of
   reasons a calibration can miss — needs a list nobody has yet, and
   inventing one now would be the `tier` mistake (§7) again.
11. **The load and occupancy samples have no relation to
   `run.timestamp` or to each other.** `sampled_at` exists, and nothing
   checks that `before` precedes `after`, that either brackets the run,
   or that the two are more than a millisecond apart. The check is easy
   and was left out on purpose: the ORDER is obvious to write and the
   DURATION threshold is another invented number. A record can still
   claim two samples taken back-to-back after the run.
12. **X23 checks three normalizations and cannot check the fourth
   kind.** `engine_name` and `engine_mode` are registry assertions, and
   a testee that spells its engine `pcre-2` instead of `libpcre2`
   produces a valid record that lands in its own filter bucket forever.
   The registry is in §6.1/§6.3, in prose, and only a human reads it.
13. **X17's cross-FILE half has no control and cannot easily get one.**
   The rule fires when one invocation is handed files of differing
   MAJOR versions — but any file at a major this validator does not
   implement is already rejected standalone, so no pair of files
   isolates the cross-file behaviour. `bad/x17-future-major-version`
   covers the standalone half only. Building a real control needs a
   second validator version, which is a [B3]/[B5] concern.
14. **Nothing checked that every rule in §9's table had a control** —
   which is how five rules went uncontrolled from draft 1 to v1.1 (§9).
   CLOSED at v1.1: `schema/check_rules.py` diffs §9's rule table against
   `examples/bad/`'s listing on every `make check-schema`, the same way
   `check_fields.py` diffs the FIELD tables against the schema. What
   remains open is narrower and worth stating: the gate proves a rule
   has a control NAMED for it, and `--expect-rule` proves that control
   fires that rule. Neither proves the control sabotages the thing the
   rule is ABOUT — a control could fire X12 for a reason unrelated to
   phase names. That last step is a review, and there is no obvious
   mechanism for it.
