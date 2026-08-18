import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from sitegen import *
OUT="site"

# ============================ 04 ONBOARDING ============================
def ob(d, i, top, bot=None, t="10:05"):
    hdr = f'<div class="row between">{dots(8,i)}<span class="lbl">{i+1} of 8</span></div>'
    return phone(d, hdr+top, bot if bot is not None else '<button class="btn'+(' primary' if d=="a" else '')+'" style="width:100%">Continue</button>',
                 t=t, sm=True, screen="t-day" if d=="c" else "")

def opts(d, items, sel=0, big=False):
    out=[]
    for j,x in enumerate(items):
        if d=="c":
            out.append(f'<button class="{"on" if j==sel else ""}"><span class="mk"></span>{x}</button>')
        else:
            k = ("primary" if d=="a" else "") if j==sel else "quiet"
            out.append(f'<button class="btn {k} mt8" style="width:100%;min-height:{58 if big else 52}px;justify-content:flex-start;padding-left:18px">{x}</button>')
    return (f'<div class="coarse mt16">{"".join(out)}</div>' if d=="c" else f'<div class="mt10">{"".join(out)}</div>')

def H(d, txt, sz=24): return f'<div class="greet mt20" style="font-size:{sz}px">{txt}</div>'
def P(d, txt): return f'<div class="p mt8" style="font-size:14px">{txt}</div>'

def onboarding_steps(d):
    s=[]
    s.append(ob(d,0, H(d,"When was the baby born?")+P(d,"This sets everything else, so it’s the one thing I need first.")
        +f'<div class="card{" flat" if d=="a" else ""} mt18" style="text-align:center;padding:22px"><div class="lbl">Date of birth</div>'
        f'<div class="mt8" style="font-size:26px;font-weight:600">30 May 2026</div>'
        f'<div class="p mt6" style="font-size:13px">Eleven weeks ago</div></div>'))
    s.append(ob(d,1, H(d,"How are you feeding right now?")+P(d,"You can change this whenever it changes.")
        +opts(d,["Breastfeeding only","A mix of breast and formula","Pumping only","Weaning"],1)))
    s.append(ob(d,2, H(d,"A few numbers")+P(d,"Only used to work out your floor. Nothing here is shown to anyone.")
        +f'<div class="mt16">'
        +''.join(f'<div class="listrow"><div class="grow"><div class="nm">{k}</div></div><div class="{"val" if d!="c" else "nm"}">{v}</div></div>'
                 for k,v in [("Height","5 ft 6 in"),("Weight now","172 lb"),("Before pregnancy","148 lb")])
        +'</div>'+P(d,"Rough is fine. You can correct it later.")))
    s.append(ob(d,3, H(d,"How much are you moving?")+P(d,"Carrying a baby around all day counts.")
        +opts(d,["Mostly sitting or lying down","On my feet a fair bit","Walking most days","Back to proper exercise"],1)))
    s.append(ob(d,4, H(d,"What matters most right now?")+P(d,"This changes what the app puts first. Any of these is a real answer.")
        +opts(d,["Having more energy","Feeling stronger","Losing some weight","All of it, honestly"],0)))
    s.append(ob(d,5, H(d,"One more thing")+P(d,"Has counting food ever been hard on you — now or before you were pregnant?")
        +opts(d,["No","Sometimes","Yes"],0)
        +P(d,"There’s no score here and nothing to submit. If it’s a yes, I’ll drop the calorie counting and the streaks.")))
    s.append(target_preview(d, sm=True))
    s.append(ob(d,7, H(d,"That’s your plan")+P(d,"Make an account to keep it. Your plan is already worked out either way.")
        +f'<div class="mt16">'
        +''.join(f'<button class="btn quiet mt8" style="width:100%">{x}</button>' for x in ["Continue with Apple","Continue with email"])
        +'</div>'+P(d,"Basic logging, the daily check-in and floor warnings are free forever."),
        bot='<button class="btn ghost" style="width:100%">Look around first</button>'))
    return s

MATH = [("Your body at rest","1,415"),("Moving around","+310"),("Making milk","+400"),
        ("A gentle deficit","−125")]
