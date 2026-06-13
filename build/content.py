# -*- coding: utf-8 -*-
# Sample (dummy) social cards. em dash forbidden.
SORA = '"Sora", system-ui, sans-serif'
INT = '"Inter Tight", system-ui, sans-serif'
SG = '"Space Grotesk", system-ui, sans-serif'
FR = '"Fraunces", Georgia, serif'
UB = '"Unbounded", system-ui, sans-serif'

T_violet = dict(bg="#0e0c1a", ink="#f3f1fb", sub="#9b96b8", c1="#8b7bff", c2="#e0468a", ui=SORA, display=SORA, blobop="0.55")
T_light = dict(bg="#ffffff", ink="#16131f", sub="#6b6b7e", c1="#6d4aff", c2="#0e9e8e", ui=INT, display=INT, blobop="0.16")
T_orange = dict(bg="linear-gradient(135deg,#ff7a3c,#e0468a)", ink="#ffffff", sub="rgba(255,255,255,.86)", c1="#ffffff", c2="#ffd9c4", ui=SORA, display=SORA, blobop="0.18")
T_lime = dict(bg="#0a0e0c", ink="#eaf3ec", sub="#8aa394", c1="#aef03a", c2="#36d399", ui=SG, display=SG, blobop="0.4")
T_cream = dict(bg="#fbf6ee", ink="#1f1a12", sub="#7a6f5e", c1="#b3361f", c2="#c8862a", ui=INT, display=FR, blobop="0.14")
T_pink = dict(bg="#fff5fa", ink="#1c1019", sub="#7a6470", c1="#e0249a", c2="#7b2ff7", ui=SORA, display=UB, blobop="0.16")
T_navy = dict(bg="#0a0f1e", ink="#e8edf7", sub="#8893ad", c1="#4f8bff", c2="#2dd4bf", ui=INT, display=INT, blobop="0.5")

ITEMS = [
 dict(slug="01-quote-og", name="Citát (OG)", design="quote", fmt="og", theme=T_violet,
   content=dict(quote="Nevyhrává ten, kdo má nejvíc dat, ale kdo z nich nejrychleji udělá rozhodnutí.", author="Ukázkový autor", role="pro náhled šablony", brand="ZNAČKA")),
 dict(slug="02-stat-square", name="Statistika (čtverec)", design="stat", fmt="sq", theme=T_lime,
   content=dict(eyebrow="Meziroční růst", num="+248%", label="nárůst objednávek", sub="za posledních dvanáct měsíců", brand="ZNAČKA")),
 dict(slug="03-announce-og", name="Oznámení (OG)", design="headline", fmt="og", theme=T_orange,
   content=dict(eyebrow="Novinka", head="Spouštíme <em>v září</em>.", sub="Nová verze, na kterou jste čekali. Registrace už běží.", brand="ZNAČKA", handle="@znacka")),
 dict(slug="04-event-story", name="Událost (story)", design="event", fmt="story", theme=T_navy,
   content=dict(day="19", month="června", eyebrow="Workshop", head="AI pro <em>vaši firmu</em>.", meta="// 9:00 / Vinohradská / Praha", brand="ZNAČKA", handle="@znacka")),
 dict(slug="05-tips-square", name="Tipy (čtverec)", design="list", fmt="sq", theme=T_light,
   content=dict(eyebrow="Rychlé tipy", head="Tři tipy na <em>lepší prompt</em>.", items=["Řekněte cíl, ne jen téma","Dejte příklad správného výstupu","Nechte model ptát se zpět"], brand="ZNAČKA")),
 dict(slug="06-promo-square", name="Akce (čtverec)", design="promo", fmt="sq", theme=T_pink,
   content=dict(badge="Sleva", big="-40 %", head="Na všechny <em>roční plány</em>.", code="PODZIM40", brand="ZNAČKA", handle="@znacka")),
 dict(slug="07-blogpost-og", name="Článek (OG)", design="headline", fmt="og", theme=T_cream,
   content=dict(eyebrow="Blog / Návod", head="Jak napsat <em>zadání</em>, kterému AI rozumí.", sub="Sedm minut čtení. Konkrétní příklady a šablona ke stažení.", brand="ZNAČKA", handle="ctení 7 min")),
 dict(slug="08-testimonial-square", name="Reference (čtverec)", design="quote", fmt="sq", theme=T_pink,
   content=dict(quote="Za měsíc nám to ušetřilo desítky hodin práce. Nevrátíme se zpátky.", author="Ukázkový klient", role="provozní ředitel", brand="ZNAČKA")),
 dict(slug="09-rating-og", name="Hodnocení (OG)", design="stat", fmt="og", theme=T_navy,
   content=dict(eyebrow="Spokojenost", num="4,9 / 5", label="průměrné hodnocení", sub="z více než dvou tisíc recenzí", brand="ZNAČKA")),
 dict(slug="10-hiring-square", name="Nábor (čtverec)", design="headline", fmt="sq", theme=T_lime,
   content=dict(eyebrow="Hledáme posily", head="Vývojář/ka <em>do týmu</em>.", sub="Remote, plný úvazek, skvělá parta. Pošlete CV.", brand="ZNAČKA", handle="@znacka")),
 dict(slug="11-webinar-og", name="Webinář (OG)", design="event", fmt="og", theme=T_violet,
   content=dict(day="07", month="srpna", eyebrow="Online webinář", head="Automatizace <em>bez kódu</em>.", meta="// 18:00 / zdarma / online", brand="ZNAČKA", handle="@znacka")),
 dict(slug="12-flashsale-story", name="Flash sale (story)", design="promo", fmt="story", theme=T_orange,
   content=dict(badge="48 hodin", big="1+1", head="Druhý vstup <em>zdarma</em>.", code="DUO", brand="ZNAČKA", handle="@znacka")),
 dict(slug="13-launch-wide", name="Uvedení (wide)", design="headline", fmt="wide", theme=T_navy,
   content=dict(eyebrow="Verze 2.0", head="Rychlejší. Chytřejší. <em>Vaše.</em>", sub="Největší aktualizace v historii produktu je tady.", brand="ZNAČKA", handle="@znacka")),
 dict(slug="14-howto-story", name="Návod (story)", design="list", fmt="story", theme=T_light,
   content=dict(eyebrow="Začněte hned", head="Jak začít ve <em>třech krocích</em>.", items=["Založte si účet zdarma","Propojte svá data","Spusťte první report"], brand="ZNAČKA")),
 dict(slug="15-editorial-wide", name="Editorial (wide)", design="quote", fmt="wide", theme=T_cream,
   content=dict(quote="Dobrá značka není to, co řeknete vy. Je to, co si zapamatují ostatní.", author="Ukázkový citát", role="pro náhled šablony", brand="ZNAČKA")),
 dict(slug="16-milestone-story", name="Milník (story)", design="stat", fmt="story", theme=T_orange,
   content=dict(eyebrow="Děkujeme", num="10 000", label="spokojených klientů", sub="a teprve začínáme", brand="ZNAČKA")),
]
