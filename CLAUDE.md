# The Agenda: working rules

Read RUNBOOK.md, fc/INSTRUCTIONS.md and fc/polls/BRIEF.md before changing data.

## Standing rules
- Never infer support. Anyone without their own statement or vote is Undecided/Unclear.
- Republicans default to No on fil/dcpr/gerry and on state npv/avr.
- Fixed calls: the Kansas governor is D. Arizona and Alaska are Democratic trifectas. Texas is split.
- Every changed position needs a source URL and a date in its note.
- Verify factual claims. Flag mismatches in the commit message or the pull request instead of silently changing them.

## Building
- Build with `./build.sh`. Never push if `checks.py` fails.
- Edit data in `fc/manual.json`, `fc/polls/`, `gop/` and `champ/`. Never hand-edit `site/index.html`.
