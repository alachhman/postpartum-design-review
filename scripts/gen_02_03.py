import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from sitegen import *

OUT = "site"

# =====================================================================
# 02 — CHECK-IN
# =====================================================================
Q = [("Did your feeds feel like they usually do?", ["Yes","Somewhat","No"], 0),
     ("How was pumping today, next to your usual?", ["More","Same","Less","Didn’t pump"], 1),
     ("Did the baby seem settled after feeds?", ["Yes","Not sure","No"], 0)]

def a_step(i):
    q,ans,sel = Q[i]
    rows = "".join(
      f'<button class="btn {"primary" if j==sel else "quiet"} mt10" style="width:100%;min-height:58px;justify-content:flex-start;padding-left:18px">{a}</button>'
      for j,a in enumerate(ans))
    return phone("a",
      f'<div class="row between">{dots(3,i)}<span class="lbl">{i+1} of 3</span></div>'
      f'<div class="greet mt24" style="font-size:24px">{q}</div>'
      f'<div class="p mt8" style="font-size:13.5px">Compared with a normal day for you.</div>{rows}',
      f'<button class="btn ghost" style="width:100%">Skip this one</button>', t="7:12", sm=True)

def b_step(i):
    q,ans,sel = Q[i]
    rows = "".join(
      f'<button class="btn {"" if j==sel else "quiet"} mt10" style="width:100%;min-height:58px">{a}</button>'
      for j,a in enumerate(ans))
    return phone("b",
      f'<div class="row between">{dots(3,i)}<span class="lbl">{i+1} of 3</span></div>'
      f'<div class="greet mt24" style="font-size:23px">{q}</div>'
      f'<div class="p mt8" style="font-size:13.5px">Compared with a normal day for you.</div>{rows}',
      f'<button class="btn ghost" style="width:100%">Skip this one</button>', t="7:12", sm=True)

def c_step(i, night=False):
    q,ans,sel = Q[i]
    rows = "".join(
      f'<button class="{"on" if j==sel else ""}"><span class="mk"></span>{a}</button>' for j,a in enumerate(ans))
    return phone("c",
      f'<div class="row between">{dots(3,i)}<span class="lbl">{i+1} of 3</span></div>'
      f'<div class="greet mt24" style="font-size:25px">{q}</div>'
      f'<div class="p mt8">Compared with a normal day for you.</div>'
      f'<div class="coarse mt18">{rows}</div>',
      f'<button class="btn ghost" style="width:100%">Skip this one</button>',
      t="3:24" if night else "7:12", batt=9 if night else 16,
      screen="t-night" if night else "t-day", frame="night" if night else "", sm=True)

DONE_TOP = ('{banner}'
  '<div class="mt20"><div class="sec">Today</div>'
  '<div class="mt8"><div class="listrow"><div class="grow"><div class="nm">Feeds</div></div><div class="{val}">Normal</div></div>'
  '<div class="listrow"><div class="grow"><div class="nm">Pumping</div></div><div class="{val}">Same as usual</div></div>'
  '<div class="listrow"><div class="grow"><div class="nm">Baby after feeds</div></div><div class="{val}">Settled</div></div></div></div>')

def done(d):
    val = "val" if d!="c" else "nm"
    top = ('<div class="greet">Saved.</div><div class="greet-sub">Five days in a row.</div>'
           + DONE_TOP.format(banner=banner(d,"steady","Steady — 5 days","Your answers have been in your usual range."), val=val).replace('class="mt20"','class="mt18"'))
    bot = ('<button class="btn quiet" style="width:100%">Something’s off today</button>'
           '<button class="btn ghost mt4" style="width:100%">Done</button>')
    return phone(d, top, bot, t="7:12", sm=True,
                 screen="t-day" if d=="c" else "")

PAUSE = [("Baby is sick",""),("I’m sick",""),("Cluster feeding",""),("Travelling",""),("In hospital","")]
def pause(d):
    if d=="c":
        rows = "".join(f'<button class="{"on" if i==0 else ""}"><span class="mk"></span>{p}</button>' for i,(p,_) in enumerate(PAUSE))
        body = f'<div class="coarse mt18">{rows}</div>'
    else:
        body = "".join(f'<button class="btn {"primary" if (i==0 and d=="a") else ("" if i==0 else "quiet")} mt8" style="width:100%;min-height:52px">{p}</button>' for i,(p,_) in enumerate(PAUSE))
        body = f'<div class="mt14">{body}</div>'
    return phone(d,
      f'<div class="greet" style="font-size:24px">What’s going on?</div>'
      f'<div class="p mt8">We’ll stop counting missed days until you say it’s over. Your streak stays where it is.</div>{body}',
      '<button class="btn ghost" style="width:100%">Never mind</button>', t="7:13", sm=True,
      screen="t-day" if d=="c" else "")

