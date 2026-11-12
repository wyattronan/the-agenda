# Senate data for the 120th Congress (Jan 2027), assuming Colom (MS) and Peltola (AK) win.
# Each issue value: (stance, evidence). Stances: Support / Lean support / Mixed / Unclear / Lean oppose / Oppose / N/A
# "Support" always means support FOR the policy named in the column header.

import issue_meta as _im
ISSUES = [(k, s_) for k, s_, *_ in _im.META]

FIL2022 = {"Baldwin","Bennet","Blumenthal","Booker","Cantwell","Coons","Cortez Masto","Duckworth","Gillibrand",
           "Hassan","Heinrich","Hickenlooper","Hirono","Kaine","Kelly","King","Luján","Markey","Merkley","Murphy",
           "Murray","Ossoff","Padilla","Reed","Rosen","Sanders","Schatz","Schumer","Van Hollen","Warner","Warnock",
           "Warren","Whitehouse","Wyden"}
M4A = {"Baldwin","Blumenthal","Booker","Gillibrand","Heinrich","Hirono","Luján","Markey","Merkley","Padilla","Schatz",
       "Schiff","Warren","Welch","Whitehouse","Van Hollen"}
DC = {"Schumer","Alsobrooks","Baldwin","Bennet","Blumenthal","Booker","Cantwell","Coons","Cortez Masto","Duckworth",
      "Gillibrand","Hassan","Heinrich","Hickenlooper","Hirono","Kaine","Kim","Markey","Merkley","Murphy","Murray",
      "Padilla","Reed","Rosen","Sanders","Schatz","Schiff","Warner","Warnock","Warren","Welch","Whitehouse","Wyden",
      "Slotkin","Luján"}
PR = {"Heinrich","Cortez Masto","Padilla","Schumer","Gillibrand","Booker","Hickenlooper","Schatz","Baldwin","Bennet",
      "Blumenthal","Rosen"}
WAGE = {"Alsobrooks","Baldwin","Blumenthal","Blunt Rochester","Booker","Cantwell","Duckworth","Fetterman","Gallego",
        "Gillibrand","Hirono","Kaine","Kelly","Kim","Markey","Merkley","Murphy","Murray","Padilla","Reed","Schatz",
        "Schiff","Van Hollen","Warnock","Warren","Welch","Whitehouse","Wyden"}
ISR_NONE = {"Schumer","Gillibrand","Rosen","Cortez Masto","Blumenthal","Fetterman","Coons"}
ISR_HALF = {"Warner","Reed","Whitehouse"}
TALKING = {"Banks","Budd","Britt","Cruz","Hagerty","Hawley","Johnson","Lee","Moody","Moreno","Paul","Risch",
           "Schmitt","Scott (FL)","Scott (SC)","Sheehy","McCormick"}

# Recorded votes used in place of party inference
R_OLD = {"Murkowski","Boozman","Cotton","Scott (FL)","Crapo","Risch","Young","Grassley","Moran","Paul","Kennedy",
         "Wicker","Hawley","Fischer","Hoeven","Cramer","Lankford","Scott (SC)","Thune","Rounds","Hagerty","Cruz",
         "Lee","Capito","Johnson","Barrasso"}          # Republican senators serving in Mar 2021 & May 2022
HOUSE_WHPA_NAY = {"Banks","Budd","Curtis","Moore","Barr","Hern","Letlow"}  # House roll 295, Sep 24 2021
S744_NO = {"Barrasso","Boozman","Crapo","Cruz","Fischer","Grassley","Johnson","Lee","Moran","Paul","Risch",
           "Scott (SC)","Thune","Wicker"}
S744_YES_R = {"Murkowski","Hoeven"}
S744_YES_D = {"Baldwin","Bennet","Blumenthal","Cantwell","Coons","Gillibrand","Heinrich","Hirono","Kaine","King",
              "Merkley","Murphy","Murray","Reed","Sanders","Schatz","Schumer","Warner","Warren","Whitehouse","Wyden"}
SANDERS15_YES = {"Bennet","Hickenlooper","Ossoff","Cortez Masto","Rosen","Heinrich","Luján","Schumer","Warner"}
SANDERS15_NO = {"Coons","Hassan","King"}
V_WHPA = "Voted against advancing the Women's Health Protection Act (May 11 2022, 49–51)."
V_WHPA_H = "Voted against the Women's Health Protection Act in the House (Sep 24 2021, 218–211)."
V_15 = "Voted against Sanders' $15 minimum-wage amendment (Mar 5 2021, 42–58)."
V_744 = "the 2013 comprehensive immigration bill, S.744 (Jun 27 2013, 68–32)."
NS = "No statement or vote found."

AI_VOTE = "Voted to strip the 10-year moratorium on state AI laws from the OBBBA (99-1, Jul 1 2025)."

