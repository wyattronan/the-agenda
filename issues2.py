"""Positions on the 26 issues added Nov 6 2026. Only statements, cosponsorships and recorded votes; no party inference.
POS[issue][senator_key] = (stance, evidence). Anything missing defaults to Unclear."""
POS = {}
def P(issue, keys, stance, ev):
    for k in ([keys] if isinstance(keys, str) else keys):
        POS.setdefault(issue, {})[k] = (stance, ev)

import senate_data as _sd
ROSTER = _sd.ROSTER
NEWK = _sd.NEW_D | _sd.NEW_R
INC = [r[1] for r in ROSTER if r[1] not in NEWK]
INC_D = [r[1] for r in ROSTER if r[1] not in NEWK and r[3].startswith(("D", "I"))]
INC_R = [r[1] for r in ROSTER if r[1] not in NEWK and r[3].startswith("R")]
D_2023PLUS = {"Fetterman", "Welch", "Schiff", "Kim", "Slotkin", "Gallego", "Blunt Rochester", "Alsobrooks"}
D_2022 = [k for k in INC_D if k not in D_2023PLUS]                       # Dems serving in 2022
D_2024 = [k for k in INC_D if k not in {"Schiff", "Kim", "Slotkin", "Gallego", "Blunt Rochester", "Alsobrooks"}]
R_OLD = _sd.R_OLD                                                          # Rs serving 2021-22
R_2024 = set(R_OLD) | {"Britt", "Budd", "Schmitt", "Ricketts"}
HOUSE_R_NEW = ["Moore", "Barr", "Letlow", "Hern", "Hageman"]

def cos(issue, names, stance, ev):
    P(issue, names, stance, ev)

# ---------------- ACA enhanced premium tax credits ----------------
V = "Voted to advance Democrats' clean 3-year extension of the enhanced ACA credits (Dec 11 2025, 51–48, failed)."
P("aca", INC_D, "Support", V)
P("aca", ["Hawley", "Murkowski"], "Support", "One of four Republicans who " + V[0].lower() + V[1:])
P("aca", [k for k in INC_R if k not in ("Hawley", "Murkowski")], "Oppose",
  "Voted against advancing Democrats' 3-year extension of the enhanced ACA credits (Dec 11 2025, 51–48).")
P("aca", "Paul", "Oppose", "Voted against both the Democratic 3-year extension and the GOP HSA alternative (Dec 11 2025).")
P("aca", "Brown", "Lean support", "Voted for the American Rescue Plan (2021), which created the enhanced credits, and the IRA (2022), which extended them.")

# ---------------- OBBBA Medicaid cuts (and top-bracket cuts) ----------------
OB_NO = "Voted against the One Big Beautiful Bill Act, which made the Medicaid cuts and work requirements (Jul 1 2025, 51–50)."
OB_YES = "Voted for the One Big Beautiful Bill Act, which made the Medicaid cuts and work requirements (Jul 1 2025, 51–50)."
P("medicaid", INC_D, "Lean support", OB_NO)
P("medicaid", INC_R, "Oppose", OB_YES)
P("medicaid", "Hawley", "Mixed", "Voted for the OBBBA (Jul 2025) but called the Medicaid cuts 'a mistake' and pledged to 'do everything in my power to reverse future cuts to Medicaid.'")
P("medicaid", "Murkowski", "Mixed", "Backed Wyden's amendment to shield Medicaid (Apr 2025, failed 49–50), then cast the deciding vote for the OBBBA (Jul 1 2025).")
P("medicaid", "Paul", "Unclear", "Voted against the OBBBA over its debt-limit increase, not its Medicaid cuts (Jul 2025).")
P("medicaid", HOUSE_R_NEW, "Oppose", "Voted for the One Big Beautiful Bill Act in the House (Jul 3 2025, 218–214).")
P("medicaid", "Pappas", "Lean support", "Voted against the One Big Beautiful Bill Act in the House (Jul 3 2025, 218–214).")

TX_NO = "Voted against the One Big Beautiful Bill Act and its top-bracket tax cuts (Jul 1 2025, 51–50)."
TX_YES = "Voted for the One Big Beautiful Bill Act and its tax cuts (Jul 1 2025, 51–50)."
P("toptax", INC_D, "Lean support", TX_NO)
P("toptax", INC_R, "Oppose", TX_YES)
P("toptax", "Paul", "Unclear", "Voted against the OBBBA over its debt-limit increase, not its tax cuts (Jul 2025).")
P("toptax", HOUSE_R_NEW, "Oppose", "Voted for the One Big Beautiful Bill Act and its tax cuts in the House (Jul 3 2025, 218–214).")
P("toptax", "Pappas", "Lean support", "Voted against the One Big Beautiful Bill Act in the House (Jul 3 2025, 218–214).")

