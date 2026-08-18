"""Shared page scaffolding for the design-review site."""

NAVITEMS = [("index.html","Overview"),("01-home.html","Home"),("02-checkin.html","Check-in"),
            ("03-nudges.html","Nudges"),("04-onboarding.html","Onboarding"),("05-log.html","Log"),
            ("06-trends.html","Trends"),("07-paywall.html","Paywall"),("08-adapted.html","Adapted mode"),
            ("docs/index.html","Context")]

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700"
         "&family=Be+Vietnam+Pro:wght@300;400;500;600&family=Fraunces:opsz,wght@9..144,400..700"
         "&family=Hanken+Grotesk:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500"
         "&family=Instrument+Serif&family=Newsreader:opsz,wght@6..72,300..600"
         "&family=Nunito:wght@400;600;700;800&family=Petrona:wght@300;400;500;600&display=swap")

def head(title, extra_css=""):
    return f'''<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="css/site.css"><link rel="stylesheet" href="css/device.css">
<link rel="stylesheet" href="css/dir-a.css"><link rel="stylesheet" href="css/dir-b.css">
<link rel="stylesheet" href="css/dir-c.css">{extra_css}
</head><body>'''

def nav(current):
    links = "".join(f'    <a href="{h}"{" aria-current=\"page\"" if h==current else ""}>{t}</a>\n'
                    for h,t in NAVITEMS)
    return f'''<nav class="nav"><div class="nav-in">
  <a class="nav-mark" href="index.html">
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M2 13a8 8 0 0 1 16 0" stroke="#C98A5B" stroke-width="1.6" stroke-linecap="round"/><path d="M2 16.5h16" stroke="#F0EBE1" stroke-width="1.6" stroke-linecap="round"/></svg>
    <b>Design review</b></a>
  <div class="nav-links">
{links}  </div>
</div></nav>'''

def foot(prev=None, nxt=None):
    p = f'<a href="{prev[0]}">← {prev[1]}</a>' if prev else '<span></span>'
    n = f'<a href="{nxt[0]}">{nxt[1]} →</a>' if nxt else '<span></span>'
    return f'''<div class="wrap"><div class="pager">{p}{n}</div></div>
<footer><div class="wrap f-in">
  <span>Design exploration · the app is unnamed; wordmarks are placeholders</span>
  <span>§ references point to the design research document</span>
</div></footer>
<script src="js/shot.js"></script>
</body></html>'''

_G = ('<svg width="18" height="11" viewBox="0 0 18 11" fill="currentColor"><rect x="0" y="7" width="3" height="4" rx="1"/>'
      '<rect x="5" y="5" width="3" height="6" rx="1"/><rect x="10" y="2.5" width="3" height="8.5" rx="1"/>'
      '<rect x="15" y="0" width="3" height="11" rx="1"/></svg>'
      '<svg width="16" height="11" viewBox="0 0 16 12" fill="currentColor"><path d="M8 10.6 6.2 8.8a2.6 2.6 0 0 1 3.6 0L8 10.6Zm0-4.1c-1.4 0-2.7.5-3.7 1.5L2.9 6.6a7.2 7.2 0 0 1 10.2 0l-1.4 1.4A5.2 5.2 0 0 0 8 6.5Zm0-3.6c-2.3 0-4.5.9-6.2 2.5L.4 4C2.4 2 5.1.9 8 .9s5.6 1.1 7.6 3.1l-1.4 1.4A8.8 8.8 0 0 0 8 2.9Z"/></svg>')

def sb(t="9:41", batt=16):
    return (f'<div class="sb"><span>{t}</span><span class="glyphs">{_G}'
            f'<svg width="25" height="12" viewBox="0 0 25 12" fill="none">'
            f'<rect x=".5" y=".5" width="21" height="11" rx="3.2" stroke="currentColor" stroke-opacity=".38"/>'
            f'<rect x="2" y="2" width="{batt}" height="8" rx="2" fill="currentColor"/>'
            f'<path d="M23 4.2v3.6a2 2 0 0 0 0-3.6Z" fill="currentColor" fill-opacity=".45"/></svg>'
            f'</span></div><div class="notch"></div>')