def dem_defaults(n):
    d = {}
    if n in FIL2022:
        d["fil"] = ("Lean support", "Voted Jan 19 2022 to change Senate rules to pass voting-rights bill by simple majority; no 2025-26 statement found.")
    else:
        d["fil"] = ("Unclear", "Joined Senate after the 2022 rules vote; no 2025-26 statement found.")
    d["sch"] = ("Unclear", "No public statement found. Leadership vote is a secret ballot, expected early Dec 2026.")
    d["m4a"] = ("Support", "Cosponsor, Medicare for All Act S.1506 (Apr 29 2025).") if n in M4A else \
               ("Unclear", "Not a cosponsor of S.1506; no endorsement found.")
    d["roe"] = ("Support", "Cosponsor, Women's Health Protection Act S.2150 (Jun 24 2025) — introduced by the entire Dem caucus.")
    dc = "Cosponsor, DC Admission Act S.51 (Jan 2025)." if n in DC else "Not an original S.51 (DC) cosponsor."
    pr = " Cosponsored Puerto Rico Status Act (S.3231, 118th Cong.)." if n in PR else ""
    d["dcpr"] = ("Support" if n in DC else "Unclear", dc + pr)
    if n in WAGE:
        d["wage"] = ("Support", "Cosponsor, Raise the Wage Act S.1332 — $17 by 2030 (Apr 8 2025).")
    elif n in SANDERS15_YES:
        d["wage"] = ("Lean support", "Voted for Sanders' $15 amendment (Mar 5 2021); not a cosponsor of the 2025 $17 bill.")
    elif n in SANDERS15_NO:
        d["wage"] = ("Lean oppose", "Voted against Sanders' $15 amendment (Mar 5 2021); not a cosponsor of the 2025 $17 bill.")
    else:
        d["wage"] = ("Unclear", "Not an original cosponsor of S.1332 ($17); no statement or vote found.")
    d["ai"] = ("Lean support", AI_VOTE)
    d["imm"] = ("Lean support", "Voted for " + V_744 + " No 2025-26 statement found.") if n in S744_YES_D else \
               ("Unclear", "No specific 2025-26 statement or vote found.")
    d["ice"] = ("Support", "Backed caucus ICE-reform demands ('masks off, body cameras on', judicial warrants) during the 2026 DHS shutdown; voted NO on $70B ICE/CBP reconciliation (Jun 5 2026).")
    if n in ISR_NONE:
        d["isr"] = ("Oppose", "Voted against both Sanders resolutions to block bulldozer & 1,000-lb bomb sales to Israel (Apr 15 2026).")
    elif n in ISR_HALF:
        d["isr"] = ("Mixed", "Voted to block the bulldozer sale but not the bomb sale (Apr 15 2026).")
    else:
        d["isr"] = ("Support", "Voted to block both bulldozer & 1,000-lb bomb sales to Israel (Apr 15 2026).")
    return d

def rep_defaults(n):
    d = {}
    if n in TALKING:
        d["fil"] = ("Mixed", "Backed a 'talking filibuster' to pass SAVE America Act (Meadows/CPI list, Mar 11 2026) — not outright elimination.")
    else:
        d["fil"] = ("Unclear", "No specific statement found. Thune: votes 'not anywhere close' to nuking it (Mar 2026).")
    d["sch"] = ("N/A", "Republican — does not vote in Dem leadership election.")
    d["m4a"] = ("Unclear", NS + " Medicare for All has never had a Senate floor vote.")
    d["roe"] = ("Oppose", V_WHPA) if n in R_OLD else ("Oppose", V_WHPA_H) if n in HOUSE_WHPA_NAY else ("Unclear", NS)
    d["dcpr"] = ("Unclear", NS + " DC statehood has never had a Senate floor vote.")
    d["wage"] = ("Oppose", V_15) if n in R_OLD else ("Unclear", NS)
    d["ai"] = ("Lean support", AI_VOTE)
    if n in S744_NO:
        d["imm"] = ("Lean oppose", "Voted against " + V_744)
    elif n in S744_YES_R:
        d["imm"] = ("Lean support", "Voted for " + V_744)
    else:
        d["imm"] = ("Unclear", NS)
    d["ice"] = ("Oppose", "Voted YES on $70B ICE/CBP funding reconciliation through 2029, no reforms (Jun 5 2026, 52-47).")
    d["isr"] = ("Oppose", "Voted against both Sanders resolutions to block arms sales to Israel (Apr 15 2026).")
    return d

NF = ("Unclear", "No statement found.")

def newcomer(**kw):
    d = {k: NF for k, _ in ISSUES}
    d.update(kw)
    return d

def r_newcomer(key="_", **kw):
    d = rep_defaults(key)
    d["fil"] = ("Unclear", "No statement found.")
    d["ai"] = ("Unclear", "No statement found.")
    d["ice"] = ("Unclear", "No statement or Senate vote found.")
    d["isr"] = ("Unclear", "No statement or Senate vote found.")
    d.update(kw)
    return d

