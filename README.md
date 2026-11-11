# Dossier Kiroween

Dossier de travail ouvert du hackathon [Kiroween 2026](https://kiroween.devpost.com/) :
**1 850 idées** générées par vagues successives, **quatre classements** sur quatre critères dominants
différents, et **quatorze cahiers des charges** complets.

**Site publié** : <https://baptistefaisy.github.io/kiroween-dossier/>

## Contenu

```
index.md        la page d'accueil du site
src/            les sources Markdown — une seule source de vérité
tools/          le générateur de site (python-markdown, une seule implémentation)
site/           la génération locale, pour relecture hors ligne
docs/           la génération publiée par GitHub Pages
.github/        ci.yml (garde-fous) et pages.yml (anti-dérive)
```

## Régénérer le site

```bash
python3 -m pip install markdown
python3 tools/build_site.py site/     # relecture locale
python3 tools/build_site.py docs/     # ce qui est publié
```

La CI vérifie que `docs/` correspond exactement à ce que le générateur produit depuis `src/` :
modifier le texte sans régénérer le site fait échouer le build.

## Les quatre classements

| Classement | Critère dominant | Ce qu'il met en tête |
|---|---|---|
| `classement-technique` | élégance technique et plan de vidéo | métaphores brillantes, usage rare |
| `classement-2mois` | ambition à horizon deux mois | moteurs profonds, public encore étroit |
| `classement-usage` | réalité de l'usage (75 points sur 100) | obligations légales, argent, fréquence |
| `classement-devs` | **reconnaissance immédiate par un développeur** | sûreté des agents IA, preuve, exploitation honnête |

Les quatre sont conservés : la comparaison montre ce que le changement de critère fait entrer et sortir,
et c'est la partie la plus utile du dossier.

## Garde-fous

- Licence MIT présente et détectable.
- Aucun fichier de code au-delà de 500 lignes.
- CI bornée à 5 minutes, `concurrency` actif, `fetch-depth: 1`.
- Aucune page vide ; les classements contiennent leurs tableaux.

## Avertissement

Dossier public : il expose une stratégie de concours à environ 12 000 autres participants. Choix assumé —
la valeur est dans l'exécution, pas dans la liste.
