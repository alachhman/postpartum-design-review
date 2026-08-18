# Design Research — Postpartum Weight & Wellness App

*Compiled August 17, 2026. Companion to `02_MVP_Design_Brief.md` (source of truth) and `04_Style_Guide.md` (visual direction).*

**Authority note.** The brief is locked on product decisions and this document does not relitigate them. The style guide explicitly invites refinement of palette and type, and §4 takes that invitation with contrast math. §1 flags places where evidence contradicts a stated premise — those are for the founder to accept or reject, not design-side decisions.

**Evidence base.** Four research streams: nutrition/calorie-tracker UX, maternal/postpartum/femtech UX, cross-domain design, and a Reddit qualitative pass (§0A). Primary sources were App Store metadata and verbatim customer-review corpora (`itunes.apple.com/lookup` and the customer-reviews RSS), live CSS harvests of competitor sites, published product documentation, peer-reviewed literature via PubMed/Europe PMC, and ~35 Reddit threads read in full with comments. Where a claim could not be verified it is marked **[unverified]**.

**A note on §0A.** The first three streams were run without Reddit access (403 on automated fetch), which left the largest hole in the research — this audience does its actual thinking in public there. The Reddit pass was added afterwards via a rendered browser session, and it overturned or sharpened several conclusions. Where it does, the earlier section carries a pointer. §0A.7 is the summary of what changed.

---

## 0. The ten things that should change

Ordered by how much they alter the current design. Items 8–10 came from the Reddit pass (§0A) and are the ones most likely to be uncomfortable.

1. **Invert the headline number.** Not "1,460 remaining" but **"Still to eat today: 550."** Simple's Safe-to-Spend is the only mainstream product that ever solved this inversion, and it solved it by changing the arithmetic, not the chart. §2.4.
2. **Draw the floor as a region, not a line.** A hairline radial tick invites knife-edge anxiety and is hard to label. Every working precedent — Dexcom's AGP, Gentler Streak's Activity Path, MacroFactor's maintenance dial — renders the safe state as a *band* with a dead zone. §2.5.
3. **Encode state in geometry, not hue.** Baby-tracker users report that amber and yellow icons are indistinguishable in dark mode and that thin red graph lines vanish. A sage/amber/coral banner is a documented failure mode at 3am. §4.5.
4. **The supply verdict must be self-referential, never normative.** KellyMom — the clinical authority the target user already reads — states plainly that pump output is *not* a valid measure of supply. "Compared to your own last 7 days" survives that critique. "Compared to typical" does not. §3.
5. **Ship user-declarable suspension states.** Oura's Rest Mode and Gentler Streak's illness/injury/vacation statuses converged independently. Yours: *baby is sick, I'm sick, cluster feeding, travelling.* Suspends floor-miss accounting, preserves the streak, changes the copy. §6.4.
6. **Drop three unverified claims from the pitch and the copy.** "23 minutes to refocus" is not in the paper everyone cites. Red-shifted night mode has no melatonin evidence. Clue's "award-winning" status has no retrievable record. §1.
7. **Fix the amber.** Amber 600 `#C98A2D` on Cream is **2.75:1** — it fails even the 3:1 floor for graphical objects, and 2.57:1 on its own tint. The supply-dip state is currently the least legible thing in the system. §4.1.
8. **Design for *decreasing* daily interaction.** Your competitor is not another tracker — it is **abandonment**. She quits logging at 2–8 weeks and calls it a mental-health win, with community backing. A calorie ring *plus* a daily check-in is two daily obligations imposed on a population organising to quit logging. §0A.2.
9. **Build a graceful story for flat-or-rising weight.** A large, loud cohort **gains** weight while nursing. A product whose loop is "stay above the floor and the weight comes off" fails them by design. §0A.5.
10. **Put the clinical credential in front of the paywall, not behind it.** Credentialing — not features — is the axis on which this audience decides whether to pay for nutrition advice, and they have been burned. §0A.4.

---

## 0A. Addendum — Reddit field evidence

*Added after the initial draft. Reddit was inaccessible to the first three research passes and was the largest gap in the document; this section closes it. ~35 threads read in full with comments, across r/breastfeeding, r/beyondthebump, r/NewParents, r/ExclusivelyPumping, r/Mommit, r/loseit, r/1200isplenty, r/Myfitnesspal, r/workingmoms. Upvote counts are given so consensus can be distinguished from outliers.*

### 0A.1 The best news in this document: the floor is already installed

You are not teaching a concept. You are **arbitrating a number.**

The floor exists in the wild as a folk model, stated unprompted, with exactly the structure you are building — a number below which you must not go, *because of the baby*:

> "My understanding is that <1500 calories can drastically affect your milk supply." — 19↑, Nov 2025
> "I was advised not to eat under 1500 calories a day." — Feb 2024
> "you dont wanna eat below 1800" — Nov 2025

The number varies (1500 / 1800 / 2000); the mental model does not. This substantially de-risks the onboarding and makes the target-preview screen more valuable than the brief assumed — its job is to *settle an argument she is already having*, not to introduce an idea.

It also has **cross-ideological legitimacy**, which is rare. r/1200isplenty — the most restriction-tolerant sub on Reddit — enforces the floor for nursing members: *"restricting at all killed my supply (and I had plenty)"* (26↑). Even people who have opted into aggressive restriction carve out this exception.

**Design consequence:** soften §2.3's emphasis on explaining the floor concept. The inline "What's the floor?" affordance is still needed — but for the *ring geometry*, not the idea. What she wants explained is **why your number differs from the one she read on Reddit.**

### 0A.2 Your competitor is abandonment

The Notes-app hypothesis is **partially wrong**. Notes, paper and whiteboards are real but a minority; Huckleberry's free tier dominates. The actual competitive set, in order:

1. **Huckleberry free tier** — *"Huckleberry is great but premium is overkill"* (19↑)
2. **Quitting entirely** — the dominant outcome
3. MyFitnessPal with a hacked-up goal
4. Notes / paper / whiteboard

Quitting is not passive drift. It is a deliberate, celebrated, community-endorsed decision, and there are at least six separate high-engagement threads asking *when can I stop*:

> "All of the tracking apps are your enemy." — **252↑**, top comment on a 180↑ post, Jun 2026
> "I stopped tracking everything… it was one of the best things I did for my mental health." — 40↑
> "Am I the only one that absolutely hates baby tracking apps? I've tried a few and they're all data overload." — 94↑
> "Some ppl find data calming and some find it anxiety inducing. If you're the latter then skip it." — 30↑

Typical stopping point: **2 weeks to 2 months**, usually pegged to a pediatrician weight check.

There is also active **log falsification** to reduce anxiety:

> "Every day, multiple times a day, I have to remind myself that if the time spent feeding is off by seconds/minutes, it DOES NOT MATTER." — 180↑
> "I lie most of the time though so as long as I know what time I started I just go eeeehhhh reset to 20 minutes." — 55↑

**Design consequences, and these are significant:**

- **A precise numeric floor displayed against a precisely-logged intake is the interaction pattern she is describing as harmful.** Prototype a low-precision input mode — *roughly enough / not sure / definitely not enough* — as a first-class alternative to gram-level logging. This pairs naturally with the numbers-off mode in §8.2-J, which should now be considered core.
- **The product should ask for less over time, not more.** A tracker that gets quieter as she stabilises is a genuinely differentiated proposition in this category and directly answers the stated reason for quitting.
- The 7-day smoothed weight trend is your safest surface: one input, a week of signal.
- **The one thing that keeps an app alive past week six is shared state with a partner** — *"my wife asking 'when did he last eat and how much' caused so much anxiety"* (34↑). You have no partner story. That is the incumbent's retention hook and it is worth deciding deliberately whether to cede it.

### 0A.3 The MyFitnessPal hack, precisely — and it is broken

Three distinct workarounds exist and users disagree about which is right:

- **Negative-calorie food entry** — log "breastfeeding" as a food worth −500. The folk-famous one: *"there is also a 'food' option for breastfeeding that was like -500 calories."*
- **Custom exercise entry** — fragile: *"if you use a tracker like Fitbit, then this won't work because your tracker will override it."*
- **Lie to the app** — set the goal to maintain, or overstate activity, and let nursing create the deficit invisibly: *"I have it set to maintain weight and then I let my breastfeeding calories make a deficit."*

**The negative-food method has quietly stopped working.** A mother returning for her second baby, Jun 2026: *"When I had my first almost four years ago, you could enter breastfeeding as a food under calories and it would add calories to your daily goal."* The thread has four comments and no resolution. The 2016 threads describing the old method still rank in search.

Two things follow. First, **every one of these workarounds raises a ceiling; none creates a floor.** Nobody has a tool that stops them going too low — the hacks exist to stop the app *under*-feeding them, which is the same need stated in the opposite direction. Second, there is a live, high-intent, unserved search query here — women following stale advice into a dead end. That is a distribution opportunity as much as a product one, and it is cheap: write the replacement guide.

Adjacent, and worth noting for the Trends screen: *"Looking at my Apple fitness, it honestly drags me down"* (in a 37↑ thread titled "Petition to have breastfeeding included on fitness apps"), and Fitbit *"still doesn't have a pregnancy and postpartum option so it keeps telling me my next predicted period is today"* (6↑).

### 0A.4 What she believes, who she trusts, and what unlocks payment

