# Draper Ads blog: 12 articles answering the questions Meta advertisers ask

**Angle:** Meta advertisers get their questions answered by Draper.

**Method (panel mode):**
- **Question:** the questions come from what Dara Denney's audience asks most.
- **Answer:** the answers come from the **collective** knowledge of the eight paid-social experts in `michaelwonderland/aimarketingschool`. Where they agree, that's stated as industry knowledge. Where they disagree, both sides are shown, with when each wins.
- **No names:** no individual is named, quoted or linked in the articles.
- **Targeting:** every article targets a keyword with 10+ US monthly searches (DataForSEO, October 2026).

**Profile:** `draper-ads` (en-US). **Voice:** wonderblogwriter house voice (Julian Shapiro + Nat Eliason, Michael light).

## The formula

1. **Question.** A real practitioner question, matched to a validated keyword.
2. **Panel brief** (`briefs/NN-slug.md`). All eight paid-social corpora are read for that question:
   - consensus, splits (with the conditions where each side wins), number ranges, retired myths and single-source ideas;
   - names and sources stay in the brief, for verification only.
3. **Article** (`NN-slug.md`). The house voice is layered on the panel brief:
   - consensus is the backbone;
   - splits are shown without names, followed by "our take";
   - Draper's angle comes where the answer touches launching volume.
4. **Quality gates:**
   - `lint.py --forbid "$(cat forbid.txt)"`: zero errors, which means no expert names or handles;
   - an editor pass.

## How the questions were found

1. **Her videos.** All 303 of Dara's indexed videos, ranked by views. The most-watched ones cluster on creative testing, hooks, ad formats, account structure, Andromeda, AI creative and catalog ads.
2. **Her knowledge base.** The 16 frameworks and 11 themes in the knowledge base, each read for the questions it answers.
3. **Candidate searches.** 147 searches an advertiser might type, checked for US search volume (Google Ads data).
4. **Real phrasings.** DataForSEO keyword suggestions on 18 seed topics: 1,411 keywords, 1,027 of them about paid social, filtered to 10+ searches.
5. **Top SERPs.** The top 10 results checked for each finalist. Most are Reddit threads, YouTube videos and thin agency posts: beatable.

## The cluster

| # | Size | Primary keyword (US/mo) | Secondary | Format | Dara's question | Draper angle |
|---|---|---|---|---|---|---|
| 1 | Short | what is a good hook rate (20) | hook rate formula (30), what is hook rate (170) | E explainer | What hook rate should I aim for, and what does it tell me? | Hook variants are cheap to make and slow to launch |
| 2 | Short | ad set name example (50) | facebook ads naming convention (10) | C catalogue | How do I name ads so I can analyze creative? | Draper names every ad from its creative file automatically |
| 3 | Short | whitelisting vs partnership ads (20) | partnership ads (260) | E explainer | Whitelisting or partnership ads? | Creator content multiplies the ads you need to launch |
| 4 | Short | campaign budget vs ad set budget (30) | | E explainer | CBO or ABO, especially for testing? | Testing structure decides how many ad sets you launch into |
| 5 | Short | what is ad fatigue (70) | facebook ad fatigue (140) | E explainer | Is my ad fatigued, and what do I do? | The fix is new concepts, shipped fast |
| 6 | Medium | meta andromeda update (390) | meta andromeda creative diversity (20) | F essay / E | What did Andromeda change, and what do I do about it? | Diversity means volume, and volume means launching |
| 7 | Medium | testimonial ads examples (880) | testimonial facebook ads (50) | C catalogue | What makes a testimonial ad convert? | |
| 8 | Medium | static ads examples (210) | what are static ads (70) | C catalogue | What static ads work on Meta now? | Statics are the fastest format to make in volume |
| 9 | Medium | meta catalog ads (170) | catalog ads (170) | G handbook | Are catalog ads worth it, and how do I make them good? | |
| 10 | Medium | what are ugc ads (210) | ugc ads examples (70) | G handbook | What are UGC ads, and what makes them work? | |
| 11 | Long | facebook ads testing (50) | testing ads on facebook (50), meta creative testing (30), how many ads per ad set (10) | G handbook (pillar) | How do I test creative on Meta at my budget? | The test only works if you can launch 10 to 25 ads per test |
| 12 | Long | ai for facebook ads (260) | ai facebook ads (260), meta ai ads (390) | G handbook | How do I use AI across the creative workflow? | AI makes creative cheap; launching becomes the bottleneck |

Cross-links: 11 is the hub for 1, 4, 5 and 6. 12 links to 8 and 10. Each post links 2 to 3 siblings by slug (see the file names below).

## Rules for every post

- **No individual experts.** No names, handles, quotes or links to their content. Coined framework names that belong to one person are described instead of named. No brand stats, pay rates or results that only one expert relayed. No guests from their videos.
- **Primary sources are fine.** Meta's own documentation can be cited and linked, but only exact URLs, never guessed ones.
- **Draper claims:** only those in `profiles/draper-ads.md`. Partnership ads are **not** a launched Draper feature.
- **No invented first-hand data.** Use worked arithmetic with labelled hypothetical inputs. At most one `[TK]` where first-hand proof matters most.
- **Retired tactics** only ever appear as myths to stop.

## Status: 12 articles drafted in panel mode (October 2026)

| # | Article | Words | Our concept | Open TK |
|---|---|---|---|---|
| 01 | What is a good hook rate | 947 | the empty hook | hook-rate averages by format from one account |
| 02 | Ad set name examples | 944 | question-first naming | Draper screenshot: file name → ad name |
| 03 | Whitelisting vs partnership ads | 950 | byline diversity | how many ads one creator batch became |
| 04 | Campaign budget vs ad set budget | 947 | (reuses the read floor) | none |
| 05 | What is ad fatigue | 937 | false fatigue | one fading winner walked through the 6 steps |
| 06 | Meta Andromeda update | 1,695 | the same-person test | clicks to duplicate an ad into another ad set |
| 07 | Testimonial ads examples | 1,743 | the found line | spend share of single-customer testimonial ads |
| 08 | Static ads examples | 1,748 | the cosmetic variant | distinct vs cosmetic static batch, with launch time |
| 09 | Meta catalog ads | 1,521 | harvest share | new vs existing split from one catalog campaign |
| 10 | What are UGC ads | 1,694 | template UGC | none |
| 11 | Facebook ads testing (hub) | 3,159 | the read floor | weekly batch launch time, manual vs Draper |
| 12 | AI for Facebook ads | 3,052 | the judgment bottleneck | none |

**Before publishing:**
1. Fill the TKs with first-hand data from Draper or Wonderland, or cut those lines.
2. Check each post's "Claims to verify" (in its editor notes) against Meta's documentation.
3. Add Meta doc links where exact URLs are confirmed.
