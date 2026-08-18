# Build contract — read fully before writing any page

You are building ONE page of a design-review site. Three design directions are
already defined and implemented in CSS. Your job is to render your assigned
screen(s) in **all three directions**, faithfully to each direction's thesis.

Working dir: `/Users/antnee/Documents/Projects/postPartum/site`
Reference implementation (READ IT FIRST, copy its structure exactly): `01-home.html`
Server already running at `http://localhost:8731`.

---

## The three directions — do not blur them

| | **A · Ledger** (`.dir-a`) | **B · The Band** (`.dir-b`) | **C · Protected** (`.dir-c`) |
|---|---|---|---|
| Thesis | Subtract the floor out of the headline. The number counts to zero and stops; zero is the win. No ring — a horizontal bar, where a labelled tick is unambiguous. | Keep the brief's ring, fix only its geometry. Floor is a filled sector the fill crosses out of; safe state is a **band** (1,800–2,300), not an edge. Fill-to-safety, never drain-to-zero. | The app asks for **less** over time, because the real competitor is abandonment. Hero is "days protected," not today's number. Numbers off by default. Low-precision input first-class. |
| Ground | Warm greige `#EDE8DF` | Pale clay `#F3EDE4` | Runs on a clock: `.t-day` / `.t-dusk` / `.t-night` |
| Action colour | Oxblood `#7B2D20` | Sage 700 `#456B59` | Ochre `#7A5A16` (day) / `#C9A465` (night) |
| Below-floor / stop | **Value inversion** — add `.inverted` to `.screen`. NEVER red. | Coral 700 `#A6432B`, sparingly | Desaturated + hatched, never red |
| Display type | Fraunces (`.ed`, `.greet`, `.sheet h1`) | Newsreader (`.ed`, `.sheet h1`); Nunito for UI | Petrona (`.ed`, `.greet`, `.sheet h1`) |
| Radii | Tight, 9px | Soft, 20px cards / 14px buttons | 14px cards, pill buttons |
| Voice | Plain, exact, a little editorial | Warm, reassuring | Quiet, unhurried, fewest words |

---

## Page skeleton — copy verbatim from `01-home.html`

