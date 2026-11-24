#!/bin/bash
# run from the worktree root; interprets all 8 groups (no predictions file matches these set versions: verified by ls docs/dev/predictions)
set -u
for g in altwide-0.3-ryzen7700x-fullroster capability-0.4-ryzen7700x syntax-0.2-ryzen7700x bounded-0.3-ryzen7700x loglines-0.1-ryzen7700x email-specimen-0.2-ryzen7700x litrun-0.1-ryzen7700x sentinel-0.1-ryzen7700x; do
  n=2026-11-24-$g-d6c5e71a5
  sg=""; [ -f reports/$n.subject-grain.tsv ] && sg="--subject-grain reports/$n.subject-grain.tsv"
  python3 -m pcrecbench interpret reports/$n.tsv --index store/index.tsv $sg --render --out reports/$n.interpretation.md || echo "FAIL $n"
  python3 -m pcrecbench interpret reports/$n.tsv --index store/index.tsv $sg --render | cmp - reports/$n.interpretation.md && echo "CMP_OK $n"
done
echo "DONE"
