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

## Ce qui reste à faire, écrit noir sur blanc

- La **vidéo** n'est pas tournée.
- La capture est **coopérative** : l'agent appelle `replay_checkpoint` parce
  que le prompt le lui demande. Un proxy qui interpose les outils de l'agent
  (capture sans coopération) n'est pas fait.
- Le banc de 20 sessions a des **défauts injectés par script** ; les arbres,
  les exécutions et les temps, eux, sont réels.

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