def target_preview(d, sm=False):
    rows = "".join(f'<div class="listrow"><div class="grow"><div class="nm">{k}</div></div>'
                   f'<div class="{"val" if d!="c" else "nm"} tabnum">{v}</div></div>' for k,v in MATH)
    top = (f'{dots(8,6) if sm else ""}'
        f'<div class="greet {"mt16" if sm else "mt8"}" style="font-size:{23 if sm else 26}px">Where your numbers come from</div>'
        f'<div class="p mt8" style="font-size:13.5px">You’ve probably read 1,500 somewhere, or 1,800. Here’s why yours is what it is.</div>'
        f'<div class="mt12">{rows}</div>'
        f'<div class="{"card flat" if d=="a" else "card"} mt14" style="{"" if d!="c" else ""}">'
        f'<div class="row between"><span class="sec">Eat about</span><span style="font-size:23px;font-weight:{600 if d!="c" else 500}" class="tabnum">2,000</span></div>'
        f'<div class="row between mt8"><span class="sec">Never below</span><span style="font-size:23px;font-weight:{600 if d!="c" else 500}" class="tabnum">1,800</span></div></div>'
        f'<div class="p mt12" style="font-size:13px">That deficit is small on purpose. Cutting harder is what tends to '
        f'cost people their supply — though plenty of women cut more and are fine, and there’s no way to know '
        f'in advance which one you are.</div>'
        f'<div class="{"card flat" if d=="a" else "card"} mt12" style="padding:12px 14px">'
        f'<div class="lbl">Reviewed by</div>'
        f'<div class="p mt6" style="font-size:13px">Dana Reyes, RD · Marta Okonjo, IBCLC</div></div>')
    bot = ('<button class="btn'+(' primary' if d=="a" else '')+'" style="width:100%">This looks right</button>'
           '<button class="btn ghost mt4" style="width:100%">Change something</button>')
    return phone(d, top, bot, t="10:05", sm=sm, screen="t-day" if d=="c" else "")

def sixweek(d):
    top = (f'<div class="greet mt10" style="font-size:26px">Your baby is three weeks old</div>'
        f'<div class="p mt10" style="font-size:15px">So I’m not going to give you a deficit yet. Until you’ve had your '
        f'six-week check, this runs in maintenance only.</div>'
        f'<div class="{"card flat" if d=="a" else "card"} mt18">'
        f'<div class="row between"><span class="sec">Eat about</span><span style="font-size:23px;font-weight:600" class="tabnum">2,400</span></div>'
        f'<div class="row between mt10"><span class="sec">Never below</span><span style="font-size:23px;font-weight:600" class="tabnum">1,800</span></div>'
        f'<div class="p mt10" style="font-size:13px">Enough to heal on and keep your supply up.</div></div>'
        f'<div class="p mt14" style="font-size:14px">Everything else works now — logging, the daily check-in, '
        f'floor warnings. Weight targets switch on once you tell me you’ve been checked over.</div>')
    bot = ('<button class="btn'+(' primary' if d=="a" else '')+'" style="width:100%">Start in maintenance</button>'
           '<button class="btn ghost mt4" style="width:100%">I’ve had my six-week check</button>')
    return phone(d, top, bot, t="10:05", screen="t-day" if d=="c" else "")

OB_C = {"a":["<b>The math is a list, not a paragraph.</b> Four rows and a total is something she can check against what she read on Reddit — which is the actual job of this screen. <span class='cite'>§0A.1</span>",
             "<b>The credential sits above the account wall.</b> Credentialing, not features, is what decides whether this audience pays for nutrition advice, and they have been burned by people selling 1,300-calorie plans. <span class='cite'>§0A.4</span>"],
        "b":["<b>Energy and strength come before weight.</b> The body-neutral path is first in the list, not a toggle underneath it — the highest-voted motivation in the research is being able to pick the baby up a hundred times a day.",
             "<b>The gentle question has no score and no submit.</b> It never says screening, and it is the one question she has no reason to lie about. <span class='cite'>§7</span>"],
        "c":["<b>It admits what nobody knows.</b> Roughly a quarter of women cut 250–500 calories with no supply effect and nobody can predict who. Saying so is more credible than a confident promise. <span class='cite'>§0A.5</span>",
             "<b>Eight screens, no progress theatre.</b> Every extra screen bleeds users, and the plan is fully visible before the account wall — the preview is the conversion moment. <span class='cite'>§brief 6</span>"]}
