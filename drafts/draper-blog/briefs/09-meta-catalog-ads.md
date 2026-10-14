# Panel brief: Are catalog ads worth it, and how do I make them good?

```yaml
question: "Are catalog ads worth it, and how do I make them good?"
primary_keyword: "meta catalog ads"
secondary_keywords: ["catalog ads", "facebook catalog ads"]
search_intent: informational
size: medium
format: auto            # PLAN.md suggests G handbook
profile: draper-ads
experts_consulted: [barry-hott, dara-denney, phil-kiel, nick-theriot, alessio-cordeddu, ben-heath, marin-istvanic, lorenzo-pravata]
```

## 1. Coverage

| Corpus | Coverage | Main files |
|---|---|---|
| Dara | **Deep but mostly vendor-sourced.** Two long interviews with the founder of a catalog-ad vendor (2024-04, 2025-09) supply most numbers and tactics. Her own independent material: the separate-campaign rule and its reason, "launch a catalog campaign first" for multi-product brands, the SKU-level delivery mechanism, "not only for retargeting". Tier: recent (2025), not current. | `dara-denney/knowledge/frameworks/catalog-ads-playbook.md`, `themes/catalog-ads.md`; verify in `sources/youtube/BIVnOWcGnfA/transcript.md`, `sources/x/2024-Q1.md`, `2025-Q3.md` |
| Marin | **One worked audit case (2026-06), current.** Catalog headline ROAS as existing-customer harvest. | `marin-istvanic/knowledge/frameworks/account-audit-method.md §blended-vs-NC-ROAS`, `themes/attribution-and-measurement.md`, `evolution.md §1` |
| Phil | **Light, own data.** Collection ads for range brands, more catalog for high SKU counts, DPA "sometimes" its own ad set, DPA loses on net-new reach. | `phil-kiel/knowledge/frameworks/six-creative-formats.md §5`, `themes/static-ads-and-teardowns.md §Checklists`, `frameworks/bfcm-q4-q5-playbook.md` |
| Nick | **One setup rule.** Advantage+ Catalog Ads off unless hundreds of SKUs. | `nick-theriot/knowledge/frameworks/one-campaign-account-structure.md` step 3, `themes/platform-changes.md` |
| Barry | **One line.** DPA works for catalog-heavy, self-explanatory products; fails for products needing education. | `barry-hott/knowledge/themes/creative-and-hooks.md` (2024-12) |
| Alessio | **Only in a superseded structure.** A catalog-sales campaign at $1,000+/day "if SKU count supports it" (2024-12); his current two-campaign structure (2025-11) doesn't mention catalog. | `alessio-cordeddu/knowledge/themes/account-structure-and-scaling.md`, `evolution.md §1` |
| Lorenzo | **Vendor content only.** One 2025-09-30 thread promoting a catalog tool as a disclosed partner; never revisited. His index routes catalog to Dara. | `lorenzo-pravata/knowledge/evolution.md` "Gone quiet on"; `themes/ai-in-creative-production.md` (disclosures) |
| Ben | **Silent.** Says catalog audiences "aren't going to apply to like 90% of people watching"; no catalog mechanics in the corpus. | `ben-heath/knowledge/themes/campaign-structure.md`, `themes/targeting.md` |

**Sourcing warning.** `CONCEPTS.md paidsocial.catalog_ad` and Dara's knowledge files attribute some tactics to her that the transcript shows the vendor saying: "sale overlays are always a performance win… we have never seen that not lift performance… the brands on Marpipe do" (`MVg_o8WU6mo/transcript.md [47:55]`) and the 50 / 250 SKU thresholds (`[55:05]`). The "you should separate them" answer at `AS0YfAioHT0 [58:02]` is the vendor's too, but Dara gives the same rule independently in her own account-structure video (`BIVnOWcGnfA [6:05]`). All are treated below by who actually said them.

## 2. Consensus

