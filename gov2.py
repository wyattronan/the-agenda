"""Second batch of governor issues (Nov 2026), Democratic governors only.

Positions come from campaign plans, State of the State / budget addresses and signed laws.
No position is filled from party: anyone without a statement or action stays Unclear.
"""

# Areas for the Governors tab (key, label). 'ctl' (Who controls) sits in front of these.
GAREAS = [
    ("health", "Healthcare"),
    ("cost", "Cost of living"),
    ("kids", "Kids & schools"),
    ("trump", "Trump-proofing"),
    ("gov", "Democracy"),
]

# key, short label, full title, area, exec (governor can act alone)
GI = [
    ("medicaid", "Expand Medicaid", "Expand Medicaid and raise provider rates", "health", False),
    ("drugbd", "Drug price board", "A state board to negotiate prescription drug prices", "health", False),
    ("pubopt", "Public option", "A state public health insurance option", "health", False),
    ("meddebt", "Cancel medical debt", "Cancel medical debt and keep it off credit reports", "health", False),
    ("priorauth", "Prior auth & insulin", "End prior authorization and insulin co-pays", "health", False),
    ("aca", "Backfill ACA credits", "Backfill lost ACA subsidies with state money", "health", False),

    ("datactr", "Data centers pay", "Make data centers pay their full costs", "cost", False),
    ("utility", "Utility accountability", "Utility accountability: caps on fees, limits on utility influence", "cost", False),
    ("ratefreeze", "Rate freezes & credits", "Emergency rate freezes and bill credits", "cost", True),
    ("pricecap", "Cap power prices", "Push regulators and the grid operator to cap prices", "cost", True),
    ("gastax", "Gas tax relief", "Cut gas taxes or send direct payments", "cost", False),

    ("house", "Zoning reform", "Ease zoning and building rules, including statewide preemption", "cost", False),
    ("eohousing", "Fast-track housing", "Fast-track housing by executive action", "cost", True),
    ("trust", "Housing trust funds", "Housing trust funds and bonds", "cost", False),
    ("downpay", "Down payment help", "Down payment help and a broker-fee ban", "cost", False),
    ("renter", "Renter protections", "Renter protections", "cost", False),
    ("corphome", "Limit corporate buyers", "Limit corporate homebuying", "cost", False),

    ("ptaxcorp", "Tax relief, not giveaways", "Pay for property-tax cuts by ending corporate giveaways", "cost", False),
    ("ptax", "Property tax relief", "Targeted property-tax relief", "cost", False),
    ("mctax", "Middle-class tax cuts", "Middle-class tax cuts", "cost", False),
    ("ctc", "Child & family credits", "State child and working-family tax credits", "cost", False),
    ("sstax", "No Social Security tax", "End state tax on Social Security and seniors", "cost", False),
    ("millionaire", "Millionaire's tax", "A millionaire's tax", "cost", False),

    ("prek", "Universal pre-K", "Universal pre-K", "kids", False),
    ("childcare", "Universal child care", "Universal child care", "kids", False),
    ("teacher", "Raise teacher pay", "Raise teacher pay", "kids", False),
    ("vouchers", "Schools, not vouchers", "Fund public schools fully instead of vouchers", "kids", False),
    ("pfml", "Paid family leave", "Paid family and medical leave", "kids", False),

    ("wage", "$15 minimum wage", "$15 minimum wage", "cost", False),

    ("roe", "Abortion rights in law", "Write abortion rights into state law", "trump", False),
    ("ice", "Bar ICE from schools", "Bar ICE from sensitive locations", "trump", False),
    ("guard", "Block federalized Guard", "Keep a federalized National Guard out of the state without the governor's consent", "trump", False),

    ("npv", "Popular Vote Compact", "National Popular Vote Interstate Compact", "gov", False),
    ("avr", "Auto voter registration", "Automatic voter registration", "gov", True),
    ("fraud", "Anti-fraud overhaul", "Anti-fraud overhaul (audits, inspector general)", "gov", False),
]
OLD = {"npv", "pfml", "roe", "wage", "avr", "house"}   # these six keep the 'already law' status from gov_data
NEW = [k for k, *_ in GI if k not in OLD]
# For the state-legislature power rule: Republicans start as No on these.
STATE_POWER = {"npv", "avr"}

POS = {}
def P(st, k, stance, ev):
    POS.setdefault(st, {})[k] = (stance, ev)

S, L, M, U = "Support", "Lean support", "Mixed", "Unclear"