# (state, name_key, display, party, status, notes)
ROSTER = [
 ("AL","Britt","Katie Britt","R","Continuing"),
 ("AL","Moore","Barry Moore","R","Senator-elect (succeeds Tuberville)"),
 ("AK","Murkowski","Lisa Murkowski","R","Continuing"),
 ("AK","Peltola","Mary Peltola","D","Presumed winner (uncalled; led by 0.3 pts)"),
 ("AZ","Kelly","Mark Kelly","D","Continuing"),
 ("AZ","Gallego","Ruben Gallego","D","Continuing"),
 ("AR","Boozman","John Boozman","R","Continuing"),
 ("AR","Cotton","Tom Cotton","R","Re-elected 2026"),
 ("CA","Padilla","Alex Padilla","D","Continuing"),
 ("CA","Schiff","Adam Schiff","D","Continuing"),
 ("CO","Bennet","Michael Bennet","D","Continuing"),
 ("CO","Hickenlooper","John Hickenlooper","D","Re-elected 2026"),
 ("CT","Blumenthal","Richard Blumenthal","D","Continuing"),
 ("CT","Murphy","Chris Murphy","D","Continuing"),
 ("DE","Coons","Chris Coons","D","Re-elected 2026"),
 ("DE","Blunt Rochester","Lisa Blunt Rochester","D","Continuing"),
 ("FL","Scott (FL)","Rick Scott","R","Continuing"),
 ("FL","Moody","Ashley Moody","R","Won 2026 special"),
 ("GA","Warnock","Raphael Warnock","D","Continuing"),
 ("GA","Ossoff","Jon Ossoff","D","Re-elected 2026"),
 ("HI","Schatz","Brian Schatz","D","Continuing"),
 ("HI","Hirono","Mazie Hirono","D","Continuing"),
 ("ID","Crapo","Mike Crapo","R","Continuing"),
 ("ID","Risch","Jim Risch","R","Re-elected 2026"),
 ("IL","Duckworth","Tammy Duckworth","D","Continuing"),
 ("IL","Stratton","Juliana Stratton","D","Senator-elect (succeeds Durbin)"),
 ("IN","Young","Todd Young","R","Continuing"),
 ("IN","Banks","Jim Banks","R","Continuing"),
 ("IA","Grassley","Chuck Grassley","R","Continuing"),
 ("IA","Turek","Josh Turek","D","Senator-elect (flip; succeeds Ernst)"),
 ("KS","Moran","Jerry Moran","R","Continuing"),
 ("KS","Hamilton","Adam Hamilton","D","Senator-elect (flip; defeated Marshall)"),
 ("KY","Paul","Rand Paul","R","Continuing"),
 ("KY","Barr","Andy Barr","R","Senator-elect (succeeds McConnell)"),
 ("LA","Kennedy","John Kennedy","R","Continuing"),
 ("LA","Letlow","Julia Letlow","R","Senator-elect (Cassidy lost primary)"),
 ("ME","King","Angus King","I (caucuses D)","Continuing"),
 ("ME","Jackson","Troy Jackson","D","Senator-elect (flip; defeated Collins)"),
 ("MD","Van Hollen","Chris Van Hollen","D","Continuing"),
 ("MD","Alsobrooks","Angela Alsobrooks","D","Continuing"),
 ("MA","Warren","Elizabeth Warren","D","Continuing"),
 ("MA","Markey","Ed Markey","D","Re-elected 2026"),
 ("MI","Slotkin","Elissa Slotkin","D","Continuing"),
 ("MI","El-Sayed","Abdul El-Sayed","D","Senator-elect (succeeds Peters)"),
 ("MN","MN appointee","TBD — Klobuchar appointee","D (expected)","Gov.-elect Klobuchar will appoint her own successor (Jan 2027)"),
 ("MN","Flanagan","Peggy Flanagan","D","Senator-elect (succeeds Tina Smith)"),
 ("MS","Wicker","Roger Wicker","R","Continuing"),
 ("MS","Colom","Scott Colom","D","Presumed winner (uncalled; led by ~65 votes)"),
 ("MO","Hawley","Josh Hawley","R","Continuing"),
 ("MO","Schmitt","Eric Schmitt","R","Continuing"),
 ("MT","Sheehy","Tim Sheehy","R","Continuing"),
 ("MT","Alme","Kurt Alme","R","Senator-elect (succeeds Daines)"),
 ("NE","Fischer","Deb Fischer","R","Continuing"),
 ("NE","Ricketts","Pete Ricketts","R","Re-elected 2026"),
 ("NV","Cortez Masto","Catherine Cortez Masto","D","Continuing"),
 ("NV","Rosen","Jacky Rosen","D","Continuing"),
 ("NH","Hassan","Maggie Hassan","D","Continuing"),
 ("NH","Pappas","Chris Pappas","D","Senator-elect (succeeds Shaheen)"),
 ("NJ","Booker","Cory Booker","D","Re-elected 2026"),
 ("NJ","Kim","Andy Kim","D","Continuing"),
 ("NM","Heinrich","Martin Heinrich","D","Continuing"),
 ("NM","Luján","Ben Ray Luján","D","Re-elected 2026"),
 ("NY","Schumer","Chuck Schumer","D","Continuing"),
 ("NY","Gillibrand","Kirsten Gillibrand","D","Continuing"),
 ("NC","Budd","Ted Budd","R","Continuing"),
 ("NC","Cooper","Roy Cooper","D","Senator-elect (flip; succeeds Tillis)"),
 ("ND","Hoeven","John Hoeven","R","Continuing"),
 ("ND","Cramer","Kevin Cramer","R","Continuing"),
 ("OH","Moreno","Bernie Moreno","R","Continuing"),
 ("OH","Brown","Sherrod Brown","D","Senator-elect (flip; won special vs. Husted)"),
 ("OK","Lankford","James Lankford","R","Continuing"),
 ("OK","Hern","Kevin Hern","R","Senator-elect (succeeds appointee Armstrong)"),
 ("OR","Wyden","Ron Wyden","D","Continuing"),
 ("OR","Merkley","Jeff Merkley","D","Re-elected 2026"),
 ("PA","Fetterman","John Fetterman","D","Continuing"),
 ("PA","McCormick","Dave McCormick","R","Continuing"),
 ("RI","Reed","Jack Reed","D","Re-elected 2026"),
 ("RI","Whitehouse","Sheldon Whitehouse","D","Continuing"),
 ("SC","Scott (SC)","Tim Scott","R","Continuing"),
 ("SC","Andrews","Annie Andrews","D","Senator-elect (flip; defeated Darline Graham Nordone)"),
 ("SD","Thune","John Thune","R","Continuing"),
 ("SD","Rounds","Mike Rounds","R","Re-elected 2026"),
 ("TN","Hagerty","Bill Hagerty","R","Re-elected 2026"),
 ("TN","TN appointee","TBD — Blackburn appointee","R (expected)","Gov.-elect Blackburn will appoint her own successor (Jan 2027)"),
 ("TX","Cruz","Ted Cruz","R","Continuing"),
 ("TX","Talarico","James Talarico","D","Senator-elect (flip; defeated Paxton)"),
 ("UT","Lee","Mike Lee","R","Continuing"),
 ("UT","Curtis","John Curtis","R","Continuing"),
 ("VT","Sanders","Bernie Sanders","I (caucuses D)","Continuing"),
 ("VT","Welch","Peter Welch","D","Continuing"),
 ("VA","Warner","Mark Warner","D","Re-elected 2026"),
 ("VA","Kaine","Tim Kaine","D","Continuing"),
 ("WA","Murray","Patty Murray","D","Continuing"),
 ("WA","Cantwell","Maria Cantwell","D","Continuing"),
 ("WV","Capito","Shelley Moore Capito","R","Re-elected 2026"),
 ("WV","Justice","Jim Justice","R","Continuing"),
 ("WI","Johnson","Ron Johnson","R","Continuing"),
 ("WI","Baldwin","Tammy Baldwin","D","Continuing"),
 ("WY","Barrasso","John Barrasso","R","Continuing"),
 ("WY","Hageman","Harriet Hageman","R","Senator-elect (succeeds Lummis)"),
]

