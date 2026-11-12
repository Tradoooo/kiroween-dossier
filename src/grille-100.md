# La barre des 100 points — et pourquoi aucune idée ne l'atteint sur papier

Boucle lancée le 12 novembre 2026 : douze idées en tête du classement développeurs ont été
**attaquées** par un agent avocat du diable (10 objections chacune, **48 bloqueurs** au total),
puis **réécrites en fiche V2** pour neutraliser chaque bloqueur, puis **jugées par un agent
indépendant** qui ne lit que la fiche et la grille — jamais les attaques ni le cahier d'origine.

## Le résultat

| Fiche V2 | Impact | Kiro | Design | Innovation | Présentation | **Total** |
|---|---|---|---|---|---|---|
| Ver — *Mutation Score* | 14 | 12 | 14 | 15 | 12 | **67/100** |
| Rejeu — *Agent Replay* | 15 | 15 | 13 | 17 | 13 | **73/100** |
| Reprise — *Local Restore Drill* | 9 | 7 | 8 | 12 | 9 | **45/100** |

**Aucune fiche écrite ne peut atteindre 100/100.** Le juge indépendant l'a établi sans ambiguïté :
quatre critères sur cinq exigent des **artefacts qui n'existent que construits** — un dépôt avec
`.kiro/specs/` et un `KIRO_JOURNAL.md` horodaté, une propriété fast-check qui a réellement échoué,
un hook qui a réellement bloqué un commit, un rapport `axe` à zéro violation, une démo en ligne,
une vidéo. Tant que le code n'existe pas, ces cases valent entre 12 et 15 sur 20.

### Le cas Reprise : 90/100 au classement, 45/100 au juge

Reprise était notée 90 dans le classement développeurs. Le juge indépendant lui donne **45**. Trois
raisons, toutes instructives :

1. **Contradiction interne** sur le chiffre central — la fiche promettait « RTO ≤ 5 min », publiait
   « 6 min 12 s » et ouvrait la vidéo sur « 8 min 12 s ».
2. **Fréquence non sourcée** — « 4 incidents par an » inventé pour annualiser un gain.
3. **Concurrents les plus proches non nommés** — devcontainers, Nix flakes, direnv, dotenv-vault.
   Un juge peut dire : « un devcontainer rend l'état local reproductible, votre exercice perd son objet. »

Leçon : une note d'opportunité élevée ne survit pas à un juge strict si la fiche se contredit ou si le
paysage concurrentiel n'est pas épuisé. Ce sont les deux premiers contrôles à faire avant d'écrire.

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

# J-09 — Jugement indépendant de V2-09 « Reprise » (Local Restore Drill)

Juge : sous-agent indépendant, n'a lu que GRILLE-100.md et la fiche V2. Rien n'est construit : toute « preuve » citée dans la fiche est une promesse tant qu'aucun artefact de dépôt n'est vérifiable.

## Notes sur 20

| Critère | Note | Ce qui manque pour 20/20 |
|---|---|---|
| Impact | 16 | Lever la contradiction interne « garantie ≤ 5 min en v1 » (§2) contre RTO mesuré 6 min 12 s / budget 7 min (§4), et rendre l'étude 11 dévs vérifiable (`docs/reprise-11devs.md` inexistant, recrutement et définition des « 4 incidents/an » non sourcés). |
| Kiro | 17 | Que chaque artefact cité existe vraiment dans le dépôt : `.kiro/specs/*`, `KIRO_JOURNAL.md` avec graines 0xC0FFEE/0xBEEF, hook `drill-guard`, agents relecteur/testeur, comparatif spec/vibe rejouable. |
| Design | 15 | Des captures réelles des 4 états (annoncées dans `docs/etats/`, absentes) et un rapport axe-core en CI à 0 violation **exécuté**, pas affirmé. |
| Innovation | 16 | Écarter nommément les reconstructeurs d'environnement déclaratif (nix, devbox, mise, devenv) : sans eux dans §6, un juge peut dire « c'est du nix avec un chronomètre ». |
| Présentation | 14 | Respecter la longueur imposée (fiche à 208 lignes, grille : 90–150) et répondre aux 8 questions Devpost **in extenso** au lieu de renvoyer à des sections. |

**Total : 78/100.**

## Défauts qui coûtent encore des points

1. Fiche de 208 lignes, hors de la borne 90–150 de la grille.
2. Contradiction chiffrée : RTO « garanti ≤ 5 min en v1 » (§2) vs exemple 6 min 12 s et budget 7 min (§4) vs carton vidéo « 6 min 12 s » (§8).
3. Aucun artefact vérifiable : specs EARS, journal, graines PBT, incident du 12 nov., steering 2→0, `verdicts.jsonl`, captures `docs/etats/`, étude 11 dévs — tout est cité comme existant, rien n'est dans un dépôt consultable.
4. Concurrents « environnement déclaratif » (nix/devbox/mise/devenv) absents de §6, alors qu'ils ciblent exactement « reconstruire l'état local ».
5. Les 8 questions Devpost sont déclarées répondues « chiffre par chiffre » par simple renvoi à §2/§5/§9.
6. Échantillon de 11 dévs : méthode de recrutement, biais de sélection et source des « 4 incidents/an » non donnés.
7. Le mode démo embarque un corpus de 512 Mio mais la démo web est promise « < 30 s sans installation » : le chargement de ce corpus n'est pas démontré compatible avec les 30 s.

## Chiffres affirmés mais non prouvables (projet, rien n'est construit)

47 min médiane / plage 12 min–3 h 20 / 2 sur 11 impossibles / 3 h 10 par dev et par an ; première valeur en 47 s ; RTO 6 min 12 s, 8 min 12 s, 12 min 04 s, dérive +12 %, écart −38 s ; 300 manifestes générés, graines 0xC0FFEE et 0xBEEF ; 120 fixtures en 40 s ; spec/vibe (4 h 20, 9 it., 4 défauts, 380 lignes, 0,9 — vs 2 h 05, 3 it., 11 défauts, 410 lignes, 0,3) ; MCP 1 h 40 → 6 min ; axe-core 0 violation ; CI corpus 512 Mio en 2 min 12 s ; charge 6 jours-agent / 20 j.

## Verdict

**[il reste 7 défauts à traiter avant 100/100]** — total 78/100.


---
