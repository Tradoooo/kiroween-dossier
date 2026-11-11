# Kiroween 2026 — contexte partagé pour les cinq nouvelles idées

Document de référence, écrit le 11 novembre 2026. **À lire en entier avant d'écrire quoi que ce soit.**
Il contient : le règlement vérifié, la grille du jury, le portefeuille déjà soumis (à ne pas dupliquer),
les conventions de la maison, et la structure imposée du livrable.

Source : `https://kiroween.devpost.com/` consulté le 11/11/2026 à 15 h 30 (Paris).

---

## 1. Les quatre catégories, texte officiel

- **Resurrection** : « Bring your favorite dead technology back to life. Reimagine obsolete tech with
  today's innovations or solving tomorrow's problems. »
- **Frankenstein** : « Stitch together a chimera of technologies into one app. Bring together seemingly
  incompatible elements to build something unexpectedly powerful. »
- **Skeleton Crew** : « Build a skeleton code template lean enough to be clear but flexible enough to
  support various use cases. Show us its versatility with two distinct applications from your foundation. »
- **Costume Contest** : « Build any app but show us a haunting user interface that's polished and
  unforgettable. Bring in spooky design elements that enhance your app's function. »

Point décisif pour Costume Contest : le spooky doit **améliorer la fonction**, pas décorer.
Point décisif pour Skeleton Crew : le dépôt doit contenir **deux dossiers séparés** pour les deux applications.
Point décisif pour Resurrection : la technologie doit être **vraiment morte**, et la réinterprétation doit
résoudre un problème d'aujourd'hui ou de demain — pas seulement faire de la nostalgie.

## 2. Prix

1er 30 000 $ · 2e 20 000 $ · 3e 10 000 $ · Best Resurrection 5 000 $ · Best Frankenstein 5 000 $ ·
Best Skeleton Crew 5 000 $ · Best Costume Contest 5 000 $ · Best Startup 10 000 $ ·
Best Ghost of Kiroween Past 2 000 $ · Best Kiro Crew App 1 000 $ · Best Demo 1 000 $ ·
Bonus Blog (100 gagnants, 2 000 crédits) · Social Blitz (5 gagnants).
**Un projet ne peut gagner qu'un prix global OU un prix de catégorie, pas les deux. Les bonus se cumulent.**

## 3. Règles de soumission qui contraignent la conception

| Règle | Conséquence |
|---|---|
| Période de construction : 30 octobre 2026 → 4 décembre 2026, 14 h Pacifique (23 h Paris) | Dépôt créé après le 30/10. Code antérieur réutilisé = déclaré dans le README. |
| Construit avec Kiro, sinon disqualification à la discrétion des juges | Traces visibles : `/.kiro` à la racine, specs, hooks, steering, journal. |
| Dépôt GitHub **public**, licence open source détectable dans l'encart About, `/.kiro` non ignoré | MIT dès le premier commit + garde CI qui vérifie. |
| URL d'une app qui marche, gratuite, sans restriction jusqu'au **29 janvier 2027** | Hébergement à tenir ~2 mois. Mode démo sans compte ni installation. |
| Les juges **ne sont pas obligés de tester** : ils peuvent juger sur vidéo + texte | La vidéo et le texte portent l'essentiel de la note. |
| Vidéo **< 3 min**, publique sur YouTube, montrant le projet sur l'appareil visé, **sans musique ni marque tierce** | Script minuté obligatoire. Zéro logo tiers à l'écran, zéro musique sous droits. |
| Tous les éléments de soumission en **anglais** | UI, README, specs, vidéo en anglais. Le français peut rester en seconde langue d'UI. |
| Plusieurs soumissions autorisées si chacune est unique et substantiellement différente | Dépôts indépendants, **aucune dépendance d'un projet vers un autre** ; un utilitaire commun est recopié. |
| Crédits Kiro : 4 000 par participant, demande avant le 1er décembre | Les actions de hook de type « agent » consomment des crédits, les actions « commande » non. |
| Œuvre originale ; bibliothèques open source OK si licences respectées | Écarter par défaut le copyleft fort (AGPL/GPLv3). Tableau des dépendances + licences dans le README. |

## 4. Grille du jury — cinq critères, 20 % chacun