GATE_C = {"a":["<b>It reads as a decision, not an error.</b> No lock icon, no greyed-out UI, no “upgrade to unlock”. The app is choosing this. <span class='cite'>§brief 6</span>"],
          "b":["<b>Everything still works.</b> Only the deficit is withheld — logging, check-in and floor warnings all run, so the gate costs her nothing she needs."],
          "c":["<b>The loudest not-a-diet-app signal available.</b> No override, no “I understand the risks” escape hatch. It costs a few impatient users and buys the IBCLC relationship that is the actual distribution channel."]}

page04 = (head("Onboarding — three directions",
  "\n<style>.dir-b .listrow{padding:8px 0}.dir-b .greet{line-height:1.14}.dir-b .card{padding:13px}.dir-c .listrow{padding:10px 0}</style>") + nav("04-onboarding.html")
 + hero("Screen 04 · under ninety seconds", "Onboarding",
        "Eight screens, and the seventh is the one that matters. She sees her whole plan — targets, floor, and the arithmetic behind both — before she is asked for an account.",
        ["8 screens · ≤ 90 seconds","Value before the account wall","Six-week gate, no override"])
 + callout("What the target-preview screen is actually for",
   "Not teaching her what a calorie floor is. That idea is already installed — women quote 1,500, 1,800 and 2,000 to each other unprompted, and even the most restriction-tolerant corners of the internet carve out an exception for nursing. Her question is narrower and more urgent: <b>why is your number different from the one I read?</b> So the screen shows the arithmetic and lets her audit it. <span class='cite'>§0A.1 · §2.3</span>")
 + block("flow","The eight screens","Birth date first, because it gates everything. The gentle question about food sits at six, after she has already seen that this app asks about energy before it asks about weight.",
   [spec(d,"eight steps",onboarding_steps(d),OB_C[d],full=True) for d in "abc"])
 + block("preview","The target preview","The conversion moment, at full size. This is where an editorial serif earns its keep and where the reviewing clinicians are named.",
   [spec("a","the math, itemised",[target_preview("a")],
     ["<b>Shown before signup, deliberately.</b> Walling this screen would kill the trust it exists to build. <span class='cite'>§brief 6</span>"]),
    spec("b","the math, itemised",[target_preview("b")],
     ["<b>Two numbers, clearly different jobs.</b> “Eat about” is a target she can miss; “never below” is a floor she shouldn’t. Same card, different weight."]),
    spec("c","the math, itemised",[target_preview("c")],
     ["<b>Names are placeholders.</b> Recruiting a real RD and IBCLC is a launch prerequisite — this screen is the reason it matters commercially, not just clinically."])])
 + block("gate","The six-week gate","Baby under six weeks. Maintenance only, no override, until she confirms she has had her postpartum check.",
   [spec(d,"maintenance only",[sixweek(d)],GATE_C[d]) for d in "abc"])
 + foot(("03-nudges.html","Nudges"),("05-log.html","Log")))
open(f"{OUT}/04-onboarding.html","w").write(page04); print("04", len(page04))

# ============================ 05 LOG ============================
RECENTS = [("Oatmeal, banana, peanut butter","Logged 41 times","420"),
           ("Greek yoghurt, 170g","Yesterday","120"),
           ("Chicken burrito bowl","Tuesday","640"),
           ("Whole milk, large glass","Yesterday","150")]
def star(on): return f'<span style="color:{"var(--accent)" if on else "var(--ink-faint)"};font-size:15px">{"★" if on else "☆"}</span>'

def log_search(d):
    rows = "".join(f'<div class="listrow"><div class="grow"><div class="nm">{n}</div><div class="mt">{m}</div></div>'
                   f'<div class="row gap10">{star(i<2)}<div class="{"val" if d!="c" else "nm"} tabnum">{c}</div></div></div>'
                   for i,(n,m,c) in enumerate(RECENTS))
    top = (f'<div class="row between"><div class="greet" style="font-size:22px">Log food</div>'
           f'<button class="chip">Scan</button></div>'
           f'<div class="{"card flat" if d=="a" else "card"} mt14" style="padding:14px 15px">'
           f'<span class="p" style="font-size:15px">Search foods</span></div>'
           f'<div class="row between mt18"><span class="sec">Recent</span><span class="lbl">newest first</span></div>'
           f'<div class="mt4">{rows}</div>')
    bot = ('<button class="btn quiet" style="width:100%">Log this week’s weight</button>')
    return phone(d, top, bot, t="12:40", sm=True, screen="t-day" if d=="c" else "")

