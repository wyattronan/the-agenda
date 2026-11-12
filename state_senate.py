"""State senate rosters (2027) and inferred/recorded positions for NC, TX, GA on the six statehouse issues."""
import gov_data as g

import gov2
KEYS = [k for k, *_ in gov2.GI]
INF = "[Inferred] "

# ---------- defaults: no party inference ----------
NS = "No statement or recorded vote found."
def blank(p):
    return {k: ("Unclear", NS) for k in KEYS}
DEF = {"NC": blank, "TX": blank, "GA": blank}

# ---------- rosters: (district, name, party, flags, overrides) ----------
NC = [
 (1,"Jerry Tillett","R"),(2,"Norman Sanderson","R"),(3,"Bob Brinson","R"),(4,"Jess Rivera","D","new|Flip: beat Buck Newton (R)"),
 (5,"Kandie Smith","D"),(6,"Michael Lazzara","R"),(7,"Jessica Bichler","D","new|Flip: beat Majority Leader Michael Lee (R)"),
 (8,"Bill Rabon","R"),(9,"Brent Jackson","R"),(10,"Benton Sawrey","R","narrow|Held by about 2 points"),
 (11,"James Gailliard","D","new|Flip: beat Lisa Barnes (R)"),(12,"Jim Burgin","R"),(13,"Lisa Grafstein","D"),(14,"Dan Blue","D"),
 (15,"Jay Chaudhuri","D","lead|Democratic Whip"),(16,"Gale Adcock","D"),(17,"Sydney Batch","D","lead|Democratic Leader"),
 (18,"Haseeb Fatmi","D"),(19,"Val Applewhite","D"),(20,"Natalie Murdock","D"),(21,"Tom McInnis","R"),(22,"Sophia Chitlik","D"),
 (23,"Jonah Garson","D"),(24,"Danny Britt","R","narrow|Uncalled: leads Catina Hamm (D) by 268 votes, recount range"),
 (25,"Amy Galey","R","lead|Majority Whip"),(26,"Sam Page","R","new|Unseated Senate leader Phil Berger in the primary"),
 (27,"Michael Garrett","D"),(28,"Gladys Robinson","D"),(29,"Dave Craven","R"),(30,"Steve Jarvis","R"),(31,"Dana Jones","R"),
 (32,"Paul Lowe","D"),(33,"Carl Ford","R","lead|Republican Joint Caucus Leader"),(34,"April Cook","D","new|Flip: open seat"),
 (35,"Todd Johnson","R","lead|Majority Whip"),(36,"Eddie Settle","R"),(37,"Vickie Sawyer","R"),(38,"Mujtaba Mohammed","D"),
 (39,"DeAndrea Salvador","D"),(40,"Joyce Waddell","D"),(41,"Caleb Theodros","D"),(42,"Woodson Bradley","D"),
 (43,"Brad Overcash","R","narrow|Held by about 2 points"),(44,"Ted Alexander","R"),(45,"Mark Hollo","R"),(46,"Warren Daniel","R"),
 (47,"Ralph Hise","R"),(48,"Tim Moffitt","R"),(49,"Julie Mayfield","D","lead|Democratic Caucus Secretary"),(50,"Kevin Corbin","R"),
]
TX = [
 (1,"Bryan Hughes","R"),(2,"Bob Hall","R"),(3,"Trent Ashby","R","new|New senator (from the Texas House)"),
 (4,"Brett Ligon","R","new|New senator (Montgomery County DA)"),(5,"Charles Schwertner","R"),(6,"Carol Alvarado","D"),
 (7,"Paul Bettencourt","R"),(8,"Angela Paxton","R"),(9,"Taylor Rehmet","D","Flipped the seat in a Jan 2026 special; re-elected Nov 2026"),
 (10,"Phil King","R"),(11,"Dennis Paul","R","new|New senator (from the Texas House)"),(12,"Tan Parker","R"),(13,"Borris Miles","D"),
 (14,"Vacant","V","vac|Sarah Eckhardt (D) elected Comptroller; special election pending (safe D seat)"),
 (15,"Molly Cook","D"),(16,"Vacant","V","vac|Nathan Johnson (D) elected Attorney General; special election pending (safe D seat)"),
 (17,"Joan Huffman","R"),(18,"Lois Kolkhorst","R"),(19,"Roland Gutierrez","D"),(20,"Juan \"Chuy\" Hinojosa","D"),(21,"Judith Zaffirini","D"),
 (22,"David Cook","R","new|New senator (from the Texas House)"),(23,"Royce West","D"),(24,"Pete Flores","R"),(25,"Donna Campbell","R"),
 (26,"José Menéndez","D"),(27,"Adam Hinojosa","R"),(28,"Charles Perry","R"),(29,"César Blanco","D"),(30,"Brent Hagenbuch","R"),(31,"Kevin Sparks","R"),
]
GA = [
 (1,"Ben Watson","R"),(2,"Derek Mallow","D"),(3,"Mike Hodges","R"),(4,"Billy Hickman","R"),(5,"Sheikh Rahman","D"),(6,"Matt Brass","R"),
 (7,"Ruwa Romman","D","new|New senator"),(8,"Russ Goodman","R"),(9,"Nikki Merritt","D"),(10,"Larry Johnson","D"),(11,"Sam Watson","R"),
 (12,"Edward Brown","D"),(13,"Carden Summers","R"),(14,"Kevin Abel","D"),(15,"Teddy Reese","D"),(16,"Marty Harbin","R"),
 (17,"Gail Davenport","D"),(18,"Steven McNeel","R"),(19,"David Sikes","R"),(20,"Larry Walker","R"),(21,"Jason Dickerson","R"),
 (22,"Harold Jones II","D","lead|Democratic Leader"),(23,"Max Burns","R"),(24,"Lee Anderson","R"),(25,"Rick Williams","R"),(26,"David Lucas","D"),
 (27,"Mike Dudgeon","R"),(28,"Donzella James","D"),(29,"Randy Robertson","R"),(30,"Tim Bearden","R"),
 (31,"Jason Anavitarte","R","lead|Majority Leader"),(32,"Kay Kirkpatrick","R"),(33,"Doc Rhett","D"),(34,"Kenya Wicks","D"),
 (35,"Jaha Howard","D"),(36,"Nan Orrock","D"),(37,"Darcy Castro","D","new|narrow|Flip, pending: leads Sen. Ed Setzler (R) by under 1 point"),
 (38,"RaShaun Kemp","D"),(39,"Sonya Halpern","D"),(40,"Sally Harrell","D"),(41,"Kim Jackson","D"),
 (42,"Eric W. Lee Sr.","D","new|Flip: open seat"),(43,"Tonya Anderson","D"),(44,"Saira Draper","D"),
 (45,"Anthony Scott Tippetts","D","new|Flip: beat Clint Dixon (R)"),(46,"Marc McMain","R"),(47,"Frank Ginn","R"),
 (48,"Laura Murvartian","D","new|Flip: beat Shawn Still (R)"),(49,"Drew Echols","R"),(50,"Bo Hatchett","R"),(51,"Will Wade","R"),
 (52,"Chuck Hufstetler","R"),(53,"Lanny Thomas","R"),(54,"Chuck Payne","R"),(55,"Randal Mangham","D"),(56,"John Albers","R"),
]