# ---------- Governors-elect ----------
# AK Kreiss-Tomkins
P("AK", "medicaid", L, "'Let's protect Medicaid expansion' (2026 voter pamphlet statement); Alaska already expanded.")
P("AK", "utility", L, "Would 'lower electric bills by making utilities cooperate' and push co-ops to consolidate (2026).")
P("AK", "childcare", L, "Wants to 'lower the cost of childcare' by cutting regulations on providers (2026); no universal plan.")
P("AK", "house", S, "Would 'cut red tape that gets in the way of building more homes' and open state land for housing (2026).")
# CA Becerra
P("CA", "eohousing", S, "Day-one executive order declaring a housing emergency to finance about 40,000 approved affordable units (2026).")
P("CA", "ratefreeze", S, "Would 'freeze utility rates and home insurance premiums' during his housing emergency (2026).")
P("CA", "medicaid", L, "Executive order to keep coverage for people hit by federal Medi-Cal cuts; would fight to restore cuts (2026).")
P("CA", "drugbd", L, "Would expand CalRx, the state's generic-drug program (2026); not a negotiating board.")
P("CA", "childcare", L, "Pledges to 'expand help with child care' (2026); no universal plan.")
P("CA", "gastax", M, "Your list says he'd halve the gas tax; Times of San Diego reports he opposes suspending it (2026).")
P("CA", "millionaire", M, "Backs keeping the higher 2012 rates on top earners for schools; opposes Prop 40's billionaire wealth tax (2026).")
# CO Weiser
P("CO", "eohousing", S, "Day-one executive actions to streamline housing programs and target 40,000 attainable homes (Nov 2025 plan).")
P("CO", "renter", S, "Housing plan aims to cut costs for 100,000 renters and 'protect renters' (Nov 2025).")
P("CO", "datactr", L, "Backs a state law regulating data centers to protect utility rates and clean-energy standards (Aug 2026 debate).")
# GA Bottoms
P("GA", "medicaid", S, "Full Medicaid expansion is an immediate priority; would end Georgia Pathways (2026).")
P("GA", "prek", S, "Would 'guarantee pre-K for every four-year-old' (2026).")
P("GA", "teacher", S, "Would eliminate state income taxes for teachers to recruit and retain them (2026).")
P("GA", "datactr", L, "Calls for a pause on new data centers until the state sets rules (2026); not a cost-recovery plan.")
P("GA", "corphome", S, "Would crack down on corporate single-family landlords (2026).")
P("GA", "trust", S, "Proposes a statewide affordable housing trust fund (2026).")
P("GA", "gastax", S, "Would lower the state gas tax to 28 cents a gallon (2026).")
# IA Sand
P("IA", "drugbd", S, "Proposes a state board to negotiate lower prescription drug prices (2026).")
P("IA", "datactr", S, "'Data centers should pay full freight... They shouldn't be getting tax breaks' (2026).")
P("IA", "utility", S, "'Affordability for All' plan caps utility service and meter fees and adds ratemaking transparency (Sep 2026).")
P("IA", "ptaxcorp", L, "Supports taxing out-of-state property owners at a higher rate (2026).")
P("IA", "prek", S, "Proposes free preschool (2026).")
P("IA", "medicaid", L, "Backs higher Medicaid pay for disabled Iowans' care and ending Medicaid privatization (Oct 2026).")
# KS Holscher
P("KS", "medicaid", S, "Campaigned on Medicaid expansion; Kansas hasn't expanded (2026).")
P("KS", "datactr", L, "Backs a moratorium on data centers (Oct 2026).")
P("KS", "ptax", S, "Would cut residential assessment rates from 11.5% to 9% and widen the senior homestead exemption (2026).")
P("KS", "ptaxcorp", L, "Says Kansas must restrain property-tax exemptions and 'sweetheart' deals that shift the burden to homeowners (Oct 2026).")
P("KS", "vouchers", S, "Would oppose any attempt to institute private-school vouchers (2025).")
P("KS", "sstax", S, "Voted for SB 1 (2024), which ended Kansas income tax on Social Security (34–4).")
P("KS", "childcare", L, "Would 'invest in child care to lower costs' and protect child care tax credits (2025-26).")
# ME Pingree
P("ME", "pubopt", S, "Would 'create a public health insurance option: a state-backed plan' (2026).")
P("ME", "ptax", S, "Would double the homestead exemption from $25,000 to $50,000 and deepen the Property Tax Fairness Credit (2026).")
P("ME", "ptaxcorp", L, "Would let towns tax non-resident second homes at higher rates to pay for relief (2026).")
P("ME", "trust", S, "Pledges $100 million a year for affordable housing development (2026).")
P("ME", "prek", S, "Would expand universal free pre-K (Apr 2026 plan).")
P("ME", "childcare", L, "Would fund the Child Care Affordability Program to end its waitlist (2026); no universal plan.")
P("ME", "millionaire", L, "Says she'd build on Maine's new millionaire's tax (2026).")
P("ME", "priorauth", L, "Would hold insurers accountable by reducing waste and prior authorization (2026).")
# MI Benson
P("MI", "prek", S, "Would expand free pre-K to all 3- and 4-year-olds (May 2026 education plan).")
P("MI", "teacher", S, "Would require starting teacher salaries of at least $60,000 (2026).")
P("MI", "utility", S, "Would restrict utilities from using campaign contributions to influence regulators (2026).")
P("MI", "childcare", S, "Wants 'a universal full-day, five-day-per-week early childhood education system' from birth (2026).")
# MN Klobuchar
P("MN", "fraud", S, "Proposed 40-plus anti-fraud changes, including surprise audits and a statewide inspector general (May 2026).")
P("MN", "house", L, "Pledged to speed up homebuilding and permitting (May 2026).")
# NV Ford
P("NV", "datactr", S, "Would pause new data center tax abatements pending audits and make data centers pay for their own power and grid upgrades (2026).")
P("NV", "renter", S, "Would cap security deposits at one month's rent and ban junk rental fees (2026).")
P("NV", "corphome", S, "Would limit how many homes corporate investors can buy each year and create a corporate landlord registry (2026).")
P("NV", "meddebt", S, "His 26-point 'Workers First' agenda would cancel medical debt (2026).")
P("NV", "drugbd", L, "Would cap prescription drug prices (2026); no board specified.")
# NM Haaland
P("NM", "pubopt", S, "'I want to work toward a public option' (2026).")
P("NM", "ctc", S, "'I will expand the Child Tax Credit and the Earned Income Tax Credit' (Jun 2026).")
P("NM", "renter", S, "Would ban rent-fixing, including landlords' use of AI pricing (2026).")
P("NM", "corphome", S, "Would restrict how much housing private equity firms can own (Feb 2026).")
P("NM", "childcare", S, "Pledged to preserve New Mexico's universal no-cost child care (2026).")
P("NM", "medicaid", L, "Would 'protect Medicaid from Trump's cruel cuts' (2026); New Mexico already expanded.")
# OH Acton
P("OH", "drugbd", L, "'Ohio Rx' would use the Medicaid program's single PBM to negotiate lower drug prices (Apr 2026); not a board.")
P("OH", "ptax", S, "Up to $1,000 rebate when bills rise more than 4%, plus a wider senior homestead exemption (Jul 2026).")
P("OH", "vouchers", L, "Would fully implement the Fair School Funding Plan (2026); no stated plan to end EdChoice vouchers.")
P("OH", "utility", S, "Would restore efficiency programs cut in the HB 6 bribery scandal and appoint regulators 'not beholden to utility companies' (2026).")
P("OH", "datactr", S, "Would require data centers to pay extra utility and environmental costs (Apr 2026).")
# RI Foulkes
P("RI", "medicaid", S, "Would raise Medicaid reimbursement rates, now among the lowest in New England (2026).")
P("RI", "millionaire", S, "Backs a new 8.99% bracket on income over $1 million, dedicated to housing (Mar 2026).")
P("RI", "trust", S, "'Rhode Home' revolving fund to finance 20,000 homes, paid for by the millionaire's tax (Mar 2026).")
P("RI", "prek", S, "Would 'ensure every Rhode Island family has access to pre-Kindergarten' (2026).")
P("RI", "childcare", L, "Would expand child care tax credits and an employer-matched child care fund (2026).")
P("RI", "renter", L, "Would put 5% of Rhode Home funds toward rent relief (2026).")
# TX Hinojosa
P("TX", "gastax", S, "$1,500 payment to every household and would suspend the gas tax until prices stabilize (2026).")
P("TX", "vouchers", S, "Pledges to end private-school vouchers and stop state takeovers of districts (2026).")
P("TX", "teacher", S, "Pledges to raise teacher pay (2026).")
P("TX", "datactr", S, "Would end over $1 billion in data center tax exemptions and impose a permit moratorium (2026).")
P("TX", "ratefreeze", S, "Would freeze residential electricity rates until large users pay for the infrastructure they need (2026).")
P("TX", "ptaxcorp", S, "Would cut corporate subsidies to pay for property-tax cuts (2026).")
P("TX", "renter", S, "Backs cash back for renters (2026).")
# WI Crowley
P("WI", "medicaid", S, "Would fully expand BadgerCare; Wisconsin hasn't taken the ACA expansion (2026).")
P("WI", "pubopt", S, "'Badger Basics' opens BadgerCare as a public option for every household (Apr 2026).")
P("WI", "childcare", S, "Would cap out-of-pocket child care costs at 7% of income for all families (2026).")
P("WI", "datactr", S, "Data centers must 'pay the full cost of grid upgrades they drive'; would sign a repeal of their sales-tax break (2026).")
P("WI", "vouchers", L, "Would fully fund public schools (2026); no stated plan on Wisconsin's voucher programs.")
P("WI", "renter", L, "Plan 'strengthens eviction prevention' (Apr 2026).")
P("WI", "downpay", L, "Plan 'expands affordable homeownership' (Apr 2026).")
P("WI", "roe", S, "Says abortion must be 'protected at all costs' (2026).")
P("WI", "pfml", S, "Would build a child care system 'that includes paid family leave' (2026).")

