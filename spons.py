import re
NEG = re.compile(r"\bnot (?:an? |the )?(?:original |lead )?(?:co-?)?sponsor|\bnever (?:co-?)?sponsored|\bisn't a (?:co-?)?sponsor|\bno (?:co-?)?sponsorship|\bwithdrew (?:as )?(?:a )?cosponsor|\b(?:pledged|promised|vowed|would|will|plans?|wants?) to (?:co-?)?sponsor", re.I)
POS = re.compile(r"\b(?:original |lead )?(?:co-?)?sponsor(?:ed|s|ing)?\b|\bintroduced\b|\bco-?led\b|\bco-?author(?:ed)?\b|\bauthored\b|\blead author\b", re.I)
def sponsored(stance, ev):
    if stance not in ("Support", "Lean support"): return False
    t = NEG.sub(" ", ev)
    return bool(POS.search(t))
