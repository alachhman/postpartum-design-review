#!/usr/bin/env python3
"""Contract checks across every design page: hex literals, banned lexicon,
clinical-claim slips, and nav consistency."""
import glob, os, re, sys

PAGES = sorted(glob.glob("*.html"))
BANNED = ["bounce back", "get your body back", "burn it off", "earn your food",
          "summer body", "shred", "detox", "cheat day", "cheat meal",
          "before and after", "snap back"]
# wellness-speak this audience demonstrably does not use
SOFT   = ["nourish", "honour your body", "honor your body", "love your body",
          "your journey", "glow up"]
# clinical claims the app cannot substantiate
CLINICAL = [r"your supply is (good|low|fine|normal|healthy)",
            r"supply (is )?(good|low|normal)\b",
            r"above typical", r"below typical", r"compared to typical",
            r"than (most|other) (mothers|women|moms)"]

fails = 0
for p in PAGES:
    s = open(p, encoding="utf-8").read()
    body = s.split("</head>", 1)[-1]
    issues = []

    # hex literals inside phone mocks (the site chrome legitimately uses them)
    for m in re.finditer(r'class="phone[^"]*"', body):
        seg = body[m.start():m.start() + 14000]
        seg = seg.split("</div></div></div>")[0]
        for h in re.findall(r"#[0-9A-Fa-f]{6}\b", seg):
            issues.append(f"hex literal in mock: {h}")

    low = re.sub(r"\s+", " ", body.lower())
    for w in BANNED:
        if w in low: issues.append(f"BANNED lexicon: '{w}'")
    for w in SOFT:
        if w in low: issues.append(f"wellness-speak: '{w}'")
    for rx in CLINICAL:
        m = re.search(rx, low)
        if m: issues.append(f"clinical claim: '{m.group(0)}'")

    if "docs/index.html" not in s:
        issues.append("nav missing Context link")
    if "js/shot.js" not in s:
        issues.append("missing shot.js harness")
    if re.search(r"<h1[^>]*>[^<]*!", body):
        issues.append("exclamation mark in a headline")

    seen, uniq = set(), []
    for i in issues:
        if i not in seen: seen.add(i); uniq.append(i)
    if uniq:
        fails += len(uniq)
        print(f"\n{p}")
        for i in uniq[:12]: print(f"   - {i}")
        if len(uniq) > 12: print(f"   … and {len(uniq)-12} more")
    else:
        print(f"{p:24} clean")

print(f"\n{fails} issue(s) across {len(PAGES)} pages")
sys.exit(0)