| Critère | Ce que le jury regarde | Ce qu'il faut produire |
|---|---|---|
| **Potential Impact** | Vrai problème, vrai public, solution utile, intuitive, accessible. « Est-ce que quelqu'un l'utiliserait ? » | Un persona nommé + une situation datée ; **un chiffre mesuré par l'outil lui-même**. |
| **Technological Implementation** | Profondeur et variété de l'usage de Kiro, stratégie d'IA, expérimentation | Plan d'usage de Kiro chiffré (specs, hooks, steering, agents, MCP, powers, PBT, Crew, CLI headless), journal au fil de l'eau, comparaison spec contre « vibe coding » sur une fonction précise. |
| **Design** | Produit complet et cohérent, pas une preuve de concept | États vides, erreurs, chargements ; accessibilité AA ; mode démo soigné. |
| **Innovation/Idea** | Nouveauté du concept, différence avec l'existant, combinaison inhabituelle de technologies ou de **données publiques** | Nommer l'existant et dire en une phrase ce qui est différent. |
| **Presentation** | La vidéo montre le projet **de bout en bout**, le pitch est clair, mémorable | Script minute par minute avec le plan fort dans les 20 premières secondes. |

## 5. Portefeuille déjà construit — à ne PAS dupliquer

| Dépôt | Catégorie | Idée en une phrase |
|---|---|---|
| `bipeur` | Resurrection | Le pager bidirectionnel (SNPP, RFC 1861) revient pour superviser des agents IA : une ligne, un code, un tap. |
| `packet-voyage` | Frankenstein | Un diagnostic réseau de 1987 (traceroute) cousu à la géographie : suivre la route physique de ses paquets, bornée par la vitesse de la lumière. |
| `suture` | Frankenstein | Git (plomberie réelle) × fichiers `.xlsx` : versionnage de tableur sans jamais dire « Git ». |
| `ghost-hours` | Frankenstein | Commits Git × agenda iCal × notes Markdown → reconstituer les heures réellement travaillées et brouillonner la facture. |
| `thin-air` | Frankenstein | La webcam transforme l'air en instrument de musique ; rien ne quitte le navigateur. |
| `bare-bones` | Skeleton Crew | Squelette d'explorateur de données (import, filtres, graphiques, lien de partage) + budget d'association + résultats de club + recensement de bonbons. |
| `placard` | Costume Contest | Audit des secrets et données perso dans l'historique Git, habillé en manoir hanté avec rituel de tri. |

Conséquences pour les nouvelles idées :
- **Éviter** la supervision d'agents IA comme idée centrale en Resurrection (déjà `bipeur`).
- **Éviter** l'exploration de fichiers/données en lecture seule en Skeleton Crew (déjà `bare-bones`).
- **Éviter** le manoir hanté et les pièces à visiter en Costume Contest (déjà `placard`).
- Le portefeuille est déjà très « outils pour développeurs ». Les nouvelles idées gagnent à viser
  **aussi** des publics non développeurs (bénévoles, familles, petites structures), parce que le critère
  « est-ce que quelqu'un l'utiliserait vraiment » se marque mieux avec un public large.

## 6. Socle technique de la maison (reconduit pour chaque projet)

