# MVP Design Brief — Postpartum Weight & Wellness App
*Compiled from founder scoping sessions, August 17, 2026. Companion to `Postpartum_App_Market_Research.docx`.*

## Product in one sentence
The breastfeeding-safe nutrition and wellness coach: helps nursing mothers lose weight without risking milk supply, built on calorie floors, a daily supply check-in, and nudges that know when to tell her to eat more.

## Platform & constraints
- iOS first (iOS 17+), Android fast-follow. Dark mode required (3 a.m. use case).
- Every core action must be one-handed and completable in under 10 seconds.
- Nutrition engine ships with placeholder rules (structure below); coefficients finalized with RD/IBCLC advisors before public launch. UI must not need rework when real math lands.
- Privacy: no third-party advertising data sharing. Ever. It's a differentiator.
- Tone: warm, plain, zero diet-culture. No before/after imagery anywhere. "Feed your baby, fuel your recovery" — never "get your body back."

## V1 surface area
Four core screens (Home, Log, Check-in, Trends) + onboarding + paywall + two full-screen nudge moments.

---

## 1. Home — "supply-first" layout (Option A)
Decision: supply status leads, calories second. This is the positioning rendered in UI.

Stack, top to bottom:
1. Greeting (first name, time-aware).
2. **Supply status banner** — green/steady state: "Supply steady — 5 days," subtitle from yesterday's check-in. Amber when dipping, with the nudge entry point.
3. **Calories-remaining ring** with the floor drawn as a visible hard line on the ring. Beside it: "Floor: 1,800 kcal — you're safely above it."
4. Quick actions: Log food · Daily check-in. (Water chip optional, small.)

Build note: home is a reorderable component stack behind a config flag. Calories-first (Option B) exists as a layout variant for A/B testing once DAU supports it. Not deliberated further pre-launch.

## 2. Food logging
- V1 inputs: USDA database search, barcode scan, recents/favorites. Meal-grouped (breakfast/lunch/dinner/snacks).
- "Set amount, we calculate the rest" portion flow; live nutrition preview.
- Photo logging and voice entry: fast-follow, explicitly not v1.
- Benchmark: repeat log of a known food in under 10 seconds, one-handed.

## 3. Supply check-in — the moat feature
Decision: **active only** in v1; passive inference from feed logs comes later at scale.

- Daily, ~10 seconds, three taps:
  1. Feeds felt normal today? (yes / somewhat / no)
  2. Pump output vs. usual? (more / same / less / didn't pump)
  3. Baby seemed satisfied? (yes / unsure / no)
- Adaptive: question 2 hidden for non-pumpers (from onboarding nursing status).
- Streak display, gentle. Feeds the nudge engine and the Trends supply line.
- **No nursing/pumping timers in v1.** Tracker import/sync (Huckleberry et al.) targeted for v1.5.
- Roadmap note (v2): native free feeding tracker as acquisition funnel — must be genuinely feature-deep and standalone-excellent, not a stub. Nothing in v1 forecloses this.

## 4. Trends
- Weight: **weekly weigh-in prompt**; display is the 7-day smoothed trend line, not raw daily noise. Smoothing framed as a feature ("scale weight lies while nursing").
- Floor adherence: days above floor this week.
- Supply line: check-in history as a simple steady/dip band.
- Measurements: optional entry, deferred emphasis. Energy self-rating optional.

## 5. Nudge engine (rules are placeholders; shape is final)
Four families:
1. **Supply-protect** (hero moment): check-in dips 2 consecutive days AND intake under target ≥2 of last 3 days → full-screen: "Let's ease up — +300 kcal for the next 2 days." **One-tap accept** ("Raise my target →"). Never silent auto-adjust; numbers never change without her tap.
2. **Floor breach**: projected/actual day below hard floor → immediate full-screen interrupt. Repeated breaches → soften targets + IBCLC referral prompt.
3. **Positive reinforcement**: streaks, protein trend, hydration — quiet in-app cards only.
4. **Escalation**: supply dip persists 4+ days regardless of intake → app steps back, points to humans (IBCLC/provider referral). The app knows when it's out of its depth.

Loudness rule: families 1–2 are full-screen moments; 3–4 in-app cards (4 escalates to full-screen at threshold).
Notification budget: **max one push/day**, priority: floor breach > supply dip > hydration > streaks. Everything else in-app only.

## 6. Onboarding — 7 screens, ≤90 seconds
Order: baby's birth date → nursing status (exclusive/combo/pumping/weaning) → height, weight, pre-pregnancy weight → activity level → "What matters most right now?" (energy / strength / weight loss / all of it) → **live target preview with the math shown** → account creation.

Locked decisions:
- **Value before the account wall.** She sees her full personalized plan — targets, floor, and why — before signup.
- **Six-week hard gate.** Baby under 6 weeks → maintenance-only mode until she confirms she's past her postpartum checkup. No override. Loudest "not like other diet apps" signal we have.
- **Disordered-eating screen**: one gentle self-report question, not a clinical screener. If yes → adapted mode: no deficit default, no streak pressure, softer copy throughout.
- Deferred to post-signup settings: delivery type, measurements, water goal.
- "What matters most" answer personalizes tone and home emphasis (body-neutral path is first-class, not a toggle).

## 7. Paywall & pricing
- **Safety is never paywalled.** Free forever: basic logging, supply check-in, floor-breach warnings.
- Paid: personalized targets, nudge engine with one-tap adjustments, trends, future fitness programs.
- Trial: 7 days, card required, presented at the plan-reveal moment — "Start your free trial to activate your plan."
- Pricing: annual-first **$79.99/yr**, monthly **$12.99/mo** beneath it. **No weekly plan** (predatory pattern, off-brand).
- Rationale: free safety layer keeps IBCLC referrals clean, feeds the v2 tracker funnel, and avoids the "charges moms for supply warnings" headline.

## 8. Nutrition engine placeholder (structure only — clinical sign-off pending)
- Mifflin-St Jeor BMR + activity factor + lactation adjustment (+300–500 kcal by nursing status).
- Hard calorie floor by status (~1,800 kcal exclusive nursing; tiered lower for combo/weaning — final numbers from advisors).
- Deficit cap ~0.5–1 lb/week while nursing; zero deficit under six weeks postpartum.
- Macro targets weighted to protein, set from body weight.
- Hydration floor tuned for lactation (~3.0–3.8 L; advisor-confirmed).
- All coefficients live in remote config: clinical revisions must not require app releases.

## Screens to mock (design phase)
1. Onboarding ×7 (including target-preview "math shown" screen and six-week-gate variant)
2. Home (Option A; steady state + amber supply-dip state)
3. Log flow: search → portion → confirm; barcode entry
4. Supply check-in: 3-tap flow + completion state
5. Trends
6. Paywall (plan-activation moment)
7. Nudge moments: supply-protect full-screen (with one-tap accept), floor-breach interrupt
8. Adapted-mode variant of home (no deficit/streaks) — one example screen

## Explicitly out of scope for v1
Nursing/pumping timers · photo & voice logging · fitness content · community · Android · passive supply inference · PPD screening (resource links only) · GLP-1 anything · web app.

## Open items (not blocking design)
- App name & brand direction (3 directions to test in discovery interviews)
- Clinical advisor recruitment (RD + IBCLC) → finalizes engine coefficients
- Sister's HR/outside-activities confirmation + disclosed-partnership agreement (FTC)
- Willingness-to-pay validation: 20 interviews, kill criterion at <1/3 willing to pay ~$10/mo
