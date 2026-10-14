---
title: "What Is a Good Hook Rate? Formula, Ranges, and the Trap"
meta_description: "A good hook rate depends on your account: DTC video often lands at 25% to 45%, lead gen far lower. The formula, the ranges, and when a high one is bad news."
slug: what-is-a-good-hook-rate
primary_keyword: what is a good hook rate
secondary_keywords: [hook rate formula, what is hook rate]
locale: en-US
profile: draper-ads
format: E-explainer
byline: Draper Ads
word_count: 947
---

# What Is a Good Hook Rate?

**Hook rate is a video metric: the share of impressions where someone watched at least three seconds of your ad.** The hook rate formula is 3-second video plays ÷ impressions × 100. Statics don't have one.

So what is a good hook rate? There's no universal number. For DTC video, experienced Meta buyers commonly report 25% to 30% as the low end and 35% to 45% as strong, while lead gen and B2B accounts often run under 10% and stay healthy. The bar that holds is your own account average, read next to hold rate and cost per acquisition (CPA).

And a high hook rate can be bad news.

## What is hook rate, exactly?

Hook rate is a custom metric. Ads Manager doesn't ship it as a column, so you build it from two columns it does have: 3-second video plays and impressions.

Say a video gets 40,000 impressions and 12,000 three-second plays. That's a 30% hook rate. Seven in ten people shown the ad scrolled past before second three.

**It answers one narrow question: did the opening stop people?**

Check the denominator before comparing. Some tools divide by reach or by plays instead of impressions, and some call the same idea "thumb-stop rate."

Two 30% figures from two formulas aren't the same 30%.

## What is a good hook rate for your account?

Practitioners agree on the formula and disagree on the number:

| Account type | What practitioners commonly report |
|---|---|
| DTC video | 25% to 30% low end, 35% to 45% strong |
| Lead gen and B2B | Often under 10%, and still healthy |

The formulas match, so the spread comes from offer, format, placements, and audience. That's the best argument against universal benchmarks.

Pull your own baseline instead, from every video that spent past a set floor in the last 60 to 90 days, split by format. [TK: anonymized account averages by format from one Wonderland account]. Read any single ad against that line once it has a few thousand impressions.

Below that, it's noise.

## Is a high hook rate good?

Experienced buyers split on this.

One camp treats hook rate as an early signal with a bar to clear; a high number means the opening found the right people, so make more like it. That camp wins when you're iterating openings on a concept that already converts and need a read before CPA data arrives.

The other camp won't decide anything on it, because a shocking opener can buy a sky-high hook rate from people who will never buy. It wins when the account has enough purchases to judge on cost directly.

**Our take: hook rate is a diagnostic, never a target.** The second camp has spotted a real failure, and it deserves a name.

**An empty hook is an opening that stops plenty of people, but not the people who buy.** Hook rate climbs, CPA climbs with it, and the hook-rate column calls it a win. It's worse than a weak hook, because the opening also shapes whom Meta delivers to.

Reward an empty hook and delivery drifts toward people who enjoy being stopped.

So read hook rate paired with CPA:

- **High hook, CPA on target:** the hook works. Make more openings in that direction.
- **High hook, CPA off target:** an empty hook, or a body that breaks the promise. Check hold rate to see which, then rewrite the opening in the buyer's own words so the wrong people scroll on.
- **Low hook, CPA excellent:** your best candidate for new openings.
- **Low hook, CPA off target:** the concept isn't landing. Start again.

## Hold rate: check the denominator first

Hold rate tells you whether the middle of the ad keeps the people the hook stopped. Practitioners compute it two ways:

- **Per impression:** 15-second plays (or ThruPlays) ÷ impressions. Buyers using this version commonly land around 7% to 15%.
- **Per hooked viewer:** 15-second plays ÷ 3-second plays.

Take that 40,000-impression ad again. With 3,600 fifteen-second plays, its hold rate is 9% on the first formula and 30% on the second.

Pick one, label the column, and never judge it against a benchmark built the other way.

## What to stop doing

- **Chasing the highest hook rate you can get.** That's how empty hooks get scaled.
- **Pausing a good-CPA ad over a low hook rate.** Give it new openings. Some practitioners treat a lot of [ad fatigue](/blog/what-is-ad-fatigue) as a tired opening.

## New hooks are cheap to make and slow to launch

Almost every reading above ends in new openings. One body, five first-three-seconds, each aimed at a different buyer or problem, because five rewordings of one line tend to get treated as one ad.

In Ads Manager, building one ad from scratch in one ad set takes 17+ clicks. Five openings across three ad sets is 15 ads, or about 255 clicks if you rebuild each one. And unless each ad's name carries its hook, the column is unreadable a month later (our [ad set name examples](/blog/ad-set-name-examples) fix that, and our [Facebook ads testing](/blog/facebook-ads-testing) guide covers how many to launch).

Draper Ads was built inside a paid social agency, by the media buyers doing those uploads. It pulls each hook file from Google Drive, names every ad from its file, and launches the batch to every ad set at once.

Hook rate tells you where to look. CPA tells you whether you found anything.

_Draper Ads is free during beta. Connect your ad account, build the ad once, and launch it to every ad set in one go. No credit card, and setup takes under two minutes. [Get your time back from manual ad work](https://draperads.com/sign-up)._

<!-- editor-notes
Angle chosen: "A high hook rate can be bad news" (counter-narrative), carried by the named concept "empty hook" (a high hook rate from the wrong people is a failure).
Angles rejected: (1) "There is no good hook rate, only your average" (true but flat as a lead; kept as the answer). (2) "Hook rate vs hold rate: the denominator trap" (too narrow for the head term; kept as one section).
Splits shown and verdicts:
- Is a high hook rate good? Signal-with-a-bar camp vs won't-use-it camp. Verdict: diagnostic, never a target; read paired with CPA via four if/then rules.
- What range is good? DTC 25-45% vs lead gen/B2B under 10%. Verdict: the spread proves the number is account-relative; set the bar from your own average.
- Hold-rate denominator: per impression vs per 3-second viewer. Verdict: pick one, label it, never compare across formulas.
Open TKs: 1. [TK: anonymized account averages by format from one Wonderland account].
Claims to verify:
- Meta's definition of "3-second video plays" (counts autoplay; for videos shorter than 3 seconds, Meta counts plays at ~97% of length) and of ThruPlay (15 seconds or completion if shorter). No URL cited; add Meta Business Help Center links if found.
- That hook rate is not a native Ads Manager column (true as of the brief; Meta adds columns occasionally).
- "Meta tends to treat near-identical ads as one" is phrased as practitioner observation, not documented mechanics (see /blog/meta-andromeda-update).
- The delivery-feedback mechanism (the opening shapes whom Meta keeps delivering to) is practitioner reasoning, not Meta documentation.
Draper claims used: 17+ clicks per ad built from scratch in one ad set (rebuild assumption stated), automatic naming from creative file, Google Drive pull, create once deploy many, origin credential, beta CTA.
Lacks first-hand proof: yes; carried on panel consensus and labelled hypothetical arithmetic.
Lint: 0 errors, 1 warnings (open-TK warning kept deliberately: one TK for first-hand account averages)
Self-score: intro 8/10, average section 7.5/10
-->
