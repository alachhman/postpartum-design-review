#!/usr/bin/env python3
"""Render the context markdown files into the design-review site."""
import html, os, re, shutil
import markdown

SRC  = "claude_design_context"
OUT  = "site/docs"
os.makedirs(OUT, exist_ok=True)

DOCS = [
    ("00_README.md",           "Package README",   "Contents, authority order, and the original kickoff prompt."),
    ("02_MVP_Design_Brief.md", "MVP Design Brief",  "Source of truth. Every locked product decision, screen list and v1 scope."),
    ("04_Style_Guide.md",      "Style Guide",       "Visual language, palette, components and the firm voice rules."),
    ("05_Design_Research.md",  "Design Research",   "Four research streams, a Reddit field pass, and the ten things that should change."),
    ("01_Conversation_Log.md", "Conversation Log",  "The full founder working session — ideation through every scoping decision, with reasoning."),
    ("03_Market_Research.md",  "Market Research",   "Audience, competitors, the GLP-1 thesis, barriers to entry and unit economics."),
]

NAV = """<nav class="nav"><div class="nav-in">
  <a class="nav-mark" href="{root}index.html">
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M2 13a8 8 0 0 1 16 0" stroke="#C98A5B" stroke-width="1.6" stroke-linecap="round"/><path d="M2 16.5h16" stroke="#F0EBE1" stroke-width="1.6" stroke-linecap="round"/></svg>
    <b>Design review</b></a>
  <div class="nav-links">
    <a href="{root}index.html">Overview</a>
    <a href="{root}01-home.html">Home</a>
    <a href="{root}02-checkin.html">Check-in</a>
    <a href="{root}03-nudges.html">Nudges</a>
    <a href="{root}04-onboarding.html">Onboarding</a>
    <a href="{root}05-log.html">Log</a>
    <a href="{root}06-trends.html">Trends</a>
    <a href="{root}07-paywall.html">Paywall</a>
    <a href="{root}08-adapted.html">Adapted mode</a>
    <a href="{root}docs/index.html"{docsel}>Context</a>
  </div>
</div></nav>"""

HEAD = """<!doctype html><html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&family=Instrument+Serif&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/site.css">
<link rel="stylesheet" href="{root}css/docs.css">
</head><body>"""

FOOT = """<footer><div class="wrap f-in">
  <span>Source document · rendered from the repository markdown</span>
  <span>Working material · share the link deliberately</span>
</div></footer></body></html>"""

def slugify(t):
    s = re.sub(r"<[^>]+>", "", t)
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s) or "section"

def build(fname, title, blurb, prev, nxt):
    raw = open(os.path.join(SRC, fname), encoding="utf-8").read()
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists",
                                       "attr_list", "toc", "footnotes", "md_in_html"],
                           extension_configs={"toc": {"slugify": lambda v, s: slugify(v),
                                                      "permalink": False}})
    body = md.convert(raw)

    toc = []
    for t in md.toc_tokens:
        toc.append((2, t["name"], t["id"]))
        for c in t.get("children", []):
            toc.append((3, c["name"], c["id"]))
            for gc in c.get("children", []):
                toc.append((4, gc["name"], gc["id"]))
    tochtml = "".join(
        f'<li><a class="l{lvl}" href="#{i}">{html.escape(html.unescape(re.sub("<[^>]+>", "", n)))}</a></li>'
        for lvl, n, i in toc)

    words = len(re.findall(r"\S+", re.sub(r"<[^>]+>", " ", body)))
    extra = ""
    if fname == "03_Market_Research.md":
        extra = ('<div class="docnote"><b>Also available as the original .docx.</b> '
                 '<a href="03_Market_Research.docx">Download the Word version</a> — identical content, '
                 'kept for the formatting of the appendix tables.</div>')

    pager = '<div class="pager">'
    pager += f'<a href="{prev[0]}">← {prev[1]}</a>' if prev else '<span></span>'
    pager += f'<a href="{nxt[0]}">{nxt[1]} →</a>' if nxt else '<span></span>'
    pager += "</div>"

    page = (HEAD.format(title=title + " — context", root="../")
            + NAV.format(root="../", docsel=' aria-current="page"')
            + '<div class="wrap"><section class="dochead">'
              f'<span class="kind">Source document</span>'
              f'<div class="docmeta"><span>{fname}</span><span>{words:,} words</span>'
              f'<span>{len(toc)} sections</span></div></section>'
              '<div class="doclayout">'
              '<aside class="doctoc"><span class="tl">On this page</span><ul>' + tochtml + '</ul>'
              f'<span class="tl" style="margin-top:22px">All documents</span><ul>'
              + "".join(f'<li><a href="{f.replace(".md",".html")}">{t}</a></li>' for f, t, _ in DOCS)
              + '</ul></aside>'
              f'<article class="prose">{extra}{body}</article>'
              '</div>' + pager + '</div>' + FOOT)
    out = os.path.join(OUT, fname.replace(".md", ".html"))
    open(out, "w", encoding="utf-8").write(page)
    return words

