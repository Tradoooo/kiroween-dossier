# Projet F — Disquette

Cahier des charges pour la soumission **Kiroween 2026**, catégorie **Resurrection**.
Trigramme d'identifiants : `DIS`. Dépôt cible : `disquette`. Rédigé le 11 novembre 2026.
Format des exigences : EARS (§ 0.8 du contexte partagé). Prose en français, code en anglais.

## F. Disquette — la disquette revient comme budget du web

### F.1 Fiche d'identité

| | |
|---|---|
| Nom de travail | **Disquette**. Nom de soumission en anglais : « Disquette — your web app must fit on a disk ». |
| Catégorie | **Resurrection** |
| En une phrase | On ressuscite la disquette 3,5 pouces (1 440 Kio) comme **unité d'expédition** : un site web se compte en disquettes, le disque 1 est le chemin critique du premier rendu, et un plan de défragmentation dit quoi déplacer pour tenir sur moins de disquettes. |
| Public | Le développeur front-end qui livre un bundle trop lourd ; le lead technique d'une petite structure (agence, startup, association) qui arbitre le poids ; secondairement, le responsable produit qui reçoit le rapport. |
| Idée centrale | Le support a disparu, pas la **discipline de la pénurie** : une unité d'expédition dure, qu'on tient dans la main, qui rend le poids des octets concret. Cette unité entre dans la chaîne de build (CLI + garde CI) au lieu de rester un slogan. |
| Ce qui existe déjà | Les budgets de performance Lighthouse (`budget.json`), `size-limit`, `bundlesize` (archivé), bundlephobia, `webpack-bundle-analyzer`, les clubs « 512 KB » et « 1 MB », HTTP Archive (statistiques de crawl), CO2.js et Website Carbon (empreinte carbone). |
| Ce qui est différent | Aucun de ces outils n'utilise une **unité d'expédition avec spanning** (les disques se remplissent, les suivants sont différés), **aucun n'est HAR-first et hors ligne**, et **aucun ne transforme un budget en objet mémorable** qu'on peut coller dans une pull request. |
| Preuve opposable | L'outil mesure lui-même : nombre de disquettes, Kio par disquette, secondes au profil 1,6 Mbit/s, grammes de CO2e. Sur la page d'accueil médiane du web : **1,78 disquette** (2 559 Kio) et **13,1 s** de transfert. |
| Prix visés | Best Resurrection, prix globaux, Best Demo. |
| Charge | Périmètre minimal **8 jours-agent** ; options **+2,5 j** ; texte et vidéo **+1,5 j**. |

### F.2 Ce que la catégorie demande, et la réponse

| Ce que dit le règlement | Réponse de Disquette |
|---|---|
| « Bring your favorite dead technology back to life » | La disquette 3,5" 1,44 Mo, morte comme support (dernières productions de masse au début des années 2000), vivante comme icône « enregistrer ». Elle revient **dans la chaîne de build**, pas dans un musée. |
| « Reimagine obsolete tech with today's innovations » | Trois surfaces modernes : un CLI + une garde CI, une application web statique qui analyse un fichier HAR, un worker edge optionnel. |
| « Solving tomorrow's problems » | Le poids des pages est une facture (bande passante), une émission (carbone) et une exclusion (réseau lent, forfait plafonné). La pénurie est le problème ; la disquette en est l'unité. |
| « Not only nostalgia » | Le format 720 Kio est un **mode brutal** : il transforme « alléger un peu » en « tenir sur une disquette ». Le plan de défragmentation est chiffré en Kio gagnés. |
| Le dépôt doit montrer l'usage de Kiro | Specs, steering de domaine (`disk-myth.md`, `privacy.md`), hooks `disk-budget` / `no-network-guard` / `plan-determinism`, agent personnalisé `defrag-planner` en lecture seule, skill `fit-on-one-disk`, tests par propriétés sur l'allocateur, journal `KIRO_JOURNAL.md`. |
| La technologie doit être vraiment morte | Plus aucun lecteur 3,5" n'est vendu en volume depuis les années 2000 ; le format ne survit que comme icône « enregistrer ». Ce qui ressuscite est la **discipline** du budget, pas le périphérique. |

### F.3 Problème, public et pourquoi maintenant

**Le chiffre, vérifié** (HTTP Archive, *Web Almanac 2025*, chapitre « Page Weight », publié le 15/01/2026, consulté le 11/11/2026) :

| Mesure | Valeur | Ce que ça dit en disquettes |
|---|---|---|
| Page d'accueil médiane, mobile (juillet 2025) | 2 559 Kio | **1,78** → 2 disquettes |
| Page d'accueil médiane, desktop | 2 862 Kio | 1,99 → 2 disquettes |
| Page intérieure médiane, mobile | 1 769 Kio | 1,23 → 2 disquettes |
| JavaScript médian d'une page d'accueil mobile | 632 Kio | 0,44 disquette |
| Images médianes d'une page d'accueil mobile | 911 Kio | 0,63 disquette |
| Croissance annuelle du poids de la page d'accueil | +7,8 % | +44 Kio par an, soit une disquette de plus tous les 3 ans |
| Page d'accueil mobile : juillet 2015 → juillet 2025 | 845 Kio → 2 362 Kio | **+202,8 %** |

**Les conséquences, calculées par l'outil lui-même** (constantes sourcées, voir F.6) :

- **Temps** : au profil mobile de Lighthouse (1,6 Mbit/s descendant, 150 ms de latence, *docs/throttling.md* de Lighthouse, consulté le 11/11/2026), la page médiane mobile représente **13,1 s** de transfert pur. Un site de 12 disquettes (17 694 720 octets) : **88,5 s**.
- **Carbone** : modèle Sustainable Web Design v4 — intensités opérationnelles 0,055 + 0,059 + 0,080 kWh/Go et incorporées 0,012 + 0,013 + 0,081 kWh/Go, intensité du réseau mondial 494 gCO2e/kWh (Ember) — soit **148,2 gCO2e par Go transféré**. Page médiane : **0,39 g** par visite. Site de 12 disquettes : **2,62 g** par visite, donc **262 kg par mois** et **3,15 t par an** à 100 000 visites/mois.
- **Exclusion** : le même rapport note que le poids est « un obstacle physique et cognitif » pour les appareils modestes, et que l'écart de performance croît avec le poids (TBT médian mobile : 1 835 ms ; au 90ᵉ centile : 7,1 s).

**Pourquoi maintenant** : (a) le poids est redevenu un sujet de fond — le chapitre 14 de l'Almanac 2025 s'intitule « Page Weight » et le rapport CrUX montre une corrélation directe entre poids et Core Web Vitals ; (b) le coût de la bande passante est redevenu visible pour les équipes qui paient un CDN ; (c) les garde-fous de build (CI, budgets Lighthouse, `size-limit`) sont maintenant connus — mais ils tombent tous dans la même catégorie que « la page fait 2,5 Mo » : **personne ne sent ce poids**.

**Personas et situations datées**

| Persona | Situation datée | Ce que l'outil lui donne |
|---|---|---|
| **Awa, dev front-end** d'une place de marché mid-market. | 18 novembre 2026, revue de sprint : « le bundle a encore grossi de 180 ko, personne ne sait de quoi ». | `disquette check` en CI : le disque 1 déborde, la pull request est refusée, la sortie dit quel module pose problème. |
| **Marc, lead technique** d'une agence de 12 personnes. | Budget d'hébergement renewé le 1er décembre : la facture de CDN a triplé en un an. | Le rapport Markdown : « 9 disquettes, 4,1 Mo, 22 s en 3G, 0,61 gCO2e/visite ». |
| **Sonia, responsable produit** d'une petite association, non technique. | 20 novembre : elle reçoit une pull request « +600 ko de police et de script tiers ». | Elle comprend « +600 ko = +0,4 disquette = +3 s sur le terrain » sans être développeuse. |

### F.4 Objectifs, non-objectifs, indicateurs

**Objectifs**

- **O1** — Toute construction web peut être exprimée en disquettes ; l'objectif par défaut est de **tenir sur un disque** (1 440 Kio).
- **O2** — Un verdict en moins de 30 secondes, sans compte, sans installation, et **fonctionnant hors ligne** (mode hors ligne total, service worker).
- **O3** — L'allocateur est **déterministe** : même entrée, même graine → même plan, hash compris.
- **O4** — L'outil produit ses propres chiffres : disquettes, Kio, secondes, grammes de CO2e.
- **O5** — La mesure est une **porte** : `disquette check` sort en code 1 quand le disque 1 déborde.
- **O6** — L'outil s'applique à lui-même : l'application web de démonstration doit passer son propre `disquette check` (elle tient sur une disquette).

