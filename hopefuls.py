"""2028 Democratic presidential hopefuls for the Getting Stuff Done tab.
kind: 'gov' / 'sen' reuse that official's existing score (ref = state or senator id);
'selfgov' / 'selfsen' are researched here (cells: key -> [stance, evidence, url, flag]),
where flag = 'done' (accomplished in office, governor-style) or 'spons' (sponsor/cosponsor, senator-style)."""
W = "https://en.wikipedia.org/wiki/"
KH_CAMP = W + "Kamala_Harris_2024_presidential_campaign"
KH_POS = W + "Political_positions_of_Kamala_Harris"
PB = W + "Political_positions_of_Pete_Buttigieg"
AOC_POS = W + "Political_positions_of_Alexandria_Ocasio-Cortez"
CG = "https://www.congress.gov/bill/119th-congress/house-bill/{}/cosponsors"

HOPE = [
 {"n": "Raphael Warnock", "p": "D", "role": "U.S. Senator, Georgia", "kind": "sen", "ref": "Warnock"},
 {"n": "JB Pritzker", "p": "D", "role": "Governor of Illinois", "kind": "gov", "ref": "IL"},
 {"n": "Jon Ossoff", "p": "D", "role": "U.S. Senator, Georgia", "kind": "sen", "ref": "Ossoff"},
 {"n": "Gretchen Whitmer", "p": "D", "role": "Governor of Michigan, term ends Jan 2027", "kind": "gov", "ref": "MI", "statescore": True},
 {"n": "Pete Buttigieg", "p": "D", "role": "Former Transportation Secretary and South Bend mayor", "kind": "selfgov", "st": "MI",
  "office": "mayor or Secretary", "cells": {
   "pubopt": ["Support", "Ran on a 'Medicare for All Who Want It' public option (2019).", PB, ""],
   "prek": ["Support", "2019 education plan put $700B toward full-day pre-K.", PB, ""],
   "childcare": ["Support", "Same 2019 plan funds child care from infancy to age five.", PB, ""],
   "teacher": ["Support", "2019 education plan called for paying teachers more.", PB, ""],
   "pfml": ["Support", "2019 platform included national paid family leave.", PB, ""],
   "wage": ["Support", "Day after the midterms, urged a rapid-fire Democratic bill raising the minimum wage (Nov 2026); his 2019 platform called for $15.", "https://www.cnn.com/2026/11/05/politics/democrats-midterms-mandate-what-happens-2026-2028", ""],
   "medicaid": ["Support", "Day after the midterms, urged Democrats to pass a bill expanding Medicaid among their first 15 (Nov 2026).", "https://www.cnn.com/2026/11/05/politics/democrats-midterms-mandate-what-happens-2026-2028", ""],
   "ctc": ["Support", "Day after the midterms, urged a rapid-fire bill expanding the Child Tax Credit (Nov 2026).", "https://www.cnn.com/2026/11/05/politics/democrats-midterms-mandate-what-happens-2026-2028", ""],
   "roe": ["Lean support", "Backs abortion rights and repealing the Hyde Amendment (2019); no specific statute named.", PB, ""],
   "npv": ["Lean support", "Favors abolishing the Electoral College (2019); no position on the compact itself.", PB, ""],
   "millionaire": ["Lean support", "Would end Trump's tax cuts for the super wealthy to pay for his college plan (2019); federal, not a state tax.", PB, ""],
 }},
 {"n": "Kamala Harris", "p": "D", "role": "Former Vice President", "kind": "selfgov", "st": "CA", "office": "Vice President", "cells": {
   "drugbd": ["Support", "As VP, cast the tie-breaking vote for the Inflation Reduction Act (Aug 2022), which created Medicare drug price negotiation.", W + "Inflation_Reduction_Act", "done"],
   "aca": ["Support", "Biden-Harris American Rescue Plan enhanced ACA premium credits (Mar 2021), extended by the IRA (Aug 2022).", W + "American_Rescue_Plan_Act_of_2021", "done"],
   "ctc": ["Support", "The American Rescue Plan expanded the Child Tax Credit (2021); her 2024 platform proposed a $6,000 first-year credit and restoring the expansion.", KH_CAMP, "done"],
   "meddebt": ["Support", "Biden-Harris CFPB finalized a rule taking medical bills off credit reports (Jan 2025); her 2024 platform proposed eliminating medical debt.", "https://www.consumerfinance.gov/about-us/newsroom/cfpb-finalizes-rule-to-remove-medical-bills-from-credit-reports/", "done"],
   "downpay": ["Support", "2024 platform: $25,000 in down payment help for every first-time buyer.", KH_CAMP, ""],
   "corphome": ["Support", "2024 platform: strip tax breaks from Wall Street firms buying up single-family homes.", KH_CAMP, ""],
   "renter": ["Support", "2024 platform: bar landlords from using rent-setting algorithms.", KH_CAMP, ""],
   "pfml": ["Support", "Unveiled a six-month paid family and medical leave plan (2019); backed paid leave in 2024.", KH_POS, ""],
   "roe": ["Support", "Said Congress must put the protections of Roe into law (2024).", KH_CAMP, ""],
   "ice": ["Support", "Co-introduced the Protecting Sensitive Locations Act in the Senate (2019).", KH_POS, ""],
   "pubopt": ["Support", "Cosponsored the State Public Option Act (2019).", KH_POS, ""],
   "mctax": ["Support", "Proposed a tax cut for most working- and middle-class Americans (2018).", KH_POS, ""],
   "priorauth": ["Lean support", "2024 platform: extend the $35 insulin cap and $2,000 drug-cost cap; no prior-authorization position.", KH_CAMP, ""],
   "house": ["Lean support", "2024 platform: $40B in incentives for starter-home builders and YIMBY ideas; no zoning preemption plan.", KH_CAMP, ""],
   "wage": ["Lean support", "Backs raising the federal minimum wage without naming a figure (2024).", KH_CAMP, ""],
   "millionaire": ["Lean support", "Proposed a Billionaire Minimum Income Tax (2024), a federal rather than state tax.", KH_CAMP, ""],
   "guard": ["Lean support", "Signed a 2018 letter questioning Trump's 5,800-troop border deployment; related, not a consent law.", KH_POS, ""],
 }},
 {"n": "Andy Beshear", "p": "D", "role": "Governor of Kentucky", "kind": "gov", "ref": "KY"},
 {"n": "Wes Moore", "p": "D", "role": "Governor of Maryland", "kind": "gov", "ref": "MD"},
 {"n": "Mark Kelly", "p": "D", "role": "U.S. Senator, Arizona", "kind": "sen", "ref": "Kelly"},
 {"n": "Cory Booker", "p": "D", "role": "U.S. Senator, New Jersey", "kind": "sen", "ref": "Booker"},
 {"n": "Gavin Newsom", "p": "D", "role": "Governor of California, term ends Jan 2027", "kind": "gov", "ref": "CA", "statescore": True},
 {"n": "Josh Shapiro", "p": "D", "role": "Governor of Pennsylvania", "kind": "gov", "ref": "PA"},
 {"n": "Rahm Emanuel", "p": "D", "role": "Former Chicago mayor and ambassador to Japan", "kind": "selfgov", "st": "IL", "office": "mayor", "cells": {
   "prek": ["Support", "As mayor, launched free full-day pre-K for every Chicago 4-year-old, phased in from 2018.", "https://movingforward.chicago.gov/education", "done"],
   "wage": ["Lean support", "As mayor, passed a $13 Chicago minimum wage (Dec 2014), short of $15.", "https://chicago.gov/city/en/depts/mayor/press_room/press_releases/2014/dec/mayor-emanuel--city-council-approve-ordinance-to-increase-minimu.html", ""],
   "pfml": ["Lean support", "Passed a paid sick leave ordinance, up to five days a year (Jun 2016); narrower than paid family leave.", "https://movingforward.chicago.gov/working-families", ""],
   "ice": ["Lean support", "Backed Chicago's Welcoming City Ordinance limiting police help to ICE (2012); not a sensitive-locations rule.", W + "Rahm_Emanuel", ""],
   "roe": ["Lean support", "Had a 100% pro-choice voting record in Congress; no state-law action.", W + "Rahm_Emanuel", ""],
 }},
 {"n": "Alexandria Ocasio-Cortez", "p": "D", "role": "U.S. Representative, New York", "kind": "selfsen", "st": "NY", "cells": {
   "m4a": ["Support", "Cosponsor, Medicare for All Act H.R.3069 (Apr 2025).", CG.format(3069), "spons"],
   "roe": ["Support", "Cosponsor, Women's Health Protection Act H.R.12 (Jun 2025).", CG.format(12), "spons"],
   "pro": ["Support", "Cosponsor, PRO Act H.R.20 (Mar 2025).", CG.format(20), "spons"],
   "wage": ["Support", "Cosponsor, Raise the Wage Act H.R.2743 (Apr 2025).", CG.format(2743), "spons"],
   "dcpr": ["Support", "Cosponsor, Washington, D.C. Admission Act H.R.51 (Jan 2025).", CG.format(51), "spons"],
   "ctc": ["Support", "Cosponsor, American Family Act H.R.2763 (Apr 2025).", CG.format(2763), "spons"],
   "pfl": ["Support", "Cosponsor, FAMILY Act H.R.5390 (Sep 2025).", CG.format(5390), "spons"],
   "isr": ["Support", "Cosponsored the Block the Bombs Act to halt offensive weapons to Israel (2025).", AOC_POS, "spons"],
   "stock": ["Lean support", "Original cosponsor of the Restore Trust in Congress Act (2025); covers members, not the President or VP.", AOC_POS, "spons"],
   "fil": ["Support", "Reaffirmed she wants the filibuster gone, answering Kyrsten Sinema (Mar 2025).", "https://www.washingtonexaminer.com/?p=3349349", ""],
   "iran": ["Support", "Urged a yes vote on the Iran War Powers Resolution on the House floor (Apr 2026).", "https://ocasio-cortez.house.gov/media/press-releases/ocasio-cortez-denounces-trumps-unconstitutional-war-iran-house-floor", ""],
   "ice": ["Support", "Platform calls for abolishing ICE, going beyond these limits.", AOC_POS, ""],
   "toptax": ["Lean support", "Backs a 70% top rate on income over $10 million; no position on the specific OBBBA repeal.", AOC_POS, ""],
   "tariff": ["Lean support", "Called Trump's tariff policy disastrous (2025).", AOC_POS, ""],
   "datactr": ["Lean support", "Opposed new AI data centers over their environmental harm and backed an inquiry (2026); related policy.", AOC_POS, ""],
   "medicaid": ["Lean support", "Fought the OBBBA Medicaid cuts on the House floor (Jul 2025).", "https://ocasio-cortez.house.gov/taxonomy/term/137?page=5", ""],
 }},
]

