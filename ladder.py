"""Getting Stuff Done: the five-rung ladder.
Talk (10) -> Commit (25) -> Spend (50) -> Deliver (100) per issue, at the highest rung the evidence reaches
(leans earn half). Ladder = average points over the issues counted, scaled so the best record in the group sets 90
(so nobody reaches 100; the most anyone can total is 92.5).
Total = 75% ladder + 25% Steward (home-state rankings). Built from the site's own research notes."""
import re
from ladder_own import OWN, DEF_OWN

PTS = {'Talk': 10, 'Commit': 25, 'Spend': 50, 'Deliver': 100}
W_LADDER, W_STEWARD, LEAN = .75, .25, .5
# the best ladder record in each group sets 90, not 100: high marks for the leaders, room to improve for everyone
CEIL = 90
RUNGS = ['Deliver', 'Spend', 'Commit', 'Talk']

DELIVER = (r"(?<!co-)\bsign(ed|s|ing)\b(?![^;]{0,45}\b(statement|letter|pledge|petition|onto|discharge|executive order)s?\b)"
           r"|\benacted\b|tie-breaking vote|\berased\b|quadrupl"
           r"|(^|; )(created|established|eliminated|launched|expanded|cut)\b")
SPEND = (r"(^|; |, and |\band |\b(he|she) )vetoe?[ds]?\b|\bveto(ed|es)? (of )?(a|an|the|bills?|HB|SB|legislation)\b|\bsu(ed|es|ing)\b|lawsuit"
         r"|\bforc(ed|ing)\b[^.;]{0,40}\bvotes?\b|both forced|unanimous (consent|passage)|\bfiled\b[^.;]{0,20}discharge"
         r"|\bled (the |a )?(push|effort|fight|charge)|helped push|\bwhipp"
         r"|\b(gave|spent|spending|put|invested|committed|secured|directed|proposed|budget(ed)?|funded|allocat\w*|adds?)\b[^.;]{0,60}\$[0-9]"
         r"|\bproposed\b[^.;]{0,50}\bfunding\b|\bbudget (proposal|includes|adds)|\bdirected\b|\bordered\b"
         r"|\b(signed|issued) (an |a )?executive (order|action)s?|ballot (measure|initiative)[^.;]{0,30}\b(led|championed|bankrolled)"
         r"|campaigned (for|in)\b[^.;]{0,60}(states|nationally|across)")
COMMIT = (r"(?<!co)(?<!co-)\bsponsor(s|ed)?\b|\bintroduc|\bco-led\b|\bvot(ed|es|e|ing)\b|\byea\b|pledg|promis|\bvow"
          r"|platform|\bplans?\b|agenda|campaign site|propos|^would\b|\b(he|she) would\b|calls for"
          r"|\b(will|would) (push|fight|sign|expand|create|pass|cut|ban|veto|make|require|bring)\b|co-?wrote|\bauthored\b"
          r"|\b(playbook|blueprint)\b|asked (lawmakers|the legislature|congress)|called on (lawmakers|the legislature|congress)")


def rung(note, stance, flag=''):
    if stance not in ('Support', 'Lean support'):
        return None
    if flag == 'done':
        return 'Deliver'
    if flag == 'spons':
        return 'Talk'
    n = (note or '').strip()
    voter = re.match(r'(original )?(voted|cosponsor|co-sponsor)', n, re.I)
    if re.search(DELIVER, n, re.I) and not voter:
        return 'Deliver'
    if re.search(r'became law|signed into law', n, re.I) and re.match(r'(sponsor|co-?wrote|wrote|authored)', n, re.I):
        return 'Deliver'
    if re.search(SPEND, n, re.I) and not re.match(r'voted', n, re.I):
        return 'Spend'
    if re.search(COMMIT, n, re.I):
        return 'Commit'
    return 'Talk'


