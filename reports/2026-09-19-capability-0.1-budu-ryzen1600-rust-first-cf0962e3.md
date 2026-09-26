# pcrec-bench report

reporter: v24 (2026-09-26)

## Query

- filters: subbench=capability, version=0.1, until=2026-09-19T22:58:39Z, testee=rust_1.13.1_default-caps-simdna
- record source: store/index.tsv (1 record(s) matching this query)
- records included: 1
- worst other-core busy: 42.61% (`rust_1.13.1_default-caps-simdna` / `keyword-prefix-order` / `large-subject-throughput`)
    - `capability@0.1__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260919T213423Z` (store/records/capability@0.1/rust_1.13.1_default-caps-simdna/capability@0.1__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260919T213423Z.jsonl) — agreement: agree (0 of 82 groups; 0 of 3194 rows; 4 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): capability@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.6
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 1 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 90.2 | 0.0001 | 87.6 | 90.7 | 1.3 | 1.000x | 1.000x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.9 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 30.7 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 32.3 | 0.0005 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,222.6 | 2,222.1 | 2,234.9 | 5.0 | 1.000x | 1.000x | 75 | 29.6 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,442,428.7 | 1.7747 | 2,441,687.7 | 2,445,241.0 | 1,223.2 | 1.000x | 1.000x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,861,370.2 | 1.7751 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 464,531.7 | 1.7720 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 116,506.5 | 1.7777 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,496.1 | 2,436.4 | 2,504.6 | 24.8 | 1.000x | 1.000x | 75 | 33.3 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,442,944.3 | 1.7751 | 2,441,324.0 | 2,449,735.4 | 3,087.3 | 1.000x | 1.000x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,862,007.4 | 1.7757 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 464,322.9 | 1.7713 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 116,614.0 | 1.7794 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,486.0 | 2,427.5 | 2,488.3 | 23.1 | 1.000x | 1.000x | 75 | 33.1 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 82.0 | 0.0001 | 78.0 | 83.5 | 2.0 | 1.000x | 1.000x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 25.3 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 26.5 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 28.3 | 0.0004 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,762.3 | 1,740.5 | 3,003.3 | 497.9 | 1.000x | 1.000x | 75 | 23.5 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 107.4 | 0.0001 | 106.9 | 110.1 | 1.2 | 1.000x | 1.000x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 37.0 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 32.9 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 37.7 | 0.0006 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 4,060.6 | 4,018.6 | 4,078.4 | 19.9 | 1.000x | 1.000x | 75 | 54.1 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 87.7 | 0.0001 | 87.4 | 111.9 | 9.6 | 1.000x | 1.000x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 27.4 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 27.1 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 33.2 | 0.0005 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 46,454.2 | 0.0338 | 46,422.0 | 46,539.6 | 41.2 | 1.000x | 1.000x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 35,303.8 | 0.0337 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 8,882.0 | 0.0339 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,282.4 | 0.0348 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,424.6 | 1,419.0 | 1,430.2 | 3.6 | 1.000x | 1.000x | 75 | 19.0 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 23,422.6 | 0.0170 | 23,398.3 | 23,521.2 | 44.9 | 1.000x | 1.000x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,817.3 | 0.0170 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 4,459.0 | 0.0170 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 1,135.2 | 0.0173 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,228.2 | 1,226.7 | 1,230.0 | 1.1 | 1.000x | 1.000x | 75 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,444,100.7 | 1.7759 | 2,443,685.1 | 2,478,787.6 | 13,643.9 | 1.000x | 1.000x |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,861,517.3 | 1.7753 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 465,521.4 | 1.7758 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 117,203.3 | 1.7884 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18.1 | 0.0000 | 17.9 | 18.6 | 0.2 | 1.000x | 1.000x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.2 | 0.0000 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0001 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,435.3 | 1,433.0 | 1,993.4 | 223.3 | 1.000x | 1.000x | 75 | 19.1 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 366,013.7 | 0.2659 | 364,991.4 | 366,809.1 | 648.4 | 1.000x | 1.000x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 280,266.4 | 0.2673 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 69,143.3 | 0.2638 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 16,727.8 | 0.2552 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,619.6 | 1,615.9 | 1,623.8 | 2.5 | 1.000x | 1.000x | 75 | 21.6 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 86.5 | 0.0001 | 84.4 | 89.9 | 1.9 | 1.000x | 1.000x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.4 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 28.9 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 31.2 | 0.0005 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,562.5 | 1,551.7 | 1,568.0 | 5.3 | 1.000x | 1.000x | 75 | 20.8 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 86.6 | 0.0001 | 85.6 | 103.2 | 6.8 | 1.000x | 1.000x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 27.7 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 29.1 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 30.5 | 0.0005 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,674.0 | 2,657.8 | 2,687.4 | 9.7 | 1.000x | 1.000x | 75 | 35.7 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 86.8 | 0.0001 | 86.6 | 89.1 | 1.0 | 1.000x | 1.000x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.6 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 29.3 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 30.7 | 0.0005 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,969.7 | 2,965.1 | 3,034.4 | 26.7 | 1.000x | 1.000x | 75 | 39.6 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 60,176.9 | 0.0437 | 60,140.3 | 60,326.9 | 70.0 | 1.000x | 1.000x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 46,014.7 | 0.0439 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 11,435.6 | 0.0436 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,735.2 | 0.0417 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,313.2 | 1,309.4 | 1,314.5 | 1.9 | 1.000x | 1.000x | 75 | 17.5 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 82.5 | 0.0001 | 82.2 | 94.6 | 4.8 | 1.000x | 1.000x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.0 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 27.6 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 28.8 | 0.0004 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,993.1 | 1,966.1 | 1,997.3 | 11.2 | 1.000x | 1.000x | 75 | 26.6 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18.1 | 0.0000 | 17.9 | 18.6 | 0.3 | 1.000x | 1.000x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.1 | 0.0000 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 5.9 | 0.0001 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 698.2 | 696.6 | 851.3 | 59.9 | 1.000x | 1.000x | 75 | 9.3 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 306,992.6 | 0.2231 | 306,470.0 | 307,772.4 | 473.8 | 1.000x | 1.000x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 236,106.7 | 0.2252 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 56,771.8 | 0.2166 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 14,090.2 | 0.2150 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,330.5 | 1,329.3 | 1,332.6 | 1.3 | 1.000x | 1.000x | 75 | 17.7 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280,588.6 | 0.2039 | 280,476.1 | 281,656.0 | 434.5 | 1.000x | 1.000x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 213,652.7 | 0.2038 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 53,452.0 | 0.2039 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 13,472.8 | 0.2056 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 3,048.9 | 3,033.9 | 3,112.7 | 28.1 | 1.000x | 1.000x | 75 | 40.7 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 10,611,468.2 | 7.7104 | 10,601,434.4 | 10,651,336.3 | 17,923.9 | 1.000x | 1.000x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 8,118,553.5 | 7.7425 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 1,998,307.4 | 7.6229 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 490,709.4 | 7.4876 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 11,633.3 | 11,631.3 | 11,648.1 | 6.1 | 1.000x | 1.000x | 75 | 155.1 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 23,453.4 | 0.0170 | 23,444.4 | 23,486.2 | 16.3 | 1.000x | 1.000x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,863.0 | 0.0170 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 4,456.2 | 0.0170 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 1,132.3 | 0.0173 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,226.8 | 1,225.0 | 1,227.3 | 0.9 | 1.000x | 1.000x | 75 | 16.4 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 23,643.5 | 0.0172 | 23,519.6 | 23,660.0 | 51.8 | 1.000x | 1.000x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,954.3 | 0.0171 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 4,501.1 | 0.0172 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 1,171.4 | 0.0179 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,946.7 | 2,899.0 | 2,959.3 | 22.0 | 1.000x | 1.000x | 75 | 39.3 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-datetime-datefinder-alternation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 35,097,768.8 | 25.5024 | 34,665,106.8 | 36,664,770.8 | 689,613.0 | 1.000x | 1.000x |

