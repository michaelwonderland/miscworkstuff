"""Check which candidates have already appeared in Personio's LinkedIn ads.

Input: data/personio_ads.json (Apify alexmorain/linkedin-ad-library-scraper, advertiser=personio, ~12 months)
Matches a candidate if:
  - they are the poster of a Thought Leader Ad (promoted_by / member author), or
  - their full name, or their company with a testimonial-style mention, appears in the ad copy.
Output: data/ad_matches.csv, plus a list of all Thought Leader Ad posters (data/tla_posters.csv).
"""
import csv
import json
import re
import unicodedata

ads = json.load(open("data/personio_ads.json"))
people = list(csv.DictReader(open("data/ranked.csv")))
companies = json.load(open("companies.json"))


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def ad_text(a):
    return norm(" ".join(str(a.get(k) or "") for k in ("headline", "body", "promoted_by", "description", "cta")))


def clean_name(n):
    n = re.sub(r"\b(dr|prof)\b\.?", "", n, flags=re.I)
    return norm(n)


# Thought Leader Ads = ads promoted by a member rather than the company page
tla = [a for a in ads if a.get("promoted_by") or "thought" in str(a.get("format", "")).lower()]
with open("data/tla_posters.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Promoted by", "Format", "Ran from", "Ran to", "Impressions", "Countries", "Body preview", "Ad URL"])
    for a in tla:
        w.writerow([a.get("promoted_by"), a.get("format"), a.get("ran_from"), a.get("ran_to"), a.get("impressions_display"),
                    "; ".join(f"{c['country']} {c['share']}" for c in a.get("impressions_by_country") or []),
                    (a.get("body") or "")[:160], a.get("detail_url")])

texts = [(a, ad_text(a), norm(a.get("promoted_by"))) for a in ads]
matches = []
for p in people:
    name = clean_name(p["Name"])
    parts = name.split()
    if len(parts) < 2:
        continue
    first, last = parts[0], parts[-1]
    for a, t, poster in texts:
        how = None
        if poster and first in poster.split() and last in poster.split():
            how = "Thought Leader Ad poster"
        elif re.search(rf"\b{re.escape(first)}\b.*\b{re.escape(last)}\b", t):
            how = "named in ad copy"
        if how:
            matches.append({"Rank": p["Rank"], "Tier": p["Tier"], "Name": p["Name"], "Title": p["Title"], "Company": p["Company"],
                            "Match": how, "Promoted by": a.get("promoted_by"), "Format": a.get("format"),
                            "Ran": f"{a.get('ran_from')} – {a.get('ran_to')}", "Impressions": a.get("impressions_display"),
                            "Body preview": (a.get("body") or "")[:200], "Ad URL": a.get("detail_url")})

# company-level: customer brands featured in Personio ads (case-study ads)
company_hits = []
for c in companies:
    toks = [t for t in norm(c["name"].split("/")[0].split("–")[0]).split() if len(t) > 2]
    key = " ".join(toks)
    if not key:
        continue
    n = [a for a, t, _ in texts if re.search(rf"\b{re.escape(key)}\b", t)]
    if n:
        company_hits.append((c["name"], len(n), n[0].get("detail_url"), (n[0].get("body") or "")[:150]))

with open("data/ad_matches.csv", "w", newline="") as f:
    cols = ["Rank", "Tier", "Name", "Title", "Company", "Match", "Promoted by", "Format", "Ran", "Impressions", "Body preview", "Ad URL"]
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(matches)

print(f"ads: {len(ads)} | thought-leader-style ads: {len(tla)} | distinct posters: {len({a.get('promoted_by') for a in tla})}")
from collections import Counter
print("formats:", Counter(a.get("format") for a in ads).most_common())
print("top posters:", Counter(a.get("promoted_by") for a in tla).most_common(40))
print("\nCANDIDATE MATCHES:", len(matches))
for m in matches:
    print(" ", m["Rank"], m["Name"], "|", m["Company"], "|", m["Match"], "|", m["Ran"], "|", m["Ad URL"])
print("\nCUSTOMER COMPANIES MENTIONED IN ADS:")
for x in company_hits:
    print(" ", x)
