#!/usr/bin/env python3
"""[B132] condensed layout facts from 2026-10-09-b132-layout-facts.sh's output
(argv[1]): per artifact and arm: .text size, .text file offset/align, the
artifact's rx_search address (mod 64 / 4096) and size, the shim's pb_search and
pb_match_caps (the per-call wrappers the driver calls) address mod 64/4096, and
the first LOAD R E segment. Run: python3 this.py layout.txt"""
import re, sys
cur = None; D = {}
for l in open(sys.argv[1]):
    if l.startswith("###"):
        p = l.split(); cur = (p[1], p[2], p[3]); D[cur] = {"fn": {}}
    elif cur:
        m = re.match(r"\s+size -A: \.text\s+(\d+)\s+(\d+)", l)
        if m: D[cur]["text"] = int(m.group(1))
        m = re.match(r"\s+\.text hdr:.*PROGBITS\s+(\w+) (\w+) (\w+) \d+\s+AX\s+\d+\s+\d+\s+(\d+)", l)
        if m: D[cur]["texthdr"] = (m.group(2), m.group(4))
        m = re.match(r"\s+fn (\S+)\s+addr=(0x[0-9a-f]+) size=(\d+) mod64=(\d+) mod4096=(\d+)", l)
        if m: D[cur]["fn"][m.group(1)] = (m.group(2), int(m.group(3)), int(m.group(4)), int(m.group(5)))
print("%-7s %-44s | .text O->N | rx_search addr (O==N?) mod64 | pb_search O: addr mod64 mod4096 -> N | pb_match_caps O -> N" % ("cfg", "pattern"))
for (c, p, a) in D:
    if a != "OLD" or (c, p, "NEW") not in D: continue
    o, n = D[(c, p, "OLD")], D[(c, p, "NEW")]
    f = lambda d, k: d["fn"].get(k)
    rs_o, rs_n = f(o, "rx_search"), f(n, "rx_search")
    ps_o, ps_n, mc_o, mc_n = f(o, "pb_search"), f(n, "pb_search"), f(o, "pb_match_caps"), f(n, "pb_match_caps")
    print("%-7s %-44s | %d->%d (+%d) | %s %s mod64=%d | %s m64=%d m4096=%d -> %s m64=%d m4096=%d | m64=%d -> %d" % (
        c, p, o["text"], n["text"], n["text"] - o["text"], rs_o[0], "same" if rs_o == rs_n else "DIFFER", rs_o[2],
        ps_o[0], ps_o[2], ps_o[3], ps_n[0], ps_n[2], ps_n[3], mc_o[2], mc_n[2]))
