## J. Séance — un retour d'expérience où les fantômes du dépôt se contredisent

Cahier des charges rédigé le 11 novembre 2026 pour le hackathon Kiroween 2026, catégorie **Costume Contest**.
Il se lit après `00-CONTEXTE-NOUVELLES-IDEES.md` (règlement, grille, socle technique, conventions) et ne
duplique pas le projet `placard` (Costume Contest déjà soumis, qui est un **manoir à parcourir**) :
ici l'interface est **une seule pièce vue de dessus**, une table ronde et cinq chaises. On ne s'y déplace pas.

Sources citées, consultées le 11/11/2026 : `https://sre.google/workbook/postmortem-culture/` (Google SRE
Workbook, chapitre 10, licence CC BY-NC-ND 4.0, cité brièvement) et `https://incident.io/` (page produit).
Tout ce qui n'a pas pu être vérifié est marqué **À vérifier**.

---

### X.1 Fiche d'identité

| | |
|---|---|
| Nom de travail | **Séance** |
| Nom anglais de soumission | *Séance — a postmortem where the ghosts of your repository disagree* |
| Dépôt | `seance` (GitHub public, MIT dès le premier commit, `/.kiro` versionné) |
| Trigramme des exigences | **SEA** (`SEA-F-nn`, `SEA-N-nn`, `SEA-P-nn`) |
| Catégorie | Costume Contest |
| En une phrase | On ouvre une séance autour d'un incident ; cinq fantômes, un par source de vérité, énoncent des affirmations liées à leurs preuves, et la séance refuse d'être close tant que leurs contradictions ne sont pas tranchées ou explicitement laissées ouvertes. |
| Public | Toute équipe de 2 à 50 personnes qui livre du logiciel : petits collectifs sans outil dédié, associations, agences, équipes internes d'une PME. Persona principal : trois personnes, aucun SRE à temps plein. |
| Idée centrale | **Le désaccord entre sources est l'artefact principal**, pas un bruit à lisser. Le procès-verbal n'est pas rédigé de mémoire : il est *calculé* à partir d'affirmations traçables, et sa porte de sortie est un différend non résolu. |
| Ce qui existe déjà | incident.io (plateforme SaaS complète : astreinte, investigations par agent, pages d'état), Blameless, FireHydrant, Rootly, Grafana Incident, les modèles de postmortem sans blâme (Google SRE, PagerDuty), Honeycomb pour l'observabilité. Tous supposent un compte, un abonnement et une organisation déjà outillée. **À vérifier** : périmètre et tarifs exacts de Blameless, FireHydrant, Rootly et Grafana Incident (pages inaccessibles le 11/11/2026 : redirections et 404). |
| Ce qui est différent | **Hors ligne, sans compte, utilisable par une équipe de trois personnes, et le seul à faire de la contradiction entre sources l'objet principal de l'analyse** — avec une porte de clôture qui refuse de fermer un désaccord non traité. |
| Prix visés | Best Costume Contest, prix globaux, **Best Demo** |
| Charge | **10 jours-agent** (périmètre minimal X.14), + 1,5 jour pour vidéo et textes |
| Risque principal | Que le costume soit perçu comme un décor plaqué. Parade : la table de correspondance de X.11 et le mode « vue du greffier ». |

### X.2 Ce que la catégorie demande, et la réponse

Texte officiel de la catégorie : « Build any app but show us a haunting user interface that's polished and
unforgettable. Bring in spooky design elements **that enhance your app's function**. »
Le membre de phrase décisif est le dernier : l'élément effrayant doit **améliorer la fonction**.

| Exigence du règlement (citée) | Réponse précise de Séance |
|---|---|
| « a haunting user interface » | Une pièce unique, sombre, vue de dessus : table ronde, cinq chaises qui se peuplent, bougies, poussière en suspension, planchette sur son plateau. Rendu en SVG/Canvas, aucune image tierce. |
| « polished » | Quatre états par écran (vide, chargement, erreur, contenu), mode clair complet, clavier intégral, `prefers-reduced-motion`, six vérifications de contraste chiffrées (X.11). |
| « unforgettable » | Le plan fort : cinq chaises vides qui se peuplent en 4 secondes, puis **immédiatement** une contradiction affichée et le bouton de clôture qui se verrouille. C'est la seconde 12 de la vidéo. |
| « spooky design elements that **enhance your app's function** » | Chaque élément est une vue de données : la chaise = un collecteur, la flamme = la confiance, le tiroir du cabinet = un artéfact, la planchette = le flux de synthèse avec sa provenance. Table complète en X.11. Aucun élément décoratif n'existe sans donnée derrière (vérifié par `npm run costume:audit`, X.17). |
| App construite avec Kiro, traces visibles | 7 specs, 3 hooks, 5 fichiers de steering, 1 skill, 1 agent en lecture seule, PBT sur 8 propriétés. Table en X.13, preuves dans `KIRO_JOURNAL.md`. |
| Dépôt public, MIT, `/.kiro` non ignoré | MIT au premier commit ; garde CI `conformance` qui échoue si `.kiro` est ignoré ou si `LICENSE` disparaît. |
| URL qui fonctionne jusqu'au 29/01/2027, gratuite, sans restriction | Site statique GitHub Pages, **aucun serveur**. L'URL ouvre la séance de démonstration préchargée : compréhension et résultat en moins de 30 s, sans compte. |
| Les juges peuvent juger sur vidéo et texte seulement | La vidéo (X.16) montre tout le parcours ; le procès-verbal exporté est joint au dépôt en `docs/demo/minutes.md`. |
| Vidéo < 3 min, publique, sans musique ni marque tierce | Script minuté 0:00 → 2:55 (X.16), voix seule, aucun logo, aucune musique. |
| Tous les éléments en anglais | Interface en anglais par défaut, français en seconde langue ; specs, README et vidéo en anglais. |
| Œuvre originale, dépendances sous licences compatibles | Dépendances : React, Vite, Zod, fast-check, Vitest, Playwright, `idb-keyval` (MIT/Apache-2.0). Aucun copyleft fort. Tableau des licences dans le README. |
| Crédits Kiro : 4 000 par participant, demande avant le 1er décembre | Demande à déposer immédiatement ; hooks en action « commande » par défaut pour ne pas consommer de crédits. |

### X.3 Problème, public et pourquoi maintenant

**Le retour d'expérience est écrit de mémoire, tard, par une seule personne.** Le chapitre 10 du Google SRE
Workbook (consulté le 11/11/2026) décrit exactement les modes de défaillance que Séance attaque :
publication retardée (« published four months after the incident »), actions sans propriétaire ni ticket
(« Without a formal tracking process, action items from postmortems are often forgotten »), langage
accusatoire, et le principe de Treynor Sloss : « To our users, a postmortem without subsequent action is
indistinguishable from no postmortem. » Ces documents disent *comment écrire* ; aucun outil grand public ne
dit **ce qui, dans les sources, se contredit**.

Situation datée, celle de la démonstration : **mardi 14 h 02, la panne du tunnel de commande**. Trois
personnes. Le vendredi, la plus ancienne écrit le retour d'expérience en 45 minutes de mémoire. Elle écrit
« le cache Redis a saturé » parce que c'est l'alerte qui l'a réveillée. En réalité : une demande de
changement demandait que le nouveau client Redis arrive derrière un drapeau ; il est arrivé sans drapeau ;
le défaut de reprise du client a créé une boucle de reprise ; la page d'état de l'hébergeur n'a jamais
signalé de bascule. Quatre sources, au moins deux versions des faits, et **aucune trace que quelqu'un s'en
soit aperçu**. Le compte rendu d'incident publié est faux, proprement faux.

Pourquoi maintenant : le télétravail a éclaté la chronologie (les gens racontent ce qu'ils ont vu dans leur
fenêtre), les incidents se diagnostiquent de plus en plus par agents qui produisent des affirmations sans
source apparente, et les petites équipes n'ont ni budget ni effectif pour un outil d'incident à 1 200
ingénieurs — l'échelle revendiquée par les clients d'incident.io sur sa page produit consultée le
11/11/2026 (Zendesk, « 1,200+ engineers »). L'écart entre l'outillage des grands et le vécu des petits est
le marché.

Personas :

- **Nadia, 34 ans, lead d'une équipe de trois** dans une agence de 20 personnes. Deux incidents par mois.
  Elle écrit les retours d'expérience le vendredi soir, seule. Elle veut un document défendable devant un
  client sans y passer la soirée.
- **Bruno, 41 ans, seul « technique »** d'une PME de 40 personnes (facturation, site, entrepôt). Il n'a pas
  d'astreinte formalisée ; il a un carnet, des alertes par courriel et une mémoire fatiguée.
- **Mia, 29 ans, cheffe de produit.** Elle assiste au postmortem et subit le récit de la voix la plus forte.
  Elle veut voir, noir sur blanc, ce que les autres sources disent.

Chiffres d'accroche : « 4 minutes au lieu de 45 » n'est **pas encore mesuré** → **À vérifier**. Protocole
exact en X.4 (indicateur I2) : un volontaire réel, chronométré deux fois, sur la séance de démonstration, la
mesure est affichée par l'outil et reprise telle quelle dans la vidéo ; si la mesure n'est pas faite avant le
26 novembre, la soumission dit « unverified, protocol in docs/MEASURE.md » et aucun chiffre n'est avancé.

### X.4 Objectifs, non-objectifs, indicateurs

**Objectifs**

- O1 — Convoquer cinq sources hétérogènes (changements, observations, demandes, dépendances, parole humaine)
  autour d'un incident, sans compte ni serveur.
- O2 — Ne laisser passer aucune affirmation sans preuve liée et localisable.
- O3 — Rendre les contradictions visibles, appariables et **bloquantes pour la clôture**.
- O4 — Produire un procès-verbal reproductible, exportable, imprimable, qui garde chaque affirmation liée à
  son artéfact.
- O5 — Faire tenir tout cela dans un costume qui aide à comprendre au lieu de distraire.

**Non-objectifs**

- Pas de collecte automatique auprès de services tiers (Slack, Jira, Datadog) : tout passe par des fichiers
  importés. Aucune clé d'API de service tiers.
- Pas de plateforme d'astreinte, pas de pages d'état, pas de chat d'incident.
- Pas de lecture automatique des conversations : un transcript n'est importé que sur action explicite, et
  seuls les passages horodatés sélectionnés deviennent des artéfacts.
- Pas de désignation d'un coupable : aucun champ de responsabilité individuelle n'est modélisable.
- Pas de modèle de langage obligatoire : il n'intervient, s'il est activé, que pour reformuler une phrase
  déjà produite.

**Indicateurs** (tous affichés par l'outil lui-même, dans l'en-tête du procès-verbal)

| # | Indicateur | Cible |
|---|---|---|
| I1 | Affirmations sans artéfact lié, sur toute séance | **0** (propriété SEA-P-01) |
| I2 | Temps de production du procès-verbal complet, incident de démonstration, volontaire réel | ≤ 6 min, mesure affichée ; objectif d'accroche « 4 min au lieu de 45 » **À vérifier** |
| I3 | Différends détectés / résolus / laissés ouverts | affichés, séance de démo : 3 / 1 / 1 (le troisième reste à trancher à l'écran) |
| I4 | Part du procès-verbal dont chaque affirmation remonte à un artéfact ouvert en un clic | 100 % |
| I5 | Séances clôturées avec un différend ouvert **sans raison** | 0 (impossible par construction) |
| I6 | Octets sortis de la machine pendant une séance complète, modèle désactivé | **0** (mesuré par le compteur `net.bytes.sent`) |
| I7 | Ouverture de la séance de démonstration sur un portable de 2020 | < 1,5 s jusqu'à la première affirmation cliquable |
| I8 | Contraste des six couples texte/fond utilisés | AA minimum, chiffres en X.11 |

### X.5 Le concept en profondeur

**1. La séance.** Une séance est un objet créé par un geste : un intitulé (« checkout tunnel outage, Tuesday
14:02 »), une fenêtre `[from, to]`, et un lieu de stockage local. Elle a un état : `open`, `in_review`,
`closed`. Rien ne se passe tant que la séance n'est pas ouverte : c'est le pendant fonctionnel de la
convocation rituelle.

**2. Cinq fantômes, cinq sources, aucune exception.** Chaque fantôme est un collecteur **borné à une seule
famille de source** — un fantôme ne peut pas citer la source d'un autre. C'est la contrainte qui fait la
valeur : elle rend les désaccords interprétables.

| Fantôme | Source unique | Question à laquelle il répond | Importeur |
|---|---|---|---|
| **Le Diff** *(the Diff)* | commits, pull requests | qu'est-ce qui a changé ? | `git-export` (CLI, lit un dépôt local) ou `changes.json` |
| **Le Veilleur** *(the Watcher)* | journaux, métriques, alertes | qu'est-ce qui a été observé, et quand ? | `alerts.csv`, `har`, `logs.txt` |
| **Le Greffier** *(the Clerk)* | tickets, demandes de changement, gels | qu'est-ce qui avait été demandé ? | `tickets.csv`, `change-requests.json` |
| **Le Fournisseur** *(the Supplier)* | avis de sécurité des dépendances, pages d'état | qu'est-ce qui a cassé en dessous ? | `advisories.json`, `status-page.md` |
| **Le Témoin** *(the Witness)* | notes d'astreinte, transcript importé | qu'est-ce que les gens ont dit ? | `oncall.md`, `transcript.md` (sélection manuelle) |

**3. L'affirmation.** Unité de base, et rien d'autre n'existe dans le modèle. Une affirmation =
`statement` (une phrase factuelle, ≤ 280 caractères, sans jugement) + `subject`/`predicate`/`value` (la forme
comparable, qui sert à détecter les conflits) + `window` + `confidence` + **au moins un** `artifactIds`.
Le texte visible et la forme comparable sont produits ensemble par le collecteur : sans forme comparable, pas
de détection ; sans artéfact, pas d'affirmation.

**4. La table des contradictions.** Le cœur. Deux affirmations sont en conflit si elles ont la même clé
`(subject, predicate)`, des fenêtres qui se chevauchent, et des `value` incompatibles pour ce prédicat
(égalité stricte pour `value_is`, supériorité pour `degraded`, non-recouvrement pour `changed`). Le conflit
est **symétrique** et **indépendant de l'ordre d'arrivée** des fantômes : c'est une paire non ordonnée
calculée sur l'ensemble, jamais sur un flux. Chaque paire devient un `Dispute` avec ses deux côtés, chacun
affichant fantôme, phrase, artéfact, confiance, date d'extraction. Aucune synthèse automatique ne tranche :
l'outil ne dit pas qui a raison, il dit **que deux sources ne disent pas la même chose, et où c'est écrit**.

**5. La porte de clôture.** `canClose(session)` est faux tant qu'un différend est `open`. Trois sorties :
`resolved` (on choisit un côté, ou une troisième lecture, avec une raison), `left_open` (on assume le
désaccord, avec une raison d'au moins 12 caractères), `escalated` (renvoi à une personne nommée, avec une
échéance). La raison est obligatoire : c'est la différence entre un désaccord documenté et un désaccord
oublié. Le bouton de clôture reste visible, désactivé, avec la liste des différends bloquants — jamais une
erreur après coup.

**6. La planchette.** La synthèse (3 à 5 phrases) est **épelée lettre par lettre** sur le plateau, et pendant
l'épelage les artéfacts qui portent la phrase s'illuminent dans le cabinet aux esprits, dans l'ordre exact où
la phrase les cite. La planchette n'est donc pas un effet : c'est une **vue de citation en direct**. Le
texte affiché sous le plateau est toujours complet, copiable et lisible par un lecteur d'écran (« le plateau
ne prouve rien ; les preuves, si. »).

**7. Le procès-verbal.** Document Markdown déterministe : en-tête (fenêtre, participants, indicateurs I1–I5),
chronologie reconstruite et vérifiée (aucun effet avant sa cause), facteurs contribuants **regroupés par
affirmation**, ce que chaque fantôme a affirmé (avec confiance), différends résolus avec leur raison, questions
ouvertes, actions avec propriétaire et échéance. Chaque affirmation du document porte un lien vers son
artéfact (`[ev:art_7f3a]`), et l'export HTML joint un index des artéfacts.

**8. Ce qui rend le concept honnête.** L'outil ne prétend jamais établir la vérité : il établit la
**traçabilité** et la **divergence**. Le mot « fantôme » est lui-même le rappel que ce qui parle est une
source, pas une personne.

### X.6 Formats et données

Tout est validé par Zod à l'entrée (fichiers importés) et à la sortie (procès-verbal, lien de partage).
Schémas de référence, `packages/core/src/domain/` (chaque fichier < 200 lignes) :

```ts
// artifact.ts
export type ArtifactKind =
  | 'commit' | 'pull_request' | 'log_excerpt' | 'metric_series' | 'alert'
  | 'ticket' | 'change_request' | 'freeze_window' | 'advisory' | 'status_page'
  | 'oncall_note' | 'transcript_excerpt';

export const ArtifactRefSchema = z.object({
  id: z.string().regex(/^art_[0-9a-f]{8}$/),
  kind: z.enum([...]),                                  // ArtifactKind
  label: z.string().min(1).max(120),                    // « PR #412 », « alert CHECKOUT-5XX »
  locator: z.object({                                   // où ouvrir la preuve
    uri: z.string().min(1),                             // chemin relatif ou URL source
    line: z.number().int().positive().optional(),
    sha: z.string().regex(/^[0-9a-f]{7,40}$/).optional(),
    at: z.string().datetime().optional(),               // horodatage de l'artéfact
    selector: z.string().max(120).optional(),           // ancre HAR / ligne CSV
  }),
  digest: z.string().regex(/^sha256:[0-9a-f]{64}$/),    // intégrité, calculée à l'import
  importedAt: z.string().datetime(),
});

// claim.ts
export const GhostId = z.enum(['diff', 'watcher', 'clerk', 'supplier', 'witness']);
export const Predicate = z.enum([
  'changed', 'did_not_change', 'failed', 'degraded', 'recovered',
  'was_requested', 'was_not_requested', 'was_frozen', 'was_announced', 'was_said',
]);

export const ClaimSchema = z.object({
  id: z.string().regex(/^clm_[0-9a-f]{8}$/),
  sessionId: z.string(),
  ghost: GhostId,
  statement: z.string().min(8).max(280),
  subject: z.string().min(1).max(60),                   // « checkout-tunnel », « redis-client-3.1 »
  predicate: Predicate,
  value: z.string().max(120).optional(),
  window: z.object({ from: z.string().datetime(), to: z.string().datetime() }),
  confidence: z.enum(['high', 'medium', 'low']),
  artifactIds: z.array(ArtifactRefSchema.shape.id).min(1),   // ← la règle, dans le type
  extractedAt: z.string().datetime(),
});

// dispute.ts
export const ResolutionSchema = z.discriminatedUnion('kind', [
  z.object({ kind: z.literal('resolved'), side: z.enum(['a', 'b', 'third_reading']),
             reason: z.string().min(12), author: z.string().min(1) }),
  z.object({ kind: z.literal('left_open'), reason: z.string().min(12), author: z.string().min(1) }),
  z.object({ kind: z.literal('escalated'), owner: z.string().min(1),
             dueAt: z.string().datetime(), reason: z.string().min(12) }),
]);

export const DisputeSchema = z.object({
  id: z.string().regex(/^dsp_[0-9a-f]{8}$/),
  claimA: z.string(), claimB: z.string(),                     // ordre canonique : id croissant
  rule: z.enum(['value_conflict', 'polarity', 'window_overlap', 'unexplained']),
  status: z.enum(['open', 'resolved', 'left_open', 'escalated']),
  resolution: ResolutionSchema.optional(),
});
```

Fenêtre de séance et en-tête :

```ts
export const SessionSchema = z.object({
  id: z.string().regex(/^sea_[0-9a-f]{8}$/),
  title: z.string().min(3).max(120),                    // « checkout tunnel outage, Tuesday 14:02 »
  windowFrom: z.string().datetime(),
  windowTo: z.string().datetime(),
  status: z.enum(['open', 'in_review', 'closed']),
  ghosts: z.array(z.object({ id: GhostId, state: z.enum(['mute', 'convened', 'spoken']) })),
  createdAt: z.string().datetime(),
  locale: z.enum(['en', 'fr']).default('en'),
});
```

**Importeurs — formats exacts**

| Importeur | Entrée | Sortie | Règle de conversion |
|---|---|---|---|
| `git-export` (CLI, `seance-cli git-export --since 2026-11-10T13:00Z --until 2026-11-10T15:00Z > changes.json`) | dépôt Git local | `changes.json` | 1 commit touchant un chemin lié au sujet → 1 affirmation `changed` ; 1 PR fusionnée → 1 affirmation avec `sha` dans le localisateur. **Aucun code source n'est copié** : seuls chemins, messages, shas, dates. |
| `har` | fichier HAR 1.2 (export navigateur) | artéfacts `metric_series` / `log_excerpt` | une entrée par requête lente (> seuil), `selector` = index d'entrée. **À vérifier** : version exacte du format HAR au moment de l'implémentation. |
| `alerts` | CSV RFC 4180, colonnes `timestamp,source,severity,name,value,unit` | artéfacts `alert` | 1 ligne = 1 artéfact ; les métriques continues sont échantillonnées à 1 point / 10 s maximum. |
| `transcript` | Markdown, lignes `- [14:03] Nadia: …` | artéfacts `transcript_excerpt` | **sélection manuelle** : l'interface liste les passages, l'utilisateur coche, seuls les cochés entrent. |
| `advisories` | JSON (OSV-like : `id, package, version_range, summary, published`) | artéfacts `advisory` | import local d'un fichier déjà téléchargé ; aucun appel réseau. |

**Séance de démonstration préchargée** (`packages/fixtures/src/demo-session.ts`, données 100 %
fictionnelles, aucun dépôt réel, aucun nom réel) : 34 affirmations réparties 8/7/6/5/8, tags plantés
`demo-01` … `demo-34`, trois différends prévus (`dsp_1` valeur Redis, `dsp_2` drapeau demandé mais absent,
`dsp_3` bascule hébergeur). Déterminisme garanti : dates fixes en UTC, aucun `Date.now()` dans les fixtures,
`Math.random` interdit (règle de lint).

### X.7 Exigences fonctionnelles

Notation EARS, identifiants `SEA-F-nn`, priorités **I** indispensable · **S** souhaitable · **O** optionnel ·
**X** exclu.

| ID | P | Exigence |
|---|---|---|
| SEA-F-01 | I | QUAND l'utilisateur ouvre une séance (intitulé, fenêtre, au moins un artéfact importé), le système DOIT créer une séance à l'état `open` et afficher la table ronde avec cinq chaises. |
| SEA-F-02 | I | QUAND un artéfact est importé pour une famille de source, le système DOIT passer le fantôme correspondant de `mute` à `convened` et peupler sa chaise. |
| SEA-F-03 | I | TANT QU'un fantôme est à l'état `mute`, le système DOIT afficher sa chaise vide avec la raison (`no artifacts imported`) et le geste qui la remplit (bouton d'import). |
| SEA-F-04 | I | QUAND un collecteur émet une affirmation, le système DOIT refuser et journaliser `claim.rejected.no_artifact` si la liste `artifactIds` est vide. |
| SEA-F-05 | I | SI le localisateur d'un artéfact ne peut pas être ouvert, ALORS le système DOIT marquer l'affirmation `evidence_broken` et abaisser sa confiance à `low`, sans la supprimer. |
| SEA-F-06 | I | QUAND deux affirmations partagent `(subject, predicate)` avec fenêtres chevauchantes et valeurs incompatibles, le système DOIT créer un `Dispute` dont les côtés sont ordonnés par identifiant croissant. |
| SEA-F-07 | I | QUAND un différend est créé, le système DOIT l'afficher dans la table des contradictions avec les deux phrases, les deux fantômes, les deux artéfacts et les deux confiances. |
| SEA-F-08 | I | QUAND l'utilisateur clique un artéfact, le système DOIT ouvrir le tiroir correspondant du cabinet aux esprits avec l'extrait exact et son localisateur. |
| SEA-F-09 | I | TANT QU'au moins un différend est à l'état `open`, le système DOIT désactiver la clôture et lister les différends bloquants sur le bouton lui-même. |
| SEA-F-10 | I | QUAND l'utilisateur résout un différend, le système DOIT exiger un côté (`a`, `b`, `third_reading`) et une raison d'au moins 12 caractères. |
| SEA-F-11 | I | QUAND l'utilisateur laisse un différend ouvert, le système DOIT exiger une raison d'au moins 12 caractères et enregistrer l'état `left_open`. |
| SEA-F-12 | I | QUAND la séance passe à `closed`, le système DOIT produire le procès-verbal Markdown et proposer son téléchargement ainsi que l'impression. |
| SEA-F-13 | I | QUAND le procès-verbal est rendu, chaque affirmation DOIT y apparaître avec son fantôme, sa confiance et son lien d'artéfact. |
| SEA-F-14 | I | QUAND l'utilisateur demande la synthèse, le système DOIT l'épeler lettre par lettre sur le plateau en illuminant, dans l'ordre de citation, les artéfacts sources. |
| SEA-F-15 | I | OÙ `prefers-reduced-motion: reduce` est actif, le système DOIT afficher la synthèse complète immédiatement, sans épelage, avec la liste des artéfacts cités. |
| SEA-F-16 | I | OÙ le mode « vue du greffier » est activé, le système DOIT afficher un tableau clair des affirmations (fantôme, phrase, artéfact, confiance, différend) sans aucun élément de décor. |
| SEA-F-17 | I | QUAND une séance est importée depuis un transcript, le système DOIT exiger une action explicite de l'utilisateur sur chaque passage retenu ; aucun passage n'est lu automatiquement. |
| SEA-F-18 | S | QUAND l'utilisateur reconstruit la chronologie, le système DOIT trier les artéfacts par date et signaler tout effet dont l'artéfact précède sa cause déclarée. |
| SEA-F-19 | S | QUAND l'utilisateur ajoute une action au procès-verbal, le système DOIT exiger un propriétaire et une échéance. |
| SEA-F-20 | S | QUAND l'utilisateur exporte la séance, le système DOIT produire un dossier zippé : `minutes.md`, `claims.json`, `disputes.json`, `artifacts-index.csv`. |
| SEA-F-21 | S | QUAND l'utilisateur génère un lien de partage, le système DOIT produire un JSON expurgé (aucun identifiant interne, aucun chemin absolu, aucun courriel) et l'afficher pour copie manuelle. |
| SEA-F-22 | O | OÙ l'appel à un modèle est activé dans les réglages, le système DOIT proposer uniquement une reformulation de phrase existante, afficher le texte original à côté, et ne jamais créer ni modifier une affirmation. |
| SEA-F-23 | O | QUAND l'utilisateur change de langue (en/fr), le système DOIT re-render l'interface sans toucher aux données de séance. |
| SEA-F-24 | O | QUAND l'utilisateur imprime le procès-verbal, le système DOIT basculer automatiquement en feuille de style claire à fort contraste. |
| SEA-F-25 | X | Le système NE DOIT PAS envoyer de données, de code ou de transcript à un serveur tiers sans activation explicite dans les réglages. |
| SEA-F-26 | X | Le système NE DOIT PAS lire de conversation, de messagerie ou de dossier distant de sa propre initiative. |
| SEA-F-27 | X | Le système NE DOIT PAS créer de séance, de différend ou de procès-verbal sans artéfact importé : aucun contenu généré « pour l'exemple » en dehors des fixtures déclarées. |
| SEA-F-28 | X | Le système NE DOIT PAS désigner une personne comme responsable d'un incident : aucun champ de blâme n'existe dans le modèle. |

### X.8 Exigences non fonctionnelles

| ID | P | Exigence | Cible mesurable |
|---|---|---|---|
| SEA-N-01 | I | Temps d'ouverture de la séance de démonstration (chargement → première affirmation cliquable) | < 1,5 s sur portable 2020, mesuré par Playwright (`performance.timing`) |
| SEA-N-02 | I | Rendu de 500 affirmations dans la table | < 300 ms, virtualisation au-delà de 120 lignes |
| SEA-N-03 | I | Détection de contradictions sur 500 affirmations | < 200 ms (prégroupement par clé, aucun parcours quadratique global) |
| SEA-N-04 | I | Taille du bundle initial (gzip) | ≤ 250 ko ; garde CI qui échoue au-delà |
| SEA-N-05 | I | Accessibilité | Contraste AA pour les six couples de X.11, navigation clavier intégrale (carte en X.11), aucun texte porteur de sens rendu uniquement par la couleur, `prefers-reduced-motion` respecté, `axe-core` sans violation en CI |
| SEA-N-06 | I | Vie privée | Zéro requête réseau en mode normal ; CSP `default-src 'self'; connect-src 'none'` tant que le modèle n'est pas activé ; aucun télémétrie, aucun cookie |
| SEA-N-07 | I | Hors ligne | L'application fonctionne entièrement après un chargement initial ; les importeurs sont locaux ; `navigator.onLine` n'est jamais consulté pour décider d'une fonction |
| SEA-N-08 | I | Robustesse | Tout fichier importé est validé par Zod ; une entrée invalide produit une erreur lisible nommant le fichier, la ligne et le champ, et n'interrompt pas la séance |
| SEA-N-09 | S | Stockage local | IndexedDB via `idb-keyval`, plafond d'avertissement à 50 Mo, purge explicite en un geste |
| SEA-N-10 | S | Aucun son par défaut | Tout son est derrière un réglage désactivé ; aucun son pendant l'épelage de la planchette |
| SEA-N-11 | S | Code | < 500 lignes par fichier, < 50 lignes par fonction, zéro duplication ; garde `loc-budget` en CI |
| SEA-N-12 | S | Déterminisme | Le procès-verbal est une fonction pure : mêmes entrées → mêmes octets, horodatage de génération exclu du corps (placé en pied, après hachage) |
| SEA-N-13 | O | Internationalisation | anglais par défaut (soumission), français disponible ; aucune chaîne visible codée en dur hors fichiers de messages |
| SEA-N-14 | O | Pérennité de l'hébergement | Pages GitHub statiques, aucune dépendance de service, tenue jusqu'au 29/01/2027 sans intervention |

### X.9 Architecture technique

Monorepo pnpm, TypeScript strict, Vite + React pour le site statique, CLI Node pour les importeurs locaux.
**Aucun serveur** : le site est statique, les importeurs tournent sur la machine de l'utilisateur, les
données restent dans le navigateur (IndexedDB) ou dans des fichiers locaux.

```
seance/
├── .kiro/
│   ├── steering/{product,tech,structure,testing,costume}.md   # 5 fichiers, ≤ 120 lignes chacun
│   ├── specs/{ghost-diff,ghost-watcher,ghost-clerk,ghost-supplier,ghost-witness,
│   │          dispute-table,minutes}/                          # 7 specs, 3 fichiers chacune
│   ├── hooks/{claim-provenance-guard,seance-open-guard,costume-audit}.json
│   ├── agents/clerk.md                                         # relecteur en lecture seule
│   ├── skills/open-seance/SKILL.md
│   └── settings/mcp.json                                       # MCP optionnel
├── apps/
│   ├── web/                       # Vite + React, le salon et la vue du greffier
│   │   └── src/
│   │       ├── scenes/            # TableScene, DisputeTable, Cabinet, Planchette, ClerkView
│   │       ├── state/             # machine de séance (xstate-lite maison, ~180 lignes)
│   │       ├── i18n/{en,fr}.ts
│   │       └── main.tsx
│   └── cli/                       # seance-cli : git-export, har, alerts, transcript
│       └── src/commands/{git-export,har,alerts,transcript}.ts
├── packages/
│   ├── core/                      # domaine pur : claim, dispute, resolution, minutes, chronology
│   │   └── src/{artifact,claim,dispute,resolution,minutes,chronology,gate}.ts
│   ├── importers/                 # git, har, alerts, transcript, advisories → artéfacts
│   ├── fixtures/                  # demo-session.ts (déterministe, données fictionnelles)
│   ├── costume/                   # rendu SVG/Canvas : table, chaises, flammes, planchette, cabinet
│   └── ui-tokens/                 # palette, contrastes, typographie, mouvements
├── scripts/{recette.mjs,contrast.mjs,costume-audit.mjs,measure.mjs}
├── docs/{demo/minutes.md, MEASURE.md, ARCHITECTURE.md}
├── KIRO_JOURNAL.md · README.md · LICENSE (MIT) · .github/workflows/{ci,conformance}.yml
└── package.json · pnpm-workspace.yaml · tsconfig.base.json
```

**Budgets de lignes par paquet** (garde `loc-budget` en CI, fichiers < 500 lignes partout) :

| Paquet | Lignes max | Raison |
|---|---|---|
| `packages/core` | 1 400 | Domaine pur, le plus testé ; `gate.ts` ≤ 80 lignes |
| `packages/importers` | 1 200 | 5 importeurs, ≤ 250 lignes chacun |
| `packages/fixtures` | 500 | Séance de démonstration, données littérales |
| `packages/costume` | 1 500 | Table, chaises, flammes, cabinet, planchette |
| `packages/ui-tokens` | 200 | Palette et contrastes, une seule source de vérité |
| `apps/web` | 2 200 | Scènes et état |
| `apps/cli` | 700 | 4 commandes |
| `scripts` | 400 | recette, contraste, audit costume, mesure |

**Flux de données**

```
fichiers locaux ──CLI/importeurs──▶ ArtifactStore (IndexedDB)
                                        │  (digest sha256, localisateur)
                    collectors bornés ──┤  1 famille de source = 1 fantôme
                                        ▼
                                   Claim[]  ──▶ contradiction engine ──▶ Dispute[]
                                        │                                    │
                                        │                              closure gate
                                        ▼                                    ▼
                                 chronology (tri, cohérence cause/effet) ──▶ canClose?
                                                                             │
                                              planchette (épelage + provenance)│
                                                                             ▼
                                                               minutes.ts (Markdown, pur)
```

Ce qui tourne où : tout le domaine (`core`, `importers`, `costume`) tourne **dans le navigateur** pour le site
statique ; la CLI est le seul composant qui lit le disque, et elle n'écrit que des fichiers JSON/CSV que
l'utilisateur dépose lui-même dans l'interface. Le test de non-réseau (`SEA-N-06`) intercepte toutes les
requêtes dans Playwright et échoue au premier octet sortant.

### X.10 Sécurité et modèle de menace

| # | Menace | Vraisemblance | Impact | Parade |
|---|---|---|---|---|
| T1 | Fuite de code source : un importeur copie du code ou un diff complet dans un artéfact | Moyenne | Grave | Les importeurs ne conservent que chemins, messages, shas, dates, métriques. Un test de propriété vérifie qu'aucun artéfact ne contient plus de 3 lignes consécutives de code. `SEA-F-25`. |
| T2 | Fuite de conversation : un transcript importé expose des noms et des courriels dans un lien partagé | Élevée | Grave | Import sur sélection explicite (`SEA-F-17`) ; l'export de partage expurge identifiants internes, chemins absolus et courriels (`SEA-F-21`, propriété SEA-P-05) ; le transcript brut n'est jamais inclus dans le procès-verbal. |
| T3 | Exfiltration silencieuse par un appel modèle non désiré | Faible | Grave | Modèle désactivé par défaut, activation en deux gestes avec affichage de ce qui part ; CSP `connect-src 'none'` tant que non activé ; compteur `net.bytes.sent` affiché dans l'en-tête. |
| T4 | Empoisonnement des preuves : un fichier importé falsifie la chronologie ou casse la séance | Moyenne | Moyen | Validation Zod systématique, horodatages bornés à la fenêtre (hors fenêtre → artéfact rejeté avec raison), digests sha256 recalculés à chaque ouverture. |
| T5 | Faux sentiment de vérité : l'utilisateur croit que la planchette « prouve » quelque chose | Élevée | Moyen | La phrase « the board proves nothing; the evidence does » est affichée sous le plateau ; chaque lettre épelée renvoie à un artéfact cliquable ; aucun score de certitude global n'est produit. |
| T6 | Clôture forcée : un utilisateur ferme la séance en contournant la porte | Faible | Moyen | La porte est dans le domaine (`gate.ts`), pas dans l'interface : l'état `closed` est refusé côté modèle. Test de propriété SEA-P-02. |
| T7 | Déni de service local : 50 000 alertes importées gèlent l'interface | Moyenne | Faible | Plafond d'import (20 000 artéfacts par séance), échantillonnage des métriques continues, avertissement avant traitement, traitement par lots avec barre de progression. |
| T8 | Ré-identification dans une séance partagée (petite équipe + horodatages précis) | Moyenne | Moyen | Avertissement explicite à l'export ; option « anonymiser les auteurs » qui remplace les noms par des rôles (`on-call`, `reviewer`) ; les fixtures de démo n'utilisent aucun nom réel. |
| T9 | Dépôt non conforme au règlement (licence absente, `.kiro` ignoré) | Faible | Élevé | Garde CI `conformance` : échoue si `LICENSE` manque, si `.kiro` est dans `.gitignore`, ou si un copyleft fort apparaît dans le lockfile. |
| T10 | Copie d'éléments visuels tiers (polices, illustrations) | Faible | Moyen | Polices sous licence libre uniquement, illustrations SVG dessinées pour le projet, tableau des licences dans le README. |

### X.11 Interface et direction artistique

**Une seule pièce, vue de dessus.** Un salon assombri, une table ronde recouverte d'un tapis de billard vert,
cinq chaises, un cabinet aux esprits à tiroirs contre le mur, une planchette sur son plateau au centre, de la
poussière en suspension dans la lumière d'une fenêtre haute. Contrairement à `placard`, on **ne se déplace
pas** : la caméra est fixe, tout se passe à la table. Le décor est un plan de travail, pas un niveau.

**Palette (mode sombre, valeurs exactes et contrastes mesurés le 11/11/2026 avec `scripts/contrast.mjs`,
algorithme WCAG 2.1, luminance relative)**

| Rôle | Nom | Hex | Utilisation | Contraste mesuré |
|---|---|---|---|---|
| Fond de pièce | `ink` | `#0E0C14` | fond du salon | — |
| Surface | `parlour` | `#1A1626` | panneaux, tiroirs du cabinet | — |
| Tapis | `baize` | `#1F5C46` | table ronde | — |
| Tapis éclairé | `baize-lit` | `#2C7A5E` | zone survolée | — |
| Texte principal | `linen` | `#F2EDE3` | phrases, titres | 16,64:1 sur `ink`, 15,17:1 sur `parlour` — **AAA** |
| Texte secondaire | `slate` | `#B9B2C6` | libellés, horodatages | 9,48:1 sur `ink`, 8,63:1 sur `parlour` — **AAA** |
| Bougie / accent | `tallow` | `#F5C15A` | flammes, focus, liens actifs | 11,71:1 sur `ink`, 10,67:1 sur `parlour` — **AAA** |
| Esprit / lien | `ectoplasm` | `#9FE3D0` | liens d'artéfact, surbrillance planchette | 13,29:1 sur `ink`, 12,11:1 sur `parlour` — **AAA** |
| Différend | `vermilion` | `#FF7A5C` | badge de contradiction non résolue | 7,57:1 sur `ink`, 6,90:1 sur `parlour` — **AAA** |
| Cire / bord | `wax` | `#C9BFA8` | liserés, séparateurs non texte | 10,64:1 sur `ink`, 4,30:1 sur `baize` — ≥ 3:1 requis pour les éléments non texte, **conforme** |
| Texte sur tapis | `linen` sur `baize` | `#F2EDE3` / `#1F5C46` | texte posé sur la table | 6,72:1 — **AA** |

Règle dure dérivée des mesures : **aucun texte `slate` ni `vermilion` directement sur le tapis** (3,83:1 et
3,06:1, insuffisants) — les cartes d'affirmation reposent toujours sur une plaque `parlour` bordée de `wax`.
Le badge de différend ne s'affiche jamais en couleur seule : il porte le mot `UNRESOLVED` en capitales et un
glyphe de balance déséquilibrée.

**Mode clair — « la vue du greffier »** (*the Clerk's view*). Un simple tableau d'affirmations sur papier :

| Rôle | Hex | Contraste mesuré |
|---|---|---|
| Fond `clerk-bg` | `#FBF8F1` | — |
| Texte `clerk-ink` | `#1B1725` | 16,56:1 — **AAA** |
| Secondaire `clerk-muted` | `#5A5367` | 6,90:1 — **AA** |
| Accent `clerk-accent` | `#0F6B4F` | 6,12:1 — **AA** |
| Différend `clerk-dispute` | `#B3341A` | 5,78:1 — **AA** |
| Filets `clerk-rule` | `#6E6780` | 5,06:1 — **AA** (le `#8A8394` mesuré à 3,44:1 est réservé aux éléments non texte) |

L'existence de ce mode **est la preuve que le costume est une peau** : mêmes données, mêmes gestes, zéro décor.
Bascule par `v` ou par le menu, préférence persistée.

**Typographie.** Titres : un didone/décoratif libre de droits rappelant les affiches spirites de 1900
(candidat : *Playfair Display*, OFL — **À vérifier** : licence et chasse à confirmer avant intégration).
Corps : *Source Serif 4* (OFL). Code, horodatages et localisateurs : *IBM Plex Mono* (OFL). Trois familles
maximum, aucune police tierce non libre, toutes auto-hébergées dans le bundle.

**Mouvement.** Tout mouvement dure ≤ 400 ms. Les flammes de bougie vacillent avec une amplitude proportionnelle
à `(1 − confiance)` : une confiance `high` donne une flamme quasi fixe, `low` une flamme qui tremble — **et** la
confiance est écrite en toutes lettres (`high`/`medium`/`low`) **et** portée par une barre de 3 segments. Jamais
par la seule couleur, jamais par le seul mouvement. La poussière en suspension est un canvas de 60 particules
maximum, désactivé si `prefers-reduced-motion`.

`prefers-reduced-motion: reduce` → la planchette **donne le texte directement**, sans épelage, avec la liste des
artéfacts cités en dessous ; les flammes sont fixes ; la poussière disparaît ; l'apparition des fantômes devient
un fondu de 120 ms.

**Écrans (quatre, pas un de plus)**

1. **La table** (`TableScene`) — vue principale. Table ronde, cinq chaises, cabinet à droite, planchette au
   centre, bouton de clôture en bas à droite.
2. **La table des contradictions** (`DisputeTable`) — panneau latéral qui se déplie ; liste des différends,
   chacun ouvrable en vis-à-vis.
3. **Le cabinet aux esprits** (`Cabinet`) — tiroirs = magasin de preuves ; un tiroir par artéfact, groupés par
   fantôme ; s'ouvre au clic sur n'importe quel lien.
4. **Le procès-verbal** (`MinutesView`) — document rendu, export, impression.

**États obligatoires, par écran**

| État | Ce que voit l'utilisateur |
|---|---|
| Vide | Table aux cinq chaises vides, une phrase : « No séance is open. The room waits. » + bouton *Open a séance* + lien *Load the demo incident*. Aucune chaise n'est peuplée d'office. |
| Chargement | Les chaises apparaissent l'une après l'autre à mesure que les artéfacts sont indexés, avec un compteur « 12 / 34 artifacts ». Barre de progression textuelle en plus de l'animation. |
| Erreur | Une carte `parlour` bordée de `vermilion` nomme le fichier, la ligne et le champ invalides (« `alerts.csv` line 47: `timestamp` is not ISO-8601 »), propose *Skip this row* / *Skip this file* / *Cancel import*. La séance reste ouverte. |
| Contenu | Voir écrans ci-dessus. |
| Succès de clôture | Le cachet de cire se pose sur le procès-verbal, les cinq flammes s'éteignent en 400 ms, le document reste lisible et copiable. |

**Le test de cohérence (X.11) — si on retire tout le costume, il reste exactement le même outil.**

| Élément du costume | Fonction sans le costume | Preuve que c'est la même chose |
|---|---|---|
| La convocation des cinq fantômes | La collecte multi-sources bornée | Cinq chaises vides = cinq importeurs sans artéfact ; chaise peuplée = importeur ayant produit des artéfacts. Le mode greffier affiche la même liste sous forme de cinq sections. |
| Chaque fantôme (le Diff, le Veilleur, le Greffier, le Fournisseur, le Témoin) | Un collecteur borné à une seule famille de source | Le nom du fantôme est le libellé d'affichage de `GhostId` ; retirer le costume remplace le libellé par `diff`/`watcher`/… sans changer une ligne de logique. |
| La planchette qui épèle | Le flux de synthèse avec sa provenance en direct | Lettre épelée ↔ position dans le texte ; artéfact illuminé ↔ `artifactIds` de l'affirmation citée. En mode réduit, le texte et la liste des artéfacts cités suffisent. |
| Le cabinet aux esprits à tiroirs | Le magasin de preuves | Un tiroir = un `ArtifactRef` ; ouvrir le tiroir = afficher `locator` + extrait. En mode greffier, c'est une liste dépliante. |
| « Les fantômes se contredisent » | La détection de contradiction | Le différend est une paire d'affirmations avec une règle de conflit ; les visages des fantômes ne participent pas au calcul. |
| L'interdiction de clore la séance | La porte de qualité du retour d'expérience | `gate.canClose()` est une fonction pure du domaine ; le bouton verrouillé n'en est que l'affichage. |
| Les flammes qui vacillent | L'affichage de la confiance | Triple codage : flamme + mot + barre. Les deux derniers survivent sans le costume. |
| La poussière, les ombres | Rien | **Seul élément purement décoratif**, assumé comme tel, supprimé en `prefers-reduced-motion`, jamais porteur d'information. |
| Le cachet de cire à la clôture | L'état `closed` + le hachage du document | En mode greffier : la mention `CLOSED` et l'empreinte sha256. |

**Navigation clavier (complète, sans souris)**

| Touche | Action |
|---|---|
| `Tab` / `Shift+Tab` | Cycle : chaises → planchette → cabinet → table des contradictions → clôture |
| `1` … `5` | Aller au fantôme 1 à 5 (le Diff, le Veilleur, le Greffier, le Fournisseur, le Témoin) |
| `Enter` | Ouvrir l'artéfact / déplier le différend |
| `d` | Ouvrir la table des contradictions (*disputes*) |
| `c` | Ouvrir le cabinet |
| `m` | Afficher le procès-verbal |
| `v` | Basculer salon / vue du greffier |
| `Esc` | Fermer le panneau courant, rendre le focus à son origine |
| `?` | Afficher la carte des raccourcis |

Focus visible : anneau `tallow` de 2 px avec décalage de 2 px, contraste ≥ 3:1 sur toutes les surfaces
(vérifié par `axe-core`). Tous les éléments interactifs sont des éléments natifs (`button`, `a`, `input`),
jamais des `div`. Rôles ARIA : la table est une `region` nommée « séance table », les différends une `list`
avec `aria-live="polite"` sur les changements d'état, la planchette une `status` region dont le texte complet
est toujours présent dans le DOM (jamais seulement animé).

**Aucun son par défaut.** Tout son (trois au maximum : apparition, contradiction, cachet) est derrière un
réglage `sound: off` par défaut, et aucun son ne porte d'information.

### X.12 Propriétés à tester

Générateurs fast-check partagés dans `packages/core/src/testing/generators.ts` : `arbArtifact`, `arbClaim`,
`arbClaimPairSameKey`, `arbSession`, `arbDispute`. Chaque propriété est rattachée à un critère d'acceptation.

| ID | Invariant exact | Générateur | Critère lié |
|---|---|---|---|
| SEA-P-01 | **Aucune affirmation sans artéfact lié.** Pour toute affirmation admise dans une séance, `claim.artifactIds.length ≥ 1` et chaque identifiant résout vers un `ArtifactRef` existant dont le localisateur est non vide. | `arbClaim` dont le champ `artifactIds` est tiré dans `fc.array(fc.constant('art_missing'), {minLength:0, maxLength:2})` → l'admission doit échouer | SEA-F-04, I1 |
| SEA-P-02 | **Une séance avec un différend non résolu ne peut pas être close.** `gate.canClose(s) === false` dès qu'il existe un différend de statut `open` ; et `close(s)` lève `SeanceBlockedError` listant les identifiants bloquants. | `arbSession` + `fc.array(arbDispute, {minLength:1})` avec statut forcé à `open` | SEA-F-09, I5 |
| SEA-P-03 | **Le procès-verbal est une fonction pure.** `renderMinutes(s, c, d) === renderMinutes(s, c, d)` octet pour octet, pour des entrées identiques, y compris après un changement d'ordre de tableau en entrée (le rendu trie). | `arbSession` + listes permutées par `fc.shuffledSubarray` | SEA-F-12, SEA-N-12 |
| SEA-P-04 | **La détection de contradiction est symétrique et indépendante de l'ordre d'arrivée.** `detect([a,b])` et `detect([b,a])` produisent le même ensemble de différends à identifiants près, et `dispute.claimA < dispute.claimB` toujours. | `arbClaimPairSameKey`, puis permutations aléatoires de listes de 3 à 40 affirmations | SEA-F-06 |
| SEA-P-05 | **Aucun identifiant interne ne fuit dans une vue partagée.** `shareView(s)` ne contient aucune occurrence de `/^(clm|dsp|art|sea)_[0-9a-f]{8}$/`, aucun chemin absolu (`/home/`, `C:\`), aucun courriel. | `arbSession` avec artéfacts dont les `locator.uri` contiennent des chemins absolus et des courriels plantés | SEA-F-21, T2 |
| SEA-P-06 | **La chronologie est cohérente : aucun effet avant sa cause dans la fenêtre.** Pour tout couple `(cause, effet)` déclaré, `cause.window.from ≤ effet.window.from` ; sinon l'outil émet un avertissement `chronology.inverted` et ne l'efface pas. | `arbSession` + paires dont l'ordre des fenêtres est inversé dans 50 % des cas | SEA-F-18 |
| SEA-P-07 | **Confiance monotone dans la preuve.** Ajouter un artéfact à une affirmation ne peut pas diminuer sa confiance ; retirer le dernier artéfact la fait passer à `low` ou rejette l'affirmation. | `arbClaim` + `fc.array(arbArtifact, {minLength:0, maxLength:4})` | SEA-F-05, SEA-F-07 |
| SEA-P-08 | **Un artéfact hors fenêtre n'engendre aucune affirmation.** Pour tout artéfact dont l'horodatage est hors `[windowFrom, windowTo]`, aucune affirmation de la séance ne le cite. | `arbSession` + artéfacts horodatés à ±48 h de la fenêtre | SEA-N-08, T4 |
| SEA-P-09 | **Résolution exige une raison.** `resolve(d, side, reason)` échoue pour toute raison de longueur < 12 ; `left_open` idem. Aucune résolution sans raison n'est représentable. | `fc.string({minLength:0, maxLength:30})` | SEA-F-10, SEA-F-11 |
| SEA-P-10 | **Le costume ne change pas les données.** Le rendu en mode salon et en mode greffier produisent le même jeu d'affirmations, de différends et de résolutions (comparaison des vues normalisées). | `arbSession` complet | X.11 test de cohérence |
| SEA-P-11 | **Idempotence des importeurs.** Importer deux fois le même fichier produit le même ensemble d'artéfacts (mêmes digests), sans doublon. | `arbArtifactFile` rejoué deux fois | SEA-N-08 |
| SEA-P-12 | **Aucune donnée ne sort.** Pendant une séance complète en mode par défaut, le compteur `net.bytes.sent` reste à 0 (test Playwright avec interception de toutes les requêtes). | parcours de bout en bout sur les fixtures | SEA-F-25, SEA-N-06, I6 |

### X.13 Stratégie Kiro

| Fonction de Kiro | Emploi précis dans Séance | Preuve produite dans le dépôt |
|---|---|---|
| **Specs de fonctionnalité** (7) | Une spec par fantôme = un collecteur borné (`ghost-diff`, `ghost-watcher`, `ghost-clerk`, `ghost-supplier`, `ghost-witness`), plus `dispute-table` et `minutes`. Chaque spec part des exigences EARS de X.7. | `.kiro/specs/<fn>/{requirements,design,tasks}.md` ; 21 fichiers versionnés |
| **Analyse des exigences** | Passée sur chaque `requirements.md` avant conception, pour traquer les trous (ex. : que fait-on d'un différend dont un côté a une preuve cassée ?) | Notes d'analyse en tête de chaque `requirements.md` |
| **Correctness / tests par propriétés** | Les 12 propriétés SEA-P-nn sont rattachées à leurs critères et générées avec fast-check | `packages/core/src/**/*.property.test.ts`, contre-exemples conservés dans `KIRO_JOURNAL.md` |
| **Exécution parallèle des tâches** | Les cinq collecteurs sont indépendants : ils partent en vague parallèle, `dispute-table` et `minutes` en seconde vague | Historique des tâches dans `tasks.md`, horodaté |
| **Hooks** | `claim-provenance-guard` (action « commande » : interdit une affirmation sans `artifactIds`), `seance-open-guard` (refuse une mutation de séance close), `costume-audit` (vérifie que tout élément visuel porte une donnée) | `.kiro/hooks/*.json`, compteur de déclenchements dans le journal |
| **Skill `open-seance`** | Procédure répétée : ouvrir une séance à partir d'un dossier de fichiers importés, indexer, convoquer | `.kiro/skills/open-seance/SKILL.md` |
| **Agent personnalisé « le greffier »** | Relecteur **en lecture seule** qui rédige et relit le procès-verbal, sans droit d'écriture sur le code | `.kiro/agents/clerk.md`, permissions restreintes |
| **Steering** | `product.md` (le désaccord est l'artefact), `tech.md` (pile, interdits : pas de réseau, pas de `Math.random`), `structure.md` (arborescence X.9), `testing.md` (propriétés), `costume.md` (`fileMatch: packages/costume/**` — la table de correspondance X.11) | `.kiro/steering/*.md` |
| **MCP (optionnel)** | Serveur de documentation si besoin ; aucun MCP ne voit de donnée utilisateur | `.kiro/settings/mcp.json` |
| **Journal** | `KIRO_JOURNAL.md` répond aux questions du formulaire de soumission : surfaces utilisées, hooks et gain, spec contre « vibe coding » (durée, allers-retours, défauts trouvés), steering décisif, contre-exemples de PBT | Journal tenu au fil de l'eau |

Comparaison imposée « spec contre vibe coding » : la table des contradictions (`dispute-table`) est écrite une
fois en mode spec, une fois en mode libre ; le journal note durée, allers-retours et défauts trouvés par chacun.

### X.14 Plan de réalisation

**10 jours-agent** pour le périmètre minimal, hors vidéo et textes (+1,5 jour). Gel vidéo : **28 novembre**.
Tout ce qui est marqué ✅ doit être **mergé avant le 28/11** ; au-delà, c'est du polissage post-gel.

| Lot | Contenu | Dépend de | Jours | Avant gel ? |
|---|---|---|---|---|
| L0 | Socle : monorepo, MIT, CI (`ci-budget`, `conformance`), tokens, contrastes | — | 0,5 | ✅ |
| L1 | `packages/core` : artifact, claim, gate, chronology + SEA-P-01/02/03 | L0 | 1,5 | ✅ |
| L2 | Moteur de contradiction + SEA-P-04/07/08 | L1 | 1,5 | ✅ |
| L3 | Importeurs (git-export, har, alerts, transcript, advisories) + SEA-P-11 | L1 | 1,5 | ✅ |
| L4 | Fixtures de démonstration déterministes | L1, L3 | 0,5 | ✅ |
| L5 | Scènes : table, chaises, flammes, cabinet | L0, L4 | 1,5 | ✅ |
| L6 | Table des contradictions + planchette (épelage + provenance) + reduced-motion | L2, L5 | 1,5 | ✅ |
| L7 | Procès-verbal : rendu pur, export, impression, vue du greffier | L1, L2 | 1 | ✅ |
| L8 | Accessibilité : clavier, ARIA, `axe-core` en CI, SEA-P-05/10 | L5, L6, L7 | 0,5 | ✅ |
| L9 | Recette, mesures (I2 avec volontaire réel), README, journal | tout | 0,5 | ✅ |
| **Total périmètre minimal** | | | **10** | |
| L10 | Vidéo (script X.16), captures Playwright, textes Devpost, blog | L9 | 1,5 | après gel |

Chemin critique : L1 → L2 → L6/L7. Les cinq collecteurs (L3) et le décor (L5) avancent en parallèle dès L1.
Jalon de contrôle au **21/11** : le parcours complet de la séance de démonstration tourne en local, costume
compris ; sinon on réduit le décor (L5) plutôt que le domaine.

### X.15 Risques et parades

| Risque | Prob. | Impact | Parade | Plan B |
|---|---|---|---|---|
| Le jury voit le costume comme un décor plaqué | Moyenne | Élevé (catégorie perdue) | Table de correspondance X.11, mode greffier, `costume-audit` en CI, phrase d'honnêteté sur la planchette | Vidéo qui ouvre sur la contradiction, pas sur le décor |
| Détection de contradiction trop faible (rien trouvé) ou trop bavarde (faux positifs) | Moyenne | Élevé | Règles de conflit explicites par prédicat, seuils testés sur les fixtures, SEA-P-04 | Mode manuel : l'utilisateur apparie deux affirmations à la main |
| Le format HAR / CSV réel est plus sale que prévu | Élevée | Moyen | Validation Zod, erreurs nommant fichier/ligne/champ, SEA-N-08 | La démo repose sur `changes.json` et `alerts.csv` propres, fournis |
| Mesure I2 (« 4 min au lieu de 45 ») non faite à temps | Moyenne | Moyen | Créneau dédié en L9, volontaire réel | Marquer **À vérifier** et ne citer aucun chiffre |
| Contraste insuffisant sur palette sombre | Faible | Moyen | Chiffres mesurés en amont (X.11), `axe-core` en CI | Repli sur la vue du greffier pour tout texte critique |
| Débordement du bundle (> 250 ko) | Faible | Moyen | Garde CI sur la taille, SVG plutôt qu'images, pas de bibliothèque de graphes lourde | Charger le décor en lazy |
| Plagiat perçu d'incident.io / Blameless | Faible | Moyen | Différence énoncée en une phrase (X.1), hors ligne, sans compte | Insister sur la contradiction comme objet, absent des concurrents |
| Temps : 10 jours-agent sur la fenêtre restante | Moyenne | Élevé | Découpage parallèle L3/L5, jalon 21/11 | Périmètre minimal sans L5 élaboré (table simple) |

### X.16 Démonstration et soumission

**Script vidéo — 0:00 → 2:55, voix seule, aucune musique, aucune marque tierce à l'écran.**
Le plan fort (cinq chaises qui se peuplent, puis la première contradiction) est dans les **20 premières
secondes**. Voix off en anglais (soumission en anglais), minutée mot pour mot.

| Temps | Plan à l'image | Voix off (verbatim, anglais) |
|---|---|---|
| 0:00–0:06 | Le salon sombre, table ronde, cinq chaises vides. Curseur sur *Load the demo incident*. | « Every incident review gets written late, from memory, by whoever talks loudest. » |
| 0:06–0:14 | Les cinq chaises se peuplent une à une ; chaque fantôme nomme sa source. | « Séance calls five ghosts. The Diff. The Watcher. The Clerk. The Supplier. The Witness. Each one speaks from a single source — and each word carries its proof. » |
| 0:14–0:20 | **Plan fort.** Le badge `UNRESOLVED` apparaît entre deux affirmations ; le bouton de clôture se verrouille. | « And when two sources disagree, the séance refuses to close. » |
| 0:20–0:45 | Ouverture du différend en vis-à-vis : le Diff dit « the retry change shipped behind a flag », le Greffier dit « change request CR-118 asked for a flag », chacun avec son tiroir de preuve ouvert. | « This is the whole product. Not a summary — a dispute. Two claims, two artifacts, and you cannot file it away until someone decides, or writes down why it stays open. » |
| 0:45–1:10 | L'utilisateur résout le différend (choisit un côté, écrit une raison) ; le badge passe à `RESOLVED`, la flamme se stabilise. | « Resolved. Or left open, with a reason. Either way, the disagreement is recorded, not smoothed over. » |
| 1:10–1:35 | La planchette épèle la synthèse lettre par lettre ; les tiroirs cités s'illuminent dans l'ordre. | « The summary is spelled out by the board — and every letter lights the source it came from. The board proves nothing. The evidence does. » |
| 1:35–2:00 | Bascule sur la vue du greffier (`v`) : le même contenu en tableau clair, sans décor. | « Remove the costume, and it is exactly the same tool. That is the point: the ghost is a label for a source, the séance is a bounded review, the door that won't close is a quality gate. » |
| 2:00–2:30 | Clôture : le cachet de cire se pose, le procès-verbal s'affiche, chaque affirmation garde son lien ; export `.md`. | « Closing produces the record: timeline, contributing factors, what each ghost claimed, disputes resolved, open questions, actions with owners. Every claim still linked to its artifact. » |
| 2:30–2:55 | Chiffres produits par l'outil : 5 fantômes, 34 affirmations, 3 différends, 2 résolus, procès-verbal en X s. Fondu sur le titre. | « No account. No server. Nothing leaves the machine. Séance — a postmortem where the ghosts of your repository disagree. » |

**Textes Devpost** (anglais, prêts à coller)

- *Titre* : « Séance — a postmortem where the ghosts of your repository disagree ».
- *Accroche* : « Five ghosts. One incident. A review that refuses to close while its sources still disagree. »
- *Ce que ça fait* : paragraphe reprenant X.5 (convocation, cinq sources bornées, affirmations liées à leurs
  preuves, table des contradictions, porte de clôture, planchette de provenance, procès-verbal exportable).
- *Comment c'est construit* : Kiro (7 specs, 3 hooks, 1 skill, 1 agent en lecture seule, PBT), TypeScript strict,
  Vite + React, Zod, fast-check, site statique, zéro réseau.
- *Défis* : la détection de contradiction symétrique et déterministe ; le contraste AA sur palette sombre ; faire
  du costume une peau réversible (vue du greffier).
- *Ce qui est différent* : la phrase de X.1 — hors ligne, sans compte, pour une équipe de trois, et le seul à
  faire de la contradiction l'objet principal.

**Bonus.** Blog (100 gagnants, 2 000 crédits) : billet « Why your postmortem is a séance » illustré par la table
de correspondance. Social Blitz : une capture du plan fort (cinq chaises + `UNRESOLVED`).

**Démo en 30 secondes sans compte** : l'URL ouvre sur la séance de démonstration, bouton *Load the demo
incident* → cinq chaises se peuplent → première contradiction visible → le juge a compris avant la fin de la
première minute.

### X.17 Recette

Vérifications exécutables via `node scripts/recette.mjs` (chaque ligne renvoie `OK`/`KO` et un code de sortie).
Douze points, tous verts attendus.

| # | Commande | Résultat attendu |
|---|---|---|
| 1 | `node scripts/contrast.mjs` | Les six couples texte/fond sombres ≥ 4,5:1 ; les éléments non texte ≥ 3:1 ; aucun `ÉCHEC`. |
| 2 | `node scripts/recette.mjs --check demo-claims` | La séance de démonstration charge 34 affirmations, chacune avec ≥ 1 artéfact (SEA-P-01). |
| 3 | `node scripts/recette.mjs --check no-orphan` | 0 affirmation sans artéfact ; `claim.rejected.no_artifact` journalisé pour toute tentative. |
| 4 | `node scripts/recette.mjs --check disputes` | 3 différends détectés ; `dsp_1` et `dsp_2` résolus, `dsp_3` laissé ouvert avec raison ≥ 12 caractères. |
| 5 | `node scripts/recette.mjs --check gate` | `canClose()` renvoie `false` tant que `dsp_3` est `open` ; `true` une fois `left_open` avec raison. |
| 6 | `node scripts/recette.mjs --check minutes-determinism` | Deux rendus du procès-verbal sur les mêmes entrées produisent des octets identiques (SEA-P-03). |
| 7 | `node scripts/recette.mjs --check symmetry` | `detect([a,b])` et `detect([b,a])` donnent le même différend, `claimA < claimB` (SEA-P-04). |
| 8 | `node scripts/recette.mjs --check share-redaction` | La vue partagée ne contient ni identifiant interne, ni chemin absolu, ni courriel (SEA-P-05). |
| 9 | `node scripts/recette.mjs --check chronology` | Aucun effet avant sa cause ; les inversions plantées lèvent `chronology.inverted` (SEA-P-06). |
| 10 | `npx playwright test e2e/no-network.spec.ts` | 0 requête sortante pendant une séance complète ; `net.bytes.sent === 0` (SEA-P-12). |
| 11 | `npx playwright test e2e/clerk-view.spec.ts` | Bascule `v` : salon → tableau clair, mêmes données (SEA-P-10), focus clavier intact. |
| 12 | `node scripts/costume-audit.mjs` | Tout élément visuel du décor porte une donnée ; seule la poussière est déclarée décorative. |

### X.18 Questions ouvertes (arbitrages qui reviennent au user)

1. **Police décorative.** *Playfair Display* (OFL) convient-elle pour les titres spirites, ou préfères-tu une
   autre famille libre ? (**À vérifier** : licence et rendu à confirmer avant intégration.)
2. **Chiffre d'accroche I2.** Autorises-tu l'usage d'un volontaire réel pour mesurer les « 4 minutes au lieu de
   45 », ou marque-t-on **À vérifier** sans citer de chiffre ?
3. **Portée de la vue du greffier.** Doit-elle être un mode d'affichage réversible (recommandé, prouve que le
   costume est une peau) ou une page séparée ?
4. **Son.** Trois sons discrets derrière un réglage désactivé, ou strictement zéro son y compris en option ?
5. **Nom des fantômes en français.** Le Diff / le Veilleur / le Greffier / le Fournisseur / le Témoin : on garde
   ces noms en seconde langue d'interface, ou anglais seul ?
6. **Périmètre du Fournisseur.** Les avis de sécurité (OSV-like) importés en JSON local suffisent-ils, ou veux-tu
   un importeur de plus (ex. page d'état au format Markdown) ?
7. **Hébergement de secours.** GitHub Pages tient jusqu'au 29/01/2027 ; faut-il prévoir un miroir statique de
   secours (Netlify/Vercel gratuit) au cas où ?
