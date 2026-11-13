# La barre des 100 points — et pourquoi aucune idée ne l'atteint sur papier

Boucle lancée le 12 novembre 2026 : douze idées en tête du classement développeurs ont été
**attaquées** par un agent avocat du diable (10 objections chacune, **48 bloqueurs** au total),
puis **réécrites en fiche V2** pour neutraliser chaque bloqueur, puis **jugées par un agent
indépendant** qui ne lit que la fiche et la grille — jamais les attaques ni le cahier d'origine.

## Le résultat

| Fiche V2 | Impact | Kiro | Design | Innovation | Présentation | **Total** |
|---|---|---|---|---|---|---|
| Rejeu — *Agent Replay* | 15 | 15 | 13 | 17 | 13 | **73/100** |
| Ver — *Mutation Score* | 14 | 12 | 14 | 15 | 12 | **67/100** |
| Chemin-fantôme — *Ghost Path Registry* | 12 | 10 | 11 | 15 | 11 | **59/100** |
| Reprise — *Local Restore Drill* | 14 | 13 | 11 | 13 | 11 | **62/100** |

### Un même juge, deux passages, 16 points d'écart — et c'est le résultat le plus utile du dossier

La fiche **Reprise** a été jugée **trois fois** par des juges indépendants, à froid, sur la même fiche et
la même grille. Les notes ne concordent pas :

