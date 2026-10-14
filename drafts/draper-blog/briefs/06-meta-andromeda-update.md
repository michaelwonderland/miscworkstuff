# Panel brief: What did Andromeda change, and what should I do about it?

```yaml
question: "What did Andromeda change, and what should I do about it?"
primary_keyword: "meta andromeda update"
secondary_keywords: ["meta andromeda creative diversity"]
search_intent: informational
size: medium
format: auto            # PLAN suggests F essay / E explainer
profile: draper-ads
experts_consulted: [barry-hott, dara-denney, phil-kiel, nick-theriot, alessio-cordeddu, ben-heath, marin-istvanic, lorenzo-pravata]
```

## 1. Coverage

All eight cover it. None is silent. They cover it at different altitudes:

| Corpus | Altitude | Main files |
|---|---|---|
| ben-heath | Explains the system from Meta's published article (read on screen) | `ben-heath/knowledge/themes/platform-mechanics.md §Andromeda` |
| dara-denney | Explains the pipeline (Andromeda, then GEM, then Lattice); diversity audit | `dara-denney/knowledge/themes/platform-mechanics.md §Current model`; `frameworks/5-levels-of-creative-diversity.md` |
| nick-theriot | Dated rollout, two named effects, then disowns the algorithmic *reason* | `nick-theriot/knowledge/themes/platform-changes.md §Andromeda`; `evolution.md §14` |
| marin-istvanic | Observed account behaviour; format vs argument diversification | `marin-istvanic/knowledge/themes/platform-mechanics-and-andromeda.md`; `frameworks/creative-diversification-method.md` |
| lorenzo-pravata | Mechanistic theory (entity IDs) and creative production | `lorenzo-pravata/knowledge/themes/andromeda-gem-and-entity-id-theory.md`; `frameworks/account-diagnosis-and-entity-audit.md` |
| alessio-cordeddu | Creative-ops: what variation shape died | `alessio-cordeddu/knowledge/evolution.md §3`; `themes/creative-diversity.md` |
| phil-kiel | Short claims plus a contrary 2026 observation | `phil-kiel/knowledge/themes/platform-mechanics-and-bugs.md §Andromeda` |
| barry-hott | Skeptic: brief for consumers, not for Andromeda | `barry-hott/knowledge/themes/platform-mechanics.md §Andromeda` |

Boundaries: Lorenzo's corpus has no account mechanics (he declines that seat himself, `lorenzo-pravata/index.md` rule 9). Barry has no diversity audit method. None cite internal Meta engineering detail beyond the published article.

## 2. Consensus

