"""Steps 3-5: score every candidate and rank them as Thought Leader Ads prospects for Personio.

Score (0-100) =
  Reach        30  log-scaled followers (200 -> 0, 20k+ -> 30)
  Activity     25  posting cadence last 90 days (12) + median engagement on own posts (13)
  Title fit    25  proximity to Personio's buyer/voice titles (HR > CFO > CEO/MD > Finance > COO ...)
  Topic fit    10  share of recent posts about people/HR/work/leadership/finance topics
  Personio     10  mentions Personio in posts (10) or profile/experience (6)
Tier A >= 60, B >= 40, else C.
Output: data/ranked.csv, data/companies_summary.csv
"""
import csv
import json
import math
import re
import statistics
from datetime import datetime, timezone

people = json.load(open("data/people_raw.json"))
posts = json.load(open("data/posts.json"))
NOW = datetime.now(timezone.utc)

# --- title proximity -------------------------------------------------------
TITLE_RULES = [  # (points, bucket, regex) - first match wins, checked on title then headline
    (25, "HR leader", r"\b(chro|chief (people|human|hr|talent|culture)|vp (of )?(people|hr|human)|head of (people|hr|human|talent|culture)|"
                      r"vice president[^|,]{0,12}(people|hr\b|human|talent)|(director|leiter|leitung|lead)[^|,]{0,25}(people|hr\b|human resources|personal|talent|culture)|"
                      r"(people|hr|human resources|personal|culture)[^|,]{0,25}(director|leiter|leitung|lead\b|head)|personalleit|personalchef|"
                      r"people (and|&) culture)"),
    (22, "CFO", r"\b(cfo|chief financial|finanzvorstand|finanzgesch|kaufm(a|ä)nnische[rn]? (gesch|leit|vorstand))"),
    (20, "CEO / Founder / MD", r"\b(ceo|chief executive|co-?founder|founder|gr(ü|u)nder|managing director|gesch(ä|a)ftsf(ü|u)hr|vorstand|(?<!vice )president|"
                               r"inhaber|owner|general manager)\b"),
    (18, "HR / People", r"\b(hr|human resources|people|personal(referent|entwickl|wesen|abteilung|management)|talent|recruit\w*|payroll|lohn\w*|"
                        r"employer brand\w*|hrbp|people partner|culture|learning)\b"),
    (17, "Finance leader", r"\b((head|director|vp|leiter|leitung)[^|,]{0,20}(finance|finanz|accounting|controlling|rechnungswesen|buchhaltung)|"
                           r"(finance|finanz|accounting|controlling)[^|,]{0,20}(director|head|lead\b|leiter))"),
    (14, "COO", r"\b(coo|chief operating)\b"),
    (9, "Other C-level", r"\b(chief|cto|cmo|cro|cco|cdo|ciso)\b"),
    (12, "Finance", r"\b(finance|finanz|accountant|accounting|controller|controlling|buchhalt|treasury|tax)\b"),
    (8, "Partner / Director", r"\b(partner|director|direktor|head of|vp)\b"),
]


def title_fit(title, headline):
    for text in (title or "", headline or ""):
        t = text.lower()
        for pts, bucket, rx in TITLE_RULES:
            if re.search(rx, t):
                return pts if text == title else round(pts * 0.8), bucket
    return 4, "Other"


# --- topic fit -------------------------------------------------------------
TOPIC_RX = re.compile(
    r"\b(hr|people|culture|kultur|team|talent|hiring|recruit|onboard|employee|mitarbeit|leadership|f(ü|u)hrung|"
    r"payroll|lohn|benefit|future of work|arbeit|workplace|remote|hybrid|wellbeing|engagement|retention|"
    r"performance|feedback|growth|scale|finance|cfo|ai|ki|automation|digitali|compliance|employer)\w*",
    re.I,
)


def text_of(post):
    return " ".join(filter(None, [post.get("content"), (post.get("repost") or {}).get("content")]))


def lin(x, lo, hi):
    return max(0.0, min(1.0, (x - lo) / (hi - lo)))


