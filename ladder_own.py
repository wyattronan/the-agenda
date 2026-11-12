"""Newsom's and Whitmer's own records. The site's California and Michigan governor rows now hold their
successors (Becerra, Benson), so these two hopefuls need their own sourced entries. Partial: only what's verified."""
OWN = {
  "Gavin Newsom": {
    "meddebt": ["Support", "Signed SB 1061 keeping medical debt off consumer credit reports (Sep 2024).", "https://www.gov.ca.gov/2024/09/24/governor-newsom-signs-consumer-protection-bills-targeting-medical-debt-overdraft-fees-and-unfair-subscription-practices"],
    "house": ["Support", "Signed SB 79 allowing denser housing near transit (Oct 2025), on top of the 2025 CEQA streamlining laws.", "https://www.gov.ca.gov/2025/10/10/governor-newsom-builds-on-this-years-historic-housing-reforms-signs-legislation-to-accelerate-housing-and-affordability/"],
    "ctc": ["Support", "Signed the 2019-20 budget creating a $1,000 credit for working families with children under six (Jun 2019).", "https://www.gov.ca.gov/2019/06/27/governor-newsom-signs-2019-20-state-budget/"],
    "prek": ["Support", "Signed the 2021-22 budget adopting universal transitional kindergarten for all 4-year-olds (Jun 2021).", "https://www.cde.ca.gov/FG/fr/eb/yr21ltr0811.asp"],
    "pfml": ["Support", "Signed the 2019-20 budget expanding California's Paid Family Leave by two weeks (Jun 2019).", "https://ccfc.ca.gov/pdf/about/news_events/pr/pr_2019-06-28_First_5_Joint_Statement.pdf"],
    "ice": ["Support", "Signed AB 49 barring immigration agents from nonpublic areas of schools without a judicial warrant (Sep 2025).", "https://www.gov.ca.gov/2025/09/20/governor-newsom-signs-laws-to-protect-school-children-and-hospital-patients-and-limit-fear-tactics-used-by-trumps-secret-police-force-to-terrorize-communities/"],
    "guard": ["Support", "Signed SB 1354 requiring his permission before other states' Guard troops enter California (Sep 2026).", "https://www.gov.ca.gov/2026/09/19/governor-newsom-signs-bill-to-protect-californias-sovereignty-and-guard-against-unauthorized-military-deployments/"],
    "roe": ["Support", "His campaign gave $2.1 million to Prop 1, the 2022 abortion-rights amendment, and he headlined rallies for it.", "https://www.kqed.org/news/11931183/californians-vote-to-protect-abortion-in-constitution"],
  },
  "Gretchen Whitmer": {
    "roe": ["Support", "Signed the repeal of Michigan's 1931 abortion ban (Apr 2023) and the Reproductive Health Act (Nov-Dec 2023).", "https://www.michigan.gov/whitmer/news/press-releases/2023/12/11/governor-whitmer-signs-final-piece-of-reproductive-health-act"],
    "prek": ["Support", "Signed the FY25 education budget funding free pre-K for every 4-year-old (Jul 2024).", "https://www.michigan.gov/whitmer/news/press-releases/2024/07/23/gov-whitmer-signs-historic-fy25-education-budget"],
  },
}

# Steward for legislators who aren't senators in the site data: recorded votes defending laws on the books.
DEF_OWN = {
  "Alexandria Ocasio-Cortez": [
    ("medicaid", True, "Voted no on final House passage of the One Big Beautiful Bill Act, which cut Medicaid; every House Democrat voted no (Jul 3 2025, 218-214).", "https://www.axios.com/2025/07/03/trump-big-beautiful-bill-congress-house"),
  ],
}