- **SKU count decides whether catalog ads are worth it.** Range brands should run them; hero-product brands mostly shouldn't. Nick: off unless hundreds of SKUs (`nick-theriot/.../one-campaign-account-structure.md` step 3). Phil: range brands always have a collection ad live; high SKU count means more catalog ads (`phil-kiel/.../six-creative-formats.md §5`). Dara (own): "if you have multiple products… the first thing I would always do is launch a catalog ad campaign" (`BIVnOWcGnfA [6:05]`). Alessio's superseded structure gated it on SKU count too.
- **They suit self-explanatory products, not products that need education.** Barry: DPA fails where there's no room to explain why this one is different (`barry-hott/.../creative-and-hooks.md`). Marin's parallel rule for images: self-explanatory products (clothing, jewelry, toys) can prospect with images; problem-solving products need video to educate (`marin-istvanic/knowledge/evolution.md §10`). Lorenzo's statics ceiling (product needs >10 seconds to explain) points the same way (`lorenzo-pravata/.../ai-production-pipelines.md §Pipeline 1`).
- **Don't trust the catalog campaign's headline ROAS. Check who it reaches.** Marin: a 4.0-ROAS catalog campaign had 0.7 new-customer ROAS, with three quarters of spend on existing customers at frequency 15 (`marin-istvanic/.../account-audit-method.md`). Phil: DPA carousel reached a smaller share of net-new people than video (17% vs 27%) and lost the budget argument on that basis (`phil-kiel/.../six-creative-formats.md §5`). `CONCEPTS.md` flags that this is a measurement warning, not a verdict on catalog ads.
- **Keep catalog delivery from swallowing the account's budget.** Dara (own): catalog in its own campaign "because sometimes the spend will actually go all towards the catalog ads" (`BIVnOWcGnfA [6:05]`). Marin's case is the same symptom from the measurement side: the catalog campaign "was getting the most budget". Phil: DPA "sometimes" warrants its own ad set (`six-creative-formats.md §5`).
- **Audit Meta's automated defaults on catalog and image ads.** Ben: on Creative Enhancements "you very much need to be the filter" (`ben-heath/.../creative-and-hooks.md §Creative Enhancements`). Marin treats every Meta default as opt-out and audits for silent changes (`marin-istvanic/.../platform-mechanics-and-andromeda.md`). (The specific catalog example, AI backgrounds switched on by default, is vendor-sourced: see section 7.)

## 3. Splits

**Split 1. Are catalog ads a prospecting tool or a harvesting tool?**
- **Camp A (prospecting):** Dara: "If you think catalog ads are only for retargeting, you're ngmi" (`dara-denney/sources/x/2025-Q3.md`); the SKU-level matching mechanism finds new shoppers with matching intent (`themes/catalog-ads.md §principle`); a 2024 brand she reviewed dropped creative testing for a catalog-only ASC because it outperformed everything (`sources/x/2024-Q1.md`). Wins for wide-range catalogs with clean feeds where existing customers are capped or excluded.
- **Camp B (harvest unless proven otherwise):** Marin: the catalog campaign is the one most likely to be existing-customer harvest; he cut its budget 70% into prospecting, dashboard ROAS fell, revenue held, new customers rose (`account-audit-method.md`). Phil: lower net-new reach than video (`six-creative-formats.md §5`). Wins wherever reporting is platform ROAS and nobody has split the audience segments.
- **What it's about:** measurement, not taste. `CONCEPTS.md` calls it "a difference of question, not of fact": one camp asks how to build them, the other whether the reported number is real.
- **Suggested verdict:** run catalog ads if you have the range, but judge them on new-customer share and new-customer ROAS from the audience-segment breakdown. If most spend lands on existing customers, cap it or cut it; don't let the headline ROAS win budget on its own.

