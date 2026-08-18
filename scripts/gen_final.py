import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from sitegen import *
OUT="site"

# ---------- chart helpers ----------
W,H0 = 320,140
LOSS = [176.0,175.4,176.2,175.1,175.6,174.8,175.2,174.6,174.9,174.1,174.6,173.8,174.2,173.6,
        173.9,173.2,173.6,172.9,173.4,172.7,173.1,172.5,172.9,172.4,172.8,172.2,172.6,172.4]
FLAT = [172.2,172.9,172.1,172.8,172.4,173.1,172.5,173.0,172.6,173.2,172.7,173.3,172.8,173.1,
        172.9,173.4,173.0,173.5,173.1,173.6,173.2,173.5,173.3,173.7,173.2,173.6,173.4,173.5]
def smooth(v,k=7):
    out=[]
    for i in range(len(v)):
        w=v[max(0,i-k+1):i+1]; out.append(sum(w)/len(w))
    return out
def X(i,n=28): return 12+i*((W-24)/(n-1))
def Y(w,lo=171.5,hi=176.8): return 14+(hi-w)/(hi-lo)*(H0-34)

def chart_a(vals):
    tr=smooth(vals)
    conn="".join(f'<line x1="{X(i):.1f}" y1="{Y(v):.1f}" x2="{X(i):.1f}" y2="{Y(tr[i]):.1f}" stroke="var(--ink-faint)" stroke-width="1" stroke-opacity=".5"/>' for i,v in enumerate(vals))
    dia="".join(f'<rect x="{X(i)-2.6:.1f}" y="{Y(v)-2.6:.1f}" width="5.2" height="5.2" transform="rotate(45 {X(i):.1f} {Y(v):.1f})" fill="var(--{"steady" if v<tr[i] else "accent"})" fill-opacity=".85"/>' for i,v in enumerate(vals))
    line="M"+" L".join(f"{X(i):.1f} {Y(v):.1f}" for i,v in enumerate(tr))
    return (f'<svg viewBox="0 0 {W} {H0}" style="width:100%;height:auto;display:block">{conn}'
            f'<path d="{line}" fill="none" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>{dia}</svg>')

def chart_b(vals):
    tr=smooth(vals)
    top="M"+" L".join(f"{X(i):.1f} {Y(v+0.7):.1f}" for i,v in enumerate(tr))
    bot=" L".join(f"{X(i):.1f} {Y(v-0.7):.1f}" for i,v in reversed(list(enumerate(tr))))
    line="M"+" L".join(f"{X(i):.1f} {Y(v):.1f}" for i,v in enumerate(tr))
    dots="".join(f'<circle cx="{X(i):.1f}" cy="{Y(tr[i]):.1f}" r="3.4" fill="var(--surface)" stroke="var(--sage)" stroke-width="2.2"/>' for i in range(0,28,7))
    return (f'<svg viewBox="0 0 {W} {H0}" style="width:100%;height:auto;display:block">'
            f'<path d="{top} L{bot} Z" fill="var(--sage)" fill-opacity=".16"/>'
            f'<path d="{line}" fill="none" stroke="var(--sage)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>{dots}</svg>')

def chart_c(vals):
    tr=smooth(vals)
    def band(sp,op):
        t="M"+" L".join(f"{X(i):.1f} {Y(v+sp):.1f}" for i,v in enumerate(tr))
        b=" L".join(f"{X(i):.1f} {Y(v-sp):.1f}" for i,v in reversed(list(enumerate(tr))))
        return f'<path d="{t} L{b} Z" fill="var(--held)" fill-opacity="{op}"/>'
    # ribbon narrows over time
    t2="M"+" L".join(f"{X(i):.1f} {Y(v+(1.5-i*0.035)):.1f}" for i,v in enumerate(tr))
    b2=" L".join(f"{X(i):.1f} {Y(v-(1.5-i*0.035)):.1f}" for i,v in reversed(list(enumerate(tr))))
    t1="M"+" L".join(f"{X(i):.1f} {Y(v+(0.7-i*0.016)):.1f}" for i,v in enumerate(tr))
    b1=" L".join(f"{X(i):.1f} {Y(v-(0.7-i*0.016)):.1f}" for i,v in reversed(list(enumerate(tr))))
    line="M"+" L".join(f"{X(i):.1f} {Y(v):.1f}" for i,v in enumerate(tr))
    return (f'<svg viewBox="0 0 {W} {H0}" style="width:100%;height:auto;display:block">'
            f'<path d="{t2} L{b2} Z" fill="var(--held)" fill-opacity=".14"/>'
            f'<path d="{t1} L{b1} Z" fill="var(--held)" fill-opacity=".28"/>'
            f'<path d="{line}" fill="none" stroke="var(--held)" stroke-width="2.6" stroke-linecap="round"/></svg>')