The dominant belief is a **500/500 coincidence heuristic** repeated near-verbatim across years and subs: nursing burns ~500 kcal/day, 1 lb/week needs a 500 kcal/day deficit, therefore nursing *is* your deficit and you should cut nothing.

**Sourcing is peer-to-peer, not clinical.** Across the whole corpus: four mentions of IBCLC/LC/La Leche League, and **zero mentions of KellyMom.** What appears instead is active distrust of general clinicians on this specific question. To a woman whose GP said cutting calories was fine if she hydrated, the top comment by a wide margin was **"Oh my God get a new doctor"** (86↑).

The single most instructive thread is the **1300-calorie dietitian** case (66↑, 157 comments, Sep 2025): OP paid an Instagram "dietitian" for a personalised plan and was given 1300 kcal. The reaction:

> "Are you certain they are a registered dietitian? Because that plan sounds like the 💩 a nutritionist (unregulated and No education standards) would suggest." — **458↑**, top comment by 3×
> "I feel like 'Do not pay for medical advice from Instagram accounts' is a good rule of thumb." — 124↑

That thread proves three things at once: a too-low number triggers mass outrage; **credentialing is the axis on which they judge a paid nutrition product**; and they *will* pay for this and then get burned.

**On pricing.** Postpartum spending is discussed mostly as regret — *"I regret so much of the money I have spent during pregnancy"* runs to 1917↑ and 534 comments, with self-aware asides about being a marketing target. Observed price points: Baby Daybook $5/mo (paid, positive); Huckleberry premium rejected as "overkill" and bought only at 50% off; lactation consultants discussed via **insurance coverage**, not cash price. They pay real money for hardware and human expertise — SNOO at ~$1,700 is debated seriously — but they price it as **a bet on fit, not a subscription**, and immediately look for rental or resale. Nobody in the corpus expressed willingness to pay a recurring fee for reassurance.

$79.99/yr is roughly 1.3× a rejected Huckleberry premium, in a category this audience has been burned by. **The credential is the pricing lever, and it must be visible before the paywall.** The brief already puts the plan reveal before the account wall; put the named RD/IBCLC there too.

### 0A.5 Two things that will break the current design

**A large cohort gains weight while nursing, and feels betrayed about it.** In an ExclusivelyPumping thread asking whether pumping helps with weight loss, the top comment is *"Lol no. Some of us lucky ones gain weight"* (161↑), followed by *"Pumping made me put on 15-20 lbs"* (40↑).

A product whose core loop is *stay above the floor and the weight comes off* actively fails these users, and they are vocal. The 7-day trend needs a designed, non-apologetic state for **flat or rising** — one that does not read as failure and does not immediately propose a bigger deficit. The floats-and-sinkers device (§8.2-B) helps here; the "days protected" metric (§8.2-D) helps more, because it is a win condition that does not depend on the weight moving at all.

**The emotional register is grief and surrender, not panic.** She has usually already tried and already quit:

> "Anytime I adjust my calories, my milk supply takes a huge dip. It's devastating." — 61↑
> "I tracked calories and would lose my supply if I cut back even like 100 calories." — 40↑
> "I don't know anyone who lost weight while breastfeeding that didn't suffer supply dips." — 24↑
> "I'm just going to be fat for a little while and that's OK. Right now to me breast-feeding is more important than losing the weight." — **60↑**

That last one is often the highest-voted comment in its thread. **This is a different onboarding than "she's about to start."** She is returning to something that hurt her. The target-preview screen should acknowledge the previous failure rather than presenting a fresh optimistic plan.

Note also the dissent: roughly 20–25% of comments in deficit threads report cutting 250–500 kcal with no supply effect, and nobody can predict which group they are in. The community says so explicitly — *"There's not a good way to know which type you are"* (3↑). That sentence is arguably your product thesis in one line, and it is a better headline than anything currently in the positioning.

### 0A.6 Her language — use these words

**What she says about her own body**, self-critical register (the vocabulary is strikingly consistent — *disgusting, foreign, stranger, hate, deflated*):

> "I'm 8 months postpartum, and I can't even stand to look at myself in the mirror. I hate the way I look, I'm disgusted by my body." — 514↑
> "I feel so foreign in my body." — 33↑
> "Still have around 30 lbs of extra weight, feel like a stranger in my own body." — 25↑

The **self-accepting** register is plain, tired and practical — *"I'm just going to be fat for a little while and that's OK."* It is emphatically **not** wellness-brand vocabulary. Nobody says "love your body," "honour your body," or "nourish." Adding those to the copy would alienate her as surely as diet-culture language.

**The functional framing she volunteers unprompted is the best onboarding copy in this entire document:**

> "I just wanna lose the weight because my knees can't take me bending down to pick up my heavy baby off the floor 100 times a day anymore." — 20↑

The highest-upvoted statement of motivation in the corpus is about **load-bearing capacity, not appearance.** Every brand in this space leads with how she looks. Lead with what she can carry.

**Can she say "weight loss" out loud?** Yes — but almost always with a defensive preamble, and this pattern is strong:

> "Hate to use the term 'bounce back' but I don't know how else to phrase this." — 346↑
> "I'll preface this with a TW as I'd like to talk about postpartum weight loss and understand this is a sensitive topic for some." — 55↑

She puts a trigger warning on her own weight-loss post. Meanwhile "bounce back" is under active community prosecution: *"Do we ever bounce back from age 30 to 28? … THIS TERM IS ILLOGICAL"* (44↑).

**So: you may name weight loss directly — but as her stated goal, never as your product's promise — and you should supply the permission structure she is currently improvising for herself.** The banned-lexicon list in the style guide is correct and confirmed.

**What makes her recoil** is narrower and more specific than "diet culture." Three separable triggers:

1. **Anyone else naming her body.** This produces the largest engagement in the dataset — a "husband asked me to lose weight" thread runs 563↑ / 542 comments; the highest-scoring single comment encountered anywhere in this research (**1079↑**) is a flat refusal to be diplomatic about in-laws suggesting weight-loss drugs.
2. **Paid advice that undershoots.** Treated as fraud, not error. §0A.4.
3. **Anything that smells like marketing.** *"I hate how everything is either an ad or feels like one and that makes me pull back from a lot"* (157↑), in a 1351↑ thread whose top comment is *"Nothing has helped my motherhood like getting off all social media"* (2043↑).

Crucially, **none of the recoil is triggered by weight loss as a goal.** Self-initiated weight-loss threads are welcomed and supported. The trigger is *who names it* and *whether the numbers are safe*.

There is also a dark-humour register worth knowing before writing any copy: *"I'm just one stomach flu away from my goal weight"* (266↑).

### 0A.7 Revisions to earlier conclusions

| Earlier finding | Reddit verdict |
|---|---|
| Pump output is not a valid supply measure (§1.1) | **Confirmed, with a twist.** The doctrine is well known and evangelised — the canonical thread is literally titled *"Pumping is not an indicator of supply!!!"* (170↑) — yet in every weight-loss thread, women report supply status in ounces pumped. This is a **behaviour gap, not an education gap.** Telling her again will not work. **Accept the pump number and reframe it** rather than refusing it. |
| No app states a supply verdict — would anyone want one? (§1.2) | **Confirmed, and demand is stronger than expected.** "How do I know if my supply tanked", "Am I starving my baby?" recur constantly, and the community's own answer is an admission that the verdict is unavailable. She is currently getting her verdict from strangers on Reddit at 3am. **This is the wedge** — but she will only accept a verdict from a source she believes is credentialed. |
| The real competitor is Notes / texting | **Partially contradicted.** Reframe: Huckleberry's free tier, then abandonment, then hacked MFP, then Notes. §0A.2. |
| Hostile to diet-culture framing | **Confirmed, but narrower than stated.** The hostility targets other people naming her body, unsafe numbers, and marketing gloss — not weight loss as a goal. Over-rotating into wellness-speak would alienate her equally. §0A.6. |
| Would she grasp a calorie floor? | **Yes, immediately.** Already installed as a folk model. §0A.1. |

---

## 1. Corrections to premises

These are evidence problems, not taste disagreements.

### 1.1 Pump output is not a valid supply metric — and your user knows that

Kelly Bonyata, IBCLC, on KellyMom, which is the single most-read lactation resource among this audience:

> "the feel of the breast, the behavior of your baby, the frequency of nursing, the sensation of let-down, or the amount you pump are not valid ways to determine if you have enough milk for your baby"

> "The amount of milk that you can pump is not an accurate measure of your milk supply."

The brief's check-in asks exactly these three things: feeds felt normal, pump output vs. usual, baby seemed satisfied. Clinically, none is a valid absolute indicator. **This does not kill the feature — it constrains the framing absolutely.**

- Safe: *"Your check-ins have been steady for 5 days"* — a statement about her reported experience over time.
- Unsafe: *"Your supply is good"* — a clinical claim the app cannot substantiate and an IBCLC advisor will strike.
- Unsafe: *"Your output is above typical"* — normative benchmarking, which is what the one existing competitor does and what KellyMom specifically warns against.

**Revised by §0A.7.** The Reddit pass shows this is a *behaviour* gap, not an education gap: the audience knows the doctrine well enough to evangelise it — the canonical thread is titled *"Pumping is not an indicator of supply!!!"* (170↑) — and reports supply in ounces pumped anyway. Refusing the number will read as the app being unhelpful. **Accept the pump figure, then reframe it** against her own baseline rather than a norm.

