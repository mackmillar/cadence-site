import html, json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import GUIDES, CTA

SITE = sys.argv[1]
BASE = "https://cadencegym.app/"
by = {g["slug"]: g for g in GUIDES}
MONTHS = "January February March April May June July August September October November December".split()

def nice(d):
    y, m, dd = d.split("-"); return f"{int(dd)} {MONTHS[int(m)-1]} {y}"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{ogtype}">
<meta property="og:site_name" content="Cadence">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://cadencegym.app/logo.png">
<meta name="twitter:card" content="summary">
<link rel="icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<header class="nav">
  <a class="brand" href="./"><img src="logo.png" alt="" width="28" height="28">Cadence</a>
  <nav>
    <a href="guides">Guides</a>
    <a href="./#how">How it works</a>
    <a class="pill" href="./#get">Get the app</a>
  </nav>
</header>
<main class="wrap">
"""
FOOT = """
  <hr class="rule">
  <footer><a href="./">Cadence</a> · <a href="guides">Guides</a> · <a href="press">Press</a> · <a href="privacy">Privacy</a> · <a href="terms">Terms</a> · <a href="mailto:support@cadencegym.app">support@cadencegym.app</a></footer>
</main>
</body>
</html>
"""
e = lambda s: html.escape(s, quote=True)

def crumbs(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def guide(g):
    url = BASE + g["slug"]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": g["h1"], "description": g["desc"],
         "datePublished": g["published"], "dateModified": g.get("modified", g["published"]),
         "mainEntityOfPage": url, "image": BASE + "logo.png",
         "author": {"@type": "Organization", "name": "Cadence", "url": BASE},
         "publisher": {"@type": "Organization", "name": "Cadence", "logo": {"@type": "ImageObject", "url": BASE + "logo.png"}}},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]},
        crumbs([("Cadence", BASE), ("Guides", BASE + "guides"), (g["short"], url)]),
    ]}
    out = HEAD.format(title=e(g["title"] + " — Cadence"), desc=e(g["desc"]), url=url, ogtype="article",
                      ogtitle=e(g["h1"]), ld=json.dumps(ld, indent=2, ensure_ascii=False))
    out += f'  <p class="crumbs"><a href="guides">Guides</a></p>\n'
    out += f'  <h1>{e(g["h1"])}</h1>\n  <p class="meta">{e(g["kicker"])} · {nice(g.get("modified", g["published"]))}</p>\n'
    out += g["body"]
    out += "\n  <h2>Questions</h2>\n  <div class=\"qs\">\n"
    for q, a in g["faq"]:
        out += f'    <details class="q"><summary>{e(q)}</summary><p>{e(a)}</p></details>\n'
    out += "  </div>\n\n  " + CTA + "\n"
    out += '\n  <h2>More guides</h2>\n  <div class="cards">\n'
    for s in g["related"]:
        r = by[s]
        out += f'    <a class="card" href="{s}"><b>{e(r["short"])}</b><span>{e(r["card"])}</span></a>\n'
    out += "  </div>\n" + FOOT
    return out

def index():
    url = BASE + "guides"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": "Gym guides", "url": url,
         "hasPart": [{"@type": "Article", "headline": g["h1"], "url": BASE + g["slug"]} for g in GUIDES]},
        crumbs([("Cadence", BASE), ("Guides", url)])]}
    out = HEAD.format(title="Gym guides: how often to go, rest days, habits and gym anxiety — Cadence",
                      desc=e("Plain, short guides to building a gym habit that lasts: how often to go, the best time, rest days, session length, gym anxiety and how long results take, plus honest gym app comparisons."),
                      url=url, ogtype="website", ogtitle="Gym guides from Cadence", ld=json.dumps(ld, indent=2, ensure_ascii=False))
    out += "  <h1>Gym guides</h1>\n  <p class=\"meta\">Short, plain answers about the hardest part: turning up.</p>\n"
    for heading, sec in (("", None), ("Comparing gym apps", "compare")):
        if heading:
            out += f"\n  <h2>{heading}</h2>\n"
        out += '  <div class="cards">\n'
        for g in GUIDES:
            if g.get("section") == sec:
                out += f'    <a class="card" href="{g["slug"]}"><b>{e(g["short"])}</b><span>{e(g["card"])}</span></a>\n'
        out += "  </div>\n"
    out += "\n  " + CTA + "\n" + FOOT
    return out

for g in GUIDES:
    open(os.path.join(SITE, g["slug"] + ".html"), "w").write(guide(g))
open(os.path.join(SITE, "guides.html"), "w").write(index())

urls = [("", "2026-10-30"), ("guides", "2026-10-30")] + [(g["slug"], g.get("modified", g["published"])) for g in GUIDES] + [("press", "2026-10-30"), ("privacy", "2026-10-15"), ("terms", "2026-10-15")]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm += "".join(f"  <url><loc>{BASE}{p}</loc><lastmod>{d}</lastmod></url>\n" for p, d in urls) + "</urlset>\n"
open(os.path.join(SITE, "sitemap.xml"), "w").write(sm)
print("built", len(GUIDES), "guides")
