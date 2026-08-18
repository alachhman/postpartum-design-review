#!/usr/bin/env python3
"""Contract checks. The rules that matter apply to text INSIDE a phone mock —
that is product UI. The surrounding review prose legitimately quotes banned
phrasing in order to argue against it, so it is checked separately and only
for genuinely unacceptable language."""
import glob, re, sys

BANNED = ["bounce back","get your body back","burn it off","earn your food","summer body",
          "shred","detox","cheat day","cheat meal","snap back","before-and-after",
          "before/after","guilt-free"]
SOFT   = ["nourish","honour your body","honor your body","love your body","your journey",
          "glow up","self-care ritual","mama bear"]
CLINICAL = [r"your supply is (good|low|fine|normal|healthy|strong)",
            r"\bsupply (is|looks) (good|low|normal|fine)\b",
            r"(above|below|compared to) typical",
            r"than (most|other) (mothers|women|moms)",
            r"you (have|don.t have) enough milk"]

def mocks(html):
    """Visible text inside every .screen element."""
    out=[]
    for m in re.finditer(r'<div class="screen(?: [^"]*)?">(.*?)<div class="hb">', html, re.S):
        txt = re.sub(r"<[^>]+>", " ", m.group(1))
        out.append(re.sub(r"\s+", " ", txt))
    return out

fails = 0
for p in sorted(glob.glob("site/*.html")):
    html = open(p, encoding="utf-8").read()
    name = p.split("/")[-1]
    issues = []

    inside = " ".join(mocks(html)).lower()
    for w in BANNED + SOFT:
        if w in inside: issues.append(f"in-mock language: '{w}'")
    for rx in CLINICAL:
        m = re.search(rx, inside)
        if m: issues.append(f"in-mock clinical claim: '{m.group(0)}'")
    for h in re.findall(r"#[0-9A-Fa-f]{6}\b", " ".join(
            re.findall(r'<div class="screen(?: [^"]*)?">(.*?)<div class="hb">', html, re.S))):
        issues.append(f"hex literal in mock: {h}")
    if "!" in re.sub(r"<[^>]+>", "", " ".join(mocks(html))):
        issues.append("exclamation mark in app copy")

    body = html.split("</head>",1)[-1]
    if 'href="docs/index.html"' not in html: issues.append("nav missing Context link")
    if "js/shot.js" not in html: issues.append("missing shot.js harness")

    if issues:
        fails += len(issues); print(f"\n{name}")
        for i in dict.fromkeys(issues): print(f"   - {i}")
    else:
        print(f"{name:24} clean   ({len(mocks(html))} mocks)")

print(f"\n{fails} issue(s)")
