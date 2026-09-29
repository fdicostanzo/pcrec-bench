# [B116] / inbox I-119: [CLS-TREE] S0 timing session. Returned REFUSED, twice.

- Pin: da0ae4435c1ab97e7f5ac6cbe59cdece78c84c72, from `git -C ~/pcrec archive da0ae443`
  extracted into /var/tmp/clstree_s0/pcrec. There is no ~/pcrec worktree
  (O-73, confirmed by pcrecdev1).
- Compiler: gcc (Ubuntu 15.2.0-16ubuntu1) 15.2.0. Box: ubuntubudu.
- `run.sh` holds the brief's commands, run verbatim, minus the `git log -1`
  line, plus a pre-wait for low load before the first command.

| attempt | start (EDT) | pre-wait load | bench2.tsv `load1_at_start` | bench2 result | bench2-bytes | capC isolated |
|---|---|---|---|---|---|---|
| 1 | 05:00 | 0.22 0.48 0.77 | 0.22 | REFUSING mid-run, load1 0.61; 1,157 lines written | REFUSING, load1 0.61 | REFUSING, load1 0.61 |
| 2 | 05:05 | 0.07 0.27 0.59 | 0.07 | REFUSING mid-run, load1 0.52; 3,852 lines written | REFUSING, load1 0.52 | REFUSING, load1 0.52 |

- **Attempt 1.** It overlapped the tail of our own [B115] sweep's load
  and some reads we ran on the box. Attempt 2 had nothing else of ours
  running.
- **Row counts.** The expected counts were 4,620 / 132 / 205 data rows.
  Neither attempt reached any of them. No `BUILD FAIL`, `RUN FAIL` or
  `ANSWER MISMATCH` line appears in any log.
- **Contents.** Both attempts' `session.out`, the three
  `build/clstree_s0/*.log` files, and the partial `bench2.tsv` are here.
  No `bench2_bytes.tsv` or `capC_isolated.tsv` was produced.