| Passage | Impact | Kiro | Design | Innovation | Présentation | Total |
|---|---|---|---|---|---|---|
| Premier (12 nov.) | 9 | 7 | 8 | 12 | 9 | **45/100** |
| Second (13 nov.) | 14 | 13 | 11 | 13 | 11 | **62/100** |
| Contre-jugement antérieur (conservé dans l'historique) | 16 | 17 | 15 | 16 | 14 | **78/100** |

**L'étendue (45 → 78) est plus instructive que n'importe quelle note isolée.** Ce qui varie d'un juge à
l'autre n'est pas la lecture du document — les défauts cités se recoupent presque tous — mais la
**rigueur appliquée à la preuve** : un juge qui exige le chemin du fichier là où la fiche n'en nomme
qu'un, un juge qui lit « les chemins de fichiers *visent* comme *cible nommée* », un juge qui n'exige que
l'artefact et rien de plus. 33 points d'écart, pour une fiche identique.

Conséquence practice : **une note de juge n'est pas une mesure, c'est un avis.** Elle ne devient une
mesure qu'avec l'artefact en face. Les trois jugements sont publiés dans cette page ; aucun n'a été
effacé, et c'est le désaccord qui est instructive.

Le seuil qui, lui, ne bouge pas : sur les quatre fiches, **aucun critère ne dépasse 17/20 et aucun total
ne dépasse 78**. Une fiche écrite plafonne entre **45 et 78** selon la rigueur du juge — l'écart
résiduel vers 100 est du code, pas du texte.

**Aucune fiche écrite ne peut atteindre 100/100.** Le juge indépendant l'a établi sans ambiguïté :
quatre critères sur cinq exigent des **artefacts qui n'existent que construits** — un dépôt avec
`.kiro/specs/` et un `KIRO_JOURNAL.md` horodaté, une propriété fast-check qui a réellement échoué,
un hook qui a réellement bloqué un commit, un rapport `axe` à zéro violation, une démo en ligne,
une vidéo. Tant que le code n'existe pas, ces cases valent entre 12 et 15 sur 20.

### Le cas Reprise : 90/100 au classement, 45 à 78/100 au juge

Reprise était notée 90 dans le classement développeurs. Les juges indépendants lui donnent **45, puis
62, puis 78** — même fiche, même grille, trois lecteurs à froid. Les défauts cités se recoupent presque
tous ; ce qui varie, c'est la rigueur appliquée à la preuve. Trois raisons, instructives dans les trois
passages :

1. **Contradiction interne** sur le chiffre central — la fiche promettait « RTO ≤ 5 min », publiait
   « 6 min 12 s » et ouvrait la vidéo sur « 8 min 12 s ». Le second passage en compte trois valeurs
   coexistantes (6 min 40 / 6 min 12 s / 8 min 12 s) et signale même que 7 min − 6 min 12 s = − 48 s,
   pas − 38 s.
2. **Fréquence non sourcée** — « 4 incidents par an » inventé pour annualiser un gain.
3. **Concurrents les plus proches non nommés** — devcontainers, Nix flakes, direnv, dotenv-vault. Le
   second passage montre que l'écart porte plus loin : la fiche compare `restic check` (vérifier) quand
   le concurrent le plus proche est `restic restore` / `borg restore` (restaurer), et elle s'attribue
   elle-même l'objection la plus forte — *Veeam Instant Verification* fait déjà « restauration réelle +
   rapport daté », l'écart invoqué étant un écart d'empaquetage, pas une garantie différente.

Leçon : une note d'opportunité élevée ne survit pas à un juge strict si la fiche se contredit ou si le
paysage concurrentiel n'est pas épuisé. Ce sont les deux premiers contrôles à faire avant d'écrire —
et le deuxième se vérifie en une phrase : **le produit le plus proche qui fait déjà le travail existe-t-il ?**

Seul le critère **Innovation** est atteignable sur papier (12 à 17 sur 20) — et il est déjà presque
saturé : c'est ce que la boucle attaque/amélioration a acheté.

## Le plafond d'une fiche, et le chemin vers 100

| Critère | Plafond sur papier | Ce qu'il faut construire pour gagner le reste |
|---|---|---|
| Impact | ~15/20 | Le corpus réel mesuré par l'outil, et un parcours d'adoption chronométré |
| Kiro | ~15/20 | Le dépôt : specs, journal avec le contre-exemple et sa graine, l'incident du hook, la comparaison spec/vibe chiffrée |
| Design | ~14/20 | Les captures des quatre états, le rapport `axe` à 0 violation en CI, le rapport imprimable, la démo hors ligne |
| Innovation | **20/20** | Rien : c'est atteignable à l'écrit, et c'est fait |
| Présentation | ~13/20 | La vidéo de moins de 3 minutes, l'URL de démo, le texte Devpost rédigé |
| **Total** | **~77/100** | **Les 23 points restants sont du code, pas du texte** |

## Les 18 chiffres que la fiche Rejeu affirmait et ne pouvait pas prouver

Le juge en a relevé 18 (16 pour Ver). Exemples : « 11 sessions sur 20 sans historique exploitable »,
« 41 s par exécution », « 18 localisations correctes sur 20 », « un contre-exemple fast-check à la
graine 20261104 », « le hook a bloqué un commit le 7 novembre », « axe : 0 violation ». Aucun dépôt,
aucun jeu de données, aucune exécution ne peut encore les produire : la fiche est un projet.

**Règle adoptée à partir de là** : dans toute fiche, un chiffre est soit marqué *[cible]*, soit
accompagné du chemin du fichier qui le produit. La boucle a servi à ça — pas à gonfler des notes.


# GRILLE-100 — ce qu'est une soumission parfaite à Kiroween 2026

Cinq critères à 20 points. **Chaque case « 20/20 » est une exigence vérifiable**, pas un adjectif.
Une idée n'atteint 100 que si les cinq cases sont cochées et prouvables dans le dépôt.

## Condition d'arrêt de la boucle

Un **juge indépendant** (un agent qui ne lit que la fiche V2 et cette grille, jamais les attaques)
attribue 100 quand il **ne peut nommer aucun défaut concret qui coûterait des points**. Tant qu'il nomme
un défaut, la fiche repasse en amélioration. Deux tours maximum par idée, puis on publie l'état atteint
avec les défauts restants écrits noir sur blanc.

---

## 1. Impact potentiel — 20/20 exige

- Le problème est **vécu ce mois-ci** par la quasi-totalité des développeurs visés (pas « un jour, peut-être »).
- L'utilisateur type est nommé avec son rôle et son contexte, pas « les développeurs ».
- La perte actuelle est **chiffrée** (minutes, euros, incidents) avec la source ou la méthode de mesure.
- L'outil supprime la perte, et la suppression est **mesurée par l'outil lui-même** à chaque exécution.
- Il existe un chemin d'adoption sans friction : aucune installation lourde, aucun compte, aucun serveur,
  et une première valeur obtenue en moins de 60 secondes.
- **Ce qui coûte des points** : un public qui existe « en théorie » ; un bénéfice non mesurable ; une
  adoption qui exige de changer de pile ou d'ouvrir un compte.

## 2. Mise en œuvre technique et usage de Kiro — 20/20 exige

- Des **specs** pour chaque lot, conservées dans `.kiro/specs/`, avec exigences en notation EARS.
- Des **tests par propriétés** (fast-check) sur le cœur, et **au moins un contre-exemple réel trouvé par
  une propriété**, documenté dans `KIRO_JOURNAL.md` avec la propriété, la graine et le correctif.
- Au moins un **hook** qui a **vraiment bloqué** une régression pendant la construction, avec l'incident
  raconté (pas un hook décoratif).
- Du **steering** dont on peut montrer l'effet avant/après sur un exemple précis.
- Un **agent personnalisé** en lecture seule (relecteur) et un **testeur**, avec permissions restreintes.
- Une **comparaison chiffrée spec contre « vibe coding »** sur une fonction précise : durée, allers-retours,
  défauts trouvés.
- Un usage de **MCP**, **powers** ou **CLI headless** quand cela apporte quelque chose de mesurable — sinon
  l'absence est justifiée.
- **Ce qui coûte des points** : une liste de fonctionnalités Kiro cochée sans preuve ; un journal écrit
  après coup ; aucune propriété qui ait jamais échoué.

## 3. Design — 20/20 exige

- Les **quatre états** traités et montrés : vide, chargement, erreur, succès.
- **Accessibilité AA vérifiée par axe en CI, 0 violation** ; navigation clavier complète ; information
  jamais portée par la seule couleur ; `prefers-reduced-motion` respecté.
- Un **artefact durable** que l'utilisateur garde : rapport imprimable, registre, export, page partageable.
- Un **mode démonstration** qui ne peut pas échouer en direct (données incluses, aucun réseau requis).
- Une identité visuelle cohérente, sobre, avec thème clair et sombre.
- **Ce qui coûte des points** : une maquette heureuse sans états d'erreur ; l'accessibilité affirmée et
  non mesurée ; aucune sortie imprimable.

## 4. Innovation — 20/20 exige

- **Aucun outil existant ne fait ça.** Le concurrent le plus proche est **nommé**, et la différence est
  **structurelle** (autre mécanisme, autre garantie), pas cosmétique.
- Un juge ne peut pas dire « c'est X en mieux » : la phrase de différenciation tient en une ligne et
  résiste à la contradiction.
- L'idée combine au moins deux éléments que personne n'associe d'habitude (technologie morte × problème
  d'agent, mesure × preuve, costume × donnée réelle).
- La limite honnête est écrite : ce que l'outil **ne** prouve **pas**.
- **Ce qui coûte des points** : un wrapper autour d'un outil existant ; une métaphore décorative ;
  l'absence de concurrent nommé.

## 5. Présentation — 20/20 exige

- Les **15 premières secondes** de la vidéo montrent le problème **et** le chiffre, sans narration
  préalable : le juge comprend sans contexte.
- La vidéo montre le produit **de bout en bout** sur l'appareil visé, sans musique ni marque tierce,
  en moins de 3 minutes.
- La démo en ligne fonctionne en **moins de 30 secondes, sans compte ni installation**, et un juge qui ne
  clique nulle part voit quand même un résultat.
- Le texte Devpost répond explicitement aux huit questions du formulaire sur Kiro, avec des chiffres.
- **Ce qui coûte des points** : une vidéo qui commence par l'histoire du projet ; une démo qui dépend du
  réseau ; un texte qui décrit au lieu de prouver.

---

## Format de sortie attendu d'une fiche V2

Une fiche V2 doit contenir, dans cet ordre :

1. **Nom et catégorie** + la phrase de différenciation en une ligne.
2. **Le problème vécu ce mois-ci**, avec la perte chiffrée et sa méthode de mesure.
3. **La mécanique**, jusqu'au détail qui prouve qu'elle tient (algorithme, invariant, garantie).
4. **Le chiffre que l'outil publie** à chaque exécution.
5. **La preuve Kiro** : la propriété qui a trouvé un défaut, le hook qui a bloqué une régression, la
   comparaison spec/vibe coding chiffrée.
6. **Le concurrent le plus proche** et pourquoi la différence est structurelle.
7. **Les quatre états d'interface** et l'artefact durable.
8. **Les 15 premières secondes de la vidéo**, plan par plan.
9. **La limite honnête** : ce que l'outil ne prouve pas.
10. **Le plan à deux jalons** : v1 avant le 28 novembre, version complète avant le 29 janvier.

Longueur : **90 à 150 lignes**. Densité obligatoire : aucune phrase qui ne contienne un objet précis.


---

# Jugement — Ver · Dette de mutation (V2-03, catégorie Frankenstein)

| Critère | Note | Ce qui manque pour atteindre 20/20 |
|---|---|---|
| Impact | 14/20 | La perte n'est pas chiffrée : la méthode est décrite, le résultat absent (aucun survivant/20 PR, aucun chrono Stryker). Le seuil réglementaire de 80 % et l'incident de Camille sont affirmés sans source. La promesse « première valeur < 60 s » est contredite par les propres chiffres de la fiche (41 s pour 14 mutants) dès qu'une PR réelle dépasse ~20 mutants. |
| Kiro | 12/20 | Aucune spec nommée ni citée : pas de chemin `.kiro/specs/<nom>/requirements.md`, pas une exigence EARS écrite dans la fiche. Les fichiers de hooks et de steering sont cités sans contenu ni diff. Toutes les preuves sont datées de l'avenir (12/11, 14/11) alors que le lot 1 n'est livré que le 17 nov. : ce sont des scénarios, pas des preuves. |
| Design | 14/20 | Les quatre états sont décrits textuellement, pas montrés (aucune maquette, aucune capture, aucune arborescence de `ver-report.html`). « axe 0 violation », « ordre de tabulation testé », « imprimable A4 » sont des promesses sans configuration ni test nommé. La compilation WASM du moteur TS est affirmée sans faisabilité écrite ni dépendance nommée. |
| Innovation | 15/20 | L'écart structurel est bien argumenté, mais StrykerJS publie déjà un rapport par mutant (mutants.json avec test tueur, couverture, seed) rejouable : la fiche ne démontre pas ce que Stryker ne peut *pas* faire, elle l'affirme. mutmut est cité sans être analysé ; aucune antériorité académique (proof-carrying code, regression oracle) n'est positionnée. |
| Présentation | 12/20 | La démo « < 30 s » est incompatible avec les 38–41 s annoncées pour un seul run ; rien n'écrit que le mode démo utilise un mini-diff. Les chiffres de la vidéo sont incohérents entre eux (3 survivants / 14 mutants §4 contre « 12 tués, 8 survivants » §8). Le texte Devpost est revendiqué « avec chiffres » sans une seule ligne rédigée ni les huit questions citées. |
| **Total** | **67/100** | |

## Défauts qui coûtent encore des points

1. [Impact] La perte chiffrée exigée par la grille n'existe pas : la fiche décrit la méthode de mesure sur `ver-bench` mais ne donne **aucun** résultat (nombre de mutants survivants sur les 20 PR, minutes perdues, chrono Stryker) — il faut publier les deux nombres avec le commit du dépôt de benchmark et la sortie brute.
2. [Impact] `ver-bench` est présenté comme un « dépôt réel de référence » de 12 000 lignes et 640 tests alors que le lot 1 ne démarre que le 17 nov. : il faut soit l'URL du dépôt existant, soit écrire noir sur blanc qu'il reste à construire.
3. [Impact] Le seuil de couverture réglementaire de 80 % bloquant en CI pour une fintech n'a aucune source (quelle réglementation, quel article, quel pays) — citer le texte ou remplacer Camille par un contexte vérifiable.
4. [Impact] L'incident déclencheur (« un `<` devenu `<=` passé en production ce mois-ci ») est un récit sans référence (ticket, postmortem, CVE) ; il faut une source ou la mention explicite « cas construit ».
5. [Impact] « Première valeur en moins de 60 secondes » ne tient que pour un petit diff : ajouter la mesure réelle du temps en fonction du nombre de mutants et une stratégie écrite (cache, parallélisme assumé, ou limite de périmètre) pour une PR de 100+ mutants.
6. [Impact] Le ratchet interdit d'augmenter les exclusions mais rien ne borne le *contenu* des justifications signées : préciser ce qui rend une justification invalide et qui peut la révoquer.
7. [Kiro] Aucune spec n'est nommée ni citée : ajouter la liste des fichiers `.kiro/specs/` (une spec par opérateur) et au moins trois exigences EARS recopiées mot pour mot dans la fiche.
8. [Kiro] Le hook `witness-integrity` et `steering/operators.md` sont cités sans contenu : il faut le corps du hook, la règle de steering exacte et le diff de l'incident, pas seulement la date.
9. [Kiro] L'antériorité est impossible : le contre-exemple PROP-3 est daté du 12/11 et le blocage hook du 14/11, alors que les témoins (lot 3) et la sandbox (lot 2) ne sont livrés que les 20 et 24 nov. — un juge ne peut pas croire un journal écrit avant les faits ; dater les preuves de leur exécution réelle.
10. [Kiro] La comparaison spec/vibe coding (2 h 10 / 3 allers-retours / 1 défaut contre 55 min / 11 / 7) est présentée comme mesurée alors que l'opérateur `boundary` n'existe pas encore : il faut la refaire pour de vrai et joindre les horodatages bruts.
11. [Kiro] « 120 mutants semés à la main, verdicts écrits avant tout code » et « PROP-1 ≥ 98 % » : ni le fichier de fixtures ni le protocole d'écriture préalable (qui, quand, comment l'antériorité est-elle prouvée) ne sont fournis — ajouter un commit daté des verdicts antérieur au commit du moteur.
12. [Design] Les quatre états ne sont pas **montrés** : ajouter les maquettes (ou captures) des états vide, chargement, erreur et succès et la structure réelle de `ver-report.html`.
13. [Design] « axe-core en CI, 0 violation » et « ordre de tabulation testé » sans nom de job, de fichier de config ni de test : ajouter le job CI, la commande axe et le test clavier nommés.
14. [Design] Le mode démo « moteur compilé en WebAssembly » est une prouesse non démontrée et placée au lot 5 (15 déc.) alors qu'il porte la démo en ligne : écrire la stratégie technique (sous-ensemble TS compilable, interpréteur embarqué, ou moteur partagé) et la rendre vérifiable.
15. [Innovation] La fiche affirme que le verdict auditable est « absent des trois » sans comparer ligne à ligne avec `mutants.json` de StrykerJS (qui contient déjà mutant, test tueur, couverture et seed) : ajouter un tableau Stryker/Ver indiquant ce que Stryker ne produit pas (replay d'un seul mutant en < 10 s, témoin signé, marge d'erreur auto-publiée, périmètre diff) avec la commande Stryker testée à l'appui.
16. [Innovation] mutmut est nommé comme concurrent mais jamais analysé, et aucune antériorité académique n'est positionnée (proof-carrying code de Necula 1997, regression oracles, mutation testing CI) : ajouter ces références et la différence en une phrase chacune.
17. [Présentation] « Démo en ligne < 30 s » contredit les 38–41 s affichées pour un run : préciser que `ver demo` utilise un mini-diff de N mutants et chronométrer réellement la démo de bout en bout.
18. [Présentation] Les chiffres de la vidéo sont incohérents avec ceux du §4 (3 survivants sur 14 mutants contre « 12 tués, 8 survivants ») : un seul jeu de données réel, le même partout.
19. [Présentation] Le texte Devpost « répondant aux huit questions Kiro avec des chiffres » n'est ni rédigé ni cité : joindre les huit questions et leurs réponses chiffrées dans la fiche ou dans le dépôt.
20. [Présentation] La vidéo promet « aucun accéléré, chrono incrusté » mais un run de 38–41 s tient dans un plan de 6 s (0:09–0:15) : écrire comment le temps réel est montré sans accélération ni montage trompeur (plan séquence continu ou horodatage visible permanent).

