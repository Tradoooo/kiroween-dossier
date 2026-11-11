# Projet G — Tour de rôle

## G. Tour de rôle — un squelette d'ordonnancement sous contraintes et ses deux applications

### G.1 Fiche d'identité

| | |
|---|---|
| Nom de travail | Tour de rôle. En anglais : « Rota — a scheduling skeleton ». |
| Trigramme | ROT. Dépôt cible `rota`. |
| Catégorie | Skeleton Crew |
| En une phrase | Un noyau d'ordonnancement sous contraintes, maigre et lisible en une heure, qui tourne dans le navigateur, rend **toujours** le même plan pour la même graine, et qui explique chaque refus par un noyau insatisfaisable minimal — plus deux applications que tout sépare : le planning des bénévoles d'une banque alimentaire et le calendrier d'un championnat. |
| Public | D'abord le développeur qui part du squelette ; ensuite les coordinateurs bénévoles, les dirigeants de club, les organisateurs de tournois, les planificateurs de permanence. |
| Idée centrale | Un solveur n'est utile que s'il sait dire **pourquoi pas**. Le squelette rend ça mesurable : refus expliqué, plan stable, résultat reproductible à la graine près, tout dans le navigateur, sans compte. |
| Ce qui existe déjà | Timefold/OptaPlanner (Java/Kotlin, Apache-2.0, serveur, 10 692 commits, courbe d'apprentissage) ; les outils de planning SaaS (comptes, abonnement, données hébergées) ; les tableurs et leurs macros. |
| Ce qui est différent | Personne ne propose un noyau maigre, hors ligne, déterministe, borné en temps, qui explique chaque refus et se pilote depuis un simple fichier de configuration déclaratif. |
| Prix visés | Best Skeleton Crew, prix globaux, Best Demo. |
| Charge | 7 jours-agent en périmètre minimal, +2,5 pour les options (voir G.14). |

### G.2 Ce que la catégorie demande, et la réponse

| Ce que dit le règlement | Réponse de Tour de rôle |
|---|---|
| « Un gabarit assez léger pour être clair » | `core` ≤ 2 600 lignes, `ui` ≤ 1 800, gabarit ≤ 200. Un concept par fichier. Garde `loc-budget` en hook Kiro **et** en CI : le budget n'est pas une intention, c'est une porte qui refuse le merge. |
| « Assez souple pour servir à des cas variés » | Cinq points d'extension nommés (`defineResources`, `defineSlots`, `defineConstraints`, `defineObjective`, `definePresentation`) et **un seul fichier de configuration par application**. Aucune application ne modifie `core`. |
| « Deux applications distinctes » | `apps/foodbank-rota` et `apps/tournament-fixtures` : données, logique métier, objectif, présentation, partage et public différents (tableau G.9.4), ≤ 700 lignes propres chacune. |
| « Deux dossiers séparés dans le dépôt » | `apps/foodbank-rota/` et `apps/tournament-fixtures/`, chacun avec son `rota.config.ts`, ses données d'exemple et son entrée de build. |
| La polyvalence doit être **montrée**, pas affirmée | L'**épreuve de l'inconnu** (G.13.4 et G.16) : une personne qui n'a jamais vu le dépôt tire une troisième application du squelette en moins de 15 minutes, chronométrée à l'écran. |

### G.3 Problème, public et pourquoi maintenant

Le problème n'est pas « mal calculer un planning ». C'est **ne pas pouvoir expliquer un planning**. Celui qui l'a fait passer deux heures dessus, puis passe la semaine à se justifier : « pourquoi pas mardi ? », « pourquoi toujours moi ? », « pourquoi on ne peut pas juste décaler ce match ? ».

- **Nadia, coordinatrice bénévole d'une banque alimentaire.** Dimanche 8 novembre 2026, 21 h 40. Elle a 34 bénévoles, 5 créneaux par semaine, 8 semaines à couvrir. Elle travaille sur un tableur : elle recolle les disponibilités envoyées par messages, se trompe une semaine sur deux, et finit par appeler toujours les cinq mêmes personnes — celles qui disent oui. Deux bénévoles sont partis en octobre en disant « on ne me demande jamais rien d'autre que le port de charges ». Le RNA recense les associations françaises (licence Etalab 2.0) ; combien d'entre elles font du planning bénévole à la main : **À vérifier**.
- **Youssef, dirigeant bénévole d'un club amateur.** 6 équipes, 3 terrains, 12 tours. Chaque lundi un terrain est déclaré impraticable, et il refait le calendrier entier à la main — donc il déplace huit matchs quand trois suffiraient, et il doit prévenir huit équipes au lieu de trois. Le nombre de clubs amateurs concernés en France : **À vérifier**.
- **Les deuxièmes lecteurs** : les bénévoles qui consultent leur créneau sur leur téléphone, les joueurs qui cherchent leur horaire, les arbitres qu'on oublie de prévenir.

Pourquoi maintenant : les solveurs industriels existent et sont excellents, mais ils supposent un serveur, un build Java ou une JVM, et un développeur qui accepte d'apprendre un DSL d'annotations avant d'obtenir sa première affectation. Le navigateur d'aujourd'hui exécute 200 000 itérations de recherche locale en quelques centaines de millisecondes sur un téléphone de milieu de gamme. La contrainte qui justifiait la lourdeur a disparu ; la lourdeur est restée.

### G.4 Objectifs, non-objectifs, indicateurs

**Objectifs**

- O1 — Un noyau lisible en une heure : `core` ≤ 2 600 lignes hors tests, un concept par fichier, aucune dépendance d'exécution hors Zod.
- O2 — Déterminisme total : `solve(input)` est une fonction pure de `(input, seed)`. Aucune lecture d'horloge, aucun aléa non semé, aucun ordre d'itération dépendant de l'insertion dans une `Map`.
- O3 — Un refus toujours expliqué : pas de `infeasible` sans noyau insatisfaisable minimal, pas de violation sans code, raison lisible et identifiants.
- O4 — Une nouvelle application en moins de 15 minutes avec Kiro et le power fourni, par une personne qui découvre le dépôt.
- O5 — Zéro serveur, zéro compte, fonctionne hors ligne une fois chargé.

**Non-objectifs**

- Pas de routage de véhicules, pas de solveur linéaire, pas de MILP.
- Pas de planification multi-jours avec dépendances de tâches (pas un ordonnanceur de projet).
- Pas de temps réel, pas de collaboration simultanée.
- Pas d'optimum prouvé : on promet le **meilleur plan trouvé dans le budget**, avec preuve de faisabilité, jamais l'optimalité (sauf `proven-optimal` sur de très petits cas, si la recherche épuise l'espace).
- Pas d'apprentissage : aucun modèle entraîné, aucun appel réseau obligatoire.

**Indicateurs, mesurés par l'outil lui-même**

| Indicateur | Cible | Où la mesure est produite |
|---|---|---|
| Résolution `foodbank-rota` (34 ressources, 40 créneaux, 120 affectations) | < 2 000 ms, 0 violation dure | `bench.json` écrit par `scripts/recette.mjs`, affiché à l'écran |
| Écart d'équité mesuré sur 8 semaines (max − min de créneaux par bénévole) | ≤ 1 | Panneau « équité » de l'application |
| Résolution `tournament-fixtures` (6 équipes, 12 tours, 3 terrains, 36 matchs) | < 5 000 ms, 0 violation dure | `bench.json` |
| Replanification d'un terrain indisponible | < 500 ms, **≤ 3 matchs déplacés** | Écran « repair » : compteur de déplacements + diff |
| Noyau insatisfaisable sur un cas forgé | ≤ 3 éléments, produit en < 1 000 ms | Écran « pourquoi pas » |
| Nouvelle application au squelette, par une personne externe | < 15 min, chronométrée | Vidéo, plan 2:30 → 2:50 |
| Lignes : `core` / `ui` / gabarit / application | ≤ 2 600 / 1 800 / 200 / 700 | Sortie de `loc-budget` |
| Poids JavaScript au démarrage | ≤ 180 Ko compressés | `bundle-budget` |

### G.5 Le concept en profondeur

**1. Le problème est un quadruplet, pas un algorithme.** Ressources, créneaux, exigences, contraintes. Tout le reste (glouton, recherche locale, noyau) n'est qu'une façon de remplir une grille. Cette séparation est ce qui rend le squelette générique : le noyau ne connaît ni « bénévole », ni « match », ni « arbitre ». Il connaît des capacités (`capabilities: string[]`) et des exigences (`need: N` de la capacité X).

**2. La tension, formalisée.** Une exigence non satisfaite est un échec, pas une préférence. Une contrainte souple est un coût. Le score est la somme pondérée des coûts ; les contraintes dures ne sont **jamais** dans le score, elles sont un prédicat booléen. C'est le point qui distingue un solveur utilisable d'un tableur : on ne peut pas « acheter » une violation dure avec un bon score ailleurs.

**3. Construction gloutonne par tension croissante.** On n'affecte pas les créneaux dans l'ordre du calendrier, on les affecte dans l'ordre de **degré de liberté** : pour chaque exigence, on compte les ressources candidates après filtrage dur (capacité, disponibilité, non-chevauchement). La plus contrainte passe d'abord — une exigence à un seul candidat possible doit être servie avant une exigence à douze. Départage déterministe : `(candidateCount, group, slotId, requirementId)` en ordre lexicographique. À chaque affectation, on choisit le candidat qui minimise le **delta de score** ; égalité tranchée par le PRNG semé, puis par `resourceId` croissant.

**4. Recherche locale : trois opérateurs, pas trente.** `swap` échange les affectations de deux ressources partageant la capacité ; `move` déplace une affectation vers un créneau compatible ; `chain` fait tourner trois affectations. Le voisinage est énuméré dans un ordre stable (index croissant), filtré par un test de faisabilité **incrémental** (on ne réévalue que les contraintes dont le domaine a changé), et évalué sur le delta de score. Acceptation : meilleure amélioration, jamais une violation dure, avec aspiration. Mémoire tabou : couples `(requirementId, resourceId)` interdits pendant `tenure = 7` itérations, sauf si l'aspiration améliore le meilleur global. Redémarrage doux si stagnation sur `2 000` itérations : on dégrade une affectation tirée au PRNG semé.

**5. Déterminisme et budget de temps : le piège, et sa solution.** Un budget exprimé en millisecondes rend le résultat dépendant de la vitesse de la machine — deux juges n'obtiennent pas le même plan. Le noyau a donc **deux modes**, explicitement typés :
- `{ mode: "deterministic", iterations: N }` — le mode par défaut, celui des tests, des benchmarks et de la vidéo. Le résultat est une fonction pure de `(input, seed, N)`.
- `{ mode: "wall-clock", deadlineMs: D, iterations: N }` — l'**anytime** de production : on s'arrête à la première des deux bornes, `onProgress(plan)` est appelé à chaque amélioration, et `budgetUsed.stoppedBy` dit laquelle a gagné. Le plan reste valide ; il n'est simplement pas garanti identique sur une machine plus lente.
La règle de conception : la borne d'itérations est **toujours** présente, même en mode mur. Le temps ne fait que couper plus tôt, jamais décider seul.

**6. Anytime, et ce qu'on montre pendant.** `solve` rend un `SolverOutput` à la fin, mais pousse des `Plan` intermédiaires (`onProgress`). L'interface affiche donc une courbe de score qui descend et un compteur de violations dures qui tombe à zéro — et si elle ne tombe pas à zéro, on bascule sur le noyau, pas sur un message d'erreur.

**7. Le noyau insatisfaisable minimal, ou « pourquoi pas mardi ».** Quand une solution faisable n'existe pas, on ne rend pas `null` : on rend le **plus petit ensemble d'exigences et de contraintes dures dont le retrait rend le problème faisable**, et on prouve qu'il est minimal. Méthode : filtre par suppression (deletion filter). Partir de l'ensemble complet `S` ; pour chaque élément `e`, tester la faisabilité de `S \ {e}` ; si elle est établie, `e` est inutile, on le retire définitivement ; sinon on le garde. Résultat : `S*` tel que `S*` soit insatisfaisable et `S* \ {e}` faisable pour tout `e` — c'est exactement la minimalité qu'on veut, et elle est **testable par propriété** (G.12, ROT-P-07). Coût : `|S|` exécutions du solveur borné. Sur les cas visés (≤ 60 exigences, ≤ 20 contraintes dures, budget 5 000 itérations), c'est quelques centaines de millisecondes ; au-delà, on plafonne et on annonce `core.truncated = true` — jamais un noyau faux présenté comme minimal.

**8. La stabilité, ou la replanification minimale.** Une replanification utile n'est pas « un nouveau plan » : c'est **le plus petit ensemble de déplacements qui restaure la faisabilité**. D'où deux mécanismes : `locked: Assignment[]` (affectations que le solveur ne peut pas toucher, traitées comme des contraintes dures) et un composant d'objectif `churn` dont le poids domine tous les autres. On affiche le diff, pas le plan : `moved: 3`, `kept: 33`, et pour chaque déplacement, la raison. C'est la fonction décisive de `tournament-fixtures`, et c'est aussi ce qui rend l'outil crédible auprès de Nadia — un planning qui bouleverse tout chaque semaine n'est jamais adopté.

**9. L'explication comme objet de première classe.** Une violation n'est pas une chaîne de caractères, c'est une structure : `{ code, severity, constraintId, message, slotIds, resourceIds, requirementIds, magnitude }`. Les codes sont stables, énumérés, traduisibles (`E_CAPACITY_MISSING`, `E_UNAVAILABLE`, `E_DOUBLE_BOOKING`, `E_CORE_EMPTY`, `E_SOFT_EQUITY`…). Le message est composé à partir des identifiants, en une phrase : « `week-3/thu-evening` demande 1 `truck-licence` de plus que les personnes disponibles ». L'interface peut donc filtrer, trier, grouper et exporter par code — et un test peut vérifier qu'aucune violation ne sort sans code ni identifiants.

### G.6 Formats et données

**Le contrat, exact** (`packages/core/src/contract.ts`, Zod = source de vérité, types inférés) :

```ts
import { z } from "zod";

export const ResourceSchema = z.object({
  id: z.string().min(1),
  kind: z.enum(["person", "team", "machine", "referee"]),
  capabilities: z.array(z.string()).default([]),          // "truck-licence", "food-hygiene", "neutral"
  attributes: z.record(z.string(), z.union([z.string(), z.number(), z.boolean()])).default({}),
  unavailable: z.array(z.object({ slotId: z.string(), reason: z.string().optional() })).default([]),
});

export const SlotSchema = z.object({
  id: z.string(),
  group: z.string(),                    // "week-3" | "round-7" : sert « un seul par groupe »
  start: z.number().int(),              // minutes depuis l'origine de la campagne — jamais une Date
  end: z.number().int(),
  place: z.string().optional(),
});

export const RequirementSchema = z.object({
  id: z.string(),
  slotId: z.string(),
  need: z.number().int().min(1),        // N ressources…
  capability: z.string(),               // …dotées de cette capacité
  hard: z.boolean().default(true),
});

export const ViolationSchema = z.object({
  code: z.enum(["E_CAPACITY_MISSING", "E_UNAVAILABLE", "E_DOUBLE_BOOKING", "E_GROUP_CLASH",
                "E_SOFT_EQUITY", "E_SOFT_ROTATION", "E_SOFT_REST", "E_SOFT_CHURN"]),
  severity: z.enum(["hard", "soft"]),
  constraintId: z.string(),
  message: z.string(),
  slotIds: z.array(z.string()),
  resourceIds: z.array(z.string()),
  requirementIds: z.array(z.string()),
  magnitude: z.number().default(1),
});
```

```ts
export interface Assignment { requirementId: string; resourceId: string; }

export interface ConstraintContext {
  resources: ReadonlyMap<string, Resource>;
  slots: ReadonlyMap<string, Slot>;
  requirements: readonly Requirement[];
  assigned: ReadonlyMap<string, readonly string[]>;   // requirementId → resourceIds
}

export interface Constraint {
  id: string;
  kind: "hard" | "soft";
  weight?: number;                                     // souples uniquement
  evaluate(ctx: ConstraintContext): Violation[];       // fonction pure, aucun accès extérieur
}

export interface Objective {
  id: string;
  components: { id: string; weight: number; measure(ctx: ConstraintContext): number }[];
  score(ctx: ConstraintContext): number;               // somme pondérée ; plus petit = meilleur
}

export interface Core {                                // présent si status === "infeasible"
  requirementIds: string[];
  constraintIds: string[];
  proof: "deletion-filter";
  trials: number;
  truncated: boolean;
}

export type Budget =
  | { mode: "deterministic"; iterations: number }
  | { mode: "wall-clock"; deadlineMs: number; iterations: number };

export interface SolverInput {
  resources: readonly Resource[];
  slots: readonly Slot[];
  requirements: readonly Requirement[];
  constraints: readonly Constraint[];
  objective: Objective;
  seed: number;
  budget: Budget;
  locked?: readonly Assignment[];                      // replanification minimale
}

export interface Plan {
  assignments: Assignment[];
  violations: Violation[];
  score: number;
  status: "feasible" | "infeasible" | "incomplete";
  seed: number;
  budgetUsed: { iterations: number; msElapsed: number;
                stoppedBy: "iterations" | "deadline" | "exhausted" | "infeasible" };
}

export interface Solver {
  solve(input: SolverInput, onProgress?: (p: Plan) => void): { plan: Plan; core?: Core };
}
```

`msElapsed` est **exclu** de toute comparaison d'égalité : le déterminisme porte sur `(assignments, violations, score, status)`.

**Une contrainte, en entier** (`packages/core/src/constraints/noDoubleBooking.ts`) :

```ts
export const noDoubleBooking: Constraint = {
  id: "no-double-booking",
  kind: "hard",
  evaluate(ctx) {
    const out: Violation[] = [];
    for (const [reqId, resourceIds] of ctx.assigned) {
      const slot = ctx.slots.get(ctx.requirements.find(r => r.id === reqId)!.slotId)!;
      for (const rid of resourceIds) {
        for (const [otherId, other] of ctx.assigned) {
          if (otherId === reqId || !other.includes(rid)) continue;
          const otherSlot = ctx.slots.get(ctx.requirements.find(r => r.id === otherId)!.slotId)!;
          if (otherSlot.start < slot.end && slot.start < otherSlot.end && otherSlot.group === slot.group)
            out.push({ code: "E_DOUBLE_BOOKING", severity: "hard", constraintId: "no-double-booking",
                       message: `${rid} est affecté deux fois dans ${slot.group}`,
                       slotIds: [slot.id, otherSlot.id], resourceIds: [rid],
                       requirementIds: [reqId, otherId], magnitude: 1 });
        }
      }
    }
    return out;
  },
};
```

**Le fichier de configuration unique** (`apps/tournament-fixtures/rota.config.ts`) :

```ts
import { defineRota, defineResources, defineSlots, defineConstraints,
         defineObjective, definePresentation } from "@rota/core";

export default defineRota({
  id: "tournament-fixtures",
  title: "League fixtures",
  locale: "en",
  data: { kind: "bundled", path: "./data/league-2027.json" },
  resources:    defineResources(parseTeamsAndReferees),
  slots:        defineSlots(parseRoundsAndPitches),
  constraints:  defineConstraints([
    oneMatchPerTeamPerRound, oneMatchPerPitchPerSlot, refereeAvailableAndNeutral,   // dures
    noConsecutiveHome /* 3 */, homeAwayBalance /* 2 */, minRestBetweenRounds /* 2 */,
    noDerbyInRoundOne /* 4 */, eveningSpread /* 1 */,                               // souples
  ]),
  objective:    defineObjective({ components: [churn /* 100 */, fairness /* 10 */, softWeight /* 1 */] }),
  presentation: definePresentation({ screens: ["grid", "violations", "repair"] }),
  solver: { seed: 20261111, budget: { mode: "deterministic", iterations: 200_000 } },
});
```

**Jeu de données d'exemple** (`data/fixtures/`, déterministe, MIT, versionné) — schéma JSON, pas de CSV pour éviter un analyseur de plus :

```json
{
  "version": 1,
  "campaign": { "id": "foodbank-2026-w45", "origin": "2026-11-02T00:00:00Z", "unit": "minutes" },
  "resources": [{ "id": "b-01", "kind": "person", "capabilities": ["truck-licence"],
                  "attributes": { "absencesUnannounced": 2 },
                  "unavailable": [{ "slotId": "w46/sat-am", "reason": "holiday" }] }],
  "slots":     [{ "id": "w46/sat-am", "group": "w46", "start": 720, "end": 900, "place": "depot" }],
  "requirements": [{ "id": "w46/sat-am/driver", "slotId": "w46/sat-am", "need": 1,
                     "capability": "truck-licence", "hard": true }]
}
```

**Sources publiques utilisables, avec leur licence**

| Source | Usage | Licence |
|---|---|---|
| **OpenLigaDB** (`api.openligadb.de`) — résultats et calendriers de ligues (Bundesliga, DEL, etc.) | Forme réelle d'un calendrier de championnat pour l'application 2 | **ODbL** (Open Database License) — vérifié le 11/11/2026 ; attribution obligatoire, partage à l'identique des bases dérivées → n'entre **pas** dans le dépôt, seulement en fixture dérivée et citée dans `NOTICE.md` |
| **RNA — Répertoire National des Associations** (data.gouv.fr, ministère de l'Intérieur) | Nombre et nature des associations, pour dimensionner le persona de l'application 1 | **Licence Ouverte / Open Licence (Etalab)** — vérifié le 11/11/2026 |
| **football-data.org** | Alternative pour un calendrier de référence | API gratuite pour les compétitions majeures ; licence des données non explicitée → **À vérifier** avant tout usage |
| **Fixtures maison** (`data/fixtures/*.json`) | Tous les chiffres de la vidéo et des tests | MIT, comme le dépôt |

Règle : **aucune donnée personnelle réelle** dans le dépôt. Les bénévoles de Nadia sont des personnages fictifs ; les noms des clubs de l'application 2 sont fictifs aussi, seuls les formats et les contraintes sont inspirés de sources publiques.

### G.7 Exigences fonctionnelles

**Noyau — contrat et solveur**

- **ROT-F-01 (I)** — LE système DOIT valider toute entrée (`SolverInput`) par Zod et rejeter un identifiant dupliqué, une exigence pointant un créneau inexistant ou une capacité inconnue, avec un message qui nomme le champ fautif.
- **ROT-F-02 (I)** — QUAND le solveur démarre en mode `deterministic`, le système DOIT rendre un plan strictement identique pour `(input, seed, iterations)` égaux, y compris l'ordre du tableau `assignments`.
- **ROT-F-03 (I)** — LE système DOIT ordonner la construction gloutonne par nombre de candidats croissant, avec départage lexicographique sur `(candidateCount, group, slotId, requirementId)`.
- **ROT-F-04 (I)** — LE système DOIT appliquer la recherche locale avec les opérateurs `swap`, `move` et `chain`, et NE DOIT jamais accepter un état portant une violation dure.
- **ROT-F-05 (I)** — QUAND `budget.mode === "wall-clock"`, le système DOIT s'arrêter à la première des bornes atteintes et renseigner `budgetUsed.stoppedBy`.
- **ROT-F-06 (I)** — TANT QUE la recherche progresse, le système DOIT appeler `onProgress` à chaque amélioration du meilleur plan, avec un plan complet et valide.
- **ROT-F-07 (I)** — SI aucune affectation complète et faisable n'existe, ALORS le système DOIT rendre `status: "infeasible"` avec un `Core` non vide.
- **ROT-F-08 (I)** — LE système DOIT garantir que le `Core` rendu est **minimal** : le retrait de n'importe lequel de ses éléments rend le sous-problème faisable.
- **ROT-F-09 (S)** — QUAND le noyau dépasse le budget alloué, le système DOIT rendre le dernier noyau trouvé avec `truncated: true` et NE DOIT PAS le présenter comme minimal.
- **ROT-F-10 (I)** — LE système DOIT respecter `locked` : toute affectation verrouillée se retrouve à l'identique dans le plan rendu, ou le système rend `infeasible`.
- **ROT-F-11 (I)** — LE système DOIT exposer le composant d'objectif `churn` (nombre d'affectations déplacées par rapport à `locked`).
- **ROT-F-12 (I)** — CHAQUE violation DOIT porter un `code` de l'énumération, un `message` lisible et au moins un identifiant dans `slotIds`, `resourceIds` ou `requirementIds`.
- **ROT-F-13 (S)** — LE système DOIT produire un journal `Trace` optionnel : pour chaque itération retenue, l'opérateur, l'identifiant déplacé et le delta de score.
- **ROT-F-14 (O)** — LE système DOIT pouvoir prouver l'optimalité sur les cas où l'espace est épuisé (`stoppedBy: "exhausted"`).

**Squelette — extension et outillage**

- **ROT-F-15 (I)** — LES cinq points d'extension `defineResources`, `defineSlots`, `defineConstraints`, `defineObjective`, `definePresentation` DOIVENT être utilisables depuis une application sans modifier `packages/core` ni `packages/ui`.
- **ROT-F-16 (I)** — LE système DOIT refuser au lint tout import profond d'une application vers l'intérieur de `core` (`@rota/core/src/…` interdit, seule l'API publique est importable).
- **ROT-F-17 (I)** — QUAND `pnpm new-rota-app <nom>` est lancé, le système DOIT produire une application qui démarre sur un jeu d'exemple en moins de 10 secondes.
- **ROT-F-18 (I)** — LE système DOIT faire échouer `pnpm loc-budget` si `core`, `ui`, `skeleton` ou une application dépassent leur budget.
- **ROT-F-19 (I)** — LE système DOIT faire échouer `pnpm seed-guard` si un fichier de `packages/core` contient `Date.now`, `new Date(`, `Math.random`, `performance.now` ou `crypto.getRandomValues`.
- **ROT-F-20 (I)** — LE système DOIT exposer une CLI (`rota solve --config … --seed … --json`) qui rend le plan et les violations au format JSON, sans navigateur.
- **ROT-F-21 (S)** — LA CLI DOIT accepter `--explain` et rendre le noyau insatisfaisable en JSON.
- **ROT-F-22 (S)** — LE système DOIT fournir des composants d'interface réutilisables : grille des affectations, liste des violations, panneau de score, écran de replanification, export imprimable.
- **ROT-F-23 (I)** — LE système DOIT rendre chaque grille exportable en tableau HTML accessible et en CSV, toute cellule commençant par `=`, `+`, `-` ou `@` étant neutralisée.
- **ROT-F-24 (S)** — LE système DOIT proposer un lien de partage qui encode la configuration, la graine et le budget dans le fragment d'adresse, et qui rouvre le même plan.

**Application 1 — planning de banque alimentaire** (`apps/foodbank-rota`)

- **ROT-F-25 (I)** — LE système DOIT charger 34 bénévoles avec capacités (`truck-licence`, `food-hygiene`, `lifting`, `reception`), disponibilités hebdomadaires et historique d'absences non prévenues.
- **ROT-F-26 (I)** — LE système DOIT construire 5 créneaux × 8 semaines, chacun exigeant N bénévoles dotés d'une capacité donnée.
- **ROT-F-27 (I)** — LE système DOIT appliquer trois contraintes dures : capacité requise, disponibilité déclarée, pas deux créneaux le même jour pour une même personne.
- **ROT-F-28 (I)** — LE système DOIT appliquer trois contraintes souples : équité (écart ≤ 1 créneau sur 8 semaines), rotation des tâches ingrates, binômage d'un nouveau avec un ancien.
- **ROT-F-29 (I)** — LE système DOIT produire une grille imprimable A4 (une page par semaine) et une liste d'appel des remplaçants triée par proximité de disponibilité puis par ancienneté d'appel.
- **ROT-F-30 (S)** — LE système DOIT produire un lien de partage en lecture seule, sans compte, ouvrable sur téléphone.

**Application 2 — calendrier de championnat** (`apps/tournament-fixtures`)

- **ROT-F-31 (I)** — LE système DOIT construire 12 tours × 3 lieux pour 6 équipes, avec arbitres.
- **ROT-F-32 (I)** — LE système DOIT appliquer trois contraintes dures : une équipe ne joue qu'une fois par tour, un terrain n'accueille qu'un match par créneau, arbitre disponible et non affilié à l'une des deux équipes.
- **ROT-F-33 (I)** — LE système DOIT appliquer cinq contraintes souples : pas deux domiciles consécutifs, équilibre domicile/extérieur, repos minimal entre deux tours, pas de derby au premier tour, répartition des soirées.
- **ROT-F-34 (I)** — QUAND un terrain est déclaré indisponible, le système DOIT proposer le plus petit ensemble de déplacements qui restaure la faisabilité, afficher le nombre de matchs déplacés et la liste des matchs intacts.
- **ROT-F-35 (I)** — SI aucune réparation n'existe sous le verrouillage courant, ALORS le système DOIT le dire, rendre le noyau insatisfaisable et proposer de relâcher un verrou nommément.
- **ROT-F-36 (S)** — LE système DOIT exporter le calendrier en iCalendar (`.ics`) et en CSV.

### G.8 Exigences non fonctionnelles

| Id | Domaine | Exigence |
|---|---|---|
| ROT-N-01 | Légèreté | Budgets de lignes de G.4 ; `core` n'a qu'une dépendance d'exécution : Zod. |
| ROT-N-02 | Poids | ≤ 180 Ko compressés au démarrage pour chaque application. |
| ROT-N-03 | Performance | `foodbank-rota` < 2 s ; `tournament-fixtures` < 5 s ; replanification < 500 ms ; mesurés sur le profil « 4× CPU ralenti » de Chrome DevTools et consignés dans `bench.json`. |
| ROT-N-04 | Déterminisme | Aucun accès à l'horloge ni à l'aléa global dans `packages/core` ; garde `seed-guard` en hook et en CI ; PRNG maison (`mulberry32`) documenté. |
| ROT-N-05 | Robustesse | Toute entrée passe par Zod ; une entrée invalide produit une liste d'erreurs typées, jamais une exception non gérée ; aucune récursion non bornée. |
| ROT-N-06 | Accessibilité | AA : contraste vérifié, navigation clavier complète sur la grille, information jamais portée par la seule couleur (code + texte + motif), `prefers-reduced-motion` respecté, tableau équivalent pour chaque vue. |
| ROT-N-07 | Vie privée | Aucune donnée ne quitte le navigateur ; pas de compte ; pas de télémétrie ; les noms des bénévoles restent locaux (import par fichier, stockage `localStorage` seulement). |
| ROT-N-08 | Hors ligne | Application installable, fonctionnelle sans réseau après le premier chargement. |
| ROT-N-09 | Langues | Anglais (langue de soumission) et français livrés ; libellés des violations traduits par code, jamais par concaténation. |
| ROT-N-10 | Indépendance | Une application n'importe que l'API publique ; le squelette ne contient aucun mot de métier (« bénévole », « match », « arbitre ») : vérifié par un test qui lit les sources de `core`. |
| ROT-N-11 | Réversibilité | Le plan est sérialisable en JSON et rechargeable ; aucune dépendance à un état interne du solveur. |
| ROT-N-12 | Sons | Aucun son, aucun réglage de volume. |

### G.9 Architecture technique

**Arborescence du dépôt**

```
/
├── .kiro/
│   ├── steering/      product.md · tech.md · structure.md · testing.md · solver.md (fileMatch)
│   ├── specs/         contract/ solver-greedy/ solver-local/ unsat-core/ explainer/ ui-kit/
│   │                  app-foodbank/ app-tournament/ skeleton-and-power/
│   ├── hooks/         loc-budget.json · seed-guard.json · properties.json · bundle-budget.json
│   ├── agents/        reviewer.md (lecture seule) · tester.md
│   ├── skills/        new-rota-app/SKILL.md
│   └── settings/      mcp.json
├── packages/
│   ├── core/          ≤ 2 600 lignes
│   │   └── src/  contract/ · solver/ (construct.ts, improve.ts, anytime.ts, core.ts)
│   │             · explain/ (codes.ts, render.ts) · rng/ · index.ts
│   └── ui/            ≤ 1 800 lignes        grille, violations, score, repair, export
├── skeleton/          ≤ 200 lignes          rota.config.ts + main.tsx + README (gabarit recopiable)
│   └── .kiro/         steering livré avec le gabarit
├── apps/
│   ├── foodbank-rota/          ≤ 700 lignes propres
│   └── tournament-fixtures/    ≤ 700 lignes propres
├── power/new-rota-app/         power Kiro : manifeste + skill + exemple
├── cli/                        relecture sans interface (CI)
├── data/fixtures/              jeux d'exemple déterministes (MIT)
└── scripts/                    loc-budget.mjs · seed-guard.mjs · recette.mjs · bench.mjs
```

**Flux de données**

```
rota.config.ts ──▶ defineResources/Slots/Constraints/Objective/Presentation
        │                                   │
        ▼                                   ▼
  fixtures JSON ──Zod──▶ SolverInput ──▶ Solver.solve()
                                            │  glouton par tension
                                            │  recherche locale (swap/move/chain)
                                            │  anytime → onProgress
                                            ▼
                            Plan { assignments, violations, score, status }
                                            │
              ┌─────────────────────────────┼──────────────────────────┐
              ▼                             ▼                          ▼
        grille + violations        core insatisfaisable        diff de replanification
        (packages/ui)              (explain/render)            (moved / kept / raisons)
              │                             │                          │
              └────────── export A4 / CSV / .ics / lien de partage ─────┘
```

**Ce qui tourne où** : tout dans le navigateur. Aucun worker serverless, aucun stockage distant. Un `Web Worker` optionnel isole les calculs longs (mode `wall-clock`) pour que l'interface ne gèle jamais — le worker reçoit `SolverInput` sérialisé et renvoie les `Plan` par messages.

**Budgets de lignes par paquet, et comparaison avec l'existant**

| Paquet | Plafond | Contenu | Référence |
|---|---|---|---|
| `packages/core` | 2 600 | contrat, PRNG, glouton, recherche locale, noyau, explications | Timefold : 10 692 commits, plusieurs dizaines de milliers de lignes, JVM |
| `packages/ui` | 1 800 | 5 composants + thème + exports | — |
| `skeleton` | 200 | une application vide qui démarre | — |
| une application | 700 | son métier uniquement, soit < 20 % de ce qu'elle utilise | — |

**Les cinq points d'extension, et ce que chaque application y met**

| Point | Rôle | `foodbank-rota` | `tournament-fixtures` |
|---|---|---|---|
| `defineResources` | Déclarer les ressources et leurs capacités | Parse les bénévoles et leurs capacités, disponibilités, absences | Parse les équipes, terrains, arbitres et affiliations |
| `defineSlots` | Déclarer les créneaux et leurs groupes | 40 créneaux, groupe = semaine | 36 créneaux, groupe = tour |
| `defineConstraints` | Fournir les contraintes dures et souples | capacité, disponibilité, un seul par jour, équité, rotation, binômage | une équipe par tour, un match par terrain, arbitre neutre, domicile, repos, derby, soirées |
| `defineObjective` | Pondérer les composants | équité (10), pénibilité (3), churn (100) | churn (100), équilibre (10), souples (1) |
| `definePresentation` | Choisir les écrans et le thème | grille A4, liste d'appel, partage | grille des tours, violations, repair, export `.ics` |

**G.9.4 La preuve de polyvalence**

| | `foodbank-rota` | `tournament-fixtures` |
|---|---|---|
| Forme des données | Des personnes avec des capacités et des indisponibilités datées | Des entités symétriques (équipes) qui s'affrontent sur des lieux |
| Logique métier | Couverture de créneaux par compétence, sur 8 semaines | Tournoi : chaque paire une fois, symétrie domicile/extérieur |
| Objectif dominant | **Équité** entre personnes | **Stabilité** du calendrier lors d'une replanification |
| Contrainte la plus dure à tenir | Pas deux créneaux le même jour | Un arbitre non affilié, disponible |
| Présentation | Grille papier A4, liste d'appel téléphonique | Grille par tour, diff de réparation, `.ics` |
| Mode de partage | Lien lecture seule pour les bénévoles | Fichier `.ics` envoyé aux clubs |
| Public | Une coordinatrice et 34 bénévoles | Un dirigeant, 6 équipes, 3 arbitres |
| Ce qui est identique | Contrat, solveur, noyau, explications, 5 composants d'interface | |
| Lignes propres | ≤ 700 | ≤ 700 |

### G.10 Sécurité et modèle de menace

| Ce qui peut mal tourner | Parade |
|---|---|
| Un fichier de configuration malveillant (capacité énorme, `need: 99999`, identifiants dupliqués) fige le navigateur | Zod + bornes dures : `resources ≤ 5 000`, `slots ≤ 2 000`, `requirements ≤ 20 000`, `need ≤ 50` ; rejet avant tout calcul |
| Un `onProgress` qui rend un plan partiel et casse l'interface | Le plan partiel est validé par le même schéma que le plan final ; l'interface ne rend jamais un plan non validé |
| Injection HTML via un nom de bénévole ou un message de violation | Aucun `innerHTML` ; rendu React ; neutralisation des préfixes de formule à l'export CSV |
| Un lien de partage forgé injecte une configuration arbitraire | Décodage → Zod → bornes ; échec = écran par défaut + message, jamais une exception |
| Fuite de données personnelles des bénévoles | Tout reste dans `localStorage` ; aucun appel réseau ; aucun modèle de langage ; export explicite seulement |
| Déterminisme trahi par une dépendance | `seed-guard` en CI ; test qui grep `core` pour `Date`, `Math.random` ; PRNG unique et testé |
| ReDoS | Aucune expression régulière fournie par l'utilisateur ; les règles de nommage restent des comparaisons de chaînes |
| Boucle infinie dans la recherche locale | Compteur d'itérations toujours présent, même en mode mur ; budget maximal dur de 10⁷ itérations |
| Un noyau faux présenté comme minimal | Propriété ROT-P-07 exécutée sur chaque PR ; `truncated` obligatoire quand le budget a coupé |

### G.11 Interface et direction artistique

Le squelette est **volontairement nu** : une seule typographie (une grotesque système), une échelle d'espacement de 4 px, une palette neutre (encre `#1b1b1f`, papier `#fbfaf7`, un seul accent), des traits de 1 px. Aucun dégradé, aucune ombre, aucun son. Le nom « Rota » s'écrit en bas de chaque écran du gabarit : la nudité est la signature.

**Écrans communs** (dans `packages/ui`, donc identiques dans les deux applications)

| Écran | Contenu | États à soigner |
|---|---|---|
| `AssignmentGrid` | lignes = ressources, colonnes = groupes, cellules = créneaux | vide, partiel, complet, verrouillé |
| `ViolationList` | liste groupée par code, filtrable, chaque ligne = code + message + identifiants | aucune violation, violations dures, violations souples seulement |
| `ScorePanel` | score, courbe de progression, `stoppedBy`, graine | en cours, terminé, coupé par le budget |
| `RepairPanel` | diff `moved / kept`, raison par déplacement, bouton « relâcher un verrou » | réparable, non réparable, noyau affiché |
| `ExplainPanel` | noyau insatisfaisable, éléments listés, preuve de minimalité | noyau complet, noyau tronqué |

**Pourquoi chaque élément visuel améliore la fonction** — c'est la question que pose la catégorie voisine, et la réponse vaut ici aussi :

- Une violation dure est rouge **et** porte un code **et** un motif hachuré : trois canaux, donc lisible par un daltonien et copiable dans un courriel.
- La courbe de score n'est pas une décoration : elle prouve que le solveur travaille pendant l'attente, ce qui rend le budget de temps acceptable au lieu d'être subi.
- Le compteur `moved / kept` de l'écran de réparation est le chiffre qui convainc Youssef : trois matchs déplacés au lieu de huit, donc trois appels téléphoniques au lieu de huit.
- La liste des violations est triable par code, parce qu'un planificateur traite les problèmes par catégorie, pas par ordre d'apparition.

**Thèmes** : `foodbank-rota` en tons papier et chaud (lecture imprimée) ; `tournament-fixtures` en tons froids avec les couleurs du club, réglables par configuration. Le contraste AA est vérifié par un jeton unique testé automatiquement.

### G.12 Propriétés à tester

Générateurs fast-check : `arbResource`, `arbSlot`, `arbRequirement`, `arbSolverInput(bounds)` (produit des entrées **faisables par construction** pour une partie des tests, et des entrées volontairement surcontraintes pour le noyau). Le budget est toujours en mode `deterministic` avec `iterations ≤ 20 000` pour tenir en CI.

| Id | Invariant exact | Générateur |
|---|---|---|
| ROT-P-01 | Pour tout `(input, seed, budget)`, `solve` appelé deux fois rend des plans dont `assignments`, `violations`, `score` et `status` sont **structurellement égaux** (égalité profonde, ordre compris). | `arbSolverInput` × `arbSeed` |
| ROT-P-02 | Aucun plan rendu avec `status === "feasible"` ne contient de violation `severity === "hard"`. | `arbSolverInput` |
| ROT-P-03 | Si `status === "infeasible"`, alors `core` est défini, non vide, et le sous-problème restreint à `core` est insatisfaisable. | `arbOverconstrainedInput` |
| ROT-P-04 | `solve` ne lit aucune horloge ni aucun aléa global : le module `packages/core` n'importe ni `Date` ni `performance` ni `crypto`, et le résultat est identique sous `--seed` figé après un `Object.freeze` profond des entrées. | Test statique (lecture des sources) + `arbSolverInput` |
| ROT-P-05 | La recherche locale ne dégrade jamais le score du meilleur plan au-delà de `startScore × (1 + ε)` avec `ε = 0`, c'est-à-dire que `score_final ≤ score_initiale`. | `arbSolverInput` + `arbInitialPlan` |
| ROT-P-06 | Stabilité : pour tout plan faisable `P` et tout sous-ensemble `L ⊂ P` verrouillé, rejouer `solve` avec `locked = L` rend un plan qui contient `L` à l'identique et dont `churn ≤ |P \ L|`. | `arbSolverInput` × `arbLockSubset` |
| ROT-P-07 | Minimalité du noyau : pour tout `e ∈ core`, le sous-problème `restreindre(core \ {e})` est faisable. (Testé par ré-exécution sur chaque élément : coût `|core|` résolutions bornées.) | `arbOverconstrainedInput` |
| ROT-P-08 | Toute violation porte un `code` de l'énumération, un `message` non vide, et au moins un identifiant non vide dans ses trois listes. | `arbSolverInput` + `arbViolation` |
| ROT-P-09 | Équité : sur tout plan rendu par `foodbank-rota`, `max(comptes) − min(comptes) ≤ 1` ; et la somme des affectations égale la somme des `need`. | `arbFoodbankInput` |
| ROT-P-10 | Un `SolverInput` sérialisé puis relu (JSON + Zod) produit le même plan : `solve(parse(stringify(x))) === solve(x)`. | `arbSolverInput` |
| ROT-P-11 | Le repli d'un terrain (contrainte d'indisponibilité ajoutée) rend un plan faisable avec `moved ≤ 3` sur les entrées générées à cette fin, ou rend `infeasible` avec un noyau nommant le terrain. | `arbFixtureInput` × `arbPitchClosure` |
| ROT-P-12 | Aucune cellule exportée en CSV ne commence par un caractère de formule non neutralisé. | `arbCellText` |

Ces douze propriétés sont rattachées aux critères d'acceptation correspondants dans les `requirements.md`, et fast-check **conserve les graines** des contre-exemples trouvés : chaque contre-exemple devient un test de régression nommé dans `KIRO_JOURNAL.md`.

### G.13 Stratégie Kiro

| Fonction de Kiro | Emploi précis | Preuve produite dans le dépôt |
|---|---|---|
| **Specs de fonctionnalité** | Une spec par lot, dans l'ordre des dépendances (tableau ci-dessous) | `.kiro/specs/<lot>/requirements.md`, `design.md`, `tasks.md` |
| **Analyse des exigences** | Passée sur `requirements.md` avant chaque `design.md`, en IDE et en CLI | Journal : contradictions trouvées et corrigées, datées |
| **Correctness / PBT** | Les 12 propriétés de G.12 générées avec fast-check et rattachées aux critères | `packages/core/test/properties/*.test.ts` + contre-exemples au journal |
| **Exécution parallèle des tâches** | Les deux applications partent en parallèle dès l'API figée | Deux branches, deux journals, zéro modification de `core` |
| **Specs de correction de bogue** | Chaque bogue sérieux donne une spec conservée | `.kiro/specs/fix-<bogue>/` — au moins trois attendues |
| **Steering** | `solver.md` en `fileMatch` sur `packages/core/**` : vocabulaire du contrat, interdits (horloge, aléa, état global), forme d'une contrainte, forme d'une explication | Avant/après sur une contrainte écrite sans steering puis avec |
| **Hooks** | `loc-budget` (enregistrement dans `packages/**`), `seed-guard` (enregistrement dans `packages/core/**`), `properties` (enregistrement dans `packages/core/src/solver/**` → lance ROT-P-01 à 08), `bundle-budget` (après tâche de spec) | Sorties de hook dans le journal, nombre de déclenchements, un cas où un hook a bloqué une erreur |
| **Agents personnalisés** | `reviewer.md` en lecture seule (relit une PR contre le contrat et les budgets) ; `tester.md` (écrit propriétés et tests unitaires, ne touche pas `core/src`) | Rapports d'agent joints aux PR |
| **Skills** | `new-rota-app` : la procédure exacte pour tirer une application du gabarit | `.kiro/skills/new-rota-app/SKILL.md` |
| **Powers** | `power/new-rota-app` : manifeste + skill + un exemple complet (une troisième application minimale) | `power/new-rota-app/` publié dans le dépôt |
| **MCP (optionnel)** | Serveur de documentation pour vérifier l'API Zod, serveur navigateur pour les captures de la vidéo | `.kiro/settings/mcp.json` + journal |
| **CLI sans interface** | Relecture automatique en CI : `kiro … --headless` sur les `requirements.md` modifiés | Étape de CI commentée dans `.github/workflows/` |

**Les specs, dans l'ordre**

| Spec | Parcours | Contenu | Propriétés |
|---|---|---|---|
| `contract` | Exigences d'abord | ROT-F-01, 12 ; schémas Zod, types, bornes | ROT-P-08, 10 |
| `solver-greedy` | Exigences d'abord | ROT-F-03, 05, 06 ; construction par tension | ROT-P-01, 04 |
| `solver-local` | Conception d'abord | ROT-F-04, 05, 11 ; opérateurs, tabou, anytime | ROT-P-05, 06 |
| `unsat-core` | Conception d'abord | ROT-F-07, 08, 09 ; filtre par suppression | ROT-P-03, 07 |
| `explainer` | Quick Spec | ROT-F-12, 13 ; codes, messages, rendu | ROT-P-08 |
| `ui-kit` | Conception d'abord | ROT-F-22, 23, 24 ; 5 composants | ROT-P-12 |
| `skeleton-and-power` | Quick Spec | ROT-F-15 à 21 ; gabarit, commande, power | — |
| `app-foodbank` | Exigences d'abord | ROT-F-25 à 30 | ROT-P-09 |
| `app-tournament` | Exigences d'abord | ROT-F-31 à 36 | ROT-P-11 |

**G.13.4 L'épreuve de l'inconnu**

C'est la mesure centrale de la catégorie, et elle doit être une **expérience**, pas une affirmation. Protocole figé, à exécuter une fois et à filmer :

1. Une personne qui n'a jamais vu le dépôt (ni le README, ni la vidéo) reçoit une seule phrase : « voici un squelette d'ordonnancement, fais-en le planning des permanences de la bibliothèque municipale, 6 bénévoles, 3 créneaux par semaine, 4 semaines ».
2. Elle dispose de Kiro, du power `new-rota-app` et du dépôt. Rien d'autre. Pas d'aide, pas de message.
3. On chronomètre du premier clic au premier plan affiché à l'écran, avec au moins une contrainte dure et une contrainte souple propres à son cas.
4. On enregistre : durée, nombre d'allers-retours avec Kiro, fichiers touchés — et **surtout** si `packages/core` a été modifié. Le critère de réussite est double : **moins de 15 minutes**, et **zéro modification de `core`**.
5. En cas d'échec, on ne cache pas : on note le point exact de blocage et il entre dans les risques (G.15), avec la correction appliquée avant le gel du 28 novembre.

La mesure du 22 novembre sert de répétition ; celle de la vidéo est refaite avec une autre personne et un autre domaine, pour éviter l'effet d'apprentissage.

**Ce qui distingue cette stratégie des autres projets** : le squelette est aussi un **produit pour agents**. Le power, le skill et le steering `solver.md` sont livrés dans le dépôt, ce qui veut dire que la polyvalence est démontrable par un tiers absent — y compris par un agent Kiro lancé sans contexte.

### G.14 Plan de réalisation

| Lot | Contenu | Dépend de | Jours-agent |
|---|---|---|---|
| `G0` | Dépôt, licence MIT, `.kiro` complet, CI `ci-budget` (5 min, `concurrency`, `fetch-depth: 1`), `seed-guard`, `loc-budget` | — | 0,5 |
| `G1` | `contract` : schémas Zod, types, bornes, sérialisation | G0 | 1 |
| `G2` | `solver-greedy` : construction par tension, PRNG semé, `Plan`, `budgetUsed` | G1 | 1 |
| `G3` | `solver-local` : `swap`/`move`/`chain`, tabou, anytime, `onProgress`, worker | G2 | 1 |
| `G4` | `unsat-core` : filtre par suppression, `Core`, `truncated` | G2 | 1 |
| `G5` | `explainer` : codes, messages, `ExplainPanel` | G4 | 0,5 |
| `G6` | `ui-kit` : 5 composants, thème, exports A4/CSV | G1 | 1 |
| `G7` | `skeleton-and-power` : gabarit, `new-rota-app`, power, skill | G1–G6 | 0,5 |
| `G8` | `app-foodbank` | G7 | 1 |
| `G9` | `app-tournament` (dont `RepairPanel` et `.ics`) | G7 | 1 |
| `G10` | Hébergement des trois sites, README-carte, `NOTICE.md`, benchmarks, répétition de l'épreuve de l'inconnu | G8, G9 | 0,5 |
| Options | Lien de partage (0,5) · `Trace` (0,5) · MCP + relecture CLI (0,5) · troisième application d'exemple dans le power (0,5) · mode `wall-clock` + worker (0,5) | — | 2,5 |

**Périmètre minimal : 7 jours-agent.** G8 et G9 avancent en parallèle dès G7 terminé.

**Jalons et gel**

| Date | Ce qui doit être **mergé** sur `main` |
|---|---|
| 14 novembre | `G0` + `G1` : dépôt public, licence, CI, contrat figé. Rien d'autre ne peut démarrer sans ça. |
| 18 novembre | `G2` + `G3` + `G4` : le solveur résout, explique, et prouve la minimalité. **C'est le point de non-retour** : sans noyau insatisfaisable, l'idée perd sa différence. |
| 22 novembre | `G6` + `G7` + **répétition de l'épreuve de l'inconnu** (mesure de référence, avec une personne externe). |
| 26 novembre | `G8` + `G9` mergés, chiffres de `bench.json` conformes aux cibles de G.4. |
| **28 novembre** | **Gel vidéo.** Avant cette date doivent être mergés : tout le périmètre minimal, **plus** le lien de partage et le mode `wall-clock`, parce que les deux apparaissent à l'écran. Le `Trace` et MCP peuvent rester en option s'ils menacent le gel. |
| 29 novembre → 2 décembre | Captation, montage, textes Devpost, billet de blog. Aucun code de fonctionnalité. |
| 3 décembre | Soumission (marge d'un jour avant la clôture du 4). |

**Ce qui n'entre pas si le calendrier glisse, dans l'ordre où on coupe** : `Trace`, MCP, `.ics`, troisième application du power, mode `wall-clock` (le mode déterministe suffit à démontrer, l'anytime est un argument de plus).

### G.15 Risques et parades

| Risque | Prob. | Impact | Parade | Plan B |
|---|---|---|---|---|
| Le noyau insatisfaisable est trop lent et la vidéo perd son moment fort | Moyenne | **Fort** | Budget d'itérations bas (5 000) pendant le calcul du noyau ; plafond `truncated` ; cas forgé à 3 éléments pour la démo, produit en < 1 s | Montrer le noyau sur le petit cas et annoncer le plafond honnêtement |
| Le déterminisme casse à cause d'un ordre de `Map` ou d'un tri instable | Moyenne | **Fort** | ROT-P-01 et ROT-P-04 sur chaque PR ; `seed-guard` ; tri explicite partout ; PRNG unique | Consigner une graine et un cas de régression ; le déterminisme est le produit, pas un bonus |
| Les deux applications se ressemblent trop | Moyenne | Fort | Tableau G.9.4 tenu à jour ; chacune doit avoir un écran et un objectif dominants qui lui sont propres (équité vs stabilité) ; relecture par l'agent `reviewer` | Rendre l'application 2 plus « tournoi » : ajout de la symétrie aller/retour et du derby |
| Le squelette grossit sous la pression des applications | Moyenne | Fort | `loc-budget` bloquant en hook **et** en CI ; tout besoin d'application passe par un point d'extension, sinon reste dans l'application | Couper une fonctionnalité d'application plutôt que le budget |
| L'épreuve de l'inconnu dépasse 15 minutes | Moyenne | **Très fort** (c'est la preuve centrale) | Répétition le 22 novembre ; README-carte d'une page ; skill `new-rota-app` très explicite ; le gabarit démarre sans configuration | Changer de preuve : une application créée par un agent Kiro sans steering, et documenter l'écart |
| Timefold paraît plus crédible au jury | Faible | Moyen | Nommer Timefold et ce qu'il fait bien (G.1) ; montrer la différence en une phrase et par un chiffre (temps de mise en route) | Insister sur le navigateur, le hors-ligne, le déterminisme et l'explication |
| Contraintes trop simplifiées → un jury trouve le solveur naïf | Moyenne | Moyen | Les contraintes des deux applications sont réelles (arbitre neutre, binômage, rotation ingrate) ; le noyau est un vrai algorithme, pas un message d'erreur | Publier les limites dans le README (« ce que ce noyau ne fait pas ») |
| Budget de 5 min de CI dépassé par les propriétés | Faible | Moyen | `iterations ≤ 20 000` en CI, tests longs hors PR ; `timeout-minutes: 5` par job | Déplacer ROT-P-07 dans un job nocturne |

### G.16 Démonstration et soumission

**Script vidéo, 0:00 → 3:00.** Voix off en anglais (langue de soumission), donnée mot pour mot ; aucune musique, aucune marque tierce à l'écran, aucun logo. Captation en 1440×900, navigateur plein écran, une seule police système.

| Minutage | Image (plan) | Voix off, mot pour mot |
|---|---|---|
| 0:00 – 0:08 | Écran noir, puis une phrase en blanc : « Why not Tuesday? » | « Every schedule has a question behind it. Why not Tuesday? Why always me? » |
| 0:08 – 0:20 | Nadia, tableur ouvert, 34 lignes, une colonne de noms surlignée | « Nadia runs a food bank. Thirty-four volunteers, five shifts a week, eight weeks. Every Sunday she spends two hours on a spreadsheet, and calls the same five people. » |
| 0:20 – 0:35 | L'application `foodbank-rota` : la grille se remplit, le compteur de violations dures tombe à zéro | « Rota fills the grid in under two seconds. Zero hard violations. And the fairness gap — the difference between the busiest and the quietest volunteer — is one shift. » |
| 0:35 – 0:52 | On supprime une bénévole disponible un jeudi ; écran « why not » : le noyau de trois éléments s'affiche | « Now the part that matters. Remove her Thursday. Rota does not say 'impossible'. It says: these three demands cannot hold together — and it proves nothing smaller is enough. » |
| 0:52 – 1:05 | Zoom sur le noyau : les trois identifiants, le code, la raison lisible | « A code, a readable reason, and the exact identifiers. This is the answer to 'why not Tuesday'. » |
| 1:05 – 1:20 | Bascule vers `tournament-fixtures` : 6 équipes, 12 tours, 3 terrains, 36 matchs | « Same skeleton. Completely different world: a league. Six teams, three pitches, twelve rounds. » |
| 1:20 – 1:40 | Un terrain est déclaré impraticable ; l'écran `repair` s'ouvre ; 3 lignes bougent, 33 restent | « One pitch closes. Rota moves three matches, not eight. Thirty-three stay exactly where they were. Three phone calls instead of eight. » |
| 1:40 – 1:55 | Écran de score : deux résolutions côte à côte, même graine, même plan ; puis graine changée, plan différent | « Same seed, same plan. Every time, on every machine. No server, no account, no clock. » |
| 1:55 – 2:10 | Le compteur de lignes : `core 2 4xx`, `ui 1 7xx`, `skeleton 1 9x`, apps `6xx` chacune ; le hook `loc-budget` refuse un fichier trop long | « The skeleton is small, and the machine keeps it small: a hook rejects any file that breaks the budget. » |
| 2:10 – 2:30 | Le dépôt : `.kiro/` avec specs, steering `solver.md`, hooks, deux agents, le power | « Built with Kiro end to end: nine specs, a steering file that guards the solver's contract, two hooks, two custom agents, and a power that ships with the skeleton. » |
| 2:30 – 2:50 | **L'épreuve de l'inconnu** : un tiers devant Kiro, chronomètre visible, une application « library shifts » naît et affiche son plan | « This is someone who has never seen the repository. Fifteen minutes, with Kiro and the power. A new application, with its own constraints — and not one line changed in the core. » |
| 2:50 – 3:00 | Trois adresses à l'écran : skeleton, foodbank, fixtures | « A skeleton, two applications, one honest answer to why not. » |

**Textes Devpost (anglais, à rédiger dans cet ordre)**

1. **Tagline** (une ligne) : « Rota — a lean scheduling skeleton that explains every refusal. »
2. **Ce que c'est** : le contrat en quatre objets, le solveur borné, le noyau insatisfaisable, les cinq points d'extension — 120 mots maximum.
3. **Le chiffre** : « 34 volunteers, 8 weeks, 120 assignments, under 2 seconds, zero hard violations, fairness gap of 1; 6 teams, 12 rounds, closed pitch repaired with 3 moves instead of 8. »
4. **Comment Kiro a servi** : la trame en huit points de l'annexe 2 du cadre commun, remplie depuis `KIRO_JOURNAL.md`.
5. **Ce qui existait déjà** : Timefold/OptaPlanner nommé, avec ce qu'il fait bien, et la phrase de différence.
6. **Instructions de test** : trois URL, un bouton « Load demo », aucun compte, quelle contrainte retirer pour voir le noyau.

**Bonus** — billet de blog : « What a solver owes its user is an explanation, not an optimum », publié pendant la période et mentionnant Kiroween 2026. Publication sociale : commence par `#KiroweenHackathon26`, raconte ce que le steering `solver.md` a changé dans le code produit par l'agent.

**G.16.4 La place de l'épreuve de l'inconnu dans la soumission**

Elle occupe **20 secondes de la vidéo** (2:30 → 2:50) et un paragraphe du texte Devpost, mais elle porte deux critères du jury à elle seule : *Technological Implementation* (le power et le steering produisent un résultat chez un tiers) et *Innovation* (la polyvalence est mesurée, pas déclarée). Dans le formulaire, elle est écrite noir sur blanc avec ses trois nombres : **durée mesurée**, **nombre d'allers-retours**, **zéro modification de `core`** — et, si la mesure a échoué une première fois, le chiffre de la première tentative et la correction appliquée.

### G.17 Recette

`node scripts/recette.mjs` exécute ces vérifications et écrit `recette.json` ; chacune doit rendre le résultat attendu.

- [ ] `pnpm loc-budget` → `core 24xx ≤ 2600`, `ui 17xx ≤ 1800`, `skeleton 1xx ≤ 200`, chaque app `≤ 700`, code de sortie 0.
- [ ] `pnpm seed-guard` → aucune occurrence de `Date.now`, `new Date(`, `Math.random`, `performance.now`, `crypto.getRandomValues` dans `packages/core` ; code de sortie 0.
- [ ] `pnpm test` avec `FC_SEED=20261111` → 12 propriétés vertes, temps total < 90 s.
- [ ] `rota solve --config apps/foodbank-rota/rota.config.ts --seed 20261111 --json` → `status: "feasible"`, `violations` dures vides, `assignments.length === 120`, `msElapsed < 2000`.
- [ ] Même commande deux fois → les deux JSON sont identiques octet pour octet, `msElapsed` exclu.
- [ ] `rota solve --config apps/tournament-fixtures/rota.config.ts --json` → 36 matchs, 0 violation dure, `msElapsed < 5000`.
- [ ] `rota solve --config apps/tournament-fixtures/rota.config.ts --close-pitch p2 --round 7 --json` → `feasible`, `moved ≤ 3`, `kept ≥ 33`, `msElapsed < 500`.
- [ ] `rota solve --config data/fixtures/unsat-tiny.json --explain --json` → `status: "infeasible"`, `core.requirementIds.length + core.constraintIds.length === 3`, `core.truncated === false`.
- [ ] Rejouer le noyau en retirant un élément → `status: "feasible"` (minimalité vérifiée à la main, une fois par release).
- [ ] `pnpm new-rota-app demo-check` puis `pnpm --filter demo-check build` → build vert en < 10 s, aucune modification de `packages/core` (sortie de `git status --porcelain packages/core` vide).
- [ ] E2E Playwright : les trois sites chargent, le bouton « Load demo » remplit la grille, le clavier atteint la grille et la liste des violations, axe-core ne signale aucune violation AA.
- [ ] Hors ligne : après le premier chargement, réseau coupé, rechargement → l'application fonctionne et résout avec les données mises en cache.

### G.18 Questions ouvertes

1. **Le mode `wall-clock` entre-t-il dans la vidéo ?** Il est plus impressionnant (« il travaille pendant que vous regardez ») mais il casse la promesse « même graine, même plan » à l'écran. Recommandation : le montrer à 1:40 en disant explicitement que le résultat peut varier, et garder le mode déterministe pour la démonstration chiffrée. À trancher.
2. **Le troisième domaine de l'épreuve de l'inconnu** : bibliothèque municipale, planning de permanence d'un cabinet vétérinaire, ou tournoi d'échecs ? Le choix conditionne le power.
3. **Publier `@rota/core` comme paquet, ou le garder comme gabarit à copier ?** Le gabarit est plus simple à lire et à juger ; le paquet rend l'installation crédible. Recommandation : gabarit à copier, plus un `power/` — comme pour `bare-bones`.
4. **Le budget de 2 600 lignes pour `core` est un pari.** À confirmer après le lot `solver-local`, une seule fois, avant le gel.
5. **Faut-il un worker, ou tout sur le fil principal ?** Le worker protège contre le gel de l'interface mais complique le déterminisme des messages. Recommandation : worker seulement en mode `wall-clock`.
6. **L'application 1 doit-elle écrire un fichier (PDF) ou seulement imprimer ?** L'impression navigateur est plus légère, mais Nadia veut un fichier. Recommandation : impression d'abord, PDF en option.
