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

## The third command re-run (pcrecdev1's exact command, 2026-09-29 05:24 EDT)

`CC=gcc gnutimeout 600 python3 studies/cls_tree_study/bench.py --population k53 --sets '^C' --regimes member --lams 0,16,256 --rounds 41 --out capC_isolated.tsv`
→ **205 / 205 data rows**, `load1_at_start=0.21`. There is no
`BUILD FAIL` / `RUN FAIL` / `ANSWER MISMATCH` line. The log is
`measc_isolated.rerun.log`; the original `measc_isolated.log` (the
`gcc-16` failure) is kept.

One disclosed setup step: /var/tmp/clstree_s0 had been deleted after the
first retry, so the tree was re-extracted from the same
`git -C ~/pcrec archive dd3be4e4`. The first attempt at the command in
the fresh tree failed on a missing `studies/cls_tree_study/discover`
binary, which the earlier `make bench2` had built in the deleted tree.
`make -C studies/cls_tree_study discover CC=gcc` rebuilt it
(`gcc -O2 -std=gnu11 -Wall -Wextra discover.c -o discover -lm`, a build
only, no timing), and then the command ran verbatim.
