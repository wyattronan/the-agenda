# The Agenda

A single-page site tracking where governors, senators, and 2028 hopefuls stand on the agenda.

## How it's built

- `data.json`, `fc/`, `gop/`, `champ/` hold the data.
- `template.html` is the page.
- `./build.sh` runs `export.py`, which bakes the data into the page. It then runs `checks.py` and copies the result to `site/`.
- Netlify serves `site/` as is (see `netlify.toml`). There is no build step on Netlify.

## Updating by hand

```
./build.sh
git add -A && git commit -m "Update" && git push
```

Netlify deploys within about a minute of the push.

## Automatic updates

See `RUNBOOK.md`:

- **Daily light scrape:** commits straight to `main`.
- **Weekly thorough scrape:** opens a pull request for approval.
