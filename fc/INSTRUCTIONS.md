# Fact-check brief: "The Agenda" position tracker

Today is Nov 7, 2026. The site tracks where U.S. senators (the 120th Senate, seated Jan 2027, including newly elected members) and the governors serving in 2027 stand on Democratic agenda measures. Measures and what each one means: `/home/claude/fc/in/measures.json` (use the `senate` list for senators and the `governor` list for governors).

Your input file lists officials and their current recorded position on every measure (`stance` + `evidence`). Your job, for every official and every measure in that file:

1. **Verify recorded positions.** For every cell that is not `Unclear`, confirm the evidence is real, correctly attributed, correctly characterized, and not since reversed. Find a source URL for it.
2. **Hunt for hints on blank cells.** For every `Unclear` (or governor `Noted`) cell, search for anything the official has said or done on that issue through Nov 7, 2026: votes, sponsorships/cosponsorships, campaign issue pages, candidate questionnaires, debate answers, interviews, op-eds, press releases, social posts, State of the State / budget addresses, signed or vetoed bills. Hints matter: a favorable remark, conditional openness, or support for a narrower version counts.

## Stance scale
- `Support`: explicit commitment, sponsorship/cosponsorship, vote for, or signed it.
- `Lean support`: a hint, favorable remark, conditional openness, or backing a narrower version.
- `Mixed`: supports parts and opposes parts, or has said both.
- `Lean oppose`: skeptical remarks, conditional opposition, voted against a narrower version.
- `Oppose`: explicit opposition, vote against, veto.
- `Unclear`: nothing specific found. This is the correct answer when you find nothing.
- `N/A`: leave existing N/A cells alone (e.g., Republicans on the Democratic leader vote).

## Hard rules
- **Never infer from party, ideology, or what similar politicians think.** Every non-Unclear stance must rest on the official's own words or actions, with a URL.
- Ignore the site's "power rule" default (Republicans assumed No on the filibuster, DC/PR statehood, gerrymandering ban, National Popular Vote, automatic voter registration). That's a display default, not a position. Record only what they actually said or did.
- A position on a closely related but different policy is at most a Lean, and say so in the evidence.
- Evidence: one sentence, max ~200 characters, in your own words (no quotes longer than ~10 words), with month and year.

## How to work efficiently
- Start each official broad: campaign site issues page, Ballotpedia (campaign themes + survey), OnTheIssues, Vote Smart, state voter guides (newsfromthestates.com syndicates many), congress.gov cosponsor lists. One good page often covers many measures.
- Then go measure by measure for what's left. For Republicans, prioritize measures with real bipartisan traction (stock trading ban, term limits, prior authorization, data centers paying their own costs, right to repair, gas tax, Iran war powers, tariffs, AI guardrails, meatpacking, price gouging, child tax credit, paid leave, housing). For Democrats, every Unclear cell matters.
- Use WebFetch on candidate pages with a prompt that lists the measures you need, rather than reading whole pages.

## Output (required)
Write JSON to `/home/claude/fc/out/<your input file name>` (same file name as your input). It must be a list of objects:

```json
{"who": "Full Name", "state": "XX", "key": "measure_key",
 "old_stance": "...", "new_stance": "...",
 "evidence": "One sentence, own words, with month/year.",
 "url": "https://...", "confirmed": true, "changed": false}
```

- Include an entry for **every cell you changed** (`changed: true`) and **every non-Unclear cell you checked** (`confirmed: true` if accurate as recorded, else give the corrected stance and evidence with `changed: true`).
- Omit Unclear cells where you still found nothing.
- Write the file incrementally (after each official) so work isn't lost.

Finish with a 3-line summary: officials covered, cells changed, cells confirmed.
