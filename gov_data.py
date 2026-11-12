# Governors in office 2027 (assuming Holscher wins KS). For each issue: state status + governor position.
GISSUES = [("npv","National Popular Vote Compact"),("pfml","Paid family & medical leave"),
           ("roe","Codifying Roe / abortion rights"),("wage","$15 minimum wage"),
           ("avr","Automatic voter registration"),("house","Easing housing/building regulation")]

NPV = {"CA","CO","CT","DE","HI","IL","MD","ME","MA","MN","NJ","NM","NY","OR","RI","VT","VA","WA"}
PFML_MAND = {"CA":"Yes (2004)","NJ":"Yes (2009)","RI":"Yes (2014)","NY":"Yes (2018)","WA":"Yes (2020)",
             "MA":"Yes (2021)","CT":"Yes (2022)","OR":"Yes (2023)","CO":"Yes (2024)","DE":"Yes (benefits 2026)",
             "MN":"Yes (benefits Jan 2026)","ME":"Yes (benefits May 2026)","MD":"Enacted; launch delayed to 2027-28",
             "VA":"Enacted Apr 2026; benefits 2028"}
PFML_VOL = {"NH":"Voluntary state-run program only","VT":"Voluntary program only",
            "AL":"Private insurance option only","AR":"Private insurance option only","FL":"Private insurance option only",
            "TN":"Private insurance option only","TX":"Private insurance option only",
            "LA":"New 2026 law (per Mercer); not a mandatory program — verify"}
ROE = {"CA":"Yes — constitution (2022)","CO":"Yes — statute 2022 + constitution 2024","CT":"Yes — statute",
       "DE":"Yes — statute","HI":"Yes — statute","IL":"Yes — statute (2019)","ME":"Yes — statute",
       "MD":"Yes — constitution (2024)","MA":"Yes — statute (ROE Act 2020)","MI":"Yes — constitution (2022)",
       "MN":"Yes — statute (2023)","NV":"Yes — constitution (Q6 final approval Nov 2026)","NJ":"Yes — statute (2022)",
       "NM":"Yes — statute (2023)","NY":"Yes — statute + constitution (2024)","OR":"Yes — statute",
       "RI":"Yes — statute","VT":"Yes — constitution (2022)","WA":"Yes — statute","AZ":"Yes — constitution (2024)",
       "MT":"Yes — constitution (2024)","MO":"Yes — constitution (2024); repeal defeated Nov 2026",
       "VA":"Yes — constitution (Q1 approved Nov 2026)","OH":"Yes — constitution (2023)",
       "KS":"Court-recognized right (2019); voters rejected removing it (2022)",
       "AK":"Court-recognized right under state privacy clause",
       "ID":"No — near-total ban; Prop 1 defeated Nov 2026"}
WAGE = {"WA":"Yes — $17.13","CT":"Yes — $16.94","CA":"Yes — $16.90","NY":"Yes — $16.50+ (NYC area higher)",
        "NJ":"Yes — ~$15.92","HI":"Yes — $16","IL":"Yes — $15","MD":"Yes — $15","MA":"Yes — $15","DE":"Yes — $15",
        "MO":"Yes — $15 (Jan 2026)","NE":"Yes — $15 (Jan 2026)","AZ":"Yes — $15.15","CO":"Yes — $15.16",
        "ME":"Yes — $15.10","RI":"Yes — $15 ($17 by 2027)","OR":"Yes — $15.05 standard","FL":"Yes — $15 (Sep 30 2026)",
        "MI":"Not yet — $13.73; $15 Jan 2027","AK":"Not yet — $14 (Jul 2026); $15 Jul 2027","VT":"No — $14.42",
        "VA":"No — $12.77 (verify any 2026 increase)","NM":"No — $12","NV":"No — $12","MN":"No — $11.41",
        "OH":"No — $11","AR":"No — $11","MT":"No — $10.85","SD":"No — ~$11.85","WV":"No — $8.75"}
FED = {"AL","GA","ID","IN","IA","KS","KY","LA","MS","NH","NC","ND","OK","PA","SC","TN","TX","UT","WI","WY"}
AVR = {"AK","CA","CO","CT","DE","GA","HI","IL","ME","MD","MA","MI","MN","NV","NJ","NM","NY","OR","PA","RI","VT","VA","WA","WV"}
HOUSE = {"CA":"Major reforms: SB 79 transit upzoning (2025), CEQA streamlining (2025)",
         "WA":"Middle-housing mandate HB 1110 (2023)","OR":"Middle-housing law HB 2001 (2019)",
         "MT":"'Montana Miracle' zoning package (2023)","CO":"ADU & transit-oriented housing laws (2024)",
         "TX":"Small-lot & commercial-to-residential reforms (2025)","FL":"Live Local Act (2023)",
         "MA":"MBTA Communities law; Affordable Homes Act (2024)","ME":"LD 2003 zoning reform (2022)",
         "VT":"HOME Act (2023)","AZ":"ADU & middle-housing laws (2024)","UT":"Starter-home push (2025)",
         "NH":"Local zoning limits signed 2025"}

