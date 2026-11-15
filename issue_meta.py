"""Issue list, issue areas and vote thresholds for the Senate tab.

need: 'leg' = 60 unless the filibuster is gone (then 51); an int = fixed; 'caucus' = majority of Dem caucus.
who: 'both' = every senator researched; 'sitting' = continuing senators only; 'new' = senators-elect only.
"""

AREAS = [
    ("rules", "Sen. rules"),
    ("health", "Healthcare"),
    ("cost", "Cost of living"),
    ("democracy", "Democracy & ethics"),
    ("rights", "Rights & safety"),
    ("immig", "Immigration"),
    ("world", "Foreign policy"),
    ("tech", "Big Tech"),
]

# key, short label, area, need, who
# The list is the 30 measures the most 2026 Democratic winners campaigned on (fc/census/winners_2026.json, Nov 15 2026),
# plus HOT ("hot button") measures kept on purpose even though they fall outside that top 30.
META = [
    ("fil", "Eliminate the filibuster", "rules", 51, "both"),
    ("sch", "Schumer as Majority Leader", "rules", "caucus", "both"),

    ("m4a", "Medicare for All", "health", "leg", "both"),
    ("aca", "Restore enhanced ACA tax credits", "health", "leg", "both"),
    ("medicaid", "Repeal OBBBA Medicaid cuts & work requirements", "health", "leg", "both"),
    ("drugneg", "Lower drug prices: Medicare negotiation, insulin caps, PBMs", "health", "leg", "both"),
    ("priorauth", "Curb prior authorization & insurer denials", "health", "leg", "both"),
    ("pubopt", "Public option / Medicare buy-in", "health", "leg", "both"),
    ("ssm", "Protect & expand Social Security and Medicare", "health", "leg", "both"),
    ("rural", "Protect rural hospitals", "health", "leg", "both"),
    ("mental", "Expand mental health care", "health", "leg", "both"),
    ("roe", "Codify Roe (Women's Health Protection Act)", "health", "leg", "both"),
    ("ivf", "Right to IVF Act", "health", "leg", "both"),

    ("datactr", "Data centers pay their own power costs; cap utility hikes", "cost", "leg", "both"),
    ("clean", "Lower energy bills: restore clean-energy credits", "cost", "leg", "both"),
    ("ctc", "Expand the Child Tax Credit", "cost", "leg", "both"),
    ("mctax", "Middle-class income tax cut", "cost", "leg", "both"),
    ("childcare", "Lower child care costs (7% cap / universal child care)", "cost", "leg", "both"),
    ("snap", "Reverse the OBBBA SNAP cuts", "cost", "leg", "both"),
    ("toptax", "Repeal top-bracket OBBBA cuts; close billionaire loopholes", "cost", "leg", "both"),
    ("pfl", "National paid family leave", "cost", "leg", "new"),
    ("wage", "Raise the minimum wage ($15–$25) & expand overtime", "cost", "leg", "both"),
    ("pro", "PRO Act & union rights", "cost", "leg", "both"),

    ("stock", "Ban congressional stock trading (HONEST Act)", "democracy", "leg", "both"),
    ("vra", "John Lewis Voting Rights Advancement Act", "democracy", "leg", "both"),
    ("gerry", "Ban partisan gerrymandering", "democracy", "leg", "both"),
    ("dcpr", "DC / PR statehood", "democracy", "leg", "both"),
    ("pacs", "Get big money out: corporate PACs, super PACs, Citizens United", "democracy", "leg", "both"),

    ("equality", "Equality Act", "rights", "leg", "both"),
    ("gun", "Universal background checks", "rights", "leg", "both"),

    ("imm", "Comprehensive immigration reform", "immig", "leg", "both"),
    ("ice", "Rein in or abolish ICE", "immig", "leg", "both"),

    ("isr", "Condition military aid to Israel", "world", 51, "both"),
    ("iran", "Iran War Powers Resolution", "world", 51, "both"),
    ("tariff", "End tariff emergencies; pass the Trade Review Act", "cost", 51, "both"),

    ("ai", "AI guardrails", "tech", "leg", "both"),
]