There is also an operational bias worth designing around, verbatim from a pumping-app user: *"my data… is skewed because I haven't had the energy to follow this step when I pump in the middle of the night."* Missing check-ins correlate with the hardest days, which means naïve trend logic will read exhaustion as improvement.

### 1.2 "Supply status" is near-novel — but the window is closing

Prior-art verdict:

| Capability | Prior art |
|---|---|
| Logging ounces pumped | Universal commodity |
| Charting output over days/weeks | Common — 10+ apps |
| An app **stating a verdict** on supply | Near-zero — one product |
| A named "supply status" banner / stoplight | **Zero instances found** |

The one competitor: **Pump Coach: Pumping Tracker** (App Store id 6765497176, Clarks Condensed LLC / The Breastfeeding Mama), released **August 3, 2026 — two weeks ago — with three ratings.** IBCLC-built, with an IBCLC client dashboard. Its store copy:

> "Today's output at a glance, with your daily goal front and center • 7-day trends, session quality scores, and output-per-hour compared to typical • Find your best time of day and most productive pump settings • Insights written for real life — encouraging, not anxiety-inducing."

Four things to note. It **scores sessions** and benchmarks **"compared to typical"** — the normative move that fails §1.1. It is **defensive about tone in its own store listing**, which tells you the founder already knows this is the risk. The verdict layer is **paywalled**. And it has an IBCLC distribution channel, which is your channel too. Treat it as a real competitor for the positioning even though it is executionally tiny.

Also relevant: **LactApp** (id 1040787494) already ships a question-driven flow with a verdict card titled *"LactApp responds"* — tailored questions against 2,300 stored answers. It has no supply chart and no score, but the *interaction pattern* of your check-in is not new to this audience.

### 1.3 "23 minutes to refocus" is not a real finding

The figure is universally attributed to Mark, Gonzalez & Harris (2005). It is not in that paper. The actual number is **25 min 26 sec (sd = 54 min 48 sec)** and it measures *elapsed wall-clock time before returning to a "working sphere"* — not a cognitive refocus cost — in N=24 workers at one financial-IT firm.

What the literature actually supports:

- **Mark, Gudith & Klocke (2008)**, N=48: interrupted work was completed *faster* (22.77 → 20.31 min). The cost is affective — stress 6.92 → 9.46, frustration 4.73 → 6.63. Crucially, **interruption context did not matter**, which kills the intuitive "it's a baby app, so a baby interruption is fine" argument.
- **Monk et al. (2008)**: resumption lag **1,548 ms** vs. 949 ms baseline — a real cost of roughly **600 ms**, with the disruption curve asymptoting **between 13 and 23 seconds**.

**Design implication.** The cost of interrupting her is emotional, not temporal, and the recovery window is ~15–20 seconds. That is a strong argument for the sub-10-second interaction target already in the brief, and a strong argument that state preservation matters more than speed. Remove the 23-minute stat from any deck.

### 1.4 Red night mode has no evidence behind it

- Chang et al. (2015) found 55.12 ± 20.12% melatonin suppression but conceded the effect *"may be due to the difference in irradiance level rather than spectral composition."*
- Nagare et al. (2019): Night Shift interventions **did not significantly differ**.
- Duraccio et al. (2021), RCT n=167: **no sleep-outcome differences attributable to Night Shift.**
- Phillips et al. (2019): individual sensitivity (ED50) ranged **6 lux to 350 lux — a ~58-fold spread.**

**Supported:** reducing total emitted light. **Not supported:** that an amber or red colour shift does anything on its own. Build the dim mode — just never market it as protecting her sleep hormones. The defensible resolution is: dark surface, **20pt minimum type**, Dynamic Type to AX5, and near-white foreground at **7:1 (AAA)** — never dim-grey-on-black, which is the actual legibility failure in this category.

### 1.5 Smaller corrections

- **Clue's "award-winning" status is unconfirmed** — no Red Dot, iF, D&AD or Webby record found. Clue's identity was also **in-house, not agency work**. Cite Clue for its philosophy, not its trophies. **[unverified]**
- **Frida Mom's identity is in-house**; no agency case study exists, and the Oscars ad is **wordless** — no voiceover. **[unverified]**
- **Dawson & Reid (1997)** does not contain the "17 hours awake ≈ 0.05% BAC" numbers. Cite **Williamson & Feyer (2000)** instead.
- **"The Fifth Trimester" is not a Peanut campaign** — it is Lauren Smith Brody's book.
- **Canopie has no peer-reviewed RCT** — a self-published N=100 study, Hedges g = 0.68.
- **No app anywhere was verified to publicly say "we don't do streaks."** If that claim appears in positioning, it is unproven.
- **Microsoft's Persona Spectrum "holding a baby" row could not be verified verbatim** — it exists only inside an image-rendered PDF. Open it visually before quoting it. The verified principles (*"Recognize exclusion," "Solve for one, extend to many"*) make the same argument safely.

---

## 2. The central design problem: the floor

### 2.1 You are inverting a metaphor 200 million people have already learned

MyFitnessPal's home number is **Remaining**, computed as `Goal − Food + Exercise = Remaining`, with the explicit stated intent that *"at the end of the day, Remaining Calories should approach zero."*

The entire mainstream mental model is **drain-to-zero**. Yours is **fill-to-safe**. You cannot reuse the visual grammar of depletion — a ring emptying, a number counting down, red on exceed — without importing the wrong instinct along with it.

A second trap in the same formula: MFP *adds exercise calories back* as spendable credit. Lactation costs roughly 500–700 kcal/day, but it is involuntary. If you ever surface *"breastfeeding earned you 500 cal,"* you have rebuilt the exercise-credit loop that users already distrust as double-counting — and that the ED literature (§10) identifies as a mechanism of harm.

### 2.2 MFP already has a calorie floor. It is the exact anti-pattern.

MFP warns when a completed day falls under ~1,000 kcal. Users experience it as scolding:

> "It reprimands you if you go under 1000 calories for the day which is ridiculous" — 2★

And the inverse complaint, which is your product thesis written by a stranger:

> "your caloric intake should not be below your BMR… years ago in the beginning of my weight loss journey the calories goals had me at 1100 calories and I found out my BMR was closer to 1400. This had a profound effect on my mental health and weight loss. I had chronic fatigue and anxiety. It was awful. **There was no warning about consuming lower calorie and being in starvation. There was no place I could add a BMR so the app would take that into account.**" — 3★

> "the team needs to do more work into finding an appropriate caloric amount for goals (it's far too low and leads to an ED mindset)." — 3★

Four failure modes to invert deliberately:

| MFP's floor | Yours |
|---|---|
| Invisible until the day closes | Live on the primary gauge all day |
| Retrospective | **Predictive** — fires when the projected day will land under |
| A hardcoded global constant (1,000) | Individualized: BMR + lactation load + weeks postpartum + feeding mix |
| Expressed as a reprimand | Expressed as a remaining obligation |

### 2.3 The unlabelled-arc problem

The most useful single verbatim in the corpus, from a *paying* MFP subscriber, 2★:

> "Look at the dashboard. The middle third of the screen has a mildly useful chart. Bottom third is an ad. The top third is some strange progress bar, I guess, but it's **curved for some unknown reason, and no indication what progress is being represented.** Progress toward me deleting the app?"

A Premium user could not decode MFP's calorie arc. Yours carries a *second* semantic on the same geometry. Two consequences:

- The floor needs a **persistent adjacent text label**, not a legend and not an onboarding explanation.
- Ship an inline **"What's the floor?"** button next to the ring. This is Gentler Streak's published lesson about their own non-standard boundary metaphor: *"when people discover it and it clicks what it does, it becomes a hero feature"* — so they added a permanent inline explainer button rather than relying on onboarding.

**Revised by §0A.1.** The *concept* needs less explaining than assumed — the floor already exists as a folk model in this audience, with people quoting 1500 / 1800 / 2000 unprompted. What the explainer must actually answer is narrower and more urgent: **"why is your number different from the one I read on Reddit?"** Point it at the arithmetic, not the idea.

### 2.4 The strongest idea in this document: subtract the floor out

Simple's Safe-to-Spend showed **balance minus scheduled bills, minus goals, minus pending** as one number that was already protected. The coverage explains why it worked: *"the app only presents the Safe-to-Spend amount — not an available balance… making sure the consumer doesn't spend money they would rather not spend."* When it shut down in 2021, users wrote elegies: *"the first financial tool that felt like it was designed for them rather than against them."*

The trick is that **it reframed the arithmetic, not the chart.** It never drew a floor line; it subtracted the floor out of the headline number.

Applied here:

> **Instead of** "1,460 remaining · Floor: 1,800 — you're safely above it"
> **Show** "Still to eat today: **550**"

The number counts down to zero and **stops**. Zero is the win state. There is no negative, no exceed, no red. Above zero the copy becomes a stable positive terminal state — *"You're above your floor."* You cannot feel bad about overspending a number that only measures what you still owe yourself.

This is worth prototyping as the **widget, Lock Screen, and Watch complication variant** even if the ring stays the in-app hero. It is the single highest-leverage idea here, and it comes from the only product that solved this inversion commercially.

### 2.5 Ring vs. bar — and why the floor should be a band

| | Ring / arc | Horizontal bar |
|---|---|---|
| Reads in ~1s | Strong | Strong |
| Big centre number | Native | Awkward |
| Marking an internal threshold | **Weak** — a radial tick is hard to label and reads as a needle | **Strong** — a vertical tick with a label beneath is unambiguous |
| "Fill toward safety" affordance | Strong (Apple Activity rings) | Medium |
| Zone shading | Good as arc segments | Excellent |
| Thin-stroke legibility in dark mode | **Weaker** | Better |