def log_portion(d):
    top = (f'<div class="greet mt6" style="font-size:22px">Oatmeal, banana, peanut butter</div>'
           f'<div class="p mt6" style="font-size:13px">Saved meal · you’ve logged this 41 times</div>'
           f'<div class="{"card flat" if d=="a" else "card"} mt16" style="text-align:center;padding:20px">'
           f'<div class="lbl">How much?</div>'
           f'<div class="mt8" style="font-size:27px;font-weight:600">1 bowl</div>'
           f'<div class="p mt6" style="font-size:13px">Type it how you say it — “1 cup”, “180 g”, “2 eggs”.</div></div>'
           f'<div class="row gap8 mt12" style="flex-wrap:wrap"><button class="chip on">1 bowl</button>'
           f'<button class="chip">½ bowl</button><button class="chip">1½ bowls</button></div>'
           f'<div class="mt16">'
           + "".join(f'<div class="listrow"><div class="grow"><div class="nm">{k}</div></div>'
                     f'<div class="{"val" if d!="c" else "nm"} tabnum">{v}</div></div>'
                     for k,v in [("Calories","420"),("Protein","14 g")]) + '</div>')
    bot = '<button class="btn'+(' primary' if d=="a" else '')+'" style="width:100%">Add to today</button>'
    return phone(d, top, bot, t="12:40", sm=True, screen="t-day" if d=="c" else "")

def log_confirm(d):
    top = (f'<div class="greet mt10" style="font-size:24px">Added.</div>'
           f'<div class="greet-sub">Breakfast · 420 calories</div>'
           f'<div class="{"card flat" if d=="a" else "card"} mt18">'
           f'<div class="row between"><span class="sec">Today</span><span class="{"val" if d!="c" else "nm"} tabnum">540</span></div>'
           f'<div class="mt10" style="position:relative;height:10px;border-radius:6px;background:var(--surface-2);overflow:hidden">'
           f'<div style="position:absolute;inset:0 auto 0 0;width:23.5%;background:var(--{"accent" if d=="a" else "sage" if d=="b" else "held"});border-radius:6px"></div>'
           f'<div style="position:absolute;top:0;bottom:0;left:78.26%;width:2px;background:var(--ink)"></div></div>'
           f'<div class="p mt8" style="font-size:13px">1,260 to go before you’re above your floor.</div></div>'
           f'<div class="p mt14" style="font-size:13.5px">Saved to your phone straight away — you don’t need signal for this.</div>')
    bot = ('<button class="btn quiet" style="width:100%">Log something else</button>'
           '<button class="btn ghost mt4" style="width:100%">Done</button>')
    return phone(d, top, bot, t="12:41", sm=True, screen="t-day" if d=="c" else "")

def log_barcode(d):
    top = (f'<div class="greet mt6" style="font-size:22px">Scan a barcode</div>'
           f'<div class="mt14" style="border-radius:{"9px" if d=="a" else "16px"};border:1.5px dashed var(--hairline-2);'
           f'height:190px;display:flex;align-items:center;justify-content:center;background:var(--surface-2)">'
           f'<div style="width:120px;height:64px;display:flex;gap:3px;align-items:stretch">'
           + "".join(f'<div style="flex:{w};background:var(--ink);opacity:.75"></div>' if i%2==0 else f'<div style="flex:{w}"></div>'
                     for i,w in enumerate([2,1,3,1,1,2,4,1,2,1,3,1,1,2]))
           + '</div></div>'
           f'<div class="p mt14" style="font-size:14px">Free, and always in this same spot — bottom right of every screen in the app.</div>')
    bot = '<button class="btn quiet" style="width:100%">Enter it by hand instead</button>'
    return phone(d, top, bot, t="12:42", sm=True, screen="t-day" if d=="c" else "")

