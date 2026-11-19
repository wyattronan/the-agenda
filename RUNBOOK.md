# Runbook for the scheduled updates

Both scheduled runs follow the standing rules:

- Never infer support. No statement or vote means Undecided/Unclear.
- Republicans default to No on fil/dcpr/gerry and state npv/avr.
- Kansas governor is D. Arizona and Alaska are Democratic trifectas. Texas is split.
- Alaska stays a Democratic trifecta unless a source shows definitively that it isn't (for example, a Republican-led coalition organizes either chamber in January). Its bipartisan coalitions alone aren't a reason to flag it.
- Every change needs a source URL.

## Daily light scrape (no approval needed)

Scope:

- New bills signed or vetoed.
- New public statements by people already tracked.
- Poll additions (`fc/polls`).
- Office changes (resignations, appointments, swearing-ins, race calls), including the office labels (see "Office labels, daily").
- GOP postmortem statements by the people in `gop/gop_tracker.json` (see "GOP postmortem, daily" below).
- The 2028 hopefuls, including those who hold no office (see "2028 hopefuls, daily").
- U.S. Senate roll-call votes and cosponsor changes on tracked bills (see "Senate votes and cosponsors, daily").
- Federal bills becoming law (see "Bills becoming law, daily").

Steps:

1. Run `git pull`.
2. Search the news from the last 48 hours for each tracked issue and person, including the GOP postmortem people.
3. Write only sourced changes, with the date and URL, into these files: `fc/manual.json`, `fc/polls`, `gop/gop_tracker.json`, the `cells` of non-office hopefuls in `hopefuls.py`, the status labels in `senate_data.py` and `gov_data.py`, and the `ENACTED` lists in `template.html` and `camp.py`.
4. Run `./build.sh`. If `checks.py` fails, stop and change nothing.
5. Safety cap: if a run would change more than 15 positions, don't push to `main`. Open a pull request instead, as in the weekly flow.
6. Commit as "Daily update YYYY-MM-DD: N changes", with one line per change. Push to `main`, and Netlify deploys.
   Include `fc/stance_log.json` in the commit. The build stamps each stance change with the build date (Chicago time), and the site tags those cells "New stance" for 7 days. Never edit the log by hand.
7. Send a short notification listing the changes.

### GOP postmortem, daily
Search the last 48 hours for what each person in `gop/gop_tracker.json` said about the midterm loss, Trump, or the tracked issues (`issues` keys).
- A statement that pulls back from a recorded shift: add it to their `walkbacks` list, as in "Postmortem walkbacks" below. The site scores it. Each walkback counts as one change toward the 15-change cap.
- A statement that adds to or restates a position: update that `issues` field (one or two sentences, with the date), and add the outlet and date to `sources`. Not a stance change; list it under "Note text only".
- A statement that would move a `map` pre/post score or a `posture` (a new break with Trump, a Silent person speaking up): don't apply it. Flag it in the commit message for the weekly run, with the source.
- Set `as_of` and the end of `window` to the latest statement date recorded.

### 2028 hopefuls, daily
Search the last 48 hours for each person in `HOPE` in `hopefuls.py`.
- Hopefuls who hold office (`kind` sen or gov) use their Senate or governor cells: write changes to `fc/manual.json` as usual.
- Hopefuls without an office (`selfgov` / `selfsen`: Buttigieg, Harris, Emanuel, Ocasio-Cortez) keep their cells in `hopefuls.py`. Replace the cell's `[stance, evidence, url, flag]` in place (in the person's `cells`, or in the later `R3`-style block that holds that key), with the date in the evidence. Each changed cell counts toward the 15-change cap.

### Office labels, daily
When a race is called, someone resigns, is appointed or sworn in, update the status label in `senate_data.py` (Senate roster rows) or `gov_data.py` (governor rows), e.g. "Presumed winner (uncalled)" → "Senator-elect (... AP call Nov 17, 2026)". An appointee replaces the "TBD" row with the person's name and party; their cells start Unclear. Labels aren't positions and don't count toward the cap. List them under "Office change" in the commit message.

### Senate votes and cosponsors, daily
- Check senate.gov roll-call votes (and the Senate Daily Press vote summaries) from the last 48 hours. A vote on a tracked measure, or on a bill that maps to one, changes each senator's cell under the usual rules (related bill caps at a Lean; procedural votes are noted, not mapped, unless the site has mapped that kind before). Every senator's changed cell counts toward the cap, so a big vote usually means a pull request.
- Check congress.gov cosponsor lists for the tracked Senate bills cited in cell evidence (and new companion bills) for cosponsors added in the last 48 hours. A new cosponsor is Support on that bill's measure (or a Lean if it's a narrower or related bill).

### Bills becoming law, daily
When a tracked federal measure is signed into law (or a veto is overridden), add it to `ENACTED` in `template.html` (`{k:{d:'Mon D, YYYY', how:'Became law on ...'}}`) and to `ENACTED["sen"]` in `camp.py`, so it leaves the "likely to pass" lists and Top 10 rankings. Cite the signing in the commit message. This isn't a position change.

