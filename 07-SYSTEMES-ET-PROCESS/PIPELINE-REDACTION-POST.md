# ✍️ Pipeline de rédaction d'un post — chaîne obligatoire

**Créé le 21 août 2026 · Règle permanente pour tout agent qui rédige du contenu Neva / PROD'AI**

Aucun post ne s'écrit d'un seul jet. On passe par **6 étapes, dans cet ordre**, chacune confiée au skill ou à l'agent qui en est le spécialiste.

---

## La chaîne

| # | Étape | Skill / agent | Produit | Colonne Notion |
|---|---|---|---|---|
| 1 | **Hook** | `final-builder` (agent) | Plusieurs accroches neuves, jamais recyclées. On en garde une. | `Hook` |
| 2 | **Client pain** | `marketing-skills:marketing-psychology` | La douleur telle que le lecteur la vit, pas telle que l'experte la voit. | corps de page |
| 3 | **Advanced JTBD** | `nmt-craft-value-proposition` | AJTBD (Zamesin) : Job Graph, chaîne critique des jobs, critères de succès du segment. | corps de page |
| 4 | **Body** | `prodai-content-creator` | Le corps du texte, dans le Tone of Voice de Katerina / Neva. | `Instagram` · `LinkedIn` |
| 5 | **Angle** | `content-marketing` (agent) | Deux déclinaisons réellement différentes, une par plateforme. | `Plateforme` · `Format Instagram` · `Format LinkedIn` |
| 6 | **CTA** | `lead-magnet-funnel-builder` (agent) | Un seul CTA, un seul lead magnet, la chaîne de conversion. | `CTA` · `Lead Magnet` · `Conversion / Funnel` |

Quand les 6 étapes sont faites : `Statut` → **Rédigé**.

---

## Les trois règles qui font la différence

**1. Le hook s'écrit en premier, mais se valide en dernier.**
Une fois le body écrit, le vrai hook se trouve presque toujours *dans* le texte. Le hook de l'étape 1 sert d'amorce ; il est très souvent jeté à la fin. Repasser par `final-builder` après l'étape 4.

**2. Capture ≠ rédaction.**
Le bot @Prodaicontentbot ne fait que capturer. Il n'a pas le droit d'inventer hook, CTA, lead magnet ni format. Cette chaîne ne démarre que sur décision explicite : commande `develop` / `développe` / « развить идею », ou passage manuel du `Statut`.

**3. Rien ne s'invente hors de ce qu'a dit Katerina.**
Aucune étape n'ajoute d'exemple, de chiffre ou de résultat absent du matériau d'origine. Si une information manque, on la demande — on ne la comble pas.

---

## Où atterrit une nouvelle idée — la règle de rangement

*Établie le 01/09 : une fiche apparaissait dans plusieurs vues à la fois et devenait introuvable.*

**Une seule porte d'entrée : la vue `🆕 00 — NOUVEAU · à trier`.**

Elle filtre sur `Statut = Idée capturée` et trie par `Date de capture` décroissante. Tout ce qui arrive — dicté au bot ou écrit par un agent — s'y affiche en haut. C'est le seul endroit à ouvrir pour voir le neuf.

### Le cheminement

```
Nouvelle idée (bot ou agent)
   │  Statut = Idée capturée · Unité mère vide
   ↓
🆕 00 — NOUVEAU · à trier        ← tout arrive ICI
   │  on lui donne Unité mère + N° + Compte / Canal
   ↓
⭐ 01 — PLAN PAR UNITÉ           ← le plan de production
   │  Statut → Rédigé (sort automatiquement de « NOUVEAU »)
   ↓
Publication + Date publication
   ↓
SECONDAIRE — Calendrier  ·  📊 02 — MÉTRIQUES
```

### Pourquoi ça se maintient tout seul

Une fiche **quitte** la vue `NOUVEAU` dès que son statut passe à `Rédigé`. Rien à ranger à la main : le tri se fait en changeant le statut, ce qu'on fait de toute façon.

### Règle pour tout agent qui crée une fiche