# Hot buttons: on the site even though fewer 2026 Democratic winners campaigned on them than on the top 30.
HOT = {"fil", "sch", "dcpr", "m4a", "pfl", "gerry"}
# Measures dropped Nov 15 2026 when the list was re-based on the campaign census (their old research stays in fc/out).
DROPPED = {"gastax", "meat", "repair", "termlim", "gouge", "downpay", "heg", "road"}

WHY = {
    "fil": "Changing the rule by precedent (the 'nuclear option') needs a simple majority. At 50–50, VP Vance breaks the tie against it, so 51 is the real number.",
    "sch": "Decided by secret ballot inside the Democratic caucus in early December. Schumer needs a simple majority of caucus members; Republicans don't vote.",
    "isr": "Arms-sale disapproval resolutions are privileged under the Arms Export Control Act, so they can't be filibustered: 51 passes the Senate. Trump would veto, which takes 67 to override.",
    "iran": "War Powers Act joint resolutions get expedited, filibuster-proof votes, so 51 passes the Senate. Trump would veto, which takes 67 to override.",
    "tariff": "Resolutions ending a national emergency under the National Emergencies Act are privileged, so ending the tariff emergencies takes 51. The Trade Review Act itself is an ordinary bill (60 while the filibuster stands). Trump would veto either; 67 overrides.",
}
NOT_RESEARCHED = {
    "sitting": ("Unclear", "Not researched: this issue was scoped to sitting senators."),
    "new": ("Unclear", "Not researched: this issue was scoped to senators-elect."),
}

# Compact labels for menus/chips (META's label is the full title shown under "Selected measure").
SHORT = {
 "fil":"End the filibuster","sch":"Schumer as leader","m4a":"Medicare for All","aca":"Restore ACA credits",
 "medicaid":"Undo Medicaid cuts","drugneg":"Drug price negotiation","priorauth":"Curb prior auth","roe":"Codify Roe",
 "gouge":"Price-gouging ban","meat":"Break up meatpackers","gastax":"Gas tax holiday","datactr":"Data centers pay",
 "ctc":"Expand the CTC","childcare":"7% child care cap","toptax":"Repeal top-rate cuts","keeppay":"Keep Your Pay Act",
 "pfl":"Paid family leave","downpay":"Down payment help","rental":"Rental assistance",
 "wage":"Raise the minimum wage","pro":"PRO Act","repair":"Farm right-to-repair","stock":"Stock trading ban",
 "gerry":"Ban gerrymandering","dcpr":"DC / PR statehood","pacs":"Ban corporate PACs","termlim":"Term/age limits","heg":"Convict Hegseth",
 "imm":"Immigration reform","ice":"Rein in ICE","border24":"2024 border deal","isr":"Condition Israel aid",
 "iran":"Iran war powers","tariff":"End tariff emergencies","ai":"AI guardrails","clean":"Restore clean-energy credits",
}
FULL = {
 "fil":"Eliminate the legislative filibuster","sch":"Re-elect Chuck Schumer as Democratic leader",
 "m4a":"Medicare for All Act","aca":"Restore the enhanced ACA premium tax credits",
 "medicaid":"Repeal the OBBBA Medicaid cuts and work requirements",
 "drugneg":"Expand Medicare drug price negotiation (SMART Prices Act)",
 "priorauth":"Curb prior authorization (Improving Seniors' Timely Access to Care Act)",
 "roe":"Codify Roe: the Women's Health Protection Act",
 "gouge":"Ban grocery price-gouging and limit surveillance pricing",
 "meat":"Break up meatpackers (Family Grocery and Farmer Relief Act) and block grocery mergers",
 "gastax":"Suspend the federal gas tax","datactr":"Make data centers pay their own power costs and cap utility hikes",
 "ctc":"Expand the Child Tax Credit","childcare":"Cap child care at 7% of income / universal child care",
 "toptax":"Repeal the OBBBA top-bracket cuts and close billionaire loopholes",
 "keeppay":"Keep Your Pay Act (no federal income tax on the first $75,000, joint)",
 "pfl":"National paid family and medical leave",
 "downpay":"Down payment assistance for first-time buyers","rental":"Expand rental assistance and Section 8 vouchers",
 "wage":"Raise the minimum wage ($15–$25) and expand overtime","pro":"PRO Act (Protecting the Right to Organize)",
 "repair":"Federal right-to-repair for farm equipment",
 "stock":"Ban congressional stock trading: the Peters–Hawley–Merkley–Ossoff bill, covering the President and VP",
 "gerry":"Ban partisan gerrymandering","dcpr":"DC and Puerto Rico statehood","pacs":"Ban corporate PACs and super PACs",
 "termlim":"Constitutional amendment for congressional term or age limits","heg":"Convict Defense Secretary Pete Hegseth if the House impeaches him","imm":"Comprehensive immigration reform",
 "ice":"Rein in ICE: no masks, body cameras, visible ID, judicial warrants, right to sue",
 "border24":"Pass the 2024 bipartisan border deal","isr":"Condition military aid to Israel",
 "iran":"Iran War Powers Resolution","tariff":"End the tariff emergencies and pass the Trade Review Act",
 "ai":"AI guardrails","clean":"Restore the IRA clean-energy credits (Lowering Electric Bills Act)",
}
# Measures that could add to Democratic power: every Republican starts as No, per the user's rule.
POWER = {"fil", "dcpr", "gerry"}