#### `wild-datetime-datefinder-alternation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 24,494,716.0 | 23.3600 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 7,496,170.5 | 28.5956 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 3,104,509.5 | 47.3711 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-datetime-datefinder-alternation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 87,853.4 | 87,550.9 | 88,123.3 | 182.6 | 1.000x | 1.000x | 75 | 1,171.4 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 298.8 | 0.0002 | 298.3 | 306.5 | 3.1 | 1.000x | 1.000x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 40.8 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 126.1 | 0.0005 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 132.2 | 0.0020 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,043.2 | 2,041.7 | 2,059.5 | 6.7 | 1.000x | 1.000x | 75 | 27.2 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 135,249.6 | 0.0983 | 135,203.9 | 136,100.1 | 337.3 | 1.000x | 1.000x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 104,901.4 | 0.1000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 25,024.4 | 0.0955 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 5,385.9 | 0.0822 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,143.1 | 2,134.7 | 2,159.6 | 8.8 | 1.000x | 1.000x | 75 | 28.6 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 46,777.4 | 0.0340 | 46,713.8 | 46,845.5 | 53.7 | 1.000x | 1.000x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 35,503.8 | 0.0339 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 8,964.6 | 0.0342 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,283.3 | 0.0348 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,683.7 | 1,679.8 | 1,688.7 | 3.7 | 1.000x | 1.000x | 75 | 22.4 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 645,023.5 | 0.4687 | 644,579.6 | 647,071.6 | 882.2 | 1.000x | 1.000x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 493,929.8 | 0.4710 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 121,751.7 | 0.4644 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 29,243.6 | 0.4462 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,558.7 | 2,554.5 | 2,571.5 | 6.8 | 1.000x | 1.000x | 75 | 34.1 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 489,279.0 | 0.3555 | 488,438.4 | 490,860.7 | 818.6 | 1.000x | 1.000x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 372,494.4 | 0.3552 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 93,594.8 | 0.3570 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 22,876.4 | 0.3491 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,478.7 | 2,475.6 | 2,555.5 | 31.3 | 1.000x | 1.000x | 75 | 33.0 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 82,230.5 | 0.0597 | 82,015.7 | 82,304.2 | 117.6 | 1.000x | 1.000x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 63,408.7 | 0.0605 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 15,087.2 | 0.0576 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 3,648.4 | 0.0557 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,342.9 | 1,341.3 | 1,345.1 | 1.4 | 1.000x | 1.000x | 75 | 17.9 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 78.3 | 0.0001 | 77.1 | 78.8 | 0.7 | 1.000x | 1.000x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 25.7 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 25.8 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 26.4 | 0.0004 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,594.0 | 1,591.4 | 1,598.6 | 2.4 | 1.000x | 1.000x | 75 | 21.3 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,150,186.6 | 9.5550 | 13,126,662.0 | 15,510,436.1 | 947,845.2 | 1.000x | 1.000x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 10,075,484.1 | 9.6087 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 2,478,668.1 | 9.4554 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 601,581.4 | 9.1794 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,254.6 | 13,118.4 | 13,266.3 | 61.6 | 1.000x | 1.000x | 75 | 176.7 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 107.8 | 0.0001 | 107.2 | 149.5 | 16.6 | 1.000x | 1.000x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 37.3 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 32.9 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 37.4 | 0.0006 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,580.2 | 2,569.8 | 2,613.6 | 17.4 | 1.000x | 1.000x | 75 | 34.4 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 17.9 | 0.0000 | 17.9 | 18.4 | 0.2 | 1.000x | 1.000x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0001 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,253.8 | 1,252.6 | 1,257.6 | 1.8 | 1.000x | 1.000x | 75 | 16.7 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18.1 | 0.0000 | 17.9 | 18.3 | 0.1 | 1.000x | 1.000x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.1 | 0.0000 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0001 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,669.5 | 1,658.5 | 1,694.6 | 12.7 | 1.000x | 1.000x | 75 | 22.3 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 210,621.0 | 0.1530 | 209,804.6 | 211,188.0 | 514.3 | 1.000x | 1.000x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 164,530.6 | 0.1569 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 37,196.7 | 0.1419 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 8,686.0 | 0.1325 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,240.7 | 1,240.2 | 1,242.9 | 1.0 | 1.000x | 1.000x | 75 | 16.5 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,446,068.2 | 1.7773 | 2,445,903.9 | 2,446,948.0 | 384.6 | 1.000x | 1.000x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,862,013.7 | 1.7758 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 466,148.1 | 1.7782 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 118,082.0 | 1.8018 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 4,408.0 | 4,405.7 | 4,413.5 | 3.1 | 1.000x | 1.000x | 75 | 58.8 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 388,639.4 | 0.2824 | 387,931.4 | 391,513.8 | 1,318.0 | 1.000x | 1.000x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 295,961.7 | 0.2823 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 73,861.3 | 0.2818 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 18,531.2 | 0.2828 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 3,205.0 | 3,198.4 | 3,210.0 | 3.7 | 1.000x | 1.000x | 75 | 42.7 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280,700.7 | 0.2040 | 280,469.7 | 281,750.6 | 465.9 | 1.000x | 1.000x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 213,624.6 | 0.2037 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 53,419.8 | 0.2038 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 13,520.3 | 0.2063 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,127.7 | 2,124.4 | 2,149.5 | 9.0 | 1.000x | 1.000x | 75 | 28.4 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,454,310.4 | 1.7833 | 2,453,185.8 | 2,464,936.9 | 4,394.6 | 1.000x | 1.000x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,451.3 | 1.7790 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 468,468.4 | 1.7871 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 119,788.0 | 1.8278 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 4,812.2 | 4,807.9 | 4,854.4 | 17.1 | 1.000x | 1.000x | 75 | 64.2 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41,251.5 | 0.0300 | 41,172.7 | 41,305.9 | 47.8 | 1.000x | 1.000x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 31,349.4 | 0.0299 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 7,868.7 | 0.0300 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,013.4 | 0.0307 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,422.3 | 2,362.4 | 2,505.9 | 45.9 | 1.000x | 1.000x | 75 | 32.3 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 96.0 | 0.0001 | 94.1 | 99.5 | 1.8 | 1.000x | 1.000x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 28.2 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 32.2 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 35.3 | 0.0005 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,796.4 | 1,794.7 | 2,389.5 | 237.3 | 1.000x | 1.000x | 75 | 24.0 | 16.4 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `rust_1.13.1_default-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (no-expectation), `sd-empty-alt-hit` (no-expectation) |
| `high-byte-run` | `short-subject-search` | `plain` | `rust_1.13.1_default-caps-simdna` | 75 | 97% | 0 | 10 | `nu-high-byte` (wrong), `nu-lead-with-cont` (wrong) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `base10num-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 140,811.0 | 131,460.0 | 688,222.0 | 214,722.6 | 5 | - | 1.525 (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 119,471.0 | 101,620.0 | 585,952.0 | 183,436.1 | 5 | - | 1.535 (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-flat` | `plain` | `rust_1.13.1_default-caps-simdna` | 192,660.0 | 178,340.0 | 1,171,524.0 | 388,211.7 | 5 | - | 2.015 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 86,081.0 | 65,380.0 | 527,902.0 | 176,294.9 | 5 | - | 2.048 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `rust_1.13.1_default-caps-simdna` | 118,630.0 | 84,531.0 | 683,822.0 | 227,593.9 | 5 | - | 1.919 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 247,281.0 | 181,340.0 | 1,185,623.0 | 382,322.7 | 5 | - | 1.546 (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `date-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 22,320.0 | 19,260.0 | 250,001.0 | 90,575.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 26,760.0 | 22,270.0 | 232,571.0 | 82,243.1 | 5 | - | 3.073 (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 21,510.0 | 16,860.0 | 228,271.0 | 82,546.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 30,970.0 | 26,990.0 | 274,981.0 | 97,098.0 | 5 | - | 3.135 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `rust_1.13.1_default-caps-simdna` | 23,351.0 | 17,210.0 | 224,930.0 | 81,243.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 23,880.0 | 20,030.0 | 228,321.0 | 81,842.7 | 5 | - | 3.427 (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `rust_1.13.1_default-caps-simdna` | 10,640.0 | 7,380.0 | 228,510.0 | 87,256.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 85,080.0 | 60,310.0 | 481,761.0 | 160,674.5 | 5 | - | 1.889 (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor-byte` | `plain` | `rust_1.13.1_default-caps-simdna` | 4,220.0 | 1,640.0 | 170,640.0 | 67,040.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 11,210.0 | 8,330.0 | 203,481.0 | 76,535.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `rust_1.13.1_default-caps-simdna` | 96,760.0 | 88,580.0 | 1,031,093.0 | 367,727.8 | 5 | - | 3.800 (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 51,470.0 | 49,150.0 | 487,061.0 | 170,450.8 | 5 | - | 3.312 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 590,142.0 | 471,181.0 | 1,068,383.0 | 206,287.8 | 5 | - | 0.350 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 582,902.0 | 485,171.0 | 1,080,323.0 | 209,184.9 | 5 | - | 0.359 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `rust_1.13.1_default-caps-simdna` | 19,560.0 | 13,590.0 | 420,851.0 | 160,454.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 56,750.0 | 51,700.0 | 529,061.0 | 186,859.8 | 5 | - | 3.293 (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic-removed` | `plain` | `rust_1.13.1_default-caps-simdna` | 147,300.0 | 129,841.0 | 595,892.0 | 178,096.7 | 5 | - | 1.209 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 347,762.0 | 324,651.0 | 1,352,284.0 | 397,411.1 | 5 | - | 1.143 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `mojibake-curly-quote` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `negation-scope-lookbehind-var` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `numeric-id-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 82,431.0 | 67,010.0 | 526,061.0 | 176,216.0 | 5 | - | 2.138 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 85,610.0 | 75,000.0 | 497,271.0 | 163,153.0 | 5 | - | 1.906 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 109,790.0 | 90,700.0 | 631,042.0 | 207,471.2 | 5 | - | 1.890 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 92,170.0 | 81,030.0 | 529,622.0 | 172,586.6 | 5 | - | 1.872 (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `router-prefix-order` | `plain` | `rust_1.13.1_default-caps-simdna` | 8,050.0 | 5,700.0 | 195,140.0 | 74,783.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 23,290.0 | 19,790.0 | 241,111.0 | 86,204.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `trim-nested-star` | `plain` | `rust_1.13.1_default-caps-simdna` | 51,030.0 | 42,090.0 | 468,492.0 | 165,037.2 | 5 | - | 3.234 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 209,811.0 | 44,910.0 | 480,662.0 | 158,856.6 | 5 | - | 0.757 (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `uuid-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 125,351.0 | 102,370.0 | 576,502.0 | 184,029.6 | 5 | - | 1.468 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 49,400.0 | 43,570.0 | 278,650.0 | 91,957.0 | 5 | - | 1.861 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `rust_1.13.1_default-caps-simdna` | 10,280.0 | 4,310.0 | 360,371.0 | 141,188.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 11,370.0 | 8,600.0 | 205,330.0 | 77,222.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `rust_1.13.1_default-caps-simdna` | 171,580.0 | 146,901.0 | 633,192.0 | 186,365.9 | 5 | - | 1.086 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 41,760.0 | 34,130.0 | 283,641.0 | 95,965.9 | 5 | - | 2.298 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `rust_1.13.1_default-caps-simdna` | 735,312.0 | 661,912.0 | 1,814,755.0 | 432,511.5 | 5 | - | 0.588 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-object-begin` | `plain` | `rust_1.13.1_default-caps-simdna` | 4,020.0 | 1,680.0 | 177,230.0 | 69,680.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 11,480.0 | 8,520.0 | 205,981.0 | 77,400.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `rust_1.13.1_default-caps-simdna` | 35,930.0 | 32,180.0 | 258,970.0 | 88,445.5 | 5 | - | 2.462 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-datefinder-alternation` | `plain` | `rust_1.13.1_default-caps-simdna` | 10,397,271.0 | 9,794,029.0 | 16,690,550.0 | 2,548,803.5 | 5 | - | 0.245 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 10,383,311.0 | 9,743,529.0 | 23,726,090.0 | 5,357,634.1 | 5 | - | 0.516 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `rust_1.13.1_default-caps-simdna` | 2,705,828.0 | 2,651,908.0 | 4,469,613.0 | 691,916.2 | 5 | - | 0.256 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 2,532,438.0 | 2,490,967.0 | 4,210,452.0 | 657,612.0 | 5 | - | 0.260 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-secrets-aws-access-key-id` | `plain` | `rust_1.13.1_default-caps-simdna` | 140,081.0 | 129,190.0 | 605,612.0 | 184,294.2 | 5 | - | 1.316 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 51,770.0 | 46,750.0 | 269,080.0 | 86,800.4 | 5 | - | 1.677 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `rust_1.13.1_default-caps-simdna` | 229,940.0 | 193,980.0 | 687,982.0 | 186,693.9 | 5 | - | 0.812 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 136,181.0 | 107,861.0 | 372,281.0 | 100,331.4 | 5 | - | 0.737 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `rust_1.13.1_default-caps-simdna` | 660,632.0 | 569,572.0 | 1,199,373.0 | 232,799.0 | 5 | - | 0.352 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 409,412.0 | 334,581.0 | 868,422.0 | 196,301.2 | 5 | - | 0.479 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `rust_1.13.1_default-caps-simdna` | 507,941.0 | 456,622.0 | 1,194,223.0 | 277,353.5 | 5 | - | 0.546 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 445,032.0 | 380,911.0 | 1,057,693.0 | 251,045.3 | 5 | - | 0.564 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `rust_1.13.1_default-caps-simdna` | 15,120.0 | 12,080.0 | 433,781.0 | 166,549.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 57,220.0 | 51,651.0 | 475,272.0 | 165,363.4 | 5 | - | 2.890 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `rust_1.13.1_default-caps-simdna` | 31,370.0 | 24,860.0 | 463,061.0 | 171,446.1 | 5 | - | 5.465 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 40,060.0 | 27,390.0 | 467,671.0 | 172,508.3 | 5 | - | 4.306 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `rust_1.13.1_default-caps-simdna` | 83,140.0 | 71,561.0 | 531,901.0 | 177,386.3 | 5 | - | 2.134 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 102,451.0 | 83,820.0 | 635,402.0 | 211,650.2 | 5 | - | 2.066 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `rust_1.13.1_default-caps-simdna` | 36,150.0 | 31,730.0 | 256,800.0 | 87,985.3 | 5 | - | 2.434 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 97,640.0 | 91,840.0 | 576,122.0 | 190,344.3 | 5 | - | 1.949 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `rust_1.13.1_default-caps-simdna` | 97,720.0 | 90,031.0 | 361,811.0 | 104,632.8 | 5 | - | 1.071 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 85,801.0 | 77,080.0 | 308,441.0 | 90,268.5 | 5 | - | 1.052 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `rust_1.13.1_default-caps-simdna` | 485,631.0 | 416,722.0 | 943,203.0 | 193,987.2 | 5 | - | 0.399 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 494,041.0 | 320,731.0 | 952,853.0 | 229,229.7 | 5 | - | 0.464 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | 59,480.0 | 57,210.0 | 324,781.0 | 105,337.3 | 5 | - | 1.771 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 40,320.0 | 35,590.0 | 257,570.0 | 86,887.0 | 5 | - | 2.155 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `rust_1.13.1_default-caps-simdna` | 3,833,262.0 | 2,835,018.0 | 4,694,983.0 | 593,480.2 | 5 | - | 0.155 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 1,203,894.0 | 1,051,733.0 | 2,053,856.0 | 360,200.6 | 5 | - | 0.299 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `rust_1.13.1_default-caps-simdna` | 604,582.0 | 556,621.0 | 1,669,345.0 | 426,955.7 | 5 | - | 0.706 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 262,091.0 | 247,491.0 | 1,250,924.0 | 390,518.8 | 5 | - | 1.490 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `rust_1.13.1_default-caps-simdna` | 278,330.0 | 118,880.0 | 621,462.0 | 180,963.3 | 5 | - | 0.650 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 96,951.0 | 78,850.0 | 608,641.0 | 202,006.7 | 5 | - | 2.084 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `rust_1.13.1_default-caps-simdna` | 2,119,166.0 | 1,570,605.0 | 3,625,481.0 | 704,283.0 | 5 | - | 0.332 | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 1,351,014.0 | 1,148,633.0 | 2,135,166.0 | 394,928.2 | 5 | - | 0.292 | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `rust_1.13.1_default-caps-simdna` | 171,211.0 | 164,541.0 | 1,150,723.0 | 385,886.5 | 5 | - | 2.254 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 94,700.0 | 83,860.0 | 653,522.0 | 219,977.0 | 5 | - | 2.323 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 88,270.0 | 63,660.0 | 502,212.0 | 167,280.0 | 5 | - | 1.895 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 204,781.0 | 177,370.0 | 1,230,094.0 | 408,687.0 | 5 | - | 1.996 (max is trial 1) | compiled=5 |