def unknown(d):
    top = (f'<div class="greet">Morning, Sarah</div><div class="greet-sub">Eleven weeks in. Combo feeding.</div>'
           + banner(d,"unknown","Not enough check-ins to say","Two missed days. A couple more and I can tell you how you’re tracking.").replace('class="banner','class="banner mt18" data-x="banner')
           + '<div class="p mt20" style="font-size:14px">Missed days usually happen on the hardest days, so I won’t read them as good news.</div>')
    return phone(d, top, '<button class="btn" style="width:100%">Check in — 10 seconds</button>',
                 t="8:40", sm=True, screen="t-day" if d=="c" else "")

CAPS = {
 "a": ["<b>The question is the label.</b> Each step asks what it answers rather than naming a metric, which keeps the input honestly subjective — required, because pump output is not a valid measure of supply. <span class='cite'>§3.2 · §1.1</span>",
       "<b>Answer targets are 58pt.</b> Above the 44pt iOS minimum and close to the 20mm that solves nearly all one-handed error. She is holding a baby. <span class='cite'>§6.1</span>",
       "<b>Skip is always there.</b> A step she can’t answer must not block the other two, and a forced answer is a false answer."],
 "b": ["<b>Every comparison is to her own usual.</b> Never “typical”, never other women. That single grammatical choice is what separates a defensible wellness claim from a clinical one. <span class='cite'>§1.1 · §3.1</span>",
       "<b>Saved before the last tap.</b> State persists after every step, not on submit — she will be interrupted, and a silent save failure in a supply tracker is credibility poison. <span class='cite'>§6.3</span>",
       "<b>The done state reports, it does not judge.</b> “Steady — 5 days” is a statement about her answers. “Your supply is good” is a claim the app cannot make."],
 "c": ["<b>Step three runs in the 2–5am palette.</b> That is when this actually gets used, so it is designed as a first-class state rather than a dark-mode afterthought, at a 20pt type floor. <span class='cite'>§4.4 · §1.4</span>",
       "<b>“Something’s off today” is the whole streak mechanic.</b> Declaring baby is sick or cluster feeding suspends missed-day counting and keeps the streak. A streak that circumstance cannot break cannot be used to punish herself. <span class='cite'>§6.4 · §10</span>",
       "<b>The third state is the one most apps skip.</b> Two missed check-ins render as “not enough to say”, never silently as steady — and missed days correlate with the hardest days, so naive logic would read exhaustion as improvement. <span class='cite'>§8.2-I · §1.1</span>"],
}

specs = []
for d, stepf in (("a",a_step),("b",b_step),("c",c_step)):
    if d=="c":
        ph = [c_step(0), c_step(1), c_step(2, night=True), done("c"), pause("c"), unknown("c")]
    else:
        ph = [stepf(0), stepf(1), stepf(2), done(d), pause(d), unknown(d)]
    specs.append(spec(d, "three taps · about ten seconds", ph, CAPS[d], full=True))

page = (head("Check-in — three directions") + nav("02-checkin.html")
 + hero("Screen 02 · the moat feature", "Check-in",
        "Three taps, about ten seconds, one-handed. It is the only input the nudge engine needs, and the only feature no competitor has. It is also the feature most easily ruined by a single word of copy.",
        ["Daily · adaptive to nursing status","Answer targets 58pt","Persists after every step"])
 + callout("The sentence that constrains this screen",
   "KellyMom — the resource this audience already reads — states that the feel of the breast, the baby’s behaviour and the amount pumped are <em>not</em> valid ways to know whether supply is sufficient. So this screen can ask all three questions and report the pattern back, but it can never state a verdict. Everything here is phrased as her own report against her own baseline. The one thing it must never say is “your supply is fine.” <span class='cite'>§1.1 · §3.1</span>")
 + block("flow","The flow",
   "Three questions, a done state, the pause picker, and the state that says the app does not know yet. Question two hides itself for mothers who don’t pump.", specs)
 + callout("Why the pump question survives at all",
   "The doctrine that pump output means nothing is well known in this community and actively evangelised — and women report their supply in ounces pumped anyway. That is a behaviour gap, not an education gap, and telling her again will not close it. So the question accepts the number she already thinks in, then reframes it against her own last seven days instead of refusing it. <span class='cite'>§0A.7</span>", "ok")
 + foot(("01-home.html","Home"),("03-nudges.html","Nudges")))
open(f"{OUT}/02-checkin.html","w").write(page)
print("02-checkin.html", len(page), "bytes")