NEW_D = {"Peltola","Stratton","Turek","Hamilton","Jackson","El-Sayed","MN appointee","Flanagan","Colom","Pappas",
         "Cooper","Brown","Andrews","Talarico"}
NEW_R = {"Moore","Barr","Letlow","Alme","Hern","Hageman","TN appointee"}

OV = {}  # overrides for continuing senators

def ov(n, **kw):
    OV.setdefault(n, {}).update(kw)

# ---------- Democratic overrides ----------
ov("Schumer",
   fil=("Unclear", "Twice declined to answer on ending it (Nov 4 2026): 'the first thing we're going to do is reduce people's costs.' In Aug 2024 he planned carve-outs for voting rights & abortion."),
   sch=("Support", "'I'll be reelected as majority leader... The issue is not me' (Nov 4 2026)."),
   ice=("Support", "'We want masks off, body cameras on' (Jan 28 2026); 'no blank check for a lawless ICE' (Mar 27 2026)."))
ov("Warren",
   fil=("Support", "Time op-ed (~Nov 5 2026): if GOP blocks anti-corruption bills, 'let's clear away Senate filibuster rules and pass the laws anyway.'"),
   sch=("Unclear", "'We'll know a lot more after the midterms' (AP, fall 2026)."))
ov("Warnock", fil=("Support", "Proposed ending the filibuster to pass the John Lewis Voting Rights Advancement Act (May 2026)."))
ov("Fetterman",
   fil=("Oppose", "Reversed: 'I now recognize how important the filibuster is' — praised Manchin/Sinema as 'courageous' (WaPo op-ed, Jul 27 2026)."),
   ice=("Mixed", "Voted NO on $70B ICE reconciliation — 'I'm going to vote with my party' (Jun 2026); voted for 2025 GOP funding bills & the Laken Riley Act."),
   dcpr=("Lean support", "Added as S.51 (DC) cosponsor after introduction (2025). No PR statement found."),
   isr=("Oppose", "Voted against both resolutions (Apr 15 2026); only Dem to oppose Iran war-powers resolution."))