**Split 2. Separate catalog campaign, or inside the main campaign?**
- **Camp A (separate):** Dara: three campaigns for multi-product brands (testing, scaling, catalog-only Advantage+), because catalog absorbs the spend if merged; she notes this contradicts Meta's guidance (`BIVnOWcGnfA [6:05]`; `themes/catalog-ads.md`). Phil: "Yep sometimes" its own ad set.
- **Camp B (inside the one structure, toggle on or off):** Nick runs one CBO per objective and treats catalog as a campaign-level toggle, off unless hundreds of SKUs (`one-campaign-account-structure.md`). Alessio's current two-campaign structure (2025-11) adds campaigns only for a different offer, country, cost-cap test or audience; catalog isn't listed (`account-structure-and-scaling.md`). Marin runs 1 ABO + 1 ASC "that's it"; his 2023 retargeting campaign with DPA is retired (`evolution.md §1`).
- **What it's about:** budget control vs consolidation. The separate campaign exists to stop catalog eating the budget, which is Marin's audit finding too.
- **Suggested verdict:** if catalog is material to the account (wide range, real spend), separate it so you can see and cap its budget and new-customer share. If it's a small add-on for a modest range, leave it off or as the platform toggle until it proves it reaches new people.

**Split 3. Is high frequency on catalog ads a fatigue problem?**
- **Vendor position (relayed by Dara):** no, each impression can show a different product (`themes/catalog-ads.md §three myths`). Guest claim: not usable alone.
- **Marin:** frequency 15 on a catalog campaign was the tell that it was serving existing customers, not acquiring (`account-audit-method.md`).
- **Suggested verdict:** for catalog ads, frequency isn't the fatigue signal on its own. The question is who it's reaching: high frequency on existing buyers means harvest. Read frequency together with the audience-segment split.

## 4. Single-source insights
- Delivery works at SKU level (size, colour, price, stock), not creative level, which is why catalog behaves differently from image/video ads. Dara's own framing since 2024 (`sources/x/2024-Q1.md`, `2024-Q2.md`); her 2024 "third type of targeting" label has faded. Usable as mechanism, verify against Meta docs.
- A multi-product brand shouldn't advertise every product: find the most scalable product, bundle or offer for Meta and push resources there; catalog covers the long tail. Dara (`BIVnOWcGnfA [6:05]`).
- Value-based bidding with per-ad-set ROAS goals stops a wide-price catalog over-concentrating on the cheapest SKU. From a brand case in Dara's corpus (Pact, 2026-04): reasoning stands on first principles, the brand can't be named.
- Carousel quality bar: product, macro/detail and lifestyle images; sharpness and contrast; product name plus a plain-language explainer term. Phil (`static-ads-and-teardowns.md §Checklists`, 2024-09).
- Apparel model grid cropped 1:1 with the Collection format applied for shoppability; founder letter plus collection format for a promo. Phil (2024-11, 2025-08).
- Make catalog the long-tail and liquidation channel; hero creative talks about best-sellers. Vendor said it; plausible on first principles only.

## 5. Numbers
- **SKU gate:** "hundreds of SKUs" (Nick, current). The vendor's 50 / 250 thresholds are guest claims and stay out.
- **Measurement case:** 4.0 platform ROAS vs 0.7 new-customer ROAS; $3,000 of $4,000 weekly spend to existing customers; frequency 15; budget cut 70% (Marin, 2026-06; one account, use the shape, not the figures, or present as a single anonymized example).
- **Net-new reach:** DPA carousel ~17% net-new vs video ~27% over one week (Phil, 2025-12; one account).
- **Structure:** 3 campaigns for a catalog brand (Dara) vs 1-2 campaigns with catalog as a toggle (Nick, Alessio current, Marin).
- No independent corpus supplies a catalog share-of-spend, ROAS-uplift or CTR-uplift figure. All of those are vendor numbers (section 7).

## 6. Myths and retired advice
- "Catalog ads are only for retargeting." Dara, own post (2025-Q3); the original DPA era was retargeting, hence the myth. Caveat from Split 1: in practice they often do drift to existing customers, so measure it.
- A dedicated retargeting campaign "(regular + DPA)" (Marin, 2023): retired by his 2025-26 two-campaign structure.
- A catalog-sales campaign as a fixed tier at $1,000+/day (Alessio, 2024-12): superseded by his 2025-11 structure.
- "DPA as a third audience" (Dara, 2024): label faded; the mechanism claim stands.
- "Catalog headline ROAS proves it's the money machine": the panel's strongest warning (Marin 2026-06; Phil's net-new data).

