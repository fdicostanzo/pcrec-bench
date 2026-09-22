#!/usr/bin/env python3
"""[B71] P1/P2 scoring: fresh 2026-09-22 capability@0.1 records vs each
testee's newest prior record. Reads store/index.tsv + record files.
Source: session 29 collection ritual; predictions = plan.md [B71] row."""
import json, csv, sys, collections

STORE = 'store'
CASE1 = {'wild-codegrammar-json-number-extended',
         'wild-codegrammar-json-stringcontent-escape'}

idx = list(csv.DictReader(open(f'{STORE}/index.tsv'), delimiter='\t'))
cap = [r for r in idx if r['subbench'] == 'capability' and r['version'] == '0.1']
fresh = {r['testee_id']: r for r in cap if r['timestamp'].startswith('2026-09-22')}
prior = {}
for r in cap:
    if r['timestamp'].startswith('2026-09-22') or r['status'] != 'measured':
        continue
    t = r['testee_id']
    if t in fresh and (t not in prior or r['timestamp'] > prior[t]['timestamp']):
        prior[t] = r

def load(path):
    """(pattern, form) -> dict(outcome, emit, artifact_bytes); form '' = plain.
    Also returns free-spacing pattern ids (canonical_text with (?x or (?..x)."""
    rows = [json.loads(l) for l in open(f'{STORE}/{path}').read().splitlines()]
    comp = {}
    freesp = set()
    for p in rows[0].get('patterns', []):
        txt = p.get('canonical_text') or ''
        if '(?x' in txt or '(?mx' in txt or '(?sx' in txt or '(?ix' in txt:
            freesp.add(p['pattern_id'])
    for r in rows[1:]:
        if r.get('kind') != 'compile':
            continue
        key = (r['pattern_id'], r.get('form') or 'plain')
        em = r.get('engine_metadata') or {}
        val = (r['compile_outcome'], em.get('emit_bytes'), r.get('artifact_bytes'))
        if key in comp and comp[key] != val:
            print(f'  TRIAL DISAGREEMENT {path} {key}: {comp[key]} vs {val}')
        comp[key] = val
    return comp, freesp

p1_fail, p2_out_fail, p2_emit = [], [], []
for t in sorted(fresh):
    if t not in prior:
        print(f'{t}: NO PRIOR RECORD'); continue
    f_comp, f_free = load(fresh[t]['path'])
    p_comp, _ = load(prior[t]['path'])
    print(f'== {t}')
    print(f'   fresh {fresh[t]["timestamp"]}  prior {prior[t]["timestamp"]} ({prior[t]["path"].split("/")[-1][:60]}...)')
    # P1: CASE-1 whole-subject compiles wherever plain compiles; prior refused
    for pat in sorted(CASE1):
        pl = f_comp.get((pat, 'plain'))
        wh = f_comp.get((pat, 'whole-subject'))
        pw = p_comp.get((pat, 'whole-subject'))
        line = f'   P1 {pat}: plain={pl and pl[0]} whole={wh and wh[0]} prior_whole={pw and pw[0]}'
        print(line)
        if pl and pl[0] == 'compiled' and (not wh or wh[0] != 'compiled'):
            p1_fail.append((t, pat, wh))
    # P2: every other (pattern, form) outcome unchanged; emit moves only on
    # free-spacing whole-subject artifacts
    keys = set(f_comp) | set(p_comp)
    for k in sorted(keys):
        pat, form = k
        if pat in CASE1 and form == 'whole-subject':
            continue  # P1's own cells
        fo, po = f_comp.get(k), p_comp.get(k)
        if fo is None or po is None:
            p2_out_fail.append((t, k, 'row-present-mismatch', fo, po)); continue
        if fo[0] != po[0]:
            p2_out_fail.append((t, k, 'outcome', po[0], fo[0]))
        elif fo[1] != po[1]:
            allowed = (pat in f_free and form == 'whole-subject')
            p2_emit.append((t, k, po[1], fo[1], 'ALLOWED' if allowed else 'VIOLATION'))
    print(f'   free-spacing patterns detected: {sorted(f_free)}')

print('\n==== P1 verdict:', 'CONFIRMED' if not p1_fail else f'REFUTED {p1_fail}')
print('==== P2 outcome verdict:', 'CONFIRMED (all outcomes unchanged)' if not p2_out_fail else 'REFUTED:')
for x in p2_out_fail: print('   ', x)
print('==== P2 emit movers:')
for x in p2_emit: print('   ', x)
viol = [x for x in p2_emit if x[4] == 'VIOLATION']
print('==== P2 emit verdict:', 'CONFIRMED (movers confined to free-spacing whole-subject)' if not viol else f'REFUTED: {viol}')