# ---------- Continuing / re-elected Democrats (2026 addresses, budgets, records) ----------
# AZ Hobbs
P("AZ", "meddebt", S, "Erased $642 million in medical debt; would ban medical debt from credit reports (Jan 2026 address).")
P("AZ", "priorauth", S, "Proposed eliminating prior authorization requirements (Jan 2026).")
P("AZ", "mctax", S, "$200 million-plus Middle Class Tax Cuts package: higher standard deduction, no tax on overtime and tips (2026).")
P("AZ", "sstax", L, "Her middle-class package includes senior relief (2026); Arizona already exempts Social Security.")
P("AZ", "datactr", S, "Would end the $38 million data center tax exemption and charge them families' water rate (2026).")
P("AZ", "vouchers", L, "Would return the universal ESA voucher to its original mission for disabled and military children (2026).")
P("AZ", "trust", L, "Proposed a Housing Acceleration Fund seeded with $2.5 million (2026).")
P("AZ", "ratefreeze", L, "$20 million Affordability Fund for utility bills, paid for by a short-term-rental fee (2026).")
# CT Lamont
P("CT", "pubopt", S, "'Connecticut Option' with no co-pays or deductibles at high-value hospitals (2026).")
P("CT", "utility", S, "Would require regulators to bar utilities from billing ratepayers for lobbying, legal and charitable costs (2026).")
P("CT", "datactr", L, "Opposes new data centers unless they bring their own generation (2026).")
P("CT", "ratefreeze", L, "Proposed energy rebates of about $400 per family (2026).")
P("CT", "childcare", S, "Growing the child care endowment toward universal early childhood education (2026).")
P("CT", "ctc", S, "Would expand the state EITC to about $1,000 (2026).")
P("CT", "mctax", S, "Signed a $400 million middle-class income tax cut (cited Jan 2026).")
P("CT", "sstax", S, "Eliminated income tax for most seniors (cited Jan 2026).")
P("CT", "aca", S, "Connecticut backstopped the federal ACA subsidy cuts (2026).")
P("CT", "ice", S, "Committed to protecting schools and courthouses from civil immigration enforcement without judicial warrants (2026).")
P("CT", "house", M, "Vetoed the HB 5002 zoning bill (2025) but backs transit-oriented housing (2026).")
# DE Meyer
P("DE", "pricecap", S, "Called on the Public Service Commission to stop approving rate hikes (2026 address).")
P("DE", "utility", S, "Demanded Delmarva Power 'stop overcharging families' (2026).")
P("DE", "house", S, "Pursuing statewide permitting reform and zoning changes with nine local governments (2026).")
# HI Green
P("HI", "aca", S, "Committed $16.5 million in state funds to replace the enhanced ACA tax credits (2026).")
P("HI", "childcare", L, "Directs part of $600 million in recovered funds to child care (2026).")
P("HI", "house", S, "Has issued emergency housing proclamations to fast-track building (2023–).")
P("HI", "eohousing", S, "Emergency proclamations on housing since 2023, extended repeatedly.")
# IL Pritzker
P("IL", "house", S, "Proposed statewide zoning standards limiting local control over housing types (Feb 2026).")
P("IL", "datactr", S, "Paused new data center tax credits and says grid operators must make data centers pay their power bills in full (2026).")
P("IL", "downpay", S, "Proposed new down payment assistance funding (Feb 2026).")
P("IL", "meddebt", S, "Launched a plan to buy and erase $4 billion in medical debt (2024–).")
P("IL", "priorauth", S, "Signed the Healthcare Protection Act banning prior authorization for in-patient mental health care (2024).")
P("IL", "ctc", S, "Created Illinois's first child tax credit (2024).")
# KY Beshear
P("KY", "trust", S, "$150 million for the Affordable Housing Trust Fund (2026 budget address).")
P("KY", "aca", S, "$100 million to lower costs on kynect, the state exchange (2026).")
P("KY", "prek", S, "Proposed Pre-K for All (2026).")
P("KY", "teacher", S, "$159 million for mandatory educator raises, about 7% (2026).")
P("KY", "ratefreeze", L, "$75 million fund to help Kentuckians pay utility bills (2026).")
# MD Moore
P("MD", "datactr", S, "Wants data centers to cover their own power costs (2026 address).")
P("MD", "pricecap", S, "Joined governors asking PJM to cap energy prices for two years (2026).")
P("MD", "ratefreeze", L, "Proposed $100 million in additional energy rebates (2026).")
P("MD", "medicaid", L, "Fully funds the $14 billion Medicaid program (2026); Maryland already expanded.")
P("MD", "childcare", L, "Cited a 70% expansion of child care access (2026); no universal plan.")
P("MD", "ice", L, "Proposed legislation to protect Marylanders from unconstitutional actions by federal agents (2026); not specific to sensitive locations.")
# MA Healey
P("MA", "priorauth", S, "Would eliminate prior authorization: 'if your doctor says you need it, you'll get it' (2026 address).")
P("MA", "meddebt", S, "Would ban medical debt from credit reports (2026).")
P("MA", "aca", S, "Would cover premium increases for 270,000 people hit by federal subsidy cuts (2026).")
P("MA", "downpay", S, "Would expand $25,000 down payment assistance and ban broker fees (2026).")
P("MA", "ratefreeze", S, "Ordered 25% electric and 10% gas bill cuts for February and March (2026).")
P("MA", "utility", S, "Would make utilities justify every line on bills and buy power at the lowest price (2026).")
P("MA", "prek", S, "Proposes universal pre-K in every Gateway City (2026).")
P("MA", "house", S, "Cut environmental approvals for housing from over a year to 30 days (2026).")
P("MA", "ctc", S, "Would expand the state EITC (2026).")
P("MA", "mctax", L, "Cites the middle-class tax cut already delivered; pledges no tax increases (2026).")
# NJ Sherrill
P("NJ", "ratefreeze", S, "First executive order declared a utility-cost emergency and paused new rate increases (Jan 2026).")
P("NJ", "pricecap", L, "Directed the Board of Public Utilities to pause pending rate requests (Jan 2026).")
P("NJ", "ptax", S, "Budget targets $4.2 billion in property-tax relief at those most in need (Mar 2026).")
P("NJ", "downpay", L, "Budget 'invests in homeownership for first-time buyers' (Mar 2026).")
P("NJ", "ptaxcorp", L, "Budget closes about $700 million in corporate tax loopholes (Mar 2026); not tied to property-tax cuts.")
P("NJ", "ctc", L, "Budget maintains the state Child Tax Credit and EITC (Mar 2026).")
P("NJ", "childcare", L, "Adds money to the Child Care Assistance Program (Mar 2026).")
# NY Hochul
P("NY", "prek", S, "Universal pre-K for every 4-year-old by 2028 (Jan 2026 address).")
P("NY", "childcare", S, "Path to 'Universal Child care for every single family'; caps costs at $15 a week for eligible families (2026).")
P("NY", "datactr", S, "Would require data centers to 'pay their fair share' and generate their own power (2026).")
P("NY", "ice", S, "Would require judicial warrants for ICE to enter schools, daycares, hospitals and houses of worship (2026).")
P("NY", "house", S, "'Let Them Build': modernize environmental review for housing (2026).")
P("NY", "trust", L, "$250 million more for affordable housing (2026).")
P("NY", "ctc", S, "Raised the state child tax credit to up to $1,000 for children under four (cited 2026).")
P("NY", "mctax", S, "Would eliminate state income tax on up to $25,000 of tipped income (2026).")
P("NY", "priorauth", S, "Proposed eliminating co-pays for insulin (2026).")
# NC Stein
P("NC", "teacher", S, "Average 11% teacher raise, highest starting pay in the Southeast (Apr 2026 budget).")
P("NC", "vouchers", S, "Would phase out the universal Opportunity Scholarship voucher expansion (Apr 2026 budget).")
P("NC", "medicaid", S, "Would fully fund the Medicaid rebase, $319 million plus $728 million (2026).")
P("NC", "ctc", S, "Proposed a refundable Working Families Tax Credit and a child and dependent care credit (2026).")
P("NC", "mctax", L, "Proposed a larger standard deduction while halting rate cuts for top earners (2026).")
P("NC", "childcare", L, "Would raise child care subsidy rates and set a statewide floor (2026).")
# OR Kotek
P("OR", "datactr", S, "Signed the POWER Act letting regulators charge data centers their own rates; backs a moratorium on new ones (2026).")
P("OR", "eohousing", S, "Executive orders setting a 36,000-homes-a-year target and a homelessness emergency (2023–).")
P("OR", "utility", L, "Cites action to rein in utility rate increases (2026).")
# PA Shapiro
P("PA", "datactr", S, "GRID standards: data centers must pay for any new generation they need (Feb 2026 budget).")
P("PA", "pricecap", S, "Called for a continued cap on PJM wholesale electricity prices (Feb 2026).")
P("PA", "downpay", S, "Would expand homeownership assistance (2026).")
P("PA", "roe", S, "Wants abortion rights written into state law (2026).")
P("PA", "vouchers", M, "Previously backed vouchers, then dropped that support after opposition from his party.")
# VA Spanberger
P("VA", "datactr", L, "'Make high energy users pay their fair share' (Jan 2026 address).")
P("VA", "meddebt", L, "Would keep people from falling into medical debt after one emergency (2026).")
# WA Ferguson
P("WA", "millionaire", S, "Proposed a Millionaires' Tax on income over $1 million (Jan 2026).")
P("WA", "ctc", S, "Would expand the Working Families Tax Credit with Millionaires' Tax revenue (2026).")
P("WA", "trust", S, "$244 million for affordable housing, the largest supplemental housing investment (2026).")
P("WA", "ratefreeze", S, "One-time $200 utility bill credit for 125,000 families (2026).")
P("WA", "downpay", L, "Funding to help first-time homebuyers (2026).")
P("WA", "childcare", L, "Ballmer Group partnership of up to $1 billion for free early learning (2026).")

