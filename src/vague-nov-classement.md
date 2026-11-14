# Classement de la vague du 13 novembre — deux juges indépendants

Les **104 idées** de la vague du 13 novembre ont été notées par deux agents qui ne se
sont pas lus et qui n'ont pas accès au même document :

- **Juge A — juge aveugle** : ne lit que `grille-100.md` (la grille du jury : Impact /25,
  Kiro /15, Design /20, Innovation /20, Présentation /20) et les fiches. Aucune attaque,
  aucun classement antérieur.
- **Juge B — juge strict** : lit `grille-notation.md` (Impact /25, Innovation /20,
  Faisabilité /20, Démonstrabilité /20, Potentiel Kiro /15, avec malus et bonus) **et**
  les 120 objections déjà portées contre le corpus dans `boucle-100.md`.

Chaque juge a rendu un top 15, un top 3 par lot et cinq défauts récurrents. Les deux
classements sont publiés ci-dessous **tels quels**, sans fusion préalable ni effacement.

## Ce que le croisement apprend

**22 idées ont été notées par les deux juges.** Leur désaccord porte sur le **niveau**,
leur accord sur l'**ordre** :

| Mesure | Valeur |
|---|---|
| Écart moyen de note (juge B − juge A) | **+8,45 points** |
| Corrélation de rang (ρ de Spearman, 22 idées) | **0,774** |
| Plus grand déplacement de rang | 10 places (**Doute** : 6ᵉ chez A, 16ᵉ chez B) |
| Idées au-dessus de 85 | **0** chez les deux juges |
| Moyenne du top du juge A | 69,7 (max 74) |
| Moyenne du top du juge B | 79,2 (max 84) |

Le juge à qui l'on demandait la plus grande sévérité a fini **8,45 points au-dessus** de
l'autre en moyenne. La raison n'est pas l'humeur du modèle, c'est la **grille** : le juge
aveugle notait sur les critères du jury (Design et Présentation, où un artefact manquant
coûte cher), le juge strict sur une grille où Faisabilité et Démontrabilité pèsent
davantage et où le périmètre « 8 jours-agent » est crédité. **Deux grilles différentes sur
des fiches identiques produisent un décalage systématique et un ordre proche.** C'est la
même leçon que la fiche Reprise jugée trois fois (45, 62, 78) : la note est un avis
conditionné par la grille, pas une mesure.

Ce qui ne bouge pas d'un juge à l'autre :

- **Aucune idée au-dessus de 85.** Le plafond de la boucle « 100/100 » tient sur un corpus
  de 104 fiches écrites, non sur les quatre seules fiches V2.
- **Le lot H est coiffé en dessous de tous les autres** (66–68 chez les deux juges) pour
  la même raison : ses chiffres sont écrits « N sur N », c'est-à-dire une promesse de
  mesure, pas une mesure.
- **Les trois mêmes lots dominent** (A, C, E) avec les mêmes idées en tête.

## Top 10 par moyenne des deux juges

| Rang | Moy. | Idée | Lot | Juge A | Juge B | Nerf |
|---|---|---|---|---|---|---|
| 1 | **78,0** | **Tampon** | A | 73 | 83 | Compare-and-swap au niveau du fichier : l'écrivain a-t-il *lu la même version*, et non seulement « écrit en premier ». `flock` et `git index.lock` ne répondent pas à cette question. |
| 1 | **78,0** | **Mirage** | E | 74 | 82 | Mute l'attendu et rejoue l'assertion sur des sorties déjà enregistrées : **zéro modèle appelé**, donc la démo ne peut pas échouer en direct. |
| 3 | **77,5** | **Suintement** | E | 71 | 84 | Audite l'éval et non l'entraînement, et **refuse de publier un score** (code sortie 3) — ce que ni `datatrove` ni `cleanlab` ne font. |
| 4 | **76,5** | **Dérobade** | C | 70 | 83 | Mesure la fenêtre de perte en exécutant deux clients concurrents : 214 écritures perdues sur 1 000, puis 0 avec le correctif. |
| 5 | **75,5** | **Contretemps** | C | 71 | 80 | Croise deux lignes du temps (migrations × déploiements) que ni Flyway ni Liquibase ne possèdent ; fenêtre rouge de 98 min à l'écran. |
| 5 | **75,5** | **Cicatrice** | A | 70 | 81 | Mine les échecs des journaux au lieu de les déclarer (`CLAUDE.md`, `AGENTS.md`) et publie son propre taux de rappel inutile. |
| 7 | **73,5** | **Périmètre** | E | 69 | 78 | Couverture de la surface *nommée* par les cas : une eval LLM n'exécute aucune ligne de production, donc `pytest-cov` est aveugle. |
| 7 | **73,5** | **Pendule** | A | 68 | 79 | Un rappel n'est compté que s'il est ancré sur un commit réel ; la re-litigation est détectée, ce qu'un ADR écrit à la main ne fait pas. |
| 9 | **73,0** | **Contreseing** | C | 69 | 77 | Journal d'ordres append-only : le CDC (Debezium) est aveugle à un producteur qui publie avant d'écrire. |
| 9 | **73,0** | **Colonne-vide** | B | 68 | 78 | Mesure l'inactivité (taux de remplissage, dernière écriture) là où `pg_stat_statements` mesure l'écart. |

