"""Track when each published stance last changed, so the site can tag fresh ones "NEW STANCE".

fc/stance_log.json keeps one line per cell: "side:id|key": [stance, date or null].
null means the stance was already there when the log started (not new).
A build that sees a different stance than the log stamps today's date (Chicago time).
The site shows the tag for 7 days after that date; export puts recent dates in D["newst"].

Cells: "sen:<senator id>|<issue>" and "ss:<state-senate member vid>|<issue>"
(an alternate winner in an uncalled seat uses vid "<id>a", as in the site).
"""
import json, os, datetime
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(ROOT, "fc", "stance_log.json")
DAYS = 7


def today():
    return datetime.datetime.now(ZoneInfo("America/Chicago")).date().isoformat()


def cells(d):
    out = {}
    for x in d.get("sen", []):
        for k, v in x["r"].items():
            out[f"sen:{x['id']}|{k}"] = v[0]
    for S in d.get("ss", []):
        for m in S["members"]:
            for k, v in (m.get("r") or {}).items():
                out[f"ss:{m['id']}|{k}"] = v[0]
            alt = m.get("alt") or {}
            for k, v in (alt.get("r") or {}).items():
                out[f"ss:{m['id']}a|{k}"] = v[0]
    return out


def load():
    return json.load(open(LOG)) if os.path.exists(LOG) else {}


def save(log):
    # one cell per line keeps daily diffs readable
    lines = [f" {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}" for k, v in sorted(log.items())]
    open(LOG, "w").write("{\n" + ",\n".join(lines) + "\n}\n")


def stamp(log, cur, date):
    """Record stance changes in cur against log, dated `date`. Returns cells changed."""
    changed = []
    for key, st in cur.items():
        old = log.get(key)
        if old is None:
            log[key] = [st, None]
        elif old[0] != st:
            log[key] = [st, date]
            changed.append(key)
    return changed


def recent(log, cur, date):
    cut = (datetime.date.fromisoformat(date) - datetime.timedelta(days=DAYS)).isoformat()
    return {k: v[1] for k, v in log.items() if v[1] and v[1] > cut and k in cur}


def update(d, date=None):
    date = date or os.environ.get("AGENDA_TODAY") or today()
    log = load()
    cur = cells(d)
    changed = stamp(log, cur, date)
    save(log)
    if changed:
        print("new stances", len(changed))
    return recent(log, cur, date)
