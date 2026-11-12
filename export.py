import json, os
ROOT = os.path.dirname(os.path.abspath(__file__)); os.environ["AGENDA_ROOT"] = ROOT; os.chdir(ROOT)
import state_senate, senate_data, issue_meta, gov_data, gov2

d = json.load(open("data.json"))
d["ss"] = state_senate.data()
d["issues"] = [list(x) for x in senate_data.ISSUES]
d["meta"] = {k: {"s": issue_meta.SHORT[k], "full": issue_meta.FULL[k], "area": a_, "need": n_, "who": w_}
             for k, s_, a_, n_, w_ in issue_meta.META}
d["areas"] = [list(x) for x in issue_meta.AREAS]
d["why"] = issue_meta.WHY
d["power"] = sorted(issue_meta.POWER)
d["spower"] = sorted(gov2.STATE_POWER)
d["gareas"] = [list(x) for x in gov2.GAREAS]
d["gi"] = [list(x) for x in gov2.GI]
d["gold"] = sorted(gov2.OLD)
party = {r[1]: r[3] for r in senate_data.ROSTER}
for x in d["sen"]:
    x["r"] = {k: list(v) for k, v in senate_data.senator_record(x["id"], party[x["id"]]).items()}
import hegseth as _heg
for x in d["sen"]:
    if x["id"] in _heg.POS:
        _p = _heg.POS[x["id"]]; x["r"]["heg"] = [_p[0], _p[1]]
NFS = "No specific statement found."
for g in d["gov"]:
    sp = {k: list(v) for k, v in gov2.gov_new(g["st"], g["p"]).items()}
    for k in gov2.OLD:
        t = g["pos"].get(k, NFS)
        if g["st"] in gov2.POS and k in gov2.POS[g["st"]]:
            sp[k] = list(gov2.POS[g["st"]][k])
        elif t == NFS:
            sp[k] = ["Unclear", "No statement or action found."]
        else:
            sp[k] = ["Noted", t]
    g["sp"] = sp
    g["status"].update(gov2.status2(g["st"]))
for S in d["ss"]:
    S["govsp"] = next(g["sp"] for g in d["gov"] if g["st"] == S["st"])
    S.pop("govpos", None)
import sys; sys.path.insert(0, ROOT + "/champ"); sys.path.insert(0, ROOT + "/fc")
from apply_fc import apply as _fc
_fcurls = _fc(d)
_sid = {s["n"]: s["id"] for s in d["sen"]}; _gst = {g["n"]: g["st"] for g in d["gov"]}
d["curl"] = {"sen": {f"{_sid[n]}|{k}": u for (sd,n,k),u in _fcurls.items() if sd=="sen" and n in _sid}, "gov": {f"{_gst[n]}|{k}": u for (sd,n,k),u in _fcurls.items() if sd=="gov" and n in _gst}}
d["curl"]["sen"].update({f"{i}|heg": p[2] for i, p in _heg.POS.items()})
d["curl"]["gov"].update({f"{st}|guard": u for st, u in gov2.GUARD_URLS.items()})
# measures removed from the site: drop any leftover research records for them (fc/out still holds old findings)
DROPPED = {"road"}
for _x in d["sen"]:
    for _k in DROPPED: _x["r"].pop(_k, None)
d["curl"]["sen"] = {k: v for k, v in d["curl"]["sen"].items() if k.split("|")[-1] not in DROPPED}
_fcurls = {kk: v for kk, v in _fcurls.items() if not (kk[0] == "sen" and kk[2] in DROPPED)}
from build_champ import build as _bc
d["champ"], _st = _bc(d, _fcurls); print("champions", _st)
import os
d["mlinks"] = json.load(open(ROOT + "/fc/out/links.json")) if os.path.exists(ROOT + "/fc/out/links.json") else {"sen":{},"gov":{}}
import desc as _desc
sys.path.insert(0, ROOT + "/fc/polls")
from build_polls import build as _bp
_m = json.load(open(ROOT + "/fc/in/measures.json"))
_vk = ["sen:"+x["key"] for x in _m["senate"]] + ["gov:"+x["key"] for x in _m["governor"]]
d["polls"] = _bp(_vk, os.environ.get("POLLSRC", ROOT + "/fc/polls/out"))
for _k in DROPPED: d["polls"].pop("sen:"+_k, None) if isinstance(d["polls"], dict) else None; d["mlinks"].get("sen", {}).pop(_k, None)
_g = json.load(open(ROOT + "/gop/gop_tracker.json")); _gx = json.load(open(ROOT + "/gop/extras.json"))
d["gop"] = {"as_of": _g["as_of"], "window": _g["window"], "people": _g["people"], "photos": json.load(open(ROOT + "/gop/photos.json")), **_gx}
d["desc"] = {"sen": _desc.SEN, "gov": _desc.GOV}
import gsd as _gsd, spons as _sp
d["gsd"] = _gsd.build()
d["gsd"]["spons"] = {x["id"]: [k for k, v in x["r"].items() if k != "sch" and _sp.sponsored(v[0], v[1])] for x in d["sen"]}
import hopefuls as _hp
d["hope"] = _hp.HOPE
import natpush as _np
d["push"] = _np.PUSH
_NOREC = "No position on record yet."
for _x in d["sen"]:
    for _k, _v in _x["r"].items():
        if str(_v[1]).startswith("Not researched"): _v[1] = _NOREC
for _g in d["gov"]:
    for _k, _v in _g["sp"].items():
        if str(_v[1]).startswith("Not researched"): _v[1] = _NOREC
for _S in d["ss"]:
    for _k, _v in (_S.get("govsp") or {}).items():
        if str(_v[1]).startswith("Not researched"): _v[1] = _NOREC
import ladder as _lad
d["ladder"] = _lad.build(d)
_sen = [x for x in d["sen"] if "ppoint" not in x["id"]]
_sk = [i[0] for i in d["issues"] if i[0] not in ("sch", "heg")]
_ss = {k: (len(d["champ"]["sen"].get(k, [])), sum(x["r"][k][0] == "Support" for x in _sen)) for k in _sk}
_gk = [x[0] for x in d["gi"]]
_gs = {k: (len(d["champ"]["gov"].get(k, [])), sum(g["sp"].get(k, ["U"])[0] == "Support" for g in d["gov"])) for k in _gk}
# Top 10 priorities: ranked by how many 2026 Democratic winners campaigned on each item (see camp.py)
import camp as _camp
d["camp"] = _camp.build(d)
d["top10"], d["topcount"] = _camp.rank(d, d["camp"])
print("top10", d["top10"])
import oxford as _ox
d = _ox.walk(d)
json.dump(d, open("data.json", "w"), ensure_ascii=False)
tpl = open("template.html").read()
blob = json.dumps(d, ensure_ascii=False).replace("</", "<\\/")
open("index.html", "w").write(tpl.replace("__DATA__", blob))
print("ok", len(blob))