## Weighing statements (all scrapes)

Score each statement on three factors and multiply them:

| Factor | Weights |
|---|---|
| Initiative | 1.0 they started it (post, speech, op-ed, release, floor remarks) · 0.7 answering a question |
| Specificity | 1.0 engages the policy or the claim itself · 0.5 a generic formula ("no daylight", "I support the president", "everything's on the table") |
| Audience cost | 1.0 says something this audience won't like · 0.75 mixed or national audience · 0.5 tells this audience what it wants to hear |

Actions (votes, signatures, vetoes, executive orders, hires) outrank words. Outlet size and ideology are not factors by themselves: what someone tells their base can reveal more than what they tell a national audience, and the reverse. What matters is whether the statement cost them anything with the people in front of them.

### Hedging
Add a `hedge` note (one sentence, sourced, dated) to a `fc/manual.json` entry when:
- the person has been on both sides (earlier pledge, later "not viable"; wary, then open to a conditional version);
- they move a commitment past the election, or make it conditional on something unlikely;
- they say different things to different audiences.

The cell keeps its stance (the most-recent-action rule still sets it); the site adds a "Hedging" tag and shows the note. Put the source for the other side of the record in `hedge_url`. Skip it when the stance is already Mixed. Weekly runs: work through the cells whose notes say "softened to a Lean because an earlier action points the other way" and give each a specific hedge note.

### Postmortem walkbacks
A walkback is a later statement that pulls back from a post-election shift in `gop/gop_tracker.json`. Record it in the person's `walkbacks` list; don't edit `map` pre/post:

```json
{"date": "2026-11-16", "issue": "iran_war", "axes": ["trump_alignment"],
 "initiative": "prompted", "specificity": "generic", "audience": "pleasing",
 "said": "One-sentence summary with a short quote.", "source": "Outlet, date", "url": "https://..."}
```

`initiative`: self | prompted. `specificity`: specific | generic. `audience`: against | mixed | pleasing. The site computes the weight (product of the factors above) and takes back 50% × weight of whatever shift is left, per walkback: three full-weight walkbacks take back 50%, 75%, 87.5%. Add `"retract": true` only for an explicit retraction ("I was wrong") or an action that reverses the shift; that resets it fully. A walkback that restates the original claim isn't one: note it in `issues` instead. Topline numbers about scores use `{d:Name}` tokens, which the site fills in, so they stay current.

## Weekly thorough scrape (needs approval)

Scope:

- Re-verify every Senate and governor cell older than 30 days.
- Run the full GOP sweep.
- Re-check the ladder records (rung evidence) and the champion tiers.
- Refresh the steward inputs.
- Check the NC, GA and TX state senators (see "State senators, weekly").

Steps:

1. Create the branch `weekly/YYYY-MM-DD` from `main`.
2. Do the research and rebuild with `./build.sh`.
3. Push the branch and open a pull request. Its description lists:
   - every changed cell (old → new, with the source);
   - rank moves in GSD and the Top 10;
   - anything flagged as a mismatch.
4. Netlify builds a Deploy Preview link for the pull request. That preview is the exact site that will go live.
5. Approve by merging the pull request on GitHub. Netlify then deploys to production.
6. Reject by closing the pull request. Nothing goes live.
7. To change a single item, comment on the pull request. The next run reads those comments first.
8. The run's summary is emailed to Wyatt with three links: preview the site, review and approve (merge), and deny (close).
9. A reminder task runs Tuesdays at 11:43 a.m. Central. It emails only if a weekly/ or daily/ pull request is still open.
10. If a weekly pull request is still open the next Sunday, the new run folds its changes in and closes the old one, so only one ever waits.

### State senators, weekly
For each member in `state_senate.py` (NC, GA, TX, including the alternates for uncalled seats), look for new state senate roll calls on bills that map to the 35 statehouse issues and for members' own statements (campaign pages, questionnaires, releases, interviews). Only individual roll calls and own words count. Never infer from party. Record changes in `fc/ss_check.json` (one row per cell: `st`, `district`, `name`, `alt` for an alternate, `key`, `new`, `evidence`, `url`, `date`, optional `hedge`); later rows override earlier ones. List every changed cell in the pull request.

## Tab pages
Every tab has its own address: /senate/, /governors/, /top-10/, /getting-stuff-done/, /2028/, /gop-postmortem/, /glossary/. `pages.py` writes them from index.html (each with its own title and link-preview text, taken from the home-page buttons). It runs in `./build.sh` and again in the Netlify build, so only `site/index.html` and `site/404.html` are committed; `site/*/` is ignored. Old `#senate/sch`-style links still work and turn into `/senate/#sch`. The artifact copy (published from the root index.html) stays on #hashes.