Les dix premières sont toutes des **Frankenstein** ou des outils à **garantie
structurelle** (une propriété que le concurrent ne peut pas énoncer), jamais une
amélioration de degré. Aucune n'est un Costume Contest.

## Juge A — aveugle, grille du jury

| Rang | Note | Lot | Idée | Détail |
|---|---|---|---|---|
| 1 | 74 | E | **Mirage** | I:15 K:13 D:15 In:17 P:14 — boucle problème/garantie la plus serrée du corpus. |
| 2 | 73 | A | **Tampon** | I:14 K:13 D:15 In:16 P:15 — démo replay hors ligne impeccable ; « 2 sur 37 » reste revendiqué sans dépôt. |
| 3 | 71 | C | **Contretemps** | I:15 K:13 D:14 In:16 P:13 — garantie nette, mais v1 à 10 j contredit la friction nulle. |
| 4 | 71 | E | **Suintement** | I:15 K:13 D:14 In:16 P:13 — 34/200 annoncé sans artefact. |
| 5 | 70 | C | **Dérobade** | I:15 K:13 D:14 In:15 P:13 — chiffre affirmé, aucun corpus réel nommé. |
| 6 | 70 | D | **Doute** | I:15 K:12 D:14 In:16 P:13 — la démo repose sur un banc construit, pas livré. |
| 7 | 70 | A | **Cicatrice** | I:14 K:13 D:13 In:16 P:14 — « 7/12 » sur 30 sessions rejouées sans journal. |
| 8 | 69 | C | **Contreseing** | I:14 K:12 D:13 In:16 P:14 — 24 j de total pèsent sur la faisabilité. |
| 9 | 69 | B | **Remplissage** | I:15 K:12 D:14 In:15 P:13 — la fenêtre « 6 min 12 s » vient d'un rejouage non spécifié. |
| 10 | 69 | E | **Périmètre** | I:14 K:13 D:14 In:15 P:13 — la frontière « cas mentionne l'entrée » reste fragile. |
| 11 | 68 | D | **Éventail** | I:14 K:12 D:14 In:15 P:13 — 30 j et un serveur de test qui fabrique la variation visée. |
| 12 | 68 | D | **Bassin** | I:14 K:12 D:14 In:15 P:13 — le cimetière de sockets est du costume. |
| 13 | 68 | G | **Écran-vide** | I:14 K:12 D:14 In:15 P:13 — « 41 % de sortie » sans journal d'usage source. |
| 14 | 68 | B | **Colonne-vide** | I:14 K:12 D:14 In:15 P:13 — concurrents « pt-fingerprint, dejodupe » invérifiables. |
| 15 | 67 | H | **Palabre** | I:14 K:12 D:12 In:17 P:12 — meilleure innovation du lot, note coiffée par « N sur N ». |

## Juge B — strict, grille de notation + 120 objections

| Rang | Note | Lot | Idée | Détail |
|---|---|---|---|---|
| 1 | 84 | E | **Suintement** | I:21 In:17 F:16 D:17 K:13 — démo « aucun compte, aucun réseau, aucune clé ». |
| 2 | 83 | C | **Dérobade** | I:21 In:16 F:16 D:17 K:13 — avant/après mesuré, base embarquée dans le dépôt. |
| 3 | 83 | A | **Tampon** | I:20 In:17 F:16 D:17 K:13 — « 2 refusées sur 37, +1,4 ms » rejouable hors ligne. |
| 4 | 82 | E | **Mirage** | I:19 In:18 F:16 D:16 K:13 — rare dans le corpus : la démo ne peut pas échouer en direct. |
| 5 | 81 | A | **Cicatrice** | I:20 In:17 F:15 D:16 K:13 — la leçon est extraite, pas déclarée. |
| 6 | 80 | C | **Contretemps** | I:21 In:16 F:15 D:15 K:13 — le journal NDJSON doit exister chez l'utilisateur. |
| 7 | 79 | B | **Clé-absente** | I:20 In:15 F:16 D:15 K:13 — causalité (contrainte absente), pas nettoyage à posteriori. |
| 7 | 79 | A | **Pendule** | I:19 In:16 F:15 D:15 K:14 — normalisation des questions = angle mort assumé. |
| 9 | 78 | B | **Colonne-vide** | I:20 In:15 F:16 D:14 K:13 — la démo v1 tourne sans base. |
| 9 | 78 | E | **Périmètre** | I:19 In:16 F:15 D:15 K:13 — « 47 entrées sur 152 (31 %) » frappe juste. |
| 11 | 77 | C | **Contreseing** | I:19 In:16 F:14 D:15 K:13 — deux brokers simulés en local, point fragile. |
| 11 | 77 | F | **Home** | I:20 In:13 F:16 D:14 K:11 (+5 non-dev, imprimable) — innovation d'agrégation. |
| 13 | 76 | A | **Feinte** | I:19 In:15 F:17 D:14 K:11 — plus petit noyau du corpus, portée étroite. |
| 13 | 76 | D | **Éventail** | I:19 In:16 F:14 D:15 K:12 — la v1 doit tenir sans le mode multi-point. |
| 15 | 75 | C | **Injoignable** | I:19 In:15 F:14 D:15 K:12 — la discipline d'acquittement prouvée par panne. |