def phone(d, top, bottom="", t="9:41", batt=16, screen="", frame="", sm=False, label=""):
    """d: 'a'|'b'|'c'. top/bottom are inner HTML. screen: extra .screen classes."""
    bot = f'<div class="pad mtauto" style="padding-bottom:8px">{bottom}</div>' if bottom else ""
    lab = f'<span class="stagelabel">{label}</span>' if label else ""
    return (f'<div class="stage{" sm" if sm else ""}"><div class="phone{" "+frame if frame else ""} dir-{d}">'
            f'<div class="screen{" "+screen if screen else ""}">{sb(t,batt)}'
            f'<div class="body"><div class="pad" style="padding-top:14px">{top}</div>{bot}</div>'
            f'<div class="hb"></div></div></div>{lab}</div>')

DIRNAME = {"a":"A · Ledger","b":"B · The Band","c":"C · Protected"}

def spec(d, sub, phones, captions, full=False):
    caps = "".join(f'<p class="caption">{c}</p>' for c in captions)
    style = ' style="grid-column:1/-1"' if full else ''
    return (f'<div class="spec {d}"{style}><div class="spec-head"><span class="dot"></span>'
            f'<span class="nm">{DIRNAME[d]}</span><span class="sub">{sub}</span></div>'
            f'<div class="stagewrap">{"".join(phones)}</div>{caps}</div>')

def block(anchor, h2, note, specs):
    return (f'<div class="wrap"><section class="screenblock anchor" id="{anchor}">'
            f'<div class="screenhead"><h2>{h2}</h2><p class="note">{note}</p></div>'
            f'<div class="rowgrid">{"".join(specs)}</div></section></div>')

def hero(eyebrow, h1, sub, meta):
    m = "".join(f"<span>{x}</span>" for x in meta)
    return (f'<div class="wrap"><section class="hero" style="padding:64px 0 30px">'
            f'<span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="sub">{sub}</p>'
            f'<div class="metabar">{m}</div></section></div>')

def callout(lab, text, kind=""):
    k = f" {kind}" if kind else ""
    return f'<div class="wrap"><div class="callout{k}"><span class="lab">{lab}</span>{text}</div></div>'

# --- small reusable glyphs -------------------------------------------------
SHIELD = ('<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M10 2.2 3.6 4.6v5c0 4 2.7 7 6.4 8.2 3.7-1.2 6.4-4.2 6.4-8.2v-5L10 2.2Z" fill="currentColor" fill-opacity=".16" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="m7.3 9.9 1.9 1.9 3.6-3.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
SHIELD_DASH = ('<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M10 2.2 3.6 4.6v5c0 4 2.7 7 6.4 8.2 3.7-1.2 6.4-4.2 6.4-8.2v-5L10 2.2Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" stroke-dasharray="2.6 2.2"/><path d="M10 7v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="10" cy="13.6" r="1" fill="currentColor"/></svg>')
SHIELD_DOT = ('<svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M10 2.2 3.6 4.6v5c0 4 2.7 7 6.4 8.2 3.7-1.2 6.4-4.2 6.4-8.2v-5L10 2.2Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round" stroke-dasharray="1 2.4"/><circle cx="10" cy="10.4" r="1.1" fill="currentColor"/></svg>')
CHEV = '<svg width="8" height="13" viewBox="0 0 8 13" fill="none"><path d="m1.5 1.5 5 5-5 5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def dots(n, on):
    return '<div class="dots">' + "".join(f'<i class="{"on" if i==on else ""}"></i>' for i in range(n)) + '</div>'

def banner(d, kind, h, s, chev=False):
    ic = {"steady":SHIELD,"dip":SHIELD_DASH,"unknown":SHIELD_DOT}[kind]
    cls = "" if kind=="steady" else f" {kind}"
    go = f'<span class="go">{CHEV}</span>' if chev else ""
    return (f'<div class="banner{cls}"><span class="ic">{ic}</span>'
            f'<div class="grow"><div class="h">{h}</div><div class="s">{s}</div></div>{go}</div>')
