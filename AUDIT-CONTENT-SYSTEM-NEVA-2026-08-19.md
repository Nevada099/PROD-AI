# Audit mode debug — Content System PROD'AI / Neva

**Date :** 19 août 2026
**Périmètre :** 26 fichiers Markdown (Studio IA + dossier personnages) + base Notion `Neva Content — Pipeline éditorial` (55 lignes, 6 vues)
**Nature :** audit critique, pas une validation. Le but est de faire tomber ce qui ne tient pas avant de produire.

---

## 1. Ce que j'ai lu

**Couche stratégie (18 août)** — `DECISIONS.md`, `STATUS.md`, `HANDOFF.md`, `OPEN-QUESTIONS.md`, `SYNTHESE-PM-2026-08-18.md`, `MASTER-INDEX.md`, `ANALYSE-POSITIONNEMENT-MARKETING.md`, `ANALYSE-SMM-INSTAGRAM-LINKEDIN.md`, `NEVA-ARCHITECTURE-GENERATIVE-AGENTIQUE.md`, `SYNTHESE-STRATEGIQUE-3-BENCHMARKS.md`, `AUDIT-PRODUITS-JULIA-IMANE-ALLIE.md` (507 lignes).

**Couche système éditorial v1 (18 août, 22h–23h)** — `NEVA-CONTENT-SYSTEM.md`, `MIX-EDITORIAL-NEVA.md`, `NEVA-STYLE-SYSTEM-VIDEO.md` (321 lignes), `PLAN-15-CONTENUS-AJTBD-NEVA.md` (475 lignes), `NEVA-CONTENT-IMPLEMENTATION-PLAN.md`.

**Couche système éditorial v2 (19 août, 14h–15h)** — `CONTENT-CREATION-SYSTEM/00-ARCHITECTURE-CANONIQUE.md`, `SAISON-01-DE-LEXECUTION-AU-SYSTEME.md`, `CAHIERS-DES-CHARGES-NEVA.md`, `TONE-OF-VOICE-KATERINA-NEVA.md`, `LEAD-MAGNETS/*`, `PRODAI-CONTENT-SYSTEM/00-MASTER-PIPELINE.md`, `PRODAI-CONTENT-SYSTEM-IMPLEMENTATION-PLAN.md`.

**Couche personnage** — `02-personnages/neva/` : `bible.md`, `arc.md`, `voix.md`, `visual-lock.md`, `idees.md`, `offre.md`.

---

## 2. Verdict en une page

**Ce qui est très bon.** La qualité de pensée est au-dessus de la moyenne du marché. Trois pièces sont réellement fortes et réutilisables telles quelles :

