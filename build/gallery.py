# -*- coding: utf-8 -*-
import os, html
from content import ITEMS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FMT = {"og": "1200x630 OG", "sq": "1080x1080 čtverec", "story": "1080x1920 story", "wide": "1600x900 wide"}
CARD = """      <a class="card" href="templates/{slug}/index.html" data-fmt="{fmt}">
        <div class="thumb"><img src="gallery/shots/{nn}.png" alt="{name}" loading="lazy"></div>
        <div class="meta"><div class="name">{name}</div>
          <div class="tags"><span>{design}</span><span>{fmtlabel}</span></div></div></a>"""
PAGE = """<!doctype html><html lang="cs"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Sociální karty a OG obrázky</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='13' height='13' x='2.5' y='2.5' rx='3' fill='%238b7bff'/%3E%3Crect width='13' height='13' x='16.5' y='2.5' rx='3' fill='%23aef03a'/%3E%3Crect width='13' height='13' x='2.5' y='16.5' rx='3' fill='%23ff7a3c'/%3E%3Crect width='13' height='13' x='16.5' y='16.5' rx='3' fill='%23e0249a'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--bg:#fbfbfd;--card:#fff;--ink:#1d1d1f;--ink2:#6e6e73;--ink3:#86868b;--line:#e6e6eb;--blue:#0071e3}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Inter","Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;line-height:1.47}
.nav{position:sticky;top:0;z-index:50;background:rgba(251,251,253,.82);backdrop-filter:saturate(180%) blur(20px);border-bottom:1px solid var(--line)}
.nav .in{max-width:1200px;margin:0 auto;padding:0 22px;height:52px;display:flex;align-items:center;justify-content:space-between}
.nav .brand{display:flex;align-items:center;gap:10px;font-weight:600;font-size:16px}
.nav .logo{display:grid;grid-template-columns:1fr 1fr;gap:2px;width:20px;height:20px}.nav .logo i{border-radius:3px}
.nav a{color:var(--ink2);text-decoration:none;font-size:14px}
.wrap{max-width:1200px;margin:0 auto;padding:0 22px}
.hero{text-align:center;padding:92px 0 26px}
.hero h1{font-size:clamp(42px,7vw,84px);font-weight:800;letter-spacing:-.035em;line-height:1.04}
.hero .grad{background:linear-gradient(110deg,#8b7bff,#e0249a 42%,#ff7a3c 74%,#aef03a);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{margin:22px auto 0;max-width:640px;font-size:clamp(18px,2.4vw,22px);color:var(--ink2)}
.note{display:inline-flex;gap:8px;margin-top:24px;background:#f3eefe;color:#5b3a9a;border:1px solid #e2d6fb;border-radius:999px;padding:8px 16px;font-size:13.5px}
.stats{display:flex;justify-content:center;flex-wrap:wrap;gap:34px;margin-top:30px;color:var(--ink2);font-size:14px}
.stats b{display:block;font-size:30px;font-weight:700;color:var(--ink)}
.filters{display:flex;justify-content:center;gap:8px;margin:40px 0 0;flex-wrap:wrap}
.filters button{font:inherit;font-size:14px;color:var(--ink2);background:#fff;border:1px solid var(--line);border-radius:999px;padding:8px 16px;cursor:pointer}
.filters button.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px;padding:30px 0}
.card{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;text-decoration:none;color:inherit;transition:transform .22s,box-shadow .22s}
.card:hover{transform:translateY(-6px);box-shadow:0 18px 40px rgba(0,0,0,.10)}
.thumb{aspect-ratio:16/10;background:#1a1a22;display:flex;align-items:center;justify-content:center;padding:14px}
.thumb img{max-width:100%;max-height:100%;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.35)}
.meta{padding:14px 16px 16px}.name{font-weight:600;font-size:17px}
.tags{display:flex;gap:6px;margin-top:10px;font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--ink3)}
.tags span{border:1px solid var(--line);border-radius:6px;padding:3px 8px}
.how{border-top:1px solid var(--line);margin-top:24px;padding:60px 0 70px;text-align:center;color:var(--ink2)}
.how h2{color:var(--ink);font-size:clamp(26px,4vw,36px);font-weight:700;margin-bottom:14px}
.how code{font-family:ui-monospace,Menlo,monospace;font-size:.85em;background:#f0f0f3;border-radius:5px;padding:2px 6px}
.how a{color:var(--blue);text-decoration:none}
footer{border-top:1px solid var(--line);padding:24px 0 50px;color:var(--ink3);font-size:12.5px;text-align:center}
</style></head><body>
<div class="nav"><div class="in"><div class="brand"><span class="logo"><i style="background:#8b7bff"></i><i style="background:#aef03a"></i><i style="background:#ff7a3c"></i><i style="background:#e0249a"></i></span> Sociální karty</div><a href="#how">Jak to použít</a></div></div>
<div class="wrap"><section class="hero"><h1>HTML dovnitř.<br><span class="grad">{count} obrázků ven.</span></h1>
<p>Karty pro sociální sítě a OG náhledy. Návrh v HTML, export do PNG ve čtyřech formátech.</p>
<div class="note">⚠︎ Ukázkový (dummy) obsah. Texty uprav v <code>build/content.py</code>.</div>
<div class="stats"><div><b>{count}</b>karet</div><div><b>6</b>designů</div><div><b>4</b>formáty</div><div><b>PNG</b>export</div></div>
<div class="filters"><button class="on" data-f="all">Vše</button><button data-f="og">OG</button><button data-f="sq">Čtverec</button><button data-f="story">Story</button><button data-f="wide">Wide</button></div>
</section>
<div class="grid" id="grid">
{cards}
</div>
<section class="how" id="how"><h2>Jak z toho udělat vlastní obrázek</h2>
<p>Uprav texty v <code>build/content.py</code>, spusť <code>python3 build/build.py</code> a vyrenderuj přes <code>node shot.mjs</code> (Playwright). Hotové PNG je v <code>templates/&lt;slug&gt;/card.png</code>.<br>Každá karta je čisté HTML v přesných pixelech, sazba v jednotkách <code>vmin</code> se přizpůsobí formátu.</p>
<p style="margin-top:20px"><a href="README.md">README</a> &middot; <a href="https://github.com/kereptom/social-cards">GitHub</a></p></section>
</div>
<footer>Sociální karty a OG obrázky &middot; HTML do PNG &middot; ukázkový obsah</footer>
<script>const g=document.getElementById('grid');document.querySelectorAll('.filters button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.filters button').forEach(x=>x.classList.remove('on'));b.classList.add('on');const f=b.dataset.f;g.querySelectorAll('.card').forEach(c=>c.style.display=(f==='all'||c.dataset.fmt===f)?'':'none');});</script>
</body></html>"""
def main():
    cards = [CARD.format(slug=i["slug"], nn=i["slug"].split("-")[0], name=html.escape(i["name"]),
        design=i["design"], fmt=i["fmt"], fmtlabel=FMT[i["fmt"]]) for i in ITEMS]
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(
        PAGE.replace("{cards}", "\n".join(cards)).replace("{count}", str(len(ITEMS))))
    print("wrote index.html", len(cards))
if __name__ == "__main__": main()
