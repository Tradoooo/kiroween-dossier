# 100 idées pour fermer les 22 points manquants — et le top 10

Généré le 14 nov. 2026 à partir de l'état réel du dépôt `Tradoooo/rejeu`
(jugement 2 : **78/100**), de la grille des 100 points et des 18 défauts nommés
par le juge. Les chemins d'artefacts sont ceux du dépôt réel (TypeScript/pnpm,
`packages/*`, `scripts/*.mjs`, `tools/*.mjs`, `apps/web/*`, `docs/preuves/*`).

**Avertissement honnête** : les « +N pts » sont des estimations de risque, pas
des notes. Le seul juge qui peut les trancher est un nouveau passage du juge
aveugle sur le dépôt corrigé.

## Les 3 faits mesurés avant de classer (14 nov., sur le dépôt tel quel)

| Fait | Mesure | Conséquence |
|---|---|---|
| Le thème **sombre** n'est jamais mesuré par axe | `scripts/a11y.mjs` ne teste que le thème clair ; en `colorScheme: dark`, **6 violations AA sérieuses** (liens `#0000ee` sur `#12161c` = 1,93:1 ; `.primary` blanc sur `#9dbbe6` = 1,96:1) | « axe 0 violation » est vrai **pour un seul thème** — et le thème sombre est en échec |
| Les chiffres divergent encore | `vitest run` = **40 tests** (docs : 38 puis 39) ; vidéo = **69,44 s / 1 641 986 o** (docs : 59, 66, 69 s) | le reproche « chiffres divergents » du juge est toujours vrai, deux jugements de suite |
| `rejeu demo` est **annoncé mais absent** | la commande est dans l'USAGE (`packages/cli/src/index.ts:23`) mais pas dans le dispatch (l. 149-156) | la promesse « première valeur < 60 s » n'est pas tenue |

---

# Le top 10 — dans cet ordre

