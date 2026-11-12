#!/usr/bin/env bash
# Rebuild the site from the data files and stage it for Netlify (site/).
set -euo pipefail
cd "$(dirname "$0")"
export PYTHONHASHSEED=0   # stable key order, so daily diffs show only real changes
python3 export.py
python3 checks.py
cp index.html site/index.html
cp index.html site/404.html
echo "Built site/index.html"