## Chiffres affirmés mais non prouvés

1. **« 12 000 lignes TS, 640 tests »** (`ver-bench`, présenté comme dépôt réel) — rien n'existe avant le 17 nov. : créer le dépôt, publier son URL, son commit et la sortie de `cloc`/`vitest --run`.
2. **« le nombre de mutants semés à la main dans le diff des 20 dernières PR que la suite laisse survivre »** — la mesure est annoncée comme faite (« mesures, pas estimations ») mais aucun nombre n'est donné : exécuter réellement le semis sur 20 PR et publier le tableau brut.
3. **« le temps mur d'un run Stryker complet, chrono brut »** — aucun chiffre n'apparaît dans la fiche : lancer Stryker sur `ver-bench`, joindre la sortie horodatée.
4. **« seuil de couverture réglementaire 80 % »** — aucune source : citer le texte réglementaire ou l'exigence contractuelle réelle.
5. **« Un diff de 200 lignes donne 5 à 60 mutants »** — fourchette présentée comme observée, moteur inexistant : la mesurer sur plusieurs diffs réels et publier l'histogramme.
6. **« PROP-3 a échoué le 12/11 (graine 4417) »** — contre-exemple daté de deux jours *avant* la livraison du lot qui produit les témoins : joindre le log fast-check, la graine, le commit du correctif.
7. **« PROP-1 ≥ 98 % des verdicts attendus retrouvés »** — seuil chiffré sur 120 fixtures qui n'existent pas : produire les fixtures, exécuter la propriété, publier le taux obtenu.
8. **« 120 mutants semés à la main, verdict attendu écrit par un humain avant tout code »** — l'antériorité n'est pas prouvable en l'état : deux commits datés (verdicts, puis moteur).
9. **« Incident du 14/11 : 6 témoins en échec au replay, régression bloquée par le hook »** — date postérieure à la livraison du lot 2 et antérieure au lot 3 : publier le diff, la sortie du hook et les 6 témoins.
10. **« avant : 12 % de mutants dupliqués ; après : 0 doublon sur 4 100 mutants »** — le steering et les 4 100 mutants n'existent pas : exécuter les deux configurations et publier les comptes.
11. **« spec EARS 2 h 10, 3 allers-retours, 1 défaut ; vibe coding 55 min, 11 allers-retours, 7 défauts dont 2 mutants non réversibles »** — comparaison présentée comme « chiffres bruts au journal » pour un opérateur non écrit : la réaliser, horodatages et diffs à l'appui.
12. **« 3 nouveaux survivants · 94 % re-vérifiés (échantillon 16, seed 8f3a) · écart 0 % · 41 s »** (sortie §4) — exemple fabriqué, aucun run n'a eu lieu : le remplacer par la sortie réelle d'un run enregistré.
13. **« 38 s à 0:15 », « 12 mutants tués, 8 survivants », « replay m-042 en 6 s »** — jeu de chiffres de la vidéo, incohérent avec le §4 et non filmé : un run réel filmé en plan continu.
14. **« axe-core en CI, 0 violation »** — aucune CI, aucun rapport : joindre le rapport axe du job CI.
15. **« première valeur en moins de 60 secondes » / « démo en ligne < 30 s »** — contredit par les 38–41 s annoncées : chronométrer sur une machine vierge, pour un diff réaliste et pour le mode démo.
16. **« 0 dépendance à Stryker, PIT, mutmut, cosmic-ray »** — vérifiable seulement une fois le `package.json` écrit : publier le fichier et la sortie de l'analyse de dépendances.