**Non-objectifs**

- Pas de minifieur, pas de bundler, pas de rewriter de code : Disquette **mesure et propose**, elle ne réécrit pas le code.
- Pas de surveillance de production, pas de télémétrie, pas de compte.
- Pas de certification carbone : une estimation sourcée, avec sa constante visible.
- Pas d'optimum garanti : le plan est « bon, déterministe, stable », pas « optimal ».
- Pas de format exotique supplémentaire : trois formats (720 Kio, 1 440 Kio, 100 Mio).

**Indicateurs (tous mesurés par l'outil, pas déclaratifs)**

| Indicateur | Cible |
|---|---|
| Nombre de disquettes du site médian | 2 (format HD) |
| Octets du disque 1 (chemin critique) | ≤ 1 474 560 |
| Secondes au profil 1,6 Mbit/s | ≤ 4,0 s pour le disque 1 |
| CO2e par visite (SWDM v4) | ≤ 0,25 g |
| Temps de verdict sur un HAR de 5 Mo | < 800 ms sur un portable moyen |
| Requêtes réseau sortantes pendant l'analyse | 0 (vérifié par un test Playwright) |
| Déterminisme | hash du plan identique sur 100 exécutions |
| Poids de l'application de démonstration | ≤ 1 474 560 octets (elle tient sur une disquette) |

### F.5 Le concept en profondeur

**La géométrie, qui est la métaphore.** Une disquette 3,5" haute densité : 2 880 secteurs × 512 octets = **1 474 560 octets** = 1 440 Kio. Double densité : 1 440 secteurs = **737 280 octets** (720 Kio). Un Zip de 100 Mo : 104 857 600 octets. Ces trois nombres ne sont pas des quotas arbitraires : ce sont des **capacités de support**, donc des contraintes dures, ce qui transforme « je voudrais alléger » en « ça rentre ou ça ne rentre pas ».

**Le disque 1 est le chemin critique.** C'est la pièce centrale de la mécanique. Le disque 1 contient **exactement** ce que le navigateur a demandé avant le premier rendu : le document, la CSS critique, le JS d'entrée, la police au-dessus de la pliure, l'image LCP. Ce qui reste (routes paresseuses, chunks différés, images sous la pliure, scripts tiers) part sur les disques 2..n. La conséquence est immédiate et vérifiable : **on ne peut pas « remplir » le disque 1 avec du confort** — chaque octet qui n'est pas sur le chemin critique paie deux fois (transfert + CPU sur un téléphone modeste).

**Le spanning, c'est du code splitting, pas une décoration.** Le découpage multi-disques des années 90 (`INSTALL.EXE` sur disque 1, `DATA.001`, `DATA.002`…) impose une contrainte de **regroupement atomique** : un fichier ne peut pas être coupé en deux, et deux fichiers qui doivent être lus ensemble ne peuvent pas être dispersés sur deux disques. Traduction en code splitting : **une route est un groupe atomique**. Si `/admin` doit être un chunk, ce chunk est entier sur un disque. L'algorithme n'est donc pas un simple bin packing : c'est un bin packing **avec groupes indivisibles** et **une contrainte de priorité** (tout groupe critique doit tenir dans le disque 1).

**L'algorithme, précisément.**

```
1. Normaliser l'entrée en Unités (Unit) — groupes atomiques :
   - mode build  : une unité = une route du manifeste Vite / une chunk de stats webpack
   - mode HAR    : une unité = un groupe d'URL par origine (une origine tierce est toujours
                   une unité séparée : elle se charge indépendamment)
2. Trier les unités : (critique d'abord, puis premierRequestMs croissant, puis taille décroissante,
   puis id croissant) — le tri par id est la clé du déterminisme.
3. Disque 1 : placer les unités critiques dans l'ordre, en s'arrêtant à la capacité du format.
   Si une unité critique ne tient pas → erreur « disk 1 overflow », avec le nom de l'unité.
4. Unités surdimensionnées : SI une unité dépasse la capacité du format, ALORS elle est scindée
   par fichier (ses membres deviennent des unités `file`), la scission est signalée dans le
   verdict (`splitUnits: [...]`), et l'allocation reprend. C'est le seul cas où l'atomicité
   d'une unité est levée — il rend le format 720 Kio utilisable sur un vrai site.
5. Disques 2..n : First-Fit-Decreasing sur les unités restantes, en conservant l'ordre des
   groupes atomiques ; une unité ouvre un nouveau disque si elle ne tient dans aucun
   disque ouvert.
6. Bornes affichées : borne inférieure = ceil(total / capacité) ; l'algorithme peut faire
   mieux ou pire de 1 unité de la borne (il n'est pas optimal, et ne le prétend pas).
```

**Le plan de défragmentation.** Ce n'est pas une liste de conseils : c'est un **plan de découpage de routes**, chiffré. Le plan propose des actions ordonnées, chacune avec ses octets gagnés et le nombre de disquettes avant/après.

| Type d'action | Ce qu'elle dit | Exemple chiffré |
|---|---|---|
| `defer-route` | « Cette route n'est pas sur le chemin critique : charge-la en différé. » | `/admin` (218 Kio) sort du disque 1 |
| `split-route-chunk` | « Ce chunk mélange deux routes : sépare-les. » | `routes-chunk-8f2a.js` (312 Kio) = `/settings` (41 Kio) + `/reports` (271 Kio) |
| `drop-third-party` | « Ce script tiers coûte N Kio et n'est pas critique : retire-le ou charge-le après. » | `analytics-widget.js` (96 Kio) |
| `replace-library` (**optionnel, non vérifié**) | « Cette dépendance pèse N Kio ; un substitut plus léger existe peut-être. » — l'outil ne vérifie pas le substitut | `moment` (231 Kio) → `date-fns/day` (12 Kio) |

**Le compteur qui fond.** L'octet du disque 1 descend en continu pendant que l'on simule le plan : c'est une bougie qui fond. C'est le seul effet non fonctionnel du produit, et il est là pour une raison précise : il rend visible le **gain**, pas l'effort. `prefers-reduced-motion` transforme la bougie en changement de nombre instantané.

**Exemple de verdict (jeu de démonstration intégré, `fixtures/har/kitchen-sink.har`)** :

| Disque | Contenu | Octets | Remplissage |
|---|---|---|---|
| 1 — HD 1 440 Kio | `index.html` 18 Kio, `app-entry.js` 96 Kio, `critical.css` 24 Kio, `Inter-Regular.woff2` 42 Kio, `hero.avif` 210 Kio | 390 Kio | 27 % |
| 2 | `react-dom.js` 132 Kio, `router.js` 22 Kio, `charts.js` 388 Kio, `date-i18n.js` 61 Kio | 603 Kio | 42 % |
| 3 | `routes/admin.js` 218 Kio, `routes/settings.js` 41 Kio, `routes/reports.js` 271 Kio | 530 Kio | 37 % |
| 4 | `analytics-widget.js` 96 Kio, `chat-widget.js` 54 Kio, `locale-fr.js` 118 Kio, 14 polices | 331 Kio | 23 % |
| 5 | 41 images sous la pliure, 2 vidéos courtes | 892 Kio | 62 % |

Verdict affiché : **5 disquettes · 2 746 Kio · 14,1 s en 1,6 Mbit/s · 0,42 gCO2e/visite**. Après application du plan : **3 disquettes**, disque 1 ramené à **318 Kio** (−72 Kio, soit −0,4 s sur le profil 1,6 Mbit/s).

Au format DD 720 Kio, le même site donne **6 disquettes** et signale **2 unités scindées** (le groupe d'images de 892 Kio et le groupe de polices de 118 Kio dépassent la capacité du format) : c'est la seule levée d'atomicité, et elle est affichée comme telle.

**Les trois surfaces, et pourquoi la principale est hors ligne.**

1. **CLI + garde CI** (`disquette check|plan|explain`) : lit un rapport de build (`stats.json` de webpack, le manifeste Vite, ou un dossier `dist/`), alloue les unités aux disquettes, sort un rapport Markdown et un code de sortie. C'est la surface qui **reste en place** après le concours.
2. **Application web statique** (voie principale) : on dépose **un fichier HAR**. Aucun serveur, aucune donnée envoyée, aucun compte. Elle marche en navigation privée et hors ligne. L'option `--url` passe par un petit worker edge, jamais par la voie principale.
3. **L'explorateur de disquettes** : chaque disquette est dessinée (coquille, fenêtre du métal, étiquette) avec son remplissage réel ; chaque module est un fichier sur le disque ; un clic affiche qui l'importe, ce qu'il coûte, et son appartenance au chemin critique ; la vue « défragmenteur » superpose l'avant/après.

### F.6 Formats et données

**Schéma des formats de disquette** (`packages/core/src/formats.ts`)

```ts
import { z } from "zod";

export const DiskFormatId = z.enum(["dd", "hd", "zip"]);

export const DiskFormat = z.object({
  id: DiskFormatId,
  label: z.string(),          // "3.5\" HD 1.44 MB" | "3.5\" DD 720 KB" | "Zip 100 MB"
  capacityBytes: z.number().int().positive(),
  sectors: z.number().int().positive(),
  sectorBytes: z.literal(512),
  default: z.boolean(),
});

export const FORMATS: Record<DiskFormatId, DiskFormat> = {
  dd:  { id: "dd",  label: "3.5\" DD 720 KB",  capacityBytes:  737_280, sectors: 1440, sectorBytes: 512, default: false },
  hd:  { id: "hd",  label: "3.5\" HD 1.44 MB", capacityBytes: 1_474_560, sectors: 2880, sectorBytes: 512, default: true  },
  zip: { id: "zip", label: "Zip 100 MB",        capacityBytes: 104_857_600, sectors: 204_800, sectorBytes: 512, default: false },
};
```

**Modèle normalisé** (`packages/core/src/model.ts`)

```ts
export type UnitKind = "route" | "origin" | "file";

export interface Module {
  id: string;                 // "assets/app-entry-8f2a.js" — identifiant stable, trié lexicographiquement
  bytes: number;              // octets sur disque
  transferBytes?: number;     // octets transférés (gzip/brotli) si connus
  kind: "html" | "css" | "js" | "font" | "image" | "media" | "other";
  url?: string;               // présent en mode HAR
  requestStartMs?: number;    // début de la requête, relatif au début de la navigation
}

export interface Unit {
  id: string;                 // "route:/admin" | "origin:cdn.example.com" | "file:app.js"
  kind: UnitKind;
  bytes: number;              // somme des modules
  members: Module[];
  critical: boolean;          // demandé avant le premier rendu
  firstRequestMs?: number;
}

export interface Disk {
  index: number;              // 1..n
  units: Unit[];
  usedBytes: number;
  freeBytes: number;
  fillRatio: number;          // 0..1
}

export interface Verdict {
  formatId: DiskFormatId;
  disks: Disk[];
  diskCount: number;
  lowerBoundDisks: number;    // ceil(totalBytes / capacity)
  siteBytes: number;
  criticalBytes: number;      // octets du disque 1
  firstRenderSeconds: number; // profil réseau choisi
  carbonGrams: number;        // SWDM v4
  planHash: string;           // sha256 du plan, pour le déterminisme
}

export interface DefragAction {
  id: string;
  kind: "defer-route" | "split-route-chunk" | "drop-third-party" | "replace-library";
  target: string;             // id d'unité ou de module
  bytesMoved: number;
  bytesSavedOnDisk1: number;
  disksBefore: number;
  disksAfter: number;
  verified: boolean;          // false pour "replace-library"
  note: string;               // une phrase, en anglais dans l'UI
}
```

**Entrée HAR** — sous-ensemble utile de HAR 1.2, validé par Zod (`packages/har/src/schema.ts`) :

```json
{
  "log": {
    "version": "1.2",
    "creator": { "name": "Chrome DevTools", "version": "131.0" },
    "pages": [
      { "id": "page_1", "title": "https://example.test/",
        "pageTimings": { "onContentLoad": 812, "onLoad": 2480, "_startRender": 640 } }
    ],
    "entries": [
      { "pageref": "page_1", "startedDateTime": "2026-11-11T10:00:00.000Z",
        "request": { "method": "GET", "url": "https://example.test/assets/app-entry.js",
                     "headers": [{ "name": "Cookie", "value": "session=REDACTED" }] },
        "response": { "status": 200, "bodySize": 98304, "headersSize": 320,
                      "content": { "size": 98304, "mimeType": "application/javascript" } } }
    ]
  }
}
```

Règles d'ingestion :

- Le premier rendu est lu dans `pages[].pageTimings._startRender` (export Chrome). Repli : `onContentLoad`. Si les deux manquent, toutes les entrées sont « critiques » et le verdict le signale (`criticalPath: "unknown"`).
- **Assainissement obligatoire** à l'ingestion : `request.headers` de type `cookie`, `authorization`, `set-cookie`, `x-api-key` et le champ `postData` sont supprimés. L'UI affiche « 3 credentials removed ».
- Le poids retenu est `response.bodySize` s'il est > 0, sinon `response.content.size`, sinon `response._transferSize` (extension Chrome).
- Les entrées dont le `status` est ≥ 400 ou le `mimeType` vaut `text/html` pour une navigation sont ignorées pour le poids mais comptées dans les métadonnées.
- Plafond : 100 Mo par fichier, lecture en flux, refus au-delà avec un message qui dit quoi faire.

**Entrée build** (`packages/build/src/normalize.ts`) : accepte `stats.json` (webpack), le manifeste Vite (`dist/.vite/manifest.json`) ou un dossier `dist/` (dans ce dernier cas, un graphe d'imports est reconstruit depuis les sources de chunks, et les routes sont déduites des clés `src/routes/**`). Une unité = une route ; le chunk vendor est une unité `file` rattachée au disque 1 si critique.

**Constantes de mesure** (`packages/core/src/constants.ts`) — toutes sourcées et affichables dans l'UI :

```ts
export const NETWORK_PROFILES = {
  "lighthouse-mobile-slow4g": { downBps: 200_000, upBps: 93_750, rttMs: 150 }, // 1,6 Mbit/s
  "webpagetest-3g-fast":       { downBps: 200_000, upBps: 93_750, rttMs: 150 },
  "wifi-fast":                 { downBps: 2_500_000, upBps: 1_250_000, rttMs: 10 },
} as const;

export const CO2 = {
  model: "SWDM v4",
  operationalKwhPerGb: { dataCenter: 0.055, network: 0.059, userDevice: 0.080 },
  embodiedKwhPerGb:     { dataCenter: 0.012, network: 0.013, userDevice: 0.081 },
  gridIntensityGPerKwh: 494,   // Ember, moyenne mondiale
  get gramsPerGb() { /* 0,300 kWh/Go × 494 g/kWh = 148,2 gCO2e/Go */ },
};
```

**Sources de données publiques nommées**

| Source | Usage | Licence |
|---|---|---|
| HTTP Archive — *Web Almanac 2025*, chap. 14 « Page Weight » | chiffres de référence du README et de la vidéo | Apache 2.0 |
| HTTP Archive — rapports `state-of-the-web`, `page-weight` | comparaison de formats | Apache 2.0 |
| Sustainable Web Design Model v4 | facteur CO2e (148,2 g/Go) | méthode ouverte — **licence exacte À vérifier** |
| Lighthouse `docs/throttling.md` | profil réseau 1,6 Mbit/s / 150 ms | Apache 2.0 |
| WebPageTest `connectivity.ini.sample` | profil « Mobile 3G – Fast » (profil identique) | Apache 2.0 |
| Ember — Data Explorer | intensité carbone 494 gCO2e/kWh | CC BY 4.0 — **à vérifier** |
| Chrome DevTools (export HAR 1.2) | format d'entrée | — |

**Fixtures embarqués** : `fixtures/har/kitchen-sink.har`, `fixtures/har/heavy-site.har` (hôte masqué en `site-01.test`), `fixtures/har/with-credentials.har`, `fixtures/har/malformed.har`, `fixtures/build/webpack-stats.json`. Aucun HAR tiers n'est commité avec les octets d'actifs d'un tiers : seules les métadonnées et les tailles, avec des hôtes réécrits.

### F.7 Exigences fonctionnelles

| ID | Priorité | Exigence (EARS) |
|---|---|---|
| DIS-F-01 | I | QUAND un fichier HAR valide est déposé, ALORS l'application affiche un verdict (nombre de disquettes, Kio par disquette, secondes, grammes de CO2e) en moins de 3 s, sans aucune requête réseau sortante. |
| DIS-F-02 | I | QUAND le HAR contient `pages[].pageTimings._startRender`, ALORS le disque 1 contient exactement les entrées dont `startedDateTime` précède ce marqueur. |
| DIS-F-03 | I | SI le fichier déposé n'est pas un HAR 1.2 conforme au schéma Zod, ALORS l'application affiche l'erreur nommant le chemin du champ fautif et propose le HAR de démonstration. |
| DIS-F-04 | I | QUAND le format choisi est `hd`, ALORS aucune disquette du plan ne dépasse 1 474 560 octets et aucune unité n'est coupée. |
| DIS-F-05 | I | QUAND le format ou la graine changent, ALORS le plan est recalculé de façon déterministe et le `planHash` ne dépend que de l'entrée, du format et de la graine. |
| DIS-F-06 | I | TANT QUE l'analyse d'un HAR est en cours, ALORS l'interface reste interactive : l'analyse s'exécute dans un Web Worker et l'interface affiche une progression en octets traités. |
| DIS-F-07 | I | QUAND un module est sélectionné dans l'explorateur, ALORS le panneau affiche son chemin, son poids brut et transféré, son appartenance au chemin critique, et la liste des modules qui l'importent. |
| DIS-F-08 | I | OÙ la vue défragmenteur est active, ALORS l'application propose un plan ordonné d'actions, chacune chiffrée en octets gagnés et en disquettes gagnées. |
| DIS-F-09 | I | SI aucune action du plan ne réduit le nombre de disquettes, ALORS l'application le dit explicitement et affiche le gain en Kio du disque 1. |
| DIS-F-10 | I | QUAND un rapport est exporté, ALORS le fichier produit porte le format, le nombre de disquettes, l'horodatage et le `planHash`, et ne contient aucune donnée personnelle. |
| DIS-F-11 | S | QUAND un rapport de build (`stats.json`, manifeste Vite ou dossier `dist/`) est fourni, ALORS la CLI alloue les routes aux disquettes et écrit `artifacts/disquette-report.md`. |
| DIS-F-12 | I | QUAND `disquette check` s'exécute, ALORS il sort avec le code 1 si le chemin critique dépasse le format, et le message nomme l'unité fautive. |
| DIS-F-13 | S | OÙ `disquette.config.json` existe à la racine du dépôt, ALORS la CLI lit le format, la graine, le profil réseau et le seuil de budget, et les valeurs par défaut s'appliquent sinon. |
| DIS-F-14 | O | QUAND l'option `--url` est fournie, ALORS l'analyse passe par le worker edge, qui ne renvoie que des tailles agrégées et aucun contenu de page. |
| DIS-F-15 | I | TANT QUE l'onglet de l'application est ouvert, ALORS aucun octet du HAR déposé ne quitte le navigateur ; un test Playwright échoue si une requête sort vers un autre origine. |
| DIS-F-16 | S | QUAND le plan de défragmentation est simulé, ALORS l'application affiche l'avant/après côte à côte (disques et Kio du disque 1) et la bougie fond en temps réel. |
| DIS-F-17 | I | SI le graphe d'imports contient un cycle, ALORS l'explorateur l'affiche avec le cycle signalé et ne boucle pas. |
| DIS-F-18 | S | QUAND le format `zip` est choisi, ALORS l'application affiche le badge « Zip 100 MB » et n'applique pas la contrainte de 1 440 Kio. |
| DIS-F-19 | S | QUAND l'utilisateur change de profil réseau, ALORS les secondes du disque 1 et du site sont recalculées immédiatement et la constante du profil est rappelée sous le chiffre. |
| DIS-F-20 | I | QUAND un HAR contient des ressources d'origines tierces, ALORS elles sont comptées dans le poids du site, signalées comme tierces, et le plan propose de les différer ou de les retirer. |
| DIS-F-21 | I | QUAND le même HAR est analysé deux fois dans le même navigateur, ALORS le verdict et le `planHash` sont identiques. |
| DIS-F-22 | O | OÙ le mode démonstration est activé, ALORS l'application charge le HAR embarqué et joue le verdict complet sans aucune action de l'utilisateur. |
| DIS-F-23 | S | QUAND l'application est hors ligne (service worker actif), ALORS le dépôt de HAR, le verdict et l'explorateur fonctionnent intégralement. |
| DIS-F-24 | X | Le système NE DOIT PAS modifier, minifier ou réécrire le code du projet analysé. |
| DIS-F-25 | X | Le système NE DOIT PAS envoyer de données à un modèle de langage ; aucune fonction n'est conditionnée à un appel de modèle. |
| DIS-F-26 | S | SI une unité dépasse la capacité du format choisi, ALORS l'allocateur la scinde par fichier, poursuit l'allocation et liste les unités scindées dans le verdict (`splitUnits`). |

### F.8 Exigences non fonctionnelles

| ID | Priorité | Exigence |
|---|---|---|
| DIS-N-01 | I | Verdict sur un HAR de 5 Mo en moins de 800 ms sur un portable moyen ; budget CI : 1 200 ms. |
| DIS-N-02 | I | Le shell de l'application pèse au plus 200 Kio compressés ; le lecteur HAR et l'allocateur sont chargés à la demande (+150 Kio compressés) et l'ensemble du build de démonstration passe son propre `disquette check` (≤ 1 474 560 octets). |
| DIS-N-03 | I | Fonctionnement hors ligne : service worker qui précharge le shell et les fixtures ; la démonstration complète est jouable avec le réseau coupé. |
| DIS-N-04 | I | Accessibilité AA : contraste 4,5:1 minimum, navigation clavier complète dans l'explorateur de disquettes, information jamais portée par la seule couleur (le remplissage est aussi une trame de hachures), `prefers-reduced-motion` respecté. |
| DIS-N-05 | I | Vie privée : aucune télémétrie, aucun envoi, aucun cookie ; le HAR n'est jamais écrit sur disque par l'application (pas d'IndexedDB, pas de `localStorage`). |
| DIS-N-06 | I | Déterminisme : `planHash` stable sur 100 exécutions, seeds de fast-check consignées dans le rapport de test. |
| DIS-N-07 | S | Robustesse : un HAR de 50 000 entrées est analysé en moins de 5 s, avec moins de 400 Mo de mémoire ; le message d'erreur nomme le champ en cause. |
| DIS-N-08 | I | Règle de la maison : moins de 500 lignes par fichier, moins de 50 lignes par fonction ; garde automatique `loc-budget` en CI, sans exception. |
| DIS-N-09 | I | Dépendances runtime : `zod` uniquement pour le cœur et le HAR ; la CLI s'installe en moins de 10 s. Pas de copyleft fort (AGPL/GPLv3 écartés). |
| DIS-N-10 | S | Interface en anglais (soumission), français en seconde langue ; toutes les chaînes passent par un catalogue, aucune chaîne en dur dans les composants. |
| DIS-N-11 | I | Aucun son par défaut : le seul son imaginable (le claquement du volet) est derrière un réglage désactivé, et le respect de `prefers-reduced-motion` le neutralise. |
| DIS-N-12 | I | CI : `timeout-minutes: 5`, `concurrency`, `fetch-depth: 1` ; E2E et bancs longs hors PR. |
| DIS-N-13 | S | Licence MIT dès le premier commit, tableau des dépendances et de leurs licences dans le README, `.kiro/` jamais ignoré. |

### F.9 Architecture technique

**Arborescence du dépôt**

```
disquette/
├── .kiro/
│   ├── steering/          product.md · tech.md · structure.md · testing.md
│   │                      disk-myth.md (fileMatch packages/core) · privacy.md (fileMatch packages/har)
│   ├── specs/
│   │   ├── core-allocator/     requirements.md · design.md · tasks.md
│   │   ├── har-reader/         requirements.md · design.md · tasks.md
│   │   ├── disk-explorer/      requirements.md · design.md · tasks.md
│   │   ├── defrag-planner/     requirements.md · design.md · tasks.md
│   │   └── cli-guard/          requirements.md · design.md · tasks.md
│   ├── hooks/             disk-budget.json · loc-budget.json · no-network-guard.json · plan-determinism.json
│   ├── agents/            defrag-planner.md (lecture seule) · reviewer.md
│   ├── skills/            fit-on-one-disk/SKILL.md · har-scrub/SKILL.md
│   └── settings/          mcp.json
├── packages/
│   ├── core/              types, formats, Zod, allocateur, mesures, plan de défrag
│   ├── har/               lecture HAR, assainissement, extraction du premier rendu
│   ├── build/             normalisation stats.json / manifeste Vite / dist/
│   ├── cli/               commandes check · plan · explain · report
│   └── ui/               composants React : verdict, explorateur, défrag, exports
├── apps/
│   ├── web/               application statique (Vite + React) — la voie principale
│   └── worker/            worker edge optionnel pour l'analyse par URL
├── fixtures/har/          HAR de démonstration (hôtes réécrits)
├── fixtures/build/        stats.json d'exemple
├── scripts/recette.mjs    recette exécutable
├── docs/                  METHOD.md · FORMATS.md · CARBON.md · CHANGELOG.md
└── KIRO_JOURNAL.md
```

**Budgets de lignes par paquet** (source seulement, tests exclus ; plafond maison : 500 lignes par fichier, 50 par fonction)

| Paquet | Budget | Contenu | Fichiers |
|---|---|---|---|
| `packages/core` | 900 l. | `model.ts` 140, `formats.ts` 70, `allocate.ts` 180, `metrics.ts` 130, `defrag.ts` 220, `constants.ts` 60, `planHash.ts` 60, `index.ts` 40 | 8 |
| `packages/har` | 430 l. | `schema.ts` 120, `parse.ts` 150, `scrub.ts` 90, `criticalPath.ts` 70 | 4 |
| `packages/build` | 380 l. | `webpackStats.ts` 140, `viteManifest.ts` 110, `distScan.ts` 130 | 3 |
| `packages/cli` | 320 l. | `check.ts` 90, `plan.ts` 80, `explain.ts` 60, `report.ts` 60, `cli.ts` 30 | 5 |
| `packages/ui` | 760 l. | `DiskShell.tsx` 140, `DiskExplorer.tsx` 190, `ModuleInspector.tsx` 120, `DefragPlanner.tsx` 160, `VerdictCard.tsx` 90, `DropZone.tsx` 60 | 6 |
| `apps/web` | 380 l. | `main.tsx` 60, `App.tsx` 120, `workerBridge.ts` 90, `sw.ts` 60, `i18n.ts` 50 | 5 |
| `apps/worker` | 120 l. | `index.ts` 120 | 1 |
| **Total source** | **3 290 l.** | fichiers ≤ 500 l., fonctions ≤ 50 l. | 32 |

Les tests (Vitest + fast-check + Playwright) sont hors de ce budget, comme dans les autres projets de la maison.

**Flux de données**

```
HAR déposé ─┐
             ├─▶ scrub (credentials retirés) ─▶ Module[] ─▶ Unités ─▶ allocate ─▶ Disk[] ─▶ Verdict
stats.json ─┤                                  ▲                                    │
manifest ───┘                                  │                                    └─▶ defrag ─▶ DefragAction[]
dist/ ──────┘
                                                 │
config (format, graine, profil réseau, budget) ┘
```

**Ce qui tourne où**

| Élément | Exécution | Réseau |
|---|---|---|
| `packages/core`, `packages/har`, `packages/build` | Node LTS (CLI) et Web Worker (navigateur) — même code, même résultat | aucun |
| `packages/cli` | Node LTS, binaire `disquette` publié dans le dépôt | aucun |
| `apps/web` | navigateur, statique (GitHub Pages), service worker | aucun hors iframe d'options |
| `apps/worker` | edge (Cloudflare Workers ou équivalent), **optionnel** | sortante, bornée : 10 s, 5 Mo, schémas http/https, plages IP privées bloquées |

**Contrat CLI**

```bash
disquette check --har fixtures/har/kitchen-sink.har --format hd --network lighthouse-mobile-slow4g
# exit 0 | 1 (budget dépassé) ; écrit artifacts/disquette-report.md et stdout JSON

disquette plan --stats fixtures/build/webpack-stats.json --format hd --out artifacts/plan.json
disquette explain --har fixtures/har/heavy-site.har --module assets/charts.js   # qui l'importe, coût
disquette report --har <fichier> --format md --out report.md
```

**Configuration** (`disquette.config.json`)

```json
{
  "format": "hd",
  "seed": 20261111,
  "networkProfile": "lighthouse-mobile-slow4g",
  "budget": { "disk1Bytes": 1474560, "maxDisks": 12 },
  "carbon": { "model": "swdm-v4", "gridIntensityGPerKwh": 494 },
  "criticalPath": { "source": "auto", "fallback": "onContentLoad" }
}
```

### F.10 Sécurité et modèle de menace

| Menace | Surface | Parade |
|---|---|---|
| Un HAR contient des identifiants (`Cookie`, `Authorization`, `postData`) | ingestion | Assainissement obligatoire à la lecture (`scrub.ts`), avant toute visualisation ; l'UI annonce le nombre d'éléments retirés ; rien n'est persisté (DIS-N-05). |
| Un HAR contient une URL interne ou un secret dans le chemin | ingestion | Le mode démonstration masque l'hôte (`site-01.test`) ; le rapport exporté n'inclut les URL que sur option explicite `--include-urls`. |
| XSS via un nom de fichier ou un en-tête | interface | React échappe tout ; aucun `dangerouslySetInnerHTML` ; un test vérifie l'absence de `innerHTML` dans `packages/ui`. |
| Fichier immense (zip-bomb en `.har.gz`) | ingestion | Plafond 100 Mo, refus avant analyse complète, lecture en flux. |
| Écriture hors du dépôt par la CLI | CLI | Le chemin de sortie est résolu et vérifié comme descendant du répertoire de travail ; pas de `..` accepté. |
| SSRF par le worker d'URL | worker | Schémas http/https seulement, résolution DNS bloquée sur les plages privées, 10 s de délai, 5 Mo de réponse, aucun en-tête ni cookie transmis, seule la taille agrégée est retournée. |
| Fuite par la dépendance de build | CI | `pnpm-lock.yaml` commité, versions épinglées, licences auditées (MIT/Apache/BSD uniquement). |
| Le plan de défrag appliqué automatiquement casse le site | CLI | Le plan est **un fichier**, jamais une modification du code ; `disquette plan` n'écrit que dans `--out`. |
| Dérive du déterminisme (Map/Set, horloge) | cœur | Interdiction des `Date.now()` et des itérations non triées dans `core` ; garde `plan-determinism` qui rejoue 100 fois et compare les hashes. |

### F.11 Interface et direction artistique

**Le principe** : l'objet physique porte la métaphore, mais l'interface reste un outil de mesure. Le décor est une **coquille de disquette 3,5"** en plastique nervuré bleu marine, avec la fenêtre du métal argenté, l'étiquette papier crème et la languette. Rien d'autre. Pas de manoir, pas de crânes : la catégorie est *Resurrection*, pas *Costume Contest*.

**Écrans**

1. **Dépôt** (`DropZone`) : la coquille dessinée, la mention « Drop a HAR file (Chrome DevTools → Network → Export HAR) », un bouton « Use the demo HAR » et un lien « Install the CLI ».
2. **Verdict** (`VerdictCard`) : l'étiquette de la disquette 1, manuscrite, portant le verdict : « 5 disks · 2 746 KiB · 14.1 s on 1.6 Mbps · 0.42 g CO2e / visit ». C'est l'écran que le juge photographie.
3. **Explorateur** (`DiskExplorer`) : la rangée de disquettes, chacune dessinée avec son remplissage réel ; au clic sur un module, le panneau de droite (`ModuleInspector`) donne qui l'importe et ce qu'il coûte.
4. **Défragmenteur** (`DefragPlanner`) : la vue « avant / après », la bougie qui fond, et la liste des actions chiffrées.
5. **Rapport** : export Markdown, avec les constantes (format, profil réseau, facteur CO2e) imprimées dans le document.

**États vides, erreurs, chargements**

| État | Traitement |
|---|---|
| Aucun HAR déposé | La coquille vide avec une consigne ; le bouton de démonstration est visible (pas de page blanche). |
| HAR invalide | Message nommant le champ fautif, extrait du JSON, et proposition de déposer un autre fichier. |
| HAR sans métadonnées de premier rendu | Bandeau « critical path unknown — all entries counted as critical », le verdict est affiché quand même, marqué. |
| Analyse en cours | Progression en octets traités (le HAR est lu en flux) ; l'interface reste cliquable. |
| Hors ligne | Bandeau discret « offline mode — everything still works ». |
| Plan sans gain | « No route split saves a disk. Here is what it saves on disk 1: −72 KiB (−1.2 s). » |

**Palette et typographie**

| Rôle | Valeur | Usage |
|---|---|---|
| Coquille | `#1B3A6B` | fond des cartes, 4,5:1 minimum sur texte clair |
| Volet métallique | `#C9CDD3` | éléments inactifs, traits de la coque |
| Étiquette | `#F2E9D0` | la surface du verdict, encre `#1A1A1A` (13:1) |
| LED verte / rouge | `#2E7D32` / `#B3261E` | état de la garde, **jamais seule** : toujours doublée par un texte et une forme |
| Trame de hachures | 2 densités | le remplissage d'une disquette est lisible en niveaux de gris |

Typographie : pile système, chiffres tabulaires (`font-variant-numeric: tabular-nums`) — aucune police tierce, donc aucune marque à l'écran et aucune licence de police à vérifier. Les nombres sont toujours accompagnés de leur unité (Kio, s, g) et leur constante est rappelée au survol.

**Mouvement** : le compteur d'octets du disque 1 descend en `requestAnimationFrame` pendant la simulation du plan (400 ms). `prefers-reduced-motion: reduce` → changement de nombre instantané, sans animation. Aucun son.

**Pourquoi chaque élément améliore la fonction**

| Élément | Ce qu'il améliore |
|---|---|
| La rangée de disquettes | Rend le nombre abstrait (« 2,5 Mo ») physique et comparable d'un site à l'autre : on lit « 5 disques » comme on lit « 12 pages ». |
| Le disque 1 distinct | Matérialise le chemin critique : « tout ce qui n'est pas sur le disque 1 ne coûte rien au premier écran ». |
| La trame de hachures | Le remplissage reste lisible en niveaux de gris, pour les daltoniens et pour l'impression. |
| L'étiquette manuscrite | C'est un objet collable dans une pull request ou une revue de sprint ; le format devient une unité de discussion. |
| La bougie qui fond | Rend le **gain** visible sans feedback de progression fastidieux ; elle s'arrête net en mouvement réduit. |

### F.12 Propriétés à tester

| ID | Invariant exact | Générateur fast-check |
|---|---|---|
| DIS-P-01 | **Conservation** : la somme des octets des modules égale la somme des octets des unités, et la somme des `usedBytes` des disquettes égale le total du site (écart nul, octets entiers). | `arbHar(n)` → modules dérivés des entrées HAR avec tailles entières. |
| DIS-P-02 | **Capacité** : pour tout format, `disk.usedBytes ≤ format.capacityBytes`. | `arbFormat()` × `arbUnits(n)`. |
| DIS-P-03 | **Atomicité** : une unité n'apparaît jamais dans deux disquettes, et ses membres sont tous dans la même — sauf si elle figure dans `splitUnits` (cas où elle dépasse la capacité du format). | `arbUnits(n)` avec groupes de taille 1..200, dont certains surdimensionnés. |
| DIS-P-04 | **Déterminisme** : à entrée, format et graine identiques, `planHash` identique sur 100 tirages. | `arbHar(n)` avec graine fixe ; 100 exécutions. |
| DIS-P-05 | **Stabilité** : ajouter un module de taille ≤ 1 % du total ne change le nombre de disquettes que de 0 ou 1, et ne déplace aucun module critique hors du disque 1. | `arbHar(n)` + insertion d'un module minuscule à position aléatoire. |
| DIS-P-06 | **Chemin critique** : l'ensemble des modules du disque 1 est exactement l'ensemble des modules dont `requestStartMs ≤ firstRenderMs`. | `arbHar(n)` avec `firstRenderMs` tiré dans la plage des requêtes. |
| DIS-P-07 | **Borne** : `diskCount ≥ ceil(siteBytes / capacity)` et `diskCount ≤ lowerBound + nombre d'unités indivisibles non scindables`. | `arbUnits(n)` avec quelques unités surdimensionnées. |
| DIS-P-08 | **Linéarité carbone** : `carbonGrams = octets × 148,2 / 1e9`, à 1e-9 près ; un octet de plus augmente le résultat de 1,482e-7 g. | `arbBytes()`. |
| DIS-P-09 | **Idempotence du plan** : appliquer deux fois le plan de défragmentation donne le même résultat qu'une fois. | `arbPlan()` (arbitraire borné). |
| DIS-P-10 | **Absence d'identifiants** : après ingestion, le modèle normalisé ne contient aucune valeur de `cookie`, `authorization` ni `postData`. | `arbHar(n)` enrichi d'en-têtes sensibles. |
| DIS-P-11 | **Aller-retour HAR** : `parse → normalize → re-sérialiser` conserve le nombre d'entrées et le total d'octets. | `arbHar(n)`. |
| DIS-P-12 | **Scission minimale** : une unité n'est scindée que si `unit.bytes > capacity` ; la scission conserve la somme des octets de ses membres et n'augmente jamais le nombre de disquettes au-delà de la borne + 1. | `arbUnits(n)` × `arbFormat()` avec capacités de 720 Kio à 100 Mio. |

Chaque propriété est rattachée à un critère d'acceptation de `core-allocator` ou `har-reader`, et le journal note les contre-exemples trouvés (au moins un contre-exemple est attendu sur DIS-P-05 : l'algorithme FFD naïf n'est pas stable, et le correctif — réordonner par `firstRequestMs` avant le tri par taille — doit être raconté dans `KIRO_JOURNAL.md`).

### F.13 Stratégie Kiro

**Specs**

| Spec | Parcours | Contenu | Sortie attendue |
|---|---|---|---|
| `core-allocator` | Exigences d'abord | DIS-F-04, 05, 07, 08, 09 ; DIS-N-06, 08 ; DIS-P-01..08 | `packages/core` + ses propriétés |
| `har-reader` | Exigences d'abord | DIS-F-01, 02, 03, 17, 20, 23 ; DIS-N-01, 05, 07 ; DIS-P-06, 10, 11 | `packages/har` |
| `disk-explorer` | Conception d'abord | DIS-F-07, 09, 16, 18, 19 ; DIS-N-04, 10 | `packages/ui` + `apps/web` |
| `defrag-planner` | Conception d'abord | DIS-F-08, 09, 16 ; DIS-P-09 | `packages/core/defrag.ts` |
| `cli-guard` | Quick Spec | DIS-F-11, 12, 13 ; DIS-N-09, 12 | `packages/cli` + hook `disk-budget` |
| `app-shell` | Quick Spec | DIS-F-01, 22 ; DIS-N-02, 03 | `apps/web` |

**Steering**

| Fichier | Inclusion | Contenu |
|---|---|---|
| `product.md`, `tech.md`, `structure.md`, `testing.md` | toujours | fondations, dont les budgets de lignes et l'interdiction d'envoi réseau |
| `disk-myth.md` | `fileMatch` sur `packages/core/**` | les trois formats, la géométrie (2 880 × 512), le vocabulaire disque/unité/module, et l'interdiction de parler d'« optimisation » sans nombre |
| `privacy.md` | `fileMatch` sur `packages/har/**`, `apps/web/**` | l'assainissement des identifiants est une obligation, pas une option ; aucune requête sortante sur la voie principale |
| `har-scrub.md` | manuelle | procédure pas à pas pour publier un HAR sans fuite |

**Hooks** (tous en action **commande** : ils ne consomment pas de crédits)

| Hook | Déclencheur | Action | Preuve attendue |
|---|---|---|---|
| `disk-budget` | après `build` | lance `disquette check` sur `dist/` ; échec si le disque 1 déborde | journal d'un refus de PR |
| `loc-budget` | enregistrement dans `packages/**` | compte les lignes ; au-delà de 500, exige une découpe | déclencheurs comptés dans `KIRO_JOURNAL.md` |
| `no-network-guard` | enregistrement dans `apps/web/**` | refuse `fetch`, `XMLHttpRequest`, `axios`, `WebSocket` hors `apps/worker` | refus consigné |
| `plan-determinism` | fin de tâche de spec | rejoue l'allocateur 100 fois et compare les `planHash` | graine consignée |

**Agents personnalisés**

| Agent | Rôle | Permissions |
|---|---|---|
| `defrag-planner` | analyse un rapport de build et rédige un plan de défragmentation dans `.kiro/plans/<date>.md`, sans toucher au code | lecture seule sur `packages/**` ; écriture limitée à `.kiro/plans/` |
| `reviewer` | relecture des exigences EARS et des propriétés avant merge | lecture seule |

**Skills**

| Skill | Quand | Contenu |
|---|---|---|
| `fit-on-one-disk` | quand une route déborde du disque 1 | la procédure : identifier l'unité critique fautive, proposer `defer-route` / `split-route-chunk`, rejouer `disquette check` |
| `har-scrub` | avant de commiter un HAR | la procédure d'assainissement et de masquage d'hôte |

**MCP et autres surfaces**

- **MCP** : un serveur de documentation (pour citer la doc Kiro et la doc Lighthouse dans le journal) et un serveur de navigateur (pour les traces Playwright) sont déclarés dans `.kiro/settings/mcp.json`. Le journal note ce qu'ils ont permis : inspecter une trace de throttling sans deviner.
- **CLI sans interface** : relecture automatique du plan de défragmentation dans la CI (nécessite une clé d'API → optionnel, pas dans le périmètre minimal).
- **Exécution parallèle des tâches** : `core-allocator` et `har-reader` sont lancées en parallèle (aucune dépendance), puis `disk-explorer` et `defrag-planner` ensemble.
- **Crew** : non utilisé dans le périmètre minimal (une seule tâche longue).
- **Expérience « spec contre vibe coding »** : l'allocateur est fait deux fois — une version écrite à la main en 40 minutes, une version pilotée par spec avec propriétés. Le journal consigne la durée, le nombre d'allers-retours, et le contre-exemple trouvé par fast-check (DIS-P-05) qui n'apparaissait pas dans les tests unitaires.

### F.14 Plan de réalisation

| Lot | Contenu | Jours-agent | Dépendances | Fusionné avant le gel vidéo (28 nov.) |
|---|---|---|---|---|
| F1 | `packages/core` : modèle, formats, allocateur, mesures | 2,0 | — | oui (12 nov.) |
| F2 | `packages/har` : schéma Zod, lecture, assainissement, chemin critique | 1,5 | F1 | oui (14 nov.) |
| F3 | `packages/build` : stats webpack, manifeste Vite, scan `dist/` | 1,0 | F1 | oui (16 nov.) |
| F4 | `packages/cli` + hook `disk-budget` + garde `loc-budget` | 1,0 | F1, F3 | oui (19 nov.) |
| F5 | `apps/web` : coquille, dépôt, verdict, exploration | 2,5 | F1, F2 | oui (23 nov.) |
| F6 | `defrag-planner` + vue défrag + bougie | 1,5 | F1, F5 | oui (25 nov.) |
| F7 | Propriétés fast-check, fixtures, tests bout en bout, hors ligne | 1,0 | F1..F6 | oui (26 nov.) |
| F8 | Dogfooding (l'app passe son propre `check`), a11y, i18n, README | 1,0 | F7 | oui (27 nov.) |
| Options | worker d'URL (0,5), plan de défragmentation appliqué au dépôt `disquette` lui-même (0,5), export image PNG (0,5), skill + agent (0,5), power (0,5) | 2,5 | — | non (optionnel) |
| Soumission | vidéo, textes Devpost, billet de blog, publication sociale | 1,5 | gel code 27 nov. | — |

**Périmètre minimal : 8 jours-agent** (F1..F8), options +2,5 j, soumission +1,5 j.

**Calendrier** (11 nov. → 4 déc. 14 h PT)

| Date | Jalon |
|---|---|
| 12 nov. | `core-allocator` spec requirements.md revu ; `core` amorcé |
| 14 nov. | `har-reader` verte ; premier verdict sur un HAR de fixture |
| 16 nov. | `build` merged ; la CLI lit un `stats.json` |
| 19 nov. | garde CI `disk-budget` active sur le dépôt `disquette` |
| 23 nov. | l'application web affiche un verdict de bout en bout |
| 25 nov. | plan de défragmentation : avant/après chiffrés |
| 26 nov. | propriétés fast-check vertes, seeds consignées |
| 27 nov. | **gel du code** ; l'app passe son propre `disquette check` ; app déployée sur Pages |
| 28 nov. | **gel de la vidéo** : le plan fort est enregistré, tous les chiffres du script sont mesurés |
| 29 nov. – 2 déc. | montage vidéo, textes Devpost, README, `KIRO_JOURNAL.md`, billet de blog |
| 3 déc. | soumission (1 jour de marge avant le 4 déc. 14 h PT) |

**Ce qui doit être mergé avant le gel vidéo du 28 novembre** (liste de contrôle) : allocateur (`allocate.ts`) ; lecteur HAR + assainissement ; les trois formats ; le verdict (disques, Kio, secondes, CO2e) ; l'explorateur de disquettes ; la vue défragmenteur ; la CLI `check` ; le hook `disk-budget` ; les 12 propriétés ; l'application déployée sur Pages avec mode démo et mode hors ligne ; les fixtures HAR ; les chiffres du script vidéo mesurés et notés dans `docs/METHOD.md`.

### F.15 Risques et parades

| Risque | Probabilité | Impact | Parade | Plan B |
|---|---|---|---|---|
| La métaphore est perçue comme de la nostalgie | Moyenne | Fort | Le README et la vidéo ouvrent sur le nombre, pas sur la disquette ; la disquette n'apparaît qu'après le chiffre | Vidéo réécrite : le chiffre d'abord, la métaphore ensuite |
| L'allocateur n'est pas optimal et un juge le remarque | Moyenne | Moyen | On ne prétend pas à l'optimum : la borne inférieure est affichée à côté du résultat, et l'optimum exact est réservé aux petits cas (≤ 12 unités) | Ajouter un solveur exact pour les petits cas (option) |
| Le plan de défragmentation ne réduit pas le nombre de disquettes sur un vrai site | Élevée | Moyen | Le verdict distingue « disque 1 » (le vrai levier : −72 Kio, −1,2 s) et « nombre de disquettes » ; le message le dit explicitement (DIS-F-09) | Vendre le gain en Kio du disque 1 et en secondes |
| L'application de démonstration est elle-même trop lourde | Moyenne | Fort | Budget dur : shell ≤ 200 Kio compressés, lectureur chargé à la demande ; le build passe son propre `disquette check` | Réduire la visualisation (pas de graphe de dépendances interactif) |
| Un HAR de la démo contient des identifiants | Moyenne | Fort | Assainissement obligatoire + test de propriété DIS-P-10 + option `--include-urls` par défaut désactivée | HAR de démonstration re-fabriqué à la main |
| Les juges ne testent pas l'application | Élevée | Fort | La vidéo porte le message ; le mode démo se lance en un clic ; les chiffres sont dans la description Devpost | — |
| Le chiffre « 12 disquettes » du script ne correspond pas à la mesure finale | Moyenne | Moyen | Le nombre est mesuré le 27 nov. et la phrase est réécrite avec la valeur mesurée avant le gel du 28 nov. | Reprendre la voix off (2 minutes de studio) |
| Le facteur CO2 est contesté | Moyenne | Moyen | La constante est affichée dans l'UI et documentée (SWDM v4, 148,2 g/Go) ; l'intensité du réseau est modifiable dans la config ; le mot « estimation » est dans l'UI | Ne montrer que les disquettes et les secondes dans la vidéo |
| Crédits Kiro épuisés | Moyenne | Moyen | Hooks en action **commande** (0 crédit) ; l'agentic n'est utilisé que sur les specs cœur | Construire à la main les lots non critiques |
| Le temps manque (23 jours, plusieurs chantiers en parallèle) | Élevée | Fort | Périmètre minimal à 8 j, options clairement séparées ; F1+F2+F4 sont suffisants pour un dépôt honorable (CLI seule) | Soumettre la CLI seule avec la vidéo |

### F.16 Démonstration et soumission

**Vidéo — plan minuté 0:00 → 3:00.** Pas de musique, pas de marque tierce à l'écran (les hôtes sont masqués), projet filmé à l'écran sur l'appareil visé.

| Temps | Image (ce qu'on voit) | Voix off (mot pour mot, anglais) |
|---|---|---|
| 0:00–0:06 | Une disquette 3,5" réelle, de notre stock, qu'on insère dans un lecteur USB. Écran noir ensuite. | *(silence, puis)* "In 1991, this was one point four four megabytes. Everything that mattered fit on it." |
| 0:06–0:18 | L'écran de l'app : une rangée de 12 disquettes dessinées, remplies. Le compteur « 12 disks · 17.7 MB » en gros. Aucun nom de site à l'écran. | "Today the average home page on the web weighs two and a half megabytes. This one — a well-known, very heavy site — weighs twelve disks. Seventeen point seven megabytes. Thirteen seconds on a three-G connection." |
| 0:18–0:26 | Le curseur prend un fichier HAR et le dépose sur la coquille. | "Now drop in your own. No account. No upload. Nothing leaves this tab." |
| 0:26–0:42 | L'analyse : la barre de progression en octets, puis le verdict : « 5 disks · 2 746 KiB · 14.1 s · 0.42 g CO2e ». | "Five disks. Two thousand seven hundred and forty-six kibibytes. Fourteen point one seconds on a one point six megabit link — that is Lighthouse's mobile profile. And zero point four two grams of CO2 per visit." |
| 0:42–0:58 | L'explorateur : on clique sur `charts.js` ; le panneau de droite montre qui l'importe ; on voit le disque 2 se remplir. | "Click a file. Here is who imports it, and what it costs. Disk one is the critical path — everything else is deferred." |
| 0:58–1:16 | La vue défrag : on active le plan ; la bougie fond ; « 5 → 3 disks » ; la liste des actions. | "The defragmenter proposes a plan. Defer the admin route. Split a chunk that mixes two routes. Drop a third-party script. Three disks instead of five, and disk one drops by seventy-two kibibytes." |
| 1:16–1:30 | Un terminal : `disquette check --stats stats.json`, puis un `exit 1` avec le nom du module fautif. | "In CI, one command. If the critical path overflows the first disk, the build fails, and it tells you which module did it." |
| 1:30–1:52 | Le dossier `.kiro/` : `specs/`, `hooks/`, `agents/`, `skills/`. Un contre-exemple fast-check affiché dans le journal. | "Kiro wrote the allocator from a spec, wrote the property tests, and found a bug we would have shipped: adding three kibibytes moved forty files to another disk. The hook runs the check on every build." |
| 1:52–2:12 | Le mode hors ligne : on coupe le réseau (bandeau « offline mode ») ; l'app continue, on dépose un autre HAR. | "It works with the network off. The file never leaves the browser — a test fails the build if anything is ever sent." |
| 2:12–2:34 | Retour sur le verdict, format 720 Kio : le même site passe à « 6 disks » avec le bandeau « 2 units split » ; puis retour au format HD. Le sélecteur de format. | "Change the format. Double density is brutal: six disks, and two units had to be split because they are bigger than the disk itself. High density is the default. The format changes the difficulty, not the tool." |
| 2:34–2:52 | Le compteur de la bougie qui fond, plan appliqué, avant/après côte à côte ; les trois chiffres finaux. | "One disk is the goal. Fit on one disk. The number is measured, not estimated — the tool is the measure." |
| 2:52–3:00 | Écran final : l'adresse de l'app, l'adresse du dépôt, le trigramme « DIS ». | "Disquette. Your web app must fit on a disk. The app and the source are in the description. No account, no upload, no music. Thank you." |

*(Le nombre « 12 » et « 17,7 MB » sont mesurés le 27 novembre sur la fixture ; la phrase est réécrite avec la valeur mesurée si elle diffère — **À vérifier**.)*

**Textes Devpost (en anglais)**

- **Titre** : `Disquette — your web app must fit on a disk`
- **Tagline** : `A 1.44 MB floppy disk is back — as the unit of shipment for the web. Your build is counted in disks; disk one is your critical path; a defragmenter tells you what to move.`
- **What it does** : 120 mots. Dépôt d'un HAR (hors ligne, sans compte) → nombre de disquettes, Kio, secondes au profil 1,6 Mbit/s, grammes de CO2e (SWDM v4) ; explorateur de disquettes ; plan de défragmentation chiffré ; CLI `disquette check` en garde CI.
- **How we built it** : 150 mots. Kiro : specs exigences-d'abord pour le cœur et le lecteur HAR, conception-d'abord pour l'explorateur et le défrag ; steering de domaine (`disk-myth.md`, `privacy.md`) ; hooks en action commande (`disk-budget`, `loc-budget`, `no-network-guard`, `plan-determinism`) ; agent `defrag-planner` en lecture seule ; skill `fit-on-one-disk` ; 12 propriétés fast-check, dont un contre-exemple qui a fait corriger l'algorithme ; journal `KIRO_JOURNAL.md`.
- **Why it's a Resurrection** : 80 mots. La disquette est morte ; ce qu'on ressuscite est la discipline de la pénurie, et elle est reintroduite dans la chaîne de build, pas dans un décor.
- **Try it** : l'adresse de l'app (un clic, HAR de démonstration préchargé), la commande `npx disquette check --har <fichier>`, et le HAR d'exemple.
- **Tests instructions for the judges** : « Open the app. Click *Use the demo HAR*. You will see 5 disks, 2 746 KiB, 14.1 s on the 1.6 Mbps profile, 0.42 g CO2e per visit. Switch the format to *DD 720 KB* and watch the count go to 6, with two units flagged as split. Open the defrag view and apply the plan. Everything runs offline: turn off your network and repeat. »

**Bonus**

- **Blog** (pendant la période) : « The floppy disk was a shipping unit. We brought it back as a budget. » — avec les chiffres mesurés, la méthode SWDM, et le contre-exemple fast-check.
- **Social** : publication commençant par `#KiroweenHackathon26`, disant ce que Kiro a changé (le hook qui bloque une PR, la spec qui a produit le contre-exemple de stabilité).
- **Best Demo** : la vidéo des 30 premières secondes suffit.

### F.17 Recette

Exécutable par `node scripts/recette.mjs` (uniquement local, aucun réseau requis).

| # | Vérification | Résultat attendu |
|---|---|---|
| 1 | `node scripts/recette.mjs demo` — verdict sur `fixtures/har/kitchen-sink.har`, format HD | `5 disks · 2746 KiB · 14.1 s · 0.42 gCO2e` (valeurs exactes figées dans le script, après mesure) |
| 2 | Même HAR, format DD puis Zip | `6 disks · splitUnits: 2` puis `1 disk (Zip 100 MB)` |
| 3 | `fixtures/har/with-credentials.har` | `3 credentials removed` et `0` occurrences de `session=` dans le modèle |
| 4 | Deux analyses successives du même HAR | `planHash` identiques, deux exécutions → hash `a3f1…` consigné |
| 5 | Contrôle de capacité sur toutes les disquettes | `max used = 1409 KiB ≤ 1440 KiB` (aucune disquette ne dépasse le format) |
| 6 | Conservation du volume | `sum(modules) = sum(disks) = 2 811 904` (écart 0) |
| 7 | `node scripts/recette.mjs determinism` — 100 exécutions | `100/100 identical planHash` |
| 8 | `node scripts/recette.mjs properties` | `12 properties passed`, graines listées |
| 9 | `node scripts/recette.mjs cli` — `disquette check` sur un fixture en débordement puis sur un bon fixture | `exit 1` puis `exit 0`, rapport Markdown écrit dans `artifacts/` |
| 10 | `node scripts/recette.mjs offline` (Playwright, `context.setOffline(true)`) | `0 network requests`, la démo complète passe, verdict identique |
| 11 | `node scripts/recette.mjs dogfood` — `disquette check` sur le build de `apps/web` | `1 disk · ≤ 1 474 560 bytes` (l'app tient sur une disquette) |
| 12 | `node scripts/recette.mjs a11y` (Playwright + axe) | `0 violations` sur l'écran de verdict et sur l'explorateur |

### F.18 Questions ouvertes

1. **Format par défaut** : 1 440 Kio (HD) retenu ; le 720 Kio est un mode « brutal » qui fait la vidéo. Confirmer ce choix, ou faut-il faire du DD le mode d'accueil du site public ?
2. **Chiffre de la vidéo** : « 12 disquettes » est mesuré le 27 novembre sur la fixture ; si la mesure diffère, on réécrit la voix off (ou on refait la prise). Quelle marge accepte-t-on ?
3. **HAR de site tiers** : on ne commite aucun HAR de site tiers ; la mesure « site célèbre » se fait en direct via le worker, avec l'hôte masqué à l'écran. Valider ce parti pris (il protège la règle « pas de marque tierce ») ou demander l'autorisation d'afficher le nom ?
4. **Facteur carbone** : on garde la constante mondiale SWDM v4 (148,2 g/Go) et on rend l'intensité du réseau configurable. Un mode « France » (≈ 56 gCO2e/kWh, **À vérifier**) est-il utile, ou noyerait-il le message ?
5. **Agent `defrag-planner`** : il écrit dans `.kiro/plans/`. Autorise-t-on un droit d'écriture plus large (par exemple un rapport Markdown à la racine du dépôt analysé) ?
6. **CLI** : publiée sur npm (`npx disquette`) ou seulement dans le dépôt ? La publication ajoute une charge de maintenance jusqu'au 29 janvier 2027 ; le repo suffit pour les juges.
7. **Format 100 Mio** : garder Zip comme troisième format (fun, indulgent) ou le remplacer par « CD-ROM 700 Mio » ? Zip a l'avantage d'être une vraie disquette.
8. **Anti-triche** : le plan de défragmentation peut-il être appliqué automatiquement par un agent ? Pour l'instant, non (DIS-F-24 est exclu). Une option « apply with a PR » serait puissante mais risquée pour le temps disponible.
