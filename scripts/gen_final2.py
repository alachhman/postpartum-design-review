import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from sitegen import *
OUT="site"

# ============================ 07 PAYWALL ============================
def plan_card(d, annual=True):
    if annual:
        border = ("2px solid var(--accent)" if d=="a" else "2px solid var(--sage-7)" if d=="b" else "2px solid var(--accent)")
        return (f'<div class="{"card flat" if d=="a" else "card"} mt12" style="border:{border}">'
                f'<div class="row between"><span class="sec">A year</span>'
                f'<span class="chip on" style="height:26px;font-size:11px;padding:0 10px">Best value</span></div>'
                f'<div class="row between mt10" style="align-items:baseline">'
                f'<span style="font-size:28px;font-weight:{600 if d!="c" else 500}" class="tabnum">$79.99</span>'
                f'<span class="p" style="margin:0;font-size:13px">$6.67 a month</span></div></div>')
    return (f'<div class="{"card flat" if d=="a" else "card"} mt8">'
            f'<div class="row between" style="align-items:baseline"><span class="sec">A month</span>'
            f'<span style="font-size:19px;font-weight:{600 if d!="c" else 500}" class="tabnum">$12.99</span></div></div>')

def paywall(d):
    free = (f'<div class="{"card flat" if d=="a" else "card"} mt14" style="padding:13px 15px">'
            f'<div class="lbl">Free forever, with or without this</div>'
            f'<div class="p mt6" style="font-size:13px">Logging, your daily check-in, and the warning when a day '
            f'is heading under your floor. Safety isn’t behind the paywall.</div></div>')
    top = (f'<span class="{"kicker" if d!="c" else "sec"}">Your plan is ready</span>'
           f'<div class="greet mt10" style="font-size:{25 if d!="c" else 26}px">Seven days free, then decide</div>'
           f'<div class="p mt8" style="font-size:14px">Personalised targets, the nudges that tell you to eat more, '
           f'and your trends.</div>'
           f'{plan_card(d,True)}{plan_card(d,False)}'
           f'<div class="p mt10" style="font-size:12.5px">Free until 25 August. We’ll charge $79.99 then. '
           f'Cancel in Settings — two taps, and you keep the free parts.</div>'
           f'{free}')
    bot = ('<button class="btn'+(' primary' if d=="a" else '')+' big" style="width:100%">Start the free week</button>'
           '<button class="btn ghost mt4" style="width:100%">Keep using the free version</button>')
    return phone(d, top, bot, t="10:06", screen="t-day" if d=="c" else "")

FREE_ROWS = [("Logging food and weight","free"),("The daily check-in","free"),
             ("Floor-breach warnings","free"),("Your personalised target and floor","paid"),
             ("Nudges with one-tap adjustments","paid"),("Trends and days protected","paid")]
def split(d):
    rows="".join(
      f'<div class="listrow"><div class="grow"><div class="nm" style="font-size:14.5px">{n}</div></div>'
      f'<div class="{"val" if d!="c" else "nm"}" style="font-size:12px;color:var(--{"steady" if k=="free" else "ink-faint"})">'
      f'{"Free" if k=="free" else "Paid"}</div></div>' for n,k in FREE_ROWS)
    top = (f'<div class="greet" style="font-size:23px">What you get</div>'
           f'<div class="greet-sub">And what you keep if you don’t pay.</div>'
           f'<div class="mt16">{rows}</div>'
           f'<div class="{"card flat" if d=="a" else "card"} mt14" style="padding:12px 14px">'
           f'<div class="lbl">Reviewed by</div>'
           f'<div class="p mt6" style="font-size:13px">Dana Reyes, RD · Marta Okonjo, IBCLC</div>'
           f'<div class="p mt4" style="font-size:12px">They set the floors. Not a growth team.</div></div>')
    bot = '<button class="btn quiet" style="width:100%">Back</button>'
    return phone(d, top, bot, t="10:07", screen="t-day" if d=="c" else "")

P1={"a":["<b>The arithmetic does the selling.</b> $79.99 shown next to $6.67 a month, with the exact charge date and how to cancel. No timer, no crossed-out price, no “83% off”. <span class='cite'>§8.1</span>",
         "<b>Annual first because of how this ends.</b> Churn here is structural — users wean out in 12–18 months — so the annual plan is the honest way to capture the value, not a trick."],
    "b":["<b>The free tier is on the paywall, not in the footer.</b> It is what lets an IBCLC recommend the app, and it forecloses the “charges mothers for supply warnings” headline permanently. <span class='cite'>§brief 7</span>",
         "<b>No weekly plan.</b> It monetises confusion and churns 30–50% at first renewal. Leaving money on the table here is the brand."],
    "c":["<b>C almost undersells.</b> If the free tier genuinely covers safety, the paid tier has to earn its price on usefulness alone — which is the only version of this that survives an audience that discusses postpartum spending mostly as regret. <span class='cite'>§0A.4</span>",
         "<b>The credential is the pricing lever.</b> This audience judges paid nutrition advice on who stands behind the number, having been burned by an Instagram “dietitian” selling a 1,300-calorie plan. <span class='cite'>§0A.4</span>"]}