- TypeScript strict, Node LTS, pnpm workspaces, Vite + React, Zod pour toute donnée entrante.
- Tests : Vitest, **fast-check** pour les propriétés, Playwright pour le bout en bout et les captures vidéo.
- CI GitHub Actions : typecheck, lint, test, build, **ci-budget (`timeout-minutes: 5`, `concurrency`, `fetch-depth: 1`)**, garde de conformité concours (`.kiro` présent et non ignoré, licence présente). E2E et bancs longs hors PR.
- Hébergement : **site statique d'abord** (GitHub Pages), données dans le navigateur. Un petit worker serverless n'est accepté que s'il est indispensable, gratuit, sans compte, et s'il ne voit jamais de donnée en clair.
- Licence MIT ; dépendances à copyleft fort écartées.
- Appels à un modèle de langage : **toujours optionnels, désactivés par défaut**, derrière une interface de fournisseur, avec une voie sans modèle pour chaque fonction. Aucun secret ni donnée personnelle envoyé à un modèle.
- Vie privée : traitement local d'abord, aucun envoi sans action explicite.
- Accessibilité : contraste AA, navigation clavier complète, information jamais portée par la seule couleur, `prefers-reduced-motion` respecté.
- **Aucun son par défaut** (règle de l'espace de travail) : tout son est derrière un réglage désactivé.
- Règles de code : **< 500 lignes par fichier, < 50 lignes par fonction**, zéro duplication, garde automatique en CI.

## 7. Conventions de rédaction des exigences

- Identifiants : `TRI-F-nn` fonctionnelle, `TRI-N-nn` non fonctionnelle, `TRI-P-nn` propriété à tester,
  où `TRI` est le trigramme donné dans le brief de l'idée.
- Priorités : **I** indispensable (périmètre minimal), **S** souhaitable, **O** optionnel, **X** exclu.
- Critères d'acceptation en **notation EARS** : « QUAND …, le système DOIT … », « TANT QUE …, le système DOIT … »,
  « SI …, ALORS le système DOIT … », « OÙ une option est activée, le système DOIT … ».
- Identifiants de code, de fichier et d'API **en anglais** (prêts à reprendre), prose **en français**.

## 8. Structure `.kiro/` attendue (vérifiée dans la documentation Kiro)

```
.kiro/
├── steering/     product.md · tech.md · structure.md · testing.md · <domaine>.md (fileMatch)
├── specs/<fn>/   requirements.md · design.md · tasks.md
├── hooks/        <nom>.json  (format v1 : trigger, matcher, action)
├── agents/       <nom>.md    (relecteur en lecture seule, testeur, permissions restreintes)
├── skills/<nom>/SKILL.md
└── settings/mcp.json
```

Le texte de soumission pose précisément ces questions — le `KIRO_JOURNAL.md` du dépôt y répond :
surfaces de Kiro utilisées et leurs différences ; agents personnalisés ; hooks et leur gain ;
spec contre vibe coding (avec durée, allers-retours, défauts trouvés) ; le steering qui a fait la
différence ; ce qu'a permis MCP ; ce que les tests par propriétés ont trouvé (chaque contre-exemple) ;
quels powers.

## 9. Structure imposée du livrable

Chaque brief suit les 18 sections du cahier des charges de la maison :

1. **X.1 Fiche d'identité** — tableau : nom de travail (français) + nom anglais de soumission, catégorie,
   en une phrase, public, idée centrale, ce qui existe déjà, ce qui est différent, prix visés, charge en jours-agent.
2. **X.2 Ce que la catégorie demande, et la réponse** — tableau : chaque exigence du règlement citée, et la réponse précise.
3. **X.3 Problème, public et pourquoi maintenant** — personas nommés, situations datées, chiffres sourcés ou marqués **À vérifier**.
4. **X.4 Objectifs, non-objectifs, indicateurs** — avec un tableau d'indicateurs chiffrés et mesurables par l'outil.
5. **X.5 Le concept en profondeur** — la mécanique centrale expliquée jusqu'au détail qui prouve qu'on a compris le sujet.
6. **X.6 Formats et données** — schémas exacts (TypeScript/Zod), exemples réels, sources de données publiques nommées avec leur licence.
7. **X.7 Exigences fonctionnelles** — tableau EARS, identifiants, priorités.
8. **X.8 Exigences non fonctionnelles** — performance, taille, accessibilité, vie privée, robustesse, offline.
9. **X.9 Architecture technique** — arborescence du dépôt complète, paquets, budgets de lignes par paquet, flux de données, ce qui tourne où.
10. **X.10 Sécurité et modèle de menace** — ce qui peut mal tourner, et la parade.
11. **X.11 Interface et direction artistique** — écrans, états vides/erreurs/chargement, palette, typographie, mouvement, et **pourquoi chaque élément effrayant améliore la fonction**.
12. **X.12 Propriétés à tester** — liste `TRI-P-nn` avec l'invariant exact et le générateur fast-check.
13. **X.13 Stratégie Kiro** — tableau : fonction de Kiro → emploi précis → preuve produite dans le dépôt.
14. **X.14 Plan de réalisation** — lots, dépendances, jours-agent, ce qui est mergé avant le gel vidéo (28 novembre).
15. **X.15 Risques et parades** — tableau risque / probabilité / impact / parade / plan B.
16. **X.16 Démonstration et soumission** — script vidéo minuté 0:00 → 3:00 avec le plan de chaque séquence et la voix off ; textes Devpost ; bonus (blog, social).
17. **X.17 Recette** — liste de vérifications exécutables (`node scripts/recette.mjs`) avec le résultat attendu, 8 à 12 points.
18. **X.18 Questions ouvertes** — les arbitrages qui reviennent au user.

## 10. Ce qui rend une idée gagnante ici — critères de qualité du brief

- **Un chiffre opposable** : l'outil produit lui-même une mesure (ko, disquettes, heures, euros, violations,
  secondes gagnées) et la vidéo la montre. Pas d'adjectif sans nombre.
- **Le plan fort dans les 20 premières secondes** de la vidéo.
- **Démo en 30 secondes sans compte** : le juge comprend et voit un résultat avant la fin de la première minute.
- **Un seul concept par fichier, cinq points d'extension nommés au maximum.**
- **L'existant est nommé** (outils concurrents réels, avec ce qu'ils font bien) et la différence tient en une phrase.
- **Honnêteté** : ce qui n'est pas mesuré est marqué **À vérifier** ; un échec documenté vaut mieux qu'une promesse.