Note that Apple's Activity rings are the *right* ring precedent and MFP's remaining-calories ring is the wrong one: "close your rings" is already a fill-to-goal, minimum-achievement metaphor with no ceiling and no failure-by-exceeding, understood by hundreds of millions of people.

**Recommendation — hybrid.**

- Keep the ring as the emotional object with the number in the centre. Users explicitly praise this on the Watch: *"circles showing how much portions are remaining at the center, and a line around the circumference to portray how much you have consumed"* — and note they describe it as **filling**.
- Render the below-floor region as a **filled arc sector in a distinct treatment**, from 0° to the floor angle — a zone the fill has to cross out of — not as a hairline tick.
- Make the safe state a **band, not an edge**: "your protected zone: 1,800–2,300." A single line invites just-above anxiety. MacroFactor's shipped maintenance dial uses exactly this — an Under / OK / Over gauge with a **±1.5 lb dead band** driven by trend weight, with crossings triggering a small proportional correction rather than an alarm.
- Add a **linear floor bar as the compact representation** (widget, complication, notification), where a labelled tick is legible.
- On crossing the floor, **invert the fill treatment** rather than switching to green. MacroFactor does this on its target bars — the fill flips to black in light mode, white in dark. Cheap, colourblind-safe, dark-mode-safe, and it does not read as diet-culture reward.

### 2.6 Three specific traps

- **Never use red below the floor.** Dexcom can use red because a hypo is an acute emergency; under-eating by 200 kcal on a day she could not control is not. Below-floor should be desaturated and quiet.
- **Never let the ring complete and keep going into an over-state.** There is no meaningful penalty at the top. A soft, unpunished ceiling or none at all — otherwise you re-teach the exceed instinct.
- **Never show a negative remaining number.** MFP's core failure state is a red negative "Remaining." Yours goes to zero and stops.

### 2.7 The four precedents worth studying directly

**Dexcom / AGP** — the closest existing analogue, and it is a *dual*-threshold display. Target range 70–180 mg/dL rendered as a **shaded band spanning the full chart width**, a red line at the low limit, an orange line at the high, separate day/night ranges, and tiered lows (70 = low, 55 = urgent low). Endorsed in ADA Standards of Care rec. 6.4. Two things to steal:

- **Predictive breach beats retrospective breach.** Dexcom's *"urgent low soon"* fires when the value is falling fast, not after the breach. Your nudge should fire at 4pm on a projection, not at 11:59pm on a fact.
- **The percentile ribbon.** AGP plots a median line inside a dark 25–75th ribbon inside a lighter 5–95th ribbon. The ribbon **narrows when you're consistent and fattens when you're erratic** — a progress story that doesn't require the number to move. Far kinder than a single line for a user whose intake variance is largely outside her control.
- **"Time in Range" as the headline retrospective.** *"You were above your floor 26 of the last 30 days"* is robust to one bad day, matches the biology (supply responds to sustained intake, not any single day), and is a metric clinicians already recognise.

**MacroFactor's micronutrient model** — the language is already written for you:

> "Micronutrient goals in the app consist of a **target and a goal range that is determined by a floor and a ceiling.**"
> "**The floor serves as a practical minimum to stay above.**"

"A practical minimum to stay above" is close to finished UI copy.

**Gentler Streak's Activity Path** — a horizontal corridor through time with over- and under-corridor states, three zoom levels (Daily Readiness / 10-day / 30-day), and a live *"countdown to overreaching"* on the Watch. Named states rather than scores: *"You are Spot On," "Just What You Needed," "State of Extra Recovery," "Overreaching."* Apple Watch App of the Year 2022.

**Simple's Safe-to-Spend** — §2.4.

---

## 3. Supply status — the moat, and how to render it

### 3.1 What to put in the banner

Given §1.1, the banner is a statement about *her own reported trend*, phrased as observation rather than verdict.

- Steady: **"Steady — 5 days of check-ins in your usual range."** Subtitle from yesterday's answers.
- Dipping: **"Two days below your usual."** Then the reason, then the action.
- Escalation: **"Four days now. This is worth a chat with your IBCLC."**

Note the grammar: *your usual*, never *typical*, never *normal*, never *good*. This is the difference between a defensible wellness claim and a clinical one, and it is also the difference between your positioning and Pump Coach's.

Borrow Natural Cycles' third state. It is the **only app in the entire study with an explicit insufficient-data colour** — brown, for "more data is needed" — and its engine *defaults to the safe state* when it lacks information. You need this: a named **"Not enough check-ins to say"** state that is neither steady nor dipping and does not silently read as fine.

### 3.2 Phrase the check-in questions the way Oura phrases contributors

Oura labels each Readiness contributor with the *question it answers* rather than the metric it measures — *"How well did I sleep last night compared to normal?"*, *"Did I balance my activity, inactivity and rest yesterday?"* Lift this wholesale: each of your three taps answers a named question rather than entering a datum. It also quietly reinforces that the input is subjective report, which is exactly what §1.1 requires.

Oura's anti-perfectionism copy is also directly transferable: *"100s are designed to be rare rather than regular"* and *"these contributors are less about improving or aiming to hit a certain benchmark and more about being in touch with what your body needs."*

### 3.3 Timers are a trap — and skipping them is a real advantage

The brief already excludes nursing/pumping timers from v1. The review corpus strongly validates that. Forgetting to stop a timer is the single most-complained-about interaction in baby trackers, and **no app in the set advertises auto-stop or a duration cap**:

> "I tend to forget to stop the sleep tracking… A prompt when I am starting to log feedings or diapers might help."
> "And why don't they cap the timer!"
> "the timer never stopped… I don't know how long I fed."
> "on the watch, if you hit back it cancels it. So many lost sleep tracks!"

A timer-free, event-stamped 3-tap check-in sidesteps the entire class of failure. Say so in the App Store copy.

---

## 4. Colour

### 4.1 Contrast audit of the current palette

Computed WCAG 2.1 ratios for the tokens in `04_Style_Guide.md`:

| Pair | Ratio | Verdict |
|---|---|---|
| Ink `#2B2B28` on Cream `#FAF7F2` | **13.29:1** | Excellent — AAA |
| Ink-soft `#6B6A64` on Cream | **5.08:1** | AA body text ✓ |
| Coral 600 `#C4573B` on Cream | **4.12:1** | Graphical ✓ · body text ✗ (needs 4.5) |
| Sage 600 `#5C8D76` on Cream | **3.56:1** | Graphical ✓ · **body text ✗** |
| Amber 600 `#C98A2D` on Cream | **2.75:1** | **Fails everything, including the 3:1 graphical floor** |
| Amber 600 on Amber 100 `#F8EFDD` | **2.57:1** | **Fails badly** |
| Sage 800 `#3D6353` on Sage 100 `#E8F1EC` | **5.86:1** | AA text ✓ — the steady banner is fine |
| Dark: Sage `#7FA893` on `#211F1C` | **6.20:1** | Good |
| Dark: Text `#EDEAE3` on `#211F1C` | **13.68:1** | Excellent — exceeds the 7:1 AAA target |
| Dark: Text `#EDEAE3` on surface `#2C2A26` | **11.92:1** | AAA |

*Ratios computed to WCAG 2.1 relative-luminance formula and verified programmatically.*

**Two required fixes.**

1. **Sage 600 cannot be a text colour on cream.** At 3.56:1 it is fine as the active ring stroke and fine for ≥18pt/24px display type, but any 17pt body or 15pt secondary text set in sage fails AA. Add a **Sage 700 `#456B59`** for text-on-cream use — **5.61:1**, passes AA.
2. **Amber 600 must be darkened for anything but large fills.** Recommend **Amber 700 `#8F6111`** — **5.06:1** on cream, **4.73:1** on Amber 100. Both pass AA. Keep `#C98A2D` only for large fills and banner backgrounds where nothing sits on top of it.

The dark palette is in good shape and already meets the 7:1 the night-legibility evidence argues for. The steady-state banner (Sage 800 on Sage 100) also passes cleanly — it is specifically the *dip* state that fails, which is the state that most needs to be read.

### 4.2 The generic-wellness risk — worth taking seriously

Anthropic's own `frontend-design` skill names the three aesthetics AI-assisted design converges on. **The first one is warm cream `#F4F1EA` + high-contrast serif + terracotta accent.** Your canvas is `#FAF7F2`. That is not a coincidence — it is the attractor.

The competitive picture makes it worse. Palettes measured from live CSS on August 17, 2026:

- **Bodily** — forest `#005133`, ivory `#FFFAF0`, greige `#F0EDE8`, mint `#C6E6D7`, terracotta `#E8946F`
- **Expectful** — greige `#F0EFEC`, forest `#21342B`, chartreuse `#C1D96A`
- **Hey Jane** — cream `#FEF2E6`, periwinkle `#CCDDFF`, coral `#F79672`
- **Motherhood Center** — ivory `#FFF9F4`, navy `#102C4E`, peach CTA `#F7A688`

The convergent formula across the entire category is **warm cream ground → deep navy or forest text → one warm accent for action**. Sage-on-cream is squarely inside it. You will be legible and inoffensive and indistinguishable.

Three ways out, in increasing order of risk. Pick one — the point is to have *a* deliberate deviation:

