Personio x Thought Leader Ads: prospect ranking (pilot, DACH, 24 customers)

PIPELINE
1. Customers: 25 DACH companies with a public Personio case study (personio.de/.com/.ch references), found with Exa. interaktiv gGmbH dropped (no LinkedIn employees found). Leaves 24.
2. Employees: Apify HarvestAPI LinkedIn Profile Search, 2 searches per company: (a) HR/Finance/Accounting functions, Senior level and up, max 25; (b) CXO + Owner/Partner, any function, max 12. Kept only people whose CURRENT employer is that exact LinkedIn company page.
3. Activity: Apify HarvestAPI Profile Posts, last 90 days (max 20 posts), for everyone with 300+ followers.
4-5. Score 0-100 and rank.

SCORE (0-100)
Reach 30: log-scaled followers (200 = 0, 20k+ = 30)
Activity 25: own posts in 90d (2 pts each, max 12; reshares add at most 3) + median reactions+comments on own posts (log-scaled, 200+ = 13)
Title fit 25: HR leader (CHRO/CPO/VP/Head/Director People/HR) 25 | CFO 22 | CEO/Founder/MD 20 | HR/People team 18 | Finance leader 17 | COO 14 | Other C-level 9 | Finance 12 | Partner/Director 8 | Other 4 (x0.8 if only matched via headline)
Topic fit 10: recent posts about people/HR/work/leadership/finance topics (3+ posts = full)
Personio 10: posted about Personio 10 | reshared Personio content 8 | mentions Personio on profile 6
Tiers: A >= 60, B 40-59, C < 40

CAVEATS
- Customer list = public case studies, some years old; confirm they are still customers with Personio's own data before outreach.
- LinkedIn search results are capped per company, so a large company's list isn't complete. Raise maxItems for the real run.
- Follower and post data scraped 5 Nov 2026 from public profiles. GDPR: only use for this B2B partnership purpose, don't export further, delete when the campaign is done.
- Title classification is rule-based; check odd titles by hand.

COST (pilot): Exa $0.10 + Apify about $7.40 (searches $6.2, posts $1.2)
