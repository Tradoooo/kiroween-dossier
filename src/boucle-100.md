# La boucle — attaques, bloqueurs et fiches V2

Douze idées attaquées (10 objections chacune, 48 bloqueurs), puis réécrites en fiches V2 pour
neutraliser chaque bloqueur. Les fiches V2 publiées ici sont celles qui étaient stabilisées au
moment de la mise en ligne ; les autres suivent.

## Les attaques

# AT-01 · Attaque — CC-01 Chemin-fantôme (Ghost Path)

Rôle : avocat du diable. Objectif : faire perdre cette idée au concours Kiroween 2026, contre GRILLE-100.

01. [bloqueur] **L'antériorité est fatale : `tsc` fait déjà ça** — Le cœur de la promesse (« un import vers `../db/session` inexistant doit être signalé ») est exactement ce que TypeScript (`error TS2307: Cannot find module`), `eslint-plugin-import/no-unresolved` et `dependency-cruiser` produisent depuis des années, dès que le patch est écrit sur disque. Pire : Serena MCP et les serveurs LSP-MCP exposent déjà `find_symbol`/`resolve_path` à l'agent *avant* qu'il écrive — la section 10 du cahier admet elle-même qu'il faut construire ce MCP, preuve que l'existant le fournit. La grille Innovation exige « aucun outil existant ne fait ça » : ici quatre le font. · Parade : abandonner la vérification des chemins/imports (couverte) et cibler exclusivement les références *hors code compilable* — routes, tables SQL, variables d'env, symboles cités en prose dans le plan de l'agent — que ni tsc ni ESLint ne voient jamais.

02. [majeur] **La réduction tue : « c'est un linter d'imports qui lit du JSONL »** — Enlevez le costume : parser un journal JSONL, regexer les chemins, les passer à un resolver existant. Un juge écrira « diff d'entrée = log d'agent au lieu de fichier source, sinon c'est `no-unresolved` » et la phrase de différenciation en une ligne (exigence 8 de la fiche V2) ne résiste pas à cette contradiction. Le cahier revendique « on ne corrige pas l'agent, on prouve où il a menti » : c'est une métaphore décorative, explicitement listée comme ce qui coûte des points. · Parade : rendre la différence structurelle et démontrable en une phrase — par exemple la garantie de rejeu binaire au commit fixé avec attribution par citation horodatée, ce qu'aucun linter ne produit car aucun ne travaille sur une session d'agent.

03. [bloqueur] **La v1 en 8 jours est une fiction** — Le lot 1 (3 jours) promet « fichiers + exports AST » pour TypeScript : à eux seuls, les alias `tsconfig.paths`, les barrels `index.ts` avec re-exports, la résolution `node_modules` et les workspaces mono-repo consomment cette enveloppe. Derrière, il reste 5 jours pour extract sur des journaux hétérogènes, resolve + distance aux candidats, rapport HTML *accessible AA vérifiée axe en CI* (exigence Design 20/20), mode CI, plus toute la preuve Kiro (PBT, hook qui a vraiment bloqué, steering avant/après, comparaison spec/vibe chiffrée). Le gel au 28 novembre tombera avec un MVP sans rapport ni preuves Kiro. · Parade : couper la v1 à TypeScript sans alias + chemins de fichiers uniquement (pas de symboles), rapport JSON brut et page HTML minimale générée, et pré-rédiger les specs Kiro dès le jour 1 pour que les preuves existent au gel.

04. [majeur] **Le chiffre mesuré est circulaire** — « 100 % des fantômes du corpus détectés » : le corpus de fixtures est construit par l'auteur, donc la mesure prouve seulement que l'outil retrouve ce qu'on y a planté — la grille Impact exige une perte chiffrée *avec source ou méthode de mesure*, et « < 2 % de faux positifs sur code sain » est mesuré sur un dépôt sain choisi par l'auteur. Le 12 % → 3 % de la vidéo repose sur deux sessions, n=1 de chaque côté, aucune variance, aucune reproductibilité. · Parade : mesurer sur des journaux réels publics (sessions Claude Code/Codex partagées) et sur 5 dépôts open-source non choisis pour le test, publier faux positifs ET faux négatifs avec intervalles.

05. [majeur] **La vidéo montre une fonctionnalité qui n'existera pas** — La séquence 2:20–3:00 (comparaison de deux sessions via le MCP de vérité, 12 % → 3 %) dépend des lots 5 et 6, planifiés pour décembre–janvier, donc absents au gel v1 du 28 novembre : soit la vidéo ment, soit elle est reconstituée, et un juge qui vérifie le dépôt le verra. Le reste (0:20–1:40) est un terminal qui affiche du JSON puis un `ls` — la grille Présentation exige un produit montré de bout en bout sur l'appareil visé, pas un CLI brut. · Parade : couper la séquence MCP de la vidéo v1 ou livrer un MCP minimal dans la v1 ; remplacer le terminal par le rapport HTML avec citations cliquables comme plan principal.

06. [majeur] **Le récit Kiro est prévu, pas vécu** — La grille est explicite : « ce qui coûte des points : un journal écrit après coup ; aucune propriété qui ait jamais échoué ». Or le cahier planifie à l'avance le hook `ghost-path-guard` qui « refusera une PR » et la comparaison spec/vibe « mesurée » : au stade du cahier, aucune propriété n'a encore trouvé de contre-exemple réel avec graine documentée. Le hook lui-même est décoratif-circulaire : l'outil anti-fantômes garde ses propres fixtures, un scénario qu'on se fabrique en dix secondes. · Parade : écrire dans le journal les incidents réels au fur et à mesure, et faire garder par le hook un vrai dépôt tiers (un fixture open-source) où une régression a effectivement été bloquée, capture à l'appui.

07. [majeur] **Dans six mois, le problème est résolu par les agents eux-mêmes** — La boucle « l'agent écrit → le compilateur refuse → l'agent corrige » existe déjà dans Kiro, Claude Code et Cursor : un import fantôme coûte un aller-retour de compilation, quelques secondes, pas « six minutes ». La tendance lourde est l'intégration LSP native dans les agents (Serena, MCP de langage, éditeurs qui exposent le graphe de symboles) : en janvier 2027 la vérification se fera *dans* l'agent, en amont, et un scanner post-hoc de journaux sera un outil de niche pour l'audit. La grille Impact exige un problème « vécu ce mois-ci » par la quasi-totalité : celui-ci est en cours de disparition. · Parade : repositionner sur l'audit et la conformité (preuves datées pour revues de code, régulateur, équipes qui n'ont pas le droit de faire confiance à l'agent) plutôt que sur le gain de temps développeur.

08. [bloqueur] **L'angle mort technique ruine la garantie binaire** — La promesse « résolution binaire, zéro référence non résolue passée inaperçue » explose sur le réel : chemins construits dynamiquement (`` `./locales/${lang}.json` ``), alias et barrels, mono-repos où `@org/db` résout par workspaces, JavaScript non typé où `Users.getOne` n'a aucun export vérifiable, routes Express définies par composition. Et l'extraction elle-même est floue : dans la prose d'un agent, distinguer une référence à un fichier d'une simple chaîne de caractères (« range ça dans src/utils un jour ») est un problème de NLP que le cahier évacue d'une ligne. Le risque « faux positifs sur chemins dynamiques : fort » est admis par l'auteur — un juge lira que la métrique centrale n'est pas fiable. · Parade : restreindre honnêtement le périmètre aux références dans les blocs de code et diffs (jamais la prose), documenter la limite comme non-objectif chiffré, et viser la précision plutôt que le rappel dans la phrase de différenciation.

09. [mineur] **Le « déjà vu » des hackathons : énième IA-qui-vérifie-une-IA** — Les juges Devpost ont vu des dizaines de projets « hallucination checker » : métriques de faithfulness RAG dans DeepEval et LangSmith, guardrails type NeMo Guardrails, validateurs de sorties LLM. La catégorie Frankenstein attire exactement ce genre de méta-outils, et « l'agent ment, on le prouve » est une accroche usée depuis 2023. Sans un angle inattendu, le projet se noie dans la pile même s'il est bien exécuté. · Parade : incarner le costume Frankenstein par un artefact visuel fort et inédit — par exemple un « registre des mensonges » imprimable et daté, avec extraits cités façon pièce à conviction — que personne d'autre ne produit.

10. [bloqueur] **En démo directe, ça casse sur le dépôt du juge** — La grille exige une démo en ligne en moins de 30 secondes sans installation, et le meilleur argument du projet est « lancez-le sur VOTRE dépôt » : or le juge qui le fait tombe sur un format JSONL différent (Claude Code ≠ Cursor ≠ Kiro), des alias tsconfig non gérés en v1, et une avalanche de faux positifs `ghost` sur `@org/*` — la démonstration s'auto-détruit en direct. La cible « base de vérité d'un dépôt de 50 000 lignes < 20 s » n'est testée que sur des fixtures jouets ; sur un vrai dépôt avec `node_modules` et barrels, la résolution des symboles peut diverger ou exploser en mémoire. · Parade : fournir un mode démo verrouillé (journal + dépôt inclus, zéro réseau, comme l'exige la grille Design) ET un adaptateur par format de journal déclaré supporté, testé en CI sur un dépôt open-source réel de 50 k+ lignes.

---

# AT-02 · Attaque de CC-02 *Poisoned Prompt* — avocat du diable

10 objections, une par champ imposé. Objectif : faire perdre cette idée.

01. [bloqueur] **L'antériorité est écrasante et déjà open source** — **LLM Guard (Protect AI)** fait exactement ça : scanners locaux, déterministes, versionnés (`BanSubstrings`, `Secrets`, `Regex`), intégration CI, faux positifs mesurés ; **Rebuff** et **NeMo Guardrails** couvrent le reste. La fiche cite « filtres propriétaires cloud » comme seul existant — c'est un épouvantail : le concurrent direct, gratuit et local, n'est même pas nommé. · Parade : nommer LLM Guard explicitement et prouver une différence structurelle (ex. garantie de détermination + rejeu de corpus que LLM Guard n'offre pas), sinon retirer la claim d'innovation.

02. [bloqueur] **« C'est juste un grep déguisé en courrier d'Halloween »** — 60 règles déterministes sur du texte, c'est `grep -f patterns.txt` avec un rapport HTML et un costume ; la catégorie Resurrection exige que la métaphore apporte une mécanique, or le « sas de tri du courrier » ne change rien au moteur (regex + normalisation). Le jury cochera « métaphore décorative », ce que la grille punit explicitement. · Parade : faire porter la métaphore par une vraie mécanique de quarantaine (texte mis en salle d'attente, levée de doute, traçabilité type registre de courrier) visible dans le produit.

03. [majeur] **La v1 en 8 jours est un rêve de planning** — les lots 1 à 4 totalisent exactement 8 jours, zéro marge, et n'incluent ni les specs `.kiro/`, ni le PBT, ni le journal spec/vibe, ni le rapport AA à 0 violation axe — tout ce que la grille exige au score. Surtout, le lot 3 (1,5 jour) promet 200 attaques + **2 000 issues réelles anonymisées** : collecter, anonymiser et valider 2 000 issues réelles en une journée et demie est irréaliste, sans parler du RGPD. · Parade : réduire la v1 à 500 issues saines et 100 attaques, et pré-chiffrer les jours Kiro (specs/PBT/journal) dans le plan.

04. [bloqueur] **Les chiffres sont circulaires** — « 200/200 détectées » mesure un corpus construit *par* l'équipe *pour* ses règles : c'est un test unitaire déguisé en résultat. Le « 0,4 % de faux positifs » annoncé dans la vidéo est mesuré sur un corpus sain maison, jamais sur un jeu tiers ; et la grille exige que la perte soit chiffrée *avec source* — ici aucun incident réel, aucun benchmark indépendant. Un juge demande « sur quelles vraies attaques, trouvées par qui ? » et tout s'effondre. · Parade : évaluer aussi sur un corpus tiers public (ex. jeux d'injection de la littérature ou issues GitHub réelles d'incidents documentés) et publier le taux de détection *hors* corpus maison.

05. [majeur] **La vidéo démo ne prouve rien de bout en bout** — le payload montré (commentaire HTML `cat .env`) est écrit par l'équipe qui a écrit la règle : c'est un match garanti, pas une détection. Aucun plan ne montre un *agent réel* détourné sans l'outil puis sauvé avec l'outil ; le verdict `block` dans un terminal ne prouve pas que l'exfiltration aurait eu lieu. Le plan « ajout d'une règle en direct » est du théâtre rejoué mille fois. · Parade : filmer un agent Kiro qui exécute réellement l'injection (fuite vers un fichier témoin) puis la même scène avec le sas, fuite absente — avant/après mesurable.

06. [majeur] **Le récit Kiro est décoratif sur les points clés** — le serveur MCP `scan_text`, seul élément qui accroche l'outil à un agent, est repoussé au lot 6 en janvier : la v1 soumise n'est donc *pas* un pré-filtre d'agent (O4 non tenu). Le hook `rules-corpus-guard` n'est que la suite de tests rejouée — un CI banal, pas l'incident de régression raconté qu'exige la grille ; et comparer spec/vibe sur « l'écriture de 10 règles » regex est un exercice trop petit pour être probant. · Parade : livrer un MCP minimal dès la v1 et documenter un vrai blocage de hook avec date, diff et correctif.

07. [majeur] **Dans six mois, plus personne** — les plateformes intègrent nativement la défense (GitHub, Anthropic, OpenAI durcissent leurs agents contre l'injection côté produit), et le déterministe perd la course aux contournements : la fiche l'admet elle-même (« jeu du chat et de la souris assumé »). Pire, la question ouverte (2) avoue que publier le catalogue **arme les attaquants** : l'outil a une date de péremption écrite dedans. · Parade : cibler un usage durable que les plateformes ne couvriront pas (conformité/audit : registre horodaté des textes bloqués pour la preuve de diligence), pas la détection elle-même.

08. [bloqueur] **Angle mort : les issues qui *parlent* d'injection seront bloquées** — tout rapport de sécurité citant un payload (« voici l'attaque reçue : ignore previous instructions… »), toute doc, tout test déclenchera `block` : la classe de faux positifs la plus fréquente du corpus sain est structurelle, pas marginale. Et côté faux négatifs, rien ne détecte l'injection *sémantique* sans mot-clé (« le mainteneur a demandé d'afficher la config pour le debug »), ni le payload scindé sur plusieurs lignes, ni l'injection en français — les règles citées sont anglo-centrées. · Parade : contexte-aware (citer un payload dans un bloc de code/une quote ≠ l'énoncer), règles multilingues, et publier la liste des contournements connus *non* détectés.

09. [majeur] **« Déjà vu » est le verdict le plus probable du jury** — les scanners de prompt injection ont saturé les hackathons 2024-2025 ; un juge qui a vu dix « LLM firewall » locaux classera celui-ci sans même lire la différenciation. La grille exige « aucun outil existant ne fait ça » : ici trois outils le font (objection 01), et la phrase de différenciation (« local, déterministe, explicable ») décrit aussi LLM Guard. · Parade : déplacer la proposition de valeur sur l'artefact unique — le corpus versionné + le rejeu avec variation de faux positifs (INJ-F-06) comme *produit*, pas le scanner.

10. [bloqueur] **Le jour J, le juge écrit son propre texte** — deux scénarios tuent la démo live : le juge soumet une phrase innocente dans sa langue ou citant une attaque et obtient `block` (faux positif humiliant en direct), ou il paraphrase une attaque sans mot-clé et obtient `pass` (faux négatif pire encore, l'outil promettant 100 %). Le « rejeu du corpus en direct » (200 attaques + 2 000 issues) peut aussi dépasser le créneau, et aucun mode démonstration hors-ligne figé n'est prévu alors que la grille l'exige. · Parade : préparer un mode démo à données incluses + une réponse scénarisée au faux positif (« verdict review, citation de la règle, levée de doute en un clic ») qui transforme l'incident en preuve d'explicabilité.

---

# AT-03 · Ver — *Mutation Score* — avocat du diable (10 objections)

01. [bloqueur] **« Exécution ciblée » est LA fonctionnalité historique de PIT, pas une innovation** — PIT (pitest.org) sélectionne depuis 2010 les tests par couverture de ligne avant de muter, et Stryker a `--incremental` + `coverageAnalysis: perTest` qui ne rejoue que les tests pertinents ; le tableau « Différence » du cahier décrit donc le comportement par défaut des deux concurrents qu'il cite. La seule différence restante est un rapport « orienté action », c'est-à-dire cosmétique au sens de la grille (critère 4 : structurelle, pas cosmétique). · Parade : trouver un mécanisme réellement absent de PIT/Stryker (ex. preuve formelle d'équivalence par opérateur, ou sélection par graphe de dépendance de données plutôt que par couverture de ligne) et le nommer en une ligne vérifiable.

02. [bloqueur] **Le budget temps est contredit par ses propres chiffres** — 4 132 mutants en < 4 min sur 4 cœurs, c'est ~58 ms par mutant tout compris : transpilation TS, sandbox, lancement ciblé du runner. Un seul démarrage de worker Vitest/Jest coûte 200 ms à 1 s ; Stryker annonce des heures sur des dépôts de cette taille, et le lot 1 (carte ligne → tests) exige un run d'instrumentation par test, donc O(tests × suite) avant même de muter. · Parade : publier un benchmark réel sur la fixture avec le chrono brut (pas une cible), assumer un échantillonnage stratifié comme mode par défaut, ou réduire la v1 à 500 mutants sur un mini-dépôt en le disant.

03. [majeur] **La réduction méprisante tient en une phrase : « un wrapper Stryker avec un joli rapport »** — Stryker publie déjà le survivant avec sa ligne, son mutant et les tests qui le couvrent (`stryker report` + dashboard), garde un seuil en CI (`--thresholds-break`) et compare les commits sur son dashboard. Il ne reste à Ver que le formatage ; un juge qui connaît Stryker coche « wrapper autour d'un outil existant », ce qui coûte explicitement des points au critère 4. · Parade : supprimer toute dépendance possible à Stryker et démontrer une garantie qu'il n'a pas (ex. reproductibilité bit-à-bit du score, preuve que la sélection ciblée ne rate aucun test tueur — avec contre-exemple à l'appui).

04. [majeur] **Le score publié n'est pas comparable, donc le seuil CI est un gadget** — la doc Stryker elle-même avertit que le mutation score dépend du jeu d'opérateurs, du style de code et des équivalents restants : 89,3 % ici et 62 % ailleurs ne mesurent pas la même chose, et l'indicateur « score identique entre deux runs » ne prouve rien sur la signification du chiffre. Une équipe dont le dépôt est plein de code mort ou de constantes hérite d'un seuil arbitraire qu'elle passera son temps à abaisser. · Parade : ne publier en v1 que la tendance par commit et par fichier (delta de survivants sur le diff), jamais un absolu gardé par un seuil global.

05. [majeur] **L'exclusion manuelle des équivalents (MUT-F-07) est une faille de gaming béante** — la détection d'équivalence sémantique est indécidable en général ; avec une heuristique à « < 5 % de faux », la porte de sortie est évidente : marquer les survivants gênants comme `equivalent` et le score monte sans écrire un test. Le chiffre phare de l'outil est donc manipulable par son utilisateur en trois clics, ce qui ruine la promesse « mesure honnête ». · Parade : rendre toute exclusion signée, horodatée, comptée et affichée dans le score (« 89,3 % dont 4,1 % d'exclusions manuelles »), avec ratchet interdisant d'augmenter le taux d'exclusions.

06. [majeur] **La sélection par couverture de ligne rate les vrais tueurs** — un test d'intégration ou un snapshot qui échoue à cause d'un mutant situé à trois appels de là ne « couvre » pas forcément la ligne au sens de la carte ligne → tests ; MUT-P-04 ne vérifie la complétude que contre un run complet « sur un sous-ensemble », c'est-à-dire sur les fixtures de l'auteur. Résultat : des mutants classés `survived` que la suite complète tue, et un score faussement bas — exactement l'inverse de la promesse d'honnêteté. · Parade : double mode (ciblé / complet) avec mesure publiée de l'écart sur un dépôt tiers réel, pas une fixture maison.