NF = ("Unclear", "No statement or action found.")
NR = ("Unclear", "Not researched: this batch covers Democratic governors.")

def gov_new(st, party):
    out = {}
    for k in NEW:
        if party != "D":
            out[k] = NR
        else:
            out[k] = POS.get(st, {}).get(k, NF)
    return out

# ---------- "already law" status for the new issues (only where a clear statewide tracker exists) ----------
ALL = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
NONEXP = {"AL","FL","GA","KS","MS","SC","TN","TX","WI","WY"}
TRACK = {
 "medicaid": ({s for s in ALL if s not in NONEXP}, "Yes — ACA Medicaid expansion adopted", "No — hasn't adopted the ACA expansion (KFF)"),
 "pubopt": ({"WA":"Cascade Select (2021)","CO":"Colorado Option (2023)","NV":"Battle Born State Plans (2026)"}, None, "No public option"),
 "drugbd": ({"CO":"PDAB set first upper payment limit (2025)","MD":"PDAB with upper payment limits (2026 caps)","MN":"PDAB with UPL authority","WA":"PDAB with UPL authority"}, None, "No board with price-cap authority"),
 "meddebt": ({s:"Bars or limits medical debt on credit reports" for s in ["CA","CO","CT","DE","IL","ME","MD","MN","NJ","NY","OR","RI","VT","VA","WA"]}, None, "No credit-report ban (NCLC tracker)"),
 "aca": ({"NM":"Fully replaced lost credits (2026)","CA":"$190M partial backfill (2026)","CO":"Up to $100M (2026)","CT":"$70M partial backfill","MD":"State subsidies under 400% FPL (2026)","MA":"Expanded ConnectorCare subsidies (2026)"}, None, "No state backfill"),
 "prek": ({s:"Universal pre-K for 4-year-olds" for s in ["AL","CA","CO","FL","GA","IA","ME","MI","NM","NY","OK","VT","WV","WI"]}, None, "Not universal"),
 "childcare": ({"NM":"Universal no-cost child care (2025)"}, None, "No universal child care"),
 "sstax": ({s for s in ALL if s not in {"CO","CT","MN","MT","NM","RI","UT","VT"}}, "Yes — doesn't tax Social Security", "No — still taxes some Social Security benefits"),
 "millionaire": ({"CA":"1% surtax over $1M (2005)","MA":"4% surtax (2023)","NJ":"10.75% bracket over $1M","NY":"Higher brackets over $1M","MN":"1% surtax on investment income over $1M (2024)","ME":"2% surcharge (2026)","WA":"9.9% tax over $1M (signed Mar 2026)","HI":"New $1M bracket (2027)","RI":"Surtax phasing in from 2027"}, None, "No millionaire's tax"),
 "ctc": ({s:"State child tax credit" for s in ["AZ","CA","CO","CT","GA","IL","ME","MD","MA","MN","NJ","NM","NY","OK","OR","UT","VT","RI"]}, None, "No state child tax credit"),
 "ice": ({"CA":"Schools need a judicial warrant (2025)","IL":"Bars arrests near courthouses, hospitals, colleges, day cares (Dec 2025)","CO":"Sensitive-location protections (2025)","NM":"Immigrant Safety Act (2026)","ME":"LD 2106: schools, hospitals, libraries (2026)","MD":"State rules on schools","WA":"Keep Washington Working limits (2019)"}, None, "No sensitive-locations law found"),
 "datactr": ({"TX":"SB 6 (2025)","OR":"POWER Act (2025)","MN":"HF 16 (2025)","UT":"SB 132 (2025)","MD":"SB 937 (2025)","ID":"HB 911 (2026)","AL":"SB 270 (2026)","OK":"HB 2992 (2026)","TN":"SB 2128 (2026)","FL":"SB 484 (2026)"}, None, "No law making data centers cover their costs"),
}
def status2(st):
    out = {}
    for k in NEW:
        if k not in TRACK:
            out[k] = "Not tracked: no clear statewide 'already law' list for this one"
            continue
        have, yes, no = TRACK[k]
        if isinstance(have, dict):
            out[k] = ("Yes — " + have[st]) if st in have else ("No — " + no if not no.startswith("No") else no)
        else:
            out[k] = yes if st in have else no
    return out