P2={"a":["<b>Two columns, no asterisks.</b> Anything ambiguous here reads as a trap to a reader primed for one."],
    "b":["<b>“Free” is a real word here.</b> Not a trial, not limited, not three logs a day."],
    "c":["<b>Placeholder names.</b> Recruiting the RD and IBCLC is a launch prerequisite — this screen is where that recruitment converts into revenue."]}

page07 = (head("Paywall — three directions") + nav("07-paywall.html")
 + hero("Screen 07 · plan activation", "Paywall",
        "Shown at the moment her plan is revealed, not on launch. Annual first, no weekly tier, and the free safety layer stated out loud on the screen that is asking for money.",
        ["$79.99/yr · $12.99/mo","7-day trial, card required","Safety never paywalled"])
 + callout("The two constraints that shape this screen",
   "First: <b>safety is never behind the paywall</b> — logging, the check-in and floor warnings stay free forever, because that is what makes the app recommendable by a lactation consultant and what prevents a headline nobody recovers from. Second: <b>the credential is the pricing lever.</b> This audience decides whether to pay for nutrition advice based on who stands behind the number, and they have been burned badly enough that the reviewing clinicians need to be named before the ask, not after. <span class='cite'>§0A.4 · §brief 7</span>")
 + block("paywall","The ask","$79.99 a year, with the monthly beneath it and the free tier beside it.",
   [spec(d,"annual first",[paywall(d)],P1[d]) for d in "abc"])
 + block("split","Free and paid, in the product","Reachable any time from settings, so the split is never something she has to remember from a screen she saw once.",
   [spec(d,"the split",[split(d)],P2[d]) for d in "abc"])
 + '''<div class="wrap"><section class="screenblock">
  <div class="screenhead"><h2>What is deliberately absent</h2>
  <p class="note">Each of these is standard in the category and each one is a reason this audience says they pull back.</p></div>
  <table class="tbl">
    <tr><th style="width:28%">Common pattern</th><th>Why it is not here</th></tr>
    <tr><td>Countdown timer on the offer</td><td>Manufactured urgency, and the single most-named dark pattern in the review corpus.</td></tr>
    <tr><td>Crossed-out “was $199”</td><td>A price that was never charged. Trust is the whole product.</td></tr>
    <tr><td>Weekly tier at $4.99</td><td>Monetises confusion, churns 30–50% at first renewal, and is off-brand for a trust-led product.</td></tr>
    <tr><td>Paywalled barcode scanner</td><td>The biggest single churn driver in this category. It stays free.</td></tr>
    <tr><td>Free tier limited to N logs a day</td><td>Would make the free safety layer decorative, which defeats the point of having one.</td></tr>
    <tr><td>Interstitial ads</td><td>No third-party advertising data sharing, ever. It is a stated differentiator, and reviewers describe ads appearing while they eat.</td></tr>
  </table>
 </section></div>'''
 + foot(("06-trends.html","Trends"),("08-adapted.html","Adapted mode")))
open(f"{OUT}/07-paywall.html","w").write(page07); print("07", len(page07))

