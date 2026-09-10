# 02 — Système éditorial PROD'AI : de l'idée au contenu publié

> **Document maître du pipeline de production.** Il remplace et fusionne 4 documents :
> `NEVA-CONTENT-SYSTEM.md` (v1, 18/08) · `CONTENT-CREATION-SYSTEM/00-ARCHITECTURE-CANONIQUE.md` · `CAHIERS-DES-CHARGES-NEVA.md` · `PRODAI-CONTENT-SYSTEM/00-MASTER-PIPELINE.md` (v2, 19/08).
> Originaux dans `99-ARCHIVES/2026-08-19_fusion-systeme-editorial/`.
> **Mise à jour : 28 août 2026** — schéma Notion et chaîne de rédaction resynchronisés après la restructuration du 27/08.

---

## 0. La règle Notion — tranchée deux fois, état au 28/08

L'audit du 19/08 avait signalé un défaut bloquant : deux systèmes éditoriaux écrits à 16 h d'intervalle, avec des règles Notion **inverses** (v1 : 1 ligne = 1 plateforme · v2 : 1 ligne = 1 idée mère).

**La restructuration du 27/08 a tranché — et pas dans le sens que le bot avait imposé le 19/08.** La règle en vigueur réconcilie les deux :

| Niveau | Porte quoi | Champ |
|---|---|---|
| **Unité mère** | L'idée, une seule fois | `Unité mère` (U1, U2, …) |
| **Ligne** | La déclinaison sur **un** canal | `Compte / Canal` + `N°` décimal |

```
U6 — Le reveal transformé en jeu
 ├── 22.1  Instagram Neva      → Format Instagram = Reel Neva
 ├── 22.2  LinkedIn Katerina   → Format LinkedIn  = Post texte
 └── 22.3  Instagram Katerina  → Stories
```

C'est bien **une ligne par plateforme** (la règle v1), mais l'idée n'est plus dupliquée sans lien : elle vit dans `Unité mère`, qui sert de regroupement dans la vue *01 — PLAN PAR UNITÉ*. Le problème que v2 cherchait à résoudre — deux textes qui divergent sans qu'on sache lequel fait foi — est réglé par le regroupement, pas par la fusion des lignes.

**Les deux axes de classement cohabitent :**

| Axe | Valeurs | Répond à |
|---|---|---|
| **Pilier** | Product Builder · IA appliquée · Business & Mindset · Cas réels | *De quoi on parle* |
| **Catégorie** | 🔴 Difficulté d'intégration · 🔵 Insights · 🟢 Tips d'intégration | *Sous quel angle* |

> ⚠️ **À vérifier côté bot.** `@Prodaicontentbot` a été construit le 19/08 pour écrire `Phase éditoriale = Quarantaine`. **Cette propriété n'existe plus.** Le workflow n8n doit être repris pour écrire `Unité mère` (ou rien) et laisser `Project 1` vide — les captures tombent alors automatiquement dans la vue *04 — BANQUE D'IDÉES · HORS FUNNEL*.

---

## 1. Le canon narratif

**La transformation personnelle précède la transformation professionnelle.** Tout fonctionne comme un journal : Katerina porte l'expérience et l'autorité, Neva la met en scène et la démontre. Le contenu conduit vers Lab ou Academy sans réduire chaque publication à une publicité.

**Le pilier Business & Mindset** suit toujours la chaîne : `expérience → croyance révélée → conséquence business → décision → outil concret`. Il ne devient jamais du développement personnel générique.

**Les démonstrations récurrentes** portent la signature `Testée dans le Lab` et n'utilisent que des fonctions vérifiées au moment de la production.

---

## 2. Le pipeline complet

```
Idée (vocale ou écrite)
   ↓  @Prodaicontentbot
Ligne Notion qualifiée · Phase = Quarantaine · Statut = Idée capturée
   ↓  tri humain
Sujet approuvé  →  ordre narratif dans la Saison
   ↓
Fiche A→B (Advanced JTBD)
   ↓
Rédaction : version Instagram + version LinkedIn, natives
   ↓
Contrôle Tone of Voice
   ↓
Production (Canva / avatar / démo écran)
   ↓
Publication  →  lead magnet  →  newsletter  →  Lab / Academy
   ↓
Mesure  →  leçon documentée
```