CHART={"a":chart_a,"b":chart_b,"c":chart_c}

def field30(miss=(7,), thin=(2,21), pause=(14,15)):
    cells=[]
    for i in range(30):
        c = "miss" if i in miss else "thin" if i in thin else "pause" if i in pause else ""
        if i==29: c=(c+" today").strip()
        cells.append(f'<i class="{c}"></i>' if c else '<i></i>')
    return '<div class="field">'+"".join(cells)+'</div>'

def protected_bar(d, above=26, slight=2, well=2):
    return (f'<div style="display:flex;height:16px;border-radius:{"3px" if d=="a" else "9px"};overflow:hidden;gap:2px">'
            f'<div style="flex:{above};background:var(--{"steady" if d=="a" else "sage" if d=="b" else "held"})"></div>'
            f'<div style="flex:{slight};background:var(--hairline-2)"></div>'
            f'<div style="flex:{well};background:var(--{"caution" if d=="a" else "amber" if d=="b" else "miss"});opacity:.7"></div></div>')

# ============================ 06 TRENDS ============================
def trends(d, flat=False):
    vals = FLAT if flat else LOSS
    hd = "Weight" 
    verdict = "Flat for three weeks" if flat else "Down 0.6 lb a week"
    sub = ("Your weight hasn’t moved much. That happens to a lot of people while nursing, "
           "and it isn’t a sign you’re doing this wrong.") if flat else "Steady, and about as fast as is sensible while nursing."
    top = (f'<div class="greet" style="font-size:23px">Trends</div>'
           f'<div class="greet-sub">Last four weeks</div>'
           f'<div class="{"card flat" if d=="a" else "card"} mt16">'
           f'<div class="row between"><span class="sec">{hd}</span>'
           f'<span class="{"val" if d!="c" else "nm"} tabnum">172.4 lb</span></div>'
           f'<div class="mt10">{CHART[d](vals)}</div>'
           f'<div class="row between mt6"><span class="lbl">4 wks ago</span><span class="lbl">today</span></div>'
           f'<div class="p mt10" style="font-size:13.5px"><strong>{verdict}.</strong> {sub}</div></div>'
           f'<div class="{"card flat" if d=="a" else "card"} mt12">'
           f'<div class="row between"><span class="sec">Days above your floor</span>'
           f'<span class="{"val" if d!="c" else "nm"} tabnum">26 of 30</span></div>'
           f'<div class="mt10">{protected_bar(d)}</div>'
           f'<div class="p mt8" style="font-size:12.5px">Two days a bit under, two well under, two paused.</div></div>')
    bot = ('<button class="btn quiet" style="width:100%">Log this week’s weight</button>' if not flat else
           '<button class="btn'+(' primary' if d=="a" else '')+'" style="width:100%">See what else changed</button>'
           '<button class="btn ghost mt4" style="width:100%">Log this week’s weight</button>')
    return phone(d, top, bot, t="8:30", screen="t-day" if d=="c" else "")

def protected_hero(d):
    top = (f'<div class="greet" style="font-size:23px">Last 30 days</div>'
           f'<div class="greet-sub">The number that isn’t your weight.</div>'
           + (f'<div class="hero-n mt18">26<u>days protected</u></div>{field30()}'
              f'<div class="fieldkey"><span class="cellkey"><b style="background:var(--held)"></b>Above floor</span>'
              f'<span class="cellkey"><b style="border:1.5px solid var(--thin)"></b>A bit under</span>'
              f'<span class="cellkey"><b style="border:1.5px solid var(--miss)"></b>Well under</span>'
              f'<span class="cellkey"><b style="border:1.5px dashed var(--hairline-2);background:var(--surface-2)"></b>Paused</span></div>'
              if d=="c" else
              f'<div class="{"ledger" if d=="a" else ""} mt18">'
              f'<div class="{"k" if d=="a" else "sec"}">Days above your floor</div>'
              f'<div class="{"n" if d=="a" else "ring-n"} tabnum" style="{"font-size:64px" if d=="a" else "font-size:44px;margin-top:8px"}">26<u style="{"" if d=="a" else "display:none"}">of 30</u></div>'
              f'{"" if d=="a" else "<div class=ring-u style=text-align:left>of the last 30</div>"}</div>'
              f'<div class="mt16">{protected_bar(d)}</div>'
              f'<div class="row between mt8"><span class="lbl">26 above</span><span class="lbl">2 a bit under</span><span class="lbl">2 well under</span></div>')
           + f'<div class="p mt16" style="font-size:14px">Supply responds to what you do over a week, not to any single day. '
             f'One short day doesn’t undo the other twenty-nine.</div>')
    bot = '<button class="btn quiet" style="width:100%">What counts as protected?</button>'
    return phone(d, top, bot, t="8:31", screen="t-day" if d=="c" else "")

