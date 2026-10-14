# Panel brief: CBO or ABO, especially for testing?

```yaml
question: "CBO or ABO, especially for testing?"
primary_keyword: "campaign budget vs ad set budget"
secondary_keywords: []
search_intent: informational
size: short
format: E explainer
profile: draper-ads
experts_consulted: [barry-hott, dara-denney, phil-kiel, nick-theriot, alessio-cordeddu, ben-heath, marin-istvanic, lorenzo-pravata]
```

Paths are relative to `/home/user/aimarketingschool/experts/`. "K/" = `knowledge/`. Meta's current name for CBO is Advantage campaign budget (CONCEPTS `paidsocial.cbo`).

## 1. Coverage

All eight have a position, at different depths.
- **Full:** Marin (`marin-istvanic/K/frameworks/abo-testing-to-scaling-pipeline.md §1`, `K/themes/campaign-structure-and-simplicity.md`), Nick (`nick-theriot/K/frameworks/one-campaign-account-structure.md`, `K/evolution.md §1`), Alessio (`alessio-cordeddu/K/frameworks/creative-testing-protocol.md §1`), Ben (`ben-heath/K/themes/campaign-structure.md §CBO vs ABO is a dead question`), Phil (`phil-kiel/K/evolution.md §2, §4`, `K/themes/testing-and-iteration.md §Unresolved`).
- **Partial, with transcript caveat:** Dara (`dara-denney/K/frameworks/creative-testing-protocol.md §Testing structure by budget tier`). See the verification note below.
- **Thin:** Barry (a four-week-old CBO lean, `barry-hott/K/evolution.md §4`), Lorenzo (one 2026-08 article, `lorenzo-pravata/K/themes/testing-win-rate-and-account-discipline.md §Media buying and account structure`).

**Dara transcript verification (the ABO word is dropped in her auto-transcripts):**
- 2025-03-28 "Test at Every Budget" (`dara-denney/sources/youtube/7knQyPYLmfo/transcript.md` [8:07]): "whether or not you should use [—] or CBO is really a media buyer decision. I personally generally use [—] so that I can get a quick read… by throttling that spend… but I know many brands that use CBO here really successfully." The dropped word is ABO by context (contrasted with CBO; throttling per ad set). The knowledge file's reading is correct.
- Same video [12:12], Scale tier ($1M+/mo): "nearly all brands are using [—]… I would still consider this a media buyer choice because I've seen a select few ad accounts recently that were successfully using CBO at scale like this, it's just not something that I see that often." The dropped word must be **ABO**: she contrasts it with the "select few" on CBO. **The knowledge file's "Nearly all use CBO" (`creative-testing-protocol.md` line 143) is a transcription error.** At the scale tier she reports that most testing campaigns use ABO.
- 2024-02-21 (`CmkWzdgl6iI/transcript.md` [6:07]): "should you use [—] or should you use CBO, this is honestly a media buyer's dealer's choice… if you're using CBO you really need to make sure that you are adding ad set minimums and maximums… I personally use [—] because… I am manually increasing and decreasing the budgets… old school media buyer." Confirms the ABO reading; X corroboration 2024-02-21: "Many brands use ABO, but CBO works just as well" (`sources/x/2024-Q1.md`).
- 2025-08-11 short (`PVoC7H44A5w/transcript.md`): for $5K-30K/month, "one campaign… a campaign budget optimization campaign, which means that it's going to have advantage plus turned on." Explicit CBO at small budgets; no dropped word.
- 2026-03-27 X: "and then we start arguing about cbo vs abo again." No position.

## 2. Consensus