Une fiche nouvelle se crée **toujours** avec `Statut = Idée capturée` et `Unité mère` vide. C'est à Katerina de décider du rattachement — c'est son geste de tri, pas celui de l'agent.

⚠️ Ne jamais poser `Date publication` sur une fiche non publiée : elle se retrouverait dans le calendrier au milieu du travail réellement planifié.

---

## De l'idée capturée au texte rédigé — en manuel

Le bot dépose une idée. Voici comment la développer soi-même, dans l'ordre, sans rien inventer.

### Avant d'écrire — rattacher l'idée

| Champ | Ce qu'on met | Pourquoi d'abord |
|---|---|---|
| `Unité mère` | `U12 — <l'idée en 4 mots>` | Tant qu'il est vide, la ligne reste dans « No Unité mère ». C'est le geste de tri. |
| `Compte / Canal` | `Instagram Katerina` · `LinkedIn Katerina` · `Instagram Neva` | Une ligne = **un** canal |
| `N°` | décimal : 28.1, 28.2, 28.3 | Donne la séquence dans l'unité *(colonne ex-`Ordre`)* |

**Si l'idée mérite deux canaux, on duplique la ligne** (`⌘D` sur la ligne dans Notion), on garde la même `Unité mère`, et on change `Compte / Canal` + `N°`. C'est le seul cas où l'on duplique volontairement.

### Puis remplir, dans cet ordre

1. **`Pain`** — la douleur telle que le lecteur la vit, pas telle que l'experte la voit. *Test : est-ce qu'il la reconnaîtrait dans ses propres mots ?*
2. **`Solution`** — le déplacement obtenu, en une phrase. Pas la méthode, le résultat.
3. **`Hook`** — l'accroche. Souvent elle se trouve **dans le verbatim** : relire la note vocale avant d'inventer.
4. **`Instagram`** / **`LinkedIn`** — les deux angles, réellement différents. Instagram montre la scène et la bascule ; LinkedIn développe l'arbitrage et la méthode.
5. **`Format Instagram`** / **`Format LinkedIn`** — le format natif de chaque canal.
6. **`CTA`** — une seule action. **`Lead Magnet`** — un seul actif, ou « AUCUN ».
7. **`Texte final`** — seulement quand tout le reste tient.

Puis `Statut` → **Rédigé**.

### Le garde-fou

**Rien ne s'ajoute qui ne soit pas dans le verbatim.** Aucun chiffre, aucun exemple, aucun résultat inventé pour « enrichir » le texte. Si une information manque, on la demande à Katerina — on ne la comble pas. C'est ce qui distingue un post incopiable d'un post que n'importe quel concurrent pourrait signer.

**Relire contre le Tone of Voice** (`05-MARQUE-ET-CONTENU/04-TONE-OF-VOICE-KATERINA-NEVA.md`) : le texte entre-t-il par une scène ? contient-il un détail concret ? une phrase-verdict ?

---

## Étapes optionnelles

À n'utiliser que si le contenu le justifie, jamais par défaut :

- `marketing-skills:copy-editing` — passe de polissage sur un texte déjà bon
- `audit-histoire` — scoring avant production quand le post devient une vidéo
- `hook-9x16` — si le format final est une vidéo verticale (hook qui tient sans le son)

---

## Références

- Tone of Voice : `05-MARQUE-ET-CONTENU/04-TONE-OF-VOICE-KATERINA-NEVA.md`
- Canon narratif et 8 gates : `05-MARQUE-ET-CONTENU/02-SYSTEME-EDITORIAL.md`
- Stratégie et playbook des formats : `05-MARQUE-ET-CONTENU/01-STRATEGIE-COMMUNICATION-NEVA-KATERINA.md`
- Plan de contenu : `05-MARQUE-ET-CONTENU/03-PLAN-EDITORIAL-SAISON-01.md`
- Base Notion : [Neva Content — Pipeline éditorial](https://app.notion.com/p/3987299b223480428ab6e470cc6bd8ea)
- Bot de capture : `07-SYSTEMES-ET-PROCESS/BOT-CAPTURE-IDEES.md`