### Les 8 gates — aucun saut autorisé

1. **Subject Gate** — aucun texte avant approbation du sujet.
2. **Narrative Gate** — aucun format avant validation de Point A, Body, Point B et pont.
3. **Voice Gate** — aucun texte final avant contrôle du Tone of Voice.
4. **Format Gate** — Instagram et LinkedIn adaptés **séparément**.
5. **Conversion Gate** — aucun CTA si le post ne produit pas déjà une valeur autonome.
6. **Production Gate** — aucun Canva, avatar ou montage avant validation humaine.
7. **Publication Gate** — claims, droits, disclosure avatar et liens vérifiés.
8. **Learning Gate** — aucune automatisation ni production en série avant mesure d'un pilote.

---

## 3. Structure obligatoire d'une unité

Chaque contenu suit le même mouvement **Advanced JTBD** :

| # | Bloc | Exigence |
|---|---|---|
| 1 | **Hook visuel** | Compréhensible **sans le son** |
| 2 | **Hook verbal** | Texte, son ou question qui concentre la tension |
| 3 | **Point A** | Scène concrète + solution actuelle qui fonctionne mal |
| 4 | **Body** | Problème → tension → bascule → chemin technique |
| 5 | **Point B autonome** | Compréhension ou action obtenue **sans téléchargement** |
| 6 | **Pont** | La prochaine tâche naturelle, accomplie par le lead magnet |
| 7 | **CTA unique** | Une seule action |
| 8 | **Sortie** | Explorer · Academy · Lab |

Instagram montre la **scène, l'émotion, la bascule**. LinkedIn développe le **raisonnement, les arbitrages, la méthode**. Jamais un copier-coller.

---

## 4. Les 5 cahiers des charges par format

> Mécanique transférée d'Imane Oubou : `Résultat visible → promesse → processus → limite humaine → bénéfice → CTA unique`.
> Katerina porte l'expérience, le jugement et la preuve. Neva montre, synthétise et démontre. L'identité visuelle, les textes et les promesses d'Imane ne sont **pas** copiés.

### CDC 1 — Diary / transformation
- **Hook visuel :** visage, geste ou objet lié à la scène vécue.
- **Hook verbal :** vérité inconfortable ou contradiction.
- **Body :** scène → croyance → coût → bascule → nouvelle décision.
- **Preuve :** archive, document, interface ou décision réelle.
- **Instagram :** 35–55 s, Neva peut ouvrir/fermer ; Katerina porte le vécu.
- **LinkedIn :** récit plus développé, conséquence business et méthode.

### CDC 2 — Testée dans le Lab
- Montrer le **résultat dans les 3 premières secondes**.
- Nommer **une seule** tâche et **une seule** contrainte.
- Capturer l'écran réel, une action à la fois.
- Montrer l'erreur, le contrôle humain et la limite.
- Conclure sur le résultat observé, jamais sur une promesse générale.
- **Lead magnet :** démo complète, workflow, scorecard ou dossier de cas.

### CDC 3 — Carrousel méthode
7 slides : ① contradiction · ② Point A · ③ conséquence de la solution actuelle · ④ bascule · ⑤ méthode · ⑥ Point B et limite · ⑦ CTA.
- **Instagram :** 15–25 mots/slide, forte hiérarchie visuelle.
- **LinkedIn :** 25–45 mots/slide, davantage d'arbitrage.

### CDC 4 — Humain ↔ avatar
- Carton d'ouverture : `Katerina pense / Neva montre`.
- Carton de fin : `Créé et piloté par Katerina`.
- **Aucun faux dialogue ambigu**, jamais Neva présentée comme une personne indépendante.
- Katerina : expérience, choix, responsabilité. Neva : visualisation, démonstration, synthèse.

### CDC 5 — Teaser lead magnet
- Montrer un extrait **réellement utilisable**.
- Dire précisément ce que l'actif permet de faire.
- Un mot-clé **ou** un lien, jamais deux CTA.
- Tester le parcours complet **avant** publication.
- Ne pas demander commentaire + abonnement + formulaire avant toute valeur.

