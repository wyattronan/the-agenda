import os as _os
_R = _os.environ.get("AGENDA_ROOT") or _os.path.abspath(_os.path.join(_os.path.dirname(__file__), ".."))
import re, sys
sys.path.insert(0, _R + '/champ'); sys.path.insert(0, _R)
from links import L
from ladder import rung
BILL = re.compile(r'\b(S|H\.R|H\.J\.Res)\.\s?(\d+)(?![^()]*118th)')
KIND = {'S':'senate-bill','H.R':'house-bill','H.J.Res':'house-joint-resolution'}
# Commit counts toward championing only when it's their own move, not a vote: lead sponsorship, a pledge, a plan, a formal ask
OWN_COMMIT = re.compile(r"(?<!co)(?<!co-)\bsponsor(s|ed)?\b|\bintroduc|\bco-led\b|pledg|promis|\bvow|platform|\bplans?\b|agenda|campaign site|propos|^would\b|\b(he|she) would\b|calls for|\b(will|would) (push|fight|sign|expand|create|pass|cut|ban|veto|make|require|bring)\b|co-?wrote|\bauthored\b|\b(playbook|blueprint)\b|asked (lawmakers|the legislature|congress)|called on", re.I)

def tier(stance, ev):
    """'top' (Spend or Deliver), 'champ' (their own Commit), or None (a supporter: statements, cosponsorships, votes)."""
    if stance != 'Support': return None
    r = rung(ev, stance)
    if r in ('Spend', 'Deliver'): return 'top'
    if r == 'Commit' and OWN_COMMIT.search(ev or '') and not re.match(r'\s*(original )?co-?sponsor', ev or '', re.I): return 'champ'
    return None

def bill_url(ev):
    if not re.search(r'[Cc]osponsor|[Ss]ponsor|[Cc]o-lead', ev): return None
    m = BILL.search(ev)
    if not m: return None
    cong = '118th' if '118th' in ev[m.start():m.start()+40] else '119th'
    return (f'https://www.congress.gov/bill/{cong}-congress/{KIND[m.group(1)]}/{m.group(2)}/cosponsors',
            f'{m.group(1)}.{m.group(2)} on Congress.gov')

def build(d, fcurls=None):
    fcurls = fcurls or {}
    push = d.get('push', {})
    out = {'sen':{}, 'gov':{}, 'supn':{'sen':{}, 'gov':{}}}; stats = {'top':0,'champ':0,'support':0}
    def add(side, k, rec, t):
        if t: out[side].setdefault(k, []).append({**rec, 't': t}); stats[t] += 1
    for s in d['sen']:
        if s['n'].startswith('TBD') or 'ppoint' in s['id']: continue
        for k,(stance,ev) in s['r'].items():
            if stance not in ('Support','Lean support'): continue
            t = tier(stance, ev)
            if not t:
                out['supn']['sen'][k] = out['supn']['sen'].get(k, 0) + 1; stats['support'] += 1; continue
            link = L.get((s['n'],k)) or bill_url(ev) or ((fcurls[('sen',s['n'],k)], 'Source') if ('sen',s['n'],k) in fcurls else None)
            pty = 'I' if s['p']=='D' and s['pl'].startswith('I') else s['p']
            add('sen', k, {'n':s['n'],'p':pty,'st':s['st'],'u':link[0] if link else None,'src':link[1] if link else None,'ev':ev,'new':s['new']}, t)
    for g in d['gov']:
        P = push.get('gov:' + g['st'], {})
        for k,(stance,ev) in g['sp'].items():
            t = tier(stance, ev)
            if k in P:   # a national push can lift them
                tp = tier(P[k][0], P[k][1])
                if tp == 'top' or (tp and not t): t, ev = tp, P[k][1]
            if not t:
                if stance in ('Support','Lean support'):
                    out['supn']['gov'][k] = out['supn']['gov'].get(k, 0) + 1; stats['support'] += 1
                continue
            link = L.get((g['n'],k)) or ((fcurls[('gov',g['n'],k)], 'Source') if ('gov',g['n'],k) in fcurls else None)
            add('gov', k, {'n':g['n'],'p':g['p'],'st':g['st'],'u':link[0] if link else None,'src':link[1] if link else None,'ev':ev}, t)
    for side in ('sen','gov'):
        for k in out[side]: out[side][k].sort(key=lambda c:(c['t']!='top', c['u'] is None, c['st']))
    return out, stats
