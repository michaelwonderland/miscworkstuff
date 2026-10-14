# Panel brief: How should I name campaigns, ad sets and ads so I can actually analyze creative?

A panel brief turns a body of expert knowledge into the input for one article. Names and sources live here, for verification only, and never appear in the article.

```yaml
question: "How should I name campaigns, ad sets and ads so I can actually analyze creative?"
primary_keyword: "ad set name example"
secondary_keywords: ["facebook ads naming convention"]
search_intent: informational
size: short
format: auto            # PLAN.md suggests C catalogue: worked name examples per level
profile: draper-ads
experts_consulted: [barry-hott, dara-denney, phil-kiel, nick-theriot, alessio-cordeddu, ben-heath, marin-istvanic, lorenzo-pravata]
```

## 1. Coverage

| Corpus | Coverage | Where |
|---|---|---|
| **Marin** | Full framework: one formula per level (campaign, ad set, ad), field-by-field rationale, two extensions, audit method. Oldest stable core in his corpus (2023, restated 2024-11, never contradicted through 2026). | `marin-istvanic/knowledge/frameworks/naming-conventions.md` |
| **Alessio** | Full framework: the field set, a dropdown sheet that concatenates the name, one string reused across systems, "fewer variables, more adoption", the `scale` prefix. Current (2025-11, 2026-04); 2024 three-tier schema is foundational. | `alessio-cordeddu/knowledge/frameworks/naming-convention.md`; `evolution.md` §5 |
| **Phil** | Three dated ad-name templates (2023, 2025-07, 2025-10) plus qualitative tags (2026); naming as an audit red flag; Page/Creator fields for whitelisting. | `phil-kiel/knowledge/themes/testing-and-iteration.md` §Naming conventions; `frameworks/account-audit-red-flags.md` §2-3; `frameworks/partnership-whitelisting-flywheel.md` §Executing step 2 |
| **Nick** | Thin but real: ad sets named by sequential idea/batch number with parent lineage (`188-117`); landing-page duplicates named `101 Product Page`; three creatives per concept under one number. | `nick-theriot/knowledge/frameworks/creative-testing-system.md` §Step 3; `frameworks/iterations-variations-new-messaging.md` Check 2; `frameworks/one-campaign-account-structure.md` step 4 |
| **Dara** | Uses naming as a grouping key (creator-level performance), and warns that a naming label is not proof of diversity (the squint test). No published convention of her own. | `dara-denney/knowledge/frameworks/creator-program-system.md` Check 2; `frameworks/5-levels-of-creative-diversity.md` §squint test |
| **Lorenzo** | One doctrine line: ship "with consistent naming so testing data stays clean" in his 14-day pipeline. Everything else on naming in his brain is the brain author's data-access notes, not his position. | `lorenzo-pravata/knowledge/frameworks/assembly-line-and-14-day-pipeline.md` (Days 12-13) |
| **Barry** | **Silent** as doctrine. His "spend carried per creative source" metric needs a source tag, but the naming advice is the brain author's execution note. | `barry-hott/knowledge/frameworks/hit-rate-rejection.md` §Attributing ads to a source (author note) |
| **Ben** | **Silent.** No naming convention in the corpus. | — |

CONCEPTS.md has no naming concept; the only note is under funnel stage: "A naming convention is not a measurement. Funnel labels are frequently stale" (`CONCEPTS.md` funnel-stage entry, ~line 1257). No `disagreement` field applies.

## 2. Consensus

