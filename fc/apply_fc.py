import os as _os
_R = _os.environ.get("AGENDA_ROOT") or _os.path.abspath(_os.path.join(_os.path.dirname(__file__), ".."))
"""Merge fact-check agent outputs (fc/out/*.json) into the exported data dict."""
import json, glob, os
VALID = {'Support','Lean support','Mixed','Lean oppose','Oppose','Unclear','N/A'}
def apply(d, log=True):
    urls = {}           # ('sen'|'gov', name, key) -> url
    stats = {'changed':0,'confirmed':0,'skipped':0,'dupes':0}
    seen = set()
    sen_by = {s['n']: s for s in d['sen']}
    gov_by = {g['n']: g for g in d['gov']}
    # Hedging notes ("has been on both sides", "tailors it to the audience"): shown as a tag, never change the stance.
    hedge = d.setdefault('hedge', {'sen': {}, 'gov': {}})
    def _hedge(side, who, k, txt, url=None):
        t = (txt or '').strip()
        if not t: return
        tgt = (sen_by if side == 'sen' else gov_by)[who]
        hedge[side][f"{tgt['id'] if side == 'sen' else tgt['st']}|{k}"] = {'t': t, **({'u': url} if url else {})}
    for f in sorted(glob.glob(_R + '/fc/out/*.json')):
        base = os.path.basename(f)
        if base == 'links.json': continue
        side = 'sen' if base.startswith('sen') else 'gov'
        try: rows = json.load(open(f))
        except Exception as e:
            print('bad json', base, e); continue
        for r in rows:
            sig = (base, json.dumps(r, sort_keys=True))
            if sig in seen: stats['dupes'] += 1; continue
            seen.add(sig)
            who, k = r.get('who'), r.get('key')
            new = r.get('new_stance'); ev = (r.get('evidence') or '').strip(); url = r.get('url')
            tgt = (sen_by if side=='sen' else gov_by).get(who)
            if not tgt or new not in VALID:
                stats['skipped'] += 1; continue
            cells = tgt['r'] if side=='sen' else tgt['sp']
            if k not in cells:
                stats['skipped'] += 1; continue
            if url: urls[(side, who, k)] = url
            if r.get('changed') and new != 'Unclear' and not url:
                stats['skipped'] += 1; continue          # no source, no change
            if r.get('hedge'): _hedge(side, who, k, r['hedge'], r.get('hedge_url'))
            if r.get('changed'):
                cells[k] = [new, ev or cells[k][1]]
                stats['changed'] += 1
            else:
                stats['confirmed'] += 1
    try:
        for m in json.load(open(_R + '/fc/manual.json')):
            tgt = sen_by.get(m['who']) or gov_by.get(m['who'])
            cells = tgt['r'] if m['who'] in sen_by else tgt['sp']
            if m['key'] in cells:
                cells[m['key']] = [m['new_stance'], m.get('evidence') or cells[m['key']][1]]
                side = 'sen' if m['who'] in sen_by else 'gov'
                if 'hedge' in m:   # explicit; "" clears an older agent note
                    if m['hedge']: _hedge(side, m['who'], m['key'], m['hedge'], m.get('hedge_url'))
                    else: hedge[side].pop(f"{tgt['id'] if side == 'sen' else tgt['st']}|{m['key']}", None)
                if 'url' in m:   # explicit source override; None clears a stale link
                    if m['url']: urls[(side, m['who'], m['key'])] = m['url']
                    else: urls.pop((side, m['who'], m['key']), None)
    except FileNotFoundError: pass
    if log: print('fact-check', stats, 'urls', len(urls))
    return urls