# Nov 15 2026: positions on the measures added when the lists were re-based on the 2026 campaign census.
# Only new cells are added; nothing above is overwritten. [stance, evidence, url, flag]
R3 = {
 'Alexandria Ocasio-Cortez': {
   'equality': ["Support", "Voted for the Equality Act, H.R.5 (Feb 25 2021, 224–206).", "https://clerk.house.gov/evs/2021/roll039", ""],
   'gun': ["Support", "Voted for the Bipartisan Background Checks Act, H.R.8 (Mar 11 2021, 227–203).", "https://clerk.house.gov/evs/2021/roll075", ""],
   'vra': ["Support", "Voted for the John R. Lewis Voting Rights Advancement Act, H.R.4 (Aug 24 2021, 219–212).", "https://clerk.house.gov/evs/2021/roll260", ""],
   'clean': ["Lean support", "Voted against the OBBBA, H.R.1, which cut clean-energy credits (Jul 3 2025, 218–214).", "https://clerk.house.gov/evs/2025/roll190", ""],
   'snap': ["Lean support", "Voted against the OBBBA, H.R.1, which cut SNAP and shifted costs to states (Jul 3 2025, 218–214).", "https://clerk.house.gov/evs/2025/roll190", ""],
   'homes': ["Support", "Co-introduced the Homes Act with Sen. Tina Smith to build up to 1.3 million affordable homes via a public developer (Sep 2024).", "https://ocasio-cortez.house.gov/media/press-releases/us-senator-tina-smith-and-congresswoman-ocasio-cortez-introduce-homes-act", "spons"],
   'pubopt': ["Lean support", "Cosponsor, Medicare for All Act H.R.3069 (Apr 2025); single payer is broader than a public option.", "https://www.govinfo.gov/app/details/BILLS-119hr3069ih", "spons"],
   'ssm': ["Support", "Cosponsored Social Security 2100 to expand benefits and apply payroll tax above $400k; wants the wealthy to pay in (Oct 2021).", "https://truthout.org/articles/ocasio-cortez-backs-social-security-expansion-says-the-wealthy-need-to-chip-in", "spons"],
 },
 'Kamala Harris': {
   'homes': ["Support", "2024 campaign plan: 3 million new homes in four years and up to $25,000 down-payment help for first-time buyers (Aug 2024).", "https://nlihc.org/resource/harris-campaign-releases-plans-lower-housing-costs", ""],
   'corphome': ["Support", "2024 plan urged Congress to pass the Stop Predatory Investing Act, stripping tax breaks from big single-family-home buyers (Aug 2024).", "https://nlihc.org/resource/harris-campaign-releases-plans-lower-housing-costs", ""],
   'clean': ["Support", "As VP cast the tie-breaking vote passing the IRA's clean-energy credits (Aug 7 2022, 51–50); 2024 plan pledged to keep them.", "https://www.budget.senate.gov/ranking-member/newsroom/votearama/roll-call-vote-on-passage-of-hr5376-fy2022-budget-reconciliation-as-amended", "done"],
   'ssm': ["Lean support", "2024 plan: protect Social Security and Medicare, keep them solvent by making the wealthy pay more; no cap-lift named (Sep 2024).", "https://kamalaharris.com/a-new-way-forward", ""],
   'mctax': ["Lean support", "2024 plan: restore $3,600 Child Tax Credit, expand EITC, cut taxes for 100 million Americans; family credits, narrower (Sep 2024).", "https://kamalaharris.com/a-new-way-forward", ""],
   'workforce': ["Support", "2024 plan: expand Registered Apprenticeships, pre-apprenticeships and career-technical education; drop degree rules for federal jobs (Sep 2024).", "https://kamalaharris.com/a-new-way-forward", ""],
   'ai': ["Lean support", "2024 plan: continue the 2023 AI executive order to protect workers and consumers; federal, not kids-online rules (Sep 2024).", "https://kamalaharris.com/a-new-way-forward", ""],
   'gun': ["Support", "2024 campaign promise: require universal background checks for gun sales and ban assault weapons (Sep 2024).", "https://api.politifact.com/article/2024/sep/30/kamala-harris-2024-campaign-promises-here-are-her/", ""],
   'vra': ["Support", "2024 campaign promise: sign the John Lewis Voting Rights Act and the Freedom to Vote Act (Sep 2024).", "https://api.politifact.com/article/2024/sep/30/kamala-harris-2024-campaign-promises-here-are-her/", ""],
   'equality': ["Support", "2024 campaign promise: pass the Equality Act to protect LGBTQ+ Americans from discrimination (Sep 2024).", "https://api.politifact.com/article/2024/sep/30/kamala-harris-2024-campaign-promises-here-are-her/", ""],
   'ivf': ["Support", "VP statement condemned Senate GOP for blocking the IVF bill; reproductive freedom 'must include access to IVF' (Sep 17 2024).", "https://presidency.ucsb.edu/node/374244", ""],
   'pubopt': ["Lean support", "2019 Medicare for All plan let under-65s buy into Medicare in year one; her 2024 plan dropped it (Jul 2019).", "https://www.npr.org/2019/07/29/746051105/kamala-harris-releases-medicare-for-all-plan-with-a-role-for-private-insurers", ""],
   'tariff': ["Support", "2024 plan criticized Trump's proposed tariffs while backing targeted action on unfair Chinese trade (Sep 2024).", "https://kamalaharris.com/a-new-way-forward", ""],
 },
}
for _h in HOPE:
    for _k, _v in R3.get(_h['n'], {}).items():
        if 'cells' in _h: _h['cells'].setdefault(_k, _v)

