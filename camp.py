"""Which 2026 Democratic winners campaigned on each agenda item, and the Top 10 built from it.

Source: fc/census/winners_2026.json, the Nov 15 2026 census of what each 2026 Democratic winner (22 Senate, 24 governor)
ran on: campaign issue pages, ads, debates, questionnaires and plans, each entry with a source URL. Legislative records
count only when the campaign featured them. Each winner counts once per item. The same census picked the site's measure
lists: the 30 items the most winners ran on, plus hot buttons (issue_meta.HOT, gov2.HOT) kept on purpose.
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
CENSUS = os.path.join(ROOT, "fc", "census", "winners_2026.json")


def build(d):
    rows = json.load(open(CENSUS))
    keys = {"sen": [i[0] for i in d["issues"]], "gov": [g[0] for g in d["gi"]]}
    out = {"n": {}, "who": {}}
    for side in ("sen", "gov"):
        people = [p for p in rows if p["side"] == side]
        out["n"][side] = len(people)
        out["who"][side] = {}
        for k in keys[side]:
            out["who"][side][k] = [p["who"] for p in people if any(i["key"] == k for i in p["issues"])]
    return out


ENACTED = {"sen": set(), "gov": set()}   # already law; keep in sync with ENACTED in template.html


def rank(d, camp):
    """Top 10 per side by number of 2026 Democratic winners who campaigned on it; ties go to more Democratic backers overall.
    Hot buttons and measures that are already law stay out of the ranking."""
    hot = {s: set(d.get("hot", {}).get(s, [])) for s in ("sen", "gov")}
    sen = [x for x in d["sen"] if x["p"] == "D" and "ppoint" not in x["id"]]
    gov = [g for g in d["gov"] if g["p"] == "D"]
    back = {
        "sen": lambda k: sum(x["r"].get(k, ["U"])[0] == "Support" for x in sen),
        "gov": lambda k: sum(g["sp"].get(k, ["U"])[0] == "Support" for g in gov),
    }
    top = {s: sorted((k for k in w if k not in ENACTED[s] and k not in hot[s] and k != "sch"),
                     key=lambda k: (-len(w[k]), -back[s](k)))[:10] for s, w in camp["who"].items()}
    return top, {s: {k: len(camp["who"][s][k]) for k in top[s]} for s in top}
