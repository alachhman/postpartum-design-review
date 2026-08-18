# Product Development Conversation Log
*Anthony Lachhman × Claude — August 17, 2026. Faithful compilation of the full working session, from first ideation through locked MVP decisions. Where this log and `02_MVP_Design_Brief.md` differ, the brief wins.*

---

## Phase 1 — Ideation
Started as an open brainstorm on postpartum ("mommy") app ideas. Categories explored: mom-focused recovery (symptom tracking, PPD companion, pelvic floor rehab), logistics (village coordinator, partner app, night-shift scheduler), and niche angles (3 a.m. feed companion, return-to-work planner, "is this normal?" checker). Noted that feeding/sleep trackers (Huckleberry) and mom social (Peanut) are saturated.

Anthony steered to **weight loss / "getting back to your body."** Key insight that shaped everything after: generic apps actively fail this user — MyFitnessPal will assign a nursing mother a 1,200-calorie deficit that threatens milk supply. The gap is postpartum-*aware* nutrition, not another fitness app. Positioning insight: "strong enough to carry the car seat upstairs" outperforms "get your body back" with this audience — function-and-safety framing is both the ethical and the commercial move.

## Phase 2 — Market research (full findings in 03_Market_Research)
Headlines that drive the product:
- ~3.6M US births/yr; ~86% initiate breastfeeding; ~75% of women are heavier at 1 year postpartum; 47% retain >10 lbs. The audience is the statistical majority, refreshed annually.
- **GLP-1 era is the "why now":** the $135B weight-loss market is medicalizing around GLP-1s ($132B in 2025 sales), gutting generic diet apps — but GLP-1s are not recommended while breastfeeding. Nursing mothers are one of the last structurally protected niches for behavioral weight management, with a 6–18-month protected window per user.
- **Direct competition is negligible.** LatchFit (only true direct competitor): solo dev, launched Oct 2025, 7 ratings at 3.6 stars, ad-supported, $2.99 IAP, crash/data-loss-riddled version history, iOS-only. Right thesis, weak execution. MFP has no nursing mode (users hack it with a −500 kcal "breastfeeding" food entry — famous community workaround and our clearest demand signal). Noom/WW have no postpartum programs and are busy pivoting to GLP-1 prescribing.
- Postpartum fitness side is crowded-but-fragmented (MUTU, Expecting & Empowered, Every Mother, Juna, Sweat, Sculpt Society; $13–30/mo) — nobody owns nutrition.
- Why the space is empty (7 barriers, each convertible to a moat): incumbent liability veto, corporate niche math, VC churn allergy, rare dual expertise (app craft + lactation science + distribution), reputational radioactivity of marketing weight loss to new mothers, thin clinical evidence base, industry attention consumed by GLP-1s.
- Honest bear case: possibly a $5–15M ARR niche rather than venture scale; churn is structural (users wean out in 12–18 months). Mitigations: annual-first pricing, pregnancy-side entry later, acquisition-led model (self-renewing cohort), B2B2C as scale path. Failure mode is a profitable lifestyle business — acceptable asymmetry.
- Business model: freemium, $12.99/mo / $79.99/yr; year-1 base case ~10K subs / ~$1.1M ARR with a working creator channel.

## Phase 3 — Founding-creator asset
Anthony's sister: senior at Northwell Health, new mother of two, active TikTok creator. Role decided: **launch creator and product muse, not publicly attached** — she makes disclosed paid/partner content referencing the app. Constraints accepted: FTC material-connection disclosure on all content (family + paid = disclosure required, ~$53K/violation exposure, health products draw enforcement); she should quietly confirm employer outside-activities policy. Strategic upside beyond launch: Northwell relationship becomes interesting for B2B2C/health-system pilots in year 2+. Agreed she is a launch advantage, not the moat — the moat is being the app IBCLCs recommend, plus the proprietary supply-vs-intake dataset.

## Phase 4 — MVP scoping decisions (all locked)
Nutrition engine deferred until RD/IBCLC advisors are onboard; UI built against placeholder rules with coefficients in remote config.