def coarse_log(d):
    if d=="c":
        body = ('<div class="coarse mt18">'
                '<button class="on"><span class="mk"></span>Roughly enough</button>'
                '<button><span class="mk"></span>Not sure</button>'
                '<button><span class="mk"></span>Definitely not enough</button></div>')
    else:
        body = ('<div class="mt14">' + "".join(
            f'<button class="btn {("primary" if d=="a" else "") if i==0 else "quiet"} mt8" style="width:100%;min-height:58px;justify-content:flex-start;padding-left:18px">{x}</button>'
            for i,x in enumerate(["Roughly enough","Not sure","Definitely not enough"])) + '</div>')
    top = (f'<div class="greet mt10" style="font-size:24px">How was today?</div>'
           f'<div class="p mt8" style="font-size:14px">No weighing, no counting. Just how it felt.</div>{body}'
           f'<div class="p mt16" style="font-size:13px">I’ll still warn you if a few of these in a row look like you’re running short.</div>')
    bot = ('<button class="btn ghost" style="width:100%">Count it properly instead</button>')
    return phone(d, top, bot, t="9:20", screen="t-day" if d=="c" else "")

LOG_C = {"a":["<b>Free-text portions.</b> She types “1 bowl” or “180 g” and the app parses it, rather than making her hunt a dropdown for a unit she wouldn’t have chosen. <span class='cite'>§6.2</span>",
              "<b>Favourites are per item, not per meal.</b> A named, repeated complaint about the incumbent — and a saved meal whose quantity can change without becoming two saved meals."],
         "b":["<b>Weight logging lives here, not in a separate tab.</b> The single loudest structural complaint in four years of reviews is that logging food and logging a weight are on different pages. <span class='cite'>§6.2</span>",
              "<b>No top-right plus.</b> It is the wrong affordance for a one-handed user and it is the control that keeps breaking in the incumbent’s release notes."],
         "c":["<b>Barcode scanning is free and always in the same place.</b> Paywalling the scanner is the single biggest driver of churn in this category; moving it around is the second. <span class='cite'>§6.2</span>",
              "<b>Saves land immediately and say so.</b> A silent save failure in a supply-tracking app is credibility poison — it is what sank the one direct competitor’s ratings. <span class='cite'>§6.3</span>"]}

page05 = (head("Log — three directions") + nav("05-log.html")
 + hero("Screen 05 · under ten seconds", "Logging",
        "Search, portion, confirm. The benchmark is re-logging a food she eats every week in under ten seconds, one-handed, while holding a baby.",
        ["USDA search · barcode · recents","Free-text portions","Weight entry on the same surface"])
 + callout("Every item on this screen is a competitor’s one-star review",
   "Free-text portions. Per-item favourites. Recents in a predictable order. An editable quantity on a saved meal. No “have you already eaten this?” confirmation. A barcode scanner that is free and always in the same place. None of it is clever — it is all just the list of things the incumbent gets wrong, written down and fixed. <span class='cite'>§6.2</span>")
 + block("flow","Search → portion → confirm → scan","One row per direction. The fourth screen is the barcode entry, which lives in the same position on every screen in the app.",
   [spec(d,"four steps",[log_search(d),log_portion(d),log_confirm(d),log_barcode(d)],LOG_C[d],full=True) for d in "abc"])
 + block("coarse","Logging without numbers",
   "Three answers instead of grams. This is not a lite mode — a precise floor measured against precisely-logged intake is the exact pattern women in this audience describe as harmful, and many of them falsify logs to escape it.",
   [spec("a","available as a mode",[coarse_log("a")],
     ["<b>Offered, not hidden.</b> In A and B this is a mode she can switch to at any time; in C it is simply how logging works. <span class='cite'>§0A.2</span>"]),
    spec("b","available as a mode",[coarse_log("b")],
     ["<b>The floor still works.</b> Coarse answers still feed the nudge engine — “definitely not enough” three days running is a stronger signal than a fabricated number."]),
    spec("c","the default",[coarse_log("c")],
     ["<b>The exit ramp from tracking.</b> The competitor here is quitting entirely, usually between weeks two and eight. An app that asks for less as she stabilises is the only version she keeps. <span class='cite'>§0A.2 · §8.2-J</span>"])])
 + foot(("04-onboarding.html","Onboarding"),("06-trends.html","Trends")))
open(f"{OUT}/05-log.html","w").write(page05); print("05", len(page05))
