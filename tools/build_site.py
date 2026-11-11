#!/usr/bin/env python3
"""Construit le site statique du dossier Kiroween à partir des sources Markdown.

Une seule implémentation : ce script sert en local et dans la CI.
Usage : python3 tools/build_site.py [repertoire_de_sortie]
"""
from __future__ import annotations

import pathlib
import re
import sys

try:
    import markdown
except ImportError:
    sys.exit("python-markdown absent. Installer : pip install markdown")

RACINE = pathlib.Path(__file__).resolve().parent.parent
EXTENSIONS = ["tables", "fenced_code", "toc", "sane_lists"]
TITRE_SITE = "Dossier Kiroween — Hackathon 2026"
ACCROCHE = (
    "2 400 idées générées, quatre classements successifs, "
    "quatorze cahiers des charges complets."
)

# (source, slug, label de navigation)
PAGES = [
    ("index.md", "index", "Accueil"),
    ("src/classement-usage.md", "classement-usage", "Classement usage — 39"),
    ("src/classement-2mois.md", "classement-2mois", "Classement 2 mois — 39"),
    ("src/classement-technique.md", "classement-technique", "Classement technique — 39"),
    ("src/idees-usage.md", "idees-usage", "Idées · usage réel (250)"),
    ("src/idees-2mois.md", "idees-2mois", "Idées · horizon 2 mois (400)"),
    ("src/idees-semaine.md", "idees-semaine", "Idées · 15 filons (750)"),
    ("src/idees-devs.md", "idees-devs", "Idées · développeurs (1 000)"),
    ("src/classement-devs.md", "classement-devs", "Classement devs — 50"),
    ("src/cahiers-developpeurs.md", "cahiers-devs", "Cahiers devs — 10"),
    ("src/DISQUETTE-cahier.md", "disquette", "Cahier · Disquette"),
    ("src/ROTA-cahier.md", "rota", "Cahier · Rota"),
    ("src/PARTIE-DOUBLE-cahier.md", "partie-double", "Cahier · Partie double"),
    ("src/SEANCE-cahier.md", "seance", "Cahier · Séance"),
    ("src/cadre-concours.md", "cadre", "Cadre du concours"),
    ("src/consigne-2mois.md", "consigne", "Consigne de génération"),
    ("src/grille-notation.md", "grille", "Grille de notation"),
]

CSS = """
:root{--fg:#e8e6e3;--bg:#111014;--card:#1b1a20;--acc:#e08b3c;--acc2:#8fd3c7;
 --mut:#9b968f;--bd:#2c2a33}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
 font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
header{padding:1.4rem 1.2rem;border-bottom:1px solid var(--bd);background:var(--card)}
header h1{margin:0;font-size:1.25rem}
header p{margin:.3rem 0 0;color:var(--mut);font-size:.9rem}
nav{display:flex;flex-wrap:wrap;gap:.4rem;padding:.8rem 1.2rem;border-bottom:1px solid var(--bd)}
nav a{color:var(--mut);text-decoration:none;font-size:.85rem;padding:.3rem .6rem;
 border:1px solid var(--bd);border-radius:999px}
nav a:hover{color:var(--fg)}
nav a.actif{color:#111014;background:var(--acc);border-color:var(--acc);font-weight:600}
main{padding:1.2rem;max-width:64rem;margin:0 auto}
main h1{font-size:1.6rem;border-bottom:1px solid var(--bd);padding-bottom:.4rem}
main h2{font-size:1.25rem;margin-top:2rem;color:var(--acc)}
main h3{font-size:1.05rem;margin-top:1.6rem;color:var(--acc2)}
a{color:var(--acc2)}
code{background:#0c0b0f;padding:.1rem .35rem;border-radius:4px;font-size:.88em}
pre{background:#0c0b0f;padding:.9rem;border-radius:8px;overflow-x:auto;border:1px solid var(--bd)}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.9rem;display:block;overflow-x:auto}
th,td{border:1px solid var(--bd);padding:.45rem .6rem;text-align:left;vertical-align:top}
th{background:var(--card);white-space:nowrap}
blockquote{border-left:3px solid var(--acc);margin:1rem 0;padding:.2rem 1rem;color:var(--mut)}
hr{border:0;border-top:1px solid var(--bd);margin:2rem 0}
footer{padding:1.2rem;color:var(--mut);font-size:.85rem;border-top:1px solid var(--bd);text-align:center}
@media (prefers-reduced-motion:no-preference){nav a{transition:color .15s,background .15s}}
"""


def gabarit(titre: str, corps: str, actif: str) -> str:
    """Une page complète : en-tête, navigation, corps, pied de page."""
    liens = []
    for _src, slug, label in PAGES:
        cls = ' class="actif"' if slug == actif else ""
        liens.append(f'<a href="{slug}.html"{cls}>{label}</a>')
    nav = "\n".join(liens)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titre} — {TITRE_SITE}</title>
<style>{CSS}</style>
</head>
<body>
<header>
<h1>{TITRE_SITE}</h1>
<p>{ACCROCHE}</p>
</header>
<nav>
{nav}
</nav>
<main>
{corps}
</main>
<footer>Généré depuis les sources Markdown du dépôt, vérifié sans dérive en CI. Licence MIT.</footer>
</body>
</html>
"""


ITEM = re.compile(r"^\d{2}\. ")


def preparer(texte: str) -> str:
    """Insère une ligne vide avant chaque bloc d'idées numérotées.

    Sans cette ligne vide, Markdown traite les lignes « 01. … » comme la
    continuation paresseuse du paragraphe précédent : le bloc entier devient
    un seul paragraphe illisible au lieu d'une liste.
    """
    sortie: list[str] = []
    for ligne in texte.split("\n"):
        if ITEM.match(ligne):
            precedente = sortie[-1] if sortie else ""
            if precedente.strip() and not ITEM.match(precedente):
                sortie.append("")
        sortie.append(ligne)
    return "\n".join(sortie)


def convertir(src: pathlib.Path) -> str:
    texte = preparer(src.read_text(encoding="utf-8"))
    return markdown.markdown(texte, extensions=EXTENSIONS, output_format="html5")


def construire(sortie: pathlib.Path) -> int:
    """Génère toutes les pages dans `sortie`. Renvoie 0 si tout est présent."""
    if sortie.exists():
        for ancien in sortie.glob("*.html"):
            ancien.unlink()
    sortie.mkdir(parents=True, exist_ok=True)
    (sortie / "styles.css").write_text(CSS, encoding="utf-8")
    for rel, slug, label in PAGES:
        src = RACINE / rel
        if not src.exists():
            print(f"source absente : {rel}", file=sys.stderr)
            return 1
        html = gabarit(label, convertir(src), slug)
        (sortie / f"{slug}.html").write_text(html, encoding="utf-8")
        print(f"  {slug}.html  ({len(html)} octets)")
    return 0


if __name__ == "__main__":
    cible = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "site"
    sys.exit(construire(cible))