def defense(x):
    """Steward for legislators: recorded votes defending laws already on the books."""
    out = []
    m = (x['r'].get('medicaid') or ['', ''])[1]
    if re.search(r'\bvoted (no|against)\b[^.;]{0,40}(One Big|OBBBA)', m, re.I):
        out.append(['medicaid', True, m])
    elif re.search(r'(\bvoted for|deciding vote for)\b[^.;]{0,30}(One Big|OBBBA)', m, re.I):
        out.append(['medicaid', False, m])
    a = (x['r'].get('aca') or ['', ''])[1]
    if re.search(r'extension', a, re.I):
        if re.search(r'\bvoted (against|no)', a, re.I):
            out.append(['aca', False, a])
        elif re.search(r'\bvoted (to advance|for|yes)', a, re.I):
            out.append(['aca', True, a])
    return out


def pts(r, stance):
    return PTS.get(r, 0) * (LEAN if stance == 'Lean support' else 1) if r else 0


def build(d):
    SK = [x[0] for x in d['issues'] if x[0] not in ('sch', 'heg')]
    GK = [x[0] for x in d['gi']]
    sKey = lambda k: 'pfl' if k == 'pfml' else k
    AGK = list(dict.fromkeys([('pfml' if k == 'pfl' else k) for k in SK] + GK))
    GOLD = set(d['gold'])
    GOV = {g['st']: g for g in d['gov']}
    SEN = {s['id']: s for s in d['sen']}
    PUSH = d.get('push', {})
    RANKS = d['gsd']['ranks']

    def has(k, s):
        t = GOV[s]['status'].get(k) or ''
        if k not in GOLD: return t.startswith('Yes')
        if k == 'npv': return t == 'Member'
        if k == 'pfml': return t.startswith('Yes') or t.startswith('Enacted')
        if k in ('roe', 'wage', 'avr'): return t.startswith('Yes')
        if k == 'house': return not t.startswith('No major')
        return False

    def gavg(s):
        v = [RANKS[s][a] for a in ('health', 'cost', 'kids', 'gov')]
        return sum(v) / len(v)
    BA = min(gavg(s) for s in RANKS)
    steward = lambda s: (50 - gavg(s)) / (50 - BA) * 100

    def better(r, st, note, P, k):
        if k in P:
            pr = rung(P[k][1], P[k][0])
            if pts(pr, P[k][0]) > pts(r, st):
                return pr, P[k][0], 'push'
        return r, st, None

    def gov_items(s):
        g, P, out = GOV[s], PUSH.get('gov:' + s, {}), {}
        for k in GK:
            st, note = (g['sp'].get(k) or ['Unclear', ''])[:2]
            r, st, src = better(rung(note, st), st, note, P, k)
            counted = not (has(k, s) and r != 'Deliver' and k not in P)
            out[k] = (r, st, counted)
        return out

    def summarize(items, stew, scored=True, new=False, stype='state', dv=None):
        c = {k: v for k, v in items.items() if v[2]}
        den = len(c)
        per = {R: sum(pts(v[0], v[1]) for v in c.values() if v[0] == R) for R in RUNGS}
        return dict(den=den, left=len(items) - den, per=per, raw=(sum(per.values()) / den if den else 0),
                    n={R: sum(1 for v in c.values() if v[0] == R) for R in RUNGS},
                    lean={R: sum(1 for v in c.values() if v[0] == R and v[1] == 'Lean support') for R in RUNGS},
                    keys={R: [k for k, v in c.items() if v[0] == R] for R in RUNGS},
                    out=[k for k, v in items.items() if not v[2]],
                    stew=stew, scored=scored, new=new, stype=stype, dv=dv or [])

    def finish(rows):
        mx = max(r['raw'] for r in rows.values() if r['scored']) or 1
        for r in rows.values():
            r['ladder'] = r['raw'] / mx * CEIL
            # no Steward measure (no current office): the ladder carries the whole score
            wl, ws = (W_LADDER, W_STEWARD) if r['stew'] is not None else (1.0, 0.0)
            # each rung's share of the 0-100 total, so the bar adds up to the score
            r['part'] = {R: wl * (r['per'][R] / r['den'] if r['den'] else 0) / mx * CEIL for R in RUNGS}
            r['part']['Steward'] = ws * (r['stew'] or 0)
            r['raw_total'] = wl * r['ladder'] + ws * (r['stew'] or 0) if r['scored'] else None
            r['tot'] = round(r['raw_total']) if r['scored'] else None
            for k in ('per',):
                r.pop(k)
            r['ladder'] = round(r['ladder'], 2); r['stew'] = None if r['stew'] is None else round(r['stew'], 2)
            r['raw_total'] = None if r['raw_total'] is None else round(r['raw_total'], 3)
            r['part'] = {k: round(v, 2) for k, v in r['part'].items()}
            r['raw'] = round(r['raw'], 3)
        return rows

    G = {}
    for g in d['gov']:
        s = g['st']; new = bool(re.match(r'^(Governor-elect|Presumed)', g.get('s') or ''))
        G[s] = summarize(gov_items(s), 0 if new else steward(s), True, new, 'state')
    finish(G)

    S = {}
    for x in d['sen']:
        if re.search('appointee', x['id'], re.I):
            continue
        items = {}
        for k in SK:
            st, note = (x['r'].get(k) or ['Unclear', ''])[:2]
            items[k] = (rung(note, st), st, True)
        dv = defense(x)
        S[x['id']] = summarize(items, (100 * sum(1 for v in dv if v[1]) / len(dv)) if dv else 0, not x.get('new'), bool(x.get('new')), 'defense', dv)
    finish(S)

    H = {}
    for h in d['hope']:
        kind = h['kind']
        P = PUSH.get('gov:' + h['ref'], {}) if kind == 'gov' else PUSH.get('hope:' + h['n'], {})
        own = OWN.get(h['n']) if h.get('statescore') else None
        st_code = GOV[h['ref']]['st'] if kind == 'gov' else (SEN[h['ref']]['st'] if kind == 'sen' else h['st'])
        items = {}
        gi = gov_items(h['ref']) if kind == 'gov' and own is None else {}
        x = SEN[h['ref']] if kind == 'sen' else None
        for k in AGK:
            if own is not None:
                if k in own:
                    items[k] = (rung(own[k][1], own[k][0]), own[k][0], True)
                elif k in GK and has(k, h['ref']):
                    items[k] = (None, 'Unclear', False)
                else:
                    items[k] = (None, 'Unclear', True)
                continue
            if kind == 'gov':
                if k in gi:
                    items[k] = gi[k]; continue
                r, st = None, 'Unclear'
            elif kind == 'sen':
                sk = sKey(k)
                st, note = (x['r'].get(sk) or ['Unclear', ''])[:2] if sk in SK else ('Unclear', '')
                r = rung(note, st)
            else:
                cells = h.get('cells') or {}
                c = cells.get(sKey(k) if kind == 'selfsen' else k) or cells.get(k)
                st, note, flag = (c[0], c[1], c[3] if len(c) > 3 else '') if c else ('Unclear', '', '')
                r = rung(note, st, flag)
            r, st, _ = better(r, st, '', P, k)
            items[k] = (r, st, True)
        if kind == 'gov':
            stw, stype, dv = steward(st_code), 'state', []
        elif kind == 'sen':
            dv = defense(x); stw, stype = (100 * sum(1 for v in dv if v[1]) / len(dv)) if dv else 0, 'defense'
        elif h['n'] in DEF_OWN:
            dv = [list(v) for v in DEF_OWN[h['n']]]; stw, stype = 100 * sum(1 for v in dv if v[1]) / len(dv), 'defense'
        else:
            stw, stype, dv = None, None, []
        H[h['n']] = summarize(items, stw, True, False, stype, dv)
        H[h['n']]['partial'] = own is not None
    finish(H)

    mix = {R: 0 for R in RUNGS}
    for rows in (G, S):
        for r in rows.values():
            for R in RUNGS:
                mix[R] += r['n'][R]
    return dict(G=G, S=S, H=H, pts=PTS, w=[W_LADDER, W_STEWARD], lean=LEAN, mix=mix,
                own={n: {k: v for k, v in o.items()} for n, o in OWN.items()})