---

## 5. La base Notion — schéma de référence

**Base :** [Neva Content — Pipeline éditorial](https://app.notion.com/p/3987299b223480428ab6e470cc6bd8ea)
**Dernière vérification : 28 août 2026.** La base a été restructurée le 27/08 autour du **Mini-funnel 27 €** — la propriété `Phase éditoriale` a disparu, remplacée par un regroupement en **unités mères**.

### La règle d'organisation

```
Unité mère (U1, U2, …)  =  une idée
     ├── ligne « Instagram Katerina »
     ├── ligne « LinkedIn Katerina »
     └── ligne « Instagram Neva »
```

Une **unité mère** porte l'idée ; chaque **ligne** porte sa déclinaison sur un canal. Le champ `N°` (décimal : 11.1, 11.2, 11.3) donne la séquence à l'intérieur de l'unité.

### Les 4 vues actives

| Vue | Ce qu'elle montre |
|---|---|
| **01 — PLAN PAR UNITÉ** | Tout, groupé par `Unité mère`, trié par `Ordre`. **C'est le plan de production.** |
| **02 — TEXTES PAR PLATEFORME** | Les textes du funnel 27 €, avec `Asset maître`, `Texte final`, `CTA` |
| **03 — MÉTRIQUES APRÈS PUBLICATION** | Vues, Likes, Commentaires, Enregistrements, Partages, Demandes VIDÉO, Leads qualifiés |
| **04 — BANQUE D'IDÉES · HORS FUNNEL** | Tout ce qui n'appartient pas au funnel 27 €. **Destination des captures et des brouillons.** |

### Les champs, par usage

**Identification** — `Sujet` (titre) · `Unité mère` · `Compte / Canal` · `N°` · `Plateforme` · `Project 1`
**Repérage** — `Date de capture` (automatique, ajoutée le 28/08 : date et heure exactes de chaque capture)
**Cadrage éditorial** — `Pilier` · `Catégorie` · `Pain` · `Solution` · `Advanced JTBD` · `Rôle plateforme`
**Écriture** — `Hook` · `Instagram` · `LinkedIn` · `Texte final` · `Newsletter`
**Format** — `Format Instagram` · `Format LinkedIn` · `Asset maître` · `Canva` · `Drive`
**Conversion** — `CTA` · `Lead Magnet` · `Conversion / Funnel`
**Publication** — `Statut` · `Timing` · `Date publication` · `URL publication`
**Mesure** — `Vues` · `Likes` · `Commentaires` · `Enregistrements` · `Partages` · `Demandes VIDÉO` · `Leads qualifiés`

### Statuts

`Idée capturée` → `Rédigé` → `À valider` → `En production` → `Prêt` → `Publié`

Le passage à **`Rédigé`** n'est légitime qu'une fois les 6 étapes de la chaîne de rédaction faites (voir §5 bis).

### Champs à nettoyer

`Column 2` · `Project 2` · `Project 3` · `Semaine` (S1–S4, hérités de l'ancienne stratégie immobilière, jamais remplis).

---

## 5 bis. La chaîne de rédaction d'un post — 6 étapes obligatoires

> Procédure complète : `07-SYSTEMES-ET-PROCESS/PIPELINE-REDACTION-POST.md` (règle permanente du 21/08).

Aucun post ne s'écrit d'un seul jet. Chaque étape est confiée au spécialiste :

| # | Étape | Skill / agent | Va dans |
|---|---|---|---|
| 1 | **Hook** | `final-builder` | `Hook` |
| 2 | **Douleur client** | `marketing-psychology` | `Pain` |
| 3 | **Advanced JTBD** | `nmt-craft-value-proposition` | `Advanced JTBD` |
| 4 | **Body** | `prodai-content-creator` | `Instagram` · `LinkedIn` |
| 5 | **Angle par plateforme** | `content-marketing` | `Format Instagram` · `Format LinkedIn` |
| 6 | **CTA** | `lead-magnet-funnel-builder` | `CTA` · `Lead Magnet` · `Conversion / Funnel` |

**Trois règles qui font la différence :**

1. **Le hook s'écrit en premier mais se valide en dernier.** Une fois le body écrit, le vrai hook est presque toujours *dans* le texte. Repasser par `final-builder` après l'étape 4.
2. **Capture ≠ rédaction.** Le bot ne fait que capturer. Il n'invente ni hook, ni CTA, ni lead magnet. La chaîne ne démarre que sur décision explicite.
3. **Rien ne s'invente hors de ce qu'a dit Katerina.** Si une information manque, on la demande — on ne la comble pas.

## 6. Definition of Done

Une unité est prête quand :

- [ ] le sujet est approuvé ;
- [ ] le déplacement A→B est clair ;
- [ ] les **deux hooks** sont fonctionnels (le visuel marche sans le son) ;
- [ ] le body apporte une **méthode**, pas une opinion ;
- [ ] le Point B est **autonome** (utile sans téléchargement) ;
- [ ] le lead magnet accomplit réellement la prochaine tâche ;
- [ ] Instagram et LinkedIn sont adaptés **séparément** ;
- [ ] les affirmations sont vérifiées et sourcées ;
- [ ] le CTA est **unique** ;
- [ ] le temps de production est tracé (`Temps total`) ;
- [ ] l'approbation humaine est obtenue.

---

## 7. Ce qui est repris du pipeline 9×16, et ce qui est écarté

**À reprendre :** hook en moins de 3 secondes · compréhension sans le son · arc A→B · continuité · storyboard · visual lock · voice lock · test de quelques plans avant production en série · human approval · analytics · apprentissage documenté.

**À écarter :** cliffhanger artificiel · conflit mélodramatique · hyperbole non soutenue par le vécu · twist sans valeur pédagogique · dépendance à un personnage fictif au détriment de l'autorité de Katerina.

---

## 8. Les skills mobilisés

| Étape | Skill | Évolution prévue |
|---|---|---|
| Capture | `insight-capture-protocol` + bot Telegram | Préserver le verbatim, ajouter l'ID d'idée mère |
| Sujet et ordre | `content-strategy` | Contrôle des doublons, place dans l'arc |
| Transformation A→B | `nmt-craft-value-proposition` | Wrapper éditorial Advanced JTBD |
| Narration | `scenario-9x16` · `hook-9x16` · `structure-virale-9x16` | Arc, hook, continuité — sans mélodrame |
| Voix | `04-TONE-OF-VOICE-KATERINA-NEVA.md` | Voice Lock, interdits, disclosure |
| Rédaction | `copywriting` · `prodai-content-creator` | Adapter à la fiche narrative validée |
| Plateformes | `social` | Deux versions natives depuis une idée mère |
| Lead magnet | `lead-magnets` | Point B → prochaine tâche → actif |
| Conversion | `marketing-loops` | Instagram et LinkedIn distincts |
| Newsletter | `emails` | L'idée mère devient un approfondissement |
| Visuel | `05-STYLE-SYSTEM-VIDEO-NEVA.md` + Canva/HeyGen | Storyboard, visual lock, test pilote |
| Mesure | `analytics` · `ab-testing` | ROI éditorial par idée mère |

---

## 9. Boucle d'apprentissage

```
Observation → diagnostic → hypothèse → changement contrôlé → résultat → décision
```

- Leçon confirmée → `07-SYSTEMES-ET-PROCESS/LESSONS.md`
- Nouvelle procédure répétable → le skill concerné
- Changement de séquence → **ce document**
- Changement stratégique → `00-COCKPIT.md`

**Indicateur central :** `leads qualifiés / temps total de production`.
⚠️ Aujourd'hui non calculable : `Temps total` et `Résultat` ne sont remplis sur aucune ligne.

---

## 10. Garde-fous

- Un contenu = **une plateforme native + un format + une micro-conversion**.
- Aucune création Canva avant validation humaine.
- Ne jamais transformer un pilote en preuve client définitive.
- Copier les **mécanismes** des benchmarks, jamais leurs textes, marques ou promesses.
- Aucune affirmation sur un outil sans vérification **au moment de publier**.
- Aucun automatisme avant validation d'un pilote manuel.
