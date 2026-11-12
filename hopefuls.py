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