ov("Van Hollen",
   sch=("Lean oppose", "'No one should be committing to anybody as the next Democratic leader... We need commitments' (Bloomberg, ~Nov 4 2026). Floated as alternative; El-Sayed backs him."),
   m4a=("Support", "Cosponsored S.1506 (Nov 2025); 'we need a Medicare-for-All-type solution' (Politico, Oct 26 2026)."),
   dcpr=("Support", "Sponsor, DC Admission Act S.51 (Jan 9 2025)."))
ov("Slotkin",
   sch=("Oppose", "'We need significant new leadership... old models are no longer working'; agreed that includes Schumer & Jeffries (late Jun 2026)."),
   wage=("Support", "Added as S.1332 ($17) cosponsor after introduction."),
   isr=("Support", "Voted to block both sales (Apr 15 2026): 'struggled with these as much as any vote since I joined Congress.'"))
ov("Booker", sch=("Lean support", "Commended Schumer's midterm leadership; expects a 'family discussion' (ABC, Nov 4 2026)."))
ov("Sanders",
   sch=("Lean oppose", "Said lack of commitments to Schumer shows party is 'ready for a rebirth' with new leadership (Mar 2026)."),
   m4a=("Support", "Sponsor, Medicare for All Act S.1506 (Apr 2025)."),
   wage=("Support", "Sponsor, Raise the Wage Act S.1332 — $17 by 2030 (Apr 2025)."),
   isr=("Support", "Led the resolutions: 'more than 80% of the Democratic caucus... voted to block U.S. military aid to Netanyahu' (Apr 15 2026)."))
ov("Markey",
   sch=("Lean oppose", "'We need a big debate about new leadership in the Senate' (primary debate, Aug 2026)."),
   ai=("Support", "Cosponsored Blackburn amendment to strip state-AI moratorium; voted 99-1 to strip it (Jul 2025)."))
ov("Heinrich", sch=("Lean oppose", "Called on Schumer/DSCC to stay out of contested primaries after Mills exit (spring 2026); part of the 'fight club' of senators challenging his strategy."),
   dcpr=("Support", "Cosponsor S.51 (DC); sponsor of Puerto Rico Status Act (S.3231, 118th)."))
ov("Ossoff", sch=("Unclear", "Senior campaign staffer said he had no answer on backing Schumer (pre-election, Nov 2026)."),
   isr=("Support", "Voted to block both sales — first time (Apr 15 2026)."))
ov("Kelly", imm=("Support", "Joined lawmakers backing the bipartisan Dignity Act (Apr 22 2026)."),
   isr=("Support", "Voted to block both sales but 'cannot and will not abandon Israel' (Apr 15 2026)."))
ov("Coons", imm=("Support", "Said he would champion the bipartisan Dignity Act in the Senate (2025)."),
   isr=("Oppose", "Voted against both (Apr 15 2026): votes not 'an abandonment of the state of Israel'; voted to end Iran war."))
ov("Cantwell", ai=("Support", "Co-led amendment stripping state-AI moratorium: 'we can't just run over good state consumer protection laws' (Jul 2025)."))
ov("Hassan", isr=("Support", "Flipped to block both sales, 'informed by President Trump's and PM Netanyahu's reckless decision to go to war' (Apr 2026)."))
ov("Schiff", isr=("Support", "Joint w/ Padilla: opposed 'specific weapons... which might be used in Iran' (Apr 15 2026)."))
ov("Padilla", isr=("Support", "Joint w/ Schiff: opposed 'specific weapons... which might be used in Iran' (Apr 15 2026)."))
ov("Gillibrand", isr=("Oppose", "Voted against both: won't 'leave an ally... being attacked without support' (Apr 15 2026)."))
ov("Warner", isr=("Mixed", "Blocked bulldozers, not bombs: 'The United States can and must hold two truths at once' (Apr 15 2026)."))
ov("Welch", wage=("Support", "Cosponsor S.1332 ($17) AND co-lead of Hawley's $15 bill S.2013 (Jun 10 2025)."))
ov("Cortez Masto", fil=("Lean support", "Voted for 2022 rules change; earlier backed a 'talking filibuster'. No 2025-26 statement found."))

