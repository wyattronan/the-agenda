"""Serial (Oxford) comma pass over the site's display text. Leaves direct quotes, URLs and poll wording alone."""
import re
ITEM = r"(?:[^,;:.?!<>\"\n{}()']|\([^()]{0,24}\)|(?<=\w)'(?=\w))"
RX = re.compile(r",( " + ITEM + r"{1,48}?) (and|or) (?=\S)")
QUOTE = re.compile(r"(?<![\w])'[^']{2,}?'(?![\w])|\"[^\"]*\"|“[^”]*”|‘[^’]*’")
SKIP_FIRST = {"which","who","that","while","but","so","saying","as","when","where","because","if","though","although","with","without","then","not","plus","also","calling","arguing","adding","noting","citing","and","or","before","after","since","until","demanding","banning","covering","creating","including","giving","making","expanding","shielding","allowing","easing","requiring","raising","lowering","aiming","funding","overriding","ending","cutting","seeking","opposing","wanting","leaving","blaming","faulting","pushing","taking","starting","keeping","helping","speeding","adding","limiting","capping","touted","signed","voted","said","says","he","she","they","it","his","her","their","its","there","this","these","those"}
BLOCK = ["no specific statement or vote","no tax on overtime and tips","delivered via new child","faulted Trump and","federalization unlawful and","for example through a bigger","decide coverage and","aimed at waitlists and","Massie is pushing","for seniors and veterans","to recruit and keep","short of a formal freeze","Cruz tariffs and the war","corruption and the Epstein files","defended the war and","housing goals and standards","family and medical","Family Grocery and Farmer","Families and Workers","Washington, DC and","Washington, D.C. and","Bill Act, which","State addresses and","Act, S.","Act S.","rules statewide","H.R. ","H.R.","S.2823","S.4007","Peters-Hawley","Peters–Hawley"]
CHANGES = []
def _fix(seg):
    def r(m):
        item = m.group(1).strip()
        w = item.split()[0].lower().strip("'’") if item.split() else ""
        if not item.split() or w in SKIP_FIRST or w.endswith("ing") and w not in {"housing","spending","something","nothing","everything","funding","training","bring"}: return m.group(0)
        if len(item.split())>7: return m.group(0)
        s = seg[max(0,m.start()-60):m.end()+30]
        if any(b in s for b in BLOCK): return m.group(0)
        CHANGES.append(seg[max(0,m.start()-50):m.end()+20])
        return f",{m.group(1)}, {m.group(2)} "
    return RX.sub(r, seg)
EXTRA = [("Chicago, St. Louis and New York","Chicago, St. Louis, and New York"),("Amb. Huckabee and pro-Israel","Amb. Huckabee, and pro-Israel"),("Rep. Randy Fine and others","Rep. Randy Fine, and others"),("state property, courthouses and schools","state property, courthouses, and schools")]
def oxford(s):
    if not isinstance(s,str) or s.startswith("http") or len(s)<12: return s
    for a,b in EXTRA: s = s.replace(a,b)
    out, last = [], 0
    for q in QUOTE.finditer(s):
        out.append(_fix(s[last:q.start()])); out.append(q.group(0)); last = q.end()
    out.append(_fix(s[last:]))
    return "".join(out)
SKIP_KEYS = {"q","u","url","src","photos","quote","quotes","said","text_raw"}
def walk(o, key=None):
    if isinstance(o, dict): return {k: (v if k in SKIP_KEYS else walk(v,k)) for k,v in o.items()}
    if isinstance(o, list): return [walk(v,key) for v in o]
    return oxford(o) if isinstance(o,str) else o
