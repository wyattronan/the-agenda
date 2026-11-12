# Polling brief: state-by-state public support for "The Agenda" measures

Today is Nov 7, 2026. The site tracks 66 Democratic agenda measures (32 federal "sen:" measures, 34 state "gov:" policies; full list with keys in /home/claude/fc/polls/measures.txt). For each measure we want **state-level public polling on support for it**, to show on a 50-state map. Each state's number is the average of up to 3 polls covering that state.

## What counts
- A poll can match the **specific bill/proposal** or the **broad concept** (e.g., "raise the minimum wage to $15" for both sen:wage and gov:wage; "abortion should be legal in all/most cases" for sen:roe and gov:roe). Tag every measure key a poll fits; set `match` to "bill" or "concept".
- **Direct state polls**: a poll fielded in one state (e.g., a Marquette poll of Wisconsin voters). type = "state".
- **Multi-state polls**: one survey reporting separate results for several states from real state samples (e.g., a 7-swing-state poll). type = "multistate".
- **Modeled estimates** (MRP or similar, projecting a national survey to all states: YouGov MRP, Cooperative Election Study tables, Data for Progress MRP, PRRI American Values Atlas state estimates, UMD Program for Public Consultation state/district estimates). type = "modeled". These are allowed and will be labeled "modeled" on the site.
- A **national-only** poll is useful too: record it with `national` filled and `states` empty. It shows as context, not on the map.
- NOT polls: ballot measure election results, advocacy "petition" counts, opt-in website surveys, push polls.

## Hard rules
- **Never invent or estimate a number.** Every figure must come from a page or PDF you actually opened (WebFetch), with its URL. If a page won't load, don't use numbers from a search snippet unless the snippet itself shows the exact figure and the source.
- **Support must point in the measure's direction.** `sup` = % favoring what the measure does. If the poll asks the reverse (e.g., % supporting school vouchers for gov:vouchers, which opposes vouchers), store the % opposing vouchers as `sup` and the % supporting as `opp`, and say so in `note`.
- Use the share of all respondents as reported (don't re-percentage excluding "unsure"). Record `opp` when reported.
- Prefer recent polls (2023–2026). Older back to 2019 is OK if nothing newer exists; never older than 2019.
- Reputability tier: 1 = nonpartisan media/academic/major pollsters (AP-NORC, Pew, KFF, Gallup, Marist, Quinnipiac, Siena, Emerson, Marquette, Monmouth, SurveyUSA, university state polls, YouGov for media, state newspaper polls); 2 = nonpartisan research or modeled estimates (CES, PRRI, UMD PPC, YouGov MRP); 3 = partisan/advocacy pollsters (Data for Progress, Navigator, party/campaign/advocacy-sponsored polls). Use tier 3 only when tier 1–2 don't exist for that state/measure, and note the sponsor.
- Keep `question` to a short paraphrase in your own words (no long quotes).

## Output
Write a JSON list to /home/claude/fc/polls/out/<your batch name>.json, rewriting it (reload + append) after each measure so nothing is lost:

```json
{"keys": ["sen:wage","gov:wage"], "match": "concept",
 "pollster": "Marquette Law School", "sponsor": "", "tier": 1,
 "type": "state", "fielded": "2026-02", "n": 1003,
 "question": "Raise Wisconsin's minimum wage to $15 an hour",
 "url": "https://...",
 "states": {"WI": {"sup": 64, "opp": 31}},
 "national": null,
 "note": ""}
```
For modeled or multistate polls, `states` holds every state reported. For national-only, `states` is {} and `national` is {"sup":..,"opp":..}.

## Efficiency
- Each agent has a WebSearch budget (given in your prompt); prefer WebFetch. A separate "cross-cutting" agent is covering the big multi-state/modeled sources (UMD PPC, PRRI Atlas, Pew Religious Landscape, CES, YouGov MRP, Data for Progress MRP) for ALL measures — topic agents should focus on direct state polls and multistate polls, and only grab a modeled source if they stumble on it.
- Good hunting grounds for state polls: university polls (Marquette WI, Siena NY, Quinnipiac, Emerson, UNH, Suffolk, Monmouth NJ, Roanoke/VCU VA, Elon/High Point NC, UT/Texas Politics Project TX, PPIC CA, Berkeley IGS CA, Michigan EPIC-MRA/Glengariff, F&M PA, Muhlenberg, Iowa Selzer/DMR, KFF state polls, AARP state polls, Ohio Northern, Mason-Dixon, Saint Anselm NH, Winthrop SC, Georgia AJC/UGA, Arizona Noble/OH Predictive, Colorado polls, Minnesota Star Tribune), plus local news write-ups that link the toplines.
- Write scratch scripts in /tmp/<your batch name>, not in fc/.
- Finish with a short summary: polls found per measure, states covered per measure, anything doubtful.