# ============================ 08 ADAPTED ============================
def adapted_home(d):
    if d=="a":
        hero = ('<div class="ledger mt20"><div class="k">Today</div>'
                '<div class="n tabnum" style="font-size:66px">74<u>g protein</u></div>'
                '<div class="say">Out of about 110 on a normal day.</div></div>'
                '<div class="fbar"><div class="track"><div class="band"></div>'
                '<div class="under" style="width:78.26%"></div><div class="fill safe" style="width:67%"></div>'
                '<div class="tick" style="left:78.26%"></div></div>'
                '<div class="ticklab" style="left:78.26%">Enough</div>'
                '<div class="ends"><span></span><span>eating steadily</span><span></span></div></div>')
    elif d=="b":
        hero = ('<div class="card tint mt16"><div class="row between"><span class="sec">Protein today</span>'
                '<span style="font-size:22px;font-weight:800" class="tabnum">74 g</span></div>'
                '<div class="mt10" style="position:relative;height:12px;border-radius:7px;background:var(--surface);overflow:hidden">'
                '<div style="position:absolute;inset:0 auto 0 0;width:67%;background:var(--sage);border-radius:7px"></div></div>'
                '<div class="p mt8" style="font-size:13px">Out of about 110 on a normal day.</div></div>'
                '<div class="card mt10"><div class="row between"><span class="sec">Energy this week</span>'
                '<span style="font-size:16px;font-weight:800">Better than last</span></div></div>')
    else:
        hero = ('<div class="mt20"><div class="sec">Last 30 days</div>'
                '<div class="hero-n mt10">26<u>days you ate enough</u></div>'
                '<div class="field mt14">' + "".join('<i></i>' if i not in (7,14,15,21) else
                 ('<i class="pause"></i>' if i in (14,15) else '<i class="thin"></i>') for i in range(30)) + '</div></div>'
                '<div class="hero-say mt16">No target to miss. Just enough, most days.</div>')
    top = (f'<div class="greet">Good morning, Sarah</div><div class="greet-sub">Eleven weeks in. Combo feeding.</div>'
           + banner(d,"steady","Steady — 5 days","Your check-ins have been in your usual range.").replace('class="banner"','class="banner mt16"') + hero)
    bot = ('<div class="qa"><button class="qa-item'+(' accent' if d!="c" else '')+'"><span class="d">10 sec</span><span class="t">Log food</span></button>'
           '<button class="qa-item"><span class="d">3 taps</span><span class="t">Daily check-in</span></button></div>') if d!="c" else \
          ('<button class="btn" style="width:100%">Check in — 10 seconds</button>'
           '<button class="btn ghost mt4" style="width:100%">Log something</button>')
    return phone(d, top, bot, t="8:12", screen="t-day" if d=="c" else "")

def numbers_off(d):
    if d=="a":
        hero = ('<div class="ledger mt20"><div class="k">Today</div>'
                '<div class="say" style="font-size:26px;margin-top:12px;line-height:1.24">You’ve eaten enough to be above your floor.</div></div>'
                '<div class="fbar"><div class="track"><div class="band"></div>'
                '<div class="under" style="width:78.26%"></div><div class="fill safe" style="width:88%"></div>'
                '<div class="tick" style="left:78.26%"></div></div>'
                '<div class="ends" style="margin-top:14px"><span>not yet</span><span></span><span>enough</span></div></div>')
    elif d=="b":
        hero = ('<div class="ringwrap mt14"><svg viewBox="0 0 242 242">'
                '<g transform="rotate(-90 121 121)">'
                '<circle cx="121" cy="121" r="100" fill="none" stroke="var(--surface-2)" stroke-width="24"/>'
                '<circle cx="121" cy="121" r="100" fill="none" stroke="var(--sage-1)" stroke-width="24" stroke-dasharray="136.6 491.7" stroke-dashoffset="-491.7"/>'
                '<circle cx="121" cy="121" r="100" fill="none" stroke="var(--sage)" stroke-width="24" stroke-dasharray="553.0 75.3" stroke-linecap="round"/></g>'
                '<line x1="9.3" y1="98.0" x2="36.8" y2="103.7" stroke="var(--ink)" stroke-width="3.5" stroke-linecap="round"/></svg>'
                '<div class="ring-c"><div class="ring-u" style="font-size:17px;line-height:1.3;font-weight:800;color:var(--ink)">Above your floor</div></div></div>'
                '<div class="bandlab"><span class="sw"></span>In the protected band</div>')
    else:
        hero = ('<div class="mt24"><div class="sec">Today</div>'
                '<div class="hero-say" style="font-size:24px;margin-top:12px">You’ve eaten enough today.</div>'
                '<div class="field mt18">' + "".join('<i></i>' if i not in (7,14,15,21) else
                 ('<i class="pause"></i>' if i in (14,15) else '<i class="thin"></i>') for i in range(30)) + '</div>'
                '<div class="p mt12">Green means you were above your floor. That’s the only number that matters, and you don’t have to see it.</div></div>')
    top = (f'<div class="greet">Good morning, Sarah</div><div class="greet-sub">Eleven weeks in. Combo feeding.</div>'
           + banner(d,"steady","Steady — 5 days","Your check-ins have been in your usual range.").replace('class="banner"','class="banner mt16"') + hero)
    bot = ('<button class="btn quiet" style="width:100%">Log something</button>'
           '<button class="btn ghost mt4" style="width:100%">Show the numbers again</button>')
    return phone(d, top, bot, t="8:12", screen="t-day" if d=="c" else "")

