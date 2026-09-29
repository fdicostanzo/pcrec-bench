# testees/pcrec/findings/email/ — the email PROFILED bundle (prose only)

[B115] (inbox I-118, outbox O-72 Q4). No shipped bundle (`weblog`/`log`)
fits `bench/email`'s shape — both are log-line corpora, unrelated to RFC
5322 addresses in prose — so DECLARED is **n/a** here in this pass; only
PROFILED, and only on the generated-prose throughput pair, is built.

## Why only t-d/t-e

`bench/email`'s 85 short subjects are HAND-CURATED (copied verbatim from
pcrec's srEmail specimen) — not draws from a class, so a train/test split
would split a test LIST rather than sample one; PROFILED is n/a there.
Of the five throughput subjects, `t-a-valid-addrs`/`t-b-no-at`/
`t-c-long-atom-run` are fixed constants (no seed moves them at all — see
`disjointness.tsv`'s three `sha256_overlap=1` control rows). Only
`t-d-prose-sparse-addrs`/`t-e-prose-no-at` come from a seeded generator
(`random.Random(GEN_SEED)`), so only they have a TRAIN/TEST split.

## PROFILED: `email-prose-profiled.rxt`

```
python3 bench/email/gen_throughput_subjects.py --seed 20261001 --out /var/tmp/b115/email-train
cat .../t-d-prose-sparse-addrs.bin .../t-e-prose-no-at.bin > prose-corpus.bin   # 2,097,152 B
build/pcrec-f7f5a143/build/pcrec-analyze --name email-prose-profiled \
    --retrieved 2026-09-28 --scan freq \
    --source "bench/email TRAIN generation (gen_throughput_subjects.py --seed 20261001, t-d/t-e prose pair only)" \
    --license "N/A (synthetic, generated in-repo)" \
    prose-corpus.bin > email-prose-profiled.rxt
```

`disjointness.tsv`: t-d/t-e's TRAIN bytes share **0 of 2** sha256 digests
with the committed `manifest_throughput.tsv` rows for the same ids (the
other three ids' digests are, as expected, IDENTICAL under the new seed —
the control that `--seed` cannot move a hand-curated subject).
`build_prose` (`bench/email/gen_throughput_subjects.py`) opens no file and
draws only from `VOCAB`/`VALID_ADDRS`, two fixed in-file lists, so there is
no corpus to grep for a bench path either.

`list_analysis_email-prose-profiled.tsv` is `pcrec --list-analysis
email-prose-profiled -I testees/pcrec/findings/email` archived verbatim —
digest `8f0dbb8b882ee447`, cross-checked live by
`tools/selfcheck.py:check_b115_tune_analysis_axis`'s sibling assertion for
loglines (the same shape; email is not asserted a second time there since
one real-compile witness per mechanism is what that check proves).

## The prerequisite

Same as `testees/pcrec/findings/loglines/README.md`'s: built by
`build/pcrec-f7f5a143` (git f7f5a1432d1d2cf464f3f15fd268cdf11428d0d5, abi
44), never a re-pin of `configs.toml`'s `a32bc86e`.
