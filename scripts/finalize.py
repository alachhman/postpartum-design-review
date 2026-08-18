#!/usr/bin/env python3
"""Final pass over every design page: add the Context nav link, drop build
scaffolding, and confirm each page carries the screenshot harness."""
import glob, os, re

CTX = '    <a href="docs/index.html">Context</a>\n'
added = 0
for p in sorted(glob.glob("*.html")):
    s = open(p, encoding="utf-8").read()
    orig = s
    if 'href="docs/index.html"' not in s:
        s = s.replace('    <a href="08-adapted.html">Adapted mode</a>\n',
                      '    <a href="08-adapted.html">Adapted mode</a>\n' + CTX)
    # the nav wordmark is a project label, not an app name — the app is unnamed
    s = s.replace('<b>Floor</b>', '<b>Design review</b>')
    if 'js/shot.js' not in s:
        s = s.replace('</body>', '<script src="js/shot.js"></script>\n</body>')
    if s != orig:
        open(p, "w", encoding="utf-8").write(s); added += 1
        print(f"  updated {p}")
print(f"{added} page(s) updated")
