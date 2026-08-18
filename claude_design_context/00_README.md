# Claude Design Context Package — Postpartum Weight & Wellness App
Prepared August 17, 2026 for import into Claude Design.

## Contents (authority order — when files conflict, higher wins)
1. `02_MVP_Design_Brief.md` — **source of truth.** Every locked product decision, screen list, and v1 scope.
2. `04_Style_Guide.md` — visual language, palette, components, voice rules. Tone rules and "never" list are firm; palette/type are a starting system open to refinement.
3. `01_Conversation_Log.md` — the full founder working session: ideation → research findings → every scoping decision *with its reasoning*. Use this to understand intent behind the brief.
4. `03_Market_Research.md` / `.docx` — full 23-page market research: audience, competitors, GLP-1 thesis, barriers to entry, unit economics. Background context.

## Kickoff prompt
Design the iOS MVP for a breastfeeding-safe nutrition coach — it helps nursing
mothers lose weight without risking milk supply. The attached brief
(02_MVP_Design_Brief.md) is the source of truth for every product decision;
follow it exactly. Style direction in 04_Style_Guide.md; decision rationale in
01_Conversation_Log.md.

Build in this order:
1. Home, supply-first layout (Option A): supply-status banner top, calorie ring
   with a visible hard "floor" line, quick actions. Two states: steady (sage)
   and supply-dip (amber).
2. Supply check-in: the 3-tap daily flow plus completion state.
3. The two full-screen nudge moments: supply-protect ("+300 kcal for 2 days,"
   one-tap accept) and floor-breach interrupt.
4. Onboarding, 8 screens, including the live target-preview screen that shows
   the math, and the six-week maintenance-gate variant.
5. Log flow (search → portion → confirm), Trends (7-day smoothed weight),
   Paywall (annual-first $79.99/yr, $12.99/mo below, 7-day trial).
6. Adapted-mode home variant (no deficit, no streaks — see style guide).

Sample data throughout: user "Sarah," 1,460 kcal remaining, floor 1,800 kcal,
target 2,000, supply steady 5 days, baby 11 weeks, combo feeding.

Screens 1–3 are the signature moments that define the visual language;
everything else inherits from them.

## Working name
None yet — use a neutral placeholder wordmark (naming is an open item; avoid diet-culture names in any placeholder).