## Top 3 par lot, chez chaque juge

| Lot | Juge A | Juge B |
|---|---|---|
| A — agent de code | Tampon 73 · Cicatrice 70 · Pendule 68 | Tampon 83 · Cicatrice 81 · Pendule 79 |
| B — donnée qui change de forme | Remplissage 69 · Colonne-vide 68 · Clé-absente 66 | Clé-absente 79 · Colonne-vide 78 · Remplissage 76 |
| C — le temps | Contretemps 71 · Dérobade 70 · Contreseing 69 | Dérobade 83 · Contretemps 80 · Contreseing 77 |
| D — le réseau | Doute 70 · Éventail 68 · Bassin 68 | Éventail 76 · Doute 74 · Rafale 72 |
| E — données des modèles | Mirage 74 · Suintement 71 · Périmètre 69 | Suintement 84 · Mirage 82 · Périmètre 78 |
| F — le poste | Home 65 · Relais 63 · Secret-partagé 62 | Home 77 · Secret-partagé 73 · Chemin-mort 72 |
| G — l'interface | Écran-vide 68 · Double-clic 63 · Perte-texte 62 | Écran-vide 75 · Double-clic 72 · Perte-texte 71 |
| H — vie d'équipe | Palabre 67 · Rumeur 66 · Quinzaine 64 | Rumeur 68 · Palabre 67 · Quinzaine 66 |

Trois lots se détachent chez **les deux** juges : A, C, E. Deux s'effondrent chez **les
deux** : F et G (aucune idée au-dessus de 77, parce que 12 idées sur 13 y sont sans fiche
détaillée) et H (coiffé à 68 par le chiffre « N sur N »).

## Les cinq défauts récurrents, comptés dans le fichier

Les deux juges ont listé cinq défauts chacun. Recoupés et **comptés à la main sur les 104
fiches** (et non estimés par le juge) :

| Défaut | Idées touchées | Preuve |
|---|---|---|
| Chiffre écrit « N sur N » (promesse de mesure, pas une mesure) | **16** | les **13 du lot H** (tous), plus Bobine (A), Éventail et Rafale (D) |
| Fiche sans « chiffre mesuré / démo 30 s / concurrent nommé » | **84 sur 104** | 20 fiches détaillées seulement ; lots F et G n'en ont **qu'une** chacun, non trois |
| Périmètre total ≥ 30 jours-agent | **13** | les 13 du lot D — la v1 est crédible, le chiffre promis arrive au mois 2 |
| v1 ≥ 9 jours-agent (contre la promesse « 8 jours ») | **20** | concentrée sur les lots C et D |
| Métaphore décorative (retirez-la, l'outil n'est ni meilleur ni différent) | **~18 sur 19** | le juge B qualifie presque tout **Costume Contest** — l'idée en contient 19 : Perfo, Reliquaire, Bassin, Ballon, Ronde, Ouroboros, Orphelin, Caveau, Fil rouge, Post-it, Entre-deux, Doublure… Malus −10 appliqué. |

Et **un défaut du dossier lui-même**, trouvé par le juge strict : la page annonce que
« Bobine » a été retirée de la liste comme renommage de *Rejeu* — **elle y est toujours**
(lot A, idée 05). Le juge B lui applique le malus −20 de doublon ; le juge A ne la
mentionne pas dans son top. La contradiction est corrigée dans la page d'origine :
l'idée est conservée et marquée comme doublon assumé de *Rejeu*, avec le malus écrit en
clair, au lieu d'être annoncée retirée.

## Ce que ça change pour la suite

- **Rien au podium** : les trois mêmes idées (Tampon, Mirage, Suintement) gagnent chez les
  deux juges, avec ou sans accès aux 120 objections. Le classement devs antérieur
  (Chemin-fantôme 95 → 59 chez un juge) ne se répète pas ici : les fiches de cette vague
  étaient déjà écrites contre la grille, pas contre l'enthousiasme.
- **Le levier le plus rentable n'est pas une nouvelle idée** : 84 fiches sur 104 n'ont ni
  démo de 30 s, ni concurrent nommé, ni limite honnête. Les écrire ferait bouger plus de
  notes que n'importe quel ajout d'idées.
- **Le lot H ne sera pas construit tel quel** : ses 13 chiffres sont des « N sur N ». Avant
  d'en bâtir un, il faut un dépôt réel à mesurer — c'est du code, pas de la fiche.