# ---------- Republican overrides ----------
ov("Thune", fil=("Oppose", "'There aren't anywhere close to the votes — not even close — to nuking the filibuster' (Mar 2026)."))
ov("Johnson", fil=("Support", "'The only way we can stop them is to end the filibuster now' (Fox, ~May 4 2026); op-ed calling it a change he's 'willing to make'."))
ov("Lee", fil=("Support", "Leading push to change rules (talking filibuster / nuke) for SAVE America Act; argues Dems will end it anyway (2026)."))
ov("Paul", fil=("Support", "Among GOP senators arguing to eliminate/weaken the 60-vote rule before Dems do (May 2026)."),
   ai=("Support", "Opposed state-AI moratorium as federal overreach; voted to strip it (Jul 2025)."),
   ice=("Mixed", "Voted NO on Apr 23 2026 ICE budget resolution (wanted $70B offset) but YES on final Jun 5 bill."))
ov("McCormick", fil=("Oppose", "Would oppose ending it — worried about DC/PR statehood and Court-packing (Center Square, Jul 2026); earlier on 'talking filibuster' list (Mar 2026)."))
ov("Cramer", fil=("Oppose", "Defended the filibuster after Cornyn's flip (Mar 2026)."),
   wage=("Oppose", "Questioned need for any federal minimum wage; warned $15 would cut entry-level jobs (Jun 2025)."))
ov("Murkowski", fil=("Lean oppose", "Opposes the SAVE America Act outright; not among senators pushing to end filibuster (2026)."),
   roe=("Mixed", "Not a WHPA cosponsor; co-led bipartisan Reproductive Freedom for Women Act w/ Collins & Kaine (2023)."),
   ice=("Support", "Only Republican to vote NO on $70B ICE/CBP reconciliation (Jun 5 2026) and on the Apr 23 budget resolution."))
ov("Hawley", wage=("Support", "Sponsor, Higher Wages for American Workers Act S.2013 — $15 + inflation (Jun 10 2025)."),
   ai=("Support", "Opposed state-AI moratorium; co-leads bipartisan AI chatbot/minor-safety (GUARD) legislation (2025)."))
ov("Cruz", ai=("Oppose", "Led the 10-yr moratorium on state AI laws; as Commerce chair pushes federal preemption (2025-26). Still voted to strip it."))
ov("Moreno", ice=("Oppose", "Defended agents' masks: they'd 'be happy not to wear masks' if not doxxed (Jan 2026); voted YES on ICE reconciliation (Jun 2026)."))
ov("Marshall_unused")
ov("Wicker", dcpr=("Mixed", "Sponsored a Puerto Rico Status Act with a 'commonwealth' option (S.2944, 2023); no DC statement found."))
ov("Barrasso", ice=("Oppose", "'ICE and Border Patrol agents weren't the problem... Democrats are' (Apr 2026); voted YES on reconciliation."))

# ---------- Newcomers ----------
NEW = {}
NEW["Stratton"] = newcomer(
 fil=("Support", "'When Democrats take back the Senate, I want us to end the filibuster and get things done' (Center Square, ~Oct 2026)."),
 sch=("Oppose", "Spokesperson reaffirmed she will not back Schumer (Nov 4 2026)."),
 m4a=("Support", "'We will fight for Medicare for all' (primary night, Mar 17 2026)."),
 roe=("Lean support", "Touts Illinois record protecting 'reproductive freedom'; wants the filibuster gone partly to secure abortion rights (Oct 2026). No codification quote found."),
 wage=("Support", "Wants a $25 federal minimum wage (2026 campaign; earlier backed $17)."),
 imm=("Unclear", "No reform-specific statement found."),
 ice=("Support", "'I want to abolish ICE because this agency cannot be reformed' (Jan 26 2026 debate)."),
 isr=("Unclear", "Received AIPAC-aligned donor money; described as supportive of Israel (Al Jazeera, Mar 2026). No arms-conditioning statement found."))
NEW["Turek"] = newcomer(
 sch=("Unclear", "Repeatedly declined to commit when asked (Nov 2025–Nov 2026)."),
 m4a=("Lean oppose", "Backs a public option, not single-payer (May 2026 debate)."),
 roe=("Support", "Has called for codifying Roe; wrote bill to repeal Iowa's near-total ban."),
 wage=("Support", "$15 tied to inflation (Iowa PBS debate, May 5 2026); 'Dignity in Work' bill ending 14(c) subminimum wage."),
 imm=("Support", "'Fix this broken immigration system... overhaul ICE... pathway to legal status for people... who have not committed violent crimes' (May 2026)."),
 ice=("Support", "Wants to 'overhaul ICE'; enforcement under Trump 'fundamentally wrong' (May 2026). Voted for Iowa's 2024 state immigration-crime law."))
