"""External state rankings for the 'Getting Stuff Done' governor score.
Each area: rank among the 50 states, 1 = best."""

MERIC = dict(OK=83.8, MS=86.6, AL=86.9, WV=87.9, KS=88.8, MO=88.8, IA=89.1, AR=89.1, TN=90.0, IN=90.6, NE=90.9,
             GA=91.0, ND=91.0, NM=91.1, TX=91.1, LA=91.8, SD=91.9, OH=92.3, MI=92.5, SC=92.6, KY=93.0, WY=93.3,
             MN=93.8, IL=95.2, NC=96.6, PA=97.0, WI=97.8, ID=98.0, VA=99.4, UT=100.2, DE=101.6, FL=101.6, NV=102.3,
             CO=102.6, AZ=107.8, NH=109.6, MT=109.6, OR=110.8, RI=112.3, WA=113.3, ME=114.0, CT=114.1, VT=114.2,
             NJ=116.4, MD=119.9, AK=127.1, NY=127.2, CA=137.9, MA=148.6, HI=186.0)

CWF = "MA HI NH RI DC NY MD VT WA CO CT OR PA VA MN NJ UT IA ID CA ME ND MI NE DE WI IL MT NC OH NM SD KS AZ IN SC KY AK FL WY LA AL MO TN GA NV WV AR OK TX MS".split()

KIDS = dict(NH=1, MA=2, UT=3, VT=4, MN=5, NJ=6, CT=7, WI=8, NE=9, IA=10, VA=11, WY=12, ID=13, CO=14, KS=14, ND=14,
            WA=17, PA=18, MD=19, IL=20, ME=21, SD=22, OR=23, MT=24, HI=25, RI=26, OH=27, MO=28, IN=29, NY=30, DE=31,
            NC=32, CA=33, MI=34, FL=35, KY=36, TN=37, SC=38, GA=39, AZ=40, WV=41, AL=42, AR=43, OK=44, TX=44, NV=46,
            AK=47, LA=48, NM=49, MS=50)

COVI = dict(WA=1, OR=2, HI=3, NV=4, VT=5, UT=6, CA=7, CO=8, IL=9, MN=10, MA=11, MI=12, NY=12, ME=14, VA=15, ND=16,
            MD=17, NJ=18, NM=19, RI=20, AK=21, CT=22, WV=23, IA=24, DE=25, PA=26, ID=27, NE=28, AZ=29, NC=30, MT=31,
            FL=32, LA=33, IN=34, GA=35, OK=36, KY=37, KS=38, SD=39, WY=40, MO=41, TN=42, SC=43, AL=44, OH=45, WI=46,
            NH=47, TX=48, AR=49, MS=50)


def _rank_by(vals):
    """Competition ranking, lower value = better (ties share a rank)."""
    out = {}
    for s, v in vals.items():
        out[s] = 1 + sum(1 for w in vals.values() if w < v)
    return out


def build():
    health = {s: i + 1 for i, s in enumerate([x for x in CWF if x != "DC"])}
    cost = _rank_by(MERIC)
    ranks = {s: {"health": health[s], "cost": cost[s], "kids": KIDS[s], "gov": COVI[s]} for s in health}
    assert len(ranks) == 50 and all(len(v) == 4 for v in ranks.values())
    src = {
        "health": {"name": "Commonwealth Fund, 2025 Scorecard on State Health System Performance",
                   "u": "https://www.commonwealthfund.org/publications/scorecard/2025/jun/2025-scorecard-state-health-system-performance",
                   "note": "Overall rank; DC removed and states re-ranked 1–50."},
        "cost": {"name": "MERIC Cost of Living Data Series, Q3 2026",
                 "u": "https://meric.mo.gov/data/cost-living-data-series",
                 "note": "Ranked from lowest to highest composite price index. This measures price levels, not policy."},
        "kids": {"name": "Annie E. Casey Foundation, 2026 KIDS COUNT Data Book",
                 "u": "https://www.aecf.org/databook",
                 "note": "Overall child well-being rank (economics, education, health, family and community)."},
        "gov": {"name": "Cost of Voting Index, 2024 (as reported by the Institute for Responsive Government)",
                "u": "https://responsivegov.org/wp-content/uploads/2026/02/ResponsiveGov_StateReportCards_2026_P3.pdf",
                "note": "1 = easiest state in which to vote."},
    }
    return {"ranks": ranks, "src": src}
