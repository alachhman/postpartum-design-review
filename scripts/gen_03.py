import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from sitegen import *
OUT="site"

FOODS = [("Peanut butter on toast","+330"),("Greek yoghurt and honey","+280"),("Big glass of whole milk","+150")]

def food_rows(d, show_bar=True):
    out=[]
    for i,(n,delta) in enumerate(FOODS):
        if d=="a":
            bar = ('<div class="fbar" style="margin-top:9px"><div class="track" style="height:8px">'
                   '<div class="band"></div><div class="under" style="width:78.26%"></div>'
                   f'<div class="fill" style="width:51.3%"></div>'
                   f'<div class="fill" style="width:{51.3+ (330 if i==0 else 280 if i==1 else 150)/23:.1f}%;opacity:.3"></div>'
                   '<div class="tick" style="left:78.26%"></div></div></div>') if show_bar else ""
            out.append(f'<button class="card flat mt8" style="width:100%;text-align:left;display:block;cursor:pointer">'
                       f'<div class="row between"><span style="font-size:15px;font-weight:500">{n}</span>'
                       f'<span class="mono" style="font-size:13px;color:var(--accent);font-weight:600">{delta}</span></div>{bar}</button>')
        elif d=="b":
            out.append(f'<button class="card mt8" style="width:100%;text-align:left;display:block;cursor:pointer;padding:13px 15px">'
                       f'<div class="row between"><span style="font-size:15.5px;font-weight:700">{n}</span>'
                       f'<span style="font-size:14px;color:var(--sage-7);font-weight:800">{delta}</span></div>'
                       f'<div class="mt8" style="position:relative;height:8px;border-radius:5px;background:var(--surface-2);overflow:hidden">'
                       f'<div style="position:absolute;inset:0 auto 0 0;width:51.3%;background:var(--sage);border-radius:5px"></div>'
                       f'<div style="position:absolute;inset:0 auto 0 0;width:{51.3+(330 if i==0 else 280 if i==1 else 150)/23:.1f}%;background:var(--sage);opacity:.34;border-radius:5px"></div>'
                       f'<div style="position:absolute;top:0;bottom:0;left:78.26%;width:2px;background:var(--ink)"></div></div></button>')
        else:
            note = ["gets you most of the way","gets you most of the way","a decent dent"][i]
            out.append(f'<button class="card quiet mt8" style="width:100%;text-align:left;display:block;cursor:pointer;border-style:solid">'
                       f'<div style="font-size:16px;font-weight:500">{n}</div>'
                       f'<div class="p mt4" style="font-size:13px">{note}</div></button>')
    return "".join(out)

# ---------------- 1. supply-protect ----------------
def protect(d):
    if d=="a":
        top = ('<div class="sheet" style="padding:0"><span class="kicker">Two days below your usual</span>'
               '<h1>Let’s ease up for two days</h1>'
               '<p class="why">Your check-ins have been lower than usual, and you finished under 1,800 on both days. '
               'Eating a bit more for a couple of days is the usual fix.</p>'
               '<div class="row gap14 mt24"><div class="stat"><div class="statn">2,000</div><div class="statl">Target now</div></div>'
               '<div class="stat" style="color:var(--accent)"><div class="statn">2,300</div><div class="statl">For two days</div></div>'
               '<div class="stat"><div class="statn">1,800</div><div class="statl">Floor, unchanged</div></div></div>'
               f'<div class="mt20"><div class="lbl">Easy ways to get there</div>{food_rows("a")}</div></div>')
        bot = ('<button class="btn primary big" style="width:100%">Raise my target to 2,300</button>'
               '<button class="btn ghost mt4" style="width:100%">Not now</button>'
               '<div class="p tc mt6" style="font-size:12px">Nothing changes unless you tap.</div>')
    elif d=="b":
        top = ('<div class="sheet" style="padding:0"><span class="kicker">Two days below your usual</span>'
               '<h1>Let’s ease up for two days</h1>'
               '<p class="why">Your check-ins have been lower than usual, and you finished under 1,800 on both days. '
               'Eating a bit more for a couple of days is the usual fix.</p>'
               '<div class="card tint mt20"><div class="row between"><span class="sec">Target</span>'
               '<span style="font-size:17px;font-weight:800">2,000 → <span style="color:var(--sage-8)">2,300</span></span></div>'
               '<div class="p mt6" style="font-size:13px">Your floor stays at 1,800.</div></div>'
               f'<div class="mt16"><div class="sec">Easy ways to get there</div>{food_rows("b")}</div></div>')
        bot = ('<button class="btn big" style="width:100%">Raise my target to 2,300</button>'
               '<button class="btn ghost mt4" style="width:100%">Not now</button>'
               '<div class="p tc mt6" style="font-size:12.5px">Nothing changes unless you tap.</div>')
    else:
        top = ('<div class="sheet" style="padding:0"><div class="breath mt14"></div>'
               '<h1 class="tc mt20" style="font-size:32px">Let’s ease up for two days</h1>'
               '<p class="why tc">Your last two check-ins were lower than usual for you, and both days finished under your floor.</p>'
               f'<div class="mt20"><div class="sec">A couple of easy ones</div>{food_rows("c")}</div></div>')
        bot = ('<button class="btn held big" style="width:100%">Eat a bit more for two days</button>'
               '<button class="btn ghost mt4" style="width:100%">Not now</button>'
               '<div class="p tc mt6" style="font-size:12.5px">Nothing changes unless you tap.</div>')
    return phone(d, top, bot, t="4:12", batt=11, screen="t-dusk" if d=="c" else "", frame="night" if d=="c" else "")

