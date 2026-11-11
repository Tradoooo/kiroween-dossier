# Dossier Kiroween — 1 350 idées, classées par cas d'usage réel

Dossier de travail ouvert du hackathon **Kiroween 2026** (Kiro, clôture des soumissions le
4 décembre 2026, fin du jugement le 29 janvier 2027). Il contient tout ce qui a servi à choisir
quoi construire : le corpus d'idées, les trois classements successifs et quatre cahiers des charges
complets.

Le site est **généré** depuis les sources Markdown de `src/` par `tools/build_site.py`, et la CI
vérifie qu'il n'y a aucune dérive entre le texte et les pages publiées.

## Ce qu'il y a à lire, dans l'ordre

| Page | Contenu |
|---|---|
| **[Classement usage — 39](classement-usage.html)** | Le classement qui fait foi : 39 idées notées sur une grille où **75 points sur 100 viennent de la réalité de l'usage** (obligation légale, argent en jeu, fréquence, utilisateur nommable) et 25 seulement de la séduction. |
| [Classement 2 mois — 39](classement-2mois.html) | L'étape précédente : les mêmes 39 notées à l'horizon deux mois, mais encore dominées par l'élégance technique. |
| [Classement technique — 39](classement-technique.html) | Le premier classement, à l'échelle d'une semaine de construction. Conservé pour la traçabilité. |
| [Idées · usage réel](idees-usage.html) | 200 idées ciblées sur quatre filons à forte obligation : métiers de bouche, social et aide à domicile, associations, argent du foyer. |
| [Idées · horizon 2 mois](idees-2mois.html) | 400 idées ambitieuses : paradigmes et protocoles morts, squelettes à moteur profond, domaines réglementés. |
| [Idées · 15 filons](idees-semaine.html) | 750 idées de la première vague, une par filon de technologie morte ou de squelette. |
| [Cahier · Disquette](disquette.html) | Cahier des charges complet en 18 sections : la disquette 1,44 Mo ressuscitée comme budget dur du web. |
| [Cahier · Rota](rota.html) | Squelette d'ordonnancement sous contraintes et ses deux applications (banque alimentaire, championnat). |
| [Cahier · Partie double](partie-double.html) | Squelette de grand livre immuable et ses deux applications (enveloppes d'un foyer, fonds d'entraide public). |
| [Cahier · Séance](seance.html) | Retour d'expérience où les fantômes du dépôt se contredisent (Costume Contest). |
| [Cadre du concours](cadre.html) | Règlement vérifié, grille du jury, portefeuille déjà soumis, socle technique commun. |
| [Consigne de génération](consigne.html) | La consigne exacte donnée aux agents qui ont produit les idées. |
| [Grille de notation](grille.html) | Critères, malus et bonus appliqués au classement technique. |

## Le podium du classement « usage d'abord »

| Rang | Idée | Catégorie | Pourquoi |
|---|---|---|---|
| 1 | **Registre** | Skeleton Crew | Chaîne du froid HACCP et registre de sécurité d'un établissement recevant du public : relevés **deux fois par jour**, obligation légale, sanction jusqu'à la fermeture administrative. Aujourd'hui un cahier papier. |
| 2 | **Compte rendu financier** | Frankenstein | Toute association subventionnée doit rendre un compte rendu conforme à un modèle officiel, sous peine de reversement. 1,5 million d'associations concernées en France. |
| 3 | **Facture contestée** | Resurrection | Contrôle de l'index, de la TVA et des coefficients d'une facture d'énergie : argent rendu, des millions de foyers, litiges fréquents. |
| 4 | **Agios à la loupe** | Resurrection | Recalcul du coût réel d'un découvert et des commissions. Mensuel, public fragile, aucune protection existante. |
| 5 | **Allées** | Costume Contest | Registre des concessions funéraires des 35 000 communes : obligation, échéances, reprises, contentieux. Quasi aucun outil abordable. |

## La leçon de méthode, écrite noir sur blanc

Trois classements successifs ont été produits sur le même corpus, avec trois critères dominants
différents : d'abord **l'élégance technique**, puis **l'ambition à deux mois**, enfin **l'usage réel**.
Les deux premiers classements hissaient en tête des idées brillantes et peu utilisées
(vérificateur de chiffres façon règle à calculer, rapport exécutable, métaphores hantées).
Le troisième les fait toutes sortir du haut du tableau.

> Ce ne sont ni les technologies mortes ni les costumes qui font gagner, ce sont **les obligations**.
> Un registre obligatoire tenu deux fois par jour par des centaines de milliers de professionnels bat
> n'importe quelle métaphore brillante. La catégorie du concours devient un habillage : on choisit
> d'abord l'obligation, ensuite la catégorie où elle score le mieux.

## Comment ce corpus a été produit

- **Vague 1** — 15 sous-agents, 15 filons disjoints (supports de stockage morts, réseaux et protocoles
  morts, terminaux et saisie, bureau et papier, domestique et médias, instruments analogiques, paradigmes
  logiciels, squelettes algorithmiques, associations, données publiques, artisans, pédagogie, rituels,
  lieux hantés, monstres) : **750 idées**.
- **Vague 2** — horizon porté de huit jours à **deux mois**, avec v1 avant le 4 décembre et version
  complète avant la fin du jugement : **400 idées** sur huit filons.
- **Vague 3** — recentrage sur le gisement qui score le plus haut : les obligations légales et l'argent
  des publics non développeurs : **200 idées** sur quatre filons.

Chaque idée tient en une ligne avec son utilisateur, sa douleur, sa fréquence et sa charge estimée en
jours-agent. Les doublons avec les sept projets déjà soumis au concours sont écartés à la génération.

## Avertissement

Ce dossier est public. Il expose une stratégie de concours à 12 000 autres participants. C'est un choix
assumé : la valeur est dans l'exécution, pas dans la liste.
