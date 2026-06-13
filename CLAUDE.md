# CLAUDE.md  (read this first, then stop)

Knihovna 16 sociálních karet (HTML do PNG). Tahle stránka je celý kontext.

## Jak to funguje
- `templates/NN-slug/index.html` = karta v přesných pixelech (vygenerováno).
  `templates/NN-slug/card.png` = vyrenderovaný obrázek. NEEDITUJ ručně.
- Zdroj pravdy: `build/build.py` (designy `d_<name>` + CSS, sazba ve `vmin`) a
  `build/content.py` (seznam `ITEMS`, presety témat nahoře).
- Build HTML: `python3 build/build.py`. Render PNG: `node shot.mjs` (Playwright).
  Galerie: `python3 build/gallery.py`.

## Nejčastější úkol: upravit jednu kartu
1. Najdi `NN` v tabulce dole.
2. Uprav její `dict(...)` v `build/content.py` (`content`, `theme`, `fmt`, `design`).
3. `python3 build/build.py` a `node shot.mjs`. Hotovo.
4. Deploy jen na vyžádání: `vercel deploy --prod --yes`.
   Web: https://30socialcards.vercel.app  GitHub: kereptom/social-cards

## Co NEČÍST: jiné projekty, templates/ ručně.
## Pravidla: dummy obsah; nikdy em dash (U+2014); každý nadpis může mít <em> pro akcent.
## Formáty: og 1200x630, sq 1080x1080, story 1080x1920, wide 1600x900.

## Index (NN -> slug -> design / formát)

| NN | slug | název | design | fmt |
|----|------|-------|--------|-----|
| 01 | `01-quote-og` | Citát (OG) | quote | og |
| 02 | `02-stat-square` | Statistika | stat | sq |
| 03 | `03-announce-og` | Oznámení | headline | og |
| 04 | `04-event-story` | Událost | event | story |
| 05 | `05-tips-square` | Tipy | list | sq |
| 06 | `06-promo-square` | Akce | promo | sq |
| 07 | `07-blogpost-og` | Článek | headline | og |
| 08 | `08-testimonial-square` | Reference | quote | sq |
| 09 | `09-rating-og` | Hodnocení | stat | og |
| 10 | `10-hiring-square` | Nábor | headline | sq |
| 11 | `11-webinar-og` | Webinář | event | og |
| 12 | `12-flashsale-story` | Flash sale | promo | story |
| 13 | `13-launch-wide` | Uvedení | headline | wide |
| 14 | `14-howto-story` | Návod | list | story |
| 15 | `15-editorial-wide` | Editorial | quote | wide |
| 16 | `16-milestone-story` | Milník | stat | story |
