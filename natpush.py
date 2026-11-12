"""National pushes: sourced 2026-campaign or post-election advocacy for agenda items beyond a leader's own office.

Used two ways:
  * Governors get credit for backing a measure that is ALREADY LAW at home only if it appears here
    (they campaigned for it elsewhere or pushed it federally in 2026 or after the election).
  * Presidential hopefuls get credit for backing Senate measures (governors) here, on top of their own record.
Keys can be Senate keys or governor keys. Stance is "Support" or "Lean support". Never inferred: each row needs a source.
"""
CNI_P = "https://capitolnewsillinois.com/news/on-1st-day-since-winning-3rd-term-as-governor-pritzker-releases-200-point-national-agenda/"
NBC_P = "https://www.nbcchicago.com/news/politics/illinois-gov-jb-pritzker-day-one-road-map-congress/4012865/"
CNN_B = "https://www.cnn.com/2026/11/05/politics/democrats-midterms-mandate-what-happens-2026-2028"
POL_B = "https://www.yahoo.com/news/politics/articles/buttigieg-midterm-blitz-helping-him-152552741.html"
W = "https://en.wikipedia.org/wiki/"

PUSH = {
 "gov:IL": {
   "medicaid": ["Support", "Day One Agenda for the new Congress calls for repealing the H.R. 1 provisions that cut federal Medicaid support (Nov 2026).", CNI_P],
   "wage": ["Support", "Day One Agenda calls on Congress to raise the minimum wage (Nov 2026).", CNI_P],
   "roe": ["Support", "Day One Agenda calls on Congress to codify abortion rights nationally (Nov 2026).", CNI_P],
   "imm": ["Support", "Day One Agenda calls for comprehensive immigration reform and an end to mass-deportation round-ups (Nov 2026).", NBC_P],
   "tariff": ["Lean support", "Day One Agenda would refund consumers for tariff costs (Nov 2026); doesn't name the Trade Review Act.", CNI_P],
 },
 "hope:Pete Buttigieg": {
   "gerry": ["Support", "Day after the midterms, urged a rapid-fire Democratic bill limiting gerrymandering (Nov 2026).", CNN_B],
   "pacs": ["Lean support", "Day after the midterms, urged reforms limiting money in politics (Nov 2026); no specific PAC ban named.", CNN_B],
   "tariff": ["Lean support", "Said a Democratic Congress should move quickly on tariffs (Oct 2026); no specific bill named.", POL_B],
 },
 "hope:Kamala Harris": {
   "imm": ["Support", "2024 campaign: pair strong border security with an earned pathway to citizenship; promised to push comprehensive immigration reform.", W + "Political_positions_of_Kamala_Harris"],
   "gouge": ["Support", "2024 campaign: anti-price-gouging rules for groceries and food.", W + "Kamala_Harris_2024_presidential_campaign"],
 },
}
