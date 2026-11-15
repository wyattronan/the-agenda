# The Agenda: working rules

Read RUNBOOK.md, fc/INSTRUCTIONS.md and fc/polls/BRIEF.md before changing data.

## Standing rules
- Never infer support. Anyone without their own statement or vote is Undecided/Unclear.
- Republicans default to No on fil/dcpr/gerry and on state npv/avr.
- Fixed calls: the Kansas governor is D. Arizona and Alaska are Democratic trifectas. Texas is split.
- Every changed position needs a source URL and a date in its note.
- A position's default vote follows its stance: Support or Lean support defaults to Yes; Oppose or Lean oppose defaults to No. When a stance changes, the default changes with it. `defVote` in template.html does this, and visitors' saved votes reset when a cell's default moves, so don't override the default by hand.
- New stances are tagged "New stance" on their Senate and state-senate cards for 7 days. `newstance.py` dates each change in `fc/stance_log.json` at build time; commit that file with every data change.
- Verify factual claims. Flag mismatches in the commit message or the pull request instead of silently changing them.
- When a Senate measure becomes law, add it to ENACTED in template.html and camp.py so it leaves the 'likely to pass' lists and Top 10 rankings.
- Three Things to Know and Top 10 text that cite numbers should be computed from the data, not typed in. If you must hand-write a number, re-check it on every run.

## Building
- Build with `./build.sh`. Never push if `checks.py` fails.
- Edit data in `fc/manual.json`, `fc/polls/`, `gop/` and `champ/`. Never hand-edit `site/index.html`.
