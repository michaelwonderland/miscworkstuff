# Panel brief: What hook rate should I aim for, and what does it tell me?

```yaml
question: "What hook rate should I aim for, and what does it tell me?"
primary_keyword: "what is a good hook rate"
secondary_keywords: ["hook rate formula", "what is hook rate"]
search_intent: informational
size: short
format: auto          # PLAN suggests E explainer
profile: draper-ads
experts_consulted: [barry-hott, dara-denney, phil-kiel, nick-theriot, alessio-cordeddu, ben-heath, marin-istvanic, lorenzo-pravata]
```

Routing note: "hooks" spans several corpora. This brief is about the **metric** (hook rate on a video ad), not hook-writing craft and not organic post openers. CONCEPTS.md `metric.hook_rate` records six uses that "do not reduce to one instruction", and declines to pick a canonical formula because the denominator is not standardised. That is the frame for the whole article.

## 1. Coverage

| Expert | Coverage | Where |
|---|---|---|
| Dara | Full: definition, formula, hold rate, read points, diagnostic matrix, "never decide on it" | `dara-denney/knowledge/themes/hooks.md §Measuring hooks`; `frameworks/hook-taxonomy.md §Step 2`; `frameworks/two-question-analysis.md §The metric split, §Her custom metrics` |
| Alessio | Full: custom columns, 2024 benchmark table, winning threshold (unstable), soft vs hard metrics, retention bands | `alessio-cordeddu/knowledge/themes/creative-testing.md §Which metrics he trusts, §The 2024 benchmark table`; `evolution.md` (numbers table, "Winning hook rate") |
| Lorenzo | Full: formula incl. hold-rate variant, moving self-reported target, qualified-hook-rate correction, hook+hold diagnostic | `lorenzo-pravata/knowledge/themes/hooks-and-qualified-attention.md` (all sections); `frameworks/hook-writing-system.md §The qualified-hook-rate judgement, §Executing with MCP data`; `evolution.md §5, §6` |
| Ben | Full: formula, 2024 benchmarks (much lower range), diagnostic pairings, low-hook/good-CPA splice method | `ben-heath/knowledge/themes/creative-and-hooks.md §Hooks`; `frameworks/hook-multiplication-and-splicing.md §Step 1-2, §What NOT to do`; `frameworks/account-diagnostic.md` |
| Marin | Partial: reads thumb-stop/hold **relative to account average**, only in combination; one dated example | `marin-istvanic/knowledge/themes/creative-strategy-and-diversification.md §Creative metrics only read in combination`; `frameworks/account-audit-method.md §Step 5 — Ads`; `frameworks/creative-diversification-method.md` ("high opportunity" ads); `themes/testing-and-iteration.md` (kill signals) |
| Barry | Position only: hook rate measures attention, not relevance; down-weighted; **declines to give a benchmark** | `barry-hott/knowledge/themes/testing-and-measurement.md §(metrics that lie)` |
| Nick | Position only: **refuses** hook rate and hold rate as decision metrics; uses raw video drop-off instead | `nick-theriot/knowledge/themes/metrics-and-diagnostics.md §What he refuses to optimise for` and columns table |
| Phil | **Silent.** No hook-rate or hold-rate material in his corpus. Do not infer a position. | — |

## 2. Consensus

