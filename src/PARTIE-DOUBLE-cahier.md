# Kiroween 2026 — Projet H · Partie double

Cahier des charges rédigé le 11 novembre 2026. Trigramme **LED**. Dépôt cible : `ledger`. Catégorie **Skeleton Crew**.
Ce document est la matière première des specs Kiro : chaque exigence y est identifiée (`LED-F-nn`, `LED-N-nn`,
`LED-P-nn`) et priorisée (**I**ndispensable, **S**ouhaitable, **O**ptionnel, e**X**clu). Prose en français,
identifiants de code en anglais. Ce qui n'est pas mesuré est marqué **À vérifier**. Sources consultées le 11/11/2026 :
règlement et grille Devpost (restitués dans `00-CONTEXTE-NOUVELLES-IDEES.md`), `actualbudget.org`, `hledger.org`,
`beancount.github.io`, `firefly-iii.org`.

## H. Partie double — un squelette de grand livre immuable et ses deux applications

### H.1 Fiche d'identité

| | |
|---|---|
| Nom de travail | Partie double. Nom anglais de soumission : « Ledger — a double-entry skeleton ». |
| Catégorie / trigramme / dépôt | Skeleton Crew · `LED` · `ledger` |
| En une phrase | Un noyau de comptabilité en partie double, maigre et immuable, dont chaque écriture est irréversible, chaque solde un pli sur le journal, et dont deux applications héritent des mêmes invariants prouvés : le budget privé d'un foyer et le grand livre public d'un fonds d'entraide. |
| Public | Le développeur qui part du squelette ; puis deux publics non développeurs aux antipodes de la vie privée — un foyer (Sarah) et un collectif solidaire de 6 bénévoles — et ceux qui lisent leurs liens. |
| Idée centrale | Le grand livre est le gabarit « maigre mais souple » canonique : ~4 200 lignes servent un foyer, une association, un fonds d'entraide, une banque du temps, un inventaire. Les invariants comptables donnent aux tests par propriétés une matière que peu de projets ont : **la justesse n'est pas une opinion, c'est une équation.** |
| Ce qui existe déjà | Beancount, hledger, ledger-cli (texte, développeurs, aucune interface) ; Actual Budget (open source, local-first, enveloppes, à installer) ; GnuCash (bureau, lourd) ; Firefly III (serveur PHP auto-hébergé). |
| Ce qui est différent | Personne ne propose un squelette comptable maigre, hors ligne, dans le navigateur, dont les deux applications se situent aux deux extrémités du spectre de la vie privée — l'une cache tout, l'autre publie tout — avec une chaîne de hash vérifiable. |
| Prix visés | Best Skeleton Crew (5 000 $), prix globaux, bonus Blog, Best Kiro Crew App. |
| Charge | 11 jours-agent de périmètre minimal + 3 jours d'options (H.14). |

**Non-duplication avec `bare-bones` (déjà soumis, Skeleton Crew).** `bare-bones` contient une application
`nonprofit-budget` qui **explore un CSV en lecture seule** : import, types de colonnes déduits, filtres, graphiques,
lien de partage. Partie double **tient un livre** : modèle en écriture, invariants algébriques, contre-passation,
chaîne de hash, enveloppes avec report, piste d'audit. La différence tient en un mot — *lire* contre *écrire* — et se
vérifie mécaniquement : `bare-bones` n'a aucune notion de solde, de hash ni d'immutabilité ; `ledger` n'a ni grille
exploratoire, ni déduction de types, ni adaptateur de partage par état. **Aucun code partagé, aucun paquet commun,
aucune dépendance d'un dépôt vers l'autre** ; la CI de `ledger` interdit tout import croisé. Détail en H.3.

### H.2 Ce que la catégorie demande, et la réponse

| Ce que dit le règlement | Réponse de Partie double |
|---|---|
| « lean enough to be clear » | Budgets de lignes vérifiés par le hook `loc-budget` et la CI : `core` ≤ 2 200, `ui` ≤ 1 800, `skeleton` ≤ 200, chaque application ≤ 700 lignes propres. Un concept par fichier. README-carte d'une page. |
| « flexible enough to support various use cases » | Cinq points d'extension nommés — `defineChart`, `defineRules`, `defineEnvelopes`, `defineReports`, `definePresentation` — et un fichier déclaratif par application (`ledger.config.ts`). Le même noyau porte une devise (EUR) et une unité non monétaire (heures). |
| « two distinct applications from your foundation » | `apps/envelopes` (foyer, tout privé, rien ne quitte le navigateur) et `apps/mutual-aid` (fonds, tout publié, chaîne vérifiable par un donateur). Tableau de comparaison en H.9. |
| Deux dossiers séparés dans le dépôt | `apps/envelopes/` et `apps/mutual-aid/`, plus `apps/time-bank/` généré en direct pendant la vidéo (troisième preuve, H.13 et H.16). |
| Construit avec Kiro, traces visibles | `/.kiro` non ignoré : 8 specs, 5 hooks, 5 steering dont `accounting.md` en `fileMatch` sur `packages/core/**`, 2 agents personnalisés, 1 power, `KIRO_JOURNAL.md` au fil de l'eau. |
| Vidéo < 3 min, sans musique ni marque tierce | Script minuté 0:00 → 3:00 (H.16), voix off en anglais, aucun logo tiers à l'écran (relevés et bénéficiaires fictifs), aucune piste audio. |
| URL d'app qui marche, gratuite, sans compte, tenue jusqu'au 29/01/2027 | Trois sites statiques GitHub Pages, aucun service, aucun compte, zéro requête réseau après chargement (LED-N-05). |
| Dépôt public, licence open source | MIT dès le premier commit, aucune dépendance à copyleft fort, tableau des licences dans le README, garde CI qui vérifie licence et présence de `/.kiro`. |

### H.3 Problème, public et pourquoi maintenant

Le besoin est banal et très mal servi : **tenir un livre**. Pas explorer un fichier, pas regarder un graphique —
*tenir* quelque chose dont on peut dire plus tard « c'est exact, et voici pourquoi ». Deux populations en ont besoin
et n'ont rien : les foyers qui veulent un chiffre, et les petites structures qui doivent rendre des comptes sans
comptable.

**Sarah, 38 ans, deux enfants (7 et 11 ans), compte joint.** Situation datée : jeudi 26 novembre 2026, 22 h 40. Elle
ouvre son application bancaire sur le téléphone de la cuisine. Le relevé affiche `PRLV SEPA EDF ENERGIE`, `CARREFOUR
MARKET PARIS 12`, `VIR M DUPONT` — et un solde. Pas un budget. Sa question tient en une phrase : **« est-ce que je
peux encore dépenser demain ? »**. Paramètres de simulation du jeu de démonstration : revenu net du foyer 2 480
€/mois, 3 ans de relevé (12 000 lignes), 9 enveloppes. Aucun outil actuel ne lui donne ce chiffre sans abonnement,
sans compte, et sans que son relevé quitte sa machine. Statistiques de marché (part des ménages qui budgètent, coût
moyen d'un abonnement) : **À vérifier** — rien n'est affirmé sans source dans la soumission.

**Le collectif « Les Voisins Solidaires », 6 bénévoles, 40 000 € de dons par an.** Situation datée : assemblée
générale du 14 mars 2027. 180 donateurs récurrents, une soixantaine d'aides versées (bons alimentaires, cantine, une
caution). Aucune compétence comptable dans le collectif ; la trésorière tient un tableur partagé et fabrique un PDF à
la main. Un donateur pose la seule question qui compte : **« où est passé l'argent ? »** La réponse actuelle est un
document non vérifiable. Le collectif ne peut ni payer un expert-comptable, ni héberger un serveur, ni demander à ses
bénévoles d'apprendre la comptabilité en texte.

