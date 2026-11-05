"""Step 1-2: for each Personio customer, find current employees on LinkedIn.

Two searches per company (HarvestAPI LinkedIn Profile Search, full profiles):
  A) HR / Finance / Accounting functions, Senior level and up
  B) CXO + Owner/Partner, any function (CEO, founders, MD, CFO, COO...)
Only people whose *current* employer is the exact LinkedIn company (linkedin_slugs) are kept.

Usage:
  python3 1_find_people.py                  # run all searches
  python3 1_find_people.py --reuse          # re-process cached results only
  python3 1_find_people.py --only "Emma,interaktiv"   # re-run some companies, keep the rest cached
Output: data/people_raw.json
"""
import json
import os
import re
import sys
import unicodedata

from apify import run_many

ACTOR = "harvestapi/linkedin-profile-search"
FN_HR, FN_FIN, FN_ACC = "12", "10", "1"
SEN_SENIOR_UP = ["120", "200", "210", "220", "300", "310", "320"]
SEN_EXEC = ["310", "320"]
CACHE = "data/search_results.json"

companies = json.load(open("companies.json"))


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def matches(company, pos):
    slug = pos.get("companyUniversalName")
    if slug:
        return slug in company.get("linkedin_slugs", [])
    # no LinkedIn company page linked: require the full company name inside the employer text
    name = norm(company["name"].split("/")[0].split("–")[0])
    return bool(name) and name in norm(pos.get("companyName"))


def search_inputs(c):
    base = {"profileScraperMode": "Full", "currentCompanies": [c["linkedin_query"]]}
    return [
        {**base, "functionIds": [FN_HR, FN_FIN, FN_ACC], "seniorityLevelIds": SEN_SENIOR_UP, "maxItems": 25},
        {**base, "seniorityLevelIds": SEN_EXEC, "maxItems": 12},
    ]


cache = {}  # company name -> list of [input, items, run]
if os.path.exists(CACHE):
    old = json.load(open(CACHE))
    if isinstance(old, list):  # legacy flat format: 2 entries per company in companies.json order
        old = {c["name"]: old[2 * i: 2 * i + 2] for i, c in enumerate(companies)}
    cache = old

only = None
if "--only" in sys.argv:
    only = [s.strip().lower() for s in sys.argv[sys.argv.index("--only") + 1].split(",")]
todo = [] if "--reuse" in sys.argv else [
    c for c in companies if (only is None or any(o in c["name"].lower() for o in only))
]

if todo:
    inputs = [(c, i) for c in todo for i in search_inputs(c)]
    print(f"Starting {len(inputs)} searches for {len(todo)} companies...")
    results = run_many(ACTOR, [i for _, i in inputs])
    for c in todo:
        cache[c["name"]] = []
    for (c, _), res in zip(inputs, results):
        cache[c["name"]].append(list(res))
    json.dump(cache, open(CACHE, "w"), ensure_ascii=False)

people = {}
for c in companies:
    found = kept = 0
    for _, items, run in cache.get(c["name"], []):
        for p in items:
            found += 1
            cur = [pos for pos in (p.get("currentPosition") or []) if matches(c, pos)]
            key = (p.get("linkedinUrl") or "").rstrip("/").lower()
            if cur and key and key not in people:
                kept += 1
                people[key] = {"company": c, "position": cur[0], "profile": p}
    print(f"{c['name']:36s} found={found:3d} kept={kept:3d}")

json.dump(list(people.values()), open("data/people_raw.json", "w"), ensure_ascii=False)
print("TOTAL people:", len(people))