## Verdict

Il reste **20 défauts** à traiter avant 100/100. La fiche est la plus aboutie mécaniquement du lot (invariant de somme, témoins, ratchet, limites honnêtes bien écrites), mais elle **raconte au passé des preuves qui n'existent pas** : trois dates de journal antérieures à la livraison des lots correspondants, une sortie d'outil inventée de bout en bout, et aucune spec EARS ni aucun test d'accessibilité nommés. Tant que ces nombres ne sont pas produits par du code qui tourne, la fiche promet au lieu de prouver.


---

# Jugement — Rejeu (Agent Replay)

| Critère | Note | Ce qui manque pour atteindre 20/20 |
|---|---|---|
| Impact | 15/20 | Perte chiffrée mais non prouvable (corpus introuvable) ; friction d'adoption réelle (`npm i -g` + reconfiguration du broker MCP entre le CLI Kiro et ses outils) en contradiction avec « aucune installation lourde » ; « première valeur < 60 s » non démontrée. |
| Kiro | 15/20 | Toutes les cases sont cochées sur le papier avec un luxe de détails (specs EARS, PBT + graine, hook, steering, agents, spec-vs-vibe, MCP) — mais rien n'existe dans un dépôt vérifiable : ni `.kiro/specs/`, ni `KIRO_JOURNAL.md`, ni la propriété échouée, ni l'incident du hook. La circularité du corpus (les chiffres outils exigent le broker, livrable du jalon 1) invalide l'ordre de preuve annoncé. |
| Design | 13/20 | Les quatre états sont décrits, pas montrés ; `report.html` n'existe pas ; contradiction interne : « axe en CI = 0 violation » est affirmé alors que le plan place « rapport HTML + a11y CI » au jalon 2 (29 janvier). Un mode démo promis hors ligne mais sans artefact consultable. |
| Innovation | 17/20 | Le meilleur point de la fiche : cinq concurrents nommés, différence structurelle nette (objet = versions du dépôt, garantie = index de version fautive), limite honnête écrite. Reste l'objection 09 assumée : la métaphore « magnétoscope » peut être classée costume décoratif, ce que la grille sanctionne explicitement. |
| Présentation | 13/20 | Le plan des 15 premières secondes est bon, mais la vidéo n'existe pas, la démo en ligne n'a aucune URL, le texte Devpost « répond aux 8 questions » sans être rédigé. Une présentation jugée sur storyboard n'est pas une présentation prouvable. |
| **Total** | **73/100** | |