# ---------------- 2. floor breach ----------------
def breach(d):
    if d=="a":
        top = ('<div class="sheet" style="padding:0"><span class="kicker">Heads up</span>'
               '<h1>Today’s heading under 1,800</h1>'
               '<p class="why">You’re at 1,180 with about four hours left. On a normal day you’d be at 1,600 by now.</p>'
               '<div class="fbar mt24"><div class="track"><div class="band"></div>'
               '<div class="under" style="width:78.26%"></div><div class="fill" style="width:51.3%"></div>'
               '<div class="fill" style="width:70.4%;opacity:.34"></div><div class="tick" style="left:78.26%"></div></div>'
               '<div class="ticklab" style="left:78.26%">Floor 1,800</div>'
               '<div class="ends"><span>0</span><span>on track for 1,620</span><span>2,300</span></div></div>'
               f'<div class="mt18"><div class="lbl">620 to go</div>{food_rows("a", show_bar=False)}</div></div>')
        bot = ('<button class="btn primary big" style="width:100%">Log something now</button>'
               '<button class="btn ghost mt4" style="width:100%">I’ll sort it</button>')
        return phone("a", top, bot, t="7:48", batt=10, screen="inverted")
    if d=="b":
        top = ('<div class="sheet" style="padding:0"><span class="kicker">Heads up</span>'
               '<h1>Today’s heading under 1,800</h1>'
               '<p class="why">You’re at 1,180 with about four hours left. On a normal day you’d be at 1,600 by now.</p>'
               '<div class="card mt20" style="border:1.5px solid var(--coral)">'
               '<div class="row between"><span class="sec">On track for</span>'
               '<span style="font-size:19px;font-weight:800;color:var(--coral)">1,620</span></div>'
               '<div class="mt10" style="position:relative;height:12px;border-radius:7px;background:var(--surface-2);overflow:hidden">'
               '<div style="position:absolute;inset:0 auto 0 0;width:51.3%;background:var(--sage);border-radius:7px"></div>'
               '<div style="position:absolute;inset:0 auto 0 0;width:70.4%;background:var(--sage);opacity:.34;border-radius:7px"></div>'
               '<div style="position:absolute;top:0;bottom:0;left:78.26%;width:2.5px;background:var(--ink)"></div></div>'
               '<div class="p mt8" style="font-size:13px">620 short of your floor.</div></div>'
               f'<div class="mt14">{food_rows("b")}</div></div>')
        bot = ('<button class="btn stop big" style="width:100%">Log something now</button>'
               '<button class="btn ghost mt4" style="width:100%">I’ll sort it</button>')
        return phone("b", top, bot, t="7:48", batt=10)
    top = ('<div class="sheet" style="padding:0"><div class="breath mt10"></div>'
           '<h1 class="tc mt18" style="font-size:31px">Today’s heading under your floor</h1>'
           '<p class="why tc">You’re about 620 short with a few hours left.</p>'
           f'<div class="mt18"><div class="sec">A couple of easy ones</div>{food_rows("c")}</div></div>')
    bot = ('<button class="btn big" style="width:100%">Log something now</button>'
           '<button class="btn ghost mt4" style="width:100%">I’ll sort it</button>')
    return phone("c", top, bot, t="7:48", batt=10, screen="t-night", frame="night")

