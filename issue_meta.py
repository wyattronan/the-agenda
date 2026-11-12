"""Issue list, issue areas and vote thresholds for the Senate tab.

need: 'leg' = 60 unless the filibuster is gone (then 51); an int = fixed; 'caucus' = majority of Dem caucus.
who: 'both' = every senator researched; 'sitting' = continuing senators only; 'new' = senators-elect only.
"""

AREAS = [
    ("rules", "Sen. rules"),
    ("health", "Healthcare"),
    ("cost", "Cost of living"),
    ("democracy", "Democracy & ethics"),
    ("immig", "Immigration"),
    ("world", "Foreign policy"),
    ("tech", "Big Tech"),
]

# key, short label, area, need, who
META = [
    ("fil", "Eliminate the filibuster", "rules", 51, "both"),
    ("sch", "Schumer as Majority Leader", "rules", "caucus", "both"),

    ("m4a", "Medicare for All", "health", "leg", "both"),
    ("aca", "Restore enhanced ACA tax credits", "health", "leg", "both"),
    ("medicaid", "Repeal OBBBA Medicaid cuts & work requirements", "health", "leg", "both"),
    ("drugneg", "Expand Medicare drug price negotiation", "health", "leg", "both"),
    ("priorauth", "Curb prior authorization & insurer denials", "health", "leg", "both"),
    ("roe", "Codify Roe (Women's Health Protection Act)", "health", "leg", "both"),

    ("gouge", "Grocery price-gouging ban & surveillance-pricing limits", "cost", "leg", "both"),
    ("meat", "Break up meatpackers & block grocery mergers", "cost", "leg", "both"),
    ("gastax", "Suspend the federal gas tax", "cost", "leg", "both"),
    ("datactr", "Data centers pay their own power costs; cap utility hikes", "cost", "leg", "both"),

    ("ctc", "Expand the Child Tax Credit", "cost", "leg", "both"),
    ("childcare", "Cap childcare at 7% of income / universal childcare", "cost", "leg", "both"),
    ("toptax", "Repeal top-bracket OBBBA cuts; close billionaire loopholes", "cost", "leg", "both"),
    ("pfl", "National paid family leave", "cost", "leg", "new"),

    ("downpay", "Down payment help for first-time buyers", "cost", "leg", "both"),

    ("wage", "Raise the minimum wage ($15–$25) & expand overtime", "cost", "leg", "both"),
    ("pro", "PRO Act", "cost", "leg", "new"),
    ("repair", "Right to repair for farm equipment", "cost", "leg", "new"),

    ("stock", "Ban congressional stock trading (HONEST Act)", "democracy", "leg", "both"),
    ("gerry", "Ban partisan gerrymandering", "democracy", "leg", "both"),
    ("dcpr", "DC / PR statehood", "democracy", "leg", "both"),
    ("pacs", "Ban corporate PACs & super PACs", "democracy", "leg", "new"),
    ("termlim", "Term or age limits amendment", "democracy", 67, "new"),
    ("heg", "Convict an impeached Sec. Hegseth", "democracy", 67, "both"),

    ("imm", "Comprehensive immigration reform", "immig", "leg", "both"),
    ("ice", "Rein in ICE: no masks, cameras, ID, warrants, right to sue", "immig", "leg", "both"),

    ("isr", "Condition military aid to Israel", "world", 51, "both"),
    ("iran", "Iran War Powers Resolution", "world", 51, "both"),
    ("tariff", "End tariff emergencies; pass the Trade Review Act", "cost", 51, "both"),

    ("ai", "AI guardrails", "tech", "leg", "both"),
]

WHY = {
    "fil": "Changing the rule by precedent (the 'nuclear option') needs a simple majority. At 50–50, VP Vance breaks the tie against it, so 51 is the real number.",
    "sch": "Decided by secret ballot inside the Democratic caucus in early December. Schumer needs a simple majority of caucus members; Republicans don't vote.",
    "isr": "Arms-sale disapproval resolutions are privileged under the Arms Export Control Act, so they can't be filibustered: 51 passes the Senate. Trump would veto, which takes 67 to override.",
    "iran": "War Powers Act joint resolutions get expedited, filibuster-proof votes, so 51 passes the Senate. Trump would veto, which takes 67 to override.",
    "tariff": "Resolutions ending a national emergency under the National Emergencies Act are privileged, so ending the tariff emergencies takes 51. The Trade Review Act itself is an ordinary bill (60 while the filibuster stands). Trump would veto either; 67 overrides.",
    "heg": "Removing an impeached official takes a two-thirds vote of senators present (67 if all 100 vote). The filibuster doesn't apply, and the president has no role.",
    "termlim": "A constitutional amendment needs two-thirds of the Senate (67) and the House, then ratification by 38 states. The president has no role.",
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
