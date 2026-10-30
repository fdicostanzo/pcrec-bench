# [B148] L9 re-run read (lane b148l9rread, 2026-10-30): analysis helper over the SCRATCH store build/scratch-store/records/unusual@0.1 (main tree); reads JSONL, no timing. Both the L9 (2026-10-28/29) and the re-run (2026-10-29T23:33Z onward) records are present; NEW = timestamp >= RERUN_FROM.
import json,glob,os
R='/home/pcrec/projects/pcrec-bench/build/scratch-store/records/unusual@0.1'
RERUN_FROM='20261029T233000Z'
def recs():
    """yield (tid, is_new, [header, rows...]) for every record"""
    for d in sorted(os.listdir(R)):
        for f in sorted(glob.glob(f'{R}/{d}/*.jsonl')):
            ls=open(f).read().splitlines()
            ts=f.rsplit('__',1)[1].split('.')[0]
            yield d,ts>=RERUN_FROM,[json.loads(l) for l in ls]