# ---------------- 3. escalation ----------------
def escalate(d):
    common_h = "Four days now"
    why = ("Your check-ins have been below your usual for four days, and eating more hasn’t shifted it. "
           "That’s further than I can work out from three questions a day.")
    if d=="a":
        top = ('<div class="sheet" style="padding:0"><span class="kicker">Worth a conversation</span>'
               f'<h1>{common_h}</h1><p class="why">{why}</p>'
               '<div class="card flat mt24"><div class="lbl">A lactation consultant can</div>'
               '<div class="p mt8" style="font-size:14px">Watch a feed, check the latch, and weigh the baby before and after. '
               'None of that is something an app can do.</div></div>'
               '<div class="p mt14" style="font-size:13.5px">Most US insurance plans cover these visits in full.</div></div>')
        bot = ('<button class="btn primary big" style="width:100%">Find an IBCLC near me</button>'
               '<button class="btn quiet mt8" style="width:100%">Check what my insurance covers</button>'
               '<button class="btn ghost mt4" style="width:100%">Remind me tomorrow</button>')
    elif d=="b":
        top = ('<div class="sheet" style="padding:0"><span class="kicker">Worth a conversation</span>'
               f'<h1>{common_h}</h1><p class="why">{why}</p>'
               '<div class="card tint mt20"><div class="sec">A lactation consultant can</div>'
               '<div class="p mt8" style="font-size:14px">Watch a feed, check the latch, and weigh the baby before and after — '
               'none of which an app can do.</div></div>'
               '<div class="p mt14" style="font-size:13.5px">Most US insurance plans cover these visits in full.</div></div>')
        bot = ('<button class="btn big" style="width:100%">Find an IBCLC near me</button>'
               '<button class="btn quiet mt8" style="width:100%">Check what my insurance covers</button>'
               '<button class="btn ghost mt4" style="width:100%">Remind me tomorrow</button>')
    else:
        top = ('<div class="sheet" style="padding:0"><span class="kicker">Worth a conversation</span>'
               f'<h1>{common_h}</h1><p class="why">{why}</p>'
               '<div class="card mt20"><div class="sec">What they can do that I can’t</div>'
               '<div class="p mt8">Watch a feed, check the latch, weigh the baby before and after.</div></div>'
               '<div class="p mt14">Most US insurance plans cover these visits in full.</div></div>')
        bot = ('<button class="btn big" style="width:100%">Find an IBCLC near me</button>'
               '<button class="btn quiet mt8" style="width:100%">Check my insurance</button>'
               '<button class="btn ghost mt4" style="width:100%">Remind me tomorrow</button>')
    return phone(d, top, bot, t="9:02", screen="t-day" if d=="c" else "")

C1 = {"a":["<b>One tap, and only on her tap.</b> The target never moves on its own, which is both the trust argument and the cleaner liability posture. <span class='cite'>§brief 5.1</span>",
           "<b>Each suggestion previews itself on the bar.</b> The pale extension shows where the toast lands her before she commits — interrupt and offer the fix, never interrupt and leave. <span class='cite'>§8.2-H · §6.5</span>"],
      "b":["<b>The floor is untouched.</b> Only the target moves. Saying so on the screen stops the adjustment reading as the app quietly lowering its own standards.",
           "<b>Warm, but no reward layer.</b> No streak bonus, no badge, no confetti. A mother at 3am does not want to earn anything. <span class='cite'>§6.5</span>"],
      "c":["<b>A breath before the ask.</b> A short pause beats a hard block — forced friction is what lets someone make the choice consciously instead of reflexively dismissing. <span class='cite'>§6.5</span>",
           "<b>No numbers unless she wants them.</b> The suggestions are described by effect rather than calorie count, which is the only version of this screen that works in numbers-off mode. <span class='cite'>§8.2-J</span>"]}
C2 = {"a":["<b>This is A’s whole argument in one screen.</b> Below the floor, the screen inverts in value rather than turning red. Colourblind-safe, dark-mode-safe, and it does not read as an alarm. <span class='cite'>§2.5 · §2.6</span>",
           "<b>Under-eating by 600 calories on a hard day is not a medical emergency.</b> Dexcom can use red because a hypo is acute. This isn’t, and treating it as such teaches her to dread the app."],
      "b":["<b>Predictive, not retrospective.</b> It fires at 7:48pm on a projection, not at 11:59 on a fact — by midnight the information is useless. Borrowed from Dexcom’s “urgent low soon”. <span class='cite'>§2.7</span>",
           "<b>Coral appears here and nowhere else.</b> Reserved so it always means stop, and darkened to 5.22:1 so it is legible as text. <span class='cite'>§4.1</span>"],
      "c":["<b>Desaturated at night, never alarming.</b> A pure-black screen with a saturated red warning reads as a hospital monitor to someone holding an infant at 3am. <span class='cite'>§4.4</span>",
           "<b>“I’ll sort it” is a real answer.</b> Dismissal without guilt has to be one tap, or she will start dismissing the app entirely."]}