| # | Topic | Decision | Reasoning |
|---|-------|----------|-----------|
| 1 | Supply signal architecture | **Active daily check-in only in v1** (3 taps: feeds normal? / pump output vs usual? / baby satisfied?). Passive inference later at scale. | Passive requires building a full feeding tracker — v1 scope suicide vs entrenched, loved incumbents. |
| 2 | Feeding timers | **Out of v1.** Tracker import/sync in v1.5. | Moms pick trackers in week one; our user arrives week 6+ already invested. Don't double-log her. |
| 3 | Feeding tracker long-term | **v2: build a genuinely excellent FREE feeding tracker as acquisition funnel** — Huckleberry playbook (free tracker → paid program). Anthony's requirement: must be feature-deep and standalone-excellent, a real draw — not a loss-leader stub. | Captures moms at week 0, before weight-loss intent exists; converts at week 6+. |
| 4 | Home screen hierarchy | **Option A: supply-first** (supply banner → calorie ring with visible floor line → quick actions). Built as a reorderable component stack behind a config flag; calories-first variant kept for A/B testing once DAU supports it. | Anthony initially pushed to A/B test instead of deliberate; agreed compromise: opinionated default now (A/B needs volume we won't have pre-launch), near-free test later via the flag. A is the positioning rendered on screen one. |
| 5 | Weigh-ins | **Weekly prompt**; display 7-day smoothed trend, never raw daily noise. | Daily weigh-ins are psychologically rough on this audience; smoothing is a feature ("scale weight lies while nursing"). |
| 6 | Nudge families | Four: supply-protect (hero: 2-day dip + under-target → "+300 kcal for 2 days"), floor-breach (immediate interrupt; repeated → soften targets + IBCLC referral), positive reinforcement (quiet cards), escalation (4+ day dip → app steps back, refers to humans). | The app must know when it's out of its depth — that's also the liability posture. |
| 7 | Nudge loudness | Supply-protect and floor-breach are **full-screen moments**; everything else quiet in-app cards. | Those two ARE the product promise. |
| 8 | Target adjustments | **One-tap accept** ("Raise my target →"). Never silent auto-adjust. | Agency, trust (numbers never move mysteriously), cleaner liability. |
| 9 | Notifications | **Hard cap: one push/day**, priority floor-breach > supply-dip > hydration > streaks; rest in-app. | New moms are drowning in pings; restraint is a feature. |
| 10 | Onboarding flow | ~8 screens ≤90s: baby birth date → nursing status → height/weight/pre-preg weight → activity → "what matters most right now?" (energy/strength/weight/all — body-neutral path is first-class) → gentle disordered-eating question → **live target preview with the math shown** → account. | Every extra screen bleeds users; showing the math builds trust with a research-driven, diet-app-skeptical audience. |
| 11 | Account wall | **Value before account** — she sees her full plan before signup. | The preview IS the conversion moment; walling it kills trust. |
| 12 | Six-week gate | **Hard gate, no override**: baby under 6 weeks → maintenance-only until she confirms she's past her postpartum checkup. | Costs a few impatient users; buys clinical defensibility, IBCLC goodwill, and the loudest "not like other diet apps" signal available. |
| 13 | ED screening | **One gentle self-report question**, not a clinical screener (SCOFF etc.). Yes → adapted mode: no deficit default, no streak pressure, softer copy. | Formal screeners drag us out of the FDA wellness lane; the gentle version does the ethical job in v1. |
| 14 | Paywall split | **Safety is never paywalled.** Free forever: basic logging, supply check-in, floor-breach warnings. Paid: personalized targets, nudge engine, one-tap adjustments, trends, future fitness. | IBCLCs can recommend a free app that warns moms; "charges mothers for supply warnings" is a never-headline; free tier feeds the v2 tracker funnel. |
| 15 | Trial mechanics | 7-day trial, **card required**, presented at the plan-reveal moment ("start your trial to activate your plan"). **Annual-first** $79.99/yr, $12.99/mo beneath. | Peak-motivation placement; annual-first captures LTV against structural wean-out churn. |
| 16 | Weekly plan | **No weekly pricing tier.** | Monetizes confusion, 30–50% first-renewal churn, predatory pattern, off-brand for a trust-led product. |

## Phase 5 — Handoff intent
All decisions compiled into `02_MVP_Design_Brief.md` (source of truth). This package exists to give Claude Design full context: research grounding, decision rationale, brief, and style direction (`04_Style_Guide.md`). Signature screens to design first: supply-first home (steady + dip states), 3-tap check-in, the two full-screen nudge moments. Sample data: user "Sarah," 1,460 kcal remaining, floor 1,800 kcal, supply steady 5 days.

## Open items (tracked, not blocking design)
1. App name and brand direction — 3 directions to test in discovery interviews (avoid diet-culture naming).
2. Clinical advisors (RD + IBCLC) — finalize engine coefficients; launch prerequisite.
3. Sister: HR outside-activities confirmation + disclosed-partnership agreement.
4. Willingness-to-pay validation: 20 interviews; kill criterion if <1/3 would pay ~$10/mo.
5. Bootstrap vs pre-seed decision after discovery (both viable per research doc).