# Nov 15 2026, second pass.
R3B = {
 "Pete Buttigieg": {
  "clean": [
   "Lean support",
   "2019 climate plan: double clean electricity by 2025, zero-emission power by 2035, solar subsidies; no stance on restoring the OBBBA-cut credits.",
   "https://en.wikipedia.org/wiki/Political_positions_of_Pete_Buttigieg",
   ""
  ],
  "snap": [
   "Lean support",
   "Said the OBBBA would 'cut food' for veterans and children as it passed the House (Jul 2025); no restoration bill named.",
   "https://www.advocate.com/politics/pete-buttigieg-one-big-beautiful-bill",
   ""
  ],
  "ssm": [
   "Support",
   "Proposed raising the Social Security payroll-tax cap from $132,900 to $250,000 for solvency (2019 campaign).",
   "https://www.fa-mag.com/news/buttigieg-unveils-social-security-proposal-50667.html",
   ""
  ],
  "vra": [
   "Lean support",
   "2019 Douglass Plan proposed a federal 'New Voting Rights Act' to widen access (Jul 2019); did not name the John Lewis Act.",
   "https://en.wikipedia.org/wiki/Political_positions_of_Pete_Buttigieg",
   ""
  ],
  "equality": [
   "Support",
   "Platform backs passing the federal Equality Act to give LGBTQ Americans nondiscrimination protections (2019-20 campaign).",
   "https://en.wikipedia.org/wiki/Political_positions_of_Pete_Buttigieg",
   ""
  ],
  "ivf": [
   "Lean support",
   "Called Trump's broken IVF promise 'cruel'; pro-family means ensuring access and cost of care (Aug 2025); no bill named.",
   "https://gayexpress.co.nz/2025/08/pete-buttigieg-slams-trump-for-breaking-ivf-promise-its-cruel-not-pro-family/",
   ""
  ],
  "gun": [
   "Support",
   "2020 campaign backed universal background checks, an assault weapons ban, red-flag laws and national gun licensing.",
   "https://en.wikipedia.org/wiki/Political_positions_of_Pete_Buttigieg",
   ""
  ],
  "rural": [
   "Lean support",
   "Said the OBBBA would 'shut down rural hospitals' (Jul 2025); no rural hospital bill named.",
   "https://www.advocate.com/politics/pete-buttigieg-one-big-beautiful-bill",
   ""
  ],
  "mental": [
   "Support",
   "Released a $300 billion plan to expand mental health care and fight addiction (Aug 2019).",
   "https://en.wikipedia.org/wiki/Political_positions_of_Pete_Buttigieg",
   ""
  ],
  "schools": [
   "Support",
   "2019 education plan would triple federal Title I funding for schools.",
   "https://en.wikipedia.org/wiki/Political_positions_of_Pete_Buttigieg",
   ""
  ],
  "college": [
   "Support",
   "2019 plan: free public college for the bottom 80% of students, sliding-scale tuition above; opposes free college for all.",
   "https://en.wikipedia.org/wiki/Political_positions_of_Pete_Buttigieg",
   ""
  ],
  "tariff": [
   "Support",
   "Publicly criticized Trump's tariffs as feeding his concentration of arbitrary power, with Jon Stewart (Apr 2025).",
   "https://petebuttigieg.substack.com/p/talking-trumps-tariffs-billionaire",
   ""
  ]
 },
 "Rahm Emanuel": {
  "schools": [
   "Lean support",
   "As mayor, ended Chicago's shortest-in-nation school day, a change that sparked the 2012 teachers strike; not a funding change.",
   "https://chicago.suntimes.com/news/what-is-mayor-rahm-emanuel-legacy-public-schools-police-shooting-property-tax-pension/",
   "done"
  ],
  "college": [
   "Support",
   "As mayor, launched the Star Scholarship: free tuition and books at City Colleges for qualifying CPS graduates (mayor 2011-19; year not on page).",
   "https://movingforward.chicago.gov/education",
   "done"
  ],
  "workforce": [
   "Support",
   "As mayor, launched College to Careers, aligning City Colleges with in-demand industries for job training (2011).",
   "https://movingforward.chicago.gov/education",
   "done"
  ],
  "safety": [
   "Support",
   "As mayor, pledged to hire 1,000 new police officers in two years (2016); net gain of about 600 by May 2018.",
   "https://chicago.suntimes.com/news/what-is-mayor-rahm-emanuel-legacy-public-schools-police-shooting-property-tax-pension/",
   "done"
  ],
  "ai": [
   "Support",
   "Urged a U.S. ban on social media for kids under 16, like Australia's (Dec 2025).",
   "https://www.wptv.com/science-and-tech/social-media/prominent-democrat-calls-for-us-to-restrict-social-media-for-kids-16-and-younger",
   ""
  ],
  "tariff": [
   "Support",
   "Called Trump's tariffs 'the largest tax increase in memory' and a blunder (Apr 2025); backs high tariffs on China.",
   "https://rahmemanuel.substack.com/p/trumps-folly-is-piling-up-and-america",
   ""
  ],
  "equality": [
   "Lean support",
   "Backed same-sex marriage with a 100% HRC score in Congress; as mayor added transgender protections; no Equality Act statement.",
   "https://www.wikiwand.com/en/articles/Rahm_Emanuel",
   ""
  ],
  "gun": [
   "Lean support",
   "Backed banning many rifles under 'sporting purposes' rules (1998); NRA rated him F (Dec 2003); no background-check vote found.",
   "https://www.wikiwand.com/en/articles/Rahm_Emanuel",
   ""
  ]
 },
 "Kamala Harris": {
  "schools": [
   "Lean support",
   "2024 plan touted 'the largest investment in public education' (federal aid) but proposed no new K-12 funding (Sep 2024).",
   "https://kamalaharris.com/a-new-way-forward",
   ""
  ],
  "college": [
   "Lean support",
   "2024 plan cited a $900 Pell Grant increase and vowed to make college more affordable; no free or capped tuition (Sep 2024).",
   "https://kamalaharris.com/a-new-way-forward",
   ""
  ],
  "rural": [
   "Support",
   "2024 plan: 'helping increase funding for rural hospitals' and $130M for rural health infrastructure (Sep 2024).",
   "https://kamalaharris.com/a-new-way-forward",
   ""
  ],
  "mental": [
   "Support",
   "VP statement backed the final mental health parity rule barring stricter limits on mental health care (Sep 2024).",
   "https://www.presidency.ucsb.edu/documents/fact-sheet-biden-harris-administration-lowers-mental-health-care-costs-improving-access",
   ""
  ],
  "safety": [
   "Support",
   "As VP announced $285M for school mental health counselors plus $6M for community violence intervention (Jan 2024).",
   "https://www.presidency.ucsb.edu/documents/press-release-vice-president-harris-announces-285-million-increase-mental-health",
   ""
  ]
 },
 "Alexandria Ocasio-Cortez": {
  "ivf": [
   "Support",
   "Original cosponsor, Right to IVF Act of 2026 H.R.9941 (Jul 2026).",
   "https://www.govinfo.gov/app/details/BILLS-119hr9941ih",
   "spons"
  ]
 }
}
for _h in HOPE:
    for _k, _v in R3B.get(_h['n'], {}).items():
        if 'cells' in _h: _h['cells'].setdefault(_k, _v)