# Nov 15 2026: labels for the measures added or widened when the list was re-based on the campaign census.
SHORT.update({
 "clean":"Lower energy bills","pubopt":"Public option","ssm":"Social Security & Medicare","rural":"Rural hospitals",
 "mental":"Mental health care","ivf":"Right to IVF","mctax":"Middle-class tax cut","snap":"Reverse SNAP cuts",
 "vra":"Voting Rights Act","equality":"Equality Act","gun":"Background checks",
 "drugneg":"Lower drug prices","childcare":"Lower child care costs","pacs":"Get big money out","ice":"Rein in or abolish ICE",
 "pro":"PRO Act & unions","toptax":"Tax billionaires",
})
FULL.update({
 "clean":"Lower energy bills: restore the clean-energy tax credits the OBBBA cut (Lowering Electric Bills Act)",
 "pubopt":"Create a public health insurance option or Medicare buy-in",
 "ssm":"Protect and expand Social Security and Medicare: no benefit cuts, and the wealthy pay in (lift the payroll-tax cap)",
 "rural":"Protect rural hospitals: more funding, and undo the hit from the Medicaid cuts",
 "mental":"Expand mental health care: parity enforcement, crisis lines and school counselors",
 "ivf":"Right to IVF Act",
 "mctax":"A middle-class income tax cut (Keep Your Pay Act / Working Americans' Tax Cut Act)",
 "snap":"Reverse the OBBBA's SNAP (food assistance) cuts",
 "vra":"Pass the John Lewis Voting Rights Advancement Act",
 "equality":"Pass the Equality Act (LGBTQ civil rights)",
 "gun":"Universal background checks (Background Check Expansion Act)",
 "drugneg":"Lower drug prices: expand Medicare negotiation, cap insulin costs, rein in PBMs",
 "childcare":"Lower child care costs: cap at 7% of income, universal child care, or bigger subsidies",
 "pacs":"Get big money out: ban corporate PACs and super PACs, overturn Citizens United",
 "ice":"Rein in or abolish ICE: no masks, body cameras, visible ID, judicial warrants, right to sue",
 "pro":"PRO Act and union rights",
 "toptax":"Repeal the OBBBA top-bracket cuts and close billionaire loopholes",
})