C3 = {"a":["<b>The app says what it cannot do.</b> Naming the limit is the ethical move and the liability posture at once. <span class='cite'>§brief 5.4</span>",
           "<b>Insurance, not price.</b> This audience discusses lactation consultants through coverage rather than cash cost, so that is the framing that converts. <span class='cite'>§0A.4</span>"],
      "b":["<b>Escalation is the only nudge that gets louder.</b> Everything else stays a quiet card; this one earns a full screen at four days. <span class='cite'>§brief 5</span>",
           "<b>No diagnosis, no cause.</b> It reports the pattern and hands her to a human — it never speculates about why."],
      "c":["<b>Referral is a feature, not a failure.</b> Being the app IBCLCs recommend is the actual moat, and that starts with the app sending people to them. <span class='cite'>§0A.4</span>",
           "<b>Check the crisis numbers before launch.</b> A competitor still ships pre-988 lifeline copy. Whatever resources ship here need auditing against current numbers. <span class='cite'>§7</span>"]}

page = (head("Nudges — three directions") + nav("03-nudges.html")
 + hero("Screen 03 · the product promise", "The two moments",
        "Everything else in the app is a tracker. These two screens are the reason it exists: the one that tells her to eat more, and the one that catches a day before it lands under the floor.",
        ["Full-screen · families 1 and 2","Max one push per day","Never a silent adjustment"])
 + callout("The gate, before any of this fires",
   "No nudge unless something specific in yesterday’s data bears on today. Never a scheduled nudge, never a daily prompt dressed as insight. That rule is what keeps the one-push-a-day budget honest, and it is the difference between an app that pays attention so she doesn’t have to and an app that just pings.")
 + block("protect","Supply-protect",
   "Her check-ins dipped two days running and she finished under her floor on both. This is the hero moment — calm, specific, and answerable with one thumb.",
   [spec("a","one-tap accept",[protect("a")],C1["a"]),
    spec("b","one-tap accept",[protect("b")],C1["b"]),
    spec("c","breath first",[protect("c")],C1["c"])])
 + block("breach","Floor-breach interrupt",
   "7:48pm. She is at 1,180 and the day is projected to land at 1,620. It fires now, while she can still do something about it.",
   [spec("a","value inversion",[breach("a")],C2["a"]),
    spec("b","coral, used once",[breach("b")],C2["b"]),
    spec("c","night palette",[breach("c")],C2["c"])])
 + block("escalate","Escalation",
   "Four days of dipped check-ins that eating more has not shifted. The app stops trying to solve it and hands her to a human.",
   [spec("a","hands off to a human",[escalate("a")],C3["a"]),
    spec("b","hands off to a human",[escalate("b")],C3["b"]),
    spec("c","hands off to a human",[escalate("c")],C3["c"])])
 + '''<div class="wrap"><section class="screenblock anchor" id="budget">
  <div class="screenhead"><h2>The notification budget</h2>
  <p class="note">One push per day, hard cap. Everything below the line lives in the app and waits until she opens it. New mothers are drowning in pings; restraint is the feature.</p></div>
  <table class="tbl">
    <tr><th style="width:22%">Family</th><th style="width:18%">Loudness</th><th style="width:16%">Push priority</th><th>Fires when</th></tr>
    <tr><td>Floor breach</td><td>Full screen</td><td class="mono">1 — always wins</td><td>Today is projected to land under the floor, with hours left to fix it.</td></tr>
    <tr><td>Supply-protect</td><td>Full screen</td><td class="mono">2</td><td>Check-ins below her usual two days running <em>and</em> intake under target on two of the last three.</td></tr>
    <tr><td>Escalation</td><td>Card, full screen at four days</td><td class="mono">3</td><td>Dip persists four days regardless of intake. Points to an IBCLC.</td></tr>
    <tr><td>Hydration</td><td>In-app card</td><td class="mono">4</td><td>Never pushes if anything above it fired today.</td></tr>
    <tr><td>Streaks and protein</td><td>In-app card only</td><td class="mono">never pushes</td><td>She sees it when she opens the app, or she doesn’t.</td></tr>
  </table>
  <div class="callout ok"><span class="lab">What this rules out</span>
    No daily “time to log!” reminder. No streak-loss warning. No re-engagement push after three quiet days.
    Those are the four notifications every competitor sends, and they are the reason this audience turns
    notifications off — at which point the floor-breach warning, the one message that actually matters,
    never arrives either.</div>
 </section></div>'''
 + foot(("02-checkin.html","Check-in"),("04-onboarding.html","Onboarding")))
open(f"{OUT}/03-nudges.html","w").write(page)
print("03-nudges.html", len(page), "bytes")
