import os as _os
_R = _os.environ.get("AGENDA_ROOT") or _os.path.abspath(_os.path.join(_os.path.dirname(__file__), "../.."))
"""Merge polling agent outputs (fc/polls/out/*.json) into a compact per-measure structure.

For each measure and state: keep up to 3 polls, ranked by reputability tier (1 best),
then direct state/multistate polls ahead of modeled estimates, then most recent;
the state's number is the plain average of their support figures.
"""
import json, glob, os, re

STATES = set("AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY".split())
TYPES = {'state': 0, 'multistate': 0, 'modeled': 1, 'national': 2}

def _num(x):
    try:
        v = float(x)
        return v if 0 <= v <= 100 else None
    except (TypeError, ValueError):
        return None

def _date(s):
    m = re.match(r'(\d{4})(?:-(\d{1,2}))?', str(s or ''))
    return (int(m.group(1)), int(m.group(2) or 6)) if m else (0, 0)

def build(valid_keys, src=_R + '/fc/polls/out', log=True):
    rows, seen, bad = [], set(), 0
    try: EXC = {e['url'] for e in json.load(open(os.path.join(os.path.dirname(src), 'exclude.json')))}
    except Exception: EXC = set()
    for f in sorted(glob.glob(os.path.join(src, '*.json'))):
        try:
            data = json.load(open(f))
        except Exception as e:
            print('polls: bad json', os.path.basename(f), e); continue
        for r in data if isinstance(data, list) else []:
            url = (r.get('url') or '').strip()
            if url in EXC: bad += 1; continue
            if not url.startswith('http'):
                bad += 1; continue
            keys = [k for k in (r.get('keys') or []) if k in valid_keys]
            if not keys:
                bad += 1; continue
            states = {}
            for st, v in (r.get('states') or {}).items():
                st = st.upper().strip()
                if st not in STATES or not isinstance(v, dict): continue
                sup = _num(v.get('sup'))
                if sup is None: continue
                opp = _num(v.get('opp'))
                states[st] = (round(sup), None if opp is None else round(opp))
            nat = r.get('national') if isinstance(r.get('national'), dict) else None
            if nat and _num(nat.get('sup')) is None: nat = None
            if not states and not nat:
                bad += 1; continue
            sig = (url, tuple(sorted(keys)), r.get('question', '')[:60], tuple(sorted(states.items())))
            if sig in seen: continue
            seen.add(sig)
            typ = r.get('type') if r.get('type') in TYPES else 'state'
            tier = r.get('tier') if r.get('tier') in (1, 2, 3) else 3
            rows.append(dict(keys=keys, states=states, nat=nat, typ=typ, tier=tier, url=url,
                             who=(r.get('pollster') or '').strip()[:60],
                             spon=(r.get('sponsor') or '').strip()[:60],
                             date=str(r.get('fielded') or '')[:7], n=r.get('n'),
                             q=(r.get('question') or '').strip()[:160],
                             match=r.get('match') if r.get('match') in ('bill', 'concept') else 'concept',
                             note=(r.get('note') or '').strip()[:200]))
    out = {}
    for k in valid_keys:
        mine = [r for r in rows if k in r['keys']]
        if not mine: continue
        polls, idx = [], {}
        def pid(r):
            i = id(r)
            if i not in idx:
                idx[i] = len(polls)
                p = {'w': r['who'], 'd': r['date'], 't': r['typ'], 'r': r['tier'], 'q': r['q'],
                     'u': r['url'], 'm': r['match']}
                if r['spon']: p['s'] = r['spon']
                if r['n']: p['n'] = r['n']
                if r['note']: p['x'] = r['note']
                if r['nat']:
                    p['nat'] = [round(_num(r['nat']['sup'])),
                                None if _num(r['nat'].get('opp')) is None else round(_num(r['nat']['opp']))]
                polls.append(p)
            return idx[i]
        states = {}
        for st in sorted(STATES):
            cand = [r for r in mine if st in r['states']]
            if not cand: continue
            cand.sort(key=lambda r: (r['tier'], TYPES[r['typ']], tuple(-x for x in _date(r['date']))))
            top, urls = [], set()
            for r in cand:
                sv = (r['who'].lower(), r['date'])     # same pollster + same month = same survey
                if r['url'] in urls or (r['date'] and sv in urls): continue   # one survey counts once per state
                urls.add(r['url']); urls.add(sv); top.append(r)
                if len(top) == 3: break
            sups = [r['states'][st][0] for r in top]
            states[st] = {'a': round(sum(sups) / len(sups)),
                          'i': [[pid(r), r['states'][st][0], r['states'][st][1]] for r in top]}
        for r in mine:
            if r['nat']: pid(r)
        out[k] = {'p': polls, 's': states}
    if log:
        cov = {k: len(v['s']) for k, v in out.items()}
        print('polls: rows', len(rows), 'rejected', bad, 'measures', len(out),
              'states covered (median)', sorted(cov.values())[len(cov)//2] if cov else 0)
    return out