| # | Idée | Ce qu'elle ferme | Effort | Ce qu'elle prouve au juge | Premier pas |
|---|---|---|---|---|---|
| 1 | **Thème sombre mesuré** | Design (19/20) + une affirmation publiée non vraie | 0,5 j | « 0 violation » **dans les deux thèmes**, avec la trace jointe | tokens de liens/bouton en sombre + run axe `--scheme dark` en CI |
| 2 | **Chiffres à source unique** | Présentation (le reproche récurrent) | 1 j | un seul générateur de vérité ; le build **casse** si un chiffre dérive | `scripts/gen-docs.mjs` + garde-fou CI (`git diff --exit-code`) |
| 3 | **`rejeu demo` qui existe** | Impact (adoption sans friction) | 0,25 j | une première valeur < 60 s, sans serveur, sans compte | implémenter la commande dans le dispatch + fixture |
| 4 | **Vidéo : le CLI en action** | Présentation (15/20) | 1 j | l'outil **tourne à l'écran**, pas un lecteur de sorties | capture terminal réelle (ffmpeg) + 15 premières secondes avec le chiffre |
| 5 | **Preuve « bisect impossible »** | Innovation (16/20) + Impact | 1 j | `git bisect` échoue (commits absents), Rejeu réussit : tableau rejouable | `tools/bisect-proof.mjs` sur les 20 sessions du corpus |
| 6 | **Devpost aligné + contrôlé** | Présentation (chiffres divergents) | 0,5 j | les 8 questions du formulaire, chacune avec un chiffre du dépôt | réécriture + `tools/check-devpost.mjs` |
| 7 | **Étude humaine (12 sujets)** | Impact (13/20) — le seul point que je ne peux pas faire seul | 3-5 j + recrutement | la perte en **minutes humaines**, pas en minutes agent | protocole + recrutement ; entre-temps : 8 sujets agents en attendant |
| 8 | **Suppression de la perte, mesurée à chaque exécution** | Impact (« l'outil supprime la perte, et le mesure ») | 1 j | chaque run écrit `seconds_saved` ; sans baseline, il refuse de conclure | `.rejeu/ledger.jsonl` + baseline versionnée |
| 9 | **Contre-exemple trouvé PAR une propriété** | Kiro (le reproche exact du juge) | 1 j | REJ-P-07 : une propriété échoue sur un commit bugué, mutant shrinké, deux sorties jointes | `scripts/find-counterexample.mjs` sur l'historique du dépôt |
| 10 | **Hook hors proxy + incident de régression bloquée** | Kiro (hook décoratif) | 1 j | le hook bloque **une vraie régression** dans un dépôt réel, incident daté et transcrit | hook git installé + reproduction du bug de stockage/`app.js` |

**Remplaçants** si tu veux d'autrescritères : « registre des preuves » (9),
« traçabilité exigence→test→preuve » (11), « spec-vs-vibe chiffré » (13),
« le dossier qui se mesure lui-même » (26).

---

# Lot A — Impact (25 idées)

1. **Étude humaine 12 sujets** — 12 développeurs volontaires, « retrouver l'itération fautive » sur une PR squashée, bras manuel vs Rejeu, à l'aveugle. [Impact +4 | M | `studies/human-v1/results.csv` + `PROTOCOL.md` | `node tools/human-study.mjs --check --min-n 12` → exit 0]
2. **Chronométrage en aveugle** — 20 sessions, ordre randomisé, évaluateur ignorant l'outil, temps médian comparé. [+3 | M | `studies/blind/timings.jsonl` | `node tools/blind-report.mjs --min-n 20` → exit 0]
3. **Ledger de suppression** — chaque exécution écrit `seconds_saved = baseline − observé`, et refuse de conclure sans baseline. [+4 | M | `.rejeu/ledger.jsonl` + `packages/core/src/ledger.ts` | `rejeu verify --ledger` → exit 0]
4. **Baselines versionnées** — temps médian de la méthode manuelle par dépôt, avec provenance (commit + horodatage), zéro saisie. [+3 | S | `baselines/index.json` | `node tools/baseline-check.mjs --strict` → exit 0]
5. **Lecteur web zéro installation** — page statique GitHub Pages qui charge un `.rejeu.json` et rejoue les versions, sans compte ni serveur. [+4 | M | `apps/web/player.html` | `node tools/e2e-web.mjs --max-ms 60000` → exit 0]
6. **Export autoportant** — `rejeu export --out session.rejeu.json` embarque états, graphe et baseline, ouvrable hors ligne. [+3 | S | `packages/cli/src/export.ts` | `node tools/open-offline.mjs` → exit 0]
7. **`npx rejeu` sans daemon** — zéro serveur, zéro compte, zéro clé, première valeur en < 60 s. [+4 | M | `packages/cli` (binaire `rejeu`) | `node tools/e2e-npx.mjs --max 60000` → exit 0]
8. **Hook post-merge natif** — `rejeu install-hook` installe un `post-merge` qui snapshot l'état, sans MCP. [+3 | S | `templates/post-merge` + `packages/core/test/hook.test.ts` | `vitest run hook` → exit 0]
9. **Capture fantôme sans agent** — `rejeu shadow watch` enregistre les états de fichiers (inotify), sans MCP ni modification de l'agent : c'est la réponse à la friction. [+3 | M | `packages/core/src/shadow.ts` | `vitest run shadow` → exit 0]
10. **Persona exécutable** — `personas/tech-lead.yaml` (rôle, contexte, stack, contrainte) génère le premier rapport : une config, pas un paragraphe. [+3 | S | `personas/tech-lead.yaml` + `rejeu persona apply` | `rejeu report --json --max-ms 60000` → exit 0]
11. **Entonnoir d'adoption local** — install → 1er run → 1re localisation, zéro télémétrie réseau, seuil d'abandon. [+3 | M | `.rejeu/funnel.jsonl` + `tools/funnel-report.mjs` | `--fail-if-step3-under 0.6` → exit 0]
12. **Corpus novembre 2026** — 10 sessions réelles de PR squashées fusionnées ce mois-ci, horodatées et rejouables. [+4 | M | `corpus/2026-11/*.rejeu.json` | `node tools/corpus-validate.mjs --since 2026-11-01 --min 10` → exit 0]
13. **Preuve « bisect impossible »** — pour chaque session : `git bisect` échoue (commits absents), Rejeu réussit, tableau côte à côte rejouable. [+3 | M | `docs/preuves/bisect-vs-rejeu.md` + `tools/bisect-proof.mjs` | `--all` → bisect_fail=20/20, replay_ok=20/20]
14. **Rapport d'impact généré** — `rejeu impact --format md` : perte / économie / preuve, chaque ligne avec sa source `fichier:ligne`. [+3 | S | `IMPACT.md` généré | `rejeu impact --check` → 0 ligne sans source]
15. **Preuve vérifiable par un tiers** — `rejeu prove` écrit `proof.json` (commit, hash des états, itération fautive, durée) vérifiable sans Rejeu. [+3 | S | `docs/preuves/proof.json` + `tools/verify-proof.mjs` | exit 0]
16. **Étude reproductible** — `make study` rejoue les 3 bras et régénère tous les chiffres publiés ; le diff doit être vide. [+3 | L | `Makefile` + `studies/repro/` | `make study && git diff --exit-code` → exit 0]
17. **Garde-fou CI « première valeur »** — test e2e chronométré du clone au premier rapport, bloquant sur 3 exécutions. [+3 | S | `.github/workflows/ci.yml` (job) | `node tools/ci-first-value.mjs --max 60000 --runs 3` → exit 0]
18. **Import direct d'une URL de PR** — première valeur sans clone ni installation. [+3 | M | `packages/core/src/github-import.ts` | `vitest run github-import` → exit 0, durée mesurée dans le test]
19. **Comparateur de méthodes** — sur le corpus : `git log -p`, `git bisect` (quand possible), lecture manuelle, Rejeu — temps médian par méthode. [+3 | M | `studies/methods/comparison.json` | `node tools/method-compare.mjs --min-n 10 --require rejeu_fastest` → exit 0]
20. **Recrutement + consentements** — 15 sessions collectées ce mois-ci via 3 communautés, consentement horodaté. [+3 | M | `studies/recruit/consents/*.json` | `node tools/consent-check.mjs --min 15 --since 2026-11-01` → exit 0]
21. **Tableau de bord local (TUI)** — ledger + entonnoir + corpus agrégés en un score d'impact horodaté, sans serveur. [+2 | M | `packages/cli/src/dashboard.ts` | `rejeu dashboard --check` → exit 0]
22. **Test anti-friction** — un test échoue si l'installation exige un compte, un serveur ou une clé. [+3 | S | `packages/core/test/zero-friction.test.ts` | exit 0, 0 appel réseau]
23. **Cinq entretiens datés** — 5 entretiens de 20 min, verbatims horodatés, chacun lié à un test e2e. [+3 | M | `studies/interviews/*.md` | `node tools/interview-check.mjs --min 5` → exit 0]
24. **Banc bas de gamme** — même parcours sur conteneur 2 cœurs / 4 Go, pour prouver l'accessibilité matérielle. [+3 | M | `studies/lowspec/results.json` | `node tools/e2e-lowspec.mjs --max 60000` → exit 0]
25. **Page d'impact publiée par la CI** — chaque chiffre horodaté, sourcé, jamais recopié à la main. [+3 | M | `apps/web/impact.html` | `node tools/publish-impact.mjs --check` → exit 0]

# Lot B — Kiro (25 idées)

26. **Contre-exemple trouvé PAR une propriété (REJ-P-07)** — une propriété fast-check échoue sur un commit bugué de l'historique du dépôt ; le mutant est shrinké et les deux sorties jointes. [Kiro +4 | M | `scripts/find-counterexample.mjs` + `docs/preuves/propriete-contre-exemple-v2.txt` | la commande affiche « trouvé par la propriété, graine, N étapes » + exit 0]
27. **Shrink du contre-exemple** — réduction automatique du mutant au plus petit fragment qui casse la propriété. [+2 | M | `packages/core/src/shrink.ts` + `packages/core/test/shrink.test.ts` | `vitest run shrink` → 6/6, mutant réduit à 1 ligne]
28. **Propriété d'unicité** — `find` renvoie le plus petit index dont le prédicat échoue (corpus entier). [+2 | M | `packages/core/test/find-property.test.ts` | fast-check 1000 cas, 0 falsification]
29. **Propriété de minimalité** — l'état trouvé est bien le premier basculement (vrai à k−1, faux à k). [+2 | M | `packages/core/test/first-faulty-property.test.ts` | fast-check 1000 cas, 0 falsification]
30. **Propriété sur la chaîne d'attestation** — toute altération d'un octet rompt la chaîne, prouvé par propriété et non par test. [+2 | M | `packages/core/test/chain-property.test.ts` | 1000 mutations, 0 chaîne acceptée à tort]
31. **Propriété d'idempotence** — rejouer deux fois le même état rend le même verdict. [+1 | S | `packages/core/test/replay-idempotent.test.ts` | 500 cas, verdicts identiques]
32. **Les propriétés sur l'historique du dépôt** — les 28 commits passent dans le property-based tester ; il en sort un vrai mutant, avec le correctif qui passe. [+3 | M | `docs/preuves/propriete-historique.md` | ≥ 1 mutant trouvé et correctif vert]
33. **Exigences EARS à vérificateur obligatoire** — outil qui refuse toute exigence sans vérificateur nommé (le cas REJ-S-01). [+3 | S | `tools/check-requirements.mjs` | échoue sur l'exigence sans vérificateur, passe sur le dépôt]
34. **Traçabilité exigence → test → preuve datée** — chaque exigence EARS renvoie vers un test et une preuve horodatée. [+2 | M | `docs/TRACE.html` + `tools/check-trace.mjs` | 100 % des exigences mappées]
35. **Hook hors proxy** — le `checkpoint-guard` installé dans un dépôt de démonstration bloque `git commit --amend` **et** `git reset --hard` pendant une capture. [+4 | M | `.githooks/checkpoint-guard` + `scripts/install-hook.sh` | test : les deux commandes → refus + message + exit ≠ 0]
36. **Incident de hook ayant bloqué une RÉGRESSION** — rejouer un vrai bug du dépôt (stockage `git gc`, ou `app.js` vide) hook armé, incident daté et transcrit. [+4 | M | `docs/preuves/incident-hook-regression.md` | le script reproduit l'échec AVANT correctif et le refus du hook]
37. **Hook dans la CI** — job dédié qui installe le hook et prouve le blocage, plus un cas négatif volontaire. [+2 | M | `.github/workflows/ci.yml` (job `hook`) | run vert + cas négatif qui échoue]
38. **Steering versionné** — règles dans `.kiro/steering/`, et le relecteur refuse un diff non conforme. [+2 | S | `.kiro/steering/rejeu.md` | `tools/relecteur.mjs --steering` sort 1 sur diff fautif, 0 sur diff conforme]
39. **Steering avant/après sur un exemple rejoué** — même scénario, avec et sans steering, chiffres publiés. [+2 | M | `docs/preuves/steering-avant-apres.md` + `scripts/measure-steering.mjs --scenario` | 6→0 faux écarts sur 7 captures, scénario rejouable]
40. **Relecteur chiffré** — corpus de diffs, défauts trouvés par le relecteur contre manuels. [+2 | M | `docs/preuves/relecteur.json` + `scripts/measure-relecteur.mjs` | « défauts : k/12 » publié]
41. **Testeur chiffré** — précision et rappel sur un corpus annoté (faux positifs compris). [+2 | M | `docs/preuves/testeur.json` | matrice de confusion publiée]
42. **Spec vs vibe : l'écart de DÉFAUTS mesuré** — même fonction, deux modes, suite de 14 cas + mutants ; on compte les défauts trouvés à l'identique, pas des durées déclarées. [+4 | M | `experiments/spec-vibe/resultats.md` + `scripts/measure-spec-vibe.mjs` | la commande affiche le nombre de défauts par mode et l'écart]
43. **Spec vs vibe : temps extraits des transcripts** — durée et allers-retours lus dans les journaux d'agent, pas déclarés. [+2 | S | `experiments/spec-vibe/temps.json` | le parseur sort les durées et le nombre d'allers-retours]
44. **Deux agents Kiro sur un mini-lot** — spec-writer + implementer, journal d'allers-retours chiffré. [+2 | M | `experiments/kiro-duo/` + `KIRO_JOURNAL.md` | rapport chiffré (allers-retours, défauts)]
45. **Conformité Kiro en CI** — le job échoue si une exigence n'a pas de vérificateur qui passe. [+3 | S | `.github/workflows/ci.yml` (job `kiro-conformite`) | passe sur `main`, échoue sur une branche de test]
46. **Taux de survie des mutants** — mutation testing du cœur : la preuve que les tests mordent. [+2 | M | `docs/preuves/mutation-score.md` + `scripts/measure-mutation.mjs` | score publié, seuil en CI]
47. **Journal vérifiable** — chaque entrée de `KIRO_JOURNAL.md` pointe vers un commit, un fichier de preuve et une commande. [+2 | S | `tools/check-journal.mjs` | 0 entrée sans commit ni preuve]
48. **MCP justifié et mesuré** — ce que le broker apporte (latence, appels capturés), chiffres publiés, et justification de l'usage. [+2 | S | `docs/preuves/mcp.json` + `scripts/measure-broker.mjs` | latence mesurée + chiffres publiés]
49. **CLI headless comme second agent réel** — session `opencode --print` capturée sans TUI, rejouée, verdict identique. [+2 | M | `fixtures/session-headless/` + `scripts/measure-headless.mjs` | index identique à la session broker]
50. **Plan de lot vérifié contre les commits** — chaque tâche cochée de `.kiro/specs/replay/tasks.md` correspond à un commit et à une preuve. [+1 | S | `tools/check-tasks.mjs` | 0 tâche cochée sans commit]

# Lot C — Design (25 idées)

51. **Axe en thème sombre** — le job ne mesure que le clair : en `dark`, 6 nœuds sont en échec réel (mesuré le 14 nov.). [+2 | S | `scripts/a11y.mjs` (+ `--scheme dark`) + `docs/preuves/a11y-sombre.json` | `node scripts/a11y.mjs --strict --scheme dark` → 0 violation]
52. **Axe strict, `incomplete` compris** — le README annonce « 0 contrôle non concluant » alors qu'un contrôle `incomplete` existe et que le script les ignore. [+2 | S | `scripts/a11y.mjs` (`--strict`) | 0 violation **et** 0 incomplet]
53. **Trace d'axe versionnée** — JSON horodaté, sha256 du rapport, version d'axe et commande exacte, joints au dépôt au lieu d'une capture muette. [+2 | S | `docs/preuves/a11y.json` + `apps/web/preuves.html` | `node tools/check-preuves.mjs` → chaque preuve a date, sha256, commande]
54. **Le juge qui ne clique pas** — l'état succès est prérendu dans le HTML : le JS ne porte plus le verdict, il ne fait qu+'animer. [+2 | M | `apps/web/index.html` + `apps/web/app.js` | Playwright `javaScriptEnabled:false` → « Itération fautive » présent]
55. **Démo en un seul fichier** — `hors-ligne.html`, données inline, zéro `fetch`, ouvrable en `file://`. [+2 | M | `apps/web/hors-ligne.html` | `node scripts/check-hors-ligne.mjs` → 0 requête réseau, verdict visible]
56. **Galerie des quatre états** — les 4 états sur les 4 surfaces, avec ancres `#etat=erreur` partageables. [+2 | M | `apps/web/etats.html` + `docs/preuves/etats/*.png` | `node scripts/check-etats.mjs` → 16 ancres, axe 0 sur chacune]
57. **Trois erreurs, pas une** — `E-DEMO-DATA`, `E-CHAINE-ROMPUE`, `E-PREDICAT-ABSENT` : message, action de reprise, fixture. [+1 | M | `fixtures/demo/erreurs/*.json` | `node scripts/check-erreurs.mjs` → 3 codes, focus sur le titre]
58. **Chargement adossé au réel** — la barre suit les durées enregistrées par checkpoint, pas un `setInterval` de 420 ms. [+1 | S | `apps/web/app.js` + `fixtures/demo/verdict.json` | écart DOM/JSON ≤ 5 %]
59. **Registre des preuves** — `docs/preuves/registre.json` (fichier, sha256, date, commande, seuil) ; un contrôle refuse tout fichier de preuve non enregistré. [+2 | M | `docs/preuves/registre.json` + `apps/web/registre.html` | `node scripts/check-registre.mjs` → 0 orphelin]
60. **Reproduction depuis le rapport** — le rapport imprime la commande exacte et un test l'exécute sur un clone du fixture pour retrouver le même index. [+2 | M | `packages/core/src/report.ts` + `scripts/verif-reproduction.mjs` | index identique, exit 0]
61. **Bundle exportable** — `rejeu export --bundle` : HTML autonome + `chain.json` + empreintes, revérifiables hors ligne. [+1 | M | `packages/cli/src/index.ts` + `docs/preuves/bundle/` | `export --bundle` puis `verify --bundle` → exit 0]
62. **`rejeu demo`** — la commande figure dans l'USAGE mais pas dans le dispatch (`packages/cli/src/index.ts:23` vs l. 149-156). [+1 | S | `packages/cli/src/index.ts` | `rejeu demo --out /tmp/demo.html` → exit 0, verdict présent, < 5 s]
63. **Page accessibilité** — méthode, résultats mesurés, limites assumées, date, commande ; les chiffres sont injectés depuis le JSON, jamais recopiés. [+2 | M | `apps/web/accessibilite.html` | `node scripts/check-accessibilite.mjs` → page == JSON]
64. **Documents générés** — `MESURES.md` et les tableaux du dossier générés depuis les JSON, garde-fou CI : toute dérive casse le build. [+2 | M | `scripts/gen-docs.mjs` | `node scripts/gen-docs.mjs && git diff --exit-code docs README.md` → exit 0]
65. **Thème explicite** — bouton clair/sombre/auto avec `color-scheme`, persistance locale, impression forcée en clair. [+1 | S | `apps/web/theme.js` + `apps/web/style.css` | `node scripts/check-theme.mjs` → 2 captures, axe 0 dans les deux]
66. **Contraste calculé** — `tokens.json` + script WCAG maison qui refuse tout token sous 4,5:1 (texte) ou 3:1 (grand). [+2 | S | `tokens.json` + `docs/preuves/contraste.json` | `node scripts/measure-contrast.mjs` → tous les ratios ≥ seuil]
67. **Planche de marque** — échelle typo, couleurs, densités, états ; test de parité entre `tokens.json` et le CSS. [+1 | M | `apps/web/design.html` + `scripts/check-tokens.mjs` | 0 token orphelin]
68. **`prefers-reduced-motion` réel** — la frappe du reel et l'auto-play ignorent le réglage aujourd'hui ; mesure sur tous les nœuds animés. [+2 | M | `apps/web/reel.js` + `scripts/a11y.mjs` | `node scripts/check-motion.mjs --reduced` → 0 animation]
69. **Reel sous contrôle** — pause, reprise, arrêt, navigation scène par scène au clavier (WCAG 2.2.2) + piste texte des scènes. [+2 | M | `apps/web/reel.html` + `apps/web/reel.js` | Espace fige la scène 2 s, 0 violation]
70. **Clavier complet** — lien d'évitement, focus déplacé sur le titre de l'état après changement, ordre de tabulation vérifié. [+1 | S | `apps/web/index.html` + `apps/web/app.js` | `node scripts/check-clavier.mjs` → 12/12 focus visibles]
71. **Zoom 200 % et 320 px** — aucun débordement horizontal, cibles ≥ 24 px (WCAG 2.5.8), tableaux défilants légendés. [+1 | S | `apps/web/style.css` + `docs/preuves/reflow-320.png` | `node scripts/check-reflow.mjs` → `scrollWidth ≤ clientWidth`]
72. **L'outil en action, filmé** — capture du CLI réel (terminal + ffmpeg, ~20 s) au lieu d'une page qui rejoue des sorties. [+3 | M | `docs/preuves/cli-action.mp4` + `apps/web/preuve.html` | la commande affichée == la commande lancée]
73. **Verdict en une phrase** — « le 3ᵉ état sur 7 a fait basculer le prédicat », bouton « copier la commande », ancre `#verdict`. [+2 | S | `apps/web/app.js` + `packages/core/src/report.ts` | `node scripts/check-verdict.mjs` → copie == commande exacte]
74. **Page 404** — GitHub Pages sert une 404 nue : page d'erreur statique, mesurée par axe. [+1 | S | `apps/web/404.html` | `node scripts/check-404.mjs` → code 200, axe 0]
75. **Budget CI publié** — la durée réelle du job a11y (build + axe dans les deux thèmes) dans `docs/preuves/ci.json`, seuil 5 min vérifié. [+1 | S | `docs/preuves/ci.json` + `scripts/measure-ci.mjs` | exit 0 si total ≤ 300 s]

# Lot D — Innovation & Présentation (25 idées)

76. **Prédicats arbitraires** — `rejeu find` accepte n'importe quel prédicat en bac à sable jetable, avec rapport signé qui le désigne : la garantie floue devient un objet nommé. [+3 | M | `packages/core/src/predicate.ts` + `packages/core/src/report.ts` | `vitest run predicate` ≥ 12/12, `rejeu verify` exit 0]
77. **Contre-exemple rejoué automatiquement** — rejouer l'exemple minimal qui réfute une affirmation et l'afficher dans le rapport. [+3 | M | `packages/core/src/contre-exemple.ts` | la mesure affiche « contre-exemples : 1/1 rejoué »]
78. **Attestation hors dépôt** — sceller `chain.json` dans un digest annexe exportable, pour prouver l'indépendance de la chaîne. [+2 | M | `packages/core/src/scellement.ts` | `rejeu verify --scellement` exit 0 + un test qui casse la chaîne et échoue]
79. **Bac à sable sans `unshare`** — publier le taux de rejeu possible quand le bac noyau est refusé, avec la commande de repli et la garantie affaiblie. [+2 | S | `scripts/measure-sandbox.mjs` + `docs/MESURES.md` | taux publié]
80. **Rejeu non coopératif complet** — plus d'appels d'agent non interceptés (aujourd'hui 3 appels → 2 checkpoints) : instrumenter le proxy et republier la mesure. [+3 | L | `packages/proxy/src/intercepteur.ts` | `pnpm measure:non-cooperatif` → 3 appels → 3 checkpoints]
81. **Limites en une page** — ce que Rejeu ne prouve pas (agent malveillant, artefacts non suivis, exécution déterministe), avec sources. [+2 | S | `docs/LIMITES.md` | `node tools/check-limitations.mjs` ≥ 8 limites sourcées]
82. **Rejeu de rejeu** — rejouer une session qui a utilisé Rejeu : la reproductibilité de bout en bout. [+2 | M | `examples/rejeu-de-rejeu/` | `rejeu find --session nested` → index attendu 2/2]
83. **Diff d'états, pas de commits** — le diff lisible entre deux états non commités, chose que `git bisect` et Aider ne savent pas faire. [+3 | M | `packages/core/src/diff-etats.ts` | `rejeu diff --entre 0 --et 2` imprime le diff]
84. **Rejeu à rebours (mode avocat)** — chercher le dernier état bon plutôt que le premier fautif, et montrer la frontière exacte. [+2 | S | `packages/cli/src/find.ts` | `rejeu find --mode dernier-bon` → frontière 2/2]
85. **Deux versions du dossier des concurrents** — une version longue et une version 8 lignes, et vérifier que la courte tient sans mot creux. [+2 | S | `docs/CONCURRENTS-court.md` | `node scripts/check-line-limits.mjs` ≤ 8 lignes]
86. **Nommer les perdants** — la fiche « pourquoi Rejeu perd face à `git bisect run` » avec les cas mesurés où bisect gagne. [+2 | S | `docs/AUTOPSY.md` | la mesure affiche 3 cas où bisect gagne]
87. **Journal des tentatives ratées** — les variantes de garantie abandonnées et la raison **mesurée** de chaque abandon. [+2 | M | `docs/JOURNAL.md` | `node tools/check-journal.mjs` ≥ 7 entrées datées]
88. **Barème de nouveauté** — un test refuse toute affirmation « aucun outil existant ne fait ça » sans concurrent nommé **et** mécanisme. [+2 | S | `tools/check-nouveaute.mjs` | exit 0 sur les 20 concurrents]
89. **Métrique de la preuve** — pour chaque page du dossier, le nombre de chiffres traçables à une commande, affiché sur l'accueil. [+2 | M | `apps/web/trace.html` + `tools/check-trace.mjs` | ≥ 80 % de chiffres traçables]
90. **Fiches V1 contre V2** — montrer la fiche et sa refonte côte à côte, avec la phrase de différenciation qui a changé et pourquoi la première était fausse. [+2 | S | `src/ver-v1-v2.md` | le contrôle affiche 1 phrase supprimée, 1 ajoutée]
91. **Chemin-fantôme appliqué au dossier** — détecter les chemins inventés dans les textes du dossier lui-même et publier le taux. [+3 | M | `scripts/ghost-path.mjs` | taux de références fantômes publié, exit 0]
92. **Ver appliqué au dossier** — faire tourner la logique de dette de mutation sur `kiroween-dossier` lui-même, verdict par ligne de diff. [+3 | M | `scripts/ver-dossier.mjs` | affiche « 0 survivant », exit 0]
93. **Le dossier comme corpus mesuré** — un compteur par page (idées, cahiers, jugements) vérifié contre le contenu réel. [+2 | M | `tools/check-counts.mjs` | écart 0 entre l'annoncé et le réel]
94. **Vidéo : le CLI à l'écran** — refaire le reel en filmant le terminal : `rejeu find` tapé, verdict affiché, sans lecteur de sorties. [+3 | M | `docs/demo/rejeu-cli.mp4` + `scripts/capture-cli.mjs` | `ffprobe` : H.264, ≥ 60 s, `rejeu find` visible à l'écran]
95. **Vidéo : 15 premières secondes** — le chiffre (20/20, 1,90 s) avant 0:08, sans narration, total < 3 min. [+3 | S | `docs/demo/rejeu-demo-v2.mp4` + `docs/VIDEO.md` | `node scripts/check-video.mjs` → chiffre à l'écran avant 8 s, durée ≤ 180 s]
96. **Durée unique** — supprimer les 59/66/69 s divergents : une seule durée générée par `ffprobe`, propagée et vérifiée en CI (mesurée : **69,44 s / 1 641 986 o**). [+2 | S | `docs/DUREE.json` + `scripts/check-duration.mjs` | écart 0 s entre les fichiers]
97. **Démo sans clic** — page statique GitHub Pages : verdict, 20/20 et commande copiable, sans compte ni installation, en < 30 s. [+3 | M | `apps/web/index.html` | `node scripts/check-demo.mjs` → premier verdict < 30 s]
98. **38 ou 39 ou 40** — trancher le nombre de tests et le faire vérifier par un script (mesuré aujourd'hui : **40**). [+2 | S | `docs/TESTS.md` + `scripts/check-tests.mjs` | `vitest run` affiche 40 passés, le contrôle exit 0]
99. **0,6 s ou 3,0 s** — une seule mesure de session (commande, machine, horodatage, écart-type) ; l'autre valeur disparaît de tous les fichiers. [+2 | S | `docs/MESURES.md` + `scripts/measure-session.mjs` | une valeur médiane, `grep "3,0 s" docs` vide]
100. **Devpost aligné** — les huit questions du formulaire Kiro, chacune avec un chiffre du dépôt, et une correspondance vérifiée par script. [+3 | M | `docs/DEVPOST.md` + `tools/check-devpost.mjs` | 8 sections, 8 chiffres, exit 0]

---

## Ce que je n'ai pas mis dans la liste, et pourquoi

- **Construire Chemin-fantôme (59/100) ou Ver (67/100)** : ce sont de bonnes fiches,
  mais elles ouvrent un second dépôt à 3 semaines de la clôture et font perdre le
  focus sur les 22 points qui restent **accessibles** sur Rejeu. À faire seulement
  si le temps de construction de Rejeu est épuisé.
- **Un second agent de présentation** : la vidéo est le seul livrable qui ne se
  corrige pas par un script. Il mérite un créneau, pas une idée.
- **Publier les chiffres de coût de l'outillage** : c'est de la transparence
  interne, pas un point de grille. Va dans le journal de bord.