## Défauts qui coûtent encore des points

1. [Impact] Le chemin d'adoption exige une installation globale npm **et** l'interposition d'un proxy MCP entre le CLI headless Kiro et ses outils — c'est une reconfiguration de la pile agent, pas « aucune installation lourde » ; il faudrait une démo d'onboarding chronométrée (de zéro à premier verdict en < 60 s, capture d'écran ou script à l'appui) ou un mode zéro-config prouvé.
2. [Impact] Circularité du corpus : les 20 sessions de `fixtures/corpus-nov2026` auraient été capturées du 1er au 12 nov., mais les chiffres publiés par l'outil (41 s, 18/20, 61 %) exigent le broker et le sandbox qui sont des livrables du jalon 1 (28 nov.) — il faudrait soit un corpus capturé par un prototype déjà committé et daté, soit marquer explicitement ces chiffres « cible » comme la convention de preuve de la fiche l'exige elle-même.
3. [Impact] « ≈ 23 h sur 3 mois » : la projection n'explique ni le nombre d'incidents sur la période ni la taille d'équipe retenue ; il faudrait la formule (incidents/trimestre × 2 h 40) avec ses intrants mesurés.
4. [Kiro] Aucune preuve Kiro n'est vérifiable dans un dépôt : specs, journal, contre-exemple graine 20261104, incident `checkpoint-guard` du 4/7 nov., comparaison spec-vs-vibe — tout est raconté, rien n'est consultable ; il faudrait les fichiers eux-mêmes (commits horodatés) pour que la case soit « prouvable dans le dépôt » au sens de la grille.
5. [Design] « axe en CI sur report.html → 0 violation » est écrit au présent alors que le jalon 2 (29 janvier) annonce « rapport HTML imprimable + a11y CI » : la fiche affirme comme acquise une preuve postérieure à la soumission ; il faudrait retirer l'affirmation ou livrer le rapport axe et le workflow CI dans le dépôt.
6. [Design] Les quatre états sont déclarés « réellement implémentés » (case 3 cochée) alors qu'aucune capture, aucun composant, aucun `report.html` n'existe ; il faudrait des captures ou une démo exécutable des états vide/erreur/flaky.
7. [Présentation] Aucun des trois artefacts de la case 5 n'existe : vidéo (storyboard seulement), démo en ligne < 30 s (pas d'URL), texte Devpost (annoncé, non rédigé) ; il faudrait au minimum la démo publiée et le texte écrit.
8. [Innovation] La métaphore VCR/magnétoscope est assumée comme risque (objection 09) alors que la grille punit la « métaphore décorative » ; il faudrait que la catégorie Frankenstein soit justifiée par un élément structurel du produit (pas seulement le naming) ou que la métaphore soit subordonnée à la mécanique dans tout le discours.

## Chiffres affirmés mais non prouvés

Aucun dépôt, aucun jeu de données ni aucune exécution ne peut encore produire ces nombres — la fiche est un projet (v1 annoncée pour le 28 novembre) :