total = 0
for i, (f, t, b) in enumerate(DOCS):
    prev = (DOCS[i-1][0].replace(".md", ".html"), DOCS[i-1][1]) if i else ("../index.html", "Overview")
    nxt  = (DOCS[i+1][0].replace(".md", ".html"), DOCS[i+1][1]) if i < len(DOCS)-1 else None
    w = build(f, t, b, prev, nxt)
    total += w
    print(f"  {f:28} {w:6,} words")

# --- docs index ---
cards = "".join(
    f'<a class="ix" href="{f.replace(".md",".html")}"><div class="n">{f.split("_")[0]}</div>'
    f'<div class="t">{t}</div><div class="d">{b}</div>'
    f'<div class="c">{len(open(os.path.join(SRC,f),encoding="utf-8").read().split()):,} words</div></a>'
    for f, t, b in DOCS)

idx = (HEAD.format(title="Context documents", root="../")
       + NAV.format(root="../", docsel=' aria-current="page"')
       + """<div class="wrap"><section class="hero" style="padding:70px 0 26px">
       <span class="eyebrow">Context</span><h1>The source documents.</h1>
       <p class="sub">Everything the designs were built from, rendered in full and readable in the browser.
       The brief is the source of truth on product decisions; the research is where the evidence lives;
       the log is where the reasoning behind each decision was recorded.</p>
       <div class="metabar"><span>6 documents</span><span>%s words total</span>
       <span>Authority order: brief &gt; style guide &gt; log &gt; market research</span></div>
       </section>
       <div class="docnote" style="margin-top:10px"><b>Heads up on what is in here.</b> These pages carry
       commercial strategy, pricing and unit economics, and the founding-creator arrangement. The site is
       excluded from search engines, but the URL works for anyone who has it and requires no sign-in —
       so share it deliberately.</div>
       <div class="indexgrid" style="margin-bottom:60px">%s</div></div>""" % (f"{total:,}", cards)
       + FOOT)
# reuse the index card styles from the overview page
idx = idx.replace("</head>", """<style>
  .indexgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:34px}
  @media(max-width:1100px){.indexgrid{grid-template-columns:repeat(2,1fr)}}
  @media(max-width:620px){.indexgrid{grid-template-columns:1fr}}
  .ix{display:block;text-decoration:none;border:1px solid var(--edge);border-radius:13px;
    padding:18px 18px 20px;background:var(--page-2);transition:.18s}
  .ix:hover{border-color:var(--fg-3);background:var(--page-3);transform:translateY(-2px)}
  .ix .n{font-family:var(--f-mono);font-size:10.5px;letter-spacing:.13em;color:var(--fg-3)}
  .ix .t{font-family:var(--f-disp);font-size:24px;line-height:1.1;margin:9px 0 6px;color:var(--fg)}
  .ix .d{font-size:13px;color:var(--fg-2);line-height:1.5}
  .ix .c{margin-top:12px;font-family:var(--f-mono);font-size:10px;letter-spacing:.09em;color:var(--fg-3);text-transform:uppercase}
</style></head>""")
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(idx)

# carry the .docx across as a download
shutil.copy(os.path.join(SRC, "03_Market_Research.docx"), os.path.join(OUT, "03_Market_Research.docx"))
print(f"\n  docs/index.html + {len(DOCS)} pages + .docx  ({total:,} words)")
