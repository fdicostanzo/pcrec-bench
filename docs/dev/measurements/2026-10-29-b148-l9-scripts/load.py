# [B148] L9 read (lane b148l9read, 2026-10-29): analysis helper over the SCRATCH store build/scratch-store/records/unusual@0.1; reads JSONL, no timing. Run: python3 -I is NOT used (imports its sibling).
import json,glob,os
R='/home/pcrec/projects/pcrec-bench/build/scratch-store/records/unusual@0.1'
def recs():
    for d in sorted(os.listdir(R)):
        for f in glob.glob(f'{R}/{d}/*.jsonl'):
            ls=open(f).read().splitlines()
            yield d,[json.loads(l) for l in ls]
