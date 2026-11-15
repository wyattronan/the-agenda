#!/usr/bin/env python3
"""Give every tab its own page.

Reads the built index.html and writes site/index.html plus one copy per tab
(site/senate/index.html, site/top-10/index.html, ...). Each copy has its own
<title>, description and link-preview tags, and a <meta name="agenda-paths">
tag that tells the page to use real addresses (/senate/) instead of #hashes.
The descriptions are lifted from the home-page buttons, so any numbers in them
come from the same data as the site.

Runs in build.sh and again in the Netlify build (netlify.toml), so the per-tab
copies don't need to be committed.
"""
import html, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "index.html")
OUT = os.path.join(ROOT, "site")

# tab id -> (folder, page name); keep in step with PAGE / PAGE_T in template.html
PAGES = {
    "senate":    ("senate", "U.S. Senate Whip"),
    "governors": ("governors", "Governors & State Houses"),
    "top10":     ("top-10", "The Agenda Top 10"),
    "gsd":       ("getting-stuff-done", "Getting Stuff Done"),
    "proj":      ("2028", "2028 Projections"),
    "gop":       ("gop-postmortem", "GOP Midterm Postmortem"),
    "gloss":     ("glossary", "Glossary"),
}
HOME_DESC = "Your one-stop civic engagement tool: the Democratic agenda, who backs it, and what it would take to pass."


def button_blurbs(page):
    """Home-page button text per tab, without the title and the arrow."""
    out = {}
    for m in re.finditer(r'<a class="homebtn" href="#(\w+)">(.*?)</a>', page, re.S):
        body = re.sub(r"<svg.*?</svg>", "", m.group(2), flags=re.S)
        body = re.sub(r"<(b|strong|h\d)[^>]*>.*?</\1>", "", body, count=1, flags=re.S)  # the title line
        text = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", body)).split()).rstrip("→ ").strip()
        out[m.group(1)] = text
    return out


def head_tags(title, desc, path):
    e = lambda s: html.escape(s, quote=True)
    return (f'<meta name="agenda-paths" content="1">\n'
            f'<meta name="description" content="{e(desc)}">\n'
            f'<meta property="og:type" content="website">\n'
            f'<meta property="og:site_name" content="The Agenda">\n'
            f'<meta property="og:title" content="{e(title)}">\n'
            f'<meta property="og:description" content="{e(desc)}">\n'
            f'<meta name="twitter:card" content="summary">\n'
            f'<meta name="agenda-page" content="{e(path)}">\n')


def render(page, title, desc, path):
    assert page.count("<title>The Agenda</title>") == 1, "pages.py: expected one <title>The Agenda</title>"
    return page.replace("<title>The Agenda</title>",
                        f"<title>{html.escape(title)}</title>\n" + head_tags(title, desc, path), 1)


def main():
    page = open(SRC, encoding="utf-8").read()
    blurbs = button_blurbs(page)
    missing = [t for t in PAGES if not blurbs.get(t)]
    if missing:
        sys.exit(f"pages.py: no home-page button text for {missing}")
    os.makedirs(OUT, exist_ok=True)
    home = render(page, "The Agenda", HOME_DESC, "/")
    for name in ("index.html", "404.html"):
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(home)
    for tab, (folder, name) in PAGES.items():
        d = os.path.join(OUT, folder)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(
            render(page, f"{name} · The Agenda", blurbs[tab], f"/{folder}/"))
    print(f"Wrote site/index.html and {len(PAGES)} tab pages")


if __name__ == "__main__":
    main()
