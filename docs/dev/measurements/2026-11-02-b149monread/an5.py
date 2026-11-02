# b149monread an5: stamps behind the isbn/member x2 cross-pin move; the _in >=2x short cells; floor stamps.
import sys, collections, statistics
sys.path.insert(0, "docs/dev/measurements/2026-11-02-b149monread")
from recs import *
R = {n: load(n)[0] for n in NAMES}
keys = ("engine", "req_why", "req_byte", "req_run", "vm_start_scan", "dfa_scan", "dfa_prefilter", "prefilter", "program_sha256_v3", "vm_program_bytes", "emit_bytes")
print("== compile stamps 614d45eb3 -> cb32eda28 (vm route, plain)")
for pat in ("co-luhn", "co-luhn-pass", "co-luhn-twin", "co-isbn", "co-isbn-pass", "co-isbn-twin", "co-member", "co-member-pass", "co-member-twin", "co-netstr", "floor", "cscan-onig"):
    for a in ("vm614", "vm"):
        em = R[a][1][(pat, "plain")][0]["engine_metadata"]
        print(f"  {pat:15s} {a:6s}", {k: (str(em.get(k))[:14] if k != 'req_run' else em.get(k)) for k in keys if k in em})
print("\n== _in vs default (auto): short cells where _in is >= 2x faster, by pattern")
c = collections.Counter(); sub = collections.defaultdict(list)
for k, rows in R["auto_in"][2].items():
    if k[1] != "short-subject-search": continue
    o = R["auto"][2][k]
    if o[0]["o"] == rows[0]["o"] == "matched-as-expected" and med(o) and med(rows) and med(rows) / med(o) < 0.5:
        c[k[0]] += 1; sub[k[0]].append(k[2])
print(dict(c))
for p, s in sub.items(): print("  ", p, s[:12])
em = R["auto"][1][("cscan", "plain")][0]["engine_metadata"]; print("  cscan stamps fast_frames/fast_trail/frame_capacity/trail:", em.get("fast_frames"), em.get("fast_trail"), em.get("frame_capacity"), em.get("resume_frames"), em.get("trail_frames"))
em = R["auto_in"][1][("cscan", "plain")][0]["engine_metadata"]; print("  auto_in cscan:", em.get("fast_frames"), em.get("fast_trail"), em.get("frame_capacity"), em.get("resume_frames"), em.get("trail_frames"), em.get("buffer_frames"), em.get("buffer_trail"))
print("\n== cscan compile stamps at both pins (engine, trail/frames)")
for a in ("auto614", "auto"):
    em = R[a][1][("cscan", "plain")][0]["engine_metadata"]
    print("  ", a, {k: em.get(k) for k in ("engine", "engine_sel", "fast_frames", "fast_trail", "frame_capacity", "resume_frames", "trail_frames", "resume_frame_size", "trail_frame_size", "emit_bytes", "vm_program_bytes", "abi")})