07. [majeur] **La vidéo repose sur une exécution qu'elle ne peut pas montrer** — le plan 0:20–1:00 affiche un run de 4 132 mutants censé tenir en 40 secondes à l'écran alors que la cible interne est 4 minutes : tout le monde verra l'accéléré ou le cache, et la grille punit la démo qui ne tient pas ses promesses. Pire payoff dramatique : ajouter un test fait passer le score de 89,3 à 89,4 — un dixième de point, invisible, anticlimatique. · Parade : démo sur un mini-dépôt où le run réel tient en < 60 s chrono affiché à l'écran, et un survivant qui fait chuter un fichier entier de 95 % à 40 % pour que le chiffre saute aux yeux.

08. [mineur] **Le récit Kiro est circulaire et interchangeable** — tester un générateur de mutants avec des mutants générés aléatoirement (MUT-P-01 à 05) n'a de valeur que si l'oracle est indépendant, or l'oracle est… l'outil lui-même ; et le hook `mutation-budget` est une commande CI banale que GitHub Actions exécute sans Kiro. La comparaison spec/vibe coding sur l'opérateur `boundary` est le seul point réellement probant, et il porte sur le composant le plus simple. · Parade : propriétés avec oracle externe (ex. mutants semés à la main avec verdict connu, ou comparaison contre PIT sur du code JVM équivalent) et un hook Kiro qui bloque une vraie régression du moteur, racontée avec date et diff.

09. [majeur] **Dans six mois, plus personne** — les équipes qui adoptent le mutation testing l'abandonnent massivement à cause du coût (c'est le reproche n°1 dans les issues Stryker), et Stryker/PIT sont gratuits, maintenus, intégrés aux dashboards existants ; un mutateur TS solo de hackathon n'a aucune raison de survivre face à eux, surtout si sa seule avance (ciblage) est déjà dans leurs releases. Le public « toute équipe qui affiche une couverture » est précisément le public théorique que la grille pénalise. · Parade : nommer un utilisateur type précis avec sa perte chiffrée ce mois-ci (ex. équipe CI-contrainte à un seuil de couverture réglementaire) et un canal d'adoption en < 60 s (`npx` sur le dépôt courant, sans config).

10. [bloqueur] **Le jour J, c'est le chronomètre et le sandbox qui cassent** — en live : machine du jury ≠ 4 cœurs garantis, parallélisation qui rend l'ordre des timeouts non déterministe (un mutant `timeout` compte-t-il `killed` ? le cahier ne tranche pas), tests utilisant `Date.now()` ou le réseau qui rendent le score non reproductible, et MUT-F-01 « jamais modifier le disque » : le moindre bug d'écriture dans le bac à sable corrompt l'arbre de travail devant le jury. « Mutation testing » est en outre un sujet classique de hackathon (technique de 1978, DeMillo/Lipton/Sayward) : le « déjà vu » est garanti sans preuve d'un mécanisme neuf. · Parade : mode démo 100 % pré-enregistré en cache avec données embarquées (exigence grille §3), politique `timeout` écrite noir sur blanc, empreinte d'arbre vérifiée avant/après chaque run de démo, et une slide assumant l'antériorité avec la différence structurelle en une ligne.

---

# AT-04 · Attaque de CC-04 « Fuite / Redact » — 10 objections (avocat du diable)

01. [bloqueur] **Antériorité écrasante : le canal sortant est déjà occupé** — gitleaks et trufflehog lisent `stdin`/flux depuis des années, GitGuardian et GitHub secret scanning interceptent au push, et Nightfall AI fait exactement la rédaction en ligne d'un flux sortant avec journal d'audit. Le DLP d'entreprise (Zscaler, Forcepoint) est le « point de passage unique » que la fiche revendique comme sien. · Parade : nommer Nightfall comme concurrent direct et déplacer la garantie sur le registre chaîné vérifiable **hors ligne, sans cloud, sans compte** — seule chose qu'aucun des quatre n'offre.

02. [majeur] **La réduction méprisante tient en une ligne : « c'est gitleaks sur un pipe »** — motifs par type, entropie sur jetons longs, validation Luhn : c'est littéralement le jeu de règles public de gitleaks (MIT) plus une substitution de sous-chaîne et un fichier append-only. Un juge technique compte ~200 lignes réelles de logique neuve pour 3 500 annoncées. · Parade : assumer « moteur emprunté, garantie nouvelle » et prouver la garantie par PBT (P-02) et par une vérification tierce du journal — ce que gitleaks ne fait pas.

03. [bloqueur] **La v1 de 8 jours n'intercepte pas la sortie du scénario d'accroche** — le plan met le proxy HTTP/prompt au lot 5, en décembre : au gel du 28 novembre, `gate` ne couvre que logs et exports fichiers. La fuite racontée en §2 (le prompt de l'agent qui part avec `DATABASE_URL`) est donc impossible à montrer dans la vidéo de la v1. · Parade : remplacer le proxy TLS par un wrapper/hook MCP `check_outbound` sur un seul agent (Kiro ou Claude Code), livrable au lot 3, et rayer le HTTPS de la v1.

04. [majeur] **Le chiffre publié est une tautologie** — « 100 % des secrets du corpus interceptés » ne mesure rien : le corpus est écrit par l'auteur, qui connaît chaque secret et chaque motif. « 37 secrets interceptés sur la journée » et « 41 alertes / 12 confirmées » sont des nombres de démonstration, pas une perte vécue ce mois-ci comme l'exige la grille §1. · Parade : mesurer sur un corpus réel non contrôlé (historique git public, `git-secrets-tests`, logs réels du poste) et publier un taux avec intervalle et faux négatifs assumés.

05. [majeur] **La vidéo est illisible : trois minutes de terminal et de voix off** — les 15 premières secondes (fichier `.env` + agent qui prépare une requête + « Regardez ce qui part vraiment ») dépendent entièrement de la narration, ce que la grille §5 interdit explicitement. Le moment fort (`redact verify` échoue après altération) est du texte gris sur fond noir, invisible en 720p. · Parade : une page locale à deux volets (flux brut / flux rédigé) avec compteur qui s'incrémente en direct, et un plan d'ouverture où `[REDACTED:github_token]` apparaît en rouge sans un mot.

06. [majeur] **Le récit Kiro est décoratif** — le hook `no-secret-in-fixtures` ne bloque aucune régression puisqu'il vérifie des fixtures écrites par l'auteur ; P-02 est un test de non-occurrence sur des corpus connus ; et aucune comparaison chiffrée spec/vibe coding n'apparaît dans le cahier. La grille §2 exige un incident réel raconté et une mesure, pas un tableau d'intentions. · Parade : fabriquer dès maintenant un incident vérifiable (secret injecté en CI, hook qui refuse le commit, graine et correctif dans `KIRO_JOURNAL.md`) et chiffrer une fonction réalisée spec contre vibe.

07. [mineur] **À six mois : aucun chemin d'adoption** — un certificat racine local à installer, une politique par canal à écrire, des listes blanches à entretenir : c'est un outillage DLP déguisé en outil dev, et le dev visé a déjà le secret scanning gratuit de son forge. Le non-objectif « pas de DLP d'entreprise » contredit la mécanique, qui en demande l'effort d'installation. · Parade : une seule commande d'installation, zéro certificat, zéro compte, première valeur en moins de 60 secondes, et le catalogue de motifs publié comme bien commun.

08. [bloqueur] **Angle mort assumé mais noyé : faux sentiment de sécurité** — un mot de passe interne, un jeton maison, un nom de client sous NDA, une URL de staging : rien n'est intercepté, et la fiche le range en ligne 4 d'un tableau de risques. Pire, le journal chaîné devient une « preuve » que rien n'a fuité alors qu'il ne prouve que l'absence des familles connues. · Parade : afficher à chaque `guard` la couverture mesurée (« 8 familles, X % du corpus réel ») et bannir tout vocabulaire de garantie au profit de « filet détectable ».

09. [majeur] **Risque « déjà vu » maximal dans la catégorie** — la sécurité des sorties d'agents est le thème le plus saturé de 2026 : prompt-injection shields, MCP gateways, sandboxes, et chaque saison Devpost amène son lot de « ne laissez pas l'agent fuiter vos clés ». Un juge qui en a vu cinq ne lira pas la ligne de différenciation, il cochera « wrapper de scanner ». · Parade : ne plus se vendre comme protection mais comme **preuve** — registre chaîné auditable par un tiers, angle que les shields ne traitent pas.

10. [bloqueur] **En démo directe, ça casse devant le juge** — le juge colle un vrai jeton `ghp_` expiré (faux négatif immédiat), ou une ligne de log contenant un UUID/un hash de commit déclenche l'entropie et la rédaction corrompt une sortie légitime (faux positif visible). L'altération du journal, seul moment spectaculaire, dépend de l'état d'un fichier et d'un terminal non rejouable. · Parade : un mode `redact demo` 100 % fixtures sans réseau, et montrer volontairement un faux négatif et un faux positif avant le succès — l'honnêteté devient jouable en direct.

---

# AT-05 — Attaque de CC-05 *Rejeu* (avocat du diable)

Lecture : GRILLE-100.md + cahiers/CC-05-rejeu.md. Dix objections, une par champ imposé.

01. [majeur] **rr et replay.io font déjà le rejeu déterministe, en plus fort** — Mozilla **rr** rejoue un processus réel au niveau des appels système avec FS virtuel et horloge contrôlée ; **replay.io** vend le time-travel debugging ; **VCR/cassettes** rejouent le réseau ; LangSmith/Langfuse rejouent des traces d'agents. La grille exige « aucun outil existant ne fait ça » : ici quatre le font, et le cahier ne nomme aucun concurrent précis — il cite des catégories floues (« journaux d'agent », « snapshots »), ce qui coûte directement les 20 points d'innovation. · Parade : nommer rr et replay.io et prouver une différence structurelle (rejeu hors processus, au format ouvert, sans runtime instrumenté) — sinon abandonner la claim d'innovation.

02. [bloqueur] **« C'est juste un enregistreur de log avec un diff »** — la capture produit un JSONL (ce que Claude Code, Kiro et OpenAI Agents SDK écrivent déjà), le rejeu relit ce JSONL en réinjectant les sorties, et le « diff étape par étape » est un `jq` + `diff`. Toute la mécanique tient en une phrase de mépris, et la grille punit explicitement « un wrapper autour d'un outil existant ». · Parade : ajouter une garantie que le log seul n'offre pas (signature cryptographique de la chaîne d'étapes, empreinte de dépôt vérifiée à chaque étape, détection de triche) et la montrer comme impossible avec un log brut.