NEW["Hamilton"] = newcomer(
 sch=("Oppose", "'I'm not supporting Schumer... we need new leadership... young blood' (CNN, Sep 2026)."),
 m4a=("Lean oppose", "Platform: reverse Medicaid cuts, restore ACA credits, add Medicare dental/vision — no M4A."),
 roe=("Mixed", "Personally 'pro-life with a heavy heart' but would protect 'reproductive freedom'; wants birth control codified (Oct 2026)."),
 ai=("Support", "Supports AI regulation by Congress; data-center guardrails (Oct 2026)."),
 imm=("Mixed", "Named immigration reform a priority (Nov 5 2026) but 'no amnesty'; called Biden policy 'a disaster' (Oct 2026)."),
 ice=("Lean support", "'ICE's operation in southwest Kansas caused chaos... it can't happen this way again' (KSN Q&A, Oct 2026)."),
 isr=("Mixed", "Would halt some but not all weapons transfers; condemns destruction of Gaza; backs two-state solution (Oct 2026)."))
NEW["Jackson"] = newcomer(
 fil=("Support", "'Yes. I support eliminating the filibuster.' (Press Herald voter guide, fall 2026)."),
 sch=("Oppose", "Told Schumer he will 'support somebody else' (Nov 2 2026)."),
 m4a=("Support", "Platform calls for universal health care / Medicare for All (2026)."),
 roe=("Unclear", "No abortion or codification statement found."),
 imm=("Support", "'We need comprehensive immigration reform — not masked raids, detention quotas and fear' (fall 2026)."),
 ice=("Support", "'I think ICE needs to be abolished' (WGME, Aug 2026)."),
 isr=("Support", "'I support ending U.S. military aid that enables Israel's assault on Gaza, which is a genocide' (fall 2026)."))
NEW["El-Sayed"] = newcomer(
 fil=("Support", "Campaigned on abolishing the filibuster (2026)."),
 sch=("Oppose", "'I want new leadership'; backs Chris Van Hollen for leader (CNN, Nov 5 2026)."),
 m4a=("Support", "Centerpiece: 'Money out of politics! Money in your pocket! Medicare for All!' (2026)."),
 roe=("Unclear", "No abortion or codification statement found."),
 ice=("Support", "'There is no re-forming. There is no retraining. There is only abolishing ICE' (Apr 2026)."),
 isr=("Support", "Calls for a total arms embargo on Israel, incl. defensive weapons (Sep 2026); calls Gaza a 'genocide'."))
NEW["Flanagan"] = newcomer(
 sch=("Oppose", "'I am tremendously grateful for Chuck Schumer's leadership... it is time for new leadership' (Nov 4 2026)."),
 m4a=("Support", "'I will fight to pass Medicare for All' (MPR/KAXE guide, Sep 2026)."),
 roe=("Unclear", "No federal abortion or codification statement found."),
 wage=("Lean support", "Calls for raising the federal minimum wage (no figure found)."),
 ice=("Support", "'We have to rip ICE apart'; ICE 'shouldn't get another penny' (Aug 13 2026); 'ICE as it currently exists is not it.'"),
 isr=("Support", "'I would not vote... to send more weapons to Israel to fight this war' (spring 2026); ran on ending unconditional aid."))
NEW["Pappas"] = newcomer(
 fil=("Unclear", "Dodged; hasn't ruled out modifying or ending it (Jun 2026)."),
 sch=("Lean oppose", "Voters want 'a new generation of leadership in the Senate' (late Oct 2026); won't commit."),
 roe=("Support", "Voted for the Women's Health Protection Act in the House (Sep 24 2021, 218–211)."),
 imm=("Unclear", "'We need a secure border' (2026 debate); voted for Laken Riley Act."),
 ice=("Mixed", "Rejects abolishing ICE; wants reform; bill to redirect $75B in ICE funding to local police (Face the Nation, Oct 11 2026)."),
 isr=("Lean support", "Wants 'a reset with respect to the U.S. policy toward Israel' (Sep 2026); historically AIPAC-aligned."))
NEW["Cooper"] = newcomer(
 sch=("Unclear", "Repeatedly declined to say (2025–26)."),
 m4a=("Lean oppose", "Focuses on expanding existing coverage, not M4A (Oct 2026)."),
 roe=("Support", "Will 'defend reproductive rights'; vetoed NC 12-week ban as governor."),
 wage=("Unclear", "Backed raising NC minimum wage (2019); no federal figure found."),
 ice=("Lean support", "Called for 'immediate reforms' to ICE operations before further funding; vetoed sheriff-ICE cooperation bills."),
 isr=("Oppose", "'Generally does not believe we should withhold aid from a critical ally like Israel' (campaign, Aug 2025)."))