# ---------------- Tariff emergencies + Trade Review Act ----------------
P("tariff", INC_D, "Support", "Voted to end the Brazil, Canada and global tariff emergencies (Oct 28–30 2025).")
P("tariff", INC_R, "Oppose", "Voted against ending the Brazil tariff emergency (Oct 28 2025, 52–48).")
P("tariff", "Paul", "Support", "Co-led the resolutions ending the tariff emergencies (Oct 2025): 'end these unconstitutional import taxes.'")
P("tariff", "Murkowski", "Support", "Voted to end the Brazil, Canada and global tariff emergencies (Oct 2025); cosponsor, Trade Review Act S.1272.")
TRA = "Cosponsor, Trade Review Act S.1272 (Apr 2025), requiring Congress to approve new tariffs."
for k in ["Cantwell", "Klobuchar", "Warner", "Bennet", "Welch", "Coons", "Blumenthal"]:
    P("tariff", k, "Support", "Voted to end the tariff emergencies (Oct 2025); " + TRA[0].lower() + TRA[1:])
P("tariff", ["Grassley", "Moran", "Young"], "Mixed", "Cosponsor of the Trade Review Act S.1272 (Apr 2025), but voted against ending the Brazil tariff emergency (Oct 28 2025).")

# ---------------- Iran War Powers ----------------
P("iran", INC_D, "Support", "Voted for Kaine's Iran war powers resolution (Apr 15 2026, 47–52).")
P("iran", "Fetterman", "Oppose", "Only Democrat to vote against the Iran war powers resolution (Apr 15 2026, 47–52).")
P("iran", INC_R, "Oppose", "Voted against the Iran war powers resolution (Apr 15 2026, 47–52).")
P("iran", "Paul", "Support", "Only Republican to vote for the Iran war powers resolution (Apr 15 2026, 47–52).")

# ---------------- 2024 bipartisan border deal (sitting only) ----------------
B1 = "Voted to advance the bipartisan border deal (Feb 7 2024, 49–50, and May 23 2024, 43–50)."
P("border24", [k for k in D_2024], "Support", B1)
P("border24", ["Sanders", "Markey", "Padilla"], "Oppose", "Voted against advancing the bipartisan border deal both times (Feb 7 and May 23 2024).")
P("border24", "Warren", "Lean oppose", "Voted against advancing the bipartisan border deal (Feb 7 2024, 49–50).")
P("border24", "Booker", "Lean oppose", "Voted for the package in Feb 2024 but against the standalone bill in May 2024: 'it includes several provisions that will violate Americans' shared values.'")
P("border24", "Schumer", "Support", "Brought the deal to the floor twice (Feb & May 2024); his Feb 'no' was procedural, to allow a re-vote.")
P("border24", "Murphy", "Support", "Lead Democratic negotiator of the 2024 deal; voted to advance it both times.")
P("border24", "Fetterman", "Support", "Voted to advance it both times: 'I know we must secure our border, and this bill would help do that' (May 2024).")
P("border24", [k for k in R_2024], "Oppose", "Voted against advancing the bipartisan border deal (Feb 7 & May 23 2024).")
P("border24", "Murkowski", "Support", "Only Republican to vote to advance the deal both times (Feb 7 & May 23 2024).")
P("border24", "Lankford", "Mixed", "Lead GOP negotiator; voted for it in Feb 2024 but against the May 2024 re-vote, calling it 'a prop.'")
P("border24", "McCormick", "Lean oppose", "Called it a 'good, well meaning effort' that 'didn't accomplish the mission'; preferred H.R. 2 (May 2024, as candidate).")