rows = []
for p in people:
    prof, pos, comp = p["profile"], p["position"], p["company"]
    url = prof["linkedinUrl"].rstrip("/")
    followers = prof.get("followerCount") or 0
    plist = posts.get(url.lower(), [])

    # repostedBy set = they reshared someone else's post; otherwise they authored it (incl. quote posts)
    originals = [x for x in plist if not x.get("repostedBy")]
    reposts = len(plist) - len(originals)
    eng = [((x.get("engagement") or {}).get("likes") or 0) + ((x.get("engagement") or {}).get("comments") or 0) for x in originals]
    med_eng = statistics.median(eng) if eng else 0
    last = max((x.get("postedAt") or {}).get("date", "") for x in plist) if plist else ""

    reach = 30 * lin(math.log10(max(followers, 1)), math.log10(200), math.log10(20000))
    cadence = min(12.0, 2 * len(originals) + min(3.0, 0.25 * reposts))  # TLAs promote own posts; reshares count little
    engagement = 13 * lin(math.log10(1 + med_eng), 0, math.log10(201))
    activity = cadence + engagement

    tpts, bucket = title_fit(pos.get("position"), prof.get("headline"))

    topical = sum(1 for x in plist if TOPIC_RX.search(text_of(x)))
    topic = 10 * min(1.0, topical / 3)

    profile_text = " ".join(filter(None, [prof.get("headline"), prof.get("about")] +
                                   [e.get("description") or "" for e in prof.get("experience") or []]))
    own_p = sum(1 for x in originals if "personio" in json.dumps([x.get("content"), x.get("repost")], ensure_ascii=False).lower())
    shared_p = sum(1 for x in plist if x.get("repostedBy") and "personio" in json.dumps(x, ensure_ascii=False).lower())
    if own_p:
        pers, pers_note = 10, f"posted about Personio ({own_p}x in 90d)"
    elif shared_p:
        pers, pers_note = 8, f"reshared Personio content ({shared_p}x in 90d)"
    elif "personio" in profile_text.lower():
        pers, pers_note = 6, "mentions Personio on profile"
    else:
        pers, pers_note = 0, ""

    score = round(reach + activity + tpts + topic + pers, 1)
    tier = "A" if score >= 60 else "B" if score >= 40 else "C"

    why = [bucket, f"{followers:,} followers"]
    if plist:
        why.append(f"{len(originals)} posts + {reposts} reposts in 90d, median {med_eng:g} reactions")
    elif followers >= 300:
        why.append("no posts in 90d")
    if pers_note:
        why.append(pers_note)
    if prof.get("creator"):
        why.append("creator mode")

    rows.append({
        "Score": score, "Tier": tier,
        "Name": f"{prof.get('firstName', '')} {prof.get('lastName', '')}".strip(),
        "Title": pos.get("position"), "Title bucket": bucket, "Company": comp["name"],
        "Country": comp["country"], "Location": (prof.get("location") or {}).get("linkedinText", ""),
        "Followers": followers, "Posts 90d": len(originals), "Reposts 90d": reposts,
        "Median reactions": med_eng, "Last post": last[:10],
        "Personio signal": pers_note, "Creator mode": "yes" if prof.get("creator") else "",
        "Reach pts": round(reach, 1), "Activity pts": round(activity, 1), "Title pts": tpts,
        "Topic pts": round(topic, 1), "Personio pts": pers,
        "Why": " · ".join(why), "LinkedIn": url, "Headline": prof.get("headline"),
        "Customer evidence": comp["evidence_url"],
    })

rows.sort(key=lambda r: -r["Score"])
for i, r in enumerate(rows, 1):
    r["Rank"] = i
cols = ["Rank"] + [k for k in rows[0] if k != "Rank"]
with open("data/ranked.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)

# per-company summary
comp_rows = []
companies = json.load(open("companies.json"))
for c in companies:
    rs = [r for r in rows if r["Company"] == c["name"]]
    top = rs[0] if rs else None
    comp_rows.append({
        "Company": c["name"], "Country": c["country"], "Employees": c["employees"], "Industry": c["industry"],
        "Candidates found": len(rs), "Tier A": sum(r["Tier"] == "A" for r in rs), "Tier B": sum(r["Tier"] == "B" for r in rs),
        "Best prospect": f"{top['Name']} ({top['Title']}, {top['Score']})" if top else "",
        "Customer evidence": c["evidence_url"],
    })
comp_rows.sort(key=lambda r: (-r["Tier A"], -r["Tier B"]))
with open("data/companies_summary.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(comp_rows[0]))
    w.writeheader()
    w.writerows(comp_rows)

from collections import Counter
print("tiers", Counter(r["Tier"] for r in rows), "buckets", Counter(r["Title bucket"] for r in rows).most_common())
for r in rows[:30]:
    print(f"{r['Rank']:3d} {r['Score']:5.1f} {r['Tier']} {r['Name'][:24]:24s} {str(r['Title'])[:38]:38s} {r['Company'][:18]:18s} {r['Why'][:110]}")