def status(st):
    s = {}
    s["npv"] = "Member" if st in NPV else "Not a member"
    if st == "NV": s["npv"] = "Not a member (Sisolak vetoed 2019; Legislature passed as const. amendment 2023)"
    s["pfml"] = PFML_MAND.get(st) or PFML_VOL.get(st) or "No program"
    s["roe"] = ROE.get(st, "No statutory/constitutional right")
    s["wage"] = WAGE.get(st) or ("No — $7.25 federal" if st in FED else "No")
    s["avr"] = "Yes" if st in AVR else "No"
    if st == "HI": s["avr"] = "Yes (expanded 2026; auto-registration from Jan 2027)"
    s["house"] = HOUSE.get(st, "No major statewide reform identified")
    return s

NF = "No specific statement found."
def gp(**kw):
    d = {k: NF for k, _ in GISSUES}
    d.update(kw)
    return d

# (state, governor, party, status, positions)
GOVS = [
 ("AL","Tommy Tuberville","R","Governor-elect (new)", gp(roe="Opposes abortion rights (Senate record).")),
 ("AK","Jonathan Kreiss-Tomkins","D","Governor-elect (flip)", gp()),
 ("AZ","Katie Hobbs","D","Re-elected", gp(roe="Signed repeal of 1864 abortion ban (2024); backed Prop 139.",
   house="Signed ADU & middle-housing bills (2024).")),
 ("AR","Sarah Huckabee Sanders","R","Re-elected", gp(roe="Opposes abortion rights.")),
 ("CA","Xavier Becerra","D","Governor-elect (new)", gp(roe="Defended abortion rights as AG/HHS Sec.",
   house="Day-one housing emergency EO; 'build off SB 79... end exclusionary zoning around more types of transit' (2026).")),
 ("CO","Phil Weiser","D","Governor-elect (new)", gp(roe="Defended abortion access as AG.")),
 ("CT","Ned Lamont","D","Re-elected", gp(house="Mixed: vetoed major zoning bill HB 5002 (Jun 2025); later revised version advanced.")),
 ("DE","Matt Meyer","D","Continuing (term to 2029)", gp()),
 ("FL","Byron Donalds","R","Governor-elect (new)", gp(roe="Opposes abortion rights (House record).")),
 ("GA","Keisha Lance Bottoms","D","Governor-elect (flip)", gp(wage="Supports $15 state minimum wage (Oct 2026).",
   house="Statewide affordable housing trust fund; crack down on corporate single-family landlords (2026).",
   roe="Supports abortion rights.")),
 ("HI","Josh Green","D","Re-elected", gp(house="Issued emergency housing proclamations to fast-track building (2023-).")),
 ("ID","Brad Little","R","Re-elected", gp(roe="Signed near-total ban.")),
 ("IL","JB Pritzker","D","Re-elected", gp(roe="Signed Reproductive Health Act (2019).", wage="Signed $15 by 2025 (2019).",
   pfml="Signed Paid Leave for All Workers (PTO, 2023) — not a PFML insurance program.")),
 ("IN","Mike Braun","R","Continuing (term to 2029)", gp(roe="Opposes abortion rights.")),
 ("IA","Rob Sand","D","Governor-elect (flip)", gp(wage="Proposes raising to $12 (Aug 2026); earlier said $15 (2025).",
   roe="Will veto new abortion restrictions; opposes Dobbs.", house="Simplify permitting/fees; rural housing task force (Aug 2026).")),
 ("KS","Cindy Holscher","D","Presumed winner (uncalled)", gp(roe="Abortion-rights supporter (2022 amendment fight).")),
 ("KY","Andy Beshear","D","Continuing (term to 2027)", gp(roe="Supports abortion rights; vetoes overridden.")),
 ("LA","Jeff Landry","R","Continuing (term to 2028)", gp(roe="Opposes abortion rights.")),
 ("ME","Hannah Pingree","D","Governor-elect (new)", gp()),
 ("MD","Wes Moore","D","Re-elected", gp(pfml="Signed delays to FAMLI launch (2024-25).", roe="Backed 2024 constitutional amendment.")),
 ("MA","Maura Healey","D","Re-elected", gp(house="Signed Affordable Homes Act (2024).")),
 ("MI","Jocelyn Benson","D","Governor-elect (new)", gp(avr="Implemented AVR as Secretary of State.", roe="Backed Prop 3 (2022).")),
 ("MN","Amy Klobuchar","D","Governor-elect (new)", gp(npv="Backed abolishing the Electoral College (2019 presidential run).",
   roe="Cosponsored WHPA in the Senate (2025).")),
 ("MS","Tate Reeves","R","Continuing (term to 2028)", gp(roe="Opposes abortion rights.")),
 ("MO","Mike Kehoe","R","Continuing (term to 2029)", gp(roe="Backed repeal: defeat would be 'a sad day for Missouri' (Nov 2026).")),
 ("MT","Greg Gianforte","R","Continuing (term to 2029)", gp(house="Signed 'Montana Miracle' zoning package (2023).")),
 ("NE","Jim Pillen","R","Re-elected", gp(roe="Opposes abortion rights.")),
 ("NV","Aaron Ford","D","Governor-elect (flip)", gp(roe="Abortion-rights supporter as AG.")),
 ("NH","Kelly Ayotte","R","Re-elected", gp(roe="Pledged not to sign further abortion restrictions.", house="Signed bills limiting local zoning barriers (2025).")),
 ("NJ","Mikie Sherrill","D","Continuing (elected 2025)", gp()),
 ("NM","Deb Haaland","D","Governor-elect (new)", gp(roe="Cosponsored WHPA in the House.")),
 ("NY","Kathy Hochul","D","Re-elected", gp(roe="Signed state ERA (approved by voters 2024).", wage="Signed $16.50+ schedule (2023).",
   house="Pro-housing budget deals (2024-25).")),
 ("NC","Josh Stein","D","Continuing (term to 2029)", gp(roe="Supports abortion rights.")),
 ("ND","Kelly Armstrong","R","Continuing (term to 2029)", gp()),
 ("OH","Amy Acton","D","Governor-elect (flip)", gp(wage="Would 'raise the minimum wage' (2026).",
   roe="'I will protect reproductive freedom' (2026).", house="Housing affordability top priority; day-one EOs (2026).")),
 ("OK","Mike Mazzei","R","Governor-elect (new)", gp()),
 ("OR","Tina Kotek","D","Re-elected", gp(house="Housing-production push; signed 2024 housing bill (SB 1537).")),
 ("PA","Josh Shapiro","D","Re-elected", gp(avr="Implemented AVR administratively (2023).", wage="Has repeatedly proposed raising PA wage to $15.",
   roe="Vowed to veto abortion restrictions.")),
 ("RI","Helena Foulkes","D","Governor-elect (new)", gp()),
 ("SC","Alan Wilson","R","Governor-elect (new)", gp(roe="Opposes abortion rights; defended SC ban as AG.")),
 ("SD","Larry Rhoden","R","Re-elected", gp(roe="Opposes abortion rights.")),
 ("TN","Marsha Blackburn","R","Governor-elect (new)", gp(roe="Opposes abortion rights (Senate record).")),
 ("TX","Gina Hinojosa","D","Governor-elect (flip)", gp(wage="Backs a minimum wage increase (2026).", roe="Backs abortion rights.",
   house="'Expand the supply of homes Texans can afford' (2026).")),
 ("UT","Spencer Cox","R","Continuing (term to 2029)", gp(house="Champion of 'starter homes' agenda (2025).")),
 ("VT","Phil Scott","R","Re-elected", gp(pfml="Vetoed mandatory PFML (2020); created voluntary program.", roe="Supported Prop 5 (2022).",
   house="Signed HOME Act (2023).")),
 ("VA","Abigail Spanberger","D","Continuing (elected 2025)", gp(npv="Signed HB 965 joining NPVIC (Apr 2026).",
   pfml="Signed PFML law (Apr 2026).", roe="Signed bill placing reproductive-freedom amendment on ballot (Feb 2026).")),
 ("WA","Bob Ferguson","D","Continuing (term to 2029)", gp()),
 ("WV","Patrick Morrisey","R","Continuing (term to 2029)", gp(roe="Opposes abortion rights.")),
 ("WI","David Crowley","D","Governor-elect (new)", gp(house="Streamline permits; legalize duplexes, fourplexes & ADUs (2026).")),
 ("WY","Eric Barlow","R","Governor-elect (new)", gp()),
]