# ---------------- Child Tax Credit ----------------
C24 = "Voted to advance the bipartisan Wyden–Smith bill expanding the Child Tax Credit (Aug 1 2024, 48–44)."
P("ctc", D_2024, "Lean support", C24)
P("ctc", "Sanders", "Unclear", "Voted against the 2024 Wyden–Smith tax package, which paired a modest CTC expansion with business tax breaks (Aug 1 2024).")
P("ctc", "Schumer", "Lean support", "Brought the 2024 CTC expansion to the floor; his 'no' was procedural (Aug 1 2024).")
P("ctc", ["Fetterman", "Warner"], "Unclear", "Did not vote on the 2024 CTC expansion (Aug 1 2024); no other statement found.")
P("ctc", [k for k in R_2024], "Lean oppose", "Voted against advancing the bipartisan bill expanding the Child Tax Credit (Aug 1 2024, 48–44).")
P("ctc", ["Hawley", "Scott (FL)"], "Lean support", "One of three Republicans to vote to advance the 2024 Child Tax Credit expansion (Aug 1 2024).")
P("ctc", ["Hoeven", "Scott (SC)"], "Unclear", "Did not vote on the 2024 CTC expansion (Aug 1 2024); no other statement found.")
P("ctc", "Booker", "Support", "Long-time sponsor of permanent CTC expansion (American Family Act); Keep Your Pay Act raises it to $4,320 per young child (2026).")

# ---------------- Drug price negotiation ----------------
IRA_Y = "Voted for the Inflation Reduction Act, which created Medicare drug negotiation (Aug 7 2022, 51–50)."
IRA_N = "Voted against the Inflation Reduction Act, which created Medicare drug negotiation (Aug 7 2022, 51–50)."
P("drugneg", D_2022, "Lean support", IRA_Y)
P("drugneg", list(R_OLD), "Lean oppose", IRA_N)
SM = "Cosponsor, SMART Prices Act S.1836 (May 2025), raising negotiated drugs from 15 to 50 a year."
P("drugneg", ["Klobuchar", "Welch", "King", "Cantwell", "Reed", "Whitehouse", "Duckworth", "Warren", "Gillibrand", "Merkley",
              "Murray", "Blumenthal", "Cortez Masto", "Baldwin", "Booker", "Van Hollen", "Murphy", "Fetterman", "Markey",
              "Luján", "Hassan", "Heinrich", "Slotkin", "Bennet"], "Support", SM)
P("drugneg", "Brown", "Lean support", "Voted for the Inflation Reduction Act's Medicare drug negotiation (Aug 7 2022).")

# ---------------- Prior authorization ----------------
PA = "Cosponsor, Improving Seniors' Timely Access to Care Act S.1816 (May 2025), streamlining Medicare Advantage prior authorization."
P("priorauth", ["Warner", "Hassan", "Fetterman", "Klobuchar", "Capito", "Hickenlooper", "Lankford", "Merkley", "Kaine",
                "Rounds", "Padilla", "Hagerty", "Kim", "Boozman", "Moran", "Gillibrand", "Cantwell", "Hirono", "Booker",
                "Welch", "Whitehouse", "Budd", "Cortez Masto", "Sheehy", "Baldwin", "Ricketts", "Blumenthal", "Warren",
                "Duckworth", "Hoeven", "Scott (FL)", "Kelly", "Rosen", "Heinrich", "Fischer", "Coons", "Hawley", "Murray"],
  "Support", PA)

# ---------------- Childcare ----------------
CC = "Cosponsor, Child Care for Working Families Act S.2295 (Jul 2025), capping costs at 7% of income."
P("childcare", ["Murray"], "Support", "Sponsor, Child Care for Working Families Act S.2295 (Jul 2025), capping costs at 7% of income.")
P("childcare", ["Kaine", "Hirono", "Kim", "Reed", "Whitehouse", "Cortez Masto"], "Support", CC)

# ---------------- Meatpackers ----------------
P("meat", "Schumer", "Support", "Sponsor, Family Grocery and Farmer Relief Act (Mar 2026), forcing big meatpackers to pick one meat.")
P("meat", ["Booker", "Welch", "Warren", "Sanders", "Gallego", "Merkley", "Schatz", "Markey", "Kim", "Murphy", "Whitehouse"],
  "Support", "Cosponsor, Family Grocery and Farmer Relief Act (Mar 2026), which breaks up dominant meatpackers.")

# ---------------- Clean energy credits (sitting only) ----------------
P("clean", "Schumer", "Support", "Sponsor, Lowering Electric Bills Act S.2681 (Aug 2025), restoring IRA clean-energy credits.")
P("clean", ["Wyden", "Warner", "Cantwell", "Bennet", "Schatz", "Duckworth", "Reed", "Hickenlooper", "Gallego", "Blumenthal",
            "Van Hollen", "Kim", "Warren", "Gillibrand", "Klobuchar", "Rosen", "Padilla", "Booker", "Kelly", "King",
            "Hirono", "Murray", "Markey", "Slotkin", "Coons", "Whitehouse", "Alsobrooks", "Blunt Rochester", "Merkley", "Ossoff"],
  "Support", "Cosponsor, Lowering Electric Bills Act S.2681 (Aug 2025), restoring IRA clean-energy credits.")