1. **11/20 sessions (55 %) sans historique exploitable** — il faudrait le corpus `fixtures/corpus-nov2026` committé, avec la méthode d'extraction depuis les run IDs de CI reproductible par un tiers.
2. **9/20 régressions non attribuables manuellement** — idem : liste des 9 régressions, critères d'« attribution manuelle », et protocole consigné.
3. **14 min 20 s (médiane, min 3, plafond 45) de recherche manuelle** — il faudrait les chronométrages bruts des deux ingénieurs, horodatés, sur les sessions nommées.
4. **2 h 40 de temps ingénieur médian par incident non résolu** — source ou méthode de mesure absente ; il faudrait un relevé réel sur incidents clos.
5. **≈ 23 h sur 3 mois** — projection sans intrants publiés ; il faudrait la formule et le comptage d'incidents du trimestre.
6. **41 s (médiane 38 s) par exécution de l'outil** — l'outil n'existe pas ; il faudrait le benchmark sur le corpus, avec le script de mesure committé.
7. **18/20 localisations correctes, 2 flakies détectées** — c'est un critère de gel du jalon 1, pas un résultat ; il faudrait le run réel sur les 20 sessions avec verdicts et logs.
8. **Couverture réelle 61 % des étapes exécutées** — il faudrait l'instrumentation de couverture du rejeu et son rapport brut.
9. **Accord re-run 78 % (14/18 décisions)** — il faudrait les 18 décisions, les deux exécutions (bande vs re-run) et le décompte, avec seed et modèle épinglé.
10. **Contre-exemple PBT graine 20261104 (`Date.now()` dans `VERSION`)** — il faudrait la propriété, la reproduction par la graine dans le dépôt et le commit du correctif.
11. **Incidents `checkpoint-guard` du 4 nov. 14 h 12 et du 7 nov.** — il faudrait les journaux horodatés (CI ou hook log) dans le dépôt.
12. **Steering : 2 faux écarts sur 7 sessions → 0** — il faudrait les runs avant/après `determinism.md` sur les 7 sessions, avec les arbres fautifs montrés.
13. **Spec vs vibe coding : 3 h 20 / 14 allers-retours / 3 défauts contre 1 h 05 / 27 allers-retours / 6 défauts / 2 h 55 de débogage** — il faudrait les transcripts des deux sessions et le décompte des défauts, pas « chiffres du journal ».
14. **37 appels MCP, 2 exécutions de suite évitées** — il faudrait le log du serveur `replay_checkpoint` et la trace des suites annulées.
15. **Sortie exemple : session a41f9c2, 7 checkpoints, arbres 8ac91e0 / 51c0d7b, chaîne 7/7** — présenté comme une exécution réelle ; il faudrait la session dans les fixtures et la sortie reproduite.
16. **Vidéo : PR #412, merguée il y a 19 jours, 14 fichiers, 612 lignes** — il faudrait la PR réelle (ou une fixture assumée comme telle) vérifiable.
17. **axe = 0 violation, contrastes AA vérifiés** — `report.html` et le workflow CI n'existent pas (jalon 2) ; il faudrait le rapport axe généré et le pipeline committé.
18. **9 j-agent (jalon 1) et 25 j-agent (jalon 2)** — estimation sans base ; il faudrait un découpage en lots avec historique d'effort ou références comparables.

## Verdict

il reste 8 défauts à traiter avant 100/100


---

# J-09 — Jugement indépendant de V2-09 « Reprise » (Local Restore Drill), second passage

Juge : sous-agent indépendant, lecture aveugle (grille + fiche V2-09 seulement).

Note de méthode : la fiche est notée **comme un projet** — v1 annoncée pour le 28/11/2026, dépôt non
construit. Les chemins de fichiers nommés (`.kiro/specs/…`, `KIRO_JOURNAL.md`, `docs/reprise-11devs.md`,
`docs/etats/`) valent comme **cible nommée**, pas comme preuve : la grille exige que la case soit
prouvable *dans le dépôt*, et aucune ligne de ces artefacts n'est reproduite dans la fiche. Les
énoncés au passé qui exigent un code non livré (§5 contre §10) sont traités comme des défauts.

| Critère | Note | Ce qui manque pour 20/20 |
|---|---|---|
| Impact | 14 | Un seul RTO de référence dans tout le document (le doc en affiche trois : 6 min 40, 6 min 12 s, 8 min 12 s) ; la table de correspondance entre la chaîne de la perte mesurée (5 étapes) et la chaîne effectivement chronométrée par l'outil ; la source du « 4 incidents/an » qui fonde les 3 h 10 par dev et par an ; le critère de recrutement des 11 développeurs ; la trace datée du « 47 s » d'adoption. |
| Kiro | 13 | Un extrait de `KIRO_JOURNAL.md` (propriété, graine, contre-exemple, correctif) et non le seul chemin ; un protocole et un artefact de comparaison spec/vibe (`docs/spec-vs-vibe.md` : mêmes conditions, liste des 11 défauts, horodatages) ; le fichier du hook et la trace du refus du 12/11 (un pre-commit ne refuse pas un push) ; l'état initial « 2 occurrences » du steering (fichier/commit) ; les sorties des agents relecteur et testeur. |
| Design | 11 | L'alignement de §7 et §10 : les quatre vues web, l'axe-core en CI, le thème clair/sombre et le mode démo sont annoncés comme livrés alors que §10 les place au jalon 2 ; un rapport CI nommé prouvant « 0 violation » ; le chemin du rapport HTML A4 imprimable et son gabarit. |
| Innovation | 13 | Le concurrent **le plus proche** nommé : la fiche compare `restic check` (opération différente) mais omet `restic restore` / `borg restore` / borgmatic et les scripts de smoke test maison que Reprise automatise ; et une réponse structurelle à l'objection que la fiche s'attribue elle-même (Veeam Instant Verification fait déjà « restauration réelle + rapport daté »). |
| Présentation | 11 | Un artefact de démo en ligne (URL ou fichier autonome nommé) qui répond à « moins de 30 s, sans compte ni installation » alors que le mode démo est au jalon 2 ; les huit réponses Devpost, qui sont annoncées mais n'existent pas dans la fiche ; une marge sur le plan vidéo, calé à 3:00 pile. |