NEW["Brown"] = newcomer(
 fil=("Lean support", "Voted for the Jan 2022 voting-rights rules change as senator; no 2026 statement found."),
 sch=("Unclear", "Declined to commit; previously voted for Schumer as leader."),
 m4a=("Lean oppose", "Favors building on ACA / Medicare buy-in, not full M4A."),
 roe=("Support", "Supports 'abortion access for all women'; voted for WHPA in 2022."),
 wage=("Support", "Supports $17/hr (2026 campaign); sponsored $15 bill in 2021."),
 dcpr=("Unclear", "Cosponsored DC & PR bills as senator (2019-24); no 2026 statement found."),
 imm=("Unclear", "Backs border security and 'closing the border' (May 2026); supported DACA path (2017)."),
 ice=("Mixed", "'I'm not close enough to make those decisions... we need rules around ICE' — body cams, unmasking; does not support abolishing (May 2026)."),
 isr=("Oppose", "Voted against Sanders resolutions (Nov 2024); Israel has 'undeniable right to defend itself' (Aug 2025)."))
NEW["Andrews"] = newcomer(
 sch=("Oppose", "Campaigned against backing Schumer; 'it's time for a generational change on both sides of the aisle' (Fox, Nov 5 2026)."),
 roe=("Support", "Would seek to restore Roe v. Wade (Jun 2026)."),
 imm=("Mixed", "'We need a secure border... enforce the immigration laws'; 'deport illegal immigrants who break the law' (fall 2026)."),
 ice=("Lean support", "'Masked ICE agents ripping families apart... so deeply unamerican' (fall 2026)."),
 isr=("Unclear", "Opposes the Iran war (spring 2026); JACPAC-endorsed; no arms-conditioning statement found."))
NEW["Talarico"] = newcomer(
 fil=("Support", "'The filibuster... is a Jim Crow relic' — would abolish, keep a talking filibuster (NBC, Nov 2 2026)."),
 sch=("Unclear", "Won't commit; wants to 'hear about [Schumer's] vision' (Nov 2026)."),
 m4a=("Mixed", "'Medicare for Y'all' buy-in (Feb 2026); campaign later said he'd vote for M4A with public option as a bridge."),
 roe=("Lean support", "Voted against SB 8, Texas's six-week ban, in the Texas House (May 6 2021). No federal codification statement found."),
 ai=("Support", "Opposes federal preemption of state AI rules; backs kids' online safety & worker AI-surveillance limits (Feb 2026)."),
 imm=("Support", "Supports the Dignity Act framework (Feb 2026)."),
 ice=("Mixed", "Won't abolish ICE, but it 'should go after gang members and human traffickers, not moms and babies' (2026)."),
 isr=("Support", "'We should stop offensive weapons sales to the Netanyahu government,' keep Iron Dome (Feb 2026)."))
NEW["Colom"] = newcomer(
 sch=("Oppose", "Said he won't support Schumer (Democracy Now, Nov 6 2026)."),
 roe=("Mixed", "'As a Christian... I've always been pro-life' but trusts women to make their own choices (2026)."),
 wage=("Lean support", "'We haven't raised the minimum wage in close to 20 years' — would raise it (no figure)."))
NEW["Peltola"] = newcomer(
 sch=("Unclear", "Schumer recruit; no commitment found."),
 roe=("Support", "Abortion-rights supporter; backed federal protections in the House."),
 isr=("Unclear", "JACPAC-endorsed, but no statement on conditioning arms found."))
NEW["MN appointee"] = newcomer(sch=("Unclear", "Not yet named. Angie Craig widely speculated."))

NEW["Moore"] = r_newcomer("Moore")
NEW["Barr"] = r_newcomer("Barr")
NEW["Letlow"] = r_newcomer("Letlow")
NEW["Alme"] = r_newcomer("Alme")
NEW["Hern"] = r_newcomer("Hern")
NEW["Hageman"] = r_newcomer("Hageman")
NEW["TN appointee"] = r_newcomer(sch=("N/A", "Not yet named. Glenn Jacobs & Rep. Tim Burchett floated."))

def _old_record(key, party):
    if key in NEW:
        return dict(NEW[key])
    d = dem_defaults(key) if party.startswith(("D", "I")) else rep_defaults(key)
    d.update(OV.get(key, {}))
    return d

def senator_record(key, party):
    import issue_meta, issues2
    d = _old_record(key, party)
    is_new = key in NEW
    out = {}
    for k, _s, _a, _n, who in issue_meta.META:
        if k in d and k not in issues2.POS:
            out[k] = d[k]
            continue
        if (who == "sitting" and is_new) or (who == "new" and not is_new):
            out[k] = d.get(k, issue_meta.NOT_RESEARCHED[who])
            continue
        out[k] = issues2.POS.get(k, {}).get(key, d.get(k, ("Unclear", "No statement or recorded vote found.")))
    return out