- le **Tone of Voice** (`TONE-OF-VOICE-KATERINA-NEVA.md`) — c'est le meilleur document du corpus. Il est fondé sur des textes réels, il nomme les tics, les interdits, l'architecture narrative et une grille d'intensité chiffrée. C'est un vrai actif ;
- l'**audit des 3 benchmarks** — avec un niveau de preuve explicite ([Fait] / [Déclaration] / [Inférence]), ce qui est rare et honnête ;
- les **deux textes complets dictés** (« combiner l'incombinable » et « ne rien faire de mes propres mains ») — ce sont les seuls contenus du corpus qu'aucun autre consultant IA ne pourrait écrire.

**Ce qui ne tient pas.** Le système a été écrit **deux fois en deux jours, sans que la deuxième version n'annule la première**. Résultat : deux taxonomies, deux règles Notion opposées, deux structures d'unité, quatre comptes de contenus différents. La base Notion porte matériellement les deux schémas en même temps. Et surtout : le corpus déclare lui-même que le contenu doit venir **en dernier**, après l'offre, la preuve et le funnel — or c'est le contenu qui a été construit en premier.

**Diagnostic en une phrase :** le système est excellent en méthode et pauvre en matière. Il y a 8 gates de contrôle et 15 lead magnets planifiés pour 2 textes réellement écrits et 0 preuve chiffrée.

---

## 3. Mode debug — les défauts

### 🔴 BLOQUANT

#### D1. Deux systèmes éditoriaux concurrents, aucun n'a été déclaré obsolète

| | Version 1 (18/08, 22h) | Version 2 (19/08, 14h) |
|---|---|---|
| Taxonomie | 3 rubriques : Difficulté / Insight / Tip | 4 piliers : Product Builder / IA appliquée / Business & Mindset / Cas réels |
| Règle Notion | **1 ligne = 1 plateforme + 1 format** (une idée sur 2 réseaux = 2 lignes) | **1 ligne = 1 idée mère**, Instagram et LinkedIn en 2 colonnes |
| Structure d'unité | AJTBD en 8 temps (État A → Problème → Tension → Insight → Méthode → État B → CTA → actif) | 8 blocs (Hook visuel → Hook verbal → Point A → Body → Point B → Pont → CTA → Sortie) |
| Volume | 15 contenus (12 socle + 3 ponts) | 7 chapitres de Saison 1 |
| Contrôle | Contrôle qualité par checklist | 8 « Gates » |
| Capture | Bot Telegram + n8n | Capture manuelle, `insight-capture-protocol` |

Les deux règles Notion sont **exactement inverses**. Aucun des deux documents ne dit qu'il remplace l'autre. Aucun n'est en `99-ARCHIVES/`.

**Preuve matérielle :** la base Notion contient les deux schémas simultanément — la propriété `Catégorie` (3 options v1) **et** la propriété `Pilier` (4 options v2) ; `Plateforme` + `Format` (v1) **et** `Instagram` / `Format Instagram` / `LinkedIn` / `Format LinkedIn` (v2). 30 lignes utilisent le schéma v1, 7 lignes le schéma v2.

> **À trancher :** une seule version survit. Sans ça, aucun contenu ne peut être produit sans se contredire.

---

#### D2. Le corpus viole sa propre règle de séquencement

Trois documents disent la même chose, très clairement :

- `DECISIONS.md` n°7 : « Le contenu est l'étape finale, après inventaire, offre, preuve et funnel. »
- `STATUS.md`, section *Interdit avant validation* : « écrire un calendrier de contenu final ».
- `SYNTHESE-PM`, ordre de travail : `… → deux pilotes maximum → entretiens segments → choix d'un segment → pilotes mesurés → atelier Academy → positionnement/CTA/site → stratégie IG/LI → calendrier`.

Et pourtant, en 24 h ont été produits : un plan de 15 contenus, un style system vidéo de 321 lignes, un Tone of Voice, une saison de 7 chapitres et 55 lignes Notion — **avant** l'offre validée, **avant** la preuve, **avant** le funnel.

> **À trancher :** soit tu assumes que le contenu passe devant (il faut alors réécrire `DECISIONS.md` n°7 et `STATUS.md`), soit tu gèles la production éditoriale. Le système ne peut pas dire les deux.

Mon avis : le contenu **peut** passer devant, mais alors le contenu de lancement doit être du **contenu de découverte** (raconter, poser l'identité, tester les angles) et **pas** du contenu à lead magnet. Voir D4.

---

#### D3. Neva n'existe pas encore comme personnage

Le dossier `02-personnages/neva/` est **vide** : `bible.md`, `arc.md`, `voix.md`, `visual-lock.md`, `idees.md` ne contiennent que les commentaires du gabarit. Et `offre.md` dit :

> « **Décidé :** danseuse. Offre à définir. »

Il y a donc **deux Neva** dans l'arborescence : une danseuse de dessin animé, et un avatar corporate PROD'AI. Rien ne les relie.

Conséquences concrètes :
- `NEVA-STYLE-SYSTEM-VIDEO.md` contient un contrôle qualité sur le lip-sync, les clignements, les mains déformées, la stabilité des cheveux… **pour un avatar qui n'a ni visage figé, ni voix, ni verrou visuel, ni seed, ni compte HeyGen documenté** ;
- la palette (§3.3) est déclarée « provisoire, à confirmer contre la charte PROD'AI ». Or une charte existe déjà : `Claude.md files/Studio IA/Brand/BRAND-AUDIT-ET-REFONTE.md` (direction « Cuivre & Encre », palette relevée en hex). Les deux n'ont jamais été croisés ;
- `OPEN-QUESTIONS.md` demande encore : « Neva est-elle uniquement l'interface éditoriale ou aussi un produit avatar vendable ? » — non tranché.

> **À faire avant toute vidéo :** remplir le passeport Neva (skill `distillation-personnage` puis `passeport-serie`), figer le visual lock et la voix, croiser avec la charte PROD'AI existante.

---

### 🟠 SÉRIEUX

#### D4. La règle « pas 15 lead magnets » a été écrite trois fois et jamais appliquée

- `AUDIT-PRODUITS` §6 étape 2 : « **un actif de conversion, pas quinze** » ;
- `AUDIT-PRODUITS` §7.2 : « Ne pas créer un lead magnet lourd par post » ;
- `HANDOFF.md`, prochaine action n°2 : « Construire seulement **2 à 3 lead magnets modulaires** au lieu de 15 actifs séparés. »

Or `PLAN-15-CONTENUS-AJTBD-NEVA.md` attribue **un actif distinct à chacun des 15 contenus** (matrice, template, diagnostic, calculateur, modèle de brief, checklist, matrice de supervision, scorecard, charte, fiche, carte, canevas + 3 pages de cas). Et la base Notion porte les 15 mots-clés Chatplace correspondants. La correction n'a été appliquée **nulle part**.

Aggravation : `LEAD-MAGNETS/00-BIBLIOTHEQUE-ET-REGLES.md` (v2) réintroduit un mapping **1 chapitre = 1 actif**, soit 7 actifs. Troisième chiffre.

> **Recommandation :** une seule bibliothèque Notion modulaire (« AI Operating System Starter Kit ») + 2 actifs autonomes maximum. Le mot-clé pointe vers une *section* de la bibliothèque, pas vers un PDF différent à chaque fois.

---

#### D5. Le funnel s'arrête sur un trou

Trois versions du chemin de conversion cohabitent, et aucune ne nomme l'outil final :

- Notion / v1 : `Chatplace — mot-clé X` (orthographié tantôt *Chatplace*, tantôt *ChatPlace*) ;
- `LEAD-MAGNETS` / v2 : `Instagram : mot-clé → aperçu en DM → **page email** → actif` ; `LinkedIn : commentaire → **DM manuel pendant le pilote** → page email` ;
- `NEVA-CONTENT-IMPLEMENTATION-PLAN` : Telegram + n8n + Notion + Canva + Drive — **ChatPlace n'y figure pas**.

« Page email » n'est jamais rattachée à un outil (pas de Systeme.io, pas de Brevo, pas de formulaire nommé). Il n'y a donc aujourd'hui **aucun endroit où un lead peut réellement atterrir**.

`NEVA-STYLE-SYSTEM-VIDEO` §5 exige pourtant, avant publication : « Le tunnel Chatplace est testé de bout en bout ». Ce contrôle est aujourd'hui impossible à cocher.

> **À faire :** nommer l'outil de capture email et tester une fois le parcours complet à la main, avant le premier post.

---

#### D6. Les 12 contenus de socle ne contiennent aucune preuve

`MASTER-INDEX.md` pose une règle de preuve : chaque affirmation doit indiquer source, date, statut (`TESTÉ` / `PILOTE` / `EN CONSTRUCTION` / `HYPOTHÈSE`), résultat, limite, part humaine. Le Tone of Voice exige des détails non remplaçables (`15 mois`, `36 m²`, `8 h 20`) et coche : *« Le texte contient une scène qu'une autre personne ne pourrait pas revendiquer. »*

Sur les 12 contenus de socle du plan AJTBD, **10 sont des thèses générales sur l'IA** : « automatiser un chaos ne crée pas un système », « le human-in-the-loop n'est pas un échec », « génératif, agentique, automatisé », « ce n'est pas un problème de prompt »… Ce sont exactement les sujets que **n'importe quel consultant IA francophone peut publier demain**. Seuls les n°01 et 02 passent le test anti-générique.

Aggravation : `SAISON-01` liste 9 gisements de matière réelle (Booking Control Flow, JobsAI, Jade/Luna/Neva, Content Intelligence — 1 715 posts et 61 comptes analysés, assistant vocal, Bubble, Studio IA, production vidéo). Sur ces 9 gisements, **3 seulement sont exploités** (contenus 13, 14, 15) et le plan les repousse explicitement en « réserve vague 2 ».

> Autrement dit : la matière qui rend le contenu incopiable a été mise **de côté**, et la matière copiable a été mise **devant**. C'est l'inverse de ce que dit le TOV.

---

#### D7. Contradiction de dosage : « Promotion 1/5 » vs. 15 posts à lead magnet

Le Tone of Voice fixe l'intensité **Promotion = 1/5** avec la règle : « La preuve et la transformation précèdent l'offre. »

Or le plan AJTBD met un CTA + mot-clé + lead magnet sur **15 contenus sur 15**, dès le tout premier. Un compte dont 100 % des publications de lancement demandent un commentaire pour recevoir un fichier n'est pas à 1/5 de promotion.

> **Recommandation :** les 3 à 4 premiers contenus sans aucun lead magnet — juste la scène, la vérité et une question. Le mot-clé arrive quand il y a une audience à convertir.

---

#### D8. Les deux plans de contenu ne se recouvrent qu'à moitié

| Chapitre Saison 1 (v2) | Contenu AJTBD (v1) |
|---|---|
| 1. Product Builder | ✅ n°03 |
| 2. Combiner sans terminer | ✅ n°01 |
| 3. Noyée par l'IA | 🟡 partiellement n°04 |
| 4. Apprendre la langue | 🟡 partiellement n°05 |
| 5. Claude Code / Cursor / Codex | ❌ absent |
| 6. Le skill n'est pas le système | ❌ absent |
| 7. Transformer le travail en capital | ❌ absent |

Et inversement : les AJTBD 06, 07, 08, 09, 10, 11, 12 n'ont **aucun** chapitre correspondant. Recouvrement réel : environ 40 %.

---

### 🟡 À CORRIGER

#### D9. Chemins de fichiers cassés dans le canon

`00-ARCHITECTURE-CANONIQUE.md` déclare comme source de vérité :

> « `SKILLS & PIPELINES/PRODAI-CONTENT-SYSTEM/` contient les procédures exécutables. »

Ce dossier **n'existe pas**. Le dossier `SKILLS & PIPELINES/` existe bien (dans `AI-WORKSPACE/Cartoons/`) mais ne contient que `character-story-unpacker`, `character-to-vertical-series`, `producing-vertical-series-9x16` et un dossier de cours. Le Master Pipeline a en réalité été écrit dans `studio-ia-migration/05-MARQUE-ET-CONTENU/PRODAI-CONTENT-SYSTEM/`.

La tâche 1 du plan d'implémentation est pourtant cochée `[x]` pour un chemin qui n'existe pas.

**Fichiers annoncés et absents :** `CHAPITRE-01-PRODUCT-BUILDER.md`, `LEAD-MAGNET-AI-OS-STARTER-KIT.md`, `LESSONS.md`, `LEAD-MAGNETS/01-*`.

#### D10. Deux plans d'implémentation actifs en parallèle

`NEVA-CONTENT-IMPLEMENTATION-PLAN.md` (bot Telegram, 3 tâches, **0 case cochée**) et `PRODAI-CONTENT-SYSTEM-IMPLEMENTATION-PLAN.md` (6 tâches, 5 cochées sur 24). Ils ne se citent pas, ne se hiérarchisent pas, et la tâche 2 du second (« restructurer Notion : 1 ligne = 1 idée mère ») **détruirait** la structure exigée par le premier.

#### D11. Le style system vidéo repose sur une source secondaire

`NEVA-STYLE-SYSTEM-VIDEO.md` est honnête à ce sujet (§2 liste 11 éléments non validés), mais il faut le dire clairement : la déconstruction du Reel d'Imane vient d'**une étude de cas, pas des fichiers vidéo**. Typographie, sous-titres, safe zones, colorimétrie, cadence de coupe restent non vérifiés. §7 demande de réunir 5 à 10 Reels avant de figer la v1.0 — **ce n'est pas fait**.

#### D12. Coquilles visibles dans Notion

Ligne ID 20 : « Post 1 - Je pensais que l'intégration d'agents IA était un problème **téchnique**, **maisc'est** finalement un problème d'ego ». Deux fautes dans un titre destiné à devenir un post.

---

## 4. Analyse de la base Notion

**55 lignes, 6 vues, 28 propriétés.**

### Répartition réelle

| Phase éditoriale | Lignes | Texte final rempli | Commentaire |
|---|---:|---:|---|
| Archive historique | 18 | 0 | dont **8 lignes vides** (ID 1–8) et 9 contenus de l'**ancienne stratégie immobilière** |
| Quarantaine | 30 | 30 | les 15 sujets AJTBD × 2 plateformes |
| Rédaction | 1 | 0 | la seule ligne au nouveau schéma |
| Sujet approuvé | 6 | 0 | chapitres 2 à 7, vides |
| Sujet brut | 0 | — | **la vue « 00 — Sujets à approuver » est vide** |
| Production | 0 | — | **les vues « Instagram — Production » et « LinkedIn — Production » sont vides** |

**3 vues sur 6 n'affichent rien.** Et le lien que tu m'as envoyé (`v=3c07299b2234816a94e1000cc66ee5ce`) pointe vers la vue **« 99 — Archive historique »** — c'est-à-dire les vieux contenus immobiliers, pas le plan actif.

### Ce que ça révèle

1. **Le travail réel est en quarantaine.** 30 textes existent, statut « Rédigé » ou « À valider »… et sont rangés dans la phase qui veut dire « mis de côté ». Pendant ce temps, la vue « 01 — Série narrative » repart de 7 sujets vides. **Le système redémarre à zéro alors que 30 textes sont déjà écrits.**

2. **Ces 30 textes ne sont pas des posts.** Ils font entre **187 et 744 caractères** — des résumés, pas des publications. Le texte complet LinkedIn du plan AJTBD fait environ 2 000 caractères. Le statut « Rédigé » est donc trompeur : il faudrait lire « synopsis écrit ».

3. **Ils ne respectent pas le Tone of Voice.** Règle n°1 du TOV : *« Entrer par une scène, jamais par une leçon. »* Sur les 5 textes que j'ai ouverts, **5 ouvrent sur une leçon** :
   - *« Après avoir testé trop d'outils, j'ai cessé de comparer leurs listes de fonctionnalités… »*
   - *« Garder un humain dans la boucle n'est pas admettre que l'IA a échoué. »*
   Aucun lieu, aucune heure, aucun objet, aucun dialogue. C'est propre, c'est juste — mais ce n'est pas ta voix, c'est la voix d'un consultant. Ils sont à réécrire, pas à valider.

4. **Doublons structurels.** « Automatiser Booking sans déshumaniser la réponse » existe 2 fois (ID 31 LinkedIn, ID 33 Instagram) — normal selon la règle v1, **doublon** selon la règle v2. Si tu bascules sur v2, les 30 lignes de quarantaine doivent fusionner en 15.

5. **Propriétés mortes à supprimer :** `Column 2`, `Project 1`, `Project 2`, `Project 3` (jamais remplies), `Semaine` (S1–S4, appartient à l'ancienne stratégie immobilière). Et le doublon fonctionnel `Format` vs `Format Instagram`/`Format LinkedIn`.

6. **Champs de pilotage jamais remplis :** `Temps total` = 0 ligne, `Résultat` = 0 ligne, `Canva` = 0 ligne, `Drive` = 0 ligne, `Newsletter` = 0 ligne. Or la mesure `leads qualifiés / temps total de production` est le cœur de la « boucle d'apprentissage » du Master Pipeline. **Elle ne peut pas fonctionner.**

7. **Un seul `Hook` rempli sur 55 lignes.** Alors que la règle du studio (`Cartoons/CLAUDE.md`) est : *« Aucun scénario ne démarre tant que le hook n'est pas formulé en une seule ligne et validé "fonctionne sans le son". »*

---

## 5. Les 6 arbitrages à faire (avec ma recommandation)

| # | Question | Recommandation |
|---|---|---|
| 1 | v1 (3 rubriques, 1 ligne = 1 plateforme) ou v2 (4 piliers, 1 ligne = 1 idée mère) ? | **v2** — c'est plus récent, c'est aligné avec la Saison 1, et une idée mère unique évite deux textes divergents. Archiver v1 dans `99-ARCHIVES/`. |
| 2 | 7 chapitres ou 15 contenus ? | **7 chapitres × 2 plateformes = 14 unités.** Garder les meilleurs AJTBD comme sous-sujets à l'intérieur des chapitres, pas comme plan parallèle. |
| 3 | Combien de lead magnets ? | **1 bibliothèque modulaire + 2 actifs max.** C'est déjà écrit 3 fois dans le corpus, il suffit de l'appliquer. |
| 4 | Où atterrit le lead ? | **À nommer cette semaine.** Sans ça, aucun post ne peut sortir. Tant que le volume est faible : DM manuel + une page Notion publique. |
| 5 | Neva = média seul, ou produit vendable ? | **Média seul pour le lancement.** Un avatar vendable exige un passeport, un visual lock et une voix — rien n'existe. |
| 6 | Le contenu passe-t-il avant l'offre ? | **Oui, mais en mode découverte.** Réécrire `DECISIONS.md` n°7 pour l'assumer, et retirer les lead magnets des 3–4 premiers contenus. |

---

## 6. Plan de correction — 5 mouvements

**Mouvement 1 — Trancher (30 min, toi seule).**
Répondre aux 6 arbitrages ci-dessus. Rien d'autre ne peut avancer avant.

**Mouvement 2 — Nettoyer le canon (1 h).**
- Déplacer les documents de la version perdante dans `99-ARCHIVES/` avec un en-tête `REMPLACÉ PAR : …`.
- Corriger le chemin cassé de `00-ARCHITECTURE-CANONIQUE.md`.
- Fusionner les deux plans d'implémentation en un seul.

**Mouvement 3 — Nettoyer Notion (1 h).**
- Supprimer les 8 lignes vides et les 4 propriétés mortes.
- Sortir les 30 textes de quarantaine → les rattacher aux 7 chapitres comme matière première (pas comme posts).
- Renommer le statut `Rédigé` → `Synopsis` pour ces lignes : elles ne sont pas rédigées.
- Réparer ou supprimer les 3 vues vides.

**Mouvement 4 — Faire exister Neva (2 h).**
Passeport personnage, visual lock, voix, croisement avec la charte `Brand/BRAND-AUDIT-ET-REFONTE.md`. Aucune vidéo avant.

**Mouvement 5 — Un seul pilote complet (le vrai test).**
Chapitre 1 uniquement, de bout en bout : fiche A→B, hook validé sans le son, texte LinkedIn au TOV, Reel Instagram, lead magnet réel, parcours de capture testé à la main, temps de production chronométré, résultat mesuré → `LESSONS.md`.

**Tant que ce pilote n'est pas fait, ne rien produire en série.** C'est exactement ce que dit le Learning Gate n°8 du Master Pipeline — et c'est la règle la plus importante du corpus.

---

## 7. Ce qu'il ne faut surtout pas perdre

En nettoyant, ne pas jeter :
- `TONE-OF-VOICE-KATERINA-NEVA.md` — intact, c'est l'actif n°1 ;
- les 2 textes complets dictés (plan AJTBD, section finale) — la seule matière incopiable ;
- l'audit des 3 benchmarks et sa notation du niveau de preuve ;
- les 8 Gates du Master Pipeline ;
- la structure de vidéo en 6 segments du style system.
