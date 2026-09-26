# SCRATCH-ORIGIN sizing model ([B77] U5, archived with
# 2026-09-25-b77u5-validate-once-probe.txt), NOT an oracle: it counts find-all
# calls (using PCRE2_NO_UTF_CHECK only to count them cheaply) and models the
# bytes libpcre2 would re-validate per call under utf8_set_v1.md 8.2 as
# originally written. Run from the repo root.
import sys, time
sys.path.insert(0, '.')
from pcrecbench import oracle_pcre2 as o
from pcrecbench.subbench import load
from pcrecbench.expectations import oracle_option_word
sb = load('bench/utf8')
NOCHK = 0x40000000
subs = [(s.subject_id, sb.subject_bytes(s.subject_id)) for s in sb.subjects_for('throughput')]
tot = 0
for p in sb.patterns:
    try:
        rx = o.compile(sb.pattern_bytes(p.name), oracle_option_word(sb, p))
    except o.Pcre2Error as e:
        print(p.name, 'COMPILE-REFUSED', e); continue
    row = []; pc = 0
    for sid, b in subs:
        n = len(b); pos = 0; calls = 0; vb = 0
        while pos <= n:
            calls += 1; vb += n - pos
            got = o._search_raw(rx, b, pos, NOCHK)
            if got is None: break
            (s, e), _ = got
            pos = e if e > s else o.next_start(b, s, True)
        c = calls*5e-6 + vb/0.68e9
        pc += c; row.append('%s:%d/%.1fs' % (sid, calls, c))
    tot += pc
    print('%-22s %8.1fs  %s' % (p.name, pc, ' '.join(row)), flush=True)
print('TOTAL model s', tot)