1. **Andromeda is not why your ads are bad; don't make it the scapegoat.** All eight say this independently. Barry: "Stop trying to make Andromeda happy. Make consumers happy" (`barry-hott/knowledge/themes/platform-mechanics.md §Andromeda`). Phil: "Andromeda didn't stop your ads from working. They didn't work in the first place" (`phil-kiel/knowledge/themes/platform-mechanics-and-bugs.md §Andromeda`). Nick: brands that blame it are "extremely stuck" (`nick-theriot/knowledge/evolution.md §14`). Ben: "fear-mongering" (`ben-heath/.../platform-mechanics.md §Andromeda`). Dara: not responsible, with an asterisk: competitors with better ads and bigger budgets (`dara-denney/.../platform-mechanics.md §Current model`). Lorenzo: "Andromeda isn't to blame for your bad ads" (`lorenzo-pravata/.../andromeda-gem-and-entity-id-theory.md §guardrails`). Marin tracks "Andromeda" as the latest swapped scapegoat (`marin-istvanic/.../platform-mechanics-and-andromeda.md §Andromeda`).
2. **Small variations of one asset no longer count as new ads.** Headline swaps on one image (Nick, `platform-changes.md §Andromeda`), filters (Alessio, `evolution.md §3`), text overlays, thumbnails and widgets (Marin, `creative-diversification-method.md §2`), 15 lookalike assets (Phil, `platform-mechanics-and-bugs.md §Andromeda`), messaging-only changes on the same visuals (Dara, `platform-mechanics.md §Current model`), and a new hook on the same footage (Lorenzo, `andromeda-gem-and-entity-id-theory.md §What the model tells you to do`).
3. **Real diversity means reaching a different person, not just a different look.** Six corpora name the axes: persona, awareness stage, desire or reason to buy. Dara (levels 2 to 4, `5-levels-of-creative-diversity.md`), Ben (awareness stages, pain points, desires, avatars, `platform-mechanics.md §Andromeda`), Marin (argument diversification, `creative-diversification-method.md §3`), Alessio ("a new way to sell the same product to a different person", `themes/creative-diversity.md`), Lorenzo (persona, awareness, format, actor, angle, `creative-diversity-over-volume.md`), Nick (same visual across different avatars, `platform-changes.md §Andromeda`).
4. **Volume without difference is waste.** Ben: "Don't create volume for the sake of volume" (`platform-mechanics.md §Andromeda`). Phil: 20 similar ads a week is worse than 10 with a bigger conceptual gap (`platform-mechanics-and-bugs.md §Andromeda`). Dara: "volume is not exactly the answer" (`themes/creative-diversity.md §volume-versus-diversity`). Marin: 500 variations a week at a 1 to 2% hit rate (`creative-diversification-method.md §5`). Alessio: diversity > quantity > quality (`themes/creative-diversity.md §4`).
5. **Don't rebuild your account structure for it.** Marin kept his structure "Andromeda update or not" (`platform-mechanics-and-andromeda.md §Andromeda`). Ben warns against elaborate "Andromeda-proof" structures (`platform-mechanics.md §Andromeda`). Phil: if you're winning, your structure is probably already compatible (`platform-mechanics-and-bugs.md §Andromeda`). Dara: structure is now "far less important" (`platform-mechanics.md §Current model`). Each expert's preferred structure still differs (see the panel's account-structure split). The shared point is: don't restructure *because of* Andromeda.
6. **Targeting moved into the creative.** Dara: interests, lookalikes and prospecting/retargeting splits are "pretty much useless" (`platform-mechanics.md §Current model`). Lorenzo: "Targeting used to live in the adset. Now it lives inside the ad itself" (`andromeda-gem-and-entity-id-theory.md §5`). Ben: personalisation moves from group to individual level (`platform-mechanics.md §Andromeda`). Nick: "ad creates the audience" (`platform-changes.md §Andromeda`).

## 3. Splits

### Split A: why diversity works (the key split)
- **The question:** Is the case for diversity built on how Meta's system works, or on what you can observe in your own account?
- **Camp A, observed behaviour (Marin):** Starts from what he saw. Iterations stopped beating originals (2025-07-09). Then a narrow claim: Meta's classifier groups visually similar ads and serves them to roughly the same people. He grounds it in Meta's own Creative Diversification Cheat Sheet and a Meta confirmation that a different thumbnail gets a different entity ID (2026-02-26). Then hit-rate maths. He is explicitly skeptical of algorithm stories: "test it on your own account." He never publishes an internal model. Wins when the reader runs a real account and can check the claims against their own data. `marin-istvanic/.../platform-mechanics-and-andromeda.md §Andromeda, §Empiricism, §What this theme does not claim`; `creative-diversification-method.md §2`.
- **Camp B, mechanistic theory (Lorenzo):** Builds a full model. Two-stage retrieval in about 300ms. An entity ID computed as a semantic fingerprint (visuals, narration, copy, pacing). One auction ticket per distinct entity, so "Most brands running 50 ads are running 3 entities." A behavioural tree that cuts whole branches. **The corpus cites no Meta documentation, and no Meta API returns an entity ID.** His language hardened from "may" (2026-02-20) to flat assertion (2026-03-05) with no new evidence. Wins as a teaching device for creative teams: it makes "shoot it differently" feel necessary. `lorenzo-pravata/.../andromeda-gem-and-entity-id-theory.md §Read this before, §The model`; `lorenzo-pravata/index.md` rule 8.
- **Camp C, consumer-first (Nick, Barry):** Nick taught the algorithmic reason through late 2025. By 2026-07-10 he calls the "Andromeda era" explanation "completely false" *as a reason*. He still recommends format diversity, for consumer-preference reasons (`nick-theriot/.../evolution.md §14`). Barry: brief for people, not the algorithm, and the best advertisers were already doing this "since 2024 or earlier" (`barry-hott/.../platform-mechanics.md §Andromeda`).
- **What the split is about:** evidence standards, not tactics. All three reach the same prescription. CONCEPTS.md `creative.diversity` calls this "the most load-bearing record in this pair."
- **Suggested verdict:** Explain only what Meta documents (section 6, "What Andromeda is"). Present the prescription as something the reader can test in their own account, backed by consumer logic. You can mention mechanistic theories ("some practitioners model it as ...") but always label them as theory, never as how Meta works. Never tell the reader their account "has N entity IDs". Use the safety line from the Lorenzo theme file: the moves stand on their own merits even if the internal story is wrong.

