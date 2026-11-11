# CONSIGNE 2 — fabrique d'idées Kiroween 2026, horizon DEUX MOIS

Tu produis un **lot de 50 idées** de projets pour le hackathon Kiroween 2026. Rien d'autre.
Tu ne crées aucun dépôt, aucun code, aucun fichier autre que ton lot. **Tu ne délègues pas.**

**Cette consigne remplace la précédente.** Le changement majeur : l'horizon n'est plus « 8 jours-agent »,
c'est **deux mois de construction**. Les idées doivent donc être **beaucoup plus ambitieuses** : des
produits complets, pas des utilitaires d'un week-end.

## Les 4 catégories (texte officiel)

- **Resurrection** — ressusciter une technologie morte, réinterprétée avec les innovations d'aujourd'hui
  ou pour résoudre les problèmes de demain.
- **Frankenstein** — coudre des technologies apparemment incompatibles en une seule app, pour un résultat
  inattendu et puissant.
- **Skeleton Crew** — un **gabarit de code squelette**, assez maigre pour être clair, assez souple pour
  servir à des cas variés, prouvé par **deux applications distinctes** tirées de cette base
  (deux dossiers séparés dans le dépôt).
- **Costume Contest** — n'importe quelle app, mais avec une **interface hantée, léchée et inoubliable**,
  où les éléments effrayants **améliorent la fonction** (pas de décoration gratuite).

## Horizon et jalons — la contrainte qui remplace toutes les autres

- **Horizon total : deux mois**, du 12 novembre 2026 à la mi-janvier 2027, soit ~40 jours-personne,
  démultipliables par une flotte d'agents pilotée par une personne.
- **Jalon 1 — v1 soumise avant le 4 décembre 2026, 23 h Paris.** Elle doit déjà tenir debout seule :
  un parcours complet de bout en bout, un mode démo sans compte, une vidéo de moins de 3 minutes.
- **Jalon 2 — version complète avant le 29 janvier 2027** (fin du jugement ; les juges peuvent re-regarder
  le dépôt et l'app). C'est là que l'ambition se paie : profondeur du moteur, richesse des données,
  multi-supports, publication durable.
- Chaque idée doit donc être **découpable** : dis en une clause ce que contient la v1 et ce que le
  deuxième mois ajoute.

## Ce que « ambitieux » veut dire ici — barre de qualité

Une idée à deux mois doit cocher **au moins quatre** de ces six points :

1. **Un moteur réel**, pas seulement une interface : solveur, moteur de règles avec explication, moteur de
   simulation calibré, index et recherche, moteur de fusion/synchronisation, compilateur d'un petit langage,
   chaîne de preuves cryptographiques.
2. **Des données réelles et volumineuses** : jeux de données publics ouverts, historique long, corpus
   importé par l'utilisateur, plusieurs territoires ou plusieurs années.
3. **Plusieurs surfaces cohérentes** : web, CLI, export imprimable, fichier auto-portant, éventuellement
   un petit worker gratuit — le tout partageant le même cœur.
4. **Un artefact durable** que l'utilisateur garde : rapport imprimé, registre chaîné, album, page
   publique, certificat vérifiable, archive lisible dans trente ans.
5. **Une preuve mesurée par l'outil lui-même** : un chiffre opposable aux juges (exactitude, temps,
   économies, couverture, conformité, écart à une référence).
6. **Une profondeur vérifiable** : propriétés testées (fast-check), corpus de cas tordus, rejeu
   déterministe, banc de performance rejoué en intégration continue.

## Contraintes dures inchangées

1. **Juges = développeurs/AWS-Kiro**, note sur 5 critères à 20 % : impact potentiel, usage de Kiro,
   design, innovation, présentation vidéo de moins de 3 minutes.
2. **Démo en 30 secondes sans compte ni installation** pour la v1 ; un chiffre mesuré par l'outil.
3. Application en **anglais**, dépôt public MIT, dossier `.kiro` à la racine et non ignoré.
4. **Aucune marque tierce** (pas de Tamagotchi, Winamp, Kodak, Nintendo, Clippy…), aucune musique sous
   droits, aucun texte religieux réel cité, aucune image sous droit.
5. Vie privée : traitement local d'abord, aucun envoi de donnée sans action explicite ; aucun son par défaut.
   Un petit worker serverless gratuit et sans compte est accepté s'il est indispensable.
6. Accessibilité AA, clavier complet, `prefers-reduced-motion`, information jamais portée par la seule couleur.
7. Règles de code de la maison : moins de 500 lignes par fichier, moins de 50 lignes par fonction,
   budgets de lignes par paquet gardés en CI, intégration continue sous 5 minutes.
8. Modèle de langage : toujours **optionnel et désactivé par défaut**, derrière une interface de
   fournisseur, avec une voie sans modèle pour chaque fonction.

## À ne PAS dupliquer (déjà soumis par le user)

`bipeur` (pager SNPP pour superviser des agents IA, Resurrection) · `packet-voyage` (traceroute 1987 ×
géographie, Frankenstein) · `suture` (Git × tableur .xlsx, Frankenstein) · `ghost-hours` (commits × agenda ×
notes → heures et facture, Frankenstein) · `thin-air` (webcam → instrument de musique, Frankenstein) ·
`bare-bones` (squelette d'explorateur de données + 2 apps, Skeleton Crew) · `placard` (audit des secrets
Git en manoir hanté, Costume Contest).
Plus les cinq idées déjà écrites en cahier des charges : **Disquette** (budget 1,44 Mo), **Rota**
(squelette d'ordonnancement), **Partie double** (squelette de grand livre), **Exorcisme** (rite d'expulsion
d'une dépendance), **Séance** (postmortem où les fantômes se contredisent).

Le portefeuille est saturé d'outils pour développeurs : **au moins la moitié de ton lot doit viser un
public non développeur** (bénévoles, familles, artisans, enseignants, soignants non médicaux, communes,
associations, usagers du service public).

## Format de sortie — strict, rien d'autre

Fichier : une seule écriture. En-tête de 2 lignes, puis **exactement 50 lignes numérotées**, une idée par
ligne, **60 mots maximum par idée** :

```
# Lot NN — <nom du filon>
<1 ligne : ce que couvre ce filon>
01. **Nom** — le produit et son public. Le moteur ou la mécanique réelle. v1 : … ; mois 2 : … [v1 X j / total Y j]
02. ...
```

`[v1 X j / total Y j]` = charge en jours-agent de la v1, puis du projet complet (total ≤ 40).
Pas de tableau, pas de section, pas de conclusion : **50 lignes et c'est tout**.

## Interdits

Les clones de jeu rétro, les générateurs d'art, les « tableaux de bord pour X » sans moteur ni
différenciateur, les idées exigeant un matériel introuvable, une API payante, un compte tiers obligatoire,
ou un modèle de langage indispensable au fonctionnement. Interdit aussi : l'idée dont la métaphore est
décorative — retire-la, l'outil doit rester meilleur *grâce* à elle.