Same `<head>` (fonts + 5 stylesheets), same `<nav>` (set `aria-current="page"` on
your page's link), same `<footer>`, same `<script src="js/shot.js"></script>`
before `</body>`, same `.pager` links.

Page body pattern:

```html
<div class="wrap">
  <section class="hero" style="padding:64px 0 30px">
    <span class="eyebrow">Screen NN · …</span>
    <h1>…</h1>
    <p class="sub">…</p>
  </section>
  <div class="callout">…the tension or constraint on this screen…</div>
</div>
<div class="wrap"><section class="screenblock anchor" id="…">
  <div class="screenhead"><h2>…</h2><p class="note">…</p></div>
  <div class="rowgrid">
    <div class="spec a"><div class="spec-head"><span class="dot"></span>
      <span class="nm">A · Ledger</span><span class="sub">short descriptor</span></div>
      <div class="stagewrap"> …phones… </div>
      <p class="caption"><b>Lead.</b> Why. <span class="cite">§ref</span></p>
    </div>
    …spec b… …spec c…
  </div>
</section></div>
```

Phone shell (the direction class goes on `.phone`):
```html
<div class="stage"><div class="phone dir-a"><div class="screen">
  <div class="sb">…status bar, copy from 01-home.html…</div><div class="notch"></div>
  <div class="body">
    <div class="pad" style="padding-top:14px"> …top content… </div>
    <div class="pad mtauto" style="padding-bottom:8px"> …actions… </div>
  </div>
  <div class="hb"></div>
</div></div></div>
```

**Multi-step flows** (check-in taps, log search→portion→confirm, onboarding):
give each direction its OWN full-width row, with the steps side by side as
`<div class="stage sm">` (0.62 scale). Structure:
```html
<div class="spec a" style="grid-column:1/-1">
  <div class="spec-head">…</div>
  <div class="stagewrap">…3–4 <div class="stage sm">…</div>…</div>
  <p class="caption">…</p>
</div>
```
Use `.stage sm` ONLY inside a full-width `.spec`; single-screen comparisons use
plain `.stage` in the 3-column `.rowgrid`.

---

## Available classes (already styled in all three directions)

`.greet .greet-sub .sec .lbl .ed .p` — type
`.banner` + `.dip .unknown .breach`, children `.ic .h .s .go` — supply status
`.card` (`.flat` in A, `.tint` in B, `.quiet` in C) · `.divider` · `.listrow` + `.nm .mt .val`
`.btn` + `.primary .quiet .ghost .big` (B also `.caution .stop`; C also `.held`)
`.chip` + `.on` · `.qa` + `.qa-item` + `.t .d` (`.accent`) · `.dots` + `i.on`
`.sheet` + `.kicker` `h1` `.why` · `.statn .statl`
A only: `.ledger` + `.k .n u .say`, `.fbar` + `.track .band .under .fill .tick .ticklab .ends`
B only: `.ringwrap` + svg, `.ring-c .ring-n .ring-u .ring-k`, `.bandlab` + `.sw`
C only: `.field` + `i` / `i.thin .miss .pause .void .today`, `.fieldkey .cellkey`,
        `.hero-n` + `u`, `.hero-say`, `.coarse` + `button` + `.mk` + `.on`, `.breath`
Utility: `.row .between .grow .tc .tabnum .mtauto .gap8…14 .mt4…mt40 .pad`

**Never write a hex literal in page HTML.** Use `var(--ink)`, `var(--accent)`,
`var(--held)` etc. If you need something the CSS lacks, add a small
`<style>` block in the page `<head>` scoped under `.dir-x`, using the
existing custom properties only.

---

## Sample data — use these exact values everywhere

Sarah · 11 weeks postpartum · combo feeding · baby born 30 May
Floor **1,800** · target **2,000** · protected band **1,800–2,300**
Today: **540 eaten**, **1,460 left of target**, **1,260 still to eat** (11:42am)
Dip scenario: 4:12pm, **1,180 eaten**, heading to **1,620**, two days below her usual
Supply: **steady, 5 days** · **26 of the last 30 days protected**
Weight: 172.4 lb now, pre-pregnancy 148, 7-day trend **−0.6 lb/wk**
Pricing: **$79.99/yr** annual-first, **$12.99/mo** beneath, 7-day trial, card required

---

## Hard rules (these come from the research; violating them breaks the deliverable)

1. **Never a clinical verdict on supply.** Allowed: "steady — 5 days", "two days
   below *your usual*", "not enough check-ins to say". Banned: "your supply is
   good/low/normal", "above typical", any comparison to other women. §1.1 §3.1
2. **Never red below the floor.** Below-floor is quiet and desaturated. Coral is
   reserved for the floor-breach interrupt only, and A uses inversion instead. §2.6
3. **Never a negative remaining number.** Zero and stop. §2.6
4. **No exercise credits, ever.** Never "breastfeeding earned you 500 cal". §2.1 §9
5. **Banned lexicon:** bounce back, get your body back, guilt, cheat, burn it off,
   earn your food, summer body, shred, detox. Also avoid wellness-speak she does
   not use: nourish, honour your body, love your body, journey, glow. §0A.6
6. **Sentence case. No ALL CAPS in content, no exclamation points.**
7. **Numbers always carry context.** "1,260 left — you're above your floor", never a naked figure.
8. **Nudges are never dismiss-only** — always offer the substitute and always a quiet "Not now".
9. **Tap targets ≥44pt**; check-in answer targets ≥56pt. Primary actions in the
   centre / lower third, never in a corner, never a top-right "+". §6.1
10. **Every state redundantly encoded** — hue AND geometry (dash/hatch/inset) AND
    icon. Amber and sage converge in dark mode. §4.5
11. **Adapted mode & numbers-off must feel like a sibling, not a downgrade.**
12. Placeholder wordmark only — the app is unnamed. Write it as `[app name]` in
    the direction's display face where a wordmark is needed.

---

## Captions are part of the deliverable

Under each phone write 2–3 `<p class="caption">` lines. Each starts with a bold
claim, then *why*, then a `<span class="cite">§x.y</span>` pointing at the
research section. Write for a cofounder deciding between directions — say what
the trade-off costs, not just what it does. Do not pad; three sharp lines beat six.

---

## Verify before you finish (required)

```
/private/tmp/claude-501/-Users-antnee-Documents-Projects-postPartum/7a716143-65fa-4029-aa14-9b9c6661540b/scratchpad/audit.sh YOURPAGE.html
```
Must print `CLEAN`. `OVERFLOW` = content taller than the 852pt screen: cut copy
or tighten spacing until it fits — never let a mock clip. `SMALLTAP` = a control
under 44pt: fix it.

Then screenshot at least two of your screens and LOOK at them:
```
/private/tmp/claude-501/-Users-antnee-Documents-Projects-postPartum/7a716143-65fa-4029-aa14-9b9c6661540b/scratchpad/shot.sh YOURPAGE.html <stageIndex> <name>
```
(stageIndex = 0-based index of `.stage` in page order.) Read the PNG with the
Read tool, judge it as a designer, fix what looks wrong, repeat. Do not report
done until the screenshots actually look good and the audit is CLEAN.