### Split B: kill discipline
- **The question:** Should you turn off underperforming ads post-Andromeda/GEM?
- **Camp A, don't kill ads that are spending (Lorenzo, joined by Barry and Phil):** Lorenzo (2026-08-05): "Spend is a confidence signal". Killing a spending ad loses its learned history, creates volatility and keeps the wrong survivors. Check blended results 1 to 3 days later and reverse if they got worse (`lorenzo-pravata/knowledge/evolution.md §11`). His GEM claim: "GEM needs stable signals over time" (`andromeda-gem-and-entity-id-theory.md §6`). Barry: "I AM BEGGING YOU NOT TO TURN OFF HIGH SPENDING ADS". The further an ad's CPA sits above the account average, the more evidence he needs (`barry-hott/knowledge/evolution.md`, 2026-07-28/31). Phil flags high-spend, high-CPA ads that shouldn't be paused (`phil-kiel/.../cpmr-diagnostic.md §4`).
- **Camp B, disciplined kills on a schedule (Marin):** Kills inside a fixed testing schedule on early indicators. Cost per add-to-cart at 2x target, CPC at 3x the account average, spend at 2x AOV with no sale (`marin-istvanic/.../testing-and-iteration.md`; `cpa-roas-decomposition.md §3`). But he does *not* kill ads he has carried to scaling, and he warns against killing a prospecting video that a retargeting image is closing behind (`creative-diversification-method.md §4`).
- **What the split is about:** the ad's stage. Marin kills new tests before they earn spend. Lorenzo and Barry protect ads that already carry spend. Lorenzo's own Feb 2026 rule (off at 3x target CPA) is superseded by his Aug 2026 position.
- **Suggested verdict:** If/then. Cut a new test early on thresholds you set before launch. Don't turn off an ad that carries meaningful spend on ad-level CPA alone. Check blended results after any kill.

### Split C: are hook variants still worth making?
- **Ben:** Hooks still matter post-Andromeda ("They absolutely do"). He multiplies hooks on one body (`ben-heath/.../creative-and-hooks.md`).
- **Lorenzo:** Three hooks per concept, not ten. A new hook on the same footage counts as the same ad, under his theory (`lorenzo-pravata/.../hook-writing-system.md`; evolution §7).
- **Alessio:** Four hook variants of a *new* concept is now his named anti-pattern (2026-06-07). Hook refreshes survive only for a proven winner (`alessio-cordeddu/knowledge/evolution.md §3`).
- **Marin:** Hook variations are near-zero cost and exempt. They find the best version of one concept inside one ad set; they don't diversify the account (`creative-diversification-method.md §6`).
- **Suggested verdict:** Hooks optimise a concept; they don't diversify an account. Count diversity at the concept or argument level. Keep a few hook variants per concept.

### Split D: visual difference or argument difference?
- **Dara:** Andromeda only counts *visual* difference as diversity. Messaging-only variation doesn't count, even if it targets different people (she learned this on a Meta office visit; it applies mainly to Advantage+). Lorenzo agrees: "Difference must be visual, not scripted."
- **Marin:** Format (visual) diversification only extends the life of an argument that's already working. Argument diversification reaches new people. Most teams spend 80/20 on format vs argument when "the impact ratio is the reverse". "If you're only doing one, make sure it's the second" (`creative-diversification-method.md §3`).
- **Suggested verdict:** Each new argument needs its own visual treatment. A new reason to buy, shot differently, satisfies both camps.

### Unresolved observation (not a split, but flag it)
Phil (2026-06-13) reports Meta *concentrating* spend into 2 or 3 ads, "more like Meta circa 2021", against the theory that it spreads spend (`phil-kiel/.../platform-mechanics-and-bugs.md §Andromeda`). Lorenzo holds a similar tension inside his own corpus: "30 small winners" (2026-05-08) vs "2 or 3 ads a month that can each absorb $50k+" (2026-08-01) (`lorenzo-pravata/knowledge/evolution.md §3`). Don't promise readers that spend will spread evenly.