# ---------- individual records (statements and roll calls) ----------
OVR = {}
def put(st, d, **kw):
    OVR.setdefault((st, d), {}).update(kw)

# NC: SB 20 (12-week ban) veto override, May 16 2023, 30-20 party line (ncleg roll call #215)
NC_AYE_D = [44,35,9,6,12,50,29,46,33,25,47,9,30,35,6,21,48,43,8,2,10,37,36,24]  # districts of current members who voted aye
for d in sorted(set(NC_AYE_D)):
    put("NC", d, roe=("Oppose", "Voted to override Gov. Cooper's veto of SB 20, the 12-week abortion ban (May 16 2023, 30–20)."))
for d in [16,19,17,14,15,27,13,32,49,38,20,28,39,5,40]:
    put("NC", d, roe=("Lean support", "Voted to sustain Gov. Cooper's veto of SB 20, the 12-week abortion ban (May 16 2023, 30–20)."))
put("NC", 17, pfml=("Support", "Sponsor of the NC Paid Family Leave Insurance Act (SB 480): \"it is outrageous that we don't provide paid leave\" (Mar 2025)."))

# TX: SB 8 (six-week ban) third reading, Mar 30 2021, 19-12 (Senate Journal)
for d in [7,25,2,17,1,18,8,28,5]:
    put("TX", d, roe=("Oppose", "Voted for SB 8, the six-week 'heartbeat' ban (Mar 30 2021, 19–12)."))
