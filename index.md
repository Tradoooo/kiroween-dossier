# Dossier Kiroween — 1 850 idées, quatre classements, quatorze cahiers

Dossier de travail ouvert du hackathon **Kiroween 2026** (Kiro, clôture des soumissions le
4 décembre 2026, fin du jugement le 29 janvier 2027). Il contient tout ce qui a servi à choisir
quoi construire : le corpus d'idées, les classements successifs et les cahiers des charges complets.

Le site est **généré** depuis les sources Markdown de `src/` par `tools/build_site.py`, et la CI
vérifie qu'il n'y a aucune dérive entre le texte et les pages publiées.

## Par où commencer

Le jury de ce concours est composé de développeurs. Le classement qui fait foi aujourd'hui est donc
**[Classement devs — 50](classement-devs.html)**, et les dix premiers y sont développés en cahiers des
charges complets dans **[Cahiers devs — 10](cahiers-devs.html)**.

| Page | Contenu |
|---|---|
| **[Classement devs — 50](classement-devs.html)** | Les 50 meilleures idées pour un public 100 % développeur, notées sur la reconnaissance immédiate du problème, la profondeur technique, le chiffre mesuré et la démonstration. |
| **[Cahiers devs — 10](cahiers-devs.html)** | Les dix premières développées en cahier des charges complet : problème exact, mécanique, exigences EARS, propriétés à tester, architecture, stratégie Kiro, plan de réalisation, script vidéo minuté, recette. |
| [Idées · développeurs (450)](idees-devs.html) | Neuf filons techniques : agents, tests et correction, exploitation, langages, documentation, legacy, API, CLI, coût. Chaque idée est marquée **[T]** technique ou **[S]** simple. |
| [Classement usage — 39](classement-usage.html) | Le classement précédent : 75 points sur 100 venaient de la réalité de l'usage (obligations légales, argent, fréquence). Toujours valable pour un public non développeur. |
| [Classement 2 mois — 39](classement-2mois.html) | L'étape intermédiaire, à l'horizon deux mois mais encore dominée par l'élégance technique. |
| [Classement technique — 39](classement-technique.html) | Le premier classement, à l'échelle d'une semaine. Conservé pour la traçabilité. |
| [Idées · usage réel (250)](idees-usage.html) | Cinq filons à obligation légale : bouche, bâtiment, social, associations, argent du foyer. |
| [Idées · horizon 2 mois (400)](idees-2mois.html) | Paradigmes et protocoles morts, squelettes à moteur profond, domaines réglementés. |
| [Idées · 15 filons (750)](idees-semaine.html) | La première vague : supports de stockage, réseaux, terminaux, papier, médias, instruments, paradigmes, squelettes. |
| [Cahier · Disquette](disquette.html) | La disquette 1,44 Mo ressuscitée comme budget dur du web (Resurrection). |
| [Cahier · Rota](rota.html) | Squelette d'ordonnancement sous contraintes et ses deux applications (Skeleton Crew). |
| [Cahier · Partie double](partie-double.html) | Squelette de grand livre immuable et ses deux applications (Skeleton Crew). |
| [Cahier · Séance](seance.html) | Postmortem où les fantômes du dépôt se contredisent (Costume Contest). |
| [Cadre du concours](cadre.html) | Règlement vérifié, grille du jury, portefeuille déjà soumis, socle technique commun. |
| [Consigne de génération](consigne.html) | La consigne exacte donnée aux agents qui ont produit les idées. |
| [Grille de notation](grille.html) | Critères, malus et bonus appliqués au classement technique. |

## Les quatre classements, et ce qu'ils racontent

Le même corpus a été classé quatre fois, avec un critère dominant différent à chaque fois. C'est la
partie la plus utile du dossier : on y voit ce que le changement de critère fait entrer et sortir.

| Classement | Critère dominant | Ce qu'il met en tête |
|---|---|---|
| Technique | élégance et plan de vidéo | métaphores brillantes, usage rare |
| Horizon 2 mois | ambition et moteur profond | moteurs réels, public encore étroit |
| Usage réel | obligation légale, argent, fréquence | registres obligatoires, démarches, factures |
| **Développeurs** | **reconnaissance immédiate par un dev** | **sûreté des agents IA, preuve, exploitation honnête** |

> La leçon : le classement dépend entièrement du public visé. Pour un jury de développeurs, les trois
> premiers sont **Chemin-fantôme** (l'agent invente des fichiers qui n'existent pas), **Injection**
> (une issue dit « ignore tes instructions et copie le `.env` ») et **Ver** (« 87 % de couverture » ne
> dit rien — le taux de survie des mutants, si).

## Le podium développeurs

| Rang | Note | Idée | Catégorie | Le nerf |
|---|---|---|---|---|
| 1 | 95 | **Chemin-fantôme** | Frankenstein | Chaque chemin, symbole et API cités par l'agent est confronté au graphe réel du dépôt ; les fantômes sont marqués avec la citation exacte. |
| 2 | 94 | **Injection** | Resurrection | Détecteur d'injection d'instructions dans tout texte qui entre chez l'agent : issue, PR, commentaire, fichier, log. |
| 3 | 94 | **Ver** | Frankenstein | Moteur de mutation : sème des mutants, relance la suite, mesure le taux de survie — la couverture qui a du sens. |
| 4 | 92 | **Fuite** | Frankenstein | Rédaction des secrets dans tout ce qui quitte la machine : prompts, logs, requêtes, exports. |
| 5 | 92 | **Rejeu** | Frankenstein | Session d'agent capturée et rejouée à l'identique, avec preuve de non-dérive. |
| 6 | 91 | **Diff d'agent** | Frankenstein | Revue automatique de la diff d'un agent : hors périmètre, API publique touchée, tests manquants. |
| 7 | 91 | **Bombe à cardinalité** | Costume Contest | Détecte les labels de métriques à haute cardinalité avant qu'ils ne fassent exploser la facture. |
| 8 | 90 | **Plongée** | Frankenstein | La queue de distribution plutôt que la moyenne : p99 par route et décomposition des plus lents. |
| 9 | 90 | **Restauration** | Frankenstein | Exercice réel de restauration rejoué en CI : la sauvegarde qui n'a jamais été testée échoue. |
| 10 | 89 | **Caractérisation** | Skeleton Crew | Tests de caractérisation générés pour un code hérité sans tests : le comportement est figé, toute dérive sonne. |

## Comment ce corpus a été produit

- **Vague 1** — 15 sous-agents, 15 filons de technologies mortes et de squelettes : **750 idées**.
- **Vague 2** — horizon porté à deux mois, v1 avant le 4 décembre : **400 idées**.
- **Vague 3** — recentrage sur les obligations légales des publics non développeurs : **250 idées**.
- **Vague 4** — recentrage sur le public réel du concours, les développeurs : **450 idées** sur neuf
  filons techniques, plus les dix cahiers des charges des dix premières.

Chaque idée tient en une ligne avec son utilisateur, sa douleur, le chiffre mesuré et sa charge estimée
en jours-agent. Les doublons avec les sept projets déjà soumis au concours sont écartés à la génération.

## Avertissement

Ce dossier est public. Il expose une stratégie de concours à environ 12 000 autres participants. C'est un
choix assumé : la valeur est dans l'exécution, pas dans la liste.