1. **Formula: 3-second video plays ÷ impressions, as a custom metric.** It is not a native Ads Manager column. Dara, Ben, Alessio and Lorenzo all build it this way. (`dara-denney/knowledge/frameworks/hook-taxonomy.md §Step 2`; `ben-heath/knowledge/frameworks/hook-multiplication-and-splicing.md §Step 1`; `alessio-cordeddu/knowledge/themes/creative-testing.md §custom columns` (he calls it "attention rate"); `lorenzo-pravata/knowledge/frameworks/hook-writing-system.md §Executing` (2024-03-20 definition))
2. **It answers one narrow question: did the opening stop people?** Not whether the ad sells. Seven of eight corpora say this in some form; Phil is silent. (Barry: "measures attention, not relevance", `barry-hott/.../testing-and-measurement.md`; Alessio: soft metrics "don't confirm traffic quality or conversion", `alessio-cordeddu/.../creative-testing.md §Which metrics he trusts`; Dara: a "storytelling" metric, `dara-denney/.../two-question-analysis.md §The metric split`)
3. **Never scale, pause or kill on hook rate alone. Spend, CPA and ROAS decide.** Dara (only primary metrics may drive an action), Ben (diagnostic, never a target; never turn off a good-ROAS ad over a secondary metric), Alessio (sort by spend; soft vs hard quadrant), Barry (no surefire metric but dollars, 2025-04-25), Nick (refuses it), Lorenzo (2026-04-21 correction), Marin (only in combination). (Sources as in §1.)
4. **A high hook rate from the wrong people is worth nothing, or worse.** Independently held by Barry (2025-02-12), Nick (2026-07-10), Lorenzo (2026-04-20/21) and Dara (her "55% hook rate that didn't convert" interview test). Lorenzo and Dara both add the mechanism: the opening also tells Meta whom to deliver to, so chasing raw hook rate can train delivery towards non-buyers. (`barry-hott/.../testing-and-measurement.md`; `nick-theriot/.../metrics-and-diagnostics.md`; `lorenzo-pravata/.../hooks-and-qualified-attention.md §Non-negotiable: the qualified-hook-rate correction`; `dara-denney/.../hooks.md §The principle (2), §Measuring hooks`)
5. **Read it paired, not alone: hook vs hold (or play time) vs CTR vs CPA.** The pairings localise the problem.
   - High hook + low hold/play time: the opening works, the body or the hook-body continuity doesn't. Fix the middle, keep the hook. (Lorenzo 2023-12-20 onward; Ben `account-diagnostic.md`; Alessio's retention drop 3s→25%)
   - High hook + low CTR: wrong audience, unconvincing offer, or not enough proof. (Dara matrix; Ben `account-diagnostic.md`)
   - Low hook + low hold: the creative isn't landing; back to the drawing board. (Dara)
   - Strong soft + weak hard metrics: the back end (offer, landing page, targeting) is broken, not the creative. (Alessio 4-quadrant, 2026-04-05; Ben "landing page / post-click problem")
6. **Compare against your own account, not a universal number.** Marin reads thumb-stop and hold "compared to the average"; Alessio says prefer account-relative thresholds and frames his table as a starting point; Dara calls her figures personal reference points and benchmarks category-relative; Barry gives none at all. (`marin-istvanic/.../account-audit-method.md §Step 5`; `alessio-cordeddu/knowledge/evolution.md` numbers table; `dara-denney/.../hook-taxonomy.md §Step 2`)
7. **Video only.** There is no hook rate for a static. (Dara, explicit, `static-ad-construction.md` and `two-question-analysis.md`; implicit everywhere else.)

## 3. Splits

### Split A: Is a high hook rate a good sign?
- **Camp A, "useful early signal, with a bar":** Alessio treats it as a reliable soft metric readable off a few thousand impressions (2,000-impression floor), with a winning threshold (>40%). Dara: "high hook rate alone = you're reaching the right demographic; make more hooks like it." Lorenzo publishes a target (see §5). Wins when: you are iterating hooks on a concept that already converts, and you need a fast read before CPA data arrives. (`alessio-cordeddu/.../creative-testing.md`; `dara-denney/.../hooks.md §diagnostic matrix`)
- **Camp B, "the metric lies / I won't use it":** Nick: "Hook rate is also just the worst thing to look at" (2026-07-10), because a shocking opener can buy a near-100% hook rate from people who'll never buy; he uses raw milestone drop-off instead. Barry down-weights hook, hold and CTR as Meta automates more and declines to benchmark. Wins when: the account optimises to purchases and has enough conversion volume to judge on CPA directly. (`nick-theriot/.../metrics-and-diagnostics.md`; `barry-hott/.../testing-and-measurement.md`)
- **Camp C, "diagnostic and production tool, never a target":** Ben uses it to find which ads deserve a new opening (low hook rate + excellent cost per result = the best ad to re-hook). Lorenzo has moved here: his 2026-04-21 self-correction says raw hook rate "means nothing" until paired with downstream CPA/CVR on the same ad. (`ben-heath/.../hook-multiplication-and-splicing.md §Step 2`; `lorenzo-pravata/knowledge/evolution.md §6`)
- **What it's really about:** what the metric is *for*. Nobody in Camp A says optimise to it either; the split is whether it earns a threshold at all.
- **Suggested verdict:** take Camp C as the article's spine. If hook rate is high **and** CPA is on target, the hook is working: make more like it. If hook rate is high and CPA is bad, you hooked the wrong people (or the body fails): rewrite the opening to pre-qualify, or fix the body. If hook rate is low but CPA is excellent, that ad is your best candidate for new hooks. Never act on hook rate alone.