1. **Shift the accent off sage.** Clue's move is instructive: Marta Pucci, *"It's red, not pink. A strong seed of life that's not flowerish or super girly."* Clue's `#A80014` is oxblood — warm, serious, unmistakably not-wellness. A deep oxblood or a dark ochre as the primary action colour, with sage demoted to the steady-state tint, would read as considered rather than generic.
2. **Shift the ground off cream.** A warm greige or a very pale clay rather than cream. Small change, meaningful differentiation.
3. **Let the palette follow the clock.** §4.4.

Also worth noting from Clue: **they do use pink-adjacent tints** (`#FFEEEB`, `#FFDBD6`) as card backgrounds. The rule was never "no pink" — it was "not pink as *identity*." The style guide's blanket ban is slightly over-tight; pale warm tints as surfaces are fine and Clue proves it.

### 4.3 The "not pink" trap has two siblings

Pili Laviolette (Random Pattern Studio) names three traps, and the second one is the one you are closest to falling into:

> "**Pink isn't the problem. It's the pattern.** The issue isn't using colour, it's relying on the stereotypical meaning behind it."

- **The Pink Trap** — flowers, pastels, infantilising. You have avoided this.
- **The Clinical Trap** — *"sterile palettes… works for investors and healthcare partners, but it can alienate users who need empathy as much as evidence."* Your positioning leans hard on clinical credibility. This is your real risk.
- **The Empowerment Trap** — *"bold fonts, loud taglines… can feel performative or even intimidating."* Frida Mom lives here, and it cost them: February 2026 Forbes backlash over packaging copy, pulled pages, a 1M+ view TikTok.

Her conclusion is the right brief: *"The goal isn't to reject pink or softness or science. It's to use them intentionally."*

Michelle Kennedy of Peanut, on the same theme: *"When a woman becomes a mother, she doesn't automatically lose her appreciation for design"* — arguing against *"icons that scream motherhood, such as prams or a rattle."* Your style guide's no-storks-no-cartoon-babies rule is well-founded.

### 4.4 Let the palette follow the clock

**Tide Guide** won the 2026 Apple Design Award for Visuals and Graphics, and Apple's citation names exactly one technique: *"The app's palette is even designed to match the color of the sky throughout the day."*

That is your 3am answer, and it is better than a light/dark toggle:

- **Day** — warm off-white ground, sage accents, full contrast
- **Evening** — warm dusk, reduced luminance
- **2am–5am** — deep warm charcoal (never `#000`), amber-shifted, low total luminance, with the floor line in a dim amber rather than a saturated alert

The reasoning is defensible on legibility grounds alone (§1.4): what helps is reducing *total emitted light*, and a time-driven palette does that continuously rather than in one step. A pure-black OLED UI with a red below-floor indicator at 3am reads as a medical alarm to a sleep-deprived person holding an infant.

### 4.5 The colour-coding failure that will bite you

Direct from baby-tracker reviews, and this is the most actionable finding in the maternal research:

> "Currently those icons are yellow and orange which are so similar in dark mode I almost tap the wrong one every time"

> "Dark mode doesn't use a very good color palette… It's hard to use the app in dark mode."

> "the red on the graphs barely show as a thin line"

Your supply banner is currently **green = steady, amber = dipping**, and your ring states are **sage / amber / coral**. In a desaturated dark palette at low brightness, sage and amber converge. This is a documented, repeated, real-world failure in exactly your users' hands.

**Encode state redundantly:**

| State | Hue | Geometry | Position | Icon |
|---|---|---|---|---|
| Steady | Sage | Solid fill, full-width band | — | Filled shield |
| Dipping | Amber 700 | **Dashed / hatched** band, inset | — | Outlined shield |
| Below floor | Desaturated | **Sector notch** on the ring | Distinct | Half-filled |
| Not enough data | Neutral | **Ghosted outline** | — | Dotted |

Gentler Streak enumerates support for *"bold text, dynamic type, reduced transparency, increased contrast, motion adjustments, and voiceover"* — including **Differentiate Without Color**, which a hue-only floor line fails outright. Peanut declares Dark Interface / Differentiate Without Color / Reduced Motion. **Ovia declares none.** Be in the first group.

---

## 5. Typography

The style guide specifies SF Pro Rounded with Nunito as fallback. Two observations.

**SF Pro Rounded is the safe, correct, invisible choice.** It signals iOS-native, it's warm without being cute, and it will never be the reason someone doesn't trust the app. It is also what every competent iOS wellness app uses, which means it contributes nothing to differentiation.

What the competition does — measured live:

| Brand | Display | Text |
|---|---|---|
| Bodily | **Louize** (Blaze) 400/~40px | Apercu (Colophon) |
| Expectful | **Teodor** (Newlyn) 300, 52px, −1.04px tracking | Inter |
| Clue | **TT Commons** | **Mrs Eaves XL Serif** |
| Canopie / Hey Jane | DM Serif Display | Mulish / Libre Franklin |
| Mahmee | Recoleta | Lato |
| Frida Mom | GT Walsheim, h1 800/60px UPPERCASE | GT Walsheim 700 |

Clue's pairing rationale is the most instructive: **"geometric sans for data, literary serif for knowledge."** That maps precisely onto your two content types — the numbers she checks in three seconds, and the explanations that earn her trust. Frida is the cautionary case: body copy at weight 700 is, in the researcher's phrase, *"the typographic equivalent of being yelled at encouragingly."*

**Recommendation.** Keep SF Pro Rounded for all numeric and UI surfaces — it is genuinely right for glanceable data and it gets you Dynamic Type and SF Symbols for free. Introduce **one editorial serif** for the explanatory layer only: the target-preview "here's the math" screen, the methodology page, the nudge headlines, the escalation copy. That is where trust is built and where the difference between "an app" and "a knowledgeable friend" is made visually.

**Night-mode floor:** minimum **20pt** type in the 2am–5am palette (not the 13pt general minimum), Dynamic Type support to AX5, and foreground at 7:1.

---

## 6. Layout and interaction

### 6.1 Thumb zones — use the 2017 numbers, not the famous ones

The widely-circulated thumb-sweep diagram is wrong, and UXmatters now carries an editor's note on the 2013 article calling it *"the well-known, but incorrect thumb-sweep chart."* Hoober's 2017 observational data:

- **75%** of users touch the screen with one thumb only
- **fewer than 50%** hold the phone one-handed
- **36%** cradle; **10%** hold in one hand, tap with the other
- Minimum target **7mm at screen centre**, **~12mm at the corners**
- **Carrying a bag** degrades corner accuracy to **over 30mm** — the postpartum case exactly
- Henze: error rises sharply below 15mm; **over 40% error under 8mm**
- Schildbach & Rukzio: **20mm targets solve almost all problems**

Hoober's conclusion contradicts naïve thumb-zone advice: **put primary clickables in the centre**, secondaries top and bottom, and design targets **20% larger** than you think you need.

NN/g's Aurora Harley wrote about this exact user and names **Glow Baby** as the failure case — a 6mm × <1mm scrubber, *"It took about 10 tries"* — while praising its **2.3cm-wide** nursing-timer targets. The concept she names is **view–tap asymmetry**: what is comfortable to *see* is not what is comfortable to *tap*.

**Resolution for home.** The infant-app convention is large controls at the top; the one-handed evidence says centre. Split them: **status display up top** (supply banner, ring), **actions in the centre and lower third** (log food, check in), nothing interactive in the corners. 44pt is the iOS minimum, not the target — aim for **20mm ≈ 56pt** on the check-in taps.

### 6.2 Logging friction — the specific complaints

Every one of these is a named MFP gap and a cheap differentiator:

| Pattern | Verbatim |
|---|---|
| Free-text portion entry | *"I wish you can choose the item and immediately write 1 cup or 100 g, 1 oz"* |
| Per-item favourites, distinct from recents | *"The ability to favorite individual items should be there… instead of having to scan the item again"* |
| Predictably sorted recents | *"the recent foods is not listed alphabetically"* |
| Editable quantity on a saved meal | *"sometimes I eat 2 eggs sometimes 4. Seems ridiculous to make that into two separate meals"* |
| No gratuitous confirm steps | *"when you go to login food now it asks you if you've already eaten the meal. Are you serious?"* |
| Barcode entry in a **fixed** location | *"Depending on which page you are on, the 'scan barcode' may be in a different place"* |
| Free barcode scan | The dominant churn driver — MFP paywalled it Oct 2022 and reviewers name Lose It! and Cronometer as destinations by name |

And the one that matters most for your architecture, repeated across four years of reviews:

> "There are only two things we need to do. **Log a weight for the day and quickly log food.** … The face page has extraneous information when it should present the two most important things… **Those should not be on separate pages.**" — 3★, May 2026

> "**You click about 8 times**… to finally get to the place to enter my weight." — 2★

Weigh-in and food entry belong on the same surface, both reachable one-thumb. And note the recurring bug class: *"today's update broke the ability to add today's weight. You tap on weight, and the little + in the top right corner no longer shows up."* **The top-right "+" is the wrong affordance** for this user, and it is fragile.

### 6.3 Interruption tolerance

She will be interrupted mid-flow. Per §1.3 the cost is affective and the recovery window is ~15–20 seconds, which means the design goal is **never losing state**, not speed.

**Nara Baby is the only app in the study with deliberate anti-interruption behaviour** — it *"keeps your phone unlocked and awake"* during a feeding timer and lets you leave the timer window without losing it. Everyone else's story is a bug report, and the worst class is **silent save failure**:

> "or worse, you don't realize it didn't save and your data is now inaccurate."

**Requirements:**

- Every multi-step flow (log, check-in, onboarding) persists after **every** step, not on submit.
- Returning after any interval resumes exactly where she left off, with a visible *"picking up where you left off."*
- Saves are confirmed visibly. A silent failure in a supply-tracking app is credibility poison — it is precisely what killed LatchFit's ratings.
- Never a destructive control that can't be undone. Huckleberry's finish-feed button is *"now too easy to accidentally press (by myself or my little one) and you cannot reopen a feed."*

### 6.4 Streaks — make them forgiving by mechanism, not by tone

The brief says "streak display, gentle." Gentleness of copy is not enough; the mechanic itself has to forgive.

Two award-winning apps converged independently on the same primitive:

- **Gentler Streak**: *"Keep your streak alive by following your body's needs, even when it calls for rest days. When life happens—be it illness, injury, or vacation—adjust your status to reflect real life and skip feeling guilty."* The streak measures **consistency of attention**, not performance, and users can declare life states that pause evaluation without breaking the chain.
- **Oura Rest Mode**: temporarily mutes the Activity Score and contributors when illness or life prevents meeting goals.

**Build the equivalent:** *baby is sick · I'm sick · cluster feeding · travelling · hospital.* Suspends floor-miss accounting, preserves the streak, and changes the copy. This is also the honest answer to the ED-risk problem (§10) — a streak that cannot be broken by circumstance cannot be used as a self-punishment instrument.

### 6.5 Nudges — the ethical gate and the shape

Gentler Streak's published rationale for their morning notification is the best statement of nudge ethics found anywhere in this research:

> "**The benefit: the app pays attention so you don't have to, and speaks up when yesterday has something to tell you about today.**"

Adopt that as the literal gate: **no nudge unless there is something specific in yesterday's data that bears on today.** Never a scheduled nudge. This also protects the brief's max-one-push-per-day budget.

For the shape of the full-screen moment, **one sec** is the most rigorously evidenced interrupt design in consumer software — PNAS 2023, CHI 2024, plus a Danish Competition and Consumer Authority field experiment. The user testimony explains why friction beats blocking:

> "Strict blockers never worked: I just turned them off. **The forced pause is critical to be able to consciously make the choice** though."

Its paid feature that matters most is **Healthy Alternatives** — interrupt *and immediately offer the substitute*. Combined with Gentler Streak's "Go Gentler" pattern, where each recommendation is shown **with a preview of how it moves your position on the gauge**, the supply-protect nudge becomes:

> Brief breath animation → *"You're 550 below your floor."* → three tappable food cards, **each showing how far it moves the ring** as a ghosted arc extension → "Not now," always present.

Never dismiss-only. Never a modal with a single OK.

**Do not copy Opal's reward layer** — a gem-collection ladder (First Gem, Determined, Driven, Committed, Balanced, Loyal, Soulful, Devoted, Unwavering Gem). A nursing mother at 3am does not want to earn an Unwavering Gem. It is a useful boundary marker for what "warm" excludes.

---

## 7. Copy and tone

The style guide's voice rules are firm and correct. Two additions from research.

**The best tonal models in the category**, verbatim:

- Bodily: *"Our cultural obsession with 'snapping back'… obscures the fact that what people really need to focus on after birth is recovery."* And on breastfeeding: *"it is anything but easy for the vast majority of people."*
- Motherhood Center: *"a waterfall of 'shoulds' and 'supposed to's' that cause many women to feel guilty, ashamed, and like a failure… motherhood is messy. … we make space for it all."*
- Peanut's **Renaming Revolution** — a genuinely good idea worth borrowing structurally: *geriatric pregnancy → 35+ pregnancy; inhospitable womb → uterine lining challenges; failure to progress → slowed labor.* You have an equivalent list to write: *low supply, failure to thrive, insufficient glandular tissue, non-compliant.*
- MacroFactor, on trend weight: *"Your weight trend is the signal in all of that noise."* And *"it can help people maintain a bit more peace of mind."*

**Bodily's calm-declarative register is the safest floor.** Frida's jokey register is a documented liability.