## 4. Single-source insights
- **Use the right word for each kind of change (Marin):** concept (format), angle (reason to buy), iteration (meaningfully different execution), variation (cosmetic change), net-new concept. Usable as our own vocabulary (`creative-diversification-method.md §1`).
- **The signature of format-only diversification (Marin):** spend concentrates in 1 or 2 ads while account frequency keeps climbing (`creative-diversification-method.md`, MCP step 2).
- **Videos prospect, images retarget, for products that need explaining (Marin):** image frequency above 2.0 means the image is reaching warm people (`§4`). Use as "some practitioners".
- **What share of spend is new (Lorenzo):** the share of current spend earned by creative shipped in the last 30 and 90 days (his healthy read: ~20% and ~50%; `lorenzo-pravata/index.md` rule 10). It's a sound audit idea; present the numbers as one practitioner's targets, or drop them.
- **Two named effects (Nick):** faster response to intent signals (minutes), and matching people down to creative *format* preference (`platform-changes.md §Andromeda`).
- **Diversity as insurance (Lorenzo):** if every ad shares one benefit and persona, one change in what Meta predicts about intent removes the whole account from an auction. He states this once; it's the thinnest part of his model. Usable only as reasoning.

## 5. Numbers
- **Ads per ad set:** 3 to 6 variations per concept (Marin, 2026-01/07) up to 20+ ads (Ben, post-Andromeda; his old "6 ads per ad set" is retired). Dara: 10 to 25. Range: 3 to 25+, depending on whether the ad set holds one concept or many.
- **Hooks per concept:** 3 (Lorenzo, 2026-05) to a full hook matrix (Ben). Alessio: none as the variation axis for net-new concepts (lengths instead).
- **New concepts per week:** indexed to hit rate. 5/week at a 10% hit rate, 20/week at 40% (Marin, 2026-08-02). Lorenzo: 10 to 15 structurally distinct concepts per 14-day cycle (2026-05-12). Nick refuses a number.
- **Dates:** Meta published its Andromeda article on **2024-12-02** (Ben; Dara and Phil say "launched 2024/December 2024"). Nick dates the rollout to **July 2025**. Ben says the rollout was gradual and depended on campaign type, which explains why it became the dominant topic only in late 2025. GEM: Lorenzo introduces it 2025-11-27. Dara explains it 2025-12-21. Nick dates it Q2 2025 (his own chronology doesn't hold, `nick-theriot/.../platform-changes.md`).
- **Meta-sourced figures relayed by experts (verify before use; cite Meta directly, never the expert):** >20 creatives in an Advantage+ campaign gives a 29% lower incremental cost per purchase (relayed by Dara). Retrieval narrows "tens of millions" of candidates to "a few thousand" (Meta's article, read by Ben). 45% average drop in likelihood to convert after four repeated exposures (relayed by Marin).
- **Patience:** Phil warns most advertisers quit diversity/consolidation fixes after ~14 days when the problem built over years (`cpmr-diagnostic.md §5`).

## 6. Myths and retired advice
- **"Andromeda means structure doesn't matter."** An over-reading. Marin's structure is unchanged (`platform-mechanics-and-andromeda.md §Andromeda`).
- **"Hooks don't matter after Andromeda."** Rebutted by Ben, 2025-12-12.
- **"Iterations are dead."** Marin's own 2026-05-22 claim, which his 2026-08-04 thread corrects as "too broad". Cosmetic iterations are dead; structural ones work (`evolution.md`; `creative-diversification-method.md §2`).
- **"Andromeda is new" / "it's a penalty or tax."** It was announced in 2024 (Phil, Ben, Dara). Nick's "Andromeda tax" flipped meaning within a month (`evolution.md §14`). Ben calls the anti-advertiser conspiracy "absolutely not the case."
- **What to stop doing (each retired by date):**
  - Four hook variants per new concept (Alessio, retired 2026-06-07).
  - Ten headlines on one winning image (Nick, 2025-11-15).
  - Cosmetic iterations of winners, like overlays, thumbnails and comment widgets (Marin, 2026-08-04; "pre-2023 easy wins").
  - Black-and-white or filter versions (Alessio, 2026-02-24).
  - Six-ads-per-ad-set caps (Ben).
  - Interest and lookalike stacking (Dara, 2025-12).
  - Segmenting statics by message across ad sets (Dara, Dec 2025).
  - Volume for its own sake: Dara's 2026 correction, and Lorenzo's volume-first 2025 lines, which coexist with his newer position and are unresolved (`lorenzo-pravata/knowledge/evolution.md §2`).
  - Elaborate "Andromeda-proof" structures (Ben).
  - Killing spending ads on one bad day (Lorenzo, 2026-08-05).

## 7. Do not use in the article
- **Names, handles, quotes, links** for any of the eight.
- **Coined names:** "5 Levels of Creative Diversity"; "streams"; "dimensional variations"; "mute-and-strip test"; "The Resurrection"; "Andromeda tax"; "Breakdown Effect"; "harvest vs plant intent"; "iteration paralysis"; "four doors that all lead to the same room"; "one auction ticket per entity". The "squint test" is used by two experts independently and is close to generic; describe it ("look at your top ads as thumbnails and ask whether they look like different ads") rather than naming it.
- **Lorenzo's mechanism as fact:** entity-ID counts ("50 ads, 3 entities"), "~300 milliseconds", "semantic fingerprint", "behavioural trees", "1 of 4 updates" (he never names the other three; the post is a lead magnet).
- **Brand cases and stats:** Seed Health (1 in 7), Caraway, Pact (300+ ads), Headspace/Monks (460 assets, 62%), "Jones Miracle Bomb", Grüns. Nick's $63 → $32 CPA case. Lorenzo's $180K/month, 52-of-80 case (it's in a sponsored article). Marin's Creative Similarity score of 11 and "50+ whitelisting pages". Ben's relayed Meta stats (22% ROAS, 7%, 15M ads); cite Meta directly if at all.
- **Self-reported spend, revenue and audit counts** from any expert. Lorenzo's "2% unique concept rate".
- **Dara's account of a Meta office visit** as a source. If the visual-diversity rule is used, attribute it to Meta's own published guidance only once verified (section 9).

## 8. Draper angle
- **The argument:** Andromeda raised the bar from "more ads" to "more *different* ads". Different concepts mean more distinct ads to build and launch, and Ads Manager's campaign-first workflow makes you rebuild each one per ad set ("Ads Manager wasn't built for this pace"). The profile's belief "The algorithm rewards diversity" fits, but the article must keep the panel's line that volume without difference doesn't count.
- **Worked arithmetic** (do it in the open, label the assumption): e.g. 10 new concepts a fortnight × 3 variations = 30 ads. At 17+ clicks to build one ad from scratch in one ad set, that's 510+ clicks *assuming each is built from scratch*. Mark the duplicate-into-another-ad-set cost `[TK]` (profile rule).
- **Automatic naming supports the audit.** You can only count diversity by concept or angle if ad names carry those fields (Marin's naming rule; Alessio refuses angle-level findings without them, `expert-panel/SKILL.md §Refusals`). Draper names each ad from its creative file. Name the files by concept and angle, and the diversity audit becomes a filter.
- **Cloud-native creative:** pull from Google Drive, so a batch of genuinely different concepts goes out without re-uploading.
- **Never claim** Draper improves ROAS or delivery. It saves time; the team spends that time on concepts. No partnership-ads claims.
- **CTA:** the profile's standard CTA, once, at the end. One optional inline mention where the post describes rebuilding the same ad per ad set.

## 9. Open questions
- **Verify against Meta's own docs before publishing:**
  - The 2024-12-02 engineering article (exact URL, and its wording on retrieval vs ranking).
  - Whether Meta publicly documents GEM and Lattice, and their dates.
  - The Creative Diversification Cheat Sheet (does it exist publicly; does it say "different message AND different style"?).
  - Whether Meta has said anything public on thumbnails creating a distinct entity ID.
  - The 29% and 45% figures.
  - The status of the rep-only Creative Similarity & Fatigue report and the planned native Creative Insights.
- **Does "entity ID" originate with Meta?** Marin reports a Meta confirmation using the term, but Lorenzo's ticket-counting mechanism is his own. Settle what Meta says before the article uses the term at all. Safest: avoid it.
- **Phil's spend-concentration observation vs the spreading theory:** unresolved. A good `[TK]` would be first-hand data showing spend distribution across concepts before and after diversifying.
- **No expert offers a validated score for "diverse enough."** Dara says she's unsolved on a KPI. Don't invent one.
- **Suggested article angle:** Andromeda changed *how Meta picks ads*, not what wins. Meta now matches each person to the creative that fits them, so near-copies stop earning extra reach. The fix is new reasons to buy, each shot differently, launched without rebuilding your account. Audit your top spenders by concept, not ad count.
