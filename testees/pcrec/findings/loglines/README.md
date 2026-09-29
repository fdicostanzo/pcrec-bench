# testees/pcrec/findings/loglines/ — the loglines DECLARED/PROFILED bundles

[B115] (inbox I-118, outbox O-72). Everything here supports the scratch-tier
FINDINGS-BENCH-TIERS sweep over `bench/loglines`; nothing here is read by any
pinned config or by `store/` — R-BENCH-4 keeps anything pcrec-shaped out of
`bench/`, and this project's own [B31] ruling puts it here instead.

## DECLARED: pcrec's two shipped bundles

`weblog` (1 MB of real Apache combined-format request lines,
`elastic/examples`, Apache-2.0) and `log` (999,960 B of a SYNTHESIZED
Hadoop-DataNode-shaped corpus) are pcrec's own, built into `libpcrec` — no
bundle authored here. `list_analysis_weblog.tsv` / `list_analysis_log.tsv`
are `pcrec --list-analysis <name>` archived verbatim (pcrec D35's stable-name
convention).

**Disjointness proof** (docs/spec/findings.md §6's own two provenance
lines, grepped for a bench path):

```
$ grep -i "bench/loglines\|bench/email\|pcrec-bench" \
    list_analysis_weblog.tsv list_analysis_log.tsv
NO MATCH
```

`weblog`'s provenance names `elastic-examples-apache-logs-bc53b584`
(a GitHub URL + git ref); `log`'s names `synth-log-lines-v1` (a
`fidelity synthesized` corpus, MIT). Neither is bench/loglines-shaped by
construction, and `bench/loglines/logtext.py` (the generator both TRAIN and
committed subjects come from) opens no file at all — there is no corpus for
either shipped bundle to have touched, and no corpus for a TRAIN split to
have leaked from.

## PROFILED: `loglines-profiled.rxt`

Built from a TRAIN generation (never committed — only this `.rxt` is):

```
python3 bench/loglines/gen_subjects.py --seed 20260930 --out /var/tmp/b115/loglines-train/search
python3 bench/loglines/gen_throughput_subjects.py --seed 20260931 --out /var/tmp/b115/loglines-train/throughput
cat .../search/*.bin .../throughput/*.bin > corpus.bin        # 4,341,004 B
build/pcrec-f7f5a143/build/pcrec-analyze --name loglines-profiled \
    --retrieved 2026-09-28 --scan freq \
    --source "bench/loglines TRAIN generation (gen_subjects.py --seed 20260930, gen_throughput_subjects.py --seed 20260931)" \
    --license "N/A (synthetic, generated in-repo)" \
    corpus.bin > loglines-profiled.rxt
```

`disjointness.tsv` is the sha256-level proof: **0 of 124 TRAIN subject
digests** appear in either committed manifest (`bench/loglines/manifest.tsv`,
`manifest_throughput.tsv`). The LINE-level overlap (provenance only, per
outbox O-72 Q1 — short syslog-shaped lines from one grammar can repeat by
chance, and real logs repeat too, so this is never a gate): of 1,840 TRAIN
search-band lines, **0** also appear among the 1,846 committed lines, at
this seed pair.

`list_analysis_loglines-profiled.tsv` is `pcrec --list-analysis
loglines-profiled -I testees/pcrec/findings/loglines` archived verbatim —
the digest it names (`b39463706bb39c9e`) is the one a compile's
`<PREFIX>_FINDINGS` stamp carries under `-I testees/pcrec/findings/loglines
--analysis loglines-profiled`, cross-checked live by
`tools/selfcheck.py:check_b115_tune_analysis_axis`.

## The prerequisite: a scratch-tier pcrec, not a re-pin

Every listing here was produced by `build/pcrec-f7f5a143` (git commit
`f7f5a1432d1d2cf464f3f15fd268cdf11428d0d5`, abi 44, post-[FINDINGS] B6),
built the way `pin.sh` builds any commit (`testees/pcrec/pin.sh f7f5a143`) —
NOT this project's pinned commit (`configs.toml`'s `a32bc86e`, abi 41, which
predates `--analysis`/`-I`/`pcrec-analyze` entirely). `pcrec-local` is
pointed at this binary via `$PCREC_BIN` for every DECLARED/PROFILED/
ORACLE-BEST arm; `scripts/findings_tiers.sh` does this for the whole sweep.