1. **Fewer campaigns.** Every corpus has moved toward one to three campaigns: Nick (one CBO per business objective), Ben (two), Alessio (two), Marin (two), Phil ("ABO, ASC or CBO is all you need", ~90% of accounts fit ABO+ASC, `evolution.md §2`), Lorenzo ("you don't need more than 2", 2024; one CBO per product, 2026), Barry (consolidate, `account-structure-and-media-buying.md §Structure`), Dara (two campaigns, `K/themes/account-structure-and-scaling.md §Current tactic`).
2. **The budget setting matters less than offer and creative.** Nick (structure ~5% of performance, CONCEPTS `paidsocial.cbo`), Marin ("account prefers good ads", `abo-testing-to-scaling-pipeline.md §1`), Phil ("cost caps won't fix poor creative strategy"; "don't believe the preachers"), Ben (asked more about structure than offers and creative combined, "least deserved"), Dara ("a media buyer decision").
3. **With one ad set in a campaign, the question disappears.** Ben states it directly (`campaign-structure.md`). Scaling campaigns are single-ad-set in Alessio (CBO, 20-40 winners), Dara (one ad set of winners), Phil ("single ad set per campaign, start here", 2026-04).
4. **Scale on campaign-level budget.** Alessio (CBO scaling), Marin (Advantage+ with cost cap), Nick (CBO), Phil (CBO per product or offer), Dara (Advantage+ scaling campaign), Lorenzo (CBO per product). Nobody argues for ABO as the scaling default (Marin's twist: winners also keep scaling inside the ABO testing ad set).
5. **Under campaign budget, new ads struggle to get spend next to proven ones.** Marin (CBO picks on early engagement, starving new concepts), Ben (Meta "won't put any budget on the new stuff", `scaling-testing-campaign-structure.md §The problem`), Alessio (fair shot needs fixed budgets), Dara 2024 (CBO needs ad-set minimums). Counterpoint: Barry posted an account showing CBO spreading spend across many ads (2026-07-14); Nick and Phil read non-spend as Meta's verdict on the ad.

## 3. Splits

### The question: for **testing**, ad set budget or campaign budget?

- **Camp A, ad set budget for testing:** Marin: "not a preference thing, but a math thing". Use ABO when hit rate is high enough because winners pay for losers; switch to CBO "if your hit rate is lower or budget is low compared to creatives you want to test" (rule of thumb: 10 tests a week with 1 winner → CBO) (`abo-testing-to-scaling-pipeline.md §1`). Alessio: ABO with equal budgets so outcomes aren't an artefact of allocation; CBO is unstable at small spend (`creative-testing-protocol.md §1`). Dara personally, for a fast read by throttling spend (2024, 2025; transcript-verified above), and most $1M+/mo testing campaigns she sees. Phil's 2026-04 folder tree: "Separate ABO for testing only". **Wins when** budget covers every concept ad set at a readable daily amount, conversion volume is healthy, and the team will make manual budget calls on a schedule.
- **Camp B, campaign budget (no separate ABO test):** Nick: one CBO, a new ad set per idea; abandoned ABO testing in 2022 because winners found at $20-30/day "died" in a $2-3K/day CBO (`evolution.md §1`); a 2026-01-30 post restating ABO-test/CBO-scale is a holdover. Lorenzo, 2026-08: "No ABOs. With an ABO you are the one deciding where budget goes", hedged ("plenty of brands scale on other ones"). Barry, 2026-07: "mostly a CBO maxi now", hedged five days later ("I use CBO with a decent amount of caution and control"). Dara for $5-30K/mo: one CBO/Advantage+ campaign. **Wins when** budget is small relative to the number of creatives, hit rate is low, or nobody will manage budgets daily.
- **Camp C, it doesn't matter (or it changes month to month):** Ben: with one ad set per campaign it makes no difference; exception, multiple ad sets split by location → ABO. Phil: public CBO↔ABO whipsaw July-August 2026, resolved as "some accounts are ripping on CBO… don't believe the preachers" (`evolution.md §4`). Never quote Phil for either side.
- **What the split is really about:** budget per concept and hit rate. ABO buys fairness and a fast read but spends on losers; CBO saves money on losers but can starve new ideas. Marin's version is the only one that states the switch condition.
- **Suggested verdict:** an if/then rule. *If* you can fund each new concept at roughly your fair-shot floor per day and your tests hit often enough that winners cover losers, test in ABO. *If* budget is thin for the number of creatives, or most tests fail, test inside one CBO/Advantage+ campaign and accept less control. Scale on campaign budget either way.

### Sub-split: minimum spend per ad set inside CBO
Dara 2024: add ad-set minimums and maximums if testing in CBO. Phil: recommended % minimums (2025-11-03), then reversed within six weeks: "No minimum budgets per ad set… stop fighting it with artificial floors" (2025-12-11). Marin: CBO with min-spend is his low-hit-rate fallback, but min-spend plus a cost cap doesn't work (the cap overrides the minimum), and different bid caps per ad set send budget to the highest cap. Nick: at most a $5-10/day minimum on a non-spending ad set, "if it still doesn't spend, it's probably trash". **Verdict:** minimums are a patch for testing inside CBO, not a default; never combine them with cost caps.

## 4. Single-source insights
- The ABO-test winner that dies in CBO (Nick): a cheap ad set reaches demand already warmed by the account's other ads. Plausible; present as "some practitioners found".
- A winner can keep working in the testing ad set while failing as a copy in the scaling CBO; keep both (Alessio). Also the logic of Marin's "the testing campaign is the scaling campaign".
- Separate campaigns can be justified by different attribution settings (cost cap campaign on click-only, the rest on 7-day click/1-day view) (Marin).
- A separate testing campaign needs ~50 conversions a week on the optimised event; below that, put new ads into the existing ad set or use Meta's creative test tool (Ben, `scaling-testing-campaign-structure.md §Choosing how to test`).

## 5. Numbers
- **Test ad set daily budget under ABO:** $50-500, mostly $100-200 (Marin 2026-06); $100-200 (Dara, ~$1K/day accounts, 2025-03).
- **Testing vs scaling budget:** ~20:80 (Alessio; Ben's normal dial, raise testing share when results are poor). At $1K/day: 100% Advantage+, or 60/40 Advantage+/ABO (Phil 2025-11).
- **Switch to CBO:** ~10% hit rate, e.g. 1 winner in 10 weekly tests (Marin 2026-01).
- **Separate testing campaign gate:** ~50 conversions/week (Ben 2026-01).
- **Spend tiers:** CBO/Advantage+ only for $5-30K/mo (Dara 2025-08); two campaigns from ~$1K/day (Dara 2025-03).

## 6. Myths and retired advice
- **"Use ABO to test, then move winners to CBO and turn off the original."** Every corpus that moves winners copies them and leaves the original running (Marin, Alessio); Phil and Nick don't move them at all.
- **"Set ad-set minimums in CBO."** Phil reversed it (2025-12).
- **"Separate TOF/MOF/BOF or retargeting campaigns, each with its own budget."** Retired by Marin (2025-09), Nick, Ben (hybrid ad sets).
- **"CBO dumps everything into one or two ads, so it can't test."** Contested: Barry's 2026-07 counter-evidence; Marin says it starves new concepts, not that it can't spread. Present as contested, not as a myth.
- **"Turn off Advantage campaign budget for Dynamic Creative structures."** Ben's 2023 structure, now obsolete.
- **"Consolidation is bad for scaling."** Marin's 2023 position, superseded (2025-04).

## 7. Do not use in the article
- Names, handles, quotes, links; Dara's business partner and his "one campaign method".
- Coined names: "the ABO Scaling guy", "CBO maxi", "ABO gurus", "one-CBO-per-objective doctrine", "folder tree", "Manual Bids, Decoded", "all-funnel campaign".
- Case data: Nick's consolidation CPA results and the $20-30/day vs $2-3K/day anecdote numbers, Phil's CPMr/Reach results from the single-CBO funnel test, Marin's managed-spend figures.
- Do not cite Dara's knowledge file "Nearly all use CBO" at scale: it contradicts the transcript (section 1).

## 8. Draper angle
Testing structure decides how many ad sets you launch into: ABO testing means a new ad set per concept every week, each needing the same ads, names and UTMs. With a copy-don't-move rule, winners are also deployed into a second campaign. That's the "create once, deploy to many ad sets" job; use the 17+ clicks per ad built from scratch (state the rebuild assumption). Worked hypothetical: 4 concepts × 4 variants = 16 ads/week, plus winners copied into scaling. No performance claims for Draper.

## 9. Open questions
- Meta docs: Advantage campaign budget naming and ad set spending limits (min/max) inside it; whether a cost cap overrides an ad-set minimum; whether ABO is still selectable on Advantage+ sales campaigns; daily overspend allowance.
- Does copying a winner by post ID into a CBO keep its social proof? Practitioners say yes; confirm against Meta docs.
- No corpus shows controlled data comparing ABO vs CBO testing hit rates; anything beyond the if/then rule is `[TK]`.
