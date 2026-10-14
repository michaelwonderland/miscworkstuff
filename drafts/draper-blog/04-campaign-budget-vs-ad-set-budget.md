---
title: "Campaign Budget vs Ad Set Budget: Which to Use for Testing"
meta_description: "Campaign budget vs ad set budget on Meta: use CBO to scale and on small accounts, ABO for a testing campaign at $1,000+ a day. The math behind each verdict."
slug: campaign-budget-vs-ad-set-budget
primary_keyword: campaign budget vs ad set budget
secondary_keywords: []
locale: en-US
profile: draper-ads
format: E missing explainer
byline: Draper Ads
word_count: 0
---

# Campaign Budget vs Ad Set Budget: CBO or ABO for Testing?

Use campaign budget (CBO) for your scaling campaign and for any account small enough to run as one campaign. Use ad set budget (ABO) for a dedicated creative testing campaign once you spend around $1,000 a day, because it guarantees every new test gets money.

Most guides stop at the definitions. The useful part is the verdict by situation, so that's what this page is for.

## What's the difference between campaign budget and ad set budget?

**Campaign budget lets Meta move one budget between your ad sets. Ad set budget fixes how much each ad set can spend.**

With CBO, which Meta now calls Advantage campaign budget, you set $450 a day on the campaign and Meta decides each ad set's share, day by day. With ABO, you set $150 on each of three ad sets and each one spends its $150.

One change since 2025 matters here. As creative strategist Dara Denney [pointed out in August 2025](https://www.youtube.com/watch?v=MmXb2JmWDj8&t=60s), Advantage+ became the default for sales campaigns, and its machine learning runs under both budget types.

So the choice is no longer "automated vs manual." It's who controls the split between ad sets: you or Meta.

## Which one should you use?

**Pick by the job the campaign does, then by spend.** Here's the verdict for each situation:

| Situation | Use | Why |
|---|---|---|
| Lean account, $5K to $30K a month, one campaign | Campaign budget | Too little money to split by hand |
| Testing campaign at ~$1,000 a day | Ad set budget | Each test gets a fixed, readable slice |
| Testing campaign at $1M+ a month | Ad set budget, usually | Fast reads on many tests a week |
| Scaling campaign with one ad set of winners | Either | With one ad set, there's nothing to split |

The testing rows are Denney's own calls. At the lean tier, she runs [one campaign with campaign budget and Advantage+ on](https://www.youtube.com/shorts/PVoC7H44A5w), with a new test ad set each week. At the growth tier, she calls the choice "a media buyer decision" but [uses ad set budgets herself](https://www.youtube.com/watch?v=7knQyPYLmfo&t=487s), throttling spend to get a read on new creative within a few days.

At $1M+ a month, she says she has seen only a select few testing campaigns succeed with campaign budget. Her guess at the reason is that creative teams want a quick read so they can start iterating.

## Why ad set budget wins for a testing campaign

**Under campaign budget, last week's test can starve this week's.**

Say your testing campaign has three ad sets, one for each of the last three weeks. Labeled inputs:

- Campaign budget: $450 a day
- Target cost per purchase: $40
- Ad set A, two weeks old, holds a clear winner
- Ad set C launched today, with 20 new statics

Meta favors what it already knows converts. So suppose it sends $320 a day to A, $90 to B and $40 to C.

At $40 a day, C buys about one purchase a day. Reaching 50 purchases, a fair point to call a test, takes about 50 days.

Put the same $450 on ad set budgets at $150 each. C now buys almost four purchases a day and reaches 50 in about 13 days.

Same money, a read roughly four times sooner. That's the case for ad set budgets in testing, and it's the same math we use to size tests in our [Facebook ads testing handbook](/blog/facebook-ads-testing).

There's a related warning from Denney: dropping a creative test into an otherwise performing campaign tends to drag that campaign down. Keep testing and scaling in separate campaigns, whatever the budget type.

## When campaign budget is the right call

**Below roughly $30K a month, campaign budget is the better default, testing included.**

At $5,000 a month, you have about $165 a day. Split that into three $55 ad sets and none of them buys enough purchases to learn from. One campaign-budget campaign pools the money, and the new ad set each week competes inside it.

Campaign budget also suits a buyer who would rather trust Meta's allocation than force it. Denney's own [breakdown of Seed Health's testing](https://www.youtube.com/watch?v=hGCdGNP5oGE) describes a team that stopped forcing even spend across ads because it pushed money into creative the algorithm had already judged less scalable.

The same logic applies one level up. If an ad set gets little spend under campaign budget, that's information, not unfairness.

And in the scaling campaign, the question mostly disappears. Denney keeps [all winners in a single ad set](https://www.youtube.com/watch?v=MmXb2JmWDj8&t=182s), growing to 50+ ads over time. With one ad set, campaign and ad set budgets do the same thing.

## What the choice means for launching

**Ad set budgets mean a new ad set for every test, every week.**

That's the hidden cost. At Denney's current sizing of 10 to 25 ads per test ad set, each new test is 20 ads built inside a fresh ad set. In Ads Manager, building one ad from scratch inside one ad set takes 17+ clicks.

So a 20-ad weekly test is 20 × 17 = 340 clicks, before naming each ad and typing its UTMs. That's 1,360 clicks a month on one testing campaign.

If you launch a 10-ad test once a month, Ads Manager handles it fine. If it's every week, that's the job Draper Ads does: build the ad once, launch it to the right ad sets, with names and UTMs filled in.

Pick the budget type for the read you need, not for the setup it saves.

*If launching new test ad sets is eating your week, Draper Ads is what we built to fix it.*

Draper Ads is free during beta. Connect your ad account, build the ad once, and launch it to every ad set in one go. No credit card, and setup takes under two minutes. [Try Draper Ads](https://draperads.com/sign-up).

<!-- editor-notes
Angle chosen: "Pick by the job, then by spend" (counter-narrative to the SERP's generic definitions). Verdict table by situation, with the worked math showing why campaign budget starves a new test inside a testing campaign, plus the scaling-campaign point that one ad set makes the choice moot.
Angles rejected: (1) "CBO is dead for testing": too absolute; Denney recommends CBO for lean accounts. (2) "It doesn't matter anymore because Advantage+ powers both": true in part but leaves the searcher without a verdict.
Named concept: none coined; the post borrows "days to signal" style math from the pillar without naming it, to keep the short post focused.
Open TKs: none.
Claims to verify:
- Meta's current name for CBO is "Advantage campaign budget" (general knowledge; confirm UI label).
- Scale tier: the knowledge base file says "nearly all use CBO", but the transcript of Test at Every Budget (12:12) reads "nearly all brands are using [term dropped by transcription]... I've seen a select few ad accounts recently that were successfully using CBO at scale like this." The transcript drops "ABO" elsewhere too (e.g. "manual campaigns which included CBO and [ ]"). The draft follows the transcript: ABO is the norm at scale, CBO the exception. Worth confirming by ear.
- Aug 2025 video: Denney says she "really do[es] prefer to use [term dropped]" for the testing campaign; consistent with ABO but not quoted.
- Timestamps t=60s, t=487s, t=182s derived from transcript segment markers (1:00, 8:07, 3:02).
- The $320/$90/$40 split is a labeled hypothetical, not observed data.
Lint: see final run.
Self-score: intro 8/10, average section 7.6/10.
No first-hand account data; the post relies on Denney's cited positions and worked arithmetic.
-->