P("clean", INC_R, "Lean oppose", "Voted for the OBBBA, which phased out the IRA wind, solar and residential clean-energy credits (Jul 1 2025).")
P("clean", "Paul", "Unclear", "Voted against the OBBBA over its debt-limit increase (Jul 2025); no clean-credit statement found.")

# ---------------- Keep Your Pay (sitting only) ----------------
P("keeppay", "Booker", "Support", "Sponsor, Keep Your Pay Act (Mar 10 2026): 'No household in America should pay federal income tax on their first $75,000.'")

# ---------------- Stock trading ban ----------------
HON = "Cosponsor, HONEST Act S.1498 (Peters–Hawley–Merkley–Ossoff), banning stock trading by members, the President and VP."
P("stock", ["Hawley"], "Support", "Sponsor, HONEST Act S.1498, banning stock trading by members of Congress, the President and VP; passed committee 8–7 (Jul 30 2025).")
P("stock", ["Merkley", "Ossoff", "Cortez Masto"], "Support", HON)
P("stock", ["Hassan", "Blumenthal", "Fetterman", "Kim", "Gallego", "Slotkin"], "Support",
  "Voted for the HONEST Act in Homeland Security Committee (Jul 30 2025, 8–7).")
P("stock", "Moreno", "Mixed", "Original cosponsor of the HONEST Act but called the committee version 'a publicity show' (Jul 2025).")
P("stock", "Paul", "Oppose", "Voted against the HONEST Act in committee, calling it 'a really crummy bill' (Jul 30 2025).")
P("stock", "Johnson", "Oppose", "Voted against the HONEST Act in committee, calling it 'legislative demagoguery' (Jul 30 2025).")
P("stock", "Scott (FL)", "Oppose", "Voted against the HONEST Act in committee: 'This idea that we are going to attack people because they make money is wrong' (Jul 2025).")
BCS = "Cosponsor, Ban Congressional Stock Trading Act S.1879 (May 2025), requiring blind trusts for members."
P("stock", ["Kelly", "Baldwin", "Duckworth", "Schatz", "Warnock", "Bennet", "Gillibrand"], "Support", BCS)

# ---------------- Data centers ----------------
RPA_Y = "Voted to advance the GOP's Ratepayer Protection Act, which asks states to consider making big data centers pay their full grid costs (Sep 30 2026, 57–43)."
RPA_N = "Voted against the GOP's Ratepayer Protection Act (Sep 30 2026), which Democrats called too weak because it only asks states to consider charging data centers; no individual statement found."
P("datactr", INC_R, "Lean support", RPA_Y)
P("datactr", INC_D, "Unclear", RPA_N)
P("datactr", ["Hassan", "Klobuchar", "Ossoff", "Warnock"], "Lean support", "One of four Democrats who " + RPA_Y[0].lower() + RPA_Y[1:])
P("datactr", "Schumer", "Support", "'Senate Democrats want to make it mandatory for data centers to cover their own costs, by law' (Sep 30 2026); voted against the voluntary GOP bill.")
P("datactr", "Blumenthal", "Support", "Co-led the bipartisan GRID Act with Hawley (Feb 2026); 'I support ratepayer protection... not this bill' (Sep 30 2026).")
P("datactr", "Hawley", "Support", "Co-led the bipartisan GRID Act to keep data-center costs off household bills (Feb 2026); voted for the GOP bill (Sep 30 2026).")
P("datactr", "Van Hollen", "Support", "Sponsor, Power for the People Act (Jan 2026), requiring data centers to supply their own power and pay for grid upgrades.")
P("datactr", "Schiff", "Support", "Filed a bill requiring data centers over 50 MW to secure their own power and pay for grid upgrades (Jun 2026).")
P("datactr", "Heinrich", "Support", "Co-led the bipartisan American Affordability and Jobs Act requiring data centers to pay their own costs (Sep 2026); said the GOP bill 'suggests, but does not require' it.")
P("datactr", "Hickenlooper", "Lean support", "'Republicans' Ratepayer Protection Act has no teeth' (Sep 2026); voted against it.")
P("datactr", ["Lee", "Capito", "Whitehouse"], "Support", "Co-led the bipartisan American Affordability and Jobs Act of 2026, requiring data centers to pay for their own power costs (Sep 2026).")