## 7. Do not use in the article
- Any expert name, handle, quote or link (see `PLAN.md` forbid list, which includes Marpipe, Pantelo and Varos).
- **Vendor claims relayed in Dara's catalog videos (Marpipe founder as guest), with no independent support in another corpus:**
  - 60%+ / 68% of e-commerce ad spend on catalog; 40% of Meta's global ad revenue; ~95% of catalog ads are plain product-on-white; ~70% of Lululemon spend; vendor's tracked spend $300-350K/day → $750K/day.
  - Varos/Marpipe study: ROAS 78.3% higher, CTR 36% higher than image/video (3,500 accounts, $4B).
  - Sale/discount overlays "always a performance win" / "never seen it fail" / "lowest hanging fruit" (vendor's words, misattributed to Dara in her KB).
  - 50 / 250 SKU thresholds (vendor's words); Pinterest 50 / 100 thresholds.
  - Templates: "200 products + 1 template ≈ 400 ads", "start with 5-6 templates".
  - Product-level video "a slam dunk usually every time"; Lorenzo's partner thread "Video DPA crushing regular ads", "6.86 vs 4.0 ROAS" (disclosed partner, not independent).
  - The three myths list as stated (ugly / retargeting-only / frequency fine); "amazing for brand awareness".
  - Meta AI backgrounds "couch floating on a beach" anecdote; Shopify native integration "a disappointment".
  - Cross-platform expansion claims: Pinterest "set and forget", Reddit and Snap catalog overhauls, CTV Universal Ads at ~$5K/week, "transfers cleanly cross-platform", "every gen-AI ad will be catalog powered".
- Brand cases: Cozy Earth (30 treatments, +220% spend, +60% ROAS), eBay/Poshmark/Walmart "doing it wrong", Wayfair/On/Quince "doing it right", Ridge/Simple Modern/Hexclad, Pact (500 SKUs, $15 vs $150, 50K customers), Reformation, Lululemon, Raymour & Flanigan, Kizik.
- Meta's own alpha stats quoted second-hand (omnichannel ads "41% better with catalog ads") unless taken from Meta's documentation directly.
- Coined labels: "competitor hack", "cashier pretending to be a salesperson", "money machine", "raw vs enriched" as a branded framework (describing the difference is fine).

## 8. Draper angle
- Weak fit; the PLAN row leaves it blank. Catalog ads are assembled from a feed, so they don't create a per-ad upload burden the way statics or video variants do. Don't force a volume pitch here.
- Honest touchpoint: the non-catalog side of the account. Catalog covers the long tail; best-sellers and offers still need hand-made creative, and the panel wants those tested in volume. "Create once, deploy many", automatic naming and Google Drive import apply to that creative, not to the catalog feed.
- Don't claim Draper builds catalog ads, manages feeds or templates, or improves catalog ROAS. None of that is in `profiles/draper-ads.md`.
- Best placement: one inline mention plus the standard end CTA, or let the article stand without an inline mention.

## 9. Open questions
- Meta's current product naming (Advantage+ catalog ads) and whether catalog runs inside Advantage+ sales campaigns by default; Meta's own guidance on separate vs combined (Dara says it contradicts Meta's).
- The existing-customer budget cap in Advantage+ campaigns: current name, default and where it lives (Marin's related ASC case found a 25% cap left on).
- Whether catalog creative templates/overlays, product-level video and adaptive placements for catalog are native Meta features now (cite exact Meta URLs only).
- Advantage+ creative enhancements for catalog (AI-generated backgrounds): current default and how to turn it off.
- Other platforms: Pinterest, Snap, Reddit, TikTok and Threads catalog formats. The panel only offers vendor claims; anything in the article needs each platform's own docs, or should be left as a short "your feed is portable" note.
- `[TK]` candidate: an audience-segment split (new vs existing) for one real catalog campaign, from Wonderland or a Draper user, to show the measurement check.
