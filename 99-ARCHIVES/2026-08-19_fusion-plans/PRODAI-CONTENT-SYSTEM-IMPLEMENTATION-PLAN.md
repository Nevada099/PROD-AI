> ⚠️ **DOCUMENT REMPLACÉ le 19/08/2026.** Fusionné dans `07-SYSTEMES-ET-PROCESS/PLAN-IMPLEMENTATION-CONTENT-SYSTEM.md`.

# PROD’AI Content System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construire et tester un workflow éditorial qui transforme une idée vécue en contenus Instagram/LinkedIn, lead magnet, newsletter, orientation Lab/Academy et mesure de ROI.

**Architecture:** Studio IA garde le canon; `SKILLS & PIPELINES/PRODAI-CONTENT-SYSTEM` porte les procédures; Notion conserve une idée mère par ligne avec deux colonnes éditoriales distinctes; les productions visuelles sont déclenchées seulement après validation.

**Tech Stack:** Markdown local, Notion, ChatPlace, email, Canva, HeyGen, captures d’écran, analytics par liens UTM et ID d’idée mère.

**Spec:** `studio-ia-migration/05-MARQUE-ET-CONTENU/CONTENT-CREATION-SYSTEM/00-ARCHITECTURE-CANONIQUE.md`

## Global Constraints

- Transformation personnelle avant conséquence professionnelle.
- Hook visuel compréhensible sans le son.
- Une idée mère par ligne Notion; Instagram et LinkedIn dans deux colonnes distinctes.
- Point B utile sans téléchargement.
- Un CTA par unité.
- Aucun automatisme avant validation d’un pilote manuel.
- Aucune affirmation récente sur un outil sans vérification au moment de publier.

---

### Task 1: Canon et pipeline local

**Files:**
- Create: `studio-ia-migration/05-MARQUE-ET-CONTENU/CONTENT-CREATION-SYSTEM/00-ARCHITECTURE-CANONIQUE.md`
- Create: `SKILLS & PIPELINES/PRODAI-CONTENT-SYSTEM/00-MASTER-PIPELINE.md`

- [x] Formaliser la décision narrative et les huit gates.
- [x] Cartographier les skills existants et les trois évolutions nécessaires.
- [x] Ajouter `TONE-OF-VOICE-KATERINA-NEVA.md` après analyse de plusieurs textes bruts français et russes.
- [ ] Ajouter `LESSONS.md` lors du premier pilote publié.

### Task 2: Restructuration non destructive de Notion

**Data source:** `collection://3987299b-2234-8009-b32a-000b4c508db9`

- [ ] Ajouter `Ordre`, `Pilier`, `Instagram`, `Format Instagram`, `LinkedIn`, `Format LinkedIn`, `Newsletter`, `ID idée mère`, `Temps total` et `Résultat`.
- [ ] Conserver les anciennes propriétés et archives sans suppression.
- [ ] Transformer la vue principale en une ligne par idée mère.
- [ ] Afficher Instagram et LinkedIn côte à côte comme colonnes verticales.
- [ ] Insérer les sept sujets approuvés dans l’ordre narratif.
- [ ] Vérifier que les vues Archive et Quarantaine restent intactes.

### Task 3: Fiche Tone of Voice

**File:**
- Create: `studio-ia-migration/05-MARQUE-ET-CONTENU/CONTENT-CREATION-SYSTEM/TONE-OF-VOICE-KATERINA-NEVA.md`

- [x] Extraire rythme, dialogues, contradictions, vocabulaire, humour, vulnérabilité et phrases-manifestes.
- [x] Séparer la voix Katerina de la fonction de médiation de Neva.
- [x] Définir les formulations interdites et le test anti-texte-lisse.
- [ ] Faire valider un paragraphe test avant rédaction en série.

### Task 4: Développement du chapitre 1

**File:**
- Create: `studio-ia-migration/05-MARQUE-ET-CONTENU/CONTENT-CREATION-SYSTEM/CHAPITRE-01-PRODUCT-BUILDER.md`

- [ ] Écrire la fiche A→B sans prose finale.
- [ ] Valider hook visuel, hook verbal, body, Point B, pont et CTA.
- [ ] Écrire la version Instagram.
- [ ] Écrire la version LinkedIn.
- [ ] Contrôler chaque version contre le Voice Lock.

### Task 5: AI Operating System Starter Kit MVP

**Files:**
- Create: `studio-ia-migration/05-MARQUE-ET-CONTENU/CONTENT-CREATION-SYSTEM/LEAD-MAGNET-AI-OS-STARTER-KIT.md`

- [ ] Limiter le kit à une carte, un Pipeline Canvas, une arborescence, une règle de classement et une vidéo courte.
- [ ] Donner un aperçu avant la capture email.
- [ ] Ajouter les sorties Explorer, Academy et Lab après la livraison.
- [ ] Tester manuellement la demande avant d’automatiser ChatPlace ou LinkedIn.

### Task 6: Pilote et mesure

- [ ] Attribuer un ID unique au chapitre 1 et à toutes ses déclinaisons.
- [ ] Tracer recherche, rédaction, production et temps total.
- [ ] Tracer portée, abonnés, mots-clés, clics, emails, consommation et orientation Lab/Academy.
- [ ] Calculer `leads qualifiés / temps total de production`.
- [ ] Documenter la décision : répéter, corriger ou arrêter.
- [ ] Mettre à jour `LESSONS.md`, le skill concerné ou le Master Pipeline.