**Le développeur (et l'agent) qui part du squelette.** Il ne veut ni base de données ni serveur, et ne veut pas
réapprendre la comptabilité. Il veut un contrat lisible en une heure, cinq points d'extension, et la garantie que le
noyau ne peut pas produire une écriture déséquilibrée. Depuis que des agents écrivent du code, « un gabarit lisible »
est devenu mesurable : si Kiro en tire une troisième application en moins de quinze minutes, la clarté est prouvée,
pas affirmée (H.13).

**Pourquoi maintenant.** (1) Le navigateur sait tout faire : `WebCrypto` (SHA-256, AES-GCM), IndexedDB, service
workers — un grand livre embarqué n'exige plus de serveur. (2) La demande de preuve traverse le champ associatif :
fonds d'entraide, banques du temps, inventaires partagés. (3) Les outils de finances personnelles ont glissé vers «
compte + synchronisation bancaire tierce », exactement ce que ce public refuse.

| Outil | Ce qu'il fait bien (vérifié sur son site le 11/11/2026) | Ce qui manque pour notre public |
|---|---|---|
| Beancount | Partie double depuis fichiers texte, rigoureux, écosystème riche | Fichiers texte, aucune interface, aucun partage public |
| hledger | Texte brut robuste et rapide, `hledger check --strict`, gère argent, titres et **temps**, `hledger web` en lecture seule | Binaire à installer, pas d'enveloppes avec report, pas de page publique anonymisée |
| ledger-cli | Le format historique, minimal | Encore plus technique, aucune interface |
| Actual Budget | Open source, rapide, local-first, enveloppes, chiffrement de bout en bout optionnel, imports QIF/OFX/QFX/CAMT.053/CSV | Application à installer ou serveur de synchronisation à héberger ; synchro bancaire via des tiers (GoCardless, SimpleFIN) ; pas de squelette à dériver, pas de chaîne de hash |
| GnuCash | Bureautique, complet, éprouvé | Lourd, poste de travail, pas de partage, pas de modèle à dériver |
| Firefly III | Partie double, multi-devises, moteur de règles, budgets, API JSON REST | Serveur PHP auto-hébergé à maintenir ; aucune page publique vérifiable |

**La différence, en une phrase** : personne ne propose un squelette comptable maigre, hors ligne, dans le navigateur,
dont les deux applications se situent aux deux extrémités du spectre de la vie privée — l'une cache tout, l'autre
publie tout — avec une chaîne de hash vérifiable.

**La différence avec `bare-bones`, noir sur blanc.** `bare-bones` est un explorateur : il lit un fichier, déduit des
types, filtre, agrège, dessine, partage un état de vue — et n'a pas de mémoire. Partie double est un livre : il écrit,
refuse une écriture déséquilibrée, rend toute correction visible comme une paire d'écritures, enchaîne ses entrées par
hash, reporte les reliquats d'un mois sur l'autre, produit une piste d'audit. Aucun paquet commun, aucun import
croisé, aucune ligne recopiée. Là où `bare-bones` prouve la polyvalence par *trois fichiers différents*, Partie double
la prouve par *deux modèles de confiance opposés sur le même noyau algébrique*.

### H.4 Objectifs, non-objectifs, indicateurs

**Objectifs.** O1 — un noyau dont la justesse est démontrée par la machine : 15 propriétés fast-check, dont « toute
écriture somme à zéro » et « la chaîne de hash se vérifie après toute insertion et toute contre-passation ». O2 — un
squelette lisible en une heure : ≤ 4 200 lignes hors tests (`core` 2 200, `ui` 1 800, `skeleton` 200). O3 — une
nouvelle application de grand livre en < 15 min avec Kiro et le power fourni, chronométrée par une personne qui ne
connaît pas le dépôt. O4 — deux applications réelles aux antipodes de la vie privée, ≤ 700 lignes propres chacune. O5
— zéro requête réseau par défaut, et un chiffre unique en haut de l'écran pour Sarah. O6 — une page publique qui
répond à « où est passé l'argent ? » en < 150 ko, vérifiable par un donateur sans outil ni compte.

**Non-objectifs.** Pas de synchronisation bancaire (aucun agrégateur, aucun PSD2) : import de fichiers seulement. Pas
de comptes utilisateurs, de droits, de multi-utilisateur, de serveur. Pas de TVA, de liasse fiscale, de plan comptable
réglementaire complet, de consolidation — c'est un livre, pas un logiciel d'expertise comptable. Pas de rapprochement
bancaire automatique. Pas de devise hors ISO 4217 ni de taux de change automatique (les conversions sont des écritures
explicites). Pas de modèle de langage dans le noyau : aucune fonctionnalité n'en dépend, les règles sont
déterministes. Pas d'application mobile native.

**Indicateurs — tous produits par l'outil lui-même, affichés dans la page `#/bench`**

| Indicateur | Cible | Où la mesure est produite |
|---|---|---|
| Import de 3 ans de relevé (12 000 lignes) | < 1 s | `scripts/bench.mjs` + chronomètre affiché à l'écran |
| Écritures déséquilibrées sur 10 000 journaux aléatoires | 0 | `pnpm test:property` (compteur fast-check imprimé) |
| Page publique `mutual-aid` | < 150 ko gzip | `scripts/bundle-budget.mjs`, sortie CI |
| Lignes du squelette | `core` ≤ 2 200 · `ui` ≤ 1 800 · `skeleton` ≤ 200 | hook `loc-budget` + CI |
| Lignes propres par application | ≤ 700 chacune | hook `loc-budget` + CI |
| Vérification de la chaîne sur 12 000 entrées | < 150 ms | `scripts/bench.mjs` |
| Balance générale sur 10 000 entrées | < 50 ms | `scripts/bench.mjs` |
| Requêtes réseau après chargement | 0 | test Playwright qui intercepte tout trafic |
| Nouvelle application tirée du squelette | < 15 min chronométrées | `docs/UNKNOWN-ROOM.md` (H.13) |
| Temps jusqu'au chiffre unique (Sarah) | < 2 s après import | mesure Playwright `performance.now()` |
| Défauts trouvés par les tests par propriétés | ≥ 3 contre-exemples consignés | section dédiée du `KIRO_JOURNAL.md` |

### H.5 Le concept en profondeur

#### H.5.1 Le vocabulaire, en une page

Un **compte** (`Account`) est une case du plan comptable : un type (actif, passif, capitaux propres, produit, charge),
une unité (devise ISO 4217 ou quantité : heures, kilos) et un **solde normal**. Une **écriture** (`Posting`) est un
montant signé qui tombe dans une case. Une **entrée** (`Entry`) est un paquet d'écritures qui **somme à zéro** : c'est
la loi de la partie double et la seule loi du noyau. Le **journal** (`Journal`) est la liste en ajout seul des
entrées, chacune portant le hash de la précédente. Un **solde** n'est jamais stocké : c'est un pli sur le journal.

Solde normal par type (convention débit positif) : `asset` et `expense` → **débit**, solde typiquement
positif (ce que l'on possède, ce que l'on a consommé) ; `liability`, `equity` et `income` → **crédit**,
solde typiquement négatif (ce que l'on doit, ce qui appartient aux propriétaires, ce que l'on a reçu).

L'équation que la machine vérifie à chaque entrée : pour toute devise, `Σ actifs + Σ charges = Σ passifs + Σ capitaux
+ Σ produits` (en soldes normaux), soit `Σ débits = Σ crédits`, soit encore, en convention signée brute, `Σ de tous
les soldes = 0`. Exemple du jeu de démonstration (centimes) :

```
Entry 01JB3QK7X9M2P4R6T8V0W1Y3Z5  date 2026-11-03  kind transaction  unit EUR
note  "Groceries — Carrefour Market, rue de Charenton"
  expenses:food:groceries  +8420      assets:bank:joint  -8420      somme 0 ✓ accepté
```

#### H.5.2 La règle d'or : on ne modifie jamais, on contre-passe

Le noyau **n'expose aucune fonction qui modifie une entrée**. Toute correction passe par `contra(entryId, reason)`,
qui ajoute une entrée miroir (`kind: "reversal"`, `reverses: <id>`, montants strictement opposés, note en langage
clair obligatoire). Le relevé du 4 novembre corrige le montant à 48,20 € :

```
1  01JB3QK7…Z5  2026-11-03  transaction  groceries +8420 / joint −8420
2  01JB3QM0…A2  2026-11-04  reversal, reverses 01JB3QK7…Z5
                            note "Reversal: wrong amount, bank restated 48.20"
                            groceries −8420 / joint +8420
3  01JB3QM1…B7  2026-11-04  transaction  groceries +4820 / joint −4820
```

Solde de `expenses:food:groceries` : **48,20 €**, exactement la vérité ; et la piste d'audit montre la correction
comme une paire visible. Aucune ligne supprimée, aucune éditée. C'est ce que protège le hook `immutable-journal-guard`
(H.13) et ce que prouve `LED-P-05`.

#### H.5.3 La chaîne de hash : ce qu'elle prouve, et ce qu'elle ne prouve pas

```
canonical(entry) = "ledger:v1\n" + entry.prevHash + "\n"
                 + canonicalJson({ id, date, kind, note, unit, tags, reverses, postings })
canonicalJson    = clés triées, aucun espace, montants en entiers, dates "YYYY-MM-DD", JSON strict
hash(entry)      = hex(sha256(canonical(entry)))        genesis = "0".repeat(64)
```

L'ordre des `postings` **compte** dans le hash (il fait partie de l'entrée telle qu'écrite) alors qu'il ne compte pas
dans les soldes. Asymétrie volontaire et documentée : elle prouve l'intégrité de la saisie sans rendre les soldes
dépendants de l'ordre. Ce que la chaîne prouve : rien n'a été **édité**, **retiré** ni **réordonné** depuis que la
tête a été publiée. Ce qu'elle ne prouve **pas**, écrit noir sur blanc dans la page publique : (1) que les écritures
sont sincères — la chaîne prouve la cohérence, pas la vérité ; (2) que le journal n'a pas été **tronqué par la fin** —
qui possède le fichier peut couper la queue et republier une tête plus courte. Parade : la tête est ancrée dans le
rapport annuel imprimable et dans un commit du dépôt ; le donateur compare. Cette section « what this chain proves /
does not prove » fait partie du produit : l'honnêteté sur la limite est un argument, pas une faiblesse.

Implémentation : SHA-256 en TypeScript pur (`packages/core/src/hash.ts`, ~90 lignes), **synchrone**. WebCrypto est
écarté du noyau : `crypto.subtle` est asynchrone et empoisonnerait `append`, `verify`, les plis et toutes les
propriétés. Un test unitaire confronte l'implémentation à `crypto.subtle.digest` pour garantir la conformité.

#### H.5.4 Les soldes sont un pli, pas un état

```
balances(journal, asOf, unit) = journal.records
  .filter(r => r.date <= asOf && r.unit === unit)
  .flatMap(r => r.postings)
  .reduce((acc, p) => acc.set(p.accountId, (acc.get(p.accountId) ?? 0) + p.amountMinor), new Map())
```

Trois conséquences exploitées partout : (1) **indépendance de l'ordre** — l'addition est commutative et associative,
donc permuter les entrées ne change aucun solde (`LED-P-03`) ; (2) **rejeu** — un instantané sérialisé puis rejoué
redonne les mêmes soldes bit à bit (`LED-P-06`) ; (3) **aucun cache à invalider** — le seul état est le journal, donc
la classe de bug « solde désynchronisé » n'existe pas. Coût : un parcours linéaire, borné par les cibles de H.4 (10
000 entrées < 50 ms) et par un index optionnel toujours recomputable, jamais persisté.

#### H.5.5 Enveloppes et report conservatif

Une enveloppe n'est pas une écriture : c'est une **projection** sur un compte de charges pour une période. Elle ne
touche donc jamais l'invariant de somme nulle.

```
spent(env, p)      = −Σ postings du compte de l'enveloppe (et de ses enfants) datés dans p
carriedIn(env, p₀) = 0
carriedIn(env, p)  = clampReport(available(env, p−1), env.rollover, env.capMinor)
                     none → 0 · carry → max(0, ·) · carry-deficit → · (le déficit suit)
available(env, p)  = env.budgetMinor + carriedIn(env, p) − spent(env, p)
```

Invariant de conservation, testé sur 24 mois simulés (`LED-P-08`) : `Σ_p budget_p + report_initial = Σ_p spent_p +
report_final + Σ_p abandoned_p`, où `abandoned_p` est **explicitement** ce que la politique de report abandonne (mode
`none`, ou plafonnement `capMinor`). Rien n'apparaît ; tout ce qui disparaît est compté comme abandon de politique,
jamais comme bug. C'est cette formulation qui rend le report testable au lieu d'être « probablement juste ».

#### H.5.6 Le chiffre unique de Sarah

Une seule valeur en haut de l'écran, en gros, et rien d'autre au premier regard :

```
daysLeft  = jours restants du mois courant, aujourd'hui inclus
available = Σ available(env, ceMois) pour les enveloppes dont le compte a daily: true
committed = Σ montants des règles récurrentes (weekly/monthly) dont l'échéance tombe entre
            aujourd'hui et la fin du mois et qui ne sont pas encore dans le journal
reserve   = Σ montants des enveloppes daily: false explicitement réservées (Santé, Imprévus)
leftToday = floor((available − committed − reserve) / daysLeft)   // euros, arrondi inférieur
```

L'arrondi inférieur n'est pas un détail : il garantit que dépenser exactement `leftToday` chaque jour restant ne met
jamais le mois en déficit (`LED-P-13`, résidu final dans `[0, daysLeft)` centimes). Sous ce chiffre, et seulement sous
lui, la projection de fin de mois est rendue **en fourchette** (médiane et écart des trois derniers mois par
enveloppe), jamais comme un nombre unique : un budget n'est pas une prédiction, et l'afficher comme telle serait
malhonnête.

#### H.5.7 Les cinq points d'extension

| Point | Ce qu'on y branche | Signature | `envelopes` | `mutual-aid` |
|---|---|---|---|---|
| `defineChart` | Plan comptable : comptes, types, unités | `(accounts: AccountInput[]) => Chart` | 24 comptes, EUR | 18 comptes, EUR |
| `defineRules` | Affectation automatique et récurrente | `(rules: RuleInput[]) => RuleSet` | 31 règles dont 12 apprises | 4 règles (dons, aides, frais) |
| `defineEnvelopes` | Budgets par période avec report | `(envs: EnvelopeInput[]) => EnvelopeSet` | 9 enveloppes, report `carry` | 0 — le fonds ne budgète pas, il rend compte |
| `defineReports` | Rapports publiés | `(defs: ReportDef[]) => ReportSet` | 3 (enveloppes, balance, audit) | 4 (+ résultat, rapport annuel) |
| `definePresentation` | Thème, langue, libellés, colonnes | `(p: PresentationInput) => Presentation` | `warm-paper`, fr | `ink-paper`, en, mise en page d'impression |

Tout le reste (journal, hash, plis, contre-passation, validation Zod, rapports de base, anonymisation) est dans le
noyau et **identique** pour les deux applications. C'est la preuve de polyvalence : pas deux variantes d'un même cas,
mais deux modèles de confiance opposés sur un noyau commun.

#### H.5.8 Ce qui n'est pas dans le squelette, et pourquoi

Pas d'authentification, de synchronisation, de connecteur bancaire, de fiscalité, de multi-utilisateur, de graphs
au-delà d'une sparkline SVG, d'i18n au-delà de en/fr, de LLM. Chaque refus est consigné dans `.kiro/steering/lean.md`
avec sa raison : un squelette qui dit oui à tout cesse d'être clair. Test d'admission dans `core` : *les deux
applications en ont-elles besoin, et l'invariant est-il prouvable ?* Sinon la fonction reste dans l'application.

### H.6 Formats et données

#### H.6.1 Le contrat (TypeScript + Zod, à figer tel quel dans la spec `ledger-contract`)

```ts
// packages/core/src/schema.ts
import { z } from "zod";
/* primitives */
export const UnitCode   = z.string().regex(/^[A-Z]{3}$/);                  // ISO 4217 ou quantité déclarée
export const AccountId  = z.string().regex(/^[a-z][a-z0-9]*(?::[a-z0-9-]+)*$/);
export const EntryId    = z.string().regex(/^[0-9A-HJKMNP-TV-Z]{26}$/);    // ULID, triable
export const Hash       = z.string().regex(/^[0-9a-f]{64}$/);
export const IsoDate    = z.string().regex(/^\d{4}-\d{2}-\d{2}$/);
export const Period     = z.string().regex(/^\d{4}-\d{2}$/);
export const MinorUnits = z.number().int().safe();                        // jamais de flottant
export const AccountType = z.enum(["asset","liability","equity","income","expense"]);
export const NormalSide  = z.enum(["debit","credit"]);
export const Unit = z.union([
  z.object({ kind: z.literal("currency"), code: z.string().regex(/^[A-Z]{3}$/) }),
  z.object({ kind: z.literal("quantity"), label: z.string().min(1).max(24) }),  // "hour", "kg"
]);
/* Account */
export const Account = z.object({
  id: AccountId, type: AccountType, normalBalance: NormalSide, unit: Unit,
  label: z.string().min(1).max(120), parent: AccountId.nullable().default(null),
  archived: z.boolean().default(false), daily: z.boolean().default(false),  // compte dans leftToday ?
}).strict();
/* Posting — immuable */
export const PartyRef = z.object({
  id: z.string().min(1),                 // interne, jamais publié
  label: z.string().max(120),            // "Mme K." — privé
  publicLabel: z.string().max(120),      // "a household, case 41" — publié
  disclosed: z.boolean().default(false), // la partie accepte d'être nommée
}).strict();
export const Posting = z.object({
  id: z.string().min(1), accountId: AccountId, amountMinor: MinorUnits,     // signé : débit > 0
  unit: UnitCode, memo: z.string().max(200).optional(), party: PartyRef.optional(),
  evidence: z.array(z.string()).readonly().optional(),                      // empreintes de lignes CSV
}).strict();
/* Entry — somme à zéro, datée, note en langage clair obligatoire */
export const EntryKind = z.enum(["transaction","opening","reversal","conversion"]);
export const Entry = z.object({
  id: EntryId, date: IsoDate, note: z.string().min(1).max(200), unit: UnitCode,
  kind: EntryKind.default("transaction"), postings: z.array(Posting).min(2).readonly(),
  reverses: EntryId.nullable().default(null), tags: z.array(z.string()).readonly().default([]),
}).strict();
/* Journal — ajout seul, chaîne vérifiable */
export const JournalRecord = Entry.extend({ seq: z.number().int().nonnegative(), prevHash: Hash, hash: Hash });
export const Journal = z.object({ version: z.literal(1), createdAt: IsoDate,
  records: z.array(JournalRecord).readonly() }).strict();
/* Rule — affectation automatique ou récurrente */
export const Rule = z.object({
  id: z.string().min(1),
  when: z.object({ field: z.enum(["memo","party","reference"]).default("memo"),
    op: z.enum(["contains","equals","startsWith","regex"]), value: z.string().max(200),
    amountBetween: z.tuple([MinorUnits, MinorUnits]).optional() }).strict(),
  then: z.object({ accountId: AccountId, envelopeId: z.string().optional(), note: z.string().max(200).optional(),
    split: z.array(z.object({ accountId: AccountId, weight: z.number().int().min(1) })).optional() }).strict(),
  frequency: z.enum(["on-import","weekly","monthly","once"]).default("on-import"),
  origin: z.enum(["authored","learned"]), uses: z.number().int().nonnegative().default(0),
  confidence: z.number().min(0).max(1).optional(),
}).strict();
/* Envelope — budget sur un compte pour une période, avec report */
export const Envelope = z.object({
  id: z.string().min(1), label: z.string().min(1).max(80), accountId: AccountId, period: Period,
  budgetMinor: MinorUnits.nonnegative(), rollover: z.enum(["none","carry","carry-deficit"]).default("carry"),
  capMinor: MinorUnits.nonnegative().nullable().default(null), unit: UnitCode,
}).strict();
/* Report — union discriminée, sortie pure du noyau */
const Row = z.object({ accountId: AccountId, label: z.string(), debit: MinorUnits, credit: MinorUnits, balance: MinorUnits }).strict();
const EnvRow = z.object({ envelopeId: z.string(), label: z.string(), budgetMinor: MinorUnits, spentMinor: MinorUnits,
  carriedMinor: MinorUnits, availableMinor: MinorUnits, leftTodayMinor: MinorUnits }).strict();
const AuditRow = z.object({ seq: z.number().int(), date: IsoDate, note: z.string(), kind: EntryKind, hash: Hash, reverses: EntryId.nullable() }).strict();
export const Report = z.discriminatedUnion("kind", [
  z.object({ kind: z.literal("trial-balance"), asOf: IsoDate, unit: UnitCode, rows: z.array(Row),
    totals: z.object({ debit: MinorUnits, credit: MinorUnits }) }).strict(),
  z.object({ kind: z.literal("income-statement"), from: IsoDate, to: IsoDate, unit: UnitCode, rows: z.array(Row), netMinor: MinorUnits }).strict(),
  z.object({ kind: z.literal("envelopes"), period: Period, unit: UnitCode, totalLeftTodayMinor: MinorUnits, rows: z.array(EnvRow) }).strict(),
  z.object({ kind: z.literal("audit-trail"), from: IsoDate, to: IsoDate, headHash: Hash, rows: z.array(AuditRow) }).strict(),
]);
/* View — lecture seule, sérialisable, jamais de réseau */
export const RedactionPolicy = z.object({
  parties: z.enum(["named","pseudonymised","aggregate"]), dates: z.enum(["exact","month"]),
  amounts: z.enum(["exact","bucket10"]), memo: z.enum(["as-is","whitelist"]),
  minGroupSize: z.number().int().min(1).default(3),   // seuil d'agrégation (k-anonymat)
}).strict();
export const View = z.object({
  v: z.literal(1), app: z.enum(["envelopes","mutual-aid","skeleton"]),
  report: z.enum(["trial-balance","income-statement","envelopes","audit-trail","public-ledger"]),
  params: z.object({ from: IsoDate.optional(), to: IsoDate.optional(), period: Period.optional(),
    accounts: z.array(AccountId).default([]), tags: z.array(z.string()).default([]) }).strict(),
  redaction: RedactionPolicy.optional(),
}).strict();
```

**Invariants vérifiés à la construction**, pas par convention : `Σ amountMinor = 0` par entrée ; `kind: "reversal"`
exige `reverses` non nul et des montants exactement opposés à la cible ; `kind: "conversion"` est la seule à pouvoir
porter deux unités, et exige alors deux groupes internement équilibrés plus un `rate` et une date ; `normalBalance`
doit correspondre au `type` sauf déclaration explicite commentée.

#### H.6.2 Le fichier de configuration déclaratif (un par application)

```ts
// apps/envelopes/ledger.config.ts — la seule chose qu'une application écrit
import { defineLedger, defineChart, defineRules, defineEnvelopes, defineReports, definePresentation } from "@ledger/core";
const EUR = { kind: "currency", code: "EUR" } as const;
export default defineLedger({
  name: "Household envelopes", locale: "fr", unit: EUR,
  chart: defineChart([
    { id: "assets:bank:joint", type: "asset", unit: EUR, label: "Compte joint", daily: true },
    { id: "expenses:food:groceries", type: "expense", unit: EUR, label: "Courses", daily: true },
    /* … 22 autres comptes … */ ]),
  rules: defineRules([
    { id: "r-groceries", when: { field: "memo", op: "contains", value: "CARREFOUR" },
      then: { accountId: "expenses:food:groceries", envelopeId: "env-groceries" }, origin: "authored" },
    { id: "r-rent", when: { field: "memo", op: "contains", value: "PRLV SEPA LOYER" },
      then: { accountId: "expenses:housing:rent" }, frequency: "monthly", origin: "authored" } ]),
  envelopes: defineEnvelopes([
    { id: "env-groceries", label: "Courses", accountId: "expenses:food:groceries", period: "2026-11", budgetMinor: 45000, rollover: "carry" },
    { id: "env-energy", label: "Énergie", accountId: "expenses:housing:energy", period: "2026-11", budgetMinor: 18000, rollover: "carry-deficit" } ]),
  reports: defineReports(["envelopes", "trial-balance", "audit-trail"]),
  presentation: definePresentation({ theme: "warm-paper", columns: ["date","label","amount","envelope"] }),
});
```

Côté `apps/mutual-aid`, le même fichier déclare 18 comptes, 4 règles, **aucune enveloppe**, un rapport de plus
(`income-statement` + `public-ledger`) et une présentation d'impression. La différence entre les deux applications
tient entièrement dans ce fichier et dans leurs écrans.

#### H.6.3 Import CSV : la réalité européenne

```
Date;Libellé;Débit;Crédit;Devise
03/11/2026;"CARREFOUR MARKET PARIS 12";84,20;;EUR
04/11/2026;"PRLV SEPA EDF ENERGIE";112,47;;EUR
05/11/2026;"VIR M DUPONT SALAIRE";;2480,00;EUR
```

Encodage Windows-1252, séparateur `;`, virgule décimale, libellés entre guillemets, dates `jj/mm/aaaa`, deux colonnes
de montant. Variante acceptée : une colonne `Montant` où le débit est négatif. **Hors périmètre** : QIF, OFX,
CAMT.053, rapprochement. En-têtes exacts des banques françaises : **À vérifier** banque par banque au moment d'écrire
les fixtures. Détection, dans cet ordre et **affichée à l'utilisateur avant validation** : (1) encodage — BOM UTF-8,
sinon UTF-8 strict, sinon Windows-1252 ; (2) séparateur — celui qui donne le plus de champs constants sur 20 lignes ;
(3) séparateur décimal — celui qui rend tous les montants analysables ; (4) colonne de date — première colonne
analysable, format deviné par motif ; (5) mapping des colonnes par correspondance floue, puis écran de confirmation.
Deux lignes identiques sont **conservées toutes les deux**, la seconde marquée « doublon possible » : le noyau ne
supprime jamais seul. L'empreinte de la ligne source est gardée dans `Posting.evidence`, ce qui rend l'import
idempotent (`LED-P-14`).

#### H.6.4 Sérialisation

| Artefact | Format | Destination | Taille cible |
|---|---|---|---|
| Journal | JSON `Journal` v1 | fichier `.ledger.json`, IndexedDB | 12 000 entrées ≈ 3,4 Mo **À vérifier** |
| Instantané | JSON + `headHash` + `asOf` | sauvegarde locale | idem |
| Vue | `View` compressé (deflate-raw) en **fragment** d'URL | presse-papier, jamais un serveur | < 2 000 caractères |
| Vue publique | `public/ledger-<period>.json` + page statique | dépôt, servi en statique | < 150 ko gzip |
| Reçu de donateur | `{ entryId, hash, amount, date }` | courriel ou papier | < 300 octets |

Le **fragment** (`#v=…`) et non la requête (`?v=…`) : un fragment n'est jamais envoyé au serveur, n'apparaît ni dans
les journaux d'accès ni dans `Referer`. Toute vue lue depuis une URL est validée par Zod et bornée en taille ; une vue
invalide ouvre la vue par défaut avec un message.

#### H.6.5 Fixtures et sources de données

**Aucune donnée réelle n'est embarquée.** Tous les jeux sont synthétiques, générés par `scripts/gen-fixtures.mjs` avec
une graine fixe (`LEDGER_FIXTURE_SEED=20261103`), reproductibles bit à bit : `fixtures/household-3y.csv` (12 000
lignes, 36 mois), `fixtures/mutual-aid-2026.csv` (214 écritures, 180 dons, 62 aides), `fixtures/messy-csv/*.csv` (6
fichiers tordus : BOM absent, `;` et `,` mélangés, libellé avec retour à la ligne, montant entre guillemets, colonnes
inversées, Windows-1252 accentué).

| Source de référence | Usage | Licence |
|---|---|---|
| ISO 4217 | 12 codes devise écrits à la main dans `core/src/units.ts` | Usage comme référence ; republication de la liste complète **À vérifier** |
| ISO 20022 / camt.053 | Lecture de la spécification pour comprendre les exports bancaires ; aucun fichier copié | Spécification consultée, non redistribuée |
| Plan comptable général (ANC) | Inspiration de la nomenclature du plan par défaut ; aucun numéro officiel reproduit | **À vérifier** si des numéros officiels sont cités |
| Aucun jeu de données public | Volontaire : des données bancaires ou de bénéficiaires réelles sont hors de question | — |

Garde CI `fixture-privacy-guard` : refuse dans `fixtures/**` tout IBAN (`[A-Z]{2}\d{2}[A-Z0-9]{11,30}`), tout numéro
de carte valide au test de Luhn, tout couple prénom+nom d'une liste de contrôle interne, et exige la première ligne `#
FIXTURE: FICTIONAL DATA`.

### H.7 Exigences fonctionnelles

| Id | P | Exigence (EARS) | Vérification |
|---|---|---|---|
| LED-F-01 | I | QUAND une entrée est soumise, le système DOIT la refuser si ses écritures ne somment pas à zéro par devise, avec l'erreur typée `UnbalancedEntry` nommant le déséquilibre exact. | LED-P-01 |
| LED-F-02 | I | QUAND un compte est déclaré, le système DOIT valider type, solde normal, unité et parent, et DOIT rejeter un identifiant hors du motif `a:b:c`. | unit |
| LED-F-03 | I | TANT QUE le journal existe, le système DOIT n'exposer aucune fonction publique qui modifie une entrée ; toute correction DOIT passer par `contra()`. | LED-P-05 |
| LED-F-04 | I | QUAND l'utilisateur contre-passe une entrée, le système DOIT ajouter une entrée `reversal` liée par `reverses`, aux montants strictement opposés, avec note obligatoire. | LED-P-10 |
| LED-F-05 | I | QUAND une entrée est ajoutée, le système DOIT calculer `hash` sur la forme canonique avec `prevHash` et DOIT incrémenter `seq`. | LED-P-04 |
| LED-F-06 | I | QUAND `verifyChain()` est demandé, le système DOIT répondre `ok` ou le premier index fautif avec sa raison (`broken-link`, `bad-hash`, `bad-seq`). | LED-P-04 |
| LED-F-07 | I | Le système DOIT calculer tout solde et tout rapport comme un pli sur le journal, sans état dérivé persistant. | LED-P-03, LED-P-06 |
| LED-F-08 | I | QUAND une entrée mélange deux unités sans `kind: "conversion"` explicite, le système DOIT la refuser (`MixedUnits`). | LED-P-07 |
| LED-F-09 | I | QUAND un relevé CSV est déposé, le système DOIT détecter encodage, séparateur, séparateur décimal et colonne de date, et DOIT afficher sa détection avant tout import. | `fixtures/messy-csv` |
| LED-F-10 | I | SI une ligne importée produirait une écriture déséquilibrée, ALORS le système DOIT la refuser et la placer dans un rapport de rejets exportable. | E2E |
| LED-F-11 | I | QUAND le même relevé est importé deux fois, le système DOIT ignorer les lignes déjà présentes (empreinte `evidence`) et le signaler. | LED-P-14 |
| LED-F-12 | S | QUAND une règle correspond à une opération importée, le système DOIT proposer l'affectation sans l'appliquer, sauf mode `auto` activé explicitement. | unit |
| LED-F-13 | S | QUAND l'utilisateur corrige une affectation proposée, le système DOIT enregistrer une règle `learned` (motif → compte) avec son compteur d'usages. | E2E |
| LED-F-14 | S | QUAND une règle à `split` est appliquée, le système DOIT répartir le montant sans perte ni création (le reliquat d'arrondi va à la première jambe). | LED-P-12 |
| LED-F-15 | S | Le système DOIT calculer `available = budget + carriedIn − spent` par enveloppe et reporter le reliquat selon `rollover` et `capMinor`. | LED-P-08 |
| LED-F-16 | I | QUAND l'utilisateur ouvre `envelopes`, le système DOIT afficher le chiffre unique `leftToday` avant toute autre donnée. | E2E, LED-P-13 |
| LED-F-17 | S | Le système DOIT rendre la projection de fin de mois en fourchette (médiane et écart des trois derniers mois), jamais en valeur unique. | unit |
| LED-F-18 | I | Le système DOIT produire les quatre rapports comme fonctions pures du journal et de la configuration, sans effet de bord. | LED-P-02 |
| LED-F-19 | I | QUAND une vue est sérialisée dans l'URL, le système DOIT n'écrire que dans le fragment, validé par Zod et borné à 2 000 caractères. | LED-P-15 |
| LED-F-20 | I | QUAND une écriture est préparée pour publication, le système DOIT appliquer la `RedactionPolicy` et afficher côte à côte version privée et version publique avant validation. | LED-P-09 |
| LED-F-21 | I | Le système DOIT générer une page publique autonome, sans requête réseau, dont la chaîne de hash est recalculée sur les entrées **rédigées**. | LED-P-09 |
| LED-F-22 | S | QUAND un donateur saisit son reçu (`entryId` + `hash`), le système DOIT confirmer ou infirmer sa présence dans la chaîne, hors ligne. | E2E |
| LED-F-23 | S | Le système DOIT produire un rapport annuel imprimable : A4, paginé, lisible sans couleur, totaux en toutes lettres. | E2E |
| LED-F-24 | O | OÙ le chiffrement au repos est activé, le système DOIT chiffrer IndexedDB en AES-GCM avec clé dérivée par PBKDF2 (600 000 itérations, **À vérifier**) d'une phrase jamais stockée. | unit |
| LED-F-25 | O | Le système DOIT exposer `#/bench` affichant en direct toutes les mesures de H.4. | E2E |
| LED-F-26 | X | Multi-utilisateur, authentification, synchronisation bancaire, TVA, rapprochement automatique : exclus. | — |

### H.8 Exigences non fonctionnelles

| Id | Domaine | Exigence |
|---|---|---|
| LED-N-01 | Légèreté | Budgets de H.4 vérifiés par le hook `loc-budget` et la CI ; < 500 lignes par fichier, < 50 lignes par fonction ; un concept par fichier. |
| LED-N-02 | Poids | Page publique < 150 ko gzip ; chaque application < 220 ko au démarrage ; polices système uniquement, aucune police web. |
| LED-N-03 | Performance | Import 12 000 lignes < 1 s hors fil principal ; `verifyChain()` sur 12 000 entrées < 150 ms ; balance sur 10 000 entrées < 50 ms. |
| LED-N-04 | Déterminisme | Aucun `Date.now()` ni `Math.random()` dans `core` : horloge et fabrique d'identifiants injectées ; tests reproductibles par graine. |
| LED-N-05 | Réseau | Zéro requête réseau par défaut : CSP `connect-src 'none'`, grep CI sur `fetch\|XMLHttpRequest\|WebSocket\|sendBeacon` dans `packages/core` et `apps/**`, test Playwright qui échoue dès la première requête. |
| LED-N-06 | Sécurité | Aucune évaluation de code venant des données ; libellés rendus en texte ; expressions régulières bornées en longueur et exécutées avec délai (anti-ReDoS) ; export CSV neutralisé contre l'injection de formules. |
| LED-N-07 | Accessibilité | Niveau AA ; navigation clavier complète ; chiffres en `font-variant-numeric: tabular-nums` ; l'information n'est jamais portée par la seule couleur ; `prefers-reduced-motion` respecté ; aucun son. |
| LED-N-08 | Langues | en et fr livrés ; ajout d'une langue = un fichier ; identifiants de code en anglais. |
| LED-N-09 | Hors ligne | Service worker : utilisable après le premier chargement ; export/import `.ledger.json` comme seule sauvegarde requise. |
| LED-N-10 | Robustesse | Toute donnée entrante (fichier, URL, IndexedDB) est validée par Zod et produit une erreur typée, jamais une exception non gérée. |
| LED-N-11 | Dépendances | Runtime limité à `zod` (MIT) et React ; aucun copyleft fort ; lockfile committé ; licences vérifiées en CI. |
| LED-N-12 | Confidentialité des fixtures | Garde `fixture-privacy-guard` en CI ; aucune donnée réelle ; graine fixe. |
| LED-N-13 | Tests par propriétés | 10 000 journaux aléatoires en < 60 s (P95 < 20 s) pour rester dans le budget CI de 5 minutes. |

### H.9 Architecture technique

```
/
├── .kiro/         steering/ (product · tech · structure · testing · accounting[fileMatch] · lean · apps)
│                  specs/ (ledger-contract · ledger-journal · ledger-reports · ledger-envelopes ·
│                          ledger-csv-import · ledger-ui · app-envelopes · app-mutual-aid)
│                  hooks/ (loc-budget · immutable-journal-guard · property-guard ·
│                          fixture-privacy-guard · bundle-budget) · agents/ (ledger-reviewer ·
│                          property-tester) · skills/new-ledger-app/SKILL.md · settings/mcp.json
├── packages/core/   ≤ 2 200 lignes — le noyau, aucune dépendance à React
├── packages/ui/     ≤ 1 800 lignes — composants, aucun accès direct à IndexedDB
├── skeleton/        ≤ 200 lignes — une application vide qui fonctionne
├── apps/envelopes/  ≤ 700 lignes propres · apps/mutual-aid/ ≤ 700 lignes propres
├── power/new-ledger-app/ · fixtures/ · scripts/ · docs/
└── KIRO_JOURNAL.md · README.md · LICENSE (MIT)
```

| Paquet | Fichiers (lignes cibles) | Total |
|---|---|---|
| `packages/core` | `schema.ts` 200 · `hash.ts` 90 · `journal.ts` 260 · `contra.ts` 90 · `ledger.ts` 140 · `reports.ts` 330 · `envelopes.ts` 250 · `rules.ts` 240 · `csv.ts` 320 · `units.ts` 80 · `view.ts` 120 · `index.ts` 80 | 2 200 |
| `packages/ui` | `Shell` 180 · `NumberBand` 140 · `JournalTable` 220 · `EntryForm` 240 · `ImportWizard` 260 · `EnvelopeBoard` 200 · `ReportViews` 200 · `AuditTrace` 120 · `PrintReport` 100 · `a11y` 140 | 1 800 |
| `skeleton` | `main.tsx` 80 · `ledger.config.ts` 60 · `spec-samples/` 60 | 200 |
| `apps/envelopes` | `ledger.config.ts` 70 · `screens/` 280 · `domain/` 230 · `data/` 120 | 700 |
| `apps/mutual-aid` | `ledger.config.ts` 60 · `screens/` 300 · `domain/` 220 · `publish/` 120 | 700 |

**Flux de données**

```
CSV (fictif) ──▶ csv.ts (détection + validation Zod) ──▶ Entry[] proposées
                     │                                        │
                rules.ts (affectation, apprises)         rejets exportables
                     ▼                                        ▼
              journal.ts  ── append-only ──▶ hash.ts (chaîne) ──▶ verifyChain()
                     │                              │
        ┌────────────┼──────────────┐               └──▶ contra.ts (corrections)
        ▼            ▼              ▼
   ledger.ts    envelopes.ts    reports.ts  ──▶  view.ts (fragment d'URL)
   (pli/soldes) (report, leftToday) (4 rapports)        │
                                              apps/mutual-aid ──▶ redaction ──▶ page publique
```

**Ce qui tourne où.** 100 % dans le navigateur : parsing, hash, plis, rapports, rendu, stockage (IndexedDB
chiffrable). Hébergement = GitHub Pages statique pour les trois sites ; aucun worker serverless, aucun service tiers,
aucune base. Les scripts `bench`, `recette`, `loc-budget` et la garde de confidentialité tournent en Node dans la CI,
jamais dans l'application.

**Preuve de polyvalence — les deux applications aux antipodes**

| | `apps/envelopes` | `apps/mutual-aid` |
|---|---|---|
| Forme des données | Journal privé dense : 12 000 lignes importées d'un relevé bancaire, 9 enveloppes | Grand livre public clairsemé : 214 écritures saisies à la main, notes en langage clair obligatoires |
| Logique métier | Affectation par règles apprises, report d'enveloppe, `leftToday`, projection en fourchette | Rédaction/anonymisation avant publication, chaîne publique, rapport annuel imprimable |
| Modèle de confiance | **Tout privé** : la confiance vient du silence (zéro réseau, données chiffrables au repos) | **Tout public** : la confiance vient de la preuve (chaîne de hash vérifiable par un donateur) |
| Rapports | `envelopes`, `trial-balance`, `audit-trail` | `trial-balance`, `income-statement`, `audit-trail`, `public-ledger` |
| Mode de partage | Aucun par défaut ; vue locale en fragment d'URL, export `.ledger.json` chiffrable | Page publique statique + reçu `{entryId, hash}` remis à chaque donateur |
| Public | Sarah, un foyer de 4 personnes | Un collectif de 6 bénévoles, 180 donateurs, une AG |
| Lignes propres | ≤ 700 (cible 640) sur ~4 200 lignes de squelette réutilisées | ≤ 700 (cible 680) sur le même squelette |
| Unité de compte | EUR uniquement | EUR, et `unit: quantity("hour")` activable pour une banque du temps |

À publier dans le README : pour chaque application, le nombre de lignes propres et le nombre de lignes du squelette
qu'elle réutilise — la fraction réutilisée est l'argument de la catégorie.

### H.10 Sécurité et modèle de menace

C'est le point sensible du projet : données bancaires d'un côté, données de bénéficiaires publiées de l'autre. Le
modèle de confiance est donc double, et assumé comme tel.

| Menace | Scénario concret | Parade | Preuve |
|---|---|---|---|
| Fuite par l'URL de partage | Une vue collée dans une messagerie emporte des libellés privés | La vue ne contient que des paramètres (rapport, période, filtres) — jamais d'écritures ; sérialisation en **fragment** (`#v=`), jamais en query : non envoyée au serveur, absente des logs et de `Referer` | LED-P-15, test de longueur ≤ 2 000 caractères |
| Fuite par la vue publique | Un donateur reconnaît un bénéficiaire | `RedactionPolicy` : pseudonymes stables (« a household, case 41 »), dates au mois, montants par palier de 10 €, notes sur liste blanche, seuil d'agrégation `minGroupSize: 3` (k-anonymat) ; prévisualisation privée/publique côte à côte avant publication | LED-P-09, écran de comparaison obligatoire |
| Ré-identification par le hash | Un attaquant devine nom + montant + date, recalcule le hash et confirme sa présence dans la chaîne publique | La chaîne publique est **recalculée sur les entrées rédigées** : le hash privé n'est jamais publié. Le sel de pseudonymisation reste local et n'est jamais exporté | LED-P-09, revue de `redact.ts` |
| Troncature de la chaîne | Couper la queue du journal et republier une tête plus courte | Ancrage de la tête dans le rapport annuel imprimable et dans un commit du dépôt ; encart « what this chain proves / does not prove » sur la page publique | H.5.3, page publique |
| Vol du fichier local | Ordinateur partagé, `.ledger.json` copié | Chiffrement au repos optionnel : AES-GCM, clé dérivée PBKDF2 d'une phrase jamais stockée ; export chiffré par défaut dès qu'une phrase est définie | LED-F-24, test de déchiffrement avec mauvaise clé |
| Exfiltration silencieuse | Une dépendance ou un script tiers envoie le relevé | Zéro requête par défaut : CSP `connect-src 'none'`, grep CI sur `fetch\|XMLHttpRequest\|WebSocket\|sendBeacon`, test Playwright qui échoue dès la première requête sortante | LED-N-05 |
| XSS par libellé bancaire | `"><script>` dans un libellé importé | Rendu React en texte uniquement, aucun `dangerouslySetInnerHTML`, aucune évaluation de configuration venue d'un fichier | LED-N-06, test E2E avec libellé hostile |
| Injection de formule à l'export | Un CSV exporté ouvert dans un tableur exécute `=cmd\|…` | Préfixe `'` sur toute cellule commençant par `=`, `+`, `-`, `@`, tabulation | LED-P-11 |
| ReDoS par règle apprise | Une regex utilisateur catastrophique bloque l'interface | Longueur de motif bornée (200), opérateurs limités à `contains/equals/startsWith`, `regex` exécuté avec délai et repli | LED-N-06 |
| Fixtures indiscrètes | Un vrai relevé commité par erreur | Garde CI `fixture-privacy-guard` (IBAN, Luhn, prénoms+noms) + en-tête obligatoire `# FIXTURE: FICTIONAL DATA` | LED-N-12 |

**Risque résiduel assumé et écrit dans le README** : l'anonymisation réduit le risque de ré-identification, elle ne
l'annule pas. Un montant rare, une date précise et un contexte local peuvent suffire à identifier un ménage. C'est
pourquoi le mode `aggregate` (totaux par catégorie et par mois, sans écriture individuelle) est proposé comme niveau
par défaut recommandé pour les petits fonds, et que le choix est documenté comme un arbitrage entre transparence et
protection.

### H.11 Interface et direction artistique

Le squelette est volontairement nu : typographie système, échelle d'espacement 4/8 px, traits fins, aucun ornement.
Registre visuel : **papier et encre**, chiffres tabulaires, hashes en monospace. Ce projet n'est pas en Costume
Contest : aucun registre fantastique. La règle équivalente — chaque élément visuel doit servir la fonction — est tenue
à l'envers : tout ce qui n'aide pas à lire un solde est supprimé. Seule concession au thème, assumée : la
contre-passation s'affiche en **encre rouge barrée**, comme dans un vrai grand livre, et ce rouge porte une
information fonctionnelle (« cette ligne est annulée ») doublée d'un signe et d'un libellé.

- **Palette** : `--ink #1c1b1a`, `--paper #fdfbf6`, `--rule #e3ded2`, `--red-ink #a4332b`, `--green-ink #2f6b4f` ; contrastes AA ≥ 4,5:1 sur papier, information jamais portée par la seule couleur (signe `−`/`+` et mention textuelle systématiques).
- **Écrans `envelopes`** : `Today` (chiffre unique plein cadre, `aria-live="polite"`, puis fourchette de projection et enveloppes) · `Journal` · `Import` (assistant en 4 étapes, détection affichée) · `Envelopes` (report mois par mois) · `Audit`.
- **Écrans `mutual-aid`** : `Book` (saisie d'une aide en langage clair) · `Publish` (comparaison privée/publique obligatoire avant export) · `Public` (répond à « où est passé l'argent ? », vérification de reçu, encart « what this chain proves ») · `Annual report` (A4).
- **États à soigner** : livre vide · import en cours (progression par lignes) · écriture refusée (déséquilibre exact affiché, jamais un message générique) · chaîne rompue (index + raison) · phrase de passe erronée · vue invalide (retour au défaut + message) · rien à publier.
- **Mouvement, son, démo** : aucune animation par défaut, 120 ms maximum, `prefers-reduced-motion` respecté ; **aucun son**, nulle part, pas même derrière un réglage ; bouton `Load demo data` qui charge les fixtures fictives en moins de 2 s, sans compte ni installation.

### H.12 Propriétés à tester

Toutes en fast-check, graines consignées dans `KIRO_JOURNAL.md` ; jeu par défaut 1 000 exécutions, 10 000 pour la
campagne de soumission (`LED-N-13`).

| Id | Invariant exact | Générateur fast-check |
|---|---|---|
| LED-P-01 | Toute entrée construite par l'API somme à zéro, par devise | `arbBalancedEntry` : `fc.array(arbPosting, {minLength:1,maxLength:5})` + écriture d'équilibrage sur `suspense` ; assertion `sumByUnit === 0` |
| LED-P-02 | La balance générale est toujours équilibrée (`Σ débits = Σ crédits`) | `arbJournal(1..200)` ; `trialBalance(j).totals.debit === .credit` |
| LED-P-03 | Les soldes sont un pli sur le journal, indépendants de l'ordre | `arbJournal` + permutation (`fc.shuffledSubarray` complet) ; égalité stricte des deux maps de soldes |
| LED-P-04 | La chaîne de hash se vérifie après toute insertion et toute contre-passation | `arbJournal` × `fc.array(arbOp)` où `arbOp = append \| contra` ; `verifyChain() === { ok: true }` |
| LED-P-05 | Aucune écriture n'est mutable : une tentative produit une contre-passature, pas un edit | tout objet exposé est `Object.isFrozen` récursivement ; `fc.assert` que `r.postings[0].amountMinor = 1` lève, et que le hash reste identique |
| LED-P-06 | Instantané + rejeu = mêmes soldes et même tête | `serialize → parse → replay` ; égalité bit à bit des soldes et du `headHash` |
| LED-P-07 | Aucune devise mélangée sans écriture de conversion explicite | `arbEntry` à deux unités ; rejet `MixedUnits` sauf `kind: "conversion"` avec `rate` et deux groupes équilibrés |
| LED-P-08 | Le report d'enveloppe est conservatif sur 24 mois simulés | `arbEnvelopePlan(24)` × `arbMonthlySpending` ; `Σ budget + report₀ === Σ spent + reportFinal + Σ abandoned` |
| LED-P-09 | L'anonymisation est irréversible dans la vue publique | entrées privées portant des marqueurs uniques (`PRIV-` + `fc.hexaString`) ; aucun marqueur, aucun `accountId` privé, aucun `party.id` dans le JSON publié |
| LED-P-10 | Une contre-passation annule exactement l'entrée ciblée | `balances(j + contra(e))` === `balances(j sans e)` pour toute entrée terminale |
| LED-P-11 | Aucune cellule exportée ne commence par un caractère de formule non neutralisé | `arbCsvText` hostile (`=`, `+`, `-`, `@`, tabulation) ; export puis relecture |
| LED-P-12 | La répartition (`split`) est conservative | `arbSplit(2..6 jambes)` ; `Σ jambes === montant`, reliquat d'arrondi < nombre de jambes |
| LED-P-13 | `leftToday` ne met jamais le mois en déficit | simulation : dépenser exactement `leftToday` chaque jour restant ; résidu final ∈ `[0, daysLeft)` centimes |
| LED-P-14 | L'import est idempotent | `arbCsv(1..500 lignes)` importé une puis deux fois ; même nombre d'entrées, mêmes hashes |
| LED-P-15 | Toute chaîne passée à l'ouverture d'une vue donne une vue valide ou une erreur typée | `fc.string()` arbitraire en fragment ; jamais d'exception non gérée |

### H.13 Stratégie Kiro

| Surface | Emploi précis | Preuve dans le dépôt |
|---|---|---|
| Specs (8) | `ledger-contract` (exigences d'abord, H.6.1 en entrée) · `ledger-journal` (conception d'abord : chaîne de hash + contre-passation) · `ledger-reports` · `ledger-envelopes` · `ledger-csv-import` · `ledger-ui` · `app-envelopes` · `app-mutual-aid` | `.kiro/specs/<lot>/{requirements,design,tasks}.md`, exigences `LED-*` tracées |
| Steering | `product.md`, `tech.md`, `structure.md`, `testing.md` (toujours) ; **`accounting.md` en `fileMatch` sur `packages/core/**`** : convention de signe, soldes normaux, forme canonique du hash, interdiction absolue de muter une entrée ; `lean.md` (ce qu'on refuse d'ajouter et pourquoi) ; `apps.md` en `fileMatch` sur `apps/**` (interdiction d'import profond, cinq points d'extension) | `.kiro/steering/*.md` + journal : quelle règle du steering a évité quelle erreur |
| Hooks | `loc-budget` (compte les lignes, refuse au-delà du budget) · **`immutable-journal-guard`** (refuse toute fonction qui mute une écriture : `.push`/`.splice`/`.sort` sur `records`, assignation sur `amountMinor`, `Object.assign` sur `Entry`, `delete`) · `property-guard` (relance les propriétés du noyau à l'enregistrement) · `fixture-privacy-guard` · `bundle-budget` | `.kiro/hooks/*.json` (format v1 : `trigger`, `matcher`, `action`) + capture de la sortie d'erreur dans le journal |
| Agents personnalisés | `ledger-reviewer` : lecture seule, confronte un diff aux exigences EARS et au steering `accounting.md`, ne peut pas écrire · `property-tester` : écrit uniquement dans `*.test.ts`, doit produire un contre-exemple reproductible avec sa graine | `.kiro/agents/*.md` + compte rendu de revue commité |
| Power | `new-ledger-app` : manifeste + skill qui copie `skeleton/`, génère `ledger.config.ts` à partir de réponses (nom, unité, comptes, rapports), crée la spec et lance `loc-budget` | `power/new-ledger-app/`, utilisé en direct dans la vidéo |
| MCP (optionnel) | Serveur `ledger-mcp` exposant en lecture seule `verify_chain`, `trial_balance`, `balances_asof` : l'agent vérifie son arithmétique auprès du noyau au lieu de la deviner | `.kiro/settings/mcp.json`, journal d'une session qui s'en sert |
| Crew / CLI | Deux sessions parallèles sur `app-envelopes` et `app-mutual-aid` à partir du même steering ; `kiro` en mode sans interface dans la CI pour rejouer les tâches de spec | Journal : si les deux aboutissent sans toucher au noyau, la clarté est démontrée |

**Comparaison spec / vibe coding** (demandée par le formulaire) : fonction mesurée = `contra()` + recalcul de la
chaîne. Même énoncé, deux sessions — l'une avec la spec `ledger-journal`, l'autre en invite libre ; on compte durée,
allers-retours et défauts trouvés. Chiffres dans `KIRO_JOURNAL.md` §4 (**À mesurer**, rien d'annoncé à l'avance).

**L'épreuve de l'inconnu.** Une personne qui n'a jamais ouvert le dépôt reçoit l'URL du dépôt, le power
`new-ledger-app` et un énoncé d'une page (« un grand livre de banque du temps : heures données et reçues, unité `hour`,
un rapport mensuel, aucune enveloppe »). Chronomètre lancé. Réussite : l'application démarre, accepte deux écritures,
en refuse une déséquilibrée, affiche le rapport — **en moins de 15 minutes, sans modifier `packages/core` ni
`packages/ui`**. Protocole, chrono et vidéo brute dans `docs/UNKNOWN-ROOM.md` ; c'est la troisième application de la
vidéo (`apps/time-bank`) et la preuve la plus directe que le squelette est clair, y compris pour un agent.

**Ce que les tests par propriétés ont trouvé** : section dédiée du `KIRO_JOURNAL.md` (§6), un paragraphe par
contre-exemple, avec la graine fast-check, l'entrée minimale qui casse, le défaut et le correctif. Le formulaire de
soumission pose explicitement la question ; trois classes de défauts sont attendues et seront documentées avec les cas
réels : arrondi d'une répartition `split` non conservative, dépendance du hash à l'ordre des clés d'un objet, report
d'enveloppe qui recrée un reliquat déjà consommé (**À confirmer par l'exécution** — rien n'est inventé avant mesure).

### H.14 Plan de réalisation

| Lot | Contenu | Dépend de | Jours-agent |
|---|---|---|---|
| H1 | Socle dépôt, MIT, CI (ci-budget, conformité concours), squelette vide qui démarre | — | 0,5 |
| H2 | `core` : contrat Zod, unités, `hash.ts`, `journal.ts`, `contra.ts` | H1 | 2 |
| H3 | `core` : `ledger.ts` (plis), `reports.ts` (4 rapports) | H2 | 1,5 |
| H4 | `core` : `envelopes.ts` (report, `leftToday`), `rules.ts` (apprises) | H3 | 1 |
| H5 | `core` : `csv.ts` (détection, validation, rejets, idempotence) | H2 | 1 |
| H6 | `ui` : Shell, NumberBand, JournalTable, EntryForm, ImportWizard, EnvelopeBoard, ReportViews, AuditTrace, PrintReport | H3 | 2 |
| H7 | `apps/envelopes` | H4, H5, H6 | 1 |
| H8 | `apps/mutual-aid` (rédaction, page publique, reçu, rapport annuel) | H3, H6 | 1 |
| H9 | Propriétés (15), hooks, steering, agents, fixtures + garde de confidentialité | H2–H5 | 1 |
| H10 | `skeleton/`, power `new-ledger-app`, épreuve de l'inconnu, README-carte, hébergement | H7, H8 | 1 |
| H11 | Captures, montage vidéo, textes Devpost, blog | H10 | 1,5 |
| | **Périmètre minimal** | | **11** |
| Options | Chiffrement au repos (0,5) · MCP `ledger-mcp` (0,5) · sparkline SVG et thème sombre (0,5) · service worker hors ligne (0,5) · banque du temps en 4e application livrée (0,5) · version fr de la page publique (0,5) | | 3 |

**Calendrier** (aujourd'hui 11/11 ; période de construction ouverte jusqu'au 04/12 14 h Pacifique). H1–H3 du 12 au
16/11 · H4–H6 du 17 au 21/11 (H5 et H6 en parallèle) · H7 et H8 du 22 au 24/11 en parallèle (deux sessions Crew, même
steering) · H9–H10 les 25 et 26/11 · **tout doit être mergé sur `main` le 26/11 à 18 h** · captures et montage les 27
et 28/11 · **gel vidéo le 28/11** · dépôt de la soumission le 30/11, marge de 4 jours avant la clôture.

**Mergé avant le gel vidéo du 28 novembre** (sinon la séquence est coupée du montage) : H1 à H4 (contrat, journal,
chaîne de hash, contre-passation, rapports, enveloppes), H6 (NumberBand et ImportWizard au minimum), H7 et H8 en état
de démonstration, H9 (les 15 propriétés vertes en CI et la sortie imprimable de la campagne à 10 000 journaux), H10
(power + `apps/time-bank` généré une fois à blanc). Restent hors gel : options, blog, et la version française de la
page publique.

### H.15 Risques et parades

| Risque | Prob. | Impact | Parade | Plan B |
|---|---|---|---|---|
| Chevauchement perçu avec `bare-bones` | Moyenne | Forte — les deux sont en Skeleton Crew | Paragraphe dédié en H.1 et H.3, section « Read vs Write » dans les deux README, aucun code partagé | Vidéo qui ouvre sur l'écriture et la contre-passation, jamais sur un import exploratoire |
| Les deux applications se ressemblent | Faible | Forte | Tableau H.9 tenu à jour ; modèles de confiance opposés ; `mutual-aid` n'a aucune enveloppe, `envelopes` n'a aucune publication | Rendre `mutual-aid` strictement non-éditable en ligne (saisie locale puis publication d'un fichier) |
| Le noyau grossit à chaque besoin d'application | Forte | Forte — la promesse « lean » tombe | Hook `loc-budget` bloquant ; tout besoin passe par un point d'extension ou reste dans l'application ; `lean.md` | Reporter la fonctionnalité en option non livrée |
| La partie double effraie le public non développeur | Moyenne | Moyenne | Aucun mot de comptable dans `envelopes` : un chiffre, des enveloppes, des libellés ; le vocabulaire technique n'apparaît que dans `audit` | Mode « simple » qui masque balance et piste d'audit |
| L'anonymisation ne suffit pas à protéger un bénéficiaire | Moyenne | Forte — préjudice réel | Rédaction avant hachage, sel local, seuil `minGroupSize`, mode `aggregate` par défaut recommandé, risque résiduel écrit dans le README | Publication agrégée uniquement (totaux par catégorie et par mois), aucune écriture individuelle |
| Les propriétés ne trouvent rien d'intéressant à raconter | Faible | Moyenne — le formulaire de soumission les demande | 15 propriétés sur les zones à risque (arrondi, report, canonicalisation) ; campagne à 10 000 journaux | Documenter honnêtement « aucun défaut trouvé, voici les graines » : un échec documenté vaut mieux qu'une promesse |
| L'épreuve de l'inconnu dépasse 15 minutes | Moyenne | Moyenne | `skeleton/` + power testés à blanc sur H10 ; README-carte relu par un agent sans contexte | Deux tentatives filmées, la meilleure retenue, l'échec documenté |
| Gel vidéo du 28/11 non tenu | Moyenne | Forte | Liste de ce qui doit être mergé (H.14), options toutes reportables | Vidéo réduite à 2 min sur les deux applications seules |
| Poids de la page publique > 150 ko | Faible | Faible | Hook `bundle-budget` ; aucune police web ; JSON publié paginé par période | Publier le JSON en fichier externe chargé à la demande |

### H.16 Démonstration et soumission

Voix off en anglais (élément de soumission), aucune musique, aucune marque tierce à l'écran : les relevés, noms et
bénéficiaires sont fictifs, les interfaces sont les nôtres.

| Temps | Plan (image) | Voix off, mot pour mot |
|---|---|---|
| 0:00–0:14 | Plein écran : un relevé CSV de 12 000 lignes défile, un compteur monte, s'arrête sur `0.6 s`. Puis un chiffre unique apparaît : `34 €` | "Three years of a bank statement. Twelve thousand lines. Imported in zero point six seconds, offline, and nothing left this laptop. And this is the only number Sarah needs: what she can still spend today." |
| 0:14–0:34 | Coupe sur le dépôt : arborescence, puis `schema.ts` — le type `Entry` et la ligne `Σ = 0` surlignée | "This is Ledger: a double-entry skeleton. Four thousand two hundred lines. One law: every entry sums to zero. Everything else is configuration." |
| 0:34–0:58 | Terminal de l'application : tentative de modifier un montant → refus affiché ; puis `contra()` → deux écritures apparaissent, l'originale barrée en rouge ; `verifyChain()` → `ok` | "You cannot edit an entry. You reverse it. The mistake stays visible, forever, and the hash chain proves nothing was rewritten. Correctness here is not an opinion. It is an equation." |
| 0:58–1:26 | Application `envelopes` : assistant d'import (séparateur `;`, virgule décimale, Windows-1252 détectés et affichés), une correction `CARREFOUR MARKET → Courses`, la règle apprise, le tableau des enveloppes avec report | "Application one: a household budget. It reads a real European bank export — semicolons, decimal commas, Windows-1252. Correct one assignment and it learns the rule. Leftovers roll over. Nothing is uploaded, ever." |
| 1:26–1:58 | Application `mutual-aid` : saisie d'une aide, écran de comparaison privée/publique (« a household, case 41 »), page publique qui s'ouvre sur un téléphone, un donateur saisit son reçu → `verified`, rapport annuel A4 | "Application two: the public book of a mutual-aid fund. Same core, opposite promise. Every donation and every grant is published in plain language, beneficiaries become case numbers, and any donor can verify the chain themselves. One question answered: where did the money go?" |
| 1:58–2:18 | Écran partagé : tableau H.9 (les deux applications aux antipodes) puis sortie de `loc-budget` et d'un hook qui refuse un fichier trop long | "One hides everything. One publishes everything. Same two thousand two hundred lines of core, and a machine that refuses to let it grow." |
| 2:18–2:40 | Sortie de test : `10000 runs, 0 unbalanced entries`, graines affichées ; puis un contre-exemple du journal avec son correctif | "Fifteen properties, ten thousand random journals, zero unbalanced entries. And three real bugs the properties caught that our tests had missed." |
| 2:40–2:56 | Chronomètre à l'écran : une personne qui n'a jamais vu le dépôt, Kiro, le power `new-ledger-app`, une banque du temps en unités d'heures qui démarre — `14 min 32 s` | "The unknown-room test: someone who has never seen this repository, Kiro, and the shipped power. A working time-bank ledger in fourteen minutes thirty-two, without touching the core." |
| 2:56–3:00 | Les trois adresses sur fond papier, aucune décoration | "Ledger. A skeleton you can audit." |

**Textes Devpost** (anglais). Titre : *Ledger — a double-entry skeleton*. Accroche : « A 4 200-line double-entry core
you cannot lie to: entries are immutable, corrections are visible pairs, balances are a fold, and every claim is a
tested property. Two apps inherit it — one hides everything, one publishes everything. » Description : le problème
(H.3), le squelette et ses cinq points d'extension (H.5.7), les deux applications (H.9), les preuves chiffrées (H.4),
la stratégie Kiro (H.13), les limites assumées (H.5.3 et H.10). Section « Built with Kiro » : specs, hooks, steering
`accounting.md`, deux agents, power, MCP optionnel, et les contre-exemples trouvés par fast-check. **Bonus** : article
de blog « What a hash chain proves — and what it doesn't » (2 000 crédits) ; publication sociale avec une capture du
chiffre unique et une de la page publique.

### H.17 Recette

Les seuils sont durs ; les valeurs numériques ci-dessous sont des exemples de sortie à remplacer par la sortie réelle
le jour de la recette (ne jamais publier une valeur non mesurée).

- [ ] `node scripts/recette.mjs --only=import` → `12000 rows parsed in 0.61 s, 0 rejected` (< 1 s).
- [ ] `node scripts/recette.mjs --only=balance` → `trial balance: debit 4 317 55 = credit 4 317 55, 12000 entries` (égalité stricte).
- [ ] `node scripts/recette.mjs --only=chain` → `verifyChain: ok, 12000 links, head 9f2c…e41a, 118 ms` (< 150 ms).
- [ ] `node scripts/recette.mjs --only=tamper` (un octet modifié dans le fichier journal) → `verifyChain: FAILED at seq 4287, reason bad-hash` (index exact).
- [ ] `node scripts/recette.mjs --only=immutable` → `TypeError: cannot assign to read only property` puis `contra() produced 2 entries, original hash unchanged`.
- [ ] `pnpm test:property -- --numRuns=10000` → `15 properties passed, 0 unbalanced entries, seeds logged` (LED-N-13 : < 60 s).
- [ ] `node scripts/recette.mjs --only=replay` → `snapshot + replay: balances identical, head identical`.
- [ ] `node scripts/recette.mjs --only=public` → `public view: 147 812 bytes gzip (< 152 400), 0 private markers, 0 private account ids`.
- [ ] `node scripts/recette.mjs --only=network` (Playwright, 30 s d'usage sur les deux applications) → `0 requests`.
- [ ] `node scripts/recette.mjs --only=loc` → `core 2 143/2 200 · ui 1 771/1 800 · skeleton 186/200 · envelopes 638/700 · mutual-aid 674/700`.
- [ ] `node scripts/recette.mjs --only=a11y` (axe sur les trois sites) → `0 critical, 0 serious`.
- [ ] `node scripts/recette.mjs --only=fixtures` → `fixture-privacy-guard: 0 IBAN, 0 card numbers, 6/6 files marked FICTIONAL`.

### H.18 Questions ouvertes

1. Nom anglais définitif : « Ledger — a double-entry skeleton » (retenu) ou un nom moins générique, plus cherchable ? Le dépôt `ledger` est-il libre, sinon `ledger-skeleton` ?
2. `apps/time-bank` (banque du temps) reste-t-elle un artefact de la vidéo, ou devient-elle une troisième application livrée et hébergée ? Coût : 0,5 jour.
3. Niveau d'anonymisation par défaut de `mutual-aid` : `pseudonymised` (détail lisible, plus transparent) ou `aggregate` (plus protecteur, moins incarné) ? À trancher avant le lot H8.
4. Chiffrement au repos : livré en option (0,5 jour) ou exclu du périmètre pour tenir le gel vidéo ?
5. Serveur MCP `ledger-mcp` : le livrer (preuve d'usage MCP, +0,5 jour) ou s'en tenir à l'optionnel ?
6. La page publique est-elle un fichier commité dans le dépôt (prouvable par l'historique Git, ancrage naturel de la tête de chaîne) ou servie depuis un fragment d'URL ? Le premier est plus fort pour l'argument « vérifiable », le second plus simple.
7. Langue de l'interface par défaut : `en` seul (règlement) ou `en` + `fr` (notre public réel) ?
