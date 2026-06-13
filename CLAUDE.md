# CLAUDE.md  (read this first, then stop)

Knihovna 30 sociálních karet (HTML do PNG). Tahle stránka je celý kontext.

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
| 01 | `01-quote-og` | Citát (OG) | quote | og |
| 02 | `02-stat-square` | Statistika (čtverec) | stat | sq |
| 03 | `03-announce-og` | Oznámení (OG) | headline | og |
| 04 | `04-event-story` | Událost (story) | event | story |
| 05 | `05-tips-square` | Tipy (čtverec) | list | sq |
| 06 | `06-promo-square` | Akce (čtverec) | promo | sq |
| 07 | `07-blogpost-og` | Článek (OG) | headline | og |
| 08 | `08-testimonial-square` | Reference (čtverec) | quote | sq |
| 09 | `09-rating-og` | Hodnocení (OG) | stat | og |
| 10 | `10-hiring-square` | Nábor (čtverec) | headline | sq |
| 11 | `11-webinar-og` | Webinář (OG) | event | og |
| 12 | `12-flashsale-story` | Flash sale (story) | promo | story |
| 13 | `13-launch-wide` | Uvedení (wide) | headline | wide |
| 14 | `14-howto-story` | Návod (story) | list | story |
| 15 | `15-editorial-wide` | Editorial (wide) | quote | wide |
| 16 | `16-milestone-story` | Milník (story) | stat | story |
| 17 | `17-speaker-og` | Řečník (OG) | profile | og |
| 18 | `18-checklist-square` | Checklist (čtverec) | checklist | sq |
| 19 | `19-countdown-story` | Odpočet (story) | countdown | story |
| 20 | `20-compare-og` | Srovnání (OG) | compare | og |
| 21 | `21-hiring-story` | Nábor (story) | headline | story |
| 22 | `22-bigstat-wide` | Velké číslo (wide) | stat | wide |
| 23 | `23-quote-story` | Citát (story) | quote | story |
| 24 | `24-bigsale-og` | Velká sleva (OG) | promo | og |
| 25 | `25-reasons-og` | Důvody (OG) | list | og |
| 26 | `26-meetup-square` | Meetup (čtverec) | event | sq |
| 27 | `27-team-square` | Člen týmu (čtverec) | profile | sq |
| 28 | `28-packing-story` | Seznam (story) | checklist | story |
| 29 | `29-launchday-square` | Den D (čtverec) | countdown | sq |
| 30 | `30-thanks-square` | Poděkování (čtverec) | stat | sq |