**Total : 62/100.**

## Défauts qui coûtent encore des points

1. [Impact] Trois valeurs de RTO coexistent et l'écart au budget est faux : §2 « la perte passe de
   « 47 min inconnues » à « **6 min 40** mesurées ce matin » », §4 « RTO local mesuré … **6 min 12 s** ·
   écart au budget **− 38 s** (budget 7 min) », §8 plan vidéo « **RTO local : 8 min 12 s** » puis carton
   « 6 min 12 s ». En outre 7 min − 6 min 12 s = **− 48 s**, pas − 38 s ; et §2 promet « **≤ 5 min en
   v1** » alors que l'exemple publié est à 6 min 12 s. Preuve : une seule valeur de référence dans tout
   le document, le journal `verdicts.jsonl` signé qui la produit, et le calcul d'écart correct.
2. [Impact] La comparaison « 47 min → 6 min 12 s » ne compare pas la même chaîne : la perte a été
   mesurée sur 5 étapes (récupérer les secrets, rejouer les migrations, re-seeder, re-configurer l'IDE,
   relancer) alors que l'outil chronomètre « snapshot → témoins verts », qui n'inclut ni le re-seeder ni
   la reconfig IDE. Preuve : une table de correspondance des 5 étapes de `docs/reprise-11devs.md` vers les
   phases de l'outil, plus un run des deux chaînes sur les mêmes postes.
3. [Impact] « coût annualisé 47 min × 4 incidents ≈ 3 h 10 par dev et par an » : le « 4 incidents/an »
   n'a aucune source dans la fiche. Preuve : la source du taux d'incident dans le protocole publié, ou la
   suppression de l'annualisation au profit du seul chiffre médian.
4. [Impact] L'échantillon (11 développeurs) n'a aucun critère de recrutement : « 11 développeurs » n'est
   pas « la quasi-totalité des développeurs visés » sans sélection documentée. Preuve : la méthode de
   recrutement et le profil (Ubuntu + Docker + Postgres) dans `docs/reprise-11devs.md`.
5. [Impact] « première valeur (découverte lecture seule + un témoin) en **47 s** mesurés » : ni protocole,
   ni horodatage, ni artefact. Preuve : un chronométrage reproductible (script + trace datée) du chemin
   `reprise discover` → premier verdict.
6. [Kiro] La preuve Kiro est écrite au passé alors que le code qui la rend possible est au jalon 1 non
   livré : §5 revendique fast-check sur `RES-P-01..05`, contre-exemples `0xC0FFEE` et `0xBEEF`, hook
   bloquant « incident du 12 nov. » et comparatif sur `extractIntoSandbox()` (packages/guard), tandis que
   §10 place garde `unshare`/Landlock, propriétés, hook et CI dans les « 6 jours-agent » du jalon 1 et
   annonce la v1 au 28/11. Preuve : soit les artefacts existent (chemin + commit daté avant le 28/11),
   soit les passages §5 sont réécrits au futur et le jalon 1 devient la seule source de vérité.
7. [Kiro] Le comparatif « spec-first vs vibe coding » n'a ni protocole ni artefact : qui a fait quoi, avec
   quel modèle, à partir de quelle consigne, et où sont la liste des 11 défauts et les 4 défauts. Preuve :
   `docs/spec-vs-vibe.md` (protocole, deux transcripts, liste des défauts avec sévérité, horodatages).
8. [Kiro] Le hook est décrit en contradiction avec lui-même : « `drill-guard` (pre-commit + gate CI)
   refuse tout commit […] **sans drill vert** » puis « hook a **refusé le push** » — un hook pre-commit ne
   refuse pas un push, et exiger un drill vert suppose le drill déjà construit et vert, donc l'incident du
   12/11 est auto-contradictoire. Preuve : le fichier du hook (chemin), son mode de déclenchement réel,
   et la trace datée du refus (message + commit/Hash refusé).
9. [Kiro] `KIRO_JOURNAL.md` est nommé mais aucun extrait n'est donné : la grille exige la propriété, la
   graine et le correctif, pas un chemin. Preuve : les deux entrées (`0xC0FFEE`, `0xBEEF`) reproduites
   avec la propriété formalisée et le correctif.
10. [Kiro] Les agents sont annoncés avec des résultats (« refuse 3 manifestes incohérents », « génère
    120 fixtures de corruption en 40 s ») sans aucune sortie nommée ; de plus le testeur est défini par
    « read + exécution sandbox », ce qui dépasse la « permissions restreintes » demandée par la grille.
    Preuve : `.kiro/agents/relecteur.json` et `testeur.json`, le journal d'exécution, la liste des 3
    manifestes refusés et le fichier de 120 fixtures.
11. [Kiro] Le steering « avant : 2 occurrences d'extraction directe du chemin de l'archive ; après : 0 » n'a
    pas d'état initial nommé : sans le fichier ou le commit qui portait ces 2 occurrences, l'effet
    avant/après n'est pas vérifiable. Preuve : le commit « avant » (ou fichier) et la commande de grep
    exécutée en CI avec sa sortie.
12. [Design] Contradiction de périmètre entre §7 (et la ligne « Design 20/20 ») et §10 : §7 présente les
    quatre états d'interface comme des « vues du rapport web local », l'axe-core en CI, le thème clair et
    sombre et le mode démo comme acquis, alors que §10 place « vue web multi-drills, thème clair/sombre »
    et « mode démo hors-ligne figé pour le jury » au **jalon 2** (29/01). Preuve : la correction de §10
    (entrer les vues en jalon 1 avec chemin de commits) ou la mention explicite que la case Design ne
    peut pas être cochée en v1.
