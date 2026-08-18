# Style & Design Direction
*Visual language for the breastfeeding-safe nutrition coach. These are strong suggestions, not locked decisions — Claude Design should treat palette/type as a starting system and propose refinements, but the tone rules and "never" list are firm.*

## Personality in five words
Warm. Calm. Trustworthy. Unhurried. Grown-up.

The emotional target: a knowledgeable friend who happens to be a lactation consultant — not a coach yelling, not a hospital, not a pastel baby brand. She is exhausted and skeptical; the design's job is to lower her shoulders.

## Color
Primary system (light mode):

| Token | Hex | Use |
|---|---|---|
| Sage 600 (primary) | #5C8D76 | Primary actions, active ring, steady-state accents |
| Sage 800 | #3D6353 | Text on sage tints, pressed states |
| Sage 100 | #E8F1EC | Supply-steady banner bg, positive tints |
| Cream (canvas) | #FAF7F2 | App background — never stark white pages |
| Surface | #FFFFFF | Cards on cream |
| Ink | #2B2B28 | Primary text — warm near-black, never pure #000 |
| Ink-soft | #6B6A64 | Secondary text |
| Hairline | #E7E2D9 | Borders, dividers |
| Amber 600 | #C98A2D | Supply-dip state, gentle caution |
| Amber 100 | #F8EFDD | Dip banner bg |
| Coral 600 | #C4573B | Floor-breach only — reserved, so it always means "stop" |
| Coral 100 | #F9E7E1 | Breach surface bg |

Rules: sage carries the brand; amber and coral are *states*, never decoration. No red anywhere except coral's role. No pinks-and-pastels baby palette. Dark mode is required (3 a.m. use): warm dark charcoal (#211F1C canvas, #2C2A26 surfaces), desaturated sage (#7FA893), text #EDEae3 — never pure black/white; dim, low-glare, nursery-safe.

## Typography
- iOS: SF Pro Rounded (display + text). Cross-platform/mock fallback: Nunito.
- Scale: 28/semibold display (big numbers like calories remaining), 22/semibold titles, 17/regular body, 15 secondary, 13 captions. Minimum 13pt anywhere.
- Numbers she cares about are big and calm — not dashboard-dense. One hero number per screen.
- Sentence case everywhere. No ALL CAPS, no exclamation points in system copy.

## Shape & layout
- Radii: cards 20pt, buttons 14pt, chips/pills fully rounded. Soft, but not bubble-cute.
- Spacing on a 4pt grid; generous — whitespace is the calm.
- One-handed rule: primary actions live in the bottom 40% of the screen; tap targets ≥44pt.
- Shadows: barely-there (y2 blur8 @6%) or none — prefer hairline borders.

## Signature components
- **Supply status banner** (home, top): tinted card with shield/leaf icon, headline ("Supply steady — 5 days"), one-line subtitle from yesterday's check-in. Green sage = steady, amber = dipping (with nudge entry point).
- **Calorie ring with floor line**: the differentiating visual. Progress ring for intake vs target, with the floor rendered as a distinct notch/line the fill visibly sits above. Label pattern: "Floor: 1,800 — you're safely above it." The floor must read at a glance; it is the brand promise drawn as geometry.
- **3-tap check-in cards**: three sequential large-tap-target cards (yes / somewhat / no pattern), each answerable with a thumb, progress dots, done in ~10 seconds.
- **Full-screen nudge sheet** (supply-protect): calm, not alarming — sage surface, plain-language headline ("Let's ease up for two days"), the reason in one sentence, one-tap primary ("Raise my target to 2,300 →") and a quiet "Not now." Floor-breach variant uses coral, firmer copy, same structure.
- **Trend chart**: single smoothed line with a soft confidence band; weekly dots; no gridline clutter; annotations in plain words ("steady," "down 0.8 lb/wk").
- **Paywall**: plan-activation framing ("Your plan is ready"), annual card first with 2px sage border + "Best value" chip, monthly beneath, trial terms in honest plain type. No countdown timers, no fake discounts.

## Iconography & imagery
- Icons: soft rounded-outline set (SF Symbols rounded weight), never sharp/techy.
- Illustration (if any): abstract organic shapes, botanical hints — no storks, no cartoon babies, no scales, no tape measures.
- Photography: real postpartum bodies when used in marketing; NEVER before/after pairs, in-app or in ads.

## Motion & feedback
- 200–300ms ease-out transitions; nothing bouncy or game-like.
- Haptics: light on check-in completion and one-tap accepts.
- Celebration is restrained and aimed at *behaviors* (check-in streaks, floor adherence) — never at weight lost. No confetti on the scale, ever.

## Voice & copy rules (firm)
- Warm, plain, specific. "Let's ease up for two days" — not "Alert: supply risk detected."
- The app admits limits: escalation moments hand her to humans ("This is worth a chat with your IBCLC").
- Banned lexicon: "bounce back," "get your body back," "guilt," "cheat," "burn it off," "earn your food," "summer body," "shred," "detox."
- Preferred frames: fuel, recovery, strength, steady, protected, "the weight that's ready to go."
- Numbers with context, never naked: "1,460 left — comfortably above your floor."

## Adapted mode (from the gentle onboarding question)
When enabled: no deficit by default, no streaks, hero metric switches from calories-remaining to energy/protein, copy drops all loss language. Design every screen knowing this variant exists — it should feel like a sibling, not a downgrade.
