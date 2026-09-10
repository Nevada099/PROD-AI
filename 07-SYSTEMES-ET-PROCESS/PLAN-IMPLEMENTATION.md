# Plan d'implémentation — Content System PROD'AI

> **Plan unique.** Il fusionne les 3 plans qui tournaient en parallèle et se contredisaient :
> `IMPLEMENTATION-PLAN.md` (consolidation Studio IA) · `NEVA-CONTENT-IMPLEMENTATION-PLAN.md` (bot) · `PRODAI-CONTENT-SYSTEM-IMPLEMENTATION-PLAN.md` (canon éditorial).
> Originaux dans `99-ARCHIVES/2026-08-19_fusion-plans/`. **Mise à jour : 19 août 2026.**

**Objectif :** transformer une idée vécue en contenus Instagram + LinkedIn, lead magnet, newsletter, orientation Lab/Academy et mesure de ROI.

**Architecture :** ce dossier `Prod'AI/` est la source documentaire unique · Notion est le cockpit opérationnel (une ligne = une idée mère) · le bot Telegram alimente Notion · les productions visuelles ne se déclenchent qu'après validation humaine.

**Stack :** Markdown local · Notion · Telegram + n8n · OpenAI (transcription + qualification) · Canva · HeyGen · captures d'écran · UTM par ID d'idée mère.

---

## Contraintes permanentes

- Transformation personnelle avant conséquence professionnelle.
- Hook visuel compréhensible **sans le son**.
- Une idée mère par ligne Notion ; Instagram et LinkedIn dans deux colonnes distinctes.
- Point B utile **sans téléchargement**.
- Un seul CTA par unité.
- Aucun automatisme avant validation d'un pilote manuel.
- Aucune affirmation sur un outil sans vérification au moment de publier.

---

## Chantier 1 — Canon documentaire ✅ TERMINÉ

- [x] Formaliser la décision narrative et les 8 gates.
- [x] Cartographier les skills et leurs évolutions.
- [x] Écrire le Tone of Voice à partir de textes bruts FR et RU.
- [x] **Fusionner les documents redondants** (19/08) : 5 docs de communication → `01`, 4 docs de système → `02`, 2 plans de contenu → `03`, 3 benchmarks → 1, 3 plans → celui-ci.
- [x] Consolider `studio-ia-migration` dans l'arborescence `Prod'AI/`.
- [ ] Créer `LESSONS.md` lors du premier pilote publié.

## Chantier 2 — Bot de capture ✅ ACTIF

*Documentation complète et journal des corrections : `BOT-CAPTURE-IDEES.md`.*

- [x] Bot `@Prodaicontentbot` créé, workflow n8n publié (17 nœuds).
- [x] Routage voix / texte / commande.
- [x] Transcription Whisper FR + qualification éditoriale IA.
- [x] Création de la ligne Notion en Quarantaine, verbatim conservé dans le corps de page.
- [x] Garde-fou anti-silence (rejet des artefacts Whisper).
- [ ] Tester 20 entrées FR réelles, dont voix bruitée, texte court et idée multi-plateforme.
- [ ] Boutons Telegram ✅ Approuver / ♻️ Reformuler / 🗑 Jeter.

## Chantier 3 — Nettoyage Notion ⏳ À FAIRE

**Base :** `collection://3987299b-2234-8009-b32a-000b4c508db9`

- [ ] Supprimer les 8 lignes vides (ID 1–8) de l'Archive historique.
- [ ] Supprimer les propriétés mortes : `Column 2`, `Project 1`, `Project 2`, `Project 3`, `Semaine`.
- [ ] Sortir les 30 textes de Quarantaine → les rattacher aux 7 chapitres comme **matière première**, pas comme posts.
- [ ] Renommer leur statut `Rédigé` → ce sont des synopsis de 187 à 744 caractères, pas des publications.
- [ ] Fusionner les doublons de plateforme (30 lignes → 15 idées mères).
- [ ] Remplir `Ordre` sur les 7 chapitres de la Saison 1.

## Chantier 4 — Personnage Neva ⛔ BLOQUANT

*Rien ne peut être produit en vidéo tant que ce chantier n'est pas fait.*

- [ ] Remplir le passeport : bible, arc, voix, visual lock (aujourd'hui vides).
- [ ] Trancher la contradiction : `offre.md` dit « danseuse », le reste du corpus dit « avatar PROD'AI ».
- [ ] Croiser la palette provisoire du style system avec `Brand/BRAND-AUDIT-ET-REFONTE.md` (« Cuivre & Encre »).
- [ ] Choisir et figer le casting HeyGen (seed, visage, voix).

## Chantier 5 — Funnel ⛔ BLOQUANT

- [ ] **Nommer l'outil de capture email.** Aujourd'hui aucun lead ne peut atterrir nulle part.
- [ ] Réduire à 1 bibliothèque Notion modulaire + 2 actifs autonomes maximum.
- [ ] Donner un aperçu avant la capture email.
- [ ] Ajouter les sorties Explorer / Academy / Lab après la livraison.
- [ ] Tester le parcours complet **à la main** avant d'automatiser.

## Chantier 6 — Production Canva

- [ ] Sélectionner un modèle de marque compatible autofill (carrousel + visuel statique).
- [ ] Mapper les champs Notion vers le modèle.
- [ ] Ne déclencher Canva qu'au statut `En production`, après validation.
- [ ] Réécrire le lien Canva dans la fiche Notion.
- [ ] Router `Vidéo Neva` vers script/storyboard et `Démo écran` vers plan de capture.
- [ ] Tester 3 unités avant tout traitement en série.

## Chantier 7 — Le pilote (le vrai test)

**Chapitre 1 uniquement, de bout en bout.**

- [ ] Attribuer un ID unique au chapitre 1 et à toutes ses déclinaisons.
- [ ] Écrire la fiche A→B, valider les deux hooks.
- [ ] Écrire la version Instagram, puis la version LinkedIn.
- [ ] Contrôler chaque version contre le Voice Lock.
- [ ] Tracer recherche, rédaction, production et `Temps total`.
- [ ] Tracer portée, mots-clés, clics, emails et orientation Lab/Academy.
- [ ] Calculer `leads qualifiés / temps total de production`.
- [ ] Documenter la décision : répéter, corriger ou arrêter.
- [ ] Mettre à jour `LESSONS.md` et le document concerné.

> **Learning Gate :** tant que ce pilote n'est pas mesuré, aucune production en série.

---

## Chantiers hérités — consolidation Studio IA

- [x] Auditer le dossier existant et les pages Notion.
- [x] Valider l'architecture avec Katerina.
- [x] Créer les sections et documents de pilotage.
- [ ] Ajouter la distinction Lab/Academy au hub Notion.
- [ ] Relier Formation Qualiopi à Academy sans dupliquer son projet.
- [ ] Lancer les agents d'audit avec responsabilités séparées.