for d in [6,29,19,20,26,13,23,21]:
    put("TX", d, roe=("Lean support", "Voted against SB 8, the six-week 'heartbeat' ban (Mar 30 2021, 19–12)."))
put("TX", 1, roe=("Oppose", "Authored SB 8 (2021), the six-week 'heartbeat' ban, and voted for it (19–12)."))
# TX: SB 15 conference report adopted 31-0, May 31 2025 — every senator then serving
SB15 = "Voted for the final version of SB 15, allowing smaller homes on smaller lots (May 31 2025, 31–0)."
for d in [6,7,29,25,15,24,19,30,2,27,20,17,1,10,18,26,13,12,8,28,5,31,23,21]:
    put("TX", d, house=("Support", SB15))
put("TX", 1, house=("Support", "Authored SB 840 (2025), allowing apartments and mixed use on commercial land without rezoning; voted for final SB 15 (31–0)."))
put("TX", 7, house=("Support", "Authored SB 15 (2025), capping minimum lot sizes in big cities' new subdivisions; final version passed 31–0."))
put("TX", 19, house=("Support", "Co-authored SB 15 (2025), one of two Democrats to sign on; voted for the final version (31–0)."))
put("TX", 23, house=("Support", "Co-authored SB 15 (2025), one of two Democrats to sign on; voted for the final version (31–0)."))
put("TX", 24, house=("Support", "Authored SB 785 (2025) limiting city restrictions on manufactured housing; voted for final SB 15 (31–0)."))

# GA: HB 481 (six-week ban), Mar 22 2019, 34-18. Every Republican present voted yes; Kirkpatrick was the one GOP absence.
for d in [56,24,6,47,16,52,54,29,1]:
    put("GA", d, roe=("Oppose", "Voted for HB 481, the six-week abortion ban (Mar 22 2019, 34–18)."))
put("GA", 32, roe=("Mixed", "Missed the 2019 HB 481 vote for a funeral; said afterward she would have voted against the six-week ban."))
GA_D19 = "Senate Democrats opposed HB 481 (Mar 22 2019, 34–18), but three were absent and the per-member roll call wasn't retrievable; no other statement found."
for d in [43,17,40,22,28,26,36,5,33]:
    put("GA", d, roe=("Unclear", GA_D19))


# ---------- second batch: roll calls mapped to the new governor issues ----------
# NC HB 76, Medicaid expansion, Senate third reading Mar 15 2023, 44–2 (RCS S-51)
NC76 = "Voted for HB 76, North Carolina's Medicaid expansion (Mar 15 2023, 44–2)."
for d in [16,19,17,14,15,27,13,32,49,38,20,28,39,5,40, 44,24,12,50,29,46,33,25,47,9,35,6,21,43,8,10,37]:
    put("NC", d, medicaid=("Support", NC76))
