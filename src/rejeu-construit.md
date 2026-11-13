# Rejeu — la fiche qui est devenue du code

Les quatre jugements de ce dossier disent la même chose : **une fiche écrite
ne dépasse pas ~77/100**, parce que quatre critères sur cinq exigent des
artefacts qui n'existent que construits. Le 13 novembre 2026, la meilleure
fiche jugée (Rejeu, 73/100) a donc été **construite** — et les chiffres qu'elle
annonçait ont été remplacés par des chiffres **mesurés**.

| | Fiche V2-05 (12 nov.) | Dépôt (13 nov.) |
|---|---|---|
| Artefacts Kiro | racontés | `.kiro/specs/replay/requirements.md` (exigences EARS, chacune avec son vérificateur nommé), `KIRO_JOURNAL.md`, hook `checkpoint-guard` **éprouvé par un script en CI** |
| Contre-exemple fast-check | « graine 20261104 » | **contre-exemple réel** : la capture se capturait elle-même (`.replay/` dans l'arbre), donc deux captures du même état donnaient deux arbres — détecté par un test, corrigé, verrouillé |
| Localisation | « 18/20 » | **20/20** sur le banc, et une **session réelle d'agent** (opencode + broker MCP) où la régression est localisée en 3,0 s |
| Temps | « 41 s » | **médiane 1,90 s** par session (min 0,74 s, max 3,30 s) |
| Accessibilité | « axe 0 violation » (affirmé) | **0 violation** sur quatre pages, mesuré par `scripts/a11y.mjs` dans la CI |
| Preuve durable | — | `chain.json` (chaîne d'attestation à digest chaîné), `report.html` imprimable A4, démo hors ligne sur Pages |
| Vidéo | « plan minuté » | **66 s enregistrée**, sans narration, sorties réelles |

## Les deux jugements du dépôt construit

Un juge indépendant (la grille seule, sans la fiche d'origine ni les attaques) a
noté le **dépôt** : **60/100** au premier passage, **78/100** au second, après
les corrections listées plus bas. Les deux verdicts sont publiés en entier dans
le dépôt du projet : [`docs/jugements.md`](https://github.com/Tradoooo/rejeu/blob/main/docs/jugements.md).

| Critère | Jugement 1 | Jugement 2 |
|---|---|---|
| Impact | 8/20 | 13/20 |
| Kiro | 11/20 | 15/20 |
| Design | 14/20 | 19/20 |
| Innovation | 14/20 | 16/20 |
| Présentation | 13/20 | 15/20 |
| **Total** | **60/100** | **78/100** |

Le premier jugement a nommé 19 défauts ; presque tous ont été corrigés dans la
demi-heure suivante : contre-exemple **trouvé par une propriété fast-check**
(graine 20261104, échec sur le code d'avant le correctif), effet du steering
**mesuré** (6 faux écarts → 0), « moins de 30 s » et « moins de 60 s »
**chronométrés** (0,38 s et 0,77 s), chiffres **unifiés** dans un tableau unique,
chaîne **exportable** pour être versionnée, trace d'axe jointe — et un garde-fou
qui refuse désormais de valider une page qui ne rend rien (un bug de syntaxe
avait fait passer la démo cassée pendant une heure).

## Ce qui a été fait depuis (13 nov., 16 h)

| Ajout | Preuve |
|---|---|
| **Vidéo** (69 s, H.264, sans audio) | `docs/demo/rejeu-demo.mp4` ; toutes les sorties affichées sont produites par `scripts/capture-reel.mjs` (vraies exécutions) ; les 15 premières secondes montrent le problème **et** le chiffre |
| **Incident réel du hook** | un agent a tenté `git commit --amend` pendant une session capturée : le hook a refusé, la commande n'a jamais atteint `git` (`fixtures/session-hook/incident.md`) |
| **Relecteur / testeur** | `tools/relecteur.mjs` (lecture seule) et `tools/testeur.mjs` ; le relecteur a trouvé une exigence sans vérificateur |
| **Comparaison spec / vibe coding** | `experiments/spec-vibe/` : deux sous-agents, même fonction, suite partagée de 14 cas |
| **Comparaison des concurrents** | `docs/CONCURRENTS.md` : 20 concurrents sourcés ; elle a fait trouver un défaut de stockage (`git gc --prune=now` effaçait les arbres), corrigé par une ref par checkpoint |
| **La perte, mesurée** | étude à trois bras (5 + 9 + 9 sujets, dépôts réels, PR squashée) : sans capture, l'itération se retrouve 4/5 mais coûte **19 à 73 min** d'archéologie `git fsck` ; avec capture, **9/9**. Notre outil n'est pas plus rapide qu'un agent qui refait la boucle : **il supprime le travail, pas la latence** (`docs/PERTES-resultats.md`) |
| **Fréquence du problème** | **616 PRs mergées** analysées sur 10 dépôts réels : **615 (99,8 %)** squashées, **204 (33,1 %)** portaient une histoire d'itération effacée (`scripts/measure-frequency.mjs`) |
| **Capture non coopérative** | `packages/proxy/` : un proxy MCP enveloppe le serveur d'outils de l'agent et capture chaque changement d'état. Prouvé sur un agent réel : **3 appels → 2 checkpoints**, l'appel de lecture n'en produit aucun. 4 tests dédiés |
| Session réelle d'agent | `fixtures/session-agent/` (opencode + broker) : régression localisée à l'**itération #0 en 3,0 s** |
| Session proxy | `fixtures/session-proxy/` (opencode + proxy) : capture automatique, sans coopération |

## Ce qui reste à faire, écrit noir sur blanc

- Le banc de 20 sessions a des **défauts injectés par script** ; les arbres,
  les exécutions et les temps, eux, sont réels.
- L'étude de perte a des **sujets agents**, pas humains : la comparaison entre
  bras est valide, le temps humain reste à chronométrer.
- La capture non coopérative suppose que l'agent passe par un serveur MCP
  enveloppé.
- L'agent personnalisé en lecture seule, la comparaison spec/vibe coding
  chiffrée et l'incident de hook « ayant bloqué une régression » **n'existent
  pas** : la grille les exige, le dépôt ne les fournit pas encore.

## Où le voir

- Dépôt : <https://github.com/Tradoooo/rejeu>
- Démonstration hors ligne : <https://tradoooo.github.io/rejeu/>
- Rapport de la session réelle : <https://tradoooo.github.io/rejeu/report-agent.html>
- Mesures : <https://github.com/Tradoooo/rejeu/blob/main/docs/MESURES.md>

## Ce que la fiche annonçait et que le dépôt ne tient pas encore

La fiche V2-05 annonçait un « taux d'accord de décision de 78 % (14/18) » en
mode re-run : **rien dans le dépôt ne produit ce chiffre**. Il n'est donc pas
repris. De même, la comparaison « spec vs vibe coding » (3 h 20 / 1 h 05) et
les 18 chiffres non prouvés de la fiche **ne sont pas repris** : le dépôt ne
les honore pas encore.
