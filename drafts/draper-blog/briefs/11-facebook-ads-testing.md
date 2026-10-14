# Panel brief: How should I test creative on Meta, at my budget?

```yaml
question: "How should I test creative on Meta, at my budget?"
primary_keyword: "facebook ads testing"
secondary_keywords: ["testing ads on facebook", "meta creative testing", "how many ads per ad set"]
search_intent: informational
size: long
format: G handbook (pillar; hub for 01, 04, 05, 06)
profile: draper-ads
experts_consulted: [barry-hott, dara-denney, phil-kiel, nick-theriot, alessio-cordeddu, ben-heath, marin-istvanic, lorenzo-pravata]
```

Paths are relative to `/home/user/aimarketingschool/experts/`. "K/" = `knowledge/`.

## 1. Coverage

| Corpus | Coverage | Where |
|---|---|---|
| Dara | Full: sizing, big swings, windows, budget tiers, 70/30 | `dara-denney/K/frameworks/creative-testing-protocol.md`, `K/themes/creative-testing.md`, `K/evolution.md §2, §5` |
| Marin | Full: concept-per-ad-set ABO pipeline, weekly clock, proxies, hit-rate-indexed volume | `marin-istvanic/K/frameworks/abo-testing-to-scaling-pipeline.md`, `K/themes/testing-and-iteration.md` |
| Alessio | Full: ABO test / CBO scale, four kill/graduate rules, spend-band budgets | `alessio-cordeddu/K/frameworks/creative-testing-protocol.md`, `K/frameworks/scaling-roadmap-by-spend.md` |
| Ben | Full: scaling + testing campaigns, the four testing options, test priority order | `ben-heath/K/frameworks/scaling-testing-campaign-structure.md`, `K/frameworks/testing-priority-hierarchy.md`, `K/evolution.md §2` |
| Phil | Full: in-situ testing, win rate, spend-based kill rules, weekly rhythm | `phil-kiel/K/themes/testing-and-iteration.md`, `K/evolution.md §3` |
| Nick | Full: one-CBO testing, 3 creatives per idea, refuses a volume number, kill procedure | `nick-theriot/K/frameworks/creative-testing-system.md`, `K/frameworks/one-campaign-account-structure.md`, `K/evolution.md §2, §3, §12` |
| Barry | Partial: how results are read (spend, not ad-level metrics), 90/10, hit-rate rejection. No test-structure spec | `barry-hott/K/themes/testing-and-measurement.md`, `K/frameworks/creative-resourcing-90-10.md`, `K/frameworks/hit-rate-rejection.md` |
| Lorenzo | Partial: batch cadence, win rate, kill reversal. Declares his account layer thin; no ad-set test structure | `lorenzo-pravata/K/themes/testing-win-rate-and-account-discipline.md` |

No corpus is silent. Barry and Lorenzo are silent on ad-set sizing and test budgets specifically; do not stretch them there.

## 2. Consensus