**On the disordered-eating question at onboarding.** The EPDS-US revision (Moyer et al., *J Women's Health* 32(10):1080–1085, 2023) is the model for softening a screener without breaking it: drop "unnecessarily" and "for no good reason," change "have been" → "have felt," rewrite the sleep item as *"difficulty sleeping even when I have the opportunity to sleep"* — and **the authors themselves call it a "check-in."**

Falsification is item-specific and real. One documented case scored an honest 25 and a written 8 — *"I lied through my teeth… they took away my baby"* — but **did not falsify the self-harm item**. Design accordingly: the gentle question should be the one she has no incentive to lie about.

Category patterns worth copying: Motherhood Center's "How are you feeling?" is a card carousel with **no score and no submit button**. Canopie never uses the word "screening" — it says *"Share how you're feeling."* Momwell refuses depression screening entirely and uses only the word **burnout**. **Ovia's escalation copy is stale** — it still references the pre-988 lifeline. Do not copy it, and audit your own crisis resources against current numbers before launch.

---

## 8. Novel concepts

Split as requested: a conventional core that will not surprise anyone, and a set of swings.

### 8.1 The safe core

These are proven and should not be argued about.

1. **Number-in-centre, arc-on-circumference, filling.** The pattern users explicitly praise on MFP's Watch app.
2. **Trend weight with MacroFactor's exact pedagogy** — pale raw line, bold trend line, one chart. Plus their three rhetorical devices: a worked numeric example, the "weight is a range not a number" frame, and a named FAQ entry for *"Should I still log my weight if I'm bloated?"* Postpartum noise is worse than the general case — lochia, resolving edema, engorgement, hydration swings, pre/post-feed differences. Say so explicitly and widen the smoothing constant accordingly.
3. **Meal-grouped logging, free barcode scan, per-item favourites, free-text portions.** §6.2.
4. **Weigh-in and food logging on one surface.** §6.2.
5. **Annual-first paywall at the plan-activation moment**, no countdown timers, no fake discounts. Already in the brief; the review corpus confirms every predatory pattern is resented.

### 8.2 The swings

Ordered by conviction. Each carries an honest build-risk note.

---

**A. "Still to eat today" replaces "calories remaining."** *(Highest conviction. Low build risk. Tests trivially.)*

§2.4. Subtract the floor out of the headline number. It counts down to zero and stops; zero is the win. Ship it on the widget and Lock Screen first even if the in-app ring stays conventional — that's a cheap A/B and the widget is where the glance actually happens.

The deeper move: this kills the budget frame entirely. There is no number to overspend.

---

**B. Floats and sinkers on the trend chart.** *(High conviction. Medium build risk. Genuinely novel in this category.)*

From *The Hacker's Diet*, and it is the best reframe device found in the entire research corpus. Plot the trend line, plot each day's raw reading as a diamond, and **draw a short connector from each diamond to the trend line.** Walker's framing:

> "Think of the trend as a fishing line in the water. Daily weights that fall below it are **sinkers**, pulling it down… When the trend is rising, most daily weights will be above the trend line: **floats**, tethered to the line, pulling it up."

This converts a bad day from *evidence of failure* into *a force acting on the truth* — and the connector lines make the mechanism visible without a word of copy. Invert the polarity for intake: a low-intake day is a sinker pulling her protection trend down.

Walker's supporting numbers are worth building the copy around: during a diet that worked exactly as planned, the raw scale produced constant despair, but across 51 days the trend went **down 37 days, unchanged 10, up only 4.** That three-row table is itself a good UI element.

His warmth device is also worth stealing: translate an abstract slope into food. *"An excess of 66 calories a day, comparable to a single Oreo cookie, half a tablespoon of mayonnaise, or 5 peanuts roasted in the shell."* Making the correction feel trivially achievable is the whole game.

---

**C. The floor line moves, visibly.** *(High conviction. Low build risk. Strong differentiation.)*

Gentler Streak moves its target range with menstrual phase. Your equivalent: the floor **rises during cluster feeding, growth spurts, and exclusive pumping**, and falls through weaning. Do not change it silently — **animate the floor line moving**, with one sentence of reason.

This is the single clearest way to prove the floor is a physiological fact and not a judgment. It also directly answers the loudest MFP complaint: *"There was no place I could add a BMR so the app would take that into account."*

Corollary constraint on the weekly-budget mechanic: redistribution must be **asymmetric**. An over-day may borrow from later days; an under-day must **never** be banked as credit. Undershooting the floor is a supply-risk event, not savings.

---

**D. "Days protected" as the hero retrospective.** *(High conviction. Low build risk.)*

Dexcom's Time in Range, ported. **"You protected your supply on 26 of the last 30 days."** Rendered as a stacked horizontal bar: days above floor / slightly under / well under.

Robust to a single bad day, matches the biology, recognised by clinicians, and — importantly — it is a weekly headline metric that **is not a weight**. The brief already wants progress-beyond-the-scale; this is the concrete form of it.

---

**E. A character at the centre of the ring.** *(Medium conviction. Medium build risk. Real tonal payoff, real tonal danger.)*

Three separate award-recognised wellbeing apps put a character at the centre of the metric: **Harvee** (2026 ADA Social Impact finalist — *"a friendly little guy who sits at the center of the experience and serves as an avatar for a person's state"*), **Gentler Streak** (the Yorhart heart mascot, which changes for the "State of Extra Recovery"), and **Finch**.

The mechanism is real: **the character absorbs the emotional valence that would otherwise attach to the number.** The app can communicate "you're low" through a face without the user reading it as *you failed.* For a product whose central risk is that a number makes an exhausted woman feel judged, this is a serious tool.

The danger is equally real: your style guide bans cartoon babies and pastel-baby aesthetics for good reasons, and a cute mascot in a postpartum weight app could read as condescending — the exact "infantilising women's health design" failure §4.3 warns about. If you try this, the character must be **abstract and adult** — Bodily's organic-shape vocabulary rather than anything with eyes. Prototype it; do not commit to it.

---

**F. The percentile ribbon instead of a single line.** *(Medium conviction. Higher build risk. Best long-term idea.)*

Dexcom's AGP superimposes 14 days onto one 24-hour frame with five percentile curves: a heavy median inside a dark 25–75th ribbon inside a light 5–95th ribbon.

Ported: *"here is your typical day, and here is how much you vary."* The ribbon **narrows as she becomes more consistent** — which is a progress story that does not require the weight to move at all. For a user whose intake variance is largely outside her control and whose scale weight is postpartum noise, this may be the most honest progress metric available.

Build risk is real: it needs enough data to be meaningful, so it can't be the day-one Trends screen. Ship it as the 30-day view, or as a v1.5 unlock.

---

**G. Palette on a clock.** *(Medium conviction. Low build risk. Cheap distinctiveness.)*

§4.4. Tide Guide won an ADA for exactly this. It solves a real legibility problem, it differentiates a palette that is otherwise category-generic, and it is a genuinely lovely detail for a product whose defining use case is a specific hour of the night.

---

**H. Log the food, get the arc preview.** *(Medium conviction. Low build risk.)*

Gentler Streak shows each recommendation **with a preview of how it will move your position on the Activity Path.** On the below-floor nudge, render each suggested food as a **ghosted arc extension** on the ring — she sees the peanut butter toast close the gap before she taps it.

This is the "Healthy Alternatives" mechanic (§6.5) made visual, and it is the difference between an alert and a piece of help.

---

**I. An explicit "we don't know yet" state.** *(Underrated. Trivial build risk.)*

Natural Cycles' brown day — *"more data is needed"* — is the **only explicit insufficient-data colour found in any app across the whole study**, and their engine defaults to the safe state when it lacks information.

You need this and currently don't have it. Two missed check-ins should not silently render as "steady." It also expresses uncertainty as *duration* rather than probability, which is far more legible: *"a few more days of check-ins and I'll be able to say."*

---

**J. Numbers-off mode.** *(Should probably be core, not a swing.)*

An actual MFP user request, 5★, 2024:

> "Being able to check a bubble that indicates if you stopped eating at enough and ate when hungry to help with intuitive eating. **This view could also have an option to hide calories and macros.**"

The adapted mode in the brief already goes most of the way. Making "hide the numbers" a first-class toggle available to *everyone* — not just the adapted-mode cohort — is cheap, is user-requested, and is the strongest single signal that this app is not a diet app.

---

## 9. The do-not list

Consolidated anti-patterns, all evidence-backed.

**From the ED literature.** Three findings that should shape v1 scope:

- **Levinson, Fewell & Brosof (2017)**, *Eating Behaviors* — clinical sample, n=105 with diagnosed eating disorders. ~75% had used MyFitnessPal; of those, **73% said it contributed at least somewhat to their eating disorder, 30% "very much."**
- **Simpson & Mazzeo (2017)**, n=493 — **fitness tracking, not calorie tracking, was the unique predictor** of ED symptomatology, attributed to appearance-motivated exercise and the absence of rest days or activity ceilings.
- **Plateau et al.**, *BJPsych Open* — qualitative account of how these apps entrench ED behaviours.

Therefore: **no exercise credits, ever.** No "you burned it, you can eat it." And Simpson & Mazzeo argues directly against adding step or workout tracking to v1 at all — which the brief already excludes. Keep it excluded.

**From the review corpora:**

- No interstitial ads. Beyond the obvious: *"the images for the weird ads are so gross it makes me stop eating"* — from a user logging while eating, which is your 3am user exactly.
- No condescending coaching voice. *"the same as ChatGPT but more condescending… told her sleep is 'junk'… I cancelled immediately."*
- No AI advice that can be wrong about the baby. One app was *"repeatedly telling me I am overfeeding my baby"* using the wrong age.
- No forced arithmetic. *"how many minutes is .4 hours?"*
- No tracking-induced anxiety. *"After a week of use I realized I was paying less attention to my child, more anxious, and deeply unhappy."* This is the deepest risk in the category and the reason numbers-off mode matters.
- No primary buttons at the top. Glow Baby is the named failure case in NN/g's write-up.
- No top-right "+" as the main entry point.
- No hue-only state encoding. §4.5.
- No timers without caps — or better, no timers. §3.3.
- No silent save failures. §6.3.

---

## 10. Claude Code design toolchain

The headline: **most of the "Claude Code design tooling" ecosystem is web/React/Tailwind-shaped and irrelevant to a SwiftUI app.** shadcn MCP, 21st.dev Magic, superdesign, Playwright visual QA — all assume a DOM. The real iOS stack is smaller and better.

### 10.1 Install these

```bash
# Figma MCP — includes the figma-swiftui skill
claude plugin install figma@claude-plugins-official

# Anthropic's frontend-design skill
/plugin install frontend-design@claude-plugins-official

# The SwiftUI build + simulator + screenshot loop
brew tap getsentry/xcodebuildmcp && brew install xcodebuildmcp
xcodebuildmcp init
claude mcp add XcodeBuildMCP -s user -- npx -y xcodebuildmcp@latest mcp

# Useful prompt-library skills (brief / IA / tokens only)
npx skills add julianoczkowski/designer-skills
```

Plus: **upgrade to Xcode 26.3+**, which ships a built-in MCP exposing 20 Xcode capabilities including **rendering SwiftUI Previews so the agent can see them without a full build/install cycle**.

### 10.2 The `figma-swiftui` skill is the find

Figma ships a dedicated bidirectional SwiftUI skill (`github.com/figma/mcp-server-guide`, `skills/figma-swiftui/SKILL.md`). Its load-bearing rules:

- Pass `clientLanguages: "swift"`, `clientFrameworks: "swiftui"` to `get_design_context` or you get React + Tailwind back.
- *"The React+Tailwind in `get_design_context` output is a structural reference, not a literal source… **the screenshot is the source of truth in both directions.**"* This is why naïve Figma-to-code produces absolute-positioned garbage.
- iOS HIG semantic colours map as **tokens, not hex**: `var(--backgrounds/primary)` → `Color(.systemBackground)`.
- SF Symbols round-trip **by name, never codepoint**.
- Pattern recognition over literal nodes: large title + back chevron → `NavigationStack`; bottom icon+label row → `TabView`; repeating same-height rows → `List`.

Use `get_metadata` first on large frames to avoid blowing context, then `get_design_context` + `get_screenshot` on the specific node.

### 10.3 The code-to-design direction is the underrated half

You have no designer. So don't start in Figma — build 2–3 SwiftUI screens in code, then:

> "Mirror my SwiftUI design system in Figma: create a new file, then push the views in `Sources/DesignSystem/` as a component library with variables for colour and spacing."

`figma-generate-library` builds a Figma design system **from your code** in reviewed phases (Discovery → Foundations → File structure → Components with variants and screenshot validation → QA). You end up with a real Figma library generated from your actual code, which you can restyle visually and pull back down. That inverts the usual dependency, which is correct when you're solo.

`use_figma` executes JavaScript against the Figma Plugin API, so it can do anything Figma can. Free during beta; will become usage-based. Requires a Full or Dev seat. **Skip Code Connect** — it's Organization/Enterprise only.

### 10.4 The loop that actually produces good UI

This is where the leverage is. XcodeBuildMCP (Sentry-maintained, 6.3k stars, ~82 tools) gives you `snapshot_ui` for running-simulator screenshots and bundles **AXe**, which drives the simulator through Accessibility APIs using deterministic `accessibilityIdentifier` targeting rather than pixel guessing.

> "Build `SupplyBannerView`, run it on the iPhone 17 simulator, screenshot it, then critique your own screenshot against `.claude/skills/design-system/SKILL.md` — check contrast ratios, tap-target size in mm, type scale, Dynamic Type at AX5, and legibility in the 3am palette at 20% brightness. Fix what fails and screenshot again. Repeat until it passes."

Two things make this work:

1. **Critique against a written spec**, never "does this look good" — otherwise it rubber-stamps its own output.
2. Use **Xcode previews for tight per-component iteration** and `snapshot_ui` for whole-screen and flow verification.

Add one-handed operation and the §4.5 colour-redundancy table to the checklist. Your users are holding a baby.

### 10.5 Encode the design system so it can't drift

Three layers:

1. **`CLAUDE.md`** — always-on, small: fonts, colour discipline, forbidden patterns.
2. **`.claude/skills/design-system/SKILL.md`** — on-demand: the full token table, component inventory, the anti-pattern list from §9, and SwiftUI conventions (semantic colours not hex, Dynamic Type, SF Symbols by name, 56pt tap targets on check-in).
3. **`DesignTokens.swift`** — a single source-of-truth enum. Then the rule in the skill is: *never write a literal hex, spacing value, or font size; only reference `DesignTokens`.* That makes drift mechanically detectable — grep the view layer for hex literals.

Steal designer-skills' **"Respect Existing Code"** principle: every skill that touches the codebase runs a detection checklist first (token files, theme configs, component dirs) so the agent doesn't invent a fourth green.

### 10.6 Getting non-generic visual output from Claude

Anthropic's published guidance (`claude.com/blog/improving-frontend-design-through-skills`, and the `prompting_for_frontend_aesthetics` cookbook) diagnoses the problem as distributional convergence: *"Safe design choices — those that work universally and offend no one — dominate web training data. Without direction, Claude samples from this high-probability center."*

Three techniques: guide specific dimensions individually (typography, colour, motion, backgrounds); reference design inspirations without over-prescribing; and **explicitly call out the defaults to avoid**.

The subtlest and most useful warning is about **second-order convergence**: telling Claude to avoid Inter just moves it to a different local maximum (their example: Space Grotesk). Name the specific second choices you've already seen it produce.

**Two caveats for this project.** The cookbook's aesthetics block is CSS-specific — rewrite it in SwiftUI terms. And it optimises for *distinctive and surprising*, which is not what you want for a health app used by exhausted people at 3am. Take the anti-default lists and the typographic discipline; discard "take one real aesthetic risk."

### 10.7 Skip these

- **21st.dev Magic** — unmaintained (no commits in 3 months as of Feb 2026), unresolved prompt-injection advisory, React-only.
- **superdesign** — thin client for a paid hosted service; its model requires hand-maintaining an HTML replica of your iOS app.
- **shadcn MCP** — React-only; shadcn.io's is $19/mo.
- **Figma Code Connect** — Enterprise-only.
- **The "3,000 skills" mega-marketplaces** — volume plays, unvetted.

Add **Chrome DevTools MCP** only for the marketing site.

---

## 11. What to validate next

Design-side questions the research could not settle. Most fold into the 20 discovery interviews already planned.

1. **Does the "Still to eat today" framing land, or does it feel like a chore?** The strongest idea here is also the least tested in this domain. Two static mockups in the interviews would settle it.
2. **Does a self-referential supply statement feel useful, or does it feel like the app is dodging?** §1.1 constrains the copy hard. Test whether *"steady vs. your own last 7 days"* satisfies the anxiety that drives the feature at all.
3. **Character or no character?** §8.2-E. Genuine tonal upside, genuine condescension risk.
4. **Is sage-on-cream distinctive enough?** Show the palette next to Bodily, Expectful, and Hey Jane and watch whether anyone can tell them apart.
5. **Pixel-level competitor teardown remains open.** No screenshots were visually read in this research — all layout description is inferred from text, review descriptions, and screenshot filenames. The fastest close is Chrome MCP against App Store listings, or installing the top five on a device.
6. **Pump Coach's actual UI.** Three ratings, no review corpus, and `thebreastfeedingmama.com/pump-coach/` returns empty. Worth installing.
7. **Does a low-precision input mode actually satisfy her?** §0A.2 shows people falsifying logs to reduce anxiety, which argues for *roughly enough / not sure / definitely not enough*. But it is untested whether that feels supportive or feels like the app isn't taking her seriously. Two mockups in the interviews.
8. **The partner question.** Shared state with a spouse is the single most-cited reason for keeping any baby app past week six, and you have no answer to it. Decide deliberately whether to cede that ground — it may be the difference between month-2 and month-8 retention.
9. **The gaining-weight cohort.** How large is it really, and what does a non-failure state look like for them? Recruit at least three interviewees who gained while nursing; they will not volunteer.

---

## Sources

**Nutrition / calorie trackers**
MyFitnessPal App Store listing & customer-review RSS (id 341232718, retrieved 2026-08-17) · MFP Help Center, "How does MyFitnessPal calculate my initial goals" · MacroFactor Help Center: [Weight Trend](https://help.macrofactorapp.com/en/articles/21-weight-trend), [Dashboard](https://help.macrofactorapp.com/en/articles/22-get-to-know-your-dashboard), [Micronutrient floor/target/ceiling](https://help.macrofactorapp.com/en/articles/138-what-are-the-micronutrient-floor-target-and-ceiling), [Coached-mode program options](https://help.macrofactorapp.com/en/articles/34-what-are-the-different-program-options-in-coached-mode), [Weekly budget](https://help.macrofactorapp.com/en/articles/92-weekly-budget) · Cronometer, Lose It!, Noom App Store listings

**Eating-disorder literature**
Levinson, Fewell & Brosof (2017), *Eating Behaviors* — [PubMed 28843591](https://pubmed.ncbi.nlm.nih.gov/28843591/) · Simpson & Mazzeo (2017), *Eating Behaviors* — [PubMed 28214452](https://pubmed.ncbi.nlm.nih.gov/28214452/) · Plateau et al., *BJPsych Open*

**Lactation & clinical**
[KellyMom — weight loss while breastfeeding](https://kellymom.com/nutrition/mothers-diet/mom-weightloss/) · [La Leche League International](https://llli.org/breastfeeding-info/weight-loss-mothers/) · [InfantRisk Center](https://www.infantrisk.com/content/weight-loss-lactation) · Academy of Nutrition and Dietetics · Dienelt et al., *Health Informatics Journal* (2020)

**Maternal / baby apps**
App Store listings and customer-review RSS for Huckleberry (1169136078), Nara Baby (1444639029), Baby Tracker (779656557), Baby Feed Timer (395357581), Baby Daybook (1446283219), Sprout Baby (551448817), Glow Baby (1077177456), Feed Baby (868611155), Ovia Parenting (1106614359), Pump Coach (6765497176), Pump Log (814112299), LactApp (1040787494) · Live CSS harvests of bodily.com, expectful.com, canopie.app, motherhoodcenter.com, heyjane.com, mahmee.com, fridamom.com, peanut-app.io, helloclue.com (17 Aug 2026)

**Reddit field evidence (§0A)**
~35 threads read in full with comments, Aug 2026, across r/breastfeeding, r/beyondthebump, r/NewParents, r/ExclusivelyPumping, r/Mommit, r/loseit, r/1200isplenty, r/Myfitnesspal, r/workingmoms. Key threads: [Pumping is not an indicator of supply!!!](https://www.reddit.com/r/breastfeeding/comments/g4a2o9/) (170↑) · [1300-calorie dietitian plan](https://www.reddit.com/r/breastfeeding/comments/1n59rsl/) (66↑, 157c) · [Petition to have breastfeeding included on fitness apps](https://www.reddit.com/r/breastfeeding/comments/1c6fg1y/) (37↑) · [MFP breastfeeding entry removed](https://www.reddit.com/r/Myfitnesspal/comments/1uh0tyi/) · [Tracking-app fatigue](https://www.reddit.com/r/breastfeeding/comments/1uidyge/) (180↑, 252↑ top comment) · [Do I need a tracking app](https://www.reddit.com/r/NewParents/comments/1m877fr/) (587c) · [Deficit and supply](https://www.reddit.com/r/breastfeeding/comments/1mgmwao/) · [Gaining weight while pumping](https://www.reddit.com/r/ExclusivelyPumping/comments/1rewrd7/) (111c) · [Postpartum body image](https://www.reddit.com/r/beyondthebump/comments/101qwdf/) (514↑) · [Breastfeeding in r/1200isplenty](https://www.reddit.com/r/1200isplenty/comments/u4xdnh/) · [Regret spending in pregnancy](https://www.reddit.com/r/beyondthebump/comments/l1crmr/) (1917↑, 534c)

**Design philosophy & rebrands**
Marta Pucci and Ida Tin on Clue's identity · Mother Design on Bodily (ADC Bronze Cube 2020) · AIGA Eye on Design, femtech branding waves · Pili Laviolette, Random Pattern Studio, on the pink/clinical/empowerment traps · Michelle Kennedy (Peanut)

**Cross-domain**
[Gentler Stories](https://gentlerstories.com/gentlerstreak) · [Oura Readiness Score](https://ouraring.com/blog/readiness-score/) · [Apple Design Awards](https://developer.apple.com/design/awards/) · [Dexcom Time in Range](https://www.dexcom.com/en-us/faqs/what-is-time-in-range) · [AGP Report](https://agpreport.org/agp/about) · [The Hacker's Diet, "Signal and Noise"](https://www.fourmilab.ch/hackdiet/e4/signalnoise.html) · Happy Scale review corpus (532430574) · [one sec research](https://one-sec.app/research/); Grüning, Riedel & Lorenz-Spreen, *PNAS* 120(8) e2213114120 (2023); Haliburton et al., *CHI '24* · Simple bank coverage (The Financial Brand, TechCrunch, PCWorld)

**Interruption & ergonomics**
Mark, Gonzalez & Harris (2005); Mark, Gudith & Klocke (2008); Monk et al. (2008) · Hoober, UXmatters (2017) · Harley, Nielsen Norman Group · Henze et al.; Schildbach & Rukzio

**Night light**
Chang et al. (2015) · Nagare et al. (2019) · Duraccio et al. (2021) · Phillips et al. (2019)

**Tooling**
[Anthropic skills](https://github.com/anthropics/skills) · [Figma MCP server docs](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/) · [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) · [XcodeBuildMCP](https://github.com/getsentry/XcodeBuildMCP) · [Anthropic — Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) · [claude-cookbooks — prompting for frontend aesthetics](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) · [Anthropic × Apple Xcode](https://www.anthropic.com/news/apple-xcode-claude-agent-sdk)
