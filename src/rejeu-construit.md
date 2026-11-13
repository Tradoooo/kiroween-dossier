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

## Ce qui a été fait depuis (13 nov., 16 h)

| Ajout | Preuve |
|---|---|
| **Vidéo** (66 s, H.264, sans narration) | `docs/demo/rejeu-demo.mp4` ; toutes les sorties affichées sont produites par `scripts/capture-reel.mjs` (vraies exécutions) |
| **Capture non coopérative** | `packages/proxy/` : un proxy MCP enveloppe le serveur d'outils de l'agent et capture chaque changement d'état. Prouvé sur un agent réel : **3 appels → 2 checkpoints**, l'appel de lecture n'en produit aucun. 4 tests dédiés |
| Session réelle d'agent | `fixtures/session-agent/` (opencode + broker) : régression localisée à l'**itération #0 en 3,0 s** |
| Session proxy | `fixtures/session-proxy/` (opencode + proxy) : capture automatique, sans coopération |

## Ce qui reste à faire, écrit noir sur blanc

- Le banc de 20 sessions a des **défauts injectés par script** ; les arbres,
  les exécutions et les temps, eux, sont réels.
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