1. **Creative analysis starts with the name.** If a variable isn't in the name, you can't group by it, so you can't answer "which angle / creator / format wins". Alessio (`naming-convention.md` §The principle), Marin ("naming → structure → pattern recognition", `naming-conventions.md` intro and §5), Phil ("the substrate of every comparison", `testing-and-iteration.md` §Naming), Lorenzo (`assembly-line-and-14-day-pipeline.md` Days 12-13).
2. **Default and duplicated names are the red flag.** "New ad" and stacked "- Copy - Copy" hide performance patterns. Marin (`naming-conventions.md` §Executing step 3, 2024-11), Phil (`testing-and-iteration.md` §Naming, 2023-12 and 2025-08; `account-audit-red-flags.md` §3, `Copy of Copy_V3_NEW_Final2`, 2025-11). Nick's brain makes the same check from ad-set names (`creative-testing-system.md` Check 3, author note).
3. **Fields that recur across independent conventions** (the backbone of the article's examples):
   - **Format / creative type** (video, static, carousel): Marin ad level, Alessio, Phil 2023/2025/2025-10.
   - **Concept** (the idea being tested): Marin (ad set level), Alessio, Phil 2025 and 2025-10, Nick (idea number).
   - **Creator / talent**: Marin (`Unboxing Laura`), Alessio (Model, "who's worth rebooking"), Phil (Creator), Dara (groups by creator via the name).
   - **Version / iteration**: Marin (`v3`), Alessio (Variation + test type), Phil (Version/Iteration, 2025), Nick (parent lineage `188-117`).
   - **Date or batch**: Marin (ad-set launch date), Alessio (weekly batch), Phil (Date), Nick (batch number).
   - **Landing page / destination**: Marin (PDP / advertorial / listicle), Phil (LP / PDP, 2023, 2025, 2025-10), Nick (ad sets named by page type).
   - **Angle / copy argument**: Marin (copy/angle), Alessio (Angle). Product: Alessio, Phil 2025-10.
4. **One convention for the whole account, used by everyone.** Mixed conventions from freelancers, agencies and in-house teams are a named failure. Alessio (`naming-convention.md` §two rules, Check 3), Phil (finding many previous agencies' names in campaign names, `account-audit-red-flags.md` §2, 2025-10; "renaming campaigns to your agency name isn't onboarding", `agency-operations-and-career.md`, 2025-06).
5. **Don't rename live entities to retrofit a convention.** It breaks reporting continuity and the join to third-party trackers; apply going forward and back-fill in a side table. Alessio (`naming-convention.md` §What NOT to do), Marin (`naming-conventions.md` §Executing step 4 and §refuses).
6. **Naming is a reporting fix, not a performance fix.** Marin states it outright (`naming-conventions.md` §refuses: "It does not claim naming improves performance"); Alessio frames it as turning data into decisions (`naming-convention.md` §principle). Use this to keep the article honest.

## 3. Splits

### Split A: How many fields, and how much detail?
- **Camp A, lean (5 fields per level, compressed codes):** Marin's ad name is 5 fields (`Creative type - style - copy/angle - headline - destination`), ad set 4, campaign 4. He uses short codes (`LC`, `CC`, `@`, an opaque token for awareness), partly because Meta shortened the inline name-edit field in Feb 2025 (`naming-conventions.md` §1-5). Nick is leaner still: a number plus lineage. Wins for small teams and media-buyer-led accounts.
- **Camp B, rich (7 to 12 fields, generated not typed):** Alessio's current set runs to ~12 fields incl. awareness, model, product, test type, with ops metadata, but generated by dropdowns + a concatenation formula (`naming-convention.md` §current field set, §mechanism). Phil's 2025-07 template has 11 parameters, trimmed to 7 by 2025-10, then extended with qualitative tags in 2026 (`testing-and-iteration.md` §Naming). Wins for teams with a creative strategist and a production pipeline, where the name is the brief ID.
- **The tension inside Camp B:** Alessio's own lesson is that more variables reduced adoption ("our creative strategists were using it less, paradoxically"), and his ad tier was deliberately simplified from the 2024 schema. Phil's template also shrank 11 → 7.
- **What it's really about:** team size and whether names are typed by hand or generated.
- **Suggested verdict:** If people type names by hand, cap the ad name at 5 to 7 fields. Go richer only when the name is generated (sheet, formula, or tool) and every field is one you'll actually pivot on. Rule of thumb for the article: "add a field only when you can name the question it answers."

### Split B: What goes at which level, especially the concept?
- **Camp A, concept at ad-set level:** Marin names the ad set `Launch date - Audience - bid type - concept` because one ad set = one concept in his testing system (`naming-conventions.md` §2). Nick names the ad set by idea number (`creative-testing-system.md` §Step 3).
- **Camp B, everything that matters at the ad level:** Alessio's single concatenated string lives on the ad (and the file, brief and ticket); campaign and ad-set tiers are "useful and largely uncontroversial" but secondary (`naming-convention.md` §2024 schema status). Phil's templates are all ad-name templates.
- **What it's really about:** testing structure. Concept-per-ad-set works while the ad stays in its ad set. Marin himself copies winners by post ID into a scaling campaign (`marin-istvanic/knowledge/frameworks/abo-testing-to-scaling-pipeline.md`), where the ad-set name no longer travels with the ad. (This last inference is ours, not his.)
- **Suggested verdict:** Campaign = structure (type, objective, location, offer). Ad set = when and how it's being bought (launch date, audience, bid type, plus concept if you run one concept per ad set). **Ad = everything about the creative**, including the concept, because the ad name is what survives copying, duplicating and exporting to reports.

### Split C: Funnel stage in campaign names
- Marin's 2023 campaign field was funnel position (1-4 / TOF, BOF, Repeat); his 2024 revision replaced it with Prospecting vs Existing buyers, "don't separate rtg", hardened in 2026 to "you don't need TOF/MOF/BOF campaigns" (`naming-conventions.md` §1; `evolution.md`). Alessio's 2024 campaign prefix (`0/1/2` stage) encodes testing vs scaling, not funnel (`naming-convention.md` §2024 schema). Not a live split so much as a retired field; see section 6.

### Split D: Words vs codes
- Marin and Alessio both use compact codes (`LC`, `@`, `B3-C2-V1`) with a key that lives with the team; Phil writes descriptive tokens. Codes survive the short edit field and are filterable; words are readable by a new hire. **Verdict:** codes for closed lists (bid type, format, destination), words for open ones (concept, creator), and publish the key.

## 4. Single-source insights
- **Generate the name, don't type it** (Alessio): every field is a dropdown; a formula concatenates them; the same string is used for the brief, the export filename, the ad name and the task ticket (`naming-convention.md` §mechanism). Stands on first principles; it is also the Draper tie.
- **A `scale` prefix** for ads being scaled while still inside the testing campaign, so month-end analysis attributes the spend correctly (Alessio, `naming-convention.md` §two rules, 2025-11).
- **A one-character prefix for a tactic** (Marin's `@` for whitelisting ad sets) turns "have we really tested this?" into a filter with a spend total (`naming-conventions.md` §4, 2026-04). Generalisable: prefix any tactic you'll want to total later.
- **Launch date in the ad-set name** is the join key to third-party trackers and lets you cohort weekly launches (Marin, §2).
- **Lineage in the name** (`188-117` = idea 188 iterates idea 117) lets you see iteration chains drifting from the original (Nick, `iterations-variations-new-messaging.md` Check 2).
- **Bid type in the ad-set name** makes Cost Cap vs Lowest Cost reportable (Marin, §2).
- **Creator field converts "who do we rebook?" into a data question** (Alessio, Check 5; Dara uses the same cut for creator concentration, `creator-program-system.md` Check 2). Two experts, so near-consensus.
- **A name is not a diversity measure.** Lay out your top creatives and check whether they look the same, "no matter what your naming convention says" (Dara, `5-levels-of-creative-diversity.md`). Good caution line.
- **Score your own account before adopting someone else's scheme**: parse names, measure compliance, flag defaults first (Marin §Executing steps 2-4, 8; Alessio Checks 1-3). Usable as a "5-minute audit" section.

## 5. Numbers
- **Fields per ad name:** 5 (Marin, 2024-11) to ~12 incl. ops metadata (Alessio, 2025-11/2026-04); Phil 11 (2025-07) → 7 (2025-10). Most usable conventions cluster at 5 to 7 creative fields.
- **Fields per ad-set name:** 4 (Marin); 3 (Alessio 2024 foundational: date, audience, placement).
- **Fields per campaign name:** 4 (Marin: type, objective, location, offer); 4 (Alessio 2024: stage, setting, goal, location).
- **Creatives per concept under one number:** 3 (Nick, `creative-formats.md` §Production rules). Context only.
- **Primary source to verify:** Ads Manager name-field length / inline edit behaviour (Marin's Feb 2025 complaint). No character limit is stated in the corpus.

## 6. Myths and retired advice
- **Funnel-stage campaign labels (TOF/MOF/BOF).** Marin retired the field 2023 → 2024-11 and the campaigns themselves by 2026-05 (`naming-conventions.md` §1, §refuses). Labels go stale relative to what the campaign actually does (`CONCEPTS.md` funnel note).
- **The bigger the convention, the better.** Alessio's own history: more variables, less use (`naming-convention.md` §principle); the 2024 ad tier was simplified.
- **Fixing names fixes performance.** Marin: no (`naming-conventions.md` §refuses).
- **Renaming the whole account to the new scheme on day one.** Alessio and Marin both: don't; go forward and back-fill.
- **Old test-type vocabularies.** Alessio's "new / more / better" field values are superseded twice (→ early/script/fine-tuning/late iteration); don't present the 2024 values as current (`naming-convention.md` §2024 schema).

## 7. Do not use in the article
- Expert names, handles, quotes, links. Forbidden list in `forbid.txt` includes the analytics-tool brand some experts cite; also don't name third-party trackers as recommended by anyone.
- Alessio's agency prefix (`99ads-…`) and his "$200,000/month account" opening anecdote; the 12-hour/2-hour course references.
- Marin's awareness codenames (the two girls' names), his `@` stats (650+ tests, ~$4M, 300-350 pages), the "$300 across 83 ad sets" audit, his Feb 2025 profanity about the name field.
- Phil's verbatim joke about "Copy" correlating with ROAS, the `[kitchen=banger]` tag, "15 previous agencies" anecdote, his "Old Media Buying Techniques #43".
- Coined framework names: "3A", "EPIC", "grand slam", "Concept vs Angle vs Iteration vs Variation" as a named taxonomy, "5 Levels". Describe the ideas instead.
- Alessio's four-stage awareness labels (indifferent / frustrated / open / ready) are his vocabulary; if the article shows an awareness field, use generic Schwartz-style levels or "awareness stage" without his labels.

## 8. Draper angle
- **Automatic ad naming**: every ad inherits its name from the creative file, editable in one place before launch (`profiles/draper-ads.md` §Features). The panel's strongest operational idea is that one string should follow the creative from brief to file to ad name. If your file names carry the convention, Draper carries it into Ads Manager without anyone retyping it, which removes the failure mode where people type names by hand and stop filling fields.
- **Smart UTM management**: define the UTM structure once. Pairs naturally with the "naming, post IDs and UTMs are one identity layer" point (Marin, `naming-conventions.md` §5).
- **Create once, deploy many**: the same ad going to many ad sets keeps one name, instead of "- Copy" chains from duplicating.
- Keep within the profile: Draper does **not** claim to parse, validate or enforce a convention, or to name campaigns and ad sets. Don't say it improves performance; it removes manual work and naming drift. One CTA at the end; optional inline mention at the "generate the name from the file" point.

## 9. Open questions
- Ads Manager's current ad-name length limit and inline-edit behaviour (Meta docs) — the corpus only has one complaint, 2025-02.
- Whether the article should show one full worked example per level. Recommended: yes, a three-row table (campaign / ad set / ad) using neutral, invented tokens, plus a "lean" and a "rich" ad-name variant.
- `[TK]` candidate: a Draper screenshot or first-hand example of a file name becoming an ad name. No usage numbers exist; don't invent any.
- No expert addresses naming for Advantage+ / flexible-format ads where Meta mixes assets inside one ad; worth a one-line caveat only if Meta docs confirm the behaviour.
