# CONSIGNE — fabrique d'idées Kiroween 2026

Tu produis un **lot de 50 idées** de projets pour le hackathon Kiroween 2026. Rien d'autre.
Tu ne crées aucun dépôt, aucun code, aucun fichier autre que ton lot. **Tu ne délègues pas.**

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

## Contraintes dures (une idée qui les viole est une idée morte)

1. Faisable par **une personne pilotant des agents en ≤ 8 jours-agent**, du 12 novembre au 28 novembre
   (gel avant vidéo). Site statique d'abord, données dans le navigateur, zéro serveur si possible.
2. **Juges = développeurs/AWS-Kiro**, note sur 5 critères à 20 % : impact potentiel, usage de Kiro,
   design, innovation, présentation vidéo de moins de 3 minutes.
3. **Démo en 30 secondes sans compte ni installation** ; un chiffre mesuré par l'outil lui-même.
4. Application en **anglais**, dépôt public MIT, dossier `.kiro` à la racine.
5. **Aucune marque tierce** (pas de Tamagotchi, Winamp, Kodak, Nintendo, Clippy…), aucune musique sous droits,
   aucun texte religieux réel cité.
6. Vie privée : traitement local, aucun envoi de donnée sans action explicite ; aucun son par défaut.
7. Accessibilité AA, clavier, `prefers-reduced-motion`.

## À ne PAS dupliquer (déjà soumis par le user)

`bipeur` (pager SNPP pour superviser des agents IA, Resurrection) · `packet-voyage` (traceroute 1987 ×
géographie, Frankenstein) · `suture` (Git × tableur .xlsx, Frankenstein) · `ghost-hours` (commits × agenda ×
notes → heures et facture, Frankenstein) · `thin-air` (webcam → instrument de musique, Frankenstein) ·
`bare-bones` (squelette d'explorateur de données + 2 apps, Skeleton Crew) · `placard` (audit des secrets
Git en manoir hanté, Costume Contest).
En plus : 5 idées déjà écrites et à écarter — **Disquette** (budget 1,44 Mo), **Rota** (squelette
d'ordonnancement), **Partie double** (squelette de grand livre), **Exorcisme** (rite d'expulsion d'une
dépendance), **Séance** (postmortem où les fantômes se contredisent).
Le portefeuille est déjà très « outils pour développeurs » : **au moins la moitié de ton lot doit viser un
public non développeur** (bénévoles, familles, artisans, enseignants, soignants non médicaux, petites
associations, usagers de service public).

## Format de sortie — strict, rien d'autre

Fichier : une seule écriture, pas de relecture inutile. En-tête de 2 lignes, puis **exactement 50 lignes
numérotées**, une idée par ligne, **45 mots maximum par idée** :

```
# Lot NN — <nom du filon>
<1 ligne : ce que couvre ce filon>
01. **Nom du projet** — ce que c'est et pour qui, en une phrase. Différenciateur en une clause. [X j]
02. ...
```

`[X j]` = charge estimée en jours-agent (1 à 8). Pas de tableau, pas de section, pas de conclusion,
pas de liste de vérification : **50 lignes et c'est tout**.

## Barre de qualité — ce qui sépare une idée gagnante d'une idée banale

- **Une idée par ligne doit tenir debout seule** : on comprend le produit, le public et le différenciateur
  sans lire autre chose.
- La métaphore **porte la fonction** : si on retire le costume ou la technologie morte, l'outil doit rester
  utile, et l'élément ressuscité/déguisé doit coder une information réelle.
- Cherche **l'inattendu utile**, pas le joli vide : un chiffre mesurable, un artefact que l'on peut montrer
  en 10 secondes de vidéo, un public qui existe vraiment.
- Interdit : les clones de jeu rétro, les générateurs d'art, les « dashboard pour X » sans différenciateur,
  les idées qui nécessitent un matériel introuvable, une API payante ou un compte tiers.
- **Varie les publics, les domaines et les formes** à l'intérieur du lot : pas 50 variantes de la même idée.
- Les noms de projet doivent être évocateurs, courts, en français ou en anglais, et **non déjà pris**
  par un produit connu.