1. **Variants must be visibly different; single-variable tweaks are retired.** Dara (`creative-testing-protocol.md §Hook variants`), Phil (`phil-kiel/K/themes/testing-and-iteration.md §Retired tactics`, 2025-06), Marin (`marin-istvanic/K/themes/testing-and-iteration.md §Isolation-effect testing`), Alessio (`alessio-cordeddu/K/frameworks/creative-testing-protocol.md §2`, scroll-past litmus test), Nick (`nick-theriot/K/evolution.md §14`, 2025-11: headline swaps on one image "classified as the same ad"), Ben (`scaling-testing-campaign-structure.md §Option 4`: same-body-different-hook variants can be treated as duplicates). Six corpora.
2. **Most tests fail, by design; judge the portfolio, not each ad.** Ben ("most tests fail", VC framing, `testing-priority-hierarchy.md §The diagnosis`), Phil (10-20% is a good win rate, `testing-and-iteration.md §Current tactic`), Nick (1 in 10 normal, `evolution.md §15`), Lorenzo (80%+ won't become winners, `testing-win-rate-and-account-discipline.md §Testing cadence`), Marin (losers land at 1.2-1.5 vs target 2, `testing-and-iteration.md §Principle 4`).
3. **Never kill the winner to "move" it. Promotion is a copy; the original keeps running.** Marin (`abo-testing-to-scaling-pipeline.md §5`), Alessio (`creative-testing-protocol.md §The one thing everyone gets wrong`), Phil ("Duplication ❌ Scale where it is ✅", `testing-and-iteration.md §Retired`), Nick (stopped migrating winners 2024, `evolution.md §10`), Ben (don't turn off the current winner, `scaling-testing-campaign-structure.md §What not to do`), Barry (never turn off the top spender, `account-structure-and-media-buying.md §4`).
4. **Write a hypothesis before launch.** Dara (`themes/creative-testing.md §Principle 3`), Nick ("If we can't fill that in, we don't make the ad", `creative-testing-system.md §Step 1`), Alessio ("you're gambling", `creative-testing-protocol.md §The principle`), Ben (test hypotheses with a batch, `testing-priority-hierarchy.md §Test hygiene`), Marin (hypothesis per concept, `abo-testing-to-scaling-pipeline.md §2`).
5. **Launch on a fixed cadence, not when performance dips.** Nick (`creative-testing-system.md §Weekly production pipeline`), Marin (Wednesday launches, `abo-testing-to-scaling-pipeline.md §3`), Phil (Mon scale / Wed launch / Fri pause, `testing-and-iteration.md §Current tactic`), Lorenzo (batch days on a calendar, `§Testing cadence`), Dara (new test ad set every week on small budgets, `creative-testing-protocol.md §Ad-set sizing`).
6. **Decide on spend and conversions, not on a day count.** Ben (refuses "run it N days", CONCEPTS `experiment.significance_threshold`), Phil (spend + performance, never a clock), Alessio ($900 + ~10 conversions, AOV-adjusted), Marin (survives repeated budget raises). Note Ben's 2025-04 video still says "use a statistical-significance calculator" (`testing-priority-hierarchy.md §Test hygiene`); Marin rejects significance outright.
7. **Offer and product come before creative testing.** Ben (offer first in the test order, `testing-priority-hierarchy.md §The order`), Marin (Product > Offer > Creative > Media buying; hit rate moved by offer, `testing-and-iteration.md §Current tactic`), Alessio (under $10K/mo the variable is the offer, `scaling-roadmap-by-spend.md §Phase 1`), Dara (economics gate the conversation, `dara-denney/index.md` rule 6).
8. **Test creative, not audiences; broad targeting.** Marin (`testing-and-iteration.md §Principle 2`), Dara (2025-08 short: "focusing entirely on testing creatives, not on audiences"), Nick (`one-campaign-account-structure.md §Ad set level`).

## 3. Splits

### 3a. How many ads per test ad set (the keyword question)
- **Camp A, one concept per ad set, 3-6 variants:** Marin 3-6 (Jan 2026), 3-5 (Jul 2026), ceiling 5-6 (`abo-testing-to-scaling-pipeline.md §2`); Alessio 3-5, three lengths for a net-new concept (`creative-testing-protocol.md §1-2`); Nick exactly 3 (`creative-testing-system.md §Step 2`); Phil 4-6 in a test ad set, 10-15 in an evergreen one (`testing-and-iteration.md §Principle 6`). Reasoning: a clean read per idea, and each concept gets its own budget. Wins when you run a testing campaign with per-ad-set budgets.
- **Camp B, a multi-concept batch of 10-25:** Dara 10-25 (statics 20-25, video 10-15; no more than 2-3 variants of one concept), explicitly retiring her 2-4 (`dara-denney/K/evolution.md §2`); Ben 20+ as the target at volume but **start with 4 genuinely different concepts**, "don't create volume for the sake of volume" (`ben-heath/K/evolution.md §2`); Nick's new-product launch ad set holds 6-12 different ads (`one-campaign-account-structure.md §Worked example`). Reasoning: Meta allocates inside the ad set, so diversity inside it is what's being tested.
- **What it's really about:** two different quantities. Camp A counts variants of one idea; Camp B counts distinct ideas sharing a budget. Both cap near-duplicates at about 3.
- **Verdict:** if each concept gets its own ad set and budget, 3-6 variants. If you load one ad set and let Meta allocate, 10-20 distinct ads, with at most 2-3 per concept. Below ~$100/day, start with 4 strong, different concepts rather than 20 weak ones.

### 3b. Where new creative is tested
- **Camp A, a separate, funded testing campaign:** Marin (ABO, one ad set per concept; the testing campaign is also where winners scale), Alessio (ABO test, CBO scale, ~20:80), Ben (testing + scaling, one ad set each, gated at ~50 conversions/week), Dara at ~$1,000/day+ (adding tests to a performing campaign "tanks" it, `creative-testing-protocol.md §Tier 2`). Reasoning: incumbents with social proof starve new ads.
- **Camp B, test in situ:** Phil, 2026-02-24: separating testing and scaling is "a waste of time" (`phil-kiel/K/evolution.md §3`), though his own Apr and Aug 2026 posts still show a separate ABO testing branch; date it and flag the tension. Nick: one CBO, new ad sets weekly, no testing campaign (`one-campaign-account-structure.md §The principle`). Dara at $5-30K/mo: one Advantage+/CBO campaign. Ben's option 3 below 50 conversions/week: new, meaningfully different ads into the same ad set.
- **What it's really about:** conversion volume and budget. Everyone agrees winners aren't killed and rebuilt; the split is whether a new concept gets its own protected budget.
- **Verdict:** below ~50 conversions/week (or under ~$1K/day), one campaign: add new ad sets or new ads there. Above it, a separate testing campaign with fixed per-concept budgets; copy winners out by post ID and leave the originals running.

### 3c. How much to test per week
- **Indexed to hit rate:** Marin, ~40% hit rate supports ~20 concepts/week, ~10% means ~5 (`abo-testing-to-scaling-pipeline.md §2`).
- **Fewer, bigger:** Phil, 5-10 well-considered ads a week; solo founders 2 a week; "have you tried launching less ads?" (`testing-and-iteration.md §Current tactic`). Nick refuses a number after a costed volume failure (`evolution.md §3`).
- **Fixed high volume:** Lorenzo, 25 ads/week (2026-01) or ~65/month (2026-08), unreconciled; Dara at $1M+/mo, 10-20+ tests/week.
- **Verdict:** volume is set by what your budget can fund to a readable spend and by your hit rate, not by ambition. Show the arithmetic in the article.

### 3d. Iteration vs net-new
- **Net-new heavy:** Barry 90/10 (2024-12 panel, `creative-resourcing-90-10.md §1`), guarding against "iteration paralysis".
- **Iteration heavy:** Dara ~70/30 iterative (reversed her 2024 90/10; 2026: under-iteration is the #1 problem); Phil ~70% proven / 30% exploration (2026-02); Nick ~80/20; Alessio 80-90% of winners from variations, speculation capped at 10-20%.
- **Neither:** Marin refuses a ratio; cosmetic iteration is dead, structural iteration works (CONCEPTS `creative.iteration_ratio`).
- **Verdict:** the 2026 weight is iteration-heavy (four corpora), with the rule that an "iteration" must look different (new person, setting, length, format), not a cosmetic tweak. Present 90/10 as the counterweight for accounts stuck on one look.

### 3e. Kill discipline
- **Fast, pre-written stop-losses:** Alessio, 2× target CPA with zero sales in 2-3 days; Marin, 2× target cost per add-to-cart with no sale, or spend at 2× AOV with zero sales; Phil, $200 at 3× target CPA.
- **Don't kill what's spending:** Barry (don't act on ad-level metrics; sort by spend), Lorenzo 2026-08 ("spend is a confidence signal", reversing his earlier 3× CPA kill), Nick 2026-08 (protect the top two spenders; any pause is reversible after 3 days).
- **What it's really about:** the stage. Stop-losses apply to new tests that are burning budget with no sales. The don't-kill rule applies to ads the system is already funding.
- **Verdict:** cut new tests fast on a pre-set multiple; never cut an established spender on ad-level ROAS alone. Check the account's blended result 1-3 days after any cut.

### 3f. Is hit rate the right scoreboard?
Marin and Phil make it the core metric (Phil: below 10% you're in a volume game). Lorenzo uses "win rate" defined as becoming a top spender. Barry rejects hit rate and judges a creative source by how much spend its ads carry. Nick holds both views within three weeks (`evolution.md §15`). **Verdict:** track the share of tests that reach real spend at target, and say the definition out loud.

## 4. Single-source insights
- Proxy reads two days in: back-solve target cost per add-to-cart and per checkout from target CPA and historical funnel rates (Marin, `abo-testing-to-scaling-pipeline.md §3`). Sound arithmetic; usable as our reasoning.
- A one-week outcome of roughly a third killed, a third scaled, a third held on a lower budget (Marin). Self-reported; "some practitioners".
- Test order: offer, angle, style, hook, then small variables (Ben, `testing-priority-hierarchy.md`). First-principles sound.
- Testing budget share shrinks as spend grows: ~100% under $10K/mo, ~20% at $10-100K, 10-15%, 5-10%, under 5% at $1.5M+ (Alessio, `scaling-roadmap-by-spend.md`).
- Three lengths (short, main, long) instead of three hooks for a new concept (Alessio).
- Sort ad sets by 7-day spend: 90% of spend on two ads signals a diversity problem (Phil, 2026-02).
- Reviving starved ads in a small fixed-budget campaign (Phil). Interesting, one account's result; "some practitioners".
- Seed new tests small: $100/day for five days beats $500 killed by afternoon (Marin).

## 5. Numbers
- **Ads per test ad set:** 3 to 25. Concept-per-ad-set camp clusters at 3-6 (Marin, Alessio, Nick, Phil; 2025-26). Batch camp at 10-25 (Dara 2025-08; Ben 20+ at volume, start at 4, 2026-03). Meta's own guidance per Ben moved from a 6-ad recommendation (2024) to no worry about an upper limit (2026-02); verify against Meta docs.
- **Daily budget per test ad set:** $50-500, most cite $100-200 (Marin 2026-06; Dara growth tier 2025-03). Dara's scale tier: ~$200/day for ~7 days or until ~$1,000 spent. Alessio's floor formula: (target CPA × 50) ÷ 7 per week of ~50 purchases. Nick's single-CBO default: $100/day for the campaign.
- **Spend before judging:** ~$500 (AOV under $100) to $2,000+ (AOV over $300) (Phil 2025-12); ~$900 + 10 conversions, AOV-adjusted (Alessio 2025-11).
- **Read windows:** 2-day proxy read and 5-day decision (Marin); 7 days hands-off (Nick); 7-10 days default, adjusted by conversion volume (Ben 2025-04); ~7 days to ~2 weeks (Dara 2025).
- **Stop-loss multiples:** 2× target CPA with zero sales (Alessio) to 3× at $200 spent (Phil); 2× target cost per ATC (Marin).
- **Testing share of budget:** ~20% at growth stage (Alessio, Ben's normal 80/20 dial); falls to under 5% at $1.5M+/mo (Alessio).
- **Hit rate:** 10-20% "good" (Phil); ~10% normal (Nick); 10-40% range across good and bad stretches (Marin). Never present as a benchmark.
- **Iteration share:** 10% (Barry 2024) to ~80-90% (Nick, Alessio); 2026 cluster 70-80%.
- **Learning phase:** ~50 optimisation events per ad set per week (Ben 2026-03). Primary source: verify in Meta docs.

## 6. Myths and retired advice
- **"Change one variable at a time."** Retired by Phil (2025-06), Marin (2023-24 isolation testing, superseded post-Andromeda), Dara (rejected "Absolutely not", 2026-06). Ben's 2025-04 "isolate one variable" survives only at the hypothesis level (test a batch against one claim), not as one-word tweaks.
- **"Four hook variants of one video is a test."** Alessio's default for two years, now his named anti-pattern (`alessio-cordeddu/index.md` rule 3).
- **"2-4 variations per test."** Dara, retired 2025-08.
- **"Kill anything that hasn't won in 7 days."** Nick retired it (2025-09 → 2026-08); Phil replaced day counts with spend rules (2025-12).
- **"An ad running 200+ days is a winner."** Dara, retired 2025-04.
- **"Exiting the learning phase makes CPA drop sharply."** Marin's standing debunk (`testing-and-iteration.md §Principle 5`).
- **"Duplicate the winner into scaling and pause the original."** Phil (2026-01), Nick (2024), Alessio, Marin all against.
- **"Force even spend across every test ad."** Dara presents a large brand abandoning it; Nick ran forced spend vs CBO and lost. Ben still forces spend via a testing campaign, so frame the myth as forcing spend onto every ad, not funding a testing campaign.
- **"Max 6 ads per ad set."** Ben, 2024 → no upper limit 2026.
- **"Cost caps for testing."** Marin never; Alessio tests caps only in a separate CBO with proven winners.

## 7. Do not use in the article
- All expert names, handles, quotes, video/post links; Dara's business partner; guests (Seed Health's strategist).
- Coined names: "Monday-Wednesday-Friday Protocol", "supporting winners", "ecosystem, not a monarchy", "the ABO Scaling guy", "budget ladder" (describe it instead), "early indicators", "Jpeg factory", "zombie campaigns", "basic banger ad printing", "creative flooding", "grand slam / low-profile winner", "trim the fat", "dimensional variations", "iteration ladders", "iteration paralysis", "spend carried", "freshness share", "distance-to-target rule", "all-funnel campaign", "5 Levels", "Million Dollar Iteration Playbook", "Andromeda tax", "70/30 Rule", "Scalability School".
- Brand stats and case studies: Caraway (70/30, 300+ live ads), Seed Health (sprints, "1 in 7"), Varos live-creative counts by spend tier, the UK puzzle-notebook £ results, Nick's cigar client "180", Nick's consolidation CPA drops and forced-spend $71 vs $36, Ben's 5.7x UGC example, Phil's Related Media anecdote and zombie 2.5 ROAS, Phil's −30% CVR duplication result, Marin's client 10%→40% hit rate, the 500-creatives/week client, Marin's "four accounts seeded at $100".
- Self-reported scale and losses: Marin's $7M/mo, Nick's "six figures"/$70K/$450K, Nick's 50/week and 15/week retainer outputs, Lorenzo's audit counts.
- The claim that Meta told someone Andromeda "only recognises visual difference": second-hand from an office visit, not documented. Say "practitioners report" or cite Meta docs.

## 8. Draper angle
- Every structure in section 3 multiplies launches: one ad set per concept, weekly, with 3-6 variants, plus copying winners into a scaling campaign by post ID. That's 17+ clicks per ad built from scratch inside one ad set (profile proof point; state the rebuild assumption). Worked example to show in the open: 5 concepts × 4 variants = 20 ads/week × 17 clicks = 340 clicks, hypothetical inputs.
- Draper fits the "build once, deploy to many ad sets" step and naming: automatic ad names from the creative file make concept/variant naming consistent, which every corpus's analysis depends on.
- Tension to handle: the profile's belief "creative volume wins" collides with the panel's "volume without diversity doesn't count". Frame Draper as removing the launch cost of **diverse** tests, not as a volume engine. No ROAS claims.

## 9. Open questions
- Meta docs: current max ads per ad set; Meta's recommended ads-per-ad-set range; learning-phase threshold; the native creative-testing tool (variant count, default comparison metric, audience partitioning); whether reusing a post ID preserves engagement; daily budget overspend tolerance.
- Whether Andromeda groups near-duplicate creatives: practitioners agree, the mechanism is undocumented.
- `[TK]` candidate: first-hand data on time to launch one weekly test batch manually vs with Draper.
- Corpus doesn't settle an ad-set count for $3K-30K/month accounts under the concept-per-ad-set model; derive with arithmetic from the budget floors.
