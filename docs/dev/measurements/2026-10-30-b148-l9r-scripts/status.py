# [B148] L9 re-run read (lane b148l9rread): per-record status, pre-flight and target-core readings, trial agreement. Run: python3 status.py
import sys,os,statistics as st; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from load import *
print('| testee | run | status | load1 b/a | pre busiest other (cpu) / target | after busiest / target | tl median max_other | agreement | status_detail |')
print('|---|---|---|---|---|---|---|---|---|')
for tid,new,rs in recs():
    h=rs[0]; e=h['environment']; o=e['occupancy']; b=o['before']; a=o.get('after') or {}
    tl=[x['max_other_busy_pct'] for x in o.get('timeline',[])]
    ta=h['trial_agreement']
    print('| %s | %s | %s | %.2f/%.2f | %s / %s | %s / %s | %s | %s (%d dis. groups of %d) | %s |'%(tid.replace('_caps-simdna','').replace('-simdna',''),'RERUN' if new else 'L9',h['status'],e['load']['before']['load1'],(e['load'].get('after') or {}).get('load1',-1),b.get('max_busy_pct'),b.get('target_busy_pct'),a.get('max_busy_pct','-'),a.get('target_busy_pct','-'),'%.2f'%st.median(tl) if tl else '-',ta['verdict'],ta['groups_disagreeing'],ta['groups_judged'],(h.get('status_detail') or '')[:260].replace('|','/')))