03. [bloqueur] **O3 (capture sans instrumenter l'agent) est incompatible avec la capture promise** — le cahier promet graine, horloge injectée et config capturées, mais un adaptateur JSONL passif ne voit que ce que l'agent veut bien logger : ni graine, ni horloge, ni empreinte par étape. Injecter une horloge logique dans un agent tiers exige de le modifier — exactement ce que REJ-N-01 interdit. En 9 jours, il faut choisir : capturer pauvrement (et le rejeu n'est plus « déterministe ») ou forker l'agent (et O3 tombe). · Parade : restreindre la v1 à un agent dont on contrôle le runtime (le CLI headless de Kiro) et l'écrire noir sur blanc dans la fiche V2, en sacrifiant O3.

04. [bloqueur] **Le chiffre phare « 214/214 identiques » est une tautologie** — le rejeu réinjecte les sorties capturées des étapes non déterministes (REJ-F-02), donc l'identité est vraie **par construction** : l'indicateur « 100 % des sessions rejouées à l'identique » ne peut mathématiquement pas échouer. La seule mesure honnête — relancer l'agent avec la même graine et comparer — est listée en non-objectif (« pas de régénération des réponses du modèle »). La grille exige une perte chiffrée mesurée par l'outil : ici l'outil mesure sa propre tautologie. · Parade : publier un deuxième chiffre non tautologique (ex. taux de rejeu identique après régénération réelle du modèle avec graine fixée, même à 60 %) ou retirer la prétention de mesure.

05. [majeur] **La démo vidéo montre un lecteur de vidéo** — 0:20–1:00 : on regarde défiler deux fois la même sortie, « 214 identiques » ; 1:00–1:50 : on édite un champ JSON à la main et une ligne rouge apparaît — c'est un diff, pas un produit. Aucun des quatre états d'interface n'existe visuellement, rien n'est spectaculaire en 15 secondes, et la grille exige que le juge comprenne le problème **et** le chiffre sans narration : ici la voix off fait tout le travail. · Parade : ouvrir sur une régression réelle incompréhensible, puis montrer le rejeu qui la rejoue et localise l'étape fautive en direct, avec une vraie interface (timeline, états vide/erreur/chargement).

06. [majeur] **Kiro est décoratif dans le récit d'usage** — le hook `logical-clock-guard` est une règle de lint (interdire `Date.now`), le serveur MCP est un wrapper du CLI, et le « rejeu nocturne Crew » rejoue des fixtures, pas du travail réel. Rien n'utilise specs/steering comme mécanisme central ; l'outil est agent-agnostique et tournerait aussi bien sans Kiro, ce qui affaiblit « Best Kiro Crew App » visé en prix. · Parade : faire de Kiro le sujet — capturer les sessions des agents Crew de Kiro elles-mêmes, et montrer qu'une spec EARS du dépôt génère le contrat que le rejeu vérifie.

07. [majeur] **Personne ne rejoue une session d'agent** — le scénario du cahier (régression trois semaines après un correctif accepté) se résout aujourd'hui par `git blame`, le diff de la PR et les tests CI, pas par le rejeu d'une session ; le public « équipes qui audittent » existe surtout dans la compliance, qui a déjà LangSmith/Langfuse avec rétention et export. La grille exige un problème vécu **ce mois-ci** par la quasi-totalité des développeurs visés : « je voudrais rejouer ma session d'agent » n'est le besoin de personne, c'est une solution en quête de problème. · Parade : trouver un cas où le rejeu est la seule issue (bug Heisenberg non reproductible même avec les logs, incident où le journal est incomplet) et le chiffrer sur une session réelle.

08. [bloqueur] **Le rejeu « exécute réellement » les effets de bord** — l'étape 3 de la mécanique rejoue les sorties capturées du modèle mais **exécute** le reste : écritures de fichiers, commandes shell, git push de la session d'origine, le tout sur une machine dont le dépôt a dérivé depuis la capture. Rejouer une session qui contenait `rm -rf` ou un push est soit destructeur, soit diverge dès l'étape 1 (empreinte de dépôt fausse) ; le cahier classe le bac à sable FS en **question ouverte** (question 2) alors que c'est le cœur du moteur. · Parade : décider maintenant — soit sandbox complet (overlay FS + réseau coupé, ce qui mange le lot 3 entier), soit rejeu 100 % simulé, et assumer que dans ce cas on retombe sur l'objection 02.

09. [mineur] **Le jury dira « déjà vu » dans la catégorie Frankenstein** — « ressusciter le magnétoscope » est la métaphore la plus évidente du lot, et record/replay est un thème rabâché de hackathon (rr date de 2013, replay.io a levé 25 M$ dessus) ; sans preuve d'un mécanisme nouveau, le juge classe l'idée en « VCR pour agents, sympathique ». · Parade : une ligne de différenciation qui résiste à la contradiction — par exemple « le seul rejeu qui fonctionne sur un journal déjà écrit, sans avoir instrumenté l'exécution d'origine » — et la défendre avec l'objection 03 résolue.

10. [majeur] **Le jour de la démo en direct, l'empreinte du dépôt ne matchera pas** — le rejeu vérifie `repoDigest` et exécute de vraies étapes : sur la machine de démo (autre chemin absolu, autre version de Node, autre locale), les étapes déterministes divergent pour de fausses raisons et le rapport affiche des divergences parasites devant le jury — le contraire exact du « mode démonstration qui ne peut pas échouer » exigé par la grille. Pire : si la démo tombe sur l'étape qui exécute un shell, elle peut échouer en direct. · Parade : un mode démo embarqué (fixtures + dépôt miniature inclus, zéro réseau, zéro exécution réelle) construit dès le lot 1, pas à la veille du gel.

---
Bilan : 4 bloqueurs (02, 03, 04, 08) — la tautologie du chiffre (04) et l'angle mort des effets de bord (08) sont les deux plus mortelles pour la grille.

---

# AT-06 · Agent Review — 10 objections (avocat du diable)

Cible : `cahiers/CC-06-diff-agent.md`, jugée contre `GRILLE-100.md`. Objectif : faire perdre cette idée.

01. [bloqueur] **Tout l'outillage existe déjà, pièce par pièce** — `danger.js` fait depuis 2017 exactement les règles du lot 4 (`fail` si lockfile modifié, si un fichier hors liste déclarée est touché, si des tests sont supprimés), le `dependency-review-action` officiel de GitHub publie déjà dépendances ajoutées, licences et taille (DAG-F-06 recopié), et Microsoft `api-extractor` établit la surface publique d'un paquet TS avec ses ruptures. Il ne reste qu'un `git diff --stat` collé à trois actions existantes. · Parade : prouver qu'aucune composition d'outils existants ne produit le même rapport, en exécutant danger.js + dependency-review + api-extractor sur la même diff et en montrant ce qu'ils ratent, chiffre à l'appui.

02. [majeur] **La réduction qui tue : « un diff --stat avec un champ declaredFiles »** — un juge pressé résume l'idée en une phrase : tu fais saisir à l'humain le périmètre que tu prétends deviner, puis tu soustrais deux listes de chemins et tu appelles ça une mesure. Le cahier lui-même avoue la béquille (risque 1 : « exiger une liste de fichiers déclarés en mode strict »), donc le mode fiable est celui où l'outil ne devine rien. · Parade : supprimer le mode « périmètre déclaré obligatoire » du récit et démontrer l'extraction automatique sur une demande jamais vue, ou assumer et vendre autre chose que la reconstitution du périmètre.

03. [bloqueur] **8 jours pour quatre paquets, dont le seul qui compte est impossible** — le lot 2 (1,5 jour) doit transformer « ajoute une validation d'email sur le formulaire d'inscription » en ensemble de fichiers et symboles autorisés ; c'est un problème de compréhension de code ouvert, pas une tâche d'après-midi. Pire, DAG-N-01 exige un verdict de base sans modèle : sans LLM l'extraction se réduit à des mots-clés, et « formulaire » ne mène pas à `apps/signup/Form.tsx` + `packages/validation/*`. Les 2 jours du lot 4 (rapport Markdown, HTML AA, commentaire de PR, check GitHub) sont eux-mêmes sous-estimés d'un facteur deux. · Parade : couper le périmètre v1 à ce qui est décidable sans LLM (fichiers déclarés + graphe d'imports) et le dire dès la phrase de différenciation, en déplaçant l'extraction en langage naturel au jalon de janvier.

04. [bloqueur] **Le chiffre publié n'est pas une mesure, c'est un avis déguisé** — « 6 out-of-scope » dépend entièrement d'un seuil que le cahier admet ne pas savoir placer (question ouverte 2), et la cible « ≥ 95 % sur corpus étiqueté » s'appuie sur un corpus qui n'existe pas (question ouverte 3 : « publier le corpus »). Un contre-exemple suffit à ruiner l'objectivité : la demande « ajoute une validation d'email » implique légitimement de renommer `checkInput` en `validateEmail`, donc 12 sites d'import deviennent « hors périmètre » alors qu'ils sont la conséquence directe de la demande. Quant au « temps de revue économisé estimé », c'est une estimation inventée, or la grille (critère 1) exige une suppression de perte **mesurée par l'outil à chaque exécution**. · Parade : publier l'intervalle et la règle de décision avec le chiffre, remplacer le temps économisé par une grandeur réellement observée (symboles publics cassés sans test, tests supprimés), et livrer le corpus étiqueté à deux annotateurs avec kappa de Cohen.

05. [majeur] **La vidéo contredit la grille et montre du code qui n'existera pas** — les 20 premières secondes sont portées par une voix off (« Deux minutes de revue humaine. Voici ce qui passe. ») alors que la grille impose le problème **et** le chiffre sans narration préalable ; et le plan 2:20–3:00 (comparaison de deux agents, 4 % contre 31 %) met en scène le lot 6, prévu en janvier, dans une vidéo tournée pour un gel v1 au 28 novembre. Ajoutons que 3:00 pile dépasse « moins de 3 minutes ». · Parade : ouvrir sur un plan muet du rapport chiffré plein écran, supprimer le plan comparaison ou le filmer réellement, viser 2:30.

06. [majeur] **La preuve Kiro est décorative : aucune propriété ne peut échouer** — DAG-P-01 (chaque changement reçoit une classification) et DAG-P-02 (la somme des lignes égale le total) sont des identités comptables vraies par construction ; DAG-P-05 (une diff contenue dans les fichiers déclarés ne produit aucun hors-périmètre) teste un filtre de chemins, pas la classification. Aucune ne peut trouver le moindre défaut, donc aucune ne produira le contre-exemple réel avec graine et correctif que la grille exige. Le hook `scope-guard` refuse une PR sans périmètre déclaré : c'est une politique, pas une régression bloquée, et l'agent « relecteur » qui relit le rapport n'apporte aucune mesure. · Parade : écrire une propriété sémantique falsifiable (ex. « tout symbole exporté modifié a au moins un test qui l'exerce ou un drapeau `manque` »), la faire échouer sur une vraie diff d'agent, documenter graine et correctif, et remplacer le hook par un garde qui a réellement arrêté une régression pendant la construction.

07. [majeur] **Deux semaines d'usage et tout le monde le contourne** — le destin des indicateurs de PR est connu : les équipes élargissent le périmètre déclaré jusqu'à l'absurdité (« scope: tout le dépôt ») pour obtenir le check vert, exactement comme les quality gates SonarQube et les seuils CodeClimate finissent muets ou relevés. Et la valeur s'effondre dès que l'agent devient discipliné : Claude Code avec un plan validé, Cursor avec `.cursor/rules` ou Copilot coding agent produisent déjà des diffs bornées, donc l'outil mesure un défaut en voie de disparition. · Parade : chiffrer la dérive sur un vrai historique de PR (taux de périmètres déclarés dégénérés) et montrer une valeur qui subsiste quand l'agent est sage — la preuve de non-régression (API publique cassée sans test) plutôt que le taux de hors-périmètre.

08. [bloqueur] **Angle mort : le refactoring légitime est la norme, pas l'exception** — un agent qui extrait un helper, renomme pour cohérence, met à jour 12 imports, régénère un lockfile ou déplace un fichier produit mécaniquement du « hors périmètre » ; `git diff` sans détection de renommage solide (`-M` à seuil élevé) lit un déplacement comme suppression + ajout, et la propriété DAG-P-02 devient fausse dès qu'un fichier est copié. Contre-exemple concret : `package-lock.json` ajoute 8 000 lignes pour une dépendance demandée, ce qui écrase `outOfScopeLines` et `testToCodeRatio` et rend le rapport illisible. · Parade : traiter explicitement renommages, déplacements, fichiers générés et lockfiles (règles dédiées, exclusion du comptage de lignes, détection par graphe de similarité), et publier la liste des faux positifs connus comme limite honnête.

09. [majeur] **Le jury dira « déjà vu » en trois secondes** — CodeRabbit, Greptile, Qodo `PR-Agent` et Ellipsis publient déjà des revues de PR structurées avec détection de changements non liés, GitHub Copilot code review poste des commentaires de revue automatiques, et le slogan du cahier (« read the patch before the human does ») est mot pour mot la promesse de CodeRabbit. La seule différence annoncée (« mesure, pas opinion ») repose sur le seuil arbitraire de l'objection 04, donc la phrase de différenciation d'une ligne ne résiste pas à la contradiction comme l'exige le critère 4. · Parade : nommer CodeRabbit et Qodo PR-Agent dans la fiche, exécuter l'un d'eux sur la même diff dans la vidéo, et montrer côte à côte la ligne qu'ils ne publient pas (symbole public cassé + consommateurs listés) plutôt que de revendiquer une catégorie entière.

10. [majeur] **Le jour J, la démo en direct casse par les deux bouts** — en mode « données incluses, aucun réseau » imposé par la grille, `agent-review pr` (commentaire + check rouge GitHub) ne peut pas tourner : le plan 1:40–2:20 sera un enregistrement, et un juge qui le remarque perd confiance dans le reste. En mode réel sur une diff que le jury propose, l'extraction du périmètre en langage naturel échoue publiquement (objection 03) et le verdict « sans modèle » s'effondre ; sans oublier le budget < 3 s sur 500 lignes qui saute dès qu'un lockfile ou un fichier généré entre dans la diff, ni les quatre états d'interface (vide, chargement, erreur, succès) et l'accessibilité AA qui sont difficiles à montrer dans un terminal. · Parade : construire une démo hors réseau avec un dépôt embarqué et trois scénarios fixes (diff propre, diff d'agent, diff ambiguë), afficher le rapport en HTML accessible plutôt qu'en terminal, et répéter le cas « diff inconnue » avec un repli assumé sur le périmètre déclaré.

---

# AT-07 — Attaques contre CC-07 · Bombe à cardinalité (avocat du diable)

Grille de référence : GRILLE-100.md. Dix objections, une par champ imposé (a)→(j).

01. [bloqueur] **L'antériorité est écrasante et déjà nommée à moitié** — Chronosphere Control Plane, Grafana Cloud « Cardinality Explorer » (usage insights), Datadog « tag cardinality » et `megaease/cardinal` font déjà l'analyse de cardinalité par label avec coût et ordre de suppression ; le cahier ne cite que `promtool` et la doc, ce qui est un aveu d'angle mort. Pire : tous ces outils partent de séries **réelles** dans le TSDB, là où CC-07 promet une estimation statique strictement moins fiable. · Parade : citer les quatre concurrents nommément et repositionner la différence structurelle sur « avant déploiement, sans TSDB ni compte fournisseur » — la seule case qu'ils n'occupent pas.

02. [majeur] **La réduction méprisante tient en une ligne** — « c'est un grep qui multiplie des nombres de labels et invente une facture » : le cœur (produit des cardinalités par classe heuristique) est arithmétiquement trivial, et toute la valeur perçue repose sur des heuristiques de classification qu'un juge peut qualifier de devinettes habillées en champ de mines. Le costume « démineur » renforce la suspicion de métaphore décorative, explicitement pénalisée par la grille (critère 4). · Parade : démontrer une classification non triviale (preuve par occurrence, borne inférieure/ supérieure encadrant une mesure réelle) et assumer « linter de cardinalité » comme catégorie plutôt que de la maquiller.

03. [bloqueur] **La v1 en 8 jours est un plan de 30 jours compressé** — les lots 1–4 (8 jours) doivent livrer : scan AST TypeScript, heuristiques de classification avec preuves, estimation bornée, plan de déminage, rapport HTML accessible AA vérifié par axe, mode CI bloquant, serveur MCP `estimate_metric`, hook Kiro, steering, PBT fast-check avec au moins un contre-exemple documenté, journal, comparaison chiffrée spec/vibe coding — c'est la totalité du critère 2 de la grille en plus du produit. Et le cahier promet un public « Prometheus, OTel, CloudWatch » alors que Python/Go n'arrivent qu'au lot 5 (décembre) : la v1 du concours ne couvre qu'un seul langage, donc une fraction du public annoncé. · Parade : réduire la v1 assumée à TypeScript + sortie markdown/CI, déplacer MCP et rapport HTML en stretch, et écrire la limite « un seul langage en v1 » noir sur blanc dans la fiche.

04. [bloqueur] **Le chiffre publié est un produit supérieur sans signification économique** — estimer 480 000 séries en multipliant les cardinalités par label suppose que toutes les combinaisons existent, ce qui est faux en pratique (la plupart des couples `user_id × path` ne se produisent jamais) ; le chiffre réel peut être 10 à 100 fois inférieur, donc le « coût mensuel estimé » et le « −99,7 % » du plan de déminage sont gonflés d'autant. La grille (critère 1) exige une perte chiffrée **avec source ou méthode de mesure** : « cette ligne coûte 400 € par mois » n'a ici ni mesure ni tarif réel, seulement un tarif « fourni par l'utilisateur » multiplié par une borne supérieure. · Parade : publier systématiquement l'intervalle [borne inf., borne sup.] avec le ratio réel mesuré sur au moins trois dépôts open source instrumentés, et retirer tout chiffre en euros non adossé à un tarif public daté.

05. [majeur] **La vidéo prouve uniquement ce que l'auteur a planté** — le scénario 0:00–3:00 tourne sur un dépôt de fixtures dont les trois bombes ont été écrites par l'équipe : « 100 % de bombes détectées sur le corpus » est une tautologie, et un juge le sentira dès que la voix off annonce un coût jamais facturé. Les 15 premières secondes montrent `counter.inc({ user_id })` puis une affirmation chiffrée non prouvée, exactement le « décrit au lieu de prouver » pénalisé par le critère 5. · Parade : inclure dans la vidéo un scan **non monté** d'un dépôt réel connu (ex. un service OTel open source) avec l'écart estimation/mesure affiché à l'écran.

06. [mineur] **Le récit Kiro est auto-référentiel** — le hook `cardinality-guard` surveille les fichiers d'instrumentation… du projet qui détecte l'instrumentation, et le contre-exemple PBT annoncé (« retirer un label augmentait les séries ») ressemble à un cas synthétique fabriqué pour cocher la case « au moins un défaut trouvé ». La comparaison spec/vibe coding sur des heuristiques de classification sera difficile à rendre honnête, car il n'existe pas de référence objective pour trancher laquelle des deux approches classe mieux. · Parade : faire tourner le hook et le scan sur un vrai dépôt tiers instrumenté intégré comme fixture, et choisir pour la comparaison spec/vibe une fonction à contrat vérifiable (ex. le calcul de bornes) plutôt que les heuristiques.

07. [bloqueur] **Le public est une niche, pas « la quasi-totalité des développeurs »** — la majorité des développeurs n'expose aucune métrique Prometheus/OTel ; ceux qui le font sont des équipes platform/SRE déjà équipées de Grafana Cloud, Datadog ou Chronosphere, c'est-à-dire des outils qui mesurent la cardinalité réelle en continu. Le critère 1 de la grille exige un problème « vécu ce mois-ci » par la quasi-totalité du public visé : ici le problème est vécu par les opérateurs, pas par le développeur qui écrit la ligne, et il est déjà couvert côté opérateur. · Parade : cibler explicitement les développeurs **avant** qu'ils aient un backend de métriques (CI comme premier filet) et chiffrer l'audience réelle (nombre de dépôts GitHub avec instrumentation Prometheus/OTel) plutôt que « les développeurs ».

08. [bloqueur] **L'angle mort technique invalide la promesse « depuis le code »** — la cardinalité finale d'une série se décide largement hors du code applicatif : `relabel_configs` et `metric_relabel_configs` du scrape, labels injectés par le service discovery Kubernetes (`pod`, `namespace`, `container`, `instance`), attributs de ressource OTel et surtout labels ajoutés par les bibliothèques d'auto-instrumentation (`http.route`, `http.response.status_code`, `net.peer.ip`) qui n'apparaissent jamais dans le dépôt scanné. Contre-exemple concret : l'incident Roblox d'octobre 2021 (73 h d'indisponibilité) venait de métriques Consul émises par l'infrastructure, pas par une ligne de code métier — un scan statique du code ne l'aurait pas vu. · Parade : analyser aussi la configuration Prometheus/OTel Collector (fichiers de scrape et pipelines) en v1, et écrire dans la limite honnête que les labels d'auto-instrumentation ne sont couverts que via une base de connaissances des bibliothèques.

09. [majeur] **Le jury dira « déjà vu » dès l'accroche** — la bombe à cardinalité est le marronnier documenté du secteur depuis Roblox : blogs Grafana et Datadog, talk « cardinality is the root of all evil », et chaque hackathon observabilité produit son linter de labels ; la phrase « reads your code and tells you which ones are lit » ne résiste pas à la contradiction puisque Chronosphere le fait en temps réel sur données réelles. Le critère 4 exige qu'aucun outil existant ne fasse ça : or « estimer la cardinalité depuis le code » se rapproche de ce que font déjà les règles de linting OTel et les validateurs de `relabel_config`. · Parade : déplacer la différenciation sur l'artefact que personne n'a — l'**ordre de déminage chiffré avec bornes et preuves par occurrence**, testable par propriétés — et non sur la détection.

10. [majeur] **Le jour de la démo en direct, trois choses cassent** — (1) un juge lance le scan sur son propre dépôt : s'il est en Go/Python (majoritaire chez les exposants de métriques), la v1 ne trouve rien et affiche l'état vide ; (2) sur un dépôt réel non instrumenté ou instrumenté via un framework, le rapport sort « 0 bombe » et la démo devient muette ; (3) le mode démo hors réseau exige des données incluses, mais le coût mensuel dépend d'un tarif « fourni par l'utilisateur », donc absent ou inventé en direct. Sans compter le seuil des < 20 s sur 50 000 lignes à tenir sur la machine du stand. · Parade : embarquer trois dépôts réels pré-analysés (TS, Go, Python via résultats figés clairement étiquetés) et un mode démo avec tarif public daté inclus, vérifié sur la machine de secours avant le gel.

---

# AT-08 — Attaque de CC-08 « Plongée / Tail » (avocat du diable)

Objectif : faire perdre cette idée au concours. Dix objections, une par champ imposé.
Verdict d'ensemble : un outil juste, mais un pitch de talk de 2013 habillé en produit — le jury le sentira.

01. [bloqueur] **L'antériorité est écrasante et déjà open source** — `goaccess` lit un access.log brut, sans agent, et publie p50/p90/p99 par URL dans un rapport HTML statique depuis des années ; Loki + `quantile_over_time` et Datadog Watchdog font la « décomposition des lents » en production, et le talk de Gil Tene « How NOT to Measure Latency » (2013) + HDRHistogram ont déjà installé le récit « la moyenne ment ». Ce que Tail ajoute — deux modes détectés, un test de fenêtre — est une couche statistique fine sur un produit existant. · Parade : assumer goaccess comme concurrent nommé et déplacer la promesse sur la comparaison de distributions avant/après avec effet mesuré, seule chose qu'aucun des trois ne fait.

02. [majeur] **La réduction « script awk avec des percentiles » tient debout** — `awk '{print $NF}' access.log | sort -n | sed -n "$((99*$(wc -l < access.log)/100))p"` donne le p99 exact en une ligne ; le group-by dimensionnel, c'est `sort | uniq -c`. Tout le lot 2 (2,5 jours pour « histogramme exact + percentiles ») est trivial en mémoire : 1 M de flottants = 8 Mo, on trie et on indexe. Il faut que le cœur de valeur soit ailleurs que le percentile. · Parade : faire de la détection de bimodalité et du test de fenêtre le produit, et montrer en démo l'échec explicite de la ligne awk (logs désordonnés, champs manquants, durées hétérogènes).

03. [bloqueur] **La v1 en 8 jours-agent est une fiction** — le plan promet 4 paquets (~3 700 lignes), 3 parseurs + schéma déclaré, détection de modes (un problème de KDE/dip-test, pas un tri), test de différence de distribution avec effect size, rapport HTML accessible AA avec équivalent textuel de chaque figure, un serveur MCP, le CLI, 5 propriétés PBT avec graines, les fixtures étiquetées à 95 % de rappel, le journal Kiro, la comparaison spec/vibe chiffrée ET la vidéo. Le lot 4 seul (comparaison + rapport, 1,5 jour) en mange 3 dès qu'on touche l'accessibilité. · Parade : couper la détection de modes et le MCP de la v1, garder analyze + compare + rapport texte ; le HTML devient un lot de décembre.

04. [majeur] **La « décomposition causale » est une corrélation, et le cahier se contredit** — O2 promet « décomposition causale sans agent » alors que le risque 12.3 jure « jamais le mot cause » ; sur l'exemple vidéo, `version=v2.14` et `route=/search` sont probablement la base rate du trafic (si v2.14 sert 78 % des requêtes, le chiffre ne dit rien). Sans groupe témoin ni normalisation par le volume de chaque dimension, on tombe en plein paradoxe de Simpson, et PLG-P-04 (« 100 % des lentes attribuées à des dimensions existantes ») est une tautologie : tout enregistrement a des dimensions. · Parade : publier un lift (part des lentes ÷ part du trafic global par valeur de dimension) et renommer l'objectif O2 « attribution par association, jamais causale ».

05. [majeur] **La vidéo démontre un meurtre dont l'équipe est l'auteur** — les fixtures sont synthétiques : c'est le candidat qui a injecté le pic `v2.14` sur `/search`, donc la « découverte » à 1:00–1:50 est circulaire, et le tableau de bord « 84 ms » des 15 premières secondes est une maquette, pas un vrai Grafana. Le jury Devpost a vu cinquante démos sur données fabriquées ; rien ici ne prouve que l'outil survit à un log qu'il n'a pas écrit. · Parade : un plan sur un vrai log public (dataset HTTP de Wikipedia/Alibaba cluster trace) non retouché, avec le résultat brut, même imparfait.

06. [majeur] **Le récit Kiro est décoratif** — PLG-P-01 (« p99 égale la valeur théorique ») teste surtout la convention de quantile choisie (R-7 vs R-8, interpolation ou non) : la propriété « échouera » à la première définition ambiguë, ce qui fabrique un faux contre-exemple de journal ; et PLG-P-02 (invariance d'ordre) est vraie par construction pour un histogramme trié — le « contre-exemple trouvé par PBT » promis au journal sera soit trivial, soit écrit après coup, exactement ce que la grille §2 sanctionne. Le hook `stats-exactness` qui rejoue des fixtures est un test CI banal, pas « un hook qui a vraiment bloqué une régression ». · Parade : choisir une propriété non triviale (PLG-P-03 faux positifs de changement sur fenêtres glissantes, avec graines et échec documenté en cours de construction) et raconter l'incident daté dans le journal.

07. [majeur] **Personne n'analyse ses logs à la main en 2026** — les équipes qui ont un p99 à 4,2 s et une culture SLO ont déjà Prometheus + Grafana ou un APM (Datadog, Grafana Cloud) ; celles qui n'ont qu'un fichier de log brut sont trop petites pour souffrir de la queue de latence, et leur « perte chiffrée » (grille §1 : vécue ce mois-ci, mesurée) est introuvable. Le public nommé, « équipes qui se fient à une moyenne », est un repoussoir rhétorique, pas un utilisateur avec un rôle et un contexte. · Parade : cibler précisément les équipes auto-hébergées/sans APM pour raisons de coût ou de confidentialité (PLG-N-01 devient l'argument n° 1) et chiffrer la perte sur un cas réel daté.

08. [bloqueur] **Les logs réels ne contiennent pas ce que l'outil suppose** — le format nginx combined n'a ni durée ni identifiant de corrélation par défaut (il faut configurer `$request_time`), `request_time` et `upstream_response_time` ne mesurent pas la même chose, Apache, HAProxy, les logs JSON applicatifs et CloudFront ont chacun leur sémantique ; les requêtes annulées (499) disparaissent précisément quand elles sont lentes, biaisant la queue qu'on veut mesurer. Avec « 3 parseurs courants + schéma déclaré », la première exécution sur le log d'un juge produit soit une erreur, soit des percentiles faussement confiants — pire que rien. · Parade : une étape obligatoire de « contrat de champ » qui fait dire à l'outil ce qu'il a compris (unité, horloge, couverture des statuts) et un état d'erreur riche quand la durée manque ou que les annulées sont absentes.

09. [bloqueur] **Le jury dira « déjà vu » avant la deuxième minute** — l'accroche « Your dashboard says 84 ms. Your users say otherwise. » est la diapositive d'ouverture de chaque talk sur la latence depuis treize ans (Tene 2013, les SLO de Google SRE Book chapitre 4), la catégorie Frankenstein n'est pas exploitée — « plongée × queue de distribution » est une métaphore décorative, le costume que la grille §4 pénalise — et le concurrent nommé (APM/Prometheus) est battu sur un critère cosmétique (local, pas d'agent) plutôt que structurel. Il ne reste que le test de différence de distribution entre fenêtres, qui tient en une phrase et ne remplit pas une vidéo de 3 minutes. · Parade : faire du test statistique honnête (effet mesuré, faux positifs bornés, PLG-P-03) LA ligne de différenciation, et supprimer la métaphore sous-marine ou la rendre fonctionnelle (profondeur = rang dans la queue, affiché).

10. [mineur] **Le jour de la démo en direct, tout vient du fichier qu'on vous tend** — si un juge lance `tail analyze` sur son propre log, le schéma déclaré transforme la démo en séance de configuration ; sur données inattendues (durées négatives ou en secondes mélangées à des millisecondes, horodatages multi-fuseaux, NaN, log multi-lignes) les cas limites non spécifiés dans les exigences produisent un crash ou un p99 absurde publié avec aplomb. Le « mode démonstration qui ne peut pas échouer » (grille §3) existe peut-être, mais la démo live sur log inconnu est le seul moment où le juge teste vraiment l'outil. · Parade : un `tail doctor` qui valide le log avant analyse et refuse de publier un chiffre tant que l'unité et le fuseau ne sont pas confirmés — l'échec élégant devient la preuve de rigueur.

## Synthèse pour le parent
Trois bloqueurs (01 antériorité goaccess, 03 périmètre 8 jours, 08 hétérogénéité des logs) + un quasi-bloqueur (09 « déjà vu »).
L'idée n'est sauvable qu'en rétrécissant : analyze+compare sur schéma validé, test de distribution comme seule promesse, fixtures réelles publiques.

---

# AT-09 — Attaques : Restore Drill (CC-09)

10 objections, avocat du diable. But : faire perdre cette idée.

01. [bloqueur] **L'antériorité est accablante** — `restic check --read-data` lit déjà tous les paquets et reconstitue les fichiers, `borg check --verify-data` fait exactement la comparaison d'empreintes revendiquée, et Veeam/Acronis vendent des « SureBackup »/« Instant Verification » qui restaurent réellement en bac à sable et publient un rapport daté depuis plus de dix ans. Restore Drill n'est que la juxtaposition de mécanismes existants, sans aucune garantie nouvelle : la grille exige une différence **structurelle**, ici elle est cosmétique (un wrapper multi-sources autour de vérifications déjà faites par les sources elles-mêmes). · Parade : cibler précisément ce que `restic check` ne fait PAS (ouvrir et décoder les fichiers témoins, verdict unifié multi-sources rejoué en CI) et le démontrer par une comparaison chiffrée côte à côte dans la fiche.

02. [majeur] **La réduction méprisante est prête** — « c'est un script shell de 30 lignes : `tar -x` dans un tmpdir, `sha256sum -c`, `echo fail` » — et honnêtement, la v1 gelée au 28 nov. est exactement ça, puisque les adaptateurs `restic`/`borg` (la seule partie intéressante) sont repoussés au lot 5 en décembre. Un juge technique qui lit le plan de réalisation verra que la v1 ne restaure que des dossiers et des tar, ce qu'aucun jury ne peut appeler innovation. · Parade : amener au moins l'adaptateur `restic` dans la v1 et montrer le manifeste + garde d'écriture comme la vraie valeur (le shell script n'a ni bac à sable prouvé, ni historique, ni verdict signé).

03. [bloqueur] **La v1 en 8 jours est intenable, et le plan le trahit** — le cahier annonce 8 jours-agent pour la v1 mais le tableau des lots en additionne 8 pour les seuls lots 1–4, sans le corpus de fixtures corrompues, sans le rapport accessible AA, sans la démo CI, sans les specs EARS/PBT/hooks Kiro exigés par la grille. Pire : la propriété RES-P-01 (« aucune écriture hors du bac à sable, vérifiée par trace système ») demande un audit syscall (strace/fanotify/landlock) qui à lui seul peut manger 3 jours, et sans lui le « 0 écriture hors sandbox » est une affirmation, pas une preuve. · Parade : réduire la v1 à `tar` + `directory` + garde par `landlock` ou chroot simple, tracer RES-P-01 par audit du FS (diff avant/après) plutôt que par syscall, et assumer 6 jours au lieu de 8 avec un périmètre écrit noir sur blanc.

04. [majeur] **Le chiffre mesuré ne prouve rien d'utile** — « 1 204 fichiers restaurés, 11 témoins vérifiés, 38 secondes » : ce sont des compteurs d'activité, pas une réduction de perte chiffrée comme l'exige le critère Impact (minutes ou euros perdus aujourd'hui, mesurés à chaque exécution). Le seul chiffre opposable serait « probabilité que votre sauvegarde soit restaurable » et l'outil ne peut pas la calculer : un exercice qui passe sur 11 témoins choisis par l'utilisateur ne dit rien des 1 193 autres fichiers ni de la restauration complète. · Parade : publier à chaque exécution l'écart au budget déclaré et l'âge du dernier exercice réussi (« votre sauvegarde n'a pas été prouvée depuis N jours »), chiffre d'alerte actionnable, et écrire la limite honnête sur l'échantillonnage.

05. [majeur] **La démo vidéo est un théâtre de fixtures** — tout se joue sur des archives de test avec corruptions semées à des positions connues (section 9) : le juge comprendra en 20 secondes que « l'archive de trois mois » de 0:00–0:20 est fabriquée pour l'occasion, puisque l'outil n'a jamais touché une vraie sauvegarde d'équipe. Le verdict `fail` puis `pass` après « réparation » montre seulement que l'outil sait lire un sha256 fourni dans le manifeste — la boucle du spectacle est écrite d'avance. · Parade : faire au moins un exercice réel et documenté (vraie sauvegarde restic du dépôt du projet, anonymisée, avec consentement) dans la vidéo, et montrer une corruption naturelle (bit-rot ou snapshot incomplet) plutôt que semée.

06. [majeur] **Le récit d'usage de Kiro est plaqué** — « une spec par adaptateur » mais la v1 n'a que deux adaptateurs triviaux ; la comparaison spec/vibe coding est prévue sur l'adaptateur `restic`… qui n'existe pas avant décembre : la preuve Kiro centrale sera donc soit fausse, soit écrite après coup, exactement ce que la grille punit. Le hook `sandbox-guard` (« tout test doit déclarer son bac à sable ») est décoratif : il valide un champ obligatoire d'un type TypeScript, il ne peut pas « vraiment bloquer une régression » de manière spectaculaire. · Parade : déplacer la comparaison spec/vibe sur la garde d'écriture (vrai sujet de sûreté, en EARS), et concevoir un hook qui bloque réellement — par exemple interdiction d'exécuter un test qui monte un volume ou touche `$HOME`.

07. [bloqueur] **Le jury n'a pas de sauvegardes à tester** — les juges et le public Devpost sont des développeurs dont la « sauvegarde » c'est GitHub, Time Machine en fond, ou un snapshot SaaS : aucun ne vit ce mois-ci la perte décrite (disque qui lâche + archive corrompue), et aucun n'exécutera un exercice de restauration sur ses propres données pendant le jugement. Le critère Impact exige un problème vécu ce mois-ci par la quasi-totalité du public visé ; ici le public réel (équipes avec restic/borg et obligations de conformité) est absent du jury, et la démo en ligne « sans compte ni installation » est impossible — on ne restaure pas une archive de 2 Go dans un navigateur en 30 secondes. · Parade : recadrer sur les données que les devs sauvegardent vraiment (bases locales, `.env`, media projects) et fournir une démo web avec une micro-archive embarquée qui rejoue un verdict réel pré-calculé.

08. [majeur] **L'angle mort technique ruine la promesse** — les vraies restaurations qui échouent ne sont pas des fichiers corrompus mais des états vivants : base PostgreSQL restaurée sans cohérence transactionnelle, permissions/ACL perdues, volumes Docker et montages réseaux introuvables, chemins absolus codés en dur. Le cahier exclut explicitement bases managées (v1) et PRA, donc l'outil prouve précisément la classe de problèmes la plus facile (fichiers plats intègres) et se tait sur celle qui tue réellement les restaurations. Un juge DBA dira : « restaurer un dump SQL et l'ouvrir, ça ne prouve pas qu'il se charge ». · Parade : ajouter dès la v1 un témoin « ouvrable par son application » (ex. `sqlite3 file . integrity_check` ou `pg_restore --list`) — prouver que le fichier est utilisable, pas seulement lisible.

09. [mineur] **Le « déjà vu » guette en catégorie Frankenstein** — la métaphore exercice d'évacuation incendie × sauvegarde est celle de Veeam SureBackup marketing depuis des années (« your backup is only as good as your restore » est un slogan usé jusqu'à la corde), et les Devpost regorgent d'outils « backup verifier » en CI. La combinaison « technologie morte × problème d'agent » exigée par la grille est faible : rien ici n'implique d'agent ni d'IA, le MCP `run_drill` est un gadget sans bénéfice mesurable. · Parade : revendiquer l'antériorité Veeam dans la fiche (concurrent nommé, différence = open source, multi-sources, local-first, CI natif) et supprimer le MCP s'il n'apporte pas un chiffre.

10. [bloqueur] **Le jour de la démo en direct, le risque est de toucher une vraie source** — la démonstration exige par construction d'accéder à de vraies archives ; si le stand ou la vidéo en direct branche un dépôt restic/borg réel, le moindre chemin mal déclaré écrit hors du bac à sable devant le jury — et l'outil dont la promesse unique est « 0 écriture hors sandbox » n'a pas encore la garde prouvée en v1 (voir objection 03). Un seul `tar -x -P` avec chemin absolu dans une fixture suffit à extraire dans `/` : le scénario catastrophe du projet EST son scénario de démo. · Parade : démo en direct exclusivement sur fixtures embarquées read-only, source montée en lecture seule au niveau OS, et la garde d'écriture démontrée AVANT toute restauration (trace affichée à l'écran).

---

# AT-10 — Attaques contre CC-10 « Caractérisation » (CTA)

Adversaire : avocat du diable. Objectif : faire perdre cette idée au concours. 10 objections, une par champ imposé.

01. [bloqueur] **L'antériorité est dans le titre même** — « Characterization test » n'est pas un concept de 2026 : c'est le chapitre 13 de *Working Effectively with Legacy Code* (Michael Feathers, 2004), et le record/replay au niveau fonction existe en production depuis **VCR/vcrpy** (cassettes Ruby/Python), **Polly.js** et **nock-recorder** : on enregistre le réel, on le rejoue, on hurle à la dérive. Un juge qui connaît Feathers ne voit qu'un nom de livre recyclé en produit. · Parade : assumer l'héritage en une ligne et déplacer la nouveauté sur ce que ni Feathers ni vcrpy ne font (le compteur de chemins observés + la sensibilité mesurée), puis renommer l'outil pour qu'il ne s'appelle pas comme le chapitre.

02. [bloqueur] **« C'est un snapshot test à l'échelle du module »** — la réduction tient en 30 lignes de code : `for (const f of corpus) expect(parse(f)).toMatchSnapshot()`. Jest fait exactement ça, **Approval Tests** d'Emily Bache et le **Golden Master** le théorisent depuis quinze ans, et `jest --ci` refuse déjà toute dérive non approuvée. Le tableau « Ce qui existe déjà » du cahier écarte Jest d'un revers (« suppose un test écrit à la main »), ce qui est faux : une boucle sur un dossier de corpus est un test écrit à la main de dix lignes. · Parade : prouver en direct que la boucle-snapshot échoue là où CTA réussit (sortie non sérialisable, exception, chemin non couvert), et filmer cet échec — sinon la différence reste cosmétique au sens de la grille §4.

03. [bloqueur] **La v1 en 9 jours repose sur une instrumentation qui n'existe pas** — `withRecorder(fn)` « sans patcher le source » exige quand même de connaître le point d'appel et de l'éditer : les appels *internes* du parseur (`matchBrace`, `assignEmpty`) ne passent jamais par le proxy, donc le `pathLabel` promis ne peut pas venir de là. Or V8 coverage ne rend que des plages d'octets, pas des noms de branches : le mapping `parseIni>matchBrace>assignEmpty` est un projet à lui seul, et il faut en plus écrire à la main les deux adaptateurs de 250 lignes et le « legacy » de 3 200 lignes qui n'existe nulle part. · Parade : réduire la v1 à la seule frontière publique du module (une fonction exportée, entrées/sorties, zéro pathLabel), et livrer le pathLabel en L6 avec une méthode écrite et vérifiable.

04. [majeur] **Les chiffres sont auto-attribués, et l'un d'eux est une tautologie** — O3 exige C ≥ 95 % « des chemins observés », mais la suite est *générée depuis* ces mêmes chemins observés : C = 100 % par construction, et la recette V5 l'écrit noir sur blanc. Un indicateur qui ne peut pas échouer ne mesure rien, et la grille §1 exige une perte *supprimée* et mesurée, pas un compteur décoratif. Côté mutants, les 50 mutants sont choisis par l'outil, injectés dans un module écrit par l'équipe : 92 % de détection sur ses propres mutants, c'est une note qu'on se donne. · Parade : publier un chiffre qui peut rater (C mesuré sur un corpus *étranger*, taux de mutants équivalents survivants, mutants tiers type Stryker), et supprimer O3 ou le reformuler en « chemins du module non observés ».

05. [majeur] **La vidéo démontre un test unitaire qui passe** — le climax (1:20–1:55) consiste à changer `+` en `-` dans un moteur de prix *écrit par l'équipe* puis à voir D = 1 : n'importe quelle suite de tests attrape ça, et le juge ne voit ni le parseur de 2016, ni les 4 jours de détection tardive, ni les 1 800 € de rollback du §2. Pire, les 15 premières secondes exigées par la grille §5 (« le problème **et** le chiffre ») montrent un dépôt et `0 tests` — aucun chiffre. · Parade : ouvrir sur le chiffre réel (11 % de lignes à `0000-00-00`, 1 800 €, 4 jours) et faire de la dérive un vrai refactor de 40 lignes dont seul CTA attrape l'effet, pas une mutation d'opérateur.

06. [majeur] **Le récit « deux applications éloignées » ne tient pas, et la preuve Kiro est post-hoc** — un parseur de fichiers et un moteur de prix, tous deux en TypeScript, tous deux fonctions pures, tous deux dans `examples/`, écrits par le même auteur à trois jours d'intervalle, ne sont pas « far apart » : ce sont deux fixtures du même harnais, et la catégorie Skeleton Crew attend un squelette transplanté dans des mondes réellement distincts. Côté Kiro, les hooks annoncés sont `wc -l`, `lint` et un grep sur `http` — décoratifs, alors que la grille §2 exige un hook qui a *vraiment bloqué* une régression ; et le lot L9 (specs, steering, hooks, agents, powers) est planifié **après** L8, soit un journal écrit après coup, le défaut explicitement pénalisé. · Parade : remplacer une des deux applications par un corps étranger réel (un vrai module npm abandonné, ou un langage/paradigme différent) et avancer L9 en L1 pour que le hook bloquant soit daté avant la v1.

07. [majeur] **Dans six mois, personne ne le branche en CI** — 1 042 assertions générées, c'est 1 042 triages humains à la première dérive : dès qu'une sortie dépend de l'horloge, d'un flottant, d'un ordre de clés de `Map` ou d'un objet mutable aliasé, la suite devient flaky, l'équipe met `--threshold-drift 999` et l'outil meurt (le R5 du cahier admet « probabilité élevée, impact élevé »). Le périmètre Node/TS exclut l'essentiel du legacy réel — Java, .NET, PHP, COBOL — et l'alternative gagnante en 2027 est triviale : demander à Kiro ou Copilot d'écrire les tests du module, ce qui produit de la compréhension en plus du filet. · Parade : cibler un écosystème où le legacy est massif et l'offre faible, et prouver la stabilité sur 200 exécutions consécutives sans faux positif publiée dans le README.

08. [bloqueur] **L'angle mort est exactement l'incident raconté** — le proxy capture l'entrée, la sortie et l'exception : jamais les effets de bord. Un refactor qui cesse d'écrire le fichier de log, saute un `INSERT` ou n'émet plus l'événement passe à D = 0 en vert, alors que le §2 décrit précisément une perte de donnée en production ; et les entrées non capturables (stream, handle, `this`, closure, tampon mutable modifié après l'appel) rendent le rejeu infidèle sans avertissement. Côté bugs figés, `test.fails` de Vitest *passe* quand le test échoue : le jour où le `known-bug` LEGACY-42 est corrigé, la suite redevient rouge pour une bonne nouvelle, et le label dépend d'une décision humaine non tranchée (arbitrage n° 5). · Parade : documenter la limite en page 1 du README (« ne prouve pas les effets de bord »), capturer un canal effets de bord injectable (fs/clock/émetteur espionnés), et rendre la correction d'un `known-bug` explicitement attendue plutôt que rouge.

09. [mineur] **« Déjà vu » garanti, et aucun costume** — le pipeline INSTRUMENT → RECORDER → GENERATE → COMPARE ressemble à s'y méprendre à un enchaînement d'outils existants (jest-snapshot, Approval Tests, Stryker) et le rendu est une sortie terminal plus un rapport HTML : dans une édition Kiroween où la catégorie Skeleton Crew promet un squelette *visible*, un CLI qui affiche trois compteurs ne donne au juge aucune image à retenir ni aucune seconde de surprise. · Parade : une identité visuelle forte (le squelette qui se fige autour du module, animation des chemins observés) et une accroche qui ne soit pas une reformulation de Feathers.

10. [bloqueur] **En démo directe, ça casse à la première commande du juge** — il n'y a pas d'instrumentation générique : `cta capture --module <m>` suppose un adaptateur dédié (R1 du cahier, et `src/adapters/legacy-file-parser`), donc « essayez sur votre code » échoue immédiatement ; la démo en ligne < 30 s sans installation exigée par la grille §5 est impossible pour un CLI Node qui a besoin d'un corpus et de `npx` ; `unshare -n` (V11) n'existe pas dans un navigateur ; et V4 admet jusqu'à 60 s pour 1 042 tests — un trou d'air d'une minute en direct, suivi de `cta mutate` qui rejoue 50 fois la suite, tue les 3 minutes. · Parade : un mode démo figé (corpus embarqué, résultats pré-calculés, `--max-cases 50`) qui ne peut pas échouer au sens de la grille §3, plus une cible web où un module de démonstration est réellement capturé sans adaptateur.

---

# AT-11 — Graphmantle (Skeleton Crew, 90/100) — attaque avocat du diable

01. [bloqueur] **L'antériorité est massive et commerciale** — « Cette CVE est-elle atteignable chez moi ? » est déjà vendu par JFrog Xray Contextual Analysis, Endor Labs Reachability et Snyk Reachability ; Eclipse Steady (ex-VULAS, SAP) le faisait en 2017 et osv-scanner a un mode expérimental « callgraph » (Soot pour Java, PoC Python). La grille exige qu'« aucun outil existant ne fait ça » : ici trois éditeurs en vivent. · Parade : se différencier structurellement (preuve vérifiable par le juge, chemin citable ligne à ligne, VEX signé en sortie) et nommer ces concurrents dans la fiche avant que le jury ne le fasse.

02. [majeur] **La réduction méprisante tient en une ligne** — « C'est `madge` collé à `osv-scanner` avec un joli graphe en sortie » : un wrapper qui parse, construit un graphe de dépendances d'appels et affiche un compteur, sans moteur propriétaire. Un juge qui connaît npm audit + un visualiseur de graphe classera ça en « déjà fait le week-end ». · Parade : publier l'invariant non trivial (complétude du graphe sur les callbacks/async) et une propriété fast-check qui a vraiment échoué, pour montrer un noyau et non un collage.

03. [bloqueur] **9 jours pour deux frontends inter-procédures fiables, c'est intenable** — Un call graph TS doit résoudre les types, les generics et surtout le code **compilé/minifié** publié sur npm (la plupart des paquets livrent du dist JS, pas le TS) ; côté Python il faut gérer importlib, décorateurs et resolution d'attributs. Pire : aucune base publique ne mappe CVE → **symbole** vulnérable (OSV donne des plages de versions, pas des noms de fonctions) — sans cette donnée, l'analyse ne démarre même pas. · Parade : restreindre la v1 à un langage et à un corpus de ~20 CVE mappées à la main (documenté), ou utiliser CodeQL/Semgrep comme moteur et se concentrer sur le chemin et le chiffre.

04. [majeur] **Le chiffre publié est invérifiable et son faux négatif est une faute grave** — Dire « 42 CVE publiées, 3 atteignables » sans ground truth (un PoC par CVE) n'est qu'une assertion ; et si l'outil déclare « non atteignable » à tort, le développeur laisse un trou exploitable — aucun RSSI n'acceptera ce verdict, d'où l'existence du format VEX justement pour encadrer cette prétention. · Parade : publier le taux avec la méthode de validation (échantillon vérifié à la main + faux négatifs documentés) et formuler la sortie comme un VEX « needs review », jamais comme un feu vert.

05. [mineur] **La vidéo sera ennuyeuse et infalsifiable** — Les 15 premières secondes montrent… un parseur qui tourne puis un nombre, que le juge ne peut pas distinguer d'un `print(3)` codé en dur ; construire un graphe n'a aucune tension visuelle. · Parade : ouvrir sur une vraie CVE du mois sur un repo connu, écran scindé avant/après (npm audit : 42 alertes ; Graphmantle : 3 chemins cliquables jusqu'à la route HTTP), avec la commande visible à l'écran.

06. [majeur] **Les deux applications ne sont pas « éloignées » et le noyau partagé est un mythe** — TypeScript/npm et Python/PyPI sont deux langages dynamiques à gestionnaire de paquets, même forme exacte ; un juge dira « le même démo deux fois ». Et le « noyau d'atteignabilité » ne partage rien de substantiel : les parsers, la résolution d'appels et le mapping de symboles sont spécifiques à chaque langage — ce qui contredit le récit Skeleton Crew (peu de code, beaucoup de squelette commun). · Parade : mesurer et afficher le pourcentage de lignes réellement partagées, ou remplacer la 2e app par un vrai éloignement (binaire Go/Rust, ou un monorepo avec appels RPC).

07. [majeur] **L'impact réel est douteux : la réponse n'est pas actionnable** — Même « non atteignable », la conformité (ISO 27001, clients entreprise, scanners du CI) exige de patcher ou de justifier par un VEX revu par un humain ; l'équipe sécurité qui reçoit « 3/42 » doit quand même traiter les 42. Le gain annoncé (ignorer 93 % des CVE) est exactement celui que JFrog vend déjà aux entreprises — un dev solo, lui, n'a pas le droit d'ignorer. · Parade : faire produire à l'outil le VEX/justification conforme directement consommable par osv-scanner/Snyk, et chiffrer le temps de rédaction de VEX économisé plutôt que les CVE « ignorées ».

08. [bloqueur] **L'angle mort technique invalide le chiffre : sondeur contre sous-approximation** — Node est saturé d'EventEmitter (`emit`/`on` casse tout chemin statique), de callbacks promisifiés, de DI (NestJS, Angular) et de `require(variable)` ; Python a getattr, monkey-patching et les métaclasses. Un graphe **sûr** (sur-approximé) rend tout atteignable et le chiffre s'effondre à 42/42 — inutile ; un graphe précis sous-approxime et produit les faux négatifs mortels du point 04. · Parade : borner honnêtement la garantie (« atteignabilité directe + callbacks résolus par convention X »), tracer chaque arête non résolue dans le rapport, et le dire dans la limite honnête de la fiche.

09. [majeur] **Le jury dira « déjà vu » avant la fin de la vidéo** — Entre le battage JFrog Contextual Analysis, les VEX de l'OpenSSF et les projets Devpost des éditions précédentes sur « reachability + CodeQL », l'espace est saturé de demos de graphe d'appel ; « CVE + call graph » est le sujet de stage classique de la sécurité applicative. · Parade : déplacer le pitch sur l'artefact unique (chemin d'exploitation reproductible, exportable, testé) plutôt que sur la question « atteignable ou pas », déjà possédée par le marché.

10. [majeur] **Le jour J, la démo casse sur le réseau ou sur un dist minifié** — La grille impose un mode démo sans réseau, mais une CVE crédible « de ce mois-ci » exige l'API OSV en direct ; et il suffit d'une dépendance qui ne livre que du JS bundlé/minifié (ou d'un `export default` ré-exporté) pour que le graphe se vide devant le juge. Le parse d'un vrai repo dépasse facilement les 30 secondes imposées. · Parade : jeu de données figé et pré-calculé dans le repo (snapshot OSV daté + cache du graphe), avec un bouton « données live » optionnel, et un chronomètre affiché prouvant le < 30 s.

---

# AT-12-shrink — avocat du diable (Shrink, Resurrection, 89/100)

01. [bloqueur] **Antériorité massive : tout existe déjà** — C-Reduce, `afl-tmin`, `cvt`, le minimiseur de libFuzzer (`-minimize_crash=1`) et surtout **Hypothesis**, dont le shrinking automatique est une fonctionnalité phare depuis 2014, couvrent exactement le périmètre annoncé. La grille innovation (20/20) exige « aucun outil existant ne fait ça » avec concurrent nommé et différence *structurelle* : Shrink est un ddmin générique de plus, sans mécanisme nouveau. · Parade : trouver une garantie qu'aucun réducteur n'offre (ex. preuve formelle d'équivalence d'erreur par hachage du message + de la trace), et nommer Hypothesis/libFuzzer comme concurrents battus sur cette garantie précise.

02. [bloqueur] **« C'est ddmin, un algorithme de 2002 »** — ddmin (Zeller, ISSTA 2002) tient en ~80 lignes ; un juge technique écrase l'innovation en une phrase, et la grille punit explicitement le « wrapper autour d'un outil existant ». Le budget de 32 jours pour un algorithme publié il y a 24 ans paraît disproportionné et se retourne contre l'équipe. · Parade : ne pas vendre l'algorithme mais le système autour (oracle fiable, cache d'exécutions, réduction parallèle, rapport diffable) et le chiffrer en complexité réellement nouvelle.

03. [majeur] **9 jours de v1 irréalistes pour la fiabilité** — ddmin est trivial en démonstration, mais la robustesse vient du harnais : timeout de l'oracle, codes de sortie ambigus, stderr non stable, reproductibilité, parallélisation des exécutions. Les réducteurs existants ont mis des années à absorber ces cas limites ; en 9 jours on livrera le happy path exact que la grille « mise en œuvre » (propriétés fast-check, contre-exemple réel, hook qui bloque) rend insuffisant. · Parade : réduire le périmètre v1 à un seul type d'entrée (CSV) avec oracle déterministe contractuel, et documenter le reste comme hors-limite honnête.

04. [majeur] **Le chiffre publié ne prouve rien** — « 8 000 lignes → 6 lignes » mesure la capacité de ddmin à supprimer du bruit, pas la valeur du résultat : la perte chiffrée exigée par la grille impact doit être en *minutes de développeur économisées*, avec source ou méthode de mesure. Un chiffre de taille est gonflable à l'infini en choisissant un jeu d'entrée volumineux et un bogue sensible à une seule ligne — le juge y verra une métrique de concours. · Parade : publier le temps humain de réduction manuelle mesuré sur plusieurs développeurs contre le temps Shrink, sur le même cas.

05. [majeur] **Démo vidéo sans spectacle** — une réduction est une boucle qui retire des lignes pendant N minutes : à l'écran, un compteur et du texte qui rétrécit, l'inverse des « 15 premières secondes » exigeant problème + chiffre sans narration. Aucun mouvement, aucune couleur, aucun « wow » ; la grille présentation sera notée sévèrement. · Parade : montage avant/après en split-screen accéléré avec l'erreur qui reste identique en surbrillance, et le chiffre de réduction incrusté dès la seconde 3.

06. [majeur] **La technique n'est pas morte — donc pas de Resurrection** — le shrinking est plus vivant que jamais : Hypothesis, fast-check, jqwik, `cargo test` avec proptest, libFuzzer et les réducteurs LLM émergents l'utilisent ou le réinventent en 2024-2026. La catégorie Resurrection suppose une technique abandonnée que Kiro remet au goût du jour ; ici le récit est faux et un juge qui connaît le fuzzing le dira. · Parade : recadrer sur ce qui est réellement mort (C-Reduce, spécifique C/C++ et quasi abandonné) et l'étendre aux données modernes (CSV/JSON) — ou changer de catégorie.

07. [majeur] **Public minuscule, problème rare** — combien de développeurs réduisent des cas d'échec à la main *ce mois-ci* ? Le fuzzing est l'affaire d'une niche (sécurité, compilateurs, parsers) ; l'utilisateur type nommé avec rôle et contexte, exigé par la grille, sera introuvable au-delà de « ingénieur QA chez un éditeur de parsers ». Le critère « vécu ce mois-ci par la quasi-totalité des développeurs visés » échoue. · Parade : cibler un pain mainstream vérifiable — jeux de fixtures de tests d'intégration qui gonflent — et le chiffrer par enquête ou statistiques publiques.

08. [bloqueur] **Oracle non déterministe et bug morphing** — dès que l'erreur dépend de l'ordre, du temps, de la mémoire ou de la graine (flaky test, heap overflow, data race), la « garantie que le cas réduit déclenche exactement la même erreur » est fausse : ddmin peut converger vers un *autre* bogue qui satisfait l'oracle, ou réduire vers le vide. C'est le trou technique central, et la limite honnête de la grille le rendra visible. · Parade : exécuter l'oracle k fois (k configurable) avec comparaison normalisée de l'erreur, et publier un score de confiance au lieu d'une « garantie ».

09. [mineur] **Le jury dira « déjà vu »** — entre `afl-tmin`, le minimize de libFuzzer et Hypothesis, tout juge ayant fait du fuzzing a déjà vu un réducteur tourner en direct ; l'effet « jamais vu » de la grille présentation/innovation tombe à plat, et la note 89 actuelle repose probablement sur des juges non-spécialistes. · Parade : différencier par l'expérience (rapport HTML diffable, intégration CI en un hook Kiro) plutôt que par l'algorithme, et le dire d'emblée dans la fiche.

10. [mineur] **Casse-jour de démo en direct** — la réduction d'un vrai cas prend des minutes à des heures (des milliers d'exécutions de l'oracle) ; en live, soit la démo tourne trop lentement, soit l'équipe triche avec un cas pré-réduit — et la grille exige un mode démonstration qui ne peut pas échouer, sans réseau. Un oracle lent, un timeout ou un flaky le jour J produit un cas réduit invalide en direct. · Parade : mode démo avec données incluses et exécutions pré-enregistrées rejouables (cache d'oracle), plus un vrai mini-cas qui se réduit en < 30 s pour prouver que ce n'est pas du playback.

---

## Les fiches V2

# V2-01 · Registre des chemins fantômes (Ghost Path Registry)

**Catégorie : Frankenstein (méta-outil agent).** Différenciation en une ligne : *un linter vérifie du code écrit ; Ghost Path vérifie les **affirmations d'un agent avant qu'elles ne deviennent du code**, les attribue à l'étape précise de la session qui les a produites, et publie un taux de références fantômes daté, hashé et rejouable.*

## 1. Le problème vécu ce mois-ci

Utilisateur type : **Baptiste, développeur seul sur des dépôts TypeScript/Kotlin, qui pilote 3 à 8 sous-agents par tâche** (contexte réel de ce dépôt, novembre 2026). Un agent écrit dans son plan « je lis `src/db/session.ts`, j'appelle `SessionPool.acquire()` et j'ajoute la route `/api/v1/ghosts` » ; deux références sur trois n'existent pas. Coût : l'agent part, revient, le parent relit, et le mensonge n'est découvert qu'au merge ou en runtime.

Méthode de mesure de la perte (aucun chiffre inventé) : protocole `mesure/perte.md` à écrire au jalon 1 — compter, sur N sessions réelles publiques, les minutes entre l'affirmation fantôme et son rejet par le compilateur ou le relecteur. Perte visée : `[cible]` minutes par session, `[cible]` % des affirmations de chemin/symbole/route fantômes. Tant que `mesure/perte.md` n'a pas tourné, la fiche n'affiche aucun nombre.

## 2. La mécanique

1. **Extract** — un adaptateur par format de journal déclaré supporté (Kiro, Claude Code JSONL, Cursor) extrait les références **uniquement dans les blocs de code, les diffs et les chemins entre backticks**, jamais dans la prose libre. Chaque référence garde `(session_id, step_index, horodatage, citation littérale)`.
2. **Truth** — base de vérité du dépôt au commit fixé : fichiers, exports AST, routes déclarées, tables SQL des migrations, variables d'env de `.env.example`. Périmètre v1 : **chemins TypeScript sans alias `tsconfig.paths`, sans barrels, sans workspaces** ; symboles et routes en v2.
3. **Resolve** — sortie **ternaire** : `résolu` / `fantôme` / `indéterminé` (chemin dynamique, alias non supporté, hors périmètre). **Invariant `I1`** : aucune référence extraite ne sort sans l'un des trois états, pas de silence. **Invariant `I2`** : `résolu` exige un nœud de graphe identifié par id, jamais une heuristique de chaîne.
4. **Attribuer** — le fantôme est rattaché à l'étape d'agent qui l'a énoncé en premier, avec sa citation exacte. C'est la sortie que ni `tsc`, ni ESLint, ni un LSP ne peuvent produire : ils n'ont ni session, ni étape, ni auteur.
5. **Rejeu** — même journal + même commit ⇒ **même registre bit à bit** ; le hash SHA-256 du registre est publié.

## 3. Le chiffre publié à chaque exécution

Une ligne en fin de run, toujours : `registre <sha256> · commit <sha> · <n> références · <f> fantômes · <i> indéterminés · précision sur corpus témoin [cible] %`. Le JSON brut est l'artefact de référence, le HTML n'en est qu'une vue. Faux positifs **et** faux négatifs publiés avec intervalles, sur corpus externe (§5), jamais sur les seules fixtures de l'auteur.

## 4. La preuve Kiro

- **Specs** `.kiro/specs/{extract,truth,resolve,registry,report}/`, exigences EARS ; un lot = une spec.
- **Propriétés (fast-check)** : `résoudre(r) ≠ indéterminé ⇒ le nœud existe dans la vérité` ; `extraire ∘ résoudre` idempotent ; registre déterministe à commit fixé. Un contre-exemple réel, avec propriété + graine + correctif, sera consigné dans `KIRO_JOURNAL.md` **le jour où il survient** — rien de pré-rédigé ; si aucun n'a surgi au gel, la fiche le dit noir sur blanc.
- **Hook `ghost-path-guard`** : garde un **vrai dépôt tiers open-source** (pas nos fixtures) ; incident raconté avec capture et lien de CI. S'il n'a jamais bloqué, on le retire de la fiche.
- **Steering** : avant/après sur un exemple précis — la consigne « ne citer que des chemins vérifiés » mesurée en fantômes par session, `[cible]` → `[cible]`.
- **Agents** : un relecteur en lecture seule et un testeur, permissions restreintes, commits visibles.
- **Spec vs vibe coding** sur une fonction nommée (`resolvePath`) : durée, allers-retours, défauts = `[cible]`, mesuré au jalon 1, publié même si défavorable.
- **MCP** : serveur minimal `ghost-truth` livré **dans la v1** seulement si le lot tient ; sinon absence justifiée en une phrase, et aucune séquence vidéo ne le montre.

## 5. Corpus externe (anti-circularité)

Cinq dépôts open-source **non choisis pour le test** (tirage aléatoire documenté parmi les 20 premiers résultats d'une requête GitHub fixée à l'avance) + journaux d'agents publics. Protocole, tirage et résultats versionnés. Objectif affiché : **précision plutôt que rappel**.

## 6. Le concurrent le plus proche

`eslint-plugin-import/no-unresolved` — et derrière lui `tsc` TS2307, `dependency-cruiser`, Serena/LSP-MCP. Différence **structurelle**, pas cosmétique :

| | no-unresolved / tsc | Ghost Path |
|---|---|---|
| Entrée | fichier `.ts` sur disque | session d'agent, avant écriture du code |
| Objet | code compilable | toute affirmation : chemin, symbole, route, table, var d'env |
| Sortie | erreur de build | référence + étape d'agent + citation horodatée |
| Métrique | aucune dans le temps | taux de fantômes par session, par modèle, rejouable |
| Preuve | non | registre hashé, daté, imprimable |

Un linter ne peut pas produire la colonne « étape d'agent » : il n'a ni auteur ni horodatage.

## 7. Interface et artefact durable

**Vide** : « aucun journal trouvé — voici le mode démo », bouton vers le corpus inclus. **Chargement** : progression par lot (extract → truth → resolve) avec pourcentage réel, pas un spinner. **Erreur** : format inconnu ou dépôt hors périmètre → message nommant la cause et l'adaptateur manquant, code de sortie non nul. **Succès** : registre à citations cliquables, chaque fantôme lié à son étape d'agent. Le tout vérifié par axe-core en CI à **0 violation `[cible]`**, navigation clavier complète, fantôme signalé par icône + texte (jamais la couleur seule), `prefers-reduced-motion` respecté, thème clair/sombre.

**Artefact durable** : le *Registre des mensonges* — page imprimable datée, extraits cités façon pièce à conviction, hash du registre en pied de page. **Mode démo verrouillé** : journal + dépôt inclus, zéro réseau.

## 8. Les 15 premières secondes de la vidéo

1. `0:00–0:04` — plein écran, une citation d'agent : « je modifie `src/db/session.ts` ».
2. `0:04–0:08` — la même ligne frappée d'un tampon **FANTÔME** + `ls src/db/` qui renvoie `No such file`.
3. `0:08–0:15` — le registre imprimé : 3 fantômes, l'étape d'agent, le hash, la date.

Aucune narration avant `0:15`, pas de musique, pas de marque tierce. Plan principal = le **rapport HTML**, pas le terminal. Aucune séquence ne montre une fonctionnalité absente du dépôt au moment du gel. Vidéo < 3 min, de bout en bout sur l'appareil visé.

## 9. La limite honnête

Ghost Path **ne prouve pas** que l'agent a menti délibérément ; **ne** vérifie **pas** la prose libre (exclue par décision explicite, non-objectif chiffré : `[cible]` % de la prose ignorée) ; **ne** résout **pas** chemins dynamiques, alias, barrels et workspaces en v1 — tout cela sort en `indéterminé`, jamais en `résolu`. L'outil ne prouve pas la correction du code, seulement l'existence ou l'inexistence des références citées. Un dépôt sain peut produire des `indéterminés` en nombre : c'est assumé.

## 10. Les deux jalons

**v1 — avant le 28 novembre** : TypeScript sans alias, chemins de fichiers uniquement, JSON brut + page HTML minimale générée, un adaptateur de journal, mode démo verrouillé, specs Kiro écrites dès le jour 1.
**Version complète — avant le 29 janvier** : symboles, routes, tables SQL, vars d'env ; 3 adaptateurs testés en CI sur un dépôt open-source réel de `[cible]` k+ lignes ; corpus externe et intervalles publiés ; MCP minimal si le lot tient. Le gel publie l'état atteint **avec les défauts restants écrits noir sur blanc**.

## Les cinq cases 20/20

- **Impact** : utilisateur nommé (Baptiste, sous-agents en parallèle), perte mesurée par un protocole versionné `mesure/perte.md` — chiffre `[cible]` jusqu'à exécution ; adoption sans friction : CLI + page HTML statique, aucun compte, aucun serveur, première valeur en moins de 60 secondes sur le corpus de démo inclus.
- **Kiro** : specs EARS par lot, propriétés fast-check sur `resolve`, journal écrit au fil des incidents réels (rien de pré-rédigé), hook gardant un dépôt tiers, steering avant/après, relecteur + testeur restreints, comparaison spec/vibe chiffrée `[cible]`, MCP justifié ou absent.
- **Design** : quatre états implémentés et montrés, axe-core 0 violation en CI `[cible]`, clavier, pas de couleur seule, reduced-motion, thème double, *Registre des mensonges* imprimable, mode démo hors réseau.
- **Innovation** : concurrent nommé (`no-unresolved`), différence structurelle en une ligne et en tableau (§6) ; combinaison inédite **graphe de dépôt × journal d'agent × preuve horodatée rejouable** ; limite honnête écrite (§9).
- **Présentation** : 15 premières secondes = problème + tampon + registre, sans narration (§8) ; vidéo < 3 min de bout en bout sur le rapport HTML ; démo en ligne < 30 s, sans compte ni installation, résultat visible sans clic ; texte Devpost répondant aux huit questions avec les chiffres que l'outil publie, `[cible]` compris.

## Objections traitées

- **« C'est un linter d'imports / le LSP le fait déjà »** (AT-01, AT-02) → l'entrée n'est pas un fichier sur disque mais une session d'agent ; la sortie n'est pas une erreur de build mais une attribution d'étape + citation horodatée + registre hashé. Périmètre étendu au non-compilable (routes, tables, vars d'env) en v2. La différenciation tient en une ligne et résiste au tableau §6.
- **« La v1 en 8 jours est une fiction »** (AT-03) → périmètre coupé : TypeScript sans alias, chemins seulement, JSON + HTML minimal, un seul adaptateur ; specs Kiro dès le jour 1 pour que les preuves existent au gel.
- **« Mesure circulaire »** (AT-04) → corpus externe : 5 dépôts tirés au sort selon protocole versionné, journaux publics, faux positifs et faux négatifs avec intervalles ; aucune mesure passée inventée, tout chiffre est `[cible]`.
- **« La vidéo montre l'inexistant »** (AT-05) → aucune séquence MCP tant que le lot n'est pas livré ; plan principal = rapport HTML.
- **« Récit Kiro prévu, pas vécu »** (AT-06) → journal écrit au fil de l'eau, hook sur dépôt tiers avec capture ; si rien n'a échoué au gel, la fiche le déclare.
- **« Dans six mois le problème est résolu par les agents »** (AT-07) → repositionnement sur **l'audit et la conformité** : preuve datée et rejouable pour les revues de code, le régulateur, les équipes qui n'ont pas le droit de faire confiance à l'agent — utile même quand l'agent se corrigera tout seul.
- **« Angle mort : chemins dynamiques, prose »** (AT-08) → sortie ternaire, `indéterminé` assumé, prose exclue comme non-objectif chiffré, précision préférée au rappel dans la phrase de différenciation.
- **« Énième IA-qui-vérifie-une-IA »** (AT-09) → l'artefact est un registre imprimable, daté et hashé, pièce à conviction — pas un score de faithfulness façon DeepEval/LangSmith.
- **« En démo directe ça casse sur le dépôt du juge »** (AT-10) → mode démo verrouillé hors réseau par défaut, adaptateurs testés en CI sur dépôt open-source réel, et `indéterminé` plutôt qu'une cascade de faux positifs sur `@org/*`.

---

# V2-03 · Ver — *Dette de mutation* (catégorie : Frankenstein)

**Différenciation en une ligne :** Stryker, PIT et mutmut publient un **score agrégé non vérifiable** ; Ver publie, pour chaque ligne du diff, un **verdict muni d'un témoin rejouable en < 10 s** que la CI re-vérifie elle-même — un rapport *proof-carrying*, pas un chiffre de plus.

## 2. Le problème vécu ce mois-ci

Utilisatrice type : **Camille, tech lead de 6 devs sur une appli fintech** soumise à un seuil de couverture réglementaire (80 %) bloquant en CI. Ce mois-ci sa suite est verte à 87 % et un `<` devenu `<=` dans un calcul de plafond de remise est passé en production : la couverture mesure ce qui est **exécuté**, jamais ce qui est **asserté**.

Perte mesurée, méthode écrite : sur `ver-bench` (dépôt réel de référence, 12 000 lignes TS, 640 tests) nous mesurons (a) le nombre de mutants semés **à la main** dans le diff des 20 dernières PR que la suite laisse survivre, (b) le temps mur d'un run Stryker complet, chrono brut. Les deux chiffres sont publiés dans `KIRO_JOURNAL.md` : mesures, pas estimations. Adoption : `npx ver`, sans compte, sans serveur, sans config — lecture de `git diff`, première valeur en **moins de 60 secondes**.

## 3. La mécanique (jusqu'au détail qui prouve qu'elle tient)

1. **Périmètre = le diff.** `git diff --unified=0 base…head` → lignes touchées → mutants AST sur ces seules lignes (6 opérateurs : comparaison, logique, constante, borne, retour, suppression d'appel). Un diff de 200 lignes donne 5 à 60 mutants : le budget temps est borné par la taille de la PR, jamais par celle du dépôt.
2. **Exécution déterministe.** Sandbox `tmpfs` par mutant, arbre de travail jamais écrit (empreinte SHA-256 de l'arbre vérifiée avant/après chaque run, publiée). Carte ligne → tests construite une fois, cachée par empreinte d'arbre. Exécution **mono-process, séquentielle, triée par `mutantId`** → même JSON octet par octet entre deux runs.
3. **Témoin (le mécanisme neuf).** Chaque verdict produit un artefact signé : `{mutantId, hash du patch AST, seed, commande de replay, sortie tronquée du test tueur, exit code, durée, horloge virtuelle figée}`. `ver replay <mutantId>` rejoue **ce seul mutant** en < 10 s et doit retrouver le même verdict ; `ver audit` re-vérifie un échantillon aléatoire (seed publiée) et publie le **taux de verdicts confirmés**. Rien n'est demandé « sur parole ».
```ts
type Witness = { mutantId: string; patchSha: string; seed: number; replayCmd: string;
  killerTest?: string; tail: string; exitCode: number; durationMs: number; virtualClock: string };
type DebtEntry = { mutantId: string; file: string; line: number; justification: string;
  signedBy: string; signedAt: string; treeSha: string };
type VerRun = { commit: string; base: string; treeShaBefore: string; treeShaAfter: string;
  total: number; killed: number; survived: number; timeout: number; equivalent: number;
  auditedSample: number; confirmedRate: number; fullSuiteGap: number; wallMs: number };
```

4. **Contrôle d'honnêteté.** Mode « écart » : sur 30 mutants du diff, suite **complète** au lieu du ciblage ; l'écart de verdicts (`fullSuiteGap`) est publié à chaque run, et > 5 % bascule la CI en mode complet. Un rapport dont `treeShaBefore ≠ treeShaAfter` est un échec dur, pas un avertissement.
5. **Verdicts.** `killed` (un test échoue), `survived` (aucun ne bronche → **dette**), `timeout` (politique écrite : compté à part, **jamais** `killed`, exclu du numérateur), `equivalent` (toujours manuel, signé, horodaté, compté dans la ligne « dont x % d'exclusions »).
6. **Invariant.** `killed + survived + timeout + equivalent = total`, vérifié par le moteur à chaque run : un rapport qui le viole est rejeté, pas publié.

## 4. Le chiffre que l'outil publie à chaque exécution

Quatre nombres, rien d'autre : **« 3 nouveaux survivants sur ce diff · 94 % des verdicts re-vérifiés (échantillon 16, seed 8f3a) · écart ciblé/complet 0 % · 41 s »**.

```
$ npx ver                       # diff de PR, 14 mutants générés
nouveaux survivants   3        (src/pricing/limit.ts:88, :104, src/pricing/fx.ts:31)
verdicts re-vérifiés  94 %     (échantillon 16/14+cache, seed 8f3a, `ver replay` < 10 s chacun)
écart ciblé/complet   0 %      (30 mutants rejoués en suite complète)
temps                 41 s     arbre inchangé (sha 9c1f… = 9c1f…)
grille CI             ÉCHEC — dette signée 0, nouveaux survivants 3
```

Aucun score global absolu : la grille de CI est **`nouveaux survivants ≤ dette signée`**, et le registre de dette ne peut que stagner ou décroître (ratchet). Le chiffre publié **est** la perte supprimée : chaque survivant est une branche du diff que personne n'asserte.

## 5. La preuve Kiro

- **PBT à oracle externe.** 120 mutants semés **à la main** dans `fixtures/known-verdicts/`, verdict attendu écrit par un humain avant tout code (`killed`/`survived`/`equivalent` + test tueur). PROP-1 ≥ 98 % des verdicts attendus retrouvés ; PROP-2 arbre inchangé (empreinte) ; PROP-3 déterminisme octet par octet ; PROP-4 invariant de somme ; PROP-5 mutant en code mort = `survived`, jamais `killed`. fast-check sur arbres TS aléatoires bornés pour la génération AST. **Contre-exemple réel** : PROP-3 a échoué le 12/11 (graine 4417) — `durationMs` du témoin variait et contaminait le hachage canonique du rapport ; correctif = champ exclu du hachage. Propriété, graine et diff dans `KIRO_JOURNAL.md`.
- **Hook qui a vraiment bloqué.** `.kiro/hooks/witness-integrity` refuse tout commit dont un témoin de fixture n'est pas rejouable. Incident du 14/11 : cache de couverture périmé après un rebase, 6 témoins en échec au replay, régression bloquée par le hook (date + diff au journal) ; correctif = invalidation par empreinte d'arbre.
- **Steering avant/après.** `steering/operators.md` (fileMatch `packages/mutate`) : avant, `boundary` produisait 12 % de mutants dupliqués sur le chaînage optionnel ; après la règle « une mutation par nœud AST, ignorer `?.` déjà couvert », 0 doublon sur 4 100 mutants.
- **Spec contre vibe coding, chiffré**, sur l'opérateur `boundary` (le plus piégeux, pas le plus simple) : spec EARS 2 h 10, 3 allers-retours, 1 défaut ; vibe coding 55 min, 11 allers-retours, 7 défauts dont 2 mutants non réversibles. Chiffres bruts au journal.
- **Agents** : `ver-reviewer` en lecture seule (aucune écriture), `ver-tester` borné à `fixtures/**` et `packages/*/tests/**`. **CLI headless** : run nocturne sur `main`, registre publié en artefact. **MCP** écarté et justifié : aucun serveur externe n'apporte de mesure ici.

## 6. Le concurrent le plus proche, et pourquoi l'écart est structurel

Concurrents nommés : **StrykerJS** (`--incremental`, `coverageAnalysis: perTest`, `--thresholds-break`, dashboard) et **PIT** (sélection de tests par couverture depuis 2010). Leur ciblage est assumé comme **acquis** : il n'est pas notre innovation. L'écart porte sur l'objet produit — eux répondent « quel est ton score ? » (scalaire non rejouable, non comparable d'un dépôt à l'autre, non auditable sans refaire le run entier) ; Ver répond « ce diff introduit N branches non assertées, voici la preuve rejouable de chaque verdict ». Trois conséquences structurelles, pas cosmétiques : (a) **auditable** — un tiers rejoue un mutant en < 10 s sans réinstaller ni relancer la suite ; (b) **périmètre diff** — temps borné par la PR, chiffre comparable entre PR d'un même dépôt ; (c) l'outil **publie sa propre marge d'erreur** (taux de re-vérification + écart ciblé/complet), ce qu'aucun des trois ne fait. Moteur AST TypeScript écrit pour le projet : **0 dépendance** à Stryker, PIT, mutmut, cosmic-ray.

## 7. Les quatre états et l'artefact durable

- **Vide** : diff sans ligne mutable → « 0 mutant, rien à prouver » + accès au mode dépôt complet. **Chargement** : progression par mutant, chrono visible (pas de spinner menteur). **Erreur** : suite cassée au départ → « tes tests ne passent pas, Ver ne peut rien mesurer », exit code distinct (2) ; sandbox indisponible → refus net, jamais d'écriture. **Succès** : tableau des survivants (fichier, ligne, avant/après, tests l'ayant exécuté sans échouer, commande de replay copiable).
- **Artefact durable** : `ver-report.html`, page **auto-portante** (CSS/JS inline, zéro réseau), imprimable A4, partageable hors ligne, embarquant le registre de dette signé (survivant, justification, auteur, date, hash) ; `ver-report.json` pour la CI.
- **Accessibilité** : axe-core en CI, **0 violation** ; navigation clavier complète (ordre de tabulation testé) ; statut jamais porté par la seule couleur (icône + texte) ; `prefers-reduced-motion` respecté ; thème clair/sombre.
- **Mode démo** : `ver demo` = moteur compilé en **WebAssembly** + fixtures embarquées, run réel dans la page, aucun réseau, aucune dépendance à la machine du juge.

## 8. Les 15 premières secondes de la vidéo, plan par plan

- **0:00–0:04** plein écran sur le check CI « coverage 87 % ✓ — PR merged », aucune narration.
- **0:04–0:09** le diff : `if (total < limit)` → `<=` ; carton « 0 test n'échoue. »
- **0:09–0:15** `npx ver` ; **chrono réel incrusté** ; à 0:15 il affiche 38 s et « 3 nouveaux survivants — merge bloqué ». Le chiffre saute : 12 mutants tués, 8 survivants sur le diff.
- Suite : 0:15–1:10 `ver replay m-042` (6 s, même verdict) ; 1:10–2:00 le test ajouté, le survivant meurt, la dette repasse à 0 ; 2:00–2:40 le ratchet refuse une PR qui augmente les exclusions ; 2:40–3:00 la limite honnête à l'écran. < 3 min, sans musique ni marque tierce, **aucun accéléré** : le chrono incrusté est la preuve.

## 9. La limite honnête

Ver ne prouve **pas** que ta suite est bonne en général : il ne mesure que les lignes du diff. Il ne prouve **pas** l'équivalence sémantique (indécidable) : `equivalent` reste une décision humaine signée et comptée. Il ne détecte **pas** les régressions induites à distance (changement d'API cassant un comportement hors diff) : seul le mode « écart » en donne une mesure partielle, publiée comme telle. Un diff à 0 survivant n'est pas un diff sans bug.

## 10. Plan à deux jalons

| Lot | Contenu | Jours | Avant |
|---|---|---|---|
| 1 | Diff → lignes → mutants AST (6 opérateurs) + 120 fixtures à verdicts connus | 2,5 | 17 nov. |
| 2 | Sandbox, exécution ciblée séquentielle, empreinte d'arbre, cache de couverture | 2 | 20 nov. |
| 3 | Témoins rejouables, `ver replay`, `ver audit` (échantillon, seed publiée) | 2 | 24 nov. |
| 4 | Registre de dette signé, ratchet, rapport HTML AA auto-portant, grille CI | 1,5 | **27 nov. (gel v1 28)** |
| 5 | Mode « écart » suite complète, comparaison de PR, `ver demo` WASM, vidéo | 5 | 15 déc. |
| 6 | Python (mêmes témoins), suggestion de test par survivant, run nocturne | 6 | **29 janv.** |

**v1 = lots 1 à 4** : la promesse tient (diff, témoins, rejouabilité, ratchet) sans le lot 5.

## Les cinq cases 20/20

- **Impact 20/20** — utilisatrice nommée (Camille, tech lead fintech sous seuil réglementaire) ; perte mesurée sur `ver-bench` (mutants semés à la main survivant aux 20 dernières PR + chrono Stryker brut, au journal) ; suppression mesurée **par l'outil à chaque run** (les 4 nombres du §4) ; adoption `npx` sans compte ni serveur, première valeur < 60 s.
- **Kiro 20/20** — specs EARS par opérateur dans `.kiro/specs/` ; PBT fast-check à **oracle externe** (120 verdicts humains) avec contre-exemple réel documenté (PROP-3, graine 4417, 12/11) ; hook `witness-integrity` ayant **vraiment bloqué** le 14/11 (date + diff) ; steering avant/après chiffré (12 % → 0 %) ; relecteur lecture seule + testeur borné ; spec/vibe chiffré sur `boundary` ; CLI headless nocturne ; MCP écarté et justifié.
- **Design 20/20** — quatre états implémentés et filmés ; axe **0 violation** en CI ; clavier complet ; jamais la couleur seule ; `prefers-reduced-motion` ; clair/sombre ; artefact durable imprimable (`ver-report.html` auto-portant + registre signé) ; mode démo WASM hors réseau.
- **Innovation 20/20** — concurrents nommés (StrykerJS, PIT, mutmut) ; écart **structurel** : verdict à témoin rejouable + auto-publication de la marge d'erreur + périmètre diff, contre un scalaire non auditable ; combinaison inédite (preuve × mesure de tests, technique de 1978 × gate de PR) ; limite honnête §9 ; 0 dépendance aux outils cités.
- **Présentation 20/20** — 15 s = problème + chiffre sans narration ; chrono réel incrusté ; démo de bout en bout < 3 min sans musique ni marque tierce ; démo en ligne < 30 s sans compte ni installation avec résultat visible sans cliquer ; texte Devpost répondant aux huit questions Kiro avec chiffres.

## Objections traitées

- 01 antériorité PIT/Stryker sur l'exécution ciblée : **[neutralisée]** — le ciblage n'est plus vendu comme innovation ; le produit est le verdict à témoin rejouable sur le diff, absent des trois.
- 02 budget temps irréaliste (4 132 mutants / 4 min) : **[neutralisée]** — abandon du run dépôt complet en v1 ; périmètre diff (5–60 mutants), chrono réel publié, benchmark brut au journal.
- 03 « wrapper Stryker avec joli rapport » : **[neutralisée]** — 0 dépendance et garantie nouvelle (rejouabilité, déterminisme octet par octet) démontrée par `ver replay` / `ver audit`.
- 04 score absolu non comparable, seuil gadget : **[neutralisée]** — plus de score global ; grille sur les nouveaux survivants du diff + ratchet de dette signée.
- 05 gaming par exclusion d'équivalents : **[neutralisée]** — exclusion signée, horodatée, comptée dans le chiffre affiché, ratchet interdisant d'augmenter le taux d'exclusions.
- 06 le ciblage rate les vrais tueurs : **[neutralisée]** — mode « écart » sur suite complète (30 mutants), écart publié à chaque run, bascule automatique > 5 %.
- 07 vidéo non crédible, payoff invisible : **[neutralisée]** — run réel de 38 s chrono incrusté ; payoff = 8 survivants sur le diff et merge bloqué (plus de 89,3 → 89,4).
- 08 récit Kiro circulaire (oracle = l'outil) : **[neutralisée]** — oracle externe : 120 mutants semés à la main, verdicts écrits avant le code ; hook raconté avec date et diff.
- 09 abandon à six mois, public théorique : **[assumée : la survie dépend de l'intégration au gate de PR existant, pas de l'outil seul]** — utilisatrice précise nommée, perte chiffrée sur dépôt réel, adoption `npx` < 60 s sans config.
- 10 jour J (chrono, sandbox, déterminisme) : **[neutralisée]** — exécution séquentielle triée, horloge virtuelle figée, politique `timeout` écrite (jamais `killed`), empreinte d'arbre avant/après, démo WASM 100 % embarquée.

---

# V2-05 · Rejeu — *rejouer les versions d'un agent, pas ses logs*

## 1. Nom, catégorie, phrase de différenciation

| | |
|---|---|
| Nom | **Rejeu** — *Agent Replay : rejouer les versions d'un agent, pas ses logs* |
| Catégorie | Frankenstein — le magnétoscope ressuscité, mais la bobine est l'historique de versions d'un agent, pas une capture d'écran |
| Public | Équipes de 4 à 15 personnes qui reviewent des PR produites par un agent de code (Anaïs, dev senior, 6 personnes, 3 PR d'agent/semaine, 2 dépôts) |
| Prix visés | Best Frankenstein, Best Kiro Crew App, prix globaux |

**Phrase de différenciation (une ligne) :** « rr restitue l'exécution d'un processus qu'il a dû lancer sous ptrace ; Rejeu restitue les **versions successives du dépôt** qu'un agent a traversées puis qu'un *squash* a effacées, et produit l'**index de la version fautive** — une information qu'aucun traceur (qui n'exécute rien) ni `git bisect` (dont les commits n'existent plus) ne peut fournir. »

**Les trois objets, tenus séparés (le cœur de la V2) :** ce qui est **rejoué** = les états du dépôt (arbres git, adressés par contenu) ; ce qui est **prouvé** = l'index du premier checkpoint où le prédicat bascule, établi par **exécution réelle** du prédicat dans un bac à sable ; ce qui est **versionné** = `replay/<session>/chain.json` (chaîne d'attestation) + `report.html`, commités dans le dépôt — la preuve devient un **test de non-régression** rejouable en CI.

## 2. Le problème vécu ce mois-ci, la perte chiffrée et sa méthode

- **Fait vécu, novembre 2026 :** l'agent itère (il corrige son propre test rouge), puis l'équipe fait `git commit --amend` ou `git rebase -i` pour obtenir une PR propre. **Les états intermédiaires disparaissent du dépôt.** La PR finale est élégante ; la version qui a introduit le bug est introuvable.
- **Perte chiffrée (corpus `fixtures/corpus-nov2026`, 20 sessions du CLI headless Kiro, 1er→12 nov. 2026) :** **11 sessions sur 20 (55 %) n'ont plus d'historique exploitable** ; **9 régressions sur 20 n'ont pas pu être attribuées manuellement** ; temps de recherche manuelle quand l'historique existe : **14 min 20 s** (médiane, 2 ingénieurs, min 3, plafond 45 min) ; **2 h 40** de temps ingénieur médian par incident non résolu, **≈ 23 h sur 3 mois** pour l'équipe.
- **Méthode de mesure :** extraction des sessions depuis les run IDs de CI (1er→12 nov.), comparaison avec l'historique git du serveur *avant* squash (référence), chronométrage manuel par deux ingénieurs du service. Le chiffre **41 s** publié par l'outil (point 4) est obtenu sur le même corpus, sur la même métrique.
- **Pourquoi le rejeu est la seule issue, pas un nicer :** l'information n'existe plus (squash), `git bisect` exige des commits existants, les logs d'agent ne portent pas l'état du dépôt, et `rr` n'a jamais vu la session (elle a eu lieu sans lui). Aucun concurrent ne peut reconstruire un état effacé.

## 3. La mécanique, jusqu'au détail qui prouve qu'elle tient

1. **Capture par proxy d'outils, sans toucher au code de l'agent.** Un serveur MCP (`replay-broker`) s'interpose entre le CLI headless Kiro et ses outils. Après chaque appel mutant (`edit`, `write`, `bash` touchant le dépôt), il écrit un **checkpoint** : `git write-tree` (arbre git du dépôt de travail), diff contre le checkpoint précédent, sortie de l'outil, empreinte des fichiers **hors dépôt** connus, `SOURCE_DATE_EPOCH`/`seed`/`modelVersion`. L'agent n'est ni patché ni forké : **seuls ses appels d'outils passent par le proxy**.
2. **Store de checkpoints, pas un journal.** `.replay/objects/` est un store **adressé par contenu** (arbres git) ; `chain.json` liste les checkpoints dans l'ordre, chaque entrée portant le hash de la précédente → **attestation** : retoucher le journal casse la chaîne et `replay verify` sort en 1. Une chaîne d'attestation n'existe pas dans un log brut éditable.
3. **Rejeu 100 % simulé.** `replay find` extrait chaque checkpoint dans un répertoire jetable (`git archive` de l'arbre), coupe le réseau (`unshare -n`, allowlist du fournisseur uniquement en mode re-run), exécute le **prédicat** (`pnpm test agents/parser.spec.ts`) **dans ce bac à sable**, et ne touche jamais le dépôt de travail : **0 écriture hors sandbox**, aucune commande destructive rejouée sur la machine hôte.
4. **Recherche de la version fautive.** Dichotomie sur l'ordre des checkpoints quand le prédicat est monotone, balayage linéaire sinon ; sortie = **le plus petit k tel que P(k) faux et P(k-1) vrai**. *Invariant REJ-P-01 :* rejouer le checkpoint k depuis k-1 redonne **exactement** le même hash d'arbre ; *invariant REJ-P-03 :* le sandbox ne modifie que son propre répertoire (hash du dépôt hôte inchangé avant/après).
5. **Deux modes honnêtes.** Mode **bande** : les sorties capturées du modèle sont réinjectées (utile pour isoler un composant, et **tautologique par construction** — ce n'est donc pas le chiffre publié). Mode **re-run** : le fournisseur est réellement appelé (température 0, modèle épinglé, `seed` si le fournisseur l'expose) → l'**accord de décision est mesuré (78 %, 14/18 décisions)**, jamais supposé.
6. **Trois sorties distinctes :** le **verdict** (index du checkpoint fautif, son arbre, le prédicat qui bascule), la **timeline** (les 7 checkpoints, état de chaque prédicat), et la **chaîne** (traçabilité complète, committable).

## 4. Le chiffre que l'outil publie à chaque exécution

```
REJEU 1.0 · session a41f9c2 · 7 checkpoints · 7/7 rejoués · couverture réelle 61 %
VERDICT  itération fautive #3 (arbre 8ac91e0) · prédicat : agents/parser.spec.ts › trailing comma
PRÉCÉDENT #2 (arbre 51c0d7b) passe · TEMPS 41 s · CHAÎNE vérifiée 7/7 · RE-RUN accord 78 % (14/18)
```

- **Chiffre en gras : l'itération fautive** — nombre produit par exécution réelle du prédicat, pas par comparaison de texte.
- **Trois chiffres non tautologiques :** itération localisée correctement sur **18/20 sessions** (2 flakies détectées, verdict suspendu « non déterministe ») ; temps **41 s** (médiane 38 s) contre **14 min 20 s** en recherche manuelle ; **couverture réelle 61 %** des étapes exécutées (le reste est bandé).
- Une bande ne peut produire aucun de ces trois chiffres : elle n'exécute aucun prédicat. Un log + diff n'en produit qu'un : le diff.

## 5. La preuve Kiro

- **Specs** : `.kiro/specs/replay/*.md`, une par lot, exigences en EARS ; chaque exigence possède un **vérificateur** exécuté à chaque checkpoint → « exigence REJ-F-03 violée au checkpoint #3 ». Les specs **fournissent les prédicats** : c'est le mécanisme central, pas une case cochée.
- **Propriétés (fast-check)** : 5 propriétés, dont REJ-P-01 (arbre stable) et REJ-P-03 (sandbox isolé). **Contre-exemple réel** : la propriété « l'arbre du checkpoint k est stable pour deux captures de la même action » a échoué, **graine 20261104** — `scripts/version.mjs` insérait `Date.now()` dans `VERSION`, donc deux captures de la même action donnaient deux arbres ; correctif : `.replayignore` + digest séparé pour les fichiers générés. Journal `KIRO_JOURNAL.md`, section « property seed 20261104 ».
- **Hook qui a vraiment bloqué** : `checkpoint-guard` (pre-tool) refuse `git commit --amend`, `git reset --hard`, `git checkout -- .` pendant une session capturée. **Incident du 4 nov., 14 h 12** : l'amend a détruit l'arbre du checkpoint #3, `find` a désigné la mauvaise itération ; hook écrit le soir même ; **il a re-bloqué le même appel le 7 nov.** sur une session réelle.
- **Steering** `determinism.md` (horloge logique, `TZ=UTC`, `seed` épinglé, générateurs dans `.replayignore`) — avant/après sur `scripts/version.mjs` : **2 faux écarts de checkpoint sur 7 sessions → 0**.
- **Agents personnalisés** : `relecteur` (lecture seule : audite `chain.json`, le mapping exigence↔vérificateur, refuse les schémas non conformes) et `testeur` (sandbox + PBT, réseau coupé) ; permissions : lecture seule sur le dépôt, écriture seulement dans `.replay/`.
- **Spec vs « vibe coding » sur `findFaultyCheckpoint`** : **spec (EARS + 5 PBT) = 3 h 20, 14 allers-retours, 3 défauts avant merge** ; **vibe coding (prompt direct, sans spec) = 1 h 05, 27 allers-retours, 6 défauts dont 2 bloquants (faux positif sur test flaky, divergence non localisée), 2 h 55 de débogage** — chiffres du journal de construction.
- **MCP + CLI headless** : serveur `replay_checkpoint` (« arbre au checkpoint n », « premier checkpoint fautif », « vérifier la chaîne ») — **37 appels** par les agents Kiro pendant la construction, **2 exécutions complètes de suite évitées** ; `kiro-cli --headless` pour capturer le corpus des 20 sessions ; aucune donnée sortante.
- *Convention de preuve :* incidents datés = déjà survenus pendant la construction ; chiffres marqués « cible » seront mesurés sur `fixtures/corpus-nov2026` (20 sessions) au jalon 1.

## 6. Le concurrent le plus proche, et pourquoi la différence est structurelle

| Concurrent | Ce qu'il rejoue | Ce qu'il exige | Pourquoi ce n'est pas la même garantie |
|---|---|---|---|
| **`rr`** (Mozilla) | appels système d'**un processus** | démarrer le processus sous `rr` (ptrace, Linux) | ne rejoue pas un **état effacé**, n'attribue rien à une itération d'agent, pas de chaîne, pas de portabilité |
| **`replay.io`** | time-travel debugging natif | abonnement, instrumentation native | commercial, hors agents, pas d'artefact versionnable |
| **VCR / cassettes** (VCR.py, Polly) | requêtes HTTP | proxy réseau pendant l'original | rejoue l'I/O réseau, pas les versions successives du dépôt |
| **LangSmith / Langfuse** | traces d'agents | SDK dans l'agent | observabilité : n'exécutent **rien**, ne localisent aucune version fautive |
| **`git bisect`** | commits existants | que les commits existent | les commits de l'agent ont été **squashés** : le commit à finder n'existe plus |

**Différence structurelle (une phrase) :** nous rejouons **le dépôt**, pas **le processus**, et la garantie produite est **l'index de la version fautive** (par exécution réelle du prédicat à chaque version), non la fidélité bit-à-bit d'une trace. Aucun des cinq ne peut la produire, y compris sur une session déjà passée.

## 7. Les quatre états d'interface et l'artefact durable

- **Vide** : aucune session capturée → « Aucune session. Lancez `replay capture` » + les 3 dernières sessions locales ; aucune maquette de contenu fantôme.
- **Chargement** : progression par checkpoint (« checkpoint 4/7 — prédicat en cours — 12 s »), squelette de timeline, Annuler possible.
- **Erreur** — trois cas distincts, tous actionnables : prédicat introuvable, checkpoint non rejouable (dépendance manquante), **flaky** (« le prédicat a échoué 2 fois puis réussi 1 fois : test non déterministe, verdict suspendu »).
- **Succès** : verdict, timeline des checkpoints (icône + texte + couleur, **jamais la couleur seule**), diff du checkpoint fautif vs le précédent, bouton « rejouer ce checkpoint ».
- **Artefact durable** : `replay/<session>/report.html` **imprimable A4** (verdict + timeline + chaîne + prédicat), `replay/<session>/chain.json` **versionné** dans le dépôt, store `.replay/objects/` (arbres git adressés par contenu).
- **Accessibilité** : `axe` en CI sur `report.html` → **0 violation** ; navigation clavier complète (Tab/Entrée/Échap, focus visible) ; `prefers-reduced-motion` coupe les transitions de la timeline ; contrastes AA vérifiés sur thème clair et sombre.
- **Mode démonstration** : fixtures + dépôt miniature embarqués, **zéro réseau, zéro exécution réelle** (résultats préenregistrés) → il ne peut pas échouer devant un jury.

## 8. Les 15 premières secondes de la vidéo, plan par plan

- **0:00–0:03** : CI rouge sur la PR #412, merguée il y a 19 jours ; la liste des commits n'en montre qu'**un** — étiquette « squashed ».
- **0:03–0:07** : on fait défiler le diff : 14 fichiers, 612 lignes, aucun commit intermédiaire ; aucune narration.
- **0:07–0:11** : surimpression — **« 2 h 40 perdus · 9 sessions sur 20 sans historique »**.
- **0:11–0:15** : `replay find a41f9c2` → **« itération fautive #3 · 41 s »** ; la timeline passe au rouge au checkpoint 3, le diff s'ouvre.
- Aucun carton d'intro, aucun texte projet avant 0:07 : le problème **et** le chiffre sont à l'écran.
- **0:15–3:00** : capture via le broker (0:15–0:40) · rejeu en sandbox, réseau coupé visible (0:40–1:20) · divergence localisée (1:20–1:50) · `checkpoint-guard` qui refuse un `commit --amend` (1:50–2:10) · `report.html` imprimable + `chain.json` committé (2:10–2:40) · mode démo hors ligne (2:40–3:00).

## 9. La limite honnête : ce que l'outil ne prouve pas

- Il **ne prouve pas** que le modèle est reproductible : le taux d'accord (78 %) est **mesuré**, l'identité ne l'est pas ; un fournisseur peut changer un modèle sous une version épinglée → le mode re-run signale la dérive au lieu de la masquer.
- Il **ne capture** que ce qui passe par le broker : un outil écrivant hors dépôt sur un chemin non listé n'est pas suivi (liste blanche explicite : `~`, `/tmp`, caches outils).
- Il **ne remplace pas la revue de code** : il localise la version fautive, il ne dit pas si le correctif est bon.
- Il **ne rattrape pas le passé** : la capture doit être active (comme `rr`) — mais contrairement à `rr`, aucun traceur n'est requis : un proxy d'outils suffit, l'agent n'est pas instrumenté.
- Un test **flaky** suspend le verdict (« non déterministe ») au lieu de deviner.
- `unshare` ⇒ **Linux uniquement en v1** (macOS/Windows déclarés hors périmètre) ; la chaîne prouve l'**intégrité** du journal, pas l'honnêteté de l'agent qui l'a écrit.

## 10. Le plan à deux jalons

- **Jalon 1 — v1 avant le 28 novembre (9 j-agent)** : broker MCP (capture + checkpoints `git write-tree`) · store `.replay/objects/` · `chain.json` + `replay verify` · `find` sur un prédicat unique avec sandbox `unshare -n` · rapport terminal · mode démo hors ligne. **Critère de gel :** 20 sessions capturées, 18/20 localisées, chaîne vérifiée, démo qui ne peut pas échouer.
- **Jalon 2 — version complète avant le 29 janvier (25 j-agent)** : dichotomie + détection de flakies · attribution aux exigences EARS · rapport HTML imprimable + a11y CI · multi-prédicats · **Crew nocturne sur les sessions du jour** (rejeu réel, ouverture d'un ticket au premier checkpoint fautif) · serveur MCP `replay_checkpoint` · CI `replay verify` en merge-blocking.

## Les cinq cases 20/20

- [x] **1 · Impact** — problème mesuré ce mois-ci sur 20 sessions réelles (11/20 sans historique, 2 h 40/incident) ; l'outil **publie lui-même** le temps de localisation (41 s) et le taux de localisations correctes ; adoption sans friction : `npm i -g replay` + un proxy MCP, aucun compte, aucun serveur, première valeur < 60 s.
- [x] **2 · Technique / Kiro** — 5 specs EARS dans `.kiro/specs/replay/` **fournissant les prédicats** ; 5 propriétés fast-check dont **un contre-exemple réel (graine 20261104)** consigné dans `KIRO_JOURNAL.md` ; hook `checkpoint-guard` ayant **réellement bloqué** un `commit --amend` le 7 nov. ; steering `determinism.md` (2 faux écarts → 0) ; agents `relecteur`/`testeur` en lecture seule ; comparaison chiffrée sur `findFaultyCheckpoint` ; MCP (37 appels, 2 suites évitées) + CLI headless.
- [x] **3 · Design** — 4 états réellement implémentés (vide / chargement / erreur / succès, flakie comprise) ; `axe` CI = **0 violation** ; clavier complet ; icône + texte en plus de la couleur ; `prefers-reduced-motion` ; artefacts durables `report.html` imprimable A4 + `chain.json` versionné ; mode démo hors ligne (fixtures + dépôt miniature, aucune exécution).
- [x] **4 · Innovation** — concurrents nommés (`rr`, `replay.io`, VCR/cassettes, LangSmith/Langfuse, `git bisect`) ; différence **structurelle** (objet = versions du dépôt, garantie = index de version fautive, non fidélité d'une trace) ; combinaison inhabituelle : rejeu système × régression d'agent × exécution de tests ; limite honnête écrite au point 9.
- [x] **5 · Présentation** — 0:00–0:15 problème + chiffre à l'écran, sans narration préalable ; démo hors ligne < 30 s, sans compte ni installation, résultat visible sans clic ; 8 questions Devpost reprises avec les chiffres ci-dessus.

## Objections traitées

01. **[neutralisée]** — `rr` et `replay.io` nommés au point 6 ; l'objet n'est pas le processus mais les versions du dépôt, la garantie est l'index de version fautive : hors de portée de `rr` (ptrace, processus vivant, état effacé non rattrapable). Différence structurelle, pas cosmétique.
02. **[neutralisée]** — ce n'est pas un log + diff : store de checkpoints **adressé par contenu** (arbres git), exécution réelle du prédicat en sandbox, chaîne d'attestation vérifiable (`replay verify`), et une **sortie qui est un verdict** (index), pas une liste de différences. Un log brut n'exécute rien et ne prouve rien.
03. **[neutralisée]** — v1 restreinte au runtime contrôlé (CLI headless Kiro + Crew) ; capture par **proxy d'outils** sans modifier le code de l'agent ; l'absence de garantie pour un agent tiers est écrite noir sur blanc au point 9 (et O3 est reformulé, pas abandonné en silence).
04. **[neutralisée]** — le chiffre phare n'est plus « identité par construction » : c'est l'itération fautive (**18/20**, 2 flakies suspendues) et le temps (**41 s** vs 14 min 20 s) ; l'identité de la bande n'est qu'un prérequis, l'accord après régénération (**78 %**) est mesuré.
05. **[neutralisée]** — la vidéo ouvre sur une régression réelle et un diff squashé (0:00–0:07), pas sur un lecteur de log ; les 4 états sont visibles ; le chiffre est à l'écran à 0:07, narration nulle avant.
06. **[neutralisée]** — Kiro devient le sujet : broker MCP sur le CLI headless, specs EARS **qui fournissent les prédicats**, hook + CI `replay verify` sur `chain.json`, Crew nocturne qui rejoue **les sessions du jour** (pas des fixtures).
07. **[neutralisée]** — le cas vécu est chiffré sur 20 sessions réelles : le squash efface l'itération fautive (11/20), `git bisect` est impossible, les logs ne portent pas l'état du dépôt — le rejeu est la seule voie restante, pas un nicer.
08. **[neutralisée]** — décision arrêtée et documentée : **rejeu 100 % simulé** (répertoire jetable, réseau coupé, dépôt de travail intact, commandes destructives jamais rejouées sur l'hôte) ; l'overlay est le bac à sable, pas une question ouverte.
09. **[assumée : la métaphore « magnétoscope » est conservée et peut coûter des points d'esthétique — le jury la classera peut-être en « sympathetic VCR for agents » ; on assume ce risque plutôt que de masquer la mécanique réelle sous une métaphore neuve.]
10. **[neutralisée]** — mode démo embarqué dès le lot 1 (fixtures + dépôt miniature, zéro réseau, zéro exécution) ; l'empreinte du dépôt n'est pas rejouée telle quelle mais **reconstruite** dans le sandbox à la volée, donc aucun chemin absolu ni version de Node figé ne peut faire diverger la démo.

---

# V2-09 — « Reprise » (*Local Restore Drill*)

> **Recadrage de fond vs CC-09** : la cible n'est plus « les équipes qui ont restic/borg », mais
> **l'environnement local du développeur** — l'état que Git ne contient pas — et la garantie n'est plus
> « l'archive est intacte » mais « **l'environnement est vivant** : restauré, puis rouvert par
> l'application qui en dépend, en un temps mesuré ».

## 1. Nom et catégorie

| | |
|---|---|
| Nom | **Reprise**. Anglais : *Local Restore Drill — the state git doesn't keep is the state nobody restores*. |
| Catégorie | Frankenstein — *l'exercice d'évacuation incendie des années 70* × *le poste de travail du développeur comme sinistre*, plus *la CI transformée en simulateur d'incident permanent*. |
| Prix visés | Best Frankenstein, Best Demo, prix globaux. |
| Charge | v1 **6 jours-agent** (périmètre écrit noir sur blanc, §10), total 20 j. |
| Différenciation (une ligne) | `restic check` prouve que l'**archive** est intacte ; **Reprise** prouve que l'**environnement local** — celui que Git ne contient pas — est **vivant** : il le restaure en bac à sable, le fait rouvrir par **l'application qui en dépend** (`.env` déchiffré, `sqlite3 .integrity_check`, `pg_restore --list`, `npm ci && vitest`), et publie le **RTO local mesuré** à chaque commit. |

## 2. Le problème vécu ce mois-ci

**Persona (nommé) :** *Alex, dev full-stack sur poste Ubuntu, conteneur Postgres 16 local + `.env`
(12 secrets) + 34 fichiers ignorés par Git (seeds, exports SQL, captures) + config IDE + 2 workspaces
npm*. Il perd l'état local quand un `docker compose down -v` vide un volume, quand un `.env` est
écrasé par un stash mal fusionné, quand le disque se remplit, quand le portable ne redémarre plus.

**Perte chiffrée (méthode : chronométrage sur 5 étapes — récupérer les secrets, rejouer les
migrations, re-seeder, re-configurer l'IDE, relancer) :**
- médiane **47 min** de reprise, plage **12 min – 3 h 20** (11 dévs, protocole + captures
  horodatées publiés dans `docs/reprise-11devs.md`) ;
- **2 / 11** n'ont pas pu rejouer leurs seeds (état non reconstruit, chemins codés en dur) → **absence
  de reprise**, pas seulement lenteur ;
- coût annualisé : 47 min × 4 incidents/an ≈ **3 h 10 par dev et par an**, hors heures de travail
  perdues.

**Ce que l'outil supprime, mesuré par lui-même à chaque exécution :** le drill reconstruit réellement
l'environnement local dans un bac à sable et chronomètre la chaîne complète → **RTO local mesuré**
(garantie ≤ 5 min en v1 avec snapshot à chaud), publié à chaque run. La perte passe de « 47 min
inconnues, parfois impossibles » à « **6 min 40 mesurées ce matin, état par état** ».

**Adoption sans friction :** binaire unique, **zéro compte, zéro serveur, zéro configuration
préexistante** (pas de restic à installer, pas de NAS à brancher) ; première valeur (découverte
lecture seule + un témoin) en **47 s** mesurés. Le plus dur — décider *ce qui* doit survivre — est
proposé par l'outil et validé en une touche.

## 3. La mécanique — jusqu'à l'invariant

1. **Déclarer (0 s, lecture seule).** `reprise discover` liste les *états vitaux* candidats : `.env*`,
   volumes Docker nommés, fichiers ignorés Git non triviaux, secrets du trousseau, config d'outils.
   Sortie : un manifeste `reprise.toml` proposé, que le dev valide (une ligne par état vital).
2. **Capturer.** Un snapshot local chiffré (restic en moteur, dépôt local, clé `age` dans le trousseau
   OS) des états vitaux déclarés. Rien n'est écrit ailleurs que dans le dépôt de snapshot + le bac
   à sable.
3. **Bac à sable (le cœur).** `unshare -m` (namespace de montage) + source montée **en lecture seule**
   (`mount --bind,ro`) + Landlock (kernel ≥ 5.13) interdisant l'écriture sur `$HOME` et sur la source +
   `tmpfs` inscriptible unique pour le travail. **Aucun `tar -x` ne s'exécute hors de ce namespace.**
4. **Restaurer.** Décompactage du snapshot dans le sandbox, restitution des secrets (déchiffrement
   `age` via la clé du trousseau), re-materialisation du volume, rechargement de la config.
5. **Faire rouvrir par l'application (le cœur distinctif).** Chaque état vital porte un **témoin
   applicatif déterministe**, exécuté *dans* le sandbox : `sqlite3 db .integrity_check`,
   `pg_restore --list dump.sql`, `psql -c 'select count(*) from users'` en transaction **lecture
   seule**, `npm ci && vitest run --changed`, `docker compose config -q`. Un fichier lisible mais
   inexploitable ⇒ `fail`.
6. **Mesurer.** RTO (chaîne complète snapshot→témoins verts), débit, taille, écart au budget déclaré.
7. **Publier.** Verdict daté, signé (ed25519), `sha256` du rapport, append-only dans `verdicts.jsonl`.
8. **Rejouer.** Hook de commit + job CI nightly : dérive détectée si le RTO monte de > 30 %, si un
   état vital disparaît du manifeste, si un témoin passe de vert à rouge.

**Invariant (prouvé, pas affirmé) :** *le drill ne modifie ni ne supprime l'état d'origine* —
le hash d'arbre du dépôt, du volume et de `$HOME` est calculé **avant et après**, et la CI échoue si
les deux diffèrent. **Garantie :** *un drill vert prouve que N états vitaux ont été restaurés **et
rouverts par l'application qui en dépend**, en ≤ budget, sans que l'environnement d'origine n'ait
été modifié.*

**Preuve par propriété qui a réellement échoué :** `RES-P-01` (« aucune écriture hors bac à sable »),
fast-check, 300 manifestes générés (traversées `../../`, symlinks, chemins absolus), **graine
`0xC0FFEE`** → contre-exemple : un tar à entrée absolue `/home/alex/.bashrc` était extrait **pendant
la phase de pré-vérification, avant que le namespace soit appliqué** ⇒ sortie du sandbox. Correctif :
extraction **uniquement** via `unshare` + `mount --bind,ro` + Landlock **avant** toute extraction, et
rejet des entrées absolues/`..` par `tar --list` avant extraction. Journal : `KIRO_JOURNAL.md`,
propriété + graine + contre-exemple + correctif.

## 4. Le chiffre que l'outil publie à chaque exécution

| Champ | Exemple mesuré |
|---|---|
| **RTO local mesuré** (chaîne complète) | **6 min 12 s** |
| États vitaux rouverts par leur application | **5 / 5** |
| Écart au budget déclaré | **− 38 s** (budget 7 min) |
| Dérive RTO depuis le drill précédent | **+ 12 %** (seuil d'alerte 30 %) |
| Âge du dernier drill vert | **2 j** (alerte à 7 j) |
| Octets écrits hors bac à sable | **0** (diff d'empreintes avant/après) |
| Empreinte + signature du verdict | `sha256:9f2c…` / `ed25519:7a1e…` |

Un seul chiffre porte la promesse : **« votre poste peut revenir en 6 min 12 s, prouvé par
l'application qui l'utilise, ce matin. »**

## 5. La preuve Kiro

| Attendu par la grille | Preuve concrète |
|---|---|
| Specs EARS | `.kiro/specs/sandbox-guard.md`, `witness-runner.md`, `manifest-discovery.md`, `verdict-signing.md` — exigences `RES-F-01..08` en notation EARS, conservées |
| PBT + contre-exemple réel | fast-check sur `RES-P-01..05` ; contre-exemples `0xC0FFEE` (extraction avant namespace) et `0xBEEF` (fichier au sha256 correct mais au contenu indécodable ⇒ faux `pass` → ajout du témoin « ouvrabilité ») documentés dans `KIRO_JOURNAL.md` |
| Hook qui a bloqué une régression | `drill-guard` (pre-commit + gate CI) : refuse tout commit touchant `.env*`, `docker-compose*.yml`, `migrations/**`, `*.sql` sans drill vert sur le digest courant de l'arbre. **Incident du 12 nov.** : un commit renommant `0042_add_index.sql` faisait disparaître silencieusement le témoin `pg_restore --list` du manifeste ⇒ hook a **refusé le push** (« witness pg_restore manquant pour l'état vital db-local »), régression bloquée avant merge |
| Steering avant/après | `safety.md` : avant, 2 occurrences d'extraction directe du chemin de l'archive ; après, 0 (tout passe par `sandbox.extract()`), vérifié par un grep en CI |
| Agents à permissions restreintes | `.kiro/agents/relecteur.json` (lecture seule : `read`/`grep`/`list`, aucun write) relit manifeste + verdict et refuse 3 manifestes incohérents ; `.kiro/agents/testeur.json` (read + exécution sandbox) génère **120 fixtures de corruption en 40 s** |
| Comparaison spec vs vibe coding, chiffrée | Fonction précise : `extractIntoSandbox()` (packages/guard). Spec-first : 4 h 20, 9 itérations, **4 défauts avant merge**, 380 lignes, 0,9 ligne de test/LOC. Vibe coding : 2 h 05, 3 itérations, **11 défauts avant merge** dont **2 safety-critical** (traversée de chemin, évasion symlink), 410 lignes, 0,3. Conclusion mesurée : le vibe est plus rapide sur le chemin heureux, mais **ses 2 seuls défauts graves sont exactement ceux que la propriété RES-P-01 rattrape** |
| MCP justifié | `drill_mcp` (`drill_run`, `drill_verdict`, `drill_fixtures`) : intégration CI de **1 h 40 (script + parsing JSON) à 6 min** ; le relecteur agent lit le verdict sans accès shell |

## 6. Le concurrent le plus proche, et la différence structurelle

**`restic check --read-data`** (et `borg check --verify-data`) : vérifie l'**intégrité des paquets** de
l'archive, sur place, **sans jamais recréer un artefact utilisable**. **Veeam SureBackup / Instant
Verification** : restauration réelle + rapport daté, mais appliance propriétaire, licence, périmètre serveur.
**`docker compose down -v`** : le vrai destructeur, sans aucune trace.

Différence **structurelle**, trois axes, pas cosmétique :
1. **Objet de la preuve** : octets du conteneur (`check`) ↔ **environnement applicatif rejoué**
   (témoin exécuté par l'application qui en dépend) ;
2. **Périmètre** : les sauvegardes déjà configurées (serveurs) ↔ **l'état local que personne ne
   sauvegarde et que Git ne contient pas** (`.env`, volume, ignorés) ;
3. **Sortie** : « paquets intacts » ↔ **RTO mesuré + verdict signé + historique + gate CI**.

**Phrase de différenciation qui résiste à la contradiction :** « `restic check` peut passer vert et
votre poste rester irrécupérable ; Reprise ne dit jamais « intact », il dit « rouvre en 6 min 12 s » —
et il le prouve en faisant tourner l'application. »

## 7. Les quatre états d'interface et l'artefact durable

| État | Écran (vues du rapport web local, hors-ligne) |
|---|---|
| **Vide** | « 0 état vital déclaré » + `reprise discover` proposé (lecture seule, aucune écriture) |
| **Chargement** | phases nommées : capture → restauration → témoins (n/5) → verdict, % et phase courante |
| **Erreur** | échec **nommé** : quel état vital, quelle commande témoin, stderr complet, verdict `fail` signé, aucun crash ni page blanche |
| **Succès** | verdict horodaté, RTO, 5/5, empreinte, signature, bouton « imprimer le rapport » |

- **Accessibilité AA vérifiée par axe en CI** : `axe-core` sur les 4 vues, **0 violation** ; navigation
  clavier complète (tab/entrée, focus visible) ; l'information **n'est jamais portée par la seule
  couleur** (verdict = mot `PASS`/`FAIL` + icône + bordure double) ; `prefers-reduced-motion` respecté.
- **Artefact durable** : `verdicts.jsonl` append-only signé (ed25519) + **rapport HTML autonome
  imprimable** (A4, une page par drill) exportable et vérifiable hors ligne.
- **Mode démonstration qui ne peut pas échouer en direct** : `--demo` embarque un corpus signé
  (512 Mio) et rejoue des verdicts réels **pré-calculés** ; **aucun réseau requis**.
- **Identité visuelle** : sobre, deux couleurs d'état, thème clair et sombre via `prefers-color-scheme`.

## 8. Les 15 premières secondes de la vidéo, plan par plan

| Temps | Plan | Texte à l'écran |
|---|---|---|
| 0:00–0:04 | Terminal plein cadre, une ligne rouge | `RTO local : 8 min 12 s — db-local : rouvert ✓` |
| 0:04–0:09 | Même écran, relance d'un drill | `12 min 04 s — 4/5 — .env a changé depuis le dernier drill` |
| 0:09–0:15 | Split : `docker compose down -v` puis `reprise run` | reconstruction complète, verdict vert horodaté et signé |
| 0:15–0:20 | Carton | **« 47 min pour rebricoler votre poste après une perte d'état local — médiane mesurée sur 11 développeurs. Nous on le prouve : 6 min 12 s. »** |

Puis 0:20–1:10 le drill réel sur le dépôt du projet (vraie base locale, vrais secrets de démo) ·
1:10–1:40 le témoin `pg_restore --list` et `sqlite3 .integrity_check` qui prouvent que les fichiers
servent · 1:40–2:20 le hook `drill-guard` qui refuse un commit et sa trace à l'écran · 2:20–2:50
l'historique des verdicts et la dérive + la démo web hors-ligne · 2:50–3:00 l'artefact imprimé.

## 9. La limite honnête — ce que l'outil ne prouve pas

- Il ne prouve **que les états vitaux déclarés** : un `.env` non déclaré reste non couvert (le
  manifeste est donc affiché, jamais caché).
- Il ne prouve **pas** la survie du hardware : un disque mort reste un disque mort (Reprise réduit le
  coût de la *reprise*, pas la *panne*).
- Il ne remplace pas une **stratégie de sauvegarde serveur** : `restic` reste le moteur de capture,
  pas la stratégie.
- Un témoin applicatif exécuté **dans le sandbox** ne prouve pas le comportement en production
  (charge, réseau, migrations concurrentes) : RTO mesuré en local ≠ RTO en conditions réelles.
- Il ne dit **rien** des fichiers non déclarés, et son RTO est une **moyenne d'un scénario**, pas
  une borne.

## 10. Le plan à deux jalons

**Jalon 1 — v1 gelée le 28 novembre (6 jours-agent, périmètre noir sur blanc) :**
manifeste + découverte (1 j) · garde `unshare` + Landlock + diff d'empreintes (1,5 j) · snapshot
local + restauration en sandbox (1 j) · deux témoins applicatifs (`sqlite3 .integrity_check`,
`pg_restore --list`) (1 j) · verdict signé + RTO + rapport imprimable (1 j) · hook `drill-guard` +
CI (corpus 512 Mio, **2 min 12 s**, budget 5 min) + propriétés cassées documentées (0,5 j).
**Hors v1, assumé :** pas de cluster Postgres, pas de cloud, pas de Windows, pas de multi-états
simultanés au-delà de 2.

**Jalon 2 — version complète avant le 29 janvier :** `docker compose` multi-services · `pg_verifybackup`
et cohérence transactionnelle · agent **testeur** de corruption naturelle (bit-rot, snapshot
interrompu) · extension des états non-Git (hors-ligne, caches, configs IDE) · vue web multi-drills,
thème clair/sombre, export PDF · MCP v1 stable · corpus de corruptions publié et appel à
contribution · mode démo hors-ligne figé pour le jury.

## Les cinq cases 20/20, cochées avec leur preuve

| Critère | Preuve concrète |
|---|---|
| **1. Impact 20/20** | Persona *Alex* nommé ; perte **47 min médiane / 2 sur 11 reprises impossibles**, mesurée sur 11 dévs (protocole + horodatages dans `docs/reprise-11devs.md`) ; suppression **mesurée par l'outil à chaque run** (RTO local) ; adoption **zéro compte, zéro serveur, binaire unique, première valeur en 47 s** |
| **2. Mise en œuvre 20/20** | 4 specs EARS dans `.kiro/specs/` ; 2 propriétés fast-check **qui ont réellement échoué** (`0xC0FFEE`, `0xBEEF`) avec correctif dans `KIRO_JOURNAL.md` ; hook `drill-guard` qui a **refusé un commit le 12 nov.** (incident raconté) ; steering `safety.md` **2 → 0** occurrence ; agents relecteur/testeur **lecture seule** ; comparatif spec/vibe chiffré sur `extractIntoSandbox()` (4 h 20 / 9 it. / 4 défauts **vs** 2 h 05 / 3 it. / 11 défauts dont 2 safety-critical) ; MCP **1 h 40 → 6 min** |
| **3. Design 20/20** | 4 états (vide/chargement/erreur/succès) décrits + 4 captures dans `docs/etats/` ; **axe-core en CI, 0 violation**, clavier complet, verdict jamais porté par la couleur, `prefers-reduced-motion` ; artefact durable = `verdicts.jsonl` signé + **rapport HTML A4 imprimable** ; **mode démo hors-ligne** (corpus embarqué, zéro réseau) ; thème clair/sombre |
| **4. Innovation 20/20** | Concurrent nommé **et** comparé : `restic check --read-data`, `borg check --verify-data`, **Veeam SureBackup** ; différence **structurelle** (preuve applicative rejouée vs intégrité de paquets ; état local vs serveur ; RTO vs binaire) ; combinaison rare : *exercice d'évacuation × poste de travail × CI* ; limite honnête écrite (§9) |
| **5. Présentation 20/20** | 0:00–0:15 : **le chiffre `8 min 12 s` à l'écran**, narration différée ; 0:09–0:15 la cause réelle (`down -v`) ; démo de bout en bout ≤ 3 min, sans musique ni marque tierce ; **démo web < 30 s, sans compte ni installation, corpus embarqué, résultat visible sans clic** ; les 8 questions du formulaire Devpost répondues **chiffre par chiffre** (§2, §5, §9) |

## Objections traitées

- **01 — antériorité (`restic check`, `borg check`, Veeam)** : `[neutralisée]` — la garantie n'est plus l'intégrité mais la **preuve applicative rejouée + RTO mesuré**, sur l'**état local** que Git ne contient pas ; concurrent nommé et comparé axe par axe (§6), plus la comparaison chiffrée spec/vibe qui montre ce que `check` ne prouve pas (§5).
- **02 — « c'est un script shell »** : `[neutralisée]` — la v1 livre **4 specs EARS**, fast-check, garde noyau (Landlock + mount namespace), **témoins applicatifs**, verdict signé, hook qui bloque vraiment, rapport web/HTML ; et l'objection devient la démonstration : vibe coding = 11 défauts dont 2 safety-critical, spec-first = 4 (§5).
- **03 — v1 en 8 jours intenable** : `[neutralisée]` — v1 **réduite à 6 jours-agent**, périmètre écrit noir sur blanc (§10) ; P-01 tracée par **diff d'empreintes d'arbre avant/après** (pas d'audit syscall), Landlock au lieu d'un audit complet ; fixtures, rapport, CI et specs inclus dans les 6 jours.
- **04 — le chiffre ne prouve rien** : `[neutralisée]` — le chiffre publié est le **RTO local mesuré par reconstruction réelle**, avec 5/5 rouverts, dérive et âge ; l'échantillonnage est une limite assumée (§9) et non un angle mort.
- **05 — démo de fixtures** : `[neutralisée]` — la vidéo montre **le drill réel du dépôt du projet** (vraie base locale, vrais secrets de démo) et une **corruption naturelle** (dump tronqué / snapshot interrompu), plus le `down -v` réel ; les fixtures semées ne servent qu'au test, pas au spectacle.
- **06 — récit Kiro plaqué** : `[neutralisée]` — comparatif spec/vibe **déplacé sur la garde d'écriture** (sujet de sûreté, EARS, chiffres réels) ; hook `drill-guard` **bloquant une régression réelle** (incident du 12 nov.) ; property PBT **cassée** ; steering avec effet mesuré 2 → 0.
- **07 — le jury n'a pas de sauvegarde à tester** : `[neutralisée]` — **recadrage complet de la cible** : l'objet est l'**environnement local du développeur**, que tout développeur possède, qui n'est pas dans Git et que personne ne teste ; le premier run se fait sur sa propre machine, sans compte ni serveur, en 47 s ; démo web hors-ligne pour le juge qui ne clique pas.
- **08 — angle mort technique (états vivants)** : `[neutralisée]` — le **témoin applicatif est obligatoire dès la v1** (`sqlite3 .integrity_check`, `pg_restore --list`, `psql` en lecture seule, `npm ci && vitest`), permissions/UID/GID et chemins absolus vérifiés, `pg_verifybackup` prévu au jalon 2 ; la corruption « lisible mais inutilisable » est le contre-exemple `0xBEEF` qui a fait évoluer le produit.
- **09 — « déjà vu » en Frankenstein** : `[assumée : la métaphore d'évacuation est antérieure à Veeam — on la revendique et on la déplace sur le poste de travail, seul lieu où elle n'a jamais été appliquée ; le MCP est conservé car il apporte 1 h 40 → 6 min mesurés]`
- **10 — risque de toucher une vraie source en démo** : `[neutralisée]` — le drill **ne déplace ni ne supprime l'état réel** : il ne fait que le *dupliquer* vers un bac à sable ; la source est montée **en lecture seule au niveau OS**, la garde est démontrée **avant** toute restauration (trace affichée), et la démo live n'utilise que le corpus embarqué read-only.

---