# ---------------- Grocery price gouging / surveillance pricing ----------------
P("gouge", "Warren", "Support", "Sponsor, Price Gouging Prevention Act S.2321 (Jul 2025).")
P("gouge", ["Markey", "Sanders", "Baldwin", "Slotkin", "Fetterman", "Kim", "Blumenthal", "Merkley", "Whitehouse"], "Support",
  "Cosponsor, Price Gouging Prevention Act S.2321 (Jul 2025).")
P("gouge", "Luján", "Support", "Sponsor, Stop Price Gouging in Grocery Stores Act S.3892 (Feb 2026), banning grocery price gouging and surveillance pricing.")
P("gouge", ["Heinrich", "Ossoff"], "Support", "Cosponsor, Stop Price Gouging in Grocery Stores Act S.3892 (2026), banning grocery price gouging and surveillance pricing.")
P("gouge", "Merkley", "Support", "Co-lead, Stop Price Gouging in Grocery Stores Act S.3892 (Feb 2026); cosponsor, Price Gouging Prevention Act S.2321.")
P("gouge", "Gallego", "Support", "Sponsor, One Fair Price Act S.3387 (Dec 2025), banning surveillance-based pricing.")
P("gouge", "Gillibrand", "Support", "Cosponsor, One Fair Price Act S.3387, banning surveillance-based pricing.")

# ---------------- Down payment assistance ----------------
P("downpay", "Warnock", "Support", "Sponsor, Downpayment Toward Equity Act S.967 (Mar 2025), grants for first-generation homebuyers.")
P("downpay", ["Padilla", "Kaine", "Warner", "Van Hollen", "Booker"], "Support", "Cosponsor, Downpayment Toward Equity Act S.967 (Mar 2025).")

# ---------------- Gas tax holiday ----------------
P("gastax", ["Kelly"], "Support", "Sponsor, Gas Prices Relief Act of 2026, suspending the federal gas tax through Oct 1 2026 (Mar 2026); also led the 2022 version.")
P("gastax", ["Blumenthal"], "Support", "Co-lead, Gas Prices Relief Act of 2026 (Mar 2026).")
P("gastax", ["Hassan", "Cortez Masto", "Warnock", "Rosen"], "Support", "Co-led the 2022 Gas Prices Relief Act suspending the federal gas tax (Feb 2022).")
P("gastax", "Hawley", "Support", "Sponsor, Gas Tax Suspension Act: a 90-day federal gas and diesel tax holiday (May 2026).")
P("gastax", "Pappas", "Support", "Sponsored the House Gas Prices Relief Act of 2026, suspending the gas tax through Oct 1 2026.")
P("gastax", "Thune", "Lean oppose", "Warned a gas-tax pause leaves a 'big hole' in the Highway Trust Fund (May 2026).")
P("gastax", "Murphy", "Lean oppose", "On Trump's gas-tax holiday: end the Iran war and 'stop looking for other gimmicks' (May 2026).")

# ---------------- Gerrymandering ----------------
FTV = "Voted to advance the Freedom to Vote: John R. Lewis Act, which bans partisan gerrymandering (Jan 19 2022)."
P("gerry", D_2022, "Lean support", FTV)
P("gerry", [k for k in R_OLD if k != "Murkowski"], "Lean oppose", "Voted against advancing the Freedom to Vote: John R. Lewis Act, which bans partisan gerrymandering (Jan 19 2022).")
P("gerry", "Padilla", "Support", "Sponsor, Redistricting Reform Act S.2885 (Sep 2025): independent commissions and no mid-decade redistricting.")
P("gerry", ["King", "Warnock", "Schiff"], "Support", "Cosponsor, Redistricting Reform Act S.2885 (Sep 2025), banning partisan and mid-decade gerrymanders.")
P("gerry", "Brown", "Lean support", "Voted to advance the Freedom to Vote: John R. Lewis Act, which bans partisan gerrymandering (Jan 19 2022).")

# ---------------- Rental assistance (sitting only) ----------------
CAH = "Cosponsor, Choice in Affordable Housing Act S.890 (Mar 2025), expanding funding for and landlord use of Section 8 vouchers."
P("rental", "Coons", "Support", "Sponsor, Choice in Affordable Housing Act S.890 (Mar 2025), expanding Section 8 voucher access.")
P("rental", ["Cramer"], "Support", "Republican co-lead, Choice in Affordable Housing Act S.890 (Mar 2025).")
P("rental", ["Warnock", "Moran", "Curtis", "Heinrich"], "Support", CAH)
P("rental", "Schiff", "Support", "Sponsor, a 2025 housing bill authorizing more vouchers and eviction assistance (S.3464).")

