# Neva Content Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Capturer une idée vocale ou textuelle en moins de cinq minutes, la transformer en unités Instagram/LinkedIn et préparer son actif Canva ou avatar.

**Architecture:** Telegram reçoit voix ou texte; n8n transcrit et structure; Notion conserve une unité par plateforme; Canva reçoit uniquement les unités validées compatibles. Les vidéos Neva utilisent un pipeline avatar séparé.

**Tech Stack:** Telegram Bot API, n8n Cloud, transcription OpenAI, LLM structuré, Notion, Canva MCP, Drive.

**Spec:** `Studio IA/05-MARQUE-ET-CONTENU/NEVA-CONTENT-SYSTEM.md`

## Global Constraints

- Une base Notion unique et neuf champs visibles.
- Trois catégories seulement au lancement.
- Aucune création Canva avant validation humaine.
- Une idée multi-plateforme crée deux unités adaptées.
- Le bot accepte voix et texte.

---

### Task 1: Base éditoriale Notion

- [ ] Auditer les lignes historiques et conserver toutes les données.
- [ ] Renommer la base et le champ titre.
- [ ] Ajouter Catégorie, Texte final, Drive et Canva.
- [ ] Remplacer le format historique par le format MVP sans supprimer les anciennes valeurs.
- [ ] Limiter la vue principale aux neuf champs validés.
- [ ] Ajouter le schéma d’interaction sous la base.
- [ ] Créer les premières unités et vérifier leur rendu.

### Task 2: Bot Telegram Neva Content

- [ ] Créer un bot dédié avec BotFather et stocker son token dans les credentials n8n.
- [ ] Dupliquer les briques éprouvées du workflow vocal existant sans réutiliser sa destination Tasks.
- [ ] Router texte et vocal vers le même objet structuré.
- [ ] Transcrire le vocal et produire le JSON `sujet, categorie, plateforme, format, texte_final, lead_magnet`.
- [ ] Créer une ou deux unités Notion selon la plateforme.
- [ ] Envoyer les boutons Valider, Modifier et Garder comme idée.
- [ ] Tester 20 entrées FR, dont voix bruitée, texte court et idée multi-plateforme.

### Task 3: Canva et production

- [ ] Sélectionner un modèle de marque compatible autofill pour carrousel et visuel statique.
- [ ] Mapper les champs Notion vers le modèle Canva.
- [ ] Déclencher Canva uniquement au statut En production après validation.
- [ ] Réécrire le lien Canva dans la fiche Notion.
- [ ] Router Vidéo Neva vers script/storyboard et Démo écran vers plan de capture.
- [ ] Tester trois unités avant tout traitement en série.

