"""Sanity checks run after every build. A run that fails these must not be published."""
import json, os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(ROOT, "data.json")))
html = open(os.path.join(ROOT, "index.html")).read()
problems = []
if len(html) < 1_000_000: problems.append(f"index.html is only {len(html):,} bytes")
if "__DATA__" in html: problems.append("data was not injected into the template")
if len(d["sen"]) != 100: problems.append(f"expected 100 Senate seats, found {len(d['sen'])}")
if len(d["gov"]) != 50: problems.append(f"expected 50 governors, found {len(d['gov'])}")
for s in d["sen"]:
    for k, v in s["r"].items():
        if not (isinstance(v, list) and len(v) >= 2 and v[0]):
            problems.append(f"bad Senate cell {s['n']}/{k}")
L = d.get("ladder", {})
if not L or len(L.get("G", {})) != 50: problems.append("ladder scores missing")
if problems:
    print("CHECKS FAILED:\n- " + "\n- ".join(problems)); sys.exit(1)
print("checks passed")