# ---------------- ROAD to Housing ----------------
RD = "Voted for final passage of the 21st Century ROAD to Housing Act (Jun 22 2026, 85–5), which became law Jul 11 2026."
P("road", INC, "Support", RD)
P("road", ["Johnson", "Lee", "Paul", "Scott (FL)"], "Oppose", "One of five senators to vote against the 21st Century ROAD to Housing Act (Jun 22 2026, 85–5).")
P("road", ["Bennet", "Cruz", "Curtis", "Justice", "Murray", "Slotkin", "Whitehouse", "Young"], "Unclear",
  "Did not vote on final passage of the ROAD to Housing Act (Jun 22 2026); its earlier 89–10 Senate vote isn't broken out here.")
P("road", "Scott (SC)", "Support", "Co-wrote the ROAD to Housing Act as Banking chair; it passed committee 24–0 and became law Jul 11 2026.")
P("road", "Warren", "Support", "Co-wrote the ROAD to Housing Act as Banking ranking member; it became law Jul 11 2026.")

P("gerry", "Murkowski", "Lean oppose", "Voted against advancing the Freedom to Vote: John R. Lewis Act, which bans partisan gerrymandering (Jan 19 2022).")

# ================= Senators-elect =================
# Flanagan (MN)
P("priorauth", "Flanagan", "Support", "Platform: 'End prior authorization' (Aug 2026 primary-night agenda).")
P("childcare", "Flanagan", "Support", "'I'll fight to... pass universal childcare' (MPR/KAXE voter guide, Sep 2026).")
P("pro", "Flanagan", "Support", "Pledged to 'pass the PRO Act to strengthen unions' (MoveOn endorsement profile, 2026).")
P("pfl", "Flanagan", "Support", "'We need a national paid leave policy' (City Cast, 2026); co-founded Minnesotans for Paid Family and Medical Leave.")
P("repair", "Flanagan", "Support", "Will 'protect farmers' right to repair their own equipment' (MPR/KAXE voter guide, Sep 2026).")
P("pacs", "Flanagan", "Lean support", "'Get Big Money out of our politics'; refuses corporate PAC money; backs banning corporate money in elections (2026).")
P("drugneg", "Flanagan", "Lean support", "Backs allowing Medicare to negotiate drug prices (Minnesota Reformer, Jul 2026).")
P("tariff", "Flanagan", "Lean support", "Will 'protect [farmers'] markets from Trump's reckless tariffs' (Sep 2026).")
P("wage", "Flanagan", "Support", "Backs raising the federal minimum wage from $7.25 to $20 an hour (Minnesota Reformer, Jul 2026).")
P("roe", "Flanagan", "Support", "Platform: pass the Women's Health Protection Act to codify reproductive rights (2026).")

# Jackson (ME)
P("stock", "Jackson", "Support", "'In the Senate, I'll... ban congressional stock trading' (Press Herald voter guide, fall 2026).")
P("pacs", "Jackson", "Lean support", "'I'll reject corporate PAC money, fight to overturn Citizens United, require full disclosure' (fall 2026).")
P("pfl", "Jackson", "Lean support", "As Maine Senate President helped pass a 12-week paid family and medical leave program; no federal plan found.")
P("roe", "Jackson", "Lean support", "As Maine Senate President helped pass 'some of the strongest abortion protections in the country'; no federal codification quote found.")

# El-Sayed (MI)
P("pro", "El-Sayed", "Support", "'Passing the PRO Act to stand with unions like the UAW' (final primary debate, Jul 2026).")
P("pacs", "El-Sayed", "Support", "Pledged to cosponsor Slotkin's Ban Corporate PACs Act; refuses corporate PAC and super PAC money (2026).")
P("stock", "El-Sayed", "Support", "Part of End Citizens United's Unrig Washington program, which commits candidates to a congressional stock-trading ban (2026).")
P("gerry", "El-Sayed", "Support", "'Money out of politics' platform includes ending partisan gerrymandering (2026).")

# Stratton (IL)
P("pacs", "Stratton", "Support", "Promises to 'fight for campaign finance reform and a ban on corporate PAC money' (Feb 2026 debate).")
P("stock", "Stratton", "Lean support", "Endorsed by End Citizens United, whose pledge includes banning congressional stock trading (Nov 2025).")

