# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import ITEMS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = "\n".join(f"| {i['slug'].split('-')[0]} | `{i['slug']}` | {i['name']} | {i['design']} | {i['fmt']} |" for i in ITEMS)
doc = """# CLAUDE.md  (read this first, then stop)

Knihovna {N} sociálních karet (HTML do PNG). Tahle stránka je celý kontext.

## Jak to funguje
- `templates/NN-slug/index.html` = karta v přesných pixelech (vygenerováno).
  `templates/NN-slug/card.png` = vyrenderovaný obrázek. NEEDITUJ ručně.
- Zdroj pravdy: `build/build.py` (designy `d_<name>` + CSS, sazba ve `vmin`) a
  `build/content.py` (seznam `ITEMS`, presety témat nahoře).
- Build HTML: `python3 build/build.py`. Render PNG: `node shot.mjs` (potřebuje
  Playwright; pokud chybí node_modules, spusť render z projektu, který ho má).
  Galerie: `python3 build/gallery.py`.

## Nejčastější úkol: upravit jednu kartu
1. Najdi `NN` v tabulce dole.
2. Uprav její `dict(...)` v `build/content.py` (`content`, `theme`, `fmt`, `design`).
3. `python3 build/build.py` a render PNG. Hotovo.
4. Deploy jen na vyžádání: `vercel deploy --prod --yes`.
   Web: https://30socialcards.vercel.app  GitHub: kereptom/social-cards

## Designy: headline, quote, stat, event, list, promo, profile, checklist, countdown, compare.
## Formáty: og 1200x630, sq 1080x1080, story 1080x1920, wide 1600x900.
## Co NEČÍST: jiné projekty, templates/ ručně.
## Pravidla: dummy obsah; nikdy em dash (U+2014); akcent v nadpisu přes <em>; v obsahu používej znak `·`, ne `&middot;` (escapuje se).

## Index (NN -> slug -> design / formát)

| NN | slug | název | design | fmt |
|----|------|-------|--------|-----|
{ROWS}
""".replace("{N}", str(len(ITEMS))).replace("{ROWS}", rows)
assert chr(0x2014) not in doc
open(os.path.join(ROOT, "CLAUDE.md"), "w", encoding="utf-8").write(doc)
print("CLAUDE.md regenerated:", len(ITEMS), "rows")