### Split B: What range is "good"? (A split of context, not of method)
- **DTC/creative-agency camp:** 25-45% on 3s ÷ impressions (Dara, Alessio, Lorenzo, Marin's example). 
- **Ben:** >10% good, <5% poor (2024), with "90%+ of people for most advertisers never get past three seconds" (2025-06-03). Same formula. His examples come from his own lead-gen/info accounts, and he says on camera B2B sits on the low side. (`ben-heath/sources/youtube/mycqb92wJqk/transcript.md` [7:07], [15:14])
- **What it's really about:** account type, offer and format (lead gen/B2B vs DTC; talking-head/podcast formats vs other video), plus placement mix and vintage. The formulas match, so the gap is real-world variance, which is itself the strongest argument for account-relative reading.
- **Suggested verdict:** give the DTC cluster as "what practitioners commonly report", show the lead-gen/B2B figure as proof that the number moves with business type, and tell readers to set their bar from their own account average.

### Split C: Hold rate's denominator
- Dara: 15-second plays (or completion if under 15s) ÷ **impressions**. Alessio: ThruPlay ÷ **impressions**. Lorenzo: 15-second views ÷ **3-second views**. Ben uses average play time instead; Nick uses raw milestone drop-off; Marin wants hook + hold + watch time all strong together.
- **What it's really about:** definitions. Impression-based hold rates land around 7-15%; a hold rate over 3-second viewers will read far higher for the same ad.
- **Suggested verdict:** present both formulas, say which one you use, and never compare a number to a benchmark computed the other way. Same for hook rate across tools (CONCEPTS.md: impressions vs reach vs plays).

## 4. Single-source insights
- **Pre-qualify inside the hook** (Lorenzo, 2026-05-21): use the buyer's own vocabulary in the first few words so the right people stop and the wrong ones scroll. Stands on first principles; usable as our reasoning.
- **"Ad fatigue is really hook fatigue"** (Ben): since most viewers never pass 3 seconds, a new opening on the same body can extend an ad's life. Usable as "some practitioners…"; links to article 05.
- **High-opportunity ads** (Marin, 2026-07-11): iterate ads that are outstanding on one video metric and bad on another (e.g. high hold, poor hook), not ads that are average on both. Usable as our reasoning.
- **Meta's effective hook window is ~1-1.5 seconds, not 3** (Dara, attributed to Meta). Needs a Meta primary source before use (see §9).
- **Creator Marketplace shows creators' organic hook rate** as a sourcing signal (Dara). Verify in Meta docs before use.
- **Retention-band surgery** (Alessio): map the biggest drop in the 3s / 25 / 50 / 75 / 95% curve back to the script block that causes it. Usable as generic method, without his band names.

## 5. Numbers

**Hook rate (3-second plays ÷ impressions, video):**
| Source | Figure | Date / context |
|---|---|---|
| Dara | ~25% "could get better", 35%+ good, 40%+ impressive; one worked account averaged ~30% | 2024-10-16, her client base, DTC; personal reference points, not benchmarks |
| Alessio | <30% bad, 30-37% average, >37% good, >45% great; "winning" stated as >40% (and >45%) | Table 2024-11-11 (never republished); >40% repeated 2026-02-01. Unreconciled; flag the variance |
| Lorenzo | 30% minimum → 35%+ → 40-45% for podcast-style ads | 2024-07-11 → 2025-10/2026-02 → 2026-08-21. Self-reported from his own accounts, increasingly format-specific |
| Marin | Outlier at 44% vs 24% account average | 2026-07-04, one inherited account; illustrates relative reading |
| Ben | >10% good, <5% poor; worked examples 10.6-16.2% (2024) and 15.55-27% (2026-03-10, lead gen) | 2024 diagnostic video; he flags B2B as lower. 2024 vintage, predates Reels-first |
| Barry, Nick | No figure, by choice | — |

**Panel summary for the article:** "For DTC video ads, practitioners commonly report roughly 25-30% as the low end and 35-45% as strong. Lead-gen and B2B accounts often sit far lower, under 10%, and that can still be healthy. Your own account average is the only bar that matters." (Ranges, not one person's number.)

**Hold rate:** Dara ~7-8% account average (15s ÷ impressions); Alessio <7% bad, 7-12% average, >12% good, >15% great (ThruPlay ÷ impressions, 2024). Lorenzo's 15s ÷ 3s formula has no published benchmark. Two impression-based sources cluster at roughly 7-15%.

**Read floor:** Alessio's 2,000 impressions before reading soft metrics (single source; usable as "a few thousand impressions" reasoning).

## 6. Myths and retired advice
- **"Get the highest hook rate you can."** Retired by its own most vocal promoter (Lorenzo, self-correction 2026-04-21) and rejected by Barry and Nick. Strong "stop doing" section.
- **"Hook rate is a column in Ads Manager."** It isn't; you build it. (Dara, Ben)
- **"My static ad has a hook rate."** Hook rate is video-only. (Dara)
- **"Hooks are 80% (or 90%) of an ad's success."** Unmeasured and self-contradicting (Lorenzo stated 90% in 2024-08, then 80% from 2024-09). Don't print either as fact.
- **">10% is good" as a current universal threshold.** Ben's 2024 figure; his own brain flags it as 2024-vintage, pre-Reels-first. Don't present it as current or general.
- **"Test 2-4 clean hook variants."** Dara's 2024 rule, replaced by 3-6 big-swing variants (2026). Only relevant if the article touches testing (link out to 11).
- **Comparing hook rates across tools or formulas.** Different denominators (impressions, reach, plays) make them incomparable. (CONCEPTS.md `metric.hook_rate`)

## 7. Do not use in the article
- Any expert name, handle, quote or link (including the punchy lines: "You can't deposit hook rate in a bank account", "Thought-stopping > thumb-stopping", "worst thing to look at", the "naked girl" 100%-hook-rate example).
- Coined names: Dara's "two-question analysis" and "trigger word hook"; Alessio's "Gut / Brain A / Brain B / Pocket" retention bands and "ugly duckling" quadrant label; Ben's "Frankenstein" splice and "hook fatigue" as a named concept; Lorenzo's "qualified hook rate" as *his* term, "two jobs of every hook", "three ingredients", "first six words". Describe the ideas. ("Hook rate among likely buyers" is a safe paraphrase; "qualified hook rate" is generic enough to use once as a plain-English phrase, never as a named framework.)
- Headline numbers tied to one person's business: "45%+ hook rates" (Dara's 2026 video title, Lorenzo's article title), "40-45% with podcast ads, most agencies struggle to crack 30", "$17M / $100M+ in spend", Ben's £30 vs £11.02 example, Marin's 44% vs 24% and "4 winners out of 6", the creator "50% hook rate / 7% interaction rate", "10-15% of top creative contains POV".
- Ratio pairs used rhetorically ("15% of buyers beats 60% of the wrong people", etc.): they vary between tellings and aren't data.
- Gated assets: the 500+ hooks list, 25-page hooks guide, hook-writing Claude Skill.
- Third-party tools named in corpora (Motion, Varos). PLAN rule: no Motion mentions.

## 8. Draper angle
Per PLAN: "Hook variants are cheap to make and slow to launch." Defensible from the profile:
- The consensus action on a good hook rate is "make more hooks like it", and on a low-hook/good-CPA ad it's "give it new openings". Both mean many near-identical ads going into ad sets. In Ads Manager that's 17+ clicks per ad when built from scratch in one ad set (profile unit; if the article multiplies across ad sets, say it assumes a rebuild each time or mark the duplicate cost `[TK]`).
- **Automatic ad naming** from the creative file: if each hook variant's file name carries the hook, the hook-rate comparison by ad is readable later. Ties to article 02 (naming).
- **Create once, deploy many** and **cloud-native creative** from Google Drive: one body, several hook files, launched together.
- Don't claim Draper improves hook rate, ROAS or performance; it saves the launch time. Avoid "AI-powered".
- Cross-links: hub article 11 (testing), 05 (fatigue, via "new hook on the same body"), 02 (naming).

## 9. Open questions
- **Meta definitions to verify against Meta's own docs:** what "3-second video plays" counts (autoplay; 97% length for short videos), ThruPlay (15s or completion if shorter), and whether any 2025-26 change to video metrics alters the formula's inputs. Exact Meta URLs only.
- **"Meta says the effective hook window is 1-1.5 seconds"** (relayed by Dara): needs a Meta primary source or drop it.
- **Placement effects:** Reels vs Feed vs Stories likely shift hook rate; no expert gives numbers. Possible `[TK]` or omit.
- **Thumb-stop rate vs hook rate:** some tools use reach or plays as the denominator; the article should state the formula it uses and note the naming is inconsistent.
- **First-hand proof:** a Draper/Wonderland anonymised account-average example (hook rate by format) would strengthen the "use your own average" point. Candidate `[TK]`.
