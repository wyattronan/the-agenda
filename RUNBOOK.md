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
7. Send a short notification listing the changes.

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