for d in [2,36]:
    put("NC", d, medicaid=("Oppose", "Voted against HB 76, North Carolina's Medicaid expansion (Mar 15 2023, 44–2)."))
for d in [30,48]:
    put("NC", d, medicaid=("Unclear", "Excused absence on HB 76, Medicaid expansion (Mar 15 2023); no other statement found."))
# NC HB 10 veto override, Nov 20 2024, 30–19 (RCS S-669): $463M to clear the voucher waitlist, bundled with sheriff–ICE cooperation
HB10 = "HB 10 (2024) put $463 million into Opportunity Scholarship vouchers, bundled with a sheriff–ICE cooperation mandate."
for d in [44,3,24,12,50,29,46,33,25,47,9,30,35,6,21,48,43,8,2,10,37,36]:
    put("NC", d, vouchers=("Lean oppose", "Voted to override Gov. Cooper's veto of HB 10 (Nov 20 2024, 30–19). " + HB10))
for d in [16,19,17,14,15,27,13,32,49,38,20,28,39,5,40]:
    put("NC", d, vouchers=("Lean support", "Voted to sustain Gov. Cooper's veto of HB 10 (Nov 20 2024, 30–19). " + HB10))

# TX: members serving in the 2025 regular session
TX25R = [1,2,5,7,8,10,12,17,18,24,25,27,28,30,31]
TX25D = [6,13,15,19,20,21,23,26,29]
for d in TX25R:
    put("TX", d, vouchers=("Oppose", "Voted for SB 2, the $1 billion private-school voucher (ESA) program (Feb 5 2025, 19–12)."))
for d in TX25D:
    put("TX", d, vouchers=("Lean support", "Voted against SB 2, the $1 billion private-school voucher (ESA) program (Feb 5 2025, 19–12)."))
for d in TX25R + TX25D:
    put("TX", d, teacher=("Support", "Voted for HB 2, $8.5 billion for schools including $4.2 billion in teacher and staff raises (May 23 2025, 31–0)."),
        datactr=("Support", "Voted for SB 6, which makes data centers and other large loads pay toward grid hookup costs and accept curtailment (Senate passed unanimously, Mar 19 2025)."),
        ptax=("Lean support", "SB 4, raising the school homestead exemption to $140,000, passed the Senate 30–0 (Feb 13 2025). One senator didn't vote and the per-member roll call wasn't retrievable."))
put("TX", 10, datactr=("Support", "Authored SB 6 (2025), which makes data centers pay toward grid hookup costs; passed the Senate unanimously."))
put("TX", 7, ptax=("Support", "Authored SB 4 and SB 23 (2025), raising homestead exemptions to $140,000 and $200,000 for seniors."))

# GA: members serving in 2023–24 (same two-year term)
GA23R = [1,3,4,6,8,11,13,16,20,23,24,25,29,30,31,32,47,50,52,54,56]
GA23D = [2,5,9,17,22,26,28,33,36,39,40,41,43]
for d in GA23R:
    put("GA", d, vouchers=("Oppose", "Voted for SB 233, the Georgia Promise Scholarship voucher (Mar 6 2023, 33–23, every Republican yes)."))
for d in GA23D:
    put("GA", d, vouchers=("Lean support", "Voted against SB 233, the Georgia Promise Scholarship voucher (Mar 6 2023, 33–23, every Democrat no)."))
for d in GA23R + GA23D:
    put("GA", d, ptax=("Lean support", "HB 581 (2024), the floating homestead exemption capping assessment increases, passed the Senate 52–0 (Mar 28 2024). Four senators didn't vote and the per-member roll call wasn't retrievable."))
put("GA", 52, datactr=("Support", "Sponsor of SB 34 (2025–26) to bar Georgia Power from passing data center costs to residential customers: 'Ninety percent of people want this protection.'"))