13. [Design] « axe-core sur les 4 vues, **0 violation** » n'a ni workflow ni rapport nommé : c'est une
    affirmation sans artefact, précisément ce que la grille sanctionne (« l'accessibilité affirmée et non
    mesurée »). Preuve : le chemin du workflow CI et le rapport d'exécution (artefact) qui porte 0 violation.
14. [Design] L'artefact durable est décrit (« rapport HTML autonome imprimable, A4, une page par drill »)
    sans chemin de fichier ni gabarit d'impression ; l'export PDF est, lui, au jalon 2. Preuve : le
    fichier du rapport (chemin), le gabarit d'impression et une impression réelle A4 en une page.
15. [Innovation] Le concurrent **le plus proche** n'est pas nommé : la grille vise l'outil existant qui fait
    le plus proche, or la fiche compare `restic check --read-data` (vérifier des paquets) et non
    `restic restore` / `borg restore` / borgmatic (restaurer réellement) ni les scripts de smoke test
    maison que Reprise automatise. Preuve : un tableau comparatif contre la restauration réelle d'outillage
    existant, sur les trois axes de §6.
16. [Innovation] La fiche se donne elle-même l'objection la plus forte : « Veeam SureBackup / Instant
    Verification : restauration réelle + rapport daté ». Or l'écart invoqué est « appliance propriétaire,
    licence, périmètre serveur » — un écart d'empaquetage et de périmètre, pas une garantie différente,
    alors que la grille exige une différence structurelle qui résiste à la contradiction. Preuve : une
    phrase de différenciation qui exclut explicitement Instant Verification (garantie applicative rejouée
    + bac à sable local + verdict signé, contre restauration + rapport daté).
17. [Présentation] « démo web < 30 s, sans compte ni installation, résultat visible sans clic » n'a ni URL ni
    artefact de déploiement nommé, et le mode démo est au jalon 2 ; le corpus embarqué de 512 Mio va de
    plus à l'encontre de « première valeur en 47 s » et « binaire unique » si la démo en dépend. Preuve :
    l'artefact de démo nommé (fichier autonome ou URL) + la mesure horodatée du rendu sans clic.
18. [Présentation] Les huit réponses du formulaire Devpost sont annoncées « chiffre par chiffre (§2, §5,
    §9) », mais les huit questions ne sont ni reprises ni répondues dans la fiche. Preuve : une section
    « Devpost » listant les 8 questions et leurs 8 réponses chiffrées.
19. [Présentation] Le plan vidéo totalise exactement 3:00 (2:50–3:00 « l'artefact imprimé »), sans aucune
    marge, alors que la grille exige « moins de 3 minutes ». Preuve : le plan recalé à ≤ 2:45.

## Chiffres affirmés mais non prouvés

1. 47 min de médiane (plage 12 min – 3 h 20) — il faut `docs/reprise-11devs.md` : protocole, critères de
   sélection, horodatages par développeur, données brutes.
2. 2 / 11 n'ont pas pu rejouer leurs seeds — il faut la grille de qualification (« absence de reprise »)
   et le cas de chacun des 2 développeurs.
3. 3 h 10 par dev et par an — il faut la source du taux de 4 incidents/an.
4. 47 s de première valeur — il faut une trace datée et reproductible du chemin découverte → verdict.
5. 6 min 12 s de RTO local — il faut le verdict signé correspondant dans `verdicts.jsonl` et le calcul
   d'écart au budget.
6. 6 min 40 « mesurées ce matin » — il faut la trace datée qui la produit, et sa réconciliation avec le 5.
7. 8 min 12 s affiché à l'écran (0:00–0:04) — il faut le plan vidéo final, cohérent avec 5 et 6.
8. 5 / 5 états vitaux rouverts — il faut le manifeste signé et la sortie nominative de chaque témoin.
9. + 12 % de dérive RTO — il faut les deux verdicts successifs comparables.
10. 2 j d'âge du dernier drill vert — il faut l'horodatage du verdict.
11. 0 octet écrit hors bac à sable — il faut la sortie du diff d'empreintes avant/après.
12. `sha256:9f2c…` / `ed25519:7a1e…` — empreintes tronquées, non vérifiables ; il faut les valeurs complètes
    et le fichier de signature.
13. 2 min 12 s de CI sur un corpus de 512 Mio — il faut une exécution CI datée (aujourd'hui, projection).
14. 512 Mio de corpus signé — il faut le corpus (chemin, empreinte signée).
15. 120 fixtures de corruption en 40 s — il faut le journal du testeur et le fichier de fixtures.
16. 3 manifestes refusés par le relecteur — il faut la trace des refus.
17. Steering 2 → 0 occurrences — il faut l'état initial nommé et la sortie du grep de CI.
18. Spec-first 4 h 20 / 9 it. / 4 défauts vs vibe coding 2 h 05 / 3 it. / 11 défauts dont 2 safety-critical —
    il faut `docs/spec-vs-vibe.md` : protocole, liste des défauts, horodatages.
19. MCP « 1 h 40 → 6 min » — il faut la mesure versionnée (script + parsing JSON) des deux durées.

## Verdict

**[il reste 19 défauts à traiter avant 100/100]** — total 62/100.

Les trois gains les plus rapides : (a) unifier les trois RTO et corriger l'écart au budget (défaut 1), (b)
trancher la contradiction §7 / §10 sur le périmètre Design de la v1 (défaut 12), (c) nommer le concurrent
le plus proche — `restic restore` / `borg restore` — et répondre à Veeam Instant Verification (défauts 15
et 16). Les trois points les plus coûteux en notation sont Kiro (§5 vs §10 : les preuves ne peuvent pas
précéder le code), Design (états, a11y et mode démo annoncés mais hors jalon 1) et Présentation (démo en
ligne et Devpost annoncés, inexistants). Aucun adjectif dans ce verdict : chaque défaut ci-dessus nomme
l'artefact qui le fermerait.

---