T1={"a":["<b>Floats and sinkers.</b> Each day is a diamond tethered to the trend line — days below pull it down, days above pull it up. A bad day stops being evidence of failure and becomes one force among twenty-eight. <span class='cite'>§8.2-B</span>",
         "<b>The connectors do the explaining.</b> No copy needed to say the raw number is noise; the drawing says it."],
     "b":["<b>The trend inside a corridor.</b> Same band grammar as the ring, so the whole product reads as one system rather than a set of screens.",
          "<b>Weekly dots, not daily.</b> Weighing daily is psychologically rough on this audience; the prompt is weekly and the display smooths seven days. <span class='cite'>§brief 4</span>"],
     "c":["<b>A percentile ribbon.</b> The band narrows as she becomes more consistent and fattens when she is erratic — progress that does not require the number to move. Borrowed from Dexcom’s AGP. <span class='cite'>§8.2-F</span>",
          "<b>Honest caveat: this needs data.</b> It cannot be the day-one screen. It is a 30-day view or a later unlock."]}
T2={"a":["<b>The state the brief doesn’t have.</b> A large, vocal group gains while nursing — the top comment in the relevant thread is “some of us lucky ones gain weight”, at 161 upvotes. A product whose loop is “stay above the floor and it comes off” fails them by design. <span class='cite'>§0A.5</span>"],
    "b":["<b>It does not propose a bigger deficit.</b> That is the reflex every other app has, and here it is the one response that would be actively harmful."],
    "c":["<b>It redirects to a win that exists.</b> Days protected, energy, protein — all true, all unrelated to the scale. No apology, no “don’t worry”, no reframing her result as a secret success."]}
T3={"a":["<b>Time in Range, ported.</b> Clinicians already read this shape, which matters when the growth channel is IBCLC referral. <span class='cite'>§8.2-D · §2.7</span>"],
    "b":["<b>Robust to one bad day.</b> A metric that a single hard Tuesday can destroy is a metric that teaches her to avoid the app on hard Tuesdays."],
    "c":["<b>Paused days are visible and neutral.</b> They are neither wins nor misses — drawn dashed, counted separately, and never silently folded into a failure. <span class='cite'>§6.4</span>"]}

page06 = (head("Trends — three directions") + nav("06-trends.html")
 + hero("Screen 06 · the honest one", "Trends",
        "A weekly weigh-in, a seven-day smoothed line, and a second metric that isn’t a weight at all — because for a meaningful share of this audience the weight will not move, and the product still has to work for them.",
        ["Weekly prompt · 7-day smoothing","Days protected as a second hero","A designed flat-or-rising state"])
 + callout("Why the smoothing is a feature, not a compromise",
   "Postpartum scale noise is worse than the general case — lochia, resolving oedema, engorgement, hydration swings, and a real difference before and after a feed. A raw daily number is mostly artefact. Saying that plainly, and widening the smoothing accordingly, turns the most demoralising number in the product into the one that finally makes sense.")
 + block("good","Losing steadily","Four weeks in, down about 0.6 lb a week. Three different chart devices, not three skins of one chart.",
   [spec(d,"7-day smoothed",[trends(d)],T1[d]) for d in "abc"])
 + block("flat","Flat, or rising",
   "Three weeks with no movement. This state has to exist, be designed, and not read as failure — and it must not respond by proposing a bigger deficit.",
   [spec(d,"non-apologetic",[trends(d,flat=True)],T2[d]) for d in "abc"])
 + block("protected","Days protected",
   "The retrospective that survives a bad week. Robust to one hard day, matched to how supply actually responds, and recognisable to a clinician.",
   [spec(d,"time in range",[protected_hero(d)],T3[d]) for d in "abc"])
 + callout("Should she log a weight when she’s bloated?",
   "Yes — and the answer belongs in the product, not in a support article. One heavy reading moves a seven-day trend by a fraction of what it moves the raw number, which is exactly the point of drawing the trend at all. The apps that skip this question are the ones whose users quietly stop weighing.", "ok")
 + foot(("05-log.html","Log"),("07-paywall.html","Paywall")))
open(f"{OUT}/06-trends.html","w").write(page06); print("06", len(page06))