# alternates for uncalled seats
ALT = {
 ("NC",24): ("Catina Hamm", "D", "Trails Sen. Danny Britt by 268 votes; a win makes the chamber 25–25 with Lt. Gov. Rachel Hunt (D) breaking ties"),
 ("GA",37): ("Ed Setzler", "R", "Incumbent (author of HB 481, the 2019 six-week ban); trails Darcy Castro by under 1 point"),
}
ALT_OVR = {("GA",37): {"roe": ("Oppose", "Sponsored HB 481 (2019), Georgia's six-week abortion ban."),
  "vouchers": ("Oppose", "Voted for SB 233, the Georgia Promise Scholarship voucher (Mar 6 2023, 33–23, every Republican yes)."),
  "ptax": ("Lean support", "HB 581 (2024), the floating homestead exemption, passed the Senate 52–0 (Mar 28 2024); four didn't vote and the per-member roll call wasn't retrievable.")}}

def rec(st, d, p, ov=None):
    base = DEF[st]("D" if p in ("D","V") else "R")
    r = {k: list(base[k]) for k in KEYS}
    for k, v in (ov or {}).items():
        r[k] = list(v)
    return r

def build_state(st, roster):
    out = []
    for row in roster:
        d, n, p = row[:3]
        meta = row[3] if len(row) > 3 else ""
        parts = meta.split("|") if meta else []
        flags = [x for x in parts if x in ("new","narrow","lead","vac")]
        note = next((x for x in parts if x not in ("new","narrow","lead","vac")), "")
        m = {"id": f"{st}{d}", "d": d, "n": n, "p": p, "f": flags, "note": note, "r": rec(st, d, p, OVR.get((st, d)))}
        if (st, d) in ALT:
            an, ap, anote = ALT[(st, d)]
            m["alt"] = {"n": an, "p": ap, "note": anote, "r": rec(st, d, ap, ALT_OVR.get((st, d)))}
        out.append(m)
    return out

STATES = [
 {"st":"NC","name":"North Carolina","seats":50,
  "gov":"Gov. Josh Stein (D)","pres":"Lt. Gov. Rachel Hunt (D)","tb":True,
  "house":"Democratic (flipped Nov 2026)",
  "rule":"Bills need a majority of senators voting. The lieutenant governor votes only to break a tie, so 25–25 passes with Hunt.",
  "alt":"SD24", "members": build_state("NC", NC)},
 {"st":"TX","name":"Texas","seats":31,
  "gov":"Gov.-elect Gina Hinojosa (D)","pres":"Lt. Gov.-elect Vikki Goodwin (D)","tb":True,
  "house":"Democratic (flipped Nov 2026)",
  "rule":"Final passage takes a majority of senators present; the lieutenant governor breaks ties. Under the Senate's current rules a bill can't reach the floor without 5/9 of members (18 of 31) agreeing to take it up, and the Republican majority writes the rules for 2027, including how much agenda power Goodwin keeps.",
  "alt":"vac", "members": build_state("TX", TX)},
 {"st":"GA","name":"Georgia","seats":56,
  "gov":"Gov.-elect Keisha Lance Bottoms (D)","pres":"Lt. Gov.-elect Josh McLaurin (D)","tb":False,
  "house":"Democratic (flipped Nov 2026)",
  "rule":"Georgia's constitution requires a majority of all 56 senators (29) for final passage, whoever is absent. The lieutenant governor presides but casts no tie-breaking vote on bills.",
  "alt":"SD37", "members": build_state("GA", GA)},
]
for s in STATES:
    s["status"] = g.status(s["st"])
    govrow = next(r for r in g.GOVS if r[0] == s["st"])
    s["govpos"] = govrow[4]

def data():
    return STATES

if __name__ == "__main__":
    for s in STATES:
        ms = s["members"]
        print(s["st"], len(ms), sum(m["p"]=="R" for m in ms), "R", sum(m["p"]=="D" for m in ms), "D", sum(m["p"]=="V" for m in ms), "V")