STATES=["Baby is sick","I’m sick","Cluster feeding","Travelling","In hospital"]
def suspend(d):
    if d=="c":
        body='<div class="coarse mt16">'+"".join(f'<button class="{"on" if i==0 else ""}"><span class="mk"></span>{x}</button>' for i,x in enumerate(STATES))+'</div>'
    else:
        body='<div class="mt12">'+"".join(f'<button class="btn {("primary" if d=="a" else "") if i==0 else "quiet"} mt8" style="width:100%;min-height:52px;justify-content:flex-start;padding-left:18px">{x}</button>' for i,x in enumerate(STATES))+'</div>'
    top=(f'<div class="greet" style="font-size:24px">What’s going on?</div>'
         f'<div class="p mt8" style="font-size:14px">I’ll stop counting missed days until you tell me it’s over. '
         f'Your streak stays where it is and nothing goes down as a miss.</div>{body}')
    bot='<button class="btn ghost" style="width:100%">Never mind</button>'
    return phone(d, top, bot, t="6:40", screen="t-day" if d=="c" else "")

A1={"a":["<b>The hero changes, the layout doesn’t.</b> Protein where calories were, in the same slot at the same size — so it reads as a different plan, not a stripped one. <span class='cite'>§style guide</span>"],
    "b":["<b>The supply banner stays.</b> Safety information is never what gets removed in adapted mode; only the loss framing goes."],
    "c":["<b>No deficit, no streak, no target to miss.</b> “Enough, most days” is the whole scoring system, and it cannot be failed on a hard week."]}
A2={"a":["<b>The bar answers the question without a number.</b> Position past the tick, plus the words “above your floor” — she can still tell she is safe, which is the requirement. <span class='cite'>§8.2-J</span>"],
    "b":["<b>The ring keeps working with nothing in the middle.</b> Fill past the sector into the band is a complete answer on its own."],
    "c":["<b>Arguably this should be core, not a mode.</b> It was user-requested, it costs almost nothing to build, and it is the single strongest signal that this is not a diet app. <span class='cite'>§8.2-J</span>"]}
A3={"a":["<b>Forgiving by mechanism, not by tone.</b> Gentle copy on a streak that still breaks is just a nicer way to lose it. <span class='cite'>§6.4</span>"],
    "b":["<b>Two award-winning apps landed on this independently</b> — declarable life states that pause evaluation without breaking the chain."],
    "c":["<b>This is the eating-disorder answer.</b> A streak that circumstance cannot break cannot be turned into an instrument for punishing herself. <span class='cite'>§6.4 · §9</span>"]}

page08 = (head("Adapted mode — three directions") + nav("08-adapted.html")
 + hero("Screen 08 · the sibling", "Adapted mode",
        "Switched on by one gentle question during onboarding. No deficit, no streak pressure, no loss language — and it has to look like a considered product in its own right, not the real app with things taken away.",
        ["No deficit by default","Numbers-off available to everyone","Declarable suspension states"])
 + callout("The bar this page has to clear",
   "If adapted mode looks like the main app with features removed, it has failed. She will read the subtraction instantly and correctly as being handed the lesser version. Everything below keeps the same layout, the same hierarchy and the same visual weight — what changes is which number sits in the hero slot and what the copy is allowed to say.")
 + block("home","Adapted-mode home","Compare directly against screen 01. Same structure, same supply banner, different hero and different vocabulary.",
   [spec(d,"no deficit, no streaks",[adapted_home(d)],A1[d]) for d in "abc"])
 + block("off","Numbers off",
   "Every figure suppressed. The design problem: she must still be able to tell whether she is above her floor. All three solve it with position and plain words instead of a value.",
   [spec(d,"no figures anywhere",[numbers_off(d)],A2[d]) for d in "abc"])
 + block("suspend","Suspension states",
   "Baby is sick, I’m sick, cluster feeding, travelling, in hospital. Missed-day accounting stops, the streak holds, and the copy changes.",
   [spec(d,"life happens",[suspend(d)],A3[d]) for d in "abc"])
 + callout("Why this is not an accessibility afterthought",
   "In a clinical sample of people with diagnosed eating disorders, around three quarters had used MyFitnessPal — and of those, <b>73% said it contributed to their disorder, 30% “very much”.</b> That is the risk this mode exists to answer. Building it well, making numbers-off available to everyone rather than only to the cohort that discloses, and letting a streak survive a sick baby are the strongest available evidence that the product’s central claim is real. <span class='cite'>§9 · §8.2-J</span>", "ok")
 + foot(("07-paywall.html","Paywall"),("index.html","Back to overview")))
open(f"{OUT}/08-adapted.html","w").write(page08); print("08", len(page08))
