#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Social / OG image cards. Fixed-pixel HTML per card (rendered to PNG by the
shot script). 6 designs x formats x themes. No em dashes."""
import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "templates")
from content import ITEMS

FORMATS = {"og": (1200, 630), "sq": (1080, 1080), "story": (1080, 1920), "wide": (1600, 900)}

def e(s): return html.escape(str(s), quote=True)

# ---- design renderers: return inner HTML of .card -------------------------
def d_headline(c):
    return (f'<span class="eyebrow">{e(c.get("eyebrow",""))}</span>'
            f'<h1>{c["head"]}</h1><p class="sub">{e(c.get("sub",""))}</p>'
            f'<div class="foot"><span class="brand">{e(c["brand"])}</span><span class="handle">{e(c.get("handle",""))}</span></div>')
def d_quote(c):
    return (f'<div class="qmark">&ldquo;</div><blockquote>{e(c["quote"])}</blockquote>'
            f'<div class="by"><strong>{e(c["author"])}</strong><span>{e(c.get("role",""))}</span></div>'
            f'<div class="foot"><span class="brand">{e(c["brand"])}</span></div>')
def d_stat(c):
    return (f'<span class="eyebrow">{e(c.get("eyebrow",""))}</span>'
            f'<div class="bignum">{e(c["num"])}</div><p class="statlbl">{e(c["label"])}</p>'
            f'<p class="sub">{e(c.get("sub",""))}</p><div class="foot"><span class="brand">{e(c["brand"])}</span></div>')
def d_event(c):
    return (f'<div class="datechip"><span class="d">{e(c["day"])}</span><span class="m">{e(c["month"])}</span></div>'
            f'<span class="eyebrow">{e(c.get("eyebrow",""))}</span><h1>{c["head"]}</h1>'
            f'<div class="evmeta">{e(c.get("meta",""))}</div>'
            f'<div class="foot"><span class="brand">{e(c["brand"])}</span><span class="handle">{e(c.get("handle",""))}</span></div>')
def d_list(c):
    items = "".join(f'<li><span class="n">{i+1}</span><span>{e(x)}</span></li>' for i, x in enumerate(c["items"]))
    return (f'<span class="eyebrow">{e(c.get("eyebrow",""))}</span><h1>{c["head"]}</h1>'
            f'<ul class="list">{items}</ul><div class="foot"><span class="brand">{e(c["brand"])}</span></div>')
def d_promo(c):
    return (f'<span class="badge">{e(c.get("badge",""))}</span>'
            f'<div class="bignum">{e(c["big"])}</div><h1>{c["head"]}</h1>'
            f'<div class="code">{e(c.get("code",""))}</div>'
            f'<div class="foot"><span class="brand">{e(c["brand"])}</span><span class="handle">{e(c.get("handle",""))}</span></div>')
DESIGN = {"headline": d_headline, "quote": d_quote, "stat": d_stat, "event": d_event, "list": d_list, "promo": d_promo}

PAGE = """<!doctype html><html lang="{lang}"><head><meta charset="utf-8">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400..800&family=Sora:wght@400..800&family=Space+Grotesk:wght@400..700&family=Fraunces:opsz,wght@9..144,400..800&family=Unbounded:wght@400..700&family=JetBrains+Mono:wght@400..600&display=swap" rel="stylesheet">
<style>
:root{{--c-1:{c1};--c-2:{c2};--ink:{ink};--sub:{sub};--ui:{ui};--display:{display}}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden}}
.card{{position:relative;width:{W}px;height:{H}px;background:{bg};color:var(--ink);padding:8vmin;display:flex;flex-direction:column;justify-content:{justify};font-family:var(--ui);overflow:hidden}}
.blob{{position:absolute;border-radius:50%;filter:blur(8vmin);opacity:{blobop};pointer-events:none}}
.b1{{width:46vmin;height:46vmin;background:var(--c-1);top:-12vmin;right:-10vmin}}
.b2{{width:38vmin;height:38vmin;background:var(--c-2);bottom:-12vmin;left:-8vmin}}
.eyebrow{{font-family:var(--ui);font-weight:700;font-size:2.6vmin;letter-spacing:.14em;text-transform:uppercase;color:var(--c-1);margin-bottom:3vmin}}
h1{{font-family:var(--display);font-weight:800;font-size:8.4vmin;line-height:1.04;letter-spacing:-.02em;max-width:15ch;position:relative}}
h1 em{{font-style:normal;color:var(--c-1)}}
.sub{{font-size:3.2vmin;color:var(--sub);margin-top:3vmin;max-width:26ch;line-height:1.4}}
.foot{{position:absolute;left:8vmin;right:8vmin;bottom:7vmin;display:flex;align-items:center;justify-content:space-between}}
.brand{{font-family:var(--display);font-weight:700;font-size:3vmin;display:flex;align-items:center;gap:1.4vmin}}
.brand::before{{content:"";width:3.4vmin;height:3.4vmin;border-radius:0.9vmin;background:var(--c-1)}}
.handle{{font-family:"JetBrains Mono",monospace;font-size:2.5vmin;color:var(--sub)}}
.qmark{{font-family:var(--display);font-size:22vmin;line-height:.5;color:var(--c-1);margin-bottom:1vmin}}
blockquote{{font-family:var(--display);font-weight:600;font-size:6.6vmin;line-height:1.18;letter-spacing:-.015em;max-width:18ch}}
.by{{margin-top:5vmin}}.by strong{{font-family:var(--display);font-size:3.4vmin}}.by span{{display:block;color:var(--sub);font-size:2.7vmin;margin-top:.6vmin}}
.bignum{{font-family:var(--display);font-weight:800;font-size:20vmin;line-height:.92;letter-spacing:-.03em;color:var(--c-1)}}
.statlbl{{font-size:4vmin;font-weight:600;margin-top:1vmin}}
.datechip{{align-self:flex-start;background:var(--c-1);color:#fff;border-radius:2.4vmin;padding:2vmin 3vmin;text-align:center;margin-bottom:4vmin}}
.datechip .d{{display:block;font-family:var(--display);font-weight:800;font-size:7vmin;line-height:1}}
.datechip .m{{display:block;font-weight:700;font-size:2.6vmin;letter-spacing:.1em;text-transform:uppercase}}
.evmeta{{font-family:"JetBrains Mono",monospace;font-size:3vmin;color:var(--sub);margin-top:3vmin}}
.list{{list-style:none;margin-top:4vmin;display:flex;flex-direction:column;gap:3vmin}}
.list li{{display:flex;gap:3vmin;align-items:center;font-size:4vmin;font-weight:600}}
.list .n{{flex:none;width:7vmin;height:7vmin;border-radius:50%;background:var(--c-1);color:#fff;font-family:var(--display);font-weight:800;display:flex;align-items:center;justify-content:center;font-size:3.4vmin}}
.badge{{align-self:flex-start;background:var(--c-1);color:#fff;font-weight:700;font-size:2.8vmin;letter-spacing:.1em;text-transform:uppercase;padding:1.4vmin 3vmin;border-radius:999px;margin-bottom:3vmin}}
.code{{align-self:flex-start;margin-top:3vmin;font-family:"JetBrains Mono",monospace;font-size:3.4vmin;font-weight:600;border:0.5vmin dashed var(--c-1);color:var(--c-1);padding:1.6vmin 3vmin;border-radius:1.4vmin}}
</style></head><body>
<div class="card"><div class="blob b1"></div><div class="blob b2"></div>{inner}</div>
</body></html>"""

def build_one(it):
    W, H = FORMATS[it["fmt"]]
    t = it["theme"]
    inner = DESIGN[it["design"]](it["content"])
    justify = "center" if it["design"] in ("quote", "stat", "promo") else "center"
    p = PAGE.format(lang=it.get("lang", "cs"), title=e(it["name"]), W=W, H=H,
        c1=t["c1"], c2=t.get("c2", t["c1"]), ink=t["ink"], sub=t["sub"], ui=t["ui"], display=t["display"],
        bg=t["bg"], blobop=t.get("blobop", "0.5"), justify=justify, inner=inner)
    d = os.path.join(TPL, it["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(p)

if __name__ == "__main__":
    import json
    man = []
    for it in ITEMS:
        build_one(it)
        W, H = FORMATS[it["fmt"]]
        man.append(dict(slug=it["slug"], nn=it["slug"].split("-")[0], w=W, h=H, name=it["name"], fmt=it["fmt"]))
    json.dump(man, open(os.path.join(ROOT, "build", "manifest.json"), "w"), ensure_ascii=False)
    print("built", len(ITEMS), "cards")
