# GRILLE — notation des idées Kiroween 2026

Note chaque idée sur **100 points**, puis applique les malus. Sois **sévère** : une idée à 70 est déjà
excellente. Ne note jamais au-dessus de 85 sans une raison écrite.

## Critères

| Critère | Points | Ce que tu regardes |
|---|---|---|
| **Impact réel** | /25 | Un public nommable existe, la douleur est réelle et fréquente, quelqu'un l'utiliserait vraiment après le concours. Un outil « sympa » sans utilisateur régulier vaut 8 au plus. |
| **Innovation** | /20 | Différence nette avec l'existant (nommé dans l'idée), combinaison inattendue, aucun équivalent évident en tête des juges. Un clone amélioré vaut 6 au plus. |
| **Faisabilité** | /20 | Tient en ≤ 8 jours-agent par une personne pilotant des agents ; site statique ou un seul petit worker ; aucune dépendance à un matériel introuvable, une API payante, un compte tiers, ou un modèle de langage indispensable. |
| **Démontrabilité** | /20 | Un plan fort visible en moins de 20 secondes de vidéo, un **chiffre mesuré par l'outil lui-même**, une démo utilisable en 30 s sans compte, un résultat compréhensible par un juge non spécialiste du domaine. |
| **Potentiel Kiro** | /15 | Matière à specs, tests par propriétés, hooks, steering, agents personnalisés, powers, MCP ; une fonction où la comparaison spec contre « vibe coding » est intéressante à raconter. |

## Malus (à soustraire)

- **−20** si l'idée duplique un projet déjà soumis : `bipeur`, `packet-voyage`, `suture`, `ghost-hours`,
  `thin-air`, `bare-bones`, `placard`, ou les cinq idées déjà écrites (Disquette, Rota, Partie double,
  Exorcisme, Séance).
- **−15** si elle nécessite un serveur permanent coûteux, une API payante, une marque tierce, un texte
  religieux réel, ou des données personnelles sensibles sans garde-fou.
- **−10** si le public n'est pas nommable, ou si l'utilité disparaît après le 31 décembre.
- **−10** si la métaphore (technologie morte, costume, couture) est décorative : retire-la et l'outil
  n'est ni meilleur ni différent.
- **−5** si l'accessibilité AA ou l'absence de son par défaut est impossible à tenir.

## Bonus

- **+5** si l'idée vise un public **non développeur** bien identifié (le portefeuille du candidat est déjà
  saturé d'outils pour développeurs).
- **+5** si l'idée produit un **artefact physique ou imprimable** montrable en vidéo (feuille, carte,
  registre, disque, affiche).

## Format de sortie — strict

Tu rends **uniquement les 25 meilleures idées de ton périmètre**, triées par note décroissante, une par ligne :

```
1. [note]/100 · lot-NN · **Nom** · Catégorie · une phrase : pourquoi elle gagne (le chiffre ou le plan fort).
```

Pas d'en-tête, pas de conclusion, pas de commentaire sur les idées rejetées. **25 lignes et c'est tout.**
Si deux idées de ton périmètre sont des doublons l'une de l'autre, n'en garde qu'une et signale-le en fin de
ligne par `(absorbe l'idée NN du lot MM)`.