# Turek (IA)
P("stock", "Turek", "Support", "'I think we need to ban members of Congress and the Supreme Court from owning and trading stocks' (2026).")
P("pacs", "Turek", "Support", "Platform: 'Ban corporate PAC money in campaigns'; constitutional amendment to reverse Citizens United (Mar 2026).")
P("termlim", "Turek", "Support", "Platform: 'Set term limits for Members of Congress and Supreme Court Justices' (Mar 2026).")
P("pro", "Turek", "Support", "Platform: 'Pass the PRO Act to strengthen our unions' (Mar 2026).")
P("pfl", "Turek", "Support", "Platform: 'Ensure every Iowan has access to paid family and medical leave' (Mar 2026).")
P("repair", "Turek", "Support", "Wants a farm bill with a 'right to repair'; backed Iowa's 2026 farm right-to-repair bill as a legislator.")
P("tariff", "Turek", "Support", "Proposes 'ending the Trump administration's tariffs' (The Gazette, 2026).")
P("toptax", "Turek", "Lean support", "Proposes 'closing tax loopholes for billionaires and large businesses' (The Gazette, 2026).")

# Hamilton (KS)
P("tariff", "Hamilton", "Lean support", "Campaign platform opposes Trump's tariffs (May 2026).")
P("termlim", "Hamilton", "Support", "Supports 'either term limits or age limits' for members of Congress (May 2026).")
P("stock", "Hamilton", "Support", "Committed to banning lawmakers from trading stocks (Oct 2026).")
P("datactr", "Hamilton", "Support", "Committed to 'forcing data centers to pay for their own energy' (Oct 2026).")
P("aca", "Hamilton", "Support", "Wants to 'restore subsidies so people can afford insurance' (American Prospect, Oct 2026).")
P("wage", "Hamilton", "Lean support", "Supports raising the federal minimum wage (May 2026 platform); no figure found.")

# Talarico (TX)
P("pacs", "Talarico", "Support", "'I don't care if they're Democratic super PACs or Republican super PACs, I think we got to ban them all' (CNN town hall, Oct 2026).")
P("gerry", "Talarico", "Support", "'We must finally pass a national ban to end gerrymandering' (May 2026).")
P("stock", "Talarico", "Support", "First bill would ban members of Congress from trading stocks (May 2026).")
P("termlim", "Talarico", "Support", "'We must pass term limits' for Congress and the Supreme Court (May 2026).")
P("toptax", "Talarico", "Support", "Would repeal OBBBA tax breaks for the top 1% to fund a 'cost-of-living tax cut' (Aug 2026 economic agenda).")
P("childcare", "Talarico", "Support", "Economic agenda: 'passing universal childcare' (Aug 2026).")
P("pfl", "Talarico", "Support", "Economic agenda: universal childcare 'and paid family leave' (Aug 2026).")
P("ctc", "Talarico", "Support", "Economic agenda: 'permanently expanding the child tax credit' (Aug 2026).")
P("iran", "Talarico", "Lean support", "Calls for 'ending the war in Iran' to cut the deficit (CNN town hall, Oct 2026).")

# Cooper (NC)
P("stock", "Cooper", "Support", "Backs banning stock trading by members of Congress and the president: 'It's wrong. It leads to corruption' (Dec 2025).")
P("aca", "Cooper", "Support", "Priority: 'restoring the tax credits for people's health insurance' (2026).")
P("medicaid", "Cooper", "Support", "Wants to 'reverse cuts to the Affordable Care Act and Medicaid' (2026).")
P("tariff", "Cooper", "Support", "Congress must 'take back the constitutional authority on trading and tariffs' and end tariffs paid by consumers (Jun 2026).")

# Brown (OH)
P("stock", "Brown", "Support", "'No one – NO ONE – who serves in Congress, or their spouse, should be able to trade stocks' (campaign site, 2026).")
P("tariff", "Brown", "Lean support", "'The second thing we should do is fight to end the tariffs' (2026); has backed targeted tariffs in the past.")
P("datactr", "Brown", "Support", "Would 'cap how much utility companies can increase electricity rates' and require data centers to cover their full utility costs (2026).")
P("priorauth", "Brown", "Support", "Platform restricts health insurance companies from denying care (2026); co-led the prior-authorization bill as senator (2022).")
P("medicaid", "Brown", "Lean support", "Attacks Husted for casting 'the deciding vote to take healthcare away from 490,000 Ohioans' (Aug 2026).")
P("iran", "Brown", "Lean support", "'The first thing we should do is fight to end the war' (2026).")

