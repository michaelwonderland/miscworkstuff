---
title: "Campaign Budget vs Ad Set Budget: Which to Use for Testing"
meta_description: "Campaign budget vs ad set budget only matters for testing. Use ad set budget if winners pay for losers, campaign budget if budget is thin, and scale on CBO."
slug: campaign-budget-vs-ad-set-budget
primary_keyword: campaign budget vs ad set budget
secondary_keywords: []
locale: en-US
profile: draper-ads
format: E explainer
byline: Draper Ads
word_count: 947
---

# Campaign Budget vs Ad Set Budget

Campaign budget vs ad set budget is only a real choice when you're testing. Here's the rule:

- **Test on ad set budget (ABO)** if you can fund each new concept to a readable spend and enough tests win to pay for the losers.
- **Test inside one campaign-budget campaign (CBO, now Advantage campaign budget, or an Advantage+ campaign)** if your budget is thin for the number of ideas, or most of your tests fail.
- **Scale on campaign budget either way.**

The rest of this page is why, with the math that tells you which side of the line you're on.

## What's the difference?

**Ad set budget means you set the spend for each ad set. Campaign budget means you set one figure and Meta moves it between ad sets.** With ABO, every concept gets the money you gave it whether it wins or not, while with CBO, Meta shifts spend toward whatever looks best in the first day or two, often before slower ideas have had a chance.

That trade is the whole debate.

ABO buys a fair read and spends on losers. CBO saves money on losers and can starve a new idea before it gets a turn.

## Where experienced buyers agree

We compared how eight experienced Meta buyers set budgets. They agree on more than the forums suggest:

- **Fewer campaigns.** Every one of them has moved to one to three campaigns per account.
- **One ad set makes the question disappear.** If a campaign holds a single ad set, the two settings behave the same.
- **Scale on campaign budget.** Nobody argues for ad set budget as the scaling default.
- **The setting matters less than offer and creative.** It's the most-asked question in paid social and among the least important.

They also mostly agree that under campaign budget, new ads struggle to win spend next to proven ones. That one is contested, though. Some buyers have posted accounts where CBO spread spend across many ads, and others read a new ad's lack of spend as Meta's verdict on it.

## Should you test on ABO or CBO?

Experienced buyers split three ways on this.

**One camp tests on ad set budget.** Equal budgets mean a result reflects the ad, not how Meta happened to allocate. CBO, they add, is unstable at small spend. This camp is explicit that it's a math decision, not a preference: ABO works when enough tests win that the winners cover what the losers cost. It wins when budget covers every concept ad set at a readable daily amount and someone will adjust budgets on a schedule.

**A second camp tests inside one CBO or Advantage+ campaign,** adding a new ad set per idea each week. With ABO, you decide where the money goes; with CBO, Meta does. Some in this camp found that winners from cheap ABO test ad sets faded once they moved into a big CBO. It wins when budget is small relative to the number of creatives, hit rate is low, or nobody will manage budgets daily.

**A third camp says it doesn't matter.** With one ad set per campaign, it doesn't. Even experienced buyers who've argued both sides in public within a few months end up saying some accounts thrive on CBO and others on ABO, which tells you how much the setting decides on its own.

Not much.

**Our take:** the first camp's switch condition is the right one, because it's arithmetic rather than taste.

## The math: when do winners pay for losers?

Say your target CPA is $50. A fair read on a concept needs about ten conversions' worth of spend, which our [Facebook ads testing guide](/blog/facebook-ads-testing) calls the **read floor**: here, $500.

Under ABO, every concept spends its full read floor before you judge it:

- **4 concepts a week, 1 winner:** $2,000 of testing, $1,500 of it on losers. If one winner earns back more than $1,500 in margin, ABO pays.
- **10 concepts a week, 1 winner:** $5,000 of testing, $4,500 on losers, for the same single winner.

At one win in ten, ABO is paying full price for nine verdicts you could have had cheaper.

That's the point practitioners in the ABO camp switch to CBO, which cuts weak ads early at the cost of some ideas never getting a turn.

Some buyers patch CBO testing with minimum spend per ad set. Treat that as a patch, not a default, and never combine it with a cost cap, which overrides the minimum.

## What this changes for your launch week

**Your testing structure decides how many ad sets you launch into.** ABO testing means a new ad set per concept every week. Four concepts at four variations is 16 ads a week, each needing a name and UTMs. Winners then get copied into the scaling campaign, with the originals left running.

Building one ad from scratch inside one ad set takes 17+ clicks in Ads Manager. Rebuild those 16 ads and that's 272 clicks before a single winner is copied. Draper Ads builds each ad once and deploys it to every ad set it belongs in, named from the creative file, so the weekly ABO routine stops eating the afternoon you'd rather spend on next week's concepts. At one or two concepts a week, Ads Manager is fine.

Pick the setting your budget can afford, then spend your time on the creative, where the results come from.

*Draper Ads is free during beta. Connect your ad account, build the ad once, and launch it to every ad set in one go. No credit card, and [setup takes under two minutes](https://draperads.com/sign-up).*

<!-- editor-notes
Angle chosen: "It only matters for testing, and the switch condition is arithmetic" (counter-narrative to the endless CBO vs ABO debate): if/then rule first, then the hit-rate math.
Angles rejected: (1) "CBO vs ABO is a dead question" (one camp's view; would flatten the split). (2) "Always ABO for testing" (contradicts half the panel).
Split shown: three-way testing split (ABO for testing / one CBO or Advantage+ campaign / doesn't matter). Verdict: if/then rule (fund each concept to the read floor and winners cover losers → ABO; thin budget or low hit rate → CBO); scale on campaign budget either way. Sub-split on CBO minimums: a patch, never with cost caps.
Deliberately not used: the "nearly all use CBO at $1M+" line, which the brief shows is a transcription error (at that tier most testing campaigns reportedly use ABO). The article makes no claim about what large accounts use.
Claims to verify:
(a) Meta's current name: "Advantage campaign budget" for CBO; confirm in Meta Business Help Center.
(b) A cost cap overriding an ad-set minimum inside a campaign-budget campaign is a practitioner report; confirm in Meta docs.
(c) "With one ad set, the two settings behave the same": first-principles; confirm no delivery difference in Meta docs.
(d) 17+ clicks is the Draper site's figure for one ad built from scratch in one ad set; 272 assumes a full build per ad.
(e) Read floor (target CPA x 10) is our own arithmetic, shared with the hub post.
Open TKs: none.
Lint: 0 errors, 0 warnings. Sentence SD 8.4, one-sentence paragraphs 41%.
Self-score: intro 8/10, average section 7.5/10. No first-hand proof; carried on panel consensus and labelled arithmetic.
-->
