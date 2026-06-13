# Sociální karty a OG obrázky

Knihovna **30 karet pro sociální sítě** a OG náhledy. Návrh je čisté HTML
v přesných pixelech, render do PNG přes Playwright. Deset designů ve čtyřech
formátech (OG 1200x630, čtverec 1080x1080, story 1080x1920, wide 1600x900).

> Obsahuje **ukázkový (dummy) obsah**. Před použitím nahraď vlastním.

Živá galerie: `index.html`. Hotové PNG je v `templates/<slug>/card.png`.

## Designy
headline (oznámení, článek, nábor, uvedení), quote (citát, reference),
stat (velké číslo), event (datum + název), list (číslované tipy/kroky),
promo (sleva, kód).

## Použití
1. Uprav texty v `build/content.py` (každá karta = `dict` s `design`, `fmt`,
   `theme`, `content`).
2. `python3 build/build.py` vygeneruje HTML.
3. `node shot.mjs` (vyžaduje Playwright) vyrenderuje PNG do `templates/*/card.png`.
4. Galerii obnovíš `python3 build/gallery.py`.

Sazba je v jednotkách `vmin`, takže se text přizpůsobí každému formátu. Barvy
a fonty jsou v `theme` dictu (presety nahoře v `content.py`).

## Pravidla
Statické, nasazení `vercel deploy --prod`. Nikdy znak dlouhé pomlčky (em dash).
