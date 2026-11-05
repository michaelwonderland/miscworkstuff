"""Step 3: pull each candidate's last-90-day LinkedIn posts (HarvestAPI Profile Posts).

Only people with >= MIN_FOLLOWERS are fetched: activity only matters if there's an audience.
Output: data/posts.json  {profile_url_lower: [post, ...]}
"""
import json
import os

from apify import run_many

ACTOR = "harvestapi/linkedin-profile-posts"
MIN_FOLLOWERS = 300
BATCH = 25
OUT = "data/posts.json"

people = json.load(open("data/people_raw.json"))
have = json.load(open(OUT)) if os.path.exists(OUT) else {}
urls = [
    p["profile"]["linkedinUrl"]
    for p in people
    if (p["profile"].get("followerCount") or 0) >= MIN_FOLLOWERS
    and p["profile"]["linkedinUrl"].rstrip("/").lower() not in have
]
print(f"Fetching posts for {len(urls)} profiles")

batches = [urls[i: i + BATCH] for i in range(0, len(urls), BATCH)]
inputs = [
    {"targetUrls": b, "maxPosts": 20, "postedLimit": "3months", "includeQuotePosts": True,
     "includeReposts": True, "scrapeReactions": False, "scrapeComments": False}
    for b in batches
]
results = run_many(ACTOR, inputs) if inputs else []

cost = 0
for inp, items, run in results:
    cost += run.get("usageTotalUsd") or 0
    for u in inp["targetUrls"]:
        have.setdefault(u.rstrip("/").lower(), [])
    for post in items:
        q = (post.get("query") or {})
        src = (q.get("targetUrl") or q.get("profileUrl") or (post.get("author") or {}).get("linkedinUrl") or "")
        key = src.rstrip("/").lower()
        if key in have:
            have[key].append(post)
        else:  # fall back to author match
            have.setdefault(key, []).append(post)

json.dump(have, open(OUT, "w"), ensure_ascii=False)
print(f"Done. {sum(len(v) for v in have.values())} posts for {len(have)} profiles. cost ${cost:.2f}")