# ---------- Federalized National Guard (added Nov 10 2026): researched for every governor, both parties ----------
# Support = opposes a federalized or out-of-state Guard entering without the governor's consent (sued, signed a law,
# pledged to block). Oppose = welcomed or asked for Trump's Guard deployments in their own state, or defended
# deployments over another governor's objection. Sending troops to D.C. or praising deployments = Lean oppose.
O, LO, MX = "Oppose", "Lean oppose", "Mixed"
GUARD = {
 "AK": (U, "No statement found on federal Guard deployments.", None),
 "AZ": (L, "Called Trump's federalization of California's Guard 'an unprecedented overreach' that went around the governor (June 2025); signed the June 2025 Democratic governors' statement.", "https://ktar.com/arizona-news/hobbs-troops-to-los-angeles"),
 "CA": (L, "Called the Los Angeles deployment unconstitutional, 'usurping the state's authority' (2025), and says he'd back the attorney general in court against troops sent into California (2026).", "https://fox5sandiego.com/news/politics/inside-california-politics/theyre-the-aggressors-former-hhs-secretary-xavier-becerra-blasts-national-guard-deployment-as-unconstitutional/"),
 "CO": (S, "As attorney general, joined multistate court briefs against the Los Angeles and D.C. deployments, calling them a violation of law and the Constitution (2025).", "https://www.yahoo.com/news/colorado-joins-states-opposing-national-141729062.html"),
 "CT": (L, "Opposes Trump's Guard mobilizations into other states (Oct 2025); signed the June 2025 Democratic governors' statement.", "https://ctmirror.org/2025/10/08/trump-troops-national-governors-association-ned-lamont/"),
 "DE": (L, "Signed the Aug 2025 Democratic governors' statement calling Guard deployments without a governor's consent 'an alarming abuse of power.'", "https://democraticgovernors.org/updates/joint-statement-from-democratic-governors-on-president-trump-and-the-national-guard/"),
 "GA": (L, "Said nothing justifies sending the Guard into Atlanta, calling Trump's talk 'inflammatory' (Oct 2026); pledged to review Georgia's troops in D.C.", "https://www.wrdw.com/2026/10/27/trump-defends-federal-poll-watchers-georgia-floats-guard-deployment/"),
 "HI": (MX, "Signed the June 2025 statement against the Los Angeles deployment, but sent 27 Hawaii Guard members to D.C. for America 250 (July 2026).", "https://www.staradvertiser.com/2026/07/16/hawaii-news/calls-grow-for-green-to-recall-hawaii-national-guard-from-dc/"),
 "IL": (S, "Sued to block the federalized Illinois Guard and Texas troops sent to Chicago (Oct 2025) and won at the Supreme Court.", "https://www.militarytimes.com/news/pentagon-congress/2026/01/02/trump-says-hes-dropping-push-for-national-guard-in-la-other-cities/"),
 "IA": (U, "Says he'd talk with Guard leaders before deciding whether to keep Iowa troops in D.C. (Nov 2026).", "https://www.newsfromthestates.com/node/437321"),
 "KS": (U, "No statement found on federal Guard deployments.", None),
 "KY": (S, "Joined court briefs against the Oregon and Illinois deployments (Oct 2025); recalled a Kentucky Guard member diverted to Trump's D.C. task force (June 2026).", "https://www.pa.gov/governor/newsroom/2025-press-releases/icymi--gov-shapiro-takes-action-against-pres-trump-s-national-gu"),
 "ME": (U, "No statement found on federal Guard deployments.", None),
 "MD": (S, "'I will not authorize it, and it will not happen' on Guard patrols in Baltimore (Aug 2025); weighed legal options with the attorney general.", "https://foxbaltimore.com/spotlight-on-maryland/gov-wes-moore-says-he-will-not-deploy-the-national-guard-white-house-and-fop-responds"),
 "MA": (S, "Filed a bill making it unlawful for another state's Guard to enter Massachusetts without her permission (Jan 2026).", "https://www.mass.gov/news/governor-healey-takes-action-to-keep-ice-out-of-schools-hospitals-courthouses-and-places-of-worship"),
 "MI": (L, "Called the Los Angeles deployment a 'flagrant, tyrannical abuse of power' (June 2025).", "https://www.clickondetroit.com/news/local/2025/06/10/michigan-gubernatorial-candidates-spar-over-trumps-military-deployment-amid-immigration-protests"),
 "MN": (L, "On Trump's threat to send troops into Minnesota: 'This Administration is escalating rather than de-escalating and it needs to stop' (Jan 2026).", "https://www.startribune.com/insurrection-act-trump-minnesota/601564579"),
 "NV": (S, "As attorney general, called the Los Angeles federalization unlawful and joined multistate briefs; opposed Nevada Guard support for ICE (2025).", "https://ag.nv.gov/News/PR/2025/Attorney_General_Ford_Condemns_Trump_Administration_for_Unlawfully_Deploying_the_California_National_Guard"),
 "NJ": (S, "Vowed to sue if Trump sends troops into New Jersey (Oct 2025); in Congress, wrote an amendment requiring the receiving governor's consent.", "https://www.foxnews.com/politics/new-jersey-dem-hopeful-vows-sue-trump-over-troop-deployments-says-states-would-pay-price"),
 "NM": (U, "No statement found on federal Guard deployments.", None),
 "NY": (S, "Said she'd do everything in her power to keep Trump's troops out of New York (Aug 2025); signed the Democratic governors' statement.", "https://www.cbsnews.com/newyork/news/president-trump-national-guard-nyc-gov-kathy-hochul-response"),
 "NC": (L, "Signed the Aug 2025 Democratic governors' statement against deployments without consent; sent one Guard member to D.C. for America 250 (2026).", "https://democraticgovernors.org/updates/joint-statement-from-democratic-governors-on-president-trump-and-the-national-guard/"),
 "OH": (U, "No statement found on federal Guard deployments.", None),
 "OR": (S, "Sued over the federalized Oregon Guard and out-of-state troops sent to Portland; won a permanent injunction (Nov 2025).", "https://www.opb.org/article/2026/01/06/oregon-national-guard-trump/"),
 "PA": (S, "Filed court briefs against the Oregon and Illinois deployments, calling them 'incredibly dangerous' (Oct 2025).", "https://www.pa.gov/governor/newsroom/2025-press-releases/icymi--gov-shapiro-takes-action-against-pres-trump-s-national-gu"),
 "RI": (U, "No statement found on federal Guard deployments.", None),
 "TX": (L, "Criticized Abbott for sending Texas Guard troops to Chicago and Portland as 'political theater' (Oct 2025).", "https://news4sanantonio.com/news/instagram/retired-military-major-general-weighs-in-on-potential-deployment-of-texas-national-guard"),
 "VA": (L, "Signed SB 337 (Apr 2026), which orders a study of how Virginia should respond to Guard deployments the governor hasn't approved and bars using the Guard to intimidate voters.", "https://lis.blob.core.windows.net/files/1225078.HTML"),
 "WA": (S, "Signed HB 1321 (Apr 2025) barring other states' Guard from entering without his permission.", "https://governor.wa.gov/node/80270"),
 "WI": (U, "No statement found on federal Guard deployments.", None),
 "AL": (O, "Backs Trump sending the Guard into cities 'that can't control their own people' and pledged to deploy it in Birmingham and Montgomery (2025).", "https://365.military.com/daily-news/2025/10/02/tuberville-backs-sending-national-guard-urban-cities-cant-control-their-own-people.html"),
 "AR": (O, "'We're always going to invite Donald Trump and safety and security into our state' (Aug 2025); sent 100 troops to D.C.", "https://www.axios.com/local/nw-arkansas/2025/08/26/sanders-trump-national-guard-crime"),
 "FL": (LO, "Urged Guard deployments to Chicago, St. Louis and New York (Aug 2025).", "https://floridapolitics.com/archives/753766-donalds-national-guard"),
 "ID": (U, "No statement found on federal Guard deployments into states.", None),
 "IN": (LO, "Backed Trump's Guard deployment in D.C.: 'it makes sense' (Aug 2025).", "https://indianacapitalchronicle.com/2025/08/19/repub/four-gop-states-send-nearly-1000-national-guard-to-d-c-for-trump-crackdown/"),
 "LA": (O, "Requested up to 1,000 Guard troops for New Orleans and other cities (Sep 2025); sent 135 to D.C.", "https://www.npr.org/2025/10/01/nx-s1-5558457/portland-chicago-memphis-trump-national-guard"),
 "MS": (LO, "Sent 200 Mississippi Guard troops to Trump's D.C. mission (Aug 2025).", "https://www.cbsnews.com/news/west-virginia-to-deploy-hundreds-of-national-guard-troops-to-d-c"),
 "MO": (LO, "'Certainly Chicago could use some help' (Oct 2025); Missouri Guard assists ICE.", "https://ctmirror.org/2025/10/08/trump-troops-national-governors-association-ned-lamont/"),
 "MT": (LO, "Backs Trump's Guard deployment in D.C. (Aug 2025).", "https://www.mtpr.org/montana-news/2025-08-29/montana-republican-leaders-back-trumps-national-guard-deployment"),
 "NE": (LO, "Supported Trump's D.C. plan, including Guard troops from other states (Aug 2025).", "https://lailluminator.com/2025/08/18/repub/national-guard-d-c/"),
 "NH": (U, "Said she would 'evaluate any request' to send the New Hampshire Guard to cities (Aug 2025).", "https://www.nhpr.org/nh-news/2025-08-27/ayotte-says-she-would-evaluate-nh-natl-guard-deployment-to-cities-but-no-request-has-come"),
 "ND": (U, "No statement found on federal Guard deployments into states.", None),
 "OK": (U, "No statement found on federal Guard deployments.", None),
 "SC": (O, "As attorney general, co-led state briefs defending Trump's Guard deployments to D.C. and to Chicago over Illinois' objection (2025).", "https://www.scag.gov/about-the-office/news/attorney-general-alan-wilson-leads-defense-of-trump-s-deployment-of-national-guard-to-chicago/"),
 "SD": (LO, "Sent 12 Guard members to D.C. 'in solidarity with President Trump' (Aug 2025).", "https://www.sdpb.org/politics/2025-08-31/south-dakota-national-guard-mobilized-to-washington-d-c"),
 "TN": (O, "Applauded and lobbied for Trump sending the Guard into Memphis (Sep 2025).", "https://www.blackburn.senate.gov/2025/9/crime/blackburn-applauds-president-trump-s-decision-to-send-national-guard-to-memphis"),
 "UT": (LO, "Called the federalization of California's Guard constitutional and said he was 'grateful' (June 2025), while wishing presidents lacked that power.", "https://www.deseret.com/politics/2025/06/10/utah-governor-sides-with-president-trump-on-deploying-national-guard-troops-to-california"),
 "VT": (L, "Turned down Trump's requests for Vermont troops and called the Chicago and Portland deployments unconstitutional (Oct 2025).", "https://vnews.com/2025/10/12/phil-scott-slams-trump-national-guard/"),
 "WV": (LO, "Sent 300 to 400 troops to D.C., 'proud to stand with President Trump' (Aug 2025).", "https://abc6onyourside.com/news/nation-world/four-red-states-send-national-guard-troops-to-dc-to-support-trumps-crime-crackdown"),
 "WY": (U, "No statement found on federal Guard deployments.", None),
}
TRACK["guard"] = ({"WA": "HB 1321 (2025) bars other states' Guard without the governor's OK",
                   "CA": "SB 1354 (2026) bars other states' Guard without the governor's OK",
                   "TX": "Older law requires state approval for other states' troops",
                   "ID": "Older law requires state approval for other states' troops",
                   "ND": "Older law requires state approval for other states' troops",
                   "KS": "Older law requires state approval for other states' troops"},
                  None, "No law limiting outside Guard troops")
_gov_new0 = gov_new
def gov_new(st, party):
    out = _gov_new0(st, party)
    s, e, _u = GUARD.get(st, (U, "No statement found on federal Guard deployments.", None))
    out["guard"] = (s, e)
    return out
GUARD_URLS = {st: u for st, (_s, _e, u) in GUARD.items() if u}
