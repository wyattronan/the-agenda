# Runbook for the scheduled updates

Both scheduled runs follow the standing rules:

- Never infer support. No statement or vote means Undecided/Unclear.
- Republicans default to No on fil/dcpr/gerry and state npv/avr.
- Kansas governor is D. Arizona and Alaska are Democratic trifectas. Texas is split.
- Every change needs a source URL.

## Daily light scrape (no approval needed)

Scope:

- New bills signed or vetoed.
- New public statements by people already tracked.
- Poll additions (`fc/polls`).
- Office changes (resignations, appointments, swearing-ins).

Steps:

1. Run `git pull`.
2. Search the news from the last 48 hours for each tracked issue and person.
3. Write only sourced changes into `fc/manual.json` and `fc/polls`, with the date and URL.
4. Run `./build.sh`. If `checks.py` fails, stop and change nothing.
5. Safety cap: if a run would change more than 15 positions, don't push to `main`. Open a pull request instead, as in the weekly flow.
6. Commit as "Daily update YYYY-MM-DD: N changes", with one line per change. Push to `main`, and Netlify deploys.
   Include `fc/stance_log.json` in the commit. The build stamps each stance change with the build date (Chicago time), and the site tags those cells "New stance" for 7 days. Never edit the log by hand.
7. Send a short notification listing the changes.

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

The cell keeps its stance (the most-recent-action rule still sets it); the site adds a "Hedging" tag and shows the note. Skip it when the stance is already Mixed. Weekly runs: work through the cells whose notes say "softened to a Lean because an earlier action points the other way" and give each a specific hedge note.

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

## Tab pages
Every tab has its own address: /senate/, /governors/, /top-10/, /getting-stuff-done/, /2028/, /gop-postmortem/, /glossary/. `pages.py` writes them from index.html (each with its own title and link-preview text, taken from the home-page buttons). It runs in `./build.sh` and again in the Netlify build, so only `site/index.html` and `site/404.html` are committed; `site/*/` is ignored. Old `#senate/sch`-style links still work and turn into `/senate/#sch`. The artifact copy (published from the root index.html) stays on #hashes.
