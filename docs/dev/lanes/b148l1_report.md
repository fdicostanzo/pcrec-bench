# Lane b148l1 — [B148] L1: record schema v1.11 and the shared code for the unusual set

Lane b148l1, branch `lane/b148l1`, 2026-10-27. Tier: code + checks. No
timing. ~/pcrec read only (one `--list-source` probe at 614d45eb3, run to
confirm that the `.rxt` tag key `twin_of` is accepted). Source:
docs/design/unusual_set_v1.md v0.2 §10 L1, §7.2, §7.4, §7.5, §5.5, §6.4;
r9 review C2/C3/C10 and the -schema S-2..S-5, S-10, S-11, S-14 findings.

## Charter vs committed

| charter item | committed | where |
|---|---|---|
| regime `call-stream` | yes: schema enum, `subbench.REGIME_TO_ENUM`/`REGIME_MODE` (`calls`) | `schema/record.schema.json`, `pcrecbench/subbench.py` |
| `match_row.stream` {calls, segment_bytes, matched, nomatch, refused, gave_up, results_sha256} | yes, with optional `first_limit` (X49 has to name the limit, so the row carries it) | schema |
| `testee.assist` {assist_version, members[{member,tokens,lines,sha256}]} | yes | schema |
| `trial_agreement.rule` `v1.11-group` | yes; reduce.py AND validate.py each read their own `ONE_ITERATION_REGIMES` table (rule -> regimes timed at `iterations >= 1`), no shared source | `pcrecbench/reduce.py`, `schema/validate.py` |
| X47-X53, each with a negative example | yes, 13 sabotages, generated | `schema/examples/gen_example_111.py`, `bad/x47-*..x53-*` |
| history entry | yes: the schema `$comment`, the record_schema.md version table + the 1.10→1.11 paragraph, a new §6.13, FIELD TABLE rows, §9 rows | `docs/design/record_schema.md` |
| X32 text / gate_shape | §3.8 `v1.11-group` (template: §3.7) + a checks-table row | `docs/design/gate_shape_v14.md` |
| 1.10 records still validate | yes: every committed example and sabotage; the whole store too (see below) | — |
| `REQUIRES_VOCAB` `vars`, `unusual-<member>` | yes: `vars` added; `unusual-<member>` is a PREFIX FAMILY (`is_requires_token`); plus the NOT-CAPABLE `declaration_ref` spelling helpers | `pcrecbench/capability.py` |
| `twin_of` pattern tag | yes: flat `twin_of-<id>`, `subbench.twin_groups()` checked at load, refusals by name | `pcrecbench/subbench.py` |
| record-fit check for §6.4's integers | `check_unusual_record_fit` (2^40 and 2^53-1 `deep_mem_bytes`, `callout_fires`, `callees_sha256`, `assist_deferred_compile`: each validates and reads back exactly; X52 controls) | `tools/selfcheck.py` |
| reader skip tables | `reduce.SET_GRAIN_SKIP_REGIMES` + `set_grain_rows`, read by viewer_export, trend digest and frontpage; report.py refuses a call-stream-only selection by name and drops the stream rows from a mixed record (with a header count printed only when > 0) | `tools/*.py`, `pcrecbench/report.py` |
| `--grain stream` view | NOT built (it belongs to L4/L5 under §7.5) | — |
| harness guard | `harness.CALL_STREAM_PENDING`: a call-stream cell is refused by name until L4 | `pcrecbench/harness.py` |

## X-rule table

| rule | statement (as implemented) | negatives |
|---|---|---|
| X47 | `stream` present iff `regime = call-stream`; both the regime and the field are refused below 1.11 | `x47-stream-absent-on-call-stream-row`, `x47-stream-on-other-regime`, `x47-call-stream-on-110-record` |
| X48 | `calls = matched + nomatch + refused + gave_up` | `x48-stream-counts-off-by-one` |
| X49 | `gave-up` iff `gave_up > 0`; `first_limit` iff `gave_up > 0`; the diagnostic contains `first_limit` | `x49-gave-up-count-but-matched`, `x49-diagnostic-does-not-name-limit` |
| X50 | `testee.assist` iff `config_extra` carries `assist-v<NN>`; the versions are equal; members are unique; refused below 1.11 | `x50-assist-token-without-object`, `x50-assist-duplicate-member` |
| X51 | `v1.11-group` only at >= 1.11 (checked before X32's pairing) | `x51-v111-group-on-110-record` |
| X52 (>= 1.11) | `deep_mem_bytes` iff `deep_mem_method`; method in {canary, counting-alloc, mincore, rss-delta} | `x52-deep-mem-bytes-without-method`, `x52-deep-mem-method-unknown` |
| X53 | `segment_bytes > 0`; `refused > 0` only on a pattern tagged `requires-vars` | `x53-refused-on-a-non-vars-pattern`, `x53-segment-bytes-zero` |

## Checks

- `make check-schema`: 12 examples accepted, 104 sabotages rejected for the
  intended rule, 0 wrong (91 before the lane). `check_fields` and
  `check_rules` pass, and gen_example_14/110/ident110/111 all reproduce.
- The new selfcheck functions run directly, together with the two existing
  trial-agreement fixtures: 41/41 PASS.
- `pcrecbench/tests/test_report.py`: 111 passed, 0 failed (+1:
  `test_call_stream_skipped_by_set_grain_b148`).
- `tools/tests/test_frontpage.py`: 44 PASS. `test_trend.py`: ALL PASS.
- **OWED (manager launches, BOILERPLATE "long runs"):**
  1. Full `make check`, cwd `/home/pcrec/projects/pcrec-bench/worktrees/b148l1`:
     `setsid gnutimeout 5400 make check > /var/tmp/pcrecbench/b148l1/make_check.log 2>&1; echo "DONE rc=$?" >> /var/tmp/pcrecbench/b148l1/make_check.log`
     (the marker is the `DONE rc=` line). The email quick-cell check is load-sensitive.
  2. Whole-store validation (631 records, 3.8 GB, about 10+ min, detached):
     `setsid nice gnutimeout 3000 python3 -u /var/tmp/pcrecbench/b148l1/val_store.py /home/pcrec/projects/pcrec-bench/worktrees/b148l1 > /var/tmp/pcrecbench/b148l1/val_store.log 2>&1; echo "DONE rc=$?" >> /var/tmp/pcrecbench/b148l1/val_store.log`
     The last line should read `files 631 invalid 0 ...`. The lane's own run was
     stopped unfinished (rc=143) so that it could be handed off. Its output was
     buffered, so it yields no verdict.

## Findings and proposals

1. **The `requires=<feature>` spelling.** The note writes this tag. The
   loader flattens `tag key=value` to `key-value`, so the existing
   `requires-<token>` tags are already the spelling. Nothing new was added.
2. **§6.4 "beside the process maxrss_kb".** `match_row.process` is scoped by
   X38 to process testees. A LIBRARY testee's high-water maxrss has to be
   an engine_metadata integer (for example `deep_maxrss_kb`). The note
   needs a one-line amendment.
3. **X53 extra clause (proposal, not implemented).**
   `timing.bytes_processed = segment_bytes * iterations` would tie the
   throughput denominator to the stream. It is left for Frank/L4 because
   the harness's bytes accounting for `--mode calls` is L4's.
4. **Version gating** of the new regime and fields is folded into X47 and
   X50. No extra rule number was used.
5. `CALL_STREAM_PENDING` is the switch L4 flips. L4 must remove it, and
   replace `check_call_stream_readers`'s harness arm with a real cell.
