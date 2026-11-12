"""Which 2026 Democratic winners campaigned on each agenda item.

On the 2026 ballot = re-elected, elected (incl. specials and flips), or presumed winners; seats filled by appointment and
members not up in 2026 don't count. Losing candidates aren't tracked on this site.
Campaigned on = a Support stance (or a Democratic champion entry) whose evidence is dated 2026 and is something they said,
pledged, or put in a platform, not a legislative record (votes, cosponsorships, bill signings), which every sitting member
already gets credit for in scoring and champion tags.
"""
import re

BALLOT = re.compile(r"Re-elected|Senator-elect|Presumed winner|Won 2026|Governor-elect")
LEG = re.compile(r"^\s*(\(original\)\s*)?(Voted|Co-?sponsor|Original cosponsor|Signed|Introduced|Sponsor|Lead sponsor|Vetoed)", re.I)
Y26 = re.compile(r"2026")


def _camp(note):
    return bool(note) and bool(Y26.search(note)) and not LEG.search(note)


def build(d):
    sides = {
        "sen": ([x for x in d["sen"] if x["p"] == "D" and BALLOT.search(x["s"])],
                [i[0] for i in d["issues"] if i[0] not in ("sch", "heg")], lambda x, k: x["r"].get(k)),
        "gov": ([g for g in d["gov"] if g["p"] == "D" and BALLOT.search(g["s"])],
                [g[0] for g in d["gi"]], lambda g, k: g["sp"].get(k)),
    }
    out = {"n": {}, "who": {}}
    for side, (people, keys, get) in sides.items():
        out["n"][side] = len(people)
        out["who"][side] = {}
        for k in keys:
            ch = {c["n"]: c for c in d["champ"][side].get(k, []) if c["p"] in ("D", "I")}
            who = []
            for x in people:
                v = get(x, k) or ["Unclear", ""]
                if (v[0] == "Support" and _camp(v[1])) or (x["n"] in ch and _camp(ch[x["n"]].get("ev", ""))):
                    who.append(x["n"])
            out["who"][side][k] = who
    return out


ENACTED = {"sen": set(), "gov": set()}   # already law; keep in sync with ENACTED in template.html


def rank(d, camp):
    """Top 10 per side by number of 2026 Democratic winners who campaigned on it; ties go to more Democratic backers overall."""
    # measures that are already law drop out of the rankings
    sen = [x for x in d["sen"] if x["p"] == "D" and "ppoint" not in x["id"]]
    gov = [g for g in d["gov"] if g["p"] == "D"]
    back = {
        "sen": lambda k: sum(x["r"].get(k, ["U"])[0] == "Support" for x in sen),
        "gov": lambda k: sum(g["sp"].get(k, ["U"])[0] == "Support" for g in gov),
    }
    top = {s: sorted((k for k in w if k not in ENACTED[s]), key=lambda k: (-len(w[k]), -back[s](k)))[:10] for s, w in camp["who"].items()}
    return top, {s: {k: len(camp["who"][s][k]) for k in top[s]} for s in top}
