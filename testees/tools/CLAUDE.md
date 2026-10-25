# testees/tools/ — the TOOLS-tier adapter ([B140] step 4, lane b140tools, 2026-10-25)

Five testees that are not libraries but COMMAND-LINE TOOLS, launched fresh
per trial (`testee.invocation = "process"`, record schema v1.9). Charter:
`docs/design/subst_bench_v1.md` 3.2, 4, 8a (item 7 binding). They run only the
substitution set (`bench/subst`); `bench/capability/gen_patterns.py`'s
`EXCLUDED_TESTEES` lists all five by name.

| file | role |
|---|---|
| `tools.toml` | the PIN FILE and the testee table (read in place of a `configs.toml`; `adapter.py` overrides `Adapter.__init__`). sd and ripgrep are pinned BY BINARY SHA256 (`binary_sha256`, checked at describe/prepare/run time); sed, perl and python3 are the distro binaries pinned by the VERSION STRING they must report (a changed version is refused), their sha256 recorded live in `testee.binary`. sd 1.1.0's `--version` prints a stale `1.0.0` (`reported_version_is_stale`): never trusted, recorded as provenance |
| `adapter.py` | `describe` (process / interpretive / empty `compile_phases`), `prepare`, `compile` (writes the pattern file, returns a handle; NO compile row is recorded for a compiled case, S7/X41), `subst_support` (`count = "oracle"`), `measure_subst`. Absolute paths only, never PATH |
| `subst_py.py` | the python testee's committed script: `python3 -I subst_py.py PATTERN_FILE TEMPLATE_FILE INPUT` -> whole-file `re.sub(bytes, flags=re.ASCII)` to stdout |

| testee id | tool | command (case N; `@IN@` = acc input) | engine_version | convention |
|---|---|---|---|---|
| `sed-ere` | GNU sed | `sed -E s/PAT/REPL/g @IN@` | 4.9 | posix-leftmost-longest |
| `perl-p` | perl | `perl -pe s/PAT/REPL/g @IN@` | 5.40.1 | perl-leftmost-first |
| `python-resub` | python3 | `python3 -I subst_py.py PAT REPL @IN@` | 3.14.4 | perl-leftmost-first |
| `sd-stdin` | sd | `sd PAT REPL < @IN@` (default line-by-line) | 1.1.0 | perl-leftmost-first |
| `rg-passthru` | ripgrep | `rg --no-config --passthru -N --no-heading --color never -j1 -r REPL PAT @IN@` | 15.2.0 | perl-leftmost-first |

## What a trial is (`pcrecbench/toolrun.py`)

1. Trial 1 only: an UNTIMED correctness pass, `tool ... > out_dir/<ID>.out`
   (no sink). `substrun`'s gate hashes it against `expectations.tsv`
   (unchanged). Its size is the VALIDATED size.
2. Every trial: the TIMED launch `tool ... | wc -c`, `os.posix_spawn` with the
   pipe wired by file actions (no shell), the tool under `taskset -c N`, wc
   under `taskset -c M` (M != N and not N's SMT sibling), env `LC_ALL=C` only.
   Clock = `perf_counter_ns` from just before the tool's spawn (wc is already
   up, blocked on its read) to the second `wait4`. The input is read warm and
   `fincore` must report 100 % resident before every timed launch.
3. The SINK CHECK: wc's count must equal the validated size or the run
   raises `SinkMismatch` BY NAME and writes nothing.

`match.process` carries the argv (paths elided to `@IN@`/`@PATTERN@`/
`@TEMPLATE@`), `sink`, `sink_bytes`, both cores, user/sys CPU and maxrss from
the tool's own `wait4` rusage, and the resident fraction.

## Things that are not obvious

* The count: a tool prints no substitution count. `subst_support` says
  `count = "oracle"`, and `substrun._judge` takes `nsubst` from the
  expectation iff the output's sha256 equals the oracle's (a wrong output
  records nsubst 0, a placeholder its diagnostic says so). `truncation_check`
  is `not-applicable`: the whole-output sha256 is the evidence.
* The timed trial 1 also runs when its untimed output later fails the gate:
  one wasted launch, never a recorded timing (substrun writes no timing for a
  wrong cell).
* `--pin-cpu` gives the tool core; with none the runner picks the highest
  allowed core and a record note says so. `$PCRECBENCH_TOOLS_SINK_CPU`
  overrides the wc core.
* wc here is uutils coreutils (`/usr/bin/wc` -> cargo coreutils); its version
  and sha256 are in `build_flags`.
* Binaries under `build/tools/` are gitignored; a lane worktree finds them in
  the main checkout (`$PCRECBENCH_TOOLS_ROOT` overrides). The sha256 pin makes
  the root immaterial.