# Andrews (SC)
P("stock", "Andrews", "Support", "'My Taxpayer Pledge starts with Congress: ban members from trading stocks' (Nov 2026).")
P("termlim", "Andrews", "Support", "Supports congressional term limits (2026 platform).")
P("pacs", "Andrews", "Support", "Supports banning corporate PAC money for politicians (Jun 2026).")
P("pfl", "Andrews", "Support", "Platform: 'Expand affordable child care and paid family leave' (2026).")
P("childcare", "Andrews", "Lean support", "Platform: 'Expand affordable child care' (2026); no 7%-cap or universal plan specified.")
P("tariff", "Andrews", "Support", "'Stop the unconstitutional on-again, off-again tariffs' (Sep 2026).")
P("ctc", "Andrews", "Lean support", "Wants to prioritize 'making the child tax credit permanent' (2025).")
P("toptax", "Andrews", "Lean support", "Wants to 'cut tax breaks for billionaires' (Jun 2026).")
P("medicaid", "Andrews", "Lean support", "Supports expanding access to Medicaid and Medicare (Jun 2026).")

# Colom (MS)
P("aca", "Colom", "Support", "Supports extending Affordable Care Act tax credits: 'We have to cancel those healthcare cuts' (2026).")
P("medicaid", "Colom", "Support", "Proposes restoring the OBBBA Medicaid cuts, paid for by taxing very high earners (2026).")
P("tariff", "Colom", "Lean support", "'The tariffs are a sales tax'; wants 'to eliminate tariffs' (Oct 2026). Earlier called tariffs 'a really good tool.'")
P("stock", "Colom", "Support", "Wants to ban lawmakers from trading individual stocks (Neshoba County Fair, Jun 2026).")
P("toptax", "Colom", "Lean support", "Champions a tax increase on high-income earners to restore health coverage (2026).")
P("iran", "Colom", "Lean support", "Wants 'lower gas prices by getting us out of the war in Iran' (Oct 2026).")

# Peltola (AK)
P("stock", "Peltola", "Support", "'Congress really gets serious about saying no to allowing stock trading for members of Congress' (Aug 2026).")
P("termlim", "Peltola", "Support", "Called for congressional term limits (Juneau rally, May 2026).")
P("pacs", "Peltola", "Lean support", "Backs a constitutional amendment overturning Citizens United and Alaska-style limits on corporate and PAC money (2026).")
P("iran", "Peltola", "Support", "Supports Congress limiting the Iran war and 'would support a war powers resolution' (May 2026).")
P("medicaid", "Peltola", "Lean support", "Pledges to 'reverse harmful healthcare cuts' (2026 voter pamphlet).")
P("aca", "Peltola", "Lean support", "Criticized double or triple insurance costs after the ACA credits were removed (Aug 2026).")
P("tariff", "Peltola", "Lean support", "'The tariffs drove costs up'; criticizes the administration's 'outsized role' on tariffs (2026).")

# Pappas (NH)
P("stock", "Pappas", "Support", "Led House efforts to ban member stock trading; cosponsor, Restore Trust in Congress Act (2025-26).")
P("aca", "Pappas", "Support", "'We need to extend Affordable Care Act premium tax credits' (The Dartmouth, Apr 2026).")
P("medicaid", "Pappas", "Support", "'We also need to reverse Medicaid cuts' (Apr 2026); voted against the OBBBA (Jul 2025).")
P("tariff", "Pappas", "Support", "'Fighting to stop Trump's tariffs that are driving up costs' (Jun 2026).")
P("downpay", "Pappas", "Lean support", "Would 'support first-time homebuyers with tax credits' (Apr 2026).")
P("pro", "Pappas", "Support", "Voted for the PRO Act in the House (Mar 9 2021, 225–206).")
P("pacs", "Pappas", "Unclear", "Refuses corporate PAC money for himself; no position on a ban found.")

# Republican senators-elect
P("pro", ["Moore", "Barr", "Hern"], "Oppose", "Voted against the PRO Act in the House (Mar 9 2021, 225–206).")
P("termlim", ["Moore", "Hern", "Letlow"], "Support", "Cosponsor, H.J.Res. 12 (119th), a constitutional amendment limiting House members to three terms and senators to two.")
P("termlim", "Alme", "Support", "Supports mandatory term limits (Club for Growth / MTN, 2026).")
P("tariff", "Alme", "Lean oppose", "Was 'originally skeptical' of Trump's tariffs but says Canada has 'gone with unfair trade for too long' (Oct 2026).")
P("tariff", "Barr", "Oppose", "Supports Trump's tariff and trade positions (Oct 2025).")
P("gastax", "Talarico", "Support", "Backs suspending the federal gas tax (2026), per user-supplied note; see Punchbowl News report.")
