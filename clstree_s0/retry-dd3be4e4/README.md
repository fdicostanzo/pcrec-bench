# I-120 retry, [CLS-TREE] S0 at pcrec dd3be4e4 (archive form), 2026-09-29 05:21-05:23 EDT

- Pin: dd3be4e4, recorded from the archive command.
- Compiler: gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0. Box: ubuntubudu, load
  0.03 at launch.
- `run.sh` holds the brief's commands verbatim.

| command | result | data rows (expected) | load1_at_start |
|---|---|---|---|
| b1 `make bench2` | completed | **4,620** (4,620) | 0.02 |
| `make bench2-bytes` | completed; the gate waited once ("load1 0.54 >= 0.50 -- waiting for quiet") | **132** (132) | 0.46 |
| isolated `^C`/member `bench.py` | **did not run**: `FileNotFoundError: [Errno 2] No such file or directory: 'gcc-16'` (log tail verbatim in `measc_isolated.log`) | 0 (205) | n/a (no file written) |

- **`n_atoms`.** N=4 → 5, N=16 → 16, N=32 → 29. There was no ">64
  atoms" refusal.
- **Failure lines.** There is no `BUILD FAIL`, `RUN FAIL` or
  `ANSWER MISMATCH` line in any log.
- **The failed command.** The third command, as written in the brief,
  sets no `CC=` (the first two pass `CC=gcc` to make), and this box has
  no `gcc-16` binary.
- The done-trailer `CLS-TREE-S0-TIMING DONE` was printed.
