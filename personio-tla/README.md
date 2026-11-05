# Personio × Thought Leader Ads: prospect finder

Finds employees of Personio customers who would be good voices for Personio Thought Leader Ads on LinkedIn, and ranks them.

| Step | Script | Source |
|---|---|---|
| 1. Customer list | `companies.json` | Exa search of public Personio case studies (later: Personio's own customer export) |
| 2. Employees | `1_find_people.py` | Apify `harvestapi/linkedin-profile-search` (full profiles) |
| 3. Activity | `2_fetch_posts.py` | Apify `harvestapi/linkedin-profile-posts` (last 90 days) |
| 4–5. Score + rank | `3_score.py` | Rules: see `METHOD.md` |
| Output | `4_build_sheet.py` | `data/personio_tla_prospects.xlsx` |

```bash
export APIFY_TOKEN=...   # already set in the cloud environment
python3 1_find_people.py && python3 2_fetch_posts.py && python3 3_score.py && python3 4_build_sheet.py
```

Useful flags: `1_find_people.py --reuse` re-processes cached results without new Apify spend, and `--only "Emma,Statista"` re-runs just those companies.
To scale up to Personio's real customer list, replace `companies.json` with the same fields
(`name`, `linkedin_query`, which can be a LinkedIn company URL, `linkedin_slugs`, `country`, `employees`, `industry`, `evidence_url`).

`data/` holds scraped personal data and is git-ignored on purpose (GDPR). Don't commit it.
