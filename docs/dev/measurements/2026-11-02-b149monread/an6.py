# b149monread an6: every engine_metadata key that differs 614d45eb3 -> cb32eda28 on the callout members (vm route, plain).
import sys
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
a_, b_ = load("vm614")[0], load("vm")[0]
for pat in ("co-luhn", "co-isbn", "co-isbn-twin", "co-member", "co-member-twin", "co-netstr"):
    x = a_[1][(pat, "plain")][0]["engine_metadata"]; y = b_[1][(pat, "plain")][0]["engine_metadata"]
    d = {k: (x.get(k), y.get(k)) for k in sorted(set(x) | set(y)) if x.get(k) != y.get(k) and k not in ("program_sha256", "program_sha256_v3")}
    print(pat, d)
